#!/usr/bin/env bash
# Builds every deployed specification branch with a given set of tools, and diffs two builds.
#
# A tool or version change must not alter what Beckn domains generate. Build all branches with
# the current tools (BASE), build them again with the changed tools (NEW), then diff:
#
#   golden.sh list > tooling/golden/branches.lock      # pin each draft/release branch to a commit
#   golden.sh build /tmp/golden-base                   # tools from tooling/ (tooling/versions.env)
#   golden.sh build /tmp/golden-new /path/to/tooling   # a tooling dir with the changed tools
#   golden.sh diff /tmp/golden-base /tmp/golden-new    # exit 1 on any unexplained difference
#
# Environment:
#   GOLDEN_JOBS   parallel builds (default 4)
#   GOLDEN_ONLY   regex; build only branches whose name matches
#
# What is compared, per branch: build.yaml, the RAG table, the generated API-service config,
# schemas, L1 validation code, Dockerfile and compose files, the step exit codes, and the
# documents automation-db would store (capture-ingest.mjs). The cloned plugin sources and the
# build log are kept out of the comparison.

set -euo pipefail

HERE="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
REPO="$(cd "$HERE/../.." && pwd)"
LOCK="$HERE/branches.lock"
EXPLAINED="$HERE/explained-diffs.yaml"

info() { echo "  [info]  $*" >&2; }
die()  { echo "  [error] $*" >&2; exit 1; }

# ── list ─────────────────────────────────────────────────────────────────────
# Deployed branches are the long-lived draft-* and release-* branches that carry both a config
# and the deploy workflow. Deprecated and backup copies are skipped.
cmd_list() {
  git -C "$REPO" fetch -q origin
  git -C "$REPO" for-each-ref --format='%(refname:short)' refs/remotes/origin |
    grep -E '^origin/(draft|release)-' |
    grep -viE 'deprecat|depricat|backup' |
    while read -r ref; do
      if git -C "$REPO" cat-file -e "${ref}:config/index.yaml" 2>/dev/null &&
         git -C "$REPO" cat-file -e "${ref}:.github/workflows/deploy-eks.yml" 2>/dev/null; then
        echo "${ref#origin/} $(git -C "$REPO" rev-parse "$ref")"
      fi
    done
}

# ── build ────────────────────────────────────────────────────────────────────
build_one() {
  local name="$1" sha="$2" out="$3" tooling="$4"
  local dest="$out/$name" work
  work="$(mktemp -d)"
  mkdir -p "$dest"

  git -C "$REPO" archive "$sha" config | tar -x -C "$work"
  # The generator's scripts run ./node_modules/.bin/ondc-code-generator from the working
  # directory, so linking the tooling here pins the code generator too.
  ln -s "$tooling/node_modules" "$work/node_modules"

  (
    cd "$work"
    run() { local step="$1"; shift; if "$@" >>log.txt 2>&1; then echo "$step=0"; else echo "$step=$?"; fi >>status.txt; }
    run parse ./node_modules/.bin/ondc-tools parse -i config -o build.yaml
    run validate ./node_modules/.bin/ondc-tools validate -i build.yaml
    # Fixed placeholder environment, so generated config depends only on the spec and tools.
    run generate env IS_ONIX_ENABLED=true PORT=7039 REDIS_HOST=redis REDIS_PORT=6379 \
      REDIS_PASSWORD=golden CONFIG_SERVICE_URL=http://config MOCK_SERVER_URL=http://mock \
      RECORDER_SERVICE_HTTP_URL=http://recorder RECORDER_SERVICE_GRPC_URL=recorder:8090 \
      ./node_modules/.bin/ondc-api-service-generator --config ./build.yaml
    run rag ./node_modules/.bin/ondc-tools gen-rag-table -i build.yaml -o generated
    if [ -f build.yaml ]; then
      run ingest sh -c "node '$HERE/capture-ingest.mjs' build.yaml '$tooling' > ingest.json"
    fi
  )

  cp "$work/status.txt" "$dest/status.txt"
  cp "$work/log.txt" "$dest/log.txt" 2>/dev/null || true
  for f in build.yaml generated/raw_table.json ingest.json \
           build-output/Dockerfile build-output/docker-compose.yml build-output/docker-entrypoint.sh \
           build-output/temp/config build-output/temp/schemas build-output/temp/validationpkg \
           build-output/temp/validPaths.json build-output/temp/page build-output/temp/readme.md; do
    if [ -e "$work/$f" ]; then
      mkdir -p "$dest/$(dirname "$f")"
      cp -R "$work/$f" "$dest/$f"
    fi
  done
  rm -rf "$work"
  echo "$name $(tr '\n' ' ' <"$dest/status.txt")"
}

cmd_build() {
  local out="${1:?usage: golden.sh build OUT_DIR [TOOLING_DIR]}"
  local tooling="${2:-$REPO/tooling}"
  [ -f "$LOCK" ] || die "missing $LOCK; run: golden.sh list > $LOCK"
  [ -x "$tooling/node_modules/.bin/ondc-tools" ] || die "no tools in $tooling; run: npm ci --prefix $tooling"
  tooling="$(cd "$tooling" && pwd)"
  mkdir -p "$out"
  out="$(cd "$out" && pwd)"

  # The code generator pipes every generated Go file through gofmt, which has been seen to hang
  # on large domains. Formatting does not change what is compared, so by default a stub gofmt
  # that fails is put first on PATH; the generator then keeps its unformatted code, as it does
  # when gofmt is missing. GOLDEN_GOFMT=1 keeps the real gofmt.
  if [ "${GOLDEN_GOFMT:-0}" != "1" ]; then
    local stub
    stub="$(mktemp -d)"
    printf '#!/bin/sh\nexit 1\n' >"$stub/gofmt"
    chmod +x "$stub/gofmt"
    export PATH="$stub:$PATH"
  fi

  {
    echo "tooling=$tooling"
    echo "gofmt=${GOLDEN_GOFMT:-0}"
    (cd "$tooling" && npm ls --depth=0 2>/dev/null || true)
  } >"$out/MANIFEST.txt"

  export -f build_one
  export REPO HERE GOLDEN_OUT="$out" GOLDEN_TOOLING="$tooling"
  grep -E "${GOLDEN_ONLY:-.}" "$LOCK" |
    xargs -P "${GOLDEN_JOBS:-4}" -L 1 bash -c 'build_one "$1" "$2" "$GOLDEN_OUT" "$GOLDEN_TOOLING"' _
  info "built $(find "$out" -mindepth 1 -maxdepth 1 -type d | wc -l | tr -d ' ') branches into $out"
}

# ── diff ─────────────────────────────────────────────────────────────────────
cmd_diff() {
  local base="${1:?usage: golden.sh diff BASE_DIR NEW_DIR}" new="${2:?usage: golden.sh diff BASE_DIR NEW_DIR}"
  local report="$new/_diff" unexplained=0
  rm -rf "$report"
  mkdir -p "$report"

  for dir in "$base"/*/ "$new"/*/; do basename "$dir"; done | grep -v '^_diff$' | sort -u |
    while read -r name; do
      if diff -r -x log.txt "$base/$name" "$new/$name" >"$report/$name.diff" 2>&1; then
        rm "$report/$name.diff"
      fi
    done

  for file in "$report"/*.diff; do
    [ -e "$file" ] || continue
    local name
    name="$(basename "$file" .diff)"
    if node "$HERE/explained.mjs" "$EXPLAINED" "$name" "$file" "$base" "$new"; then
      echo "explained    $name"
    else
      echo "UNEXPLAINED  $name   ($file)"
      unexplained=$((unexplained + 1))
    fi
  done

  if [ "$unexplained" -gt 0 ]; then
    die "$unexplained branch(es) changed without an entry in $EXPLAINED"
  fi
  info "no unexplained differences"
}

case "${1:-}" in
  list)  shift; cmd_list "$@" ;;
  build) shift; cmd_build "$@" ;;
  diff)  shift; cmd_diff "$@" ;;
  *) sed -n '2,20p' "$0"; exit 2 ;;
esac

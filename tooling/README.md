# Pinned build tooling

Every specification branch is built into an API service with the same, exactly pinned tools:

| File | Holds |
|---|---|
| `versions.env` | The pinned versions, plus the plugin commit and ONIX image digest |
| `package.json`, `package-lock.json` | The npm tools at those versions (`npm ci` installs them) |
| `golden/` | The every-domain diff that guards a version bump |

The deploy and spec workflows check out this folder from `main` and run the tools from
`./node_modules/.bin`, never `npx …@latest`. The generator's scripts call
`./node_modules/.bin/ondc-code-generator` from the working directory, so the code generator is
pinned by the same install.

## Bumping a tool

1. Change the version in both `versions.env` and `package.json`, then run `npm install` here to
   update the lockfile.
2. Open a PR. `.github/workflows/pwb-golden.yml` builds every branch in `golden/branches.lock`
   with `main`'s tools and with the PR's tools, and fails on any difference that
   `golden/explained-diffs.yaml` does not approve.

## Running the golden diff locally

```bash
npm ci --prefix tooling
tooling/golden/golden.sh list > tooling/golden/branches.lock   # refresh pinned branches
tooling/golden/golden.sh build /tmp/golden-base                # current tools
tooling/golden/golden.sh build /tmp/golden-new /path/to/other/tooling
tooling/golden/golden.sh diff /tmp/golden-base /tmp/golden-new
```

`GOLDEN_JOBS` sets parallelism (default 4); `GOLDEN_ONLY` limits the run to matching branches.

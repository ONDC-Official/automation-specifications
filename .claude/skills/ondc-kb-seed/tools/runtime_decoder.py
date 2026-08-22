#!/usr/bin/env python3
"""
Tool D2 — runtime decoder (deterministic).

The config's per-step logic ships as **base64-encoded JS** under
`steps[<action_id>].mock.{generate,validate,requirements}`. Nothing else in the
pipeline decodes it, so ~26 MB of grounded runtime semantics was invisible to
Stage E: required fields, structural rules, error codes, step preconditions,
which payload paths a step populates, and which runtime helpers it calls.

This tool decodes every block, dedupes by content hash, and extracts structured
facts that Stage E can turn into atoms **without guessing**.

Basis discipline (important — the sandbox is a stub):
  * The config *declares* this logic, so a fact read out of it is `basis:declared`
    grounded at the positional node-path of the block. It is NOT `sandbox-tested`:
    that basis means the code was *executed* and needs an observation ref.
    `runtime_probe.py` is what produces those.
  * Literal fixture values inside `generate` ("xyz.com", "SHAHEED_STHAL") are stub
    data, never protocol truth. They are captured under `defaults` for context and
    must not be asserted as facts.

Output: knowledge/_work/runtime-decoded.json
Exit 0 always (a decode failure is reported, never fatal).
"""
import os, re, sys, json, glob, base64, hashlib, collections
import _env, _yaml

FN_KEYS = ("generate", "validate", "requirements")
# Helper API exposed to `generate` scope. Verified against
# packages/automation-mock-runner-lib/src/lib/helpers/ (not from prose).
HELPERS = ("getSubscriberUrl", "uuidv4", "generate6DigitId", "currentTimestamp",
           "isoDurToSec", "setCityFromInputs", "createFormURL", "generateConsentHandler")
B64_RE = re.compile(r"^[A-Za-z0-9+/=\s]+$")


def walk_blocks(node, path=""):
    """Yield (node-path, key, base64-string) for every embedded function block.

    Four kinds, not three: besides mock.{generate,validate,requirements}, the
    `saveData` map hides a fourth — a value may be `EVAL#<base64>`, a custom
    getSave(payload) extractor run instead of a JSONPath. Those are real step
    logic and were invisible until this was added."""
    if isinstance(node, dict):
        for k, v in node.items():
            if k in FN_KEYS and isinstance(v, str):
                yield f"{path}.{k}", k, v
            elif isinstance(v, str) and v.startswith("EVAL#"):
                yield f"{path}.{k}", "getSave", v[len("EVAL#"):]
            else:
                yield from walk_blocks(v, f"{path}.{k}")
    elif isinstance(node, list):
        for i, v in enumerate(node):
            # prefer a stable id over a positional index (invariant: never a line number)
            key = None
            if isinstance(v, dict):
                for f in ("action_id", "id", "_NAME_", "name", "code"):
                    if v.get(f):
                        key = str(v[f]); break
            yield from walk_blocks(v, f"{path}[{key}]" if key else f"{path}[{i}]")


def decode(b64):
    s = (b64 or "").strip()
    if len(s) < 40 or not B64_RE.fullmatch(s):
        return None
    try:
        return base64.b64decode(s).decode("utf-8")
    except Exception:
        return None


def paths_from_validate(js):
    """Required payload paths + error codes asserted by a validate() block."""
    req, codes, struct = [], set(), []
    # ["context","bpp_id"] style segment arrays
    for m in re.finditer(r'\[\s*((?:"[^"]+"\s*,\s*)+"[^"]+")\s*\]', js):
        segs = [x.strip().strip('"') for x in m.group(1).split(",")]
        if segs and segs[0] in ("context", "message", "error"):
            req.append(".".join(segs))
    # dotted access on the payload argument
    for m in re.finditer(r'targetPayload\.((?:[A-Za-z_$][\w$]*\.){1,6}[A-Za-z_$][\w$]*)', js):
        req.append(m.group(1))
    for m in re.finditer(r'code:\s*["\']?(\d{3,5})["\']?', js):
        codes.add(m.group(1))
    # human-readable assertion text is the best summary of a structural rule
    for m in re.finditer(r'description:\s*[\'"]([^\'"]{8,160})[\'"]', js):
        struct.append(m.group(1))
    return sorted(set(req)), sorted(codes), struct


def facts_from_requirements(js):
    """Session keys / user inputs a step requires before it may run."""
    sess, inputs, codes = [], [], set()
    for name, bucket in (("requiredSession", sess), ("requiredInputs", inputs)):
        m = re.search(name + r'\s*=\s*\[([^\]]*)\]', js, re.S)
        if m:
            bucket.extend(x.strip().strip('"\'') for x in m.group(1).split(",") if x.strip())
    for m in re.finditer(r'sessionData\.([A-Za-z_$][\w$]*)', js):
        if m.group(1) not in ("user_inputs",):
            sess.append(m.group(1))
    for m in re.finditer(r'code:\s*["\']?([A-Z0-9_]{3,40})["\']?', js):
        codes.add(m.group(1))
    return sorted(set(x for x in sess if x)), sorted(set(x for x in inputs if x)), sorted(codes)


def facts_from_generate(js):
    """Which payload paths the step populates, helpers used, session reads, stub defaults."""
    sets, used, reads, defaults = [], [], [], []
    for m in re.finditer(r'defaultPayload\.((?:[A-Za-z_$][\w$]*\.){0,8}[A-Za-z_$][\w$]*)\s*=', js):
        sets.append(m.group(1))
    for h in HELPERS:
        if re.search(r'\b' + h + r'\s*\(', js):
            used.append(h)
    for m in re.finditer(r'(?:sessionData|user_input)\??\.([A-Za-z_$][\w$]*)', js):
        reads.append(m.group(1))
    # `?? "literal"` — sandbox fixture values. Context only; never asserted.
    for m in re.finditer(r'\?\?\s*"([^"]{1,60})"', js):
        defaults.append(m.group(1))
    return sorted(set(sets)), sorted(set(used)), sorted(set(reads)), sorted(set(defaults))


def run():
    out = {"_tool": "runtime_decoder", "books": {}}
    seen = {}                       # sha1 -> first (book, node) that carried it
    totals = collections.Counter()
    for cfg_root in sorted(glob.glob(os.path.join(_env.CONFIGS, "*"))):
        cfg = os.path.join(cfg_root, "config")
        if not os.path.isdir(cfg):
            continue
        bid = _env.book_id(cfg_root)
        blocks, failed = [], 0
        for f in sorted(glob.glob(os.path.join(cfg, "**", "*.yaml"), recursive=True)):
            doc, err = _yaml.load_file(f)
            if err or doc is None:
                continue
            rel = os.path.relpath(f, cfg)
            for node, kind, b64 in walk_blocks(doc):
                js = decode(b64)
                if js is None:
                    failed += 1
                    continue
                h = hashlib.sha1(js.encode()).hexdigest()[:12]
                totals[kind] += 1
                rec = {"kind": kind, "file": rel, "node": node.lstrip("."), "sha": h,
                       "ground": f"{bid}:{rel}#{node.lstrip('.')}"}
                if h in seen:
                    rec["same_as"] = seen[h]          # dedupe: 9-10x for validate/requirements
                else:
                    seen[h] = rec["ground"]
                    if kind == "validate":
                        r, c, s = paths_from_validate(js)
                        rec.update(requires=r, error_codes=c, assertions=s[:6])
                    elif kind == "requirements":
                        s, i, c = facts_from_requirements(js)
                        rec.update(session_keys=s, user_inputs=i, codes=c)
                    elif kind == "getSave":
                        # what this extractor pulls out of the payload into session state
                        rec["extracts"] = sorted(set(
                            m.group(1) for m in
                            re.finditer(r'payload\.((?:[A-Za-z_$][\w$]*\.){0,6}[A-Za-z_$][\w$]*)', js)))
                    else:
                        st, hp, rd, df = facts_from_generate(js)
                        rec.update(sets_paths=st, helpers=hp, session_reads=rd, defaults=df)
                blocks.append(rec)
        out["books"][bid] = {"blocks": len(blocks), "decode_failures": failed, "items": blocks}
    out["_totals"] = dict(totals)
    out["_distinct"] = len(seen)
    os.makedirs(os.path.dirname(_env.w("runtime-decoded.json")), exist_ok=True)
    with open(_env.w("runtime-decoded.json"), "w", encoding="utf-8") as fh:
        json.dump(out, fh, indent=1)

    print("RUNTIME DECODE (base64 step logic)\n")
    print(f"  {'book':34} {'blocks':>7} {'fail':>5}")
    print("  " + "-" * 50)
    for bid, v in out["books"].items():
        print(f"  {bid:34} {v['blocks']:>7} {v['decode_failures']:>5}")
    print("  " + "-" * 50)
    print(f"  {'TOTAL':34} {sum(v['blocks'] for v in out['books'].values()):>7} "
          f"{sum(v['decode_failures'] for v in out['books'].values()):>5}")
    print(f"\n  by kind: {dict(totals)}")
    print(f"  distinct blocks: {out['_distinct']}  (dedupe collapses the rest)")
    print(f"  -> {_env.w('runtime-decoded.json')}")
    return 0


if __name__ == "__main__":
    sys.exit(run())

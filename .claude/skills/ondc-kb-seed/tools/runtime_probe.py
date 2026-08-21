#!/usr/bin/env python3
"""
Tool D3 driver — converts a flow YAML with the repo's runtime loader and hands it
to `runtime_probe.mjs`, which executes the step logic on the real mock-runner engine.

Split in two because the flow YAML must be read the way the runtime reads it
(js-yaml anchor semantics — see tools/_yaml.py); re-implementing that in Node
would be a second source of truth. Python parses, Node executes.

  runtime_probe.py <flow.yaml> [--json out.json]
  runtime_probe.py --book <book-id> [--limit N]     # probe a whole book's flows

Produces observation records for `basis:sandbox-tested` atoms. Read the header of
runtime_probe.mjs for what the sandbox does and does not prove.
"""
import os, sys, json, glob, shutil, tempfile, subprocess
import _env, _yaml

HERE = os.path.dirname(os.path.abspath(__file__))
MJS = os.path.join(HERE, "runtime_probe.mjs")
LIB = os.path.join(_env.ROOT, "automation-framework/packages/automation-mock-runner-lib/dist/index.js")


def preflight():
    if not shutil.which("node"):
        print("STOP: node not on PATH — the probe executes the real runtime engine.")
        return False
    if not os.path.exists(LIB):
        print("STOP: mock-runner-lib is not built.\n"
              "  cd automation-framework/packages/automation-mock-runner-lib && npm install && npm run build")
        return False
    return True


def probe_flow(path, json_out=None):
    doc, err = _yaml.load_file(path)
    if err or doc is None:
        return {"flow": path, "error": f"yaml: {err}", "observations": []}
    tmp = tempfile.NamedTemporaryFile("w", suffix=".json", delete=False, encoding="utf-8")
    json.dump(doc, tmp, default=str)
    tmp.close()
    out = json_out or tempfile.NamedTemporaryFile(suffix=".json", delete=False).name
    try:
        r = subprocess.run(["node", MJS, tmp.name, "--json", out],
                           capture_output=True, text=True, timeout=300)
        print(r.stdout.rstrip() or r.stderr.rstrip()[:500])
        if os.path.exists(out):
            with open(out, encoding="utf-8") as fh:
                data = json.load(fh)
            data["flow"] = path                      # report the real path, not the temp copy
            return data
        return {"flow": path, "error": (r.stderr or "no output")[:300], "observations": []}
    except subprocess.TimeoutExpired:
        return {"flow": path, "error": "probe timeout (>300s)", "observations": []}
    finally:
        os.unlink(tmp.name)


def main():
    if not preflight():
        return 2
    args = sys.argv[1:]
    if not args:
        print(__doc__)
        return 2
    if args[0] == "--book":
        bid = args[1]
        limit = int(args[args.index("--limit") + 1]) if "--limit" in args else 0
        cfg = None
        for d in glob.glob(os.path.join(_env.CONFIGS, "*")):
            if _env.book_id(d) == bid:
                cfg = os.path.join(d, "config"); break
        if not cfg:
            print(f"STOP: no config book '{bid}'")
            return 2
        flows = sorted(glob.glob(os.path.join(cfg, "flows", "**", "*.yaml"), recursive=True))
        flows = [f for f in flows if os.path.basename(f) != "index.yaml"]
        if limit:
            flows = flows[:limit]
        results = [probe_flow(f) for f in flows]
        out = _env.w(f"runtime-observations-{bid}.json")
        with open(out, "w", encoding="utf-8") as fh:
            json.dump({"book": bid, "flows": results}, fh, indent=1)
        ok = sum(1 for r in results for o in r.get("observations", []) if o.get("ok"))
        tot = sum(len(r.get("observations", [])) for r in results)
        print(f"\n{bid}: flows={len(results)}  executions={tot}  ok={ok}\n-> {out}")
        return 0
    j = args[args.index("--json") + 1] if "--json" in args else None
    probe_flow(args[0], j)
    return 0


if __name__ == "__main__":
    sys.exit(main())

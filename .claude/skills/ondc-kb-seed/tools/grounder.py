#!/usr/bin/env python3
"""
Tool B — Grounder (KEP deterministic spine, B1).
Assign every unit-worthy config node a stable POSITIONAL node-path = its
grounded_in anchor: "<book>:<file>#<node-path>". Node-paths are id-based where an
array item has a natural id (positional, never line numbers) so they survive reorder.
An INDEPENDENT resolver navigates each node-path back to prove round-trip (invariant G-1: 100%).
Input: scope-graphs.json (in-scope files from Tool A). Output: ground-map.json + round-trip report.
"""
import os, sys, json
import _env, _yaml

HERE = os.path.dirname(__file__)
REF = _env.CONFIGS
SCOPE = _env.w("scope-graphs.json")
ID_KEYS = ("action_id", "_NAME_", "code", "id")   # array-item identity, in priority order

def load(p):
    if p.endswith((".yaml", ".yml")):
        return _yaml.load_file(p)
    try:
        with open(p) as f:
            return json.load(f), None
    except Exception as e:
        return None, str(e).splitlines()[0]

def seg_for_item(item, idx):
    """id-based array segment if the item has a natural id, else numeric."""
    if isinstance(item, dict):
        for k in ID_KEYS:
            if k in item and isinstance(item[k], (str,int)):
                return f"[{item[k]}]"
    return f"[{idx}]"

def emit(node, path, kind, out):
    out.append({"node_path": path, "kind": kind})

def ground_file(rel, doc, out):
    """dispatch by file role; emit unit-worthy node-paths."""
    base = os.path.basename(rel)
    if rel.endswith("specs/openapi.yaml"):
        for name in (doc.get("components",{}) or {}).get("schemas",{}) or {}:
            emit(None, f"components.schemas.{name}", "schema", out)
        for p in doc.get("paths",{}) or {}:
            emit(None, f"paths.{p}", "path", out)
    elif rel.endswith("actions/index.yaml"):
        for a in (doc.get("supportedActions",{}) or {}):
            emit(None, f"supportedActions.{a}", "action", out)
    elif rel.endswith("errors/index.yaml"):
        rows = doc.get("code") if isinstance(doc, dict) else doc
        for i, r in enumerate(rows or []):
            emit(None, f"code{seg_for_item(r,i)}", "error", out)
    elif "flows/" in rel and base != "index.yaml":
        for i, s in enumerate((doc or {}).get("steps",[]) or []):
            emit(None, f"steps{seg_for_item(s,i)}", "flow-step", out)
    elif rel.endswith("validations/index.yaml"):
        def walk_t(n, p):
            if isinstance(n, dict):
                if "_NAME_" in n: emit(None, p, "validation", out); return
                for k,v in n.items(): walk_t(v, f"{p}.{k}" if p else k)
            elif isinstance(n, list):
                for i,v in enumerate(n): walk_t(v, f"{p}{seg_for_item(v,i)}")
        walk_t(doc.get("_TESTS_",{}) if isinstance(doc,dict) else {}, "_TESTS_")
    elif "attributes/" in rel and base != "index.yaml":
        def walk_a(n, p):
            if isinstance(n, dict):
                if "_description" in n: emit(None, p, "attribute", out)
                for k,v in n.items():
                    if k != "_description": walk_a(v, f"{p}.{k}" if p else k)
        walk_a(doc, "")

def resolve(doc, node_path):
    """INDEPENDENT navigator: parse node-path, walk doc, return True if node exists."""
    cur = doc
    tok, i = "", 0
    parts = []
    # tokenize into keys and [id] segments
    buf = ""
    while i < len(node_path):
        c = node_path[i]
        if c == ".":
            if buf: parts.append(("key", buf)); buf = ""
        elif c == "[":
            if buf: parts.append(("key", buf)); buf = ""
            j = node_path.index("]", i)
            parts.append(("idx", node_path[i+1:j])); i = j
        else:
            buf += c
        i += 1
    if buf: parts.append(("key", buf))
    for typ, val in parts:
        if typ == "key":
            if isinstance(cur, dict) and val in cur: cur = cur[val]
            else: return False
        else:  # idx: numeric or id-based
            if isinstance(cur, list):
                if val.isdigit() and int(val) < len(cur): cur = cur[int(val)]
                else:
                    hit = None
                    for it in cur:
                        if isinstance(it, dict) and any(str(it.get(k))==val for k in ID_KEYS):
                            hit = it; break
                    if hit is None: return False
                    cur = hit
            else: return False
    return True

def run():
    scope = json.load(open(SCOPE))
    results = {}
    for book_dir, sg in scope.items():
        book = book_dir.split("eks-")[1]
        cfg = os.path.join(REF, book_dir, "config")
        entries, bykind, failed = [], {}, []
        for rel in sg.get("in_scope_files", []):
            if not rel.endswith((".yaml",".yml",".json")): continue
            doc, err = load(os.path.join(cfg, rel))
            if err or doc is None: continue
            out = []
            ground_file(rel, doc, out)
            for e in out:
                gi = f"{book}:{rel}#{e['node_path']}"
                ok = resolve(doc, e["node_path"])      # independent round-trip
                if not ok: failed.append(gi)
                entries.append({"grounded_in": gi, "kind": e["kind"], "resolves": ok})
                bykind[e["kind"]] = bykind.get(e["kind"],0)+1
        total = len(entries); passed = total - len(failed)
        results[book] = {
            "nodes_grounded": total,
            "by_kind": bykind,
            "roundtrip_pass": passed,
            "roundtrip_rate": round(100*passed/total,2) if total else 100.0,
            "failed_sample": failed[:5],
            "sample": [e["grounded_in"] for e in entries[:6]],
        }
    out_path = _env.w("ground-map.json")
    json.dump(results, open(out_path,"w"), indent=2)
    for b, r in results.items():
        print(f"{b}: grounded={r['nodes_grounded']}  round-trip={r['roundtrip_rate']}%  by_kind={r['by_kind']}")
        if r["failed_sample"]: print("   FAILED:", r["failed_sample"])

if __name__ == "__main__":
    run()

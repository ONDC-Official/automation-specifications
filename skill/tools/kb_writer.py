#!/usr/bin/env python3
"""
Tool E→F — Interpretation + KB Writer (KEP). BOOK-GENERIC.
Derives structural KB-storage atoms for ANY config book from its actions + first flow,
interns shared meanings as anchors, writes a KB instance validated by validate_kb.py.
The AI interpretation layer (E) plugs into the same seam to enrich beyond structure.

Usage: python3 kb_writer.py [book_dir]
  book_dir defaults to the first book in scope-graphs.json (Tool A output).
Degrades: if the workbench KB is absent, runtime-meaning atoms are omitted (not faked);
object atoms ground to the book's own openapi schema.
"""
import os, sys, re, glob, json, yaml
import _env
HERE = os.path.dirname(os.path.abspath(__file__))
REFROOT = _env.CONFIGS
CMP = _env.WORK

def norm_book(dirname):
    b = os.path.basename(dirname)
    b = re.sub(r"^automation-specifications-release-eks-", "", b)
    return b.lower()

def pick_book():
    if len(sys.argv) > 1: return sys.argv[1]
    sg = os.path.join(CMP, "scope-graphs.json")
    if os.path.exists(sg):
        for name in json.load(open(sg)):
            hit = glob.glob(os.path.join(REFROOT, "**", name), recursive=True)
            if hit: return hit[0]
    hits = [os.path.dirname(os.path.dirname(p)) for p in
            glob.glob(os.path.join(REFROOT, "**", "config", "index.yaml"), recursive=True)
            if os.path.exists(os.path.join(os.path.dirname(p), "specs", "openapi.yaml"))]
    if not hits: sys.exit("no config book found")
    return hits[0]

def load(p):
    try: return yaml.safe_load(open(p))
    except Exception: return None

def build(book_dir):
    BK = norm_book(book_dir)
    cfg = os.path.join(book_dir, "config")
    OUT = os.path.join(_env.KNOWLEDGE, BK)
    os.makedirs(os.path.join(OUT, "anchors"), exist_ok=True)
    def g(rel, node): return f"grounded-in:{BK}:{rel}#{node}"
    workbench = _env.workbench_kb()
    schemas = ((load(os.path.join(cfg, "specs/openapi.yaml")) or {}).get("components", {}) or {}).get("schemas", {}) or {}
    sup = (load(os.path.join(cfg, "actions/index.yaml")) or {}).get("supportedActions", {}) or {}
    entry = sup.get("null") or sup.get(None) or []
    action_names = [a for a in sup.keys() if a not in (None, "null")]
    flow_files = [f for f in glob.glob(os.path.join(cfg, "flows", "**", "*.yaml"), recursive=True)
                  if os.path.basename(f) != "index.yaml"]
    flow = min(flow_files, key=len) if flow_files else None
    flow_rel = os.path.relpath(flow, cfg) if flow else None
    steps = (load(flow) or {}).get("steps", []) if flow else []

    def h(name): return "anchor." + re.sub(r"[^a-z0-9]+", "-", str(name).lower()).strip("-")
    ATOMS = []
    for obj in ("Provider", "Item", "Payment", "Fulfillment"):
        if obj in schemas:
            ATOMS.append((h(obj), "isa", "anchor.beckn-object", "declared", g("specs/openapi.yaml", f"components.schemas.{obj}")))
    for a in action_names:
        ATOMS.append((h(a), "isa", "anchor.action", "declared", g("actions/index.yaml", f"supportedActions.{a}")))
    for a in entry:  # null-predecessor is in config -> declared + grounded (no workbench needed)
        ATOMS.append((h(a), "isa", "anchor.transaction-entry", "declared", g("actions/index.yaml", "supportedActions.null")))
    if workbench and entry:  # runtime MEANING needs workbench; omit (don't fake) if absent
        ATOMS.append(("anchor.transaction-entry", "isa", "anchor.runtime-concept", "authority",
                      "grounded-in:workbench:frames/flow-state-machine.md"))
    if flow_rel:
        prev = None
        for s in steps:
            if not isinstance(s, dict): continue
            api = s.get("api"); aid = s.get("action_id")
            if prev and api:
                ATOMS.append((h(prev), "precedes", h(api), "declared", g(flow_rel, f"steps[{aid}]")))
            prev = api
    if entry:  # inferred (AI-decoded-JS placeholder) — no grounded-in, quarantined
        ATOMS.append((h(entry[0]), "requires", '"provider-id"', "inferred", None))

    anchors, lines = set(), []
    for s, r, o, basis, extra in ATOMS:
        for x in (s, o):
            if x.startswith("anchor."): anchors.add(x)
        parts = [s, r, o, f"basis:{basis}", f"asof:{BK}"]
        if extra: parts.append(extra)
        lines.append(" | ".join(parts))
    anchors |= {"anchor.beckn-object", "anchor.action", "anchor.transaction-entry", "anchor.runtime-concept"}
    reg = ["# Anchors — interned meanings", "", "| handle | meaning | grounded-in | asof |", "|---|---|---|---|"]
    for hnd in sorted(anchors):
        reg.append(f"| {hnd} | {hnd.split('.',1)[1].replace('-',' ')} | {BK} | {BK} |")
    open(os.path.join(OUT, "anchors", "index.md"), "w").write("\n".join(reg) + "\n")
    open(os.path.join(OUT, "atoms.md"), "w").write(f"# {BK} KB atoms (structural, book-generic)\n\n" + "\n".join(lines) + "\n")
    print(f"book={BK}  atoms={len(lines)}  anchors={len(anchors)}  "
          f"workbench={'yes' if workbench else 'NO (runtime-meaning omitted)'}  -> {OUT}")
    return OUT, BK

if __name__ == "__main__":
    build(pick_book())

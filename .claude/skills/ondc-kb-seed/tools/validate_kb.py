#!/usr/bin/env python3
"""
Reference KB validator — decides whether a KB instance is VALID per spec/60-invariants.md.

READ-ONLY. This is not an operator: it never mutates the KB. Operators (skills) run it as a gate.

Usage:  python3 validate_kb.py <kb_root>
Exit:   0 = valid; 1 = invalid (violations printed).

Scope: enforces the structure-level invariants that are checkable without an operator's
grounding backend. Grounding *resolution* against a live config repo (invariant 2) is checked
only for shape here (config anchors must not be line numbers); full resolution is delegated to a
skill that has the spec repo, per 70-interface.md.
"""
import sys, os, re, glob, json

RELATIONS = {
    "isa","part-of","has-slot","disjoint-with","scoped-to","sent-by",
    "precedes","wasInformedBy","requires","causes","constrains",
    "wasDerivedFrom","wasAttributedTo","wasRevisionOf","wasGeneratedBy","used",
}
GOLDEN_RELATIONS = {"asks-about","answered-by","expects-plane","expects-scope"}
# slot/role handles that are structural fillers, not standalone nodes
SLOT_FILLERS = {"grantor","grantee","object","evidence","lifecycle-anchor"}
BASIS  = {"declared","sandbox-tested","observed-live","authority","ecosystem","derived","inferred"}
PLANE  = {"spec","session-logic","runtime-state","cross"}   # valid !plane=<p> argument
FLAGS  = {"untethered","deprecated","desired","plane"}       # exception-flag names (the only status written by hand)
GROUND_NEEDS_ANCHOR = BASIS - {"inferred","ecosystem"}       # these basis values must carry grounded-in (or a flag)

def load_frontmatter(path):
    with open(path, encoding="utf-8") as fh: t = fh.read()
    if not t.startswith("---"): return {}, t
    end = t.find("\n---", 3)
    if end == -1: return {}, t
    fm = {}
    for line in t[3:end].splitlines():
        m = re.match(r"^([a-zA-Z_-]+):\s*(.*)$", line)
        if m: fm[m.group(1)] = m.group(2).strip()
    return fm, t

def parse_atom(line):
    # mandatory triple + optional key:value fields (basis/asof/grounded-in/...) + optional !flags.
    parts = [p.strip() for p in line.split("|")]
    if len(parts) < 3: return None
    s, r, o = parts[0], parts[1], parts[2]
    kv = {}; flags = {}
    for p in parts[3:]:
        if not p: continue
        if p.startswith("!"):                      # exception flag: !name or !name=arg
            name = p[1:]; arg = True
            if "=" in name: name, arg = (x.strip() for x in name.split("=", 1))
            flags[name.strip()] = arg
        elif ":" in p:
            k, v = p.split(":", 1); kv[k.strip()] = v.strip()
        else:
            return None
    return {"s": s, "r": r, "o": o, "flags": flags, **kv}

def main():
    if len(sys.argv) != 2:
        print("usage: validate_kb.py <kb_root>"); sys.exit(2)
    root = sys.argv[1]
    V = []  # violations

    # ---- collect nodes (handles) ----
    frame_ids, adr_ids = {}, set()
    for f in glob.glob(os.path.join(root, "**", "frames", "*.md"), recursive=True):
        fm, _ = load_frontmatter(f)
        fid = fm.get("id")
        if not fid: V.append(f"[5] frame missing id: {f}"); continue
        if fid in frame_ids: V.append(f"[4] duplicate id '{fid}' ({f} & {frame_ids[fid]})")
        frame_ids[fid] = f
        for forbidden in ("requirement","adoption","confidence"):
            if forbidden in fm: V.append(f"[format] frame '{fid}' has forbidden '{forbidden}:'")
    for f in glob.glob(os.path.join(root, "**", "decisions", "adr-*.md"), recursive=True):
        fm, _ = load_frontmatter(f); adr_ids.add(fm.get("id",""))
    ref_ids = set()
    for f in glob.glob(os.path.join(root, "**", "references", "*.md"), recursive=True):
        fm, _ = load_frontmatter(f); ref_ids.add(fm.get("id",""))

    # ---- collect anchor handles from the committed registry (anchors/*.md rows) ----
    # a registry row is "| anchor.<kebab> | canonical meaning | grounded-in | asof |"
    anchor_ids = set()
    for f in glob.glob(os.path.join(root, "**", "anchors", "*.md"), recursive=True):
        with open(f, encoding="utf-8") as fh:
            for raw in fh:
                cells = [c.strip() for c in raw.split("|")]
                if len(cells) >= 2 and re.match(r"^anchor\.[a-z0-9]([a-z0-9._-]*[a-z0-9])?$", cells[1]):
                    anchor_ids.add(cells[1])

    known = set(frame_ids) | set(adr_ids) | set(ref_ids) | anchor_ids | SLOT_FILLERS
    # allow golden q: handles and literals
    def resolvable(h):
        if h.startswith('"') and h.endswith('"'): return True          # literal
        if h.startswith("q:"): return True                              # golden
        if h in (PLANE | {"live","desired"}): return True               # golden expects-plane / expects-scope values
        if h in known: return True
        # dotted path whose root is a known handle (e.g. frame.slot)
        return h.split(".")[0] in known

    # ---- atoms ----
    atoms = []
    isa_edges = []
    for af in glob.glob(os.path.join(root, "**", "atoms*.md"), recursive=True) + \
              glob.glob(os.path.join(root, "**", "golden", "*.md"), recursive=True):
        with open(af, encoding="utf-8") as fh:
            for ln, raw in enumerate(fh, 1):
                line = raw.strip()
                if not line or line.startswith("#") or "|" not in line: continue
                a = parse_atom(line)
                if not a: V.append(f"[10] malformed atom {af}:{ln}: {line[:60]}"); continue
                atoms.append((af, ln, a))

    for af, ln, a in atoms:
        base = a["r"][4:] if a["r"].startswith("not-") else a["r"]
        if base not in RELATIONS and base not in GOLDEN_RELATIONS: V.append(f"[6] bad relation '{a['r']}' {af}:{ln}")
        basis = a.get("basis")                       # None on a bare/immature triple
        g = a.get("grounded-in")                     # the pointer, or None
        if basis is not None and basis not in BASIS: V.append(f"[6] bad basis '{basis}' {af}:{ln}")
        # invariant 4: basis:inferred <=> no grounded-in (both directions)
        if basis == "inferred" and g:
            V.append(f"[4] basis:inferred must carry NO grounded-in {af}:{ln}")
        # invariant 3: flag vocabulary (+ !plane argument)
        for fname, farg in a["flags"].items():
            if fname not in FLAGS: V.append(f"[3] unknown flag '!{fname}' {af}:{ln}")
            if fname == "plane" and farg not in PLANE: V.append(f"[3] bad !plane value '{farg}' {af}:{ln}")
        # invariant 2 shape: a config anchor (grounded-in with '#') must not be a bare line number
        if g and "#" in g:
            node = g.split("#",1)[1]
            if re.match(r"^L?\d+$", node.strip()):
                V.append(f"[2] config anchor is a line number '{node}' {af}:{ln}")
        # invariant 5: untethered-must-be-tagged — a basis that needs an anchor but has none must be flagged
        tagged = ("untethered" in a["flags"]) or ("deprecated" in a["flags"])
        if basis in GROUND_NEEDS_ANCHOR and not g and not tagged:
            V.append(f"[5] untethered unit (basis:{basis}, no grounded-in) not tagged !untethered {af}:{ln}")
        # invariant 1: handles resolve
        for role in ("s","o"):
            if not resolvable(a[role]): V.append(f"[1] unresolved handle '{a[role]}' {af}:{ln}")
        if a["r"] == "isa": isa_edges.append((a["s"], a["o"]))

    # ---- invariant 3: isa DAG (cycle check) ----
    graph = {}
    for s,o in isa_edges: graph.setdefault(s, set()).add(o)
    WHITE,GRAY,BLACK = 0,1,2
    color = {}
    def dfs(n):
        color[n] = GRAY
        for m in graph.get(n, ()):
            if color.get(m,WHITE)==GRAY: return [n,m]
            if color.get(m,WHITE)==WHITE:
                c = dfs(m)
                if c: return [n]+c
        color[n]=BLACK; return None
    for n in list(graph):
        if color.get(n,WHITE)==WHITE:
            cyc = dfs(n)
            if cyc: V.append(f"[3] isa cycle: {' -> '.join(cyc)}"); break

    # ---- report ----
    if V:
        print(f"INVALID — {len(V)} violation(s):")
        for v in V: print("  " + v)
        sys.exit(1)
    print(f"VALID — {len(atoms)} atoms, {len(frame_ids)} frames, {len(anchor_ids)} anchors, {len(adr_ids)} ADRs, isa-DAG ok")
    sys.exit(0)

if __name__ == "__main__":
    main()

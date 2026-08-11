#!/usr/bin/env python3
"""
Tool G — Derived Views + Selective Regeneration (KEP, B5).
- Reverse index: config node-path -> the units grounded there (INDEX spine).
- Derived views: regenerated as a PURE FUNCTION of committed atoms (never committed).
- Selective regen: given a config diff (changed node-paths), the blast radius =
  units grounded there (direct) + one PROV-O hop (derived-from an affected subject).
  Everything else is untouched. Proves grounding pays off: change is local.
Input: skill/kb-out/fis13/atoms.md. Output: regen-report.json.
"""
import os, re, json, glob
import _env
HERE = os.path.dirname(os.path.abspath(__file__))

def pick_book():
    """book id from arg, else the first kb-out/<book> dir."""
    import sys
    if len(sys.argv) > 1: return sys.argv[1]
    outs = sorted(glob.glob(os.path.join(_env.KNOWLEDGE, "*", "atoms.md")))
    if not outs: raise SystemExit("no kb-out/<book>/atoms.md — run kb_writer first")
    return os.path.basename(os.path.dirname(outs[0]))

BOOK = pick_book()
ATOMS_MD = os.path.join(_env.KNOWLEDGE, BOOK, "atoms.md")

def parse():
    atoms = []
    for raw in open(ATOMS_MD):
        line = raw.strip()
        if not line or line.startswith("#") or "|" not in line: continue
        parts = [p.strip() for p in line.split("|")]
        s, r, o = parts[0], parts[1], parts[2]
        kv = {}
        for p in parts[3:]:
            if ":" in p and not p.startswith("!"):
                k, v = p.split(":", 1); kv[k.strip()] = v.strip()
        atoms.append({"s": s, "r": r, "o": o, "basis": kv.get("basis"),
                      "grounded": kv.get("grounded-in"), "line": line})
    return atoms

def config_path(g):
    """return the config node-path (file#node) if grounded in THIS book, else None."""
    if not g: return None
    m = re.match(rf"^{re.escape(BOOK)}:(.+)$", g)
    return m.group(1) if m else None

def run():
    atoms = parse()
    # ---- reverse index: config node-path -> [atom idx] ----
    rev = {}
    for i, a in enumerate(atoms):
        cp = config_path(a["grounded"])
        if cp: rev.setdefault(cp, []).append(i)

    # ---- derived views (pure function of committed atoms; never committed) ----
    seq = [(a["s"], a["o"]) for a in atoms if a["r"] == "precedes"]
    taxonomy = sorted(a["s"] for a in atoms if a["r"] == "isa" and a["o"] == "anchor.beckn-object")
    views = {"action_sequence": [f"{s} → {o}" for s, o in seq],
             "beckn_object_taxonomy": taxonomy}

    # ---- selective regen: blast radius per changed config node ----
    def blast(changed_paths):
        direct = set()
        for p in changed_paths:
            direct |= set(rev.get(p, []))
        subjects = {atoms[i]["s"] for i in direct}
        # one PROV-O hop: derived units grounded in an affected subject
        indirect = set()
        for i, a in enumerate(atoms):
            if a["basis"] == "derived" and a["grounded"] in subjects:
                indirect.add(i)
        affected = direct | indirect
        return {"changed": changed_paths,
                "direct": sorted(atoms[i]["line"][:70] for i in direct),
                "indirect_provo": sorted(atoms[i]["line"][:70] for i in indirect),
                "affected_count": len(affected),
                "untouched_count": len(atoms) - len(affected)}

    # sample 3 real changed nodes generically (one per config area if available)
    def sample(pred):
        return next((p for p in sorted(rev) if pred(p)), None)
    picks = [p for p in (sample(lambda x: x.startswith("validations")),
                         sample(lambda x: x.startswith("flows")),
                         sample(lambda x: x.startswith("actions")),
                         sample(lambda x: x.startswith("errors")),
                         sample(lambda x: x.startswith("specs"))) if p]
    demos = {f"change: {p}": blast([p]) for p in picks[:3]}

    report = {"total_atoms": len(atoms), "indexed_config_nodes": len(rev),
              "views": views, "regen_demos": demos}
    out = _env.w("regen-report.json")
    json.dump(report, open(out, "w"), indent=2)

    print(f"atoms={len(atoms)}  indexed config nodes={len(rev)}")
    print("\nderived views (regenerated from atoms):")
    print("  action_sequence:", " ; ".join(views["action_sequence"]))
    print("  beckn_taxonomy :", views["beckn_object_taxonomy"])
    print("\nselective regen (blast radius):")
    for name, d in demos.items():
        print(f"  {name}: affected={d['affected_count']} / untouched={d['untouched_count']}")
        for x in d["direct"]: print(f"      direct:   {x}")
        for x in d["indirect_provo"]: print(f"      derived:  {x}")

if __name__ == "__main__":
    run()

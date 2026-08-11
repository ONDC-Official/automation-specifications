#!/usr/bin/env python3
"""
Stage G consolidation — the INDEX spine across ALL books.

tool_g.py writes one regen-report per invocation, so running it per book leaves only the last
book's report on disk. The reverse index is the thing selective regeneration actually rides on, so
it has to span every seeded book at once. This builds:

  knowledge/_index/reverse-index.json   config file -> node-path -> units grounded there
  knowledge/_index/blast-radius.json    per config FILE: how many units a change there touches
  knowledge/_index/cross-book.json      shared vs book-specific meanings across books
  knowledge/_index/README.md            how to use the above

Selective regen (the promise): given a changed config node-path, the units to revisit are the ones
grounded at that path, plus one PROV-O hop (anything derived from an affected subject). Everything
else is untouched.
"""
import os, re, json, glob, collections
import _env

PROV = {"wasDerivedFrom", "wasRevisionOf", "wasInformedBy", "wasGeneratedBy", "used"}

def parse(line):
    parts = [p.strip() for p in line.split("|")]
    if len(parts) < 3: return None
    s, r, o = parts[:3]
    kv = {}
    for p in parts[3:]:
        if p and not p.startswith("!") and ":" in p:
            k, v = p.split(":", 1); kv[k.strip()] = v.strip()
    return s, r, o, kv

def main():
    OUT = os.path.join(_env.KNOWLEDGE, "_index")
    os.makedirs(OUT, exist_ok=True)

    rev = collections.defaultdict(list)      # "book:file#node" -> [ {book, line, triple} ]
    byfile = collections.Counter()           # "book:file" -> unit count
    subj_units = collections.defaultdict(list)   # (book, subject) -> [line]
    prov_edges = collections.defaultdict(list)   # (book, source-subject) -> [dependent line]
    anchor_books = collections.defaultdict(set)  # anchor handle -> {books}
    rel_c, book_units = collections.Counter(), collections.Counter()

    for atoms in sorted(glob.glob(os.path.join(_env.KNOWLEDGE, "*", "atoms.md"))):
        bid = os.path.basename(os.path.dirname(atoms))
        for ln, raw in enumerate(open(atoms, encoding="utf-8"), 1):
            line = raw.strip()
            if not line or line.startswith("#") or "|" not in line: continue
            p = parse(line)
            if not p: continue
            s, r, o, kv = p
            book_units[bid] += 1
            rel_c[r] += 1
            subj_units[(bid, s)].append(ln)
            if s.startswith("anchor."): anchor_books[s].add(bid)
            if o.startswith("anchor."): anchor_books[o].add(bid)
            base = r[4:] if r.startswith("not-") else r
            if base in PROV: prov_edges[(bid, o)].append(ln)
            g = kv.get("grounded-in")
            if g and "#" in g and not g.startswith("workbench:"):
                pre, node = g.split("#", 1)
                rev[f"{pre}#{node}"].append({"book": bid, "line": ln, "s": s, "r": r, "o": o})
                byfile[pre] += 1

    # blast radius per config file: direct units + one PROV-O hop
    blast = {}
    for pre, direct in byfile.most_common():
        bid = pre.split(":", 1)[0]
        subs = {u["s"] for k, us in rev.items() if k.startswith(pre + "#") for u in us}
        hop = sum(len(prov_edges.get((bid, s), [])) for s in subs)
        blast[pre] = {"direct": direct, "prov_hop": hop,
                      "total_affected": direct + hop,
                      "book_total": book_units.get(bid, 0),
                      "untouched": book_units.get(bid, 0) - (direct + hop)}

    shared = {a: sorted(bs) for a, bs in anchor_books.items() if len(bs) > 1}
    solo = {a: list(bs)[0] for a, bs in anchor_books.items() if len(bs) == 1}
    fam = collections.defaultdict(set)
    for a, bs in anchor_books.items():
        for b in bs: fam[re.split(r"[-.]", b)[0][:5]].add(a)
    fis = set().union(*[v for k, v in fam.items() if k.startswith("fis")]) if any(k.startswith("fis") for k in fam) else set()
    trv = set().union(*[v for k, v in fam.items() if k.startswith("trv")]) if any(k.startswith("trv") for k in fam) else set()

    json.dump({k: v for k, v in rev.items()}, open(os.path.join(OUT, "reverse-index.json"), "w"), indent=1)
    json.dump(blast, open(os.path.join(OUT, "blast-radius.json"), "w"), indent=1)
    json.dump({"shared_across_books": shared, "book_specific_count": len(solo),
               "fis_only": sorted(fis - trv), "trv_only": sorted(trv - fis),
               "fis_and_trv": sorted(fis & trv)},
              open(os.path.join(OUT, "cross-book.json"), "w"), indent=1)

    top = sorted(blast.items(), key=lambda kv: -kv[1]["total_affected"])[:12]
    readme = [
        "# Index spine (Stage G, consolidated)", "",
        f"Built from {len(book_units)} books / {sum(book_units.values())} units / "
        f"{len(rev)} distinct grounded config node-paths.", "",
        "## Files", "",
        "| file | what it answers |", "|---|---|",
        "| `reverse-index.json` | *which units are grounded at this config node-path?* — key is `<book>:<file>#<node>` |",
        "| `blast-radius.json` | *if this config file changes, how much of the KB must be revisited?* |",
        "| `cross-book.json` | *which interned meanings are shared across books vs book-specific?* |",
        "",
        "## Selective regeneration", "",
        "A config change revisits only the units grounded at the changed node-path, plus one PROV-O",
        "hop (anything derived from an affected subject). Everything else is untouched — that is the",
        "whole return on positional grounding.", "",
        "## Highest blast radius (change these files and the most units need revisiting)", "",
        "| config file | direct | +prov hop | untouched in book |", "|---|---|---|---|",
    ]
    for pre, m in top:
        readme.append(f"| `{pre}` | {m['direct']} | {m['prov_hop']} | {m['untouched']} |")
    readme += ["", "## Cross-book meaning reuse", "",
               f"- interned meanings shared by >1 book: **{len(shared)}**",
               f"- book-specific meanings: **{len(solo)}**",
               f"- present in both the FIS and TRV families: **{len(fis & trv)}**",
               f"- FIS-family only: **{len(fis - trv)}** · TRV-family only: **{len(trv - fis)}**", ""]
    open(os.path.join(OUT, "README.md"), "w").write("\n".join(readme) + "\n")

    print(f"reverse-index : {len(rev)} grounded node-paths across {len(book_units)} books")
    print(f"blast-radius  : {len(blast)} config files")
    print(f"cross-book    : {len(shared)} shared meanings, {len(solo)} book-specific")
    print(f"               FIS∩TRV={len(fis & trv)}  FIS-only={len(fis - trv)}  TRV-only={len(trv - fis)}")
    print("\ntop blast radius:")
    for pre, m in top[:8]:
        print(f"   {pre:58} direct={m['direct']:4} +hop={m['prov_hop']:3} untouched={m['untouched']:4}")
    print("\ntop relations:")
    for r, c in rel_c.most_common(10): print(f"   {r:20} {c}")

if __name__ == "__main__":
    main()

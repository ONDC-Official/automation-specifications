#!/usr/bin/env python3
"""
Stage F completion — registry finalizer (KEP).

kb_writer.py interns anchors only for the structural atoms IT generated. Stage E (the AI
interpretation step) plugs into the same seam and interns many more meanings, plus a small number
of non-anchor node handles (dom.* / usecase.* / flow.* / journey.* / step.* / error.*). The
interning invariant requires every handle used as a subject/object to resolve to a declared node,
so after E's units are merged this rebuilds the per-book registries from what atoms.md actually
uses:

  anchors/index.md   one row per anchor.<kebab> handle  -> the anchor registry the validator reads
  frames/<id>.md     one frame per non-anchor handle    -> declared node with id frontmatter

Grounding for a registry row is taken from the atom that FIRST uses the handle as a subject with a
grounded-in pointer — i.e. the position the meaning was interned at. Handles that are never
grounded anywhere are written with grounding '-' so they stay visible rather than looking settled.

READ-ONLY w.r.t. atoms: never edits a unit, only rebuilds the registries the units reference.
Usage: python3 finalize_registries.py [book_dir_or_id ...]   (default: every book in knowledge/)
"""
import os, re, sys, glob, json
import _env

ANCHOR_RE = re.compile(r"^anchor\.[a-z0-9]([a-z0-9._-]*[a-z0-9])?$")
KIND = {  # frame kind by handle root — kind vocabulary is class|instance|concept|pattern
    "flow": "instance", "journey": "instance", "step": "instance", "error": "instance",
    "dom": "concept", "usecase": "concept", "docs": "reference-note",
}

def parse_atom(line):
    parts = [p.strip() for p in line.split("|")]
    if len(parts) < 3: return None
    s, r, o = parts[0], parts[1], parts[2]
    kv = {}
    for p in parts[3:]:
        if p and not p.startswith("!") and ":" in p:
            k, v = p.split(":", 1); kv[k.strip()] = v.strip()
    return s, r, o, kv

def meaning(handle):
    tail = handle.split(".", 1)[1] if "." in handle else handle
    return tail.replace("-", " ").replace("_", " ").replace(".", " ")

def finalize(book_dir):
    bid = os.path.basename(book_dir)
    atoms = os.path.join(book_dir, "atoms.md")
    if not os.path.exists(atoms): return None
    anchors, others, ground, order = set(), set(), {}, []
    for raw in open(atoms, encoding="utf-8"):
        line = raw.strip()
        if not line or line.startswith("#") or "|" not in line: continue
        p = parse_atom(line)
        if not p: continue
        s, r, o, kv = p
        g = kv.get("grounded-in")
        for h in (s, o):
            if h.startswith('"') or h.startswith("q:"): continue
            if ANCHOR_RE.match(h):
                if h not in anchors: anchors.add(h); order.append(h)
            else:
                others.add(h)
        # the interning position: first time the handle is the SUBJECT of a grounded atom
        if g and s not in ground: ground[s] = g

    os.makedirs(os.path.join(book_dir, "anchors"), exist_ok=True)
    rows = ["# Anchors — interned meanings", "",
            f"> Rebuilt from `atoms.md` for `{bid}` (structural + Stage E). One row per interned",
            "> meaning; `grounded-in` is the position the meaning was first interned at.", "",
            "| handle | meaning | grounded-in | asof |", "|---|---|---|---|"]
    for h in sorted(anchors):
        rows.append(f"| {h} | {meaning(h)} | {ground.get(h, '-')} | {bid} |")
    open(os.path.join(book_dir, "anchors", "index.md"), "w", encoding="utf-8").write("\n".join(rows) + "\n")

    nframes = 0
    if others:
        fdir = os.path.join(book_dir, "frames")
        os.makedirs(fdir, exist_ok=True)
        for h in sorted(others):
            root = h.split(".")[0]
            fn = re.sub(r"[^a-z0-9._-]+", "-", h.lower()) + ".md"
            body = [
                "---",
                f"id: {h}",
                f"kind: {KIND.get(root, 'concept')}",
                "layer: domain",
                "status: draft",
                f"asof: {bid}",
                "---",
                "",
                f"# {h}",
                "",
                f"Declared node for `{h}` — {meaning(h)}.",
                "",
                f"Grounded at: `{ground.get(h, '(no grounded atom uses this handle as subject)')}`",
                "",
                "Seeded by Stage E interpretation; body intentionally light — the facts live in",
                "`atoms.md`, not in prose.",
            ]
            open(os.path.join(fdir, fn), "w", encoding="utf-8").write("\n".join(body) + "\n")
            nframes += 1
    return bid, len(anchors), nframes, sum(1 for h in anchors if h not in ground)

if __name__ == "__main__":
    targets = sys.argv[1:]
    books = []
    if targets:
        for t in targets:
            books.append(t if os.path.isdir(t) else os.path.join(_env.KNOWLEDGE, t))
    else:
        books = [d for d in sorted(glob.glob(os.path.join(_env.KNOWLEDGE, "*")))
                 if os.path.isdir(d) and not os.path.basename(d).startswith("_")]
    tot_a = tot_f = 0
    for b in books:
        r = finalize(b)
        if not r: continue
        bid, na, nf, ung = r
        tot_a += na; tot_f += nf
        print(f"  {bid:24} anchors={na:5}  frames={nf:4}  ungrounded-anchors={ung}")
    print(f"\nregistries rebuilt: {tot_a} anchors, {tot_f} frames across {len(books)} book(s)")

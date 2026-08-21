#!/usr/bin/env python3
"""kb_query.py — read-side query tool over the ONDC grounded KB (knowledge/).

Never mutates the KB. Every answer it prints is traceable to an atom line or a
config node-path, so a caller can cite `<book>:<file>#<node>`.

KB root discovery order:
  1. --root
  2. $ONDC_KB_ROOT                      (dir that contains knowledge/)
  3. walk up from this file until a dir with knowledge/_index/ is found
"""
from __future__ import annotations

import argparse
import json
import os
import re
import sys
from pathlib import Path

# ---------------------------------------------------------------- root + load


def die(msg: str, code: int = 2):
    print(f"error: {msg}", file=sys.stderr)
    sys.exit(code)


def find_root(explicit: str | None = None) -> Path:
    cands = []
    if explicit:
        cands.append(Path(explicit).expanduser())
    if os.environ.get("ONDC_KB_ROOT"):
        cands.append(Path(os.environ["ONDC_KB_ROOT"]).expanduser())
    cands.extend(Path(__file__).resolve().parents)
    for c in cands:
        if (c / "knowledge" / "_index").is_dir():
            return c
        if c.name == "knowledge" and (c / "_index").is_dir():
            return c.parent
    die("cannot locate the KB — set ONDC_KB_ROOT to the dir containing knowledge/")


def load_json(p: Path):
    if not p.exists():
        return {}
    try:
        return json.loads(p.read_text())
    except Exception as e:  # a half-written work file must not kill a query
        print(f"warn: {p.name} unreadable ({e})", file=sys.stderr)
        return {}


def parse_atom(line: str) -> dict | None:
    parts = [p.strip() for p in line.split("|")]
    if len(parts) < 3 or not parts[0] or not parts[1]:
        return None
    a = {
        "s": parts[0],
        "r": parts[1],
        "o": parts[2],
        "basis": None,
        "asof": None,
        "grounded_in": None,
        "flags": [],
        "raw": line,
    }
    for p in parts[3:]:
        if p.startswith("basis:"):
            a["basis"] = p[len("basis:"):]
        elif p.startswith("asof:"):
            a["asof"] = p[len("asof:"):]
        elif p.startswith("grounded-in:"):
            a["grounded_in"] = p[len("grounded-in:"):]
        elif p.startswith("!"):
            a["flags"].append(p)
    return a


class KB:
    def __init__(self, root: Path):
        self.root = root
        self.kdir = root / "knowledge"
        self.books = sorted(
            d.name
            for d in self.kdir.iterdir()
            if d.is_dir() and not d.name.startswith("_") and (d / "atoms.md").exists()
        )
        self._atoms: dict[str, list[dict]] = {}
        self._anchors: dict[str, dict[str, dict]] = {}
        self._j: dict[str, dict] = {}

    # -- lazy artifacts
    def j(self, rel: str):
        if rel not in self._j:
            self._j[rel] = load_json(self.kdir / rel)
        return self._j[rel]

    def reverse_index(self):
        return self.j("_index/reverse-index.json")

    def blast(self):
        return self.j("_index/blast-radius.json")

    def cross_book(self):
        return self.j("_index/cross-book.json")

    def conformance(self):
        return self.j("_work/base-conformance.json")

    # -- pipeline artifacts key books in different cases; match case-insensitively
    def seq_entry(self, book: str) -> dict:
        for k, v in self.j("_work/sequence-graph.json").items():
            if k.lower() == book.lower():
                return v
        return {}

    def ground_entry(self, book: str) -> dict:
        for k, v in self.j("_work/ground-map.json").items():
            if k.lower() == book.lower():
                return v
        return {}

    def scope_entry(self, book: str):
        for k, v in self.j("_work/scope-graphs.json").items():
            if k.lower().replace("release-eks-", "") == book.lower():
                return k, v
        return None, {}

    def conformance_entry(self, book: str) -> dict:
        for k, v in self.conformance().items():
            if k.lower() == book.lower():
                return v
        return {}

    # -- atoms
    def atoms(self, book: str) -> list[dict]:
        if book not in self._atoms:
            rows = []
            for n, line in enumerate((self.kdir / book / "atoms.md").read_text().splitlines(), 1):
                line = line.strip()
                if not line or line.startswith("#") or line.startswith("|"):
                    continue
                a = parse_atom(line)
                if a:
                    a["book"], a["line"] = book, n
                    rows.append(a)
            self._atoms[book] = rows
        return self._atoms[book]

    # -- anchors (interned meanings)
    def anchors(self, book: str) -> dict[str, dict]:
        if book not in self._anchors:
            out: dict[str, dict] = {}
            f = self.kdir / book / "anchors" / "index.md"
            if f.exists():
                for line in f.read_text().splitlines():
                    if not line.startswith("| anchor."):
                        continue
                    cells = [c.strip() for c in line.strip().strip("|").split("|")]
                    if len(cells) >= 4:
                        out[cells[0]] = {
                            "handle": cells[0],
                            "meaning": cells[1],
                            "grounded_in": None if cells[2] == "-" else cells[2],
                            "asof": cells[3],
                        }
            self._anchors[book] = out
        return self._anchors[book]

    def frames(self, book: str) -> list[Path]:
        d = self.kdir / book / "frames"
        return sorted(d.glob("*.md")) if d.is_dir() else []


# ---------------------------------------------------------------- resolution

_VERSION_RE = re.compile(r"-(\d+(?:\.\d+)+)$")  # trailing release version, not the domain's digits


def norm(q: str) -> str:
    q = q.strip().lower()
    q = re.sub(r"^ondc[:\-_]", "", q)
    q = q.replace("release-eks-", "")
    return re.sub(r"[\s_]+", "-", q)


def resolve_books(kb: KB, query: str | None, all_ok: bool = False) -> list[str]:
    """Map a loose 'FIS12 2.3.0' / 'ondc:trv11' / 'fis12 pf' to book ids, best first."""
    if not query:
        if all_ok:
            return kb.books
        die("a domain/version is required (try: kb_query.py books)")
    q = norm(query)
    if q in kb.books:
        return [q]
    toks = [t for t in re.split(r"[-\s]+", q) if t]
    hits = [b for b in kb.books if all(t in b for t in toks)]
    if not hits:
        flat = q.replace("-", "").replace(".", "")
        hits = [b for b in kb.books if flat in b.replace("-", "").replace(".", "")]
    if not hits:
        return []

    def newest_first(b: str):
        m = _VERSION_RE.search(b)
        return tuple(int(x) for x in m.group(1).split(".")) if m else (0,)

    return sorted(hits, key=newest_first, reverse=True)


def one_book(kb: KB, query: str) -> str:
    hits = resolve_books(kb, query)
    if not hits:
        die(f"no book matches '{query}'. known books: {', '.join(kb.books)}")
    if len(hits) > 1:
        print(f"# '{query}' matched {len(hits)} books: {', '.join(hits)} — using {hits[0]}", file=sys.stderr)
    return hits[0]


# ---------------------------------------------------------------- formatting


def fmt_atom(a: dict, show_book: bool = False) -> str:
    bits = [f"{a['s']} | {a['r']} | {a['o']}"]
    if a["basis"]:
        bits.append(f"basis:{a['basis']}")
    if a["grounded_in"]:
        bits.append(f"grounded-in:{a['grounded_in']}")
    bits.extend(a["flags"])
    return (f"[{a['book']}] " if show_book else "") + "  ·  ".join(bits)


def emit(rows: list[str], limit: int, total: int | None = None):
    total = len(rows) if total is None else total
    for r in rows[:limit]:
        print(r)
    if total > limit:
        print(f"\n… {total - limit} more (raise --limit or narrow the filter). total={total}")
    elif not rows:
        print("(no matches)")


# ---------------------------------------------------------------- commands


def cmd_books(kb: KB, a):
    print(f"KB root: {kb.root}\n{len(kb.books)} books\n")
    print(f"{'book':<24} {'domain':<14} {'version':<9} {'atoms':>6} {'anchors':>8} {'flows':>6}  entry-actions")
    print("-" * 100)
    for b in kb.books:
        _, sc = kb.scope_entry(b)
        sq = kb.seq_entry(b)
        print(
            f"{b:<24} {sc.get('domain','?'):<14} {sc.get('version','?'):<9} "
            f"{len(kb.atoms(b)):>6} {len(kb.anchors(b)):>8} {str(sq.get('flows','?')):>6}  "
            f"{','.join(sq.get('entry_actions') or ['?'])}"
        )


def cmd_resolve(kb: KB, a):
    hits = resolve_books(kb, a.query)
    if not hits:
        print(f"(no book matches '{a.query}')\nknown: {', '.join(kb.books)}")
        return
    for b in hits:
        _, sc = kb.scope_entry(b)
        print(f"{b}\t{sc.get('domain','?')}\t{sc.get('version','?')}")


def cmd_overview(kb: KB, a):
    b = one_book(kb, a.book)
    key, sc = kb.scope_entry(b)
    sq, gm, conf = kb.seq_entry(b), kb.ground_entry(b), kb.conformance_entry(b)
    atoms = kb.atoms(b)

    print(f"# {b}  ({sc.get('domain','?')} {sc.get('version','?')})")
    print(f"config book : configs/{key}/config" if key else "config book : (not found)")
    print(f"atoms       : {len(atoms)}   anchors: {len(kb.anchors(b))}   frames: {len(kb.frames(b))}")
    if gm:
        print(f"grounded    : {gm.get('nodes_grounded','?')} config nodes, "
              f"round-trip {gm.get('roundtrip_rate','?')}%")
        by = gm.get("by_kind", {})
        if by:
            print("              " + ", ".join(f"{k}:{v}" for k, v in by.items()))
    if sq:
        print(f"entry actions: {', '.join(sq.get('entry_actions', []))}")
        print(f"actions: {sq.get('action_nodes','?')}  edges: {sq.get('edges','?')}  "
              f"flows: {sq.get('flows','?')}  steps: {sq.get('total_steps','?')} "
              f"(protocol {sq.get('protocol_steps','?')} / ui {sq.get('ui_steps','?')})")
        for f in sq.get("flags_sample", [])[:5]:
            print(f"  !flag {f.get('type')}: {f.get('flow','')}")

    counts: dict[str, int] = {}
    bases: dict[str, int] = {}
    for x in atoms:
        counts[x["r"]] = counts.get(x["r"], 0) + 1
        bases[x["basis"] or "-"] = bases.get(x["basis"] or "-", 0) + 1
    print("\nrelations   : " + ", ".join(f"{k}={v}" for k, v in sorted(counts.items(), key=lambda t: -t[1])[:10]))
    print("basis       : " + ", ".join(f"{k}={v}" for k, v in sorted(bases.items(), key=lambda t: -t[1])))
    flagged = [x for x in atoms if x["flags"]]
    if flagged:
        print(f"flagged     : {len(flagged)} atoms carry !flags — see `atoms --book {b} --flagged`")

    if conf:
        print(f"\nbase deviations vs common-config/beckn-base.yaml: {conf.get('deviation_count',0)} "
              f"(schemas checked {conf.get('schemas_checked','?')})")
        for d in conf.get("deviations", [])[:8]:
            v = f" {d.get('values')}" if d.get("values") else ""
            print(f"  - {d.get('type')}: {d.get('at')}{v}")

    files = sc.get("in_scope_files", [])
    if files:
        print(f"\nin-scope config files ({len(files)}):")
        for f in files:
            print(f"  {b}:{f}")


def cmd_flows(kb: KB, a):
    b = one_book(kb, a.book)
    sq = kb.seq_entry(b)
    if not sq:
        die(f"no sequence graph recorded for {b}")
    spines = sq.get("flow_spines", [])
    if a.flow:
        pat = norm(a.flow)
        spines = [s for s in spines if pat in norm(s.get("flow", ""))]
    print(f"# {b} — entry actions: {', '.join(sq.get('entry_actions', []))}; {len(spines)} flow(s)\n")
    for s in spines[: a.limit]:
        print(f"{s.get('flow')}  ({s.get('n_steps')} steps)")
        print("  " + " → ".join(s.get("spine", [])))
    if len(spines) > a.limit:
        print(f"\n… {len(spines)-a.limit} more")
    print(f"\n(flow semantics live in atoms — try `atoms --book {b} --grep flows/`)")


def cmd_anchors(kb: KB, a):
    b = one_book(kb, a.book)
    rows = list(kb.anchors(b).values())
    if a.pattern:
        p = a.pattern.lower()
        rows = [r for r in rows if p in r["handle"].lower() or p in r["meaning"].lower()]
    print(f"# {b} — {len(rows)} anchors" + (f" matching '{a.pattern}'" if a.pattern else "") + "\n")
    emit([f"{r['handle']:<44} {r['meaning']:<38} {r['grounded_in'] or '-'}" for r in rows], a.limit)


def cmd_about(kb: KB, a):
    handle = a.handle if "." in a.handle else "anchor." + norm(a.handle)
    books = resolve_books(kb, a.book) if a.book else kb.books
    if not books:
        die(f"no book matches '{a.book}'")
    found = False
    for b in books:
        atoms = kb.atoms(b)
        subj = [x for x in atoms if x["s"] == handle]
        obj = [x for x in atoms if x["o"] == handle]
        if not subj and not obj:
            continue
        found = True
        meta = kb.anchors(b).get(handle)
        print(f"\n## {handle}  in {b}")
        if meta:
            print(f"meaning     : {meta['meaning']}")
            print(f"interned at : {meta['grounded_in'] or '(no single position)'}")
        print(f"as subject  : {len(subj)}   as object: {len(obj)}")
        isa = sorted({x["o"] for x in subj if x["r"] == "isa"})
        kids = sorted({x["s"] for x in obj if x["r"] == "isa"})
        if isa:
            print(f"isa         : {', '.join(isa)}")
        if kids:
            more = f" … +{len(kids)-12}" if len(kids) > 12 else ""
            print(f"kinds of it : {', '.join(kids[:12])}{more}")
        print("\n-- as subject --")
        emit([fmt_atom(x) for x in subj], a.limit)
        print("\n-- as object --")
        emit([fmt_atom(x) for x in obj], a.limit)
    if not found:
        print(f"(no atoms mention {handle} in {', '.join(books)})")
        stem = handle.split(".", 1)[-1]
        near = sorted({h for b in books for h in kb.anchors(b) if stem in h})
        if near:
            print("did you mean: " + ", ".join(near[:15]))
        return
    shared = kb.cross_book().get("shared_across_books", {}).get(handle)
    if shared:
        print(f"\nshared across books: {', '.join(shared)}")


def cmd_atoms(kb: KB, a):
    books = resolve_books(kb, a.book) if a.book else kb.books
    if not books:
        die(f"no book matches '{a.book}'")
    rows, total = [], 0
    for b in books:
        for x in kb.atoms(b):
            if a.subject and a.subject.lower() not in x["s"].lower():
                continue
            if a.relation and x["r"] != a.relation:
                continue
            if a.object and a.object.lower() not in x["o"].lower():
                continue
            if a.basis and x["basis"] != a.basis:
                continue
            if a.flagged and not x["flags"]:
                continue
            if a.grep and a.grep.lower() not in x["raw"].lower():
                continue
            total += 1
            rows.append(fmt_atom(x, show_book=len(books) > 1))
    emit(rows, a.limit, total)


def cmd_search(kb: KB, a):
    books = resolve_books(kb, a.book) if a.book else kb.books
    if not books:
        die(f"no book matches '{a.book}'")
    term = a.term.lower()
    hits, total = [], 0
    for b in books:
        for h, m in kb.anchors(b).items():
            if term in h.lower() or term in m["meaning"].lower():
                total += 1
                hits.append(f"[{b}] anchor  {h:<40} {m['meaning']:<32} {m['grounded_in'] or '-'}")
    for b in books:
        for x in kb.atoms(b):
            if term in x["raw"].lower():
                total += 1
                hits.append(f"[{b}] atom    {fmt_atom(x)}")
    print(f"# '{a.term}' — {total} hits across {len(books)} book(s)\n")
    emit(hits, a.limit, total)


def cmd_ground(kb: KB, a):
    ri = kb.reverse_index()
    q = a.node.lower()
    keys = sorted(k for k in ri if q in k.lower())
    if not keys:
        print(f"(no grounded units at a node matching '{a.node}')")
        return
    print(f"# {len(keys)} config node-path(s) match '{a.node}'\n")
    for k in keys[: a.limit]:
        units = ri[k]
        print(f"{k}   → {len(units)} unit(s)")
        for u in units[: a.per_node]:
            print(f"    {u['s']} | {u['r']} | {u['o']}   ({u['book']} atoms.md:{u['line']})")
        if len(units) > a.per_node:
            print(f"    … {len(units)-a.per_node} more")
    if len(keys) > a.limit:
        print(f"\n… {len(keys)-a.limit} more node-paths")


def cmd_blast(kb: KB, a):
    items = sorted(kb.blast().items(), key=lambda t: -t[1].get("total_affected", 0))
    if a.file:
        q = a.file.lower()
        items = [(k, v) for k, v in items if q in k.lower()]
    print(f"{'config file':<52} {'direct':>7} {'+prov':>7} {'total':>7} {'book tot':>9} {'untouched':>10}")
    print("-" * 100)
    for k, v in items[: a.limit]:
        print(f"{k:<52} {v.get('direct',0):>7} {v.get('prov_hop',0):>7} "
              f"{v.get('total_affected',0):>7} {v.get('book_total',0):>9} {v.get('untouched',0):>10}")
    if len(items) > a.limit:
        print(f"… {len(items)-a.limit} more")


def cmd_compare(kb: KB, a):
    books = []
    for q in a.books:
        hits = resolve_books(kb, q)
        if not hits:
            die(f"no book matches '{q}'")
        books.append(hits[0])
    b1, b2 = books
    s1 = {(x["s"], x["r"], x["o"]) for x in kb.atoms(b1)}
    s2 = {(x["s"], x["r"], x["o"]) for x in kb.atoms(b2)}
    print(f"# {b1} vs {b2}\nshared triples: {len(s1 & s2)}   only in {b1}: {len(s1-s2)}   "
          f"only in {b2}: {len(s2-s1)}\n")
    for label, s in ((b1, s1 - s2), (b2, s2 - s1)):
        rows = sorted(f"{x[0]} | {x[1]} | {x[2]}" for x in s)
        if a.grep:
            rows = [r for r in rows if a.grep.lower() in r.lower()]
        print(f"-- only in {label} ({len(rows)}) --")
        emit(rows, a.limit)
        print()
    sq1, sq2 = kb.seq_entry(b1), kb.seq_entry(b2)
    if sq1 and sq2:
        print(f"entry actions  {b1}: {sq1.get('entry_actions')}   {b2}: {sq2.get('entry_actions')}")
        print(f"flows          {b1}: {sq1.get('flows')}   {b2}: {sq2.get('flows')}")


def cmd_frames(kb: KB, a):
    b = one_book(kb, a.book)
    fs = kb.frames(b)
    if a.name:
        p = norm(a.name)
        match = [f for f in fs if p in norm(f.stem)]
        if not match:
            print(f"(no frame matching '{a.name}' in {b}; {len(fs)} frames exist)")
            return
        for f in match[:3]:
            print(f"--- {b}/frames/{f.name} ---")
            print(f.read_text())
        return
    print(f"# {b} — {len(fs)} frames\n")
    emit([f.stem for f in fs], a.limit)


def cmd_files(kb: KB, a):
    b = one_book(kb, a.book)
    key, sc = kb.scope_entry(b)
    files = sc.get("in_scope_files", [])
    print(f"# {b} — {len(files)} in-scope config files (index.yaml traversal only)")
    print(f"# on disk: {kb.root}/configs/{key}/config/\n")
    for f in files:
        print(f"{b}:{f}")
    orph = sc.get("orphans") or sc.get("orphan_files")
    if orph:
        print(f"\norphans (out of scope, never seeded): {len(orph)}")
        for o in orph[:20]:
            print(f"  {o}")


def cmd_shared(kb: KB, a):
    cb = kb.cross_book().get("shared_across_books", {})
    if a.handle:
        h = a.handle if "." in a.handle else "anchor." + norm(a.handle)
        books = cb.get(h)
        print(f"{h}: " + (", ".join(books) if books else "(book-specific, or not an interned meaning)"))
        return
    rows = sorted(cb.items(), key=lambda t: -len(t[1]))
    print(f"# {len(rows)} meanings shared by >1 book (most-shared first)\n")
    emit([f"{h:<44} {len(bs):>2} books  {', '.join(bs)}" for h, bs in rows], a.limit)


def cmd_stats(kb: KB, a):
    cb = kb.cross_book()
    print(f"KB root: {kb.root}")
    print(f"books: {len(kb.books)}   atoms: {sum(len(kb.atoms(b)) for b in kb.books)}   "
          f"anchor rows: {sum(len(kb.anchors(b)) for b in kb.books)}")
    print(f"meanings shared across >1 book: {len(cb.get('shared_across_books', {}))}")
    print(f"book-specific meanings: {cb.get('book_specific_count', '?')}")
    print(f"FIS-only: {len(cb.get('fis_only', []))}   TRV-only: {len(cb.get('trv_only', []))}   "
          f"both families: {len(cb.get('fis_and_trv', []))}")


# ---------------------------------------------------------------- cli


def main():
    p = argparse.ArgumentParser(prog="kb_query.py", description="Query the ONDC grounded KB (read-only).")
    p.add_argument("--root", help="repo root containing knowledge/ (else $ONDC_KB_ROOT or auto-detect)")
    sub = p.add_subparsers(dest="cmd", required=True)

    s = sub.add_parser("books", help="list every book with domain, version, size")
    s.set_defaults(fn=cmd_books)

    s = sub.add_parser("resolve", help="map 'FIS12 2.3.0' / 'ondc:trv11' to book ids")
    s.add_argument("query")
    s.set_defaults(fn=cmd_resolve)

    s = sub.add_parser("overview", help="one book: domain, actions, flows, grounding, base deviations, files")
    s.add_argument("book")
    s.set_defaults(fn=cmd_overview)

    s = sub.add_parser("flows", help="flow spines (api call sequence) for a book")
    s.add_argument("book")
    s.add_argument("flow", nargs="?", help="filter by flow-name substring")
    s.add_argument("--limit", type=int, default=40)
    s.set_defaults(fn=cmd_flows)

    s = sub.add_parser("anchors", help="interned meanings in a book")
    s.add_argument("book")
    s.add_argument("pattern", nargs="?")
    s.add_argument("--limit", type=int, default=60)
    s.set_defaults(fn=cmd_anchors)

    s = sub.add_parser("about", help="everything the KB says about one anchor (the main answer command)")
    s.add_argument("handle")
    s.add_argument("--book", help="restrict to a book; omit to sweep all books")
    s.add_argument("--limit", type=int, default=40)
    s.set_defaults(fn=cmd_about)

    s = sub.add_parser("atoms", help="filter atom lines")
    s.add_argument("--book")
    s.add_argument("--subject")
    s.add_argument("--relation")
    s.add_argument("--object")
    s.add_argument("--basis", choices=["declared", "sandbox-tested", "observed-live", "authority",
                                       "ecosystem", "derived", "inferred"])
    s.add_argument("--flagged", action="store_true", help="only atoms carrying !flags")
    s.add_argument("--grep")
    s.add_argument("--limit", type=int, default=50)
    s.set_defaults(fn=cmd_atoms)

    s = sub.add_parser("search", help="free-text over anchors + atoms")
    s.add_argument("term")
    s.add_argument("--book")
    s.add_argument("--limit", type=int, default=50)
    s.set_defaults(fn=cmd_search)

    s = sub.add_parser("ground", help="config node-path → the units grounded there (reverse index)")
    s.add_argument("node", help="substring of <book>:<file>#<node-path>")
    s.add_argument("--limit", type=int, default=20, help="max node-paths")
    s.add_argument("--per-node", type=int, default=8)
    s.set_defaults(fn=cmd_ground)

    s = sub.add_parser("blast", help="if this config file changes, how much of the KB is affected")
    s.add_argument("file", nargs="?")
    s.add_argument("--limit", type=int, default=25)
    s.set_defaults(fn=cmd_blast)

    s = sub.add_parser("compare", help="triple-level diff between two books (e.g. two versions)")
    s.add_argument("books", nargs=2)
    s.add_argument("--grep")
    s.add_argument("--limit", type=int, default=30)
    s.set_defaults(fn=cmd_compare)

    s = sub.add_parser("frames", help="list or print frame nodes of a book")
    s.add_argument("book")
    s.add_argument("name", nargs="?")
    s.add_argument("--limit", type=int, default=60)
    s.set_defaults(fn=cmd_frames)

    s = sub.add_parser("files", help="in-scope config files for a book (what grounding exists)")
    s.add_argument("book")
    s.set_defaults(fn=cmd_files)

    s = sub.add_parser("shared", help="cross-book meaning reuse")
    s.add_argument("handle", nargs="?")
    s.add_argument("--limit", type=int, default=40)
    s.set_defaults(fn=cmd_shared)

    s = sub.add_parser("stats", help="KB-wide totals")
    s.set_defaults(fn=cmd_stats)

    a = p.parse_args()
    a.fn(KB(find_root(a.root)), a)


if __name__ == "__main__":
    main()

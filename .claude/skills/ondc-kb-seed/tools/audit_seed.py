#!/usr/bin/env python3
"""
Independent post-seed audit (KEP verification step). READ-ONLY.

Checks, across every seeded book:
  1. grounding round-trip  — every config anchor <book>:<file>#<node> resolves to a real node
  2. no line-number anchors, file exists, book-id prefix matches, asof matches
  3. basis distribution + inferred <=> no grounded-in
  4. untethered-must-be-tagged
  5. no `confidence` field anywhere
  6. field order (basis, asof, grounded-in, flags)
  7. closed vocabularies (relation / basis / flag)
  8. duplicates and R vs not-R contradictions
  9. anchor registry coverage
 10. HELD-OUT gate: no basis:declared unit asserts a base-conformance deviation
"""
import os, re, sys, json, glob, yaml, collections
import _env, _yaml

KB = _env.ROOT
KNOW = _env.KNOWLEDGE
RELATIONS = {"isa","part-of","has-slot","disjoint-with","scoped-to","sent-by","precedes",
             "wasInformedBy","requires","causes","constrains","wasDerivedFrom","wasAttributedTo",
             "wasRevisionOf","wasGeneratedBy","used"}
BASIS = {"declared","sandbox-tested","observed-live","authority","ecosystem","derived","inferred"}
FLAGS = {"untethered","deprecated","desired","plane"}
NEEDS_GROUND = BASIS - {"inferred","ecosystem"}
ORDER = ["basis","asof","grounded-in"]
# Field leaves too generic to use as a held-out match token: they occur inside
# unrelated anchor names (anchor.status, anchor.type) and cause false positives.
# For a new-enum-value deviation the specific enum VALUES are matched instead of
# the field leaf; for a new-field on a generic leaf only the qualified Schema.field
# is kept. See REVIEW-QUEUE.md gate 1 (the "869 false positives" note).
GENERIC_LEAVES = {"type","status","name","code","id","value","values","tags","list",
                  "display","url","time","state","order","item","form","error","price",
                  "descriptor","symbol","data","text","title","label","kind","ref"}

_cache = {}
def load_yaml(path):
    """(doc, how). 'strict' = PyYAML's composer accepted it too; 'lenient' = it only
    parses under the runtime's js-yaml anchor semantics (see _yaml.py)."""
    if path in _cache: return _cache[path]
    doc, err = _yaml.load_file(path)
    if err:
        how = "fail"
    else:
        how = "strict" if _yaml.strict_ok(path) else "lenient"
    _cache[path] = (doc, how); return _cache[path]

TOKEN = re.compile(r"([^.\[\]]+)|\[([^\]]*)\]")
def steps_lookup(node, key):
    """steps[<action_id>] -> element of the list whose action_id/id/_NAME_ matches."""
    if isinstance(node, list):
        for el in node:
            if isinstance(el, dict):
                for f in ("action_id","id","_NAME_","name","code"):
                    if str(el.get(f)) == key: return el, True
        for el in node:                      # plain scalar list: [value] = membership
            if not isinstance(el, (dict, list)) and str(el) == key: return el, True
        if key.isdigit() and int(key) < len(node): return node[int(key)], True
    return None, False

def walk(doc, path):
    cur = doc
    for m in TOKEN.finditer(path):
        plain, brack = m.group(1), m.group(2)
        key = plain if plain is not None else brack
        key = key.strip()
        if key == "": continue
        if isinstance(cur, dict):
            if key in cur: cur = cur[key]; continue
            # numeric-ish or quoted key
            k2 = key.strip("'\"")
            if k2 in cur: cur = cur[k2]; continue
            for kk in cur:
                if str(kk) == key: cur = cur[kk]; break
            else:
                return None, False
            continue
        if isinstance(cur, list):
            nxt, ok = steps_lookup(cur, key)
            if ok: cur = nxt; continue
            return None, False
        return None, False
    return cur, True

def md_has(path, node):
    try: txt = open(path, encoding="utf-8").read()
    except Exception: return False
    flat = lambda x: re.sub(r"[^a-z0-9]+", "", x.lower())
    slug = re.sub(r"[^a-z0-9]+", "-", node.lower()).strip("-")
    fslug = flat(node)
    for line in txt.splitlines():
        if line.lstrip().startswith("#"):
            head = line.lstrip("# ")
            h = re.sub(r"[^a-z0-9]+", "-", head.lower()).strip("-")
            if h == slug or slug in h or flat(head) == fslug or (fslug and fslug in flat(head)):
                return True
    return bool(slug) and slug.replace("-", " ") in txt.lower()

def parse(line):
    parts = [p.strip() for p in line.split("|")]
    if len(parts) < 3: return None
    s, r, o = parts[:3]
    kv, flags, seen_order = {}, {}, []
    for p in parts[3:]:
        if not p: continue
        if p.startswith("!"):
            n = p[1:]; a = True
            if "=" in n: n, a = (x.strip() for x in n.split("=", 1))
            flags[n.strip()] = a; seen_order.append("!")
        elif ":" in p:
            k, v = p.split(":", 1); kv[k.strip()] = v.strip(); seen_order.append(k.strip())
        else:
            kv["__malformed__"] = p
    return s, r, o, kv, flags, seen_order

def book_config(bid):
    for d in glob.glob(os.path.join(_env.CONFIGS, "*")):
        if _env.book_id(d) == bid: return os.path.join(d, "config")
    return None

def main():
    bc = json.load(open(_env.w("base-conformance.json")))
    held = {}
    for k, v in bc.items():
        if k.startswith("_"): continue
        toks = set()
        for d in v["deviations"]:
            at = d["at"]; dt = d.get("type")
            if dt == "new-schema":
                toks.add(at)                     # distinctive schema name (e.g. Tag1)
            elif dt == "new-enum-value":
                for val in d.get("values", []):  # match the specific new enum values
                    toks.add(str(val))           # (IN-PROGRESS, REFUND) — never the generic leaf
            else:                                 # new-field
                leaf = at.split(".")[-1]
                toks.add(at)                     # qualified Schema.field (won't false-match anchors)
                if leaf.lower() not in GENERIC_LEAVES:
                    toks.add(leaf)               # bare leaf only when it is distinctive
        held[k] = {t for t in toks if t}

    rows, tot = [], collections.Counter()
    viol = collections.defaultdict(list)
    lenient_books = set()
    for d in sorted(glob.glob(os.path.join(KNOW, "*"))):
        bid = os.path.basename(d)
        if bid.startswith("_") or not os.path.isdir(d): continue
        atoms = os.path.join(d, "atoms.md")
        if not os.path.exists(atoms): continue
        cfg = book_config(bid)
        reg = set()
        ai = os.path.join(d, "anchors", "index.md")
        if os.path.exists(ai):
            for raw in open(ai, encoding="utf-8"):
                c = [x.strip() for x in raw.split("|")]
                if len(c) >= 2 and c[1].startswith("anchor."): reg.add(c[1])
        n = ng = ca = res = unres = 0
        basis_c = collections.Counter()
        seen_lines, rel_pairs, used_anchors = set(), set(), set()
        hits_ok = hits_bad = 0
        for ln, raw in enumerate(open(atoms, encoding="utf-8"), 1):
            line = raw.strip()
            if not line or line.startswith("#") or "|" not in line: continue
            p = parse(line)
            if not p: viol["malformed"].append(f"{bid}:{ln}"); continue
            s, r, o, kv, flags, order = p
            n += 1
            if line in seen_lines: viol["duplicate-unit"].append(f"{bid}:{ln}")
            seen_lines.add(line)
            b = kv.get("basis"); basis_c[b or "(none)"] += 1
            g = kv.get("grounded-in")
            # vocab
            base = r[4:] if r.startswith("not-") else r
            if base not in RELATIONS: viol["bad-relation"].append(f"{bid}:{ln} {r}")
            if b and b not in BASIS: viol["bad-basis"].append(f"{bid}:{ln} {b}")
            for fn, fa in flags.items():
                if fn not in FLAGS: viol["bad-flag"].append(f"{bid}:{ln} !{fn}")
            if "confidence" in kv: viol["confidence-field"].append(f"{bid}:{ln}")
            if "__malformed__" in kv: viol["malformed-field"].append(f"{bid}:{ln}")
            # field order
            ks = [k for k in order if k != "!"]
            idx = [ORDER.index(k) for k in ks if k in ORDER]
            if idx != sorted(idx): viol["field-order"].append(f"{bid}:{ln}")
            if "!" in order and order.index("!") < len(ks): pass
            # asof
            if kv.get("asof") and kv["asof"] != bid: viol["asof-mismatch"].append(f"{bid}:{ln} {kv['asof']}")
            # inferred <=> no ground
            if b == "inferred" and g: viol["inferred-with-ground"].append(f"{bid}:{ln}")
            if g and b == "inferred": pass
            # untethered tagged
            if b in NEEDS_GROUND and not g and not (flags.get("untethered") or flags.get("deprecated")):
                viol["untethered-untagged"].append(f"{bid}:{ln}")
            # not-R contradiction
            key = (base, s, o, kv.get("asof"))
            if r.startswith("not-"):
                if ("POS",) + key in rel_pairs: viol["R-and-notR"].append(f"{bid}:{ln}")
                rel_pairs.add(("NEG",) + key)
            else:
                if ("NEG",) + key in rel_pairs: viol["R-and-notR"].append(f"{bid}:{ln}")
                rel_pairs.add(("POS",) + key)
            for h in (s, o):
                if h.startswith("anchor."): used_anchors.add(h)
            # grounding
            if g: ng += 1
            if g and "#" in g and not g.startswith("workbench:"):
                ca += 1
                pre, node = g.split("#", 1)
                bk, _, fp = pre.partition(":")
                if bk != bid: viol["ground-book-mismatch"].append(f"{bid}:{ln} {bk}")
                if re.match(r"^L?\d+$", node.strip()): viol["line-number-anchor"].append(f"{bid}:{ln}")
                full = os.path.join(cfg, fp) if cfg else None
                if not full or not os.path.exists(full):
                    unres += 1; viol["ground-file-missing"].append(f"{bid}:{ln} {fp}")
                elif fp.endswith((".yaml", ".yml")):
                    doc, how = load_yaml(full)
                    if how == "lenient": lenient_books.add(bid)
                    if doc is None: unres += 1; viol["ground-unparseable"].append(f"{bid}:{ln} {fp}")
                    else:
                        _, ok = walk(doc, node)
                        res += 1 if ok else 0; unres += 0 if ok else 1
                        if not ok and len(viol["ground-unresolved"]) < 400:
                            viol["ground-unresolved"].append(f"{bid}:{ln} {fp}#{node[:70]}")
                elif fp.endswith(".md"):
                    ok = md_has(full, node); res += 1 if ok else 0; unres += 0 if ok else 1
                    if not ok and len(viol["ground-unresolved-md"]) < 100:
                        viol["ground-unresolved-md"].append(f"{bid}:{ln} {fp}#{node[:50]}")
                else:
                    res += 1
            # HELD-OUT gate
            hset = held.get(bid, set())
            if hset and b == "declared":
                blob = f"{s} {o} {g or ''}"
                for t in hset:
                    tl = t.lower()
                    if len(tl) < 4: continue
                    if tl in blob.lower() or tl.replace("_", "-") in blob.lower():
                        hits_bad += 1
                        viol["HELD-OUT-ASSERTED"].append(f"{bid}:{ln} [{t}] {line[:110]}")
                        break
            elif hset and b != "declared":
                blob = f"{s} {o} {g or ''}".lower()
                if any(len(t) >= 4 and t.lower() in blob for t in hset): hits_ok += 1
        missing_reg = sorted(used_anchors - reg)
        if missing_reg: viol["anchor-not-registered"] += [f"{bid}: {m}" for m in missing_reg[:5]]
        rows.append((bid, n, ng, ca, res, unres, len(reg), len(used_anchors), hits_ok, hits_bad, basis_c))
        for k, v in basis_c.items(): tot[k] += v

    print("=" * 108)
    print("GROUNDING ROUND-TRIP + REGISTRY")
    print(f"  {'book':22} {'units':>6} {'ground':>7} {'cfgAnc':>7} {'resolv':>7} {'UNRES':>6} {'reg':>5} {'used':>5} {'heldOK':>7} {'heldBAD':>8}")
    print("  " + "-" * 100)
    T = [0] * 8
    for (bid, n, ng, ca, res, unres, reg, used, hok, hbad, _) in rows:
        print(f"  {bid:22} {n:>6} {ng:>7} {ca:>7} {res:>7} {unres:>6} {reg:>5} {used:>5} {hok:>7} {hbad:>8}")
        for i, v in enumerate((n, ng, ca, res, unres, reg, used, hbad)): T[i] += v
    print("  " + "-" * 100)
    print(f"  {'TOTAL':22} {T[0]:>6} {T[1]:>7} {T[2]:>7} {T[3]:>7} {T[4]:>6} {T[5]:>5} {T[6]:>5} {'':>7} {T[7]:>8}")
    rate = 100.0 * T[3] / T[2] if T[2] else 0
    print(f"\n  config-anchor resolution: {T[3]}/{T[2]} = {rate:.2f}%")
    if lenient_books: print(f"  lenient YAML needed for: {sorted(lenient_books)}")

    print("\n" + "=" * 108)
    print("BASIS DISTRIBUTION (all books)")
    for k, v in tot.most_common(): print(f"  {k:18} {v:>6}  ({100.0*v/T[0]:.1f}%)")

    print("\n" + "=" * 108)
    print("INVARIANT VIOLATIONS")
    order = ["HELD-OUT-ASSERTED","confidence-field","inferred-with-ground","untethered-untagged",
             "bad-relation","bad-basis","bad-flag","field-order","asof-mismatch","duplicate-unit",
             "R-and-notR","line-number-anchor","ground-book-mismatch","ground-file-missing",
             "ground-unparseable","anchor-not-registered","malformed","malformed-field"]
    clean = True
    for k in order:
        v = viol.get(k, [])
        mark = "OK " if not v else "!! "
        if v: clean = False
        print(f"  {mark}{k:24} {len(v)}")
        for x in v[:6]: print(f"        {x}")
    ur = viol.get("ground-unresolved", []); urm = viol.get("ground-unresolved-md", [])
    print(f"\n  unresolved yaml node-paths: {T[4]} total (samples below)")
    for x in ur[:15]: print(f"        {x}")
    for x in urm[:5]: print(f"     md {x}")
    print("\nAUDIT", "CLEAN" if clean and T[4] == 0 else "HAS FINDINGS")

if __name__ == "__main__":
    main()

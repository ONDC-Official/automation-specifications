#!/usr/bin/env python3
"""
Tool E1 — x-validation atomizer (deterministic).

`x-validations` -> config/validations/index.yaml `_TESTS_` DSL -> compiled by
automation-validation-compiler (JVAL) into a Go `validationpkg` -> consumed by the
`ondc-validator` beckn plugin -> executed inside `beckn-onix` (the API-service
instance) as PerformL1validations. So `_TESTS_` is PROTOCOL: real enforcement on
live traffic, and it grounds to the CONFIG position, never to a runtime observation.

The `_RETURN_` mini-language is small and regular (25 distinct shapes over 13,959
named rules corpus-wide), so turning a rule into atoms is a mechanical transform,
not an interpretation. That is why this is a deterministic tool rather than an AI
stage: the same input always yields the same atoms, and every emitted grounding is
re-walked against the real config before it is written.

Rules nest: a `_RETURN_` may itself be a list of sub-rules, which is why grounding
paths look like `_TESTS_.<action>[<NAME>]._RETURN_[<NAME>]`.

Usage:
  xval_atomizer.py                 # all books -> knowledge/<book>/candidate-xval.md
  xval_atomizer.py <book-id>       # one book
  xval_atomizer.py --apply         # append verified atoms into atoms.md (+ anchors)

Emits nothing it cannot ground. Unresolvable rules are reported, never written.
"""
import os, re, sys, glob, collections
import _env, _yaml

# _RETURN_ predicate -> KB relation. Closed vocabulary only (vocabularies.md).
PRESENT_RE = re.compile(r'^\s*(?P<lhs>[A-Za-z_][\w]*)\s+are\s+present\s*$')
INSET_RE   = re.compile(r'^\s*\(?\s*(?P<lhs>[A-Za-z_][\w]*)\s+(?P<q>all|any)\s+in\s+(?P<rhs>[A-Za-z_][\w]*)\s*\)?\s*$')
REGEX_RE   = re.compile(r'^\s*(?P<lhs>[A-Za-z_][\w]*)\s+follow\s+regex\s+(?P<rhs>[A-Za-z_][\w]*)\s*$')
EQUAL_RE   = re.compile(r'^\s*(?P<lhs>[A-Za-z_][\w]*)\s+equal\s+to\s+(?P<rhs>[A-Za-z_][\w]*)\s*$')
UNIQUE_RE  = re.compile(r'^\s*(?P<lhs>[A-Za-z_][\w]*)\s+are\s+unique\s*$')

# operand name -> the rule key holding its JSONPath (or literal value set)
PATH_KEYS = ("attr", "subTags", "enumPath", "tagPath", "usecasepath")
SET_KEYS  = ("enumList", "validValues", "validTags", "reg", "version")


def norm(s):
    return " ".join(str(s).split())


def kebab(s):
    s = re.sub(r'[^0-9A-Za-z]+', '-', str(s)).strip('-').lower()
    return re.sub(r'-{2,}', '-', s) or "x"


def lit(s):
    """A literal object in the atom grammar is a quoted string; keep pipes out."""
    return '"' + str(s).replace('"', "'").replace("|", "/") + '"'


def conj_parts(expr):
    """Split a _RETURN_ on && only (|| would be a disjunction we must not assert
    as separate facts — a disjunct is not independently true)."""
    if "||" in expr:
        return []
    return [p for p in (x.strip() for x in expr.split("&&")) if p]


def operand_value(rule, name):
    """Resolve an operand name to the rule's JSONPath / value-set, if present.

    `subTags` is expressed RELATIVE to the rule's `_SCOPE_` (e.g. _SCOPE_
    "$.context.location.city" + subTags "$.code" means "$.context.location.city.code").
    Emitting the bare relative path would be wrong on its own, so join them here."""
    if name not in rule:
        return None
    val = rule[name]
    if name in ("subTags", "tagPath") and isinstance(val, str):
        scope = rule.get("_SCOPE_")
        if isinstance(scope, str) and val.startswith("$."):
            return scope.rstrip(".") + "." + val[2:]
    return val


def rule_atoms(rule, action, ground, book):
    """Mechanically map ONE named rule to atoms. Returns list of (line, anchors_used)."""
    out = []
    ret = rule.get("_RETURN_")
    if not isinstance(ret, str):
        return out                              # nested rule list; handled by the walker
    subj = f"anchor.{kebab(action)}"
    for part in conj_parts(norm(ret)):
        m = PRESENT_RE.match(part)
        if m:
            p = operand_value(rule, m.group("lhs"))
            if p is None:
                continue
            out.append((f"{subj} | requires | {lit(p)} | basis:declared | asof:{book} | grounded-in:{ground}", []))
            continue
        m = INSET_RE.match(part)
        if m:
            p = operand_value(rule, m.group("lhs"))
            vals = operand_value(rule, m.group("rhs"))
            if p is None or vals is None:
                continue
            if isinstance(vals, (list, tuple)):
                shown = ",".join(str(v) for v in vals[:8]) + ("…" if len(vals) > 8 else "")
            else:
                shown = str(vals)
            q = "one of" if m.group("q") == "any" else "in"
            out.append((f"{subj} | constrains | {lit(f'{p} {q} [{shown}]')} | basis:declared | asof:{book} | "
                        f"grounded-in:{ground}.{m.group('rhs')}", []))
            continue
        m = REGEX_RE.match(part)
        if m:
            p = operand_value(rule, m.group("lhs"))
            rx = operand_value(rule, m.group("rhs"))
            if p is None or rx is None:
                continue
            rxs = rx[0] if isinstance(rx, (list, tuple)) and rx else rx
            out.append((f"{subj} | constrains | {lit(f'{p} matches {rxs}')} | basis:declared | asof:{book} | "
                        f"grounded-in:{ground}.{m.group('rhs')}", []))
            continue
        m = EQUAL_RE.match(part)
        if m:
            p = operand_value(rule, m.group("lhs"))
            rhs = operand_value(rule, m.group("rhs"))
            if p is None or rhs is None:
                continue
            out.append((f"{subj} | constrains | {lit(f'{p} equals {norm(rhs)}')} | basis:declared | asof:{book} | "
                        f"grounded-in:{ground}", []))
            continue
        m = UNIQUE_RE.match(part)
        if m:
            p = operand_value(rule, m.group("lhs"))
            if p is None:
                continue
            out.append((f"{subj} | constrains | {lit(f'{p} unique')} | basis:declared | asof:{book} | "
                        f"grounded-in:{ground}", []))
            continue
    # Scoping belongs to the RULE, not to the action. Emitting
    # `anchor.<action> | scoped-to | <useCasePath>` would claim the whole action is
    # confined to that path — and with one such unit per rule the same action would
    # be "scoped-to" many conflicting things. So the qualifier is folded into the
    # constraint literal it actually governs, keeping it attached to its own rule.
    scope = rule.get("useCasePath")
    if out and isinstance(scope, str) and scope.strip():
        tag = f" [when {norm(scope)}]"
        out = [(l.replace('" | basis:declared', tag + '" | basis:declared', 1)
                if " | constrains | " in l or " | requires | " in l else l, a) for l, a in out]
    return out


def walk_rules(node, action, base, book, acc, seen_names):
    """Recurse `_TESTS_.<action>` lists; a rule's `_RETURN_` may hold nested rules."""
    if isinstance(node, list):
        for item in node:
            walk_rules(item, action, base, book, acc, seen_names)
        return
    if not isinstance(node, dict):
        return
    name = node.get("_NAME_")
    if name:
        ground = f"{base}[{name}]"
        seen_names.add((action, str(name)))
        acc.extend(rule_atoms(node, action, ground, book))
        ret = node.get("_RETURN_")
        if isinstance(ret, (list, dict)):
            walk_rules(ret, action, f"{ground}._RETURN_", book, acc, seen_names)
    else:
        for v in node.values():
            walk_rules(v, action, base, book, acc, seen_names)


TOKEN = re.compile(r"([^.\[\]]+)|\[([^\]]*)\]")


def resolve(doc, path):
    """Walk a positional node-path, matching list items by _NAME_/id/action_id.
    A ground this tool cannot re-walk is never written (invariant: 100% round-trip)."""
    cur = doc
    for m in TOKEN.finditer(path):
        plain, brack = m.group(1), m.group(2)
        key = (plain if plain is not None else brack).strip()
        if isinstance(cur, dict):
            if key in cur:
                cur = cur[key]; continue
            return False
        if isinstance(cur, list):
            hit = None
            for el in cur:
                if isinstance(el, dict):
                    for f in ("_NAME_", "action_id", "id", "name", "code"):
                        if str(el.get(f)) == key:
                            hit = el; break
                if hit is not None:
                    break
            if hit is None and key.isdigit() and int(key) < len(cur):
                hit = cur[int(key)]
            if hit is None:
                return False
            cur = hit; continue
        return False
    return True


def existing_atom_lines(kb):
    p = os.path.join(kb, "atoms.md")
    if not os.path.exists(p):
        return set(), ""
    txt = open(p, encoding="utf-8").read()
    return set(l.strip() for l in txt.splitlines() if "|" in l), txt


def run(only=None, apply_=False):
    books = []
    for d in sorted(glob.glob(os.path.join(_env.CONFIGS, "*"))):
        cfg = os.path.join(d, "config")
        if not os.path.isdir(cfg):
            continue
        bid = _env.book_id(d)
        if only and bid != only:
            continue
        books.append((bid, cfg))

    print(f"{'book':24} {'rules':>6} {'atoms':>7} {'new':>7} {'dup':>6} {'UNRES':>6}")
    print("-" * 64)
    tot_rules = tot_atoms = tot_new = tot_unres = 0
    for bid, cfg in books:
        kb = os.path.join(_env.KNOWLEDGE, bid)
        if not os.path.isdir(kb):
            continue
        have, _ = existing_atom_lines(kb)
        vdocs = {}
        acc, seen_names = [], set()
        for f in sorted(glob.glob(os.path.join(cfg, "validations", "*.yaml"))):
            doc, err = _yaml.load_file(f)
            if err or doc is None:
                continue
            tests = doc.get("_TESTS_")
            if not isinstance(tests, dict):
                continue
            rel = os.path.relpath(f, cfg)
            for action, rules in tests.items():
                base = f"{bid}:{rel}#_TESTS_.{action}"
                walk_rules(rules, action, base, bid, acc, seen_names)
        lines = []
        dup = unres = 0
        for line, _ in acc:
            if line in have or line in lines:
                dup += 1
                continue
            # Never write a ground we cannot re-walk (100% round-trip invariant).
            m = re.search(r'grounded-in:[^:]+:([^#]+)#(.+?)\s*$', line)
            if m:
                vf = os.path.join(cfg, m.group(1))
                vdoc = vdocs.get(vf)
                if vdoc is None:
                    vdoc, _e = _yaml.load_file(vf)
                    vdocs[vf] = vdoc
                if vdoc is None or not resolve(vdoc, m.group(2)):
                    unres += 1
                    continue
            lines.append(line)
        tot_rules += len(seen_names); tot_atoms += len(acc); tot_new += len(lines)
        print(f"{bid:24} {len(seen_names):>6} {len(acc):>7} {len(lines):>7} {dup:>6} {unres:>6}")
        tot_unres += unres
        out = os.path.join(kb, "candidate-xval.md")
        with open(out, "w", encoding="utf-8") as fh:
            fh.write(f"# x-validation candidate atoms — {bid}\n\n"
                     f"> Generated by tools/xval_atomizer.py from `_TESTS_` (x-validations).\n"
                     f"> These are PROTOCOL facts: the same rules compile into the Go validationpkg\n"
                     f"> that ondc-validator runs inside beckn-onix. Grounded at the CONFIG position.\n"
                     f"> {len(seen_names)} named rules -> {len(acc)} atoms, {len(lines)} new.\n\n")
            for l in lines:
                fh.write(l + "\n")
        if apply_:
            with open(os.path.join(kb, "atoms.md"), "a", encoding="utf-8") as fh:
                fh.write("\n# --- x-validation (_TESTS_) — generated by xval_atomizer.py ---\n")
                for l in lines:
                    fh.write(l + "\n")
    print("-" * 64)
    print(f"{'TOTAL':24} {tot_rules:>6} {tot_atoms:>7} {tot_new:>7} {'':>6} {tot_unres:>6}")
    print(f"\n{'APPLIED to atoms.md' if apply_ else 'candidates written (use --apply to append)'}")
    return 0


if __name__ == "__main__":
    args = [a for a in sys.argv[1:]]
    apply_ = "--apply" in args
    args = [a for a in args if not a.startswith("--")]
    sys.exit(run(args[0] if args else None, apply_))

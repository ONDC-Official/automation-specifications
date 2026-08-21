#!/usr/bin/env python3
"""
Tool C.classify — 3-Tier Difference Classifier (KEP, B2).
Every cross-book difference is routed to exactly one tier:
  invariant      -> matches the Beckn base/skeleton; map directly
  authoring-style-> same meaning, different writing; NORMALIZE (rule attached)
  semantic       -> genuinely different meaning; PRESERVE, scoped-to domain
Rules (skeleton): strictness(additionalProperties)->closed · $ref vs wrapper->collapse ·
enums->union+dedupe hyphen/underscore, canonical case · near-universal field->core ·
domain-only field / different enum values / entry actions / search mode -> semantic.
Inputs: the 3 book OpenAPI schemas + signatures.json + sequence-graph.json.
Output: classification.json.
"""
import os, re, sys, glob, json
import _env, _yaml
HERE = os.path.dirname(os.path.abspath(__file__))
REF = _env.CONFIGS
CMP = _env.WORK

# discover config books generically (no hardcoded book set); exclude framework/vendor
VENDOR = ("automation-framework","node_modules","/packages/","api-service","mock-service")
def discover():
    out = {}
    for idx in glob.glob(os.path.join(REF, "**", "config", "index.yaml"), recursive=True):
        if any(v in idx for v in VENDOR): continue
        cfg = os.path.dirname(idx)
        if os.path.exists(os.path.join(cfg, "specs/openapi.yaml")) and os.path.exists(os.path.join(cfg, "attributes/index.yaml")):
            name = re.sub(r"^automation-specifications-release-eks-", "", os.path.basename(os.path.dirname(cfg)))
            out[name] = cfg
    return out
BOOKS = discover()
if len(BOOKS) < 2:
    print(f"DEGRADED: {len(BOOKS)} book(s) — cross-book classification needs ≥2. "
          f"Single book → every schema is core (no cross-book diff). Nothing to classify.")
    sys.exit(0)

def schemas(cfg):
    d = _yaml.load(os.path.join(cfg, "specs/openapi.yaml"))
    return (d.get("components",{}) or {}).get("schemas",{}) or {}
REL = BOOKS                       # {name: config_dir}
S = {r: schemas(cfg) for r, cfg in BOOKS.items()}

SPELLING = {"multiple_sumbissions":"multiple_submissions"}   # known typos → canonical
def lp(sc):
    p = {}
    if isinstance(sc, dict):
        p.update(sc.get("properties") or {})
        for a in sc.get("allOf",[]) or []:
            if isinstance(a, dict): p.update(a.get("properties") or {})
    return {SPELLING.get(k, k): v for k, v in p.items()}   # normalize known-typo keys

# IGM feature-module schema set (from the derived base) — absence = minification, not semantics
try:
    _base = _yaml.load(_env.BECKN_BASE)
    MODULE_SCHEMAS = set((_base.get("x-module-schemas", {}) or {}).get("IGM", []))
except Exception:
    MODULE_SCHEMAS = set()

def norm_enum(vals): return {str(v).upper().replace("_","-") for v in (vals or [])}

def classify_prop(variants):
    """variants: {book: def}. Base = the union, so every schema field is CORE.
    Fields differ only in how they're written (authoring) or in mere presence
    (still core, in base). No schema field is 'semantic' — only behaviour is."""
    defs = list(variants.values()); present = set(variants); absent = set(REL) - present
    # present only in some books — but it IS in the base (union) → core
    if absent:
        return ("invariant", f"in base core (union); populated in {'/'.join(present)}")
    def strip_ap(d): return {k:v for k,v in d.items() if k!="additionalProperties"} if isinstance(d,dict) else d
    if all(isinstance(d,dict) for d in defs):
        if len({json.dumps(strip_ap(d),sort_keys=True) for d in defs}) == 1:
            return ("authoring-style","strictness (additionalProperties) → adopt closed")
        def is_ref(d): return set(d.keys())=={"$ref"} or ("allOf" in d and len(d["allOf"])==1)
        if any(is_ref(d) for d in defs):
            return ("authoring-style","$ref vs allOf/anyOf wrapper → collapse to $ref")
        if all("enum" in d for d in defs):
            norms = [norm_enum(d["enum"]) for d in defs]
            if all(n==norms[0] for n in norms):
                return ("authoring-style","enum casing / hyphen-underscore → canonical form")
            return ("authoring-style","enum values differ → union in base (+dedupe)")
        if all("properties" in d for d in defs):
            return ("authoring-style","nested object differs → union in base (superset)")
    return ("authoring-style","definition union in base")

def run():
    report = {"invariant":[], "authoring-style":[], "semantic":[]}
    module_count = 0
    # ---- Beckn schema layer (classified against the BASE = union → schema is CORE) ----
    names = sorted(set().union(*[set(s.keys()) for s in S.values()]))
    common = set.intersection(*[set(s.keys()) for s in S.values()])
    for n in names:
        if n not in common:
            holders = [r for r in REL if n in S[r]]
            if n in MODULE_SCHEMAS:
                module_count += 1
                report["invariant"].append({"item":f"schema:{n}","rule":f"IGM module — in base core (activation-tagged; used {'/'.join(holders)})"})
            else:
                report["invariant"].append({"item":f"schema:{n}","rule":f"in base core (union); used {'/'.join(holders)}"})
            continue
        propsets = {r: lp(S[r][n]) for r in REL}
        allkeys = set().union(*[set(p) for p in propsets.values()])
        divergent = False
        for k in sorted(allkeys):
            variants = {r: propsets[r][k] for r in REL if k in propsets[r]}
            sers = {json.dumps(v,sort_keys=True) for v in variants.values()}
            if len(variants)==len(REL) and len(sers)==1:
                continue  # this property identical
            divergent = True
            tier, rule = classify_prop(variants)
            report[tier].append({"item":f"{n}.{k}","rule":rule})
        if not divergent:
            report["invariant"].append({"item":f"schema:{n}","rule":"identical across all books"})
    # ---- structural signals ----
    sig = json.load(open(os.path.join(CMP,"signatures.json")))
    # error field order
    orders = {r.split('-')[0]: v["errors"]["field_order"] for r,v in sig.items()}
    sets = {r: set(v["errors"]["field_set"]) for r,v in sig.items()}
    if len({tuple(o) for o in orders.values()})>1 and len({frozenset(s) for s in sets.values()})==1:
        report["authoring-style"].append({"item":"errors.field_order","rule":"same 4 fields, different order → canonical order"})
    else:
        report["invariant"].append({"item":"errors.field_set","rule":"identical error fields"})
    # validation root shape
    roots = {r: tuple(sorted(v["validations"]["root_keys"])) for r,v in sig.items()}
    report["invariant" if len(set(roots.values()))==1 else "authoring-style"].append(
        {"item":"validations.root_shape","rule":"uniform _TESTS_/_SESSION_DATA_ across books" if len(set(roots.values()))==1 else "root-shape differs → normalize"})
    # entry actions (semantic)
    seq = json.load(open(os.path.join(CMP,"sequence-graph.json")))
    entries = {b.split('-')[0]: tuple(r["entry_actions"]) for b,r in seq.items()}
    if len(set(entries.values()))>1:
        report["semantic"].append({"item":"transaction.entry_actions","rule":f"differ by domain {dict(entries)} → search-mode semantics, preserve"})
    # search mode signal (bpp_* on search) — semantic, from context_keys
    ck = {r: set(v["flow"].get("context_keys",[])) for r,v in sig.items()}
    has_bpp = {r: ("bpp_id" in s and "bpp_uri" in s) for r,s in ck.items()}
    if len(set(has_bpp.values()))>1:
        report["semantic"].append({"item":"context.bpp_id + context.bpp_uri on search",
            "rule":"BOTH bpp_id & bpp_uri present = P2P/directed; both absent = broadcast → preserve search mode"})

    tally = {k:len(v) for k,v in report.items()}
    tally["_igm_in_core"] = module_count
    report["_tally"] = tally
    json.dump(report, open(os.path.join(CMP,"classification.json"),"w"), indent=2)
    print("TALLY:", tally)
    for tier in ("invariant","authoring-style","semantic"):
        print(f"\n=== {tier} ({tally[tier]}) ===")
        for e in report[tier][:8]:
            print(f"  {e['item']:34} {e['rule']}")
        if tally[tier]>8: print(f"  … +{tally[tier]-8} more")

if __name__ == "__main__":
    run()

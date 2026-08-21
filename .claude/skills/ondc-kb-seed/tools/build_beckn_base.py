#!/usr/bin/env python3
"""
Derive the union Beckn base spec from the 4 releases.
- Union of components/schemas across FIS12/13/14/TRV14.
- Property-level merge per schema (superset of fields seen anywhere).
- Known-typo normalization to the Beckn-correct form (not majority vote).
- Provenance map: every schema + divergent property -> contributing releases (groundable).
DERIVED artifact — regenerate before seeding; never hand-edit the outputs.
"""
import os, json, yaml, _env
import _env
HERE = os.path.dirname(os.path.abspath(__file__))
# BOOTSTRAP utility: in real execution beckn-base.yaml is a PROVIDED input (common-config/).
# This regenerates it as the union of the config books when it isn't provided.
BOOKS = {_env.book_id(b): b for b in _env.discover_books()}    # {id: book_dir}
REL = BOOKS
PRIORITY = list(BOOKS.keys())
SPELLING = {"multiple_sumbissions":"multiple_submissions"}     # canonical from Beckn base, not majority

def spec(r):
    return yaml.safe_load(open(os.path.join(REL[r], "config/specs/openapi.yaml")))
SPEC = {r: spec(r) for r in REL}
def schemas(r): return (SPEC[r].get("components",{}) or {}).get("schemas",{}) or {}
def paths(r):   return SPEC[r].get("paths",{}) or {}

S = {r: schemas(r) for r in REL}
P = {r: paths(r) for r in REL}
all_names = sorted(set().union(*[set(s.keys()) for s in S.values()]))

def local_props(schema):
    """properties dict from a schema, merging allOf-local property blocks; also refs."""
    props, refs = {}, []
    if not isinstance(schema, dict): return props, refs
    for k,v in (schema.get("properties") or {}).items(): props[k]=v
    for sub in schema.get("allOf",[]) or []:
        if isinstance(sub, dict):
            if "$ref" in sub: refs.append(sub["$ref"])
            for k,v in (sub.get("properties") or {}).items(): props.setdefault(k,v)
    return props, refs

def canon(key): return SPELLING.get(key, key)

base_schemas = {}
prov = {}
for name in all_names:
    holders = [r for r in PRIORITY if name in S[r]]
    merged_props = {}
    refs = set()
    prop_sources = {}     # canonical prop -> [releases]
    divergent = {}        # canonical prop -> releases whose def differs from chosen
    chosen_def = {}       # canonical prop -> json-serialized chosen def
    for r in holders:
        p, rf = local_props(S[r][name])
        refs |= set(rf)
        for rawk, v in p.items():
            k = canon(rawk)
            prop_sources.setdefault(k, []).append(r)
            ser = json.dumps(v, sort_keys=True)
            if k not in chosen_def:
                chosen_def[k] = ser; merged_props[k] = v
            elif chosen_def[k] != ser:
                divergent.setdefault(k, []).append(r)
    # assemble base schema
    if refs and merged_props:
        base_schemas[name] = {"allOf": [{"$ref": r} for r in sorted(refs)] +
                                        [{"type":"object","properties":merged_props}]}
    elif refs:
        base_schemas[name] = {"allOf": [{"$ref": r} for r in sorted(refs)]}
    elif merged_props:
        base_schemas[name] = {"type":"object","properties":merged_props}
    else:
        # scalar/enum/other — take highest-priority full definition
        base_schemas[name] = S[holders[0]][name] if holders else {}
    prov[name] = {
        "sources": holders,
        "universal": len(holders) == len(REL),
        "prop_sources": {k: sorted(set(v)) for k,v in prop_sources.items()},
        "divergent_props": {k: sorted(set(v)) for k,v in divergent.items()},
        "spelling_fixed": [rk for rk in SPELLING if any(rk in local_props(S[r][name])[0] for r in holders)],
    }

# module tagging (IGM = schemas/paths absent from the minified FIS14 core)
core_names = set.intersection(*[set(s.keys()) for s in S.values()])
igm_names = sorted(set(all_names) - core_names)

# ---- union of PATHS (IGM paths included in the base) ----
all_paths = sorted(set().union(*[set(p.keys()) for p in P.values()]))
core_paths = set.intersection(*[set(p.keys()) for p in P.values()])
igm_paths = sorted(p for p in all_paths if p.strip("/") in
                   {"issue","issue_status","on_issue","on_issue_status"})
base_paths = {}
path_prov = {}
for pk in all_paths:
    holders = [r for r in PRIORITY if pk in P[r]]
    base_paths[pk] = P[holders[0]][pk]          # priority-release definition
    path_prov[pk] = {"sources": holders, "universal": len(holders) == len(REL),
                     "module": "IGM" if pk in igm_paths else None}

# ---------------------------------------------------------------------------
# CANONICALIZATION PASS — apply the reviewed resolution rules to the 12 divergent
# schemas so the base is authoritative. (divergence-resolution.md §2/§3)
# PRIORITY=TRV14-first already yields: additionalProperties:false (strictness),
# rating_category UPPERCASE, clean Payment.type, and $ref structures. Remaining:
#   - enum supersets (Payment.status, Order.status) -> union + dedupe twins
#   - Payment.params nested union (superset), closed
#   - collapse single-member allOf/anyOf -> direct $ref (R4: Item.quantity)
#   - Form.data -> additionalProperties:true (R5, free-form exception)
# ---------------------------------------------------------------------------
canon_log = []
def prop_defs(name, key):
    out = {}
    for r in REL:
        if name in S[r]:
            d = local_props(S[r][name])[0].get(key)
            if d is not None: out[r] = d
    return out
def dedupe_enum(vals):
    groups = {}
    for v in vals:
        groups.setdefault(v.replace("_","-"), []).append(v)   # hyphen/underscore twins
    return sorted(k if k in vs else vs[0] for k, vs in groups.items())
def set_prop(schema, key, val):
    tgt = schema
    if "allOf" in schema:
        tgt = next((b for b in schema["allOf"] if isinstance(b, dict) and "properties" in b), None)
    if tgt is None or "properties" not in tgt: return False
    tgt["properties"][key] = val; return True

# enum supersets (union across releases, twins deduped)
for schn, key in [("Payment","status"), ("Order","status")]:
    vals = []
    for r, d in prop_defs(schn, key).items():
        for v in (d.get("enum") or []):
            if v not in vals: vals.append(v)
    if vals:
        du = dedupe_enum(vals)
        if set_prop(base_schemas[schn], key, {"type":"string",
                    "description":"Status of the "+schn.lower(), "enum":du}):
            canon_log.append(f"{schn}.{key}: enum union -> {du}")

# Payment.params nested union, closed
pp = {}
for r, d in prop_defs("Payment","params").items():
    for k, v in (d.get("properties") or {}).items(): pp.setdefault(k, v)
if pp and set_prop(base_schemas["Payment"], "params",
                   {"type":"object","additionalProperties":False,"properties":pp}):
    canon_log.append(f"Payment.params: nested union ({len(pp)} fields), closed")

# collapse single-member allOf/anyOf -> direct $ref, across all schemas
def collapse_ref(v):
    """Collapse ONLY a single-member wrapper that is purely a $ref (no sibling
    property blocks) -> {$ref}. Preserves legitimate ref+extension allOf."""
    if not isinstance(v, dict): return v
    for wrap in ("allOf","anyOf"):
        members = v.get(wrap)
        if isinstance(members, list) and len(members) == 1 and isinstance(members[0], dict):
            m = members[0]
            if set(m.keys()) == {"$ref"}:
                return {"$ref": m["$ref"]}
            if set(m.keys()) == {"allOf"} and isinstance(m["allOf"], list) and len(m["allOf"]) == 1 \
               and set(m["allOf"][0].keys()) == {"$ref"}:
                return {"$ref": m["allOf"][0]["$ref"]}
    return v
collapsed = 0
for sn, sc in base_schemas.items():
    tgt = sc
    if "allOf" in sc:
        tgt = next((b for b in sc["allOf"] if isinstance(b, dict) and "properties" in b), None)
    if isinstance(tgt, dict):
        for k, v in list((tgt.get("properties") or {}).items()):
            nv = collapse_ref(v)
            if nv is not v and nv != v:
                tgt["properties"][k] = nv; collapsed += 1
if collapsed: canon_log.append(f"collapsed {collapsed} single-ref allOf/anyOf wrappers -> $ref")

# Form.data free-form (R5 exception)
if set_prop(base_schemas.get("Form", {}), "data",
            {"type":"object","additionalProperties":True,"description":"The form submission data (free-form)"}):
    canon_log.append("Form.data: additionalProperties:true (free-form exception)")

base_doc = {
 "openapi":"3.0.0",
 "info":{"title":"ONDC Beckn Base (derived union, canonicalized)","version":"0.2.0",
   "description":"DERIVED + CANONICALIZED union of components/schemas across "
                 "FIS13/FIS14/TRV14 (FIS12 excluded — deprecated/partial manifest). "
                 "Regenerate with build_beckn_base.py; do not hand-edit. "
                 "Provenance in beckn-base.provenance.json."},
 "x-derived-from":{r:{"domain":REL[r]} for r in REL},
 "x-canonicalization":canon_log,
 "x-core-schema-count":len(core_names),
 "x-module-schemas":{"IGM":igm_names},
 "x-module-paths":{"IGM":igm_paths},
 "paths": {k: base_paths[k] for k in all_paths},
 "components":{"schemas": {k: base_schemas[k] for k in all_names}},
}
os.makedirs(_env.COMMON, exist_ok=True)
yaml.safe_dump(base_doc, open(_env.BECKN_BASE,"w"), sort_keys=True, default_flow_style=False)
json.dump({"generated_from":{r:REL[r] for r in REL},
           "core_schema_count":len(core_names),
           "total_schema_count":len(all_names),
           "total_path_count":len(all_paths),
           "core_path_count":len(core_paths),
           "module_IGM_schemas":igm_names,
           "module_IGM_paths":igm_paths,
           "schemas":prov,
           "paths":path_prov},
          open(os.path.join(_env.COMMON,"beckn-base.provenance.json"),"w"), indent=2)

# summary
universal = [n for n in all_names if prov[n]["universal"]]
divergent_schemas = [n for n in all_names if prov[n]["divergent_props"]]
print(f"total schemas in base: {len(all_names)}")
print(f"universal (in all {len(REL)}):  {len(universal)}")
print(f"IGM-module schemas:    {len(igm_names)} -> {igm_names[:8]}...")
print(f"total paths in base:   {len(all_paths)} (core {len(core_paths)}, IGM {len(igm_paths)} -> {igm_paths})")
print(f"schemas with divergent prop defs: {len(divergent_schemas)} -> {divergent_schemas}")
print(f"spelling normalized: multiple_sumbissions -> multiple_submissions where present")
print("\ncanonicalization applied:")
for c in canon_log: print("  -", c)
# verification of the decided outcomes
bs = base_schemas
def has(schema, key):
    t = schema.get("allOf") and next((b for b in schema["allOf"] if "properties" in b), {}) or schema
    return (t.get("properties") or {}).get(key)
print("\nverify (authoritative outcomes):")
print("  Item.quantity is $ref:", has(bs["Item"],"quantity"))
print("  Rating.rating_category enum[:3]:", (has(bs["Rating"],"rating_category") or {}).get("enum",[])[:3])
print("  Payment.status enum:", (has(bs["Payment"],"status") or {}).get("enum"))
print("  Form.data additionalProperties:", (has(bs["Form"],"data") or {}).get("additionalProperties"))
print("  ItemQuantity.selected additionalProperties:", (has(bs["ItemQuantity"],"selected") or {}).get("additionalProperties"))
print("\nwrote beckn-base.yaml + beckn-base.provenance.json")

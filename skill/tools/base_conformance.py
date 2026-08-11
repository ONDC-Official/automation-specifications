#!/usr/bin/env python3
"""
Base-conformance gate (KEP). beckn-base.yaml is the HUMAN-OWNED authority.
The skill grounds against it and NEVER rewrites it. This tool checks each config
book against the base and RAISES deviations: a schema / field / enum value a config
uses that the base does not cover. On any deviation the skill must STOP seeding the
deviating element and ask the USER to update common-config/beckn-base.yaml manually.

PATCH (inline-schema harvest): some release books declare NO components.schemas and
instead inline their request/response schemas under paths.*.*.requestBody/responses.
The original comparison read components.schemas only, so those books compared an empty
dict against the base and reported a VACUOUS "0 deviations" — an unverified pass that
reads identically to a real one. This version additionally harvests inline path schemas
and binds them to base schema names by the Beckn property-name convention
(order->Order, items->Item, fulfillments->Fulfillment, ...). Books where nothing could
be bound are reported as UNVERIFIABLE rather than conformant. Named-schema comparison
semantics are unchanged.

Output: knowledge/_work/base-conformance.json  ·  exit 0 = conformant, 3 = deviations.
"""
import os, sys, json, yaml, _env

def load(p):
    try: return yaml.safe_load(open(p))
    except Exception: return {}

def schemas_of(spec): return (spec.get("components",{}) or {}).get("schemas",{}) or {}
def props(sc):
    p = {}
    if isinstance(sc, dict):
        p.update(sc.get("properties") or {})
        for a in sc.get("allOf",[]) or []:
            if isinstance(a, dict): p.update(a.get("properties") or {})
    return p
def enum_of(d): return set(map(str, d.get("enum", []))) if isinstance(d, dict) else set()

# ---------------------------------------------------------------- inline harvest
IRREGULAR = {
    "billing": "Billing", "quote": "Quote", "context": "Context", "message": None,
    "categories": "Category", "cancellation_terms": "CancellationTerm",
    "replacement_terms": "ReplacementTerm", "return_terms": "ReturnTerm",
    "xinput": "XInput", "descriptor": "Descriptor", "fulfillment": "Fulfillment",
    "payment": "Payment", "provider": "Provider", "location": "Location",
    "address": "Address", "time": "Time", "error": "Error", "form": "Form",
    "price": "Price", "customer": "Customer", "person": "Person", "contact": "Contact",
    "state": "State", "city": "City", "country": "Country", "order": "Order",
    "catalog": "Catalog", "intent": "Intent", "item": "Item", "tag": "Tag",
    "agent": "Agent", "vehicle": "Vehicle", "stop": "Stop", "authorization": "Authorization",
    "creator": "Creator", "schedule": "Schedule", "circle": "Circle", "gps": None,
}

def to_schema_name(key):
    """Beckn convention: a property key names the schema of its value.
    items -> Item, fulfillments -> Fulfillment, cancellation_terms -> CancellationTerm."""
    k = key.strip()
    if k in IRREGULAR: return IRREGULAR[k]
    s = k
    if s.endswith("ies") and len(s) > 4: s = s[:-3] + "y"
    elif s.endswith("ss"): pass
    elif s.endswith("s") and len(s) > 3: s = s[:-1]
    return "".join(w[:1].upper() + w[1:] for w in s.split("_") if w)

def unwrap(node):
    """descend through array wrappers to the object node that carries properties."""
    seen = 0
    while isinstance(node, dict) and node.get("type") == "array" and "items" in node and seen < 8:
        node = node["items"]; seen += 1
    return node if isinstance(node, dict) else None

def harvest_inline(spec, base, out, depth=0, _guard=None):
    """walk paths.* inline schemas; bind object nodes to base schema names by key.
    out: {schema_name: merged_schema_node}. Merges across paths so a schema seen in
    several endpoints is compared once against the union of what the book declares."""
    if _guard is None: _guard = set()
    def walk(node, key=None):
        node = unwrap(node)
        if not isinstance(node, dict): return
        nid = id(node)
        if nid in _guard: return
        _guard.add(nid)
        if key is not None:
            name = to_schema_name(key)
            if name and name in base and (node.get("properties") or node.get("enum")):
                tgt = out.setdefault(name, {"properties": {}, "_enums": {}})
                for pk, pv in (node.get("properties") or {}).items():
                    prev = tgt["properties"].get(pk)
                    if prev is None:
                        tgt["properties"][pk] = pv
                    elif isinstance(pv, dict) and isinstance(prev, dict):
                        merged = dict(prev)
                        e = sorted(set(map(str, prev.get("enum", []))) | set(map(str, pv.get("enum", []))))
                        if e: merged["enum"] = e
                        tgt["properties"][pk] = merged
        for pk, pv in (node.get("properties") or {}).items():
            walk(pv, pk)
        for comb in ("allOf", "anyOf", "oneOf"):
            for sub in node.get(comb, []) or []:
                walk(sub, key)
    for _path, ops in (spec.get("paths") or {}).items():
        if not isinstance(ops, dict): continue
        for _m, op in ops.items():
            if not isinstance(op, dict): continue
            bodies = []
            rb = (op.get("requestBody") or {}).get("content") or {}
            for ct in rb.values():
                if isinstance(ct, dict) and ct.get("schema"): bodies.append(ct["schema"])
            for _code, resp in (op.get("responses") or {}).items():
                for ct in ((resp or {}).get("content") or {}).values():
                    if isinstance(ct, dict) and ct.get("schema"): bodies.append(ct["schema"])
            for b in bodies:
                b = unwrap(b)
                if not isinstance(b, dict): continue
                for pk, pv in (b.get("properties") or {}).items():
                    walk(pv, pk)
    return out

def compare(cfg_schemas, base):
    """unchanged comparison semantics: new-schema / new-field / new-enum-value."""
    devs = []
    for name, sc in cfg_schemas.items():
        if name not in base:
            devs.append({"type": "new-schema", "at": name}); continue
        bprops = props(base[name])
        for field, fdef in props(sc).items():
            if field not in bprops:
                devs.append({"type": "new-field", "at": f"{name}.{field}"})
            else:
                norm = lambda s: {v.upper().replace("_", "-") for v in s}
                extra = norm(enum_of(fdef)) - norm(enum_of(bprops[field]))
                if extra:
                    devs.append({"type": "new-enum-value", "at": f"{name}.{field}",
                                 "values": sorted(extra)[:6]})
    return devs

def run():
    if not os.path.exists(_env.BECKN_BASE):
        print("STOP: beckn-base.yaml (human-owned authority) is missing — cannot check conformance."); sys.exit(2)
    base = schemas_of(load(_env.BECKN_BASE))
    report, total, unverifiable = {}, 0, []
    for book in _env.discover_books():
        bid = _env.book_id(book)
        spec = load(os.path.join(book, "config", "specs", "openapi.yaml"))
        named = schemas_of(spec)
        source, cfg = "components.schemas", dict(named)
        if not named:
            cfg = harvest_inline(spec, base, {})
            source = "inline:paths"
        devs = compare(cfg, base)
        unver = (len(cfg) == 0)
        if unver: unverifiable.append(bid)
        report[bid] = {"schema_source": source, "schemas_checked": len(cfg),
                       "unverifiable": unver,
                       "deviation_count": len(devs), "deviations": devs[:40]}
        total += len(devs)
    verdict = "UNVERIFIABLE" if unverifiable and total == 0 else ("CONFORMANT" if total == 0 else "DEVIATIONS")
    report["_verdict"] = verdict; report["_total"] = total
    report["_unverifiable_books"] = unverifiable
    os.makedirs(_env.WORK, exist_ok=True)
    json.dump(report, open(_env.w("base-conformance.json"), "w"), indent=2)

    print(f"BASE CONFORMANCE — {verdict} ({total} deviation(s))\n")
    print(f"  {'book':34} {'source':16} {'checked':>7} {'devs':>5}")
    print("  " + "-" * 68)
    for bid, r in report.items():
        if bid.startswith("_"): continue
        mark = "  UNVERIFIABLE" if r["unverifiable"] else ""
        print(f"  {bid:34} {r['schema_source']:16} {r['schemas_checked']:>7} {r['deviation_count']:>5}{mark}")
    print()
    for bid, r in report.items():
        if bid.startswith("_") or not r["deviations"]: continue
        print(f"  {bid}:")
        for d in r["deviations"][:8]:
            print(f"      {d['type']:15} {d['at']}" + (f"  {d.get('values')}" if d.get("values") else ""))
    if unverifiable:
        print(f"\n⚠ UNVERIFIABLE ({len(unverifiable)}): no schema could be bound to the base — "
              f"'0 deviations' here means NOT CHECKED, not clean.")
        for b in unverifiable: print(f"      {b}")
    if total:
        print("\n⚠ RAISED: configs deviate from the human-owned beckn-base.")
        print("  → Update common-config/beckn-base.yaml MANUALLY to cover these, then re-run.")
        print("  → The skill will NOT modify the base; deviating elements are held out of seeding until reconciled.")
    elif not unverifiable:
        print("\n✓ All configs conform to the base — safe to ground against it.")
    sys.exit(3 if total else 0)

if __name__ == "__main__":
    run()

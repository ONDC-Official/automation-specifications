#!/usr/bin/env python3
"""
Cross-release signature comparator.
Separates SEMANTIC INVARIANT from manual FORMAT/MANAGEMENT variance across
FIS12 (credit), FIS13 (insurance), FIS14 (mutual funds), TRV14 (travel).
Extracts a comparable 'signature' per dimension; classification is done in synthesis.
"""
import os, re, json, glob, yaml, _env, _yaml
from collections import Counter

# generic book discovery (no hardcoded set)
REL = {_env.book_id(b): b for b in _env.discover_books()}     # {id: book_dir}
def cfg(r, rel): return os.path.join(REL[r], "config", rel)
def yload(p):
    doc, err = _yaml.load_file(p)
    return None if err else doc
def read(p):
    try:
        with open(p) as f: return f.read()
    except Exception: return ""

def sig_actions(r):
    doc = yload(cfg(r,"actions/index.yaml")) or {}
    sup = doc.get("supportedActions", {})
    entry = sup.get("null") or sup.get(None) or []
    acts = sorted(sup.keys()) if isinstance(sup, dict) else []
    edges = sum(len(v) for v in sup.values() if isinstance(v, list)) if isinstance(sup, dict) else 0
    return {"schema_keys":sorted(doc.keys()),"entry_actions":entry,
            "action_count":len(acts),"edge_count":edges,"actions":acts}

def sig_errors(r):
    doc = yload(cfg(r,"errors/index.yaml")) or {}
    rows = doc.get("code") if isinstance(doc, dict) else doc
    rows = rows if isinstance(rows, list) else []
    first = rows[0] if rows and isinstance(rows[0], dict) else {}
    return {"container":"code:list" if isinstance(doc,dict) and "code" in doc else type(doc).__name__,
            "field_order":list(first.keys()),"field_set":sorted(first.keys()),"count":len(rows)}

def sig_validations(r):
    p = cfg(r,"validations/index.yaml"); raw = read(p)
    dc, _uc = _yaml.anchors(raw, is_text=True)
    defs = set(dc)
    # strict = also parses under PyYAML's stricter-than-spec composer; the doc itself is
    # read with runtime (js-yaml) semantics either way, so a False here is a report, not a loss.
    strict = True
    try: yaml.safe_load(raw) if raw.strip() else {}
    except Exception: strict = False
    try: doc = _yaml.loads(raw) if raw.strip() else {}
    except Exception: doc = None
    if doc is not None and isinstance(doc, dict): root = sorted(doc.keys())
    else: root = sorted(set(re.findall(r"^([A-Za-z_][A-Za-z0-9_]*):", raw, re.M)))
    ops = sorted(set(re.findall(r"_RETURN_:\s*([^\n]+)", raw)))[:0]  # placeholder
    # sample operator vocabulary from _RETURN_ lines
    rets = re.findall(r"_RETURN_:\s*(.+)", raw)
    vocab = Counter()
    for x in rets:
        for tok in ("are present","all in","any in","none in","follow regex","are unique"):
            if tok in x: vocab[tok]+=1
    return {"root_keys":root,"strict_yaml_ok":strict,"anchor_defs":len(defs),
            "return_ops":dict(vocab),"lines":raw.count("\n")+1}

def sig_flow(r):
    flows = glob.glob(cfg(r,"flows/**/*.yaml"), recursive=True)
    flows = [f for f in flows if "index" not in os.path.basename(f).lower()]
    if not flows: return {"note":"no flow"}
    # pick the largest flow as representative
    f = max(flows, key=lambda p: os.path.getsize(p))
    doc = yload(f) or {}
    steps = doc.get("steps", []) if isinstance(doc, dict) else []
    step_keys = sorted({k for s in steps if isinstance(s,dict) for k in s.keys()})
    apis = [s.get("api") for s in steps if isinstance(s,dict)]
    mock_keys = sorted({k for s in steps if isinstance(s,dict) for k in (s.get("mock") or {}).keys()})
    dp = next((s.get("mock",{}).get("defaultPayload",{}) for s in steps
               if isinstance(s,dict) and (s.get("mock") or {}).get("defaultPayload")), {})
    ctx_keys = sorted((dp.get("context") or {}).keys()) if isinstance(dp,dict) else []
    return {"rep_flow":os.path.basename(f),"n_steps":len(steps),"step_keys":step_keys,
            "mock_keys":mock_keys,"api_spine":apis[:8],"has_html_form":"html_form" in apis,
            "has_dynamic_form":"dynamic_form" in apis,"context_keys":ctx_keys}

def sig_attributes(r):
    files = [x for x in glob.glob(cfg(r,"attributes/*.yaml")) if "index" not in os.path.basename(x)]
    if not files: return {"note":"none"}
    doc = yload(max(files, key=os.path.getsize)) or {}
    desc_keys = Counter()
    def walk(n):
        if isinstance(n, dict):
            if "_description" in n and isinstance(n["_description"], dict):
                for k in n["_description"].keys(): desc_keys[k]+=1
            for v in n.values(): walk(v)
        elif isinstance(n, list):
            for v in n: walk(v)
    walk(doc)
    return {"sample_file":os.path.basename(max(files,key=os.path.getsize)),
            "descriptor_keys":sorted(desc_keys.keys()),"leaf_count":sum(1 for _ in [0] )+max(desc_keys.values() or [0])}

def sig_specs(r):
    doc = yload(cfg(r,"specs/openapi.yaml")) or {}
    info = doc.get("info",{}) if isinstance(doc,dict) else {}
    paths = doc.get("paths",{}) if isinstance(doc,dict) else {}
    return {"openapi_version":info.get("version"),"n_paths":len(paths)}

out = {}
for r in REL:
    out[r] = {"actions":sig_actions(r),"errors":sig_errors(r),
              "validations":sig_validations(r),"flow":sig_flow(r),
              "attributes":sig_attributes(r),"specs":sig_specs(r)}
with open(_env.w("signatures.json"),"w") as f:
    json.dump(out, f, indent=2)

# quick console diff
def line(label, fn):
    print(f"\n== {label} ==")
    for r in REL: print(f"  {r:14} {fn(out[r])}")
line("errors field_order", lambda s: s["errors"]["field_order"])
line("errors field_set",   lambda s: s["errors"]["field_set"])
line("actions entry",      lambda s: s["actions"]["entry_actions"])
line("actions count/edges",lambda s: f"{s['actions']['action_count']} actions / {s['actions']['edge_count']} edges")
line("validations root",   lambda s: s["validations"]["root_keys"])
line("validations strict", lambda s: f"strict={s['validations']['strict_yaml_ok']} anchors={s['validations']['anchor_defs']}")
line("flow step_keys",     lambda s: s["flow"].get("step_keys"))
line("flow mock_keys",     lambda s: s["flow"].get("mock_keys"))
line("flow context_keys",  lambda s: s["flow"].get("context_keys"))
line("flow forms",         lambda s: f"html_form={s['flow'].get('has_html_form')} dynamic_form={s['flow'].get('has_dynamic_form')}")
line("attr descriptor_keys",lambda s: s["attributes"].get("descriptor_keys"))
print("\nsignatures.json written.")

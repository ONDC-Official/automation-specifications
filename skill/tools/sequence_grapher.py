#!/usr/bin/env python3
"""
Tool C.sequence — Call-Sequence Grapher (KEP deterministic spine, B1).
Builds, per book: (1) the action state machine from actions/index.yaml
(entry actions + adjacency), and (2) per-flow ordered api spine with responseFor
links from the in-scope flows. Validates: every step api is a known protocol
action or a recognised UI step; responseFor points at an earlier step; entry
actions non-empty. Input: scope-graphs.json. Output: sequence-graph.json.
"""
import os, json, yaml
import _env

HERE = os.path.dirname(__file__)
REF = _env.CONFIGS
SCOPE = _env.w("scope-graphs.json")
UI_STEPS = {"html_form", "dynamic_form", "form"}   # non-protocol interactive steps

def load(p):
    try:
        with open(p) as f: return yaml.safe_load(f)
    except Exception: return None

def state_machine(cfg):
    doc = load(os.path.join(cfg, "actions", "index.yaml")) or {}
    sup = doc.get("supportedActions", {}) or {}
    entry = sup.get("null") or sup.get(None) or []
    nodes, edges = set(), 0
    for a, nxts in sup.items():
        if a not in (None, "null"): nodes.add(a)
        for n in (nxts or []):
            nodes.add(n); edges += 1
    return {"entry_actions": entry, "action_nodes": sorted(nodes), "edges": edges,
            "vocab": nodes | set(entry)}

def run():
    scope = json.load(open(SCOPE))
    results = {}
    for book_dir, sg in scope.items():
        book = book_dir.split("eks-")[1]
        cfg = os.path.join(REF, book_dir, "config")
        sm = state_machine(cfg)
        vocab = sm["vocab"]
        flows, flags, total_steps, protocol_steps, ui_steps = [], [], 0, 0, 0
        for rel in sg.get("in_scope_files", []):
            if "flows/" not in rel or os.path.basename(rel) == "index.yaml": continue
            doc = load(os.path.join(cfg, rel))
            if not isinstance(doc, dict): continue
            steps = doc.get("steps", []) or []
            seen, spine = set(), []   # seen = earlier apis AND action_ids
            for s in steps:
                if not isinstance(s, dict): continue
                api = s.get("api"); aid = s.get("action_id"); total_steps += 1; spine.append(api)
                if api in UI_STEPS: ui_steps += 1
                elif api in vocab: protocol_steps += 1
                else: flags.append({"type": "unknown-api", "flow": rel, "api": api})
                rf = s.get("responseFor")
                # responseFor references the REQUEST step's action_id (or api); must appear earlier
                if rf and rf not in seen and rf not in UI_STEPS:
                    flags.append({"type": "dangling-responseFor", "flow": rel, "responseFor": rf})
                seen.add(api);
                if aid: seen.add(aid)
            flows.append({"flow": os.path.basename(rel).replace(".yaml",""),
                          "n_steps": len(steps), "spine": spine[:10]})
        if not sm["entry_actions"]:
            flags.append({"type": "no-entry-actions"})
        results[book] = {
            "entry_actions": sm["entry_actions"],
            "action_nodes": len(sm["action_nodes"]),
            "edges": sm["edges"],
            "flows": len(flows),
            "total_steps": total_steps,
            "protocol_steps": protocol_steps,
            "ui_steps": ui_steps,
            "flag_count": len(flags),
            "flags_sample": flags[:5],
            "flow_spines": flows,
        }
    out = _env.w("sequence-graph.json")
    json.dump(results, open(out, "w"), indent=2)
    for b, r in results.items():
        print(f"{b}: entry={r['entry_actions']} actions={r['action_nodes']} edges={r['edges']} "
              f"flows={r['flows']} steps={r['total_steps']} (protocol={r['protocol_steps']} ui={r['ui_steps']}) "
              f"flags={r['flag_count']}")
        if r["flags_sample"]: print("   flags:", r["flags_sample"])

if __name__ == "__main__":
    run()

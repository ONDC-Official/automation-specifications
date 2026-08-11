#!/usr/bin/env python3
"""
Tool D — Runtime Enricher (KEP, B3).
For each grounded node KIND, assign its runtime ROLE and attach the established
config->runtime semantics (from the workbench KB). Roles:
  runtime-behavioral  — the workbench executes it (validations, flow steps, actions, schema, errors, paths)
  observed-example    — concrete observed runtime data (defaultPayload)
  documentation-only  — specification with no runtime execution (attribute info/usage prose)
  unknown             — mapping not established -> FLAG, never guess
Facts are grounded to the workbench KB. Input: ground-map.json + sequence-graph.json.
Output: runtime-annotation.json.
"""
import os, json
import _env
HERE = os.path.dirname(__file__)
CMP = _env.WORK
WBK = "references/automation-framework/knowledge/protocol-workbench"

# KIND -> (role, basis_hint, [facts], workbench-KB grounding)
KIND_MAP = {
 "action":     ("runtime-behavioral", "authority",
                ["state-machine gating; supportedActions[null] = valid transaction ENTRY point",
                 "async_predecessor enforces ordering via resolver chain"],
                f"{WBK}/frames/flow-state-machine.md"),
 "validation": ("runtime-behavioral", "sandbox-tested",
                ["compiled JVAL->Go (ondc-code-generator); executed as L1 on /seller,/buyer paths",
                 "failure -> ACK:NACK + error code (HTTP 200); gated by protocol_validation header",
                 "_CONTINUE_ = runtime skip guard"],
                f"{WBK}/frames/validation-layers.md"),
 "flow-step":  ("runtime-behavioral", "observed-live",
                ["executed by mock-runner-lib; JS timeouts generate 45s / validate 5s / requirements 3s",
                 "saveData (JSONPath) accumulates into session MOCK_DATA; responseFor pairs callback->request",
                 "phase statuses: RESPONDING / INPUT-REQUIRED / WAITING-SUBMISSION drive sequencing"],
                f"{WBK}/frames/mock-runner-lib.md"),
 "error":      ("runtime-behavioral", "observed-live",
                ["emitted on NACK with this code + From(BAP/BPP)"],
                f"{WBK}/scripts/onix-request-lifecycle.md"),
 "schema":     ("runtime-behavioral", "declared",
                ["L0 JSON-schema validation at runtime (schemavalidator plugin)"],
                f"{WBK}/frames/validation-layers.md"),
 "path":       ("runtime-behavioral", "declared",
                ["API endpoint served by ONIX api-service (nginx :3032 -> :7039)"],
                f"{WBK}/scripts/onix-request-lifecycle.md"),
 "attribute":  ("documentation-only", "declared",
                ["field dictionary: info/usage = documentation (no runtime execution)",
                 "type/required/enums are structural inputs consumed by validation/generation, not executed here"],
                None),
 # defaultPayload examples live INSIDE flow steps; tagged observed-example when lifted
 "example":    ("observed-example", "observed-live",
                ["concrete protocol message actually sent at runtime"],
                f"{WBK}/references/runtime-verification-2026-06-28.md"),
}

def run():
    gm = json.load(open(os.path.join(CMP, "ground-map.json")))
    seq = json.load(open(os.path.join(CMP, "sequence-graph.json")))
    entries = {b.split('-')[0]: r["entry_actions"] for b, r in seq.items()}
    results = {}
    for book, g in gm.items():
        bk = book.split('-')[0]
        by_kind = g.get("by_kind", {})
        roles = {}; unknown = []
        for kind, count in by_kind.items():
            m = KIND_MAP.get(kind)
            if not m:
                unknown.append(kind); continue
            role = m[0]
            roles.setdefault(role, {"count":0, "kinds":[]})
            roles[role]["count"] += count
            roles[role]["kinds"].append(f"{kind} ({count})")
        results[bk] = {
            "total_nodes": g.get("nodes_grounded", 0),
            "roles": {r: v["count"] for r, v in roles.items()},
            "role_kinds": {r: v["kinds"] for r, v in roles.items()},
            "entry_points": entries.get(bk, []),
            "unknown_kinds": unknown,
            "facts": {k: {"role":v[0], "basis":v[1], "facts":v[2], "grounded_in":v[3]}
                      for k, v in KIND_MAP.items() if k in by_kind},
        }
    json.dump(results, open(os.path.join(CMP, "runtime-annotation.json"), "w"), indent=2)
    for bk, r in results.items():
        print(f"{bk}: total={r['total_nodes']}  roles={r['roles']}  entry_points={r['entry_points']}  unknown={r['unknown_kinds']}")

if __name__ == "__main__":
    run()

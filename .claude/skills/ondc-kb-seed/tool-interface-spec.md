# KEP Skill — Tool Interface Spec (A–G)

> Contracts for the seven components before any implementation. Each tool is defined by inputs, outputs, invariants, determinism, and dependencies. Data contracts (§9) are the interfaces passed between tools; the orchestrator (§10) wires them.
> **Date:** 2026-07-19 · Companion to `skill-build-plan.md`. Form (SKILL.md vs codebase) is deferred — these contracts hold either way.

---

## 0. Determinism map (the trust boundary)

| Tool | A | B | C | D | E | F | G |
|---|---|---|---|---|---|---|---|
| Deterministic | ✅ | ✅ | ✅ | ✅* | ❌ (AI) | ✅ (write/validate) | ✅ |

`D` is deterministic *given the workbench runtime KB* — the runtime's use of config is itself deterministic; where the config→runtime mapping is unknown it returns `unknown` + flag, never a guess. `E` is the only inferential stage. Grounding, scope, structure, classification, and regeneration are all deterministic.

---

## A. Scope Resolver `deterministic`
**Purpose:** produce the in-scope, dereferenced config graph for one book, from the `index.yaml` manifest only.
**Inputs:** `book_root` (dir with `config/index.yaml`); `opts{ preserve_anchors=true }`.
**Outputs:** `ScopeGraph` (§9.1).
**Contract / invariants:**
- Scope = only what `index.yaml` dereferences into. Orphan/unreferenced files (`*_old.yaml`, hyphen/underscore duplicates) are **excluded** and listed in `orphans_ignored`.
- Resolve JSON-Pointer `$ref` + expand `$ref` include-lists.
- **Preserve YAML anchors as a symbol table** (`&name`→def, `*name`→sites); never inline.
- **JSONPath selectors** (`$.context…`) are data-plane — captured, never dereferenced.
- Lenient parse (tolerate duplicate anchor names) + a defined anchor-resolution rule; parse issues → `flags`.
**Depends on:** nothing (entry tool).
**Failure modes → flags:** unresolved `$ref`; invalid-YAML; duplicate-anchor.
**Manifest-completeness review — GATE (mandatory):** A emits a review of scope quality (orphan count, partial/commented manifest, parse flags). This **must be surfaced and confirmed by a human before any downstream tool acts** — scope is never assumed correct. Precedent: FIS12-2.3.0 was *eliminated* at this gate (deprecated/partial manifest, 62 orphans). A book that fails the gate is held out, not seeded.

## B. Grounder `deterministic`
**Purpose:** assign every in-scope node a stable positional node-path = its `grounded-in` anchor.
**Inputs:** `ScopeGraph`.
**Outputs:** `GroundMap` (§9.2): `node_id → "<book>:<file>#<node-path>"`, plus reverse index `config-node → [node_id]`.
**Contract / invariants:**
- Node-path is **positional, never a line number**; survives reorder.
- **Round-trip resolvable:** given a `grounded-in`, locate the exact config node (this is the grounding-resolver the KB validator delegates).
- **Invariant G-1:** 100% of node-paths resolve to a real config position (proven on the slice).
**Depends on:** A.

## C. Structure + Classifier `deterministic`
Two operations.

**C.sequence** — call-sequence graph.
**Inputs:** `ScopeGraph` (flows + actions).
**Outputs:** `SequenceGraph` (§9.3): nodes (actions/steps), edges (`next-action`, `responseFor`), `entry_actions`, per-step `{api, owner, responseFor, saveData_keys, has_inputs_schema}`.
**Contract:** edges/entry from `supportedActions` + step order; deterministic.

**C.classify** — 3-tier difference classifier.
**Inputs:** a grounded element + its peers across books + `beckn-base.yaml` + skeleton rules.
**Outputs:** `Classification` (§9.4): `tier ∈ {invariant, authoring-style, semantic}`, plus `canonical_form` (authoring→normalized per skeleton rules) or `scope=<domain>` (semantic), `evidence`, `needs_human?`.
**Contract:**
- **Classify against the BASE (union), not per-release.** The base includes every field + all feature-module (IGM) schemas, so schema-level items are **core** — including domain-only fields (in base, sparsely populated) and IGM (core, activation-tagged). **invariant/core** → in base, map directly; **authoring-style** → normalize (strictness→closed, `$ref`-collapse, enum union/dedupe, casing, nested union — *before* diffing); **semantic** → genuine *behaviour* only (entry actions, search mode), never schema presence. (Reclassified per review 2026-07-19: 78 core / 19 authoring / 2 semantic.)
- **Canonical form from the Beckn base, not majority vote.**
- Ambiguous (noise vs meaning) → consult **D**; still unresolved → `needs_human`.
**Depends on:** A, B, `beckn-base.yaml`, skeleton.

## D. Runtime Enricher `deterministic given workbench KB`
**Purpose:** classify each element's runtime **role** and attach runtime semantics.
**Inputs:** grounded element + kind (`validation|flow-step|action|attribute|error`) + workbench runtime KB.
**Outputs:** `RuntimeAnnotation` (§9.5): `role ∈ {runtime-behavioral, observed-example, documentation-only, unknown}`, `facts[]` (timing/scope/failure/sequencing/entry-point), `basis_hint ∈ {observed-live, authority, declared}`, `runtime_grounding` (workbench-KB refs).
**Contract:**
- Role from the **established config→runtime mapping** (e.g. `supportedActions:null`⇒entry-point; `x-validations`⇒L1-executed; base64 JS⇒runtime-behavioral; `attributes.info`⇒documentation-only; `defaultPayload`⇒observed-example).
- **Unknown mapping → `role=unknown` + flag; never guess.**
- Distinguish **absent-because-minified** (module not activated) from **absent-because-domain** using the module catalog.
- Runtime facts are grounded to the workbench KB (their own `grounded-in`).
**Depends on:** A, B, workbench runtime KB, module catalog.

## E. Interpretation `AI (in-skill reasoning)`
**Purpose:** assign meaning; produce candidate KB units. The only inferential stage.
**Inputs:** grounded element + `RuntimeAnnotation` + `Classification` + `examples(defaultPayload)` + decoded JS + docs/`info` prose + beckn-base object ontology.
**Outputs:** `CandidateUnit[]` (§9.6).
**Contract:**
- Every candidate carries a `grounded-in`.
- `basis` reflects source strength: `declared` (parsed structure) · `sandbox-tested` (compiles/runs) · `observed-live`/`authority` (runtime facts from D) · `inferred` (+`!desired`) for decoded-JS / prose interpretation.
- **No `confidence` field** — strength lives in `basis`.
- Nothing `inferred` is auto-committed (governance gate at F).
**Depends on:** B, C, D.

## F. KB Writer `deterministic write + validate`
**Purpose:** commit candidate units to KB-storage; intern anchors; validate.
**Inputs:** `CandidateUnit[]`, existing KB (anchors/units/INDEX), `asof` (book), `beckn-base` (anchor identities).
**Outputs:** written `KBUnit`s (§9.7), interned anchors, INDEX updates, `validate_kb.py` report.
**Contract / invariants:**
- Emit `subject | relation | object` + `basis` + `asof` + `grounded-in` + PROV-O; relations from the **closed registry**.
- **Shared Beckn objects** (provider/payment/item/fulfillment, from beckn-base) **interned once as anchors**; domain senses attach via `scoped-to`.
- **`asof` isolation** — no cross-version inference.
- **Governance gate:** auto-commit `declared`/`sandbox-tested`/`observed-live`; route `inferred`/`!desired`/ontology-evolution to human review (basis + change-type).
- Must pass **`validate_kb.py`** (triple/vocab/handle-resolution/anchor-not-line-number/cycle).
**Depends on:** E, KB-storage validator, beckn-base.

## G. Views + Selective Regen `deterministic`
**Purpose:** derived views (regenerated at load) + selective regeneration on a config diff.
**Inputs:** committed units + INDEX + reverse index; a `config_diff` (changed node-paths).
**Outputs:** regenerated derived views (never committed); `affected_set` (units/anchors/views to revisit).
**Contract:**
- Derived is **never source of truth**.
- A diff maps changed config node-paths → affected units via INDEX/reverse index → **only those revisit**; unaffected untouched.
- `kb-release` bump per the Q5 axis when the base/skeleton changes.
**Depends on:** B, F.

---

## 9. Shared data contracts (the interfaces)

- **9.1 `ScopeGraph`** `{ book, domain, version, files_in_scope[], config_tree(deref'd), symbol_table[{name,def,sites[]}], jsonpath_selectors[], orphans_ignored[], flags[] }`
- **9.2 `GroundMap`** `{ forward: {node_id: grounded_in}, reverse: {config_node: [node_id]} }` ; `grounded_in = "<book>:<file>#<node-path>"`
- **9.3 `SequenceGraph`** `{ nodes[{action_id,api,owner}], edges[{from,to,rel}], entry_actions[] }`
- **9.4 `Classification`** `{ element_id, tier, canonical_form?, scope?, evidence[], needs_human }`
- **9.5 `RuntimeAnnotation`** `{ element_id, role, facts[{kind,value,grounded_in}], basis_hint, runtime_grounding[] }`
- **9.6 `CandidateUnit`** `{ subject, relation, object, basis, asof, grounded_in, refs[], flags[] }`
- **9.7 `KBUnit`** (committed) = `CandidateUnit` validated + PROV-O links + anchor references; serialized in KB-storage atom grammar.

---

## 10. Orchestration (SKILL flow)

```
A ─▶ B ─▶ ├─ C (sequence + classify) ─┐
          └─ D (runtime enrich) ───────┴─▶ E (interpret) ─▶ F (write+validate) ─▶ G (views/regen)
```
Per book: resolve scope → ground → (classify + runtime-enrich in parallel) → interpret → write+validate → views. Selective regen (G) re-enters at B for a diff.

---

## 11. Open items (not blocking the contracts)
1. **Skill vs Agent (layering — proposed, confirm):** not either/or. **Skill** = the reusable procedure + domain knowledge + A→G orchestration (SKILL.md, instantiates KB-storage `operations/seed`). **Agent (subagent)** = the isolated execution context for heavy runs; **fan out one subagent per book** (books are `asof`-isolated → parallel-safe). **Deterministic tools A–D/F-write/G = CLI scripts** both call. **Governance gate (F) + human review = main thread.** Light maintenance (small-diff regen) runs inline via the skill without a subagent. *Not* a standalone codebase. Mental model: Skill = brain · Agent = body · scripts = hands · main thread = review.
2. **Anchor equivalence in F:** shared-object identity comes from beckn-base (deterministic); cross-domain sense-merging may need light AI — decide at B4.
3. **Module catalog** (for D's minified-vs-domain call) — needs a small catalog of IGM/track/rating schema+path sets (derivable from provenance).
4. **`Order.status` synonyms** — a `needs_human` item feeding C/E.

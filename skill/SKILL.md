---
name: ondc-kb-seed
description: >-
  Seed and maintain a grounded semantic knowledge base (KB-storage format) from ONDC
  automation-specification config releases. Use when asked to "seed the KB", "build KB
  from config", "extract semantic knowledge from automation specs", "turn ONDC config
  into a knowledge base", "regenerate docs/MCP/knowledge from specs", or to add/refresh a
  domain (FIS/TRV/RET/etc.) in the protocol knowledge base. Runs a 7-tool pipeline
  (scope → ground → sequence/classify → runtime-enrich → interpret → write → views) over
  each config book and emits validated KB-storage atoms.
---

# ONDC KB Seed — orchestrator

Turns config (Ground 0) + the derived Beckn base + the workbench runtime KB into a
**grounded, validated semantic KB** (KB-storage atoms), from which every downstream
product is a regenerable view. The seven tools are deterministic scripts; this skill is
the procedure that runs them, holds the **review gates**, and interprets meaning.

**Layering:** Skill = brain · Agent (subagent, one per book) = body · `tools/*.py` = hands · main thread = review.
**Grounding priority:** a domain fact grounds to its own config first; `common-config/beckn-base.yaml` is the shared reference/fallback.

## Canonical layout (provided at execution) — paths centralized in `tools/_env.py`
| Dir | Role |
|---|---|
| `configs/` | **config books** (Ground 0), 1+; scope = whatever each `config/index.yaml` dereferences into |
| `common-config/` | **provided shared grounding** — `beckn-base.yaml` (+provenance). *This is an INPUT, not built by the skill;* `build_beckn_base.py` only bootstraps it when absent. |
| `references/` | additional grounding material (e.g. KB-storage output-format spec); pointed to for grounding if needed |
| `automation-framework/` | workbench runtime **code + knowledge** (`protocol-workbench`) — source of runtime/protocol understanding for Tool D |
| `knowledge/` | **OUTPUT** — KB atoms + anchors per book; `knowledge/_work/` holds regenerable intermediate stage data |
| `skill/` | the skill (`SKILL.md`, `tools/`, bundled `validate_kb.py`) |

## Prerequisites & preflight (PUSH BACK before acting)

Run `tools/preflight.py <root>` **first**. It discovers config books generically (no hardcoded book id) and decides **RUN / DEGRADED / STOP**. The skill must not proceed past a STOP, and must announce every DEGRADED mode.

| Input | Requirement | If missing |
|-------|-------------|-----------|
| **≥1 config book** (`config/index.yaml` + `specs/openapi.yaml` + actions/flows/validations/attributes) | **MANDATORY** | **STOP** — no KB output is possible. |
| **`automation-framework/`** (workbench runtime + `protocol-workbench` knowledge) | **MANDATORY** | **STOP** — runtime/protocol understanding cannot be grounded without it. |
| **`common-config/beckn-base.yaml`** | **MANDATORY — human-owned authority** (skill grounds against it, never rewrites it) | **STOP** — bootstrap ONCE with `build_beckn_base.py`, then it is user-owned. |
| **≥2 books** | for cross-book classify (C.cls) | **DEGRADED** — C.cls runs single-book (no cross-book diff). |
| **KB validator** | for F | **bundled** in `tools/validate_kb.py` — no external dependency. |

Books are handled **generically**: `kb_writer.py [book_dir]` and `tool_g.py [book]` operate on any book (default: the first discovered); nothing is pinned to a specific release.

## Base authority & grounding evolution (how new/changed grounding is handled)

**The base is human-owned; the skill relies on it and never rewrites it.**
- **`tools/base_conformance.py` (gate, before seeding):** checks every config book against `common-config/beckn-base.yaml`. A schema/field/enum a config uses that the base does not cover is a **deviation** → the skill **RAISES it and asks the user to update `beckn-base.yaml` manually**; deviating elements are **held out of seeding** until reconciled. The skill does **not** extend the base itself. (`build_beckn_base.py` is a one-time bootstrap only.)
- **`tools/source_state.py` (incremental):** snapshots the content of every in-scope source file (config/references) into `knowledge/_state/` and diffs against the last run → **added / modified / removed** grounding. **MODIFIED/REMOVED** → Tool G re-seeds only the affected units (reverse index + PROV-O hop); **ADDED** → new units seeded. First run = all-new. This is how new additions and modifications of existing grounding facts are detected and propagated selectively (no full re-seed).
- **Grounding priority holds:** a domain fact grounds to its own config first; the base is the shared reference. A config that *conflicts* with the base is surfaced, never silently overridden.

## Pipeline (per book)

| Stage | Tool | Kind | Output |
|-------|------|------|--------|
| A | `tools/scope_resolver.py` | deterministic | in-scope files (index.yaml traversal), orphans, symbols, flags |
| B | `tools/grounder.py` | deterministic | positional node-paths (`<book>:<file>#<node>`), 100% round-trip |
| C.seq | `tools/sequence_grapher.py` | deterministic | action state machine + per-flow api spine |
| C.cls | `tools/classifier.py` | deterministic | core / authoring / semantic (base = union) |
| D | `tools/runtime_enricher.py` | deterministic* | runtime role + facts (grounded to workbench KB) |
| E | *AI (this skill)* | inference | CandidateUnits (`subj\|rel\|obj` + `basis` + `grounded-in`) |
| F | `tools/kb_writer.py` | deterministic | KB-storage atoms + anchors; validated by `validate_kb.py` |
| G | `tools/tool_g.py` | deterministic | reverse index, derived views, selective regen |

`*` D is deterministic given the workbench KB; unknown mappings → `unknown` + flag (never guessed).

## Orchestration

0. **Preflight (mandatory).** Run `tools/preflight.py`; **STOP** if a mandatory input is missing (config book · automation-framework · beckn-base), announce any DEGRADED mode.
0b. **Base-conformance gate.** Run `tools/base_conformance.py`; if configs deviate from the human-owned base, **RAISE and ask the user to update `beckn-base.yaml` manually** — hold deviating elements until reconciled.
0c. **Source-change scan.** Run `tools/source_state.py` to compute added/modified/removed grounding; seed new + re-seed only affected (skip unchanged).
1. **Fan out one subagent per book** (books are `asof`-isolated → parallel-safe). Each subagent runs A→G for its book and returns a summary + a review queue. The main thread merges results.
2. **Per book, in order:** A → B → (C.seq ∥ C.cls ∥ D) → E → F → G.
3. **Interpretation (E)** is the only AI step: read each grounded + classified + runtime-enriched node (config + runtime facts + examples/defaultPayload + decoded step JS + attribute prose) and emit CandidateUnits with `basis` reflecting source strength (`declared`/`sandbox-tested`/`observed-live`/`authority`/`derived`/`inferred`). **Write per the embedded format contract — `kb-format/atom.grammar.md` + `kb-format/vocabularies.md`** (closed relation/basis vocab, `grounded-in`, anchors); never emit a `confidence` field; nothing `inferred` is asserted.

## Output format — EMBEDDED (self-contained)
The KB-storage format ships **with the skill**, so no external `KB-storage` repo is a runtime dependency:
- `kb-format/` — the contract E and F write to: `atom.grammar.md`, `vocabularies.md`, `unit.md`, `anchor.md`, `invariants.md`.
- `tools/validate_kb.py` — the bundled reference validator (F gate).
`references/KB-storage` (if present) is fuller design documentation only, not required to run.

## Review gates (confirm with a human before acting)

1. **Manifest-completeness (after A)** — surface orphans / partial or deprecated manifest; a book that fails is **held out**, not seeded. (Precedent: FIS12-2.3.0 excluded.)
2. **Classifier `needs_human` (after C.cls)** — ambiguous invariant-vs-semantic items.
3. **Governance (at F)** — auto-commit `declared`/`sandbox-tested`/`observed-live`; route `inferred`/`!desired`/ontology-evolution to human review.

Each gate is delivered as an interactive review (see `review-harness*.html`); proceed only on approval.

## Invariants (enforced)
- Scope = `index.yaml` traversal only; orphans ignored.
- Grounding is positional & id-based, never a line number; 100% round-trip.
- Classify against the **base (union)**: schema fields + IGM = core; only *behaviour* (entry actions, search mode) is semantic.
- Atoms pass `references/KB-storage/structure/validators/validate_kb.py` (closed relation/basis vocab, `inferred ⇔ no grounded-in`, isa-DAG).
- Selective regen: a config change revisits only units grounded at the changed node + one PROV-O hop.
- Evolution via the **KB-release axis** (Q5): protocol change ⇒ KB-release; KB maturation may bump KB-release without a protocol change.

## Run
`tools/run_pipeline.py <references_dir>` chains A→G and reports each stage's artifact + the gate summary. In production each book runs in its own subagent.

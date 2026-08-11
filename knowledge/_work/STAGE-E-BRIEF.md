# Stage E — Interpretation brief (ONDC KB seed)

You are the **AI interpretation step (Stage E)** for exactly ONE config book. Stages A–D
(deterministic) already ran; F/G (deterministic) run after you. Your only job is to read the
grounded, classified, runtime-enriched material for your book and emit **CandidateUnits**.

## Paths
- Root: `/home/claude/kbroot`
- Your book config: `/home/claude/kbroot/configs/release-eks-<BOOK_DIR>/config/`
- Format contract (READ FIRST, all of it):
  `/home/claude/kbroot/skill/kb-format/atom.grammar.md`
  `/home/claude/kbroot/skill/kb-format/vocabularies.md`
  `/home/claude/kbroot/skill/kb-format/unit.md`
  `/home/claude/kbroot/skill/kb-format/anchor.md`
  `/home/claude/kbroot/skill/kb-format/invariants.md`
- Stage A–D outputs (your book's entries only):
  `/home/claude/kbroot/knowledge/_work/scope-graphs.json`     (in-scope files — SCOPE AUTHORITY)
  `/home/claude/kbroot/knowledge/_work/sequence-graph.json`   (action state machine + flow spines)
  `/home/claude/kbroot/knowledge/_work/classification.json`   (core / authoring / semantic)
  `/home/claude/kbroot/knowledge/_work/runtime-annotation.json` (runtime role + facts)
  `/home/claude/kbroot/knowledge/_work/base-conformance.json` (HELD-OUT elements — see below)
- Workbench runtime knowledge (what a position *means* at runtime):
  `/home/claude/kbroot/automation-framework/knowledge/protocol-workbench/`
- Structural atoms already written for you (do NOT duplicate these):
  `/home/claude/kbroot/knowledge/<book-id>/atoms.md`

## Output — write exactly one file
`/home/claude/kbroot/knowledge/<book-id>/candidate-units.md`

One unit per line, pipe-delimited, in the atom grammar:

```
<subject> | <relation> | <object> | basis:<b> | asof:<book-id> [| grounded-in:<book-id>:<file>#<node-path>] [| !<flag>]
```

Field order is FIXED: `basis`, `asof`, `grounded-in`, then flags. No header lines other than a
single `# <book-id> candidate units (Stage E)` first line. No prose, no bullets, no commentary.

## Hard rules (the validator and the skill invariants enforce these)
1. **Never emit a `confidence` field.** It does not exist in this grammar.
2. **`basis:inferred` ⇔ NO `grounded-in`** (both directions). Nothing `inferred` is asserted as fact.
3. **Relations are a closed registry** — only those in `vocabularies.md`. Any may take `not-`.
   Never invent a free-text verb.
4. **`basis` is a closed vocabulary**: `declared` · `sandbox-tested` · `observed-live` ·
   `authority` · `ecosystem` · `derived` · `inferred`. Pick the one that honestly reflects source
   strength. Config/spec declares it → `declared` (this is the bulk). Regulation/principle →
   `authority`. Built from other KB facts → `derived`. Model-guessed → `inferred` (and then no
   grounding, and it is never asserted).
5. **`grounded-in` is a POSITIONAL node-path**, `<book-id>:<file>#<node-path>` — e.g.
   `fis12-2.3.0:flows/LAMF/master_search.yaml#steps[search_1].inputs.jsonSchema.properties.pan`.
   **NEVER a line number.** The path must actually exist in the config — verify before emitting.
6. **untethered-must-be-tagged**: no `grounded-in` and `basis ∉ {inferred, ecosystem}` ⇒ must carry
   `!untethered`. Silent dangling is invalid.
7. **Interning invariant**: a meaning grounded at a config `&anchor`, or recurring in ≥2 positions,
   is referenced as an `anchor.<kebab>` handle — never restated inline. Confine a position-specific
   meaning with `scoped-to` rather than cloning the anchor.
8. **Scope = `index.yaml` traversal only.** Use only files listed in `in_scope_files` for your book
   in `scope-graphs.json`. Orphans are out of scope — ignore them entirely.
9. **`asof:` is your book-id** (e.g. `trv11-2.1.0`) — no `release-eks-` prefix.
10. **isa must stay a DAG** — no cycles.
11. Do not restate an atom already present in `atoms.md`.

## HELD-OUT elements (base-conformance gate)
`beckn-base.yaml` is the human-owned authority and has NOT yet been updated to cover the
deviations your book declares. Look up your book in `base-conformance.json`. For every element
listed there, you **must not** emit a `basis:declared` unit asserting it as conformant protocol.
If the element matters to your book's meaning, emit it with `!untethered` so it is parked
explicitly and visible for reconciliation, or omit it. Never silently assert a held-out element.

## What to interpret (the actual work)
Read each in-scope node and say what it *means*, not what it looks like:
- **actions/index.yaml** — the action set and `supportedActions.null` (transaction entry).
  Entry actions are *behaviour* → semantic, per the classifier.
- **flows/** — each step's `api`, `action_id`, `responseFor`, and any decoded step JS. Order
  relations (`precedes`), causal relations (`causes`), and preconditions (`requires`). One flow is
  a journey; name what the journey accomplishes.
- **attributes/*.yaml** — attribute prose, `owner`, `required`, `usage`, `enums`, `tags`. This is
  the richest semantic material. `owner` tells you `sent-by`. `required` gives `requires`.
- **validations/index.yaml** — YAML `&anchors` are interned meanings by construction. Each anchor
  is an `anchor.<kebab>` handle; its uses are `scoped-to` the positions that use it.
- **specs/openapi.yaml** — schema shape. Structural `isa`/`has-slot`.
- **errors/index.yaml** — error codes and what `causes` them.
- **docs/*.md** — the human rationale. Often the only source for `authority` basis (a rule that
  exists because a regulator or a design principle demands it). Use it to explain *why*.
- **runtime-annotation.json** — `runtime-behavioral` vs `documentation-only`. A documentation-only
  node must not be asserted as runtime behaviour.

Prefer fewer, correct, well-grounded units over many weak ones. **Closed-world: absence means
not-known.** Leave a relation out rather than force a weak one. Explicit negatives (`not-`) are
valid facts and are welcome where the config genuinely establishes them.

Aim for depth proportional to the book: interpret every flow, every attribute file, and every
validation anchor. A few hundred well-grounded units is a good outcome for a rich book; do not
pad.

## Return value
Your final message is consumed programmatically. Return ONLY a compact JSON object:
`{"book":"<book-id>","units":<int>,"by_basis":{...},"anchors_interned":<int>,"held_out_respected":<int>,"notes":"<=200 chars"}`

# Unit — the triple that matures into an atom

The unit is the only committed unit of fact-truth; every other layer derives from it. A unit is a
**triple** that **matures in place**: it starts as a bare `subject | relation | object` and accretes a
few optional fields as it earns them. A fully matured, grounded triple is an **atom**. Every atom is a
triple; not every triple is an atom.

## Line grammar

```text
<subject> | <relation> | <object>                                        # mandatory head
<subject> | <relation> | <object> | basis:<b> | asof:<v> [| grounded-in:<anchor>] [| !<flag> …]   # mature
```

Pipe-delimited, one fact per line, stored in `atoms.md` (or sharded `atoms/*.md`). Field order is fixed
for greppability: `basis`, `asof`, `grounded-in`, then any `!flags`.

| field | domain | required | notes |
|---|---|---|---|
| subject | id-handle \| literal | **yes** | resolves to a node or a literal |
| relation | registry ([vocabularies](vocabularies.md)) | **yes** | no free-text verbs; may take `not-` |
| object | id-handle \| literal | **yes** | |
| basis | `declared` \| `sandbox-tested` \| `observed-live` \| `authority` \| `ecosystem` \| `derived` \| `inferred` | optional | what backs the fact + how strongly |
| asof | version-baseline id | optional | e.g. `dom-a1-1.0.0`; carries the book axis; no cross-version inference |
| grounded-in | `<book>:<file>#<node-path>` \| `<obs-ref>` \| `<ref>` \| `<unit/anchor-handle>` | optional | the **pointer only** — no kind prefix; a config anchor is a **positional node-path**, **never a line number** |
| ref-subject / ref-object | `node:<id>` \| `config:<ref>#<node>` \| `external:<uri>` | optional | endpoint pointer; may be unresolved-but-tagged |
| `!flags` | `!untethered` \| `!deprecated` \| `!desired` \| `!plane=<p>` | optional | the only status written by hand |

**Only the triple is mandatory.** `basis`/`asof`/`grounded-in` are accreted with maturity.

## Derived — never written, computed at load

| axis | rule |
|---|---|
| maturity | triple-only → `bare`; some fields → `partially-grounded`; `basis`+`asof`+ground → `mature` |
| plane | `precedes`/`wasInformedBy` → `session-logic`; `basis ∈ {authority, ecosystem}` → `cross`; `basis ∈ {sandbox-tested, observed-live}` → `runtime-state`; else `spec` (override: `!plane=<p>`) |
| scope | `live` unless `!desired` |
| grounding-status | `grounded` when `grounded-in` resolves; else the unit must carry `!untethered`/`!deprecated` |

## Grounding — position is the anchor

Config meaning is **position-dependent**: the same key means different things by path (`descriptor.code`
under `xinput.head` ≠ under `payment.tags[].list[]`). So a config `grounded-in` is a **positional
node-path** — `<book>:<file>#<node-path>`, e.g.
`fis12-2.3.0:flows/LAMF/lamf_credit_line_with_mfc#steps[search_1].inputs.jsonSchema.properties.pan` — and
**never** a line number (paths survive reorganization; line numbers don't). What a position *means* is
interpreted by consulting the workbench knowledge (a **reference**), never copied into the unit. When the
same meaning recurs across positions, intern it as an [anchor](anchor.md) and confine positions with
`scoped-to`.

## Rules (per-unit validity)

- **`basis:inferred` ⇔ no `grounded-in`** (both directions). An inferred fact has no anchor and is never
  asserted.
- A **config anchor** (`grounded-in` with `#`, under `basis:declared`) is a positional node-path, never a
  line number.
- subject/object handles resolve to a known node (frame, **anchor**, reference, relation, slot-filler) or
  a literal.
- relation ∈ the [registry](vocabularies.md); any relation may take `not-` — explicit negatives are
  infrastructure, not gaps.
- **untethered-must-be-tagged** — a unit with no resolvable grounding (`grounded-in` absent and
  `basis ∉ {inferred, ecosystem}`) is valid only if it carries `!untethered` (or `!deprecated`).
- **derive-honesty** — `plane`/`scope`/`maturity`/`grounding-status` appear only as a `!flag` that
  *deviates* from the rule above; a flag that restates the derived value is noise.
- no exact-duplicate unit; never both `R` and `not-R` with identical facets.
- a unit is *timeless for its `asof`* — no dated/incident narrative (that lives in references and the ADR
  operation buffer).

## Reference

A reference is a **field on an endpoint**, not its own triple. Three tagged kinds: `node:` (another KB
handle) · `config:` (a positional config node-path, e.g. a `_TESTS_` validation node) · `external:` (a
URI). It may be unresolved as long as it is tagged (surfaced for grilling, never treated as fact) and
carries no independent version — it rides the unit's `asof`.

> Machine form: the EBNF and cross-field constraints live in [`../schemas/atom.grammar.md`](../schemas/atom.grammar.md).

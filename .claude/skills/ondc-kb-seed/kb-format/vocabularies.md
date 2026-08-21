# Controlled vocabularies

A valid KB uses only these values. They are the closed alphabets the [validator](../validators/validate_kb.py)
checks.

## Relations — one flat registry

Relations live in `relations/` as **declared nodes**, each with a one-line definition. The registry is
**flat** (no core/provisional tier) and **openly extensible** — you add a relation by declaring one. The
discipline is in *use*, not in a closed list: assert a relation only when it **definitely** holds; leave
it out rather than force a weak one (closed-world: absence = not-known). Guardrail: every relation is a
*declared node with a definition* — never a free-text verb. Any relation may take **`not-`**; explicit
negatives are valid facts and mandatory closed-world infrastructure.

| relation | definition | family |
|---|---|---|
| `isa` | X is a kind of Y — builds the IS-A taxonomy (a DAG) | structural |
| `has-slot` | X declares a named slot / field Y | structural |
| `part-of` | X is a component of the whole Y | structural |
| `disjoint-with` | X and Y can't both hold of the same thing | structural |
| `scoped-to` | X's meaning/applicability is confined to context Y (position · provider · action · domain) — carries config **node-position semantics** without cloning the meaning | structural |
| `sent-by` | X (a message / flow step) is emitted by participant Y (BAP \| BPP) | structural |
| `precedes` | X must occur before Y | semantic |
| `requires` | X can't hold unless Y also does | semantic |
| `causes` | X brings about Y | semantic |
| `constrains` | X limits or guards Y | semantic |
| `wasDerivedFrom` | X was built from source Y | provenance · PROV-O |
| `wasRevisionOf` | X is a new version of Y | provenance · PROV-O |
| `wasInformedBy` | X was shaped by session / activity Y | provenance · PROV-O |
| `wasAttributedTo` | X is credited to authority Y | provenance · PROV-O |
| `wasGeneratedBy` | X was produced by activity Y | provenance · PROV-O |
| `used` | activity X consumed input Y | provenance · PROV-O |

The camelCase names are **PROV-O literals** borrowed verbatim for interoperability; our own relations are
kebab. Two principled families, not inconsistency — don't "standardize" the PROV-O names.

## `basis` — what backs the fact + how strongly

One field folding a fact's source kind, its grounding *kind*, and its derivation status, so backing is
stated once.

| basis | meaning | has `grounded-in`? |
|---|---|---|
| `declared` | config / spec declares it (the default, the bulk) | yes → config node |
| `sandbox-tested` | exercised in the sandbox | yes → obs ref |
| `observed-live` | seen in production (real participants do it) | yes → obs ref |
| `authority` | mandated by regulation / principle (the "why") | yes → authority doc |
| `ecosystem` | ecosystem rule / convention | optional |
| `derived` | built from other KB facts | yes → source unit(s) |
| `inferred` | model-guessed, unverified — **never asserted** | no (empty) |

## `grounded-in` — the pointer only

Optional, no kind prefix (basis owns the kind). Interpreted by `basis`: a config node
`<book>:<file>#<node-path>` (declared — a **positional path** that names a node, never a line number; the
path *is* the anchor because config meaning is position-dependent — see
[anchor.md](anchor.md#position-carries-meaning----scoped-to)), an obs ref (sandbox-tested /
observed-live), an authority ref in `references/` (authority), or a source unit / **anchor** handle
(derived / interned). Absent for `basis:inferred`.

## `!flags` — the only status written by hand

`plane`, `scope`, `grounding-status`, `maturity` are **derived** ([unit.md](unit.md)). Write a flag only
when the unit *deviates*:

| flag | meaning |
|---|---|
| `!untethered` | no resolvable ground — parked explicitly |
| `!deprecated` | ground removed / superseded |
| `!desired` | intended, not yet real — quarantined, never asserted |
| `!plane=<p>` | override the derived plane; `p ∈ {spec, session-logic, runtime-state, cross}` |

## Reference kinds & frame vocabularies

- **reference** (`ref-subject`/`ref-object`): `node · config · external`; may be unresolved-but-tagged.
- **frame kind**: `class · instance · concept · pattern`.
- **frame layer**: `protocol · domain`.
- **frame status**: `draft · solidified` (a skill may extend the lifecycle; these two are baseline).
- **node kind** (beyond frames): `anchor` — an interned schematic meaning ([anchor.md](anchor.md)); a
  light registry node, not a frame. Handle convention `anchor.<kebab>`.

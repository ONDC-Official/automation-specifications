# LOCATOR — trv10-2.0.1

"Where do I find X" for the `trv10-2.0.1` book (invariant 18). Every answer is a *place*,
never a restated fact — facts are only in `atoms.md`.

## By question

| I want … | look in | how to get there |
|---|---|---|
| any fact at all | `atoms.md` | grep the subject/object handle; one fact per line |
| what a handle `anchor.X` *means* | `anchors/index.md` | grep `\| anchor.X \|`; the row gives meaning + `grounded-in` |
| the config position a fact came from | `atoms.md` | read the `grounded-in:` field — `<book>:<file>#<node-path>` |
| the list of flows | `INDEX.md` § Flows covered | or `configs/release-eks-TRV10-2.0.1/config/flows/index.yaml` |
| one flow's node | `frames/flow.<kebab-flowId>.md` | grounded at that flow file's `meta.flowId` |
| one flow's step sequence | config flow file `steps[]` | steps are addressed by `action_id`, e.g. `#steps[on_cancel_hard]` |
| the list of protocol actions | `INDEX.md` § Actions covered | or `config/actions/index.yaml#supportedActions` |
| one action's node | `frames/action.<kebab>.md` | `on_issue_status` → `action.on-issue-status` |
| which action may legally follow which | `config/actions/index.yaml#supportedActions.<action>` | the value list is the allowed successors |
| async pairing / transaction partners | `config/actions/index.yaml#apiProperties.<action>` | `async_predecessor`, `transaction_partner` |
| ordering facts already interned | `atoms.md` | grep `precedes` |
| who sends a message (BAP vs BPP) | `atoms.md` | grep `sent-by`; config source is `steps[].owner` |
| a ride-hailing domain concept | `frames/concept.*.md` | e.g. `concept.driver-assignment`, `concept.igm` |
| the domain / use case node | `frames/dom.trv10.md`, `frames/usecase.ride-hailing.md` | grounded at `index.yaml#info.domain`, `attributes/Ride_hailing.yaml#meta.use_case_id` |
| the sector story, actors, key concepts | `config/docs/overview.md` | anchors point at `#summary`, `#sector-purpose`, `#real-world-actors`, `#key-concepts` |
| a field's required/owner/type/enum | `config/attributes/Ride_hailing.yaml` | path `attribute_set.<action>.<json.path>._description` |
| an enum's allowed values | `anchors/index.md` → `anchor.v-*` rows | they ground at `validations/index.yaml#_TESTS_.…VALID_ENUM_…` |
| a required-field rule | `anchors/index.md` → `anchor.v-*-req-*` rows | ground at `…_RETURN_[REQUIRED_…]` |
| a tag-code rule | `anchors/index.md` → `anchor.*-tag-code` rows | ground at `…_RETURN_[VALIDATE_TAG_…]` |
| an error code | `config/errors/index.yaml#code[<n>]` | 90201 route not serviceable · 90202 tracking not enabled · 90203 driver not assigned |
| the HTTP surface for an action | `config/specs/openapi.yaml#paths./<action>` | interned as `anchor.path-<action>` |
| units not yet promoted | `candidate-units.md` | staging only — never cite as fact |

## Relation census (what it is worth grepping `atoms.md` for)

| relation | lines | relation | lines |
|---|---|---|---|
| `isa` | 245 | `part-of` | 123 |
| `scoped-to` | 113 | `requires` | 94 |
| `constrains` | 68 | `sent-by` | 63 |
| `precedes` | 61 | `has-slot` | 28 |
| `causes` | 20 | `used` | 14 |
| `disjoint-with` | 6 | `wasRevisionOf` | 1 |

Counts exclude the 15 `not-` negatives (`not-requires` 3 · `not-isa` 3 · `not-has-slot` 3 ·
`not-causes` 3 · `not-scoped-to` 2 · `not-part-of` 1), which are facts in their own right —
closed-world infrastructure, not gaps. Grep `| not-` to read them.

## By id prefix (frames)

| prefix | kind / layer | count | grounded at |
|---|---|---|---|
| `flow.` | `instance` / `domain` | 11 | `flows/Ride-hailing/<file>.yaml#meta.flowId` |
| `action.` | `class` / `protocol` | 19 | `actions/index.yaml#supportedActions.<action>` |
| `concept.` | `concept` / `domain` | 13 | `docs/overview.md#<section>`, a flow `steps[…]`, or an `attribute_set.…` path |
| `dom.` | `concept` / `domain` | 1 | `index.yaml#info.domain` |
| `usecase.` | `concept` / `domain` | 1 | `attributes/Ride_hailing.yaml#meta.use_case_id` |

## By handle prefix (anchor registry, 287 rows)

| prefix | what it interns | typical ground |
|---|---|---|
| `anchor.v-*` (84) | one validation rule / group | `validations/index.yaml#_TESTS_.<action>[…]._RETURN_[…]` |
| `anchor.step-*` (23) | one flow step position | `flows/Ride-hailing/<file>.yaml#steps[<action_id>]` |
| `anchor.path-*` (19) | one OpenAPI path | `specs/openapi.yaml#paths./<action>` |
| `anchor.flow-*` (12) | one flow entry (+ `anchor.flow-step`) | `flows/index.yaml#flows[<flowId>]` |
| `anchor.error-*` (4) | the three error codes + the generic `anchor.error-code` | `errors/index.yaml#code[<n>]` |
| everything else | actions, attributes, actors, states, workbench concepts | `actions/`, `attributes/Ride_hailing.yaml`, `docs/overview.md`, `workbench:frames/*` |

## Cross-walk: frame ↔ anchor

A `flow.<tail>` frame and the registry row `anchor.flow-<tail>` name the same flow from two
sides: the frame is grounded at the flow file (`meta.flowId`), the anchor at the flow index
entry (`flows/index.yaml#flows[…]`). Same for `action.<kebab>` ↔ `anchor.<kebab>`
(`actions/index.yaml#supportedActions.<action>`). Atoms in this book address these subjects by
**anchor** handle; frames are the rendered node, not a second fact store.

## Not here

| X | why |
|---|---|
| `attributes/Ride-hailing.yaml` | orphan hyphen twin of `Ride_hailing.yaml`; not `$ref`'d by `attributes/index.yaml` — out of scope, nothing is grounded at it |
| `decisions/`, `references/`, `golden/` | not present in this book |
| `confidence`, free-text relations, line-number grounds | forbidden by the KB-storage contract |

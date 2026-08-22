# LOCATOR — fis13-health-2.0.1

"Where do I find X" for this book (invariant 18). Config paths are relative to
`configs/release-eks-FIS13-HEALTH-2.0.1/config/`; KB paths to `knowledge/fis13-health-2.0.1/`.

## In the KB

| I want… | Look in | How to find it |
|---|---|---|
| a fact (the only committed truth) | `atoms.md` | grep the handle: `grep 'anchor.on-select' atoms.md` |
| what a shared meaning *is* + where it was interned | `anchors/index.md` | one row per handle: `handle \| meaning \| grounded-in \| asof` |
| a declared node for a flow | `frames/flow.<kebab>.md` | e.g. `frames/flow.claim-motor-insurance.md` |
| a declared node for a protocol action | `frames/action.<kebab>.md` | e.g. `frames/action.on-status.md` (`kind: class`, `layer: protocol`) |
| a declared node for an error code | `frames/error.code-<code>.md` | `error.code-81201` … `error.code-81208` |
| a declared node for a recurring domain idea | `frames/concept.<kebab>.md` | e.g. `frames/concept.deferred-underwriting.md` |
| the flow family a flow belongs to | `frames/journey.<kebab>.md` + `atoms.md` | `grep -E 'isa \| anchor\.policy-' atoms.md` |
| the domain root | `frames/dom.fis13.md` | grounded at `index.yaml#info.domain` |
| counts, coverage, links | `INDEX.md` | — |
| not-yet-promoted material | `candidate-units.md` | **not** committed fact — never cite as truth |
| who sends a message (BAP vs BPP) | `atoms.md` | `grep 'sent-by' atoms.md` |
| what is explicitly *not* true | `atoms.md` | `grep -E '\| not-' atoms.md` (closed-world negatives) |
| facts with no resolvable ground | `atoms.md` | `grep '!untethered' atoms.md` (6 units) |
| model-guessed, never-asserted material | `atoms.md` | `grep 'basis:inferred' atoms.md` (2 units, quarantined) |

## In the config (what grounds what)

| I want… | Config node-path |
|---|---|
| the domain + version + use-case list | `index.yaml#info.domain`, `index.yaml#info.x-usecases` |
| the flow catalogue (id, usecase, tags, description) | `flows/index.yaml#flows[<flow-id>]` |
| a flow's step sequence | `flows/<USE CASE>/<File>.yaml#steps[<action_id>]` (steps are keyed by `action_id`) |
| whether a step is a seller-initiated callback | `flows/<USE CASE>/<File>.yaml#steps[<action_id>].unsolicited` |
| which action may legally follow which | `actions/index.yaml#supportedActions.<action>` |
| async predecessor / transaction partners of an action | `actions/index.yaml#apiProperties.<action>` |
| the per-action payload contract | `attributes/HEALTH_INSURANCE.yaml#attribute_set.<action>` · `attributes/MOTOR_INSURANCE.yaml#attribute_set.<action>` |
| buyer-side form fields | `attributes/<USE_CASE>.yaml#attribute_set.html_form` |
| seller-driven form fields | `attributes/<USE_CASE>.yaml#attribute_set.dynamic_form` |
| an enum's allowed values | `attributes/<USE_CASE>.yaml#…_description.enums[<VALUE>]` |
| a tag group's meaning | `attributes/<USE_CASE>.yaml#attribute_set.<action>.…tags.<TAG_GROUP>` |
| validation rules / test assertions | `validations/index.yaml#_TESTS_.<action>[<TEST_NAME>]` |
| the value a rule returns | `validations/index.yaml#_TESTS_.<action>[<TEST>]._RETURN_[<KEY>]` |
| error codes and their owner | `errors/index.yaml#code[<code>]` |
| Beckn object schemas | `specs/openapi.yaml#components.schemas.<Schema>` |
| API endpoints | `specs/openapi.yaml#paths./<action>` |
| narrative background (actors, key concepts) | `docs/overview.md#<heading-slug>` |

## Grounding rules to respect when editing

- A config ground is a **positional node-path**, never a line number
  (`unit.md#grounding`, invariant 4).
- An anchor is interned **once** in `anchors/index.md` and referenced by handle; a position that
  tweaks it records only the delta (invariant 8).
- An anchor does **not** need a frame — frames exist for flows, actions, errors, journeys, use
  cases, and genuinely recurring concepts only (`anchor.md`).
- Frame bodies stay light: a declaration, its ground, and a pointer to `atoms.md`. A frame asserts
  no fact that no unit carries (invariant 12).
- Relations, `basis` values, and `!flags` come only from `vocabularies.md`. `confidence` is never
  written.

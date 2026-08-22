# LOCATOR — fis13-sachet

"Where do I find X" (invariant 18). KB paths are relative to `knowledge/fis13-sachet/`;
config paths are relative to `configs/release-eks-FIS13-sachet/config/`.

## Start here

| I want to know… | look in the KB | grounded in config |
|---|---|---|
| every committed fact for this book | `atoms.md` | — |
| what a handle *means* | `anchors/index.md` (row per handle) | column 3 of that row |
| what nodes exist and how they connect | `INDEX.md`, then `frames/` | — |
| whether a fact is asserted or merely staged | asserted ⇒ `atoms.md`; staged ⇒ `candidate-units.md` | — |

## By question

| question | KB entry point | config node |
|---|---|---|
| which domain / version / branch is this? | `frames/anchor.ondc-fis13.md`, `frames/anchor.fis13-sachet-book.md` | `index.yaml#info.domain`, `#info.version`, `#info.x-branch-name` |
| which use cases exist? | `frames/anchor.{accidental,hospicash,transit}-insurance.md` | `index.yaml#info.x-usecases` |
| which flows exist, and how are they tagged? | `INDEX.md` § Flows covered; `frames/anchor.flow-*.md` | `flows/index.yaml#flows` (`.id`, `.usecase`, `.type`, `.tags`) |
| what steps a flow runs, in what order, and who owns each | — (`precedes` / `part-of` / `sent-by` units in `atoms.md`) | `flows/<usecase>/<FlowId>.yaml#steps[<action_id>]` — `.api`, `.owner`, `.responseFor`, `.description` |
| the payload a step sends | — | `flows/<usecase>/<FlowId>.yaml#steps[<action_id>].mock.defaultPayload` (and `.examples[0].payload`) |
| which actions are supported, and what may follow each | `frames/anchor.<action>.md` | `actions/index.yaml#supportedActions.<action>` |
| async predecessor / transaction partners of an action | — | `actions/index.yaml#apiProperties.<action>` |
| whether BAP or BPP sends an action | `INDEX.md` § Actions covered | `attributes/<usecase>_insurance.yaml#attribute_set.<action>.context.action._description.owner` |
| the HTTP surface (which actions have a path) | `frames/anchor.api-surface.md`; `anchor.path-*` rows in `anchors/index.md` | `specs/openapi.yaml#paths` — 9 paths only (`/search`, `/on_search`, `/select`, `/on_select`, `/init`, `/on_init`, `/confirm`, `/on_confirm`, `/on_update`) |
| what a request/response must contain | `frames/anchor.context-envelope.md` and the block frames | `validations/index.yaml#_TESTS_.<action>[<TEST_NAME>]` |
| the required context fields / regexes | `frames/anchor.context-envelope.md` | `validations/index.yaml#_TESTS_.search[SEARCH_CONTEXT]._RETURN_` |
| valid enum values (order status, fulfillment state, category code) | `frames/anchor.order-status.md`, `frames/anchor.fulfillment-state.md`, `frames/anchor.insurance-category-code.md` | `validations/index.yaml#…._RETURN_[VALID_*].enumList[<VALUE>]` |
| which tag groups exist and where | `frames/anchor.{master-policy,bap-inputs,general-info,policy-info,nominee-details}-tag.md` | `validations/index.yaml#…validTags[<TAG_CODE>]` |
| the values inside a tag group | `frames/anchor.{accidental,hospicash}-benefit-terms.md`, `frames/anchor.transit-consignment-inputs.md` | `validations/index.yaml#…validValues[<VALUE_CODE>]` |
| the three distinct `search` shapes | `frames/anchor.search-variant.md` + the three `frames/anchor.search-*.md` | `validations/index.yaml#_TESTS_.search` |
| error codes and their meanings | `frames/anchor.fis13-error-catalog.md`; `anchor.err-8220xx` rows in `anchors/index.md` | `errors/index.yaml#code[<code>]` — `.Event`, `.Description`, `.From` |
| the CD-balance failure path | `frames/anchor.cd-balance-check.md`, `frames/anchor.cd-balance-error.md` | `flows/<usecase>/CD_Balance_Error_*.yaml#steps[on_init_cd_balance_error]` |
| master policy / product / policy document concepts | `frames/anchor.master-policy.md`, `frames/anchor.insurance-product.md`, `frames/anchor.policy-id.md`, `frames/anchor.policy-document.md` | `docs/overview.md#key-concepts`, `validations/index.yaml` |
| prose background on the sector | — | `docs/overview.md` (`#summary`, `#sector--purpose`, `#real-world-actors`, `#use-cases`, `#key-concepts`, `#example-scenario`) |
| what changed in this release | — | `docs/release-notes.md`, `docs/references.md` |
| the attribute dictionary for a use case | `anchor.attr-set-*` rows in `anchors/index.md` | `attributes/<usecase>_insurance.yaml#attribute_set` (indexed by `attributes/index.yaml`) |

## Handle naming

| prefix | what it names | example |
|---|---|---|
| `anchor.flow-*` | one flow in `flows/index.yaml` | `anchor.flow-purchase-journey-transit` |
| `anchor.path-*` | one OpenAPI path | `anchor.path-on-confirm` |
| `anchor.err-*` | one code in `errors/index.yaml` | `anchor.err-822018` |
| `anchor.attr-set-*` | one attribute-set file | `anchor.attr-set-hospicash` |
| `anchor.*-tag` | a tag group (`descriptor.code` of a `tags[]` entry) | `anchor.nominee-details-tag` |
| `anchor.<action>` | a protocol action | `anchor.on-init` |

## Caveats

- **Frames are light on purpose.** A frame carries a declaration and one ground; it
  asserts nothing. If a frame and `atoms.md` disagree, `atoms.md` wins.
- **Not every anchor has a frame** (169 anchors, 63 frames). Unframed anchors are found
  by grepping `anchors/index.md`.
- **Workbench-grounded anchors** (`anchor.bap`, `anchor.bpp`, `anchor.validation-rule`,
  `anchor.api-path`, `anchor.error-code`, `anchor.usecase`, `anchor.runtime-concept`,
  `anchor.transaction-entry`, …) point at `workbench:…`, not at this config; they are
  deliberately unframed here.
- **`anchor.action`, `anchor.beckn-object`, `anchor.beckn-base-element`,
  `anchor.runtime-concept`** carry `-` in the registry's `grounded-in` column — they are
  taxonomy roots with no config position.

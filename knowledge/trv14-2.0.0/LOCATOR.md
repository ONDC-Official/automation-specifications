# LOCATOR — trv14-2.0.0

"Where do I find X" for the `trv14-2.0.0` book (invariant 18). Config paths are relative to
`configs/release-eks-TRV14-2.0.0/config/`; KB paths are relative to `knowledge/trv14-2.0.0/`.

## By question

| I want … | look in | how |
|---|---|---|
| every committed fact | `atoms.md` | one pipe-delimited unit per line; grep the handle |
| what a shared meaning *means* | `anchors/index.md` | 237 rows: `handle │ meaning │ grounded-in │ asof` |
| a named node (flow / action / concept) | `frames/<id>.md` | filename **is** the id |
| the navigation overview + counts | `INDEX.md` | flow table, action table, concept table |
| units not yet committed | `candidate-units.md` | staging only — never cite as fact |

## By KB handle prefix

| prefix | means | example |
|---|---|---|
| `anchor.*` | interned meaning — registry row in `anchors/index.md`; **all** atom subjects/objects use this form | `anchor.on-confirm` |
| `flow.*` | frame, `kind: instance`, `layer: domain` — one per flow | `flow.technical-cancellation` |
| `action.*` | frame, `kind: class`, `layer: protocol` — one per supported action | `action.on-status` |
| `concept.*` | frame, `kind: concept` — recurring domain/protocol concept | `concept.soft-cancel` |
| `dom.*` / `usecase.*` | frame, `kind: concept`, `layer: domain` — the domain and its use case | `dom.trv14` |
| `"QUOTED"` | a literal (enum value, code, tag name), not a node | `"SOFT_CANCEL"` |

Frames carry no facts. A frame names a node, cites one grounding position, and points at the
`anchor.*` handle under which its facts live in `atoms.md`.

## By config file

| I want … | config file | typical node-path |
|---|---|---|
| domain id, version, use-case list, security | `index.yaml` | `info.domain`, `info.x-usecases`, `security[0]` |
| which action may follow which | `actions/index.yaml` | `supportedActions.<action>` |
| async predecessor / transaction partners | `actions/index.yaml` | `apiProperties.<action>.async_predecessor` |
| the catalogue of flows + their tags | `flows/index.yaml` | `flows[<flowId>].tags`, `flows[<flowId>].config` |
| a flow's step sequence | `flows/unreserved-entry-pass/<file>.yaml` | `meta.flowId`, `steps[<action_id>].api`, `steps[<action_id>].owner` |
| a step's mock payload / validation script | `flows/unreserved-entry-pass/<file>.yaml` | `steps[<action_id>].mock.generate`, `.mock.validate` |
| assertions run against an action | `validations/index.yaml` | `_TESTS_.<action>[<BLOCK_NAME>]._RETURN_[<TEST_NAME>]` |
| an enum's allowed values | `validations/index.yaml` | `…[<TEST_NAME>].enumList` or `.validValues` |
| the gate that skips a validation block | `validations/index.yaml` | `_TESTS_.<action>[<BLOCK_NAME>]._CONTINUE_` |
| human-facing field documentation | `attributes/unreserved_entry_pass.yaml` | `attribute_set.<action>.<json.path>._description` |
| beckn schema shapes | `specs/openapi.yaml` | `components.schemas.<Schema>` |
| an API endpoint | `specs/openapi.yaml` | `paths./<action>.post` |
| registered error codes | `errors/index.yaml` | `code` (a list; each entry has `code`, `Event`, `Description`, `From`) |
| release prose | `docs/overview.md`, `docs/references.md`, `docs/release-notes.md` | — |

## Grounding path grammar

`<book>:<file>#<node-path>` — always a **positional path**, never a line number.

- `.` walks a mapping key: `info.domain`
- `[X]` selects: a mapping key (`supportedActions[search]`), or the list element whose
  `_NAME_` / `action_id` / `id` / `flowId` equals `X`
- validation blocks nest through `._RETURN_[…]` repeatedly

Example: `trv14-2.0.0:validations/index.yaml#_TESTS_.cancel[CANCEL_MESSAGE_1]._RETURN_[VALID_CANCELLATION_REASON_ID].enumList`

## Known gaps / traps

| trap | note |
|---|---|
| `attributes/unreserved-entry-pass.yaml` | hyphen-spelled orphan twin of `unreserved_entry_pass.yaml`. **Out of scope** — never ground to it |
| YAML will not parse with plain PyYAML | some files redefine anchors; load with `.claude/skills/ondc-kb-seed/tools/_yaml.py` (`_yaml.load(path)`), which uses js-yaml anchor semantics |
| `errors/index.yaml` is thin | only 3 codes (90201, 90202, 90203). Codes such as `93201` appear only in flow mocks (`steps[…].mock.generate`), not in the registry |
| flow ids contain spaces and parentheses | e.g. `User Cancellation (Full)`, `purchase_journey_without_form_with_IGM(v-2.0.0)` — the *file* name sanitises them; `meta.flowId` does not |
| `validations/index.yaml` declares `rating` / `on_rating` | those two actions are **not** in `actions/index.yaml#supportedActions` |
| `_TESTS_.<action>` is a **list**, not a map | select a block by its `_NAME_` |

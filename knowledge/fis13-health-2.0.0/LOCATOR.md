# fis13-health-2.0.0 — LOCATOR

Where do I find X. Scan this table first, then open only the named node — that is the
token-reduction path. Everything here is `asof: fis13-health-2.0.0`; the config book is
`configs/release-eks-FIS13-HEALTH-2.0.0/config/` and every `grounded-in` pointer in `atoms.md`
is written `fis13-health-2.0.0:<file>#<node-path>` (a **positional path**, never a line number).

Start at `INDEX.md` for counts and the full flow / action / use-case tables.

## Protocol surface

| I want to know… | KB node | Config node-path |
|---|---|---|
| which actions this domain supports | `frames/action.*.md` · `anchor.<action>` | `actions/index.yaml#supportedActions` |
| what may legally follow an action | atoms `anchor.<a> \| precedes \| anchor.<b>` | `actions/index.yaml#supportedActions.<action>` (the value list) |
| whether an action is a callback / who it pairs with | `anchor.async-predecessor` · `anchor.transaction-entry` | `actions/index.yaml#apiProperties.<action>.async_predecessor` · `.transaction_partner` |
| which action starts a transaction | atoms on `anchor.transaction-entry` | `actions/index.yaml#supportedActions.null` |
| BAP vs BPP ownership of a message | atoms `… \| sent-by \| anchor.bap` / `anchor.bpp` | `flows/<USECASE>/<flow>.yaml#steps[<action_id>].owner` |
| the HTTP surface / request-response schemas | `anchor.<beckn-object>` (e.g. `anchor.provider`, `anchor.item`, `anchor.payment`, `anchor.fulfillment`) | `specs/openapi.yaml#paths` · `specs/openapi.yaml#components.schemas.<Schema>` |

## Flows

| I want to know… | KB node | Config node-path |
|---|---|---|
| which flows exist, and for which use case | `INDEX.md` → *Flows covered* · `frames/flow.*.md` | `flows/index.yaml#flows[<flowId>].usecase` |
| whether a flow is mandatory / reportable / workbench-only | atoms grounded on the manifest | `flows/index.yaml#flows[<flowId>].tags` |
| what a flow is for, in one line | `flows/index.yaml` description | `flows/index.yaml#flows[<flowId>].description` |
| the identity of a flow file | `frames/flow.*.md` → `Grounded at:` | `flows/<USECASE>/<file>.yaml#meta.flowId` |
| the step spine of a flow (order, api, owner) | atoms `precedes` chains | `flows/<USECASE>/<file>.yaml#steps[<action_id>]` |
| the payload a step sends | — (payloads are not atoms) | `flows/<USECASE>/<file>.yaml#steps[<action_id>].mock.defaultPayload` |
| what a step carries forward into the session | `anchor.form-sequence` and friends | `flows/<USECASE>/<file>.yaml#steps[<action_id>].mock.saveData` |
| an unsolicited (BPP-pushed) callback | `anchor.bpp-initiated-message` | `flows/<USECASE>/<file>.yaml#steps[<action_id>].unsolicited` |
| a worked example payload for a step | — | `flows/<USECASE>/<file>.yaml#steps[<action_id>].examples` |

`<USECASE>` is one of the five directory names with a space in it — `HEALTH INSURANCE`,
`MOTOR INSURANCE`, `ACCIDENTAL INSURANCE`, `HOSPICASH INSURANCE`, `TRANSIT INSURANCE`.

## Fields, enums and tags

| I want to know… | KB node | Config node-path |
|---|---|---|
| whether a field is required for an action | `anchor.attribute-dictionary` | `attributes/<USECASE>.yaml#attribute_set.<action>.<json path>._description.required` |
| the allowed values of a coded field | the enum's own anchor (e.g. `anchor.add-on-cover`, `anchor.policy-doc`, `anchor.form-status-*`) | `attributes/<USECASE>.yaml#attribute_set.<action>.<json path>._description.enums` |
| which tag groups an action must carry | `anchor.*-tag` (e.g. `anchor.master-policy-tag`, `anchor.bap-inputs-tag`, `anchor.bap-terms-tag`) | `validations/index.yaml#_TESTS_.<action>[<TEST>]._RETURN_[<SUB>].validTags` |
| the members of a tag group | `anchor.bap-inputs-hospicash`, `anchor.bap-inputs-transit`, `anchor.policy-info-tag`, … | `validations/index.yaml#_TESTS_.<action>[<TEST>]._RETURN_[<SUB>].validValues` |
| the insurance category codes | `anchor.category-health`, `anchor.category-motor`, `anchor.category-micro-*` | `validations/index.yaml#_TESTS_.search[SEARCH_CATEGORY_CODE]._RETURN_[VALID_ENUM_CATEGORY_CODE].enumList` |
| context rules (ttl, city code, bap_id regex) | `anchor.context-ttl`, `anchor.context-city-code`, `anchor.context-bap-id` | `validations/index.yaml#_TESTS_.search[SEARCH_CONTEXT]._RETURN_[CONTEXT_REGEX]._RETURN_[<RULE>].reg` |
| a validation rule / what would NACK | atoms with `constrains` / `requires` | `validations/index.yaml#_TESTS_.<action>[<TEST>]` |
| what the session carries between steps | — | `validations/index.yaml#_SESSION_DATA_` |

`_TESTS_` is keyed by action (`search`, `on_search`, `select`, … `on_issue_status`); each entry is
addressed by its `_NAME_` in brackets and nests through `_RETURN_[…]`.

`attributes/<USECASE>.yaml` — `HEALTH_INSURANCE.yaml` and `MOTOR_INSURANCE.yaml` carry 16
`attribute_set` keys (14 actions + `html_form` + `dynamic_form`); `accidental_insurance.yaml`,
`hospicash_insurance.yaml` and `transit_insurance.yaml` carry 9 and no form keys.

## Forms (xinput)

| I want to know… | KB node | Config node-path |
|---|---|---|
| which forms a journey renders, and in what order | `anchor.form-*` (e.g. `anchor.form-ped`, `anchor.form-ekyc`, `anchor.form-cis`, `anchor.form-manual-review`, `anchor.form-claim`, `anchor.form-renew`) | `flows/<USECASE>/<file>.yaml#steps[<action_id>]` (the `on_*` step that emits the form) |
| html form vs dynamic form | `anchor.html-form` · `anchor.dynamic-form` | `attributes/HEALTH_INSURANCE.yaml#attribute_set.html_form` · `#attribute_set.dynamic_form` (also in `MOTOR_INSURANCE.yaml`; the three micro-insurance dictionaries have neither) |
| the form-response contract (submission_id, status) | `anchor.form-response`, `anchor.form-status-*` | `attributes/HEALTH_INSURANCE.yaml#attribute_set.select.message.order.items.xinput.form_response.status._description.enums` |
| the mime types a form may return | `anchor.form-mime-text-html`, `anchor.form-mime-application-html` | `docs/xinput-form-response.md#form-response` |

## Errors and failure paths

| I want to know… | KB node | Config node-path |
|---|---|---|
| the FIS13 error codes (8 of them, 81201–81208) | `anchor.error-812xx` · `anchor.fis13-error-code` | `errors/index.yaml#code[<code>].code` |
| what an error code means | atoms `anchor.error-812xx \| causes \| …` | `errors/index.yaml#code[<code>].Event` · `.Description` |
| who emits an error code | atoms `… \| sent-by \| anchor.bpp` | `errors/index.yaml#code[<code>].From` |
| the CD-balance failure path | `anchor.cd-balance-error` | `flows/HOSPICASH INSURANCE/CD_Balance_Error_Hospicash_Insurance.yaml#steps[on_init_cd_balance_error]` |
| payment-failure retry journeys | `frames/flow.payment-failure-*.md` | `flows/<USECASE>/Payment_Failure_*.yaml#meta.flowId` |
| grievance / IGM handling | `anchor.issue*`, `anchor.igm*` · `frames/action.issue.md`, `action.on-issue.md`, `action.on-issue-status.md` | `actions/index.yaml#supportedActions.issue` · `flows/<USECASE>/*_With_IGM*.yaml` |

## Domain background

| I want to know… | KB node | Config node-path |
|---|---|---|
| the domain and version this book covers | `frames/dom.fis13.md` · `anchor.ondc-fis13` | `index.yaml#info.domain` · `index.yaml#info.version` |
| which use cases are released | `frames/usecase.*.md` · `anchor.usecase-*` | `index.yaml#info.x-usecases` · `index.yaml#info.x-status` |
| the network actors | `anchor.bap`, `anchor.bpp`, `anchor.insurance-agency` | `docs/overview.md#realworld-actors` |
| domain key concepts (policy lifecycle, …) | `anchor.policy-lifecycle` | `docs/overview.md#key-concepts` |
| what changed in this release | — | `docs/release-notes.md` · `docs/references.md` |

## Runtime behaviour (not this config)

19 atoms ground into the workbench knowledge book rather than the config —
`grounded-in:workbench:frames/<frame>.md`. Read them there, not here:
`flow-state-machine`, `mock-runner-lib`, `validation-layers`, `validation-compiler`,
`transaction-session`, `spec-lifecycle-status`, `report-pramaan`, `ondc-ecosystem`,
`flow-usecase`, `domain-version`, `automation-specifications`, and
`workbench:scripts/onix-request-lifecycle.md`. Source:
`automation-framework/knowledge/protocol-workbench/`.

## Known gaps (closed-world: absence = not-known)

| gap | where it shows |
|---|---|
| 8 flow files have a frame but **no unit** in `atoms.md` | `INDEX.md` → *Flow coverage gap* |
| 89 of 438 anchors carry `-` as their ground (meaning interned, position not yet pinned) | `anchors/index.md`, column `grounded-in` |
| 11 atoms are explicitly parked as `!untethered` | `grep '!untethered' atoms.md` |
| 3 flow files collapse into one anchor (`anchor.flow-discovery-insurers`) | `INDEX.md` → *Flow coverage gap* |

Nothing outside `atoms.md` is a fact. Frames declare nodes; `anchors/index.md` interns meanings;
neither asserts anything the units do not carry (invariant 12).

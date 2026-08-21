# LOCATOR — trv11-2.0.0

"Where do I find X" for the `trv11-2.0.0` book. Config paths are relative to
`configs/release-eks-TRV11-2.0.0/config/`; KB paths are relative to `knowledge/trv11-2.0.0/`.
Every config pointer is a **positional node-path**, never a line number.

## By question

| I want to know… | KB surface | config ground |
|---|---|---|
| what the domain code is | `frames/dom.trv11.md`, `atoms.md` (`anchor.domain-code`) | `index.yaml#info.domain` |
| which use cases exist | `frames/usecase.metro.md`, `frames/usecase.bus.md` | `index.yaml#info.x-usecases` |
| whether the release is reportable | `frames/concept.reportable-flow.md` | `index.yaml#info.x-reporting` |
| which flows exist, and their use case | `INDEX.md` → "Flows covered", `frames/flow.*.md` | `flows/index.yaml#flows` |
| whether a flow is MANDATORY / OPTIONAL / REPORTABLE | `atoms.md` (`isa anchor.mandatory-flow` / `anchor.optional-flow` / `anchor.reportable-flow`) | `flows/index.yaml#flows[<FLOW_ID>].tags` |
| a flow's canonical id and use case | `frames/flow.*.md` | `flows/<UseCase>/<FILE>.yaml#meta.flowId`, `…#meta.use_case_id` |
| the steps of a flow, and who owns each | `atoms.md` (`sent-by`) | `flows/<UseCase>/<FILE>.yaml#steps[<action_id>].owner` |
| the request/response payload a step sends | — (not interned; read config) | `flows/<UseCase>/<FILE>.yaml#steps[<action_id>].mock.defaultPayload` |
| what a step asks the tester for | `atoms.md` (`requires` on `anchor.init-with-user-input`, `anchor.search-*`) | `flows/<UseCase>/<FILE>.yaml#steps[<action_id>].mock.inputs.jsonSchema.properties.<field>` |
| which protocol actions are supported | `frames/action.*.md`, `INDEX.md` → "Actions covered" | `actions/index.yaml#supportedActions` |
| what may legally follow an action | `atoms.md` (`precedes`) | `actions/index.yaml#supportedActions.<action>` |
| which action a callback answers | `atoms.md` (`requires`) | `actions/index.yaml#apiProperties.<action>.async_predecessor` |
| which prior calls an action depends on | `atoms.md` (`requires` / `not-requires`) | `actions/index.yaml#apiProperties.<action>.transaction_partner` |
| which actions are **not** supported here | `atoms.md` (`anchor.unsupported-action`) — no frame | `specs/openapi.yaml#paths./<action>` |
| a Beckn schema object (Provider, Item, Payment, …) | `anchors/index.md` — anchors, not frames | `specs/openapi.yaml#components.schemas.<Schema>` |
| a required field for an action | `atoms.md` (`requires`) | `validations/index.yaml#_TESTS_.<action>[<TEST_NAME>]` |
| the allowed values of an enum | `atoms.md` (`part-of` an `anchor.*` enum-set) | `validations/index.yaml#_TESTS_.<action>[<TEST_NAME>].enumList` |
| which JSON path an enum constrains | `atoms.md` (`constrains`) | `validations/index.yaml#_TESTS_.<action>[<TEST_NAME>].enumPath` / `.attr` |
| whether a rule applies only to Metro or only to Bus | `atoms.md` (`scoped-to anchor.usecase-*`) | `validations/index.yaml#_TESTS_.<action>[<TEST_NAME>].useCode` / `.useCasePath` |
| a tag group's valid codes | `atoms.md` (`part-of` an `anchor.tag-*`) | `validations/index.yaml#_TESTS_.<action>[validate_tag_<n>_<FAMILY>].validValues` |
| where a tag group hangs in the payload | `atoms.md` (`scoped-to`) | `validations/index.yaml#_TESTS_.<action>[validate_tag_<n>].tagPath`, `…._SCOPE_` |
| the attribute dictionary (owner / required / enums) | `atoms.md` (`sent-by`, `requires`) | `attributes/Metro.yaml#attribute_set.<action>.<path>._description.owner` / `.required` / `.enums` |
| an error code's meaning and what it guards | `anchors/index.md` (`anchor.error-<code>`) — no frame | `errors/index.yaml#code[<code>]`, `…[<code>].Description` |
| the IGM issue profile in force | `frames/concept.igm-1-0-0.md`, `frames/concept.igm-2-0-0.md` | `validations/index.yaml#_TESTS_.issue[ISSUE_VALIDATION_VERSION_100 \| _200]` |
| ticket types (SJT / SFSJT / RJT / PASS) | `frames/concept.ticket-type-code.md` | `validations/index.yaml#_TESTS_.on_select[REQUIRED_MESSAGE_CODE_16].enumList` |
| station codes and the station-code catalog | `frames/concept.station-code.md`, `frames/concept.station-code-catalog.md` | `validations/index.yaml#_TESTS_.on_search[REQUIRED_MESSAGE_CODE_20]`; `flows/Metro/STATION_CODE_FLOW_CATALOG.yaml#steps[on_search1_METRO_200].mock.defaultPayload.message.catalog` |
| the two-search pattern (catalog vs fare) | `frames/concept.search-catalog-discovery.md`, `frames/concept.search-fare-discovery.md` | `flows/Metro/STATION_CODE_FLOW_CATALOG.yaml#steps[search1_METRO_200]`; `flows/Metro/ORDER_TO_CONFIRM_TO_JOURNEY_COMPLETION_SJT.yaml#steps[search2_METRO_200]` |
| how a flow skips search_1 and select | `frames/concept.init-with-user-input.md` | `flows/Metro/ORDER_TO_CONFIRM_TO_JOURNEY_COMPLETION_SJT_WITHOUT_SEARCH_ND_SELECT.yaml#steps[init_with_user_input_METRO_200]` |
| the QR ticket / authorization token | `frames/concept.qr-ticket.md` | `validations/index.yaml#_TESTS_.on_confirm[REQUIRED_MESSAGE_TOKEN_32]` |
| order status values | `frames/concept.order-status.md` | `validations/index.yaml#_TESTS_.select[VALID_ENUM_MESSAGE_STATUS_7]` |
| two-phase user cancellation (soft → confirm) | `frames/concept.soft-cancel.md`, `frames/concept.confirm-cancel.md` | `flows/Metro/USER_CANCELLATION_FLOW.yaml#steps[cancel_soft_METRO_200 \| cancel_hard_METRO_200].mock.defaultPayload.message.descriptor.code` |
| technical cancellation (on_confirm beyond TTL) | `frames/concept.technical-cancellation.md` | `flows/Metro/TECHNICAL_CANCELLATION_FLOW.yaml#steps[cancel_tech_METRO_200]` |
| partial cancellation (via `update`) | `frames/concept.partial-cancellation.md` | `flows/Metro/PARTIAL_CANCELLATION_FLOW.yaml#steps[update_METRO_201]` |
| seller-initiated offline cancellation | `frames/concept.seller-offline-cancellation.md` | `flows/Metro/SELLER_OFFLINE_CANCELLATION_WITHOUT_SEARCH_ND_SELECT.yaml#steps[on_cancel_unsoliciated]` |
| what is *not* yet committed | `candidate-units.md` | — |

## By handle shape

| handle / id | what it is | where it lives |
|---|---|---|
| `anchor.<kebab>` | interned schematic meaning | row in `anchors/index.md`; units in `atoms.md` |
| `flow.<usecase>-<name>` | a flow frame (`instance` · `domain`) | `frames/flow.*.md` — pairs with `anchor.flow-<usecase>-<name>` |
| `action.<name>` | a protocol action frame (`class` · `protocol`) | `frames/action.*.md` — pairs with `anchor.<name>` |
| `concept.<kebab>`, `dom.trv11`, `usecase.<name>` | a recurring domain concept (`concept` · `domain`) | `frames/concept.*.md`, `frames/dom.*.md`, `frames/usecase.*.md` |
| `"literal"` | a literal value (enum member, JSON path, status) | object position in `atoms.md` |

Frame ↔ anchor is a 1:1 naming convention, not an asserted relation: every frame body names the
`anchor.*` handle its units are filed under.

## Grep recipes

Run from the repo root.

```sh
# every unit whose subject is one action
grep '^anchor\.on-confirm ' knowledge/trv11-2.0.0/atoms.md

# everything a flow declares (subject or object)
grep 'anchor\.flow-metro-sjt-purchase' knowledge/trv11-2.0.0/atoms.md

# every Metro-only rule
grep 'anchor\.usecase-metro' knowledge/trv11-2.0.0/atoms.md

# every explicit negative (closed-world infrastructure)
grep -E '\| not-[a-z-]+ \|' knowledge/trv11-2.0.0/atoms.md

# every parked / ungrounded unit
grep '!untethered' knowledge/trv11-2.0.0/atoms.md

# every unit grounded in the validation library
grep 'validations/index.yaml' knowledge/trv11-2.0.0/atoms.md

# one anchor's canonical meaning + its config ground
grep '^. anchor\.qr-ticket ' knowledge/trv11-2.0.0/anchors/index.md

# validate the book
python3 .claude/skills/ondc-kb-seed/tools/validate_kb.py knowledge/trv11-2.0.0
```

# trv11-2.1.0 — LOCATOR

Where do I find X. Config paths are relative to
`configs/release-eks-TRV11-2.1.0/config/`; every node path here is positional and was
resolved against the actual YAML — never a line number.

Companion: [`INDEX.md`](INDEX.md) — counts, and the full flow / action / error tables.

## Start here

| I want… | go to |
|---|---|
| a fact, with its basis and ground | `atoms.md` — one triple per line |
| what a recurring meaning *is* | `anchors/index.md` — 98 rows, handle → meaning → ground |
| a named node (flow, action, error, step, concept) | `frames/<id>.md` — filename **is** the id |
| the whole book at a glance | `INDEX.md` |
| the raw spec | `configs/release-eks-TRV11-2.1.0/config/` |
| to query instead of grep | `.claude/skills/ondc-kb/kb_query.py`, e.g. `about anchor.pass --book trv11-2.1.0` |

## By question

| question | KB node | config ground |
|---|---|---|
| which domain / version is this | `dom.trv11` | `index.yaml#info.domain`, `index.yaml#info.version` |
| which use cases exist | `usecase.bus`, `usecase.metro` | `index.yaml#info.x-usecases` |
| which actions exist, and what may follow one | `action.*` (17) | `actions/index.yaml#supportedActions` |
| which action is a callback to which | `action.*` | `actions/index.yaml#apiProperties.<action>.async_predecessor` |
| which action may open a transaction | `action.search/select/init/confirm/update` | `actions/index.yaml#supportedActions.null` |
| which actions may partner in one transaction | `action.*` | `actions/index.yaml#apiProperties.<action>.transaction_partner` |
| who sends a call, BAP or BPP | atoms with relation `sent-by` | `flows/**/<flow>.yaml#steps[<action_id>].owner` |
| which call answers which | atoms with relation `precedes` | `flows/**/<flow>.yaml#steps[<action_id>].responseFor` |
| which calls arrive unsolicited | `anchor.unsolicited-callback` | `flows/**/<flow>.yaml#steps[<action_id>].unsolicited` |
| what flows exist and how they are tagged | `flow.*` (27) | `flows/index.yaml#flows` |
| which use case a flow belongs to | `flow.*` | `flows/<Usecase>/<flow>.yaml#meta.use_case_id` |
| the step list of a flow | `flow.*` | `flows/<Usecase>/<flow>.yaml#steps` |
| the payload a step mocks | — | `flows/<Usecase>/<flow>.yaml#steps[<action_id>].mock.defaultPayload` |
| the input form a step asks for | — | `flows/<Usecase>/<flow>.yaml#steps[<action_id>].mock.inputs.jsonSchema` |
| what a step hands to later steps | `anchor.session-data` | `flows/<Usecase>/<flow>.yaml#steps[<action_id>].mock.saveData` |
| what a field *means* | `anchor.attribute-dictionary` | `attributes/Bus.yaml#attribute_set.<action>`, `attributes/Metro.yaml#attribute_set.<action>` |
| what a field is *checked* against | `anchor.validation-node` | `validations/index.yaml#_TESTS_.<action>` |
| when a check is skipped | `anchor.continue-guard`, `anchor.usecase-path-guard` | `validations/index.yaml#_TESTS_.<action>[<TEST>]._CONTINUE_`, `…[<TEST>].useCasePath` |
| session values the runner keeps | `anchor.session-data` | `validations/index.yaml#_SESSION_DATA_` |
| what error codes exist | `error.code-*` (18) | `errors/index.yaml#code[<code>]` |
| the wire schema of an object | `anchor.order`, `anchor.item`, … | `specs/openapi.yaml#components.schemas.<Name>` |
| the HTTP surface | `anchor.track`, `anchor.rating`, `anchor.support` | `specs/openapi.yaml#paths[/<action>]` |
| human prose about the release | — | `docs/overview.md`, `docs/references.md`, `docs/release-notes.md` |

## By TRV11 subject

| subject | KB node | config ground |
|---|---|---|
| ticket vs pass vs agent ticket | `concept.fulfillment-type`, `anchor.fulfillment-type`, `anchor.fulfillment-type-catalog` | `validations/index.yaml#_TESTS_.on_search[REQUIRED_MESSAGE_TYPE_18].enumList` |
| item codes (SJT / RJT / SFSJT / PASS / PURCHASE / RECHARGE / AGENT_TICKETING) | `anchor.item-code`, `anchor.item-descriptor-code` | `validations/index.yaml#_TESTS_.on_search[VALID_ITEM_DESCRIPTOR_CODE].validValues` |
| bus vs metro category | `anchor.vehicle-category`, `anchor.vehicle-variant` | `validations/index.yaml#_TESTS_.search[REQUIRED_MESSAGE_CATEGORY_12].enumList` |
| QR / OTP at the gate | `concept.stop-authorization`, `anchor.stop-auth-type`, `anchor.auth-status` | `validations/index.yaml#_TESTS_.on_confirm[REQUIRED_MESSAGE_TYPE_31].enumList` |
| stop kinds (START / END / …) | `anchor.stop`, `anchor.stop-type` | `validations/index.yaml#_TESTS_.on_search[VALID_STOP_TYPE_VALUES].validValues` |
| soft cancel then confirm cancel | `concept.two-phase-cancellation`, `step.cancel-soft`, `step.cancel-hard` | `validations/index.yaml#_TESTS_.cancel[REQUIRED_MESSAGE_CODE_16].enumList` |
| order lifecycle states | `anchor.order-status`, `anchor.fulfillment-state-code` | `attributes/Bus.yaml#attribute_set.on_status.message.order.status._description.enums` |
| what an update call targets | `anchor.update-target`, `step.update-end-stop-soft` | `validations/index.yaml#_TESTS_.update[REQUIRED_MESSAGE_UPDATE_TARGET_14]` |
| who collects payment, and in what state | `anchor.payment-collector`, `anchor.payment-status`, `anchor.payment-type` | `validations/index.yaml#_TESTS_.confirm[REQUIRED_MESSAGE_COLLECTED_BY_19].enumList` |
| buyer-finder fees / settlement | `anchor.bap-terms`, `anchor.settlement-terms` | `validations/index.yaml#_TESTS_.search[validate_tag_0_BUYER_FINDER_FEES]` |
| fare breakup titles | `anchor.quote-breakup-title`, `anchor.quotation` | `validations/index.yaml#_TESTS_.on_select[REQUIRED_MESSAGE_TITLE_34].enumList` |
| fare policy on the catalog | `anchor.fare-policy-tag` | `validations/index.yaml#_TESTS_.on_search[validate_tag_0_FARE_POLICY]` |
| catalog paging | `anchor.pagination-tag`, `flow.bus-search-pagination` | `validations/index.yaml#_TESTS_.search[validate_tag_1_PAGINATION]` |
| route / schedule / ticket info tags | `anchor.route-info-tag`, `anchor.scheduled-info-tag`, `anchor.ticket-info-tag`, `anchor.info-tag` | `validations/index.yaml#_TESTS_.on_search[validate_tag_1_ROUTE_INFO]` |
| extra provider APIs (GTFS etc.) | `anchor.additional-apis` | `attributes/Bus.yaml#attribute_set.on_search.message.catalog.providers.tags.ADDITIONAL_APIS._description` |
| metro card buy / top-up | `flow.metro-card-purchase`, `flow.metro-card-recharge`, `anchor.card-identifier`, `anchor.creds-type` | `flows/Metro/METRO_CARD_RECHARGE.yaml#steps[select_METRO_RECHARGE_210].mock.inputs.jsonSchema.properties.credential_type` |
| agent onboarding and agent-sold tickets | `journey.agent-onboarding`, `journey.agent-issued-ticket`, `anchor.agent`, `anchor.agent-ticketing` | `flows/Bus/IntraCity_Agent_Login_Route_allotment_by_Seller_.yaml#steps` |
| grievance / IGM | `journey.grievance`, `step.issue-open`, `step.issue-close`, `action.issue` | `flows/Bus/IntraCity_Purchase_Journey_FlowCode_Based_Flow_With_IGM_v-1_0_0_.yaml#steps` |
| linking a new order to an old one | `anchor.ref-order-ids` | `specs/openapi.yaml#components.schemas.Order.properties.ref_order_ids` |

## Where the sharp edges are

| edge | look at |
|---|---|
| a `&NAME` anchor declared twice, meaning two things | `concept.duplicate-yaml-anchor` — 7 names, none interned from a single definition |
| a `responseFor` that yields no ordering edge | `concept.unwired-response-for` — 1 dangling, 1 mutual |
| anchors with no config ground (`grounded-in: -`) | `anchors/index.md`; the units carry `!untethered` |
| facts grounded outside this book | any `workbench:frames/…` ground — resolves under `automation-framework/knowledge/protocol-workbench/` |
| `attributes/index.yaml` lists `Metro.yaml` twice | `attributes/index.yaml` — the duplicate `$ref` is in the config, not in the KB |
| `attribute_set` does not cover every action | Bus declares 12 of 17, Metro declares 8 — `attributes/Bus.yaml#attribute_set`, `attributes/Metro.yaml#attribute_set` |

## Reading an atom line

```text
subject | relation | object | basis:<b> | asof:trv11-2.1.0 | grounded-in:<book>:<file>#<node> [| !flag]
```

`basis` says how strongly the fact is backed (`declared` is the config saying so;
`inferred` is a guess and is never asserted). A `not-` relation is a **positive** fact — the
spec establishes that the thing does *not* hold. Absence is not-known, not false.
Format contract: `.claude/skills/ondc-kb-seed/kb-format/`.

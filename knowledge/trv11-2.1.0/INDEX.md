# trv11-2.1.0 — book index

| | |
|---|---|
| book id | `trv11-2.1.0` |
| domain | `ONDC:TRV11` (`index.yaml#info.domain`) |
| version | `2.1.0` |
| use cases | Bus, Metro (`index.yaml#info.x-usecases`) |
| config root | `configs/release-eks-TRV11-2.1.0/config/` |
| atoms | 642 (`atoms.md`) |
| anchors | 98 (`anchors/index.md`) |
| frames | 93 (`frames/*.md`) |
| ADRs | 0 |

Frames by kind: 17 `action.*` (class · protocol) · 27 `flow.*` · 18 `error.*` · 13 `step.*` ·
10 `journey.*` · 5 `concept.*` · 2 `usecase.*` · 1 `dom.*`.

Navigation companion: [`LOCATOR.md`](LOCATOR.md) — "where do I find X".

---

## Protocol actions — 17 of 17 covered

Every action in `actions/index.yaml#supportedActions` has a frame; each frame names the
interned handle in `anchors/index.md` that the atoms actually carry.

| frame | anchor handle | call properties |
|---|---|---|
| `action.search` | `anchor.search` | `actions/index.yaml#apiProperties.search` |
| `action.on-search` | `anchor.on-search` | `actions/index.yaml#apiProperties.on_search` |
| `action.select` | `anchor.select` | `actions/index.yaml#apiProperties.select` |
| `action.on-select` | `anchor.on-select` | `actions/index.yaml#apiProperties.on_select` |
| `action.init` | `anchor.init` | `actions/index.yaml#apiProperties.init` |
| `action.on-init` | `anchor.on-init` | `actions/index.yaml#apiProperties.on_init` |
| `action.confirm` | `anchor.confirm` | `actions/index.yaml#apiProperties.confirm` |
| `action.on-confirm` | `anchor.on-confirm` | `actions/index.yaml#apiProperties.on_confirm` |
| `action.status` | `anchor.status` | `actions/index.yaml#apiProperties.status` |
| `action.on-status` | `anchor.on-status` | `actions/index.yaml#apiProperties.on_status` |
| `action.cancel` | `anchor.cancel` | `actions/index.yaml#apiProperties.cancel` |
| `action.on-cancel` | `anchor.on-cancel` | `actions/index.yaml#apiProperties.on_cancel` |
| `action.update` | `anchor.update` | `actions/index.yaml#apiProperties.update` |
| `action.on-update` | `anchor.on-update` | `actions/index.yaml#apiProperties.on_update` |
| `action.issue` | `anchor.issue` | `actions/index.yaml#apiProperties.issue` |
| `action.on-issue` | `anchor.on-issue` | `actions/index.yaml#apiProperties.on_issue` |
| `action.on-issue-status` | `anchor.on-issue-status` | `actions/index.yaml#apiProperties.on_issue_status` |

Transaction-entry actions (may open a transaction, per `supportedActions.null`): `search`,
`select`, `init`, `confirm`, `update`.

`track`, `rating` and `support` (and their callbacks) have paths in `specs/openapi.yaml` but
are absent from `supportedActions`, so they get an anchor and no `action.*` frame — see
`anchor.track` / `anchor.rating` / `anchor.support` in `anchors/index.md`.

---

## Flows — 27 of 27 covered

| frame | use case | journey | config file (under `flows/`) |
|---|---|---|---|
| `flow.bus-agent-activation` | usecase.bus | journey.agent-onboarding | `Bus/IntraCity_Agent_Activation_Route_Selection_by_Agent_.yaml` |
| `flow.bus-agent-login` | usecase.bus | journey.agent-onboarding | `Bus/IntraCity_Agent_Login_Route_allotment_by_Seller_.yaml` |
| `flow.bus-agent-purchase` | usecase.bus | journey.agent-issued-ticket | `Bus/IntraCity_Purchase_Journey_Agent_Based_.yaml` |
| `flow.bus-base-order-update` | usecase.bus | journey.post-order-amendment | `Bus/IntraCity_Base_Order_Update_Journey.yaml` |
| `flow.bus-purchase-code-based` | usecase.bus | journey.purchase | `Bus/IntraCity_Purchase_Journey_Flow_Code_Based.yaml` |
| `flow.bus-purchase-igm` | usecase.bus | journey.grievance | `Bus/IntraCity_Purchase_Journey_FlowCode_Based_Flow_With_IGM_v-1_0_0_.yaml` |
| `flow.bus-search-pagination` | usecase.bus | journey.discovery | `Bus/IntraCity_Search_Pagination_Flow_Code_Based.yaml` |
| `flow.bus-seller-based-confirmation` | usecase.bus | journey.purchase | `Bus/Intracity_Seller_Based_Confirmation_flow.yaml` |
| `flow.bus-technical-cancellation` | usecase.bus | journey.cancellation | `Bus/IntraCity_Technical_Cancellation_Flow.yaml` |
| `flow.bus-unlimited-passes` | usecase.bus | journey.unlimited-pass | `Bus/IntraCity_Unlimited_Passes_Flow_Code_Based_.yaml` |
| `flow.bus-user-based-confirmation` | usecase.bus | journey.purchase | `Bus/IntraCity_User_Based_Confirmation_flow.yaml` |
| `flow.bus-user-cancellation` | usecase.bus | journey.cancellation | `Bus/IntraCity_User_Cancellation_Flow.yaml` |
| `flow.bus-vehicle-based-confirmation-with-update` | usecase.bus | journey.purchase | `Bus/IntraCity_Vehicle_Based_Confirmation_flow_With_Update_Call_.yaml` |
| `flow.bus-vehicle-based-confirmation-without-update` | usecase.bus | journey.purchase | `Bus/IntraCity_Vehicle_Based_Confirmation_flow_Without_Update_Call_.yaml` |
| `flow.metro-card-purchase` | usecase.metro | journey.stored-value-instrument | `Metro/METRO_CARD_PURCHASE.yaml` |
| `flow.metro-card-recharge` | usecase.metro | journey.stored-value-instrument | `Metro/METRO_CARD_RECHARGE.yaml` |
| `flow.metro-delayed-cancellation-accepted` | usecase.metro | journey.cancellation | `Metro/DELAYED_CANCELLATION_FLOW_ACCEPTED.yaml` |
| `flow.metro-delayed-cancellation-rejected` | usecase.metro | journey.cancellation | `Metro/DELAYED_CANCELLATION_FLOW_REJECTED.yaml` |
| `flow.metro-end-stop-update` | usecase.metro | journey.post-order-amendment | `Metro/END_STOP_UPDATE_FLOW.yaml` |
| `flow.metro-master-search` | usecase.metro | journey.discovery | `Metro/METRO_MASTER_SEARCH_FLOW.yaml` |
| `flow.metro-offline-cancellation` | usecase.metro | journey.cancellation | `Metro/OFFLINE_CANCELLATION_FLOW.yaml` |
| `flow.metro-partial-cancellation` | usecase.metro | journey.cancellation | `Metro/PARTIAL_CANCELLATION_FLOW.yaml` |
| `flow.metro-purchase-station-code` | usecase.metro | journey.purchase | `Metro/PURCHASE_JOURNEY_STATION_CODE_BASED_FLOW.yaml` |
| `flow.metro-purchase-station-code-igm` | usecase.metro | journey.grievance | `Metro/PURCHASE_JOURNEY_STATION_CODE_BASED_FLOW_WITH_IGM_v-1_0_0_.yaml` |
| `flow.metro-technical-cancellation` | usecase.metro | journey.cancellation | `Metro/TECHNICAL_CANCELLATION_FLOW.yaml` |
| `flow.metro-unlimited-pass` | usecase.metro | journey.unlimited-pass | `Metro/METRO_UNLIMITED_PASS_FLOW.yaml` |
| `flow.metro-user-cancellation` | usecase.metro | journey.cancellation | `Metro/USER_CANCELLATION_FLOW.yaml` |

---

## Journeys — 10

`journey.agent-issued-ticket` · `journey.agent-onboarding` · `journey.cancellation` ·
`journey.discovery` · `journey.grievance` · `journey.post-order-amendment` ·
`journey.pre-known-item-purchase` · `journey.purchase` · `journey.stored-value-instrument` ·
`journey.unlimited-pass`

Each is grounded in the workbench frame `workbench:frames/flow-usecase.md`, not in this
book's config — journeys are the cross-book classification the flows hang off.

## Named steps — 13

`step.cancel-soft` · `step.cancel-hard` · `step.on-cancel-soft` · `step.on-cancel-hard` ·
`step.on-cancel-initiated` · `step.status-technical-cancel` · `step.update-soft-cancel` ·
`step.update-confirm-cancel` · `step.update-end-stop-soft` · `step.update-end-stop-payment` ·
`step.update-end-stop-confirm` · `step.issue-open` · `step.issue-close`

These are the steps that carry meaning beyond "the Nth call" — the cancellation and
end-stop-update legs, and the two IGM legs.

## Concepts — 5

| frame | what it is for |
|---|---|
| `concept.fulfillment-type` | the ROUTE/TRIP/PASS/TICKET/STOPS/AGENT_TICKETING/ONLINE discriminator |
| `concept.stop-authorization` | authorization type on the START stop + Metro-only claim status |
| `concept.two-phase-cancellation` | the soft-then-confirm `cancel` shape shared by the cancellation flows |
| `concept.duplicate-yaml-anchor` | the 7 duplicate `&NAME` declarations — ambiguity recorded, not resolved |
| `concept.unwired-response-for` | the 2 `responseFor` values that yield no `precedes` edge |

## Errors — 18

| frame | event | from |
|---|---|---|
| `error.code-30001` | Internal Error | BPP |
| `error.code-30008` | Location unserviceable | BPP |
| `error.code-50001` | Cancellation not possible | BPP |
| `error.code-91201` | Route Serviceability error | BPP |
| `error.code-91202` | Origin station not serviceable | BPP |
| `error.code-91203` | Destination not serviceable | BPP |
| `error.code-91204` | Maximum order qty exceeded | BPP |
| `error.code-91205` | Tracking not enabled | BPP |
| `error.code-91206` | Temporarily unavailable | BPP |
| `error.code-91207` | Transaction failure | BPP |
| `error.code-91208` | Out-of-operational hours | BPP |
| `error.code-91209` | Error in retrieving the QR | BPP |
| `error.code-91210` | Unable to get stations data | BPP |
| `error.code-91211` | Fare fetch error | BPP |
| `error.code-91212` | Invalid transaction | BPP |
| `error.code-91213` | Stale transaction | BPP |
| `error.code-91214` | Wrong fare while booking ticket | BPP |
| `error.code-91215` | Item not found | BPP |

All 18 are grounded at `errors/index.yaml#code[<code>]`.

---

## Known open items

Recorded so their absence reads as a decision, not a gap. Details in the frames named.

- **7 duplicate YAML anchors** — `ADDITIONAL_APIS`, `BPP_TERMS`, `COMMON_FULFILLMENT_ITEMS`,
  `PASS`, `REQUIRED_ITEM_FULFILLMENT_IDS`, `REQUIRED_ORDER_ID`, `TICKET`. No single definition
  is interned. → `concept.duplicate-yaml-anchor`
- **2 unusable `responseFor` values** — one dangling, one mutual. No `precedes` atom asserted
  for either. → `concept.unwired-response-for`
- **9 `!untethered` units**, over 7 anchors with `grounded-in: -` in `anchors/index.md`:
  `anchor.action`, `anchor.beckn-object`, `anchor.runtime-concept` and `anchor.tag1` are
  abstract parents no single position owns; `anchor.common-fulfillment-items`,
  `anchor.required-item-fulfillment-ids` and `anchor.required-order-id` are three of the
  duplicate-anchor names above. No `!deprecated` and no `!desired` units in this book.

## Files in this book

| file | what it holds |
|---|---|
| `atoms.md` | the facts, one triple per line; structural atoms first, then Stage E units |
| `anchors/index.md` | the 98 interned meanings: handle → meaning → grounded-in → asof |
| `frames/*.md` | the 93 node files; filename = frame `id` |
| `candidate-units.md` | pre-merge Stage E output; query `atoms.md` instead |
| `INDEX.md` | this file |
| `LOCATOR.md` | where-do-I-find-X table |

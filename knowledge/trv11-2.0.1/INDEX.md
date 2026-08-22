# INDEX — trv11-2.0.1

Navigation surface for this book (invariant 18). Nothing here is a fact — every fact lives in
`atoms.md`, every interned meaning in `anchors/index.md`. This page tells you **what exists** and
**where to open it**; `LOCATOR.md` tells you **where to find X**.

## The book

| | |
|---|---|
| book id | `trv11-2.0.1` |
| domain | `ONDC:TRV11` — intra-city public transit ticketing |
| version | `2.0.1` (`x-branch-name: draft-TRV11-2.0.1`) |
| use cases | Bus · Metro |
| config (Ground 0) | `configs/release-eks-TRV11-2.0.1/config/` |
| manifest | `configs/release-eks-TRV11-2.0.1/config/index.yaml` |

## Counts

| surface | count | file |
|---|---|---|
| atoms | 753 | `atoms.md` |
| anchors (interned meanings) | 178 | `anchors/index.md` |
| frames | 93 | `frames/*.md` |
| — flows (`instance` · `domain`) | 42 | `frames/flow.*.md` |
| — protocol actions (`class` · `protocol`) | 17 + `anchor.action` | `frames/anchor.*.md` |
| — concepts (`concept`) | 13 | `frames/anchor.*.md`, `frames/trv11*.md` |
| — error codes (`instance` · `domain`) | 18 | `frames/error.code-*.md` |
| — doc notes | 2 | `frames/docs.*.md` |
| candidate units (pre-merge Stage E) | — | `candidate-units.md` |

## Flows covered — 42 / 42 in `flows/index.yaml`

Every flow declared in `configs/release-eks-TRV11-2.0.1/config/flows/index.yaml` has a frame.
Frame ground is that flow's `#meta.description` node.

### Bus — 13

| frame | flow id (config) | flow file | tags |
|---|---|---|---|
| `flow.bus-merchant-side-cancellation` | `IntraCity_Merchant_Side_Cancellation` | `IntraCity_Merchant_Side_Cancellation.yaml` | PRAMAAN · MANDATORY · REPORTABLE · WORKBENCH |
| `flow.bus-monthly-pass-purchase` | `IntraCity_Monthly_Passes_Flow_Code_Based` | `IntraCity_Monthly_Passes_Flow_Code_Based.yaml` | PRAMAAN · WORKBENCH · MANDATORY · REPORTABLE |
| `flow.bus-purchase-igm-no-action-v2` | `IntraCity_Purchase_Journey_FlowCode_Based_Flow_With_IGM_No_Action(v-2.0.0)` | `IntraCity_Purchase_Journey_FlowCode_Based_Flow_With_IGM_No_Action_v-2_0_0_.yaml` | MANDATORY · WORKBENCH |
| `flow.bus-purchase-igm-rejection-v2` | `IntraCity_Purchase_Journey_FlowCode_Based_Flow_With_IGM_Rejection(v-2.0.0)` | `IntraCity_Purchase_Journey_FlowCode_Based_Flow_With_IGM_Rejection_v-2_0_0_.yaml` | MANDATORY · WORKBENCH |
| `flow.bus-purchase-igm-v1` | `IntraCity_Purchase_Journey_FlowCode_Based_Flow_With_IGM(v-1.0.0)` | `IntraCity_Purchase_Journey_FlowCode_Based_Flow_With_IGM_v-1_0_0_.yaml` | MANDATORY · WORKBENCH |
| `flow.bus-purchase-igm-v2` | `IntraCity_Purchase_Journey_FlowCode_Based_Flow_With_IGM(v-2.0.0)` | `IntraCity_Purchase_Journey_FlowCode_Based_Flow_With_IGM_v-2_0_0_.yaml` | MANDATORY · WORKBENCH |
| `flow.bus-purchase-journey` | `IntraCity_Purchase_Journey_Flow_Code_Based` | `IntraCity_Purchase_Journey_Flow_Code_Based.yaml` | PRAMAAN · MANDATORY · REPORTABLE · WORKBENCH |
| `flow.bus-search-pagination` | `IntraCity_Search_Pagination_FlowCode_Based` | `IntraCity_Search_Pagination_FlowCode_Based.yaml` | WORKBENCH · OPTIONAL |
| `flow.bus-technical-cancellation` | `IntraCity_Technical_Cancellation_Flow` | `IntraCity_Technical_Cancellation_Flow.yaml` | PRAMAAN · MANDATORY · REPORTABLE · WORKBENCH |
| `flow.bus-user-based-confirmation` | `IntraCity_User_Based_Confirmation_flow` | `IntraCity_User_Based_Confirmation_flow.yaml` | WORKBENCH · OPTIONAL |
| `flow.bus-user-cancellation` | `IntraCity_User_Cancellation_Flow` | `IntraCity_User_Cancellation_Flow.yaml` | PRAMAAN · MANDATORY · REPORTABLE · WORKBENCH |
| `flow.bus-vehicle-based-confirmation-with-update` | `IntraCity_Vehicle_Based_Confirmation_flow(With Update Call)` | `IntraCity_Vehicle_Based_Confirmation_flow_With_Update_Call_.yaml` | WORKBENCH · OPTIONAL |
| `flow.bus-vehicle-based-confirmation-without-update` | `IntraCity_Vehicle_Based_Confirmation_flow(Without Update Call)` | `IntraCity_Vehicle_Based_Confirmation_flow_Without_Update_Call_.yaml` | WORKBENCH · OPTIONAL |

### Metro — 29

| frame | flow id (config) | flow file | tags |
|---|---|---|---|
| `flow.metro-delayed-cancellation-accepted-technical` | `DELAYED_CANCELLATION_FLOW_ACCEPTED_IN_CASE_OF_TECHNICAL_CANCELLATION` | `DELAYED_CANCELLATION_FLOW_ACCEPTED.yaml` | WORKBENCH · MANDATORY · REPORTABLE |
| `flow.metro-delayed-cancellation-accepted-technical-wo-search-select` | `DELAYED_CANCELLATION_FLOW_ACCEPTED_IN_CASE_OF_TECHNICAL_CANCELLATION (W/O Search1 and Select)` | `DELAYED_CANCELLATION_FLOW_ACCEPTED__W_O_Search_and_Select_.yaml` | WORKBENCH · MANDATORY · REPORTABLE |
| `flow.metro-delayed-cancellation-accepted-user` | `DELAYED_CANCELLATION_FLOW_ACCEPTED_IN_CASE_OF_USER_CANCELLATION` | `DELAYED_CANCELLATION_FLOW_ACCEPTED_IN_CASE_OF_USER_CANCELLATION.yaml` | WORKBENCH · MANDATORY · REPORTABLE |
| `flow.metro-delayed-cancellation-accepted-user-wo-search-select` | `DELAYED_CANCELLATION_FLOW_ACCEPTED_IN_CASE_OF_USER_CANCELLATION (W/O Search1 and Select)` | `DELAYED_CANCELLATION_FLOW_ACCEPTED_IN_CASE_OF_USER_CANCELLATION__W_O_Search_and_Select_.yaml` | WORKBENCH · MANDATORY · REPORTABLE |
| `flow.metro-delayed-cancellation-rejected-technical` | `DELAYED_CANCELLATION_FLOW_REJECTED_IN_CASE_OF_TECHNICAL_CANCELLATION` | `DELAYED_CANCELLATION_FLOW_REJECTED.yaml` | WORKBENCH · MANDATORY · REPORTABLE |
| `flow.metro-delayed-cancellation-rejected-technical-wo-search-select` | `DELAYED_CANCELLATION_FLOW_REJECTED_IN_CASE_OF_TECHNICAL_CANCELLATION (W/O Search1 and Select)` | `DELAYED_CANCELLATION_FLOW_REJECTED__W_O_Search_and_Select_.yaml` | WORKBENCH · MANDATORY · REPORTABLE |
| `flow.metro-delayed-cancellation-rejected-user` | `DELAYED_CANCELLATION_FLOW_REJECTED_IN_CASE_OF_USER_CANCELLATION` | `DELAYED_CANCELLATION_FLOW_REJECTED_IN_CASE_OF_USER_CANCELLATION.yaml` | WORKBENCH · MANDATORY · REPORTABLE |
| `flow.metro-delayed-cancellation-rejected-user-wo-search-select` | `DELAYED_CANCELLATION_FLOW_REJECTED_IN_CASE_OF_USER_CANCELLATION (W/O Search1 and Select)` | `DELAYED_CANCELLATION_FLOW_REJECTED_IN_CASE_OF_USER_CANCELLATION__W_O_Search_and_Select_.yaml` | WORKBENCH · MANDATORY · REPORTABLE |
| `flow.metro-end-stop-update` | `END_STOP_UPDATE_FLOW` | `END_STOP_UPDATE_FLOW.yaml` | WORKBENCH · MANDATORY · REPORTABLE |
| `flow.metro-end-stop-update-wo-search-select` | `END_STOP_UPDATE_FLOW (W/O Search1 and Select)` | `END_STOP_UPDATE_FLOW__W_O_Search_and_Select_.yaml` | WORKBENCH · MANDATORY · REPORTABLE |
| `flow.metro-offline-cancellation` | `OFFLINE_CANCELLATION_FLOW` | `OFFLINE_CANCELLATION_FLOW.yaml` | WORKBENCH · MANDATORY · REPORTABLE |
| `flow.metro-offline-cancellation-wo-search-select` | `OFFLINE_CANCELLATION_FLOW (W/O Search1 and Select)` | `OFFLINE_CANCELLATION_FLOW_W_O_Search_and_Select.yaml` | WORKBENCH · MANDATORY · REPORTABLE |
| `flow.metro-partial-cancellation` | `PARTIAL_CANCELLATION_FLOW` | `PARTIAL_CANCELLATION_FLOW.yaml` | WORKBENCH · MANDATORY · REPORTABLE |
| `flow.metro-partial-cancellation-wo-search-select` | `PARTIAL_CANCELLATION_FLOW (W/O Search1 and Select)` | `PARTIAL_CANCELLATION_FLOW_W_O_Search_and_Select.yaml` | WORKBENCH · MANDATORY · REPORTABLE |
| `flow.metro-station-code-catalog` | `STATION_CODE_FLOW_CATALOG` | `STATION_CODE_FLOW_CATALOG.yaml` | WORKBENCH · MANDATORY · REPORTABLE |
| `flow.metro-station-code-order` | `STATION_CODE_FLOW_ORDER` | `STATION_CODE_FLOW_ORDER.yaml` | WORKBENCH · MANDATORY · REPORTABLE |
| `flow.metro-station-code-order-igm-no-action-v1` | `STATION_CODE_FLOW_ORDER_IGM_No_Action(v-1.0.0)` | `STATION_CODE_FLOW_ORDER_IGM_No_Action_v-1_0_0_.yaml` | WORKBENCH · MANDATORY · REPORTABLE |
| `flow.metro-station-code-order-igm-no-action-v1-wo-search-select` | `STATION_CODE_FLOW_ORDER_IGM_No_Action(v-1.0.0)(W/O Search1 and Select)` | `STATION_CODE_FLOW_ORDER_IGM_No_Action_v-1_0_0__W_O_Search_and_Select_.yaml` | WORKBENCH · MANDATORY · REPORTABLE |
| `flow.metro-station-code-order-igm-no-action-v2` | `STATION_CODE_FLOW_ORDER_IGM_No_Action(v-2.0.0)` | `STATION_CODE_FLOW_ORDER_IGM_No_Action_v-2_0_0_.yaml` | WORKBENCH · MANDATORY · REPORTABLE |
| `flow.metro-station-code-order-igm-no-action-v2-wo-search-select` | `STATION_CODE_FLOW_ORDER_IGM_No_Action(v-2.0.0)(W/O Search1 and Select)` | `STATION_CODE_FLOW_ORDER_IGM_No_Action_v-2_0_0__W_O_Search_and_Select_.yaml` | WORKBENCH · MANDATORY · REPORTABLE |
| `flow.metro-station-code-order-igm-rejection-v2` | `STATION_CODE_FLOW_ORDER_IGM_Rejection(v-2.0.0)` | `STATION_CODE_FLOW_ORDER_IGM_Rejection_v-2_0_0_.yaml` | WORKBENCH · MANDATORY · REPORTABLE |
| `flow.metro-station-code-order-igm-rejection-v2-wo-search-select` | `STATION_CODE_FLOW_ORDER_IGM_Rejection(v-2.0.0)(W/O Search1 and Select)` | `STATION_CODE_FLOW_ORDER_IGM_Rejection_v-2_0_0__W_O_Search_and_Select_.yaml` | WORKBENCH · MANDATORY · REPORTABLE |
| `flow.metro-station-code-order-igm-v2` | `STATION_CODE_FLOW_ORDER_IGM(v-2.0.0)` | `STATION_CODE_FLOW_ORDER_IGM_v-2_0_0_.yaml` | WORKBENCH · MANDATORY · REPORTABLE |
| `flow.metro-station-code-order-igm-v2-wo-search-select` | `STATION_CODE_FLOW_ORDER_IGM(v-2.0.0)(W/O Search1 and Select)` | `STATION_CODE_FLOW_ORDER_IGM_v-2_0_0__W_O_Search_and_Select_.yaml` | WORKBENCH · MANDATORY · REPORTABLE |
| `flow.metro-station-code-order-wo-search-select` | `STATION_CODE_FLOW_ORDER (W/O Search1 and Select)` | `STATION_CODE_FLOW_ORDER__W_O_Search_and_Select_.yaml` | WORKBENCH · MANDATORY · REPORTABLE |
| `flow.metro-technical-cancellation` | `TECHNICAL_CANCELLATION_FLOW` | `TECHNICAL_CANCELLATION_FLOW.yaml` | WORKBENCH · MANDATORY · REPORTABLE |
| `flow.metro-technical-cancellation-wo-search-select` | `TECHNICAL_CANCELLATION_FLOW (W/O Search1 and Select)` | `TECHNICAL_CANCELLATION_FLOW__W_O_Search_and_Select_.yaml` | WORKBENCH · MANDATORY · REPORTABLE |
| `flow.metro-user-cancellation` | `USER_CANCELLATION_FLOW` | `USER_CANCELLATION_FLOW.yaml` | WORKBENCH · MANDATORY · REPORTABLE |
| `flow.metro-user-cancellation-wo-search-select` | `USER_CANCELLATION_FLOW (W/O Search1 and Select)` | `USER_CANCELLATION_FLOW__W_O_Search_and_Select_.yaml` | WORKBENCH · MANDATORY · REPORTABLE |

`*-wo-search-select` frames are the `(W/O Search1 and Select)` variants — same journey entered at
`init` without a preceding `select`; see `anchor.wo-search-and-select-variant`.

## Actions covered — 17 / 17 in `actions/index.yaml`

Each action is an interned anchor with a `class` · `protocol` frame. Sequencing (`precedes`) and
ownership (`sent-by`) facts are atoms, not frame prose.

| frame | action | grounded at |
|---|---|---|
| `anchor.search` | `search` | `actions/index.yaml#supportedActions.search` |
| `anchor.on-search` | `on_search` | `actions/index.yaml#supportedActions.on_search` |
| `anchor.select` | `select` | `actions/index.yaml#supportedActions.select` |
| `anchor.on-select` | `on_select` | `actions/index.yaml#supportedActions.on_select` |
| `anchor.init` | `init` | `actions/index.yaml#supportedActions.init` |
| `anchor.on-init` | `on_init` | `actions/index.yaml#supportedActions.on_init` |
| `anchor.confirm` | `confirm` | `actions/index.yaml#supportedActions.confirm` |
| `anchor.on-confirm` | `on_confirm` | `actions/index.yaml#supportedActions.on_confirm` |
| `anchor.status` | `status` | `actions/index.yaml#supportedActions.status` |
| `anchor.on-status` | `on_status` | `actions/index.yaml#supportedActions.on_status` |
| `anchor.cancel` | `cancel` | `actions/index.yaml#supportedActions.cancel` |
| `anchor.on-cancel` | `on_cancel` | `actions/index.yaml#supportedActions.on_cancel` |
| `anchor.update` | `update` | `actions/index.yaml#supportedActions.update` |
| `anchor.on-update` | `on_update` | `actions/index.yaml#supportedActions.on_update` |
| `anchor.issue` | `issue` | `actions/index.yaml#supportedActions.issue` |
| `anchor.on-issue` | `on_issue` | `actions/index.yaml#supportedActions.on_issue` |
| `anchor.on-issue-status` | `on_issue_status` | `actions/index.yaml#supportedActions.on_issue_status` |

Parent class: `anchor.action` — grounded at `actions/index.yaml#supportedActions`.
Successor sets per action live at `actions/index.yaml#supportedActions.<action>`; async pairing and
transaction partners at `actions/index.yaml#apiProperties.<action>`.

## Concepts

| frame | layer | grounded at |
|---|---|---|
| `trv11` | domain | `index.yaml#info.domain` |
| `trv11.bus` | domain | `index.yaml#info.x-usecases` |
| `trv11.metro` | domain | `index.yaml#info.x-usecases` |
| `anchor.purchase-journey` | domain | `flows/index.yaml#flows[IntraCity_Purchase_Journey_Flow_Code_Based].description` |
| `anchor.cancellation-journey` | domain | `flows/index.yaml#flows[USER_CANCELLATION_FLOW].description` |
| `anchor.igm-journey` | domain | `flows/index.yaml#flows[STATION_CODE_FLOW_ORDER_IGM(v-2.0.0)].description` |
| `anchor.igm-v1` | domain | `validations/index.yaml#_TESTS_.issue[ISSUE_VALIDATION_VERSION_100]` |
| `anchor.igm-v2` | domain | `validations/index.yaml#_TESTS_.issue[ISSUE_VALIDATION_VERSION_200]` |
| `anchor.mandatory-flow` | domain | `flows/index.yaml#flows[USER_CANCELLATION_FLOW].tags` |
| `anchor.wo-search-and-select-variant` | domain | `flows/Metro/USER_CANCELLATION_FLOW__W_O_Search_and_Select_.yaml#steps[init_without_select_METRO_201]` |
| `anchor.soft-cancel` | domain | `flows/Metro/USER_CANCELLATION_FLOW.yaml#steps[cancel_soft_METRO_201].mock.defaultPayload.message.descriptor.code` |
| `anchor.bap` | protocol | `attributes/Bus.yaml#attribute_set.search.context.bap_id._description.owner` |
| `anchor.bpp` | protocol | `attributes/Bus.yaml#attribute_set.on_search.message.catalog._description.owner` |

28 of the 178 interned meanings carry a frame (the 17 actions, `anchor.action`, the two participant
roles, and the 8 recurring domain concepts above). The other 150 — enums, tag groups, field
semantics — are registry rows in `anchors/index.md` only: per `kb-format/anchor.md` an anchor does
not need a frame.

## Error codes — 18 / 18 in `errors/index.yaml`

| frame | code | event | raised by |
|---|---|---|---|
| `error.code-30001` | 30001 | Internal Error | BPP |
| `error.code-30008` | 30008 | Location unserviceable | BPP |
| `error.code-50001` | 50001 | Cancellation not possible | BPP |
| `error.code-91201` | 91201 | Route Serviceability error | BPP |
| `error.code-91202` | 91202 | Origin station not serviceable | BPP |
| `error.code-91203` | 91203 | Destination not serviceable | BPP |
| `error.code-91204` | 91204 | Maximum order qty exceeded | BPP |
| `error.code-91205` | 91205 | Tracking not enabled | BPP |
| `error.code-91206` | 91206 | Temporarily unavailable | BPP |
| `error.code-91207` | 91207 | Transaction failure | BPP |
| `error.code-91208` | 91208 | Out-of-operational hours | BPP |
| `error.code-91209` | 91209 | Error in retrieving the QR | BPP |
| `error.code-91210` | 91210 | Unable to get stations data | BPP |
| `error.code-91211` | 91211 | Fare fetch error | BPP |
| `error.code-91212` | 91212 | Invalid transaction | BPP |
| `error.code-91213` | 91213 | Stale transaction | BPP |
| `error.code-91214` | 91214 | Wrong fare while booking ticket | BPP |
| `error.code-91215` | 91215 | Item not found | BPP |

## Docs

| frame | source |
|---|---|
| `docs.references` | `docs/references.md` |
| `docs.release-notes` | `docs/release-notes.md` |

`docs/overview.md` has no frame; it grounds atoms directly (`#summary`, `#real-world-actors`,
`#use-cases`, `#key-concepts`).

## Links

- `atoms.md` — the facts (structural block, then the `# --- Stage E candidate units ---` block)
- `anchors/index.md` — interned meanings: `| handle | meaning | grounded-in | asof |`
- `candidate-units.md` — Stage E output before merge; query `atoms.md` instead
- `frames/` — node files, bodies deliberately light
- `LOCATOR.md` — where do I find X
- `../../configs/release-eks-TRV11-2.0.1/config/` — Ground 0
- `../../.claude/skills/ondc-kb-seed/kb-format/` — the format contract
- `../../.claude/skills/ondc-kb/kb_query.py` — read-only query tool

## Validation

```
python3 .claude/skills/ondc-kb-seed/tools/validate_kb.py knowledge/trv11-2.0.1
```

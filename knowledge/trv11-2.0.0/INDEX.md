# INDEX — trv11-2.0.0

Navigation surface for the `trv11-2.0.0` KB book (ONDC:TRV11, config release
`configs/release-eks-TRV11-2.0.0/config`). Facts live in `atoms.md`; interned meanings live in
`anchors/index.md`; frames are light declared nodes. Nothing here asserts a fact that is not a
committed unit — this file is navigation only.

## Book

| field | value |
|---|---|
| book id | `trv11-2.0.0` |
| domain | `ONDC:TRV11` (`index.yaml#info.domain`) |
| use cases | Bus, Metro (`index.yaml#info.x-usecases`) |
| config root | `configs/release-eks-TRV11-2.0.0/config` |

## Counts

| surface | count | file |
|---|---|---|
| atoms | 686 | `atoms.md` |
| anchors | 160 | `anchors/index.md` |
| frames | 57 | `frames/*.md` |
| — flow frames (`kind: instance`, `layer: domain`) | 17 | `frames/flow.*.md` |
| — action frames (`kind: class`, `layer: protocol`) | 17 | `frames/action.*.md` |
| — concept frames (`kind: concept`, `layer: domain`) | 23 | `frames/dom.*.md`, `frames/usecase.*.md`, `frames/concept.*.md` |
| candidate units (not committed) | — | `candidate-units.md` |

Validator: `python3 .claude/skills/ondc-kb-seed/tools/validate_kb.py knowledge/trv11-2.0.0`

## Flows covered (17)

Grounded at `flows/index.yaml#flows[…]` and each flow file's `meta.flowId`. Flow classification
(`MANDATORY` / `OPTIONAL` / `REPORTABLE`) is read from `flows/index.yaml#flows[…].tags` — see
`LOCATOR.md`.

### Bus (4)

| frame | anchor handle | config file |
|---|---|---|
| `flow.bus-order-to-journey-completion` | `anchor.flow-bus-order-to-journey-completion` | `flows/Bus/ORDER_TO_CONFIRM_TO_JOURNEY_COMPLETION.yaml` |
| `flow.bus-station-code-catalog` | `anchor.flow-bus-station-code-catalog` | `flows/Bus/STATION_CODE_FLOW_CATALOG.yaml` |
| `flow.bus-technical-cancellation` | `anchor.flow-bus-technical-cancellation` | `flows/Bus/TECHNICAL_CANCELLATION_FLOW.yaml` |
| `flow.bus-user-cancellation` | `anchor.flow-bus-user-cancellation` | `flows/Bus/USER_CANCELLATION_FLOW.yaml` |

### Metro (13)

| frame | anchor handle | config file |
|---|---|---|
| `flow.metro-station-code-catalog` | `anchor.flow-metro-station-code-catalog` | `flows/Metro/STATION_CODE_FLOW_CATALOG.yaml` |
| `flow.metro-sjt-purchase` | `anchor.flow-metro-sjt-purchase` | `flows/Metro/ORDER_TO_CONFIRM_TO_JOURNEY_COMPLETION_SJT.yaml` |
| `flow.metro-rjt-purchase` | `anchor.flow-metro-rjt-purchase` | `flows/Metro/ORDER_TO_CONFIRM_TO_JOURNEY_COMPLETION_RJT.yaml` |
| `flow.metro-sjt-purchase-direct-init` | `anchor.flow-metro-sjt-purchase-direct-init` | `flows/Metro/ORDER_TO_CONFIRM_TO_JOURNEY_COMPLETION_SJT_WITHOUT_SEARCH_ND_SELECT.yaml` |
| `flow.metro-rjt-purchase-direct-init` | `anchor.flow-metro-rjt-purchase-direct-init` | `flows/Metro/ORDER_TO_CONFIRM_TO_JOURNEY_COMPLETION_RJT_WITHOUT_SEARCH_ND_SELECT.yaml` |
| `flow.metro-sjt-purchase-with-igm` | `anchor.flow-metro-sjt-purchase-with-igm` | `flows/Metro/ORDER_TO_CONFIRM_TO_JOURNEY_COMPLETION_SJT_WITHOUT_SEARCH_ND_SELECT_WITH_IGM_1_0_0.yaml` |
| `flow.metro-user-cancellation` | `anchor.flow-metro-user-cancellation` | `flows/Metro/USER_CANCELLATION_FLOW.yaml` |
| `flow.metro-user-cancellation-direct-init` | `anchor.flow-metro-user-cancellation-direct-init` | `flows/Metro/USER_CANCELLATION_FLOW_WITHOUT_SEARCH_ND_SELECT.yaml` |
| `flow.metro-technical-cancellation` | `anchor.flow-metro-technical-cancellation` | `flows/Metro/TECHNICAL_CANCELLATION_FLOW.yaml` |
| `flow.metro-technical-cancellation-direct-init` | `anchor.flow-metro-technical-cancellation-direct-init` | `flows/Metro/TECHNICAL_CANCELLATION_FLOW_WITHOUT_SEARCH_ND_SELECT.yaml` |
| `flow.metro-partial-cancellation` | `anchor.flow-metro-partial-cancellation` | `flows/Metro/PARTIAL_CANCELLATION_FLOW.yaml` |
| `flow.metro-partial-cancellation-direct-init` | `anchor.flow-metro-partial-cancellation-direct-init` | `flows/Metro/PARTIAL_CANCELLATION_FLOW_WITHOUT_SEARCH_ND_SELECT.yaml` |
| `flow.metro-seller-offline-cancellation` | `anchor.flow-metro-seller-offline-cancellation` | `flows/Metro/SELLER_OFFLINE_CANCELLATION_WITHOUT_SEARCH_ND_SELECT.yaml` |

## Actions covered (17)

All grounded at `actions/index.yaml#supportedActions.<action>`; ordering constraints at
`actions/index.yaml#apiProperties.<action>`.

| frame | action | anchor handle |
|---|---|---|
| `action.search` | `search` | `anchor.search` |
| `action.on-search` | `on_search` | `anchor.on-search` |
| `action.select` | `select` | `anchor.select` |
| `action.on-select` | `on_select` | `anchor.on-select` |
| `action.init` | `init` | `anchor.init` |
| `action.on-init` | `on_init` | `anchor.on-init` |
| `action.confirm` | `confirm` | `anchor.confirm` |
| `action.on-confirm` | `on_confirm` | `anchor.on-confirm` |
| `action.status` | `status` | `anchor.status` |
| `action.on-status` | `on_status` | `anchor.on-status` |
| `action.cancel` | `cancel` | `anchor.cancel` |
| `action.on-cancel` | `on_cancel` | `anchor.on-cancel` |
| `action.update` | `update` | `anchor.update` |
| `action.on-update` | `on_update` | `anchor.on-update` |
| `action.issue` | `issue` | `anchor.issue` |
| `action.on-issue` | `on_issue` | `anchor.on-issue` |
| `action.on-issue-status` | `on_issue_status` | `anchor.on-issue-status` |

Actions present in `specs/openapi.yaml#paths` but **not** in `supportedActions` (`track`,
`on_track`, `rating`, `on_rating`, `support`, `on_support`, `issue_status`) are recorded in
`atoms.md` under `anchor.unsupported-action`; they have no frame.

## Concepts (23)

| frame | anchor handle |
|---|---|
| `dom.trv11` | `anchor.trv11` |
| `usecase.metro` | `anchor.usecase-metro` |
| `usecase.bus` | `anchor.usecase-bus` |
| `concept.mandatory-flow` | `anchor.mandatory-flow` |
| `concept.optional-flow` | `anchor.optional-flow` |
| `concept.reportable-flow` | `anchor.reportable-flow` |
| `concept.ticket-type-code` | `anchor.ticket-type-code` |
| `concept.vehicle-category` | `anchor.vehicle-category` |
| `concept.fulfillment-type` | `anchor.fulfillment-type` |
| `concept.station-code` | `anchor.station-code` |
| `concept.station-code-catalog` | `anchor.station-code-catalog` |
| `concept.search-catalog-discovery` | `anchor.search-catalog-discovery` |
| `concept.search-fare-discovery` | `anchor.search-fare-discovery` |
| `concept.init-with-user-input` | `anchor.init-with-user-input` |
| `concept.qr-ticket` | `anchor.qr-ticket` |
| `concept.order-status` | `anchor.order-status` |
| `concept.soft-cancel` | `anchor.soft-cancel` |
| `concept.confirm-cancel` | `anchor.confirm-cancel` |
| `concept.technical-cancellation` | `anchor.technical-cancellation` |
| `concept.partial-cancellation` | `anchor.partial-cancellation` |
| `concept.seller-offline-cancellation` | `anchor.seller-offline-cancellation` |
| `concept.igm-1-0-0` | `anchor.igm-1-0-0` |
| `concept.igm-2-0-0` | `anchor.igm-2-0-0` |

Error codes (`anchor.error-30001` … `anchor.error-91216`), Beckn schema objects
(`anchor.provider`, `anchor.item`, …), enum sets and tag families are **anchors, not frames** —
per `kb-format/anchor.md` an anchor is a registry row plus units, and does not require a frame.
Look them up in `anchors/index.md`.

## Links

| file | what it holds |
|---|---|
| `atoms.md` | every committed unit (the only fact surface) |
| `anchors/index.md` | interned-meaning registry: handle → meaning → config ground → asof |
| `frames/` | 57 declared nodes (flows · actions · concepts) |
| `candidate-units.md` | Stage E candidates, **not** committed |
| `LOCATOR.md` | "where do I find X" table |
| `../trv11-2.0.1/`, `../trv11-2.1.0/` | later TRV11 books (separate `asof`; no cross-version inference) |
| `.claude/skills/ondc-kb-seed/kb-format/` | the format contract (`unit` · `anchor` · `vocabularies` · `invariants`) |

## Known gaps

- `flows/Metro/SELLER_OFFLINE_CANCELLATION_WITHOUT_SEARCH_ND_SELECT.yaml` carries a `responseFor`
  pointing at `cancel_hard_METRO_200`, a step that does not exist in that flow. `atoms.md` records
  this as `anchor.seller-offline-cancellation | requires | "cancel_hard_METRO_200"` flagged
  `!untethered`; no frame asserts that edge.
- A handful of units carry `!untethered` for schema slots not resolvable in
  `specs/openapi.yaml` (`anchor.tag1`, `error-object.type`, `error-object.tags`,
  `form.multiple_sumbissions`). See `grep '!untethered' atoms.md`.

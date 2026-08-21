# trv10-2.1.0 — KB index

Navigation surface for the `trv10-2.1.0` book (invariant 18). Counts are of committed
storage, not of derived views.

| field | value |
|---|---|
| book id | `trv10-2.1.0` |
| domain | `ONDC:TRV10` (`index.yaml#info.domain`) |
| version | `2.1.0` (`index.yaml#info.version`) |
| usecase | `Ride-hailing` (`index.yaml#info.x-usecases`) |
| config release | `configs/release-eks-TRV10-2.1.0/config/` |
| atoms | 785 (`atoms.md`) |
| anchors | 341 (`anchors/index.md`) |
| frames | 86 (`frames/*.md`) |
| ADRs | 0 |
| flows covered | 27 of 27 in `flows/index.yaml` |
| actions covered | 19 of 19 in `actions/index.yaml` |
| error codes | 3 (`errors/index.yaml`) — not framed; carried as atoms + anchors |

## Files

| file | what it holds |
|---|---|
| [`atoms.md`](atoms.md) | the committed units — every fact of this book |
| [`anchors/index.md`](anchors/index.md) | interned schematic meanings, handle → meaning → config ground |
| [`frames/`](frames/) | 86 declared nodes (flows, protocol actions, ride-hailing concepts) |
| [`candidate-units.md`](candidate-units.md) | Stage E working buffer — not committed fact |
| [`LOCATOR.md`](LOCATOR.md) | "where do I find X" |

## Frames by kind

| kind · layer | count | id prefix |
|---|---|---|
| `instance` · `domain` | 27 | `flow.*` |
| `class` · `protocol` | 19 | `action.*` |
| `concept` · `domain` | 40 | `dom.trv10`, `usecase.ride-hailing`, `concept.*` |

An anchor does **not** get a frame ([anchor.md](../../.claude/skills/ondc-kb-seed/kb-format/anchor.md));
the 341 anchors live as registry rows only.

## Flows covered (27)

Every flow in `flows/index.yaml` has a frame grounded at its own
`flows/Ride-hailing/<file>.yaml#meta.flowId`.

| frame | flow id | tags |
|---|---|---|
| `flow.driver-not-found-on-onconfirm` | `Driver_not_found_on_onconfirm` | MANDATORY · ON_DEMAND |
| `flow.driver-not-found-post-onconfirm` | `Driver_not_found_post_onconfirm` | MANDATORY · ON_DEMAND |
| `flow.no-acceptance-softcancel` | `No_Acceptance_SoftCancel` | OPTIONAL · ON_DEMAND · CANCELLATION |
| `flow.no-acceptance-softupdate` | `No_Acceptance_SoftUpdate` | OPTIONAL · ON_DEMAND |
| `flow.ondemand-assign-driver-on-onconfirm` | `OnDemand_Assign_driver_on_onconfirm` | MANDATORY · ON_DEMAND |
| `flow.ondemand-assign-driver-on-onconfirm-add-ons` | `OnDemand_Assign_driver_on_onconfirm_Add_Ons` | OPTIONAL · ON_DEMAND |
| `flow.ondemand-assign-driver-on-onconfirm-bap-collecting` | `OnDemand_Assign_driver_on_onconfirm_BAP_Collecting` | OPTIONAL · ON_DEMAND |
| `flow.ondemand-assign-driver-on-onconfirm-bap-collecting-pre-order` | `OnDemand_Assign_driver_on_onconfirm_BAP_Collecting_Pre_Order` | OPTIONAL · ON_DEMAND |
| `flow.ondemand-assign-driver-on-onconfirm-bap-collecting-quote-update` | `OnDemand_Assign_driver_on_onconfirm_BAP_Collecting_Quote_Update` | OPTIONAL · ON_DEMAND |
| `flow.ondemand-assign-driver-on-onconfirm-with-igm-v-1-0-0` | `OnDemand_Assign_driver_on_onconfirm_With_IGM(v-1.0.0)` | MANDATORY · ON_DEMAND |
| `flow.ondemand-assign-driver-on-onconfirm-with-igm-v-2-0-0` | `OnDemand_Assign_driver_on_onconfirm_With_IGM(v-2.0.0)` | OPTIONAL · ON_DEMAND |
| `flow.ondemand-assign-driver-on-onconfirm-with-igm-no-action-v-2-0-0` | `OnDemand_Assign_driver_on_onconfirm_With_IGM_No_Action(v-2.0.0)` | OPTIONAL · ON_DEMAND |
| `flow.ondemand-assign-driver-on-onconfirm-with-igm-rejection-v-2-0-0` | `OnDemand_Assign_driver_on_onconfirm_With_IGM_Rejection(v-2.0.0)` | OPTIONAL · ON_DEMAND |
| `flow.ondemand-assign-driver-post-on-confirm` | `OnDemand_Assign_driver_post_on_ confirm` | MANDATORY · ON_DEMAND |
| `flow.ondemand-assign-driver-post-onconfirmselfpickup` | `OnDemand_Assign_driver_post_onconfirmSelfPickup` | OPTIONAL · ON_DEMAND |
| `flow.ondemand-post-order-tip` | `OnDemand_Post_Order_Tip` | OPTIONAL · ON_DEMAND |
| `flow.ondemand-pre-order-bid` | `OnDemand_Pre_Order_Bid` | OPTIONAL · ON_DEMAND |
| `flow.ondemand-purple-tags-assign-driver-on-onconfirm` | `OnDemand_Purple_Tags_Assign_driver_on_onconfirm` | OPTIONAL · ON_DEMAND |
| `flow.ondemand-rental` | `OnDemand_Rental` | OPTIONAL · ON_DEMAND · RENTAL |
| `flow.ondemand-rentalwhen-end-stop-gps-coordinate-is-present` | `OnDemand_Rentalwhen_end_stop_gps_coordinate_is_present` | OPTIONAL · ON_DEMAND · RENTAL |
| `flow.ondemand-ride-technical-cancellation-flow` | `OnDemand_Ride_Technical_Cancellation_Flow` | MANDATORY · ON_DEMAND · CANCELLATION |
| `flow.ondemand-ride-cancellation-by-driver` | `OnDemand_Ride_cancellation_by_driver` | MANDATORY · ON_DEMAND · CANCELLATION |
| `flow.ondemand-ride-cancellation-by-rider` | `OnDemand_Ride_cancellation_by_rider` | MANDATORY · ON_DEMAND · CANCELLATION |
| `flow.ondemand-ride-with-multiple-stops` | `OnDemand_Ride_with_multiple_stops` | OPTIONAL · ON_DEMAND |
| `flow.ondemand-update-stop` | `OnDemand_Update_Stop` | OPTIONAL · ON_DEMAND |
| `flow.schedule-rental` | `Schedule_Rental` | OPTIONAL · SCHEDULED · RENTAL |
| `flow.schedule-trip` | `Schedule_Trip` | OPTIONAL · SCHEDULED |

All 27 are tagged `REPORTABLE`; 8 `MANDATORY` / 19 `OPTIONAL`.

## Actions covered (19)

Every key of `actions/index.yaml#supportedActions` has a frame
(`kind: class`, `layer: protocol`), grounded at `#supportedActions.<action>`.

| BAP-side | BPP-side |
|---|---|
| `action.search` · `action.select` · `action.init` · `action.confirm` · `action.status` · `action.track` · `action.cancel` · `action.update` · `action.issue` | `action.on-search` · `action.on-select` · `action.on-init` · `action.on-confirm` · `action.on-status` · `action.on-track` · `action.on-cancel` · `action.on-update` · `action.on-issue` · `action.on-issue-status` |

The transaction entry point is `search` (`supportedActions."null"`); the
`precedes` chain lives in `atoms.md`, not here.

## Ride-hailing concepts (40)

`dom.trv10` · `usecase.ride-hailing` · `concept.rider` · `concept.driver` ·
`concept.network-interoperability` · `concept.ride-lifecycle` · `concept.driver-assignment` ·
`concept.on-demand-ride` · `concept.scheduled-ride` · `concept.rental-ride` ·
`concept.ride-state` · `concept.order-status` · `concept.trip-category` ·
`concept.vehicle-category` · `concept.fulfillment-type` · `concept.stop-type` ·
`concept.stop-authorization` · `concept.payment-collector` · `concept.payment-timing` ·
`concept.cancellation-term` · `concept.cancellation-reason` · `concept.route-info` ·
`concept.quote-breakup` · `concept.add-on` · `concept.update-target` ·
`concept.multi-stop-journey` · `concept.tracking-status` · `concept.settlement-terms` ·
`concept.buyer-finder-fees` · `concept.purple-tag` · `concept.self-pickup` ·
`concept.post-order-tip` · `concept.pre-order-bid` · `concept.broadcast-discovery` ·
`concept.soft-cancel` · `concept.hard-cancel` · `concept.soft-update` ·
`concept.technical-cancellation` · `concept.bap-collected-settlement` · `concept.igm`

## Grounding spread (atoms)

| config file | atoms grounded there |
|---|---|
| `validations/index.yaml` | 340 |
| `attributes/Ride_hailing.yaml` | 118 |
| `flows/Ride-hailing/*.yaml` | 114 |
| `flows/index.yaml` | 92 |
| `actions/index.yaml` | 78 |
| `errors/index.yaml` | 10 |
| `docs/overview.md` | 7 |
| `index.yaml` | 4 |
| `specs/openapi.yaml` | 2 |
| `workbench:*` (reference) | 16 |

`basis` spread: 761 `declared` · 13 `authority` · 6 `observed-live` · 3 `sandbox-tested` ·
1 `derived` · 1 `inferred`.

## Out of scope

`attributes/Ride-hailing.yaml` (hyphen twin of `attributes/Ride_hailing.yaml`) is an
orphan — not referenced from `attributes/index.yaml`. Nothing in this book is framed or
grounded against it.

## Related books

`trv10-2.0.1` is the predecessor baseline (`anchor.trv10-ride-hailing | wasRevisionOf |
anchor.trv10-2-0-1`). Cross-version inference is not permitted — each unit is timeless for
its own `asof` (invariant 15).

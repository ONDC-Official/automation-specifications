# INDEX — trv10-2.0.1

Navigation surface for the `trv10-2.0.1` book (invariant 18). Facts live in `atoms.md`;
this file only tells you what is in the book and where to go next.

| field | value |
|---|---|
| book id | `trv10-2.0.1` |
| domain | `ONDC:TRV10` (ride-hailing / on-demand mobility) |
| spec version | `2.0.1` |
| config root | `configs/release-eks-TRV10-2.0.1/config/` |
| atoms | 851 (35 structural + 816 Stage E) — `atoms.md` |
| anchors | 287 — `anchors/index.md` |
| frames | 45 — `frames/*.md` |
| ADRs | 0 |

## Frames by kind

| kind | layer | count | id prefix |
|---|---|---|---|
| `instance` | `domain` | 11 | `flow.*` — one per flow in `flows/index.yaml` |
| `class` | `protocol` | 19 | `action.*` — one per `supportedActions` key |
| `concept` | `domain` | 15 | `dom.trv10`, `usecase.ride-hailing`, `concept.*` |

## Flows covered (11)

All 11 flows sit under the single use case `Ride-hailing` and are typed `playground`.
Each frame is grounded at its flow file's `meta.flowId`; the matching registry anchor
`anchor.flow-<same-tail>` is grounded at `flows/index.yaml#flows[<flowId>]`.

| frame | config `flowId` | flow file |
|---|---|---|
| `flow.driver-not-found-on-onconfirm` | `Driver_not_found_on_onconfirm` | `flows/Ride-hailing/Driver_not_found_on_onconfirm.yaml` |
| `flow.driver-not-found-post-onconfirm` | `Driver_not_found_post_onconfirm` | `flows/Ride-hailing/Driver_not_found_post_onconfirm.yaml` |
| `flow.ondemand-assign-driver-on-onconfirm` | `OnDemand_Assign_driver_on_onconfirm` | `flows/Ride-hailing/OnDemand_Assign_driver_on_onconfirm.yaml` |
| `flow.ondemand-assign-driver-on-onconfirm-with-igm-1-0-0` | `OnDemand_Assign_driver_on_onconfirm_with_IGM(1.0.0)` | `flows/Ride-hailing/OnDemand_Assign_driver_on_onconfirm_with_IGM_1_0_0_.yaml` |
| `flow.ondemand-assign-driver-post-onconfirm` | `OnDemand_Assign_driver_post_onconfirm` | `flows/Ride-hailing/OnDemand_Assign_driver_post_onconfirm.yaml` |
| `flow.ondemand-assign-driver-post-onconfirmselfpickup` | `OnDemand_Assign_driver_post_onconfirmSelfPickup` | `flows/Ride-hailing/OnDemand_Assign_driver_post_onconfirmSelfPickup.yaml` |
| `flow.ondemand-female-driver-flow` | `OnDemand_Female_driver_flow` | `flows/Ride-hailing/OnDemand_Female_driver_flow.yaml` |
| `flow.ondemand-journey-updation-flow` | `OnDemand_journey_updation_flow` | `flows/Ride-hailing/OnDemand_journey_updation_flow.yaml` |
| `flow.ondemand-ride-cancellation-by-driver` | `OnDemand_Ride_cancellation_by_driver` | `flows/Ride-hailing/OnDemand_Ride_cancellation_by_driver.yaml` |
| `flow.ondemand-ride-cancellation-by-rider` | `OnDemand_Ride_cancellation_by_rider` | `flows/Ride-hailing/OnDemand_Ride_cancellation_by_rider.yaml` |
| `flow.technical-cancellation-flow` | `Technical_cancellation_flow` | `flows/Ride-hailing/Technical_cancellation_flow.yaml` |

## Actions covered (19)

One `action.*` frame per key of `actions/index.yaml#supportedActions`. Kebab id ↔ snake
config key (`action.on-issue-status` ↔ `on_issue_status`). Eighteen of the nineteen appear
as `steps[].api` in at least one flow; `update` is declared as a supported action and in
`apiProperties` but is exercised by no flow file in this release.

| discovery | ordering | fulfilment | post-order | grievance |
|---|---|---|---|---|
| `action.search` | `action.select` | `action.confirm` | `action.status` | `action.issue` |
| `action.on-search` | `action.on-select` | `action.on-confirm` | `action.on-status` | `action.on-issue` |
| | `action.init` | `action.track` | `action.update` | `action.on-issue-status` |
| | `action.on-init` | `action.on-track` | `action.on-update` | |
| | | | `action.cancel` | |
| | | | `action.on-cancel` | |

## Concept frames (15)

`dom.trv10` · `usecase.ride-hailing` · `concept.rider` · `concept.driver` ·
`concept.ride-hailing-provider` · `concept.on-demand-matching` · `concept.driver-assignment` ·
`concept.multi-provider-discovery` · `concept.live-tracking` · `concept.journey-progress` ·
`concept.ride-cancellation` · `concept.technical-cancellation` ·
`concept.female-driver-preference` · `concept.self-pickup` · `concept.igm`

## Links

| target | path |
|---|---|
| atoms (the only committed fact store) | [`atoms.md`](atoms.md) |
| anchor registry | [`anchors/index.md`](anchors/index.md) |
| frames | [`frames/`](frames/) |
| where-do-I-find-X | [`LOCATOR.md`](LOCATOR.md) |
| pre-promotion units | [`candidate-units.md`](candidate-units.md) |
| KB-storage contract | `.claude/skills/ondc-kb-seed/kb-format/` |
| validator | `.claude/skills/ondc-kb-seed/tools/validate_kb.py` |

## Scope notes

- `attributes/Ride-hailing.yaml` (hyphen twin) is an **orphan** — not referenced by
  `attributes/index.yaml`, which `$ref`s only `./Ride_hailing.yaml`. It is out of scope: no
  frame is grounded at it.
- The book carries no `decisions/`, `references/`, or `golden/` directories.

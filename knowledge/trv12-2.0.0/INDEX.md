# INDEX — trv12-2.0.0

Navigation surface for the `trv12-2.0.0` book (invariant 18). Committed and hand-maintained.

| field | value |
|---|---|
| book id | `trv12-2.0.0` |
| domain | `ONDC:TRV12` — intercity public transport (airlines + intercity buses) |
| spec version | `2.0.0` |
| config release | `configs/release-eks-TRV12-2.0.0/config/` |
| atoms | 739 |
| anchors | 239 |
| frames | 57 |
| ADRs | 0 |

## Files

| file | what it holds |
|---|---|
| [`atoms.md`](atoms.md) | every committed unit — the only fact-truth in this book |
| [`anchors/index.md`](anchors/index.md) | the interned-meaning registry: handle → canonical meaning → config ground |
| [`frames/`](frames/) | light declared nodes (flows, actions, recurring concepts) — no facts, pointers only |
| [`candidate-units.md`](candidate-units.md) | staging buffer; **not** committed fact |
| [`LOCATOR.md`](LOCATOR.md) | "where do I find X" lookup |

## Use cases covered

| use case | frame | attribute dictionary |
|---|---|---|
| Airline | [`usecase.airline`](frames/usecase.airline.md) | `attributes/Airline.yaml#attribute_set` |
| Intercity (Bus) | [`usecase.intercity`](frames/usecase.intercity.md) | `attributes/Intercity.yaml#attribute_set` |

## Flows covered (15)

All grounded at `trv12-2.0.0:flows/index.yaml#flows[<id>]`.

### Airline (6)

| frame | config flow id |
|---|---|
| [`flow.airline-pagination`](frames/flow.airline-pagination.md) | `Airlines - Seller App Pagination Flow` |
| [`flow.airline-purchase`](frames/flow.airline-purchase.md) | `Purchase Journey(Code Based Flow)` |
| [`flow.airline-purchase-igm`](frames/flow.airline-purchase-igm.md) | `Purchase Journey(Code Based Flow)_WITH_IGM(v-1.0.0)` |
| [`flow.airline-multi-ticket`](frames/flow.airline-multi-ticket.md) | `Purchase Journey(Multiple Tickets)` |
| [`flow.airline-cancel-buyer`](frames/flow.airline-cancel-buyer.md) | `Cancellation by Buyer` |
| [`flow.airline-cancel-seller`](frames/flow.airline-cancel-seller.md) | `Cancellation by Seller` |

### Intercity / Bus (9)

| frame | config flow id |
|---|---|
| [`flow.bus-station-code`](frames/flow.bus-station-code.md) | `Intercity(Bus)_Station_Code_Based_Flow` |
| [`flow.bus-station-code-multi`](frames/flow.bus-station-code-multi.md) | `Intercity(Bus)_Station_Code_Based_Flow_Multiple_Tickets` |
| [`flow.bus-station-code-igm`](frames/flow.bus-station-code-igm.md) | `Intercity(Bus)_Station_Code_Based_Flow_WITH_IGM(v-1.0.0)` |
| [`flow.bus-cancel-buyer`](frames/flow.bus-cancel-buyer.md) | `Intercity(Bus)_Cancel_Flow(Buyer)` |
| [`flow.bus-cancel-seller`](frames/flow.bus-cancel-seller.md) | `Intercity(Bus)_Seller_Cancellation` |
| [`flow.bus-partial-cancel`](frames/flow.bus-partial-cancel.md) | `Intercity(Bus)_Partial_Cancellation_Flow` |
| [`flow.bus-soft-lock-error`](frames/flow.bus-soft-lock-error.md) | `Intercity(Bus)_Error_Response(Soft Locking Time)` |
| [`flow.bus-rating-success`](frames/flow.bus-rating-success.md) | `Intercity(Bus)_Rating(Success)` |
| [`flow.bus-rating-error`](frames/flow.bus-rating-error.md) | `Intercity(Bus)_Rating(Error Flow)` |

## Actions covered (21)

All grounded at `trv12-2.0.0:actions/index.yaml#supportedActions.<action>`; successor sets and
`apiProperties` (async predecessor, transaction partners) are recorded as units in `atoms.md`.

| pair | request frame | callback frame |
|---|---|---|
| discovery | [`action.search`](frames/action.search.md) | [`action.on-search`](frames/action.on-search.md) |
| selection | [`action.select`](frames/action.select.md) | [`action.on-select`](frames/action.on-select.md) |
| initialisation | [`action.init`](frames/action.init.md) | [`action.on-init`](frames/action.on-init.md) |
| confirmation | [`action.confirm`](frames/action.confirm.md) | [`action.on-confirm`](frames/action.on-confirm.md) |
| status | [`action.status`](frames/action.status.md) | [`action.on-status`](frames/action.on-status.md) |
| cancellation | [`action.cancel`](frames/action.cancel.md) | [`action.on-cancel`](frames/action.on-cancel.md) |
| amendment | [`action.update`](frames/action.update.md) | [`action.on-update`](frames/action.on-update.md) |
| tracking | [`action.track`](frames/action.track.md) | [`action.on-track`](frames/action.on-track.md) |
| rating | [`action.rating`](frames/action.rating.md) | [`action.on-rating`](frames/action.on-rating.md) |
| grievance | [`action.issue`](frames/action.issue.md) | [`action.on-issue`](frames/action.on-issue.md), [`action.on-issue-status`](frames/action.on-issue-status.md) |

The `null` key of `supportedActions` (transaction entry / re-entry) is framed as
[`concept.transaction-reentry`](frames/concept.transaction-reentry.md), not as an action.

## Concept frames (20)

| frame | layer |
|---|---|
| [`dom.trv12`](frames/dom.trv12.md) | domain |
| [`usecase.airline`](frames/usecase.airline.md) · [`usecase.intercity`](frames/usecase.intercity.md) | domain |
| [`concept.multi-operator-aggregation`](frames/concept.multi-operator-aggregation.md) | domain |
| [`concept.code-based-discovery`](frames/concept.code-based-discovery.md) | domain |
| [`concept.station-code-discovery`](frames/concept.station-code-discovery.md) | domain |
| [`concept.catalog-pagination`](frames/concept.catalog-pagination.md) | domain |
| [`concept.two-phase-cancellation`](frames/concept.two-phase-cancellation.md) | domain |
| [`concept.buyer-cancellation`](frames/concept.buyer-cancellation.md) | domain |
| [`concept.seller-cancellation`](frames/concept.seller-cancellation.md) | domain |
| [`concept.partial-cancellation`](frames/concept.partial-cancellation.md) | domain |
| [`concept.soft-lock`](frames/concept.soft-lock.md) | domain |
| [`concept.soft-lock-expiry`](frames/concept.soft-lock-expiry.md) | domain |
| [`concept.seat-selection`](frames/concept.seat-selection.md) | domain |
| [`concept.multi-ticket-order`](frames/concept.multi-ticket-order.md) | domain |
| [`concept.igm-resolution`](frames/concept.igm-resolution.md) | domain |
| [`concept.rating-acceptance`](frames/concept.rating-acceptance.md) · [`concept.rating-rejection`](frames/concept.rating-rejection.md) | domain |
| [`concept.transaction-reentry`](frames/concept.transaction-reentry.md) | protocol |
| [`concept.unsolicited-callback`](frames/concept.unsolicited-callback.md) | protocol |
| [`error.code-90203`](frames/error.code-90203.md) | domain |

## Notes for readers

- Frames are **light**: a declaration plus a `Grounded at` pointer. They assert nothing; every fact
  is a unit in `atoms.md`.
- Anchors do **not** get a frame by default — look them up in `anchors/index.md`.
- `errors/index.yaml#code` is an empty list in this release, so the only error surface in the book
  is `90203`, observed in flow mocks and recorded as `not-part-of` the error registry.
- The soft-lock error path hangs off the confined subject `anchor.on-init-soft-lock-expired`, not
  off `anchor.on-init` itself — see [`concept.soft-lock-expiry`](frames/concept.soft-lock-expiry.md).

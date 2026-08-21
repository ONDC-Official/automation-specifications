# LOCATOR — trv12-2.0.0

"Where do I find X" for the `trv12-2.0.0` book (invariant 18). Committed and hand-maintained.

Config paths are relative to `configs/release-eks-TRV12-2.0.0/config/` and are written in the
`grounded-in` form `trv12-2.0.0:<file>#<node-path>` — a **positional node path**, never a line
number.

## Start here

| I want… | Go to |
|---|---|
| the shape of the book, counts, flow/action coverage | [`INDEX.md`](INDEX.md) |
| a **fact** (anything asserted) | [`atoms.md`](atoms.md) — the only fact-truth |
| what an `anchor.*` handle means and where it was interned | [`anchors/index.md`](anchors/index.md) |
| a declared node for a flow / action / concept | [`frames/`](frames/) |
| something not yet committed | [`candidate-units.md`](candidate-units.md) — staging, **not** fact |

## By question

| Question | KB lookup | Config ground |
|---|---|---|
| Which flows exist, and for which use case? | `grep 'anchor.flow-' atoms.md`; [`INDEX.md`](INDEX.md) flow tables | `flows/index.yaml#flows` |
| What steps does one flow run? | frame `flow.*` → its anchor handle in `atoms.md` | `flows/Airline/*.yaml#steps`, `flows/Intercity/*.yaml#steps` (step identity is `action_id`) |
| Which flows are Pramaan / mandatory / reportable? | `grep 'anchor.flow-tag-' atoms.md` | `flows/index.yaml#flows[<id>].tags` |
| Which actions exist and what may follow each? | `grep 'precedes' atoms.md`; frames `action.*` | `actions/index.yaml#supportedActions.<action>` |
| Which callback is paired to which request? | `grep 'requires\|wasInformedBy' atoms.md` | `actions/index.yaml#apiProperties.<action>.async_predecessor`, `…transaction_partner` |
| Where may a transaction (re-)enter? | frame [`concept.transaction-reentry`](frames/concept.transaction-reentry.md) | `actions/index.yaml#supportedActions.null` |
| Who sends an action — BAP or BPP? | `grep 'sent-by' atoms.md` | `flows/*/*.yaml#steps[<action_id>].owner` |
| Which callbacks arrive unsolicited? | frame [`concept.unsolicited-callback`](frames/concept.unsolicited-callback.md) | `flows/*/*.yaml#steps[<action_id>].unsolicited` |
| What fields are required on an action? | `grep '\-required' atoms.md`; anchors `anchor.*-required` | `validations/index.yaml#_TESTS_.<action>[<TEST>]._RETURN_` |
| What values may an enum take? | `grep 'anchor.enum-set' atoms.md` | `validations/index.yaml#_TESTS_.<action>[…].enumList` |
| What format must a code / timestamp match? | `grep 'anchor.regex-constraint' atoms.md` | `validations/index.yaml#_TESTS_.<action>[…].reg` |
| Which context fields are always required? | `grep 'anchor.context-required-fields' atoms.md` | `validations/index.yaml#_TESTS_.<action>[<ACTION>_CONTEXT]._RETURN_` |
| What does a field mean, who owns it, is it required? | `grep 'anchor.attribute-dictionary' atoms.md` | `attributes/Airline.yaml#attribute_set…_description`, `attributes/Intercity.yaml#attribute_set…_description` |
| Which use case does an attribute belong to? | `grep 'anchor.usecase-' atoms.md` | `attributes/<UseCase>.yaml#meta.use_case_id` |
| What is the request/response schema of an object? | `grep 'anchor.beckn-object' atoms.md` | `specs/openapi.yaml#components.schemas.<Schema>` |
| Which API paths are published? | `grep 'anchor.path-' atoms.md` | `specs/openapi.yaml#paths` |
| What error codes does the book register? | `grep 'anchor.trv12-error-registry' atoms.md` | `errors/index.yaml#code` — **empty list in this release** |
| Where does error `90203` come from? | frame [`error.code-90203`](frames/error.code-90203.md) | `flows/Intercity/Intercity_Bus__Error_Response_Soft_Locking_Time_.yaml#steps[on_init_BUS_221].mock.defaultPayload.error.code` |

## By subject area

| Subject | Frames | Anchor handles to grep | Config ground |
|---|---|---|---|
| Domain identity & purpose | [`dom.trv12`](frames/dom.trv12.md), [`concept.multi-operator-aggregation`](frames/concept.multi-operator-aggregation.md) | `anchor.trv12`, `anchor.intercity-transport-domain` | `index.yaml#info.domain`, `docs/overview.md#sector-purpose` |
| Use-case split (Airline vs Intercity) | [`usecase.airline`](frames/usecase.airline.md), [`usecase.intercity`](frames/usecase.intercity.md) | `anchor.usecase-airline`, `anchor.usecase-intercity`, `anchor.vehicle-category` | `validations/index.yaml#_TESTS_.search[AIRLINE_VALIDATION]._SCOPE_`, `…search[BUS_VALIDATION]._SCOPE_` |
| Code-based discovery | [`concept.code-based-discovery`](frames/concept.code-based-discovery.md), [`concept.station-code-discovery`](frames/concept.station-code-discovery.md) | `anchor.station-code`, `anchor.airport-code`, `anchor.search-round-origin/-route/-segment` | `docs/overview.md#key-concepts`; `flows/Intercity/Intercity_Bus__Station_Code_Based_Flow.yaml#steps[search_BUS_202].mock.defaultPayload.message.intent.fulfillment.stops` |
| Catalog pagination (Airline) | [`concept.catalog-pagination`](frames/concept.catalog-pagination.md) | `anchor.pagination-tag-group`, `anchor.current-page-number`, `anchor.max-page-number` | `flows/Airline/Airlines_-_Seller_App_Pagination_Flow.yaml#steps[on_search_1_Airline_200].mock.defaultPayload.message.catalog.tags` |
| Seat selection & soft lock (Intercity) | [`concept.seat-selection`](frames/concept.seat-selection.md), [`concept.soft-lock`](frames/concept.soft-lock.md), [`concept.soft-lock-expiry`](frames/concept.soft-lock-expiry.md) | `anchor.seat-grid`, `anchor.soft-lock`, `anchor.soft-lock-expiry`, `anchor.on-init-soft-lock-expired` | `flows/Intercity/Intercity_Bus__Station_Code_Based_Flow.yaml#steps[on_select_BUS_202].description`; `flows/Intercity/Intercity_Bus__Error_Response_Soft_Locking_Time_.yaml#steps[on_init_BUS_221].description` |
| Cancellation (buyer / seller / partial) | [`concept.two-phase-cancellation`](frames/concept.two-phase-cancellation.md), [`concept.buyer-cancellation`](frames/concept.buyer-cancellation.md), [`concept.seller-cancellation`](frames/concept.seller-cancellation.md), [`concept.partial-cancellation`](frames/concept.partial-cancellation.md) | `anchor.soft-cancel`, `anchor.confirm-cancel`, `anchor.cancelled-by-consumer/-provider`, `anchor.update-target` | `flows/Airline/Cancellation_by_Buyer.yaml#steps[cancel_Airline_201]`; `flows/Airline/Cancellation_by_Seller.yaml#steps[on_cancel_Airline_203].owner`; `flows/Intercity/Intercity_Bus__Partial_Cancellation_Flow.yaml#steps[update_BUS_231].mock.defaultPayload.message.update_target` |
| Multi-ticket orders | [`concept.multi-ticket-order`](frames/concept.multi-ticket-order.md) | `anchor.parent-item-id`, `anchor.per-passenger-item`, `anchor.add-ons` | `flows/Airline/Purchase_Journey_Multiple_Tickets_.yaml#steps[select_1_Airline_200].mock.defaultPayload.message.order.items`; `specs/openapi.yaml#components.schemas.Item.properties.parent_item_id` |
| Rating | [`concept.rating-acceptance`](frames/concept.rating-acceptance.md), [`concept.rating-rejection`](frames/concept.rating-rejection.md), [`action.rating`](frames/action.rating.md) | `anchor.rating-category-fulfillment`, `anchor.order-status-completed` | `attributes/Intercity.yaml#attribute_set.rating`; `flows/Intercity/Intercity_Bus__Rating_Error_Flow_.yaml#steps[on_rating_261].mock.defaultPayload.error` |
| Grievance / IGM | [`concept.igm-resolution`](frames/concept.igm-resolution.md), [`action.issue`](frames/action.issue.md) | `anchor.igm-1-0-0`, `anchor.igm-2-0-0`, `anchor.issue-open`, `anchor.issue-close`, `anchor.grievance-redressal-officer` | `validations/index.yaml#_TESTS_.issue[ISSUE_VALIDATION_VERSION_100]._SCOPE_`; `flows/Intercity/Intercity_Bus__Station_Code_Based_Flow_With_Igm_1.0.0_.yaml#steps[issue_open_bus_100].api` |
| Payment terms | — (anchors only) | `anchor.payment-collected-by`, `anchor.payment-status-type-enums`, `anchor.payment-tag-groups` | `validations/index.yaml#_TESTS_.init[BUS_VALIDATION]._RETURN_[INIT_PAYMENTS]` |

## Conventions worth knowing before you grep

- A flow step is addressed by its `action_id`, e.g. `#steps[on_init_BUS_221]` — not by list index
  and not by line number.
- `_TESTS_.<action>[<TEST_NAME>]` in `validations/index.yaml` nests through `._RETURN_[…]`;
  a validation's scope lives at `._SCOPE_`.
- Airline tests are keyed `AIRLINE_VALIDATION`, Intercity tests `BUS_VALIDATION`.
- An `anchor.*` handle with `-` in the `grounded-in` column of `anchors/index.md` was interned
  without a config position; its grounded uses are still in `atoms.md`.
- `anchor.on-init-soft-lock-expired` is a **distinct confined subject**, not a synonym for
  `anchor.on-init`. Grep for it before reasoning about the `init → confirm` ordering.

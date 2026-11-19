# ONDC:TRV11 2.0.0 — Metro Overview

A practical guide for new participants (Buyer Apps and Seller Apps) integrating **Metro** ticketing on the ONDC Mobility specification, **TRV11 version 2.0.0**.

| | |
|---|---|
| **Domain** | `ONDC:TRV11` |
| **Version** | `2.0.0` |
| **Use case** | `Metro` (`message.intent.fulfillment.vehicle.category = METRO`) |
| **Audience** | BAP (Buyer App) and BPP (Seller App / Metro operator platform) developers |
| **Source of truth** | The [ONDC TRV11 2.0.0 contract](https://ondc-official.github.io/mobility-specification/?branch=release-TRV11-2.0.0), implemented in `config/flows/Metro`, `config/attributes/Metro.yaml`, `config/validations` and `config/errors` |

---

## 1. What this use case covers

Metro in TRV11 lets a buyer discover a metro operator's network, pick a station pair, buy tickets, receive a QR ticket, and (optionally) cancel or raise a grievance. Every interaction is an asynchronous ONDC API call pair: the caller sends `X`, the receiver acknowledges, then later sends `on_X` with the actual response.

Supported capabilities in 2.0.0:

- Catalog discovery by city, including **route and station codes** (full network)
- Station-pair search returning **fare-bearing items** (point-to-point trips)
- Ticket types: **SJT** (Single Journey Ticket) and **RJT** (Return Journey Ticket)
- Quantity-based purchase (e.g. 2 tickets), with one trip fulfillment per ticket
- BAP-collected payment with settlement terms and buyer-finder fee
- QR-based ticket authorization on each fulfillment
- Order status tracking, including seller-pushed (unsolicited) status updates
- Cancellation: user (soft then hard), partial (per fulfillment), technical, and seller-initiated offline
- Issue and Grievance Management (IGM)

---

## 2. Participants

| Role | Short name | Responsibility |
|---|---|---|
| Buyer App | **BAP** | Customer-facing app. Initiates `search`, `select`, `init`, `confirm`, `status`, `cancel`, `update`. Collects payment (`collected_by: BAP`). |
| Seller App | **BPP** | Metro operator / aggregator platform. Responds with `on_*` callbacks, owns catalog, fares, ticket (QR) generation and order lifecycle. |
| Gateway | — | Broadcasts `search` to BPPs on a city/domain basis. Not involved after `on_search`; all later calls go BAP ↔ BPP directly. |

---

## 3. API summary

| API | Direction | Purpose |
|---|---|---|
| `search` / `on_search` | BAP → BPP / BPP → BAP | Discover catalog (stations/routes) or fares for a station pair |
| `select` / `on_select` | BAP → BPP / BPP → BAP | Choose item and quantity; BPP returns quote and fulfillments |
| `init` / `on_init` | BAP → BPP / BPP → BAP | Provide billing and payment terms; BPP confirms terms |
| `confirm` / `on_confirm` | BAP → BPP / BPP → BAP | Place order after payment; BPP returns order id, `ACTIVE` status and QR tickets |
| `status` / `on_status` | BAP → BPP / BPP → BAP | Fetch current order state; BPP may also push `on_status` unsolicited |
| `cancel` / `on_cancel` | BAP → BPP / BPP → BAP | Cancel the order (soft = query terms, hard = confirm). BPP may also push `on_cancel` unsolicited |
| `update` / `on_update` | BAP → BPP / BPP → BAP | Partial cancellation of individual fulfillments |
| `issue` / `on_issue` / `on_issue_status` | IGM | Raise and resolve grievances |

---

## 4. End-to-end happy path (Single Journey Ticket)

```
BAP                                              BPP
 |-- search (city, METRO) ---------------------->|  1. Catalog search
 |<-------------------- on_search (stations) ----|
 |-- search (START/END station codes) ---------->|  2. Fare search
 |<-------------------- on_search (SJT item) ----|
 |-- select (item I1, qty 2) ------------------->|  3. Select
 |<-------------------- on_select (quote) ------|
 |-- init (billing, payment terms) ------------->|  4. Initialize
 |<-------------------- on_init ----------------|
 |        [ BAP collects payment from buyer ]    |
 |-- confirm (payment PAID) -------------------->|  5. Confirm
 |<-------------------- on_confirm (ACTIVE, QR) -|
 |-- status ------------------------------------>|  6. Track
 |<-------------------- on_status ---------------|
 |<-------------------- on_status (COMPLETED) ---|  7. Journey completion (unsolicited)
```

### Step 1 — Catalog search (`STATION_CODE_FLOW_CATALOG`)

The BAP searches without stops to fetch the operator's network.

- `context.location.city.code`: city code (for example `std:080`), or `*` for all.
- `message.intent.fulfillment.vehicle.category = METRO`.
- `message.intent.payment.collected_by = BAP`, plus tags:
  - `BUYER_FINDER_FEES` (`BUYER_FINDER_FEES_PERCENTAGE`, `BUYER_FINDER_FEES_TYPE`)
  - `SETTLEMENT_TERMS` (`DELAY_INTEREST`, `STATIC_TERMS`)

The BPP's `on_search` returns `catalog.providers[]` with:

- `categories[]`: `TICKET` (`C1`) and `PASS` (`C2`)
- `time.range`: operating hours of the provider
- `fulfillments[]` of `type: ROUTE`, each listing `stops[]` in order. Stop types: `START`, `INTERMEDIATE_STOP`, `TRANSIT_STOP` (interchange, with `instructions.short_desc` such as "Change for Blue Line"), `END`. Each stop has `location.descriptor.code` (the **station code**), `gps`, `id` and `parent_stop_id` (previous stop, which forms a linked chain)
- `payments[]` with `BUYER_FINDER_FEES` and `SETTLEMENT_TERMS` (`SETTLEMENT_WINDOW`, `SETTLEMENT_BASIS`, `MANDATORY_ARBITRATION`, `COURT_JURISDICTION`, `STATIC_TERMS`)
- `tags` with `SCHEDULED_INFO` → `GTFS` (link to the GTFS feed)

> The BAP should cache the station codes from this response and use them as `START` / `END` codes in subsequent searches.

### Step 2 — Fare search (`search` with stops)

Same envelope as Step 1, plus `message.intent.fulfillment.stops`:

```yaml
stops:
  - type: START
    location: { descriptor: { code: SHAHEED_STHAL } }
  - type: END
    location: { descriptor: { code: AZADPUR } }
```

The BPP's `on_search` returns:

- `items[]`, for example `I1` "Single Journey Ticket" (`descriptor.code: SJT`), `price` in INR, `quantity.minimum/maximum.count` (for example 1 to 6), `fulfillment_ids`, and `time` (label `Validity`, duration `P2D`)
- `fulfillments[]` of `type: TRIP` with the stop sequence between the chosen stations

For a return journey the item code is `RJT` (flow `..._RJT`).

### Step 3 — Select

BAP sends the chosen item and quantity:

```yaml
order:
  provider: { id: P1 }
  items:
    - id: I1
      quantity: { selected: { count: 2 } }
```

`on_select` returns the priced order: items, provider, a **trip fulfillment per ticket** (for example `F1`, `F2`), and the `quote`:

- `quote.price` (total) and `quote.breakup[]` (`title: BASE_FARE`, per-item price and quantity)
- `cancellation_terms[].external_ref` (link to the cancellation T&C)
- `tags` → `SCHEDULED_INFO`/`GTFS`

### Step 4 — Init

BAP sends `billing` (buyer details) and a `payments[]` entry:

- `collected_by: BAP`, `status: NOT-PAID`, `type: PRE-ORDER`
- `tags`: `BUYER_FINDER_FEES` and `SETTLEMENT_TERMS` (`SETTLEMENT_AMOUNT`, `SETTLEMENT_WINDOW`, `SETTLEMENT_TYPE`, `DELAY_INTEREST`, `STATIC_TERMS`, `MANDATORY_ARBITRATION`, `COURT_JURISDICTION`)

`on_init` echoes the order and finalized payment terms and quote.

### Step 5 — Confirm

After the buyer pays, BAP sends `confirm` with `payments[0]`:

- `id` (for example `PA1`), `status: PAID`, `type: PRE-ORDER`
- `params: { currency, amount }`
- Same tag structure as `init`

`on_confirm` returns:

- `order.id` (BPP order id) and `order.status: ACTIVE`
- For each trip fulfillment, on the `START` stop an `authorization` block:
  - `type: QR`, `token` (base64 QR image), `valid_to`, `status: UNCLAIMED`

> `on_confirm` must arrive within the `ttl` (`PT30S` by default). A late response is the trigger for the **technical cancellation** flow (section 6).

### Step 6 — Status

`status` queries an order. `on_status` returns the current `order.status` and ticket authorization state. As the buyer uses the QR at the gate, the authorization status changes from `UNCLAIMED` to `CLAIMED`.

### Step 7 — Journey completion

The BPP pushes an **unsolicited** `on_status` when the journey ends: `order.status: COMPLETED` (fulfillment authorization `CLAIMED`).

---

## 5. Ticket variants

| Variant | Item code | Flow files |
|---|---|---|
| Single Journey Ticket | `SJT` | `ORDER_TO_CONFIRM_TO_JOURNEY_COMPLETION_SJT` |
| Return Journey Ticket | `RJT` | `ORDER_TO_CONFIRM_TO_JOURNEY_COMPLETION_RJT` (the second `search` returns an RJT item) |

Each ticket type has a variant ending in `_WITHOUT_SEARCH_ND_SELECT`. It starts at the fare `search`, uses `init_with_user_input`, and skips the catalog search and `select`. Use it when you only want to test the order-creation part.

---

## 6. Cancellation flows

| Flow | Who initiates | Sequence | Notes |
|---|---|---|---|
| **User cancellation** (`USER_CANCELLATION_FLOW`) | Buyer | `cancel` (`descriptor.code: SOFT_CANCEL`) → `on_cancel` (terms and refund preview) → `cancel` (`CONFIRM_CANCEL`) → `on_cancel` | Soft cancel is a query; hard cancel executes. `cancellation_reason_id` such as `"005"` |
| **Partial cancellation** (`PARTIAL_CANCELLATION_FLOW`) | Buyer | `update` (`update_target: order.fulfillments`, fulfillment `F2`, `SOFT_CANCEL`) → `on_update` → `update` (`CONFIRM_CANCEL`) → `on_update` | One fulfillment (one ticket) at a time, per current Workbench limitation |
| **Technical cancellation** (`TECHNICAL_CANCELLATION_FLOW`) | Buyer app | `confirm` → delayed `on_confirm` (beyond `ttl`) → `status` → `cancel` (`CONFIRM_CANCEL`, reason `"000"`) → `on_cancel` | BAP cancels because of a technical failure such as a late `on_confirm` |
| **Seller offline cancellation** (`SELLER_OFFLINE_CANCELLATION`) | Seller | Order confirmed → unsolicited `on_cancel` from BPP | Seller cancels outside the app (for example at the counter or an operational issue) |

---

## 7. Issue and Grievance Management (IGM)

IGM variants of the SJT flow follow the order completion with `issue` / `on_issue` calls:

| Flow | Scenario |
|---|---|
| `..._With_IGM_v-2.0.0` | `issue_open` → `on_issue` (processing) → need more info → `issue_info_provided` → resolution → accept → resolved → close |
| `..._With_IGM_Rejection_v-2.0.0` | Buyer rejects the resolution, then escalates, and finally accepts a later resolution |
| `..._With_IGM_No_Action_v-2.0.0` | Seller proposes a resolution, buyer accepts, issue closed |
| `..._WITH_IGM_1_0_0` | Same order flow with IGM 1.0.0 `issue` / `on_issue` / `on_issue_status` |

---

## 8. Flow catalogue

| Flow ID | Purpose |
|---|---|
| `STATION_CODE_FLOW_CATALOG` | Fetch provider catalog with routes and station codes |
| `ORDER_TO_CONFIRM_TO_JOURNEY_COMPLETION_SJT` | Full SJT journey, search to completion |
| `ORDER_TO_CONFIRM_TO_JOURNEY_COMPLETION_SJT_WITHOUT_SEARCH_ND_SELECT` | SJT, starting from fare search, no select |
| `ORDER_TO_CONFIRM_TO_JOURNEY_COMPLETION_RJT` | Full RJT journey |
| `ORDER_TO_CONFIRM_TO_JOURNEY_COMPLETION_RJT_WITHOUT_SEARCH_ND_SELECT` | RJT, no catalog search or select |
| `..._SJT_WITHOUT_SEARCH_ND_SELECT_With_IGM_v-2.0.0` | SJT + IGM 2.0.0 (need-more-info path) |
| `..._With_IGM_Rejection_v-2.0.0` | SJT + IGM 2.0.0 (reject and escalate) |
| `..._With_IGM_No_Action_v-2.0.0` | SJT + IGM 2.0.0 (accept resolution) |
| `..._WITH_IGM_1_0_0` | SJT + IGM 1.0.0 |
| `USER_CANCELLATION_FLOW` (+ `_WITHOUT_SEARCH_ND_SELECT`) | Buyer-initiated cancellation |
| `PARTIAL_CANCELLATION_FLOW` (+ `_WITHOUT_SEARCH_ND_SELECT`) | Cancel one ticket in an order |
| `TECHNICAL_CANCELLATION_FLOW` (+ `_WITHOUT_SEARCH_ND_SELECT`) | Cancel after a delayed `on_confirm` |
| `SELLER_OFFLINE_CANCELLATION_WITHOUT_SEARCH_ND_SELECT` | Seller-initiated cancellation |

---

## 9. Key data model

### Context (all calls)

| Field | Notes |
|---|---|
| `domain` | `ONDC:TRV11` |
| `action` | API name (`search`, `on_search`, …) |
| `version` | `2.0.0` |
| `location.country.code` | `IND` |
| `location.city.code` | City STD code such as `std:080`, or `*` on first search |
| `transaction_id` | Constant for the whole order lifecycle |
| `message_id` | Unique per request; a callback reuses the request's `message_id` |
| `timestamp` | ISO 8601, validated by the Seller App |
| `ttl` | ISO 8601 duration, format `PT<n>S` (for example `PT30S`) |
| `bap_id`, `bap_uri` | Buyer App identity |
| `bpp_id`, `bpp_uri` | Seller App identity. **Omit on the first `search`**, since it is broadcast |

### Fulfillment and stop types

| Fulfillment `type` | Used in | Meaning |
|---|---|---|
| `ROUTE` | `on_search` (catalog) | A metro line with all its stops |
| `TRIP` | fare `on_search` onward | Journey between the selected `START` and `END` stations |

| Stop `type` | Meaning |
|---|---|
| `START` | Origin station |
| `INTERMEDIATE_STOP` | Station along the way |
| `TRANSIT_STOP` | Interchange station (see `instructions.short_desc`) |
| `END` | Destination station |

### Order and ticket states

| Object | Values seen in flows |
|---|---|
| `order.status` | `ACTIVE` → `COMPLETED`; cancellation states such as `SOFT_CANCEL` and cancelled |
| `payment.status` | `NOT-PAID` (init) → `PAID` (confirm) |
| `fulfillment.stops[].authorization.status` | `UNCLAIMED` (QR issued) → `CLAIMED` (QR used) |
| `descriptor.code` in `cancel` | `SOFT_CANCEL`, `CONFIRM_CANCEL` |

### Payment tags

| Tag | Typical codes |
|---|---|
| `BUYER_FINDER_FEES` | `BUYER_FINDER_FEES_PERCENTAGE`, `BUYER_FINDER_FEES_TYPE` (`percent`) |
| `SETTLEMENT_TERMS` | `SETTLEMENT_AMOUNT`, `SETTLEMENT_WINDOW` (for example `P30D`), `SETTLEMENT_BASIS`, `SETTLEMENT_TYPE` (for example `NEFT`), `DELAY_INTEREST`, `MANDATORY_ARBITRATION`, `COURT_JURISDICTION`, `STATIC_TERMS` |

---

## 10. Integration checklist

**Buyer App (BAP)**

- [ ] Send `vehicle.category = METRO` and `payment.collected_by = BAP` on `search`
- [ ] Do not set `bpp_id` / `bpp_uri` on the first `search`
- [ ] Cache station codes from the catalog `on_search` and use them in `START` / `END` stops
- [ ] Respect item `quantity.minimum` / `maximum` in `select`
- [ ] Keep `transaction_id` constant for one order; use a new `message_id` per request
- [ ] Send `confirm` only after payment is `PAID`, with the amount equal to the quote
- [ ] Handle a late `on_confirm` with the technical cancellation flow
- [ ] Be ready to receive **unsolicited** `on_status` and `on_cancel`
- [ ] Handle the error codes in section 12, retrying only retryable ones (`91219`)
- [ ] Treat a repeated `message_id` as a duplicate (`91214`) and do not resend `confirm` for an in-progress order (`91213`)

**Seller App (BPP)**

- [ ] Return both `ROUTE` fulfillments (catalog) and `TRIP` fulfillments (fare search)
- [ ] Create one `TRIP` fulfillment per ticket quantity
- [ ] Return a QR `authorization` (`type`, `token`, `valid_to`, `status`) on each fulfillment in `on_confirm`
- [ ] Respond to `confirm` within `ttl`
- [ ] Push `on_status` on journey completion and `on_cancel` on seller-side cancellation
- [ ] Include `cancellation_terms` and the `GTFS` tag in the quote
- [ ] Return contract error codes (section 12) in `error.code`, including `91212` after the cancellation window and `91214` for duplicate calls

---

## 11. Validations and testing

- Request payloads are checked by the rules in `config/validations/index.yaml`. Rules apply to Metro only when `message.intent.fulfillment.vehicle.category` is `METRO`. Required context fields include `country.code` (`IND`), `domain` (`ONDC:TRV11`), `timestamp`, `bap_id`, `transaction_id`, `message_id`.
- Attribute definitions (required / usage / owner / type for every path) are in `config/attributes/Metro.yaml`.
- Error codes returned by the Seller App should come from section 12.
- Run the flows in the ONDC Workbench, in this order:
  1. `STATION_CODE_FLOW_CATALOG`
  2. `ORDER_TO_CONFIRM_TO_JOURNEY_COMPLETION_SJT` (then RJT)
  3. Cancellation flows
  4. IGM flows
- Use the `_WITHOUT_SEARCH_ND_SELECT` variants to iterate quickly on order creation.

---

## 12. Error codes

Errors are returned in the `error` object of the `on_*` callback (or the sync NACK). `error.type` is one of `CONTEXT-ERROR`, `CORE-ERROR`, `DOMAIN-ERROR`, `POLICY-ERROR`, `JSON-SCHEMA-ERROR`, and `error.code` comes from the table below. The table mirrors the `x-errorcodes` section of the contract and `config/errors/index.yaml`.

| Code | Event | When it is raised | From |
|---|---|---|---|
| `30001` | Internal Error | Unexpected failure on the seller side | BPP |
| `30008` | Location unserviceable | The city in `context.location.city.code` cannot be serviced | BPP |
| `50001` | Cancellation not possible | Cancellation is not allowed for the selected item | BPP |
| `91201` | Route Serviceability error | The To/From pair is not serviceable by the Seller App | BPP |
| `91202` | Origin station not serviceable | Origin (`START`) station is not operational or unavailable | BPP |
| `91203` | Destination not serviceable | Destination (`END`) station is not operational or unavailable | BPP |
| `91204` | Maximum order qty exceeded | Selected quantity is above `quantity.maximum.count` | BPP |
| `91205` | Tracking not enabled | Tracking is not enabled for any fulfillment in the order | BPP |
| `91206` | Temporarily unavailable | Service temporarily unavailable from the seller side | BPP |
| `91207` | Transaction failure | Payment transaction failed | BPP |
| `91208` | Out-of-operational hours | Ticketing is not allowed outside operating hours | BPP |
| `91209` | Error in retrieving the QR | Unable to retrieve ticket details | BPP |
| `91210` | Unable to get stations data | Unable to retrieve the station list and data | BPP |
| `91211` | Fare fetch error | Cannot fetch fare details for the selected route | BPP |
| `91212` | Cancellation Window Closed | Cancel requested after the cancellation window | BPP |
| `91213` | Order in progress or existing | Same `transaction_id` with a different `message_id` for a booking that is in progress or already created | BPP |
| `91214` | Duplicate API call | Same `transaction_id` and same `message_id` received again | BPP |
| `91215` | Active booking exists | The user already has an active booking | BPP - AFCS |
| `91216` | Ticket already used | Ticket was already used for check-in / check-out | BPP - AFCS |
| `91217` | Payment reference id duplicate | The payment reference id is a duplicate | BPP - AFCS |
| `91218` | Sub system failure | Something went wrong in the ticketing system (**non-retryable**) | BPP - AFCS |
| `91219` | Sub system failure | Request timeout (**retryable**) | BPP - AFCS |

> `BPP - AFCS` means the error originates in the operator's Automatic Fare Collection System behind the Seller App. BAPs can retry only `91219`; the other codes need a changed request or user action.

---

## 13. Resources and related documents

**Contract and specification**

- Interactive contract (API, flows, attributes, error codes, TLC terms): <https://ondc-official.github.io/mobility-specification/?branch=release-TRV11-2.0.0>
- Contract source (`build.yaml`): <https://github.com/ONDC-Official/mobility-specification/blob/release-TRV11-2.0.0/api/build/build.yaml>
- Contract sections used in this guide: `x-flows` (Metro - Station Code Based Flow, GPS Based Flow, Cancel Flow, Partial Cancellation Flow), `x-attributes`, `x-errorcodes`, `x-tlc` (settlement and buyer finder fee terms)

**In this repository**

- [overview.md](./overview.md): TRV11 2.0.0 general overview
- [references.md](./references.md): reference links
- [release-notes.md](./release-notes.md): release notes
- `config/errors/index.yaml`: error codes
- `config/flows/Metro/`: Workbench flow definitions
- `config/attributes/Metro.yaml`: attribute definitions
- `config/validations/index.yaml`: validation rules

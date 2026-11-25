# Beauty & Personal Care (ONDC:RET13 1.2.5)

> **Shop beauty and personal care from any seller, through any app.** ONDC lets one buyer app show catalogs from many beauty sellers, and lets one seller reach buyers on every buyer app, all through a single open protocol.

## At a Glance

| | |
|---|---|
| **Domain** | `ONDC:RET13` (Beauty & Personal Care) |
| **Version** | `1.2.5` |
| **What is sold** | Skin care, hair care, make-up, fragrances, bath and body, and grooming products |
| **Use case** | `BPC` |
| **Delivery model** | Seller-managed delivery, within the city or across cities |
| **Payment** | Prepaid, collected by the buyer app (`payment.type` `ON-ORDER`, `collected_by` `BAP`); cash on delivery (`ON-FULFILLMENT`, Flow 2) |
| **Fulfillment types offered** | `Delivery` (seller delivers) |
| **Flows in this spec** | 20 (17 mandatory): ordering, delivery, cancellation, RTO, returns, replacement, catalog sync and grievances |
| **Grievances** | IGM 1.0.0 and IGM 2.0.0 |

**Why beauty and personal care is different:** products are used on the body, so catalogs carry ingredients, net quantity, expiry dates and manufacturer details, and come in variants such as shade or pack size. Hygiene rules mean many items can't be returned once opened, so return windows and returnability are set per item. Buyers often mix categories, for example skin care and hair care, in one order.

**Who is responsible for what:** the seller owns its catalog, prices, stock, packing, delivery and after-sales service. ONDC standardizes the messages used to discover products, place orders, track delivery, and handle cancellations, returns and grievances.

### What's New in 1.2.5

Compared with version 1.2.0, this version adds:

| Area | What it adds |
|---|---|
| **Payments and commercials** | Cash on Delivery, seller offers applied to the quote. |
| **Products and sellers** | Cross-category carts, seller credentials (for example GI). |
| **Reverse flows** | Replacement with reverse QC, forced cancellation, seller cancellation with RTO. |
| **Catalog** | Catalog rejection by the buyer app. |

---

## Who Is Involved

![Who is involved in a RET13 order: buyer, buyer app, Gateway, seller app, beauty seller and logistics provider](https://raw.githubusercontent.com/ONDC-Official/automation-specifications/draft-RET13-1.2.5/config/docs/assets/ret13-participants.svg)

| Participant | Role in RET13 |
|---|---|
| **Buyer App (BAP)** | Where the buyer searches, builds a cart, pays, tracks the order and raises complaints. It usually collects the payment and settles with the seller later. |
| **Seller App (BPP)** | Represents beauty brands, beauty retailers and D2C personal care sellers. It publishes the catalog, checks stock and serviceability, prices and confirms the order, manages packing and delivery, and handles cancellations, RTO, returns and replacements. |
| **Logistics Provider** | Picks up from the store and delivers to the buyer. Arranged by the seller app. |
| **Gateway** | Forwards a buyer app's `/search` to every seller app serving that city for `ONDC:RET13`. |

### How the Two Apps Talk

Every call is **asynchronous**. The sender gets only an acknowledgement on the same HTTP call. The real answer comes later as a separate call in the other direction, named `on_<action>`.

- An **ACK** only means the message passed schema and signature checks. It is not a business "yes".
- A **business failure**, such as an out-of-stock item, comes back inside the callback as an `error` object (for example `40002` in Flow 7).

| Concept | What it means in RET13 |
|---|---|
| `context.domain` | Always `ONDC:RET13`. `context.core_version` is `1.2.5`. |
| `context.transaction_id` | One ID for one cart's whole journey, from `/select` through delivery, cancellation, return and grievance. |
| `context.message_id` | Pairs a request with its callback: `/select` with M2 is answered by `/on_select` with M2. |
| **Solicited and unsolicited** | A solicited callback answers a request. An unsolicited one is pushed by the seller app on its own, for example `/on_status` when the order is packed, or `/on_search` when a price changes. |
| **Order and fulfillment** | The order has one `state`. Each **fulfillment** inside it has its own `state` and `type`: `Delivery` for the forward shipment, `Cancel` for items the seller cancelled, `RTO` for a failed delivery going back, `Return` for items the buyer returned. |
| **Quote and breakup** | `quote.price` is the order total. `quote.breakup` has one line per item plus `delivery`, `packing`, `tax`, `discount` and `misc` lines (`@ondc/org/title_type`). |
| **Quote trail** | When a cancel, RTO or return lowers the order value, the seller app records the change as a quote trail. The buyer app works out the refund from it. |

---

## Order Lifecycle

A beauty and personal care order goes through two phases. In **pre-order** the two apps agree on the cart, price and terms; nothing is committed. The **order** starts at `/confirm`, once the payment terms are fixed. From then on the order has an ID and a state, and every change is a message on the same `transaction_id`.

![RET13 order lifecycle: Discover, Select, Init, Confirm, Fulfil, then After the order and Settle](https://raw.githubusercontent.com/ONDC-Official/automation-specifications/draft-RET13-1.2.5/config/docs/assets/ret13-order-lifecycle.svg)

| Phase | Buyer app sends | Seller app answers | What is decided in RET13 |
|---|---|---|---|
| Discover | `/search` (through the Gateway) | `/on_search` | Which sellers serve the buyer, with their items, prices and stock |
| Select | `/select` | `/on_select` | Stock and serviceability for the cart; item prices, delivery and packing charges, taxes; delivery time (`@ondc/org/TAT`); offers (Flow 5) |
| Init | `/init` | `/on_init` | Delivery address and billing; final quote; payment, cancellation, return and settlement terms |
| Confirm | `/confirm` | `/on_confirm` | Payment `PAID` (or `NOT-PAID` for cash on delivery, Flow 2); the order is `Created`, its delivery fulfillment is `Pending` |
| Fulfil | `/track` | `/on_status` (unsolicited), `/on_track` | Accepted, packed, agent assigned, picked up, out for delivery, delivered |
| After order | `/cancel`, `/update`, `/issue` | `/on_cancel`, `/on_update`, `/on_issue` | Cancellation, part-cancellation, RTO, returns, replacements, refunds, complaints |
| Settle | — (off-network) | — | Whoever collected the payment settles with the other side as agreed in `/on_init`, less the agreed buyer app fee and taxes such as TCS or TDS |

If the buyer changes the delivery address, or `/on_init` comes back with a smaller cart, the buyer app must send `/select` again.

### Order States

The order `state` is what the buyer sees. It follows the state of the order's fulfillments.

![Order states: Created, Accepted, In-progress, Completed, with Cancelled and returns](https://raw.githubusercontent.com/ONDC-Official/automation-specifications/draft-RET13-1.2.5/config/docs/assets/ret13-order-states.svg)

| Order state | Meaning |
|---|---|
| `Created` | `/on_confirm` sent. The seller app has the order; the seller hasn't accepted it yet. |
| `Accepted` | The seller accepted the order. Cancellation terms from `/on_init` apply from here. |
| `In-progress` | The order is being packed, picked up or delivered. |
| `Completed` | The order is delivered. Only returns can change it now. |
| `Cancelled` | The whole order is cancelled: by the buyer before shipping, or because delivery failed (RTO). |

### Delivery Fulfillment States

The seller app reports every step of the delivery fulfillment in an unsolicited `/on_status`, one message per change. The seller arranges delivery through its own fleet or a logistics provider, within the city or across cities.

![Delivery fulfillment states from Pending to Order-delivered, with cancel and RTO branches](https://raw.githubusercontent.com/ONDC-Official/automation-specifications/draft-RET13-1.2.5/config/docs/assets/ret13-fulfillment-states.svg)

| Fulfillment state | When it is set | Order state | Sent in |
|---|---|---|---|
| `Pending` | As soon as the order is confirmed | `Created`, then `Accepted` | `/on_confirm`, `/on_status` |
| `Packed` | Items packed and ready for pickup | `In-progress` | `/on_status` |
| `Agent-assigned` | Delivery agent assigned; name and phone shared | `In-progress` | `/on_status` |
| `Order-picked-up` | Agent collected the order from the store | `In-progress` | `/on_status` |
| `Out-for-delivery` | Agent on the way to the buyer | `In-progress` | `/on_status` |
| `Order-delivered` | Handed over, with the delivery time; for cash on delivery, payment becomes `PAID` | `Completed` | `/on_status` |
| `Cancelled` | Fulfillment cancelled, or RTO started | `Cancelled` | `/on_cancel` |

### Lifecycle Rules for RET13 Implementations

1. **Terminal states are frozen.** Nothing changes a `Cancelled` order. A `Completed` order changes only through returns and replacements.
2. **One message per change.** Every status change is an unsolicited `/on_status`. Every change to order details (part-cancel, return) is an `/on_update`. Changes are never batched.
3. **`/on_update` and `/on_status` carry the full picture:** every item and fulfillment with its current state, the quote and breakup, the quote trail and the settlement trail.
4. **The order value never goes up after confirmation.** It only goes down, and only by reducing an item's quantity.
5. **Cancellation fees follow the terms in `/on_init`,** which are set per fulfillment state and reason code.
6. **Refunds are settled with `/update`.** After a part-cancel, RTO or return, the buyer app sends `/update` with the settlement details for the refund (Flows 9 and 11).

---

## Scenarios: Where the Order Branches

These are the points in a RET13 order where more than one outcome is possible, with the flow that tests each path. The green **refund trigger** badge marks the point: the seller app sends the updated quote there, and the buyer app works out the refund from the quote trail.

### 1. Select: Is Everything in Stock?

Each shade and pack size is stocked separately, so the seller app re-checks every item at `/select`.

![Select scenario: all in stock goes to /init; out of stock returns error 40002 and the buyer fixes the cart](https://raw.githubusercontent.com/ONDC-Official/automation-specifications/draft-RET13-1.2.5/config/docs/assets/ret13-scenario-select.svg)

Flow 7 stops at the error. Flow 6 goes on: the buyer fixes the cart, selects again and completes the order.

### 2. Cancellation: Who Cancels, and When

![Cancellation: buyer cancels, seller part-cancels, delivery fails (RTO), or forced cancellation](https://raw.githubusercontent.com/ONDC-Official/automation-specifications/draft-RET13-1.2.5/config/docs/assets/ret13-scenario-cancellation.svg)

A forced cancellation (Flow 10) is for an order that is already out for delivery. The buyer app first sends `/cancel` with the `force` param set to `no`, which the seller can refuse within `ttl_response`. It then sends `/cancel` again with `force` set to `yes`, and the seller app must cancel the order.

### 3. Return to Origin (RTO): Delivery Failed

RTO starts when the buyer refuses the order or can't be reached at the address.

![RTO: delivery fails, /on_cancel with reason 013, refund settlement, RTO-Delivered](https://raw.githubusercontent.com/ONDC-Official/automation-specifications/draft-RET13-1.2.5/config/docs/assets/ret13-scenario-rto.svg)

If the items are not taken back to the store, the RTO fulfillment ends in `RTO-Disposed` instead of `RTO-Delivered`.

### 4. Return: After Delivery

A buyer can return a delivered item within its return window from the catalog (`@ondc/org/return_window`), for the full order or part of it. The buyer app sends `/update` with the item, quantity and reason. The seller app creates a new **Return** fulfillment and reports each step in an unsolicited `/on_update`.

![Return states: Return_Initiated, Return_Approved, Return_Picked, Return_Delivered, or Liquidated](https://raw.githubusercontent.com/ONDC-Official/automation-specifications/draft-RET13-1.2.5/config/docs/assets/ret13-scenario-return.svg)

The order stays `Completed` throughout. The refund is triggered at `Return_Picked` (pickup) or `Liquidated` (no pickup).

**Replacement (Flow 12).** The buyer asks for a replacement of a damaged or wrong item. The seller approves it, a reverse quality check (QC) is done at pickup, the item goes back to the seller, and a replacement is packed and delivered.

### 5. Variations on the Standard Order

RET13 1.2.5 adds flows that change one part of the standard order: how it is paid for, how it is delivered, or what goes in the cart.

![Variations on the RET13 order: payment, delivery and cart options, each with its flow](https://raw.githubusercontent.com/ONDC-Official/automation-specifications/draft-RET13-1.2.5/config/docs/assets/ret13-order-variants.svg)

| Variation | What changes | Flow |
|---|---|---|
| Cash on delivery | The buyer chooses to pay at delivery. The order is placed with payment type `ON-FULFILLMENT` and payment status `NOT-PAID`. When the agent collects cash at the door, the seller sends the delivered status with the payment marked `PAID`. | 2 |
| Offers | Sellers publish offers in their catalog. The buyer applies an offer during `/select`, and the seller reflects the discount in the quote through to order confirmation. | 5 |
| Cross-category cart | The buyer can place one order with items from different categories offered by the same seller, and the order is priced and fulfilled together. | 4 |
| Seller credentials | Sellers can share credentials such as a Geographical Indication (GI) certificate in `provider.creds`. These are carried with the order so the buyer app can display them. | 3 |

### 6. Complaints (IGM)

A buyer can raise a complaint about a delivered order, for example a leaking bottle, an expired product or a wrong shade. It runs on its own `/issue` and `/on_issue` messages, on the same order.

![IGM complaint flow with info request, rejection, escalation and outcomes](https://raw.githubusercontent.com/ONDC-Official/automation-specifications/draft-RET13-1.2.5/config/docs/assets/ret13-scenario-igm.svg)

| Version | How it works in RET13 |
|---|---|
| **IGM 1.0.0** | The buyer opens an issue, the seller acknowledges it and sends the resolution through `/on_issue_status`, and the buyer closes it (Flow 17). |
| **IGM 2.0.0** | Adds information requests, resolution acceptance or rejection, and escalation. An accepted resolution can start a replacement or a return on the order through `/on_update` (Flows 18, 19 and 20). |

---

## The Beauty Catalog

### What the Catalog Contains

Each seller app's `/on_search` can include:

- Seller name, location and serviceable area
- Products with images, brand and description
- Variants such as shade, size or pack quantity
- Ingredients, net quantity and expiry date
- MRP, selling price and stock availability
- Return window and whether the item is returnable, plus statutory details such as manufacturer and country of origin

If a catalog has errors, such as a price above MRP, the buyer app sends `/catalog_rejection` with each error's type, code and path (Flow 16).

### Keeping Catalogs Fresh

Sellers don't need to resend the whole catalog for every change.

![Catalog sync: push with unsolicited /on_search, or pull with /search for changed items](https://raw.githubusercontent.com/ONDC-Official/automation-specifications/draft-RET13-1.2.5/config/docs/assets/ret13-catalog-sync.svg)

---

## Flow Summary

17 of the 20 flows are mandatory. The API Walkthrough shows the step-by-step calls for each one.

| # | Flow | Group | Status | What it covers |
|---|---|---|---|---|
| 1 | Delivery Flow | Ordering | Mandatory | The standard order: the buyer selects items, gets a quote, pays online, and receives the order through seller-managed delivery |
| 2 | Cash on Delivery Flow | Payment | Optional | Same as the Delivery Flow, except the buyer pays in cash at the door instead of paying online |
| 3 | Seller Credentials Flow | Ordering | Mandatory | A normal order where the seller's credentials (for example a GI certification) are shared with the order, so the buyer app can show them to the buyer |
| 4 | Cross-Category Cart Flow | Ordering | Mandatory | The buyer combines items from more than one category in a single cart and order |
| 5 | Offers Flow | Payment | Mandatory | The buyer applies a seller offer (such as a discount) while selecting items, and the quote reflects the offer |
| 6 | Out of Stock Flow | Ordering | Mandatory | An item turns out to be out of stock when the buyer selects it |
| 7 | Out of Stock Flow (Error Code) | Ordering | Mandatory | The seller rejects the selection straight away because an item is out of stock |
| 8 | Buyer Cancellation Flow | After the order | Mandatory | The buyer cancels a confirmed order before it is shipped |
| 9 | Seller Cancellation Flow | After the order | Mandatory | The seller cancels part of the order after confirmation, and later the remaining order is cancelled as Return to Origin (RTO) when delivery fails |
| 10 | Forced Cancellation Flow | After the order | Mandatory | The order is already out for delivery when the buyer wants to cancel |
| 11 | Return Flow | After the order | Mandatory | After delivery, the buyer returns an item |
| 12 | Replacement Flow | After the order | Optional | After delivery, the buyer asks for a replacement |
| 13 | Discovery Flow – Full Catalog | Catalog | Mandatory | The buyer app searches a city and the seller returns its full catalog |
| 14 | Discovery Flow – Incremental Catalog (Push) | Catalog | Mandatory | After the first search, the seller pushes catalog changes as they happen, without resending the whole catalog |
| 15 | Discovery Flow – Incremental Catalog Refresh (Pull) | Catalog | Optional | The buyer app asks the seller for only the items that changed after a given time |
| 16 | Catalog Rejection Flow | Catalog | Mandatory | The buyer app finds errors in a seller's catalog and rejects it, telling the seller what is wrong |
| 17 | Delivery Flow with IGM 1.0.0 | Grievances | Mandatory | A delivered order followed by a complaint handled under IGM 1.0.0 |
| 18 | Delivery Flow with IGM 2.0.0 – No Action | Grievances | Mandatory | A complaint under IGM 2.0.0 that the seller resolves with an explanation and no further action, which the buyer accepts |
| 19 | Delivery Flow with IGM 2.0.0 – Rejection and Escalation | Grievances | Mandatory | The buyer rejects the seller's resolution and escalates the complaint |
| 20 | Delivery Flow with IGM 2.0.0 | Grievances | Mandatory | A complaint under IGM 2.0.0 where the seller asks for more information, proposes a replacement, and the buyer accepts |

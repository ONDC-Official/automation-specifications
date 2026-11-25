# Food & Beverage (ONDC:RET11 1.2.0)

> **Order food from any restaurant, through any app.** ONDC lets one buyer app show menus from many restaurants, and lets one restaurant reach buyers on every buyer app, all through a single open protocol.

## At a Glance

| | |
|---|---|
| **Domain** | `ONDC:RET11` (Food & Beverage) |
| **Version** | `1.2.0` |
| **What is sold** | Restaurant meals, snacks, beverages, desserts and bakery items, prepared to order |
| **Use case** | `F&B` |
| **Delivery model** | Hyperlocal: one restaurant to one buyer, one rider, delivery usually within the hour |
| **Payment** | Prepaid, collected by the buyer app (`payment.type` `ON-ORDER`, `collected_by` `BAP`) |
| **Fulfillment types offered** | `Delivery` (seller delivers), `Buyer-Delivery` (buyer app delivers) |
| **Flows in this spec** | 13 (13 mandatory): ordering, delivery, cancellation, RTO, returns, catalog sync and grievances |
| **Grievances** | IGM 1.0.0 and IGM 2.0.0 |

**Why food is different:** every order is cooked to order and has to reach the buyer hot and fast. Restaurants serve a small radius and have opening hours and preparation times, menu items sell out during the day, and most dishes come with customisations such as size, add-ons and toppings, grouped as custom groups with minimum and maximum choices. Food can't go back on the shelf, so a failed delivery usually ends with the food disposed of rather than returned (`RTO-Disposed`). Outlets must also show FSSAI details and mark items as veg or non-veg.

**Who is responsible for what:** the seller owns its catalog, prices, stock, packing, delivery and after-sales service. ONDC standardizes the messages used to discover products, place orders, track delivery, and handle cancellations, returns and grievances.

---

## Who Is Involved

![Who is involved in a RET11 order: buyer, buyer app, Gateway, seller app, restaurant and logistics provider](https://raw.githubusercontent.com/ONDC-Official/automation-specifications/draft-RET11-1.2.0/config/docs/assets/ret11-participants.svg)

| Participant | Role in RET11 |
|---|---|
| **Buyer App (BAP)** | Where the buyer searches, builds a cart, pays, tracks the order and raises complaints. It usually collects the payment and settles with the seller later. In Flow 2 it also arranges delivery. |
| **Seller App (BPP)** | Represents restaurants, cloud kitchens, cafés and food chains. It publishes the catalog, checks stock and serviceability, prices and confirms the order, manages packing and delivery, and handles cancellations, RTO, returns. |
| **Logistics Provider** | Picks up from the restaurant and delivers to the buyer. Usually arranged by the seller app; arranged by the buyer app in Flow 2. |
| **Gateway** | Forwards a buyer app's `/search` to every seller app serving that city for `ONDC:RET11`. |

### How the Two Apps Talk

Every call is **asynchronous**. The sender gets only an acknowledgement on the same HTTP call. The real answer comes later as a separate call in the other direction, named `on_<action>`.

- An **ACK** only means the message passed schema and signature checks. It is not a business "yes".
- A **business failure**, such as an out-of-stock item, comes back inside the callback as an `error` object (for example `40002` in Flow 3).

| Concept | What it means in RET11 |
|---|---|
| `context.domain` | Always `ONDC:RET11`. `context.core_version` is `1.2.0`. |
| `context.transaction_id` | One ID for one cart's whole journey, from `/select` through delivery, cancellation, return and grievance. |
| `context.message_id` | Pairs a request with its callback: `/select` with M2 is answered by `/on_select` with M2. |
| **Solicited and unsolicited** | A solicited callback answers a request. An unsolicited one is pushed by the seller app on its own, for example `/on_status` when the order is packed, or `/on_search` when a price changes. |
| **Order and fulfillment** | The order has one `state`. Each **fulfillment** inside it has its own `state` and `type`: `Delivery` (or `Buyer-Delivery`) for the forward shipment, `Cancel` for items the seller cancelled, `RTO` for a failed delivery going back, `Return` for items the buyer returned. |
| **Quote and breakup** | `quote.price` is the order total. `quote.breakup` has one line per item plus `delivery`, `packing`, `tax`, `discount` and `misc` lines (`@ondc/org/title_type`). Each chosen customisation is its own line, linked to its parent item. |
| **Quote trail** | When a cancel, RTO or return lowers the order value, the seller app records the change as a quote trail. The buyer app works out the refund from it. |

---

## Order Lifecycle

A food order goes through two phases. In **pre-order** the two apps agree on the cart, price and terms; nothing is committed. The **order** starts at `/confirm`, after the buyer has paid. From then on the order has an ID and a state, and every change is a message on the same `transaction_id`.

![RET11 order lifecycle: Discover, Select, Init, Confirm, Fulfil, then After the order and Settle](https://raw.githubusercontent.com/ONDC-Official/automation-specifications/draft-RET11-1.2.0/config/docs/assets/ret11-order-lifecycle.svg)

| Phase | Buyer app sends | Seller app answers | What is decided in RET11 |
|---|---|---|---|
| Discover | `/search` (through the Gateway) | `/on_search` | Which sellers serve the buyer, with their menus, customisations, prices and availability |
| Select | `/select` | `/on_select` | Stock and serviceability for the cart; item prices, delivery and packing charges, taxes; delivery time (`@ondc/org/TAT`) |
| Init | `/init` | `/on_init` | Delivery address and billing; final quote; payment, cancellation, return and settlement terms |
| Confirm | `/confirm` | `/on_confirm` | Payment `PAID`; the order is `Created`, its delivery fulfillment is `Pending` |
| Fulfil | `/track` | `/on_status` (unsolicited), `/on_track` | Accepted, packed, agent assigned, picked up, out for delivery, delivered |
| After order | `/cancel`, `/update`, `/issue` | `/on_cancel`, `/on_update`, `/on_issue` | Cancellation, part-cancellation, RTO, returns, refunds, complaints |
| Settle | — (off-network) | — | The buyer app pays the seller as agreed in `/on_init`, less the agreed buyer app fee and taxes such as TCS or TDS |

If the buyer changes the delivery address, or `/on_init` comes back with a smaller cart, the buyer app must send `/select` again.

### Order States

The order `state` is what the buyer sees. It follows the state of the order's fulfillments.

![Order states: Created, Accepted, In-progress, Completed, with Cancelled and returns](https://raw.githubusercontent.com/ONDC-Official/automation-specifications/draft-RET11-1.2.0/config/docs/assets/ret11-order-states.svg)

| Order state | Meaning |
|---|---|
| `Created` | `/on_confirm` sent. The seller app has the order; the seller hasn't accepted it yet. |
| `Accepted` | The seller accepted the order. Cancellation terms from `/on_init` apply from here. |
| `In-progress` | The order is being packed, picked up or delivered. |
| `Completed` | The order is delivered. Only returns can change it now. |
| `Cancelled` | The whole order is cancelled: by the buyer before shipping, or because delivery failed (RTO). |

### Delivery Fulfillment States

The seller app reports every step of the delivery fulfillment in an unsolicited `/on_status`, one message per change. Food delivery is hyperlocal: one rider takes the order from the restaurant to the buyer.

![Delivery fulfillment states from Pending to Order-delivered, with cancel and RTO branches](https://raw.githubusercontent.com/ONDC-Official/automation-specifications/draft-RET11-1.2.0/config/docs/assets/ret11-fulfillment-states.svg)

| Fulfillment state | When it is set | Order state | Sent in |
|---|---|---|---|
| `Pending` | As soon as the order is confirmed | `Created`, then `Accepted` | `/on_confirm`, `/on_status` |
| `Packed` | Items packed and ready for pickup | `In-progress` | `/on_status` |
| `Agent-assigned` | Delivery agent assigned; name and phone shared | `In-progress` | `/on_status` |
| `Order-picked-up` | Agent collected the order from the restaurant | `In-progress` | `/on_status` |
| `Out-for-delivery` | Agent on the way to the buyer | `In-progress` | `/on_status` |
| `Order-delivered` | Handed over, with the delivery time | `Completed` | `/on_status` |
| `Cancelled` | Fulfillment cancelled, or RTO started | `Cancelled` | `/on_cancel` |

In Flow 2 (`Buyer-Delivery`), the same states are reported the other way: the buyer app sends them to the seller app in `/update`.

### Lifecycle Rules for RET11 Implementations

1. **Terminal states are frozen.** Nothing changes a `Cancelled` order. A `Completed` order changes only through returns.
2. **One message per change.** Every status change is an unsolicited `/on_status`. Every change to order details (part-cancel, return) is an `/on_update`. Changes are never batched.
3. **`/on_update` and `/on_status` carry the full picture:** every item and fulfillment with its current state, the quote and breakup, the quote trail and the settlement trail.
4. **The order value never goes up after confirmation.** It only goes down, and only by reducing an item's quantity.
5. **Cancellation fees follow the terms in `/on_init`,** which are set per fulfillment state and reason code.
6. **Refunds are settled with `/update`.** After a part-cancel, RTO or return, the buyer app sends `/update` with the settlement details for the refund (Flows 5 and 6).

---

## Scenarios: Where the Order Branches

These are the points in a RET11 order where more than one outcome is possible, with the flow that tests each path. The green **refund trigger** badge marks the point: the seller app sends the updated quote there, and the buyer app works out the refund from the quote trail.

### 1. Select: Is Everything in Stock?

Dishes and add-ons can sell out during the day, so the seller app re-checks every item, including its customisations, at `/select`.

![Select scenario: all in stock goes to /init; out of stock returns error 40002 and the buyer fixes the cart](https://raw.githubusercontent.com/ONDC-Official/automation-specifications/draft-RET11-1.2.0/config/docs/assets/ret11-scenario-select.svg)

### 2. Cancellation: Who Cancels, and When

![Cancellation: buyer cancels, seller part-cancels, delivery fails (RTO)](https://raw.githubusercontent.com/ONDC-Official/automation-specifications/draft-RET11-1.2.0/config/docs/assets/ret11-scenario-cancellation.svg)

### 3. Return to Origin (RTO): Delivery Failed

RTO starts when the buyer refuses the order or can't be reached at the address.

![RTO: delivery fails, /on_cancel with reason 013, refund settlement, RTO-Disposed](https://raw.githubusercontent.com/ONDC-Official/automation-specifications/draft-RET11-1.2.0/config/docs/assets/ret11-scenario-rto.svg)

Cooked food can't be resold, so the RTO fulfillment usually ends in `RTO-Disposed`. If the items are taken back to the restaurant, it ends in `RTO-Delivered` instead.

### 4. Return: After Delivery

A buyer can return a delivered item within its return window from the catalog (`@ondc/org/return_window`), for the full order or part of it. The buyer app sends `/update` with the item, quantity and reason. The seller app creates a new **Return** fulfillment and reports each step in an unsolicited `/on_update`.

![Return states: Return_Initiated, Return_Approved, Return_Picked, Return_Delivered, or Liquidated](https://raw.githubusercontent.com/ONDC-Official/automation-specifications/draft-RET11-1.2.0/config/docs/assets/ret11-scenario-return.svg)

The order stays `Completed` throughout. The refund is triggered at `Return_Picked` (pickup) or `Liquidated` (no pickup).

### 5. Who Delivers?

| Fulfillment type | Who arranges delivery | Who reports delivery states | Flow |
|---|---|---|---|
| `Delivery` | The seller app, through its own fleet or a logistics provider | The seller app, in unsolicited `/on_status` | 1 |
| `Buyer-Delivery` | The buyer app, through its own logistics provider | The buyer app, in `/update`; the seller app answers with `/on_update` and marks the order complete once delivered | 2 |

For `Buyer-Delivery`, the seller app's quote has packing charges but no delivery charge, plus the time to get the order ready and the package weight and dimensions.

### 6. Complaints (IGM)

A buyer can raise a complaint about a delivered order, for example a missing item, a wrong dish or spilled food. It runs on its own `/issue` and `/on_issue` messages, on the same order.

![IGM complaint flow with info request, rejection, escalation and outcomes](https://raw.githubusercontent.com/ONDC-Official/automation-specifications/draft-RET11-1.2.0/config/docs/assets/ret11-scenario-igm.svg)

| Version | How it works in RET11 |
|---|---|
| **IGM 1.0.0** | The buyer opens an issue, the seller acknowledges it and sends the resolution through `/on_issue_status`, and the buyer closes it (Flow 10). |
| **IGM 2.0.0** | Adds information requests, resolution acceptance or rejection, and escalation. An accepted resolution can start a replacement or a return on the order through `/on_update` (Flows 11, 12 and 13). |

---

## The Menu Catalog

### What the Catalog Contains

Each seller app's `/on_search` can include:

- Restaurant name, location, timings, preparation time and serviceable area
- Menu categories and items, with images and descriptions
- Customisation groups such as size, crust or add-ons, with minimum and maximum choices
- Veg or non-veg marker for each item
- Price and availability
- FSSAI licence details of the outlet

### Keeping Catalogs Fresh

Sellers don't need to resend the whole catalog for every change.

![Catalog sync: push with unsolicited /on_search, or pull with /search for changed items](https://raw.githubusercontent.com/ONDC-Official/automation-specifications/draft-RET11-1.2.0/config/docs/assets/ret11-catalog-sync.svg)

---

## Flow Summary

All 13 flows are mandatory. The API Walkthrough shows the step-by-step calls for each one.

| # | Flow | Group | What it covers |
|---|---|---|---|
| 1 | Delivery Flow | Ordering | The standard order: the buyer selects items, gets a quote, pays online, and receives the order through seller-managed delivery |
| 2 | Buyer Delivery Flow | Ordering | The buyer app arranges delivery |
| 3 | Out of Stock Flow (Error Code) | Ordering | The seller rejects the selection straight away because an item is out of stock |
| 4 | Buyer Cancellation Flow | After the order | The buyer cancels a confirmed order before it is shipped |
| 5 | RTO and Part-Cancellation Flow | After the order | The seller cancels some items it cannot supply, then delivery of the rest fails and the order returns to the seller (Return to Origin) |
| 6 | Return Flow | After the order | After delivery, the buyer returns an item |
| 7 | Discovery Flow – Full Catalog | Catalog | The buyer app searches a city and the seller returns its full catalog |
| 8 | Discovery Flow – Incremental Catalog (Push) | Catalog | After the first search, the seller pushes catalog changes as they happen, without resending the whole catalog |
| 9 | Discovery Flow – Incremental Catalog Refresh (Pull) | Catalog | The buyer app asks the seller for only the items that changed after a given time |
| 10 | Delivery Flow with IGM 1.0.0 | Grievances | A delivered order followed by a complaint handled under IGM 1.0.0 |
| 11 | Delivery Flow with IGM 2.0.0 – No Action | Grievances | A complaint under IGM 2.0.0 that the seller resolves with an explanation and no further action, which the buyer accepts |
| 12 | Delivery Flow with IGM 2.0.0 – Rejection and Escalation | Grievances | The buyer rejects the seller's resolution and escalates the complaint |
| 13 | Delivery Flow with IGM 2.0.0 | Grievances | A complaint under IGM 2.0.0 where the seller asks for more information, proposes a replacement, and the buyer accepts |

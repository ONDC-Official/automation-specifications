# Logistics (P2H2P)

> Point-to-hub-to-point (intercity) delivery on ONDC, domain `ONDC:LOG11`, as defined in the **ONDC API Contract for Logistics, v1.2.5**.

---

## 1. Overview

In a **point-to-hub-to-point (P2H2P)** shipment, the package doesn't go straight from the seller to the buyer. It is picked up, taken to the LSP's source hub, moved through its network to a destination hub, and then delivered. This is the model for intercity and courier shipments, which usually take a day or more.

| Leg | Where the package is | State the LSP reports |
| --- | --- | --- |
| Pickup | Picked up from the merchant | `Order-picked-up` |
| First mile | At the LSP's source hub | `In-transit` |
| Between hubs | At the hub that serves the delivery location | `At-destination-hub` |
| Last mile | On the way to the customer | `Out-for-delivery` |
| Delivery | Handed over to the customer | `Order-delivered` |

Because the package is sorted and handled at hubs, it needs suitable packaging and an **AWB number** to identify it along the way. Both are part of every P2H2P order.

A logistics order always sits behind a retail order. When a customer buys from a seller on ONDC, the seller's app has to get the goods delivered. To do that, it becomes a **buyer on the logistics network** and books a shipment from a **Logistics Service Provider (LSP)**. It shares the retail order's details with the LSP as the *linked order*.

The retail seller app sells on the retail network and buys on the logistics network. In the logistics transaction it is the BAP, and the LSP is the BPP.

**Why a separate domain:** since version 1.2.5, P2H2P shipments use their own domain code, `ONDC:LOG11`. This lets the Gateway send a P2H2P search only to P2H2P providers. Direct, hyperlocal shipments use `ONDC:LOG10`.

**Version:** 1.2.5 builds on 1.2.0, and most APIs are backward compatible. The one exception is the updated RTO flow, described in [Return to Origin](#9-return-to-origin-rto). Because of it, the two versions run side by side.

### Participants

| Participant | Role |
| --- | --- |
| **Logistics buyer (LBNP)** | The buyer app (BAP) on the logistics network, usually the seller app of the retail order. It searches for shipping options, books one, says when the package is ready to ship, and tracks the shipment. |
| **Logistics Service Provider (LSP)** | The seller app (BPP) on the logistics network, typically a courier. It quotes prices and delivery times, provides the AWB number and shipping label, moves the package through its hubs, and reports progress until delivery. |
| **Rider** | The LSP's agent for pickup and last-mile delivery. The rider doesn't call any API, but the states the LSP reports, such as `Out-for-pickup` and `Out-for-delivery`, follow the rider's progress. |
| **End seller and end buyer** | The merchant who hands over the package and the customer who receives it. They confirm the handover with pickup and delivery codes, such as an OTP. |

---

## 2. Key Terms

| Term | Meaning |
| --- | --- |
| **AWB number** | The air waybill number that identifies the shipment through the LSP's network. It is required for `ONDC:LOG11` and is 11 to 16 digits long. It can come from either side: the LBNP in `/confirm` or `/update`, or the LSP in `/on_confirm` or `/on_update`. |
| **Shipping label** | The label the LSP provides to put on the package, as an image or a PDF. The LSP can send several labels in different page sizes. |
| **Shipment type** | `flyer` (a soft packet) or `box`. It decides how the weight for pricing is worked out. See [Weight for pricing](#weight-for-pricing). |
| **Ready to ship (RTS)** | The `ready_to_ship` tag says the package is packed and can be picked up. The LSP arranges pickup only after RTS. |
| **S2D TAT** | Ship-to-delivery turnaround time: how long the LSP takes to deliver once it has the shipment. It is quoted per category, or per option, in `/on_search`. |
| **Linked order** | The retail order being shipped: its ID, items, weight, dimensions, declared value and category. |
| **NDR** | Non-delivery report: what happens after a failed delivery attempt. See [Failed Attempts and NDR](#6-failed-attempts-and-ndr). |
| **RTO** | Return to origin: what happens to a package that can't be delivered. |
| **Baseline and enhanced features** | Every participant must support the baseline features. Enhanced features are optional and have a feature ID, for example `00E` for the pickup and delivery attempt trail. See [Enhanced Features](#12-enhanced-features). |

---

## 3. Delivery Categories and Pricing

| Category | How the package travels |
| --- | --- |
| **Express Delivery** | By air. P2H2P only. |
| **Standard Delivery** | By surface. Its sub-categories are Immediate, Same Day and Next Day Delivery. |

- **A search for Express Delivery** returns every P2H2P option the LSP can offer.
- **A search for Standard Delivery** returns every option the LSP can offer in that category, including its sub-categories.
- **Rate card:** an LSP can also publish a rate card from pickup to delivery location by weight slab, with separate rates for Standard and Express, and for forward and return shipments (feature `004`).

### Weight for Pricing

For P2H2P, the LSP prices a shipment on its dead weight or its volumetric weight (its size), depending on the shipment type.

| Shipment type | Dead weight | Priced on |
| --- | --- | --- |
| `flyer` | Under 1 kg | The dead weight |
| `flyer` | 1 kg or more | The higher of the dead weight and the volumetric weight |
| `box` | Any | The higher of the dead weight and the volumetric weight |

**Example:** a seller ships 500 g in a 22 × 20 × 18 cm box. The volumetric weight is 22 × 20 × 18 / 5000 ≈ 1.58 kg. That is higher than the dead weight, so the shipment is priced on the volumetric weight. A large box takes up space and handling in the LSP's network even when it is light.

---

## 4. The Order Journey

### The Complete Flow

A complete order passes through these calls, in this order:

1. **Discover:** the LBNP sends `/search` through the Gateway, which sends it only to P2H2P providers, and each LSP that can serve the route replies with `/on_search`: its options, prices, S2D TAT and RTO price.
2. **Book:** the LBNP sends `/init` with the chosen option, addresses, billing and payment type, and the LSP replies with `/on_init`: the final quote and the payment and cancellation terms. The LBNP then sends `/confirm` with the order in state `Created` and the linked retail order, and the LSP replies with `/on_confirm`: the order `Accepted`, with the fulfillment `Pending`.
3. **Ready to ship:** the LBNP sends `/update` with `ready_to_ship` set to `yes`, and the LSP replies with `/on_update`: the fulfillment moves to `Searching-for-Agent`, with the AWB number and shipping labels.
4. **Pickup and hubs:** the LSP sends unsolicited `/on_status` updates: `Agent-assigned`, `Out-for-pickup` and `Order-picked-up`, then `In-transit` at the source hub and `At-destination-hub`.
5. **Deliver:** the LBNP can call `/track`, and the LSP replies with `/on_track` (a tracking URL). The LSP keeps sending `/on_status`: `Out-for-delivery` and then `Order-delivered`, at which point the order is `Completed`.

The **ORDER FLOW BASE LINE** flow in the API Walkthrough follows this sequence. Every flow in the API Walkthrough also has its own sequence diagram: pick a step and open the **Sequence Diagram** tab to see the whole flow, with that step highlighted.

### Stage 1: Discover

The LBNP asks which providers can ship between two points, and at what price.

**Network interaction:**

- **`/search`**: The LBNP sends the pickup and drop locations (GPS coordinates and area code), the category, the package's weight, dimensions and declared value, and the payment type. The Gateway sends the search only to P2H2P providers.
- **`/on_search`**: Each LSP checks whether it can serve the route. If it can, it returns its catalog. The catalog lists each shipping option with a tax-inclusive price and the S2D TAT. Each option comes with a linked RTO price, so the LBNP knows the return cost up front. If the shipment must be dropped off at the LSP's location, the catalog gives that location. An LSP that can't serve the route doesn't respond.

### Stage 2: Book

The LBNP picks an option, gets the final quote, and places the order.

**Network interaction:**

- **`/init`**: The LBNP sends the chosen option, the full pickup and drop addresses and contacts, its billing details, including its GST number, and the payment type. The LSP checks serviceability again and returns an error if it can't serve the locations.
- **`/on_init`**: The LSP returns the itemised quote: the delivery charge and tax, whose total must equal the sum of the line items. The quote also gives how long it is valid, along with the payment terms and cancellation terms. The price must match `/on_search` and can't change until the order is confirmed.
- **`/confirm`**: The LBNP creates the order in state **`Created`**, with an order ID that is unique across the network. It sends:
  - the linked retail order;
  - the shipment type, weight and dimensions, which are mandatory for intercity shipments;
  - the pickup and delivery codes and the `ready_to_ship` status;
  - whether a failed delivery should return to the pickup location;
  - its acceptance of the LSP's terms.

  If the weight or dimensions differ from the search, the LSP can reply with **NACK 60011**. The LSP creates the shipment manifest.
- **`/on_confirm`**: The LSP returns the same order ID in state **`Accepted`**, with the fulfillment in **`Pending`**, and confirms the S2D TAT. For an inter-state shipment, it also gives the e-way bill number, where one applies.

The payment type is one of `ON-ORDER` (prepaid, typically from a wallet), `ON-FULFILLMENT` (cash on delivery) or `POST-FULFILLMENT` (billed after delivery).

#### Confirming an Order Safely

The contract sets rules so that neither side keeps an order the other side doesn't have. `/confirm` and `/on_confirm` must be idempotent: sending the same call again must not create a second order.

- **If the LSP can't accept `/confirm`:** it replies with **NACK 66002**, and the LBNP cancels the order with reason **996**.
- **If `/confirm` gets no response, or NACK 66001:** the LBNP retries `/confirm`. If that also fails, it cancels with reason **996**.
- **If the LBNP can't accept `/on_confirm`:** it replies with **NACK 63002**, and the LSP cancels the order with reason **997**.
- **If `/on_confirm` gets no response, or NACK 63001:** the LSP retries `/on_confirm`. If that also fails, it cancels with reason **997**.

### Stage 3: Ready to Ship

The LSP arranges pickup only once the package is packed. The LBNP can say the package is ready in `/confirm`, or later with `/update`.

**Network interaction:**

- **`/update`**: The LBNP sets `ready_to_ship` to `yes` and sends the pickup code, and the AWB number if it generates one.
- **`/on_update`**: The LSP moves the order to **`In-progress`** and the fulfillment to **`Searching-for-Agent`**. It returns the pickup time slot, the AWB number if it generates one, and the shipping labels for the package.

If the package was already ready at `/confirm`, the LSP sends the pickup slot and the shipping labels in `/on_confirm` instead.

### Stage 4: Pickup

The LSP sends unsolicited `/on_status` updates as pickup progresses.

**Network interaction:**

- **`/on_status`**: **`Agent-assigned`**, when a rider is assigned.
- **`/on_status`**: **`Out-for-pickup`**, when the rider sets out for the pickup location.
- **`/on_status`**: **`Order-picked-up`**, once the rider has the package and the pickup code is verified.

If a pickup attempt fails, the LSP reports **`Pickup-failed`** with a reason code, and then **`Pickup-rescheduled`** with the new pickup slot. See [Failed Attempts and NDR](#6-failed-attempts-and-ndr).

### Stage 5: Hubs

**Network interaction:**

- **`/on_status`**: **`In-transit`**, when the package reaches the source hub and starts moving through the LSP's network.
- **`/on_status`**: **`At-destination-hub`**, when the package reaches the hub that serves the delivery location.
- **`/track`** and **`/on_track`**: The LBNP asks where the shipment is. For P2H2P, the LSP returns a tracking URL rather than live GPS coordinates. If tracking isn't enabled for the order yet, the LSP can reply with **NACK 60012**.

### Stage 6: Deliver

**Network interaction:**

- **`/on_status`**: **`Out-for-delivery`**, when the rider sets out for the delivery location.
- **`/on_status`**: **`Order-delivered`**, after the handover, and after the delivery code check if one was set. The order is now **`Completed`**.

If a delivery attempt fails, the LSP reports **`Delivery-failed`**, and the NDR process decides what happens next.

---

## 5. Order and Fulfillment States

Each `/on_confirm`, `/on_update`, `/on_status` and `/on_cancel` carries two states: the **order** state and the **fulfillment** state. On the normal path the fulfillment moves `Pending` → `Searching-for-Agent` → `Agent-assigned` → `Out-for-pickup` → `Order-picked-up` → `In-transit` → `At-destination-hub` → `Out-for-delivery` → `Order-delivered`. A failed pickup adds `Pickup-failed` and `Pickup-rescheduled`, and a failed delivery adds `Delivery-failed` and `Delivery-rescheduled` (see [Failed Attempts and NDR](#6-failed-attempts-and-ndr)). If the buyer declines another attempt, the LSP starts a [Return to Origin](#9-return-to-origin-rto).

When an order is cancelled, both the order and the fulfillment move to `Cancelled`. See [Cancellation](#8-cancellation).

| Fulfillment state | When the LSP sets it | Order state |
| --- | --- | --- |
| `Pending` | The default, from `/on_confirm` | `Created` or `Accepted` |
| `Searching-for-Agent` | After the package is ready to ship | `In-progress` |
| `Agent-assigned` | A rider is assigned | `In-progress` |
| `Out-for-pickup` | The rider is on the way to the pickup | `In-progress` |
| `Pickup-failed` | A pickup was attempted but failed | `In-progress` |
| `Pickup-rescheduled` | The pickup is rescheduled | `In-progress` |
| `Order-picked-up` | The rider picks up the package | `In-progress` |
| `In-transit` | The package is at the source hub | `In-progress` |
| `At-destination-hub` | The package is at the destination hub | `In-progress` |
| `Out-for-delivery` | The rider is on the way to the delivery | `In-progress` |
| `Delivery-failed` | A delivery was attempted but failed | `In-progress` |
| `Delivery-rescheduled` | The delivery is rescheduled | `In-progress` |
| `Order-delivered` | The package is delivered | `Completed` |
| `Cancelled` | The order is cancelled | `Cancelled` |

**Who sets the order state:** the LBNP creates the order as `Created` in `/confirm`, and the LSP returns it as `Accepted` in `/on_confirm`. The LSP never holds an order in `Created`.

---

## 6. Failed Attempts and NDR

Feature `00E`, the pickup and delivery attempt trail, records every failed attempt for intercity orders. A failed delivery starts a **non-delivery report (NDR)**: someone asks the buyer what to do, and the answer decides whether the LSP tries again or returns the package.

Who talks to the end buyer is agreed up front. The LBNP proposes the owner, itself or the LSP, in `/init`, and the LSP confirms it in `/on_init`.

1. The LSP reports the failed attempt: `/on_status` with `Delivery-failed`, and `/on_update` with the attempt and the delay reason code.
2. **If the LBNP owns buyer communication**, it asks the end buyer what to do, for example over WhatsApp, IVR or SMS:
   - **The buyer wants another attempt (BPR):** the LBNP sends `/update` with the BPR and, optionally, a reattempt date. The LSP acknowledges with `/on_update`, reports `Delivery-rescheduled` in `/on_status`, and later `Order-delivered`.
   - **The buyer declines (BNR):** the LBNP sends `/update` with the BNR, and the LSP starts an RTO with `/on_cancel`.
3. **If the LSP owns buyer communication**, it contacts the buyer outside the network and reattempts under its own process.

- **BPR and BNR:** the buyer's positive response and the buyer's negative response.
- **Pickup failures** work the same way: the LSP reports the failed attempt with a reason code and updates the pickup slot.
- The attempt details can arrive in `/on_update` or in `/on_status`.

See **PICKUP DELIVERY ATTEMPT** in the API Walkthrough.

---

## 7. Weight Differential

The LSP may find at a hub that the package is heavier or bigger than declared. Under feature `021`, it charges the difference with an unsolicited update.

1. The LSP sends an unsolicited `/on_update` with the extra charge and its tax, the actual weight and size, and proof images.
2. **If the LBNP accepts**, it replies with an ACK, and the extra charge is added to the shipment's cost.
3. **If the LBNP disagrees**, it replies with **NACK 62504**. The LSP reverts the quote, weight and size, and the agreed terms apply.

- The update can also come in `/on_status`. If the difference changes the RTO charge, the LSP sends it in `/on_cancel`.
- Once accepted, the extra charge can also affect cancellation fees if the order is cancelled later.

See **WEIGHT DIFFERENTIAL FLOW** in the API Walkthrough.

---

## 8. Cancellation

Either side can cancel an order. The LBNP asks with `/cancel`, and the LSP cancels on its own with an unsolicited `/on_cancel`.

- If the reason code isn't valid, the LSP can reply with **NACK 60009**.
- If the LBNP cancels for a missed delivery time (reason **175**) but the LSP hasn't missed it, the LSP can reply with **NACK 60010**.
- `/on_cancel` records the fulfillment's state just before the cancellation (`precancel_state`). Its quote shows the final amount, including any cancellation fee.

See **BUYER SIDE ORDER CANCELLATION**, **SELLER SIDE ORDER CANCELLATION** and, for fees by fulfillment state, **CANCELLATION TERMS FLOW** (feature `01A`).

---

## 9. Return to Origin (RTO)

If the package can't be delivered, for example because the buyer declines it after a failed attempt, the LSP starts an RTO. It sends an unsolicited `/on_cancel` with an RTO reason code.

- **Two fulfillments:** the LSP creates a separate fulfillment of type `RTO`, linked to the delivery fulfillment through the `rto_event` tag. The delivery fulfillment ends in state `RTO`, and the RTO fulfillment starts at `RTO-Initiated`.
- **Order state:** stays as it was (`In-progress`) until the RTO fulfillment reaches `RTO-Disposed` or `RTO-Delivered`. Then the order is `Completed`.
- **Quote:** the RTO charge, the RTO price quoted in `/on_search`, is added to the order's quote. A weight differential can change it too.
- **With or without return:** by default the package is not brought back (`RTO-Disposed`). An LSP that supports **RTO with return** (feature `022`) brings it back to the pickup location (`RTO-Delivered`). The LBNP marks which fulfillments should come back with `return_to_origin` in `/confirm`.
- **Accepting the request:** the LBNP must accept a valid RTO request. Under feature `022`, if the RTO charge differs from the `/on_search` quote, the LBNP can reply with **NACK 62503**, and the LSP must resend the request with the correct charge.
- **E-way bill:** for an RTO fulfillment, the LSP creates a new e-way bill number (feature `019`).
- **Retail order:** when the delivery was booked over ONDC (on-network logistics), the RTO also leads to an `/on_cancel` on the linked retail order.

See **RTO FLOW** and, for verifying the return with an OTP, **STATIC OTP RTO DELIVERY** (feature `00A`).

---

## 10. Reverse QC

When the LSP picks up a returned item, a fulfillment of type `Return`, the rider can check its condition first. This is feature `01B`.

1. In `/confirm`, the LBNP sends the checklist for the `Return` fulfillment: the product details and the questions to answer.
2. At pickup, the rider inspects the item.
3. If the item passes, the LSP reports `Order-picked-up` in `/on_status`, with the rider's answers. If it fails, the LSP reports `Pickup-failed`, also with the rider's answers.

The checklist is the LBNP's quality-check procedure, sent in a fixed, coded format, so the rider's answers can be matched to its questions. See **REVERSE QC** in the API Walkthrough.

---

## 11. Changing an Order

The LBNP uses `/update`, and the LSP replies with `/on_update`, to:

- say the package is ready to ship, and share the AWB number if the LBNP generates it;
- change the delivery instructions;
- change the linked retail order, for example when part of the retail order is cancelled or returned and the weight or items change;
- change how pickup or delivery is verified;
- pass on the buyer's response after a failed delivery attempt (see [Failed Attempts and NDR](#6-failed-attempts-and-ndr)).

---

## 12. Enhanced Features

Enhanced features are optional, so each side tells the other which ones it supports. This is called **feature discovery**.

1. In `/search`, the LBNP lists the feature IDs it supports in the `lbnp_features` tag.
2. In `/on_search`, each LSP lists the feature IDs it supports in the `lsp_features` tag.
3. The LBNP keeps each LSP's list and uses only features that both sides support. If it sends a call that uses a feature the LSP doesn't support, the LSP replies with **NACK 61001**.

If the LSP sends an update that uses a feature the LBNP doesn't support, the LBNP can reply with **NACK 64001**. The **FEATURE DISCOVERY** flow shows the exchange.

| Feature | What It Adds | Flow in the API Walkthrough |
| --- | --- | --- |
| `004` Rate card for P2H2P | A price list by weight slab, with separate Standard and Express rates and separate forward and return rates | RATE CARD (P2H2P) |
| `008` Cash on delivery | The rider collects the order value. Payment terms for the logistics order and the retail order are kept separate. | CASH ON DELIVERY FLOW |
| `009` Static OTP (pickup and delivery) | A fixed OTP, set by the LBNP, that the seller gives at pickup and the buyer gives at delivery | STATIC OTP PICKUP DELIVERY |
| `00A` Static OTP (RTO) | A fixed OTP that the seller gives when an RTO package comes back | STATIC OTP RTO DELIVERY |
| `00D` Payment wallet | Prepaid payment from a wallet the LSP keeps for the LBNP: blocked in `/on_init`, debited in `/on_confirm` | PREPAID PAYMENT FLOW |
| `00E` Pickup and delivery attempt trail | Failed attempts, reason codes and the NDR process | PICKUP DELIVERY ATTEMPT |
| `00F` ePOD | Electronic proof of pickup and delivery, such as a photo, the rider's GPS position or the recipient's name | E-POD |
| `010` Call masking | Contact modes other than a phone number, such as IVR | Call-Masking |
| `014` Seller credentials | Tags orders from specific sellers, for example women-owned or tribal-owned businesses | ORDER FLOW BASE LINE SELLER CREDS |
| `019` E-way bill | Several e-way bills per order. The LBNP sends each item's HSN code and e-way bill exemption, and the seller's GSTIN. | E-WAY BILL |
| `01A` Cancellation terms | Cancellation fees by fulfillment state and reason | CANCELLATION TERMS FLOW |
| `01B` Reverse QC | A quality check on returned items at pickup | REVERSE QC |
| `01C` SLA metrics | Service levels the LBNP defines, with penalties | ORDER FLOW BASE LINE SLA METRICS |
| `01D` Special capabilities | What the LSP can handle, such as fragile or dangerous goods, cold storage, open-box delivery and cash on delivery | ORDER FLOW BASE LINE PUBLIC SPECIAL CAPABILITIES |
| `01E` RCM self-declaration | The LSP's declaration for the GST reverse charge mechanism | ORDER FLOW RCM |
| `01F` Codified static terms | The LSP's standard terms, published in `/on_search` | ORDER FLOW CODIFIED STATIC TERMS |
| `020` Customer support details | Support contacts exchanged in `/confirm` and `/on_confirm` | ORDER FLOW EXCHANGE CUSTOMER SUPPORT DETAILS |
| `021` Differential weight charges | Extra charges when the actual weight or size differs from the declared one | WEIGHT DIFFERENTIAL FLOW |

The API Walkthrough also has **ORDER FLOW B2B** and **B2B ORDER CANCELLATION**, for business-to-business shipments.

---

## 13. Issue and Grievance Management

Either side can raise an issue about an order, for example a delayed, damaged, lost or undelivered shipment. Issues are handled with the IGM APIs.

**Network interaction:**

- **`/issue`**: The LBNP raises an issue for an order, with its category, a description and the expected resolution time.
- **`/on_issue`**: The LSP replies with the actions it has taken and a proposed resolution, and keeps sending updates until the issue is resolved.
- **`/issue`**: The LBNP accepts the resolution or escalates it, and closes the issue.

If an order is cancelled through an issue, the LSP can refer to the resolved issue in `/on_cancel` and in later updates. The API Walkthrough has flows for IGM v1.0.0 and v2.0.0, covering issues that are resolved, rejected or closed with no action.

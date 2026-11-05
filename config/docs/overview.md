# Logistics (P2H2P)

---

## Overview

Point-to-Hub-to-Point (P2H2P) logistics covers shipments that are picked up, routed through one or more hubs, and then delivered. It is the typical model for intercity, courier and B2B shipments, where a package travels over a network of sorting hubs before the last mile.

A seller app that needs a shipment moved searches the network, compares the services and prices that Logistics Service Providers offer, and books one. The provider issues an AWB number and shipping label, picks up the package, moves it through its hub network, and keeps the seller app updated until delivery. ONDC lets seller apps and logistics providers work through one common, open protocol instead of building a separate integration with each other.

---

## Participants

| Participant | What This Means |
|---|---|
| **Logistics Buyer (LBNP)** | The buyer application on the logistics network, usually a retail or B2B seller app that needs a shipment delivered. It searches for logistics services, books one, shares shipment readiness, and tracks the order. Acts as the BAP. |
| **Logistics Service Provider (LSP)** | A courier or logistics provider (or its seller application) offering hub-based delivery on the network. It quotes prices and delivery terms, issues the AWB number and shipping label, moves the shipment through its hubs, and sends status updates. Acts as the BPP. |
| **End customer** | The person or business receiving the shipment. They don't talk to the network directly, but delivery details, delivery attempts and proof of delivery all relate to them. |

---

## How P2H2P Differs from P2P

- **Routing through hubs**: the shipment moves from the pickup location to an origin hub, through the provider's network to a destination hub, and then to the delivery location.
- **AWB number and shipping label**: the LSP shares an AWB (air waybill) number and a shipping label for the package from `/on_confirm` onwards. The Logistics Buyer prints the label and attaches it to the package before pickup.
- **Longer, multi-day timelines**: categories such as Express Delivery and Standard Delivery are common. Hub-related states such as `In-transit`, `At-destination-hub` and `Out-for-delivery` appear in the journey.
- **Failed delivery handling**: P2H2P adds flows for delivery attempts, non-delivery reports (NDR), weight differential and reverse quality check.

---

## The User Journey

The P2H2P journey runs from discovering a delivery service, through booking and hub transit, to the final delivery. It has the following stages:

### 1. Service Discovery

The Logistics Buyer searches for providers that can deliver between the pickup and delivery locations, often in different cities.

**Network interaction:**

- **`/search`**: The LBNP sends the pickup and delivery locations, the package details (such as weight and dimensions), and the requested category.
- **`/on_search`**: Each LSP returns its catalogue: the delivery categories it serves, the price of each option, the expected turnaround time, and the features it supports.

### 2. Order Initialization

**Network interaction:**

- **`/init`**: The LBNP sends the chosen item, the pickup and delivery fulfillment details, billing information and the payment method.
- **`/on_init`**: The LSP returns the final quote, the fulfillment route, the payment terms and the cancellation terms for the order.

### 3. Order Confirmation

**Network interaction:**

- **`/confirm`**: The LBNP confirms the order.
- **`/on_confirm`**: The LSP accepts the order and returns the finalised order with the AWB number and shipping label. The fulfillment state is now **`Pending`**.

### 4. Ready to Ship

Once the package is packed and labelled, the Logistics Buyer tells the LSP.

**Network interaction:**

- **`/update`**: The LBNP marks the shipment as ready to ship.
- **`/on_update`**: The LSP acknowledges it and arranges pickup. The fulfillment state becomes **`Searching-for-Agent`**.

### 5. Pickup, Hub Transit and Delivery

The LSP sends unsolicited status updates as the shipment moves through its network.

**Network interaction:**

- **`/on_status`**: Pickup progress: **`Agent-assigned`**, **`At-pickup`**, **`Order-picked-up`**.
- **`/on_status`**: Hub transit: **`In-transit`** between hubs, then **`At-destination-hub`**.
- **`/track`** and **`/on_track`**: The LBNP can request tracking information for the shipment at any point.
- **`/on_status`**: Last mile: **`Out-for-delivery`**, **`At-delivery`**, and finally **`Order-delivered`**.

The full list of fulfillment states in the spec also includes `Out-for-pickup`, `Pickup-failed`, `Pickup-rescheduled`, `Delivery-failed`, `Delivery-rescheduled` and `Cancelled`.

---

## Additional Scenarios

### 1. Order Cancellation

- **By the buyer**: the LBNP sends **`/cancel`** with the order ID and a reason. The LSP confirms with **`/on_cancel`**, applying the agreed cancellation terms.
- **By the provider**: the LSP sends an unsolicited **`/on_cancel`** with the reason and the updated order.
- **B2B order cancellation** has its own flow.

### 2. Failed Delivery Attempt and NDR

When a pickup or delivery attempt fails, the LSP raises a non-delivery report (NDR) and the end customer's response decides what happens next.

**Network interaction:**

- **`/on_update`**: The LSP reports the failed attempt with a reason code, and any delay to the fulfillment.
- **`/update`**: The LBNP passes on the end customer's response, for example a request to re-attempt delivery.
- **`/on_update`**: The LSP acknowledges the response. It then either re-attempts delivery or moves to RTO.

### 3. Return to Origin (RTO)

When a delivery can't be completed, the shipment is returned to the pickup location.

**Network interaction:**

- **`/on_cancel`**: The LSP cancels the forward delivery and creates a linked **RTO** fulfillment in state **`RTO-Initiated`**.
- **`/on_status`**: The LSP reports RTO progress until the package is **`RTO-Delivered`** back to the origin, or **`RTO-Disposed`**.

### 4. Reverse Quality Check (Reverse QC)

For failed deliveries where goods have to go back to the logistics hub, for example because the buyer is unavailable, the Reverse QC flow covers the return order and its status updates.

### 5. Weight Differential

When the actual weight of the shipment differs from the declared weight, the LSP charges the difference.

**Network interaction:**

- **`/on_update`**: The LSP reports the weight discrepancy and the differential charge.
- **`/update`** and **`/on_update`**: The order and quote are updated with the adjusted charges.

### 6. Other Supported Flows

The spec also covers:

- **B2B orders**
- **Rate card**: `/search` and `/on_search` only, to fetch prices.
- **Cash on delivery**
- **Prepaid payment**: a wallet that the Logistics Buyer prepays.
- **Electronic proof of delivery (e-POD)**
- **E-way bill**
- **Static OTP**: OTP verification at pickup, delivery and RTO.
- **Call masking**
- **SLA metrics**
- **Codified static terms**
- **Exchange of customer support details**
- **Seller credentials**
- **Reverse charge mechanism (RCM)**

Each one has its own flow in the API Walkthrough.

---

## Issue and Grievance Management

Either side can raise an issue against an order, for example a delayed, damaged, lost or undelivered shipment. The resolution is handled through the IGM APIs.

**Network interaction:**

- **`/issue`**: The LBNP raises an issue for an order, with its category, a description and the expected resolution time.
- **`/on_issue`**: The LSP responds with the actions taken and a proposed resolution. It keeps sending updates until the issue is resolved.
- **`/issue`**: The LBNP accepts or escalates the resolution, and closes the issue.

The spec includes flows for IGM v1.0.0 and v2.0.0. These cover issues that are resolved, rejected, or closed with no action.

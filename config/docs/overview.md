# Logistics (P2P)

---

## Overview

Point-to-Point (P2P) logistics covers shipments that move directly from a pickup location to a delivery location, without being routed through a hub. It is the typical model for hyperlocal and intracity deliveries, such as food, grocery and other retail orders that a seller app needs delivered to a customer.

A seller app that needs a delivery searches the network, compares the delivery options and prices that Logistics Service Providers offer, and books the one it wants. The provider then assigns an agent, picks up the package, and keeps the seller app updated until delivery. ONDC lets seller apps and logistics providers work through one common, open protocol instead of building a separate integration with each other.

---

## Participants

| Participant | What This Means |
|---|---|
| **Logistics Buyer (LBNP)** | The buyer application on the logistics network, usually a retail seller app that needs a shipment delivered. It searches for logistics services, books one, shares shipment readiness, and tracks the order. Acts as the BAP. |
| **Logistics Service Provider (LSP)** | A logistics provider (or its seller application) offering delivery services on the network. It quotes prices and delivery terms, assigns delivery agents, picks up and delivers the shipment, and sends status updates. Acts as the BPP. |
| **End customer** | The person receiving the shipment. They don't talk to the network directly, but delivery details, OTPs and proof of delivery all relate to them. |

---

## Delivery Categories

The LSP returns its services as categories in the catalogue. The spec supports:

- **Immediate Delivery**: hyperlocal, within minutes.
- **Instant Delivery**
- **Same Day Delivery**
- **Next Day Delivery**
- **Express Delivery**
- **Standard Delivery**

Each order has a **Delivery** fulfillment. If the shipment can't be delivered, a linked **RTO** (Return to Origin) fulfillment brings it back to the pickup location.

---

## The User Journey

The P2P journey runs from discovering a delivery service, through booking, to the final delivery. It has the following stages:

### 1. Service Discovery

The Logistics Buyer searches for providers that can deliver between the pickup and drop-off locations.

**Network interaction:**

- **`/search`**: The LBNP sends the pickup and drop-off locations, the package details (such as weight and dimensions), and the requested category.
- **`/on_search`**: Each LSP returns its catalogue: the delivery categories it serves, the price of each option, the expected turnaround time, and the features it supports.

### 2. Order Initialization

The Logistics Buyer picks a delivery option and shares the order details.

**Network interaction:**

- **`/init`**: The LBNP sends the chosen item, the pickup and delivery fulfillment details, billing information and the payment method.
- **`/on_init`**: The LSP returns the final quote, the fulfillment details, the payment terms and the cancellation terms for the order.

### 3. Order Confirmation

**Network interaction:**

- **`/confirm`**: The LBNP confirms the order.
- **`/on_confirm`**: The LSP accepts the order and returns the finalised order. The fulfillment state is now **`Pending`**.

### 4. Ready to Ship

Once the package is packed and ready for pickup, the Logistics Buyer tells the LSP.

**Network interaction:**

- **`/update`**: The LBNP marks the shipment as ready to ship.
- **`/on_update`**: The LSP acknowledges it and starts looking for an agent. The fulfillment state becomes **`Searching-for-Agent`**.

### 5. Pickup

The LSP sends unsolicited status updates as the pickup progresses.

**Network interaction:**

- **`/on_status`**: **`Agent-assigned`**, after an agent accepts the job.
- **`/on_status`**: **`At-pickup`**, when the agent reaches the pickup location.
- **`/on_status`**: **`Order-picked-up`**, after the agent collects the package.

### 6. In Transit and Tracking

While the shipment is moving, the Logistics Buyer can ask for its live location.

**Network interaction:**

- **`/track`**: The LBNP requests tracking information for the order.
- **`/on_track`**: The LSP returns tracking information for the shipment.

### 7. Delivery

**Network interaction:**

- **`/on_status`**: **`At-delivery`**, when the agent reaches the delivery location.
- **`/on_status`**: **`Order-delivered`**, after the package is handed over. The order is now complete.

The full list of fulfillment states in the spec also includes `Out-for-pickup`, `Pickup-failed`, `Pickup-rescheduled`, `In-transit`, `At-destination-hub`, `Out-for-delivery`, `Delivery-failed`, `Delivery-rescheduled` and `Cancelled`.

---

## Additional Scenarios

### 1. Order Cancellation by the Buyer

**Network interaction:**

- **`/cancel`**: The LBNP cancels a confirmed order, sending the order ID and a cancellation reason.
- **`/on_cancel`**: The LSP confirms the cancellation and returns the final order, including any cancellation charges under the agreed cancellation terms.

### 2. Order Cancellation by the Provider

The LSP can cancel an order itself, for example when no agent is available.

**Network interaction:**

- **`/on_cancel`** (unsolicited): The LSP notifies the LBNP that the order is cancelled, with the reason and the updated fulfillment and payment details.

### 3. Return to Origin (RTO)

When a delivery fails or the customer refuses the package, the shipment is returned to the pickup location.

**Network interaction:**

- **`/on_cancel`**: The LSP cancels the forward delivery and creates a linked **RTO** fulfillment in state **`RTO-Initiated`**.
- **`/on_status`**: The LSP reports RTO progress until the package is **`RTO-Delivered`** back to the origin, or **`RTO-Disposed`**.

### 4. Update Delivery Address

**Network interaction:**

- **`/update`**: The LBNP sends the updated delivery address for a confirmed order.
- **`/on_update`**: The LSP confirms the change and returns the revised fulfillment details. Delivery then continues as normal.

### 5. Cash on Delivery

The agent collects payment from the customer at delivery. The order follows the normal journey, with the COD terms agreed in the order and the collected amount settled with the Logistics Buyer.

### 6. Surge Fee

When operating conditions change, for example due to bad weather or high demand, the LSP can add a surge fee.

**Network interaction:**

- **`/update`** and **`/on_update`**: The order is updated with the surge charge the LSP added, and the revised quote is confirmed.

### 7. Other Supported Flows

The spec also covers:

- **Rate card**: `/search` and `/on_search` only, to fetch prices.
- **Prepaid payment**: a wallet that the Logistics Buyer prepays.
- **Electronic proof of delivery (e-POD)**
- **E-way bill**
- **Static OTP**: OTP verification at pickup, delivery and RTO.
- **Call masking**: privacy-protected calls between the agent and the customer.
- **Quick commerce**
- **FIFO**: first-in, first-out dispatch.
- **SLA metrics**
- **Codified static terms**
- **Exchange of customer support details**
- **Seller credentials**
- **Seller and buyer instructions**
- **Reverse charge mechanism (RCM)**

Each one has its own flow in the API Walkthrough.

---

## Issue and Grievance Management

Either side can raise an issue against an order, for example a delayed, damaged or undelivered shipment. The resolution is handled through the IGM APIs.

**Network interaction:**

- **`/issue`**: The LBNP raises an issue for an order, with its category, a description and the expected resolution time.
- **`/on_issue`**: The LSP responds with the actions taken and a proposed resolution. It keeps sending updates until the issue is resolved.
- **`/issue`**: The LBNP accepts or escalates the resolution, and closes the issue.

The spec includes flows for IGM v1.0.0 and v2.0.0. These cover issues that are resolved, rejected, or closed with no action.

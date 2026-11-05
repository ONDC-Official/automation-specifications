# Logistics (NIC2004:60232)

---

## Overview

This is version 1.2.0 of the ONDC logistics specification, published under the domain code `nic2004:60232`. It covers delivery services that a seller app books from a logistics provider: both direct **Point-to-Point (P2P)** deliveries, typical for hyperlocal and intracity orders, and **Point-to-Hub-to-Point (P2H2P)** shipments routed through hubs.

A seller app that needs a delivery searches the network, compares the services and prices that Logistics Service Providers offer, and books one. The provider then assigns an agent, picks up the package, and keeps the seller app updated until delivery. ONDC lets seller apps and logistics providers work through one common, open protocol instead of building a separate integration with each other.

> Version 1.2.5 splits this domain into **ONDC:LOG10** (P2P) and **ONDC:LOG11** (P2H2P), and adds many more flows. New integrations should check which version their counterparties support.

---

## Participants

| Participant | What This Means |
|---|---|
| **Logistics Buyer (LBNP)** | The buyer application on the logistics network, usually a retail seller app that needs a shipment delivered. It searches for logistics services, books one, shares shipment readiness, and tracks the order. Acts as the BAP. |
| **Logistics Service Provider (LSP)** | A logistics provider (or its seller application) offering delivery services on the network. It quotes prices and delivery terms, assigns delivery agents, picks up and delivers the shipment, and sends status updates. Acts as the BPP. |
| **End customer** | The person receiving the shipment. They don't talk to the network directly, but delivery details and proof of delivery relate to them. |

---

## Services and Pricing

- **Delivery categories**: the spec supports Immediate Delivery, Same Day Delivery, Next Day Delivery, Express Delivery and Standard Delivery.
- **Delivery type**: each item's `descriptor.code` says whether the service is **P2P** or **P2H2P**.
- **RTO quote**: in `/on_search`, the LSP quotes the Return to Origin charge as a separate item linked to the delivery item through `parent_item_id`. The Logistics Buyer knows the RTO cost up front.
- **Fulfillments**: each order has a **Delivery** fulfillment. If the shipment can't be delivered, a linked **RTO** fulfillment brings it back to the pickup location.
- **AWB number**: the order carries an AWB number from `/confirm` onwards, so the shipment can be identified throughout.

---

## The User Journey

The journey runs from discovering a delivery service, through booking, to the final delivery. It has the following stages:

### 1. Service Discovery

**Network interaction:**

- **`/search`**: The LBNP sends the pickup and delivery locations, the package details (such as weight and dimensions), and the requested category.
- **`/on_search`**: Each LSP returns its catalogue: the categories and delivery types it serves, the price of each option, the linked RTO quote, and the expected turnaround time.

### 2. Order Initialization

**Network interaction:**

- **`/init`**: The LBNP sends the chosen item, the pickup and delivery fulfillment details, billing information and the payment method.
- **`/on_init`**: The LSP returns the final quote, the fulfillment details, the payment terms and the cancellation terms for the order.

### 3. Order Confirmation

**Network interaction:**

- **`/confirm`**: The LBNP confirms the order. Here it states whether the shipment is already ready to ship (`ready_to_ship`), and whether it should be returned to origin if delivery fails.
- **`/on_confirm`**: The LSP accepts the order and returns the finalised order with the AWB number. The fulfillment state is now **`Pending`**.

### 4. Ready to Ship

If the package wasn't ready at confirmation, the Logistics Buyer tells the LSP once it is packed.

**Network interaction:**

- **`/update`**: The LBNP tags the pickup fulfillment as `ready_to_ship`, so the order can be assigned to an agent.
- **`/on_update`**: The LSP acknowledges it and returns the revised order. The fulfillment state becomes **`Searching-for-Agent`**.

If the shipment was marked ready to ship at `/confirm`, this step is skipped. The spec covers that case as a separate flow (**ORDER_FLOW_BASELINE (without rts)**), where the order moves straight to status updates.

### 5. Pickup, Tracking and Delivery

The LSP sends unsolicited status updates as the shipment progresses.

**Network interaction:**

- **`/on_status`**: **`Agent-assigned`**, after an agent accepts the job.
- **`/on_status`**: **`Order-picked-up`**, after the agent collects the package.
- **`/track`** and **`/on_track`**: The LBNP requests tracking information for the shipment, and the LSP returns it.
- **`/on_status`**: **`Out-for-delivery`**, during the last mile.
- **`/on_status`**: **`Order-delivered`**, after the package is handed over. The order is now complete.

---

## Additional Scenarios

### 1. Order Cancellation by the Buyer

**Network interaction:**

- **`/cancel`**: The LBNP cancels a confirmed order, sending the order ID and a cancellation reason.
- **`/on_cancel`**: The LSP confirms the cancellation and returns the order in the **`Cancelled`** state, applying the agreed cancellation terms.

### 2. Return to Origin (RTO)

When a delivery can't be completed, the shipment is returned to the pickup location.

**Network interaction:**

- **`/on_status`**: The order progresses as normal up to **`Out-for-delivery`**.
- **`/on_cancel`** (unsolicited): Delivery fails, so the LSP cancels the forward delivery with an RTO reason code and a revised quote that includes the RTO charge. It also creates the linked **RTO** fulfillment in state **`RTO-Initiated`**.
- **`/on_status`**: The LSP reports the RTO leg as **`RTO-Delivered`** once the shipment is handed back at the pickup location.

---

## Issue and Grievance Management

Either side can raise an issue against an order, for example a delayed, damaged or undelivered shipment. This version uses **IGM v1.0.0**.

**Network interaction:**

- **`/issue`**: The LBNP raises an issue for an order, with its category, a description and the expected resolution time.
- **`/on_issue`**: The LSP responds with the actions taken and a proposed resolution.
- **`/on_issue_status`** (unsolicited): The LSP sends status updates on the resolution.
- **`/issue`**: The LBNP accepts the resolution and closes the issue, or escalates it.

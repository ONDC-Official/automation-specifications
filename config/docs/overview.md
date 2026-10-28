# Retail Grocery (ONDC:RET10)

- [Overview](#overview)
- [Participants](#participants)
- [The User Journey](#the-user-journey)
  - [1. Discovery and Catalog Search](#1-discovery-and-catalog-search)
  - [2. Item Selection and Serviceability Check](#2-item-selection-and-serviceability-check)
  - [3. Order Initialization and Delivery Configuration](#3-order-initialization-and-delivery-configuration)
  - [4. Order Confirmation and Payment](#4-order-confirmation-and-payment)
  - [5. Order Processing and Packaging](#5-order-processing-and-packaging)
  - [6. Logistics and Rider Assignment](#6-logistics-and-rider-assignment)
  - [7. Order Dispatch, Live Tracking, and Delivery](#7-order-dispatch-live-tracking-and-delivery)
  - [8. Settlement and Post-Fulfillment](#8-settlement-and-post-fulfillment)
- [Additional Scenarios](#additional-scenarios)
  - [1. Buyer-Side Order Cancellation](#1-buyer-side-order-cancellation)
  - [2. Merchant-Side Part-Cancellation and Return to Origin (RTO)](#2-merchant-side-part-cancellation-and-return-to-origin-rto)
  - [3. Buyer-Initiated Return and Refund (Full & Partial)](#3-buyer-initiated-return-and-refund-full--partial)
  - [4. Out of Stock and Inventory Exceptions](#4-out-of-stock-and-inventory-exceptions)
  - [5. Buyer-Managed Delivery / Self-Pickup Fulfillment](#5-buyer-managed-delivery--self-pickup-fulfillment)
  - [6. Incremental Catalog Refresh (Push and Pull)](#6-incremental-catalog-refresh-push-and-pull)
  - [7. Statutory Compliance and Catalog Validation](#7-statutory-compliance-and-catalog-validation)
- [Issue and Grievance Management](#issue-and-grievance-management)
  - [1. IGM 1.0.0 Architecture](#1-igm-100-architecture)
  - [2. IGM 2.0.0 Architecture](#2-igm-200-architecture)
- [Detailed Protocol Flows](#detailed-protocol-flows)
  - [Flow 1: Order to Confirm to Fulfillment (Prepaid Standard Delivery)](#flow-1-order-to-confirm-to-fulfillment-prepaid-standard-delivery)
  - [Flow 2: Buyer Delivery / Buyer-Managed Logistics](#flow-2-buyer-delivery--buyer-managed-logistics)
  - [Flow 3: Buyer-Side Order Cancellation](#flow-3-buyer-side-order-cancellation)
  - [Flow 4: Merchant-Side Part-Order Cancellation and Return to Origin (RTO)](#flow-4-merchant-side-part-order-cancellation-and-return-to-origin-rto)
  - [Flow 5: Buyer-Initiated Return (Full Order and Partial Order)](#flow-5-buyer-initiated-return-full-order-and-partial-order)
  - [Flow 6: Out of Stock Error Handling (Inventory Shortage)](#flow-6-out-of-stock-error-handling-inventory-shortage)
  - [Flow 7: Search and Custom Menu – Full Catalog City Discovery](#flow-7-search-and-custom-menu--full-catalog-city-discovery)
  - [Flow 8: Search and Custom Menu – Incremental Catalog Push](#flow-8-search-and-custom-menu--incremental-catalog-push)
  - [Flow 9: Discovery Flow – Incremental Catalog Refresh Pull](#flow-9-discovery-flow--incremental-catalog-refresh-pull)
  - [Flow 10: Catalog Rejection Flow – Compliance Discrepancy](#flow-10-catalog-rejection-flow--compliance-discrepancy)
  - [Flow 11: Order to Confirm with IGM 1.0.0 Resolution](#flow-11-order-to-confirm-with-igm-100-resolution)
  - [Flow 12: Order to Confirm with IGM 2.0.0 – Resolution Accepted (No Action)](#flow-12-order-to-confirm-with-igm-200--resolution-accepted-no-action)
  - [Flow 13: Order to Confirm with IGM 2.0.0 – Rejection, Escalation & Return](#flow-13-order-to-confirm-with-igm-200--rejection-escalation--return)
  - [Flow 14: Order to Confirm with IGM 2.0.0 – Resolution & Item Replacement](#flow-14-order-to-confirm-with-igm-200--resolution--item-replacement)

---

## Overview

The Grocery domain (**ONDC:RET10**) enables digital commerce for groceries, fresh fruits and vegetables, packaged commodities, dairy, staples, and daily household essentials across the Open Network for Digital Commerce (ONDC). Retail grocery transactions are characterized by hyperlocal discovery, fast turnaround fulfillment, perishable and packaged commodity statutory requirements (FSSAI and Legal Metrology / Packaged Commodities Rules 2011), frequent inventory fluctuations, and complex post-fulfillment lifecycles (partial cancellations, returns, liquidations, and Return-to-Origin).

ONDC unbundles the traditional e-commerce grocery ecosystem. Buyers use their preferred **Buyer Application (BAP)** to discover sellers, compare prices, check delivery serviceability, and manage orders. Sellers list their store inventories through a **Seller Application (BPP)**, maintaining complete autonomy over their inventory, pricing, packaging, and fulfillment policies. Logistics can be fulfilled either by the seller's integrated logistics partner, by an on-network Logistics Service Provider (LSP), or directly via buyer-managed delivery.

The protocol standardizes all network interactions across discovery (`/search`, `/on_search`), ordering (`/select`, `/on_select`, `/init`, `/on_init`, `/confirm`, `/on_confirm`), post-order tracking (`/status`, `/on_status`, `/track`, `/on_track`), fulfillment servicing (`/update`, `/on_update`, `/cancel`, `/on_cancel`), and grievance redressal (IGM 1.0.0 and 2.0.0).

---

## Participants

| Participant | What This Means |
|---|---|
| **Buyer Application (BAP)** | The consumer-facing application (e.g. consumer e-commerce apps, UPI apps, chat apps, telco apps) where consumers browse grocery catalogs, configure delivery addresses, build shopping carts, pay for orders, track delivery riders, and raise grievances. |
| **Seller Application (BPP)** | An application representing grocery retailers, supermarkets, kirana stores, or Direct-to-Consumer (D2C) brands. The BPP publishes item catalogs, validates delivery serviceability, computes tax/delivery quotes, manages order confirmation, coordinates warehouse/store picking and packing, and handles returns or cancellations. |
| **Logistics Service Provider (LSP)** | A delivery network participant that provides hyperlocal or intercity fulfillment. In Seller-managed logistics, the BPP coordinates with the LSP; in Buyer-managed delivery (`Buyer_Delivery`), the BAP coordinates logistics and transmits delivery tracking updates back to the BPP. |
| **Gateway** | The ONDC routing infrastructure that multicasts broadcast discovery requests (`/search`) from BAPs to active seller applications (BPPs) based on domain code, geolocation, or city code. |

---

## The User Journey

The standard grocery ordering journey enables a consumer to discover local grocery stores, evaluate delivery estimates and item prices, configure delivery coordinates, make payment, and receive goods with real-time tracking.

### 1. Discovery and Catalog Search

The buyer initiates discovery on the BAP by searching for grocery items, stores, or categories (e.g. "Atta", "Fruits and Vegetables", "Dairy"):

- **Intent Broadcast**: The BAP transmits a `/search` request specifying the domain category (`ONDC:RET10`), buyer location (GPS coordinates and pincode/area code), and fulfillment type (`Delivery` or `Self-Pickup`).
- **Catalog Delivery**: Active BPPs within the serviceable area respond via asynchronous `/on_search` payloads containing their store catalog (`bpp/providers[]`). This includes items, images, MRP, selling price, unitized measure (e.g., 1 kg, 500 g), stock availability, serviceability tags, and statutory packaged commodity details (manufacturer name, address, packaging date, consumer care details).

### 2. Item Selection and Serviceability Check

The buyer selects items from a specific grocery provider and adds them to their cart:

- **Network interaction:**
  - **`/select` (BAP -> BPP)**: The BAP transmits the selected items (`order.items[]`), quantities, provider location ID, and destination GPS coordinates (`fulfillments[0].end.location.gps` and `address.area_code`).
  - **`/on_select` (BPP -> BAP)**: The seller validates real-time inventory and delivery serviceability. The seller returns an itemized price quote (`quote.breakup[]`) breaking down item costs, delivery charges, packaging fees, applicable taxes (CGST/SGST), and estimated turnaround time (`@ondc/org/TAT`). If items are unavailable, the seller returns appropriate error codes (e.g. `40002` or `30009` for Out of Stock).

### 3. Order Initialization and Delivery Configuration

The buyer provides finalized delivery and billing details:

- **Network interaction:**
  - **`/init` (BAP -> BPP)**: The BAP sends the buyer's full street address, contact details (phone, email), billing address, and selected payment method preferences.
  - **`/on_init` (BPP -> BAP)**: The seller freezes the order quote, specifies static/dynamic terms (cancellation terms, return windows, credit terms), sets payment collection rules (e.g., BAP-collected prepaid payment or Pay-on-Delivery), and returns settlement fee details.

### 4. Order Confirmation and Payment

The buyer completes digital payment (or selects Cash on Delivery):

- **Network interaction:**
  - **`/confirm` (BAP -> BPP)**: The BAP captures payment, generates the formal order record (`order.id`), and transmits payment confirmation parameters (`payment.params.transaction_id`, `payment.status = "PAID"`).
  - **`/on_confirm` (BPP -> BAP)**: The seller validates payment, records the order in its Point of Sale / Order Management System (POS/OMS), marks `order.state = "Created"`, and sets initial fulfillment state to `"Pending"`.

### 5. Order Processing and Packaging

The seller's store or warehouse team picks the ordered grocery items from shelves and packs them:

- **`on_status (Accepted)` (BPP -> BAP)**: An unsolicited status update indicating the merchant has reviewed and accepted the grocery order (`order.state = "Accepted"`).
- **`on_status (Packed)` (BPP -> BAP)**: An unsolicited status update confirming all grocery items have been picked, weighed, verified, and bagged into parcels ready for pickup (`fulfillment.state = "Packed"`, `order.state = "In-progress"`).

### 6. Logistics and Rider Assignment

A delivery partner or store rider is assigned to the fulfillment:

- **`on_status (Agent-assigned)` (BPP -> BAP)**: The seller sends an unsolicited update once a delivery executive accepts the trip. The payload provides delivery rider credentials (`fulfillments[0].agent.name`, `agent.phone`) so the buyer can contact the delivery agent.

### 7. Order Dispatch, Live Tracking, and Delivery

The delivery executive collects the packed groceries from the store and transports them to the buyer's address:

- **`on_status (Order-picked-up)` (BPP -> BAP)**: The seller notifies the BAP that the parcel has left the merchant premises (`fulfillment.state = "Order-picked-up"`), recording `fulfillments[0].start.time.timestamp`.
- **`/track` & `/on_track` (BAP $\leftrightarrow$ BPP)**: The BAP polls for live GPS telemetry of the delivery executive, receiving active tracking URLs and location coordinates.
- **`on_status (Out-for-delivery)` (BPP -> BAP)**: Triggered when the rider enters the destination neighborhood.
- **`on_status (Order-delivered)` (BPP -> BAP)**: Sent upon successful physical handover of grocery items at the buyer's door (`fulfillment.state = "Order-delivered"`, `order.state = "Completed"`), recording `fulfillments[0].end.time.timestamp` and electronic proof of delivery (ePOD / delivery OTP verification).

### 8. Settlement and Post-Fulfillment

Post-delivery, the network transaction proceeds to financial reconciliation. The BAP releases funds to the seller according to the agreed settlement window (T+1 / T+2), withholding agreed buyer finder fees and routing statutory tax deductions where applicable.

---

## Additional Scenarios

Grocery retail involves dynamic operational conditions that diverge from the happy path. The protocol handles the following standard edge cases and operational workflows.

### 1. Buyer-Side Order Cancellation

A buyer may cancel an order before the seller has dispatched the goods (subject to the merchant's cancellation terms):

- **Network interaction:**
  - **`/cancel` (BAP -> BPP)**: The BAP transmits a cancellation request with a standard ONDC cancellation reason code (e.g. `001` for buyer change of mind, `003` for delayed delivery estimate).
  - **`/on_cancel` (BPP -> BAP)**: The seller validates that the order is within the cancellable window (`@ondc/org/cancellable = true`). The seller terminates fulfillment, updates `order.state = "Cancelled"`, recalculates any applicable fee deductions, and provides refund instructions.

### 2. Merchant-Side Part-Cancellation and Return to Origin (RTO)

Hyperlocal grocery fulfillment frequently encounters situations where a seller is partially out of stock during picking, or where a delivery executive cannot reach the consumer:

- **Partial Cancellation (`on_update`)**: If one item in a multi-item basket is missing or damaged prior to dispatch, the merchant issues an unsolicited `/on_update` with `quote.breakup` adjusted to reflect the partial cancellation. The BAP responds with `/update` containing the updated settlement trail to credit the differential refund.
- **Return to Origin (`on_cancel_rto`)**: When a rider arrives at the destination but the customer is unreachable or refuses delivery, the BPP triggers an unsolicited `/on_cancel` with cancellation reason codes `011`–`015` (RTO initiated). The fulfillment transitions to `RTO-Initiated` -> `RTO-Delivered` once the items are returned to the merchant's store.

### 3. Buyer-Initiated Return and Refund (Full & Partial)

For perishable or packaged grocery items that are damaged, expired, incorrect, or missing:

- **Initiation (`/update`)**: Within the return window (`@ondc/org/return_window`, e.g. `P7D` for packaged staples, `P1D` for produce), the buyer submits a return request specifying the item ID, quantity, return reason code (e.g. `001` for damaged goods), and photographic evidence.
- **Approval & Pickup (`on_update`)**: The merchant reviews the return request, approves it (`return_approved`), dispatches a reverse-logistics agent to inspect and collect the item (`return_picked`), and marks it `return_delivered` upon receipt at the store.
- **Refund Settlement (`update_settlement_trail`)**: The BAP transmits a settlement trail update specifying the refund amount, beneficiary details, and payment transaction ID.

### 4. Out of Stock and Inventory Exceptions

When a consumer selects grocery items whose inventory has just been depleted by an in-store shopper:

- **Error Response (`on_select`)**: The seller returns an error block containing ONDC error code `40002` (Out of Stock) or `30009` along with descriptor details.
- **Cart Reconfiguration**: The BAP renders the out-of-stock notification to the buyer, allowing them to adjust item quantities or substitute brands before retrying the `/select` sequence.

### 5. Buyer-Managed Delivery / Self-Pickup Fulfillment

In scenarios where the buyer application orchestrates logistics or the buyer chooses in-store pickup:

- **Buyer Logistics (`Buyer_Delivery`)**: The order is confirmed without seller logistics. Once the seller packs the order (`on_status_packed`), the BAP initiates pickup via its own delivery partner, notifying the seller of pickup progress via `/update` (`update_buyer_delivery_intermin` and `update_buyer_delivery_final`), with the seller acknowledging via `/on_update`.

### 6. Incremental Catalog Refresh (Push and Pull)

Grocery store inventories and prices change dynamically throughout the day:

- **Incremental Push (`Search_and_Custom_Menu_Incremental_Push`)**: The seller actively broadcasts real-time price updates, out-of-stock toggles, or store open/close events (`serviceability` enable/disable) via unsolicited `/on_search` payloads without waiting for consumer queries.
- **Incremental Pull (`Discovery_Flow_incremental_catalog_refresh_pull`)**: The buyer application polls the seller for catalog changes that occurred since a specific timestamp (`last_updated_at`), minimizing network bandwidth while keeping local caches synchronized.

### 7. Statutory Compliance and Catalog Validation

Packaged grocery goods are strictly regulated under the Legal Metrology Act and FSSAI:

- **Catalog Rejection (`Catalog_Rejection_Flow`)**: If a seller's `/on_search` catalog omits mandatory statutory requirements (Packaged Commodities declaration, manufacturer name, net weight, ingredients, nutritional information, or valid FSSAI license numbers), the buyer app rejects the catalog via `catalog_rejection` to prevent non-compliant listings from being displayed to consumers.

---

## Issue and Grievance Management

The grocery domain supports robust complaint handling across both ONDC Issue and Grievance Management (IGM) framework versions.

### 1. IGM 1.0.0 Architecture

In IGM 1.0.0, grievances follow a linear status progression:
1. **`issue (open)` (BAP -> BPP)**: The buyer files an issue against an order or item (e.g., "Item spoiled or leaking"), categorizing it as `ISSUE`, providing descriptions, photos, and complainant details.
2. **`on_issue (processing)` (BPP -> BAP)**: The seller acknowledges receipt of the complaint, providing a grievance ticket ID, respondent details, and expected Resolution Time (TAT).
3. **`on_issue_status (resolved)` (BPP -> BAP)**: The seller investigates and publishes a formal resolution (e.g. `REFUND`, `REPLACEMENT`, or `NO_ACTION`) with resolution remarks.
4. **`issue (close)` (BAP -> BPP)**: The buyer reviews the resolution and closes the grievance ticket.

### 2. IGM 2.0.0 Architecture

IGM 2.0.0 introduces multi-party interactions, evidence exchange, dispute escalation, and automated settlement linkages:
- **Clarification & Information Exchange**: The seller can request additional evidence (`on_issue_need_more_info`), and the buyer can respond with supplementary photos or explanations (`issue_info_provided`).
- **Resolution Acceptance & Rejection**: The complainant can formally accept or reject proposed resolutions.
- **Dispute Escalation**: If dissatisfied, the buyer can escalate the issue from Level 1 (Inter-party Grievance) to Level 2 (Grievance Redressal Officer / ODR Platform).
- **Downstream Actions**: Upon resolution approval, the seller automatically issues corrective fulfillment actions, such as an item replacement (`on_update_igm_replacement`) or refund return (`on_update_igm_return`).

---

## Detailed Protocol Flows

### Flow 1: Order to Confirm to Fulfillment (Prepaid Standard Delivery)

#### 1. Short Description
The primary forward-fulfillment grocery purchase journey. A buyer selects grocery items, receives an itemized quote with delivery fees and taxes, provides shipping addresses, pays upfront, and receives the goods through seller-managed delivery with live rider tracking and delivery verification.

#### 2. API Breakdown & Technical Actions
- **`/select` (BAP -> BPP)**: The BAP transmits selected item IDs (`I1`, `I2`), quantities, store location (`L1`), and delivery coordinates (`fulfillments[0].end.location.gps` and `address.area_code = "560001"`).
- **`/on_select` (BPP -> BAP)**: The BPP validates store inventory and delivery radius. It returns an itemized price quote (`quote.breakup[]`) with base prices, delivery fees (`@ondc/org/title_type="delivery"`), packaging charges, and delivery turnaround time (`@ondc/org/TAT = "PT45M"`).
- **`/init` (BAP -> BPP)**: The buyer confirms the cart and inputs their full shipping destination (building, street, city, pin code) and billing details.
- **`/on_init` (BPP -> BAP)**: The BPP freezes the order quote, publishes settlement terms, and provides payment collection instructions.
- **`/confirm` (BAP -> BPP)**: The BAP collects payment digitally, binds the transaction with `payment.status = "PAID"`, and sends the final order commitment.
- **`/on_confirm` (BPP -> BAP)**: The BPP confirms order acceptance, assigning an official `order.id` with state `Created` and fulfillment state `Pending`.
- **`on_status (on_status_accepted)` [Unsolicited] (BPP -> BAP)**: Merchant marks order as accepted for fulfillment (`order.state = "Accepted"`).
- **`on_status (on_status_packed)` [Unsolicited] (BPP -> BAP)**: Merchant picks and packs items into bags ready for courier dispatch (`fulfillment.state = "Packed"`, `order.state = "In-progress"`).
- **`on_status (on_status_agent_assigned)` [Unsolicited] (BPP -> BAP)**: Delivery executive assigned; payload includes rider name and mobile number.
- **`on_status (on_status_picked)` [Unsolicited] (BPP -> BAP)**: Rider picks up package from store (`fulfillment.state = "Order-picked-up"`, with pickup timestamp).
- **`/track` & `/on_track` (BAP $\leftrightarrow$ BPP)**: BAP requests live tracking URL / websocket endpoint for real-time rider map display.
- **`on_status (on_status_out_for_delivery)` [Unsolicited] (BPP -> BAP)**: Rider is approaching buyer's premises (`fulfillment.state = "Out-for-delivery"`).
- **`on_status (on_status_order_delivered)` [Unsolicited] (BPP -> BAP)**: Package successfully delivered with delivery timestamp and electronic proof of delivery (`fulfillment.state = "Order-delivered"`, `order.state = "Completed"`).

---

### Flow 2: Buyer Delivery / Buyer-Managed Logistics

#### 1. Short Description
Used when the Buyer Application manages delivery or coordinates self-pickup. The seller prepares and packs the grocery items, after which the buyer application dispatches its own delivery partner, continuously updating the seller on pickup, transit, and delivery completion.

#### 2. API Breakdown & Technical Actions
- **`/select` -> `/on_select` -> `/init` -> `/on_init` -> `/confirm` -> `/on_confirm`**: Standard ordering sequence establishing store pickup fulfillment.
- **`on_status (on_status_pending)` [Unsolicited] (BPP -> BAP)**: Seller acknowledges order in queue.
- **`on_status (on_status_packed)` [Unsolicited] (BPP -> BAP)**: Seller signals that groceries are packed and waiting for buyer-arranged pickup at the merchant store counter.
- **`/update (update_buyer_delivery_intermin)` (BAP -> BPP)**: The BAP updates fulfillment status to `Order-picked-up`, providing delivery agent details (name, phone, provider ID) and dispatch timestamp.
- **`/on_update (on_update_buyer_delivery_intermin)` (BPP -> BAP)**: Seller acknowledges the pickup and updates its internal store logs.
- **`/update (update_buyer_delivery_final)` (BAP -> BPP)**: The BAP notifies the seller that the delivery agent has successfully handed over the order to the end consumer (`fulfillment.state = "Order-delivered"`).
- **`/on_update (on_update_buyer_delivery_final)` (BPP -> BAP)**: Seller records delivery completion and transitions order to `Completed`.

---

### Flow 3: Buyer-Side Order Cancellation

#### 1. Short Description
Exercises the process of a consumer cancelling a placed grocery order prior to fulfillment, ensuring the seller halts picking, updates order status to `Cancelled`, and triggers refund processing.

#### 2. API Breakdown & Technical Actions
- **`/select` through `/on_confirm`**: Buyer places and confirms a prepaid grocery order.
- **`/cancel` (BAP -> BPP)**: Buyer triggers cancellation from the app before merchant dispatch, supplying a standard ONDC cancellation reason code (`order.cancellation_reason_id = "001"`).
- **`/on_cancel` (BPP -> BAP)**: The seller validates that the order is within the cancellable window (`@ondc/org/cancellable = true`). The seller terminates fulfillment, updates `order.state = "Cancelled"`, recalculates any applicable fee deductions, and provides refund instructions.

---

### Flow 4: Merchant-Side Part-Order Cancellation and Return to Origin (RTO)

#### 1. Short Description
A multi-exception flow handling merchant inventory stock-outs during packaging, followed by an unsuccessful delivery attempt where the customer is unreachable, culminating in Return to Origin (RTO).

#### 2. API Breakdown & Technical Actions
- **`/confirm` -> `/on_confirm`**: Order established for multiple grocery items.
- **`on_update (on_update_part_cancel)` [Unsolicited] (BPP -> BAP)**: While picking, the merchant discovers one item is unavailable. The seller issues an unsolicited update cancelling that specific line item and updating the price quote.
- **`/update (update_settlement_trail)` (BAP -> BPP)**: The BAP acknowledges the item reduction and transmits the updated settlement trail reflecting the partial refund to the customer.
- **`on_status` sequence**: Order is packed, agent assigned, picked up, and marked out for delivery.
- **`on_cancel (on_cancel_rto)` [Unsolicited] (BPP -> BAP)**: Delivery agent attempts delivery but cannot reach the buyer. The seller initiates RTO with cancellation reason code `013` (Buyer unreachable), reversing route direction.
- **`/update (update_settlement_trail)` (BAP -> BPP)**: BAP transmits RTO settlement terms (accounting for return logistics deductions).
- **`on_status (on_status_rto_delivered)` [Unsolicited] (BPP -> BAP)**: Undelivered goods safely returned to merchant warehouse; order marked `Cancelled`.

---

### Flow 5: Buyer-Initiated Return (Full Order and Partial Order)

#### 1. Short Description
Covers the end-to-end post-delivery return lifecycle. The buyer requests a return for delivered items within the eligible window, the merchant approves the request, reverse pickup is executed, and financial settlement trails are completed.

#### 2. API Breakdown & Technical Actions
- **Forward Delivery Completion**: Order delivered with full `on_status` milestone sequence.
- **`/update (update_return)` (BAP -> BPP)**: Buyer submits a return request for specific delivered items, supplying reason codes (e.g. `001` - Damaged item), item quantities, and return images.
- **`/on_update (on_update_return_init)` (BPP -> BAP)**: Seller logs return request in state `Return_Initiated`.
- **`on_update (on_update_return_approved)` [Unsolicited] (BPP -> BAP)**: Seller accepts the return request and authorizes reverse logistics pickup.
- **`on_update (on_update_return_picked)` [Unsolicited] (BPP -> BAP)**: Reverse logistics agent collects the returned items from the customer.
- **`/update (update_settlement_trail)` (BAP -> BPP)**: Buyer application supplies bank account / UPI refund settlement instructions.
- **`on_update (on_update_return_delivered)` [Unsolicited] (BPP -> BAP)**: Goods reach seller facility; seller validates item condition and confirms full refund execution.

---

### Flow 6: Out of Stock Error Handling (Inventory Shortage)

#### 1. Short Description
Demonstrates exception handling when a buyer attempts to checkout items that have run out of stock. The seller gracefully rejects the initial selection with error code `40002`/`30009`, allowing the consumer to modify cart quantities and proceed with available inventory.

#### 2. API Breakdown & Technical Actions
- **`/select (select0)` (BAP -> BPP)**: Buyer selects grocery items with desired quantities.
- **`/on_select (on_select_out_of_stock)` (BPP -> BAP)**: Seller identifies that requested inventory is depleted. It returns an error response with error code `40002` (Out of stock) or `30009` and item availability details (`quantity.available.count = 0`).
- **`/select` (BAP -> BPP)**: Buyer adjusts cart to select available items or lower quantities.
- **`/on_select` (BPP -> BAP)**: Seller confirms stock availability and generates itemized quote.
- **`/init` through `/on_status (order_delivered)`**: Normal purchase and fulfillment sequence proceeds to completion.

---

### Flow 7: Search and Custom Menu – Full Catalog City Discovery

#### 1. Short Description
The foundational discovery flow for retail grocery. A consumer searches for groceries across an entire city or broad geolocation, and the seller returns its comprehensive product catalog, custom menus, categorized hierarchies, and serviceability rules.

#### 2. API Breakdown & Technical Actions
- **`/search (search_1)` (BAP -> Gateway)**: BAP broadcasts a city-wide discovery query (`context.city = "std:080"`, `intent.category.id = "ONDC:RET10"`).
- **`/on_search (on_search1)` (BPP -> BAP)**: Seller responds with full catalog:
  - `bpp/providers[]`: Store identity, operating hours, geolocation (`L1`), and serviceability radiuses.
  - `categories[]`: Hierarchical grocery categories (e.g. Atta/Flours, Fruits & Vegetables, Dairy).
  - `items[]`: Item descriptions, barcodes/GTINs, prices, images, unitized measures, and packaged commodity statutory tags.
  - `offers[]`: Available promotional discounts and bundle deals (e.g. Flat ₹50 off, Buy 2 Get 1).

---

### Flow 8: Search and Custom Menu – Incremental Catalog Push

#### 1. Short Description
Validates the merchant-initiated incremental catalog push mechanism. Sellers broadcast live updates regarding price alterations, flash discounts, stock replenishments, or temporary store closures without requiring a full catalog reload.

#### 2. API Breakdown & Technical Actions
- **`/search (search_inc)` (BAP -> Gateway)**: Preliminary search establishing active listening.
- **`on_search (on_search_inc)` [Unsolicited] (BPP -> BAP)**: Seller pushes differential item pricing or inventory adjustments.
- **`on_search (on_search_inc_close)` [Unsolicited] (BPP -> BAP)**: Seller signals temporary store closure (`serviceability` tags set to disabled for active hours).
- **`on_search (on_search_inc_open)` [Unsolicited] (BPP -> BAP)**: Seller re-enables store operations and serviceability.
- **`/search (search_inc1)` (BAP -> Gateway)**: Verification query confirming catalog state consistency.

---

### Flow 9: Discovery Flow – Incremental Catalog Refresh Pull

#### 1. Short Description
Validates the buyer application pull mechanism for catalog synchronization. The buyer requests catalog updates modified after a given timestamp, enabling efficient bandwidth utilization and consistent local price caches.

#### 2. API Breakdown & Technical Actions
- **`/search (search_1)` -> `/on_search (on_search1)`**: Baseline full catalog discovery.
- **`/search (search_inc_pull)` (BAP -> BPP)**: Targeted point-to-point search passing `tags` with `mode = "incremental_refresh"` and `last_updated_at` timestamp.
- **`/on_search (on_search_inc_pull)` (BPP -> BAP)**: Seller responds containing strictly those grocery items whose pricing, quantity, or metadata changed since the requested cutoff.

---

### Flow 10: Catalog Rejection Flow – Compliance Discrepancy

#### 1. Short Description
Validates regulatory safeguards in the grocery domain. When a seller's published catalog fails statutory compliance rules under the Legal Metrology (Packaged Commodities) Rules or FSSAI guidelines, the buyer app automatically rejects the catalog.

#### 2. API Breakdown & Technical Actions
- **`/search (search_1)` (BAP -> Gateway)**: BAP transmits discovery request.
- **`/on_search (on_search1)` (BPP -> BAP)**: Seller returns catalog containing items that violate mandatory statutory declarations (e.g., missing manufacturer name, absent net quantity, missing MRP, or expired license).
- **`catalog_rejection` (BAP Internal / Log)**: BAP compliance validator detects non-conforming items, flags statutory violations, and rejects the provider's catalog from consumer listings.

---

### Flow 11: Order to Confirm with IGM 1.0.0 Resolution

#### 1. Short Description
A complete purchase and fulfillment flow integrated with the standard IGM 1.0.0 complaint resolution cycle. After receiving groceries, the consumer raises a quality grievance, which the merchant resolves and closes.

#### 2. API Breakdown & Technical Actions
- **Delivery Steps (1–14)**: Order placed, paid, packed, dispatched, tracked, and delivered.
- **`/issue (issue_open_100)` (BAP -> BPP)**: Buyer files a complaint citing item quality defects (e.g. damaged packaging), attaching photos and contact info.
- **`/on_issue (on_issue_processing_100)` (BPP -> BAP)**: Seller acknowledges complaint, generates a ticket number, and assigns an expected resolution deadline.
- **`on_issue_status (on_issue_resolved_100)` [Unsolicited] (BPP -> BAP)**: Seller investigates and posts a resolution (`RESOLVED`), authorizing a refund or credit adjustment.
- **`/issue (issue_close_100)` (BAP -> BPP)**: Buyer confirms satisfactory resolution and closes the issue.

---

### Flow 12: Order to Confirm with IGM 2.0.0 – Resolution Accepted (No Action)

#### 1. Short Description
Validates the advanced IGM 2.0.0 framework where a grievance is processed, a formal resolution explanation is tendered by the seller without secondary physical fulfillment actions, and the consumer accepts the resolution.

#### 2. API Breakdown & Technical Actions
- **Delivery Steps (1–14)**: Order placed and delivered.
- **`/issue (issue_open_2)` (BAP -> BPP)**: Buyer registers an issue under IGM 2.0.0 schema with sub-category codes and complainant details.
- **`/on_issue (on_issue_processing)` (BPP -> BAP)**: Seller acknowledges receipt and assigns grievance handler.
- **`on_issue (on_issue_resolution_igm_3)` [Unsolicited] (BPP -> BAP)**: Seller provides formal resolution proposal (`action_triggered = "NO_ACTION"` with explanatory justification).
- **`/issue (issue_resolution_accept_igm_3)` (BAP -> BPP)**: Complainant reviews and formally accepts the resolution.
- **`/on_issue (on_issue_resolved_igm_3)` (BPP -> BAP)**: Seller marks issue state as `RESOLVED`.
- **`/issue (issue_close_igm_3)` (BAP -> BPP)**: Buyer closes the ticket.
- **`on_status (on_status_igm_3)` [Unsolicited] (BPP -> BAP)**: Seller finalizes post-resolution order audit status.

---

### Flow 13: Order to Confirm with IGM 2.0.0 – Rejection, Escalation & Return

#### 1. Short Description
A multi-tier grievance escalation flow under IGM 2.0.0. The buyer rejects the initial resolution, escalates the dispute to higher grievance redressal authorities, reaches a mutually accepted resolution, and executes an authorized product return.

#### 2. API Breakdown & Technical Actions
- **Delivery Steps (1–14)**: Order delivered successfully.
- **`/issue (issue_open)` -> `/on_issue (processing)`**: Initial grievance filed.
- **`on_issue (on_issue_resolution)` [Unsolicited] (BPP -> BAP)**: Seller proposes an initial settlement.
- **`/issue (issue_resolution_reject)` (BAP -> BPP)**: Buyer rejects the proposed resolution as unsatisfactory.
- **`/on_issue (on_issue_processing_1)` -> `on_issue (on_issue_resolution_1)`**: Seller reconsiders with a revised proposal.
- **`/issue (issue_escalate)` (BAP -> BPP)**: Buyer escalates grievance to Level 2 (Grievance Redressal Officer / Arbitrator).
- **`/on_issue (on_issue_processing_2)` -> `on_issue (on_issue_resolution_2)`**: Escalated resolution published.
- **`/issue (issue_resolution_accept)` (BAP -> BPP)**: Complainant accepts the escalated resolution terms.
- **`/on_issue (on_issue_resolved)` -> `/issue (issue_close)`**: Ticket closed as successfully resolved.
- **`on_update (on_update_igm_return)` [Unsolicited] (BPP -> BAP)**: As mandated by the grievance agreement, seller initiates an official return and refund workflow for the contested items.

---

### Flow 14: Order to Confirm with IGM 2.0.0 – Resolution & Item Replacement

#### 1. Short Description
Validates the interactive evidence-gathering cycle in IGM 2.0.0. The seller requests additional item photographs, the buyer supplies the evidence, and the seller approves an item replacement, automatically dispatching a replacement grocery parcel.

#### 2. API Breakdown & Technical Actions
- **Delivery Steps (1–14)**: Order delivered.
- **`/issue (issue_open)` -> `/on_issue (processing)`**: Buyer files an issue claiming an incorrect or damaged item was delivered.
- **`on_issue (on_issue_need_more_info)` [Unsolicited] (BPP -> BAP)**: Seller requests verification proof (e.g. barcode scan and package label photo).
- **`/issue (issue_info_provided)` (BAP -> BPP)**: Buyer uploads the requested media and explanatory text.
- **`/on_issue (on_issue_provided)` (BPP -> BAP)**: Seller confirms receipt of additional evidence.
- **`on_issue (on_issue_resolution)` [Unsolicited] (BPP -> BAP)**: Seller validates proof and proposes full item replacement (`action_triggered = "REPLACEMENT"`).
- **`/issue (issue_resolution_accept)` (BAP -> BPP)**: Buyer accepts the replacement offer.
- **`/on_issue (on_issue_resolved)` -> `/issue (issue_close)`**: Grievance closed as resolved.
- **`on_update (on_update_igm_replacement)` [Unsolicited] (BPP -> BAP)**: Seller automatically generates and triggers a new replacement fulfillment parcel containing the replacement grocery item.

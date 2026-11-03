# Retail Fashion (ONDC:RET12 1.2.0)

- [Overview](#overview)
- [Participants](#participants)
- [The User Journey](#the-user-journey)
  - [1. Discovery and Catalog Search](#1-discovery-and-catalog-search)
  - [2. Variant Selection, Sizing, and Serviceability Check](#2-variant-selection-sizing-and-serviceability-check)
  - [3. Order Initialization and Shipping Configuration](#3-order-initialization-and-shipping-configuration)
  - [4. Order Confirmation and Payment](#4-order-confirmation-and-payment)
  - [5. Order Processing, Picking, and Packaging](#5-order-processing-picking-and-packaging)
  - [6. Logistics and Courier Assignment](#6-logistics-and-courier-assignment)
  - [7. Order Dispatch, In-Flight Tracking, and Doorstep Delivery](#7-order-dispatch-in-flight-tracking-and-doorstep-delivery)
  - [8. Settlement and Post-Fulfillment](#8-settlement-and-post-fulfillment)
- [Additional Scenarios](#additional-scenarios)
  - [1. Buyer-Initiated Returns (Full and Partial Order)](#1-buyer-initiated-returns-full-and-partial-order)
  - [2. Buyer-Side Order Cancellation](#2-buyer-side-order-cancellation)
  - [3. Merchant-Side Part-Cancellation and Return to Origin (RTO)](#3-merchant-side-part-cancellation-and-return-to-origin-rto)
  - [4. Out of Stock and Inventory Variant Depletion](#4-out-of-stock-and-inventory-variant-depletion)
  - [5. Incremental Catalog Refresh (Push and Pull)](#5-incremental-catalog-refresh-push-and-pull)
  - [6. Statutory Compliance & Legal Metrology for Apparel](#6-statutory-compliance--legal-metrology-for-apparel)
- [Issue and Grievance Management](#issue-and-grievance-management)
  - [1. IGM 1.0.0 Architecture](#1-igm-100-architecture)
  - [2. IGM 2.0.0 Architecture](#2-igm-200-architecture)
- [Detailed Protocol Flows](#detailed-protocol-flows)
  - [Flow 1: Order to Confirm to Fulfillment (Prepaid Standard Delivery)](#flow-1-order-to-confirm-to-fulfillment-prepaid-standard-delivery)
  - [Flow 2: Buyer-Initiated Return (Full Order and Partial Order)](#flow-2-buyer-initiated-return-full-order-and-partial-order)
  - [Flow 3: Buyer-Side Order Cancellation](#flow-3-buyer-side-order-cancellation)
  - [Flow 4: Merchant-Side Part-Order Cancellation and Return to Origin (RTO)](#flow-4-merchant-side-part-order-cancellation-and-return-to-origin-rto)
  - [Flow 5: Out of Stock Error Handling (Inventory Shortage)](#flow-5-out-of-stock-error-handling-inventory-shortage)
  - [Flow 6: Search and Custom Menu – Full Catalog City Discovery](#flow-6-search-and-custom-menu--full-catalog-city-discovery)
  - [Flow 7: Search and Custom Menu – Incremental Catalog Push](#flow-7-search-and-custom-menu--incremental-catalog-push)
  - [Flow 8: Discovery Flow – Incremental Catalog Refresh Pull](#flow-8-discovery-flow--incremental-catalog-refresh-pull)
  - [Flow 9: Order to Confirm with IGM 1.0.0 Resolution](#flow-9-order-to-confirm-with-igm-100-resolution)
  - [Flow 10: Order to Confirm with IGM 2.0.0 – Resolution Accepted (No Action)](#flow-10-order-to-confirm-with-igm-200--resolution-accepted-no-action)
  - [Flow 11: Order to Confirm with IGM 2.0.0 – Rejection, Escalation & Item Replacement](#flow-11-order-to-confirm-with-igm-200--rejection-escalation--item-replacement)
  - [Flow 12: Order to Confirm with IGM 2.0.0 – Evidence Exchange & Return Resolution](#flow-12-order-to-confirm-with-igm-200--evidence-exchange--return-resolution)

---

## Overview

The Fashion retail domain (**ONDC:RET12**, specification version **1.2.0**) establishes an open, interoperable digital commerce standard for apparel, clothing, footwear, ethnic wear, innerwear, and fashion accessories across the Open Network for Digital Commerce (ONDC). Fashion commerce is characterized by SKU variant hierarchies (parent products with multiple size, color, fit, and style combinations), high return frequency due to sizing and visual tactile mismatches, fast-moving seasonal inventory, statutory declarations under the Legal Metrology (Packaged Commodities) Rules, and both hyperlocal and intercity parcel logistics.

Historically, independent garment stores, regional boutique brands, and fashion retailers were locked into closed proprietary marketplaces (such as Amazon, Flipkart, or Myntra), enduring exorbitant commission rates and restrictive platform rules. ONDC:RET12 unbundles this ecosystem:
- **Shoppers** use their preferred **Buyer Application (BAP)** to browse fashion products from multiple brands and local stores, evaluate sizing charts, compare prices, check delivery serviceability, and manage post-purchase returns.
- **Fashion Retailers** list their merchandise via a **Seller Application (BPP)**, maintaining complete autonomy over inventory, pricing, discount strategies, fulfillment policies, and return windows.
- **Logistics Service Providers (LSPs)** execute forward delivery and reverse pickup logistics seamlessly over the open protocol.

The protocol standardizes all network interactions across:
- **Discovery**: `/search` and `/on_search` (city-wide full catalog broadcasts, category hierarchies, incremental push/pull).
- **Ordering**: `/select`, `/on_select`, `/init`, `/on_init`, `/confirm`, and `/on_confirm`.
- **Fulfillment & Tracking**: unsolicited `/on_status` lifecycle events (`Accepted`, `Packed`, `Agent-assigned`, `Order-picked-up`, `Out-for-delivery`, `Order-delivered`), `/track`, and `/on_track`.
- **Post-Order Lifecycle & Returns**: `/update`, `/on_update`, `/cancel`, and `/on_cancel` (full and partial buyer returns, reverse logistics pickup, condition verification, merchant part-cancellations, and Return to Origin / RTO).
- **Grievance Redressal**: Issue and Grievance Management under both **IGM 1.0.0** and **IGM 2.0.0** architectures.

---

## Participants

| Participant | What This Means |
|---|---|
| **Buyer Application (BAP)** | The consumer-facing platform (e.g. fashion e-commerce apps, banking/UPI apps, telco marketplaces) where consumers discover fashion catalogs, filter by size, color, and gender, configure delivery addresses, make digital payments, track shipments, and request returns or size exchanges. |
| **Seller Application (BPP)** | An application representing clothing stores, fashion labels, garment manufacturers, or D2C apparel brands. The BPP publishes product catalogs with variant attributes (size, color, material), validates delivery serviceability, provides itemized pricing and delivery quotes, manages picking and packing, and processes reverse returns. |
| **Logistics Service Provider (LSP)** | A delivery network participant that executes hyperlocal same-day delivery or intercity surface/air logistics. In seller-managed delivery, the BPP or its integrated logistics partner coordinates pickup, transit, delivery verification, and reverse logistics return pickups. |
| **Gateway** | The ONDC routing infrastructure that multicasts broadcast discovery requests (`/search`) from BAPs to active seller applications (BPPs) based on domain code (`ONDC:RET12`), city code (e.g. `std:080`), and geolocation parameters. |

---

## The User Journey

The standard fashion ordering journey (`Order_to_confirm_to_fulfillment_(Prepaid)`) enables a shopper to discover clothing items, select precise size and color variants, review transparent price breakdowns and estimated delivery windows, pay digitally, and receive packed garments with end-to-end shipment milestone tracking.

### 1. Discovery and Catalog Search

The shopper initiates discovery on the BAP by searching for apparel categories, styles, or brands (e.g., "Men's Slim Fit Jeans", "Cotton T-Shirts", "Sarees"):

- **Intent Broadcast**: The BAP transmits a `/search` request specifying the domain category (`ONDC:RET12`), shopper delivery GPS coordinates and area pin code, and fulfillment type (`Delivery`).
- **Catalog Delivery**: Active fashion BPPs within serviceable delivery range respond via asynchronous `/on_search` payloads containing their store catalog (`bpp/providers[]`). This includes parent products, variant SKUs, images, size options, color swatches, fabric details, MRP, selling price, brand name, and statutory packaged commodity details.

### 2. Variant Selection, Sizing, and Serviceability Check

The shopper selects specific items with desired sizes and colors and adds them to their cart:

- **Network interaction:**
  - **`/select` (BAP -> BPP)**: The BAP transmits selected item IDs, variant SKUs, quantities, store location ID, and delivery destination coordinates (`fulfillments[0].end.location.gps` and `address.area_code`).
  - **`/on_select` (BPP -> BAP)**: The seller validates real-time inventory for the chosen size/color variants and delivery serviceability. The seller returns an itemized price quote (`quote.breakup[]`) breaking down base item prices, delivery charges (`@ondc/org/title_type="delivery"`), packaging fees, applicable taxes (CGST/SGST), and estimated turnaround time (`@ondc/org/TAT`). If a size variant is out of stock, the seller returns error code `40002` or `30009`.

### 3. Order Initialization and Shipping Configuration

The shopper provides finalized delivery and billing details:

- **Network interaction:**
  - **`/init` (BAP -> BPP)**: The BAP transmits the shopper's full shipping address (flat/house number, building, street, landmark, area code), contact details (phone, email), billing address, and payment preferences.
  - **`/on_init` (BPP -> BAP)**: The seller freezes the order quote, specifies static/dynamic cancellation terms and return window (`@ondc/org/return_window`, e.g. `P7D` for 7-day return eligibility), sets payment collection rules, and returns settlement fee details.

### 4. Order Confirmation and Payment

The shopper completes digital prepaid payment:

- **Network interaction:**
  - **`/confirm` (BAP -> BPP)**: The BAP captures digital payment, generates the formal order ID (`order.id`), and transmits payment confirmation parameters (`payment.params.transaction_id`, `payment.status = "PAID"`).
  - **`/on_confirm` (BPP -> BAP)**: The seller validates payment, records the order in its ERP / Warehouse Management System (WMS), sets `order.state = "Created"`, and establishes initial fulfillment state `Pending`.

### 5. Order Processing, Picking, and Packaging

The clothing retailer or warehouse team picks the specific size/color garment from inventory shelves, inspects quality, and packs the parcel:

- **`on_status (Accepted)` [Unsolicited] (BPP -> BAP)**: Unsolicited status update indicating the merchant has accepted the fashion order (`order.state = "Accepted"`).
- **`on_status (Packed)` [Unsolicited] (BPP -> BAP)**: Unsolicited status update confirming the garments have been folded, bagged/boxed, sealed in tamper-evident packaging, and labeled with a shipping barcode (`order.state = "In-progress"`, `fulfillment.state = "Packed"`).

### 6. Logistics and Courier Assignment

A delivery partner or courier executive is assigned to the parcel:

- **`on_status (Agent-assigned)` [Unsolicited] (BPP -> BAP)**: The logistics provider allocates a courier agent or assigns an airway bill (AWB) number. The payload provides delivery agent credentials (`fulfillments[0].agent.name`, `agent.phone`).

### 7. Order Dispatch, In-Flight Tracking, and Doorstep Delivery

The courier collects the packaged apparel from the store/warehouse and transports it to the buyer's destination:

- **`on_status (Order-picked-up)` [Unsolicited] (BPP -> BAP)**: Seller notifies that the courier has picked up the package from the store (`fulfillment.state = "Order-picked-up"`), recording `fulfillments[0].start.time.timestamp`.
- **`/track` & `/on_track` (BAP $\leftrightarrow$ BPP)**: The BAP polls for live shipment tracking URL / GPS coordinates.
- **`on_status (Out-for-delivery)` [Unsolicited] (BPP -> BAP)**: Triggered when the last-mile delivery courier is out for doorstep delivery.
- **`on_status (Order-delivered)` [Unsolicited] (BPP -> BAP)**: Sent upon successful physical delivery at the buyer's address (`fulfillment.state = "Order-delivered"`, `order.state = "Completed"`), recording `fulfillments[0].end.time.timestamp` and electronic proof of delivery (ePOD / delivery OTP).

### 8. Settlement and Post-Fulfillment

Following successful delivery and expiry of the return window (or immediate provisional hold), financial reconciliation takes place. The BAP releases funds to the seller according to agreed settlement windows (T+1 / T+2), withholding agreed buyer finder fees and routing statutory tax deductions where applicable.

---

## Additional Scenarios

Fashion retail involves dynamic operational conditions that diverge from the happy path, particularly regarding returns, out-of-stock sizes, and order cancellations.

### 1. Buyer-Initiated Returns (Full and Partial Order)

Because apparel cannot be tried on prior to purchase, returns due to sizing, fit, fabric feel, or color differences are standard in fashion retail:
- **Return Initiation (`update_return`)**: Within the return window (`@ondc/org/return_window`, e.g. 7 days), the buyer requests a return for either the entire order or specific items (partial return), providing item IDs, quantities, return reason codes (e.g., `001` - Size mismatch/fit issue, `002` - Defective/damaged fabric, `003` - Product different from image), and photos.
- **Acknowledgment & Approval (`on_update_return_init` & `on_update_return_approved`)**: The seller acknowledges the return request (`Return_Initiated`) and issues authorization (`return_approved`).
- **Reverse Logistics Collection (`on_update_return_picked`)**: A reverse logistics courier is dispatched to inspect the garment tags and packaging and collect the return parcel from the consumer.
- **Refund Settlement (`update_settlement_trail`)**: The BAP transmits bank account/UPI settlement instructions to credit the consumer.
- **Delivery at Merchant Facility (`on_update_return_delivered`)**: The returned parcel arrives at the merchant's warehouse, where staff inspect garment condition and confirm full refund execution.

### 2. Buyer-Side Order Cancellation

A consumer may cancel an order before the seller has dispatched the parcel:
- **`/cancel` (BAP -> BPP)**: The BAP transmits a cancellation request with an ONDC cancellation reason code (`order.cancellation_reason_id = "001"`).
- **`/on_cancel` (BPP -> BAP)**: The seller validates that the order is within its cancellable window (`@ondc/org/cancellable = true`), terminates fulfillment, sets `order.state = "Cancelled"`, recalculates any applicable fee deductions, and provides refund instructions.

### 3. Merchant-Side Part-Cancellation and Return to Origin (RTO)

Hyperlocal and intercity fashion fulfillment encounters situations where specific sizes are out of stock during picking, or where a delivery attempt fails:
- **Partial Order Cancellation (`on_update_part_cancel`)**: If one garment in a multi-item order is found defective or out of stock during warehouse picking, the seller sends an unsolicited `/on_update` adjusting `quote.breakup`. The BAP responds with `/update (update_settlement_trail)` to credit the differential refund.
- **Return to Origin (`on_cancel_rto`)**: When the courier attempts delivery but the customer is unreachable, rejects delivery, or provides an incorrect address, the seller initiates RTO with cancellation reason codes `011`–`015`. The parcel is routed back to the merchant store/warehouse (`on_status_rto_delivered`), and settlement trails are adjusted for reverse transit costs.

### 4. Out of Stock and Inventory Variant Depletion

When a consumer selects a specific size/color SKU whose inventory was just depleted:
- **Error Response (`on_select_out_of_stock`)**: The seller returns an error block containing ONDC error code `40002` (Out of Stock) or `30009` and item availability details (`quantity.available.count = 0`).
- **Shopper Reconfiguration**: The BAP displays the out-of-stock notification, allowing the shopper to pick an alternative size or color variant.

### 5. Incremental Catalog Refresh (Push and Pull)

Fashion catalogs, seasonal collections, flash sales, and size availability fluctuate continuously:
- **Incremental Push (`Search_and_Custom_Menu__Incremental_Push_`)**: The seller broadcasts real-time price drops, stock replenishment, new style arrivals, or temporary store closures (`on_search_inc_disable`) via unsolicited `/on_search` payloads.
- **Incremental Pull (`Discovery_Flow_incremental_catalog_refresh_pull`)**: The buyer application queries the seller for catalog changes that occurred since a specific timestamp (`last_updated_at`), minimizing network bandwidth while keeping local caches synchronized.

### 6. Statutory Compliance & Legal Metrology for Apparel

Packaged fashion and apparel goods are governed by the Legal Metrology (Packaged Commodities) Rules:
- Product listings must include manufacturer/packer/importer name and address, country of origin, net quantity (e.g. 1 Piece / 1 Pair), consumer care details, month and year of manufacture/import, and exact size measurements (e.g., chest, waist, length in cm and inches).

---

## Issue and Grievance Management

The fashion domain provides robust complaint handling across both ONDC Issue and Grievance Management (IGM) framework versions.

### 1. IGM 1.0.0 Architecture

In IGM 1.0.0, grievances follow a linear status progression:
1. **`issue (open)` (BAP -> BPP)**: The shopper files a complaint against an order or item (e.g., "Received defective garment", "Stitching torn", "Wrong size received"), providing descriptions, photos, and complainant details.
2. **`on_issue (processing)` (BPP -> BAP)**: The seller acknowledges receipt of the complaint, providing a grievance ticket ID, respondent details, and expected Resolution Time (TAT).
3. **`on_issue_status (resolved)` (BPP -> BAP)**: The seller investigates and publishes a formal resolution (`REFUND`, `REPLACEMENT`, or `NO_ACTION`) with resolution remarks.
4. **`issue (close)` (BAP -> BPP)**: The shopper reviews the resolution and closes the grievance ticket.

### 2. IGM 2.0.0 Architecture

IGM 2.0.0 introduces multi-party interactions, evidence exchange, dispute escalation, and automated fulfillment linkages:
- **Evidence Exchange (`Order_to_confirm_to_fulfillment__Prepaid_with_IGM(v-2.0.0)`)**: The seller requests detailed garment/tag photos (`on_issue_need_more_info`), and the shopper uploads the proof (`issue_info_provided`), triggering an approved refund/return (`on_update_igm_return`).
- **No-Action Resolution (`Order_to_confirm_to_fulfillment__Prepaid_with_IGM_No_Action(v-2.0.0)`)**: The seller investigates and tenders an explanatory resolution with `action_triggered = "NO_ACTION"`, accepted by the shopper, followed by post-resolution order audit status (`on_status_igm_3`).
- **Rejection, Escalation & Item Replacement (`Order_to_confirm_to_fulfillment__Prepaid_with_IGM_Rejection(v-2.0.0)`)**: The shopper rejects initial resolution proposals (`issue_resolution_reject`), escalates the dispute to Level 2 (Grievance Redressal Officer / Arbitrator), reaches an accepted binding resolution, and receives a replacement garment parcel dispatched by the seller (`on_update_igm_replacement`).

---

## Detailed Protocol Flows

### Flow 1: Order to Confirm to Fulfillment (Prepaid Standard Delivery)

#### 1. Short Description
The primary forward-fulfillment fashion purchase journey. A shopper selects clothing items and size variants, receives an itemized quote with delivery fees and taxes, provides shipping addresses, pays upfront, and receives the goods through seller-managed delivery with live courier tracking and delivery verification.

#### 2. API Breakdown & Technical Actions
- **`/select` (BAP -> BPP)**: The BAP transmits selected garment item IDs, size/color variant codes, quantities, store location ID, and delivery coordinates (`fulfillments[0].end.location.gps` and `address.area_code`).
- **`/on_select` (BPP -> BAP)**: The seller validates store inventory and delivery radius. It returns an itemized price quote (`quote.breakup[]`) with base garment prices, delivery fees (`@ondc/org/title_type="delivery"`), packaging charges, and delivery turnaround time (`@ondc/org/TAT`).
- **`/init` (BAP -> BPP)**: The shopper inputs full shipping destination (house/flat, building, street, city, pin code) and contact details.
- **`/on_init` (BPP -> BAP)**: The seller freezes the order quote, specifies cancellation terms, publishes the return window (`@ondc/org/return_window = "P7D"`), and provides payment collection instructions.
- **`/confirm` (BAP -> BPP)**: The BAP collects payment digitally, binds the transaction with `payment.status = "PAID"`, and sends the final order commitment.
- **`/on_confirm` (BPP -> BAP)**: The seller confirms order acceptance, assigning an official `order.id` with state `Created` and fulfillment state `Pending`.
- **`on_status (on_status_pending)` [Unsolicited] (BPP -> BAP)**: Merchant marks order as accepted for fulfillment (`order.state = "Accepted"`).
- **`on_status (on_status_packed)` [Unsolicited] (BPP -> BAP)**: Garments picked, quality-checked, and packed into parcel with shipping label (`fulfillment.state = "Packed"`, `order.state = "In-progress"`).
- **`on_status (on_status_agent_assigned)` [Unsolicited] (BPP -> BAP)**: Delivery courier assigned; payload includes courier name, mobile number, and tracking ID.
- **`on_status (on_status_picked)` [Unsolicited] (BPP -> BAP)**: Courier collects package from store/warehouse (`fulfillment.state = "Order-picked-up"`, with pickup timestamp).
- **`/track` & `/on_track` (BAP $\leftrightarrow$ BPP)**: BAP requests live tracking URL / endpoint for real-time shipment progress.
- **`on_status (on_status_out_for_delivery)` [Unsolicited] (BPP -> BAP)**: Courier is out for delivery to shopper's doorstep (`fulfillment.state = "Out-for-delivery"`).
- **`on_status (on_status_order_delivered)` [Unsolicited] (BPP -> BAP)**: Package successfully delivered with delivery timestamp and electronic proof of delivery (`fulfillment.state = "Order-delivered"`, `order.state = "Completed"`).

---

### Flow 2: Buyer-Initiated Return (Full Order and Partial Order)

#### 1. Short Description
Covers the complete post-delivery return lifecycle for fashion apparel. The shopper requests a return for delivered garments (e.g. wrong fit, size mismatch, or damaged fabric) within the 7-day window. The merchant approves the request, reverse logistics pickup is executed, condition is validated, and full refund settlement is processed.

#### 2. API Breakdown & Technical Actions
- **Forward Delivery Completion (Steps 1–12)**: Order delivered with full `on_status` sequence (`accepted` $\rightarrow$ `packed` $\rightarrow$ `agent_assigned` $\rightarrow$ `picked` $\rightarrow$ `out_for_delivery` $\rightarrow$ `order_delivered`).
- **`/update (update_return)` (BAP -> BPP)**: Shopper submits a return request for specific delivered garments, supplying return reason codes (e.g., `001` - Size mismatch/fit issue), item quantities, and return photos.
- **`/on_update (on_update_return_init)` (BPP -> BAP)**: Seller logs return request in state `Return_Initiated`.
- **`on_update (on_update_return_approved)` [Unsolicited] (BPP -> BAP)**: Seller reviews and accepts the return request, authorizing reverse logistics pickup.
- **`on_update (on_update_return_picked)` [Unsolicited] (BPP -> BAP)**: Reverse logistics courier inspects garment tags and collects the parcel from the consumer.
- **`/update (update_settlement_trail)` (BAP -> BPP)**: Buyer application supplies bank account / UPI refund settlement instructions.
- **`on_update (on_update_return_delivered)` [Unsolicited] (BPP -> BAP)**: Garments reach seller warehouse; merchant validates condition and confirms full refund execution.

---

### Flow 3: Buyer-Side Order Cancellation

#### 1. Short Description
Exercises the process of a consumer cancelling a placed fashion order prior to merchant dispatch, ensuring the seller halts picking, updates order status to `Cancelled`, and triggers refund processing.

#### 2. API Breakdown & Technical Actions
- **Steps 1–6 (`/select` to `/on_confirm`)**: Shopper places and confirms a prepaid clothing order.
- **`/cancel` (BAP -> BPP)**: Shopper triggers cancellation from the app before merchant dispatch, supplying a standard ONDC cancellation reason code (`order.cancellation_reason_id = "001"`).
- **`/on_cancel` (BPP -> BAP)**: The seller validates that the order is within the cancellable window (`@ondc/org/cancellable = true`). The seller terminates fulfillment, updates `order.state = "Cancelled"` and `fulfillment.state = "Cancelled"`, recalculates any applicable fee deductions, and provides refund instructions.

---

### Flow 4: Merchant-Side Part-Order Cancellation and Return to Origin (RTO)

#### 1. Short Description
A multi-exception flow handling merchant inventory stock-outs during warehouse picking, followed by an unsuccessful delivery attempt where the customer is unreachable, culminating in Return to Origin (RTO).

#### 2. API Breakdown & Technical Actions
- **Steps 1–6 (`/select` to `/on_confirm`)**: Order confirmed for multiple fashion items.
- **`on_update (on_update_part_cancel)` [Unsolicited] (BPP -> BAP)**: While picking, the merchant discovers a specific garment size is unavailable. The seller issues an unsolicited update cancelling that specific line item and updating the price quote.
- **`/update (update_settlement_trail)` (BAP -> BPP)**: The BAP acknowledges the item reduction and transmits the updated settlement trail reflecting the partial refund to the customer.
- **Fulfillment Progression (Steps 9–13)**: Remaining items are packed, courier assigned, picked up, and marked out for delivery.
- **`on_cancel (on_cancel_rto)` [Unsolicited] (BPP -> BAP)**: Courier attempts delivery but cannot reach the buyer. The seller initiates RTO with cancellation reason code `013` (Buyer unreachable), reversing route direction.
- **`/update (update_settlement_trail_1)` (BAP -> BPP)**: BAP transmits RTO settlement terms (accounting for return logistics deductions).
- **`on_status (on_status_rto_delivered)` [Unsolicited] (BPP -> BAP)**: Undelivered garments safely returned to merchant warehouse; order marked `Cancelled`.

---

### Flow 5: Out of Stock Error Handling (Inventory Shortage)

#### 1. Short Description
Demonstrates protocol error handling when a shopper attempts to select a fashion catalogue item or size variant that is depleted. The seller platform rejects the selection via `on_select` with error code `40002`/`30009`.

#### 2. API Breakdown & Technical Actions
- **`/select (select0)` (BAP -> BPP)**: Shopper selects garment items with desired size/color variants and quantities.
- **`/on_select (on_select_out_of_stock)` (BPP -> BAP)**: Seller identifies that requested variant inventory is exhausted. It returns an error response with error code `40002` (Out of stock) or `30009` and item availability details (`quantity.available.count = 0`), allowing the buyer app to inform the consumer.

---

### Flow 6: Search and Custom Menu – Full Catalog City Discovery

#### 1. Short Description
The foundational discovery flow for fashion retail. A consumer searches for clothing and apparel across an entire city or broad geolocation, and the seller returns its comprehensive product catalog, categories, variant options, and serviceability rules.

#### 2. API Breakdown & Technical Actions
- **`/search (search_1)` (BAP -> Gateway)**: BAP broadcasts a city-wide discovery query (`context.city = "std:080"`, `intent.category.id = "ONDC:RET12"`).
- **`/on_search (on_search1)` (BPP -> BAP)**: Seller responds with full catalog:
  - `bpp/providers[]`: Store identity, operating hours, geolocation, and serviceability radiuses.
  - `categories[]`: Hierarchical fashion categories (e.g. Men's Wear, Women's Ethnic, Footwear, Accessories).
  - `items[]`: Garment descriptions, variant attributes (size, color, material, pattern), prices, images, brand names, and Legal Metrology statutory tags.
  - `offers[]`: Available promotional discounts and bundle deals.

---

### Flow 7: Search and Custom Menu – Incremental Catalog Push

#### 1. Short Description
Validates the merchant-initiated incremental catalog push mechanism. Sellers broadcast live updates regarding price alterations, seasonal flash discounts, size replenishment, new style drops, or temporary store closures without requiring a full catalog reload.

#### 2. API Breakdown & Technical Actions
- **`/search (search_inc)` (BAP -> Gateway)**: Preliminary search establishing active listening.
- **`on_search (on_search_inc)` [Unsolicited] (BPP -> BAP)**: Seller pushes differential item pricing or inventory adjustments.
- **`on_search (on_search_inc_disable)` [Unsolicited] (BPP -> BAP)**: Seller signals temporary store closure or disables catalog serviceability.
- **`/search (search_inc1)` (BAP -> Gateway)**: Verification query confirming catalog state consistency.

---

### Flow 8: Discovery Flow – Incremental Catalog Refresh Pull

#### 1. Short Description
Validates the buyer application pull mechanism for catalog synchronization. The buyer requests catalog updates modified after a given timestamp (`last_updated_at`), minimizing network bandwidth while keeping local price and size caches fresh.

#### 2. API Breakdown & Technical Actions
- **`/search (search_1)` -> `/on_search (on_search1)`**: Baseline full catalog discovery.
- **`/search (search_inc_pull)` (BAP -> BPP)**: Targeted point-to-point search passing `tags` with `mode = "incremental_refresh"` and `last_updated_at` timestamp.
- **`/on_search (on_search_inc_pull)` (BPP -> BAP)**: Seller responds containing strictly those fashion items whose pricing, inventory, or metadata changed since the requested cutoff.

---

### Flow 9: Order to Confirm with IGM 1.0.0 Resolution

#### 1. Short Description
A complete forward fulfillment flow integrated with the standard IGM 1.0.0 complaint resolution cycle. After receiving apparel, the consumer raises a quality or defect grievance, which the merchant investigates, resolves, and closes.

#### 2. API Breakdown & Technical Actions
- **Delivery Steps (1–14)**: Order placed, paid, packed, dispatched, tracked, and delivered.
- **`/issue (issue_open_100)` (BAP -> BPP)**: Shopper files a complaint citing garment defects (e.g. torn stitching, defective zipper, stained fabric), attaching photos and contact info.
- **`/on_issue (on_issue_processing_100)` (BPP -> BAP)**: Seller acknowledges complaint, generates a ticket number, and assigns an expected resolution deadline.
- **`on_issue_status (on_issue_resolved_100)` [Unsolicited] (BPP -> BAP)**: Seller investigates and posts a resolution (`RESOLVED`), authorizing a refund or credit adjustment.
- **`/issue (issue_close_100)` (BAP -> BPP)**: Shopper confirms satisfactory resolution and closes the issue.

---

### Flow 10: Order to Confirm with IGM 2.0.0 – Resolution Accepted (No Action)

#### 1. Short Description
Validates the IGM 2.0.0 framework where a grievance is processed, a formal resolution explanation is tendered by the seller without secondary physical fulfillment actions, and the shopper accepts the resolution.

#### 2. API Breakdown & Technical Actions
- **Delivery Steps (1–14)**: Order placed, fulfilled, and delivered.
- **`/issue (issue_open_2)` (BAP -> BPP)**: Shopper registers an issue under IGM 2.0.0 schema with sub-category codes and complainant details.
- **`/on_issue (on_issue_processing)` (BPP -> BAP)**: Seller acknowledges receipt and assigns a grievance handler.
- **`on_issue (on_issue_resolution_igm_3)` [Unsolicited] (BPP -> BAP)**: Seller provides formal resolution proposal (`action_triggered = "NO_ACTION"` with explanatory justification).
- **`/issue (issue_resolution_accept_igm_3)` (BAP -> BPP)**: Complainant reviews and formally accepts the resolution.
- **`/on_issue (on_issue_resolved_igm_3)` (BPP -> BAP)**: Seller marks issue state as `RESOLVED`.
- **`/issue (issue_close_igm_3)` (BAP -> BPP)**: Shopper closes the ticket.
- **`on_status (on_status_igm_3)` [Unsolicited] (BPP -> BAP)**: Seller finalizes post-resolution order audit status.

---

### Flow 11: Order to Confirm with IGM 2.0.0 – Rejection, Escalation & Item Replacement

#### 1. Short Description
A multi-tier grievance escalation flow under IGM 2.0.0. The shopper rejects initial resolution proposals, escalates the dispute to higher grievance redressal authorities (GRO / Arbitrator), reaches a mutually accepted resolution, and receives an authorized replacement garment.

#### 2. API Breakdown & Technical Actions
- **Delivery Steps (1–14)**: Order delivered successfully.
- **`/issue (issue_open)` -> `/on_issue (processing)`**: Initial grievance filed.
- **`on_issue (on_issue_resolution)` [Unsolicited] (BPP -> BAP)**: Seller proposes an initial settlement.
- **`/issue (issue_resolution_reject)` (BAP -> BPP)**: Shopper rejects the proposed resolution as unsatisfactory.
- **`/on_issue (processing_1)` -> `on_issue (resolution_1)`**: Seller reconsiders with a revised proposal.
- **`/issue (issue_escalate)` (BAP -> BPP)**: Shopper escalates grievance to Level 2 (Grievance Redressal Officer / Arbitrator).
- **`/on_issue (processing_2)` -> `on_issue (resolution_2)`**: Escalated resolution published.
- **`/issue (issue_resolution_accept)` (BAP -> BPP)**: Complainant accepts the escalated resolution terms.
- **`/on_issue (on_issue_resolved)` -> `/issue (issue_close)`**: Ticket closed as successfully resolved.
- **`on_update (on_update_igm_replacement)` [Unsolicited] (BPP -> BAP)**: As mandated by the agreement, seller automatically triggers a replacement fulfillment parcel containing the replacement garment.

---

### Flow 12: Order to Confirm with IGM 2.0.0 – Evidence Exchange & Return Resolution

#### 1. Short Description
Validates the interactive evidence-gathering cycle in IGM 2.0.0. The seller requests additional garment photographs, the shopper supplies the evidence, and the seller approves an authorized return and refund workflow.

#### 2. API Breakdown & Technical Actions
- **Delivery Steps (1–14)**: Order delivered.
- **`/issue (issue_open)` -> `/on_issue (processing)`**: Shopper files an issue claiming an incorrect or damaged garment was delivered.
- **`on_issue (on_issue_need_more_info)` [Unsolicited] (BPP -> BAP)**: Seller requests verification proof (e.g. photos of the size label, defect, and packaging barcode).
- **`/issue (issue_info_provided)` (BAP -> BPP)**: Shopper uploads the requested media and explanatory text.
- **`/on_issue (on_issue_provided)` (BPP -> BAP)**: Seller confirms receipt of additional evidence.
- **`on_issue (on_issue_resolution)` [Unsolicited] (BPP -> BAP)**: Seller validates proof and proposes full return and refund resolution.
- **`/issue (issue_resolution_accept)` (BAP -> BPP)**: Shopper accepts the resolution offer.
- **`/on_issue (on_issue_resolved)` -> `/issue (issue_close)`**: Grievance closed as resolved.
- **`on_update (on_update_igm_return)` [Unsolicited] (BPP -> BAP)**: Seller automatically initiates an official return and refund fulfillment workflow for the contested garment.

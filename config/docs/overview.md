# Beauty & Personal Care (ONDC:RET13 1.2.0)

- [Overview](#overview)
- [Participants](#participants)
- [The User Journey](#the-user-journey)
  - [1. Discovery and Catalog Search](#1-discovery-and-catalog-search)
  - [2. Shade/Variant Selection and Serviceability Check](#2-shadevariant-selection-and-serviceability-check)
  - [3. Order Initialization and Shipping Configuration](#3-order-initialization-and-shipping-configuration)
  - [4. Order Confirmation and Payment](#4-order-confirmation-and-payment)
  - [5. Order Processing, Picking, and Protective Packaging](#5-order-processing-picking-and-protective-packaging)
  - [6. Logistics and Courier Assignment](#6-logistics-and-courier-assignment)
  - [7. Order Dispatch, In-Flight Tracking, and Doorstep Delivery](#7-order-dispatch-in-flight-tracking-and-doorstep-delivery)
  - [8. Settlement and Post-Fulfillment](#8-settlement-and-post-fulfillment)
- [Additional Scenarios](#additional-scenarios)
  - [1. Buyer-Initiated Returns (Full and Partial Order)](#1-buyer-initiated-returns-full-and-partial-order)
  - [2. Buyer-Side Order Cancellation](#2-buyer-side-order-cancellation)
  - [3. Merchant-Side Part-Cancellation and Return to Origin (RTO)](#3-merchant-side-part-cancellation-and-return-to-origin-rto)
  - [4. Out of Stock and Shade Variant Depletion](#4-out-of-stock-and-shade-variant-depletion)
  - [5. Incremental Catalog Refresh (Push and Pull)](#5-incremental-catalog-refresh-push-and-pull)
  - [6. Statutory Compliance & Cosmetics Regulation (Drugs & Cosmetics Act)](#6-statutory-compliance--cosmetics-regulation-drugs--cosmetics-act)
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
  - [Flow 11: Order to Confirm with IGM 2.0.0 – Rejection, Escalation & Return](#flow-11-order-to-confirm-with-igm-200--rejection-escalation--return)
  - [Flow 12: Order to Confirm with IGM 2.0.0 – Evidence Exchange & Item Replacement](#flow-12-order-to-confirm-with-igm-200--evidence-exchange--item-replacement)

---

## Overview

The Beauty & Personal Care domain (**ONDC:RET13**, specification version **1.2.0**) establishes an open, interoperable digital commerce standard for cosmetics, skincare, haircare, fragrances, bath & body, personal hygiene, men's grooming, and baby care products across the Open Network for Digital Commerce (ONDC). BPC retail is characterized by diverse product forms (creams, serums, powders, sprays, liquid flacons), variant hierarchies (foundation shades, lipstick tones, volume sizes in ml/g), strict consumer health and statutory requirements (Drugs & Cosmetics Act 1940, Cosmetics Rules 2020, Legal Metrology Packaged Commodities Rules), fragile/leak-proof packaging considerations, and hygiene-governed post-purchase lifecycles.

ONDC unbundles the traditionally centralized beauty retail marketplace. Shoppers can discover products from independent pharmacies, specialized beauty boutiques, direct-to-consumer (D2C) cosmetic brands, and national retail chains using their preferred **Buyer Application (BAP)**. Sellers manage their inventory, batch numbers, manufacturing licenses, expiry dates, and pricing through a **Seller Application (BPP)**, while integrated **Logistics Service Providers (LSPs)** handle hyperlocal same-day delivery or intercity surface/air parcel transit with specialized cushioning for fragile glass flacons and liquid containers.

The protocol standardizes all network interactions across:
- **Discovery**: `/search` and `/on_search` (city-wide broadcast queries, category taxonomies, shade/variant structures, incremental push/pull).
- **Ordering**: `/select`, `/on_select`, `/init`, `/on_init`, `/confirm`, and `/on_confirm`.
- **Fulfillment & Real-time Tracking**: unsolicited `/on_status` lifecycle events (`Accepted`, `Packed`, `Agent-assigned`, `Order-picked-up`, `Out-for-delivery`, `Order-delivered`), `/track`, and `/on_track`.
- **Post-Order Lifecycle & Exceptions**: `/update`, `/on_update`, `/cancel`, and `/on_cancel` (buyer returns for damaged/leaked items, reverse logistics pickup, warehouse verification, merchant part-cancellations, and Return to Origin / RTO).
- **Grievance Redressal**: Issue and Grievance Management under both **IGM 1.0.0** and **IGM 2.0.0** architectures.

---

## Participants

| Participant | What This Means |
|---|---|
| **Buyer Application (BAP)** | The consumer-facing platform (e.g. beauty shopping apps, super-apps, banking/UPI platforms) where consumers search BPC catalogs, filter by brand, skin/hair type, ingredient preferences, and cosmetic shades, configure delivery addresses, complete digital payments, track delivery couriers, and raise post-delivery grievances. |
| **Seller Application (BPP)** | An application representing beauty retailers, pharmacies, cosmetics distributors, salons, or D2C skincare brands. The BPP publishes item catalogs with variant attributes (volume, shade, active ingredients, expiry dates), checks delivery serviceability, calculates itemized quotes, coordinates warehouse picking and protective bubble-wrapping, and processes returns or replacements. |
| **Logistics Service Provider (LSP)** | A delivery network participant that executes hyperlocal same-day delivery or intercity surface/air shipping. In seller-managed delivery, the BPP or its integrated delivery partner allocates couriers, provides live GPS tracking, and conducts reverse logistics return pickups. |
| **Gateway** | The ONDC routing infrastructure that multicasts broadcast discovery requests (`/search`) from BAPs to active seller applications (BPPs) based on domain code (`ONDC:RET13`), city code (e.g. `std:080`), and geolocation parameters. |

---

## The User Journey

The standard BPC ordering journey (`Order_to_confirm_to_fulfillment_(Prepaid)`) enables a shopper to discover beauty and personal care items, select specific shades or volume variants, review transparent price breakdowns and turnaround times, provide delivery coordinates, complete payment, and receive carefully packaged goods with end-to-end shipment tracking.

### 1. Discovery and Catalog Search

The shopper initiates discovery on the BAP by searching for BPC categories, brands, or product types (e.g., "Vitamin C Serum", "Matte Lipstick", "Sunscreen SPF 50", "Anti-Dandruff Shampoo"):

- **Intent Broadcast**: The BAP transmits a `/search` request specifying domain category (`ONDC:RET13`), buyer delivery GPS coordinates and area pin code, and fulfillment type (`Delivery`).
- **Catalog Delivery**: Active BPC BPPs within serviceable delivery range respond via asynchronous `/on_search` payloads containing their store catalog (`bpp/providers[]`). This includes product categories, brand details, shade options, volume/weight (ml/g), ingredient lists, MRP, selling price, expiry/best-before dates, and statutory regulatory declarations.

### 2. Shade/Variant Selection and Serviceability Check

The shopper selects specific items with desired volume sizes or cosmetic shades and adds them to their cart:

- **Network interaction:**
  - **`/select` (BAP -> BPP)**: The BAP transmits selected item IDs, variant SKUs (e.g. 50ml bottle, Shade #04 Warm Nude), quantities, store location ID, and delivery destination coordinates (`fulfillments[0].end.location.gps` and `address.area_code`).
  - **`/on_select` (BPP -> BAP)**: The seller validates real-time inventory and delivery serviceability. The seller returns an itemized price quote (`quote.breakup[]`) breaking down base item prices, delivery charges (`@ondc/org/title_type="delivery"`), packaging fees, applicable taxes (CGST/SGST), and estimated turnaround time (`@ondc/org/TAT`). If a shade variant is out of stock, the seller returns error code `40002` or `30009`.

### 3. Order Initialization and Shipping Configuration

The shopper provides finalized delivery and billing details:

- **Network interaction:**
  - **`/init` (BAP -> BPP)**: The BAP transmits the shopper's full shipping address (flat/house number, building, street, landmark, area code), contact details (phone, email), billing address, and payment preferences.
  - **`/on_init` (BPP -> BAP)**: The seller freezes the order quote, specifies static/dynamic cancellation terms and return window (`@ondc/org/return_window`, e.g. `P7D` for 7-day return eligibility), sets payment collection rules, and returns settlement fee details.

### 4. Order Confirmation and Payment

The shopper completes digital prepaid payment:

- **Network interaction:**
  - **`/confirm` (BAP -> BPP)**: The BAP captures digital payment, generates the formal order ID (`order.id`), and transmits payment confirmation parameters (`payment.params.transaction_id`, `payment.status = "PAID"`).
  - **`/on_confirm` (BPP -> BAP)**: The seller validates payment, records the order in its Warehouse Management System (WMS), sets `order.state = "Created"`, and establishes initial fulfillment state `Pending`.

### 5. Order Processing, Picking, and Protective Packaging

The beauty retailer or warehouse team picks the specific product batch, verifies expiry dates, and packs the cosmetics with protective cushioning:

- **`on_status (Accepted)` [Unsolicited] (BPP -> BAP)**: Unsolicited status update indicating the merchant has accepted the order (`order.state = "Accepted"`).
- **`on_status (Packed)` [Unsolicited] (BPP -> BAP)**: Unsolicited status update confirming the cosmetics have been checked for seal integrity, wrapped in protective bubble wrap/cushioning (essential for glass dropper serums and perfumes), boxed, sealed with tamper tape, and labeled with a shipping barcode (`order.state = "In-progress"`, `fulfillment.state = "Packed"`).

### 6. Logistics and Courier Assignment

A delivery partner or courier executive is assigned to the parcel:

- **`on_status (Agent-assigned)` [Unsolicited] (BPP -> BAP)**: The logistics provider allocates a courier agent or assigns an airway bill (AWB) number. The payload provides delivery agent credentials (`fulfillments[0].agent.name`, `agent.phone`).

### 7. Order Dispatch, In-Flight Tracking, and Doorstep Delivery

The courier collects the packaged cosmetics from the store/warehouse and transports them to the buyer's destination:

- **`on_status (Order-picked-up)` [Unsolicited] (BPP -> BAP)**: Seller notifies that the courier has picked up the package from the store (`fulfillment.state = "Order-picked-up"`), recording `fulfillments[0].start.time.timestamp`.
- **`/track` & `/on_track` (BAP $\leftrightarrow$ BPP)**: The BAP polls for live shipment tracking URL / GPS coordinates.
- **`on_status (Out-for-delivery)` [Unsolicited] (BPP -> BAP)**: Triggered when the last-mile delivery courier is out for doorstep delivery.
- **`on_status (Order-delivered)` [Unsolicited] (BPP -> BAP)**: Sent upon successful physical delivery at the buyer's address (`fulfillment.state = "Order-delivered"`, `order.state = "Completed"`), recording `fulfillments[0].end.time.timestamp` and electronic proof of delivery (ePOD / delivery OTP).

### 8. Settlement and Post-Fulfillment

Following successful delivery and expiry of the return window, financial reconciliation takes place. The BAP releases funds to the seller according to agreed settlement windows (T+1 / T+2), withholding agreed buyer finder fees and routing statutory tax deductions where applicable.

---

## Additional Scenarios

Beauty and Personal Care retail involves specialized operational conditions that diverge from the happy path, particularly regarding hygiene return rules, damaged/leaked cosmetics, and out-of-stock shades.

### 1. Buyer-Initiated Returns (Full and Partial Order)

Due to health and hygiene standards, cosmetics and personal care products with opened seals or used contents are strictly non-returnable. However, post-delivery returns and refunds are fully supported for legitimate defects:
- **Return Eligibility**: Broken/shattered glass containers (e.g. perfumes, serums), leaked liquids/creams in transit, expired or near-expiry batches delivered, broken tamper-evident seals, or wrong shade/product delivered.
- **Return Initiation (`update_return`)**: Within the return window (`@ondc/org/return_window`, e.g. 7 days), the buyer requests a return for the entire order or specific items (partial return), providing item IDs, quantities, return reason codes (e.g., `001` - Damaged/Leaked, `002` - Expired product, `003` - Wrong shade/item), and photos of the defective package.
- **Acknowledgment & Approval (`on_update_return_init` & `on_update_return_approved`)**: The seller acknowledges the return request (`Return_Initiated`) and issues authorization (`return_approved`).
- **Reverse Logistics Collection (`on_update_return_picked`)**: A reverse logistics courier collects the parcel from the consumer.
- **Refund Settlement (`update_settlement_trail`)**: The BAP transmits bank account/UPI settlement instructions to credit the consumer.
- **Delivery at Merchant Facility (`on_update_return_delivered`)**: The parcel arrives at the seller warehouse, where merchant staff inspect container condition and confirm full refund execution.

### 2. Buyer-Side Order Cancellation

A consumer may cancel an order before the seller has dispatched the parcel:
- **`/cancel` (BAP -> BPP)**: The BAP transmits a cancellation request with an ONDC cancellation reason code (`order.cancellation_reason_id = "001"`).
- **`/on_cancel` (BPP -> BAP)**: The seller validates that the order is within its cancellable window (`@ondc/org/cancellable = true`), terminates fulfillment, sets `order.state = "Cancelled"` and `fulfillment.state = "Cancelled"`, recalculates any applicable fee deductions, and provides refund instructions.

### 3. Merchant-Side Part-Cancellation and Return to Origin (RTO)

Hyperlocal and intercity BPC fulfillment encounters situations where specific cosmetic shades or batches are unavailable during picking, or where a delivery attempt fails:
- **Partial Order Cancellation (`on_update_part_cancel`)**: If one cosmetic item in a multi-item order is found out of stock, near expiry, or damaged during warehouse picking, the seller sends an unsolicited `/on_update` adjusting `quote.breakup`. The BAP responds with `/update (update_settlement_trail)` to credit the differential refund.
- **Return to Origin (`on_cancel_rto`)**: When the courier attempts delivery but the customer is unreachable, rejects delivery, or provides an incorrect address, the seller initiates RTO with cancellation reason codes `011`–`015`. The parcel is routed back to the merchant store/warehouse (`on_status_rto_delivered`), and settlement trails are adjusted for reverse transit costs.

### 4. Out of Stock and Shade Variant Depletion

When a consumer selects a specific cosmetic shade or size SKU whose inventory was just depleted:
- **Error Response (`on_select_out_of_stock`)**: The seller returns an error block containing ONDC error code `40002` (Out of Stock) or `30009` and item availability details (`quantity.available.count = 0`).
- **Shopper Reconfiguration**: The BAP displays the out-of-stock notification, allowing the shopper to pick an alternative shade or volume variant.

### 5. Incremental Catalog Refresh (Push and Pull)

BPC catalogs, seasonal collections, flash beauty sales, and shade availability fluctuate continuously:
- **Incremental Push (`Search_and_Custom_Menu__Incremental_Push_`)**: The seller broadcasts real-time price drops, stock replenishment, new product launches, or temporary store closures (`on_search_inc_close`) via unsolicited `/on_search` payloads.
- **Incremental Pull (`Discovery_Flow_incremental_catalog_refresh_pull`)**: The buyer application queries the seller for catalog changes that occurred since a specific timestamp (`last_updated_at`), minimizing network bandwidth while keeping local caches synchronized.

### 6. Statutory Compliance & Cosmetics Regulation (Drugs & Cosmetics Act)

Cosmetics and personal care items are strictly regulated under the Drugs and Cosmetics Act (1940), Cosmetics Rules (2020), and Legal Metrology (Packaged Commodities) Rules:
- Product listings must include manufacturing license number, batch/lot number, expiry date or "best before" period, complete list of ingredients (INCI standard), country of origin, manufacturer/packer/importer details, net quantity (volume in ml or net weight in g), directions for safe use, and allergen/safety warnings (e.g. "perform patch test before use").

---

## Issue and Grievance Management

The BPC domain provides robust complaint handling across both ONDC Issue and Grievance Management (IGM) framework versions.

### 1. IGM 1.0.0 Architecture

In IGM 1.0.0, grievances follow a linear status progression:
1. **`issue (open)` (BAP -> BPP)**: The shopper files a complaint against an order or item (e.g., "Leaked shampoo bottle", "Shattered perfume glass", "Expired cream delivered", "Broken pump dispenser"), providing descriptions, photos, and complainant details.
2. **`on_issue (processing)` (BPP -> BAP)**: The seller acknowledges receipt of the complaint, providing a grievance ticket ID, respondent details, and expected Resolution Time (TAT).
3. **`on_issue_status (resolved)` (BPP -> BAP)**: The seller investigates and publishes a formal resolution (`REFUND`, `REPLACEMENT`, or `NO_ACTION`) with resolution remarks.
4. **`issue (close)` (BAP -> BPP)**: The shopper reviews the resolution and closes the grievance ticket.

### 2. IGM 2.0.0 Architecture

IGM 2.0.0 introduces multi-party interactions, evidence exchange, dispute escalation, and automated fulfillment linkages:
- **Evidence Exchange & Item Replacement (`Order_to_confirm_to_fulfillment__Prepaid_with_IGM_v-2.0.0`)**: The seller requests photos of the damaged container or batch label (`on_issue_need_more_info`), the shopper uploads the proof (`issue_info_provided`), and the seller proposes a replacement (`action_triggered = "REPLACEMENT"`), automatically dispatching a replacement cosmetic item (`on_update_igm_replacement`).
- **No-Action Resolution (`Order_to_confirm_to_fulfillment__Prepaid_with_IGM_No_Action_v-2.0.0`)**: The seller investigates and tenders an explanatory resolution with `action_triggered = "NO_ACTION"`, accepted by the shopper, followed by post-resolution order audit status (`on_status_igm_3`).
- **Rejection, Escalation & Return (`Order_to_confirm_to_fulfillment__Prepaid_with_IGM_Rejection_v-2.0.0`)**: The shopper rejects initial resolution proposals (`issue_resolution_reject`), escalates the dispute to Level 2 (Grievance Redressal Officer / Arbitrator), reaches an accepted binding resolution, and receives an authorized return/refund (`on_update_igm_return`).

---

## Detailed Protocol Flows

### Flow 1: Order to Confirm to Fulfillment (Prepaid Standard Delivery)

#### 1. Short Description
The primary forward-fulfillment BPC purchase journey. A shopper selects cosmetics or personal care items and shade/size variants, receives an itemized quote with delivery fees and taxes, provides shipping addresses, pays upfront, and receives the goods through seller-managed delivery with live courier tracking and delivery verification.

#### 2. API Breakdown & Technical Actions
- **`/select` (BAP -> BPP)**: The BAP transmits selected cosmetic item IDs, shade/volume variant codes, quantities, store location ID, and delivery coordinates (`fulfillments[0].end.location.gps` and `address.area_code`).
- **`/on_select` (BPP -> BAP)**: The seller validates store inventory and delivery radius. It returns an itemized price quote (`quote.breakup[]`) with base product prices, delivery fees (`@ondc/org/title_type="delivery"`), packaging fees, and delivery turnaround time (`@ondc/org/TAT`).
- **`/init` (BAP -> BPP)**: The shopper inputs full shipping destination (house/flat, building, street, city, pin code) and contact details.
- **`/on_init` (BPP -> BAP)**: The seller freezes the order quote, specifies cancellation terms, publishes the return window (`@ondc/org/return_window = "P7D"`), and provides payment collection instructions.
- **`/confirm` (BAP -> BPP)**: The BAP collects payment digitally, binds the transaction with `payment.status = "PAID"`, and sends the final order commitment.
- **`/on_confirm` (BPP -> BAP)**: The seller confirms order acceptance, assigning an official `order.id` with state `Created` and fulfillment state `Pending`.
- **`on_status (on_status_pending)` [Unsolicited] (BPP -> BAP)**: Merchant marks order as accepted for fulfillment (`order.state = "Accepted"`).
- **`on_status (on_status_packed)` [Unsolicited] (BPP -> BAP)**: Products picked, inspected for seal integrity, cushioned in bubble wrap, and packed into parcel with shipping label (`fulfillment.state = "Packed"`, `order.state = "In-progress"`).
- **`on_status (on_status_agent_assigned)` [Unsolicited] (BPP -> BAP)**: Delivery courier assigned; payload includes courier name, mobile number, and tracking ID.
- **`on_status (on_status_picked)` [Unsolicited] (BPP -> BAP)**: Courier collects package from store/warehouse (`fulfillment.state = "Order-picked-up"`, with pickup timestamp).
- **`/track` & `/on_track` (BAP $\leftrightarrow$ BPP)**: BAP requests live tracking URL / endpoint for real-time shipment progress.
- **`on_status (on_status_out_for_delivery)` [Unsolicited] (BPP -> BAP)**: Courier is out for delivery to shopper's doorstep (`fulfillment.state = "Out-for-delivery"`).
- **`on_status (on_status_order_delivered)` [Unsolicited] (BPP -> BAP)**: Package successfully delivered with delivery timestamp and electronic proof of delivery (`fulfillment.state = "Order-delivered"`, `order.state = "Completed"`).

---

### Flow 2: Buyer-Initiated Return (Full Order and Partial Order)

#### 1. Short Description
Covers the post-delivery return lifecycle for BPC products. The shopper requests a return for delivered items (e.g., shattered perfume bottle, spilled shampoo, or wrong foundation shade delivered) within the return window. The merchant approves the request, reverse logistics pickup is executed, condition is validated, and full refund settlement is processed.

#### 2. API Breakdown & Technical Actions
- **Forward Delivery Completion (Steps 1–12)**: Order delivered with full `on_status` sequence (`accepted` $\rightarrow$ `packed` $\rightarrow$ `agent_assigned` $\rightarrow$ `picked` $\rightarrow$ `out_for_delivery` $\rightarrow$ `order_delivered`).
- **`/update (update_return)` (BAP -> BPP)**: Shopper submits a return request for specific delivered items, supplying return reason codes (e.g., `001` - Damaged/leaked product), item quantities, and return photos.
- **`/on_update (on_update_return_init)` (BPP -> BAP)**: Seller logs return request in state `Return_Initiated`.
- **`on_update (on_update_return_approved)` [Unsolicited] (BPP -> BAP)**: Seller reviews and accepts the return request, authorizing reverse logistics pickup.
- **`on_update (on_update_return_picked)` [Unsolicited] (BPP -> BAP)**: Reverse logistics courier inspects packaging and collects the parcel from the consumer.
- **`/update (update_settlement_trail)` (BAP -> BPP)**: Buyer application supplies bank account / UPI refund settlement instructions.
- **`on_update (on_update_return_delivered)` [Unsolicited] (BPP -> BAP)**: Items reach seller warehouse; merchant validates condition and confirms full refund execution.

---

### Flow 3: Buyer-Side Order Cancellation

#### 1. Short Description
Exercises the process of a consumer cancelling a placed BPC order prior to merchant dispatch, ensuring the seller halts picking, updates order status to `Cancelled`, and triggers refund processing.

#### 2. API Breakdown & Technical Actions
- **Steps 1–6 (`/select` to `/on_confirm`)**: Shopper places and confirms a prepaid cosmetics order.
- **`/cancel` (BAP -> BPP)**: Shopper triggers cancellation from the app before merchant dispatch, supplying a standard ONDC cancellation reason code (`order.cancellation_reason_id = "001"`).
- **`/on_cancel` (BPP -> BAP)**: The seller validates that the order is within the cancellable window (`@ondc/org/cancellable = true`). The seller terminates fulfillment, updates `order.state = "Cancelled"` and `fulfillment.state = "Cancelled"`, recalculates any applicable fee deductions, and provides refund instructions.

---

### Flow 4: Merchant-Side Part-Order Cancellation and Return to Origin (RTO)

#### 1. Short Description
A multi-exception flow handling merchant inventory stock-outs during warehouse picking, followed by an unsuccessful delivery attempt where the customer is unreachable, culminating in Return to Origin (RTO).

#### 2. API Breakdown & Technical Actions
- **Steps 1–6 (`/select` to `/on_confirm`)**: Order confirmed for multiple BPC items.
- **`on_update (on_update_part_cancel)` [Unsolicited] (BPP -> BAP)**: While picking, the merchant discovers a specific cosmetic shade or batch is unavailable or near expiry. The seller issues an unsolicited update cancelling that specific line item and updating the price quote.
- **`/update (update_settlement_trail)` (BAP -> BPP)**: The BAP acknowledges the item reduction and transmits the updated settlement trail reflecting the partial refund to the customer.
- **Fulfillment Progression (Steps 9–13)**: Remaining items are packed, courier assigned, picked up, and marked out for delivery.
- **`on_cancel (on_cancel_rto)` [Unsolicited] (BPP -> BAP)**: Courier attempts delivery but cannot reach the buyer. The seller initiates RTO with cancellation reason code `013` (Buyer unreachable), reversing route direction.
- **`/update (update_settlement_trail_1)` (BAP -> BPP)**: BAP transmits RTO settlement terms (accounting for return logistics deductions).
- **`on_status (on_status_rto_delivered)` [Unsolicited] (BPP -> BAP)**: Undelivered cosmetics safely returned to merchant warehouse; order marked `Cancelled`.

---

### Flow 5: Out of Stock Error Handling (Inventory Shortage)

#### 1. Short Description
Demonstrates protocol error handling when a shopper attempts to select a BPC catalogue item or cosmetic shade variant that is depleted. The seller platform rejects the selection via `on_select` with error code `40002`/`30009`.

#### 2. API Breakdown & Technical Actions
- **`/select (select0)` (BAP -> BPP)**: Shopper selects cosmetics items with desired shades/volume variants and quantities.
- **`/on_select (on_select_out_of_stock)` (BPP -> BAP)**: Seller identifies that requested variant inventory is exhausted. It returns an error response with error code `40002` (Out of stock) or `30009` and item availability details (`quantity.available.count = 0`), allowing the buyer app to inform the consumer.

---

### Flow 6: Search and Custom Menu – Full Catalog City Discovery

#### 1. Short Description
The foundational discovery flow for BPC retail. A consumer searches for cosmetics and personal care across an entire city or broad geolocation, and the seller returns its comprehensive product catalog, categories, variant options, and serviceability rules.

#### 2. API Breakdown & Technical Actions
- **`/search (search_1)` (BAP -> Gateway)**: BAP broadcasts a city-wide discovery query (`context.city = "std:080"`, `intent.category.id = "ONDC:RET13"`).
- **`/on_search (on_search1)` (BPP -> BAP)**: Seller responds with full catalog:
  - `bpp/providers[]`: Store identity, operating hours, geolocation, and serviceability radiuses.
  - `categories[]`: Hierarchical BPC categories (e.g. Skincare, Haircare, Makeup, Fragrances, Bath & Body).
  - `items[]`: Product descriptions, variant attributes (shade, volume, form, skin type), prices, images, brand names, and Drugs & Cosmetics / Legal Metrology statutory tags.
  - `offers[]`: Available promotional discounts and bundle deals.

---

### Flow 7: Search and Custom Menu – Incremental Catalog Push

#### 1. Short Description
Validates the merchant-initiated incremental catalog push mechanism. Sellers broadcast live updates regarding price alterations, seasonal beauty flash discounts, shade replenishment, new product launches, or temporary store closures without requiring a full catalog reload.

#### 2. API Breakdown & Technical Actions
- **`/search (search_inc)` (BAP -> Gateway)**: Preliminary search establishing active listening.
- **`on_search (on_search_inc)` [Unsolicited] (BPP -> BAP)**: Seller pushes differential item pricing or inventory adjustments.
- **`on_search (on_search_inc_close)` [Unsolicited] (BPP -> BAP)**: Seller signals temporary store closure or disables catalog serviceability.
- **`/search (search_inc1)` (BAP -> Gateway)**: Verification query confirming catalog state consistency.

---

### Flow 8: Discovery Flow – Incremental Catalog Refresh Pull

#### 1. Short Description
Validates the buyer application pull mechanism for catalog synchronization. The buyer requests catalog updates modified after a given timestamp (`last_updated_at`), minimizing network bandwidth while keeping local price and inventory caches fresh.

#### 2. API Breakdown & Technical Actions
- **`/search (search_1)` -> `/on_search (on_search1)`**: Baseline full catalog discovery.
- **`/search (search_inc_pull)` (BAP -> BPP)**: Targeted point-to-point search passing `tags` with `mode = "incremental_refresh"` and `last_updated_at` timestamp.
- **`/on_search (on_search_inc_pull)` (BPP -> BAP)**: Seller responds containing strictly those BPC items whose pricing, inventory, or metadata changed since the requested cutoff.

---

### Flow 9: Order to Confirm with IGM 1.0.0 Resolution

#### 1. Short Description
A complete forward fulfillment flow integrated with the standard IGM 1.0.0 complaint resolution cycle. After receiving cosmetics, the consumer raises a quality or defect grievance, which the merchant investigates, resolves, and closes.

#### 2. API Breakdown & Technical Actions
- **Delivery Steps (1–14)**: Order placed, paid, packed, dispatched, tracked, and delivered.
- **`/issue (issue_open_100)` (BAP -> BPP)**: Shopper files a complaint citing product defects (e.g. broken dropper, leaking bottle, unsealed box), attaching photos and contact info.
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

### Flow 11: Order to Confirm with IGM 2.0.0 – Rejection, Escalation & Return

#### 1. Short Description
A multi-tier grievance escalation flow under IGM 2.0.0. The shopper rejects initial resolution proposals, escalates the dispute to higher grievance redressal authorities (GRO / Arbitrator), reaches a mutually accepted resolution, and receives an authorized return and refund workflow.

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
- **`on_update (on_update_igm_return)` [Unsolicited] (BPP -> BAP)**: As mandated by the agreement, seller automatically triggers an official return and refund workflow for the contested items.

---

### Flow 12: Order to Confirm with IGM 2.0.0 – Evidence Exchange & Item Replacement

#### 1. Short Description
Validates the interactive evidence-gathering cycle in IGM 2.0.0. The seller requests additional photographs of a damaged or leaked cosmetic product, the shopper supplies the evidence, and the seller approves an item replacement, automatically dispatching a replacement BPC parcel.

#### 2. API Breakdown & Technical Actions
- **Delivery Steps (1–14)**: Order delivered.
- **`/issue (issue_open)` -> `/on_issue (processing)`**: Shopper files an issue claiming a cosmetic item was damaged or leaked during transit.
- **`on_issue (on_issue_need_more_info)` [Unsolicited] (BPP -> BAP)**: Seller requests verification proof (e.g. photos of the damaged bottle, batch code, and outer carton).
- **`/issue (issue_info_provided)` (BAP -> BPP)**: Shopper uploads the requested media and explanatory text.
- **`/on_issue (on_issue_provided)` (BPP -> BAP)**: Seller confirms receipt of additional evidence.
- **`on_issue (on_issue_resolution)` [Unsolicited] (BPP -> BAP)**: Seller validates proof and proposes item replacement (`action_triggered = "REPLACEMENT"`).
- **`/issue (issue_resolution_accept)` (BAP -> BPP)**: Shopper accepts the replacement offer.
- **`/on_issue (on_issue_resolved)` -> `/issue (issue_close)`**: Grievance closed as resolved.
- **`on_update (on_update_igm_replacement)` [Unsolicited] (BPP -> BAP)**: Seller automatically generates and triggers a new replacement fulfillment parcel containing the replacement cosmetic item.

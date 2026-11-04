# Retail Fashion (ONDC:RET12 1.2.5)

- [Overview](#overview)
- [Participants](#participants)
- [The User Journey](#the-user-journey)
  - [1. Discovery and Catalog Search](#1-discovery-and-catalog-search)
  - [2. Variant Selection, Sizing, and Serviceability Check](#2-variant-selection-sizing-and-serviceability-check)
  - [3. Order Initialization and Shipping Configuration](#3-order-initialization-and-shipping-configuration)
  - [4. Order Confirmation and Payment](#4-order-confirmation-and-payment)
  - [5. Order Processing, Picking, and Quality Packaging](#5-order-processing-picking-and-quality-packaging)
  - [6. Logistics and Courier Assignment](#6-logistics-and-courier-assignment)
  - [7. Order Dispatch, In-Flight Tracking, and Doorstep Delivery](#7-order-dispatch-in-flight-tracking-and-doorstep-delivery)
  - [8. Settlement and Post-Fulfillment](#8-settlement-and-post-fulfillment)
- [Additional Scenarios & 1.2.5 Enhancements](#additional-scenarios--125-enhancements)
  - [1. Post-Order Garment Replacement Flow (Size / Color Exchange)](#1-post-order-garment-replacement-flow-size--color-exchange)
  - [2. Buyer-Initiated Return with Reverse QC](#2-buyer-initiated-return-with-reverse-qc)
  - [3. Cancel Return Request Flow](#3-cancel-return-request-flow)
  - [4. Mid-Order Address & Buyer Delivery Instructions Update](#4-mid-order-address--buyer-delivery-instructions-update)
  - [5. Cash on Delivery (COD) Payment Flow](#5-cash-on-delivery-cod-payment-flow)
  - [6. Seller Credit Checkout Flow](#6-seller-credit-checkout-flow)
  - [7. Buyer-Side Order Cancellation](#7-buyer-side-order-cancellation)
  - [8. Seller-Initiated Cancellation and RTO](#8-seller-initiated-cancellation-and-rto)
  - [9. Force Cancellation Flow](#9-force-cancellation-flow)
  - [10. Out of Stock Handling (Cart Recovery vs. Immediate Error Rejection)](#10-out-of-stock-handling-cart-recovery-vs-immediate-error-rejection)
  - [11. Incremental Catalog Refresh (Push and Pull)](#11-incremental-catalog-refresh-push-and-pull)
  - [12. Statutory Compliance & Legal Metrology for Apparel](#12-statutory-compliance--legal-metrology-for-apparel)
- [Issue and Grievance Management](#issue-and-grievance-management)
  - [1. IGM 1.0.0 Architecture](#1-igm-100-architecture)
  - [2. IGM 2.0.0 Architecture](#2-igm-200-architecture)
- [Detailed Protocol Flows](#detailed-protocol-flows)
  - [Flow 1: Delivery_Flow (Prepaid Standard Delivery)](#flow-1-delivery_flow-prepaid-standard-delivery)
  - [Flow 2: Replacement_Flow (Garment Replacement & Reverse Logistics)](#flow-2-replacement_flow-garment-replacement--reverse-logistics)
  - [Flow 3: Return_Flow (Buyer Return with Reverse QC & Settlement)](#flow-3-return_flow-buyer-return-with-reverse-qc--settlement)
  - [Flow 4: Cancel_Return_Request_Flow (Cancellation of Active Return Request)](#flow-4-cancel_return_request_flow-cancellation-of-active-return-request)
  - [Flow 5: Buyer_Instructions_And_Delivery_Update_Flow](#flow-5-buyer_instructions_and_delivery_update_flow)
  - [Flow 6: Cash_On_Delivery_Flow (COD Payment & Fulfillment)](#flow-6-cash_on_delivery_flow-cod-payment--fulfillment)
  - [Flow 7: Seller_Cred_Flow (Seller Credit Purchase)](#flow-7-seller_cred_flow-seller-credit-purchase)
  - [Flow 8: Buyer_Cancellation_Flow (Buyer-Initiated Order Cancellation)](#flow-8-buyer_cancellation_flow-buyer-initiated-order-cancellation)
  - [Flow 9: Seller_Cancellation_Flow (Part-Cancel & RTO Disposition)](#flow-9-seller_cancellation_flow-part-cancel--rto-disposition)
  - [Flow 10: Force_Cancellation_Flow (In-Flight Force Cancellation)](#flow-10-force_cancellation_flow-in-flight-force-cancellation)
  - [Flow 11: Out_Of_Stock_Flow (Cart Revision and Stockout Recovery)](#flow-11-out_of_stock_flow-cart-revision-and-stockout-recovery)
  - [Flow 12: Out_Of_Stock_Flow(Error-code) (Immediate Error Rejection)](#flow-12-out_of_stock_flowerror-code-immediate-error-rejection)
  - [Flow 13: Discovery_Flow_full_catalog (City-Wide Full Catalog Search)](#flow-13-discovery_flow_full_catalog-city-wide-full-catalog-search)
  - [Flow 14: Discovery_Flow_incremental_catalog (Incremental Catalog Push)](#flow-14-discovery_flow_incremental_catalog-incremental-catalog-push)
  - [Flow 15: Discovery_Flow_incremental_catalog_refresh_pull (Incremental Pull)](#flow-15-discovery_flow_incremental_catalog_refresh_pull-incremental-pull)
  - [Flow 16: Delivery_Flow_With_IGM(v-1.0.0) (Grievance Resolution v1.0.0)](#flow-16-delivery_flow_with_igmv-100-grievance-resolution-v100)
  - [Flow 17: Delivery_Flow_With_IGM(v-2.0.0) (Evidence Exchange & Return Action)](#flow-17-delivery_flow_with_igmv-200-evidence-exchange--return-action)
  - [Flow 18: Delivery_Flow_With_IGM_No_Action(v-2.0.0) (No-Action Resolution)](#flow-18-delivery_flow_with_igm_no_actionv-200-no-action-resolution)
  - [Flow 19: Delivery_Flow_With_IGM_Rejection(v-2.0.0) (Rejection, Escalation & Replacement)](#flow-19-delivery_flow_with_igm_rejectionv-200-rejection-escalation--replacement)

---

## Overview

The Fashion retail domain (**ONDC:RET12**, specification version **1.2.5**) establishes an open, interoperable digital commerce standard for apparel, clothing, footwear, ethnic wear, innerwear, and fashion accessories across the Open Network for Digital Commerce (ONDC). Fashion retail is distinguished by multi-attribute SKU variant hierarchies (parent products with multiple size, color, fit, and pattern combinations), seasonal inventory turnover, statutory declarations under Legal Metrology (Packaged Commodities) Rules, and high return/replacement rates resulting from tactile, visual, or sizing mismatches.

Historically, offline fashion shops, local garment boutiques, and direct-to-consumer (D2C) apparel labels were dependent on dominant, proprietary e-commerce marketplaces (such as Amazon, Flipkart, or Myntra), incurring steep commission deductions and restrictive merchant policies. ONDC:RET12 levels the playing field:
- **Shoppers** discover clothing from a multitude of local boutiques, regional retail stores, and national apparel brands through any ONDC-enabled **Buyer Application (BAP)**.
- **Fashion Retailers** list their merchandise via a **Seller Application (BPP)**, maintaining complete autonomy over their inventory, pricing, sizing charts, fulfillment policies, and return/replacement eligibility windows.
- **Logistics Providers (LSPs)** execute forward delivery, reverse quality checks (Reverse QC), and return pickups over open protocol rails.

Building upon earlier releases, **version 1.2.5** introduces essential retail capabilities specifically tailored to fashion e-commerce:
- **Dedicated Post-Order Replacement Flow (`Replacement_Flow`)**: End-to-end support for garment size and color exchanges, complete with reverse pickup and replacement parcel dispatch.
- **Cancel Return Request (`Cancel_Return_Request_Flow`)**: Enabling shoppers to revoke an initiated return request before reverse courier pickup.
- **Cash on Delivery (`Cash_On_Delivery_Flow`)**: Standardized COD payment method support across fashion ordering journeys.
- **Seller Credit Checkout (`Seller_Cred_Flow`)**: Enabling retail purchases under pre-approved seller credit terms.
- **Mid-Order Address & Buyer Instructions Update**: Allowing shoppers to modify drop-off addresses or communicate special delivery notes post-confirmation prior to courier dispatch.
- **Comprehensive Cancellation & Stockout Handlers**: Dedicated flows for seller-initiated cancellations, forced transit cancellations, graceful cart recovery, and immediate out-of-stock error codes.
- **Advanced Grievance Framework**: Complete IGM 1.0.0 and 2.0.0 support, including replacement dispatch and evidence verification.

---

## Participants

| Participant | What This Means |
|---|---|
| **Buyer Application (BAP)** | The consumer-facing platform (e.g. fashion e-commerce apps, banking/UPI apps, telco marketplaces) where consumers discover fashion catalogs, filter by size, color, and gender, configure delivery addresses, select payment options (prepaid or COD), track shipments, and request returns or size exchanges. |
| **Seller Application (BPP)** | An application representing clothing stores, fashion labels, garment manufacturers, or D2C apparel brands. The BPP publishes product catalogs with variant attributes (size, color, material), validates delivery serviceability, provides itemized pricing and delivery quotes, manages picking and packing, and processes reverse returns. |
| **Logistics Service Provider (LSP)** | A delivery network participant that executes hyperlocal same-day delivery or intercity surface/air logistics. In seller-managed delivery, the BPP or its integrated logistics partner coordinates pickup, transit, delivery verification, and reverse logistics return pickups. |
| **Gateway** | The ONDC routing infrastructure that multicasts broadcast discovery requests (`/search`) from BAPs to active seller applications (BPPs) based on domain code (`ONDC:RET12`), city code (e.g. `std:080`), and geolocation parameters. |

---

## The User Journey

The standard fashion ordering journey (`Delivery_Flow`) enables a shopper to discover clothing items, select precise size and color variants, review transparent price breakdowns and estimated delivery windows, pay digitally, and receive packed garments with end-to-end shipment milestone tracking.

### 1. Discovery and Catalog Search

The shopper initiates discovery on the BAP by searching for apparel categories, styles, or brands (e.g., "Men's Slim Fit Jeans", "Cotton T-Shirts", "Kurtis"):

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

### 5. Order Processing, Picking, and Quality Packaging

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

Following successful delivery and expiry of the return window, financial reconciliation takes place. The BAP releases funds to the seller according to agreed settlement windows (T+1 / T+2), withholding agreed buyer finder fees and routing statutory tax deductions where applicable.

---

## Additional Scenarios & 1.2.5 Enhancements

Version 1.2.5 formalizes comprehensive operational variations to support real-world fashion commerce dynamics.

### 1. Post-Order Garment Replacement Flow (Size / Color Exchange)

Fashion e-commerce requires seamless item replacement when a delivered garment does not fit or has a color/fabric mismatch:
- **Replacement Request (`update_reverse_qc_rep`)**: The consumer initiates a replacement request within the return window, specifying replacement reason codes (e.g., incorrect size) and reverse QC parameters.
- **Approval & Reverse Pickup (`on_update_return_approved` & `on_update_return_picked_rep`)**: The seller acknowledges and approves the request, dispatching a reverse logistics courier to collect the original garment.
- **Warehouse Receipt (`on_update_return_delivered_rep`)**: The returned garment arrives at the seller warehouse and passes QC verification.
- **Replacement Dispatch & Delivery (`on_status_packed_rep` $\rightarrow$ `on_status_order_delivered_rep`)**: The merchant packs the replacement size SKU, dispatches it via forward logistics, and completes doorstep handover.

### 2. Buyer-Initiated Return with Reverse QC

- **Return Initiation (`update_reverse_qc`)**: Shopper requests return for delivered garments, providing item IDs, quantities, return reason codes, and reverse quality check parameters.
- **Approval & Reverse Pickup (`on_update_return_approved` & `on_update_return_picked`)**: Seller authorizes return and dispatches reverse courier.
- **Settlement & Delivery (`update_reverse_qc_settlement` & `on_update_return_delivered`)**: The BAP transmits refund payment details, and the seller confirms receipt and executes refund.

### 3. Cancel Return Request Flow

Consumers sometimes change their mind after requesting a return (e.g. deciding to keep the garment or gifting it):
- After initiating a return request (`update_reverse_qc`) and receiving seller approval (`on_update_return_approved`), the shopper triggers `/cancel (cancel_return_request)`.
- The seller verifies that the reverse courier has not yet picked up the item, acknowledges via `/on_cancel (on_cancel_return_request)`, and closes the return request while maintaining order state as completed.

### 4. Mid-Order Address & Buyer Delivery Instructions Update

Consumers frequently need to adjust delivery details after checkout before courier dispatch:
- **Buyer Instructions (`update_buyer_instructions`)**: Shopper transmits special instructions (e.g., "leave with neighbor", "call upon reaching security gate") via `/update`.
- **Address Update (`update_delivery_address`)**: Shopper submits corrected delivery address details via `/update`.
- **Delivery Authorization (`on_update_delivery_auth`)**: Seller transmits delivery authentication codes (e.g. OTP requirements) prior to final doorstep delivery.

### 5. Cash on Delivery (COD) Payment Flow

To serve shoppers who prefer paying upon physical parcel receipt:
- The payment method is set to Cash on Delivery during checkout (`init_cod` and `confirm_cod`).
- Fulfillment proceeds normally through packing, courier pickup, and transit.
- Upon doorstep handover, the courier collects cash/UPI payment and triggers `on_status_order_delivered_cod`.

### 6. Seller Credit Checkout Flow

Supports B2B or consumer credit terms:
- Checkout is executed under approved seller credit terms (`confirm_seller_cred` and `on_confirm_seller_cred`), establishing payment liabilities without upfront digital debit.

### 7. Buyer-Side Order Cancellation

Shopper cancels an order prior to merchant dispatch:
- `/cancel` submitted with cancellation reason code `001`.
- Seller acknowledges via `/on_cancel`, transitions order state to `Cancelled`, and triggers refund.

### 8. Seller-Initiated Cancellation and RTO

- **Partial Cancellation**: Merchant identifies that a specific size/color SKU is unavailable during warehouse picking (`on_update_part_cancel`), prompting a partial refund settlement (`update_partial_cancel_settlement`).
- **Return to Origin (RTO)**: Courier attempts delivery but customer is unreachable; seller initiates RTO (`on_cancel_rto`), parcel is returned to warehouse (`on_status_rto_delivereddisposed`), and reverse shipping deductions are settled (`update_partial_cancel_settlement_1`).

### 9. Force Cancellation Flow

Handles forced system or seller cancellation post-confirmation due to critical logistical failures:
- `/cancel (cancel_yes)` issued after fulfillment progression.
- Seller confirms via `/on_cancel (on_cancel_yes)` and BAP issues refund settlement (`update_settlement_cancel`).

### 10. Out of Stock Handling (Cart Recovery vs. Immediate Error Rejection)

- **Cart Recovery (`Out_Of_Stock_Flow`)**: Shopper encounters an out-of-stock response during selection (`on_select_out_of_stock`), updates selection to an available size/item (`select`), and proceeds through confirmation to delivery.
- **Immediate Error Rejection (`Out_Of_Stock_Flow(Error-code)`)**: Selection is immediately rejected with error code `40002` (Out of stock) or `30009`.

### 11. Incremental Catalog Refresh (Push and Pull)

- **Push (`Discovery_Flow_incremental_catalog`)**: Seller broadcasts live price alterations, stock replenishment, new style drops, or temporary store closures (`on_search_inc_disable`).
- **Pull (`Discovery_Flow_incremental_catalog_refresh_pull`)**: Buyer queries delta updates using timestamp cutoff (`last_updated_at`).

### 12. Statutory Compliance & Legal Metrology for Apparel

- Product listings must include manufacturer/packer/importer name and address, country of origin, net quantity, consumer care details, month and year of manufacture/import, and exact size measurements (e.g., chest, waist, length in cm and inches).

---

## Issue and Grievance Management

The fashion domain provides robust complaint handling across both ONDC Issue and Grievance Management (IGM) framework versions.

### 1. IGM 1.0.0 Architecture

1. **`issue (open)` (BAP -> BPP)**: Shopper files a grievance citing garment defects, wrong size, or transit damage.
2. **`on_issue (processing)` (BPP -> BAP)**: Seller acknowledges receipt with ticket ID and resolution TAT.
3. **`on_issue_status (resolved)` (BPP -> BAP)**: Seller investigates and publishes resolution (`REFUND`, `REPLACEMENT`, or `NO_ACTION`).
4. **`issue (close)` (BAP -> BPP)**: Shopper confirms resolution and closes the issue.

### 2. IGM 2.0.0 Architecture

- **Evidence Exchange (`Delivery_Flow_With_IGM(v-2.0.0)`)**: Seller requests photo proof of tags/defects (`on_issue_need_more_info`), shopper uploads images (`issue_info_provided`), seller proposes resolution, accepted by shopper, triggering return workflow (`on_update_igm_return`).
- **No-Action Resolution (`Delivery_Flow_With_IGM_No_Action(v-2.0.0)`)**: Seller provides an explanatory resolution with `action_triggered = "NO_ACTION"`, accepted by shopper, followed by post-resolution order audit status (`on_status_igm_3`).
- **Rejection, Escalation & Replacement (`Delivery_Flow_With_IGM_Rejection(v-2.0.0)`)**: Shopper rejects initial resolution, escalates to Level 2 (GRO / Arbitrator), escalated authority issues binding resolution, accepted by shopper, triggering replacement garment parcel dispatch (`on_update_igm_replacement`).

---

## Detailed Protocol Flows

### Flow 1: Delivery_Flow (Prepaid Standard Delivery)

#### 1. Short Description
The primary forward-fulfillment fashion purchase journey. A shopper selects clothing items and size variants, receives an itemized quote with delivery fees and taxes, provides shipping addresses, pays upfront, and receives the goods through seller-managed delivery with live courier tracking and delivery verification.

#### 2. API Breakdown & Technical Actions
- **`/select` (BAP -> BPP)**: The BAP transmits selected garment item IDs, size/color variant codes, quantities, store location ID, and delivery coordinates.
- **`/on_select` (BPP -> BAP)**: Seller validates inventory and delivery radius, returning itemized quote (`quote.breakup[]`) with base garment prices, delivery charges, packaging fees, CGST/SGST taxes, and estimated turnaround time (`@ondc/org/TAT`).
- **`/init` (BAP -> BPP)**: Shopper inputs shipping address (building, street, city, pin code) and contact details.
- **`/on_init` (BPP -> BAP)**: Seller freezes order quote, specifies cancellation terms, publishes return window (`@ondc/org/return_window = "P7D"`), and returns payment terms.
- **`/confirm` (BAP -> BPP)**: BAP collects digital payment and sends confirmed order payload (`payment.status = "PAID"`).
- **`/on_confirm` (BPP -> BAP)**: Seller confirms order placement, assigning `order.id` with state `Created` and fulfillment state `Pending`.
- **`on_status (on_status_pending)` [Unsolicited] (BPP -> BAP)**: Merchant marks order accepted (`order.state = "Accepted"`).
- **`on_status (on_status_packed)` [Unsolicited] (BPP -> BAP)**: Garments picked, quality-checked, and packed into parcel (`fulfillment.state = "Packed"`, `order.state = "In-progress"`).
- **`on_status (on_status_agent_assigned)` [Unsolicited] (BPP -> BAP)**: Courier assigned with agent name and phone.
- **`on_status (on_status_picked)` [Unsolicited] (BPP -> BAP)**: Courier collects package from warehouse (`fulfillment.state = "Order-picked-up"`).
- **`/track` & `/on_track` (BAP $\leftrightarrow$ BPP)**: BAP polls for live shipment tracking URL / GPS coordinates.
- **`on_status (on_status_out_for_delivery)` [Unsolicited] (BPP -> BAP)**: Courier is out for doorstep delivery (`fulfillment.state = "Out-for-delivery"`).
- **`on_status (on_status_order_delivered)` [Unsolicited] (BPP -> BAP)**: Package successfully delivered with electronic proof of delivery (`fulfillment.state = "Order-delivered"`, `order.state = "Completed"`).

---

### Flow 2: Replacement_Flow (Garment Replacement & Reverse Logistics)

#### 1. Short Description
A complete 20-step post-order replacement journey for fashion apparel. A shopper requests an exchange for a delivered garment (e.g., swapping for an alternative size), the seller approves the exchange, reverse logistics collects the original item, and the seller dispatches and delivers the replacement garment.

#### 2. API Breakdown & Technical Actions
- **Forward Fulfillment (Steps 1–11)**: Garment selected, initialized, confirmed, packed, picked up, transported, and delivered (`on_status_order_delivered`).
- **`/update (update_reverse_qc_rep)` (BAP -> BPP)**: Shopper initiates a replacement request, supplying reason codes (e.g. size exchange), item IDs, and reverse QC parameters.
- **`/on_update (on_update_interim_reverseQc)` (BPP -> BAP)**: Seller records replacement request in state `Return_Initiated`.
- **`on_update (on_update_return_approved)` [Unsolicited] (BPP -> BAP)**: Seller authorizes replacement and reverse pickup.
- **`on_update (on_update_return_picked_rep)` [Unsolicited] (BPP -> BAP)**: Reverse logistics courier collects original garment from consumer.
- **`on_update (on_update_return_delivered_rep)` [Unsolicited] (BPP -> BAP)**: Original garment arrives at seller warehouse and passes QC verification.
- **`on_status (on_status_packed_rep)` [Unsolicited] (BPP -> BAP)**: Seller packs replacement garment parcel.
- **`on_status (on_status_picked_rep)` [Unsolicited] (BPP -> BAP)**: Courier collects replacement parcel from warehouse.
- **`on_status (on_status_out_for_delivery_rep)` [Unsolicited] (BPP -> BAP)**: Replacement parcel out for delivery.
- **`on_status (on_status_order_delivered_rep)` [Unsolicited] (BPP -> BAP)**: Replacement garment successfully delivered to consumer.

---

### Flow 3: Return_Flow (Buyer Return with Reverse QC & Settlement)

#### 1. Short Description
Covers the end-to-end post-delivery return lifecycle. The shopper requests a return for delivered garments within the eligible window, the merchant approves the request with reverse QC, pickup is executed, condition is validated, and refund settlement is completed.

#### 2. API Breakdown & Technical Actions
- **Forward Delivery Completion (Steps 1–11)**: Order confirmed and delivered.
- **`/update (update_reverse_qc)` (BAP -> BPP)**: Shopper submits return request specifying return reason codes (e.g., `001` - Size mismatch/defective), item quantities, and reverse QC details.
- **`/on_update (on_update_interim_reverseQc)` (BPP -> BAP)**: Seller acknowledges return in state `Return_Initiated`.
- **`on_update (on_update_return_approved)` [Unsolicited] (BPP -> BAP)**: Seller authorizes return and reverse pickup.
- **`on_update (on_update_return_picked)` [Unsolicited] (BPP -> BAP)**: Reverse logistics courier inspects garment tags and collects parcel.
- **`/update (update_reverse_qc_settlement)` (BAP -> BPP)**: BAP transmits refund bank/UPI settlement instructions.
- **`on_update (on_update_return_delivered)` [Unsolicited] (BPP -> BAP)**: Returned garments reach seller warehouse; merchant validates condition and executes refund.

---

### Flow 4: Cancel_Return_Request_Flow (Cancellation of Active Return Request)

#### 1. Short Description
Demonstrates the scenario where a shopper initiates a return request after delivery, but subsequently cancels the return before reverse courier collection, ensuring status synchronization and order state retention.

#### 2. API Breakdown & Technical Actions
- **Steps 1–11**: Order confirmed and delivered (`on_status_order_delivered`).
- **`/update (update_reverse_qc)` (BAP -> BPP)**: Shopper initiates return request.
- **`/on_update (on_update_interim_reverseQc)` & `on_update_return_approved`**: Seller acknowledges and approves return request.
- **`/cancel (cancel_return_request)` (BAP -> BPP)**: Shopper cancels return request prior to courier pickup.
- **`/on_cancel (on_cancel_return_request)` (BPP -> BAP)**: Seller confirms return request cancellation (`fulfillment.state = "Completed"`, return cancelled), leaving original order intact.

---

### Flow 5: Buyer_Instructions_And_Delivery_Update_Flow

#### 1. Short Description
Validates in-flight order modifications post-confirmation. The shopper updates delivery instructions and drop-off address before dispatch, followed by delivery authorization credentials and completion.

#### 2. API Breakdown & Technical Actions
- **Steps 1–7 (`/select` to `on_status_pending`)**: Standard order creation and acceptance.
- **`/update (update_buyer_instructions)` (BAP -> BPP)**: Shopper submits special delivery instructions (e.g., "leave with security desk").
- **`/on_update` (BPP -> BAP)**: Seller acknowledges instructions.
- **`/update (update_delivery_address)` (BAP -> BPP)**: Shopper submits updated drop-off address.
- **`/on_update` (BPP -> BAP)**: Seller confirms address modification.
- **Fulfillment Milestones (Steps 12–14)**: Garment packed, courier assigned, and parcel picked up.
- **`on_update (on_update_delivery_auth)` [Unsolicited] (BPP -> BAP)**: Seller generates delivery authorization credentials (e.g. OTP verification).
- **Steps 16–17**: Out for delivery and delivered to doorstep.

---

### Flow 6: Cash_On_Delivery_Flow (COD Payment & Fulfillment)

#### 1. Short Description
Executes a fashion purchase where the shopper chooses Cash on Delivery as the payment method, covering fulfillment tracking through to payment collection upon delivery.

#### 2. API Breakdown & Technical Actions
- **`/select` -> `/on_select`**: Variant selection and quote computation.
- **`/init (init_cod)` -> `/on_init (on_init_cod)`**: Order initialized with payment type configured as COD.
- **`/confirm (confirm_cod)` -> `/on_confirm (on_confirm_cod)`**: Order confirmed with payment status `NOT-PAID`.
- **Fulfillment Milestones (Steps 7–10)**: Order accepted, packed, picked up, and out for delivery.
- **`on_status (on_status_order_delivered_cod)` [Unsolicited] (BPP -> BAP)**: Courier collects cash/digital payment at doorstep and completes delivery (`payment.status = "PAID"`).

---

### Flow 7: Seller_Cred_Flow (Seller Credit Purchase)

#### 1. Short Description
Exercises an apparel order journey where the buyer places an order under pre-approved seller credit terms.

#### 2. API Breakdown & Technical Actions
- **`/select` -> `/on_select` -> `/init` -> `/on_init`**: Standard variant selection and initialization.
- **`/confirm (confirm_seller_cred)` (BAP -> BPP)**: Buyer confirms order binding seller credit payment terms.
- **`/on_confirm (on_confirm_seller_cred)` (BPP -> BAP)**: Seller validates credit terms and creates order record.

---

### Flow 8: Buyer_Cancellation_Flow (Buyer-Initiated Order Cancellation)

#### 1. Short Description
Validates buyer-initiated cancellation of a confirmed fashion order prior to courier dispatch.

#### 2. API Breakdown & Technical Actions
- **Steps 1–6 (`/select` to `/on_confirm`)**: Order confirmed.
- **`/cancel` (BAP -> BPP)**: Buyer triggers cancellation before dispatch, supplying cancellation reason code `001`.
- **`/on_cancel` (BPP -> BAP)**: Seller terminates fulfillment, marks `order.state = "Cancelled"`, and initiates refund.

---

### Flow 9: Seller_Cancellation_Flow (Part-Cancel & RTO Disposition)

#### 1. Short Description
Multi-exception flow covering merchant-initiated partial item cancellation during warehouse picking, followed by a failed delivery attempt culminating in Return to Origin and warehouse disposition.

#### 2. API Breakdown & Technical Actions
- **Steps 1–6**: Multi-item apparel order confirmed.
- **`on_update (on_update_part_cancel)` [Unsolicited] (BPP -> BAP)**: Seller identifies one item is out of stock in warehouse, cancels that line item, and adjusts quote.
- **`/update (update_partial_cancel_settlement)` (BAP -> BPP)**: BAP transmits settlement trail reflecting partial refund.
- **Steps 9–13**: Remaining items packed, courier assigned, picked up, and out for delivery.
- **`on_cancel (on_cancel_rto)` [Unsolicited] (BPP -> BAP)**: Delivery fails (customer unreachable); seller initiates RTO.
- **`/update (update_partial_cancel_settlement_1)` (BAP -> BPP)**: BAP updates settlement terms for RTO.
- **`on_status (on_status_rto_delivereddisposed)` [Unsolicited] (BPP -> BAP)**: Parcel returned to warehouse; order closed.

---

### Flow 10: Force_Cancellation_Flow (In-Flight Force Cancellation)

#### 1. Short Description
Handles forced system or seller cancellation post-confirmation after goods have progressed through intermediate fulfillment stages.

#### 2. API Breakdown & Technical Actions
- **Steps 1–6**: Order confirmed.
- **Steps 7–11**: Order accepted, packed, courier assigned, picked up, and marked out for delivery (`on_status_out_for_delivery_force`).
- **`/cancel (cancel_yes)` (BAP -> BPP)**: Forced cancellation initiated due to delivery impossibility.
- **`/on_cancel (on_cancel_yes)` (BPP -> BAP)**: Seller confirms forced cancellation (`order.state = "Cancelled"`).
- **`/update (update_settlement_cancel)` (BAP -> BPP)**: BAP transmits immediate refund settlement instructions.

---

### Flow 11: Out_Of_Stock_Flow (Cart Revision and Stockout Recovery)

#### 1. Short Description
Demonstrates cart recovery when a shopper encounters an out-of-stock garment variant during selection. The shopper revises the selection to an available item and completes fulfillment to delivery.

#### 2. API Breakdown & Technical Actions
- **`/select (select_out_of_stock)` (BAP -> BPP)**: Shopper selects depleted item.
- **`/on_select (on_select_out_of_stock)` (BPP -> BAP)**: Seller alerts stockout (`quantity.available.count = 0`).
- **`/select (select)` (BAP -> BPP)**: Shopper modifies cart to select available size/item.
- **`/on_select (on_select)` (BPP -> BAP)**: Seller confirms stock and returns quote.
- **Steps 5–14**: Order progresses through initialization, confirmation, packing, dispatch, and delivery completion.

---

### Flow 12: Out_Of_Stock_Flow(Error-code) (Immediate Error Rejection)

#### 1. Short Description
Validates immediate protocol rejection when a shopper selects an unavailable fashion SKU, returning standardized ONDC error codes (`40002` / `30009`).

#### 2. API Breakdown & Technical Actions
- **`/select (select_out_of_stock)` (BAP -> BPP)**: Shopper selects depleted garment.
- **`/on_select (on_select_out_of_stock)` (BPP -> BAP)**: Seller immediately rejects selection with error code `40002` or `30009`.

---

### Flow 13: Discovery_Flow_full_catalog (City-Wide Full Catalog Search)

#### 1. Short Description
Broad broadcast discovery enabling shoppers to explore full fashion catalogs, apparel categories, size/color variant options, and serviceability radiuses across a city.

#### 2. API Breakdown & Technical Actions
- **`/search (search)` (BAP -> Gateway)**: BAP broadcasts discovery query (`context.city = "std:080"`, `intent.category.id = "ONDC:RET12"`).
- **`/on_search (on_search)` (BPP -> BAP)**: Seller responds with complete catalog (apparel categories, variant attributes, images, MRP, and Legal Metrology details).

---

### Flow 14: Discovery_Flow_incremental_catalog (Incremental Catalog Push)

#### 1. Short Description
Validates merchant-initiated real-time catalog push. Sellers push live updates regarding price alterations, size replenishment, new style drops, or temporary store closures without requiring a full catalog reload.

#### 2. API Breakdown & Technical Actions
- **`/search (search_inc)` (BAP -> Gateway)**: Preliminary search.
- **`on_search (on_search_inc)` [Unsolicited] (BPP -> BAP)**: Seller pushes item-level delta changes.
- **`on_search (on_search_inc_disable)` [Unsolicited] (BPP -> BAP)**: Seller pushes catalog disablement / store closure.
- **`/search (search_inc)` (BAP -> Gateway)**: Verification query confirming state synchronization.

---

### Flow 15: Discovery_Flow_incremental_catalog_refresh_pull (Incremental Pull)

#### 1. Short Description
Validates the buyer application pull mechanism for catalog synchronization. The buyer requests catalog updates modified after a given timestamp (`last_updated_at`).

#### 2. API Breakdown & Technical Actions
- **`/search` -> `/on_search`**: Baseline discovery.
- **`/search (search_inc_pull)` (BAP -> BPP)**: Targeted point-to-point search passing `mode = "incremental_refresh"` and `last_updated_at`.
- **`/on_search (on_search_inc_pull)` (BPP -> BAP)**: Seller returns delta changes since cutoff.

---

### Flow 16: Delivery_Flow_With_IGM(v-1.0.0) (Grievance Resolution v1.0.0)

#### 1. Short Description
Complete forward fulfillment flow integrated with the standard IGM 1.0.0 complaint resolution cycle. After delivery, the shopper reports a garment defect, which the merchant investigates and resolves.

#### 2. API Breakdown & Technical Actions
- **Delivery Steps (1–12)**: Order confirmed and delivered (`on_status_order_delivered`).
- **`/issue (issue_open_100)` (BAP -> BPP)**: Shopper files complaint citing defective stitching or fabric damage.
- **`/on_issue (on_issue_processing_100)` (BPP -> BAP)**: Seller acknowledges complaint with ticket ID and resolution TAT.
- **`on_issue_status (on_issue_resolved_100)` [Unsolicited] (BPP -> BAP)**: Seller resolves issue (`RESOLVED`), authorizing refund.
- **`/issue (issue_close_100)` (BAP -> BPP)**: Shopper confirms resolution and closes ticket.

---

### Flow 17: Delivery_Flow_With_IGM(v-2.0.0) (Evidence Exchange & Return Action)

#### 1. Short Description
Validates interactive evidence-gathering under IGM 2.0.0. The seller requests photos of the garment defect and tags, the shopper uploads proof, the seller approves resolution, and an automated post-resolution return/refund is triggered.

#### 2. API Breakdown & Technical Actions
- **Delivery Steps (1–12)**: Order delivered.
- **`/issue (issue_open)` -> `/on_issue (processing)`**: Shopper reports damaged/defective garment.
- **`on_issue (on_issue_need_more_info)` [Unsolicited] (BPP -> BAP)**: Seller requests photos of the garment tag, defect, and packaging.
- **`/issue (issue_info_provided)` (BAP -> BPP)**: Shopper uploads requested media and description.
- **`/on_issue (on_issue_provided)` (BPP -> BAP)**: Seller confirms receipt of evidence.
- **`on_issue (on_issue_resolution)` [Unsolicited] (BPP -> BAP)**: Seller validates proof and proposes resolution.
- **`/issue (issue_resolution_accept)` (BAP -> BPP)**: Shopper accepts resolution.
- **`/on_issue (on_issue_resolved)` -> `/issue (issue_close)`**: Grievance closed as resolved.
- **`on_update (on_update_igm_return)` [Unsolicited] (BPP -> BAP)**: Seller triggers automated post-resolution return/refund workflow.

---

### Flow 18: Delivery_Flow_With_IGM_No_Action(v-2.0.0) (No-Action Resolution)

#### 1. Short Description
Validates IGM 2.0.0 where a grievance is processed, a formal explanation is tendered with `action_triggered = "NO_ACTION"`, accepted by the shopper, and finalized with an order audit update.

#### 2. API Breakdown & Technical Actions
- **Delivery Steps (1–12)**: Order delivered.
- **`/issue (issue_open_2)` -> `/on_issue (on_issue_processing)`**: Grievance registered and acknowledged.
- **`on_issue (on_issue_resolution_igm_3)` [Unsolicited] (BPP -> BAP)**: Seller tenders resolution proposal (`action_triggered = "NO_ACTION"` with explanatory justification).
- **`/issue (issue_resolution_accept_igm_3)` (BAP -> BPP)**: Shopper formally accepts explanation.
- **`/on_issue (on_issue_resolved_igm_3)` -> `/issue (issue_close_igm_3)`**: Grievance marked resolved and closed.
- **`on_status (on_status_igm_3)` (BPP -> BAP)**: Seller updates post-resolution order audit status.

---

### Flow 19: Delivery_Flow_With_IGM_Rejection(v-2.0.0) (Rejection, Escalation & Replacement)

#### 1. Short Description
A multi-tier grievance escalation flow under IGM 2.0.0. The shopper rejects initial resolution proposals, escalates the dispute to Level 2 (GRO / Arbitrator), reaches an accepted binding resolution, and receives a replacement garment parcel dispatched by the seller.

#### 2. API Breakdown & Technical Actions
- **Delivery Steps (1–12)**: Order delivered.
- **`/issue (issue_open)` -> `/on_issue (processing)`**: Initial grievance logged.
- **`on_issue (on_issue_resolution)` [Unsolicited] (BPP -> BAP)**: Seller proposes initial settlement.
- **`/issue (issue_resolution_reject)` (BAP -> BPP)**: Shopper rejects proposed resolution as unsatisfactory.
- **`/on_issue (processing_1)` -> `on_issue (resolution_1)`**: Seller tenders revised proposal.
- **`/issue (issue_escalate)` (BAP -> BPP)**: Shopper escalates grievance to Level 2 (Grievance Redressal Officer / Arbitrator).
- **`/on_issue (processing_2)` -> `on_issue (resolution_2)`**: Escalated authority issues binding resolution.
- **`/issue (issue_resolution_accept)` (BAP -> BPP)**: Shopper accepts escalated resolution.
- **`/on_issue (on_issue_resolved)` -> `/issue (issue_close)`**: Ticket closed as resolved.
- **`on_update (on_update_igm_replacement)` [Unsolicited] (BPP -> BAP)**: Seller automatically triggers replacement fulfillment parcel containing the replacement garment.

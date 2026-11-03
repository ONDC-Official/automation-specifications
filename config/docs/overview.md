# Beauty & Personal Care (ONDC:RET13 1.2.5)

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
- [Additional Scenarios & 1.2.5 Enhancements](#additional-scenarios--125-enhancements)
  - [1. Cross-Category Cart Shopping](#1-cross-category-cart-shopping)
  - [2. Post-Order Cosmetic Replacement Flow](#2-post-order-cosmetic-replacement-flow)
  - [3. Promotional Offers & Beauty Bundles Flow](#3-promotional-offers--beauty-bundles-flow)
  - [4. Cash on Delivery (COD) Payment Flow](#4-cash-on-delivery-cod-payment-flow)
  - [5. Seller Credit Checkout Flow](#5-seller-credit-checkout-flow)
  - [6. Statutory Compliance & Catalog Rejection (Drugs & Cosmetics Rules)](#6-statutory-compliance--catalog-rejection-drugs--cosmetics-rules)
  - [7. Buyer-Initiated Returns (Damaged, Leaked, or Expired Items)](#7-buyer-initiated-returns-damaged-leaked-or-expired-items)
  - [8. Buyer-Side Order Cancellation](#8-buyer-side-order-cancellation)
  - [9. Seller-Initiated Cancellation and RTO](#9-seller-initiated-cancellation-and-rto)
  - [10. Force Cancellation Flow](#10-force-cancellation-flow)
  - [11. Out of Stock Handling (Cart Recovery vs. Immediate Error Rejection)](#11-out-of-stock-handling-cart-recovery-vs-immediate-error-rejection)
  - [12. Incremental Catalog Refresh (Push and Pull)](#12-incremental-catalog-refresh-push-and-pull)
- [Issue and Grievance Management](#issue-and-grievance-management)
  - [1. IGM 1.0.0 Architecture](#1-igm-100-architecture)
  - [2. IGM 2.0.0 Architecture](#2-igm-200-architecture)
- [Detailed Protocol Flows](#detailed-protocol-flows)
  - [Flow 1: Delivery_Flow (Prepaid Standard Delivery)](#flow-1-delivery_flow-prepaid-standard-delivery)
  - [Flow 2: Cross_Category_Cart_Flow (Multi-Domain Cart Checkout)](#flow-2-cross_category_cart_flow-multi-domain-cart-checkout)
  - [Flow 3: Offers_Flow (Promotional Offers and Bundle Deals)](#flow-3-offers_flow-promotional-offers-and-bundle-deals)
  - [Flow 4: Replacement_Flow (Post-Order Cosmetic Replacement)](#flow-4-replacement_flow-post-order-cosmetic-replacement)
  - [Flow 5: Return_Flow (Buyer Return with Reverse Logistics)](#flow-5-return_flow-buyer-return-with-reverse-logistics)
  - [Flow 6: Cancel_Return_Request_Flow (Revocation of Return Request)](#flow-6-cancel_return_request_flow-revocation-of-return-request)
  - [Flow 7: Cash_On_Delivery_Flow (COD Payment & Delivery)](#flow-7-cash_on_delivery_flow-cod-payment--delivery)
  - [Flow 8: Seller_Cred_Flow (Seller Credit Purchase)](#flow-8-seller_cred_flow-seller-credit-purchase)
  - [Flow 9: Catalog_Rejection_Flow (Statutory Compliance Discrepancy)](#flow-9-catalog_rejection_flow-statutory-compliance-discrepancy)
  - [Flow 10: Buyer_Cancellation_Flow (Buyer-Initiated Order Cancellation)](#flow-10-buyer_cancellation_flow-buyer-initiated-order-cancellation)
  - [Flow 11: Seller_Cancellation_Flow (Part-Cancel & RTO Disposition)](#flow-11-seller_cancellation_flow-part-cancel--rto-disposition)
  - [Flow 12: Force_Cancellation_Flow (In-Flight Force Cancellation)](#flow-12-force_cancellation_flow-in-flight-force-cancellation)
  - [Flow 13: Out_Of_Stock_Flow (Cart Revision and Stockout Recovery)](#flow-13-out_of_stock_flow-cart-revision-and-stockout-recovery)
  - [Flow 14: Out_Of_Stock_Flow(Error-code) (Immediate Error Rejection)](#flow-14-out_of_stock_flowerror-code-immediate-error-rejection)
  - [Flow 15: Discovery_Flow_full_catalog (City-Wide Full Catalog Search)](#flow-15-discovery_flow_full_catalog-city-wide-full-catalog-search)
  - [Flow 16: Discovery_Flow_incremental_catalog (Incremental Catalog Push)](#flow-16-discovery_flow_incremental_catalog-incremental-catalog-push)
  - [Flow 17: Discovery_Flow_incremental_catalog_refresh_pull (Incremental Pull)](#flow-17-discovery_flow_incremental_catalog_refresh_pull-incremental-pull)
  - [Flow 18: Delivery_Flow_With_IGM(v-1.0.0) (Grievance Resolution v1.0.0)](#flow-18-delivery_flow_with_igmv-100-grievance-resolution-v100)
  - [Flow 19: Delivery_Flow_With_IGM(v-2.0.0) (Evidence Exchange & Return Action)](#flow-19-delivery_flow_with_igmv-200-evidence-exchange--return-action)
  - [Flow 20: Delivery_Flow_With_IGM_No_Action(v-2.0.0) (No-Action Resolution)](#flow-20-delivery_flow_with_igm_no_actionv-200-no-action-resolution)
  - [Flow 21: Delivery_Flow_With_IGM_Rejection(v-2.0.0) (Rejection, Escalation & Replacement)](#flow-21-delivery_flow_with_igm_rejectionv-200-rejection-escalation--replacement)

---

## Overview

The Beauty & Personal Care domain (**ONDC:RET13**, specification version **1.2.5**) establishes an open, interoperable digital commerce standard for cosmetics, skincare, haircare, fragrances, bath & body, personal grooming, baby care, and hygiene products across the Open Network for Digital Commerce (ONDC). BPC retail transactions are characterized by SKU shade and volume variants (foundations, lipsticks, serums in ml/g), protective packaging requirements for fragile and liquid flacons, strict regulatory mandates (Drugs & Cosmetics Act 1940, Cosmetics Rules 2020, and Legal Metrology Packaged Commodities Rules), and hygiene-governed post-purchase lifecycles.

ONDC democratizes beauty commerce by connecting local cosmetic stores, independent pharmacies, salons, and direct-to-consumer (D2C) brands with consumers across India. Rather than having to build proprietary applications or accept hefty commission deductions from closed e-commerce marketplaces (such as Nykaa, Amazon, or Purplle), independent beauty stores can list their inventory on ONDC-enabled seller applications (BPPs) and reach buyers seamlessly through any buyer application (BAP).

Building upon version 1.2.0, **version 1.2.5** introduces essential retail capabilities specifically tailored to beauty retail dynamics:
- **Cross-Category Cart Shopping (`Cross_Category_Cart_Flow`)**: Enabling shoppers to combine beauty products with items from other retail domains (e.g., Grocery, Fashion, Electronics) in a single consolidated checkout.
- **Dedicated Cosmetic Replacement Flow (`Replacement_Flow`)**: A full 21-step lifecycle for swapping damaged containers, leaked flacons, or defective pumps with replacement items.
- **Promotional Offers & Bundles (`Offers_Flow`)**: Discovery and checkout incorporating coupon codes, promotional discounts, and cosmetic gift sets.
- **Cash on Delivery (`Cash_On_Delivery_Flow`)**: Standardized COD payment method support across beauty ordering journeys.
- **Catalog Rejection Safeguards (`Catalog_Rejection_Flow`)**: Formal protocol-level rejection when published cosmetic listings fail statutory compliance (e.g. missing manufacturing licenses or absent ingredient declarations).
- **Seller Credit Purchases (`Seller_Cred_Flow`)**: Supporting retail purchases under pre-approved seller credit terms.
- **Comprehensive Cancellation & Stockout Handlers**: Dedicated flows for seller-initiated cancellations, forced transit cancellations, cart reconfiguration recovery, and immediate out-of-stock error codes.
- **Complete Grievance Framework**: Full coverage across **IGM 1.0.0** and all **IGM 2.0.0** branches.

---

## Participants

| Participant | What This Means |
|---|---|
| **Buyer Application (BAP)** | The consumer-facing platform (e.g. beauty shopping apps, super-apps, banking/UPI platforms) where consumers search BPC catalogs, filter by brand, skin/hair type, ingredient preferences, and cosmetic shades, configure delivery addresses, select payment methods (prepaid or COD), track delivery couriers, and raise post-delivery grievances. |
| **Seller Application (BPP)** | An application representing beauty retailers, pharmacies, cosmetics distributors, salons, or D2C skincare brands. The BPP publishes item catalogs with variant attributes (volume, shade, active ingredients, expiry dates), checks delivery serviceability, calculates itemized quotes, coordinates warehouse picking and protective bubble-wrapping, and processes returns or replacements. |
| **Logistics Service Provider (LSP)** | A delivery network participant that executes hyperlocal same-day delivery or intercity surface/air shipping. In seller-managed delivery, the BPP or its integrated delivery partner allocates couriers, provides live GPS tracking, and conducts reverse logistics return pickups. |
| **Gateway** | The ONDC routing infrastructure that multicasts broadcast discovery requests (`/search`) from BAPs to active seller applications (BPPs) based on domain code (`ONDC:RET13`), city code (e.g. `std:080`), and geolocation parameters. |

---

## The User Journey

The standard BPC forward ordering journey (`Delivery_Flow`) enables a shopper to discover beauty and personal care items, select specific shades or volume variants, review transparent price breakdowns and turnaround times, provide delivery coordinates, complete payment, and receive carefully packaged goods with end-to-end shipment tracking.

### 1. Discovery and Catalog Search

The shopper initiates discovery on the BAP by searching for BPC categories, brands, or product types (e.g., "Niacinamide Serum", "Matte Lipstick", "Sunscreen SPF 50", "Keratin Shampoo"):

- **Intent Broadcast**: The BAP transmits a `/search` request specifying domain category (`ONDC:RET13`), buyer delivery GPS coordinates and area pin code, and fulfillment type (`Delivery`).
- **Catalog Delivery**: Active BPC BPPs within serviceable delivery range respond via asynchronous `/on_search` payloads containing their store catalog (`bpp/providers[]`). This includes product categories, brand details, shade options, volume/weight (ml/g), ingredient lists, MRP, selling price, expiry/best-before dates, and statutory regulatory declarations.

### 2. Shade/Variant Selection and Serviceability Check

The shopper selects specific items with desired volume sizes or cosmetic shades and adds them to their cart:

- **Network interaction:**
  - **`/select` (BAP -> BPP)**: The BAP transmits selected item IDs, variant SKUs (e.g. 30ml dropper bottle, Shade #06 Ruby Red), quantities, store location ID, and delivery destination coordinates (`fulfillments[0].end.location.gps` and `address.area_code`).
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

## Additional Scenarios & 1.2.5 Enhancements

Version 1.2.5 formalizes comprehensive operational variations to support modern beauty commerce dynamics.

### 1. Cross-Category Cart Shopping

Consumers frequently purchase beauty products alongside other retail categories (e.g. buying face cream alongside fashion apparel or grocery items):
- **Unified Cart (`Cross_Category_Cart_Flow`)**: The BAP constructs a consolidated cart with items across different categories (`select_ccc`). The BPP computes category-specific taxes, packaging fees, and fulfillment terms in `on_select_ccc`, progressing through initialization (`init_ccc`) and confirmation (`confirm_ccc`) to multi-item fulfillment.

### 2. Post-Order Cosmetic Replacement Flow

When a cosmetic item arrives with a shattered glass dropper, defective pump dispenser, or transit leakage, a replacement is often preferred over a refund:
- **Replacement Request (`update_reverse_qc_rep`)**: Shopper initiates a replacement request within the return window, specifying reverse QC parameters and damage reason codes.
- **Reverse Pickup & Warehouse QC (`on_update_return_approved` $\rightarrow$ `on_update_return_delivered_rep`)**: Reverse courier collects the damaged item and returns it to the seller facility for QC verification.
- **Replacement Dispatch & Handover (`on_status_packed_rep` $\rightarrow$ `on_status_order_delivered_rep`)**: The merchant packs a replacement product from a fresh batch, dispatches it via courier, and completes doorstep handover.

### 3. Promotional Offers & Beauty Bundles Flow

Beauty commerce relies heavily on seasonal discounts, gift-with-purchase, and bundled kits:
- **Offer Validation (`Offers_Flow`)**: During `/select` (`select_offers`), the buyer applies an eligible promotional offer. The seller returns `quote.breakup[]` in `on_select_offers` reflecting the discount deductions and promo tags, proceeding smoothly through checkout.

### 4. Cash on Delivery (COD) Payment Flow

To accommodate consumers who prefer cash or UPI upon physical receipt:
- The payment method is set to Cash on Delivery during checkout (`init_cod` and `confirm_cod`).
- Fulfillment proceeds through packing, courier pickup, and transit.
- Upon doorstep handover, the courier collects payment and triggers `on_status_order_delivered_cod` (`payment.status = "PAID"`).

### 5. Seller Credit Checkout Flow

Supports B2B retail or consumer credit purchasing:
- Checkout is executed under pre-approved seller credit terms (`confirm_seller_cred` and `on_confirm_seller_cred`), establishing payment liabilities without upfront digital debit.

### 6. Statutory Compliance & Catalog Rejection (Drugs & Cosmetics Rules)

Cosmetics are strictly regulated under the Drugs and Cosmetics Act (1940) and Cosmetics Rules (2020):
- **Catalog Rejection (`Catalog_Rejection_Flow`)**: When a seller's published `/on_search` catalog omits mandatory statutory declarations (such as manufacturing license number, batch/lot number, expiry date, or complete INCI ingredients list), the buyer app compliance engine triggers `catalog_rejection` to prevent non-compliant listings from appearing to consumers.

### 7. Buyer-Initiated Returns (Damaged, Leaked, or Expired Items)

Due to hygiene regulations, opened cosmetics are non-returnable. However, returns and refunds are fully supported for legitimate defects (broken glass, leaked creams, expired batches, tampered seals):
- Shopper initiates return request via `/update (update_return)`.
- Seller acknowledges (`on_update_return_init`) and approves (`on_update_return_approved`).
- Reverse logistics courier collects parcel (`on_update_return_picked`).
- Refund settlement instructions are sent via `update_settlement_trail`, and the seller executes refund upon warehouse receipt (`on_update_return_delivered`).

### 8. Buyer-Side Order Cancellation

Shopper cancels an order prior to merchant dispatch:
- `/cancel` submitted with cancellation reason code `001`.
- Seller acknowledges via `/on_cancel`, transitions order state to `Cancelled`, and triggers refund.

### 9. Seller-Initiated Cancellation and RTO

- **Partial Cancellation**: Merchant identifies that a specific cosmetic shade or batch is unavailable during warehouse picking (`on_update_part_cancel`), prompting a partial refund settlement (`update_partial_cancel_settlement`).
- **Return to Origin (RTO)**: Courier attempts delivery but customer is unreachable; seller initiates RTO (`on_cancel_rto`), parcel is returned to warehouse (`on_status_rto_delivereddisposed`), and reverse shipping deductions are settled.

### 10. Force Cancellation Flow

Handles forced system or seller cancellation post-confirmation due to critical logistical failures:
- `/cancel (cancel_yes)` issued after fulfillment progression.
- Seller confirms via `/on_cancel (on_cancel_yes)` and BAP issues refund settlement (`update_settlement_cancel`).

### 11. Out of Stock Handling (Cart Recovery vs. Immediate Error Rejection)

- **Cart Recovery (`Out_Of_Stock_Flow`)**: Shopper encounters an out-of-stock response during selection (`on_select_out_of_stock`), updates selection to an available shade/item (`select`), and proceeds through confirmation to delivery.
- **Immediate Error Rejection (`Out_Of_Stock_Flow(Error-code)`)**: Selection is immediately rejected with error code `40002` (Out of stock) or `30009`.

### 12. Incremental Catalog Refresh (Push and Pull)

- **Push (`Discovery_Flow_incremental_catalog`)**: Seller broadcasts live price alterations, shade replenishment, new launches, or temporary store closures (`on_search_inc_disable`).
- **Pull (`Discovery_Flow_incremental_catalog_refresh_pull`)**: Buyer queries delta updates using timestamp cutoff (`last_updated_at`).

---

## Issue and Grievance Management

The BPC domain provides robust complaint handling across both ONDC Issue and Grievance Management (IGM) framework versions.

### 1. IGM 1.0.0 Architecture

1. **`issue (open)` (BAP -> BPP)**: Shopper files a grievance citing cosmetic damage, leakage, or expired items.
2. **`on_issue (processing)` (BPP -> BAP)**: Seller acknowledges receipt with ticket ID and resolution TAT.
3. **`on_issue_status (resolved)` (BPP -> BAP)**: Seller investigates and publishes resolution (`REFUND`, `REPLACEMENT`, or `NO_ACTION`).
4. **`issue (close)` (BAP -> BPP)**: Shopper confirms resolution and closes the issue.

### 2. IGM 2.0.0 Architecture

- **Evidence Exchange & Return (`Delivery_Flow_With_IGM(v-2.0.0)`)**: Seller requests photo proof of leaked bottle or batch code (`on_issue_need_more_info`), shopper uploads images (`issue_info_provided`), seller proposes resolution, accepted by shopper, triggering return workflow (`on_update_igm_return`).
- **No-Action Resolution (`Delivery_Flow_With_IGM_No_Action(v-2.0.0)`)**: Seller provides an explanatory resolution with `action_triggered = "NO_ACTION"`, accepted by shopper, followed by post-resolution order audit status (`on_status_igm_3`).
- **Rejection, Escalation & Replacement (`Delivery_Flow_With_IGM_Rejection(v-2.0.0)`)**: Shopper rejects initial resolution, escalates to Level 2 (GRO / Arbitrator), escalated authority issues binding resolution, accepted by shopper, triggering replacement cosmetic parcel dispatch (`on_update_igm_replacement`).

---

## Detailed Protocol Flows

### Flow 1: Delivery_Flow (Prepaid Standard Delivery)

#### 1. Short Description
The primary forward-fulfillment BPC purchase journey. A shopper selects cosmetics or personal care items, receives an itemized quote with delivery fees and taxes, provides shipping addresses, pays upfront, and receives the goods through seller-managed delivery with live courier tracking and delivery verification.

#### 2. API Breakdown & Technical Actions
- **`/select` (BAP -> BPP)**: The BAP transmits selected cosmetic item IDs, shade/volume variant codes, quantities, store location ID, and delivery coordinates.
- **`/on_select` (BPP -> BAP)**: Seller validates inventory and delivery radius, returning itemized quote (`quote.breakup[]`) with base product prices, delivery charges, packaging fees, CGST/SGST taxes, and estimated turnaround time (`@ondc/org/TAT`).
- **`/init` (BAP -> BPP)**: Shopper inputs shipping address (building, street, city, pin code) and contact details.
- **`/on_init` (BPP -> BAP)**: Seller freezes order quote, specifies cancellation terms, publishes return window (`@ondc/org/return_window = "P7D"`), and returns payment terms.
- **`/confirm` (BAP -> BPP)**: BAP collects digital payment and sends confirmed order payload (`payment.status = "PAID"`).
- **`/on_confirm` (BPP -> BAP)**: Seller confirms order placement, assigning `order.id` with state `Created` and fulfillment state `Pending`.
- **`on_status (on_status_pending)` [Unsolicited] (BPP -> BAP)**: Merchant marks order accepted (`order.state = "Accepted"`).
- **`on_status (on_status_packed)` [Unsolicited] (BPP -> BAP)**: Items inspected for seal integrity, cushioned in bubble wrap, and packed into parcel (`fulfillment.state = "Packed"`, `order.state = "In-progress"`).
- **`on_status (on_status_agent_assigned)` [Unsolicited] (BPP -> BAP)**: Courier assigned with agent name and phone.
- **`on_status (on_status_picked)` [Unsolicited] (BPP -> BAP)**: Courier collects package from warehouse (`fulfillment.state = "Order-picked-up"`).
- **`/track` & `/on_track` (BAP $\leftrightarrow$ BPP)**: BAP polls for live shipment tracking URL / GPS coordinates.
- **`on_status (on_status_out_for_delivery)` [Unsolicited] (BPP -> BAP)**: Courier is out for doorstep delivery (`fulfillment.state = "Out-for-delivery"`).
- **`on_status (on_status_order_delivered)` [Unsolicited] (BPP -> BAP)**: Package successfully delivered with electronic proof of delivery (`fulfillment.state = "Order-delivered"`, `order.state = "Completed"`).

---

### Flow 2: Cross_Category_Cart_Flow (Multi-Domain Cart Checkout)

#### 1. Short Description
Demonstrates a multi-category retail checkout where a consumer combines beauty and personal care products with items from other retail categories in a single unified cart, validating quote consolidation and fulfillment tracking.

#### 2. API Breakdown & Technical Actions
- **`/select (select_ccc)` (BAP -> BPP)**: Buyer selects items from multiple retail categories in a consolidated cart.
- **`/on_select (on_select_ccc)` (BPP -> BAP)**: Seller validates serviceability and returns consolidated itemized quote.
- **`/init (init_ccc)` -> `/on_init (on_init_ccc)`**: Unified order initialized with shipping details and settlement terms.
- **`/confirm (confirm_ccc)` -> `/on_confirm (on_confirm_ccc)`**: Order confirmed across categories (`order.state = "Created"`).
- **Fulfillment Progression (Steps 7–12)**: Order accepted (`on_status_accepted_ccc`), packed (`on_status_packed_ccc`), courier assigned (`on_status_agent_assigned_ccc`), picked up (`on_status_picked_ccc`), transported (`on_status_out_for_delivery_ccc`), and delivered (`on_status_order_delivered_ccc`).

---

### Flow 3: Offers_Flow (Promotional Offers and Bundle Deals)

#### 1. Short Description
Demonstrates discovery, validation, and checkout with promotional discounts, coupon codes, and bundle offers applied to cosmetics and skincare items.

#### 2. API Breakdown & Technical Actions
- **`/select (select_offers)` (BAP -> BPP)**: Shopper selects cosmetics and applies an eligible promotional offer.
- **`/on_select (on_select_offers)` (BPP -> BAP)**: Seller validates offer terms and returns quote with discounted totals.
- **`/init (init_offers)` -> `/on_init` -> `/confirm` -> `/on_confirm`**: Order confirmed with offer-adjusted pricing.
- **Fulfillment Milestones (Steps 7–12)**: Order accepted, packed, courier assigned, picked up, transported, and delivered.

---

### Flow 4: Replacement_Flow (Post-Order Cosmetic Replacement)

#### 1. Short Description
A complete 21-step post-order replacement journey for cosmetics. A shopper requests an exchange for a damaged, leaked, or incorrect cosmetic product, the seller approves the request, reverse logistics collects the damaged item, and the seller dispatches and delivers the replacement item.

#### 2. API Breakdown & Technical Actions
- **Forward Fulfillment (Steps 1–12)**: Order confirmed and delivered (`on_status_order_delivered`).
- **`/update (update_reverse_qc_rep)` (BAP -> BPP)**: Shopper initiates a replacement request, supplying damage reason codes (e.g. broken pump/leaked container) and reverse QC details.
- **`/on_update (on_update_interim_reverseQc)` (BPP -> BAP)**: Seller records replacement request in state `Order-delivered` / processing.
- **`on_update (on_update_return_approved)` [Unsolicited] (BPP -> BAP)**: Seller authorizes replacement and reverse pickup.
- **`on_update (on_update_return_picked_rep)` [Unsolicited] (BPP -> BAP)**: Reverse logistics courier collects damaged item from consumer.
- **`on_update (on_update_return_delivered_rep)` [Unsolicited] (BPP -> BAP)**: Damaged item arrives at seller warehouse and passes QC verification.
- **`on_status (on_status_packed_rep)` [Unsolicited] (BPP -> BAP)**: Seller packs replacement cosmetic parcel from fresh inventory.
- **`on_status (on_status_picked_rep)` [Unsolicited] (BPP -> BAP)**: Courier collects replacement parcel from warehouse.
- **`on_status (on_status_out_for_delivery_rep)` [Unsolicited] (BPP -> BAP)**: Replacement parcel out for delivery.
- **`on_status (on_status_order_delivered_rep)` [Unsolicited] (BPP -> BAP)**: Replacement cosmetic successfully delivered to consumer.

---

### Flow 5: Return_Flow (Buyer Return with Reverse Logistics)

#### 1. Short Description
Covers the post-delivery return lifecycle. The shopper requests a return for delivered items (broken glass, leaked liquid, or expired batch), the merchant approves the request, reverse pickup is executed, condition is validated, and refund settlement is processed.

#### 2. API Breakdown & Technical Actions
- **Forward Fulfillment (Steps 1–12)**: Order confirmed and delivered.
- **`/update (update_return)` (BAP -> BPP)**: Shopper submits return request specifying return reason codes (e.g. damaged/leaked), item quantities, and defect photos.
- **`/on_update (on_update_return_init)` (BPP -> BAP)**: Seller acknowledges return in state `Order-delivered`.
- **`on_update (on_update_return_approved)` [Unsolicited] (BPP -> BAP)**: Seller authorizes return and reverse pickup.
- **`on_update (on_update_return_picked)` [Unsolicited] (BPP -> BAP)**: Reverse logistics courier inspects packaging and collects parcel.
- **`/update (update_settlement_trail)` (BAP -> BPP)**: BAP transmits refund bank/UPI settlement instructions.
- **`on_update (on_update_return_delivered)` [Unsolicited] (BPP -> BAP)**: Returned items reach seller warehouse; merchant validates condition and executes refund.

---

### Flow 6: Cancel_Return_Request_Flow (Revocation of Return Request)

#### 1. Short Description
Demonstrates the scenario where a shopper initiates a return request after delivery, but subsequently revokes the return before reverse courier collection, maintaining order completion.

#### 2. API Breakdown & Technical Actions
- **Forward Delivery & Return Initiation**: Order delivered, shopper submits return request, seller approves return.
- **`/cancel (cancel_return_request)` (BAP -> BPP)**: Shopper cancels return request prior to courier pickup.
- **`/on_cancel (on_cancel_return_request)` (BPP -> BAP)**: Seller confirms return request cancellation, closing the return while preserving original order completion.

---

### Flow 7: Cash_On_Delivery_Flow (COD Payment & Delivery)

#### 1. Short Description
Executes a BPC purchase where the shopper chooses Cash on Delivery as the payment method, covering fulfillment tracking through to payment collection upon delivery.

#### 2. API Breakdown & Technical Actions
- **`/select` -> `/on_select`**: Item selection and quote computation.
- **`/init (init_cod)` -> `/on_init (on_init_cod)`**: Order initialized with payment type configured as COD.
- **`/confirm (confirm_cod)` -> `/on_confirm (on_confirm_cod)`**: Order confirmed with payment status `NOT-PAID`.
- **Fulfillment Milestones (Steps 7–10)**: Order accepted, packed, picked up, and out for delivery.
- **`on_status (on_status_order_delivered_cod)` [Unsolicited] (BPP -> BAP)**: Courier collects cash/digital payment at doorstep and completes delivery (`payment.status = "PAID"`).

---

### Flow 8: Seller_Cred_Flow (Seller Credit Purchase)

#### 1. Short Description
Exercises a beauty retail purchase journey where the buyer places an order under pre-approved seller credit terms.

#### 2. API Breakdown & Technical Actions
- **`/select` -> `/on_select` -> `/init` -> `/on_init`**: Standard item selection and initialization.
- **`/confirm (confirm_seller_cred)` (BAP -> BPP)**: Buyer confirms order binding seller credit payment terms.
- **`/on_confirm (on_confirm_seller_cred)` (BPP -> BAP)**: Seller validates credit terms and creates order record.

---

### Flow 9: Catalog_Rejection_Flow (Statutory Compliance Discrepancy)

#### 1. Short Description
Validates regulatory safeguards in the BPC domain under the Drugs and Cosmetics Act and Legal Metrology Rules. When a seller's published catalog omits mandatory statutory declarations, the buyer app automatically rejects the catalog.

#### 2. API Breakdown & Technical Actions
- **`/search (search)` (BAP -> Gateway)**: BAP transmits discovery request.
- **`/on_search (on_search)` (BPP -> BAP)**: Seller returns catalog containing items that violate mandatory statutory rules (e.g., missing manufacturing license, absent expiry date, or missing ingredients list).
- **`catalog_rejection` (BAP -> System / Log)**: BAP compliance validator detects non-conforming items, flags statutory violations, and rejects the provider's catalog from consumer listings.

---

### Flow 10: Buyer_Cancellation_Flow (Buyer-Initiated Order Cancellation)

#### 1. Short Description
Validates buyer-initiated cancellation of a confirmed BPC order prior to courier dispatch.

#### 2. API Breakdown & Technical Actions
- **Steps 1–6 (`/select` to `/on_confirm`)**: Order confirmed.
- **`/cancel` (BAP -> BPP)**: Buyer triggers cancellation before dispatch, supplying cancellation reason code `001`.
- **`/on_cancel` (BPP -> BAP)**: Seller terminates fulfillment, marks `order.state = "Cancelled"`, and initiates refund.

---

### Flow 11: Seller_Cancellation_Flow (Part-Cancel & RTO Disposition)

#### 1. Short Description
Multi-exception flow covering merchant-initiated partial item cancellation during warehouse picking, followed by a failed delivery attempt culminating in Return to Origin and warehouse disposition.

#### 2. API Breakdown & Technical Actions
- **Steps 1–6**: Multi-item BPC order confirmed.
- **`on_update (on_update_part_cancel)` [Unsolicited] (BPP -> BAP)**: Seller identifies one item is out of stock in warehouse, cancels that line item, and adjusts quote.
- **`/update (update_partial_cancel_settlement)` (BAP -> BPP)**: BAP transmits settlement trail reflecting partial refund.
- **Steps 9–13**: Remaining items packed, courier assigned, picked up, and out for delivery.
- **`on_cancel (on_cancel_rto)` [Unsolicited] (BPP -> BAP)**: Delivery fails (customer unreachable); seller initiates RTO.
- **`on_status (on_status_rto_delivereddisposed)` [Unsolicited] (BPP -> BAP)**: Parcel returned to warehouse; order closed.

---

### Flow 12: Force_Cancellation_Flow (In-Flight Force Cancellation)

#### 1. Short Description
Handles forced system or seller cancellation post-confirmation after goods have progressed through intermediate fulfillment stages.

#### 2. API Breakdown & Technical Actions
- **Steps 1–6**: Order confirmed.
- **Steps 7–11**: Order accepted, packed, courier assigned, picked up, and marked out for delivery (`on_status_out_for_delivery_force`).
- **`/cancel (cancel_yes)` (BAP -> BPP)**: Forced cancellation initiated due to delivery impossibility.
- **`/on_cancel (on_cancel_yes)` (BPP -> BAP)**: Seller confirms forced cancellation (`order.state = "Cancelled"`).
- **`/update (update_settlement_cancel)` (BAP -> BPP)**: BAP transmits immediate refund settlement instructions.

---

### Flow 13: Out_Of_Stock_Flow (Cart Revision and Stockout Recovery)

#### 1. Short Description
Demonstrates cart recovery when a shopper encounters an out-of-stock cosmetic shade or volume during selection. The shopper revises the selection to an available item and completes fulfillment to delivery.

#### 2. API Breakdown & Technical Actions
- **`/select (select_out_of_stock)` (BAP -> BPP)**: Shopper selects depleted item.
- **`/on_select (on_select_out_of_stock)` (BPP -> BAP)**: Seller alerts stockout (`quantity.available.count = 0`).
- **`/select (select)` (BAP -> BPP)**: Shopper modifies cart to select available shade/item.
- **`/on_select (on_select)` (BPP -> BAP)**: Seller confirms stock and returns quote.
- **Steps 5–14**: Order progresses through initialization, confirmation, packing, dispatch, and delivery completion.
- **`/track` & `/on_track` (BAP $\leftrightarrow$ BPP)**: Shipment telemetry monitored.

---

### Flow 14: Out_Of_Stock_Flow(Error-code) (Immediate Error Rejection)

#### 1. Short Description
Validates immediate protocol rejection when a shopper selects an unavailable BPC SKU, returning standardized ONDC error codes (`40002` / `30009`).

#### 2. API Breakdown & Technical Actions
- **`/select (select_out_of_stock)` (BAP -> BPP)**: Shopper selects depleted item.
- **`/on_select (on_select_out_of_stock)` (BPP -> BAP)**: Seller immediately rejects selection with error code `40002` or `30009`.

---

### Flow 15: Discovery_Flow_full_catalog (City-Wide Full Catalog Search)

#### 1. Short Description
Broad broadcast discovery enabling shoppers to explore full BPC catalogs, product categories, shade/volume variant options, and serviceability radiuses across a city.

#### 2. API Breakdown & Technical Actions
- **`/search (search)` (BAP -> Gateway)**: BAP broadcasts discovery query (`context.city = "std:080"`, `intent.category.id = "ONDC:RET13"`).
- **`/on_search (on_search)` (BPP -> BAP)**: Seller responds with complete catalog (product categories, variant attributes, images, MRP, and Drugs & Cosmetics statutory details).

---

### Flow 16: Discovery_Flow_incremental_catalog (Incremental Catalog Push)

#### 1. Short Description
Validates merchant-initiated real-time catalog push. Sellers push live updates regarding price alterations, shade replenishment, new beauty drops, or temporary store closures without requiring a full catalog reload.

#### 2. API Breakdown & Technical Actions
- **`/search (search_inc)` (BAP -> Gateway)**: Preliminary search.
- **`on_search (on_search_inc)` [Unsolicited] (BPP -> BAP)**: Seller pushes item-level delta changes.
- **`on_search (on_search_inc_disable)` [Unsolicited] (BPP -> BAP)**: Seller pushes catalog disablement / store closure.
- **`/search (search_inc1)` (BAP -> Gateway)**: Verification query confirming state synchronization.

---

### Flow 17: Discovery_Flow_incremental_catalog_refresh_pull (Incremental Pull)

#### 1. Short Description
Validates the buyer application pull mechanism for catalog synchronization. The buyer requests catalog updates modified after a given timestamp (`last_updated_at`).

#### 2. API Breakdown & Technical Actions
- **`/search` -> `/on_search`**: Baseline discovery.
- **`/search (search_inc_pull)` (BAP -> BPP)**: Targeted point-to-point search passing `tags` with `mode = "incremental_refresh"` and `last_updated_at`.
- **`/on_search (on_search_inc_pull)` (BPP -> BAP)**: Seller returns delta changes since cutoff.

---

### Flow 18: Delivery_Flow_With_IGM(v-1.0.0) (Grievance Resolution v1.0.0)

#### 1. Short Description
Complete forward fulfillment flow integrated with the standard IGM 1.0.0 complaint resolution cycle. After delivery, the shopper reports a product defect, which the merchant investigates and resolves.

#### 2. API Breakdown & Technical Actions
- **Delivery Steps (1–12)**: Order confirmed and delivered (`on_status_order_delivered`).
- **`/issue (issue_open_100)` (BAP -> BPP)**: Shopper files complaint citing leaked or damaged cosmetic items.
- **`/on_issue (on_issue_processing_100)` (BPP -> BAP)**: Seller acknowledges complaint with ticket ID and resolution TAT.
- **`on_issue_status (on_issue_resolved_100)` [Unsolicited] (BPP -> BAP)**: Seller resolves issue (`RESOLVED`), authorizing refund.
- **`/issue (issue_close_100)` (BAP -> BPP)**: Shopper confirms resolution and closes ticket.

---

### Flow 19: Delivery_Flow_With_IGM(v-2.0.0) (Evidence Exchange & Return Action)

#### 1. Short Description
Validates interactive evidence-gathering under IGM 2.0.0. The seller requests photos of the damaged container and batch code, the shopper uploads proof, the seller approves resolution, and an automated post-resolution return/refund is triggered.

#### 2. API Breakdown & Technical Actions
- **Delivery Steps (1–12)**: Order delivered.
- **`/issue (issue_open)` -> `/on_issue (processing)`**: Shopper reports damaged/defective cosmetic item.
- **`on_issue (on_issue_need_more_info)` [Unsolicited] (BPP -> BAP)**: Seller requests photos of the damaged container, batch code, and packaging.
- **`/issue (issue_info_provided)` (BAP -> BPP)**: Shopper uploads requested media and description.
- **`/on_issue (on_issue_provided)` (BPP -> BAP)**: Seller confirms receipt of evidence.
- **`on_issue (on_issue_resolution)` [Unsolicited] (BPP -> BAP)**: Seller validates proof and proposes resolution.
- **`/issue (issue_resolution_accept)` (BAP -> BPP)**: Shopper accepts resolution.
- **`/on_issue (on_issue_resolved)` -> `/issue (issue_close)`**: Grievance closed as resolved.
- **`on_update (on_update_igm_return)` [Unsolicited] (BPP -> BAP)**: Seller triggers automated post-resolution return/refund workflow.

---

### Flow 20: Delivery_Flow_With_IGM_No_Action(v-2.0.0) (No-Action Resolution)

#### 1. Short Description
Validates IGM 2.0.0 where a grievance is processed, a formal explanation is tendered with `action_triggered = "NO_ACTION"`, accepted by the shopper, and finalized with an order audit update.

#### 2. API Breakdown & Technical Actions
- **Delivery Steps (1–12)**: Order delivered.
- **`/issue (issue_open_2)` -> `/on_issue (on_issue_processing)`**: Grievance registered and acknowledged.
- **`on_issue (on_issue_resolution_igm_3)` [Unsolicited] (BPP -> BAP)**: Seller tenders resolution proposal (`action_triggered = "NO_ACTION"` with explanatory justification).
- **`/issue (issue_resolution_accept_igm_3)` (BAP -> BPP)**: Shopper formally accepts explanation.
- **`/on_issue (on_issue_resolved_igm_3)` -> `/issue (issue_close_igm_3)`**: Grievance marked resolved and closed.
- **`on_status (on_status_igm_3)` [Unsolicited] (BPP -> BAP)**: Seller updates post-resolution order audit status.

---

### Flow 21: Delivery_Flow_With_IGM_Rejection(v-2.0.0) (Rejection, Escalation & Replacement)

#### 1. Short Description
A multi-tier grievance escalation flow under IGM 2.0.0. The shopper rejects initial resolution proposals, escalates the dispute to Level 2 (GRO / Arbitrator), reaches an accepted binding resolution, and receives a replacement cosmetic parcel dispatched by the seller.

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
- **`on_update (on_update_igm_replacement)` [Unsolicited] (BPP -> BAP)**: Seller automatically triggers replacement fulfillment parcel containing the replacement cosmetic item.

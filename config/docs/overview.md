# Retail Home & Kitchen (ONDC:RET16 1.2.5)

- [Overview](#overview)
- [Participants](#participants)
- [The User Journey](#the-user-journey)
  - [1. Discovery and Catalog Search](#1-discovery-and-catalog-search)
  - [2. Material/Dimension Selection and Serviceability Check](#2-materialdimension-selection-and-serviceability-check)
  - [3. Order Initialization and Shipping Configuration](#3-order-initialization-and-shipping-configuration)
  - [4. Order Confirmation and Prepaid Escrow](#4-order-confirmation-and-prepaid-escrow)
  - [5. Order Processing, Picking, and Protective Packaging](#5-order-processing-picking-and-protective-packaging)
  - [6. Logistics and Fragile Handling Courier Assignment](#6-logistics-and-fragile-handling-courier-assignment)
  - [7. Order Dispatch, In-Flight Tracking, and Secure Delivery](#7-order-dispatch-in-flight-tracking-and-secure-delivery)
  - [8. Settlement and Post-Fulfillment](#8-settlement-and-post-fulfillment)
- [Additional Scenarios in Version 1.2.5](#additional-scenarios-in-version-125)
  - [1. Text Customization and Personalized Engraving](#1-text-customization-and-personalized-engraving)
  - [2. Purchase Financing, Consumer Credit, and EMI Checkout](#2-purchase-financing-consumer-credit-and-emi-checkout)
  - [3. Seller Network Participant (SNP) Payment Collection](#3-seller-network-participant-snp-payment-collection)
  - [4. Dedicated Post-Order Hardware and Homeware Replacement](#4-dedicated-post-order-hardware-and-homeware-replacement)
  - [5. Buyer-Initiated Return and Reverse QC Pickup](#5-buyer-initiated-return-and-reverse-qc-pickup)
  - [6. Catalog Rejection and Compliance Validation](#6-catalog-rejection-and-compliance-validation)
  - [7. Buyer-Side Order Cancellation](#7-buyer-side-order-cancellation)
  - [8. Merchant-Side Part-Cancellation and Return to Origin (RTO)](#8-merchant-side-part-cancellation-and-return-to-origin-rto)
  - [9. In-Transit Force Cancellation and Settlement](#9-in-transit-force-cancellation-and-settlement)
  - [10. Out of Stock Handling: Cart Recovery vs. Protocol Error Code](#10-out-of-stock-handling-cart-recovery-vs-protocol-error-code)
  - [11. Incremental Catalog Refresh (Push and Pull)](#11-incremental-catalog-refresh-push-and-pull)
  - [12. Statutory Compliance, BIS Quality Orders, and Food Contact Standards](#12-statutory-compliance-bis-quality-orders-and-food-contact-standards)
- [Issue and Grievance Management](#issue-and-grievance-management)
  - [1. IGM 1.0.0 Architecture](#1-igm-100-architecture)
  - [2. IGM 2.0.0 Architecture](#2-igm-200-architecture)
- [Detailed Protocol Flows](#detailed-protocol-flows)
  - [Flow 1: Delivery Flow (Standard Forward Fulfillment)](#flow-1-delivery-flow-standard-forward-fulfillment)
  - [Flow 2: Customization Input Text Flow](#flow-2-customization-input-text-flow)
  - [Flow 3: Purchase Finance Flow](#flow-3-purchase-finance-flow)
  - [Flow 4: SNP Collecting Payment Flow](#flow-4-snp-collecting-payment-flow)
  - [Flow 5: Replacement Flow (Homeware Reverse QC and Reshipment)](#flow-5-replacement-flow-homeware-reverse-qc-and-reshipment)
  - [Flow 6: Return Flow (Post-Delivery Return and Refund)](#flow-6-return-flow-post-delivery-return-and-refund)
  - [Flow 7: Buyer Cancellation Flow](#flow-7-buyer-cancellation-flow)
  - [Flow 8: Seller Cancellation Flow (Warehouse Part-Cancellation and RTO)](#flow-8-seller-cancellation-flow-warehouse-part-cancellation-and-rto)
  - [Flow 9: Force Cancellation Flow (In-Transit Cancellation)](#flow-9-force-cancellation-flow-in-transit-cancellation)
  - [Flow 10: Out of Stock Flow (Cart Modification Recovery)](#flow-10-out-of-stock-flow-cart-modification-recovery)
  - [Flow 11: Out of Stock Flow (Immediate Error Code)](#flow-11-out-of-stock-flow-immediate-error-code)
  - [Flow 12: Catalog Rejection Flow (Statutory and Category Discrepancy)](#flow-12-catalog-rejection-flow-statutory-and-category-discrepancy)
  - [Flow 13: Discovery Flow: Full Catalog City Broadcast](#flow-13-discovery-flow-full-catalog-city-broadcast)
  - [Flow 14: Discovery Flow: Incremental Catalog Push and Disablement](#flow-14-discovery-flow-incremental-catalog-push-and-disablement)
  - [Flow 15: Discovery Flow: Incremental Catalog Refresh Pull](#flow-15-discovery-flow-incremental-catalog-refresh-pull)
  - [Flow 16: Delivery Flow with IGM 1.0.0 Dispute Resolution](#flow-16-delivery-flow-with-igm-100-dispute-resolution)
  - [Flow 17: Delivery Flow with IGM 2.0.0: Evidence Exchange and Return](#flow-17-delivery-flow-with-igm-200-evidence-exchange-and-return)
  - [Flow 18: Delivery Flow with IGM 2.0.0: Resolution Accepted (No Action)](#flow-18-delivery-flow-with-igm-200-resolution-accepted-no-action)
  - [Flow 19: Delivery Flow with IGM 2.0.0: Rejection, Escalation and Replacement](#flow-19-delivery-flow-with-igm-200-rejection-escalation-and-replacement)

---

## Overview

The Home & Kitchen domain (**ONDC:RET16**, specification version **1.2.5**) establishes an open, interoperable digital commerce standard for cookware, kitchenware, tableware, dining essentials, home furnishing, bed linen, home decor, lighting, household storage, and domestic cleaning utilities across the Open Network for Digital Commerce (ONDC). Retail home and kitchen merchandise spans an extraordinarily diverse range of materials, dimensions, and handling requirements—from fragile ceramic dinner sets and crystal glassware to heavy tri-ply cookware, high-thread-count bed linens, and modular storage organizers.

Specification version **1.2.5** expands the foundational retail architecture with dedicated homeware capabilities:
1. **Customization & Monogramming Directives**: Enabling buyers to specify custom text inputs (such as personalized monogramming on chef aprons, laser-engraved personal names on knife sets, custom dedication plaques on decor items, or custom curtain dimension directives) captured seamlessly during cart selection.
2. **Purchase Financing & EMI Checkout**: Direct protocol support for consumer credit, Equated Monthly Installments (EMI), and Buy-Now-Pay-Later (BNPL) integrations to accommodate premium cookware sets, artisanal tableware, and luxury home furnishing suites.
3. **Seller Network Participant (SNP) Payment Collection**: Enabling sellers to collect payments directly via their own payment gateways or merchant accounts rather than exclusively relying on BAP escrow capture.
4. **Dedicated Homeware Replacement Lifecycle**: A specialized 21-step post-delivery replacement workflow incorporating interim reverse QC evaluation, doorstep transit damage inspection, reverse courier transport, and outbound dispatch of a replacement unit.
5. **Catalog Rejection Validation**: Automated network rejection mechanisms (`/catalog_rejection`) ensuring items violating Bureau of Indian Standards (BIS) Quality Control Orders (QCO) for pressure cookers, non-electric cookware standards, or Legal Metrology rules are flagged and rejected.
6. **In-Transit Forced Cancellation**: Formalized procedures for terminating delivery when a shipment is already out for delivery, with automated freight settlement reconciliation.
7. **Store Disablement Broadcasting**: Real-time push notifications signaling warehouse operational shutdowns, temporary maintenance, or localized service cutoffs.

ONDC unbundles the traditionally closed home retail marketplace. Consumers can discover products across local homeware stores, regional kitchenware distributors, artisan ceramic studios, and direct-to-consumer (D2C) home furnishing brands using their preferred **Buyer Application (BAP)**. Sellers manage their inventory, dimensions, material tags, and transparent pricing through a **Seller Application (BPP)**, while specialized **Logistics Service Providers (LSPs)** execute delicate parcel delivery, protective cushioning, and doorstep reverse logistics.

The protocol standardizes all network interactions across:
- **Discovery**: `/search` and `/on_search` (city-wide broadcast queries, category taxonomies, material/dimension attributes, and incremental catalog push/pull).
- **Ordering**: `/select`, `/on_select`, `/init`, `/on_init`, `/confirm`, and `/on_confirm`.
- **Fulfillment & Real-time Tracking**: Unsolicited `/on_status` lifecycle events (`Accepted`, `Packed`, `Agent-assigned`, `Order-picked-up`, `Out-for-delivery`, `Order-delivered`), `/track`, and `/on_track`.
- **Post-Order Lifecycle & Exceptions**: `/update`, `/on_update`, `/cancel`, `/on_cancel`, and `/catalog_rejection` (doorstep quality-checked returns, reverse logistics pickup, warehouse bench testing, merchant part-cancellations, in-transit forced cancellations, and Return to Origin / RTO).
- **Grievance Redressal**: Issue and Grievance Management under both **IGM 1.0.0** and **IGM 2.0.0** architectures.

---

## Participants

| Participant | What This Means |
|---|---|
| **Buyer Application (BAP)** | The consumer-facing digital application (e.g., home decor shopping apps, banking portals, super-apps, telco marketplaces) where shoppers search cookware and home furnishing catalogs, filter by material, dimensions, and brand, select personalization options, apply for purchase financing, configure delivery addresses, complete prepaid payments, track couriers in real time, and raise post-delivery grievances. |
| **Seller Application (BPP)** | An application representing kitchenware retail chains, home decor boutiques, linen manufacturers, artisanal tableware studios, or D2C homeware brands. The BPP publishes item catalogs with material attributes, dimensions, and BIS certification details, validates delivery serviceability, calculates quotes with customization surcharges, manages protective packing with fragile labels, coordinates consumer financing terms, and executes reverse QC inspections. |
| **Logistics Service Provider (LSP)** | A delivery network participant that executes parcel transport with fragile cargo care (protective cushioning, honeycomb paper wrapping, anti-shock transit handling). In seller-managed logistics, the BPP or its integrated delivery partner allocates couriers, provides live GPS tracking, captures secure OTP delivery verification, and executes reverse logistics pickups. |
| **Gateway** | The ONDC routing infrastructure that multicasts broadcast discovery requests (`/search`) from BAPs to active seller applications (BPPs) based on domain code (`ONDC:RET16`), city code (e.g. `std:080`), and geolocation parameters. |

---

## The User Journey

The standard home and kitchen ordering journey (`Delivery_Flow`) enables a consumer to search for cookware, dining sets, or home furnishing, compare materials and dimensions, review transparent price breakdowns and turnaround times, provide delivery coordinates, complete prepaid payment, and receive securely packaged homeware with continuous shipment tracking.

### 1. Discovery and Catalog Search

The buyer initiates discovery on the BAP by searching for home and kitchen products, material variants, or specific categories (e.g., "Tri-ply Stainless Steel Kadai 24cm", "Ceramic Dinner Set 18 piece", "Cotton King Bedsheet 300TC", "Borosilicate Glass Containers"):

- **Intent Broadcast**: The BAP transmits an asynchronous `/search` request via the ONDC Gateway specifying domain `ONDC:RET16`, buyer geolocation coordinates, city code, and fulfillment type (`Delivery`).
- **Catalog Delivery**: Active BPPs within the serviceable area respond with asynchronous `/on_search` payloads containing their store catalog (`bpp/providers[]`). This includes product categories, custom menu groupings, brand metadata, model numbers, hardware/material specifications (cookware diameter, volume in liters, bedsheet dimensions in cm, thread count, dishwasher/microwave safety tags), MRP, discounted selling price, stock availability, warranty disclosure, customization capabilities, and statutory Legal Metrology attributes.

### 2. Material/Dimension Selection and Serviceability Check

The buyer selects an exact homeware product, set size, or dimension variant (e.g., 28cm Non-Stick Frying Pan with Glass Lid) and proceeds to configure checkout:

- **Network interaction:**
  - **`/select` (BAP -> BPP)**: The BAP transmits the selected item ID, variant specifications, quantity, provider location ID, and delivery destination coordinates (`fulfillments[0].end.location.gps` and `address.area_code`).
  - **`/on_select` (BPP -> BAP)**: The seller validates real-time inventory at the fulfillment facility, confirms delivery serviceability, and computes a detailed quote breakdown (`quote.breakup[]`). This includes the item base price, applicable taxes (CGST/SGST), protective fragile packaging / honeycomb padding fees, logistics shipping charges, and estimated turnaround time (`@ondc/org/TAT`). If the requested item or variant is depleted, the seller responds with an out-of-stock protocol error code (`40002` or `30009`).

### 3. Order Initialization and Shipping Configuration

The buyer confirms recipient information and finalized delivery coordinates:

- **Network interaction:**
  - **`/init` (BAP -> BPP)**: The BAP transmits customer details (name, phone number, email), exact street address, floor number, fragile delivery reminders (e.g., handle with care), and payment preference.
  - **`/on_init` (BPP -> BAP)**: The seller freezes the item quote and turnaround time, specifies static and dynamic order terms (cancellation window, return eligibility duration), establishes payment collection requirements (prepaid BAP-collected transaction or SNP-collected gateway flow), and returns settlement fee details.

### 4. Order Confirmation and Prepaid Escrow

Transactions in this domain follow a prepaid escrow model to protect high-value cookware and delicate home decor shipments:

- **Network interaction:**
  - **`/confirm` (BAP -> BPP)**: The BAP captures digital payment from the buyer via UPI, credit card, net banking, or consumer finance/EMI, generates a unique order identifier (`order.id`), and transmits payment confirmation parameters (`payment.params.transaction_id`, `payment.status = "PAID"`, `payment.type = "PRE-PAID"`).
  - **`/on_confirm` (BPP -> BAP)**: The seller validates payment receipt, records the order in its Warehouse Management / Order Management System (WMS/OMS), initializes order state (`order.state = "Created"`), and confirms order creation.

### 5. Order Processing, Picking, and Protective Packaging

The seller initiates warehouse fulfillment operations:

- The warehouse picks the items from storage bins (cookware, glassware, dinner sets, or packaged linens).
- Packaging undergoes rigorous shock-mitigation protocols:
  - Fragile ceramics and glassware are encased in multi-layer bubble cushioning, honeycomb paper, and corrugated partitions.
  - Heavy cast-iron and steel cookware items are boxed with edge protectors and reinforced tape.
  - Exterior cartons are prominently marked with "Fragile - Handle with Care" and orientation arrows.
- **Protocol Status Progression:**
  - **`on_status (on_status_pending)` [Unsolicited] (BPP -> BAP)**: Merchant system acknowledges order processing; `order.state` advances to `Accepted`.
  - **`on_status (on_status_packed)` [Unsolicited] (BPP -> BAP)**: Unit is securely packaged with invoice and warranty booklet inside; `fulfillment.state` updates to `Packed` and `order.state` to `In-progress`.

### 6. Logistics and Fragile Handling Courier Assignment

The seller or its integrated Logistics Service Provider assigns a dedicated courier:

- A delivery agent equipped for fragile parcel transit is allocated to the shipment.
- **Protocol Status Progression:**
  - **`on_status (on_status_agent_assigned)` [Unsolicited] (BPP -> BAP)**: Courier details (agent name, masked phone number, vehicle type) are transmitted; `order.state` remains `In-progress`.
  - **`on_status (on_status_picked)` [Unsolicited] (BPP -> BAP)**: Courier verifies external carton integrity, scans airway bill barcode, and departs warehouse; `order.state` remains `In-progress`.

### 7. Order Dispatch, In-Flight Tracking, and Secure Delivery

The shipment moves through the courier network toward the buyer's doorstep:

- **Real-Time Tracking:**
  - **`/track` (BAP -> BPP)**: The BAP queries live parcel transit coordinates.
  - **`/on_track` (BPP -> BAP)**: The BPP or LSP returns real-time GPS telemetry and an active web tracking link (`tracking.url`).
- **Doorstep Authentication & Handover:**
  - **`on_status (on_status_out_for_delivery)` [Unsolicited] (BPP -> BAP)**: Courier arrives in the immediate delivery sector; `order.state` remains `In-progress`.
  - At the doorstep, the delivery agent hands over the parcel and completes delivery verification. The customer is advised to retain the original carton and unboxing packaging in case return inspection is required.
  - **`on_status (on_status_order_delivered)` [Unsolicited] (BPP -> BAP)**: Successful handover is confirmed; `order.state` transitions to terminal state `Completed`.

### 8. Settlement and Post-Fulfillment

Upon successful delivery completion:
- The return window countdown timer begins (typically 7 days for home & kitchen goods, subject to seller policy).
- The BAP releases funds from escrow to the seller's account net of network fees, taxes, and shipping logistics charges in accordance with ONDC settlement guidelines.
- The buyer retains the tax invoice enabling registration for manufacturer warranties on pressure cookers and cookware coatings.

---

## Additional Scenarios in Version 1.2.5

Version 1.2.5 introduces expanded capabilities specifically tailored to home and kitchen commerce, including personalization inputs, installment financing, SNP-collected payments, dedicated homeware replacements, in-transit force cancellations, and catalog compliance rejections.

### 1. Text Customization and Personalized Engraving

Home and kitchen items frequently offer personalization such as monogrammed linens or laser-engraved cutlery and chef knives (`Customization_Input_Text_Flow`):

- **Custom Input Capture (`/select` - `select_input`)**: During cart selection, the buyer provides customized text input (such as personalized monogram text, custom names for laser engraving, or custom curtain dimension directives) via tagged configuration attributes.
- **Customization Pricing & Serviceability (`/on_select` - `on_select_input`)**: The seller evaluates the requested customization, calculates any customization/engraving surcharges in the itemized quote (`quote.breakup[]`), and confirms delivery timelines.
- **Fulfillment with Personalization**: The warehouse completes custom engraving or monogramming before packaging, and the order progresses through standard fulfillment to `Completed`.

### 2. Purchase Financing, Consumer Credit, and EMI Checkout

High-value cookware sets (multi-piece tri-ply stainless steel sets, premium Dutch ovens, luxury dinner services) rely heavily on Equated Monthly Installment (EMI) and Buy-Now-Pay-Later (BNPL) credit models (`Purchase_Finance_Flow`):

- **Financing Terms Initialization (`/init` - `init_fin`)**: The buyer chooses a consumer credit or financing payment method, specifying preferred tenure (e.g., 3, 6, 9, or 12 months), down payment amount, and NBFC / lending partner details.
- **Credit Schedule & Interest Quote (`/on_init` - `on_init_fin`)**: The seller responds with frozen financing parameters, including installment schedules, monthly interest rates, processing fees, and loan sanction terms.
- **Financed Order Confirmation (`/confirm` - `confirm_fin`)**: Upon successful loan sanction and down payment capture, the BAP confirms the order, passing the financier transaction identifier. Fulfillment proceeds with progressive tracking.

### 3. Seller Network Participant (SNP) Payment Collection

In addition to standard BAP-collected escrow payments, version 1.2.5 explicitly supports direct payment collection by the Seller Network Participant (`SNP_Collecting_Payment_Flow`):

- **SNP Gateway Routing (`/on_init` - `on_init_snp` & `on_init_snp_unsolicited`)**: The seller indicates that payment collection is handled directly by the BPP / seller gateway. The seller emits an unsolicited callback containing a direct payment gateway checkout URL or tokenized payment request.
- **SNP Payment Confirmation (`/confirm` - `confirm_snp`)**: The buyer completes payment on the seller gateway, and the BAP conveys payment verification parameters to the BPP to finalize order creation.

### 4. Dedicated Post-Order Hardware and Homeware Replacement

Unlike simple returns for refund, damaged or shattered multi-piece tableware frequently triggers a dedicated replacement workflow (`Replacement_Flow`):

- **Replacement Request with Reverse QC (`/update` - `update_reverse_qc_rep`)**: After delivery, the buyer requests a replacement citing transit breakage (e.g., shattered glass lid or cracked ceramic casserole), uploading unboxing photos and part identifiers.
- **Interim Reverse QC & Approval (`/on_update` - `on_update_interim_reverseQc` & `on_update_return_approved`)**: The seller reviews preliminary evidence and authorizes a doorstep reverse QC pickup.
- **Reverse Pickup & Warehouse Receipt (`on_update_return_picked_rep` & `on_update_return_delivered_rep`)**: A reverse logistics courier collects the damaged component after verifying physical condition.
- **Replacement Unit Reshipment (`on_status_packed_rep` to `on_status_order_delivered_rep`)**: Once the return is accepted, the seller initiates a replacement fulfillment leg: packaging a brand-new replacement component or set, assigning a courier, and delivering it to the buyer with end-to-end status tracking.

### 5. Buyer-Initiated Return and Reverse QC Pickup

For orders eligible for refund rather than replacement (`Return_Flow`):

- **Return Initiation & Evaluation (`/update` - `update_return` & `on_update_return_init`)**: The buyer requests a return for refund within the allowed return policy window.
- **Doorstep Reverse QC (`on_update_return_picked`)**: A reverse logistics courier conducts physical checks (ensuring cookware is unburnt, original accessories present, and bed linen unwashed/tagged).
- **Settlement Trail Disbursement (`update_settlement_trail` & `on_update_return_delivered`)**: When the item is received and validated at the merchant facility, the seller releases the refund settlement to the buyer.

### 6. Catalog Rejection and Compliance Validation

Version 1.2.5 introduces an automated compliance validation path (`Catalog_Rejection_Flow`):

- **Catalog Validation (`/catalog_rejection` - `catalog_rejection`)**: Following catalog discovery (`/search` and `/on_search`), the buyer application validates seller homeware listings against network compliance rules. If a pressure cooker listing omits mandatory Bureau of Indian Standards (BIS) ISI licensing under Quality Control Orders (QCO) or violates Legal Metrology guidelines, the BAP transmits a formal catalog rejection message, isolating non-compliant items from being purchased.

### 7. Buyer-Side Order Cancellation

Pre-dispatch cancellation initiated by the consumer (`Buyer_Cancellation_Flow`):

- **Cancellation Request (`/cancel`)**: The buyer triggers order cancellation prior to courier pickup, providing a standardized cancellation reason code (e.g., `001` for accidental order).
- **Merchant Acknowledgment (`/on_cancel`)**: The BPP verifies that the order is cancellable (`@ondc/org/cancellable = true`), terminates warehouse picking, transitions `order.state = "Cancelled"`, and triggers an automated full refund.

### 8. Merchant-Side Part-Cancellation and Return to Origin (RTO)

A dual-exception lifecycle (`Seller_Cancellation_Flow`) handling warehouse packing discrepancies and delivery failures:

- **Warehouse Part-Cancellation (`on_update` - `on_update_part_cancel`)**: The merchant discovers during packaging that one specific homeware item is damaged or out of stock. The seller cancels that line item via an unsolicited update, and the BAP adjusts the settlement trail (`update_partial_cancel_settlement`).
- **Outbound Fulfillment**: Remaining serviceable items are dispatched to `Out-for-delivery`.
- **Doorstep Delivery Failure & RTO (`on_cancel_rto` & `on_status_rto_delivereddisposed`)**: If the buyer is unreachable or refuses delivery, the courier initiates RTO. The goods return to the origin warehouse or are disposed of per policy, and the order is marked `Cancelled`.

### 9. In-Transit Force Cancellation and Settlement

In exceptional circumstances where a buyer insists on cancelling while goods are already in transit (`Force_Cancellation_Flow`):

- **Initial Attempt & Policy Enforcement (`/cancel` - `cancel_no`)**: The buyer requests cancellation while the shipment is `Out-for-delivery`. The system initially rejects the cancellation because the parcel is in active delivery transit.
- **Forced Cancellation Override (`/cancel` - `cancel_yes` & `/on_cancel` - `on_cancel_yes`)**: The buyer or network authority invokes a forced cancellation override citing a critical valid reason code. The seller halts delivery, instructs the courier to return, marks the order `Cancelled`, and the BAP coordinates an immediate cancellation settlement update (`update_settlement_cancel`).

### 10. Out of Stock Handling: Cart Recovery vs. Protocol Error Code

When inventory for a specific cookware model, pan diameter, or bedsheet color configuration is depleted:

- **Cart Recovery Path (`Out_Of_Stock_Flow`)**: The buyer selects an out-of-stock homeware item. On receiving the shortage notice, the buyer modifies the selection to an alternative model or available variant within the same transaction session, proceeds to order placement, and completes fulfillment with live tracking.
- **Immediate Error Code Path (`Out_Of_Stock_Flow(Error-code)`)**: When an item or variant is unavailable and no substitution occurs, the BPP immediately rejects the `/select` call on `/on_select` with error code `40002` (Out of Stock) or `30009`, allowing the buyer app to display clear unavailable badges.

### 11. Incremental Catalog Refresh (Push and Pull)

Homeware catalogs experience regular seasonal updates, festive sales promotions, stock replenishings, and store operating hours:

- **Incremental Push (`Discovery_Flow_incremental_catalog`)**: The seller proactively publishes catalog delta updates via unsolicited `/on_search` payloads containing modified items and pricing. In version 1.2.5, sellers can also broadcast store/warehouse disablement notifications (`on_search_inc_disable`) to temporarily pause ordering during stocktaking or emergencies.
- **Incremental Pull (`Discovery_Flow_incremental_catalog_refresh_pull`)**: The buyer app periodically polls for catalog changes by transmitting a `/search` request with tag `catalog_inc = "true"` and a timestamp filter, receiving only modified products.

### 12. Statutory Compliance, BIS Quality Orders, and Food Contact Standards

Retail home and kitchen listings on ONDC are subject to strict Indian regulatory and consumer protection standards:

- **BIS Quality Control Orders (QCO) for Domestic Pressure Cookers**: All domestic pressure cookers sold in India must mandatorily conform to Indian Standard IS 2347 and display a valid Bureau of Indian Standards (BIS) Standard Mark (ISI mark) and license number. Listings without valid BIS licensing are prohibited.
- **Food Contact Material Safety**: Cookware, bake-ware, and food storage containers must comply with non-toxic, food-grade standards:
  - PTFE non-stick coatings must be certified PFOA-free and cadmium/lead-safe.
  - Stainless steel utensils must specify commercial grades (e.g. AISI 304 / 18/8 food-grade steel).
- **Legal Metrology (Packaged Commodities) Rules, 2011**: Product listings must explicitly publish the country of origin, manufacturer and importer details, date of manufacture/import, Maximum Retail Price (MRP inclusive of all taxes), net dimensions (diameter, height, length in cm), volume capacity (in liters/ml), gross weight, and customer grievance redressal contact information.
- **Textile & Bed Linen Labeling**: Bed sheets, blankets, and curtains must disclose fiber composition (e.g., 100% Cotton, Microfiber), thread count (TC), dimensions, and care washing instructions.

---

## Issue and Grievance Management

ONDC specifies structured dispute resolution mechanisms to handle post-order grievances—such as broken glassware, missing pot lids, chipped ceramic plates, or delayed deliveries—under both **IGM 1.0.0** and **IGM 2.0.0** architectures.

### 1. IGM 1.0.0 Architecture

IGM 1.0.0 provides a single-ticket grievance lifecycle between the buyer application and seller application:

- **Issue Filing (`/issue` - `issue_open_100`)**: The buyer submits a formal grievance via the BAP specifying the complaint category, subcategory (e.g., `TRANSIT_DAMAGE`, `DEFECTIVE_PRODUCT`, `MISSING_ACCESSORIES`), narrative description, and contact details.
- **Issue Acknowledgment (`/on_issue` - `on_issue_processing_100`)**: The BPP acknowledges the issue, assigns an internal ticket identifier, and furnishes the details of the designated Grievance Officer.
- **Issue Resolution (`on_issue_status` [Unsolicited] - `on_issue_resolved_100`)**: The seller investigates the claim and publishes a resolution payload detailing the remedial action taken (e.g., dispatching replacement parts or processing partial credit).
- **Issue Closure (`/issue` - `issue_close_100`)**: The buyer verifies that the grievance has been satisfactorily addressed and emits an issue closure message.

### 2. IGM 2.0.0 Architecture

IGM 2.0.0 introduces a robust, multi-participant, role-based dispute framework featuring evidence exchange, photographic proof of transit breakage, multiple resolution remedies (`REFUND`, `REPLACEMENT`, `NO_ACTION`), and formal escalation paths to Level 2 Grievance Officers and Network Intermediaries:

1. **Evidence Exchange & Return Authorization (`Delivery_Flow_With_IGM(v-2.0.0)`)**:
   - The buyer opens a grievance reporting damaged cookware upon delivery.
   - The seller requests additional photographic evidence via `on_issue_need_more_info`.
   - The buyer provides unboxing photos via `issue_info_provided`.
   - The seller acknowledges and approves a return resolution, initiating reverse courier pickup and refund settlement via an unsolicited `on_update` (`on_update_igm_return`).

2. **Resolution Accepted with `NO_ACTION` (`Delivery_Flow_With_IGM_No_Action(v-2.0.0)`)**:
   - The buyer opens a grievance alleging a product defect (e.g., stainless steel cookware surface showing natural heat tint).
   - The merchant examines the photographic evidence and determines that the coloration is standard stainless steel oxidation that does not impair cooking or food safety.
   - The seller issues an unsolicited `on_issue` with resolution action `NO_ACTION`, accompanied by proper cleaning care guidance.
   - The buyer accepts the technical explanation (`/issue`), the ticket is closed, and the seller synchronizes the final order audit record via an unsolicited `on_status`.

3. **Rejection, Level 2 Escalation & Replacement Ruling (`Delivery_Flow_With_IGM_Rejection(v-2.0.0)`)**:
   - The buyer reports shattered ceramic dinnerware upon unboxing.
   - The merchant initially proposes an inadequate cosmetic voucher.
   - The buyer rejects the resolution (`issue_resolution_reject`).
   - The merchant attempts a revised proposal, which the buyer also rejects, subsequently escalating the dispute to a Level 2 Grievance Officer / Network Intermediary (`issue_escalate`).
   - The escalated mediator reviews unboxing photos and delivery timestamps, ruling in favor of the buyer and ordering full product replacement.
   - The buyer accepts the escalated ruling, the dispute is closed, and the seller dispatches a replacement parcel with reverse collection via an unsolicited `on_update` (`on_update_igm_replacement`).

---

## Detailed Protocol Flows

All **19 protocol flows** defined in `automation-specifications/config/flows/index.yaml` for the Home & Kitchen domain (`ONDC:RET16 1.2.5`) are detailed below with their classification tags, operational contexts, and full step-by-step API message sequences.

---

### Flow 1: Delivery Flow (Standard Forward Fulfillment)

- **Flow ID:** `Delivery_Flow`
- **Config File:** `./HOME&KITCHEN/Delivery_Flow.yaml`
- **Protocol Version:** `1.2.5`
- **Use Case:** `HOME&KITCHEN`
- **Tags:** `PRAMAAN`, `REPORTABLE`, `WORKBENCH`, `MANDATORY`

#### 1. Short Description
The baseline forward fulfillment lifecycle for home and kitchen merchandise in version 1.2.5. Covers product selection, delivery quote verification, order initialization, prepaid payment capture, warehouse picking with shock-mitigation packaging, progressive status updates, live tracking telemetry, and doorstep delivery.

#### 2. API Breakdown & Technical Actions
- **Step 1: `/select (select)` (BAP -> BPP)**: The BAP selects home and kitchen products from the seller's catalog, specifying delivery destination coordinates and fulfillment type.
- **Step 2: `/on_select (on_select)` (BPP -> BAP)**: The seller validates real-time inventory, confirms fulfillment serviceability (`Fulfillment: Serviceable`), and returns an itemized price quote (`quote.breakup[]`) with delivery turnaround time.
- **Step 3: `/init (init)` (BAP -> BPP)**: The BAP transmits customer details, billing address, exact delivery location, and payment preference to initiate the order draft.
- **Step 4: `/on_init (on_init)` (BPP -> BAP)**: The seller responds with frozen commercial terms, payment parameters, cancellation windows, and settlement rules.
- **Step 5: `/confirm (confirm)` (BAP -> BPP)**: The BAP captures prepaid digital payment and submits the confirmed order with `order.state = "Created"`.
- **Step 6: `/on_confirm (on_confirm)` (BPP -> BAP)**: The seller validates payment, records the order in OMS/WMS, and confirms `order.state = "Created"`.
- **Step 7: `on_status (on_status_pending)` [Unsolicited] (BPP -> BAP)**: The merchant confirms warehouse order processing; `order.state` transitions to `Accepted`.
- **Step 8: `on_status (on_status_packed)` [Unsolicited] (BPP -> BAP)**: The item is picked from storage, wrapped in protective bubble/honeycomb padding, and packed in reinforced cartons; `fulfillment.state` updates to `Packed` and `order.state` to `In-progress`.
- **Step 9: `on_status (on_status_agent_assigned)` [Unsolicited] (BPP -> BAP)**: A courier trained in fragile cargo handling is assigned; `order.state` remains `In-progress`.
- **Step 10: `on_status (on_status_picked)` [Unsolicited] (BPP -> BAP)**: The courier picks up the package from the merchant warehouse; `order.state` remains `In-progress`.
- **Step 11: `/track (track)` (BAP -> BPP)**: The BAP queries live in-transit location telemetry.
- **Step 12: `/on_track (on_track)` (BPP -> BAP)**: The BPP returns real-time GPS coordinates and an active web tracking link.
- **Step 13: `on_status (on_status_out_for_delivery)` [Unsolicited] (BPP -> BAP)**: The courier arrives in the delivery sector; `order.state` remains `In-progress`.
- **Step 14: `on_status (on_status_order_delivered)` [Unsolicited] (BPP -> BAP)**: Secure doorstep handover is completed and the customer receives the parcel; `order.state` transitions to `Completed`.

---

### Flow 2: Customization Input Text Flow

- **Flow ID:** `Customization_Input_Text_Flow`
- **Config File:** `./HOME&KITCHEN/Customization_Input_Text_Flow.yaml`
- **Protocol Version:** `1.2.5`
- **Use Case:** `HOME&KITCHEN`
- **Tags:** `PRAMAAN`, `REPORTABLE`, `WORKBENCH`, `MANDATORY`

#### 1. Short Description
Demonstrates homeware customization and personalization. The buyer inputs custom text (such as personalized monogram text, custom names for laser engraving on knives/cookware, or custom curtain dimension directives) during cart selection. The seller validates the customization, quotes any applicable customization surcharges, and fulfills the order.

#### 2. API Breakdown & Technical Actions
- **Step 1: `/select (select_input)` (BAP -> BPP)**: The BAP selects a homeware product and supplies custom personalization text input within the customization tags.
- **Step 2: `/on_select (on_select_input)` (BPP -> BAP)**: The seller validates text feasibility, confirms serviceability (`Fulfillment: Serviceable`), and computes an itemized quote including customization fees.
- **Step 3: `/init (init)` (BAP -> BPP)**: Order draft initialization with customer and delivery details.
- **Step 4: `/on_init (on_init)` (BPP -> BAP)**: Seller confirms commercial and customization terms.
- **Step 5: `/confirm (confirm)` (BAP -> BPP)**: Buyer confirms prepaid payment; `order.state = "Created"`.
- **Step 6: `/on_confirm (on_confirm)` (BPP -> BAP)**: Seller confirms order creation; `order.state = "Created"`.
- **Step 7: `on_status (on_status_pending)` [Unsolicited] (BPP -> BAP)**: Warehouse stages custom engraving or monogramming; `order.state` transitions to `Accepted`.
- **Step 8: `on_status (on_status_packed)` [Unsolicited] (BPP -> BAP)**: Personalized item is verified, quality checked, and packed; `fulfillment.state = "Packed"`, `order.state = "In-progress"`.
- **Step 9: `on_status (on_status_agent_assigned)` [Unsolicited] (BPP -> BAP)**: Courier assigned; `order.state = "In-progress"`.
- **Step 10: `on_status (on_status_picked)` [Unsolicited] (BPP -> BAP)**: Courier takes custody; `order.state = "In-progress"`.
- **Step 11: `on_status (on_status_out_for_delivery)` [Unsolicited] (BPP -> BAP)**: Package out for delivery; `order.state = "In-progress"`.
- **Step 12: `on_status (on_status_order_delivered)` [Unsolicited] (BPP -> BAP)**: Doorstep delivery completed; `order.state = "Completed"`.

---

### Flow 3: Purchase Finance Flow

- **Flow ID:** `Purchase_Finance_Flow`
- **Config File:** `./HOME&KITCHEN/Purchase_Finance_Flow.yaml`
- **Protocol Version:** `1.2.5`
- **Use Case:** `HOME&KITCHEN`
- **Tags:** `PRAMAAN`, `REPORTABLE`, `WORKBENCH`, `MANDATORY`

#### 1. Short Description
Purchase of premium homeware, luxury dinner sets, or comprehensive cookware suites with consumer installment financing (EMI / BNPL). Covers product selection, financing terms configuration, down payment and loan confirmation, and multi-stage fulfillment tracking.

#### 2. API Breakdown & Technical Actions
- **Step 1: `/select (select)` (BAP -> BPP)**: Buyer selects high-value homeware products.
- **Step 2: `/on_select (on_select)` (BPP -> BAP)**: Seller validates inventory and confirms delivery serviceability (`Fulfillment: Serviceable`).
- **Step 3: `/init (init_fin)` (BAP -> BPP)**: The BAP configures financing preferences, including installment tenure, down payment, and lending partner details.
- **Step 4: `/on_init (on_init_fin)` (BPP -> BAP)**: The seller returns the formal financing schedule, interest rate, processing charges, and loan agreement parameters.
- **Step 5: `/confirm (confirm_fin)` (BAP -> BPP)**: The BAP passes loan approval reference and down payment capture; `order.state = "Created"`.
- **Step 6: `/on_confirm (on_confirm_fin)` (BPP -> BAP)**: The seller validates financing terms and confirms order creation; `order.state = "Created"`.
- **Step 7: `on_status (on_status_pending_fin)` [Unsolicited] (BPP -> BAP)**: Order accepted by warehouse; `order.state` transitions to `Accepted`.
- **Step 8: `on_status (on_status_packed_fin)` [Unsolicited] (BPP -> BAP)**: Item packed with finance and warranty documentation; `order.state` transitions to `Accepted`.
- **Step 9: `on_status (on_status_agent_assigned_fin)` [Unsolicited] (BPP -> BAP)**: Courier assigned; `order.state` transitions to `Accepted`.
- **Step 10: `on_status (on_status_picked_fin)` [Unsolicited] (BPP -> BAP)**: Parcel loaded; `order.state` transitions to `Accepted`.
- **Step 11: `on_status (on_status_out_for_delivery_fin)` [Unsolicited] (BPP -> BAP)**: Parcel out for delivery; `order.state` transitions to `Accepted`.
- **Step 12: `on_status (on_status_order_delivered_fin)` [Unsolicited] (BPP -> BAP)**: Doorstep handover completed; `order.state` transitions to `Accepted`.

---

### Flow 4: SNP Collecting Payment Flow

- **Flow ID:** `SNP_Collecting_Payment_Flow`
- **Config File:** `./HOME&KITCHEN/SNP_Collecting_Payment_Flow.yaml`
- **Protocol Version:** `1.2.5`
- **Use Case:** `HOME&KITCHEN`
- **Tags:** `PRAMAAN`, `REPORTABLE`, `WORKBENCH`, `MANDATORY`

#### 1. Short Description
A retail transaction flow where the Seller Network Participant (SNP / BPP) collects payment directly from the consumer via a seller-hosted payment gateway or direct collection mechanism, followed by order confirmation and fulfillment tracking.

#### 2. API Breakdown & Technical Actions
- **Step 1: `/select (select)` (BAP -> BPP)**: Item selection and delivery serviceability query.
- **Step 2: `/on_select (on_select)` (BPP -> BAP)**: Seller confirms item availability and quote (`Fulfillment: Serviceable`).
- **Step 3: `/init (init)` (BAP -> BPP)**: Order draft initialization with customer and delivery details.
- **Step 4: `/on_init (on_init_snp)` (BPP -> BAP)**: Seller signals an SNP-collected payment model.
- **Step 5: `on_init (on_init_snp_unsolicited)` [Unsolicited] (BPP -> BAP)**: The seller transmits an unsolicited callback providing the seller payment gateway redirect URL and collection parameters.
- **Step 6: `/confirm (confirm_snp)` (BAP -> BPP)**: The buyer completes payment on the seller gateway, and the BAP transmits payment verification; `order.state = "Created"`.
- **Step 7: `/on_confirm (on_confirm)` (BPP -> BAP)**: Seller validates payment on its gateway and confirms order creation; `order.state = "Created"`.
- **Steps 8–13 (`on_status_pending` to `on_status_order_delivered`)**: Unsolicited fulfillment updates advancing through `Accepted` -> `Packed` -> `Agent-assigned` -> `Order-picked-up` -> `Out-for-delivery` -> `Completed`.

---

### Flow 5: Replacement Flow (Homeware Reverse QC and Reshipment)

- **Flow ID:** `Replacement_Flow`
- **Config File:** `./HOME&KITCHEN/Replacement_Flow.yaml`
- **Protocol Version:** `1.2.5`
- **Use Case:** `HOME&KITCHEN`
- **Tags:** `PRAMAAN`, `REPORTABLE`, `WORKBENCH`, `OPTIONAL`

#### 1. Short Description
A comprehensive 21-step post-delivery replacement lifecycle for home and kitchen items. Following delivery, the buyer requests a replacement for a transit-damaged or defective homeware component (e.g., shattered tempered glass lid). The seller conducts an interim reverse QC check, approves replacement, dispatches a reverse courier to verify and collect the damaged unit, and ships a brand-new replacement unit with complete status tracking.

#### 2. API Breakdown & Technical Actions
- **Steps 1–12 (`/select` to `on_status_order_delivered`)**: Outbound delivery of the original homeware product from cart checkout to successful delivery completion (`order.state = "Completed"`).
- **Step 13: `/update (update_reverse_qc_rep)` (BAP -> BPP)**: Buyer files a replacement request with reverse QC, submitting defect details, photos, and item identifiers.
- **Step 14: `/on_update (on_update_interim_reverseQc)` (BPP -> BAP)**: Seller acknowledges the reverse QC request and prepares return logistics.
- **Step 15: `on_update (on_update_return_approved)` [Unsolicited] (BPP -> BAP)**: Seller formally approves the replacement.
- **Step 16: `on_update (on_update_return_picked_rep)` [Unsolicited] (BPP -> BAP)**: Reverse pickup courier verifies item condition and collects the damaged component.
- **Step 17: `on_update (on_update_return_delivered_rep)` [Unsolicited] (BPP -> BAP)**: Defective component delivered back to seller warehouse.
- **Step 18: `on_status (on_status_packed_rep)` [Unsolicited] (BPP -> BAP)**: Seller packs a brand-new replacement component/unit; `order.state` transitions to `In-progress`.
- **Step 19: `on_status (on_status_picked_rep)` [Unsolicited] (BPP -> BAP)**: Courier picks up the replacement unit; `order.state` marked `Completed`.
- **Step 20: `on_status (on_status_out_for_delivery_rep)` [Unsolicited] (BPP -> BAP)**: Replacement package out for delivery; `order.state` marked `Completed`.
- **Step 21: `on_status (on_status_order_delivered_rep)` [Unsolicited] (BPP -> BAP)**: Replacement unit successfully delivered to the customer; order marked `Completed`.

---

### Flow 6: Return Flow (Post-Delivery Return and Refund)

- **Flow ID:** `Return_Flow`
- **Config File:** `./HOME&KITCHEN/Return_Flow.yaml`
- **Protocol Version:** `1.2.5`
- **Use Case:** `HOME&KITCHEN`
- **Tags:** `PRAMAAN`, `REPORTABLE`, `WORKBENCH`, `MANDATORY`

#### 1. Short Description
Standard post-delivery return flow for home and kitchen merchandise. Covers buyer return initiation, merchant return approval, doorstep reverse courier pickup with physical condition verification, settlement trail reconciliation, and warehouse receipt with refund release.

#### 2. API Breakdown & Technical Actions
- **Steps 1–12 (`/select` to `on_status_order_delivered`)**: Complete outbound order placement, confirmation, and delivery fulfillment (`order.state = "Completed"`).
- **Step 13: `/update (update_return)` (BAP -> BPP)**: Buyer submits a return request for refund within the return policy window.
- **Step 14: `/on_update (on_update_return_init)` (BPP -> BAP)**: Seller initializes reverse fulfillment.
- **Step 15: `on_update (on_update_return_approved)` [Unsolicited] (BPP -> BAP)**: Seller approves the return following photo verification.
- **Step 16: `on_update (on_update_return_picked)` [Unsolicited] (BPP -> BAP)**: Reverse courier verifies item condition (cookware unburnt, linen unwashed), checks physical condition, and accepts custody.
- **Step 17: `/update (update_settlement_trail)` (BAP -> BPP)**: BAP transmits updated settlement trail details for the refund disbursement.
- **Step 18: `on_update (on_update_return_delivered)` [Unsolicited] (BPP -> BAP)**: Item delivered to merchant warehouse, bench diagnostics verified, and return completed.

---

### Flow 7: Buyer Cancellation Flow

- **Flow ID:** `Buyer_Cancellation_Flow`
- **Config File:** `./HOME&KITCHEN/Buyer_Cancellation_Flow.yaml`
- **Protocol Version:** `1.2.5`
- **Use Case:** `HOME&KITCHEN`
- **Tags:** `PRAMAAN`, `REPORTABLE`, `WORKBENCH`, `MANDATORY`

#### 1. Short Description
Validates buyer-initiated pre-dispatch cancellation for a confirmed home & kitchen order. The seller halts warehouse packing and pallet dispatch, marks the order cancelled, and initiates an automated full refund.

#### 2. API Breakdown & Technical Actions
- **Steps 1–6 (`/select` to `/on_confirm`)**: Standard prepaid order creation and confirmation.
- **Step 7: `/cancel (cancel)` (BAP -> BPP)**: Buyer triggers cancellation before shipment dispatch, providing a valid cancellation reason code.
- **Step 8: `/on_cancel (on_cancel)` (BPP -> BAP)**: Seller validates cancellability (`@ondc/org/cancellable = true`), terminates fulfillment, sets `order.state = "Cancelled"`, and triggers automated refund.

---

### Flow 8: Seller Cancellation Flow (Warehouse Part-Cancellation and RTO)

- **Flow ID:** `Seller_Cancellation_Flow`
- **Config File:** `./HOME&KITCHEN/Seller_Cancellation_Flow.yaml`
- **Protocol Version:** `1.2.5`
- **Use Case:** `HOME&KITCHEN`
- **Tags:** `PRAMAAN`, `REPORTABLE`, `WORKBENCH`, `MANDATORY`

#### 1. Short Description
Exercises a multi-exception merchant lifecycle: warehouse picking stockout / damaged unit leading to partial order cancellation, outbound delivery of remaining goods, doorstep delivery failure (unreachable buyer), and Return to Origin (RTO) with warehouse return/disposal.

#### 2. API Breakdown & Technical Actions
- **Steps 1–6 (`/select` to `/on_confirm`)**: Multi-item homeware order confirmed.
- **Step 7: `on_update (on_update_part_cancel)` [Unsolicited] (BPP -> BAP)**: During warehouse picking, the seller identifies an unavailable/damaged item and emits an unsolicited update cancelling that line item.
- **Step 8: `/update (update_partial_cancel_settlement)` (BAP -> BPP)**: BAP adjusts quote and transmits partial refund settlement trail.
- **Steps 9–13 (`on_status_pending` to `on_status_out_for_delivery`)**: Outbound fulfillment of remaining items to `Out-for-delivery`.
- **Step 14: `on_cancel (on_cancel_rto)` [Unsolicited] (BPP -> BAP)**: Doorstep delivery fails (customer unreachable / delivery refused); seller initiates RTO (`order.state = "Cancelled"`).
- **Step 15: `on_status (on_status_rto_delivereddisposed)` [Unsolicited] (BPP -> BAP)**: Package returned to seller origin warehouse or disposed of per policy (`order.state = "Accepted"`).

---

### Flow 9: Force Cancellation Flow (In-Transit Cancellation)

- **Flow ID:** `Force_Cancellation_Flow`
- **Config File:** `./HOME&KITCHEN/Force_Cancellation_Flow.yaml`
- **Protocol Version:** `1.2.5`
- **Use Case:** `HOME&KITCHEN`
- **Tags:** `PRAMAAN`, `REPORTABLE`, `WORKBENCH`, `MANDATORY`

#### 1. Short Description
Handles an exceptional scenario where a customer demands cancellation while the homeware parcel is already in transit (`Out-for-delivery`). An initial cancellation attempt is rejected, followed by an authorized force cancellation override, shipment termination, and settlement trail adjustment.

#### 2. API Breakdown & Technical Actions
- **Steps 1–10 (`/select` to `on_status_picked`)**: Order confirmed and packed; courier takes custody.
- **Step 11: `on_status (on_status_out_for_delivery_force)` [Unsolicited] (BPP -> BAP)**: Parcel is out for delivery.
- **Step 12: `/cancel (cancel_no)` (BAP -> BPP)**: Buyer attempts cancellation; rejected due to active delivery transit.
- **Step 13: `/cancel (cancel_yes)` (BAP -> BPP)**: Buyer invokes force cancellation with critical reason code.
- **Step 14: `/on_cancel (on_cancel_yes)` (BPP -> BAP)**: Seller terminates delivery, instructs courier to return, and sets `order.state = "Cancelled"`.
- **Step 15: `/update (update_settlement_cancel)` [Unsolicited] (BAP -> BPP)**: BAP updates settlement trail to process immediate cancellation refund.

---

### Flow 10: Out of Stock Flow (Cart Modification Recovery)

- **Flow ID:** `Out_Of_Stock_Flow`
- **Config File:** `./HOME&KITCHEN/Out_Of_Stock_Flow.yaml`
- **Protocol Version:** `1.2.5`
- **Use Case:** `HOME&KITCHEN`
- **Tags:** `PRAMAAN`, `REPORTABLE`, `WORKBENCH`, `MANDATORY`

#### 1. Short Description
Demonstrates stockout recovery during checkout. The buyer selects an out-of-stock homeware item, receives an unavailable response, modifies the cart to select an available model or dimension variant, and successfully completes the order through to delivery.

#### 2. API Breakdown & Technical Actions
- **Step 1: `/select (select_out_of_stock)` (BAP -> BPP)**: Buyer selects a depleted model/pan diameter.
- **Step 2: `/on_select (on_select_out_of_stock)` (BPP -> BAP)**: Seller indicates out of stock (`quantity.available.count = 0`).
- **Step 3: `/select (select)` (BAP -> BPP)**: Buyer modifies cart, selecting an available model/size variant.
- **Step 4: `/on_select (on_select)` (BPP -> BAP)**: Seller confirms availability and quote (`Fulfillment: Serviceable`).
- **Steps 5–14 (`/init` to `on_status_order_delivered`)**: Standard order creation, prepaid confirmation, warehouse packaging, and delivery completion (`Completed`).

---

### Flow 11: Out of Stock Flow (Immediate Error Code)

- **Flow ID:** `Out_Of_Stock_Flow(Error-code)`
- **Config File:** `./HOME&KITCHEN/Out_Of_Stock_Flow_Error-code_.yaml`
- **Protocol Version:** `1.2.5`
- **Use Case:** `HOME&KITCHEN`
- **Tags:** `PRAMAAN`, `REPORTABLE`, `WORKBENCH`, `MANDATORY`

#### 1. Short Description
Validates protocol exception handling when a homeware buyer selects an out-of-stock product and the seller immediately rejects the transaction via structured error codes.

#### 2. API Breakdown & Technical Actions
- **Step 1: `/select (select_out_of_stock)` (BAP -> BPP)**: Buyer selects an out-of-stock item.
- **Step 2: `/on_select (on_select_out_of_stock)` (BPP -> BAP)**: Seller responds with error code `40002` or `30009` and sets `quantity.available.count = 0`, halting checkout progression.

---

### Flow 12: Catalog Rejection Flow (Statutory and Category Discrepancy)

- **Flow ID:** `Catalog_Rejection_Flow`
- **Config File:** `./HOME&KITCHEN/Catalog_Rejection_Flow.yaml`
- **Protocol Version:** `1.2.5`
- **Use Case:** `HOME&KITCHEN`
- **Tags:** `PRAMAAN`, `REPORTABLE`, `WORKBENCH`, `MANDATORY`

#### 1. Short Description
Validates network catalog compliance handling for home and kitchen merchandise. When a seller app transmits a catalog listing that violates statutory quality standards (such as missing Bureau of Indian Standards ISI certification for domestic pressure cookers or non-compliant Legal Metrology disclosures), the buyer app transmits a catalog rejection message to isolate non-compliant entries.

#### 2. API Breakdown & Technical Actions
- **Step 1: `/search (search)` (BAP -> BPP via Gateway)**: Broadcast search query for home and kitchen items.
- **Step 2: `/on_search (on_search)` (BPP -> BAP)**: Seller app transmits homeware catalog entries.
- **Step 3: `/catalog_rejection (catalog_rejection)` (BAP -> BPP)**: The BAP transmits a formal catalog rejection payload specifying non-compliant item IDs and compliance error codes.

---

### Flow 13: Discovery Flow: Full Catalog City Broadcast

- **Flow ID:** `Discovery_Flow_full_catalog`
- **Config File:** `./HOME&KITCHEN/Discovery_Flow_full_catalog.yaml`
- **Protocol Version:** `1.2.5`
- **Use Case:** `HOME&KITCHEN`
- **Tags:** `PRAMAAN`, `MANDATORY`, `REPORTABLE`, `WORKBENCH`

#### 1. Short Description
City-wide broadcast discovery where a buyer app searches for home and kitchen products and sellers return their full catalogs featuring custom menu groupings, material specifications, dimensions, and transparent pricing.

#### 2. API Breakdown & Technical Actions
- **Step 1: `/search (search)` (BAP -> BPP via Gateway)**: Broadcast search query specifying domain `ONDC:RET16` and city location coordinates.
- **Step 2: `/on_search (on_search)` (BPP -> BAP)**: Seller returns comprehensive catalog with category trees, brand attributes, material specs, warranty terms, and pricing.

---

### Flow 14: Discovery Flow: Incremental Catalog Push and Disablement

- **Flow ID:** `Discovery_Flow_incremental_catalog`
- **Config File:** `./HOME&KITCHEN/Discovery_Flow_incremental_catalog.yaml`
- **Protocol Version:** `1.2.5`
- **Use Case:** `HOME&KITCHEN`
- **Tags:** `PRAMAAN`, `REPORTABLE`, `WORKBENCH`, `MANDATORY`

#### 1. Short Description
Seller-initiated incremental catalog updates. The seller pushes delta product/pricing modifications and broadcasts warehouse disablement / operational shutdown notifications.

#### 2. API Breakdown & Technical Actions
- **Step 1: `/search (search_inc)` (BAP -> BPP)**: Initial baseline search.
- **Step 2: `on_search (on_search_inc)` [Unsolicited] (BPP -> BAP)**: Seller pushes an unsolicited incremental catalog update with revised prices and stock.
- **Step 3: `on_search (on_search_inc_disable)` [Unsolicited] (BPP -> BAP)**: Seller pushes store/service disablement status.
- **Step 4: `/search (search_inc)` (BAP -> BPP)**: Buyer app synchronizes and acknowledges updated status.

---

### Flow 15: Discovery Flow: Incremental Catalog Refresh Pull

- **Flow ID:** `Discovery_Flow_incremental_catalog_refresh_pull`
- **Config File:** `./HOME&KITCHEN/Discovery_Flow_incremental_catalog_refresh_pull.yaml`
- **Protocol Version:** `1.2.5`
- **Use Case:** `HOME&KITCHEN`
- **Tags:** `PRAMAAN`, `REPORTABLE`, `WORKBENCH`, `OPTIONAL`

#### 1. Short Description
Buyer-initiated incremental catalog refresh. The buyer app polls sellers using timestamp filters, fetching only modified products and pricing changes without re-downloading entire city catalogs.

#### 2. API Breakdown & Technical Actions
- **Step 1: `/search (search)` (BAP -> BPP via Gateway)**: Baseline discovery request.
- **Step 2: `/on_search (on_search)` (BPP -> BAP)**: Initial full catalog response.
- **Step 3: `/search (search_inc_pull)` (BAP -> BPP)**: Incremental pull query with `tags.catalog_inc = "true"` and timestamp filter.
- **Step 4: `/on_search (on_search_inc_pull)` (BPP -> BAP)**: Compact delta catalog payload.

---

### Flow 16: Delivery Flow with IGM 1.0.0 Dispute Resolution

- **Flow ID:** `Delivery_Flow_With_IGM(v-1.0.0)`
- **Config File:** `./HOME&KITCHEN/Delivery_Flow_With_IGM_v-1_0_0_.yaml`
- **Protocol Version:** `1.2.5`
- **Use Case:** `HOME&KITCHEN`
- **Tags:** `PRAMAAN`, `MANDATORY`, `REPORTABLE`, `WORKBENCH`

#### 1. Short Description
Full prepaid homeware delivery lifecycle combined with post-fulfillment dispute redressal under legacy IGM 1.0.0 architecture.

#### 2. API Breakdown & Technical Actions
- **Steps 1–12 (`/select` to `on_status_order_delivered`)**: Complete forward fulfillment from cart checkout to doorstep delivery.
- **Step 13: `/issue (issue_open_100)` (BAP -> BPP)**: Buyer lodges a grievance under IGM 1.0.0 (e.g., missing pot lid).
- **Step 14: `/on_issue (on_issue_processing_100)` (BPP -> BAP)**: Seller acknowledges the complaint and assigns a Grievance Officer.
- **Step 15: `on_issue_status (on_issue_resolved_100)` [Unsolicited] (BPP -> BAP)**: Seller issues an unsolicited resolution update detailing remedial action.
- **Step 16: `/issue (issue_close_100)` (BAP -> BPP)**: Customer confirms resolution and closes the grievance ticket.

---

### Flow 17: Delivery Flow with IGM 2.0.0: Evidence Exchange and Return

- **Flow ID:** `Delivery_Flow_With_IGM(v-2.0.0)`
- **Config File:** `./HOME&KITCHEN/Delivery_Flow_With_IGM_v-2_0_0_.yaml`
- **Protocol Version:** `1.2.5`
- **Use Case:** `HOME&KITCHEN`
- **Tags:** `PRAMAAN`, `MANDATORY`, `REPORTABLE`, `WORKBENCH`

#### 1. Short Description
Interactive IGM 2.0.0 workflow. The buyer reports damaged cookware, the seller requests additional diagnostic and unboxing proof, the buyer supplies the evidence, and the seller approves a return and refund.

#### 2. API Breakdown & Technical Actions
- **Steps 1–12 (`/select` to `on_status_order_delivered`)**: Forward delivery lifecycle.
- **Step 13: `/issue (issue_open)` (BAP -> BPP)**: Buyer opens an issue reporting damaged cookware.
- **Step 14: `/on_issue (on_issue_processing)` (BPP -> BAP)**: Initial seller acknowledgment.
- **Step 15: `on_issue (on_issue_need_more_info)` [Unsolicited] (BPP -> BAP)**: Seller requests photos of damaged item and shipping box.
- **Step 16: `/issue (issue_info_provided)` (BAP -> BPP)**: Buyer uploads requested diagnostic evidence URLs.
- **Step 17: `/on_issue (on_issue_provided)` (BPP -> BAP)**: Seller acknowledges receipt of evidence.
- **Step 18: `on_issue (on_issue_resolution)` [Unsolicited] (BPP -> BAP)**: Seller validates defect and proposes return resolution.
- **Step 19: `/issue (issue_resolution_accept)` (BAP -> BPP)**: Buyer accepts resolution.
- **Step 20: `/on_issue (on_issue_resolved)` (BPP -> BAP)**: Seller confirms resolution agreement.
- **Step 21: `/issue (issue_close)` (BAP -> BPP)**: Buyer closes the grievance.
- **Step 22: `on_update (on_update_igm_return)` [Unsolicited] (BPP -> BAP)**: Seller schedules reverse pickup and refund processing.

---

### Flow 18: Delivery Flow with IGM 2.0.0: Resolution Accepted (No Action)

- **Flow ID:** `Delivery_Flow_With_IGM_No_Action(v-2.0.0)`
- **Config File:** `./HOME&KITCHEN/Delivery_Flow_With_IGM_No_Action_v-2_0_0_.yaml`
- **Protocol Version:** `1.2.5`
- **Use Case:** `HOME&KITCHEN`
- **Tags:** `PRAMAAN`, `REPORTABLE`, `WORKBENCH`, `MANDATORY`

#### 1. Short Description
IGM 2.0.0 dispute where the seller investigates a reported homeware issue (e.g., natural rainbow heat tint on stainless steel cookware), determines that the item conforms strictly to material standards, and provides an explanatory `NO_ACTION` resolution that the buyer accepts.

#### 2. API Breakdown & Technical Actions
- **Steps 1–12 (`/select` to `on_status_order_delivered`)**: Standard forward fulfillment lifecycle.
- **Step 13: `/issue (issue_open_2)` (BAP -> BPP)**: Buyer opens a complaint under IGM 2.0.0.
- **Step 14: `/on_issue (on_issue_processing)` (BPP -> BAP)**: Seller acknowledges the issue.
- **Step 15: `on_issue (on_issue_resolution_igm_3)` [Unsolicited] (BPP -> BAP)**: Seller provides an explanatory `NO_ACTION` resolution detailing correct stainless steel care and cleaning.
- **Step 16: `/issue (issue_resolution_accept_igm_3)` (BAP -> BPP)**: Buyer accepts the technical explanation.
- **Step 17: `/on_issue (on_issue_resolved_igm_3)` (BPP -> BAP)**: Seller confirms resolution status.
- **Step 18: `/issue (issue_close_igm_3)` (BAP -> BPP)**: Buyer closes the dispute.
- **Step 19: `on_status (on_status_igm_3)` [Unsolicited] (BPP -> BAP)**: Seller updates the final order audit record.

---

### Flow 19: Delivery Flow with IGM 2.0.0: Rejection, Escalation and Replacement

- **Flow ID:** `Delivery_Flow_With_IGM_Rejection(v-2.0.0)`
- **Config File:** `./HOME&KITCHEN/Delivery_Flow_With_IGM_Rejection_v-2_0_0_.yaml`
- **Protocol Version:** `1.2.5`
- **Use Case:** `HOME&KITCHEN`
- **Tags:** `PRAMAAN`, `MANDATORY`, `REPORTABLE`, `WORKBENCH`

#### 1. Short Description
Dispute escalation flow. The buyer reports shattered ceramic dinnerware upon unboxing, rejects inadequate settlement proposals, escalates the dispute to a Level 2 Grievance Officer, receives an arbitrator ruling in favor of replacement, and the seller dispatches a replacement parcel.

#### 2. API Breakdown & Technical Actions
- **Steps 1–12 (`/select` to `on_status_order_delivered`)**: Forward delivery lifecycle.
- **Step 13: `/issue (issue_open)` (BAP -> BPP)**: Buyer opens dispute for transit damage.
- **Step 14: `/on_issue (on_issue_processing)` (BPP -> BAP)**: Seller acknowledgment.
- **Step 15: `on_issue (on_issue_resolution)` [Unsolicited] (BPP -> BAP)**: Seller proposes nominal cosmetic voucher.
- **Step 16: `/issue (issue_resolution_reject)` (BAP -> BPP)**: Buyer rejects inadequate resolution.
- **Step 17: `/on_issue (on_issue_processing_1)` (BPP -> BAP)**: Seller acknowledges rejection.
- **Step 18: `on_issue (on_issue_resolution_1)` [Unsolicited] (BPP -> BAP)**: Seller offers revised settlement.
- **Step 19: `/issue (issue_escalate)` (BAP -> BPP)**: Buyer escalates dispute to Level 2 Grievance Officer.
- **Step 20: `/on_issue (on_issue_processing_2)` (BPP -> BAP)**: Escalation acknowledged.
- **Step 21: `on_issue (on_issue_resolution_2)` [Unsolicited] (BPP -> BAP)**: Level 2 arbitrator reviews unboxing proof and rules in favor of replacement.
- **Step 22: `/issue (issue_resolution_accept)` (BAP -> BPP)**: Buyer accepts escalated ruling.
- **Step 23: `/on_issue (on_issue_resolved)` (BPP -> BAP)**: Dispute marked resolved.
- **Step 24: `/issue (issue_close)` (BAP -> BPP)**: Dispute officially closed.
- **Step 25: `on_update (on_update_igm_replacement)` [Unsolicited] (BPP -> BAP)**: Seller dispatches replacement unit and schedules reverse pickup of damaged item; `Completed`.

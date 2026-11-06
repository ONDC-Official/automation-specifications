# Retail Health & Wellness (ONDC:RET18 1.2.0)

- [Overview](#overview)
- [Participants](#participants)
- [The User Journey](#the-user-journey)
  - [1. Discovery and Catalog Search](#1-discovery-and-catalog-search)
  - [2. Form Factor, Dosage & Serviceability Check](#2-form-factor-dosage-serviceability-check)
  - [3. Order Initialization and Shipping Configuration](#3-order-initialization-and-shipping-configuration)
  - [4. Order Confirmation and Prepaid Escrow](#4-order-confirmation-and-prepaid-escrow)
  - [5. Order Processing, Picking, and Batch/Expiry Verification](#5-order-processing-picking-and-batchexpiry-verification)
  - [6. Logistics Assignment & Temperature/Cold-Chain Handling](#6-logistics-assignment-temperaturecold-chain-handling)
  - [7. Order Dispatch, In-Flight Tracking, and Secure Delivery](#7-order-dispatch-in-flight-tracking-and-secure-delivery)
  - [8. Settlement and Post-Fulfillment](#8-settlement-and-post-fulfillment)
- [Additional Scenarios](#additional-scenarios)
  - [1. Buyer-Initiated Return and Reverse QC Pickup (Full and Partial Order)](#1-buyer-initiated-return-and-reverse-qc-pickup-full-and-partial-order)
  - [2. Buyer-Side Order Cancellation](#2-buyer-side-order-cancellation)
  - [3. Merchant-Side Part-Cancellation and Return to Origin (RTO)](#3-merchant-side-part-cancellation-and-return-to-origin-rto)
  - [4. Out of Stock and Inventory Exceptions](#4-out-of-stock-and-inventory-exceptions)
  - [5. Incremental Catalog Refresh (Push and Pull)](#5-incremental-catalog-refresh-push-and-pull)
  - [6. Statutory Compliance, Batch & Expiry Tracking, and Schedule K Guidelines](#6-statutory-compliance-batch-expiry-tracking-and-schedule-k-guidelines)
- [Issue and Grievance Management](#issue-and-grievance-management)
  - [1. IGM 1.0.0 Architecture](#1-igm-100-architecture)
  - [2. IGM 2.0.0 Architecture](#2-igm-200-architecture)
- [Detailed Protocol Flows](#detailed-protocol-flows)
  - [Flow 1: Order to Confirm to Fulfillment (Prepaid Standard Delivery)](#flow-1-order-to-confirm-to-fulfillment-prepaid-standard-delivery)
  - [Flow 2: Buyer-Initiated Return (Full Order and Partial Order)](#flow-2-buyer-initiated-return-full-order-and-partial-order)
  - [Flow 3: Buyer-Side Order Cancellation](#flow-3-buyer-side-order-cancellation)
  - [Flow 4: Merchant-Side Part-Order Cancellation and Return to Origin (RTO)](#flow-4-merchant-side-part-order-cancellation-and-return-to-origin-rto)
  - [Flow 5: Out of Stock Error Handling (Inventory Shortage)](#flow-5-out-of-stock-error-handling-inventory-shortage)
  - [Flow 6: Search and Custom Menu: Full Catalog City Discovery](#flow-6-search-and-custom-menu-full-catalog-city-discovery)
  - [Flow 7: Search and Custom Menu: Incremental Catalog Push](#flow-7-search-and-custom-menu-incremental-catalog-push)
  - [Flow 8: Discovery Flow: Incremental Catalog Refresh Pull](#flow-8-discovery-flow-incremental-catalog-refresh-pull)
  - [Flow 9: Order to Confirm with IGM 1.0.0 Resolution](#flow-9-order-to-confirm-with-igm-100-resolution)
  - [Flow 10: Order to Confirm with IGM 2.0.0: Resolution Accepted (No Action)](#flow-10-order-to-confirm-with-igm-200-resolution-accepted-no-action)
  - [Flow 11: Order to Confirm with IGM 2.0.0: Rejection, Escalation and Return](#flow-11-order-to-confirm-with-igm-200-rejection-escalation-and-return)
  - [Flow 12: Order to Confirm with IGM 2.0.0: Evidence Exchange and Item Replacement](#flow-12-order-to-confirm-with-igm-200-evidence-exchange-and-item-replacement)

---

## Overview

The Health & Wellness domain (**ONDC:RET18**, specification version **1.2.0**) establishes an open, standardized digital commerce framework for the procurement, fulfillment, and return of Over-The-Counter (OTC) healthcare items, dietary supplements, sports nutrition, ayurvedic remedies, personal hygiene essentials, and domestic medical devices across the Open Network for Digital Commerce (ONDC).

Historically, the healthcare and wellness retail landscape in India has been divided between neighborhood community pharmacies, specialized sports nutrition outlets, ayurvedic dispensaries, and centralized direct-to-consumer (D2C) e-commerce platforms. This fragmentation has created substantial barriers for consumers seeking rapid, hyperlocal delivery of urgent wellness necessities (such as fever relief syrups, electrolyte solutions, antiseptic dressings, or blood glucose monitor strips) while limiting local pharmacies and licensed supplement distributors from participating in network-wide digital commerce.

**ONDC:RET18** standardizes health and wellness retail by decoupling buyer-facing discovery from seller fulfillment:
- **Consumer Empowerment**: Buyers can search for wellness merchandise across all connected pharmacies, specialized nutrition stores, and healthcare brands within their city using any compliant **Buyer Application (BAP)**.
- **Merchant Inclusion**: Licensed pharmacies, wellness dispensaries, and supplement manufacturers can broadcast their catalogs, real-time inventory, batch identifiers, and pricing through a **Seller Application (BPP)** without developing proprietary digital shopping applications.
- **Logistics Integration**: Certified **Logistics Service Providers (LSPs)** execute delicate healthcare transport, offering ambient or temperature-controlled carriage, spill-resistant cushioning, and tamper-evident packaging.
- **Regulatory Rigor**: Protocol compliance ensures strict alignment with statutory mandates, including the Drugs and Cosmetics Act (Schedule K exemptions for OTC formulations), Food Safety and Standards Authority of India (FSSAI) Nutraceutical Regulations (2022), and Legal Metrology (Packaged Commodities) Rules regarding mandatory disclosure of Maximum Retail Price (MRP), net quantity, manufacturing batch numbers, and exact expiration dates.

---

## Participants

The ONDC health and wellness ecosystem operates through four synchronized network roles:

```
+----------------------------------------------------------------------------------------------------+
|                                         ONDC GATEWAY / REGISTRY                                    |
|             (Participant Lookup, Cryptographic Ed25519 Authentication, Broadcast Routing)         |
+----------------------------------------------------------------------------------------------------+
              ^                                                                  ^
              | /search                                                          | /on_search
              v                                                                  v
+-----------------------------+                                    +-----------------------------+
|   BUYER APPLICATION (BAP)   |                                    |   SELLER APPLICATION (BPP)  |
| - Health & Wellness Portals | ======= /select, /init, /confirm =====> | - Retail Pharmacies         |
| - Multi-Category Apps       | <====== /on_select, /on_init, /on_confirm == | - Supplement Distributors   |
| - Chronic Care Platforms    |                                    | - Ayurvedic & Wellness D2Cs |
| - Diagnostic & Wellness Apps| <------ unsolicited on_status / on_update -- | - Medical Device Outlets    |
+-----------------------------+                                    +-----------------------------+
              |                                                                  |
              | Track Live Telemetry (/track)                                    | Assign Courier & Packaging
              v                                                                  v
+----------------------------------------------------------------------------------------------------+
|                                    LOGISTICS SERVICE PROVIDER (LSP)                                |
|        (Ambient/Cold-Chain Handling, Tamper-Evident Courier Transport, Doorstep Handover)          |
+----------------------------------------------------------------------------------------------------+
```

1. **Buyer Application (BAP)**:
   - Provides consumer interfaces for symptom/product search, category browsing (Vitamins, Sports Nutrition, Ayurveda, Medical Devices, First Aid), and dosage/form-factor selection.
   - Transmits structured transaction requests (`/search`, `/select`, `/init`, `/confirm`, `/status`, `/track`, `/cancel`, `/update`, `/issue`).
   - Collects payments from buyers and manages escrow disbursements according to network settlement rules.

2. **Seller Application (BPP)**:
   - Deployed by retail pharmacies, nutraceutical distributors, ayurvedic manufacturers, and medical supply stores.
   - Publishes catalogs with mandatory regulatory tags (batch ID, manufacturing date, expiry date, FSSAI license, net weight, dosage form).
   - Validates inventory in real time, manages warehouse picking, verifies tamper seals, packs delicate health products in tamper-evident outer containers, and coordinates carrier pickup.
   - Emits asynchronous protocol callbacks (`/on_search`, `/on_select`, `/on_init`, `/on_confirm`, `/on_status`, `/on_track`, `/on_cancel`, `/on_update`, `/on_issue`).

3. **Logistics Service Provider (LSP)**:
   - On-demand hyperlocal couriers and express parcel networks integrated with the BPP.
   - Executes ambient, spill-resistant, or temperature-monitored transport for heat-sensitive supplements (e.g. probiotics, softgel capsules) and delicate medical diagnostic kits.
   - Enforces tamper-evident handover, doorstep verification, and reverse logistics inspection for approved returns.

4. **Gateway and Registry**:
   - Maintains verified registry of network participants with their digital cryptographic public keys (`Ed25519`).
   - Multicasts buyer discovery queries to relevant sellers based on geographic serviceability polygons (City/PIN code).

---

## The User Journey

The standard forward fulfillment lifecycle for a Health & Wellness order is structured into eight distinct operational and protocol phases:

```
+---------------------+      +---------------------+      +---------------------+      +---------------------+
| 1. Discovery &      | ---> | 2. Form Factor,     | ---> | 3. Order Init &     | ---> | 4. Order Confirm &  |
|    Catalog Search   |      |    Dosage Check     |      |    Delivery Config  |      |    Escrow Payment   |
+---------------------+      +---------------------+      +---------------------+      +---------------------+
           |                                                                                      |
           v                                                                                      v
+---------------------+      +---------------------+      +---------------------+      +---------------------+
| 5. Warehouse Picking| ---> | 6. Logistics &      | ---> | 7. Dispatch, Live   | ---> | 8. Settlement &     |
|    & Expiry Check   |      |    Courier Assign   |      |    Tracking & Handover|   |    Post-Fulfillment |
+---------------------+      +---------------------+      +---------------------+      +---------------------+
```

### 1. Discovery and Catalog Search
- The consumer enters a search query on the BAP (e.g., "Whey Protein Isolate 1kg", "Vitamin D3 60,000 IU", "Digital Blood Pressure Monitor", "Ayurvedic Giloy Juice").
- The BAP generates a broadcast `/search` request targeting domain `ONDC:RET18` across the buyer's delivery city.
- The ONDC Gateway routes the query to all registered seller nodes serviceable in that geographic zone.
- Each BPP responds asynchronously with `/on_search`, returning catalog hierarchies, item descriptions, therapeutic categories, form factors (tablets, capsules, powder, liquid, ointment), MRP, sale prices, and statutory compliance tags.

### 2. Form Factor, Dosage & Serviceability Check
- The consumer selects the exact item variant (e.g., Chocolate Flavour 1kg Tub, Pack of 60 Capsules, Sterile Bandage Box of 100) and specifies the delivery location.
- The BAP fires `/select` containing item identifiers, quantities, and destination GPS coordinates.
- The BPP performs real-time stock validation against pharmacy/warehouse inventory, evaluates delivery polygon serviceability, verifies that remaining shelf life exceeds mandatory threshold limits, and responds with `/on_select`.
- The response returns an itemized commercial quotation (`quote.breakup[]`), including base product price, applicable GST, logistics fee, packaging charges, and estimated delivery turnaround time.

### 3. Order Initialization and Shipping Configuration
- The consumer proceeds to checkout, supplying the patient/recipient name, contact number, delivery address, and billing information.
- The BAP sends `/init` to the BPP with buyer identity, delivery coordinates, and chosen fulfillment type.
- The BPP validates the shipping parameters, reserves the requested inventory for a defined reservation window, locks in tax and freight calculations, and returns `/on_init`.
- The callback details exact payment parameters, merchant escrow credentials, settlement windows, and cancellation policy terms.

### 4. Order Confirmation and Prepaid Escrow
- The consumer completes payment on the BAP via UPI, credit/debit card, or net banking into the BAP's escrow account.
- The BAP issues `/confirm` with `order.state = "Created"`, embedding payment confirmation, authorization transaction ID, and buyer billing metadata.
- The BPP validates the payment token, registers the order in its Pharmacy Management System (PMS) / Warehouse Management System (WMS), creates a firm commercial contract, and responds with `/on_confirm`.
- `/on_confirm` acknowledges the order, returns a permanent network `order.id`, confirms `order.state = "Created"`, and initializes fulfillment state to `Pending`.

### 5. Order Processing, Picking, and Batch/Expiry Verification
- The pharmacy or warehouse team initiates order processing. Pharmacists inspect the physical packaging, verify that tamper-evident seals are unbroken, confirm that the batch number corresponds to verified inventory, and ensure that the expiration date has at least 6 months of remaining shelf life.
- The seller emits an unsolicited `on_status (on_status_pending)`, updating `order.state` to `Accepted`.
- Items are packaged in tamper-evident, opaque, padded envelopes or corrugated boxes with bubble wrap to safeguard glass bottles and prevent transit leaks.
- Once packed, the BPP emits an unsolicited `on_status (on_status_packed)`, advancing `fulfillment.state` to `Packed` and `order.state` to `In-progress`.

### 6. Logistics Assignment & Temperature/Cold-Chain Handling
- The BPP assigns a dedicated delivery rider through its logistics partner, ensuring handling requirements (such as "Keep away from direct sunlight and heat" or "Fragile liquid container") are communicated to the courier.
- The BPP transmits an unsolicited `on_status (on_status_agent_assigned)`, advancing `fulfillment.state` to `Agent-assigned` and providing the courier agent's name and contact phone number.
- The delivery rider arrives at the dispensing facility, verifies the parcel's barcode, and assumes custody.
- The BPP emits an unsolicited `on_status (on_status_picked)`, transitioning `fulfillment.state` to `Order-picked-up`.

### 7. Order Dispatch, In-Flight Tracking, and Secure Delivery
- The buyer monitors the dispatch in real time. The BAP can invoke `/track`, and the BPP responds with `/on_track` providing real-time GPS coordinates and a web tracking URL.
- When the delivery rider approaches the delivery address, the BPP fires an unsolicited `on_status (on_status_out_for_delivery)`, updating `fulfillment.state` to `Out-for-delivery`.
- The courier completes doorstep delivery, verifying the recipient.
- The BPP emits an unsolicited `on_status (on_status_order_delivered)`, finalizing `fulfillment.state` to `Order-delivered` and `order.state` to `Completed`.

### 8. Settlement and Post-Fulfillment
- Doorstep delivery opens the customer verification and return window.
- The BAP updates the settlement trail via `/update (update_settlement_trail)`, confirming the final fulfillment state and authorized payment allocations.
- If no dispute or return is lodged within the return window, the escrow bank settles payment, deducting network convenience fees and transferring net proceeds to the seller and logistics partner.

---

## Additional Scenarios

In addition to standard forward fulfillment, **ONDC:RET18 1.2.0** defines rigorous handling procedures for returns, cancellations, out-of-stock recovery, catalog synchronization, and healthcare compliance:

### 1. Buyer-Initiated Return and Reverse QC Pickup (Full and Partial Order)
- Due to patient safety, contamination risks, and regulatory standards, returns in Health & Wellness are strictly governed by transparent return policies. Returns are eligible only for defective medical equipment, broken/leaking containers, incorrect items dispatched, or expired batches.
- **Partial Return Capability**: The buyer can return a single item from a multi-item health order (e.g., returning an inaccurate pulse oximeter while keeping sealed nutritional supplements) or return the complete order.
- **Protocol Flow**:
  1. The buyer submits a return request via `/update (update_return)` specifying item IDs, return quantity, and reason code.
  2. The BPP evaluates the claim and responds with `/on_update (on_update_return_init)`.
  3. The seller approves the return via `on_update (on_update_return_approved)`.
  4. A reverse courier is assigned to inspect the product at the buyer's doorstep (checking that tamper-evident seals are intact and serial/batch numbers match).
  5. Upon pickup, the seller emits `on_update (on_update_return_picked)`.
  6. The BAP updates the settlement trail via `/update (update_settlement_trail)` to calculate refund obligations.
  7. Upon warehouse receipt and final verification, the seller emits `on_update (on_update_return_delivered)`, executing the automated buyer refund.

### 2. Buyer-Side Order Cancellation
- The buyer may cancel an order prior to courier handover (pre-dispatch) if they placed an accidental order or changed their treatment requirement.
- The BAP sends `/cancel` specifying the cancellation reason code.
- The BPP validates that the order is still prior to the `Order-picked-up` fulfillment stage, terminates the warehouse dispatch process, and responds with `/on_cancel`.
- The order state transitions to `Cancelled`, and a full 100% refund is initiated back to the buyer's original payment method without penalty.

### 3. Merchant-Side Part-Cancellation and Return to Origin (RTO)
- **Part-Order Cancellation**: During physical picking, a pharmacist may discover that one requested item has an expired batch or damaged tamper seal with no replacement stock available.
  - The BPP emits `on_update (on_update_part_cancel)`, cancelling only the unavailable line item, reducing the total quote, and preserving the remainder of the order.
  - The BAP acknowledges the revised quote and updates settlement allocations via `/update (update_settlement_trail)`.
  - The remaining healthy items proceed through standard packaging, pickup, and delivery.
- **Return to Origin (RTO)**: When an dispatched order cannot be delivered due to buyer unavailability, incorrect address, or unresponsiveness:
  - After delivery failure, the courier initiates RTO.
  - The BPP emits `on_cancel (on_cancel_rto)`, marking the forward fulfillment as terminated and initiating reverse transit.
  - The BAP updates settlement records via `/update (update_settlement_trail_1)`.
  - Once the returned package is received back at the dispensing pharmacy, the BPP fires `on_status (on_status_rto_delivered)`, triggering a refund to the buyer minus legitimate two-way logistics costs.

### 4. Out of Stock and Inventory Exceptions
- When a buyer attempts to select a health product that has just been depleted from physical inventory:
  - The BAP sends `/select (select0)` requesting the desired quantity.
  - The BPP immediately detects inventory exhaustion and responds with `/on_select (on_select_out_of_stock)` embedding standard ONDC protocol error codes (`40002` or `30009` - Item Out of Stock).
  - The error payload includes clear error descriptors, preventing invalid checkout progression and allowing the BAP to inform the customer and suggest therapeutic alternatives.

### 5. Incremental Catalog Refresh (Push and Pull)
- **Incremental Push (`Search_and_Custom_Menu_(Incremental_Push)`)**:
  - Healthcare sellers frequently update stock levels, batch details, and operating hours.
  - Sellers push incremental updates directly using `on_search` without waiting for a buyer query.
  - Furthermore, sellers can broadcast emergency operational closures (e.g. pharmacy closing for scheduled sanitation or national holiday) using `on_search` with `bpp/providers[].items[].tags` indicating closure.
- **Incremental Refresh Pull (`Discovery_Flow_incremental_catalog_refresh_pull`)**:
  - Buyer applications query sellers for catalog changes that occurred after a specific timestamp.
  - BAP sends `/search` containing `tags[refresh]` with a `timestamp` parameter.
  - BPP responds with `/on_search` returning solely modified, newly added, or out-of-stock items, conserving network bandwidth and keeping consumer apps up to date.

### 6. Statutory Compliance, Batch & Expiry Tracking, and Schedule K Guidelines
- **Drugs and Cosmetics Act & Schedule K**: Non-prescription OTC health products sold under `ONDC:RET18` must strictly qualify for Schedule K exemptions. Standard retail flows do not process Schedule H/H1/X prescription drugs.
- **Mandatory Batch & Expiry Tagging**: Every packaged medicine, supplement, and diagnostic reagent must include:
  - Manufacturing Batch ID (`batch_id`)
  - Date of Manufacture (`mfg_date`)
  - Date of Expiry / Best Before (`expiry_date`)
  - Sellers are strictly prohibited from dispatching items within 30 days of expiration unless explicitly branded as short-expiry clearance with full buyer consent.
- **FSSAI Nutraceutical Regulations**: Dietary supplements, protein powders, and herbal formulations must publish valid FSSAI registration numbers, nutritional facts panels, allergen declarations, and non-medicinal use disclaimers.
- **Legal Metrology Declarations**: Complete transparency regarding Maximum Retail Price (MRP), Net Quantity, Country of Origin, Manufacturer Name, and Consumer Care Contact Details.

---

## Issue and Grievance Management

The health and wellness domain supports both **IGM 1.0.0** and **IGM 2.0.0** architectures to resolve customer disputes, damaged items, incorrect dosages, and missing products.

### 1. IGM 1.0.0 Architecture
- A linear grievance resolution framework.
- The buyer opens a ticket via `/issue` (`issue_open_100`) specifying grievance category, item ID, and issue description (e.g., shattered syrup bottle or missing blister strip).
- The BPP acknowledges the ticket via `/on_issue` (`on_issue_processing_100`), transitioning status to `PROCESSING`.
- The merchant reviews warehouse CCTV and packing logs, formulates a resolution (such as a full refund), and sends `/on_issue_status` (`on_issue_resolved_100`) marking status as `RESOLVED`.
- The buyer verifies the resolution and closes the issue via `/issue` (`issue_close_100`).

### 2. IGM 2.0.0 Architecture
- An interactive, multi-party dispute resolution standard providing bidirectional evidence sharing, interim status codes, and grievance escalation.
- **Core Real-World Scenarios in RET18**:
  1. **Evidence Exchange & Product Replacement (`Order_to_confirm_to_fulfillment__Prepaid_with_IGM_v-2.0.0`)**:
     - Buyer reports a defective digital blood pressure monitor displaying calibration errors.
     - The seller issues an unsolicited `on_issue` (`on_issue_need_more_info`), requesting an image or video demonstration of the display error.
     - The buyer submits verification media URLs via `/issue` (`issue_info_provided`).
     - The seller validates the defect, issues `on_issue (on_issue_resolution)` proposing an item `REPLACEMENT`, and upon buyer acceptance, dispatches a brand-new replacement unit via unsolicited `on_update` (`on_update_igm_replacement`).
  2. **Resolution Accepted with Explanatory No-Action (`Order_to_confirm_to_fulfillment__Prepaid_with_IGM_No_Action_v-2.0.0`)**:
     - Buyer submits a complaint that an organic ayurvedic juice has natural herbal sediment at the bottom of the bottle.
     - The merchant's medical team examines batch retain samples and issues an explanatory resolution clarifying that sediment is natural for unrefined herbal extracts and does not indicate spoilage.
     - The buyer accepts the clarification without requiring a refund or replacement, and the ticket closes cleanly with status `RESOLVED` (`NO_ACTION`).
  3. **Dispute Rejection, Escalation, and Overturned Return (`Order_to_confirm_to_fulfillment__Prepaid_with_IGM_Rejection_v-2.0.0`)**:
     - Buyer reports receiving a crushed supplement container.
     - The seller initially rejects the claim asserting outer packaging was intact upon dispatch.
     - The buyer rejects the resolution (`issue_resolution_reject`) and escalates to a network Grievance Officer / Ombudsman (`issue_escalate`).
     - The mediator reviews unboxing photos and courier delivery transit logs, ruling in favor of the consumer.
     - The seller complies with the escalated ruling, issues a full return resolution, and executes reverse pickup and refund via unsolicited `on_update` (`on_update_igm_return`).

---

## Detailed Protocol Flows

All **12 protocol flows** defined in `automation-specifications/config/flows/index.yaml` for the Health & Wellness domain (`ONDC:RET18 1.2.0`) are detailed below with their classification tags, operational contexts, and full step-by-step API message sequences.

---

### Flow 1: Order to Confirm to Fulfillment (Prepaid Standard Delivery)

- **Flow ID:** `Order_to_confirm_to_fulfillment_(Prepaid)`
- **Config File:** `./HEALTH&WELLNESS/Order_to_confirm_to_fulfillment__Prepaid_.yaml`
- **Protocol Version:** `1.2.0`
- **Use Case:** `HEALTH&WELLNESS`
- **Tags:** `WORKBENCH`, `PRAMAAN`, `MANDATORY`, `REPORTABLE`

#### 1. Short Description
The canonical end-to-end forward fulfillment journey for health and wellness products. Covers item selection, dosage and availability verification, order initialization, prepaid payment capture, pharmacy warehouse picking with batch verification, multi-stage courier status updates, live GPS tracking, and secure doorstep delivery completion.

#### 2. API Breakdown & Technical Actions
- **Step 1: `/select (select)` (BAP -> BPP)**: The BAP selects specific healthcare items, dosage variants, and quantities from the seller's catalog, specifying delivery destination coordinates.
- **Step 2: `/on_select (on_select)` (BPP -> BAP)**: The seller confirms product availability, returns an itemized price breakdown (`quote.breakup[]`), confirms fulfillment serviceability (`Fulfillment: Serviceable`), and quotes delivery turnaround time.
- **Step 3: `/init (init)` (BAP -> BPP)**: The BAP transmits patient/recipient details, billing address, exact delivery location, and prepaid payment preference to initiate the order draft.
- **Step 4: `/on_init (on_init)` (BPP -> BAP)**: The seller responds with frozen commercial terms, payment parameters, cancellation windows, and settlement rules.
- **Step 5: `/confirm (confirm)` (BAP -> BPP)**: The BAP captures prepaid digital payment and submits the confirmed order with `order.state = "Created"`.
- **Step 6: `/on_confirm (on_confirm)` (BPP -> BAP)**: The seller validates payment, records the order in PMS/WMS, confirms `order.state = "Created"`, and sets initial fulfillment state to `Pending`.
- **Step 7: `on_status (on_status_pending)` [Unsolicited] (BPP -> BAP)**: The pharmacy confirms order processing and batch allocation; `order.state` transitions to `Accepted`.
- **Step 8: `on_status (on_status_packed)` [Unsolicited] (BPP -> BAP)**: The healthcare products are picked, inspected for unbroken tamper seals, and packed in secure tamper-evident packaging; `fulfillment.state` updates to `Packed` and `order.state` to `In-progress`.
- **Step 9: `on_status (on_status_agent_assigned)` [Unsolicited] (BPP -> BAP)**: A delivery courier is assigned; `fulfillment.state` advances to `Agent-assigned`.
- **Step 10: `on_status (on_status_picked)` [Unsolicited] (BPP -> BAP)**: The courier picks up the package from the dispensing pharmacy; `fulfillment.state` updates to `Order-picked-up`.
- **Step 11: `/track (track)` (BAP -> BPP)**: The BAP queries live in-transit location telemetry.
- **Step 12: `/on_track (on_track)` (BPP -> BAP)**: The BPP returns real-time GPS coordinates and an active web tracking link.
- **Step 13: `on_status (on_status_out_for_delivery)` [Unsolicited] (BPP -> BAP)**: The courier arrives in the delivery sector; `fulfillment.state` transitions to `Out-for-delivery`.
- **Step 14: `on_status (on_status_order_delivered)` [Unsolicited] (BPP -> BAP)**: Secure doorstep handover is completed and the customer receives the parcel; `fulfillment.state` reaches `Order-delivered` and `order.state` transitions to `Completed`.

---

### Flow 2: Buyer-Initiated Return (Full Order and Partial Order)

- **Flow ID:** `Buyer_Initiated_Return_(Full_Order_and_Partial_Order)`
- **Config File:** `./HEALTH&WELLNESS/Buyer_Initiated_Return__Full_Order_and_Partial_Order_.yaml`
- **Protocol Version:** `1.2.0`
- **Use Case:** `HEALTH&WELLNESS`
- **Tags:** `WORKBENCH`, `PRAMAAN`, `MANDATORY`, `REPORTABLE`

#### 1. Short Description
Exercises the complete post-delivery return lifecycle for health and wellness products (covering both full-order and partial-item returns). Includes return request authorization, doorstep reverse logistics collection with condition inspection, settlement trail coordination, and final warehouse verification and refund closure.

#### 2. API Breakdown & Technical Actions
- **Steps 1–6 (`/select` to `/on_confirm`)**: Standard prepaid order creation and payment confirmation.
- **Steps 7–12 (`on_status` sequence)**: Progressive fulfillment from `Accepted`, `Packed`, `Agent-assigned`, `Order-picked-up`, `Out-for-delivery`, to `Order-delivered`.
- **Step 13: `/update (update_return)` (BAP -> BPP)**: The buyer initiates a return request specifying the return reason (e.g. damaged container or defective unit) and item IDs for full or partial return.
- **Step 14: `/on_update (on_update_return_init)` (BPP -> BAP)**: The seller acknowledges the return request, updates fulfillment status, and generates reverse logistics tracking identifiers.
- **Step 15: `on_update (on_update_return_approved)` [Unsolicited] (BPP -> BAP)**: The seller approves the return request after validating eligibility against healthcare return policies.
- **Step 16: `on_update (on_update_return_picked)` [Unsolicited] (BPP -> BAP)**: The reverse courier completes doorstep physical verification (seal check) and picks up the return package.
- **Step 17: `/update (update_settlement_trail)` (BAP -> BPP)**: The BAP updates the settlement trail with adjusted payment allocations and refund obligations.
- **Step 18: `on_update (on_update_return_delivered)` [Unsolicited] (BPP -> BAP)**: The return shipment is delivered to the merchant facility, final inspection passes, and the refund is finalized.

---

### Flow 3: Buyer-Side Order Cancellation

- **Flow ID:** `Buyer_Side_Order_Cancellation`
- **Config File:** `./HEALTH&WELLNESS/Buyer_Side_Order_Cancellation.yaml`
- **Protocol Version:** `1.2.0`
- **Use Case:** `HEALTH&WELLNESS`
- **Tags:** `WORKBENCH`, `PRAMAAN`, `MANDATORY`, `REPORTABLE`

#### 1. Short Description
Demonstrates a pre-dispatch order cancellation initiated by the consumer prior to pharmacy dispatch. Validates immediate cancellation processing, inventory release, and automated payment refund without penalty.

#### 2. API Breakdown & Technical Actions
- **Steps 1–6 (`/select` to `/on_confirm`)**: Standard prepaid order discovery, initialization, and confirmation.
- **Step 7: `/cancel (cancel)` (BAP -> BPP)**: The buyer submits an order cancellation request citing a valid cancellation reason code (e.g., accidental order or delivery window too late).
- **Step 8: `/on_cancel (on_cancel)` (BPP -> BAP)**: The seller confirms cancellation, terminates warehouse processing, marks `order.state = "Cancelled"`, and triggers a full refund.

---

### Flow 4: Merchant-Side Part-Order Cancellation and Return to Origin (RTO)

- **Flow ID:** `Merchant_Side_RTO_and_Part_Order_Cancellation_Flow`
- **Config File:** `./HEALTH&WELLNESS/Merchant_Side_RTO_and_Part_Order_Cancellation_Flow.yaml`
- **Protocol Version:** `1.2.0`
- **Use Case:** `HEALTH&WELLNESS`
- **Tags:** `WORKBENCH`, `PRAMAAN`, `MANDATORY`, `REPORTABLE`

#### 1. Short Description
Demonstrates dual edge-case scenarios: (1) merchant part-order cancellation during warehouse picking due to damaged/expired batch inventory, and (2) delivery failure leading to Return to Origin (RTO) and reverse freight settlement.

#### 2. API Breakdown & Technical Actions
- **Steps 1–6 (`/select` to `/on_confirm`)**: Standard prepaid order flow for a multi-item health order.
- **Step 7: `on_update (on_update_part_cancel)` [Unsolicited] (BPP -> BAP)**: The merchant cancels an unavailable or expired item during warehouse picking, recalculating the commercial quote.
- **Step 8: `/update (update_settlement_trail)` (BAP -> BPP)**: The BAP updates the settlement trail with refund adjustments for the cancelled item.
- **Steps 9–13 (`on_status` sequence)**: The remaining active item progresses through `Accepted`, `Packed`, `Agent-assigned`, `Order-picked-up`, and reaches `Out-for-delivery`.
- **Step 14: `on_cancel (on_cancel_rto)` [Unsolicited] (BPP -> BAP)**: Delivery fails at the customer doorstep (e.g. customer unreachable); the courier initiates RTO.
- **Step 15: `/update (update_settlement_trail_1)` (BAP -> BPP)**: The BAP updates settlement records to account for legitimate two-way logistics costs.
- **Step 16: `on_status (on_status_rto_delivered)` [Unsolicited] (BPP -> BAP)**: The courier returns the package to the merchant warehouse, finalizing the RTO lifecycle.

---

### Flow 5: Out of Stock Error Handling (Inventory Shortage)

- **Flow ID:** `Out_of_Stock(Error_code)`
- **Config File:** `./HEALTH&WELLNESS/Out_of_Stock_Error_code_.yaml`
- **Protocol Version:** `1.2.0`
- **Use Case:** `HEALTH&WELLNESS`
- **Tags:** `WORKBENCH`, `PRAMAAN`, `MANDATORY`, `REPORTABLE`

#### 1. Short Description
Validates the seller's ability to communicate immediate inventory depletion and protocol error reporting when a requested health product is unavailable.

#### 2. API Breakdown & Technical Actions
- **Step 1: `/select (select0)` (BAP -> BPP)**: The BAP attempts to select a healthcare item and quantity from the seller's catalog.
- **Step 2: `/on_select (on_select_out_of_stock)` (BPP -> BAP)**: The seller identifies stock exhaustion and responds with protocol error codes (`40002` / `30009`), communicating inventory unavailability.

---

### Flow 6: Search and Custom Menu: Full Catalog City Discovery

- **Flow ID:** `Search_and_Custom_Menu_(Full_Catalog_City)`
- **Config File:** `./HEALTH&WELLNESS/Search_and_Custom_Menu__Full_Catalog_City_.yaml`
- **Protocol Version:** `1.2.0`
- **Use Case:** `HEALTH&WELLNESS`
- **Tags:** `WORKBENCH`, `PRAMAAN`, `MANDATORY`, `REPORTABLE`

#### 1. Short Description
Demonstrates broad product discovery where a buyer searches for available health and wellness offerings within an entire city, receiving complete categorized catalogs from participating pharmacies and wellness stores.

#### 2. API Breakdown & Technical Actions
- **Step 1: `/search (search_1)` (BAP -> Gateway/BPP)**: The BAP issues a city-wide broadcast search specifying domain `ONDC:RET18` and delivery city code.
- **Step 2: `/on_search (on_search1)` (BPP -> BAP)**: The seller responds with its complete catalog, including therapeutic categories, dosage forms, pricing, and fulfillment capabilities.

---

### Flow 7: Search and Custom Menu: Incremental Catalog Push

- **Flow ID:** `Search_and_Custom_Menu_(Incremental_Push)`
- **Config File:** `./HEALTH&WELLNESS/Search_and_Custom_Menu__Incremental_Push_.yaml`
- **Protocol Version:** `1.2.0`
- **Use Case:** `HEALTH&WELLNESS`
- **Tags:** `WORKBENCH`, `PRAMAAN`, `MANDATORY`, `REPORTABLE`

#### 1. Short Description
Exercises progressive catalog delivery and merchant store status broadcasting. Simulates sellers pushing real-time inventory updates and temporary operational closures (e.g. branch disinfection or stock audit) directly to buyer applications.

#### 2. API Breakdown & Technical Actions
- **Step 1: `/search (search_inc)` (BAP -> BPP)**: Initial query establishing discovery context.
- **Step 2: `/on_search (on_search_inc)` (BPP -> BAP)**: The seller responds with incremental catalog updates.
- **Step 3: `on_search (on_search_inc_close)` [Unsolicited] (BPP -> BAP)**: The seller pushes an unsolicited store status update signaling temporary branch closure or service suspension.
- **Step 4: `/search (search_inc1)` (BAP -> BPP)**: Follow-up query confirming modified catalog and operational status.

---

### Flow 8: Discovery Flow: Incremental Catalog Refresh Pull

- **Flow ID:** `Discovery_Flow_incremental_catalog_refresh_pull`
- **Config File:** `./HEALTH&WELLNESS/Discovery_Flow_incremental_catalog_refresh_pull.yaml`
- **Protocol Version:** `1.2.0`
- **Use Case:** `HEALTH&WELLNESS`
- **Tags:** `WORKBENCH`

#### 1. Short Description
Enables buyer applications to periodically pull modified, newly listed, or out-of-stock items using timestamped delta queries, minimizing network bandwidth and ensuring real-time inventory precision.

#### 2. API Breakdown & Technical Actions
- **Step 1: `/search (search)` (BAP -> BPP)**: Baseline search query for initial catalog synchronization.
- **Step 2: `/on_search (on_search)` (BPP -> BAP)**: The seller returns initial catalog items.
- **Step 3: `/search (search_inc_pull)` (BAP -> BPP)**: The BAP sends a targeted differential search with `tags[refresh]` containing a timestamp parameter.
- **Step 4: `/on_search (on_search_inc_pull)` (BPP -> BAP)**: The seller returns only items modified or updated after the specified timestamp.

---

### Flow 9: Order to Confirm with IGM 1.0.0 Resolution

- **Flow ID:** `Order_to_confirm_to_fulfillment__Prepaid_with_igm_1.0.0`
- **Config File:** `./HEALTH&WELLNESS/Order_to_confirm_to_fulfillment__Prepaid_with_igm_1.0.0.yaml`
- **Protocol Version:** `1.2.0`
- **Use Case:** `HEALTH&WELLNESS`
- **Tags:** `WORKBENCH`, `MANDATORY`

#### 1. Short Description
Covers standard forward fulfillment followed by an IGM 1.0.0 issue resolution lifecycle. The buyer reports an issue with delivered healthcare items (e.g. damaged seal or wrong pack size), and the merchant investigates and resolves the dispute through linear status updates.

#### 2. API Breakdown & Technical Actions
- **Steps 1–6 (`/select` to `/on_confirm`)**: Standard prepaid order placement and confirmation.
- **Steps 7–10 (`on_status` sequence)**: Progressive fulfillment from `Accepted` to `Order-picked-up`.
- **Steps 11–12 (`/track` and `/on_track`)**: Live transit tracking query and telemetry callback.
- **Steps 13–14 (`on_status` sequence)**: Delivery transit to `Out-for-delivery` and final `Order-delivered`.
- **Step 15: `/issue (issue_open_100)` (BAP -> BPP)**: The buyer opens a support ticket detailing product discrepancies or damaged goods.
- **Step 16: `/on_issue (on_issue_processing_100)` (BPP -> BAP)**: The merchant acknowledges the ticket and marks status as `PROCESSING`.
- **Step 17: `/on_issue_status (on_issue_resolved_100)` (BPP -> BAP)**: The merchant completes the investigation and provides a resolution (e.g. refund approved), marking status as `RESOLVED`.
- **Step 18: `/issue (issue_close_100)` (BAP -> BPP)**: The buyer accepts the resolution and marks the issue as `CLOSED`.

---

### Flow 10: Order to Confirm with IGM 2.0.0: Resolution Accepted (No Action)

- **Flow ID:** `Order_to_confirm_to_fulfillment__Prepaid_with_IGM_No_Action_v-2.0.0`
- **Config File:** `./HEALTH&WELLNESS/Order_to_confirm_to_fulfillment__Prepaid_with_IGM_No_Action_v-2.0.0.yaml`
- **Protocol Version:** `1.2.0`
- **Use Case:** `HEALTH&WELLNESS`
- **Tags:** `WORKBENCH`, `MANDATORY`

#### 1. Short Description
Demonstrates an IGM 2.0.0 grievance where a buyer inquires about a perceived issue (e.g. herbal sediment in natural juice or packaging rebranding). The merchant's medical team provides technical clarification, the buyer accepts the explanation, and the ticket is resolved with a `NO_ACTION` disposition.

#### 2. API Breakdown & Technical Actions
- **Steps 1–6 (`/select` to `/on_confirm`)**: Standard prepaid order flow.
- **Steps 7–10 (`on_status` sequence)**: Warehouse processing and carrier pickup.
- **Steps 11–12 (`/track` and `/on_track`)**: Active route tracking.
- **Steps 13–14 (`on_status` sequence)**: Out-for-delivery and final delivery completion.
- **Step 15: `/issue (issue_open_2)` (BAP -> BPP)**: Buyer files an IGM 2.0.0 complaint regarding product appearance or formulation.
- **Step 16: `/on_issue (on_issue_processing)` (BPP -> BAP)**: Seller acknowledges the complaint with `PROCESSING` status.
- **Step 17: `on_issue (on_issue_resolution_igm_3)` [Unsolicited] (BPP -> BAP)**: Seller provides an explanatory resolution clarifying manufacturer formulation standards (`NO_ACTION`).
- **Step 18: `/issue (issue_resolution_accept_igm_3)` (BAP -> BPP)**: Buyer reviews and accepts the technical explanation.
- **Step 19: `on_issue (on_issue_resolved_igm_3)` [Unsolicited] (BPP -> BAP)**: Seller marks the issue status as `RESOLVED`.
- **Step 20: `/issue (issue_close_igm_3)` (BAP -> BPP)**: Buyer confirms final closure of the ticket.
- **Step 21: `on_status (on_status_igm_3)` [Unsolicited] (BPP -> BAP)**: Seller confirms the final order state remains `Completed`.

---

### Flow 11: Order to Confirm with IGM 2.0.0: Rejection, Escalation and Return

- **Flow ID:** `Order_to_confirm_to_fulfillment__Prepaid_with_IGM_Rejection_v-2.0.0`
- **Config File:** `./HEALTH&WELLNESS/Order_to_confirm_to_fulfillment__Prepaid_with_IGM_Rejection_v-2.0.0.yaml`
- **Protocol Version:** `1.2.0`
- **Use Case:** `HEALTH&WELLNESS`
- **Tags:** `WORKBENCH`, `MANDATORY`

#### 1. Short Description
Demonstrates an escalated dispute lifecycle under IGM 2.0.0. The seller initially rejects a buyer's claim regarding transit damage. The buyer escalates to a network Grievance Officer / Ombudsman, who overturns the seller's rejection, ordering a return and refund.

#### 2. API Breakdown & Technical Actions
- **Steps 1–6 (`/select` to `/on_confirm`)**: Standard prepaid order flow.
- **Steps 7–10 (`on_status` sequence)**: Warehouse processing and carrier pickup.
- **Steps 11–12 (`/track` and `/on_track`)**: Live transit tracking query and callback.
- **Steps 13–14 (`on_status` sequence)**: Out-for-delivery and final delivery completion.
- **Step 15: `/issue (issue_open)` (BAP -> BPP)**: Buyer opens an IGM 2.0.0 dispute reporting damaged health supplies.
- **Step 16: `/on_issue (on_issue_processing)` (BPP -> BAP)**: Seller acknowledges the issue (`PROCESSING`).
- **Step 17: `on_issue (on_issue_resolution)` [Unsolicited] (BPP -> BAP)**: Seller rejects the complaint asserting dispatch was intact.
- **Step 18: `/issue (issue_resolution_reject)` (BAP -> BPP)**: Buyer rejects the seller's refusal.
- **Step 19: `on_issue (on_issue_processing_1)` [Unsolicited] (BPP -> BAP)**: Seller re-evaluates the complaint under second-level review.
- **Step 20: `on_issue (on_issue_resolution_1)` [Unsolicited] (BPP -> BAP)**: Seller reiterates rejection.
- **Step 21: `/issue (issue_escalate)` (BAP -> BPP)**: Buyer escalates the grievance to a network Grievance Officer / Ombudsman.
- **Step 22: `on_issue (on_issue_processing_2)` [Unsolicited] (BPP -> BAP)**: The ombudsman assumes jurisdiction and reviews transit logs and packaging photos.
- **Step 23: `on_issue (on_issue_resolution_2)` [Unsolicited] (BPP -> BAP)**: Ombudsman overturns the merchant rejection, ruling in favor of the consumer and ordering a return and refund.
- **Step 24: `/issue (issue_resolution_accept)` (BAP -> BPP)**: Buyer accepts the escalated binding ruling.
- **Step 25: `on_issue (on_issue_resolved)` [Unsolicited] (BPP -> BAP)**: The grievance is marked as `RESOLVED`.
- **Step 26: `/issue (issue_close)` (BAP -> BPP)**: The ticket is formally closed.
- **Step 27: `on_update (on_update_igm_return)` [Unsolicited] (BPP -> BAP)**: Seller executes reverse courier pickup and automated refund settlement.

---

### Flow 12: Order to Confirm with IGM 2.0.0: Evidence Exchange and Item Replacement

- **Flow ID:** `Order_to_confirm_to_fulfillment__Prepaid_with_IGM_v-2.0.0`
- **Config File:** `./HEALTH&WELLNESS/Order_to_confirm_to_fulfillment__Prepaid_with_IGM_v-2.0.0.yaml`
- **Protocol Version:** `1.2.0`
- **Use Case:** `HEALTH&WELLNESS`
- **Tags:** `WORKBENCH`, `MANDATORY`

#### 1. Short Description
Demonstrates collaborative evidence exchange under IGM 2.0.0. The seller requests additional verification regarding a defective medical device, the buyer provides photo/video evidence, and the seller approves an item replacement, initiating dispatch of a new replacement unit.

#### 2. API Breakdown & Technical Actions
- **Steps 1–6 (`/select` to `/on_confirm`)**: Standard prepaid order flow.
- **Steps 7–10 (`on_status` sequence)**: Warehouse processing and carrier pickup.
- **Steps 11–12 (`/track` and `/on_track`)**: Live transit tracking query and callback.
- **Steps 13–14 (`on_status` sequence)**: Out-for-delivery and final delivery completion.
- **Step 15: `/issue (issue_open)` (BAP -> BPP)**: Buyer files an IGM 2.0.0 dispute reporting a defective medical diagnostic unit.
- **Step 16: `/on_issue (on_issue_processing)` (BPP -> BAP)**: Seller acknowledges the issue (`PROCESSING`).
- **Step 17: `on_issue (on_issue_need_more_info)` [Unsolicited] (BPP -> BAP)**: Seller requests additional visual evidence (photos/videos of device malfunction).
- **Step 18: `/issue (issue_info_provided)` (BAP -> BPP)**: Buyer provides the requested evidence media URLs.
- **Step 19: `on_issue (on_issue_provided)` [Unsolicited] (BPP -> BAP)**: Seller confirms receipt of supporting evidence.
- **Step 20: `on_issue (on_issue_resolution)` [Unsolicited] (BPP -> BAP)**: Seller validates the defect and proposes an item `REPLACEMENT`.
- **Step 21: `/issue (issue_resolution_accept)` (BAP -> BPP)**: Buyer accepts the replacement resolution.
- **Step 22: `on_issue (on_issue_resolved)` [Unsolicited] (BPP -> BAP)**: The grievance is marked as `RESOLVED`.
- **Step 23: `/issue (issue_close)` (BAP -> BPP)**: The ticket is formally closed.
- **Step 24: `on_update (on_update_igm_replacement)` [Unsolicited] (BPP -> BAP)**: Seller initiates dispatch of the replacement medical unit.

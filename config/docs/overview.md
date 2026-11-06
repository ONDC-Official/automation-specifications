# Retail Health & Wellness (ONDC:RET18 1.2.5)

- [Overview](#overview)
- [Participants](#participants)
- [The User Journey](#the-user-journey)
  - [1. Discovery and Catalog Search](#1-discovery-and-catalog-search)
  - [2. Form Factor, Dosage & Serviceability Check](#2-form-factor-dosage-serviceability-check)
  - [3. Order Initialization and Shipping Configuration](#3-order-initialization-and-shipping-configuration)
  - [4. Order Confirmation and Escrow Payment](#4-order-confirmation-and-escrow-payment)
  - [5. Order Processing, Picking, and Batch/Expiry Verification](#5-order-processing-picking-and-batchexpiry-verification)
  - [6. Logistics Assignment & Temperature/Cold-Chain Handling](#6-logistics-assignment-temperaturecold-chain-handling)
  - [7. Order Dispatch, In-Flight Tracking, and Secure Delivery](#7-order-dispatch-in-flight-tracking-and-secure-delivery)
  - [8. Settlement and Post-Fulfillment](#8-settlement-and-post-fulfillment)
- [Additional Scenarios in Version 1.2.5](#additional-scenarios-in-version-125)
  - [1. Buyer-Managed Delivery Logistics](#1-buyer-managed-delivery-logistics)
  - [2. Buyer Delivery Instructions & Address Updates](#2-buyer-delivery-instructions-address-updates)
  - [3. Cash on Delivery (COD) Checkout](#3-cash-on-delivery-cod-checkout)
  - [4. Cross-Category Multi-Item Cart](#4-cross-category-multi-item-cart)
  - [5. Dedicated Medical Device & Homeware Replacement](#5-dedicated-medical-device-homeware-replacement)
  - [6. Click-and-Collect Pharmacy Self-Pickup](#6-click-and-collect-pharmacy-self-pickup)
  - [7. Credentialed Pharmacist & Merchant Verification](#7-credentialed-pharmacist-merchant-verification)
  - [8. Slotted & Scheduled Time-Window Delivery](#8-slotted-scheduled-time-window-delivery)
  - [9. Buyer-Initiated Return and Reverse QC Pickup](#9-buyer-initiated-return-and-reverse-qc-pickup)
  - [10. Buyer-Side Pre-Dispatch Cancellation](#10-buyer-side-pre-dispatch-cancellation)
  - [11. Merchant Part-Cancellation and Return to Origin (RTO)](#11-merchant-part-cancellation-and-return-to-origin-rto)
  - [12. In-Transit Force Cancellation and Settlement](#12-in-transit-force-cancellation-and-settlement)
  - [13. Out of Stock Handling: Cart Recovery vs. Protocol Error Code](#13-out-of-stock-handling-cart-recovery-vs-protocol-error-code)
  - [14. Incremental Catalog Refresh (Push and Pull) with Store Disablement](#14-incremental-catalog-refresh-push-and-pull-with-store-disablement)
  - [15. Statutory Compliance, Batch & Expiry Tracking, and Schedule K Guidelines](#15-statutory-compliance-batch-expiry-tracking-and-schedule-k-guidelines)
- [Issue and Grievance Management](#issue-and-grievance-management)
  - [1. IGM 1.0.0 Architecture](#1-igm-100-architecture)
  - [2. IGM 2.0.0 Architecture](#2-igm-200-architecture)
- [Detailed Protocol Flows](#detailed-protocol-flows)
  - [Flow 1: Delivery Flow (Standard Forward Fulfillment)](#flow-1-delivery-flow-standard-forward-fulfillment)
  - [Flow 2: Buyer Delivery Flow (Buyer-Managed Logistics)](#flow-2-buyer-delivery-flow-buyer-managed-logistics)
  - [Flow 3: Buyer Instructions and Delivery Update Flow](#flow-3-buyer-instructions-and-delivery-update-flow)
  - [Flow 4: Cash on Delivery Flow (COD)](#flow-4-cash-on-delivery-flow-cod)
  - [Flow 5: Cross Category Cart Flow (Multi-Category Cart)](#flow-5-cross-category-cart-flow-multi-category-cart)
  - [Flow 6: Replacement Flow (Medical Diagnostics & Supplies Replacement)](#flow-6-replacement-flow-medical-diagnostics-supplies-replacement)
  - [Flow 7: Self Pickup Flow (Click-and-Collect)](#flow-7-self-pickup-flow-click-and-collect)
  - [Flow 8: Seller Cred Flow (Credentialed Seller Verification)](#flow-8-seller-cred-flow-credentialed-seller-verification)
  - [Flow 9: Slotted Delivery Flow (Time-Window Fulfillment)](#flow-9-slotted-delivery-flow-time-window-fulfillment)
  - [Flow 10: Return Flow (Post-Delivery Return and Refund)](#flow-10-return-flow-post-delivery-return-and-refund)
  - [Flow 11: Buyer Cancellation Flow](#flow-11-buyer-cancellation-flow)
  - [Flow 12: Seller Cancellation Flow (Warehouse Part-Cancellation and RTO)](#flow-12-seller-cancellation-flow-warehouse-part-cancellation-and-rto)
  - [Flow 13: Force Cancellation Flow (In-Transit Cancellation)](#flow-13-force-cancellation-flow-in-transit-cancellation)
  - [Flow 14: Out of Stock Flow (Cart Modification Recovery)](#flow-14-out-of-stock-flow-cart-modification-recovery)
  - [Flow 15: Out of Stock Flow (Immediate Error Code)](#flow-15-out-of-stock-flow-immediate-error-code)
  - [Flow 16: Discovery Flow: Full Catalog City Broadcast](#flow-16-discovery-flow-full-catalog-city-broadcast)
  - [Flow 17: Discovery Flow: Incremental Catalog Push and Disablement](#flow-17-discovery-flow-incremental-catalog-push-and-disablement)
  - [Flow 18: Discovery Flow: Incremental Catalog Refresh Pull](#flow-18-discovery-flow-incremental-catalog-refresh-pull)
  - [Flow 19: Delivery Flow with IGM 1.0.0 Dispute Resolution](#flow-19-delivery-flow-with-igm-100-dispute-resolution)
  - [Flow 20: Delivery Flow with IGM 2.0.0: Evidence Exchange and Resolution](#flow-20-delivery-flow-with-igm-200-evidence-exchange-and-resolution)
  - [Flow 21: Delivery Flow with IGM 2.0.0: Resolution Accepted (No Action)](#flow-21-delivery-flow-with-igm-200-resolution-accepted-no-action)
  - [Flow 22: Delivery Flow with IGM 2.0.0: Rejection, Escalation and Return](#flow-22-delivery-flow-with-igm-200-rejection-escalation-and-return)

---

## Overview

The Health & Wellness domain (**ONDC:RET18**, specification version **1.2.5**) establishes an open, interoperable digital commerce standard for Over-The-Counter (OTC) medicines, dietary supplements, nutraceuticals, sports nutrition, ayurvedic formulations, medical diagnostic devices, first-aid equipment, personal hygiene essentials, and mobility aids across the Open Network for Digital Commerce (ONDC).

Specification version **1.2.5** dramatically expands the foundational retail architecture with comprehensive operational enhancements tailored for health retail:
1. **Buyer-Managed Delivery Fulfillment (`Buyer_Delivery_Flow`)**: Enabling the buyer application or consumer to arrange their own dedicated or third-party courier pickup from the dispensing pharmacy.
2. **Buyer Delivery Directives & In-Flight Address Updates (`Buyer_Instructions_And_Delivery_Update_Flow`)**: Enabling buyers to specify critical delivery instructions (such as "Leave with clinic receptionist", "Do not ring bell - infant asleep", or "Fragile glass bottle") and update their delivery destination address prior to final dispatch.
3. **Cash on Delivery (COD) (`Cash_On_Delivery_Flow`)**: Native support for post-paid settlement collected directly at the doorstep.
4. **Cross-Category Multi-Item Cart (`Cross_Category_Cart_Flow`)**: Facilitating single-transaction checkouts combining items across disparate categories (e.g., OTC cold medicine, whey protein powder, and glucometer test strips).
5. **Dedicated Medical Diagnostics & Equipment Replacement (`Replacement_Flow`)**: A specialized 22-step post-delivery replacement workflow incorporating reverse QC evaluation, doorstep transit damage inspection, return courier transport, and outbound dispatch of a replacement device.
6. **Self-Pickup / Click-and-Collect (`Self_Pickup_Flow`)**: Streamlined customer collection directly from the physical pharmacy or retail store with secure handover codes.
7. **Credentialed Pharmacist & Merchant Verification (`Seller_Cred_Flow`)**: Validation of pharmacy operating credentials, pharmacist licenses, and network regulatory trust seals during order initialization.
8. **Slotted & Scheduled Delivery (`Slotted_Delivery_Flow`)**: Multi-window scheduling enabling patients to book specific delivery slots (e.g., morning 08:00–10:00 AM for fasting blood tests or evening hours for home delivery).
9. **In-Transit Forced Cancellation (`Force_Cancellation_Flow`)**: Formalized procedures for terminating delivery when a shipment is already out for delivery, with automated freight settlement reconciliation.
10. **Store Disablement Broadcasting**: Real-time push notifications signaling pharmacy operational shutdowns, branch sanitization, or temporary maintenance closures.

ONDC unbundles healthcare commerce, allowing consumers to discover authentic wellness merchandise from verified neighborhood pharmacies, regional pharmaceutical distributors, and certified direct-to-consumer (D2C) nutraceutical brands using any compliant **Buyer Application (BAP)**. Sellers manage their catalogs, batch codes, manufacturing dates, and expiration timelines through a **Seller Application (BPP)**, while certified **Logistics Service Providers (LSPs)** guarantee ambient or temperature-controlled carriage, leak-proof packaging, and tamper-evident delivery.

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
| - Health & Wellness Portals | ======= /select, /init, /confirm =====> | - Licensed Retail Pharmacies|
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
   - Consumer front-end providing symptom/product search, category exploration (Supplements, Sports Nutrition, Ayurveda, Medical Devices, First Aid), dosage form selection, delivery instruction inputs, and slotted delivery bookings.
   - Collects payments (prepaid digital or coordinates COD), enforces buyer authorization, and communicates cancellation or return requests.

2. **Seller Application (BPP)**:
   - Deployed by retail pharmacies, nutraceutical distributors, ayurvedic manufacturers, and medical supply stores.
   - Publishes catalogs with mandatory regulatory tags (batch ID, manufacturing date, expiry date, FSSAI license, net weight, dosage form).
   - Validates inventory in real time, manages warehouse picking, verifies tamper seals, packs delicate health products in tamper-evident outer containers, and coordinates carrier pickup.
   - Emits asynchronous protocol callbacks (`/on_search`, `/on_select`, `/on_init`, `/on_confirm`, `/on_status`, `/on_track`, `/on_cancel`, `/on_update`, `/on_issue`).

3. **Logistics Service Provider (LSP)**:
   - Hyperlocal on-demand couriers and express parcel networks integrated with the BPP or selected directly by the BAP.
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

### 4. Order Confirmation and Escrow Payment
- The consumer completes payment on the BAP via UPI, credit/debit card, or net banking into the BAP's escrow account (or opts for Cash on Delivery).
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

## Additional Scenarios in Version 1.2.5

Version **1.2.5** expands the health retail protocol with 15 advanced operational scenarios:

### 1. Buyer-Managed Delivery Logistics
- In `Buyer_Delivery_Flow`, the buyer application or customer coordinates the logistics fulfillment rather than relying on seller dispatch.
- The BAP coordinates carrier pickup, transitions fulfillment to `Order-picked-up` via `/update (update_picked_up)`, and marks completion upon arrival via `/update (update_delivered)`.

### 2. Buyer Delivery Instructions & Address Updates
- In `Buyer_Instructions_And_Delivery_Update_Flow`, the buyer transmits critical healthcare delivery notes (e.g. "Leave with clinic receptionist", "Do not ring doorbell - infant resting") via `/update (update_buyer_instructions)`.
- If the patient changes wards or the delivery address requires adjustment prior to packaging, the buyer invokes `/update (update_delivery_address)`, allowing seamless re-routing.

### 3. Cash on Delivery (COD) Checkout
- In `Cash_On_Delivery_Flow`, buyers opt for post-paid payment at the doorstep.
- The BAP initializes and confirms the order with `payment.type = "ON-FULFILLMENT"`.
- Upon successful doorstep cash collection by the courier, the seller confirms delivery and payment collection via `on_status (on_status_order_delivered_cod)`.

### 4. Cross-Category Multi-Item Cart
- In `Cross_Category_Cart_Flow`, consumers select and purchase products spanning multiple wellness domains (e.g., OTC cold medicine, sports whey protein, and diabetes diagnostic test strips) in a single unified cart and checkout session.
- The protocol manages mixed tax rates (e.g. 12% vs 18% GST) and consolidated fulfillment tracking.

### 5. Dedicated Medical Device & Homeware Replacement
- In `Replacement_Flow`, a comprehensive 22-step workflow manages post-delivery replacements for defective diagnostic hardware (e.g., faulty blood glucose meter or cracked nebulizer mask).
- The buyer initiates replacement via `/update (update_reverse_qc_rep)`. The seller evaluates the defect (`on_update_interim_reverseQc`), approves the replacement (`on_update_return_approved`), conducts doorstep reverse pickup (`on_update_return_picked_rep`), receives the returned unit, and dispatches a brand-new replacement unit through a complete forward delivery lifecycle.

### 6. Click-and-Collect Pharmacy Self-Pickup
- In `Self_Pickup_Flow`, the buyer selects "Self-Pickup" fulfillment to collect urgent medications directly from a neighborhood pharmacy counter.
- The pharmacy confirms when the order is packaged (`on_status_self_pick_packed`), and completes custody handover upon OTP verification at the counter (`on_status_self_pick_picked`).

### 7. Credentialed Pharmacist & Merchant Verification
- In `Seller_Cred_Flow`, the protocol verifies merchant pharmacy credentials, state pharmacy council retail drug licenses, and pharmacist registration tokens during checkout initialization and confirmation.

### 8. Slotted & Scheduled Time-Window Delivery
- In `Slotted_Delivery_Flow`, buyers schedule delivery within specific time bands (e.g. 08:00–10:00 AM for morning diagnostic samples or 06:00–08:00 PM evening delivery).
- The seller locks the requested time slot during `/on_select` and `/on_init`, ensuring the courier arrives within the promised window.

### 9. Buyer-Initiated Return and Reverse QC Pickup
- In `Return_Flow`, buyers return eligible damaged or incorrect wellness items.
- A reverse courier performs doorstep verification (verifying tamper seal integrity, batch matching, and unexpired shelf life) before the seller issues a full refund.

### 10. Buyer-Side Pre-Dispatch Cancellation
- In `Buyer_Cancellation_Flow`, the buyer cancels an unfulfilled order prior to courier handover.
- The seller acknowledges via `/on_cancel`, releases warehouse reservations, and triggers an automated refund without cancellation fee deductions.

### 11. Merchant Part-Cancellation and Return to Origin (RTO)
- In `Seller_Cancellation_Flow`, the merchant identifies an expired batch or damaged packaging during picking and cancels that specific item via `on_update (on_update_part_cancel)`, adjusting the quotation while proceeding with the rest of the order.
- If doorstep delivery fails due to buyer unavailability, the courier initiates RTO via `on_cancel (on_cancel_rto)`, returning the package to the pharmacy with settlement trail reconciliation.

### 12. In-Transit Force Cancellation and Settlement
- In `Force_Cancellation_Flow`, when a critical constraint or emergency occurs while an order is out for delivery, a force cancellation sequence is executed.
- The cancellation is acknowledged via `/on_cancel`, terminating delivery, and the BAP executes `/update (update_settlement_cancel)` to balance reverse logistics fees and buyer refunds.

### 13. Out of Stock Handling: Cart Recovery vs. Protocol Error Code
- **Soft Cart Recovery (`Out_Of_Stock_Flow`)**: The seller detects an unavailable item during `/select`, updates the quotation to exclude the missing item or adjust quantity, and allows the buyer to re-select an alternative therapeutic product and complete checkout.
- **Immediate Error Code (`Out_Of_Stock_Flow(Error-code)`)**: The seller terminates the invalid checkout immediately by responding to `/select` with standard ONDC protocol error codes (`40002` / `30009`).

### 14. Incremental Catalog Refresh (Push and Pull) with Store Disablement
- **Push & Disablement (`Discovery_Flow_incremental_catalog`)**: Sellers push real-time catalog changes and broadcast emergency pharmacy closures (e.g. branch disinfection or stock audits) using `on_search` with provider item disablement tags.
- **Incremental Pull (`Discovery_Flow_incremental_catalog_refresh_pull`)**: Buyer applications poll sellers with timestamped queries (`tags[refresh]`) to receive lightweight differential updates of updated prices, stock, and batch IDs.

### 15. Statutory Compliance, Batch & Expiry Tracking, and Schedule K Guidelines
- **Schedule K OTC Exemptions**: Strict restriction to non-prescription OTC healthcare formulations, nutraceuticals, and medical devices.
- **Mandatory Batch & Expiry Tracking**: Disclosure of `batch_id`, `mfg_date`, and `expiry_date` for every line item, enforcing minimum remaining shelf-life thresholds.
- **FSSAI & Legal Metrology**: Compliance with FSSAI Nutraceutical Regulations (2022) and Legal Metrology (Packaged Commodities) Rules for MRP, Net Quantity, Country of Origin, and Consumer Care details.

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
- **Core Real-World Scenarios in RET18 1.2.5**:
  1. **Evidence Exchange & Product Replacement (`Delivery_Flow_With_IGM(v-2.0.0)`)**:
     - Buyer reports a defective digital blood pressure monitor displaying calibration errors.
     - The seller issues an unsolicited `on_issue` (`on_issue_need_more_info`), requesting an image or video demonstration of the display error.
     - The buyer submits verification media URLs via `/issue` (`issue_info_provided`).
     - The seller validates the defect, issues `on_issue (on_issue_resolution)` proposing an item `REPLACEMENT`, and upon buyer acceptance, dispatches a brand-new replacement unit via unsolicited `on_update` (`on_update_igm_replacement`).
  2. **Resolution Accepted with Explanatory No-Action (`DELIVERY_FLOW_WITH_IGM_No_Action(v-2.0.0)`)**:
     - Buyer submits a complaint that an organic ayurvedic juice has natural herbal sediment at the bottom of the bottle.
     - The merchant's medical team examines batch retain samples and issues an explanatory resolution clarifying that sediment is natural for unrefined herbal extracts and does not indicate spoilage.
     - The buyer accepts the clarification without requiring a refund or replacement, and the ticket closes cleanly with status `RESOLVED` (`NO_ACTION`).
  3. **Dispute Rejection, Escalation, and Overturned Return (`Delivery_Flow_With_IGM_Rejection(v-2.0.0)`)**:
     - Buyer reports receiving a crushed supplement container.
     - The seller initially rejects the claim asserting outer packaging was intact upon dispatch.
     - The buyer rejects the resolution (`issue_resolution_reject`) and escalates to a network Grievance Officer / Ombudsman (`issue_escalate`).
     - The mediator reviews unboxing photos and courier delivery transit logs, ruling in favor of the consumer.
     - The seller complies with the escalated ruling, issues a full return resolution, and executes reverse pickup and refund via unsolicited `on_update` (`on_update_igm_return`).

---

## Detailed Protocol Flows

All **22 protocol flows** defined in `automation-specifications/config/flows/index.yaml` for the Health & Wellness domain (`ONDC:RET18 1.2.5`) are detailed below with their classification tags, operational contexts, and full step-by-step API message sequences.

---

### Flow 1: Delivery Flow (Standard Forward Fulfillment)

- **Flow ID:** `Delivery_Flow`
- **Config File:** `./HEALTH&WELLNESS/Delivery_Flow.yaml`
- **Protocol Version:** `1.2.5`
- **Use Case:** `HEALTH&WELLNESS`
- **Tags:** `PRAMAAN`, `MANDATORY`, `REPORTABLE`, `WORKBENCH`

#### 1. Short Description
The canonical end-to-end forward fulfillment journey for health and wellness products in specification version 1.2.5. Covers catalog item selection, dosage and availability verification, order initialization, prepaid payment capture, pharmacy warehouse picking with batch verification, multi-stage courier status updates, live GPS tracking, and secure doorstep delivery completion.

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

### Flow 2: Buyer Delivery Flow (Buyer-Managed Logistics)

- **Flow ID:** `Buyer_Delivery_Flow`
- **Config File:** `./HEALTH&WELLNESS/Buyer_Delivery_Flow.yaml`
- **Protocol Version:** `1.2.5`
- **Use Case:** `HEALTH&WELLNESS`
- **Tags:** `PRAMAAN`, `REPORTABLE`, `WORKBENCH`, `OPTIONAL`

#### 1. Short Description
Demonstrates a fulfillment model where the buyer application coordinates and manages parcel pickup and delivery from the pharmacy, rather than the seller arranging shipping.

#### 2. API Breakdown & Technical Actions
- **Step 1: `/select (select)` (BAP -> BPP)**: The buyer selects items requesting buyer-managed fulfillment.
- **Step 2: `/on_select (on_select_buyer_delivery)` (BPP -> BAP)**: The seller confirms product availability without quoting seller delivery freight charges.
- **Step 3: `/init (init_buyer_delivery)` (BAP -> BPP)**: Order initialization confirming pickup facility coordinates.
- **Step 4: `/on_init (on_init_buyer_delivery)` (BPP -> BAP)**: Seller confirms commercial terms and facility operating hours.
- **Step 5: `/confirm (confirm)` (BAP -> BPP)**: Buyer confirms prepaid order.
- **Step 6: `/on_confirm (on_confirm)` (BPP -> BAP)**: Seller records order as Created.
- **Step 7: `on_status (on_status_pending)` [Unsolicited] (BPP -> BAP)**: Seller acknowledges order processing.
- **Step 8: `on_status (on_status_packed)` [Unsolicited] (BPP -> BAP)**: Seller packs health items in tamper-evident container.
- **Step 9: `on_status (on_status_ready_to_ship)` [Unsolicited] (BPP -> BAP)**: Seller marks order as ready for pickup at the dispensing counter.
- **Step 10: `/update (update_picked_up)` (BAP -> BPP)**: Buyer's designated courier arrives, verifies package, and marks parcel as picked up.
- **Step 11: `/update (update_delivered)` (BAP -> BPP)**: Buyer confirms delivery handover completion.

---

### Flow 3: Buyer Instructions and Delivery Update Flow

- **Flow ID:** `Buyer_Instructions_And_Delivery_Update_Flow`
- **Config File:** `./HEALTH&WELLNESS/Buyer_Instructions_And_Delivery_Update_Flow.yaml`
- **Protocol Version:** `1.2.5`
- **Use Case:** `HEALTH&WELLNESS`
- **Tags:** `PRAMAAN`, `REPORTABLE`, `WORKBENCH`, `OPTIONAL`

#### 1. Short Description
Captures buyer-specified delivery instructions (such as "Leave with receptionist" or "Call upon arrival") and supports in-flight delivery address updates prior to order packaging.

#### 2. API Breakdown & Technical Actions
- **Steps 1–7 (`/select` to `on_status_pending`)**: Standard order initialization, confirmation, and initial processing.
- **Step 8: `/update (update_buyer_instructions)` (BAP -> BPP)**: Buyer submits specific delivery handling directives.
- **Step 9: `/on_update (on_update_buyer_instructions)` (BPP -> BAP)**: Seller acknowledges and associates instructions with fulfillment.
- **Step 10: `/update (update_delivery_address)` (BAP -> BPP)**: Buyer updates destination address coordinates before dispatch.
- **Step 11: `/on_update (on_update_delivery_address)` (BPP -> BAP)**: Seller validates address update and reconfirms routing.
- **Step 12: `on_status (on_status_packed)` [Unsolicited] (BPP -> BAP)**: Package is sealed.
- **Step 13: `on_status (on_status_agent_assigned)` [Unsolicited] (BPP -> BAP)**: Delivery courier assigned.
- **Step 14: `on_status (on_status_picked)` [Unsolicited] (BPP -> BAP)**: Courier takes custody.
- **Step 15: `on_update (on_update_delivery_auth)` [Unsolicited] (BPP -> BAP)**: Delivery authorization code (OTP) generated.
- **Step 16: `on_status (on_status_out_for_delivery)` [Unsolicited] (BPP -> BAP)**: Out-for-delivery status broadcast.
- **Step 17: `on_status (on_status_order_delivered)` [Unsolicited] (BPP -> BAP)**: Handover completed using delivery instructions.

---

### Flow 4: Cash on Delivery Flow (COD)

- **Flow ID:** `Cash_On_Delivery_Flow`
- **Config File:** `./HEALTH&WELLNESS/Cash_On_Delivery_Flow.yaml`
- **Protocol Version:** `1.2.5`
- **Use Case:** `HEALTH&WELLNESS`
- **Tags:** `PRAMAAN`, `OPTIONAL`, `REPORTABLE`, `WORKBENCH`

#### 1. Short Description
Demonstrates post-paid cash on delivery (COD) fulfillment. Buyers select items and confirm checkout with deferred cash collection at the doorstep.

#### 2. API Breakdown & Technical Actions
- **Step 1: `/select (select)` (BAP -> BPP)**: Buyer selects wellness products.
- **Step 2: `/on_select (on_select)` (BPP -> BAP)**: Seller quotes prices and confirms COD availability.
- **Step 3: `/init (init_cod)` (BAP -> BPP)**: Order initialized specifying `payment.type = "ON-FULFILLMENT"`.
- **Step 4: `/on_init (on_init_cod)` (BPP -> BAP)**: Seller accepts COD terms.
- **Step 5: `/confirm (confirm_cod)` (BAP -> BPP)**: Order confirmed with pending payment status.
- **Step 6: `/on_confirm (on_confirm_cod)` (BPP -> BAP)**: Order recorded as Created.
- **Steps 7–11 (`on_status` sequence)**: Progressive fulfillment from `Accepted` to `Out-for-delivery`.
- **Step 12: `on_status (on_status_order_delivered_cod)` [Unsolicited] (BPP -> BAP)**: Courier collects cash payment at doorstep and marks order as `Completed` and payment as `PAID`.

---

### Flow 5: Cross Category Cart Flow (Multi-Category Cart)

- **Flow ID:** `Cross_Category_Cart_Flow`
- **Config File:** `./HEALTH&WELLNESS/Cross_Category_Cart_Flow.yaml`
- **Protocol Version:** `1.2.5`
- **Use Case:** `HEALTH&WELLNESS`
- **Tags:** `PRAMAAN`, `REPORTABLE`, `WORKBENCH`, `MANDATORY`

#### 1. Short Description
Validates multi-category basket shopping within health and wellness, where consumers combine items across different categories (e.g. OTC medicines, protein powders, and medical diagnostic test strips) in a single checkout session.

#### 2. API Breakdown & Technical Actions
- **Step 1: `/select (select_ccc)` (BAP -> BPP)**: Cart containing products across multiple category taxonomies.
- **Step 2: `/on_select (on_select_ccc)` (BPP -> BAP)**: Seller validates inventory and returns consolidated quote breakup with individual item tax mappings.
- **Step 3: `/init (init_ccc)` (BAP -> BPP)**: Checkout initialized for the combined basket.
- **Step 4: `/on_init (on_init_ccc)` (BPP -> BAP)**: Commercial terms frozen.
- **Step 5: `/confirm (confirm_ccc)` (BAP -> BPP)**: Single consolidated payment captured.
- **Step 6: `/on_confirm (on_confirm_ccc)` (BPP -> BAP)**: Order confirmed across categories.
- **Steps 7–12 (`on_status` sequence)**: Consolidated warehouse picking, packing, dispatch, tracking, and final delivery.

---

### Flow 6: Replacement Flow (Medical Diagnostics & Supplies Replacement)

- **Flow ID:** `Replacement_Flow`
- **Config File:** `./HEALTH&WELLNESS/Replacement_Flow.yaml`
- **Protocol Version:** `1.2.5`
- **Use Case:** `HEALTH&WELLNESS`
- **Tags:** `PRAMAAN`, `REPORTABLE`, `WORKBENCH`, `OPTIONAL`

#### 1. Short Description
A complete 22-step post-delivery replacement workflow for defective medical devices or transit-damaged containers. Covers initial delivery, buyer replacement request, reverse QC inspection, doorstep return pickup, warehouse receipt, and outbound dispatch of a replacement unit.

#### 2. API Breakdown & Technical Actions
- **Steps 1–12 (`/select` to `on_status_order_delivered`)**: Complete initial order delivery lifecycle.
- **Step 13: `/update (update_reverse_qc_rep)` (BAP -> BPP)**: Buyer submits replacement claim for defective equipment.
- **Step 14: `on_update (on_update_interim_reverseQc)` [Unsolicited] (BPP -> BAP)**: Seller initiates reverse QC evaluation.
- **Step 15: `on_update (on_update_return_approved)` [Unsolicited] (BPP -> BAP)**: Seller approves replacement request.
- **Step 16: `on_update (on_update_return_picked_rep)` [Unsolicited] (BPP -> BAP)**: Reverse courier picks up defective unit from customer.
- **Step 17: `on_update (on_update_return_delivered_rep)` [Unsolicited] (BPP -> BAP)**: Return unit delivered to merchant facility.
- **Step 18: `on_status (on_status_packed_rep)` [Unsolicited] (BPP -> BAP)**: New replacement unit packed.
- **Step 19: `on_status (on_status_agent_assigned_rep)` [Unsolicited] (BPP -> BAP)**: Delivery courier assigned for replacement.
- **Step 20: `on_status (on_status_picked_rep)` [Unsolicited] (BPP -> BAP)**: Replacement package picked up.
- **Step 21: `on_status (on_status_out_for_delivery_rep)` [Unsolicited] (BPP -> BAP)**: Replacement out for delivery.
- **Step 22: `on_status (on_status_order_delivered_rep)` [Unsolicited] (BPP -> BAP)**: Customer receives replacement unit; fulfillment completed.

---

### Flow 7: Self Pickup Flow (Click-and-Collect)

- **Flow ID:** `Self_Pickup_Flow`
- **Config File:** `./HEALTH&WELLNESS/Self_Pickup_Flow.yaml`
- **Protocol Version:** `1.2.5`
- **Use Case:** `HEALTH&WELLNESS`
- **Tags:** `PRAMAAN`, `REPORTABLE`, `WORKBENCH`, `OPTIONAL`

#### 1. Short Description
Demonstrates click-and-collect customer pickup directly from a local retail pharmacy counter, bypassing third-party courier dispatch.

#### 2. API Breakdown & Technical Actions
- **Step 1: `/select (select)` (BAP -> BPP)**: Buyer selects items specifying self-pickup fulfillment.
- **Step 2: `/on_select (on_select_self_pickup)` (BPP -> BAP)**: Seller confirms store collection availability (0 delivery fee).
- **Step 3: `/init (init_self_pickup)` (BAP -> BPP)**: Customer identity and pickup store location locked.
- **Step 4: `/on_init (on_init_self_pickup)` (BPP -> BAP)**: Terms and pickup operating window confirmed.
- **Step 5: `/confirm (confirm)` (BAP -> BPP)**: Prepaid payment captured.
- **Step 6: `/on_confirm (on_confirm)` (BPP -> BAP)**: Order registered as Created.
- **Step 7: `on_status (on_status_pending)` [Unsolicited] (BPP -> BAP)**: Store staff begins picking.
- **Step 8: `on_status (on_status_self_pick_packed)` [Unsolicited] (BPP -> BAP)**: Order packed and marked ready for customer collection.
- **Step 9: `on_status (on_status_self_pick_picked)` [Unsolicited] (BPP -> BAP)**: Customer presents pickup code at pharmacy counter and collects parcel; order marked `Completed`.

---

### Flow 8: Seller Cred Flow (Credentialed Seller Verification)

- **Flow ID:** `Seller_Cred_Flow`
- **Config File:** `./HEALTH&WELLNESS/Seller_Cred_Flow.yaml`
- **Protocol Version:** `1.2.5`
- **Use Case:** `HEALTH&WELLNESS`
- **Tags:** `PRAMAAN`, `REPORTABLE`, `WORKBENCH`, `MANDATORY`

#### 1. Short Description
Validates merchant operating credentials, retail drug licenses, and pharmacist certifications during checkout initialization and confirmation.

#### 2. API Breakdown & Technical Actions
- **Step 1: `/select (select)` (BAP -> BPP)**: Product selection from credentialed seller.
- **Step 2: `/on_select (on_select)` (BPP -> BAP)**: Seller returns item pricing and verification tags.
- **Step 3: `/init (init)` (BAP -> BPP)**: Buyer initiates checkout requesting credential verification.
- **Step 4: `/on_init (on_init)` (BPP -> BAP)**: Seller provides verifiable credentials in quote tags.
- **Step 5: `/confirm (confirm_seller_cred)` (BAP -> BPP)**: Order confirmed embedding credential validation proof.
- **Step 6: `/on_confirm (on_confirm_seller_cred)` (BPP -> BAP)**: Seller acknowledges confirmed credentialed order.

---

### Flow 9: Slotted Delivery Flow (Time-Window Fulfillment)

- **Flow ID:** `Slotted_Delivery_Flow`
- **Config File:** `./HEALTH&WELLNESS/Slotted_Delivery_Flow.yaml`
- **Protocol Version:** `1.2.5`
- **Use Case:** `HEALTH&WELLNESS`
- **Tags:** `PRAMAAN`, `REPORTABLE`, `WORKBENCH`, `OPTIONAL`

#### 1. Short Description
Enables patients and buyers to schedule deliveries within dedicated time windows (e.g. morning slot 08:00–10:00 AM for fasting medical diagnostic supplies).

#### 2. API Breakdown & Technical Actions
- **Step 1: `/select (select)` (BAP -> BPP)**: Product selection specifying desired delivery time slot.
- **Step 2: `/on_select (on_select_slotted_delivery)` (BPP -> BAP)**: Seller validates slot availability and quotes delivery fee.
- **Step 3: `/init (init_slotted_delivery)` (BAP -> BPP)**: Order initialization locking delivery window.
- **Step 4: `/on_init (on_init_slotted_delivery)` (BPP -> BAP)**: Frozen terms with slot reservation.
- **Step 5: `/confirm (confirm)` (BAP -> BPP)**: Prepaid order confirmation.
- **Step 6: `/on_confirm (on_confirm)` (BPP -> BAP)**: Order recorded as Created.
- **Steps 7–12 (`on_status` sequence)**: Progressive fulfillment timed specifically to execute courier handover within the booked window.

---

### Flow 10: Return Flow (Post-Delivery Return and Refund)

- **Flow ID:** `Return_Flow`
- **Config File:** `./HEALTH&WELLNESS/Return_Flow.yaml`
- **Protocol Version:** `1.2.5`
- **Use Case:** `HEALTH&WELLNESS`
- **Tags:** `PRAMAAN`, `REPORTABLE`, `WORKBENCH`, `MANDATORY`

#### 1. Short Description
Standard post-delivery return lifecycle for damaged or incorrect health supplies. Covers return request authorization, doorstep reverse logistics collection with condition inspection, settlement trail coordination, and final warehouse verification and refund closure.

#### 2. API Breakdown & Technical Actions
- **Steps 1–12 (`/select` to `on_status_order_delivered`)**: Complete initial order delivery lifecycle.
- **Step 13: `/update (update_return)` (BAP -> BPP)**: Buyer initiates return claim specifying return reason.
- **Step 14: `/on_update (on_update_return_init)` (BPP -> BAP)**: Seller acknowledges return request.
- **Step 15: `on_update (on_update_return_approved)` [Unsolicited] (BPP -> BAP)**: Seller validates eligibility and approves return.
- **Step 16: `on_update (on_update_return_picked)` [Unsolicited] (BPP -> BAP)**: Reverse courier inspects seal and collects item.
- **Step 17: `/update (update_settlement_trail)` (BAP -> BPP)**: Settlement trail updated with refund terms.
- **Step 18: `on_update (on_update_return_delivered)` [Unsolicited] (BPP -> BAP)**: Return parcel arrives at warehouse; refund executed.

---

### Flow 11: Buyer Cancellation Flow

- **Flow ID:** `Buyer_Cancellation_Flow`
- **Config File:** `./HEALTH&WELLNESS/Buyer_Cancellation_Flow.yaml`
- **Protocol Version:** `1.2.5`
- **Use Case:** `HEALTH&WELLNESS`
- **Tags:** `PRAMAAN`, `MANDATORY`, `REPORTABLE`, `WORKBENCH`

#### 1. Short Description
Demonstrates a pre-dispatch order cancellation initiated by the consumer prior to pharmacy dispatch. Validates immediate cancellation processing, inventory release, and automated payment refund without penalty.

#### 2. API Breakdown & Technical Actions
- **Steps 1–6 (`/select` to `/on_confirm`)**: Standard prepaid order flow.
- **Step 7: `/cancel (cancel)` (BAP -> BPP)**: Buyer cancels order citing valid cancellation code.
- **Step 8: `/on_cancel (on_cancel)` (BPP -> BAP)**: Seller acknowledges cancellation, marks order `Cancelled`, and initiates full refund.

---

### Flow 12: Seller Cancellation Flow (Warehouse Part-Cancellation and RTO)

- **Flow ID:** `Seller_Cancellation_Flow`
- **Config File:** `./HEALTH&WELLNESS/Seller_Cancellation_Flow.yaml`
- **Protocol Version:** `1.2.5`
- **Use Case:** `HEALTH&WELLNESS`
- **Tags:** `PRAMAAN`, `REPORTABLE`, `WORKBENCH`, `MANDATORY`

#### 1. Short Description
Demonstrates dual exception scenarios: merchant part-cancellation during warehouse picking due to damaged/expired batch inventory, followed by delivery failure leading to Return to Origin (RTO) and reverse freight settlement.

#### 2. API Breakdown & Technical Actions
- **Steps 1–6 (`/select` to `/on_confirm`)**: Standard prepaid multi-item order flow.
- **Step 7: `on_update (on_update_part_cancel)` [Unsolicited] (BPP -> BAP)**: Seller cancels unavailable/expired item during picking.
- **Step 8: `/update (update_partial_cancel_settlement)` (BAP -> BPP)**: Settlement trail adjusted for partial refund.
- **Steps 9–13 (`on_status` sequence)**: Remaining active item progresses through packaging to `Out-for-delivery`.
- **Step 14: `on_cancel (on_cancel_rto)` [Unsolicited] (BPP -> BAP)**: Courier fails delivery at destination and triggers RTO.
- **Step 15: `on_status (on_status_rto_delivereddisposed)` [Unsolicited] (BPP -> BAP)**: Courier returns package to pharmacy warehouse; refund issued minus legitimate shipping costs.

---

### Flow 13: Force Cancellation Flow (In-Transit Cancellation)

- **Flow ID:** `Force_Cancellation_Flow`
- **Config File:** `./HEALTH&WELLNESS/Force_Cancellation_Flow.yaml`
- **Protocol Version:** `1.2.5`
- **Use Case:** `HEALTH&WELLNESS`
- **Tags:** `PRAMAAN`, `REPORTABLE`, `WORKBENCH`, `MANDATORY`

#### 1. Short Description
Demonstrates in-transit force cancellation when an emergency or critical constraint occurs while the shipment is already out for delivery.

#### 2. API Breakdown & Technical Actions
- **Steps 1–11 (`/select` to `on_status_out_for_delivery`)**: Forward fulfillment progresses to out-for-delivery.
- **Step 12: `/cancel (cancel_no)` (BAP -> BPP)**: Initial cancellation probe rejected if conditions not met.
- **Step 13: `/cancel (cancel_yes)` (BAP -> BPP)**: Buyer submits mandatory force cancellation with override justification.
- **Step 14: `/on_cancel (on_cancel_yes)` (BPP -> BAP)**: Seller confirms termination of in-transit delivery.
- **Step 15: `/update (update_settlement_cancel)` (BAP -> BPP)**: Settlement trail reconciled with reverse logistics fee calculations.

---

### Flow 14: Out of Stock Flow (Cart Modification Recovery)

- **Flow ID:** `Out_Of_Stock_Flow`
- **Config File:** `./HEALTH&WELLNESS/Out_Of_Stock_Flow.yaml`
- **Protocol Version:** `1.2.5`
- **Use Case:** `HEALTH&WELLNESS`
- **Tags:** `PRAMAAN`, `REPORTABLE`, `WORKBENCH`, `MANDATORY`

#### 1. Short Description
Demonstrates soft recovery when an item is out of stock during `/select`. The buyer updates their cart selection with an available alternative, successfully completing checkout.

#### 2. API Breakdown & Technical Actions
- **Step 1: `/select (select_out_of_stock)` (BAP -> BPP)**: Buyer selects unavailable item.
- **Step 2: `/on_select (on_select_out_of_stock)` (BPP -> BAP)**: Seller signals stock shortage in quote breakup.
- **Step 3: `/select (select)` (BAP -> BPP)**: Buyer modifies cart with available alternative.
- **Step 4: `/on_select (on_select)` (BPP -> BAP)**: Seller confirms availability and quotes pricing.
- **Steps 5–14 (`/init` to `on_status_order_delivered`)**: Standard checkout and forward delivery completed.

---

### Flow 15: Out of Stock Flow (Immediate Error Code)

- **Flow ID:** `Out_Of_Stock_Flow(Error-code)`
- **Config File:** `./HEALTH&WELLNESS/Out_Of_Stock_Flow_Error-code_.yaml`
- **Protocol Version:** `1.2.5`
- **Use Case:** `HEALTH&WELLNESS`
- **Tags:** `PRAMAAN`, `REPORTABLE`, `WORKBENCH`, `MANDATORY`

#### 1. Short Description
Tests out-of-stock protocol error reporting when a customer selects an unavailable health product and the seller terminates the transaction with an immediate error response.

#### 2. API Breakdown & Technical Actions
- **Step 1: `/select (select_out_of_stock)` (BAP -> BPP)**: Buyer attempts to select out-of-stock item.
- **Step 2: `/on_select (on_select_out_of_stock)` (BPP -> BAP)**: Seller returns immediate ONDC protocol error codes (`40002` / `30009`), halting invalid progression.

---

### Flow 16: Discovery Flow: Full Catalog City Broadcast

- **Flow ID:** `Discovery_Flow_full_catalog`
- **Config File:** `./HEALTH&WELLNESS/Discovery_Flow_full_catalog.yaml`
- **Protocol Version:** `1.2.5`
- **Use Case:** `HEALTH&WELLNESS`
- **Tags:** `PRAMAAN`, `MANDATORY`, `REPORTABLE`, `WORKBENCH`

#### 1. Short Description
Broad city-wide product discovery where a buyer searches for available health and wellness offerings within an entire city, receiving complete categorized catalogs from participating pharmacies and wellness stores.

#### 2. API Breakdown & Technical Actions
- **Step 1: `/search (search_full_catalog)` (BAP -> Gateway/BPP)**: City-wide broadcast search across domain `ONDC:RET18`.
- **Step 2: `/on_search (on_search_full_catalog)` (BPP -> BAP)**: Participating pharmacies respond with full item menus, pricing, batch details, and delivery capabilities.

---

### Flow 17: Discovery Flow: Incremental Catalog Push and Disablement

- **Flow ID:** `Discovery_Flow_incremental_catalog`
- **Config File:** `./HEALTH&WELLNESS/Discovery_Flow_incremental_catalog.yaml`
- **Protocol Version:** `1.2.5`
- **Use Case:** `HEALTH&WELLNESS`
- **Tags:** `PRAMAAN`, `MANDATORY`, `REPORTABLE`, `WORKBENCH`

#### 1. Short Description
Progressive catalog delivery and merchant store status broadcasting. Simulates sellers pushing real-time inventory updates and temporary operational closures (e.g. branch disinfection or stock audit) directly to buyer applications.

#### 2. API Breakdown & Technical Actions
- **Step 1: `/search (search_inc)` (BAP -> BPP)**: Initial query establishing discovery context.
- **Step 2: `/on_search (on_search_inc)` (BPP -> BAP)**: Seller pushes incremental inventory updates.
- **Step 3: `on_search (on_search_inc_disable)` [Unsolicited] (BPP -> BAP)**: Seller broadcasts store closure or item disablement.
- **Step 4: `/search (search_inc1)` (BAP -> BPP)**: Buyer confirms updated status.

---

### Flow 18: Discovery Flow: Incremental Catalog Refresh Pull

- **Flow ID:** `Discovery_Flow_incremental_catalog_refresh_pull`
- **Config File:** `./HEALTH&WELLNESS/Discovery_Flow_incremental_catalog_refresh_pull.yaml`
- **Protocol Version:** `1.2.5`
- **Use Case:** `HEALTH&WELLNESS`
- **Tags:** `PRAMAAN`, `REPORTABLE`, `WORKBENCH`, `OPTIONAL`

#### 1. Short Description
Enables buyer applications to periodically pull modified, newly listed, or out-of-stock items using timestamped delta queries, minimizing network bandwidth and ensuring real-time inventory precision.

#### 2. API Breakdown & Technical Actions
- **Step 1: `/search (search)` (BAP -> BPP)**: Baseline search query for catalog synchronization.
- **Step 2: `/on_search (on_search)` (BPP -> BAP)**: Initial catalog baseline returned.
- **Step 3: `/search (search_inc_pull)` (BAP -> BPP)**: Differential search with timestamp tag (`tags[refresh]`).
- **Step 4: `/on_search (on_search_inc_pull)` (BPP -> BAP)**: Seller returns only items modified after the timestamp.

---

### Flow 19: Delivery Flow with IGM 1.0.0 Dispute Resolution

- **Flow ID:** `Delivery_Flow_With_IGM(v-1.0.0)`
- **Config File:** `./HEALTH&WELLNESS/Delivery_Flow_With_IGM_v-1_0_0_.yaml`
- **Protocol Version:** `1.2.5`
- **Use Case:** `HEALTH&WELLNESS`
- **Tags:** `PRAMAAN`, `MANDATORY`, `REPORTABLE`, `WORKBENCH`

#### 1. Short Description
Forward delivery with integrated IGM 1.0.0 grievance management. A customer logs an issue regarding damaged or incorrect items, and the merchant resolves it through standard linear ticketing.

#### 2. API Breakdown & Technical Actions
- **Steps 1–12 (`/select` to `on_status_order_delivered`)**: Complete forward delivery lifecycle.
- **Step 13: `/issue (issue_open_100)` (BAP -> BPP)**: Buyer files grievance with issue description and photos.
- **Step 14: `/on_issue (on_issue_processing_100)` (BPP -> BAP)**: Merchant acknowledges ticket as `PROCESSING`.
- **Step 15: `/on_issue_status (on_issue_resolved_100)` (BPP -> BAP)**: Merchant investigates and provides resolution (`RESOLVED`).
- **Step 16: `/issue (issue_close_100)` (BAP -> BPP)**: Buyer verifies resolution and marks ticket `CLOSED`.

---

### Flow 20: Delivery Flow with IGM 2.0.0: Evidence Exchange and Resolution

- **Flow ID:** `Delivery_Flow_With_IGM(v-2.0.0)`
- **Config File:** `./HEALTH&WELLNESS/Delivery_Flow_With_IGM_v-2_0_0_.yaml`
- **Protocol Version:** `1.2.5`
- **Use Case:** `HEALTH&WELLNESS`
- **Tags:** `PRAMAAN`, `MANDATORY`, `REPORTABLE`, `WORKBENCH`

#### 1. Short Description
Demonstrates collaborative evidence exchange under IGM 2.0.0. The seller requests additional verification regarding a defective medical device, the buyer provides photo/video evidence, and the seller approves an item replacement, initiating dispatch of a new replacement unit.

#### 2. API Breakdown & Technical Actions
- **Steps 1–12 (`/select` to `on_status_order_delivered`)**: Complete forward delivery lifecycle.
- **Step 13: `/issue (issue_open)` (BAP -> BPP)**: Buyer files IGM 2.0.0 grievance reporting a defective device.
- **Step 14: `/on_issue (on_issue_processing)` (BPP -> BAP)**: Seller acknowledges ticket as `PROCESSING`.
- **Step 15: `on_issue (on_issue_need_more_info)` [Unsolicited] (BPP -> BAP)**: Seller requests additional demonstration photos/videos.
- **Step 16: `/issue (issue_info_provided)` (BAP -> BPP)**: Buyer provides evidence URLs.
- **Step 17: `on_issue (on_issue_provided)` [Unsolicited] (BPP -> BAP)**: Seller confirms receipt of evidence.
- **Step 18: `on_issue (on_issue_resolution)` [Unsolicited] (BPP -> BAP)**: Seller approves resolution proposing item `REPLACEMENT`.
- **Step 19: `/issue (issue_resolution_accept)` (BAP -> BPP)**: Buyer accepts replacement resolution.
- **Step 20: `on_issue (on_issue_resolved)` [Unsolicited] (BPP -> BAP)**: Issue marked `RESOLVED`.
- **Step 21: `/issue (issue_close)` (BAP -> BPP)**: Ticket marked `CLOSED`.
- **Step 22: `on_update (on_update_igm_replacement)` [Unsolicited] (BPP -> BAP)**: Seller initiates replacement shipment.

---

### Flow 21: Delivery Flow with IGM 2.0.0: Resolution Accepted (No Action)

- **Flow ID:** `DELIVERY_FLOW_WITH_IGM_No_Action(v-2.0.0)`
- **Config File:** `./HEALTH&WELLNESS/DELIVERY_FLOW_WITH_IGM_No_Action_v-2_0_0_.yaml`
- **Protocol Version:** `1.2.5`
- **Use Case:** `HEALTH&WELLNESS`
- **Tags:** `PRAMAAN`, `REPORTABLE`, `WORKBENCH`, `MANDATORY`

#### 1. Short Description
Demonstrates an IGM 2.0.0 grievance where a buyer inquires about perceived discrepancies (e.g. natural herbal sediment or cosmetic packaging updates). The seller's medical team provides technical clarification, the buyer accepts, and the ticket is resolved with a `NO_ACTION` disposition.

#### 2. API Breakdown & Technical Actions
- **Steps 1–12 (`/select` to `on_status_order_delivered`)**: Complete forward delivery lifecycle.
- **Step 13: `/issue (issue_open_2)` (BAP -> BPP)**: Buyer lodges inquiry complaint.
- **Step 14: `/on_issue (on_issue_processing)` (BPP -> BAP)**: Seller marks status `PROCESSING`.
- **Step 15: `on_issue (on_issue_resolution_igm_3)` [Unsolicited] (BPP -> BAP)**: Seller provides technical explanation (`NO_ACTION`).
- **Step 16: `/issue (issue_resolution_accept_igm_3)` (BAP -> BPP)**: Buyer accepts explanation.
- **Step 17: `on_issue (on_issue_resolved_igm_3)` [Unsolicited] (BPP -> BAP)**: Ticket marked `RESOLVED`.
- **Step 18: `/issue (issue_close_igm_3)` (BAP -> BPP)**: Ticket marked `CLOSED`.
- **Step 19: `on_status (on_status_igm_3)` [Unsolicited] (BPP -> BAP)**: Seller confirms final order state remains `Completed`.

---

### Flow 22: Delivery Flow with IGM 2.0.0: Rejection, Escalation and Return

- **Flow ID:** `Delivery_Flow_With_IGM_Rejection(v-2.0.0)`
- **Config File:** `./HEALTH&WELLNESS/Delivery_Flow_With_IGM_Rejection_v-2_0_0_.yaml`
- **Protocol Version:** `1.2.5`
- **Use Case:** `HEALTH&WELLNESS`
- **Tags:** `PRAMAAN`, `MANDATORY`, `REPORTABLE`, `WORKBENCH`

#### 1. Short Description
Demonstrates an escalated dispute lifecycle under IGM 2.0.0. The seller initially rejects a buyer's claim regarding transit damage. The buyer escalates to a network Grievance Officer / Ombudsman, who overturns the seller's rejection, ordering a return and refund.

#### 2. API Breakdown & Technical Actions
- **Steps 1–12 (`/select` to `on_status_order_delivered`)**: Complete forward delivery lifecycle.
- **Step 13: `/issue (issue_open)` (BAP -> BPP)**: Buyer opens dispute for transit damage.
- **Step 14: `/on_issue (on_issue_processing)` (BPP -> BAP)**: Seller marks ticket `PROCESSING`.
- **Step 15: `on_issue (on_issue_resolution)` [Unsolicited] (BPP -> BAP)**: Seller initially rejects claim.
- **Step 16: `/issue (issue_resolution_reject)` (BAP -> BPP)**: Buyer rejects merchant resolution.
- **Step 17: `on_issue (on_issue_processing_1)` [Unsolicited] (BPP -> BAP)**: Second review undertaken.
- **Step 18: `on_issue (on_issue_resolution_1)` [Unsolicited] (BPP -> BAP)**: Seller reiterates rejection.
- **Step 19: `/issue (issue_escalate)` (BAP -> BPP)**: Buyer escalates to network Grievance Officer / Ombudsman.
- **Step 20: `on_issue (on_issue_processing_2)` [Unsolicited] (BPP -> BAP)**: Ombudsman assumes jurisdiction.
- **Step 21: `on_issue (on_issue_resolution_2)` [Unsolicited] (BPP -> BAP)**: Ombudsman overturns rejection, ordering full return and refund.
- **Step 22: `/issue (issue_resolution_accept)` (BAP -> BPP)**: Buyer accepts binding ruling.
- **Step 23: `on_issue (on_issue_resolved)` [Unsolicited] (BPP -> BAP)**: Ticket marked `RESOLVED`.
- **Step 24: `/issue (issue_close)` (BAP -> BPP)**: Ticket marked `CLOSED`.
- **Step 25: `on_update (on_update_igm_return)` [Unsolicited] (BPP -> BAP)**: Seller initiates reverse courier pickup and refund settlement.

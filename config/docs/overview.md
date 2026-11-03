# Retail Grocery (ONDC:RET10 — Version 1.2.5)

- [Overview](#overview)
- [Key Advancements in v1.2.5](#key-advancements-in-v125)
- [Participants](#participants)
- [The User Journey](#the-user-journey)
  - [1. Discovery and Catalog Search](#1-discovery-and-catalog-search)
  - [2. Multi-Fulfillment and Slotted Item Selection](#2-multi-fulfillment-and-slotted-item-selection)
  - [3. Order Initialization, Delivery Configuration, and Commercials](#3-order-initialization-delivery-configuration-and-commercials)
  - [4. Order Confirmation and Payment Options (Prepaid & COD)](#4-order-confirmation-and-payment-options-prepaid--cod)
  - [5. Order Processing, Dynamic Instructions, and Packing](#5-order-processing-dynamic-instructions-and-packing)
  - [6. Logistics, Delivery Assignment, and Real-Time Tracking](#6-logistics-delivery-assignment-and-real-time-tracking)
  - [7. Order Handover, OTP Verification, and Delivery](#7-order-handover-otp-verification-and-delivery)
  - [8. Financial Settlement, Commercial Fees, and Reconciliation](#8-financial-settlement-commercial-fees-and-reconciliation)
- [Additional Scenarios in v1.2.5](#additional-scenarios-in-v125)
  - [1. Cash on Delivery (COD) Checkout](#1-cash-on-delivery-cod-checkout)
  - [2. Slotted & Scheduled Deliveries](#2-slotted--scheduled-deliveries)
  - [3. Multi-Option Fulfillment Selection](#3-multi-option-fulfillment-selection)
  - [4. In-Store Self-Pickup (Click & Collect)](#4-in-store-self-pickup-click--collect)
  - [5. In-Flight Buyer Instructions and Address Updates](#5-in-flight-buyer-instructions-and-address-updates)
  - [6. Item Replacement and Reverse Quality Check (QC)](#6-item-replacement-and-reverse-quality-check-qc)
  - [7. Forced and System Cancellations](#7-forced-and-system-cancellations)
  - [8. Merchant Part-Cancellation and Return to Origin (RTO)](#8-merchant-part-cancellation-and-return-to-origin-rto)
  - [9. Buyer-Initiated Return and Refund](#9-buyer-initiated-return-and-refund)
  - [10. Out of Stock Handling (Cart Recovery & Immediate Error Code)](#10-out-of-stock-handling-cart-recovery--immediate-error-code)
  - [11. Commercial Settlement Model (BNP / SNP Fees)](#11-commercial-settlement-model-bnp--snp-fees)
  - [12. Incremental Catalog Sync (Push and Pull)](#12-incremental-catalog-sync-push-and-pull)
  - [13. Statutory Compliance and Catalog Rejection](#13-statutory-compliance-and-catalog-rejection)
- [Issue and Grievance Management](#issue-and-grievance-management)
  - [1. IGM 1.0.0 Architecture](#1-igm-100-architecture)
  - [2. IGM 2.0.0 Architecture](#2-igm-200-architecture)
- [Detailed Protocol Flows](#detailed-protocol-flows)
  - [Flow 1: Delivery Flow (Standard Prepaid Home Delivery)](#flow-1-delivery-flow-standard-prepaid-home-delivery)
  - [Flow 2: Buyer Delivery Flow (Buyer-Managed Logistics)](#flow-2-buyer-delivery-flow-buyer-managed-logistics)
  - [Flow 3: Buyer Instructions and Delivery Update Flow](#flow-3-buyer-instructions-and-delivery-update-flow)
  - [Flow 4: Cancellation Flow (Buyer-Side Order Cancellation)](#flow-4-cancellation-flow-buyer-side-order-cancellation)
  - [Flow 5: Cash on Delivery Flow (COD Fulfillment)](#flow-5-cash-on-delivery-flow-cod-fulfillment)
  - [Flow 6: Commercial Model for BNP and SNP Flow](#flow-6-commercial-model-for-bnp-and-snp-flow)
  - [Flow 7: Slotted Delivery Flow (Time Slot Scheduling)](#flow-7-slotted-delivery-flow-time-slot-scheduling)
  - [Flow 8: Multi-Option Fulfillment Flow (Express / Standard / Same Day)](#flow-8-multi-option-fulfillment-flow-express--standard--same-day)
  - [Flow 9: Self-Pickup Flow (Click & Collect)](#flow-9-self-pickup-flow-click--collect)
  - [Flow 10: Replacement Flow (Reverse QC & Item Replacement)](#flow-10-replacement-flow-reverse-qc--item-replacement)
  - [Flow 11: Return Flow (Customer-Initiated Return & Refund)](#flow-11-return-flow-customer-initiated-return--refund)
  - [Flow 12: RTO and Part-Cancellation Flow](#flow-12-rto-and-part-cancellation-flow)
  - [Flow 13: Forced Cancellation Flow](#flow-13-forced-cancellation-flow)
  - [Flow 14: Out of Stock Flow (Cart Rebalancing & Recovery)](#flow-14-out-of-stock-flow-cart-rebalancing--recovery)
  - [Flow 15: Out of Stock Flow (Error Code Rejection)](#flow-15-out-of-stock-flow-error-code-rejection)
  - [Flow 16: Discovery Flow – Full Catalog City Discovery](#flow-16-discovery-flow--full-catalog-city-discovery)
  - [Flow 17: Discovery Flow – Incremental Catalog Push](#flow-17-discovery-flow--incremental-catalog-push)
  - [Flow 18: Discovery Flow – Incremental Catalog Refresh Pull](#flow-18-discovery-flow--incremental-catalog-refresh-pull)
  - [Flow 19: Catalog Rejection Flow (Statutory Non-Compliance)](#flow-19-catalog-rejection-flow-statutory-non-compliance)
  - [Flow 20: Delivery Flow with IGM 1.0.0 Resolution](#flow-20-delivery-flow-with-igm-100-resolution)
  - [Flow 21: Delivery Flow with IGM 2.0.0 – Evidence Exchange & Replacement](#flow-21-delivery-flow-with-igm-200--evidence-exchange--replacement)
  - [Flow 22: Delivery Flow with IGM 2.0.0 – Resolution Accepted (No Action)](#flow-22-delivery-flow-with-igm-200--resolution-accepted-no-action)
  - [Flow 23: Delivery Flow with IGM 2.0.0 – Dispute Escalation & Mandated Return](#flow-23-delivery-flow-with-igm-200--dispute-escalation--mandated-return)

---

## Overview

The Retail Grocery domain (**ONDC:RET10**), standardized under core specification version **1.2.5**, governs digital commerce transactions for packaged commodities, fresh staples, dairy, fruits and vegetables, and daily household essentials across the Open Network for Digital Commerce (ONDC).

Grocery retail is distinguished by high transaction frequency, hyperlocal geographic radii, perishable inventories with dynamic price and stock swings, stringent statutory labelling mandates (FSSAI licenses and the Legal Metrology / Packaged Commodities Rules 2011), and a wide spectrum of fulfillment modalities. 

ONDC decouples consumer-facing applications (**Buyer Applications / BAPs**) from store operators and catalog aggregators (**Seller Applications / BPPs**). A buyer uses their preferred consumer interface to discover multiple grocery providers within their delivery locality, evaluate real-time inventory and delivery turnaround times (TAT), build composite baskets, configure fulfillment preferences, and monitor fulfillment live. Sellers manage their inventory, pricing, batch packaging, and dispatch policies independently while connecting to the open network.

---

## Key Advancements in v1.2.5

The **v1.2.5** retail grocery specification expands upon previous minor releases by introducing critical commercial and operational capabilities required for production-scale commerce:

1. **Flexible Fulfillment Modalities**:
   - **Multi-Option Fulfillment**: Empowers sellers to present tiered delivery tiers (e.g., Express Delivery, Standard Home Delivery, Same-Day) within the same quote.
   - **Slotted Deliveries**: Enables consumers to select specific calendar dates and time windows (e.g. 10:00 AM – 12:00 PM) for parcel arrival.
   - **Self-Pickup (Click & Collect)**: Explicit zero-delivery-fee flows where the consumer personally collects packed parcels from merchant premises.
2. **Dynamic In-Flight Order Modifications**:
   - Allows buyers to send real-time delivery instructions (e.g. "Leave with guard", "Do not ring doorbell") and update destination addresses post-confirmation before parcel dispatch.
   - Introduces secure delivery authentication mechanisms (`on_update_delivery_auth` OTP tokens).
3. **Enhanced Commercial and Settlement Architecture**:
   - Establishes standardized commercial fee models for Buyer Network Participants (BNP finder fees) and Seller Network Participants (SNP platform fees), with support for TDS/TCS statutory withholdings and credit terms.
   - Formalizes Pay-on-Delivery / **Cash on Delivery (COD)** checkout and post-delivery cash collection reconciliation.
4. **End-to-End Reverse QC and Item Replacements**:
   - Introduces dedicated reverse logistics lifecycles incorporating doorstep quality check (QC), item pickup authorization, and forward dispatch of replacement grocery goods.
5. **Robust Exception Handling & Cancellation Controls**:
   - Distinguishes standard buyer cancellations from emergency merchant/system **Forced Cancellations** triggered by sudden logistical or inventory failure.
   - Standardizes Return to Origin (RTO) execution with automated reverse settlement deductions.
6. **Dual IGM Framework Support**:
   - Standardizes both **IGM 1.0.0** (linear ticket resolution) and **IGM 2.0.0** (multi-party evidence exchange, dispute escalation to Level 2 grievance officers, and automated fulfillment linkages).

---

## Participants

| Participant | Role & Network Function |
|---|---|
| **Buyer Application (BAP)** | The consumer-facing application (e.g. consumer e-commerce apps, UPI apps, chat apps, telco apps) where consumers browse grocery catalogs, configure delivery addresses, build shopping carts, pay for orders, track delivery riders, and raise grievances. |
| **Seller Application (BPP)** | An application representing grocery retailers, supermarkets, kirana stores, or Direct-to-Consumer (D2C) brands. The BPP publishes item catalogs, validates delivery serviceability, computes tax/delivery quotes, manages order confirmation, coordinates warehouse/store picking and packing, and handles returns or cancellations. |
| **Logistics Service Provider (LSP)** | A delivery network participant providing hyperlocal or intercity fulfillment. In Seller-managed logistics, the BPP coordinates with the LSP; in Buyer-managed delivery (`Buyer_Delivery_Flow`), the BAP coordinates logistics and transmits delivery tracking updates back to the BPP. |
| **Gateway** | The ONDC routing infrastructure that multicasts broadcast discovery requests (`/search`) from BAPs to active seller applications (BPPs) based on domain code, geolocation, or city code. |

---

## The User Journey

The standard grocery ordering journey enables a consumer to discover local grocery stores, evaluate delivery estimates and item prices, configure delivery coordinates, make payment, and receive goods with real-time tracking.

### 1. Discovery and Catalog Search

The buyer initiates discovery on the BAP by searching for grocery items, stores, or categories (e.g. "Atta", "Fruits and Vegetables", "Dairy"):

- **Intent Broadcast**: The BAP transmits a `/search` request specifying the domain category (`ONDC:RET10`), buyer location (GPS coordinates and pincode/area code), and fulfillment type (`Delivery` or `Self-Pickup`).
- **Catalog Delivery**: Active BPPs within the serviceable area respond via asynchronous `/on_search` payloads containing their store catalog (`bpp/providers[]`). This includes items, images, MRP, selling price, unitized measure (e.g., 1 kg, 500 g), stock availability, serviceability tags, and statutory packaged commodity details (manufacturer name, address, packaging date, consumer care details).

### 2. Multi-Fulfillment and Slotted Item Selection

The buyer selects items from a specific grocery provider and adds them to their cart:

- **Network interaction:**
  - **`/select` (BAP -> BPP)**: The BAP transmits the selected items (`order.items[]`), quantities, provider location ID (`location_id`), and destination GPS coordinates (`fulfillments[0].end.location.gps` and `address.area_code`).
  - **`/on_select` (BPP -> BAP)**: The seller validates real-time inventory and delivery serviceability. The seller returns an itemized price quote (`quote.breakup[]`) breaking down item costs, delivery charges, packaging fees, applicable taxes (CGST/SGST), and estimated turnaround time (`@ondc/org/TAT`). In slotted or multi-option flows, available fulfillment IDs and schedule windows are presented.

### 3. Order Initialization, Delivery Configuration, and Commercials

The buyer provides finalized delivery and billing details:

- **Network interaction:**
  - **`/init` (BAP -> BPP)**: The BAP sends the buyer's full street address, contact details (phone, email), billing address, and selected payment method preferences.
  - **`/on_init` (BPP -> BAP)**: The seller freezes the order quote, specifies static/dynamic terms (cancellation terms, return windows, credit terms), sets payment collection rules (e.g., BAP-collected prepaid payment or Pay-on-Delivery), and returns settlement fee details.

### 4. Order Confirmation and Payment Options (Prepaid & COD)

The buyer completes digital payment (or selects Cash on Delivery):

- **Network interaction:**
  - **`/confirm` (BAP -> BPP)**: The BAP captures payment (or registers COD intent), generates the formal order record (`order.id`), and transmits payment confirmation parameters (`payment.status = "PAID"` or `"NOT-PAID"` for COD).
  - **`/on_confirm` (BPP -> BAP)**: The seller validates payment, records the order in its Point of Sale / Order Management System (POS/OMS), marks `order.state = "Created"`, and sets initial fulfillment state to `"Pending"`.

### 5. Order Processing, Dynamic Instructions, and Packing

The seller's store or warehouse team picks the ordered grocery items from shelves and packs them:

- **`on_status (Accepted)` (BPP -> BAP)**: An unsolicited status update indicating the merchant has reviewed and accepted the grocery order (`order.state = "Accepted"`).
- **In-Flight Customization**: In flows supporting buyer updates, the buyer transmits specialized handling instructions or revised addresses via `/update`, which the merchant confirms via `/on_update`.
- **`on_status (Packed)` (BPP -> BAP)**: An unsolicited status update confirming all grocery items have been picked, weighed, verified, and bagged into parcels ready for pickup (`fulfillment.state = "Packed"`, `order.state = "In-progress"`).

### 6. Logistics, Delivery Assignment, and Real-Time Tracking

A delivery partner or store rider is assigned to the fulfillment:

- **`on_status (Agent-assigned)` (BPP -> BAP)**: The seller sends an unsolicited update once a delivery executive accepts the trip. Under v1.2.5 contracts, rider credentials (`fulfillments[0].agent.name`, `agent.phone`) are mandatory.
- **`on_status (Order-picked-up)` (BPP -> BAP)**: The seller notifies the BAP that the parcel has left the merchant premises (`fulfillment.state = "Order-picked-up"`), recording `fulfillments[0].start.time.timestamp`.
- **`/track` & `/on_track` (BAP $\leftrightarrow$ BPP)**: The BAP polls for live GPS telemetry of the delivery executive, receiving active tracking URLs and location coordinates.

### 7. Order Handover, OTP Verification, and Delivery

The delivery executive collects the packed groceries from the store and transports them to the buyer's address:

- **`on_status (Out-for-delivery)` (BPP -> BAP)**: Triggered when the rider enters the destination neighborhood.
- **`on_update (Delivery Auth)` (BPP -> BAP)**: The seller issues a secure OTP delivery authentication token.
- **`on_status (Order-delivered)` (BPP -> BAP)**: Sent upon successful physical handover of grocery items at the buyer's door (`fulfillment.state = "Order-delivered"`, `order.state = "Completed"`), recording `fulfillments[0].end.time.timestamp` and electronic proof of delivery (ePOD / delivery OTP verification).

### 8. Financial Settlement, Commercial Fees, and Reconciliation

Post-delivery, the network transaction proceeds to financial reconciliation. The BAP releases funds to the seller according to the agreed settlement window (T+1 / T+2), withholding agreed buyer finder fees and routing statutory tax deductions (TCS/TDS) where applicable.

---

## Additional Scenarios in v1.2.5

The v1.2.5 specification expands coverage across operational, fulfillment, and commercial edge cases:

### 1. Cash on Delivery (COD) Checkout
In `Cash_On_Delivery_Flow`, the consumer selects Cash on Delivery. The order is initiated with `payment.type = "ON-FULFILLMENT"` and confirmed with `payment.status = "NOT-PAID"`. Upon arrival, the delivery executive collects cash at the doorstep and issues `on_status (order_delivered_cod)` setting `payment.status = "PAID"`.

### 2. Slotted & Scheduled Deliveries
In `Slotted_Delivery_Flow`, the merchant presents specific calendar fulfillment windows during `/on_select`. The buyer selects a target slot (`fulfillment.time.range`), which is preserved across `/init`, `/confirm`, and fulfillment scheduling.

### 3. Multi-Option Fulfillment Selection
In `Multi_Option_Fulfillment_Flow`, the seller provides multiple delivery speeds (e.g. Standard 2-day delivery vs 45-minute hyperlocal express) with distinct pricing and TATs. The buyer binds their choice during `/select`.

### 4. In-Store Self-Pickup (Click & Collect)
In `Self_Pickup_Flow`, zero logistics fees are billed. The merchant transitions the order to `self_pick_packed`, after which the consumer presents proof of purchase at the retail counter, culminating in `self_pick_picked`.

### 5. In-Flight Buyer Instructions and Address Updates
In `Buyer_Instructions_And_Delivery_Update_Flow`, buyers submit post-confirmation instructions (`update_buyer_instructions`) and correct delivery destination addresses (`update_delivery_address`) prior to parcel dispatch, followed by delivery authentication OTP dispatch (`on_update_delivery_auth`).

### 6. Item Replacement and Reverse Quality Check (QC)
In `Replacement_Flow`, customers request replacement for damaged/spoiled items. The seller executes an on-doorstep Reverse QC, picks up the defective unit, inspects it at the warehouse (`on_update_return_delivered_rep`), and dispatches a fresh replacement parcel (`on_status_packed_rep` through `order_delivered_rep`).

### 7. Forced and System Cancellations
In `Forced_Cancellation_Flow`, unforeseen merchant stock collapse or courier failure after rider dispatch triggers an unrecoverable cancellation sequence (`cancel_no`, `cancel_yes`, `on_cancel_force`), immediately followed by `/update (update_settlement_cancel)` to refund the consumer.

### 8. Merchant Part-Cancellation and Return to Origin (RTO)
In `RTO_And_Part_Cancellation_Flow`, out-of-stock items are cancelled pre-dispatch via `on_update_part_cancel`. Subsequently, when the customer is unreachable at delivery, the merchant issues an unsolicited `on_cancel_rto` (reason code `013`), updates the settlement trail, and confirms store return via `on_status_rto_delivered`.

### 9. Buyer-Initiated Return and Refund
In `Return_Flow`, buyers initiate returns for eligible returnable grocery items. Merchants review, approve reverse logistics, pick up the goods, and execute full/partial financial refunds via `update_settlement_trail`.

### 10. Out of Stock Handling (Cart Recovery & Immediate Error Code)
- **Cart Recovery (`Out_Of_Stock_Flow`)**: The seller flags out-of-stock items in `/on_select`. The buyer adjusts quantities and re-submits `/select`, successfully proceeding to checkout.
- **Immediate Rejection (`Out_Of_Stock_Flow_Error-code`)**: The seller immediately rejects `/select` with ONDC error code `40002` (Out of Stock) or `30009`.

### 11. Commercial Settlement Model (BNP / SNP Fees)
In `Commercial_Model_For_BNP_SNP_Flow`, explicit settlement rules, Buyer Network Participant finder fees, commission deductions, and statutory withholdings are agreed upon during `/on_select` and `/on_init` and committed at `/confirm`.

### 12. Incremental Catalog Sync (Push and Pull)
- **Incremental Push (`Discovery_Flow_incremental_catalog`)**: Sellers push live differential price/stock updates and store open/close events via unsolicited `/on_search`.
- **Incremental Refresh Pull (`Discovery_Flow_incremental_catalog_refresh_pull`)**: Buyer apps poll for items modified after a specific `last_updated_at` timestamp.

### 13. Statutory Compliance and Catalog Rejection
In `Catalog_Rejection_Flow`, catalogs omitting mandatory statutory declarations (Packaged Commodities rules, manufacturer name, net weight, ingredients, or FSSAI license numbers) are rejected via `catalog_rejection`.

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

### Flow 1: Delivery Flow (Standard Prepaid Home Delivery)

#### 1. Short Description
The standard forward-fulfillment prepaid grocery purchase journey. A buyer selects grocery items, receives an itemized quote with delivery fees and taxes, provides shipping addresses, pays upfront, and receives the goods through seller-managed delivery with live rider tracking and delivery verification.

#### 2. API Breakdown & Technical Actions
- **`/select` (BAP -> BPP)**: The BAP transmits selected item IDs, quantities, store location (`location_id: "L1"`), and delivery coordinates (`fulfillments[0].end.location.gps` and `address.area_code = "560001"`).
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

### Flow 2: Buyer Delivery Flow (Buyer-Managed Logistics)

#### 1. Short Description
Used when the Buyer Application or a 3PL logistics provider contracted by the buyer manages shipping. The merchant prepares and packs the items, after which the buyer application updates pickup progress and signals delivery handover to the merchant.

#### 2. API Breakdown & Technical Actions
- **`/select` -> `/on_select (on_select_buyer_delivery)`**: Selection establishing buyer-managed logistics (zero seller shipping fee).
- **`/init (init_buyer_delivery)` -> `/on_init (on_init_buyer_delivery)`**: Order initialized with buyer pickup intent.
- **`/confirm` -> `/on_confirm`**: Order booked in merchant system.
- **`on_status (on_status_accepted)` [Unsolicited] (BPP -> BAP)**: Merchant accepts order.
- **`on_status (on_status_packed)` [Unsolicited] (BPP -> BAP)**: Groceries packed.
- **`on_status (on_status_ready_to_ship)` [Unsolicited] (BPP -> BAP)**: Merchant notifies BAP that parcels are staged at the store dispatch counter.
- **`/update (update_picked_up)` [Unsolicited] (BAP -> BPP)**: BAP notifies seller that buyer-contracted courier has retrieved the package.
- **`/update (update_delivered)` [Unsolicited] (BAP -> BPP)**: BAP notifies seller that the package has been delivered to the consumer, completing the transaction.

---

### Flow 3: Buyer Instructions and Delivery Update Flow

#### 1. Short Description
Demonstrates in-flight adjustments to an active order. Post-confirmation, the consumer sends specific doorstep handling instructions and modifies their delivery address before dispatch, concluding with delivery authentication OTP handover.

#### 2. API Breakdown & Technical Actions
- **`/select` through `/on_confirm`**: Standard ordering sequence.
- **`on_status (on_status_accepted)` [Unsolicited] (BPP -> BAP)**: Merchant accepts order.
- **`/update (update_buyer_instructions)` (BAP -> BPP)**: Buyer submits specific handling notes (e.g. "Do not ring bell, call on arrival").
- **`/on_update (on_update_buyer_instructions)` (BPP -> BAP)**: Merchant acknowledges and stores instructions.
- **`/update (update_delivery_address)` (BAP -> BPP)**: Buyer submits updated apartment/flat number or landmark coordinates.
- **`/on_update (on_update_delivery_address)` (BPP -> BAP)**: Merchant re-validates serviceability and updates rider waypoint.
- **`on_status` sequence**: Packed -> Agent-assigned -> Picked -> Out-for-delivery.
- **`on_update (on_update_delivery_auth)` [Unsolicited] (BPP -> BAP)**: Merchant generates secure delivery OTP authentication code.
- **`on_status (on_status_order_delivered)` [Unsolicited] (BPP -> BAP)**: Handover completed upon OTP verification.

---

### Flow 4: Cancellation Flow (Buyer-Side Order Cancellation)

#### 1. Short Description
Standard buyer-initiated order cancellation prior to order packing and dispatch, validating merchant cancellation policies, fee calculations, and refund processing.

#### 2. API Breakdown & Technical Actions
- **`/select` through `/on_confirm`**: Buyer places order.
- **`/cancel` (BAP -> BPP)**: Buyer triggers cancellation specifying reason code (e.g. `001` - Buyer change of mind).
- **`/on_cancel` (BPP -> BAP)**: Seller validates cancellation terms (`@ondc/org/cancellable = true`), updates `order.state = "Cancelled"`, recalculates cancellation fee deductions, and confirms refund instructions.

---

### Flow 5: Cash on Delivery Flow (COD Fulfillment)

#### 1. Short Description
Encompasses the entire order lifecycle when Cash on Delivery is chosen. The order is initiated and confirmed without upfront digital payment; the delivery executive collects cash at the doorstep and marks the payment as settled.

#### 2. API Breakdown & Technical Actions
- **`/select` -> `/on_select`**: Item and fulfillment selection.
- **`/init (init_cod)` (BAP -> BPP)**: Buyer selects Pay-on-Delivery (`payment.type = "ON-FULFILLMENT"`).
- **`/on_init (on_init_cod)` (BPP -> BAP)**: Merchant confirms COD availability and terms.
- **`/confirm (confirm_cod)` (BAP -> BPP)**: Order confirmed with `payment.status = "NOT-PAID"`.
- **`/on_confirm (on_confirm_cod)` (BPP -> BAP)**: Order booked.
- **Milestones**: Accepted -> Packed -> Agent-assigned -> Picked -> Track -> Out-for-delivery.
- **`on_status (on_status_order_delivered_cod)` [Unsolicited] (BPP -> BAP)**: Delivery executive receives cash payment, marks `payment.status = "PAID"`, records `Order-delivered`, and closes the order.

---

### Flow 6: Commercial Model for BNP and SNP Flow

#### 1. Short Description
Exercises the commercial fee architecture between Buyer Network Participants (BNP) and Seller Network Participants (SNP), validating finder fees, commission withholding, TCS/TDS statutory tax handling, and settlement terms.

#### 2. API Breakdown & Technical Actions
- **`/select` -> `/on_select (on_select_commercial_model)`**: Quote returned with itemized commercial commission structures and buyer finder fee rates.
- **`/init (init_commercial_model)` -> `/on_init (on_init_commercial_model)`**: Formal terms defined for settlement windows, TDS deductions, and payer/payee bank account specifications.
- **`/confirm (confirm_commercial_model)` -> `/on_confirm (on_confirm_commercial_model)`**: Final order commitment binding the commercial settlement agreement.

---

### Flow 7: Slotted Delivery Flow (Time Slot Scheduling)

#### 1. Short Description
A scheduled fulfillment flow where the consumer books a specific date and time slot for grocery delivery (e.g. morning vs evening slot).

#### 2. API Breakdown & Technical Actions
- **`/select` (BAP -> BPP)**: Buyer queries store availability with delivery preferences.
- **`/on_select (on_select_slotted_delivery)` (BPP -> BAP)**: Merchant returns available calendar time slots (`fulfillment.time.range.start` and `end`) with slot IDs and fees.
- **`/init (init_slotted_delivery)` (BAP -> BPP)**: Buyer selects preferred time slot.
- **`/on_init (on_init_slotted_delivery)` (BPP -> BAP)**: Merchant locks the slot in its dispatch calendar.
- **`/confirm` -> `/on_confirm`**: Order confirmed with selected slot.
- **Fulfillment**: Merchant holds dispatch until scheduled window, triggering `Packed` -> `Agent-assigned` -> `Picked` -> `Track` -> `Out-for-delivery` -> `Order-delivered` within the reserved slot.

---

### Flow 8: Multi-Option Fulfillment Flow (Express / Standard / Same Day)

#### 1. Short Description
Demonstrates multi-option fulfillment where a merchant presents several shipping tiers (e.g. 45-minute Hyperlocal Express vs Standard Next-Day Delivery) with distinct charges and TATs, allowing the consumer to choose.

#### 2. API Breakdown & Technical Actions
- **`/select` -> `/on_select (on_select_multi_fulfillment)`**: Merchant returns multiple fulfillment options (`fulfillments[]`), each with a unique ID, service tier code, fee breakup, and TAT estimate.
- **`/init (init_multi_fulfillment)` (BAP -> BPP)**: Buyer binds their cart to the chosen fulfillment ID.
- **`/on_init (on_init_multi_fulfillment)` (BPP -> BAP)**: Quote frozen based on chosen speed tier.
- **`/confirm` -> `/on_confirm`**: Order finalized.
- **Fulfillment**: Standard milestone tracking through to delivery.

---

### Flow 9: Self-Pickup Flow (Click & Collect)

#### 1. Short Description
A fulfillment flow where the consumer orders groceries online and collects them in person at the local supermarket counter, eliminating delivery charges and rider dispatch.

#### 2. API Breakdown & Technical Actions
- **`/select` -> `/on_select (on_select_self_pickup)`**: Cart configured with `fulfillment.type = "Self-Pickup"` (zero delivery fee).
- **`/init (init_self_pickup)` -> `/on_init (on_init_self_pickup)`**: Store counter location and collection window specified.
- **`/confirm` -> `/on_confirm`**: Order booked.
- **`on_status (on_status_accepted)` [Unsolicited] (BPP -> BAP)**: Merchant accepts order.
- **`on_status (on_status_self_pick_packed)` [Unsolicited] (BPP -> BAP)**: Store staff packs groceries into customer-ready bags and generates pickup OTP/barcode.
- **`on_status (on_status_self_pick_picked)` [Unsolicited] (BPP -> BAP)**: Customer arrives at store, presents pickup verification, collects parcel, and transaction closes.

---

### Flow 10: Replacement Flow (Reverse QC & Item Replacement)

#### 1. Short Description
A complete replacement lifecycle for defective, damaged, or wrong items. The merchant conducts an on-doorstep Reverse QC, picks up the defective item, inspects it at the warehouse, and dispatches a replacement parcel.

#### 2. API Breakdown & Technical Actions
- **Forward Order**: Order delivered via normal steps (1–12).
- **`/update (update_reverse_qc_rep)` (BAP -> BPP)**: Buyer submits replacement request with item ID, reason code, and photos.
- **`/on_update (on_update_interim_reverseQc)` (BPP -> BAP)**: Merchant logs replacement request in `Replacement_Initiated`.
- **`on_update (on_update_return_approved)` [Unsolicited] (BPP -> BAP)**: Merchant approves reverse pickup.
- **`on_update (on_update_return_picked_rep)` [Unsolicited] (BPP -> BAP)**: Courier performs doorstep QC and collects defective goods.
- **`on_update (on_update_return_delivered_rep)` [Unsolicited] (BPP -> BAP)**: Defective item arrives at merchant warehouse and is validated.
- **`on_status (on_status_packed_rep)` [Unsolicited] (BPP -> BAP)**: Fresh replacement item packed.
- **`on_status (on_status_picked_rep)` [Unsolicited] (BPP -> BAP)**: Replacement picked up by rider.
- **`on_status (on_status_out_for_delivery_rep)` [Unsolicited] (BPP -> BAP)**: Replacement en route.
- **`on_status (on_status_order_delivered_rep)` [Unsolicited] (BPP -> BAP)**: Replacement successfully delivered to customer.

---

### Flow 11: Return Flow (Customer-Initiated Return & Refund)

#### 1. Short Description
The post-delivery return lifecycle for eligible returnable grocery items. Buyer initiates return within window, merchant approves, reverse pickup is executed, and refund settlement is concluded.

#### 2. API Breakdown & Technical Actions
- **Forward Order**: Order delivered (steps 1–12).
- **`/update (update_return)` (BAP -> BPP)**: Buyer requests return specifying item, return reason code (e.g. `001` - Defective/Expired), and evidence photos.
- **`/on_update (on_update_return_init)` (BPP -> BAP)**: Merchant logs return request.
- **`on_update (on_update_return_approved)` [Unsolicited] (BPP -> BAP)**: Return authorized.
- **`on_update (on_update_return_picked)` [Unsolicited] (BPP -> BAP)**: Reverse logistics agent collects items.
- **`/update (update_settlement_trail)` (BAP -> BPP)**: Buyer app supplies bank/UPI refund routing instructions.
- **`on_update (on_update_return_delivered)` [Unsolicited] (BPP -> BAP)**: Merchant confirms receipt and releases refund.

---

### Flow 12: RTO and Part-Cancellation Flow

#### 1. Short Description
A complex exception flow combining merchant-side part-cancellation during store picking (due to stock shortage) with an unsuccessful delivery attempt where the buyer is unreachable, leading to Return to Origin (RTO).

#### 2. API Breakdown & Technical Actions
- **Forward Order**: Order placed and confirmed.
- **`on_update (on_update_part_cancel)` [Unsolicited] (BPP -> BAP)**: Merchant cancels unavailable line items pre-dispatch.
- **`/update (update_settlement_trail)` (BAP -> BPP)**: BAP updates settlement trail reflecting partial refund.
- **Dispatch**: Remaining items packed, assigned, picked, and marked out for delivery.
- **`on_cancel (on_cancel_rto)` [Unsolicited] (BPP -> BAP)**: Delivery fails (buyer unreachable / refused delivery), triggering RTO cancellation.
- **`/update (update_settlement_trail_1)` (BAP -> BPP)**: BAP transmits RTO settlement terms (factoring in return shipping costs).
- **`on_status (on_status_rto_delivered)` [Unsolicited] (BPP -> BAP)**: Parcel returned to merchant warehouse.

---

### Flow 13: Forced Cancellation Flow

#### 1. Short Description
Handles emergency forced cancellations triggered by merchant system failures, unresolvable inventory collapse, or transport crises post-dispatch.

#### 2. API Breakdown & Technical Actions
- **Order Pipeline**: Order created, accepted, packed, agent assigned, and picked up.
- **`/cancel (cancel_no)` (BAP -> BPP)**: Buyer attempts soft cancellation; rejected if out for delivery.
- **`/cancel (cancel_yes)` (BAP -> BPP)**: System/emergency forced cancellation triggered.
- **`/on_cancel (on_cancel_force)` (BPP -> BAP)**: Merchant terminates order immediately and confirms cancellation state.
- **`/update (update_settlement_cancel)` (BAP -> BPP)**: BAP executes settlement trail refund to consumer.

---

### Flow 14: Out of Stock Flow (Cart Rebalancing & Recovery)

#### 1. Short Description
Demonstrates cart recovery when an item is identified as out of stock during preliminary selection. The seller returns unavailable status, the buyer adjusts cart quantities or swaps items, and the checkout successfully proceeds.

#### 2. API Breakdown & Technical Actions
- **`/select (select0)` (BAP -> BPP)**: Initial selection of desired items.
- **`/on_select (on_select_out_of_stock)` (BPP -> BAP)**: Seller flags depleted item (`quantity.available.count = 0`).
- **`/select` (BAP -> BPP)**: Buyer adjusts cart to available items.
- **`/on_select` (BPP -> BAP)**: Quote successfully generated.
- **Checkout**: Order confirmed, packed, dispatched, tracked, and delivered.

---

### Flow 15: Out of Stock Flow (Error Code Rejection)

#### 1. Short Description
A lightweight selection rejection flow where the seller immediately denies checkout with standard ONDC error code `40002` (Out of Stock) or `30009`.

#### 2. API Breakdown & Technical Actions
- **`/select` (BAP -> BPP)**: Buyer requests item selection.
- **`/on_select (on_select_out_of_stock)` (BPP -> BAP)**: Seller returns an error block containing code `40002` / `30009` and error descriptor, halting the session.

---

### Flow 16: Discovery Flow – Full Catalog City Discovery

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

### Flow 17: Discovery Flow – Incremental Catalog Push

#### 1. Short Description
Validates the merchant-initiated incremental catalog push mechanism. Sellers broadcast live updates regarding price alterations, flash discounts, stock replenishments, or temporary store closures without requiring a full catalog reload.

#### 2. API Breakdown & Technical Actions
- **`/search (search_inc)` (BAP -> Gateway)**: Preliminary search establishing active listening.
- **`on_search (on_search_inc)` [Unsolicited] (BPP -> BAP)**: Seller pushes differential item pricing or inventory adjustments.
- **`on_search (on_search_inc_close)` [Unsolicited] (BPP -> BAP)**: Seller signals temporary store closure (`serviceability` tags set to disabled for active hours).
- **`on_search (on_search_inc_open)` [Unsolicited] (BPP -> BAP)**: Seller re-enables store operations and serviceability.
- **`/search (search_inc1)` (BAP -> Gateway)**: Verification query confirming catalog state consistency.

---

### Flow 18: Discovery Flow – Incremental Catalog Refresh Pull

#### 1. Short Description
Validates the buyer application pull mechanism for catalog synchronization. The buyer requests catalog updates modified after a given timestamp, enabling efficient bandwidth utilization and consistent local price caches.

#### 2. API Breakdown & Technical Actions
- **`/search (search_1)` -> `/on_search (on_search1)`**: Baseline full catalog discovery.
- **`/search (search_inc_pull)` (BAP -> BPP)**: Targeted point-to-point search passing `tags` with `mode = "incremental_refresh"` and `last_updated_at` timestamp.
- **`/on_search (on_search_inc_pull)` (BPP -> BAP)**: Seller responds containing strictly those grocery items whose pricing, quantity, or metadata changed since the requested cutoff.

---

### Flow 19: Catalog Rejection Flow (Statutory Non-Compliance)

#### 1. Short Description
Validates regulatory safeguards in the grocery domain. When a seller's published catalog fails statutory compliance rules under the Legal Metrology (Packaged Commodities) Rules or FSSAI guidelines, the buyer app automatically rejects the catalog.

#### 2. API Breakdown & Technical Actions
- **`/search` (BAP -> Gateway)**: Discovery query.
- **`/on_search` (BPP -> BAP)**: Seller returns catalog with non-compliant listings (e.g. missing manufacturer declaration, net weight, ingredients, or FSSAI registration number).
- **`catalog_rejection` (BAP Internal / Log)**: Compliance engine flags statutory defects and drops the catalog from buyer search results.

---

### Flow 20: Delivery Flow with IGM 1.0.0 Resolution

#### 1. Short Description
Integrates the complete grocery purchase and fulfillment pipeline with the linear IGM 1.0.0 complaint resolution framework.

#### 2. API Breakdown & Technical Actions
- **Delivery Steps (1–12)**: Order placed, paid, packed, dispatched, and delivered.
- **`/issue (issue_open_100)` (BAP -> BPP)**: Customer files complaint (e.g. damaged parcel packaging) with photo evidence.
- **`/on_issue (on_issue_processing_100)` (BPP -> BAP)**: Seller assigns ticket ID and expected TAT.
- **`on_issue_status (on_issue_resolved_100)` [Unsolicited] (BPP -> BAP)**: Merchant publishes resolution (`RESOLVED`) with credit/refund action.
- **`/issue (issue_close_100)` (BAP -> BPP)**: Buyer verifies resolution and closes the grievance.

---

### Flow 21: Delivery Flow with IGM 2.0.0 – Evidence Exchange & Replacement

#### 1. Short Description
Advanced IGM 2.0.0 interaction featuring dynamic evidence gathering. The seller requests additional verification pictures, the buyer provides them, and the seller issues an automated item replacement fulfillment.

#### 2. API Breakdown & Technical Actions
- **Delivery Steps (1–12)**: Order delivered.
- **`/issue (issue_open)` (BAP -> BPP)**: Customer files complaint citing wrong item delivered.
- **`/on_issue (on_issue_processing)` (BPP -> BAP)**: Complaint acknowledged.
- **`on_issue (on_issue_need_more_info)` [Unsolicited] (BPP -> BAP)**: Seller requests batch label and barcode photo.
- **`/issue (issue_info_provided)` (BAP -> BPP)**: Buyer uploads requested photos.
- **`/on_issue (on_issue_provided)` (BPP -> BAP)**: Seller acknowledges receipt of evidence.
- **`on_issue (on_issue_resolution)` [Unsolicited] (BPP -> BAP)**: Seller validates proof and proposes item replacement (`action_triggered = "REPLACEMENT"`).
- **`/issue (issue_resolution_accept)` (BAP -> BPP)**: Buyer accepts resolution.
- **`/on_issue (on_issue_resolved)` -> `/issue (issue_close)`**: Ticket closed as resolved.
- **`on_update (on_update_igm_replacement)` [Unsolicited] (BPP -> BAP)**: Seller automatically generates replacement fulfillment order.

---

### Flow 22: Delivery Flow with IGM 2.0.0 – Resolution Accepted (No Action)

#### 1. Short Description
Demonstrates IGM 2.0.0 handling where a customer complaint is investigated, a formal operational clarification is provided without secondary physical actions (`NO_ACTION`), and the customer accepts the resolution.

#### 2. API Breakdown & Technical Actions
- **Delivery Steps (1–14)**: Order placed, delivered, and live-tracked.
- **`/issue (issue_open_2)` (BAP -> BPP)**: Customer registers grievance.
- **`/on_issue (on_issue_processing)` (BPP -> BAP)**: Grievance under investigation.
- **`on_issue (on_issue_resolution_igm_3)` [Unsolicited] (BPP -> BAP)**: Seller provides resolution with detailed explanation (`action_triggered = "NO_ACTION"`).
- **`/issue (issue_resolution_accept_igm_3)` (BAP -> BPP)**: Customer accepts explanation.
- **`/on_issue (on_issue_resolved_igm_3)` -> `/issue (issue_close_igm_3)`**: Grievance closed.
- **`on_status (on_status_igm_3)` [Unsolicited] (BPP -> BAP)**: Order audit status finalized.

---

### Flow 23: Delivery Flow with IGM 2.0.0 – Dispute Escalation & Mandated Return

#### 1. Short Description
A multi-tier grievance escalation workflow under IGM 2.0.0. The buyer rejects initial merchant resolutions, escalates the complaint to higher dispute resolution authorities (Level 2 Grievance Officer / Arbitrator), achieves a binding resolution, and executes an official return.

#### 2. API Breakdown & Technical Actions
- **Delivery Steps (1–12)**: Order completed.
- **`/issue (issue_open)` -> `/on_issue (processing)`**: Initial grievance filed.
- **`on_issue (on_issue_resolution)` [Unsolicited] (BPP -> BAP)**: Seller proposes initial settlement.
- **`/issue (issue_resolution_reject)` (BAP -> BPP)**: Buyer rejects resolution.
- **`/on_issue (on_issue_processing_1)` -> `on_issue (on_issue_resolution_1)`**: Seller reconsiders.
- **`/issue (issue_escalate)` (BAP -> BPP)**: Buyer escalates dispute to Level 2 Grievance Redressal Officer.
- **`/on_issue (on_issue_processing_2)` -> `on_issue (on_issue_resolution_2)`**: Arbitrator / GRO issues binding resolution.
- **`/issue (issue_resolution_accept)` (BAP -> BPP)**: Resolution accepted.
- **`/on_issue (on_issue_resolved)` -> `/issue (issue_close)`**: Grievance officially marked resolved.
- **`on_update (on_update_igm_return)` [Unsolicited] (BPP -> BAP)**: Mandated return and refund workflow executed for contested items.

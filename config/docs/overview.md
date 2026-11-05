# Retail Electronics (ONDC:RET14 1.2.5)

- [Overview](#overview)
- [Participants](#participants)
- [The User Journey](#the-user-journey)
  - [1. Discovery and Catalog Search](#1-discovery-and-catalog-search)
  - [2. Model/Specification Selection and Serviceability Check](#2-modelspecification-selection-and-serviceability-check)
  - [3. Order Initialization and Shipping Configuration](#3-order-initialization-and-shipping-configuration)
  - [4. Order Confirmation and Prepaid Escrow](#4-order-confirmation-and-prepaid-escrow)
  - [5. Order Processing, Picking, and Serial Number Verification](#5-order-processing-picking-and-serial-number-verification)
  - [6. Logistics and Secure Courier Assignment](#6-logistics-and-secure-courier-assignment)
  - [7. Order Dispatch, In-Flight Tracking, and Secure Delivery](#7-order-dispatch-in-flight-tracking-and-secure-delivery)
  - [8. Settlement and Post-Fulfillment](#8-settlement-and-post-fulfillment)
- [Additional Scenarios in Version 1.2.5](#additional-scenarios-in-version-125)
  - [1. Text Customization and Hardware Personalization](#1-text-customization-and-hardware-personalization)
  - [2. Purchase Financing, Consumer Credit, and EMI Checkout](#2-purchase-financing-consumer-credit-and-emi-checkout)
  - [3. Seller Network Participant (SNP) Payment Collection](#3-seller-network-participant-snp-payment-collection)
  - [4. Dedicated Post-Order Hardware Replacement Workflow](#4-dedicated-post-order-hardware-replacement-workflow)
  - [5. Buyer-Initiated Return and Reverse QC Pickup](#5-buyer-initiated-return-and-reverse-qc-pickup)
  - [6. Buyer-Side Order Cancellation](#6-buyer-side-order-cancellation)
  - [7. Merchant-Side Part-Cancellation and Return to Origin (RTO)](#7-merchant-side-part-cancellation-and-return-to-origin-rto)
  - [8. In-Transit Force Cancellation and Settlement](#8-in-transit-force-cancellation-and-settlement)
  - [9. Out of Stock Handling: Cart Recovery vs. Protocol Error Code](#9-out-of-stock-handling-cart-recovery-vs-protocol-error-code)
  - [10. Incremental Catalog Refresh (Push and Pull)](#10-incremental-catalog-refresh-push-and-pull)
  - [11. Statutory Compliance, BIS Certification, and E-Waste Regulations](#11-statutory-compliance-bis-certification-and-e-waste-regulations)
- [Issue and Grievance Management](#issue-and-grievance-management)
  - [1. IGM 1.0.0 Architecture](#1-igm-100-architecture)
  - [2. IGM 2.0.0 Architecture](#2-igm-200-architecture)
- [Detailed Protocol Flows](#detailed-protocol-flows)
  - [Flow 1: Delivery Flow (Standard Forward Fulfillment)](#flow-1-delivery-flow-standard-forward-fulfillment)
  - [Flow 2: Customization Input Text Flow](#flow-2-customization-input-text-flow)
  - [Flow 3: Purchase Finance Flow](#flow-3-purchase-finance-flow)
  - [Flow 4: SNP Collecting Payment Flow](#flow-4-snp-collecting-payment-flow)
  - [Flow 5: Replacement Flow (Hardware Reverse QC and Reshipment)](#flow-5-replacement-flow-hardware-reverse-qc-and-reshipment)
  - [Flow 6: Return Flow (Post-Delivery Return and Refund)](#flow-6-return-flow-post-delivery-return-and-refund)
  - [Flow 7: Buyer Cancellation Flow](#flow-7-buyer-cancellation-flow)
  - [Flow 8: Seller Cancellation Flow (Warehouse Part-Cancellation and RTO)](#flow-8-seller-cancellation-flow-warehouse-part-cancellation-and-rto)
  - [Flow 9: Force Cancellation Flow (In-Transit Cancellation)](#flow-9-force-cancellation-flow-in-transit-cancellation)
  - [Flow 10: Out of Stock Flow (Cart Modification Recovery)](#flow-10-out-of-stock-flow-cart-modification-recovery)
  - [Flow 11: Out of Stock Flow (Immediate Error Code)](#flow-11-out-of-stock-flow-immediate-error-code)
  - [Flow 12: Discovery Flow: Full Catalog City Broadcast](#flow-12-discovery-flow-full-catalog-city-broadcast)
  - [Flow 13: Discovery Flow: Incremental Catalog Push and Disablement](#flow-13-discovery-flow-incremental-catalog-push-and-disablement)
  - [Flow 14: Discovery Flow: Incremental Catalog Refresh Pull](#flow-14-discovery-flow-incremental-catalog-refresh-pull)
  - [Flow 15: Delivery Flow with IGM 1.0.0 Dispute Resolution](#flow-15-delivery-flow-with-igm-100-dispute-resolution)
  - [Flow 16: Delivery Flow with IGM 2.0.0: Evidence Exchange and Replacement](#flow-16-delivery-flow-with-igm-200-evidence-exchange-and-replacement)
  - [Flow 17: Delivery Flow with IGM 2.0.0: Resolution Accepted (No Action)](#flow-17-delivery-flow-with-igm-200-resolution-accepted-no-action)
  - [Flow 18: Delivery Flow with IGM 2.0.0: Rejection, Escalation and Replacement](#flow-18-delivery-flow-with-igm-200-rejection-escalation-and-replacement)

---

## Overview

The Consumer Electronics domain (**ONDC:RET14**, specification version **1.2.5**) defines an open, interoperable digital commerce standard for consumer electronics, personal computing devices, mobile communications, home entertainment systems, smart domestic appliances, wearables, gaming hardware, and audio gear across the Open Network for Digital Commerce (ONDC). Electronics retail is characterized by high average order values (AOV), specification-driven purchasing choices, strict anti-fraud safeguards, fragile transit logistics, and comprehensive statutory regulations.

Specification version **1.2.5** expands the foundational retail architecture with dedicated high-value electronics capabilities:
1. **Hardware Text Customization**: Enabling bespoke laser engraving (e.g. customized names or serial dedications on laptop chassis, tablet backs, or earbuds) and custom configuration directives captured seamlessly during cart selection.
2. **Purchase Financing & EMI Checkout**: Direct protocol support for consumer credit, Equated Monthly Installments (EMI), and Buy-Now-Pay-Later (BNPL) integrations to accommodate high-ticket electronics purchases.
3. **Seller Network Participant (SNP) Payment Collection**: Enabling sellers to collect payments directly via their own payment gateways or merchant accounts rather than exclusively relying on BAP escrow capture.
4. **Dedicated Hardware Replacement Lifecycle**: A specialized 21-step post-delivery replacement workflow incorporating interim reverse QC evaluation, doorstep serial number / IMEI verification, reverse transport, and outbound dispatch of a replacement unit.
5. **In-Transit Forced Cancellation**: Formalized procedures for terminating delivery when a shipment is already out for delivery, with automated settlement reconciliation.
6. **Store Disablement Broadcasting**: Real-time push notifications signaling merchant operational shutdowns, temporary maintenance, or localized service cutoffs.

ONDC unbundles the traditionally closed e-commerce marketplace landscape. Shoppers can search and compare electronics across authorized brand stores, regional superstores, independent appliance dealers, and local electronics retailers using their preferred **Buyer Application (BAP)**. Sellers manage their inventory, serial numbers, warranty terms, and transparent pricing through a **Seller Application (BPP)**, while specialized **Logistics Service Providers (LSPs)** execute high-security parcel transit with live tracking, doorstep OTP authentication, and reverse logistics quality checks.

The protocol standardizes all network interactions across:
- **Discovery**: `/search` and `/on_search` (city-wide broadcast queries, category taxonomies, variant hierarchies, technical specifications, and incremental catalog push/pull).
- **Ordering**: `/select`, `/on_select`, `/init`, `/on_init`, `/confirm`, and `/on_confirm`.
- **Fulfillment & Real-time Tracking**: Unsolicited `/on_status` lifecycle events (`Accepted`, `Packed`, `Agent-assigned`, `Order-picked-up`, `Out-for-delivery`, `Order-delivered`), `/track`, and `/on_track`.
- **Post-Order Lifecycle & Exceptions**: `/update`, `/on_update`, `/cancel`, and `/on_cancel` (doorstep quality-checked returns, reverse logistics pickup, warehouse bench testing, merchant part-cancellations, in-transit forced cancellations, and Return to Origin / RTO).
- **Grievance Redressal**: Issue and Grievance Management under both **IGM 1.0.0** and **IGM 2.0.0** architectures.

---

## Participants

| Participant | What This Means |
|---|---|
| **Buyer Application (BAP)** | The consumer-facing digital application (e.g., tech marketplace apps, banking portals, super-apps, telco commerce platforms) where shoppers browse electronics catalogs, filter by technical hardware specs, select customization options, apply for purchase financing, configure delivery addresses, complete prepaid payments, track courier transit in real time, and raise returns or grievances. |
| **Seller Application (BPP)** | An application representing electronics retail chains, direct-to-consumer (D2C) hardware brands, authorized distributors, regional appliance dealerships, or refurbished electronics merchants. The BPP publishes item catalogs with variant attributes (storage, RAM, color, screen size), checks delivery serviceability, calculates quotes with customization surcharges, manages serial number / IMEI registration during packing, coordinates consumer financing terms, and executes reverse QC inspections. |
| **Logistics Service Provider (LSP)** | A delivery network participant that executes fragile and high-value cargo transport (hyperlocal courier or intercity surface/air parcel shipping). In seller-managed logistics, the BPP or its integrated delivery partner allocates couriers, provides live GPS tracking, captures secure OTP delivery verification, and executes reverse logistics pickups with doorstep physical checks. |
| **Gateway** | The ONDC routing infrastructure that multicasts broadcast discovery requests (`/search`) from BAPs to active seller applications (BPPs) based on domain code (`ONDC:RET14`), city code (e.g. `std:080`), and geolocation parameters. |

---

## The User Journey

The standard electronics ordering journey (`Delivery_Flow`) enables a consumer to search for electronic devices, compare technical specifications and warranties, review transparent price breakdowns and turnaround times, provide delivery coordinates, complete prepaid payment, and receive securely packaged hardware with continuous shipment tracking.

### 1. Discovery and Catalog Search

The buyer initiates discovery on the BAP by searching for electronics products, device models, or appliance categories (e.g., "OLED TV 55 inch", "Laptops 16GB RAM", "Smartphones", "Direct Cool Refrigerators"):

- **Intent Broadcast**: The BAP transmits an asynchronous `/search` request via the ONDC Gateway specifying domain `ONDC:RET14`, buyer geolocation coordinates, city code, and fulfillment type (`Delivery`).
- **Catalog Delivery**: Active BPPs within the serviceable area respond with asynchronous `/on_search` payloads containing their store catalog (`bpp/providers[]`). This includes product categories, custom menu groupings, brand metadata, model numbers, hardware specifications (processor, memory, display dimensions, energy star ratings), MRP, discounted selling price, stock availability, warranty disclosure (manufacturer vs. seller warranty), customization capabilities, and statutory Legal Metrology attributes.

### 2. Model/Specification Selection and Serviceability Check

The buyer selects an exact electronics item or variant (e.g., 256GB Midnight Black Smartphone) and proceeds to configure checkout:

- **Network interaction:**
  - **`/select` (BAP -> BPP)**: The BAP transmits the selected item ID, variant specifications, quantity, provider location ID, and delivery destination coordinates (`fulfillments[0].end.location.gps` and `address.area_code`).
  - **`/on_select` (BPP -> BAP)**: The seller validates real-time inventory at the fulfillment node, confirms delivery serviceability, and computes a detailed quote breakdown (`quote.breakup[]`). This includes the hardware base price, applicable taxes (CGST/SGST), protective packaging / wooden crate fees (for large panels or fragile electronics), logistics shipping charges, and estimated turnaround time (`@ondc/org/TAT`). If the requested device or variant is depleted, the seller responds with an out-of-stock protocol error code (`40002` or `30009`).

### 3. Order Initialization and Shipping Configuration

The buyer confirms recipient information and finalized delivery coordinates:

- **Network interaction:**
  - **`/init` (BAP -> BPP)**: The BAP transmits customer details (name, phone number, email), exact street address, billing information, delivery instructions (e.g., gate code, fragile handling reminder), and payment preference.
  - **`/on_init` (BPP -> BAP)**: The seller freezes the item quote and turnaround time, specifies static and dynamic order terms (cancellation window, return eligibility duration, brand warranty registration link), establishes payment collection requirements (prepaid BAP-collected transaction or SNP-collected gateway flow), and returns settlement fee details.

### 4. Order Confirmation and Prepaid Escrow

Because consumer electronics represent high-value merchandise, transactions follow a prepaid escrow model:

- **Network interaction:**
  - **`/confirm` (BAP -> BPP)**: The BAP captures digital payment from the buyer via UPI, credit card, net banking, or consumer finance/EMI, generates a unique order identifier (`order.id`), and transmits payment confirmation parameters (`payment.params.transaction_id`, `payment.status = "PAID"`, `payment.type = "PRE-PAID"`).
  - **`/on_confirm` (BPP -> BAP)**: The seller validates payment receipt, records the order in its Warehouse Management / Order Management System (WMS/OMS), initializes order state (`order.state = "Created"`), and confirms order creation.

### 5. Order Processing, Picking, and Serial Number Verification

The seller initiates warehouse fulfillment operations:

- The warehouse picks the device from secured high-value inventory cages.
- The merchant scans and registers the unit's unique serial number, IMEI, or MAC address against the order record to safeguard against return fraud.
- The device undergoes protective packaging: anti-static shielding, multi-layer bubble wrap, edge guards for screens, and tamper-evident security tape.
- **Protocol Status Progression:**
  - **`on_status (on_status_pending)` [Unsolicited] (BPP -> BAP)**: Merchant system acknowledges order processing; `order.state` advances to `Accepted`.
  - **`on_status (on_status_packed)` [Unsolicited] (BPP -> BAP)**: Unit is securely packaged with invoice and warranty card inside; `fulfillment.state` updates to `Packed` and `order.state` to `In-progress`.

### 6. Logistics and Secure Courier Assignment

The seller or its integrated Logistics Service Provider assigns a delivery courier:

- A delivery agent equipped for high-value parcel handling is allocated to the shipment.
- **Protocol Status Progression:**
  - **`on_status (on_status_agent_assigned)` [Unsolicited] (BPP -> BAP)**: Courier details (agent name, masked phone number, vehicle type) are transmitted; `order.state` remains `In-progress`.
  - **`on_status (on_status_picked)` [Unsolicited] (BPP -> BAP)**: Courier verifies parcel integrity, scans airway bill barcode, and takes physical custody; `order.state` remains `In-progress`.

### 7. Order Dispatch, In-Flight Tracking, and Secure Delivery

The shipment moves through the transit hub network toward the buyer's doorstep:

- **Real-Time Tracking:**
  - **`/track` (BAP -> BPP)**: The BAP queries live shipment coordinates.
  - **`/on_track` (BPP -> BAP)**: The BPP or LSP returns real-time GPS telemetry and an active web tracking URL (`tracking.url`).
- **Doorstep Authentication & Handover:**
  - **`on_status (on_status_out_for_delivery)` [Unsolicited] (BPP -> BAP)**: Courier is in the immediate vicinity; `order.state` remains `In-progress`.
  - At the doorstep, the delivery agent requests a secure one-time password (OTP) generated on the buyer's app to verify identity prior to handing over the high-value electronics package. The agent may also inspect external box seals in the customer's presence.
  - **`on_status (on_status_order_delivered)` [Unsolicited] (BPP -> BAP)**: Successful handover is confirmed; `order.state` transitions to terminal state `Completed`.

### 8. Settlement and Post-Fulfillment

Upon successful delivery completion:
- The return window countdown timer begins (typically 7 to 10 days for electronics, subject to seller policy).
- The BAP releases funds from escrow to the seller's account net of network fees, taxes, and logistics charges in accordance with ONDC settlement guidelines.
- The buyer receives a tax invoice enabling registration with authorized brand service centers for the manufacturer's warranty.

---

## Additional Scenarios in Version 1.2.5

Version 1.2.5 introduces expanded capabilities specifically tailored to electronics commerce, including customization, installment financing, SNP-collected payments, dedicated hardware replacements, and in-transit force cancellations.

### 1. Text Customization and Hardware Personalization

Consumer electronics frequently offer personalized finishes such as laser engraving or custom configuration options (`Customization_Input_Text_Flow`):

- **Custom Input Capture (`/select` - `select_input`)**: During cart selection, the buyer provides customized text (e.g., custom name, motto, or gift message) via tagged configuration attributes.
- **Customization Pricing & Serviceability (`/on_select` - `on_select_input`)**: The seller evaluates the requested customization, validates text length and content restrictions, calculates any customization surcharge in the itemized quote (`quote.breakup[]`), and confirms delivery timelines.
- **Fulfillment with Custom Manufacturing**: The warehouse schedules engraving before packaging, and the order progresses through standard fulfillment to `Completed`.

### 2. Purchase Financing, Consumer Credit, and EMI Checkout

High-value electronics (laptops, premium smartphones, smart televisions) rely heavily on Equated Monthly Installment (EMI) and Buy-Now-Pay-Later (BNPL) credit models (`Purchase_Finance_Flow`):

- **Financing Terms Initialization (`/init` - `init_fin`)**: The buyer chooses a consumer credit or financing payment method, specifying preferred tenure (e.g., 3, 6, 9, or 12 months), down payment amount, and NBFC / lending partner details.
- **Credit Schedule & Interest Quote (`/on_init` - `on_init_fin`)**: The seller responds with frozen financing parameters, including installment schedules, monthly interest rates, processing fees, and loan sanction terms.
- **Financed Order Confirmation (`/confirm` - `confirm_fin`)**: Upon successful loan sanction and down payment capture, the BAP confirms the order, passing the financier transaction identifier. Fulfillment proceeds with progressive tracking.

### 3. Seller Network Participant (SNP) Payment Collection

In addition to standard BAP-collected escrow payments, version 1.2.5 explicitly supports direct payment collection by the Seller Network Participant (`SNP_Collecting_Payment_Flow`):

- **SNP Gateway Routing (`/on_init` - `on_init_snp` & `on_init_snp_unsolicited`)**: The seller indicates that payment collection is handled directly by the BPP / seller gateway. The seller emits an unsolicited callback containing a direct payment gateway checkout URL or tokenized payment request.
- **SNP Payment Confirmation (`/confirm` - `confirm_snp`)**: The buyer completes payment on the seller-hosted gateway, and the BAP conveys payment verification parameters to the BPP to finalize order creation.

### 4. Dedicated Post-Order Hardware Replacement Workflow

Unlike simple returns for refund, defective or dead-on-arrival (DOA) electronic devices often trigger a hardware replacement workflow (`Replacement_Flow`):

- **Replacement Request with Reverse QC (`/update` - `update_reverse_qc_rep`)**: After delivery, the buyer requests a replacement citing hardware failure, uploading photo evidence and serial numbers.
- **Interim Reverse QC & Approval (`/on_update` - `on_update_interim_reverseQc` & `on_update_return_approved`)**: The seller reviews preliminary evidence and authorizes a doorstep reverse QC pickup.
- **Reverse Pickup & Warehouse Receipt (`on_update_return_picked_rep` & `on_update_return_delivered_rep`)**: A reverse logistics courier collects the defective unit after verifying that the serial number/IMEI matches the dispatch record and that no unauthorized tampering occurred.
- **Replacement Unit Reshipment (`on_status_packed_rep` to `on_status_order_delivered_rep`)**: Once the return is accepted, the seller initiates a replacement fulfillment leg: packing a brand-new replacement unit, assigning a courier, and delivering it to the buyer with end-to-end status tracking.

### 5. Buyer-Initiated Return and Reverse QC Pickup

For orders eligible for refund rather than replacement (`Return_Flow`):

- **Return Initiation & Evaluation (`/update` - `update_return` & `on_update_return_init`)**: The buyer requests a return for refund within the allowed return policy window.
- **Doorstep Reverse QC (`on_update_return_picked`)**: A reverse logistics agent conducts physical and technical checks (IMEI match, screen check, power test, accessories included).
- **Settlement Trail Disbursement (`update_settlement_trail` & `on_update_return_delivered`)**: When the device is received and validated at the merchant facility, the seller releases the refund settlement to the buyer.

### 6. Buyer-Side Order Cancellation

Pre-dispatch cancellation initiated by the consumer (`Buyer_Cancellation_Flow`):

- **Cancellation Request (`/cancel`)**: The buyer triggers order cancellation prior to courier pickup, providing a standardized cancellation reason code (e.g., `001` for accidental order).
- **Merchant Acknowledgment (`/on_cancel`)**: The BPP verifies that the order is cancellable (`@ondc/org/cancellable = true`), terminates warehouse picking, transitions `order.state = "Cancelled"`, and triggers an automated full refund.

### 7. Merchant-Side Part-Cancellation and Return to Origin (RTO)

A dual-exception lifecycle (`Seller_Cancellation_Flow`) handling warehouse picking discrepancies and delivery failures:

- **Warehouse Part-Cancellation (`on_update` - `on_update_part_cancel`)**: The merchant discovers during picking that one specific item or peripheral is damaged or out of stock. The seller cancels that line item via an unsolicited update, and the BAP adjusts the settlement trail (`update_partial_cancel_settlement`).
- **Outbound Fulfillment**: Remaining serviceable items are dispatched to `Out-for-delivery`.
- **Doorstep Delivery Failure & RTO (`on_cancel_rto` & `on_status_rto_delivereddisposed`)**: If the buyer is unreachable or refuses delivery, the courier initiates RTO. The goods return to the origin warehouse or are disposed of per agreement, and the order is marked `Cancelled`.

### 8. In-Transit Force Cancellation and Settlement

In exceptional circumstances where a buyer insists on cancelling while goods are already in transit (`Force_Cancellation_Flow`):

- **Initial Attempt & Policy Enforcement (`/cancel` - `cancel_no`)**: The buyer requests cancellation while the shipment is `Out-for-delivery`. The system initially rejects the cancellation because the parcel is in active transit.
- **Forced Cancellation Override (`/cancel` - `cancel_yes` & `/on_cancel` - `on_cancel_yes`)**: The buyer or network authority invokes a forced cancellation override citing a critical valid reason code. The seller halts delivery, instructs the courier to turn back, marks the order `Cancelled`, and the BAP coordinates an immediate cancellation settlement update (`update_settlement_cancel`).

### 9. Out of Stock Handling: Cart Recovery vs. Protocol Error Code

When inventory for a specific device model, color, or storage configuration is depleted:

- **Cart Recovery Path (`Out_Of_Stock_Flow`)**: The buyer selects an out-of-stock item. On receiving the shortage notice, the buyer modifies the selection to an alternative model or available variant within the same transaction session, proceeds to order placement, and completes fulfillment with live tracking.
- **Immediate Error Code Path (`Out_Of_Stock_Flow(Error-code)`)**: When an item or variant is unavailable and no substitution occurs, the BPP immediately rejects the `/select` call on `/on_select` with error code `40002` (Out of Stock) or `30009`, allowing the buyer app to display clear unavailable badges.

### 10. Incremental Catalog Refresh (Push and Pull)

Electronics catalogs experience rapid price drops, flash discounts, new model releases, and store schedule updates:

- **Incremental Push (`Discovery_Flow_incremental_catalog`)**: The seller proactively publishes catalog delta updates via unsolicited `/on_search` payloads containing modified items and pricing. In version 1.2.5, sellers can also broadcast store disablement notifications (`on_search_inc_disable`) to temporarily pause ordering during stocktaking or emergencies.
- **Incremental Pull (`Discovery_Flow_incremental_catalog_refresh_pull`)**: The buyer app periodically polls for catalog changes by transmitting a `/search` request with tag `catalog_inc = "true"` and a timestamp filter, receiving only modified products.

### 11. Statutory Compliance, BIS Certification, and E-Waste Regulations

Retail electronics listings on ONDC are subject to strict Indian regulatory and consumer protection standards:

- **BIS Compulsory Registration Scheme (CRS)**: Under Ministry of Electronics and Information Technology (MeitY) guidelines, consumer electronic products (laptops, tablets, mobile phones, power adapters, LED displays) must have valid Bureau of Indian Standards (BIS) CRS registration numbers displayed in catalog metadata.
- **BEE Star Labeling**: The Bureau of Energy Efficiency mandates energy consumption star ratings (1 to 5 stars) for major appliances including refrigerators, air conditioners, ceiling fans, and televisions. BPPs must include the appliance star rating, annual electricity consumption (kWh), and energy label validity year.
- **E-Waste (Management) Rules, 2022**: Sellers and manufacturers must disclose Extended Producer Responsibility (EPR) registration details, safe disposal instructions, and authorized collection center / take-back channels in compliance with Central Pollution Control Board (CPCB) directives.
- **Legal Metrology (Packaged Commodities) Rules, 2011**: Product listings must explicitly publish the country of origin, manufacturer and importer details, date of manufacture/import, Maximum Retail Price (MRP inclusive of all taxes), net dimensions, gross weight, and customer grievance redressal contact information.

---

## Issue and Grievance Management

ONDC specifies structured dispute resolution mechanisms to handle post-order grievances—such as damaged packaging, dead-on-arrival devices, missing accessories, or delayed deliveries—under both **IGM 1.0.0** and **IGM 2.0.0** architectures.

### 1. IGM 1.0.0 Architecture

IGM 1.0.0 provides a single-ticket grievance lifecycle between the buyer application and seller application:

- **Issue Filing (`/issue` - `issue_open_100`)**: The buyer submits a formal grievance via the BAP specifying the complaint category, subcategory, narrative description, and contact details.
- **Issue Acknowledgment (`/on_issue` - `on_issue_processing_100`)**: The BPP acknowledges the issue, assigns an internal ticket identifier, and furnishes the details of the designated Grievance Officer.
- **Issue Resolution (`on_issue_status` [Unsolicited] - `on_issue_resolved_100`)**: The seller investigates the claim and publishes a resolution payload detailing the remedial action taken (e.g., dispatching a replacement power cable or approving a partial refund).
- **Issue Closure (`/issue` - `issue_close_100`)**: The buyer verifies that the grievance has been satisfactorily addressed and emits an issue closure message.

### 2. IGM 2.0.0 Architecture

IGM 2.0.0 introduces a robust, multi-participant, role-based dispute framework featuring evidence exchange, diagnostic data submission, multiple resolution remedies (`REFUND`, `REPLACEMENT`, `NO_ACTION`), and formal escalation paths to Level 2 Grievance Officers and Network Intermediaries:

1. **Evidence Exchange & Hardware Replacement (`Delivery_Flow_With_IGM(v-2.0.0)`)**:
   - The buyer lodges a grievance reporting that a newly delivered laptop will not power on (Dead-on-Arrival).
   - Rather than immediate rejection, the BPP requests additional verification via an unsolicited `on_issue` (`on_issue_need_more_info`), requesting photographs of the serial number / IMEI sticker on the bottom chassis and a video of the charging LED indicator.
   - The buyer provides the requested media URLs via `/issue` (`issue_info_provided`).
   - The seller's technical team validates the defect and issues an unsolicited resolution approving an item `REPLACEMENT`.
   - The buyer accepts the replacement resolution, and the seller executes an unsolicited `on_status` synchronizing the order audit record.

2. **Resolution Accepted with `NO_ACTION` (`Delivery_Flow_With_IGM_No_Action(v-2.0.0)`)**:
   - The buyer opens a grievance alleging a technical fault (e.g., smart TV display resolution mismatch).
   - The merchant examines device specifications and determines that the television operates strictly within manufacturer specifications and that the customer is feeding an incompatible signal source.
   - The seller issues an unsolicited `on_issue` with resolution action `NO_ACTION`, accompanied by detailed technical guidance and configuration instructions.
   - The buyer accepts the technical explanation (`/issue`), the ticket is closed, and the seller synchronizes the final order audit record via an unsolicited `on_status`.

3. **Rejection, Level 2 Escalation & Replacement Ruling (`Delivery_Flow_With_IGM_Rejection(v-2.0.0)`)**:
   - The buyer reports physical casing damage upon delivery.
   - The merchant initially proposes a minor cosmetic coupon or nominal discount.
   - The buyer rejects the resolution (`issue_resolution_reject`).
   - The merchant attempts a revised proposal, which the buyer also rejects, subsequently escalating the dispute to a Level 2 Grievance Officer / Network Intermediary (`issue_escalate`).
   - The escalated mediator reviews unboxing photos and delivery timestamps, ruling in favor of the buyer and ordering full product replacement.
   - The buyer accepts the escalated ruling, the dispute is closed, and the seller dispatches a replacement parcel with reverse collection via an unsolicited `on_update` (`on_update_igm_replacement`).

---

## Detailed Protocol Flows

All **18 protocol flows** defined in `automation-specifications/config/flows/index.yaml` for the Electronics domain (`ONDC:RET14 1.2.5`) are detailed below with their classification tags, operational contexts, and full step-by-step API message sequences.

---

### Flow 1: Delivery Flow (Standard Forward Fulfillment)

- **Flow ID:** `Delivery_Flow`
- **Config File:** `./ELECTRONICS/Delivery_Flow.yaml`
- **Protocol Version:** `1.2.5`
- **Use Case:** `ELECTRONICS`
- **Tags:** `PRAMAAN`, `MANDATORY`, `REPORTABLE`, `WORKBENCH`

#### 1. Short Description
The baseline forward fulfillment lifecycle for consumer electronics in version 1.2.5. Covers product selection, delivery quote verification, order initialization, prepaid payment capture, warehouse picking with serial number logging, progressive status updates, live tracking telemetry, and OTP-authenticated doorstep delivery.

#### 2. API Breakdown & Technical Actions
- **Step 1: `/select (select)` (BAP -> BPP)**: The BAP selects electronics products from the seller's catalog, specifying delivery destination coordinates and fulfillment type.
- **Step 2: `/on_select (on_select)` (BPP -> BAP)**: The seller validates real-time inventory, confirms fulfillment serviceability (`Fulfillment: Serviceable`), and returns an itemized price quote (`quote.breakup[]`) with delivery turnaround time.
- **Step 3: `/init (init)` (BAP -> BPP)**: The BAP transmits customer details, billing address, exact delivery location, and payment preference to initiate the order draft.
- **Step 4: `/on_init (on_init)` (BPP -> BAP)**: The seller responds with frozen commercial terms, payment parameters, cancellation windows, and settlement rules.
- **Step 5: `/confirm (confirm)` (BAP -> BPP)**: The BAP captures prepaid digital payment and submits the confirmed order with `order.state = "Created"`.
- **Step 6: `/on_confirm (on_confirm)` (BPP -> BAP)**: The seller validates payment, records the order in OMS/WMS, and confirms `order.state = "Created"`.
- **Step 7: `on_status (on_status_pending)` [Unsolicited] (BPP -> BAP)**: The merchant confirms warehouse order processing; `order.state` transitions to `Accepted`.
- **Step 8: `on_status (on_status_packed)` [Unsolicited] (BPP -> BAP)**: The unit is picked from secured storage, serial number/IMEI recorded, and securely packaged with tamper seals; `fulfillment.state` updates to `Packed` and `order.state` to `In-progress`.
- **Step 9: `on_status (on_status_agent_assigned)` [Unsolicited] (BPP -> BAP)**: A logistics courier is assigned for parcel transport; `order.state` remains `In-progress`.
- **Step 10: `on_status (on_status_picked)` [Unsolicited] (BPP -> BAP)**: The courier picks up the package from the merchant warehouse; `order.state` remains `In-progress`.
- **Step 11: `/track (track)` (BAP -> BPP)**: The BAP queries live in-transit location telemetry.
- **Step 12: `/on_track (on_track)` (BPP -> BAP)**: The BPP returns real-time GPS coordinates and an active web tracking link.
- **Step 13: `on_status (on_status_out_for_delivery)` [Unsolicited] (BPP -> BAP)**: The courier arrives in the delivery sector; `order.state` remains `In-progress`.
- **Step 14: `on_status (on_status_order_delivered)` [Unsolicited] (BPP -> BAP)**: Secure OTP doorstep verification is completed and the parcel is handed to the customer; `order.state` transitions to `Completed`.

---

### Flow 2: Customization Input Text Flow

- **Flow ID:** `Customization_Input_Text_Flow`
- **Config File:** `./ELECTRONICS/Customization_Input_Text_Flow.yaml`
- **Protocol Version:** `1.2.5`
- **Use Case:** `ELECTRONICS`
- **Tags:** `WORKBENCH`, `MANDATORY`, `REPORTABLE`

#### 1. Short Description
Demonstrates hardware personalization for consumer electronics. The buyer inputs custom text (such as custom laser engraving or personalization dedications) during cart selection. The seller validates the customization, quotes any applicable customization surcharges, and fulfills the personalized order.

#### 2. API Breakdown & Technical Actions
- **Step 1: `/select (select_input)` (BAP -> BPP)**: The BAP selects an electronic item and supplies custom text input within the customization tags.
- **Step 2: `/on_select (on_select_input)` (BPP -> BAP)**: The seller validates text feasibility, confirms serviceability (`Fulfillment: Serviceable`), and computes an itemized quote including customization fees.
- **Step 3: `/init (init)` (BAP -> BPP)**: Order draft initialization with customer and delivery details.
- **Step 4: `/on_init (on_init)` (BPP -> BAP)**: Seller confirms commercial and customization terms.
- **Step 5: `/confirm (confirm)` (BAP -> BPP)**: Buyer confirms prepaid payment; `order.state = "Created"`.
- **Step 6: `/on_confirm (on_confirm)` (BPP -> BAP)**: Seller confirms order creation; `order.state = "Created"`.
- **Step 7: `on_status (on_status_pending)` [Unsolicited] (BPP -> BAP)**: Warehouse initiates custom engraving and preparation; `order.state` transitions to `Accepted`.
- **Step 8: `on_status (on_status_packed)` [Unsolicited] (BPP -> BAP)**: Customized hardware is verified, quality checked, and packed; `fulfillment.state = "Packed"`, `order.state = "In-progress"`.
- **Step 9: `on_status (on_status_agent_assigned)` [Unsolicited] (BPP -> BAP)**: Courier assigned; `order.state = "In-progress"`.
- **Step 10: `on_status (on_status_picked)` [Unsolicited] (BPP -> BAP)**: Courier takes custody; `order.state = "In-progress"`.
- **Step 11: `on_status (on_status_out_for_delivery)` [Unsolicited] (BPP -> BAP)**: Package out for delivery; `order.state = "In-progress"`.
- **Step 12: `on_status (on_status_order_delivered)` [Unsolicited] (BPP -> BAP)**: Doorstep delivery completed; `order.state = "Completed"`.

---

### Flow 3: Purchase Finance Flow

- **Flow ID:** `Purchase_Finance_Flow`
- **Config File:** `./ELECTRONICS/Purchase_Finance_Flow.yaml`
- **Protocol Version:** `1.2.5`
- **Use Case:** `ELECTRONICS`
- **Tags:** `WORKBENCH`, `MANDATORY`, `REPORTABLE`

#### 1. Short Description
Purchase of high-value electronics with consumer installment financing (EMI / BNPL). Covers product selection, financing terms configuration, down payment and loan confirmation, and multi-stage fulfillment tracking.

#### 2. API Breakdown & Technical Actions
- **Step 1: `/select (select)` (BAP -> BPP)**: Buyer selects high-value electronic goods.
- **Step 2: `/on_select (on_select)` (BPP -> BAP)**: Seller validates inventory and confirms delivery serviceability (`Fulfillment: Serviceable`).
- **Step 3: `/init (init_fin)` (BAP -> BPP)**: The BAP configures financing preferences, including installment tenure, down payment, and lending partner details.
- **Step 4: `/on_init (on_init_fin)` (BPP -> BAP)**: The seller returns the formal financing schedule, interest rate, processing charges, and loan agreement parameters.
- **Step 5: `/confirm (confirm_fin)` (BAP -> BPP)**: The BAP passes loan approval reference and down payment capture; `order.state = "Created"`.
- **Step 6: `/on_confirm (on_confirm_fin)` (BPP -> BAP)**: The seller validates financing terms and confirms order creation; `order.state = "Created"`.
- **Step 7: `on_status (on_status_pending_fin)` [Unsolicited] (BPP -> BAP)**: Order accepted by warehouse; `order.state = "Accepted"`.
- **Step 8: `on_status (on_status_packed_fin)` [Unsolicited] (BPP -> BAP)**: Device packed with finance and warranty documentation; `fulfillment.state = "Packed"`, `order.state = "In-progress"`.
- **Step 9: `on_status (on_status_agent_assigned_fin)` [Unsolicited] (BPP -> BAP)**: Courier assigned; `order.state = "In-progress"`.
- **Step 10: `on_status (on_status_picked_fin)` [Unsolicited] (BPP -> BAP)**: Parcel picked up; `order.state = "In-progress"`.
- **Step 11: `on_status (on_status_out_for_delivery_fin)` [Unsolicited] (BPP -> BAP)**: Parcel out for delivery; `order.state = "In-progress"`.
- **Step 12: `on_status (on_status_order_delivered_fin)` [Unsolicited] (BPP -> BAP)**: Doorstep handover completed; `order.state = "Completed"`.

---

### Flow 4: SNP Collecting Payment Flow

- **Flow ID:** `SNP_Collecting_Payment_Flow`
- **Config File:** `./ELECTRONICS/SNP_Collecting_Payment_Flow.yaml`
- **Protocol Version:** `1.2.5`
- **Use Case:** `ELECTRONICS`
- **Tags:** `WORKBENCH`, `MANDATORY`, `REPORTABLE`

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

### Flow 5: Replacement Flow (Hardware Reverse QC and Reshipment)

- **Flow ID:** `Replacement_Flow`
- **Config File:** `./ELECTRONICS/Replacement_Flow.yaml`
- **Protocol Version:** `1.2.5`
- **Use Case:** `ELECTRONICS`
- **Tags:** `PRAMAAN`, `OPTIONAL`, `REPORTABLE`, `WORKBENCH`

#### 1. Short Description
A comprehensive 21-step post-delivery hardware replacement lifecycle for electronics. Following delivery, the buyer requests a replacement for defective hardware. The seller conducts an interim reverse QC check, approves replacement, dispatches a reverse courier to verify and collect the unit, and ships a brand-new replacement device with complete status tracking.

#### 2. API Breakdown & Technical Actions
- **Steps 1–12 (`/select` to `on_status_order_delivered`)**: Outbound delivery of the original device from cart checkout to successful delivery completion (`order.state = "Completed"`).
- **Step 13: `/update (update_reverse_qc_rep)` (BAP -> BPP)**: Buyer files a replacement request with reverse QC, submitting defect details, photos, and serial number.
- **Step 14: `/on_update (on_update_interim_reverseQc)` (BPP -> BAP)**: Seller acknowledges the reverse QC request and prepares return logistics.
- **Step 15: `on_update (on_update_return_approved)` [Unsolicited] (BPP -> BAP)**: Seller formally approves the hardware replacement.
- **Step 16: `on_update (on_update_return_picked_rep)` [Unsolicited] (BPP -> BAP)**: Reverse pickup agent verifies IMEI / serial number and collects the defective device.
- **Step 17: `on_update (on_update_return_delivered_rep)` [Unsolicited] (BPP -> BAP)**: Defective device delivered back to seller facility.
- **Step 18: `on_status (on_status_packed_rep)` [Unsolicited] (BPP -> BAP)**: Seller packs a brand-new replacement unit; `order.state` transitions to `In-progress`.
- **Step 19: `on_status (on_status_picked_rep)` [Unsolicited] (BPP -> BAP)**: Courier picks up the replacement unit.
- **Step 20: `on_status (on_status_out_for_delivery_rep)` [Unsolicited] (BPP -> BAP)**: Replacement package out for delivery.
- **Step 21: `on_status (on_status_order_delivered_rep)` [Unsolicited] (BPP -> BAP)**: Replacement unit successfully delivered to the customer; order marked `Completed`.

---

### Flow 6: Return Flow (Post-Delivery Return and Refund)

- **Flow ID:** `Return_Flow`
- **Config File:** `./ELECTRONICS/Return_Flow.yaml`
- **Protocol Version:** `1.2.5`
- **Use Case:** `ELECTRONICS`
- **Tags:** `WORKBENCH`, `MANDATORY`, `REPORTABLE`

#### 1. Short Description
Standard post-delivery return flow for consumer electronics. Covers buyer return initiation, merchant return approval, doorstep reverse courier pickup with serial number verification, settlement trail reconciliation, and warehouse receipt with refund release.

#### 2. API Breakdown & Technical Actions
- **Steps 1–12 (`/select` to `on_status_order_delivered`)**: Complete outbound order placement, confirmation, and delivery fulfillment (`order.state = "Completed"`).
- **Step 13: `/update (update_return)` (BAP -> BPP)**: Buyer submits a return request for refund within the return policy window.
- **Step 14: `/on_update (on_update_return_init)` (BPP -> BAP)**: Seller initializes reverse fulfillment.
- **Step 15: `on_update (on_update_return_approved)` [Unsolicited] (BPP -> BAP)**: Seller approves the return following photo verification.
- **Step 16: `on_update (on_update_return_picked)` [Unsolicited] (BPP -> BAP)**: Reverse courier verifies device serial number / IMEI, checks physical condition, and accepts custody.
- **Step 17: `/update (update_settlement_trail)` (BAP -> BPP)**: BAP transmits updated settlement trail details for the refund disbursement.
- **Step 18: `on_update (on_update_return_delivered)` [Unsolicited] (BPP -> BAP)**: Device delivered to merchant warehouse, bench diagnostics verified, and return completed.

---

### Flow 7: Buyer Cancellation Flow

- **Flow ID:** `Buyer_Cancellation_Flow`
- **Config File:** `./ELECTRONICS/Buyer_Cancellation_Flow.yaml`
- **Protocol Version:** `1.2.5`
- **Use Case:** `ELECTRONICS`
- **Tags:** `PRAMAAN`, `MANDATORY`, `REPORTABLE`, `WORKBENCH`

#### 1. Short Description
Validates buyer-initiated pre-dispatch cancellation for a confirmed electronics order. The seller halts warehouse processing, marks the order cancelled, and initiates an automated full refund.

#### 2. API Breakdown & Technical Actions
- **Steps 1–6 (`/select` to `/on_confirm`)**: Standard prepaid order creation and confirmation.
- **Step 7: `/cancel (cancel)` (BAP -> BPP)**: Buyer triggers cancellation before shipment dispatch, providing a valid cancellation reason code.
- **Step 8: `/on_cancel (on_cancel)` (BPP -> BAP)**: Seller validates cancellability (`@ondc/org/cancellable = true`), terminates fulfillment, sets `order.state = "Cancelled"`, and triggers automated refund.

---

### Flow 8: Seller Cancellation Flow (Warehouse Part-Cancellation and RTO)

- **Flow ID:** `Seller_Cancellation_Flow`
- **Config File:** `./ELECTRONICS/Seller_Cancellation_Flow.yaml`
- **Protocol Version:** `1.2.5`
- **Use Case:** `ELECTRONICS`
- **Tags:** `WORKBENCH`, `MANDATORY`, `REPORTABLE`

#### 1. Short Description
Exercises a multi-exception merchant lifecycle: picking stockout / damaged unit leading to partial order cancellation, outbound delivery of remaining goods, doorstep delivery failure (unreachable buyer), and Return to Origin (RTO) with warehouse return/disposal.

#### 2. API Breakdown & Technical Actions
- **Steps 1–6 (`/select` to `/on_confirm`)**: Multi-item electronics order confirmed.
- **Step 7: `on_update (on_update_part_cancel)` [Unsolicited] (BPP -> BAP)**: During warehouse picking, the seller identifies an unavailable/damaged item and emits an unsolicited update cancelling that line item.
- **Step 8: `/update (update_partial_cancel_settlement)` (BAP -> BPP)**: BAP adjusts quote and transmits partial refund settlement trail.
- **Steps 9–13 (`on_status_pending` to `on_status_out_for_delivery`)**: Outbound fulfillment of remaining items to `Out-for-delivery`.
- **Step 14: `on_cancel (on_cancel_rto)` [Unsolicited] (BPP -> BAP)**: Doorstep delivery fails (customer unreachable / OTP refused); seller initiates RTO (`order.state = "Cancelled"`).
- **Step 15: `on_status (on_status_rto_delivereddisposed)` [Unsolicited] (BPP -> BAP)**: Package returned to seller origin warehouse or disposed of per policy (`order.state = "Cancelled"`).

---

### Flow 9: Force Cancellation Flow (In-Transit Cancellation)

- **Flow ID:** `Force_Cancellation_Flow`
- **Config File:** `./ELECTRONICS/Force_Cancellation_Flow.yaml`
- **Protocol Version:** `1.2.5`
- **Use Case:** `ELECTRONICS`
- **Tags:** `WORKBENCH`, `MANDATORY`, `REPORTABLE`

#### 1. Short Description
Handles an exceptional scenario where a customer demands cancellation while the electronics parcel is already in transit (`Out-for-delivery`). An initial cancellation attempt is rejected, followed by an authorized force cancellation override, shipment termination, and settlement trail adjustment.

#### 2. API Breakdown & Technical Actions
- **Steps 1–10 (`/select` to `on_status_picked`)**: Order confirmed and packed; courier takes custody.
- **Step 11: `on_status (on_status_out_for_delivery_force)` [Unsolicited] (BPP -> BAP)**: Package is out for delivery.
- **Step 12: `/cancel (cancel_no)` (BAP -> BPP)**: Buyer attempts cancellation; rejected due to active delivery transit.
- **Step 13: `/cancel (cancel_yes)` (BAP -> BPP)**: Buyer invokes force cancellation with critical reason code.
- **Step 14: `/on_cancel (on_cancel_yes)` (BPP -> BAP)**: Seller terminates delivery, instructs courier to return, and sets `order.state = "Cancelled"`.
- **Step 15: `/update (update_settlement_cancel)` [Unsolicited] (BAP -> BPP)**: BAP updates settlement trail to process immediate cancellation refund.

---

### Flow 10: Out of Stock Flow (Cart Modification Recovery)

- **Flow ID:** `Out_Of_Stock_Flow`
- **Config File:** `./ELECTRONICS/Out_Of_Stock_Flow.yaml`
- **Protocol Version:** `1.2.5`
- **Use Case:** `ELECTRONICS`
- **Tags:** `WORKBENCH`, `MANDATORY`, `REPORTABLE`

#### 1. Short Description
Demonstrates stockout recovery during checkout. The buyer selects an out-of-stock electronic item, receives an unavailable response, modifies the cart to select an available model or variant, and successfully completes the order with live tracking.

#### 2. API Breakdown & Technical Actions
- **Step 1: `/select (select_out_of_stock)` (BAP -> BPP)**: Buyer selects a depleted model/variant.
- **Step 2: `/on_select (on_select_out_of_stock)` (BPP -> BAP)**: Seller indicates out of stock (`quantity.available.count = 0`).
- **Step 3: `/select (select)` (BAP -> BPP)**: Buyer modifies cart, selecting an available model/color variant.
- **Step 4: `/on_select (on_select)` (BPP -> BAP)**: Seller confirms availability and quote (`Fulfillment: Serviceable`).
- **Steps 5–14 (`/init` to `on_status_order_delivered`)**: Standard order creation, prepaid confirmation, warehouse packaging, and delivery completion (`Completed`).
- **Steps 15–16 (`/track` and `/on_track`)**: In-transit GPS tracking verification.

---

### Flow 11: Out of Stock Flow (Immediate Error Code)

- **Flow ID:** `Out_Of_Stock_Flow(Error-code)`
- **Config File:** `./ELECTRONICS/Out_Of_Stock_Flow_Error-code_.yaml`
- **Protocol Version:** `1.2.5`
- **Use Case:** `ELECTRONICS`
- **Tags:** `WORKBENCH`, `MANDATORY`, `REPORTABLE`

#### 1. Short Description
Validates protocol exception handling when an electronics buyer selects an out-of-stock product and the seller immediately rejects the transaction via structured error codes.

#### 2. API Breakdown & Technical Actions
- **Step 1: `/select (select_out_of_stock)` (BAP -> BPP)**: Buyer selects an out-of-stock device.
- **Step 2: `/on_select (on_select_out_of_stock)` (BPP -> BAP)**: Seller responds with error code `40002` or `30009` and sets `quantity.available.count = 0`, halting checkout progression.

---

### Flow 12: Discovery Flow: Full Catalog City Broadcast

- **Flow ID:** `Discovery_Flow_full_catalog`
- **Config File:** `./ELECTRONICS/Discovery_Flow_full_catalog.yaml`
- **Protocol Version:** `1.2.5`
- **Use Case:** `ELECTRONICS`
- **Tags:** `PRAMAAN`, `MANDATORY`, `REPORTABLE`, `WORKBENCH`

#### 1. Short Description
City-wide broadcast discovery where a buyer app searches for electronics products and sellers return their full catalogs featuring custom menu groupings, technical specifications, and pricing.

#### 2. API Breakdown & Technical Actions
- **Step 1: `/search (search)` (BAP -> BPP via Gateway)**: Broadcast search query specifying domain `ONDC:RET14` and city location coordinates.
- **Step 2: `/on_search (on_search)` (BPP -> BAP)**: Seller returns comprehensive catalog with category trees, brand attributes, technical specs, warranty terms, and pricing.

---

### Flow 13: Discovery Flow: Incremental Catalog Push and Disablement

- **Flow ID:** `Discovery_Flow_incremental_catalog`
- **Config File:** `./ELECTRONICS/Discovery_Flow_incremental_catalog.yaml`
- **Protocol Version:** `1.2.5`
- **Use Case:** `ELECTRONICS`
- **Tags:** `PRAMAAN`, `MANDATORY`, `REPORTABLE`, `WORKBENCH`

#### 1. Short Description
Seller-initiated incremental catalog updates. The seller pushes delta product/pricing modifications and broadcasts store disablement / operational shutdown notifications.

#### 2. API Breakdown & Technical Actions
- **Step 1: `/search (search_inc)` (BAP -> BPP)**: Initial baseline search.
- **Step 2: `on_search (on_search_inc)` [Unsolicited] (BPP -> BAP)**: Seller pushes an unsolicited incremental catalog update with revised prices and stock.
- **Step 3: `on_search (on_search_inc_disable)` [Unsolicited] (BPP -> BAP)**: Seller pushes store/service disablement status.
- **Step 4: `/search (search_inc)` (BAP -> BPP)**: Buyer app synchronizes and acknowledges updated status.

---

### Flow 14: Discovery Flow: Incremental Catalog Refresh Pull

- **Flow ID:** `Discovery_Flow_incremental_catalog_refresh_pull`
- **Config File:** `./ELECTRONICS/Discovery_Flow_incremental_catalog_refresh_pull.yaml`
- **Protocol Version:** `1.2.5`
- **Use Case:** `ELECTRONICS`
- **Tags:** `WORKBENCH`, `OPTIONAL`, `REPORTABLE`

#### 1. Short Description
Buyer-initiated incremental catalog refresh. The buyer app polls sellers using timestamp filters, fetching only modified products and pricing changes without re-downloading entire city catalogs.

#### 2. API Breakdown & Technical Actions
- **Step 1: `/search (search)` (BAP -> BPP via Gateway)**: Baseline discovery request.
- **Step 2: `/on_search (on_search)` (BPP -> BAP)**: Initial full catalog response.
- **Step 3: `/search (search_inc_pull)` (BAP -> BPP)**: Incremental pull query with `tags.catalog_inc = "true"` and timestamp filter.
- **Step 4: `/on_search (on_search_inc_pull)` (BPP -> BAP)**: Compact delta catalog payload.

---

### Flow 15: Delivery Flow with IGM 1.0.0 Dispute Resolution

- **Flow ID:** `Delivery_Flow_With_IGM(v-1.0.0)`
- **Config File:** `./ELECTRONICS/Delivery_Flow_With_IGM_v-1_0_0_.yaml`
- **Protocol Version:** `1.2.5`
- **Use Case:** `ELECTRONICS`
- **Tags:** `PRAMAAN`, `MANDATORY`, `REPORTABLE`, `WORKBENCH`

#### 1. Short Description
Full prepaid electronics delivery lifecycle combined with post-fulfillment dispute redressal under legacy IGM 1.0.0 architecture.

#### 2. API Breakdown & Technical Actions
- **Steps 1–12 (`/select` to `on_status_order_delivered`)**: Complete forward fulfillment from cart checkout to doorstep delivery.
- **Step 13: `/issue (issue_open_100)` (BAP -> BPP)**: Buyer lodges a grievance under IGM 1.0.0 (e.g., missing cable/accessory).
- **Step 14: `/on_issue (on_issue_processing_100)` (BPP -> BAP)**: Seller acknowledges the complaint and assigns a Grievance Officer.
- **Step 15: `on_issue_status (on_issue_resolved_100)` [Unsolicited] (BPP -> BAP)**: Seller issues an unsolicited resolution update detailing remedial action.
- **Step 16: `/issue (issue_close_100)` (BAP -> BPP)**: Customer confirms resolution and closes the grievance ticket.

---

### Flow 16: Delivery Flow with IGM 2.0.0: Evidence Exchange and Replacement

- **Flow ID:** `Delivery_Flow_With_IGM(v-2.0.0)`
- **Config File:** `./ELECTRONICS/Delivery_Flow_With_IGM_v-2_0_0_.yaml`
- **Protocol Version:** `1.2.5`
- **Use Case:** `ELECTRONICS`
- **Tags:** `PRAMAAN`, `MANDATORY`, `REPORTABLE`, `WORKBENCH`

#### 1. Short Description
Interactive IGM 2.0.0 workflow. The buyer reports a dead-on-arrival / defective electronic device, the seller requests additional diagnostic and serial number proof, the buyer supplies the evidence, and the seller approves an item replacement.

#### 2. API Breakdown & Technical Actions
- **Steps 1–12 (`/select` to `on_status_order_delivered`)**: Forward delivery lifecycle.
- **Step 13: `/issue (issue_open)` (BAP -> BPP)**: Buyer opens an issue reporting hardware failure.
- **Step 14: `/on_issue (on_issue_processing)` (BPP -> BAP)**: Initial seller acknowledgment.
- **Step 15: `on_issue (on_issue_need_more_info)` [Unsolicited] (BPP -> BAP)**: Seller requests photos of serial number sticker and charging LED indicator.
- **Step 16: `/issue (issue_info_provided)` (BAP -> BPP)**: Buyer uploads requested diagnostic evidence URLs.
- **Step 17: `/on_issue (on_issue_provided)` (BPP -> BAP)**: Seller acknowledges receipt of evidence.
- **Step 18: `on_issue (on_issue_resolution)` [Unsolicited] (BPP -> BAP)**: Seller validates defect and proposes an item `REPLACEMENT` resolution.
- **Step 19: `/issue (issue_resolution_accept)` (BAP -> BPP)**: Buyer accepts replacement resolution.
- **Step 20: `/on_issue (on_issue_resolved)` (BPP -> BAP)**: Seller confirms resolution agreement.
- **Step 21: `/issue (issue_close)` (BAP -> BPP)**: Buyer closes the grievance.
- **Step 22: `on_status (on_status_igm_2)` [Unsolicited] (BPP -> BAP)**: Seller updates order audit record; `Completed`.

---

### Flow 17: Delivery Flow with IGM 2.0.0: Resolution Accepted (No Action)

- **Flow ID:** `Delivery_Flow_With_IGM_No_Action(v-2.0.0)`
- **Config File:** `./ELECTRONICS/Delivery_Flow_With_IGM_No_Action_v-2_0_0_.yaml`
- **Protocol Version:** `1.2.5`
- **Use Case:** `ELECTRONICS`
- **Tags:** `WORKBENCH`, `MANDATORY`, `REPORTABLE`

#### 1. Short Description
IGM 2.0.0 dispute where the seller investigates a reported issue, determines that the hardware operates within manufacturer specifications or that the issue is due to third-party accessories, and provides an explanatory `NO_ACTION` resolution that the buyer accepts.

#### 2. API Breakdown & Technical Actions
- **Steps 1–12 (`/select` to `on_status_order_delivered`)**: Standard forward fulfillment lifecycle.
- **Step 13: `/issue (issue_open_2)` (BAP -> BPP)**: Buyer opens a complaint under IGM 2.0.0.
- **Step 14: `/on_issue (on_issue_processing)` (BPP -> BAP)**: Seller acknowledges the issue.
- **Step 15: `on_issue (on_issue_resolution_igm_3)` [Unsolicited] (BPP -> BAP)**: Seller provides an explanatory `NO_ACTION` resolution detailing correct device operation and settings.
- **Step 16: `/issue (issue_resolution_accept_igm_3)` (BAP -> BPP)**: Buyer accepts the technical explanation.
- **Step 17: `/on_issue (on_issue_resolved_igm_3)` (BPP -> BAP)**: Seller confirms resolution status.
- **Step 18: `/issue (issue_close_igm_3)` (BAP -> BPP)**: Buyer closes the dispute.
- **Step 19: `on_status (on_status_igm_3)` [Unsolicited] (BPP -> BAP)**: Seller updates the final order audit record; `Completed`.

---

### Flow 18: Delivery Flow with IGM 2.0.0: Rejection, Escalation and Replacement

- **Flow ID:** `Delivery_Flow_With_IGM_Rejection(v-2.0.0)`
- **Config File:** `./ELECTRONICS/Delivery_Flow_With_IGM_Rejection_v-2_0_0_.yaml`
- **Protocol Version:** `1.2.5`
- **Use Case:** `ELECTRONICS`
- **Tags:** `PRAMAAN`, `MANDATORY`, `REPORTABLE`, `WORKBENCH`

#### 1. Short Description
Dispute escalation flow. The buyer reports physical damage, rejects inadequate settlement proposals, escalates the dispute to a Level 2 Grievance Officer, receives an arbitrator ruling in favor of replacement, and the seller dispatches a replacement unit.

#### 2. API Breakdown & Technical Actions
- **Steps 1–12 (`/select` to `on_status_order_delivered`)**: Forward delivery lifecycle.
- **Step 13: `/issue (issue_open)` (BAP -> BPP)**: Buyer opens dispute for transit damage.
- **Step 14: `/on_issue (on_issue_processing)` (BPP -> BAP)**: Seller acknowledgment.
- **Step 15: `on_issue (on_issue_resolution)` [Unsolicited] (BPP -> BAP)**: Seller proposes nominal accessory voucher.
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

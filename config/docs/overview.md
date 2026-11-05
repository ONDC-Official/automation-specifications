# Retail Electronics (ONDC:RET14 1.2.0)

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
- [Additional Scenarios](#additional-scenarios)
  - [1. Buyer-Initiated Return and Reverse QC Pickup (Full and Partial Order)](#1-buyer-initiated-return-and-reverse-qc-pickup-full-and-partial-order)
  - [2. Buyer-Side Order Cancellation](#2-buyer-side-order-cancellation)
  - [3. Merchant-Side Part-Cancellation and Return to Origin (RTO)](#3-merchant-side-part-cancellation-and-return-to-origin-rto)
  - [4. Out of Stock and Variant Inventory Shortage](#4-out-of-stock-and-variant-inventory-shortage)
  - [5. Incremental Catalog Refresh (Push and Pull)](#5-incremental-catalog-refresh-push-and-pull)
  - [6. Statutory Compliance, BIS Certification, and E-Waste Regulations](#6-statutory-compliance-bis-certification-and-e-waste-regulations)
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

The Consumer Electronics domain (**ONDC:RET14**, specification version **1.2.0**) establishes an open, interoperable digital commerce standard for consumer electronics, computing devices, mobile communications, home entertainment, large and small domestic appliances, audio gear, wearables, gaming consoles, and tech accessories across the Open Network for Digital Commerce (ONDC). Electronics retail represents high average order values (AOV), specification-driven buyer decision journeys, critical anti-fraud protections, fragile transit logistics, and rigorous statutory compliance mandates.

Unlike low-cost FMCG or grocery transactions, consumer electronics purchases involve intricate technical parameters (processor generations, storage tiers, RAM capacities, screen refresh rates, BEE energy efficiency star ratings, and input/output interfaces). Furthermore, high unit costs necessitate precise tracking of serial numbers, IMEI identifiers, and MAC addresses at packing and dispatch to prevent fraud during post-delivery return or replacement claims. Fragile high-value hardware—such as smart TVs with delicate LED/OLED panels, glass-backed smartphones, and sensitive precision optics—mandates specialized shock-absorbing transit packaging and secure OTP-based delivery handovers.

ONDC unbundles the traditionally closed e-commerce marketplace landscape. Buyers can search and compare electronics across authorized brand stores, regional superstores, independent appliance dealers, and local electronics retailers using their preferred **Buyer Application (BAP)**. Sellers manage their inventory, serial numbers, warranty terms, and transparent pricing through a **Seller Application (BPP)**, while specialized **Logistics Service Providers (LSPs)** execute high-security parcel transit with live tracking, doorstep OTP authentication, and reverse logistics quality checks.

The protocol standardizes all network interactions across:
- **Discovery**: `/search` and `/on_search` (city-wide broadcast queries, category taxonomies, variant hierarchies, technical specifications, and incremental catalog synchronization).
- **Ordering**: `/select`, `/on_select`, `/init`, `/on_init`, `/confirm`, and `/on_confirm`.
- **Fulfillment & Real-time Tracking**: Unsolicited `/on_status` lifecycle events (`Accepted`, `Packed`, `Agent-assigned`, `Order-picked-up`, `Out-for-delivery`, `Order-delivered`), `/track`, and `/on_track`.
- **Post-Order Lifecycle & Exceptions**: `/update`, `/on_update`, `/cancel`, and `/on_cancel` (doorstep quality-checked returns, reverse logistics pickup, warehouse bench testing, merchant part-cancellations, and Return to Origin / RTO).
- **Grievance Redressal**: Issue and Grievance Management under both **IGM 1.0.0** and **IGM 2.0.0** architectures.

---

## Participants

| Participant | What This Means |
|---|---|
| **Buyer Application (BAP)** | The consumer-facing digital application (e.g., tech marketplace apps, banking portals, super-apps, telco commerce platforms) where shoppers browse electronics catalogs, filter by technical hardware specs, compare warranties, configure delivery addresses, complete prepaid payments, track courier transit in real time, and raise returns or grievances. |
| **Seller Application (BPP)** | An application representing electronics retail chains, direct-to-consumer (D2C) hardware brands, authorized distributors, regional appliance dealerships, or refurbished electronics merchants. The BPP publishes item catalogs with variant attributes (storage, RAM, color, screen size), checks delivery serviceability, calculates quotes, manages serial number / IMEI registration during packing, and coordinates reverse QC inspections. |
| **Logistics Service Provider (LSP)** | A delivery network participant that executes fragile and high-value cargo transport (hyperlocal courier or intercity surface/air parcel shipping). In seller-managed logistics, the BPP or its integrated delivery partner allocates couriers, provides live GPS tracking, captures secure OTP delivery verification, and executes reverse logistics pickups with doorstep physical checks. |
| **Gateway** | The ONDC routing infrastructure that multicasts broadcast discovery requests (`/search`) from BAPs to active seller applications (BPPs) based on domain code (`ONDC:RET14`), city code (e.g. `std:080`), and geolocation parameters. |

---

## The User Journey

The standard electronics ordering journey (`Order_to_confirm_to_fulfillment_(Prepaid)`) enables a consumer to search for electronic devices, compare technical specifications and warranties, review transparent price breakdowns and turnaround times, provide delivery coordinates, complete prepaid payment, and receive securely packaged hardware with continuous shipment tracking.

### 1. Discovery and Catalog Search

The buyer initiates discovery on the BAP by searching for electronics products, device models, or appliance categories (e.g., "OLED TV 55 inch", "Laptops 16GB RAM", "Smartphones", "Direct Cool Refrigerators"):

- **Intent Broadcast**: The BAP transmits an asynchronous `/search` request via the ONDC Gateway specifying domain `ONDC:RET14`, buyer geolocation coordinates, city code, and fulfillment type (`Delivery`).
- **Catalog Delivery**: Active BPPs within the serviceable area respond with asynchronous `/on_search` payloads containing their store catalog (`bpp/providers[]`). This includes product categories, custom menu groupings, brand metadata, model numbers, hardware specifications (processor, memory, display dimensions, energy star ratings), MRP, discounted selling price, stock availability, warranty disclosure (manufacturer vs. seller warranty), and statutory Legal Metrology attributes.

### 2. Model/Specification Selection and Serviceability Check

The buyer selects an exact electronics item or variant (e.g., 256GB Midnight Black Smartphone) and proceeds to configure checkout:

- **Network interaction:**
  - **`/select` (BAP -> BPP)**: The BAP transmits the selected item ID, variant specifications, quantity, provider location ID, and delivery destination coordinates (`fulfillments[0].end.location.gps` and `address.area_code`).
  - **`/on_select` (BPP -> BAP)**: The seller validates real-time inventory at the fulfillment node, confirms delivery serviceability, and computes a detailed quote breakdown (`quote.breakup[]`). This includes the hardware base price, applicable taxes (CGST/SGST), protective packaging / wooden crate fees (for large panels or fragile electronics), logistics shipping charges, and estimated turnaround time (`@ondc/org/TAT`). If the requested device or variant is depleted, the seller responds with an out-of-stock protocol error code (`40002` or `30009`).

### 3. Order Initialization and Shipping Configuration

The buyer confirms recipient information and finalized delivery coordinates:

- **Network interaction:**
  - **`/init` (BAP -> BPP)**: The BAP transmits customer details (name, phone number, email), exact street address, billing information, delivery instructions (e.g., gate code, fragile handling reminder), and payment preference.
  - **`/on_init` (BPP -> BAP)**: The seller freezes the item quote and turnaround time, specifies static and dynamic order terms (cancellation window, return eligibility duration, brand warranty registration link), establishes payment collection requirements (prepaid BAP-collected transaction), and returns settlement fee details.

### 4. Order Confirmation and Prepaid Escrow

Because consumer electronics represent high-value merchandise, transactions follow a prepaid escrow model:

- **Network interaction:**
  - **`/confirm` (BAP -> BPP)**: The BAP captures digital payment from the buyer via UPI, credit card, net banking, or consumer finance/EMI, generates a unique order identifier (`order.id`), and transmits payment confirmation parameters (`payment.params.transaction_id`, `payment.status = "PAID"`, `payment.type = "PRE-PAID"`).
  - **`/on_confirm` (BPP -> BAP)**: The seller validates payment receipt, records the order in its Warehouse Management / Order Management System (WMS/OMS), initializes order state (`order.state = "Created"`), and sets the primary fulfillment status to `Pending`.

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
  - **`on_status (on_status_agent_assigned)` [Unsolicited] (BPP -> BAP)**: Courier details (agent name, masked phone number, vehicle type) are transmitted; `fulfillment.state` transitions to `Agent-assigned`.
  - **`on_status (on_status_picked)` [Unsolicited] (BPP -> BAP)**: Courier verifies parcel integrity, scans airway bill barcode, and takes physical custody; `fulfillment.state` transitions to `Order-picked-up`.

### 7. Order Dispatch, In-Flight Tracking, and Secure Delivery

The shipment moves through the transit hub network toward the buyer's doorstep:

- **Real-Time Tracking:**
  - **`/track` (BAP -> BPP)**: The BAP queries live shipment coordinates.
  - **`/on_track` (BPP -> BAP)**: The BPP or LSP returns real-time GPS telemetry and an active web tracking URL (`tracking.url`).
- **Doorstep Authentication & Handover:**
  - **`on_status (on_status_out_for_delivery)` [Unsolicited] (BPP -> BAP)**: Courier is in the immediate vicinity; `fulfillment.state` updates to `Out-for-delivery`.
  - At the doorstep, the delivery agent requests a secure one-time password (OTP) generated on the buyer's app to verify identity prior to handing over the high-value electronics package. The agent may also inspect external box seals in the customer's presence.
  - **`on_status (on_status_order_delivered)` [Unsolicited] (BPP -> BAP)**: Successful handover is confirmed; `fulfillment.state` transitions to `Order-delivered` and `order.state` reaches terminal state `Completed`.

### 8. Settlement and Post-Fulfillment

Upon successful delivery completion:
- The return window countdown timer begins (typically 7 to 10 days for electronics, subject to seller policy).
- The BAP releases funds from escrow to the seller's account net of network fees, taxes, and logistics charges in accordance with ONDC settlement guidelines.
- The buyer receives a tax invoice enabling registration with authorized brand service centers for the manufacturer's warranty.

---

## Additional Scenarios

Beyond standard prepaid delivery, ONDC:RET14 defines standardized workflows for post-delivery returns, pre-dispatch cancellations, stock exceptions during warehouse picking, failed deliveries (RTO), and continuous catalog synchronization.

### 1. Buyer-Initiated Return and Reverse QC Pickup (Full and Partial Order)

Electronics returns involve high financial risk and require strict verification to prevent fraudulent returns (such as counterfeit swapping or returning damaged units). The domain defines an end-to-end 18-step return flow (`Buyer_Initiated_Return_(Full_Order_and_Partial_Order)`):

- **Return Initiation (`/update` - `update_return`)**: Within the return window, the shopper initiates a return request specifying the return reason code (e.g., Dead-on-Arrival / DOA, defective hardware, damaged casing, incorrect specification delivered), uploading mandatory photographic/unboxing video proof, and selecting full-order or partial-item return.
- **Merchant Evaluation (`/on_update` - `on_update_return_init` & `on_update_return_approved`)**: The seller reviews the uploaded evidence, validates that the return policy covers the fault, and emits an unsolicited `on_update` approving the return and creating a reverse logistics fulfillment leg.
- **Doorstep Reverse Quality Check (`/on_update` - `on_update_return_picked`)**: A reverse logistics pickup agent arrives at the buyer's address. The agent conducts a physical inspection:
  - Verifying the serial number / IMEI on the device against the original dispatch record.
  - Confirming the physical condition (no unauthorized opening, no user-inflicted liquid immersion, screen uncracked).
  - Ensuring all in-box accessories (power adapter, cables, warranty card, remote control) are present.
  - Upon successful QC check, the agent takes custody and the seller emits an unsolicited `on_update` marking the return fulfillment as picked up.
- **Settlement & Warehouse Bench Verification (`/update` - `update_settlement_trail` & `/on_update` - `on_update_return_delivered`)**: The BAP transmits updated settlement trail details. When the package arrives at the merchant's technical facility, technicians conduct bench diagnostics. Once verified, the seller emits `on_update` confirming delivery and releases the refund settlement to the buyer.

### 2. Buyer-Side Order Cancellation

Consumers may cancel an order before warehouse dispatch (`Buyer_Side_Order_Cancellation`):

- **Pre-Dispatch Cancellation (`/cancel`)**: The buyer requests cancellation from the BAP interface prior to courier pickup, providing a standardized cancellation reason code (e.g., `001` - Order placed by mistake, `003` - Delivery delay anticipated).
- **Merchant Validation (`/on_cancel`)**: The BPP verifies that the order has not passed the non-cancellable threshold (`@ondc/org/cancellable = true`). The merchant immediately aborts picking, releases reserved inventory, transitions `order.state = "Cancelled"` and `fulfillment.state = "Cancelled"`, and triggers an automated full refund to the buyer's original payment method.

### 3. Merchant-Side Part-Cancellation and Return to Origin (RTO)

A dual-exception lifecycle (`Merchant_Side_RTO_and_Part_Order_Cancellation_Flow`) handling inventory discrepancies during picking and failed doorstep deliveries:

- **Warehouse Part-Cancellation (`on_update` - `on_update_part_cancel`)**: In a multi-item electronics order (e.g., a laptop, mouse, and external monitor), the merchant identifies during picking that the requested monitor variant has sustained packaging damage or is depleted. The seller issues an unsolicited `on_update` cancelling that specific line item while keeping the rest of the order active. The BAP acknowledges and updates the settlement trail (`/update`) to refund the cancelled item.
- **Outbound Dispatch**: The remaining serviceable items are packed, handed to the courier, and progress through transit to `Out-for-delivery`.
- **Doorstep Delivery Failure & RTO (`on_cancel` - `on_cancel_rto`)**: The courier attempts delivery, but the customer is unreachable after multiple contact attempts, or the customer refuses to provide the delivery OTP. The courier initiates a Return to Origin (RTO) with cancellation reason code `013` (Buyer unreachable / refused delivery).
- **Settlement Adjustment & Origin Delivery (`/update` & `on_status` - `on_status_rto_delivered`)**: The BAP submits updated settlement terms to deduct approved return logistics costs. When the secure package arrives back at the merchant facility, the merchant issues an unsolicited `on_status` marking the RTO shipment delivered and closing the transaction.

### 4. Out of Stock and Variant Inventory Shortage

When inventory for a specific device model, color, or storage configuration is exhausted:

- **Immediate Error Response (`Out_of_Stock(Error_code)`)**: When a buyer submits a `/select` request for a depleted item or variant, the BPP immediately rejects the selection on `/on_select` with protocol error code `40002` (Out of Stock) or `30009` and sets `quantity.available.count = 0`. This prevents phantom checkout attempts and prompts the buyer app to display unavailable stock clearly.

### 5. Incremental Catalog Refresh (Push and Pull)

Consumer electronics catalogs experience continuous updates—rapid price adjustments, flash sale promotions, new model arrivals, and store operating hours:

- **Incremental Push (`Search_and_Custom_Menu_(Incremental_Push)`)**: The seller proactively publishes catalog delta updates via unsolicited `/on_search` payloads containing only modified items, revised pricing, or updated stock levels. Sellers can also push store closure or maintenance disablement messages (`on_search_inc_close`) to temporarily take products offline.
- **Incremental Pull (`Discovery_Flow_incremental_catalog_refresh_pull`)**: The buyer app periodically polls for catalog changes by transmitting a `/search` request with tag `catalog_inc = "true"` and a timestamp filter. The BPP responds via `/on_search` with only the delta changes recorded since that timestamp, drastically reducing bandwidth and computation.

### 6. Statutory Compliance, BIS Certification, and E-Waste Regulations

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

- **Issue Filing (`/issue`)**: The buyer submits a formal grievance via the BAP specifying the complaint category (e.g., `ITEM`, `FULFILLMENT`), subcategory (e.g., `DEAD_ON_ARRIVAL`, `MISSING_ACCESSORIES`), narrative description, and contact details.
- **Issue Acknowledgment (`/on_issue`)**: The BPP acknowledges the issue, assigns an internal ticket identifier, and furnishes the details of the designated Grievance Officer.
- **Issue Resolution (`on_issue_status` [Unsolicited])**: The seller investigates the claim and publishes a resolution payload detailing the remedial action taken (e.g., dispatching a replacement power cable, arranging a technical technician visit, or approving a partial refund).
- **Issue Closure (`/issue`)**: The buyer verifies that the grievance has been satisfactorily addressed and emits an issue closure message.

### 2. IGM 2.0.0 Architecture

IGM 2.0.0 introduces a robust, multi-participant, role-based dispute framework featuring evidence exchange, diagnostic data submission, multiple resolution remedies (`REFUND`, `REPLACEMENT`, `NO_ACTION`), and formal escalation paths to Level 2 Grievance Officers and Network Intermediaries:

1. **Resolution Accepted with `NO_ACTION` (`Order_to_confirm_to_fulfillment__Prepaid_with_IGM_No_Action_v-2.0.0`)**:
   - The buyer opens a grievance (e.g., alleging that a newly purchased smart TV does not display high dynamic range / HDR content).
   - The merchant examines device specifications and determines that the television operates strictly within manufacturer specifications and that the customer is feeding an incompatible signal source.
   - The seller issues an unsolicited `on_issue` with resolution action `NO_ACTION`, accompanied by detailed technical guidance and configuration instructions.
   - The buyer accepts the technical explanation (`/issue`), the ticket is closed, and the seller synchronizes the final order audit record via an unsolicited `on_status`.

2. **Rejection, Escalation and Return Authorization (`Order_to_confirm_to_fulfillment__Prepaid_with_IGM_Rejection_v-2.0.0`)**:
   - The buyer reports physical casing damage upon delivery.
   - The merchant initially proposes a minor cosmetic coupon or nominal discount.
   - The buyer rejects the resolution (`issue_resolution_reject`).
   - The merchant attempts a revised proposal, which the buyer also rejects, subsequently escalating the dispute to a Level 2 Grievance Officer / Network Intermediary (`issue_escalate`).
   - The escalated mediator reviews unboxing photos and delivery timestamps, ruling in favor of the buyer and ordering full product return and refund.
   - The buyer accepts the escalated ruling, the dispute is closed, and the seller triggers reverse logistics and refund settlement via an unsolicited `on_update` (`on_update_igm_return`).

3. **Evidence Exchange & Hardware Replacement (`Order_to_confirm_to_fulfillment__Prepaid_with_IGM_v-2.0.0`)**:
   - The buyer lodges a grievance reporting that a newly delivered laptop will not power on (Dead-on-Arrival).
   - Rather than immediate rejection, the BPP requests additional verification via an unsolicited `on_issue` (`on_issue_need_more_info`), requesting photographs of the serial number / IMEI sticker on the bottom chassis and a video of the charging LED indicator.
   - The buyer provides the requested media URLs via `/issue` (`issue_info_provided`).
   - The seller's technical team validates the defect and issues an unsolicited resolution approving an item `REPLACEMENT`.
   - The buyer accepts the replacement resolution, and the seller executes an unsolicited `on_update` (`on_update_igm_replacement`), scheduling a simultaneous doorstep swap: dispatching a brand-new replacement unit while picking up the defective hardware for return to the factory.

---

## Detailed Protocol Flows

All **12 protocol flows** defined in `automation-specifications/config/flows/index.yaml` for the Electronics domain (`ONDC:RET14 1.2.0`) are detailed below with their classification tags, operational contexts, and full step-by-step API message sequences.

---

### Flow 1: Order to Confirm to Fulfillment (Prepaid Standard Delivery)

- **Flow ID:** `Order_to_confirm_to_fulfillment_(Prepaid)`
- **Config File:** `./ELECTRONICS/Order_to_confirm_to_fulfillment__Prepaid_.yaml`
- **Protocol Version:** `1.2.0`
- **Use Case:** `ELECTRONICS`
- **Tags:** `WORKBENCH`, `PRAMAAN`, `MANDATORY`, `REPORTABLE`

#### 1. Short Description
The canonical end-to-end forward fulfillment journey for consumer electronics. Covers item selection, price and specification verification, order initialization, prepaid payment capture, warehouse picking with serial number logging, multi-stage courier status updates, live GPS tracking, and secure doorstep delivery completion.

#### 2. API Breakdown & Technical Actions
- **Step 1: `/select (select)` (BAP -> BPP)**: The BAP selects electronics products from the seller's catalog, specifying delivery destination coordinates and fulfillment type.
- **Step 2: `/on_select (on_select)` (BPP -> BAP)**: The seller confirms product availability, returns an itemized price breakdown (`quote.breakup[]`), confirms fulfillment serviceability (`Fulfillment: Serviceable`), and quotes delivery turnaround time.
- **Step 3: `/init (init)` (BAP -> BPP)**: The BAP transmits customer details, billing address, exact delivery location, and prepaid payment preference to initiate the order draft.
- **Step 4: `/on_init (on_init)` (BPP -> BAP)**: The seller responds with frozen commercial terms, payment parameters, cancellation windows, and settlement rules.
- **Step 5: `/confirm (confirm)` (BAP -> BPP)**: The BAP captures prepaid digital payment and submits the confirmed order with `order.state = "Created"`.
- **Step 6: `/on_confirm (on_confirm)` (BPP -> BAP)**: The seller validates payment, records the order in OMS/WMS, confirms `order.state = "Created"`, and sets initial fulfillment state to `Pending`.
- **Step 7: `on_status (on_status_pending)` [Unsolicited] (BPP -> BAP)**: The merchant confirms warehouse order processing; `order.state` transitions to `Accepted`.
- **Step 8: `on_status (on_status_packed)` [Unsolicited] (BPP -> BAP)**: The unit is picked from secured storage, serial number/IMEI recorded, and securely packaged with tamper seals; `fulfillment.state` updates to `Packed` and `order.state` to `In-progress`.
- **Step 9: `on_status (on_status_agent_assigned)` [Unsolicited] (BPP -> BAP)**: A logistics courier is assigned for parcel transport; `fulfillment.state` advances to `Agent-assigned`.
- **Step 10: `on_status (on_status_picked)` [Unsolicited] (BPP -> BAP)**: The courier picks up the package from the merchant warehouse; `fulfillment.state` updates to `Order-picked-up`.
- **Step 11: `/track (track)` (BAP -> BPP)**: The BAP queries live in-transit location telemetry.
- **Step 12: `/on_track (on_track)` (BPP -> BAP)**: The BPP returns real-time GPS coordinates and an active web tracking link.
- **Step 13: `on_status (on_status_out_for_delivery)` [Unsolicited] (BPP -> BAP)**: The courier arrives in the delivery sector; `fulfillment.state` transitions to `Out-for-delivery`.
- **Step 14: `on_status (on_status_order_delivered)` [Unsolicited] (BPP -> BAP)**: Secure OTP doorstep verification is completed and the parcel is handed to the customer; `fulfillment.state` reaches `Order-delivered` and `order.state` transitions to `Completed`.

---

### Flow 2: Buyer-Initiated Return (Full Order and Partial Order)

- **Flow ID:** `Buyer_Initiated_Return_(Full_Order_and_Partial_Order)`
- **Config File:** `./ELECTRONICS/Buyer_Initiated_Return__Full_Order_and_Partial_Order_.yaml`
- **Protocol Version:** `1.2.0`
- **Use Case:** `ELECTRONICS`
- **Tags:** `WORKBENCH`, `PRAMAAN`, `MANDATORY`, `REPORTABLE`

#### 1. Short Description
Exercises the complete post-delivery return lifecycle for electronics items (covering both full-order and partial-item returns). Includes return request authorization, doorstep reverse logistics collection with serial number / IMEI inspection, settlement trail coordination, and final warehouse technical verification and refund closure.

#### 2. API Breakdown & Technical Actions
- **Steps 1–6 (`/select` to `/on_confirm`)**: Standard prepaid order creation and payment confirmation.
- **Steps 7–12 (`on_status_accepted` to `on_status_order_delivered`)**: Full outbound fulfillment progression from warehouse packing to successful doorstep delivery.
- **Step 13: `/update (update_return)` (BAP -> BPP)**: The buyer submits a return request for eligible items within the return window, specifying return reason codes (e.g., defective hardware, screen defect) and image proof URLs.
- **Step 14: `/on_update (on_update_return_init)` (BPP -> BAP)**: The seller acknowledges the return request and initializes a reverse fulfillment leg.
- **Step 15: `on_update (on_update_return_approved)` [Unsolicited] (BPP -> BAP)**: The seller formally approves the return following photo verification and authorizes courier reverse pickup.
- **Step 16: `on_update (on_update_return_picked)` [Unsolicited] (BPP -> BAP)**: A reverse pickup agent conducts doorstep physical and IMEI/serial number verification, accepts custody of the device, and emits a pickup update.
- **Step 17: `/update (update_settlement_trail)` (BAP -> BPP)**: The BAP transmits revised settlement terms specifying the refund disbursement trail.
- **Step 18: `on_update (on_update_return_delivered)` [Unsolicited] (BPP -> BAP)**: The returned device arrives at the merchant's warehouse, undergoes technical bench inspection, and the seller confirms return closure with refund execution.

---

### Flow 3: Buyer-Side Order Cancellation

- **Flow ID:** `Buyer_Side_Order_Cancellation`
- **Config File:** `./ELECTRONICS/Buyer_Side_Order_Cancellation.yaml`
- **Protocol Version:** `1.2.0`
- **Use Case:** `ELECTRONICS`
- **Tags:** `WORKBENCH`, `PRAMAAN`, `MANDATORY`, `REPORTABLE`

#### 1. Short Description
Demonstrates a buyer-initiated pre-dispatch cancellation for a confirmed electronics order. The seller verifies that the order is within the allowed cancellation window, halts warehouse fulfillment, and confirms cancellation with automated refund initiation.

#### 2. API Breakdown & Technical Actions
- **Steps 1–6 (`/select` to `/on_confirm`)**: Standard prepaid order placement, validation, and confirmation.
- **Step 7: `/cancel (cancel)` (BAP -> BPP)**: Prior to courier pickup, the buyer triggers an order cancellation request citing a standardized cancellation reason code (e.g., `001` for accidental order).
- **Step 8: `/on_cancel (on_cancel)` (BPP -> BAP)**: The seller validates that the order is cancellable (`@ondc/org/cancellable = true`), halts warehouse processing, transitions `order.state = "Cancelled"` and `fulfillment.state = "Cancelled"`, and communicates refund terms.

---

### Flow 4: Merchant-Side Part-Order Cancellation and Return to Origin (RTO)

- **Flow ID:** `Merchant_Side_RTO_and_Part_Order_Cancellation_Flow`
- **Config File:** `./ELECTRONICS/Merchant_Side_RTO_and_Part_Order_Cancellation_Flow.yaml`
- **Protocol Version:** `1.2.0`
- **Use Case:** `ELECTRONICS`
- **Tags:** `WORKBENCH`, `PRAMAAN`, `MANDATORY`, `REPORTABLE`

#### 1. Short Description
A comprehensive dual-exception operational flow. Handles merchant stockout or damaged unit detection during picking (part-cancellation), followed by an unsuccessful delivery attempt where the buyer is unreachable, resulting in Return to Origin (RTO) and reverse warehouse delivery.

#### 2. API Breakdown & Technical Actions
- **Steps 1–6 (`/select` to `/on_confirm`)**: Multi-item electronics order confirmed and prepaid.
- **Step 7: `on_update (on_update_part_cancel)` [Unsolicited] (BPP -> BAP)**: While picking items in the warehouse, the seller identifies that one specific unit is damaged or unavailable. The seller emits an unsolicited update cancelling that item and adjusting the price quote.
- **Step 8: `/update (update_settlement_trail)` (BAP -> BPP)**: The BAP acknowledges the item reduction and transmits updated settlement instructions for the partial refund.
- **Steps 9–13 (`on_status_pending` to `on_status_out_for_delivery`)**: The remaining items are packed, handed to the courier, and progress through transit to `Out-for-delivery`.
- **Step 14: `on_cancel (on_cancel_rto)` [Unsolicited] (BPP -> BAP)**: At the buyer's doorstep, the delivery agent cannot reach the customer. The seller initiates an RTO with cancellation reason code `013` (Buyer unreachable / delivery refused).
- **Step 15: `/update (update_settlement_trail_1)` (BAP -> BPP)**: The BAP submits updated settlement terms accounting for approved return shipping deductions.
- **Step 16: `on_status (on_status_rto_delivered)` [Unsolicited] (BPP -> BAP)**: The shipment is returned safely to the seller's origin warehouse; `fulfillment.state` and `order.state` update to `Cancelled`.

---

### Flow 5: Out of Stock Error Handling (Inventory Shortage)

- **Flow ID:** `Out_of_Stock(Error_code)`
- **Config File:** `./ELECTRONICS/Out_of_Stock_Error_code_.yaml`
- **Protocol Version:** `1.2.0`
- **Use Case:** `ELECTRONICS`
- **Tags:** `WORKBENCH`, `PRAMAAN`, `MANDATORY`, `REPORTABLE`

#### 1. Short Description
Validates protocol exception handling when a buyer selects an electronics product or specific hardware variant that is depleted in seller inventory. The BPP responds immediately on `/on_select` with structured out-of-stock error codes.

#### 2. API Breakdown & Technical Actions
- **Step 1: `/select (select0)` (BAP -> BPP)**: The buyer selects a specific device model, color, or configuration.
- **Step 2: `/on_select (on_select_out_of_stock)` (BPP -> BAP)**: The seller identifies that the inventory is exhausted. It returns an error response with error code `40002` (Out of Stock) or `30009` and item availability count `0`, preventing checkout progression.

---

### Flow 6: Search and Custom Menu: Full Catalog City Discovery

- **Flow ID:** `Search_and_Custom_Menu_(Full_Catalog_City)`
- **Config File:** `./ELECTRONICS/Search_and_Custom_Menu__Full_Catalog_City_.yaml`
- **Protocol Version:** `1.2.0`
- **Use Case:** `ELECTRONICS`
- **Tags:** `WORKBENCH`, `PRAMAAN`, `MANDATORY`, `REPORTABLE`

#### 1. Short Description
City-wide broadcast discovery where a buyer app searches for consumer electronics products and receives comprehensive seller catalogs with custom menus, category trees, detailed hardware specifications, warranty terms, and transparent pricing.

#### 2. API Breakdown & Technical Actions
- **Step 1: `/search (search_1)` (BAP -> BPP via Gateway)**: The BAP broadcasts a discovery search specifying domain `ONDC:RET14` and city location coordinates.
- **Step 2: `/on_search (on_search1)` (BPP -> BAP)**: Active electronics sellers return full catalog payloads featuring product taxonomies, custom menu groupings (e.g., "Smartphones", "Laptops & Peripherals", "Home Appliances"), detailed hardware attributes, warranty terms, and Legal Metrology compliance data.

---

### Flow 7: Search and Custom Menu: Incremental Catalog Push

- **Flow ID:** `Search_and_Custom_Menu_(Incremental_Push)`
- **Config File:** `./ELECTRONICS/Search_and_Custom_Menu__Incremental_Push_.yaml`
- **Protocol Version:** `1.2.0`
- **Use Case:** `ELECTRONICS`
- **Tags:** `WORKBENCH`, `PRAMAAN`, `MANDATORY`, `REPORTABLE`

#### 1. Short Description
Demonstrates seller-initiated incremental catalog push updates. The seller publishes real-time catalog changes—such as price drops, newly launched gadgets, updated inventory levels, and store closure/disablement notifications—via unsolicited search callbacks.

#### 2. API Breakdown & Technical Actions
- **Step 1: `/search (search_inc)` (BAP -> BPP)**: Initial search establishing connection.
- **Step 2: `on_search (on_search_inc)` [Unsolicited] (BPP -> BAP)**: The seller pushes an unsolicited incremental catalog payload containing updated device listings, revised prices, or adjusted stock quantities.
- **Step 3: `on_search (on_search_inc_close)` [Unsolicited] (BPP -> BAP)**: The seller pushes an unsolicited store disablement/closure status (e.g., closing online orders during maintenance or holiday).
- **Step 4: `/search (search_inc1)` (BAP -> BPP)**: The BAP transmits a search query acknowledging and synchronizing with the updated store state.

---

### Flow 8: Discovery Flow: Incremental Catalog Refresh Pull

- **Flow ID:** `Discovery_Flow_incremental_catalog_refresh_pull`
- **Config File:** `./ELECTRONICS/Discovery_Flow_incremental_catalog_refresh_pull.yaml`
- **Protocol Version:** `1.2.0`
- **Use Case:** `ELECTRONICS`
- **Tags:** `WORKBENCH`

#### 1. Short Description
Buyer-initiated incremental catalog refresh. The buyer app periodically polls sellers for catalog updates using timestamp filters, fetching only modified products and pricing changes without re-downloading entire city catalogs.

#### 2. API Breakdown & Technical Actions
- **Step 1: `/search (search_1)` (BAP -> BPP via Gateway)**: Baseline discovery request.
- **Step 2: `/on_search (on_search1)` (BPP -> BAP)**: Full initial catalog response.
- **Step 3: `/search (search_inc_pull)` (BAP -> BPP)**: Subsequent incremental search request bearing `tags.catalog_inc = "true"` and a timestamp filter.
- **Step 4: `/on_search (on_search_inc_pull)` (BPP -> BAP)**: The seller returns a compact delta catalog containing only products whose price, inventory, or specifications changed since the specified timestamp.

---

### Flow 9: Order to Confirm with IGM 1.0.0 Resolution

- **Flow ID:** `Order_to_confirm_to_fulfillment__Prepaid_with_igm_1.0.0`
- **Config File:** `./ELECTRONICS/Order_to_confirm_to_fulfillment__Prepaid_with_igm_1.0.0.yaml`
- **Protocol Version:** `1.2.0`
- **Use Case:** `ELECTRONICS`
- **Tags:** `WORKBENCH`, `MANDATORY`

#### 1. Short Description
A full prepaid electronics delivery lifecycle combined with post-fulfillment dispute redressal under the legacy IGM 1.0.0 architecture. Covers issue submission, seller acknowledgment with Grievance Officer details, resolution status delivery, and customer ticket closure.

#### 2. API Breakdown & Technical Actions
- **Steps 1–14 (`/select` to `on_status_order_delivered` including `/track` and `/on_track`)**: Complete forward fulfillment from cart checkout to doorstep delivery.
- **Step 15: `/issue (issue_open_100)` (BAP -> BPP)**: The buyer lodges a grievance under IGM 1.0.0 (e.g., missing charging cable or power adapter).
- **Step 16: `/on_issue (on_issue_processing_100)` (BPP -> BAP)**: The seller acknowledges the complaint, generates a ticket ID, and assigns a designated Grievance Officer.
- **Step 17: `on_issue_status (on_issue_resolved_100)` [Unsolicited] (BPP -> BAP)**: The seller investigates and issues an unsolicited resolution update detailing the remedial action taken.
- **Step 18: `/issue (issue_close_100)` (BAP -> BPP)**: The customer confirms satisfaction and closes the grievance ticket.

---

### Flow 10: Order to Confirm with IGM 2.0.0: Resolution Accepted (No Action)

- **Flow ID:** `Order_to_confirm_to_fulfillment__Prepaid_with_IGM_No_Action_v-2.0.0`
- **Config File:** `./ELECTRONICS/Order_to_confirm_to_fulfillment__Prepaid_with_IGM_No_Action_v-2.0.0.yaml`
- **Protocol Version:** `1.2.0`
- **Use Case:** `ELECTRONICS`
- **Tags:** `WORKBENCH`, `MANDATORY`

#### 1. Short Description
Prepaid order fulfillment followed by an IGM 2.0.0 dispute where the seller investigates the claim, determines that the device operates strictly within standard manufacturer specifications or that the issue stems from third-party accessories, and provides a justified `NO_ACTION` resolution that the buyer accepts.

#### 2. API Breakdown & Technical Actions
- **Steps 1–14 (`/select` to `on_status_order_delivered` including `/track` and `/on_track`)**: Standard prepaid forward order and delivery lifecycle.
- **Step 15: `/issue (issue_open_2)` (BAP -> BPP)**: The buyer opens a complaint under IGM 2.0.0 (e.g., alleging non-functioning fast charging).
- **Step 16: `/on_issue (on_issue_processing)` (BPP -> BAP)**: The seller acknowledges the issue.
- **Step 17: `on_issue (on_issue_resolution_igm_3)` [Unsolicited] (BPP -> BAP)**: Following technical assessment, the seller provides an explanatory `NO_ACTION` resolution demonstrating that the device requires a compatible high-wattage USB-PD adapter.
- **Step 18: `/issue (issue_resolution_accept_igm_3)` (BAP -> BPP)**: The buyer reviews and accepts the seller's explanation.
- **Step 19: `/on_issue (on_issue_resolved_igm_3)` (BPP -> BAP)**: The seller confirms the resolved status.
- **Step 20: `/issue (issue_close_igm_3)` (BAP -> BPP)**: The buyer closes the dispute.
- **Step 21: `on_status (on_status_igm_3)` [Unsolicited] (BPP -> BAP)**: The seller synchronizes the final order audit record.

---

### Flow 11: Order to Confirm with IGM 2.0.0: Rejection, Escalation and Return

- **Flow ID:** `Order_to_confirm_to_fulfillment__Prepaid_with_IGM_Rejection_v-2.0.0`
- **Config File:** `./ELECTRONICS/Order_to_confirm_to_fulfillment__Prepaid_with_IGM_Rejection_v-2.0.0.yaml`
- **Protocol Version:** `1.2.0`
- **Use Case:** `ELECTRONICS`
- **Tags:** `WORKBENCH`, `MANDATORY`

#### 1. Short Description
A comprehensive dispute escalation flow. The buyer reports hardware physical damage, rejects the merchant's initial settlement offers, escalates the matter to a Level 2 Grievance Officer, receives a favorable mediator ruling, and the seller triggers reverse courier pickup and refund settlement.

#### 2. API Breakdown & Technical Actions
- **Steps 1–14 (`/select` to `on_status_order_delivered` including `/track` and `/on_track`)**: Standard prepaid forward order and delivery.
- **Step 15: `/issue (issue_open)` (BAP -> BPP)**: The buyer opens a dispute reporting severe transit casing damage.
- **Step 16: `/on_issue (on_issue_processing)` (BPP -> BAP)**: Initial seller acknowledgment.
- **Step 17: `on_issue (on_issue_resolution)` [Unsolicited] (BPP -> BAP)**: The seller proposes a nominal accessory voucher.
- **Step 18: `/issue (issue_resolution_reject)` (BAP -> BPP)**: The buyer rejects the inadequate resolution.
- **Step 19: `/on_issue (on_issue_processing_1)` (BPP -> BAP)**: Seller acknowledges rejection.
- **Step 20: `on_issue (on_issue_resolution_1)` [Unsolicited] (BPP -> BAP)**: Seller offers a revised settlement.
- **Step 21: `/issue (issue_escalate)` (BAP -> BPP)**: The buyer escalates the unresolved grievance to a Level 2 Grievance Officer / Network Intermediary.
- **Step 22: `/on_issue (on_issue_processing_2)` (BPP -> BAP)**: Escalation acknowledged.
- **Step 23: `on_issue (on_issue_resolution_2)` [Unsolicited] (BPP -> BAP)**: Level 2 arbitrator reviews unboxing photos and rules in favor of full product return and refund.
- **Step 24: `/issue (issue_resolution_accept)` (BAP -> BPP)**: The buyer accepts the escalated ruling.
- **Step 25: `/on_issue (on_issue_resolved)` (BPP -> BAP)**: Issue marked resolved.
- **Step 26: `/issue (issue_close)` (BAP -> BPP)**: Dispute officially closed.
- **Step 27: `on_update (on_update_igm_return)` [Unsolicited] (BPP -> BAP)**: The seller initiates reverse logistics pickup and refund settlement.

---

### Flow 12: Order to Confirm with IGM 2.0.0: Evidence Exchange and Item Replacement

- **Flow ID:** `Order_to_confirm_to_fulfillment__Prepaid_with_IGM_v-2.0.0`
- **Config File:** `./ELECTRONICS/Order_to_confirm_to_fulfillment__Prepaid_with_IGM_v-2.0.0.yaml`
- **Protocol Version:** `1.2.0`
- **Use Case:** `ELECTRONICS`
- **Tags:** `WORKBENCH`, `MANDATORY`

#### 1. Short Description
Exercises an interactive IGM 2.0.0 evidence exchange workflow. The buyer reports a dead-on-arrival / defective electronic device, the seller requests additional photographic and serial number proof, the buyer supplies the evidence, and the seller approves and dispatches an item replacement with reverse pickup.

#### 2. API Breakdown & Technical Actions
- **Steps 1–14 (`/select` to `on_status_order_delivered` including `/track` and `/on_track`)**: Standard prepaid delivery lifecycle.
- **Step 15: `/issue (issue_open)` (BAP -> BPP)**: The buyer opens an issue reporting hardware failure (unit fails to power on).
- **Step 16: `/on_issue (on_issue_processing)` (BPP -> BAP)**: Initial seller acknowledgment.
- **Step 17: `on_issue (on_issue_need_more_info)` [Unsolicited] (BPP -> BAP)**: The seller requests additional diagnostic evidence: photographs of the serial number / IMEI sticker and a video of the charging indicator.
- **Step 18: `/issue (issue_info_provided)` (BAP -> BPP)**: The buyer uploads and transmits the requested image and video URLs.
- **Step 19: `/on_issue (on_issue_provided)` (BPP -> BAP)**: The seller acknowledges receipt of the diagnostic evidence.
- **Step 20: `on_issue (on_issue_resolution)` [Unsolicited] (BPP -> BAP)**: The seller validates the hardware defect and proposes an item `REPLACEMENT` resolution.
- **Step 21: `/issue (issue_resolution_accept)` (BAP -> BPP)**: The buyer accepts the replacement remedy.
- **Step 22: `/on_issue (on_issue_resolved)` (BPP -> BAP)**: The seller confirms resolution agreement.
- **Step 23: `/issue (issue_close)` (BAP -> BPP)**: The buyer closes the grievance.
- **Step 24: `on_update (on_update_igm_replacement)` [Unsolicited] (BPP -> BAP)**: The seller initiates an unsolicited order update scheduling a replacement fulfillment leg (dispatching a new replacement unit and picking up the defective item).

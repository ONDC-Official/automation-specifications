# Retail Appliances (ONDC:RET15 1.2.0)

- [Overview](#overview)
- [Participants](#participants)
- [The User Journey](#the-user-journey)
  - [1. Discovery and Catalog Search](#1-discovery-and-catalog-search)
  - [2. Model/Capacity Selection and Serviceability Check](#2-modelcapacity-selection-and-serviceability-check)
  - [3. Order Initialization and Shipping Configuration](#3-order-initialization-and-shipping-configuration)
  - [4. Order Confirmation and Prepaid Escrow](#4-order-confirmation-and-prepaid-escrow)
  - [5. Order Processing, Picking, and Serial Number Verification](#5-order-processing-picking-and-serial-number-verification)
  - [6. Heavy Freight Logistics and Delivery Slot Allocation](#6-heavy-freight-logistics-and-delivery-slot-allocation)
  - [7. Order Dispatch, In-Flight Tracking, and Secure Delivery](#7-order-dispatch-in-flight-tracking-and-secure-delivery)
  - [8. Settlement and Installation Coordination](#8-settlement-and-installation-coordination)
- [Additional Scenarios](#additional-scenarios)
  - [1. Buyer-Initiated Return and Reverse QC Pickup (Full and Partial Order)](#1-buyer-initiated-return-and-reverse-qc-pickup-full-and-partial-order)
  - [2. Buyer-Side Order Cancellation](#2-buyer-side-order-cancellation)
  - [3. Merchant-Side Part-Cancellation and Return to Origin (RTO)](#3-merchant-side-part-cancellation-and-return-to-origin-rto)
  - [4. Out of Stock and Capacity Variant Depletion](#4-out-of-stock-and-capacity-variant-depletion)
  - [5. Incremental Catalog Refresh (Push and Pull)](#5-incremental-catalog-refresh-push-and-pull)
  - [6. Statutory Compliance, BEE Star Labeling, and BIS Standards](#6-statutory-compliance-bee-star-labeling-and-bis-standards)
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

The Home Appliances domain (**ONDC:RET15**, specification version **1.2.0**) establishes an open, interoperable digital commerce standard for domestic appliances, consumer durables, white goods, and kitchen equipment across the Open Network for Digital Commerce (ONDC). The appliances retail domain encompasses major household appliances (refrigerators, split and window air conditioners, front-load and top-load washing machines, dishwashers, deep freezers, kitchen chimneys, water purifiers, and water heaters/geysers) as well as small domestic appliances (microwave ovens, induction cooktops, mixer grinders, air fryers, vacuum cleaners, and electric fans).

Appliance retail is distinguished by several critical operational and commercial attributes:
1. **Bulky Freight and Specialized Handling**: Major appliances represent large volumetric weight and heavy physical cargo requiring specialized two-person handling, lift-gate vehicles, vertical orientation safeguards (to prevent compressor oil migration in refrigeration units), and transit bolt protections for washing machines.
2. **Technical Specifications & Capacity Hierarchy**: Purchases are driven by technical parameters—such as cooling tonnage (e.g. 1.0T, 1.5T, 2.0T), storage capacity in liters, washing load in kilograms, inverter compressor technologies, and input wattage.
3. **Mandatory Energy Star Ratings**: Bureau of Energy Efficiency (BEE) energy star labeling is legally mandated in India for key appliances, requiring transparent disclosure of star ratings, Indian Seasonal Energy Efficiency Ratio (ISEER) metrics, and annual kilowatt-hour (kWh) electricity consumption.
4. **Installation & Commissioning Workflows**: Large appliances almost universally require authorized unboxing, leveling, plumbing, wall-mounting, or electrical commissioning to prevent transit damage disputes and ensure manufacturer warranty coverage.
5. **Rigorous Reverse QC**: High unit values and expensive reverse freight necessitate stringent verification (checking compressor/motor serial numbers, physical cabinet dents, intact copper piping, and included accessories) prior to return authorization and refund disbursement.

ONDC unbundles the traditionally centralized appliance e-commerce marketplace. Consumers can discover appliances across multi-brand superstores, regional appliance distributors, authorized brand outlets, and independent local electronics dealers using their preferred **Buyer Application (BAP)**. Sellers manage their inventory, serial numbers, warranty terms, and transparent pricing through a **Seller Application (BPP)**, while specialized **Logistics Service Providers (LSPs)** execute heavy-freight delivery, scheduled appointment slotting, and doorstep reverse logistics.

The protocol standardizes all network interactions across:
- **Discovery**: `/search` and `/on_search` (city-wide broadcast queries, category taxonomies, capacity hierarchies, energy star attributes, and incremental catalog synchronization).
- **Ordering**: `/select`, `/on_select`, `/init`, `/on_init`, `/confirm`, and `/on_confirm`.
- **Fulfillment & Real-time Tracking**: Unsolicited `/on_status` lifecycle events (`Accepted`, `Packed`, `Agent-assigned`, `Order-picked-up`, `Out-for-delivery`, `Order-delivered`), `/track`, and `/on_track`.
- **Post-Order Lifecycle & Exceptions**: `/update`, `/on_update`, `/cancel`, and `/on_cancel` (doorstep quality-checked returns, reverse logistics pickup, warehouse bench diagnostics, merchant part-cancellations, and Return to Origin / RTO).
- **Grievance Redressal**: Issue and Grievance Management under both **IGM 1.0.0** and **IGM 2.0.0** architectures.

---

## Participants

| Participant | What This Means |
|---|---|
| **Buyer Application (BAP)** | The consumer-facing digital application (e.g., consumer durables shopping apps, banking portals, super-apps, telco marketplaces) where shoppers search appliance catalogs, filter by capacity and BEE energy star ratings, compare manufacturer warranties, configure delivery addresses, complete prepaid payments, track freight delivery in real time, and raise post-delivery grievances. |
| **Seller Application (BPP)** | An application representing appliance retail chains, direct-to-consumer (D2C) home appliance brands, authorized distributors, regional appliance dealerships, or multi-brand electronics retailers. The BPP publishes item catalogs with capacity and energy specifications, validates delivery serviceability and staircase accessibility, calculates quotes, manages compressor/appliance serial numbers during packing, and coordinates reverse QC inspections. |
| **Logistics Service Provider (LSP)** | A delivery network participant that executes heavy-freight cargo transport (specialized appliance transport with two-person delivery crews and lift-gate vehicles). In seller-managed logistics, the BPP or its integrated delivery partner allocates freight carriers, provides live tracking, coordinates delivery appointments, captures secure OTP delivery verification, and executes reverse logistics pickups with doorstep physical checks. |
| **Gateway** | The ONDC routing infrastructure that multicasts broadcast discovery requests (`/search`) from BAPs to active seller applications (BPPs) based on domain code (`ONDC:RET15`), city code (e.g. `std:080`), and geolocation parameters. |

---

## The User Journey

The standard appliances ordering journey (`Order_to_confirm_to_fulfillment_(Prepaid)`) enables a consumer to search for household appliances, compare energy efficiency ratings and capacities, review transparent price breakdowns and freight turnaround times, provide delivery coordinates, complete prepaid payment, and receive securely crated appliances with continuous shipment tracking.

### 1. Discovery and Catalog Search

The buyer initiates discovery on the BAP by searching for home appliances, capacity variants, or specific categories (e.g., "Inverter Split AC 1.5 Ton 5 Star", "Double Door Refrigerator 260L", "Front Load Washing Machine 7kg"):

- **Intent Broadcast**: The BAP transmits an asynchronous `/search` request via the ONDC Gateway specifying domain `ONDC:RET15`, buyer geolocation coordinates, city code, and fulfillment type (`Delivery`).
- **Catalog Delivery**: Active BPPs within the serviceable area respond with asynchronous `/on_search` payloads containing their store catalog (`bpp/providers[]`). This includes appliance categories, custom menu groupings, brand metadata, model numbers, hardware specifications (capacity, BEE star rating, annual electricity consumption, compressor warranty duration, dimensions, weight), MRP, discounted selling price, stock availability, warranty disclosure (comprehensive vs. compressor/motor warranty), and statutory Legal Metrology attributes.

### 2. Model/Capacity Selection and Serviceability Check

The buyer selects an exact appliance model or capacity configuration (e.g., 1.5 Ton 5-Star Dual Inverter Split AC) and proceeds to configure checkout:

- **Network interaction:**
  - **`/select` (BAP -> BPP)**: The BAP transmits the selected item ID, capacity variant specifications, quantity, provider location ID, and delivery destination coordinates (`fulfillments[0].end.location.gps` and `address.area_code`).
  - **`/on_select` (BPP -> BAP)**: The seller validates real-time inventory at the appliance warehouse, confirms heavy-freight delivery serviceability, and computes a detailed quote breakdown (`quote.breakup[]`). This includes the appliance base price, applicable taxes (CGST/SGST), protective heavy-freight crating fees, logistics shipping charges, and estimated turnaround time (`@ondc/org/TAT`). If the requested appliance or capacity variant is depleted, the seller responds with an out-of-stock protocol error code (`40002` or `30009`).

### 3. Order Initialization and Shipping Configuration

The buyer confirms recipient information and finalized delivery coordinates:

- **Network interaction:**
  - **`/init` (BAP -> BPP)**: The BAP transmits customer details (name, phone number, email), exact street address, floor number, elevator availability notice, delivery instructions (e.g., heavy freight lift-gate access), and payment preference.
  - **`/on_init` (BPP -> BAP)**: The seller freezes the item quote and turnaround time, specifies static and dynamic order terms (cancellation window, return eligibility duration, authorized technician installation coordination link), establishes payment collection requirements (prepaid BAP-collected transaction), and returns settlement fee details.

### 4. Order Confirmation and Prepaid Escrow

Because home appliances represent high-value consumer durables, transactions follow a prepaid escrow model:

- **Network interaction:**
  - **`/confirm` (BAP -> BPP)**: The BAP captures digital payment from the buyer via UPI, credit card, net banking, or consumer finance/EMI, generates a unique order identifier (`order.id`), and transmits payment confirmation parameters (`payment.params.transaction_id`, `payment.status = "PAID"`, `payment.type = "PRE-PAID"`).
  - **`/on_confirm` (BPP -> BAP)**: The seller validates payment receipt, records the order in its Warehouse Management / Order Management System (WMS/OMS), initializes order state (`order.state = "Created"`), and sets the primary fulfillment status to `Pending`.

### 5. Order Processing, Picking, and Serial Number Verification

The seller initiates warehouse fulfillment operations:

- The warehouse picks the appliance crated unit from heavy-duty pallet racks.
- The merchant scans and registers the unit's unique appliance serial number, compressor/motor serial code, and warranty barcode against the order record to safeguard against return fraud.
- The appliance undergoes reinforced packaging: high-density polystyrene shock corners, shrink-wrap moisture barriers, and heavy-duty strapping bands.
- **Protocol Status Progression:**
  - **`on_status (on_status_pending)` [Unsolicited] (BPP -> BAP)**: Merchant system acknowledges order processing; `order.state` advances to `Accepted`.
  - **`on_status (on_status_packed)` [Unsolicited] (BPP -> BAP)**: Unit is securely palletized and crated with invoice and warranty card inside; `fulfillment.state` updates to `Packed` and `order.state` to `In-progress`.

### 6. Heavy Freight Logistics and Delivery Slot Allocation

The seller or its integrated Logistics Service Provider assigns a dedicated appliance freight carrier:

- A two-person delivery team equipped for heavy cargo handling is allocated to the shipment.
- **Protocol Status Progression:**
  - **`on_status (on_status_agent_assigned)` [Unsolicited] (BPP -> BAP)**: Freight carrier details (team lead name, masked phone number, commercial vehicle number) are transmitted; `fulfillment.state` transitions to `Agent-assigned`.
  - **`on_status (on_status_picked)` [Unsolicited] (BPP -> BAP)**: Delivery team verifies crate integrity, scans airway bill barcode, loads unit vertically, and departs warehouse; `fulfillment.state` transitions to `Order-picked-up`.

### 7. Order Dispatch, In-Flight Tracking, and Secure Delivery

The heavy-freight vehicle moves toward the buyer's destination:

- **Real-Time Tracking:**
  - **`/track` (BAP -> BPP)**: The BAP queries live shipment coordinates.
  - **`/on_track` (BPP -> BAP)**: The BPP or LSP returns real-time GPS telemetry and an active web tracking URL (`tracking.url`).
- **Doorstep Authentication & Handover:**
  - **`on_status (on_status_out_for_delivery)` [Unsolicited] (BPP -> BAP)**: Delivery truck is in the immediate sector; `fulfillment.state` transitions to `Out-for-delivery`.
  - At the doorstep, the delivery crew carefully offloads the appliance, brings it into the customer's residence (navigating stairs/elevators), and requests a secure one-time password (OTP) generated on the buyer's app to verify identity prior to physical handover. The delivery team and customer inspect external box strapping and seal tape for any transit impacts.
  - **`on_status (on_status_order_delivered)` [Unsolicited] (BPP -> BAP)**: Successful handover is confirmed; `fulfillment.state` transitions to `Order-delivered` and `order.state` reaches terminal state `Completed`.

### 8. Settlement and Installation Coordination

Upon successful delivery completion:
- The return window countdown timer begins (typically 7 to 10 days for appliances, subject to seller policy).
- The seller or brand-authorized service center coordinates technician scheduling for installation, wall-mounting, unboxing inspection, and water/power commissioning.
- The BAP releases funds from escrow to the seller's account net of network fees, taxes, and freight logistics charges in accordance with ONDC settlement guidelines.
- The buyer receives a tax invoice enabling registration for manufacturer warranty coverage.

---

## Additional Scenarios

Beyond standard prepaid delivery, ONDC:RET15 defines standardized workflows for post-delivery returns, pre-dispatch cancellations, stock exceptions during warehouse picking, failed deliveries (RTO), and continuous catalog synchronization.

### 1. Buyer-Initiated Return and Reverse QC Pickup (Full and Partial Order)

Appliance returns involve high freight costs and require strict physical verification to prevent fraud and assess genuine transit or manufacturing damage. The domain defines an end-to-end 18-step return flow (`Buyer_Initiated_Return_(Full_Order_and_Partial_Order)`):

- **Return Initiation (`/update` - `update_return`)**: Within the return window, the shopper initiates a return request specifying the return reason code (e.g., Dead-on-Arrival / DOA, severe transit dent, damaged compressor, unresolvable technical defect), uploading mandatory unboxing/technician inspection photos, and selecting full-order or partial-item return (e.g., returning a microwave while retaining a mixer grinder).
- **Merchant Evaluation (`/on_update` - `on_update_return_init` & `on_update_return_approved`)**: The seller reviews the uploaded evidence and technician report, validates that the fault falls within return policy terms, and emits an unsolicited `on_update` approving the return and creating a reverse freight logistics leg.
- **Doorstep Reverse Quality Check (`/on_update` - `on_update_return_picked`)**: A reverse logistics team arrives at the buyer's residence. The team conducts a rigorous inspection:
  - Verifying the serial number / barcode on the appliance against the original dispatch record.
  - Checking that no unauthorized alterations, third-party repairs, or physical drops occurred.
  - Ensuring all original installation accessories (inlet/outlet hoses, remote controls, user manuals, mounting brackets) are collected.
  - Upon successful verification, the team crates the unit and emits an unsolicited `on_update` marking the return fulfillment as picked up.
- **Settlement & Warehouse Bench Verification (`/update` - `update_settlement_trail` & `/on_update` - `on_update_return_delivered`)**: The BAP transmits updated settlement trail details. When the unit arrives at the merchant facility, technicians conduct bench diagnostics. Once verified, the seller emits `on_update` confirming delivery and releases the refund settlement to the buyer.

### 2. Buyer-Side Order Cancellation

Consumers may cancel an order before warehouse dispatch (`Buyer_Side_Order_Cancellation`):

- **Pre-Dispatch Cancellation (`/cancel`)**: The buyer requests cancellation from the BAP interface prior to freight courier pickup, providing a standardized cancellation reason code (e.g., `001` - Order placed by mistake, `003` - Delivery delay anticipated).
- **Merchant Validation (`/on_cancel`)**: The BPP verifies that the order has not passed the non-cancellable threshold (`@ondc/org/cancellable = true`). The merchant immediately aborts picking, releases reserved warehouse inventory, transitions `order.state = "Cancelled"` and `fulfillment.state = "Cancelled"`, and triggers an automated full refund to the buyer's original payment method.

### 3. Merchant-Side Part-Cancellation and Return to Origin (RTO)

A dual-exception lifecycle (`Merchant_Side_RTO_and_Part_Order_Cancellation_Flow`) handling inventory discrepancies during picking and failed doorstep deliveries:

- **Warehouse Part-Cancellation (`on_update` - `on_update_part_cancel`)**: In a multi-item appliance order (e.g., a refrigerator and a microwave oven), the merchant identifies during warehouse staging that the requested microwave has sustained carton puncture damage and no replacement unit is available. The seller issues an unsolicited `on_update` cancelling that specific line item while keeping the refrigerator active. The BAP acknowledges and updates the settlement trail (`/update`) to refund the cancelled item.
- **Outbound Freight Dispatch**: The remaining serviceable appliance is crated, loaded onto the freight truck, and progresses through transit to `Out-for-delivery`.
- **Doorstep Delivery Failure & RTO (`on_cancel` - `on_cancel_rto`)**: The delivery crew reaches the destination, but the customer is unreachable after multiple phone calls, or the customer refuses to provide the delivery OTP. The freight carrier initiates a Return to Origin (RTO) with cancellation reason code `013` (Buyer unreachable / delivery refused).
- **Settlement Adjustment & Origin Delivery (`/update` & `on_status` - `on_status_rto_delivered`)**: The BAP submits updated settlement terms to deduct approved two-way freight logistics costs. When the appliance arrives back at the merchant facility, the merchant issues an unsolicited `on_status` marking the RTO shipment delivered and closing the transaction.

### 4. Out of Stock and Capacity Variant Depletion

When inventory for a specific appliance model, tonnage, or star-rating configuration is exhausted:

- **Immediate Error Response (`Out_of_Stock(Error_code)`)**: When a buyer submits a `/select` request for an out-of-stock appliance or depleted capacity variant, the BPP immediately rejects the selection on `/on_select` with protocol error code `40002` (Out of Stock) or `30009` and sets `quantity.available.count = 0`. This prevents impossible checkouts and prompts the buyer app to display unavailable stock clearly.

### 5. Incremental Catalog Refresh (Push and Pull)

Appliance catalogs experience regular price updates, energy star label revisions, seasonal promotional discounts, and store operating hours:

- **Incremental Push (`Search_and_Custom_Menu_(Incremental_Push)`)**: The seller proactively publishes catalog delta updates via unsolicited `/on_search` payloads containing only modified items, revised pricing, or updated stock levels. Sellers can also push store closure or maintenance disablement messages (`on_search_inc_close`) to temporarily suspend incoming orders.
- **Incremental Pull (`Discovery_Flow_incremental_catalog_refresh_pull`)**: The buyer app periodically polls for catalog changes by transmitting a `/search` request with tag `catalog_inc = "true"` and a timestamp filter. The BPP responds via `/on_search` with only the delta changes recorded since that timestamp, optimizing bandwidth and compute.

### 6. Statutory Compliance, BEE Star Labeling, and BIS Standards

Retail appliance listings on ONDC are subject to strict Indian regulatory and consumer protection standards:

- **Bureau of Energy Efficiency (BEE) Star Labeling**: Under the Energy Conservation Act, 2001, BEE energy labels (1 to 5 stars) are mandatory for appliances including frost-free and direct-cool refrigerators, room air conditioners, electric water heaters, and washing machines. Catalogs must explicitly publish the star rating, appliance energy efficiency metric (e.g., ISEER for air conditioners), annual electricity consumption (kWh/year), and label validity period.
- **BIS Certification & Compulsory Registration Scheme**: All electrical appliances must comply with safety standards established by the Bureau of Indian Standards (BIS) and carry valid ISI or CRS registration marks.
- **E-Waste (Management) Rules, 2022**: Appliance manufacturers and retailers must disclose Extended Producer Responsibility (EPR) registration numbers, safe disposal guidelines, and authorized take-back / recycling collection channels.
- **Legal Metrology (Packaged Commodities) Rules, 2011**: Product listings must explicitly publish the country of origin, manufacturer and importer details, date of manufacture/import, Maximum Retail Price (MRP inclusive of all taxes), appliance dimensions (height, width, depth in cm), gross weight, and customer grievance redressal contact information.

---

## Issue and Grievance Management

ONDC specifies structured dispute resolution mechanisms to handle post-order grievances—such as transit damage, dead-on-arrival compressors, missing installation kits, or delayed deliveries—under both **IGM 1.0.0** and **IGM 2.0.0** architectures.

### 1. IGM 1.0.0 Architecture

IGM 1.0.0 provides a single-ticket grievance lifecycle between the buyer application and seller application:

- **Issue Filing (`/issue` - `issue_open_100`)**: The buyer submits a formal grievance via the BAP specifying the complaint category, subcategory (e.g., `TRANSIT_DAMAGE`, `DEFECTIVE_PRODUCT`, `MISSING_ACCESSORIES`), narrative description, and contact details.
- **Issue Acknowledgment (`/on_issue` - `on_issue_processing_100`)**: The BPP acknowledges the issue, assigns an internal ticket identifier, and furnishes the details of the designated Grievance Officer.
- **Issue Resolution (`on_issue_status` [Unsolicited] - `on_issue_resolved_100`)**: The seller investigates the claim and publishes a resolution payload detailing the remedial action taken (e.g., dispatching missing inlet pipes, arranging a technician inspection, or approving a partial refund).
- **Issue Closure (`/issue` - `issue_close_100`)**: The buyer verifies that the grievance has been satisfactorily addressed and emits an issue closure message.

### 2. IGM 2.0.0 Architecture

IGM 2.0.0 introduces a robust, multi-participant, role-based dispute framework featuring evidence exchange, technician diagnostic reports, multiple resolution remedies (`REFUND`, `REPLACEMENT`, `NO_ACTION`), and formal escalation paths to Level 2 Grievance Officers and Network Intermediaries:

1. **Resolution Accepted with `NO_ACTION` (`Order_to_confirm_to_fulfillment__Prepaid_with_IGM_No_Action_v-2.0.0`)**:
   - The buyer opens a grievance alleging a technical fault (e.g., air conditioner not cooling adequately).
   - An authorized technician inspects the site and finds that the unit is operating strictly within manufacturer specifications and that the cooling inadequacy is caused by an unclosed window or incorrect remote temperature setting.
   - The seller issues an unsolicited `on_issue` with resolution action `NO_ACTION`, accompanied by the technician's site inspection report and guidance on optimal operating conditions.
   - The buyer accepts the technical explanation (`/issue`), the ticket is closed, and the seller synchronizes the final order audit record via an unsolicited `on_status`.

2. **Rejection, Escalation & Return Authorization (`Order_to_confirm_to_fulfillment__Prepaid_with_IGM_Rejection_v-2.0.0`)**:
   - The buyer reports physical cabinet denting and a cracked drain pan upon unboxing.
   - The merchant initially proposes a minor cosmetic coupon or nominal discount.
   - The buyer rejects the resolution (`issue_resolution_reject`).
   - The merchant attempts a revised proposal, which the buyer also rejects, subsequently escalating the dispute to a Level 2 Grievance Officer / Network Intermediary (`issue_escalate`).
   - The escalated mediator reviews unboxing photos and technician damage reports, ruling in favor of the buyer and ordering full product return and refund.
   - The buyer accepts the escalated ruling, the dispute is closed, and the seller triggers reverse freight pickup and refund settlement via an unsolicited `on_update` (`on_update_igm_return`).

3. **Evidence Exchange & Hardware Replacement (`Order_to_confirm_to_fulfillment__Prepaid_with_IGM_v-2.0.0`)**:
   - The buyer lodges a grievance reporting that a newly delivered washing machine will not power on (Dead-on-Arrival).
   - Rather than immediate rejection, the BPP requests additional verification via an unsolicited `on_issue` (`on_issue_need_more_info`), requesting photographs of the serial number sticker on the rear chassis, electrical outlet testing, and a short video of the power switch failure.
   - The buyer provides the requested media URLs via `/issue` (`issue_info_provided`).
   - The seller's technical team validates the defect and issues an unsolicited resolution approving an item `REPLACEMENT`.
   - The buyer accepts the replacement resolution, and the seller executes an unsolicited `on_update` (`on_update_igm_replacement`), scheduling a freight swap: delivering a brand-new replacement appliance while collecting the defective unit for factory analysis.

---

## Detailed Protocol Flows

All **12 protocol flows** defined in `automation-specifications/config/flows/index.yaml` for the Appliances domain (`ONDC:RET15 1.2.0`) are detailed below with their classification tags, operational contexts, and full step-by-step API message sequences.

---

### Flow 1: Order to Confirm to Fulfillment (Prepaid Standard Delivery)

- **Flow ID:** `Order_to_confirm_to_fulfillment_(Prepaid)`
- **Config File:** `./APPLIANCES/Order_to_confirm_to_fulfillment__Prepaid_.yaml`
- **Protocol Version:** `1.2.0`
- **Use Case:** `APPLIANCES`
- **Tags:** `WORKBENCH`, `PRAMAAN`, `MANDATORY`, `REPORTABLE`

#### 1. Short Description
The canonical end-to-end forward fulfillment journey for consumer home appliances. Covers product selection, capacity and energy rating verification, delivery initialization, prepaid payment capture, warehouse picking with compressor/appliance serial number registration, multi-stage freight status updates, live GPS tracking, and secure OTP-authenticated doorstep delivery.

#### 2. API Breakdown & Technical Actions
- **Step 1: `/select (select)` (BAP -> BPP)**: The BAP selects an appliance model, specifying delivery destination coordinates, floor details, and fulfillment type.
- **Step 2: `/on_select (on_select)` (BPP -> BAP)**: The seller confirms product inventory, returns an itemized price breakdown (`quote.breakup[]`), confirms freight serviceability (`Fulfillment: Serviceable`), and quotes delivery turnaround time.
- **Step 3: `/init (init)` (BAP -> BPP)**: The BAP transmits customer details, billing address, exact delivery location, and prepaid payment preference to initiate the order draft.
- **Step 4: `/on_init (on_init)` (BPP -> BAP)**: The seller responds with frozen commercial terms, payment parameters, cancellation windows, installation coordination terms, and settlement rules.
- **Step 5: `/confirm (confirm)` (BAP -> BPP)**: The BAP captures prepaid digital payment and submits the confirmed order with `order.state = "Created"`.
- **Step 6: `/on_confirm (on_confirm)` (BPP -> BAP)**: The seller validates payment, records the order in OMS/WMS, confirms `order.state = "Created"`, and sets initial fulfillment state to `Pending`.
- **Step 7: `on_status (on_status_pending)` [Unsolicited] (BPP -> BAP)**: The merchant confirms warehouse order processing; `order.state` transitions to `Accepted`.
- **Step 8: `on_status (on_status_packed)` [Unsolicited] (BPP -> BAP)**: The appliance is picked from warehouse pallet racks, serial numbers recorded, and unit crated with polystyrene corners and strapping bands; `fulfillment.state` updates to `Packed` and `order.state` to `In-progress`.
- **Step 9: `on_status (on_status_agent_assigned)` [Unsolicited] (BPP -> BAP)**: A two-person heavy-freight delivery team is assigned; `fulfillment.state` advances to `Agent-assigned`.
- **Step 10: `on_status (on_status_picked)` [Unsolicited] (BPP -> BAP)**: The freight carrier verifies crate integrity, loads the unit vertically, and departs warehouse; `fulfillment.state` updates to `Order-picked-up`.
- **Step 11: `/track (track)` (BAP -> BPP)**: The BAP queries live freight transit location.
- **Step 12: `/on_track (on_track)` (BPP -> BAP)**: The BPP returns real-time GPS coordinates and an active web tracking link.
- **Step 13: `on_status (on_status_out_for_delivery)` [Unsolicited] (BPP -> BAP)**: The freight vehicle arrives in the delivery sector; `fulfillment.state` transitions to `Out-for-delivery`.
- **Step 14: `on_status (on_status_order_delivered)` [Unsolicited] (BPP -> BAP)**: Secure OTP doorstep verification is completed, crate seals inspected, and the appliance is delivered; `fulfillment.state` reaches `Order-delivered` and `order.state` transitions to `Completed`.

---

### Flow 2: Buyer-Initiated Return (Full Order and Partial Order)

- **Flow ID:** `Buyer_Initiated_Return_(Full_Order_and_Partial_Order)`
- **Config File:** `./APPLIANCES/Buyer_Initiated_Return__Full_Order_and_Partial_Order_.yaml`
- **Protocol Version:** `1.2.0`
- **Use Case:** `APPLIANCES`
- **Tags:** `WORKBENCH`, `PRAMAAN`, `MANDATORY`, `REPORTABLE`

#### 1. Short Description
Exercises the complete post-delivery return lifecycle for appliances (covering both full-order and partial-item returns). Includes return request authorization, doorstep reverse freight logistics collection with compressor/motor serial number inspection, settlement trail coordination, and final warehouse technical verification and refund closure.

#### 2. API Breakdown & Technical Actions
- **Steps 1–6 (`/select` to `/on_confirm`)**: Standard prepaid order creation and payment confirmation.
- **Steps 7–12 (`on_status_accepted` to `on_status_order_delivered`)**: Full outbound fulfillment progression from warehouse crating to successful doorstep delivery.
- **Step 13: `/update (update_return)` (BAP -> BPP)**: The buyer submits a return request for eligible items within the return window, specifying return reason codes (e.g., defective compressor, physical transit damage) and unboxing/technician report photos.
- **Step 14: `/on_update (on_update_return_init)` (BPP -> BAP)**: The seller acknowledges the return request and initializes a reverse freight fulfillment leg.
- **Step 15: `on_update (on_update_return_approved)` [Unsolicited] (BPP -> BAP)**: The seller formally approves the return following photo/technician verification and authorizes reverse freight pickup.
- **Step 16: `on_update (on_update_return_picked)` [Unsolicited] (BPP -> BAP)**: A reverse pickup crew conducts doorstep physical and serial number verification, secures the appliance with protective wrap, and emits a pickup update.
- **Step 17: `/update (update_settlement_trail)` (BAP -> BPP)**: The BAP transmits revised settlement terms specifying the refund disbursement trail.
- **Step 18: `on_update (on_update_return_delivered)` [Unsolicited] (BPP -> BAP)**: The returned appliance arrives at the merchant's warehouse, undergoes technical bench inspection, and the seller confirms return closure with refund execution.

---

### Flow 3: Buyer-Side Order Cancellation

- **Flow ID:** `Buyer_Side_Order_Cancellation`
- **Config File:** `./APPLIANCES/Buyer_Side_Order_Cancellation.yaml`
- **Protocol Version:** `1.2.0`
- **Use Case:** `APPLIANCES`
- **Tags:** `WORKBENCH`, `PRAMAAN`, `MANDATORY`, `REPORTABLE`

#### 1. Short Description
Demonstrates a buyer-initiated pre-dispatch cancellation for a confirmed appliance order. The seller verifies that the order is within the allowed cancellation window, halts warehouse crating and pallet dispatch, and confirms cancellation with automated refund initiation.

#### 2. API Breakdown & Technical Actions
- **Steps 1–6 (`/select` to `/on_confirm`)**: Standard prepaid order placement, validation, and confirmation.
- **Step 7: `/cancel (cancel)` (BAP -> BPP)**: Prior to freight carrier pickup, the buyer triggers an order cancellation request citing a standardized cancellation reason code (e.g., `001` for accidental order).
- **Step 8: `/on_cancel (on_cancel)` (BPP -> BAP)**: The seller validates that the order is cancellable (`@ondc/org/cancellable = true`), halts warehouse processing, transitions `order.state = "Cancelled"` and `fulfillment.state = "Cancelled"`, and communicates refund terms.

---

### Flow 4: Merchant-Side Part-Order Cancellation and Return to Origin (RTO)

- **Flow ID:** `Merchant_Side_RTO_and_Part_Order_Cancellation_Flow`
- **Config File:** `./APPLIANCES/Merchant_Side_RTO_and_Part_Order_Cancellation_Flow.yaml`
- **Protocol Version:** `1.2.0`
- **Use Case:** `APPLIANCES`
- **Tags:** `WORKBENCH`, `PRAMAAN`, `MANDATORY`, `REPORTABLE`

#### 1. Short Description
A comprehensive dual-exception operational flow. Handles merchant stockout or damaged appliance detection during warehouse staging (part-cancellation), followed by an unsuccessful delivery attempt where the buyer is unreachable, resulting in Return to Origin (RTO) and reverse freight delivery.

#### 2. API Breakdown & Technical Actions
- **Steps 1–6 (`/select` to `/on_confirm`)**: Multi-item appliance order confirmed and prepaid.
- **Step 7: `on_update (on_update_part_cancel)` [Unsolicited] (BPP -> BAP)**: While picking items in the warehouse, the seller identifies that one specific unit is damaged or unavailable. The seller emits an unsolicited update cancelling that item and adjusting the price quote.
- **Step 8: `/update (update_settlement_trail)` (BAP -> BPP)**: The BAP acknowledges the item reduction and transmits updated settlement instructions for the partial refund.
- **Steps 9–13 (`on_status_pending` to `on_status_out_for_delivery`)**: The remaining items are crated, loaded onto the freight truck, and progress through transit to `Out-for-delivery`.
- **Step 14: `on_cancel (on_cancel_rto)` [Unsolicited] (BPP -> BAP)**: At the destination, the delivery crew cannot reach the customer. The seller initiates an RTO with cancellation reason code `013` (Buyer unreachable / delivery refused).
- **Step 15: `/update (update_settlement_trail_1)` (BAP -> BPP)**: The BAP submits updated settlement terms accounting for approved return shipping deductions.
- **Step 16: `on_status (on_status_rto_delivered)` [Unsolicited] (BPP -> BAP)**: The appliance is returned safely to the seller's origin warehouse; `fulfillment.state` and `order.state` update to `Cancelled`.

---

### Flow 5: Out of Stock Error Handling (Inventory Shortage)

- **Flow ID:** `Out_of_Stock(Error_code)`
- **Config File:** `./APPLIANCES/Out_of_Stock_Error_code_.yaml`
- **Protocol Version:** `1.2.0`
- **Use Case:** `APPLIANCES`
- **Tags:** `WORKBENCH`, `PRAMAAN`, `MANDATORY`, `REPORTABLE`

#### 1. Short Description
Validates protocol exception handling when a buyer selects a home appliance model or specific capacity variant that is depleted in seller inventory. The BPP responds immediately on `/on_select` with structured out-of-stock error codes.

#### 2. API Breakdown & Technical Actions
- **Step 1: `/select (select0)` (BAP -> BPP)**: The buyer selects a specific appliance model, tonnage, or star-rating configuration.
- **Step 2: `/on_select (on_select_out_of_stock)` (BPP -> BAP)**: The seller identifies that the inventory is exhausted. It returns an error response with error code `40002` (Out of Stock) or `30009` and item availability count `0`, preventing checkout progression.

---

### Flow 6: Search and Custom Menu: Full Catalog City Discovery

- **Flow ID:** `Search_and_Custom_Menu_(Full_Catalog_City)`
- **Config File:** `./APPLIANCES/Search_and_Custom_Menu__Full_Catalog_City_.yaml`
- **Protocol Version:** `1.2.0`
- **Use Case:** `APPLIANCES`
- **Tags:** `WORKBENCH`, `PRAMAAN`, `MANDATORY`, `REPORTABLE`

#### 1. Short Description
City-wide broadcast discovery where a buyer app searches for home appliances and receives comprehensive seller catalogs with custom menus, category trees, detailed hardware specifications (capacities, BEE star ratings, energy metrics), warranty terms, and transparent pricing.

#### 2. API Breakdown & Technical Actions
- **Step 1: `/search (search_1)` (BAP -> BPP via Gateway)**: The BAP broadcasts a discovery search specifying domain `ONDC:RET15` and city location coordinates.
- **Step 2: `/on_search (on_search1)` (BPP -> BAP)**: Active appliance sellers return full catalog payloads featuring product taxonomies, custom menu groupings (e.g., "Air Conditioners", "Refrigerators", "Washing Machines", "Kitchen Appliances"), detailed technical attributes, BEE energy star ratings, warranty terms, and Legal Metrology compliance data.

---

### Flow 7: Search and Custom Menu: Incremental Catalog Push

- **Flow ID:** `Search_and_Custom_Menu_(Incremental_Push)`
- **Config File:** `./APPLIANCES/Search_and_Custom_Menu__Incremental_Push_.yaml`
- **Protocol Version:** `1.2.0`
- **Use Case:** `APPLIANCES`
- **Tags:** `WORKBENCH`, `PRAMAAN`, `MANDATORY`, `REPORTABLE`

#### 1. Short Description
Demonstrates seller-initiated incremental catalog push updates. The seller publishes real-time catalog changes—such as seasonal promotional discounts, newly arrived appliance models, updated inventory levels, and store closure/disablement notifications—via unsolicited search callbacks.

#### 2. API Breakdown & Technical Actions
- **Step 1: `/search (search_inc)` (BAP -> BPP)**: Initial search establishing connection.
- **Step 2: `on_search (on_search_inc)` [Unsolicited] (BPP -> BAP)**: The seller pushes an unsolicited incremental catalog payload containing updated appliance listings, revised prices, or adjusted stock quantities.
- **Step 3: `on_search (on_search_inc_close)` [Unsolicited] (BPP -> BAP)**: The seller pushes an unsolicited store disablement/closure status (e.g., closing online orders during warehouse inventory count or maintenance).
- **Step 4: `/search (search_inc1)` (BAP -> BPP)**: The BAP transmits a search query acknowledging and synchronizing with the updated store state.

---

### Flow 8: Discovery Flow: Incremental Catalog Refresh Pull

- **Flow ID:** `Discovery_Flow_incremental_catalog_refresh_pull`
- **Config File:** `./APPLIANCES/Discovery_Flow_incremental_catalog_refresh_pull.yaml`
- **Protocol Version:** `1.2.0`
- **Use Case:** `APPLIANCES`
- **Tags:** `WORKBENCH`

#### 1. Short Description
Buyer-initiated incremental catalog refresh. The buyer app periodically polls sellers for catalog updates using timestamp filters, fetching only modified appliance models and pricing changes without re-downloading entire city catalogs.

#### 2. API Breakdown & Technical Actions
- **Step 1: `/search (search_1)` (BAP -> BPP via Gateway)**: Baseline discovery request.
- **Step 2: `/on_search (on_search1)` (BPP -> BAP)**: Full initial catalog response.
- **Step 3: `/search (search_inc_pull)` (BAP -> BPP)**: Subsequent incremental search request bearing `tags.catalog_inc = "true"` and a timestamp filter.
- **Step 4: `/on_search (on_search_inc_pull)` (BPP -> BAP)**: The seller returns a compact delta catalog containing only appliances whose price, inventory, or specifications changed since the specified timestamp.

---

### Flow 9: Order to Confirm with IGM 1.0.0 Resolution

- **Flow ID:** `Order_to_confirm_to_fulfillment__Prepaid_with_igm_1.0.0`
- **Config File:** `./APPLIANCES/Order_to_confirm_to_fulfillment__Prepaid_with_igm_1.0.0.yaml`
- **Protocol Version:** `1.2.0`
- **Use Case:** `APPLIANCES`
- **Tags:** `WORKBENCH`, `PRAMAAN`, `MANDATORY`, `REPORTABLE`

#### 1. Short Description
A full prepaid appliance delivery lifecycle combined with post-fulfillment dispute redressal under the legacy IGM 1.0.0 architecture. Covers issue submission, seller acknowledgment with Grievance Officer details, resolution status delivery, and customer ticket closure.

#### 2. API Breakdown & Technical Actions
- **Steps 1–14 (`/select` to `on_status_order_delivered` including `/track` and `/on_track`)**: Complete forward fulfillment from cart checkout to doorstep delivery.
- **Step 15: `/issue (issue_open_100)` (BAP -> BPP)**: The buyer lodges a grievance under IGM 1.0.0 (e.g., missing installation accessories or remote control).
- **Step 16: `/on_issue (on_issue_processing_100)` (BPP -> BAP)**: The seller acknowledges the complaint, generates a ticket ID, and assigns a designated Grievance Officer.
- **Step 17: `on_issue_status (on_issue_resolved_100)` [Unsolicited] (BPP -> BAP)**: The seller investigates and issues an unsolicited resolution update detailing the remedial action taken (e.g., dispatching missing parts or scheduling a technician visit).
- **Step 18: `/issue (issue_close_100)` (BAP -> BPP)**: The customer confirms satisfaction and closes the grievance ticket.

---

### Flow 10: Order to Confirm with IGM 2.0.0: Resolution Accepted (No Action)

- **Flow ID:** `Order_to_confirm_to_fulfillment__Prepaid_with_IGM_No_Action_v-2.0.0`
- **Config File:** `./APPLIANCES/Order_to_confirm_to_fulfillment__Prepaid_with_IGM_No_Action_v-2.0.0.yaml`
- **Protocol Version:** `1.2.0`
- **Use Case:** `APPLIANCES`
- **Tags:** `WORKBENCH`, `MANDATORY`

#### 1. Short Description
Prepaid order fulfillment followed by an IGM 2.0.0 dispute where the seller investigates the claim via an on-site technician inspection, determines that the appliance operates strictly within standard manufacturer specifications, and provides a justified `NO_ACTION` resolution that the buyer accepts.

#### 2. API Breakdown & Technical Actions
- **Steps 1–14 (`/select` to `on_status_order_delivered` including `/track` and `/on_track`)**: Standard prepaid forward order and delivery lifecycle.
- **Step 15: `/issue (issue_open_2)` (BAP -> BPP)**: The buyer opens a complaint under IGM 2.0.0 (e.g., alleging insufficient cooling on a newly installed air conditioner).
- **Step 16: `/on_issue (on_issue_processing)` (BPP -> BAP)**: The seller acknowledges the issue.
- **Step 17: `on_issue (on_issue_resolution_igm_3)` [Unsolicited] (BPP -> BAP)**: Following site inspection, the seller provides an explanatory `NO_ACTION` resolution demonstrating that the room exceeds rated square footage and windows were left open, with instructions for optimal usage.
- **Step 18: `/issue (issue_resolution_accept_igm_3)` (BAP -> BPP)**: The buyer reviews and accepts the seller's explanation.
- **Step 19: `/on_issue (on_issue_resolved_igm_3)` (BPP -> BAP)**: The seller confirms the resolved status.
- **Step 20: `/issue (issue_close_igm_3)` (BAP -> BPP)**: The buyer closes the dispute.
- **Step 21: `on_status (on_status_igm_3)` [Unsolicited] (BPP -> BAP)**: The seller synchronizes the final order audit record.

---

### Flow 11: Order to Confirm with IGM 2.0.0: Rejection, Escalation and Return

- **Flow ID:** `Order_to_confirm_to_fulfillment__Prepaid_with_IGM_Rejection_v-2.0.0`
- **Config File:** `./APPLIANCES/Order_to_confirm_to_fulfillment__Prepaid_with_IGM_Rejection_v-2.0.0.yaml`
- **Protocol Version:** `1.2.0`
- **Use Case:** `APPLIANCES`
- **Tags:** `WORKBENCH`, `MANDATORY`

#### 1. Short Description
A comprehensive dispute escalation flow. The buyer reports severe physical crate/casing damage upon unboxing, rejects the merchant's initial settlement offers, escalates the matter to a Level 2 Grievance Officer, receives a favorable mediator ruling, and the seller triggers reverse freight pickup and refund settlement.

#### 2. API Breakdown & Technical Actions
- **Steps 1–14 (`/select` to `on_status_order_delivered` including `/track` and `/on_track`)**: Standard prepaid forward order and delivery.
- **Step 15: `/issue (issue_open)` (BAP -> BPP)**: The buyer opens a dispute reporting severe cabinet denting and a cracked compressor frame.
- **Step 16: `/on_issue (on_issue_processing)` (BPP -> BAP)**: Initial seller acknowledgment.
- **Step 17: `on_issue (on_issue_resolution)` [Unsolicited] (BPP -> BAP)**: The seller proposes a nominal cosmetic voucher.
- **Step 18: `/issue (issue_resolution_reject)` (BAP -> BPP)**: The buyer rejects the inadequate resolution.
- **Step 19: `/on_issue (on_issue_processing_1)` (BPP -> BAP)**: Seller acknowledges rejection.
- **Step 20: `on_issue (on_issue_resolution_1)` [Unsolicited] (BPP -> BAP)**: Seller offers a revised partial refund.
- **Step 21: `/issue (issue_escalate)` (BAP -> BPP)**: The buyer escalates the unresolved grievance to a Level 2 Grievance Officer / Network Intermediary.
- **Step 22: `/on_issue (on_issue_processing_2)` (BPP -> BAP)**: Escalation acknowledged.
- **Step 23: `on_issue (on_issue_resolution_2)` [Unsolicited] (BPP -> BAP)**: Level 2 arbitrator reviews technician unboxing photos and rules in favor of full appliance return and refund.
- **Step 24: `/issue (issue_resolution_accept)` (BAP -> BPP)**: The buyer accepts the escalated ruling.
- **Step 25: `/on_issue (on_issue_resolved)` (BPP -> BAP)**: Issue marked resolved.
- **Step 26: `/issue (issue_close)` (BAP -> BPP)**: Dispute officially closed.
- **Step 27: `on_update (on_update_igm_return)` [Unsolicited] (BPP -> BAP)**: The seller initiates reverse freight logistics pickup and refund settlement.

---

### Flow 12: Order to Confirm with IGM 2.0.0: Evidence Exchange and Item Replacement

- **Flow ID:** `Order_to_confirm_to_fulfillment__Prepaid_with_IGM_v-2.0.0`
- **Config File:** `./APPLIANCES/Order_to_confirm_to_fulfillment__Prepaid_with_IGM_v-2.0.0.yaml`
- **Protocol Version:** `1.2.0`
- **Use Case:** `APPLIANCES`
- **Tags:** `WORKBENCH`, `MANDATORY`

#### 1. Short Description
Exercises an interactive IGM 2.0.0 evidence exchange workflow. The buyer reports a dead-on-arrival appliance, the seller requests additional technician inspection and serial number proof, the buyer supplies the evidence, and the seller approves and dispatches an appliance replacement with reverse freight pickup.

#### 2. API Breakdown & Technical Actions
- **Steps 1–14 (`/select` to `on_status_order_delivered` including `/track` and `/on_track`)**: Standard prepaid delivery lifecycle.
- **Step 15: `/issue (issue_open)` (BAP -> BPP)**: The buyer opens an issue reporting appliance failure (washing machine motor fails to engage).
- **Step 16: `/on_issue (on_issue_processing)` (BPP -> BAP)**: Initial seller acknowledgment.
- **Step 17: `on_issue (on_issue_need_more_info)` [Unsolicited] (BPP -> BAP)**: The seller requests additional diagnostic evidence: photographs of the rear serial number plate, technician inspection job sheet, and a short video of the motor error code.
- **Step 18: `/issue (issue_info_provided)` (BAP -> BPP)**: The buyer uploads and transmits the requested image and document URLs.
- **Step 19: `/on_issue (on_issue_provided)` (BPP -> BAP)**: The seller acknowledges receipt of the diagnostic evidence.
- **Step 20: `on_issue (on_issue_resolution)` [Unsolicited] (BPP -> BAP)**: The seller validates the motor defect and proposes an appliance `REPLACEMENT` resolution.
- **Step 21: `/issue (issue_resolution_accept)` (BAP -> BPP)**: The buyer accepts the replacement remedy.
- **Step 22: `/on_issue (on_issue_resolved)` (BPP -> BAP)**: The seller confirms resolution agreement.
- **Step 23: `/issue (issue_close)` (BAP -> BPP)**: The buyer closes the grievance.
- **Step 24: `on_update (on_update_igm_replacement)` [Unsolicited] (BPP -> BAP)**: The seller initiates an unsolicited order update scheduling a replacement freight delivery and simultaneous reverse pickup of the defective unit.

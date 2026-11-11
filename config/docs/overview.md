# Agriculture (ONDC:AGR10 1.2.0)

## Overview

The Agriculture domain (**ONDC:AGR10**, specification version **1.2.0**) establishes an open, standardized digital commerce framework for agricultural inputs, farm supplies, and packaged agri-commodities across the Open Network for Digital Commerce (ONDC). Adapting Beckn Core `0.9.3` for agri-commerce, **ONDC:AGR10** covers **Seeds and Planting Material**, **Fertilizers and Plant Nutrients** (granular, water-soluble, nano-liquid, and organic formulations), **Pesticides and Crop Protection** (insecticides, fungicides, herbicides, and bio-pesticides), **Plant Growth Regulators and Micronutrients**, **Farm Implements, Sprayers, and Irrigation Accessories**, **Animal Feed and Veterinary Supplements**, and **Pre-Packaged Agri-Commodities**.

India's agricultural supply chain has historically been fragmented across block-level agri-input dealers, mandi agents, primary agricultural credit societies (PACS), Farmer Producer Organizations (FPOs), and closed agritech marketplaces. Farmers and institutional buyers frequently face opaque pricing, seasonal stockouts during critical Kharif, Rabi, and Zaid sowing windows, and limited visibility into batch authenticity or delivery timelines, while rural input retailers struggle to reach buyers outside their immediate locality.

**ONDC:AGR10** unbundles agri-commerce by separating buyer-side discovery from seller inventory and logistics execution:
- **Farmer and FPO Empowerment**: Farmers, FPO procurement desks, and agri-entrepreneurs can search crop inputs across licensed regional dealers, state seed corporations, cooperative societies, and agri-brands using any compliant **Buyer Application (BAP)**.
- **Input Dealer and FPO Inclusion**: Licensed agri-input stores, FPO collection centers, fertilizer/agrochemical distributors, and D2C seed or implement manufacturers publish live stock, unitized pack sizes, prices, and serviceability areas through a **Seller Application (BPP)**.
- **Rural and Heavy-Cargo Logistics**: **Logistics Service Providers (LSPs)**—alongside seller-managed fleets, buyer-managed pickup (`Buyer-Delivery`), and depot `Self-Pickup`—handle moisture-sensitive treated seed sacks, 25 kg / 50 kg fertilizer bags, leak-proof agrochemical bottles, and bulky farm equipment across semi-urban and rural corridors.
- **Regulatory and Statutory Rigor**: Listings and order lifecycles align with Indian agricultural and packaged-goods laws, including the **Seeds Act, 1966** and **Seeds Rules, 1968**, the **Fertiliser (Inorganic, Organic or Mixed) Control Order (FCO), 1985**, the **Insecticides Act, 1968** (CIB&RC registration), the **Legal Metrology (Packaged Commodities) Rules, 2011** (`@ondc/org/statutory_reqs_packaged_commodities`), and **FSSAI** requirements (`@ondc/org/statutory_reqs_prepackaged_food`) where edible pre-packaged agri-commodities are sold.

The protocol standardizes all network interactions across:
- **Discovery**: `/search`, `/on_search`, and `/catalog_rejection` (city-wide and incremental push/pull catalog sync, variant groups, statutory declarations, and compliance rejection).
- **Ordering**: `/select`, `/on_select`, `/init`, `/on_init`, `/confirm`, and `/on_confirm`.
- **Fulfillment and Real-Time Tracking**: Unsolicited `/on_status` milestones (`Accepted`, `Packed`, `Agent-assigned`, `Order-picked-up`, `Out-for-delivery`, `Order-delivered`), `/track`, `/on_track`, and buyer-managed delivery `/update` callbacks.
- **Post-Order Lifecycle and Exceptions**: `/update`, `/on_update`, `/cancel`, and `/on_cancel` (pre-dispatch cancellations, merchant part-cancellations, Return to Origin / RTO, and quality-checked returns).
- **Grievance Redressal**: Issue and Grievance Management under both **IGM 1.0.0** and **IGM 2.0.0** architectures.

---

## Participants

The ONDC Agriculture ecosystem coordinates four core network roles:

```
+----------------------------------------------------------------------------------------------------+
|                                         ONDC GATEWAY / REGISTRY                                    |
|            (Participant Lookup, Cryptographic Ed25519 Authentication, Broadcast Routing)           |
+----------------------------------------------------------------------------------------------------+
              ^                                                                  ^
              | /search                                                          | /on_search
              v                                                                  v
+-----------------------------+                                    +-----------------------------+
|   BUYER APPLICATION (BAP)   |                                    |   SELLER APPLICATION (BPP)  |
| - Farmer & e-Krishi Apps    | ======= /select, /init, /confirm ====> | - Licensed Agri-Input Stores|
| - FPO Procurement Portals   | <====== /on_select, /on_init, /on_confirm == | - Seed & Fertilizer Depots  |
| - Agritech Advisory Apps    |                                    | - FPO & Cooperative Sellers |
| - Multi-Category Buyer Apps | <------ unsolicited on_status / on_update -- | - Agrochemical & Tool Brands|
+-----------------------------+                                    +-----------------------------+
              |                                                                  |
              | Track Live Telemetry (/track) or                                 | Assign Freight / Pickup
              | Coordinate Buyer-Delivery (/update)                              | or Self-Pickup Handover
              v                                                                  v
+----------------------------------------------------------------------------------------------------+
|                                    LOGISTICS SERVICE PROVIDER (LSP)                                |
|    (Bulk 25-50 kg Bag Haulage, Moisture-Safe Seed Transit, Spill-Proof Chemical Cargo, Last-Mile)  |
+----------------------------------------------------------------------------------------------------+
```

1. **Buyer Application (BAP)**:
   - Interfaces used by farmers, progressive growers, FPO procurement managers, and rural service kiosks to discover agri-inputs by crop, active nutrient/ingredient, pack weight, and price.
   - Transmits standardized transaction requests (`/search`, `/select`, `/init`, `/confirm`, `/cancel`, `/update`, `/track`, `/issue`, `/catalog_rejection`).
   - Collects prepaid payments (or configures supported payment terms), coordinates buyer-managed transport when `Buyer-Delivery` is used, and orchestrates escrow settlements and buyer refunds.

2. **Seller Application (BPP)**:
   - Operated by licensed block/district agri-input retailers, FPO input outlets, state cooperative federations, seed producers, agrochemical stockists, and farm-implement suppliers.
   - Publishes item catalogs with unitized weights/volumes (`kilogram`, `gram`, `tonne`, `litre`, `millilitre`, `unit`, `dozen`), variant groups, serviceability rules (`pincode`, `km`, or `geojson`), return/cancellation windows, and packaged-commodity statutory metadata.
   - Validates real-time stock, prepares sealed and leak-proof consignments, triggers unsolicited `/on_status` and `/on_update` events, and processes cancellations, RTOs, and quality-verified returns.

3. **Logistics Service Provider (LSP)**:
   - Hyperlocal rural couriers, regional block-level transporters, and heavy-parcel carriers integrated either with the BPP (seller-managed logistics) or with the BAP (buyer-managed delivery).
   - Handles bulk sack weights (e.g., 25 kg–50 kg fertilizer and feed bags), keeps treated seeds dry and protected from heat/moisture, segregates liquid crop-protection bottles with leak-resistant cushioning, collects OTP/electronic Proof of Delivery (ePOD), and performs reverse QC pickups on approved returns.

4. **Gateway and Registry**:
   - Maintains the verified directory of accredited participants and their `Ed25519` public signing keys.
   - Broadcasts `/search` discovery intents from BAPs to active agriculture BPPs matching the target domain (`ONDC:AGR10`) and city/region code.

---

## The User Journey

The standard prepaid forward-fulfillment lifecycle for an Agriculture order unfolds across eight operational and protocol phases:

```
+---------------------+      +---------------------+      +---------------------+      +---------------------+
| 1. Discovery &      | ---> | 2. Varietal, Grade  | ---> | 3. Order Init &     | ---> | 4. Order Confirm &  |
|    Catalog Search   |      |    & Serviceability   |      |    Delivery Config  |      |    Escrow Payment   |
+---------------------+      +---------------------+      +---------------------+      +---------------------+
           |                                                                                      |
           v                                                                                      v
+---------------------+      +---------------------+      +---------------------+      +---------------------+
| 5. Warehouse Picking| ---> | 6. Logistics &      | ---> | 7. Dispatch, Live   | ---> | 8. Settlement &     |
|    & Seal/Lot Check |      |    Cargo Assignment |      |    Tracking & Delivery|   |    Post-Fulfillment |
+---------------------+      +---------------------+      +---------------------+      +---------------------+
```

### 1. Discovery and Catalog Search
- A farmer or FPO buyer searches the BAP for required seasonal inputs or supplies (e.g., "Hybrid Paddy Seeds 5 kg", "Water-Soluble NPK 19:19:19 1 kg", "Neem Azadirachtin Bio-Pesticide 1 L", "Chelated Zinc Micronutrient", "16L Knapsack Sprayer").
- The BAP broadcasts a `/search` request specifying `domain = "ONDC:AGR10"`, `core_version = "1.2.0"`, city code (`std:...` or `*`), finder fee parameters, and fulfillment preferences (`Delivery`, `Self-Pickup`, or `Buyer-Delivery`).
- The ONDC Gateway routes the request to registered BPPs servicing the target geography.
- Each BPP responds asynchronously with `/on_search`, returning `bpp/providers[]` with store timings, geolocation/pincode serviceability tags, category taxonomies, `variant_group` hierarchies, unitized pack sizes (`kilogram`, `gram`, `tonne`, `litre`, `millilitre`, `unit`, `dozen`), prices, promotional offers, and statutory commodity declarations.

### 2. Varietal Selection, Grade, and Serviceability Check
- The buyer chooses the exact crop variety, formulation grade, and pack size (for example, 5 kg treated hybrid paddy seed pouch and two 1 kg pouches of water-soluble NPK) and enters the farm/village PIN code or GPS coordinates.
- The BAP sends `/select` with selected `provider.id`, `locations[].id`, `items[]` (IDs and quantities), and `fulfillments[0].end.location`.
- The BPP checks real-time warehouse stock for the requested lot/pack size, evaluates rural delivery polygon or pincode serviceability (`Fulfillment: Serviceable`), computes shipping charges and applicable GST, and returns `/on_select`.
- `/on_select` supplies an itemized commercial quote (`quote.breakup[]`), total payable value, quote validity (`quote.ttl`), and delivery turnaround time (`@ondc/org/TAT`). If any SKU is out of stock, an explicit domain error (`40002`) is returned immediately.

### 3. Order Initialization and Shipping Configuration
- At checkout, the buyer provides the recipient name (farmer or FPO authorized receiver), village/street address, landmark, mobile number, and billing details.
- The BAP fires `/init` containing billing information, finalized `fulfillments[]` destination coordinates, and selected fulfillment type (`Delivery`, `Self-Pickup`, or `Buyer-Delivery`).
- The BPP validates the delivery address, locks the itemized quotation and tax/freight breakdown, attaches statutory cancellation and return terms, and responds with `/on_init`.
- `/on_init` returns payment collection parameters (`collected_by`, settlement details, buyer finder fee terms, and `@ondc/org/settlement_window`).

### 4. Order Confirmation and Prepaid Escrow
- The buyer completes digital payment on the BAP (via UPI, Rupay/debit card, net banking, or agri-wallet) into the collecting participant's escrow flow.
- The BAP issues `/confirm` with `order.state = "Created"`, carrying the formal `order.id`, billing metadata, finalized quote, and verified payment parameters (`payment.params.transaction_id`, `payment.status = "PAID"`).
- The BPP validates payment status and quote integrity, books the consignment in its dealer ERP / Warehouse Management System (WMS), and responds with `/on_confirm` confirming `order.state = "Created"` and initializing fulfillment state to `Pending`.

### 5. Warehouse Picking, Seal Inspection, and Lot Verification
- The agri-input dealer or FPO warehouse team picks the ordered inputs from storage racks.
- Staff verify that seed pouches, fertilizer bags, and agrochemical containers have intact factory tamper seals, legible batch/lot codes, valid germination/test/expiry dates, and dry, undamaged packaging.
- Once the order is reviewed and confirmed for preparation, the BPP sends an unsolicited `on_status (on_status_accepted)`, moving `order.state` to `Accepted`.
- Heavy fertilizer bags are checked for double-stitching, seed packets are placed in moisture-resistant outer liners, and liquid pesticide or nutrient bottles are upright-packed with leak-proof cushioning.
- When ready for dispatch, the BPP emits an unsolicited `on_status (on_status_packed)`, advancing `fulfillment.state` to `Packed` and `order.state` to `In-progress`.

### 6. Logistics Assignment and Bulk or Spill-Safe Handling
- The seller assigns a carrier or delivery rider suited to the consignment weight and handling profile (standard van/two-wheeler courier for small seed/chemical cartons, light commercial vehicle for multi-bag fertilizer orders, or seller-side rider for regional block routes).
- The BPP emits an unsolicited `on_status (on_status_agent_assigned)`, updating `fulfillment.state` to `Agent-assigned` and sharing the courier agent's name and phone number so farmers in low-connectivity zones can coordinate handover.
- When the rider verifies the airway bill/label and takes custody of the consignment, the BPP fires an unsolicited `on_status (on_status_picked)`, transitioning `fulfillment.state` to `Order-picked-up` with the pickup timestamp.

### 7. Order Dispatch, Live Tracking, and Rural Delivery
- While the consignment is in transit, the BAP can poll `/track`, receiving `/on_track` with real-time GPS coordinates and a tracking URL.
- Upon reaching the buyer's block or village cluster, the BPP sends an unsolicited `on_status (on_status_out_for_delivery)`, advancing `fulfillment.state` to `Out-for-delivery`.
- At the farm gate, village residence, or FPO depot, the courier completes physical handover with delivery OTP / electronic Proof of Delivery (ePOD).
- The BPP emits an unsolicited `on_status (on_status_order_delivered)`, marking `fulfillment.state = "Order-delivered"` and `order.state = "Completed"`.

### 8. Settlement and Post-Fulfillment
- Successful delivery starts the item's configured return window (`@ondc/org/return_window`, where `@ondc/org/returnable = true`).
- Where settlement updates apply (such as post-delivery adjustments or buyer-confirmed closures), financial settlement records (`settlement_details`) capture payout allocations and withholding rules.
- After the settlement window elapses without a cancellation/return claim, net funds (order value minus agreed buyer finder fees and applicable statutory deductions such as TCS/TDS) settle to the agri-input merchant and logistics provider.

---

## Additional Scenarios

Agricultural commerce regularly contends with seasonal demand spikes, bulky cargo logistics, strict licensing rules, and rural last-mile challenges. **ONDC:AGR10 1.2.0** supports the following key exception and operational scenarios.

### 1. Buyer-Side Order Cancellation
- A farmer or FPO may cancel an order before courier pickup—for example, due to unexpected rainfall shifting sowing schedules, duplicate ordering, or extended delivery ETA (`001`–`005`, `051`–`053`, etc.).
- **Protocol Flow**:
  1. The BAP sends `/cancel` specifying `order_id` and `cancellation_reason_id` (such as `"051"` or `"001"`).
  2. The BPP verifies that the order is marked `@ondc/org/cancellable = true` and has not entered non-cancellable dispatch stages.
  3. The seller halts warehouse dispatch, releases reserved seed/fertilizer stock, and responds with `/on_cancel`, updating `order.state = "Cancelled"`, canceling active fulfillment, and returning refund/quote-trail details so the BAP can refund the buyer.

### 2. Merchant-Side Part-Cancellation and Return to Origin (RTO)
- **Part-Order Cancellation (`on_update_part_cancel`)**: During picking in a multi-item seasonal basket (e.g., 2 bags of urea, 1 sprayer nozzle kit, and 2 pouches of certified cotton seeds), the store discovers one SKU has moisture damage or failed lot inspection.
  - The BPP sends an unsolicited `on_update (on_update_part_cancel)` cancelling only the affected line item (`reason_id: "002"`), recalculating `quote.breakup[]` and total price via `quote_trail`, while keeping remaining items active.
  - The BAP acknowledges the adjustment and transmits `/update (update_settlement_trail)` to align differential refund settlement.
  - Available items continue through packing and dispatch.
- **Return to Origin (`on_cancel_rto`)**: In rural and peri-urban routes, field work during harvest/sowing or network dead zones can leave a buyer unreachable at delivery time.
  - After failed delivery attempts, the courier initiates Return to Origin and the BPP emits an unsolicited `on_cancel (on_cancel_rto)` with reason code `"013"`, transitioning the forward fulfillment to cancelled and creating an `RTO` fulfillment in `RTO-Initiated`.
  - The BAP submits `/update (update_settlement_trail)` reflecting settled two-way freight deductions where applicable.
  - When the consignment returns to the merchant depot, the BPP fires an unsolicited `on_status (on_status_rto_delivered)`, marking RTO fulfillment `RTO-Delivered` and closing refund settlement.

### 3. Buyer-Initiated Return and Reverse QC Pickup (Full and Partial Order)
- Because open or contaminated seeds, agrochemicals, and fertilizers cannot be resold for agronomic safety reasons, agriculture returns focus on sealed-pack errors, expired/near-expiry lots, punctured liquid containers, wrong crop varieties, or defective implements (`@ondc/org/returnable = true` and within `@ondc/org/return_window`).
- **Partial & Full Support**: A buyer may return either a single damaged container/defective sprayer or the entire multi-item order.
- **Protocol Flow**:
  1. The BAP triggers `/update (update_return)` (`update_target: "item"`) creating a `Return` fulfillment with `return_request` tags (`reason_id`, `reason_desc`, defect `images`, `ttl_approval`, `ttl_reverseqc`).
  2. The BPP validates eligibility and returns `/on_update (on_update_return_init)` in `Return_Initiated` state.
  3. After inspecting submitted photos/lot info, the seller approves the return via unsolicited `on_update (on_update_return_approved)`.
  4. A reverse courier visits the buyer to verify that factory seals remain unbroken (for sealed inputs) and labels match, then collects the return via unsolicited `on_update (on_update_return_picked)`.
  5. The BAP updates settlement records via `/update (update_settlement_trail)` for refund processing.
  6. Upon return receipt and final warehouse check, the BPP emits unsolicited `on_update (on_update_return_delivered)`, finalizing refund closure.

### 4. Out of Stock and Seasonal Inventory Exceptions
- Sowing-season surges (onset of monsoon for Kharif or post-harvest land preparation for Rabi) cause rapid depletion of high-demand hybrid seed varieties and subsidized/specialty nutrients.
- **Protocol Flow**:
  1. The BAP sends `/select (select0)` with the buyer's desired items and quantities.
  2. The BPP detects zero stock for one or more SKUs and responds with `/on_select (on_select_out_of_stock)` containing `error.type = "DOMAIN-ERROR"`, `error.code = "40002"`, and item quantity bounds set to `available.count = "0"` and `maximum.count = "0"` in the breakup.
  3. The BAP notifies the farmer/buyer, removes or substitutes the depleted SKU with an available agronomic alternative or pack size, and re-runs `/select` cleanly through delivery.

### 5. Buyer-Managed Delivery and Self-Pickup Fulfillment
- FPOs, dairy cooperatives, and agritech hubs frequently arrange their own transport vehicles or aggregate village orders from a central input depot (`Buyer-Delivery` or `Self-Pickup`).
- **Protocol Flow (`Buyer_Delivery`)**:
  1. Forward ordering (`/select` through `/on_confirm`) configures a buyer-managed fulfillment, followed by unsolicited `on_status (on_status_pending)` and `on_status (on_status_packed)` once the dealer weighs, labels, and stages the cargo at the warehouse gate.
  2. The BAP sends `/update (update_buyer_delivery_intermin)` (`update_target: "fulfillment"`) with `update_state = "Order-picked-up"`, `update_agent_details` (assigned driver/vehicle contact), and `update_label` (shipping label URL) as its carrier collects the consignment; the BPP confirms via `/on_update (on_update_buyer_delivery_intermin)`.
  3. Upon completion of delivery to the farmer or FPO collection center, the BAP transmits `/update (update_buyer_delivery_final)` with `update_state = "Order-delivered"`, and the BPP acknowledges closure via `/on_update (on_update_buyer_delivery_final)`.

### 6. Incremental Catalog Refresh (Push and Pull)
- Seasonal weather shifts, mandi rate fluctuations, and dealer restocking require frequent catalog synchronization without resending full catalogs.
- **Incremental Push (`Search_and_Custom_Menu_(Incremental_Push)`)**:
  - The BAP subscribes via `/search (search_inc)` carrying `intent.tags` with `code = "catalog_inc"` and `mode = "start"`.
  - The BPP pushes unsolicited `on_search` deltas (`on_search_inc`) for modified item prices, restocked seed lots, or pack updates, and broadcasts store availability transitions via `on_search (on_search_inc_close)` (`location.time.label = "close"`) and `on_search (on_search_inc_open)` (`location.time.label = "open"`).
  - The BAP halts the push stream when needed via `/search (search_inc1)` with `mode = "stop"`.
- **Incremental Refresh Pull (`Discovery_Flow_incremental_catalog_refresh_pull`)**:
  - After baseline sync, the BAP issues `/search (search_inc_pull)` passing `catalog_inc` tags with `start_time` and `end_time` timestamps (alongside `bap_terms` `effective_date`).
  - The BPP responds via `/on_search (on_search_inc_pull)` with only catalog items modified inside that window.

### 7. Statutory Compliance, Input Licensing, and Catalog Rejection
- Agriculture listings are subject to strict price ceiling and statutory labeling mandates:
  - **Seeds Act, 1966 & Seeds Rules, 1968**: Accurate disclosure of crop, cultivar/hybrid name, seed class, germination/purity assertions, net weight, and testing validity without misleading agronomic claims.
  - **Fertiliser Control Order (FCO), 1985**: Accurate nutrient composition (e.g., NPK ratios), formulation type, licensed distribution, and adherence to statutory MRP limits.
  - **Insecticides Act, 1968 (CIB&RC)**: Only approved crop-protection formulations with mandatory toxicity warnings, active ingredient concentration, and safe usage labels may be listed; banned or restricted formulations are prohibited.
  - **Legal Metrology (Packaged Commodities) Rules, 2011 & FSSAI**: Mandatory disclosure of `@ondc/org/statutory_reqs_packaged_commodities` (`manufacturer_or_packer_name`, `manufacturer_or_packer_address`, `common_or_generic_name_of_commodity`, `month_year_of_manufacture_packing_import`, consumer care details, and MRP) plus `@ondc/org/statutory_reqs_prepackaged_food` for applicable edible pre-packaged agri-commodities.
- **Catalog Rejection (`Catalog_Rejection_Flow`)**:
  - Following `/search` -> `/on_search`, if the BAP detects pricing violations (such as selling price exceeding `maximum_value` / MRP, reported with `type = "ITEM-ERROR"`, `code = "91001"`, `message = "Item price > MRP"`) or statutory catalog omissions (`ITEM-ERROR`, `PROVIDER-ERROR`, or `CATALOG-ERROR`), the BAP transmits `/catalog_rejection` specifying `errors[]` (`type`, `code`, `message`, `path`) to exclude non-compliant listings from buyer storefronts.

---

## Issue and Grievance Management

The Agriculture domain supports both **IGM 1.0.0** and **IGM 2.0.0** to resolve post-delivery grievances such as leaking liquid agrochemical bottles, torn fertilizer sacks, wrong seed varieties, or damaged farm implements.

### 1. IGM 1.0.0 Architecture
A linear four-step ticket workflow:
1. **`/issue (issue_open_100)` (BAP -> BPP)**: Buyer opens an issue citing an order/item defect (e.g., punctured bio-pesticide bottle or torn 25 kg seed bag) with supporting photos and complainant details.
2. **`/on_issue (on_issue_processing_100)` (BPP -> BAP)**: Merchant acknowledges the grievance, supplies respondent details and resolution TAT, and marks the issue `PROCESSING`.
3. **`on_issue_status (on_issue_resolved_100)` [Unsolicited] (BPP -> BAP)**: Merchant completes warehouse dispatch log checks and resolves the claim (e.g., `REFUND`), setting status to `RESOLVED`.
4. **`/issue (issue_close_100)` (BAP -> BPP)**: Buyer confirms satisfaction and closes the ticket.

### 2. IGM 2.0.0 Architecture
An interactive, multi-tier grievance framework supporting evidence exchange, customer acceptance/rejection, Ombudsman escalation, and automated reverse logistics or replacement dispatches:
1. **Explanatory Closure Without Physical Action (`Order_to_confirm_to_fulfillment__Prepaid_with_IGM_No_Action_v-2.0.0`)**:
   - A farmer questions unnatural pink/blue coating on treated hybrid maize seeds or minor moisture-free caking in water-soluble NPK fertilizer.
   - After acknowledging (`on_issue_processing`), the dealer's agronomist provides a technical clarification via unsolicited `on_issue (on_issue_resolution_igm_3)` (`NO_ACTION`) explaining approved fungicide seed-treatment dyeing or normal crystal agglomeration in high-grade soluble NPK.
   - The buyer accepts (`issue_resolution_accept_igm_3`), seller confirms `RESOLVED` (`on_issue_resolved_igm_3`), buyer closes the ticket (`issue_close_igm_3`), and seller confirms order state via `on_status (on_status_igm_3)`.
2. **Rejection, Level-2 Escalation, and Overturned Return (`Order_to_confirm_to_fulfillment__Prepaid_with_IGM_Rejection_v-2.0.0`)**:
   - Buyer reports a cracked 16L knapsack sprayer tank delivered at the farm.
   - Seller initially rejects the claim (`on_issue_resolution`), buyer rejects the response (`issue_resolution_reject`), and seller reiterates denial after internal re-check (`on_issue_resolution_1`).
   - Buyer escalates to Level 2 / Grievance Officer (`issue_escalate`). The Ombudsman reviews unboxing photos and transit custody logs, overturns the merchant rejection (`on_issue_resolution_2`), and mandates return & refund.
   - After buyer acceptance and ticket closure, the seller initiates reverse return/refund settlement via unsolicited `on_update (on_update_igm_return)`.
3. **Interactive Evidence Exchange and Item Replacement (`Order_to_confirm_to_fulfillment__Prepaid_with_IGM_v-2.0.0`)**:
   - Buyer reports receiving an incorrect paddy seed hybrid maturity grade or crushed packet.
   - Seller issues unsolicited `on_issue (on_issue_need_more_info)` requesting clear photographs of the batch/lot tag and damaged pouch.
   - Buyer uploads media evidence via `/issue (issue_info_provided)`, acknowledged by `/on_issue (on_issue_provided)`.
   - Seller validates the discrepancy and offers `REPLACEMENT` (`on_issue_resolution`). Upon buyer acceptance (`issue_resolution_accept`), resolution (`on_issue_resolved`), and closure (`issue_close`), the seller triggers replacement dispatch via unsolicited `on_update (on_update_igm_replacement)`.

---

## Detailed Protocol Flows

All **14 protocol flows** registered in [config/flows/index.yaml](file:///c:/Users/Ranvijay/ondc-work/automation-specifications/config/flows/index.yaml) for the Agriculture domain (`ONDC:AGR10 1.2.0`, flow definitions stored under `config/flows/Agriculture/`) are detailed below with their exact Flow IDs, classification tags, and verified step-by-step API sequences.

---

### Flow 1: Order to Confirm to Fulfillment (Prepaid Standard Delivery)

- **Flow ID:** `Order_to_confirm_to_fulfillment_(Prepaid)`
- **Protocol Version:** `1.2.0`
- **Use Case:** `AGRICULTURE`
- **Tags:** `WORKBENCH`, `PRAMAAN`, `MANDATORY`, `REPORTABLE`

#### 1. Short Description
The canonical end-to-end forward fulfillment journey for prepaid agricultural input and commodity orders. Covers item and pack-size selection, serviceability quote, checkout initialization, digital escrow payment capture, dealer warehouse picking and seal inspection, courier assignment, live GPS tracking, and final doorstep or farm-gate delivery.

#### 2. API Breakdown & Technical Actions
- **Step 1: `/select (select)` (BAP -> BPP)**: Buyer selects agri-input items (e.g., certified seeds, water-soluble fertilizers, sprayers), pack quantities, store location ID, and destination coordinates/PIN code.
- **Step 2: `/on_select (on_select)` (BPP -> BAP)**: Seller confirms stock availability, delivery serviceability (`Serviceable`), itemized quote breakup (`quote.breakup[]`), and estimated `@ondc/org/TAT`.
- **Step 3: `/init (init)` (BAP -> BPP)**: BAP sends recipient details, full delivery address, billing metadata, and chosen prepaid fulfillment type.
- **Step 4: `/on_init (on_init)` (BPP -> BAP)**: Seller locks the quotation, attaches cancellation/return terms, and supplies settlement and payment parameters.
- **Step 5: `/confirm (confirm)` (BAP -> BPP)**: BAP captures prepaid digital payment and submits the confirmed order (`order.state = "Created"`, `payment.status = "PAID"`).
- **Step 6: `/on_confirm (on_confirm)` (BPP -> BAP)**: Seller validates payment, registers the order in its OMS/WMS, confirms `order.state = "Created"`, and sets initial fulfillment state to `Pending`.
- **Step 7: `on_status (on_status_accepted)` [Unsolicited] (BPP -> BAP)**: Agri-input merchant reviews and accepts the order for processing; `order.state` transitions to `Accepted`.
- **Step 8: `on_status (on_status_packed)` [Unsolicited] (BPP -> BAP)**: Items are picked, checked for intact tamper seals and batch labels, and packed in moisture/leak-safe packaging; `fulfillment.state` updates to `Packed` and `order.state` to `In-progress`.
- **Step 9: `on_status (on_status_agent_assigned)` [Unsolicited] (BPP -> BAP)**: Carrier or delivery rider is assigned; `fulfillment.state` moves to `Agent-assigned` with agent contact details.
- **Step 10: `on_status (on_status_picked)` [Unsolicited] (BPP -> BAP)**: Delivery agent collects the consignment from the dealer warehouse/depot; `fulfillment.state` advances to `Order-picked-up`.
- **Step 11: `/track (track)` (BAP -> BPP)**: BAP queries live transit tracking telemetry.
- **Step 12: `/on_track (on_track)` (BPP -> BAP)**: BPP returns active tracking URL and/or GPS coordinates.
- **Step 13: `on_status (on_status_out_for_delivery)` [Unsolicited] (BPP -> BAP)**: Delivery agent reaches the destination block/village area; `fulfillment.state` transitions to `Out-for-delivery`.
- **Step 14: `on_status (on_status_order_delivered)` [Unsolicited] (BPP -> BAP)**: Consignment is handed over to the buyer/FPO receiver; `fulfillment.state` reaches `Order-delivered` and `order.state` transitions to `Completed`.

---

### Flow 2: Buyer Delivery and Buyer-Managed Logistics

- **Flow ID:** `Buyer_Delivery`
- **Protocol Version:** `1.2.0`
- **Use Case:** `AGRICULTURE`
- **Tags:** `WORKBENCH`, `PRAMAAN`, `MANDATORY`, `REPORTABLE`

#### 1. Short Description
Governs orders where the Buyer Application (or an FPO's own transport network) coordinates pickup and delivery logistics after the seller prepares and packs the agricultural inputs at the depot. The BAP notifies the seller of pickup (including shipping label details and driver info) and final delivery via `/update` calls.

#### 2. API Breakdown & Technical Actions
- **Steps 1–6 (`/select`, `/on_select`, `/init`, `/on_init`, `/confirm`, `/on_confirm`)**: Standard prepaid checkout sequence configuring a buyer-managed (`Buyer-Delivery`) fulfillment.
- **Step 7: `on_status (on_status_pending)` [Unsolicited] (BPP -> BAP)**: Seller places the confirmed order in pending warehouse processing queue.
- **Step 8: `on_status (on_status_packed)` [Unsolicited] (BPP -> BAP)**: Dealer packs the agri-inputs and marks the consignment ready for buyer-arranged pickup (`fulfillment.state = "Packed"`).
- **Step 9: `/update (update_buyer_delivery_intermin)` (BAP -> BPP)**: BAP targets `update_target = "fulfillment"`, sending `update_state = "Order-picked-up"`, driver/agent contact details (`update_agent_details`), and shipping label PDF reference (`update_label`).
- **Step 10: `/on_update (on_update_buyer_delivery_intermin)` (BPP -> BAP)**: Seller acknowledges pickup handoff and updates fulfillment state to `Order-picked-up`.
- **Step 11: `/update (update_buyer_delivery_final)` (BAP -> BPP)**: BAP sends `update_state = "Order-delivered"` upon reaching the buyer or FPO collection point.
- **Step 12: `/on_update (on_update_buyer_delivery_final)` (BPP -> BAP)**: Seller records final delivery confirmation (`Order-delivered` / `Completed`).

---

### Flow 3: Buyer-Side Order Cancellation

- **Flow ID:** `Buyer_Side_Order_Cancellation`
- **Protocol Version:** `1.2.0`
- **Use Case:** `AGRICULTURE`
- **Tags:** `WORKBENCH`, `PRAMAAN`, `MANDATORY`, `REPORTABLE`

#### 1. Short Description
Validates pre-dispatch order cancellation initiated by the buyer (for instance, due to delayed sowing weather or accidental order creation). Confirms immediate cancellation acceptance, inventory release, and refund initiation.

#### 2. API Breakdown & Technical Actions
- **Steps 1–6 (`/select`, `/on_select`, `/init`, `/on_init`, `/confirm`, `/on_confirm`)**: Standard prepaid order placement and confirmation.
- **Step 7: `/cancel (cancel)` (BAP -> BPP)**: BAP requests full order cancellation specifying `order_id` and a valid ONDC `cancellation_reason_id` (e.g., `"051"` or `"001"`).
- **Step 8: `/on_cancel (on_cancel)` (BPP -> BAP)**: Seller validates cancellability (`@ondc/org/cancellable = true`), halts dispatch, updates `order.state = "Cancelled"`, sets fulfillment state to `Cancelled`, and confirms refund quote details.

---

### Flow 4: Merchant-Side Part-Order Cancellation and Return to Origin (RTO)

- **Flow ID:** `Merchant_Side_RTO_and_Part_Order_Cancellation_Flow`
- **Protocol Version:** `1.2.0`
- **Use Case:** `AGRICULTURE`
- **Tags:** `WORKBENCH`, `PRAMAAN`, `MANDATORY`, `REPORTABLE`

#### 1. Short Description
Handles two post-confirmation merchant/logistics exceptions in one lifecycle: (1) seller-initiated partial cancellation during picking when a specific seed/fertilizer SKU cannot be fulfilled, followed by settlement adjustment, and (2) unsuccessful doorstep delivery leading to Return to Origin (RTO) and reverse freight settlement.

#### 2. API Breakdown & Technical Actions
- **Steps 1–6 (`/select`, `/on_select`, `/init`, `/on_init`, `/confirm`, `/on_confirm`)**: Prepaid multi-item order confirmed.
- **Step 7: `on_update (on_update_part_cancel)` [Unsolicited] (BPP -> BAP)**: Merchant cancels one unfulfillable item during warehouse picking (`reason_id: "002"`), adjusting item counts and `quote_trail` deductions.
- **Step 8: `/update (update_settlement_trail)` (BAP -> BPP)**: BAP sends settlement trail updates reflecting the differential partial refund.
- **Steps 9–12 (`on_status_packed`, `on_status_agent_assigned`, `on_status_picked`, `on_status_out_for_delivery`) [Unsolicited] (BPP -> BAP)**: Remaining active items are packed, assigned to a courier, picked up, and taken out for delivery.
- **Step 13: `on_cancel (on_cancel_rto)` [Unsolicited] (BPP -> BAP)**: Delivery fails (e.g., buyer unreachable / delivery refused); BPP triggers RTO with `reason_id: "013"`, cancelling forward fulfillment and creating an `RTO` fulfillment in `RTO-Initiated` state.
- **Step 14: `/update (update_settlement_trail)` (BAP -> BPP)**: BAP updates the settlement trail to reconcile RTO refund and applicable logistics deductions.
- **Step 15: `on_status (on_status_rto_delivered)` [Unsolicited] (BPP -> BAP)**: Undelivered consignment returns to the agri-input warehouse; RTO fulfillment closes as `RTO-Delivered`.

---

### Flow 5: Buyer-Initiated Return (Full Order and Partial Order)

- **Flow ID:** `Buyer_Initiated_Return_(Full_Order_and_Partial_Order)`
- **Protocol Version:** `1.2.0`
- **Use Case:** `AGRICULTURE`
- **Tags:** `WORKBENCH`, `PRAMAAN`, `MANDATORY`, `REPORTABLE`

#### 1. Short Description
Covers the end-to-end post-delivery return lifecycle (supporting both single-item partial returns and full-order returns) when delivered agri-inputs or farm tools are damaged, wrong variety, or defective. Validates reverse pickup approval, seal/condition inspection, settlement trail update, and warehouse return closure.

#### 2. API Breakdown & Technical Actions
- **Steps 1–6 (`/select` to `/on_confirm`)**: Standard prepaid order confirmation.
- **Steps 7–12 (`on_status_accepted`, `on_status_packed`, `on_status_agent_assigned`, `on_status_picked`, `on_status_out_for_delivery`, `on_status_order_delivered`) [Unsolicited] (BPP -> BAP)**: Forward delivery completed.
- **Step 13: `/update (update_return)` (BAP -> BPP)**: BAP initiates return (`update_target = "item"`) creating a `Return` fulfillment with `return_request` tags (`reason_id: "001"`, item quantities, defect `images`, `ttl_approval`, `ttl_reverseqc`).
- **Step 14: `/on_update (on_update_return_init)` (BPP -> BAP)**: Seller logs the return request in `Return_Initiated` state.
- **Step 15: `on_update (on_update_return_approved)` [Unsolicited] (BPP -> BAP)**: Merchant approves the return request (`Return_Approved`) after eligibility review and schedules reverse pickup.
- **Step 16: `on_update (on_update_return_picked)` [Unsolicited] (BPP -> BAP)**: Reverse logistics agent inspects seals/packaging condition at the buyer's premises and picks up the parcel (`Return_Picked`).
- **Step 17: `/update (update_settlement_trail)` (BAP -> BPP)**: BAP transmits settlement instructions for buyer refund reconciliation.
- **Step 18: `on_update (on_update_return_delivered)` [Unsolicited] (BPP -> BAP)**: Returned goods reach the seller warehouse (`Return_Delivered`), finalizing refund settlement.

---

### Flow 6: Out of Stock Error Handling (Inventory Shortage)

- **Flow ID:** `Out_of_Stock(Error_code)`
- **Protocol Version:** `1.2.0`
- **Use Case:** `AGRICULTURE`
- **Tags:** `WORKBENCH`, `PRAMAAN`, `MANDATORY`, `REPORTABLE`

#### 1. Short Description
Demonstrates graceful inventory-shortage handling during peak sowing demand. When a requested agricultural SKU becomes unavailable at `/select`, the BPP returns domain error `40002` with zeroed availability counts, enabling the buyer to revise cart selection and complete fulfillment cleanly.

#### 2. API Breakdown & Technical Actions
- **Step 1: `/select (select0)` (BAP -> BPP)**: Buyer submits an initial cart selection that includes a temporarily depleted agri-input SKU.
- **Step 2: `/on_select (on_select_out_of_stock)` (BPP -> BAP)**: Seller detects zero stock and responds with `error.type = "DOMAIN-ERROR"`, `error.code = "40002"`, and sets `quantity.available.count = "0"` and `quantity.maximum.count = "0"` for the unavailable SKU.
- **Step 3: `/select (select)` (BAP -> BPP)**: Buyer modifies the cart to in-stock items or adjusted quantities.
- **Step 4: `/on_select (on_select)` (BPP -> BAP)**: Seller confirms availability and returns the updated price quotation and TAT.
- **Steps 5–16 (`/init`, `/on_init`, `/confirm`, `/on_confirm`, `on_status_accepted`, `on_status_packed`, `on_status_agent_assigned`, `on_status_picked`, `/track`, `/on_track`, `on_status_out_for_delivery`, `on_status_order_delivered`)**: Standard checkout, live tracking, and completed delivery sequence for the updated cart.

---

### Flow 7: Search and Custom Menu: Full Catalog City Discovery

- **Flow ID:** `Search_and_Custom_Menu_(Full_Catalog_City)`
- **Protocol Version:** `1.2.0`
- **Use Case:** `AGRICULTURE`
- **Tags:** `WORKBENCH`, `PRAMAAN`, `MANDATORY`, `REPORTABLE`

#### 1. Short Description
Establishes baseline city- or region-wide discovery for `ONDC:AGR10`. A Buyer Application broadcasts a discovery search across a target city, and Agriculture BPPs publish complete store locations, crop-input categories, pack variants, unitized quantities, statutory declarations, offers, and serviceability boundaries.

#### 2. API Breakdown & Technical Actions
- **Step 1: `/search (search_1)` (BAP -> Gateway/BPP)**: BAP broadcasts a full-catalog search specifying `context.domain = "ONDC:AGR10"`, city code, finder fee terms, and `bap_terms` tags.
- **Step 2: `/on_search (on_search1)` (BPP -> BAP)**: Seller publishes its complete catalog including `bpp/descriptor`, `bpp/fulfillments` (`Delivery`, `Self-Pickup`, `Buyer-Delivery`), `bpp/providers[]`, depot locations, `timing` and `serviceability` rules (`pincode`/`km`/`geojson`), `variant_group` categories, compliant item metadata, and active `offers[]`.

---

### Flow 8: Search and Custom Menu: Incremental Catalog Push

- **Flow ID:** `Search_and_Custom_Menu_(Incremental_Push)`
- **Protocol Version:** `1.2.0`
- **Use Case:** `AGRICULTURE`
- **Tags:** `WORKBENCH`, `PRAMAAN`, `MANDATORY`, `REPORTABLE`

#### 1. Short Description
Validates real-time merchant-initiated incremental catalog pushes (`catalog_inc`). Sellers continuously push updated agri-input stock, price changes, and temporary store/depot closures or reopenings without resending full city catalogs.

#### 2. API Breakdown & Technical Actions
- **Step 1: `/search (search_inc)` (BAP -> Gateway/BPP)**: BAP initiates incremental push subscription using `intent.tags` with `code = "catalog_inc"` and `mode = "start"`.
- **Step 2: `on_search (on_search_inc)` [Unsolicited] (BPP -> BAP)**: BPP pushes unsolicited item-level price, stock, or catalog attribute deltas.
- **Step 3: `on_search (on_search_inc_close)` [Unsolicited] (BPP -> BAP)**: BPP broadcasts a temporary depot/store closure (`location.time.label = "close"` with closure `range.start`).
- **Step 4: `on_search (on_search_inc_open)` [Unsolicited] (BPP -> BAP)**: BPP broadcasts store reopening (`location.time.label = "open"`).
- **Step 5: `/search (search_inc1)` (BAP -> Gateway/BPP)**: BAP terminates incremental push updates with `catalog_inc` tag `mode = "stop"`.

---

### Flow 9: Discovery Flow: Incremental Catalog Refresh Pull

- **Flow ID:** `Discovery_Flow_incremental_catalog_refresh_pull`
- **Protocol Version:** `1.2.0`
- **Use Case:** `AGRICULTURE`
- **Tags:** `WORKBENCH`, `PRAMAAN`, `MANDATORY`, `REPORTABLE`

#### 1. Short Description
Validates BAP-initiated incremental catalog polling (`catalog_inc` with time bounds). Following initial discovery, the buyer app requests only catalog items created or modified between `start_time` and `end_time`, conserving bandwidth across seasonal price and stock updates.

#### 2. API Breakdown & Technical Actions
- **Step 1: `/search (search_1)` (BAP -> Gateway/BPP)**: Initial full-catalog search request.
- **Step 2: `/on_search (on_search1)` (BPP -> BAP)**: BPP returns baseline store and product catalog.
- **Step 3: `/search (search_inc_pull)` (BAP -> BPP)**: BAP sends a targeted refresh pull passing `intent.tags` with `code = "catalog_inc"` (`start_time` and `end_time`) and `bap_terms` (`effective_date`).
- **Step 4: `/on_search (on_search_inc_pull)` (BPP -> BAP)**: BPP responds with strictly those catalog entries updated within the requested time range.

---

### Flow 10: Catalog Rejection Flow: Price and Compliance Discrepancy

- **Flow ID:** `Catalog_Rejection_Flow`
- **Protocol Version:** `1.2.0`
- **Use Case:** `AGRICULTURE`
- **Tags:** `WORKBENCH`, `PRAMAAN`, `MANDATORY`, `REPORTABLE`

#### 1. Short Description
Enforces pricing integrity and statutory compliance in the Agriculture domain. When a seller catalog violates MRP ceilings (e.g., selling price exceeding MRP) or omits required packaged-commodity/input declarations, the BAP rejects the offending items or catalog via `/catalog_rejection`.

#### 2. API Breakdown & Technical Actions
- **Step 1: `/search (search_1)` (BAP -> Gateway/BPP)**: BAP initiates city catalog discovery (`ONDC:AGR10`).
- **Step 2: `/on_search (on_search1)` (BPP -> BAP)**: BPP publishes catalog items, including non-conforming SKUs (e.g., `price.value > price.maximum_value` or missing statutory metadata).
- **Step 3: `/catalog_rejection (catalog_rejection)` (BAP -> BPP)**: BAP sends `message.errors[]` identifying exact JSON paths and violation codes (such as `type = "ITEM-ERROR"`, `code = "91001"`, `message = "Item price > MRP"`, or `PROVIDER-ERROR` / `CATALOG-ERROR` codes), blocking non-compliant listings from consumer display.

---

### Flow 11: Order to Confirm with IGM 1.0.0 Resolution

- **Flow ID:** `Order_to_confirm_to_fulfillment__Prepaid_with_igm_1.0.0`
- **Protocol Version:** `1.2.0`
- **Use Case:** `AGRICULTURE`
- **Tags:** `WORKBENCH`, `MANDATORY`

#### 1. Short Description
Combines standard prepaid agri-input delivery with a linear IGM `1.0.0` post-delivery grievance workflow (such as reporting a punctured agrochemical bottle or damaged seed bag), leading to investigation, refund resolution, and ticket closure.

#### 2. API Breakdown & Technical Actions
- **Steps 1–14 (`/select` through `on_status_order_delivered`)**: Standard forward prepaid ordering, packing, courier pickup, live `/track` and `/on_track`, and completed doorstep delivery.
- **Step 15: `/issue (issue_open_100)` (BAP -> BPP)**: Buyer opens an IGM `1.0.0` grievance specifying category, item ID, description, and damage images.
- **Step 16: `/on_issue (on_issue_processing_100)` (BPP -> BAP)**: Seller acknowledges the grievance with ticket metadata, respondent details, and expected resolution TAT (`PROCESSING`).
- **Step 17: `on_issue_status (on_issue_resolved_100)` [Unsolicited] (BPP -> BAP)**: Merchant resolves the claim (e.g., authorizing `REFUND`) and marks status `RESOLVED`.
- **Step 18: `/issue (issue_close_100)` (BAP -> BPP)**: Buyer accepts the resolution and formally closes the grievance ticket.

---

### Flow 12: Order to Confirm with IGM 2.0.0: Resolution Accepted (No Action)

- **Flow ID:** `Order_to_confirm_to_fulfillment__Prepaid_with_IGM_No_Action_v-2.0.0`
- **Protocol Version:** `1.2.0`
- **Use Case:** `AGRICULTURE`
- **Tags:** `WORKBENCH`, `MANDATORY`

#### 1. Short Description
Exercises IGM `2.0.0` when a buyer raises a concern regarding an agricultural product characteristic (such as fungicide seed-treatment coloring or benign crystal clumping in water-soluble NPK) that requires technical clarification rather than a refund or replacement, concluding with a `NO_ACTION` resolution.

#### 2. API Breakdown & Technical Actions
- **Steps 1–14 (`/select` through `on_status_order_delivered`)**: Standard forward prepaid fulfillment, tracking, and delivery completion.
- **Step 15: `/issue (issue_open_2)` (BAP -> BPP)**: Buyer opens an IGM `2.0.0` grievance describing the observed product concern.
- **Step 16: `/on_issue (on_issue_processing)` (BPP -> BAP)**: Seller acknowledges receipt and transitions issue status to `PROCESSING`.
- **Step 17: `on_issue (on_issue_resolution_igm_3)` [Unsolicited] (BPP -> BAP)**: Seller proposes an explanatory resolution with `NO_ACTION` (clarifying standard seed-treatment dye or normal water-soluble fertilizer properties).
- **Step 18: `/issue (issue_resolution_accept_igm_3)` (BAP -> BPP)**: Buyer accepts the proposed resolution.
- **Step 19: `/on_issue (on_issue_resolved_igm_3)` (BPP -> BAP)**: Seller confirms issue state transition to `RESOLVED`.
- **Step 20: `/issue (issue_close_igm_3)` (BAP -> BPP)**: Buyer closes the grievance ticket.
- **Step 21: `on_status (on_status_igm_3)` [Unsolicited] (BPP -> BAP)**: Seller sends post-grievance `on_status` confirmation keeping order state `Completed`.

---

### Flow 13: Order to Confirm with IGM 2.0.0: Rejection, Escalation and Return

- **Flow ID:** `Order_to_confirm_to_fulfillment__Prepaid_with_IGM_Rejection_v-2.0.0`
- **Protocol Version:** `1.2.0`
- **Use Case:** `AGRICULTURE`
- **Tags:** `WORKBENCH`, `MANDATORY`

#### 1. Short Description
Demonstrates multi-stage IGM `2.0.0` dispute escalation when an initial seller rejection (for instance, over a cracked sprayer tank or torn bulk bag) is challenged by the buyer, reviewed again, escalated to Level-2 Grievance Redressal Officer / Ombudsman mediation, and resolved in the buyer's favor with an automated return and refund.

#### 2. API Breakdown & Technical Actions
- **Steps 1–14 (`/select` through `on_status_order_delivered`)**: Standard forward prepaid fulfillment, tracking, and delivery completion.
- **Step 15: `/issue (issue_open)` (BAP -> BPP)**: Buyer raises an IGM `2.0.0` damage complaint.
- **Step 16: `/on_issue (on_issue_processing)` (BPP -> BAP)**: Seller acknowledges complaint processing.
- **Step 17: `on_issue (on_issue_resolution)` [Unsolicited] (BPP -> BAP)**: Seller issues an initial resolution rejecting the claim.
- **Step 18: `/issue (issue_resolution_reject)` (BAP -> BPP)**: Buyer rejects the seller's initial decision.
- **Step 19: `/on_issue (on_issue_processing_1)` (BPP -> BAP)**: Seller reopens internal Level-1 review (`PROCESSING`).
- **Step 20: `on_issue (on_issue_resolution_1)` [Unsolicited] (BPP -> BAP)**: Seller publishes its revised Level-1 resolution response.
- **Step 21: `/issue (issue_escalate)` (BAP -> BPP)**: Unsatisfied buyer escalates the dispute to Level 2 (Grievance Redressal Officer / ODR).
- **Step 22: `/on_issue (on_issue_processing_2)` (BPP -> BAP)**: Escalated respondent acknowledges review of evidence and transit logs.
- **Step 23: `on_issue (on_issue_resolution_2)` [Unsolicited] (BPP -> BAP)**: Escalated resolution rules in the buyer's favor, authorizing return and refund.
- **Step 24: `/issue (issue_resolution_accept)` (BAP -> BPP)**: Buyer accepts the escalated binding resolution.
- **Step 25: `/on_issue (on_issue_resolved)` (BPP -> BAP)**: Ticket transitions to `RESOLVED`.
- **Step 26: `/issue (issue_close)` (BAP -> BPP)**: Buyer closes the ticket.
- **Step 27: `on_update (on_update_igm_return)` [Unsolicited] (BPP -> BAP)**: Seller initiates the return fulfillment and refund settlement mandated by the escalated ruling.

---

### Flow 14: Order to Confirm with IGM 2.0.0: Evidence Exchange and Item Replacement

- **Flow ID:** `Order_to_confirm_to_fulfillment__Prepaid_with_IGM_v-2.0.0`
- **Protocol Version:** `1.2.0`
- **Use Case:** `AGRICULTURE`
- **Tags:** `WORKBENCH`, `MANDATORY`

#### 1. Short Description
Validates collaborative evidence exchange under IGM `2.0.0`. The seller requests supplementary verification photos (e.g., seed lot tag or damaged pesticide seal), the buyer uploads media evidence, and the seller approves a `REPLACEMENT` resolution, dispatching a replacement agricultural consignment.

#### 2. API Breakdown & Technical Actions
- **Steps 1–14 (`/select` through `on_status_order_delivered`)**: Standard forward prepaid fulfillment, tracking, and delivery completion.
- **Step 15: `/issue (issue_open)` (BAP -> BPP)**: Buyer files an IGM `2.0.0` issue reporting a wrong varietal delivery or damaged input pouch.
- **Step 16: `/on_issue (on_issue_processing)` (BPP -> BAP)**: Seller acknowledges the grievance (`PROCESSING`).
- **Step 17: `on_issue (on_issue_need_more_info)` [Unsolicited] (BPP -> BAP)**: Seller asks for supporting evidence (e.g., batch/lot label photo or outer package image).
- **Step 18: `/issue (issue_info_provided)` (BAP -> BPP)**: Buyer submits the requested image/media URLs and remarks.
- **Step 19: `/on_issue (on_issue_provided)` (BPP -> BAP)**: Seller confirms receipt of the additional evidence.
- **Step 20: `on_issue (on_issue_resolution)` [Unsolicited] (BPP -> BAP)**: Seller validates the claim and proposes `REPLACEMENT`.
- **Step 21: `/issue (issue_resolution_accept)` (BAP -> BPP)**: Buyer accepts the replacement proposal.
- **Step 22: `/on_issue (on_issue_resolved)` (BPP -> BAP)**: Seller marks the issue `RESOLVED`.
- **Step 23: `/issue (issue_close)` (BAP -> BPP)**: Buyer closes the grievance ticket.
- **Step 24: `on_update (on_update_igm_replacement)` [Unsolicited] (BPP -> BAP)**: Seller initiates a replacement fulfillment order to dispatch the correct replacement agri-input item.

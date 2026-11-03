# Food & Beverage (ONDC:RET11 1.2.0)

- [Overview](#overview)
- [Participants](#participants)
- [The User Journey](#the-user-journey)
  - [1. Discovery and Menu Search](#1-discovery-and-menu-search)
  - [2. Dish Selection, Customization, and Serviceability Check](#2-dish-selection-customization-and-serviceability-check)
  - [3. Order Initialization and Delivery Configuration](#3-order-initialization-and-delivery-configuration)
  - [4. Order Confirmation and Payment](#4-order-confirmation-and-payment)
  - [5. Kitchen Order Acceptance, Cooking, and Packaging](#5-kitchen-order-acceptance-cooking-and-packaging)
  - [6. Logistics and Rider Assignment](#6-logistics-and-rider-assignment)
  - [7. Rider Arrival at Kitchen, Dispatch, Live Tracking, and Handover](#7-rider-arrival-at-kitchen-dispatch-live-tracking-and-handover)
  - [8. Settlement and Post-Fulfillment](#8-settlement-and-post-fulfillment)
- [Additional Scenarios](#additional-scenarios)
  - [1. Buyer-Side Order Cancellation](#1-buyer-side-order-cancellation)
  - [2. Merchant-Side Part-Cancellation and Return to Origin (RTO / Disposal)](#2-merchant-side-part-cancellation-and-return-to-origin-rto--disposal)
  - [3. Buyer-Initiated Return and Refund (Spoiled, Missing, or Incorrect Food)](#3-buyer-initiated-return-and-refund-spoiled-missing-or-incorrect-food)
  - [4. Out of Stock and Kitchen Ingredient Depletion](#4-out-of-stock-and-kitchen-ingredient-depletion)
  - [5. Buyer-Managed Delivery / Self-Pickup Fulfillment](#5-buyer-managed-delivery--self-pickup-fulfillment)
  - [6. Incremental Menu Refresh (Push and Pull)](#6-incremental-menu-refresh-push-and-pull)
  - [7. Statutory Compliance and Food Safety (FSSAI)](#7-statutory-compliance-and-food-safety-fssai)
- [Issue and Grievance Management](#issue-and-grievance-management)
  - [1. IGM 1.0.0 Architecture](#1-igm-100-architecture)
  - [2. IGM 2.0.0 Architecture](#2-igm-200-architecture)
- [Detailed Protocol Flows](#detailed-protocol-flows)
  - [Flow 1: Order to Confirm to Fulfillment (Prepaid Standard Delivery)](#flow-1-order-to-confirm-to-fulfillment-prepaid-standard-delivery)
  - [Flow 2: Buyer Delivery / Buyer-Managed Logistics](#flow-2-buyer-delivery--buyer-managed-logistics)
  - [Flow 3: Buyer-Side Order Cancellation](#flow-3-buyer-side-order-cancellation)
  - [Flow 4: Merchant-Side Part-Order Cancellation and Return to Origin (RTO)](#flow-4-merchant-side-part-order-cancellation-and-return-to-origin-rto)
  - [Flow 5: Buyer-Initiated Return (Full Order and Partial Order)](#flow-5-buyer-initiated-return-full-order-and-partial-order)
  - [Flow 6: Out of Stock Error Handling (Inventory Shortage)](#flow-6-out-of-stock-error-handling-inventory-shortage)
  - [Flow 7: Search and Custom Menu – Full Catalog City Discovery](#flow-7-search-and-custom-menu--full-catalog-city-discovery)
  - [Flow 8: Search and Custom Menu – Incremental Catalog Push](#flow-8-search-and-custom-menu--incremental-catalog-push)
  - [Flow 9: Search and Custom Menu – Incremental Catalog Refresh Pull](#flow-9-search-and-custom-menu--incremental-catalog-refresh-pull)
  - [Flow 10: Order to Confirm with IGM 1.0.0 Resolution](#flow-10-order-to-confirm-with-igm-100-resolution)
  - [Flow 11: Order to Confirm with IGM 2.0.0 – Resolution Accepted (No Action)](#flow-11-order-to-confirm-with-igm-200--resolution-accepted-no-action)
  - [Flow 12: Order to Confirm with IGM 2.0.0 – Rejection, Escalation & Return](#flow-12-order-to-confirm-with-igm-200--rejection-escalation--return)
  - [Flow 13: Order to Confirm with IGM 2.0.0 – Resolution & Item Replacement](#flow-13-order-to-confirm-with-igm-200--resolution--item-replacement)

---

## Overview

The Food & Beverage domain (**ONDC:RET11**, specification version **1.2.0**) enables digital commerce for restaurants, cloud kitchens, bakeries, cafes, quick-service restaurants (QSRs), and beverage outlets across the Open Network for Digital Commerce (ONDC). F&B retail transactions are characterized by hyper-local serviceability, ultra-fast on-demand fulfillment, live culinary customization (portion sizing, crust choices, add-on toppings, spice levels), strict perishable food safety regulations (FSSAI licensing, dietary declarations such as vegetarian, non-vegetarian, egg, allergen disclosures, nutritional values), kitchen prep schedules, and tightly coordinated delivery milestones.

ONDC unbundles the traditional centralized food delivery marketplace. Consumers use their preferred **Buyer Application (BAP)** to discover nearby restaurants, explore categorized menus, configure dish customizations, view transparent price breakdowns, place orders, and track rider telemetry in real time. Restaurants and culinary brands publish their menus through a **Seller Application (BPP)**, maintaining complete ownership over their pricing, kitchen prep lead times, operational timings, and packaging charges. Order delivery can be orchestrated via seller-integrated logistics (in-house delivery fleet or on-network Logistics Service Providers / LSPs) or via buyer-managed delivery (`Buyer_Delivery`).

The protocol formalizes all network interactions across:
- **Discovery**: `/search` and `/on_search` (full catalog queries, custom menu structures, incremental push/pull).
- **Ordering**: `/select`, `/on_select`, `/init`, `/on_init`, `/confirm`, and `/on_confirm`.
- **Fulfillment & Real-time Tracking**: unsolicited `/on_status` lifecycle events (`Accepted`, `In-progress`, `Packed`, `Agent-assigned`, `At-pickup`, `Order-picked-up`, `At-delivery`, `Order-delivered`), `/track`, and `/on_track`.
- **Post-Order Adjustments & Exceptions**: `/update`, `/on_update`, `/cancel`, and `/on_cancel` (kitchen ingredient stockouts, partial order cancellations, RTO/disposal, post-delivery spoiled food refunds).
- **Grievance Redressal**: Issue and Grievance Management across both **IGM 1.0.0** and **IGM 2.0.0** architectures.

---

## Participants

| Participant | What This Means |
|---|---|
| **Buyer Application (BAP)** | The consumer-facing application (e.g. food ordering apps, UPI apps, super-apps, telco applications) where diners discover nearby eateries, browse food menus, select dish variants and customizations, supply delivery locations, complete payment, track riders, and raise grievances. |
| **Seller Application (BPP)** | An application representing restaurants, cloud kitchens, QSRs, or food franchises. The BPP publishes live food menus, manages item customizations, checks kitchen serviceability radii, computes itemized quotes (dish prices, packaging fees, CGST/SGST, delivery), manages Kitchen Order Tickets (KOT), signals order prep status, and manages cancellations or refunds. |
| **Logistics Service Provider (LSP)** | A delivery network participant that executes hyperlocal point-to-point delivery. In Seller-managed logistics, the BPP or its integrated delivery partner assigns riders; in Buyer-managed delivery (`Buyer_Delivery`), the BAP coordinates logistics and pushes rider telemetry updates to the BPP. |
| **Gateway** | The ONDC routing infrastructure that multicasts broadcast discovery requests (`/search`) from BAPs to active seller applications (BPPs) based on domain code (`ONDC:RET11`), city code (e.g. `std:080`), and geolocation coordinates. |

---

## The User Journey

The standard F&B ordering journey enables a diner to discover nearby restaurants, customize food items, review transparent pricing and delivery estimates, submit delivery coordinates, pay digitally, and receive freshly prepared food with end-to-end milestone tracking.

### 1. Discovery and Menu Search

The diner initiates discovery on the BAP by searching for restaurants, cuisines (e.g., North Indian, Italian, Biryani), or specific dishes:

- **Intent Broadcast**: The BAP transmits a `/search` request specifying the domain category (`ONDC:RET11`), buyer delivery GPS coordinates and area pin code, and fulfillment type (`Delivery` or `Self-Pickup`).
- **Menu Response**: Active restaurant BPPs within serviceable delivery range respond via asynchronous `/on_search` payloads containing their store profile (`bpp/providers[]`). This includes restaurant operating hours, serviceability polygons/radii, FSSAI registration numbers, custom menu categories (e.g., Starters, Main Course, Beverages), dish descriptions, dietary tags (`veg_non_veg`), allergen information, nutritional information, item prices, packaging fees, and customization groups (`CG1`, `CG2`).

### 2. Dish Selection, Customization, and Serviceability Check

The buyer selects dishes and customizes toppings, portion sizes, or crusts:

- **Network interaction:**
  - **`/select` (BAP -> BPP)**: The BAP transmits selected base items (`order.items[]`), selected customization items tagged with `type="customization"` and linked to customization groups via `parent_item_id`, quantities, restaurant location ID, and destination delivery GPS coordinates.
  - **`/on_select` (BPP -> BAP)**: The restaurant validates real-time kitchen availability and delivery radius. It returns an itemized price quote (`quote.breakup[]`) breaking down base item prices, customization charges, packaging charges (`@ondc/org/title_type="packing"`), delivery charges (`@ondc/org/title_type="delivery"`), applicable taxes (CGST/SGST), and estimated turnaround time (`@ondc/org/TAT`, e.g. `PT45M`). If a dish or ingredient is unavailable, the BPP returns error code `40002` or `30009` (Out of Stock).

### 3. Order Initialization and Delivery Configuration

The diner provides complete delivery and billing information:

- **Network interaction:**
  - **`/init` (BAP -> BPP)**: The BAP transmits the buyer's full street address (flat/house number, building, street, landmark, area code), contact details (phone, email), billing address, and payment preferences.
  - **`/on_init` (BPP -> BAP)**: The restaurant freezes the order quote, specifies static/dynamic cancellation terms, establishes payment collection rules (e.g., BAP-collected prepaid digital payment or Cash on Delivery), and provides settlement fee parameters.

### 4. Order Confirmation and Payment

The diner completes payment:

- **Network interaction:**
  - **`/confirm` (BAP -> BPP)**: The BAP captures digital payment, generates the formal order ID (`order.id`), and transmits payment confirmation parameters (`payment.params.transaction_id`, `payment.status = "PAID"`).
  - **`/on_confirm` (BPP -> BAP)**: The restaurant validates payment, registers the order in its Point of Sale / Kitchen Display System (POS/KDS), sets `order.state = "Created"`, and establishes initial fulfillment state `Pending`.

### 5. Kitchen Order Acceptance, Cooking, and Packaging

The restaurant kitchen accepts the Kitchen Order Ticket (KOT), prepares the dishes, and packs the meal:

- **`on_status (Accepted)` [Unsolicited] (BPP -> BAP)**: The restaurant marks the order accepted (`order.state = "Accepted"`), committing to kitchen preparation.
- **`on_status (Packed)` [Unsolicited] (BPP -> BAP)**: Kitchen staff cook, assemble, inspect, and seal the food into thermal/leak-proof containers ready for courier dispatch (`order.state = "In-progress"`, `fulfillment.state = "Packed"`).

### 6. Logistics and Rider Assignment

A delivery executive is allocated to the pickup task:

- **`on_status (Agent-assigned)` [Unsolicited] (BPP -> BAP)**: The delivery partner assigns a rider to the order. The payload supplies the rider's identity credentials (`fulfillments[0].agent.name`, `agent.phone`) so the diner can contact the delivery agent.

### 7. Rider Arrival at Kitchen, Dispatch, Live Tracking, and Handover

The delivery executive travels to the restaurant, collects the order, and transports it to the diner:

- **`on_status (At-pickup)` [Unsolicited] (BPP -> BAP)**: The rider arrives at the restaurant pickup counter (`fulfillment.state = "At-pickup"`).
- **`on_status (Order-picked-up)` [Unsolicited] (BPP -> BAP)**: The rider verifies the order token, collects the sealed meal parcel, and departs from the restaurant (`fulfillment.state = "Order-picked-up"`), recording `fulfillments[0].start.time.timestamp`.
- **`/track` & `/on_track` (BAP $\leftrightarrow$ BPP)**: The BAP queries live GPS telemetry for real-time map rendering on the diner's screen.
- **`on_status (At-delivery)` [Unsolicited] (BPP -> BAP)**: The rider arrives at the diner's delivery premises (`fulfillment.state = "At-delivery"`).
- **`on_status (Order-delivered)` [Unsolicited] (BPP -> BAP)**: The meal is handed over to the diner (`fulfillment.state = "Order-delivered"`, `order.state = "Completed"`), recording the delivery timestamp and electronic proof of delivery (ePOD / delivery OTP).

### 8. Settlement and Post-Fulfillment

After successful delivery, financial reconciliation takes place. The BAP disburses funds to the restaurant BPP based on agreed settlement cycles (T+1 / T+2), withholding agreed buyer finder fees and routing statutory tax deductions (TCS/TDS) where applicable.

---

## Additional Scenarios

Food and Beverage retail involves dynamic operational situations that diverge from the happy path. The protocol handles the following scenarios and edge cases.

### 1. Buyer-Side Order Cancellation

A diner may cancel an order before the restaurant has commenced food preparation:

- **Network interaction:**
  - **`/cancel` (BAP -> BPP)**: The BAP transmits a cancellation request with a standard ONDC cancellation reason code (e.g., `001` for buyer change of mind, `003` for delayed kitchen TAT).
  - **`/on_cancel` (BPP -> BAP)**: The restaurant checks if the order is within its cancellable window (`@ondc/org/cancellable = true`). If accepted, `order.state` and `fulfillment.state` are updated to `Cancelled`, applicable cancellation fees are computed according to cancellation terms, and refund instructions are issued.

### 2. Merchant-Side Part-Cancellation and Return to Origin (RTO / Disposal)

Operational disruptions during kitchen prep or delivery:

- **Kitchen Part-Cancellation (`on_update`)**: If a specific ingredient runs out during cooking, the restaurant sends an unsolicited `/on_update` with an adjusted `quote.breakup` removing the unavailable item. The BAP responds with `/update` containing an updated settlement trail to refund the differential amount to the diner.
- **Return to Origin / Perishable Disposal (`on_cancel_rto` & `on_status_rto_disposed`)**: When a rider arrives at the destination but the customer is unreachable or refuses the order, the BPP issues an unsolicited `/on_cancel` with cancellation reason codes `011`–`015`. Because prepared food is perishable and cannot be returned to kitchen inventory, the fulfillment transitions to `on_status_rto_disposed` (`RTO-Disposed`) upon arrival at the origin.

### 3. Buyer-Initiated Return and Refund (Spoiled, Missing, or Incorrect Food)

Prepared food is generally non-returnable for resale; however, post-delivery refund/return claims apply to food quality defects, incorrect items, missing items, or spilled containers:

- **Return Claim (`/update`)**: The diner submits a claim detailing item ID, quantity, return reason code (e.g., `001` for damaged/spilled food, `002` for incorrect dish, `003` for spoiled food), and image evidence.
- **Acknowledgment & Approval (`on_update`)**: The restaurant acknowledges the claim (`Return_Initiated`) and approves the refund (`return_approved`).
- **Settlement Trail (`update_settlement_trail`)**: The BAP transmits the refund payment instructions to credit the customer's account.

### 4. Out of Stock and Kitchen Ingredient Depletion

When a diner selects a dish or customization whose ingredients were depleted right before checkout:

- **Error Response (`on_select`)**: The restaurant returns an error response with ONDC error code `40002` (Out of Stock) or `30009` and item availability details (`quantity.available.count = 0`).
- **Cart Modification**: The BAP displays the out-of-stock alert, allowing the diner to swap dishes or adjust customizations before retrying the `/select` call.

### 5. Buyer-Managed Delivery / Self-Pickup Fulfillment

When the buyer application manages logistics or the diner opts for self-pickup:

- **Buyer Logistics (`Buyer_Delivery`)**: The order is placed without seller logistics. Once the restaurant prepares and packs the meal (`on_status_packed`), the BAP coordinates pickup through its own delivery fleet, sending `/update` notifications (`update_buyer_delivery_intermin` upon pickup and `update_buyer_delivery_final` upon delivery), which the restaurant confirms via `/on_update`.

### 6. Incremental Menu Refresh (Push and Pull)

Restaurant menus, active dishes, and pricing change frequently throughout the day:

- **Incremental Push (`Search_and_Custom_Menu__Incremental_Push_`)**: The restaurant broadcasts live updates regarding sold-out dishes ("86'd" items), daily specials, price changes, or temporary kitchen pauses (`serviceability` toggle) via unsolicited `/on_search` payloads.
- **Incremental Pull (`Search_and_Custom_Menu__Incremental_Pull_`)**: The buyer application queries the restaurant for menu updates modified after a given timestamp (`last_updated_at`), maintaining cache consistency without loading full catalogs.

### 7. Statutory Compliance and Food Safety (FSSAI)

Food products are governed by Food Safety and Standards Authority of India (FSSAI) regulations:

- Every restaurant BPP must publish a valid 14-digit FSSAI license number in its provider tags.
- Food items must include dietary declarations (`veg_non_veg`: `veg`, `non_veg`, or `egg`), allergen advisories (nuts, dairy, gluten), nutritional values, and transparent ingredient lists.

---

## Issue and Grievance Management

The F&B domain supports grievance redressal across both ONDC Issue and Grievance Management (IGM) framework versions.

### 1. IGM 1.0.0 Architecture

In IGM 1.0.0, grievances follow a linear lifecycle:
1. **`issue (open)` (BAP -> BPP)**: The diner files a complaint regarding delivered food (e.g., "Food spilled or cold", "Missing item"), attaching photographs and complainant details.
2. **`on_issue (processing)` (BPP -> BAP)**: The restaurant acknowledges the complaint, providing a grievance ticket ID, respondent details, and expected Resolution Time (TAT).
3. **`on_issue_status (resolved)` (BPP -> BAP)**: The restaurant reviews the claim and issues a resolution (`REFUND`, `REPLACEMENT`, or `NO_ACTION`) with explanatory remarks.
4. **`issue (close)` (BAP -> BPP)**: The diner reviews the resolution and closes the grievance ticket.

### 2. IGM 2.0.0 Architecture

IGM 2.0.0 introduces multi-party interactions, evidence exchange, dispute escalation, and automated settlement linkages:
- **Clarification & Evidence Exchange**: The restaurant can request additional evidence (`on_issue_need_more_info`), and the diner responds with supplementary container/food photos (`issue_info_provided`).
- **Resolution Acceptance & Rejection**: The complainant can formally accept or reject proposed resolutions.
- **Multi-Level Escalation**: If dissatisfied, the diner can escalate the dispute to Level 2 (Grievance Redressal Officer / ODR Arbitrator).
- **Corrective Fulfillment Actions**: Upon resolution approval, the restaurant can automatically trigger a replacement dish delivery (`on_update_igm_replacement`) or refund workflow (`on_update_igm_return`).

---

## Detailed Protocol Flows

### Flow 1: Order to Confirm to Fulfillment (Prepaid Standard Delivery)

#### 1. Short Description
The primary forward-fulfillment F&B ordering journey. A diner selects dishes and customizations, receives an itemized quote with packaging charges, delivery fees, and taxes, inputs a delivery address, pays upfront, and receives the freshly prepared meal via seller-managed logistics with comprehensive rider milestone tracking (`At-pickup`, `Order-picked-up`, `At-delivery`, `Order-delivered`).

#### 2. API Breakdown & Technical Actions
- **`/select` (BAP -> BPP)**: The BAP transmits selected dish items, customization items (`tags` with `type="customization"` and `parent_item_id`), restaurant location ID, and destination delivery GPS coordinates.
- **`/on_select` (BPP -> BAP)**: The restaurant validates kitchen serviceability and returns an itemized price quote (`quote.breakup[]`) including base dish prices, customization costs, packaging charges (`@ondc/org/title_type="packing"`), delivery fees (`@ondc/org/title_type="delivery"`), CGST/SGST taxes, and estimated turnaround time (`@ondc/org/TAT = "PT45M"`).
- **`/init` (BAP -> BPP)**: The diner inputs shipping address (building, street, city, pin code) and contact details.
- **`/on_init` (BPP -> BAP)**: The restaurant freezes the quote, publishes cancellation terms, and returns payment settlement terms.
- **`/confirm` (BAP -> BPP)**: The BAP collects digital payment and sends the confirmed order payload (`payment.status = "PAID"`).
- **`/on_confirm` (BPP -> BAP)**: The restaurant confirms order placement, assigning `order.id` with state `Created` and fulfillment state `Pending`.
- **`on_status (on_status_pending)` [Unsolicited] (BPP -> BAP)**: Restaurant acknowledges and accepts the order (`order.state = "Accepted"`).
- **`on_status (on_status_packed)` [Unsolicited] (BPP -> BAP)**: Kitchen prepares and packs the food into sealed delivery parcels (`order.state = "In-progress"`, `fulfillment.state = "Packed"`).
- **`on_status (on_status_agent_assigned)` [Unsolicited] (BPP -> BAP)**: Delivery executive assigned; payload includes rider name and mobile number.
- **`on_status (on_status_at_pickup)` [Unsolicited] (BPP -> BAP)**: Rider arrives at the restaurant kitchen counter (`fulfillment.state = "At-pickup"`).
- **`on_status (on_status_order_picked)` [Unsolicited] (BPP -> BAP)**: Rider collects the food parcel (`fulfillment.state = "Order-picked-up"`), recording pickup timestamp.
- **`/track` & `/on_track` (BAP $\leftrightarrow$ BPP)**: BAP polls for live GPS telemetry of the delivery executive.
- **`on_status (on_status_at_delivery)` [Unsolicited] (BPP -> BAP)**: Rider arrives at the diner's delivery location (`fulfillment.state = "At-delivery"`).
- **`on_status (on_status_order_delivered)` [Unsolicited] (BPP -> BAP)**: Food safely delivered with delivery timestamp and electronic proof of delivery (`fulfillment.state = "Order-delivered"`, `order.state = "Completed"`).

---

### Flow 2: Buyer Delivery / Buyer-Managed Logistics

#### 1. Short Description
Used when the Buyer Application coordinates logistics or the diner opts for self-pickup. The restaurant prepares and packs the food, after which the buyer application dispatches its own delivery partner, updating the restaurant on pickup and delivery completion.

#### 2. API Breakdown & Technical Actions
- **`/select` -> `/on_select` (on_select_multiple_fulfillment) -> `/init` -> `/on_init` -> `/confirm` -> `/on_confirm`**: Standard ordering sequence establishing buyer-managed delivery fulfillment.
- **`on_status (on_status_pending)` [Unsolicited] (BPP -> BAP)**: Restaurant accepts the order.
- **`on_status (on_status_packed)` [Unsolicited] (BPP -> BAP)**: Restaurant cooks and packs the meal, signalling that the order is ready for pickup at the counter.
- **`/update (update_buyer_delivery_intermin)` (BAP -> BPP)**: The BAP updates fulfillment status to `Order-picked-up`, providing delivery agent details and dispatch timestamp.
- **`/on_update (on_update_buyer_delivery_intermin)` (BPP -> BAP)**: Restaurant acknowledges pickup and updates internal kitchen logs.
- **`/update (update_buyer_delivery_final)` (BAP -> BPP)**: The BAP notifies the restaurant that the courier has successfully delivered the food to the diner (`fulfillment.state = "Order-delivered"`).
- **`/on_update (on_update_buyer_delivery_final)` (BPP -> BAP)**: Restaurant records order completion and marks `order.state = "Completed"`.

---

### Flow 3: Buyer-Side Order Cancellation

#### 1. Short Description
Validates the cancellation of a confirmed F&B order by the buyer before food preparation or dispatch, ensuring the restaurant halts kitchen operations, marks the order cancelled, and initiates refund processing.

#### 2. API Breakdown & Technical Actions
- **`/select` through `/on_confirm`**: Diner places and confirms a prepaid food order.
- **`/cancel` (BAP -> BPP)**: Diner triggers cancellation from the application before kitchen dispatch, providing an ONDC cancellation reason code (`order.cancellation_reason_id = "001"`).
- **`/on_cancel` (BPP -> BAP)**: The restaurant checks order eligibility against cancellation terms (`@ondc/org/cancellable = true`). The restaurant cancels fulfillment, updates `order.state = "Cancelled"`, recalculates any applicable cancellation charges, and provides refund details.

---

### Flow 4: Merchant-Side Part-Order Cancellation and Return to Origin (RTO)

#### 1. Short Description
A multi-exception workflow handling kitchen ingredient stockouts during preparation, followed by an unsuccessful delivery attempt where the diner is unreachable, culminating in Return to Origin and perishable food disposal.

#### 2. API Breakdown & Technical Actions
- **`/confirm` -> `/on_confirm`**: Order established for multiple food items and customizations.
- **`on_update (on_update_part_cancel)` [Unsolicited] (BPP -> BAP)**: While preparing the meal, the kitchen discovers a dish or ingredient is exhausted. The restaurant cancels that specific item and updates the price quote.
- **`/update (update_settlement_part_cancel)` (BAP -> BPP)**: The BAP acknowledges the item cancellation and updates the settlement trail for the partial refund.
- **`on_status` sequence**: Remaining items are packed, rider assigned, arrived at pickup, picked up, arrived at delivery location.
- **`on_cancel (on_cancel_rto)` [Unsolicited] (BPP -> BAP)**: Rider attempts delivery but cannot reach the buyer. The restaurant initiates RTO with cancellation reason code `013` (Buyer unreachable).
- **`/update (update_settlement_part_cancel_1)` (BAP -> BPP)**: BAP transmits RTO settlement terms (accounting for return logistics deductions).
- **`on_status (on_status_rto_disposed)` [Unsolicited] (BPP -> BAP)**: Undelivered perishable food returned to restaurant premises is marked disposed/liquidated; order marked `Cancelled`.

---

### Flow 5: Buyer-Initiated Return (Full Order and Partial Order)

#### 1. Short Description
Covers the post-delivery claim and refund lifecycle. When delivered food arrives spilled, cold, spoiled, or incorrect, the diner submits a return/refund claim, which the restaurant validates and approves, followed by financial settlement.

#### 2. API Breakdown & Technical Actions
- **Forward Delivery Completion**: Order delivered with full `on_status` milestone sequence (`at_pickup`, `order_picked`, `track`, `at_delivery`, `order_delivered`).
- **`/update (update_return)` (BAP -> BPP)**: Diner submits a return/refund claim for specific delivered dishes, supplying reason codes (e.g., `001` - Damaged/spilled food, `002` - Wrong dish delivered), quantities, and photo proof.
- **`/on_update (on_update_return_init)` (BPP -> BAP)**: Restaurant acknowledges the claim in state `Return_Initiated`.
- **`on_update (on_update_return_approved)` [Unsolicited] (BPP -> BAP)**: Restaurant approves the return/refund request.
- **`/update (update_settlement_trail)` (BAP -> BPP)**: BAP transmits payment settlement instructions to refund the diner.

---

### Flow 6: Out of Stock Error Handling (Inventory Shortage)

#### 1. Short Description
Demonstrates exception handling when a diner attempts to order dishes that have run out of stock in the kitchen. The restaurant rejects the initial selection with error code `40002`/`30009`, allowing the diner to adjust dish choices or quantities and proceed.

#### 2. API Breakdown & Technical Actions
- **`/select (select0)` (BAP -> BPP)**: Diner selects dishes and customizations.
- **`/on_select (on_select_out_of_stock)` (BPP -> BAP)**: Restaurant identifies that the dish or required ingredients are exhausted. It returns an error response with code `40002` (Out of stock) or `30009` and item availability details (`quantity.available.count = 0`).
- **`/select` (BAP -> BPP)**: Diner adjusts the cart to select available menu items.
- **`/on_select` (BPP -> BAP)**: Restaurant confirms inventory availability and generates the itemized quote.
- **`/init` through `/on_status (order_delivered)`**: Normal order placement and fulfillment sequence proceeds to completion.

---

### Flow 7: Search and Custom Menu – Full Catalog City Discovery

#### 1. Short Description
The foundational discovery flow for F&B. A diner searches for restaurants or dishes across a city or broad geolocation, and the restaurant returns its full menu catalog, hierarchical categories, dish customizations, and serviceability rules.

#### 2. API Breakdown & Technical Actions
- **`/search (search)` (BAP -> Gateway)**: BAP broadcasts a city-wide discovery query (`context.city = "std:080"`, `intent.category.id = "ONDC:RET11"`).
- **`/on_search (on_search)` (BPP -> BAP)**: Restaurant responds with its complete menu catalog:
  - `bpp/providers[]`: Restaurant name, operating hours, geolocation, FSSAI license, and serviceability radiuses.
  - `categories[]`: Menu categories (e.g., Starters, Main Course, Biryanis, Beverages, Desserts).
  - `items[]`: Dishes, descriptions, prices, images, veg/non-veg tags (`veg_non_veg`), allergen information, nutritional information, and preparation TAT.
  - Customization Groups (`CG1`, `CG2`): Portions, crust sizes, topping options, and spice levels linked via `parent_item_id`.
  - `offers[]`: Promotional discounts and combo offers.

---

### Flow 8: Search and Custom Menu – Incremental Catalog Push

#### 1. Short Description
Validates merchant-initiated real-time menu updates. Restaurants push live changes regarding dish availability ("86'd" items sold out during rush hour), flash discounts, or temporary kitchen closure without requiring a full catalog reload.

#### 2. API Breakdown & Technical Actions
- **`/search (search1)` (BAP -> Gateway)**: Preliminary search establishing active listening.
- **`/on_search (on_search1)` (BPP -> BAP)**: Baseline menu catalog response.
- **`on_search (on_search3)` [Unsolicited] (BPP -> BAP)**: Restaurant pushes item-level changes (dish marked unavailable, price change).
- **`on_search (on_search_2)` [Unsolicited] (BPP -> BAP)**: Restaurant signals temporary kitchen closure (`serviceability` disabled during peak hours).
- **`/search (search_1)` (BAP -> Gateway)**: Verification query confirming catalog synchronization.

---

### Flow 9: Search and Custom Menu – Incremental Catalog Refresh Pull

#### 1. Short Description
Validates the buyer application pull mechanism for menu synchronization. The buyer requests menu modifications that occurred after a specific timestamp, minimizing network bandwidth while keeping local menus fresh.

#### 2. API Breakdown & Technical Actions
- **`/search (search_1)` -> `/on_search (on_search1)`**: Baseline full menu discovery.
- **`/search (search_inc_pull)` (BAP -> BPP)**: Targeted point-to-point search passing tags with `mode = "incremental_refresh"` and `last_updated_at` timestamp.
- **`/on_search (on_search_inc_pull)` (BPP -> BAP)**: Restaurant responds with strictly those dishes whose pricing, availability, or customization details changed since the requested cutoff.

---

### Flow 10: Order to Confirm with IGM 1.0.0 Resolution

#### 1. Short Description
A complete F&B purchase and fulfillment flow integrated with the IGM 1.0.0 complaint resolution cycle. After receiving food, the diner reports a quality defect, which the restaurant investigates, resolves, and closes.

#### 2. API Breakdown & Technical Actions
- **Delivery Steps (1–15)**: Order placed, paid, packed, dispatched, tracked, and delivered.
- **`/issue (issue_open_100)` (BAP -> BPP)**: Diner files a complaint citing food quality defects (e.g., cold food, missing item, spilled soup), attaching photos and contact info.
- **`/on_issue (on_issue_processing_100)` (BPP -> BAP)**: Restaurant acknowledges the complaint, generates a ticket number, and assigns an expected resolution deadline.
- **`on_issue_status (on_issue_resolved_100)` [Unsolicited] (BPP -> BAP)**: Restaurant investigates and posts a resolution (`RESOLVED`), authorizing a refund or credit adjustment.
- **`/issue (issue_close_100)` (BAP -> BPP)**: Diner confirms satisfactory resolution and closes the issue.

---

### Flow 11: Order to Confirm with IGM 2.0.0 – Resolution Accepted (No Action)

#### 1. Short Description
Validates the IGM 2.0.0 framework where a grievance is processed, a formal resolution explanation is tendered by the restaurant without secondary fulfillment actions, and the diner accepts the resolution.

#### 2. API Breakdown & Technical Actions
- **Delivery Steps (1–15)**: Order placed, fulfilled, and delivered.
- **`/issue (issue_open_2)` (BAP -> BPP)**: Diner registers an issue under IGM 2.0.0 schema with sub-category codes and complainant details.
- **`/on_issue (on_issue_processing)` (BPP -> BAP)**: Restaurant acknowledges receipt and assigns a grievance handler.
- **`on_issue (on_issue_resolution_igm_3)` [Unsolicited] (BPP -> BAP)**: Restaurant provides formal resolution proposal (`action_triggered = "NO_ACTION"` with explanatory justification).
- **`/issue (issue_resolution_accept_igm_3)` (BAP -> BPP)**: Complainant reviews and formally accepts the resolution.
- **`/on_issue (on_issue_resolved_igm_3)` (BPP -> BAP)**: Restaurant marks issue state as `RESOLVED`.
- **`/issue (issue_close_igm_3)` (BAP -> BPP)**: Diner closes the ticket.
- **`on_status (on_status_igm_3)` [Unsolicited] (BPP -> BAP)**: Restaurant finalizes post-resolution order audit status.

---

### Flow 12: Order to Confirm with IGM 2.0.0 – Rejection, Escalation & Return

#### 1. Short Description
A multi-tier grievance escalation flow under IGM 2.0.0. The diner rejects the initial resolution, escalates the dispute to higher grievance redressal authorities, reaches a mutually accepted resolution, and receives an authorized refund/return.

#### 2. API Breakdown & Technical Actions
- **Delivery Steps (1–15)**: Order delivered successfully.
- **`/issue (issue_open)` -> `/on_issue (processing)`**: Initial grievance filed.
- **`on_issue (on_issue_resolution)` [Unsolicited] (BPP -> BAP)**: Restaurant proposes an initial settlement.
- **`/issue (issue_resolution_reject)` (BAP -> BPP)**: Diner rejects the proposed resolution.
- **`/on_issue (on_issue_processing_1)` -> `on_issue (on_issue_resolution_1)`**: Restaurant reconsiders with a revised proposal.
- **`/issue (issue_escalate)` (BAP -> BPP)**: Diner escalates grievance to Level 2 (Grievance Redressal Officer / Arbitrator).
- **`/on_issue (on_issue_processing_2)` -> `on_issue (on_issue_resolution_2)`**: Escalated resolution published.
- **`/issue (issue_resolution_accept)` (BAP -> BPP)**: Complainant accepts the escalated resolution terms.
- **`/on_issue (on_issue_resolved)` -> `/issue (issue_close)`**: Ticket closed as successfully resolved.
- **`on_update (on_update_igm_return)` [Unsolicited] (BPP -> BAP)**: Restaurant initiates an official return and refund workflow for the contested items.

---

### Flow 13: Order to Confirm with IGM 2.0.0 – Resolution & Item Replacement

#### 1. Short Description
Validates the interactive evidence-gathering cycle in IGM 2.0.0. The restaurant requests additional food container photographs, the diner supplies the evidence, and the restaurant approves an item replacement, automatically dispatching a replacement meal parcel.

#### 2. API Breakdown & Technical Actions
- **Delivery Steps (1–15)**: Order delivered.
- **`/issue (issue_open)` -> `/on_issue (processing)`**: Diner files an issue claiming an incorrect or damaged dish was delivered.
- **`on_issue (on_issue_need_more_info)` [Unsolicited] (BPP -> BAP)**: Restaurant requests verification proof (e.g., photo of the delivered meal package and receipt).
- **`/issue (issue_info_provided)` (BAP -> BPP)**: Diner uploads the requested photo evidence and explanation.
- **`/on_issue (on_issue_provided)` (BPP -> BAP)**: Restaurant confirms receipt of additional evidence.
- **`on_issue (on_issue_resolution)` [Unsolicited] (BPP -> BAP)**: Restaurant validates proof and proposes item replacement (`action_triggered = "REPLACEMENT"`).
- **`/issue (issue_resolution_accept)` (BAP -> BPP)**: Diner accepts the replacement offer.
- **`/on_issue (on_issue_resolved)` -> `/issue (issue_close)`**: Grievance closed as resolved.
- **`on_update (on_update_igm_replacement)` [Unsolicited] (BPP -> BAP)**: Restaurant kitchen automatically generates and triggers a new replacement fulfillment parcel containing the replacement dish.

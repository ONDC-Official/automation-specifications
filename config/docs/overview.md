# Food & Beverage (ONDC:RET11 1.2.5)

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
- [Additional Scenarios & 1.2.5 Enhancements](#additional-scenarios--125-enhancements)
  - [1. Mid-Order Address & Buyer Instructions Update](#1-mid-order-address--buyer-instructions-update)
  - [2. Buyer-Side Order Cancellation](#2-buyer-side-order-cancellation)
  - [3. Seller/System Force Cancellation](#3-sellersystem-force-cancellation)
  - [4. Buyer-Managed Delivery (Buyer Logistics)](#4-buyer-managed-delivery-buyer-logistics)
  - [5. Self-Pickup (Takeaway Fulfillment)](#5-self-pickup-takeaway-fulfillment)
  - [6. Slotted and Scheduled Delivery](#6-slotted-and-scheduled-delivery)
  - [7. Multi-Option Fulfillment (Dine-in / Takeaway / Delivery)](#7-multi-option-fulfillment-dine-in--takeaway--delivery)
  - [8. BNP / SNP Negotiated Commercial Model](#8-bnp--snp-negotiated-commercial-model)
  - [9. Promotional Offers and Discounts Flow](#9-promotional-offers-and-discounts-flow)
  - [10. Merchant-Side Part-Cancellation and Return to Origin (RTO & Disposal)](#10-merchant-side-part-cancellation-and-return-to-origin-rto--disposal)
  - [11. Post-Delivery Return, Liquidation, and Refund](#11-post-delivery-return-liquidation-and-refund)
  - [12. Out of Stock Handling (Cart Recovery vs. Immediate Error Rejection)](#12-out-of-stock-handling-cart-recovery-vs-immediate-error-rejection)
  - [13. Incremental Menu Refresh (Push and Pull)](#13-incremental-menu-refresh-push-and-pull)
  - [14. Statutory Compliance and Food Safety (FSSAI)](#14-statutory-compliance-and-food-safety-fssai)
- [Issue and Grievance Management](#issue-and-grievance-management)
  - [1. IGM 1.0.0 Architecture](#1-igm-100-architecture)
  - [2. IGM 2.0.0 Architecture](#2-igm-200-architecture)
- [Detailed Protocol Flows](#detailed-protocol-flows)
  - [Flow 1: ORDER_FLOW (Prepaid Standard Delivery)](#flow-1-order_flow-prepaid-standard-delivery)
  - [Flow 2: BUYER INSTRUCTIONS AND ADDRESS UPDATE FLOW](#flow-2-buyer-instructions-and-address-update-flow)
  - [Flow 3: BUYER_CANCEL (Buyer-Initiated Order Cancellation)](#flow-3-buyer_cancel-buyer-initiated-order-cancellation)
  - [Flow 4: FORCE_CANCEL (Force Cancellation Post-Confirmation)](#flow-4-force_cancel-force-cancellation-post-confirmation)
  - [Flow 5: BUYER_DELIVERY (Buyer-Managed Logistics)](#flow-5-buyer_delivery-buyer-managed-logistics)
  - [Flow 6: SELF_PICKUP (Takeaway / Self-Collection)](#flow-6-self_pickup-takeaway--self-collection)
  - [Flow 7: SLOTTED_DELIVERY (Scheduled Delivery Windows)](#flow-7-slotted_delivery-scheduled-delivery-windows)
  - [Flow 8: MULTI_OPTION_FULFILLMENT_FLOW (Multi-Fulfillment Modes)](#flow-8-multi_option_fulfillment_flow-multi-fulfillment-modes)
  - [Flow 9: COMMERCIAL_MODEL_FOR_BNP/SNP_FLOW (Negotiated Commercials)](#flow-9-commercial_model_for_bnpsnp_flow-negotiated-commercials)
  - [Flow 10: OFFERS_FLOW (Offer Discovery and Pricing Adjustment)](#flow-10-offers_flow-offer-discovery-and-pricing-adjustment)
  - [Flow 11: OUT_OF_STOCK (Inventory Depletion with Cart Recovery)](#flow-11-out_of_stock-inventory-depletion-with-cart-recovery)
  - [Flow 12: OUT_OF_STOCK(ERROR-CODE) (Immediate Error Rejection)](#flow-12-out_of_stockerror-code-immediate-error-rejection)
  - [Flow 13: RETURN_FLOW (Post-Delivery Return & Liquidation)](#flow-13-return_flow-post-delivery-return--liquidation)
  - [Flow 14: RTO_PLUS_PART_CANCELLATION (Kitchen Stockout & Failed Last-Mile RTO)](#flow-14-rto_plus_part_cancellation-kitchen-stockout--failed-last-mile-rto)
  - [Flow 15: FULL_CATALOG (Full Menu Discovery)](#flow-15-full_catalog-full-menu-discovery)
  - [Flow 16: INCREMENTAL_CATALOG (Incremental Menu Push)](#flow-16-incremental_catalog-incremental-menu-push)
  - [Flow 17: INCREMENTAL_CATALOG_PULL (Incremental Menu Pull)](#flow-17-incremental_catalog_pull-incremental-menu-pull)
  - [Flow 18: DELIVERY_FLOW_WITH_IGM(v-1.0.0) (Grievance Resolution v1.0.0)](#flow-18-delivery_flow_with_igmv-100-grievance-resolution-v100)
  - [Flow 19: DELIVERY_FLOW_WITH_IGM(v-2.0.0) (Evidence Exchange & Corrective Return)](#flow-19-delivery_flow_with_igmv-200-evidence-exchange--corrective-return)
  - [Flow 20: DELIVERY_FLOW_WITH_IGM_No_Action(v-2.0.0) (No-Action Resolution)](#flow-20-delivery_flow_with_igm_no_actionv-200-no-action-resolution)
  - [Flow 21: DELIVERY_FLOW_WITH_IGM_Rejection(v-2.0.0) (Rejection & Escalation)](#flow-21-delivery_flow_with_igm_rejectionv-200-rejection--escalation)

---

## Overview

The Food & Beverage domain (**ONDC:RET11**, specification version **1.2.5**) establishes an open, interoperable digital commerce framework for restaurants, cloud kitchens, bakeries, cafes, food carts, and Quick Service Restaurants (QSRs) across the Open Network for Digital Commerce (ONDC). F&B retail is characterized by hyperlocal discovery, fast turnaround fulfillment, kitchen preparation workflows (Kitchen Order Tickets / KOT), complex dish customizations (portion sizes, crust variants, toppings, spice grades), strict food safety and statutory requirements (FSSAI licensing, vegetarian/non-vegetarian/egg indicators, allergen advisories, nutritional information), and perishable product handling.

Building upon earlier iterations, **version 1.2.5** expands the protocol with crucial capabilities designed to address real-world operational challenges:
- **BNP / SNP Commercial Model**: Formal on-network negotiation of commercial terms, convenience fees, and commission structures between the Buyer Network Participant (BNP) and Seller Network Participant (SNP).
- **Flexible Fulfillment Variations**: Dedicated standardized flows for **Slotted/Scheduled Delivery**, in-store **Self-Pickup (Takeaway)**, and simultaneous **Multi-Option Fulfillment** (Dine-in, Takeaway, Home Delivery).
- **In-Flight Order Adjustments**: Mid-order updates allowing consumers to modify drop-off addresses or communicate special buyer delivery instructions after order confirmation before dispatch.
- **Enhanced Exception Lifecycles**: Dedicated **Force Cancellation** by sellers/systems, dual out-of-stock mechanisms (graceful cart reconfiguration vs. immediate error rejection), and explicit post-delivery **Return Liquidation Disposition**.
- **Complete Grievance Framework**: Full coverage across **IGM 1.0.0** and all four branches of **IGM 2.0.0** (Evidence Exchange with Replacement/Return, No Action, and Dispute Escalation).

The protocol standardizes all network interactions across:
- **Discovery**: `/search` and `/on_search` (full catalog queries, custom menu structures, incremental push/pull).
- **Ordering**: `/select`, `/on_select`, `/init`, `/on_init`, `/confirm`, and `/on_confirm`.
- **Fulfillment & Real-time Tracking**: unsolicited `/on_status` lifecycle events (`Accepted`, `In-progress`, `Packed`, `Agent-assigned`, `At-pickup`, `Order-picked-up`, `At-delivery`, `Order-delivered`, `Self-delivery-picked`), `/track`, and `/on_track`.
- **In-Flight Modifications & Exceptions**: `/update`, `/on_update`, `/cancel`, and `/on_cancel`.
- **Grievance Redressal**: Issue and Grievance Management under both IGM 1.0.0 and 2.0.0 architectures.

---

## Participants

| Participant | What This Means |
|---|---|
| **Buyer Application (BAP / BNP)** | The consumer-facing application (e.g. food delivery apps, bank/UPI apps, telco platforms) where diners discover nearby eateries, configure dish variants and customizations, select fulfillment modes (delivery, slotted delivery, self-pickup), input instructions, pay digitally, track delivery riders, and raise grievances. In commercial flows, acts as the Buyer Network Participant (BNP). |
| **Seller Application (BPP / SNP)** | An application representing restaurants, cloud kitchens, QSRs, food carts, or culinary aggregators. The BPP publishes live food menus, manages item customizations, checks kitchen serviceability, computes itemized quotes (dish prices, packaging fees, CGST/SGST, delivery), manages Kitchen Order Tickets (KOT), signals order prep status, and manages cancellations or refunds. In commercial flows, acts as the Seller Network Participant (SNP). |
| **Logistics Service Provider (LSP)** | A delivery network participant providing hyperlocal fulfillment. In Seller-managed logistics, the BPP or its integrated delivery partner assigns riders; in Buyer-managed delivery (`BUYER_DELIVERY`), the BAP coordinates logistics and pushes rider telemetry updates to the BPP. |
| **Gateway** | The ONDC routing infrastructure that multicasts broadcast discovery requests (`/search`) from BAPs to active seller applications (BPPs) based on domain code (`ONDC:RET11`), city code (e.g. `std:080`), and geolocation coordinates. |

---

## The User Journey

The standard F&B forward ordering journey (`ORDER_FLOW`) enables a diner to discover nearby restaurants, configure dish customizations, review transparent pricing and delivery turnaround times, provide delivery coordinates, complete payment, and receive freshly prepared food with end-to-end milestone tracking.

### 1. Discovery and Menu Search

The diner initiates discovery on the BAP by searching for restaurants, cuisines, or specific dishes:

- **Intent Broadcast**: The BAP transmits a `/search` request specifying domain code (`ONDC:RET11`), delivery GPS coordinates, area pin code, and fulfillment type (`Delivery` or `Self-Pickup`).
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

## Additional Scenarios & 1.2.5 Enhancements

Version 1.2.5 formally specifies diverse operational workflows and fulfillment variants that reflect the complexity of modern food delivery.

### 1. Mid-Order Address & Buyer Instructions Update

Consumers frequently need to adjust delivery details after checkout (e.g. updating a gate code, adding "do not ring bell" instructions, or correcting a house number before rider dispatch):
- **Address Update (`update_address`)**: The BAP transmits an updated shipping address via `/update` post-confirmation. The BPP validates the new address against restaurant serviceability and confirms via `/on_update`.
- **Buyer Instructions (`update_buyer_inst`)**: The BAP submits updated delivery instructions (e.g., contactless delivery notes, landmark descriptions) via `/update`, which the BPP acknowledges via `/on_update`.
- **Delivery Authorization (`on_update_delivery_auth`)**: The BPP sends an unsolicited update providing delivery authentication parameters (e.g., OTP requirements) prior to final doorstep delivery.

### 2. Buyer-Side Order Cancellation

A diner cancels an order before kitchen preparation or dispatch:
- **`/cancel` (BAP -> BPP)**: The BAP sends a cancellation request with an ONDC cancellation reason code (`order.cancellation_reason_id = "001"`).
- **`/on_cancel` (BPP -> BAP)**: The restaurant validates that the order is within its cancellable window (`@ondc/org/cancellable = true`), terminates fulfillment, sets `order.state = "Cancelled"`, recalculates any applicable fee deductions, and provides refund instructions.

### 3. Seller/System Force Cancellation

When unexpected kitchen failures occur (e.g., sudden equipment breakdown, fire, or severe logistic disruption) after confirmation:
- **`/cancel (cancel_force)` (BAP -> BPP)**: The BAP executes a force cancellation triggered by unresolvable fulfillment impediments.
- **`/on_cancel` (BPP -> BAP)**: The restaurant acknowledges cancellation and transitions states to `Cancelled`.
- **`/update (update_settelment_cancel)` (BAP -> BPP)**: The BAP issues an immediate refund settlement instruction to return funds to the customer.

### 4. Buyer-Managed Delivery (Buyer Logistics)

When the Buyer Application orchestrates delivery via its own logistics partner:
- The order is confirmed without seller logistics. Once packed (`on_status_packed`), the BAP coordinates pickup through its own delivery fleet, progressively notifying the restaurant:
  1. `update_buyer_delivery_agent_assigned` / `on_update`
  2. `update_buyer_delivery_intermin` (rider picked up parcel) / `on_update`
  3. `update_buyer_delivery_out_for_delivery` / `on_update`
  4. `update_buyer_delivery_final` (delivered to customer) / `on_update`

### 5. Self-Pickup (Takeaway Fulfillment)

Consumers order food to collect in person from the restaurant counter:
- In `/select` and `/init`, fulfillment type is configured as `Self-Pickup` without delivery charges.
- The restaurant prepares the food and marks it ready (`on_status_packed`).
- When the diner collects the meal at the restaurant, the BPP sends an unsolicited `on_status_self_delivery_picked` (`fulfillment.state = "Order-picked-up"`), completing the order.

### 6. Slotted and Scheduled Delivery

Consumers schedule food orders for specific future meal times (e.g., ordering at 10:00 AM for 1:30 PM delivery):
- In `/select` and `/init`, the buyer selects a delivery time slot (`on_select_slotted`).
- The restaurant holds the KOT until the appropriate prep window, cooks the meal, packs it, and coordinates timely rider dispatch to arrive strictly within the committed delivery slot.

### 7. Multi-Option Fulfillment (Dine-in / Takeaway / Delivery)

The restaurant presents multiple simultaneous fulfillment options in `/on_select` (e.g. Home Delivery, Takeaway, Dine-in):
- The buyer selects their preferred fulfillment option in `/init` (`init_fulfillment_array`).
- The quote and fulfillment terms dynamically reflect the selected mode.

### 8. BNP / SNP Negotiated Commercial Model

Protocol 1.2.5 standardizes commercial negotiations between Buyer Network Participants (BNPs) and Seller Network Participants (SNPs):
- During `/select` (`on_select_commercial_model`), `/init`, and `/confirm`, the participants negotiate and record commercial fee structures, commission models, buyer finder fees, and service charges directly within the protocol message contracts, ensuring transparent on-network settlement.

### 9. Promotional Offers and Discounts Flow

Exercises the discovery, validation, and application of promotional offers:
- During `/search` and `/select`, available restaurant offers (e.g., percentage discounts, flat off, item bundles) are transmitted in `offers[]`.
- In `/on_select` and `/on_init`, the seller applies promotional discounts, dynamically updating `quote.breakup[]` with discounted item totals and offer tags.

### 10. Merchant-Side Part-Cancellation and Return to Origin (RTO & Disposal)

- **Part-Cancellation**: If a dish ingredient is depleted mid-prep, the restaurant sends an unsolicited `/on_update (on_update_part_cancel)` removing the item and updating the quote. The BAP sends `/update (update_settlement_part_cancel)` to refund the difference.
- **RTO & Disposal**: If the rider arrives at the customer's location but the customer is unreachable, the restaurant initiates RTO (`on_cancel_rto`). Because prepared food is perishable, the returned parcel is liquidated/disposed of (`on_status_rto_disposed`).

### 11. Post-Delivery Return, Liquidation, and Refund

For spoiled, contaminated, cold, or incorrect food delivered to the customer:
- The diner submits a return claim (`update_return`).
- The restaurant acknowledges (`on_update_return_intermin`) and approves the claim (`on_update_return_final`), specifying liquidation disposition of the food.
- The BAP completes the refund via `update_settelment_return`.

### 12. Out of Stock Handling (Cart Recovery vs. Immediate Error Rejection)

- **Cart Recovery (`OUT_OF_STOCK`)**: The seller alerts the buyer via `on_select_out_of_stock`, allowing the buyer to modify the cart (`select`) and successfully proceed through checkout.
- **Immediate Error Rejection (`OUT_OF_STOCK(ERROR-CODE)`)**: Immediate rejection with standardized error codes `40002` (Out of Stock) or `30009` when checkout cannot proceed.

### 13. Incremental Menu Refresh (Push and Pull)

- **Push (`INCREMENTAL_CATALOG`)**: Restaurant broadcasts real-time menu deltas (sold-out items, price changes, kitchen pauses) via unsolicited `/on_search`.
- **Pull (`INCREMENTAL_CATALOG_PULL`)**: Buyer queries menu updates modified after a given timestamp (`last_updated_at`).

### 14. Statutory Compliance and Food Safety (FSSAI)

- Every restaurant must publish its 14-digit FSSAI license number in provider tags.
- Food items must include dietary declarations (`veg_non_veg`: `veg`, `non_veg`, or `egg`), allergen warnings, nutritional information, and transparent ingredient lists.

---

## Issue and Grievance Management

The F&B domain provides comprehensive complaint handling across both ONDC Issue and Grievance Management framework versions.

### 1. IGM 1.0.0 Architecture

1. **`issue (open)` (BAP -> BPP)**: Diner files a grievance regarding food quality, missing items, or delivery delays.
2. **`on_issue (processing)` (BPP -> BAP)**: Restaurant acknowledges the grievance with a ticket ID and expected resolution TAT.
3. **`on_issue_status (resolved)` (BPP -> BAP)**: Restaurant investigates and publishes resolution (`REFUND`, `REPLACEMENT`, or `NO_ACTION`).
4. **`issue (close)` (BAP -> BPP)**: Diner confirms resolution and closes the issue.

### 2. IGM 2.0.0 Architecture

IGM 2.0.0 features multi-party interactions, evidence exchange, dispute escalation, and automated corrective fulfillment:
- **Evidence Exchange (`DELIVERY_FLOW_WITH_IGM(v-2.0.0)`)**: Restaurant requests photo proof (`on_issue_need_more_info`), diner uploads images (`issue_info_provided`), restaurant proposes resolution, accepted by diner, triggering post-resolution refund/return (`on_update_igm_return`).
- **No-Action Resolution (`DELIVERY_FLOW_WITH_IGM_No_Action(v-2.0.0)`)**: Restaurant investigates and provides an explanatory resolution with `action_triggered = "NO_ACTION"`, accepted by diner, followed by audit status update (`on_status_igm_3`).
- **Rejection & Escalation (`DELIVERY_FLOW_WITH_IGM_Rejection(v-2.0.0)`)**: Diner rejects initial resolution (`issue_resolution_reject`), restaurant re-evaluates, diner escalates to Level 2 (Grievance Redressal Officer / Arbitrator), escalated resolution accepted, triggering corrective return (`on_update_igm_return`).

---

## Detailed Protocol Flows

### Flow 1: ORDER_FLOW (Prepaid Standard Delivery)

#### 1. Short Description
The foundational forward-fulfillment ordering journey. A diner selects dishes and customizations, receives an itemized quote with packaging charges, delivery fees, and taxes, inputs a delivery address, pays upfront, and receives the freshly prepared meal via seller-managed logistics with comprehensive rider milestone tracking.

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

### Flow 2: BUYER INSTRUCTIONS AND ADDRESS UPDATE FLOW

#### 1. Short Description
Demonstrates mid-order modifications where a buyer updates delivery instructions (e.g. "leave at security desk") and modifies the drop-off address after confirmation before rider dispatch, followed by delivery authorization and fulfillment.

#### 2. API Breakdown & Technical Actions
- **Steps 1–6 (`/select` to `/on_confirm`)**: Standard order creation and payment confirmation.
- **`on_status (on_status_pending)` [Unsolicited] (BPP -> BAP)**: Restaurant accepts the order.
- **`/update (update_address)` (BAP -> BPP)**: Buyer submits a corrected drop-off address (building, flat, street) via `/update`.
- **`/on_update (on_update_address)` (BPP -> BAP)**: Restaurant validates serviceability for the updated address and confirms modification.
- **`/update (update_buyer_inst)` (BAP -> BPP)**: Buyer adds specific delivery instructions (e.g., "call before arriving, ring second bell").
- **`/on_update (on_update_buyer_inst)` (BPP -> BAP)**: Restaurant logs instructions into the order fulfillment profile.
- **Fulfillment Progression**: Restaurant packs food (`on_status_packed`), rider assigned (`on_status_agent_assigned`), rider arrives at kitchen (`on_status_at_pickup`), and collects order (`on_status_order_picked`).
- **`on_update (on_update_delivery_auth)` [Unsolicited] (BPP -> BAP)**: Restaurant generates delivery authorization credentials (e.g., OTP verification).
- **Delivery Completion**: Rider arrives at location (`on_status_at_delivery`) and completes handover (`on_status_order_delivered`).

---

### Flow 3: BUYER_CANCEL (Buyer-Initiated Order Cancellation)

#### 1. Short Description
Exercises consumer-initiated order cancellation prior to food preparation or courier dispatch, validating order status termination and refund initiation.

#### 2. API Breakdown & Technical Actions
- **Steps 1–6 (`/select` to `/on_confirm`)**: Buyer places and confirms a prepaid food order.
- **`/cancel` (BAP -> BPP)**: Buyer initiates cancellation before dispatch, supplying cancellation reason code `001`.
- **`/on_cancel` (BPP -> BAP)**: Restaurant confirms cancellation (`order.state = "Cancelled"`, `fulfillment.state = "Cancelled"`), applies cancellation policy terms, and triggers refund.

---

### Flow 4: FORCE_CANCEL (Force Cancellation Post-Confirmation)

#### 1. Short Description
Handles force cancellation by the seller or system after confirmation due to unexpected kitchen or fulfillment disruptions, ensuring clean state termination and refund settlement.

#### 2. API Breakdown & Technical Actions
- **Steps 1–6 (`/select` to `/on_confirm`)**: Standard ordering and payment confirmation.
- **Steps 7–12 (`on_status`)**: Order accepted, packed, agent assigned, arrived at pickup, and picked up.
- **`on_status (on_status_at_delivery)` (BPP -> BAP)**: Rider arrives at delivery vicinity, where an insurmountable failure occurs.
- **`/cancel (cancel_force)` (BAP -> BPP)**: Force cancellation triggered.
- **`/on_cancel (on_cancel)` (BPP -> BAP)**: Restaurant confirms order cancellation (`order.state = "Cancelled"`).
- **`/update (update_settelment_cancel)` (BAP -> BPP)**: BAP transmits immediate refund settlement instructions.

---

### Flow 5: BUYER_DELIVERY (Buyer-Managed Logistics)

#### 1. Short Description
Validates buyer-managed logistics where the Buyer Application coordinates delivery and pushes progressive status updates to the restaurant BPP.

#### 2. API Breakdown & Technical Actions
- **Steps 1–6 (`/select` to `/on_confirm`)**: Order confirmed with buyer-managed delivery (`on_select_multiple_fulfillment`).
- **`on_status (on_status_pending)` & `on_status (on_status_packed)` (BPP -> BAP)**: Restaurant accepts and packs food.
- **`/update (update_buyer_delivery_agent_assigned)` (BAP -> BPP)**: BAP notifies restaurant that a delivery rider has been assigned.
- **`/on_update` (BPP -> BAP)**: Restaurant acknowledges rider assignment.
- **`/update (update_buyer_delivery_intermin)` (BAP -> BPP)**: BAP signals rider has collected food from restaurant (`Order-picked-up`).
- **`/on_update` (BPP -> BAP)**: Restaurant logs pickup.
- **`/update (update_buyer_delivery_out_for_delivery)` (BAP -> BPP)**: BAP updates status to out for delivery.
- **`/on_update` (BPP -> BAP)**: Restaurant acknowledges transit state.
- **`/update (update_buyer_delivery_final)` (BAP -> BPP)**: BAP reports successful delivery to consumer.
- **`/on_update` (BPP -> BAP)**: Restaurant finalizes order state as `Completed`.

---

### Flow 6: SELF_PICKUP (Takeaway / Self-Collection)

#### 1. Short Description
Consumer places an order for takeaway or in-person collection directly at the restaurant counter, omitting courier logistics.

#### 2. API Breakdown & Technical Actions
- **`/select` -> `/on_select (on_select_multiple_fulfillment)`**: Buyer specifies `Self-Pickup` fulfillment type; quote omits delivery charges.
- **`/init` -> `/on_init` -> `/confirm` -> `/on_confirm`**: Order established for takeaway.
- **`on_status (on_status_pending)` (BPP -> BAP)**: Restaurant accepts order.
- **`on_status (on_status_packed)` (BPP -> BAP)**: Kitchen prepares food and marks order ready for collection at the counter.
- **`on_status (on_status_self_delivery_picked)` [Unsolicited] (BPP -> BAP)**: Customer collects the food parcel in person (`fulfillment.state = "Order-picked-up"` / completed).

---

### Flow 7: SLOTTED_DELIVERY (Scheduled Delivery Windows)

#### 1. Short Description
Buyer selects a specific future delivery time slot (e.g. lunch or dinner time window) during checkout; the restaurant manages kitchen preparation to meet the committed slot.

#### 2. API Breakdown & Technical Actions
- **`/select` (BAP -> BPP)**: Buyer requests order with preferred time slot parameters.
- **`/on_select (on_select_slotted)` (BPP -> BAP)**: Restaurant confirms serviceability and locks the chosen delivery slot.
- **`/init (init_multiple_fulfillment)` -> `/on_init` -> `/confirm` -> `/on_confirm`**: Order confirmed for the scheduled window.
- **Fulfillment Progression**: Closer to the slot, restaurant accepts (`on_status_pending`), prepares and packs (`on_status_packed`), assigns rider (`on_status_agent_assigned`), executes pickup (`on_status_at_pickup`, `on_status_order_picked`), and delivers within the committed slot (`on_status_at_delivery`, `on_status_order_delivered`).

---

### Flow 8: MULTI_OPTION_FULFILLMENT_FLOW (Multi-Fulfillment Modes)

#### 1. Short Description
The restaurant presents multiple simultaneous fulfillment options (Home Delivery, Takeaway, Dine-in) in `/on_select`, allowing the buyer to evaluate and select the desired mode.

#### 2. API Breakdown & Technical Actions
- **`/select` (BAP -> BPP)**: Buyer explores menu offerings.
- **`/on_select (on_select_fulfillment_array)` (BPP -> BAP)**: Restaurant returns multiple fulfillment options with distinct pricing and TATs.
- **`/init (init_fulfillment_array)` (BAP -> BPP)**: Buyer selects their chosen fulfillment mode from the array.
- **`/on_init (on_init_fulfillment_array)` (BPP -> BAP)**: Restaurant freezes terms and quote tailored to the selected fulfillment mode.
- **`/confirm` -> `/on_confirm`**: Order confirmed.
- **`on_status` Milestones**: Order progresses through acceptance, packaging, pickup, transit, and delivery completion.

---

### Flow 9: COMMERCIAL_MODEL_FOR_BNP/SNP_FLOW (Negotiated Commercials)

#### 1. Short Description
Exercises on-network commercial agreements and negotiated pricing between the Buyer Network Participant (BNP) and Seller Network Participant (SNP), ensuring commercial terms and commissions are validated.

#### 2. API Breakdown & Technical Actions
- **`/select` (BAP -> BPP)**: Buyer initiates cart selection.
- **`/on_select (on_select_commercial_model)` (BPP -> BAP)**: Restaurant provides quote incorporating negotiated BNP/SNP commercial model attributes.
- **`/init (init_commercial_model)` -> `/on_init (on_init_commercial_model)`**: Both participants exchange settlement terms, buyer finder fee percentages, and commission models.
- **`/confirm (confirm_commercial_model)` -> `/on_confirm (on_confirm_commercial_model)`**: Order confirmed, legally binding agreed commercial terms on-network.

---

### Flow 10: OFFERS_FLOW (Offer Discovery and Pricing Adjustment)

#### 1. Short Description
Demonstrates discovery, validation, and application of promotional discounts, coupon codes, and offer-adjusted quotes during checkout.

#### 2. API Breakdown & Technical Actions
- **`/search` -> `/on_search`**: Catalog returned with promotional discounts and coupon codes in `offers[]`.
- **`/select` (BAP -> BPP)**: Buyer selects dishes and applies eligible promo offer.
- **`/on_select` (BPP -> BAP)**: Restaurant validates offer eligibility, returning `quote.breakup[]` with discount deductions.
- **`/init` -> `/on_init` -> `/confirm` -> `/on_confirm`**: Order successfully initialized and confirmed with discounted net totals.

---

### Flow 11: OUT_OF_STOCK (Inventory Depletion with Cart Recovery)

#### 1. Short Description
Handles inventory shortages where an ordered dish is temporarily depleted. The restaurant alerts the buyer via `on_select_out_of_stock`, allowing the diner to modify cart items and complete the purchase.

#### 2. API Breakdown & Technical Actions
- **`/select (select0)` (BAP -> BPP)**: Diner selects dishes.
- **`/on_select (on_select_out_of_stock)` (BPP -> BAP)**: Restaurant flags item as unavailable (`quantity.available.count = 0`).
- **`/select (select)` (BAP -> BPP)**: Diner adjusts cart to choose available menu items.
- **`/on_select (on_select)` (BPP -> BAP)**: Restaurant validates stock and generates quote.
- **`/init` through `/on_status (order_delivered)`**: Order proceeds through normal confirmation and fulfillment to delivery.

---

### Flow 12: OUT_OF_STOCK(ERROR-CODE) (Immediate Error Rejection)

#### 1. Short Description
Validates immediate protocol rejection when a buyer attempts to checkout items that are out of stock, returning standardized ONDC error codes (`40002` / `30009`).

#### 2. API Breakdown & Technical Actions
- **`/select (select_oos)` (BAP -> BPP)**: Buyer selects depleted items.
- **`/on_select (on_select_oos)` (BPP -> BAP)**: Restaurant immediately rejects selection with error block containing code `40002` (Out of stock) or `30009`.

---

### Flow 13: RETURN_FLOW (Post-Delivery Return & Liquidation)

#### 1. Short Description
Covers the post-delivery claim and liquidation lifecycle. When delivered food arrives spoiled, spilled, or incorrect, the diner submits a return claim, which the restaurant approves with liquidation disposition, followed by refund settlement.

#### 2. API Breakdown & Technical Actions
- **Forward Fulfillment (Steps 1–13)**: Order placed, prepared, dispatched, and delivered (`on_status_order_delivered`).
- **`/update (update_return)` (BAP -> BPP)**: Diner submits a claim detailing affected items, quantities, return reason code (e.g., `001` - quality/damaged), and photographic evidence.
- **`/on_update (on_update_return_intermin)` (BPP -> BAP)**: Restaurant acknowledges claim in state `Return_Initiated`.
- **`on_update (on_update_return_final)` [Unsolicited] (BPP -> BAP)**: Restaurant approves claim and authorizes liquidation disposition (food disposed, not returned to kitchen).
- **`/update (update_settelment_return)` (BAP -> BPP)**: BAP transmits refund settlement instructions.

---

### Flow 14: RTO_PLUS_PART_CANCELLATION (Kitchen Stockout & Failed Last-Mile RTO)

#### 1. Short Description
A multi-exception workflow handling kitchen ingredient stockouts during prep (part-cancellation), followed by an unsuccessful delivery attempt where the diner is unreachable, culminating in Return to Origin and perishable food disposal.

#### 2. API Breakdown & Technical Actions
- **Steps 1–6 (`/select` to `/on_confirm`)**: Multi-item food order confirmed.
- **`on_update (on_update_part_cancel)` [Unsolicited] (BPP -> BAP)**: Kitchen realizes an ingredient is depleted, partially cancels that item, and adjusts price quote.
- **`/update (update_settlement_part_cancel)` (BAP -> BPP)**: BAP submits settlement trail reflecting the partial refund.
- **Fulfillment Progression (Steps 9–15)**: Remaining dishes packed, rider assigned, picked up, and transported to destination.
- **`on_cancel (on_cancel_rto)` [Unsolicited] (BPP -> BAP)**: Rider cannot contact buyer at destination; restaurant initiates RTO (reason `013`).
- **`/update (update_settlement_part_cancel_1)` (BAP -> BPP)**: BAP transmits RTO settlement terms.
- **`on_status (on_status_rto_disposed)` [Unsolicited] (BPP -> BAP)**: Undelivered perishable meal disposed/liquidated at store; order marked `Cancelled`.

---

### Flow 15: FULL_CATALOG (Full Menu Discovery)

#### 1. Short Description
City-wide broadcast discovery enabling diners to explore full restaurant menus, categories, dishes, customization groups, and serviceability radiuses.

#### 2. API Breakdown & Technical Actions
- **`/search (search)` (BAP -> Gateway)**: BAP broadcasts discovery query (`context.city = "std:080"`, `intent.category.id = "ONDC:RET11"`).
- **`/on_search (on_search)` (BPP -> BAP)**: Restaurant responds with comprehensive menu catalog (categories, dishes, prices, veg/non-veg tags, customization groups `CG1`/`CG2`, and FSSAI license).

---

### Flow 16: INCREMENTAL_CATALOG (Incremental Menu Push)

#### 1. Short Description
Validates merchant-initiated real-time menu updates. Restaurants push live changes regarding dish availability ("86'd" items), daily specials, or temporary kitchen closure without requiring a full catalog reload.

#### 2. API Breakdown & Technical Actions
- **`/search (search_1)` -> `/on_search (on_search_1)`**: Baseline search.
- **`on_search (on_search_3)` [Unsolicited] (BPP -> BAP)**: Restaurant pushes item delta (e.g. dish marked out of stock).
- **`on_search (on_search_2)` [Unsolicited] (BPP -> BAP)**: Restaurant pushes serviceability delta (e.g. kitchen temporarily paused).
- **`/search (search_2)` (BAP -> Gateway)**: Verification query confirming catalog synchronization.

---

### Flow 17: INCREMENTAL_CATALOG_PULL (Incremental Menu Pull)

#### 1. Short Description
Validates the buyer application pull mechanism for menu synchronization. The buyer requests menu modifications that occurred after a specific timestamp (`last_updated_at`).

#### 2. API Breakdown & Technical Actions
- **`/search (search_1)` -> `/on_search (on_search1)`**: Baseline full catalog discovery.
- **`/search (search_inc_pull)` (BAP -> BPP)**: Targeted search specifying `mode = "incremental_refresh"` and `last_updated_at`.
- **`/on_search (on_search_inc_pull)` (BPP -> BAP)**: Restaurant responds with strictly those dishes modified since the requested cutoff.

---

### Flow 18: DELIVERY_FLOW_WITH_IGM(v-1.0.0) (Grievance Resolution v1.0.0)

#### 1. Short Description
Complete forward fulfillment flow integrated with the standard IGM 1.0.0 complaint resolution cycle. After delivery, the diner reports a quality defect, which the restaurant investigates and resolves.

#### 2. API Breakdown & Technical Actions
- **Delivery Steps (1–15)**: Forward fulfillment completed to `order_delivered`.
- **`/issue (issue_open_100)` (BAP -> BPP)**: Diner files a complaint citing food quality defects (e.g., cold food, missing item), attaching photos and contact info.
- **`/on_issue (on_issue_processing_100)` (BPP -> BAP)**: Restaurant acknowledges complaint, assigns ticket ID, and sets expected resolution TAT.
- **`on_issue_status (on_issue_resolved_100)` [Unsolicited] (BPP -> BAP)**: Restaurant investigates and posts resolution (`RESOLVED`), authorizing refund.
- **`/issue (issue_close_100)` (BAP -> BPP)**: Diner confirms satisfactory resolution and closes ticket.

---

### Flow 19: DELIVERY_FLOW_WITH_IGM(v-2.0.0) (Evidence Exchange & Corrective Return)

#### 1. Short Description
Validates interactive evidence-gathering under IGM 2.0.0. The restaurant requests photo proof of food containers, the diner uploads evidence, the restaurant approves resolution, and an automated post-resolution refund/return is triggered.

#### 2. API Breakdown & Technical Actions
- **Delivery Steps (1–15)**: Order delivered.
- **`/issue (issue_open)` -> `/on_issue (processing)`**: Diner reports damaged/wrong meal delivered.
- **`on_issue (on_issue_need_more_info)` [Unsolicited] (BPP -> BAP)**: Restaurant requests photo evidence of food containers and bill.
- **`/issue (issue_info_provided)` (BAP -> BPP)**: Diner uploads requested photos and remarks.
- **`/on_issue (on_issue_provided)` (BPP -> BAP)**: Restaurant confirms receipt of evidence.
- **`on_issue (on_issue_resolution)` [Unsolicited] (BPP -> BAP)**: Restaurant validates proof and proposes resolution.
- **`/issue (issue_resolution_accept)` (BAP -> BPP)**: Diner accepts resolution.
- **`/on_issue (on_issue_resolved)` -> `/issue (issue_close)`**: Grievance closed as resolved.
- **`on_update (on_update_igm_return)` [Unsolicited] (BPP -> BAP)**: Restaurant triggers automated post-resolution refund/return fulfillment.

---

### Flow 20: DELIVERY_FLOW_WITH_IGM_No_Action(v-2.0.0) (No-Action Resolution)

#### 1. Short Description
Validates IGM 2.0.0 where a grievance is processed, a formal explanation is tendered with `action_triggered = "NO_ACTION"`, accepted by the diner, and finalized with an order audit update.

#### 2. API Breakdown & Technical Actions
- **Delivery Steps (1–15)**: Order delivered.
- **`/issue (issue_open_2)` -> `/on_issue (on_issue_processing)`**: Grievance registered and acknowledged.
- **`on_issue (on_issue_resolution_igm_3)` [Unsolicited] (BPP -> BAP)**: Restaurant tenders resolution proposal (`action_triggered = "NO_ACTION"` with explanatory remarks).
- **`/issue (issue_resolution_accept_igm_3)` (BAP -> BPP)**: Diner formally accepts the explanation.
- **`/on_issue (on_issue_resolved_igm_3)` -> `/issue (issue_close_igm_3)`**: Grievance marked resolved and closed.
- **`on_status (on_status_igm_3)` [Unsolicited] (BPP -> BAP)**: Restaurant updates post-resolution order audit status.

---

### Flow 21: DELIVERY_FLOW_WITH_IGM_Rejection(v-2.0.0) (Rejection & Escalation)

#### 1. Short Description
A multi-tier grievance escalation flow under IGM 2.0.0. The diner rejects the initial resolution, escalates the dispute to higher authorities (Grievance Redressal Officer / Arbitrator), reaches an accepted binding resolution, and receives an authorized refund/return.

#### 2. API Breakdown & Technical Actions
- **Delivery Steps (1–15)**: Forward fulfillment completed.
- **`/issue (issue_open)` -> `/on_issue (processing)`**: Initial grievance logged.
- **`on_issue (on_issue_resolution)` [Unsolicited] (BPP -> BAP)**: Restaurant proposes initial settlement.
- **`/issue (issue_resolution_reject)` (BAP -> BPP)**: Diner rejects proposed resolution as unsatisfactory.
- **`/on_issue (processing_1)` -> `on_issue (resolution_1)`**: Restaurant tenders revised proposal.
- **`/issue (issue_escalate)` (BAP -> BPP)**: Diner escalates grievance to Level 2 (GRO / ODR arbitrator).
- **`/on_issue (processing_2)` -> `on_issue (resolution_2)`**: Escalated authority issues binding resolution.
- **`/issue (issue_resolution_accept)` (BAP -> BPP)**: Diner accepts escalated resolution.
- **`/on_issue (on_issue_resolved)` -> `/issue (issue_close)`**: Ticket closed as resolved.
- **`on_update (on_update_igm_return)` [Unsolicited] (BPP -> BAP)**: Restaurant initiates official return and refund workflow for contested items.

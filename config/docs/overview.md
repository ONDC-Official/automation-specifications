# ONDC:TRV10 2.1.0 — Overview

## Summary

ONDC:TRV10 is the ONDC domain specification for **ride-hailing (mobility) services**. It lets a passenger discover, book, track, modify, cancel and pay for a ride through any ONDC-enabled buyer app, with the ride fulfilled by any ONDC-enabled provider platform on the network. Instead of being locked into a single app, consumers can search across multiple ride-hailing providers, and providers can offer their vehicles and drivers to many consumer apps at once.

Version 2.1.0 covers the **Ride-hailing** use case and is marked **RELEASED**.

## Sector & Purpose

This specification addresses urban and intercity transportation. The problem it solves is **consumer and driver lock-in**: passengers normally install a separate app for each ride-hailing service, and drivers must juggle several platforms to keep their earnings up. TRV10 defines a common, machine-readable contract (APIs, message schemas, flows and validations) so that any buyer app can request rides from any provider, and any driver or fleet can serve requests from any buyer app.

## Real-World Actors

| Actor | Role in the network |
| --- | --- |
| **Rider / Passenger** | The consumer who needs a ride, for themselves or for others. |
| **BAP (Buyer App)** | The consumer-facing app that discovers rides, lets the rider book, track, update, cancel and rate, and may collect payment. |
| **BPP (Seller App / Provider Platform)** | The ride-hailing platform that owns or manages vehicles and drivers, quotes fares, assigns drivers and fulfills the ride. |
| **Driver / Agent** | The person who drives the vehicle. They are assigned by the BPP and shown to the rider with vehicle and location details. |
| **Registry & Gateway** | ONDC network infrastructure that authenticates participants (signed requests) and broadcasts discovery requests. |

## The User Journey

1. **Discover** — The rider enters pickup and drop locations (and optionally time, vehicle category or preferences). The BAP sends `search`; providers reply with `on_search` listing available vehicle types, fares and ETAs.
2. **Select** — The rider picks an option, optionally with add-ons (for example a child seat or luggage carrier). `select` / `on_select` returns a firm quote with a fare breakup.
3. **Initiate** — The BAP sends `init` with billing and payment details; the BPP replies with `on_init` containing the final terms, quote and payment settlement terms.
4. **Confirm** — The BAP sends `confirm` to book the ride. The BPP responds with `on_confirm`. Depending on the flow, the **driver is assigned at `on_confirm`** or **after `on_confirm`** through an `on_status` / `on_update`.
5. **Track the trip** — The BAP polls with `status` or receives unsolicited `on_status`/`on_update` as the ride moves through its stages, and uses `track` / `on_track` for the driver's live location.
6. **Modify (optional)** — While the ride is active the rider can change stops (`update` / `on_update`), or the BAP can report a payment settlement.
7. **Complete** — The ride ends, the final fare is shown (and revised if the actual ride differed from the quote), payment is settled, and the rider may add a tip or rate the experience.
8. **Support and issues** — At any point the rider can reach support (`support` / `on_support`) or raise a grievance (`issue`, `on_issue`, `on_issue_status`) via IGM.

## Ride Lifecycle

A ride moves through fulfillment states reported by the provider:

`RIDE_CONFIRMED` → `RIDE_ASSIGNED` → `RIDE_ENROUTE_PICKUP` → `RIDE_ARRIVED_PICKUP` → `RIDE_STARTED` → `RIDE_ENDED`

A ride can end instead in `RIDE_CANCELLED`, initiated by the rider, the driver, or the platform (for example when no driver is found, or a technical cancellation occurs).

## Supported Actions

| Group | Actions |
| --- | --- |
| Discovery | `search`, `on_search` |
| Booking | `select`, `on_select`, `init`, `on_init`, `confirm`, `on_confirm` |
| Fulfillment | `status`, `on_status`, `track`, `on_track` |
| Changes | `update`, `on_update`, `cancel`, `on_cancel` |
| Support | `support`, `on_support`, `rating` |
| Grievance (IGM) | `issue`, `on_issue`, `on_issue_status` |

## Use Cases

- **On-demand ride booking** — Immediate ride with driver assignment either at `on_confirm` or after it.
- **Scheduled trips** — A ride booked in advance for a future pickup time, with or without the "ride en route to pickup" status.
- **Rental rides** — A vehicle booked for an hourly/extended period, including the case where the end stop GPS is known.
- **Multiple stops and stop updates** — A ride with several pickup or drop points, and changes to a stop during an active ride.
- **Add-ons** — Optional extras (child seat, luggage carrier, pet carrier) attached at selection and carried through quote, confirmation and status.
- **Pre-order bidding** — Providers bid on a ride request before confirmation.
- **Payment collection models** — Provider-collected payment, or **BAP-collecting** (including pre-order payment, and a revised fare at ride end that the BAP settles via `update`).
- **Cancellation** — Rider-initiated, driver-initiated, technical cancellation with retry, and soft cancellation when a ride is not accepted.
- **Driver not found** — Failure handling when no driver is available at `on_confirm` or after it, for both on-demand and scheduled rides.
- **Post-ride tip** — The rider adds a tip after the ride is completed.
- **Preference-based matching** — For example a female-driver flow for rider safety.
- **Grievance management (IGM)** — Issue raising and resolution, including seller-initiated cancellation and rejection or no-action handling.

## Key Concepts

- **Network interoperability** — Any BAP can book with any BPP; no single company controls access.
- **Quote and fare breakup** — Fares are expressed as itemised components (base fare, distance, add-ons, taxes, tips and so on) that stay consistent from `on_select` through `on_status`.
- **Driver assignment timing** — Assignment can be immediate at `on_confirm` or deferred; the flows differ in when driver and vehicle details appear.
- **Collector of payment** — Either the BPP or the BAP collects the fare, with settlement terms agreed at `init`.
- **Unsolicited updates** — The BPP pushes ride state changes through `on_status` and `on_update` without a request from the BAP.
- **Signed, authenticated messages** — Every call is signed by the sender and verified against the network registry.

## Flow Catalogue

The spec ships **43 flows**, all under the Ride-hailing use case. Tags show whether a flow is `MANDATORY` or `OPTIONAL` for certification, whether it is `ON_DEMAND` or `SCHEDULED`, and whether it is `REPORTABLE`. In the sequences below, `*` marks an unsolicited call (sent by the BPP without a request), and every request is followed by its `on_` callback. All flows begin with `search → select → init → confirm` and the matching callbacks.

### 1. Core on-demand booking

| Flow | Tags | What it covers | Calls after `on_confirm` |
| --- | --- | --- | --- |
| **OnDemand_Assign_driver_on_onconfirm** (base flow) | Mandatory | The driver is assigned at `on_confirm`. The ride is tracked and moves through every ride state to completion, and the rider then rates it. | `on_track*`, `on_status*`, `track`, `on_status*` (×3), `on_update*`, `status`, `rating` |
| **OnDemand_Assign_driver_post_on_confirm** | Mandatory | `on_confirm` returns without a driver. The BPP assigns one later through an unsolicited `on_update`. Includes an unsolicited `on_support` and a final `rating`. | `on_update*`, `on_track*`, `track`, `on_status*`, `on_support*`, `on_update*`, `status`, `rating` |
| **OnDemand_Assign_driver_post_onconfirmSelfPickup** | Optional | Late assignment where the rider goes to the pickup point (self pickup) instead of the driver coming to them. | `on_update*`, `on_track*`, `track`, `on_status*`, `status` |
| **OnDemand_Pre_Order_Bid** | Optional | Providers bid on the ride request, and the rider confirms a pre-order at the bid price. | tracking and status updates to ride end |
| **OnDemand_Post_Order_Tip** | Optional | The rider adds a tip after the ride is completed, using `update` / `on_update`. | tracking, `status`, then `update` / `on_update` |
| **OnDemand_Assign_driver_on_onconfirm_Add_Ons** | Optional | Optional extras (child seat, luggage carrier) are attached at `select`. The add-on fare component persists through quote, confirmation and status. | base flow without rating |
| **OnDemand_Purple_Tags_Assign_driver_on_onconfirm** | Optional | Base on-demand booking that carries the Purple (accessibility / inclusive-service) tag group. | tracking and `status` |
| **OnDemand_Female_Driver_Flow** | Optional | Rider and driver are both female (safety preference matching). | tracking, `on_update*`, `status` |

### 2. Payment collection by the buyer app (BAP-collecting)

| Flow | What it covers |
| --- | --- |
| **..._BAP_Collecting** | The BAP collects the fare. After the ride ends, it reports the PAID payment through `update`, and the BPP acknowledges with `on_update`. |
| **..._BAP_Collecting_Pre_Order** | The BAP collects up front. Payment is marked PAID, with amount and payment transaction id, at `confirm`, and it persists through tracking to completion. |
| **..._BAP_Collecting_Quote_Update** | The fare is revised at ride end. The ride-ended `on_update` carries the revised quote, the BAP settles the new amount through `update`, and the BPP acknowledges with `on_update`. |

### 3. Cancellations and failures

| Flow | Tags | What it covers |
| --- | --- | --- |
| **Driver_not_found_on_onconfirm** | Mandatory | No driver is available when the booking is confirmed. The failure is returned in `on_confirm`. |
| **Driver_not_found_post_onconfirm** | Mandatory | The booking is accepted at `on_confirm`, then the BPP cancels with an unsolicited `on_cancel` because no driver could be assigned. |
| **OnDemand_Ride_cancellation_by_driver** | Mandatory | After confirmation the driver cancels, and the BPP notifies the BAP with an unsolicited `on_cancel`. |
| **OnDemand_Ride_cancellation_by_rider** | Mandatory | The rider cancels a confirmed ride before it starts, using `cancel` / `on_cancel`. The flow shows the cancel sequence twice, covering the cancellation-terms check and the final cancel. |
| **OnDemand_Ride_Technical_Cancellation_Flow** | Optional | A technical cancellation and its retry handling. The flow runs `status` and then `cancel` / `on_cancel` twice. |
| **No_Acceptance_SoftCancel** | Optional | The ride stays unaccepted, so the rider soft-cancels. The BPP's `on_cancel` and a following `on_status*` confirm the order state. |
| **No_Acceptance_SoftUpdate** | Optional | The ride stays unaccepted, and the rider tries to modify it with `update` / `on_update` while tracking. |

### 4. Changing a ride in progress

| Flow | Tags | What it covers |
| --- | --- | --- |
| **OnDemand_Ride_with_multiple_stops** | Optional | A ride with several pickup or drop points. Tracking and status updates cover each leg. |
| **OnDemand_Update_Stop** | Optional | The rider changes a pickup or drop stop during the ride. Two `update` / `on_update` exchanges are shown, and the ride is then tracked to completion. |

### 5. Rentals

| Flow | Tags | What it covers |
| --- | --- | --- |
| **OnDemand_Rental** | Optional, rental | An on-demand hourly rental with tracking and status updates to completion. |
| **OnDemand_Rentalwhen_end_stop_gps_coordinate_is_present** | Optional, rental | A rental where the end stop has a GPS coordinate. The BPP sends an `on_update*` after confirmation. |
| **Schedule_Rental** | Optional, scheduled, rental | A rental booked ahead for a future start time. |

### 6. Grievance management (IGM)

| Flow | What it covers |
| --- | --- |
| **..._With_IGM(v-1.0.0)** | An issue is raised after the ride (`issue`, `on_issue`, `on_issue_status*`), and the buyer follows up with a second `issue`. This is a mandatory flow. |
| **..._With_IGM(v-2.0.0)** | The IGM 2.0 issue lifecycle, with several `issue` / `on_issue` exchanges and unsolicited `on_issue*` updates. |
| **..._With_IGM_No_Action(v-2.0.0)** | An IGM 2.0 issue that the seller does not act on, ending in escalation. |
| **..._With_IGM_Rejection(v-2.0.0)** | An IGM 2.0 issue that the seller rejects, ending with the buyer's final response. |
| **..._With_IGM_v-1.0.0_With_Seller_Cancellation** | An IGM 1.0 issue raised right after confirmation that leads to a seller-initiated `on_cancel*`. |
| **Schedule_Trip_With_IGM(v-1.0.0)** | An IGM 1.0 issue raised on a scheduled trip. |
| **Schedule_Trip_With_IGM_v-1.0.0_With_Seller_Cancellation** | An IGM 1.0 issue on a scheduled trip that leads to a seller cancellation. |

### 7. Scheduled trips

| Flow | What it covers |
| --- | --- |
| **Schedule_Trip** | The base scheduled booking. The rider books for a future pickup time, the driver is assigned later through `on_update*`, and the trip ends with `status` and `rating`. |
| **Schedule_Trip_Without_Ride_Enroute_Pickup_Status** | The same as above, but the provider does not send the `RIDE_ENROUTE_PICKUP` state. |
| **Schedule_Trip_Cancellation_By_Driver** | The driver cancels a scheduled trip, and the BPP sends an unsolicited `on_cancel`. |
| **Schedule_Trip_Cancellation_By_Rider** | The rider cancels a scheduled trip after tracking has begun. |
| **Schedule_Trip_Rider_Cancellation_After_Driver_Assignment** | The rider cancels right after a driver has been assigned. |
| **Schedule_Trip_Driver_Not_Found_Post_onconfirm** | No driver is found after confirmation, and the BPP cancels the order. |
| **Schedule_Trip_With_Pre_Order_Bid** (and **..._Without_Ride_Enroute_Pickup**) | Provider bidding on a scheduled trip, with an unsolicited `on_support*` in the base variant. |
| **Schedule_Trip_BAP_Collecting** (and **..._Without_Ride_Enroute_Pickup**) | The buyer app collects payment on a scheduled trip. |
| **Schedule_Trip_With_Add_Ons** (and **..._Without_Ride_Enroute_Pickup**) | Optional add-ons (child seat, luggage carrier, pet carrier) on a scheduled trip. |

### How the flows differ

- **Driver assignment timing** — At `on_confirm` (on-demand base flows) or later through `on_update*` (post-`on_confirm` and every scheduled flow).
- **Who collects payment** — The BPP by default, or the BAP in the BAP-collecting flows, where payment is reported through `update`.
- **Who ends the order early** — The rider (`cancel`), the driver or provider (unsolicited `on_cancel*`), or the system (driver not found, no acceptance).
- **Optional ride states** — The scheduled "Without Ride Enroute Pickup" variants skip `RIDE_ENROUTE_PICKUP`.


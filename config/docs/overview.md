# ONDC:TRV10 2.0.1 — Overview

## Summary

ONDC:TRV10 is a domain specification for on-demand ride-hailing that lets passengers book cabs, auto-rickshaws and two-wheelers through any ONDC-enabled buyer application on a shared network. Instead of being locked into a single app, consumers can search for and book rides across multiple ride-hailing providers, and providers can offer their vehicles and drivers to many buyer apps at once.

Version 2.0.1 is a patch release on the 2.0 specification. It adds:
- the `SELF_PICKUP` fulfilment type for queue locations such as airports and railway stations;
- vehicle category and variant enums;
- standard cancellation reason codes;
- the `RIDE_CONFIRMED` ride state;
- flows for driver-not-found handling, female driver preference, issue handling (IGM 1.0.0) and seller-collected payment confirmation.

## Sector & Purpose

This domain addresses the ride-hailing and transportation sector. The problem it solves is **consumer lock-in**: passengers normally need a separate app for each ride-hailing service, and every platform keeps its own isolated user base. Drivers and fleets depend on the demand that a single platform can generate for them.

ONDC:TRV10 creates an interoperable network. A single buyer app can request rides from any participating provider, and any provider can serve requests from any buyer app. Passengers get a wider choice of vehicles and prices in one place, and providers reach riders they would not have reached on their own.

## Real-World Actors

The transactions happen between **consumers** (passengers looking for a ride) and **ONDC-enabled ride-hailing platforms** (the companies that operate fleets, manage drivers and run booking systems).

- **Passenger / rider** — Needs a ride. Searches, compares and books through a buyer app, shares pickup and drop locations, and gives an OTP to start the trip.
- **Buyer app (BAP)** — The consumer-facing application. Sends `search`, `select`, `init` and `confirm`, shows the quote and live ride status, and can raise a cancellation or an issue.
- **Seller app (BPP)** — The ride-hailing platform. Publishes its catalogue of vehicles and fares, assigns a driver and vehicle, sends status and tracking updates, and can cancel when no driver is available.
- **Driver / agent** — Operates the vehicle and fulfils the ride. Name and vehicle details are shared with the passenger once assigned, except for self-pickup rides.
- **ONDC network** — Carries discovery and transaction messages between buyer and seller apps.

## How a Ride Works (start here)

Every call goes from one app to the other and is acknowledged with an `ACK`. The real answer then arrives asynchronously as the matching `on_` call, so every action has a request and a callback.

| Step | Call (BAP → BPP) | Callback (BPP → BAP) | What happens |
| :--- | :--------------- | :------------------- | :----------- |
| 1. Discover | `search` | `on_search` | The buyer app sends the pickup and drop locations; each seller app returns its catalogue with vehicle options and estimated fares |
| 2. Choose | `select` | `on_select` | The passenger picks an option and receives a detailed quote |
| 3. Initialise | `init` | `on_init` | Order terms and payment terms are shared and agreed, giving a final draft order |
| 4. Confirm | `confirm` | `on_confirm` | The booking is confirmed; the driver may be assigned here or later |
| 5. Follow the ride | `status`, `track` | `on_status`, `on_track`, `on_update` | The ride moves through pickup, trip start and trip end; the seller app can also push `on_status` and `on_update` unsolicited |
| 6. Cancel (if needed) | `cancel` | `on_cancel` | A soft cancel returns the terms, and a confirm cancel finalises the cancellation |
| 7. Raise an issue | `issue`, `issue_status` | `on_issue`, `on_issue_status` | The buyer app raises a complaint and checks its resolution status, handled with IGM 1.0.0 |

Which calls are allowed to follow which is defined in `config/actions/index.yaml`. For example, `confirm` can only be followed by `on_confirm` or `status`, and `on_confirm` can be followed by `status`, `cancel`, `on_status`, `on_update`, `update` or `on_cancel`.

## Use Cases

- **On-demand ride booking** — A passenger requests an immediate ride and gets vehicle options and fares; the ride is confirmed once the booking is selected, initialised and confirmed
- **Driver assignment on confirm** — The seller app assigns a driver and vehicle in the `on_confirm` response, so the passenger sees driver details straight away
- **Driver assignment after confirm** — The ride is confirmed first, and driver and vehicle details follow later through `on_status` and `on_update`
- **Self-pickup rides** — At designated queue locations, only an OTP is shared after `RIDE_CONFIRMED`, with no agent or vehicle details; the `START` stop may carry instructions for reaching the pickup point, which the buyer app must display
- **Female driver preference** — The passenger can ask for a female driver using the optional customer and agent gender fields
- **Real-time tracking and journey updates** — The passenger tracks the vehicle with `track`/`on_track` and follows the ride through status and update calls
- **Seller-collected payment confirmation** — The seller app collects the payment and confirms it with the buyer app
- **Ride cancellation by the rider** — The passenger cancels a confirmed ride before it starts, using soft and confirm cancel, and the quote shows the refund
- **Ride cancellation by the driver** — The seller app cancels after the driver declines or becomes unavailable, and the `on_cancel` carries the reason
- **Technical cancellation** — Either side cancels for a technical reason (code `000`)
- **Driver not found on confirm** — The booking fails at `on_confirm` because no driver is available
- **Driver not found after confirm** — The booking is confirmed, but no driver is found afterwards and the ride is auto-cancelled with a refund
- **Issue and grievance handling** — The passenger raises an issue and it is tracked to resolution with IGM 1.0.0

## Key Concepts

- **Network interoperability** — Any ONDC-enabled provider can serve any buyer app; no single company controls access
- **Fulfilment types** — `fulfillment.type` is `DELIVERY` (driver and vehicle details are shared once assigned) or `SELF_PICKUP` (OTP only, for queue locations)
- **Vehicle categories and variants** — `fulfillment.vehicle.category` is `CAB` or `TWO_WHEELER`; variants are AUTO_RICKSHAW, CAB (SEDAN, SUV, HATCHBACK) and TWO_WHEELER, and `energy_type` describes the fuel or power source
- **Ride states** — `RIDE_CONFIRMED` is shared whenever a ride is confirmed, before `RIDE_ASSIGNED`
  - Delivery: `RIDE_CONFIRMED` → `RIDE_ASSIGNED` → `RIDE_ENROUTE_PICKUP` → `RIDE_ARRIVED_PICKUP` → `RIDE_STARTED` → `RIDE_ENDED`
  - Delivery, cancelled: `RIDE_CONFIRMED` → `RIDE_ASSIGNED` → `RIDE_ENROUTE_PICKUP` (optional) → `RIDE_ARRIVED_PICKUP` (optional) → `RIDE_CANCELLED`
  - Self-pickup: `RIDE_CONFIRMED` → `RIDE_ASSIGNED` → `RIDE_STARTED` → `RIDE_ENDED`
- **Cancellation reason codes** — `000` technical cancellation; rider-side codes `001`–`005` (driver not moving, unable to contact driver, driver asked me to cancel, incorrect pickup location, booked by mistake); driver-side codes `012`–`014` (rider not present, accepted by mistake, unable to contact rider); `011` no drivers available
- **Who collects payment** — Payments are collected either by the buyer app (`BAP`) or the seller app (`BPP`) and are recorded in the `collected_by` field. Payment is made on fulfilment, not as a pre-order
- **Quote and refund** — Cancellation flows include a refund in the quote, and `on_cancel` carries the `cancellation` object, timestamps and stop status
- **Order status** — The order-level status is `COMPLETED` once the ride has finished

## Tags You Will See

Many details travel as tag groups rather than fixed fields. The ones a new joiner meets first:

| Tag group | Used for |
| :-------- | :------- |
| `BUYER_FINDER_FEES` | The buyer-finder fee type and percentage, sent in the `search` payment tags |
| `SETTLEMENT_TERMS` | Settlement terms for the payment between the two apps |
| `FARE_POLICY` | Fare rules such as the minimum fare |
| `INFO` | Additional ride information |
| `ROUTE_INFO` | Route details such as the encoded polyline |

The Attribute-UI in the developer guide lists every field with its owner (BAP or BPP) and whether it is required. Required rules are defined in `validations/index.yaml`.

## Errors

The seller app can return these errors:

| Code | Event |
| :--- | :---- |
| `90201` | Route serviceability error: the pickup and drop locations are not serviceable |
| `90202` | Tracking not enabled for any fulfilment in the order |
| `90203` | Driver not assigned to the order |

## Flows

The developer guide's Flow-UI lists these flows for 2.0.1:

| Flow | What it shows |
| :--- | :------------ |
| BPP Collecting - Payment Confirmation | `init`, `on_init`, form, `status`, `on_status`, `confirm`, `on_confirm` with the seller app collecting the payment |
| On-Demand - Assign driver on on-confirm | Driver assigned in `on_confirm`, followed by tracking and status updates |
| On-Demand - Assign driver post on-confirm | The ride is confirmed first and the driver is assigned afterwards |
| On-Demand - Assign driver post on-confirm (Self-Pickup) | A queue-location ride where only an OTP is shared |
| On-Demand - Female Driver Flow | A booking that requests a female driver |
| On-Demand - Ride cancellation by driver | The driver cancels after being assigned |
| On-Demand - Ride cancellation by rider | The passenger cancels a confirmed ride |
| Driver not found on on_confirm | No driver is available when the booking is confirmed |
| Driver not found post on_confirm | No driver is found after confirmation and the ride is auto-cancelled |

This repository's `config/flows` also holds the IGM 1.0.0, journey updation and technical cancellation flows.

## Where to Find Things

The developer guide has these tabs: Swagger-UI (API definitions), Flow-UI (step-by-step flows), Attribute-UI (every field and tag), Error-UI, TLC-UI (terms), Change-Log-UI and SandBox-UI. In this repository:

- `config/flows` — flow definitions
- `config/attributes` — field and tag descriptions
- `config/validations` — required and conditional rules
- `config/actions` — which call may follow which
- `config/errors` — error codes
- `config/docs` — this overview, the release notes and references

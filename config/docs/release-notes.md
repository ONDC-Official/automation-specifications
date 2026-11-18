# ONDC:TRV10 2.0.1 — Release Notes

Branch: `draft-TRV10-2.0.1` · Version: `TRV10_2.0.1_030924` · Use case: Ride-hailing

## Change Log — On_Demand API specs

Source: `release-TRV10-2.0.1` branch of the ONDC mobility-specification (Change Log tab).

### 3rd September 2024 — `TRV10_2.0.1_030924`

TRV10 Patch Update (2.0.1)

- Added `fulfillment.type` enum `SELF_PICKUP`.
  - This handles the queue use case at designated locations such as an airport or railway station.
  - From a protocol point of view, for such a fulfilment only the OTP is available once the state is `RIDE_CONFIRMED` in `on_confirm`/`on_update`; no agent or vehicle details are shared along with `RIDE_ASSIGNED`.
  - The `START` stop type may carry instructions to reach the pickup point, which the buyer app must display.
- Added `fulfillment.vehicle.category` enums `CAB`, `TWO_WHEELER`.
- Enabled `fulfillment.vehicle.variant` enums:
  - AUTO_RICKSHAW {AUTO_RICKSHAW, EV}
  - CAB {SEDAN, SUV, HATCHBACK, EV}
  - TWO_WHEELER {TWO_WHEELER, EV}
- Added cancellation reason code enums:

  | Code | Reason | Raised by |
  | :--- | :----- | :-------- |
  | 000 | Technical cancellation | BAP/BPP |
  | 011 | No drivers available | BPP |
  | 001 | Driver not moving | BAP |
  | 002 | Unable to contact driver | BAP |
  | 003 | Driver asked me to cancel | BAP |
  | 004 | My pickup location is incorrect | BAP |
  | 005 | Booked by mistake | BAP |
  | 012 | Rider not present at location | BPP |
  | 013 | Accepted by mistake | BPP |
  | 014 | Unable to contact rider | BPP |

- Added `fulfillment.state.descriptor.code` enum `RIDE_CONFIRMED`. The seller app shares it whenever a ride is confirmed, before `RIDE_ASSIGNED`. Order of status updates:
  - `DELIVERY` fulfilment type: RIDE_CONFIRMED → RIDE_ASSIGNED → RIDE_ENROUTE_PICKUP → RIDE_ARRIVED_PICKUP → RIDE_STARTED → RIDE_ENDED
  - `DELIVERY` fulfilment type (cancel flow): RIDE_CONFIRMED → RIDE_ASSIGNED → RIDE_ENROUTE_PICKUP (optional) → RIDE_ARRIVED_PICKUP (optional) → RIDE_CANCELLED
  - `SELF_PICKUP` fulfilment type: RIDE_CONFIRMED → RIDE_ASSIGNED → RIDE_STARTED → RIDE_ENDED
- For cancellation flows, added REFUND as part of the quote.

### 17th September 2024 — `TRV10_2.0.1_170924`

- Added all the tags in attribute-ui.
- Added two new flows:
  - Driver not found on on_confirm
  - Driver not found post on_confirm
- Payment type changed from pre-order to on-fulfilment.

### 9th October 2024 — `TRV10_2.0.1_030924`

- Updated hyphen to underscore in `soft_cancel` and `confirm_cancel`.
- Removed `ev` from vehicle variant.
- Added `energy_type` enums.
- Removed the `order.status` enum from pre-`on_confirm` calls and added it for `on_confirm` and subsequent calls.
- Added `energy_type` in the On-Demand - Assign driver on on-confirm flow examples.

### 28th October 2024

- Updated quote in the `on_cancel` API for the `Driver not found post on_confirm` flow.

### 13th November 2024

- Removed `energy_type` from the search call.
- Added `created_at` & `updated_at` for `on_cancel` calls.
- Added `valid_to` & `status` for `stops` in `on_cancel` calls.

### 7th January 2025

- Added the `cancellation` object as part of the `on_cancel` calls.

### 29th Oct 2025

- Added fulfilment id to the select API.
- Updated attribute-ui for mandatory/optional fields.

### 28th Nov 2025

- Added a new flow for Female Driver with optional customer and agent gender:

  ```json
  "fulfillment": {
    "customer": { "person": { "gender": "FEMALE" } },
    "agent": { "person": { "gender": "FEMALE" } }
  }
  ```

### 16th Dec 2025

- Updated the order-level status from `COMPLETE` to `COMPLETED` in the enums section.

### 6th August 2026

- Updated payment type enum values by replacing hyphens (-) with underscores (_).

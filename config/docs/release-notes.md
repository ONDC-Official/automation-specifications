# ONDC:TRV11 2.0.0 — Release Notes

---

## Metro

### Change Logs: Metro API specs

| Version                         | TRV11_2.0.0_130824 |
| :------------------------------ | :----------------- |
| Updates in API Specs on dev doc | 13th August 2024   |

##### Metro:

- Added `bpp_id` & `bpp_uri` in the `search_2` call.
- Fixed peer-to-peer `search` (2) call.

****21st October 2024****
- Added missing `BUYER_FINDER_FEES` tag group in `on_status` calls.

****16th Dec 2025****
 - Updated the order level status from `COMPLETE` to `COMPLETED`.

****13th April 2026****
  - Added missing `auth` field as part of `on_status` calls.

****14th May 2026****
  - Updated error codes.

****22nd May 2026****
  - Added Partial Cancellation Flow.

****6th August 2026****
  - Updated payment type enum values by replacing hyphens (-) with underscores (_).
      - For example: PRE-ORDER to PRE_ORDER

****3rd November 2026****
  - Added `update` / `on_update` calls to handle refund status updates in the Metro Cancellation Flow.

#####

---

## Bus

### Change Logs: Bus (IntraCity) API specs

| Version                         | TRV11_2.0.0_130824 |
| :------------------------------ | :----------------- |
| Updates in API Specs on dev doc | 13th August 2024   |

##### Bus:

- Added `collected_by` in the `search` call.
- Fixed peer-to-peer `search` (2) call.

****25th February 2025****
  - Updated `cancellation_reason_id` from `0` to `000` for the Technical Cancellation Flow.

****16th Dec 2025****
 - Updated the order level status from `COMPLETE` to `COMPLETED`.

****13th April 2026****
  - Added missing `auth` field as part of `on_status` calls.

# ONDC:TRV13 2.0.1 — Release Notes

## Overview
This document tracks all version releases, feature additions, schema modifications, and protocol updates for the **Hotel Booking domain (`ONDC:TRV13`)** across the ONDC network.

---

## Version History

### Version TRV13_2.0.1_210925 (21st August 2025)

#### Hotel Booking Enhancements & Flow Additions

1. **New Flow Implementations**:
   - **Seller App Pagination Flow**: Introduced multi-page catalog delivery mechanism (`PAGINATION` tag group with `PAGINATION_ID`, `CURRENT_PAGE_NUMBER`, and `MAX_PAGE_NUMBER`) allowing hotel aggregators and large chains to serve multi-property inventory across consecutive asynchronous callbacks without payload truncation.
   - **Purchase Journey**: Standardized end-to-end purchase journey from discovery by city or GPS, room selection with meal plans, guest verification, advance deposit payment, to voucher confirmation.

2. **Cancellation Terms Specification**:
   - Updated `cancellation_terms` schema to include structured `cancel_by.range` (`start` and `end` timestamps) and itemized `cancellation_fee` (supporting both percentage-based and fixed amount deductions).

3. **Inclusion & Exclusion Taxonomy**:
   - Added standardized `INCLUSIONS` and `EXCLUSIONS` tag groups at both **Provider (Hotel Property)** and **Item (Room Accommodation)** levels to provide transparent amenity disclosures (e.g., Free Toiletries, LAN, Lawn, Patio, Swimming Pool, Microwave).

4. **Order Status Standardization**:
   - Updated the terminal order-level lifecycle status descriptor from `COMPLETE` to **`COMPLETED`** to ensure network-wide state machine consistency.

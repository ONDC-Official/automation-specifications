# ONDC:TRV12 2.0.0 — Release Notes

---

## Airline

### Change Logs:  Airlines API specs

| Version                         | TRV12_2.0.0_160724 |
| :------------------------------ | :----------------- |




##### Airlines:

****16th July 2024****

- Added dob, as part of person to accommodate date of birth.
```
    person:
      name: Joe Adams
      age: "30"
      gender: MALE
      dob: "2023-03-23"

```
- Added `created_at` and `updated_at` to the on_confirm call and all subsequent calls.
- In on_cancel, removed refund terms, updated quote with refund & cancellation charges 
    ```
    - title: REFUND
        item:
          id: I1
          quantity:
            selected:
              count: 3
          price:
            currency: INR
            value: "-9280"      
        price:
          currency: INR
          value: "-28640"
    - title: REFUND
        item:
          id: "I2-1"
          add_ons:
            - id: "A1"
        price:
          value: "-300"
          currency: INR          
    - title: CANCELLATION_CHARGES
        price:
          currency: INR
          value:  '1000'          
    ```


****17th December 2024****
- Updated the enum `BASE_PRICE` to `BASE_FARE` in the enums section.

****26th March 2025****
- Updated the `fulfillments.customer.person.name` field to follow the format: `<Title>|<First Name>|<Middle Name>|<Last Name>`.

****3rd July 2025****
 * Added missing id in quote object
 * Added missing payments id in confirm call

****3rd November 2025****
 * Added missing tags in the tags section
 * In OTHER_CHARGES, updated field key from `code: surcharge` to `name: surcharge`.

****11th November 2025****
* Updated select payload for both parent and child item selection in alignment with the current implementation.
* Added missing `parent_item_id` reference in examples.

****18th November 2025****
* Added Buyer and Seller cancellation flows.
* Added standardized cancellation reason codes & Error UI.
* Updated `select` payload to handle item selection using only `parent_item_id`

****16th Dec 2025**** 
 - Updated the order level status from `COMPLETE` to `COMPLETED`. 

****6th August 2026****
  - Updated payment type enum values by replacing hyphens (-) with underscores (_).
      - For example: PRE_ORDER to PRE_ORDER  
#####

---

## Intercity

### Change Logs: Intercity API specs

| Version                         | TRV12_2.0.0_120824 |
| :------------------------------ | :----------------- |
| Updates in API Specs on dev doc | 12th August 2024      |

##### Intercity:

- Added new fulfillments type as TICKET.
- Added separate fulfillment for each ticket quantity.
- Added cancellation flow.
- Moved seat_grid to on_select call.

****22nd October 2024****
- Added `created_At` & `updated_at` for on_cancel calls`
---

****14th November 2024****
- Added `energy_types`, `wheels_count`,`capacity`,`variant` into examples and enums

****17th December 2024****
- Updated the enum `BASE_PRICE` to `BASE_FARE` in the enums section.

****7th May 2025****
- Added multiple SEAT_GRID tag values under fulfillment type TRIP in the initial on_select call.

****27th May 2025****
- Added fulfillments states
  - CONFIRMED
  - IN_PROGRESS
  - COMPLETED
- Added cancellation terms in on_search API examples.
- Added new flow `Error Response(Soft Locking Time)`
- Updated type QR to PNR in authorization object.
- Added Rating API.

****10th June 2025****
  - Added  on_rating API examples
  - Added two new flows
    - Rating(with feedback form)
    - Rating(without feedback form)

****19th June 2025****
  
  * Added the new flows: 
    - Rating (Success)
    - Rating (Error)
    - Partial Cancellation Flow
    - Seller cancellation
  * Added `on_status` API call in order journey for code based flow.
  * Added the `fulfillment_ids` mapping in quote for "seat_fare" line item
  * Added the state in fulfillments where type is TICKET.

****1st July 2025****
  * Removed GPS based flow.
  * Updated order level status `COMPLETE` to `COMPLETED`.
  * Added status/on_status calls to  Station Code Based flow.
  * Added `rateable` & `rating` in fulfillments to on_search(second & third) call

****26th Aug 2025****
  - Added enum values for the `RESTRICTED_GENDER` tag.

****29th Aug 2025****
  - Added new title & tag-group `SELLER_FEES` in quote.breakup.
  - Added `Service_Tax` as an enum for TAX tag-group in quote.breakup.

****3rd November 2025****  
  - Added missing tags in the tags section

****24th November 2025****
- Enabled Error_UI in the developer guide.
- Updated cancellation reason codes in the examples and in the enums section.
- Removed order id from confirm call.

****13th April 2026****
  - Added a new flow `Technical Cancellation Flow`

****30th April 2026****
  - Updated order status from `CANCELLED` to `ACTIVE` in Partial Cancellation flow

****12 May 2026****
  - Added optional fields `name` as part of stops in Search call.

****6th August 2026****
  - Updated payment type enum values by replacing hyphens (-) with underscores (_).
      - For example: PRE-ORDER to PRE_ORDER   

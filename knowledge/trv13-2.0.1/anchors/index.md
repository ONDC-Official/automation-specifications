# Anchors — interned meanings

> Rebuilt from `atoms.md` for `trv13-2.0.1` (structural + Stage E). One row per interned
> meaning; `grounded-in` is the position the meaning was first interned at.

| handle | meaning | grounded-in | asof |
|---|---|---|---|
| anchor.aadhaar | aadhaar | - | trv13-2.0.1 |
| anchor.accommodation-item | accommodation item | trv13-2.0.1:attributes/Hotel_Booking-V2.yaml#attribute_set.on_search.message.catalog.providers.items._description | trv13-2.0.1 |
| anchor.accommodation-transaction | accommodation transaction | - | trv13-2.0.1 |
| anchor.action | action | - | trv13-2.0.1 |
| anchor.add-on-price | add on price | - | trv13-2.0.1 |
| anchor.adults-count | adults count | trv13-2.0.1:attributes/Hotel_Booking-V2.yaml#attribute_set.select.message.order.fulfillments.tags.list.descriptor.code._description | trv13-2.0.1 |
| anchor.adv-deposit-tag | adv deposit tag | trv13-2.0.1:validations/index.yaml#_TESTS_.on_status[ON_STATUS_PAYMENTS]._RETURN_[REQUIRED_PAYMENTS_LINKED_TAGS]._RETURN_[REQUIRED_LINKED_PAYMENT_TAG].enumList | trv13-2.0.1 |
| anchor.area-code | area code | - | trv13-2.0.1 |
| anchor.bap-id | bap id | trv13-2.0.1:attributes/Hotel_Booking-V2.yaml#attribute_set.search.context.bap_id._description | trv13-2.0.1 |
| anchor.bap-terms | bap terms | trv13-2.0.1:validations/index.yaml#_TESTS_.search[SEARCH_INTENT_TAGS]._RETURN_[TAG_BAP_TERMS].validValues | trv13-2.0.1 |
| anchor.bap-uri | bap uri | trv13-2.0.1:attributes/Hotel_Booking-V2.yaml#attribute_set.search.context.bap_uri._description | trv13-2.0.1 |
| anchor.base-deviation | base deviation | - | trv13-2.0.1 |
| anchor.billing | billing | trv13-2.0.1:validations/index.yaml#_TESTS_.init[INIT_ORDER_BILLING]._RETURN_[REQUIRED_BILLING_TAX_ID] | trv13-2.0.1 |
| anchor.billing-organization | billing organization | - | trv13-2.0.1 |
| anchor.billing-state | billing state | trv13-2.0.1:attributes/Hotel_Booking-V2.yaml#attribute_set.init.message.order.billing.state._description | trv13-2.0.1 |
| anchor.binding-offer | binding offer | - | trv13-2.0.1 |
| anchor.booking-commitment | booking commitment | - | trv13-2.0.1 |
| anchor.booking-confirmation-document | booking confirmation document | trv13-2.0.1:flows/Hotel-Booking-V2/Order_to_Confirm_to_Fulfillment__City_Code_.yaml#steps[on_status_city_code].mock.defaultPayload.message.order.documents[0].descriptor.code | trv13-2.0.1 |
| anchor.booking-intent | booking intent | - | trv13-2.0.1 |
| anchor.booking-update | booking update | trv13-2.0.1:docs/overview.md#use-cases | trv13-2.0.1 |
| anchor.bpp-id | bpp id | trv13-2.0.1:attributes/Hotel_Booking-V2.yaml#attribute_set.on_search.context.bpp_id._description | trv13-2.0.1 |
| anchor.bpp-terms | bpp terms | trv13-2.0.1:validations/index.yaml#_TESTS_.on_init[ON_INIT_TAGS]._RETURN_[PAYMENT_TAG_GROUP].validTags | trv13-2.0.1 |
| anchor.breakup-title | breakup title | - | trv13-2.0.1 |
| anchor.buyer-endpoint | buyer endpoint | trv13-2.0.1:specs/openapi.yaml#paths[/search].post.operationId | trv13-2.0.1 |
| anchor.buyer-finder-fees | buyer finder fees | trv13-2.0.1:validations/index.yaml#_TESTS_.search[SEARCH_INTENT_TAGS]._RETURN_[TAG_BUYER_FINDER_FEES].validValues | trv13-2.0.1 |
| anchor.buyer-finder-fees-percentage | buyer finder fees percentage | - | trv13-2.0.1 |
| anchor.buyer-initiated-cancellation | buyer initiated cancellation | trv13-2.0.1:flows/Hotel-Booking-V2/Buyer_Side_Full_Cancellation.yaml#steps[cancel_5].api | trv13-2.0.1 |
| anchor.callback-endpoint | callback endpoint | - | trv13-2.0.1 |
| anchor.cancel | cancel | trv13-2.0.1:actions/index.yaml#supportedActions.cancel | trv13-2.0.1 |
| anchor.cancel-and-rebook | cancel and rebook | - | trv13-2.0.1 |
| anchor.cancel-by-window | cancel by window | trv13-2.0.1:attributes/Hotel_Booking-V2.yaml#attribute_set.on_search.message.catalog.providers.items.cancellation_terms.cancel_by.range.end._description | trv13-2.0.1 |
| anchor.cancellation-descriptor | cancellation descriptor | trv13-2.0.1:attributes/Hotel_Booking-V2.yaml#attribute_set.cancel.message.descriptor._description | trv13-2.0.1 |
| anchor.cancellation-eligible | cancellation eligible | trv13-2.0.1:attributes/Hotel_Booking-V2.yaml#attribute_set.on_search.message.catalog.providers.items.cancellation_terms.cancellation_eligible._description | trv13-2.0.1 |
| anchor.cancellation-fee-percentage | cancellation fee percentage | - | trv13-2.0.1 |
| anchor.cancellation-policy | cancellation policy | trv13-2.0.1:docs/overview.md#key-concepts | trv13-2.0.1 |
| anchor.cancellation-reason-id | cancellation reason id | trv13-2.0.1:validations/index.yaml#_TESTS_.cancel[CANCEL_MESSAGE_1]._RETURN_[VALID_CANCELLATION_REASON_ID].enumList | trv13-2.0.1 |
| anchor.cancellation-terms | cancellation terms | trv13-2.0.1:attributes/Hotel_Booking-V2.yaml#attribute_set.on_search.message.catalog.providers.items.cancellation_terms.cancellation_fee._description | trv13-2.0.1 |
| anchor.cancelled-by | cancelled by | - | trv13-2.0.1 |
| anchor.cancelled-by-consumer | cancelled by consumer | trv13-2.0.1:attributes/Hotel_Booking-V2.yaml#attribute_set.on_cancel.message.order.cancellation.cancelled_by._description | trv13-2.0.1 |
| anchor.cancelled-by-merchant | cancelled by merchant | - | trv13-2.0.1 |
| anchor.catalog-inc | catalog inc | trv13-2.0.1:validations/index.yaml#_TESTS_.search[SEARCH_INTENT_TAGS]._RETURN_[TAG_GROUPS_REQUIRED].validTags | trv13-2.0.1 |
| anchor.catalog-refresh-response | catalog refresh response | trv13-2.0.1:flows/Hotel-Booking-V2/Hotel_Booking__ttl_based__booking.yaml#steps[on_search_7].mock.generate | trv13-2.0.1 |
| anchor.catalog-refresh-search | catalog refresh search | trv13-2.0.1:flows/Hotel-Booking-V2/Hotel_Booking__ttl_based__booking.yaml#steps[search_7].api | trv13-2.0.1 |
| anchor.children-count | children count | - | trv13-2.0.1 |
| anchor.city-code | city code | trv13-2.0.1:attributes/Hotel_Booking-V2.yaml#attribute_set.search.context.location.city._description | trv13-2.0.1 |
| anchor.collected-by | collected by | trv13-2.0.1:attributes/Hotel_Booking-V2.yaml#attribute_set.init.message.order.payments.collected_by._description.enums | trv13-2.0.1 |
| anchor.confirm | confirm | trv13-2.0.1:actions/index.yaml#supportedActions.confirm | trv13-2.0.1 |
| anchor.confirm-cancel | confirm cancel | - | trv13-2.0.1 |
| anchor.confirm-phase-context-required | confirm phase context required | trv13-2.0.1:validations/index.yaml#_TESTS_.on_confirm[ON_CONFIRM_CONTEXT]._RETURN_ | trv13-2.0.1 |
| anchor.confirm-update | confirm update | - | trv13-2.0.1 |
| anchor.context-action | context action | - | trv13-2.0.1 |
| anchor.context-ttl | context ttl | trv13-2.0.1:attributes/Hotel_Booking-V2.yaml#attribute_set.search.context.ttl._description | trv13-2.0.1 |
| anchor.country-code | country code | trv13-2.0.1:attributes/Hotel_Booking-V2.yaml#attribute_set.search.context.location.country._description | trv13-2.0.1 |
| anchor.court-jurisdiction | court jurisdiction | - | trv13-2.0.1 |
| anchor.current-page-number | current page number | trv13-2.0.1:attributes/Hotel_Booking-V2.yaml#attribute_set.on_search.message.catalog.tags.list.value._description | trv13-2.0.1 |
| anchor.customer-contact | customer contact | trv13-2.0.1:validations/index.yaml#_TESTS_.init[INIT_ORDER_FULFILLMENTS]._RETURN_[REQUIRED_CUSTOMER_CONTACT_EMAIL] | trv13-2.0.1 |
| anchor.customer-contact-email | customer contact email | trv13-2.0.1:flows/Hotel-Booking-V2/Order_to_Confirm_to_Fulfillment__Updates_in_Booking_.yaml#steps[update_5].mock.defaultPayload.message.order.fulfillments[0].tags[0].list[0].descriptor.code | trv13-2.0.1 |
| anchor.customer-phone | customer phone | - | trv13-2.0.1 |
| anchor.default-search-ttl | default search ttl | - | trv13-2.0.1 |
| anchor.discovery-phase-context-required | discovery phase context required | trv13-2.0.1:validations/index.yaml#_TESTS_.search[SEARCH_CONTEXT]._RETURN_[CONTEXT_REQUIRED] | trv13-2.0.1 |
| anchor.discovery-scope | discovery scope | - | trv13-2.0.1 |
| anchor.document-code | document code | - | trv13-2.0.1 |
| anchor.document-url | document url | - | trv13-2.0.1 |
| anchor.effective-date | effective date | - | trv13-2.0.1 |
| anchor.enum | enum | - | trv13-2.0.1 |
| anchor.error-code | error code | trv13-2.0.1:errors/index.yaml#code | trv13-2.0.1 |
| anchor.external-terms-ref | external terms ref | trv13-2.0.1:attributes/Hotel_Booking-V2.yaml#attribute_set.on_search.message.catalog.providers.items.cancellation_terms.external_ref._description | trv13-2.0.1 |
| anchor.final-payment-tag | final payment tag | trv13-2.0.1:validations/index.yaml#_TESTS_.on_update[ON_UPDATE_PAYMENTS]._RETURN_[REQUIRED_PAYMENTS_LINKED_TAGS]._RETURN_[REQUIRED_LINKED_PAYMENT_TAG].enumList | trv13-2.0.1 |
| anchor.flow | flow | - | trv13-2.0.1 |
| anchor.flow-buyer-cancellation | flow buyer cancellation | trv13-2.0.1:flows/index.yaml#flows[Buyer Side Full Cancellation] | trv13-2.0.1 |
| anchor.flow-city-code | flow city code | trv13-2.0.1:flows/index.yaml#flows[Order to Confirm to Fulfillment (City Code)] | trv13-2.0.1 |
| anchor.flow-city-code-igm | flow city code igm | trv13-2.0.1:flows/index.yaml#flows[Order_to_Confirm_to_Fulfillment_City_Code_with_igm_1.0.0] | trv13-2.0.1 |
| anchor.flow-merchant-cancellation | flow merchant cancellation | trv13-2.0.1:flows/index.yaml#flows[Merchant Side Full Cancellation] | trv13-2.0.1 |
| anchor.flow-seller-pagination | flow seller pagination | trv13-2.0.1:flows/index.yaml#flows[Hotel Booking Seller App Pagination Flow] | trv13-2.0.1 |
| anchor.flow-ttl-booking | flow ttl booking | trv13-2.0.1:flows/index.yaml#flows[Hotel Booking (ttl based) booking] | trv13-2.0.1 |
| anchor.flow-updates-in-booking | flow updates in booking | trv13-2.0.1:flows/index.yaml#flows[Order to Confirm to Fulfillment (Updates in Booking)] | trv13-2.0.1 |
| anchor.fulfillment-id | fulfillment id | trv13-2.0.1:attributes/Hotel_Booking-V2.yaml#attribute_set.update.message.order.fulfillments.id._description | trv13-2.0.1 |
| anchor.fulfillment-stop | fulfillment stop | trv13-2.0.1:attributes/Hotel_Booking-V2.yaml#attribute_set.search.message.intent.fulfillment.stops.location.gps._description | trv13-2.0.1 |
| anchor.fulfillment-tag-group | fulfillment tag group | - | trv13-2.0.1 |
| anchor.fulfillment-tracking | fulfillment tracking | trv13-2.0.1:flows/Hotel-Booking-V2/Order_to_Confirm_to_Fulfillment__City_Code_.yaml#steps[status_5] | trv13-2.0.1 |
| anchor.gps | gps | - | trv13-2.0.1 |
| anchor.gps-located-point | gps located point | - | trv13-2.0.1 |
| anchor.guest-age | guest age | - | trv13-2.0.1 |
| anchor.guest-credential | guest credential | trv13-2.0.1:flows/Hotel-Booking-V2/Order_to_Confirm_to_Fulfillment__City_Code_.yaml#steps[confirm_5].mock.defaultPayload.message.order.fulfillments[0].customer.person.creds[0].type | trv13-2.0.1 |
| anchor.guest-dob | guest dob | - | trv13-2.0.1 |
| anchor.guest-gender | guest gender | - | trv13-2.0.1 |
| anchor.guest-identity | guest identity | trv13-2.0.1:validations/index.yaml#_TESTS_.init[INIT_ORDER_FULFILLMENTS]._RETURN_[REQUIRED_CUSTOMER_AGE] | trv13-2.0.1 |
| anchor.guests-tag | guests tag | trv13-2.0.1:attributes/Hotel_Booking-V2.yaml#attribute_set.select.message.order.fulfillments.tags.descriptor.code._description | trv13-2.0.1 |
| anchor.hotel-booking | hotel booking | trv13-2.0.1:docs/overview.md#key-concepts | trv13-2.0.1 |
| anchor.hotel-booking-v2 | hotel booking v2 | trv13-2.0.1:index.yaml#info.x-usecases | trv13-2.0.1 |
| anchor.hotel-catalog | hotel catalog | trv13-2.0.1:attributes/Hotel_Booking-V2.yaml#attribute_set.on_search.message.catalog._description | trv13-2.0.1 |
| anchor.hotel-category | hotel category | trv13-2.0.1:validations/index.yaml#_TESTS_.search[SEARCH_INTENT]._RETURN_[VALID_ENUM_CATEGORY_CODE] | trv13-2.0.1 |
| anchor.hotel-property-location | hotel property location | trv13-2.0.1:attributes/Hotel_Booking-V2.yaml#attribute_set.on_search.message.catalog.providers.locations.descriptor.code._description | trv13-2.0.1 |
| anchor.hotel-provider | hotel provider | trv13-2.0.1:validations/index.yaml#_TESTS_.on_search[PROVIDERS_REQUIRED]._RETURN_[REQUIRED_PROVIDER_ID] | trv13-2.0.1 |
| anchor.igm | igm | - | trv13-2.0.1 |
| anchor.igm-context-required | igm context required | trv13-2.0.1:validations/index.yaml#_TESTS_.issue[REQUIRED_CONTEXT_FIELDS] | trv13-2.0.1 |
| anchor.igm-v1 | igm v1 | trv13-2.0.1:validations/index.yaml#_TESTS_.issue[ISSUE_VALIDATION_VERSION_100] | trv13-2.0.1 |
| anchor.igm-v2 | igm v2 | trv13-2.0.1:validations/index.yaml#_TESTS_.issue[ISSUE_VALIDATION_VERSION_200]._RETURN_[REQUIRED_MESSAGE_ID_10] | trv13-2.0.1 |
| anchor.inclusions-exclusions | inclusions exclusions | - | trv13-2.0.1 |
| anchor.incremental-catalog-refresh | incremental catalog refresh | trv13-2.0.1:flows/index.yaml#flows[Hotel Booking (ttl based) booking].description | trv13-2.0.1 |
| anchor.india-only-network | india only network | - | trv13-2.0.1 |
| anchor.init | init | trv13-2.0.1:actions/index.yaml#supportedActions.init | trv13-2.0.1 |
| anchor.inventory-freshness | inventory freshness | - | trv13-2.0.1 |
| anchor.invoice-document | invoice document | trv13-2.0.1:flows/Hotel-Booking-V2/Order_to_Confirm_to_Fulfillment__City_Code_.yaml#steps[on_status_city_code].mock.defaultPayload.message.order.documents[1].descriptor.code | trv13-2.0.1 |
| anchor.issue | issue | trv13-2.0.1:actions/index.yaml#supportedActions.issue | trv13-2.0.1 |
| anchor.issue-actors | issue actors | - | trv13-2.0.1 |
| anchor.issue-close | issue close | trv13-2.0.1:flows/Hotel-Booking-V2/Order_to_Confirm_to_Fulfillment_City_Code_with_igm_1.0.0.yaml#steps[issue_close_100].mock.generate | trv13-2.0.1 |
| anchor.issue-complainant-info | issue complainant info | - | trv13-2.0.1 |
| anchor.issue-level | issue level | - | trv13-2.0.1 |
| anchor.issue-open | issue open | trv13-2.0.1:flows/Hotel-Booking-V2/Order_to_Confirm_to_Fulfillment_City_Code_with_igm_1.0.0.yaml#steps[issue_open_100].mock.generate | trv13-2.0.1 |
| anchor.issue-order-details | issue order details | - | trv13-2.0.1 |
| anchor.issue-refs | issue refs | - | trv13-2.0.1 |
| anchor.issue-resolution | issue resolution | trv13-2.0.1:validations/index.yaml#_TESTS_.on_issue_status[ISSUE_ON_ISSUE_STATUS_VALIDATION]._RETURN_[REQUIRED_RESOLUTION_ACTION_TRIGGERED] | trv13-2.0.1 |
| anchor.item-add-on | item add on | trv13-2.0.1:attributes/Hotel_Booking-V2.yaml#attribute_set.on_search.message.catalog.providers.items.add_ons.price._description | trv13-2.0.1 |
| anchor.item-amenity-tag | item amenity tag | - | trv13-2.0.1 |
| anchor.item-availability-window | item availability window | trv13-2.0.1:flows/Hotel-Booking-V2/Hotel_Booking__ttl_based__booking.yaml#steps[on_search_6].mock.generate | trv13-2.0.1 |
| anchor.item-id | item id | - | trv13-2.0.1 |
| anchor.item-price | item price | trv13-2.0.1:validations/index.yaml#_TESTS_.on_search[PROVIDER_ITEMS]._RETURN_[REQUIRED_ITEM_PRICE_MAX_VALUE] | trv13-2.0.1 |
| anchor.large-inventory | large inventory | - | trv13-2.0.1 |
| anchor.liability-allocation | liability allocation | - | trv13-2.0.1 |
| anchor.linked-payments-tag | linked payments tag | trv13-2.0.1:flows/Hotel-Booking-V2/Order_to_Confirm_to_Fulfillment__City_Code_.yaml#steps[confirm_5].mock.defaultPayload.message.order.payments[0].tags[0].descriptor.code | trv13-2.0.1 |
| anchor.location-id | location id | - | trv13-2.0.1 |
| anchor.long-validity-ttl | long validity ttl | trv13-2.0.1:flows/Hotel-Booking-V2/Hotel_Booking__ttl_based__booking.yaml#steps[search_6].mock.defaultPayload.context.ttl | trv13-2.0.1 |
| anchor.mandatory-arbitration | mandatory arbitration | - | trv13-2.0.1 |
| anchor.mandatory-flow | mandatory flow | - | trv13-2.0.1 |
| anchor.max-bookable-count | max bookable count | - | trv13-2.0.1 |
| anchor.max-liability | max liability | - | trv13-2.0.1 |
| anchor.max-page-number | max page number | - | trv13-2.0.1 |
| anchor.maximum-price | maximum price | - | trv13-2.0.1 |
| anchor.meal-plan | meal plan | - | trv13-2.0.1 |
| anchor.merchant-initiated-cancellation | merchant initiated cancellation | trv13-2.0.1:flows/Hotel-Booking-V2/Merchant_Side_Full_Cancellation.yaml#steps[on_cancel_unsolicited].description | trv13-2.0.1 |
| anchor.message-id | message id | trv13-2.0.1:attributes/Hotel_Booking-V2.yaml#attribute_set.search.context.message_id._description | trv13-2.0.1 |
| anchor.message-validity | message validity | - | trv13-2.0.1 |
| anchor.occupancy | occupancy | - | trv13-2.0.1 |
| anchor.on-cancel | on cancel | trv13-2.0.1:actions/index.yaml#supportedActions.on_cancel | trv13-2.0.1 |
| anchor.on-confirm | on confirm | trv13-2.0.1:actions/index.yaml#supportedActions.on_confirm | trv13-2.0.1 |
| anchor.on-fulfillment-payment | on fulfillment payment | trv13-2.0.1:attributes/Hotel_Booking-V2.yaml#attribute_set.on_search.message.catalog.providers.payments.type._description.enums | trv13-2.0.1 |
| anchor.on-init | on init | trv13-2.0.1:actions/index.yaml#supportedActions.on_init | trv13-2.0.1 |
| anchor.on-issue | on issue | trv13-2.0.1:actions/index.yaml#supportedActions.on_issue | trv13-2.0.1 |
| anchor.on-issue-status | on issue status | trv13-2.0.1:actions/index.yaml#supportedActions.on_issue_status | trv13-2.0.1 |
| anchor.on-search | on search | trv13-2.0.1:actions/index.yaml#supportedActions.on_search | trv13-2.0.1 |
| anchor.on-select | on select | trv13-2.0.1:actions/index.yaml#supportedActions.on_select | trv13-2.0.1 |
| anchor.on-status | on status | trv13-2.0.1:actions/index.yaml#supportedActions.on_status | trv13-2.0.1 |
| anchor.on-track | on track | trv13-2.0.1:actions/index.yaml#supportedActions.on_track | trv13-2.0.1 |
| anchor.on-update | on update | trv13-2.0.1:actions/index.yaml#supportedActions.on_update | trv13-2.0.1 |
| anchor.ondc-domain | ondc domain | - | trv13-2.0.1 |
| anchor.optional-flow | optional flow | - | trv13-2.0.1 |
| anchor.order | order | - | trv13-2.0.1 |
| anchor.order-active | order active | trv13-2.0.1:validations/index.yaml#_TESTS_.on_confirm[ON_CONFIRM_ORDER]._RETURN_[VALID_ENUM_ON_CONFIRM_ORDER]._RETURN_[VALID_ENUM_ORDER_STATUS].enumList | trv13-2.0.1 |
| anchor.order-cancelled | order cancelled | trv13-2.0.1:attributes/Hotel_Booking-V2.yaml#attribute_set.on_cancel.message.order.status._description | trv13-2.0.1 |
| anchor.order-created-at | order created at | - | trv13-2.0.1 |
| anchor.order-documents | order documents | trv13-2.0.1:validations/index.yaml#_TESTS_.on_status[ON_STATUS_DOCUMENTS]._RETURN_[REQUIRED_DOCUMENTS]._RETURN_[REQUIRED_DOCUMENTS_DESCRIPTOR_CODE] | trv13-2.0.1 |
| anchor.order-fulfillment | order fulfillment | trv13-2.0.1:validations/index.yaml#_TESTS_.init[INIT_ORDER_FULFILLMENTS]._RETURN_[REQUIRED_CUSTOMER_NAME] | trv13-2.0.1 |
| anchor.order-id | order id | trv13-2.0.1:flows/Hotel-Booking-V2/Order_to_Confirm_to_Fulfillment__City_Code_.yaml#steps[on_confirm_5].description | trv13-2.0.1 |
| anchor.order-initialisation | order initialisation | - | trv13-2.0.1 |
| anchor.order-lifecycle | order lifecycle | - | trv13-2.0.1 |
| anchor.order-phase-context-required | order phase context required | trv13-2.0.1:validations/index.yaml#_TESTS_.select[SELECT_CONTEXT]._RETURN_[REQUIRED_CONTEXT_FIELDS]._RETURN_[REQUIRED_CONTEXT_BPP_ID] | trv13-2.0.1 |
| anchor.order-status | order status | trv13-2.0.1:attributes/Hotel_Booking-V2.yaml#attribute_set.on_status.message.order.status._description.enums | trv13-2.0.1 |
| anchor.order-terms | order terms | trv13-2.0.1:docs/overview.md#key-concepts | trv13-2.0.1 |
| anchor.order-updated-at | order updated at | - | trv13-2.0.1 |
| anchor.overbooking | overbooking | - | trv13-2.0.1 |
| anchor.paginated-catalog-delivery | paginated catalog delivery | trv13-2.0.1:docs/overview.md#use-cases | trv13-2.0.1 |
| anchor.pagination-cursor | pagination cursor | - | trv13-2.0.1 |
| anchor.pagination-id | pagination id | trv13-2.0.1:attributes/Hotel_Booking-V2.yaml#attribute_set.on_search.message.catalog.tags.list.descriptor.code._description | trv13-2.0.1 |
| anchor.pagination-tag-group | pagination tag group | trv13-2.0.1:attributes/Hotel_Booking-V2.yaml#attribute_set.on_search.message.catalog.tags._description | trv13-2.0.1 |
| anchor.part-payment | part payment | trv13-2.0.1:validations/index.yaml#_TESTS_.on_init[ON_INIT_PAYMENTS]._RETURN_[VALID_PAYMENT_TYPES].enumList | trv13-2.0.1 |
| anchor.payment-amount | payment amount | - | trv13-2.0.1 |
| anchor.payment-id | payment id | trv13-2.0.1:attributes/Hotel_Booking-V2.yaml#attribute_set.init.message.order.payments.tags.list.descriptor.code._description | trv13-2.0.1 |
| anchor.payment-status | payment status | trv13-2.0.1:validations/index.yaml#_TESTS_.on_init[ON_INIT_PAYMENTS]._RETURN_[VALID_PAYMENT_STATUS].enumList | trv13-2.0.1 |
| anchor.payment-tag-group | payment tag group | - | trv13-2.0.1 |
| anchor.payment-type | payment type | trv13-2.0.1:attributes/Hotel_Booking-V2.yaml#attribute_set.on_search.message.catalog.providers.payments.type._description.enums | trv13-2.0.1 |
| anchor.perishable-inventory | perishable inventory | - | trv13-2.0.1 |
| anchor.post-confirm-context-check | post confirm context check | anchor.confirm-phase-context-required | trv13-2.0.1 |
| anchor.pre-order-payment | pre order payment | trv13-2.0.1:attributes/Hotel_Booking-V2.yaml#attribute_set.on_search.message.catalog.providers.payments.type._description.enums | trv13-2.0.1 |
| anchor.price-consistency | price consistency | - | trv13-2.0.1 |
| anchor.price-validity | price validity | - | trv13-2.0.1 |
| anchor.property-rating | property rating | - | trv13-2.0.1 |
| anchor.property-type-code | property type code | trv13-2.0.1:attributes/Hotel_Booking-V2.yaml#attribute_set.on_search.message.catalog.providers.locations.descriptor.code._description.enums | trv13-2.0.1 |
| anchor.protocol-version | protocol version | trv13-2.0.1:validations/index.yaml#_TESTS_.search[SEARCH_CONTEXT].version | trv13-2.0.1 |
| anchor.provider-amenity-tag | provider amenity tag | trv13-2.0.1:attributes/Hotel_Booking-V2.yaml#attribute_set.on_search.message.catalog.providers.tags.descriptor.code._description | trv13-2.0.1 |
| anchor.provider-filter | provider filter | trv13-2.0.1:attributes/Hotel_Booking-V2.yaml#attribute_set.search.message.intent.provider.id._description | trv13-2.0.1 |
| anchor.provider-id | provider id | - | trv13-2.0.1 |
| anchor.provider-image | provider image | - | trv13-2.0.1 |
| anchor.provider-payment-option | provider payment option | trv13-2.0.1:validations/index.yaml#_TESTS_.on_search[PROVIDER_PAYMENTS]._RETURN_[VALID_PAYMENT_TYPES].enumList | trv13-2.0.1 |
| anchor.quote | quote | trv13-2.0.1:validations/index.yaml#_TESTS_.on_select[ON_SELECT_ORDER_QUOTE]._RETURN_[REQUIRED_QUOTE_BREAKUP] | trv13-2.0.1 |
| anchor.quote-breakup | quote breakup | trv13-2.0.1:attributes/Hotel_Booking-V2.yaml#attribute_set.on_select.message.order.quote.breakup.item.add_ons.price._description | trv13-2.0.1 |
| anchor.quote-total | quote total | trv13-2.0.1:attributes/Hotel_Booking-V2.yaml#attribute_set.on_select.message.order.quote.price.value._description | trv13-2.0.1 |
| anchor.quote-ttl | quote ttl | trv13-2.0.1:attributes/Hotel_Booking-V2.yaml#attribute_set.on_select.message.order.quote.ttl._description | trv13-2.0.1 |
| anchor.recommended-flag | recommended flag | - | trv13-2.0.1 |
| anchor.refund-eligibility | refund eligibility | - | trv13-2.0.1 |
| anchor.remote-document | remote document | - | trv13-2.0.1 |
| anchor.reportable-flow | reportable flow | - | trv13-2.0.1 |
| anchor.request-callback-cycle | request callback cycle | - | trv13-2.0.1 |
| anchor.resolution-provider | resolution provider | - | trv13-2.0.1 |
| anchor.revised-booking-state | revised booking state | - | trv13-2.0.1 |
| anchor.rfc3339-millis-timestamp | rfc3339 millis timestamp | - | trv13-2.0.1 |
| anchor.room-category | room category | - | trv13-2.0.1 |
| anchor.room-inventory | room inventory | trv13-2.0.1:docs/overview.md#key-concepts | trv13-2.0.1 |
| anchor.room-type-code | room type code | trv13-2.0.1:attributes/Hotel_Booking-V2.yaml#attribute_set.on_search.message.catalog.providers.items.descriptor.code._description | trv13-2.0.1 |
| anchor.route-serviceability-error | route serviceability error | trv13-2.0.1:errors/index.yaml#code[90201] | trv13-2.0.1 |
| anchor.runtime-concept | runtime concept | - | trv13-2.0.1 |
| anchor.search | search | trv13-2.0.1:actions/index.yaml#supportedActions.search | trv13-2.0.1 |
| anchor.search-intent | search intent | trv13-2.0.1:attributes/Hotel_Booking-V2.yaml#attribute_set.search.message.intent._description | trv13-2.0.1 |
| anchor.search-intent-category | search intent category | - | trv13-2.0.1 |
| anchor.search-intent-tag-group | search intent tag group | - | trv13-2.0.1 |
| anchor.search-intent-tags | search intent tags | trv13-2.0.1:validations/index.yaml#_TESTS_.search[SEARCH_INTENT_TAGS]._RETURN_[TAG_GROUPS_REQUIRED].validTags | trv13-2.0.1 |
| anchor.select | select | trv13-2.0.1:actions/index.yaml#supportedActions.select | trv13-2.0.1 |
| anchor.selected-quantity | selected quantity | trv13-2.0.1:attributes/Hotel_Booking-V2.yaml#attribute_set.select.message.order.items.quantity.selected.count._description | trv13-2.0.1 |
| anchor.seller-endpoint | seller endpoint | trv13-2.0.1:specs/openapi.yaml#paths[/on_search].post.operationId | trv13-2.0.1 |
| anchor.settlement-direction | settlement direction | - | trv13-2.0.1 |
| anchor.single-listing-multi-buyer-reach | single listing multi buyer reach | - | trv13-2.0.1 |
| anchor.soft-cancel | soft cancel | trv13-2.0.1:attributes/Hotel_Booking-V2.yaml#attribute_set.on_status.message.order.status._description.enums | trv13-2.0.1 |
| anchor.soft-update | soft update | trv13-2.0.1:attributes/Hotel_Booking-V2.yaml#attribute_set.on_status.message.order.status._description.enums | trv13-2.0.1 |
| anchor.split-settlement | split settlement | trv13-2.0.1:flows/Hotel-Booking-V2/Order_to_Confirm_to_Fulfillment__Updates_in_Booking_.yaml#steps[on_update_5].mock.generate | trv13-2.0.1 |
| anchor.star-rating | star rating | - | trv13-2.0.1 |
| anchor.state-level-tax | state level tax | - | trv13-2.0.1 |
| anchor.static-terms | static terms | - | trv13-2.0.1 |
| anchor.status | status | trv13-2.0.1:actions/index.yaml#supportedActions.status | trv13-2.0.1 |
| anchor.status-phase-context-required | status phase context required | trv13-2.0.1:validations/index.yaml#_TESTS_.on_status[ON_STATUS_CONTEXT]._RETURN_ | trv13-2.0.1 |
| anchor.stay-date-range | stay date range | trv13-2.0.1:attributes/Hotel_Booking-V2.yaml#attribute_set.select.message.order.provider.time._description | trv13-2.0.1 |
| anchor.std-code-pattern | std code pattern | - | trv13-2.0.1 |
| anchor.stop-end | stop end | trv13-2.0.1:attributes/Hotel_Booking-V2.yaml#attribute_set.search.message.intent.fulfillment.stops.type._description.enums | trv13-2.0.1 |
| anchor.stop-type | stop type | trv13-2.0.1:attributes/Hotel_Booking-V2.yaml#attribute_set.search.message.intent.fulfillment.stops.type._description.enums | trv13-2.0.1 |
| anchor.sub-tag-code | sub tag code | - | trv13-2.0.1 |
| anchor.subscriber-id | subscriber id | - | trv13-2.0.1 |
| anchor.tag-display-flag | tag display flag | - | trv13-2.0.1 |
| anchor.tag-group | tag group | - | trv13-2.0.1 |
| anchor.tag-list | tag list | - | trv13-2.0.1 |
| anchor.tax-id | tax id | - | trv13-2.0.1 |
| anchor.tax-number | tax number | - | trv13-2.0.1 |
| anchor.track | track | trv13-2.0.1:actions/index.yaml#supportedActions.track | trv13-2.0.1 |
| anchor.tracking-not-enabled-error | tracking not enabled error | trv13-2.0.1:errors/index.yaml#code[90202] | trv13-2.0.1 |
| anchor.transaction-context | transaction context | trv13-2.0.1:attributes/Hotel_Booking-V2.yaml#attribute_set.search.context._description | trv13-2.0.1 |
| anchor.transaction-entry | transaction entry | workbench:frames/flow-state-machine.md | trv13-2.0.1 |
| anchor.transaction-id | transaction id | trv13-2.0.1:attributes/Hotel_Booking-V2.yaml#attribute_set.search.context.transaction_id._description | trv13-2.0.1 |
| anchor.transaction-session | transaction session | - | trv13-2.0.1 |
| anchor.trv13 | trv13 | trv13-2.0.1:index.yaml#info.domain | trv13-2.0.1 |
| anchor.unserviceable-location | unserviceable location | trv13-2.0.1:errors/index.yaml#code[90201].Description | trv13-2.0.1 |
| anchor.unsolicited-on-cancel | unsolicited on cancel | trv13-2.0.1:flows/Hotel-Booking-V2/Merchant_Side_Full_Cancellation.yaml#steps[on_cancel_unsolicited].api | trv13-2.0.1 |
| anchor.unsolicited-on-search | unsolicited on search | trv13-2.0.1:flows/Hotel-Booking-V2/Hotel_Booking_Seller_App_Pagination_Flow.yaml#steps[on_search_2].api | trv13-2.0.1 |
| anchor.unsolicited-on-status | unsolicited on status | trv13-2.0.1:flows/Hotel-Booking-V2/Order_to_Confirm_to_Fulfillment__City_Code_.yaml#steps[on_status_unsoliciated].api | trv13-2.0.1 |
| anchor.updatable-field | updatable field | - | trv13-2.0.1 |
| anchor.update | update | trv13-2.0.1:actions/index.yaml#supportedActions.update | trv13-2.0.1 |
| anchor.update-phase-context-required | update phase context required | trv13-2.0.1:validations/index.yaml#_TESTS_.on_update[ON_UPDATE_CONTEXT]._RETURN_ | trv13-2.0.1 |
| anchor.update-request-tag | update request tag | trv13-2.0.1:attributes/Hotel_Booking-V2.yaml#attribute_set.update.message.order.fulfillments.tags.descriptor.code._description | trv13-2.0.1 |
| anchor.update-target | update target | trv13-2.0.1:validations/index.yaml#_TESTS_.update[UPDATE_MESSAGE_1]._RETURN_[VALID_UPDATE_TARGET].enumList | trv13-2.0.1 |
| anchor.update-target-fulfillment | update target fulfillment | trv13-2.0.1:flows/Hotel-Booking-V2/Order_to_Confirm_to_Fulfillment__Updates_in_Booking_.yaml#steps[update_5].mock.defaultPayload.message.update_target | trv13-2.0.1 |
| anchor.validation-anchor | validation anchor | - | trv13-2.0.1 |

# trv13-2.0.1 candidate units (Stage E)

anchor.trv13 | isa | anchor.ondc-domain | basis:declared | asof:trv13-2.0.1 | grounded-in:trv13-2.0.1:index.yaml#info.domain
anchor.hotel-booking-v2 | part-of | anchor.trv13 | basis:declared | asof:trv13-2.0.1 | grounded-in:trv13-2.0.1:index.yaml#info.x-usecases
anchor.trv13 | constrains | anchor.hotel-booking | basis:authority | asof:trv13-2.0.1 | grounded-in:trv13-2.0.1:docs/overview.md#sector--purpose
anchor.hotel-booking | isa | anchor.accommodation-transaction | basis:authority | asof:trv13-2.0.1 | grounded-in:trv13-2.0.1:docs/overview.md#key-concepts
anchor.hotel-booking | requires | anchor.stay-date-range | basis:authority | asof:trv13-2.0.1 | grounded-in:trv13-2.0.1:docs/overview.md#key-concepts
anchor.trv13 | causes | anchor.single-listing-multi-buyer-reach | basis:authority | asof:trv13-2.0.1 | grounded-in:trv13-2.0.1:docs/overview.md#sector--purpose
anchor.room-inventory | isa | anchor.perishable-inventory | basis:authority | asof:trv13-2.0.1 | grounded-in:trv13-2.0.1:docs/overview.md#key-concepts
anchor.cancellation-policy | constrains | anchor.refund-eligibility | basis:authority | asof:trv13-2.0.1 | grounded-in:trv13-2.0.1:docs/overview.md#key-concepts
anchor.booking-update | disjoint-with | anchor.cancel-and-rebook | basis:authority | asof:trv13-2.0.1 | grounded-in:trv13-2.0.1:docs/overview.md#use-cases
anchor.trv13 | not-has-slot | "release-notes" | basis:declared | asof:trv13-2.0.1 | grounded-in:trv13-2.0.1:docs/release-notes.md#ondctrv13-201--release-notes
anchor.trv13 | not-has-slot | "external-references" | basis:declared | asof:trv13-2.0.1 | grounded-in:trv13-2.0.1:docs/references.md#ondctrv13-201--references

anchor.search | scoped-to | anchor.trv13 | basis:declared | asof:trv13-2.0.1 | grounded-in:trv13-2.0.1:validations/index.yaml#_TESTS_.search[SEARCH_CONTEXT].domain
anchor.hotel-category | isa | anchor.search-intent-category | basis:declared | asof:trv13-2.0.1 | grounded-in:trv13-2.0.1:validations/index.yaml#_TESTS_.search[SEARCH_INTENT]._RETURN_[VALID_ENUM_CATEGORY_CODE]
anchor.search | requires | anchor.hotel-category | basis:declared | asof:trv13-2.0.1 | grounded-in:trv13-2.0.1:validations/index.yaml#_TESTS_.search[SEARCH_INTENT]._RETURN_[REQUIRED_CATEGORY_CODE]
anchor.on-search | requires | anchor.hotel-catalog | basis:declared | asof:trv13-2.0.1 | grounded-in:trv13-2.0.1:validations/index.yaml#_TESTS_.on_search[ON_SEARCH_CONTEXT]._RETURN_[REQUIRED_CATALOG_CODE]
anchor.confirm | precedes | anchor.status | basis:declared | asof:trv13-2.0.1 | grounded-in:trv13-2.0.1:actions/index.yaml#supportedActions.confirm
anchor.on-confirm | precedes | anchor.update | basis:declared | asof:trv13-2.0.1 | grounded-in:trv13-2.0.1:actions/index.yaml#supportedActions.on_confirm
anchor.on-confirm | precedes | anchor.cancel | basis:declared | asof:trv13-2.0.1 | grounded-in:trv13-2.0.1:actions/index.yaml#supportedActions.on_confirm
anchor.on-status | precedes | anchor.track | basis:declared | asof:trv13-2.0.1 | grounded-in:trv13-2.0.1:actions/index.yaml#supportedActions.on_status
anchor.on-init | precedes | anchor.init | basis:declared | asof:trv13-2.0.1 | grounded-in:trv13-2.0.1:actions/index.yaml#supportedActions.on_init
anchor.on-search | precedes | anchor.on-search | basis:declared | asof:trv13-2.0.1 | grounded-in:trv13-2.0.1:actions/index.yaml#supportedActions.on_search
anchor.on-select | requires | anchor.select | basis:declared | asof:trv13-2.0.1 | grounded-in:trv13-2.0.1:actions/index.yaml#apiProperties.on_select.async_predecessor
anchor.on-init | requires | anchor.init | basis:declared | asof:trv13-2.0.1 | grounded-in:trv13-2.0.1:actions/index.yaml#apiProperties.on_init.async_predecessor
anchor.on-confirm | requires | anchor.confirm | basis:declared | asof:trv13-2.0.1 | grounded-in:trv13-2.0.1:actions/index.yaml#apiProperties.on_confirm.async_predecessor
anchor.on-search | not-requires | anchor.search | basis:declared | asof:trv13-2.0.1 | grounded-in:trv13-2.0.1:actions/index.yaml#apiProperties.on_search.async_predecessor
anchor.on-cancel | not-requires | anchor.cancel | basis:declared | asof:trv13-2.0.1 | grounded-in:trv13-2.0.1:actions/index.yaml#apiProperties.on_cancel.async_predecessor
anchor.on-status | not-requires | anchor.status | basis:declared | asof:trv13-2.0.1 | grounded-in:trv13-2.0.1:actions/index.yaml#apiProperties.on_status.async_predecessor
anchor.on-update | not-requires | anchor.update | basis:declared | asof:trv13-2.0.1 | grounded-in:trv13-2.0.1:actions/index.yaml#apiProperties.on_update.async_predecessor
anchor.confirm | requires | anchor.on-init | basis:declared | asof:trv13-2.0.1 | grounded-in:trv13-2.0.1:actions/index.yaml#apiProperties.confirm.transaction_partner
anchor.cancel | requires | anchor.on-confirm | basis:declared | asof:trv13-2.0.1 | grounded-in:trv13-2.0.1:actions/index.yaml#apiProperties.cancel.transaction_partner
anchor.update | requires | anchor.on-status | basis:declared | asof:trv13-2.0.1 | grounded-in:trv13-2.0.1:actions/index.yaml#apiProperties.update.transaction_partner
anchor.issue | not-requires | anchor.on-confirm | basis:declared | asof:trv13-2.0.1 | grounded-in:trv13-2.0.1:actions/index.yaml#apiProperties.issue.transaction_partner
anchor.search | not-requires | anchor.on-search | basis:declared | asof:trv13-2.0.1 | grounded-in:trv13-2.0.1:actions/index.yaml#apiProperties.search.transaction_partner

anchor.buyer-endpoint | has-slot | anchor.search | basis:declared | asof:trv13-2.0.1 | grounded-in:trv13-2.0.1:specs/openapi.yaml#paths[/search].post.operationId
anchor.seller-endpoint | has-slot | anchor.on-search | basis:declared | asof:trv13-2.0.1 | grounded-in:trv13-2.0.1:specs/openapi.yaml#paths[/on_search].post.operationId
anchor.trv13 | has-slot | anchor.igm | basis:declared | asof:trv13-2.0.1 | grounded-in:trv13-2.0.1:specs/openapi.yaml#paths[/issue].post.operationId
anchor.seller-endpoint | not-has-slot | anchor.on-track | basis:declared | asof:trv13-2.0.1 | grounded-in:trv13-2.0.1:specs/openapi.yaml#paths
anchor.buyer-endpoint | not-has-slot | anchor.track | basis:declared | asof:trv13-2.0.1 | grounded-in:trv13-2.0.1:specs/openapi.yaml#paths
anchor.trv13 | not-has-slot | "components.schemas" | basis:declared | asof:trv13-2.0.1 | grounded-in:trv13-2.0.1:specs/openapi.yaml#paths

anchor.flow-ttl-booking | isa | anchor.flow | basis:declared | asof:trv13-2.0.1 | grounded-in:trv13-2.0.1:flows/index.yaml#flows[Hotel Booking (ttl based) booking]
anchor.flow-ttl-booking | part-of | anchor.hotel-booking-v2 | basis:declared | asof:trv13-2.0.1 | grounded-in:trv13-2.0.1:flows/index.yaml#flows[Hotel Booking (ttl based) booking].usecase
anchor.flow-ttl-booking | isa | anchor.mandatory-flow | basis:declared | asof:trv13-2.0.1 | grounded-in:trv13-2.0.1:flows/index.yaml#flows[Hotel Booking (ttl based) booking].tags
anchor.flow-ttl-booking | causes | anchor.incremental-catalog-refresh | basis:declared | asof:trv13-2.0.1 | grounded-in:trv13-2.0.1:flows/index.yaml#flows[Hotel Booking (ttl based) booking].description
anchor.incremental-catalog-refresh | constrains | anchor.room-inventory | basis:declared | asof:trv13-2.0.1 | grounded-in:trv13-2.0.1:flows/index.yaml#flows[Hotel Booking (ttl based) booking].description
anchor.flow-ttl-booking | has-slot | anchor.catalog-refresh-search | basis:declared | asof:trv13-2.0.1 | grounded-in:trv13-2.0.1:flows/Hotel-Booking-V2/Hotel_Booking__ttl_based__booking.yaml#steps[search_7]
anchor.catalog-refresh-search | isa | anchor.search | basis:declared | asof:trv13-2.0.1 | grounded-in:trv13-2.0.1:flows/Hotel-Booking-V2/Hotel_Booking__ttl_based__booking.yaml#steps[search_7].api
anchor.catalog-refresh-search | requires | anchor.context-ttl | basis:declared | asof:trv13-2.0.1 | grounded-in:trv13-2.0.1:flows/Hotel-Booking-V2/Hotel_Booking__ttl_based__booking.yaml#steps[search_7].mock.defaultPayload.context.ttl
anchor.catalog-refresh-search | scoped-to | anchor.long-validity-ttl | basis:declared | asof:trv13-2.0.1 | grounded-in:trv13-2.0.1:flows/Hotel-Booking-V2/Hotel_Booking__ttl_based__booking.yaml#steps[search_7].mock.generate
anchor.long-validity-ttl | disjoint-with | anchor.default-search-ttl | basis:declared | asof:trv13-2.0.1 | grounded-in:trv13-2.0.1:flows/Hotel-Booking-V2/Hotel_Booking__ttl_based__booking.yaml#steps[search_6].mock.defaultPayload.context.ttl
anchor.catalog-refresh-search | requires | anchor.stay-date-range | basis:declared | asof:trv13-2.0.1 | grounded-in:trv13-2.0.1:flows/Hotel-Booking-V2/Hotel_Booking__ttl_based__booking.yaml#steps[search_7].mock.defaultPayload.message.intent.category.time.range
anchor.catalog-refresh-search | requires | anchor.fulfillment-stop | basis:declared | asof:trv13-2.0.1 | grounded-in:trv13-2.0.1:flows/Hotel-Booking-V2/Hotel_Booking__ttl_based__booking.yaml#steps[search_7].mock.defaultPayload.message.intent.fulfillment.stops
anchor.catalog-refresh-search | wasDerivedFrom | anchor.search-intent-tags | basis:declared | asof:trv13-2.0.1 | grounded-in:trv13-2.0.1:flows/Hotel-Booking-V2/Hotel_Booking__ttl_based__booking.yaml#steps[search_6].mock.saveData.search_6_tags
anchor.catalog-refresh-search | wasDerivedFrom | anchor.search-intent-category | basis:declared | asof:trv13-2.0.1 | grounded-in:trv13-2.0.1:flows/Hotel-Booking-V2/Hotel_Booking__ttl_based__booking.yaml#steps[search_6].mock.saveData.search_6_intent_category
anchor.item-availability-window | part-of | anchor.accommodation-item | basis:declared | asof:trv13-2.0.1 | grounded-in:trv13-2.0.1:flows/Hotel-Booking-V2/Hotel_Booking__ttl_based__booking.yaml#steps[on_search_6].mock.generate
anchor.item-availability-window | causes | anchor.inventory-freshness | basis:declared | asof:trv13-2.0.1 | grounded-in:trv13-2.0.1:attributes/Hotel_Booking-V2.yaml#attribute_set.on_search.message.catalog.providers.items.time.range._description
anchor.catalog-refresh-response | wasRevisionOf | anchor.hotel-catalog | basis:declared | asof:trv13-2.0.1 | grounded-in:trv13-2.0.1:flows/Hotel-Booking-V2/Hotel_Booking__ttl_based__booking.yaml#steps[on_search_7].mock.generate
anchor.catalog-refresh-response | wasDerivedFrom | anchor.hotel-catalog | basis:declared | asof:trv13-2.0.1 | grounded-in:trv13-2.0.1:flows/Hotel-Booking-V2/Hotel_Booking__ttl_based__booking.yaml#steps[on_search_6].mock.saveData.on_search_6_catalog
anchor.catalog-refresh-response | isa | anchor.on-search | basis:declared | asof:trv13-2.0.1 | grounded-in:trv13-2.0.1:flows/Hotel-Booking-V2/Hotel_Booking__ttl_based__booking.yaml#steps[on_search_7].api
anchor.catalog-refresh-response | sent-by | "BPP" | basis:declared | asof:trv13-2.0.1 | grounded-in:trv13-2.0.1:flows/Hotel-Booking-V2/Hotel_Booking__ttl_based__booking.yaml#steps[on_search_7].owner
anchor.catalog-refresh-search | sent-by | "BAP" | basis:declared | asof:trv13-2.0.1 | grounded-in:trv13-2.0.1:flows/Hotel-Booking-V2/Hotel_Booking__ttl_based__booking.yaml#steps[search_7].owner
anchor.catalog-refresh-response | requires | anchor.transaction-id | basis:declared | asof:trv13-2.0.1 | grounded-in:trv13-2.0.1:flows/Hotel-Booking-V2/Hotel_Booking__ttl_based__booking.yaml#steps[on_search_7].mock.requirements
anchor.flow-ttl-booking | not-has-slot | anchor.confirm | basis:declared | asof:trv13-2.0.1 | grounded-in:trv13-2.0.1:flows/Hotel-Booking-V2/Hotel_Booking__ttl_based__booking.yaml#steps

anchor.flow-seller-pagination | isa | anchor.flow | basis:declared | asof:trv13-2.0.1 | grounded-in:trv13-2.0.1:flows/index.yaml#flows[Hotel Booking Seller App Pagination Flow]
anchor.flow-seller-pagination | part-of | anchor.hotel-booking-v2 | basis:declared | asof:trv13-2.0.1 | grounded-in:trv13-2.0.1:flows/index.yaml#flows[Hotel Booking Seller App Pagination Flow].usecase
anchor.flow-seller-pagination | causes | anchor.paginated-catalog-delivery | basis:declared | asof:trv13-2.0.1 | grounded-in:trv13-2.0.1:flows/index.yaml#flows[Hotel Booking Seller App Pagination Flow].description
anchor.paginated-catalog-delivery | constrains | anchor.large-inventory | basis:authority | asof:trv13-2.0.1 | grounded-in:trv13-2.0.1:docs/overview.md#use-cases
anchor.pagination-tag-group | part-of | anchor.hotel-catalog | basis:declared | asof:trv13-2.0.1 | grounded-in:trv13-2.0.1:attributes/Hotel_Booking-V2.yaml#attribute_set.on_search.message.catalog.tags._description
anchor.pagination-tag-group | sent-by | "BPP" | basis:declared | asof:trv13-2.0.1 | grounded-in:trv13-2.0.1:attributes/Hotel_Booking-V2.yaml#attribute_set.on_search.message.catalog.tags.descriptor.code._description
anchor.pagination-tag-group | has-slot | anchor.pagination-id | basis:declared | asof:trv13-2.0.1 | grounded-in:trv13-2.0.1:flows/Hotel-Booking-V2/Hotel_Booking_Seller_App_Pagination_Flow.yaml#steps[on_search_1].mock.defaultPayload.message.catalog.tags[0].list[0].descriptor.code
anchor.pagination-tag-group | has-slot | anchor.max-page-number | basis:declared | asof:trv13-2.0.1 | grounded-in:trv13-2.0.1:flows/Hotel-Booking-V2/Hotel_Booking_Seller_App_Pagination_Flow.yaml#steps[on_search_1].mock.defaultPayload.message.catalog.tags[0].list[1].descriptor.code
anchor.pagination-tag-group | has-slot | anchor.current-page-number | basis:declared | asof:trv13-2.0.1 | grounded-in:trv13-2.0.1:flows/Hotel-Booking-V2/Hotel_Booking_Seller_App_Pagination_Flow.yaml#steps[on_search_2].mock.defaultPayload.message.catalog.tags[0].list[1].descriptor.code
anchor.pagination-id | constrains | anchor.paginated-catalog-delivery | basis:declared | asof:trv13-2.0.1 | grounded-in:trv13-2.0.1:attributes/Hotel_Booking-V2.yaml#attribute_set.on_search.message.catalog.tags.list.descriptor.code._description
anchor.current-page-number | isa | anchor.pagination-cursor | basis:declared | asof:trv13-2.0.1 | grounded-in:trv13-2.0.1:attributes/Hotel_Booking-V2.yaml#attribute_set.on_search.message.catalog.tags.list.value._description
anchor.current-page-number | scoped-to | anchor.pagination-tag-group | basis:declared | asof:trv13-2.0.1 | grounded-in:trv13-2.0.1:attributes/Hotel_Booking-V2.yaml#attribute_set.on_search.message.catalog.tags.list.value._description
anchor.unsolicited-on-search | isa | anchor.on-search | basis:declared | asof:trv13-2.0.1 | grounded-in:trv13-2.0.1:flows/Hotel-Booking-V2/Hotel_Booking_Seller_App_Pagination_Flow.yaml#steps[on_search_2].api
anchor.unsolicited-on-search | not-requires | anchor.search | basis:declared | asof:trv13-2.0.1 | grounded-in:trv13-2.0.1:flows/Hotel-Booking-V2/Hotel_Booking_Seller_App_Pagination_Flow.yaml#steps[on_search_2].unsolicited
anchor.unsolicited-on-search | sent-by | "BPP" | basis:declared | asof:trv13-2.0.1 | grounded-in:trv13-2.0.1:flows/Hotel-Booking-V2/Hotel_Booking_Seller_App_Pagination_Flow.yaml#steps[on_search_2].owner
anchor.unsolicited-on-search | part-of | anchor.flow-seller-pagination | basis:declared | asof:trv13-2.0.1 | grounded-in:trv13-2.0.1:flows/Hotel-Booking-V2/Hotel_Booking_Seller_App_Pagination_Flow.yaml#steps[on_search_3].unsolicited
anchor.unsolicited-on-search | causes | anchor.current-page-number | basis:declared | asof:trv13-2.0.1 | grounded-in:trv13-2.0.1:flows/Hotel-Booking-V2/Hotel_Booking_Seller_App_Pagination_Flow.yaml#steps[on_search_3].mock.generate
anchor.unsolicited-on-search | wasDerivedFrom | anchor.hotel-catalog | basis:declared | asof:trv13-2.0.1 | grounded-in:trv13-2.0.1:flows/Hotel-Booking-V2/Hotel_Booking_Seller_App_Pagination_Flow.yaml#steps[on_search_2].mock.saveData.on_search_2_catalog
anchor.paginated-catalog-delivery | requires | anchor.transaction-id | basis:declared | asof:trv13-2.0.1 | grounded-in:trv13-2.0.1:flows/Hotel-Booking-V2/Hotel_Booking_Seller_App_Pagination_Flow.yaml#steps[on_search_4].mock.requirements
anchor.paginated-catalog-delivery | not-requires | anchor.select | basis:declared | asof:trv13-2.0.1 | grounded-in:trv13-2.0.1:flows/Hotel-Booking-V2/Hotel_Booking_Seller_App_Pagination_Flow.yaml#steps
anchor.search | requires | anchor.city-code | basis:declared | asof:trv13-2.0.1 | grounded-in:trv13-2.0.1:flows/Hotel-Booking-V2/Hotel_Booking_Seller_App_Pagination_Flow.yaml#steps[search_1].mock.inputs.jsonSchema.properties.city_code

anchor.flow-city-code | isa | anchor.flow | basis:declared | asof:trv13-2.0.1 | grounded-in:trv13-2.0.1:flows/index.yaml#flows[Order to Confirm to Fulfillment (City Code)]
anchor.flow-city-code | part-of | anchor.hotel-booking-v2 | basis:declared | asof:trv13-2.0.1 | grounded-in:trv13-2.0.1:flows/index.yaml#flows[Order to Confirm to Fulfillment (City Code)].usecase
anchor.flow-city-code | causes | anchor.fulfillment-tracking | basis:declared | asof:trv13-2.0.1 | grounded-in:trv13-2.0.1:flows/index.yaml#flows[Order to Confirm to Fulfillment (City Code)].description
anchor.flow-city-code | scoped-to | anchor.city-code | basis:declared | asof:trv13-2.0.1 | grounded-in:trv13-2.0.1:flows/Hotel-Booking-V2/Order_to_Confirm_to_Fulfillment__City_Code_.yaml#steps[search_6].mock.defaultPayload.context.location.city.code
anchor.city-code | isa | anchor.discovery-scope | basis:declared | asof:trv13-2.0.1 | grounded-in:trv13-2.0.1:attributes/Hotel_Booking-V2.yaml#attribute_set.search.context.location.city._description
anchor.city-code | constrains | anchor.hotel-catalog | basis:declared | asof:trv13-2.0.1 | grounded-in:trv13-2.0.1:attributes/Hotel_Booking-V2.yaml#attribute_set.search.context.location.city._description
anchor.city-code | scoped-to | anchor.transaction-context | basis:declared | asof:trv13-2.0.1 | grounded-in:trv13-2.0.1:attributes/Hotel_Booking-V2.yaml#attribute_set.search.context.location._description
anchor.city-code | sent-by | "BAP" | basis:declared | asof:trv13-2.0.1 | grounded-in:trv13-2.0.1:attributes/Hotel_Booking-V2.yaml#attribute_set.search.context.location.city.code._description
anchor.city-code | constrains | anchor.std-code-pattern | basis:declared | asof:trv13-2.0.1 | grounded-in:trv13-2.0.1:validations/index.yaml#_TESTS_.search[SEARCH_CONTEXT]._RETURN_[CONTEXT_REQUIRED]._RETURN_[REQUIRED_CONTEXT_LOCATION_CITY_CODE].reg
anchor.on-search | requires | anchor.city-code | basis:declared | asof:trv13-2.0.1 | grounded-in:trv13-2.0.1:validations/index.yaml#_TESTS_.on_search[ON_SEARCH_CONTEXT]._RETURN_[CONTEXT_REQUIRED]._RETURN_[REQUIRED_CONTEXT_LOCATION_CITY_CODE]
anchor.country-code | scoped-to | anchor.transaction-context | basis:declared | asof:trv13-2.0.1 | grounded-in:trv13-2.0.1:attributes/Hotel_Booking-V2.yaml#attribute_set.search.context.location.country._description
anchor.country-code | constrains | anchor.india-only-network | basis:declared | asof:trv13-2.0.1 | grounded-in:trv13-2.0.1:validations/index.yaml#_TESTS_.search[SEARCH_CONTEXT]._RETURN_[CONTEXT_ENUM]._RETURN_[VALID_CONTEXT_LOCATION_COUNTRY_CODE].enumList
anchor.flow-city-code | not-requires | anchor.fulfillment-stop | basis:declared | asof:trv13-2.0.1 | grounded-in:trv13-2.0.1:flows/Hotel-Booking-V2/Order_to_Confirm_to_Fulfillment__City_Code_.yaml#steps[search_6].mock.defaultPayload.message.intent
anchor.fulfillment-stop | isa | anchor.gps-located-point | basis:declared | asof:trv13-2.0.1 | grounded-in:trv13-2.0.1:attributes/Hotel_Booking-V2.yaml#attribute_set.search.message.intent.fulfillment.stops.location.gps._description
anchor.fulfillment-stop | has-slot | anchor.area-code | basis:declared | asof:trv13-2.0.1 | grounded-in:trv13-2.0.1:attributes/Hotel_Booking-V2.yaml#attribute_set.search.message.intent.fulfillment.stops.location.area_code._description
anchor.fulfillment-stop | has-slot | anchor.stop-type | basis:declared | asof:trv13-2.0.1 | grounded-in:trv13-2.0.1:attributes/Hotel_Booking-V2.yaml#attribute_set.search.message.intent.fulfillment.stops.type._description
anchor.stop-type | isa | anchor.enum | basis:declared | asof:trv13-2.0.1 | grounded-in:trv13-2.0.1:attributes/Hotel_Booking-V2.yaml#attribute_set.search.message.intent.fulfillment.stops.type._description.enums
anchor.stop-end | isa | anchor.stop-type | basis:declared | asof:trv13-2.0.1 | grounded-in:trv13-2.0.1:attributes/Hotel_Booking-V2.yaml#attribute_set.search.message.intent.fulfillment.stops.type._description.enums
anchor.stop-end | scoped-to | anchor.hotel-property-location | basis:declared | asof:trv13-2.0.1 | grounded-in:trv13-2.0.1:flows/Hotel-Booking-V2/Hotel_Booking__ttl_based__booking.yaml#steps[search_7].mock.generate
anchor.fulfillment-tracking | requires | anchor.status | basis:declared | asof:trv13-2.0.1 | grounded-in:trv13-2.0.1:flows/Hotel-Booking-V2/Order_to_Confirm_to_Fulfillment__City_Code_.yaml#steps[status_5]
anchor.unsolicited-on-status | isa | anchor.on-status | basis:declared | asof:trv13-2.0.1 | grounded-in:trv13-2.0.1:flows/Hotel-Booking-V2/Order_to_Confirm_to_Fulfillment__City_Code_.yaml#steps[on_status_unsoliciated].api
anchor.unsolicited-on-status | not-requires | anchor.status | basis:declared | asof:trv13-2.0.1 | grounded-in:trv13-2.0.1:flows/Hotel-Booking-V2/Order_to_Confirm_to_Fulfillment__City_Code_.yaml#steps[on_status_unsoliciated].unsolicited
anchor.unsolicited-on-status | causes | anchor.fulfillment-tracking | basis:declared | asof:trv13-2.0.1 | grounded-in:trv13-2.0.1:flows/Hotel-Booking-V2/Order_to_Confirm_to_Fulfillment__City_Code_.yaml#steps[on_status_unsoliciated].description
anchor.status | requires | anchor.order-id | basis:declared | asof:trv13-2.0.1 | grounded-in:trv13-2.0.1:flows/Hotel-Booking-V2/Order_to_Confirm_to_Fulfillment__City_Code_.yaml#steps[status_5].mock.requirements
anchor.order-id | wasGeneratedBy | anchor.on-confirm | basis:declared | asof:trv13-2.0.1 | grounded-in:trv13-2.0.1:flows/Hotel-Booking-V2/Order_to_Confirm_to_Fulfillment__City_Code_.yaml#steps[on_confirm_5].description
anchor.on-status | has-slot | anchor.order-documents | basis:declared | asof:trv13-2.0.1 | grounded-in:trv13-2.0.1:validations/index.yaml#_TESTS_.on_status[ON_STATUS_DOCUMENTS]
anchor.order-documents | requires | anchor.document-code | basis:declared | asof:trv13-2.0.1 | grounded-in:trv13-2.0.1:validations/index.yaml#_TESTS_.on_status[ON_STATUS_DOCUMENTS]._RETURN_[REQUIRED_DOCUMENTS]._RETURN_[REQUIRED_DOCUMENTS_DESCRIPTOR_CODE]
anchor.order-documents | requires | anchor.document-url | basis:declared | asof:trv13-2.0.1 | grounded-in:trv13-2.0.1:validations/index.yaml#_TESTS_.on_status[ON_STATUS_DOCUMENTS]._RETURN_[REQUIRED_DOCUMENTS]._RETURN_[REQUIRED_DOCUMENTS_URL]
anchor.booking-confirmation-document | isa | anchor.document-code | basis:declared | asof:trv13-2.0.1 | grounded-in:trv13-2.0.1:flows/Hotel-Booking-V2/Order_to_Confirm_to_Fulfillment__City_Code_.yaml#steps[on_status_city_code].mock.defaultPayload.message.order.documents[0].descriptor.code
anchor.invoice-document | isa | anchor.document-code | basis:declared | asof:trv13-2.0.1 | grounded-in:trv13-2.0.1:flows/Hotel-Booking-V2/Order_to_Confirm_to_Fulfillment__City_Code_.yaml#steps[on_status_city_code].mock.defaultPayload.message.order.documents[1].descriptor.code
anchor.order-documents | sent-by | "BPP" | basis:declared | asof:trv13-2.0.1 | grounded-in:trv13-2.0.1:attributes/Hotel_Booking-V2.yaml#attribute_set.on_status.message.order.documents._description
anchor.order-documents | not-part-of | anchor.on-confirm | basis:declared | asof:trv13-2.0.1 | grounded-in:trv13-2.0.1:flows/Hotel-Booking-V2/Order_to_Confirm_to_Fulfillment__City_Code_.yaml#steps[on_confirm_5].mock.defaultPayload.message.order

anchor.flow-city-code-igm | isa | anchor.flow | basis:declared | asof:trv13-2.0.1 | grounded-in:trv13-2.0.1:flows/index.yaml#flows[Order_to_Confirm_to_Fulfillment_City_Code_with_igm_1.0.0]
anchor.flow-city-code-igm | wasRevisionOf | anchor.flow-city-code | basis:declared | asof:trv13-2.0.1 | grounded-in:trv13-2.0.1:flows/index.yaml#flows[Order_to_Confirm_to_Fulfillment_City_Code_with_igm_1.0.0].description
anchor.flow-city-code-igm | has-slot | anchor.igm | basis:declared | asof:trv13-2.0.1 | grounded-in:trv13-2.0.1:flows/Hotel-Booking-V2/Order_to_Confirm_to_Fulfillment_City_Code_with_igm_1.0.0.yaml#steps[issue_open_100]
anchor.flow-city-code-igm | not-isa | anchor.reportable-flow | basis:declared | asof:trv13-2.0.1 | grounded-in:trv13-2.0.1:flows/index.yaml#flows[Order_to_Confirm_to_Fulfillment_City_Code_with_igm_1.0.0].tags
anchor.on-status | precedes | anchor.issue | basis:declared | asof:trv13-2.0.1 | grounded-in:trv13-2.0.1:flows/Hotel-Booking-V2/Order_to_Confirm_to_Fulfillment_City_Code_with_igm_1.0.0.yaml#steps[issue_open_100]
anchor.issue | precedes | anchor.on-issue | basis:declared | asof:trv13-2.0.1 | grounded-in:trv13-2.0.1:flows/Hotel-Booking-V2/Order_to_Confirm_to_Fulfillment_City_Code_with_igm_1.0.0.yaml#steps[on_issue_processing_100]
anchor.on-issue | precedes | anchor.on-issue-status | basis:declared | asof:trv13-2.0.1 | grounded-in:trv13-2.0.1:flows/Hotel-Booking-V2/Order_to_Confirm_to_Fulfillment_City_Code_with_igm_1.0.0.yaml#steps[on_issue_resolved_100]
anchor.issue-open | isa | anchor.issue | basis:declared | asof:trv13-2.0.1 | grounded-in:trv13-2.0.1:flows/Hotel-Booking-V2/Order_to_Confirm_to_Fulfillment_City_Code_with_igm_1.0.0.yaml#steps[issue_open_100].mock.generate
anchor.issue-close | isa | anchor.issue | basis:declared | asof:trv13-2.0.1 | grounded-in:trv13-2.0.1:flows/Hotel-Booking-V2/Order_to_Confirm_to_Fulfillment_City_Code_with_igm_1.0.0.yaml#steps[issue_close_100].mock.generate
anchor.issue-open | precedes | anchor.issue-close | basis:declared | asof:trv13-2.0.1 | grounded-in:trv13-2.0.1:flows/Hotel-Booking-V2/Order_to_Confirm_to_Fulfillment_City_Code_with_igm_1.0.0.yaml#steps[issue_close_100]
anchor.on-issue-status | sent-by | "BPP" | basis:declared | asof:trv13-2.0.1 | grounded-in:trv13-2.0.1:flows/Hotel-Booking-V2/Order_to_Confirm_to_Fulfillment_City_Code_with_igm_1.0.0.yaml#steps[on_issue_resolved_100].owner
anchor.on-issue-status | not-requires | anchor.issue | basis:declared | asof:trv13-2.0.1 | grounded-in:trv13-2.0.1:flows/Hotel-Booking-V2/Order_to_Confirm_to_Fulfillment_City_Code_with_igm_1.0.0.yaml#steps[on_issue_resolved_100].unsolicited
anchor.igm-v1 | disjoint-with | anchor.igm-v2 | basis:declared | asof:trv13-2.0.1 | grounded-in:trv13-2.0.1:validations/index.yaml#_TESTS_.issue[ISSUE_VALIDATION_VERSION_100]
anchor.igm-v1 | requires | anchor.issue-complainant-info | basis:declared | asof:trv13-2.0.1 | grounded-in:trv13-2.0.1:validations/index.yaml#_TESTS_.issue[ISSUE_VALIDATION_VERSION_100]._RETURN_[ISSUE_VALIDATION_OPEN]._RETURN_[REQUIRED_COMPLAINANT_PERSON_NAME]
anchor.igm-v1 | requires | anchor.issue-order-details | basis:declared | asof:trv13-2.0.1 | grounded-in:trv13-2.0.1:validations/index.yaml#_TESTS_.issue[ISSUE_VALIDATION_VERSION_100]._RETURN_[ISSUE_VALIDATION_OPEN]._RETURN_[REQUIRED_ORDER_ID]
anchor.igm-v2 | requires | anchor.issue-actors | basis:declared | asof:trv13-2.0.1 | grounded-in:trv13-2.0.1:validations/index.yaml#_TESTS_.issue[ISSUE_VALIDATION_VERSION_200]._RETURN_[REQUIRED_MESSAGE_ID_10]
anchor.igm-v2 | requires | anchor.issue-refs | basis:declared | asof:trv13-2.0.1 | grounded-in:trv13-2.0.1:validations/index.yaml#_TESTS_.issue[ISSUE_VALIDATION_VERSION_200]._RETURN_[REQUIRED_MESSAGE_REF_ID]
anchor.igm-v2 | has-slot | anchor.issue-level | basis:declared | asof:trv13-2.0.1 | grounded-in:trv13-2.0.1:validations/index.yaml#_TESTS_.issue[ISSUE_VALIDATION_VERSION_200]._RETURN_[REQUIRED_MESSAGE_LEVEL].enumList
anchor.issue-resolution | part-of | anchor.on-issue-status | basis:declared | asof:trv13-2.0.1 | grounded-in:trv13-2.0.1:validations/index.yaml#_TESTS_.on_issue_status[ISSUE_ON_ISSUE_STATUS_VALIDATION]._RETURN_[REQUIRED_RESOLUTION_ACTION_TRIGGERED]
anchor.issue-resolution | requires | anchor.resolution-provider | basis:declared | asof:trv13-2.0.1 | grounded-in:trv13-2.0.1:validations/index.yaml#_TESTS_.on_issue_status[ISSUE_ON_ISSUE_STATUS_VALIDATION]._RETURN_[REQUIRED_RESOLUTION_PROVIDER_TYPE]

anchor.flow-updates-in-booking | isa | anchor.flow | basis:declared | asof:trv13-2.0.1 | grounded-in:trv13-2.0.1:flows/index.yaml#flows[Order to Confirm to Fulfillment (Updates in Booking)]
anchor.flow-updates-in-booking | isa | anchor.optional-flow | basis:declared | asof:trv13-2.0.1 | grounded-in:trv13-2.0.1:flows/index.yaml#flows[Order to Confirm to Fulfillment (Updates in Booking)].tags
anchor.flow-updates-in-booking | causes | anchor.booking-update | basis:declared | asof:trv13-2.0.1 | grounded-in:trv13-2.0.1:flows/index.yaml#flows[Order to Confirm to Fulfillment (Updates in Booking)].description
anchor.booking-update | requires | anchor.on-confirm | basis:declared | asof:trv13-2.0.1 | grounded-in:trv13-2.0.1:flows/Hotel-Booking-V2/Order_to_Confirm_to_Fulfillment__Updates_in_Booking_.yaml#steps[update_5].mock.requirements
anchor.on-status | precedes | anchor.update | basis:declared | asof:trv13-2.0.1 | grounded-in:trv13-2.0.1:flows/Hotel-Booking-V2/Order_to_Confirm_to_Fulfillment__Updates_in_Booking_.yaml#steps[update_5]
anchor.update | precedes | anchor.on-update | basis:declared | asof:trv13-2.0.1 | grounded-in:trv13-2.0.1:flows/Hotel-Booking-V2/Order_to_Confirm_to_Fulfillment__Updates_in_Booking_.yaml#steps[on_update_5]
anchor.update | sent-by | "BAP" | basis:declared | asof:trv13-2.0.1 | grounded-in:trv13-2.0.1:flows/Hotel-Booking-V2/Order_to_Confirm_to_Fulfillment__Updates_in_Booking_.yaml#steps[update_5].owner
anchor.on-update | sent-by | "BPP" | basis:declared | asof:trv13-2.0.1 | grounded-in:trv13-2.0.1:flows/Hotel-Booking-V2/Order_to_Confirm_to_Fulfillment__Updates_in_Booking_.yaml#steps[on_update_5].owner
anchor.update | requires | anchor.update-target | basis:declared | asof:trv13-2.0.1 | grounded-in:trv13-2.0.1:validations/index.yaml#_TESTS_.update[UPDATE_MESSAGE_1]._RETURN_[REQUIRED_UPDATE_TARGET]
anchor.update-target | isa | anchor.enum | basis:declared | asof:trv13-2.0.1 | grounded-in:trv13-2.0.1:validations/index.yaml#_TESTS_.update[UPDATE_MESSAGE_1]._RETURN_[VALID_UPDATE_TARGET].enumList
anchor.update-target | constrains | anchor.booking-update | basis:declared | asof:trv13-2.0.1 | grounded-in:trv13-2.0.1:attributes/Hotel_Booking-V2.yaml#attribute_set.update.message.update_target._description
anchor.update-target-fulfillment | isa | anchor.update-target | basis:declared | asof:trv13-2.0.1 | grounded-in:trv13-2.0.1:flows/Hotel-Booking-V2/Order_to_Confirm_to_Fulfillment__Updates_in_Booking_.yaml#steps[update_5].mock.defaultPayload.message.update_target
anchor.update | requires | anchor.order-id | basis:declared | asof:trv13-2.0.1 | grounded-in:trv13-2.0.1:validations/index.yaml#_TESTS_.update[UPDATE_MESSAGE_1]._RETURN_[REQUIRED_ORDER_ID]
anchor.update | requires | anchor.fulfillment-id | basis:declared | asof:trv13-2.0.1 | grounded-in:trv13-2.0.1:validations/index.yaml#_TESTS_.update[UPDATE_MESSAGE_1]._RETURN_[REQUIRED_FULFILLMENT_ID]
anchor.fulfillment-id | constrains | anchor.booking-update | basis:declared | asof:trv13-2.0.1 | grounded-in:trv13-2.0.1:attributes/Hotel_Booking-V2.yaml#attribute_set.update.message.order.fulfillments.id._description
anchor.fulfillment-id | wasGeneratedBy | anchor.confirm | basis:declared | asof:trv13-2.0.1 | grounded-in:trv13-2.0.1:flows/Hotel-Booking-V2/Order_to_Confirm_to_Fulfillment__Updates_in_Booking_.yaml#steps[update_5].mock.requirements
anchor.update-request-tag | scoped-to | anchor.order-fulfillment | basis:declared | asof:trv13-2.0.1 | grounded-in:trv13-2.0.1:attributes/Hotel_Booking-V2.yaml#attribute_set.update.message.order.fulfillments.tags.descriptor.code._description
anchor.update-request-tag | isa | anchor.fulfillment-tag-group | basis:declared | asof:trv13-2.0.1 | grounded-in:trv13-2.0.1:validations/index.yaml#_TESTS_.update[UPDATE_MESSAGE_1]._RETURN_[VALID_TAG_DESCRIPTOR_CODE].enumList
anchor.update-request-tag | constrains | anchor.updatable-field | basis:declared | asof:trv13-2.0.1 | grounded-in:trv13-2.0.1:attributes/Hotel_Booking-V2.yaml#attribute_set.update.message.order.fulfillments.tags.list.descriptor.code._description
anchor.customer-contact-email | isa | anchor.updatable-field | basis:declared | asof:trv13-2.0.1 | grounded-in:trv13-2.0.1:flows/Hotel-Booking-V2/Order_to_Confirm_to_Fulfillment__Updates_in_Booking_.yaml#steps[update_5].mock.defaultPayload.message.order.fulfillments[0].tags[0].list[0].descriptor.code
anchor.booking-update | not-causes | anchor.order-id | basis:declared | asof:trv13-2.0.1 | grounded-in:trv13-2.0.1:flows/Hotel-Booking-V2/Order_to_Confirm_to_Fulfillment__Updates_in_Booking_.yaml#steps[on_update_5].mock.defaultPayload.message.order.id
anchor.on-update | causes | anchor.revised-booking-state | basis:declared | asof:trv13-2.0.1 | grounded-in:trv13-2.0.1:flows/Hotel-Booking-V2/Order_to_Confirm_to_Fulfillment__Updates_in_Booking_.yaml#steps[on_update_5].description
anchor.on-update | requires | anchor.order-updated-at | basis:declared | asof:trv13-2.0.1 | grounded-in:trv13-2.0.1:validations/index.yaml#_TESTS_.on_update[ON_UPDATE_ORDER]._RETURN_[REQUIRED_ON_UPDATE_ORDER]._RETURN_[REQUIRED_ORDER_UPDATED_AT]
anchor.on-update | requires | anchor.order-status | basis:declared | asof:trv13-2.0.1 | grounded-in:trv13-2.0.1:validations/index.yaml#_TESTS_.on_update[ON_UPDATE_ORDER]._RETURN_[REQUIRED_ON_UPDATE_ORDER]._RETURN_[REQUIRED_ORDER_STATUS]
anchor.on-update | has-slot | anchor.quote | basis:declared | asof:trv13-2.0.1 | grounded-in:trv13-2.0.1:validations/index.yaml#_TESTS_.on_update[ON_UPDATE_ORDER_QUOTE]
anchor.on-update | has-slot | anchor.order-documents | basis:declared | asof:trv13-2.0.1 | grounded-in:trv13-2.0.1:validations/index.yaml#_TESTS_.on_update[ON_UPDATE_DOCUMENTS]

anchor.flow-buyer-cancellation | isa | anchor.flow | basis:declared | asof:trv13-2.0.1 | grounded-in:trv13-2.0.1:flows/index.yaml#flows[Buyer Side Full Cancellation]
anchor.flow-buyer-cancellation | causes | anchor.buyer-initiated-cancellation | basis:declared | asof:trv13-2.0.1 | grounded-in:trv13-2.0.1:flows/index.yaml#flows[Buyer Side Full Cancellation].description
anchor.buyer-initiated-cancellation | requires | anchor.cancel | basis:declared | asof:trv13-2.0.1 | grounded-in:trv13-2.0.1:flows/Hotel-Booking-V2/Buyer_Side_Full_Cancellation.yaml#steps[cancel_5].api
anchor.cancel | sent-by | "BAP" | basis:declared | asof:trv13-2.0.1 | grounded-in:trv13-2.0.1:flows/Hotel-Booking-V2/Buyer_Side_Full_Cancellation.yaml#steps[cancel_5].owner
anchor.on-cancel | sent-by | "BPP" | basis:declared | asof:trv13-2.0.1 | grounded-in:trv13-2.0.1:flows/Hotel-Booking-V2/Buyer_Side_Full_Cancellation.yaml#steps[on_cancel_5].owner
anchor.buyer-initiated-cancellation | requires | anchor.order-id | basis:declared | asof:trv13-2.0.1 | grounded-in:trv13-2.0.1:flows/Hotel-Booking-V2/Buyer_Side_Full_Cancellation.yaml#steps[cancel_5].mock.requirements
anchor.cancel | requires | anchor.cancellation-reason-id | basis:declared | asof:trv13-2.0.1 | grounded-in:trv13-2.0.1:validations/index.yaml#_TESTS_.cancel[CANCEL_MESSAGE_1]._RETURN_[REQUIRED_CANCELLATION_ID]
anchor.cancellation-reason-id | isa | anchor.enum | basis:declared | asof:trv13-2.0.1 | grounded-in:trv13-2.0.1:validations/index.yaml#_TESTS_.cancel[CANCEL_MESSAGE_1]._RETURN_[VALID_CANCELLATION_REASON_ID].enumList
anchor.cancellation-reason-id | scoped-to | anchor.cancel | basis:declared | asof:trv13-2.0.1 | grounded-in:trv13-2.0.1:attributes/Hotel_Booking-V2.yaml#attribute_set.cancel.message.cancellation_reason_id._description
anchor.cancellation-reason-id | sent-by | "BAP" | basis:declared | asof:trv13-2.0.1 | grounded-in:trv13-2.0.1:attributes/Hotel_Booking-V2.yaml#attribute_set.cancel.message.cancellation_reason_id._description
anchor.cancel | requires | anchor.cancellation-descriptor | basis:declared | asof:trv13-2.0.1 | grounded-in:trv13-2.0.1:validations/index.yaml#_TESTS_.cancel[CANCEL_MESSAGE_1]._RETURN_[REQUIRED_CANCELLATION_SHORT_DESC]
anchor.cancellation-descriptor | scoped-to | anchor.on-cancel | basis:declared | asof:trv13-2.0.1 | grounded-in:trv13-2.0.1:attributes/Hotel_Booking-V2.yaml#attribute_set.cancel.message.descriptor._description
anchor.on-cancel | requires | anchor.cancelled-by | basis:declared | asof:trv13-2.0.1 | grounded-in:trv13-2.0.1:validations/index.yaml#_TESTS_.on_cancel[ON_CANCEL_MESSAGE_1]._RETURN_[REQUIRED_CANCELLED_BY]
anchor.on-cancel | causes | anchor.order-cancelled | basis:declared | asof:trv13-2.0.1 | grounded-in:trv13-2.0.1:validations/index.yaml#_TESTS_.on_cancel[ON_CANCEL_MESSAGE_1]._RETURN_[VALID_ORDER_STATUS].enumList
anchor.order-cancelled | isa | anchor.order-status | basis:declared | asof:trv13-2.0.1 | grounded-in:trv13-2.0.1:attributes/Hotel_Booking-V2.yaml#attribute_set.on_cancel.message.order.status._description
anchor.on-cancel | requires | anchor.order-updated-at | basis:declared | asof:trv13-2.0.1 | grounded-in:trv13-2.0.1:validations/index.yaml#_TESTS_.on_cancel[ON_CANCEL_MESSAGE_1]._RETURN_[REQUIRED_UPDATED_AT]
anchor.on-cancel | requires | anchor.cancellation-reason-id | basis:declared | asof:trv13-2.0.1 | grounded-in:trv13-2.0.1:validations/index.yaml#_TESTS_.on_cancel[ON_CANCEL_MESSAGE_1]._RETURN_[REQUIRED_CANCELLATION_REASON_ID]
anchor.buyer-initiated-cancellation | causes | anchor.cancelled-by-consumer | basis:declared | asof:trv13-2.0.1 | grounded-in:trv13-2.0.1:flows/Hotel-Booking-V2/Buyer_Side_Full_Cancellation.yaml#steps[on_cancel_5].mock.generate
anchor.cancelled-by-consumer | isa | anchor.cancelled-by | basis:declared | asof:trv13-2.0.1 | grounded-in:trv13-2.0.1:attributes/Hotel_Booking-V2.yaml#attribute_set.on_cancel.message.order.cancellation.cancelled_by._description
anchor.on-cancel | wasDerivedFrom | anchor.cancellation-reason-id | basis:declared | asof:trv13-2.0.1 | grounded-in:trv13-2.0.1:flows/Hotel-Booking-V2/Buyer_Side_Full_Cancellation.yaml#steps[on_cancel_5].mock.generate
anchor.status | precedes | anchor.cancel | basis:declared | asof:trv13-2.0.1 | grounded-in:trv13-2.0.1:flows/Hotel-Booking-V2/Buyer_Side_Full_Cancellation.yaml#steps[status_5].description

anchor.flow-merchant-cancellation | isa | anchor.flow | basis:declared | asof:trv13-2.0.1 | grounded-in:trv13-2.0.1:flows/index.yaml#flows[Merchant Side Full Cancellation]
anchor.flow-merchant-cancellation | causes | anchor.merchant-initiated-cancellation | basis:declared | asof:trv13-2.0.1 | grounded-in:trv13-2.0.1:flows/index.yaml#flows[Merchant Side Full Cancellation].description
anchor.merchant-initiated-cancellation | disjoint-with | anchor.buyer-initiated-cancellation | basis:declared | asof:trv13-2.0.1 | grounded-in:trv13-2.0.1:flows/Hotel-Booking-V2/Merchant_Side_Full_Cancellation.yaml#steps[on_cancel_unsolicited].description
anchor.merchant-initiated-cancellation | not-requires | anchor.cancel | basis:declared | asof:trv13-2.0.1 | grounded-in:trv13-2.0.1:flows/Hotel-Booking-V2/Merchant_Side_Full_Cancellation.yaml#steps[on_cancel_unsolicited].unsolicited
anchor.unsolicited-on-cancel | isa | anchor.on-cancel | basis:declared | asof:trv13-2.0.1 | grounded-in:trv13-2.0.1:flows/Hotel-Booking-V2/Merchant_Side_Full_Cancellation.yaml#steps[on_cancel_unsolicited].api
anchor.unsolicited-on-cancel | sent-by | "BPP" | basis:declared | asof:trv13-2.0.1 | grounded-in:trv13-2.0.1:flows/Hotel-Booking-V2/Merchant_Side_Full_Cancellation.yaml#steps[on_cancel_unsolicited].owner
anchor.unsolicited-on-cancel | causes | anchor.order-cancelled | basis:declared | asof:trv13-2.0.1 | grounded-in:trv13-2.0.1:flows/Hotel-Booking-V2/Merchant_Side_Full_Cancellation.yaml#steps[on_cancel_unsolicited].mock.generate
anchor.unsolicited-on-cancel | requires | anchor.order-id | basis:declared | asof:trv13-2.0.1 | grounded-in:trv13-2.0.1:flows/Hotel-Booking-V2/Merchant_Side_Full_Cancellation.yaml#steps[on_cancel_unsolicited].mock.requirements
anchor.on-status | precedes | anchor.on-cancel | basis:declared | asof:trv13-2.0.1 | grounded-in:trv13-2.0.1:flows/Hotel-Booking-V2/Merchant_Side_Full_Cancellation.yaml#steps[on_cancel_unsolicited]
anchor.unsolicited-on-cancel | not-causes | anchor.cancelled-by-merchant | basis:declared | asof:trv13-2.0.1 | grounded-in:trv13-2.0.1:flows/Hotel-Booking-V2/Merchant_Side_Full_Cancellation.yaml#steps[on_cancel_unsolicited].mock.generate
anchor.merchant-initiated-cancellation | wasInformedBy | anchor.overbooking | basis:authority | asof:trv13-2.0.1 | grounded-in:trv13-2.0.1:docs/overview.md#use-cases

anchor.confirm-phase-context-required | isa | anchor.validation-anchor | basis:declared | asof:trv13-2.0.1 | grounded-in:trv13-2.0.1:validations/index.yaml#_TESTS_.on_confirm[ON_CONFIRM_CONTEXT]._RETURN_
anchor.confirm-phase-context-required | scoped-to | anchor.on-confirm | basis:declared | asof:trv13-2.0.1 | grounded-in:trv13-2.0.1:validations/index.yaml#_TESTS_.on_confirm[ON_CONFIRM_CONTEXT].action
anchor.confirm-phase-context-required | scoped-to | anchor.status | basis:declared | asof:trv13-2.0.1 | grounded-in:trv13-2.0.1:validations/index.yaml#_TESTS_.status[STATUS_CONTEXT]._RETURN_
anchor.confirm-phase-context-required | requires | anchor.transaction-id | basis:declared | asof:trv13-2.0.1 | grounded-in:trv13-2.0.1:validations/index.yaml#_TESTS_.on_confirm[ON_CONFIRM_CONTEXT]._RETURN_[REQUIRED_ON_CONFIRM_CONTEXT]._RETURN_[REQUIRED_CONTEXT_TRANSACTION_ID]
anchor.confirm-phase-context-required | requires | anchor.message-id | basis:declared | asof:trv13-2.0.1 | grounded-in:trv13-2.0.1:validations/index.yaml#_TESTS_.on_confirm[ON_CONFIRM_CONTEXT]._RETURN_[REQUIRED_ON_CONFIRM_CONTEXT]._RETURN_[REQUIRED_CONTEXT_MESSAGE_ID]
anchor.confirm-phase-context-required | constrains | anchor.rfc3339-millis-timestamp | basis:declared | asof:trv13-2.0.1 | grounded-in:trv13-2.0.1:validations/index.yaml#_TESTS_.on_confirm[ON_CONFIRM_CONTEXT]._RETURN_[REQUIRED_ON_CONFIRM_CONTEXT]._RETURN_[REGEX_CONTEXT_TIMESTAMP].reg
anchor.confirm-phase-context-required | not-requires | anchor.city-code | basis:declared | asof:trv13-2.0.1 | grounded-in:trv13-2.0.1:validations/index.yaml#_TESTS_.on_confirm[ON_CONFIRM_CONTEXT]._RETURN_[REQUIRED_ON_CONFIRM_CONTEXT]._RETURN_
anchor.confirm-phase-context-required | disjoint-with | anchor.discovery-phase-context-required | basis:declared | asof:trv13-2.0.1 | grounded-in:trv13-2.0.1:validations/index.yaml#_TESTS_.search[SEARCH_CONTEXT]._RETURN_[CONTEXT_REQUIRED]._RETURN_

anchor.status-phase-context-required | isa | anchor.validation-anchor | basis:declared | asof:trv13-2.0.1 | grounded-in:trv13-2.0.1:validations/index.yaml#_TESTS_.on_status[ON_STATUS_CONTEXT]._RETURN_
anchor.status-phase-context-required | scoped-to | anchor.on-status | basis:declared | asof:trv13-2.0.1 | grounded-in:trv13-2.0.1:validations/index.yaml#_TESTS_.on_status[ON_STATUS_CONTEXT].action
anchor.status-phase-context-required | scoped-to | anchor.update | basis:declared | asof:trv13-2.0.1 | grounded-in:trv13-2.0.1:validations/index.yaml#_TESTS_.update[UPDATE_CONTEXT]._RETURN_
anchor.status-phase-context-required | requires | anchor.protocol-version | basis:declared | asof:trv13-2.0.1 | grounded-in:trv13-2.0.1:validations/index.yaml#_TESTS_.on_status[ON_STATUS_CONTEXT]._RETURN_[REQUIRED_ON_STATUS_CONTEXT]._RETURN_[REQUIRED_CONTEXT_VERSION]
anchor.status-phase-context-required | constrains | anchor.rfc3339-millis-timestamp | basis:declared | asof:trv13-2.0.1 | grounded-in:trv13-2.0.1:validations/index.yaml#_TESTS_.on_status[ON_STATUS_CONTEXT]._RETURN_[REQUIRED_ON_STATUS_CONTEXT]._RETURN_[REGEX_CONTEXT_TIMESTAMP].reg

anchor.update-phase-context-required | isa | anchor.validation-anchor | basis:declared | asof:trv13-2.0.1 | grounded-in:trv13-2.0.1:validations/index.yaml#_TESTS_.on_update[ON_UPDATE_CONTEXT]._RETURN_
anchor.update-phase-context-required | scoped-to | anchor.on-update | basis:declared | asof:trv13-2.0.1 | grounded-in:trv13-2.0.1:validations/index.yaml#_TESTS_.on_update[ON_UPDATE_CONTEXT].action
anchor.update-phase-context-required | scoped-to | anchor.cancel | basis:declared | asof:trv13-2.0.1 | grounded-in:trv13-2.0.1:validations/index.yaml#_TESTS_.cancel[CANCEL_CONTEXT]._RETURN_
anchor.update-phase-context-required | scoped-to | anchor.on-cancel | basis:declared | asof:trv13-2.0.1 | grounded-in:trv13-2.0.1:validations/index.yaml#_TESTS_.on_cancel[ON_CANCEL_CONTEXT]._RETURN_
anchor.update-phase-context-required | requires | anchor.context-action | basis:declared | asof:trv13-2.0.1 | grounded-in:trv13-2.0.1:validations/index.yaml#_TESTS_.on_update[ON_UPDATE_CONTEXT]._RETURN_[REQUIRED_ON_UPDATE_CONTEXT]._RETURN_[REQUIRED_CONTEXT_ACTION]
anchor.update-phase-context-required | constrains | anchor.rfc3339-millis-timestamp | basis:declared | asof:trv13-2.0.1 | grounded-in:trv13-2.0.1:validations/index.yaml#_TESTS_.on_update[ON_UPDATE_CONTEXT]._RETURN_[REQUIRED_ON_UPDATE_CONTEXT]._RETURN_[REGEX_CONTEXT_TIMESTAMP].reg
anchor.post-confirm-context-check | isa | anchor.validation-anchor | basis:derived | asof:trv13-2.0.1 | grounded-in:anchor.confirm-phase-context-required
anchor.post-confirm-context-check | constrains | anchor.order-lifecycle | basis:derived | asof:trv13-2.0.1 | grounded-in:anchor.update-phase-context-required

anchor.discovery-phase-context-required | isa | anchor.validation-anchor | basis:declared | asof:trv13-2.0.1 | grounded-in:trv13-2.0.1:validations/index.yaml#_TESTS_.search[SEARCH_CONTEXT]._RETURN_[CONTEXT_REQUIRED]
anchor.discovery-phase-context-required | requires | anchor.context-ttl | basis:declared | asof:trv13-2.0.1 | grounded-in:trv13-2.0.1:validations/index.yaml#_TESTS_.search[SEARCH_CONTEXT]._RETURN_[CONTEXT_REQUIRED]._RETURN_[REQUIRED_CONTEXT_TTL]
anchor.discovery-phase-context-required | not-requires | anchor.bpp-id | basis:declared | asof:trv13-2.0.1 | grounded-in:trv13-2.0.1:validations/index.yaml#_TESTS_.search[SEARCH_CONTEXT]._RETURN_[CONTEXT_REQUIRED]._RETURN_
anchor.order-phase-context-required | requires | anchor.bpp-id | basis:declared | asof:trv13-2.0.1 | grounded-in:trv13-2.0.1:validations/index.yaml#_TESTS_.select[SELECT_CONTEXT]._RETURN_[REQUIRED_CONTEXT_FIELDS]._RETURN_[REQUIRED_CONTEXT_BPP_ID]
anchor.order-phase-context-required | scoped-to | anchor.init | basis:declared | asof:trv13-2.0.1 | grounded-in:trv13-2.0.1:validations/index.yaml#_TESTS_.init[INIT_CONTEXT]._RETURN_[REQUIRED_CONTEXT_FIELDS]
anchor.order-phase-context-required | scoped-to | anchor.confirm | basis:declared | asof:trv13-2.0.1 | grounded-in:trv13-2.0.1:validations/index.yaml#_TESTS_.confirm[CONFIRM_CONTEXT]._RETURN_[REQUIRED_CONTEXT_FIELDS]
anchor.igm-context-required | scoped-to | anchor.issue | basis:declared | asof:trv13-2.0.1 | grounded-in:trv13-2.0.1:validations/index.yaml#_TESTS_.issue[REQUIRED_CONTEXT_FIELDS]
anchor.igm-context-required | not-scoped-to | anchor.trv13 | basis:declared | asof:trv13-2.0.1 | grounded-in:trv13-2.0.1:validations/index.yaml#_TESTS_.issue[REQUIRED_CONTEXT_FIELDS]

anchor.search-intent-tags | requires | anchor.bap-terms | basis:declared | asof:trv13-2.0.1 | grounded-in:trv13-2.0.1:validations/index.yaml#_TESTS_.search[SEARCH_INTENT_TAGS]._RETURN_[TAG_GROUPS_REQUIRED].validTags
anchor.search-intent-tags | requires | anchor.buyer-finder-fees | basis:declared | asof:trv13-2.0.1 | grounded-in:trv13-2.0.1:validations/index.yaml#_TESTS_.search[SEARCH_INTENT_TAGS]._RETURN_[TAG_GROUPS_REQUIRED].validTags
anchor.catalog-inc | isa | anchor.search-intent-tag-group | basis:declared | asof:trv13-2.0.1 | grounded-in:trv13-2.0.1:validations/index.yaml#_TESTS_.search[SEARCH_INTENT_TAGS]._RETURN_[TAG_GROUPS_REQUIRED].validTags
anchor.catalog-inc | constrains | anchor.incremental-catalog-refresh | basis:inferred | asof:trv13-2.0.1
anchor.bap-terms | has-slot | anchor.static-terms | basis:declared | asof:trv13-2.0.1 | grounded-in:trv13-2.0.1:validations/index.yaml#_TESTS_.search[SEARCH_INTENT_TAGS]._RETURN_[TAG_BAP_TERMS].validValues
anchor.bap-terms | has-slot | anchor.effective-date | basis:declared | asof:trv13-2.0.1 | grounded-in:trv13-2.0.1:validations/index.yaml#_TESTS_.search[SEARCH_INTENT_TAGS]._RETURN_[TAG_BAP_TERMS].validValues
anchor.buyer-finder-fees | has-slot | anchor.buyer-finder-fees-percentage | basis:declared | asof:trv13-2.0.1 | grounded-in:trv13-2.0.1:validations/index.yaml#_TESTS_.search[SEARCH_INTENT_TAGS]._RETURN_[TAG_BUYER_FINDER_FEES].validValues
anchor.bap-terms | sent-by | "BAP" | basis:declared | asof:trv13-2.0.1 | grounded-in:trv13-2.0.1:attributes/Hotel_Booking-V2.yaml#attribute_set.search.message.intent.tags.descriptor.code._description
anchor.bpp-terms | sent-by | "BPP" | basis:declared | asof:trv13-2.0.1 | grounded-in:trv13-2.0.1:validations/index.yaml#_TESTS_.on_init[ON_INIT_TAGS]._RETURN_[PAYMENT_TAG_GROUP].validTags
anchor.bpp-terms | has-slot | anchor.max-liability | basis:declared | asof:trv13-2.0.1 | grounded-in:trv13-2.0.1:validations/index.yaml#_TESTS_.on_init[ON_INIT_TAGS]._RETURN_[REQUIRED_PAYMENT_TAG_BPP_TERMS].validValues
anchor.bpp-terms | has-slot | anchor.court-jurisdiction | basis:declared | asof:trv13-2.0.1 | grounded-in:trv13-2.0.1:validations/index.yaml#_TESTS_.on_init[ON_INIT_TAGS]._RETURN_[REQUIRED_PAYMENT_TAG_BPP_TERMS].validValues
anchor.bpp-terms | has-slot | anchor.mandatory-arbitration | basis:declared | asof:trv13-2.0.1 | grounded-in:trv13-2.0.1:validations/index.yaml#_TESTS_.on_init[ON_INIT_TAGS]._RETURN_[REQUIRED_PAYMENT_TAG_BPP_TERMS].validValues
anchor.bpp-terms | has-slot | anchor.tax-number | basis:declared | asof:trv13-2.0.1 | grounded-in:trv13-2.0.1:validations/index.yaml#_TESTS_.confirm[CONFIRM_TAGS]._RETURN_[REQUIRED_PAYMENT_TAG_BPP_TERMS].validValues
anchor.bpp-terms | scoped-to | anchor.order | basis:declared | asof:trv13-2.0.1 | grounded-in:trv13-2.0.1:validations/index.yaml#_TESTS_.confirm[CONFIRM_TAGS]._RETURN_[PAYMENT_TAG_GROUP].tagPath
anchor.bap-terms | precedes | anchor.bpp-terms | basis:declared | asof:trv13-2.0.1 | grounded-in:trv13-2.0.1:validations/index.yaml#_TESTS_.init[INIT_ORDER_TAGS]._RETURN_[REQUIRED_BAP_TERMS]
anchor.order-terms | constrains | anchor.liability-allocation | basis:authority | asof:trv13-2.0.1 | grounded-in:trv13-2.0.1:docs/overview.md#key-concepts

anchor.hotel-catalog | sent-by | "BPP" | basis:declared | asof:trv13-2.0.1 | grounded-in:trv13-2.0.1:attributes/Hotel_Booking-V2.yaml#attribute_set.on_search.message.catalog._description
anchor.hotel-catalog | has-slot | anchor.hotel-provider | basis:declared | asof:trv13-2.0.1 | grounded-in:trv13-2.0.1:attributes/Hotel_Booking-V2.yaml#attribute_set.on_search.message.catalog.providers._description
anchor.hotel-provider | requires | anchor.provider-id | basis:declared | asof:trv13-2.0.1 | grounded-in:trv13-2.0.1:validations/index.yaml#_TESTS_.on_search[PROVIDERS_REQUIRED]._RETURN_[REQUIRED_PROVIDER_ID]
anchor.hotel-provider | requires | anchor.hotel-property-location | basis:declared | asof:trv13-2.0.1 | grounded-in:trv13-2.0.1:attributes/Hotel_Booking-V2.yaml#attribute_set.on_search.message.catalog.providers.locations._description
anchor.hotel-provider | requires | anchor.provider-image | basis:declared | asof:trv13-2.0.1 | grounded-in:trv13-2.0.1:validations/index.yaml#_TESTS_.on_search[PROVIDERS_REQUIRED]._RETURN_[REQUIRED_PROVIDER_IMAGES]
anchor.hotel-property-location | has-slot | anchor.property-type-code | basis:declared | asof:trv13-2.0.1 | grounded-in:trv13-2.0.1:attributes/Hotel_Booking-V2.yaml#attribute_set.on_search.message.catalog.providers.locations.descriptor.code._description
anchor.property-type-code | isa | anchor.enum | basis:declared | asof:trv13-2.0.1 | grounded-in:trv13-2.0.1:attributes/Hotel_Booking-V2.yaml#attribute_set.on_search.message.catalog.providers.locations.descriptor.code._description.enums
anchor.property-type-code | has-slot | anchor.star-rating | basis:declared | asof:trv13-2.0.1 | grounded-in:trv13-2.0.1:attributes/Hotel_Booking-V2.yaml#attribute_set.on_search.message.catalog.providers.locations.descriptor.code._description.enums
anchor.hotel-property-location | requires | anchor.gps | basis:declared | asof:trv13-2.0.1 | grounded-in:trv13-2.0.1:attributes/Hotel_Booking-V2.yaml#attribute_set.on_search.message.catalog.providers.locations.gps._description
anchor.hotel-property-location | requires | anchor.area-code | basis:declared | asof:trv13-2.0.1 | grounded-in:trv13-2.0.1:attributes/Hotel_Booking-V2.yaml#attribute_set.on_search.message.catalog.providers.locations.area_code._description
anchor.hotel-property-location | has-slot | anchor.property-rating | basis:declared | asof:trv13-2.0.1 | grounded-in:trv13-2.0.1:attributes/Hotel_Booking-V2.yaml#attribute_set.on_search.message.catalog.providers.locations.rating._description
anchor.hotel-provider | has-slot | anchor.room-category | basis:declared | asof:trv13-2.0.1 | grounded-in:trv13-2.0.1:attributes/Hotel_Booking-V2.yaml#attribute_set.on_search.message.catalog.providers.categories._description
anchor.hotel-provider | has-slot | anchor.provider-amenity-tag | basis:declared | asof:trv13-2.0.1 | grounded-in:trv13-2.0.1:attributes/Hotel_Booking-V2.yaml#attribute_set.on_search.message.catalog.providers.tags._description
anchor.provider-amenity-tag | constrains | anchor.inclusions-exclusions | basis:declared | asof:trv13-2.0.1 | grounded-in:trv13-2.0.1:attributes/Hotel_Booking-V2.yaml#attribute_set.on_search.message.catalog.providers.tags.descriptor.code._description
anchor.provider-amenity-tag | has-slot | anchor.tag-display-flag | basis:declared | asof:trv13-2.0.1 | grounded-in:trv13-2.0.1:attributes/Hotel_Booking-V2.yaml#attribute_set.on_search.message.catalog.providers.tags.display._description
anchor.hotel-provider | has-slot | anchor.provider-payment-option | basis:declared | asof:trv13-2.0.1 | grounded-in:trv13-2.0.1:attributes/Hotel_Booking-V2.yaml#attribute_set.on_search.message.catalog.providers.payments._description
anchor.provider-payment-option | constrains | anchor.payment-type | basis:declared | asof:trv13-2.0.1 | grounded-in:trv13-2.0.1:validations/index.yaml#_TESTS_.on_search[PROVIDER_PAYMENTS]._RETURN_[VALID_PAYMENT_TYPES].enumList

anchor.accommodation-item | part-of | anchor.hotel-provider | basis:declared | asof:trv13-2.0.1 | grounded-in:trv13-2.0.1:attributes/Hotel_Booking-V2.yaml#attribute_set.on_search.message.catalog.providers.items._description
anchor.accommodation-item | requires | anchor.item-id | basis:declared | asof:trv13-2.0.1 | grounded-in:trv13-2.0.1:validations/index.yaml#_TESTS_.on_search[PROVIDER_ITEMS]._RETURN_[REQUIRED_ITEM_ID]
anchor.accommodation-item | requires | anchor.item-price | basis:declared | asof:trv13-2.0.1 | grounded-in:trv13-2.0.1:validations/index.yaml#_TESTS_.on_search[PROVIDER_ITEMS]._RETURN_[REQUIRED_ITEM_PRICE]
anchor.item-price | has-slot | anchor.maximum-price | basis:declared | asof:trv13-2.0.1 | grounded-in:trv13-2.0.1:validations/index.yaml#_TESTS_.on_search[PROVIDER_ITEMS]._RETURN_[REQUIRED_ITEM_PRICE_MAX_VALUE]
anchor.item-price | constrains | anchor.price-consistency | basis:declared | asof:trv13-2.0.1 | grounded-in:trv13-2.0.1:attributes/Hotel_Booking-V2.yaml#attribute_set.on_search.message.catalog.providers.items.price.value._description
anchor.accommodation-item | requires | anchor.room-inventory | basis:declared | asof:trv13-2.0.1 | grounded-in:trv13-2.0.1:validations/index.yaml#_TESTS_.on_search[PROVIDER_ITEMS]._RETURN_[REQUIRED_ITEM_QUANTITY_AVAILABLE]
anchor.room-inventory | constrains | anchor.max-bookable-count | basis:declared | asof:trv13-2.0.1 | grounded-in:trv13-2.0.1:attributes/Hotel_Booking-V2.yaml#attribute_set.on_search.message.catalog.providers.items.quantity.maximum._description
anchor.room-inventory | scoped-to | anchor.accommodation-item | basis:declared | asof:trv13-2.0.1 | grounded-in:trv13-2.0.1:attributes/Hotel_Booking-V2.yaml#attribute_set.on_search.message.catalog.providers.items.quantity.available.count._description
anchor.accommodation-item | requires | anchor.location-id | basis:declared | asof:trv13-2.0.1 | grounded-in:trv13-2.0.1:validations/index.yaml#_TESTS_.on_search[PROVIDER_ITEMS]._RETURN_[REQUIRED_ITEM_LOCATION_LINK]
anchor.accommodation-item | requires | anchor.payment-id | basis:declared | asof:trv13-2.0.1 | grounded-in:trv13-2.0.1:validations/index.yaml#_TESTS_.on_search[PROVIDER_ITEMS]._RETURN_[REQUIRED_ITEM_PAYMENT_LINK]
anchor.accommodation-item | requires | anchor.room-category | basis:declared | asof:trv13-2.0.1 | grounded-in:trv13-2.0.1:validations/index.yaml#_TESTS_.on_search[PROVIDER_ITEMS]._RETURN_[REQUIRED_ITEM_CATEGORY_LINK]
anchor.accommodation-item | has-slot | anchor.item-availability-window | basis:declared | asof:trv13-2.0.1 | grounded-in:trv13-2.0.1:validations/index.yaml#_TESTS_.on_search[PROVIDER_ITEMS]._RETURN_[REQUIRED_ITEM_TIMESTAMPS]
anchor.accommodation-item | has-slot | anchor.item-add-on | basis:declared | asof:trv13-2.0.1 | grounded-in:trv13-2.0.1:attributes/Hotel_Booking-V2.yaml#attribute_set.on_search.message.catalog.providers.items.add_ons._description
anchor.item-add-on | has-slot | anchor.add-on-price | basis:declared | asof:trv13-2.0.1 | grounded-in:trv13-2.0.1:attributes/Hotel_Booking-V2.yaml#attribute_set.on_search.message.catalog.providers.items.add_ons.price._description
anchor.item-add-on | scoped-to | anchor.meal-plan | basis:declared | asof:trv13-2.0.1 | grounded-in:trv13-2.0.1:attributes/Hotel_Booking-V2.yaml#attribute_set.on_search.message.catalog.providers.items.add_ons.descriptor.short_desc._description
anchor.accommodation-item | has-slot | anchor.item-amenity-tag | basis:declared | asof:trv13-2.0.1 | grounded-in:trv13-2.0.1:attributes/Hotel_Booking-V2.yaml#attribute_set.on_search.message.catalog.providers.items.tags._description
anchor.accommodation-item | has-slot | anchor.recommended-flag | basis:declared | asof:trv13-2.0.1 | grounded-in:trv13-2.0.1:attributes/Hotel_Booking-V2.yaml#attribute_set.on_search.message.catalog.providers.items.recommended._description
anchor.room-type-code | scoped-to | anchor.accommodation-item | basis:declared | asof:trv13-2.0.1 | grounded-in:trv13-2.0.1:attributes/Hotel_Booking-V2.yaml#attribute_set.on_search.message.catalog.providers.items.descriptor.code._description

anchor.cancellation-terms | part-of | anchor.accommodation-item | basis:declared | asof:trv13-2.0.1 | grounded-in:trv13-2.0.1:attributes/Hotel_Booking-V2.yaml#attribute_set.on_search.message.catalog.providers.items.cancellation_terms.cancellation_fee._description
anchor.cancellation-terms | has-slot | anchor.cancellation-fee-percentage | basis:declared | asof:trv13-2.0.1 | grounded-in:trv13-2.0.1:attributes/Hotel_Booking-V2.yaml#attribute_set.on_search.message.catalog.providers.items.cancellation_terms.cancellation_fee.percentage._description
anchor.cancellation-terms | has-slot | anchor.cancel-by-window | basis:declared | asof:trv13-2.0.1 | grounded-in:trv13-2.0.1:attributes/Hotel_Booking-V2.yaml#attribute_set.on_search.message.catalog.providers.items.cancellation_terms.cancel_by._description
anchor.cancel-by-window | constrains | anchor.buyer-initiated-cancellation | basis:declared | asof:trv13-2.0.1 | grounded-in:trv13-2.0.1:attributes/Hotel_Booking-V2.yaml#attribute_set.on_search.message.catalog.providers.items.cancellation_terms.cancel_by.range.end._description
anchor.cancellation-eligible | constrains | anchor.buyer-initiated-cancellation | basis:declared | asof:trv13-2.0.1 | grounded-in:trv13-2.0.1:attributes/Hotel_Booking-V2.yaml#attribute_set.on_search.message.catalog.providers.items.cancellation_terms.cancellation_eligible._description
anchor.cancellation-terms | has-slot | anchor.external-terms-ref | basis:declared | asof:trv13-2.0.1 | grounded-in:trv13-2.0.1:validations/index.yaml#_TESTS_.on_search[ITEM_ADDONS]._RETURN_[REQUIRED_CANCELLATION_TERMS_URL]
anchor.external-terms-ref | isa | anchor.remote-document | basis:declared | asof:trv13-2.0.1 | grounded-in:trv13-2.0.1:attributes/Hotel_Booking-V2.yaml#attribute_set.on_search.message.catalog.providers.items.cancellation_terms.external_ref._description
anchor.cancellation-terms | scoped-to | anchor.order | basis:declared | asof:trv13-2.0.1 | grounded-in:trv13-2.0.1:attributes/Hotel_Booking-V2.yaml#attribute_set.on_select.message.order.cancellation_terms._description
anchor.cancellation-terms | precedes | anchor.on-confirm | basis:declared | asof:trv13-2.0.1 | grounded-in:trv13-2.0.1:attributes/Hotel_Booking-V2.yaml#attribute_set.on_confirm.message.order.cancellation_terms._description
anchor.cancellation-terms | wasGeneratedBy | anchor.on-select | basis:declared | asof:trv13-2.0.1 | grounded-in:trv13-2.0.1:attributes/Hotel_Booking-V2.yaml#attribute_set.on_select.message.order.cancellation_terms.cancellation_eligible._description

anchor.select | causes | anchor.booking-intent | basis:declared | asof:trv13-2.0.1 | grounded-in:trv13-2.0.1:flows/Hotel-Booking-V2/Order_to_Confirm_to_Fulfillment__City_Code_.yaml#steps[select_5].description
anchor.select | requires | anchor.stay-date-range | basis:declared | asof:trv13-2.0.1 | grounded-in:trv13-2.0.1:validations/index.yaml#_TESTS_.select[SELECT_ORDER]._RETURN_[REQUIRED_PROVIDER_TIME_RANGE]
anchor.stay-date-range | scoped-to | anchor.hotel-provider | basis:declared | asof:trv13-2.0.1 | grounded-in:trv13-2.0.1:attributes/Hotel_Booking-V2.yaml#attribute_set.select.message.order.provider.time._description
anchor.select | requires | anchor.selected-quantity | basis:declared | asof:trv13-2.0.1 | grounded-in:trv13-2.0.1:validations/index.yaml#_TESTS_.select[SELECT_ORDER_ITEMS]._RETURN_[REQUIRED_ITEM_QUANTITY_SELECTED]
anchor.selected-quantity | sent-by | "BAP" | basis:declared | asof:trv13-2.0.1 | grounded-in:trv13-2.0.1:attributes/Hotel_Booking-V2.yaml#attribute_set.select.message.order.items.quantity.selected.count._description
anchor.select | requires | anchor.guests-tag | basis:declared | asof:trv13-2.0.1 | grounded-in:trv13-2.0.1:validations/index.yaml#_TESTS_.select[SELECT_ORDER_FULFILLMENTS]._RETURN_[VALID_FULFILLMENT_TAG_GUESTS].enumList
anchor.guests-tag | isa | anchor.fulfillment-tag-group | basis:declared | asof:trv13-2.0.1 | grounded-in:trv13-2.0.1:attributes/Hotel_Booking-V2.yaml#attribute_set.select.message.order.fulfillments.tags.descriptor.code._description
anchor.guests-tag | has-slot | anchor.adults-count | basis:declared | asof:trv13-2.0.1 | grounded-in:trv13-2.0.1:validations/index.yaml#_TESTS_.select[SELECT_ORDER_FULFILLMENTS]._RETURN_[VALID_FULFILLMENT_SUBTAGS].enumList
anchor.guests-tag | has-slot | anchor.children-count | basis:declared | asof:trv13-2.0.1 | grounded-in:trv13-2.0.1:validations/index.yaml#_TESTS_.select[SELECT_ORDER_FULFILLMENTS]._RETURN_[VALID_FULFILLMENT_SUBTAGS].enumList
anchor.adults-count | constrains | anchor.occupancy | basis:declared | asof:trv13-2.0.1 | grounded-in:trv13-2.0.1:attributes/Hotel_Booking-V2.yaml#attribute_set.select.message.order.fulfillments.tags.list.descriptor.code._description
anchor.guests-tag | scoped-to | anchor.order-fulfillment | basis:declared | asof:trv13-2.0.1 | grounded-in:trv13-2.0.1:flows/Hotel-Booking-V2/Order_to_Confirm_to_Fulfillment__City_Code_.yaml#steps[select_5].mock.defaultPayload.message.order.fulfillments[0].tags[0].descriptor.code
anchor.on-select | causes | anchor.quote | basis:declared | asof:trv13-2.0.1 | grounded-in:trv13-2.0.1:attributes/Hotel_Booking-V2.yaml#attribute_set.on_select.message.order.quote._description
anchor.quote | requires | anchor.quote-breakup | basis:declared | asof:trv13-2.0.1 | grounded-in:trv13-2.0.1:validations/index.yaml#_TESTS_.on_select[ON_SELECT_ORDER_QUOTE]._RETURN_[REQUIRED_QUOTE_BREAKUP]
anchor.quote | requires | anchor.quote-ttl | basis:declared | asof:trv13-2.0.1 | grounded-in:trv13-2.0.1:validations/index.yaml#_TESTS_.on_select[ON_SELECT_ORDER_QUOTE]._RETURN_[REQUIRED_QUOTE_TTL]
anchor.quote-ttl | constrains | anchor.price-validity | basis:declared | asof:trv13-2.0.1 | grounded-in:trv13-2.0.1:attributes/Hotel_Booking-V2.yaml#attribute_set.on_select.message.order.quote.ttl._description
anchor.quote-total | wasDerivedFrom | anchor.quote-breakup | basis:declared | asof:trv13-2.0.1 | grounded-in:trv13-2.0.1:attributes/Hotel_Booking-V2.yaml#attribute_set.on_select.message.order.quote.price.value._description
anchor.quote-breakup | has-slot | anchor.add-on-price | basis:declared | asof:trv13-2.0.1 | grounded-in:trv13-2.0.1:attributes/Hotel_Booking-V2.yaml#attribute_set.on_select.message.order.quote.breakup.item.add_ons.price._description
anchor.quote-breakup | requires | anchor.breakup-title | basis:declared | asof:trv13-2.0.1 | grounded-in:trv13-2.0.1:validations/index.yaml#_TESTS_.on_select[ON_SELECT_ORDER_QUOTE]._RETURN_[REQUIRED_QUOTE_BREAKUP_TITLE]
anchor.quote | precedes | anchor.confirm | basis:declared | asof:trv13-2.0.1 | grounded-in:trv13-2.0.1:validations/index.yaml#_TESTS_.confirm[CONFIRM_ORDER_QUOTE]

anchor.init | causes | anchor.order-initialisation | basis:declared | asof:trv13-2.0.1 | grounded-in:trv13-2.0.1:flows/Hotel-Booking-V2/Order_to_Confirm_to_Fulfillment__City_Code_.yaml#steps[init_5].description
anchor.init | requires | anchor.billing | basis:declared | asof:trv13-2.0.1 | grounded-in:trv13-2.0.1:validations/index.yaml#_TESTS_.init[INIT_ORDER_BILLING]
anchor.billing | requires | anchor.tax-id | basis:declared | asof:trv13-2.0.1 | grounded-in:trv13-2.0.1:validations/index.yaml#_TESTS_.init[INIT_ORDER_BILLING]._RETURN_[REQUIRED_BILLING_TAX_ID]
anchor.billing | requires | anchor.billing-organization | basis:declared | asof:trv13-2.0.1 | grounded-in:trv13-2.0.1:validations/index.yaml#_TESTS_.init[INIT_ORDER_BILLING]._RETURN_[REQUIRED_BILLING_ORGANIZATION_DESCRIPTOR_NAME]
anchor.billing | has-slot | anchor.billing-state | basis:declared | asof:trv13-2.0.1 | grounded-in:trv13-2.0.1:attributes/Hotel_Booking-V2.yaml#attribute_set.init.message.order.billing.state._description
anchor.billing-state | causes | anchor.state-level-tax | basis:declared | asof:trv13-2.0.1 | grounded-in:trv13-2.0.1:attributes/Hotel_Booking-V2.yaml#attribute_set.init.message.order.billing.state._description
anchor.billing | sent-by | "BAP" | basis:declared | asof:trv13-2.0.1 | grounded-in:trv13-2.0.1:attributes/Hotel_Booking-V2.yaml#attribute_set.init.message.order.billing._description
anchor.init | requires | anchor.order-fulfillment | basis:declared | asof:trv13-2.0.1 | grounded-in:trv13-2.0.1:validations/index.yaml#_TESTS_.init[INIT_ORDER_FULFILLMENTS]._RETURN_[REQUIRED_FULFILLMENT_ID]
anchor.order-fulfillment | requires | anchor.guest-identity | basis:declared | asof:trv13-2.0.1 | grounded-in:trv13-2.0.1:validations/index.yaml#_TESTS_.init[INIT_ORDER_FULFILLMENTS]._RETURN_[REQUIRED_CUSTOMER_NAME]
anchor.guest-identity | requires | anchor.guest-age | basis:declared | asof:trv13-2.0.1 | grounded-in:trv13-2.0.1:validations/index.yaml#_TESTS_.init[INIT_ORDER_FULFILLMENTS]._RETURN_[REQUIRED_CUSTOMER_AGE]
anchor.guest-identity | requires | anchor.guest-dob | basis:declared | asof:trv13-2.0.1 | grounded-in:trv13-2.0.1:validations/index.yaml#_TESTS_.init[INIT_ORDER_FULFILLMENTS]._RETURN_[REQUIRED_CUSTOMER_DOB]
anchor.guest-identity | requires | anchor.guest-gender | basis:declared | asof:trv13-2.0.1 | grounded-in:trv13-2.0.1:validations/index.yaml#_TESTS_.init[INIT_ORDER_FULFILLMENTS]._RETURN_[REQUIRED_CUSTOMER_GENDER]
anchor.guest-identity | has-slot | anchor.guest-credential | basis:declared | asof:trv13-2.0.1 | grounded-in:trv13-2.0.1:attributes/Hotel_Booking-V2.yaml#attribute_set.init.message.order.fulfillments.customer.person.creds._description
anchor.guest-credential | scoped-to | anchor.aadhaar | basis:declared | asof:trv13-2.0.1 | grounded-in:trv13-2.0.1:flows/Hotel-Booking-V2/Order_to_Confirm_to_Fulfillment__City_Code_.yaml#steps[confirm_5].mock.defaultPayload.message.order.fulfillments[0].customer.person.creds[0].type
anchor.customer-contact | requires | anchor.customer-contact-email | basis:declared | asof:trv13-2.0.1 | grounded-in:trv13-2.0.1:validations/index.yaml#_TESTS_.init[INIT_ORDER_FULFILLMENTS]._RETURN_[REQUIRED_CUSTOMER_CONTACT_EMAIL]
anchor.customer-contact | requires | anchor.customer-phone | basis:declared | asof:trv13-2.0.1 | grounded-in:trv13-2.0.1:validations/index.yaml#_TESTS_.init[INIT_ORDER_FULFILLMENTS]._RETURN_[REQUIRED_CUSTOMER_CONTACT]
anchor.customer-contact | part-of | anchor.order-fulfillment | basis:declared | asof:trv13-2.0.1 | grounded-in:trv13-2.0.1:attributes/Hotel_Booking-V2.yaml#attribute_set.init.message.order.fulfillments.customer.contact._description
anchor.on-init | causes | anchor.binding-offer | basis:declared | asof:trv13-2.0.1 | grounded-in:trv13-2.0.1:flows/Hotel-Booking-V2/Merchant_Side_Full_Cancellation.yaml#steps[on_init_5].description
anchor.on-init | requires | anchor.payment-status | basis:declared | asof:trv13-2.0.1 | grounded-in:trv13-2.0.1:validations/index.yaml#_TESTS_.on_init[ON_INIT_PAYMENTS]._RETURN_[REQUIRED_PAYMENT_STATUS]
anchor.confirm | causes | anchor.booking-commitment | basis:declared | asof:trv13-2.0.1 | grounded-in:trv13-2.0.1:flows/Hotel-Booking-V2/Merchant_Side_Full_Cancellation.yaml#steps[confirm_5].description
anchor.confirm | requires | anchor.order-created-at | basis:declared | asof:trv13-2.0.1 | grounded-in:trv13-2.0.1:validations/index.yaml#_TESTS_.confirm[CONFIRM_TIMESTAMPS]._RETURN_[REQUIRED_CREATED_AT]
anchor.on-confirm | causes | anchor.order-id | basis:declared | asof:trv13-2.0.1 | grounded-in:trv13-2.0.1:validations/index.yaml#_TESTS_.on_confirm[ON_CONFIRM_ORDER]._RETURN_[REQUIRED_ON_CONFIRM_ORDER]._RETURN_[REQUIRED_ORDER_ID]
anchor.on-confirm | causes | anchor.order-active | basis:declared | asof:trv13-2.0.1 | grounded-in:trv13-2.0.1:flows/Hotel-Booking-V2/Order_to_Confirm_to_Fulfillment__City_Code_.yaml#steps[on_confirm_5].mock.defaultPayload.message.order.status
anchor.order-active | isa | anchor.order-status | basis:declared | asof:trv13-2.0.1 | grounded-in:trv13-2.0.1:validations/index.yaml#_TESTS_.on_confirm[ON_CONFIRM_ORDER]._RETURN_[VALID_ENUM_ON_CONFIRM_ORDER]._RETURN_[VALID_ENUM_ORDER_STATUS].enumList
anchor.order-status | isa | anchor.enum | basis:declared | asof:trv13-2.0.1 | grounded-in:trv13-2.0.1:attributes/Hotel_Booking-V2.yaml#attribute_set.on_status.message.order.status._description.enums
anchor.soft-cancel | precedes | anchor.confirm-cancel | basis:declared | asof:trv13-2.0.1 | grounded-in:trv13-2.0.1:attributes/Hotel_Booking-V2.yaml#attribute_set.on_status.message.order.status._description.enums
anchor.soft-update | precedes | anchor.confirm-update | basis:declared | asof:trv13-2.0.1 | grounded-in:trv13-2.0.1:attributes/Hotel_Booking-V2.yaml#attribute_set.on_status.message.order.status._description.enums
anchor.soft-cancel | isa | anchor.order-status | basis:declared | asof:trv13-2.0.1 | grounded-in:trv13-2.0.1:validations/index.yaml#_TESTS_.on_status[ON_STATUS_ORDER]._RETURN_[VALID_ENUM_ON_STATUS_ORDER]._RETURN_[VALID_ENUM_ORDER_STATUS].enumList
anchor.order-status | not-scoped-to | anchor.select | basis:declared | asof:trv13-2.0.1 | grounded-in:trv13-2.0.1:validations/index.yaml#_TESTS_.on_select[ON_SELECT_ORDER]

anchor.payment-type | isa | anchor.enum | basis:declared | asof:trv13-2.0.1 | grounded-in:trv13-2.0.1:attributes/Hotel_Booking-V2.yaml#attribute_set.on_search.message.catalog.providers.payments.type._description.enums
anchor.pre-order-payment | isa | anchor.payment-type | basis:declared | asof:trv13-2.0.1 | grounded-in:trv13-2.0.1:attributes/Hotel_Booking-V2.yaml#attribute_set.on_search.message.catalog.providers.payments.type._description.enums
anchor.on-fulfillment-payment | isa | anchor.payment-type | basis:declared | asof:trv13-2.0.1 | grounded-in:trv13-2.0.1:attributes/Hotel_Booking-V2.yaml#attribute_set.on_search.message.catalog.providers.payments.type._description.enums
anchor.part-payment | isa | anchor.payment-type | basis:declared | asof:trv13-2.0.1 | grounded-in:trv13-2.0.1:validations/index.yaml#_TESTS_.on_init[ON_INIT_PAYMENTS]._RETURN_[VALID_PAYMENT_TYPES].enumList
anchor.payment-status | isa | anchor.enum | basis:declared | asof:trv13-2.0.1 | grounded-in:trv13-2.0.1:validations/index.yaml#_TESTS_.on_init[ON_INIT_PAYMENTS]._RETURN_[VALID_PAYMENT_STATUS].enumList
anchor.collected-by | isa | anchor.enum | basis:declared | asof:trv13-2.0.1 | grounded-in:trv13-2.0.1:attributes/Hotel_Booking-V2.yaml#attribute_set.init.message.order.payments.collected_by._description.enums
anchor.collected-by | constrains | anchor.settlement-direction | basis:declared | asof:trv13-2.0.1 | grounded-in:trv13-2.0.1:attributes/Hotel_Booking-V2.yaml#attribute_set.init.message.order.payments.collected_by._description
anchor.linked-payments-tag | scoped-to | anchor.part-payment | basis:declared | asof:trv13-2.0.1 | grounded-in:trv13-2.0.1:flows/Hotel-Booking-V2/Order_to_Confirm_to_Fulfillment__City_Code_.yaml#steps[confirm_5].mock.defaultPayload.message.order.payments[0].tags[0].descriptor.code
anchor.linked-payments-tag | isa | anchor.payment-tag-group | basis:declared | asof:trv13-2.0.1 | grounded-in:trv13-2.0.1:validations/index.yaml#_TESTS_.on_status[ON_STATUS_PAYMENTS]._RETURN_[REQUIRED_PAYMENTS_LINKED_TAGS]._RETURN_[REQUIRED_LINKED_PAYMENT_TAG].enumList
anchor.adv-deposit-tag | isa | anchor.payment-tag-group | basis:declared | asof:trv13-2.0.1 | grounded-in:trv13-2.0.1:validations/index.yaml#_TESTS_.on_status[ON_STATUS_PAYMENTS]._RETURN_[REQUIRED_PAYMENTS_LINKED_TAGS]._RETURN_[REQUIRED_LINKED_PAYMENT_TAG].enumList
anchor.final-payment-tag | isa | anchor.payment-tag-group | basis:declared | asof:trv13-2.0.1 | grounded-in:trv13-2.0.1:validations/index.yaml#_TESTS_.on_update[ON_UPDATE_PAYMENTS]._RETURN_[REQUIRED_PAYMENTS_LINKED_TAGS]._RETURN_[REQUIRED_LINKED_PAYMENT_TAG].enumList
anchor.adv-deposit-tag | scoped-to | anchor.pre-order-payment | basis:declared | asof:trv13-2.0.1 | grounded-in:trv13-2.0.1:flows/Hotel-Booking-V2/Order_to_Confirm_to_Fulfillment__City_Code_.yaml#steps[confirm_5].mock.defaultPayload.message.order.payments[1].tags[0].descriptor.code
anchor.final-payment-tag | scoped-to | anchor.on-fulfillment-payment | basis:declared | asof:trv13-2.0.1 | grounded-in:trv13-2.0.1:flows/Hotel-Booking-V2/Order_to_Confirm_to_Fulfillment__City_Code_.yaml#steps[confirm_5].mock.defaultPayload.message.order.payments[2].tags[0].descriptor.code
anchor.linked-payments-tag | causes | anchor.split-settlement | basis:declared | asof:trv13-2.0.1 | grounded-in:trv13-2.0.1:attributes/Hotel_Booking-V2.yaml#attribute_set.on_select.message.order.payments.tags._description
anchor.adv-deposit-tag | precedes | anchor.final-payment-tag | basis:declared | asof:trv13-2.0.1 | grounded-in:trv13-2.0.1:flows/Hotel-Booking-V2/Order_to_Confirm_to_Fulfillment__City_Code_.yaml#steps[confirm_5].mock.defaultPayload.message.order.payments
anchor.split-settlement | causes | anchor.payment-status | basis:declared | asof:trv13-2.0.1 | grounded-in:trv13-2.0.1:flows/Hotel-Booking-V2/Order_to_Confirm_to_Fulfillment__Updates_in_Booking_.yaml#steps[on_update_5].mock.generate
anchor.init | requires | anchor.payment-amount | basis:declared | asof:trv13-2.0.1 | grounded-in:trv13-2.0.1:validations/index.yaml#_TESTS_.init[INIT_ORDER_PAYMENTS]._RETURN_[REQUIRED_PAYMENT_PARAMS]
anchor.part-payment | not-requires | anchor.payment-amount | basis:declared | asof:trv13-2.0.1 | grounded-in:trv13-2.0.1:validations/index.yaml#_TESTS_.init[INIT_ORDER_PAYMENTS]._RETURN_[REQUIRED_PAYMENT_PARAMS].attr
anchor.payment-id | constrains | anchor.linked-payments-tag | basis:declared | asof:trv13-2.0.1 | grounded-in:trv13-2.0.1:attributes/Hotel_Booking-V2.yaml#attribute_set.init.message.order.payments.tags.list.descriptor.code._description

anchor.transaction-id | constrains | anchor.transaction-session | basis:declared | asof:trv13-2.0.1 | grounded-in:trv13-2.0.1:attributes/Hotel_Booking-V2.yaml#attribute_set.search.context.transaction_id._description
anchor.message-id | scoped-to | anchor.request-callback-cycle | basis:declared | asof:trv13-2.0.1 | grounded-in:trv13-2.0.1:attributes/Hotel_Booking-V2.yaml#attribute_set.search.context.message_id._description
anchor.context-ttl | constrains | anchor.message-validity | basis:declared | asof:trv13-2.0.1 | grounded-in:trv13-2.0.1:attributes/Hotel_Booking-V2.yaml#attribute_set.search.context.ttl._description
anchor.bap-id | isa | anchor.subscriber-id | basis:declared | asof:trv13-2.0.1 | grounded-in:trv13-2.0.1:attributes/Hotel_Booking-V2.yaml#attribute_set.search.context.bap_id._description
anchor.bpp-id | isa | anchor.subscriber-id | basis:declared | asof:trv13-2.0.1 | grounded-in:trv13-2.0.1:attributes/Hotel_Booking-V2.yaml#attribute_set.on_search.context.bpp_id._description
anchor.bap-uri | isa | anchor.callback-endpoint | basis:declared | asof:trv13-2.0.1 | grounded-in:trv13-2.0.1:attributes/Hotel_Booking-V2.yaml#attribute_set.search.context.bap_uri._description
anchor.transaction-context | sent-by | "BAP" | basis:declared | asof:trv13-2.0.1 | grounded-in:trv13-2.0.1:attributes/Hotel_Booking-V2.yaml#attribute_set.search.context._description
anchor.transaction-context | scoped-to | anchor.on-search | basis:declared | asof:trv13-2.0.1 | grounded-in:trv13-2.0.1:attributes/Hotel_Booking-V2.yaml#attribute_set.on_search.context._description
anchor.protocol-version | constrains | anchor.trv13 | basis:declared | asof:trv13-2.0.1 | grounded-in:trv13-2.0.1:validations/index.yaml#_TESTS_.search[SEARCH_CONTEXT].version
anchor.search-intent | sent-by | "BAP" | basis:declared | asof:trv13-2.0.1 | grounded-in:trv13-2.0.1:attributes/Hotel_Booking-V2.yaml#attribute_set.search.message.intent._description
anchor.search-intent | has-slot | anchor.stay-date-range | basis:declared | asof:trv13-2.0.1 | grounded-in:trv13-2.0.1:attributes/Hotel_Booking-V2.yaml#attribute_set.search.message.intent.category.time._description
anchor.search-intent | has-slot | anchor.provider-filter | basis:declared | asof:trv13-2.0.1 | grounded-in:trv13-2.0.1:attributes/Hotel_Booking-V2.yaml#attribute_set.search.message.intent.provider._description
anchor.provider-filter | not-requires | anchor.provider-id | basis:declared | asof:trv13-2.0.1 | grounded-in:trv13-2.0.1:attributes/Hotel_Booking-V2.yaml#attribute_set.search.message.intent.provider.id._description
anchor.search-intent | not-requires | anchor.fulfillment-stop | basis:declared | asof:trv13-2.0.1 | grounded-in:trv13-2.0.1:attributes/Hotel_Booking-V2.yaml#attribute_set.search.message.intent.fulfillment._description

anchor.route-serviceability-error | isa | anchor.error-code | basis:declared | asof:trv13-2.0.1 | grounded-in:trv13-2.0.1:errors/index.yaml#code[90201]
anchor.route-serviceability-error | sent-by | "BPP" | basis:declared | asof:trv13-2.0.1 | grounded-in:trv13-2.0.1:errors/index.yaml#code[90201].From
anchor.unserviceable-location | causes | anchor.route-serviceability-error | basis:declared | asof:trv13-2.0.1 | grounded-in:trv13-2.0.1:errors/index.yaml#code[90201].Description
anchor.tracking-not-enabled-error | isa | anchor.error-code | basis:declared | asof:trv13-2.0.1 | grounded-in:trv13-2.0.1:errors/index.yaml#code[90202]
anchor.tracking-not-enabled-error | sent-by | "BPP" | basis:declared | asof:trv13-2.0.1 | grounded-in:trv13-2.0.1:errors/index.yaml#code[90202].From
anchor.track | causes | anchor.tracking-not-enabled-error | basis:declared | asof:trv13-2.0.1 | grounded-in:trv13-2.0.1:errors/index.yaml#code[90202].Description
anchor.error-code | not-scoped-to | anchor.cancel | basis:declared | asof:trv13-2.0.1 | grounded-in:trv13-2.0.1:errors/index.yaml#code

anchor.tag-group | has-slot | anchor.tag-list | basis:declared | asof:trv13-2.0.1 | !untethered
anchor.tag-list | isa | anchor.base-deviation | basis:declared | asof:trv13-2.0.1 | !untethered
anchor.tag-list | constrains | anchor.sub-tag-code | basis:declared | asof:trv13-2.0.1 | !untethered

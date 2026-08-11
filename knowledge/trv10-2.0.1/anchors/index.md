# Anchors — interned meanings

> Rebuilt from `atoms.md` for `trv10-2.0.1` (structural + Stage E). One row per interned
> meaning; `grounded-in` is the position the meaning was first interned at.

| handle | meaning | grounded-in | asof |
|---|---|---|---|
| anchor.action | action | - | trv10-2.0.1 |
| anchor.api-endpoint | api endpoint | workbench:frames/api-service.md | trv10-2.0.1 |
| anchor.attribute-dictionary | attribute dictionary | workbench:frames/spec-logic.md | trv10-2.0.1 |
| anchor.authorization-status | authorization status | trv10-2.0.1:validations/index.yaml#_TESTS_.select[fulfillments_Tests]._RETURN_[fulfillments_Enums_Tests]._RETURN_[VALID_ENUM_message_order_fulfillments_stops_authorization_status] | trv10-2.0.1 |
| anchor.authorization-type | authorization type | trv10-2.0.1:attributes/Ride_hailing.yaml#attribute_set.on_confirm.message.order.fulfillments.stops.authorization.type | trv10-2.0.1 |
| anchor.bap | bap | workbench:frames/ondc-protocol.md | trv10-2.0.1 |
| anchor.beckn-object | beckn object | - | trv10-2.0.1 |
| anchor.beckn-state | beckn state | - | trv10-2.0.1 |
| anchor.beckn-tag | beckn tag | - | trv10-2.0.1 |
| anchor.bpp | bpp | - | trv10-2.0.1 |
| anchor.cancel | cancel | trv10-2.0.1:actions/index.yaml#supportedActions.cancel | trv10-2.0.1 |
| anchor.cancellation-fee | cancellation fee | trv10-2.0.1:attributes/Ride_hailing.yaml#attribute_set.on_init.message.order.cancellation_terms.cancellation_fee | trv10-2.0.1 |
| anchor.cancellation-phase | cancellation phase | anchor.rider-initiated-cancellation | trv10-2.0.1 |
| anchor.cancellation-reason-code | cancellation reason code | trv10-2.0.1:attributes/Ride_hailing.yaml#attribute_set.cancel.message.cancellation_reason_id | trv10-2.0.1 |
| anchor.cancellation-reason-input | cancellation reason input | trv10-2.0.1:flows/Ride-hailing/OnDemand_Ride_cancellation_by_rider.yaml#steps[cancel].mock.inputs.jsonSchema.properties.cancellation_reason_id.enum | trv10-2.0.1 |
| anchor.cancellation-terms | cancellation terms | trv10-2.0.1:attributes/Ride_hailing.yaml#attribute_set.on_init.message.order.cancellation_terms | trv10-2.0.1 |
| anchor.cancelled-by | cancelled by | trv10-2.0.1:attributes/Ride_hailing.yaml#attribute_set.on_cancel.message.order.cancellation.cancelled_by | trv10-2.0.1 |
| anchor.catalog-tag-code | catalog tag code | trv10-2.0.1:validations/index.yaml#_TESTS_.on_search[tags_Tests]._RETURN_[tags_Tags_Tests]._RETURN_[VALIDATE_TAG_message_catalog_tags_descriptor_code] | trv10-2.0.1 |
| anchor.category-descriptor-code | category descriptor code | trv10-2.0.1:validations/index.yaml#_TESTS_.search[category_Tests]._RETURN_[category_Enums_Tests]._RETURN_[VALID_ENUM_message_intent_category_descriptor_code] | trv10-2.0.1 |
| anchor.complainant-action | complainant action | trv10-2.0.1:validations/index.yaml#_TESTS_.issue[ISSUE_VALIDATION_VERSION_100]._RETURN_[ISSUE_VALIDATION_OPEN]._RETURN_[REQUIRED_ISSUE_ACTIONS_OPEN] | trv10-2.0.1 |
| anchor.confirm | confirm | trv10-2.0.1:actions/index.yaml#supportedActions.confirm | trv10-2.0.1 |
| anchor.confirm-cancel | confirm cancel | trv10-2.0.1:flows/Ride-hailing/OnDemand_Ride_cancellation_by_rider.yaml#steps[cancel_hard] | trv10-2.0.1 |
| anchor.country-code | country code | trv10-2.0.1:attributes/Ride_hailing.yaml#attribute_set.search.context.location.country.code | trv10-2.0.1 |
| anchor.cross-operator-ride-comparison | cross operator ride comparison | - | trv10-2.0.1 |
| anchor.delivery-pickup | delivery pickup | trv10-2.0.1:attributes/Ride_hailing.yaml#attribute_set.on_search.message.catalog.providers.fulfillments.type | trv10-2.0.1 |
| anchor.disability-tag-code | disability tag code | trv10-2.0.1:validations/index.yaml#_TESTS_.on_select[items_Tests]._RETURN_[items_Tags_Tests]._RETURN_[VALIDATE_TAG_message_order_items_tags_descriptor_code] | trv10-2.0.1 |
| anchor.documentation-only | documentation only | - | trv10-2.0.1 |
| anchor.domain-code | domain code | trv10-2.0.1:attributes/Ride_hailing.yaml#attribute_set.search.context.domain | trv10-2.0.1 |
| anchor.driver | driver | trv10-2.0.1:docs/overview.md#real-world-actors | trv10-2.0.1 |
| anchor.driver-assignment | driver assignment | trv10-2.0.1:docs/overview.md#key-concepts | trv10-2.0.1 |
| anchor.driver-assignment-on-confirm | driver assignment on confirm | trv10-2.0.1:flows/Ride-hailing/OnDemand_Assign_driver_on_onconfirm.yaml#steps[on_confirm] | trv10-2.0.1 |
| anchor.driver-assignment-post-confirm | driver assignment post confirm | trv10-2.0.1:flows/Ride-hailing/OnDemand_Assign_driver_post_onconfirm.yaml#steps[on_update_ride] | trv10-2.0.1 |
| anchor.driver-initiated-cancellation | driver initiated cancellation | trv10-2.0.1:flows/Ride-hailing/OnDemand_Ride_cancellation_by_driver.yaml#steps[on_cancel_async] | trv10-2.0.1 |
| anchor.driver-not-assigned | driver not assigned | trv10-2.0.1:errors/index.yaml#code[90203] | trv10-2.0.1 |
| anchor.driver-not-found | driver not found | trv10-2.0.1:errors/index.yaml#code[90203] | trv10-2.0.1 |
| anchor.driver-not-found-on-confirm | driver not found on confirm | trv10-2.0.1:flows/Ride-hailing/Driver_not_found_on_onconfirm.yaml#steps[on_confirm_driver_not_found] | trv10-2.0.1 |
| anchor.driver-not-found-post-confirm | driver not found post confirm | trv10-2.0.1:flows/Ride-hailing/Driver_not_found_post_onconfirm.yaml#steps[on_cancel_rider_not_found] | trv10-2.0.1 |
| anchor.enum-check | enum check | workbench:frames/validation-layers.md | trv10-2.0.1 |
| anchor.enum-set | enum set | workbench:frames/validation-layers.md | trv10-2.0.1 |
| anchor.error-90201 | error 90201 | trv10-2.0.1:errors/index.yaml#code[90201] | trv10-2.0.1 |
| anchor.error-90202 | error 90202 | trv10-2.0.1:errors/index.yaml#code[90202] | trv10-2.0.1 |
| anchor.error-90203 | error 90203 | trv10-2.0.1:errors/index.yaml#code[90203] | trv10-2.0.1 |
| anchor.error-code | error code | - | trv10-2.0.1 |
| anchor.female-driver-assignment | female driver assignment | trv10-2.0.1:flows/Ride-hailing/OnDemand_Female_driver_flow.yaml#steps[on_search_female] | trv10-2.0.1 |
| anchor.female-driver-preference | female driver preference | trv10-2.0.1:specs/openapi.yaml#paths./search.post.requestBody.content.application/json.schema.properties.message.properties.intent.properties.fulfillment.properties.agent.properties.person.properties.gender | trv10-2.0.1 |
| anchor.flow-driver-not-found-on-onconfirm | flow driver not found on onconfirm | trv10-2.0.1:flows/index.yaml#flows[Driver_not_found_on_onconfirm] | trv10-2.0.1 |
| anchor.flow-driver-not-found-post-onconfirm | flow driver not found post onconfirm | trv10-2.0.1:flows/index.yaml#flows[Driver_not_found_post_onconfirm] | trv10-2.0.1 |
| anchor.flow-ondemand-assign-driver-on-onconfirm | flow ondemand assign driver on onconfirm | trv10-2.0.1:flows/index.yaml#flows[OnDemand_Assign_driver_on_onconfirm] | trv10-2.0.1 |
| anchor.flow-ondemand-assign-driver-on-onconfirm-with-igm-1-0-0 | flow ondemand assign driver on onconfirm with igm 1 0 0 | trv10-2.0.1:flows/index.yaml#flows[OnDemand_Assign_driver_on_onconfirm_with_IGM(1.0.0)] | trv10-2.0.1 |
| anchor.flow-ondemand-assign-driver-post-onconfirm | flow ondemand assign driver post onconfirm | trv10-2.0.1:flows/index.yaml#flows[OnDemand_Assign_driver_post_onconfirm] | trv10-2.0.1 |
| anchor.flow-ondemand-assign-driver-post-onconfirmselfpickup | flow ondemand assign driver post onconfirmselfpickup | trv10-2.0.1:flows/index.yaml#flows[OnDemand_Assign_driver_post_onconfirmSelfPickup] | trv10-2.0.1 |
| anchor.flow-ondemand-female-driver-flow | flow ondemand female driver flow | trv10-2.0.1:flows/index.yaml#flows[OnDemand_Female_driver_flow] | trv10-2.0.1 |
| anchor.flow-ondemand-journey-updation-flow | flow ondemand journey updation flow | trv10-2.0.1:flows/index.yaml#flows[OnDemand_journey_updation_flow] | trv10-2.0.1 |
| anchor.flow-ondemand-ride-cancellation-by-driver | flow ondemand ride cancellation by driver | trv10-2.0.1:flows/index.yaml#flows[OnDemand_Ride_cancellation_by_driver] | trv10-2.0.1 |
| anchor.flow-ondemand-ride-cancellation-by-rider | flow ondemand ride cancellation by rider | trv10-2.0.1:flows/index.yaml#flows[OnDemand_Ride_cancellation_by_rider] | trv10-2.0.1 |
| anchor.flow-step | flow step | workbench:frames/mock-runner-lib.md | trv10-2.0.1 |
| anchor.flow-technical-cancellation-flow | flow technical cancellation flow | trv10-2.0.1:flows/index.yaml#flows[Technical_cancellation_flow] | trv10-2.0.1 |
| anchor.fulfillment-agent | fulfillment agent | trv10-2.0.1:attributes/Ride_hailing.yaml#attribute_set.on_confirm.message.order.fulfillments.agent.person.gender | trv10-2.0.1 |
| anchor.fulfillment-customer | fulfillment customer | trv10-2.0.1:attributes/Ride_hailing.yaml#attribute_set.on_confirm.message.order.fulfillments.customer | trv10-2.0.1 |
| anchor.fulfillment-mode | fulfillment mode | - | trv10-2.0.1 |
| anchor.fulfillment-state | fulfillment state | trv10-2.0.1:attributes/Ride_hailing.yaml#attribute_set.on_confirm.message.order.fulfillments.state | trv10-2.0.1 |
| anchor.fulfillment-stop | fulfillment stop | trv10-2.0.1:attributes/Ride_hailing.yaml#attribute_set.on_confirm.message.order.fulfillments.stops | trv10-2.0.1 |
| anchor.fulfillment-tag-code | fulfillment tag code | trv10-2.0.1:validations/index.yaml#_TESTS_.confirm[fulfillments_Tests]._RETURN_[fulfillments_Tags_Tests]._RETURN_[VALIDATE_TAG_message_order_fulfillments_tags_descriptor_code] | trv10-2.0.1 |
| anchor.fulfillment-type | fulfillment type | trv10-2.0.1:attributes/Ride_hailing.yaml#attribute_set.on_search.message.catalog.providers.fulfillments.type | trv10-2.0.1 |
| anchor.fulfillment-vehicle | fulfillment vehicle | trv10-2.0.1:attributes/Ride_hailing.yaml#attribute_set.on_confirm.message.order.fulfillments.vehicle | trv10-2.0.1 |
| anchor.fulfilment-failure | fulfilment failure | - | trv10-2.0.1 |
| anchor.grievance-management | grievance management | - | trv10-2.0.1 |
| anchor.igm | igm | trv10-2.0.1:flows/Ride-hailing/OnDemand_Assign_driver_on_onconfirm_with_IGM_1_0_0_.yaml#steps[issue_open_100] | trv10-2.0.1 |
| anchor.igm-v100 | igm v100 | trv10-2.0.1:validations/index.yaml#_TESTS_.issue[ISSUE_VALIDATION_VERSION_100] | trv10-2.0.1 |
| anchor.igm-v200 | igm v200 | trv10-2.0.1:validations/index.yaml#_TESTS_.issue[ISSUE_VALIDATION_VERSION_200] | trv10-2.0.1 |
| anchor.init | init | trv10-2.0.1:actions/index.yaml#supportedActions.init | trv10-2.0.1 |
| anchor.intent-tag-code | intent tag code | trv10-2.0.1:validations/index.yaml#_TESTS_.search[tags_Tests]._RETURN_[tags_Tags_Tests]._RETURN_[VALIDATE_TAG_message_intent_tags_descriptor_code] | trv10-2.0.1 |
| anchor.interned-vocabulary | interned vocabulary | - | trv10-2.0.1 |
| anchor.issue | issue | trv10-2.0.1:actions/index.yaml#supportedActions.issue | trv10-2.0.1 |
| anchor.issue-actor-type | issue actor type | trv10-2.0.1:validations/index.yaml#_TESTS_.issue[ISSUE_VALIDATION_VERSION_200]._RETURN_[REQUIRED_MESSAGE_TYPE] | trv10-2.0.1 |
| anchor.issue-level | issue level | trv10-2.0.1:validations/index.yaml#_TESTS_.issue[ISSUE_VALIDATION_VERSION_200]._RETURN_[REQUIRED_MESSAGE_LEVEL] | trv10-2.0.1 |
| anchor.issue-ref-type | issue ref type | trv10-2.0.1:validations/index.yaml#_TESTS_.issue[ISSUE_VALIDATION_VERSION_200]._RETURN_[REQUIRED_MESSAGE_REF_TYPE] | trv10-2.0.1 |
| anchor.issue-resolution | issue resolution | - | trv10-2.0.1 |
| anchor.issue-status | issue status | trv10-2.0.1:validations/index.yaml#_TESTS_.issue[ISSUE_VALIDATION_VERSION_200]._RETURN_[REQUIRED_MESSAGE_STATUS] | trv10-2.0.1 |
| anchor.item-descriptor-code | item descriptor code | trv10-2.0.1:attributes/Ride_hailing.yaml#attribute_set.on_select.message.order.items.descriptor.code | trv10-2.0.1 |
| anchor.item-tag-code | item tag code | trv10-2.0.1:validations/index.yaml#_TESTS_.on_select[items_Tests]._RETURN_[items_Tags_Tests]._RETURN_[VALIDATE_TAG_message_order_items_tags_descriptor_code] | trv10-2.0.1 |
| anchor.journey-progress | journey progress | trv10-2.0.1:flows/Ride-hailing/OnDemand_journey_updation_flow.yaml#steps[on_status_unsolicited] | trv10-2.0.1 |
| anchor.l1-validation | l1 validation | - | trv10-2.0.1 |
| anchor.live-tracking | live tracking | trv10-2.0.1:flows/Ride-hailing/OnDemand_Assign_driver_on_onconfirm.yaml#steps[on_track_ride] | trv10-2.0.1 |
| anchor.mandatory-flow | mandatory flow | workbench:frames/flow-usecase.md | trv10-2.0.1 |
| anchor.multi-provider-discovery | multi provider discovery | trv10-2.0.1:docs/overview.md#summary | trv10-2.0.1 |
| anchor.on-cancel | on cancel | trv10-2.0.1:actions/index.yaml#supportedActions.on_cancel | trv10-2.0.1 |
| anchor.on-confirm | on confirm | trv10-2.0.1:actions/index.yaml#supportedActions.on_confirm | trv10-2.0.1 |
| anchor.on-demand-matching | on demand matching | trv10-2.0.1:docs/overview.md#key-concepts | trv10-2.0.1 |
| anchor.on-demand-mobility | on demand mobility | - | trv10-2.0.1 |
| anchor.on-init | on init | trv10-2.0.1:actions/index.yaml#supportedActions.on_init | trv10-2.0.1 |
| anchor.on-issue | on issue | trv10-2.0.1:actions/index.yaml#supportedActions.on_issue | trv10-2.0.1 |
| anchor.on-issue-status | on issue status | trv10-2.0.1:actions/index.yaml#supportedActions.on_issue_status | trv10-2.0.1 |
| anchor.on-search | on search | trv10-2.0.1:actions/index.yaml#supportedActions.on_search | trv10-2.0.1 |
| anchor.on-select | on select | trv10-2.0.1:actions/index.yaml#supportedActions.on_select | trv10-2.0.1 |
| anchor.on-status | on status | trv10-2.0.1:actions/index.yaml#supportedActions.on_status | trv10-2.0.1 |
| anchor.on-track | on track | trv10-2.0.1:actions/index.yaml#supportedActions.on_track | trv10-2.0.1 |
| anchor.on-update | on update | trv10-2.0.1:actions/index.yaml#supportedActions.on_update | trv10-2.0.1 |
| anchor.ondc-domain | ondc domain | - | trv10-2.0.1 |
| anchor.order-billing | order billing | trv10-2.0.1:attributes/Ride_hailing.yaml#attribute_set.init.message.order.billing | trv10-2.0.1 |
| anchor.order-cancellation | order cancellation | trv10-2.0.1:attributes/Ride_hailing.yaml#attribute_set.on_cancel.message.order.cancellation | trv10-2.0.1 |
| anchor.order-object | order object | - | trv10-2.0.1 |
| anchor.order-payment | order payment | trv10-2.0.1:attributes/Ride_hailing.yaml#attribute_set.on_confirm.message.order.payments | trv10-2.0.1 |
| anchor.order-provider | order provider | trv10-2.0.1:attributes/Ride_hailing.yaml#attribute_set.on_confirm.message.order.provider | trv10-2.0.1 |
| anchor.order-quote | order quote | trv10-2.0.1:attributes/Ride_hailing.yaml#attribute_set.on_confirm.message.order.quote | trv10-2.0.1 |
| anchor.order-status-code | order status code | trv10-2.0.1:attributes/Ride_hailing.yaml#attribute_set.on_confirm.message.order.status | trv10-2.0.1 |
| anchor.order-tag-code | order tag code | trv10-2.0.1:validations/index.yaml#_TESTS_.confirm[tags_Tests]._RETURN_[tags_Tags_Tests]._RETURN_[VALIDATE_TAG_message_order_tags_descriptor_code] | trv10-2.0.1 |
| anchor.path-cancel | path cancel | trv10-2.0.1:specs/openapi.yaml#paths./cancel | trv10-2.0.1 |
| anchor.path-confirm | path confirm | trv10-2.0.1:specs/openapi.yaml#paths./confirm | trv10-2.0.1 |
| anchor.path-init | path init | trv10-2.0.1:specs/openapi.yaml#paths./init | trv10-2.0.1 |
| anchor.path-issue | path issue | trv10-2.0.1:specs/openapi.yaml#paths./issue | trv10-2.0.1 |
| anchor.path-on-cancel | path on cancel | trv10-2.0.1:specs/openapi.yaml#paths./on_cancel | trv10-2.0.1 |
| anchor.path-on-confirm | path on confirm | trv10-2.0.1:specs/openapi.yaml#paths./on_confirm | trv10-2.0.1 |
| anchor.path-on-init | path on init | trv10-2.0.1:specs/openapi.yaml#paths./on_init | trv10-2.0.1 |
| anchor.path-on-issue | path on issue | trv10-2.0.1:specs/openapi.yaml#paths./on_issue | trv10-2.0.1 |
| anchor.path-on-issue-status | path on issue status | trv10-2.0.1:specs/openapi.yaml#paths./on_issue_status | trv10-2.0.1 |
| anchor.path-on-search | path on search | trv10-2.0.1:specs/openapi.yaml#paths./on_search | trv10-2.0.1 |
| anchor.path-on-select | path on select | trv10-2.0.1:specs/openapi.yaml#paths./on_select | trv10-2.0.1 |
| anchor.path-on-status | path on status | trv10-2.0.1:specs/openapi.yaml#paths./on_status | trv10-2.0.1 |
| anchor.path-on-track | path on track | trv10-2.0.1:specs/openapi.yaml#paths./on_track | trv10-2.0.1 |
| anchor.path-on-update | path on update | trv10-2.0.1:specs/openapi.yaml#paths./on_update | trv10-2.0.1 |
| anchor.path-search | path search | trv10-2.0.1:specs/openapi.yaml#paths./search | trv10-2.0.1 |
| anchor.path-select | path select | trv10-2.0.1:specs/openapi.yaml#paths./select | trv10-2.0.1 |
| anchor.path-status | path status | trv10-2.0.1:specs/openapi.yaml#paths./status | trv10-2.0.1 |
| anchor.path-track | path track | trv10-2.0.1:specs/openapi.yaml#paths./track | trv10-2.0.1 |
| anchor.path-update | path update | trv10-2.0.1:specs/openapi.yaml#paths./update | trv10-2.0.1 |
| anchor.payment-collected-by | payment collected by | trv10-2.0.1:attributes/Ride_hailing.yaml#attribute_set.init.message.order.payments.collected_by | trv10-2.0.1 |
| anchor.payment-status | payment status | trv10-2.0.1:attributes/Ride_hailing.yaml#attribute_set.init.message.order.payments.status | trv10-2.0.1 |
| anchor.payment-type | payment type | trv10-2.0.1:attributes/Ride_hailing.yaml#attribute_set.init.message.order.payments.type | trv10-2.0.1 |
| anchor.provider-catalog | provider catalog | trv10-2.0.1:attributes/Ride_hailing.yaml#attribute_set.on_search.message.catalog | trv10-2.0.1 |
| anchor.provider-initiated-cancellation | provider initiated cancellation | trv10-2.0.1:flows/Ride-hailing/OnDemand_Ride_cancellation_by_driver.yaml#steps[on_cancel_async] | trv10-2.0.1 |
| anchor.quote-breakup | quote breakup | trv10-2.0.1:attributes/Ride_hailing.yaml#attribute_set.on_confirm.message.order.quote.breakup | trv10-2.0.1 |
| anchor.quote-breakup-title | quote breakup title | trv10-2.0.1:attributes/Ride_hailing.yaml#attribute_set.on_select.message.order.quote.breakup.title | trv10-2.0.1 |
| anchor.regex-check | regex check | workbench:frames/validation-layers.md | trv10-2.0.1 |
| anchor.reportable-flow | reportable flow | workbench:frames/flow-usecase.md | trv10-2.0.1 |
| anchor.required-field-check | required field check | workbench:frames/validation-layers.md | trv10-2.0.1 |
| anchor.respondent-action | respondent action | trv10-2.0.1:validations/index.yaml#_TESTS_.on_issue[ON_ISSUE_VALIDATION_VERSION_100]._RETURN_[REQUIRED_RESPONDENT_ACTION] | trv10-2.0.1 |
| anchor.ride-cancellation | ride cancellation | trv10-2.0.1:attributes/Ride_hailing.yaml#attribute_set.on_cancel.message.order.cancellation | trv10-2.0.1 |
| anchor.ride-fulfillment | ride fulfillment | trv10-2.0.1:attributes/Ride_hailing.yaml#attribute_set.on_confirm.message.order.fulfillments | trv10-2.0.1 |
| anchor.ride-hailing | ride hailing | trv10-2.0.1:docs/overview.md#sector-purpose | trv10-2.0.1 |
| anchor.ride-hailing-journey | ride hailing journey | workbench:frames/flow-usecase.md | trv10-2.0.1 |
| anchor.ride-hailing-provider | ride hailing provider | trv10-2.0.1:docs/overview.md#real-world-actors | trv10-2.0.1 |
| anchor.ride-hailing-usecase | ride hailing usecase | trv10-2.0.1:flows/index.yaml#flows[Driver_not_found_on_onconfirm].usecase | trv10-2.0.1 |
| anchor.ride-item | ride item | trv10-2.0.1:attributes/Ride_hailing.yaml#attribute_set.on_confirm.message.order.items | trv10-2.0.1 |
| anchor.ride-order | ride order | trv10-2.0.1:attributes/Ride_hailing.yaml#attribute_set.on_confirm.message.order | trv10-2.0.1 |
| anchor.ride-preference | ride preference | trv10-2.0.1:flows/Ride-hailing/OnDemand_Female_driver_flow.yaml#steps[on_search_female] | trv10-2.0.1 |
| anchor.ride-state-code | ride state code | trv10-2.0.1:attributes/Ride_hailing.yaml#attribute_set.on_confirm.message.order.fulfillments.state.descriptor.code | trv10-2.0.1 |
| anchor.rider | rider | trv10-2.0.1:docs/overview.md#real-world-actors | trv10-2.0.1 |
| anchor.rider-gender-preference | rider gender preference | trv10-2.0.1:flows/Ride-hailing/OnDemand_Female_driver_flow.yaml#steps[search_ride_female].examples[0].payload.message.intent.fulfillment.customer.person.gender | trv10-2.0.1 |
| anchor.rider-initiated-cancellation | rider initiated cancellation | trv10-2.0.1:flows/Ride-hailing/OnDemand_Ride_cancellation_by_rider.yaml#steps[cancel] | trv10-2.0.1 |
| anchor.route-not-serviceable | route not serviceable | trv10-2.0.1:errors/index.yaml#code[90201] | trv10-2.0.1 |
| anchor.runtime-behavior | runtime behavior | - | trv10-2.0.1 |
| anchor.runtime-concept | runtime concept | - | trv10-2.0.1 |
| anchor.search | search | trv10-2.0.1:actions/index.yaml#supportedActions.search | trv10-2.0.1 |
| anchor.search-intent | search intent | trv10-2.0.1:attributes/Ride_hailing.yaml#attribute_set.search.message.intent | trv10-2.0.1 |
| anchor.select | select | trv10-2.0.1:actions/index.yaml#supportedActions.select | trv10-2.0.1 |
| anchor.self-pickup | self pickup | trv10-2.0.1:attributes/Ride_hailing.yaml#attribute_set.on_search.message.catalog.providers.fulfillments.type | trv10-2.0.1 |
| anchor.single-operator-platform | single operator platform | - | trv10-2.0.1 |
| anchor.skip-guard | skip guard | workbench:frames/validation-layers.md | trv10-2.0.1 |
| anchor.soft-cancel | soft cancel | trv10-2.0.1:flows/Ride-hailing/OnDemand_Ride_cancellation_by_rider.yaml#steps[cancel] | trv10-2.0.1 |
| anchor.status | status | trv10-2.0.1:actions/index.yaml#supportedActions.status | trv10-2.0.1 |
| anchor.step-driver-not-found-on-onconfirm-confirm | step driver not found on onconfirm confirm | trv10-2.0.1:flows/Ride-hailing/Driver_not_found_on_onconfirm.yaml#steps[on_confirm_driver_not_found].responseFor | trv10-2.0.1 |
| anchor.step-driver-not-found-on-onconfirm-on-confirm-driver-not-found | step driver not found on onconfirm on confirm driver not found | trv10-2.0.1:flows/Ride-hailing/Driver_not_found_on_onconfirm.yaml#steps[on_confirm_driver_not_found] | trv10-2.0.1 |
| anchor.step-driver-not-found-post-onconfirm-confirm | step driver not found post onconfirm confirm | trv10-2.0.1:flows/Ride-hailing/Driver_not_found_post_onconfirm.yaml#steps[on_confirm_driver_not_assigned].responseFor | trv10-2.0.1 |
| anchor.step-driver-not-found-post-onconfirm-on-cancel-rider-not-found | step driver not found post onconfirm on cancel rider not found | trv10-2.0.1:flows/Ride-hailing/Driver_not_found_post_onconfirm.yaml#steps[on_cancel_rider_not_found] | trv10-2.0.1 |
| anchor.step-driver-not-found-post-onconfirm-on-confirm-driver-not-assigned | step driver not found post onconfirm on confirm driver not assigned | trv10-2.0.1:flows/Ride-hailing/Driver_not_found_post_onconfirm.yaml#steps[on_confirm_driver_not_assigned] | trv10-2.0.1 |
| anchor.step-ondemand-assign-driver-on-onconfirm-confirm | step ondemand assign driver on onconfirm confirm | trv10-2.0.1:flows/Ride-hailing/OnDemand_Assign_driver_on_onconfirm.yaml#steps[on_confirm].responseFor | trv10-2.0.1 |
| anchor.step-ondemand-assign-driver-on-onconfirm-on-confirm | step ondemand assign driver on onconfirm on confirm | trv10-2.0.1:flows/Ride-hailing/OnDemand_Assign_driver_on_onconfirm.yaml#steps[on_confirm] | trv10-2.0.1 |
| anchor.step-ondemand-assign-driver-on-onconfirm-with-igm-1-0-0-issue-close-100 | step ondemand assign driver on onconfirm with igm 1 0 0 issue close 100 | trv10-2.0.1:flows/Ride-hailing/OnDemand_Assign_driver_on_onconfirm_with_IGM_1_0_0_.yaml#steps[issue_close_100] | trv10-2.0.1 |
| anchor.step-ondemand-assign-driver-on-onconfirm-with-igm-1-0-0-issue-open-100 | step ondemand assign driver on onconfirm with igm 1 0 0 issue open 100 | trv10-2.0.1:flows/Ride-hailing/OnDemand_Assign_driver_on_onconfirm_with_IGM_1_0_0_.yaml#steps[issue_open_100] | trv10-2.0.1 |
| anchor.step-ondemand-assign-driver-on-onconfirm-with-igm-1-0-0-on-issue-processing-100 | step ondemand assign driver on onconfirm with igm 1 0 0 on issue processing 100 | trv10-2.0.1:flows/Ride-hailing/OnDemand_Assign_driver_on_onconfirm_with_IGM_1_0_0_.yaml#steps[on_issue_processing_100] | trv10-2.0.1 |
| anchor.step-ondemand-assign-driver-on-onconfirm-with-igm-1-0-0-on-issue-resolved-100 | step ondemand assign driver on onconfirm with igm 1 0 0 on issue resolved 100 | trv10-2.0.1:flows/Ride-hailing/OnDemand_Assign_driver_on_onconfirm_with_IGM_1_0_0_.yaml#steps[on_issue_resolved_100] | trv10-2.0.1 |
| anchor.step-ondemand-assign-driver-post-onconfirm-on-update-ride | step ondemand assign driver post onconfirm on update ride | trv10-2.0.1:flows/Ride-hailing/OnDemand_Assign_driver_post_onconfirm.yaml#steps[on_update_ride] | trv10-2.0.1 |
| anchor.step-ondemand-assign-driver-post-onconfirmselfpickup-on-update-ride | step ondemand assign driver post onconfirmselfpickup on update ride | trv10-2.0.1:flows/Ride-hailing/OnDemand_Assign_driver_post_onconfirmSelfPickup.yaml#steps[on_update_ride] | trv10-2.0.1 |
| anchor.step-ondemand-female-driver-flow-on-search-female | step ondemand female driver flow on search female | trv10-2.0.1:flows/Ride-hailing/OnDemand_Female_driver_flow.yaml#steps[on_search_female] | trv10-2.0.1 |
| anchor.step-ondemand-female-driver-flow-search-ride-female | step ondemand female driver flow search ride female | trv10-2.0.1:flows/Ride-hailing/OnDemand_Female_driver_flow.yaml#steps[search_ride_female] | trv10-2.0.1 |
| anchor.step-ondemand-journey-updation-flow-on-status-solicited | step ondemand journey updation flow on status solicited | trv10-2.0.1:flows/Ride-hailing/OnDemand_journey_updation_flow.yaml#steps[on_status_solicited] | trv10-2.0.1 |
| anchor.step-ondemand-ride-cancellation-by-driver-on-cancel-async | step ondemand ride cancellation by driver on cancel async | trv10-2.0.1:flows/Ride-hailing/OnDemand_Ride_cancellation_by_driver.yaml#steps[on_cancel_async] | trv10-2.0.1 |
| anchor.step-ondemand-ride-cancellation-by-rider-cancel | step ondemand ride cancellation by rider cancel | trv10-2.0.1:flows/Ride-hailing/OnDemand_Ride_cancellation_by_rider.yaml#steps[cancel] | trv10-2.0.1 |
| anchor.step-ondemand-ride-cancellation-by-rider-cancel-hard | step ondemand ride cancellation by rider cancel hard | trv10-2.0.1:flows/Ride-hailing/OnDemand_Ride_cancellation_by_rider.yaml#steps[cancel_hard] | trv10-2.0.1 |
| anchor.step-ondemand-ride-cancellation-by-rider-on-cancel-hard | step ondemand ride cancellation by rider on cancel hard | trv10-2.0.1:flows/Ride-hailing/OnDemand_Ride_cancellation_by_rider.yaml#steps[on_cancel_hard] | trv10-2.0.1 |
| anchor.step-ondemand-ride-cancellation-by-rider-on-cancel-ride-cancel | step ondemand ride cancellation by rider on cancel ride cancel | trv10-2.0.1:flows/Ride-hailing/OnDemand_Ride_cancellation_by_rider.yaml#steps[on_cancel_ride_cancel] | trv10-2.0.1 |
| anchor.step-technical-cancellation-flow-confirm | step technical cancellation flow confirm | trv10-2.0.1:flows/Ride-hailing/Technical_cancellation_flow.yaml#steps[on_confirm_ride_delay].responseFor | trv10-2.0.1 |
| anchor.step-technical-cancellation-flow-on-confirm-ride-delay | step technical cancellation flow on confirm ride delay | trv10-2.0.1:flows/Ride-hailing/Technical_cancellation_flow.yaml#steps[on_confirm_ride_delay] | trv10-2.0.1 |
| anchor.stop-authorization | stop authorization | trv10-2.0.1:attributes/Ride_hailing.yaml#attribute_set.on_confirm.message.order.fulfillments.stops.authorization | trv10-2.0.1 |
| anchor.stop-type | stop type | trv10-2.0.1:attributes/Ride_hailing.yaml#attribute_set.search.message.intent.fulfillment.stops.type | trv10-2.0.1 |
| anchor.tag-check | tag check | workbench:frames/validation-layers.md | trv10-2.0.1 |
| anchor.tag-vocabulary | tag vocabulary | workbench:frames/validation-layers.md | trv10-2.0.1 |
| anchor.technical-cancellation | technical cancellation | trv10-2.0.1:flows/Ride-hailing/Technical_cancellation_flow.yaml#steps[cancel] | trv10-2.0.1 |
| anchor.track | track | trv10-2.0.1:actions/index.yaml#supportedActions.track | trv10-2.0.1 |
| anchor.transaction-actor | transaction actor | - | trv10-2.0.1 |
| anchor.transaction-entry | transaction entry | workbench:frames/flow-state-machine.md | trv10-2.0.1 |
| anchor.transaction-journey | transaction journey | - | trv10-2.0.1 |
| anchor.transaction-termination | transaction termination | - | trv10-2.0.1 |
| anchor.trv10 | trv10 | trv10-2.0.1:index.yaml#info.domain | trv10-2.0.1 |
| anchor.unsolicited-callback | unsolicited callback | workbench:frames/mock-runner-lib.md | trv10-2.0.1 |
| anchor.update | update | trv10-2.0.1:actions/index.yaml#supportedActions.update | trv10-2.0.1 |
| anchor.usecase | usecase | - | trv10-2.0.1 |
| anchor.v-confirm-enum-order-fulfillments-type | v confirm enum order fulfillments type | trv10-2.0.1:validations/index.yaml#_TESTS_.confirm[fulfillments_Tests]._RETURN_[fulfillments_Enums_Tests]._RETURN_[VALID_ENUM_message_order_fulfillments_type] | trv10-2.0.1 |
| anchor.v-confirm-fulfillments-enums-tests | v confirm fulfillments enums tests | trv10-2.0.1:validations/index.yaml#_TESTS_.confirm[fulfillments_Tests]._RETURN_[fulfillments_Enums_Tests] | trv10-2.0.1 |
| anchor.v-confirm-fulfillments-tags-tests | v confirm fulfillments tags tests | trv10-2.0.1:validations/index.yaml#_TESTS_.confirm[fulfillments_Tests]._RETURN_[fulfillments_Tags_Tests] | trv10-2.0.1 |
| anchor.v-confirm-payments-attributes-tests | v confirm payments attributes tests | trv10-2.0.1:validations/index.yaml#_TESTS_.confirm[payments_Tests]._RETURN_[payments_Attributes_Tests] | trv10-2.0.1 |
| anchor.v-confirm-payments-tests | v confirm payments tests | trv10-2.0.1:validations/index.yaml#_TESTS_.confirm[payments_Tests] | trv10-2.0.1 |
| anchor.v-confirm-req-order-payments-id | v confirm req order payments id | trv10-2.0.1:validations/index.yaml#_TESTS_.confirm[payments_Tests]._RETURN_[payments_Attributes_Tests]._RETURN_[REQUIRED_message_order_payments_id] | trv10-2.0.1 |
| anchor.v-confirm-tag-order-fulfillments-tags-descriptor-code | v confirm tag order fulfillments tags descriptor code | trv10-2.0.1:validations/index.yaml#_TESTS_.confirm[fulfillments_Tests]._RETURN_[fulfillments_Tags_Tests]._RETURN_[VALIDATE_TAG_message_order_fulfillments_tags_descriptor_code] | trv10-2.0.1 |
| anchor.v-confirm-tag-order-tags-descriptor-code | v confirm tag order tags descriptor code | trv10-2.0.1:validations/index.yaml#_TESTS_.confirm[tags_Tests]._RETURN_[tags_Tags_Tests]._RETURN_[VALIDATE_TAG_message_order_tags_descriptor_code] | trv10-2.0.1 |
| anchor.v-confirm-tags-tests | v confirm tags tests | trv10-2.0.1:validations/index.yaml#_TESTS_.confirm[tags_Tests] | trv10-2.0.1 |
| anchor.v-init-billing-tests | v init billing tests | trv10-2.0.1:validations/index.yaml#_TESTS_.init[billing_Tests] | trv10-2.0.1 |
| anchor.v-init-enum-order-fulfillments-vehicle-category | v init enum order fulfillments vehicle category | trv10-2.0.1:validations/index.yaml#_TESTS_.init[fulfillments_Tests]._RETURN_[fulfillments_Enums_Tests]._RETURN_[VALID_ENUM_message_order_fulfillments_vehicle_category] | trv10-2.0.1 |
| anchor.v-init-enum-order-payments-collected-by | v init enum order payments collected by | trv10-2.0.1:validations/index.yaml#_TESTS_.init[payments_Tests]._RETURN_[payments_Enums_Tests]._RETURN_[VALID_ENUM_message_order_payments_collected_by] | trv10-2.0.1 |
| anchor.v-init-enum-order-payments-status | v init enum order payments status | trv10-2.0.1:validations/index.yaml#_TESTS_.init[payments_Tests]._RETURN_[payments_Enums_Tests]._RETURN_[VALID_ENUM_message_order_payments_status] | trv10-2.0.1 |
| anchor.v-init-enum-order-payments-type | v init enum order payments type | trv10-2.0.1:validations/index.yaml#_TESTS_.init[payments_Tests]._RETURN_[payments_Enums_Tests]._RETURN_[VALID_ENUM_message_order_payments_type] | trv10-2.0.1 |
| anchor.v-init-fulfillments-attributes-tests | v init fulfillments attributes tests | trv10-2.0.1:validations/index.yaml#_TESTS_.init[fulfillments_Tests]._RETURN_[fulfillments_Attributes_Tests] | trv10-2.0.1 |
| anchor.v-init-payments-enums-tests | v init payments enums tests | trv10-2.0.1:validations/index.yaml#_TESTS_.init[payments_Tests]._RETURN_[payments_Enums_Tests] | trv10-2.0.1 |
| anchor.v-init-req-order-fulfillments-customer-contact-phone | v init req order fulfillments customer contact phone | trv10-2.0.1:validations/index.yaml#_TESTS_.init[fulfillments_Tests]._RETURN_[fulfillments_Attributes_Tests]._RETURN_[REQUIRED_message_order_fulfillments_customer_contact_phone] | trv10-2.0.1 |
| anchor.v-init-req-order-fulfillments-customer-person-name | v init req order fulfillments customer person name | trv10-2.0.1:validations/index.yaml#_TESTS_.init[fulfillments_Tests]._RETURN_[fulfillments_Attributes_Tests]._RETURN_[REQUIRED_message_order_fulfillments_customer_person_name] | trv10-2.0.1 |
| anchor.v-init-req-order-fulfillments-id | v init req order fulfillments id | trv10-2.0.1:validations/index.yaml#_TESTS_.init[fulfillments_Tests]._RETURN_[fulfillments_Attributes_Tests]._RETURN_[REQUIRED_message_order_fulfillments_id] | trv10-2.0.1 |
| anchor.v-on-cancel-req-order-cancellation-terms-fulfillment-state-descriptor-code | v on cancel req order cancellation terms fulfillment state descriptor code | trv10-2.0.1:validations/index.yaml#_TESTS_.on_cancel[cancellation_terms_Tests]._RETURN_[cancellation_Attributes_Tests]._RETURN_[REQUIRED_message_order_cancellation_terms_fulfillment_state_descriptor_code] | trv10-2.0.1 |
| anchor.v-on-confirm-enum-order-fulfillments-state-descriptor-code | v on confirm enum order fulfillments state descriptor code | trv10-2.0.1:validations/index.yaml#_TESTS_.on_confirm[VALID_TESTS]._RETURN_[fulfillments_Tests]._RETURN_[fulfillments_Enums_Tests]._RETURN_[VALID_ENUM_message_order_fulfillments_state_descriptor_code] | trv10-2.0.1 |
| anchor.v-on-confirm-enum-order-status | v on confirm enum order status | trv10-2.0.1:validations/index.yaml#_TESTS_.on_confirm[VALID_TESTS]._RETURN_[status_Tests]._RETURN_[status_Enums_Tests]._RETURN_[VALID_ENUM_message_order_status] | trv10-2.0.1 |
| anchor.v-on-confirm-id-tests | v on confirm id tests | trv10-2.0.1:validations/index.yaml#_TESTS_.on_confirm[VALID_TESTS]._RETURN_[id_Tests] | trv10-2.0.1 |
| anchor.v-on-confirm-req-order-created-at | v on confirm req order created at | trv10-2.0.1:validations/index.yaml#_TESTS_.on_confirm[VALID_TESTS]._RETURN_[created_at_Tests]._RETURN_[created_Attributes_Tests]._RETURN_[REQUIRED_message_order_created_at] | trv10-2.0.1 |
| anchor.v-on-confirm-req-order-updated-at | v on confirm req order updated at | trv10-2.0.1:validations/index.yaml#_TESTS_.on_confirm[VALID_TESTS]._RETURN_[updated_at_Tests]._RETURN_[updated_Attributes_Tests]._RETURN_[REQUIRED_message_order_updated_at] | trv10-2.0.1 |
| anchor.v-on-confirm-status-tests | v on confirm status tests | trv10-2.0.1:validations/index.yaml#_TESTS_.on_confirm[VALID_TESTS]._RETURN_[status_Tests] | trv10-2.0.1 |
| anchor.v-on-init-cancellation-terms-tests | v on init cancellation terms tests | trv10-2.0.1:validations/index.yaml#_TESTS_.on_init[cancellation_terms_Tests] | trv10-2.0.1 |
| anchor.v-on-init-enum-order-cancellation-terms-fulfillment-state-descriptor-code | v on init enum order cancellation terms fulfillment state descriptor code | trv10-2.0.1:validations/index.yaml#_TESTS_.on_init[cancellation_terms_Tests]._RETURN_[cancellation_Enums_Tests]._RETURN_[VALID_ENUM_message_order_cancellation_terms_fulfillment_state_descriptor_code] | trv10-2.0.1 |
| anchor.v-on-init-items-tests | v on init items tests | trv10-2.0.1:validations/index.yaml#_TESTS_.on_init[items_Tests] | trv10-2.0.1 |
| anchor.v-on-init-quote-tests | v on init quote tests | trv10-2.0.1:validations/index.yaml#_TESTS_.on_init[quote_Tests] | trv10-2.0.1 |
| anchor.v-on-init-req-order-cancellation-terms-reason-required | v on init req order cancellation terms reason required | trv10-2.0.1:validations/index.yaml#_TESTS_.on_init[cancellation_terms_Tests]._RETURN_[cancellation_Attributes_Tests]._RETURN_[REQUIRED_message_order_cancellation_terms_reason_required] | trv10-2.0.1 |
| anchor.v-on-init-req-order-fulfillments-type | v on init req order fulfillments type | trv10-2.0.1:validations/index.yaml#_TESTS_.on_init[fulfillments_Tests]._RETURN_[fulfillments_Attributes_Tests]._RETURN_[REQUIRED_message_order_fulfillments_type] | trv10-2.0.1 |
| anchor.v-on-init-req-order-items-payment-ids | v on init req order items payment ids | trv10-2.0.1:validations/index.yaml#_TESTS_.on_init[items_Tests]._RETURN_[items_Attributes_Tests]._RETURN_[REQUIRED_message_order_items_payment_ids] | trv10-2.0.1 |
| anchor.v-on-select-enum-order-items-descriptor-code | v on select enum order items descriptor code | trv10-2.0.1:validations/index.yaml#_TESTS_.on_select[items_Tests]._RETURN_[items_Enums_Tests]._RETURN_[VALID_ENUM_message_order_items_descriptor_code] | trv10-2.0.1 |
| anchor.v-on-select-enum-order-quote-breakup-title | v on select enum order quote breakup title | trv10-2.0.1:validations/index.yaml#_TESTS_.on_select[quote_Tests]._RETURN_[quote_Enums_Tests]._RETURN_[VALID_ENUM_message_order_quote_breakup_title] | trv10-2.0.1 |
| anchor.v-on-select-items-enums-tests | v on select items enums tests | trv10-2.0.1:validations/index.yaml#_TESTS_.on_select[items_Tests]._RETURN_[items_Enums_Tests] | trv10-2.0.1 |
| anchor.v-on-select-items-tags-tests | v on select items tags tests | trv10-2.0.1:validations/index.yaml#_TESTS_.on_select[items_Tests]._RETURN_[items_Tags_Tests] | trv10-2.0.1 |
| anchor.v-on-select-quote-enums-tests | v on select quote enums tests | trv10-2.0.1:validations/index.yaml#_TESTS_.on_select[quote_Tests]._RETURN_[quote_Enums_Tests] | trv10-2.0.1 |
| anchor.v-on-select-req-order-items-descriptor-name | v on select req order items descriptor name | trv10-2.0.1:validations/index.yaml#_TESTS_.on_select[items_Tests]._RETURN_[items_Attributes_Tests]._RETURN_[REQUIRED_message_order_items_descriptor_name] | trv10-2.0.1 |
| anchor.v-on-select-req-order-items-fulfillment-ids | v on select req order items fulfillment ids | trv10-2.0.1:validations/index.yaml#_TESTS_.on_select[items_Tests]._RETURN_[items_Attributes_Tests]._RETURN_[REQUIRED_message_order_items_fulfillment_ids] | trv10-2.0.1 |
| anchor.v-on-select-req-order-items-price-currency | v on select req order items price currency | trv10-2.0.1:validations/index.yaml#_TESTS_.on_select[items_Tests]._RETURN_[items_Attributes_Tests]._RETURN_[REQUIRED_message_order_items_price_currency] | trv10-2.0.1 |
| anchor.v-on-select-req-order-items-price-value | v on select req order items price value | trv10-2.0.1:validations/index.yaml#_TESTS_.on_select[items_Tests]._RETURN_[items_Attributes_Tests]._RETURN_[REQUIRED_message_order_items_price_value] | trv10-2.0.1 |
| anchor.v-on-select-req-order-quote-breakup-price-currency | v on select req order quote breakup price currency | trv10-2.0.1:validations/index.yaml#_TESTS_.on_select[quote_Tests]._RETURN_[quote_Attributes_Tests]._RETURN_[REQUIRED_message_order_quote_breakup_price_currency] | trv10-2.0.1 |
| anchor.v-on-select-req-order-quote-breakup-price-value | v on select req order quote breakup price value | trv10-2.0.1:validations/index.yaml#_TESTS_.on_select[quote_Tests]._RETURN_[quote_Attributes_Tests]._RETURN_[REQUIRED_message_order_quote_breakup_price_value] | trv10-2.0.1 |
| anchor.v-on-select-req-order-quote-price-currency | v on select req order quote price currency | trv10-2.0.1:validations/index.yaml#_TESTS_.on_select[quote_Tests]._RETURN_[quote_Attributes_Tests]._RETURN_[REQUIRED_message_order_quote_price_currency] | trv10-2.0.1 |
| anchor.v-on-select-req-order-quote-price-value | v on select req order quote price value | trv10-2.0.1:validations/index.yaml#_TESTS_.on_select[quote_Tests]._RETURN_[quote_Attributes_Tests]._RETURN_[REQUIRED_message_order_quote_price_value] | trv10-2.0.1 |
| anchor.v-on-select-tag-order-items-tags-descriptor-code | v on select tag order items tags descriptor code | trv10-2.0.1:validations/index.yaml#_TESTS_.on_select[items_Tests]._RETURN_[items_Tags_Tests]._RETURN_[VALIDATE_TAG_message_order_items_tags_descriptor_code] | trv10-2.0.1 |
| anchor.v-on-update-order-tags-tests | v on update order tags tests | trv10-2.0.1:validations/index.yaml#_TESTS_.on_update[order_Tests]._RETURN_[order_Tags_Tests] | trv10-2.0.1 |
| anchor.v-on-update-req-order-fulfillments-agent-contact-phone | v on update req order fulfillments agent contact phone | trv10-2.0.1:validations/index.yaml#_TESTS_.on_update[order_Tests]._RETURN_[order_Attributes_Tests]._RETURN_[REQUIRED_message_order_fulfillments_agent_contact_phone] | trv10-2.0.1 |
| anchor.v-on-update-req-order-fulfillments-agent-person-name | v on update req order fulfillments agent person name | trv10-2.0.1:validations/index.yaml#_TESTS_.on_update[order_Tests]._RETURN_[order_Attributes_Tests]._RETURN_[REQUIRED_message_order_fulfillments_agent_person_name] | trv10-2.0.1 |
| anchor.v-on-update-req-order-fulfillments-vehicle-registration | v on update req order fulfillments vehicle registration | trv10-2.0.1:validations/index.yaml#_TESTS_.on_update[order_Tests]._RETURN_[order_Attributes_Tests]._RETURN_[REQUIRED_message_order_fulfillments_vehicle_registration] | trv10-2.0.1 |
| anchor.v-search-chk-city-code-format | v search chk city code format | trv10-2.0.1:validations/index.yaml#_TESTS_.search[Context_tests]._RETURN_[Context_Attributes_Tests]._RETURN_[VALIDATE_CITY_CODE_FORMAT] | trv10-2.0.1 |
| anchor.v-search-enum-context-domain | v search enum context domain | trv10-2.0.1:validations/index.yaml#_TESTS_.search[Context_tests]._RETURN_[Context_Enums_Tests]._RETURN_[VALID_ENUM_context_domain] | trv10-2.0.1 |
| anchor.v-search-enum-context-location-country-code | v search enum context location country code | trv10-2.0.1:validations/index.yaml#_TESTS_.search[Context_tests]._RETURN_[Context_Enums_Tests]._RETURN_[VALID_ENUM_context_location_country_code] | trv10-2.0.1 |
| anchor.v-search-req-context-bap-id | v search req context bap id | trv10-2.0.1:validations/index.yaml#_TESTS_.search[Context_tests]._RETURN_[Context_Attributes_Tests]._RETURN_[REQUIRED_context_bap_id] | trv10-2.0.1 |
| anchor.v-search-req-context-bap-uri | v search req context bap uri | trv10-2.0.1:validations/index.yaml#_TESTS_.search[Context_tests]._RETURN_[Context_Attributes_Tests]._RETURN_[REQUIRED_context_bap_uri] | trv10-2.0.1 |
| anchor.v-search-req-context-msg-id | v search req context msg id | trv10-2.0.1:validations/index.yaml#_TESTS_.search[Context_tests]._RETURN_[Context_Attributes_Tests]._RETURN_[REQUIRED_context_message_id] | trv10-2.0.1 |
| anchor.v-search-req-context-timestamp | v search req context timestamp | trv10-2.0.1:validations/index.yaml#_TESTS_.search[Context_tests]._RETURN_[Context_Attributes_Tests]._RETURN_[REQUIRED_context_timestamp] | trv10-2.0.1 |
| anchor.v-search-req-context-transaction-id | v search req context transaction id | trv10-2.0.1:validations/index.yaml#_TESTS_.search[Context_tests]._RETURN_[Context_Attributes_Tests]._RETURN_[REQUIRED_context_transaction_id] | trv10-2.0.1 |
| anchor.v-search-req-context-ttl | v search req context ttl | trv10-2.0.1:validations/index.yaml#_TESTS_.search[Context_tests]._RETURN_[Context_Attributes_Tests]._RETURN_[REQUIRED_context_ttl] | trv10-2.0.1 |
| anchor.v-search-req-context-version | v search req context version | trv10-2.0.1:validations/index.yaml#_TESTS_.search[Context_tests]._RETURN_[Context_Attributes_Tests]._RETURN_[REQUIRED_context_version] | trv10-2.0.1 |
| anchor.v-select-context-attributes-tests | v select context attributes tests | trv10-2.0.1:validations/index.yaml#_TESTS_.select[Context_tests]._RETURN_[Context_Attributes_Tests] | trv10-2.0.1 |
| anchor.v-select-enum-order-fulfillments-state-descriptor-code | v select enum order fulfillments state descriptor code | trv10-2.0.1:validations/index.yaml#_TESTS_.select[fulfillments_Tests]._RETURN_[fulfillments_Enums_Tests]._RETURN_[VALID_ENUM_message_order_fulfillments_state_descriptor_code] | trv10-2.0.1 |
| anchor.v-select-enum-order-fulfillments-stops-authorization-status | v select enum order fulfillments stops authorization status | trv10-2.0.1:validations/index.yaml#_TESTS_.select[fulfillments_Tests]._RETURN_[fulfillments_Enums_Tests]._RETURN_[VALID_ENUM_message_order_fulfillments_stops_authorization_status] | trv10-2.0.1 |
| anchor.v-select-enum-order-fulfillments-stops-authorization-type | v select enum order fulfillments stops authorization type | trv10-2.0.1:validations/index.yaml#_TESTS_.select[fulfillments_Tests]._RETURN_[fulfillments_Enums_Tests]._RETURN_[VALID_ENUM_message_order_fulfillments_stops_authorization_type] | trv10-2.0.1 |
| anchor.v-select-enum-order-fulfillments-type | v select enum order fulfillments type | trv10-2.0.1:validations/index.yaml#_TESTS_.select[fulfillments_Tests]._RETURN_[fulfillments_Enums_Tests]._RETURN_[VALID_ENUM_message_order_fulfillments_type] | trv10-2.0.1 |
| anchor.v-select-enum-order-fulfillments-vehicle-category | v select enum order fulfillments vehicle category | trv10-2.0.1:validations/index.yaml#_TESTS_.select[fulfillments_Tests]._RETURN_[fulfillments_Enums_Tests]._RETURN_[VALID_ENUM_message_order_fulfillments_vehicle_category] | trv10-2.0.1 |
| anchor.v-select-enum-order-fulfillments-vehicle-energy-type | v select enum order fulfillments vehicle energy type | trv10-2.0.1:validations/index.yaml#_TESTS_.select[fulfillments_Tests]._RETURN_[fulfillments_Enums_Tests]._RETURN_[VALID_ENUM_message_order_fulfillments_vehicle_energy_type] | trv10-2.0.1 |
| anchor.v-select-enum-order-fulfillments-vehicle-variant | v select enum order fulfillments vehicle variant | trv10-2.0.1:validations/index.yaml#_TESTS_.select[fulfillments_Tests]._RETURN_[fulfillments_Enums_Tests]._RETURN_[VALID_ENUM_message_order_fulfillments_vehicle_variant] | trv10-2.0.1 |
| anchor.v-select-enum-order-items-descriptor-code | v select enum order items descriptor code | trv10-2.0.1:validations/index.yaml#_TESTS_.select[items_Tests]._RETURN_[items_Enums_Tests]._RETURN_[VALID_ENUM_message_order_items_descriptor_code] | trv10-2.0.1 |
| anchor.v-select-enum-order-payments-collected-by | v select enum order payments collected by | trv10-2.0.1:validations/index.yaml#_TESTS_.select[payments_Tests]._RETURN_[payments_Enums_Tests]._RETURN_[VALID_ENUM_message_order_payments_collected_by] | trv10-2.0.1 |
| anchor.v-select-enum-order-payments-status | v select enum order payments status | trv10-2.0.1:validations/index.yaml#_TESTS_.select[payments_Tests]._RETURN_[payments_Enums_Tests]._RETURN_[VALID_ENUM_message_order_payments_status] | trv10-2.0.1 |
| anchor.v-select-enum-order-payments-type | v select enum order payments type | trv10-2.0.1:validations/index.yaml#_TESTS_.select[payments_Tests]._RETURN_[payments_Enums_Tests]._RETURN_[VALID_ENUM_message_order_payments_type] | trv10-2.0.1 |
| anchor.v-select-items-attributes-tests | v select items attributes tests | trv10-2.0.1:validations/index.yaml#_TESTS_.select[items_Tests]._RETURN_[items_Attributes_Tests] | trv10-2.0.1 |
| anchor.v-select-items-enums-tests | v select items enums tests | trv10-2.0.1:validations/index.yaml#_TESTS_.select[items_Tests]._RETURN_[items_Enums_Tests] | trv10-2.0.1 |
| anchor.v-select-items-tests | v select items tests | trv10-2.0.1:validations/index.yaml#_TESTS_.select[items_Tests] | trv10-2.0.1 |
| anchor.v-select-payments-tests | v select payments tests | trv10-2.0.1:validations/index.yaml#_TESTS_.select[payments_Tests] | trv10-2.0.1 |
| anchor.v-select-provider-tests | v select provider tests | trv10-2.0.1:validations/index.yaml#_TESTS_.select[provider_Tests] | trv10-2.0.1 |
| anchor.v-select-req-context-bpp-id | v select req context bpp id | trv10-2.0.1:validations/index.yaml#_TESTS_.select[Context_tests]._RETURN_[Context_Attributes_Tests]._RETURN_[REQUIRED_context_bpp_id] | trv10-2.0.1 |
| anchor.v-select-req-context-bpp-uri | v select req context bpp uri | trv10-2.0.1:validations/index.yaml#_TESTS_.select[Context_tests]._RETURN_[Context_Attributes_Tests]._RETURN_[REQUIRED_context_bpp_uri] | trv10-2.0.1 |
| anchor.v-select-req-order-items-id | v select req order items id | trv10-2.0.1:validations/index.yaml#_TESTS_.select[items_Tests]._RETURN_[items_Attributes_Tests]._RETURN_[REQUIRED_message_order_items_id] | trv10-2.0.1 |
| anchor.v-select-req-order-provider-id | v select req order provider id | trv10-2.0.1:validations/index.yaml#_TESTS_.select[provider_Tests]._RETURN_[provider_Attributes_Tests]._RETURN_[REQUIRED_message_order_provider_id] | trv10-2.0.1 |
| anchor.v-update-req-order-id | v update req order id | trv10-2.0.1:validations/index.yaml#_TESTS_.update[order_Tests]._RETURN_[order_Attributes_Tests]._RETURN_[REQUIRED_message_order_id] | trv10-2.0.1 |
| anchor.v-update-shared-return-a57 | v update shared return a57 | trv10-2.0.1:validations/index.yaml#_TESTS_.update[order_Tests]._RETURN_[order_Attributes_Tests]._RETURN_ | trv10-2.0.1 |
| anchor.validation-group | validation group | workbench:frames/validation-layers.md | trv10-2.0.1 |
| anchor.validation-rule | validation rule | workbench:frames/validation-layers.md | trv10-2.0.1 |
| anchor.vehicle-category | vehicle category | trv10-2.0.1:attributes/Ride_hailing.yaml#attribute_set.search.message.intent.fulfillment.vehicle.category | trv10-2.0.1 |
| anchor.vehicle-energy-type | vehicle energy type | trv10-2.0.1:validations/index.yaml#_TESTS_.select[fulfillments_Tests]._RETURN_[fulfillments_Enums_Tests]._RETURN_[VALID_ENUM_message_order_fulfillments_vehicle_energy_type] | trv10-2.0.1 |
| anchor.vehicle-variant | vehicle variant | trv10-2.0.1:attributes/Ride_hailing.yaml#attribute_set.search.message.intent.fulfillment.vehicle.variant | trv10-2.0.1 |

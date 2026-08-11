# fis14-2.1.0 candidate units (Stage E)
dom.fis14 | isa | anchor.ondc-domain | basis:declared | asof:fis14-2.1.0 | grounded-in:fis14-2.1.0:index.yaml#info.domain
dom.fis14 | has-slot | anchor.mutual-funds-usecase | basis:declared | asof:fis14-2.1.0 | grounded-in:fis14-2.1.0:index.yaml#info.x-usecases
anchor.mutual-funds-usecase | scoped-to | dom.fis14 | basis:declared | asof:fis14-2.1.0 | grounded-in:fis14-2.1.0:attributes/MUTUAL_FUNDS.yaml#meta.use_case_id
anchor.fis14-action-set | part-of | dom.fis14 | basis:declared | asof:fis14-2.1.0 | grounded-in:fis14-2.1.0:actions/index.yaml#supportedActions
anchor.book-rationale | not-part-of | dom.fis14 | basis:declared | asof:fis14-2.1.0 | grounded-in:fis14-2.1.0:index.yaml#x-docs
anchor.release-notes | not-part-of | dom.fis14 | basis:declared | asof:fis14-2.1.0 | grounded-in:fis14-2.1.0:index.yaml#x-docs
anchor.external-references | not-part-of | dom.fis14 | basis:declared | asof:fis14-2.1.0 | grounded-in:fis14-2.1.0:index.yaml#x-docs
dom.fis14 | constrains | anchor.category-code | basis:declared | asof:fis14-2.1.0 | grounded-in:fis14-2.1.0:validations/index.yaml#_TESTS_.search[SEARCH_CATEGORY_CODE]._RETURN_[VALID_ENUM_CATEGORY_CODE].enumList
anchor.category-code | isa | anchor.enum-anchor | basis:declared | asof:fis14-2.1.0 | grounded-in:fis14-2.1.0:validations/index.yaml#_TESTS_.on_search[ON_SEARCH_CATEGORIES]._RETURN_[VALID_ENUM_CATEGORIES_CODE].enumList
anchor.category-code | constrains | anchor.category-hierarchy | basis:declared | asof:fis14-2.1.0 | grounded-in:fis14-2.1.0:validations/index.yaml#_TESTS_.on_search[ON_SEARCH_CATEGORIES]._RETURN_[REQUIRED_CATEGORIES_PARENT_ID]._CONTINUE_
anchor.category-hierarchy | has-slot | anchor.parent-category-id | basis:declared | asof:fis14-2.1.0 | grounded-in:fis14-2.1.0:validations/index.yaml#_TESTS_.on_search[ON_SEARCH_CATEGORIES]._RETURN_[REQUIRED_CATEGORIES_PARENT_ID].attr
anchor.category-hierarchy | sent-by | anchor.bpp | basis:declared | asof:fis14-2.1.0 | grounded-in:fis14-2.1.0:attributes/MUTUAL_FUNDS.yaml#attribute_set.on_search.message.catalog.providers.categories._description.owner
anchor.select | not-requires | anchor.search | basis:declared | asof:fis14-2.1.0 | grounded-in:fis14-2.1.0:actions/index.yaml#apiProperties.select.async_predecessor
anchor.select | not-requires | anchor.on-search | basis:declared | asof:fis14-2.1.0 | grounded-in:fis14-2.1.0:actions/index.yaml#apiProperties.select.transaction_partner
anchor.search | not-requires | anchor.select | basis:declared | asof:fis14-2.1.0 | grounded-in:fis14-2.1.0:actions/index.yaml#apiProperties.search.transaction_partner
anchor.search | not-requires | anchor.bpp-id | basis:declared | asof:fis14-2.1.0 | grounded-in:fis14-2.1.0:validations/index.yaml#_TESTS_.search[SEARCH_CONTEXT]._RETURN_[CONTEXT_REQUIRED]._RETURN_[REQUIRED_CONTEXT_BPP_ID]._CONTINUE_
anchor.search | not-requires | anchor.bpp-uri | basis:declared | asof:fis14-2.1.0 | grounded-in:fis14-2.1.0:validations/index.yaml#_TESTS_.search[SEARCH_CONTEXT]._RETURN_[CONTEXT_REQUIRED]._RETURN_[REQUIRED_CONTEXT_BPP_URI]._CONTINUE_
anchor.catalog-discovery | isa | anchor.transaction-purpose | basis:declared | asof:fis14-2.1.0 | grounded-in:fis14-2.1.0:flows/index.yaml#flows[Main_Search].tags
anchor.investment-order | isa | anchor.transaction-purpose | basis:declared | asof:fis14-2.1.0 | grounded-in:fis14-2.1.0:flows/index.yaml#flows[SIP_Creation_New_Folio].tags
anchor.catalog-discovery | disjoint-with | anchor.investment-order | basis:declared | asof:fis14-2.1.0 | grounded-in:fis14-2.1.0:flows/index.yaml#flows
anchor.search | scoped-to | anchor.catalog-discovery | basis:declared | asof:fis14-2.1.0 | grounded-in:fis14-2.1.0:flows/MUTUAL FUNDS/Main_Search.yaml#steps[search]
anchor.select | scoped-to | anchor.investment-order | basis:declared | asof:fis14-2.1.0 | grounded-in:fis14-2.1.0:flows/MUTUAL FUNDS/SIP_Creation_New_Folio.yaml#steps[select]
anchor.catalog-discovery | precedes | anchor.investment-order | basis:inferred | asof:fis14-2.1.0
anchor.select | requires | anchor.provider-id | basis:declared | asof:fis14-2.1.0 | grounded-in:fis14-2.1.0:validations/index.yaml#_TESTS_.select[SELECT_PROVIDER_ID].attr
anchor.select | requires | anchor.item-id | basis:declared | asof:fis14-2.1.0 | grounded-in:fis14-2.1.0:validations/index.yaml#_TESTS_.select[SELECT_ITEMS]._RETURN_[REQUIRED_ITEM_ID].attr
anchor.investment-order | requires | anchor.scheme-plan | basis:declared | asof:fis14-2.1.0 | grounded-in:fis14-2.1.0:validations/index.yaml#_TESTS_.on_select[ON_SELECT_ITEMS]._RETURN_[VALID_ITEM_DESCRIPTOR_CODE_ENUM].enumList
anchor.on-search | precedes | anchor.select | basis:declared | asof:fis14-2.1.0 | grounded-in:fis14-2.1.0:actions/index.yaml#supportedActions.on_search
anchor.on-search | precedes | anchor.search | basis:declared | asof:fis14-2.1.0 | grounded-in:fis14-2.1.0:actions/index.yaml#supportedActions.on_search
anchor.select | precedes | anchor.on-select | basis:declared | asof:fis14-2.1.0 | grounded-in:fis14-2.1.0:actions/index.yaml#supportedActions.select
anchor.on-select | precedes | anchor.init | basis:declared | asof:fis14-2.1.0 | grounded-in:fis14-2.1.0:actions/index.yaml#supportedActions.on_select
anchor.on-select | precedes | anchor.select | basis:declared | asof:fis14-2.1.0 | grounded-in:fis14-2.1.0:actions/index.yaml#supportedActions.on_select
anchor.on-select | precedes | anchor.status | basis:declared | asof:fis14-2.1.0 | grounded-in:fis14-2.1.0:actions/index.yaml#supportedActions.on_select
anchor.on-select | precedes | anchor.on-status | basis:declared | asof:fis14-2.1.0 | grounded-in:fis14-2.1.0:actions/index.yaml#supportedActions.on_select
anchor.init | precedes | anchor.on-init | basis:declared | asof:fis14-2.1.0 | grounded-in:fis14-2.1.0:actions/index.yaml#supportedActions.init
anchor.on-init | precedes | anchor.confirm | basis:declared | asof:fis14-2.1.0 | grounded-in:fis14-2.1.0:actions/index.yaml#supportedActions.on_init
anchor.on-init | precedes | anchor.init | basis:declared | asof:fis14-2.1.0 | grounded-in:fis14-2.1.0:actions/index.yaml#supportedActions.on_init
anchor.confirm | precedes | anchor.on-confirm | basis:declared | asof:fis14-2.1.0 | grounded-in:fis14-2.1.0:actions/index.yaml#supportedActions.confirm
anchor.on-confirm | precedes | anchor.update | basis:declared | asof:fis14-2.1.0 | grounded-in:fis14-2.1.0:actions/index.yaml#supportedActions.on_confirm
anchor.on-confirm | precedes | anchor.on-update | basis:declared | asof:fis14-2.1.0 | grounded-in:fis14-2.1.0:actions/index.yaml#supportedActions.on_confirm
anchor.on-confirm | precedes | anchor.status | basis:declared | asof:fis14-2.1.0 | grounded-in:fis14-2.1.0:actions/index.yaml#supportedActions.on_confirm
anchor.on-confirm | precedes | anchor.on-status | basis:declared | asof:fis14-2.1.0 | grounded-in:fis14-2.1.0:actions/index.yaml#supportedActions.on_confirm
anchor.on-confirm | precedes | anchor.issue | basis:declared | asof:fis14-2.1.0 | grounded-in:fis14-2.1.0:actions/index.yaml#supportedActions.on_confirm
anchor.update | precedes | anchor.on-update | basis:declared | asof:fis14-2.1.0 | grounded-in:fis14-2.1.0:actions/index.yaml#supportedActions.update
anchor.on-update | precedes | anchor.update | basis:declared | asof:fis14-2.1.0 | grounded-in:fis14-2.1.0:actions/index.yaml#supportedActions.on_update
anchor.on-update | precedes | anchor.status | basis:declared | asof:fis14-2.1.0 | grounded-in:fis14-2.1.0:actions/index.yaml#supportedActions.on_update
anchor.on-update | precedes | anchor.on-status | basis:declared | asof:fis14-2.1.0 | grounded-in:fis14-2.1.0:actions/index.yaml#supportedActions.on_update
anchor.on-update | precedes | anchor.issue | basis:declared | asof:fis14-2.1.0 | grounded-in:fis14-2.1.0:actions/index.yaml#supportedActions.on_update
anchor.status | precedes | anchor.on-status | basis:declared | asof:fis14-2.1.0 | grounded-in:fis14-2.1.0:actions/index.yaml#supportedActions.status
anchor.on-status | precedes | anchor.status | basis:declared | asof:fis14-2.1.0 | grounded-in:fis14-2.1.0:actions/index.yaml#supportedActions.on_status
anchor.on-status | precedes | anchor.init | basis:declared | asof:fis14-2.1.0 | grounded-in:fis14-2.1.0:actions/index.yaml#supportedActions.on_status
anchor.on-status | precedes | anchor.update | basis:declared | asof:fis14-2.1.0 | grounded-in:fis14-2.1.0:actions/index.yaml#supportedActions.on_status
anchor.on-status | precedes | anchor.on-update | basis:declared | asof:fis14-2.1.0 | grounded-in:fis14-2.1.0:actions/index.yaml#supportedActions.on_status
anchor.on-status | precedes | anchor.select | basis:declared | asof:fis14-2.1.0 | grounded-in:fis14-2.1.0:actions/index.yaml#supportedActions.on_status
anchor.on-status | precedes | anchor.issue | basis:declared | asof:fis14-2.1.0 | grounded-in:fis14-2.1.0:actions/index.yaml#supportedActions.on_status
anchor.issue | precedes | anchor.on-issue | basis:declared | asof:fis14-2.1.0 | grounded-in:fis14-2.1.0:actions/index.yaml#supportedActions.issue
anchor.on-issue | precedes | anchor.on-issue-status | basis:declared | asof:fis14-2.1.0 | grounded-in:fis14-2.1.0:actions/index.yaml#supportedActions.on_issue
anchor.on-issue-status | precedes | anchor.on-issue | basis:declared | asof:fis14-2.1.0 | grounded-in:fis14-2.1.0:actions/index.yaml#supportedActions.on_issue_status
anchor.on-search | requires | anchor.search | basis:declared | asof:fis14-2.1.0 | grounded-in:fis14-2.1.0:actions/index.yaml#apiProperties.on_search.async_predecessor
anchor.on-init | requires | anchor.init | basis:declared | asof:fis14-2.1.0 | grounded-in:fis14-2.1.0:actions/index.yaml#apiProperties.on_init.async_predecessor
anchor.on-confirm | requires | anchor.confirm | basis:declared | asof:fis14-2.1.0 | grounded-in:fis14-2.1.0:actions/index.yaml#apiProperties.on_confirm.async_predecessor
anchor.on-select | requires | anchor.select | basis:declared | asof:fis14-2.1.0 | grounded-in:fis14-2.1.0:actions/index.yaml#apiProperties.on_select.transaction_partner
anchor.init | requires | anchor.on-select | basis:declared | asof:fis14-2.1.0 | grounded-in:fis14-2.1.0:actions/index.yaml#apiProperties.init.transaction_partner
anchor.confirm | requires | anchor.on-init | basis:declared | asof:fis14-2.1.0 | grounded-in:fis14-2.1.0:actions/index.yaml#apiProperties.confirm.transaction_partner
anchor.on-update | requires | anchor.on-confirm | basis:declared | asof:fis14-2.1.0 | grounded-in:fis14-2.1.0:actions/index.yaml#apiProperties.on_update.transaction_partner
anchor.status | requires | anchor.on-select | basis:declared | asof:fis14-2.1.0 | grounded-in:fis14-2.1.0:actions/index.yaml#apiProperties.status.transaction_partner
anchor.on-status | requires | anchor.on-select | basis:declared | asof:fis14-2.1.0 | grounded-in:fis14-2.1.0:actions/index.yaml#apiProperties.on_status.transaction_partner
anchor.update | not-requires | anchor.on-confirm | basis:declared | asof:fis14-2.1.0 | grounded-in:fis14-2.1.0:actions/index.yaml#apiProperties.update.transaction_partner
anchor.issue | not-part-of | anchor.fis14-flow-set | basis:declared | asof:fis14-2.1.0 | grounded-in:fis14-2.1.0:flows/index.yaml#flows
anchor.on-issue | not-part-of | anchor.fis14-flow-set | basis:declared | asof:fis14-2.1.0 | grounded-in:fis14-2.1.0:flows/index.yaml#flows
anchor.cancel | not-part-of | anchor.fis14-action-set | basis:declared | asof:fis14-2.1.0 | grounded-in:fis14-2.1.0:actions/index.yaml#supportedActions
anchor.cancel | has-slot | anchor.cancellation-reason | basis:declared | asof:fis14-2.1.0 | grounded-in:fis14-2.1.0:attributes/MUTUAL_FUNDS.yaml#attribute_set.cancel.message.cancellation_reason_id
anchor.track | not-part-of | anchor.fis14-action-set | basis:declared | asof:fis14-2.1.0 | grounded-in:fis14-2.1.0:actions/index.yaml#supportedActions
anchor.rating | not-part-of | anchor.fis14-action-set | basis:declared | asof:fis14-2.1.0 | grounded-in:fis14-2.1.0:actions/index.yaml#supportedActions
anchor.support | not-part-of | anchor.fis14-action-set | basis:declared | asof:fis14-2.1.0 | grounded-in:fis14-2.1.0:actions/index.yaml#supportedActions
anchor.l1-payload-validation | isa | anchor.validation-layer | basis:authority | asof:fis14-2.1.0 | grounded-in:workbench:frames/validation-layers.md
anchor.validation-block | part-of | anchor.l1-payload-validation | basis:authority | asof:fis14-2.1.0 | grounded-in:workbench:frames/validation-layers.md
anchor.context-envelope | isa | anchor.validation-block | basis:declared | asof:fis14-2.1.0 | grounded-in:fis14-2.1.0:validations/index.yaml#_TESTS_.search[SEARCH_CONTEXT]._RETURN_
anchor.context-envelope | scoped-to | anchor.on-search | basis:declared | asof:fis14-2.1.0 | grounded-in:fis14-2.1.0:validations/index.yaml#_TESTS_.on_search[ON_SEARCH_CONTEXT]._RETURN_
anchor.context-envelope | scoped-to | anchor.select | basis:declared | asof:fis14-2.1.0 | grounded-in:fis14-2.1.0:validations/index.yaml#_TESTS_.select[SELECT_CONTEXT]._RETURN_
anchor.context-envelope | scoped-to | anchor.on-select | basis:declared | asof:fis14-2.1.0 | grounded-in:fis14-2.1.0:validations/index.yaml#_TESTS_.on_select[ON_SELECT_CONTEXT]._RETURN_
anchor.context-envelope | scoped-to | anchor.init | basis:declared | asof:fis14-2.1.0 | grounded-in:fis14-2.1.0:validations/index.yaml#_TESTS_.init[INIT_CONTEXT]._RETURN_
anchor.context-envelope | scoped-to | anchor.on-init | basis:declared | asof:fis14-2.1.0 | grounded-in:fis14-2.1.0:validations/index.yaml#_TESTS_.on_init[ON_INIT_CONTEXT]._RETURN_
anchor.context-envelope | scoped-to | anchor.confirm | basis:declared | asof:fis14-2.1.0 | grounded-in:fis14-2.1.0:validations/index.yaml#_TESTS_.confirm[CONFIRM_CONTEXT]._RETURN_
anchor.context-envelope | scoped-to | anchor.on-confirm | basis:declared | asof:fis14-2.1.0 | grounded-in:fis14-2.1.0:validations/index.yaml#_TESTS_.on_confirm[ON_CONFIRM_CONTEXT]._RETURN_
anchor.context-envelope | scoped-to | anchor.status | basis:declared | asof:fis14-2.1.0 | grounded-in:fis14-2.1.0:validations/index.yaml#_TESTS_.status[STATUS_CONTEXT]._RETURN_
anchor.context-envelope | scoped-to | anchor.on-status | basis:declared | asof:fis14-2.1.0 | grounded-in:fis14-2.1.0:validations/index.yaml#_TESTS_.on_status[ON_STATUS_CONTEXT]._RETURN_
anchor.context-envelope | scoped-to | anchor.update | basis:declared | asof:fis14-2.1.0 | grounded-in:fis14-2.1.0:validations/index.yaml#_TESTS_.update[UPDATE_CONTEXT]._RETURN_
anchor.context-envelope | scoped-to | anchor.on-update | basis:declared | asof:fis14-2.1.0 | grounded-in:fis14-2.1.0:validations/index.yaml#_TESTS_.on_update[ON_UPDATE_CONTEXT]._RETURN_
anchor.context-envelope | requires | anchor.transaction-id | basis:declared | asof:fis14-2.1.0 | grounded-in:fis14-2.1.0:validations/index.yaml#_TESTS_.search[SEARCH_CONTEXT]._RETURN_[CONTEXT_REQUIRED]._RETURN_[REQUIRED_CONTEXT_TRANSACTION_ID].attr
anchor.context-envelope | requires | anchor.message-id | basis:declared | asof:fis14-2.1.0 | grounded-in:fis14-2.1.0:validations/index.yaml#_TESTS_.search[SEARCH_CONTEXT]._RETURN_[CONTEXT_REQUIRED]._RETURN_[REQUIRED_CONTEXT_MESSAGE_ID].attr
anchor.context-envelope | constrains | anchor.ttl | basis:declared | asof:fis14-2.1.0 | grounded-in:fis14-2.1.0:validations/index.yaml#_TESTS_.search[SEARCH_CONTEXT]._RETURN_[CONTEXT_REGEX]._RETURN_[REGEX_CONTEXT_TTL].reg
anchor.context-envelope | constrains | anchor.city-code | basis:declared | asof:fis14-2.1.0 | grounded-in:fis14-2.1.0:validations/index.yaml#_TESTS_.search[SEARCH_CONTEXT]._RETURN_[CONTEXT_REGEX]._RETURN_[REGEX_CONTEXT_LOCATION_CITY_CODE].reg
anchor.context-envelope | constrains | anchor.country-code | basis:declared | asof:fis14-2.1.0 | grounded-in:fis14-2.1.0:validations/index.yaml#_TESTS_.search[SEARCH_CONTEXT]._RETURN_[CONTEXT_ENUM]._RETURN_[VALID_CONTEXT_LOCATION_COUNTRY_CODE].enumList
anchor.fulfillment-type | isa | anchor.enum-anchor | basis:declared | asof:fis14-2.1.0 | grounded-in:fis14-2.1.0:validations/index.yaml#_TESTS_.on_search[ON_SEARCH_FULFILLMENTS]._RETURN_[VALID_FULFILLMENT_TYPE_ENUM].enumList
anchor.fulfillment-type | scoped-to | anchor.select | basis:declared | asof:fis14-2.1.0 | grounded-in:fis14-2.1.0:validations/index.yaml#_TESTS_.select[SELECT_FULFILLMENTS]._RETURN_[VALID_FULFILLMENT_TYPE_ENUM].enumList
anchor.fulfillment-type | scoped-to | anchor.on-select | basis:declared | asof:fis14-2.1.0 | grounded-in:fis14-2.1.0:validations/index.yaml#_TESTS_.on_select[ON_SELECT_FULFILLMENTS]._RETURN_[REQUIRED_FULFILLMENT_TYPE].enumList
anchor.fulfillment-type | scoped-to | anchor.init | basis:declared | asof:fis14-2.1.0 | grounded-in:fis14-2.1.0:validations/index.yaml#_TESTS_.init[INIT_FULFILLMENTS]._RETURN_[REQUIRED_FULFILLMENT_TYPE].enumList
anchor.fulfillment-type | scoped-to | anchor.on-init | basis:declared | asof:fis14-2.1.0 | grounded-in:fis14-2.1.0:validations/index.yaml#_TESTS_.on_init[ON_INIT_FULFILLMENTS]._RETURN_[REQUIRED_FULFILLMENT_TYPE].enumList
anchor.fulfillment-type | scoped-to | anchor.confirm | basis:declared | asof:fis14-2.1.0 | grounded-in:fis14-2.1.0:validations/index.yaml#_TESTS_.confirm[CONFIRM_FULFILLMENTS]._RETURN_[REQUIRED_FULFILLMENT_TYPE].enumList
anchor.fulfillment-type | scoped-to | anchor.on-confirm | basis:declared | asof:fis14-2.1.0 | grounded-in:fis14-2.1.0:validations/index.yaml#_TESTS_.on_confirm[ON_CONFIRM_FULFILLMENTS]._RETURN_[REQUIRED_FULFILLMENT_TYPE].enumList
anchor.lumpsum | isa | anchor.fulfillment-type | basis:declared | asof:fis14-2.1.0 | grounded-in:fis14-2.1.0:validations/index.yaml#_TESTS_.on_search[ON_SEARCH_FULFILLMENTS_LUMPSUM]._SCOPE_
anchor.sip | isa | anchor.fulfillment-type | basis:declared | asof:fis14-2.1.0 | grounded-in:fis14-2.1.0:validations/index.yaml#_TESTS_.on_search[ON_SEARCH_FULFILLMENTS_SIP]._SCOPE_
anchor.redemption | isa | anchor.fulfillment-type | basis:declared | asof:fis14-2.1.0 | grounded-in:fis14-2.1.0:validations/index.yaml#_TESTS_.on_search[ON_SEARCH_FULFILLMENTS_REDEMPTION]._SCOPE_
anchor.instant-redemption | isa | anchor.fulfillment-type | basis:declared | asof:fis14-2.1.0 | grounded-in:fis14-2.1.0:validations/index.yaml#_TESTS_.on_search[ON_SEARCH_FULFILLMENTS_INSTANT_REDEMPTION]._SCOPE_
anchor.swp | isa | anchor.fulfillment-type | basis:declared | asof:fis14-2.1.0 | grounded-in:fis14-2.1.0:validations/index.yaml#_TESTS_.on_search[ON_SEARCH_FULFILLMENTS_SWP]._SCOPE_
anchor.stp | isa | anchor.fulfillment-type | basis:declared | asof:fis14-2.1.0 | grounded-in:fis14-2.1.0:validations/index.yaml#_TESTS_.on_search[ON_SEARCH_FULFILLMENTS_STP]._SCOPE_
anchor.sip-instalment | isa | anchor.fulfillment-type | basis:declared | asof:fis14-2.1.0 | grounded-in:fis14-2.1.0:validations/index.yaml#_TESTS_.on_search[ON_SEARCH_FULFILLMENTS]._RETURN_[VALID_FULFILLMENT_TYPE_ENUM].enumList
anchor.fulfillment-type | part-of | anchor.fulfillment-type-dictionary | basis:declared | asof:fis14-2.1.0 | grounded-in:fis14-2.1.0:attributes/MUTUAL_FUNDS.yaml#attribute_set.on_search.message.catalog.providers.fulfillments.type._description.enums
anchor.kyc-fulfillment | isa | anchor.fulfillment-type-dictionary | basis:declared | asof:fis14-2.1.0 | grounded-in:fis14-2.1.0:attributes/MUTUAL_FUNDS.yaml#attribute_set.on_search.message.catalog.providers.fulfillments.type._description.enums
anchor.payment-mandate-fulfillment | isa | anchor.fulfillment-type-dictionary | basis:declared | asof:fis14-2.1.0 | grounded-in:fis14-2.1.0:attributes/MUTUAL_FUNDS.yaml#attribute_set.on_search.message.catalog.providers.fulfillments.type._description.enums
anchor.zero-balance-folio-fulfillment | isa | anchor.fulfillment-type-dictionary | basis:declared | asof:fis14-2.1.0 | grounded-in:fis14-2.1.0:attributes/MUTUAL_FUNDS.yaml#attribute_set.on_search.message.catalog.providers.fulfillments.type._description.enums
anchor.switch-fulfillment | isa | anchor.fulfillment-type-dictionary | basis:declared | asof:fis14-2.1.0 | grounded-in:fis14-2.1.0:attributes/MUTUAL_FUNDS.yaml#attribute_set.on_search.message.catalog.providers.fulfillments.type._description.enums
anchor.kyc-fulfillment | not-isa | anchor.fulfillment-type | basis:declared | asof:fis14-2.1.0 | grounded-in:fis14-2.1.0:validations/index.yaml#_TESTS_.on_search[ON_SEARCH_FULFILLMENTS]._RETURN_[VALID_FULFILLMENT_TYPE_ENUM].enumList
anchor.payment-mandate-fulfillment | not-isa | anchor.fulfillment-type | basis:declared | asof:fis14-2.1.0 | grounded-in:fis14-2.1.0:validations/index.yaml#_TESTS_.on_search[ON_SEARCH_FULFILLMENTS]._RETURN_[VALID_FULFILLMENT_TYPE_ENUM].enumList
anchor.switch-fulfillment | not-isa | anchor.fulfillment-type | basis:declared | asof:fis14-2.1.0 | grounded-in:fis14-2.1.0:validations/index.yaml#_TESTS_.on_search[ON_SEARCH_FULFILLMENTS]._RETURN_[VALID_FULFILLMENT_TYPE_ENUM].enumList
anchor.distributor-cred-type | isa | anchor.enum-anchor | basis:declared | asof:fis14-2.1.0 | grounded-in:fis14-2.1.0:validations/index.yaml#_TESTS_.search[SEARCH_AGENT_CREDENTIALS]._RETURN_[VALID_AGENT_CREDS_TYPE_ENUM].enumList
anchor.distributor-cred-type | scoped-to | anchor.select | basis:declared | asof:fis14-2.1.0 | grounded-in:fis14-2.1.0:validations/index.yaml#_TESTS_.select[SELECT_FULFILLMENTS_SIP]._RETURN_[VALID_AGENT_CREDS_TYPE_ENUM].enumList
anchor.arn | isa | anchor.distributor-cred-type | basis:declared | asof:fis14-2.1.0 | grounded-in:fis14-2.1.0:attributes/MUTUAL_FUNDS.yaml#attribute_set.on_confirm.message.order.fulfillments.agent.organization.creds.type._description.enums
anchor.sub-broker-arn | isa | anchor.distributor-cred-type | basis:declared | asof:fis14-2.1.0 | grounded-in:fis14-2.1.0:attributes/MUTUAL_FUNDS.yaml#attribute_set.on_confirm.message.order.fulfillments.agent.organization.creds.type._description.enums
anchor.ria | not-isa | anchor.distributor-cred-type | basis:declared | asof:fis14-2.1.0 | grounded-in:fis14-2.1.0:validations/index.yaml#_TESTS_.search[SEARCH_AGENT_CREDENTIALS]._RETURN_[VALID_AGENT_CREDS_TYPE_ENUM].enumList
anchor.search | requires | anchor.distributor-cred-type | basis:declared | asof:fis14-2.1.0 | grounded-in:fis14-2.1.0:validations/index.yaml#_TESTS_.search[SEARCH_AGENT_CREDENTIALS]._RETURN_[REQUIRED_AGENT_ORGANIZATION_CREDS].attr
anchor.bap-terms | isa | anchor.tag-group-anchor | basis:declared | asof:fis14-2.1.0 | grounded-in:fis14-2.1.0:validations/index.yaml#_TESTS_.search[SEARCH_BAP_TERMS]._RETURN_[REQUIRED_BAP_TERMS_TAG_GROUP].validTags
anchor.bap-terms | scoped-to | anchor.select | basis:declared | asof:fis14-2.1.0 | grounded-in:fis14-2.1.0:validations/index.yaml#_TESTS_.select[SELECT_BAP_TERMS]._RETURN_[REQUIRED_BAP_TERMS_TAG_GROUP].tagPath
anchor.bap-terms | sent-by | anchor.bap | basis:declared | asof:fis14-2.1.0 | grounded-in:fis14-2.1.0:validations/index.yaml#_TESTS_.search[SEARCH_BAP_TERMS]._RETURN_[REQUIRED_BAP_TERMS_TAG_GROUP].tagPath
anchor.terms-list | isa | anchor.enum-anchor | basis:declared | asof:fis14-2.1.0 | grounded-in:fis14-2.1.0:validations/index.yaml#_TESTS_.search[SEARCH_BAP_TERMS]._RETURN_[REQUIRED_BAP_TERMS_LIST].validValues
anchor.terms-list | scoped-to | anchor.bap-terms | basis:declared | asof:fis14-2.1.0 | grounded-in:fis14-2.1.0:validations/index.yaml#_TESTS_.search[SEARCH_BAP_TERMS]._RETURN_[REQUIRED_BAP_TERMS_LIST]._SCOPE_
anchor.terms-list | scoped-to | anchor.bpp-terms | basis:declared | asof:fis14-2.1.0 | grounded-in:fis14-2.1.0:validations/index.yaml#_TESTS_.on_select[ON_SELECT_BPP_TERMS]._RETURN_[REQUIRED_BPP_TERMS_LIST]._SCOPE_
anchor.bpp-terms | isa | anchor.tag-group-anchor | basis:declared | asof:fis14-2.1.0 | grounded-in:fis14-2.1.0:validations/index.yaml#_TESTS_.on_select[ON_SELECT_BPP_TERMS]._RETURN_[REQUIRED_BPP_TERMS_TAG_GROUP].validTags
anchor.bpp-terms | sent-by | anchor.bpp | basis:declared | asof:fis14-2.1.0 | grounded-in:fis14-2.1.0:attributes/MUTUAL_FUNDS.yaml#attribute_set.on_init.message.order.tags.BPP_TERMS._description.owner
anchor.plan-information | isa | anchor.tag-group-anchor | basis:declared | asof:fis14-2.1.0 | grounded-in:fis14-2.1.0:validations/index.yaml#_TESTS_.on_search[ON_SEARCH_ITEMS_SCHEME_PLAN]._RETURN_[REQUIRED_PLAN_INFORMATION_TAG_GROUP].validTags
anchor.plan-information | scoped-to | anchor.on-select | basis:declared | asof:fis14-2.1.0 | grounded-in:fis14-2.1.0:validations/index.yaml#_TESTS_.on_select[ON_SELECT_ITEMS_TAGS]._RETURN_[REQUIRED_PLAN_INFORMATION_TAG_GROUP].tagPath
anchor.plan-identifiers | isa | anchor.tag-group-anchor | basis:declared | asof:fis14-2.1.0 | grounded-in:fis14-2.1.0:validations/index.yaml#_TESTS_.on_search[ON_SEARCH_ITEMS_SCHEME_PLAN]._RETURN_[REQUIRED_PLAN_IDENTIFIERS_TAG_GROUP].validTags
anchor.plan-identifiers | scoped-to | anchor.on-select | basis:declared | asof:fis14-2.1.0 | grounded-in:fis14-2.1.0:validations/index.yaml#_TESTS_.on_select[ON_SELECT_ITEMS_TAGS]._RETURN_[REQUIRED_PLAN_IDENTIFIERS_TAG_GROUP].tagPath
anchor.plan-identifiers | has-slot | anchor.isin | basis:declared | asof:fis14-2.1.0 | grounded-in:fis14-2.1.0:validations/index.yaml#_TESTS_.on_search[ON_SEARCH_ITEMS_SCHEME_PLAN]._RETURN_[REQUIRED_PLAN_IDENTIFIERS_LIST].validValues
anchor.plan-identifiers | has-slot | anchor.rta-identifier | basis:declared | asof:fis14-2.1.0 | grounded-in:fis14-2.1.0:validations/index.yaml#_TESTS_.on_search[ON_SEARCH_ITEMS_SCHEME_PLAN]._RETURN_[REQUIRED_PLAN_IDENTIFIERS_LIST].validValues
anchor.plan-identifiers | has-slot | anchor.amfi-identifier | basis:declared | asof:fis14-2.1.0 | grounded-in:fis14-2.1.0:validations/index.yaml#_TESTS_.on_search[ON_SEARCH_ITEMS_SCHEME_PLAN]._RETURN_[REQUIRED_PLAN_IDENTIFIERS_LIST].validValues
anchor.plan-options | isa | anchor.tag-group-anchor | basis:declared | asof:fis14-2.1.0 | grounded-in:fis14-2.1.0:validations/index.yaml#_TESTS_.on_search[ON_SEARCH_ITEMS_SCHEME_PLAN]._RETURN_[REQUIRED_PLAN_OPTIONS_TAG_GROUP].validTags
anchor.plan-options | scoped-to | anchor.on-select | basis:declared | asof:fis14-2.1.0 | grounded-in:fis14-2.1.0:validations/index.yaml#_TESTS_.on_select[ON_SELECT_ITEMS_TAGS]._RETURN_[REQUIRED_PLAN_OPTIONS_TAG_GROUP].tagPath
anchor.plan-options | constrains | anchor.plan-variant | basis:declared | asof:fis14-2.1.0 | grounded-in:fis14-2.1.0:validations/index.yaml#_TESTS_.on_search[ON_SEARCH_ITEMS_SCHEME_PLAN]._RETURN_[VALID_PLAN_VALUE_ENUM].enumList
anchor.plan-options | constrains | anchor.payout-option | basis:declared | asof:fis14-2.1.0 | grounded-in:fis14-2.1.0:validations/index.yaml#_TESTS_.on_search[ON_SEARCH_ITEMS_SCHEME_PLAN]._RETURN_[VALID_OPTION_VALUE_ENUM].enumList
anchor.plan-options | constrains | anchor.idcw-option | basis:declared | asof:fis14-2.1.0 | grounded-in:fis14-2.1.0:validations/index.yaml#_TESTS_.on_search[ON_SEARCH_ITEMS_SCHEME_PLAN]._RETURN_[VALID_IDCW_OPTION_VALUE_ENUM].enumList
anchor.threshold-tag-groups | isa | anchor.tag-group-anchor | basis:declared | asof:fis14-2.1.0 | grounded-in:fis14-2.1.0:validations/index.yaml#_TESTS_.on_search[ON_SEARCH_FULFILLMENTS]._RETURN_[REQUIRED_THRESHOLDS_TAG_GROUP].validTags
anchor.threshold-tag-groups | scoped-to | anchor.on-select | basis:declared | asof:fis14-2.1.0 | grounded-in:fis14-2.1.0:validations/index.yaml#_TESTS_.on_select[ON_SELECT_FULFILLMENTS]._RETURN_[REQUIRED_THRESHOLDS_TAG_GROUP].tagPath
anchor.threshold-tag-groups | constrains | anchor.lumpsum | basis:declared | asof:fis14-2.1.0 | grounded-in:fis14-2.1.0:validations/index.yaml#_TESTS_.on_search[ON_SEARCH_FULFILLMENTS_LUMPSUM]._RETURN_[OPTIONAL_LUMPSUM_THRESHOLDS_LIST].validValues
anchor.threshold-tag-groups | constrains | anchor.sip | basis:declared | asof:fis14-2.1.0 | grounded-in:fis14-2.1.0:validations/index.yaml#_TESTS_.on_search[ON_SEARCH_FULFILLMENTS_SIP]._RETURN_[OPTIONAL_SIP_THRESHOLDS_LIST].validValues
anchor.threshold-tag-groups | constrains | anchor.redemption | basis:declared | asof:fis14-2.1.0 | grounded-in:fis14-2.1.0:validations/index.yaml#_TESTS_.on_search[ON_SEARCH_FULFILLMENTS_REDEMPTION]._RETURN_[OPTIONAL_REDEMPTION_THRESHOLDS_LIST].validValues
anchor.threshold-tag-groups | constrains | anchor.swp | basis:declared | asof:fis14-2.1.0 | grounded-in:fis14-2.1.0:validations/index.yaml#_TESTS_.on_search[ON_SEARCH_FULFILLMENTS_SWP]._RETURN_[OPTIONAL_SWP_THRESHOLDS_LIST].validValues
anchor.threshold-tag-groups | constrains | anchor.stp | basis:declared | asof:fis14-2.1.0 | grounded-in:fis14-2.1.0:validations/index.yaml#_TESTS_.on_search[ON_SEARCH_FULFILLMENTS_STP]._RETURN_[OPTIONAL_STP_THRESHOLDS_LIST].validValues
anchor.sip | requires | anchor.sip-frequency | basis:declared | asof:fis14-2.1.0 | grounded-in:fis14-2.1.0:validations/index.yaml#_TESTS_.select[SELECT_FULFILLMENTS_SIP]._RETURN_[REQUIRED_STOPS_SCHEDULE_FREQUENCY].attr
anchor.sip-frequency | isa | anchor.iso8601-repeating-interval | basis:declared | asof:fis14-2.1.0 | grounded-in:fis14-2.1.0:validations/index.yaml#_TESTS_.select[SELECT_FULFILLMENTS_SIP]._RETURN_[VALID_STOPS_SCHEDULE_FREQUENCY_REGEX].reg
anchor.sip-frequency | constrains | anchor.instalment-count | basis:declared | asof:fis14-2.1.0 | grounded-in:fis14-2.1.0:validations/index.yaml#_TESTS_.on_search[ON_SEARCH_FULFILLMENTS_SIP]._RETURN_[OPTIONAL_SIP_THRESHOLDS_LIST].validValues
anchor.quantity-unit | isa | anchor.enum-anchor | basis:declared | asof:fis14-2.1.0 | grounded-in:fis14-2.1.0:validations/index.yaml#_TESTS_.select[SELECT_ITEMS]._RETURN_[REQUIRED_ITEM_QUANTITY]._RETURN_[VALID_QUANTITY_UNIT_ENUM].enumList
anchor.quantity-unit | scoped-to | anchor.payment-currency | basis:declared | asof:fis14-2.1.0 | grounded-in:fis14-2.1.0:validations/index.yaml#_TESTS_.init[INIT_PAYMENTS]._RETURN_[REQUIRED_PAYMENT_PARAMS]._RETURN_[REQUIRED_PAYMENT_PARAMS_CURRENCY].enumList
anchor.quantity-unit | scoped-to | anchor.quote-price | basis:declared | asof:fis14-2.1.0 | grounded-in:fis14-2.1.0:validations/index.yaml#_TESTS_.on_init[ON_INIT_QUOTE]._RETURN_[REQUIRED_QUOTE_PRICE_CURRENCY].enumList
anchor.inr | isa | anchor.quantity-unit | basis:declared | asof:fis14-2.1.0 | grounded-in:fis14-2.1.0:attributes/MUTUAL_FUNDS.yaml#attribute_set.select.message.order.items.quantity.selected.measure.unit._description.enums
anchor.mf-units | isa | anchor.quantity-unit | basis:declared | asof:fis14-2.1.0 | grounded-in:fis14-2.1.0:attributes/MUTUAL_FUNDS.yaml#attribute_set.select.message.order.items.quantity.selected.measure.unit._description.enums
anchor.quantity-unit | constrains | anchor.investment-order | basis:declared | asof:fis14-2.1.0 | grounded-in:fis14-2.1.0:validations/index.yaml#_TESTS_.select[SELECT_ITEMS]._RETURN_[REQUIRED_ITEM_QUANTITY]._RETURN_[REQUIRED_QUANTITY_SELECTED_MEASURE_UNIT].attr
anchor.scheme-plan | isa | anchor.item-code | basis:declared | asof:fis14-2.1.0 | grounded-in:fis14-2.1.0:validations/index.yaml#_TESTS_.on_select[ON_SELECT_ITEMS]._RETURN_[VALID_ITEM_DESCRIPTOR_CODE_ENUM].enumList
anchor.scheme-plan | scoped-to | anchor.on-init | basis:declared | asof:fis14-2.1.0 | grounded-in:fis14-2.1.0:validations/index.yaml#_TESTS_.on_init[ON_INIT_ITEMS]._RETURN_[REQUIRED_ITEM_DESCRIPTOR_CODE].enumList
anchor.scheme-plan | scoped-to | anchor.on-confirm | basis:declared | asof:fis14-2.1.0 | grounded-in:fis14-2.1.0:validations/index.yaml#_TESTS_.on_confirm[ON_CONFIRM_ITEMS]._RETURN_[REQUIRED_ITEM_DESCRIPTOR_CODE].enumList
anchor.scheme-plan | part-of | anchor.scheme | basis:declared | asof:fis14-2.1.0 | grounded-in:fis14-2.1.0:validations/index.yaml#_TESTS_.on_search[ON_SEARCH_ITEMS_SCHEME_PLAN]._RETURN_[REQUIRED_ITEM_PARENT_ITEM_ID].attr
anchor.scheme | isa | anchor.item-code | basis:declared | asof:fis14-2.1.0 | grounded-in:fis14-2.1.0:validations/index.yaml#_TESTS_.on_search[ON_SEARCH_ITEMS_SCHEME]._SCOPE_
anchor.scheme | has-slot | anchor.scheme-information | basis:declared | asof:fis14-2.1.0 | grounded-in:fis14-2.1.0:validations/index.yaml#_TESTS_.on_search[ON_SEARCH_ITEMS_SCHEME]._RETURN_[REQUIRED_SCHEME_INFORMATION_TAG_GROUP].validTags
anchor.scheme-information | constrains | anchor.lockin-period | basis:declared | asof:fis14-2.1.0 | grounded-in:fis14-2.1.0:validations/index.yaml#_TESTS_.on_search[ON_SEARCH_ITEMS_SCHEME]._RETURN_[REQUIRED_SCHEME_INFORMATION_LIST].validValues
anchor.scheme-information | constrains | anchor.nfo-window | basis:declared | asof:fis14-2.1.0 | grounded-in:fis14-2.1.0:validations/index.yaml#_TESTS_.on_search[ON_SEARCH_ITEMS_SCHEME]._RETURN_[REQUIRED_SCHEME_INFORMATION_LIST].validValues
anchor.scheme-information | constrains | anchor.exit-load | basis:declared | asof:fis14-2.1.0 | grounded-in:fis14-2.1.0:validations/index.yaml#_TESTS_.on_search[ON_SEARCH_ITEMS_SCHEME]._RETURN_[REQUIRED_SCHEME_INFORMATION_LIST].validValues
anchor.scheme-information | constrains | anchor.investor-eligibility | basis:declared | asof:fis14-2.1.0 | grounded-in:fis14-2.1.0:validations/index.yaml#_TESTS_.on_search[ON_SEARCH_ITEMS_SCHEME]._RETURN_[REQUIRED_SCHEME_INFORMATION_LIST].validValues
anchor.scheme-plan | not-part-of | anchor.scheme-information | basis:declared | asof:fis14-2.1.0 | grounded-in:fis14-2.1.0:validations/index.yaml#_TESTS_.on_search[ON_SEARCH_ITEMS_SCHEME_PLAN]._SCOPE_
anchor.payment-timing | isa | anchor.enum-anchor | basis:declared | asof:fis14-2.1.0 | grounded-in:fis14-2.1.0:validations/index.yaml#_TESTS_.init[INIT_PAYMENTS]._RETURN_[VALID_PAYMENT_TYPE_ENUM].enumList
anchor.payment-timing | scoped-to | anchor.on-init | basis:declared | asof:fis14-2.1.0 | grounded-in:fis14-2.1.0:validations/index.yaml#_TESTS_.on_init[ON_INIT_PAYMENTS]._RETURN_[REQUIRED_PAYMENT_TYPE].enumList
anchor.payment-timing | scoped-to | anchor.confirm | basis:declared | asof:fis14-2.1.0 | grounded-in:fis14-2.1.0:validations/index.yaml#_TESTS_.confirm[CONFIRM_PAYMENTS]._RETURN_[REQUIRED_PAYMENT_TYPE].enumList
anchor.pre-fulfillment-payment | isa | anchor.payment-timing | basis:declared | asof:fis14-2.1.0 | grounded-in:fis14-2.1.0:attributes/MUTUAL_FUNDS.yaml#attribute_set.init.message.order.payments.type._description.enums
anchor.post-fulfillment-payment | not-isa | anchor.payment-timing-dictionary | basis:declared | asof:fis14-2.1.0 | grounded-in:fis14-2.1.0:attributes/MUTUAL_FUNDS.yaml#attribute_set.init.message.order.payments.type._description.enums
anchor.post-fulfillment-payment | isa | anchor.payment-timing | basis:declared | asof:fis14-2.1.0 | grounded-in:fis14-2.1.0:validations/index.yaml#_TESTS_.init[INIT_PAYMENTS]._RETURN_[VALID_PAYMENT_TYPE_ENUM].enumList
anchor.payment-collector | isa | anchor.enum-anchor | basis:declared | asof:fis14-2.1.0 | grounded-in:fis14-2.1.0:validations/index.yaml#_TESTS_.init[INIT_PAYMENTS]._RETURN_[VALID_PAYMENT_COLLECTED_BY_ENUM].enumList
anchor.payment-collector | scoped-to | anchor.on-confirm | basis:declared | asof:fis14-2.1.0 | grounded-in:fis14-2.1.0:validations/index.yaml#_TESTS_.on_confirm[ON_CONFIRM_PAYMENTS]._RETURN_[REQUIRED_PAYMENT_COLLECTED_BY].enumList
anchor.cancellable-state | isa | anchor.enum-anchor | basis:declared | asof:fis14-2.1.0 | grounded-in:fis14-2.1.0:validations/index.yaml#_TESTS_.on_init[ON_INIT_CANCELLATION_TERMS]._RETURN_[VALID_CANCELLATION_FULFILLMENT_STATE_ENUM].enumList
anchor.cancellable-state | scoped-to | anchor.on-confirm | basis:declared | asof:fis14-2.1.0 | grounded-in:fis14-2.1.0:validations/index.yaml#_TESTS_.on_confirm[ON_CONFIRM_CANCELLATION_TERMS]._RETURN_[REQUIRED_CANCELLATION_TERMS_FULFILLMENT_STATE].enumList
anchor.cancellable-state | constrains | anchor.cancellation-terms | basis:declared | asof:fis14-2.1.0 | grounded-in:fis14-2.1.0:validations/index.yaml#_TESTS_.on_init[ON_INIT_CANCELLATION_TERMS].cancellationpath
anchor.fulfillment-state | isa | anchor.enum-anchor | basis:declared | asof:fis14-2.1.0 | grounded-in:fis14-2.1.0:validations/index.yaml#_TESTS_.on_confirm[ON_CONFIRM_FULFILLMENTS]._RETURN_[VALID_FULFILLMENT_STATE_ENUM].enumList
anchor.cancellable-state | part-of | anchor.fulfillment-state | basis:declared | asof:fis14-2.1.0 | grounded-in:fis14-2.1.0:validations/index.yaml#_TESTS_.on_confirm[ON_CONFIRM_FULFILLMENTS]._RETURN_[VALID_FULFILLMENT_STATE_ENUM].enumList
anchor.ongoing-state | not-isa | anchor.fulfillment-state | basis:declared | asof:fis14-2.1.0 | grounded-in:fis14-2.1.0:validations/index.yaml#_TESTS_.on_confirm[ON_CONFIRM_FULFILLMENTS]._RETURN_[VALID_FULFILLMENT_STATE_ENUM].enumList
anchor.failed-state | not-isa | anchor.fulfillment-state | basis:declared | asof:fis14-2.1.0 | grounded-in:fis14-2.1.0:validations/index.yaml#_TESTS_.on_confirm[ON_CONFIRM_FULFILLMENTS]._RETURN_[VALID_FULFILLMENT_STATE_ENUM].enumList
anchor.fulfillment-state | wasDerivedFrom | anchor.lending-fulfillment-state | basis:inferred | asof:fis14-2.1.0
anchor.order-status | isa | anchor.enum-anchor | basis:declared | asof:fis14-2.1.0 | grounded-in:fis14-2.1.0:validations/index.yaml#_TESTS_.on_confirm[ON_CONFIRM_ORDER]._RETURN_[VALID_ORDER_STATUS_ENUM].enumList
anchor.order-created | isa | anchor.order-status | basis:declared | asof:fis14-2.1.0 | grounded-in:fis14-2.1.0:validations/index.yaml#_TESTS_.on_init[ON_INIT_ORDER]._RETURN_[VALID_ORDER_STATUS_ENUM].enumList
anchor.on-init | causes | anchor.order-created | basis:declared | asof:fis14-2.1.0 | grounded-in:fis14-2.1.0:validations/index.yaml#_TESTS_.on_init[ON_INIT_ORDER]._RETURN_[VALID_ORDER_STATUS_ENUM].enumList
anchor.on-confirm | causes | anchor.order-accepted | basis:declared | asof:fis14-2.1.0 | grounded-in:fis14-2.1.0:validations/index.yaml#_TESTS_.on_confirm[ON_CONFIRM_ORDER]._RETURN_[VALID_ORDER_STATUS_ENUM].enumList
anchor.order-completed | not-isa | anchor.order-status | basis:declared | asof:fis14-2.1.0 | grounded-in:fis14-2.1.0:validations/index.yaml#_TESTS_.on_confirm[ON_CONFIRM_ORDER]._RETURN_[VALID_ORDER_STATUS_ENUM].enumList
anchor.payment-status | isa | anchor.enum-anchor | basis:declared | asof:fis14-2.1.0 | grounded-in:fis14-2.1.0:validations/index.yaml#_TESTS_.on_confirm[ON_CONFIRM_PAYMENTS]._RETURN_[VALID_PAYMENT_STATUS_ENUM].enumList
anchor.payment-failed | not-isa | anchor.payment-status | basis:declared | asof:fis14-2.1.0 | grounded-in:fis14-2.1.0:validations/index.yaml#_TESTS_.on_confirm[ON_CONFIRM_PAYMENTS]._RETURN_[VALID_PAYMENT_STATUS_ENUM].enumList
anchor.payment-failed | isa | anchor.payment-status-dictionary | basis:declared | asof:fis14-2.1.0 | grounded-in:fis14-2.1.0:attributes/MUTUAL_FUNDS.yaml#attribute_set.on_confirm.message.order.payments.status._description.enums
anchor.payment-timing-dictionary | part-of | anchor.payment-timing | basis:declared | asof:fis14-2.1.0 | grounded-in:fis14-2.1.0:attributes/MUTUAL_FUNDS.yaml#attribute_set.init.message.order.payments.type._description.enums
anchor.payment-status-dictionary | isa | anchor.attribute-dictionary | basis:declared | asof:fis14-2.1.0 | grounded-in:fis14-2.1.0:attributes/MUTUAL_FUNDS.yaml#attribute_set.on_confirm.message.order.payments.status._description.enums
anchor.fulfillment-type-dictionary | isa | anchor.attribute-dictionary | basis:declared | asof:fis14-2.1.0 | grounded-in:fis14-2.1.0:attributes/MUTUAL_FUNDS.yaml#attribute_set.on_search.message.catalog.providers.fulfillments.type._description.enums
anchor.order-status-dictionary | isa | anchor.attribute-dictionary | basis:declared | asof:fis14-2.1.0 | grounded-in:fis14-2.1.0:attributes/MUTUAL_FUNDS.yaml#attribute_set.on_confirm.message.order.status._description.enums
anchor.order-completed | isa | anchor.order-status-dictionary | basis:declared | asof:fis14-2.1.0 | grounded-in:fis14-2.1.0:attributes/MUTUAL_FUNDS.yaml#attribute_set.on_confirm.message.order.status._description.enums
anchor.attribute-dictionary | not-part-of | anchor.l1-payload-validation | basis:authority | asof:fis14-2.1.0 | grounded-in:workbench:decisions/adr-0030-attributes-human-not-ai.md
anchor.attribute-dictionary | wasAttributedTo | anchor.human-schematic-author | basis:authority | asof:fis14-2.1.0 | grounded-in:workbench:decisions/adr-0030-attributes-human-not-ai.md
anchor.update | not-part-of | anchor.l1-payload-validation | basis:declared | asof:fis14-2.1.0 | grounded-in:fis14-2.1.0:validations/index.yaml#_TESTS_.update
anchor.on-update | not-part-of | anchor.l1-payload-validation | basis:declared | asof:fis14-2.1.0 | grounded-in:fis14-2.1.0:validations/index.yaml#_TESTS_.on_update
anchor.status | not-part-of | anchor.l1-payload-validation | basis:declared | asof:fis14-2.1.0 | grounded-in:fis14-2.1.0:validations/index.yaml#_TESTS_.status
anchor.on-status | not-part-of | anchor.l1-payload-validation | basis:declared | asof:fis14-2.1.0 | grounded-in:fis14-2.1.0:validations/index.yaml#_TESTS_.on_status
anchor.xinput | isa | anchor.validation-block | basis:declared | asof:fis14-2.1.0 | grounded-in:fis14-2.1.0:validations/index.yaml#_TESTS_.on_select[ON_SELECT_XINPUT].xinputpath
anchor.xinput | scoped-to | anchor.init | basis:declared | asof:fis14-2.1.0 | grounded-in:fis14-2.1.0:validations/index.yaml#_TESTS_.init[INIT_XINPUT].xinputpath
anchor.xinput | sent-by | anchor.bpp | basis:declared | asof:fis14-2.1.0 | grounded-in:fis14-2.1.0:attributes/MUTUAL_FUNDS.yaml#attribute_set.on_select.message.order.xinput.form._description.owner
anchor.xinput | has-slot | anchor.form-id | basis:declared | asof:fis14-2.1.0 | grounded-in:fis14-2.1.0:validations/index.yaml#_TESTS_.on_select[ON_SELECT_XINPUT]._RETURN_[REQUIRED_XINPUT_FORM_ID].attr
anchor.xinput | has-slot | anchor.form-index | basis:declared | asof:fis14-2.1.0 | grounded-in:fis14-2.1.0:validations/index.yaml#_TESTS_.on_select[ON_SELECT_XINPUT]._RETURN_[OPTIONAL_XINPUT_HEAD_INDEX].headpath
anchor.form-index | constrains | anchor.multi-page-form | basis:declared | asof:fis14-2.1.0 | grounded-in:fis14-2.1.0:validations/index.yaml#_TESTS_.on_select[ON_SELECT_XINPUT]._RETURN_[OPTIONAL_XINPUT_HEAD_INDEX]._RETURN_[REQUIRED_XINPUT_HEAD_INDEX_MAX].attr
anchor.xinput-headings | isa | anchor.enum-anchor | basis:declared | asof:fis14-2.1.0 | grounded-in:fis14-2.1.0:validations/index.yaml#_TESTS_.on_select[ON_SELECT_XINPUT]._RETURN_[VALID_XINPUT_HEADINGS_ENUM].enumList
anchor.form-mime-type | isa | anchor.enum-anchor | basis:declared | asof:fis14-2.1.0 | grounded-in:fis14-2.1.0:validations/index.yaml#_TESTS_.on_select[ON_SELECT_XINPUT]._RETURN_[VALID_XINPUT_FORM_MIME_TYPE_ENUM].enumList
anchor.init | requires | anchor.form-submission-id | basis:declared | asof:fis14-2.1.0 | grounded-in:fis14-2.1.0:validations/index.yaml#_TESTS_.init[INIT_XINPUT]._RETURN_[REQUIRED_XINPUT_FORM_RESPONSE_SUBMISSION_ID].attr
anchor.form-submission-id | wasGeneratedBy | anchor.form-submission | basis:declared | asof:fis14-2.1.0 | grounded-in:fis14-2.1.0:attributes/MUTUAL_FUNDS.yaml#attribute_set.on_select.message.order.xinput.form_response.status._description.enums
anchor.form-submission | isa | anchor.out-of-band-step | basis:authority | asof:fis14-2.1.0 | grounded-in:workbench:frames/flow-state-machine.md
anchor.form-submission | precedes | anchor.select | basis:declared | asof:fis14-2.1.0 | grounded-in:fis14-2.1.0:flows/MUTUAL FUNDS/SIP_Creation_New_Folio.yaml#steps[select_2]
anchor.investor | requires | anchor.pan | basis:declared | asof:fis14-2.1.0 | grounded-in:fis14-2.1.0:attributes/MUTUAL_FUNDS.yaml#attribute_set.select.message.order.fulfillments.customer.person.id._description.usage
anchor.investor | sent-by | anchor.bap | basis:declared | asof:fis14-2.1.0 | grounded-in:fis14-2.1.0:attributes/MUTUAL_FUNDS.yaml#attribute_set.select.message.order.fulfillments.customer.person.id._description.owner
anchor.investor | isa | anchor.customer | basis:declared | asof:fis14-2.1.0 | grounded-in:fis14-2.1.0:validations/index.yaml#_TESTS_.select[SELECT_FULFILLMENTS_SIP]._RETURN_[REQUIRED_CUSTOMER_PERSON_ID].attr
anchor.distributor | isa | anchor.agent | basis:declared | asof:fis14-2.1.0 | grounded-in:fis14-2.1.0:validations/index.yaml#_TESTS_.select[SELECT_FULFILLMENTS_SIP]._RETURN_[REQUIRED_AGENT_PERSON_ID].attr
anchor.distributor | requires | anchor.euin | basis:declared | asof:fis14-2.1.0 | grounded-in:fis14-2.1.0:attributes/MUTUAL_FUNDS.yaml#attribute_set.select.message.order.fulfillments.agent.person.id._description.usage
anchor.distributor | sent-by | anchor.bap | basis:declared | asof:fis14-2.1.0 | grounded-in:fis14-2.1.0:attributes/MUTUAL_FUNDS.yaml#attribute_set.select.message.order.fulfillments.agent.organization.creds._description.owner
anchor.folio | isa | anchor.customer-credential | basis:declared | asof:fis14-2.1.0 | grounded-in:fis14-2.1.0:validations/index.yaml#_TESTS_.init[INIT_FULFILLMENTS]._RETURN_[VALID_FULFILLMENT_CUSTOMER_CREDS_TYPE_ENUM].enumList
anchor.init | requires | anchor.customer-credential | basis:declared | asof:fis14-2.1.0 | grounded-in:fis14-2.1.0:validations/index.yaml#_TESTS_.init[INIT_FULFILLMENTS]._RETURN_[REQUIRED_FULFILLMENT_CUSTOMER_CREDS].attr
anchor.folio-information | isa | anchor.tag-group-anchor | basis:declared | asof:fis14-2.1.0 | grounded-in:fis14-2.1.0:flows/MUTUAL FUNDS/SIP_Creation_Existing_Folio.yaml#steps[on_select_existing_folio].mock.defaultPayload.message.order.fulfillments[0].tags[0].descriptor.code
anchor.folio-information | has-slot | anchor.two-factor-contact | basis:declared | asof:fis14-2.1.0 | grounded-in:fis14-2.1.0:flows/MUTUAL FUNDS/SIP_Creation_Existing_Folio.yaml#steps[on_select_existing_folio].mock.defaultPayload.message.order.fulfillments[0].tags[0].list
anchor.on-confirm | requires | anchor.document-set | basis:declared | asof:fis14-2.1.0 | grounded-in:fis14-2.1.0:validations/index.yaml#_TESTS_.on_confirm[ON_CONFIRM_DOCUMENTS].documentspath
anchor.document-set | constrains | anchor.document-mime-type | basis:declared | asof:fis14-2.1.0 | grounded-in:fis14-2.1.0:validations/index.yaml#_TESTS_.on_confirm[ON_CONFIRM_DOCUMENTS]._RETURN_[REQUIRED_DOCUMENT_MIME_TYPE].enumList
anchor.quote | scoped-to | anchor.on-init | basis:declared | asof:fis14-2.1.0 | grounded-in:fis14-2.1.0:validations/index.yaml#_TESTS_.on_init[ON_INIT_QUOTE].quotepath
anchor.quote | scoped-to | anchor.on-confirm | basis:declared | asof:fis14-2.1.0 | grounded-in:fis14-2.1.0:validations/index.yaml#_TESTS_.on_confirm[ON_CONFIRM_QUOTE].quotepath
error.distributor-not-empanelled | sent-by | anchor.bpp | basis:declared | asof:fis14-2.1.0 | grounded-in:fis14-2.1.0:errors/index.yaml#code[822001].From
error.distributor-not-empanelled | causes | anchor.empty-catalog | basis:declared | asof:fis14-2.1.0 | grounded-in:fis14-2.1.0:errors/index.yaml#code[822001].Description
error.distributor-not-empanelled | scoped-to | anchor.on-search | basis:declared | asof:fis14-2.1.0 | grounded-in:fis14-2.1.0:errors/index.yaml#code[822001].Description
error.distributor-license-invalid | constrains | anchor.arn | basis:declared | asof:fis14-2.1.0 | grounded-in:fis14-2.1.0:errors/index.yaml#code[822002].Description
error.sub-broker-license-invalid | constrains | anchor.sub-broker-arn | basis:declared | asof:fis14-2.1.0 | grounded-in:fis14-2.1.0:errors/index.yaml#code[822003].Description
error.euin-not-mapped | constrains | anchor.euin | basis:declared | asof:fis14-2.1.0 | grounded-in:fis14-2.1.0:errors/index.yaml#code[822004].Description
error.euin-not-mapped | requires | anchor.arn | basis:declared | asof:fis14-2.1.0 | grounded-in:fis14-2.1.0:errors/index.yaml#code[822004].Description
error.euin-invalid | constrains | anchor.euin | basis:declared | asof:fis14-2.1.0 | grounded-in:fis14-2.1.0:errors/index.yaml#code[822005].Description
error.investor-not-supported | constrains | anchor.investor-eligibility | basis:declared | asof:fis14-2.1.0 | grounded-in:fis14-2.1.0:errors/index.yaml#code[822006].Description
error.investor-not-supported | causes | anchor.tax-status-rejection | basis:declared | asof:fis14-2.1.0 | grounded-in:fis14-2.1.0:errors/index.yaml#code[822006].Description
error.investor-kyc-pending | constrains | anchor.kyc-fulfillment | basis:declared | asof:fis14-2.1.0 | grounded-in:fis14-2.1.0:errors/index.yaml#code[822007].Description
error.investor-kyc-pending | sent-by | anchor.bpp | basis:declared | asof:fis14-2.1.0 | grounded-in:fis14-2.1.0:errors/index.yaml#code[822007].From
error.payout-bank-verification-failure | constrains | anchor.payout-bank-account | basis:declared | asof:fis14-2.1.0 | grounded-in:fis14-2.1.0:errors/index.yaml#code[822008].Description
error.investor-data-verification-failure | constrains | anchor.investor | basis:declared | asof:fis14-2.1.0 | grounded-in:fis14-2.1.0:errors/index.yaml#code[822009].Description
error.invalid-folio | constrains | anchor.folio | basis:declared | asof:fis14-2.1.0 | grounded-in:fis14-2.1.0:errors/index.yaml#code[822010].Description
error.invalid-payout-account-for-redemption | scoped-to | anchor.redemption | basis:declared | asof:fis14-2.1.0 | grounded-in:fis14-2.1.0:errors/index.yaml#code[822011].Description
error.thresholds-not-matched | constrains | anchor.threshold-tag-groups | basis:declared | asof:fis14-2.1.0 | grounded-in:fis14-2.1.0:errors/index.yaml#code[822012].Description
error.scheme-not-active | constrains | anchor.scheme | basis:declared | asof:fis14-2.1.0 | grounded-in:fis14-2.1.0:errors/index.yaml#code[822013].Description
error.scheme-not-active | causes | anchor.catalog-refresh | basis:declared | asof:fis14-2.1.0 | grounded-in:fis14-2.1.0:errors/index.yaml#code[822013].Description
error.fulfillment-not-allowed | constrains | anchor.fulfillment-type | basis:declared | asof:fis14-2.1.0 | grounded-in:fis14-2.1.0:errors/index.yaml#code[822014].Description
error.fulfillment-not-allowed | causes | anchor.catalog-refresh | basis:declared | asof:fis14-2.1.0 | grounded-in:fis14-2.1.0:errors/index.yaml#code[822014].Description
error.two-factor-mismatch | constrains | anchor.two-factor-contact | basis:declared | asof:fis14-2.1.0 | grounded-in:fis14-2.1.0:errors/index.yaml#code[822015].Description
error.two-factor-mismatch | requires | anchor.folio | basis:declared | asof:fis14-2.1.0 | grounded-in:fis14-2.1.0:errors/index.yaml#code[822015].Description
error.payment-source-bank-verification-failure | constrains | anchor.source-bank-account | basis:declared | asof:fis14-2.1.0 | grounded-in:fis14-2.1.0:errors/index.yaml#code[822016].Description
error.mandate-amount-invalid | constrains | anchor.mandate-limit | basis:declared | asof:fis14-2.1.0 | grounded-in:fis14-2.1.0:errors/index.yaml#code[822017].Description
anchor.mandate-limit | constrains | anchor.sip-instalment | basis:declared | asof:fis14-2.1.0 | grounded-in:fis14-2.1.0:errors/index.yaml#code[822017].Description
error.fatal-error | sent-by | anchor.bpp | basis:declared | asof:fis14-2.1.0 | grounded-in:fis14-2.1.0:errors/index.yaml#code[822018].From
error.cross-call-data-mismatch | constrains | anchor.transaction-id | basis:declared | asof:fis14-2.1.0 | grounded-in:fis14-2.1.0:errors/index.yaml#code[822019].Description
error.cross-call-data-mismatch | scoped-to | anchor.init | basis:declared | asof:fis14-2.1.0 | grounded-in:fis14-2.1.0:errors/index.yaml#code[822019].Description
anchor.fis14-error-set | sent-by | anchor.bpp | basis:declared | asof:fis14-2.1.0 | grounded-in:fis14-2.1.0:errors/index.yaml#code
anchor.fis14-error-set | not-sent-by | anchor.bap | basis:declared | asof:fis14-2.1.0 | grounded-in:fis14-2.1.0:errors/index.yaml#code
anchor.fis14-error-set | isa | anchor.nack-payload | basis:observed-live | asof:fis14-2.1.0 | grounded-in:workbench:scripts/onix-request-lifecycle.md
anchor.form-mime-type-multi | isa | anchor.form-mime-type | basis:declared | asof:fis14-2.1.0 | !untethered
anchor.form-multiple-submissions | has-slot | anchor.form | basis:declared | asof:fis14-2.1.0 | !untethered
anchor.refund-payment | isa | anchor.payment-timing | basis:declared | asof:fis14-2.1.0 | !untethered
anchor.search-flow-family | isa | anchor.catalog-discovery | basis:declared | asof:fis14-2.1.0 | grounded-in:fis14-2.1.0:flows/index.yaml#flows[Main_Search].tags
anchor.lumpsum-flow-family | isa | anchor.investment-order | basis:declared | asof:fis14-2.1.0 | grounded-in:fis14-2.1.0:flows/index.yaml#flows[Lumpsum_New_Folio].tags
anchor.redemption-flow-family | isa | anchor.investment-order | basis:declared | asof:fis14-2.1.0 | grounded-in:fis14-2.1.0:flows/index.yaml#flows[Redemption_By_Amount].tags
anchor.sip-setup-flow-family | isa | anchor.investment-order | basis:declared | asof:fis14-2.1.0 | grounded-in:fis14-2.1.0:flows/index.yaml#flows[SIP_Creation_New_Folio].tags
anchor.sip-lifecycle-flow-family | isa | anchor.investment-order | basis:declared | asof:fis14-2.1.0 | grounded-in:fis14-2.1.0:flows/index.yaml#flows[SIP_Instalment].tags
anchor.sip-setup-flow-family | precedes | anchor.sip-lifecycle-flow-family | basis:declared | asof:fis14-2.1.0 | grounded-in:fis14-2.1.0:flows/index.yaml#flows[SIP_Instalment].description
flow.main-search | isa | anchor.search-flow-family | basis:declared | asof:fis14-2.1.0 | grounded-in:fis14-2.1.0:flows/index.yaml#flows[Main_Search].tags
flow.main-search | isa | anchor.user-initiated-journey | basis:declared | asof:fis14-2.1.0 | grounded-in:fis14-2.1.0:flows/index.yaml#flows[Main_Search].tags
flow.main-search | causes | anchor.catalog-refresh | basis:declared | asof:fis14-2.1.0 | grounded-in:fis14-2.1.0:flows/MUTUAL FUNDS/Main_Search.yaml#steps[on_search]
flow.main-search | requires | anchor.distributor-cred-type | basis:declared | asof:fis14-2.1.0 | grounded-in:fis14-2.1.0:flows/MUTUAL FUNDS/Main_Search.yaml#steps[search].mock.defaultPayload.message.intent.fulfillment.agent.organization.creds
flow.main-search | not-requires | anchor.investor | basis:declared | asof:fis14-2.1.0 | grounded-in:fis14-2.1.0:flows/MUTUAL FUNDS/Main_Search.yaml#steps[search].mock.defaultPayload.message.intent
flow.search-incremental-pull | isa | anchor.search-flow-family | basis:declared | asof:fis14-2.1.0 | grounded-in:fis14-2.1.0:flows/index.yaml#flows[Search_Incremental_Pull].tags
flow.search-incremental-pull | isa | anchor.user-initiated-journey | basis:declared | asof:fis14-2.1.0 | grounded-in:fis14-2.1.0:flows/index.yaml#flows[Search_Incremental_Pull].tags
flow.search-incremental-pull | causes | anchor.incremental-catalog-pull | basis:declared | asof:fis14-2.1.0 | grounded-in:fis14-2.1.0:flows/MUTUAL FUNDS/Search_Incremental_Pull.yaml#steps[search_incremental_pull]
anchor.incremental-catalog-pull | requires | anchor.transaction-id | basis:declared | asof:fis14-2.1.0 | grounded-in:fis14-2.1.0:flows/MUTUAL FUNDS/Search_Incremental_Pull.yaml#transaction_data.transaction_id
anchor.sip-details | scoped-to | anchor.incremental-catalog-pull | basis:declared | asof:fis14-2.1.0 | grounded-in:fis14-2.1.0:flows/MUTUAL FUNDS/Search_Incremental_Pull.yaml#steps[on_search_incremental_pull]
anchor.sip-details | isa | anchor.threshold-tag-groups | basis:declared | asof:fis14-2.1.0 | grounded-in:fis14-2.1.0:validations/index.yaml#_TESTS_.on_search[ON_SEARCH_FULFILLMENTS]._RETURN_[REQUIRED_THRESHOLDS_TAG_GROUP].validTags
flow.lumpsum-existing-folio | isa | anchor.lumpsum-flow-family | basis:declared | asof:fis14-2.1.0 | grounded-in:fis14-2.1.0:flows/index.yaml#flows[Lumpsum_Existing_Folio].tags
flow.lumpsum-existing-folio | isa | anchor.user-initiated-journey | basis:declared | asof:fis14-2.1.0 | grounded-in:fis14-2.1.0:flows/index.yaml#flows[Lumpsum_Existing_Folio].tags
flow.lumpsum-existing-folio | requires | anchor.folio | basis:declared | asof:fis14-2.1.0 | grounded-in:fis14-2.1.0:flows/index.yaml#flows[Lumpsum_Existing_Folio].description
flow.lumpsum-existing-folio | not-requires | anchor.investor-details-form | basis:declared | asof:fis14-2.1.0 | grounded-in:fis14-2.1.0:flows/MUTUAL FUNDS/Lumpsum_Existing_Folio.yaml#steps
anchor.payment-mandate-form | part-of | flow.lumpsum-existing-folio | basis:declared | asof:fis14-2.1.0 | grounded-in:fis14-2.1.0:flows/MUTUAL FUNDS/Lumpsum_Existing_Folio.yaml#steps[payment_mandate_form]
flow.lumpsum-existing-folio | causes | anchor.order-completed | basis:declared | asof:fis14-2.1.0 | grounded-in:fis14-2.1.0:flows/MUTUAL FUNDS/Lumpsum_Existing_Folio.yaml#steps[on_update_unsolicited_existing_folio]
flow.lumpsum-new-folio | isa | anchor.lumpsum-flow-family | basis:declared | asof:fis14-2.1.0 | grounded-in:fis14-2.1.0:flows/index.yaml#flows[Lumpsum_New_Folio].tags
flow.lumpsum-new-folio | isa | anchor.user-initiated-journey | basis:declared | asof:fis14-2.1.0 | grounded-in:fis14-2.1.0:flows/index.yaml#flows[Lumpsum_New_Folio].tags
flow.lumpsum-new-folio | requires | anchor.investor-details-form | basis:declared | asof:fis14-2.1.0 | grounded-in:fis14-2.1.0:flows/MUTUAL FUNDS/Lumpsum_New_Folio.yaml#steps[investor_details_form]
flow.lumpsum-new-folio | causes | anchor.folio-creation | basis:declared | asof:fis14-2.1.0 | grounded-in:fis14-2.1.0:flows/index.yaml#flows[Lumpsum_New_Folio].description
anchor.investor-details-form | isa | anchor.html-form-step | basis:declared | asof:fis14-2.1.0 | grounded-in:fis14-2.1.0:flows/MUTUAL FUNDS/Lumpsum_New_Folio.yaml#steps[investor_details_form].api
anchor.investor-details-form | precedes | anchor.folio-creation | basis:declared | asof:fis14-2.1.0 | grounded-in:fis14-2.1.0:flows/MUTUAL FUNDS/Lumpsum_New_Folio.yaml#steps[select_2]
anchor.html-form-step | isa | anchor.out-of-band-step | basis:authority | asof:fis14-2.1.0 | grounded-in:workbench:frames/flow-state-machine.md
anchor.payment-url-form | isa | anchor.dynamic-form-step | basis:declared | asof:fis14-2.1.0 | grounded-in:fis14-2.1.0:flows/MUTUAL FUNDS/Lumpsum_New_Folio.yaml#steps[payment_url_form].api
anchor.dynamic-form-step | isa | anchor.out-of-band-step | basis:authority | asof:fis14-2.1.0 | grounded-in:workbench:frames/flow-state-machine.md
flow.lumpsum-new-folio-with-kyc | isa | anchor.lumpsum-flow-family | basis:declared | asof:fis14-2.1.0 | grounded-in:fis14-2.1.0:flows/index.yaml#flows[Lumpsum_New_Folio_With_KYC].tags
flow.lumpsum-new-folio-with-kyc | isa | anchor.user-initiated-journey | basis:declared | asof:fis14-2.1.0 | grounded-in:fis14-2.1.0:flows/index.yaml#flows[Lumpsum_New_Folio_With_KYC].tags
flow.lumpsum-new-folio-with-kyc | requires | anchor.kyc-fulfillment | basis:declared | asof:fis14-2.1.0 | grounded-in:fis14-2.1.0:flows/MUTUAL FUNDS/Lumpsum_New_Folio_With_KYC.yaml#steps[kyc_details_form]
flow.lumpsum-new-folio-with-kyc | requires | anchor.esign | basis:declared | asof:fis14-2.1.0 | grounded-in:fis14-2.1.0:flows/MUTUAL FUNDS/Lumpsum_New_Folio_With_KYC.yaml#steps[E_sign_verification_status]
anchor.kyc-fulfillment | precedes | anchor.esign | basis:declared | asof:fis14-2.1.0 | grounded-in:fis14-2.1.0:flows/MUTUAL FUNDS/Lumpsum_New_Folio_With_KYC.yaml#steps[select_esign]
anchor.esign | precedes | anchor.init | basis:declared | asof:fis14-2.1.0 | grounded-in:fis14-2.1.0:flows/MUTUAL FUNDS/Lumpsum_New_Folio_With_KYC.yaml#steps[select_final]
anchor.kyc-verification-status | isa | anchor.dynamic-form-step | basis:declared | asof:fis14-2.1.0 | grounded-in:fis14-2.1.0:flows/MUTUAL FUNDS/Lumpsum_New_Folio_With_KYC.yaml#steps[verification_status].api
anchor.kyc-verification-status | causes | anchor.on-status | basis:declared | asof:fis14-2.1.0 | grounded-in:fis14-2.1.0:flows/MUTUAL FUNDS/Lumpsum_New_Folio_With_KYC.yaml#steps[on_status_unsolicited].unsolicited
flow.lumpsum-payment-by-buyer-app | isa | anchor.lumpsum-flow-family | basis:declared | asof:fis14-2.1.0 | grounded-in:fis14-2.1.0:flows/index.yaml#flows[Lumpsum_Payment_By_Buyer_App].tags
flow.lumpsum-payment-by-buyer-app | isa | anchor.user-initiated-journey | basis:declared | asof:fis14-2.1.0 | grounded-in:fis14-2.1.0:flows/index.yaml#flows[Lumpsum_Payment_By_Buyer_App].tags
flow.lumpsum-payment-by-buyer-app | not-isa | anchor.reportable-flow | basis:declared | asof:fis14-2.1.0 | grounded-in:fis14-2.1.0:flows/index.yaml#flows[Lumpsum_Payment_By_Buyer_App].tags
flow.lumpsum-payment-by-buyer-app | requires | anchor.settlement-details | basis:declared | asof:fis14-2.1.0 | grounded-in:fis14-2.1.0:flows/MUTUAL FUNDS/Lumpsum_Payment_By_Buyer_App.yaml#steps[update_buyer_payment].mock.defaultPayload.message.order.payments
anchor.settlement-details | scoped-to | anchor.update | basis:declared | asof:fis14-2.1.0 | grounded-in:fis14-2.1.0:flows/MUTUAL FUNDS/Lumpsum_Payment_By_Buyer_App.yaml#steps[update_buyer_payment].mock.defaultPayload.message.update_target
anchor.settlement-details | has-slot | anchor.utr | basis:declared | asof:fis14-2.1.0 | grounded-in:fis14-2.1.0:flows/MUTUAL FUNDS/Lumpsum_Payment_By_Buyer_App.yaml#steps[update_buyer_payment].mock.defaultPayload.message.order.payments[0].tags
anchor.update | causes | anchor.payment-collector | basis:declared | asof:fis14-2.1.0 | grounded-in:fis14-2.1.0:flows/MUTUAL FUNDS/Lumpsum_Payment_By_Buyer_App.yaml#steps[update_buyer_payment].mock.defaultPayload.message.order.payments[0].collected_by
flow.lumpsum-payment-retry | isa | anchor.lumpsum-flow-family | basis:declared | asof:fis14-2.1.0 | grounded-in:fis14-2.1.0:flows/index.yaml#flows[Lumpsum_Payment_Retry].tags
flow.lumpsum-payment-retry | isa | anchor.hybrid-journey | basis:declared | asof:fis14-2.1.0 | grounded-in:fis14-2.1.0:flows/index.yaml#flows[Lumpsum_Payment_Retry].tags
flow.lumpsum-payment-retry | not-isa | anchor.reportable-flow | basis:declared | asof:fis14-2.1.0 | grounded-in:fis14-2.1.0:flows/index.yaml#flows[Lumpsum_Payment_Retry].tags
anchor.payment-failure | causes | anchor.on-update | basis:declared | asof:fis14-2.1.0 | grounded-in:fis14-2.1.0:flows/MUTUAL FUNDS/Lumpsum_Payment_Retry.yaml#steps[on_update_unsolicited_failed].unsolicited
anchor.payment-failure | precedes | anchor.payment-retry | basis:declared | asof:fis14-2.1.0 | grounded-in:fis14-2.1.0:flows/MUTUAL FUNDS/Lumpsum_Payment_Retry.yaml#steps[update_payment_retry]
anchor.payment-retry | causes | anchor.payment-url-form | basis:declared | asof:fis14-2.1.0 | grounded-in:fis14-2.1.0:flows/MUTUAL FUNDS/Lumpsum_Payment_Retry.yaml#steps[retry_payment_url_form]
anchor.payment-failure | has-slot | anchor.failure-reason | basis:declared | asof:fis14-2.1.0 | grounded-in:fis14-2.1.0:flows/MUTUAL FUNDS/Lumpsum_Payment_Retry.yaml#steps[on_update_unsolicited_failed].examples[0].payload.message.order.payments[0].tags
flow.redemption-by-amount | isa | anchor.redemption-flow-family | basis:declared | asof:fis14-2.1.0 | grounded-in:fis14-2.1.0:flows/index.yaml#flows[Redemption_By_Amount].tags
flow.redemption-by-amount | isa | anchor.user-initiated-journey | basis:declared | asof:fis14-2.1.0 | grounded-in:fis14-2.1.0:flows/index.yaml#flows[Redemption_By_Amount].tags
flow.redemption-by-amount | requires | anchor.inr | basis:declared | asof:fis14-2.1.0 | grounded-in:fis14-2.1.0:flows/MUTUAL FUNDS/Redemption_By_Amount.yaml#steps[select_redemption].mock.defaultPayload.message.order.items[0].quantity.selected.measure.unit
flow.redemption-by-units | isa | anchor.redemption-flow-family | basis:declared | asof:fis14-2.1.0 | grounded-in:fis14-2.1.0:flows/index.yaml#flows[Redemption_By_Units].tags
flow.redemption-by-units | isa | anchor.user-initiated-journey | basis:declared | asof:fis14-2.1.0 | grounded-in:fis14-2.1.0:flows/index.yaml#flows[Redemption_By_Units].tags
flow.redemption-by-units | not-requires | anchor.mf-units | basis:declared | asof:fis14-2.1.0 | grounded-in:fis14-2.1.0:flows/MUTUAL FUNDS/Redemption_By_Units.yaml#steps[select_redemption].mock.defaultPayload.message.order.items[0].quantity.selected.measure.unit
flow.redemption-redeem-all | isa | anchor.redemption-flow-family | basis:declared | asof:fis14-2.1.0 | grounded-in:fis14-2.1.0:flows/index.yaml#flows[Redemption_Redeem_All].tags
flow.redemption-redeem-all | isa | anchor.user-initiated-journey | basis:declared | asof:fis14-2.1.0 | grounded-in:fis14-2.1.0:flows/index.yaml#flows[Redemption_Redeem_All].tags
flow.redemption-redeem-all | wasDerivedFrom | flow.redemption-by-amount | basis:declared | asof:fis14-2.1.0 | grounded-in:fis14-2.1.0:flows/MUTUAL FUNDS/Redemption_Redeem_All.yaml#steps[select_redemption]
flow.redemption-by-units | wasDerivedFrom | flow.redemption-by-amount | basis:declared | asof:fis14-2.1.0 | grounded-in:fis14-2.1.0:flows/MUTUAL FUNDS/Redemption_By_Units.yaml#steps[select_redemption]
anchor.redemption-variant | constrains | anchor.quantity-unit | basis:inferred | asof:fis14-2.1.0
anchor.redemption | requires | anchor.payout-bank-account | basis:declared | asof:fis14-2.1.0 | grounded-in:fis14-2.1.0:flows/MUTUAL FUNDS/Redemption_By_Amount.yaml#steps[init_redemption].mock.defaultPayload.message.order.fulfillments[0].tags
anchor.redemption | not-requires | anchor.xinput | basis:declared | asof:fis14-2.1.0 | grounded-in:fis14-2.1.0:flows/MUTUAL FUNDS/Redemption_By_Amount.yaml#steps
anchor.redemption | causes | anchor.unit-allocation-reversal | basis:declared | asof:fis14-2.1.0 | grounded-in:fis14-2.1.0:flows/MUTUAL FUNDS/Redemption_By_Amount.yaml#steps[on_update_redemption].mock.defaultPayload.message.order.items[0].quantity.allocated
anchor.redemption | causes | anchor.exit-load | basis:declared | asof:fis14-2.1.0 | grounded-in:fis14-2.1.0:flows/MUTUAL FUNDS/Redemption_By_Amount.yaml#steps[on_update_redemption].mock.defaultPayload.message.order.quote.breakup
flow.redemption-by-amount | causes | anchor.order-completed | basis:declared | asof:fis14-2.1.0 | grounded-in:fis14-2.1.0:flows/MUTUAL FUNDS/Redemption_By_Amount.yaml#steps[on_update_redemption].mock.defaultPayload.message.order.status
flow.sip-creation-existing-folio | isa | anchor.sip-setup-flow-family | basis:declared | asof:fis14-2.1.0 | grounded-in:fis14-2.1.0:flows/index.yaml#flows[SIP_Creation_Existing_Folio].tags
flow.sip-creation-existing-folio | isa | anchor.user-initiated-journey | basis:declared | asof:fis14-2.1.0 | grounded-in:fis14-2.1.0:flows/index.yaml#flows[SIP_Creation_Existing_Folio].tags
flow.sip-creation-existing-folio | requires | anchor.folio | basis:declared | asof:fis14-2.1.0 | grounded-in:fis14-2.1.0:flows/index.yaml#flows[SIP_Creation_Existing_Folio].description
flow.sip-creation-existing-folio | not-requires | anchor.investor-details-form | basis:declared | asof:fis14-2.1.0 | grounded-in:fis14-2.1.0:flows/MUTUAL FUNDS/SIP_Creation_Existing_Folio.yaml#steps
flow.sip-creation-existing-folio | requires | anchor.folio-information | basis:declared | asof:fis14-2.1.0 | grounded-in:fis14-2.1.0:flows/MUTUAL FUNDS/SIP_Creation_Existing_Folio.yaml#steps[on_select_existing_folio].mock.defaultPayload.message.order.fulfillments[0].tags
flow.sip-creation-new-folio | isa | anchor.sip-setup-flow-family | basis:declared | asof:fis14-2.1.0 | grounded-in:fis14-2.1.0:flows/index.yaml#flows[SIP_Creation_New_Folio].tags
flow.sip-creation-new-folio | isa | anchor.user-initiated-journey | basis:declared | asof:fis14-2.1.0 | grounded-in:fis14-2.1.0:flows/index.yaml#flows[SIP_Creation_New_Folio].tags
flow.sip-creation-new-folio | causes | anchor.folio-creation | basis:declared | asof:fis14-2.1.0 | grounded-in:fis14-2.1.0:flows/index.yaml#flows[SIP_Creation_New_Folio].description
flow.sip-creation-new-folio | requires | anchor.payment-mandate | basis:declared | asof:fis14-2.1.0 | grounded-in:fis14-2.1.0:flows/MUTUAL FUNDS/SIP_Creation_New_Folio.yaml#steps[payment_url_form]
flow.sip-creation-new-folio | causes | anchor.sip-active | basis:declared | asof:fis14-2.1.0 | grounded-in:fis14-2.1.0:flows/MUTUAL FUNDS/SIP_Creation_New_Folio.yaml#steps[on_update_unsolicited_new_folio].mock.defaultPayload.message.order.fulfillments[0].state.descriptor.code
anchor.sip-active | isa | anchor.ongoing-state | basis:declared | asof:fis14-2.1.0 | grounded-in:fis14-2.1.0:flows/MUTUAL FUNDS/SIP_Creation_New_Folio.yaml#steps[on_update_unsolicited_new_folio].mock.defaultPayload.message.order.fulfillments[0].state.descriptor.code
anchor.payment-mandate | requires | anchor.mandate-limit | basis:declared | asof:fis14-2.1.0 | grounded-in:fis14-2.1.0:flows/MUTUAL FUNDS/SIP_Creation_New_Folio.yaml#steps[on_confirm_new_folio].examples[0].payload.message.order.payments[0].tags
anchor.payment-mandate | has-slot | anchor.mandate-identifier | basis:declared | asof:fis14-2.1.0 | grounded-in:fis14-2.1.0:flows/MUTUAL FUNDS/SIP_Creation_New_Folio.yaml#steps[on_confirm_new_folio].examples[0].payload.message.order.payments[0].tags
anchor.payment-mandate | constrains | anchor.payment-mode | basis:declared | asof:fis14-2.1.0 | grounded-in:fis14-2.1.0:flows/MUTUAL FUNDS/SIP_Creation_New_Folio.yaml#steps[on_select_2_new_folio].examples[0].payload.message.order.payments[2].tags
anchor.payment-mode | isa | anchor.enum-anchor | basis:declared | asof:fis14-2.1.0 | grounded-in:fis14-2.1.0:flows/MUTUAL FUNDS/SIP_Creation_New_Folio.yaml#steps[on_select_2_new_folio].examples[0].payload.message.order.payments[2].tags
anchor.mandate-auth | isa | anchor.enum-anchor | basis:declared | asof:fis14-2.1.0 | grounded-in:fis14-2.1.0:flows/MUTUAL FUNDS/SIP_Creation_New_Folio.yaml#steps[on_select_2_new_folio].examples[0].payload.message.order.payments[2].tags
anchor.mandate-auth | scoped-to | anchor.payment-mode | basis:declared | asof:fis14-2.1.0 | grounded-in:fis14-2.1.0:flows/MUTUAL FUNDS/SIP_Creation_New_Folio.yaml#steps[on_select_2_new_folio].examples[0].payload.message.order.payments[2].tags
flow.sip-creation-new-folio-with-kyc | isa | anchor.sip-setup-flow-family | basis:declared | asof:fis14-2.1.0 | grounded-in:fis14-2.1.0:flows/index.yaml#flows[SIP_Creation_New_Folio_With_KYC].tags
flow.sip-creation-new-folio-with-kyc | isa | anchor.user-initiated-journey | basis:declared | asof:fis14-2.1.0 | grounded-in:fis14-2.1.0:flows/index.yaml#flows[SIP_Creation_New_Folio_With_KYC].tags
flow.sip-creation-new-folio-with-kyc | requires | anchor.kyc-fulfillment | basis:declared | asof:fis14-2.1.0 | grounded-in:fis14-2.1.0:flows/MUTUAL FUNDS/SIP_Creation_New_Folio_With_KYC.yaml#steps[kyc_details_form]
flow.sip-creation-new-folio-with-kyc | requires | anchor.esign | basis:declared | asof:fis14-2.1.0 | grounded-in:fis14-2.1.0:flows/MUTUAL FUNDS/SIP_Creation_New_Folio_With_KYC.yaml#steps[E_sign_verification_status]
flow.sip-creation-new-folio-with-kyc | wasDerivedFrom | flow.sip-creation-new-folio | basis:declared | asof:fis14-2.1.0 | grounded-in:fis14-2.1.0:flows/index.yaml#flows[SIP_Creation_New_Folio_With_KYC].description
anchor.esign | precedes | anchor.folio-creation | basis:declared | asof:fis14-2.1.0 | grounded-in:fis14-2.1.0:flows/MUTUAL FUNDS/SIP_Creation_New_Folio_With_KYC.yaml#steps[select_final]
flow.sip-creation-without-payment-mandate | isa | anchor.sip-setup-flow-family | basis:declared | asof:fis14-2.1.0 | grounded-in:fis14-2.1.0:flows/index.yaml#flows[SIP_Creation_Without_Payment_Mandate].tags
flow.sip-creation-without-payment-mandate | isa | anchor.user-initiated-journey | basis:declared | asof:fis14-2.1.0 | grounded-in:fis14-2.1.0:flows/index.yaml#flows[SIP_Creation_Without_Payment_Mandate].tags
flow.sip-creation-without-payment-mandate | not-isa | anchor.reportable-flow | basis:declared | asof:fis14-2.1.0 | grounded-in:fis14-2.1.0:flows/index.yaml#flows[SIP_Creation_Without_Payment_Mandate].tags
flow.sip-creation-without-payment-mandate | not-requires | anchor.payment-mandate | basis:declared | asof:fis14-2.1.0 | grounded-in:fis14-2.1.0:flows/index.yaml#flows[SIP_Creation_Without_Payment_Mandate].description
anchor.skip-payment-mode | disjoint-with | anchor.payment-mandate | basis:declared | asof:fis14-2.1.0 | grounded-in:fis14-2.1.0:flows/MUTUAL FUNDS/SIP_Creation_Without_Payment_Mandate.yaml#steps[on_select_2_new_folio].examples[0].payload.message.order.payments[1].tags
anchor.skip-payment-mode | isa | anchor.payment-mode | basis:declared | asof:fis14-2.1.0 | grounded-in:fis14-2.1.0:flows/MUTUAL FUNDS/SIP_Creation_Without_Payment_Mandate.yaml#steps[on_select_2_new_folio].examples[0].payload.message.order.payments[1].tags
flow.sip-completion | isa | anchor.sip-setup-flow-family | basis:declared | asof:fis14-2.1.0 | grounded-in:fis14-2.1.0:flows/index.yaml#flows[SIP_Completion].tags
flow.sip-completion | isa | anchor.user-initiated-journey | basis:declared | asof:fis14-2.1.0 | grounded-in:fis14-2.1.0:flows/index.yaml#flows[SIP_Completion].tags
flow.sip-completion | causes | anchor.sip-completed | basis:declared | asof:fis14-2.1.0 | grounded-in:fis14-2.1.0:flows/MUTUAL FUNDS/SIP_Completion.yaml#steps[on_update_unsolicited_completion].examples[0].payload.message.order.fulfillments[0].state.descriptor.code
anchor.sip-completed | isa | anchor.fulfillment-state | basis:declared | asof:fis14-2.1.0 | grounded-in:fis14-2.1.0:validations/index.yaml#_TESTS_.on_confirm[ON_CONFIRM_FULFILLMENTS]._RETURN_[VALID_FULFILLMENT_STATE_ENUM].enumList
anchor.sip-completed | requires | anchor.instalment-count | basis:declared | asof:fis14-2.1.0 | grounded-in:fis14-2.1.0:flows/MUTUAL FUNDS/SIP_Completion.yaml#steps[on_update_unsolicited_completion].examples[0].payload.message.order.fulfillments[0].tags
anchor.sip-active | precedes | anchor.sip-completed | basis:declared | asof:fis14-2.1.0 | grounded-in:fis14-2.1.0:flows/MUTUAL FUNDS/SIP_Completion.yaml#steps[on_update_unsolicited_completion]
anchor.parent-order | has-slot | anchor.child-order-id | basis:declared | asof:fis14-2.1.0 | grounded-in:fis14-2.1.0:flows/MUTUAL FUNDS/SIP_Completion.yaml#steps[on_update_unsolicited_completion].examples[0].payload.message.order.fulfillments[0].tags
anchor.sip | isa | anchor.parent-order | basis:declared | asof:fis14-2.1.0 | grounded-in:fis14-2.1.0:flows/MUTUAL FUNDS/SIP_Completion.yaml#steps[on_update_unsolicited_completion].examples[0].payload.message.order.fulfillments[0].tags
flow.sip-auto-cancellation | isa | anchor.sip-setup-flow-family | basis:declared | asof:fis14-2.1.0 | grounded-in:fis14-2.1.0:flows/index.yaml#flows[SIP_Auto_Cancellation].tags
flow.sip-auto-cancellation | isa | anchor.user-initiated-journey | basis:declared | asof:fis14-2.1.0 | grounded-in:fis14-2.1.0:flows/index.yaml#flows[SIP_Auto_Cancellation].tags
flow.sip-auto-cancellation | causes | anchor.sip-cancellation | basis:declared | asof:fis14-2.1.0 | grounded-in:fis14-2.1.0:flows/MUTUAL FUNDS/SIP_Auto_Cancellation.yaml#steps[on_update_unsolicited_auto_cancellation].examples[0].payload.message.order.fulfillments[0].state.descriptor.code
anchor.sip-cancellation | sent-by | anchor.bpp | basis:declared | asof:fis14-2.1.0 | grounded-in:fis14-2.1.0:flows/MUTUAL FUNDS/SIP_Auto_Cancellation.yaml#steps[on_update_unsolicited_auto_cancellation].owner
anchor.sip-cancellation | scoped-to | anchor.provider-initiated | basis:declared | asof:fis14-2.1.0 | grounded-in:fis14-2.1.0:flows/MUTUAL FUNDS/SIP_Auto_Cancellation.yaml#steps[on_update_unsolicited_auto_cancellation].examples[0].payload.message.order.fulfillments[0].tags
anchor.provider-initiated | causes | anchor.instalment-failure-threshold | basis:declared | asof:fis14-2.1.0 | grounded-in:fis14-2.1.0:flows/MUTUAL FUNDS/SIP_Auto_Cancellation.yaml#steps[on_update_unsolicited_auto_cancellation].examples[0].payload.message.order.fulfillments[0].tags
anchor.sip-cancellation | causes | anchor.order-cancelled | basis:declared | asof:fis14-2.1.0 | grounded-in:fis14-2.1.0:flows/MUTUAL FUNDS/SIP_Auto_Cancellation.yaml#steps[on_update_unsolicited_auto_cancellation].examples[0].payload.message.order.status
anchor.sip-cancellation | has-slot | anchor.cancellation-info | basis:declared | asof:fis14-2.1.0 | grounded-in:fis14-2.1.0:flows/MUTUAL FUNDS/SIP_Auto_Cancellation.yaml#steps[on_update_unsolicited_auto_cancellation].examples[0].payload.message.order.fulfillments[0].tags
flow.sip-auto-cancellation | not-requires | anchor.update | basis:declared | asof:fis14-2.1.0 | grounded-in:fis14-2.1.0:flows/MUTUAL FUNDS/SIP_Auto_Cancellation.yaml#steps
flow.sip-cancellation-by-the-investor | isa | anchor.sip-setup-flow-family | basis:declared | asof:fis14-2.1.0 | grounded-in:fis14-2.1.0:flows/index.yaml#flows[SIP_Cancellation_By_The_Investor].tags
flow.sip-cancellation-by-the-investor | isa | anchor.user-initiated-journey | basis:declared | asof:fis14-2.1.0 | grounded-in:fis14-2.1.0:flows/index.yaml#flows[SIP_Cancellation_By_The_Investor].tags
flow.sip-cancellation-by-the-investor | requires | anchor.update | basis:declared | asof:fis14-2.1.0 | grounded-in:fis14-2.1.0:flows/MUTUAL FUNDS/SIP_Cancellation_By_The_Investor.yaml#steps[update_cancellation]
anchor.update | causes | anchor.sip-cancellation | basis:declared | asof:fis14-2.1.0 | grounded-in:fis14-2.1.0:flows/MUTUAL FUNDS/SIP_Cancellation_By_The_Investor.yaml#steps[update_cancellation].examples[0].payload.message.update_target
anchor.sip-cancellation | scoped-to | anchor.consumer-initiated | basis:declared | asof:fis14-2.1.0 | grounded-in:fis14-2.1.0:flows/MUTUAL FUNDS/SIP_Cancellation_By_The_Investor.yaml#steps[update_cancellation].examples[0].payload.message.order.fulfillments[0].tags
anchor.consumer-initiated | requires | anchor.cancellation-reason | basis:declared | asof:fis14-2.1.0 | grounded-in:fis14-2.1.0:flows/MUTUAL FUNDS/SIP_Cancellation_By_The_Investor.yaml#steps[update_cancellation].examples[0].payload.message.order.fulfillments[0].tags
anchor.consumer-initiated | disjoint-with | anchor.provider-initiated | basis:declared | asof:fis14-2.1.0 | grounded-in:fis14-2.1.0:flows/MUTUAL FUNDS/SIP_Cancellation_By_The_Investor.yaml#steps[update_cancellation].examples[0].payload.message.order.fulfillments[0].tags
flow.sip-instalment | isa | anchor.sip-lifecycle-flow-family | basis:declared | asof:fis14-2.1.0 | grounded-in:fis14-2.1.0:flows/index.yaml#flows[SIP_Instalment].tags
flow.sip-instalment | isa | anchor.unsolicited-journey | basis:declared | asof:fis14-2.1.0 | grounded-in:fis14-2.1.0:flows/index.yaml#flows[SIP_Instalment].tags
flow.sip-instalment | causes | anchor.sip-active | basis:declared | asof:fis14-2.1.0 | grounded-in:fis14-2.1.0:flows/MUTUAL FUNDS/SIP_Instalment.yaml#steps[on_update_unsolicited_new_folio].mock.defaultPayload.message.order.fulfillments[0].state.descriptor.code
anchor.sip-instalment | isa | anchor.child-order | basis:declared | asof:fis14-2.1.0 | grounded-in:fis14-2.1.0:flows/MUTUAL FUNDS/SIP_Manual_Trigger_Instalment.yaml#steps[init].mock.defaultPayload.message.order.ref_order_ids
anchor.child-order | requires | anchor.parent-order | basis:declared | asof:fis14-2.1.0 | grounded-in:fis14-2.1.0:flows/MUTUAL FUNDS/SIP_Manual_Trigger_Instalment.yaml#steps[init].mock.defaultPayload.message.order.ref_order_ids
anchor.sip-instalment | precedes | anchor.unit-allocation | basis:declared | asof:fis14-2.1.0 | grounded-in:fis14-2.1.0:flows/MUTUAL FUNDS/SIP_Instalment_Failure.yaml#steps[on_status_unsolicited_new_folio_payment]
flow.sip-instalment-failure | isa | anchor.sip-lifecycle-flow-family | basis:declared | asof:fis14-2.1.0 | grounded-in:fis14-2.1.0:flows/index.yaml#flows[SIP_Instalment_Failure].tags
flow.sip-instalment-failure | isa | anchor.unsolicited-journey | basis:declared | asof:fis14-2.1.0 | grounded-in:fis14-2.1.0:flows/index.yaml#flows[SIP_Instalment_Failure].tags
flow.sip-instalment-failure | not-isa | anchor.reportable-flow | basis:declared | asof:fis14-2.1.0 | grounded-in:fis14-2.1.0:flows/index.yaml#flows[SIP_Instalment_Failure].tags
flow.sip-instalment-failure | causes | anchor.failed-state | basis:declared | asof:fis14-2.1.0 | grounded-in:fis14-2.1.0:flows/MUTUAL FUNDS/SIP_Instalment_Failure.yaml#steps[on_update_unsolicited_new_folio].mock.defaultPayload.message.order.fulfillments[0].state.descriptor.code
anchor.failed-state | requires | anchor.error-information | basis:declared | asof:fis14-2.1.0 | grounded-in:fis14-2.1.0:flows/MUTUAL FUNDS/SIP_Instalment_Failure.yaml#steps[on_update_unsolicited_new_folio].mock.defaultPayload.message.order.fulfillments[0].tags
anchor.error-information | has-slot | anchor.failure-reason | basis:declared | asof:fis14-2.1.0 | grounded-in:fis14-2.1.0:flows/MUTUAL FUNDS/SIP_Instalment_Failure.yaml#steps[on_update_unsolicited_new_folio].mock.defaultPayload.message.order.fulfillments[0].tags
anchor.failed-state | causes | anchor.order-cancelled | basis:declared | asof:fis14-2.1.0 | grounded-in:fis14-2.1.0:flows/MUTUAL FUNDS/SIP_Instalment_Failure.yaml#steps[on_update_unsolicited_new_folio].mock.defaultPayload.message.order.status
anchor.failure-reason | not-isa | anchor.fis14-error-set | basis:declared | asof:fis14-2.1.0 | grounded-in:fis14-2.1.0:errors/index.yaml#code
flow.sip-manual-trigger-instalment | isa | anchor.sip-setup-flow-family | basis:declared | asof:fis14-2.1.0 | grounded-in:fis14-2.1.0:flows/index.yaml#flows[SIP_Manual_Trigger_Instalment].tags
flow.sip-manual-trigger-instalment | isa | anchor.user-initiated-journey | basis:declared | asof:fis14-2.1.0 | grounded-in:fis14-2.1.0:flows/index.yaml#flows[SIP_Manual_Trigger_Instalment].tags
flow.sip-manual-trigger-instalment | not-isa | anchor.reportable-flow | basis:declared | asof:fis14-2.1.0 | grounded-in:fis14-2.1.0:flows/index.yaml#flows[SIP_Manual_Trigger_Instalment].tags
flow.sip-manual-trigger-instalment | causes | anchor.sip-instalment | basis:declared | asof:fis14-2.1.0 | grounded-in:fis14-2.1.0:flows/MUTUAL FUNDS/SIP_Manual_Trigger_Instalment.yaml#steps[init].mock.defaultPayload.message.order.fulfillments[0].type
flow.sip-manual-trigger-instalment | not-causes | anchor.unit-allocation | basis:declared | asof:fis14-2.1.0 | grounded-in:fis14-2.1.0:flows/MUTUAL FUNDS/SIP_Manual_Trigger_Instalment.yaml#steps
anchor.sip-instalment | scoped-to | anchor.init | basis:declared | asof:fis14-2.1.0 | grounded-in:fis14-2.1.0:flows/MUTUAL FUNDS/SIP_Manual_Trigger_Instalment.yaml#steps[init].mock.defaultPayload.message.order.fulfillments[0].type
anchor.rta-source-ref | isa | anchor.external-refs | basis:declared | asof:fis14-2.1.0 | grounded-in:fis14-2.1.0:flows/MUTUAL FUNDS/SIP_Manual_Trigger_Instalment.yaml#steps[on_confirm_new_folio].mock.defaultPayload.message.order.fulfillments[0].tags
anchor.external-refs | isa | anchor.tag-group-anchor | basis:declared | asof:fis14-2.1.0 | grounded-in:fis14-2.1.0:flows/MUTUAL FUNDS/SIP_Manual_Trigger_Instalment.yaml#steps[on_confirm_new_folio].mock.defaultPayload.message.order.fulfillments[0].tags
anchor.rta-source-ref | sent-by | anchor.bpp | basis:declared | asof:fis14-2.1.0 | grounded-in:fis14-2.1.0:flows/MUTUAL FUNDS/SIP_Manual_Trigger_Instalment.yaml#steps[on_confirm_new_folio].owner
anchor.order | isa | anchor.beckn-object | basis:declared | asof:fis14-2.1.0 | grounded-in:fis14-2.1.0:specs/openapi.yaml#components.schemas.Order
anchor.order | has-slot | anchor.ref-order-ids | basis:declared | asof:fis14-2.1.0 | grounded-in:fis14-2.1.0:specs/openapi.yaml#components.schemas.Order.properties.ref_order_ids
anchor.child-order | scoped-to | anchor.ref-order-ids | basis:declared | asof:fis14-2.1.0 | grounded-in:fis14-2.1.0:specs/openapi.yaml#components.schemas.Order.properties.ref_order_ids
anchor.order | has-slot | anchor.cancellation-terms | basis:declared | asof:fis14-2.1.0 | grounded-in:fis14-2.1.0:specs/openapi.yaml#components.schemas.Order.properties.cancellation_terms
anchor.xinput | isa | anchor.beckn-object | basis:declared | asof:fis14-2.1.0 | grounded-in:fis14-2.1.0:specs/openapi.yaml#components.schemas.XInput
anchor.form | part-of | anchor.xinput | basis:declared | asof:fis14-2.1.0 | grounded-in:fis14-2.1.0:specs/openapi.yaml#components.schemas.XInput.properties.form
anchor.form | isa | anchor.beckn-object | basis:declared | asof:fis14-2.1.0 | grounded-in:fis14-2.1.0:specs/openapi.yaml#components.schemas.Form
anchor.form | has-slot | anchor.form-mime-type | basis:declared | asof:fis14-2.1.0 | grounded-in:fis14-2.1.0:specs/openapi.yaml#components.schemas.Form.properties.mime_type
anchor.fulfillment-state | part-of | anchor.fulfillment | basis:declared | asof:fis14-2.1.0 | grounded-in:fis14-2.1.0:specs/openapi.yaml#components.schemas.Fulfillment.properties.state
anchor.fulfillment | has-slot | anchor.sip-schedule | basis:declared | asof:fis14-2.1.0 | grounded-in:fis14-2.1.0:specs/openapi.yaml#components.schemas.Fulfillment.properties.stops
anchor.sip-schedule | isa | anchor.beckn-object | basis:declared | asof:fis14-2.1.0 | grounded-in:fis14-2.1.0:specs/openapi.yaml#components.schemas.Schedule
anchor.sip-frequency | part-of | anchor.sip-schedule | basis:declared | asof:fis14-2.1.0 | grounded-in:fis14-2.1.0:specs/openapi.yaml#components.schemas.Schedule.properties.frequency
anchor.item-quantity | isa | anchor.beckn-object | basis:declared | asof:fis14-2.1.0 | grounded-in:fis14-2.1.0:specs/openapi.yaml#components.schemas.ItemQuantity
anchor.item-quantity | has-slot | anchor.unit-allocation | basis:declared | asof:fis14-2.1.0 | grounded-in:fis14-2.1.0:specs/openapi.yaml#components.schemas.ItemQuantity.properties.allocated
anchor.item-quantity | part-of | anchor.item | basis:declared | asof:fis14-2.1.0 | grounded-in:fis14-2.1.0:specs/openapi.yaml#components.schemas.Item.properties.quantity
anchor.quote | isa | anchor.beckn-object | basis:declared | asof:fis14-2.1.0 | grounded-in:fis14-2.1.0:specs/openapi.yaml#components.schemas.Quotation
anchor.customer | isa | anchor.beckn-object | basis:declared | asof:fis14-2.1.0 | grounded-in:fis14-2.1.0:specs/openapi.yaml#components.schemas.Customer
anchor.agent | isa | anchor.beckn-object | basis:declared | asof:fis14-2.1.0 | grounded-in:fis14-2.1.0:specs/openapi.yaml#components.schemas.Agent
anchor.customer-credential | isa | anchor.beckn-object | basis:declared | asof:fis14-2.1.0 | grounded-in:fis14-2.1.0:specs/openapi.yaml#components.schemas.Credential
anchor.tag-group-anchor | isa | anchor.beckn-object | basis:declared | asof:fis14-2.1.0 | grounded-in:fis14-2.1.0:specs/openapi.yaml#components.schemas.TagGroup
anchor.cancellation-terms | isa | anchor.beckn-object | basis:declared | asof:fis14-2.1.0 | grounded-in:fis14-2.1.0:specs/openapi.yaml#components.schemas.CancellationTerm
anchor.payment-status | part-of | anchor.payment | basis:declared | asof:fis14-2.1.0 | grounded-in:fis14-2.1.0:specs/openapi.yaml#components.schemas.Payment.properties.status
anchor.source-bank-account | part-of | anchor.payment | basis:declared | asof:fis14-2.1.0 | grounded-in:fis14-2.1.0:specs/openapi.yaml#components.schemas.Payment.properties.params
anchor.payment-collector | part-of | anchor.payment | basis:declared | asof:fis14-2.1.0 | grounded-in:fis14-2.1.0:specs/openapi.yaml#components.schemas.Payment.properties.collected_by
anchor.schema-validation | isa | anchor.validation-layer | basis:declared | asof:fis14-2.1.0 | grounded-in:fis14-2.1.0:specs/openapi.yaml#components.schemas
anchor.schema-validation | precedes | anchor.l1-payload-validation | basis:authority | asof:fis14-2.1.0 | grounded-in:workbench:frames/validation-layers.md
anchor.fis14-action-set | constrains | anchor.api-path | basis:declared | asof:fis14-2.1.0 | grounded-in:fis14-2.1.0:specs/openapi.yaml#paths
anchor.api-path | isa | anchor.runtime-endpoint | basis:declared | asof:fis14-2.1.0 | grounded-in:fis14-2.1.0:specs/openapi.yaml#paths./search
anchor.api-path | wasGeneratedBy | anchor.onix-api-service | basis:observed-live | asof:fis14-2.1.0 | grounded-in:workbench:scripts/onix-request-lifecycle.md
anchor.l1-payload-validation | wasGeneratedBy | anchor.validation-compiler | basis:sandbox-tested | asof:fis14-2.1.0 | grounded-in:workbench:frames/validation-compiler.md
anchor.l1-payload-validation | causes | anchor.nack-payload | basis:sandbox-tested | asof:fis14-2.1.0 | grounded-in:workbench:frames/validation-layers.md
anchor.continue-guard | isa | anchor.runtime-skip-guard | basis:sandbox-tested | asof:fis14-2.1.0 | grounded-in:workbench:frames/validation-layers.md
anchor.continue-guard | scoped-to | anchor.xinput | basis:declared | asof:fis14-2.1.0 | grounded-in:fis14-2.1.0:validations/index.yaml#_TESTS_.on_select[ON_SELECT_XINPUT]._CONTINUE_
anchor.continue-guard | scoped-to | anchor.payment | basis:declared | asof:fis14-2.1.0 | grounded-in:fis14-2.1.0:validations/index.yaml#_TESTS_.init[INIT_PAYMENTS]._CONTINUE_
anchor.continue-guard | scoped-to | anchor.quote | basis:declared | asof:fis14-2.1.0 | grounded-in:fis14-2.1.0:validations/index.yaml#_TESTS_.on_init[ON_INIT_QUOTE]._CONTINUE_
anchor.continue-guard | scoped-to | anchor.cancellation-terms | basis:declared | asof:fis14-2.1.0 | grounded-in:fis14-2.1.0:validations/index.yaml#_TESTS_.on_init[ON_INIT_CANCELLATION_TERMS]._CONTINUE_
anchor.continue-guard | scoped-to | anchor.document-set | basis:declared | asof:fis14-2.1.0 | grounded-in:fis14-2.1.0:validations/index.yaml#_TESTS_.on_confirm[ON_CONFIRM_DOCUMENTS]._CONTINUE_
anchor.session-fullness | isa | anchor.runtime-concept | basis:observed-live | asof:fis14-2.1.0 | grounded-in:workbench:frames/mock-runner-lib.md
anchor.session-fullness | used | anchor.folio | basis:declared | asof:fis14-2.1.0 | grounded-in:fis14-2.1.0:flows/MUTUAL FUNDS/SIP_Creation_New_Folio.yaml#steps[init].mock.saveData.folio_number
anchor.session-fullness | used | anchor.form-submission-id | basis:declared | asof:fis14-2.1.0 | grounded-in:fis14-2.1.0:flows/MUTUAL FUNDS/SIP_Creation_New_Folio.yaml#steps[select].mock.saveData.submission_id
anchor.session-fullness | used | anchor.quote | basis:declared | asof:fis14-2.1.0 | grounded-in:fis14-2.1.0:flows/MUTUAL FUNDS/SIP_Creation_New_Folio.yaml#steps[on_select_1_new_folio].mock.saveData.quote
anchor.on-confirm | causes | anchor.payment-url-form | basis:declared | asof:fis14-2.1.0 | grounded-in:fis14-2.1.0:flows/MUTUAL FUNDS/SIP_Creation_New_Folio.yaml#steps[on_confirm_new_folio].mock.saveData.payment_url_form
anchor.unsolicited-callback | isa | anchor.runtime-concept | basis:observed-live | asof:fis14-2.1.0 | grounded-in:workbench:frames/flow-state-machine.md
anchor.on-status | isa | anchor.unsolicited-callback | basis:declared | asof:fis14-2.1.0 | grounded-in:fis14-2.1.0:flows/MUTUAL FUNDS/SIP_Creation_New_Folio.yaml#steps[on_status_unsolicited_new_folio_payment].unsolicited
anchor.on-update | isa | anchor.unsolicited-callback | basis:declared | asof:fis14-2.1.0 | grounded-in:fis14-2.1.0:flows/MUTUAL FUNDS/SIP_Creation_New_Folio.yaml#steps[on_update_unsolicited_new_folio].unsolicited
anchor.unsolicited-callback | sent-by | anchor.bpp | basis:declared | asof:fis14-2.1.0 | grounded-in:fis14-2.1.0:flows/MUTUAL FUNDS/SIP_Creation_New_Folio.yaml#steps[on_update_unsolicited_new_folio].owner
anchor.sip-lifecycle-flow-family | requires | anchor.unsolicited-callback | basis:declared | asof:fis14-2.1.0 | grounded-in:fis14-2.1.0:flows/index.yaml#flows[SIP_Instalment].tags
anchor.search | sent-by | anchor.bap | basis:declared | asof:fis14-2.1.0 | grounded-in:fis14-2.1.0:flows/MUTUAL FUNDS/Main_Search.yaml#steps[search].owner
anchor.on-search | sent-by | anchor.bpp | basis:declared | asof:fis14-2.1.0 | grounded-in:fis14-2.1.0:flows/MUTUAL FUNDS/Main_Search.yaml#steps[on_search].owner
anchor.select | sent-by | anchor.bap | basis:declared | asof:fis14-2.1.0 | grounded-in:fis14-2.1.0:flows/MUTUAL FUNDS/SIP_Creation_New_Folio.yaml#steps[select].owner
anchor.on-select | sent-by | anchor.bpp | basis:declared | asof:fis14-2.1.0 | grounded-in:fis14-2.1.0:flows/MUTUAL FUNDS/SIP_Creation_New_Folio.yaml#steps[on_select_1_new_folio].owner
anchor.init | sent-by | anchor.bap | basis:declared | asof:fis14-2.1.0 | grounded-in:fis14-2.1.0:flows/MUTUAL FUNDS/SIP_Creation_New_Folio.yaml#steps[init].owner
anchor.on-init | sent-by | anchor.bpp | basis:declared | asof:fis14-2.1.0 | grounded-in:fis14-2.1.0:flows/MUTUAL FUNDS/SIP_Creation_New_Folio.yaml#steps[on_init_new_folio].owner
anchor.confirm | sent-by | anchor.bap | basis:declared | asof:fis14-2.1.0 | grounded-in:fis14-2.1.0:flows/MUTUAL FUNDS/SIP_Creation_New_Folio.yaml#steps[confirm].owner
anchor.on-confirm | sent-by | anchor.bpp | basis:declared | asof:fis14-2.1.0 | grounded-in:fis14-2.1.0:flows/MUTUAL FUNDS/SIP_Creation_New_Folio.yaml#steps[on_confirm_new_folio].owner
anchor.update | sent-by | anchor.bap | basis:declared | asof:fis14-2.1.0 | grounded-in:fis14-2.1.0:flows/MUTUAL FUNDS/SIP_Cancellation_By_The_Investor.yaml#steps[update_cancellation].owner
anchor.catalog | sent-by | anchor.bpp | basis:declared | asof:fis14-2.1.0 | grounded-in:fis14-2.1.0:attributes/MUTUAL_FUNDS.yaml#attribute_set.on_search.message.catalog._description.owner
anchor.provider | sent-by | anchor.bpp | basis:declared | asof:fis14-2.1.0 | grounded-in:fis14-2.1.0:attributes/MUTUAL_FUNDS.yaml#attribute_set.on_search.message.catalog.providers._description.owner
anchor.item | sent-by | anchor.bpp | basis:declared | asof:fis14-2.1.0 | grounded-in:fis14-2.1.0:attributes/MUTUAL_FUNDS.yaml#attribute_set.on_search.message.catalog.providers.items.id._description.owner
anchor.item-quantity | sent-by | anchor.bap | basis:declared | asof:fis14-2.1.0 | grounded-in:fis14-2.1.0:attributes/MUTUAL_FUNDS.yaml#attribute_set.select.message.order.items.quantity._description.owner
anchor.payment | sent-by | anchor.bpp | basis:declared | asof:fis14-2.1.0 | grounded-in:fis14-2.1.0:attributes/MUTUAL_FUNDS.yaml#attribute_set.on_init.message.order.payments._description.owner
anchor.source-bank-account | sent-by | anchor.bap | basis:declared | asof:fis14-2.1.0 | grounded-in:fis14-2.1.0:attributes/MUTUAL_FUNDS.yaml#attribute_set.init.message.order.payments.params.source_bank_code._description.owner
anchor.order-status | sent-by | anchor.bap | basis:declared | asof:fis14-2.1.0 | grounded-in:fis14-2.1.0:attributes/MUTUAL_FUNDS.yaml#attribute_set.on_confirm.message.order.status._description.owner
anchor.update-target | scoped-to | anchor.update | basis:declared | asof:fis14-2.1.0 | grounded-in:fis14-2.1.0:attributes/MUTUAL_FUNDS.yaml#attribute_set.update.message.update_target._description.usage
anchor.update-target | sent-by | anchor.bap | basis:declared | asof:fis14-2.1.0 | grounded-in:fis14-2.1.0:attributes/MUTUAL_FUNDS.yaml#attribute_set.update.message.update_target._description.owner
anchor.update | not-requires | anchor.item | basis:declared | asof:fis14-2.1.0 | grounded-in:fis14-2.1.0:attributes/MUTUAL_FUNDS.yaml#attribute_set.update.message.order
anchor.status | requires | anchor.order-id | basis:declared | asof:fis14-2.1.0 | grounded-in:fis14-2.1.0:attributes/MUTUAL_FUNDS.yaml#attribute_set.status.message.order_id._description.required

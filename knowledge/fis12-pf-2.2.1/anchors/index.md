# Anchors — interned meanings

> Rebuilt from `atoms.md` for `fis12-pf-2.2.1` (structural + Stage E). One row per interned
> meaning; `grounded-in` is the position the meaning was first interned at.

| handle | meaning | grounded-in | asof |
|---|---|---|---|
| anchor.aa-consent-journey | aa consent journey | fis12-pf-2.2.1:flows/index.yaml#flows[Purchase_Finance_With_AA].tags | fis12-pf-2.2.1 |
| anchor.aa-consent-round | aa consent round | fis12-pf-2.2.1:flows/PURCHASE FINANCE/Purchase_Finance_With_AA.yaml#steps[on_search6_purchase_finance].responseFor | fis12-pf-2.2.1 |
| anchor.aa-id | aa id | fis12-pf-2.2.1:attributes/PURCHASE_FINANCE.yaml#attribute_set.html_form.aa_id._description.info | fis12-pf-2.2.1 |
| anchor.aa-offer-round | aa offer round | fis12-pf-2.2.1:flows/PURCHASE FINANCE/Purchase_Finance_With_AA.yaml#steps[on_search6_purchase_finance].action_id | fis12-pf-2.2.1 |
| anchor.account-aggregator | account aggregator | - | fis12-pf-2.2.1 |
| anchor.ack-nack | ack nack | fis12-pf-2.2.1:specs/openapi.yaml#paths./search.post.responses.200.content.application/json.schema.properties.message.properties.ack.properties.status | fis12-pf-2.2.1 |
| anchor.action | action | - | fis12-pf-2.2.1 |
| anchor.bap | bap | - | fis12-pf-2.2.1 |
| anchor.bap-terms-tag | bap terms tag | fis12-pf-2.2.1:validations/index.yaml#_TESTS_.search[SEARCH_PAYMENT]._RETURN_[REQUIRED_PAYMENT_TAGS_GROUPS]._RETURN_[REQUIRED_BAP_TERMS_TAG].tagPath | fis12-pf-2.2.1 |
| anchor.base-order-delivered | base order delivered | fis12-pf-2.2.1:flows/PURCHASE FINANCE/Purchase_Finance_Without_AA.yaml#steps[on_update1_unsolicited_purchase_finance].mock.defaultPayload.message.order.fulfillments[0].state.descriptor.code | fis12-pf-2.2.1 |
| anchor.base-order-fulfillment | base order fulfillment | fis12-pf-2.2.1:validations/index.yaml#_TESTS_.on_init[ON_INIT_FULFILLMENTS]._RETURN_[REQUIRED_FULFILLMENT_TYPE].enumList | fis12-pf-2.2.1 |
| anchor.beckn-base | beckn base | - | fis12-pf-2.2.1 |
| anchor.beckn-context | beckn context | - | fis12-pf-2.2.1 |
| anchor.borrower | borrower | fis12-pf-2.2.1:docs/overview.md#real-world-actors | fis12-pf-2.2.1 |
| anchor.borrower-contact | borrower contact | - | fis12-pf-2.2.1 |
| anchor.borrower-income | borrower income | fis12-pf-2.2.1:attributes/PURCHASE_FINANCE.yaml#attribute_set.html_form.income._description.info | fis12-pf-2.2.1 |
| anchor.borrower-pan | borrower pan | fis12-pf-2.2.1:attributes/PURCHASE_FINANCE.yaml#attribute_set.html_form.pan._description.info | fis12-pf-2.2.1 |
| anchor.bpp | bpp | - | fis12-pf-2.2.1 |
| anchor.bpp-id | bpp id | - | fis12-pf-2.2.1 |
| anchor.bpp-terms-tag | bpp terms tag | fis12-pf-2.2.1:validations/index.yaml#_TESTS_.on_search[ON_SEARCH_PAYMENT]._RETURN_[REQUIRED_BPP_TERMS_TAG].tagPath | fis12-pf-2.2.1 |
| anchor.breakup-tag | breakup tag | fis12-pf-2.2.1:validations/index.yaml#_TESTS_.on_confirm[ON_CONFIRM_PAYMENTS_POST_FULFILLMENT]._RETURN_[REQUIRED_POST_FULFILLMENT_BREAKUP_LIST].validValues | fis12-pf-2.2.1 |
| anchor.broadcast-discovery | broadcast discovery | - | fis12-pf-2.2.1 |
| anchor.bureau-consent | bureau consent | fis12-pf-2.2.1:attributes/PURCHASE_FINANCE.yaml#attribute_set.html_form.bureauConsent._description.info | fis12-pf-2.2.1 |
| anchor.buyer-finder-fee | buyer finder fee | fis12-pf-2.2.1:validations/index.yaml#_TESTS_.on_search[ON_SEARCH_PAYMENT]._RETURN_[VALID_BUYER_FINDER_FEES_TYPE_VALUE].enumList | fis12-pf-2.2.1 |
| anchor.cancel | cancel | fis12-pf-2.2.1:actions/index.yaml#supportedActions.cancel | fis12-pf-2.2.1 |
| anchor.cancellation-fee | cancellation fee | - | fis12-pf-2.2.1 |
| anchor.cancellation-not-possible | cancellation not possible | fis12-pf-2.2.1:errors/index.yaml#code[50001].Description | fis12-pf-2.2.1 |
| anchor.cancellation-reason-id | cancellation reason id | - | fis12-pf-2.2.1 |
| anchor.cancellation-tail | cancellation tail | fis12-pf-2.2.1:flows/PURCHASE FINANCE/Purchase_Finance_With_AA_Cancellation.yaml#steps[soft_cancel_purchase_finance].mock.defaultPayload.message.descriptor.code | fis12-pf-2.2.1 |
| anchor.cancellation-term-states | cancellation term states | fis12-pf-2.2.1:validations/index.yaml#_TESTS_.on_init[ON_INIT_CANCELLATION_TERMS]._RETURN_[VALID_CANCELLATION_TERMS_FULFILLMENT_STATE_CODE].enumList | fis12-pf-2.2.1 |
| anchor.cancellation-terms | cancellation terms | fis12-pf-2.2.1:validations/index.yaml#_TESTS_.on_confirm[ON_CONFIRM_CANCELLATION_TERMS]._RETURN_[VALID_CANCELLATION_TERMS_FULFILLMENT_STATE_CODE].attr | fis12-pf-2.2.1 |
| anchor.catalog-item | catalog item | - | fis12-pf-2.2.1 |
| anchor.category-agri-purchase-finance | category agri purchase finance | fis12-pf-2.2.1:validations/index.yaml#_TESTS_.on_search[ON_SEARCH_CATEGORIES]._RETURN_[VALID_ENUM_CATEGORIES_CODE].enumList | fis12-pf-2.2.1 |
| anchor.category-electronics-purchase-finance | category electronics purchase finance | fis12-pf-2.2.1:validations/index.yaml#_TESTS_.on_search[ON_SEARCH_CATEGORIES]._RETURN_[VALID_ENUM_CATEGORIES_CODE].enumList | fis12-pf-2.2.1 |
| anchor.category-purchase-finance | category purchase finance | fis12-pf-2.2.1:validations/index.yaml#_TESTS_.search[SEARCH_CATEGORY_CODE]._RETURN_[VALID_ENUM_CATEGORY_CODE].enumList | fis12-pf-2.2.1 |
| anchor.checklist-emandate | checklist emandate | fis12-pf-2.2.1:validations/index.yaml#_TESTS_.on_select[ON_SELECT_ITEMS_CHECKLISTS_TAG]._RETURN_[REQUIRED_CHECKLISTS_LIST].validValues | fis12-pf-2.2.1 |
| anchor.checklist-esign | checklist esign | fis12-pf-2.2.1:validations/index.yaml#_TESTS_.on_select[ON_SELECT_ITEMS_CHECKLISTS_TAG]._RETURN_[REQUIRED_CHECKLISTS_LIST].validValues | fis12-pf-2.2.1 |
| anchor.checklist-kyc | checklist kyc | fis12-pf-2.2.1:validations/index.yaml#_TESTS_.on_select[ON_SELECT_ITEMS_CHECKLISTS_TAG]._RETURN_[REQUIRED_CHECKLISTS_LIST].validValues | fis12-pf-2.2.1 |
| anchor.checklist-kyc-enach-esign | checklist kyc enach esign | fis12-pf-2.2.1:validations/index.yaml#_TESTS_.on_select[ON_SELECT_ITEMS_CHECKLISTS_TAG]._RETURN_[REQUIRED_CHECKLISTS_LIST].validValues | fis12-pf-2.2.1 |
| anchor.checklist-set-down-payment | checklist set down payment | fis12-pf-2.2.1:validations/index.yaml#_TESTS_.on_select[ON_SELECT_ITEMS_CHECKLISTS_TAG]._RETURN_[REQUIRED_CHECKLISTS_LIST].validValues | fis12-pf-2.2.1 |
| anchor.checklist-state | checklist state | fis12-pf-2.2.1:validations/index.yaml#_TESTS_.on_select[ON_SELECT_ITEMS_CHECKLISTS_TAG]._RETURN_[VALID_CHECKLIST_STATUS_VALUES].enumList | fis12-pf-2.2.1 |
| anchor.checklists-tag | checklists tag | fis12-pf-2.2.1:validations/index.yaml#_TESTS_.on_select[ON_SELECT_ITEMS_CHECKLISTS_TAG]._RETURN_[REQUIRED_CHECKLISTS_TAG_GROUP].tagPath | fis12-pf-2.2.1 |
| anchor.collected-by-enum | collected by enum | fis12-pf-2.2.1:validations/index.yaml#_TESTS_.search[SEARCH_PAYMENT]._RETURN_[VALID_PAYMENT_COLLECTED_BY_ENUM].enumList | fis12-pf-2.2.1 |
| anchor.complainant-action | complainant action | fis12-pf-2.2.1:validations/index.yaml#_TESTS_.issue[ISSUE_VALIDATION_VERSION_100]._RETURN_[ISSUE_VALIDATION_OPEN]._RETURN_[REQUIRED_ISSUE_ACTIONS_OPEN].validValues | fis12-pf-2.2.1 |
| anchor.confirm | confirm | fis12-pf-2.2.1:actions/index.yaml#supportedActions.confirm | fis12-pf-2.2.1 |
| anchor.confirm-cancel | confirm cancel | fis12-pf-2.2.1:flows/PURCHASE FINANCE/Purchase_Finance_Without_AA_Cancellation.yaml#steps[confirmed_cancel_purchase_finance].mock.defaultPayload.message.descriptor.code | fis12-pf-2.2.1 |
| anchor.consent-handler | consent handler | fis12-pf-2.2.1:flows/PURCHASE FINANCE/Purchase_Finance_With_AA.yaml#steps[on_search5_purchase_finance].mock.defaultPayload.message.catalog.providers[0].items[0].tags[0].list[0].descriptor.code | fis12-pf-2.2.1 |
| anchor.consent-info-tag | consent info tag | fis12-pf-2.2.1:flows/PURCHASE FINANCE/Purchase_Finance_With_AA.yaml#steps[on_search5_purchase_finance].mock.defaultPayload.message.catalog.providers[0].items[0].tags[0].descriptor.code | fis12-pf-2.2.1 |
| anchor.consumer-lending | consumer lending | - | fis12-pf-2.2.1 |
| anchor.contact-info-codes | contact info codes | fis12-pf-2.2.1:validations/index.yaml#_TESTS_.on_search[ON_SEARCH_PROVIDER_CONTACT_INFO]._RETURN_[REQUIRED_CONTACT_INFO_LIST].validValues | fis12-pf-2.2.1 |
| anchor.contact-info-tag | contact info tag | fis12-pf-2.2.1:validations/index.yaml#_TESTS_.on_search[ON_SEARCH_PROVIDER_CONTACT_INFO]._RETURN_[REQUIRED_CONTACT_INFO_TAG_GROUP].tagPath | fis12-pf-2.2.1 |
| anchor.context-required-block | context required block | fis12-pf-2.2.1:validations/index.yaml#_TESTS_.search[SEARCH_CONTEXT]._RETURN_ | fis12-pf-2.2.1 |
| anchor.credit-bureau-consent | credit bureau consent | - | fis12-pf-2.2.1 |
| anchor.currency-inr | currency inr | fis12-pf-2.2.1:validations/index.yaml#_TESTS_.on_select[ON_SELECT_ITEMS_BASIC]._RETURN_[REQUIRED_ITEM_PRICE_CURRENCY].enumList | fis12-pf-2.2.1 |
| anchor.delay-penalty-fee | delay penalty fee | fis12-pf-2.2.1:flows/PURCHASE FINANCE/Purchase_Finance_Without_AA.yaml#steps[on_search3_purchase_finance].mock.defaultPayload.message.catalog.providers[0].items[1].tags[0].list[6].descriptor.code | fis12-pf-2.2.1 |
| anchor.directed-search | directed search | - | fis12-pf-2.2.1 |
| anchor.document-code-enum | document code enum | fis12-pf-2.2.1:validations/index.yaml#_TESTS_.on_confirm[ON_CONFIRM_DOCUMENTS]._RETURN_[VALID_DOCUMENT_DESCRIPTOR_CODE_ENUM].enumList | fis12-pf-2.2.1 |
| anchor.domain-ondc-fis12 | domain ondc fis12 | - | fis12-pf-2.2.1 |
| anchor.down-payment | down payment | fis12-pf-2.2.1:attributes/PURCHASE_FINANCE.yaml#attribute_set.html_form.downpayment._description.info | fis12-pf-2.2.1 |
| anchor.dynamic-form | dynamic form | fis12-pf-2.2.1:flows/PURCHASE FINANCE/Purchase_Finance_With_AA.yaml#steps[on_status_unsolicited] | fis12-pf-2.2.1 |
| anchor.emandate-round | emandate round | fis12-pf-2.2.1:flows/PURCHASE FINANCE/Purchase_Finance_Without_AA.yaml#steps[Emanadate_verification_status].action_id | fis12-pf-2.2.1 |
| anchor.emi-repayment | emi repayment | - | fis12-pf-2.2.1 |
| anchor.employment-type | employment type | fis12-pf-2.2.1:attributes/PURCHASE_FINANCE.yaml#attribute_set.html_form.employmentType._description.info | fis12-pf-2.2.1 |
| anchor.error-30001 | error 30001 | fis12-pf-2.2.1:errors/index.yaml#code[30001].From | fis12-pf-2.2.1 |
| anchor.error-30008 | error 30008 | fis12-pf-2.2.1:errors/index.yaml#code[30008].From | fis12-pf-2.2.1 |
| anchor.error-50001 | error 50001 | fis12-pf-2.2.1:errors/index.yaml#code[50001].From | fis12-pf-2.2.1 |
| anchor.error-91216 | error 91216 | - | fis12-pf-2.2.1 |
| anchor.error-code | error code | workbench:scripts/onix-request-lifecycle.md | fis12-pf-2.2.1 |
| anchor.esign-round | esign round | fis12-pf-2.2.1:flows/PURCHASE FINANCE/Purchase_Finance_Without_AA.yaml#steps[E_sign_verification_status].action_id | fis12-pf-2.2.1 |
| anchor.finance-provider | finance provider | fis12-pf-2.2.1:docs/overview.md#real-world-actors | fis12-pf-2.2.1 |
| anchor.financed-product | financed product | fis12-pf-2.2.1:attributes/PURCHASE_FINANCE.yaml#attribute_set.html_form.productSKUID._description.info | fis12-pf-2.2.1 |
| anchor.financed-purchase | financed purchase | - | fis12-pf-2.2.1 |
| anchor.finvu-verification | finvu verification | - | fis12-pf-2.2.1 |
| anchor.flow-pf-sr-with-aa | flow pf sr with aa | fis12-pf-2.2.1:flows/PURCHASE FINANCE/Purchase_Finance_Single_Redirection_With_AA.yaml#steps[on_search5_purchase_finance].mock.defaultPayload.message.catalog.providers[0].items[0].tags[0].list[0].descriptor.code | fis12-pf-2.2.1 |
| anchor.flow-pf-sr-with-aa-igm | flow pf sr with aa igm | fis12-pf-2.2.1:flows/PURCHASE FINANCE/Purchase_Finance_Single_Redirection_With_AA_With_IGM_v-1_0_0_.yaml#steps[on_search5_purchase_finance].mock.defaultPayload.message.catalog.providers[0].items[0].tags[0].list[0].descriptor.code | fis12-pf-2.2.1 |
| anchor.flow-pf-sr-without-aa | flow pf sr without aa | fis12-pf-2.2.1:flows/PURCHASE FINANCE/Purchase_Finance_Single_Redirection_Without_AA.yaml#steps[on_search3_purchase_finance].mock.defaultPayload.message.catalog.providers[0].items[0].xinput.form.id | fis12-pf-2.2.1 |
| anchor.flow-pf-sr-without-aa-cancellation | flow pf sr without aa cancellation | fis12-pf-2.2.1:flows/PURCHASE FINANCE/Purchase_Finance_Single_Redirection_Without_AA_Cancellation.yaml#steps[on_search3_purchase_finance].mock.defaultPayload.message.catalog.providers[0].items[0].xinput.form.id | fis12-pf-2.2.1 |
| anchor.flow-pf-sr-without-aa-foreclosure | flow pf sr without aa foreclosure | fis12-pf-2.2.1:flows/PURCHASE FINANCE/Purchase_Finance_Single_Redirection_Without_AA_Loan_Foreclosure.yaml#steps[on_search3_purchase_finance].mock.defaultPayload.message.catalog.providers[0].items[0].xinput.form.id | fis12-pf-2.2.1 |
| anchor.flow-pf-sr-without-aa-igm | flow pf sr without aa igm | fis12-pf-2.2.1:flows/PURCHASE FINANCE/Purchase_Finance_Single_Redirection_Without_AA_With_IGM_v-1_0_0_.yaml#steps[on_search3_purchase_finance].mock.defaultPayload.message.catalog.providers[0].items[0].xinput.form.id | fis12-pf-2.2.1 |
| anchor.flow-pf-sr-without-aa-missed-emi | flow pf sr without aa missed emi | fis12-pf-2.2.1:flows/PURCHASE FINANCE/Purchase_Finance_Single_Redirection_Without_AA_Missed_EMI_Payment.yaml#steps[on_search3_purchase_finance].mock.defaultPayload.message.catalog.providers[0].items[0].xinput.form.id | fis12-pf-2.2.1 |
| anchor.flow-pf-sr-without-aa-pre-part-payment | flow pf sr without aa pre part payment | fis12-pf-2.2.1:flows/PURCHASE FINANCE/Purchase_Finance_Single_Redirection_Without_AA_Pre_Part_Payment.yaml#steps[on_search3_purchase_finance].mock.defaultPayload.message.catalog.providers[0].items[0].xinput.form.id | fis12-pf-2.2.1 |
| anchor.flow-pf-with-aa | flow pf with aa | fis12-pf-2.2.1:flows/PURCHASE FINANCE/Purchase_Finance_With_AA.yaml#steps[on_search5_purchase_finance].mock.defaultPayload.message.catalog.providers[0].items[0].tags[0].list[0].descriptor.code | fis12-pf-2.2.1 |
| anchor.flow-pf-with-aa-cancellation | flow pf with aa cancellation | fis12-pf-2.2.1:flows/PURCHASE FINANCE/Purchase_Finance_With_AA_Cancellation.yaml#steps[on_search5_purchase_finance].mock.defaultPayload.message.catalog.providers[0].items[0].tags[0].list[0].descriptor.code | fis12-pf-2.2.1 |
| anchor.flow-pf-with-aa-foreclosure | flow pf with aa foreclosure | fis12-pf-2.2.1:flows/PURCHASE FINANCE/Purchase_Finance_With_AA_Loan_Foreclosure.yaml#steps[on_search5_purchase_finance].mock.defaultPayload.message.catalog.providers[0].items[0].tags[0].list[0].descriptor.code | fis12-pf-2.2.1 |
| anchor.flow-pf-with-aa-igm | flow pf with aa igm | fis12-pf-2.2.1:flows/index.yaml#flows[Purchase_Finance_With_AA_With_IGM(v-1.0.0)].tags | fis12-pf-2.2.1 |
| anchor.flow-pf-with-aa-missed-emi | flow pf with aa missed emi | fis12-pf-2.2.1:flows/PURCHASE FINANCE/Purchase_Finance_With_AA_Missed_EMI_Payment.yaml#steps[on_search5_purchase_finance].mock.defaultPayload.message.catalog.providers[0].items[0].tags[0].list[0].descriptor.code | fis12-pf-2.2.1 |
| anchor.flow-pf-with-aa-multiple-offer | flow pf with aa multiple offer | fis12-pf-2.2.1:flows/PURCHASE FINANCE/Purchase_Finance_With_AA_Multiple_Offer.yaml#steps[on_search5_purchase_finance].mock.defaultPayload.message.catalog.providers[0].items[0].tags[0].list[0].descriptor.code | fis12-pf-2.2.1 |
| anchor.flow-pf-with-aa-pre-part-payment | flow pf with aa pre part payment | fis12-pf-2.2.1:flows/PURCHASE FINANCE/Purchase_Finance_With_AA_Pre_Part_Payment.yaml#steps[on_search5_purchase_finance].mock.defaultPayload.message.catalog.providers[0].items[0].tags[0].list[0].descriptor.code | fis12-pf-2.2.1 |
| anchor.flow-pf-without-aa | flow pf without aa | fis12-pf-2.2.1:flows/PURCHASE FINANCE/Purchase_Finance_Without_AA.yaml#steps[on_search3_purchase_finance].mock.defaultPayload.message.catalog.providers[0].items[0].xinput.form.id | fis12-pf-2.2.1 |
| anchor.flow-pf-without-aa-cancellation | flow pf without aa cancellation | fis12-pf-2.2.1:flows/PURCHASE FINANCE/Purchase_Finance_Without_AA_Cancellation.yaml#steps[on_search3_purchase_finance].mock.defaultPayload.message.catalog.providers[0].items[0].xinput.form.id | fis12-pf-2.2.1 |
| anchor.flow-pf-without-aa-foreclosure | flow pf without aa foreclosure | fis12-pf-2.2.1:flows/PURCHASE FINANCE/Purchase_Finance_Without_AA_Loan_Foreclosure.yaml#steps[on_search3_purchase_finance].mock.defaultPayload.message.catalog.providers[0].items[0].xinput.form.id | fis12-pf-2.2.1 |
| anchor.flow-pf-without-aa-igm | flow pf without aa igm | fis12-pf-2.2.1:flows/index.yaml#flows[Purchase_Finance_Without_AA_With_IGM(v-1.0.0)].tags | fis12-pf-2.2.1 |
| anchor.flow-pf-without-aa-missed-emi | flow pf without aa missed emi | fis12-pf-2.2.1:flows/PURCHASE FINANCE/Purchase_Finance_Without_AA_Missed_EMI_Payment.yaml#steps[on_search3_purchase_finance].mock.defaultPayload.message.catalog.providers[0].items[0].xinput.form.id | fis12-pf-2.2.1 |
| anchor.flow-pf-without-aa-multiple-offer | flow pf without aa multiple offer | fis12-pf-2.2.1:flows/PURCHASE FINANCE/Purchase_Finance_Without_AA_Multiple_Offer.yaml#steps[on_search4_purchase_finance].mock.defaultPayload.message.catalog.providers[0].items[0].xinput.form.id | fis12-pf-2.2.1 |
| anchor.flow-pf-without-aa-pre-part-payment | flow pf without aa pre part payment | fis12-pf-2.2.1:flows/PURCHASE FINANCE/Purchase_Finance_Without_AA_Pre_Part_Payment.yaml#steps[on_search3_purchase_finance].mock.defaultPayload.message.catalog.providers[0].items[0].xinput.form.id | fis12-pf-2.2.1 |
| anchor.foreclosure | foreclosure | fis12-pf-2.2.1:flows/PURCHASE FINANCE/Purchase_Finance_Without_AA_Loan_Foreclosure.yaml#steps[update_foreclosure].mock.defaultPayload.message.order.payments[0].time.label | fis12-pf-2.2.1 |
| anchor.foreclosure-fee | foreclosure fee | fis12-pf-2.2.1:flows/PURCHASE FINANCE/Purchase_Finance_Without_AA.yaml#steps[on_search3_purchase_finance].mock.defaultPayload.message.catalog.providers[0].items[1].tags[0].list[4].descriptor.code | fis12-pf-2.2.1 |
| anchor.foreclosure-tail | foreclosure tail | fis12-pf-2.2.1:flows/PURCHASE FINANCE/Purchase_Finance_With_AA_Loan_Foreclosure.yaml#steps[update_foreclosure].mock.defaultPayload.message.order.payments[0].time.label | fis12-pf-2.2.1 |
| anchor.form-response | form response | fis12-pf-2.2.1:flows/PURCHASE FINANCE/Purchase_Finance_Without_AA.yaml#steps[on_search3_purchase_finance].mock.defaultPayload.message.catalog.providers[0].items[0].xinput.form_response.submission_id | fis12-pf-2.2.1 |
| anchor.fulfillment-state-disbursed | fulfillment state disbursed | fis12-pf-2.2.1:flows/PURCHASE FINANCE/Purchase_Finance_Without_AA.yaml#steps[update_purchase_finance].mock.defaultPayload.message.order.fulfillments[0].state.descriptor.code | fis12-pf-2.2.1 |
| anchor.fulfillment-state-initiated | fulfillment state initiated | - | fis12-pf-2.2.1 |
| anchor.fulfillment-state-sanctioned | fulfillment state sanctioned | fis12-pf-2.2.1:validations/index.yaml#_TESTS_.on_update[ON_UPDATE_FULFILLMENTS]._RETURN_[REQUIRED_FULFILLMENT_STATE_CODE].enumList | fis12-pf-2.2.1 |
| anchor.fulfillment-type-enum | fulfillment type enum | fis12-pf-2.2.1:validations/index.yaml#_TESTS_.on_confirm[ON_CONFIRM_FULFILLMENTS]._RETURN_[REQUIRED_FULFILLMENT_TYPE].enumList | fis12-pf-2.2.1 |
| anchor.goods-seller | goods seller | fis12-pf-2.2.1:docs/overview.md#real-world-actors | fis12-pf-2.2.1 |
| anchor.grievance-protocol | grievance protocol | - | fis12-pf-2.2.1 |
| anchor.grievance-redressal-officer | grievance redressal officer | fis12-pf-2.2.1:validations/index.yaml#_TESTS_.on_search[ON_SEARCH_PROVIDER_CONTACT_INFO]._RETURN_[REQUIRED_CONTACT_INFO_LIST].validValues | fis12-pf-2.2.1 |
| anchor.html-form | html form | fis12-pf-2.2.1:flows/PURCHASE FINANCE/Purchase_Finance_With_AA.yaml#steps[search2_purchase_finance] | fis12-pf-2.2.1 |
| anchor.id-type | id type | - | fis12-pf-2.2.1 |
| anchor.igm-1-0-0 | igm 1 0 0 | fis12-pf-2.2.1:validations/index.yaml#_TESTS_.issue[ISSUE_VALIDATION_VERSION_100]._SCOPE_ | fis12-pf-2.2.1 |
| anchor.igm-2-0-0 | igm 2 0 0 | fis12-pf-2.2.1:validations/index.yaml#_TESTS_.issue[ISSUE_VALIDATION_VERSION_200]._SCOPE_ | fis12-pf-2.2.1 |
| anchor.igm-tail | igm tail | fis12-pf-2.2.1:flows/PURCHASE FINANCE/Purchase_Finance_With_AA_With_IGM_v-1_0_0_.yaml#steps[issue_open_100].action_id | fis12-pf-2.2.1 |
| anchor.info-tag | info tag | fis12-pf-2.2.1:validations/index.yaml#_TESTS_.on_select[ON_SELECT_ITEMS_INFO_TAG]._RETURN_[REQUIRED_INFO_TAG_GROUP].tagPath | fis12-pf-2.2.1 |
| anchor.info-tag-full-set | info tag full set | - | fis12-pf-2.2.1 |
| anchor.init | init | fis12-pf-2.2.1:actions/index.yaml#supportedActions.init | fis12-pf-2.2.1 |
| anchor.installment | installment | fis12-pf-2.2.1:flows/PURCHASE FINANCE/Purchase_Finance_Without_AA.yaml#steps[on_confirm_purchase_finance].mock.defaultPayload.message.order.payments[2].time.label | fis12-pf-2.2.1 |
| anchor.installment-deferred | installment deferred | fis12-pf-2.2.1:flows/PURCHASE FINANCE/Purchase_Finance_Without_AA_Loan_Foreclosure.yaml#steps[on_update_unsolicited_foreclosure].mock.defaultPayload.message.order.payments[3].status | fis12-pf-2.2.1 |
| anchor.installment-delayed | installment delayed | - | fis12-pf-2.2.1 |
| anchor.installment-schedule | installment schedule | - | fis12-pf-2.2.1 |
| anchor.interest-rate-type | interest rate type | fis12-pf-2.2.1:validations/index.yaml#_TESTS_.on_select[ON_SELECT_ITEMS_INFO_TAG]._RETURN_[VALID_INTEREST_RATE_TYPE].enumList | fis12-pf-2.2.1 |
| anchor.issue | issue | fis12-pf-2.2.1:actions/index.yaml#supportedActions.issue | fis12-pf-2.2.1 |
| anchor.issue-category | issue category | fis12-pf-2.2.1:validations/index.yaml#_TESTS_.issue[ISSUE_VALIDATION_VERSION_100]._RETURN_[ISSUE_VALIDATION_OPEN]._RETURN_[REQUIRED_ISSUE_CATEGORY].validValues | fis12-pf-2.2.1 |
| anchor.issue-close | issue close | - | fis12-pf-2.2.1 |
| anchor.issue-open | issue open | fis12-pf-2.2.1:flows/PURCHASE FINANCE/Purchase_Finance_With_AA_With_IGM_v-1_0_0_.yaml#steps[issue_close_100].action_id | fis12-pf-2.2.1 |
| anchor.item-code-loan | item code loan | fis12-pf-2.2.1:validations/index.yaml#_TESTS_.on_search[ON_SEARCH_ITEMS]._RETURN_[VALID_ITEM_DESCRIPTOR_CODE].enumList | fis12-pf-2.2.1 |
| anchor.item-price | item price | - | fis12-pf-2.2.1 |
| anchor.lending-service-provider | lending service provider | fis12-pf-2.2.1:validations/index.yaml#_TESTS_.on_search[ON_SEARCH_PROVIDER_LSP_INFO]._RETURN_[REQUIRED_LSP_INFO_LIST].validValues | fis12-pf-2.2.1 |
| anchor.loan-agreement | loan agreement | fis12-pf-2.2.1:validations/index.yaml#_TESTS_.on_confirm[ON_CONFIRM_DOCUMENTS]._RETURN_[VALID_DOCUMENT_DESCRIPTOR_CODE_ENUM].enumList | fis12-pf-2.2.1 |
| anchor.loan-fulfillment | loan fulfillment | fis12-pf-2.2.1:validations/index.yaml#_TESTS_.on_init[ON_INIT_FULFILLMENTS]._RETURN_[REQUIRED_FULFILLMENT_TYPE].enumList | fis12-pf-2.2.1 |
| anchor.loan-item | loan item | fis12-pf-2.2.1:flows/PURCHASE FINANCE/Purchase_Finance_Without_AA.yaml#steps[on_search3_purchase_finance].mock.defaultPayload.message.catalog.providers[0].items[0].xinput.form.id | fis12-pf-2.2.1 |
| anchor.lsp-info-codes | lsp info codes | fis12-pf-2.2.1:validations/index.yaml#_TESTS_.on_search[ON_SEARCH_PROVIDER_LSP_INFO]._RETURN_[REQUIRED_LSP_INFO_LIST].validValues | fis12-pf-2.2.1 |
| anchor.lsp-info-tag | lsp info tag | fis12-pf-2.2.1:validations/index.yaml#_TESTS_.on_search[ON_SEARCH_PROVIDER_LSP_INFO]._RETURN_[REQUIRED_LSP_INFO_TAG_GROUP].tagPath | fis12-pf-2.2.1 |
| anchor.missed-emi-payment | missed emi payment | fis12-pf-2.2.1:flows/PURCHASE FINANCE/Purchase_Finance_Without_AA_Missed_EMI_Payment.yaml#steps[update_missed_Emi].mock.defaultPayload.message.order.payments[0].time.label | fis12-pf-2.2.1 |
| anchor.missed-emi-tail | missed emi tail | fis12-pf-2.2.1:flows/PURCHASE FINANCE/Purchase_Finance_With_AA_Missed_EMI_Payment.yaml#steps[update_missed_Emi].mock.defaultPayload.message.order.payments[0].time.label | fis12-pf-2.2.1 |
| anchor.multi-redirection-journey | multi redirection journey | fis12-pf-2.2.1:flows/PURCHASE FINANCE/Purchase_Finance_Without_AA.yaml#steps[init2_purchase_finance].action_id | fis12-pf-2.2.1 |
| anchor.multiple-offer-variant | multiple offer variant | fis12-pf-2.2.1:flows/PURCHASE FINANCE/Purchase_Finance_With_AA_Multiple_Offer.yaml#steps[on_search4_purchase_finance].mock.defaultPayload.message.catalog.providers[0].items[2].id | fis12-pf-2.2.1 |
| anchor.nack | nack | - | fis12-pf-2.2.1 |
| anchor.non-aa-journey | non aa journey | fis12-pf-2.2.1:flows/index.yaml#flows[Purchase_Finance_Without_AA].tags | fis12-pf-2.2.1 |
| anchor.offer-item | offer item | fis12-pf-2.2.1:flows/PURCHASE FINANCE/Purchase_Finance_Without_AA.yaml#steps[on_search3_purchase_finance].mock.defaultPayload.message.catalog.providers[0].items[1].parent_item_id | fis12-pf-2.2.1 |
| anchor.on-cancel | on cancel | fis12-pf-2.2.1:actions/index.yaml#supportedActions.on_cancel | fis12-pf-2.2.1 |
| anchor.on-confirm | on confirm | fis12-pf-2.2.1:actions/index.yaml#supportedActions.on_confirm | fis12-pf-2.2.1 |
| anchor.on-init | on init | fis12-pf-2.2.1:actions/index.yaml#supportedActions.on_init | fis12-pf-2.2.1 |
| anchor.on-issue | on issue | fis12-pf-2.2.1:actions/index.yaml#supportedActions.on_issue | fis12-pf-2.2.1 |
| anchor.on-issue-status | on issue status | fis12-pf-2.2.1:actions/index.yaml#supportedActions.on_issue_status | fis12-pf-2.2.1 |
| anchor.on-search | on search | fis12-pf-2.2.1:actions/index.yaml#supportedActions.on_search | fis12-pf-2.2.1 |
| anchor.on-select | on select | fis12-pf-2.2.1:actions/index.yaml#supportedActions.on_select | fis12-pf-2.2.1 |
| anchor.on-status | on status | fis12-pf-2.2.1:actions/index.yaml#supportedActions.on_status | fis12-pf-2.2.1 |
| anchor.on-track | on track | fis12-pf-2.2.1:actions/index.yaml#supportedActions.on_track | fis12-pf-2.2.1 |
| anchor.on-update | on update | fis12-pf-2.2.1:actions/index.yaml#supportedActions.on_update | fis12-pf-2.2.1 |
| anchor.order-completed | order completed | - | fis12-pf-2.2.1 |
| anchor.order-status-cancelled | order status cancelled | fis12-pf-2.2.1:flows/PURCHASE FINANCE/Purchase_Finance_Without_AA_Cancellation.yaml#steps[on_update_unsolicited_cancel].mock.defaultPayload.message.order.status | fis12-pf-2.2.1 |
| anchor.order-status-enum | order status enum | fis12-pf-2.2.1:validations/index.yaml#_TESTS_.on_confirm[ON_CONFIRM_ORDER_STATUS].enumList | fis12-pf-2.2.1 |
| anchor.order-status-soft-cancel | order status soft cancel | fis12-pf-2.2.1:validations/index.yaml#_TESTS_.on_cancel[ON_CANCEL_ORDER]._RETURN_[REQUIRED_ORDER_STATUS].enumList | fis12-pf-2.2.1 |
| anchor.parent-category | parent category | - | fis12-pf-2.2.1 |
| anchor.payment-amount | payment amount | - | fis12-pf-2.2.1 |
| anchor.payment-status-enum | payment status enum | fis12-pf-2.2.1:validations/index.yaml#_TESTS_.on_confirm[ON_CONFIRM_PAYMENTS]._RETURN_[VALID_PAYMENT_STATUS_ENUM].enumList | fis12-pf-2.2.1 |
| anchor.payment-time-label | payment time label | fis12-pf-2.2.1:validations/index.yaml#_TESTS_.on_confirm[ON_CONFIRM_PAYMENTS_POST_FULFILLMENT]._RETURN_[REQUIRED_POST_FULFILLMENT_TIME_LABEL].enumList | fis12-pf-2.2.1 |
| anchor.payment-url | payment url | fis12-pf-2.2.1:flows/PURCHASE FINANCE/Purchase_Finance_Without_AA_Loan_Foreclosure.yaml#steps[payment_url_form].action_id | fis12-pf-2.2.1 |
| anchor.payment-url-form | payment url form | fis12-pf-2.2.1:flows/PURCHASE FINANCE/Purchase_Finance_Without_AA_Loan_Foreclosure.yaml#steps[payment_url_form].api | fis12-pf-2.2.1 |
| anchor.pf-action-state-machine | pf action state machine | workbench:frames/flow-state-machine.md | fis12-pf-2.2.1 |
| anchor.pf-attribute-dictionary | pf attribute dictionary | workbench:frames/spec-logic.md | fis12-pf-2.2.1 |
| anchor.pf-discovery-search | pf discovery search | fis12-pf-2.2.1:attributes/PURCHASE_FINANCE.yaml#attribute_set.search.context.bpp_id._description.info | fis12-pf-2.2.1 |
| anchor.pf-error-set | pf error set | - | fis12-pf-2.2.1 |
| anchor.pf-followup-search | pf followup search | fis12-pf-2.2.1:flows/PURCHASE FINANCE/Purchase_Finance_Without_AA.yaml#steps[on_search1_purchase_finance].mock.saveData.bppUri | fis12-pf-2.2.1 |
| anchor.pf-journey | pf journey | fis12-pf-2.2.1:flows/index.yaml#flows[Purchase_Finance_With_AA].usecase | fis12-pf-2.2.1 |
| anchor.pf-validation-battery | pf validation battery | workbench:frames/validation-layers.md | fis12-pf-2.2.1 |
| anchor.playground-flow | playground flow | - | fis12-pf-2.2.1 |
| anchor.post-fulfillment-payment | post fulfillment payment | fis12-pf-2.2.1:validations/index.yaml#_TESTS_.on_confirm[ON_CONFIRM_PAYMENTS_POST_FULFILLMENT]._RETURN_[REQUIRED_POST_FULFILLMENT_BREAKUP_TAG].validTags | fis12-pf-2.2.1 |
| anchor.pre-order-payment | pre order payment | fis12-pf-2.2.1:flows/PURCHASE FINANCE/Purchase_Finance_Without_AA.yaml#steps[on_init1_purchase_finance].mock.defaultPayload.message.order.payments | fis12-pf-2.2.1 |
| anchor.pre-part-payment | pre part payment | fis12-pf-2.2.1:flows/PURCHASE FINANCE/Purchase_Finance_Without_AA_Pre_Part_Payment.yaml#steps[update_prepart].mock.defaultPayload.message.order.payments[0].time.label | fis12-pf-2.2.1 |
| anchor.pre-part-payment-tail | pre part payment tail | fis12-pf-2.2.1:flows/PURCHASE FINANCE/Purchase_Finance_With_AA_Pre_Part_Payment.yaml#steps[update_prepart].mock.defaultPayload.message.order.payments[0].time.label | fis12-pf-2.2.1 |
| anchor.provider | provider | - | fis12-pf-2.2.1 |
| anchor.purchase-finance | purchase finance | fis12-pf-2.2.1:flows/index.yaml#flows[Purchase_Finance_With_AA].usecase | fis12-pf-2.2.1 |
| anchor.quote | quote | fis12-pf-2.2.1:validations/index.yaml#_TESTS_.on_select[ON_SELECT_QUOTE]._RETURN_[REQUIRED_QUOTE_TTL].attr | fis12-pf-2.2.1 |
| anchor.quote-breakup-titles | quote breakup titles | fis12-pf-2.2.1:validations/index.yaml#_TESTS_.on_select[ON_SELECT_QUOTE]._RETURN_[REQUIRED_QUOTE_BREAKUP]._RETURN_[VALID_QUOTE_BREAKUP_TITLE_ENUM].enumList | fis12-pf-2.2.1 |
| anchor.quote-price | quote price | - | fis12-pf-2.2.1 |
| anchor.quote-ttl | quote ttl | - | fis12-pf-2.2.1 |
| anchor.ref-id | ref id | - | fis12-pf-2.2.1 |
| anchor.reportable-flow | reportable flow | fis12-pf-2.2.1:flows/index.yaml#flows[Purchase_Finance_With_AA].tags | fis12-pf-2.2.1 |
| anchor.resolution | resolution | - | fis12-pf-2.2.1 |
| anchor.resolution-provider | resolution provider | - | fis12-pf-2.2.1 |
| anchor.respondent-action | respondent action | - | fis12-pf-2.2.1 |
| anchor.runtime-behavioral | runtime behavioral | - | fis12-pf-2.2.1 |
| anchor.runtime-concept | runtime concept | - | fis12-pf-2.2.1 |
| anchor.search | search | fis12-pf-2.2.1:actions/index.yaml#supportedActions.search | fis12-pf-2.2.1 |
| anchor.select | select | fis12-pf-2.2.1:actions/index.yaml#supportedActions.select | fis12-pf-2.2.1 |
| anchor.seller-subvention | seller subvention | fis12-pf-2.2.1:attributes/PURCHASE_FINANCE.yaml#attribute_set.html_form.maxSellerSubvention._description.info | fis12-pf-2.2.1 |
| anchor.settlement-basis | settlement basis | fis12-pf-2.2.1:validations/index.yaml#_TESTS_.on_search[ON_SEARCH_PAYMENT]._RETURN_[VALID_SETTLEMENT_BASIS_VALUE].enumList | fis12-pf-2.2.1 |
| anchor.settlement-type | settlement type | fis12-pf-2.2.1:validations/index.yaml#_TESTS_.init[INIT_PAYMENT_TAGS]._RETURN_[VALID_SETTLEMENT_TYPE_VALUE].enumList | fis12-pf-2.2.1 |
| anchor.single-lender-redirection | single lender redirection | - | fis12-pf-2.2.1 |
| anchor.single-redirection-journey | single redirection journey | fis12-pf-2.2.1:flows/index.yaml#flows[Purchase_Finance_Single_Redirection_Without_AA].tags | fis12-pf-2.2.1 |
| anchor.soft-cancel | soft cancel | fis12-pf-2.2.1:flows/PURCHASE FINANCE/Purchase_Finance_Without_AA_Cancellation.yaml#steps[soft_cancel_purchase_finance].mock.defaultPayload.message.descriptor.code | fis12-pf-2.2.1 |
| anchor.status | status | fis12-pf-2.2.1:actions/index.yaml#supportedActions.status | fis12-pf-2.2.1 |
| anchor.submission-id | submission id | - | fis12-pf-2.2.1 |
| anchor.subvention | subvention | fis12-pf-2.2.1:validations/index.yaml#_TESTS_.on_select[ON_SELECT_ITEMS_INFO_TAG]._RETURN_[REQUIRED_INFO_LIST].validValues | fis12-pf-2.2.1 |
| anchor.tag-group | tag group | - | fis12-pf-2.2.1 |
| anchor.tag-list | tag list | - | fis12-pf-2.2.1 |
| anchor.track | track | fis12-pf-2.2.1:actions/index.yaml#supportedActions.track | fis12-pf-2.2.1 |
| anchor.transaction-entry | transaction entry | workbench:frames/flow-state-machine.md | fis12-pf-2.2.1 |
| anchor.transaction-id | transaction id | - | fis12-pf-2.2.1 |
| anchor.transit-error-template | transit error template | - | fis12-pf-2.2.1 |
| anchor.trv11-attribute-dictionary | trv11 attribute dictionary | - | fis12-pf-2.2.1 |
| anchor.udyam-number | udyam number | fis12-pf-2.2.1:attributes/PURCHASE_FINANCE.yaml#attribute_set.html_form.udyamNumber._description.info | fis12-pf-2.2.1 |
| anchor.update | update | fis12-pf-2.2.1:actions/index.yaml#supportedActions.update | fis12-pf-2.2.1 |
| anchor.update-target | update target | fis12-pf-2.2.1:validations/index.yaml#_TESTS_.update[UPDATE_TARGET].enumList | fis12-pf-2.2.1 |
| anchor.use-case | use case | - | fis12-pf-2.2.1 |
| anchor.xinput-form | xinput form | fis12-pf-2.2.1:flows/PURCHASE FINANCE/Purchase_Finance_Without_AA.yaml#steps[on_search1_purchase_finance].mock.saveData.product_details_form | fis12-pf-2.2.1 |

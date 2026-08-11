# fis12-2.0.3 KB atoms (structural, book-generic)

anchor.search | isa | anchor.action | basis:declared | asof:fis12-2.0.3 | grounded-in:fis12-2.0.3:actions/index.yaml#supportedActions.search
anchor.on-search | isa | anchor.action | basis:declared | asof:fis12-2.0.3 | grounded-in:fis12-2.0.3:actions/index.yaml#supportedActions.on_search
anchor.select | isa | anchor.action | basis:declared | asof:fis12-2.0.3 | grounded-in:fis12-2.0.3:actions/index.yaml#supportedActions.select
anchor.on-select | isa | anchor.action | basis:declared | asof:fis12-2.0.3 | grounded-in:fis12-2.0.3:actions/index.yaml#supportedActions.on_select
anchor.init | isa | anchor.action | basis:declared | asof:fis12-2.0.3 | grounded-in:fis12-2.0.3:actions/index.yaml#supportedActions.init
anchor.on-init | isa | anchor.action | basis:declared | asof:fis12-2.0.3 | grounded-in:fis12-2.0.3:actions/index.yaml#supportedActions.on_init
anchor.confirm | isa | anchor.action | basis:declared | asof:fis12-2.0.3 | grounded-in:fis12-2.0.3:actions/index.yaml#supportedActions.confirm
anchor.on-confirm | isa | anchor.action | basis:declared | asof:fis12-2.0.3 | grounded-in:fis12-2.0.3:actions/index.yaml#supportedActions.on_confirm
anchor.update | isa | anchor.action | basis:declared | asof:fis12-2.0.3 | grounded-in:fis12-2.0.3:actions/index.yaml#supportedActions.update
anchor.on-update | isa | anchor.action | basis:declared | asof:fis12-2.0.3 | grounded-in:fis12-2.0.3:actions/index.yaml#supportedActions.on_update
anchor.status | isa | anchor.action | basis:declared | asof:fis12-2.0.3 | grounded-in:fis12-2.0.3:actions/index.yaml#supportedActions.status
anchor.on-status | isa | anchor.action | basis:declared | asof:fis12-2.0.3 | grounded-in:fis12-2.0.3:actions/index.yaml#supportedActions.on_status
anchor.issue | isa | anchor.action | basis:declared | asof:fis12-2.0.3 | grounded-in:fis12-2.0.3:actions/index.yaml#supportedActions.issue
anchor.on-issue | isa | anchor.action | basis:declared | asof:fis12-2.0.3 | grounded-in:fis12-2.0.3:actions/index.yaml#supportedActions.on_issue
anchor.on-issue-status | isa | anchor.action | basis:declared | asof:fis12-2.0.3 | grounded-in:fis12-2.0.3:actions/index.yaml#supportedActions.on_issue_status
anchor.search | isa | anchor.transaction-entry | basis:declared | asof:fis12-2.0.3 | grounded-in:fis12-2.0.3:actions/index.yaml#supportedActions.null
anchor.transaction-entry | isa | anchor.runtime-concept | basis:authority | asof:fis12-2.0.3 | grounded-in:workbench:frames/flow-state-machine.md
anchor.search | precedes | anchor.on-search | basis:declared | asof:fis12-2.0.3 | grounded-in:fis12-2.0.3:flows/GOLD LOAN/Gold_Loan_Offline.yaml#steps[on_search_gold_loan_3]
anchor.on-search | precedes | anchor.html-form | basis:declared | asof:fis12-2.0.3 | grounded-in:fis12-2.0.3:flows/GOLD LOAN/Gold_Loan_Offline.yaml#steps[gold_loan_information_form]
anchor.html-form | precedes | anchor.select | basis:declared | asof:fis12-2.0.3 | grounded-in:fis12-2.0.3:flows/GOLD LOAN/Gold_Loan_Offline.yaml#steps[select_1]
anchor.select | precedes | anchor.on-select | basis:declared | asof:fis12-2.0.3 | grounded-in:fis12-2.0.3:flows/GOLD LOAN/Gold_Loan_Offline.yaml#steps[on_select_1]
anchor.on-select | precedes | anchor.select | basis:declared | asof:fis12-2.0.3 | grounded-in:fis12-2.0.3:flows/GOLD LOAN/Gold_Loan_Offline.yaml#steps[select_2]
anchor.select | precedes | anchor.on-select | basis:declared | asof:fis12-2.0.3 | grounded-in:fis12-2.0.3:flows/GOLD LOAN/Gold_Loan_Offline.yaml#steps[on_select_2]
anchor.on-select | precedes | anchor.dynamic-form | basis:declared | asof:fis12-2.0.3 | grounded-in:fis12-2.0.3:flows/GOLD LOAN/Gold_Loan_Offline.yaml#steps[Ekyc_details_verification_status]
anchor.dynamic-form | precedes | anchor.on-status | basis:declared | asof:fis12-2.0.3 | grounded-in:fis12-2.0.3:flows/GOLD LOAN/Gold_Loan_Offline.yaml#steps[on_status_kyc_verification]
anchor.on-status | precedes | anchor.status | basis:declared | asof:fis12-2.0.3 | grounded-in:fis12-2.0.3:flows/GOLD LOAN/Gold_Loan_Offline.yaml#steps[status_gold_loan_3]
anchor.status | precedes | anchor.on-status | basis:declared | asof:fis12-2.0.3 | grounded-in:fis12-2.0.3:flows/GOLD LOAN/Gold_Loan_Offline.yaml#steps[on_status_gold_loan_3]
anchor.on-status | precedes | anchor.on-status | basis:declared | asof:fis12-2.0.3 | grounded-in:fis12-2.0.3:flows/GOLD LOAN/Gold_Loan_Offline.yaml#steps[on_status_gold_loan_3_order_update]
anchor.on-status | precedes | anchor.confirm | basis:declared | asof:fis12-2.0.3 | grounded-in:fis12-2.0.3:flows/GOLD LOAN/Gold_Loan_Offline.yaml#steps[confirm_gold_loan_3]
anchor.confirm | precedes | anchor.on-confirm | basis:declared | asof:fis12-2.0.3 | grounded-in:fis12-2.0.3:flows/GOLD LOAN/Gold_Loan_Offline.yaml#steps[on_confirm_gold_loan_3]
anchor.on-confirm | precedes | anchor.on-status | basis:declared | asof:fis12-2.0.3 | grounded-in:fis12-2.0.3:flows/GOLD LOAN/Gold_Loan_Offline.yaml#steps[on_status_installment_1]
anchor.search | requires | "provider-id" | basis:inferred | asof:fis12-2.0.3

# --- Stage E candidate units (535) ---
anchor.ondc-fis12 | isa | anchor.lending-domain | basis:declared | asof:fis12-2.0.3 | grounded-in:fis12-2.0.3:index.yaml#info.domain
anchor.lending-domain | isa | anchor.runtime-concept | basis:authority | asof:fis12-2.0.3 | grounded-in:workbench:frames/ondc-ecosystem.md
anchor.ondc-fis12 | has-slot | anchor.gold-loan-usecase | basis:declared | asof:fis12-2.0.3 | grounded-in:fis12-2.0.3:index.yaml#info.x-usecases[GOLD LOAN]
anchor.ondc-fis12 | has-slot | anchor.personal-loan-usecase | basis:declared | asof:fis12-2.0.3 | grounded-in:fis12-2.0.3:index.yaml#info.x-usecases[PERSONAL LOAN]
anchor.gold-loan-usecase | disjoint-with | anchor.personal-loan-usecase | basis:declared | asof:fis12-2.0.3 | grounded-in:fis12-2.0.3:attributes/GOLD_LOAN.yaml#meta.use_case_id
anchor.gold-loan | isa | anchor.credit-product | basis:authority | asof:fis12-2.0.3 | grounded-in:fis12-2.0.3:docs/overview.md#key-concepts
anchor.personal-loan | isa | anchor.credit-product | basis:authority | asof:fis12-2.0.3 | grounded-in:fis12-2.0.3:docs/overview.md#key-concepts
anchor.ondc-fis12 | requires | anchor.multi-lender-discovery | basis:authority | asof:fis12-2.0.3 | grounded-in:fis12-2.0.3:docs/overview.md#sector-purpose
anchor.borrower | isa | anchor.transaction-actor | basis:authority | asof:fis12-2.0.3 | grounded-in:fis12-2.0.3:docs/overview.md#real-world-actors
anchor.lender | isa | anchor.transaction-actor | basis:authority | asof:fis12-2.0.3 | grounded-in:fis12-2.0.3:docs/overview.md#real-world-actors
anchor.lender | isa | anchor.bpp | basis:authority | asof:fis12-2.0.3 | grounded-in:fis12-2.0.3:docs/overview.md#real-world-actors
anchor.bap | isa | anchor.transaction-actor | basis:declared | asof:fis12-2.0.3 | grounded-in:fis12-2.0.3:attributes/PERSONAL_LOAN.yaml#attribute_set.search.context.action._description.owner
anchor.bpp | isa | anchor.transaction-actor | basis:declared | asof:fis12-2.0.3 | grounded-in:fis12-2.0.3:attributes/PERSONAL_LOAN.yaml#attribute_set.on_search.message._description.owner
anchor.bap | disjoint-with | anchor.bpp | basis:declared | asof:fis12-2.0.3 | grounded-in:fis12-2.0.3:validations/index.yaml#_TESTS_.search[SEARCH_PAYMENT]._RETURN_[VALID_PAYMENT_COLLECTED_BY_ENUM].enumList
anchor.single-redirection | isa | anchor.loan-journey-pattern | basis:authority | asof:fis12-2.0.3 | grounded-in:fis12-2.0.3:docs/overview.md#key-concepts
anchor.real-time-loan-tracking | isa | anchor.loan-journey-pattern | basis:authority | asof:fis12-2.0.3 | grounded-in:fis12-2.0.3:docs/overview.md#key-concepts
anchor.emi-management | isa | anchor.loan-journey-pattern | basis:authority | asof:fis12-2.0.3 | grounded-in:fis12-2.0.3:docs/overview.md#key-concepts
anchor.real-time-loan-tracking | requires | anchor.unsolicited-callback | basis:authority | asof:fis12-2.0.3 | grounded-in:fis12-2.0.3:docs/overview.md#example-scenario
anchor.emi | isa | anchor.loan-servicing-event | basis:authority | asof:fis12-2.0.3 | grounded-in:fis12-2.0.3:docs/overview.md#use-cases
anchor.foreclosure | isa | anchor.loan-servicing-event | basis:authority | asof:fis12-2.0.3 | grounded-in:fis12-2.0.3:docs/overview.md#use-cases
anchor.pre-part-payment | isa | anchor.loan-servicing-event | basis:authority | asof:fis12-2.0.3 | grounded-in:fis12-2.0.3:docs/overview.md#use-cases
anchor.missed-emi | isa | anchor.loan-servicing-event | basis:authority | asof:fis12-2.0.3 | grounded-in:fis12-2.0.3:docs/overview.md#use-cases
anchor.loan-servicing-event | precedes | anchor.loan-disbursal | basis:inferred | asof:fis12-2.0.3
anchor.fis12-2-0-3 | not-has-slot | anchor.release-notes-content | basis:declared | asof:fis12-2.0.3 | grounded-in:fis12-2.0.3:docs/release-notes.md#ondcfis12-203-release-notes
anchor.fis12-2-0-3 | not-has-slot | anchor.external-references | basis:declared | asof:fis12-2.0.3 | grounded-in:fis12-2.0.3:docs/references.md#ondcfis12-203-references
anchor.on-search | precedes | anchor.select | basis:declared | asof:fis12-2.0.3 | grounded-in:fis12-2.0.3:actions/index.yaml#supportedActions.on_search[select]
anchor.select | precedes | anchor.select | basis:declared | asof:fis12-2.0.3 | grounded-in:fis12-2.0.3:actions/index.yaml#supportedActions.select[select]
anchor.on-select | precedes | anchor.init | basis:declared | asof:fis12-2.0.3 | grounded-in:fis12-2.0.3:actions/index.yaml#supportedActions.on_select[init]
anchor.on-select | precedes | anchor.on-status | basis:declared | asof:fis12-2.0.3 | grounded-in:fis12-2.0.3:actions/index.yaml#supportedActions.on_select[on_status]
anchor.init | precedes | anchor.on-init | basis:declared | asof:fis12-2.0.3 | grounded-in:fis12-2.0.3:actions/index.yaml#supportedActions.init[on_init]
anchor.on-init | precedes | anchor.confirm | basis:declared | asof:fis12-2.0.3 | grounded-in:fis12-2.0.3:actions/index.yaml#supportedActions.on_init[confirm]
anchor.on-init | precedes | anchor.init | basis:declared | asof:fis12-2.0.3 | grounded-in:fis12-2.0.3:actions/index.yaml#supportedActions.on_init[init]
anchor.on-init | precedes | anchor.on-status | basis:declared | asof:fis12-2.0.3 | grounded-in:fis12-2.0.3:actions/index.yaml#supportedActions.on_init[on_status]
anchor.on-confirm | precedes | anchor.update | basis:declared | asof:fis12-2.0.3 | grounded-in:fis12-2.0.3:actions/index.yaml#supportedActions.on_confirm[update]
anchor.on-confirm | precedes | anchor.on-update | basis:declared | asof:fis12-2.0.3 | grounded-in:fis12-2.0.3:actions/index.yaml#supportedActions.on_confirm[on_update]
anchor.on-confirm | precedes | anchor.status | basis:declared | asof:fis12-2.0.3 | grounded-in:fis12-2.0.3:actions/index.yaml#supportedActions.on_confirm[status]
anchor.on-confirm | precedes | anchor.issue | basis:declared | asof:fis12-2.0.3 | grounded-in:fis12-2.0.3:actions/index.yaml#supportedActions.on_confirm[issue]
anchor.update | precedes | anchor.on-update | basis:declared | asof:fis12-2.0.3 | grounded-in:fis12-2.0.3:actions/index.yaml#supportedActions.update[on_update]
anchor.on-update | precedes | anchor.update | basis:declared | asof:fis12-2.0.3 | grounded-in:fis12-2.0.3:actions/index.yaml#supportedActions.on_update[update]
anchor.on-update | precedes | anchor.on-update | basis:declared | asof:fis12-2.0.3 | grounded-in:fis12-2.0.3:actions/index.yaml#supportedActions.on_update[on_update]
anchor.on-update | precedes | anchor.status | basis:declared | asof:fis12-2.0.3 | grounded-in:fis12-2.0.3:actions/index.yaml#supportedActions.on_update[status]
anchor.on-status | precedes | anchor.init | basis:declared | asof:fis12-2.0.3 | grounded-in:fis12-2.0.3:actions/index.yaml#supportedActions.on_status[init]
anchor.on-status | precedes | anchor.update | basis:declared | asof:fis12-2.0.3 | grounded-in:fis12-2.0.3:actions/index.yaml#supportedActions.on_status[update]
anchor.on-status | precedes | anchor.issue | basis:declared | asof:fis12-2.0.3 | grounded-in:fis12-2.0.3:actions/index.yaml#supportedActions.on_status[issue]
anchor.issue | precedes | anchor.on-issue | basis:declared | asof:fis12-2.0.3 | grounded-in:fis12-2.0.3:actions/index.yaml#supportedActions.issue[on_issue]
anchor.issue | precedes | anchor.issue | basis:declared | asof:fis12-2.0.3 | grounded-in:fis12-2.0.3:actions/index.yaml#supportedActions.issue[issue]
anchor.issue | precedes | anchor.on-update | basis:declared | asof:fis12-2.0.3 | grounded-in:fis12-2.0.3:actions/index.yaml#supportedActions.issue[on_update]
anchor.issue | precedes | anchor.on-status | basis:declared | asof:fis12-2.0.3 | grounded-in:fis12-2.0.3:actions/index.yaml#supportedActions.issue[on_status]
anchor.issue | precedes | anchor.on-confirm | basis:declared | asof:fis12-2.0.3 | grounded-in:fis12-2.0.3:actions/index.yaml#supportedActions.issue[on_confirm]
anchor.issue | precedes | anchor.on-issue-status | basis:declared | asof:fis12-2.0.3 | grounded-in:fis12-2.0.3:actions/index.yaml#supportedActions.issue[on_issue_status]
anchor.issue | precedes | anchor.update | basis:declared | asof:fis12-2.0.3 | grounded-in:fis12-2.0.3:actions/index.yaml#supportedActions.issue[update]
anchor.on-issue | precedes | anchor.issue | basis:declared | asof:fis12-2.0.3 | grounded-in:fis12-2.0.3:actions/index.yaml#supportedActions.on_issue[issue]
anchor.on-issue | precedes | anchor.on-issue | basis:declared | asof:fis12-2.0.3 | grounded-in:fis12-2.0.3:actions/index.yaml#supportedActions.on_issue[on_issue]
anchor.on-issue | precedes | anchor.on-status | basis:declared | asof:fis12-2.0.3 | grounded-in:fis12-2.0.3:actions/index.yaml#supportedActions.on_issue[on_status]
anchor.on-issue | precedes | anchor.on-issue-status | basis:declared | asof:fis12-2.0.3 | grounded-in:fis12-2.0.3:actions/index.yaml#supportedActions.on_issue[on_issue_status]
anchor.on-issue | precedes | anchor.update | basis:declared | asof:fis12-2.0.3 | grounded-in:fis12-2.0.3:actions/index.yaml#supportedActions.on_issue[update]
anchor.on-issue | precedes | anchor.on-update | basis:declared | asof:fis12-2.0.3 | grounded-in:fis12-2.0.3:actions/index.yaml#supportedActions.on_issue[on_update]
anchor.on-issue-status | precedes | anchor.on-issue | basis:declared | asof:fis12-2.0.3 | grounded-in:fis12-2.0.3:actions/index.yaml#supportedActions.on_issue_status[on_issue]
anchor.on-issue-status | precedes | anchor.issue | basis:declared | asof:fis12-2.0.3 | grounded-in:fis12-2.0.3:actions/index.yaml#supportedActions.on_issue_status[issue]
anchor.on-issue-status | precedes | anchor.on-update | basis:declared | asof:fis12-2.0.3 | grounded-in:fis12-2.0.3:actions/index.yaml#supportedActions.on_issue_status[on_update]
anchor.on-issue-status | precedes | anchor.update | basis:declared | asof:fis12-2.0.3 | grounded-in:fis12-2.0.3:actions/index.yaml#supportedActions.on_issue_status[update]
anchor.on-search | requires | anchor.search | basis:declared | asof:fis12-2.0.3 | grounded-in:fis12-2.0.3:actions/index.yaml#apiProperties.on_search.async_predecessor
anchor.on-init | requires | anchor.init | basis:declared | asof:fis12-2.0.3 | grounded-in:fis12-2.0.3:actions/index.yaml#apiProperties.on_init.async_predecessor
anchor.on-confirm | requires | anchor.confirm | basis:declared | asof:fis12-2.0.3 | grounded-in:fis12-2.0.3:actions/index.yaml#apiProperties.on_confirm.async_predecessor
anchor.async-predecessor | isa | anchor.runtime-concept | basis:authority | asof:fis12-2.0.3 | grounded-in:workbench:frames/flow-state-machine.md
anchor.transaction-partner | isa | anchor.runtime-concept | basis:authority | asof:fis12-2.0.3 | grounded-in:workbench:frames/flow-state-machine.md
anchor.search | not-requires | anchor.async-predecessor | basis:declared | asof:fis12-2.0.3 | grounded-in:fis12-2.0.3:actions/index.yaml#apiProperties.search.async_predecessor
anchor.select | not-requires | anchor.async-predecessor | basis:declared | asof:fis12-2.0.3 | grounded-in:fis12-2.0.3:actions/index.yaml#apiProperties.select.async_predecessor
anchor.on-select | not-requires | anchor.async-predecessor | basis:declared | asof:fis12-2.0.3 | grounded-in:fis12-2.0.3:actions/index.yaml#apiProperties.on_select.async_predecessor
anchor.init | not-requires | anchor.async-predecessor | basis:declared | asof:fis12-2.0.3 | grounded-in:fis12-2.0.3:actions/index.yaml#apiProperties.init.async_predecessor
anchor.confirm | not-requires | anchor.async-predecessor | basis:declared | asof:fis12-2.0.3 | grounded-in:fis12-2.0.3:actions/index.yaml#apiProperties.confirm.async_predecessor
anchor.update | not-requires | anchor.async-predecessor | basis:declared | asof:fis12-2.0.3 | grounded-in:fis12-2.0.3:actions/index.yaml#apiProperties.update.async_predecessor
anchor.on-update | not-requires | anchor.async-predecessor | basis:declared | asof:fis12-2.0.3 | grounded-in:fis12-2.0.3:actions/index.yaml#apiProperties.on_update.async_predecessor
anchor.status | not-requires | anchor.async-predecessor | basis:declared | asof:fis12-2.0.3 | grounded-in:fis12-2.0.3:actions/index.yaml#apiProperties.status.async_predecessor
anchor.on-status | not-requires | anchor.async-predecessor | basis:declared | asof:fis12-2.0.3 | grounded-in:fis12-2.0.3:actions/index.yaml#apiProperties.on_status.async_predecessor
anchor.issue | not-requires | anchor.async-predecessor | basis:declared | asof:fis12-2.0.3 | grounded-in:fis12-2.0.3:actions/index.yaml#apiProperties.issue.async_predecessor
anchor.on-issue | not-requires | anchor.async-predecessor | basis:declared | asof:fis12-2.0.3 | grounded-in:fis12-2.0.3:actions/index.yaml#apiProperties.on_issue.async_predecessor
anchor.on-issue-status | not-requires | anchor.async-predecessor | basis:declared | asof:fis12-2.0.3 | grounded-in:fis12-2.0.3:actions/index.yaml#apiProperties.on_issue_status.async_predecessor
anchor.on-search | wasInformedBy | anchor.search | basis:declared | asof:fis12-2.0.3 | grounded-in:fis12-2.0.3:actions/index.yaml#apiProperties.on_search.transaction_partner[search]
anchor.select | wasInformedBy | anchor.on-search | basis:declared | asof:fis12-2.0.3 | grounded-in:fis12-2.0.3:actions/index.yaml#apiProperties.select.transaction_partner[on_search]
anchor.on-select | wasInformedBy | anchor.select | basis:declared | asof:fis12-2.0.3 | grounded-in:fis12-2.0.3:actions/index.yaml#apiProperties.on_select.transaction_partner[select]
anchor.init | wasInformedBy | anchor.on-select | basis:declared | asof:fis12-2.0.3 | grounded-in:fis12-2.0.3:actions/index.yaml#apiProperties.init.transaction_partner[on_select]
anchor.on-init | wasInformedBy | anchor.init | basis:declared | asof:fis12-2.0.3 | grounded-in:fis12-2.0.3:actions/index.yaml#apiProperties.on_init.transaction_partner[init]
anchor.on-confirm | wasInformedBy | anchor.confirm | basis:declared | asof:fis12-2.0.3 | grounded-in:fis12-2.0.3:actions/index.yaml#apiProperties.on_confirm.transaction_partner[confirm]
anchor.update | wasInformedBy | anchor.on-confirm | basis:declared | asof:fis12-2.0.3 | grounded-in:fis12-2.0.3:actions/index.yaml#apiProperties.update.transaction_partner[on_confirm]
anchor.search | not-wasInformedBy | anchor.transaction-partner | basis:declared | asof:fis12-2.0.3 | grounded-in:fis12-2.0.3:actions/index.yaml#apiProperties.search.transaction_partner
anchor.confirm | not-wasInformedBy | anchor.transaction-partner | basis:declared | asof:fis12-2.0.3 | grounded-in:fis12-2.0.3:actions/index.yaml#apiProperties.confirm.transaction_partner
anchor.on-update | not-wasInformedBy | anchor.transaction-partner | basis:declared | asof:fis12-2.0.3 | grounded-in:fis12-2.0.3:actions/index.yaml#apiProperties.on_update.transaction_partner
anchor.status | not-wasInformedBy | anchor.transaction-partner | basis:declared | asof:fis12-2.0.3 | grounded-in:fis12-2.0.3:actions/index.yaml#apiProperties.status.transaction_partner
anchor.on-status | not-wasInformedBy | anchor.transaction-partner | basis:declared | asof:fis12-2.0.3 | grounded-in:fis12-2.0.3:actions/index.yaml#apiProperties.on_status.transaction_partner
anchor.issue | not-wasInformedBy | anchor.transaction-partner | basis:declared | asof:fis12-2.0.3 | grounded-in:fis12-2.0.3:actions/index.yaml#apiProperties.issue.transaction_partner
anchor.on-issue | not-wasInformedBy | anchor.transaction-partner | basis:declared | asof:fis12-2.0.3 | grounded-in:fis12-2.0.3:actions/index.yaml#apiProperties.on_issue.transaction_partner
anchor.on-issue-status | not-wasInformedBy | anchor.transaction-partner | basis:declared | asof:fis12-2.0.3 | grounded-in:fis12-2.0.3:actions/index.yaml#apiProperties.on_issue_status.transaction_partner
anchor.flow-personal-loan-offline | isa | anchor.loan-journey | basis:declared | asof:fis12-2.0.3 | grounded-in:fis12-2.0.3:flows/index.yaml#flows[Personal_Loan_Offline].id
anchor.flow-personal-loan-single-redirection | isa | anchor.loan-journey | basis:declared | asof:fis12-2.0.3 | grounded-in:fis12-2.0.3:flows/index.yaml#flows[Personal_Loan_Single_Redirection].id
anchor.flow-personal-loan-dedupe-check | isa | anchor.loan-journey | basis:declared | asof:fis12-2.0.3 | grounded-in:fis12-2.0.3:flows/index.yaml#flows[Personal_Loan_Dedupe_Check].id
anchor.flow-gold-loan-offline | isa | anchor.loan-journey | basis:declared | asof:fis12-2.0.3 | grounded-in:fis12-2.0.3:flows/index.yaml#flows[Gold_Loan_Offline].id
anchor.flow-gold-loan-offline-igm-1-0-0 | isa | anchor.loan-journey | basis:declared | asof:fis12-2.0.3 | grounded-in:fis12-2.0.3:flows/index.yaml#flows[Gold_Loan_Offline_with_igm_1.0.0].id
anchor.flow-personal-loan-foreclosure-offline | isa | anchor.loan-journey | basis:declared | asof:fis12-2.0.3 | grounded-in:fis12-2.0.3:flows/index.yaml#flows[Personal_Loan_Foreclosure_Offline].id
anchor.flow-personal-loan-missed-emi-offline | isa | anchor.loan-journey | basis:declared | asof:fis12-2.0.3 | grounded-in:fis12-2.0.3:flows/index.yaml#flows[Personal_Loan_missed_emi_payment_Offline].id
anchor.flow-personal-loan-pre-part-payment-offline | isa | anchor.loan-journey | basis:declared | asof:fis12-2.0.3 | grounded-in:fis12-2.0.3:flows/index.yaml#flows[Personal_Loan_Pre_Part_Payment_Offline].id
anchor.flow-personal-loan-offline-igm-1-0-0 | isa | anchor.loan-journey | basis:declared | asof:fis12-2.0.3 | grounded-in:fis12-2.0.3:flows/index.yaml#flows[Personal_Loan_Offline_With_IGM(v-1.0.0)].id
anchor.flow-personal-loan-single-redirection-igm-1-0-0 | isa | anchor.loan-journey | basis:declared | asof:fis12-2.0.3 | grounded-in:fis12-2.0.3:flows/index.yaml#flows[Personal_Loan_Single_Redirection_With_IGM(v-1.0.0)].id
anchor.flow-personal-loan-offline | scoped-to | anchor.personal-loan-usecase | basis:declared | asof:fis12-2.0.3 | grounded-in:fis12-2.0.3:flows/index.yaml#flows[Personal_Loan_Offline].usecase
anchor.flow-personal-loan-single-redirection | scoped-to | anchor.personal-loan-usecase | basis:declared | asof:fis12-2.0.3 | grounded-in:fis12-2.0.3:flows/index.yaml#flows[Personal_Loan_Single_Redirection].usecase
anchor.flow-personal-loan-dedupe-check | scoped-to | anchor.personal-loan-usecase | basis:declared | asof:fis12-2.0.3 | grounded-in:fis12-2.0.3:flows/index.yaml#flows[Personal_Loan_Dedupe_Check].usecase
anchor.flow-gold-loan-offline | scoped-to | anchor.gold-loan-usecase | basis:declared | asof:fis12-2.0.3 | grounded-in:fis12-2.0.3:flows/index.yaml#flows[Gold_Loan_Offline].usecase
anchor.flow-gold-loan-offline-igm-1-0-0 | scoped-to | anchor.gold-loan-usecase | basis:declared | asof:fis12-2.0.3 | grounded-in:fis12-2.0.3:flows/index.yaml#flows[Gold_Loan_Offline_with_igm_1.0.0].usecase
anchor.flow-personal-loan-foreclosure-offline | scoped-to | anchor.personal-loan-usecase | basis:declared | asof:fis12-2.0.3 | grounded-in:fis12-2.0.3:flows/index.yaml#flows[Personal_Loan_Foreclosure_Offline].usecase
anchor.flow-personal-loan-missed-emi-offline | scoped-to | anchor.personal-loan-usecase | basis:declared | asof:fis12-2.0.3 | grounded-in:fis12-2.0.3:flows/index.yaml#flows[Personal_Loan_missed_emi_payment_Offline].usecase
anchor.flow-personal-loan-pre-part-payment-offline | scoped-to | anchor.personal-loan-usecase | basis:declared | asof:fis12-2.0.3 | grounded-in:fis12-2.0.3:flows/index.yaml#flows[Personal_Loan_Pre_Part_Payment_Offline].usecase
anchor.flow-personal-loan-offline-igm-1-0-0 | scoped-to | anchor.personal-loan-usecase | basis:declared | asof:fis12-2.0.3 | grounded-in:fis12-2.0.3:flows/index.yaml#flows[Personal_Loan_Offline_With_IGM(v-1.0.0)].usecase
anchor.flow-personal-loan-single-redirection-igm-1-0-0 | scoped-to | anchor.personal-loan-usecase | basis:declared | asof:fis12-2.0.3 | grounded-in:fis12-2.0.3:flows/index.yaml#flows[Personal_Loan_Single_Redirection_With_IGM(v-1.0.0)].usecase
anchor.flow-personal-loan-offline | causes | anchor.lending-decision | basis:declared | asof:fis12-2.0.3 | grounded-in:fis12-2.0.3:flows/index.yaml#flows[Personal_Loan_Offline].description
anchor.flow-personal-loan-offline | requires | anchor.offline-underwriting | basis:declared | asof:fis12-2.0.3 | grounded-in:fis12-2.0.3:flows/index.yaml#flows[Personal_Loan_Offline].description
anchor.flow-gold-loan-offline | requires | anchor.offline-underwriting | basis:declared | asof:fis12-2.0.3 | grounded-in:fis12-2.0.3:flows/index.yaml#flows[Gold_Loan_Offline].description
anchor.flow-personal-loan-single-redirection | requires | anchor.single-redirection | basis:declared | asof:fis12-2.0.3 | grounded-in:fis12-2.0.3:flows/index.yaml#flows[Personal_Loan_Single_Redirection].description
anchor.flow-personal-loan-dedupe-check | causes | anchor.duplicate-application-filtering | basis:declared | asof:fis12-2.0.3 | grounded-in:fis12-2.0.3:flows/index.yaml#flows[Personal_Loan_Dedupe_Check].description
anchor.flow-personal-loan-foreclosure-offline | causes | anchor.loan-account-closure | basis:declared | asof:fis12-2.0.3 | grounded-in:fis12-2.0.3:flows/index.yaml#flows[Personal_Loan_Foreclosure_Offline].description
anchor.flow-personal-loan-missed-emi-offline | causes | anchor.missed-emi-settlement | basis:declared | asof:fis12-2.0.3 | grounded-in:fis12-2.0.3:flows/index.yaml#flows[Personal_Loan_missed_emi_payment_Offline].description
anchor.flow-personal-loan-pre-part-payment-offline | causes | anchor.revised-repayment-terms | basis:declared | asof:fis12-2.0.3 | grounded-in:fis12-2.0.3:flows/index.yaml#flows[Personal_Loan_Pre_Part_Payment_Offline].description
anchor.flow-gold-loan-offline-igm-1-0-0 | wasDerivedFrom | anchor.flow-gold-loan-offline | basis:declared | asof:fis12-2.0.3 | grounded-in:fis12-2.0.3:flows/GOLD LOAN/Gold_Loan_Offline_with_igm_1.0.0.yaml#steps[issue_open_100]
anchor.flow-personal-loan-offline-igm-1-0-0 | wasDerivedFrom | anchor.flow-personal-loan-offline | basis:declared | asof:fis12-2.0.3 | grounded-in:fis12-2.0.3:flows/PERSONAL LOAN/Personal_Loan_Offline_With_IGM_v-1_0_0_.yaml#steps[issue_open_100]
anchor.flow-personal-loan-single-redirection-igm-1-0-0 | wasDerivedFrom | anchor.flow-personal-loan-single-redirection | basis:declared | asof:fis12-2.0.3 | grounded-in:fis12-2.0.3:flows/PERSONAL LOAN/Personal_Loan_Single_Redirection_With_IGM_v-1_0_0_.yaml#steps[issue_open_100]
anchor.flow-gold-loan-offline-igm-1-0-0 | requires | anchor.igm-1-0-0 | basis:declared | asof:fis12-2.0.3 | grounded-in:fis12-2.0.3:flows/index.yaml#flows[Gold_Loan_Offline_with_igm_1.0.0].description
anchor.igm-1-0-0 | isa | anchor.grievance-protocol | basis:declared | asof:fis12-2.0.3 | grounded-in:fis12-2.0.3:validations/index.yaml#_TESTS_.issue[ISSUE_VALIDATION_VERSION_100]
anchor.igm-2-0-0 | isa | anchor.grievance-protocol | basis:declared | asof:fis12-2.0.3 | grounded-in:fis12-2.0.3:validations/index.yaml#_TESTS_.issue[ISSUE_VALIDATION_VERSION_200]
anchor.igm-1-0-0 | disjoint-with | anchor.igm-2-0-0 | basis:declared | asof:fis12-2.0.3 | grounded-in:fis12-2.0.3:validations/index.yaml#_TESTS_.issue[ISSUE_VALIDATION_VERSION_100]._SCOPE_
anchor.igm-1-0-0 | requires | anchor.issue-actions-legacy | basis:declared | asof:fis12-2.0.3 | grounded-in:fis12-2.0.3:validations/index.yaml#_TESTS_.on_issue[ON_ISSUE_VALIDATION_VERSION_100]._SCOPE_
anchor.igm-2-0-0 | requires | anchor.issue-actions | basis:declared | asof:fis12-2.0.3 | grounded-in:fis12-2.0.3:validations/index.yaml#_TESTS_.on_issue[ON_ISSUE_VALIDATION_VERSION_200]._SCOPE_
anchor.search | sent-by | anchor.bap | basis:declared | asof:fis12-2.0.3 | grounded-in:fis12-2.0.3:flows/PERSONAL LOAN/Personal_Loan_Offline.yaml#steps[search_personal_loan_3].owner
anchor.on-search | sent-by | anchor.bpp | basis:declared | asof:fis12-2.0.3 | grounded-in:fis12-2.0.3:flows/PERSONAL LOAN/Personal_Loan_Offline.yaml#steps[on_search_personal_loan_3].owner
anchor.select | sent-by | anchor.bap | basis:declared | asof:fis12-2.0.3 | grounded-in:fis12-2.0.3:flows/PERSONAL LOAN/Personal_Loan_Offline.yaml#steps[select_3_personal_loan_3].owner
anchor.on-select | sent-by | anchor.bpp | basis:declared | asof:fis12-2.0.3 | grounded-in:fis12-2.0.3:flows/PERSONAL LOAN/Personal_Loan_Offline.yaml#steps[on_select_3_personal_loan_3].owner
anchor.status | sent-by | anchor.bap | basis:declared | asof:fis12-2.0.3 | grounded-in:fis12-2.0.3:flows/PERSONAL LOAN/Personal_Loan_Offline.yaml#steps[status_personal_loan_3].owner
anchor.on-status | sent-by | anchor.bpp | basis:declared | asof:fis12-2.0.3 | grounded-in:fis12-2.0.3:flows/PERSONAL LOAN/Personal_Loan_Offline.yaml#steps[on_status_personal_loan_3].owner
anchor.confirm | sent-by | anchor.bap | basis:declared | asof:fis12-2.0.3 | grounded-in:fis12-2.0.3:flows/PERSONAL LOAN/Personal_Loan_Offline.yaml#steps[confirm_personal_loan_3].owner
anchor.on-confirm | sent-by | anchor.bpp | basis:declared | asof:fis12-2.0.3 | grounded-in:fis12-2.0.3:flows/PERSONAL LOAN/Personal_Loan_Offline.yaml#steps[on_confirm_personal_loan_3].owner
anchor.update | sent-by | anchor.bap | basis:declared | asof:fis12-2.0.3 | grounded-in:fis12-2.0.3:flows/PERSONAL LOAN/Personal_Loan_Foreclosure_Offline.yaml#steps[update_personal_loan_3].owner
anchor.on-update | sent-by | anchor.bpp | basis:declared | asof:fis12-2.0.3 | grounded-in:fis12-2.0.3:flows/PERSONAL LOAN/Personal_Loan_Foreclosure_Offline.yaml#steps[on_update_foreclosure_pl].owner
anchor.issue | sent-by | anchor.bap | basis:declared | asof:fis12-2.0.3 | grounded-in:fis12-2.0.3:flows/GOLD LOAN/Gold_Loan_Offline_with_igm_1.0.0.yaml#steps[issue_open_100].owner
anchor.on-issue | sent-by | anchor.bpp | basis:declared | asof:fis12-2.0.3 | grounded-in:fis12-2.0.3:flows/GOLD LOAN/Gold_Loan_Offline_with_igm_1.0.0.yaml#steps[on_issue_processing_100].owner
anchor.on-issue-status | sent-by | anchor.bpp | basis:declared | asof:fis12-2.0.3 | grounded-in:fis12-2.0.3:flows/GOLD LOAN/Gold_Loan_Offline_with_igm_1.0.0.yaml#steps[on_issue_resolved_100].owner
anchor.html-form | sent-by | anchor.bpp | basis:declared | asof:fis12-2.0.3 | grounded-in:fis12-2.0.3:flows/PERSONAL LOAN/Personal_Loan_Offline.yaml#steps[personal_loan_information_form].owner
anchor.dynamic-form | sent-by | anchor.bpp | basis:declared | asof:fis12-2.0.3 | grounded-in:fis12-2.0.3:flows/PERSONAL LOAN/Personal_Loan_Offline.yaml#steps[Ekyc_details_verification_status].owner
anchor.unsolicited-callback | isa | anchor.runtime-concept | basis:authority | asof:fis12-2.0.3 | grounded-in:workbench:frames/mock-runner-lib.md
anchor.on-status | isa | anchor.unsolicited-callback | basis:declared | asof:fis12-2.0.3 | grounded-in:fis12-2.0.3:flows/PERSONAL LOAN/Personal_Loan_Offline.yaml#steps[on_status_installment_1].unsolicited
anchor.on-update | isa | anchor.unsolicited-callback | basis:declared | asof:fis12-2.0.3 | grounded-in:fis12-2.0.3:flows/PERSONAL LOAN/Personal_Loan_Foreclosure_Offline.yaml#steps[on_update_foreclosure_unsolicitated].unsolicited
anchor.on-issue-status | isa | anchor.unsolicited-callback | basis:declared | asof:fis12-2.0.3 | grounded-in:fis12-2.0.3:flows/GOLD LOAN/Gold_Loan_Offline_with_igm_1.0.0.yaml#steps[on_issue_resolved_100].unsolicited
anchor.on-status | not-requires | anchor.status | basis:declared | asof:fis12-2.0.3 | grounded-in:fis12-2.0.3:flows/PERSONAL LOAN/Personal_Loan_Offline.yaml#steps[on_status_kyc_verification].responseFor
anchor.on-confirm | precedes | anchor.installment-status-update | basis:declared | asof:fis12-2.0.3 | grounded-in:fis12-2.0.3:flows/PERSONAL LOAN/Personal_Loan_Offline.yaml#steps[on_status_installment_1]
anchor.installment-status-update | isa | anchor.unsolicited-callback | basis:declared | asof:fis12-2.0.3 | grounded-in:fis12-2.0.3:flows/PERSONAL LOAN/Personal_Loan_Offline.yaml#steps[on_status_installment_1].unsolicited
anchor.installment-status-update | scoped-to | anchor.emi-management | basis:declared | asof:fis12-2.0.3 | grounded-in:fis12-2.0.3:flows/PERSONAL LOAN/Personal_Loan_Offline.yaml#steps[on_status_installment_5]
anchor.flow-personal-loan-offline | requires | anchor.html-form | basis:declared | asof:fis12-2.0.3 | grounded-in:fis12-2.0.3:flows/PERSONAL LOAN/Personal_Loan_Offline.yaml#steps[personal_loan_information_form]
anchor.flow-personal-loan-offline | requires | anchor.ekyc-verification | basis:declared | asof:fis12-2.0.3 | grounded-in:fis12-2.0.3:flows/PERSONAL LOAN/Personal_Loan_Offline.yaml#steps[Ekyc_details_verification_status]
anchor.on-select | precedes | anchor.on-status | basis:declared | asof:fis12-2.0.3 | grounded-in:fis12-2.0.3:flows/PERSONAL LOAN/Personal_Loan_Single_Redirection.yaml#steps[on_status_kyc_verification]
anchor.on-status | precedes | anchor.dynamic-form | basis:declared | asof:fis12-2.0.3 | grounded-in:fis12-2.0.3:flows/PERSONAL LOAN/Personal_Loan_Single_Redirection.yaml#steps[Ekyc_details_verification_status]
anchor.dynamic-form | precedes | anchor.status | basis:declared | asof:fis12-2.0.3 | grounded-in:fis12-2.0.3:flows/PERSONAL LOAN/Personal_Loan_Single_Redirection.yaml#steps[status_personal_loan_3]
anchor.flow-personal-loan-single-redirection | requires | anchor.checklist-stop | basis:declared | asof:fis12-2.0.3 | grounded-in:fis12-2.0.3:flows/PERSONAL LOAN/Personal_Loan_Single_Redirection.yaml#steps[on_status_updated_checklists].mock.defaultPayload.message.order.fulfillments[0].stops
anchor.checklist-stop | has-slot | anchor.checklist-codes | basis:declared | asof:fis12-2.0.3 | grounded-in:fis12-2.0.3:flows/PERSONAL LOAN/Personal_Loan_Single_Redirection.yaml#steps[on_status_updated_checklists].mock.defaultPayload.message.order.fulfillments[0].stops[3].type
anchor.checklist-stop | requires | anchor.parent-stop-chain | basis:declared | asof:fis12-2.0.3 | grounded-in:fis12-2.0.3:flows/PERSONAL LOAN/Personal_Loan_Single_Redirection.yaml#steps[on_status_updated_checklists].mock.defaultPayload.message.order.fulfillments[0].stops[3].parent_stop_id
anchor.flow-personal-loan-single-redirection | requires | anchor.fulfillment-type-online | basis:declared | asof:fis12-2.0.3 | grounded-in:fis12-2.0.3:flows/PERSONAL LOAN/Personal_Loan_Single_Redirection.yaml#steps[on_status_updated_checklists].mock.defaultPayload.message.order.fulfillments[0].type
anchor.ekyc-verification | precedes | anchor.bank-account-verification | basis:declared | asof:fis12-2.0.3 | grounded-in:fis12-2.0.3:flows/PERSONAL LOAN/Personal_Loan_Single_Redirection.yaml#steps[on_status_updated_checklists].mock.defaultPayload.message.order.fulfillments[0].stops[4].type
anchor.bank-account-verification | precedes | anchor.repayment-mandate | basis:declared | asof:fis12-2.0.3 | grounded-in:fis12-2.0.3:flows/PERSONAL LOAN/Personal_Loan_Single_Redirection.yaml#steps[on_status_updated_checklists].mock.defaultPayload.message.order.fulfillments[0].stops[5].type
anchor.repayment-mandate | precedes | anchor.loan-agreement | basis:declared | asof:fis12-2.0.3 | grounded-in:fis12-2.0.3:flows/PERSONAL LOAN/Personal_Loan_Single_Redirection.yaml#steps[on_status_updated_checklists].mock.defaultPayload.message.order.fulfillments[0].stops[6].type
anchor.flow-personal-loan-dedupe-check | requires | anchor.fulfillment-type-dedupe | basis:declared | asof:fis12-2.0.3 | grounded-in:fis12-2.0.3:flows/PERSONAL LOAN/Personal_Loan_Dedupe_Check.yaml#steps[select_3_personal_loan_3].mock.defaultPayload.message.order.fulfillments[0].type
anchor.flow-personal-loan-dedupe-check | requires | anchor.pre-qualifier | basis:declared | asof:fis12-2.0.3 | grounded-in:fis12-2.0.3:flows/PERSONAL LOAN/Personal_Loan_Dedupe_Check.yaml#steps[on_select_3_personal_loan_3].mock.defaultPayload.message.order.items[0].descriptor.code
anchor.flow-personal-loan-dedupe-check | requires | anchor.pan-credential | basis:declared | asof:fis12-2.0.3 | grounded-in:fis12-2.0.3:flows/PERSONAL LOAN/Personal_Loan_Dedupe_Check.yaml#steps[select_3_personal_loan_3].mock.defaultPayload.message.order.fulfillments[0].customer.person.creds[0].type
anchor.flow-personal-loan-dedupe-check | not-requires | anchor.html-form | basis:declared | asof:fis12-2.0.3 | grounded-in:fis12-2.0.3:flows/PERSONAL LOAN/Personal_Loan_Dedupe_Check.yaml#steps
anchor.flow-personal-loan-dedupe-check | not-requires | anchor.status | basis:declared | asof:fis12-2.0.3 | grounded-in:fis12-2.0.3:flows/PERSONAL LOAN/Personal_Loan_Dedupe_Check.yaml#steps
anchor.on-confirm | precedes | anchor.update | basis:declared | asof:fis12-2.0.3 | grounded-in:fis12-2.0.3:flows/PERSONAL LOAN/Personal_Loan_Foreclosure_Offline.yaml#steps[update_personal_loan_3]
anchor.on-update | precedes | anchor.dynamic-form | basis:declared | asof:fis12-2.0.3 | grounded-in:fis12-2.0.3:flows/PERSONAL LOAN/Personal_Loan_Foreclosure_Offline.yaml#steps[payment_url_form]
anchor.dynamic-form | precedes | anchor.on-update | basis:declared | asof:fis12-2.0.3 | grounded-in:fis12-2.0.3:flows/PERSONAL LOAN/Personal_Loan_Foreclosure_Offline.yaml#steps[on_update_foreclosure_unsolicitated]
anchor.flow-personal-loan-foreclosure-offline | requires | anchor.payment-time-label-foreclosure | basis:declared | asof:fis12-2.0.3 | grounded-in:fis12-2.0.3:flows/PERSONAL LOAN/Personal_Loan_Foreclosure_Offline.yaml#steps[update_personal_loan_3].mock.defaultPayload.message.order.payments[0].time.label
anchor.flow-personal-loan-missed-emi-offline | requires | anchor.payment-time-label-missed-emi | basis:declared | asof:fis12-2.0.3 | grounded-in:fis12-2.0.3:flows/PERSONAL LOAN/Personal_Loan_Missed_EMI_Offline.yaml#steps[update_personal_loan_3].mock.defaultPayload.message.order.payments[0].time.label
anchor.flow-personal-loan-pre-part-payment-offline | requires | anchor.payment-time-label-pre-part-payment | basis:declared | asof:fis12-2.0.3 | grounded-in:fis12-2.0.3:flows/PERSONAL LOAN/Personal_Loan_Pre_Part_Payment_Offline.yaml#steps[update_personal_loan_3].mock.defaultPayload.message.order.payments[0].time.label
anchor.flow-personal-loan-pre-part-payment-offline | requires | anchor.payment-params-amount | basis:declared | asof:fis12-2.0.3 | grounded-in:fis12-2.0.3:flows/PERSONAL LOAN/Personal_Loan_Pre_Part_Payment_Offline.yaml#steps[update_personal_loan_3].mock.defaultPayload.message.order.payments[0].params.amount
anchor.update | requires | anchor.update-target | basis:declared | asof:fis12-2.0.3 | grounded-in:fis12-2.0.3:flows/PERSONAL LOAN/Personal_Loan_Foreclosure_Offline.yaml#steps[update_personal_loan_3].mock.defaultPayload.message.update_target
anchor.update | requires | anchor.order-id | basis:declared | asof:fis12-2.0.3 | grounded-in:fis12-2.0.3:flows/PERSONAL LOAN/Personal_Loan_Foreclosure_Offline.yaml#steps[update_personal_loan_3].mock.defaultPayload.message.order.id
anchor.payment-url-form | isa | anchor.dynamic-form | basis:declared | asof:fis12-2.0.3 | grounded-in:fis12-2.0.3:flows/PERSONAL LOAN/Personal_Loan_Missed_EMI_Offline.yaml#steps[payment_url_form]
anchor.payment-url-form | causes | anchor.offline-payment-settlement | basis:declared | asof:fis12-2.0.3 | grounded-in:fis12-2.0.3:flows/PERSONAL LOAN/Personal_Loan_Missed_EMI_Offline.yaml#steps[payment_url_form].description
anchor.flow-gold-loan-offline | requires | anchor.gold-collateral-details | basis:declared | asof:fis12-2.0.3 | grounded-in:fis12-2.0.3:flows/GOLD LOAN/Gold_Loan_Offline.yaml#steps[gold_loan_information_form].description
anchor.flow-gold-loan-offline | requires | anchor.item-code-gold-loan | basis:declared | asof:fis12-2.0.3 | grounded-in:fis12-2.0.3:flows/GOLD LOAN/Gold_Loan_Offline.yaml#steps[on_search_gold_loan_3].mock.defaultPayload.message.catalog.providers[0].items[0].descriptor.code
anchor.flow-gold-loan-offline | requires | anchor.xinput-form-response | basis:declared | asof:fis12-2.0.3 | grounded-in:fis12-2.0.3:flows/GOLD LOAN/Gold_Loan_Offline.yaml#steps[select_1].mock.defaultPayload.message.order.items[0].xinput.form_response
anchor.status | requires | anchor.ref-id | basis:declared | asof:fis12-2.0.3 | grounded-in:fis12-2.0.3:flows/PERSONAL LOAN/Personal_Loan_Single_Redirection.yaml#steps[status_personal_loan_3].mock.defaultPayload.message.ref_id
anchor.search | requires | anchor.bap-terms | basis:declared | asof:fis12-2.0.3 | grounded-in:fis12-2.0.3:flows/PERSONAL LOAN/Personal_Loan_Dedupe_Check.yaml#steps[search_personal_loan_3].mock.defaultPayload.message.intent.tags[0].descriptor.code
anchor.confirm | requires | anchor.bpp-terms | basis:declared | asof:fis12-2.0.3 | grounded-in:fis12-2.0.3:flows/PERSONAL LOAN/Personal_Loan_Dedupe_Check.yaml#steps[confirm_personal_loan_3].mock.defaultPayload.message.order.tags[1].descriptor.code
anchor.bap-terms | has-slot | anchor.offline-contract | basis:declared | asof:fis12-2.0.3 | !untethered
anchor.offline-contract | constrains | anchor.offline-underwriting | basis:derived | asof:fis12-2.0.3 | grounded-in:anchor.bap-terms
anchor.contact-info-tag | has-slot | anchor.gro-details | basis:declared | asof:fis12-2.0.3 | !untethered
anchor.gro-details | isa | anchor.grievance-redressal-contact | basis:authority | asof:fis12-2.0.3 | grounded-in:workbench:frames/ondc-ecosystem.md
anchor.context-required-block | isa | anchor.validation-rule | basis:declared | asof:fis12-2.0.3 | grounded-in:fis12-2.0.3:validations/index.yaml#_TESTS_.search[SEARCH_CONTEXT]._RETURN_
anchor.collected-by-enum | isa | anchor.enum-set | basis:declared | asof:fis12-2.0.3 | grounded-in:fis12-2.0.3:validations/index.yaml#_TESTS_.search[SEARCH_PAYMENT]._RETURN_[VALID_PAYMENT_COLLECTED_BY_ENUM].enumList
anchor.payment-tag-groups | isa | anchor.tag-group | basis:declared | asof:fis12-2.0.3 | grounded-in:fis12-2.0.3:validations/index.yaml#_TESTS_.search[ANCHOR_DEFINITIONS].validTags_a3
anchor.buyer-finder-fees-fields | isa | anchor.enum-set | basis:declared | asof:fis12-2.0.3 | grounded-in:fis12-2.0.3:validations/index.yaml#_TESTS_.search[ANCHOR_DEFINITIONS].validValues_a4
anchor.settlement-terms-tag | isa | anchor.tag-group | basis:declared | asof:fis12-2.0.3 | grounded-in:fis12-2.0.3:validations/index.yaml#_TESTS_.search[ANCHOR_DEFINITIONS].validTags_a5
anchor.contact-info-tag | isa | anchor.tag-group | basis:declared | asof:fis12-2.0.3 | grounded-in:fis12-2.0.3:validations/index.yaml#_TESTS_.on_search[ON_SEARCH_PROVIDER_CONTACT_INFO]._RETURN_[REQUIRED_CONTACT_INFO_TAG_GROUP].validTags
anchor.lsp-info-tag | isa | anchor.tag-group | basis:declared | asof:fis12-2.0.3 | grounded-in:fis12-2.0.3:validations/index.yaml#_TESTS_.on_search[ON_SEARCH_PROVIDER_LSP_INFO]._RETURN_[REQUIRED_LSP_INFO_TAG_GROUP].validTags
anchor.lsp-info-fields | isa | anchor.enum-set | basis:declared | asof:fis12-2.0.3 | grounded-in:fis12-2.0.3:validations/index.yaml#_TESTS_.on_search[ON_SEARCH_PROVIDER_LSP_INFO]._RETURN_[REQUIRED_LSP_INFO_LIST].validValues
anchor.currency-inr | isa | anchor.enum-set | basis:declared | asof:fis12-2.0.3 | grounded-in:fis12-2.0.3:validations/index.yaml#_TESTS_.on_select[ON_SELECT_2_OFFER_ITEMS_PRICE]._RETURN_[REQUIRED_ITEM_PRICE_CURRENCY].enumList
anchor.item-code-gold-loan | isa | anchor.enum-set | basis:declared | asof:fis12-2.0.3 | grounded-in:fis12-2.0.3:validations/index.yaml#_TESTS_.on_select[ON_SELECT_PROVIDER_LOCATIONS_GOLD].loan_type_match
anchor.item-code-personal-loan | isa | anchor.enum-set | basis:declared | asof:fis12-2.0.3 | grounded-in:fis12-2.0.3:validations/index.yaml#_TESTS_.select[SELECT_XINPUT_PERSONAL_LOAN].loan_type_match
anchor.item-descriptor-codes | isa | anchor.enum-set | basis:declared | asof:fis12-2.0.3 | grounded-in:fis12-2.0.3:validations/index.yaml#_TESTS_.on_select[ON_SELECT_ITEMS_BASIC]._RETURN_[VALID_ITEM_DESCRIPTOR_CODE_ENUM].enumList
anchor.offer-tag-groups | isa | anchor.tag-group | basis:declared | asof:fis12-2.0.3 | grounded-in:fis12-2.0.3:validations/index.yaml#_TESTS_.on_select[ON_SELECT_2_OFFER_LOAN_INFO]._RETURN_[REQUIRED_LOAN_INFO_TAG_GROUP].validTags
anchor.quote-breakup-titles-origination | isa | anchor.enum-set | basis:declared | asof:fis12-2.0.3 | grounded-in:fis12-2.0.3:validations/index.yaml#_TESTS_.on_select[ON_SELECT_2_OFFER_QUOTE]._RETURN_[REQUIRED_QUOTE_BREAKUP]._RETURN_[VALID_QUOTE_BREAKUP_TITLE_ENUM].enumList
anchor.fulfillment-types | isa | anchor.enum-set | basis:declared | asof:fis12-2.0.3 | grounded-in:fis12-2.0.3:validations/index.yaml#_TESTS_.on_init[ON_INIT_FULFILLMENTS]._RETURN_[REQUIRED_FULFILLMENT_TYPE].enumList
anchor.payment-types | isa | anchor.enum-set | basis:declared | asof:fis12-2.0.3 | grounded-in:fis12-2.0.3:validations/index.yaml#_TESTS_.on_init[ON_INIT_PAYMENTS]._RETURN_[VALID_PAYMENT_TYPE_ENUM].enumList
anchor.fulfillment-state-codes | isa | anchor.enum-set | basis:declared | asof:fis12-2.0.3 | grounded-in:fis12-2.0.3:validations/index.yaml#_TESTS_.update[UPDATE_FULFILLMENT_TARGET]._RETURN_[If_Validation_Result_is_REJECTED_flow_cant_move_forward].enumList
anchor.payment-status-codes | isa | anchor.enum-set | basis:declared | asof:fis12-2.0.3 | grounded-in:fis12-2.0.3:validations/index.yaml#_TESTS_.on_update[ON_UPDATE_PAYMENTS]._RETURN_[VALID_PAYMENT_STATUS_ENUM].enumList
anchor.quote-breakup-titles-servicing | isa | anchor.enum-set | basis:declared | asof:fis12-2.0.3 | grounded-in:fis12-2.0.3:validations/index.yaml#_TESTS_.on_update[ON_UPDATE_QUOTE]._RETURN_[VALID_QUOTE_BREAKUP_TITLE_ON_UPDATE_ENUM].enumList
anchor.required-order-created-at | isa | anchor.validation-rule | basis:declared | asof:fis12-2.0.3 | grounded-in:fis12-2.0.3:validations/index.yaml#_TESTS_.on_confirm[REQUIRED_ORDER_CREATED_AT]
anchor.required-order-updated-at | isa | anchor.validation-rule | basis:declared | asof:fis12-2.0.3 | grounded-in:fis12-2.0.3:validations/index.yaml#_TESTS_.on_confirm[REQUIRED_ORDER_UPDATED_AT]
anchor.required-order-id | isa | anchor.validation-rule | basis:declared | asof:fis12-2.0.3 | grounded-in:fis12-2.0.3:validations/index.yaml#_TESTS_.on_confirm[REQUIRED_ORDER_ID]
anchor.required-order-status | isa | anchor.validation-rule | basis:declared | asof:fis12-2.0.3 | grounded-in:fis12-2.0.3:validations/index.yaml#_TESTS_.on_confirm[REQUIRED_ORDER_STATUS]
anchor.quote-breakup-titles-servicing | wasDerivedFrom | anchor.quote-breakup-titles-origination | basis:derived | asof:fis12-2.0.3 | grounded-in:anchor.quote-breakup-titles-origination
anchor.context-required-block | scoped-to | anchor.on-search | basis:declared | asof:fis12-2.0.3 | grounded-in:fis12-2.0.3:validations/index.yaml#_TESTS_.on_search[ON_SEARCH_CONTEXT]._RETURN_
anchor.context-required-block | scoped-to | anchor.select | basis:declared | asof:fis12-2.0.3 | grounded-in:fis12-2.0.3:validations/index.yaml#_TESTS_.select[SELECT_CONTEXT]._RETURN_
anchor.context-required-block | scoped-to | anchor.on-select | basis:declared | asof:fis12-2.0.3 | grounded-in:fis12-2.0.3:validations/index.yaml#_TESTS_.on_select[ON_SELECT_CONTEXT]._RETURN_
anchor.context-required-block | scoped-to | anchor.init | basis:declared | asof:fis12-2.0.3 | grounded-in:fis12-2.0.3:validations/index.yaml#_TESTS_.init[INIT_CONTEXT]._RETURN_
anchor.context-required-block | scoped-to | anchor.on-init | basis:declared | asof:fis12-2.0.3 | grounded-in:fis12-2.0.3:validations/index.yaml#_TESTS_.on_init[ON_INIT_CONTEXT]._RETURN_
anchor.context-required-block | scoped-to | anchor.confirm | basis:declared | asof:fis12-2.0.3 | grounded-in:fis12-2.0.3:validations/index.yaml#_TESTS_.confirm[CONFIRM_CONTEXT]._RETURN_
anchor.context-required-block | scoped-to | anchor.on-confirm | basis:declared | asof:fis12-2.0.3 | grounded-in:fis12-2.0.3:validations/index.yaml#_TESTS_.on_confirm[ON_CONFIRM_CONTEXT]._RETURN_
anchor.context-required-block | scoped-to | anchor.update | basis:declared | asof:fis12-2.0.3 | grounded-in:fis12-2.0.3:validations/index.yaml#_TESTS_.update[UPDATE_CONTEXT]._RETURN_
anchor.context-required-block | scoped-to | anchor.on-update | basis:declared | asof:fis12-2.0.3 | grounded-in:fis12-2.0.3:validations/index.yaml#_TESTS_.on_update[ON_UPDATE_CONTEXT]._RETURN_
anchor.context-required-block | scoped-to | anchor.status | basis:declared | asof:fis12-2.0.3 | grounded-in:fis12-2.0.3:validations/index.yaml#_TESTS_.status[STATUS_CONTEXT]._RETURN_
anchor.context-required-block | scoped-to | anchor.on-status | basis:declared | asof:fis12-2.0.3 | grounded-in:fis12-2.0.3:validations/index.yaml#_TESTS_.on_status[ON_STATUS_CONTEXT]._RETURN_
anchor.context-required-block | not-scoped-to | anchor.issue | basis:declared | asof:fis12-2.0.3 | grounded-in:fis12-2.0.3:validations/index.yaml#_TESTS_.issue[REQUIRED_CONTEXT_FIELDS]
anchor.collected-by-enum | scoped-to | anchor.on-confirm | basis:declared | asof:fis12-2.0.3 | grounded-in:fis12-2.0.3:validations/index.yaml#_TESTS_.on_confirm[ON_CONFIRM_PAYMENTS_COLLECTED_BY]._RETURN_[REQUIRED_PAYMENT_COLLECTED_BY].enumList
anchor.payment-tag-groups | scoped-to | anchor.on-init | basis:declared | asof:fis12-2.0.3 | grounded-in:fis12-2.0.3:validations/index.yaml#_TESTS_.on_init[ON_INIT_PAYMENTS_ON_ORDER]._RETURN_[REQUIRED_PAYMENT_TAGS]._RETURN_[REQUIRED_BUYER_FINDER_FEES_TAG].validTags
anchor.settlement-terms-tag | scoped-to | anchor.on-init | basis:declared | asof:fis12-2.0.3 | grounded-in:fis12-2.0.3:validations/index.yaml#_TESTS_.on_init[ON_INIT_PAYMENTS_ON_ORDER]._RETURN_[REQUIRED_PAYMENT_TAGS]._RETURN_[REQUIRED_SETTLEMENT_TERMS_TAG].validTags
anchor.contact-info-tag | scoped-to | anchor.on-select | basis:declared | asof:fis12-2.0.3 | grounded-in:fis12-2.0.3:validations/index.yaml#_TESTS_.on_select[ON_SELECT_PROVIDER_TAGS]._RETURN_[REQUIRED_CONTACT_INFO_TAG_GROUP].validTags
anchor.lsp-info-tag | scoped-to | anchor.on-select | basis:declared | asof:fis12-2.0.3 | grounded-in:fis12-2.0.3:validations/index.yaml#_TESTS_.on_select[ON_SELECT_PROVIDER_TAGS]._RETURN_[REQUIRED_LSP_INFO_TAG_GROUP].validTags
anchor.currency-inr | scoped-to | anchor.quote-breakup-titles-origination | basis:declared | asof:fis12-2.0.3 | grounded-in:fis12-2.0.3:validations/index.yaml#_TESTS_.on_select[ON_SELECT_2_OFFER_QUOTE]._RETURN_[REQUIRED_QUOTE_BREAKUP]._RETURN_[REQUIRED_QUOTE_BREAKUP_PRICE_CURRENCY].enumList
anchor.item-code-personal-loan | scoped-to | anchor.on-select | basis:declared | asof:fis12-2.0.3 | grounded-in:fis12-2.0.3:validations/index.yaml#_TESTS_.on_select[ON_SELECT_2_OFFER_XINPUT_PERSONAL_LOAN].loan_type_match
anchor.item-code-personal-loan | scoped-to | anchor.init | basis:declared | asof:fis12-2.0.3 | grounded-in:fis12-2.0.3:validations/index.yaml#_TESTS_.init[INIT_XINPUT_PERSONAL_LOAN].loan_type_match
anchor.item-code-personal-loan | scoped-to | anchor.on-init | basis:declared | asof:fis12-2.0.3 | grounded-in:fis12-2.0.3:validations/index.yaml#_TESTS_.on_init[ON_INIT_XINPUT_PERSONAL_LOAN].loan_type_match
anchor.item-code-gold-loan | scoped-to | anchor.update | basis:declared | asof:fis12-2.0.3 | grounded-in:fis12-2.0.3:validations/index.yaml#_TESTS_.update[UPDATE_PAYMENT_REF_ID_GOLD].loan_type_match
anchor.item-code-gold-loan | scoped-to | anchor.on-select | basis:declared | asof:fis12-2.0.3 | grounded-in:fis12-2.0.3:validations/index.yaml#_TESTS_.on_select[ON_SELECT_2_OFFER_FULFILLMENT_GOLD].loan_type_match
anchor.item-descriptor-codes | scoped-to | anchor.on-init | basis:declared | asof:fis12-2.0.3 | grounded-in:fis12-2.0.3:validations/index.yaml#_TESTS_.on_init[ON_INIT_ITEMS]._RETURN_[REQUIRED_ITEM_DESCRIPTOR_CODE].enumList
anchor.item-descriptor-codes | scoped-to | anchor.on-confirm | basis:declared | asof:fis12-2.0.3 | grounded-in:fis12-2.0.3:validations/index.yaml#_TESTS_.on_confirm[ON_CONFIRM_ITEMS]._RETURN_[REQUIRED_ITEM_DESCRIPTOR_CODE].enumList
anchor.offer-tag-groups | scoped-to | anchor.on-init | basis:declared | asof:fis12-2.0.3 | grounded-in:fis12-2.0.3:validations/index.yaml#_TESTS_.on_init[ON_INIT_ITEMS]._RETURN_[REQUIRED_LOAN_INFO_TAG_GROUP].validTags
anchor.offer-tag-groups | scoped-to | anchor.on-confirm | basis:declared | asof:fis12-2.0.3 | grounded-in:fis12-2.0.3:validations/index.yaml#_TESTS_.on_confirm[ON_CONFIRM_ITEMS]._RETURN_[REQUIRED_LOAN_INFO_TAG].validTags
anchor.quote-breakup-titles-origination | scoped-to | anchor.on-init | basis:declared | asof:fis12-2.0.3 | grounded-in:fis12-2.0.3:validations/index.yaml#_TESTS_.on_init[ON_INIT_QUOTE]._RETURN_[REQUIRED_QUOTE_BREAKUP].enumList
anchor.quote-breakup-titles-origination | scoped-to | anchor.on-confirm | basis:declared | asof:fis12-2.0.3 | grounded-in:fis12-2.0.3:validations/index.yaml#_TESTS_.on_confirm[ON_CONFIRM_QUOTE]._RETURN_[REQUIRED_QUOTE_BREAKUP].enumList
anchor.payment-types | scoped-to | anchor.on-confirm | basis:declared | asof:fis12-2.0.3 | grounded-in:fis12-2.0.3:validations/index.yaml#_TESTS_.on_confirm[ON_CONFIRM_PAYMENTS]._RETURN_[REQUIRED_PAYMENT_TYPE].enumList
anchor.fulfillment-types | scoped-to | anchor.on-select | basis:declared | asof:fis12-2.0.3 | grounded-in:fis12-2.0.3:validations/index.yaml#_TESTS_.on_select[ON_SELECT_2_OFFER_FULFILLMENT_GOLD]._RETURN_[REQUIRED_FULFILLMENT_TYPE].enumList
anchor.fulfillment-types | scoped-to | anchor.on-confirm | basis:declared | asof:fis12-2.0.3 | grounded-in:fis12-2.0.3:validations/index.yaml#_TESTS_.on_confirm[ON_CONFIRM_FULFILLMENTS]._RETURN_[REQUIRED_FULFILLMENT_TYPE].enumList
anchor.fulfillment-types | scoped-to | anchor.on-status | basis:declared | asof:fis12-2.0.3 | grounded-in:fis12-2.0.3:validations/index.yaml#_TESTS_.on_status[ON_STATUS_FULFILLMENTS]._RETURN_[REQUIRED_FULFILLMENT_TYPE].enumList
anchor.fulfillment-state-codes | scoped-to | anchor.on-status | basis:declared | asof:fis12-2.0.3 | grounded-in:fis12-2.0.3:validations/index.yaml#_TESTS_.on_status[ON_STATUS_FULFILLMENT_STATE]._RETURN_[VALID_FULFILLMENT_STATE_CODE].enumList
anchor.payment-status-codes | scoped-to | anchor.on-status | basis:declared | asof:fis12-2.0.3 | grounded-in:fis12-2.0.3:validations/index.yaml#_TESTS_.on_status[ON_STATUS_PAYMENTS]._RETURN_[REQUIRED_PAYMENT_STATUS].enumList
anchor.quote-breakup-titles-servicing | scoped-to | anchor.on-status | basis:declared | asof:fis12-2.0.3 | grounded-in:fis12-2.0.3:validations/index.yaml#_TESTS_.on_status[ON_STATUS_QUOTE].enumList
anchor.required-order-created-at | scoped-to | anchor.on-update | basis:declared | asof:fis12-2.0.3 | grounded-in:fis12-2.0.3:validations/index.yaml#_TESTS_.on_update[REQUIRED_ORDER_CREATED_AT]
anchor.required-order-updated-at | scoped-to | anchor.on-update | basis:declared | asof:fis12-2.0.3 | grounded-in:fis12-2.0.3:validations/index.yaml#_TESTS_.on_update[REQUIRED_ORDER_UPDATED_AT]
anchor.required-order-status | scoped-to | anchor.on-update | basis:declared | asof:fis12-2.0.3 | grounded-in:fis12-2.0.3:validations/index.yaml#_TESTS_.on_update[REQUIRED_ORDER_STATUS]
anchor.required-order-id | not-scoped-to | anchor.on-update | basis:declared | asof:fis12-2.0.3 | grounded-in:fis12-2.0.3:validations/index.yaml#_TESTS_.on_update
anchor.search-category-codes | isa | anchor.enum-set | basis:declared | asof:fis12-2.0.3 | grounded-in:fis12-2.0.3:validations/index.yaml#_TESTS_.search[SEARCH_CATEGORY_CODE]._RETURN_[VALID_ENUM_CATEGORY_CODE].enumList
anchor.search | requires | anchor.search-category-codes | basis:declared | asof:fis12-2.0.3 | grounded-in:fis12-2.0.3:validations/index.yaml#_TESTS_.search[SEARCH_CATEGORY_CODE]._RETURN_[REQUIRED_CATEGORY_CODE]
anchor.personal-loan | isa | anchor.search-category-codes | basis:declared | asof:fis12-2.0.3 | grounded-in:fis12-2.0.3:validations/index.yaml#_TESTS_.search[SEARCH_CATEGORY_CODE]._RETURN_[VALID_ENUM_CATEGORY_CODE].enumList
anchor.gold-loan | isa | anchor.search-category-codes | basis:declared | asof:fis12-2.0.3 | grounded-in:fis12-2.0.3:validations/index.yaml#_TESTS_.search[SEARCH_CATEGORY_CODE]._RETURN_[VALID_ENUM_CATEGORY_CODE].enumList
anchor.credit-card | isa | anchor.search-category-codes | basis:declared | asof:fis12-2.0.3 | grounded-in:fis12-2.0.3:validations/index.yaml#_TESTS_.search[SEARCH_CATEGORY_CODE]._RETURN_[VALID_ENUM_CATEGORY_CODE].enumList
anchor.credit-card | isa | anchor.credit-product | basis:derived | asof:fis12-2.0.3 | grounded-in:anchor.search-category-codes
anchor.search | requires | anchor.collected-by-enum | basis:declared | asof:fis12-2.0.3 | grounded-in:fis12-2.0.3:validations/index.yaml#_TESTS_.search[SEARCH_PAYMENT]._RETURN_[REQUIRED_PAYMENT_COLLECTED_BY]
anchor.collected-by-enum | scoped-to | anchor.item-code-personal-loan | basis:declared | asof:fis12-2.0.3 | grounded-in:fis12-2.0.3:validations/index.yaml#_TESTS_.search[SEARCH_PAYMENT].loan_type_match
anchor.catalog-category-codes | isa | anchor.enum-set | basis:declared | asof:fis12-2.0.3 | grounded-in:fis12-2.0.3:validations/index.yaml#_TESTS_.on_search[ON_SEARCH_CATEGORIES_PL]._RETURN_[VALID_ENUM_CATEGORIES_CODE].enumList
anchor.catalog-category-codes | requires | anchor.parent-category-id | basis:declared | asof:fis12-2.0.3 | grounded-in:fis12-2.0.3:validations/index.yaml#_TESTS_.on_search[ON_SEARCH_CATEGORIES_PL]._RETURN_[REQUIRED_CATEGORIES_PARENT_ID]
anchor.bureau-loan | isa | anchor.catalog-category-codes | basis:declared | asof:fis12-2.0.3 | grounded-in:fis12-2.0.3:validations/index.yaml#_TESTS_.on_search[ON_SEARCH_CATEGORIES_PL]._RETURN_[VALID_ENUM_CATEGORIES_CODE].enumList
anchor.aa-personal-loan | isa | anchor.catalog-category-codes | basis:declared | asof:fis12-2.0.3 | grounded-in:fis12-2.0.3:validations/index.yaml#_TESTS_.on_search[ON_SEARCH_CATEGORIES_PL]._RETURN_[VALID_ENUM_CATEGORIES_CODE].enumList
anchor.pre-qualifier | isa | anchor.catalog-category-codes | basis:declared | asof:fis12-2.0.3 | grounded-in:fis12-2.0.3:validations/index.yaml#_TESTS_.on_search[ON_SEARCH_CATEGORIES_PL]._RETURN_[VALID_ENUM_CATEGORIES_CODE].enumList
anchor.general-info-tag | isa | anchor.tag-group | basis:declared | asof:fis12-2.0.3 | grounded-in:fis12-2.0.3:validations/index.yaml#_TESTS_.on_search[ON_SEARCH_ITEMS_PL]._RETURN_[REQUIRED_GENERAL_INFO_TAG_GROUP].validTags
anchor.general-info-fields | isa | anchor.enum-set | basis:declared | asof:fis12-2.0.3 | grounded-in:fis12-2.0.3:validations/index.yaml#_TESTS_.on_search[ON_SEARCH_ITEMS_PL]._RETURN_[REQUIRED_GENERAL_INFO_LIST].validValues
anchor.general-info-fields | scoped-to | anchor.general-info-tag | basis:declared | asof:fis12-2.0.3 | grounded-in:fis12-2.0.3:validations/index.yaml#_TESTS_.on_search[ON_SEARCH_ITEMS_PL]._RETURN_[REQUIRED_GENERAL_INFO_LIST]._SCOPE_
anchor.general-info-fields | constrains | anchor.offer-comparison | basis:declared | asof:fis12-2.0.3 | grounded-in:fis12-2.0.3:validations/index.yaml#_TESTS_.on_search[ON_SEARCH_ITEMS_PL]._RETURN_[REQUIRED_GENERAL_INFO_LIST].validValues
anchor.on-search | requires | anchor.xinput | basis:declared | asof:fis12-2.0.3 | grounded-in:fis12-2.0.3:validations/index.yaml#_TESTS_.on_search[ON_SEARCH_ITEMS_PL]._RETURN_[REQUIRED_XINPUT]
anchor.xinput | has-slot | anchor.xinput-form-url | basis:declared | asof:fis12-2.0.3 | grounded-in:fis12-2.0.3:validations/index.yaml#_TESTS_.on_search[ON_SEARCH_ITEMS_PL]._RETURN_[REQUIRED_XINPUT_FORM_URL]
anchor.xinput | has-slot | anchor.xinput-headings | basis:declared | asof:fis12-2.0.3 | grounded-in:fis12-2.0.3:validations/index.yaml#_TESTS_.on_search[ON_SEARCH_ITEMS_PL]._RETURN_[VALID_XINPUT_HEADINGS_ENUM].enumList
anchor.xinput-headings | isa | anchor.enum-set | basis:declared | asof:fis12-2.0.3 | grounded-in:fis12-2.0.3:validations/index.yaml#_TESTS_.on_search[ON_SEARCH_ITEMS_PL]._RETURN_[VALID_XINPUT_HEADINGS_ENUM].enumList
anchor.xinput | has-slot | anchor.xinput-head-index | basis:declared | asof:fis12-2.0.3 | grounded-in:fis12-2.0.3:validations/index.yaml#_TESTS_.select[SELECT_XINPUT_PERSONAL_LOAN]._RETURN_[REQUIRED_XINPUT_HEAD_INDEX]
anchor.xinput-head-index | constrains | anchor.multi-step-form-progression | basis:declared | asof:fis12-2.0.3 | grounded-in:fis12-2.0.3:docs/xinput-form-response.md#seller-side-form
anchor.xinput | has-slot | anchor.xinput-form-response | basis:declared | asof:fis12-2.0.3 | grounded-in:fis12-2.0.3:validations/index.yaml#_TESTS_.on_select[ON_SELECT_1_AA_CONSENT_XINPUT]._RETURN_[REQUIRED_XINPUT_FORM_RESPONSE]
anchor.xinput-form-response | has-slot | anchor.form-submission-id | basis:declared | asof:fis12-2.0.3 | grounded-in:fis12-2.0.3:validations/index.yaml#_TESTS_.on_select[ON_SELECT_1_AA_CONSENT_XINPUT]._RETURN_[REQUIRED_XINPUT_FORM_RESPONSE_SUBMISSION_ID]
anchor.xinput-form-response-status | isa | anchor.enum-set | basis:declared | asof:fis12-2.0.3 | grounded-in:fis12-2.0.3:validations/index.yaml#_TESTS_.on_select[ON_SELECT_1_AA_CONSENT_XINPUT]._RETURN_[VALID_XINPUT_FORM_RESPONSE_STATUS].enumList
anchor.xinput-form-response | has-slot | anchor.xinput-form-response-status | basis:declared | asof:fis12-2.0.3 | grounded-in:fis12-2.0.3:validations/index.yaml#_TESTS_.on_select[ON_SELECT_1_AA_CONSENT_XINPUT]._RETURN_[REQUIRED_XINPUT_FORM_RESPONSE]
anchor.xinput-form-response-status | scoped-to | anchor.on-status | basis:declared | asof:fis12-2.0.3 | grounded-in:fis12-2.0.3:validations/index.yaml#_TESTS_.on_status[ON_STATUS_XINPUT_FORM_RESPONSE_STATUS_NOT_REJECTED]._RETURN_[If_Validation_Result_is_REJECTED_flow_cant_move_forward].enumList
anchor.form-rejected | causes | anchor.flow-halt | basis:declared | asof:fis12-2.0.3 | grounded-in:fis12-2.0.3:validations/index.yaml#_TESTS_.on_status[ON_STATUS_XINPUT_FORM_RESPONSE_STATUS_NOT_REJECTED]._RETURN_[If_Validation_Result_is_REJECTED_flow_cant_move_forward]
anchor.fulfillment-state-rejected | causes | anchor.flow-halt | basis:declared | asof:fis12-2.0.3 | grounded-in:fis12-2.0.3:validations/index.yaml#_TESTS_.update[UPDATE_FULFILLMENT_TARGET]._RETURN_[If_Validation_Result_is_REJECTED_flow_cant_move_forward]
anchor.form-submission-id | wasGeneratedBy | anchor.html-form | basis:declared | asof:fis12-2.0.3 | grounded-in:fis12-2.0.3:docs/xinput-form-response.md#form-response
anchor.xinput-form-response | wasInformedBy | anchor.bap-callback-redirect | basis:declared | asof:fis12-2.0.3 | grounded-in:fis12-2.0.3:docs/xinput-form-response.md#form-response
anchor.bap-callback-redirect | precedes | anchor.on-status | basis:declared | asof:fis12-2.0.3 | grounded-in:fis12-2.0.3:docs/xinput-form-response.md#form-response
anchor.single-redirection | requires | anchor.bap-callback-redirect | basis:declared | asof:fis12-2.0.3 | grounded-in:fis12-2.0.3:docs/xinput-form-response.md#form-response
anchor.consent-info-tag | isa | anchor.tag-group | basis:declared | asof:fis12-2.0.3 | grounded-in:fis12-2.0.3:validations/index.yaml#_TESTS_.on_select[ON_SELECT_1_AA_CONSENT_ITEMS]._RETURN_[REQUIRED_CONSENT_INFO_TAG].validTags
anchor.consent-handler | scoped-to | anchor.consent-info-tag | basis:declared | asof:fis12-2.0.3 | grounded-in:fis12-2.0.3:validations/index.yaml#_TESTS_.on_select[ON_SELECT_1_AA_CONSENT_ITEMS]._RETURN_[REQUIRED_CONSENT_HANDLER].validValues
anchor.consent-handler | requires | anchor.account-aggregator | basis:authority | asof:fis12-2.0.3 | grounded-in:fis12-2.0.3:docs/overview.md#key-concepts
anchor.loan-info-tag | isa | anchor.tag-group | basis:declared | asof:fis12-2.0.3 | grounded-in:fis12-2.0.3:validations/index.yaml#_TESTS_.on_select[ON_SELECT_2_OFFER_LOAN_INFO]._RETURN_[REQUIRED_LOAN_INFO_LIST_COMMON]._SCOPE_
anchor.loan-info-fields | isa | anchor.enum-set | basis:declared | asof:fis12-2.0.3 | grounded-in:fis12-2.0.3:validations/index.yaml#_TESTS_.on_select[ON_SELECT_2_OFFER_LOAN_INFO]._RETURN_[REQUIRED_LOAN_INFO_LIST_COMMON].validValues
anchor.loan-info-fields | scoped-to | anchor.loan-info-tag | basis:declared | asof:fis12-2.0.3 | grounded-in:fis12-2.0.3:validations/index.yaml#_TESTS_.on_select[ON_SELECT_2_OFFER_LOAN_INFO]._RETURN_[REQUIRED_LOAN_INFO_LIST_COMMON]._SCOPE_
anchor.ltv-ratio | scoped-to | anchor.item-code-gold-loan | basis:declared | asof:fis12-2.0.3 | grounded-in:fis12-2.0.3:validations/index.yaml#_TESTS_.on_select[ON_SELECT_2_OFFER_LOAN_INFO]._RETURN_[REQUIRED_LOAN_INFO_LTV_RATIO_GOLD].validValues
anchor.ltv-ratio | not-scoped-to | anchor.item-code-personal-loan | basis:declared | asof:fis12-2.0.3 | grounded-in:fis12-2.0.3:validations/index.yaml#_TESTS_.on_select[ON_SELECT_2_OFFER_LOAN_INFO]._RETURN_[REQUIRED_LOAN_INFO_LTV_RATIO_GOLD]._SCOPE_
anchor.provider-location | scoped-to | anchor.item-code-gold-loan | basis:declared | asof:fis12-2.0.3 | grounded-in:fis12-2.0.3:validations/index.yaml#_TESTS_.on_select[ON_SELECT_PROVIDER_LOCATIONS_GOLD]._RETURN_[REQUIRED_PROVIDER_LOCATIONS]
anchor.provider-location | requires | anchor.gps-coordinate | basis:declared | asof:fis12-2.0.3 | grounded-in:fis12-2.0.3:validations/index.yaml#_TESTS_.on_select[ON_SELECT_PROVIDER_LOCATIONS_GOLD]._RETURN_[REQUIRED_PROVIDER_LOCATION_GPS]
anchor.fulfillment-agent | scoped-to | anchor.item-code-gold-loan | basis:declared | asof:fis12-2.0.3 | grounded-in:fis12-2.0.3:validations/index.yaml#_TESTS_.on_select[ON_SELECT_2_OFFER_FULFILLMENT_GOLD]._RETURN_[REQUIRED_FULFILLMENT_AGENT_NAME]
anchor.quote | requires | anchor.quote-ttl | basis:declared | asof:fis12-2.0.3 | grounded-in:fis12-2.0.3:validations/index.yaml#_TESTS_.on_select[ON_SELECT_2_OFFER_QUOTE]._RETURN_[REQUIRED_QUOTE_TTL]
anchor.quote | has-slot | anchor.quote-breakup-titles-origination | basis:declared | asof:fis12-2.0.3 | grounded-in:fis12-2.0.3:validations/index.yaml#_TESTS_.on_select[ON_SELECT_2_OFFER_QUOTE]._RETURN_[REQUIRED_QUOTE_BREAKUP]
anchor.on-init | requires | anchor.payment-collected-by | basis:declared | asof:fis12-2.0.3 | grounded-in:fis12-2.0.3:validations/index.yaml#_TESTS_.on_init[ON_INIT_PAYMENTS_ON_ORDER]._RETURN_[REQUIRED_PAYMENT_COLLECTED_BY]
anchor.payment-type-on-order | requires | anchor.payment-tag-groups | basis:declared | asof:fis12-2.0.3 | grounded-in:fis12-2.0.3:validations/index.yaml#_TESTS_.on_init[ON_INIT_PAYMENTS_ON_ORDER]._SCOPE_
anchor.on-confirm | requires | anchor.loan-agreement-document | basis:declared | asof:fis12-2.0.3 | grounded-in:fis12-2.0.3:validations/index.yaml#_TESTS_.on_confirm[ON_CONFIRM_DOCUMENTS]._RETURN_[REQUIRED_DOCUMENT_URL]
anchor.document-mime-types | isa | anchor.enum-set | basis:declared | asof:fis12-2.0.3 | grounded-in:fis12-2.0.3:validations/index.yaml#_TESTS_.on_confirm[ON_CONFIRM_DOCUMENTS]._RETURN_[REQUIRED_DOCUMENT_MIME_TYPE].enumList
anchor.loan-agreement-document | scoped-to | anchor.item-code-personal-loan | basis:declared | asof:fis12-2.0.3 | grounded-in:fis12-2.0.3:validations/index.yaml#_TESTS_.on_confirm[ON_CONFIRM_DOCUMENTS]._SCOPE_
anchor.cancellation-term-states | isa | anchor.enum-set | basis:declared | asof:fis12-2.0.3 | grounded-in:fis12-2.0.3:validations/index.yaml#_TESTS_.on_confirm[ON_CONFIRM_CANCELLATION_TERMS].enumList
anchor.cancellation-term-states | constrains | anchor.foreclosure | basis:declared | asof:fis12-2.0.3 | grounded-in:fis12-2.0.3:validations/index.yaml#_TESTS_.on_confirm[ON_CONFIRM_CANCELLATION_TERMS]
anchor.payment-time-labels | isa | anchor.enum-set | basis:declared | asof:fis12-2.0.3 | grounded-in:fis12-2.0.3:validations/index.yaml#_TESTS_.update[UPDATE_PAYMENT_TARGET]._RETURN_[VALID_PAYMENT_TIME_LABEL_ENUM].enumList
anchor.payment-time-label-foreclosure | isa | anchor.payment-time-labels | basis:declared | asof:fis12-2.0.3 | grounded-in:fis12-2.0.3:validations/index.yaml#_TESTS_.update[UPDATE_PAYMENT_TARGET]._RETURN_[VALID_PAYMENT_TIME_LABEL_ENUM].enumList
anchor.payment-time-label-missed-emi | isa | anchor.payment-time-labels | basis:declared | asof:fis12-2.0.3 | grounded-in:fis12-2.0.3:validations/index.yaml#_TESTS_.update[UPDATE_PAYMENT_TARGET]._RETURN_[VALID_PAYMENT_TIME_LABEL_ENUM].enumList
anchor.payment-time-label-pre-part-payment | isa | anchor.payment-time-labels | basis:declared | asof:fis12-2.0.3 | grounded-in:fis12-2.0.3:validations/index.yaml#_TESTS_.update[UPDATE_PAYMENT_TARGET]._RETURN_[VALID_PAYMENT_TIME_LABEL_ENUM].enumList
anchor.payment-time-label-installment | isa | anchor.payment-time-labels | basis:declared | asof:fis12-2.0.3 | grounded-in:fis12-2.0.3:validations/index.yaml#_TESTS_.update[UPDATE_PAYMENT_TARGET]._RETURN_[VALID_PAYMENT_TIME_LABEL_ENUM].enumList
anchor.payment-time-labels | requires | anchor.payment-params-amount | basis:declared | asof:fis12-2.0.3 | grounded-in:fis12-2.0.3:validations/index.yaml#_TESTS_.update[UPDATE_PAYMENT_TARGET]._RETURN_[REQUIRED_PAYMENT_PARAMS_AMOUNT]
anchor.update-target | disjoint-with | anchor.payment-time-labels | basis:declared | asof:fis12-2.0.3 | grounded-in:fis12-2.0.3:validations/index.yaml#_TESTS_.update[UPDATE_PAYMENT_TARGET]._CONTINUE_
anchor.loan-repayment-tag | isa | anchor.tag-group | basis:declared | asof:fis12-2.0.3 | grounded-in:fis12-2.0.3:validations/index.yaml#_TESTS_.update[UPDATE_PAYMENT_REF_ID_GOLD]._RETURN_[REQUIRED_PAYMENT_REF_ID]
anchor.loan-repayment-tag | scoped-to | anchor.item-code-gold-loan | basis:declared | asof:fis12-2.0.3 | grounded-in:fis12-2.0.3:validations/index.yaml#_TESTS_.update[UPDATE_PAYMENT_REF_ID_GOLD].loan_type_match
anchor.status | requires | anchor.order-id | basis:declared | asof:fis12-2.0.3 | grounded-in:fis12-2.0.3:validations/index.yaml#_TESTS_.status[STATUS_ORDER_ID_PERSONAL_LOAN]._RETURN_[REQUIRED_STATUS_ORDER_ID]
anchor.ref-id | scoped-to | anchor.gold-loan | basis:declared | asof:fis12-2.0.3 | grounded-in:fis12-2.0.3:validations/index.yaml#_TESTS_.status[STATUS_REF_ID_GOLD_LOAN]._RETURN_[REQUIRED_STATUS_REF_ID]
anchor.checklist-codes | isa | anchor.enum-set | basis:declared | asof:fis12-2.0.3 | grounded-in:fis12-2.0.3:validations/index.yaml#_TESTS_.on_status[ON_STATUS_CHECKLIST_CODES]._RETURN_[VALID_CHECKLIST_CODES_ENUM].enumList
anchor.checklist-codes | scoped-to | anchor.on-status | basis:declared | asof:fis12-2.0.3 | grounded-in:fis12-2.0.3:validations/index.yaml#_TESTS_.on_status[ON_STATUS_CHECKLIST_CODES].checklistpath
anchor.single-redirection | isa | anchor.checklist-codes | basis:declared | asof:fis12-2.0.3 | grounded-in:fis12-2.0.3:validations/index.yaml#_TESTS_.on_status[ON_STATUS_CHECKLIST_CODES]._RETURN_[VALID_CHECKLIST_CODES_ENUM].enumList
anchor.ekyc-verification | isa | anchor.checklist-codes | basis:declared | asof:fis12-2.0.3 | grounded-in:fis12-2.0.3:validations/index.yaml#_TESTS_.on_status[ON_STATUS_CHECKLIST_CODES]._RETURN_[VALID_CHECKLIST_CODES_ENUM].enumList
anchor.bank-account-verification | isa | anchor.checklist-codes | basis:declared | asof:fis12-2.0.3 | grounded-in:fis12-2.0.3:validations/index.yaml#_TESTS_.on_status[ON_STATUS_CHECKLIST_CODES]._RETURN_[VALID_CHECKLIST_CODES_ENUM].enumList
anchor.repayment-mandate | isa | anchor.checklist-codes | basis:declared | asof:fis12-2.0.3 | grounded-in:fis12-2.0.3:validations/index.yaml#_TESTS_.on_status[ON_STATUS_CHECKLIST_CODES]._RETURN_[VALID_CHECKLIST_CODES_ENUM].enumList
anchor.loan-agreement | isa | anchor.checklist-codes | basis:declared | asof:fis12-2.0.3 | grounded-in:fis12-2.0.3:validations/index.yaml#_TESTS_.on_status[ON_STATUS_CHECKLIST_CODES]._RETURN_[VALID_CHECKLIST_CODES_ENUM].enumList
anchor.offline-underwriting | isa | anchor.checklist-codes | basis:declared | asof:fis12-2.0.3 | grounded-in:fis12-2.0.3:validations/index.yaml#_TESTS_.on_status[ON_STATUS_CHECKLIST_CODES]._RETURN_[VALID_CHECKLIST_CODES_ENUM].enumList
anchor.issue-status-codes | isa | anchor.enum-set | basis:declared | asof:fis12-2.0.3 | grounded-in:fis12-2.0.3:validations/index.yaml#_TESTS_.issue[ISSUE_VALIDATION_VERSION_200]._RETURN_[REQUIRED_MESSAGE_STATUS].enumList
anchor.issue-levels | isa | anchor.enum-set | basis:declared | asof:fis12-2.0.3 | grounded-in:fis12-2.0.3:validations/index.yaml#_TESTS_.issue[ISSUE_VALIDATION_VERSION_200]._RETURN_[REQUIRED_MESSAGE_LEVEL].enumList
anchor.issue-ref-types | isa | anchor.enum-set | basis:declared | asof:fis12-2.0.3 | grounded-in:fis12-2.0.3:validations/index.yaml#_TESTS_.issue[ISSUE_VALIDATION_VERSION_200]._RETURN_[REQUIRED_MESSAGE_REF_TYPE].enumList
anchor.igm-2-0-0 | requires | anchor.issue-status-codes | basis:declared | asof:fis12-2.0.3 | grounded-in:fis12-2.0.3:validations/index.yaml#_TESTS_.issue[ISSUE_VALIDATION_VERSION_200]._RETURN_[REQUIRED_MESSAGE_STATUS]
anchor.igm-2-0-0 | requires | anchor.issue-levels | basis:declared | asof:fis12-2.0.3 | grounded-in:fis12-2.0.3:validations/index.yaml#_TESTS_.issue[ISSUE_VALIDATION_VERSION_200]._RETURN_[REQUIRED_MESSAGE_LEVEL]
anchor.issue-categories | isa | anchor.enum-set | basis:declared | asof:fis12-2.0.3 | grounded-in:fis12-2.0.3:validations/index.yaml#_TESTS_.issue[ISSUE_VALIDATION_VERSION_100]._RETURN_[ISSUE_VALIDATION_OPEN]._RETURN_[REQUIRED_ISSUE_CATEGORY].validValues
anchor.issue-sub-categories | isa | anchor.enum-set | basis:declared | asof:fis12-2.0.3 | grounded-in:fis12-2.0.3:validations/index.yaml#_TESTS_.issue[ISSUE_VALIDATION_VERSION_100]._RETURN_[ISSUE_VALIDATION_OPEN]._RETURN_[REQUIRED_ISSUE_SUB_CATEGORY].validValues
anchor.igm-1-0-0 | requires | anchor.issue-categories | basis:declared | asof:fis12-2.0.3 | grounded-in:fis12-2.0.3:validations/index.yaml#_TESTS_.issue[ISSUE_VALIDATION_VERSION_100]._RETURN_[ISSUE_VALIDATION_OPEN]._RETURN_[REQUIRED_ISSUE_CATEGORY]
anchor.igm-1-0-0 | requires | anchor.issue-sub-categories | basis:declared | asof:fis12-2.0.3 | grounded-in:fis12-2.0.3:validations/index.yaml#_TESTS_.issue[ISSUE_VALIDATION_VERSION_100]._RETURN_[ISSUE_VALIDATION_OPEN]._RETURN_[REQUIRED_ISSUE_SUB_CATEGORY]
anchor.respondent-action-codes | isa | anchor.enum-set | basis:declared | asof:fis12-2.0.3 | grounded-in:fis12-2.0.3:validations/index.yaml#_TESTS_.on_issue[ON_ISSUE_VALIDATION_VERSION_100]._RETURN_[REQUIRED_RESPONDENT_ACTION].enumList
anchor.on-issue | requires | anchor.respondent-action-codes | basis:declared | asof:fis12-2.0.3 | grounded-in:fis12-2.0.3:validations/index.yaml#_TESTS_.on_issue[ON_ISSUE_VALIDATION_VERSION_100]._RETURN_[REQUIRED_RESPONDENT_ACTION]
anchor.on-issue-status | requires | anchor.respondent-action-codes | basis:declared | asof:fis12-2.0.3 | grounded-in:fis12-2.0.3:validations/index.yaml#_TESTS_.on_issue_status[ISSUE_ON_ISSUE_STATUS_VALIDATION]._RETURN_[REQUIRED_RESPONDENT_ACTION]
anchor.respondent-action-codes | requires | anchor.respondent-identity | basis:declared | asof:fis12-2.0.3 | grounded-in:fis12-2.0.3:validations/index.yaml#_TESTS_.on_issue[ON_ISSUE_VALIDATION_VERSION_100]._RETURN_[REQUIRED_RESPONDENT_UPDATED_BY_ORG]
anchor.grievance | requires | anchor.issue-context-fields | basis:declared | asof:fis12-2.0.3 | grounded-in:fis12-2.0.3:validations/index.yaml#_TESTS_.issue[REQUIRED_CONTEXT_FIELDS]._RETURN_
anchor.issue-context-fields | disjoint-with | anchor.context-required-block | basis:declared | asof:fis12-2.0.3 | grounded-in:fis12-2.0.3:validations/index.yaml#_TESTS_.on_issue[REQUIRED_CONTEXT_FIELDS]._RETURN_
anchor.grievance | isa | anchor.loan-servicing-event | basis:declared | asof:fis12-2.0.3 | grounded-in:fis12-2.0.3:flows/GOLD LOAN/Gold_Loan_Offline_with_igm_1.0.0.yaml#steps[issue_open_100].description
anchor.search-intent | sent-by | anchor.bap | basis:declared | asof:fis12-2.0.3 | grounded-in:fis12-2.0.3:attributes/PERSONAL_LOAN.yaml#attribute_set.search.message.intent._description.owner
anchor.search-intent | requires | anchor.search-category-codes | basis:declared | asof:fis12-2.0.3 | grounded-in:fis12-2.0.3:attributes/PERSONAL_LOAN.yaml#attribute_set.search.message.intent.category.descriptor.code._description.required
anchor.search-intent | requires | anchor.payment-collected-by | basis:declared | asof:fis12-2.0.3 | grounded-in:fis12-2.0.3:attributes/PERSONAL_LOAN.yaml#attribute_set.search.message.intent.payment.collected_by._description.required
anchor.catalog | sent-by | anchor.bpp | basis:declared | asof:fis12-2.0.3 | grounded-in:fis12-2.0.3:attributes/PERSONAL_LOAN.yaml#attribute_set.on_search.message.catalog._description.owner
anchor.catalog | has-slot | anchor.provider | basis:declared | asof:fis12-2.0.3 | grounded-in:fis12-2.0.3:attributes/PERSONAL_LOAN.yaml#attribute_set.on_search.message.catalog.providers._description
anchor.provider | requires | anchor.provider-id | basis:declared | asof:fis12-2.0.3 | grounded-in:fis12-2.0.3:attributes/PERSONAL_LOAN.yaml#attribute_set.on_search.message.catalog.providers.id._description.required
anchor.provider | has-slot | anchor.catalog-category-codes | basis:declared | asof:fis12-2.0.3 | grounded-in:fis12-2.0.3:attributes/PERSONAL_LOAN.yaml#attribute_set.on_search.message.catalog.providers.categories._description
anchor.provider | has-slot | anchor.loan-item | basis:declared | asof:fis12-2.0.3 | grounded-in:fis12-2.0.3:attributes/PERSONAL_LOAN.yaml#attribute_set.on_search.message.catalog.providers.items._description
anchor.loan-item | requires | anchor.xinput | basis:declared | asof:fis12-2.0.3 | grounded-in:fis12-2.0.3:attributes/PERSONAL_LOAN.yaml#attribute_set.on_search.message.catalog.providers.items.xinput._description.required
anchor.loan-item | requires | anchor.catalog-category-codes | basis:declared | asof:fis12-2.0.3 | grounded-in:fis12-2.0.3:attributes/PERSONAL_LOAN.yaml#attribute_set.on_search.message.catalog.providers.items.category_ids._description.required
anchor.provider | not-requires | anchor.provider-tags | basis:declared | asof:fis12-2.0.3 | grounded-in:fis12-2.0.3:attributes/PERSONAL_LOAN.yaml#attribute_set.on_search.message.catalog.providers.tags._description.required
anchor.select | requires | anchor.provider-id | basis:declared | asof:fis12-2.0.3 | grounded-in:fis12-2.0.3:attributes/PERSONAL_LOAN.yaml#attribute_set.select.message.order.provider.id._description.required
anchor.select | requires | anchor.xinput-form-response | basis:declared | asof:fis12-2.0.3 | grounded-in:fis12-2.0.3:attributes/PERSONAL_LOAN.yaml#attribute_set.select.message.order.items.xinput.form_response._description.required
anchor.select | not-requires | anchor.fulfillment | basis:declared | asof:fis12-2.0.3 | grounded-in:fis12-2.0.3:attributes/PERSONAL_LOAN.yaml#attribute_set.select.message.order.fulfillments._description.required
anchor.on-select | requires | anchor.item-price | basis:declared | asof:fis12-2.0.3 | grounded-in:fis12-2.0.3:attributes/PERSONAL_LOAN.yaml#attribute_set.on_select.message.order.items.price._description.required
anchor.on-select | requires | anchor.currency-inr | basis:declared | asof:fis12-2.0.3 | grounded-in:fis12-2.0.3:attributes/PERSONAL_LOAN.yaml#attribute_set.on_select.message.order.items.price.currency._description.required
anchor.on-select | requires | anchor.fulfillment | basis:declared | asof:fis12-2.0.3 | grounded-in:fis12-2.0.3:attributes/PERSONAL_LOAN.yaml#attribute_set.on_select.message.order.fulfillments._description.required
anchor.on-select | sent-by | anchor.bpp | basis:declared | asof:fis12-2.0.3 | grounded-in:fis12-2.0.3:attributes/PERSONAL_LOAN.yaml#attribute_set.on_select.message._description.owner
anchor.on-init | requires | anchor.xinput-headings | basis:declared | asof:fis12-2.0.3 | grounded-in:fis12-2.0.3:attributes/PERSONAL_LOAN.yaml#attribute_set.on_init.message.order.items.xinput.head.headings._description.required
anchor.on-init | requires | anchor.quote-breakup-titles-servicing | basis:declared | asof:fis12-2.0.3 | grounded-in:fis12-2.0.3:attributes/PERSONAL_LOAN.yaml#attribute_set.on_init.message.order.quote.breakup.title._description.required
anchor.on-init | requires | anchor.payment-types | basis:declared | asof:fis12-2.0.3 | grounded-in:fis12-2.0.3:attributes/PERSONAL_LOAN.yaml#attribute_set.on_init.message.order.payments.type._description.required
anchor.on-init | requires | anchor.payment-status-codes | basis:declared | asof:fis12-2.0.3 | grounded-in:fis12-2.0.3:attributes/PERSONAL_LOAN.yaml#attribute_set.on_init.message.order.payments.status._description.required
anchor.on-init | not-requires | anchor.payment-time-labels | basis:declared | asof:fis12-2.0.3 | grounded-in:fis12-2.0.3:attributes/PERSONAL_LOAN.yaml#attribute_set.on_init.message.order.payments.time.label._description.required
anchor.on-confirm | requires | anchor.payment-time-labels | basis:declared | asof:fis12-2.0.3 | grounded-in:fis12-2.0.3:attributes/GOLD_LOAN.yaml#attribute_set.on_confirm.message.order.payments.time.label._description.required
anchor.update | requires | anchor.payment-time-labels | basis:declared | asof:fis12-2.0.3 | grounded-in:fis12-2.0.3:attributes/GOLD_LOAN.yaml#attribute_set.update.message.order.payments.time.label._description.required
anchor.on-update | requires | anchor.payment-status-codes | basis:declared | asof:fis12-2.0.3 | grounded-in:fis12-2.0.3:attributes/GOLD_LOAN.yaml#attribute_set.on_update.message.order.payments.status._description.required
anchor.on-update | sent-by | anchor.bpp | basis:declared | asof:fis12-2.0.3 | grounded-in:fis12-2.0.3:attributes/GOLD_LOAN.yaml#attribute_set.on_update.message.order.payments.status._description.owner
anchor.context-domain | constrains | anchor.ondc-fis12 | basis:declared | asof:fis12-2.0.3 | grounded-in:fis12-2.0.3:attributes/PERSONAL_LOAN.yaml#attribute_set.search.context.domain._description.enums
anchor.context-country | constrains | anchor.india-jurisdiction | basis:declared | asof:fis12-2.0.3 | grounded-in:fis12-2.0.3:attributes/PERSONAL_LOAN.yaml#attribute_set.search.context.location.country.code._description.enums
anchor.context-city | scoped-to | anchor.search | basis:declared | asof:fis12-2.0.3 | grounded-in:fis12-2.0.3:attributes/PERSONAL_LOAN.yaml#attribute_set.search.context.location.city.code._description.usage
anchor.search-category-codes | scoped-to | anchor.search-intent | basis:declared | asof:fis12-2.0.3 | grounded-in:fis12-2.0.3:attributes/GOLD_LOAN.yaml#attribute_set.search.message.intent.category.descriptor.code._description.enums
anchor.html-form-personal-loan | isa | anchor.html-form | basis:declared | asof:fis12-2.0.3 | grounded-in:fis12-2.0.3:attributes/PERSONAL_LOAN.yaml#attribute_set.html_form
anchor.html-form-gold-loan | isa | anchor.html-form | basis:declared | asof:fis12-2.0.3 | grounded-in:fis12-2.0.3:attributes/GOLD_LOAN.yaml#attribute_set.html_form
anchor.html-form-personal-loan | sent-by | anchor.bap | basis:declared | asof:fis12-2.0.3 | grounded-in:fis12-2.0.3:attributes/PERSONAL_LOAN.yaml#attribute_set.html_form.pan._description.owner
anchor.html-form-personal-loan | has-slot | anchor.pan-credential | basis:declared | asof:fis12-2.0.3 | grounded-in:fis12-2.0.3:attributes/PERSONAL_LOAN.yaml#attribute_set.html_form.pan._description
anchor.html-form-personal-loan | has-slot | anchor.employment-type | basis:declared | asof:fis12-2.0.3 | grounded-in:fis12-2.0.3:attributes/PERSONAL_LOAN.yaml#attribute_set.html_form.employmentType._description
anchor.html-form-personal-loan | has-slot | anchor.applicant-income | basis:declared | asof:fis12-2.0.3 | grounded-in:fis12-2.0.3:attributes/PERSONAL_LOAN.yaml#attribute_set.html_form.income._description
anchor.html-form-personal-loan | has-slot | anchor.applicant-address | basis:declared | asof:fis12-2.0.3 | grounded-in:fis12-2.0.3:attributes/PERSONAL_LOAN.yaml#attribute_set.html_form.addressL1._description
anchor.html-form-personal-loan | has-slot | anchor.account-aggregator | basis:declared | asof:fis12-2.0.3 | grounded-in:fis12-2.0.3:attributes/PERSONAL_LOAN.yaml#attribute_set.html_form.aa_id._description
anchor.html-form-personal-loan | has-slot | anchor.bureau-consent | basis:declared | asof:fis12-2.0.3 | grounded-in:fis12-2.0.3:attributes/PERSONAL_LOAN.yaml#attribute_set.html_form.bureauConsent._description
anchor.html-form-personal-loan | has-slot | anchor.loan-end-use | basis:declared | asof:fis12-2.0.3 | grounded-in:fis12-2.0.3:attributes/PERSONAL_LOAN.yaml#attribute_set.html_form.endUse._description
anchor.bureau-consent | precedes | anchor.bureau-loan | basis:inferred | asof:fis12-2.0.3
anchor.html-form-gold-loan | has-slot | anchor.gold-collateral-details | basis:declared | asof:fis12-2.0.3 | grounded-in:fis12-2.0.3:attributes/GOLD_LOAN.yaml#attribute_set.html_form.jewellery._description
anchor.html-form-gold-loan | has-slot | anchor.gold-purity | basis:declared | asof:fis12-2.0.3 | grounded-in:fis12-2.0.3:attributes/GOLD_LOAN.yaml#attribute_set.html_form.purity._description
anchor.html-form-gold-loan | has-slot | anchor.requested-amount | basis:declared | asof:fis12-2.0.3 | grounded-in:fis12-2.0.3:attributes/GOLD_LOAN.yaml#attribute_set.html_form.requestAmount._description
anchor.html-form-gold-loan | has-slot | anchor.requested-term | basis:declared | asof:fis12-2.0.3 | grounded-in:fis12-2.0.3:attributes/GOLD_LOAN.yaml#attribute_set.html_form.requestTerm._description
anchor.html-form-gold-loan | has-slot | anchor.applicant-constitution | basis:declared | asof:fis12-2.0.3 | grounded-in:fis12-2.0.3:attributes/GOLD_LOAN.yaml#attribute_set.html_form.constitution._description
anchor.html-form-gold-loan | has-slot | anchor.annual-income | basis:declared | asof:fis12-2.0.3 | grounded-in:fis12-2.0.3:attributes/GOLD_LOAN.yaml#attribute_set.html_form.annualIncome._description
anchor.html-form-gold-loan | not-has-slot | anchor.bureau-consent | basis:declared | asof:fis12-2.0.3 | grounded-in:fis12-2.0.3:attributes/GOLD_LOAN.yaml#attribute_set.html_form
anchor.gold-collateral-details | constrains | anchor.ltv-ratio | basis:derived | asof:fis12-2.0.3 | grounded-in:anchor.ltv-ratio
anchor.html-form-personal-loan | not-has-slot | anchor.gold-collateral-details | basis:declared | asof:fis12-2.0.3 | grounded-in:fis12-2.0.3:attributes/PERSONAL_LOAN.yaml#attribute_set.html_form
anchor.dynamic-form | has-slot | anchor.id-type | basis:declared | asof:fis12-2.0.3 | grounded-in:fis12-2.0.3:attributes/PERSONAL_LOAN.yaml#attribute_set.dynamic_form.idType._description
anchor.html-form-personal-loan | scoped-to | anchor.personal-loan-usecase | basis:declared | asof:fis12-2.0.3 | grounded-in:fis12-2.0.3:attributes/PERSONAL_LOAN.yaml#meta.use_case_id
anchor.html-form-gold-loan | scoped-to | anchor.gold-loan-usecase | basis:declared | asof:fis12-2.0.3 | grounded-in:fis12-2.0.3:attributes/GOLD_LOAN.yaml#meta.use_case_id
anchor.attribute-dictionary | not-isa | anchor.runtime-behaviour | basis:authority | asof:fis12-2.0.3 | grounded-in:workbench:frames/automation-specifications.md
anchor.html-form-personal-loan | isa | anchor.attribute-dictionary | basis:declared | asof:fis12-2.0.3 | grounded-in:fis12-2.0.3:attributes/index.yaml#[0].$ref
anchor.event-application-submittion-failure | causes | "80101" | basis:declared | asof:fis12-2.0.3 | grounded-in:fis12-2.0.3:errors/index.yaml#code[80101].Event
"80101" | sent-by | anchor.bap | basis:declared | asof:fis12-2.0.3 | grounded-in:fis12-2.0.3:errors/index.yaml#code[80101].From
"80101" | isa | anchor.error-code | basis:declared | asof:fis12-2.0.3 | grounded-in:fis12-2.0.3:errors/index.yaml#code[80101].code
anchor.event-aa-consent-creation-failure | causes | "80201" | basis:declared | asof:fis12-2.0.3 | grounded-in:fis12-2.0.3:errors/index.yaml#code[80201].Event
"80201" | sent-by | anchor.bpp | basis:declared | asof:fis12-2.0.3 | grounded-in:fis12-2.0.3:errors/index.yaml#code[80201].From
"80201" | isa | anchor.error-code | basis:declared | asof:fis12-2.0.3 | grounded-in:fis12-2.0.3:errors/index.yaml#code[80201].code
anchor.event-aa-data-pull-failure | causes | "80202" | basis:declared | asof:fis12-2.0.3 | grounded-in:fis12-2.0.3:errors/index.yaml#code[80202].Event
"80202" | sent-by | anchor.bpp | basis:declared | asof:fis12-2.0.3 | grounded-in:fis12-2.0.3:errors/index.yaml#code[80202].From
"80202" | isa | anchor.error-code | basis:declared | asof:fis12-2.0.3 | grounded-in:fis12-2.0.3:errors/index.yaml#code[80202].code
anchor.event-offer-return-failure | causes | "80203" | basis:declared | asof:fis12-2.0.3 | grounded-in:fis12-2.0.3:errors/index.yaml#code[80203].Event
"80203" | sent-by | anchor.bpp | basis:declared | asof:fis12-2.0.3 | grounded-in:fis12-2.0.3:errors/index.yaml#code[80203].From
"80203" | isa | anchor.error-code | basis:declared | asof:fis12-2.0.3 | grounded-in:fis12-2.0.3:errors/index.yaml#code[80203].code
anchor.event-offer-acceptance-failure | causes | "80102" | basis:declared | asof:fis12-2.0.3 | grounded-in:fis12-2.0.3:errors/index.yaml#code[80102].Event
"80102" | sent-by | anchor.bap | basis:declared | asof:fis12-2.0.3 | grounded-in:fis12-2.0.3:errors/index.yaml#code[80102].From
"80102" | isa | anchor.error-code | basis:declared | asof:fis12-2.0.3 | grounded-in:fis12-2.0.3:errors/index.yaml#code[80102].code
anchor.event-individual-kyc-failure | causes | "80204" | basis:declared | asof:fis12-2.0.3 | grounded-in:fis12-2.0.3:errors/index.yaml#code[80204].Event
"80204" | sent-by | anchor.bpp | basis:declared | asof:fis12-2.0.3 | grounded-in:fis12-2.0.3:errors/index.yaml#code[80204].From
"80204" | isa | anchor.error-code | basis:declared | asof:fis12-2.0.3 | grounded-in:fis12-2.0.3:errors/index.yaml#code[80204].code
anchor.event-entity-kyc-failure | causes | "80205" | basis:declared | asof:fis12-2.0.3 | grounded-in:fis12-2.0.3:errors/index.yaml#code[80205].Event
"80205" | sent-by | anchor.bpp | basis:declared | asof:fis12-2.0.3 | grounded-in:fis12-2.0.3:errors/index.yaml#code[80205].From
"80205" | isa | anchor.error-code | basis:declared | asof:fis12-2.0.3 | grounded-in:fis12-2.0.3:errors/index.yaml#code[80205].code
anchor.event-disbursment-account-sharing-failure | causes | "80103" | basis:declared | asof:fis12-2.0.3 | grounded-in:fis12-2.0.3:errors/index.yaml#code[80103].Event
"80103" | sent-by | anchor.bap | basis:declared | asof:fis12-2.0.3 | grounded-in:fis12-2.0.3:errors/index.yaml#code[80103].From
"80103" | isa | anchor.error-code | basis:declared | asof:fis12-2.0.3 | grounded-in:fis12-2.0.3:errors/index.yaml#code[80103].code
anchor.event-disbursment-account-verification-failure | causes | "80206" | basis:declared | asof:fis12-2.0.3 | grounded-in:fis12-2.0.3:errors/index.yaml#code[80206].Event
"80206" | sent-by | anchor.bpp | basis:declared | asof:fis12-2.0.3 | grounded-in:fis12-2.0.3:errors/index.yaml#code[80206].From
"80206" | isa | anchor.error-code | basis:declared | asof:fis12-2.0.3 | grounded-in:fis12-2.0.3:errors/index.yaml#code[80206].code
anchor.event-repayment-setup-failure | causes | "80207" | basis:declared | asof:fis12-2.0.3 | grounded-in:fis12-2.0.3:errors/index.yaml#code[80207].Event
"80207" | sent-by | anchor.bpp | basis:declared | asof:fis12-2.0.3 | grounded-in:fis12-2.0.3:errors/index.yaml#code[80207].From
"80207" | isa | anchor.error-code | basis:declared | asof:fis12-2.0.3 | grounded-in:fis12-2.0.3:errors/index.yaml#code[80207].code
anchor.event-loan-agreement-sharing-failure | causes | "80208" | basis:declared | asof:fis12-2.0.3 | grounded-in:fis12-2.0.3:errors/index.yaml#code[80208].Event
"80208" | sent-by | anchor.bpp | basis:declared | asof:fis12-2.0.3 | grounded-in:fis12-2.0.3:errors/index.yaml#code[80208].From
"80208" | isa | anchor.error-code | basis:declared | asof:fis12-2.0.3 | grounded-in:fis12-2.0.3:errors/index.yaml#code[80208].code
anchor.event-loan-agreement-signing-failure-aadhar-esign | causes | "80209" | basis:declared | asof:fis12-2.0.3 | grounded-in:fis12-2.0.3:errors/index.yaml#code[80209].Event
"80209" | sent-by | anchor.bpp | basis:declared | asof:fis12-2.0.3 | grounded-in:fis12-2.0.3:errors/index.yaml#code[80209].From
"80209" | isa | anchor.error-code | basis:declared | asof:fis12-2.0.3 | grounded-in:fis12-2.0.3:errors/index.yaml#code[80209].code
anchor.event-monitoring-consent-creation-failure | causes | "80210" | basis:declared | asof:fis12-2.0.3 | grounded-in:fis12-2.0.3:errors/index.yaml#code[80210].Event
"80210" | sent-by | anchor.bpp | basis:declared | asof:fis12-2.0.3 | grounded-in:fis12-2.0.3:errors/index.yaml#code[80210].From
"80210" | isa | anchor.error-code | basis:declared | asof:fis12-2.0.3 | grounded-in:fis12-2.0.3:errors/index.yaml#code[80210].code
anchor.event-monitoring-consent-approval-failure | causes | "80211" | basis:declared | asof:fis12-2.0.3 | grounded-in:fis12-2.0.3:errors/index.yaml#code[80211].Event
"80211" | sent-by | anchor.bpp | basis:declared | asof:fis12-2.0.3 | grounded-in:fis12-2.0.3:errors/index.yaml#code[80211].From
"80211" | isa | anchor.error-code | basis:declared | asof:fis12-2.0.3 | grounded-in:fis12-2.0.3:errors/index.yaml#code[80211].code
anchor.event-loan-disbursal-failure | causes | "80104" | basis:declared | asof:fis12-2.0.3 | grounded-in:fis12-2.0.3:errors/index.yaml#code[80104].Event
"80104" | sent-by | anchor.bap | basis:declared | asof:fis12-2.0.3 | grounded-in:fis12-2.0.3:errors/index.yaml#code[80104].From
"80104" | isa | anchor.error-code | basis:declared | asof:fis12-2.0.3 | grounded-in:fis12-2.0.3:errors/index.yaml#code[80104].code
anchor.event-payment-initiation-failure | causes | "80212" | basis:declared | asof:fis12-2.0.3 | grounded-in:fis12-2.0.3:errors/index.yaml#code[80212].Event
"80212" | sent-by | anchor.bpp | basis:declared | asof:fis12-2.0.3 | grounded-in:fis12-2.0.3:errors/index.yaml#code[80212].From
"80212" | isa | anchor.error-code | basis:declared | asof:fis12-2.0.3 | grounded-in:fis12-2.0.3:errors/index.yaml#code[80212].code
anchor.event-payment-completion-failure | causes | "80213" | basis:declared | asof:fis12-2.0.3 | grounded-in:fis12-2.0.3:errors/index.yaml#code[80213].Event
"80213" | sent-by | anchor.bpp | basis:declared | asof:fis12-2.0.3 | grounded-in:fis12-2.0.3:errors/index.yaml#code[80213].From
"80213" | isa | anchor.error-code | basis:declared | asof:fis12-2.0.3 | grounded-in:fis12-2.0.3:errors/index.yaml#code[80213].code
anchor.event-timeout-the-request-or-operation-timed-out | causes | "80214" | basis:declared | asof:fis12-2.0.3 | grounded-in:fis12-2.0.3:errors/index.yaml#code[80214].Event
"80214" | sent-by | anchor.bpp | basis:declared | asof:fis12-2.0.3 | grounded-in:fis12-2.0.3:errors/index.yaml#code[80214].From
"80214" | isa | anchor.error-code | basis:declared | asof:fis12-2.0.3 | grounded-in:fis12-2.0.3:errors/index.yaml#code[80214].code
anchor.event-general-error-an-unspecified-error-occurred | causes | "80215" | basis:declared | asof:fis12-2.0.3 | grounded-in:fis12-2.0.3:errors/index.yaml#code[80215].Event
"80215" | sent-by | anchor.bpp | basis:declared | asof:fis12-2.0.3 | grounded-in:fis12-2.0.3:errors/index.yaml#code[80215].From
"80215" | sent-by | anchor.bap | basis:declared | asof:fis12-2.0.3 | grounded-in:fis12-2.0.3:errors/index.yaml#code[80215].From
"80215" | isa | anchor.error-code | basis:declared | asof:fis12-2.0.3 | grounded-in:fis12-2.0.3:errors/index.yaml#code[80215].code
anchor.event-invalid-input-user-input-is-not-valid | causes | "80216" | basis:declared | asof:fis12-2.0.3 | grounded-in:fis12-2.0.3:errors/index.yaml#code[80216].Event
"80216" | sent-by | anchor.bpp | basis:declared | asof:fis12-2.0.3 | grounded-in:fis12-2.0.3:errors/index.yaml#code[80216].From
"80216" | isa | anchor.error-code | basis:declared | asof:fis12-2.0.3 | grounded-in:fis12-2.0.3:errors/index.yaml#code[80216].code
anchor.event-missing-data-required-data-is-missing | causes | "80217" | basis:declared | asof:fis12-2.0.3 | grounded-in:fis12-2.0.3:errors/index.yaml#code[80217].Event
"80217" | sent-by | anchor.bpp | basis:declared | asof:fis12-2.0.3 | grounded-in:fis12-2.0.3:errors/index.yaml#code[80217].From
"80217" | sent-by | anchor.bap | basis:declared | asof:fis12-2.0.3 | grounded-in:fis12-2.0.3:errors/index.yaml#code[80217].From
"80217" | isa | anchor.error-code | basis:declared | asof:fis12-2.0.3 | grounded-in:fis12-2.0.3:errors/index.yaml#code[80217].code
anchor.event-data-validation-failed-input-data-failed-validation | causes | "80218" | basis:declared | asof:fis12-2.0.3 | grounded-in:fis12-2.0.3:errors/index.yaml#code[80218].Event
"80218" | sent-by | anchor.bpp | basis:declared | asof:fis12-2.0.3 | grounded-in:fis12-2.0.3:errors/index.yaml#code[80218].From
"80218" | isa | anchor.error-code | basis:declared | asof:fis12-2.0.3 | grounded-in:fis12-2.0.3:errors/index.yaml#code[80218].code
anchor.event-service-unavailable-the-service-is-temporarily-unava | causes | "80219" | basis:declared | asof:fis12-2.0.3 | grounded-in:fis12-2.0.3:errors/index.yaml#code[80219].Event
"80219" | sent-by | anchor.bpp | basis:declared | asof:fis12-2.0.3 | grounded-in:fis12-2.0.3:errors/index.yaml#code[80219].From
"80219" | isa | anchor.error-code | basis:declared | asof:fis12-2.0.3 | grounded-in:fis12-2.0.3:errors/index.yaml#code[80219].code
anchor.event-file-not-found-the-requested-file-does-not-exist | causes | "80220" | basis:declared | asof:fis12-2.0.3 | grounded-in:fis12-2.0.3:errors/index.yaml#code[80220].Event
"80220" | sent-by | anchor.bpp | basis:declared | asof:fis12-2.0.3 | grounded-in:fis12-2.0.3:errors/index.yaml#code[80220].From
"80220" | isa | anchor.error-code | basis:declared | asof:fis12-2.0.3 | grounded-in:fis12-2.0.3:errors/index.yaml#code[80220].code
anchor.event-3001-file-upload-failed-an-error-occurred-while-uplo | causes | "80105" | basis:declared | asof:fis12-2.0.3 | grounded-in:fis12-2.0.3:errors/index.yaml#code[80105].Event
"80105" | sent-by | anchor.bap | basis:declared | asof:fis12-2.0.3 | grounded-in:fis12-2.0.3:errors/index.yaml#code[80105].From
"80105" | isa | anchor.error-code | basis:declared | asof:fis12-2.0.3 | grounded-in:fis12-2.0.3:errors/index.yaml#code[80105].code
anchor.event-file-format-not-supported-the-uploaded-file-format-i | causes | "80221" | basis:declared | asof:fis12-2.0.3 | grounded-in:fis12-2.0.3:errors/index.yaml#code[80221].Event
"80221" | sent-by | anchor.bpp | basis:declared | asof:fis12-2.0.3 | grounded-in:fis12-2.0.3:errors/index.yaml#code[80221].From
"80221" | isa | anchor.error-code | basis:declared | asof:fis12-2.0.3 | grounded-in:fis12-2.0.3:errors/index.yaml#code[80221].code
anchor.event-file-size-exceeded-the-uploaded-file-exceeds-size-li | causes | "80222" | basis:declared | asof:fis12-2.0.3 | grounded-in:fis12-2.0.3:errors/index.yaml#code[80222].Event
"80222" | sent-by | anchor.bpp | basis:declared | asof:fis12-2.0.3 | grounded-in:fis12-2.0.3:errors/index.yaml#code[80222].From
"80222" | isa | anchor.error-code | basis:declared | asof:fis12-2.0.3 | grounded-in:fis12-2.0.3:errors/index.yaml#code[80222].code
anchor.event-api-rate-limit-exceeded | causes | "80223" | basis:declared | asof:fis12-2.0.3 | grounded-in:fis12-2.0.3:errors/index.yaml#code[80223].Event
"80223" | sent-by | anchor.bpp | basis:declared | asof:fis12-2.0.3 | grounded-in:fis12-2.0.3:errors/index.yaml#code[80223].From
"80223" | isa | anchor.error-code | basis:declared | asof:fis12-2.0.3 | grounded-in:fis12-2.0.3:errors/index.yaml#code[80223].code
anchor.event-aa-drop-off-due-to-buffering-time | causes | "80224" | basis:declared | asof:fis12-2.0.3 | grounded-in:fis12-2.0.3:errors/index.yaml#code[80224].Event
"80224" | sent-by | anchor.bpp | basis:declared | asof:fis12-2.0.3 | grounded-in:fis12-2.0.3:errors/index.yaml#code[80224].From
"80224" | isa | anchor.error-code | basis:declared | asof:fis12-2.0.3 | grounded-in:fis12-2.0.3:errors/index.yaml#code[80224].code
anchor.event-pincode-issue | causes | "80225" | basis:declared | asof:fis12-2.0.3 | grounded-in:fis12-2.0.3:errors/index.yaml#code[80225].Event
"80225" | sent-by | anchor.bpp | basis:declared | asof:fis12-2.0.3 | grounded-in:fis12-2.0.3:errors/index.yaml#code[80225].From
"80225" | isa | anchor.error-code | basis:declared | asof:fis12-2.0.3 | grounded-in:fis12-2.0.3:errors/index.yaml#code[80225].code
anchor.event-cibil-rejection | causes | "80226" | basis:declared | asof:fis12-2.0.3 | grounded-in:fis12-2.0.3:errors/index.yaml#code[80226].Event
"80226" | sent-by | anchor.bpp | basis:declared | asof:fis12-2.0.3 | grounded-in:fis12-2.0.3:errors/index.yaml#code[80226].From
"80226" | isa | anchor.error-code | basis:declared | asof:fis12-2.0.3 | grounded-in:fis12-2.0.3:errors/index.yaml#code[80226].code
anchor.event-rejected-due-to-or-limits | causes | "80227" | basis:declared | asof:fis12-2.0.3 | grounded-in:fis12-2.0.3:errors/index.yaml#code[80227].Event
"80227" | sent-by | anchor.bpp | basis:declared | asof:fis12-2.0.3 | grounded-in:fis12-2.0.3:errors/index.yaml#code[80227].From
"80227" | isa | anchor.error-code | basis:declared | asof:fis12-2.0.3 | grounded-in:fis12-2.0.3:errors/index.yaml#code[80227].code
anchor.event-lender-policy-rejection | causes | "80228" | basis:declared | asof:fis12-2.0.3 | grounded-in:fis12-2.0.3:errors/index.yaml#code[80228].Event
"80228" | sent-by | anchor.bpp | basis:declared | asof:fis12-2.0.3 | grounded-in:fis12-2.0.3:errors/index.yaml#code[80228].From
"80228" | isa | anchor.error-code | basis:declared | asof:fis12-2.0.3 | grounded-in:fis12-2.0.3:errors/index.yaml#code[80228].code
anchor.event-report-not-received-from-bureau | causes | "80229" | basis:declared | asof:fis12-2.0.3 | grounded-in:fis12-2.0.3:errors/index.yaml#code[80229].Event
"80229" | sent-by | anchor.bpp | basis:declared | asof:fis12-2.0.3 | grounded-in:fis12-2.0.3:errors/index.yaml#code[80229].From
"80229" | isa | anchor.error-code | basis:declared | asof:fis12-2.0.3 | grounded-in:fis12-2.0.3:errors/index.yaml#code[80229].code
anchor.event-account-agreegator-id-is-required | causes | "80230" | basis:declared | asof:fis12-2.0.3 | grounded-in:fis12-2.0.3:errors/index.yaml#code[80230].Event
"80230" | sent-by | anchor.bpp | basis:declared | asof:fis12-2.0.3 | grounded-in:fis12-2.0.3:errors/index.yaml#code[80230].From
"80230" | isa | anchor.error-code | basis:declared | asof:fis12-2.0.3 | grounded-in:fis12-2.0.3:errors/index.yaml#code[80230].code
anchor.error-code | isa | anchor.runtime-concept | basis:authority | asof:fis12-2.0.3 | grounded-in:workbench:scripts/onix-request-lifecycle.md
anchor.error-code | wasGeneratedBy | anchor.nack-response | basis:observed-live | asof:fis12-2.0.3 | grounded-in:workbench:scripts/onix-request-lifecycle.md
anchor.search | has-slot | anchor.api-endpoint | basis:declared | asof:fis12-2.0.3 | grounded-in:fis12-2.0.3:specs/openapi.yaml#paths[/search].post.operationId
anchor.on-search | has-slot | anchor.api-endpoint | basis:declared | asof:fis12-2.0.3 | grounded-in:fis12-2.0.3:specs/openapi.yaml#paths[/on_search].post.operationId
anchor.select | has-slot | anchor.api-endpoint | basis:declared | asof:fis12-2.0.3 | grounded-in:fis12-2.0.3:specs/openapi.yaml#paths[/select].post.operationId
anchor.on-select | has-slot | anchor.api-endpoint | basis:declared | asof:fis12-2.0.3 | grounded-in:fis12-2.0.3:specs/openapi.yaml#paths[/on_select].post.operationId
anchor.init | has-slot | anchor.api-endpoint | basis:declared | asof:fis12-2.0.3 | grounded-in:fis12-2.0.3:specs/openapi.yaml#paths[/init].post.operationId
anchor.on-init | has-slot | anchor.api-endpoint | basis:declared | asof:fis12-2.0.3 | grounded-in:fis12-2.0.3:specs/openapi.yaml#paths[/on_init].post.operationId
anchor.confirm | has-slot | anchor.api-endpoint | basis:declared | asof:fis12-2.0.3 | grounded-in:fis12-2.0.3:specs/openapi.yaml#paths[/confirm].post.operationId
anchor.on-confirm | has-slot | anchor.api-endpoint | basis:declared | asof:fis12-2.0.3 | grounded-in:fis12-2.0.3:specs/openapi.yaml#paths[/on_confirm].post.operationId
anchor.update | has-slot | anchor.api-endpoint | basis:declared | asof:fis12-2.0.3 | grounded-in:fis12-2.0.3:specs/openapi.yaml#paths[/update].post.operationId
anchor.on-update | has-slot | anchor.api-endpoint | basis:declared | asof:fis12-2.0.3 | grounded-in:fis12-2.0.3:specs/openapi.yaml#paths[/on_update].post.operationId
anchor.status | has-slot | anchor.api-endpoint | basis:declared | asof:fis12-2.0.3 | grounded-in:fis12-2.0.3:specs/openapi.yaml#paths[/status].post.operationId
anchor.on-status | has-slot | anchor.api-endpoint | basis:declared | asof:fis12-2.0.3 | grounded-in:fis12-2.0.3:specs/openapi.yaml#paths[/on_status].post.operationId
anchor.issue | has-slot | anchor.api-endpoint | basis:declared | asof:fis12-2.0.3 | grounded-in:fis12-2.0.3:specs/openapi.yaml#paths[/issue].post.operationId
anchor.on-issue | has-slot | anchor.api-endpoint | basis:declared | asof:fis12-2.0.3 | grounded-in:fis12-2.0.3:specs/openapi.yaml#paths[/on_issue].post.operationId
anchor.on-issue-status | has-slot | anchor.api-endpoint | basis:declared | asof:fis12-2.0.3 | grounded-in:fis12-2.0.3:specs/openapi.yaml#paths[/on_issue_status].post.operationId
anchor.api-endpoint | isa | anchor.runtime-concept | basis:authority | asof:fis12-2.0.3 | grounded-in:workbench:scripts/onix-request-lifecycle.md
anchor.fis12-2-0-3 | not-has-slot | anchor.shared-schema-components | basis:declared | asof:fis12-2.0.3 | grounded-in:fis12-2.0.3:index.yaml#components
anchor.search-request | has-slot | anchor.search-intent | basis:declared | asof:fis12-2.0.3 | grounded-in:fis12-2.0.3:specs/openapi.yaml#paths[/search].post.requestBody.content[application/json].schema.properties.message.properties.intent
anchor.search-request | has-slot | anchor.context-domain | basis:declared | asof:fis12-2.0.3 | grounded-in:fis12-2.0.3:specs/openapi.yaml#paths[/search].post.requestBody.content[application/json].schema.properties.context.properties.domain
anchor.search-request | has-slot | anchor.context-city | basis:declared | asof:fis12-2.0.3 | grounded-in:fis12-2.0.3:specs/openapi.yaml#paths[/search].post.requestBody.content[application/json].schema.properties.context.properties.location.properties.city
anchor.search-request | isa | anchor.beckn-object | basis:declared | asof:fis12-2.0.3 | grounded-in:fis12-2.0.3:specs/openapi.yaml#paths[/search].post.requestBody.content[application/json].schema
anchor.search-request | requires | anchor.subscriber-auth | basis:declared | asof:fis12-2.0.3 | grounded-in:fis12-2.0.3:index.yaml#security[0]
anchor.tag | has-slot | anchor.tag-list-field | basis:declared | asof:fis12-2.0.3 | !untethered
anchor.fulfillment-state | has-slot | anchor.state-descriptor-field | basis:declared | asof:fis12-2.0.3 | !untethered
anchor.xinput-form | has-slot | anchor.multiple-submissions-field | basis:declared | asof:fis12-2.0.3 | !untethered
anchor.multiple-submissions-field | constrains | anchor.xinput-form-response | basis:declared | asof:fis12-2.0.3 | !untethered

# fis10-giftcard-2.1.0 KB atoms (structural, book-generic)

anchor.provider | isa | anchor.beckn-object | basis:declared | asof:fis10-giftcard-2.1.0 | grounded-in:fis10-giftcard-2.1.0:specs/openapi.yaml#components.schemas.Provider
anchor.item | isa | anchor.beckn-object | basis:declared | asof:fis10-giftcard-2.1.0 | grounded-in:fis10-giftcard-2.1.0:specs/openapi.yaml#components.schemas.Item
anchor.payment | isa | anchor.beckn-object | basis:declared | asof:fis10-giftcard-2.1.0 | grounded-in:fis10-giftcard-2.1.0:specs/openapi.yaml#components.schemas.Payment
anchor.fulfillment | isa | anchor.beckn-object | basis:declared | asof:fis10-giftcard-2.1.0 | grounded-in:fis10-giftcard-2.1.0:specs/openapi.yaml#components.schemas.Fulfillment
anchor.search | isa | anchor.action | basis:declared | asof:fis10-giftcard-2.1.0 | grounded-in:fis10-giftcard-2.1.0:actions/index.yaml#supportedActions.search
anchor.on-search | isa | anchor.action | basis:declared | asof:fis10-giftcard-2.1.0 | grounded-in:fis10-giftcard-2.1.0:actions/index.yaml#supportedActions.on_search
anchor.select | isa | anchor.action | basis:declared | asof:fis10-giftcard-2.1.0 | grounded-in:fis10-giftcard-2.1.0:actions/index.yaml#supportedActions.select
anchor.on-select | isa | anchor.action | basis:declared | asof:fis10-giftcard-2.1.0 | grounded-in:fis10-giftcard-2.1.0:actions/index.yaml#supportedActions.on_select
anchor.init | isa | anchor.action | basis:declared | asof:fis10-giftcard-2.1.0 | grounded-in:fis10-giftcard-2.1.0:actions/index.yaml#supportedActions.init
anchor.on-init | isa | anchor.action | basis:declared | asof:fis10-giftcard-2.1.0 | grounded-in:fis10-giftcard-2.1.0:actions/index.yaml#supportedActions.on_init
anchor.confirm | isa | anchor.action | basis:declared | asof:fis10-giftcard-2.1.0 | grounded-in:fis10-giftcard-2.1.0:actions/index.yaml#supportedActions.confirm
anchor.on-confirm | isa | anchor.action | basis:declared | asof:fis10-giftcard-2.1.0 | grounded-in:fis10-giftcard-2.1.0:actions/index.yaml#supportedActions.on_confirm
anchor.status | isa | anchor.action | basis:declared | asof:fis10-giftcard-2.1.0 | grounded-in:fis10-giftcard-2.1.0:actions/index.yaml#supportedActions.status
anchor.on-status | isa | anchor.action | basis:declared | asof:fis10-giftcard-2.1.0 | grounded-in:fis10-giftcard-2.1.0:actions/index.yaml#supportedActions.on_status
anchor.on-update | isa | anchor.action | basis:declared | asof:fis10-giftcard-2.1.0 | grounded-in:fis10-giftcard-2.1.0:actions/index.yaml#supportedActions.on_update
anchor.cancel | isa | anchor.action | basis:declared | asof:fis10-giftcard-2.1.0 | grounded-in:fis10-giftcard-2.1.0:actions/index.yaml#supportedActions.cancel
anchor.on-cancel | isa | anchor.action | basis:declared | asof:fis10-giftcard-2.1.0 | grounded-in:fis10-giftcard-2.1.0:actions/index.yaml#supportedActions.on_cancel
anchor.update | isa | anchor.action | basis:declared | asof:fis10-giftcard-2.1.0 | grounded-in:fis10-giftcard-2.1.0:actions/index.yaml#supportedActions.update
anchor.search | isa | anchor.transaction-entry | basis:declared | asof:fis10-giftcard-2.1.0 | grounded-in:fis10-giftcard-2.1.0:actions/index.yaml#supportedActions.null
anchor.transaction-entry | isa | anchor.runtime-concept | basis:authority | asof:fis10-giftcard-2.1.0 | grounded-in:workbench:frames/flow-state-machine.md
anchor.search | precedes | anchor.on-search | basis:declared | asof:fis10-giftcard-2.1.0 | grounded-in:fis10-giftcard-2.1.0:flows/gift-card/Seller_Cancellation.yaml#steps[on_search]
anchor.on-search | precedes | anchor.select | basis:declared | asof:fis10-giftcard-2.1.0 | grounded-in:fis10-giftcard-2.1.0:flows/gift-card/Seller_Cancellation.yaml#steps[select]
anchor.select | precedes | anchor.on-select | basis:declared | asof:fis10-giftcard-2.1.0 | grounded-in:fis10-giftcard-2.1.0:flows/gift-card/Seller_Cancellation.yaml#steps[on_select]
anchor.on-select | precedes | anchor.init | basis:declared | asof:fis10-giftcard-2.1.0 | grounded-in:fis10-giftcard-2.1.0:flows/gift-card/Seller_Cancellation.yaml#steps[init]
anchor.init | precedes | anchor.on-init | basis:declared | asof:fis10-giftcard-2.1.0 | grounded-in:fis10-giftcard-2.1.0:flows/gift-card/Seller_Cancellation.yaml#steps[on_init]
anchor.on-init | precedes | anchor.confirm | basis:declared | asof:fis10-giftcard-2.1.0 | grounded-in:fis10-giftcard-2.1.0:flows/gift-card/Seller_Cancellation.yaml#steps[confirm]
anchor.confirm | precedes | anchor.on-confirm | basis:declared | asof:fis10-giftcard-2.1.0 | grounded-in:fis10-giftcard-2.1.0:flows/gift-card/Seller_Cancellation.yaml#steps[on_confirm]
anchor.on-confirm | precedes | anchor.on-cancel | basis:declared | asof:fis10-giftcard-2.1.0 | grounded-in:fis10-giftcard-2.1.0:flows/gift-card/Seller_Cancellation.yaml#steps[on_cancel]
anchor.search | requires | "provider-id" | basis:inferred | asof:fis10-giftcard-2.1.0

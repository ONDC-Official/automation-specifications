# fis12-2.3.0 KB atoms (structural, book-generic)

anchor.provider | isa | anchor.beckn-object | basis:declared | asof:fis12-2.3.0 | grounded-in:fis12-2.3.0:specs/openapi.yaml#components.schemas.Provider
anchor.item | isa | anchor.beckn-object | basis:declared | asof:fis12-2.3.0 | grounded-in:fis12-2.3.0:specs/openapi.yaml#components.schemas.Item
anchor.payment | isa | anchor.beckn-object | basis:declared | asof:fis12-2.3.0 | grounded-in:fis12-2.3.0:specs/openapi.yaml#components.schemas.Payment
anchor.fulfillment | isa | anchor.beckn-object | basis:declared | asof:fis12-2.3.0 | grounded-in:fis12-2.3.0:specs/openapi.yaml#components.schemas.Fulfillment
anchor.search | isa | anchor.action | basis:declared | asof:fis12-2.3.0 | grounded-in:fis12-2.3.0:actions/index.yaml#supportedActions.search
anchor.on-search | isa | anchor.action | basis:declared | asof:fis12-2.3.0 | grounded-in:fis12-2.3.0:actions/index.yaml#supportedActions.on_search
anchor.select | isa | anchor.action | basis:declared | asof:fis12-2.3.0 | grounded-in:fis12-2.3.0:actions/index.yaml#supportedActions.select
anchor.on-select | isa | anchor.action | basis:declared | asof:fis12-2.3.0 | grounded-in:fis12-2.3.0:actions/index.yaml#supportedActions.on_select
anchor.init | isa | anchor.action | basis:declared | asof:fis12-2.3.0 | grounded-in:fis12-2.3.0:actions/index.yaml#supportedActions.init
anchor.on-init | isa | anchor.action | basis:declared | asof:fis12-2.3.0 | grounded-in:fis12-2.3.0:actions/index.yaml#supportedActions.on_init
anchor.confirm | isa | anchor.action | basis:declared | asof:fis12-2.3.0 | grounded-in:fis12-2.3.0:actions/index.yaml#supportedActions.confirm
anchor.on-confirm | isa | anchor.action | basis:declared | asof:fis12-2.3.0 | grounded-in:fis12-2.3.0:actions/index.yaml#supportedActions.on_confirm
anchor.status | isa | anchor.action | basis:declared | asof:fis12-2.3.0 | grounded-in:fis12-2.3.0:actions/index.yaml#supportedActions.status
anchor.on-status | isa | anchor.action | basis:declared | asof:fis12-2.3.0 | grounded-in:fis12-2.3.0:actions/index.yaml#supportedActions.on_status
anchor.on-update | isa | anchor.action | basis:declared | asof:fis12-2.3.0 | grounded-in:fis12-2.3.0:actions/index.yaml#supportedActions.on_update
anchor.cancel | isa | anchor.action | basis:declared | asof:fis12-2.3.0 | grounded-in:fis12-2.3.0:actions/index.yaml#supportedActions.cancel
anchor.on-cancel | isa | anchor.action | basis:declared | asof:fis12-2.3.0 | grounded-in:fis12-2.3.0:actions/index.yaml#supportedActions.on_cancel
anchor.track | isa | anchor.action | basis:declared | asof:fis12-2.3.0 | grounded-in:fis12-2.3.0:actions/index.yaml#supportedActions.track
anchor.on-track | isa | anchor.action | basis:declared | asof:fis12-2.3.0 | grounded-in:fis12-2.3.0:actions/index.yaml#supportedActions.on_track
anchor.update | isa | anchor.action | basis:declared | asof:fis12-2.3.0 | grounded-in:fis12-2.3.0:actions/index.yaml#supportedActions.update
anchor.issue | isa | anchor.action | basis:declared | asof:fis12-2.3.0 | grounded-in:fis12-2.3.0:actions/index.yaml#supportedActions.issue
anchor.on-issue | isa | anchor.action | basis:declared | asof:fis12-2.3.0 | grounded-in:fis12-2.3.0:actions/index.yaml#supportedActions.on_issue
anchor.on-issue-status | isa | anchor.action | basis:declared | asof:fis12-2.3.0 | grounded-in:fis12-2.3.0:actions/index.yaml#supportedActions.on_issue_status
anchor.search | isa | anchor.transaction-entry | basis:declared | asof:fis12-2.3.0 | grounded-in:fis12-2.3.0:actions/index.yaml#supportedActions.null
anchor.init | isa | anchor.transaction-entry | basis:declared | asof:fis12-2.3.0 | grounded-in:fis12-2.3.0:actions/index.yaml#supportedActions.null
anchor.transaction-entry | isa | anchor.runtime-concept | basis:authority | asof:fis12-2.3.0 | grounded-in:workbench:frames/flow-state-machine.md
anchor.search | precedes | anchor.on-search | basis:declared | asof:fis12-2.3.0 | grounded-in:fis12-2.3.0:flows/LAMF/master_search.yaml#steps[on_Search_1]
anchor.search | requires | "provider-id" | basis:inferred | asof:fis12-2.3.0

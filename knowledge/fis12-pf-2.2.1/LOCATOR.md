# LOCATOR — fis12-pf-2.2.1

"Where do I find X" for the `fis12-pf-2.2.1` book (invariant 18). Committed and
hand-maintained. Config paths are relative to
`configs/release-eks-FIS12-PF-2.2.1/config/`; KB paths are relative to this directory.

## 1. Where do I find a fact?

| I want… | look in | how |
|---|---|---|
| any committed fact | [`atoms.md`](atoms.md) | grep the handle: `grep 'anchor.checklists-tag' atoms.md` |
| what a shared meaning *is* | [`anchors/index.md`](anchors/index.md) | one row per interned meaning → canonical meaning + config ground |
| the node for a flow / action / concept | [`frames/`](frames/) | filename **is** the handle: `frames/<id>.md` |
| what is *not yet* committed | [`candidate-units.md`](candidate-units.md) | Stage E buffer — **never** cite as fact |
| the counts, flow list, action list | [`INDEX.md`](INDEX.md) | navigation surface |
| the format rules | `.claude/skills/ondc-kb-seed/kb-format/` | `unit.md` · `anchor.md` · `vocabularies.md` · `invariants.md` |

Closed world: if it is not a unit in `atoms.md`, it is **not known** — not false.
Frames carry no facts of their own; their bodies are deliberately light.

## 2. Where do I find a rule in the config?

| I want… | config file | node path |
|---|---|---|
| the domain / version / use-case list | `index.yaml` | `info.domain` · `info.version` · `info.x-usecases` |
| which flows exist, and their tags | `flows/index.yaml` | `flows[<flow-id>]` → `.tags` `.usecase` `.type` `.description` `.config.$ref` |
| the step sequence of one flow | `flows/PURCHASE FINANCE/<File>.yaml` | `steps[<action_id>]` → `.api` `.owner` `.responseFor` `.unsolicited` |
| the mock payload a step sends | `flows/PURCHASE FINANCE/<File>.yaml` | `steps[<action_id>].mock.defaultPayload` |
| session data a step saves for later steps | `flows/PURCHASE FINANCE/<File>.yaml` | `steps[<action_id>].mock.saveData` |
| which action may legally follow which | `actions/index.yaml` | `supportedActions.<action>` |
| async predecessor / transaction partners | `actions/index.yaml` | `apiProperties.<action>` |
| required fields, enums, tag groups per action | `validations/index.yaml` | `_TESTS_.<action>[<TEST_NAME>]._RETURN_` |
| an enum's allowed values | `validations/index.yaml` | `…[<TEST_NAME>].enumList` |
| a tag group's required members | `validations/index.yaml` | `…[<TEST_NAME>].tagPath` · `.validTags` · `.validValues` |
| a form field's meaning, owner, required-ness | `attributes/PURCHASE_FINANCE.yaml` | `attribute_set.html_form.<field>._description` |
| a request/response field's meaning | `attributes/PURCHASE_FINANCE.yaml` | `attribute_set.<action>.<path>._description` |
| the error code table | `errors/index.yaml` | `code[<code>]` → `.Event` `.Description` `.From` |
| the API surface (paths + schemas) | `specs/openapi.yaml` | `paths./<action>` · `components` |
| the narrative overview / actors | `docs/overview.md` | `#summary` · `#real-world-actors` · `#use-cases` · `#key-concepts` |

## 3. Where do I find a flow?

`INDEX.md` has the full table. The three coordinates of a flow handle:

| I have… | I get the flow by… |
|---|---|
| a `flows/index.yaml` id (`Purchase_Finance_With_AA`) | frame `flow.pf-<variant>` — see `INDEX.md` §Flows |
| a frame handle (`flow.pf-with-aa`) | interned meaning `anchor.flow-pf-with-aa` in `anchors/index.md` |
| an anchor handle (`anchor.flow-pf-with-aa`) | facts: `grep 'anchor.flow-pf-with-aa' atoms.md` |

The frame ↔ anchor mapping is uniform for all 22 flows:
`flow.pf-<variant>` ⇄ `anchor.flow-pf-<variant>`, with `<variant>` one of
`sr-with-aa` · `sr-with-aa-igm` · `sr-without-aa` · `sr-without-aa-cancellation` ·
`sr-without-aa-foreclosure` · `sr-without-aa-igm` · `sr-without-aa-missed-emi` ·
`sr-without-aa-pre-part-payment` · `with-aa` · `with-aa-cancellation` ·
`with-aa-foreclosure` · `with-aa-igm` · `with-aa-missed-emi` · `with-aa-multiple-offer` ·
`with-aa-pre-part-payment` · `without-aa` · `without-aa-cancellation` ·
`without-aa-foreclosure` · `without-aa-igm` · `without-aa-missed-emi` ·
`without-aa-multiple-offer` · `without-aa-pre-part-payment`.

The same 1:1 rule holds for actions: frame `action.<a>` ⇄ anchor `anchor.<a>`
(`action.on-search` ⇄ `anchor.on-search`, and so on for all 19).

## 4. Where do I find a concept?

| topic | frame | interned as | config ground |
|---|---|---|---|
| the domain itself | `dom.fis12` | `anchor.domain-ondc-fis12` | `index.yaml#info.domain` |
| the use case | `usecase.purchase-finance` | `anchor.purchase-finance` | `attributes/PURCHASE_FINANCE.yaml#meta.use_case_id` |
| Account Aggregator consent journeys | `concept.aa-consent-journey` | `anchor.aa-consent-journey` | `flows/index.yaml#flows[Purchase_Finance_With_AA].tags` |
| form-driven (no AA) journeys | `concept.non-aa-journey` | `anchor.non-aa-journey` | `flows/index.yaml#flows[Purchase_Finance_Without_AA].tags` |
| one-redirection journeys | `concept.single-redirection-journey` | `anchor.single-redirection-journey` | `flows/index.yaml#flows[Purchase_Finance_Single_Redirection_Without_AA].tags` |
| the playground flow type | `concept.playground-flow` | `anchor.playground-flow` | `flows/index.yaml#flows[Purchase_Finance_With_AA].type` |
| buyer-app HTML forms | `concept.html-form` | `anchor.html-form` | `attributes/PURCHASE_FINANCE.yaml#attribute_set.html_form` |
| lender-hosted dynamic forms | `concept.dynamic-form` | `anchor.dynamic-form` | `attributes/PURCHASE_FINANCE.yaml#attribute_set.dynamic_form` |
| the beckn context block | `concept.beckn-context` | `anchor.beckn-context` | `validations/index.yaml#_TESTS_.search[SEARCH_CONTEXT]` |
| the PURCHASE_FINANCE category code | `concept.purchase-finance-category` | `anchor.category-purchase-finance` | `validations/index.yaml#_TESTS_.search[SEARCH_CATEGORY_CODE]` |
| payment / settlement terms | `concept.payment-terms` | `anchor.bpp-terms-tag` | `validations/index.yaml#_TESTS_.on_search[ON_SEARCH_PAYMENT]` |
| lending service provider info | `concept.lsp-info` | `anchor.lsp-info-tag` | `validations/index.yaml#_TESTS_.on_search[ON_SEARCH_PROVIDER_LSP_INFO]` |
| provider contacts / grievance officer | `concept.contact-info` | `anchor.contact-info-tag` | `validations/index.yaml#_TESTS_.on_search[ON_SEARCH_PROVIDER_CONTACT_INFO]` |
| the LOAN catalog item | `concept.loan-item` | `anchor.loan-item` | `validations/index.yaml#_TESTS_.on_search[ON_SEARCH_ITEMS]` |
| interest rate / tenure / subvention | `concept.loan-info-tag` | `anchor.info-tag` | `validations/index.yaml#_TESTS_.on_select[ON_SELECT_ITEMS_INFO_TAG]` |
| KYC / eMandate / eSign checklists | `concept.checklists` | `anchor.checklists-tag` | `validations/index.yaml#_TESTS_.on_select[ON_SELECT_ITEMS_CHECKLISTS_TAG]` |
| quote and its breakup | `concept.quote` | `anchor.quote` | `validations/index.yaml#_TESTS_.on_select[ON_SELECT_QUOTE]` |
| loan fulfillment states | `concept.loan-fulfillment` | `anchor.loan-fulfillment` | `validations/index.yaml#_TESTS_.on_init[ON_INIT_FULFILLMENTS]` |
| down payment / pre-order payment | `concept.pre-order-payment` | `anchor.pre-order-payment` | `validations/index.yaml#_TESTS_.on_init[ON_INIT_PAYMENTS_PRE_ORDER]` |
| EMI schedule / post-fulfillment payment | `concept.post-fulfillment-payment` | `anchor.post-fulfillment-payment` | `validations/index.yaml#_TESTS_.on_confirm[ON_CONFIRM_PAYMENTS_POST_FULFILLMENT]` |
| cancellation terms | `concept.cancellation-terms` | `anchor.cancellation-terms` | `validations/index.yaml#_TESTS_.on_confirm[ON_CONFIRM_CANCELLATION_TERMS]` |
| loan agreement / documents | `concept.loan-documents` | `anchor.document-code-enum` | `validations/index.yaml#_TESTS_.on_confirm[ON_CONFIRM_DOCUMENTS]` |
| what an `update` may target | `concept.update-target` | `anchor.update-target` | `validations/index.yaml#_TESTS_.update[UPDATE_TARGET]` |
| grievances under IGM 1.0.0 | `concept.igm-1-0-0` | `anchor.igm-1-0-0` | `validations/index.yaml#_TESTS_.issue[ISSUE_VALIDATION_VERSION_100]` |
| grievances under IGM 2.0.0 | `concept.igm-2-0-0` | `anchor.igm-2-0-0` | `validations/index.yaml#_TESTS_.issue[ISSUE_VALIDATION_VERSION_200]` |
| error codes | `concept.error-code` | `anchor.error-code` | `errors/index.yaml#code` |
| the legal next-action graph | `concept.action-state-machine` | `anchor.pf-action-state-machine` | `actions/index.yaml#supportedActions` |
| async predecessors / partners | `concept.transaction-partner` | — | `actions/index.yaml#apiProperties` |
| the borrower | `concept.borrower` | `anchor.borrower` | `docs/overview.md#real-world-actors` |
| the lender | `concept.finance-provider` | `anchor.finance-provider` | `docs/overview.md#real-world-actors` |
| the merchant | `concept.goods-seller` | `anchor.goods-seller` | `docs/overview.md#real-world-actors` |
| the Account Aggregator | `concept.account-aggregator` | `anchor.account-aggregator` | `docs/overview.md#key-concepts` |
| EMI repayment | `concept.emi-repayment` | `anchor.emi-repayment` | `docs/overview.md#key-concepts` |

## 5. Where do I find a change / a gap?

| I want… | do this |
|---|---|
| everything grounded in one config file | `grep 'grounded-in:fis12-pf-2.2.1:validations/index.yaml' atoms.md` |
| what breaks if a config node moves | grep the node path in `atoms.md` **and** `anchors/index.md` |
| units with no ground | `grep '!untethered' atoms.md` |
| unverified guesses (never assert these) | `grep 'basis:inferred' atoms.md` |
| anchors still awaiting a config ground | rows with `-` in the `grounded-in` column of `anchors/index.md` |
| revalidate the book | `python3 .claude/skills/ondc-kb-seed/tools/validate_kb.py knowledge/fis12-pf-2.2.1` |

## 6. Known traps in this config

| trap | detail |
|---|---|
| `meta.flowId` is not the flow id | 7 of 22 flow files carry a `meta.flowId` that differs from their `flows/index.yaml` `id`, and 3 `meta.flowId` values are each shared by **two** flows (`…Without_AA_Cancellation`, `…Without_AA_Loan_Foreclosure_playground`, `…Without_AA_Pre_Part_Payment_playground_flow`). `#meta.flowId` is therefore not a unique key here: flow frames are grounded at `flows/index.yaml#flows[<id>]` instead. |
| `track` / `on_track` are declared but unused | present in `actions/index.yaml#supportedActions`, but no flow step and no `_TESTS_` battery uses them, and `specs/openapi.yaml` has no `/track` path. |
| error table is broader than the use case | `errors/index.yaml#code` carries transit-shaped codes (`91201`–`91216`); only `30001`, `30008`, `50001` carry grounded anchors in this book — `anchor.error-91216` is registered with no config ground. |
| IGM flows are not `REPORTABLE` | the four `…_With_IGM(v-1.0.0)` entries have `REPORTABLE` commented out in `flows/index.yaml`. |

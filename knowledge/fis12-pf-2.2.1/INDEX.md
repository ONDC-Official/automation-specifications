# INDEX — fis12-pf-2.2.1

Navigation surface for the `fis12-pf-2.2.1` KB book (invariant 18). Committed and
hand-maintained. Counts are what `tools/validate_kb.py` reports for this book root.

| axis | value |
|---|---|
| book id | `fis12-pf-2.2.1` |
| domain | `ONDC:FIS12` — `index.yaml#info.domain` |
| version | `2.2.1` — `index.yaml#info.version` |
| use case | `PURCHASE FINANCE` (single) — `attributes/PURCHASE_FINANCE.yaml#meta.use_case_id` |
| config release | `configs/release-eks-FIS12-PF-2.2.1/config/` |
| atoms | 515 |
| anchors | 206 |
| frames | 74 — 22 flow · 19 action · 33 concept |
| ADRs | 0 |

## Files

| file | what it holds |
|---|---|
| [`atoms.md`](atoms.md) | the committed units — every fact in this book |
| [`anchors/index.md`](anchors/index.md) | interned meanings registry: handle → meaning → config ground |
| [`frames/`](frames/) | one light frame per flow, protocol action, and recurring concept |
| [`candidate-units.md`](candidate-units.md) | Stage E candidates buffer — **not** committed fact |
| [`LOCATOR.md`](LOCATOR.md) | "where do I find X" lookup table |

## Flows covered (22)

All 22 flows are `type: playground`, `usecase: PURCHASE FINANCE`, registered in
`flows/index.yaml#flows[<id>]` with the flow body under `flows/PURCHASE FINANCE/`.

| frame | flows/index.yaml id | variant |
|---|---|---|
| [`flow.pf-with-aa`](frames/flow.pf-with-aa.md) | `Purchase_Finance_With_AA` | WITH_AA · multi-redirection |
| [`flow.pf-with-aa-cancellation`](frames/flow.pf-with-aa-cancellation.md) | `Purchase_Finance_With_AA_Cancellation` | WITH_AA · cancellation tail |
| [`flow.pf-with-aa-foreclosure`](frames/flow.pf-with-aa-foreclosure.md) | `Purchase_Finance_With_AA_Loan_Foreclosure` | WITH_AA · foreclosure tail |
| [`flow.pf-with-aa-missed-emi`](frames/flow.pf-with-aa-missed-emi.md) | `Purchase_Finance_With_AA_Missed_EMI_Payment` | WITH_AA · missed EMI tail |
| [`flow.pf-with-aa-multiple-offer`](frames/flow.pf-with-aa-multiple-offer.md) | `Purchase_Finance_With_AA_Multiple_Offer` | WITH_AA · multiple offers |
| [`flow.pf-with-aa-pre-part-payment`](frames/flow.pf-with-aa-pre-part-payment.md) | `Purchase_Finance_With_AA_Pre_Part_Payment` | WITH_AA · pre-part payment tail |
| [`flow.pf-with-aa-igm`](frames/flow.pf-with-aa-igm.md) | `Purchase_Finance_With_AA_With_IGM(v-1.0.0)` | WITH_AA · IGM 1.0.0 |
| [`flow.pf-without-aa`](frames/flow.pf-without-aa.md) | `Purchase_Finance_Without_AA` | WITHOUT_AA · multi-redirection |
| [`flow.pf-without-aa-cancellation`](frames/flow.pf-without-aa-cancellation.md) | `Purchase_Finance_Without_AA_Cancellation` | WITHOUT_AA · cancellation tail |
| [`flow.pf-without-aa-foreclosure`](frames/flow.pf-without-aa-foreclosure.md) | `Purchase_Finance_Without_AA_Loan_Foreclosure` | WITHOUT_AA · foreclosure tail |
| [`flow.pf-without-aa-missed-emi`](frames/flow.pf-without-aa-missed-emi.md) | `Purchase_Finance_Without_AA_Missed_EMI_Payment` | WITHOUT_AA · missed EMI tail |
| [`flow.pf-without-aa-multiple-offer`](frames/flow.pf-without-aa-multiple-offer.md) | `Purchase_Finance_Without_AA_Multiple_Offer` | WITHOUT_AA · multiple offers |
| [`flow.pf-without-aa-pre-part-payment`](frames/flow.pf-without-aa-pre-part-payment.md) | `Purchase_Finance_Without_AA_Pre_Part_Payment` | WITHOUT_AA · pre-part payment tail |
| [`flow.pf-without-aa-igm`](frames/flow.pf-without-aa-igm.md) | `Purchase_Finance_Without_AA_With_IGM(v-1.0.0)` | WITHOUT_AA · IGM 1.0.0 |
| [`flow.pf-sr-with-aa`](frames/flow.pf-sr-with-aa.md) | `Purchase_Finance_Single_Redirection_With_AA` | WITH_AA · single redirection |
| [`flow.pf-sr-with-aa-igm`](frames/flow.pf-sr-with-aa-igm.md) | `Purchase_Finance_Single_Redirection_With_AA_With_IGM(v-1.0.0)` | single redirection · IGM 1.0.0 |
| [`flow.pf-sr-without-aa`](frames/flow.pf-sr-without-aa.md) | `Purchase_Finance_Single_Redirection_Without_AA` | WITHOUT_AA · single redirection |
| [`flow.pf-sr-without-aa-cancellation`](frames/flow.pf-sr-without-aa-cancellation.md) | `Purchase_Finance_Single_Redirection_Without_AA_Cancellation` | single redirection · cancellation tail |
| [`flow.pf-sr-without-aa-foreclosure`](frames/flow.pf-sr-without-aa-foreclosure.md) | `Purchase_Finance_Single_Redirection_Without_AA_Loan_Foreclosure` | single redirection · foreclosure tail |
| [`flow.pf-sr-without-aa-missed-emi`](frames/flow.pf-sr-without-aa-missed-emi.md) | `Purchase_Finance_Single_Redirection_Without_AA_Missed_EMI_Payment` | single redirection · missed EMI tail |
| [`flow.pf-sr-without-aa-pre-part-payment`](frames/flow.pf-sr-without-aa-pre-part-payment.md) | `Purchase_Finance_Single_Redirection_Without_AA_Pre_Part_Payment` | single redirection · pre-part payment tail |
| [`flow.pf-sr-without-aa-igm`](frames/flow.pf-sr-without-aa-igm.md) | `Purchase_Finance_Single_Redirection_Without_AA_With_IGM(v-1.0.0)` | single redirection · IGM 1.0.0 |

## Actions covered (19)

Every action is declared at `actions/index.yaml#supportedActions.<action>`; the allowed
next-action graph is [`concept.action-state-machine`](frames/concept.action-state-machine.md).

`owner` is the value carried on the action's flow steps (`steps[].owner`); `—` means the
action is declared in `supportedActions` but never appears as a step in any flow of this
book. `_TESTS_` says whether `validations/index.yaml#_TESTS_` carries a battery for it.

| frame | action | owner | `_TESTS_` |
|---|---|---|---|
| [`action.search`](frames/action.search.md) | `search` | BAP | yes |
| [`action.on-search`](frames/action.on-search.md) | `on_search` | BPP | yes |
| [`action.select`](frames/action.select.md) | `select` | BAP | yes |
| [`action.on-select`](frames/action.on-select.md) | `on_select` | BPP | yes |
| [`action.init`](frames/action.init.md) | `init` | BAP | yes |
| [`action.on-init`](frames/action.on-init.md) | `on_init` | BPP | yes |
| [`action.confirm`](frames/action.confirm.md) | `confirm` | BAP | yes |
| [`action.on-confirm`](frames/action.on-confirm.md) | `on_confirm` | BPP | yes |
| [`action.status`](frames/action.status.md) | `status` | BAP | yes |
| [`action.on-status`](frames/action.on-status.md) | `on_status` | BPP | yes |
| [`action.update`](frames/action.update.md) | `update` | BAP | yes |
| [`action.on-update`](frames/action.on-update.md) | `on_update` | BPP | yes |
| [`action.cancel`](frames/action.cancel.md) | `cancel` | BAP | yes |
| [`action.on-cancel`](frames/action.on-cancel.md) | `on_cancel` | BPP | yes |
| [`action.track`](frames/action.track.md) | `track` | — | **no** |
| [`action.on-track`](frames/action.on-track.md) | `on_track` | — | **no** |
| [`action.issue`](frames/action.issue.md) | `issue` | BAP | yes |
| [`action.on-issue`](frames/action.on-issue.md) | `on_issue` | BPP | yes |
| [`action.on-issue-status`](frames/action.on-issue-status.md) | `on_issue_status` | BPP | yes |

## Concepts (33)

Domain axis — journey variants and loan semantics:
[`dom.fis12`](frames/dom.fis12.md) ·
[`usecase.purchase-finance`](frames/usecase.purchase-finance.md) ·
[`concept.aa-consent-journey`](frames/concept.aa-consent-journey.md) ·
[`concept.non-aa-journey`](frames/concept.non-aa-journey.md) ·
[`concept.single-redirection-journey`](frames/concept.single-redirection-journey.md) ·
[`concept.playground-flow`](frames/concept.playground-flow.md) ·
[`concept.html-form`](frames/concept.html-form.md) ·
[`concept.dynamic-form`](frames/concept.dynamic-form.md) ·
[`concept.purchase-finance-category`](frames/concept.purchase-finance-category.md) ·
[`concept.loan-item`](frames/concept.loan-item.md) ·
[`concept.loan-info-tag`](frames/concept.loan-info-tag.md) ·
[`concept.checklists`](frames/concept.checklists.md) ·
[`concept.quote`](frames/concept.quote.md) ·
[`concept.loan-fulfillment`](frames/concept.loan-fulfillment.md) ·
[`concept.loan-documents`](frames/concept.loan-documents.md) ·
[`concept.cancellation-terms`](frames/concept.cancellation-terms.md) ·
[`concept.update-target`](frames/concept.update-target.md) ·
[`concept.payment-terms`](frames/concept.payment-terms.md) ·
[`concept.pre-order-payment`](frames/concept.pre-order-payment.md) ·
[`concept.post-fulfillment-payment`](frames/concept.post-fulfillment-payment.md) ·
[`concept.lsp-info`](frames/concept.lsp-info.md) ·
[`concept.contact-info`](frames/concept.contact-info.md) ·
[`concept.igm-1-0-0`](frames/concept.igm-1-0-0.md) ·
[`concept.igm-2-0-0`](frames/concept.igm-2-0-0.md) ·
[`concept.borrower`](frames/concept.borrower.md) ·
[`concept.finance-provider`](frames/concept.finance-provider.md) ·
[`concept.goods-seller`](frames/concept.goods-seller.md) ·
[`concept.account-aggregator`](frames/concept.account-aggregator.md) ·
[`concept.emi-repayment`](frames/concept.emi-repayment.md)

Protocol axis:
[`concept.beckn-context`](frames/concept.beckn-context.md) ·
[`concept.action-state-machine`](frames/concept.action-state-machine.md) ·
[`concept.transaction-partner`](frames/concept.transaction-partner.md) ·
[`concept.error-code`](frames/concept.error-code.md)

## Contract

Format contract lives outside this book, in
`.claude/skills/ondc-kb-seed/kb-format/`:
[`unit.md`](../../.claude/skills/ondc-kb-seed/kb-format/unit.md) ·
[`anchor.md`](../../.claude/skills/ondc-kb-seed/kb-format/anchor.md) ·
[`vocabularies.md`](../../.claude/skills/ondc-kb-seed/kb-format/vocabularies.md) ·
[`invariants.md`](../../.claude/skills/ondc-kb-seed/kb-format/invariants.md)

Gate: `python3 .claude/skills/ondc-kb-seed/tools/validate_kb.py knowledge/fis12-pf-2.2.1`

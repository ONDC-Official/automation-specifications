# INDEX — fis12-2.0.3

Committed navigation surface for this book (invariant 18). Counts are of committed nodes, not of
config lines.

| field | value |
|---|---|
| book id | `fis12-2.0.3` |
| domain | `ONDC:FIS12` (lending) |
| config release | `configs/release-eks-FIS12-2.0.3/config` |
| units (atoms) | 567 |
| anchors (registry rows) | 248 |
| frames | 52 |
| use cases | `GOLD LOAN`, `PERSONAL LOAN` |

## Files

| file | what it holds |
|---|---|
| [`atoms.md`](atoms.md) | every committed unit — the only fact-truth in this book |
| [`anchors/index.md`](anchors/index.md) | anchor registry: handle → canonical meaning → config ground |
| [`frames/`](frames/) | one file per framed node: `<id>.md`, frontmatter + light body |
| [`candidate-units.md`](candidate-units.md) | Stage E staging buffer; **not** committed fact — not parsed by the validator |
| [`LOCATOR.md`](LOCATOR.md) | "where do I find X" lookup |

## Flows covered

Ten flow frames, one per flow carried by this book's units. Grounded at
`flows/index.yaml#flows[<id>].id`.

| frame | config flow id | use case |
|---|---|---|
| [`anchor.flow-personal-loan-offline`](frames/anchor.flow-personal-loan-offline.md) | `Personal_Loan_Offline` | PERSONAL LOAN |
| [`anchor.flow-personal-loan-single-redirection`](frames/anchor.flow-personal-loan-single-redirection.md) | `Personal_Loan_Single_Redirection` | PERSONAL LOAN |
| [`anchor.flow-personal-loan-dedupe-check`](frames/anchor.flow-personal-loan-dedupe-check.md) | `Personal_Loan_Dedupe_Check` | PERSONAL LOAN |
| [`anchor.flow-personal-loan-foreclosure-offline`](frames/anchor.flow-personal-loan-foreclosure-offline.md) | `Personal_Loan_Foreclosure_Offline` | PERSONAL LOAN |
| [`anchor.flow-personal-loan-missed-emi-offline`](frames/anchor.flow-personal-loan-missed-emi-offline.md) | `Personal_Loan_missed_emi_payment_Offline` | PERSONAL LOAN |
| [`anchor.flow-personal-loan-pre-part-payment-offline`](frames/anchor.flow-personal-loan-pre-part-payment-offline.md) | `Personal_Loan_Pre_Part_Payment_Offline` | PERSONAL LOAN |
| [`anchor.flow-personal-loan-offline-igm-1-0-0`](frames/anchor.flow-personal-loan-offline-igm-1-0-0.md) | `Personal_Loan_Offline_With_IGM(v-1.0.0)` | PERSONAL LOAN |
| [`anchor.flow-personal-loan-single-redirection-igm-1-0-0`](frames/anchor.flow-personal-loan-single-redirection-igm-1-0-0.md) | `Personal_Loan_Single_Redirection_With_IGM(v-1.0.0)` | PERSONAL LOAN |
| [`anchor.flow-gold-loan-offline`](frames/anchor.flow-gold-loan-offline.md) | `Gold_Loan_Offline` | GOLD LOAN |
| [`anchor.flow-gold-loan-offline-igm-1-0-0`](frames/anchor.flow-gold-loan-offline-igm-1-0-0.md) | `Gold_Loan_Offline_with_igm_1.0.0` | GOLD LOAN |

Three flows are declared in `flows/index.yaml` but carry **no unit and no anchor row** in this book,
so they have no frame (closed-world: absence = not-known, invariant 19):
`Personal_Loan_Foreclosure_Single_Redirection`, `Personal_Loan_Missed_EMI_Single_Redirection`,
`Personal_Loan_Pre_Part_Payment_Single_Redirection`.

## Actions covered

Fifteen protocol actions, one frame each, grounded at
`actions/index.yaml#supportedActions.<action>`. Successor sets and `apiProperties`
(`async_predecessor`, `transaction_partner`) are carried as units in `atoms.md`.

| frame | action | frame | action |
|---|---|---|---|
| [`anchor.search`](frames/anchor.search.md) | `search` | [`anchor.on-search`](frames/anchor.on-search.md) | `on_search` |
| [`anchor.select`](frames/anchor.select.md) | `select` | [`anchor.on-select`](frames/anchor.on-select.md) | `on_select` |
| [`anchor.init`](frames/anchor.init.md) | `init` | [`anchor.on-init`](frames/anchor.on-init.md) | `on_init` |
| [`anchor.confirm`](frames/anchor.confirm.md) | `confirm` | [`anchor.on-confirm`](frames/anchor.on-confirm.md) | `on_confirm` |
| [`anchor.update`](frames/anchor.update.md) | `update` | [`anchor.on-update`](frames/anchor.on-update.md) | `on_update` |
| [`anchor.status`](frames/anchor.status.md) | `status` | [`anchor.on-status`](frames/anchor.on-status.md) | `on_status` |
| [`anchor.issue`](frames/anchor.issue.md) | `issue` | [`anchor.on-issue`](frames/anchor.on-issue.md) | `on_issue` |
| [`anchor.on-issue-status`](frames/anchor.on-issue-status.md) | `on_issue_status` | | |

## Concept frames

Recurring meanings that earn a full rendering; every other interned meaning stays a registry row in
[`anchors/index.md`](anchors/index.md) (anchors do not require frames).

| layer | frames |
|---|---|
| domain | `anchor.ondc-fis12` · `anchor.personal-loan-usecase` · `anchor.gold-loan-usecase` · `anchor.loan-journey` · `anchor.credit-product` · `anchor.loan-servicing-event` · `anchor.single-redirection` · `anchor.html-form` · `anchor.dynamic-form` · `anchor.checklist-codes` · `anchor.igm-1-0-0` · `anchor.igm-2-0-0` · `anchor.grievance` · `anchor.payment-time-labels` · `anchor.search-category-codes` · `anchor.unsolicited-callback` |
| protocol | `anchor.bap` · `anchor.bpp` · `anchor.xinput` · `anchor.xinput-form-response` · `anchor.catalog` · `anchor.provider` · `anchor.loan-item` · `anchor.search-intent` · `anchor.quote` · `anchor.error-code` |

One further frame predates this pass:
[`anchor.event-data-validation-failed-input-data-failed-validation-`](frames/anchor.event-data-validation-failed-input-data-failed-validation-.md).

## Gate

```
python3 .claude/skills/ondc-kb-seed/tools/validate_kb.py knowledge/fis12-2.0.3
VALID — 567 atoms, 52 frames, 248 anchors, 0 ADRs, isa-DAG ok
```

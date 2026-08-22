# fis12-2.3.0 — book index

Navigation surface for this book (invariant 18). Nothing here is a fact; every fact is a unit in
[`atoms.md`](atoms.md).

| | |
|---|---|
| book id | `fis12-2.3.0` |
| domain | `ONDC:FIS12` — lending |
| release | `2.3.0` (branch `draft-FIS12-2.3.0`, status DRAFT for both use cases) |
| config | [`configs/release-eks-FIS12-2.3.0/config/`](../../configs/release-eks-FIS12-2.3.0/config/) |
| atoms | **1039** |
| anchors | **463** |
| frames | **116** |
| ADRs | 0 |
| validator | `python3 .claude/skills/ondc-kb-seed/tools/validate_kb.py knowledge/fis12-2.3.0` |

## Files

| file | what it holds |
|---|---|
| [`atoms.md`](atoms.md) | the committed units — the only fact-truth in this book |
| [`anchors/index.md`](anchors/index.md) | registry of 463 interned meanings: handle → meaning → config ground |
| [`frames/`](frames/) | 116 light frames (flows, protocol actions, recurring concepts) |
| [`candidate-units.md`](candidate-units.md) | pre-commit staging; **not** committed fact |
| [`LOCATOR.md`](LOCATOR.md) | "where do I find X" |

## Use cases

| use case | status | attribute book |
|---|---|---|
| LAMF LOAN | DRAFT | `attributes/LAMF_LOAN.yaml` |
| BUSINESS LOAN | DRAFT | `attributes/BUSINESS_LOAN.yaml` (commented out of `attributes/index.yaml` upstream — no atoms) |

## Flows covered (10 framed)

Order is the flow book's `meta.order` within each use case.

| frame | use case | config |
|---|---|---|
| [`anchor.flow-lamf-master-search`](frames/anchor.flow-lamf-master-search.md) | LAMF LOAN | `flows/LAMF/master_search.yaml` |
| [`anchor.flow-lamf-credit-line-mfc`](frames/anchor.flow-lamf-credit-line-mfc.md) | LAMF LOAN | `flows/LAMF/lamf_credit_line_with_mfc_single_redirection.yaml` |
| [`anchor.flow-lamf-credit-line-mfc-igm-1-0-0`](frames/anchor.flow-lamf-credit-line-mfc-igm-1-0-0.md) | LAMF LOAN | `flows/LAMF/lamf_credit_line_with_mfc_single_redirection._with_igm_1.0.0.yaml` |
| [`anchor.flow-business-master-search`](frames/anchor.flow-business-master-search.md) | BUSINESS LOAN | `flows/BUSINESS_LOAN/master_search.yaml` |
| [`anchor.flow-business-term-loan-without-aa`](frames/anchor.flow-business-term-loan-without-aa.md) | BUSINESS LOAN | `flows/BUSINESS_LOAN/business_term_loan_without_aa.yaml` |
| [`anchor.flow-business-term-loan-with-file-upload`](frames/anchor.flow-business-term-loan-with-file-upload.md) | BUSINESS LOAN | `flows/BUSINESS_LOAN/business_term_loan_with_file_upload.yaml` |
| [`anchor.flow-business-term-loan-with-aa`](frames/anchor.flow-business-term-loan-with-aa.md) | BUSINESS LOAN | `flows/BUSINESS_LOAN/business_term_loan_with_aa.yaml` |
| [`anchor.flow-business-term-loan-with-aa-igm-1-0-0`](frames/anchor.flow-business-term-loan-with-aa-igm-1-0-0.md) | BUSINESS LOAN | `flows/BUSINESS_LOAN/business_term_loan_with_aa_with_igm_1.0.0.yaml` |
| [`anchor.flow-business-term-loan-without-aa-igm-1-0-0`](frames/anchor.flow-business-term-loan-without-aa-igm-1-0-0.md) | BUSINESS LOAN | `flows/BUSINESS_LOAN/business_term_loan_without_aa_with_igm_1.0.0.yaml` |
| [`anchor.flow-business-term-loan-with-file-upload-igm-1-0-0`](frames/anchor.flow-business-term-loan-with-file-upload-igm-1-0-0.md) | BUSINESS LOAN | `flows/BUSINESS_LOAN/business_term_loan_with_file_upload_with_igm_1.0.0.yaml` |

**Not framed:** `dedupe_check` is active in `flows/index.yaml` but carries no unit in `atoms.md`, so it
has no frame (a frame must trace to ≥1 unit — invariant 12). Gap, not a decision.
The three `business_term_loan_with_offline_online_*` flows are commented out upstream and out of scope.

## Actions covered (19 framed, `kind: class`, `layer: protocol`)

Grounded at `actions/index.yaml#supportedActions.<action>`; the successor sets and
`apiProperties` (async predecessor / transaction partner) live as units in `atoms.md`.

| BAP-side | BPP callback |
|---|---|
| [`search`](frames/anchor.search.md) | [`on_search`](frames/anchor.on-search.md) |
| [`select`](frames/anchor.select.md) | [`on_select`](frames/anchor.on-select.md) |
| [`init`](frames/anchor.init.md) | [`on_init`](frames/anchor.on-init.md) |
| [`confirm`](frames/anchor.confirm.md) | [`on_confirm`](frames/anchor.on-confirm.md) |
| [`status`](frames/anchor.status.md) | [`on_status`](frames/anchor.on-status.md) |
| [`update`](frames/anchor.update.md) | [`on_update`](frames/anchor.on-update.md) |
| [`cancel`](frames/anchor.cancel.md) | [`on_cancel`](frames/anchor.on-cancel.md) |
| [`track`](frames/anchor.track.md) | [`on_track`](frames/anchor.on-track.md) |
| [`issue`](frames/anchor.issue.md) | [`on_issue`](frames/anchor.on-issue.md), [`on_issue_status`](frames/anchor.on-issue-status.md) |

Transaction entry points (`supportedActions."null"`): `search`, `init`, `select`.

## Concept frames (87)

Selected by recurrence — an anchor earns a frame here when it is touched by **≥5 units** in
`atoms.md` and has a verified config ground. The other ~350 anchors stay registry rows only
(anchor.md: "light, not a frame").

| group | frames |
|---|---|
| protocol structure | `anchor.action`, `anchor.api-properties`, `anchor.async-predecessor`, `anchor.transaction-partner`, `anchor.protocol-endpoint`, `anchor.beckn-object`, `anchor.context`, `anchor.context-requirement`, `anchor.l1-validation`, `anchor.error-code`, `anchor.unsolicited-callback` |
| participants | `anchor.bap`, `anchor.bpp`, `anchor.transaction-actor` |
| beckn objects | `anchor.provider`, `anchor.item`, `anchor.payment`, `anchor.fulfillment`, `anchor.fulfillment-state`, `anchor.fulfillment-stop`, `anchor.stop-status`, `anchor.quote`, `anchor.quote-breakup-item`, `anchor.order-id`, `anchor.order-status`, `anchor.order-document`, `anchor.cancellation-term`, `anchor.payment-status`, `anchor.payment-collector`, `anchor.search-intent`, `anchor.customer-person` |
| xinput / forms | `anchor.xinput`, `anchor.form-response`, `anchor.form-submission-id`, `anchor.form-status`, `anchor.search-form`, `anchor.on-select-form`, `anchor.required-xinput-fields`*, `anchor.on-action-items`*, `anchor.redefined-validation-anchor` |
| IGM / grievance | `anchor.grievance-protocol`, `anchor.igm-1-0-0`, `anchor.igm-2-0-0`, `anchor.igm-context-requirement`, `anchor.issue-open-state` |
| book identity | `anchor.ondc-fis12`, `anchor.fis12-2-3-0`, `anchor.lamf-loan-usecase`, `anchor.business-loan-usecase`, `anchor.attribute-book`, `anchor.loan-journey`, `anchor.mandatory-flow`, `anchor.reportable-flow` |
| loan taxonomy | `anchor.loan-category` + 16 category members (`anchor.loan`, `anchor.lamf`, `anchor.mfc`, `anchor.term-loan`, `anchor.credit-line`, `anchor.business`, `anchor.secured-personal`, `anchor.unsecured-personal`, `anchor.consumer-invoice-financing`, `anchor.other-business-entity`, `anchor.mutual-fund`, `anchor.gst`, `anchor.banking`, `anchor.rta`, `anchor.offers`, `anchor.additional-data`) |
| lending concepts | `anchor.account-aggregator`, `anchor.aa-consent`, `anchor.bureau-verification`, `anchor.mutual-fund-pledge`, `anchor.lien-marking`, `anchor.loan-agreement`, `anchor.emandate`, `anchor.checklist-stage`, `anchor.single-redirection` |
| tag groups | `anchor.loan-info-tag`, `anchor.loan-offer-tag`, `anchor.pledge-requirement-tag`, `anchor.contact-info-tag`, `anchor.lsp-info-tag`, `anchor.bap-term-tag`, `anchor.account-detail-tag`, `anchor.payment-breakup-tag` |

\* **Ambiguous by construction.** `REQUIRED_XINPUT_FIELDS` and `ON_ACTION_ITEMS` are each declared
more than once as a YAML `&anchor` in `validations/index.yaml`; under js-yaml semantics a later
declaration shadows the earlier one. Neither frame interns one definition — both point at
`anchor.redefined-validation-anchor` and record the ambiguity. **A human must decide** which
definition is authoritative per call site.

## Shape of the atom set

| axis | counts |
|---|---|
| basis | `declared` 849 · `authority` 156 · `derived` 33 · `inferred` 1 |
| top relations | `isa` 438 · `requires` 162 · `precedes` 91 · `has-slot` 79 · `sent-by` 45 · `scoped-to` 43 |
| explicit negatives | 73 units (`not-requires` 33, `not-isa` 15, `not-wasInformedBy` 12, `not-has-slot` 9, …) |
| `!untethered` | 7 |
| grounded in config | `validations/index.yaml` 337 · `flows/**` 133 · `actions/index.yaml` 133 · `docs/**` 113 · `attributes/**` 112 · `specs/openapi.yaml` 76 · `errors/index.yaml` 69 · `index.yaml` 13 |

## Contract

Format contract lives in
[`.claude/skills/ondc-kb-seed/kb-format/`](../../.claude/skills/ondc-kb-seed/kb-format/) —
[unit](../../.claude/skills/ondc-kb-seed/kb-format/unit.md) ·
[anchor](../../.claude/skills/ondc-kb-seed/kb-format/anchor.md) ·
[vocabularies](../../.claude/skills/ondc-kb-seed/kb-format/vocabularies.md) ·
[invariants](../../.claude/skills/ondc-kb-seed/kb-format/invariants.md).

> `validations/index.yaml` in this book only parses under **js-yaml** anchor semantics. PyYAML raises
> `ComposerError` on its redefined anchors — load it with
> `.claude/skills/ondc-kb-seed/tools/_yaml.py`.

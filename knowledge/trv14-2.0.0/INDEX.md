# INDEX — trv14-2.0.0

Navigation surface for the `trv14-2.0.0` KB book (invariant 18). Committed and
hand-maintained; nothing here is a fact — facts live in `atoms.md`.

| | |
|---|---|
| book id | `trv14-2.0.0` |
| domain | `ONDC:TRV14` · version `2.0.0` |
| config release | `configs/release-eks-TRV14-2.0.0/config/` |
| atoms | 751 |
| anchors | 237 |
| frames | 48 (16 flow · 18 action · 14 concept) |
| ADRs | 0 |

## Files

| file | what it holds |
|---|---|
| [`atoms.md`](atoms.md) | every committed unit for this book — the only fact surface |
| [`anchors/index.md`](anchors/index.md) | the interned-meaning registry (handle → meaning → config ground) |
| [`frames/`](frames/) | one light frame per flow, protocol action, and recurring concept |
| [`candidate-units.md`](candidate-units.md) | pre-commit staging; **not** committed fact |
| [`LOCATOR.md`](LOCATOR.md) | "where do I find X" lookup table |

## Flows covered (16)

All 16 flows belong to the single use case `unreserved-entry-pass`. Every flow is
grounded at `flows/unreserved-entry-pass/<file>.yaml#meta.flowId`.

| frame | config `flowId` | flow file | steps | tags |
|---|---|---|---|---|
| [`flow.cancellation-rejected`](frames/flow.cancellation-rejected.md) | `Cancellation Rejected` | `Cancellation_Rejected.yaml` | 12 | WORKBENCH, MANDATORY |
| [`flow.incremental-pull`](frames/flow.incremental-pull.md) | `incremental_pull_journey` | `incremental_pull_journey.yaml` | 4 | WORKBENCH, MANDATORY |
| [`flow.order-level-forms-culture-heritage`](frames/flow.order-level-forms-culture-heritage.md) | `purchase_journey_order_level_forms_culture_heritage` | `purchase_journey_order_level_forms_culture_heritage.yaml` | 15 | PRAMAAN, MANDATORY, REPORTABLE, WORKBENCH |
| [`flow.purchase-with-form`](frames/flow.purchase-with-form.md) | `purchase_journey_with_form` | `purchase_journey_with_form.yaml` | 15 | PRAMAAN, MANDATORY, REPORTABLE, WORKBENCH |
| [`flow.purchase-with-form-multiple-tickets`](frames/flow.purchase-with-form-multiple-tickets.md) | `purchase_journey_with_form_Multiple_Tickets` | `purchase_journey_with_form_Multiple_Tickets.yaml` | 15 | PRAMAAN, MANDATORY, REPORTABLE, WORKBENCH |
| [`flow.purchase-without-form`](frames/flow.purchase-without-form.md) | `purchase_journey_without_form` | `purchase_journey_without_form.yaml` | 13 | PRAMAAN, MANDATORY, REPORTABLE, WORKBENCH |
| [`flow.purchase-without-form-multiple-tickets`](frames/flow.purchase-without-form-multiple-tickets.md) | `purchase_journey_without_form_Multiple_Tickets` | `purchase_journey_without_form_Multiple_Tickets.yaml` | 12 | PRAMAAN, MANDATORY, REPORTABLE, WORKBENCH |
| [`flow.purchase-igm`](frames/flow.purchase-igm.md) | `purchase_journey_without_form_with_IGM(v-2.0.0)` | `purchase_journey_without_form_with_IGM_v-2_0_0_.yaml` | 21 | PRAMAAN, MANDATORY, REPORTABLE, WORKBENCH |
| [`flow.purchase-igm-no-action`](frames/flow.purchase-igm-no-action.md) | `purchase_journey_without_form_with_IGM_No_Action(v-2.0.0)` | `purchase_journey_without_form_with_IGM_No_Action_v-2_0_0_.yaml` | 18 | PRAMAAN, MANDATORY, REPORTABLE, WORKBENCH |
| [`flow.purchase-igm-rejection`](frames/flow.purchase-igm-rejection.md) | `purchase_journey_without_form_with_IGM_Rejection(v-2.0.0)` | `purchase_journey_without_form_with_IGM_Rejection_v-2_0_0_.yaml` | 24 | PRAMAAN, MANDATORY, REPORTABLE, WORKBENCH |
| [`flow.seller-app-pagination`](frames/flow.seller-app-pagination.md) | `seller_app_pagination_journey` | `seller_app_pagination_journey.yaml` | 4 | WORKBENCH, MANDATORY |
| [`flow.technical-cancellation`](frames/flow.technical-cancellation.md) | `technical_cancellation` | `technical_cancellation.yaml` | 16 | PRAMAAN, MANDATORY, REPORTABLE, WORKBENCH |
| [`flow.technical-cancellation-with-form`](frames/flow.technical-cancellation-with-form.md) | `technical_cancellation_with_form` | `technical_cancellation_with_form.yaml` | 19 | PRAMAAN, MANDATORY, REPORTABLE, WORKBENCH |
| [`flow.user-cancellation-full`](frames/flow.user-cancellation-full.md) | `User Cancellation (Full)` | `User_Cancellation__Full_.yaml` | 14 | PRAMAAN, MANDATORY, REPORTABLE, WORKBENCH |
| [`flow.user-cancellation-full-with-form`](frames/flow.user-cancellation-full-with-form.md) | `User_Cancellation_FULL_With_Form` | `User_Cancellation_FULL_With_Form.yaml` | 17 | PRAMAAN, MANDATORY, REPORTABLE, WORKBENCH |
| [`flow.user-cancellation-partial`](frames/flow.user-cancellation-partial.md) | `user_cancellation_partial` | `user_cancellation_partial.yaml` | 14 | WORKBENCH, MANDATORY |

## Actions covered (18)

Every action is grounded at `actions/index.yaml#supportedActions.<action>`; its successor
set and `apiProperties` sit at the same file.

| frame | action | frame | action |
|---|---|---|---|
| [`action.search`](frames/action.search.md) | `search` | [`action.on-search`](frames/action.on-search.md) | `on_search` |
| [`action.select`](frames/action.select.md) | `select` | [`action.on-select`](frames/action.on-select.md) | `on_select` |
| [`action.init`](frames/action.init.md) | `init` | [`action.on-init`](frames/action.on-init.md) | `on_init` |
| [`action.confirm`](frames/action.confirm.md) | `confirm` | [`action.on-confirm`](frames/action.on-confirm.md) | `on_confirm` |
| [`action.status`](frames/action.status.md) | `status` | [`action.on-status`](frames/action.on-status.md) | `on_status` |
| [`action.cancel`](frames/action.cancel.md) | `cancel` | [`action.on-cancel`](frames/action.on-cancel.md) | `on_cancel` |
| [`action.track`](frames/action.track.md) | `track` | [`action.on-track`](frames/action.on-track.md) | `on_track` |
| [`action.update`](frames/action.update.md) | `update` | [`action.on-update`](frames/action.on-update.md) | `on_update` |
| [`action.issue`](frames/action.issue.md) | `issue` | [`action.on-issue`](frames/action.on-issue.md) | `on_issue` |

## Concepts (14)

| frame | layer | grounded in |
|---|---|---|
| [`dom.trv14`](frames/dom.trv14.md) | domain | `index.yaml` |
| [`usecase.unreserved-entry-pass`](frames/usecase.unreserved-entry-pass.md) | domain | `attributes/unreserved_entry_pass.yaml` |
| [`concept.entry-pass-item`](frames/concept.entry-pass-item.md) | domain | `validations/index.yaml` |
| [`concept.abstract-item`](frames/concept.abstract-item.md) | domain | `validations/index.yaml` |
| [`concept.xinput-item-form`](frames/concept.xinput-item-form.md) | protocol | `validations/index.yaml` |
| [`concept.html-form`](frames/concept.html-form.md) | protocol | `flows/unreserved-entry-pass/purchase_journey_with_form.yaml` |
| [`concept.authorization`](frames/concept.authorization.md) | domain | `specs/openapi.yaml` |
| [`concept.igm`](frames/concept.igm.md) | protocol | `specs/openapi.yaml` |
| [`concept.soft-cancel`](frames/concept.soft-cancel.md) | domain | `validations/index.yaml` |
| [`concept.cancellation-reason-id`](frames/concept.cancellation-reason-id.md) | domain | `validations/index.yaml` |
| [`concept.cancellation-terms`](frames/concept.cancellation-terms.md) | domain | `validations/index.yaml` |
| [`concept.order-status`](frames/concept.order-status.md) | domain | `validations/index.yaml` |
| [`concept.fare-policy-tag`](frames/concept.fare-policy-tag.md) | domain | `validations/index.yaml` |
| [`concept.pramaan-suite`](frames/concept.pramaan-suite.md) | protocol | `flows/index.yaml` |

## Scope notes

- `configs/release-eks-TRV14-2.0.0/config/attributes/unreserved-entry-pass.yaml` (hyphen
  spelling) is an out-of-scope orphan twin of the in-scope `unreserved_entry_pass.yaml`.
  Nothing in this book grounds to it.
- `errors/index.yaml` registers only 3 codes (90201–90203); other codes referenced by this
  book (e.g. `93201`) appear only inside flow mocks. See `LOCATOR.md`.

## Validate

```
python3 .claude/skills/ondc-kb-seed/tools/validate_kb.py knowledge/trv14-2.0.0
```

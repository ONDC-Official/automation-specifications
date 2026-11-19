# ONDC:TRV11 2.0.0 — Release Notes

Notable changes in this version of the Metro use case, newest first.

## Unreleased

### Added
- **Error codes** aligned with the contract (`x-errorcodes`) in `config/errors/index.yaml`:
  - `91217` Payment reference id duplicate (BPP - AFCS)
  - `91218` Sub system failure, non-retryable (BPP - AFCS)
  - `91219` Sub system failure, request timeout, retryable (BPP - AFCS)
- `docs/overview_metro.md`: Metro integration guide with the happy path, ticket variants, cancellation and IGM flows, data model, checklists, error code reference and contract links.

### Changed
- **Error codes `91212`–`91216` now follow the contract.** Their meanings changed:

  | Code | Previously | Now (contract) |
  |---|---|---|
  | `91212` | Invalid transaction | Cancellation Window Closed |
  | `91213` | Stale transaction | Order in progress or existing |
  | `91214` | Wrong fare while booking ticket | Duplicate API call |
  | `91215` | Item not found | Active booking exists (BPP - AFCS) |
  | `91216` | Cannot cancel used ticket | Ticket already used (BPP - AFCS) |

  The previous definitions are no longer in the error list. Seller Apps returning the old meanings should move to the contract codes.
- Select/init item id validation fixed at L2.
- Metro validator checks already enforced by L1 were dropped.
- `bpp_id` / `bpp_uri` input defaults are now session-based, with environment placeholders.
- Attributes: enums removed, enum types changed to `string`, and `required` now refers to `validations/index.yaml`.

### Fixed
- Settlement amount, buyer finder fee and `ttl` regex validations across flows.
- Confirm and `on_confirm` validations; fulfillment logic for select and confirm.
- Technical cancellation flow, including the `000` reason code and the without-search-and-select variant.
- Partial cancellation flow and its `update` validation.
- IGM flow issues (rejection flow, issue level enum, fulfillment, descriptions).
- Billing issue across all flows.

## Earlier in 2.0.0 development

- Seller offline cancellation flow.
- Partial cancellation flows, with and without search and select.
- IGM 1.0.0 and IGM 2.0.0 variants of the SJT flow (need-more-info, rejection and no-action paths).
- `_WITHOUT_SEARCH_ND_SELECT` variants of all order and cancellation flows.
- Use case lifecycle status (`x-status`).
- TRV11 2.0.0 moved to the playground.

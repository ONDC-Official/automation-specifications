# INDEX — fis13-health-2.0.1

Navigation surface for this book (invariant 18). Facts live in `atoms.md`; interned meanings in
`anchors/index.md`; frames are light declared nodes.

| field | value |
|---|---|
| book id (`asof`) | `fis13-health-2.0.1` |
| domain | `ONDC:FIS13` — health & motor insurance |
| spec version | 2.0.1 |
| config release | `configs/release-eks-FIS13-HEALTH-2.0.1/config/` |
| atoms | 604 |
| anchors | 131 |
| frames | 66 |
| ADRs | 0 |

Basis mix: 589 `declared` · 13 `authority` · 2 `inferred` · 6 units carry `!untethered`.
Top relations: `isa` 196 · `requires` 82 · `scoped-to` 69 · `has-slot` 66 · `sent-by` 50 ·
`precedes` 42 · `part-of` 32. Explicit negatives present (`not-requires`, `not-isa`,
`not-scoped-to`, `not-part-of`, `not-has-slot`).

## Use cases

| frame | config ground |
|---|---|
| `usecase.health-insurance` | `attributes/HEALTH_INSURANCE.yaml#meta.use_case_id` |
| `usecase.motor-insurance` | `attributes/MOTOR_INSURANCE.yaml#meta.use_case_id` |

## Journeys

`journey.policy-application` · `journey.policy-claim` · `journey.policy-renewal` ·
`journey.policy-cancellation` — all grounded at `flows/index.yaml#flows`.

## Flows covered (16 — every flow in `flows/index.yaml`)

All 16 are tagged `WORKBENCH`, `MANDATORY`, `REPORTABLE` in the config.

| frame | config flow id | use case |
|---|---|---|
| `flow.health-insurance-application-individual` | `Health_Insurance_Application(Individual)` | HEALTH INSURANCE |
| `flow.health-insurance-application-family` | `Health_Insurance_Application(Family)` | HEALTH INSURANCE |
| `flow.health-insurance-application-pre-order-individual` | `Health_Insurance_Application(PRE-ORDER-Individual)` | HEALTH INSURANCE |
| `flow.health-insurance-application-pre-order-family` | `Health_Insurance_Application(PRE-ORDER-Family)` | HEALTH INSURANCE |
| `flow.health-insurance-application-pre-order-individual-with-manualreview` | `Health_Insurance_Application(PRE-ORDER-Individual-With-ManualReview)` | HEALTH INSURANCE |
| `flow.health-insurance-application-pre-order-family-with-manualreview` | `Health_Insurance_Application(PRE-ORDER-Family-With-ManualReview)` | HEALTH INSURANCE |
| `flow.claim-health-insurance-individual` | `Claim_Health_Insurance(Individual)` | HEALTH INSURANCE |
| `flow.claim-health-insurance-family` | `Claim_Health_Insurance(Family)` | HEALTH INSURANCE |
| `flow.renew-health-insurance-individual` | `Renew_Health_Insurance(Individual)` | HEALTH INSURANCE |
| `flow.renew-health-insurance-family` | `Renew_Health_Insurance(Family)` | HEALTH INSURANCE |
| `flow.cancel-health-insurance-individual` | `Cancel_Health_Insurance(Individual)` | HEALTH INSURANCE |
| `flow.cancel-health-insurance-family` | `Cancel_Health_Insurance(Family)` | HEALTH INSURANCE |
| `flow.motor-insurance-application` | `Motor_Insurance_Application` | MOTOR INSURANCE |
| `flow.motor-insurance-application-pre-order` | `Motor_Insurance_Application(PRE-ORDER)` | MOTOR INSURANCE |
| `flow.claim-motor-insurance` | `Claim_Motor_Insurance` | MOTOR INSURANCE |
| `flow.cancel-motor-insurance` | `Cancel_Motor_Insurance` | MOTOR INSURANCE |

## Actions covered (16 — every key in `actions/index.yaml#supportedActions`)

`action.search` · `action.on-search` · `action.select` · `action.on-select` · `action.init` ·
`action.on-init` · `action.confirm` · `action.on-confirm` · `action.status` · `action.on-status` ·
`action.update` · `action.on-update` · `action.cancel` · `action.on-cancel` · `action.track` ·
`action.on-track`

Each is grounded at `actions/index.yaml#supportedActions.<action>`.

Notes carried by `atoms.md`, not by these frames:
- `rating` and `support` exist as `specs/openapi.yaml#paths` entries but are `not-isa anchor.action`
  — they are absent from `supportedActions`, so they get no action frame.
- `track` / `on_track` are declared actions but appear in no flow step
  (`anchor.track | not-part-of | anchor.insurance-journey`).

## Error codes (8 — `errors/index.yaml#code`)

`error.code-81201` … `error.code-81208`. All are `From: BPP`.

## Domain concepts (19)

`concept.policy-lifecycle` · `concept.pre-order-application` · `concept.deferred-underwriting` ·
`concept.insurance-agency-bpp` · `concept.manual-review` · `concept.html-form` ·
`concept.dynamic-form` · `concept.xinput` · `concept.unsolicited-callback` ·
`concept.individual-cover` · `concept.family-cover` · `concept.policy` ·
`concept.policy-document` · `concept.insurance-category` · `concept.add-on-cover` ·
`concept.fulfillment-state` · `concept.mandatory-flow` · `concept.validation-rule` ·
`concept.error-code`

Plus the domain root `dom.fis13` (`index.yaml#info.domain`).

## Links

- [`atoms.md`](atoms.md) — the committed units (the only fact-truth).
- [`anchors/index.md`](anchors/index.md) — interned meanings, handle → ground.
- [`frames/`](frames/) — 66 light declared nodes.
- [`candidate-units.md`](candidate-units.md) — pre-promotion buffer, not committed fact.
- [`LOCATOR.md`](LOCATOR.md) — "where do I find X".
- Contract: `.claude/skills/ondc-kb-seed/kb-format/` (`unit.md`, `anchor.md`, `vocabularies.md`,
  `invariants.md`).
- Validator: `python3 .claude/skills/ondc-kb-seed/tools/validate_kb.py knowledge/fis13-health-2.0.1`

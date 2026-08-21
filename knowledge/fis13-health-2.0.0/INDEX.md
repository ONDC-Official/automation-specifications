# fis13-health-2.0.0 — INDEX

Navigation surface for this KB book (invariant 18). The book is **`asof`-isolated**: every
fact here is stated for `fis13-health-2.0.0` only — never read across to another release.

**Looking for a specific rule, field, enum or error? Start at [`LOCATOR.md`](LOCATOR.md)** —
it maps *"where do I find X"* onto the exact KB node and config node-path.

| | |
|---|---|
| book id | `fis13-health-2.0.0` |
| domain / version | `ONDC:FIS13` 2.0.0 |
| config book | `configs/release-eks-FIS13-HEALTH-2.0.0/config/` |
| atoms | 770 (`atoms.md`) |
| anchors | 438 (`anchors/index.md`) |
| frames | 67 (`frames/*.md`) |
| Stage E candidate units | 710 (`candidate-units.md`) — all promoted into `atoms.md` |

## Files

| file | what it holds | edit rule |
|---|---|---|
| `atoms.md` | the committed units — every fact in this book | source of truth; frames never restate it |
| `anchors/index.md` | interned schematic meanings, handle → meaning → config ground | registry rows only; an anchor needs no frame |
| `frames/*.md` | declared nodes for the significant entities (domain, use cases, actions, flows) | light bodies: one declaration + `Grounded at:` |
| `candidate-units.md` | the Stage E staging list; every line here is already an atom | staging, never queried as fact |
| `INDEX.md` · `LOCATOR.md` | navigation | hand-maintained |

## Frames

| kind · layer | handle root | count |
|---|---|---|
| concept · domain | `dom.fis13` | 1 |
| concept · domain | `usecase.*` (insurance products) | 5 |
| class · protocol | `action.*` | 19 |
| instance · domain | `flow.*` | 42 |

Errors, tags, forms, enums and schema fragments are **anchors, not frames** — they are
interned once in `anchors/index.md` and referenced by handle (see `kb-format/anchor.md`).

## Use cases covered (5)

| frame | use case | attribute dictionary | interned anchor |
|---|---|---|---|
| `usecase.health-insurance` | `HEALTH INSURANCE` | `attributes/HEALTH_INSURANCE.yaml` | `anchor.usecase-health-insurance` |
| `usecase.motor-insurance` | `MOTOR INSURANCE` | `attributes/MOTOR_INSURANCE.yaml` | `anchor.usecase-motor-insurance` |
| `usecase.accidental-insurance` | `ACCIDENTAL INSURANCE` | `attributes/accidental_insurance.yaml` | `anchor.usecase-accidental-insurance` |
| `usecase.hospicash-insurance` | `HOSPICASH INSURANCE` | `attributes/hospicash_insurance.yaml` | `anchor.usecase-hospicash-insurance` |
| `usecase.transit-insurance` | `TRANSIT INSURANCE` | `attributes/transit_insurance.yaml` | `anchor.usecase-transit-insurance` |

## Actions covered (19)

Grounded at `actions/index.yaml#supportedActions.<action>` — that node is also the action
state machine (each key lists its legal successors). Per-action validation lives under
`validations/index.yaml#_TESTS_.<action>`.

| frame | protocol action | interned anchor |
|---|---|---|
| `action.search` | `search` | `anchor.search` |
| `action.on-search` | `on_search` | `anchor.on-search` |
| `action.select` | `select` | `anchor.select` |
| `action.on-select` | `on_select` | `anchor.on-select` |
| `action.init` | `init` | `anchor.init` |
| `action.on-init` | `on_init` | `anchor.on-init` |
| `action.confirm` | `confirm` | `anchor.confirm` |
| `action.on-confirm` | `on_confirm` | `anchor.on-confirm` |
| `action.status` | `status` | `anchor.status` |
| `action.on-status` | `on_status` | `anchor.on-status` |
| `action.on-update` | `on_update` | `anchor.on-update` |
| `action.cancel` | `cancel` | `anchor.cancel` |
| `action.on-cancel` | `on_cancel` | `anchor.on-cancel` |
| `action.track` | `track` | `anchor.track` |
| `action.on-track` | `on_track` | `anchor.on-track` |
| `action.update` | `update` | `anchor.update` |
| `action.issue` | `issue` | `anchor.issue` |
| `action.on-issue` | `on_issue` | `anchor.on-issue` |
| `action.on-issue-status` | `on_issue_status` | `anchor.on-issue-status` |

## Flows covered (42)

One frame per flow **file**; grounded at that file's `#meta.flowId`. The `flows/index.yaml`
manifest carries the same 42 entries (`usecase`, `tags`, `description`, `meta.order`).

### HEALTH INSURANCE (20)

| frame | `meta.flowId` | config file | interned anchor |
|---|---|---|---|
| `flow.cancel-health-insurance-family` | `Cancel_Health_Insurance(Family)` | `flows/HEALTH INSURANCE/Cancel_Health_Insurance_Family_.yaml` | `anchor.flow-health-cancel-family` |
| `flow.cancel-health-insurance-individual` | `Cancel_Health_Insurance(Individual)` | `flows/HEALTH INSURANCE/Cancel_Health_Insurance_Individual_.yaml` | `anchor.flow-health-cancel-individual` |
| `flow.claim-health-insurance-family` | `Claim_Health_Insurance(Family)` | `flows/HEALTH INSURANCE/Claim_Health_Insurance_Family_.yaml` | `anchor.flow-health-claim-family` |
| `flow.claim-health-insurance-individual` | `Claim_Health_Insurance(Individual)` | `flows/HEALTH INSURANCE/Claim_Health_Insurance_Individual_.yaml` | `anchor.flow-health-claim-individual` |
| `flow.health-insurance-application-family` | `Health_Insurance_Application(Family)` | `flows/HEALTH INSURANCE/Health_Insurance_Application_Family_.yaml` | `anchor.flow-health-application-family` |
| `flow.health-insurance-application-family-with-igm` | `Health_Insurance_Application(Family)_With_IGM(v-1.0.0)` | `flows/HEALTH INSURANCE/Health_Insurance_Application_Family_With_IGM.yaml` | `anchor.flow-health-application-family-igm` |
| `flow.health-insurance-application-individual` | `Health_Insurance_Application(Individual)` | `flows/HEALTH INSURANCE/Health_Insurance_Application_Individual_.yaml` | `anchor.flow-health-application-individual` |
| `flow.health-insurance-application-individual-with-igm` | `Health_Insurance_Application(Individual)_With_IGM(v-1.0.0)` | `flows/HEALTH INSURANCE/Health_Insurance_Application_Individual_With_IGM.yaml` | `anchor.flow-health-application-individual-igm` |
| `flow.health-insurance-application-pre-order-family` | `Health_Insurance_Application(PRE-ORDER-Family)` | `flows/HEALTH INSURANCE/Health_Insurance_Application_PRE-ORDER-Family_.yaml` | `anchor.flow-health-preorder-family` |
| `flow.health-insurance-application-pre-order-family-with-manual-review` | `Health_Insurance_Application(PRE-ORDER-Family-With-ManualReview)` | `flows/HEALTH INSURANCE/Health_Insurance_Application_PRE-ORDER-Family-With-ManualReview_.yaml` | `anchor.flow-health-preorder-family-manual-review` |
| `flow.health-insurance-application-pre-order-family-without-cis` | `Health_Insurance_Application(PRE-ORDER-Family-Without-CIS)` | `flows/HEALTH INSURANCE/Health_Insurance_Application_PRE-ORDER-Family-Without-CIS_.yaml` | — *(no atom)* |
| `flow.health-insurance-application-pre-order-individual` | `Health_Insurance_Application(PRE-ORDER-Individual)` | `flows/HEALTH INSURANCE/Health_Insurance_Application_PRE-ORDER-Individual_.yaml` | `anchor.flow-health-preorder-individual` |
| `flow.health-insurance-application-pre-order-individual-with-manual-review` | `Health_Insurance_Application(PRE-ORDER-Individual-With-ManualReview)` | `flows/HEALTH INSURANCE/Health_Insurance_Application_PRE-ORDER-Individual-With-ManualReview_.yaml` | `anchor.flow-health-preorder-individual-manual-review` |
| `flow.health-insurance-application-pre-order-individual-without-cis` | `Health_Insurance_Application(PRE-ORDER-Individual-Without-CIS)` | `flows/HEALTH INSURANCE/Health_Insurance_Application_PRE-ORDER-Individual-Without-CIS_.yaml` | — *(no atom)* |
| `flow.payment-failure-health-insurance-family` | `Payment_Failure_Health_Insurance(Family)` | `flows/HEALTH INSURANCE/Payment_Failure_Health_Insurance_Family_.yaml` | — *(no atom)* |
| `flow.payment-failure-health-insurance-individual` | `Payment_Failure_Health_Insurance(Individual)` | `flows/HEALTH INSURANCE/Payment_Failure_Health_Insurance_Individual_.yaml` | — *(no atom)* |
| `flow.payment-failure-health-insurance-pre-order-family-with-manual-review` | `Payment_Failure_Health_Insurance(PRE-ORDER-Family-With-ManualReview)` | `flows/HEALTH INSURANCE/Payment_Failure_Health_Insurance_PRE-ORDER-Family-With-ManualReview_.yaml` | — *(no atom)* |
| `flow.payment-failure-health-insurance-pre-order-individual-with-manual-review` | `Payment_Failure_Health_Insurance(PRE-ORDER-Individual-With-ManualReview)` | `flows/HEALTH INSURANCE/Payment_Failure_Health_Insurance_PRE-ORDER-Individual-With-ManualReview_.yaml` | — *(no atom)* |
| `flow.renew-health-insurance-family` | `Renew_Health_Insurance(Family)` | `flows/HEALTH INSURANCE/Renew_Health_Insurance_Family_.yaml` | `anchor.flow-health-renew-family` |
| `flow.renew-health-insurance-individual` | `Renew_Health_Insurance(Individual)` | `flows/HEALTH INSURANCE/Renew_Health_Insurance_Individual_.yaml` | `anchor.flow-health-renew-individual` |

### MOTOR INSURANCE (7)

| frame | `meta.flowId` | config file | interned anchor |
|---|---|---|---|
| `flow.cancel-motor-insurance` | `Cancel_Motor_Insurance` | `flows/MOTOR INSURANCE/Cancel_Motor_Insurance.yaml` | `anchor.flow-motor-cancel` |
| `flow.claim-motor-insurance` | `Claim_Motor_Insurance` | `flows/MOTOR INSURANCE/Claim_Motor_Insurance.yaml` | `anchor.flow-motor-claim` |
| `flow.motor-insurance-application` | `Motor_Insurance_Application` | `flows/MOTOR INSURANCE/Motor_Insurance_Application.yaml` | `anchor.flow-motor-application` |
| `flow.motor-insurance-application-pre-order` | `Motor_Insurance_Application(PRE-ORDER)` | `flows/MOTOR INSURANCE/Motor_Insurance_Application_PRE-ORDER_.yaml` | `anchor.flow-motor-preorder` |
| `flow.motor-insurance-application-with-igm` | `Motor_Insurance_Application_With_IGM` | `flows/MOTOR INSURANCE/Motor_Insurance_Application_With_IGM.yaml` | `anchor.flow-motor-application-igm` |
| `flow.payment-failure-motor-insurance` | `Payment_Failure_Motor_Insurance` | `flows/MOTOR INSURANCE/Payment_Failure_Motor_Insurance.yaml` | — *(no atom)* |
| `flow.payment-failure-motor-insurance-pre-order` | `Payment_Failure_Motor_Insurance(PRE-ORDER)` | `flows/MOTOR INSURANCE/Payment_Failure_Motor_Insurance_PRE-ORDER.yaml` | — *(no atom)* |

### ACCIDENTAL INSURANCE (5)

| frame | `meta.flowId` | config file | interned anchor |
|---|---|---|---|
| `flow.cd-balance-error-accidental-insurance` | `CD_Balance_Error_Accidental_Insurance` | `flows/ACCIDENTAL INSURANCE/CD_Balance_Error_Accidental_Insurance.yaml` | `anchor.flow-cd-balance-accidental` |
| `flow.discovery-of-insurer-providers-and-master-policies-accidental` | `Discovery_of_Insurer_Providers_and_Master_Policies` | `flows/ACCIDENTAL INSURANCE/Discovery_of_Insurer_Providers_and_Master_Policies.yaml` | `anchor.flow-discovery-insurers` |
| `flow.discovery-of-products-from-master-policies-accidental-insurance` | `Discovery_of_Products_from_Master_Policies (Accidental Insurance)` | `flows/ACCIDENTAL INSURANCE/Discovery_of_Products_from_Master_Policies__Accidental_Insurance_.yaml` | `anchor.flow-discovery-products-accidental` |
| `flow.purchase-journey-accidental-insurance` | `Purchase_Journey_Accidental_Insurance` | `flows/ACCIDENTAL INSURANCE/Purchase_Journey_Accidental_Insurance.yaml` | `anchor.flow-purchase-accidental` |
| `flow.purchase-journey-accidental-insurance-with-igm` | `Purchase_Journey_Accidental_Insurance_with_igm_1.0.0` | `flows/ACCIDENTAL INSURANCE/Purchase_Journey_Accidental_Insurance_with_igm_1.0.0.yaml` | `anchor.flow-purchase-accidental-igm` |

### HOSPICASH INSURANCE (5)

| frame | `meta.flowId` | config file | interned anchor |
|---|---|---|---|
| `flow.cd-balance-error-hospicash-insurance` | `CD_Balance_Error_Hospicash_Insurance` | `flows/HOSPICASH INSURANCE/CD_Balance_Error_Hospicash_Insurance.yaml` | `anchor.flow-cd-balance-hospicash` |
| `flow.discovery-of-insurer-providers-and-master-policies-hospicash` | `Discovery_of_Insurer_Providers_and_Master_Policies` | `flows/HOSPICASH INSURANCE/Discovery_of_Insurer_Providers_and_Master_Policies.yaml` | `anchor.flow-discovery-insurers` |
| `flow.discovery-of-products-from-master-policies-hospicash-insurance` | `Discovery_of_Products_from_Master_Policies (Hospicash Insurance)` | `flows/HOSPICASH INSURANCE/Discovery_of_Products_from_Master_Policies__Hospicash_Insurance_.yaml` | `anchor.flow-discovery-products-hospicash` |
| `flow.purchase-journey-hospicash-insurance` | `Purchase_Journey_Hospicash_Insurance` | `flows/HOSPICASH INSURANCE/Purchase_Journey_Hospicash_Insurance.yaml` | `anchor.flow-purchase-hospicash` |
| `flow.purchase-journey-hospicash-insurance-with-igm` | `Purchase_Journey_Hospicash_Insurance_with_igm_1.0.0` | `flows/HOSPICASH INSURANCE/Purchase_Journey_Hospicash_Insurance_with_igm_1.0.0.yaml` | `anchor.flow-purchase-hospicash-igm` |

### TRANSIT INSURANCE (5)

| frame | `meta.flowId` | config file | interned anchor |
|---|---|---|---|
| `flow.cd-balance-error-transit-insurance` | `CD_Balance_Error_Transit_Insurance` | `flows/TRANSIT INSURANCE/CD_Balance_Error_Transit_Insurance.yaml` | `anchor.flow-cd-balance-transit` |
| `flow.discovery-of-insurer-providers-and-master-policies-transit` | `Discovery_of_Insurer_Providers_and_Master_Policies` | `flows/TRANSIT INSURANCE/Discovery_of_Insurer_Providers_and_Master_Policies.yaml` | `anchor.flow-discovery-insurers` |
| `flow.discovery-of-products-from-master-policies-transit-insurance` | `Discovery_of_Products_from_Master_Policies (Transit Insurance)` | `flows/TRANSIT INSURANCE/Discovery_of_Products_from_Master_Policies__Transit_Insurance_.yaml` | `anchor.flow-discovery-products-transit` |
| `flow.purchase-journey-transit-insurance` | `Purchase_Journey_Transit_Insurance` | `flows/TRANSIT INSURANCE/Purchase_Journey_Transit_Insurance.yaml` | `anchor.flow-purchase-transit` |
| `flow.purchase-journey-transit-insurance-with-igm` | `Purchase_Journey_Transit_Insurance_with_igm_1.0.0` | `flows/TRANSIT INSURANCE/Purchase_Journey_Transit_Insurance_with_igm_1.0.0.yaml` | `anchor.flow-purchase-transit-igm` |

### Flow coverage gap

8 of the 42 flow files carry **no unit in `atoms.md`** — they have a frame
(declared, grounded) but no interned meaning and no facts:

- `flow.health-insurance-application-pre-order-family-without-cis` — `Health_Insurance_Application(PRE-ORDER-Family-Without-CIS)`
- `flow.health-insurance-application-pre-order-individual-without-cis` — `Health_Insurance_Application(PRE-ORDER-Individual-Without-CIS)`
- `flow.payment-failure-health-insurance-family` — `Payment_Failure_Health_Insurance(Family)`
- `flow.payment-failure-health-insurance-individual` — `Payment_Failure_Health_Insurance(Individual)`
- `flow.payment-failure-health-insurance-pre-order-family-with-manual-review` — `Payment_Failure_Health_Insurance(PRE-ORDER-Family-With-ManualReview)`
- `flow.payment-failure-health-insurance-pre-order-individual-with-manual-review` — `Payment_Failure_Health_Insurance(PRE-ORDER-Individual-With-ManualReview)`
- `flow.payment-failure-motor-insurance` — `Payment_Failure_Motor_Insurance`
- `flow.payment-failure-motor-insurance-pre-order` — `Payment_Failure_Motor_Insurance(PRE-ORDER)`

Closed-world reading: absence = not-known, not "nothing to say". These are the first
candidates for a Stage E pass.

Three flow files share one `meta.flowId` (`Discovery_of_Insurer_Providers_and_Master_Policies`,
under ACCIDENTAL / HOSPICASH / TRANSIT). Their frames are disambiguated by use-case suffix;
`atoms.md` collapses all three into the single anchor `anchor.flow-discovery-insurers`.

## Atom shape

**Relations used** (closed vocabulary; `not-` negatives are facts, not gaps): `isa` 298 · `scoped-to` 120 · `precedes` 70 · `part-of` 62 · `requires` 54 · `has-slot` 36 · `causes` 26 · `sent-by` 25 · `constrains` 17 · `not-requires` 16 · `not-scoped-to` 15 · `disjoint-with` 11 · `not-isa` 7 · `not-has-slot` 6 · `not-causes` 3 · `not-precedes` 3 · `not-part-of` 1

**Basis mix**: `declared` 730 · `authority` 25 · `observed-live` 6 · `sandbox-tested` 5 · `inferred` 4. `inferred` units carry no `grounded-in` and are never read as asserted fact.

Grounding density by config file (atoms grounded there):

| config node | atoms |
|---|---|
| `validations/index.yaml` | 257 |
| `flows/index.yaml` | 82 |
| `attributes/HEALTH_INSURANCE.yaml` | 68 |
| `flows/HEALTH INSURANCE/Health_Insurance_Application_Individual_.yaml` | 51 |
| `actions/index.yaml` | 48 |
| `flows/MOTOR INSURANCE/Claim_Motor_Insurance.yaml` | 35 |
| `errors/index.yaml` | 33 |
| `specs/openapi.yaml` | 17 |
| `index.yaml` | 14 |
| `flows/MOTOR INSURANCE/Motor_Insurance_Application.yaml` | 14 |
| `flows/HEALTH INSURANCE/Health_Insurance_Application_Individual_With_IGM.yaml` | 13 |
| `docs/overview.md` | 12 |

## Contract

- unit grammar · `.claude/skills/ondc-kb-seed/kb-format/unit.md`
- anchors · `.claude/skills/ondc-kb-seed/kb-format/anchor.md`
- closed vocabularies · `.claude/skills/ondc-kb-seed/kb-format/vocabularies.md`
- invariants · `.claude/skills/ondc-kb-seed/kb-format/invariants.md`
- validator · `python3 .claude/skills/ondc-kb-seed/tools/validate_kb.py knowledge/fis13-health-2.0.0`

Sibling books (never mix `asof`): `knowledge/fis13-health-2.0.1/`, `knowledge/fis13-sachet/`.

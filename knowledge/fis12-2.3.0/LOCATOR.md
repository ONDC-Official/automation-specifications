# fis12-2.3.0 — locator

Where do I find X in this book (invariant 18). Start here, then grep [`atoms.md`](atoms.md) —
it is the only place facts live. [`INDEX.md`](INDEX.md) is the navigation surface.

## By question

| I want to know… | look here | how |
|---|---|---|
| what a handle *means* | [`anchors/index.md`](anchors/index.md) | `grep '^| anchor.<name> ' anchors/index.md` — one row: meaning + config ground |
| every fact about a handle | [`atoms.md`](atoms.md) | `grep 'anchor.<name>' atoms.md` (matches subject **and** object position) |
| what a frame node is | [`frames/anchor.<name>.md`](frames/) | filename **is** the handle; frontmatter carries `kind`/`layer`/`asof` |
| which flows exist | [`INDEX.md`](INDEX.md) §Flows | 10 framed; config truth in `flows/index.yaml` |
| which actions exist + who sends them | [`INDEX.md`](INDEX.md) §Actions | `grep 'sent-by' atoms.md` for BAP/BPP ownership |
| what may follow an action | [`atoms.md`](atoms.md) | `grep 'precedes' atoms.md` — grounded at `actions/index.yaml#supportedActions.<a>` |
| which action a callback answers | [`atoms.md`](atoms.md) | `grep 'async-predecessor' atoms.md` → `actions/index.yaml#apiProperties.<a>.async_predecessor` |
| what a call is required to carry | [`atoms.md`](atoms.md) | `grep ' requires ' atoms.md`; grounds land in `validations/index.yaml#_TESTS_.…` |
| what is explicitly **not** required | [`atoms.md`](atoms.md) | `grep ' not-' atoms.md` — 73 negatives; absence ≠ negative (closed world) |
| enum members (loan categories, statuses, forms) | [`atoms.md`](atoms.md) | ground path `validations/index.yaml#enums.<group>[<CODE>]` |
| tag groups on item / payment / fulfilment | [`atoms.md`](atoms.md) | ground path `validations/index.yaml#tags.<area>.<group>[<CODE>]` |
| error codes | [`atoms.md`](atoms.md) | `grep 'errors/index.yaml' atoms.md` — 23 codes (80101–80105, 80228–80245) |
| Beckn payload schemas | [`atoms.md`](atoms.md) | ground path `specs/openapi.yaml#components.schemas.<Name>` |
| HTTP endpoints | [`atoms.md`](atoms.md) | ground path `specs/openapi.yaml#paths.<path>` |
| the "why" behind a rule | [`atoms.md`](atoms.md) | `grep 'basis:authority' atoms.md` — 156 units, grounded in `docs/**` or workbench refs |
| what is not yet committed | [`candidate-units.md`](candidate-units.md) | staging only — **never** cite as fact |
| what is parked ungrounded | [`atoms.md`](atoms.md) | `grep '!untethered' atoms.md` — 7 units |

## By config file → what it grounds

| config file (under `configs/release-eks-FIS12-2.3.0/config/`) | grounds | units |
|---|---|---|
| `validations/index.yaml` | `_TESTS_` L1 rules, `enums.*`, `tags.*` | 337 |
| `flows/index.yaml` + `flows/LAMF/**` + `flows/BUSINESS_LOAN/**` | flow identity, step order, ownership, mocks, unsolicited callbacks | 133 |
| `actions/index.yaml` | `supportedActions` successor sets, `apiProperties` | 133 |
| `docs/overview.md`, `docs/loan-category-struct.md`, `docs/xinput-form-response.md` | authority-basis domain meaning | 113 |
| `attributes/LAMF_LOAN.yaml` | per-field owner/required attribute sets | 112 |
| `specs/openapi.yaml` | `components.schemas.*`, `paths.*` | 76 |
| `errors/index.yaml` | `code[<n>]` error definitions | 69 |
| `index.yaml` | domain, version, use cases, branch, `x-*` book refs | 13 |

`attributes/BUSINESS_LOAN.yaml` exists on disk but is commented out of `attributes/index.yaml`
upstream — out of scope, no units. Same for the three `business_term_loan_with_offline_online_*`
flow entries in `flows/index.yaml`.

## Node-path grammar (grounding)

A `grounded-in` is `fis12-2.3.0:<file>#<node-path>` — a **positional** path, never a line number.
`.key` walks a mapping; `[X]` walks a sequence by the item's `action_id` / `_NAME_` / `code` / `id`,
by literal scalar value, or by numeric index.

```text
fis12-2.3.0:actions/index.yaml#supportedActions.on_confirm
fis12-2.3.0:flows/index.yaml#flows[business_term_loan_with_aa].id
fis12-2.3.0:validations/index.yaml#enums.loanCategories[LAMF]
fis12-2.3.0:validations/index.yaml#_TESTS_.on_init[ON_INIT_ITEMS]._RETURN_[REQUIRED_ITEMS]
```

To resolve one by hand, load the file with `.claude/skills/ondc-kb-seed/tools/_yaml.py`
(**PyYAML alone raises `ComposerError`** on `validations/index.yaml` — it redefines YAML anchors and
only parses under js-yaml semantics) and walk the path.

## Known ambiguities — a human must decide

| handle | why | frame |
|---|---|---|
| `anchor.required-xinput-fields` | `&REQUIRED_XINPUT_FIELDS` is declared 3× in `validations/index.yaml` (plus 2 unanchored `_NAME_` copies); later declarations shadow earlier ones | [`frames/anchor.required-xinput-fields.md`](frames/anchor.required-xinput-fields.md) |
| `anchor.on-action-items` | `&ON_ACTION_ITEMS` is declared 2× and aliased 2×; the alias sites bind to whichever declaration precedes them | [`frames/anchor.on-action-items.md`](frames/anchor.on-action-items.md) |

Neither is interned to a single definition. Both `isa` [`anchor.redefined-validation-anchor`](frames/anchor.redefined-validation-anchor.md).

## Gaps

| gap | detail |
|---|---|
| `dedupe_check` flow | active in `flows/index.yaml` (order 8, BUSINESS LOAN, MANDATORY) but carries **no unit** in `atoms.md` — no anchor, no frame |
| `anchor.runtime-concept`, `anchor.loan-classification` | recur ≥5× but have no verified config ground (workbench-only / heading slug drift in `docs/loan-category-struct.md`), so no frame |
| `docs/loan-category-struct.md` headings | 14 grounds in `atoms.md` target slugs like `#unsecured-personal` while the file's headings slug to `#41-unsecured-personal` — pre-existing, not touched here |

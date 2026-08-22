# LOCATOR — fis12-2.0.3

Where to find X in this book (invariant 18). Start here, then open the file named in the last column.

- KB root: `knowledge/fis12-2.0.3/`
- config root: `configs/release-eks-FIS12-2.0.3/config/` — every `<file>#<node-path>` below is
  positional, never a line number.

## Facts about this domain

| question / topic | file | section · how to find it |
|---|---|---|
| every committed fact in this book | `atoms.md` | whole file; one `subject \| relation \| object` per line |
| what a handle means, and where it was interned | `anchors/index.md` | registry table, sorted by handle |
| which nodes have a full rendering | `frames/` | one `<id>.md` per framed node |
| counts, flow list, action list | `INDEX.md` | tables at the top |
| staged-but-not-committed triples | `candidate-units.md` | Stage E buffer; not fact, not validated |

## Flows and journeys

| question / topic | file | section · how to find it |
|---|---|---|
| which flows does this release declare | `INDEX.md` | § Flows covered (10 framed, 3 unframed) |
| the flow catalogue in config | config `flows/index.yaml` | `#flows` — `id`, `usecase`, `description`, `$ref` |
| the step sequence of one flow | config `flows/<USECASE>/<flow>.yaml` | `#steps[<action_id>]` — `owner`, `api`, `responseFor`, `unsolicited`, `mock` |
| what a flow requires / causes | `atoms.md` | grep the flow handle, e.g. `anchor.flow-gold-loan-offline` |
| which use case a flow belongs to | `atoms.md` | grep `scoped-to \| anchor.gold-loan-usecase` (or `…personal-loan-usecase`) |
| flows that add grievance handling | `frames/anchor.igm-1-0-0.md` | plus `atoms.md` grep `wasDerivedFrom` |
| the offline vs single-redirection split | `frames/anchor.single-redirection.md`, config `docs/overview.md#key-concepts` | |

## Protocol actions and sequencing

| question / topic | file | section · how to find it |
|---|---|---|
| the 15 supported actions | `INDEX.md` | § Actions covered |
| which action may follow which | config `actions/index.yaml` | `#supportedActions.<action>` (successor list) |
| ordering facts in the KB | `atoms.md` | grep `\| precedes \|` |
| which action is an async callback of which | config `actions/index.yaml` | `#apiProperties.<action>.async_predecessor` |
| paired request/response partners | config `actions/index.yaml` | `#apiProperties.<action>.transaction_partner` |
| who emits a message (BAP or BPP) | `atoms.md` | grep `\| sent-by \|`; roles framed in `frames/anchor.bap.md`, `frames/anchor.bpp.md` |
| callbacks sent with no paired request | `frames/anchor.unsolicited-callback.md` | `atoms.md` grep `anchor.unsolicited-callback` |
| the HTTP endpoint of an action | `atoms.md` grep `anchor.api-endpoint` | config `specs/openapi.yaml#paths[/<action>].post.operationId` |

## Payloads, forms and enums

| question / topic | file | section · how to find it |
|---|---|---|
| required fields per action, with owner | config `attributes/PERSONAL_LOAN.yaml`, `attributes/GOLD_LOAN.yaml` | `#attribute_set.<action>.…._description` (`required`, `owner`, `enums`, `usage`) |
| the HTML application form fields | config `attributes/<USECASE>.yaml` | `#attribute_set.html_form`; KB: `atoms.md` grep `anchor.html-form-personal-loan` / `anchor.html-form-gold-loan` |
| the dynamic (verification / payment) form | `frames/anchor.dynamic-form.md` | config `attributes/PERSONAL_LOAN.yaml#attribute_set.dynamic_form` |
| xinput form mechanics and redirection | `frames/anchor.xinput.md`, `frames/anchor.xinput-form-response.md` | config `docs/xinput-form-response.md#form-response`, `#seller-side-form` |
| catalogue shape (provider → items) | `frames/anchor.catalog.md`, `frames/anchor.provider.md`, `frames/anchor.loan-item.md` | |
| the search intent block | `frames/anchor.search-intent.md` | config `attributes/PERSONAL_LOAN.yaml#attribute_set.search.message.intent` |
| loan category codes on search | `frames/anchor.search-category-codes.md` | config `validations/index.yaml#_TESTS_.search[SEARCH_CATEGORY_CODE]` |
| quote, breakup titles, ttl | `frames/anchor.quote.md` | `atoms.md` grep `anchor.quote-breakup-titles-origination` / `…-servicing` |
| origination checklist codes | `frames/anchor.checklist-codes.md` | config `validations/index.yaml#_TESTS_.on_status[ON_STATUS_CHECKLIST_CODES]` |
| repayment event labels (foreclosure, missed EMI, pre-part) | `frames/anchor.payment-time-labels.md` | config `validations/index.yaml#_TESTS_.update[UPDATE_PAYMENT_TARGET]` |
| any other enum or tag group | `anchors/index.md` | grep the handle; its `grounded-in` is the defining config node |

## Validation, errors and grievances

| question / topic | file | section · how to find it |
|---|---|---|
| what a named validation test asserts | config `validations/index.yaml` | `#_TESTS_.<action>[<TEST_NAME>]` — `_SCOPE_`, `_RETURN_`, `enumList`, `validTags`, `validValues` |
| which rule is scoped to which action | `atoms.md` | grep `\| scoped-to \| anchor.on-` etc. |
| what halts a flow | `atoms.md` | grep `anchor.flow-halt` |
| the error-code register | `frames/anchor.error-code.md` | config `errors/index.yaml#code[<code>]` — `Event`, `Description`, `From` |
| who returns a given error code | `atoms.md` | grep the literal, e.g. `"80218"` |
| grievance protocol versions | `frames/anchor.igm-1-0-0.md`, `frames/anchor.igm-2-0-0.md` | config `validations/index.yaml#_TESTS_.issue[ISSUE_VALIDATION_VERSION_100 \| _200]` |
| grievance context requirements | `frames/anchor.grievance.md` | config `validations/index.yaml#_TESTS_.issue[REQUIRED_CONTEXT_FIELDS]` |

## Provenance and gaps

| question / topic | file | section · how to find it |
|---|---|---|
| what backs a fact | `atoms.md` | the `basis:` field on each unit |
| facts with no resolvable ground | `atoms.md` | grep `!untethered` |
| model guesses, never asserted | `atoms.md` | grep `basis:inferred` (these carry no `grounded-in`) |
| explicit negatives | `atoms.md` | grep `\| not-` |
| facts derived from other KB facts | `atoms.md` | grep `basis:derived` (ground is a unit or anchor handle) |
| domain, version and use-case declaration | config `index.yaml` | `#info.domain`, `#info.version`, `#info.x-usecases` |
| release notes / external references | config `docs/release-notes.md`, `docs/references.md` | recorded in `atoms.md` as `not-has-slot` (empty in this release) |
| re-run the validity gate | `INDEX.md` | § Gate |

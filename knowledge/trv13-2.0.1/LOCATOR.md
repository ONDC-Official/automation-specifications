# trv13-2.0.1 — locator

Where to find X. Config paths are relative to `configs/release-eks-TRV13-2.0.1/config/`;
KB paths are relative to `knowledge/trv13-2.0.1/`. A `grounded-in` pointer is always
`trv13-2.0.1:<file>#<node-path>` — a **position**, never a line number.

## KB side — "what does the KB say about X?"

| I want… | look in | how |
|---|---|---|
| every committed fact | `atoms.md` | one triple per line: `subject \| relation \| object \| basis \| asof \| grounded-in \| !flags` |
| what a handle means | `anchors/index.md` | grep the `anchor.<kebab>` row → canonical meaning + the position it was interned at |
| a framed node (flow, action, concept) | `frames/<id>.md` | filename **is** the frame `id`, e.g. `frames/anchor.flow-city-code.md` |
| everything said about one handle | `atoms.md` | `grep 'anchor.quote' atoms.md` — subject and object positions both |
| the API sequence of a flow | `atoms.md` | `grep precedes atoms.md`, or read the flow's `steps` in config |
| who sends a message | `atoms.md` | `grep sent-by atoms.md` → object is `"BAP"` or `"BPP"` |
| what is explicitly **not** required | `atoms.md` | `grep not- atoms.md` — negatives are facts, not gaps |
| unbacked / quarantined material | `atoms.md` | `grep -E '!untethered\|basis:inferred' atoms.md` (3 + 2 units) — never assert these |
| ideas that did not become atoms | `candidate-units.md` | staging only; not committed truth |
| counts, flows, actions, links | `INDEX.md` | the navigation surface |
| the format rules themselves | `.claude/skills/ondc-kb-seed/kb-format/` | `unit.md`, `anchor.md`, `vocabularies.md`, `invariants.md` |

## Config side — "where is this rule actually written?"

| I want… | file | node path shape |
|---|---|---|
| the domain / version / usecase | `index.yaml` | `info.domain`, `info.version`, `info.x-usecases` |
| which actions may follow action X | `actions/index.yaml` | `supportedActions.<action>` (`supportedActions.null` = transaction entry) |
| whether a callback needs its request | `actions/index.yaml` | `apiProperties.<action>.async_predecessor` |
| which earlier calls an action may pair with | `actions/index.yaml` | `apiProperties.<action>.transaction_partner` |
| the list of flows and their tags | `flows/index.yaml` | `flows[<flow id>]`, `.usecase`, `.tags`, `.description` |
| a flow's steps, owners and payloads | `flows/Hotel-Booking-V2/<Flow_File>.yaml` | `steps[<action_id>]`, `.api`, `.owner`, `.unsolicited`, `.description`, `.mock.defaultPayload…`, `.mock.generate`, `.mock.requirements`, `.mock.saveData…` |
| what a field *means* | `attributes/Hotel_Booking-V2.yaml` | `attribute_set.<action>.<json path>._description` (append `.enums` for its enum list) |
| a required / regex / enum rule | `validations/index.yaml` | `_TESTS_.<action>[<TEST_NAME>]._RETURN_[<CHECK_NAME>]` then `.attr`, `.reg`, `.enumList`, `.validTags`, `.validValues`, `.tagPath` |
| an error code and who raises it | `errors/index.yaml` | `code[<code>]`, `.From`, `.Description` |
| the HTTP surface | `specs/openapi.yaml` | `paths[/<action>].post.operationId` |
| narrative background (the "why") | `docs/overview.md`, `docs/references.md`, `docs/release-notes.md` | GitHub-style heading slug, e.g. `#key-concepts`, `#use-cases`, `#sector--purpose` |

## This book's hot spots

| topic | start at |
|---|---|
| discovery / catalog shape | `attributes/Hotel_Booking-V2.yaml#attribute_set.on_search.message.catalog…`, frames `anchor.hotel-catalog`, `anchor.hotel-provider`, `anchor.accommodation-item` |
| pagination | `flows/…/Hotel_Booking_Seller_App_Pagination_Flow.yaml`, frames `anchor.pagination-tag-group`, `anchor.unsolicited-on-search` |
| TTL / catalog refresh | `flows/…/Hotel_Booking__ttl_based__booking.yaml`, frames `anchor.catalog-refresh-search`, `anchor.catalog-refresh-response` |
| cancellation (both sides) | `validations/index.yaml#_TESTS_.cancel[CANCEL_MESSAGE_1]`, frames `anchor.buyer-initiated-cancellation`, `anchor.merchant-initiated-cancellation`, `anchor.cancellation-terms` |
| post-confirmation updates | `validations/index.yaml#_TESTS_.update[UPDATE_MESSAGE_1]`, frame `anchor.booking-update` |
| payments & settlement tags | `validations/index.yaml#_TESTS_.on_status[ON_STATUS_PAYMENTS]`, frames `anchor.payment-type`, `anchor.bpp-terms` |
| grievance (IGM 1.0.0 / 2.0.0) | `validations/index.yaml#_TESTS_.issue[ISSUE_VALIDATION_VERSION_100 \| _200]`, frames `anchor.issue`, `anchor.on-issue`, `anchor.on-issue-status` |
| per-phase context requirements | frames `anchor.discovery-…`, `anchor.confirm-…`, `anchor.status-…`, `anchor.update-phase-context-required` |

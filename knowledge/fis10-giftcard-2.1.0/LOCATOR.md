# LOCATOR — `fis10-giftcard-2.1.0`

"Where do I find X" for this book (invariant 18). Companion to [`INDEX.md`](INDEX.md).
Every row points at a file + section; the fact itself is always a line in
[`atoms.md`](atoms.md).

## How to read a pointer

- `atoms.md ⟨grep …⟩` — grep `atoms.md` for that handle; the matching lines *are* the answer.
- `anchors/index.md ⟨row⟩` — the interned meaning and the position it was interned at.
- `<file>#<node-path>` — a **positional** path into
  `configs/release-eks-FIS10-GIFTCARD-2.1.0/config/`. Never a line number.

## Structure of the book

| question | look here |
|---|---|
| What is this book, in one screen? | [`INDEX.md`](INDEX.md) |
| What are the raw facts? | [`atoms.md`](atoms.md) — 480 units |
| What does handle `anchor.X` mean, and where was it interned? | [`anchors/index.md`](anchors/index.md) — 156 rows |
| Which entities got a full node file? | [`frames/`](frames/) — 72 frames; `INDEX.md#frames-by-kind-72` for the split |
| What did Stage E propose before merge? | [`candidate-units.md`](candidate-units.md) (not authoritative) |
| What grammar do the atom lines follow? | `.claude/skills/ondc-kb-seed/kb-format/unit.md` |
| Which relations / basis values / flags are legal? | `.claude/skills/ondc-kb-seed/kb-format/vocabularies.md` |

## Flows

| question | look here |
|---|---|
| Which flows exist, and their step spines? | [`INDEX.md#flows-covered-6`](INDEX.md) · config `flows/index.yaml#flows` |
| What does one flow do end to end? | `flows/gift-card/<Flow_Id>.yaml#steps` (each step has `api`, `action_id`, `owner`, `responseFor`, `unsolicited`, `mock`, `examples`) |
| Which use case does a flow belong to? | `flows/index.yaml#flows[<Flow_Id>].usecase` · atom `anchor.flow.* \| part-of \| anchor.gift-card` |
| Which flows are reportable? | `flows/index.yaml#flows[<Flow_Id>].tags` · atoms `anchor.flow.* \| isa \| anchor.reportable-flow` |
| Which flow delivers the gift-card code, and how? | `atoms.md ⟨grep anchor.code-delivery⟩` · frames [`anchor.seller-fulfilled-code-delivery`](frames/anchor.seller-fulfilled-code-delivery.md), [`anchor.buyer-app-fulfilled-code-delivery`](frames/anchor.buyer-app-fulfilled-code-delivery.md) |
| How does a physical-store purchase differ? | [`frames/anchor.physical-store-pickup.md`](frames/anchor.physical-store-pickup.md) · `flows/gift-card/Physical_Store_Based_Gift_Cards.yaml#steps[select].mock.inputs.jsonSchema.properties.gps` |
| How is a receiver changed after confirm? | [`frames/anchor.receiver-replacement.md`](frames/anchor.receiver-replacement.md) · `flows/gift-card/Update_Receiver_Info.yaml#steps[update]` |
| What blocks a fulfillment mid-flow? | [`frames/anchor.blocked-fulfillment.md`](frames/anchor.blocked-fulfillment.md) · `flows/gift-card/Update_Receiver_Info.yaml#steps[unsolicited_on_status].mock.validate` |

## Actions & sequencing

| question | look here |
|---|---|
| Which actions does the domain support? | `actions/index.yaml#supportedActions` · [`INDEX.md#actions-covered-14`](INDEX.md) |
| What may follow action `A`? | `actions/index.yaml#supportedActions.<A>` · atoms `anchor.<A> \| precedes \| …` |
| Which callback is the async reply to which request? | `actions/index.yaml#apiProperties.<A>.async_predecessor` · atoms `anchor.on-* \| requires \| anchor.*` |
| Which actions share a transaction? | `actions/index.yaml#apiProperties.<A>.transaction_partner` |
| Where does a transaction start? | atoms `… \| isa \| anchor.transaction-entry`, grounded at `actions/index.yaml#supportedActions.null` |
| Who sends an action, BAP or BPP? | atoms `anchor.<A> \| sent-by \| anchor.bap\|anchor.bpp`, grounded at `flows/gift-card/<Flow>.yaml#steps[<action_id>].owner` |
| Which callbacks arrive unsolicited? | frames `anchor.unsolicited-on-*` · config `…#steps[<action_id>].unsolicited` and `.responseFor` |
| Are `rating` / `support` / `track` supported? | atoms `… \| not-part-of \| anchor.fis10` (explicit negatives) · `actions/index.yaml#supportedActions` |
| Where is `on_status_update_receiver_info`? | `anchors/index.md ⟨anchor.on-status-update-receiver-info⟩` — successor of `on_confirm` only, no `apiProperties` entry |

## Rules, validations & enums

| question | look here |
|---|---|
| What must every `context` carry? | [`frames/anchor.context-required.md`](frames/anchor.context-required.md) · `validations/index.yaml#_TESTS_.<action>[<ACTION>_CONTEXT]` |
| Which actions skip a context check? | atoms `anchor.context-required \| not-scoped-to \| …` |
| Which actions tolerate a stale `context.version`? | [`frames/anchor.stale-version-gate.md`](frames/anchor.stale-version-gate.md) · `validations/index.yaml#_TESTS_.<action>[<ACTION>_CONTEXT].version` |
| What are the legal values of enum `E`? | atoms `"VALUE" \| part-of \| anchor.<E>` — enum lists live at `validations/index.yaml#_TESTS_.<action>[<TEST>]._RETURN_[<ENUM_TEST>].enumList` |
| Fulfillment type / state? | [`anchor.fulfillment-type`](frames/anchor.fulfillment-type.md) · [`anchor.fulfillment-state`](frames/anchor.fulfillment-state.md) |
| Order status values? | [`anchor.order-status`](frames/anchor.order-status.md) · `specs/openapi.yaml#components.schemas.Order.properties.status.enum` |
| Payment status / collected-by / type? | [`anchor.payment-status`](frames/anchor.payment-status.md) · `attributes/gift_card.yaml#attribute_set.on_*.message.order.payments.*._description.enums` |
| Search category codes? | [`anchor.category-code`](frames/anchor.category-code.md) |
| Authorization type & token? | [`anchor.authorization-type`](frames/anchor.authorization-type.md) · [`anchor.authorization-token`](frames/anchor.authorization-token.md) |
| Which tag groups exist? | frames [`anchor.customization`](frames/anchor.customization.md), [`anchor.item-details-tags`](frames/anchor.item-details-tags.md), [`anchor.update-receiver-info-tags`](frames/anchor.update-receiver-info-tags.md), [`anchor.buyer-finder-fees`](frames/anchor.buyer-finder-fees.md), [`anchor.settlement-details`](frames/anchor.settlement-details.md) — plus `anchor.brand-details-tags` (registry row) |
| Which regexes constrain a field? | `validations/index.yaml#…[<TEST>].reg` · atoms `… \| constrains \| …` and `anchor.receiver-contact \| requires \| anchor.indian-mobile-number\|anchor.rfc5322-email` |
| Which field is required for action `A`? | atoms `anchor.<A> \| requires \| …` · `validations/index.yaml#_TESTS_.<A>[REQUIRED_*]` |
| Which field is explicitly **not** required? | atoms `anchor.<A> \| not-requires \| …` |

## Objects & attributes

| question | look here |
|---|---|
| What Beckn objects does the book use? | frames `anchor.{provider,item,payment,fulfillment,stop,authorization,receiver,billing,quote,offer,cancellation}` · `specs/openapi.yaml#components.schemas.<Name>` |
| Which slots hang off an object? | atoms `anchor.<obj> \| has-slot \| …` |
| What does an attribute mean at one position? | `attributes/gift_card.yaml#attribute_set.<action>.<path>._description` (`.enums`, `.owner`, `.required`, `.usage`, `.info`) |
| Which action owns a field, BAP or BPP? | `attributes/gift_card.yaml#…._description.owner` |
| Why does the same key mean two things? | the `scoped-to` units — `atoms.md ⟨grep scoped-to⟩`; see `kb-format/anchor.md#position-carries-meaning----scoped-to` |

## Session / mock runtime

| question | look here |
|---|---|
| What state does a flow carry between steps? | [`frames/anchor.session-key.md`](frames/anchor.session-key.md) · atoms `anchor.session-* \| isa \| anchor.session-key` |
| Which step writes a session key? | `…#steps[<action_id>].mock.saveData.<key>` · atoms `… \| causes \| anchor.session-*` |
| Which step reads it? | `…#steps[<action_id>].mock.requirements` · atoms `… \| requires \| anchor.session-*` |
| What input does a step ask a user for? | `…#steps[<action_id>].mock.inputs.jsonSchema` |
| What does a step assert on the payload? | `…#steps[<action_id>].mock.validate` |

## Errors

| question | look here |
|---|---|
| Which error codes does this book register? | frames `anchor.error-*` (10) · `errors/index.yaml#code` |
| What does code `N` mean, and who raises it? | `errors/index.yaml#code[N].Event` / `.Description` / `.From` |
| Which codes are inherited lending codes, not gift-card ones? | atoms `anchor.error-* \| not-scoped-to \| anchor.gift-card` (80101, 80204, 80226) |
| What raises a TTL error? | `atoms.md ⟨grep anchor.error-80214⟩` |

## Provenance, gaps & versioning

| question | look here |
|---|---|
| What is asserted vs guessed? | the `basis:` field — `declared` 444, `authority` 25, `derived` 6, `inferred` 5. `basis:inferred` is never asserted (invariant 14) |
| What has no resolvable ground? | the 16 `!untethered` units at the tail of `atoms.md` |
| Which facts come from the workbench, not the config? | `atoms.md ⟨grep workbench:⟩` — 18 units, `basis:authority` |
| Which facts were derived from other units? | `atoms.md ⟨grep "grounded-in:anchor."⟩` — 6 units, `basis:derived` |
| Which flow was modelled on another? | atoms `… \| wasDerivedFrom \| …` (`basis:inferred` — quarantined) |
| Which version does a fact hold for? | its `asof:` — always `fis10-giftcard-2.1.0`; no cross-version inference (invariant 15) |
| What changed in this release? | `docs/release-notes.md` · `docs/references.md` (both recorded `not-part-of anchor.gift-card`) |
| How do I check the book is still valid? | `python3 .claude/skills/ondc-kb-seed/tools/validate_kb.py knowledge/fis10-giftcard-2.1.0` |
| Which units break if a config file changes? | `knowledge/_index/reverse-index.json` (by node-path) · `knowledge/_index/blast-radius.json` (by file) |

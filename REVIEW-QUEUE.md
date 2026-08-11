# Review queue — items requiring a human decision

Produced by the ondc-kb-seed run. Everything here is **parked, not asserted**. The KB validates
and the seed is usable as-is; these are the places where the pipeline deliberately refused to
decide for you.

---

## 1. Gate 0b — base deviations (BLOCKING for the affected elements)

`common-config/beckn-base.yaml` is the human-owned authority. The skill grounds against it and
**never rewrites it**. 42 deviations across 16 books collapse to **15 distinct elements** that the
configs use and the base does not cover. All 15 are **held out of seeding**: the audit confirms
**0 `basis:declared` units assert any of them** — they appear only parked with `!untethered`.

| element | kind | books |
|---|---|---|
| `Form.multiple_sumbissions` | new-field (note the upstream typo: *sumbissions*) | 8 |
| `Tag.list` | new-field | 7 |
| `Tag1` | new-schema | 6 |
| `Form.mime_type` += `NONE`, `TEXT/HTML-MULTI` | new-enum-value | 5 |
| `Payment.type` += `REFUND` | new-enum-value | 4 |
| `State.descriptor` | new-field | 3 |
| `CancellationTerm.cancel_eligible` | new-field | 1 |
| `CancellationTerm.return_terms` | new-field | 1 |
| `Descriptor.symbol` | new-field | 1 |
| `Error.type` | new-field | 1 |
| `Error.tags` | new-field | 1 |
| `Item.$schema` | new-field | 1 |
| `Item.type` | new-field | 1 |
| `Order.status` += `IN-PROGRESS`, `ON-HOLD` | new-enum-value | 1 |
| `Time.transaction_id` | new-field | 1 |

**Action:** update `beckn-base.yaml` by hand to cover the ones that are legitimate protocol, then
re-run the pipeline — the held-out elements will seed as `declared` on the next pass.

Two worth a closer look before you accept them:

- **`Item.$schema` (trv11-2.0.1)** — looks like a JSON-Schema authoring artifact leaking into the
  protocol surface rather than a real field. The interpreter recorded it as a bare parked slot and
  refused to give it protocol meaning.
- **`Form.multiple_sumbissions`** — the misspelling is in the configs themselves, in 8 books. If
  you add it to the base you canonise the typo; if you fix the typo you break 8 configs. Worth a
  deliberate decision rather than a silent one.

---

## 2. Gate 1 — manifest completeness

**`FIS12-2.3.0` is HELD OUT of seeding** (only structural atoms were written, no Stage E
interpretation). This matches the precedent recorded in the skill itself.

Reason: `validations/index.yaml` **fails to parse** — duplicate YAML anchor `RTA`. Duplicate
anchors also present: `KYC_OFFLINE`, `ON_ACTION_ITEMS`, `REQUIRED_ITEM_ID`,
`REQUIRED_PARENT_ITEM_ID`, `REQUIRED_XINPUT_FIELDS`, `SCHEME_CODE`. Plus 4 orphan files not
reachable from `config/index.yaml`:
`attributes/BUSINESS_LOAN.yaml`, and three `flows/BUSINESS_LOAN/business_term_loan_with_offline_online_{foreclosure,missed_emi,pre_part}.yaml`.

**Action:** de-duplicate the anchors in `validations/index.yaml` and either wire the 4 orphans into
`index.yaml` or accept them as out of scope. Then re-run — this book seeds like the others.

Orphans in otherwise-healthy books (ignored per the scope invariant, no action needed unless the
omission is unintended):

| book | orphan |
|---|---|
| FIS10-GIFTCARD-2.1.0 | `attributes/gift-card.yaml` (the hyphen twin of the in-scope `gift_card.yaml`) |
| TRV10-2.0.1, TRV10-2.1.0 | `attributes/Ride-hailing.yaml` (twin of `Ride_hailing.yaml`) |
| TRV14-2.0.0 | `attributes/unreserved-entry-pass.yaml` (twin of `unreserved_entry_pass.yaml`) |

The hyphen/underscore twin pattern recurs in 4 books — likely a rename that left the old file
behind. Worth deleting them so the manifest gate stays quiet.

**`TRV11-2.1.0`** also carries duplicate anchors (`ADDITIONAL_APIS`, `BPP_TERMS`,
`COMMON_FULFILLMENT_ITEMS`, `PASS`, `REQUIRED_ITEM_FULFILLMENT_IDS`, `REQUIRED_ORDER_ID`,
`TICKET`) but its YAML still parses, so it was seeded. The interpreter refused to intern an
arbitrary definition: ambiguous anchors were either confined with `scoped-to` or parked
`!untethered`.

---

## 3. Gate 3 — governance: one genuine contradiction

**`trv12-2.0.0` asserts both `R` and `not-R` with identical facets.** The KB-storage invariant
forbids this, so one of the two must go or be re-scoped.

```
anchor.on-init | precedes     | anchor.confirm | basis:declared | asof:trv12-2.0.0
  grounded-in: flows/Airline/Cancellation_by_Buyer.yaml#steps[confirm_Airline_200]

anchor.on-init | not-precedes | anchor.confirm | basis:declared | asof:trv12-2.0.0
  grounded-in: flows/Intercity/Intercity_Bus__Error_Response_Soft_Locking_Time_.yaml#steps[on_init_BUS_221].mock.defaultPayload.error
```

Both are individually well-grounded — they describe **different contexts**: the positive is the
normal Airline purchase path, the negative is the Intercity soft-lock **error** path (error
`90203`, where the BAP must return to selection instead of proceeding to confirm). The unit
grammar has no scope facet, so a context-specific fact asserted globally collides.

**Recommended resolution** (not applied — this is an interpretation call, and the skill routes
these to you): keep the positive as the general rule, and re-express the negative against a
distinct subject confined with `scoped-to` — e.g. an `anchor.on-init-soft-lock-expired` scoped to
the soft-lock context — so the exception stops contradicting the rule. Alternatively drop the
negative under closed-world discipline (absence = not-known).

---

## 4. Degraded / noted, no action required

- **Sequence flags — dangling `responseFor`** (no edge was asserted across any of these):
  - `trv11-2.0.0` — `flows/Metro/SELLER_OFFLINE_CANCELLATION_WITHOUT_SEARCH_ND_SELECT.yaml` → `cancel_hard_METRO_200`
  - `trv11-2.1.0` — `flows/Bus/Intracity_Seller_Based_Confirmation_flow.yaml` → `update_1`
  - `trv11-2.1.0` — `flows/Metro/DELAYED_CANCELLATION_FLOW_REJECTED.yaml` → `on_cancel_init_METRO_210`
- **Ungrounded anchors**: 624 of 3,383 registry rows have grounding `-` — interned meanings that
  are used but never appear as the subject of a grounded atom. They are visible as `-` rather than
  looking settled. Concentrated in trv13-2.0.1 (104), fis13-health-2.0.0 (89), fis14-2.1.0 (74).
- **`basis:inferred` units (50 total, 0.5%)** carry no grounding and are never asserted, per the
  invariant. They are the model's explicit "I do not know" markers — read them as questions, not
  facts.

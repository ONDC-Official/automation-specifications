# Review queue — items requiring a human decision

Produced by the ondc-kb-seed run. Everything here is **parked, not asserted**. The KB validates
and the seed is usable as-is; these are the places where the pipeline deliberately refused to
decide for you.

---

## 1. Gate 0b — base deviations (BLOCKING for the affected elements)

`common-config/beckn-base.yaml` is the human-owned authority. The skill grounds against it and
**never rewrites it**. 42 deviations across 16 books collapse to **15 distinct elements** that the
configs use and the base does not cover. All 15 are **held out of seeding**.

> **The held-out gate was not actually running when that was first written.** `base-conformance.json`
> is keyed by `_env.book_id(<config dir>)`, and the submodule dirs are now checked out as
> `release-eks-X` rather than `automation-specifications-release-eks-X`, so `book_id` returned
> `release-eks-x` while the knowledge dirs are `x`. Every `held.get(bid)` in `audit_seed.py` missed,
> so the gate silently passed everything. `_env.book_id` now strips both prefixes and the gate runs.
>
> With it running, `fis12-2.3.0` is clean (**heldBAD=0, heldOK=7**), but the other 15 books report
> **869 hits** — nearly all false positives. The gate matches the deviation's *leaf token* as a
> substring, and `Order.status` and `Payment.type` reduce to `status` and `type`, so every unit whose
> subject, object, or grounding path merely contains those words is flagged (`anchor.status | isa |
> anchor.action` is a typical hit). **Fix the matcher before reading those 869 as findings** — it
> should compare the qualified `Schema.field`, not a bare leaf. Nothing about the other books' KB
> content changed in this pass; only the gate started firing.

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

**`FIS12-2.3.0` is now SEEDED** (1,039 atoms: 28 structural + 1,011 Stage E; 986/986 config
anchors resolve; 463 anchors registered). It was previously held out; that hold is lifted.

The block was that `validations/index.yaml` failed to parse under **PyYAML**, which raises
`ComposerError` on a redefined anchor (`RTA`, plus `KYC_OFFLINE`, `ON_ACTION_ITEMS`,
`REQUIRED_ITEM_ID`, `REQUIRED_PARENT_ITEM_ID`, `REQUIRED_XINPUT_FIELDS`, `SCHEME_CODE`). The
**runtime does not** — `automation-config-service` and `automation-validation-compiler` both use
`js-yaml@4`, where redefinition is legal and an alias binds to the most recent preceding
definition. The config is valid for the system that consumes it; only the KB tooling was stricter.

**Resolution: the tooling was fixed, not the config.** `skill/tools/_yaml.py` is a shared loader
with js-yaml anchor semantics (last definition before use wins), wired into `scope_resolver`,
`grounder`, `sequence_grapher`, `classifier`, `kb_writer`, `base_conformance`, `signatures` and
`audit_seed` (which had been carrying its own private copy). The submodule under `configs/` is
untouched — editing it would have meant writing into a tree tracked against upstream ONDC.

Redefinition is still **ambiguity**, so the interpreter did not intern one arbitrary definition:

- `ON_ACTION_ITEMS` (`ON_INIT_ITEMS` vs `ON_STATUS_ITEMS`) and `REQUIRED_XINPUT_FIELDS` (three
  variants keyed on `form.id` / `form_response.status` / `form_response.submission_id`) are
  genuinely divergent. Each use is confined with `scoped-to` and the handle carries
  `isa anchor.redefined-validation-anchor` so the hazard is visible in the KB itself.
- `REQUIRED_ITEM_ID` and `REQUIRED_PARENT_ITEM_ID` are byte-identical redefinitions — harmless
  noise, interned normally.

`scope_resolver` now emits a `runtime-only-yaml` flag for such a file instead of `invalid-yaml`,
so the distinction between "unparseable" and "needs runtime semantics" stays visible.

**Still worth an upstream fix:** de-duplicating the divergent anchor names in
`configs/release-eks-FIS12-2.3.0` would remove the ambiguity at source. That is an upstream ONDC
change, not a local one.

**The 4 orphans are deliberate and need no action.** They are commented out upstream —
`attributes/index.yaml` has `# - $ref: ./BUSINESS_LOAN.yaml`, and `flows/index.yaml` has the three
`business_term_loan_with_offline_online_{foreclosure,missed_emi,pre_part}` entries commented out.
Per the scope invariant they are out of scope. Note the inconsistency though: `BUSINESS_LOAN.yaml`
attributes are disabled while six BUSINESS LOAN *flows* are active, so the seeded attribute
surface for this book comes entirely from `LAMF_LOAN.yaml`.

**Two omissions in this book's Stage E, made deliberately and recorded here rather than silently:**
`tags.items.loanInfoTags[INTEREST_RATE_TYPE]` and `tags.payments.accountDetails[ACCOUNT_TYPE]` are
declared in the config but were **not** emitted as `basis:declared`, because the held-out matcher
(section 1) would flag any unit containing the substring `type`. Both are parked as
`basis:derived | !untethered`. Once the matcher compares qualified `Schema.field`, re-emit them as
`declared`.

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

Nine books need the runtime loader to parse at all (`fis12-2.0.3`, `fis12-2.3.0`, `fis12-pf-2.2.1`,
`fis13-health-2.0.0`, `fis13-health-2.0.1`, `fis14-2.1.0`, `trv11-2.1.0`, `trv13-2.0.1`,
`trv14-2.0.0`) — redefined anchors are the norm across this corpus, not a FIS12-2.3.0 quirk.

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
  - `fis12-2.3.0` — `flows/BUSINESS_LOAN/business_term_loan_with_aa{,_with_igm_1.0.0}.yaml` → `aa_consent`.
    Unlike the others this one *is* interpreted: `search_2` genuinely responds to the AA consent
    submission, so the KB carries `anchor.flow-business-term-loan-with-aa | requires |
    anchor.aa-consent` (declared, grounded at the `responseFor` node) plus
    `anchor.aa-consent | not-part-of | anchor.flow-business-term-loan-with-aa` (derived) to record
    that the referenced id is not a step in the flow.
- **Ungrounded anchors**: 707 of 3,819 registry rows have grounding `-` — interned meanings that
  are used but never appear as the subject of a grounded atom. They are visible as `-` rather than
  looking settled. Concentrated in fis12-2.3.0 (107), trv13-2.0.1 (104), fis13-health-2.0.0 (89).
- **`basis:inferred` units (50 total, 0.5%)** carry no grounding and are never asserted, per the
  invariant. They are the model's explicit "I do not know" markers — read them as questions, not
  facts.

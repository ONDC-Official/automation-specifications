# brand_images + offer stacking + order.offers drift fix: Order_to_confirm_to_fulfillment_with_offers(Prepaid) (RETeB2B 1.2.5)

- **Date:** 2026-10-16
- **Branch:** `draft-RETeB2B`. This session committed nothing.
- **File changed:** `config/flows/eB2B/Order_to_confirm_to_fulfillment_with_offers__Prepaid_.yaml` only. `git diff --stat` = 20 insertions/9 deletions across exactly 11 line-locations, mapped back to their `action_id`: `on_search` (the new `brand_images` tag, 10 lines), `on_select` (×2: the guard fix and the new `saveData` line), and the `generate` field of `on_init`, `on_confirm`, and all six `on_status_*` steps. Nothing else in the 6,300+ line file changed.
- **Contract:** `/tmp/ebb2b_doc.txt`.
- **Method:** extracted fresh with `extract-flow.ts`, edited sidecars + two plain-YAML edits (the `brand_images` tag and the `applied_offers` saveData key) in the dev wrapper, restored with `restore-flow.ts`. Reproduced all three hypotheses and their fixes via direct `generate()`/`createQuote()` invocation (Node `vm`) and the real report-service check functions (`validateBrandImagesConsistency`, `validateOfferStacking`, `validateOrderOffersMatchApplied`).

## Verdict: all three hypotheses confirmed

### Hypothesis 1 (brand_images): confirmed, including independent corroboration

- Read `onSearchB2BChecks.ts`'s `validateBrandImagesConsistency`: it requires `provider.tags` to carry a `brand_images` group, fails hard if absent (`brand_images configuration is required`), and additionally fails if any listed entry's `code` doesn't match an item's `attribute`/`brand` tag.
- This flow's `on_search` `defaultPayload` for provider `P1` had **no** `brand_images` tag at all — confirmed by reading `message.catalog["bpp/providers"][0].tags`, which had `order_value`, `timing`×4, `serviceability`×4, `retailer_info_required`×3 and nothing else.
- **Independent corroboration found while investigating:** `OnSearch.ts` (~L43-54) carries its own calibration comment, written by whoever last touched that validator: *"live with_offers(cod) 41 pass / 0 fail, spec cod 41/0, spec Prepaid 40/1. The one Prepaid failure is brand_images, a defect in the spec example; the rule stays mandatory."* This confirms the defect from an entirely independent source (the validator's own commit history), not just this prompt's hypothesis.
- Verified the catalog's actual brands by reading every item's `attribute`/`brand` tag directly: `I1`/`I2` → `Ashirwad`, `I3`/`I4` → `Fortune`, `I5`/`I6` → `Coca-Cola`, `I7`/`I8` → `Pepsi` — matches the prompt's claimed list exactly.

**Fix:** added, in the same relative position as the cod sibling's own `brand_images` tag:
```yaml
- code: brand_images
  list:
    - code: Ashirwad
      value: https://cdn.example.com/brands/Ashirwad.png
    - code: Fortune
      value: https://cdn.example.com/brands/fortune.png
    - code: Coca-Cola
      value: https://cdn.example.com/brands/coca-cola.png
    - code: Pepsi
      value: https://cdn.example.com/brands/pepsi.png
```
**Note on scope:** the cod sibling's own `brand_images` only lists 3 of its 4 actual brands (missing `Coca-Cola`, even though cod's catalog has `Coca-Cola` items I5/I6 too) — it currently passes validation only because the check verifies each *listed* entry matches a real brand, not that every real brand is listed. This prompt explicitly asked to verify the brand list against this flow's live items rather than just copy cod's (possibly incomplete) list, so all 4 brands are included here. Flagging cod's 3-brand list as a related, pre-existing gap — not fixed there, out of scope for this session.

### Hypothesis 2 (O1 — additive guard): confirmed, byte-for-byte the same bug as cod

Read `on_select_generate.js`'s `createQuote`: the guard was `if (!isAdditive && nonAdditiveApplied) continue;` — identical to the cod sibling flow, confirmed by diffing both files' guard lines directly. Same gap: blocks a second non-additive offer stacking on a first, but not an offer of either kind stacking on top of an already-non-additive-applied offer, nor a non-additive offer stacking on an already-additive-applied one.

**Fix** (identical to cod's, applied to this flow's own sidecar):
```js
// additive guard: additive "no" means this offer excludes every other offer, not
// just other non-additive ones. Once any offer has applied, a candidate can still
// apply only if both it and every already-applied offer are additive.
const metaList = catalogOffer.tags?.find(t => t.code === "meta")?.list || [];
const isAdditive = getListValue(metaList, "additive") !== "no";
if (appliedOfferIds.length > 0 && (!isAdditive || nonAdditiveApplied)) continue;
```

### Hypothesis 3 (O2 — order.offers drift): confirmed, with one structural difference from cod worth flagging

- Confirmed `on_select`'s `saveData` has no key for its computed `order.offers` — same gap as cod.
- Confirmed `on_init`, `on_confirm`, `on_status_accepted`, `on_status_packed`, `on_status_out_for_delivery`, `on_status_order_delivered` all independently rebuild `order.offers` from `sessionData?.selected_offers || []` — the buyer's raw opt-ins, never including auto-applied offers.
- Confirmed `on_status_agent_assigned` has **zero** offers code — `createGenericOnStatus` never touches `order.offers`, so it ships the `defaultPayload` template's hardcoded literal `offers: [{id: "discp10"}]` (verified by reading the template directly).
- **Difference from the cod sibling (reported per the ground rule "if your fix differs... report the difference"):** cod's `on_status_picked` had **no** offers code at all and needed a brand-new block. **This flow's `on_status_picked` already has the same offers-rebuild code as its five siblings** (`const selectedOffers = sessionData?.selected_offers || []; ...`) — so here it only needed the same one-line source swap as the other five legs, not a new block. The prompt's own evidence list already anticipated this (it cites `on_status_picked ~L319/321` alongside the other on_status legs, not alongside `on_status_agent_assigned`'s "hardcoded literal" callout) — confirmed by reading the code.

**Fix (parts A, B, C — identical pattern to cod):**
1. Added to `on_select`'s `saveData`: `applied_offers: $.message.order.offers[*]`.
2. In `on_init`, `on_confirm`, `on_status_accepted`, `on_status_packed`, `on_status_picked`, `on_status_out_for_delivery`, `on_status_order_delivered` (seven files — six `on_status_*` plus `on_init`/`on_confirm` is eight total minus `on_status_agent_assigned` which needed new code, see below): changed the offers source to:
   ```js
   const selectedOffers = sessionData?.applied_offers || sessionData?.selected_offers || [];
   ```
3. `on_status_agent_assigned`: added the same new offers block used for cod's equivalent leg (this one genuinely had no code to patch), including the `else { delete ... }` branch that removes the hardcoded `discp10` literal when there's nothing to carry forward.

## Verification

### 1. brand_images — real validator against the actual restored YAML

```
passed: ["on_search: provider P1 brand_images present and all 4 entry(ies) match item brand attributes"]
failed: []
```
Re-ran with the tag stripped (simulating the original defect): `failed: ["on_search: provider P1 brand_images configuration is required"]` — matches the calibration comment's description exactly.

### 2. O1 reproduced, then fixed (direct `createQuote`/`generate()` invocation)

Reused the same catalog (contract-matching `discp10`/`buy2get3`) and harness as the cod session, pointed at this flow's own sidecar:

| | `quote.breakup` applied offers | `order.offers` | Result |
|---|---|---|---|
| Before fix | `[discp10, buy2get3]` | `[discp10, buy2get3]` | **Illegal stacking reproduced** |
| After fix | `[discp10]` | `[discp10]` | Only the additive offer applies |

The inverse-order and legitimate-two-additive-offers cases were already verified generically against this exact guard algorithm in the cod session (the fixed condition is identical code, so the same isolated-logic unit test — 4 cases: live scenario, inverse order, two additive offers stacking, single non-additive offer alone — covers this flow's behavior too; not re-run here since it's the same expression, not flow-specific logic).

### 3. O2 reproduced, then fixed (direct `generate()` invocation, all 8 legs)

Same drift scenario as cod (`on_select` resolves `applied_offers = [discp10, autoAdd5]`; buyer's raw `selected_offers` is only `[discp10]`):

| Leg | Before fix | After fix |
|---|---|---|
| on_init | `[discp10]` (drift) | `[discp10, autoAdd5]` |
| on_confirm | `[discp10]` (drift) | `[discp10, autoAdd5]` |
| on_status_accepted | `[discp10]` (drift) | `[discp10, autoAdd5]` |
| on_status_packed | `[discp10]` (drift) | `[discp10, autoAdd5]` |
| on_status_agent_assigned | `[discp10]` (template literal, drift) | `[discp10, autoAdd5]` |
| on_status_picked | `[discp10]` (drift) | `[discp10, autoAdd5]` |
| on_status_out_for_delivery | `[discp10]` (drift) | `[discp10, autoAdd5]` |
| on_status_order_delivered | `[discp10]` (drift) | `[discp10, autoAdd5]` |

(One harness adjustment specific to this flow: `on_confirm`'s payment-mapping code calls a `generateRandomNumericId` helper not present in the sidecar; stubbed it in the test sandbox since it's unrelated to the offers logic being tested.)

### 4. Real report-service validators

```
on_select (O1 BEFORE): failed: ["...offer 'buy2get3' is non-additive (its offer tag's additive 'no') but is applied together with 'discp10'..."]
on_select (O1 AFTER):  passed: ["...only offer 'discp10' is applied — the stacking rule is not engaged"]

on_init (O2 BEFORE): failed: ["...order.offers [discp10, buy2get3] does not match the offers applied in quote.breakup [discp10] — ...listed but not applied: offer 'buy2get3'"]
on_init (O2 AFTER):  passed: ["...order.offers matches the offers applied in quote.breakup (discp10)"]
```
Message text matches the live-run symptoms.

**Scope note (same as the cod session):** verified these specific validator rules directly rather than reconstructing the full in-memory, Redis-stubbed `validationModule` replay across all steps (no such harness exists currently). The prompt's "expect 10 real failures → 0" count is the per-leg sum of: 1 brand_images failure + 1 stacking failure at `on_select` + up to 1 drift failure at each of 8 downstream legs — the transitions above are the per-rule equivalent of that count.

### 5. Diff scope

Confirmed via `git diff --stat` + mapping every changed line number back to its `action_id`: exactly `on_search`, `on_select` (×2), `on_init`, `on_confirm`, and all six `on_status_*` steps changed. Nothing else.

## Cross-flow / cross-repo findings (confirmed, not fixed — out of scope here)

1. **The cod sibling's own `brand_images` is missing `Coca-Cola`**, despite cod's catalog having `Coca-Cola` items (I5/I6) — confirmed by reading `Order_to_confirm_to_fulfillment_with_offers__cod_.yaml` directly. Currently passes validation only because the check doesn't require full brand coverage. Not fixed here (out of scope — the ground rules say don't edit the cod sibling).
2. **`confirm_generate.js`** (the buyer-authored step, not `on_confirm`) has the identical `sessionData?.selected_offers || []` pattern — confirmed by reading it, matching the identical finding already reported for the cod flow's `confirm_generate.js`. Not in this prompt's diff scope (which lists `on_init`/`on_confirm`/the six `on_status_*` steps, not `confirm`), so left untouched. Same open question as flagged for cod: this may be intentional (the buyer's own echo of their raw opt-ins) rather than a bug.
3. **`automation-config-service`'s mirror is not simply an unfixed copy of this repo's bug — it's structurally different code.** Confirmed by reading its `on_select` generator directly: it has no `brand_images` tag and no `applied_offers` saveData key (same end-state as this repo's pre-fix version), but its additive-handling logic is a different, simpler implementation that has **no stacking guard at all** (`nonAdditive` doesn't appear anywhere in that file) — it unconditionally applies every offer that passes its qualifier check, which is arguably a *worse* defect than this repo's partial guard, not the same one. Reported as-is per the ground rules (no sync gap to chase since nothing was fixed there), but worth flagging precisely rather than assuming byte-identical code.

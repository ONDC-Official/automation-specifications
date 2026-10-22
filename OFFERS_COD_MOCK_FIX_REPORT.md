# Offer stacking + order.offers drift fix: Order_to_confirm_to_fulfillment_with_offers(cod) (RETeB2B 1.2.5)

- **Date:** 2026-10-16
- **Branch:** `draft-RETeB2B`. This session committed nothing.
- **File changed:** `config/flows/eB2B/Order_to_confirm_to_fulfillment_with_offers__cod_.yaml` only. `git diff --stat` = 10 insertions/9 deletions across exactly 9 line-locations: `on_select`'s `generate`, `on_select`'s `saveData` (1 new line), and the `generate` field of `on_init`, `on_confirm`, and all six `on_status_*` steps. Nothing else in the 6,300+ line file changed — verified by mapping every changed line number back to its `action_id`.
- **Contract:** `/tmp/ebb2b_doc.txt` (~L5080–5420, "Schemes"). The contract's only prose on stacking is the Meta-rules table row: `additive (combinable with other offers)`. It gives no example of two offers evaluated in sequence, so the exact stacking condition (O1) is this session's reading of "combinable with other offers," cross-checked against the live-run symptom and the "test the inverse case" instruction, not a literal contract quote.
- **Method:** extracted fresh with `extract-flow.ts`, edited sidecars + the one plain-YAML `saveData` line in the dev wrapper, restored with `restore-flow.ts`. Reproduced both hypotheses and their fixes by invoking the real sidecar `generate()`/`createQuote()` functions directly (Node `vm`). Ran the real report-service checks (`validateOfferStacking` and `validateOrderOffersMatchApplied`, `offerChecks.ts`) directly against before/after order objects.

## Verdict: Both hypotheses confirmed

### O1: additive guard only blocked non-additive-on-non-additive. Confirmed.

Read `on_select_generate.js`'s `createQuote`. The guard was exactly as hypothesized:
```js
const isAdditive = getListValue(metaList, "additive") !== "no";
if (!isAdditive && nonAdditiveApplied) continue;
```
Traced it by hand for the live scenario (buyer opts into `discp10`, additive `yes`, evaluated first and applied; `nonAdditiveApplied` stays `false` because it's only set when the *applied* offer is non-additive; then catalog auto-offer `buy2get3`, additive `no`, is evaluated — `!isAdditive (true) && nonAdditiveApplied (false)` is `false`, so it is **not** blocked) — confirms the gap exactly as described: the guard only ever stops a *second* non-additive offer from stacking on a *first* one; it never stops a non-additive offer from stacking on an already-applied *additive* one, or vice versa.

### O2: order.offers rebuilt independently at every later leg. Confirmed, including both claimed exceptions.

- `on_select`'s `createQuote` correctly computes and returns `appliedOfferIds`, and `generate()` sets `defaultPayload.message.order.offers` from it (`on_select_generate.js:297-299`).
- Confirmed by direct read that `on_init`, `on_confirm`, `on_status_accepted`, `on_status_packed`, `on_status_out_for_delivery`, `on_status_order_delivered` **all** independently did:
  ```js
  const rawOffers = sessionData?.selected_offers || sessionData?.user_inputs?.available_offers || [];
  ```
  — the buyer's raw select-time opt-in list, never including auto-applied offers.
- Confirmed `on_status_agent_assigned` had **zero** offers-related code in its `generate()` — its `createGenericOnStatus` helper never touches `order.offers`, so the live payload shipped whatever the step's `defaultPayload` template literally contains. Read that template directly (plain YAML, not base64): `offers: [{id: discp10}]` — a hardcoded literal, exactly as the prompt said.
- Confirmed `on_status_picked` had **no offers-related code at all**, and its `defaultPayload` template has **no `offers` key whatsoever** — so the live payload ships `order.offers = undefined` (missing), exactly matching the live-run symptom `on_status_picked: order.offers is missing`.
- Confirmed `on_select`'s `saveData` had no key saving its computed `order.offers` anywhere — `selected_offers` (from the `select` step, not `on_select`) is the buyer's raw opt-ins, a different thing.

**Contract check (O2 step 4):** `/tmp/ebb2b_doc.txt` has no leg-specific definition of `order.offers`'s meaning — it only appears in the `on_select`/`select` Apply examples (~L5099-5420), which show offers as the seller's set of applied discounts on the quote. Nothing suggests a different meaning at later legs. The prompt's reading ("the seller's full set of applied offers, unchanged from on_select onward") stands unrefuted.

## The fixes

### Fix 1 (O1) — `on_select_generate.js`, the additive guard:
```js
// additive guard: additive "no" means this offer excludes every other offer, not
// just other non-additive ones. Once any offer has applied, a candidate can still
// apply only if both it and every already-applied offer are additive.
const metaList = catalogOffer.tags?.find(t => t.code === "meta")?.list || [];
const isAdditive = getListValue(metaList, "additive") !== "no";
if (appliedOfferIds.length > 0 && (!isAdditive || nonAdditiveApplied)) continue;
```

### Fix 2 (O2, part A) — `on_select`'s `saveData` (plain YAML, edited directly in the dev wrapper, not base64):
```yaml
applied_offers: $.message.order.offers[*]
```

### Fix 3 (O2, part B) — `on_init`, `on_confirm`, `on_status_accepted`, `on_status_packed`, `on_status_out_for_delivery`, `on_status_order_delivered`: changed the offers source to prefer the carried-forward set, falling back to the old sources for robustness:
```js
const rawOffers = sessionData?.applied_offers || sessionData?.selected_offers || sessionData?.user_inputs?.available_offers || [];
```
The rest of each leg's logic (map to `{id}`, assign to `order.offers`) is untouched — this carries the value forward unchanged, the same way `quote` already is in these generators.

### Fix 4 (O2, part C) — `on_status_agent_assigned` and `on_status_picked`: added the same offers block these legs were missing (new code, not a one-line swap, since neither had any offers logic to patch):
```js
/* --- ✅ NEW: RETRIEVE & MAP OFFERS --- */
const rawOffers = sessionData?.applied_offers || sessionData?.selected_offers || sessionData?.user_inputs?.available_offers || [];
const selectedOffers = Array.isArray(rawOffers) ? rawOffers : [rawOffers];

if (selectedOffers.length > 0) {
  generalPayload.message.order.offers = selectedOffers
    .filter(o => o)
    .map(offer => ({ id: typeof offer === 'string' ? offer : (offer.id || offer.offerId) }));
} else {
  delete generalPayload.message.order.offers;
}
```
Inserted right after each leg's existing customer-restore block, matching where the other legs do the equivalent work. The `else { delete ... }` branch (matching `on_init`'s existing pattern) also removes `on_status_agent_assigned`'s hardcoded `discp10` template literal when there's genuinely nothing to carry forward.

## Verification

### 1. O1 reproduced, then fixed (direct `createQuote`/`generate()` invocation)

Built a catalog matching the contract's own `discp10` (additive yes, auto yes) and `buy2get3` (additive no, auto yes) examples, with a buyer opting into `discp10` only:

| | `quote.breakup` applied offers | `order.offers` | Result |
|---|---|---|---|
| **Before fix** | `[discp10, buy2get3]` | `[discp10, buy2get3]` | **Illegal stacking reproduced** — matches the live-run symptom exactly |
| **After fix** | `[discp10]` | `[discp10]` | Only the additive offer applies |

Also tested (per "Verify your fix" step 3):
- **Inverse order** (non-additive evaluated first, additive second): blocked correctly either direction — isolated-logic unit test confirms `['buy2get3']` only, regardless of which offer is evaluated first.
- **Two additive offers stacking** (hypothetical `discp10` + a second additive offer): **not** blocked — confirms the fix doesn't over-block legitimate stacking.

### 2. O2 reproduced, then fixed (direct `generate()` invocation, all 8 legs)

Simulated `on_select` having correctly resolved `applied_offers = [discp10, autoAdd5]` (two legitimately-stacked additive offers) while the buyer's raw `selected_offers` was only `[discp10]` — the drift scenario:

| Leg | Before fix (`applied_offers` absent) | After fix (`applied_offers` present) |
|---|---|---|
| on_init | `[discp10]` (drift) | `[discp10, autoAdd5]` |
| on_confirm | `[discp10]` (drift) | `[discp10, autoAdd5]` |
| on_status_accepted | `[discp10]` (drift) | `[discp10, autoAdd5]` |
| on_status_packed | `[discp10]` (drift) | `[discp10, autoAdd5]` |
| on_status_agent_assigned | `[discp10]` (template literal, drift) | `[discp10, autoAdd5]` |
| on_status_picked | `[discp10]` (fallback kicked in; template has none) | `[discp10, autoAdd5]` |
| on_status_out_for_delivery | `[discp10]` (drift) | `[discp10, autoAdd5]` |
| on_status_order_delivered | `[discp10]` (drift) | `[discp10, autoAdd5]` |

All 8 legs now carry the identical, correct applied-offer set end to end.

### 3. Real report-service validators

Ran the actual check functions directly (`automation-report-service/src/validations/ONDC:RETeB2B/1.2.5/offerChecks.ts`):

**`validateOfferStacking`** (O1):
```
on_select (BEFORE): failed: ["...offer 'buy2get3' is non-additive (its offer tag's additive 'no') but is applied together with 'discp10' — a non-additive offer cannot be combined with other offers"]
on_select (AFTER):  passed: ["...only offer 'discp10' is applied — the stacking rule is not engaged"]
```

**`validateOrderOffersMatchApplied`** (O2):
```
on_init (BEFORE): failed: ["...order.offers [discp10, buy2get3] does not match the offers applied in quote.breakup [discp10] — ...listed but not applied: offer 'buy2get3'"]
on_init (AFTER):  passed: ["...order.offers matches the offers applied in quote.breakup (discp10)"]
on_status_picked (BEFORE, no `offers` key at all): failed: ["...order.offers is missing, but quote.breakup applies offer 'discp10'"]
```
Message text matches the live-run symptoms verbatim.

**Scope note:** verified these two specific validator rules directly, the same way the BIR/COD-location sessions did, rather than reconstructing the full in-memory, Redis-stubbed `validationModule` replay across all steps (the prompt's "expect 9 real failures → 0" count would require that full harness, which no longer exists from any prior session). The before/after transitions above are the per-rule equivalent of that count: 1 stacking failure at `on_select` + up to 1 drift failure at each of 8 downstream legs = the same shape of failures the live run reported.

### 4. Diff scope

`git diff --stat` + line-number-to-`action_id` mapping (above) confirms the change touches exactly: `on_select`'s `generate` and `saveData`, and the `generate` field of `on_init`, `on_confirm`, and all six `on_status_*` steps — nothing else, matching the ground rule exactly.

## Cross-flow / cross-repo findings (confirmed, not fixed — out of scope here)

1. **`Order_to_confirm_to_fulfillment_with_offers__Prepaid_.yaml` has the same O1 bug** — confirmed by reading its `on_select` generator: byte-identical buggy guard (`if (!isAdditive && nonAdditiveApplied) continue;`), and no `applied_offers` saveData key.
2. **Prepaid has the same O2 pattern, with one structural difference worth flagging for that session:** `on_confirm` and `on_status_accepted/packed/out_for_delivery/order_delivered` all read `sessionData?.selected_offers` (same drift). `on_status_agent_assigned` has **no** offers code at all (same as COD). But **`on_status_picked` in Prepaid already HAS offers-handling code that reads `selected_offers`** — unlike COD, where this leg had no offers code whatsoever. So the fix "applies almost verbatim" as the prompt anticipated, but Prepaid's `on_status_picked` needs the one-line source swap (like the other `on_status_*` legs), not a whole new block the way COD's did. Reported for the Prepaid session, not fixed here.
3. **`automation-config-service`'s mirror has the identical, unfixed O1 bug and no `applied_offers` key** (`src/config/RETeB2B/v-1.2.5/EB2B/flows/Order_to_confirm_to_fulfillment_with_offers(cod).yaml`) — confirmed by direct read, no edits made. Per the ground rules, this is not a sync gap (the bug was never fixed there to begin with), just the mirror's current (also-buggy) state, reported for completeness.
4. **`confirm_generate.js`** (the BAP-authored buyer step, not `on_confirm`) has the **identical** `sessionData?.selected_offers || sessionData?.user_inputs?.available_offers` pattern as the fixed legs. The prompt's explicit diff-scope list (`on_select`'s guard/saveData, and `on_init`/`on_confirm`/the six `on_status_*` legs — "nothing else") does not include `confirm`, so it was left untouched and is reported here rather than fixed. Worth deciding in a follow-up: since `confirm` represents the buyer's own request, it's plausible `order.offers` there is supposed to echo the buyer's opt-ins (not the seller's auto-applied additions) — i.e. this may not actually be a bug, just a different, legitimate meaning of `order.offers` for a BAP-authored step. Flagging rather than guessing.

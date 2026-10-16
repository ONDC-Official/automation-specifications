# Re-select quantity fix: Out_of_Stock(Error_code) (RETeB2B 1.2.5)

- **Date:** 2026-10-16
- **Branch:** `draft-RETeB2B`. This session committed nothing.
- **File changed:** `config/flows/eB2B/Out_of_Stock_Error_code_.yaml` only. `git diff --stat` = 2 insertions/2 deletions across exactly 2 lines: `on_select_out_of_stock`'s `generate` and `select`'s `generate` (the retry step) — confirmed by mapping both changed line numbers to their `action_id`. Nothing else in the file changed.
- **Contract:** `/tmp/ebb2b_doc.txt`.
- **Method:** extracted fresh with `extract-flow.ts`, edited both sidecars, restored with `restore-flow.ts`. Reproduced the bug and the fix by invoking the real `on_select_out_of_stock_generate.js` → `select_generate.js` pipeline directly (Node `vm`, real `Math.random`, not stubbed) across many runs to hit the random OOS branch on both candidate items. Ran the real report-service check (`validateRetrySelectAgainstOutOfStock`, `selectChecks.ts:440`) directly against before/after retry payloads.

## Verdict: confirmed, with one important correction to the prompt's framing

Both code-level claims in the hypothesis are confirmed exactly as described:

1. **`on_select_out_of_stock`'s `order.items[].quantity.count` never reflects the OOS-adjusted `finalQty`** — confirmed by reading the code: `createQuote`'s breakup gets `finalQty`, but the separate `order.items = items.map(...)` block (built *before* `createQuote` even ran) uses `item.quantity?.count ?? 1`, the original requested quantity.
2. **The retry `select`'s quantity has no clamp** — confirmed: `quantity: { count: Number(item.quantity) }`, with the saved-items fallback used only for `location_id`/`fulfillment_id`, never quantity.

**Correction to the prompt's framing:** the prompt frames these as the cause of the live-run symptom (`select: item I1 is re-selected with quantity.count 12, but the previous on_select reported only 11 available`). Tracing the *actual* validator that produces that message (`validateRetrySelectAgainstOutOfStock`, `selectChecks.ts:440`) shows it reads its ceiling from `error.message`'s `available_count` field — which comes straight from `createQuote`'s `oosItems.push({..., available_count: finalQty})`, a value that **was never buggy**. So defect #1 (`order.items` vs `quote.breakup` within the *same* `on_select_out_of_stock` payload) is a real, independently-confirmed internal-consistency defect, but it is not what this specific validator checks, and fixing it alone would not have changed this check's pass/fail outcome. Defect #2 (the retry's missing clamp) is what actually drives the live-run symptom. Both are still worth fixing — #1 is a real contract-consistency bug in its own right — but they are not the same bug wearing two hats, and the report-service validator only exercises #2 directly.

## The fixes

### Fix 1 — `on_select_out_of_stock_generate.js`: echo the OOS-adjusted quantity

Reordered so `createQuote` (which computes `finalQty` per item, including the OOS reduction) runs *before* `order.items` is built, then used its own `oosItems` output (which already carries the correct `available_count` per OOS item) to set the matching item's quantity:

```js
const quote = createQuote(items, sessionData, order.fulfillments);

const availableQtyByItemId = {};
quote.oosItems.forEach((oi) => { availableQtyByItemId[oi.item_id] = oi.available_count; });

order.items = items.map(item => ({
  id: item.id,
  fulfillment_id: item.fulfillment_id || order.fulfillments?.[0]?.id || "F1",
  location_id: item.location_id,
  quantity: {
    count: availableQtyByItemId[item.id] ?? (item.quantity?.count ?? 1)
  }
}));
```
Non-OOS items are untouched (`availableQtyByItemId` has no entry for them, so they fall back to the original requested quantity — which is also what `createQuote`'s breakup reports for them, since `finalQty = requestedQty` when not OOS).

### Fix 2 — `select_generate.js` (the retry): clamp against what was actually reported available

No `saveData` changes needed: `on_select_out_of_stock`'s existing `saveData` key `on_select_items: $.message.order.items[*]` already captures the step's output — and after fix 1, that output's `quantity.count` is the correct availability ceiling for every item (reduced for whichever one got randomly marked OOS, unchanged for the rest). Added a clamp that reads it:

```js
const previouslyAvailableByItemId = {};
(Array.isArray(sessionData?.on_select_items) ? sessionData.on_select_items.flat(2) : []).forEach((oi) => {
  if (oi?.id && oi?.quantity?.count != null) previouslyAvailableByItemId[oi.id] = oi.quantity.count;
});

finalItems = inputs.items.map((item) => {
  const requestedQty = Number(item.quantity);
  const availableQty = previouslyAvailableByItemId[item.itemId];
  return {
    ...,
    quantity: { count: availableQty != null ? Math.min(requestedQty, availableQty) : requestedQty },
    ...
  };
});
```

## Is fix 1 alone self-correcting for fix 2? Traced, not assumed: **no — and the dependency runs both ways**

Per the prompt's instruction not to assume, I traced the actual data flow and verified it empirically (see Verification §1):

- The retry `select_generate.js`'s existing fallback logic (`locationByItemId`/`fulfillmentByItemId`) reads `sessionData.selected_items` — **`select0`'s saved items, the buyer's original pre-OOS request** — not `on_select_out_of_stock`'s output. It never reads `on_select_items` at all before this fix. So fix 1 changing `on_select_out_of_stock`'s own payload has **zero** effect on the retry unless fix 2 is also applied — confirmed empirically: fix 1 alone, fix 2 reverted, still violates on every single run (30/30).
- Conversely, fix 2 **depends on** fix 1: the clamp reads `sessionData.on_select_items`, and without fix 1 that array still carries the unclamped original quantity, so clamping against it is a no-op — confirmed empirically: fix 2 alone, fix 1 reverted, still violates on every run (30/30, both the fix-1-style inconsistency and the fix-2-style over-selection).
- Only with **both** fixes applied does the retry respect the previously-reported availability — confirmed across 60 runs with real (unstubbed) randomness, hitting both candidate items as the random OOS pick, 0 violations.

## Verification

### 1. Reproduced, then fixed — direct pipeline invocation across many random seeds

Built a two-item catalog (`I1`, `I2`, ample stock) and ran the real `on_select_out_of_stock_generate.js` → `select_generate.js` pipeline with a requested quantity of 12 for both items (matching the live run), using real `Math.random` (not stubbed) so the random OOS pick varies run to run:

| Combination | Runs | Violations |
|---|---|---|
| Both BEFORE | 40 | 80 (2/run: the on_select_out_of_stock internal inconsistency + the retry over-selection) |
| Fix 1 only (fix 2 reverted) | 30 | 30/30 — retry still violates every run |
| Fix 2 only (fix 1 reverted) | 30 | 60 (both violation types still fire every run) |
| Both AFTER | 60 | **0** |

The "both AFTER" run observed both `I1` and `I2` as the random OOS pick across the 60 seeds, confirming the fix holds regardless of which item the random index lands on — not a one-item coincidence.

A ground-truth note on the harness: the oracle for "what was actually available" was `quote.breakup[]["@ondc/org/item_quantity"].count` (the quantity `createQuote` actually priced, i.e. `finalQty`) — not `item.quantity.available.count` (remaining catalog stock, a different number that stays at the catalog's full stock count for non-OOS items and is therefore not a valid ceiling for "what was ordered").

### 2. Real report-service validator

Ran `validateRetrySelectAgainstOutOfStock` (`selectChecks.ts:440`) directly:
```
select retry (BEFORE fix 2): failed: ["select: item I1 is re-selected with quantity.count 12, but the previous on_select reported only 11 available"]
select retry (AFTER fix 2):  passed: ["select: all 1 previously out-of-stock item(s) respected — 0 dropped, 1 re-selected within the available quantity (I1: 11 of 11)"]
```
Message text matches the live run exactly. As noted above, this check's `available` ceiling comes from `error.message`'s `available_count` (always correct), so this specific pass/fail transition demonstrates fix 2; it does not exercise fix 1 (which has no existing validator coverage found — see "Residual" below).

**Scope note:** verified this specific rule directly rather than reconstructing the full in-memory, Redis-stubbed `validationModule` replay (no such harness currently exists in this repo from any prior session). The validator's own code comments were themselves useful corroboration here — see "Calibration note" in `selectChecks.ts` (quoted below) confirming the expected behavior independently of this prompt.

### 3. Diff scope

`git diff --stat` + line-to-`action_id` mapping confirms exactly 2 lines changed, one in each of the two named generators, nothing else in the 460+ line file.

### 4. `automation-config-service` mirror (read-only, not edited)

Confirmed by direct read: `src/config/RETeB2B/v-1.2.5/EB2B/flows/Out_of_Stock(Error_code).yaml` has the byte-identical pre-fix `on_select_out_of_stock` quantity line and no clamp logic in its `select` step — consistent with the ground rule that this bug hasn't been fixed anywhere yet, so there's no sync gap, just the (also-buggy) mirror state as reported.

## Independent corroboration found while investigating

`selectChecks.ts`'s own code comments (immediately above `validateRetrySelectAgainstOutOfStock`) independently describe and calibrate against exactly this scenario, written by whoever last touched that validator:

> *"Calibration note: the spec's own second-select example re-selects I1 at count 1 after the rejection reported 0 available, so it legitimately fails this check. The static examples were written without running the flow's mock... the live mock sets available = requested - 1 and builds the retry from user-entered quantities, so a real 12 -> 11 session has a compliant retry at <= 11."*

This confirms, from an entirely independent source (the validator's own commit history), the exact `12 -> 11` arithmetic this session's live run and fix are built around.

## Residual / not fixed

1. **No existing report-service check validates `on_select_out_of_stock`'s internal `order.items` vs `quote.breakup` consistency** (fix 1's own target). Searched `orderFormationChecks.ts`, `offerChecks.ts`, `selectChecks.ts`, `returnChecks.ts` for a quantity-consistency rule scoped to a single payload rather than cross-leg; found none. Fix 1 is still correct and worth keeping (the payload is clearly internally inconsistent independent of any validator), but it has no current test coverage of its own beyond this session's direct-invocation harness. Flagging as a possible future validator gap, not fixing the validator (out of scope).
2. **`automation-config-service`'s mirror has the identical, unfixed bug in both generators** — confirmed, not fixed, per the ground rules (no sync gap to chase since nothing was ever fixed there).

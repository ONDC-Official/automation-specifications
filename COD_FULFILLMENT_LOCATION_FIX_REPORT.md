# COD fulfillment start-location fix: Order_to_confirm_to_fulfillment_(cod) (RETeB2B 1.2.5)

- **Date:** 2026-10-16
- **Branch:** `draft-RETeB2B`. This session committed nothing.
- **File changed:** `config/flows/eB2B/Order_to_confirm_to_fulfillment__cod_.yaml` — only the `on_confirm` step's `mock.generate` field. `git diff` touches exactly one line (the base64 blob on that line, 1 insertion / 1 deletion).
- **Contract:** `/tmp/ebb2b_doc.txt`.
- **Method:** extracted the flow fresh with `extract-flow.ts`, edited the `on_confirm_generate.js` sidecar, restored with `restore-flow.ts`. Reproduced the defect and the fix by invoking the real sidecar `generate()` directly (Node `vm`, stubbing only the irrelevant `applyDynamicTimestamps`) with `sessionData` shaped the way `select`→`confirm` save it for this flow. Also ran the real report-service check function (`validateShipFromLocation`, `orderFormationChecks.ts:1406`) directly against before/after order objects.

## Verdict: Confirmed

The hypothesis is correct and matches `BIR_FULFILLMENT_LOCATION_FIX_PROMPT.md`'s finding for the sibling BIR flow exactly: `on_confirm`'s fulfillment restore only ever assigns `order.fulfillments[0].customer`:
```js
if (order.fulfillments?.length && savedFulfillments.length > 0) {
  const firstFulfillment = savedFulfillments?.[0];
  if (firstFulfillment?.customer) order.fulfillments[0].customer = firstFulfillment.customer;
}
```
`start` is never touched, so `order.fulfillments[0].start.location.id` always ships the `defaultPayload` template's static `"L1"` (Jayanagar warehouse, `12.9563,77.6368`). Separately, `order.provider = sessionData.provider[0]` (later in the same function) replaces the whole provider object with whatever `select` resolved from the pasted catalog — which can be `[{id: "L2"}]` if that's where the catalog places the item. Result: the payload claims to ship from a location the provider doesn't declare, exactly the live-run symptom: `fulfillment F1 ships from location 'L1', which is not one of the provider's declared locations (L2)`.

**Confirmed `select`'s provider-location resolution (verified by reading `select_generate.js`, byte-identical to BIR's):**
```js
const itemLocationIds = [...new Set(finalItems.map((i) => i.location_id).filter(Boolean))];
const catalogLocationIds = (catalogProvider.locations || []).map((l) => l.id).filter(Boolean);
const locationIds = itemLocationIds.length > 0 ? itemLocationIds : catalogLocationIds.slice(0, 1);
if (locationIds.length > 0) provider.locations = locationIds.map((id) => ({ id }));
```
This matches the prompt's hypothesis exactly, including the fact that only the bare `{id}` survives — `catalogProvider.locations`' richer `{id, gps, address}` objects (from the pasted `live_catalog` / `RETeB2BCatalog` fallback) are discarded before `provider.locations = ...` is saved.

## Where the richer start-location data would come from, and why it isn't available

Checked whether `live_catalog`'s full location object (gps/address) is saved anywhere `on_confirm` can reach, per the prompt's explicit ask:
- `select`'s `saveData.provider: $.message.order.provider` saves only the bare-`{id}` shape built above — nothing richer.
- `select`'s `saveData.RETeB2BCatalog: EVAL#...` is a static hardcoded fallback catalog (used only as `select_generate.js`'s/`on_select`'s last-resort source when no live catalog is pasted), not a capture of whatever was actually pasted, and no generator in this flow reads it for the *start* location.
- Traced `saved_items` (which `on_confirm` reads) back through `confirm_generate.js`: it builds `location_id` with a 3-way fallback (`item.location_id` → `item.location` → `locationByItemId[item.id]`, backfilled from `select`'s own `selected_items`) — so `location_id` is reliable by the time `on_confirm` runs, but it's still just an id, never gps/address.

**Conclusion: no step in this flow saves a richer location object than `{id}` anywhere `on_confirm` can read it.** Per the prompt's fallback guidance, the fix syncs only `start.location.id`, leaving the template's placeholder `gps`/`address`/`contact` as a residual, unfixable-from-session-data gap (flagged below), and does not invent data for them.

## The fix

Added a new block in `on_confirm_generate.js`, directly after the existing customer-restore block (which is untouched), before the items/quote/payment logic (also untouched):

```js
/* ---------------- START LOCATION ---------------- */
if (order.fulfillments?.[0]?.start?.location) {
  const fulfillmentId = order.fulfillments[0].id || defaultFulfillmentId;
  const providerLocationIds = Array.isArray(sessionData?.provider?.[0]?.locations)
    ? sessionData.provider[0].locations.map((l) => l.id).filter(Boolean)
    : [];
  const matchingItem = savedItems.find(
    (item) => (item.fulfillment_id || defaultFulfillmentId) === fulfillmentId
  );
  const resolvedLocationId =
    matchingItem?.location_id ||
    matchingItem?.location ||
    providerLocationIds[0] ||
    order.fulfillments[0].start.location.id;

  if (resolvedLocationId) {
    order.fulfillments[0].start.location.id = resolvedLocationId;
  }
}
```
`matchingItem` reads `savedItems`, which is the same array the existing "ITEMS" block (right below, unchanged) builds `order.items` from — so `start.location.id` and `order.items[].location_id` are always derived from one consistent source. This mirrors the fix applied to the sibling BIR flow and avoids a real cross-field-inconsistency failure mode documented in `orderFormationChecks.ts` (see "Important context" below).

This flow's `on_confirm` only ever has one fulfillment (`order.fulfillments[0]`, confirmed from the `defaultPayload` template — a single-element `fulfillments` array), so the fix is scoped to index `[0]`, consistent with how the existing customer-restore code already does.

Per the ground rules, the payment/quote sync (`defaultPayload.message.order.payments[0].params.amount = savedQuote[0].price.value`) was left completely untouched and verified still correct (see Verification §2).

## Verification

### 1. Reproduced the live failure, then the fix (direct generate() invocation)

Built `sessionData` matching what `select`→`confirm` save for this flow, for a provider whose only declared location is `L2`:

| | `provider.locations[].id` | `fulfillment.start.location.id` | Result |
|---|---|---|---|
| **Before fix** | `["L2"]` | `"L1"` | **Contract violation reproduced** — matches the live-run symptom exactly |
| **After fix** | `["L2"]` | `"L2"` | Passes |

Re-ran the happy-path case (provider's only location is `L1`, matching the template) — `start.location.id` stays `"L1"`, no regression.

### 2. Payment/quote sync untouched (explicit ground-rule check)

Ran the fixed generator with `sessionData.quote = [{ price: { value: "624.00" } }]` and a default-template payment of `1150.00`: `payments[0].params.amount` came out `"624.00"` — the existing sync logic is unaffected by the new block.

### 3. Real report-service validator

Ran `validateShipFromLocation` (`automation-report-service/src/validations/ONDC:RETeB2B/1.2.5/orderFormationChecks.ts:1406`) directly against before/after `order` objects:

```
--- on_confirm (BEFORE fix) ---
failed: ["...: fulfillment F1 ships from location 'L1', which is not one of the provider's declared locations (L2)"]

--- on_confirm (AFTER fix) ---
passed: ["...: ship-from location id/gps valid on all declared fulfillment starts"]
failed: []
```
Same rule, same message text as the live run reported for this flow.

**Scope note (same as the BIR session):** verified the specific validator rule directly rather than reconstructing the full in-memory, Redis-stubbed `validationModule`/`checkPayload` end-to-end replay across every step (that harness lived in a now-gone session scratchpad). If an exact before/after pass/fail *count* across the whole flow is required, that harness would need to be rebuilt.

### 4. Round-trip / diff scope

- `extract-flow.ts` → edit → `restore-flow.ts`: `git diff` on the flow YAML shows exactly 1 line changed (the `on_confirm` step's `mock.generate` base64).
- Decoded the restored YAML's `on_confirm` generator: confirmed present and unchanged — the payment/quote sync (`savedQuote[0].price.value`), the offers-array persistence block, and the billing-timestamp restore block — alongside the new location-sync block.

### 5. Cross-flow check (confirmed, not fixed — out of scope here)

Read (did not edit) `Order_to_confirm_to_fulfillment__Prepaid_.yaml`'s `on_confirm` generator. **Same bug pattern confirmed**: it restores `order.fulfillments[0].customer` and forces `order.fulfillments[0].state`, but never touches `start`; `order.provider = sessionData.provider[0]` happens separately. So this flow's `start.location.id` can equally mismatch the resolved provider's locations — it just wasn't observed failing in the 2026-10-16 live run, which the prompt already anticipated could simply mean that run's provider happened to resolve to `L1`. Not fixed, per ground rules.

Also did **not** edit `Buyer_Initiated_Return__Full_Order_and_Partial_Order_.yaml` or `../automation-config-service`, per ground rules — the former was fixed in a separate pass (see `BIR_FULFILLMENT_LOCATION_FIX_REPORT.md`), and the latter is out of scope / a separate deployment-sync concern.

## Important context found in report-service (carried over from the BIR session; load-bearing for anyone touching this check later)

`orderFormationChecks.ts` carries a long comment directly above `validateShipFromLocation` (added 2026-10-13) warning against re-anchoring the ship-from check on the seller's **catalog** locations instead of the payload's own `order.provider.locations` — an earlier investigation found a real mock defect that re-anchoring would have silently hidden (in `Out_of_Stock_Error_code_`, `items[].location_id` itself flips only at `on_confirm` and reverts afterward). This fix's `providerLocationIds` correctly reads `sessionData.provider[0].locations`, which becomes `order.provider` in the same `on_confirm` payload — the check's intended anchor. Not a defect here, but worth knowing before touching this check or the Prepaid flow's equivalent fix.

## Residual gaps (not fixed, flagged per the prompt)

1. **`start.location`'s address/gps/contact stay the template's placeholder** (`ABC Distributors Warehouse`, Jayanagar, `12.9563,77.6368`) even after the id fix — no step in this flow saves a richer location object than `{id}`. Only the `id` was syncable from available session data; no data was invented for the rest.
2. **`Order_to_confirm_to_fulfillment__Prepaid_.yaml`'s `on_confirm` has the identical bug pattern** — confirmed by reading its generator (§5), not fixed here.
3. This flow's `on_confirm`, unlike BIR's, has no hardcoded `"L1"` fallback in its own items-restore block (`...(item.location_id ? { location_id: item.location_id } : {})` — no `|| "L1"`), so there's no equivalent secondary dormant-fallback issue to flag here.

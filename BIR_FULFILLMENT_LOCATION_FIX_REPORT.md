# BIR fulfillment start-location fix: Buyer_Initiated_Return_(Full_Order_and_Partial_Order) (RETeB2B 1.2.5)

- **Date:** 2026-10-16
- **Branch:** `draft-RETeB2B`. This session committed nothing.
- **File changed:** `config/flows/eB2B/Buyer_Initiated_Return__Full_Order_and_Partial_Order_.yaml` — only the `on_confirm` step's `mock.generate` field. `git diff` touches exactly one line (the base64 blob on that line).
- **Contract:** `/tmp/ebb2b_doc.txt`.
- **Method:** extracted the flow with `extract-flow.ts`, edited the `on_confirm_generate.js` sidecar, restored with `restore-flow.ts`. Reproduced the defect and the fix by invoking the real sidecar `generate()` directly (Node `vm`, stubbing only the irrelevant `applyDynamicTimestamps`) with `sessionData` shaped the way `select`→`confirm` save it. Also ran the actual report-service check function (`validateShipFromLocation`, `orderFormationChecks.ts:1406`) directly against before/after order objects.

## Verdict: Confirmed

The hypothesis is correct. `on_confirm`'s fulfillment-rebuild step never touched `start`, so `start.location.id` always shipped the template's static `"L1"` regardless of what provider the flow actually resolved.

**Evidence (before fix, `on_confirm_generate.js`):**
```js
if (order.fulfillments?.length && savedFulfillments.length > 0) {
  const templateFulfillments = order.fulfillments;
  order.fulfillments = savedFulfillments.map((f) => {
    const base = templateFulfillments.find((t) => t.id === f.id) || templateFulfillments[0];
    return { ...base, id: f.id, type: f.type, ...TAT, ...customer, end: f.end };
    // base supplies `start` untouched — including `start.location.id: "L1"`
  });
}
...
if (sessionData?.provider) {
  defaultPayload.message.order.provider = sessionData.provider[0]; // can be anything, e.g. only L2
}
```
`defaultPayload`'s template fulfillment hardcodes `start.location.id: L1` with the Jayanagar warehouse address/gps (flow YAML, `on_confirm` step, `message.order.fulfillments[0].start`). Nothing downstream overrides it, so if the resolved provider's only declared location is e.g. `L2`, the payload ships from a location the provider doesn't declare.

**Where the richer start location would come from, and why it isn't available:** `select_generate.js` resolves a `catalogProvider.locations` array with full `{id, gps, address}` objects from the pasted `live_catalog` (or the `RETeB2BCatalog` fallback), but immediately discards everything except the bare id before saving:
```js
const catalogLocationIds = (catalogProvider.locations || []).map((l) => l.id).filter(Boolean);
if (locationIds.length > 0) provider.locations = locationIds.map((id) => ({ id }));
```
`saveData.provider: $.message.order.provider` then persists only that bare-`{id}` shape. **No step in this flow saves a richer location object anywhere sessionData can reach it from `on_confirm`.** So per the prompt's fallback guidance, the fix syncs only `start.location.id`; the template's placeholder `gps`/`address`/`contact` for the start location are left as-is. This is a residual gap (see below), not something fixable without touching `select_generate.js`, which is out of scope for a narrowly-scoped `on_confirm` diff.

## The fix

In `on_confirm_generate.js`'s fulfillment-rebuild block, resolve `start.location.id` from the fulfillment's own items (which carry the catalog-resolved `location_id`), falling back to the provider's first declared location, falling back to the original template value:

```js
const providerLocationIds = Array.isArray(sessionData?.provider?.[0]?.locations)
  ? sessionData.provider[0].locations.map((l) => l.id).filter(Boolean)
  : [];

order.fulfillments = savedFulfillments.map((f) => {
  const base = templateFulfillments.find((t) => t.id === f.id) || templateFulfillments[0];

  const matchingItem = savedItems.find(
    (item) => (item.fulfillment_id || defaultFulfillmentId) === f.id
  );
  const resolvedLocationId =
    matchingItem?.location_id ||
    matchingItem?.location ||
    providerLocationIds[0] ||
    base?.start?.location?.id;

  const start = base?.start
    ? { ...base.start, location: { ...base.start.location, ...(resolvedLocationId ? { id: resolvedLocationId } : {}) } }
    : base?.start;

  return { ...base, id: f.id, type: f.type, ...TAT, ...customer, ...(start ? { start } : {}), end: f.end };
});
```

`matchingItem` and `order.items` (built two blocks later) both read from the same `savedItems` array, so `start.location.id` and `order.items[].location_id` are always derived from the same source and stay internally consistent — this matters because `orderFormationChecks.ts` has an extensive comment (see "Important context from report-service" below) warning that a real defect in a *different* flow (`Out_of_Stock_Error_code_`) showed `items[].location_id` flipping independently of `provider.locations` only at `on_confirm`. This fix cannot reproduce that failure mode because both fields come from one read of `savedItems`.

H1 (payments echo) and H2 (fulfillment customer/end echo), fixed in `2c9824bc`, are untouched — confirmed by decoding the restored YAML and checking both markers are still present, and by `git diff` showing only this one line changed.

## Verification

### 1. Reproduced the live failure, then the fix (direct generate() invocation)

Built `sessionData` matching what `select`→`confirm` would save for a provider whose only declared location is `L2` (not `L1`), and called the real `on_confirm_generate.js` via Node's `vm` module (stubbing only `applyDynamicTimestamps`, which is irrelevant to this bug and only re-stamps timestamps):

| | `provider.locations[].id` | `fulfillment.start.location.id` | Result |
|---|---|---|---|
| **Before fix** | `["L2"]` | `"L1"` | **Contract violation reproduced** — matches the live-run symptom exactly |
| **After fix** | `["L2"]` | `"L2"` | Passes |

Also re-ran the happy-path case (provider's only location is `L1`, matching the template) to confirm no regression: `start.location.id` stays `"L1"`.

### 2. Real report-service validator

Ran `validateShipFromLocation` (`automation-report-service/src/validations/ONDC:RETeB2B/1.2.5/orderFormationChecks.ts:1406`) directly against before/after `order` objects:

```
--- on_confirm (BEFORE fix) ---
failed: ["on_confirm (BEFORE fix): fulfillment F1 ships from location 'L1', which is not one of the provider's declared locations (L2)"]

--- on_confirm (AFTER fix) ---
passed: ["on_confirm (AFTER fix): ship-from location id/gps valid on all declared fulfillment starts"]
failed: []
```
This is the exact rule and message text the live run reported.

**Scope note:** I verified the specific validator rule directly rather than the full in-memory, Redis-stubbed `validationModule`/`checkPayload` end-to-end replay across all 18 steps that `BIR_MOCK_FIX_REPORT.md`'s session used (`report_check.js`). That harness lived in that session's scratchpad and no longer exists; reconstructing it (session-level Redis stubbing, dynamic validator-module loading via `loadConfig`, full flow replay) was out of proportion to confirming this one check. If an exact before/after pass/fail *count* across the whole flow is needed, that harness would need to be rebuilt.

### 3. Round-trip / diff scope

- `extract-flow.ts` → edit → `restore-flow.ts` round trip: `git diff` on the flow YAML shows exactly 1 line changed (the `on_confirm` step's `mock.generate` base64), confirming nothing else in the 1,000+ line file drifted.
- Decoded the restored YAML's `on_confirm` generator: contains `sessionData.payments[0]` (H1) and `f.customer`/fulfillment echo (H2) — both intact — plus the new `providerLocationIds` logic.

### 4. Deployment/sync gap (confirmed independently)

Ran the prompt's suggested check against `automation-config-service`'s mirrored copy:
```
MISSING the H1 fix
MISSING the new location fix
```
Confirms: (a) `2c9824bc` (H1–H5) is a local commit in this repo, ahead of `origin/draft-RETeB2B`, not pushed, and not mirrored into `automation-config-service`; (b) this session's new fix is local-only too. **Dev-workbench's mock-playground loads from `automation-config-service`, not this repo**, so none of H1–H5 or this fix will show up in a live dev-workbench run until (1) this repo's commits reach `origin/draft-RETeB2B`, and (2) the same changes are mirrored into `automation-config-service`'s copy of this flow. This is a deployment gap, not something fixable by editing this repo further.

### 5. Cross-flow check (confirmed, not fixed — out of scope here)

Read (did not edit) `Order_to_confirm_to_fulfillment__cod_.yaml`'s `on_confirm` generator. It has the **identical bug pattern**: it echoes only `fulfillments[0].customer` from the buyer's saved fulfillment, never touches `start`, and separately does `order.provider = sessionData.provider[0]`. So the template's static `start.location.id` placeholder can equally mismatch a resolved provider whose locations don't include it. This matches what `COD_FULFILLMENT_LOCATION_FIX_PROMPT.md` already describes for the other session fixing that file — confirmed, left untouched per the ground rules.

## Important context found in report-service (not a defect here, but load-bearing for anyone touching this check later)

`orderFormationChecks.ts` carries a long comment directly above `validateShipFromLocation` documenting an earlier investigation (2026-10-13) that tried to re-anchor the ship-from check on the seller's **catalog** locations instead of the payload's own `provider.locations`, to explain away what looked like a false positive in `Out_of_Stock_Error_code_`. That turned out to be wrong: in that flow, `items[].location_id` itself flips to a different value only at `on_confirm` and reverts afterward — a genuine mock defect, not a validator bug. The check intentionally stays anchored on the current payload's own `order.provider.locations`, which is exactly what this fix's `providerLocationIds` reads (`sessionData.provider[0].locations`, which becomes `order.provider` in the same `on_confirm` payload). Worth knowing if `Order_to_confirm_to_fulfillment__cod_`'s fix (or any future ONDC:RETeB2B on_confirm fix) is tempted to anchor on the catalog instead — don't; anchor on the payload's own provider, as the comment explains.

## Residual gaps (not fixed, flagged per the prompt)

1. **`start.location`'s address/gps/contact stay the template's placeholder** (`ABC Distributors Warehouse`, Jayanagar, `12.9563,77.6368`) even after the id fix, because no step in this flow saves a richer location object than `{id}`. Only the `id` was syncable from available session data.
2. **`order.items[].location_id` has the same class of hardcoded fallback** (`item.location_id || item.location || "L1"`, `on_confirm_generate.js`, "Restore items" block) — if an item ever lacks both fields, it would default to `"L1"` the same way `start.location.id` used to. In practice `select_generate.js` always populates `location_id` on saved items, so this is dormant, not reachable in the flows observed — reported, not fixed, to keep this session's diff scoped to the one hypothesis.
3. Confirmed via direct `node -e` reads (no edits) that `automation-config-service`'s mirrored copy of this flow lacks both H1–H5 and this new fix — see §4.

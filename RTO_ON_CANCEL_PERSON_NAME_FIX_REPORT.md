# Fix missing F1.end.person.name on on_cancel_rto: Merchant_Side_RTO_and_Part_Order_Cancellation_Flow (RETeB2B 1.2.5)

- **Date:** 2026-10-16
- **Branch:** `draft-RETeB2B`. This session committed nothing.
- **File changed:** `config/flows/eB2B/Merchant_Side_RTO_and_Part_Order_Cancellation_Flow.yaml` only — the `on_cancel_rto` step's `mock.generate` field. `git diff` = exactly 1 line (the base64 blob).
- **Contract:** `/tmp/ebb2b_doc.txt`.
- **Method:** extracted fresh with `extract-flow.ts`, edited the `on_cancel_rto_generate.js` sidecar, restored with `restore-flow.ts`. Reproduced the defect and the fix by invoking the real sidecar `generate()` directly (Node `vm`) with `sessionData` shaped the way the prior leg (`on_confirm`, carried through) actually leaves `F1`.

## Verdict: Confirmed

### The rule and the error
`config/validations/index.yaml:4719`, inside the `on_cancel:` block:
```yaml
- _NAME_: FULFILLMENTS_END_PERSON_NAME
  _SCOPE_: "$.message.order.fulfillments[*]"
  fulfillment_type: "$.type"
  var_ff_types: ["Delivery", "Return"]
  _CONTINUE_: "!(fulfillment_type any in var_ff_types)"
  attr: "$.end.person.name"
  _RETURN_: attr are present
```
Confirmed scoped to Delivery/Return fulfillments, unconditionally requires `end.person.name`, matching the live NACK text exactly.

### Contract support for the rule: confirmed (unlike the previous `/on_update` L1 task, this rule IS backed by the contract)
Read both `/on_cancel` contract examples directly:
- `/tmp/ebb2b_doc.txt:19641-19647` — F1 (Delivery)'s `end.person.name: "name_of_person"`, directly adjacent to `end.location`/`end.contact`, inside the same fulfillment object that carries the `cancel_request` tag.
- `/tmp/ebb2b_doc.txt:20476-20480` — the RTO-flow-specific `/on_cancel` example, identical shape.

Both confirm the hypothesis: this is a real contract requirement this flow's mock was missing, not an over-strict rule to relax.

### The gap: confirmed
- `on_cancel_rto_generate.js` (before): `const f1 = savedFulfillments.find((f) => f.id === "F1");` then only mutates `f1.state` and `f1.tags` — never touches `f1.end`.
- Traced `F1.end` back to its origin: `on_confirm`'s `defaultPayload` template for F1 has `end: { location: {...}, contact: {...} }` — no `person` key at all. Since no leg between `on_confirm` and `on_cancel_rto` ever adds one, it stays absent straight through.
- **Sibling flow already handles this correctly:** `Buyer_Side_Order_Cancellation.yaml`'s `on_cancel` → `createCancelFulfillments()` sets `end.person.name` with a three-level fallback (existing name → `sessionData.billing[0].name` → literal `"Buyer"`), confirmed by reading it directly — byte-for-byte matching the prompt's quote.

## The fix

In `on_cancel_rto_generate.js`, immediately before the existing `f1.state =` / `f1.tags =` mutations:
```js
// F1 (Delivery) never gets end.person set by any earlier leg in this flow, but the
// contract's own /on_cancel examples carry it on the same fulfillment — keep an
// existing name if there is one, else fall back to the buyer's billing name, else
// a final literal (matching Buyer_Side_Order_Cancellation's on_cancel).
f1.end = {
  ...f1.end,
  person: {
    name: f1.end?.person?.name || sessionData?.billing?.[0]?.name || "Buyer",
  },
};
```
`start`, `contact`, and `location` are untouched (`...f1.end` preserves them); only the missing `person` key is added. `sessionData.billing` was already loaded elsewhere in this same generator (`existingPayload.message.order.billing = sessionData.billing[0];`), so no new session-data wiring was needed.

## Verification

### 1. Reproduced, then fixed (direct `generate()` invocation)

Built `sessionData.fulfillments[0]` (F1) exactly as it arrives at `on_cancel_rto` — `end.location` + `end.contact`, no `end.person` — matching what `on_confirm`'s own template actually contains:

| | `F1.end` | Result |
|---|---|---|
| **Before fix** | `{location, contact}` — no `person` | **Contract violation reproduced** — matches the live NACK exactly |
| **After fix** | `{location, contact, person: {name: "Sharma Kirana Store"}}` | `end.person.name` present and non-empty; `location`/`contact` byte-identical to before |

### 2. Fallback chain edge cases

- **No billing name available:** `sessionData.billing = [{}]` → `F1.end.person` = `{"name": "Buyer"}` (final literal fallback fires correctly).
- **F1 already has an `end.person.name`:** pre-set to `"Original Name"`, billing says `"Someone Else"` → output stays `{"name": "Original Name"}` (existing name is preserved, not clobbered by billing).

### 3. Downstream / report-service impact

- **No `automation-report-service` TypeScript validator checks `end.person.name` or `FULFILLMENTS_END_PERSON_NAME`** — grepped the whole `ONDC:RETeB2B/1.2.5` validator directory; no hits. This rule lives only in the `config/validations/index.yaml` L1 rule-engine layer (the same layer, and the same "no local compiler/interpreter exists in this workspace" situation, as the `L1_ON_UPDATE_TIME_RULE_REPORT.md` task earlier this session).
- **Report-service's own `on_cancel` checks are unaffected.** Read `OnCancel.ts`'s imports: `validateOrderState`, `compareOrderIdContinuity`, `validateOnSelectFulfillmentRefs`, `validateAdjustmentArithmetic`, `validatePaymentParamsEcho`, `validateCreatedAtNotBeforeOrder` — none reference `end.person`, `end.contact`, or anything this fix touches. Adding the `person` key doesn't change `state`, `tags`, order id, payments, or `created_at`, so none of these are affected.
- **The `_END_PERSON_NAME`-adjacent `FULFILLMENTS_END_CONTACT_*` checks** (same `on_cancel:` block, same Delivery/Return scope) are unaffected: this fix never touches `end.contact`, confirmed by the before/after diff above (`contact` is byte-identical).

### 4. Diff scope

`git diff` on the flow YAML shows exactly 1 line changed (the `on_cancel_rto` step's `mock.generate` base64) — confirmed by decoding the restored file and checking both the new fix string and that nothing else in the function changed.

## Cross-flow / cross-repo findings (confirmed, not fixed — out of scope here)

1. **`Order_to_confirm_to_fulfillment__cod_.yaml` has no `on_cancel` or `on_update_return_*` leg at all** (confirmed by listing all its `action_id`s: `select` through `on_status_order_delivered`, no cancel/return leg) — this gap pattern isn't applicable to it.
2. **`Buyer_Initiated_Return__Full_Order_and_Partial_Order_.yaml` has the same underlying data gap**, though it isn't currently causing a live NACK the way RTO's did:
   - Its `on_confirm` template also has no `end.person` on F1 (confirmed — identical structure to RTO's).
   - None of `on_update_return_init`, `on_update_return_approved`, or `on_update_return_picked` ever set it (grepped all three; no `end.person` or `person:` hits).
   - **However**, `config/validations/index.yaml`'s `on_update:` block has **no `FULFILLMENTS_END_PERSON_NAME` rule at all** (confirmed by scoping the grep to that block specifically) — unlike `on_cancel:`, which has the mandatory version, and `confirm:`, which already has an *optional* version (`_CONTINUE_: "!(attr are present)"`, line 3219). So this data gap exists in BIR's payloads but isn't currently enforced by any live L1 rule on that leg. Flagging it since the contract itself still carries `end.person` in its lifecycle examples generally — a future rule addition there would hit the same gap this fix just closed for RTO.
3. **`automation-config-service`'s mirror of the RTO flow has the identical, unfixed gap** — confirmed by direct read (`src/config/RETeB2B/v-1.2.5/EB2B/flows/Merchant_Side_RTO_and_Part_Order_Cancellation_Flow.yaml`'s `on_cancel_rto` generator lacks the fix), no edits made, per the ground rules.

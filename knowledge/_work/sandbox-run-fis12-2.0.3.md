# Sandbox runtime observation — FIS12-2.0.3 Personal_Loan_Dedupe_Check

**SANDBOX, not production.** Local workbench stack (docker), user-authorized 2026-08-22.
Facts below may be seeded `basis:sandbox-tested` with these obs refs. They must NEVER be
recorded `observed-live`: no real network participant was involved.

## Run identity (the obs ref)
- stack: local docker compose, api-service container `api-ondcfis12-2-0-3`
- BAP session `utcCrjQkn4HjcAKiKm3q3UA5QMia57_c` · BPP session `w9UYC_J9TIwYyeZ-ux9jIWUK1FVsTAai`
- flow `Personal_Loan_Dedupe_Check` · domain ONDC:FIS12 · version 2.0.3 · usecase PERSONAL LOAN
- transaction_id `987c75e7-15b5-45f6-b6f4-d8a3e172f214`
- reached 5/7 steps (71%): search, on_search, select, on_select, on_status. 0 NACKs on this txn.

## Topology (observed, both roles)
BAP sends -> /api-service/ONDC:FIS12/2.0.3/**seller**/<action>
BPP sends -> /api-service/ONDC:FIS12/2.0.3/**buyer**/<action>
both receive at -> /mock/ONDC:FIS12/2.0.3/<action>
gateway routes (nginx): /mock/<domain>/<ver>/* -> playground-mock-service;
                        /api-service/<domain>/<ver>/* -> api-<domain>-<ver>:7039

## Runtime behaviour observed (candidate sandbox-tested facts)
1. EXPECTATION GATE. The api-service accepts a call only against a pre-registered
   expectation keyed (SessionId, FlowId, transaction_id, subscriber URL, role).
   Log: `expectation fulfilled: cache.Expectation{SessionId:..., FlowId:"Personal_Loan_Dedupe_Check"}`
   No match -> NACK `412 No active expectation found for transaction ID: ... for as a seller_np`.
2. EXPECTATIONS EXPIRE. Observed TTL ~4.5 min from flow start
   (`expectation expired at 11:34:50, now 11:39:18`). A late call NACKs 412 even if well-formed.
   -> starting a flow and sending must happen inside that window.
3. PER-ACTION PIPELINE (fixed order, observed for every action):
   fulfil expectation -> "Validating Transaction History" -> "Running TTL Validations"
   -> "Running Transaction Id Checks" -> "Stored data for action X successfully" -> forward.
4. TTL VALIDATION IS CALLBACK-ONLY. `Skipping TTL validation for non-on_ action: search`
   -> TTL validation applies to `on_*` callbacks only, not to requests.
5. MOCK AUTO-DRIVE. Starting a flow fires the MOCK-side steps automatically
   (`mockTxnCaller ... Forwarding request to .../mock/.../on_search`); only steps the UI marks
   `YOU SEND` require a real outbound call from the NP under test.
6. ROLE MIRRORING. The same flow in a BPP session inverts every step's send/mock marking
   (BAP `search: YOU SEND` <-> BPP `search: MOCK`).

## Corroboration of an x-validation atom (config -> KB -> live enforcement)
`REGEX_CONTEXT_BAP_ID` fires in the running validator with the same regex the KB atom carries:
  live NACK: `$.context.bap_id must follow ^(?!.*\b(?:http|https|www)\b)[a-zA-Z0-9-]+(\.[a-zA-Z0-9-]+)+$`
This is what exposed the atomizer's pipe-sanitisation bug (alternation corrupted). Fixed via %7C.

## Config defects surfaced by running it
- The `search` step's own `defaultPayload.context.timestamp` is `2023-05-25 05:23:03.443000+00:00`
  — a SPACE separator, not RFC3339 `T`. Had to be rewritten to send successfully.
- UI progress does not live-update; it required a page reload to move 0% -> 29% -> 71%.

## Non-form flow inventory (FIS12-2.0.3, from the running UI)
Only `Personal Loan Dedupe Check` (7 steps) is form-free. All 5 others carry FORM steps
(personal_loan_information_form / Ekyc_details_form / payment_url_form):
Offline(17), Single Redirection(19), Foreclosure Offline(21), Missed EMI Offline(21),
Pre Part Payment Offline(21).

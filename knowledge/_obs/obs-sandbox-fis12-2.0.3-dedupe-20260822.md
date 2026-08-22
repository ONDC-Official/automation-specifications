# Observation record — obs-sandbox:fis12-2.0.3-dedupe-20260822

**Kind:** SANDBOX execution. **Not production.** No real network participant was involved.
Atoms citing this ref may carry `basis:sandbox-tested` and MUST NOT carry `observed-live`.

| | |
|---|---|
| authorized by | user (shreyansh), 2026-08-22, "you may start using the runtime for non form transaction" |
| stack | local docker compose (workbench), api-service container `api-ondcfis12-2-0-3` |
| domain / version | ONDC:FIS12 / 2.0.3 · usecase PERSONAL LOAN |
| flow | `Personal_Loan_Dedupe_Check` (the only form-free flow in this book) |
| BAP session | `utcCrjQkn4HjcAKiKm3q3UA5QMia57_c` |
| BPP session | `w9UYC_J9TIwYyeZ-ux9jIWUK1FVsTAai` |
| transaction_id | `987c75e7-15b5-45f6-b6f4-d8a3e172f214` |
| outcome | 5/7 steps (71%): search, on_search, select, on_select, on_status. 0 NACKs on this txn. |
| driver | direct HTTP POST to `/api-service/ONDC:FIS12/2.0.3/seller/<action>` (the endpoint the session's Guide names) |

## What was observed (evidence lines from the api-service container log)

1. **Expectation gate** — a call is accepted only against a pre-registered expectation:
   `expectation fulfilled: cache.Expectation{SessionId:"utcCrjQkn...", FlowId:"Personal_Loan_Dedupe_Check"}`
   No match → `Sending Nack: code 412, No active expectation found for transaction ID: ... for as a seller_np`
2. **Expectations expire** — `expectation expired at 2026-08-22 11:34:50 +0000 UTC, now 11:39:18`
   (~4.5 min after flow start). A well-formed call outside the window still NACKs 412.
3. **Fixed per-action pipeline** — for every action, in order:
   fulfil expectation → `Validating Transaction History for action: X` →
   `Running TTL Validations for action: X` → `Running Transaction Id Checks` →
   `Stored data for action X successfully` → `Forwarding request to URL: .../mock/.../X`
4. **TTL validation is callback-only** — `Skipping TTL validation for non-on_ action: search`
5. **Mock auto-drive** — starting a flow fires the MOCK-side steps without any outbound call
   from the NP under test; only steps the UI marks `YOU SEND` require one.
6. **Role mirroring** — the identical flow opened in a BPP session inverts every step's
   send/mock marking (BAP `search: YOU SEND` ↔ BPP `search: MOCK`).

## Corroboration of a config-grounded atom
The running validator emits `REGEX_CONTEXT_BAP_ID` with the same regex the KB atom carries
(`^(?!.*\b(?:http|https|www)\b)[a-zA-Z0-9-]+(\.[a-zA-Z0-9-]+)+$`), closing
config `_TESTS_` → KB atom → live sandbox enforcement. This comparison is what exposed the
atomizer's pipe-sanitisation bug (alternation corrupted); fixed via `%7C`.

## Defects surfaced by running it
- `Personal_Loan_Dedupe_Check` step 0 `mock.defaultPayload.context.timestamp` is
  `2023-05-25 05:23:03.443000+00:00` — a SPACE separator, not RFC3339 `T`.
- Workbench UI flow progress does not live-update; a page reload was required to observe
  0% → 29% → 71%.

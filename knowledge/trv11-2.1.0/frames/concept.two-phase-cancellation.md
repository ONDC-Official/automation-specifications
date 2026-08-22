---
id: concept.two-phase-cancellation
kind: concept
layer: domain
status: draft
asof: trv11-2.1.0
---

# concept.two-phase-cancellation

Declared node for `concept.two-phase-cancellation` — TRV11 cancels in two `cancel` calls
distinguished by a descriptor code (a soft leg that prices the cancellation, then a confirming
leg), rather than in one. It is the shape shared by the book's cancellation flows across both
use cases.

Interned meaning: `anchor.cancel-descriptor-code` — the code set `anchor.cancel` is
constrained by. The two legs are rendered as `step.cancel-soft` / `step.cancel-hard` and their
callbacks `step.on-cancel-soft` / `step.on-cancel-hard` / `step.on-cancel-initiated`.

Grounded at: `trv11-2.1.0:validations/index.yaml#_TESTS_.cancel[REQUIRED_MESSAGE_CODE_16].enumList`
Order-status side: `trv11-2.1.0:attributes/Bus.yaml#attribute_set.on_status.message.order.status._description.enums`

Added to close a concept coverage gap; body intentionally light — the facts live in
`atoms.md`, not in prose.

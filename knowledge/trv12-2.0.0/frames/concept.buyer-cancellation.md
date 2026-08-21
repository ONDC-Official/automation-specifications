---
id: concept.buyer-cancellation
kind: concept
layer: domain
status: draft
asof: trv12-2.0.0
---

# concept.buyer-cancellation

Declared node for `concept.buyer-cancellation` — cancellation initiated by the buyer through `cancel`, carrying a cancellation reason and moving the order through the soft/confirm phases.

Grounded at: `trv12-2.0.0:flows/Airline/Cancellation_by_Buyer.yaml#steps[cancel_Airline_201].mock.defaultPayload.message.descriptor.code`

Facts live in `atoms.md` under the handle `anchor.buyer-cancellation`; body intentionally light — no prose
assertions beyond this declaration.

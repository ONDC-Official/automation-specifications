---
id: concept.unwired-response-for
kind: concept
layer: domain
status: draft
asof: trv11-2.1.0
---

# concept.unwired-response-for

Declared node for `concept.unwired-response-for` — a flow step's `responseFor` normally names
the step it answers, and that is what a `precedes` atom is built from. Two steps in this book
carry a `responseFor` that cannot yield an edge, so **no `precedes` atom is asserted for
either**. Recorded here so the absence reads as a decision, not an oversight.

1. **Dangling target.** `on_update_1` answers a step id that the flow does not contain; the
   flow's step list ends at `on_confirm_1` and the step is also marked `unsolicited: true`.
   Grounded at: `trv11-2.1.0:flows/Bus/Intracity_Seller_Based_Confirmation_flow.yaml#steps[on_update_1].responseFor`

2. **Mutual reference.** `cancel_hard_METRO_210` and `on_cancel_init_METRO_210` name each
   other, which would make each precede the other.
   Grounded at: `trv11-2.1.0:flows/Metro/DELAYED_CANCELLATION_FLOW_REJECTED.yaml#steps[cancel_hard_METRO_210].responseFor`
   and `trv11-2.1.0:flows/Metro/DELAYED_CANCELLATION_FLOW_REJECTED.yaml#steps[on_cancel_init_METRO_210].responseFor`

Both need a config fix or an explicit ruling before the edges can be added.

Added to close a concept coverage gap; body intentionally light — the facts live in
`atoms.md`, not in prose.

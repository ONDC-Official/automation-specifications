---
id: concept.fulfillment-type
kind: concept
layer: domain
status: draft
asof: trv11-2.1.0
---

# concept.fulfillment-type

Declared node for `concept.fulfillment-type` — the code that says *what kind of thing* a
TRV11 fulfillment is (ROUTE, TRIP, PASS, TICKET, STOPS, AGENT_TICKETING, ONLINE). It is the
book's main discriminator: seven of the seventeen actions carry a validation on it.

Interned meanings: `anchor.fulfillment-type` (the required-enum set) and
`anchor.fulfillment-type-catalog` (the narrower valid-values set used on the catalog leg);
`anchor.pass`, `anchor.ticket` and `anchor.agent-ticketing` are members.

Grounded at: `trv11-2.1.0:validations/index.yaml#_TESTS_.on_search[REQUIRED_MESSAGE_TYPE_18].enumList`
Catalog-leg variant: `trv11-2.1.0:validations/index.yaml#_TESTS_.on_search[VALID_FULFILLMENT_TYPE_VALUES].validValues`

**Ambiguity, not resolved here.** `PASS` and `TICKET` are two of this book's duplicate YAML
`&anchor` names — see `concept.duplicate-yaml-anchor`. The KB keeps each reading apart with
`scoped-to` rather than interning one definition.

Added to close a concept coverage gap; body intentionally light — the facts live in
`atoms.md`, not in prose.

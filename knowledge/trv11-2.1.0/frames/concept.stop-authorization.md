---
id: concept.stop-authorization
kind: concept
layer: domain
status: draft
asof: trv11-2.1.0
---

# concept.stop-authorization

Declared node for `concept.stop-authorization` — how a rider proves entitlement at a stop:
an authorization *type* carried on the START stop, plus (Metro only) a claim *status* on the
same object.

Interned meanings: `anchor.stop-auth-type` (the type code, scoped by an atom to the START
stop) and `anchor.auth-status` (the claim state).

Grounded at: `trv11-2.1.0:validations/index.yaml#_TESTS_.on_confirm[REQUIRED_MESSAGE_TYPE_31].enumList`
Attribute dictionary, type (Bus): `trv11-2.1.0:attributes/Bus.yaml#attribute_set.on_confirm.message.order.fulfillments.stops.authorization.type._description.enums`
Attribute dictionary, type (Metro): `trv11-2.1.0:attributes/Metro.yaml#attribute_set.on_confirm.message.order.fulfillments.stops.authorization.type._description.enums`
Attribute dictionary, status (Metro): `trv11-2.1.0:attributes/Metro.yaml#attribute_set.on_confirm.message.order.fulfillments.stops.authorization.status._description.enums`

Two asymmetries the KB records rather than smooths over: the `on_confirm` validation admits
fewer type codes than the attribute dictionary documents, and `authorization.status` is
declared under Metro's attribute set but not under Bus's.

Added to close a concept coverage gap; body intentionally light — the facts live in
`atoms.md`, not in prose.

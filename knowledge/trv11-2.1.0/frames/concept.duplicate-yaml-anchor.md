---
id: concept.duplicate-yaml-anchor
kind: concept
layer: domain
status: draft
asof: trv11-2.1.0
---

# concept.duplicate-yaml-anchor

Declared node for `concept.duplicate-yaml-anchor` — seven `&NAME` YAML anchors are declared
more than once in this book, each time under a different parent, so no single declaration owns
the meaning. Interning any one of them would be a guess. This frame records the ambiguity; it
does not resolve it.

The seven: `ADDITIONAL_APIS`, `BPP_TERMS`, `COMMON_FULFILLMENT_ITEMS`, `PASS`,
`REQUIRED_ITEM_FULFILLMENT_IDS`, `REQUIRED_ORDER_ID`, `TICKET`.

All seven declarations sit inside the commented-out `enums:` / `tags:` preamble and the
commented validation blocks of `validations/index.yaml`, so **there is no parsed config node
to ground them at** — a `grounded-in` path for the declaration itself would have to be
invented, and is therefore not given.

How the KB currently copes, per name:

- `PASS`, `TICKET`, `BPP_TERMS`, `ADDITIONAL_APIS` — interned at a *live* position elsewhere
  (a `_TESTS_` enum or an attribute `_description`), with each further reading held apart by
  `scoped-to` atoms instead of a second definition.
- `COMMON_FULFILLMENT_ITEMS`, `REQUIRED_ITEM_FULFILLMENT_IDS`, `REQUIRED_ORDER_ID` — carried
  as `!untethered` units, with `grounded-in: -` in `anchors/index.md`.

Worth a human decision: the two `REQUIRED_ORDER_ID` declarations bind different attributes
(one an order-level id, one a payment-level id), so they are not a harmless copy-paste.

Added to close a concept coverage gap; body intentionally light — the facts live in
`atoms.md`, not in prose.

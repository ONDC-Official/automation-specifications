---
id: anchor.on-action-items
kind: concept
layer: protocol
status: draft
asof: fis12-2.3.0
---

# anchor.on-action-items

Declared node for `anchor.on-action-items` — the item-shape test applied to `on_*` callbacks.

Grounded at: `fis12-2.3.0:validations/index.yaml#_TESTS_.on_init[ON_INIT_ITEMS]`

This handle sits on a **redefined** YAML anchor in `validations/index.yaml`: the same
`&NAME` is declared more than once and later declarations shadow earlier ones under
js-yaml semantics. No single definition is interned here — the ambiguity is recorded,
not resolved. See `anchor.redefined-validation-anchor`.

Seeded from this book's own atoms; body intentionally light — the facts live in
`atoms.md`, not in prose.

---
id: anchor.required-xinput-fields
kind: concept
layer: protocol
status: draft
asof: fis12-2.3.0
---

# anchor.required-xinput-fields

Declared node for `anchor.required-xinput-fields` — the xinput fields a callback's items must carry.

Grounded at: `fis12-2.3.0:validations/index.yaml#_TESTS_.on_select[ON_SELECT_ITEMS]._RETURN_[REQUIRED_ITEMS]._RETURN_[REQUIRED_XINPUT_FIELDS]`

This handle sits on a **redefined** YAML anchor in `validations/index.yaml`: the same
`&NAME` is declared more than once and later declarations shadow earlier ones under
js-yaml semantics. No single definition is interned here — the ambiguity is recorded,
not resolved. See `anchor.redefined-validation-anchor`.

Seeded from this book's own atoms; body intentionally light — the facts live in
`atoms.md`, not in prose.

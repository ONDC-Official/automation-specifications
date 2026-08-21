# The atom line — how to read it

```
anchor.search | requires | anchor.xinput | basis:declared | asof:fis12-2.3.0 | grounded-in:fis12-2.3.0:validations/index.yaml#_TESTS_.search[SEARCH_ITEMS]._RETURN_[REQUIRED_XINPUT_FIELDS]
└── subject ──┘ └ relation ┘ └── object ──┘ └── how backed ┘ └── which book ┘ └────────── exact config node it came from ──────────┘
```

Mandatory: `subject | relation | object`. Then, in fixed order for greppability:
`basis:` · `asof:` · `grounded-in:` · `!flags`. Fields after the triple may be absent —
a bare triple is a valid, immature atom.

- **subject/object** are either an `anchor.<kebab>` handle (an *interned meaning* — look it
  up in `anchors/index.md` or with `about`) or a `"quoted literal"`. Error codes appear as
  literals: `"80231" | isa | anchor.error-code`.
- **grounded-in** is `<book>:<file>#<node-path>` for `basis:declared`. The node path is
  positional (`steps[on_select_2].description`, `enums.loanCategories[AA_GST]`), never a line
  number — position carries meaning in these configs, which is why `scoped-to` exists.
- Some `grounded-in` values point outside the config book: `workbench:frames/*.md` and
  `workbench:decisions/adr-*.md` (runtime/authority docs), or a bare handle (`basis:derived`).

## Relations actually used, by frequency

| family | relations |
|---|---|
| structural | `isa` (taxonomy DAG) · `part-of` · `has-slot` · `scoped-to` (meaning confined to a position/provider/action) · `disjoint-with` · `sent-by` (BAP \| BPP) |
| semantic | `requires` · `precedes` · `constrains` · `causes` |
| provenance (PROV-O, camelCase on purpose) | `wasDerivedFrom` · `wasRevisionOf` · `wasInformedBy` · `wasAttributedTo` · `wasGeneratedBy` · `used` |

Any relation may be prefixed **`not-`**. `not-requires`, `not-isa`, `not-has-slot` etc. are
explicit negative facts — the closed-world infrastructure. They assert *the spec establishes
this does not hold*, which is different from the fact simply being absent.

The registry is flat and openly extensible, but every relation is a declared term with a
definition — if you see something outside the list above, treat it as intentional, not noise.

## basis

`declared` (config says so) · `authority` (doc/ADR/regulation — the why) · `sandbox-tested` ·
`observed-live` · `ecosystem` (convention) · `derived` (from other atoms) · `inferred`
(model guess — has **no** `grounded-in`, and is **never** asserted as fact).

Actual distribution across all 16 books: declared 10167, authority 442, derived 89,
inferred 50, observed-live 19, sandbox-tested 13, ecosystem 1.

## Flags — the only hand-written status

`!untethered` (no resolvable ground; parked) · `!deprecated` (ground removed/superseded) ·
`!desired` (intended, not yet real — never present as current behaviour) · `!plane=<p>`.

## Derived at load, never stored

- **maturity** — from how many fields are present: bare → partially-grounded → mature.
- **plane** — `precedes`/`wasInformedBy` → session-logic; `authority`/`ecosystem` → cross;
  `sandbox-tested`/`observed-live` → runtime-state; else spec. Overridden by `!plane=`.
- **scope** — live, unless `!desired`.
- **grounding-status** — grounded when `grounded-in` resolves; otherwise the atom must carry
  `!untethered` or `!deprecated`. Silent dangling is invalid.

Two invariants worth knowing when reading: a meaning that recurs in ≥2 positions is
**interned** as an `anchor.*` handle and referenced, never restated inline; and
`basis:inferred ⇔ no grounded-in`.

Full spec: `skill/kb-format/` (`atom.grammar.md`, `vocabularies.md`, `unit.md`, `anchor.md`,
`invariants.md`) and the bundled validator `skill/tools/validate_kb.py`.

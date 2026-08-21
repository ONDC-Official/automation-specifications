# Anchor — interned schematic meaning

An **anchor** is a committed node for a schematic meaning that recurs across the config — the KB analogue
of a YAML `&anchor`. It is **interned once** (canonical definition + its config ground) and referenced
**by handle** everywhere else. This is what keeps units light: a unit that touches a shared meaning
carries the anchor's **handle**, never a restated copy of its content. The meaning lives in exactly one
place, well recorded, with minimal diff.

Anchors mirror the config's own mechanism. `validations/index.yaml` defines `&loanCategories`,
`&LAMF`, `&fulfillmentTypes` once and `*aliases` them into attributes and flows; the KB records each such
shared definition as one anchor and points at it.

## Why interning (the problem it solves)

Without anchors, the same enum / tag-group / schema fragment gets copied into every unit that mentions it.
That bloats atoms, multiplies the diff surface (one config change → edits in many places), and lets the
same meaning drift into near-duplicates. An anchor collapses all of that to **one node + N handle
references**: change the meaning once, every reference follows; retrieval resolves a handle instead of
walking a subtree from the root.

## File & registry

Anchors are **light**. An anchor does **not** require its own frame — its record is a row in the
committed registry, and any facts *about* it are ordinary units using its handle.

```text
anchors/
├── index.md          # COMMITTED registry: handle → canonical meaning → config ground (the lookup surface)
└── {shard}.md        # optional shards when index.md grows (mirror config's per-area split)
```

Registry row (one line, greppable):

```text
| handle | canonical meaning (one line) | grounded-in | asof |
| anchor.loan-categories | enum of loan-category codes shared across attributes + flows | fis12-2.3.0:validations/index.yaml#loanCategories | fis12-2.3.0 |
| anchor.pan | applicant PAN string, pattern ^[A-Z]{5}[0-9]{4}[A-Z]$ | fis12-2.3.0:flows/LAMF/lamf_credit_line_with_mfc#steps[search_1].inputs.jsonSchema.properties.pan | fis12-2.3.0 |
```

The registry is **committed** because the canonical meanings are authored source-of-truth. What is
**derived** (never committed) is the *occurrence map* — which units and config positions reference each
anchor — recomputed at load like any reverse index ([derived](../derived/README.md)).

## Handle convention

`anchor.<kebab>` — dotted handle, resolves like any node handle ([unit.md](unit.md)). Units place it in
subject or object position:

```text
# a unit references the shared meaning by handle — the unit stays light
item.loan-info | has-slot | anchor.loan-info-tags | basis:declared | asof:fis12-2.3.0 | grounded-in:fis12-2.3.0:validations/index.yaml#loanInfoTags
```

## Position carries meaning — `scoped-to`

Config keys are position-overloaded: `descriptor.code` under `xinput.head` is not the `code` under
`payment.tags[].list[]`; `pan` means the applicant field only inside `xinput.form.data`. An anchor names
the meaning; **`scoped-to`** confines it to the context where that meaning holds, so one anchor serves
many positions without cloning:

```text
anchor.pan | scoped-to | anchor.xinput-form-data | basis:declared | asof:fis12-2.3.0 | grounded-in:fis12-2.3.0:flows/LAMF/lamf_credit_line_with_mfc#steps[search_1].inputs.jsonSchema.properties.pan
```

`scoped-to` is a declared relation in the [registry](vocabularies.md); the fact is grounded at the config
position that establishes the scoping. Interpreting *what a position means* is done by consulting the
workbench knowledge (a **reference**, never copied into a unit).

## Minimal-diff reuse (verbatim vs tweaked)

| Reuse | How to record |
|---|---|
| a position reuses the meaning **verbatim** | reference the anchor handle — nothing else |
| a position reuses it **with a tweak** | an `instance` with `isa:<anchor>` + one override unit carrying **only the diff**, with a reason (the existing class/instance rule — [frame.md](frame.md)) |

An override that restates the whole meaning instead of the delta is noise — record the diff, not the copy.

## Rules (per-anchor validity)

- **Interned once.** A schematic meaning grounded at a config `&anchor`, or recurring in ≥2 config
  positions, is one anchor node — never restated inline across units. (Interning invariant,
  [invariants.md](invariants.md).)
- **Grounded like any declared fact.** An anchor's `grounded-in` names a config **node/anchor path**,
  never a line number ([unit.md](unit.md#grounding)); `basis:declared`.
- **Light, not a frame.** An anchor earns a frame only if it needs a full rendering; the default is a
  registry row plus units. A referenced-but-unregistered `anchor.*` handle is an `!untethered` gap,
  surfaced for grilling.
- **Occurrence map is derived.** The registry commits canonical meanings; the reverse "who references me"
  is recomputed, never committed.

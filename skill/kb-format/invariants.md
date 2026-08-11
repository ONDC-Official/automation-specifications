# Invariants — what makes the committed set valid

A KB is **valid** iff all of these hold. Operators preserve them on every commit; the structure doesn't
care *how*. Each is tagged **[V]** if the reference [validator](../validators/validate_kb.py) mechanizes
it today, or **[G]** if it is a governance guarantee an operator is trusted to hold. Derived-view
invariants live in [`../derived/governance.md`](../derived/governance.md).

## The unit

1. **Mandatory triple** [V] — every unit carries `subject | relation | object`; the rest is optional.
2. **No orphan handle** [V] — every subject/object resolves to a known node or an allowed literal.
3. **Controlled vocabulary** [V] — relations, `basis` values, and `!flags` are all from
   [vocabularies](vocabularies.md). `not-` is a valid prefix on any relation.
4. **Optional-field consistency** [V] — `basis:inferred ⇔ no grounded-in` (both directions); a config
   anchor names a node, never a line number.
5. **Untethered-must-be-tagged** [G] — a unit with no resolvable grounding (`grounded-in` absent,
   `basis ∉ {inferred, ecosystem}`) is valid only if it carries `!untethered` (or `!deprecated`).
6. **Derive-honesty** [G] — `plane`/`scope`/`grounding-status`/`maturity` appear only as a `!flag` that
   *deviates* from the derivation rule; a flag restating the derived value is noise.
7. **No duplicate / no contradiction** [G] — no exact-duplicate unit; never both `R` and `not-R` with
   identical facets.
8. **Interned-once** [G] — a schematic meaning grounded at a config `&anchor`, or recurring in ≥2 config
   positions, is one [anchor](anchor.md) node referenced by handle — never restated inline across units.
   A position that reuses it with a change records only the delta (instance + `isa` + reason), not a copy.

## Taxonomy & identity

9. **Taxonomy is a DAG** [V] — `isa` has no cycles.
10. **Disjoint consistency** [G] — a `disjoint-with` pair is never both asserted true (directly or via
    inheritance).
11. **Unique handles** [V] — every `id` is unique; a rename leaves a redirect + a `wasRevisionOf` unit.

## Frames & anchors

12. **Atom↔frame traceability** [G] — every frame Fact traces to ≥1 unit; a frame asserts no fact its
    units don't carry. (Body-vs-units drift detection is a deferred operation — see [frame.md](frame.md).)
13. **Anchor grounded & resolvable** [G] — every registered [anchor](anchor.md) carries a config
    node-path ground (`basis:declared`); an `anchor.*` handle referenced but unregistered is an
    `!untethered` gap, never silent. The occurrence map over anchors is derived, never committed.

## Grounding, versioning & change

14. **Inferred/desired quarantine** [V] — `basis:inferred` and `!desired` units are never rendered as
    asserted fact.
15. **asof isolation** [G] — no unit derives a fact for a version other than its own `asof`.
16. **Provenance resolves** [G] — `wasRevisionOf` / `wasDerivedFrom` / `changed-by` targets exist. These
    links live on units; ADR *documents* are an operation buffer, not committed structure.
17. **Config-removal branch followed** [G] — when a grounding config node is removed, exactly one branch
    is taken: **clean up** · **grill** · **deprecate** · **revision-with-version-link**. `asof` stays the
    single versioning mechanism; deprecation is derived from config+asof, never stored.

## Navigation & closed-world

18. **Navigable** [G] — `INDEX.md` and `LOCATOR.md` are present (committed, hand-maintained).
19. **Closed-world integrity** [G] — nothing is asserted that is not a committed unit; absence =
    not-known. Reach-beyond answers are written back quarantined at the lowest basis and promoted only
    through the maturity ladder. `not-` negatives are mandatory infrastructure.

# What lives where in `knowledge/`

A **book** is one domain+version coordinate, e.g. `fis12-2.3.0`. It is the unit of
isolation: atoms carry `asof:<book>` and never mix across books.

```
knowledge/
  <book>/
    atoms.md            the facts. one atom per line. structural atoms first, then a
                        `# --- Stage E candidate units (N) ---` marker, then interpreted ones
    anchors/index.md    interned meanings table: | handle | meaning | grounded-in | asof |
                        `grounded-in: -` = the meaning recurs in several positions, so no
                        single position owns it
    candidate-units.md  the Stage E output before merge — same lines as the tail of atoms.md.
                        Query atoms.md, not this
    frames/*.md         optional per-book node files (flows, error codes, docs) with
                        yaml frontmatter: id, kind, layer, status, asof. Bodies are
                        deliberately light — the facts are in atoms.md, not the prose.
                        Only fis12-2.0.3, fis14-2.1.0, trv11-2.0.1, trv11-2.1.0 have them
  _index/               consolidated, regenerable
    reverse-index.json  "<book>:<file>#<node>" -> [{book, line, s, r, o}]  (which units are
                        grounded at this config node)
    blast-radius.json   "<book>:<file>" -> {direct, prov_hop, total_affected, book_total, untouched}
    cross-book.json     shared_across_books: anchor -> [books]; plus fis_only / trv_only /
                        fis_and_trv lists and book_specific_count
    README.md           human summary of the above
  _work/                per-stage pipeline artifacts, regenerable
    scope-graphs.json   book -> {domain, version, in_scope_files[]}  (keyed release-eks-UPPER)
    ground-map.json     book -> {nodes_grounded, by_kind, roundtrip_rate}  (keyed UPPER)
    sequence-graph.json book -> {entry_actions, action_nodes, edges, flows, total_steps,
                        flow_spines[{flow, n_steps, spine[]}], flags_sample[]}  (keyed UPPER)
    base-conformance.json  book -> deviations from common-config/beckn-base.yaml (keyed lower)
    classification.json    invariant / authoring-style / semantic split across books
    signatures.json, source-change.json, regen-report.json, runtime-annotation.json
    REVIEW-QUEUE.md, STAGE-E-BRIEF.md   human review state from the seeding runs
  _state/               content snapshots used for incremental re-seeding
  _logs/                per-tool run logs
```

`kb_query.py` already normalizes the three different book-key casings above — you should
never have to care which file uses which.

## Ground 0 — the config books

`configs/release-eks-<DOMAIN>-<VERSION>/config/` holds the actual spec the KB was built
from: `index.yaml` (the manifest — scope is whatever it dereferences), `specs/openapi.yaml`,
`actions/index.yaml`, `flows/**`, `attributes/**`, `validations/index.yaml`, `errors/index.yaml`,
`docs/*.md`. A `grounded-in` of `fis12-2.3.0:validations/index.yaml#tags.items.loanInfoTags`
means: open `configs/release-eks-FIS12-2.3.0/config/validations/index.yaml` and walk to that
node path. Node paths are positional and id-based — never line numbers — so they survive edits.

`common-config/beckn-base.yaml` is the shared, human-owned base every book is checked against;
`overview` reports each book's deviations from it.

Grounding references outside a config book:
- `workbench:frames/...` / `workbench:decisions/adr-...` → the runtime knowledge in
  `automation-framework/` (protocol-workbench), used for `basis:authority` atoms.
- bare handles under `basis:derived` → other KB units.

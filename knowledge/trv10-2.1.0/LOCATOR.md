# trv10-2.1.0 — LOCATOR

"Where do I find X" for the `trv10-2.1.0` book (invariant 18). Every row points at a
**committed** surface: a KB file, or the config node-path a fact is grounded at.
Nothing here is a fact — facts live in `atoms.md`.

Config paths are relative to `configs/release-eks-TRV10-2.1.0/config/`.
Handle prefixes: `anchor.*` = registry row · `flow.*` / `action.*` / `concept.*` /
`dom.*` / `usecase.*` = frame.

## Structure

| I want… | Look in | Notes |
|---|---|---|
| every committed fact of this book | `atoms.md` | one pipe-delimited unit per line |
| the meaning of an `anchor.*` handle | `anchors/index.md` | handle → one-line meaning → config ground |
| a declared node (flow / action / concept) | `frames/<id>.md` | filename is the id |
| counts, coverage, book navigation | `INDEX.md` | |
| the Stage E working buffer | `candidate-units.md` | **not** committed fact — do not cite |
| the format contract | `.claude/skills/ondc-kb-seed/kb-format/` | unit · anchor · vocabularies · invariants |

## Facts by question

| Question | Grep / open |
|---|---|
| what does action X do next? | `grep 'anchor.<x> | precedes' atoms.md` → grounded in `actions/index.yaml#supportedActions.<x>` and flow steps |
| who sends a message — BAP or BPP? | `grep 'sent-by' atoms.md` (54 units) |
| what is required / forbidden? | `grep 'requires' atoms.md` (76) · `grep 'not-requires' atoms.md` (40) |
| what constrains a field? | `grep 'constrains' atoms.md` (100) |
| what is a kind of what? | `grep '| isa |' atoms.md` (251) — the IS-A DAG |
| what is scoped to a position? | `grep 'scoped-to' atoms.md` (44) |
| which facts are unverified? | `grep 'basis:inferred' atoms.md` (1) — quarantined, never asserted (invariant 14) |
| which facts came from runtime? | `grep -E 'basis:(sandbox-tested|observed-live)' atoms.md` (9) |
| which facts came from the sector doc? | `grep 'basis:authority' atoms.md` (13) → `docs/overview.md` |

## Config → what it grounds

| I want… | Config node-path | KB entry point |
|---|---|---|
| domain + version identity | `index.yaml#info.domain`, `#info.version`, `#info.x-usecases` | `frames/dom.trv10.md`, `frames/usecase.ride-hailing.md` |
| the action state machine | `actions/index.yaml#supportedActions.<action>` | `frames/action.*.md` (19) |
| async pairing / transaction partners | `actions/index.yaml#apiProperties.<action>` | `atoms.md` |
| the flow catalogue + MANDATORY/OPTIONAL tags | `flows/index.yaml#flows[<FlowId>]` and `…​.tags` | `INDEX.md` flow table |
| one flow's step sequence | `flows/Ride-hailing/<File>.yaml#steps[<action_id>]` | `frames/flow.*.md` (27) |
| per-action attribute shape + field meaning | `attributes/Ride_hailing.yaml#attribute_set.<action>.…​._description` | `anchors/index.md` |
| enum value sets and tag groups | `validations/index.yaml#_TESTS_.<action>[…​]._RETURN_[VALID_ENUM_…​]` | `anchors/index.md` (largest ground: 340 atoms) |
| tag-group validation | `validations/index.yaml#_TESTS_.<action>[…​]._RETURN_[VALIDATE_TAG_…​]` | `concept.route-info`, item/order tag-group anchors |
| required-attribute rules | `validations/index.yaml#_TESTS_.<action>[…​]._RETURN_[REQUIRED_…​]` | `concept.cancellation-term` |
| error codes and who raises them | `errors/index.yaml#code[<code>]` | `atoms.md` — 90201 route not serviceable · 90202 tracking not enabled · 90203 driver not assigned (all BPP) |
| the API surface | `specs/openapi.yaml#paths./<action>` (19 paths) | `anchor.api-endpoint` — only `/search` and `/on_search` are grounded in `atoms.md` |
| sector purpose, actors, key concepts | `docs/overview.md#sector-purpose` · `#real-world-actors` · `#key-concepts` | `concept.rider`, `concept.driver`, `concept.network-interoperability`, `concept.ride-lifecycle`, `concept.driver-assignment` |

## Domain topics → frame

| Topic | Frame |
|---|---|
| ride states (`RIDE_CONFIRMED` · `RIDE_ASSIGNED` · … · `RIDE_ENDED` · `RIDE_CANCELLED`) | `concept.ride-state` — the value set is in `atoms.md`, not here |
| order states (`ACTIVE` · `SOFT_CANCEL` · `SOFT_UPDATE` · … · `CANCELLED` · `COMPLETE`) | `concept.order-status` — the value set is in `atoms.md`, not here |
| on-demand vs scheduled vs rental | `concept.on-demand-ride` · `concept.scheduled-ride` · `concept.rental-ride` · `concept.trip-category` |
| vehicle classes | `concept.vehicle-category` |
| fulfillment type incl. self-pickup | `concept.fulfillment-type` · `concept.self-pickup` |
| pickup / drop / intermediate stops | `concept.stop-type` · `concept.multi-stop-journey` |
| OTP / QR ride authorization | `concept.stop-authorization` |
| who collects the fare, and when | `concept.payment-collector` · `concept.payment-timing` · `concept.bap-collected-settlement` |
| fare breakup, add-ons, tips, bids | `concept.quote-breakup` · `concept.add-on` · `concept.post-order-tip` · `concept.pre-order-bid` |
| network fees and settlement | `concept.buyer-finder-fees` · `concept.settlement-terms` |
| soft/hard cancellation and its terms | `concept.soft-cancel` · `concept.hard-cancel` · `concept.cancellation-term` · `concept.cancellation-reason` · `concept.technical-cancellation` |
| mid-ride amendment | `concept.soft-update` · `concept.update-target` |
| live tracking | `concept.tracking-status` · `concept.route-info` |
| accessibility (purple) tags | `concept.purple-tag` |
| issue & grievance management | `concept.igm` |
| multi-provider discovery | `concept.broadcast-discovery` |

## Traps

| Trap | What to do |
|---|---|
| `attributes/Ride-hailing.yaml` (hyphen) | Orphan twin of `Ride_hailing.yaml` (underscore); unreferenced by `attributes/index.yaml`. Out of scope — never ground to it. |
| a `grounded-in` that looks like a line number | Invalid by construction (invariant 4). Grounds are positional node-paths only. |
| absence of a fact | Closed world — absence means *not known*, not *false* (invariant 19). Look for an explicit `not-` unit before concluding. |
| a fact about `trv10-2.0.1` | Different book. No cross-version inference (invariant 15); see `knowledge/trv10-2.0.1/`. |
| an `anchor.*` handle with no registry row | An `!untethered` gap — surface it, do not invent a meaning (invariant 13). |

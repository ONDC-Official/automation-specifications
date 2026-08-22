# LOCATOR — trv11-2.0.1

Where do I find X. `INDEX.md` says what exists; this page says where to look for it.

Closed world: if a lookup here comes back empty, the KB does not record it — that is an answer,
not a gap to fill from general Beckn knowledge.

## By question

| I want … | look in | how |
|---|---|---|
| what this book is (domain, version, use cases) | `frames/trv11.md`, `INDEX.md` § The book | `index.yaml#info` |
| whether a use case exists (Bus / Metro) | `frames/trv11.bus.md`, `frames/trv11.metro.md` | `index.yaml#info.x-usecases` |
| the list of protocol actions | `INDEX.md` § Actions covered | `actions/index.yaml#supportedActions` |
| what may legally follow an action | `atoms.md` (`precedes`) | `actions/index.yaml#supportedActions.<action>` |
| async pairing / transaction partners of an action | config directly | `actions/index.yaml#apiProperties.<action>` |
| who sends a message (BAP or BPP) | `atoms.md` (`sent-by`), `frames/anchor.bap.md`, `frames/anchor.bpp.md` | `attributes/<UseCase>.yaml#attribute_set.<action>…_description.owner` |
| the api spine of one flow | `frames/flow.*.md` → its config file | `flows/<UseCase>/<file>.yaml#steps` |
| which flows exist and how they are tagged | `INDEX.md` § Flows covered | `flows/index.yaml#flows` |
| whether a flow is certification-mandatory | `frames/anchor.mandatory-flow.md`, `atoms.md` | `flows/index.yaml#flows[<id>].tags` |
| what a flow is for, in one sentence | the flow frame's ground | `flows/<UseCase>/<file>.yaml#meta.description` |
| a single step of a flow (payload, owner, mock) | config directly | `flows/<UseCase>/<file>.yaml#steps[<action_id>]` |
| the `W/O Search1 and Select` variant convention | `frames/anchor.wo-search-and-select-variant.md` | `flows/Metro/USER_CANCELLATION_FLOW__W_O_Search_and_Select_.yaml#steps[init_without_select_METRO_201]` |
| purchase journeys | `frames/anchor.purchase-journey.md`, `frames/flow.bus-purchase-*.md` | `flows/index.yaml#flows[IntraCity_Purchase_Journey_Flow_Code_Based]` |
| cancellation journeys (user · technical · delayed · partial · offline · merchant-side) | `frames/anchor.cancellation-journey.md`, `frames/flow.*cancellation*.md` | `flows/index.yaml#flows[USER_CANCELLATION_FLOW].description` |
| soft vs hard cancel | `frames/anchor.soft-cancel.md`, `atoms.md` | `flows/Metro/USER_CANCELLATION_FLOW.yaml#steps[cancel_soft_METRO_201].mock.defaultPayload.message.descriptor.code` |
| grievance / IGM flows | `frames/anchor.igm-journey.md`, `frames/flow.*igm*.md` | `flows/index.yaml#flows[STATION_CODE_FLOW_ORDER_IGM(v-2.0.0)]` |
| IGM v1 vs v2 | `frames/anchor.igm-v1.md`, `frames/anchor.igm-v2.md` | `validations/index.yaml#_TESTS_.issue[ISSUE_VALIDATION_VERSION_100]` · `…_200` |
| an error code's meaning and who raises it | `frames/error.code-<code>.md` | `errors/index.yaml#code[<code>]` |
| the full error catalogue | `INDEX.md` § Error codes | `errors/index.yaml#code` |
| what an enum / tag / field name means here | `anchors/index.md` (grep the word) | the row's `grounded-in` |
| the validation rule behind a requirement | `atoms.md` (`requires`, `constrains`) | `validations/index.yaml#_TESTS_.<action>[<_NAME_>]` |
| field ownership and description for an action | config directly | `attributes/Bus.yaml` · `attributes/Metro.yaml` `#attribute_set.<action>` |
| the wire schema (request/response shapes) | config directly | `specs/openapi.yaml#paths` |
| auth requirement | `atoms.md` (`requires anchor.subscriber-auth`) | `index.yaml#security` |
| whether the domain is reportable | `atoms.md` | `index.yaml#info.x-reporting` |
| the prose overview / actors / key concepts | config directly (no frame) | `docs/overview.md#summary` · `#real-world-actors` · `#use-cases` · `#key-concepts` |
| release notes / references | `frames/docs.release-notes.md`, `frames/docs.references.md` | `docs/release-notes.md` · `docs/references.md` |
| what config file scope was seeded | `INDEX.md` § The book | `index.yaml` — scope is whatever it dereferences |

## By KB surface

| surface | holds | shape |
|---|---|---|
| `atoms.md` | every fact | `subject \| relation \| object \| basis:… \| asof:trv11-2.0.1 \| grounded-in:…` |
| `anchors/index.md` | 178 interned meanings | `\| handle \| meaning \| grounded-in \| asof \|` |
| `frames/*.md` | 93 node files | frontmatter `id · kind · layer · status · asof` + a light body with one `Grounded at:` |
| `candidate-units.md` | Stage E output before merge | same lines as the tail of `atoms.md` — query `atoms.md` instead |
| `INDEX.md` | what exists, and the covered flow / action / error lists | this book only |

## Handle shapes

| prefix | means | example |
|---|---|---|
| `trv11`, `trv11.<usecase>` | the domain and its use cases | `trv11.metro` |
| `flow.<usecase>-<name>` | one flow declared in `flows/index.yaml` | `flow.metro-partial-cancellation` |
| `error.code-<n>` | one entry of `errors/index.yaml#code` | `error.code-91211` |
| `anchor.<kebab>` | an interned meaning — action, role, enum, tag group, field semantic | `anchor.on-confirm` |
| `docs.<name>` | a doc note | `docs.release-notes` |

A `grounded-in` reads `trv11-2.0.1:<file>#<node-path>` — open
`configs/release-eks-TRV11-2.0.1/config/<file>` and walk the path. Node paths are positional and
id-based, never line numbers, so they survive edits. Grounds that begin `workbench:` point at
`automation-framework/knowledge/protocol-workbench/`, not at this config book.

## Query instead of grepping

```bash
KB=.claude/skills/ondc-kb/kb_query.py
python3 $KB overview trv11-2.0.1
python3 $KB about anchor.on-confirm --book trv11-2.0.1
python3 $KB flows trv11-2.0.1 cancellation
python3 $KB atoms --book trv11-2.0.1 --subject anchor.confirm --relation precedes
python3 $KB search "station code" --book trv11-2.0.1
python3 $KB frames trv11-2.0.1 anchor.igm-v2
python3 $KB ground "flows/index.yaml#flows[USER_CANCELLATION_FLOW].tags"
```

## Nearby books

`trv11-2.0.0` (predecessor) and `trv11-2.1.0` (successor) are separate books — `asof` isolation
means no fact crosses between them. Use `python3 $KB compare trv11-2.0.1 trv11-2.1.0` for the diff.

# LOCATOR — fis14-2.1.0

"Where do I find X" for the `fis14-2.1.0` book (invariant 18). Start here, then follow the
pointer. Config paths are rooted at `configs/release-eks-FIS14-2.1.0/config/`.

## In the KB

| I want to know… | Look in | How to find it |
|---|---|---|
| a plain fact ("does select require provider id?") | [`atoms.md`](atoms.md) | grep the subject handle, e.g. `grep '^anchor.select |' atoms.md` |
| what a shared meaning *is* (its canonical one-liner + where it was interned) | [`anchors/index.md`](anchors/index.md) | grep the handle, e.g. `anchor.payment-mandate` |
| whether a node exists at all, and its kind/layer/asof | [`frames/`](frames/) | file name is the id: `frames/<id>.md` |
| the flows, actions, errors and concepts this book covers, with counts | [`INDEX.md`](INDEX.md) | the coverage tables |
| something proposed but **not** asserted | [`candidate-units.md`](candidate-units.md) | uncommitted — never cite as fact |
| what is *not* true (closed-world negatives) | [`atoms.md`](atoms.md) | grep `not-`, e.g. `not-part-of`, `not-requires` |
| a fact the model guessed rather than read | [`atoms.md`](atoms.md) | grep `basis:inferred` — quarantined, never asserted |
| a fact with no resolvable ground | [`atoms.md`](atoms.md) | grep `!untethered` / `!deprecated` |

## By entity

| Entity | Frame id pattern | Grounded at (config node-path) |
|---|---|---|
| domain | `dom.fis14` | `index.yaml#info.domain` |
| flow | `flow.<config-id kebabed>` | `flows/index.yaml#flows[<Config_Id>].tags` |
| protocol action | `action.<action kebabed>` | `actions/index.yaml#supportedActions.<action>` |
| mutual-fund concept | `concept.<code kebabed>` | `attributes/MUTUAL_FUNDS.yaml#attribute_set.on_search.message.catalog.providers.fulfillments.type._description.enums[<CODE>]` |
| error code | `error.<slug>` | `errors/index.yaml#code[<822xxx>].Description` |
| interned meaning | `anchor.<kebab>` (registry row, **no frame**) | see the row's `grounded-in` column |

## In the config

| I want to know… | Config file | Node to open |
|---|---|---|
| which domain / version / usecase this release is | `index.yaml` | `info.domain`, `info.version`, `info.x-usecases` |
| which actions exist and what may follow each | `actions/index.yaml` | `supportedActions.<action>` |
| which action is a callback of which, and its transaction partner | `actions/index.yaml` | `apiProperties.<action>.async_predecessor` · `.transaction_partner` |
| the full flow list with families and descriptions | `flows/index.yaml` | `flows[<id>].tags` · `.description` · `.usecase` |
| the step-by-step API sequence of one flow | `flows/MUTUAL FUNDS/<Flow>.yaml` | `steps[<step>]` (`.api`, `.owner`, `.unsolicited`, `.examples`, `.mock`) |
| the per-attribute dictionary: owner, required, enums, usage | `attributes/MUTUAL_FUNDS.yaml` | `attribute_set.<action>.<json path>._description` |
| every mutual-fund fulfillment type and its meaning | `attributes/MUTUAL_FUNDS.yaml` | `attribute_set.on_search.message.catalog.providers.fulfillments.type._description.enums` |
| what a payload must contain / what values are legal | `validations/index.yaml` | `_TESTS_.<action>[<TEST_NAME>]` then `._RETURN_[…]` |
| the guard that skips a test when data is absent | `validations/index.yaml` | `._CONTINUE_` inside the test |
| the subtree a test applies to | `validations/index.yaml` | `._SCOPE_` (a JSONPath into the payload) |
| a legal enum list / regex / required tag group | `validations/index.yaml` | `.enumList` · `.reg` · `.validTags` · `.validValues` |
| the error catalogue | `errors/index.yaml` | `code[<822xxx>]` (`.Description`, `.Event`) |
| the wire schema of a Beckn object | `specs/openapi.yaml` | `components.schemas.<Object>` |
| the HTTP surface | `specs/openapi.yaml` | `paths./<action>` |
| release rationale, changes and external references | `docs/` | `overview.md` · `release-notes.md` · `references.md` |

## Rules of the road

- A grounding pointer is a **positional node-path**, never a line number — positions survive
  reorganisation.
- Absence is **not-known**, not false. If no unit says it, the KB does not assert it.
- Only [`atoms.md`](atoms.md) carries fact-truth; frame bodies are deliberately light and
  assert nothing the units do not carry.
- Validate after any edit: `python3 .claude/skills/ondc-kb-seed/tools/validate_kb.py knowledge/fis14-2.1.0`

# INDEX — `fis10-giftcard-2.1.0`

Committed navigation surface for this book (invariant 18). Nothing here is a fact of record —
every fact lives in [`atoms.md`](atoms.md); this page only says where to look.

| | |
|---|---|
| book id | `fis10-giftcard-2.1.0` |
| domain / version | `ONDC:FIS10` · `2.1.0` (`index.yaml#info.domain`, `index.yaml#info.version`) |
| use case | `gift-card` (`index.yaml#info.x-usecases`) |
| config book | `configs/release-eks-FIS10-GIFTCARD-2.1.0/config/` |
| atoms | **480** (29 structural + 451 Stage E) |
| anchors | **156** registry rows |
| frames | **72** |

## Files

| file | what it holds |
|---|---|
| [`atoms.md`](atoms.md) | the facts — one unit per line, `subject \| relation \| object \| basis \| asof \| grounded-in \| !flags`. Structural units first, then the `# --- Stage E candidate units (451) ---` marker, then the interpreted ones |
| [`anchors/index.md`](anchors/index.md) | the interned-meaning registry — `handle → meaning → grounded-in → asof`. `grounded-in: -` means no single position owns the meaning |
| [`frames/`](frames/) | 72 node files, one per significant entity. Frontmatter `id, kind, layer, status, asof`; bodies deliberately light |
| [`candidate-units.md`](candidate-units.md) | pre-merge Stage E output. Query `atoms.md`, not this |
| [`LOCATOR.md`](LOCATOR.md) | "where do I find X" lookup |

## Flows covered (6)

All six are `type: playground`, `usecase: gift-card`, tagged `WORKBENCH` + `REPORTABLE` in
`flows/index.yaml`. Step spines are the `steps[].action_id` sequence at each flow's config file.

| flow id | frame | config | step spine |
|---|---|---|---|
| `Seller_App_Fulfilling` | [`anchor.flow.seller-app-fulfilling`](frames/anchor.flow.seller-app-fulfilling.md) | `flows/gift-card/Seller_App_Fulfilling.yaml` | search → on_search → select → on_select → init → on_init → confirm → on_confirm → status → on_status |
| `Buyer_App_Fulfilling_Code_On_Confirm` | [`anchor.flow.buyer-app-fulfilling-code-on-confirm`](frames/anchor.flow.buyer-app-fulfilling-code-on-confirm.md) | `flows/gift-card/Buyer_App_Fulfilling_Code_On_Confirm.yaml` | search → on_search → select → on_select → init → on_init → confirm → on_confirm → status → on_status |
| `Buyer_App_Fulfilling_Code_On_Update` | [`anchor.flow.buyer-app-fulfilling-code-on-update`](frames/anchor.flow.buyer-app-fulfilling-code-on-update.md) | `flows/gift-card/Buyer_App_Fulfilling_Code_On_Update.yaml` | search → on_search → select → on_select → init → on_init → confirm → on_confirm → on_update *(unsolicited)* |
| `Physical_Store_Based_Gift_Cards` | [`anchor.flow.physical-store-based-gift-cards`](frames/anchor.flow.physical-store-based-gift-cards.md) | `flows/gift-card/Physical_Store_Based_Gift_Cards.yaml` | search → on_search → select → on_select → init → on_init → confirm → on_confirm → status → on_status |
| `Seller_Cancellation` | [`anchor.flow.seller-cancellation`](frames/anchor.flow.seller-cancellation.md) | `flows/gift-card/Seller_Cancellation.yaml` | search → on_search → select → on_select → init → on_init → confirm → on_confirm → on_cancel *(unsolicited)* |
| `Update_Receiver_Info` | [`anchor.flow.update-receiver-info`](frames/anchor.flow.update-receiver-info.md) | `flows/gift-card/Update_Receiver_Info.yaml` | search → on_search → select → on_select → init → on_init → confirm → on_confirm → unsolicited_on_status *(unsolicited)* → update → on_update → status → on_status |

## Actions covered (14)

Every key of `actions/index.yaml#supportedActions` (the `"null"` entry is the transaction-entry
marker, not an action). Each has a `kind: class`, `layer: protocol` frame.

| BAP-sent | BPP-sent |
|---|---|
| [`search`](frames/anchor.search.md) · [`select`](frames/anchor.select.md) · [`init`](frames/anchor.init.md) · [`confirm`](frames/anchor.confirm.md) · [`status`](frames/anchor.status.md) · [`update`](frames/anchor.update.md) · [`cancel`](frames/anchor.cancel.md) | [`on_search`](frames/anchor.on-search.md) · [`on_select`](frames/anchor.on-select.md) · [`on_init`](frames/anchor.on-init.md) · [`on_confirm`](frames/anchor.on-confirm.md) · [`on_status`](frames/anchor.on-status.md) · [`on_update`](frames/anchor.on-update.md) · [`on_cancel`](frames/anchor.on-cancel.md) |

`on_status_update_receiver_info` appears only as a successor of `on_confirm` in
`supportedActions`, never as a key of its own — it is registered as the anchor
`anchor.on-status-update-receiver-info` (registry row only, no frame).

Three unsolicited callbacks are framed separately because the config marks them
`unsolicited: true` with `responseFor: null`:
[`anchor.unsolicited-on-update`](frames/anchor.unsolicited-on-update.md) ·
[`anchor.unsolicited-on-cancel`](frames/anchor.unsolicited-on-cancel.md) ·
[`anchor.unsolicited-on-status`](frames/anchor.unsolicited-on-status.md).

`rating`, `support` and `track` are **not** in this book's `supportedActions` — recorded as
explicit `not-part-of` units in `atoms.md`, not as frames.

## Frames by kind (72)

| group | kind · layer | n | examples |
|---|---|---|---|
| protocol actions | `class` · `protocol` | 14 | `anchor.search`, `anchor.on-confirm` |
| flows | `instance` · `domain` | 6 | `anchor.flow.seller-app-fulfilling` |
| unsolicited callbacks | `instance` · `protocol` | 3 | `anchor.unsolicited-on-status` |
| Beckn schema objects | `class` · `protocol` | 11 | `anchor.item`, `anchor.stop`, `anchor.authorization` |
| validation gates | `pattern` · `protocol` | 2 | `anchor.context-required`, `anchor.stale-version-gate` |
| runtime concepts | `concept` · `protocol` | 2 | `anchor.session-key`, `anchor.unsolicited-callback` |
| domain concepts | `concept` · `domain` | 24 | `anchor.gift-card`, `anchor.code-delivery`, `anchor.fulfillment-type` |
| error codes | `instance` · `domain` | 10 | `anchor.error-80214` |

An anchor does not need a frame ([anchor.md](../../.claude/skills/ondc-kb-seed/kb-format/anchor.md)) —
the other 84 registry rows are light rows plus units.

## Where the units are grounded

| config file | units grounded there |
|---|---|
| `validations/index.yaml` | 144 |
| `flows/gift-card/Seller_App_Fulfilling.yaml` | 53 |
| `actions/index.yaml` | 51 |
| `attributes/gift_card.yaml` | 44 |
| `specs/openapi.yaml` | 27 |
| `flows/gift-card/Update_Receiver_Info.yaml` | 26 |
| `errors/index.yaml` | 19 |
| `flows/gift-card/Seller_Cancellation.yaml` | 18 |
| `flows/index.yaml` | 16 |
| `docs/overview.md` | 10 |
| `flows/gift-card/Buyer_App_Fulfilling_Code_On_Update.yaml` | 8 |
| `flows/gift-card/Physical_Store_Based_Gift_Cards.yaml` | 8 |
| `flows/gift-card/Buyer_App_Fulfilling_Code_On_Confirm.yaml` | 5 |
| `index.yaml` | 4 |
| `docs/references.md`, `docs/release-notes.md` | 1 each |

Off-config grounds: 18 units on `workbench:` (basis `authority`), 6 on a KB anchor handle
(basis `derived`), 5 with no ground (basis `inferred`), 16 carrying `!untethered`.

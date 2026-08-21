# trv13-2.0.1 — book index

| | |
|---|---|
| book id | `trv13-2.0.1` |
| domain | `ONDC:TRV13` (`index.yaml#info.domain`) |
| version | `2.0.1` (`index.yaml#info.version`) |
| usecase | `Hotel-Booking-V2` (`index.yaml#info.x-usecases`) |
| config | `configs/release-eks-TRV13-2.0.1/config/` |
| asof on every unit | `trv13-2.0.1` |

## Size

| surface | count | file |
|---|---|---|
| atoms | 407 | [`atoms.md`](atoms.md) |
| anchors (interned meanings) | 248 | [`anchors/index.md`](anchors/index.md) |
| frames | 64 | [`frames/`](frames/) |
| candidate units (not committed as atoms) | — | [`candidate-units.md`](candidate-units.md) |

Atom basis mix: `declared` 392 · `authority` 11 · `inferred` 2 · `derived` 2.
Hand-written flags: `!untethered` 3 (the `anchor.tag-group` / `anchor.tag-list` base-deviation
trio at the end of `atoms.md`). `basis:inferred` units are quarantined — never assert them.

## Frames

| group | kind / layer | count |
|---|---|---|
| flows | `instance` / `domain` | 7 |
| protocol actions | `class` / `protocol` | 19 |
| action specialisations seen at flow steps | `instance` / `protocol` | 4 |
| domain concepts (incl. domain + usecase) | `concept` / `domain` | 34 |

An anchor does **not** need a frame; the 248-row anchor registry is the lookup surface and only
recurring, significant meanings were framed.

## Flows covered (7)

All seven belong to the `Hotel-Booking-V2` usecase, declared at `flows/index.yaml#flows[…]`.

| frame | config flow id | tags | steps | action spine |
|---|---|---|---|---|
| [`anchor.flow-buyer-cancellation`](frames/anchor.flow-buyer-cancellation.md) | `Buyer Side Full Cancellation` | REPORTABLE, MANDATORY, WORKBENCH | 12 | search → on_search → select → on_select → init → on_init → confirm → on_confirm → status → on_status → cancel → on_cancel |
| [`anchor.flow-ttl-booking`](frames/anchor.flow-ttl-booking.md) | `Hotel Booking (ttl based) booking` | REPORTABLE, MANDATORY, WORKBENCH | 4 | search → on_search → search → on_search |
| [`anchor.flow-seller-pagination`](frames/anchor.flow-seller-pagination.md) | `Hotel Booking Seller App Pagination Flow` | REPORTABLE, MANDATORY, WORKBENCH | 5 | search → on_search ×4 |
| [`anchor.flow-merchant-cancellation`](frames/anchor.flow-merchant-cancellation.md) | `Merchant Side Full Cancellation` | REPORTABLE, MANDATORY, WORKBENCH | 11 | search … on_status → on_cancel (unsolicited) |
| [`anchor.flow-city-code`](frames/anchor.flow-city-code.md) | `Order to Confirm to Fulfillment (City Code)` | REPORTABLE, MANDATORY, WORKBENCH | 11 | search … on_status → on_status |
| [`anchor.flow-updates-in-booking`](frames/anchor.flow-updates-in-booking.md) | `Order to Confirm to Fulfillment (Updates in Booking)` | REPORTABLE, OPTIONAL, WORKBENCH | 12 | search … on_status → update → on_update |
| [`anchor.flow-city-code-igm`](frames/anchor.flow-city-code-igm.md) | `Order_to_Confirm_to_Fulfillment_City_Code_with_igm_1.0.0` | MANDATORY, WORKBENCH | 15 | search … on_status → issue → on_issue → on_issue_status → issue |

## Actions covered (19)

Declared at `actions/index.yaml#supportedActions.<action>`; the successor list at that node is
what `precedes` units are grounded in, and `apiProperties.<action>.async_predecessor` /
`.transaction_partner` back the `requires` / `not-requires` units.

| phase | actions |
|---|---|
| discovery | [`search`](frames/anchor.search.md) · [`on_search`](frames/anchor.on-search.md) |
| offer | [`select`](frames/anchor.select.md) · [`on_select`](frames/anchor.on-select.md) |
| order | [`init`](frames/anchor.init.md) · [`on_init`](frames/anchor.on-init.md) · [`confirm`](frames/anchor.confirm.md) · [`on_confirm`](frames/anchor.on-confirm.md) |
| fulfillment | [`status`](frames/anchor.status.md) · [`on_status`](frames/anchor.on-status.md) · [`track`](frames/anchor.track.md) · [`on_track`](frames/anchor.on-track.md) |
| post-order | [`update`](frames/anchor.update.md) · [`on_update`](frames/anchor.on-update.md) · [`cancel`](frames/anchor.cancel.md) · [`on_cancel`](frames/anchor.on-cancel.md) |
| grievance (IGM) | [`issue`](frames/anchor.issue.md) · [`on_issue`](frames/anchor.on-issue.md) · [`on_issue_status`](frames/anchor.on-issue-status.md) |

`search` is the only transaction entry (`supportedActions.null`). `/track` and `/on_track` have
no OpenAPI path in this book — see the `not-has-slot` units grounded at `specs/openapi.yaml#paths`.

## Links

- [`LOCATOR.md`](LOCATOR.md) — where to find X (config side and KB side)
- [`atoms.md`](atoms.md) — the committed facts; every line is `subject | relation | object | …`
- [`anchors/index.md`](anchors/index.md) — handle → canonical meaning → config ground
- [`frames/`](frames/) — one file per framed node, filename = frame `id`
- format contract: `.claude/skills/ondc-kb-seed/kb-format/`
- validator: `python3 .claude/skills/ondc-kb-seed/tools/validate_kb.py knowledge/trv13-2.0.1`

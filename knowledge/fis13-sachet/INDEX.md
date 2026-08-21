# INDEX — fis13-sachet

Navigation surface for this book (invariant 18). Counts are as reported by
`python3 .claude/skills/ondc-kb-seed/tools/validate_kb.py knowledge/fis13-sachet`.

| field | value |
|---|---|
| book id (`asof`) | `fis13-sachet` |
| config release | `configs/release-eks-FIS13-sachet/config/` |
| domain | `ONDC:FIS13` (`index.yaml#info.domain`) |
| branch | `draft-FIS13-sachet` (`index.yaml#info.x-branch-name`) |
| spec version | `2.0.0` (`index.yaml#info.version`) |
| atoms | 693 |
| anchors | 169 |
| frames | 63 |
| ADRs | 0 |

## Files

| file | what it holds |
|---|---|
| [`atoms.md`](atoms.md) | the committed units — every fact for this book. **Source of truth.** |
| [`anchors/index.md`](anchors/index.md) | interned-meaning registry: handle → canonical meaning → config ground |
| [`frames/`](frames/) | 63 light frames (declaration + ground); facts stay in `atoms.md` |
| [`candidate-units.md`](candidate-units.md) | pre-commit staging buffer — **not** committed fact |
| [`LOCATOR.md`](LOCATOR.md) | "where do I find X" table |

## Use cases covered (3)

`accidental-insurance` · `hospicash-insurance` · `transit-insurance`
— declared at `index.yaml#info.x-usecases`.

## Flows covered (12)

Four flow shapes × three use cases; all are `type: playground`, all tagged
`MANDATORY` + `REPORTABLE` + `WORKBENCH` (`flows/index.yaml`).

| flow shape | accidental | hospicash | transit |
|---|---|---|---|
| CD-balance error | [`anchor.flow-cd-balance-accidental`](frames/anchor.flow-cd-balance-accidental.md) | [`anchor.flow-cd-balance-hospicash`](frames/anchor.flow-cd-balance-hospicash.md) | [`anchor.flow-cd-balance-transit`](frames/anchor.flow-cd-balance-transit.md) |
| insurer/master-policy discovery | [`anchor.flow-provider-discovery-accidental`](frames/anchor.flow-provider-discovery-accidental.md) | [`anchor.flow-provider-discovery-hospicash`](frames/anchor.flow-provider-discovery-hospicash.md) | [`anchor.flow-provider-discovery-transit`](frames/anchor.flow-provider-discovery-transit.md) |
| product discovery | [`anchor.flow-product-discovery-accidental`](frames/anchor.flow-product-discovery-accidental.md) | [`anchor.flow-product-discovery-hospicash`](frames/anchor.flow-product-discovery-hospicash.md) | [`anchor.flow-product-discovery-transit`](frames/anchor.flow-product-discovery-transit.md) |
| purchase journey | [`anchor.flow-purchase-journey-accidental`](frames/anchor.flow-purchase-journey-accidental.md) | [`anchor.flow-purchase-journey-hospicash`](frames/anchor.flow-purchase-journey-hospicash.md) | [`anchor.flow-purchase-journey-transit`](frames/anchor.flow-purchase-journey-transit.md) |

`PRAMAAN` additionally tags the two purchase journeys for hospicash
(`flows/index.yaml#flows[7].tags[PRAMAAN]`) and transit
(`flows/index.yaml#flows[11].tags[PRAMAAN]`).

## Actions covered (16)

All 16 keys of `actions/index.yaml#supportedActions`. Sender per
`attributes/*.yaml#attribute_set.<action>.context.action._description.owner`.

| BAP-sent | BPP-sent |
|---|---|
| [`anchor.search`](frames/anchor.search.md) | [`anchor.on-search`](frames/anchor.on-search.md) |
| [`anchor.select`](frames/anchor.select.md) | [`anchor.on-select`](frames/anchor.on-select.md) |
| [`anchor.init`](frames/anchor.init.md) | [`anchor.on-init`](frames/anchor.on-init.md) |
| [`anchor.confirm`](frames/anchor.confirm.md) | [`anchor.on-confirm`](frames/anchor.on-confirm.md) |
| [`anchor.status`](frames/anchor.status.md) | [`anchor.on-status`](frames/anchor.on-status.md) |
| [`anchor.update`](frames/anchor.update.md) | [`anchor.on-update`](frames/anchor.on-update.md) |
| [`anchor.cancel`](frames/anchor.cancel.md) | [`anchor.on-cancel`](frames/anchor.on-cancel.md) |
| [`anchor.track`](frames/anchor.track.md) | [`anchor.on-track`](frames/anchor.on-track.md) |

The purchase-journey happy path exercised by the flows is
`search → on_search → select → on_select → init → on_init → confirm → on_confirm → on_update`;
`status`, `cancel`, `track` and their callbacks are declared in `supportedActions`
but not stepped by any flow in this release (see the `not-part-of` units in `atoms.md`).

## Concept frames (35)

Domain layer: the three use cases, the domain and book nodes, master policy,
insurance product / category code, policy id + document, cancellation terms,
CD-balance check + error, the five tag groups
(`MASTER_POLICY`, `BAP_INPUTS`, `GENERAL_INFO`, `POLICY_INFO`, `NOMINEE_DETAILS`),
accidental / hospicash benefit terms, transit consignment inputs, the three flow
tags (`MANDATORY`, `REPORTABLE`, `PRAMAAN`), order quote, fulfillment state,
order status, and the three search variants.

Protocol layer: `anchor.search-variant`, `anchor.context-envelope`,
`anchor.api-surface`, `anchor.tag-group`, `anchor.fis13-error-catalog`.

## Not framed (deliberate)

Per [`anchor.md`](../../.claude/skills/ondc-kb-seed/kb-format/anchor.md) an anchor is a
registry row, not a frame. The remaining 106 anchors — leaf field anchors, regex/format
anchors, the 19 `anchor.err-8220xx` codes, and the workbench-grounded runtime concepts
(`anchor.bap`, `anchor.bpp`, `anchor.validation-rule`, …) — stay registry rows.
See LOCATOR.md for how to reach them.

## Links

- Contract: [`kb-format/`](../../.claude/skills/ondc-kb-seed/kb-format/) —
  [unit](../../.claude/skills/ondc-kb-seed/kb-format/unit.md) ·
  [anchor](../../.claude/skills/ondc-kb-seed/kb-format/anchor.md) ·
  [vocabularies](../../.claude/skills/ondc-kb-seed/kb-format/vocabularies.md) ·
  [invariants](../../.claude/skills/ondc-kb-seed/kb-format/invariants.md)
- Validator: `.claude/skills/ondc-kb-seed/tools/validate_kb.py`
- Config release: `configs/release-eks-FIS13-sachet/config/`
- Sibling FIS13 book: [`../fis13-health-2.0.1/`](../fis13-health-2.0.1/)

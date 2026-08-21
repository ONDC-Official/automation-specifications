# INDEX — fis14-2.1.0

Navigation surface for the `fis14-2.1.0` book (invariant 18). Counts are the committed
state of this directory; every `Grounded at` path in a frame resolves to a node in the
release config, never to a line number.

| field | value |
|---|---|
| book id | `fis14-2.1.0` |
| domain | `ONDC:FIS14` — grounded at `fis14-2.1.0:index.yaml#info.domain` |
| version | `2.1.0` |
| usecase | `MUTUAL FUNDS` — grounded at `fis14-2.1.0:attributes/MUTUAL_FUNDS.yaml#meta.use_case_id` |
| config release | `configs/release-eks-FIS14-2.1.0/config/` |

## Counts

| surface | count | file |
|---|---|---|
| atoms | 501 | [`atoms.md`](atoms.md) |
| anchors | 221 | [`anchors/index.md`](anchors/index.md) |
| frames | 82 | [`frames/`](frames/) |
| candidate units (uncommitted) | — | [`candidate-units.md`](candidate-units.md) |

### Frames by prefix

| prefix | kind · layer | count | covers |
|---|---|---|---|
| `dom.*` | concept · domain | 1 | the domain node `dom.fis14` |
| `flow.*` | instance · domain | 33 | every flow in `flows/index.yaml` |
| `action.*` | class · protocol | 15 | every action in `actions/index.yaml#supportedActions` |
| `concept.*` | concept · domain | 14 | the mutual-fund fulfillment concepts |
| `error.*` | instance · domain | 19 | every code in `errors/index.yaml#code` |

## Flows covered — 33 / 33

Grounded at `fis14-2.1.0:flows/index.yaml#flows[<id>].tags`. Grouped by the flow-family
tag the config assigns.

| family tag | flows |
|---|---|
| `SEARCH_FLOWS` | `flow.main-search` · `flow.search-incremental-pull` |
| `LUMPSUM_FLOWS` | `flow.lumpsum-existing-folio` · `flow.lumpsum-new-folio` · `flow.lumpsum-new-folio-with-kyc` · `flow.lumpsum-payment-by-buyer-app` · `flow.lumpsum-payment-retry` · `flow.cart-lumpsum-investment` · `flow.cart-lumpsum-investment-part-failure` |
| `SIP_SETUP_FLOWS` | `flow.sip-creation-new-folio` · `flow.sip-creation-new-folio-with-kyc` · `flow.sip-creation-existing-folio` · `flow.sip-creation-without-payment-mandate` · `flow.sip-without-payment-mandate` · `flow.sip-manual-trigger-instalment` · `flow.sip-completion` · `flow.sip-auto-cancellation` · `flow.sip-cancellation-by-the-investor` · `flow.cart-sip-creation` |
| `SIP_LIFECYCLE_FLOWS` | `flow.sip-instalment` · `flow.sip-instalment-failure` · `flow.sip-modification-change-amount` · `flow.sip-modification-pause` · `flow.sip-new-payment-update` · `flow.cart-sip-installment` |
| `REDEMPTION_FLOWS` | `flow.redemption-by-amount` · `flow.redemption-by-units` · `flow.redemption-redeem-all` |
| `STP_FLOWS` / `STP_LIFECYCLE_FLOWS` | `flow.stp-by-amount` · `flow.stp-installment` |
| `SWP_FLOWS` / `SWP_LIFECYCLE_FLOWS` | `flow.swp-by-amount` · `flow.swp-installment` |
| `SWITCH_FLOWS` | `flow.switch-by-amount` |

Cross-cutting tags the config also carries on these flows: `WORKBENCH`, `REPORTABLE`,
`CART_FLOWS`, `USER_INITIATED`, `UNSOLICITED`, `HYBRID`.

## Actions covered — 15 / 15

Grounded at `fis14-2.1.0:actions/index.yaml#supportedActions.<action>`.

| BAP-side | BPP-side |
|---|---|
| `action.search` | `action.on-search` |
| `action.select` | `action.on-select` |
| `action.init` | `action.on-init` |
| `action.confirm` | `action.on-confirm` |
| `action.update` | `action.on-update` |
| `action.status` | `action.on-status` |
| `action.issue` | `action.on-issue` · `action.on-issue-status` |

`cancel`, `track`, `rating` and `support` are **not** part of this book's action set —
recorded as `not-part-of anchor.fis14-action-set` units in [`atoms.md`](atoms.md).

## Mutual-fund concepts covered — 14

Grounded at
`fis14-2.1.0:attributes/MUTUAL_FUNDS.yaml#attribute_set.on_search.message.catalog.providers.fulfillments.type._description.enums[<code>]`.

`concept.lumpsum` · `concept.sip` · `concept.sip-instalment` · `concept.swp` ·
`concept.redemption` · `concept.switch-out` · `concept.switch-in` · `concept.stp-out` ·
`concept.stp-in` · `concept.stp-out-instalment` · `concept.stp-in-instalment` ·
`concept.kyc` · `concept.payment-mandate` · `concept.zero-balance-folio`

## Errors covered — 19 / 19

Codes `822001`–`822019`, grounded at `fis14-2.1.0:errors/index.yaml#code[<code>].Description`.
See [`frames/`](frames/) for the `error.*` frames and [`atoms.md`](atoms.md) for what each
code constrains.

## Links

- [`atoms.md`](atoms.md) — the committed triples (the only fact-truth)
- [`anchors/index.md`](anchors/index.md) — interned schematic meanings, handle → meaning → ground
- [`frames/`](frames/) — one file per node, `<id>.md`
- [`candidate-units.md`](candidate-units.md) — uncommitted candidates, not asserted
- [`LOCATOR.md`](LOCATOR.md) — "where do I find X"
- config: `configs/release-eks-FIS14-2.1.0/config/` — `index.yaml`, `actions/`, `attributes/`,
  `errors/`, `flows/`, `specs/`, `validations/`, `docs/`

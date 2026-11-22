# END_STOP_UPDATE_FLOW (W/O Search1 and Select) — Sequence Diagrams

Internal data file consumed by the Developer Guide's "Sequence Diagram" tab (API Walkthrough).
Not meant to be shown as its own docs page — the frontend filters this slug out of the Use Case
Brief / Additional Resources / Changelog tab lists and instead looks up the section matching the
selected API call's `action_id` (the `##` heading below) to render that step's diagram.

One `## <action_id>` heading per step of `END_STOP_UPDATE_FLOW__W_O_Search_and_Select_.yaml` (Metro), in that flow's own step order, each followed by its Mermaid `sequenceDiagram`: the whole flow, with that call's own message(s) highlighted — same convention as the other domains' per-step sequence-diagram docs.

## search2_METRO_201

```mermaid
sequenceDiagram
  participant Buyer App (BAP)
  participant Gateway
  participant Seller App (BPP)
  rect rgb(191, 223, 255)
  Buyer App (BAP)->>Seller App (BPP): /search (A to B, peer-to-peer)
  end
  Seller App (BPP)-->>Buyer App (BAP): /on_search (catalog)
  Buyer App (BAP)->>Seller App (BPP): /init (payment NOT-PAID)
  Seller App (BPP)-->>Buyer App (BAP): /on_init (payment NOT-PAID)
  Buyer App (BAP)->>Seller App (BPP): /confirm (payment PAID)
  Seller App (BPP)-->>Buyer App (BAP): /on_confirm (order.status None)
  Buyer App (BAP)->>Seller App (BPP): /update (update_target order.fulfillments)
  Seller App (BPP)-->>Buyer App (BAP): /on_update (order.status SOFT_UPDATE)
  Buyer App (BAP)->>Seller App (BPP): /update (update_target order.fulfillments)
  Seller App (BPP)-->>Buyer App (BAP): /on_update (order.status UPDATED)
  Buyer App (BAP)->>Seller App (BPP): /update (update_target payments)
  Seller App (BPP)-->>Buyer App (BAP): /on_update (order.status UPDATED)
```

## on_search2_METRO_201

```mermaid
sequenceDiagram
  participant Buyer App (BAP)
  participant Gateway
  participant Seller App (BPP)
  Buyer App (BAP)->>Seller App (BPP): /search (A to B, peer-to-peer)
  rect rgb(191, 223, 255)
  Seller App (BPP)-->>Buyer App (BAP): /on_search (catalog)
  end
  Buyer App (BAP)->>Seller App (BPP): /init (payment NOT-PAID)
  Seller App (BPP)-->>Buyer App (BAP): /on_init (payment NOT-PAID)
  Buyer App (BAP)->>Seller App (BPP): /confirm (payment PAID)
  Seller App (BPP)-->>Buyer App (BAP): /on_confirm (order.status None)
  Buyer App (BAP)->>Seller App (BPP): /update (update_target order.fulfillments)
  Seller App (BPP)-->>Buyer App (BAP): /on_update (order.status SOFT_UPDATE)
  Buyer App (BAP)->>Seller App (BPP): /update (update_target order.fulfillments)
  Seller App (BPP)-->>Buyer App (BAP): /on_update (order.status UPDATED)
  Buyer App (BAP)->>Seller App (BPP): /update (update_target payments)
  Seller App (BPP)-->>Buyer App (BAP): /on_update (order.status UPDATED)
```

## init_without_select_METRO_201

```mermaid
sequenceDiagram
  participant Buyer App (BAP)
  participant Gateway
  participant Seller App (BPP)
  Buyer App (BAP)->>Seller App (BPP): /search (A to B, peer-to-peer)
  Seller App (BPP)-->>Buyer App (BAP): /on_search (catalog)
  rect rgb(191, 223, 255)
  Buyer App (BAP)->>Seller App (BPP): /init (payment NOT-PAID)
  end
  Seller App (BPP)-->>Buyer App (BAP): /on_init (payment NOT-PAID)
  Buyer App (BAP)->>Seller App (BPP): /confirm (payment PAID)
  Seller App (BPP)-->>Buyer App (BAP): /on_confirm (order.status None)
  Buyer App (BAP)->>Seller App (BPP): /update (update_target order.fulfillments)
  Seller App (BPP)-->>Buyer App (BAP): /on_update (order.status SOFT_UPDATE)
  Buyer App (BAP)->>Seller App (BPP): /update (update_target order.fulfillments)
  Seller App (BPP)-->>Buyer App (BAP): /on_update (order.status UPDATED)
  Buyer App (BAP)->>Seller App (BPP): /update (update_target payments)
  Seller App (BPP)-->>Buyer App (BAP): /on_update (order.status UPDATED)
```

## on_init_without_select_METRO_201

```mermaid
sequenceDiagram
  participant Buyer App (BAP)
  participant Gateway
  participant Seller App (BPP)
  Buyer App (BAP)->>Seller App (BPP): /search (A to B, peer-to-peer)
  Seller App (BPP)-->>Buyer App (BAP): /on_search (catalog)
  Buyer App (BAP)->>Seller App (BPP): /init (payment NOT-PAID)
  rect rgb(191, 223, 255)
  Seller App (BPP)-->>Buyer App (BAP): /on_init (payment NOT-PAID)
  end
  Buyer App (BAP)->>Seller App (BPP): /confirm (payment PAID)
  Seller App (BPP)-->>Buyer App (BAP): /on_confirm (order.status None)
  Buyer App (BAP)->>Seller App (BPP): /update (update_target order.fulfillments)
  Seller App (BPP)-->>Buyer App (BAP): /on_update (order.status SOFT_UPDATE)
  Buyer App (BAP)->>Seller App (BPP): /update (update_target order.fulfillments)
  Seller App (BPP)-->>Buyer App (BAP): /on_update (order.status UPDATED)
  Buyer App (BAP)->>Seller App (BPP): /update (update_target payments)
  Seller App (BPP)-->>Buyer App (BAP): /on_update (order.status UPDATED)
```

## confirm_METRO_201

```mermaid
sequenceDiagram
  participant Buyer App (BAP)
  participant Gateway
  participant Seller App (BPP)
  Buyer App (BAP)->>Seller App (BPP): /search (A to B, peer-to-peer)
  Seller App (BPP)-->>Buyer App (BAP): /on_search (catalog)
  Buyer App (BAP)->>Seller App (BPP): /init (payment NOT-PAID)
  Seller App (BPP)-->>Buyer App (BAP): /on_init (payment NOT-PAID)
  rect rgb(191, 223, 255)
  Buyer App (BAP)->>Seller App (BPP): /confirm (payment PAID)
  end
  Seller App (BPP)-->>Buyer App (BAP): /on_confirm (order.status None)
  Buyer App (BAP)->>Seller App (BPP): /update (update_target order.fulfillments)
  Seller App (BPP)-->>Buyer App (BAP): /on_update (order.status SOFT_UPDATE)
  Buyer App (BAP)->>Seller App (BPP): /update (update_target order.fulfillments)
  Seller App (BPP)-->>Buyer App (BAP): /on_update (order.status UPDATED)
  Buyer App (BAP)->>Seller App (BPP): /update (update_target payments)
  Seller App (BPP)-->>Buyer App (BAP): /on_update (order.status UPDATED)
```

## on_confirm_METRO_201

```mermaid
sequenceDiagram
  participant Buyer App (BAP)
  participant Gateway
  participant Seller App (BPP)
  Buyer App (BAP)->>Seller App (BPP): /search (A to B, peer-to-peer)
  Seller App (BPP)-->>Buyer App (BAP): /on_search (catalog)
  Buyer App (BAP)->>Seller App (BPP): /init (payment NOT-PAID)
  Seller App (BPP)-->>Buyer App (BAP): /on_init (payment NOT-PAID)
  Buyer App (BAP)->>Seller App (BPP): /confirm (payment PAID)
  rect rgb(191, 223, 255)
  Seller App (BPP)-->>Buyer App (BAP): /on_confirm (order.status None)
  end
  Buyer App (BAP)->>Seller App (BPP): /update (update_target order.fulfillments)
  Seller App (BPP)-->>Buyer App (BAP): /on_update (order.status SOFT_UPDATE)
  Buyer App (BAP)->>Seller App (BPP): /update (update_target order.fulfillments)
  Seller App (BPP)-->>Buyer App (BAP): /on_update (order.status UPDATED)
  Buyer App (BAP)->>Seller App (BPP): /update (update_target payments)
  Seller App (BPP)-->>Buyer App (BAP): /on_update (order.status UPDATED)
```

## update_end_stop_1

```mermaid
sequenceDiagram
  participant Buyer App (BAP)
  participant Gateway
  participant Seller App (BPP)
  Buyer App (BAP)->>Seller App (BPP): /search (A to B, peer-to-peer)
  Seller App (BPP)-->>Buyer App (BAP): /on_search (catalog)
  Buyer App (BAP)->>Seller App (BPP): /init (payment NOT-PAID)
  Seller App (BPP)-->>Buyer App (BAP): /on_init (payment NOT-PAID)
  Buyer App (BAP)->>Seller App (BPP): /confirm (payment PAID)
  Seller App (BPP)-->>Buyer App (BAP): /on_confirm (order.status None)
  rect rgb(191, 223, 255)
  Buyer App (BAP)->>Seller App (BPP): /update (update_target order.fulfillments)
  end
  Seller App (BPP)-->>Buyer App (BAP): /on_update (order.status SOFT_UPDATE)
  Buyer App (BAP)->>Seller App (BPP): /update (update_target order.fulfillments)
  Seller App (BPP)-->>Buyer App (BAP): /on_update (order.status UPDATED)
  Buyer App (BAP)->>Seller App (BPP): /update (update_target payments)
  Seller App (BPP)-->>Buyer App (BAP): /on_update (order.status UPDATED)
```

## on_update_end_stop_1

```mermaid
sequenceDiagram
  participant Buyer App (BAP)
  participant Gateway
  participant Seller App (BPP)
  Buyer App (BAP)->>Seller App (BPP): /search (A to B, peer-to-peer)
  Seller App (BPP)-->>Buyer App (BAP): /on_search (catalog)
  Buyer App (BAP)->>Seller App (BPP): /init (payment NOT-PAID)
  Seller App (BPP)-->>Buyer App (BAP): /on_init (payment NOT-PAID)
  Buyer App (BAP)->>Seller App (BPP): /confirm (payment PAID)
  Seller App (BPP)-->>Buyer App (BAP): /on_confirm (order.status None)
  Buyer App (BAP)->>Seller App (BPP): /update (update_target order.fulfillments)
  rect rgb(191, 223, 255)
  Seller App (BPP)-->>Buyer App (BAP): /on_update (order.status SOFT_UPDATE)
  end
  Buyer App (BAP)->>Seller App (BPP): /update (update_target order.fulfillments)
  Seller App (BPP)-->>Buyer App (BAP): /on_update (order.status UPDATED)
  Buyer App (BAP)->>Seller App (BPP): /update (update_target payments)
  Seller App (BPP)-->>Buyer App (BAP): /on_update (order.status UPDATED)
```

## update_end_stop_2

```mermaid
sequenceDiagram
  participant Buyer App (BAP)
  participant Gateway
  participant Seller App (BPP)
  Buyer App (BAP)->>Seller App (BPP): /search (A to B, peer-to-peer)
  Seller App (BPP)-->>Buyer App (BAP): /on_search (catalog)
  Buyer App (BAP)->>Seller App (BPP): /init (payment NOT-PAID)
  Seller App (BPP)-->>Buyer App (BAP): /on_init (payment NOT-PAID)
  Buyer App (BAP)->>Seller App (BPP): /confirm (payment PAID)
  Seller App (BPP)-->>Buyer App (BAP): /on_confirm (order.status None)
  Buyer App (BAP)->>Seller App (BPP): /update (update_target order.fulfillments)
  Seller App (BPP)-->>Buyer App (BAP): /on_update (order.status SOFT_UPDATE)
  rect rgb(191, 223, 255)
  Buyer App (BAP)->>Seller App (BPP): /update (update_target order.fulfillments)
  end
  Seller App (BPP)-->>Buyer App (BAP): /on_update (order.status UPDATED)
  Buyer App (BAP)->>Seller App (BPP): /update (update_target payments)
  Seller App (BPP)-->>Buyer App (BAP): /on_update (order.status UPDATED)
```

## on_update_end_stop_2

```mermaid
sequenceDiagram
  participant Buyer App (BAP)
  participant Gateway
  participant Seller App (BPP)
  Buyer App (BAP)->>Seller App (BPP): /search (A to B, peer-to-peer)
  Seller App (BPP)-->>Buyer App (BAP): /on_search (catalog)
  Buyer App (BAP)->>Seller App (BPP): /init (payment NOT-PAID)
  Seller App (BPP)-->>Buyer App (BAP): /on_init (payment NOT-PAID)
  Buyer App (BAP)->>Seller App (BPP): /confirm (payment PAID)
  Seller App (BPP)-->>Buyer App (BAP): /on_confirm (order.status None)
  Buyer App (BAP)->>Seller App (BPP): /update (update_target order.fulfillments)
  Seller App (BPP)-->>Buyer App (BAP): /on_update (order.status SOFT_UPDATE)
  Buyer App (BAP)->>Seller App (BPP): /update (update_target order.fulfillments)
  rect rgb(191, 223, 255)
  Seller App (BPP)-->>Buyer App (BAP): /on_update (order.status UPDATED)
  end
  Buyer App (BAP)->>Seller App (BPP): /update (update_target payments)
  Seller App (BPP)-->>Buyer App (BAP): /on_update (order.status UPDATED)
```

## update_end_stop_3

```mermaid
sequenceDiagram
  participant Buyer App (BAP)
  participant Gateway
  participant Seller App (BPP)
  Buyer App (BAP)->>Seller App (BPP): /search (A to B, peer-to-peer)
  Seller App (BPP)-->>Buyer App (BAP): /on_search (catalog)
  Buyer App (BAP)->>Seller App (BPP): /init (payment NOT-PAID)
  Seller App (BPP)-->>Buyer App (BAP): /on_init (payment NOT-PAID)
  Buyer App (BAP)->>Seller App (BPP): /confirm (payment PAID)
  Seller App (BPP)-->>Buyer App (BAP): /on_confirm (order.status None)
  Buyer App (BAP)->>Seller App (BPP): /update (update_target order.fulfillments)
  Seller App (BPP)-->>Buyer App (BAP): /on_update (order.status SOFT_UPDATE)
  Buyer App (BAP)->>Seller App (BPP): /update (update_target order.fulfillments)
  Seller App (BPP)-->>Buyer App (BAP): /on_update (order.status UPDATED)
  rect rgb(191, 223, 255)
  Buyer App (BAP)->>Seller App (BPP): /update (update_target payments)
  end
  Seller App (BPP)-->>Buyer App (BAP): /on_update (order.status UPDATED)
```

## on_update_end_stop_3

```mermaid
sequenceDiagram
  participant Buyer App (BAP)
  participant Gateway
  participant Seller App (BPP)
  Buyer App (BAP)->>Seller App (BPP): /search (A to B, peer-to-peer)
  Seller App (BPP)-->>Buyer App (BAP): /on_search (catalog)
  Buyer App (BAP)->>Seller App (BPP): /init (payment NOT-PAID)
  Seller App (BPP)-->>Buyer App (BAP): /on_init (payment NOT-PAID)
  Buyer App (BAP)->>Seller App (BPP): /confirm (payment PAID)
  Seller App (BPP)-->>Buyer App (BAP): /on_confirm (order.status None)
  Buyer App (BAP)->>Seller App (BPP): /update (update_target order.fulfillments)
  Seller App (BPP)-->>Buyer App (BAP): /on_update (order.status SOFT_UPDATE)
  Buyer App (BAP)->>Seller App (BPP): /update (update_target order.fulfillments)
  Seller App (BPP)-->>Buyer App (BAP): /on_update (order.status UPDATED)
  Buyer App (BAP)->>Seller App (BPP): /update (update_target payments)
  rect rgb(191, 223, 255)
  Seller App (BPP)-->>Buyer App (BAP): /on_update (order.status UPDATED)
  end
```

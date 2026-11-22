# PARTIAL_CANCELLATION_FLOW (W/O search_1 & select) — Sequence Diagrams

Internal data file consumed by the Developer Guide's "Sequence Diagram" tab (API Walkthrough).
Not meant to be shown as its own docs page — the frontend filters this slug out of the Use Case
Brief / Additional Resources / Changelog tab lists and instead looks up the section matching the
selected API call's `action_id` (the `##` heading below) to render that step's diagram.

One `## <action_id>` heading per step of `PARTIAL_CANCELLATION_FLOW_WITHOUT_SEARCH_ND_SELECT.yaml` (Metro), in that flow's own step order, each followed by its Mermaid `sequenceDiagram`: the whole flow, with that call's own message(s) highlighted — same convention as the other domains' per-step sequence-diagram docs.

## search2_METRO_200

```mermaid
sequenceDiagram
  participant Buyer App (BAP)
  participant Gateway
  participant Seller App (BPP)
  rect rgb(191, 223, 255)
  Buyer App (BAP)->>Seller App (BPP): /search (A to B, peer-to-peer)
  end
  Seller App (BPP)-->>Buyer App (BAP): /on_search (items SJT)
  Buyer App (BAP)->>Seller App (BPP): /init (payment NOT-PAID)
  Seller App (BPP)-->>Buyer App (BAP): /on_init (payment NOT-PAID)
  Buyer App (BAP)->>Seller App (BPP): /confirm (payment PAID)
  Seller App (BPP)-->>Buyer App (BAP): /on_confirm (order.status ACTIVE)
  Buyer App (BAP)->>Seller App (BPP): /update (update_target order.fulfillments)
  Seller App (BPP)-->>Buyer App (BAP): /on_update (order.status SOFT_CANCEL)
  Buyer App (BAP)->>Seller App (BPP): /update (update_target order.fulfillments)
  Seller App (BPP)-->>Buyer App (BAP): /on_update (order.status ACTIVE)
```

## on_search2_Sjt_METRO_200

```mermaid
sequenceDiagram
  participant Buyer App (BAP)
  participant Gateway
  participant Seller App (BPP)
  Buyer App (BAP)->>Seller App (BPP): /search (A to B, peer-to-peer)
  rect rgb(191, 223, 255)
  Seller App (BPP)-->>Buyer App (BAP): /on_search (items SJT)
  end
  Buyer App (BAP)->>Seller App (BPP): /init (payment NOT-PAID)
  Seller App (BPP)-->>Buyer App (BAP): /on_init (payment NOT-PAID)
  Buyer App (BAP)->>Seller App (BPP): /confirm (payment PAID)
  Seller App (BPP)-->>Buyer App (BAP): /on_confirm (order.status ACTIVE)
  Buyer App (BAP)->>Seller App (BPP): /update (update_target order.fulfillments)
  Seller App (BPP)-->>Buyer App (BAP): /on_update (order.status SOFT_CANCEL)
  Buyer App (BAP)->>Seller App (BPP): /update (update_target order.fulfillments)
  Seller App (BPP)-->>Buyer App (BAP): /on_update (order.status ACTIVE)
```

## init_with_user_input_METRO_200

```mermaid
sequenceDiagram
  participant Buyer App (BAP)
  participant Gateway
  participant Seller App (BPP)
  Buyer App (BAP)->>Seller App (BPP): /search (A to B, peer-to-peer)
  Seller App (BPP)-->>Buyer App (BAP): /on_search (items SJT)
  rect rgb(191, 223, 255)
  Buyer App (BAP)->>Seller App (BPP): /init (payment NOT-PAID)
  end
  Seller App (BPP)-->>Buyer App (BAP): /on_init (payment NOT-PAID)
  Buyer App (BAP)->>Seller App (BPP): /confirm (payment PAID)
  Seller App (BPP)-->>Buyer App (BAP): /on_confirm (order.status ACTIVE)
  Buyer App (BAP)->>Seller App (BPP): /update (update_target order.fulfillments)
  Seller App (BPP)-->>Buyer App (BAP): /on_update (order.status SOFT_CANCEL)
  Buyer App (BAP)->>Seller App (BPP): /update (update_target order.fulfillments)
  Seller App (BPP)-->>Buyer App (BAP): /on_update (order.status ACTIVE)
```

## on_init_METRO_200

```mermaid
sequenceDiagram
  participant Buyer App (BAP)
  participant Gateway
  participant Seller App (BPP)
  Buyer App (BAP)->>Seller App (BPP): /search (A to B, peer-to-peer)
  Seller App (BPP)-->>Buyer App (BAP): /on_search (items SJT)
  Buyer App (BAP)->>Seller App (BPP): /init (payment NOT-PAID)
  rect rgb(191, 223, 255)
  Seller App (BPP)-->>Buyer App (BAP): /on_init (payment NOT-PAID)
  end
  Buyer App (BAP)->>Seller App (BPP): /confirm (payment PAID)
  Seller App (BPP)-->>Buyer App (BAP): /on_confirm (order.status ACTIVE)
  Buyer App (BAP)->>Seller App (BPP): /update (update_target order.fulfillments)
  Seller App (BPP)-->>Buyer App (BAP): /on_update (order.status SOFT_CANCEL)
  Buyer App (BAP)->>Seller App (BPP): /update (update_target order.fulfillments)
  Seller App (BPP)-->>Buyer App (BAP): /on_update (order.status ACTIVE)
```

## confirm_METRO_200

```mermaid
sequenceDiagram
  participant Buyer App (BAP)
  participant Gateway
  participant Seller App (BPP)
  Buyer App (BAP)->>Seller App (BPP): /search (A to B, peer-to-peer)
  Seller App (BPP)-->>Buyer App (BAP): /on_search (items SJT)
  Buyer App (BAP)->>Seller App (BPP): /init (payment NOT-PAID)
  Seller App (BPP)-->>Buyer App (BAP): /on_init (payment NOT-PAID)
  rect rgb(191, 223, 255)
  Buyer App (BAP)->>Seller App (BPP): /confirm (payment PAID)
  end
  Seller App (BPP)-->>Buyer App (BAP): /on_confirm (order.status ACTIVE)
  Buyer App (BAP)->>Seller App (BPP): /update (update_target order.fulfillments)
  Seller App (BPP)-->>Buyer App (BAP): /on_update (order.status SOFT_CANCEL)
  Buyer App (BAP)->>Seller App (BPP): /update (update_target order.fulfillments)
  Seller App (BPP)-->>Buyer App (BAP): /on_update (order.status ACTIVE)
```

## on_confirm_METRO_200

```mermaid
sequenceDiagram
  participant Buyer App (BAP)
  participant Gateway
  participant Seller App (BPP)
  Buyer App (BAP)->>Seller App (BPP): /search (A to B, peer-to-peer)
  Seller App (BPP)-->>Buyer App (BAP): /on_search (items SJT)
  Buyer App (BAP)->>Seller App (BPP): /init (payment NOT-PAID)
  Seller App (BPP)-->>Buyer App (BAP): /on_init (payment NOT-PAID)
  Buyer App (BAP)->>Seller App (BPP): /confirm (payment PAID)
  rect rgb(191, 223, 255)
  Seller App (BPP)-->>Buyer App (BAP): /on_confirm (order.status ACTIVE)
  end
  Buyer App (BAP)->>Seller App (BPP): /update (update_target order.fulfillments)
  Seller App (BPP)-->>Buyer App (BAP): /on_update (order.status SOFT_CANCEL)
  Buyer App (BAP)->>Seller App (BPP): /update (update_target order.fulfillments)
  Seller App (BPP)-->>Buyer App (BAP): /on_update (order.status ACTIVE)
```

## update_METRO_201

```mermaid
sequenceDiagram
  participant Buyer App (BAP)
  participant Gateway
  participant Seller App (BPP)
  Buyer App (BAP)->>Seller App (BPP): /search (A to B, peer-to-peer)
  Seller App (BPP)-->>Buyer App (BAP): /on_search (items SJT)
  Buyer App (BAP)->>Seller App (BPP): /init (payment NOT-PAID)
  Seller App (BPP)-->>Buyer App (BAP): /on_init (payment NOT-PAID)
  Buyer App (BAP)->>Seller App (BPP): /confirm (payment PAID)
  Seller App (BPP)-->>Buyer App (BAP): /on_confirm (order.status ACTIVE)
  rect rgb(191, 223, 255)
  Buyer App (BAP)->>Seller App (BPP): /update (update_target order.fulfillments)
  end
  Seller App (BPP)-->>Buyer App (BAP): /on_update (order.status SOFT_CANCEL)
  Buyer App (BAP)->>Seller App (BPP): /update (update_target order.fulfillments)
  Seller App (BPP)-->>Buyer App (BAP): /on_update (order.status ACTIVE)
```

## on_update_METRO_201

```mermaid
sequenceDiagram
  participant Buyer App (BAP)
  participant Gateway
  participant Seller App (BPP)
  Buyer App (BAP)->>Seller App (BPP): /search (A to B, peer-to-peer)
  Seller App (BPP)-->>Buyer App (BAP): /on_search (items SJT)
  Buyer App (BAP)->>Seller App (BPP): /init (payment NOT-PAID)
  Seller App (BPP)-->>Buyer App (BAP): /on_init (payment NOT-PAID)
  Buyer App (BAP)->>Seller App (BPP): /confirm (payment PAID)
  Seller App (BPP)-->>Buyer App (BAP): /on_confirm (order.status ACTIVE)
  Buyer App (BAP)->>Seller App (BPP): /update (update_target order.fulfillments)
  rect rgb(191, 223, 255)
  Seller App (BPP)-->>Buyer App (BAP): /on_update (order.status SOFT_CANCEL)
  end
  Buyer App (BAP)->>Seller App (BPP): /update (update_target order.fulfillments)
  Seller App (BPP)-->>Buyer App (BAP): /on_update (order.status ACTIVE)
```

## update_METRO_202

```mermaid
sequenceDiagram
  participant Buyer App (BAP)
  participant Gateway
  participant Seller App (BPP)
  Buyer App (BAP)->>Seller App (BPP): /search (A to B, peer-to-peer)
  Seller App (BPP)-->>Buyer App (BAP): /on_search (items SJT)
  Buyer App (BAP)->>Seller App (BPP): /init (payment NOT-PAID)
  Seller App (BPP)-->>Buyer App (BAP): /on_init (payment NOT-PAID)
  Buyer App (BAP)->>Seller App (BPP): /confirm (payment PAID)
  Seller App (BPP)-->>Buyer App (BAP): /on_confirm (order.status ACTIVE)
  Buyer App (BAP)->>Seller App (BPP): /update (update_target order.fulfillments)
  Seller App (BPP)-->>Buyer App (BAP): /on_update (order.status SOFT_CANCEL)
  rect rgb(191, 223, 255)
  Buyer App (BAP)->>Seller App (BPP): /update (update_target order.fulfillments)
  end
  Seller App (BPP)-->>Buyer App (BAP): /on_update (order.status ACTIVE)
```

## on_update_METRO_202

```mermaid
sequenceDiagram
  participant Buyer App (BAP)
  participant Gateway
  participant Seller App (BPP)
  Buyer App (BAP)->>Seller App (BPP): /search (A to B, peer-to-peer)
  Seller App (BPP)-->>Buyer App (BAP): /on_search (items SJT)
  Buyer App (BAP)->>Seller App (BPP): /init (payment NOT-PAID)
  Seller App (BPP)-->>Buyer App (BAP): /on_init (payment NOT-PAID)
  Buyer App (BAP)->>Seller App (BPP): /confirm (payment PAID)
  Seller App (BPP)-->>Buyer App (BAP): /on_confirm (order.status ACTIVE)
  Buyer App (BAP)->>Seller App (BPP): /update (update_target order.fulfillments)
  Seller App (BPP)-->>Buyer App (BAP): /on_update (order.status SOFT_CANCEL)
  Buyer App (BAP)->>Seller App (BPP): /update (update_target order.fulfillments)
  rect rgb(191, 223, 255)
  Seller App (BPP)-->>Buyer App (BAP): /on_update (order.status ACTIVE)
  end
```

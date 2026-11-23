# IntraCity_User_Cancellation_Flow — Sequence Diagrams

Internal data file consumed by the Developer Guide's "Sequence Diagram" tab (API Walkthrough).
Not meant to be shown as its own docs page — the frontend filters this slug out of the Use Case
Brief / Additional Resources / Changelog tab lists and instead looks up the section matching the
selected API call's `action_id` (the `##` heading below) to render that step's diagram.

One `## <action_id>` heading per step of `IntraCity_User_Cancellation_Flow.yaml` (Bus), in that flow's own step order, each followed by its Mermaid `sequenceDiagram`: the whole flow, with that call's own message(s) highlighted — same convention as the other domains' per-step sequence-diagram docs.

## search_1

```mermaid
sequenceDiagram
  participant Buyer App (BAP)
  participant Gateway
  participant Seller App (BPP)
  rect rgb(191, 223, 255)
  Buyer App (BAP)->>Seller App (BPP): /search (A to B, peer-to-peer)
  end
  Seller App (BPP)-->>Buyer App (BAP): /on_search (items SJT, SFSJT, PASS)
  Buyer App (BAP)->>Seller App (BPP): /select (item I1 x 2)
  Seller App (BPP)-->>Buyer App (BAP): /on_select (quote)
  Buyer App (BAP)->>Seller App (BPP): /init (payment NOT-PAID)
  Seller App (BPP)-->>Buyer App (BAP): /on_init (payment NOT-PAID)
  Buyer App (BAP)->>Seller App (BPP): /confirm (payment PAID)
  Seller App (BPP)-->>Buyer App (BAP): /on_confirm (order.status ACTIVE)
  Buyer App (BAP)->>Seller App (BPP): /cancel (descriptor SOFT_CANCEL, reason 7)
  Seller App (BPP)-->>Buyer App (BAP): /on_cancel (order.status SOFT_CANCEL, cancelled_by CONSUMER)
  Buyer App (BAP)->>Seller App (BPP): /cancel (descriptor CONFIRM_CANCEL, reason 7)
  Seller App (BPP)-->>Buyer App (BAP): /on_cancel (order.status CANCELLED, cancelled_by CONSUMER)
```

## on_search_1

```mermaid
sequenceDiagram
  participant Buyer App (BAP)
  participant Gateway
  participant Seller App (BPP)
  Buyer App (BAP)->>Seller App (BPP): /search (A to B, peer-to-peer)
  rect rgb(191, 223, 255)
  Seller App (BPP)-->>Buyer App (BAP): /on_search (items SJT, SFSJT, PASS)
  end
  Buyer App (BAP)->>Seller App (BPP): /select (item I1 x 2)
  Seller App (BPP)-->>Buyer App (BAP): /on_select (quote)
  Buyer App (BAP)->>Seller App (BPP): /init (payment NOT-PAID)
  Seller App (BPP)-->>Buyer App (BAP): /on_init (payment NOT-PAID)
  Buyer App (BAP)->>Seller App (BPP): /confirm (payment PAID)
  Seller App (BPP)-->>Buyer App (BAP): /on_confirm (order.status ACTIVE)
  Buyer App (BAP)->>Seller App (BPP): /cancel (descriptor SOFT_CANCEL, reason 7)
  Seller App (BPP)-->>Buyer App (BAP): /on_cancel (order.status SOFT_CANCEL, cancelled_by CONSUMER)
  Buyer App (BAP)->>Seller App (BPP): /cancel (descriptor CONFIRM_CANCEL, reason 7)
  Seller App (BPP)-->>Buyer App (BAP): /on_cancel (order.status CANCELLED, cancelled_by CONSUMER)
```

## select_1

```mermaid
sequenceDiagram
  participant Buyer App (BAP)
  participant Gateway
  participant Seller App (BPP)
  Buyer App (BAP)->>Seller App (BPP): /search (A to B, peer-to-peer)
  Seller App (BPP)-->>Buyer App (BAP): /on_search (items SJT, SFSJT, PASS)
  rect rgb(191, 223, 255)
  Buyer App (BAP)->>Seller App (BPP): /select (item I1 x 2)
  end
  Seller App (BPP)-->>Buyer App (BAP): /on_select (quote)
  Buyer App (BAP)->>Seller App (BPP): /init (payment NOT-PAID)
  Seller App (BPP)-->>Buyer App (BAP): /on_init (payment NOT-PAID)
  Buyer App (BAP)->>Seller App (BPP): /confirm (payment PAID)
  Seller App (BPP)-->>Buyer App (BAP): /on_confirm (order.status ACTIVE)
  Buyer App (BAP)->>Seller App (BPP): /cancel (descriptor SOFT_CANCEL, reason 7)
  Seller App (BPP)-->>Buyer App (BAP): /on_cancel (order.status SOFT_CANCEL, cancelled_by CONSUMER)
  Buyer App (BAP)->>Seller App (BPP): /cancel (descriptor CONFIRM_CANCEL, reason 7)
  Seller App (BPP)-->>Buyer App (BAP): /on_cancel (order.status CANCELLED, cancelled_by CONSUMER)
```

## on_select_1

```mermaid
sequenceDiagram
  participant Buyer App (BAP)
  participant Gateway
  participant Seller App (BPP)
  Buyer App (BAP)->>Seller App (BPP): /search (A to B, peer-to-peer)
  Seller App (BPP)-->>Buyer App (BAP): /on_search (items SJT, SFSJT, PASS)
  Buyer App (BAP)->>Seller App (BPP): /select (item I1 x 2)
  rect rgb(191, 223, 255)
  Seller App (BPP)-->>Buyer App (BAP): /on_select (quote)
  end
  Buyer App (BAP)->>Seller App (BPP): /init (payment NOT-PAID)
  Seller App (BPP)-->>Buyer App (BAP): /on_init (payment NOT-PAID)
  Buyer App (BAP)->>Seller App (BPP): /confirm (payment PAID)
  Seller App (BPP)-->>Buyer App (BAP): /on_confirm (order.status ACTIVE)
  Buyer App (BAP)->>Seller App (BPP): /cancel (descriptor SOFT_CANCEL, reason 7)
  Seller App (BPP)-->>Buyer App (BAP): /on_cancel (order.status SOFT_CANCEL, cancelled_by CONSUMER)
  Buyer App (BAP)->>Seller App (BPP): /cancel (descriptor CONFIRM_CANCEL, reason 7)
  Seller App (BPP)-->>Buyer App (BAP): /on_cancel (order.status CANCELLED, cancelled_by CONSUMER)
```

## init_1

```mermaid
sequenceDiagram
  participant Buyer App (BAP)
  participant Gateway
  participant Seller App (BPP)
  Buyer App (BAP)->>Seller App (BPP): /search (A to B, peer-to-peer)
  Seller App (BPP)-->>Buyer App (BAP): /on_search (items SJT, SFSJT, PASS)
  Buyer App (BAP)->>Seller App (BPP): /select (item I1 x 2)
  Seller App (BPP)-->>Buyer App (BAP): /on_select (quote)
  rect rgb(191, 223, 255)
  Buyer App (BAP)->>Seller App (BPP): /init (payment NOT-PAID)
  end
  Seller App (BPP)-->>Buyer App (BAP): /on_init (payment NOT-PAID)
  Buyer App (BAP)->>Seller App (BPP): /confirm (payment PAID)
  Seller App (BPP)-->>Buyer App (BAP): /on_confirm (order.status ACTIVE)
  Buyer App (BAP)->>Seller App (BPP): /cancel (descriptor SOFT_CANCEL, reason 7)
  Seller App (BPP)-->>Buyer App (BAP): /on_cancel (order.status SOFT_CANCEL, cancelled_by CONSUMER)
  Buyer App (BAP)->>Seller App (BPP): /cancel (descriptor CONFIRM_CANCEL, reason 7)
  Seller App (BPP)-->>Buyer App (BAP): /on_cancel (order.status CANCELLED, cancelled_by CONSUMER)
```

## on_init_1

```mermaid
sequenceDiagram
  participant Buyer App (BAP)
  participant Gateway
  participant Seller App (BPP)
  Buyer App (BAP)->>Seller App (BPP): /search (A to B, peer-to-peer)
  Seller App (BPP)-->>Buyer App (BAP): /on_search (items SJT, SFSJT, PASS)
  Buyer App (BAP)->>Seller App (BPP): /select (item I1 x 2)
  Seller App (BPP)-->>Buyer App (BAP): /on_select (quote)
  Buyer App (BAP)->>Seller App (BPP): /init (payment NOT-PAID)
  rect rgb(191, 223, 255)
  Seller App (BPP)-->>Buyer App (BAP): /on_init (payment NOT-PAID)
  end
  Buyer App (BAP)->>Seller App (BPP): /confirm (payment PAID)
  Seller App (BPP)-->>Buyer App (BAP): /on_confirm (order.status ACTIVE)
  Buyer App (BAP)->>Seller App (BPP): /cancel (descriptor SOFT_CANCEL, reason 7)
  Seller App (BPP)-->>Buyer App (BAP): /on_cancel (order.status SOFT_CANCEL, cancelled_by CONSUMER)
  Buyer App (BAP)->>Seller App (BPP): /cancel (descriptor CONFIRM_CANCEL, reason 7)
  Seller App (BPP)-->>Buyer App (BAP): /on_cancel (order.status CANCELLED, cancelled_by CONSUMER)
```

## confirm_1

```mermaid
sequenceDiagram
  participant Buyer App (BAP)
  participant Gateway
  participant Seller App (BPP)
  Buyer App (BAP)->>Seller App (BPP): /search (A to B, peer-to-peer)
  Seller App (BPP)-->>Buyer App (BAP): /on_search (items SJT, SFSJT, PASS)
  Buyer App (BAP)->>Seller App (BPP): /select (item I1 x 2)
  Seller App (BPP)-->>Buyer App (BAP): /on_select (quote)
  Buyer App (BAP)->>Seller App (BPP): /init (payment NOT-PAID)
  Seller App (BPP)-->>Buyer App (BAP): /on_init (payment NOT-PAID)
  rect rgb(191, 223, 255)
  Buyer App (BAP)->>Seller App (BPP): /confirm (payment PAID)
  end
  Seller App (BPP)-->>Buyer App (BAP): /on_confirm (order.status ACTIVE)
  Buyer App (BAP)->>Seller App (BPP): /cancel (descriptor SOFT_CANCEL, reason 7)
  Seller App (BPP)-->>Buyer App (BAP): /on_cancel (order.status SOFT_CANCEL, cancelled_by CONSUMER)
  Buyer App (BAP)->>Seller App (BPP): /cancel (descriptor CONFIRM_CANCEL, reason 7)
  Seller App (BPP)-->>Buyer App (BAP): /on_cancel (order.status CANCELLED, cancelled_by CONSUMER)
```

## on_confirm_1

```mermaid
sequenceDiagram
  participant Buyer App (BAP)
  participant Gateway
  participant Seller App (BPP)
  Buyer App (BAP)->>Seller App (BPP): /search (A to B, peer-to-peer)
  Seller App (BPP)-->>Buyer App (BAP): /on_search (items SJT, SFSJT, PASS)
  Buyer App (BAP)->>Seller App (BPP): /select (item I1 x 2)
  Seller App (BPP)-->>Buyer App (BAP): /on_select (quote)
  Buyer App (BAP)->>Seller App (BPP): /init (payment NOT-PAID)
  Seller App (BPP)-->>Buyer App (BAP): /on_init (payment NOT-PAID)
  Buyer App (BAP)->>Seller App (BPP): /confirm (payment PAID)
  rect rgb(191, 223, 255)
  Seller App (BPP)-->>Buyer App (BAP): /on_confirm (order.status ACTIVE)
  end
  Buyer App (BAP)->>Seller App (BPP): /cancel (descriptor SOFT_CANCEL, reason 7)
  Seller App (BPP)-->>Buyer App (BAP): /on_cancel (order.status SOFT_CANCEL, cancelled_by CONSUMER)
  Buyer App (BAP)->>Seller App (BPP): /cancel (descriptor CONFIRM_CANCEL, reason 7)
  Seller App (BPP)-->>Buyer App (BAP): /on_cancel (order.status CANCELLED, cancelled_by CONSUMER)
```

## cancel_1

```mermaid
sequenceDiagram
  participant Buyer App (BAP)
  participant Gateway
  participant Seller App (BPP)
  Buyer App (BAP)->>Seller App (BPP): /search (A to B, peer-to-peer)
  Seller App (BPP)-->>Buyer App (BAP): /on_search (items SJT, SFSJT, PASS)
  Buyer App (BAP)->>Seller App (BPP): /select (item I1 x 2)
  Seller App (BPP)-->>Buyer App (BAP): /on_select (quote)
  Buyer App (BAP)->>Seller App (BPP): /init (payment NOT-PAID)
  Seller App (BPP)-->>Buyer App (BAP): /on_init (payment NOT-PAID)
  Buyer App (BAP)->>Seller App (BPP): /confirm (payment PAID)
  Seller App (BPP)-->>Buyer App (BAP): /on_confirm (order.status ACTIVE)
  rect rgb(191, 223, 255)
  Buyer App (BAP)->>Seller App (BPP): /cancel (descriptor SOFT_CANCEL, reason 7)
  end
  Seller App (BPP)-->>Buyer App (BAP): /on_cancel (order.status SOFT_CANCEL, cancelled_by CONSUMER)
  Buyer App (BAP)->>Seller App (BPP): /cancel (descriptor CONFIRM_CANCEL, reason 7)
  Seller App (BPP)-->>Buyer App (BAP): /on_cancel (order.status CANCELLED, cancelled_by CONSUMER)
```

## on_cancel_1

```mermaid
sequenceDiagram
  participant Buyer App (BAP)
  participant Gateway
  participant Seller App (BPP)
  Buyer App (BAP)->>Seller App (BPP): /search (A to B, peer-to-peer)
  Seller App (BPP)-->>Buyer App (BAP): /on_search (items SJT, SFSJT, PASS)
  Buyer App (BAP)->>Seller App (BPP): /select (item I1 x 2)
  Seller App (BPP)-->>Buyer App (BAP): /on_select (quote)
  Buyer App (BAP)->>Seller App (BPP): /init (payment NOT-PAID)
  Seller App (BPP)-->>Buyer App (BAP): /on_init (payment NOT-PAID)
  Buyer App (BAP)->>Seller App (BPP): /confirm (payment PAID)
  Seller App (BPP)-->>Buyer App (BAP): /on_confirm (order.status ACTIVE)
  Buyer App (BAP)->>Seller App (BPP): /cancel (descriptor SOFT_CANCEL, reason 7)
  rect rgb(191, 223, 255)
  Seller App (BPP)-->>Buyer App (BAP): /on_cancel (order.status SOFT_CANCEL, cancelled_by CONSUMER)
  end
  Buyer App (BAP)->>Seller App (BPP): /cancel (descriptor CONFIRM_CANCEL, reason 7)
  Seller App (BPP)-->>Buyer App (BAP): /on_cancel (order.status CANCELLED, cancelled_by CONSUMER)
```

## cancel_2

```mermaid
sequenceDiagram
  participant Buyer App (BAP)
  participant Gateway
  participant Seller App (BPP)
  Buyer App (BAP)->>Seller App (BPP): /search (A to B, peer-to-peer)
  Seller App (BPP)-->>Buyer App (BAP): /on_search (items SJT, SFSJT, PASS)
  Buyer App (BAP)->>Seller App (BPP): /select (item I1 x 2)
  Seller App (BPP)-->>Buyer App (BAP): /on_select (quote)
  Buyer App (BAP)->>Seller App (BPP): /init (payment NOT-PAID)
  Seller App (BPP)-->>Buyer App (BAP): /on_init (payment NOT-PAID)
  Buyer App (BAP)->>Seller App (BPP): /confirm (payment PAID)
  Seller App (BPP)-->>Buyer App (BAP): /on_confirm (order.status ACTIVE)
  Buyer App (BAP)->>Seller App (BPP): /cancel (descriptor SOFT_CANCEL, reason 7)
  Seller App (BPP)-->>Buyer App (BAP): /on_cancel (order.status SOFT_CANCEL, cancelled_by CONSUMER)
  rect rgb(191, 223, 255)
  Buyer App (BAP)->>Seller App (BPP): /cancel (descriptor CONFIRM_CANCEL, reason 7)
  end
  Seller App (BPP)-->>Buyer App (BAP): /on_cancel (order.status CANCELLED, cancelled_by CONSUMER)
```

## on_cancel_2

```mermaid
sequenceDiagram
  participant Buyer App (BAP)
  participant Gateway
  participant Seller App (BPP)
  Buyer App (BAP)->>Seller App (BPP): /search (A to B, peer-to-peer)
  Seller App (BPP)-->>Buyer App (BAP): /on_search (items SJT, SFSJT, PASS)
  Buyer App (BAP)->>Seller App (BPP): /select (item I1 x 2)
  Seller App (BPP)-->>Buyer App (BAP): /on_select (quote)
  Buyer App (BAP)->>Seller App (BPP): /init (payment NOT-PAID)
  Seller App (BPP)-->>Buyer App (BAP): /on_init (payment NOT-PAID)
  Buyer App (BAP)->>Seller App (BPP): /confirm (payment PAID)
  Seller App (BPP)-->>Buyer App (BAP): /on_confirm (order.status ACTIVE)
  Buyer App (BAP)->>Seller App (BPP): /cancel (descriptor SOFT_CANCEL, reason 7)
  Seller App (BPP)-->>Buyer App (BAP): /on_cancel (order.status SOFT_CANCEL, cancelled_by CONSUMER)
  Buyer App (BAP)->>Seller App (BPP): /cancel (descriptor CONFIRM_CANCEL, reason 7)
  rect rgb(191, 223, 255)
  Seller App (BPP)-->>Buyer App (BAP): /on_cancel (order.status CANCELLED, cancelled_by CONSUMER)
  end
```

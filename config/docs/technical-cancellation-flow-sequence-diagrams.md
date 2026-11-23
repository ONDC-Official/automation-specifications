# TECHNICAL_CANCELLATION_FLOW — Sequence Diagrams

Internal data file consumed by the Developer Guide's "Sequence Diagram" tab (API Walkthrough).
Not meant to be shown as its own docs page — the frontend filters this slug out of the Use Case
Brief / Additional Resources / Changelog tab lists and instead looks up the section matching the
selected API call's `action_id` (the `##` heading below) to render that step's diagram.

One `## <action_id>` heading per step of `TECHNICAL_CANCELLATION_FLOW.yaml` (Metro), in that flow's own step order, each followed by its Mermaid `sequenceDiagram`: the whole flow, with that call's own message(s) highlighted — same convention as the other domains' per-step sequence-diagram docs.

## search2_METRO_210

```mermaid
sequenceDiagram
  participant Buyer App (BAP)
  participant Gateway
  participant Seller App (BPP)
  rect rgb(191, 223, 255)
  Buyer App (BAP)->>Seller App (BPP): /search (A to B, peer-to-peer)
  end
  Seller App (BPP)-->>Buyer App (BAP): /on_search (items SJT, RJT)
  Buyer App (BAP)->>Seller App (BPP): /select (item I1 x 1)
  Seller App (BPP)-->>Buyer App (BAP): /on_select (quote)
  Buyer App (BAP)->>Seller App (BPP): /init (payment NOT-PAID)
  Seller App (BPP)-->>Buyer App (BAP): /on_init (payment NOT-PAID)
  Buyer App (BAP)->>Seller App (BPP): /confirm (payment PAID)
  Seller App (BPP)-->>Buyer App (BAP): /on_confirm (order.status ACTIVE; TICKET ACTIVE)
  Buyer App (BAP)->>Seller App (BPP): /status
  Seller App (BPP)-->>Buyer App (BAP): /on_status (order.status ACTIVE; TICKET ACTIVE)
  Buyer App (BAP)->>Seller App (BPP): /cancel (descriptor SOFT_CANCEL, reason 000)
  Seller App (BPP)-->>Buyer App (BAP): /on_cancel (order.status SOFT_CANCEL; TICKET ACTIVE, cancelled_by CONSUMER)
  Buyer App (BAP)->>Seller App (BPP): /cancel (descriptor CONFIRM_CANCEL, reason 000)
  Seller App (BPP)-->>Buyer App (BAP): /on_cancel (order.status CANCELLED; TICKET ACTIVE, cancelled_by CONSUMER)
```

## on_search2_METRO_210

```mermaid
sequenceDiagram
  participant Buyer App (BAP)
  participant Gateway
  participant Seller App (BPP)
  Buyer App (BAP)->>Seller App (BPP): /search (A to B, peer-to-peer)
  rect rgb(191, 223, 255)
  Seller App (BPP)-->>Buyer App (BAP): /on_search (items SJT, RJT)
  end
  Buyer App (BAP)->>Seller App (BPP): /select (item I1 x 1)
  Seller App (BPP)-->>Buyer App (BAP): /on_select (quote)
  Buyer App (BAP)->>Seller App (BPP): /init (payment NOT-PAID)
  Seller App (BPP)-->>Buyer App (BAP): /on_init (payment NOT-PAID)
  Buyer App (BAP)->>Seller App (BPP): /confirm (payment PAID)
  Seller App (BPP)-->>Buyer App (BAP): /on_confirm (order.status ACTIVE; TICKET ACTIVE)
  Buyer App (BAP)->>Seller App (BPP): /status
  Seller App (BPP)-->>Buyer App (BAP): /on_status (order.status ACTIVE; TICKET ACTIVE)
  Buyer App (BAP)->>Seller App (BPP): /cancel (descriptor SOFT_CANCEL, reason 000)
  Seller App (BPP)-->>Buyer App (BAP): /on_cancel (order.status SOFT_CANCEL; TICKET ACTIVE, cancelled_by CONSUMER)
  Buyer App (BAP)->>Seller App (BPP): /cancel (descriptor CONFIRM_CANCEL, reason 000)
  Seller App (BPP)-->>Buyer App (BAP): /on_cancel (order.status CANCELLED; TICKET ACTIVE, cancelled_by CONSUMER)
```

## select_METRO_210

```mermaid
sequenceDiagram
  participant Buyer App (BAP)
  participant Gateway
  participant Seller App (BPP)
  Buyer App (BAP)->>Seller App (BPP): /search (A to B, peer-to-peer)
  Seller App (BPP)-->>Buyer App (BAP): /on_search (items SJT, RJT)
  rect rgb(191, 223, 255)
  Buyer App (BAP)->>Seller App (BPP): /select (item I1 x 1)
  end
  Seller App (BPP)-->>Buyer App (BAP): /on_select (quote)
  Buyer App (BAP)->>Seller App (BPP): /init (payment NOT-PAID)
  Seller App (BPP)-->>Buyer App (BAP): /on_init (payment NOT-PAID)
  Buyer App (BAP)->>Seller App (BPP): /confirm (payment PAID)
  Seller App (BPP)-->>Buyer App (BAP): /on_confirm (order.status ACTIVE; TICKET ACTIVE)
  Buyer App (BAP)->>Seller App (BPP): /status
  Seller App (BPP)-->>Buyer App (BAP): /on_status (order.status ACTIVE; TICKET ACTIVE)
  Buyer App (BAP)->>Seller App (BPP): /cancel (descriptor SOFT_CANCEL, reason 000)
  Seller App (BPP)-->>Buyer App (BAP): /on_cancel (order.status SOFT_CANCEL; TICKET ACTIVE, cancelled_by CONSUMER)
  Buyer App (BAP)->>Seller App (BPP): /cancel (descriptor CONFIRM_CANCEL, reason 000)
  Seller App (BPP)-->>Buyer App (BAP): /on_cancel (order.status CANCELLED; TICKET ACTIVE, cancelled_by CONSUMER)
```

## on_select_METRO_210

```mermaid
sequenceDiagram
  participant Buyer App (BAP)
  participant Gateway
  participant Seller App (BPP)
  Buyer App (BAP)->>Seller App (BPP): /search (A to B, peer-to-peer)
  Seller App (BPP)-->>Buyer App (BAP): /on_search (items SJT, RJT)
  Buyer App (BAP)->>Seller App (BPP): /select (item I1 x 1)
  rect rgb(191, 223, 255)
  Seller App (BPP)-->>Buyer App (BAP): /on_select (quote)
  end
  Buyer App (BAP)->>Seller App (BPP): /init (payment NOT-PAID)
  Seller App (BPP)-->>Buyer App (BAP): /on_init (payment NOT-PAID)
  Buyer App (BAP)->>Seller App (BPP): /confirm (payment PAID)
  Seller App (BPP)-->>Buyer App (BAP): /on_confirm (order.status ACTIVE; TICKET ACTIVE)
  Buyer App (BAP)->>Seller App (BPP): /status
  Seller App (BPP)-->>Buyer App (BAP): /on_status (order.status ACTIVE; TICKET ACTIVE)
  Buyer App (BAP)->>Seller App (BPP): /cancel (descriptor SOFT_CANCEL, reason 000)
  Seller App (BPP)-->>Buyer App (BAP): /on_cancel (order.status SOFT_CANCEL; TICKET ACTIVE, cancelled_by CONSUMER)
  Buyer App (BAP)->>Seller App (BPP): /cancel (descriptor CONFIRM_CANCEL, reason 000)
  Seller App (BPP)-->>Buyer App (BAP): /on_cancel (order.status CANCELLED; TICKET ACTIVE, cancelled_by CONSUMER)
```

## init_METRO_210

```mermaid
sequenceDiagram
  participant Buyer App (BAP)
  participant Gateway
  participant Seller App (BPP)
  Buyer App (BAP)->>Seller App (BPP): /search (A to B, peer-to-peer)
  Seller App (BPP)-->>Buyer App (BAP): /on_search (items SJT, RJT)
  Buyer App (BAP)->>Seller App (BPP): /select (item I1 x 1)
  Seller App (BPP)-->>Buyer App (BAP): /on_select (quote)
  rect rgb(191, 223, 255)
  Buyer App (BAP)->>Seller App (BPP): /init (payment NOT-PAID)
  end
  Seller App (BPP)-->>Buyer App (BAP): /on_init (payment NOT-PAID)
  Buyer App (BAP)->>Seller App (BPP): /confirm (payment PAID)
  Seller App (BPP)-->>Buyer App (BAP): /on_confirm (order.status ACTIVE; TICKET ACTIVE)
  Buyer App (BAP)->>Seller App (BPP): /status
  Seller App (BPP)-->>Buyer App (BAP): /on_status (order.status ACTIVE; TICKET ACTIVE)
  Buyer App (BAP)->>Seller App (BPP): /cancel (descriptor SOFT_CANCEL, reason 000)
  Seller App (BPP)-->>Buyer App (BAP): /on_cancel (order.status SOFT_CANCEL; TICKET ACTIVE, cancelled_by CONSUMER)
  Buyer App (BAP)->>Seller App (BPP): /cancel (descriptor CONFIRM_CANCEL, reason 000)
  Seller App (BPP)-->>Buyer App (BAP): /on_cancel (order.status CANCELLED; TICKET ACTIVE, cancelled_by CONSUMER)
```

## on_init_METRO_210

```mermaid
sequenceDiagram
  participant Buyer App (BAP)
  participant Gateway
  participant Seller App (BPP)
  Buyer App (BAP)->>Seller App (BPP): /search (A to B, peer-to-peer)
  Seller App (BPP)-->>Buyer App (BAP): /on_search (items SJT, RJT)
  Buyer App (BAP)->>Seller App (BPP): /select (item I1 x 1)
  Seller App (BPP)-->>Buyer App (BAP): /on_select (quote)
  Buyer App (BAP)->>Seller App (BPP): /init (payment NOT-PAID)
  rect rgb(191, 223, 255)
  Seller App (BPP)-->>Buyer App (BAP): /on_init (payment NOT-PAID)
  end
  Buyer App (BAP)->>Seller App (BPP): /confirm (payment PAID)
  Seller App (BPP)-->>Buyer App (BAP): /on_confirm (order.status ACTIVE; TICKET ACTIVE)
  Buyer App (BAP)->>Seller App (BPP): /status
  Seller App (BPP)-->>Buyer App (BAP): /on_status (order.status ACTIVE; TICKET ACTIVE)
  Buyer App (BAP)->>Seller App (BPP): /cancel (descriptor SOFT_CANCEL, reason 000)
  Seller App (BPP)-->>Buyer App (BAP): /on_cancel (order.status SOFT_CANCEL; TICKET ACTIVE, cancelled_by CONSUMER)
  Buyer App (BAP)->>Seller App (BPP): /cancel (descriptor CONFIRM_CANCEL, reason 000)
  Seller App (BPP)-->>Buyer App (BAP): /on_cancel (order.status CANCELLED; TICKET ACTIVE, cancelled_by CONSUMER)
```

## confirm_METRO_210

```mermaid
sequenceDiagram
  participant Buyer App (BAP)
  participant Gateway
  participant Seller App (BPP)
  Buyer App (BAP)->>Seller App (BPP): /search (A to B, peer-to-peer)
  Seller App (BPP)-->>Buyer App (BAP): /on_search (items SJT, RJT)
  Buyer App (BAP)->>Seller App (BPP): /select (item I1 x 1)
  Seller App (BPP)-->>Buyer App (BAP): /on_select (quote)
  Buyer App (BAP)->>Seller App (BPP): /init (payment NOT-PAID)
  Seller App (BPP)-->>Buyer App (BAP): /on_init (payment NOT-PAID)
  rect rgb(191, 223, 255)
  Buyer App (BAP)->>Seller App (BPP): /confirm (payment PAID)
  end
  Seller App (BPP)-->>Buyer App (BAP): /on_confirm (order.status ACTIVE; TICKET ACTIVE)
  Buyer App (BAP)->>Seller App (BPP): /status
  Seller App (BPP)-->>Buyer App (BAP): /on_status (order.status ACTIVE; TICKET ACTIVE)
  Buyer App (BAP)->>Seller App (BPP): /cancel (descriptor SOFT_CANCEL, reason 000)
  Seller App (BPP)-->>Buyer App (BAP): /on_cancel (order.status SOFT_CANCEL; TICKET ACTIVE, cancelled_by CONSUMER)
  Buyer App (BAP)->>Seller App (BPP): /cancel (descriptor CONFIRM_CANCEL, reason 000)
  Seller App (BPP)-->>Buyer App (BAP): /on_cancel (order.status CANCELLED; TICKET ACTIVE, cancelled_by CONSUMER)
```

## on_confirm_delayed_METRO_210

```mermaid
sequenceDiagram
  participant Buyer App (BAP)
  participant Gateway
  participant Seller App (BPP)
  Buyer App (BAP)->>Seller App (BPP): /search (A to B, peer-to-peer)
  Seller App (BPP)-->>Buyer App (BAP): /on_search (items SJT, RJT)
  Buyer App (BAP)->>Seller App (BPP): /select (item I1 x 1)
  Seller App (BPP)-->>Buyer App (BAP): /on_select (quote)
  Buyer App (BAP)->>Seller App (BPP): /init (payment NOT-PAID)
  Seller App (BPP)-->>Buyer App (BAP): /on_init (payment NOT-PAID)
  Buyer App (BAP)->>Seller App (BPP): /confirm (payment PAID)
  rect rgb(191, 223, 255)
  Seller App (BPP)-->>Buyer App (BAP): /on_confirm (order.status ACTIVE; TICKET ACTIVE)
  end
  Buyer App (BAP)->>Seller App (BPP): /status
  Seller App (BPP)-->>Buyer App (BAP): /on_status (order.status ACTIVE; TICKET ACTIVE)
  Buyer App (BAP)->>Seller App (BPP): /cancel (descriptor SOFT_CANCEL, reason 000)
  Seller App (BPP)-->>Buyer App (BAP): /on_cancel (order.status SOFT_CANCEL; TICKET ACTIVE, cancelled_by CONSUMER)
  Buyer App (BAP)->>Seller App (BPP): /cancel (descriptor CONFIRM_CANCEL, reason 000)
  Seller App (BPP)-->>Buyer App (BAP): /on_cancel (order.status CANCELLED; TICKET ACTIVE, cancelled_by CONSUMER)
```

## status_tech_cancel_METRO_210

```mermaid
sequenceDiagram
  participant Buyer App (BAP)
  participant Gateway
  participant Seller App (BPP)
  Buyer App (BAP)->>Seller App (BPP): /search (A to B, peer-to-peer)
  Seller App (BPP)-->>Buyer App (BAP): /on_search (items SJT, RJT)
  Buyer App (BAP)->>Seller App (BPP): /select (item I1 x 1)
  Seller App (BPP)-->>Buyer App (BAP): /on_select (quote)
  Buyer App (BAP)->>Seller App (BPP): /init (payment NOT-PAID)
  Seller App (BPP)-->>Buyer App (BAP): /on_init (payment NOT-PAID)
  Buyer App (BAP)->>Seller App (BPP): /confirm (payment PAID)
  Seller App (BPP)-->>Buyer App (BAP): /on_confirm (order.status ACTIVE; TICKET ACTIVE)
  rect rgb(191, 223, 255)
  Buyer App (BAP)->>Seller App (BPP): /status
  end
  Seller App (BPP)-->>Buyer App (BAP): /on_status (order.status ACTIVE; TICKET ACTIVE)
  Buyer App (BAP)->>Seller App (BPP): /cancel (descriptor SOFT_CANCEL, reason 000)
  Seller App (BPP)-->>Buyer App (BAP): /on_cancel (order.status SOFT_CANCEL; TICKET ACTIVE, cancelled_by CONSUMER)
  Buyer App (BAP)->>Seller App (BPP): /cancel (descriptor CONFIRM_CANCEL, reason 000)
  Seller App (BPP)-->>Buyer App (BAP): /on_cancel (order.status CANCELLED; TICKET ACTIVE, cancelled_by CONSUMER)
```

## on_status_tech_METRO_210

```mermaid
sequenceDiagram
  participant Buyer App (BAP)
  participant Gateway
  participant Seller App (BPP)
  Buyer App (BAP)->>Seller App (BPP): /search (A to B, peer-to-peer)
  Seller App (BPP)-->>Buyer App (BAP): /on_search (items SJT, RJT)
  Buyer App (BAP)->>Seller App (BPP): /select (item I1 x 1)
  Seller App (BPP)-->>Buyer App (BAP): /on_select (quote)
  Buyer App (BAP)->>Seller App (BPP): /init (payment NOT-PAID)
  Seller App (BPP)-->>Buyer App (BAP): /on_init (payment NOT-PAID)
  Buyer App (BAP)->>Seller App (BPP): /confirm (payment PAID)
  Seller App (BPP)-->>Buyer App (BAP): /on_confirm (order.status ACTIVE; TICKET ACTIVE)
  Buyer App (BAP)->>Seller App (BPP): /status
  rect rgb(191, 223, 255)
  Seller App (BPP)-->>Buyer App (BAP): /on_status (order.status ACTIVE; TICKET ACTIVE)
  end
  Buyer App (BAP)->>Seller App (BPP): /cancel (descriptor SOFT_CANCEL, reason 000)
  Seller App (BPP)-->>Buyer App (BAP): /on_cancel (order.status SOFT_CANCEL; TICKET ACTIVE, cancelled_by CONSUMER)
  Buyer App (BAP)->>Seller App (BPP): /cancel (descriptor CONFIRM_CANCEL, reason 000)
  Seller App (BPP)-->>Buyer App (BAP): /on_cancel (order.status CANCELLED; TICKET ACTIVE, cancelled_by CONSUMER)
```

## cancel_tech_METRO_210

```mermaid
sequenceDiagram
  participant Buyer App (BAP)
  participant Gateway
  participant Seller App (BPP)
  Buyer App (BAP)->>Seller App (BPP): /search (A to B, peer-to-peer)
  Seller App (BPP)-->>Buyer App (BAP): /on_search (items SJT, RJT)
  Buyer App (BAP)->>Seller App (BPP): /select (item I1 x 1)
  Seller App (BPP)-->>Buyer App (BAP): /on_select (quote)
  Buyer App (BAP)->>Seller App (BPP): /init (payment NOT-PAID)
  Seller App (BPP)-->>Buyer App (BAP): /on_init (payment NOT-PAID)
  Buyer App (BAP)->>Seller App (BPP): /confirm (payment PAID)
  Seller App (BPP)-->>Buyer App (BAP): /on_confirm (order.status ACTIVE; TICKET ACTIVE)
  Buyer App (BAP)->>Seller App (BPP): /status
  Seller App (BPP)-->>Buyer App (BAP): /on_status (order.status ACTIVE; TICKET ACTIVE)
  rect rgb(191, 223, 255)
  Buyer App (BAP)->>Seller App (BPP): /cancel (descriptor SOFT_CANCEL, reason 000)
  end
  Seller App (BPP)-->>Buyer App (BAP): /on_cancel (order.status SOFT_CANCEL; TICKET ACTIVE, cancelled_by CONSUMER)
  Buyer App (BAP)->>Seller App (BPP): /cancel (descriptor CONFIRM_CANCEL, reason 000)
  Seller App (BPP)-->>Buyer App (BAP): /on_cancel (order.status CANCELLED; TICKET ACTIVE, cancelled_by CONSUMER)
```

## on_cancel_soft_tech_METRO_210

```mermaid
sequenceDiagram
  participant Buyer App (BAP)
  participant Gateway
  participant Seller App (BPP)
  Buyer App (BAP)->>Seller App (BPP): /search (A to B, peer-to-peer)
  Seller App (BPP)-->>Buyer App (BAP): /on_search (items SJT, RJT)
  Buyer App (BAP)->>Seller App (BPP): /select (item I1 x 1)
  Seller App (BPP)-->>Buyer App (BAP): /on_select (quote)
  Buyer App (BAP)->>Seller App (BPP): /init (payment NOT-PAID)
  Seller App (BPP)-->>Buyer App (BAP): /on_init (payment NOT-PAID)
  Buyer App (BAP)->>Seller App (BPP): /confirm (payment PAID)
  Seller App (BPP)-->>Buyer App (BAP): /on_confirm (order.status ACTIVE; TICKET ACTIVE)
  Buyer App (BAP)->>Seller App (BPP): /status
  Seller App (BPP)-->>Buyer App (BAP): /on_status (order.status ACTIVE; TICKET ACTIVE)
  Buyer App (BAP)->>Seller App (BPP): /cancel (descriptor SOFT_CANCEL, reason 000)
  rect rgb(191, 223, 255)
  Seller App (BPP)-->>Buyer App (BAP): /on_cancel (order.status SOFT_CANCEL; TICKET ACTIVE, cancelled_by CONSUMER)
  end
  Buyer App (BAP)->>Seller App (BPP): /cancel (descriptor CONFIRM_CANCEL, reason 000)
  Seller App (BPP)-->>Buyer App (BAP): /on_cancel (order.status CANCELLED; TICKET ACTIVE, cancelled_by CONSUMER)
```

## cancel_hard_METRO_210

```mermaid
sequenceDiagram
  participant Buyer App (BAP)
  participant Gateway
  participant Seller App (BPP)
  Buyer App (BAP)->>Seller App (BPP): /search (A to B, peer-to-peer)
  Seller App (BPP)-->>Buyer App (BAP): /on_search (items SJT, RJT)
  Buyer App (BAP)->>Seller App (BPP): /select (item I1 x 1)
  Seller App (BPP)-->>Buyer App (BAP): /on_select (quote)
  Buyer App (BAP)->>Seller App (BPP): /init (payment NOT-PAID)
  Seller App (BPP)-->>Buyer App (BAP): /on_init (payment NOT-PAID)
  Buyer App (BAP)->>Seller App (BPP): /confirm (payment PAID)
  Seller App (BPP)-->>Buyer App (BAP): /on_confirm (order.status ACTIVE; TICKET ACTIVE)
  Buyer App (BAP)->>Seller App (BPP): /status
  Seller App (BPP)-->>Buyer App (BAP): /on_status (order.status ACTIVE; TICKET ACTIVE)
  Buyer App (BAP)->>Seller App (BPP): /cancel (descriptor SOFT_CANCEL, reason 000)
  Seller App (BPP)-->>Buyer App (BAP): /on_cancel (order.status SOFT_CANCEL; TICKET ACTIVE, cancelled_by CONSUMER)
  rect rgb(191, 223, 255)
  Buyer App (BAP)->>Seller App (BPP): /cancel (descriptor CONFIRM_CANCEL, reason 000)
  end
  Seller App (BPP)-->>Buyer App (BAP): /on_cancel (order.status CANCELLED; TICKET ACTIVE, cancelled_by CONSUMER)
```

## on_cancel_hard_tech_METRO_210

```mermaid
sequenceDiagram
  participant Buyer App (BAP)
  participant Gateway
  participant Seller App (BPP)
  Buyer App (BAP)->>Seller App (BPP): /search (A to B, peer-to-peer)
  Seller App (BPP)-->>Buyer App (BAP): /on_search (items SJT, RJT)
  Buyer App (BAP)->>Seller App (BPP): /select (item I1 x 1)
  Seller App (BPP)-->>Buyer App (BAP): /on_select (quote)
  Buyer App (BAP)->>Seller App (BPP): /init (payment NOT-PAID)
  Seller App (BPP)-->>Buyer App (BAP): /on_init (payment NOT-PAID)
  Buyer App (BAP)->>Seller App (BPP): /confirm (payment PAID)
  Seller App (BPP)-->>Buyer App (BAP): /on_confirm (order.status ACTIVE; TICKET ACTIVE)
  Buyer App (BAP)->>Seller App (BPP): /status
  Seller App (BPP)-->>Buyer App (BAP): /on_status (order.status ACTIVE; TICKET ACTIVE)
  Buyer App (BAP)->>Seller App (BPP): /cancel (descriptor SOFT_CANCEL, reason 000)
  Seller App (BPP)-->>Buyer App (BAP): /on_cancel (order.status SOFT_CANCEL; TICKET ACTIVE, cancelled_by CONSUMER)
  Buyer App (BAP)->>Seller App (BPP): /cancel (descriptor CONFIRM_CANCEL, reason 000)
  rect rgb(191, 223, 255)
  Seller App (BPP)-->>Buyer App (BAP): /on_cancel (order.status CANCELLED; TICKET ACTIVE, cancelled_by CONSUMER)
  end
```

# Schedule_Trip_Rider_Cancellation_After_Driver_Assignment — Sequence Diagrams

Internal data file consumed by the Developer Guide's "Sequence Diagram" tab (API Walkthrough).
Not meant to be shown as its own docs page — the frontend filters this slug out of the Use Case
Brief / Additional Resources / Changelog tab lists and instead looks up the section matching the
selected API call's `action_id` (the `##` heading below) to render that step's diagram.

One `## <action_id>` heading per step of `Schedule_Trip_Rider_Cancellation_After_Driver_Assignment.yaml` (Ride-hailing), in that flow's own step order, each followed by its Mermaid `sequenceDiagram`: the whole flow, with that call's own message(s) highlighted — same convention as the other domains' per-step sequence-diagram docs.

## search_schedule_trip

```mermaid
sequenceDiagram
  participant Buyer App (BAP)
  participant Gateway
  participant Seller App (BPP)
  rect rgb(191, 223, 255)
  Buyer App (BAP)->>Gateway: /search (stops START, END)
  Gateway->>Seller App (BPP): /search (forwarded)
  end
  Seller App (BPP)-->>Buyer App (BAP): /on_search (catalog)
  Buyer App (BAP)->>Seller App (BPP): /select
  Seller App (BPP)-->>Buyer App (BAP): /on_select (quote)
  Buyer App (BAP)->>Seller App (BPP): /init (payment ON_FULFILLMENT NOT_PAID, collected_by BPP)
  Seller App (BPP)-->>Buyer App (BAP): /on_init (payment ON_FULFILLMENT NOT_PAID, collected_by BPP)
  Buyer App (BAP)->>Seller App (BPP): /confirm (payment ON_FULFILLMENT NOT_PAID, collected_by BPP)
  Seller App (BPP)-->>Buyer App (BAP): /on_confirm (order.status ACTIVE; fulfillment state RIDE_CONFIRMED)
  Seller App (BPP)-->>Buyer App (BAP): /on_update (unsolicited): order.status ACTIVE; fulfillment state RIDE_ASSIGNED
  Buyer App (BAP)->>Seller App (BPP): /cancel (descriptor SOFT_CANCEL, reason None)
  Seller App (BPP)-->>Buyer App (BAP): /on_cancel (order.status SOFT_CANCEL; fulfillment state RIDE_ASSIGNED, cancelled_by CONSUMER)
  Buyer App (BAP)->>Seller App (BPP): /cancel (descriptor CONFIRM_CANCEL, reason None)
  Seller App (BPP)-->>Buyer App (BAP): /on_cancel (order.status CANCELLED; fulfillment state RIDE_CANCELLED, cancelled_by CONSUMER)
```

## on_search_schedule_trip

```mermaid
sequenceDiagram
  participant Buyer App (BAP)
  participant Gateway
  participant Seller App (BPP)
  Buyer App (BAP)->>Gateway: /search (stops START, END)
  Gateway->>Seller App (BPP): /search (forwarded)
  rect rgb(191, 223, 255)
  Seller App (BPP)-->>Buyer App (BAP): /on_search (catalog)
  end
  Buyer App (BAP)->>Seller App (BPP): /select
  Seller App (BPP)-->>Buyer App (BAP): /on_select (quote)
  Buyer App (BAP)->>Seller App (BPP): /init (payment ON_FULFILLMENT NOT_PAID, collected_by BPP)
  Seller App (BPP)-->>Buyer App (BAP): /on_init (payment ON_FULFILLMENT NOT_PAID, collected_by BPP)
  Buyer App (BAP)->>Seller App (BPP): /confirm (payment ON_FULFILLMENT NOT_PAID, collected_by BPP)
  Seller App (BPP)-->>Buyer App (BAP): /on_confirm (order.status ACTIVE; fulfillment state RIDE_CONFIRMED)
  Seller App (BPP)-->>Buyer App (BAP): /on_update (unsolicited): order.status ACTIVE; fulfillment state RIDE_ASSIGNED
  Buyer App (BAP)->>Seller App (BPP): /cancel (descriptor SOFT_CANCEL, reason None)
  Seller App (BPP)-->>Buyer App (BAP): /on_cancel (order.status SOFT_CANCEL; fulfillment state RIDE_ASSIGNED, cancelled_by CONSUMER)
  Buyer App (BAP)->>Seller App (BPP): /cancel (descriptor CONFIRM_CANCEL, reason None)
  Seller App (BPP)-->>Buyer App (BAP): /on_cancel (order.status CANCELLED; fulfillment state RIDE_CANCELLED, cancelled_by CONSUMER)
```

## select

```mermaid
sequenceDiagram
  participant Buyer App (BAP)
  participant Gateway
  participant Seller App (BPP)
  Buyer App (BAP)->>Gateway: /search (stops START, END)
  Gateway->>Seller App (BPP): /search (forwarded)
  Seller App (BPP)-->>Buyer App (BAP): /on_search (catalog)
  rect rgb(191, 223, 255)
  Buyer App (BAP)->>Seller App (BPP): /select
  end
  Seller App (BPP)-->>Buyer App (BAP): /on_select (quote)
  Buyer App (BAP)->>Seller App (BPP): /init (payment ON_FULFILLMENT NOT_PAID, collected_by BPP)
  Seller App (BPP)-->>Buyer App (BAP): /on_init (payment ON_FULFILLMENT NOT_PAID, collected_by BPP)
  Buyer App (BAP)->>Seller App (BPP): /confirm (payment ON_FULFILLMENT NOT_PAID, collected_by BPP)
  Seller App (BPP)-->>Buyer App (BAP): /on_confirm (order.status ACTIVE; fulfillment state RIDE_CONFIRMED)
  Seller App (BPP)-->>Buyer App (BAP): /on_update (unsolicited): order.status ACTIVE; fulfillment state RIDE_ASSIGNED
  Buyer App (BAP)->>Seller App (BPP): /cancel (descriptor SOFT_CANCEL, reason None)
  Seller App (BPP)-->>Buyer App (BAP): /on_cancel (order.status SOFT_CANCEL; fulfillment state RIDE_ASSIGNED, cancelled_by CONSUMER)
  Buyer App (BAP)->>Seller App (BPP): /cancel (descriptor CONFIRM_CANCEL, reason None)
  Seller App (BPP)-->>Buyer App (BAP): /on_cancel (order.status CANCELLED; fulfillment state RIDE_CANCELLED, cancelled_by CONSUMER)
```

## on_select

```mermaid
sequenceDiagram
  participant Buyer App (BAP)
  participant Gateway
  participant Seller App (BPP)
  Buyer App (BAP)->>Gateway: /search (stops START, END)
  Gateway->>Seller App (BPP): /search (forwarded)
  Seller App (BPP)-->>Buyer App (BAP): /on_search (catalog)
  Buyer App (BAP)->>Seller App (BPP): /select
  rect rgb(191, 223, 255)
  Seller App (BPP)-->>Buyer App (BAP): /on_select (quote)
  end
  Buyer App (BAP)->>Seller App (BPP): /init (payment ON_FULFILLMENT NOT_PAID, collected_by BPP)
  Seller App (BPP)-->>Buyer App (BAP): /on_init (payment ON_FULFILLMENT NOT_PAID, collected_by BPP)
  Buyer App (BAP)->>Seller App (BPP): /confirm (payment ON_FULFILLMENT NOT_PAID, collected_by BPP)
  Seller App (BPP)-->>Buyer App (BAP): /on_confirm (order.status ACTIVE; fulfillment state RIDE_CONFIRMED)
  Seller App (BPP)-->>Buyer App (BAP): /on_update (unsolicited): order.status ACTIVE; fulfillment state RIDE_ASSIGNED
  Buyer App (BAP)->>Seller App (BPP): /cancel (descriptor SOFT_CANCEL, reason None)
  Seller App (BPP)-->>Buyer App (BAP): /on_cancel (order.status SOFT_CANCEL; fulfillment state RIDE_ASSIGNED, cancelled_by CONSUMER)
  Buyer App (BAP)->>Seller App (BPP): /cancel (descriptor CONFIRM_CANCEL, reason None)
  Seller App (BPP)-->>Buyer App (BAP): /on_cancel (order.status CANCELLED; fulfillment state RIDE_CANCELLED, cancelled_by CONSUMER)
```

## init

```mermaid
sequenceDiagram
  participant Buyer App (BAP)
  participant Gateway
  participant Seller App (BPP)
  Buyer App (BAP)->>Gateway: /search (stops START, END)
  Gateway->>Seller App (BPP): /search (forwarded)
  Seller App (BPP)-->>Buyer App (BAP): /on_search (catalog)
  Buyer App (BAP)->>Seller App (BPP): /select
  Seller App (BPP)-->>Buyer App (BAP): /on_select (quote)
  rect rgb(191, 223, 255)
  Buyer App (BAP)->>Seller App (BPP): /init (payment ON_FULFILLMENT NOT_PAID, collected_by BPP)
  end
  Seller App (BPP)-->>Buyer App (BAP): /on_init (payment ON_FULFILLMENT NOT_PAID, collected_by BPP)
  Buyer App (BAP)->>Seller App (BPP): /confirm (payment ON_FULFILLMENT NOT_PAID, collected_by BPP)
  Seller App (BPP)-->>Buyer App (BAP): /on_confirm (order.status ACTIVE; fulfillment state RIDE_CONFIRMED)
  Seller App (BPP)-->>Buyer App (BAP): /on_update (unsolicited): order.status ACTIVE; fulfillment state RIDE_ASSIGNED
  Buyer App (BAP)->>Seller App (BPP): /cancel (descriptor SOFT_CANCEL, reason None)
  Seller App (BPP)-->>Buyer App (BAP): /on_cancel (order.status SOFT_CANCEL; fulfillment state RIDE_ASSIGNED, cancelled_by CONSUMER)
  Buyer App (BAP)->>Seller App (BPP): /cancel (descriptor CONFIRM_CANCEL, reason None)
  Seller App (BPP)-->>Buyer App (BAP): /on_cancel (order.status CANCELLED; fulfillment state RIDE_CANCELLED, cancelled_by CONSUMER)
```

## on_init

```mermaid
sequenceDiagram
  participant Buyer App (BAP)
  participant Gateway
  participant Seller App (BPP)
  Buyer App (BAP)->>Gateway: /search (stops START, END)
  Gateway->>Seller App (BPP): /search (forwarded)
  Seller App (BPP)-->>Buyer App (BAP): /on_search (catalog)
  Buyer App (BAP)->>Seller App (BPP): /select
  Seller App (BPP)-->>Buyer App (BAP): /on_select (quote)
  Buyer App (BAP)->>Seller App (BPP): /init (payment ON_FULFILLMENT NOT_PAID, collected_by BPP)
  rect rgb(191, 223, 255)
  Seller App (BPP)-->>Buyer App (BAP): /on_init (payment ON_FULFILLMENT NOT_PAID, collected_by BPP)
  end
  Buyer App (BAP)->>Seller App (BPP): /confirm (payment ON_FULFILLMENT NOT_PAID, collected_by BPP)
  Seller App (BPP)-->>Buyer App (BAP): /on_confirm (order.status ACTIVE; fulfillment state RIDE_CONFIRMED)
  Seller App (BPP)-->>Buyer App (BAP): /on_update (unsolicited): order.status ACTIVE; fulfillment state RIDE_ASSIGNED
  Buyer App (BAP)->>Seller App (BPP): /cancel (descriptor SOFT_CANCEL, reason None)
  Seller App (BPP)-->>Buyer App (BAP): /on_cancel (order.status SOFT_CANCEL; fulfillment state RIDE_ASSIGNED, cancelled_by CONSUMER)
  Buyer App (BAP)->>Seller App (BPP): /cancel (descriptor CONFIRM_CANCEL, reason None)
  Seller App (BPP)-->>Buyer App (BAP): /on_cancel (order.status CANCELLED; fulfillment state RIDE_CANCELLED, cancelled_by CONSUMER)
```

## confirm

```mermaid
sequenceDiagram
  participant Buyer App (BAP)
  participant Gateway
  participant Seller App (BPP)
  Buyer App (BAP)->>Gateway: /search (stops START, END)
  Gateway->>Seller App (BPP): /search (forwarded)
  Seller App (BPP)-->>Buyer App (BAP): /on_search (catalog)
  Buyer App (BAP)->>Seller App (BPP): /select
  Seller App (BPP)-->>Buyer App (BAP): /on_select (quote)
  Buyer App (BAP)->>Seller App (BPP): /init (payment ON_FULFILLMENT NOT_PAID, collected_by BPP)
  Seller App (BPP)-->>Buyer App (BAP): /on_init (payment ON_FULFILLMENT NOT_PAID, collected_by BPP)
  rect rgb(191, 223, 255)
  Buyer App (BAP)->>Seller App (BPP): /confirm (payment ON_FULFILLMENT NOT_PAID, collected_by BPP)
  end
  Seller App (BPP)-->>Buyer App (BAP): /on_confirm (order.status ACTIVE; fulfillment state RIDE_CONFIRMED)
  Seller App (BPP)-->>Buyer App (BAP): /on_update (unsolicited): order.status ACTIVE; fulfillment state RIDE_ASSIGNED
  Buyer App (BAP)->>Seller App (BPP): /cancel (descriptor SOFT_CANCEL, reason None)
  Seller App (BPP)-->>Buyer App (BAP): /on_cancel (order.status SOFT_CANCEL; fulfillment state RIDE_ASSIGNED, cancelled_by CONSUMER)
  Buyer App (BAP)->>Seller App (BPP): /cancel (descriptor CONFIRM_CANCEL, reason None)
  Seller App (BPP)-->>Buyer App (BAP): /on_cancel (order.status CANCELLED; fulfillment state RIDE_CANCELLED, cancelled_by CONSUMER)
```

## on_confirm_rental

```mermaid
sequenceDiagram
  participant Buyer App (BAP)
  participant Gateway
  participant Seller App (BPP)
  Buyer App (BAP)->>Gateway: /search (stops START, END)
  Gateway->>Seller App (BPP): /search (forwarded)
  Seller App (BPP)-->>Buyer App (BAP): /on_search (catalog)
  Buyer App (BAP)->>Seller App (BPP): /select
  Seller App (BPP)-->>Buyer App (BAP): /on_select (quote)
  Buyer App (BAP)->>Seller App (BPP): /init (payment ON_FULFILLMENT NOT_PAID, collected_by BPP)
  Seller App (BPP)-->>Buyer App (BAP): /on_init (payment ON_FULFILLMENT NOT_PAID, collected_by BPP)
  Buyer App (BAP)->>Seller App (BPP): /confirm (payment ON_FULFILLMENT NOT_PAID, collected_by BPP)
  rect rgb(191, 223, 255)
  Seller App (BPP)-->>Buyer App (BAP): /on_confirm (order.status ACTIVE; fulfillment state RIDE_CONFIRMED)
  end
  Seller App (BPP)-->>Buyer App (BAP): /on_update (unsolicited): order.status ACTIVE; fulfillment state RIDE_ASSIGNED
  Buyer App (BAP)->>Seller App (BPP): /cancel (descriptor SOFT_CANCEL, reason None)
  Seller App (BPP)-->>Buyer App (BAP): /on_cancel (order.status SOFT_CANCEL; fulfillment state RIDE_ASSIGNED, cancelled_by CONSUMER)
  Buyer App (BAP)->>Seller App (BPP): /cancel (descriptor CONFIRM_CANCEL, reason None)
  Seller App (BPP)-->>Buyer App (BAP): /on_cancel (order.status CANCELLED; fulfillment state RIDE_CANCELLED, cancelled_by CONSUMER)
```

## on_update_ride_assigned

```mermaid
sequenceDiagram
  participant Buyer App (BAP)
  participant Gateway
  participant Seller App (BPP)
  Buyer App (BAP)->>Gateway: /search (stops START, END)
  Gateway->>Seller App (BPP): /search (forwarded)
  Seller App (BPP)-->>Buyer App (BAP): /on_search (catalog)
  Buyer App (BAP)->>Seller App (BPP): /select
  Seller App (BPP)-->>Buyer App (BAP): /on_select (quote)
  Buyer App (BAP)->>Seller App (BPP): /init (payment ON_FULFILLMENT NOT_PAID, collected_by BPP)
  Seller App (BPP)-->>Buyer App (BAP): /on_init (payment ON_FULFILLMENT NOT_PAID, collected_by BPP)
  Buyer App (BAP)->>Seller App (BPP): /confirm (payment ON_FULFILLMENT NOT_PAID, collected_by BPP)
  Seller App (BPP)-->>Buyer App (BAP): /on_confirm (order.status ACTIVE; fulfillment state RIDE_CONFIRMED)
  rect rgb(191, 223, 255)
  Seller App (BPP)-->>Buyer App (BAP): /on_update (unsolicited): order.status ACTIVE; fulfillment state RIDE_ASSIGNED
  end
  Buyer App (BAP)->>Seller App (BPP): /cancel (descriptor SOFT_CANCEL, reason None)
  Seller App (BPP)-->>Buyer App (BAP): /on_cancel (order.status SOFT_CANCEL; fulfillment state RIDE_ASSIGNED, cancelled_by CONSUMER)
  Buyer App (BAP)->>Seller App (BPP): /cancel (descriptor CONFIRM_CANCEL, reason None)
  Seller App (BPP)-->>Buyer App (BAP): /on_cancel (order.status CANCELLED; fulfillment state RIDE_CANCELLED, cancelled_by CONSUMER)
```

## cancel

```mermaid
sequenceDiagram
  participant Buyer App (BAP)
  participant Gateway
  participant Seller App (BPP)
  Buyer App (BAP)->>Gateway: /search (stops START, END)
  Gateway->>Seller App (BPP): /search (forwarded)
  Seller App (BPP)-->>Buyer App (BAP): /on_search (catalog)
  Buyer App (BAP)->>Seller App (BPP): /select
  Seller App (BPP)-->>Buyer App (BAP): /on_select (quote)
  Buyer App (BAP)->>Seller App (BPP): /init (payment ON_FULFILLMENT NOT_PAID, collected_by BPP)
  Seller App (BPP)-->>Buyer App (BAP): /on_init (payment ON_FULFILLMENT NOT_PAID, collected_by BPP)
  Buyer App (BAP)->>Seller App (BPP): /confirm (payment ON_FULFILLMENT NOT_PAID, collected_by BPP)
  Seller App (BPP)-->>Buyer App (BAP): /on_confirm (order.status ACTIVE; fulfillment state RIDE_CONFIRMED)
  Seller App (BPP)-->>Buyer App (BAP): /on_update (unsolicited): order.status ACTIVE; fulfillment state RIDE_ASSIGNED
  rect rgb(191, 223, 255)
  Buyer App (BAP)->>Seller App (BPP): /cancel (descriptor SOFT_CANCEL, reason None)
  end
  Seller App (BPP)-->>Buyer App (BAP): /on_cancel (order.status SOFT_CANCEL; fulfillment state RIDE_ASSIGNED, cancelled_by CONSUMER)
  Buyer App (BAP)->>Seller App (BPP): /cancel (descriptor CONFIRM_CANCEL, reason None)
  Seller App (BPP)-->>Buyer App (BAP): /on_cancel (order.status CANCELLED; fulfillment state RIDE_CANCELLED, cancelled_by CONSUMER)
```

## on_cancel_ride_cancel

```mermaid
sequenceDiagram
  participant Buyer App (BAP)
  participant Gateway
  participant Seller App (BPP)
  Buyer App (BAP)->>Gateway: /search (stops START, END)
  Gateway->>Seller App (BPP): /search (forwarded)
  Seller App (BPP)-->>Buyer App (BAP): /on_search (catalog)
  Buyer App (BAP)->>Seller App (BPP): /select
  Seller App (BPP)-->>Buyer App (BAP): /on_select (quote)
  Buyer App (BAP)->>Seller App (BPP): /init (payment ON_FULFILLMENT NOT_PAID, collected_by BPP)
  Seller App (BPP)-->>Buyer App (BAP): /on_init (payment ON_FULFILLMENT NOT_PAID, collected_by BPP)
  Buyer App (BAP)->>Seller App (BPP): /confirm (payment ON_FULFILLMENT NOT_PAID, collected_by BPP)
  Seller App (BPP)-->>Buyer App (BAP): /on_confirm (order.status ACTIVE; fulfillment state RIDE_CONFIRMED)
  Seller App (BPP)-->>Buyer App (BAP): /on_update (unsolicited): order.status ACTIVE; fulfillment state RIDE_ASSIGNED
  Buyer App (BAP)->>Seller App (BPP): /cancel (descriptor SOFT_CANCEL, reason None)
  rect rgb(191, 223, 255)
  Seller App (BPP)-->>Buyer App (BAP): /on_cancel (order.status SOFT_CANCEL; fulfillment state RIDE_ASSIGNED, cancelled_by CONSUMER)
  end
  Buyer App (BAP)->>Seller App (BPP): /cancel (descriptor CONFIRM_CANCEL, reason None)
  Seller App (BPP)-->>Buyer App (BAP): /on_cancel (order.status CANCELLED; fulfillment state RIDE_CANCELLED, cancelled_by CONSUMER)
```

## cancel_hard

```mermaid
sequenceDiagram
  participant Buyer App (BAP)
  participant Gateway
  participant Seller App (BPP)
  Buyer App (BAP)->>Gateway: /search (stops START, END)
  Gateway->>Seller App (BPP): /search (forwarded)
  Seller App (BPP)-->>Buyer App (BAP): /on_search (catalog)
  Buyer App (BAP)->>Seller App (BPP): /select
  Seller App (BPP)-->>Buyer App (BAP): /on_select (quote)
  Buyer App (BAP)->>Seller App (BPP): /init (payment ON_FULFILLMENT NOT_PAID, collected_by BPP)
  Seller App (BPP)-->>Buyer App (BAP): /on_init (payment ON_FULFILLMENT NOT_PAID, collected_by BPP)
  Buyer App (BAP)->>Seller App (BPP): /confirm (payment ON_FULFILLMENT NOT_PAID, collected_by BPP)
  Seller App (BPP)-->>Buyer App (BAP): /on_confirm (order.status ACTIVE; fulfillment state RIDE_CONFIRMED)
  Seller App (BPP)-->>Buyer App (BAP): /on_update (unsolicited): order.status ACTIVE; fulfillment state RIDE_ASSIGNED
  Buyer App (BAP)->>Seller App (BPP): /cancel (descriptor SOFT_CANCEL, reason None)
  Seller App (BPP)-->>Buyer App (BAP): /on_cancel (order.status SOFT_CANCEL; fulfillment state RIDE_ASSIGNED, cancelled_by CONSUMER)
  rect rgb(191, 223, 255)
  Buyer App (BAP)->>Seller App (BPP): /cancel (descriptor CONFIRM_CANCEL, reason None)
  end
  Seller App (BPP)-->>Buyer App (BAP): /on_cancel (order.status CANCELLED; fulfillment state RIDE_CANCELLED, cancelled_by CONSUMER)
```

## on_cancel_hard

```mermaid
sequenceDiagram
  participant Buyer App (BAP)
  participant Gateway
  participant Seller App (BPP)
  Buyer App (BAP)->>Gateway: /search (stops START, END)
  Gateway->>Seller App (BPP): /search (forwarded)
  Seller App (BPP)-->>Buyer App (BAP): /on_search (catalog)
  Buyer App (BAP)->>Seller App (BPP): /select
  Seller App (BPP)-->>Buyer App (BAP): /on_select (quote)
  Buyer App (BAP)->>Seller App (BPP): /init (payment ON_FULFILLMENT NOT_PAID, collected_by BPP)
  Seller App (BPP)-->>Buyer App (BAP): /on_init (payment ON_FULFILLMENT NOT_PAID, collected_by BPP)
  Buyer App (BAP)->>Seller App (BPP): /confirm (payment ON_FULFILLMENT NOT_PAID, collected_by BPP)
  Seller App (BPP)-->>Buyer App (BAP): /on_confirm (order.status ACTIVE; fulfillment state RIDE_CONFIRMED)
  Seller App (BPP)-->>Buyer App (BAP): /on_update (unsolicited): order.status ACTIVE; fulfillment state RIDE_ASSIGNED
  Buyer App (BAP)->>Seller App (BPP): /cancel (descriptor SOFT_CANCEL, reason None)
  Seller App (BPP)-->>Buyer App (BAP): /on_cancel (order.status SOFT_CANCEL; fulfillment state RIDE_ASSIGNED, cancelled_by CONSUMER)
  Buyer App (BAP)->>Seller App (BPP): /cancel (descriptor CONFIRM_CANCEL, reason None)
  rect rgb(191, 223, 255)
  Seller App (BPP)-->>Buyer App (BAP): /on_cancel (order.status CANCELLED; fulfillment state RIDE_CANCELLED, cancelled_by CONSUMER)
  end
```

# OnDemand_Ride_cancellation_by_rider — Sequence Diagrams

Internal data file consumed by the Developer Guide's "Sequence Diagram" tab (API Walkthrough).
Not meant to be shown as its own docs page — the frontend filters this slug out of the Use Case
Brief / Additional Resources / Changelog tab lists and instead looks up the section matching the
selected API call's `action_id` (the `##` heading below) to render that step's diagram.

One `## <action_id>` heading per step of `OnDemand_Ride_cancellation_by_rider.yaml` (Ride-hailing), in that flow's own step order, each followed by its Mermaid `sequenceDiagram`: the whole flow, with that call's own message(s) highlighted — same convention as the other domains' per-step sequence-diagram docs.

## search_ride

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
  Seller App (BPP)-->>Buyer App (BAP): /on_confirm (order.status ACTIVE; fulfillment state RIDE_ASSIGNED)
  Seller App (BPP)-->>Buyer App (BAP): /on_status (unsolicited): order.status ACTIVE; fulfillment state RIDE_ENROUTE_PICKUP
  Seller App (BPP)-->>Buyer App (BAP): /on_status (unsolicited): order.status ACTIVE; fulfillment state RIDE_ARRIVED_PICKUP
  Buyer App (BAP)->>Seller App (BPP): /cancel (descriptor SOFT_CANCEL, reason None)
  Seller App (BPP)-->>Buyer App (BAP): /on_cancel (order.status SOFT_CANCEL; fulfillment state RIDE_ARRIVED_PICKUP, cancelled_by CONSUMER)
  Buyer App (BAP)->>Seller App (BPP): /cancel (descriptor CONFIRM_CANCEL, reason None)
  Seller App (BPP)-->>Buyer App (BAP): /on_cancel (order.status CANCELLED; fulfillment state RIDE_CANCELLED, cancelled_by CONSUMER)
```

## on_search

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
  Seller App (BPP)-->>Buyer App (BAP): /on_confirm (order.status ACTIVE; fulfillment state RIDE_ASSIGNED)
  Seller App (BPP)-->>Buyer App (BAP): /on_status (unsolicited): order.status ACTIVE; fulfillment state RIDE_ENROUTE_PICKUP
  Seller App (BPP)-->>Buyer App (BAP): /on_status (unsolicited): order.status ACTIVE; fulfillment state RIDE_ARRIVED_PICKUP
  Buyer App (BAP)->>Seller App (BPP): /cancel (descriptor SOFT_CANCEL, reason None)
  Seller App (BPP)-->>Buyer App (BAP): /on_cancel (order.status SOFT_CANCEL; fulfillment state RIDE_ARRIVED_PICKUP, cancelled_by CONSUMER)
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
  Seller App (BPP)-->>Buyer App (BAP): /on_confirm (order.status ACTIVE; fulfillment state RIDE_ASSIGNED)
  Seller App (BPP)-->>Buyer App (BAP): /on_status (unsolicited): order.status ACTIVE; fulfillment state RIDE_ENROUTE_PICKUP
  Seller App (BPP)-->>Buyer App (BAP): /on_status (unsolicited): order.status ACTIVE; fulfillment state RIDE_ARRIVED_PICKUP
  Buyer App (BAP)->>Seller App (BPP): /cancel (descriptor SOFT_CANCEL, reason None)
  Seller App (BPP)-->>Buyer App (BAP): /on_cancel (order.status SOFT_CANCEL; fulfillment state RIDE_ARRIVED_PICKUP, cancelled_by CONSUMER)
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
  Seller App (BPP)-->>Buyer App (BAP): /on_confirm (order.status ACTIVE; fulfillment state RIDE_ASSIGNED)
  Seller App (BPP)-->>Buyer App (BAP): /on_status (unsolicited): order.status ACTIVE; fulfillment state RIDE_ENROUTE_PICKUP
  Seller App (BPP)-->>Buyer App (BAP): /on_status (unsolicited): order.status ACTIVE; fulfillment state RIDE_ARRIVED_PICKUP
  Buyer App (BAP)->>Seller App (BPP): /cancel (descriptor SOFT_CANCEL, reason None)
  Seller App (BPP)-->>Buyer App (BAP): /on_cancel (order.status SOFT_CANCEL; fulfillment state RIDE_ARRIVED_PICKUP, cancelled_by CONSUMER)
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
  Seller App (BPP)-->>Buyer App (BAP): /on_confirm (order.status ACTIVE; fulfillment state RIDE_ASSIGNED)
  Seller App (BPP)-->>Buyer App (BAP): /on_status (unsolicited): order.status ACTIVE; fulfillment state RIDE_ENROUTE_PICKUP
  Seller App (BPP)-->>Buyer App (BAP): /on_status (unsolicited): order.status ACTIVE; fulfillment state RIDE_ARRIVED_PICKUP
  Buyer App (BAP)->>Seller App (BPP): /cancel (descriptor SOFT_CANCEL, reason None)
  Seller App (BPP)-->>Buyer App (BAP): /on_cancel (order.status SOFT_CANCEL; fulfillment state RIDE_ARRIVED_PICKUP, cancelled_by CONSUMER)
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
  Seller App (BPP)-->>Buyer App (BAP): /on_confirm (order.status ACTIVE; fulfillment state RIDE_ASSIGNED)
  Seller App (BPP)-->>Buyer App (BAP): /on_status (unsolicited): order.status ACTIVE; fulfillment state RIDE_ENROUTE_PICKUP
  Seller App (BPP)-->>Buyer App (BAP): /on_status (unsolicited): order.status ACTIVE; fulfillment state RIDE_ARRIVED_PICKUP
  Buyer App (BAP)->>Seller App (BPP): /cancel (descriptor SOFT_CANCEL, reason None)
  Seller App (BPP)-->>Buyer App (BAP): /on_cancel (order.status SOFT_CANCEL; fulfillment state RIDE_ARRIVED_PICKUP, cancelled_by CONSUMER)
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
  Seller App (BPP)-->>Buyer App (BAP): /on_confirm (order.status ACTIVE; fulfillment state RIDE_ASSIGNED)
  Seller App (BPP)-->>Buyer App (BAP): /on_status (unsolicited): order.status ACTIVE; fulfillment state RIDE_ENROUTE_PICKUP
  Seller App (BPP)-->>Buyer App (BAP): /on_status (unsolicited): order.status ACTIVE; fulfillment state RIDE_ARRIVED_PICKUP
  Buyer App (BAP)->>Seller App (BPP): /cancel (descriptor SOFT_CANCEL, reason None)
  Seller App (BPP)-->>Buyer App (BAP): /on_cancel (order.status SOFT_CANCEL; fulfillment state RIDE_ARRIVED_PICKUP, cancelled_by CONSUMER)
  Buyer App (BAP)->>Seller App (BPP): /cancel (descriptor CONFIRM_CANCEL, reason None)
  Seller App (BPP)-->>Buyer App (BAP): /on_cancel (order.status CANCELLED; fulfillment state RIDE_CANCELLED, cancelled_by CONSUMER)
```

## on_confirm_ride

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
  Seller App (BPP)-->>Buyer App (BAP): /on_confirm (order.status ACTIVE; fulfillment state RIDE_ASSIGNED)
  end
  Seller App (BPP)-->>Buyer App (BAP): /on_status (unsolicited): order.status ACTIVE; fulfillment state RIDE_ENROUTE_PICKUP
  Seller App (BPP)-->>Buyer App (BAP): /on_status (unsolicited): order.status ACTIVE; fulfillment state RIDE_ARRIVED_PICKUP
  Buyer App (BAP)->>Seller App (BPP): /cancel (descriptor SOFT_CANCEL, reason None)
  Seller App (BPP)-->>Buyer App (BAP): /on_cancel (order.status SOFT_CANCEL; fulfillment state RIDE_ARRIVED_PICKUP, cancelled_by CONSUMER)
  Buyer App (BAP)->>Seller App (BPP): /cancel (descriptor CONFIRM_CANCEL, reason None)
  Seller App (BPP)-->>Buyer App (BAP): /on_cancel (order.status CANCELLED; fulfillment state RIDE_CANCELLED, cancelled_by CONSUMER)
```

## on_status_unsolicited

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
  Seller App (BPP)-->>Buyer App (BAP): /on_confirm (order.status ACTIVE; fulfillment state RIDE_ASSIGNED)
  rect rgb(191, 223, 255)
  Seller App (BPP)-->>Buyer App (BAP): /on_status (unsolicited): order.status ACTIVE; fulfillment state RIDE_ENROUTE_PICKUP
  end
  Seller App (BPP)-->>Buyer App (BAP): /on_status (unsolicited): order.status ACTIVE; fulfillment state RIDE_ARRIVED_PICKUP
  Buyer App (BAP)->>Seller App (BPP): /cancel (descriptor SOFT_CANCEL, reason None)
  Seller App (BPP)-->>Buyer App (BAP): /on_cancel (order.status SOFT_CANCEL; fulfillment state RIDE_ARRIVED_PICKUP, cancelled_by CONSUMER)
  Buyer App (BAP)->>Seller App (BPP): /cancel (descriptor CONFIRM_CANCEL, reason None)
  Seller App (BPP)-->>Buyer App (BAP): /on_cancel (order.status CANCELLED; fulfillment state RIDE_CANCELLED, cancelled_by CONSUMER)
```

## on_status_ride_arrived

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
  Seller App (BPP)-->>Buyer App (BAP): /on_confirm (order.status ACTIVE; fulfillment state RIDE_ASSIGNED)
  Seller App (BPP)-->>Buyer App (BAP): /on_status (unsolicited): order.status ACTIVE; fulfillment state RIDE_ENROUTE_PICKUP
  rect rgb(191, 223, 255)
  Seller App (BPP)-->>Buyer App (BAP): /on_status (unsolicited): order.status ACTIVE; fulfillment state RIDE_ARRIVED_PICKUP
  end
  Buyer App (BAP)->>Seller App (BPP): /cancel (descriptor SOFT_CANCEL, reason None)
  Seller App (BPP)-->>Buyer App (BAP): /on_cancel (order.status SOFT_CANCEL; fulfillment state RIDE_ARRIVED_PICKUP, cancelled_by CONSUMER)
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
  Seller App (BPP)-->>Buyer App (BAP): /on_confirm (order.status ACTIVE; fulfillment state RIDE_ASSIGNED)
  Seller App (BPP)-->>Buyer App (BAP): /on_status (unsolicited): order.status ACTIVE; fulfillment state RIDE_ENROUTE_PICKUP
  Seller App (BPP)-->>Buyer App (BAP): /on_status (unsolicited): order.status ACTIVE; fulfillment state RIDE_ARRIVED_PICKUP
  rect rgb(191, 223, 255)
  Buyer App (BAP)->>Seller App (BPP): /cancel (descriptor SOFT_CANCEL, reason None)
  end
  Seller App (BPP)-->>Buyer App (BAP): /on_cancel (order.status SOFT_CANCEL; fulfillment state RIDE_ARRIVED_PICKUP, cancelled_by CONSUMER)
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
  Seller App (BPP)-->>Buyer App (BAP): /on_confirm (order.status ACTIVE; fulfillment state RIDE_ASSIGNED)
  Seller App (BPP)-->>Buyer App (BAP): /on_status (unsolicited): order.status ACTIVE; fulfillment state RIDE_ENROUTE_PICKUP
  Seller App (BPP)-->>Buyer App (BAP): /on_status (unsolicited): order.status ACTIVE; fulfillment state RIDE_ARRIVED_PICKUP
  Buyer App (BAP)->>Seller App (BPP): /cancel (descriptor SOFT_CANCEL, reason None)
  rect rgb(191, 223, 255)
  Seller App (BPP)-->>Buyer App (BAP): /on_cancel (order.status SOFT_CANCEL; fulfillment state RIDE_ARRIVED_PICKUP, cancelled_by CONSUMER)
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
  Seller App (BPP)-->>Buyer App (BAP): /on_confirm (order.status ACTIVE; fulfillment state RIDE_ASSIGNED)
  Seller App (BPP)-->>Buyer App (BAP): /on_status (unsolicited): order.status ACTIVE; fulfillment state RIDE_ENROUTE_PICKUP
  Seller App (BPP)-->>Buyer App (BAP): /on_status (unsolicited): order.status ACTIVE; fulfillment state RIDE_ARRIVED_PICKUP
  Buyer App (BAP)->>Seller App (BPP): /cancel (descriptor SOFT_CANCEL, reason None)
  Seller App (BPP)-->>Buyer App (BAP): /on_cancel (order.status SOFT_CANCEL; fulfillment state RIDE_ARRIVED_PICKUP, cancelled_by CONSUMER)
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
  Seller App (BPP)-->>Buyer App (BAP): /on_confirm (order.status ACTIVE; fulfillment state RIDE_ASSIGNED)
  Seller App (BPP)-->>Buyer App (BAP): /on_status (unsolicited): order.status ACTIVE; fulfillment state RIDE_ENROUTE_PICKUP
  Seller App (BPP)-->>Buyer App (BAP): /on_status (unsolicited): order.status ACTIVE; fulfillment state RIDE_ARRIVED_PICKUP
  Buyer App (BAP)->>Seller App (BPP): /cancel (descriptor SOFT_CANCEL, reason None)
  Seller App (BPP)-->>Buyer App (BAP): /on_cancel (order.status SOFT_CANCEL; fulfillment state RIDE_ARRIVED_PICKUP, cancelled_by CONSUMER)
  Buyer App (BAP)->>Seller App (BPP): /cancel (descriptor CONFIRM_CANCEL, reason None)
  rect rgb(191, 223, 255)
  Seller App (BPP)-->>Buyer App (BAP): /on_cancel (order.status CANCELLED; fulfillment state RIDE_CANCELLED, cancelled_by CONSUMER)
  end
```

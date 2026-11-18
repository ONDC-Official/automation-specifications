# Buyer Delivery — Sequence Diagrams

Internal data file consumed by the Developer Guide's "Sequence Diagram" tab (API Walkthrough).
Not meant to be shown as its own docs page — the frontend filters this slug out of the Use Case
Brief / Additional Resources / Changelog tab lists and instead looks up the section matching the
selected API call's `action_id` (the `##` heading below) to render that step's diagram.

One `## <action_id>` heading per step of `BUYER_DELIVERY.yaml`, in that flow's own step order, each followed by its Mermaid `sequenceDiagram`: the whole flow, with that call's own message(s) highlighted — same convention as the other domains' per-step sequence-diagram docs.

## select

```mermaid
sequenceDiagram
  participant Buyer App (BAP)
  participant Seller App (BPP)
  rect rgb(191, 223, 255)
  Buyer App (BAP)->>Seller App (BPP): /select (items, store, delivery location)
  end
  Seller App (BPP)-->>Buyer App (BAP): /on_select (quote, TAT)
  Buyer App (BAP)->>Seller App (BPP): /init (address, billing)
  Seller App (BPP)-->>Buyer App (BAP): /on_init (final quote, payment terms)
  Buyer App (BAP)->>Seller App (BPP): /confirm (place order)
  Seller App (BPP)-->>Buyer App (BAP): /on_confirm (order Created)
  Seller App (BPP)-->>Buyer App (BAP): /on_status (unsolicited): Pending
  Seller App (BPP)-->>Buyer App (BAP): /on_status (unsolicited): Packed
  Buyer App (BAP)->>Seller App (BPP): /update (buyer delivery: agent assigned)
  Seller App (BPP)-->>Buyer App (BAP): /on_update (agent assignment acknowledged)
  Buyer App (BAP)->>Seller App (BPP): /update (interim buyer delivery update)
  Seller App (BPP)-->>Buyer App (BAP): /on_update (interim update acknowledged)
  Buyer App (BAP)->>Seller App (BPP): /update (buyer delivery: out for delivery)
  Seller App (BPP)-->>Buyer App (BAP): /on_update (out for delivery acknowledged)
  Buyer App (BAP)->>Seller App (BPP): /update (delivered by buyer's courier)
  Seller App (BPP)-->>Buyer App (BAP): /on_update (order completed)
```

## on_select_multiple_fulfillment

```mermaid
sequenceDiagram
  participant Buyer App (BAP)
  participant Seller App (BPP)
  Buyer App (BAP)->>Seller App (BPP): /select (items, store, delivery location)
  rect rgb(191, 223, 255)
  Seller App (BPP)-->>Buyer App (BAP): /on_select (quote, TAT)
  end
  Buyer App (BAP)->>Seller App (BPP): /init (address, billing)
  Seller App (BPP)-->>Buyer App (BAP): /on_init (final quote, payment terms)
  Buyer App (BAP)->>Seller App (BPP): /confirm (place order)
  Seller App (BPP)-->>Buyer App (BAP): /on_confirm (order Created)
  Seller App (BPP)-->>Buyer App (BAP): /on_status (unsolicited): Pending
  Seller App (BPP)-->>Buyer App (BAP): /on_status (unsolicited): Packed
  Buyer App (BAP)->>Seller App (BPP): /update (buyer delivery: agent assigned)
  Seller App (BPP)-->>Buyer App (BAP): /on_update (agent assignment acknowledged)
  Buyer App (BAP)->>Seller App (BPP): /update (interim buyer delivery update)
  Seller App (BPP)-->>Buyer App (BAP): /on_update (interim update acknowledged)
  Buyer App (BAP)->>Seller App (BPP): /update (buyer delivery: out for delivery)
  Seller App (BPP)-->>Buyer App (BAP): /on_update (out for delivery acknowledged)
  Buyer App (BAP)->>Seller App (BPP): /update (delivered by buyer's courier)
  Seller App (BPP)-->>Buyer App (BAP): /on_update (order completed)
```

## init

```mermaid
sequenceDiagram
  participant Buyer App (BAP)
  participant Seller App (BPP)
  Buyer App (BAP)->>Seller App (BPP): /select (items, store, delivery location)
  Seller App (BPP)-->>Buyer App (BAP): /on_select (quote, TAT)
  rect rgb(191, 223, 255)
  Buyer App (BAP)->>Seller App (BPP): /init (address, billing)
  end
  Seller App (BPP)-->>Buyer App (BAP): /on_init (final quote, payment terms)
  Buyer App (BAP)->>Seller App (BPP): /confirm (place order)
  Seller App (BPP)-->>Buyer App (BAP): /on_confirm (order Created)
  Seller App (BPP)-->>Buyer App (BAP): /on_status (unsolicited): Pending
  Seller App (BPP)-->>Buyer App (BAP): /on_status (unsolicited): Packed
  Buyer App (BAP)->>Seller App (BPP): /update (buyer delivery: agent assigned)
  Seller App (BPP)-->>Buyer App (BAP): /on_update (agent assignment acknowledged)
  Buyer App (BAP)->>Seller App (BPP): /update (interim buyer delivery update)
  Seller App (BPP)-->>Buyer App (BAP): /on_update (interim update acknowledged)
  Buyer App (BAP)->>Seller App (BPP): /update (buyer delivery: out for delivery)
  Seller App (BPP)-->>Buyer App (BAP): /on_update (out for delivery acknowledged)
  Buyer App (BAP)->>Seller App (BPP): /update (delivered by buyer's courier)
  Seller App (BPP)-->>Buyer App (BAP): /on_update (order completed)
```

## on_init

```mermaid
sequenceDiagram
  participant Buyer App (BAP)
  participant Seller App (BPP)
  Buyer App (BAP)->>Seller App (BPP): /select (items, store, delivery location)
  Seller App (BPP)-->>Buyer App (BAP): /on_select (quote, TAT)
  Buyer App (BAP)->>Seller App (BPP): /init (address, billing)
  rect rgb(191, 223, 255)
  Seller App (BPP)-->>Buyer App (BAP): /on_init (final quote, payment terms)
  end
  Buyer App (BAP)->>Seller App (BPP): /confirm (place order)
  Seller App (BPP)-->>Buyer App (BAP): /on_confirm (order Created)
  Seller App (BPP)-->>Buyer App (BAP): /on_status (unsolicited): Pending
  Seller App (BPP)-->>Buyer App (BAP): /on_status (unsolicited): Packed
  Buyer App (BAP)->>Seller App (BPP): /update (buyer delivery: agent assigned)
  Seller App (BPP)-->>Buyer App (BAP): /on_update (agent assignment acknowledged)
  Buyer App (BAP)->>Seller App (BPP): /update (interim buyer delivery update)
  Seller App (BPP)-->>Buyer App (BAP): /on_update (interim update acknowledged)
  Buyer App (BAP)->>Seller App (BPP): /update (buyer delivery: out for delivery)
  Seller App (BPP)-->>Buyer App (BAP): /on_update (out for delivery acknowledged)
  Buyer App (BAP)->>Seller App (BPP): /update (delivered by buyer's courier)
  Seller App (BPP)-->>Buyer App (BAP): /on_update (order completed)
```

## confirm

```mermaid
sequenceDiagram
  participant Buyer App (BAP)
  participant Seller App (BPP)
  Buyer App (BAP)->>Seller App (BPP): /select (items, store, delivery location)
  Seller App (BPP)-->>Buyer App (BAP): /on_select (quote, TAT)
  Buyer App (BAP)->>Seller App (BPP): /init (address, billing)
  Seller App (BPP)-->>Buyer App (BAP): /on_init (final quote, payment terms)
  rect rgb(191, 223, 255)
  Buyer App (BAP)->>Seller App (BPP): /confirm (place order)
  end
  Seller App (BPP)-->>Buyer App (BAP): /on_confirm (order Created)
  Seller App (BPP)-->>Buyer App (BAP): /on_status (unsolicited): Pending
  Seller App (BPP)-->>Buyer App (BAP): /on_status (unsolicited): Packed
  Buyer App (BAP)->>Seller App (BPP): /update (buyer delivery: agent assigned)
  Seller App (BPP)-->>Buyer App (BAP): /on_update (agent assignment acknowledged)
  Buyer App (BAP)->>Seller App (BPP): /update (interim buyer delivery update)
  Seller App (BPP)-->>Buyer App (BAP): /on_update (interim update acknowledged)
  Buyer App (BAP)->>Seller App (BPP): /update (buyer delivery: out for delivery)
  Seller App (BPP)-->>Buyer App (BAP): /on_update (out for delivery acknowledged)
  Buyer App (BAP)->>Seller App (BPP): /update (delivered by buyer's courier)
  Seller App (BPP)-->>Buyer App (BAP): /on_update (order completed)
```

## on_confirm

```mermaid
sequenceDiagram
  participant Buyer App (BAP)
  participant Seller App (BPP)
  Buyer App (BAP)->>Seller App (BPP): /select (items, store, delivery location)
  Seller App (BPP)-->>Buyer App (BAP): /on_select (quote, TAT)
  Buyer App (BAP)->>Seller App (BPP): /init (address, billing)
  Seller App (BPP)-->>Buyer App (BAP): /on_init (final quote, payment terms)
  Buyer App (BAP)->>Seller App (BPP): /confirm (place order)
  rect rgb(191, 223, 255)
  Seller App (BPP)-->>Buyer App (BAP): /on_confirm (order Created)
  end
  Seller App (BPP)-->>Buyer App (BAP): /on_status (unsolicited): Pending
  Seller App (BPP)-->>Buyer App (BAP): /on_status (unsolicited): Packed
  Buyer App (BAP)->>Seller App (BPP): /update (buyer delivery: agent assigned)
  Seller App (BPP)-->>Buyer App (BAP): /on_update (agent assignment acknowledged)
  Buyer App (BAP)->>Seller App (BPP): /update (interim buyer delivery update)
  Seller App (BPP)-->>Buyer App (BAP): /on_update (interim update acknowledged)
  Buyer App (BAP)->>Seller App (BPP): /update (buyer delivery: out for delivery)
  Seller App (BPP)-->>Buyer App (BAP): /on_update (out for delivery acknowledged)
  Buyer App (BAP)->>Seller App (BPP): /update (delivered by buyer's courier)
  Seller App (BPP)-->>Buyer App (BAP): /on_update (order completed)
```

## on_status_pending

```mermaid
sequenceDiagram
  participant Buyer App (BAP)
  participant Seller App (BPP)
  Buyer App (BAP)->>Seller App (BPP): /select (items, store, delivery location)
  Seller App (BPP)-->>Buyer App (BAP): /on_select (quote, TAT)
  Buyer App (BAP)->>Seller App (BPP): /init (address, billing)
  Seller App (BPP)-->>Buyer App (BAP): /on_init (final quote, payment terms)
  Buyer App (BAP)->>Seller App (BPP): /confirm (place order)
  Seller App (BPP)-->>Buyer App (BAP): /on_confirm (order Created)
  rect rgb(191, 223, 255)
  Seller App (BPP)-->>Buyer App (BAP): /on_status (unsolicited): Pending
  end
  Seller App (BPP)-->>Buyer App (BAP): /on_status (unsolicited): Packed
  Buyer App (BAP)->>Seller App (BPP): /update (buyer delivery: agent assigned)
  Seller App (BPP)-->>Buyer App (BAP): /on_update (agent assignment acknowledged)
  Buyer App (BAP)->>Seller App (BPP): /update (interim buyer delivery update)
  Seller App (BPP)-->>Buyer App (BAP): /on_update (interim update acknowledged)
  Buyer App (BAP)->>Seller App (BPP): /update (buyer delivery: out for delivery)
  Seller App (BPP)-->>Buyer App (BAP): /on_update (out for delivery acknowledged)
  Buyer App (BAP)->>Seller App (BPP): /update (delivered by buyer's courier)
  Seller App (BPP)-->>Buyer App (BAP): /on_update (order completed)
```

## on_status_packed

```mermaid
sequenceDiagram
  participant Buyer App (BAP)
  participant Seller App (BPP)
  Buyer App (BAP)->>Seller App (BPP): /select (items, store, delivery location)
  Seller App (BPP)-->>Buyer App (BAP): /on_select (quote, TAT)
  Buyer App (BAP)->>Seller App (BPP): /init (address, billing)
  Seller App (BPP)-->>Buyer App (BAP): /on_init (final quote, payment terms)
  Buyer App (BAP)->>Seller App (BPP): /confirm (place order)
  Seller App (BPP)-->>Buyer App (BAP): /on_confirm (order Created)
  Seller App (BPP)-->>Buyer App (BAP): /on_status (unsolicited): Pending
  rect rgb(191, 223, 255)
  Seller App (BPP)-->>Buyer App (BAP): /on_status (unsolicited): Packed
  end
  Buyer App (BAP)->>Seller App (BPP): /update (buyer delivery: agent assigned)
  Seller App (BPP)-->>Buyer App (BAP): /on_update (agent assignment acknowledged)
  Buyer App (BAP)->>Seller App (BPP): /update (interim buyer delivery update)
  Seller App (BPP)-->>Buyer App (BAP): /on_update (interim update acknowledged)
  Buyer App (BAP)->>Seller App (BPP): /update (buyer delivery: out for delivery)
  Seller App (BPP)-->>Buyer App (BAP): /on_update (out for delivery acknowledged)
  Buyer App (BAP)->>Seller App (BPP): /update (delivered by buyer's courier)
  Seller App (BPP)-->>Buyer App (BAP): /on_update (order completed)
```

## update_buyer_delivery_agent_assigned

```mermaid
sequenceDiagram
  participant Buyer App (BAP)
  participant Seller App (BPP)
  Buyer App (BAP)->>Seller App (BPP): /select (items, store, delivery location)
  Seller App (BPP)-->>Buyer App (BAP): /on_select (quote, TAT)
  Buyer App (BAP)->>Seller App (BPP): /init (address, billing)
  Seller App (BPP)-->>Buyer App (BAP): /on_init (final quote, payment terms)
  Buyer App (BAP)->>Seller App (BPP): /confirm (place order)
  Seller App (BPP)-->>Buyer App (BAP): /on_confirm (order Created)
  Seller App (BPP)-->>Buyer App (BAP): /on_status (unsolicited): Pending
  Seller App (BPP)-->>Buyer App (BAP): /on_status (unsolicited): Packed
  rect rgb(191, 223, 255)
  Buyer App (BAP)->>Seller App (BPP): /update (buyer delivery: agent assigned)
  end
  Seller App (BPP)-->>Buyer App (BAP): /on_update (agent assignment acknowledged)
  Buyer App (BAP)->>Seller App (BPP): /update (interim buyer delivery update)
  Seller App (BPP)-->>Buyer App (BAP): /on_update (interim update acknowledged)
  Buyer App (BAP)->>Seller App (BPP): /update (buyer delivery: out for delivery)
  Seller App (BPP)-->>Buyer App (BAP): /on_update (out for delivery acknowledged)
  Buyer App (BAP)->>Seller App (BPP): /update (delivered by buyer's courier)
  Seller App (BPP)-->>Buyer App (BAP): /on_update (order completed)
```

## on_update_buyer_delivery_agent_assigned

```mermaid
sequenceDiagram
  participant Buyer App (BAP)
  participant Seller App (BPP)
  Buyer App (BAP)->>Seller App (BPP): /select (items, store, delivery location)
  Seller App (BPP)-->>Buyer App (BAP): /on_select (quote, TAT)
  Buyer App (BAP)->>Seller App (BPP): /init (address, billing)
  Seller App (BPP)-->>Buyer App (BAP): /on_init (final quote, payment terms)
  Buyer App (BAP)->>Seller App (BPP): /confirm (place order)
  Seller App (BPP)-->>Buyer App (BAP): /on_confirm (order Created)
  Seller App (BPP)-->>Buyer App (BAP): /on_status (unsolicited): Pending
  Seller App (BPP)-->>Buyer App (BAP): /on_status (unsolicited): Packed
  Buyer App (BAP)->>Seller App (BPP): /update (buyer delivery: agent assigned)
  rect rgb(191, 223, 255)
  Seller App (BPP)-->>Buyer App (BAP): /on_update (agent assignment acknowledged)
  end
  Buyer App (BAP)->>Seller App (BPP): /update (interim buyer delivery update)
  Seller App (BPP)-->>Buyer App (BAP): /on_update (interim update acknowledged)
  Buyer App (BAP)->>Seller App (BPP): /update (buyer delivery: out for delivery)
  Seller App (BPP)-->>Buyer App (BAP): /on_update (out for delivery acknowledged)
  Buyer App (BAP)->>Seller App (BPP): /update (delivered by buyer's courier)
  Seller App (BPP)-->>Buyer App (BAP): /on_update (order completed)
```

## update_buyer_delivery_intermin

```mermaid
sequenceDiagram
  participant Buyer App (BAP)
  participant Seller App (BPP)
  Buyer App (BAP)->>Seller App (BPP): /select (items, store, delivery location)
  Seller App (BPP)-->>Buyer App (BAP): /on_select (quote, TAT)
  Buyer App (BAP)->>Seller App (BPP): /init (address, billing)
  Seller App (BPP)-->>Buyer App (BAP): /on_init (final quote, payment terms)
  Buyer App (BAP)->>Seller App (BPP): /confirm (place order)
  Seller App (BPP)-->>Buyer App (BAP): /on_confirm (order Created)
  Seller App (BPP)-->>Buyer App (BAP): /on_status (unsolicited): Pending
  Seller App (BPP)-->>Buyer App (BAP): /on_status (unsolicited): Packed
  Buyer App (BAP)->>Seller App (BPP): /update (buyer delivery: agent assigned)
  Seller App (BPP)-->>Buyer App (BAP): /on_update (agent assignment acknowledged)
  rect rgb(191, 223, 255)
  Buyer App (BAP)->>Seller App (BPP): /update (interim buyer delivery update)
  end
  Seller App (BPP)-->>Buyer App (BAP): /on_update (interim update acknowledged)
  Buyer App (BAP)->>Seller App (BPP): /update (buyer delivery: out for delivery)
  Seller App (BPP)-->>Buyer App (BAP): /on_update (out for delivery acknowledged)
  Buyer App (BAP)->>Seller App (BPP): /update (delivered by buyer's courier)
  Seller App (BPP)-->>Buyer App (BAP): /on_update (order completed)
```

## on_update_buyer_delivery_intermin

```mermaid
sequenceDiagram
  participant Buyer App (BAP)
  participant Seller App (BPP)
  Buyer App (BAP)->>Seller App (BPP): /select (items, store, delivery location)
  Seller App (BPP)-->>Buyer App (BAP): /on_select (quote, TAT)
  Buyer App (BAP)->>Seller App (BPP): /init (address, billing)
  Seller App (BPP)-->>Buyer App (BAP): /on_init (final quote, payment terms)
  Buyer App (BAP)->>Seller App (BPP): /confirm (place order)
  Seller App (BPP)-->>Buyer App (BAP): /on_confirm (order Created)
  Seller App (BPP)-->>Buyer App (BAP): /on_status (unsolicited): Pending
  Seller App (BPP)-->>Buyer App (BAP): /on_status (unsolicited): Packed
  Buyer App (BAP)->>Seller App (BPP): /update (buyer delivery: agent assigned)
  Seller App (BPP)-->>Buyer App (BAP): /on_update (agent assignment acknowledged)
  Buyer App (BAP)->>Seller App (BPP): /update (interim buyer delivery update)
  rect rgb(191, 223, 255)
  Seller App (BPP)-->>Buyer App (BAP): /on_update (interim update acknowledged)
  end
  Buyer App (BAP)->>Seller App (BPP): /update (buyer delivery: out for delivery)
  Seller App (BPP)-->>Buyer App (BAP): /on_update (out for delivery acknowledged)
  Buyer App (BAP)->>Seller App (BPP): /update (delivered by buyer's courier)
  Seller App (BPP)-->>Buyer App (BAP): /on_update (order completed)
```

## update_buyer_delivery_out_for_delivery

```mermaid
sequenceDiagram
  participant Buyer App (BAP)
  participant Seller App (BPP)
  Buyer App (BAP)->>Seller App (BPP): /select (items, store, delivery location)
  Seller App (BPP)-->>Buyer App (BAP): /on_select (quote, TAT)
  Buyer App (BAP)->>Seller App (BPP): /init (address, billing)
  Seller App (BPP)-->>Buyer App (BAP): /on_init (final quote, payment terms)
  Buyer App (BAP)->>Seller App (BPP): /confirm (place order)
  Seller App (BPP)-->>Buyer App (BAP): /on_confirm (order Created)
  Seller App (BPP)-->>Buyer App (BAP): /on_status (unsolicited): Pending
  Seller App (BPP)-->>Buyer App (BAP): /on_status (unsolicited): Packed
  Buyer App (BAP)->>Seller App (BPP): /update (buyer delivery: agent assigned)
  Seller App (BPP)-->>Buyer App (BAP): /on_update (agent assignment acknowledged)
  Buyer App (BAP)->>Seller App (BPP): /update (interim buyer delivery update)
  Seller App (BPP)-->>Buyer App (BAP): /on_update (interim update acknowledged)
  rect rgb(191, 223, 255)
  Buyer App (BAP)->>Seller App (BPP): /update (buyer delivery: out for delivery)
  end
  Seller App (BPP)-->>Buyer App (BAP): /on_update (out for delivery acknowledged)
  Buyer App (BAP)->>Seller App (BPP): /update (delivered by buyer's courier)
  Seller App (BPP)-->>Buyer App (BAP): /on_update (order completed)
```

## on_update_buyer_delivery_out_for_delivery

```mermaid
sequenceDiagram
  participant Buyer App (BAP)
  participant Seller App (BPP)
  Buyer App (BAP)->>Seller App (BPP): /select (items, store, delivery location)
  Seller App (BPP)-->>Buyer App (BAP): /on_select (quote, TAT)
  Buyer App (BAP)->>Seller App (BPP): /init (address, billing)
  Seller App (BPP)-->>Buyer App (BAP): /on_init (final quote, payment terms)
  Buyer App (BAP)->>Seller App (BPP): /confirm (place order)
  Seller App (BPP)-->>Buyer App (BAP): /on_confirm (order Created)
  Seller App (BPP)-->>Buyer App (BAP): /on_status (unsolicited): Pending
  Seller App (BPP)-->>Buyer App (BAP): /on_status (unsolicited): Packed
  Buyer App (BAP)->>Seller App (BPP): /update (buyer delivery: agent assigned)
  Seller App (BPP)-->>Buyer App (BAP): /on_update (agent assignment acknowledged)
  Buyer App (BAP)->>Seller App (BPP): /update (interim buyer delivery update)
  Seller App (BPP)-->>Buyer App (BAP): /on_update (interim update acknowledged)
  Buyer App (BAP)->>Seller App (BPP): /update (buyer delivery: out for delivery)
  rect rgb(191, 223, 255)
  Seller App (BPP)-->>Buyer App (BAP): /on_update (out for delivery acknowledged)
  end
  Buyer App (BAP)->>Seller App (BPP): /update (delivered by buyer's courier)
  Seller App (BPP)-->>Buyer App (BAP): /on_update (order completed)
```

## update_buyer_delivery_final

```mermaid
sequenceDiagram
  participant Buyer App (BAP)
  participant Seller App (BPP)
  Buyer App (BAP)->>Seller App (BPP): /select (items, store, delivery location)
  Seller App (BPP)-->>Buyer App (BAP): /on_select (quote, TAT)
  Buyer App (BAP)->>Seller App (BPP): /init (address, billing)
  Seller App (BPP)-->>Buyer App (BAP): /on_init (final quote, payment terms)
  Buyer App (BAP)->>Seller App (BPP): /confirm (place order)
  Seller App (BPP)-->>Buyer App (BAP): /on_confirm (order Created)
  Seller App (BPP)-->>Buyer App (BAP): /on_status (unsolicited): Pending
  Seller App (BPP)-->>Buyer App (BAP): /on_status (unsolicited): Packed
  Buyer App (BAP)->>Seller App (BPP): /update (buyer delivery: agent assigned)
  Seller App (BPP)-->>Buyer App (BAP): /on_update (agent assignment acknowledged)
  Buyer App (BAP)->>Seller App (BPP): /update (interim buyer delivery update)
  Seller App (BPP)-->>Buyer App (BAP): /on_update (interim update acknowledged)
  Buyer App (BAP)->>Seller App (BPP): /update (buyer delivery: out for delivery)
  Seller App (BPP)-->>Buyer App (BAP): /on_update (out for delivery acknowledged)
  rect rgb(191, 223, 255)
  Buyer App (BAP)->>Seller App (BPP): /update (delivered by buyer's courier)
  end
  Seller App (BPP)-->>Buyer App (BAP): /on_update (order completed)
```

## on_update_buyer_delivery_final

```mermaid
sequenceDiagram
  participant Buyer App (BAP)
  participant Seller App (BPP)
  Buyer App (BAP)->>Seller App (BPP): /select (items, store, delivery location)
  Seller App (BPP)-->>Buyer App (BAP): /on_select (quote, TAT)
  Buyer App (BAP)->>Seller App (BPP): /init (address, billing)
  Seller App (BPP)-->>Buyer App (BAP): /on_init (final quote, payment terms)
  Buyer App (BAP)->>Seller App (BPP): /confirm (place order)
  Seller App (BPP)-->>Buyer App (BAP): /on_confirm (order Created)
  Seller App (BPP)-->>Buyer App (BAP): /on_status (unsolicited): Pending
  Seller App (BPP)-->>Buyer App (BAP): /on_status (unsolicited): Packed
  Buyer App (BAP)->>Seller App (BPP): /update (buyer delivery: agent assigned)
  Seller App (BPP)-->>Buyer App (BAP): /on_update (agent assignment acknowledged)
  Buyer App (BAP)->>Seller App (BPP): /update (interim buyer delivery update)
  Seller App (BPP)-->>Buyer App (BAP): /on_update (interim update acknowledged)
  Buyer App (BAP)->>Seller App (BPP): /update (buyer delivery: out for delivery)
  Seller App (BPP)-->>Buyer App (BAP): /on_update (out for delivery acknowledged)
  Buyer App (BAP)->>Seller App (BPP): /update (delivered by buyer's courier)
  rect rgb(191, 223, 255)
  Seller App (BPP)-->>Buyer App (BAP): /on_update (order completed)
  end
```

# Return Flow — Sequence Diagrams

Internal data file consumed by the Developer Guide's "Sequence Diagram" tab (API Walkthrough).
Not meant to be shown as its own docs page — the frontend filters this slug out of the Use Case
Brief / Additional Resources / Changelog tab lists and instead looks up the section matching the
selected API call's `action_id` (the `##` heading below) to render that step's diagram.

One `## <action_id>` heading per step of `RETURN_FLOW.yaml`, in that flow's own step order, each followed by its Mermaid `sequenceDiagram`: the whole flow, with that call's own message(s) highlighted — same convention as the other domains' per-step sequence-diagram docs.

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
  Seller App (BPP)-->>Buyer App (BAP): /on_status (unsolicited): Agent-assigned
  Seller App (BPP)-->>Buyer App (BAP): /on_status (unsolicited): At-pickup
  Seller App (BPP)-->>Buyer App (BAP): /on_status (unsolicited): Order-picked-up
  Seller App (BPP)-->>Buyer App (BAP): /on_status (unsolicited): At-delivery
  Seller App (BPP)-->>Buyer App (BAP): /on_status (unsolicited): Order-delivered
  Buyer App (BAP)->>Seller App (BPP): /update (return request: item, quantity, reason)
  Seller App (BPP)-->>Buyer App (BAP): /on_update (return in progress)
  Seller App (BPP)-->>Buyer App (BAP): /on_update (unsolicited): return completed
  Buyer App (BAP)->>Seller App (BPP): /update (settlement for return refund)
```

## on_select

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
  Seller App (BPP)-->>Buyer App (BAP): /on_status (unsolicited): Agent-assigned
  Seller App (BPP)-->>Buyer App (BAP): /on_status (unsolicited): At-pickup
  Seller App (BPP)-->>Buyer App (BAP): /on_status (unsolicited): Order-picked-up
  Seller App (BPP)-->>Buyer App (BAP): /on_status (unsolicited): At-delivery
  Seller App (BPP)-->>Buyer App (BAP): /on_status (unsolicited): Order-delivered
  Buyer App (BAP)->>Seller App (BPP): /update (return request: item, quantity, reason)
  Seller App (BPP)-->>Buyer App (BAP): /on_update (return in progress)
  Seller App (BPP)-->>Buyer App (BAP): /on_update (unsolicited): return completed
  Buyer App (BAP)->>Seller App (BPP): /update (settlement for return refund)
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
  Seller App (BPP)-->>Buyer App (BAP): /on_status (unsolicited): Agent-assigned
  Seller App (BPP)-->>Buyer App (BAP): /on_status (unsolicited): At-pickup
  Seller App (BPP)-->>Buyer App (BAP): /on_status (unsolicited): Order-picked-up
  Seller App (BPP)-->>Buyer App (BAP): /on_status (unsolicited): At-delivery
  Seller App (BPP)-->>Buyer App (BAP): /on_status (unsolicited): Order-delivered
  Buyer App (BAP)->>Seller App (BPP): /update (return request: item, quantity, reason)
  Seller App (BPP)-->>Buyer App (BAP): /on_update (return in progress)
  Seller App (BPP)-->>Buyer App (BAP): /on_update (unsolicited): return completed
  Buyer App (BAP)->>Seller App (BPP): /update (settlement for return refund)
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
  Seller App (BPP)-->>Buyer App (BAP): /on_status (unsolicited): Agent-assigned
  Seller App (BPP)-->>Buyer App (BAP): /on_status (unsolicited): At-pickup
  Seller App (BPP)-->>Buyer App (BAP): /on_status (unsolicited): Order-picked-up
  Seller App (BPP)-->>Buyer App (BAP): /on_status (unsolicited): At-delivery
  Seller App (BPP)-->>Buyer App (BAP): /on_status (unsolicited): Order-delivered
  Buyer App (BAP)->>Seller App (BPP): /update (return request: item, quantity, reason)
  Seller App (BPP)-->>Buyer App (BAP): /on_update (return in progress)
  Seller App (BPP)-->>Buyer App (BAP): /on_update (unsolicited): return completed
  Buyer App (BAP)->>Seller App (BPP): /update (settlement for return refund)
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
  Seller App (BPP)-->>Buyer App (BAP): /on_status (unsolicited): Agent-assigned
  Seller App (BPP)-->>Buyer App (BAP): /on_status (unsolicited): At-pickup
  Seller App (BPP)-->>Buyer App (BAP): /on_status (unsolicited): Order-picked-up
  Seller App (BPP)-->>Buyer App (BAP): /on_status (unsolicited): At-delivery
  Seller App (BPP)-->>Buyer App (BAP): /on_status (unsolicited): Order-delivered
  Buyer App (BAP)->>Seller App (BPP): /update (return request: item, quantity, reason)
  Seller App (BPP)-->>Buyer App (BAP): /on_update (return in progress)
  Seller App (BPP)-->>Buyer App (BAP): /on_update (unsolicited): return completed
  Buyer App (BAP)->>Seller App (BPP): /update (settlement for return refund)
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
  Seller App (BPP)-->>Buyer App (BAP): /on_status (unsolicited): Agent-assigned
  Seller App (BPP)-->>Buyer App (BAP): /on_status (unsolicited): At-pickup
  Seller App (BPP)-->>Buyer App (BAP): /on_status (unsolicited): Order-picked-up
  Seller App (BPP)-->>Buyer App (BAP): /on_status (unsolicited): At-delivery
  Seller App (BPP)-->>Buyer App (BAP): /on_status (unsolicited): Order-delivered
  Buyer App (BAP)->>Seller App (BPP): /update (return request: item, quantity, reason)
  Seller App (BPP)-->>Buyer App (BAP): /on_update (return in progress)
  Seller App (BPP)-->>Buyer App (BAP): /on_update (unsolicited): return completed
  Buyer App (BAP)->>Seller App (BPP): /update (settlement for return refund)
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
  Seller App (BPP)-->>Buyer App (BAP): /on_status (unsolicited): Agent-assigned
  Seller App (BPP)-->>Buyer App (BAP): /on_status (unsolicited): At-pickup
  Seller App (BPP)-->>Buyer App (BAP): /on_status (unsolicited): Order-picked-up
  Seller App (BPP)-->>Buyer App (BAP): /on_status (unsolicited): At-delivery
  Seller App (BPP)-->>Buyer App (BAP): /on_status (unsolicited): Order-delivered
  Buyer App (BAP)->>Seller App (BPP): /update (return request: item, quantity, reason)
  Seller App (BPP)-->>Buyer App (BAP): /on_update (return in progress)
  Seller App (BPP)-->>Buyer App (BAP): /on_update (unsolicited): return completed
  Buyer App (BAP)->>Seller App (BPP): /update (settlement for return refund)
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
  Seller App (BPP)-->>Buyer App (BAP): /on_status (unsolicited): Agent-assigned
  Seller App (BPP)-->>Buyer App (BAP): /on_status (unsolicited): At-pickup
  Seller App (BPP)-->>Buyer App (BAP): /on_status (unsolicited): Order-picked-up
  Seller App (BPP)-->>Buyer App (BAP): /on_status (unsolicited): At-delivery
  Seller App (BPP)-->>Buyer App (BAP): /on_status (unsolicited): Order-delivered
  Buyer App (BAP)->>Seller App (BPP): /update (return request: item, quantity, reason)
  Seller App (BPP)-->>Buyer App (BAP): /on_update (return in progress)
  Seller App (BPP)-->>Buyer App (BAP): /on_update (unsolicited): return completed
  Buyer App (BAP)->>Seller App (BPP): /update (settlement for return refund)
```

## on_status_agent_assigned

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
  Seller App (BPP)-->>Buyer App (BAP): /on_status (unsolicited): Agent-assigned
  end
  Seller App (BPP)-->>Buyer App (BAP): /on_status (unsolicited): At-pickup
  Seller App (BPP)-->>Buyer App (BAP): /on_status (unsolicited): Order-picked-up
  Seller App (BPP)-->>Buyer App (BAP): /on_status (unsolicited): At-delivery
  Seller App (BPP)-->>Buyer App (BAP): /on_status (unsolicited): Order-delivered
  Buyer App (BAP)->>Seller App (BPP): /update (return request: item, quantity, reason)
  Seller App (BPP)-->>Buyer App (BAP): /on_update (return in progress)
  Seller App (BPP)-->>Buyer App (BAP): /on_update (unsolicited): return completed
  Buyer App (BAP)->>Seller App (BPP): /update (settlement for return refund)
```

## on_status_at_pickup

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
  Seller App (BPP)-->>Buyer App (BAP): /on_status (unsolicited): Agent-assigned
  rect rgb(191, 223, 255)
  Seller App (BPP)-->>Buyer App (BAP): /on_status (unsolicited): At-pickup
  end
  Seller App (BPP)-->>Buyer App (BAP): /on_status (unsolicited): Order-picked-up
  Seller App (BPP)-->>Buyer App (BAP): /on_status (unsolicited): At-delivery
  Seller App (BPP)-->>Buyer App (BAP): /on_status (unsolicited): Order-delivered
  Buyer App (BAP)->>Seller App (BPP): /update (return request: item, quantity, reason)
  Seller App (BPP)-->>Buyer App (BAP): /on_update (return in progress)
  Seller App (BPP)-->>Buyer App (BAP): /on_update (unsolicited): return completed
  Buyer App (BAP)->>Seller App (BPP): /update (settlement for return refund)
```

## on_status_order_picked

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
  Seller App (BPP)-->>Buyer App (BAP): /on_status (unsolicited): Agent-assigned
  Seller App (BPP)-->>Buyer App (BAP): /on_status (unsolicited): At-pickup
  rect rgb(191, 223, 255)
  Seller App (BPP)-->>Buyer App (BAP): /on_status (unsolicited): Order-picked-up
  end
  Seller App (BPP)-->>Buyer App (BAP): /on_status (unsolicited): At-delivery
  Seller App (BPP)-->>Buyer App (BAP): /on_status (unsolicited): Order-delivered
  Buyer App (BAP)->>Seller App (BPP): /update (return request: item, quantity, reason)
  Seller App (BPP)-->>Buyer App (BAP): /on_update (return in progress)
  Seller App (BPP)-->>Buyer App (BAP): /on_update (unsolicited): return completed
  Buyer App (BAP)->>Seller App (BPP): /update (settlement for return refund)
```

## on_status_at_delivery

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
  Seller App (BPP)-->>Buyer App (BAP): /on_status (unsolicited): Agent-assigned
  Seller App (BPP)-->>Buyer App (BAP): /on_status (unsolicited): At-pickup
  Seller App (BPP)-->>Buyer App (BAP): /on_status (unsolicited): Order-picked-up
  rect rgb(191, 223, 255)
  Seller App (BPP)-->>Buyer App (BAP): /on_status (unsolicited): At-delivery
  end
  Seller App (BPP)-->>Buyer App (BAP): /on_status (unsolicited): Order-delivered
  Buyer App (BAP)->>Seller App (BPP): /update (return request: item, quantity, reason)
  Seller App (BPP)-->>Buyer App (BAP): /on_update (return in progress)
  Seller App (BPP)-->>Buyer App (BAP): /on_update (unsolicited): return completed
  Buyer App (BAP)->>Seller App (BPP): /update (settlement for return refund)
```

## on_status_order_delivered

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
  Seller App (BPP)-->>Buyer App (BAP): /on_status (unsolicited): Agent-assigned
  Seller App (BPP)-->>Buyer App (BAP): /on_status (unsolicited): At-pickup
  Seller App (BPP)-->>Buyer App (BAP): /on_status (unsolicited): Order-picked-up
  Seller App (BPP)-->>Buyer App (BAP): /on_status (unsolicited): At-delivery
  rect rgb(191, 223, 255)
  Seller App (BPP)-->>Buyer App (BAP): /on_status (unsolicited): Order-delivered
  end
  Buyer App (BAP)->>Seller App (BPP): /update (return request: item, quantity, reason)
  Seller App (BPP)-->>Buyer App (BAP): /on_update (return in progress)
  Seller App (BPP)-->>Buyer App (BAP): /on_update (unsolicited): return completed
  Buyer App (BAP)->>Seller App (BPP): /update (settlement for return refund)
```

## update_return

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
  Seller App (BPP)-->>Buyer App (BAP): /on_status (unsolicited): Agent-assigned
  Seller App (BPP)-->>Buyer App (BAP): /on_status (unsolicited): At-pickup
  Seller App (BPP)-->>Buyer App (BAP): /on_status (unsolicited): Order-picked-up
  Seller App (BPP)-->>Buyer App (BAP): /on_status (unsolicited): At-delivery
  Seller App (BPP)-->>Buyer App (BAP): /on_status (unsolicited): Order-delivered
  rect rgb(191, 223, 255)
  Buyer App (BAP)->>Seller App (BPP): /update (return request: item, quantity, reason)
  end
  Seller App (BPP)-->>Buyer App (BAP): /on_update (return in progress)
  Seller App (BPP)-->>Buyer App (BAP): /on_update (unsolicited): return completed
  Buyer App (BAP)->>Seller App (BPP): /update (settlement for return refund)
```

## on_update_return_intermin

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
  Seller App (BPP)-->>Buyer App (BAP): /on_status (unsolicited): Agent-assigned
  Seller App (BPP)-->>Buyer App (BAP): /on_status (unsolicited): At-pickup
  Seller App (BPP)-->>Buyer App (BAP): /on_status (unsolicited): Order-picked-up
  Seller App (BPP)-->>Buyer App (BAP): /on_status (unsolicited): At-delivery
  Seller App (BPP)-->>Buyer App (BAP): /on_status (unsolicited): Order-delivered
  Buyer App (BAP)->>Seller App (BPP): /update (return request: item, quantity, reason)
  rect rgb(191, 223, 255)
  Seller App (BPP)-->>Buyer App (BAP): /on_update (return in progress)
  end
  Seller App (BPP)-->>Buyer App (BAP): /on_update (unsolicited): return completed
  Buyer App (BAP)->>Seller App (BPP): /update (settlement for return refund)
```

## on_update_return_final

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
  Seller App (BPP)-->>Buyer App (BAP): /on_status (unsolicited): Agent-assigned
  Seller App (BPP)-->>Buyer App (BAP): /on_status (unsolicited): At-pickup
  Seller App (BPP)-->>Buyer App (BAP): /on_status (unsolicited): Order-picked-up
  Seller App (BPP)-->>Buyer App (BAP): /on_status (unsolicited): At-delivery
  Seller App (BPP)-->>Buyer App (BAP): /on_status (unsolicited): Order-delivered
  Buyer App (BAP)->>Seller App (BPP): /update (return request: item, quantity, reason)
  Seller App (BPP)-->>Buyer App (BAP): /on_update (return in progress)
  rect rgb(191, 223, 255)
  Seller App (BPP)-->>Buyer App (BAP): /on_update (unsolicited): return completed
  end
  Buyer App (BAP)->>Seller App (BPP): /update (settlement for return refund)
```

## update_settelment_return

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
  Seller App (BPP)-->>Buyer App (BAP): /on_status (unsolicited): Agent-assigned
  Seller App (BPP)-->>Buyer App (BAP): /on_status (unsolicited): At-pickup
  Seller App (BPP)-->>Buyer App (BAP): /on_status (unsolicited): Order-picked-up
  Seller App (BPP)-->>Buyer App (BAP): /on_status (unsolicited): At-delivery
  Seller App (BPP)-->>Buyer App (BAP): /on_status (unsolicited): Order-delivered
  Buyer App (BAP)->>Seller App (BPP): /update (return request: item, quantity, reason)
  Seller App (BPP)-->>Buyer App (BAP): /on_update (return in progress)
  Seller App (BPP)-->>Buyer App (BAP): /on_update (unsolicited): return completed
  rect rgb(191, 223, 255)
  Buyer App (BAP)->>Seller App (BPP): /update (settlement for return refund)
  end
```

# Force Cancel — Sequence Diagrams

Internal data file consumed by the Developer Guide's "Sequence Diagram" tab (API Walkthrough).
Not meant to be shown as its own docs page — the frontend filters this slug out of the Use Case
Brief / Additional Resources / Changelog tab lists and instead looks up the section matching the
selected API call's `action_id` (the `##` heading below) to render that step's diagram.

One `## <action_id>` heading per step of `FORCE_CANCEL.yaml`, in that flow's own step order, each followed by its Mermaid `sequenceDiagram`: the whole flow, with that call's own message(s) highlighted — same convention as the other domains' per-step sequence-diagram docs.

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
  Buyer App (BAP)->>Seller App (BPP): /cancel (cancel order)
  Buyer App (BAP)->>Seller App (BPP): /cancel (force cancel request)
  Seller App (BPP)-->>Buyer App (BAP): /on_cancel (Cancelled, charges and refund)
  Buyer App (BAP)->>Seller App (BPP): /update (settlement for cancellation refund)
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
  Buyer App (BAP)->>Seller App (BPP): /cancel (cancel order)
  Buyer App (BAP)->>Seller App (BPP): /cancel (force cancel request)
  Seller App (BPP)-->>Buyer App (BAP): /on_cancel (Cancelled, charges and refund)
  Buyer App (BAP)->>Seller App (BPP): /update (settlement for cancellation refund)
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
  Buyer App (BAP)->>Seller App (BPP): /cancel (cancel order)
  Buyer App (BAP)->>Seller App (BPP): /cancel (force cancel request)
  Seller App (BPP)-->>Buyer App (BAP): /on_cancel (Cancelled, charges and refund)
  Buyer App (BAP)->>Seller App (BPP): /update (settlement for cancellation refund)
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
  Buyer App (BAP)->>Seller App (BPP): /cancel (cancel order)
  Buyer App (BAP)->>Seller App (BPP): /cancel (force cancel request)
  Seller App (BPP)-->>Buyer App (BAP): /on_cancel (Cancelled, charges and refund)
  Buyer App (BAP)->>Seller App (BPP): /update (settlement for cancellation refund)
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
  Buyer App (BAP)->>Seller App (BPP): /cancel (cancel order)
  Buyer App (BAP)->>Seller App (BPP): /cancel (force cancel request)
  Seller App (BPP)-->>Buyer App (BAP): /on_cancel (Cancelled, charges and refund)
  Buyer App (BAP)->>Seller App (BPP): /update (settlement for cancellation refund)
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
  Buyer App (BAP)->>Seller App (BPP): /cancel (cancel order)
  Buyer App (BAP)->>Seller App (BPP): /cancel (force cancel request)
  Seller App (BPP)-->>Buyer App (BAP): /on_cancel (Cancelled, charges and refund)
  Buyer App (BAP)->>Seller App (BPP): /update (settlement for cancellation refund)
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
  Buyer App (BAP)->>Seller App (BPP): /cancel (cancel order)
  Buyer App (BAP)->>Seller App (BPP): /cancel (force cancel request)
  Seller App (BPP)-->>Buyer App (BAP): /on_cancel (Cancelled, charges and refund)
  Buyer App (BAP)->>Seller App (BPP): /update (settlement for cancellation refund)
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
  Buyer App (BAP)->>Seller App (BPP): /cancel (cancel order)
  Buyer App (BAP)->>Seller App (BPP): /cancel (force cancel request)
  Seller App (BPP)-->>Buyer App (BAP): /on_cancel (Cancelled, charges and refund)
  Buyer App (BAP)->>Seller App (BPP): /update (settlement for cancellation refund)
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
  Buyer App (BAP)->>Seller App (BPP): /cancel (cancel order)
  Buyer App (BAP)->>Seller App (BPP): /cancel (force cancel request)
  Seller App (BPP)-->>Buyer App (BAP): /on_cancel (Cancelled, charges and refund)
  Buyer App (BAP)->>Seller App (BPP): /update (settlement for cancellation refund)
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
  Buyer App (BAP)->>Seller App (BPP): /cancel (cancel order)
  Buyer App (BAP)->>Seller App (BPP): /cancel (force cancel request)
  Seller App (BPP)-->>Buyer App (BAP): /on_cancel (Cancelled, charges and refund)
  Buyer App (BAP)->>Seller App (BPP): /update (settlement for cancellation refund)
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
  Buyer App (BAP)->>Seller App (BPP): /cancel (cancel order)
  Buyer App (BAP)->>Seller App (BPP): /cancel (force cancel request)
  Seller App (BPP)-->>Buyer App (BAP): /on_cancel (Cancelled, charges and refund)
  Buyer App (BAP)->>Seller App (BPP): /update (settlement for cancellation refund)
```

## cancel_no

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
  Buyer App (BAP)->>Seller App (BPP): /cancel (cancel order)
  end
  Buyer App (BAP)->>Seller App (BPP): /cancel (force cancel request)
  Seller App (BPP)-->>Buyer App (BAP): /on_cancel (Cancelled, charges and refund)
  Buyer App (BAP)->>Seller App (BPP): /update (settlement for cancellation refund)
```

## cancel_force

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
  Buyer App (BAP)->>Seller App (BPP): /cancel (cancel order)
  rect rgb(191, 223, 255)
  Buyer App (BAP)->>Seller App (BPP): /cancel (force cancel request)
  end
  Seller App (BPP)-->>Buyer App (BAP): /on_cancel (Cancelled, charges and refund)
  Buyer App (BAP)->>Seller App (BPP): /update (settlement for cancellation refund)
```

## on_cancel

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
  Buyer App (BAP)->>Seller App (BPP): /cancel (cancel order)
  Buyer App (BAP)->>Seller App (BPP): /cancel (force cancel request)
  rect rgb(191, 223, 255)
  Seller App (BPP)-->>Buyer App (BAP): /on_cancel (Cancelled, charges and refund)
  end
  Buyer App (BAP)->>Seller App (BPP): /update (settlement for cancellation refund)
```

## update_settelment_cancel

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
  Buyer App (BAP)->>Seller App (BPP): /cancel (cancel order)
  Buyer App (BAP)->>Seller App (BPP): /cancel (force cancel request)
  Seller App (BPP)-->>Buyer App (BAP): /on_cancel (Cancelled, charges and refund)
  rect rgb(191, 223, 255)
  Buyer App (BAP)->>Seller App (BPP): /update (settlement for cancellation refund)
  end
```

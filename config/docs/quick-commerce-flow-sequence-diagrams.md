# quick commerce flow — Sequence Diagrams

Internal data file consumed by the Developer Guide's "Sequence Diagram" tab (API Walkthrough).
Not meant to be shown as its own docs page — the frontend filters this slug out of the Use Case
Brief / Additional Resources / Changelog tab lists and instead looks up the section matching the
selected API call's `action_id` (the `##` heading below) to render that step's diagram.

One `## <action_id>` heading per step of `QUICK_COMMERCE_FLOW.yaml`, in that flow's own step order, each followed by its Mermaid `sequenceDiagram`: the whole flow, with that call's own message(s) highlighted — same convention as the other domains' per-step sequence-diagram docs.

## search_qc

```mermaid
sequenceDiagram
  participant LBNP as Logistics Buyer (LBNP · BAP)
  participant LSP as Logistics Provider (LSP · BPP)
  rect rgb(191, 223, 255)
  LBNP->>LSP: /search (Instant Delivery, quick commerce)
  end
  LSP-->>LBNP: /on_search (catalog for quick commerce)
  LBNP->>LSP: /init (chosen option, addresses, billing)
  LSP-->>LBNP: /on_init (quote, payment and cancellation terms)
  LBNP->>LSP: /confirm (order Created, linked order)
  LSP-->>LBNP: /on_confirm (order Accepted, Pending)
  LSP-->>LBNP: /on_status (Agent-assigned)
  LBNP->>LSP: /update (ready_to_ship = yes)
  LSP-->>LBNP: /on_update (In-progress, Searching-for-Agent)
  LSP-->>LBNP: /on_status (At-pickup)
  LSP-->>LBNP: /on_status (Order-picked-up)
  LSP-->>LBNP: /on_status (At-delivery)
  LSP-->>LBNP: /on_status (Order-delivered, order Completed)
```

## on_search_qc

```mermaid
sequenceDiagram
  participant LBNP as Logistics Buyer (LBNP · BAP)
  participant LSP as Logistics Provider (LSP · BPP)
  LBNP->>LSP: /search (Instant Delivery, quick commerce)
  rect rgb(191, 223, 255)
  LSP-->>LBNP: /on_search (catalog for quick commerce)
  end
  LBNP->>LSP: /init (chosen option, addresses, billing)
  LSP-->>LBNP: /on_init (quote, payment and cancellation terms)
  LBNP->>LSP: /confirm (order Created, linked order)
  LSP-->>LBNP: /on_confirm (order Accepted, Pending)
  LSP-->>LBNP: /on_status (Agent-assigned)
  LBNP->>LSP: /update (ready_to_ship = yes)
  LSP-->>LBNP: /on_update (In-progress, Searching-for-Agent)
  LSP-->>LBNP: /on_status (At-pickup)
  LSP-->>LBNP: /on_status (Order-picked-up)
  LSP-->>LBNP: /on_status (At-delivery)
  LSP-->>LBNP: /on_status (Order-delivered, order Completed)
```

## init_qc

```mermaid
sequenceDiagram
  participant LBNP as Logistics Buyer (LBNP · BAP)
  participant LSP as Logistics Provider (LSP · BPP)
  LBNP->>LSP: /search (Instant Delivery, quick commerce)
  LSP-->>LBNP: /on_search (catalog for quick commerce)
  rect rgb(191, 223, 255)
  LBNP->>LSP: /init (chosen option, addresses, billing)
  end
  LSP-->>LBNP: /on_init (quote, payment and cancellation terms)
  LBNP->>LSP: /confirm (order Created, linked order)
  LSP-->>LBNP: /on_confirm (order Accepted, Pending)
  LSP-->>LBNP: /on_status (Agent-assigned)
  LBNP->>LSP: /update (ready_to_ship = yes)
  LSP-->>LBNP: /on_update (In-progress, Searching-for-Agent)
  LSP-->>LBNP: /on_status (At-pickup)
  LSP-->>LBNP: /on_status (Order-picked-up)
  LSP-->>LBNP: /on_status (At-delivery)
  LSP-->>LBNP: /on_status (Order-delivered, order Completed)
```

## on_init_qc

```mermaid
sequenceDiagram
  participant LBNP as Logistics Buyer (LBNP · BAP)
  participant LSP as Logistics Provider (LSP · BPP)
  LBNP->>LSP: /search (Instant Delivery, quick commerce)
  LSP-->>LBNP: /on_search (catalog for quick commerce)
  LBNP->>LSP: /init (chosen option, addresses, billing)
  rect rgb(191, 223, 255)
  LSP-->>LBNP: /on_init (quote, payment and cancellation terms)
  end
  LBNP->>LSP: /confirm (order Created, linked order)
  LSP-->>LBNP: /on_confirm (order Accepted, Pending)
  LSP-->>LBNP: /on_status (Agent-assigned)
  LBNP->>LSP: /update (ready_to_ship = yes)
  LSP-->>LBNP: /on_update (In-progress, Searching-for-Agent)
  LSP-->>LBNP: /on_status (At-pickup)
  LSP-->>LBNP: /on_status (Order-picked-up)
  LSP-->>LBNP: /on_status (At-delivery)
  LSP-->>LBNP: /on_status (Order-delivered, order Completed)
```

## confirm_qc

```mermaid
sequenceDiagram
  participant LBNP as Logistics Buyer (LBNP · BAP)
  participant LSP as Logistics Provider (LSP · BPP)
  LBNP->>LSP: /search (Instant Delivery, quick commerce)
  LSP-->>LBNP: /on_search (catalog for quick commerce)
  LBNP->>LSP: /init (chosen option, addresses, billing)
  LSP-->>LBNP: /on_init (quote, payment and cancellation terms)
  rect rgb(191, 223, 255)
  LBNP->>LSP: /confirm (order Created, linked order)
  end
  LSP-->>LBNP: /on_confirm (order Accepted, Pending)
  LSP-->>LBNP: /on_status (Agent-assigned)
  LBNP->>LSP: /update (ready_to_ship = yes)
  LSP-->>LBNP: /on_update (In-progress, Searching-for-Agent)
  LSP-->>LBNP: /on_status (At-pickup)
  LSP-->>LBNP: /on_status (Order-picked-up)
  LSP-->>LBNP: /on_status (At-delivery)
  LSP-->>LBNP: /on_status (Order-delivered, order Completed)
```

## on_confirm_qc

```mermaid
sequenceDiagram
  participant LBNP as Logistics Buyer (LBNP · BAP)
  participant LSP as Logistics Provider (LSP · BPP)
  LBNP->>LSP: /search (Instant Delivery, quick commerce)
  LSP-->>LBNP: /on_search (catalog for quick commerce)
  LBNP->>LSP: /init (chosen option, addresses, billing)
  LSP-->>LBNP: /on_init (quote, payment and cancellation terms)
  LBNP->>LSP: /confirm (order Created, linked order)
  rect rgb(191, 223, 255)
  LSP-->>LBNP: /on_confirm (order Accepted, Pending)
  end
  LSP-->>LBNP: /on_status (Agent-assigned)
  LBNP->>LSP: /update (ready_to_ship = yes)
  LSP-->>LBNP: /on_update (In-progress, Searching-for-Agent)
  LSP-->>LBNP: /on_status (At-pickup)
  LSP-->>LBNP: /on_status (Order-picked-up)
  LSP-->>LBNP: /on_status (At-delivery)
  LSP-->>LBNP: /on_status (Order-delivered, order Completed)
```

## on_status_11_LOGISTICS

```mermaid
sequenceDiagram
  participant LBNP as Logistics Buyer (LBNP · BAP)
  participant LSP as Logistics Provider (LSP · BPP)
  LBNP->>LSP: /search (Instant Delivery, quick commerce)
  LSP-->>LBNP: /on_search (catalog for quick commerce)
  LBNP->>LSP: /init (chosen option, addresses, billing)
  LSP-->>LBNP: /on_init (quote, payment and cancellation terms)
  LBNP->>LSP: /confirm (order Created, linked order)
  LSP-->>LBNP: /on_confirm (order Accepted, Pending)
  rect rgb(191, 223, 255)
  LSP-->>LBNP: /on_status (Agent-assigned)
  end
  LBNP->>LSP: /update (ready_to_ship = yes)
  LSP-->>LBNP: /on_update (In-progress, Searching-for-Agent)
  LSP-->>LBNP: /on_status (At-pickup)
  LSP-->>LBNP: /on_status (Order-picked-up)
  LSP-->>LBNP: /on_status (At-delivery)
  LSP-->>LBNP: /on_status (Order-delivered, order Completed)
```

## update_qc

```mermaid
sequenceDiagram
  participant LBNP as Logistics Buyer (LBNP · BAP)
  participant LSP as Logistics Provider (LSP · BPP)
  LBNP->>LSP: /search (Instant Delivery, quick commerce)
  LSP-->>LBNP: /on_search (catalog for quick commerce)
  LBNP->>LSP: /init (chosen option, addresses, billing)
  LSP-->>LBNP: /on_init (quote, payment and cancellation terms)
  LBNP->>LSP: /confirm (order Created, linked order)
  LSP-->>LBNP: /on_confirm (order Accepted, Pending)
  LSP-->>LBNP: /on_status (Agent-assigned)
  rect rgb(191, 223, 255)
  LBNP->>LSP: /update (ready_to_ship = yes)
  end
  LSP-->>LBNP: /on_update (In-progress, Searching-for-Agent)
  LSP-->>LBNP: /on_status (At-pickup)
  LSP-->>LBNP: /on_status (Order-picked-up)
  LSP-->>LBNP: /on_status (At-delivery)
  LSP-->>LBNP: /on_status (Order-delivered, order Completed)
```

## on_update_qc

```mermaid
sequenceDiagram
  participant LBNP as Logistics Buyer (LBNP · BAP)
  participant LSP as Logistics Provider (LSP · BPP)
  LBNP->>LSP: /search (Instant Delivery, quick commerce)
  LSP-->>LBNP: /on_search (catalog for quick commerce)
  LBNP->>LSP: /init (chosen option, addresses, billing)
  LSP-->>LBNP: /on_init (quote, payment and cancellation terms)
  LBNP->>LSP: /confirm (order Created, linked order)
  LSP-->>LBNP: /on_confirm (order Accepted, Pending)
  LSP-->>LBNP: /on_status (Agent-assigned)
  LBNP->>LSP: /update (ready_to_ship = yes)
  rect rgb(191, 223, 255)
  LSP-->>LBNP: /on_update (In-progress, Searching-for-Agent)
  end
  LSP-->>LBNP: /on_status (At-pickup)
  LSP-->>LBNP: /on_status (Order-picked-up)
  LSP-->>LBNP: /on_status (At-delivery)
  LSP-->>LBNP: /on_status (Order-delivered, order Completed)
```

## on_status_5_LOGISTICS

```mermaid
sequenceDiagram
  participant LBNP as Logistics Buyer (LBNP · BAP)
  participant LSP as Logistics Provider (LSP · BPP)
  LBNP->>LSP: /search (Instant Delivery, quick commerce)
  LSP-->>LBNP: /on_search (catalog for quick commerce)
  LBNP->>LSP: /init (chosen option, addresses, billing)
  LSP-->>LBNP: /on_init (quote, payment and cancellation terms)
  LBNP->>LSP: /confirm (order Created, linked order)
  LSP-->>LBNP: /on_confirm (order Accepted, Pending)
  LSP-->>LBNP: /on_status (Agent-assigned)
  LBNP->>LSP: /update (ready_to_ship = yes)
  LSP-->>LBNP: /on_update (In-progress, Searching-for-Agent)
  rect rgb(191, 223, 255)
  LSP-->>LBNP: /on_status (At-pickup)
  end
  LSP-->>LBNP: /on_status (Order-picked-up)
  LSP-->>LBNP: /on_status (At-delivery)
  LSP-->>LBNP: /on_status (Order-delivered, order Completed)
```

## on_status_1_LOGISTICS

```mermaid
sequenceDiagram
  participant LBNP as Logistics Buyer (LBNP · BAP)
  participant LSP as Logistics Provider (LSP · BPP)
  LBNP->>LSP: /search (Instant Delivery, quick commerce)
  LSP-->>LBNP: /on_search (catalog for quick commerce)
  LBNP->>LSP: /init (chosen option, addresses, billing)
  LSP-->>LBNP: /on_init (quote, payment and cancellation terms)
  LBNP->>LSP: /confirm (order Created, linked order)
  LSP-->>LBNP: /on_confirm (order Accepted, Pending)
  LSP-->>LBNP: /on_status (Agent-assigned)
  LBNP->>LSP: /update (ready_to_ship = yes)
  LSP-->>LBNP: /on_update (In-progress, Searching-for-Agent)
  LSP-->>LBNP: /on_status (At-pickup)
  rect rgb(191, 223, 255)
  LSP-->>LBNP: /on_status (Order-picked-up)
  end
  LSP-->>LBNP: /on_status (At-delivery)
  LSP-->>LBNP: /on_status (Order-delivered, order Completed)
```

## on_status_12_LOGISTICS

```mermaid
sequenceDiagram
  participant LBNP as Logistics Buyer (LBNP · BAP)
  participant LSP as Logistics Provider (LSP · BPP)
  LBNP->>LSP: /search (Instant Delivery, quick commerce)
  LSP-->>LBNP: /on_search (catalog for quick commerce)
  LBNP->>LSP: /init (chosen option, addresses, billing)
  LSP-->>LBNP: /on_init (quote, payment and cancellation terms)
  LBNP->>LSP: /confirm (order Created, linked order)
  LSP-->>LBNP: /on_confirm (order Accepted, Pending)
  LSP-->>LBNP: /on_status (Agent-assigned)
  LBNP->>LSP: /update (ready_to_ship = yes)
  LSP-->>LBNP: /on_update (In-progress, Searching-for-Agent)
  LSP-->>LBNP: /on_status (At-pickup)
  LSP-->>LBNP: /on_status (Order-picked-up)
  rect rgb(191, 223, 255)
  LSP-->>LBNP: /on_status (At-delivery)
  end
  LSP-->>LBNP: /on_status (Order-delivered, order Completed)
```

## on_status_3_LOGISTICS

```mermaid
sequenceDiagram
  participant LBNP as Logistics Buyer (LBNP · BAP)
  participant LSP as Logistics Provider (LSP · BPP)
  LBNP->>LSP: /search (Instant Delivery, quick commerce)
  LSP-->>LBNP: /on_search (catalog for quick commerce)
  LBNP->>LSP: /init (chosen option, addresses, billing)
  LSP-->>LBNP: /on_init (quote, payment and cancellation terms)
  LBNP->>LSP: /confirm (order Created, linked order)
  LSP-->>LBNP: /on_confirm (order Accepted, Pending)
  LSP-->>LBNP: /on_status (Agent-assigned)
  LBNP->>LSP: /update (ready_to_ship = yes)
  LSP-->>LBNP: /on_update (In-progress, Searching-for-Agent)
  LSP-->>LBNP: /on_status (At-pickup)
  LSP-->>LBNP: /on_status (Order-picked-up)
  LSP-->>LBNP: /on_status (At-delivery)
  rect rgb(191, 223, 255)
  LSP-->>LBNP: /on_status (Order-delivered, order Completed)
  end
```

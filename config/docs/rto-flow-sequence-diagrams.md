# rto flow — Sequence Diagrams

Internal data file consumed by the Developer Guide's "Sequence Diagram" tab (API Walkthrough).
Not meant to be shown as its own docs page — the frontend filters this slug out of the Use Case
Brief / Additional Resources / Changelog tab lists and instead looks up the section matching the
selected API call's `action_id` (the `##` heading below) to render that step's diagram.

One `## <action_id>` heading per step of `RTO_FLOW.yaml`, in that flow's own step order, each followed by its Mermaid `sequenceDiagram`: the whole flow, with that call's own message(s) highlighted — same convention as the other domains' per-step sequence-diagram docs.

## search_1

```mermaid
sequenceDiagram
  participant LBNP as Logistics Buyer (LBNP · BAP)
  participant LSP as Logistics Provider (LSP · BPP)
  rect rgb(191, 223, 255)
  LBNP->>LSP: /search (pickup, drop, category, package)
  end
  LSP-->>LBNP: /on_search (catalog, prices, TAT, RTO price)
  LBNP->>LSP: /init (chosen option, addresses, billing)
  LSP-->>LBNP: /on_init (quote, payment and cancellation terms)
  LBNP->>LSP: /confirm (order Created, linked order)
  LSP-->>LBNP: /on_confirm (order Accepted, Pending)
  LSP-->>LBNP: /on_status (Searching-for-Agent)
  LSP-->>LBNP: /on_status (Agent-assigned)
  LSP-->>LBNP: /on_status (Order-picked-up)
  LSP-->>LBNP: /on_status (Out-for-delivery)
  LSP-->>LBNP: /on_cancel (RTO initiated, order Cancelled)
  LSP-->>LBNP: /on_status (RTO fulfillment RTO-Delivered)
```

## on_search_1

```mermaid
sequenceDiagram
  participant LBNP as Logistics Buyer (LBNP · BAP)
  participant LSP as Logistics Provider (LSP · BPP)
  LBNP->>LSP: /search (pickup, drop, category, package)
  rect rgb(191, 223, 255)
  LSP-->>LBNP: /on_search (catalog, prices, TAT, RTO price)
  end
  LBNP->>LSP: /init (chosen option, addresses, billing)
  LSP-->>LBNP: /on_init (quote, payment and cancellation terms)
  LBNP->>LSP: /confirm (order Created, linked order)
  LSP-->>LBNP: /on_confirm (order Accepted, Pending)
  LSP-->>LBNP: /on_status (Searching-for-Agent)
  LSP-->>LBNP: /on_status (Agent-assigned)
  LSP-->>LBNP: /on_status (Order-picked-up)
  LSP-->>LBNP: /on_status (Out-for-delivery)
  LSP-->>LBNP: /on_cancel (RTO initiated, order Cancelled)
  LSP-->>LBNP: /on_status (RTO fulfillment RTO-Delivered)
```

## init_1

```mermaid
sequenceDiagram
  participant LBNP as Logistics Buyer (LBNP · BAP)
  participant LSP as Logistics Provider (LSP · BPP)
  LBNP->>LSP: /search (pickup, drop, category, package)
  LSP-->>LBNP: /on_search (catalog, prices, TAT, RTO price)
  rect rgb(191, 223, 255)
  LBNP->>LSP: /init (chosen option, addresses, billing)
  end
  LSP-->>LBNP: /on_init (quote, payment and cancellation terms)
  LBNP->>LSP: /confirm (order Created, linked order)
  LSP-->>LBNP: /on_confirm (order Accepted, Pending)
  LSP-->>LBNP: /on_status (Searching-for-Agent)
  LSP-->>LBNP: /on_status (Agent-assigned)
  LSP-->>LBNP: /on_status (Order-picked-up)
  LSP-->>LBNP: /on_status (Out-for-delivery)
  LSP-->>LBNP: /on_cancel (RTO initiated, order Cancelled)
  LSP-->>LBNP: /on_status (RTO fulfillment RTO-Delivered)
```

## on_init_1

```mermaid
sequenceDiagram
  participant LBNP as Logistics Buyer (LBNP · BAP)
  participant LSP as Logistics Provider (LSP · BPP)
  LBNP->>LSP: /search (pickup, drop, category, package)
  LSP-->>LBNP: /on_search (catalog, prices, TAT, RTO price)
  LBNP->>LSP: /init (chosen option, addresses, billing)
  rect rgb(191, 223, 255)
  LSP-->>LBNP: /on_init (quote, payment and cancellation terms)
  end
  LBNP->>LSP: /confirm (order Created, linked order)
  LSP-->>LBNP: /on_confirm (order Accepted, Pending)
  LSP-->>LBNP: /on_status (Searching-for-Agent)
  LSP-->>LBNP: /on_status (Agent-assigned)
  LSP-->>LBNP: /on_status (Order-picked-up)
  LSP-->>LBNP: /on_status (Out-for-delivery)
  LSP-->>LBNP: /on_cancel (RTO initiated, order Cancelled)
  LSP-->>LBNP: /on_status (RTO fulfillment RTO-Delivered)
```

## confirm_1

```mermaid
sequenceDiagram
  participant LBNP as Logistics Buyer (LBNP · BAP)
  participant LSP as Logistics Provider (LSP · BPP)
  LBNP->>LSP: /search (pickup, drop, category, package)
  LSP-->>LBNP: /on_search (catalog, prices, TAT, RTO price)
  LBNP->>LSP: /init (chosen option, addresses, billing)
  LSP-->>LBNP: /on_init (quote, payment and cancellation terms)
  rect rgb(191, 223, 255)
  LBNP->>LSP: /confirm (order Created, linked order)
  end
  LSP-->>LBNP: /on_confirm (order Accepted, Pending)
  LSP-->>LBNP: /on_status (Searching-for-Agent)
  LSP-->>LBNP: /on_status (Agent-assigned)
  LSP-->>LBNP: /on_status (Order-picked-up)
  LSP-->>LBNP: /on_status (Out-for-delivery)
  LSP-->>LBNP: /on_cancel (RTO initiated, order Cancelled)
  LSP-->>LBNP: /on_status (RTO fulfillment RTO-Delivered)
```

## on_confirm1

```mermaid
sequenceDiagram
  participant LBNP as Logistics Buyer (LBNP · BAP)
  participant LSP as Logistics Provider (LSP · BPP)
  LBNP->>LSP: /search (pickup, drop, category, package)
  LSP-->>LBNP: /on_search (catalog, prices, TAT, RTO price)
  LBNP->>LSP: /init (chosen option, addresses, billing)
  LSP-->>LBNP: /on_init (quote, payment and cancellation terms)
  LBNP->>LSP: /confirm (order Created, linked order)
  rect rgb(191, 223, 255)
  LSP-->>LBNP: /on_confirm (order Accepted, Pending)
  end
  LSP-->>LBNP: /on_status (Searching-for-Agent)
  LSP-->>LBNP: /on_status (Agent-assigned)
  LSP-->>LBNP: /on_status (Order-picked-up)
  LSP-->>LBNP: /on_status (Out-for-delivery)
  LSP-->>LBNP: /on_cancel (RTO initiated, order Cancelled)
  LSP-->>LBNP: /on_status (RTO fulfillment RTO-Delivered)
```

## on_status_searching_for_agent

```mermaid
sequenceDiagram
  participant LBNP as Logistics Buyer (LBNP · BAP)
  participant LSP as Logistics Provider (LSP · BPP)
  LBNP->>LSP: /search (pickup, drop, category, package)
  LSP-->>LBNP: /on_search (catalog, prices, TAT, RTO price)
  LBNP->>LSP: /init (chosen option, addresses, billing)
  LSP-->>LBNP: /on_init (quote, payment and cancellation terms)
  LBNP->>LSP: /confirm (order Created, linked order)
  LSP-->>LBNP: /on_confirm (order Accepted, Pending)
  rect rgb(191, 223, 255)
  LSP-->>LBNP: /on_status (Searching-for-Agent)
  end
  LSP-->>LBNP: /on_status (Agent-assigned)
  LSP-->>LBNP: /on_status (Order-picked-up)
  LSP-->>LBNP: /on_status (Out-for-delivery)
  LSP-->>LBNP: /on_cancel (RTO initiated, order Cancelled)
  LSP-->>LBNP: /on_status (RTO fulfillment RTO-Delivered)
```

## on_status_agent_assigned

```mermaid
sequenceDiagram
  participant LBNP as Logistics Buyer (LBNP · BAP)
  participant LSP as Logistics Provider (LSP · BPP)
  LBNP->>LSP: /search (pickup, drop, category, package)
  LSP-->>LBNP: /on_search (catalog, prices, TAT, RTO price)
  LBNP->>LSP: /init (chosen option, addresses, billing)
  LSP-->>LBNP: /on_init (quote, payment and cancellation terms)
  LBNP->>LSP: /confirm (order Created, linked order)
  LSP-->>LBNP: /on_confirm (order Accepted, Pending)
  LSP-->>LBNP: /on_status (Searching-for-Agent)
  rect rgb(191, 223, 255)
  LSP-->>LBNP: /on_status (Agent-assigned)
  end
  LSP-->>LBNP: /on_status (Order-picked-up)
  LSP-->>LBNP: /on_status (Out-for-delivery)
  LSP-->>LBNP: /on_cancel (RTO initiated, order Cancelled)
  LSP-->>LBNP: /on_status (RTO fulfillment RTO-Delivered)
```

## on_status_order_picked_up

```mermaid
sequenceDiagram
  participant LBNP as Logistics Buyer (LBNP · BAP)
  participant LSP as Logistics Provider (LSP · BPP)
  LBNP->>LSP: /search (pickup, drop, category, package)
  LSP-->>LBNP: /on_search (catalog, prices, TAT, RTO price)
  LBNP->>LSP: /init (chosen option, addresses, billing)
  LSP-->>LBNP: /on_init (quote, payment and cancellation terms)
  LBNP->>LSP: /confirm (order Created, linked order)
  LSP-->>LBNP: /on_confirm (order Accepted, Pending)
  LSP-->>LBNP: /on_status (Searching-for-Agent)
  LSP-->>LBNP: /on_status (Agent-assigned)
  rect rgb(191, 223, 255)
  LSP-->>LBNP: /on_status (Order-picked-up)
  end
  LSP-->>LBNP: /on_status (Out-for-delivery)
  LSP-->>LBNP: /on_cancel (RTO initiated, order Cancelled)
  LSP-->>LBNP: /on_status (RTO fulfillment RTO-Delivered)
```

## on_status_out_for_delivery

```mermaid
sequenceDiagram
  participant LBNP as Logistics Buyer (LBNP · BAP)
  participant LSP as Logistics Provider (LSP · BPP)
  LBNP->>LSP: /search (pickup, drop, category, package)
  LSP-->>LBNP: /on_search (catalog, prices, TAT, RTO price)
  LBNP->>LSP: /init (chosen option, addresses, billing)
  LSP-->>LBNP: /on_init (quote, payment and cancellation terms)
  LBNP->>LSP: /confirm (order Created, linked order)
  LSP-->>LBNP: /on_confirm (order Accepted, Pending)
  LSP-->>LBNP: /on_status (Searching-for-Agent)
  LSP-->>LBNP: /on_status (Agent-assigned)
  LSP-->>LBNP: /on_status (Order-picked-up)
  rect rgb(191, 223, 255)
  LSP-->>LBNP: /on_status (Out-for-delivery)
  end
  LSP-->>LBNP: /on_cancel (RTO initiated, order Cancelled)
  LSP-->>LBNP: /on_status (RTO fulfillment RTO-Delivered)
```

## on_cancel_rto

```mermaid
sequenceDiagram
  participant LBNP as Logistics Buyer (LBNP · BAP)
  participant LSP as Logistics Provider (LSP · BPP)
  LBNP->>LSP: /search (pickup, drop, category, package)
  LSP-->>LBNP: /on_search (catalog, prices, TAT, RTO price)
  LBNP->>LSP: /init (chosen option, addresses, billing)
  LSP-->>LBNP: /on_init (quote, payment and cancellation terms)
  LBNP->>LSP: /confirm (order Created, linked order)
  LSP-->>LBNP: /on_confirm (order Accepted, Pending)
  LSP-->>LBNP: /on_status (Searching-for-Agent)
  LSP-->>LBNP: /on_status (Agent-assigned)
  LSP-->>LBNP: /on_status (Order-picked-up)
  LSP-->>LBNP: /on_status (Out-for-delivery)
  rect rgb(191, 223, 255)
  LSP-->>LBNP: /on_cancel (RTO initiated, order Cancelled)
  end
  LSP-->>LBNP: /on_status (RTO fulfillment RTO-Delivered)
```

## on_status

```mermaid
sequenceDiagram
  participant LBNP as Logistics Buyer (LBNP · BAP)
  participant LSP as Logistics Provider (LSP · BPP)
  LBNP->>LSP: /search (pickup, drop, category, package)
  LSP-->>LBNP: /on_search (catalog, prices, TAT, RTO price)
  LBNP->>LSP: /init (chosen option, addresses, billing)
  LSP-->>LBNP: /on_init (quote, payment and cancellation terms)
  LBNP->>LSP: /confirm (order Created, linked order)
  LSP-->>LBNP: /on_confirm (order Accepted, Pending)
  LSP-->>LBNP: /on_status (Searching-for-Agent)
  LSP-->>LBNP: /on_status (Agent-assigned)
  LSP-->>LBNP: /on_status (Order-picked-up)
  LSP-->>LBNP: /on_status (Out-for-delivery)
  LSP-->>LBNP: /on_cancel (RTO initiated, order Cancelled)
  rect rgb(191, 223, 255)
  LSP-->>LBNP: /on_status (RTO fulfillment RTO-Delivered)
  end
```

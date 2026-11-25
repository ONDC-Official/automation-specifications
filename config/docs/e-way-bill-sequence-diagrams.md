# e-way bill — Sequence Diagrams

Internal data file consumed by the Developer Guide's "Sequence Diagram" tab (API Walkthrough).
Not meant to be shown as its own docs page — the frontend filters this slug out of the Use Case
Brief / Additional Resources / Changelog tab lists and instead looks up the section matching the
selected API call's `action_id` (the `##` heading below) to render that step's diagram.

One `## <action_id>` heading per step of `E-WAY_BILL.yaml`, in that flow's own step order, each followed by its Mermaid `sequenceDiagram`: the whole flow, with that call's own message(s) highlighted — same convention as the other domains' per-step sequence-diagram docs.

## search_LOGISTICS

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
  LBNP->>LSP: /confirm (order Created, e-way bills)
  LSP-->>LBNP: /on_confirm (order Accepted, Pending)
  LBNP->>LSP: /update (ready_to_ship = yes, e-way bill)
  LSP-->>LBNP: /on_update (Searching-for-Agent, e-way bill)
  LSP-->>LBNP: /on_status (Agent-assigned)
  LSP-->>LBNP: /on_status (At-pickup)
  LSP-->>LBNP: /on_status (Order-picked-up)
  LBNP->>LSP: /track
  LSP-->>LBNP: /on_track (rider's live location)
  LSP-->>LBNP: /on_status (At-delivery)
  LSP-->>LBNP: /on_status (Order-delivered, order Completed)
```

## on_search_LOGISTICS

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
  LBNP->>LSP: /confirm (order Created, e-way bills)
  LSP-->>LBNP: /on_confirm (order Accepted, Pending)
  LBNP->>LSP: /update (ready_to_ship = yes, e-way bill)
  LSP-->>LBNP: /on_update (Searching-for-Agent, e-way bill)
  LSP-->>LBNP: /on_status (Agent-assigned)
  LSP-->>LBNP: /on_status (At-pickup)
  LSP-->>LBNP: /on_status (Order-picked-up)
  LBNP->>LSP: /track
  LSP-->>LBNP: /on_track (rider's live location)
  LSP-->>LBNP: /on_status (At-delivery)
  LSP-->>LBNP: /on_status (Order-delivered, order Completed)
```

## init_LOGISTICS

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
  LBNP->>LSP: /confirm (order Created, e-way bills)
  LSP-->>LBNP: /on_confirm (order Accepted, Pending)
  LBNP->>LSP: /update (ready_to_ship = yes, e-way bill)
  LSP-->>LBNP: /on_update (Searching-for-Agent, e-way bill)
  LSP-->>LBNP: /on_status (Agent-assigned)
  LSP-->>LBNP: /on_status (At-pickup)
  LSP-->>LBNP: /on_status (Order-picked-up)
  LBNP->>LSP: /track
  LSP-->>LBNP: /on_track (rider's live location)
  LSP-->>LBNP: /on_status (At-delivery)
  LSP-->>LBNP: /on_status (Order-delivered, order Completed)
```

## on_init_LOGISTICS

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
  LBNP->>LSP: /confirm (order Created, e-way bills)
  LSP-->>LBNP: /on_confirm (order Accepted, Pending)
  LBNP->>LSP: /update (ready_to_ship = yes, e-way bill)
  LSP-->>LBNP: /on_update (Searching-for-Agent, e-way bill)
  LSP-->>LBNP: /on_status (Agent-assigned)
  LSP-->>LBNP: /on_status (At-pickup)
  LSP-->>LBNP: /on_status (Order-picked-up)
  LBNP->>LSP: /track
  LSP-->>LBNP: /on_track (rider's live location)
  LSP-->>LBNP: /on_status (At-delivery)
  LSP-->>LBNP: /on_status (Order-delivered, order Completed)
```

## confirm_E_WAY_BILL_LOGISTICS

```mermaid
sequenceDiagram
  participant LBNP as Logistics Buyer (LBNP · BAP)
  participant LSP as Logistics Provider (LSP · BPP)
  LBNP->>LSP: /search (pickup, drop, category, package)
  LSP-->>LBNP: /on_search (catalog, prices, TAT, RTO price)
  LBNP->>LSP: /init (chosen option, addresses, billing)
  LSP-->>LBNP: /on_init (quote, payment and cancellation terms)
  rect rgb(191, 223, 255)
  LBNP->>LSP: /confirm (order Created, e-way bills)
  end
  LSP-->>LBNP: /on_confirm (order Accepted, Pending)
  LBNP->>LSP: /update (ready_to_ship = yes, e-way bill)
  LSP-->>LBNP: /on_update (Searching-for-Agent, e-way bill)
  LSP-->>LBNP: /on_status (Agent-assigned)
  LSP-->>LBNP: /on_status (At-pickup)
  LSP-->>LBNP: /on_status (Order-picked-up)
  LBNP->>LSP: /track
  LSP-->>LBNP: /on_track (rider's live location)
  LSP-->>LBNP: /on_status (At-delivery)
  LSP-->>LBNP: /on_status (Order-delivered, order Completed)
```

## on_confirm_LOGISTICS

```mermaid
sequenceDiagram
  participant LBNP as Logistics Buyer (LBNP · BAP)
  participant LSP as Logistics Provider (LSP · BPP)
  LBNP->>LSP: /search (pickup, drop, category, package)
  LSP-->>LBNP: /on_search (catalog, prices, TAT, RTO price)
  LBNP->>LSP: /init (chosen option, addresses, billing)
  LSP-->>LBNP: /on_init (quote, payment and cancellation terms)
  LBNP->>LSP: /confirm (order Created, e-way bills)
  rect rgb(191, 223, 255)
  LSP-->>LBNP: /on_confirm (order Accepted, Pending)
  end
  LBNP->>LSP: /update (ready_to_ship = yes, e-way bill)
  LSP-->>LBNP: /on_update (Searching-for-Agent, e-way bill)
  LSP-->>LBNP: /on_status (Agent-assigned)
  LSP-->>LBNP: /on_status (At-pickup)
  LSP-->>LBNP: /on_status (Order-picked-up)
  LBNP->>LSP: /track
  LSP-->>LBNP: /on_track (rider's live location)
  LSP-->>LBNP: /on_status (At-delivery)
  LSP-->>LBNP: /on_status (Order-delivered, order Completed)
```

## update_E_WAY_BILL_LOGISTICS

```mermaid
sequenceDiagram
  participant LBNP as Logistics Buyer (LBNP · BAP)
  participant LSP as Logistics Provider (LSP · BPP)
  LBNP->>LSP: /search (pickup, drop, category, package)
  LSP-->>LBNP: /on_search (catalog, prices, TAT, RTO price)
  LBNP->>LSP: /init (chosen option, addresses, billing)
  LSP-->>LBNP: /on_init (quote, payment and cancellation terms)
  LBNP->>LSP: /confirm (order Created, e-way bills)
  LSP-->>LBNP: /on_confirm (order Accepted, Pending)
  rect rgb(191, 223, 255)
  LBNP->>LSP: /update (ready_to_ship = yes, e-way bill)
  end
  LSP-->>LBNP: /on_update (Searching-for-Agent, e-way bill)
  LSP-->>LBNP: /on_status (Agent-assigned)
  LSP-->>LBNP: /on_status (At-pickup)
  LSP-->>LBNP: /on_status (Order-picked-up)
  LBNP->>LSP: /track
  LSP-->>LBNP: /on_track (rider's live location)
  LSP-->>LBNP: /on_status (At-delivery)
  LSP-->>LBNP: /on_status (Order-delivered, order Completed)
```

## on_update_E_WAY_BILL_LOGISTICS

```mermaid
sequenceDiagram
  participant LBNP as Logistics Buyer (LBNP · BAP)
  participant LSP as Logistics Provider (LSP · BPP)
  LBNP->>LSP: /search (pickup, drop, category, package)
  LSP-->>LBNP: /on_search (catalog, prices, TAT, RTO price)
  LBNP->>LSP: /init (chosen option, addresses, billing)
  LSP-->>LBNP: /on_init (quote, payment and cancellation terms)
  LBNP->>LSP: /confirm (order Created, e-way bills)
  LSP-->>LBNP: /on_confirm (order Accepted, Pending)
  LBNP->>LSP: /update (ready_to_ship = yes, e-way bill)
  rect rgb(191, 223, 255)
  LSP-->>LBNP: /on_update (Searching-for-Agent, e-way bill)
  end
  LSP-->>LBNP: /on_status (Agent-assigned)
  LSP-->>LBNP: /on_status (At-pickup)
  LSP-->>LBNP: /on_status (Order-picked-up)
  LBNP->>LSP: /track
  LSP-->>LBNP: /on_track (rider's live location)
  LSP-->>LBNP: /on_status (At-delivery)
  LSP-->>LBNP: /on_status (Order-delivered, order Completed)
```

## on_status_13_LOGISTICS

```mermaid
sequenceDiagram
  participant LBNP as Logistics Buyer (LBNP · BAP)
  participant LSP as Logistics Provider (LSP · BPP)
  LBNP->>LSP: /search (pickup, drop, category, package)
  LSP-->>LBNP: /on_search (catalog, prices, TAT, RTO price)
  LBNP->>LSP: /init (chosen option, addresses, billing)
  LSP-->>LBNP: /on_init (quote, payment and cancellation terms)
  LBNP->>LSP: /confirm (order Created, e-way bills)
  LSP-->>LBNP: /on_confirm (order Accepted, Pending)
  LBNP->>LSP: /update (ready_to_ship = yes, e-way bill)
  LSP-->>LBNP: /on_update (Searching-for-Agent, e-way bill)
  rect rgb(191, 223, 255)
  LSP-->>LBNP: /on_status (Agent-assigned)
  end
  LSP-->>LBNP: /on_status (At-pickup)
  LSP-->>LBNP: /on_status (Order-picked-up)
  LBNP->>LSP: /track
  LSP-->>LBNP: /on_track (rider's live location)
  LSP-->>LBNP: /on_status (At-delivery)
  LSP-->>LBNP: /on_status (Order-delivered, order Completed)
```

## on_status_5_LOGISTICS

```mermaid
sequenceDiagram
  participant LBNP as Logistics Buyer (LBNP · BAP)
  participant LSP as Logistics Provider (LSP · BPP)
  LBNP->>LSP: /search (pickup, drop, category, package)
  LSP-->>LBNP: /on_search (catalog, prices, TAT, RTO price)
  LBNP->>LSP: /init (chosen option, addresses, billing)
  LSP-->>LBNP: /on_init (quote, payment and cancellation terms)
  LBNP->>LSP: /confirm (order Created, e-way bills)
  LSP-->>LBNP: /on_confirm (order Accepted, Pending)
  LBNP->>LSP: /update (ready_to_ship = yes, e-way bill)
  LSP-->>LBNP: /on_update (Searching-for-Agent, e-way bill)
  LSP-->>LBNP: /on_status (Agent-assigned)
  rect rgb(191, 223, 255)
  LSP-->>LBNP: /on_status (At-pickup)
  end
  LSP-->>LBNP: /on_status (Order-picked-up)
  LBNP->>LSP: /track
  LSP-->>LBNP: /on_track (rider's live location)
  LSP-->>LBNP: /on_status (At-delivery)
  LSP-->>LBNP: /on_status (Order-delivered, order Completed)
```

## on_status_1_LOGISTICS

```mermaid
sequenceDiagram
  participant LBNP as Logistics Buyer (LBNP · BAP)
  participant LSP as Logistics Provider (LSP · BPP)
  LBNP->>LSP: /search (pickup, drop, category, package)
  LSP-->>LBNP: /on_search (catalog, prices, TAT, RTO price)
  LBNP->>LSP: /init (chosen option, addresses, billing)
  LSP-->>LBNP: /on_init (quote, payment and cancellation terms)
  LBNP->>LSP: /confirm (order Created, e-way bills)
  LSP-->>LBNP: /on_confirm (order Accepted, Pending)
  LBNP->>LSP: /update (ready_to_ship = yes, e-way bill)
  LSP-->>LBNP: /on_update (Searching-for-Agent, e-way bill)
  LSP-->>LBNP: /on_status (Agent-assigned)
  LSP-->>LBNP: /on_status (At-pickup)
  rect rgb(191, 223, 255)
  LSP-->>LBNP: /on_status (Order-picked-up)
  end
  LBNP->>LSP: /track
  LSP-->>LBNP: /on_track (rider's live location)
  LSP-->>LBNP: /on_status (At-delivery)
  LSP-->>LBNP: /on_status (Order-delivered, order Completed)
```

## track_LOGISTICS

```mermaid
sequenceDiagram
  participant LBNP as Logistics Buyer (LBNP · BAP)
  participant LSP as Logistics Provider (LSP · BPP)
  LBNP->>LSP: /search (pickup, drop, category, package)
  LSP-->>LBNP: /on_search (catalog, prices, TAT, RTO price)
  LBNP->>LSP: /init (chosen option, addresses, billing)
  LSP-->>LBNP: /on_init (quote, payment and cancellation terms)
  LBNP->>LSP: /confirm (order Created, e-way bills)
  LSP-->>LBNP: /on_confirm (order Accepted, Pending)
  LBNP->>LSP: /update (ready_to_ship = yes, e-way bill)
  LSP-->>LBNP: /on_update (Searching-for-Agent, e-way bill)
  LSP-->>LBNP: /on_status (Agent-assigned)
  LSP-->>LBNP: /on_status (At-pickup)
  LSP-->>LBNP: /on_status (Order-picked-up)
  rect rgb(191, 223, 255)
  LBNP->>LSP: /track
  end
  LSP-->>LBNP: /on_track (rider's live location)
  LSP-->>LBNP: /on_status (At-delivery)
  LSP-->>LBNP: /on_status (Order-delivered, order Completed)
```

## on_track_LOGISTICS

```mermaid
sequenceDiagram
  participant LBNP as Logistics Buyer (LBNP · BAP)
  participant LSP as Logistics Provider (LSP · BPP)
  LBNP->>LSP: /search (pickup, drop, category, package)
  LSP-->>LBNP: /on_search (catalog, prices, TAT, RTO price)
  LBNP->>LSP: /init (chosen option, addresses, billing)
  LSP-->>LBNP: /on_init (quote, payment and cancellation terms)
  LBNP->>LSP: /confirm (order Created, e-way bills)
  LSP-->>LBNP: /on_confirm (order Accepted, Pending)
  LBNP->>LSP: /update (ready_to_ship = yes, e-way bill)
  LSP-->>LBNP: /on_update (Searching-for-Agent, e-way bill)
  LSP-->>LBNP: /on_status (Agent-assigned)
  LSP-->>LBNP: /on_status (At-pickup)
  LSP-->>LBNP: /on_status (Order-picked-up)
  LBNP->>LSP: /track
  rect rgb(191, 223, 255)
  LSP-->>LBNP: /on_track (rider's live location)
  end
  LSP-->>LBNP: /on_status (At-delivery)
  LSP-->>LBNP: /on_status (Order-delivered, order Completed)
```

## on_status_12_LOGISTICS

```mermaid
sequenceDiagram
  participant LBNP as Logistics Buyer (LBNP · BAP)
  participant LSP as Logistics Provider (LSP · BPP)
  LBNP->>LSP: /search (pickup, drop, category, package)
  LSP-->>LBNP: /on_search (catalog, prices, TAT, RTO price)
  LBNP->>LSP: /init (chosen option, addresses, billing)
  LSP-->>LBNP: /on_init (quote, payment and cancellation terms)
  LBNP->>LSP: /confirm (order Created, e-way bills)
  LSP-->>LBNP: /on_confirm (order Accepted, Pending)
  LBNP->>LSP: /update (ready_to_ship = yes, e-way bill)
  LSP-->>LBNP: /on_update (Searching-for-Agent, e-way bill)
  LSP-->>LBNP: /on_status (Agent-assigned)
  LSP-->>LBNP: /on_status (At-pickup)
  LSP-->>LBNP: /on_status (Order-picked-up)
  LBNP->>LSP: /track
  LSP-->>LBNP: /on_track (rider's live location)
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
  LBNP->>LSP: /search (pickup, drop, category, package)
  LSP-->>LBNP: /on_search (catalog, prices, TAT, RTO price)
  LBNP->>LSP: /init (chosen option, addresses, billing)
  LSP-->>LBNP: /on_init (quote, payment and cancellation terms)
  LBNP->>LSP: /confirm (order Created, e-way bills)
  LSP-->>LBNP: /on_confirm (order Accepted, Pending)
  LBNP->>LSP: /update (ready_to_ship = yes, e-way bill)
  LSP-->>LBNP: /on_update (Searching-for-Agent, e-way bill)
  LSP-->>LBNP: /on_status (Agent-assigned)
  LSP-->>LBNP: /on_status (At-pickup)
  LSP-->>LBNP: /on_status (Order-picked-up)
  LBNP->>LSP: /track
  LSP-->>LBNP: /on_track (rider's live location)
  LSP-->>LBNP: /on_status (At-delivery)
  rect rgb(191, 223, 255)
  LSP-->>LBNP: /on_status (Order-delivered, order Completed)
  end
```

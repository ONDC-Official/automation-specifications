# TECHNICAL_CANCELLATION_FLOW — Sequence Diagrams

Internal data file consumed by the Developer Guide's "Sequence Diagram" tab (API Walkthrough).
Not meant to be shown as its own docs page — the frontend filters this slug out of the Use Case
Brief / Additional Resources / Changelog tab lists and instead looks up the section matching the
selected API call's `action_id` (the `##` heading below) to render that step's diagram.

One `## <action_id>` heading per step of `TECHNICAL_CANCELLATION_FLOW.yaml` (Bus), in that flow's own step order, each followed by its Mermaid `sequenceDiagram`: the whole flow, with that call's own message(s) highlighted — same convention as the other domains' per-step sequence-diagram docs.

## search1_BUS_200

```mermaid
sequenceDiagram
  participant Buyer App (BAP)
  participant Gateway
  participant Seller App (BPP)
  rect rgb(191, 223, 255)
  Buyer App (BAP)->>Gateway: /search (catalog search)
  Gateway->>Seller App (BPP): /search (forwarded)
  end
  Seller App (BPP)-->>Buyer App (BAP): /on_search (catalog)
  Buyer App (BAP)->>Gateway: /search (station-to-station search)
  Gateway->>Seller App (BPP): /search (forwarded)
  Seller App (BPP)-->>Buyer App (BAP): /on_search (fares for station pair)
  Buyer App (BAP)->>Seller App (BPP): /select (select ticket)
  Seller App (BPP)-->>Buyer App (BAP): /on_select (quote)
  Buyer App (BAP)->>Seller App (BPP): /init (initialise order)
  Seller App (BPP)-->>Buyer App (BAP): /on_init (order details)
  Buyer App (BAP)->>Seller App (BPP): /confirm (confirm order)
  Seller App (BPP)-->>Buyer App (BAP): /on_confirm (delayed order confirmation)
  Buyer App (BAP)->>Seller App (BPP): /status (status check)
  Seller App (BPP)-->>Buyer App (BAP): /on_status (order active)
  Buyer App (BAP)->>Seller App (BPP): /cancel (technical cancel)
  Seller App (BPP)-->>Buyer App (BAP): /on_cancel (order cancelled (technical))
```

## on_search1_BUS_200

```mermaid
sequenceDiagram
  participant Buyer App (BAP)
  participant Gateway
  participant Seller App (BPP)
  Buyer App (BAP)->>Gateway: /search (catalog search)
  Gateway->>Seller App (BPP): /search (forwarded)
  rect rgb(191, 223, 255)
  Seller App (BPP)-->>Buyer App (BAP): /on_search (catalog)
  end
  Buyer App (BAP)->>Gateway: /search (station-to-station search)
  Gateway->>Seller App (BPP): /search (forwarded)
  Seller App (BPP)-->>Buyer App (BAP): /on_search (fares for station pair)
  Buyer App (BAP)->>Seller App (BPP): /select (select ticket)
  Seller App (BPP)-->>Buyer App (BAP): /on_select (quote)
  Buyer App (BAP)->>Seller App (BPP): /init (initialise order)
  Seller App (BPP)-->>Buyer App (BAP): /on_init (order details)
  Buyer App (BAP)->>Seller App (BPP): /confirm (confirm order)
  Seller App (BPP)-->>Buyer App (BAP): /on_confirm (delayed order confirmation)
  Buyer App (BAP)->>Seller App (BPP): /status (status check)
  Seller App (BPP)-->>Buyer App (BAP): /on_status (order active)
  Buyer App (BAP)->>Seller App (BPP): /cancel (technical cancel)
  Seller App (BPP)-->>Buyer App (BAP): /on_cancel (order cancelled (technical))
```

## search2_BUS_200

```mermaid
sequenceDiagram
  participant Buyer App (BAP)
  participant Gateway
  participant Seller App (BPP)
  Buyer App (BAP)->>Gateway: /search (catalog search)
  Gateway->>Seller App (BPP): /search (forwarded)
  Seller App (BPP)-->>Buyer App (BAP): /on_search (catalog)
  rect rgb(191, 223, 255)
  Buyer App (BAP)->>Gateway: /search (station-to-station search)
  Gateway->>Seller App (BPP): /search (forwarded)
  end
  Seller App (BPP)-->>Buyer App (BAP): /on_search (fares for station pair)
  Buyer App (BAP)->>Seller App (BPP): /select (select ticket)
  Seller App (BPP)-->>Buyer App (BAP): /on_select (quote)
  Buyer App (BAP)->>Seller App (BPP): /init (initialise order)
  Seller App (BPP)-->>Buyer App (BAP): /on_init (order details)
  Buyer App (BAP)->>Seller App (BPP): /confirm (confirm order)
  Seller App (BPP)-->>Buyer App (BAP): /on_confirm (delayed order confirmation)
  Buyer App (BAP)->>Seller App (BPP): /status (status check)
  Seller App (BPP)-->>Buyer App (BAP): /on_status (order active)
  Buyer App (BAP)->>Seller App (BPP): /cancel (technical cancel)
  Seller App (BPP)-->>Buyer App (BAP): /on_cancel (order cancelled (technical))
```

## on_search2_BUS_200

```mermaid
sequenceDiagram
  participant Buyer App (BAP)
  participant Gateway
  participant Seller App (BPP)
  Buyer App (BAP)->>Gateway: /search (catalog search)
  Gateway->>Seller App (BPP): /search (forwarded)
  Seller App (BPP)-->>Buyer App (BAP): /on_search (catalog)
  Buyer App (BAP)->>Gateway: /search (station-to-station search)
  Gateway->>Seller App (BPP): /search (forwarded)
  rect rgb(191, 223, 255)
  Seller App (BPP)-->>Buyer App (BAP): /on_search (fares for station pair)
  end
  Buyer App (BAP)->>Seller App (BPP): /select (select ticket)
  Seller App (BPP)-->>Buyer App (BAP): /on_select (quote)
  Buyer App (BAP)->>Seller App (BPP): /init (initialise order)
  Seller App (BPP)-->>Buyer App (BAP): /on_init (order details)
  Buyer App (BAP)->>Seller App (BPP): /confirm (confirm order)
  Seller App (BPP)-->>Buyer App (BAP): /on_confirm (delayed order confirmation)
  Buyer App (BAP)->>Seller App (BPP): /status (status check)
  Seller App (BPP)-->>Buyer App (BAP): /on_status (order active)
  Buyer App (BAP)->>Seller App (BPP): /cancel (technical cancel)
  Seller App (BPP)-->>Buyer App (BAP): /on_cancel (order cancelled (technical))
```

## select_BUS_200

```mermaid
sequenceDiagram
  participant Buyer App (BAP)
  participant Gateway
  participant Seller App (BPP)
  Buyer App (BAP)->>Gateway: /search (catalog search)
  Gateway->>Seller App (BPP): /search (forwarded)
  Seller App (BPP)-->>Buyer App (BAP): /on_search (catalog)
  Buyer App (BAP)->>Gateway: /search (station-to-station search)
  Gateway->>Seller App (BPP): /search (forwarded)
  Seller App (BPP)-->>Buyer App (BAP): /on_search (fares for station pair)
  rect rgb(191, 223, 255)
  Buyer App (BAP)->>Seller App (BPP): /select (select ticket)
  end
  Seller App (BPP)-->>Buyer App (BAP): /on_select (quote)
  Buyer App (BAP)->>Seller App (BPP): /init (initialise order)
  Seller App (BPP)-->>Buyer App (BAP): /on_init (order details)
  Buyer App (BAP)->>Seller App (BPP): /confirm (confirm order)
  Seller App (BPP)-->>Buyer App (BAP): /on_confirm (delayed order confirmation)
  Buyer App (BAP)->>Seller App (BPP): /status (status check)
  Seller App (BPP)-->>Buyer App (BAP): /on_status (order active)
  Buyer App (BAP)->>Seller App (BPP): /cancel (technical cancel)
  Seller App (BPP)-->>Buyer App (BAP): /on_cancel (order cancelled (technical))
```

## on_select_BUS_200

```mermaid
sequenceDiagram
  participant Buyer App (BAP)
  participant Gateway
  participant Seller App (BPP)
  Buyer App (BAP)->>Gateway: /search (catalog search)
  Gateway->>Seller App (BPP): /search (forwarded)
  Seller App (BPP)-->>Buyer App (BAP): /on_search (catalog)
  Buyer App (BAP)->>Gateway: /search (station-to-station search)
  Gateway->>Seller App (BPP): /search (forwarded)
  Seller App (BPP)-->>Buyer App (BAP): /on_search (fares for station pair)
  Buyer App (BAP)->>Seller App (BPP): /select (select ticket)
  rect rgb(191, 223, 255)
  Seller App (BPP)-->>Buyer App (BAP): /on_select (quote)
  end
  Buyer App (BAP)->>Seller App (BPP): /init (initialise order)
  Seller App (BPP)-->>Buyer App (BAP): /on_init (order details)
  Buyer App (BAP)->>Seller App (BPP): /confirm (confirm order)
  Seller App (BPP)-->>Buyer App (BAP): /on_confirm (delayed order confirmation)
  Buyer App (BAP)->>Seller App (BPP): /status (status check)
  Seller App (BPP)-->>Buyer App (BAP): /on_status (order active)
  Buyer App (BAP)->>Seller App (BPP): /cancel (technical cancel)
  Seller App (BPP)-->>Buyer App (BAP): /on_cancel (order cancelled (technical))
```

## init_BUS_200

```mermaid
sequenceDiagram
  participant Buyer App (BAP)
  participant Gateway
  participant Seller App (BPP)
  Buyer App (BAP)->>Gateway: /search (catalog search)
  Gateway->>Seller App (BPP): /search (forwarded)
  Seller App (BPP)-->>Buyer App (BAP): /on_search (catalog)
  Buyer App (BAP)->>Gateway: /search (station-to-station search)
  Gateway->>Seller App (BPP): /search (forwarded)
  Seller App (BPP)-->>Buyer App (BAP): /on_search (fares for station pair)
  Buyer App (BAP)->>Seller App (BPP): /select (select ticket)
  Seller App (BPP)-->>Buyer App (BAP): /on_select (quote)
  rect rgb(191, 223, 255)
  Buyer App (BAP)->>Seller App (BPP): /init (initialise order)
  end
  Seller App (BPP)-->>Buyer App (BAP): /on_init (order details)
  Buyer App (BAP)->>Seller App (BPP): /confirm (confirm order)
  Seller App (BPP)-->>Buyer App (BAP): /on_confirm (delayed order confirmation)
  Buyer App (BAP)->>Seller App (BPP): /status (status check)
  Seller App (BPP)-->>Buyer App (BAP): /on_status (order active)
  Buyer App (BAP)->>Seller App (BPP): /cancel (technical cancel)
  Seller App (BPP)-->>Buyer App (BAP): /on_cancel (order cancelled (technical))
```

## on_init_BUS_200

```mermaid
sequenceDiagram
  participant Buyer App (BAP)
  participant Gateway
  participant Seller App (BPP)
  Buyer App (BAP)->>Gateway: /search (catalog search)
  Gateway->>Seller App (BPP): /search (forwarded)
  Seller App (BPP)-->>Buyer App (BAP): /on_search (catalog)
  Buyer App (BAP)->>Gateway: /search (station-to-station search)
  Gateway->>Seller App (BPP): /search (forwarded)
  Seller App (BPP)-->>Buyer App (BAP): /on_search (fares for station pair)
  Buyer App (BAP)->>Seller App (BPP): /select (select ticket)
  Seller App (BPP)-->>Buyer App (BAP): /on_select (quote)
  Buyer App (BAP)->>Seller App (BPP): /init (initialise order)
  rect rgb(191, 223, 255)
  Seller App (BPP)-->>Buyer App (BAP): /on_init (order details)
  end
  Buyer App (BAP)->>Seller App (BPP): /confirm (confirm order)
  Seller App (BPP)-->>Buyer App (BAP): /on_confirm (delayed order confirmation)
  Buyer App (BAP)->>Seller App (BPP): /status (status check)
  Seller App (BPP)-->>Buyer App (BAP): /on_status (order active)
  Buyer App (BAP)->>Seller App (BPP): /cancel (technical cancel)
  Seller App (BPP)-->>Buyer App (BAP): /on_cancel (order cancelled (technical))
```

## confirm_BUS_200

```mermaid
sequenceDiagram
  participant Buyer App (BAP)
  participant Gateway
  participant Seller App (BPP)
  Buyer App (BAP)->>Gateway: /search (catalog search)
  Gateway->>Seller App (BPP): /search (forwarded)
  Seller App (BPP)-->>Buyer App (BAP): /on_search (catalog)
  Buyer App (BAP)->>Gateway: /search (station-to-station search)
  Gateway->>Seller App (BPP): /search (forwarded)
  Seller App (BPP)-->>Buyer App (BAP): /on_search (fares for station pair)
  Buyer App (BAP)->>Seller App (BPP): /select (select ticket)
  Seller App (BPP)-->>Buyer App (BAP): /on_select (quote)
  Buyer App (BAP)->>Seller App (BPP): /init (initialise order)
  Seller App (BPP)-->>Buyer App (BAP): /on_init (order details)
  rect rgb(191, 223, 255)
  Buyer App (BAP)->>Seller App (BPP): /confirm (confirm order)
  end
  Seller App (BPP)-->>Buyer App (BAP): /on_confirm (delayed order confirmation)
  Buyer App (BAP)->>Seller App (BPP): /status (status check)
  Seller App (BPP)-->>Buyer App (BAP): /on_status (order active)
  Buyer App (BAP)->>Seller App (BPP): /cancel (technical cancel)
  Seller App (BPP)-->>Buyer App (BAP): /on_cancel (order cancelled (technical))
```

## on_confirm_delayed_BUS_200

```mermaid
sequenceDiagram
  participant Buyer App (BAP)
  participant Gateway
  participant Seller App (BPP)
  Buyer App (BAP)->>Gateway: /search (catalog search)
  Gateway->>Seller App (BPP): /search (forwarded)
  Seller App (BPP)-->>Buyer App (BAP): /on_search (catalog)
  Buyer App (BAP)->>Gateway: /search (station-to-station search)
  Gateway->>Seller App (BPP): /search (forwarded)
  Seller App (BPP)-->>Buyer App (BAP): /on_search (fares for station pair)
  Buyer App (BAP)->>Seller App (BPP): /select (select ticket)
  Seller App (BPP)-->>Buyer App (BAP): /on_select (quote)
  Buyer App (BAP)->>Seller App (BPP): /init (initialise order)
  Seller App (BPP)-->>Buyer App (BAP): /on_init (order details)
  Buyer App (BAP)->>Seller App (BPP): /confirm (confirm order)
  rect rgb(191, 223, 255)
  Seller App (BPP)-->>Buyer App (BAP): /on_confirm (delayed order confirmation)
  end
  Buyer App (BAP)->>Seller App (BPP): /status (status check)
  Seller App (BPP)-->>Buyer App (BAP): /on_status (order active)
  Buyer App (BAP)->>Seller App (BPP): /cancel (technical cancel)
  Seller App (BPP)-->>Buyer App (BAP): /on_cancel (order cancelled (technical))
```

## status_tech_cancel_BUS_200

```mermaid
sequenceDiagram
  participant Buyer App (BAP)
  participant Gateway
  participant Seller App (BPP)
  Buyer App (BAP)->>Gateway: /search (catalog search)
  Gateway->>Seller App (BPP): /search (forwarded)
  Seller App (BPP)-->>Buyer App (BAP): /on_search (catalog)
  Buyer App (BAP)->>Gateway: /search (station-to-station search)
  Gateway->>Seller App (BPP): /search (forwarded)
  Seller App (BPP)-->>Buyer App (BAP): /on_search (fares for station pair)
  Buyer App (BAP)->>Seller App (BPP): /select (select ticket)
  Seller App (BPP)-->>Buyer App (BAP): /on_select (quote)
  Buyer App (BAP)->>Seller App (BPP): /init (initialise order)
  Seller App (BPP)-->>Buyer App (BAP): /on_init (order details)
  Buyer App (BAP)->>Seller App (BPP): /confirm (confirm order)
  Seller App (BPP)-->>Buyer App (BAP): /on_confirm (delayed order confirmation)
  rect rgb(191, 223, 255)
  Buyer App (BAP)->>Seller App (BPP): /status (status check)
  end
  Seller App (BPP)-->>Buyer App (BAP): /on_status (order active)
  Buyer App (BAP)->>Seller App (BPP): /cancel (technical cancel)
  Seller App (BPP)-->>Buyer App (BAP): /on_cancel (order cancelled (technical))
```

## on_status_active_BUS_200

```mermaid
sequenceDiagram
  participant Buyer App (BAP)
  participant Gateway
  participant Seller App (BPP)
  Buyer App (BAP)->>Gateway: /search (catalog search)
  Gateway->>Seller App (BPP): /search (forwarded)
  Seller App (BPP)-->>Buyer App (BAP): /on_search (catalog)
  Buyer App (BAP)->>Gateway: /search (station-to-station search)
  Gateway->>Seller App (BPP): /search (forwarded)
  Seller App (BPP)-->>Buyer App (BAP): /on_search (fares for station pair)
  Buyer App (BAP)->>Seller App (BPP): /select (select ticket)
  Seller App (BPP)-->>Buyer App (BAP): /on_select (quote)
  Buyer App (BAP)->>Seller App (BPP): /init (initialise order)
  Seller App (BPP)-->>Buyer App (BAP): /on_init (order details)
  Buyer App (BAP)->>Seller App (BPP): /confirm (confirm order)
  Seller App (BPP)-->>Buyer App (BAP): /on_confirm (delayed order confirmation)
  Buyer App (BAP)->>Seller App (BPP): /status (status check)
  rect rgb(191, 223, 255)
  Seller App (BPP)-->>Buyer App (BAP): /on_status (order active)
  end
  Buyer App (BAP)->>Seller App (BPP): /cancel (technical cancel)
  Seller App (BPP)-->>Buyer App (BAP): /on_cancel (order cancelled (technical))
```

## cancel_tech_BUS_200

```mermaid
sequenceDiagram
  participant Buyer App (BAP)
  participant Gateway
  participant Seller App (BPP)
  Buyer App (BAP)->>Gateway: /search (catalog search)
  Gateway->>Seller App (BPP): /search (forwarded)
  Seller App (BPP)-->>Buyer App (BAP): /on_search (catalog)
  Buyer App (BAP)->>Gateway: /search (station-to-station search)
  Gateway->>Seller App (BPP): /search (forwarded)
  Seller App (BPP)-->>Buyer App (BAP): /on_search (fares for station pair)
  Buyer App (BAP)->>Seller App (BPP): /select (select ticket)
  Seller App (BPP)-->>Buyer App (BAP): /on_select (quote)
  Buyer App (BAP)->>Seller App (BPP): /init (initialise order)
  Seller App (BPP)-->>Buyer App (BAP): /on_init (order details)
  Buyer App (BAP)->>Seller App (BPP): /confirm (confirm order)
  Seller App (BPP)-->>Buyer App (BAP): /on_confirm (delayed order confirmation)
  Buyer App (BAP)->>Seller App (BPP): /status (status check)
  Seller App (BPP)-->>Buyer App (BAP): /on_status (order active)
  rect rgb(191, 223, 255)
  Buyer App (BAP)->>Seller App (BPP): /cancel (technical cancel)
  end
  Seller App (BPP)-->>Buyer App (BAP): /on_cancel (order cancelled (technical))
```

## on_cancel_tech_BUS_200

```mermaid
sequenceDiagram
  participant Buyer App (BAP)
  participant Gateway
  participant Seller App (BPP)
  Buyer App (BAP)->>Gateway: /search (catalog search)
  Gateway->>Seller App (BPP): /search (forwarded)
  Seller App (BPP)-->>Buyer App (BAP): /on_search (catalog)
  Buyer App (BAP)->>Gateway: /search (station-to-station search)
  Gateway->>Seller App (BPP): /search (forwarded)
  Seller App (BPP)-->>Buyer App (BAP): /on_search (fares for station pair)
  Buyer App (BAP)->>Seller App (BPP): /select (select ticket)
  Seller App (BPP)-->>Buyer App (BAP): /on_select (quote)
  Buyer App (BAP)->>Seller App (BPP): /init (initialise order)
  Seller App (BPP)-->>Buyer App (BAP): /on_init (order details)
  Buyer App (BAP)->>Seller App (BPP): /confirm (confirm order)
  Seller App (BPP)-->>Buyer App (BAP): /on_confirm (delayed order confirmation)
  Buyer App (BAP)->>Seller App (BPP): /status (status check)
  Seller App (BPP)-->>Buyer App (BAP): /on_status (order active)
  Buyer App (BAP)->>Seller App (BPP): /cancel (technical cancel)
  rect rgb(191, 223, 255)
  Seller App (BPP)-->>Buyer App (BAP): /on_cancel (order cancelled (technical))
  end
```

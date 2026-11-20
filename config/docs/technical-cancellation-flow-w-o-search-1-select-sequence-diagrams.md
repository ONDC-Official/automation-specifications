# TECHNICAL_CANCELLATION_FLOW (W/O search_1 & select) — Sequence Diagrams

Internal data file consumed by the Developer Guide's "Sequence Diagram" tab (API Walkthrough).
Not meant to be shown as its own docs page — the frontend filters this slug out of the Use Case
Brief / Additional Resources / Changelog tab lists and instead looks up the section matching the
selected API call's `action_id` (the `##` heading below) to render that step's diagram.

One `## <action_id>` heading per step of `TECHNICAL_CANCELLATION_FLOW_WITHOUT_SEARCH_ND_SELECT.yaml` (Metro), in that flow's own step order, each followed by its Mermaid `sequenceDiagram`: the whole flow, with that call's own message(s) highlighted — same convention as the other domains' per-step sequence-diagram docs.

## search2_METRO_200

```mermaid
sequenceDiagram
  participant Buyer App (BAP)
  participant Gateway
  participant Seller App (BPP)
  rect rgb(191, 223, 255)
  Buyer App (BAP)->>Gateway: /search (station-to-station search)
  Gateway->>Seller App (BPP): /search (forwarded)
  end
  Seller App (BPP)-->>Buyer App (BAP): /on_search (single journey ticket fares)
  Buyer App (BAP)->>Seller App (BPP): /init (initialise order)
  Seller App (BPP)-->>Buyer App (BAP): /on_init (order details)
  Buyer App (BAP)->>Seller App (BPP): /confirm (confirm order)
  Seller App (BPP)-->>Buyer App (BAP): /on_confirm (delayed order confirmation)
  Buyer App (BAP)->>Seller App (BPP): /status (status check)
  Seller App (BPP)-->>Buyer App (BAP): /on_status (order active)
  Buyer App (BAP)->>Seller App (BPP): /cancel (technical cancel)
  Seller App (BPP)-->>Buyer App (BAP): /on_cancel (order cancelled (technical))
```

## on_search2_Sjt_METRO_200

```mermaid
sequenceDiagram
  participant Buyer App (BAP)
  participant Gateway
  participant Seller App (BPP)
  Buyer App (BAP)->>Gateway: /search (station-to-station search)
  Gateway->>Seller App (BPP): /search (forwarded)
  rect rgb(191, 223, 255)
  Seller App (BPP)-->>Buyer App (BAP): /on_search (single journey ticket fares)
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

## init_with_user_input_METRO_200

```mermaid
sequenceDiagram
  participant Buyer App (BAP)
  participant Gateway
  participant Seller App (BPP)
  Buyer App (BAP)->>Gateway: /search (station-to-station search)
  Gateway->>Seller App (BPP): /search (forwarded)
  Seller App (BPP)-->>Buyer App (BAP): /on_search (single journey ticket fares)
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

## on_init_METRO_200

```mermaid
sequenceDiagram
  participant Buyer App (BAP)
  participant Gateway
  participant Seller App (BPP)
  Buyer App (BAP)->>Gateway: /search (station-to-station search)
  Gateway->>Seller App (BPP): /search (forwarded)
  Seller App (BPP)-->>Buyer App (BAP): /on_search (single journey ticket fares)
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

## confirm_METRO_200

```mermaid
sequenceDiagram
  participant Buyer App (BAP)
  participant Gateway
  participant Seller App (BPP)
  Buyer App (BAP)->>Gateway: /search (station-to-station search)
  Gateway->>Seller App (BPP): /search (forwarded)
  Seller App (BPP)-->>Buyer App (BAP): /on_search (single journey ticket fares)
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

## on_confirm_delayed_METRO_200

```mermaid
sequenceDiagram
  participant Buyer App (BAP)
  participant Gateway
  participant Seller App (BPP)
  Buyer App (BAP)->>Gateway: /search (station-to-station search)
  Gateway->>Seller App (BPP): /search (forwarded)
  Seller App (BPP)-->>Buyer App (BAP): /on_search (single journey ticket fares)
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

## status_tech_cancel_METRO_200

```mermaid
sequenceDiagram
  participant Buyer App (BAP)
  participant Gateway
  participant Seller App (BPP)
  Buyer App (BAP)->>Gateway: /search (station-to-station search)
  Gateway->>Seller App (BPP): /search (forwarded)
  Seller App (BPP)-->>Buyer App (BAP): /on_search (single journey ticket fares)
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

## on_status_active_METRO_200

```mermaid
sequenceDiagram
  participant Buyer App (BAP)
  participant Gateway
  participant Seller App (BPP)
  Buyer App (BAP)->>Gateway: /search (station-to-station search)
  Gateway->>Seller App (BPP): /search (forwarded)
  Seller App (BPP)-->>Buyer App (BAP): /on_search (single journey ticket fares)
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

## cancel_tech_METRO_200

```mermaid
sequenceDiagram
  participant Buyer App (BAP)
  participant Gateway
  participant Seller App (BPP)
  Buyer App (BAP)->>Gateway: /search (station-to-station search)
  Gateway->>Seller App (BPP): /search (forwarded)
  Seller App (BPP)-->>Buyer App (BAP): /on_search (single journey ticket fares)
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

## on_cancel_tech_METRO_200

```mermaid
sequenceDiagram
  participant Buyer App (BAP)
  participant Gateway
  participant Seller App (BPP)
  Buyer App (BAP)->>Gateway: /search (station-to-station search)
  Gateway->>Seller App (BPP): /search (forwarded)
  Seller App (BPP)-->>Buyer App (BAP): /on_search (single journey ticket fares)
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

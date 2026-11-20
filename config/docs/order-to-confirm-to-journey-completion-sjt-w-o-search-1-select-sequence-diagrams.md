# ORDER_TO_CONFIRM_TO_JOURNEY_COMPLETION_SJT (W/O search_1 & select) — Sequence Diagrams

Internal data file consumed by the Developer Guide's "Sequence Diagram" tab (API Walkthrough).
Not meant to be shown as its own docs page — the frontend filters this slug out of the Use Case
Brief / Additional Resources / Changelog tab lists and instead looks up the section matching the
selected API call's `action_id` (the `##` heading below) to render that step's diagram.

One `## <action_id>` heading per step of `ORDER_TO_CONFIRM_TO_JOURNEY_COMPLETION_SJT_WITHOUT_SEARCH_ND_SELECT.yaml` (Metro), in that flow's own step order, each followed by its Mermaid `sequenceDiagram`: the whole flow, with that call's own message(s) highlighted — same convention as the other domains' per-step sequence-diagram docs.

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
  Seller App (BPP)-->>Buyer App (BAP): /on_confirm (order confirmed)
  Buyer App (BAP)->>Seller App (BPP): /status (order status)
  Seller App (BPP)-->>Buyer App (BAP): /on_status (journey completed)
  Seller App (BPP)-->>Buyer App (BAP): /on_status (unsolicited): journey completed
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
  Seller App (BPP)-->>Buyer App (BAP): /on_confirm (order confirmed)
  Buyer App (BAP)->>Seller App (BPP): /status (order status)
  Seller App (BPP)-->>Buyer App (BAP): /on_status (journey completed)
  Seller App (BPP)-->>Buyer App (BAP): /on_status (unsolicited): journey completed
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
  Seller App (BPP)-->>Buyer App (BAP): /on_confirm (order confirmed)
  Buyer App (BAP)->>Seller App (BPP): /status (order status)
  Seller App (BPP)-->>Buyer App (BAP): /on_status (journey completed)
  Seller App (BPP)-->>Buyer App (BAP): /on_status (unsolicited): journey completed
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
  Seller App (BPP)-->>Buyer App (BAP): /on_confirm (order confirmed)
  Buyer App (BAP)->>Seller App (BPP): /status (order status)
  Seller App (BPP)-->>Buyer App (BAP): /on_status (journey completed)
  Seller App (BPP)-->>Buyer App (BAP): /on_status (unsolicited): journey completed
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
  Seller App (BPP)-->>Buyer App (BAP): /on_confirm (order confirmed)
  Buyer App (BAP)->>Seller App (BPP): /status (order status)
  Seller App (BPP)-->>Buyer App (BAP): /on_status (journey completed)
  Seller App (BPP)-->>Buyer App (BAP): /on_status (unsolicited): journey completed
```

## on_confirm_METRO_200

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
  Seller App (BPP)-->>Buyer App (BAP): /on_confirm (order confirmed)
  end
  Buyer App (BAP)->>Seller App (BPP): /status (order status)
  Seller App (BPP)-->>Buyer App (BAP): /on_status (journey completed)
  Seller App (BPP)-->>Buyer App (BAP): /on_status (unsolicited): journey completed
```

## status_METRO_200

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
  Seller App (BPP)-->>Buyer App (BAP): /on_confirm (order confirmed)
  rect rgb(191, 223, 255)
  Buyer App (BAP)->>Seller App (BPP): /status (order status)
  end
  Seller App (BPP)-->>Buyer App (BAP): /on_status (journey completed)
  Seller App (BPP)-->>Buyer App (BAP): /on_status (unsolicited): journey completed
```

## on_status_complete_METRO_200

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
  Seller App (BPP)-->>Buyer App (BAP): /on_confirm (order confirmed)
  Buyer App (BAP)->>Seller App (BPP): /status (order status)
  rect rgb(191, 223, 255)
  Seller App (BPP)-->>Buyer App (BAP): /on_status (journey completed)
  end
  Seller App (BPP)-->>Buyer App (BAP): /on_status (unsolicited): journey completed
```

## unsoliciated_on_status_complete_METRO_200

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
  Seller App (BPP)-->>Buyer App (BAP): /on_confirm (order confirmed)
  Buyer App (BAP)->>Seller App (BPP): /status (order status)
  Seller App (BPP)-->>Buyer App (BAP): /on_status (journey completed)
  rect rgb(191, 223, 255)
  Seller App (BPP)-->>Buyer App (BAP): /on_status (unsolicited): journey completed
  end
```

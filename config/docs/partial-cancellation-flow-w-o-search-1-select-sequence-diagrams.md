# PARTIAL_CANCELLATION_FLOW (W/O search_1 & select) — Sequence Diagrams

Internal data file consumed by the Developer Guide's "Sequence Diagram" tab (API Walkthrough).
Not meant to be shown as its own docs page — the frontend filters this slug out of the Use Case
Brief / Additional Resources / Changelog tab lists and instead looks up the section matching the
selected API call's `action_id` (the `##` heading below) to render that step's diagram.

One `## <action_id>` heading per step of `PARTIAL_CANCELLATION_FLOW_WITHOUT_SEARCH_ND_SELECT.yaml` (Metro), in that flow's own step order, each followed by its Mermaid `sequenceDiagram`: the whole flow, with that call's own message(s) highlighted — same convention as the other domains' per-step sequence-diagram docs.

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
  Buyer App (BAP)->>Seller App (BPP): /update (partial cancellation: soft cancel request)
  Seller App (BPP)-->>Buyer App (BAP): /on_update (soft cancel response)
  Buyer App (BAP)->>Seller App (BPP): /update (partial cancellation: confirm cancel request)
  Seller App (BPP)-->>Buyer App (BAP): /on_update (partial cancellation confirmed)
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
  Buyer App (BAP)->>Seller App (BPP): /update (partial cancellation: soft cancel request)
  Seller App (BPP)-->>Buyer App (BAP): /on_update (soft cancel response)
  Buyer App (BAP)->>Seller App (BPP): /update (partial cancellation: confirm cancel request)
  Seller App (BPP)-->>Buyer App (BAP): /on_update (partial cancellation confirmed)
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
  Buyer App (BAP)->>Seller App (BPP): /update (partial cancellation: soft cancel request)
  Seller App (BPP)-->>Buyer App (BAP): /on_update (soft cancel response)
  Buyer App (BAP)->>Seller App (BPP): /update (partial cancellation: confirm cancel request)
  Seller App (BPP)-->>Buyer App (BAP): /on_update (partial cancellation confirmed)
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
  Buyer App (BAP)->>Seller App (BPP): /update (partial cancellation: soft cancel request)
  Seller App (BPP)-->>Buyer App (BAP): /on_update (soft cancel response)
  Buyer App (BAP)->>Seller App (BPP): /update (partial cancellation: confirm cancel request)
  Seller App (BPP)-->>Buyer App (BAP): /on_update (partial cancellation confirmed)
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
  Buyer App (BAP)->>Seller App (BPP): /update (partial cancellation: soft cancel request)
  Seller App (BPP)-->>Buyer App (BAP): /on_update (soft cancel response)
  Buyer App (BAP)->>Seller App (BPP): /update (partial cancellation: confirm cancel request)
  Seller App (BPP)-->>Buyer App (BAP): /on_update (partial cancellation confirmed)
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
  Buyer App (BAP)->>Seller App (BPP): /update (partial cancellation: soft cancel request)
  Seller App (BPP)-->>Buyer App (BAP): /on_update (soft cancel response)
  Buyer App (BAP)->>Seller App (BPP): /update (partial cancellation: confirm cancel request)
  Seller App (BPP)-->>Buyer App (BAP): /on_update (partial cancellation confirmed)
```

## update_METRO_201

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
  Buyer App (BAP)->>Seller App (BPP): /update (partial cancellation: soft cancel request)
  end
  Seller App (BPP)-->>Buyer App (BAP): /on_update (soft cancel response)
  Buyer App (BAP)->>Seller App (BPP): /update (partial cancellation: confirm cancel request)
  Seller App (BPP)-->>Buyer App (BAP): /on_update (partial cancellation confirmed)
```

## on_update_METRO_201

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
  Buyer App (BAP)->>Seller App (BPP): /update (partial cancellation: soft cancel request)
  rect rgb(191, 223, 255)
  Seller App (BPP)-->>Buyer App (BAP): /on_update (soft cancel response)
  end
  Buyer App (BAP)->>Seller App (BPP): /update (partial cancellation: confirm cancel request)
  Seller App (BPP)-->>Buyer App (BAP): /on_update (partial cancellation confirmed)
```

## update_METRO_202

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
  Buyer App (BAP)->>Seller App (BPP): /update (partial cancellation: soft cancel request)
  Seller App (BPP)-->>Buyer App (BAP): /on_update (soft cancel response)
  rect rgb(191, 223, 255)
  Buyer App (BAP)->>Seller App (BPP): /update (partial cancellation: confirm cancel request)
  end
  Seller App (BPP)-->>Buyer App (BAP): /on_update (partial cancellation confirmed)
```

## on_update_METRO_202

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
  Buyer App (BAP)->>Seller App (BPP): /update (partial cancellation: soft cancel request)
  Seller App (BPP)-->>Buyer App (BAP): /on_update (soft cancel response)
  Buyer App (BAP)->>Seller App (BPP): /update (partial cancellation: confirm cancel request)
  rect rgb(191, 223, 255)
  Seller App (BPP)-->>Buyer App (BAP): /on_update (partial cancellation confirmed)
  end
```

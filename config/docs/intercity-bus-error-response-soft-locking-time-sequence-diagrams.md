# Intercity(Bus) Error Response(Soft Locking Time) — Sequence Diagrams

Internal data file consumed by the Developer Guide's "Sequence Diagram" tab (API Walkthrough).
Not meant to be shown as its own docs page — the frontend filters this slug out of the Use Case
Brief / Additional Resources / Changelog tab lists and instead looks up the section matching the
selected API call's `action_id` (the `##` heading below) to render that step's diagram.

One `## <action_id>` heading per step of `Intercity_Bus__Error_Response_Soft_Locking_Time_.yaml`, in that flow's own step order, each followed by its Mermaid `sequenceDiagram`: the whole flow, with that call's own message(s) highlighted — same convention as the other domains' per-step sequence-diagram docs.

## search_BUS_201

```mermaid
sequenceDiagram
  participant Buyer App (BAP)
  participant Gateway
  participant Seller App (BPP)
  rect rgb(191, 223, 255)
  Buyer App (BAP)->>Gateway: /search (bus search)
  Gateway->>Seller App (BPP): /search (forwarded)
  end
  Seller App (BPP)-->>Buyer App (BAP): /on_search (batch 1: bus catalog)
  Buyer App (BAP)->>Gateway: /search (incremental search / filter)
  Gateway->>Seller App (BPP): /search (forwarded)
  Seller App (BPP)-->>Buyer App (BAP): /on_search (batch 2: bus catalog)
  Buyer App (BAP)->>Gateway: /search (final search pull)
  Gateway->>Seller App (BPP): /search (forwarded)
  Seller App (BPP)-->>Buyer App (BAP): /on_search (batch 3: bus catalog)
  Buyer App (BAP)->>Seller App (BPP): /select (select bus route & seat)
  Seller App (BPP)-->>Buyer App (BAP): /on_select (quote, seat availability)
  Buyer App (BAP)->>Seller App (BPP): /select (boarding & dropping points)
  Seller App (BPP)-->>Buyer App (BAP): /on_select (updated quote with stops)
  Buyer App (BAP)->>Seller App (BPP): /init (passenger details, billing)
  Seller App (BPP)-->>Buyer App (BAP): /on_init (NACK: soft lock timeout expired)
```

## on_search_BUS_201

```mermaid
sequenceDiagram
  participant Buyer App (BAP)
  participant Gateway
  participant Seller App (BPP)
  Buyer App (BAP)->>Gateway: /search (bus search)
  Gateway->>Seller App (BPP): /search (forwarded)
  rect rgb(191, 223, 255)
  Seller App (BPP)-->>Buyer App (BAP): /on_search (batch 1: bus catalog)
  end
  Buyer App (BAP)->>Gateway: /search (incremental search / filter)
  Gateway->>Seller App (BPP): /search (forwarded)
  Seller App (BPP)-->>Buyer App (BAP): /on_search (batch 2: bus catalog)
  Buyer App (BAP)->>Gateway: /search (final search pull)
  Gateway->>Seller App (BPP): /search (forwarded)
  Seller App (BPP)-->>Buyer App (BAP): /on_search (batch 3: bus catalog)
  Buyer App (BAP)->>Seller App (BPP): /select (select bus route & seat)
  Seller App (BPP)-->>Buyer App (BAP): /on_select (quote, seat availability)
  Buyer App (BAP)->>Seller App (BPP): /select (boarding & dropping points)
  Seller App (BPP)-->>Buyer App (BAP): /on_select (updated quote with stops)
  Buyer App (BAP)->>Seller App (BPP): /init (passenger details, billing)
  Seller App (BPP)-->>Buyer App (BAP): /on_init (NACK: soft lock timeout expired)
```

## search_BUS_202

```mermaid
sequenceDiagram
  participant Buyer App (BAP)
  participant Gateway
  participant Seller App (BPP)
  Buyer App (BAP)->>Gateway: /search (bus search)
  Gateway->>Seller App (BPP): /search (forwarded)
  Seller App (BPP)-->>Buyer App (BAP): /on_search (batch 1: bus catalog)
  rect rgb(191, 223, 255)
  Buyer App (BAP)->>Gateway: /search (incremental search / filter)
  Gateway->>Seller App (BPP): /search (forwarded)
  end
  Seller App (BPP)-->>Buyer App (BAP): /on_search (batch 2: bus catalog)
  Buyer App (BAP)->>Gateway: /search (final search pull)
  Gateway->>Seller App (BPP): /search (forwarded)
  Seller App (BPP)-->>Buyer App (BAP): /on_search (batch 3: bus catalog)
  Buyer App (BAP)->>Seller App (BPP): /select (select bus route & seat)
  Seller App (BPP)-->>Buyer App (BAP): /on_select (quote, seat availability)
  Buyer App (BAP)->>Seller App (BPP): /select (boarding & dropping points)
  Seller App (BPP)-->>Buyer App (BAP): /on_select (updated quote with stops)
  Buyer App (BAP)->>Seller App (BPP): /init (passenger details, billing)
  Seller App (BPP)-->>Buyer App (BAP): /on_init (NACK: soft lock timeout expired)
```

## on_search_BUS_202

```mermaid
sequenceDiagram
  participant Buyer App (BAP)
  participant Gateway
  participant Seller App (BPP)
  Buyer App (BAP)->>Gateway: /search (bus search)
  Gateway->>Seller App (BPP): /search (forwarded)
  Seller App (BPP)-->>Buyer App (BAP): /on_search (batch 1: bus catalog)
  Buyer App (BAP)->>Gateway: /search (incremental search / filter)
  Gateway->>Seller App (BPP): /search (forwarded)
  rect rgb(191, 223, 255)
  Seller App (BPP)-->>Buyer App (BAP): /on_search (batch 2: bus catalog)
  end
  Buyer App (BAP)->>Gateway: /search (final search pull)
  Gateway->>Seller App (BPP): /search (forwarded)
  Seller App (BPP)-->>Buyer App (BAP): /on_search (batch 3: bus catalog)
  Buyer App (BAP)->>Seller App (BPP): /select (select bus route & seat)
  Seller App (BPP)-->>Buyer App (BAP): /on_select (quote, seat availability)
  Buyer App (BAP)->>Seller App (BPP): /select (boarding & dropping points)
  Seller App (BPP)-->>Buyer App (BAP): /on_select (updated quote with stops)
  Buyer App (BAP)->>Seller App (BPP): /init (passenger details, billing)
  Seller App (BPP)-->>Buyer App (BAP): /on_init (NACK: soft lock timeout expired)
```

## search_BUS_203

```mermaid
sequenceDiagram
  participant Buyer App (BAP)
  participant Gateway
  participant Seller App (BPP)
  Buyer App (BAP)->>Gateway: /search (bus search)
  Gateway->>Seller App (BPP): /search (forwarded)
  Seller App (BPP)-->>Buyer App (BAP): /on_search (batch 1: bus catalog)
  Buyer App (BAP)->>Gateway: /search (incremental search / filter)
  Gateway->>Seller App (BPP): /search (forwarded)
  Seller App (BPP)-->>Buyer App (BAP): /on_search (batch 2: bus catalog)
  rect rgb(191, 223, 255)
  Buyer App (BAP)->>Gateway: /search (final search pull)
  Gateway->>Seller App (BPP): /search (forwarded)
  end
  Seller App (BPP)-->>Buyer App (BAP): /on_search (batch 3: bus catalog)
  Buyer App (BAP)->>Seller App (BPP): /select (select bus route & seat)
  Seller App (BPP)-->>Buyer App (BAP): /on_select (quote, seat availability)
  Buyer App (BAP)->>Seller App (BPP): /select (boarding & dropping points)
  Seller App (BPP)-->>Buyer App (BAP): /on_select (updated quote with stops)
  Buyer App (BAP)->>Seller App (BPP): /init (passenger details, billing)
  Seller App (BPP)-->>Buyer App (BAP): /on_init (NACK: soft lock timeout expired)
```

## on_search_BUS_203

```mermaid
sequenceDiagram
  participant Buyer App (BAP)
  participant Gateway
  participant Seller App (BPP)
  Buyer App (BAP)->>Gateway: /search (bus search)
  Gateway->>Seller App (BPP): /search (forwarded)
  Seller App (BPP)-->>Buyer App (BAP): /on_search (batch 1: bus catalog)
  Buyer App (BAP)->>Gateway: /search (incremental search / filter)
  Gateway->>Seller App (BPP): /search (forwarded)
  Seller App (BPP)-->>Buyer App (BAP): /on_search (batch 2: bus catalog)
  Buyer App (BAP)->>Gateway: /search (final search pull)
  Gateway->>Seller App (BPP): /search (forwarded)
  rect rgb(191, 223, 255)
  Seller App (BPP)-->>Buyer App (BAP): /on_search (batch 3: bus catalog)
  end
  Buyer App (BAP)->>Seller App (BPP): /select (select bus route & seat)
  Seller App (BPP)-->>Buyer App (BAP): /on_select (quote, seat availability)
  Buyer App (BAP)->>Seller App (BPP): /select (boarding & dropping points)
  Seller App (BPP)-->>Buyer App (BAP): /on_select (updated quote with stops)
  Buyer App (BAP)->>Seller App (BPP): /init (passenger details, billing)
  Seller App (BPP)-->>Buyer App (BAP): /on_init (NACK: soft lock timeout expired)
```

## select_BUS_201

```mermaid
sequenceDiagram
  participant Buyer App (BAP)
  participant Gateway
  participant Seller App (BPP)
  Buyer App (BAP)->>Gateway: /search (bus search)
  Gateway->>Seller App (BPP): /search (forwarded)
  Seller App (BPP)-->>Buyer App (BAP): /on_search (batch 1: bus catalog)
  Buyer App (BAP)->>Gateway: /search (incremental search / filter)
  Gateway->>Seller App (BPP): /search (forwarded)
  Seller App (BPP)-->>Buyer App (BAP): /on_search (batch 2: bus catalog)
  Buyer App (BAP)->>Gateway: /search (final search pull)
  Gateway->>Seller App (BPP): /search (forwarded)
  Seller App (BPP)-->>Buyer App (BAP): /on_search (batch 3: bus catalog)
  rect rgb(191, 223, 255)
  Buyer App (BAP)->>Seller App (BPP): /select (select bus route & seat)
  end
  Seller App (BPP)-->>Buyer App (BAP): /on_select (quote, seat availability)
  Buyer App (BAP)->>Seller App (BPP): /select (boarding & dropping points)
  Seller App (BPP)-->>Buyer App (BAP): /on_select (updated quote with stops)
  Buyer App (BAP)->>Seller App (BPP): /init (passenger details, billing)
  Seller App (BPP)-->>Buyer App (BAP): /on_init (NACK: soft lock timeout expired)
```

## on_select_BUS_201

```mermaid
sequenceDiagram
  participant Buyer App (BAP)
  participant Gateway
  participant Seller App (BPP)
  Buyer App (BAP)->>Gateway: /search (bus search)
  Gateway->>Seller App (BPP): /search (forwarded)
  Seller App (BPP)-->>Buyer App (BAP): /on_search (batch 1: bus catalog)
  Buyer App (BAP)->>Gateway: /search (incremental search / filter)
  Gateway->>Seller App (BPP): /search (forwarded)
  Seller App (BPP)-->>Buyer App (BAP): /on_search (batch 2: bus catalog)
  Buyer App (BAP)->>Gateway: /search (final search pull)
  Gateway->>Seller App (BPP): /search (forwarded)
  Seller App (BPP)-->>Buyer App (BAP): /on_search (batch 3: bus catalog)
  Buyer App (BAP)->>Seller App (BPP): /select (select bus route & seat)
  rect rgb(191, 223, 255)
  Seller App (BPP)-->>Buyer App (BAP): /on_select (quote, seat availability)
  end
  Buyer App (BAP)->>Seller App (BPP): /select (boarding & dropping points)
  Seller App (BPP)-->>Buyer App (BAP): /on_select (updated quote with stops)
  Buyer App (BAP)->>Seller App (BPP): /init (passenger details, billing)
  Seller App (BPP)-->>Buyer App (BAP): /on_init (NACK: soft lock timeout expired)
```

## select_BUS_202

```mermaid
sequenceDiagram
  participant Buyer App (BAP)
  participant Gateway
  participant Seller App (BPP)
  Buyer App (BAP)->>Gateway: /search (bus search)
  Gateway->>Seller App (BPP): /search (forwarded)
  Seller App (BPP)-->>Buyer App (BAP): /on_search (batch 1: bus catalog)
  Buyer App (BAP)->>Gateway: /search (incremental search / filter)
  Gateway->>Seller App (BPP): /search (forwarded)
  Seller App (BPP)-->>Buyer App (BAP): /on_search (batch 2: bus catalog)
  Buyer App (BAP)->>Gateway: /search (final search pull)
  Gateway->>Seller App (BPP): /search (forwarded)
  Seller App (BPP)-->>Buyer App (BAP): /on_search (batch 3: bus catalog)
  Buyer App (BAP)->>Seller App (BPP): /select (select bus route & seat)
  Seller App (BPP)-->>Buyer App (BAP): /on_select (quote, seat availability)
  rect rgb(191, 223, 255)
  Buyer App (BAP)->>Seller App (BPP): /select (boarding & dropping points)
  end
  Seller App (BPP)-->>Buyer App (BAP): /on_select (updated quote with stops)
  Buyer App (BAP)->>Seller App (BPP): /init (passenger details, billing)
  Seller App (BPP)-->>Buyer App (BAP): /on_init (NACK: soft lock timeout expired)
```

## on_select_BUS_202

```mermaid
sequenceDiagram
  participant Buyer App (BAP)
  participant Gateway
  participant Seller App (BPP)
  Buyer App (BAP)->>Gateway: /search (bus search)
  Gateway->>Seller App (BPP): /search (forwarded)
  Seller App (BPP)-->>Buyer App (BAP): /on_search (batch 1: bus catalog)
  Buyer App (BAP)->>Gateway: /search (incremental search / filter)
  Gateway->>Seller App (BPP): /search (forwarded)
  Seller App (BPP)-->>Buyer App (BAP): /on_search (batch 2: bus catalog)
  Buyer App (BAP)->>Gateway: /search (final search pull)
  Gateway->>Seller App (BPP): /search (forwarded)
  Seller App (BPP)-->>Buyer App (BAP): /on_search (batch 3: bus catalog)
  Buyer App (BAP)->>Seller App (BPP): /select (select bus route & seat)
  Seller App (BPP)-->>Buyer App (BAP): /on_select (quote, seat availability)
  Buyer App (BAP)->>Seller App (BPP): /select (boarding & dropping points)
  rect rgb(191, 223, 255)
  Seller App (BPP)-->>Buyer App (BAP): /on_select (updated quote with stops)
  end
  Buyer App (BAP)->>Seller App (BPP): /init (passenger details, billing)
  Seller App (BPP)-->>Buyer App (BAP): /on_init (NACK: soft lock timeout expired)
```

## init_BUS_201

```mermaid
sequenceDiagram
  participant Buyer App (BAP)
  participant Gateway
  participant Seller App (BPP)
  Buyer App (BAP)->>Gateway: /search (bus search)
  Gateway->>Seller App (BPP): /search (forwarded)
  Seller App (BPP)-->>Buyer App (BAP): /on_search (batch 1: bus catalog)
  Buyer App (BAP)->>Gateway: /search (incremental search / filter)
  Gateway->>Seller App (BPP): /search (forwarded)
  Seller App (BPP)-->>Buyer App (BAP): /on_search (batch 2: bus catalog)
  Buyer App (BAP)->>Gateway: /search (final search pull)
  Gateway->>Seller App (BPP): /search (forwarded)
  Seller App (BPP)-->>Buyer App (BAP): /on_search (batch 3: bus catalog)
  Buyer App (BAP)->>Seller App (BPP): /select (select bus route & seat)
  Seller App (BPP)-->>Buyer App (BAP): /on_select (quote, seat availability)
  Buyer App (BAP)->>Seller App (BPP): /select (boarding & dropping points)
  Seller App (BPP)-->>Buyer App (BAP): /on_select (updated quote with stops)
  rect rgb(191, 223, 255)
  Buyer App (BAP)->>Seller App (BPP): /init (passenger details, billing)
  end
  Seller App (BPP)-->>Buyer App (BAP): /on_init (NACK: soft lock timeout expired)
```

## on_init_BUS_221

```mermaid
sequenceDiagram
  participant Buyer App (BAP)
  participant Gateway
  participant Seller App (BPP)
  Buyer App (BAP)->>Gateway: /search (bus search)
  Gateway->>Seller App (BPP): /search (forwarded)
  Seller App (BPP)-->>Buyer App (BAP): /on_search (batch 1: bus catalog)
  Buyer App (BAP)->>Gateway: /search (incremental search / filter)
  Gateway->>Seller App (BPP): /search (forwarded)
  Seller App (BPP)-->>Buyer App (BAP): /on_search (batch 2: bus catalog)
  Buyer App (BAP)->>Gateway: /search (final search pull)
  Gateway->>Seller App (BPP): /search (forwarded)
  Seller App (BPP)-->>Buyer App (BAP): /on_search (batch 3: bus catalog)
  Buyer App (BAP)->>Seller App (BPP): /select (select bus route & seat)
  Seller App (BPP)-->>Buyer App (BAP): /on_select (quote, seat availability)
  Buyer App (BAP)->>Seller App (BPP): /select (boarding & dropping points)
  Seller App (BPP)-->>Buyer App (BAP): /on_select (updated quote with stops)
  Buyer App (BAP)->>Seller App (BPP): /init (passenger details, billing)
  rect rgb(191, 223, 255)
  Seller App (BPP)-->>Buyer App (BAP): /on_init (NACK: soft lock timeout expired)
  end
```

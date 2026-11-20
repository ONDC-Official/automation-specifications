# Intercity(Bus) Rating(Success) — Sequence Diagrams

Internal data file consumed by the Developer Guide's "Sequence Diagram" tab (API Walkthrough).
Not meant to be shown as its own docs page — the frontend filters this slug out of the Use Case
Brief / Additional Resources / Changelog tab lists and instead looks up the section matching the
selected API call's `action_id` (the `##` heading below) to render that step's diagram.

One `## <action_id>` heading per step of `Intercity_Bus__Rating_Success_.yaml`, in that flow's own step order, each followed by its Mermaid `sequenceDiagram`: the whole flow, with that call's own message(s) highlighted — same convention as the other domains' per-step sequence-diagram docs.

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
  Seller App (BPP)-->>Buyer App (BAP): /on_init (final quote, payment terms)
  Buyer App (BAP)->>Seller App (BPP): /confirm (place bus booking)
  Seller App (BPP)-->>Buyer App (BAP): /on_confirm (booking confirmed, ticket issued)
  Seller App (BPP)-->>Buyer App (BAP): /on_status (unsolicited): trip completed
  Buyer App (BAP)->>Seller App (BPP): /rating (submit rating)
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
  Seller App (BPP)-->>Buyer App (BAP): /on_init (final quote, payment terms)
  Buyer App (BAP)->>Seller App (BPP): /confirm (place bus booking)
  Seller App (BPP)-->>Buyer App (BAP): /on_confirm (booking confirmed, ticket issued)
  Seller App (BPP)-->>Buyer App (BAP): /on_status (unsolicited): trip completed
  Buyer App (BAP)->>Seller App (BPP): /rating (submit rating)
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
  Seller App (BPP)-->>Buyer App (BAP): /on_init (final quote, payment terms)
  Buyer App (BAP)->>Seller App (BPP): /confirm (place bus booking)
  Seller App (BPP)-->>Buyer App (BAP): /on_confirm (booking confirmed, ticket issued)
  Seller App (BPP)-->>Buyer App (BAP): /on_status (unsolicited): trip completed
  Buyer App (BAP)->>Seller App (BPP): /rating (submit rating)
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
  Seller App (BPP)-->>Buyer App (BAP): /on_init (final quote, payment terms)
  Buyer App (BAP)->>Seller App (BPP): /confirm (place bus booking)
  Seller App (BPP)-->>Buyer App (BAP): /on_confirm (booking confirmed, ticket issued)
  Seller App (BPP)-->>Buyer App (BAP): /on_status (unsolicited): trip completed
  Buyer App (BAP)->>Seller App (BPP): /rating (submit rating)
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
  Seller App (BPP)-->>Buyer App (BAP): /on_init (final quote, payment terms)
  Buyer App (BAP)->>Seller App (BPP): /confirm (place bus booking)
  Seller App (BPP)-->>Buyer App (BAP): /on_confirm (booking confirmed, ticket issued)
  Seller App (BPP)-->>Buyer App (BAP): /on_status (unsolicited): trip completed
  Buyer App (BAP)->>Seller App (BPP): /rating (submit rating)
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
  Seller App (BPP)-->>Buyer App (BAP): /on_init (final quote, payment terms)
  Buyer App (BAP)->>Seller App (BPP): /confirm (place bus booking)
  Seller App (BPP)-->>Buyer App (BAP): /on_confirm (booking confirmed, ticket issued)
  Seller App (BPP)-->>Buyer App (BAP): /on_status (unsolicited): trip completed
  Buyer App (BAP)->>Seller App (BPP): /rating (submit rating)
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
  Seller App (BPP)-->>Buyer App (BAP): /on_init (final quote, payment terms)
  Buyer App (BAP)->>Seller App (BPP): /confirm (place bus booking)
  Seller App (BPP)-->>Buyer App (BAP): /on_confirm (booking confirmed, ticket issued)
  Seller App (BPP)-->>Buyer App (BAP): /on_status (unsolicited): trip completed
  Buyer App (BAP)->>Seller App (BPP): /rating (submit rating)
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
  Seller App (BPP)-->>Buyer App (BAP): /on_init (final quote, payment terms)
  Buyer App (BAP)->>Seller App (BPP): /confirm (place bus booking)
  Seller App (BPP)-->>Buyer App (BAP): /on_confirm (booking confirmed, ticket issued)
  Seller App (BPP)-->>Buyer App (BAP): /on_status (unsolicited): trip completed
  Buyer App (BAP)->>Seller App (BPP): /rating (submit rating)
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
  Seller App (BPP)-->>Buyer App (BAP): /on_init (final quote, payment terms)
  Buyer App (BAP)->>Seller App (BPP): /confirm (place bus booking)
  Seller App (BPP)-->>Buyer App (BAP): /on_confirm (booking confirmed, ticket issued)
  Seller App (BPP)-->>Buyer App (BAP): /on_status (unsolicited): trip completed
  Buyer App (BAP)->>Seller App (BPP): /rating (submit rating)
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
  Seller App (BPP)-->>Buyer App (BAP): /on_init (final quote, payment terms)
  Buyer App (BAP)->>Seller App (BPP): /confirm (place bus booking)
  Seller App (BPP)-->>Buyer App (BAP): /on_confirm (booking confirmed, ticket issued)
  Seller App (BPP)-->>Buyer App (BAP): /on_status (unsolicited): trip completed
  Buyer App (BAP)->>Seller App (BPP): /rating (submit rating)
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
  Seller App (BPP)-->>Buyer App (BAP): /on_init (final quote, payment terms)
  Buyer App (BAP)->>Seller App (BPP): /confirm (place bus booking)
  Seller App (BPP)-->>Buyer App (BAP): /on_confirm (booking confirmed, ticket issued)
  Seller App (BPP)-->>Buyer App (BAP): /on_status (unsolicited): trip completed
  Buyer App (BAP)->>Seller App (BPP): /rating (submit rating)
```

## on_init_BUS_201

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
  Seller App (BPP)-->>Buyer App (BAP): /on_init (final quote, payment terms)
  end
  Buyer App (BAP)->>Seller App (BPP): /confirm (place bus booking)
  Seller App (BPP)-->>Buyer App (BAP): /on_confirm (booking confirmed, ticket issued)
  Seller App (BPP)-->>Buyer App (BAP): /on_status (unsolicited): trip completed
  Buyer App (BAP)->>Seller App (BPP): /rating (submit rating)
```

## confirm_BUS_201

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
  Seller App (BPP)-->>Buyer App (BAP): /on_init (final quote, payment terms)
  rect rgb(191, 223, 255)
  Buyer App (BAP)->>Seller App (BPP): /confirm (place bus booking)
  end
  Seller App (BPP)-->>Buyer App (BAP): /on_confirm (booking confirmed, ticket issued)
  Seller App (BPP)-->>Buyer App (BAP): /on_status (unsolicited): trip completed
  Buyer App (BAP)->>Seller App (BPP): /rating (submit rating)
```

## on_confirm_BUS_201

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
  Seller App (BPP)-->>Buyer App (BAP): /on_init (final quote, payment terms)
  Buyer App (BAP)->>Seller App (BPP): /confirm (place bus booking)
  rect rgb(191, 223, 255)
  Seller App (BPP)-->>Buyer App (BAP): /on_confirm (booking confirmed, ticket issued)
  end
  Seller App (BPP)-->>Buyer App (BAP): /on_status (unsolicited): trip completed
  Buyer App (BAP)->>Seller App (BPP): /rating (submit rating)
```

## on_status_BUS_251

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
  Seller App (BPP)-->>Buyer App (BAP): /on_init (final quote, payment terms)
  Buyer App (BAP)->>Seller App (BPP): /confirm (place bus booking)
  Seller App (BPP)-->>Buyer App (BAP): /on_confirm (booking confirmed, ticket issued)
  rect rgb(191, 223, 255)
  Seller App (BPP)-->>Buyer App (BAP): /on_status (unsolicited): trip completed
  end
  Buyer App (BAP)->>Seller App (BPP): /rating (submit rating)
```

## rating_251

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
  Seller App (BPP)-->>Buyer App (BAP): /on_init (final quote, payment terms)
  Buyer App (BAP)->>Seller App (BPP): /confirm (place bus booking)
  Seller App (BPP)-->>Buyer App (BAP): /on_confirm (booking confirmed, ticket issued)
  Seller App (BPP)-->>Buyer App (BAP): /on_status (unsolicited): trip completed
  rect rgb(191, 223, 255)
  Buyer App (BAP)->>Seller App (BPP): /rating (submit rating)
  end
```

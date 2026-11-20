# Intercity_Bus__Station_Code_Based_Flow_With_IGM_Rejection_v-2.0.0 — Sequence Diagrams

Internal data file consumed by the Developer Guide's "Sequence Diagram" tab (API Walkthrough).
Not meant to be shown as its own docs page — the frontend filters this slug out of the Use Case
Brief / Additional Resources / Changelog tab lists and instead looks up the section matching the
selected API call's `action_id` (the `##` heading below) to render that step's diagram.

One `## <action_id>` heading per step of `Intercity_Bus__Station_Code_Based_Flow_With_IGM_Rejection_v-2.0.0.yaml`, in that flow's own step order, each followed by its Mermaid `sequenceDiagram`: the whole flow, with that call's own message(s) highlighted — same convention as the other domains' per-step sequence-diagram docs.

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
  Buyer App (BAP)->>Seller App (BPP): /status
  Seller App (BPP)-->>Buyer App (BAP): /on_status (active bus pass)
  Seller App (BPP)-->>Buyer App (BAP): /on_status (unsolicited): trip status update
  Buyer App (BAP)->>Seller App (BPP): /issue (open complaint)
  Seller App (BPP)-->>Buyer App (BAP): /on_issue (processing)
  Seller App (BPP)-->>Buyer App (BAP): /on_issue (unsolicited): resolution
  Buyer App (BAP)->>Seller App (BPP): /issue (reject resolution)
  Seller App (BPP)-->>Buyer App (BAP): /on_issue (processing)
  Seller App (BPP)-->>Buyer App (BAP): /on_issue (unsolicited): revised resolution
  Buyer App (BAP)->>Seller App (BPP): /issue (escalate)
  Seller App (BPP)-->>Buyer App (BAP): /on_issue (processing escalation)
  Seller App (BPP)-->>Buyer App (BAP): /on_issue (unsolicited): grievance resolution
  Buyer App (BAP)->>Seller App (BPP): /issue (accept resolution)
  Seller App (BPP)-->>Buyer App (BAP): /on_issue (resolved)
  Buyer App (BAP)->>Seller App (BPP): /issue (close)
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
  Buyer App (BAP)->>Seller App (BPP): /status
  Seller App (BPP)-->>Buyer App (BAP): /on_status (active bus pass)
  Seller App (BPP)-->>Buyer App (BAP): /on_status (unsolicited): trip status update
  Buyer App (BAP)->>Seller App (BPP): /issue (open complaint)
  Seller App (BPP)-->>Buyer App (BAP): /on_issue (processing)
  Seller App (BPP)-->>Buyer App (BAP): /on_issue (unsolicited): resolution
  Buyer App (BAP)->>Seller App (BPP): /issue (reject resolution)
  Seller App (BPP)-->>Buyer App (BAP): /on_issue (processing)
  Seller App (BPP)-->>Buyer App (BAP): /on_issue (unsolicited): revised resolution
  Buyer App (BAP)->>Seller App (BPP): /issue (escalate)
  Seller App (BPP)-->>Buyer App (BAP): /on_issue (processing escalation)
  Seller App (BPP)-->>Buyer App (BAP): /on_issue (unsolicited): grievance resolution
  Buyer App (BAP)->>Seller App (BPP): /issue (accept resolution)
  Seller App (BPP)-->>Buyer App (BAP): /on_issue (resolved)
  Buyer App (BAP)->>Seller App (BPP): /issue (close)
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
  Buyer App (BAP)->>Seller App (BPP): /status
  Seller App (BPP)-->>Buyer App (BAP): /on_status (active bus pass)
  Seller App (BPP)-->>Buyer App (BAP): /on_status (unsolicited): trip status update
  Buyer App (BAP)->>Seller App (BPP): /issue (open complaint)
  Seller App (BPP)-->>Buyer App (BAP): /on_issue (processing)
  Seller App (BPP)-->>Buyer App (BAP): /on_issue (unsolicited): resolution
  Buyer App (BAP)->>Seller App (BPP): /issue (reject resolution)
  Seller App (BPP)-->>Buyer App (BAP): /on_issue (processing)
  Seller App (BPP)-->>Buyer App (BAP): /on_issue (unsolicited): revised resolution
  Buyer App (BAP)->>Seller App (BPP): /issue (escalate)
  Seller App (BPP)-->>Buyer App (BAP): /on_issue (processing escalation)
  Seller App (BPP)-->>Buyer App (BAP): /on_issue (unsolicited): grievance resolution
  Buyer App (BAP)->>Seller App (BPP): /issue (accept resolution)
  Seller App (BPP)-->>Buyer App (BAP): /on_issue (resolved)
  Buyer App (BAP)->>Seller App (BPP): /issue (close)
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
  Buyer App (BAP)->>Seller App (BPP): /status
  Seller App (BPP)-->>Buyer App (BAP): /on_status (active bus pass)
  Seller App (BPP)-->>Buyer App (BAP): /on_status (unsolicited): trip status update
  Buyer App (BAP)->>Seller App (BPP): /issue (open complaint)
  Seller App (BPP)-->>Buyer App (BAP): /on_issue (processing)
  Seller App (BPP)-->>Buyer App (BAP): /on_issue (unsolicited): resolution
  Buyer App (BAP)->>Seller App (BPP): /issue (reject resolution)
  Seller App (BPP)-->>Buyer App (BAP): /on_issue (processing)
  Seller App (BPP)-->>Buyer App (BAP): /on_issue (unsolicited): revised resolution
  Buyer App (BAP)->>Seller App (BPP): /issue (escalate)
  Seller App (BPP)-->>Buyer App (BAP): /on_issue (processing escalation)
  Seller App (BPP)-->>Buyer App (BAP): /on_issue (unsolicited): grievance resolution
  Buyer App (BAP)->>Seller App (BPP): /issue (accept resolution)
  Seller App (BPP)-->>Buyer App (BAP): /on_issue (resolved)
  Buyer App (BAP)->>Seller App (BPP): /issue (close)
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
  Buyer App (BAP)->>Seller App (BPP): /status
  Seller App (BPP)-->>Buyer App (BAP): /on_status (active bus pass)
  Seller App (BPP)-->>Buyer App (BAP): /on_status (unsolicited): trip status update
  Buyer App (BAP)->>Seller App (BPP): /issue (open complaint)
  Seller App (BPP)-->>Buyer App (BAP): /on_issue (processing)
  Seller App (BPP)-->>Buyer App (BAP): /on_issue (unsolicited): resolution
  Buyer App (BAP)->>Seller App (BPP): /issue (reject resolution)
  Seller App (BPP)-->>Buyer App (BAP): /on_issue (processing)
  Seller App (BPP)-->>Buyer App (BAP): /on_issue (unsolicited): revised resolution
  Buyer App (BAP)->>Seller App (BPP): /issue (escalate)
  Seller App (BPP)-->>Buyer App (BAP): /on_issue (processing escalation)
  Seller App (BPP)-->>Buyer App (BAP): /on_issue (unsolicited): grievance resolution
  Buyer App (BAP)->>Seller App (BPP): /issue (accept resolution)
  Seller App (BPP)-->>Buyer App (BAP): /on_issue (resolved)
  Buyer App (BAP)->>Seller App (BPP): /issue (close)
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
  Buyer App (BAP)->>Seller App (BPP): /status
  Seller App (BPP)-->>Buyer App (BAP): /on_status (active bus pass)
  Seller App (BPP)-->>Buyer App (BAP): /on_status (unsolicited): trip status update
  Buyer App (BAP)->>Seller App (BPP): /issue (open complaint)
  Seller App (BPP)-->>Buyer App (BAP): /on_issue (processing)
  Seller App (BPP)-->>Buyer App (BAP): /on_issue (unsolicited): resolution
  Buyer App (BAP)->>Seller App (BPP): /issue (reject resolution)
  Seller App (BPP)-->>Buyer App (BAP): /on_issue (processing)
  Seller App (BPP)-->>Buyer App (BAP): /on_issue (unsolicited): revised resolution
  Buyer App (BAP)->>Seller App (BPP): /issue (escalate)
  Seller App (BPP)-->>Buyer App (BAP): /on_issue (processing escalation)
  Seller App (BPP)-->>Buyer App (BAP): /on_issue (unsolicited): grievance resolution
  Buyer App (BAP)->>Seller App (BPP): /issue (accept resolution)
  Seller App (BPP)-->>Buyer App (BAP): /on_issue (resolved)
  Buyer App (BAP)->>Seller App (BPP): /issue (close)
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
  Buyer App (BAP)->>Seller App (BPP): /status
  Seller App (BPP)-->>Buyer App (BAP): /on_status (active bus pass)
  Seller App (BPP)-->>Buyer App (BAP): /on_status (unsolicited): trip status update
  Buyer App (BAP)->>Seller App (BPP): /issue (open complaint)
  Seller App (BPP)-->>Buyer App (BAP): /on_issue (processing)
  Seller App (BPP)-->>Buyer App (BAP): /on_issue (unsolicited): resolution
  Buyer App (BAP)->>Seller App (BPP): /issue (reject resolution)
  Seller App (BPP)-->>Buyer App (BAP): /on_issue (processing)
  Seller App (BPP)-->>Buyer App (BAP): /on_issue (unsolicited): revised resolution
  Buyer App (BAP)->>Seller App (BPP): /issue (escalate)
  Seller App (BPP)-->>Buyer App (BAP): /on_issue (processing escalation)
  Seller App (BPP)-->>Buyer App (BAP): /on_issue (unsolicited): grievance resolution
  Buyer App (BAP)->>Seller App (BPP): /issue (accept resolution)
  Seller App (BPP)-->>Buyer App (BAP): /on_issue (resolved)
  Buyer App (BAP)->>Seller App (BPP): /issue (close)
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
  Buyer App (BAP)->>Seller App (BPP): /status
  Seller App (BPP)-->>Buyer App (BAP): /on_status (active bus pass)
  Seller App (BPP)-->>Buyer App (BAP): /on_status (unsolicited): trip status update
  Buyer App (BAP)->>Seller App (BPP): /issue (open complaint)
  Seller App (BPP)-->>Buyer App (BAP): /on_issue (processing)
  Seller App (BPP)-->>Buyer App (BAP): /on_issue (unsolicited): resolution
  Buyer App (BAP)->>Seller App (BPP): /issue (reject resolution)
  Seller App (BPP)-->>Buyer App (BAP): /on_issue (processing)
  Seller App (BPP)-->>Buyer App (BAP): /on_issue (unsolicited): revised resolution
  Buyer App (BAP)->>Seller App (BPP): /issue (escalate)
  Seller App (BPP)-->>Buyer App (BAP): /on_issue (processing escalation)
  Seller App (BPP)-->>Buyer App (BAP): /on_issue (unsolicited): grievance resolution
  Buyer App (BAP)->>Seller App (BPP): /issue (accept resolution)
  Seller App (BPP)-->>Buyer App (BAP): /on_issue (resolved)
  Buyer App (BAP)->>Seller App (BPP): /issue (close)
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
  Buyer App (BAP)->>Seller App (BPP): /status
  Seller App (BPP)-->>Buyer App (BAP): /on_status (active bus pass)
  Seller App (BPP)-->>Buyer App (BAP): /on_status (unsolicited): trip status update
  Buyer App (BAP)->>Seller App (BPP): /issue (open complaint)
  Seller App (BPP)-->>Buyer App (BAP): /on_issue (processing)
  Seller App (BPP)-->>Buyer App (BAP): /on_issue (unsolicited): resolution
  Buyer App (BAP)->>Seller App (BPP): /issue (reject resolution)
  Seller App (BPP)-->>Buyer App (BAP): /on_issue (processing)
  Seller App (BPP)-->>Buyer App (BAP): /on_issue (unsolicited): revised resolution
  Buyer App (BAP)->>Seller App (BPP): /issue (escalate)
  Seller App (BPP)-->>Buyer App (BAP): /on_issue (processing escalation)
  Seller App (BPP)-->>Buyer App (BAP): /on_issue (unsolicited): grievance resolution
  Buyer App (BAP)->>Seller App (BPP): /issue (accept resolution)
  Seller App (BPP)-->>Buyer App (BAP): /on_issue (resolved)
  Buyer App (BAP)->>Seller App (BPP): /issue (close)
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
  Buyer App (BAP)->>Seller App (BPP): /status
  Seller App (BPP)-->>Buyer App (BAP): /on_status (active bus pass)
  Seller App (BPP)-->>Buyer App (BAP): /on_status (unsolicited): trip status update
  Buyer App (BAP)->>Seller App (BPP): /issue (open complaint)
  Seller App (BPP)-->>Buyer App (BAP): /on_issue (processing)
  Seller App (BPP)-->>Buyer App (BAP): /on_issue (unsolicited): resolution
  Buyer App (BAP)->>Seller App (BPP): /issue (reject resolution)
  Seller App (BPP)-->>Buyer App (BAP): /on_issue (processing)
  Seller App (BPP)-->>Buyer App (BAP): /on_issue (unsolicited): revised resolution
  Buyer App (BAP)->>Seller App (BPP): /issue (escalate)
  Seller App (BPP)-->>Buyer App (BAP): /on_issue (processing escalation)
  Seller App (BPP)-->>Buyer App (BAP): /on_issue (unsolicited): grievance resolution
  Buyer App (BAP)->>Seller App (BPP): /issue (accept resolution)
  Seller App (BPP)-->>Buyer App (BAP): /on_issue (resolved)
  Buyer App (BAP)->>Seller App (BPP): /issue (close)
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
  Buyer App (BAP)->>Seller App (BPP): /status
  Seller App (BPP)-->>Buyer App (BAP): /on_status (active bus pass)
  Seller App (BPP)-->>Buyer App (BAP): /on_status (unsolicited): trip status update
  Buyer App (BAP)->>Seller App (BPP): /issue (open complaint)
  Seller App (BPP)-->>Buyer App (BAP): /on_issue (processing)
  Seller App (BPP)-->>Buyer App (BAP): /on_issue (unsolicited): resolution
  Buyer App (BAP)->>Seller App (BPP): /issue (reject resolution)
  Seller App (BPP)-->>Buyer App (BAP): /on_issue (processing)
  Seller App (BPP)-->>Buyer App (BAP): /on_issue (unsolicited): revised resolution
  Buyer App (BAP)->>Seller App (BPP): /issue (escalate)
  Seller App (BPP)-->>Buyer App (BAP): /on_issue (processing escalation)
  Seller App (BPP)-->>Buyer App (BAP): /on_issue (unsolicited): grievance resolution
  Buyer App (BAP)->>Seller App (BPP): /issue (accept resolution)
  Seller App (BPP)-->>Buyer App (BAP): /on_issue (resolved)
  Buyer App (BAP)->>Seller App (BPP): /issue (close)
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
  Buyer App (BAP)->>Seller App (BPP): /status
  Seller App (BPP)-->>Buyer App (BAP): /on_status (active bus pass)
  Seller App (BPP)-->>Buyer App (BAP): /on_status (unsolicited): trip status update
  Buyer App (BAP)->>Seller App (BPP): /issue (open complaint)
  Seller App (BPP)-->>Buyer App (BAP): /on_issue (processing)
  Seller App (BPP)-->>Buyer App (BAP): /on_issue (unsolicited): resolution
  Buyer App (BAP)->>Seller App (BPP): /issue (reject resolution)
  Seller App (BPP)-->>Buyer App (BAP): /on_issue (processing)
  Seller App (BPP)-->>Buyer App (BAP): /on_issue (unsolicited): revised resolution
  Buyer App (BAP)->>Seller App (BPP): /issue (escalate)
  Seller App (BPP)-->>Buyer App (BAP): /on_issue (processing escalation)
  Seller App (BPP)-->>Buyer App (BAP): /on_issue (unsolicited): grievance resolution
  Buyer App (BAP)->>Seller App (BPP): /issue (accept resolution)
  Seller App (BPP)-->>Buyer App (BAP): /on_issue (resolved)
  Buyer App (BAP)->>Seller App (BPP): /issue (close)
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
  Buyer App (BAP)->>Seller App (BPP): /status
  Seller App (BPP)-->>Buyer App (BAP): /on_status (active bus pass)
  Seller App (BPP)-->>Buyer App (BAP): /on_status (unsolicited): trip status update
  Buyer App (BAP)->>Seller App (BPP): /issue (open complaint)
  Seller App (BPP)-->>Buyer App (BAP): /on_issue (processing)
  Seller App (BPP)-->>Buyer App (BAP): /on_issue (unsolicited): resolution
  Buyer App (BAP)->>Seller App (BPP): /issue (reject resolution)
  Seller App (BPP)-->>Buyer App (BAP): /on_issue (processing)
  Seller App (BPP)-->>Buyer App (BAP): /on_issue (unsolicited): revised resolution
  Buyer App (BAP)->>Seller App (BPP): /issue (escalate)
  Seller App (BPP)-->>Buyer App (BAP): /on_issue (processing escalation)
  Seller App (BPP)-->>Buyer App (BAP): /on_issue (unsolicited): grievance resolution
  Buyer App (BAP)->>Seller App (BPP): /issue (accept resolution)
  Seller App (BPP)-->>Buyer App (BAP): /on_issue (resolved)
  Buyer App (BAP)->>Seller App (BPP): /issue (close)
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
  Buyer App (BAP)->>Seller App (BPP): /status
  Seller App (BPP)-->>Buyer App (BAP): /on_status (active bus pass)
  Seller App (BPP)-->>Buyer App (BAP): /on_status (unsolicited): trip status update
  Buyer App (BAP)->>Seller App (BPP): /issue (open complaint)
  Seller App (BPP)-->>Buyer App (BAP): /on_issue (processing)
  Seller App (BPP)-->>Buyer App (BAP): /on_issue (unsolicited): resolution
  Buyer App (BAP)->>Seller App (BPP): /issue (reject resolution)
  Seller App (BPP)-->>Buyer App (BAP): /on_issue (processing)
  Seller App (BPP)-->>Buyer App (BAP): /on_issue (unsolicited): revised resolution
  Buyer App (BAP)->>Seller App (BPP): /issue (escalate)
  Seller App (BPP)-->>Buyer App (BAP): /on_issue (processing escalation)
  Seller App (BPP)-->>Buyer App (BAP): /on_issue (unsolicited): grievance resolution
  Buyer App (BAP)->>Seller App (BPP): /issue (accept resolution)
  Seller App (BPP)-->>Buyer App (BAP): /on_issue (resolved)
  Buyer App (BAP)->>Seller App (BPP): /issue (close)
```

## status_BUS_201

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
  Buyer App (BAP)->>Seller App (BPP): /status
  end
  Seller App (BPP)-->>Buyer App (BAP): /on_status (active bus pass)
  Seller App (BPP)-->>Buyer App (BAP): /on_status (unsolicited): trip status update
  Buyer App (BAP)->>Seller App (BPP): /issue (open complaint)
  Seller App (BPP)-->>Buyer App (BAP): /on_issue (processing)
  Seller App (BPP)-->>Buyer App (BAP): /on_issue (unsolicited): resolution
  Buyer App (BAP)->>Seller App (BPP): /issue (reject resolution)
  Seller App (BPP)-->>Buyer App (BAP): /on_issue (processing)
  Seller App (BPP)-->>Buyer App (BAP): /on_issue (unsolicited): revised resolution
  Buyer App (BAP)->>Seller App (BPP): /issue (escalate)
  Seller App (BPP)-->>Buyer App (BAP): /on_issue (processing escalation)
  Seller App (BPP)-->>Buyer App (BAP): /on_issue (unsolicited): grievance resolution
  Buyer App (BAP)->>Seller App (BPP): /issue (accept resolution)
  Seller App (BPP)-->>Buyer App (BAP): /on_issue (resolved)
  Buyer App (BAP)->>Seller App (BPP): /issue (close)
```

## on_status_BUS_201

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
  Buyer App (BAP)->>Seller App (BPP): /status
  rect rgb(191, 223, 255)
  Seller App (BPP)-->>Buyer App (BAP): /on_status (active bus pass)
  end
  Seller App (BPP)-->>Buyer App (BAP): /on_status (unsolicited): trip status update
  Buyer App (BAP)->>Seller App (BPP): /issue (open complaint)
  Seller App (BPP)-->>Buyer App (BAP): /on_issue (processing)
  Seller App (BPP)-->>Buyer App (BAP): /on_issue (unsolicited): resolution
  Buyer App (BAP)->>Seller App (BPP): /issue (reject resolution)
  Seller App (BPP)-->>Buyer App (BAP): /on_issue (processing)
  Seller App (BPP)-->>Buyer App (BAP): /on_issue (unsolicited): revised resolution
  Buyer App (BAP)->>Seller App (BPP): /issue (escalate)
  Seller App (BPP)-->>Buyer App (BAP): /on_issue (processing escalation)
  Seller App (BPP)-->>Buyer App (BAP): /on_issue (unsolicited): grievance resolution
  Buyer App (BAP)->>Seller App (BPP): /issue (accept resolution)
  Seller App (BPP)-->>Buyer App (BAP): /on_issue (resolved)
  Buyer App (BAP)->>Seller App (BPP): /issue (close)
```

## on_status_unsolicited_201

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
  Buyer App (BAP)->>Seller App (BPP): /status
  Seller App (BPP)-->>Buyer App (BAP): /on_status (active bus pass)
  rect rgb(191, 223, 255)
  Seller App (BPP)-->>Buyer App (BAP): /on_status (unsolicited): trip status update
  end
  Buyer App (BAP)->>Seller App (BPP): /issue (open complaint)
  Seller App (BPP)-->>Buyer App (BAP): /on_issue (processing)
  Seller App (BPP)-->>Buyer App (BAP): /on_issue (unsolicited): resolution
  Buyer App (BAP)->>Seller App (BPP): /issue (reject resolution)
  Seller App (BPP)-->>Buyer App (BAP): /on_issue (processing)
  Seller App (BPP)-->>Buyer App (BAP): /on_issue (unsolicited): revised resolution
  Buyer App (BAP)->>Seller App (BPP): /issue (escalate)
  Seller App (BPP)-->>Buyer App (BAP): /on_issue (processing escalation)
  Seller App (BPP)-->>Buyer App (BAP): /on_issue (unsolicited): grievance resolution
  Buyer App (BAP)->>Seller App (BPP): /issue (accept resolution)
  Seller App (BPP)-->>Buyer App (BAP): /on_issue (resolved)
  Buyer App (BAP)->>Seller App (BPP): /issue (close)
```

## issue_open

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
  Buyer App (BAP)->>Seller App (BPP): /status
  Seller App (BPP)-->>Buyer App (BAP): /on_status (active bus pass)
  Seller App (BPP)-->>Buyer App (BAP): /on_status (unsolicited): trip status update
  rect rgb(191, 223, 255)
  Buyer App (BAP)->>Seller App (BPP): /issue (open complaint)
  end
  Seller App (BPP)-->>Buyer App (BAP): /on_issue (processing)
  Seller App (BPP)-->>Buyer App (BAP): /on_issue (unsolicited): resolution
  Buyer App (BAP)->>Seller App (BPP): /issue (reject resolution)
  Seller App (BPP)-->>Buyer App (BAP): /on_issue (processing)
  Seller App (BPP)-->>Buyer App (BAP): /on_issue (unsolicited): revised resolution
  Buyer App (BAP)->>Seller App (BPP): /issue (escalate)
  Seller App (BPP)-->>Buyer App (BAP): /on_issue (processing escalation)
  Seller App (BPP)-->>Buyer App (BAP): /on_issue (unsolicited): grievance resolution
  Buyer App (BAP)->>Seller App (BPP): /issue (accept resolution)
  Seller App (BPP)-->>Buyer App (BAP): /on_issue (resolved)
  Buyer App (BAP)->>Seller App (BPP): /issue (close)
```

## on_issue_processing

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
  Buyer App (BAP)->>Seller App (BPP): /status
  Seller App (BPP)-->>Buyer App (BAP): /on_status (active bus pass)
  Seller App (BPP)-->>Buyer App (BAP): /on_status (unsolicited): trip status update
  Buyer App (BAP)->>Seller App (BPP): /issue (open complaint)
  rect rgb(191, 223, 255)
  Seller App (BPP)-->>Buyer App (BAP): /on_issue (processing)
  end
  Seller App (BPP)-->>Buyer App (BAP): /on_issue (unsolicited): resolution
  Buyer App (BAP)->>Seller App (BPP): /issue (reject resolution)
  Seller App (BPP)-->>Buyer App (BAP): /on_issue (processing)
  Seller App (BPP)-->>Buyer App (BAP): /on_issue (unsolicited): revised resolution
  Buyer App (BAP)->>Seller App (BPP): /issue (escalate)
  Seller App (BPP)-->>Buyer App (BAP): /on_issue (processing escalation)
  Seller App (BPP)-->>Buyer App (BAP): /on_issue (unsolicited): grievance resolution
  Buyer App (BAP)->>Seller App (BPP): /issue (accept resolution)
  Seller App (BPP)-->>Buyer App (BAP): /on_issue (resolved)
  Buyer App (BAP)->>Seller App (BPP): /issue (close)
```

## on_issue_resolution

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
  Buyer App (BAP)->>Seller App (BPP): /status
  Seller App (BPP)-->>Buyer App (BAP): /on_status (active bus pass)
  Seller App (BPP)-->>Buyer App (BAP): /on_status (unsolicited): trip status update
  Buyer App (BAP)->>Seller App (BPP): /issue (open complaint)
  Seller App (BPP)-->>Buyer App (BAP): /on_issue (processing)
  rect rgb(191, 223, 255)
  Seller App (BPP)-->>Buyer App (BAP): /on_issue (unsolicited): resolution
  end
  Buyer App (BAP)->>Seller App (BPP): /issue (reject resolution)
  Seller App (BPP)-->>Buyer App (BAP): /on_issue (processing)
  Seller App (BPP)-->>Buyer App (BAP): /on_issue (unsolicited): revised resolution
  Buyer App (BAP)->>Seller App (BPP): /issue (escalate)
  Seller App (BPP)-->>Buyer App (BAP): /on_issue (processing escalation)
  Seller App (BPP)-->>Buyer App (BAP): /on_issue (unsolicited): grievance resolution
  Buyer App (BAP)->>Seller App (BPP): /issue (accept resolution)
  Seller App (BPP)-->>Buyer App (BAP): /on_issue (resolved)
  Buyer App (BAP)->>Seller App (BPP): /issue (close)
```

## issue_resolution_reject

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
  Buyer App (BAP)->>Seller App (BPP): /status
  Seller App (BPP)-->>Buyer App (BAP): /on_status (active bus pass)
  Seller App (BPP)-->>Buyer App (BAP): /on_status (unsolicited): trip status update
  Buyer App (BAP)->>Seller App (BPP): /issue (open complaint)
  Seller App (BPP)-->>Buyer App (BAP): /on_issue (processing)
  Seller App (BPP)-->>Buyer App (BAP): /on_issue (unsolicited): resolution
  rect rgb(191, 223, 255)
  Buyer App (BAP)->>Seller App (BPP): /issue (reject resolution)
  end
  Seller App (BPP)-->>Buyer App (BAP): /on_issue (processing)
  Seller App (BPP)-->>Buyer App (BAP): /on_issue (unsolicited): revised resolution
  Buyer App (BAP)->>Seller App (BPP): /issue (escalate)
  Seller App (BPP)-->>Buyer App (BAP): /on_issue (processing escalation)
  Seller App (BPP)-->>Buyer App (BAP): /on_issue (unsolicited): grievance resolution
  Buyer App (BAP)->>Seller App (BPP): /issue (accept resolution)
  Seller App (BPP)-->>Buyer App (BAP): /on_issue (resolved)
  Buyer App (BAP)->>Seller App (BPP): /issue (close)
```

## on_issue_processing_1

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
  Buyer App (BAP)->>Seller App (BPP): /status
  Seller App (BPP)-->>Buyer App (BAP): /on_status (active bus pass)
  Seller App (BPP)-->>Buyer App (BAP): /on_status (unsolicited): trip status update
  Buyer App (BAP)->>Seller App (BPP): /issue (open complaint)
  Seller App (BPP)-->>Buyer App (BAP): /on_issue (processing)
  Seller App (BPP)-->>Buyer App (BAP): /on_issue (unsolicited): resolution
  Buyer App (BAP)->>Seller App (BPP): /issue (reject resolution)
  rect rgb(191, 223, 255)
  Seller App (BPP)-->>Buyer App (BAP): /on_issue (processing)
  end
  Seller App (BPP)-->>Buyer App (BAP): /on_issue (unsolicited): revised resolution
  Buyer App (BAP)->>Seller App (BPP): /issue (escalate)
  Seller App (BPP)-->>Buyer App (BAP): /on_issue (processing escalation)
  Seller App (BPP)-->>Buyer App (BAP): /on_issue (unsolicited): grievance resolution
  Buyer App (BAP)->>Seller App (BPP): /issue (accept resolution)
  Seller App (BPP)-->>Buyer App (BAP): /on_issue (resolved)
  Buyer App (BAP)->>Seller App (BPP): /issue (close)
```

## on_issue_resolution_1

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
  Buyer App (BAP)->>Seller App (BPP): /status
  Seller App (BPP)-->>Buyer App (BAP): /on_status (active bus pass)
  Seller App (BPP)-->>Buyer App (BAP): /on_status (unsolicited): trip status update
  Buyer App (BAP)->>Seller App (BPP): /issue (open complaint)
  Seller App (BPP)-->>Buyer App (BAP): /on_issue (processing)
  Seller App (BPP)-->>Buyer App (BAP): /on_issue (unsolicited): resolution
  Buyer App (BAP)->>Seller App (BPP): /issue (reject resolution)
  Seller App (BPP)-->>Buyer App (BAP): /on_issue (processing)
  rect rgb(191, 223, 255)
  Seller App (BPP)-->>Buyer App (BAP): /on_issue (unsolicited): revised resolution
  end
  Buyer App (BAP)->>Seller App (BPP): /issue (escalate)
  Seller App (BPP)-->>Buyer App (BAP): /on_issue (processing escalation)
  Seller App (BPP)-->>Buyer App (BAP): /on_issue (unsolicited): grievance resolution
  Buyer App (BAP)->>Seller App (BPP): /issue (accept resolution)
  Seller App (BPP)-->>Buyer App (BAP): /on_issue (resolved)
  Buyer App (BAP)->>Seller App (BPP): /issue (close)
```

## issue_escalate

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
  Buyer App (BAP)->>Seller App (BPP): /status
  Seller App (BPP)-->>Buyer App (BAP): /on_status (active bus pass)
  Seller App (BPP)-->>Buyer App (BAP): /on_status (unsolicited): trip status update
  Buyer App (BAP)->>Seller App (BPP): /issue (open complaint)
  Seller App (BPP)-->>Buyer App (BAP): /on_issue (processing)
  Seller App (BPP)-->>Buyer App (BAP): /on_issue (unsolicited): resolution
  Buyer App (BAP)->>Seller App (BPP): /issue (reject resolution)
  Seller App (BPP)-->>Buyer App (BAP): /on_issue (processing)
  Seller App (BPP)-->>Buyer App (BAP): /on_issue (unsolicited): revised resolution
  rect rgb(191, 223, 255)
  Buyer App (BAP)->>Seller App (BPP): /issue (escalate)
  end
  Seller App (BPP)-->>Buyer App (BAP): /on_issue (processing escalation)
  Seller App (BPP)-->>Buyer App (BAP): /on_issue (unsolicited): grievance resolution
  Buyer App (BAP)->>Seller App (BPP): /issue (accept resolution)
  Seller App (BPP)-->>Buyer App (BAP): /on_issue (resolved)
  Buyer App (BAP)->>Seller App (BPP): /issue (close)
```

## on_issue_processing_2

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
  Buyer App (BAP)->>Seller App (BPP): /status
  Seller App (BPP)-->>Buyer App (BAP): /on_status (active bus pass)
  Seller App (BPP)-->>Buyer App (BAP): /on_status (unsolicited): trip status update
  Buyer App (BAP)->>Seller App (BPP): /issue (open complaint)
  Seller App (BPP)-->>Buyer App (BAP): /on_issue (processing)
  Seller App (BPP)-->>Buyer App (BAP): /on_issue (unsolicited): resolution
  Buyer App (BAP)->>Seller App (BPP): /issue (reject resolution)
  Seller App (BPP)-->>Buyer App (BAP): /on_issue (processing)
  Seller App (BPP)-->>Buyer App (BAP): /on_issue (unsolicited): revised resolution
  Buyer App (BAP)->>Seller App (BPP): /issue (escalate)
  rect rgb(191, 223, 255)
  Seller App (BPP)-->>Buyer App (BAP): /on_issue (processing escalation)
  end
  Seller App (BPP)-->>Buyer App (BAP): /on_issue (unsolicited): grievance resolution
  Buyer App (BAP)->>Seller App (BPP): /issue (accept resolution)
  Seller App (BPP)-->>Buyer App (BAP): /on_issue (resolved)
  Buyer App (BAP)->>Seller App (BPP): /issue (close)
```

## on_issue_resolution_2

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
  Buyer App (BAP)->>Seller App (BPP): /status
  Seller App (BPP)-->>Buyer App (BAP): /on_status (active bus pass)
  Seller App (BPP)-->>Buyer App (BAP): /on_status (unsolicited): trip status update
  Buyer App (BAP)->>Seller App (BPP): /issue (open complaint)
  Seller App (BPP)-->>Buyer App (BAP): /on_issue (processing)
  Seller App (BPP)-->>Buyer App (BAP): /on_issue (unsolicited): resolution
  Buyer App (BAP)->>Seller App (BPP): /issue (reject resolution)
  Seller App (BPP)-->>Buyer App (BAP): /on_issue (processing)
  Seller App (BPP)-->>Buyer App (BAP): /on_issue (unsolicited): revised resolution
  Buyer App (BAP)->>Seller App (BPP): /issue (escalate)
  Seller App (BPP)-->>Buyer App (BAP): /on_issue (processing escalation)
  rect rgb(191, 223, 255)
  Seller App (BPP)-->>Buyer App (BAP): /on_issue (unsolicited): grievance resolution
  end
  Buyer App (BAP)->>Seller App (BPP): /issue (accept resolution)
  Seller App (BPP)-->>Buyer App (BAP): /on_issue (resolved)
  Buyer App (BAP)->>Seller App (BPP): /issue (close)
```

## issue_resolution_accept

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
  Buyer App (BAP)->>Seller App (BPP): /status
  Seller App (BPP)-->>Buyer App (BAP): /on_status (active bus pass)
  Seller App (BPP)-->>Buyer App (BAP): /on_status (unsolicited): trip status update
  Buyer App (BAP)->>Seller App (BPP): /issue (open complaint)
  Seller App (BPP)-->>Buyer App (BAP): /on_issue (processing)
  Seller App (BPP)-->>Buyer App (BAP): /on_issue (unsolicited): resolution
  Buyer App (BAP)->>Seller App (BPP): /issue (reject resolution)
  Seller App (BPP)-->>Buyer App (BAP): /on_issue (processing)
  Seller App (BPP)-->>Buyer App (BAP): /on_issue (unsolicited): revised resolution
  Buyer App (BAP)->>Seller App (BPP): /issue (escalate)
  Seller App (BPP)-->>Buyer App (BAP): /on_issue (processing escalation)
  Seller App (BPP)-->>Buyer App (BAP): /on_issue (unsolicited): grievance resolution
  rect rgb(191, 223, 255)
  Buyer App (BAP)->>Seller App (BPP): /issue (accept resolution)
  end
  Seller App (BPP)-->>Buyer App (BAP): /on_issue (resolved)
  Buyer App (BAP)->>Seller App (BPP): /issue (close)
```

## on_issue_resolved

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
  Buyer App (BAP)->>Seller App (BPP): /status
  Seller App (BPP)-->>Buyer App (BAP): /on_status (active bus pass)
  Seller App (BPP)-->>Buyer App (BAP): /on_status (unsolicited): trip status update
  Buyer App (BAP)->>Seller App (BPP): /issue (open complaint)
  Seller App (BPP)-->>Buyer App (BAP): /on_issue (processing)
  Seller App (BPP)-->>Buyer App (BAP): /on_issue (unsolicited): resolution
  Buyer App (BAP)->>Seller App (BPP): /issue (reject resolution)
  Seller App (BPP)-->>Buyer App (BAP): /on_issue (processing)
  Seller App (BPP)-->>Buyer App (BAP): /on_issue (unsolicited): revised resolution
  Buyer App (BAP)->>Seller App (BPP): /issue (escalate)
  Seller App (BPP)-->>Buyer App (BAP): /on_issue (processing escalation)
  Seller App (BPP)-->>Buyer App (BAP): /on_issue (unsolicited): grievance resolution
  Buyer App (BAP)->>Seller App (BPP): /issue (accept resolution)
  rect rgb(191, 223, 255)
  Seller App (BPP)-->>Buyer App (BAP): /on_issue (resolved)
  end
  Buyer App (BAP)->>Seller App (BPP): /issue (close)
```

## issue_close

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
  Buyer App (BAP)->>Seller App (BPP): /status
  Seller App (BPP)-->>Buyer App (BAP): /on_status (active bus pass)
  Seller App (BPP)-->>Buyer App (BAP): /on_status (unsolicited): trip status update
  Buyer App (BAP)->>Seller App (BPP): /issue (open complaint)
  Seller App (BPP)-->>Buyer App (BAP): /on_issue (processing)
  Seller App (BPP)-->>Buyer App (BAP): /on_issue (unsolicited): resolution
  Buyer App (BAP)->>Seller App (BPP): /issue (reject resolution)
  Seller App (BPP)-->>Buyer App (BAP): /on_issue (processing)
  Seller App (BPP)-->>Buyer App (BAP): /on_issue (unsolicited): revised resolution
  Buyer App (BAP)->>Seller App (BPP): /issue (escalate)
  Seller App (BPP)-->>Buyer App (BAP): /on_issue (processing escalation)
  Seller App (BPP)-->>Buyer App (BAP): /on_issue (unsolicited): grievance resolution
  Buyer App (BAP)->>Seller App (BPP): /issue (accept resolution)
  Seller App (BPP)-->>Buyer App (BAP): /on_issue (resolved)
  rect rgb(191, 223, 255)
  Buyer App (BAP)->>Seller App (BPP): /issue (close)
  end
```

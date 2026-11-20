# Cancellation by Buyer — Sequence Diagrams

Internal data file consumed by the Developer Guide's "Sequence Diagram" tab (API Walkthrough).
Not meant to be shown as its own docs page — the frontend filters this slug out of the Use Case
Brief / Additional Resources / Changelog tab lists and instead looks up the section matching the
selected API call's `action_id` (the `##` heading below) to render that step's diagram.

One `## <action_id>` heading per step of `Cancellation_by_Buyer.yaml`, in that flow's own step order, each followed by its Mermaid `sequenceDiagram`: the whole flow, with that call's own message(s) highlighted — same convention as the other domains' per-step sequence-diagram docs.

## search_1_Airline_200

```mermaid
sequenceDiagram
  participant Buyer App (BAP)
  participant Gateway
  participant Seller App (BPP)
  rect rgb(191, 223, 255)
  Buyer App (BAP)->>Gateway: /search (flight search)
  Gateway->>Seller App (BPP): /search (forwarded)
  end
  Seller App (BPP)-->>Buyer App (BAP): /on_search (batch 1: flight catalog)
  Seller App (BPP)-->>Buyer App (BAP): /on_search (unsolicited): batch 2 (flight catalog)
  Seller App (BPP)-->>Buyer App (BAP): /on_search (unsolicited): batch 3 (flight catalog)
  Seller App (BPP)-->>Buyer App (BAP): /on_search (unsolicited): batch 4 (final flight catalog)
  Buyer App (BAP)->>Seller App (BPP): /select (select flight)
  Seller App (BPP)-->>Buyer App (BAP): /on_select (quote, seat availability)
  Buyer App (BAP)->>Seller App (BPP): /select (add-on services, meals/baggage)
  Seller App (BPP)-->>Buyer App (BAP): /on_select (updated quote with add-ons)
  Buyer App (BAP)->>Seller App (BPP): /init (passenger details, billing)
  Seller App (BPP)-->>Buyer App (BAP): /on_init (final quote, payment terms)
  Buyer App (BAP)->>Seller App (BPP): /confirm (place flight booking)
  Seller App (BPP)-->>Buyer App (BAP): /on_confirm (booking confirmed, ticket issued)
  Buyer App (BAP)->>Seller App (BPP): /cancel (soft cancel request)
  Seller App (BPP)-->>Buyer App (BAP): /on_cancel (cancellation quote & terms)
  Buyer App (BAP)->>Seller App (BPP): /cancel (confirm cancellation)
  Seller App (BPP)-->>Buyer App (BAP): /on_cancel (flight booking cancelled)
```

## on_search_1_Airline_200

```mermaid
sequenceDiagram
  participant Buyer App (BAP)
  participant Gateway
  participant Seller App (BPP)
  Buyer App (BAP)->>Gateway: /search (flight search)
  Gateway->>Seller App (BPP): /search (forwarded)
  rect rgb(191, 223, 255)
  Seller App (BPP)-->>Buyer App (BAP): /on_search (batch 1: flight catalog)
  end
  Seller App (BPP)-->>Buyer App (BAP): /on_search (unsolicited): batch 2 (flight catalog)
  Seller App (BPP)-->>Buyer App (BAP): /on_search (unsolicited): batch 3 (flight catalog)
  Seller App (BPP)-->>Buyer App (BAP): /on_search (unsolicited): batch 4 (final flight catalog)
  Buyer App (BAP)->>Seller App (BPP): /select (select flight)
  Seller App (BPP)-->>Buyer App (BAP): /on_select (quote, seat availability)
  Buyer App (BAP)->>Seller App (BPP): /select (add-on services, meals/baggage)
  Seller App (BPP)-->>Buyer App (BAP): /on_select (updated quote with add-ons)
  Buyer App (BAP)->>Seller App (BPP): /init (passenger details, billing)
  Seller App (BPP)-->>Buyer App (BAP): /on_init (final quote, payment terms)
  Buyer App (BAP)->>Seller App (BPP): /confirm (place flight booking)
  Seller App (BPP)-->>Buyer App (BAP): /on_confirm (booking confirmed, ticket issued)
  Buyer App (BAP)->>Seller App (BPP): /cancel (soft cancel request)
  Seller App (BPP)-->>Buyer App (BAP): /on_cancel (cancellation quote & terms)
  Buyer App (BAP)->>Seller App (BPP): /cancel (confirm cancellation)
  Seller App (BPP)-->>Buyer App (BAP): /on_cancel (flight booking cancelled)
```

## on_search_2_Airline_200

```mermaid
sequenceDiagram
  participant Buyer App (BAP)
  participant Gateway
  participant Seller App (BPP)
  Buyer App (BAP)->>Gateway: /search (flight search)
  Gateway->>Seller App (BPP): /search (forwarded)
  Seller App (BPP)-->>Buyer App (BAP): /on_search (batch 1: flight catalog)
  rect rgb(191, 223, 255)
  Seller App (BPP)-->>Buyer App (BAP): /on_search (unsolicited): batch 2 (flight catalog)
  end
  Seller App (BPP)-->>Buyer App (BAP): /on_search (unsolicited): batch 3 (flight catalog)
  Seller App (BPP)-->>Buyer App (BAP): /on_search (unsolicited): batch 4 (final flight catalog)
  Buyer App (BAP)->>Seller App (BPP): /select (select flight)
  Seller App (BPP)-->>Buyer App (BAP): /on_select (quote, seat availability)
  Buyer App (BAP)->>Seller App (BPP): /select (add-on services, meals/baggage)
  Seller App (BPP)-->>Buyer App (BAP): /on_select (updated quote with add-ons)
  Buyer App (BAP)->>Seller App (BPP): /init (passenger details, billing)
  Seller App (BPP)-->>Buyer App (BAP): /on_init (final quote, payment terms)
  Buyer App (BAP)->>Seller App (BPP): /confirm (place flight booking)
  Seller App (BPP)-->>Buyer App (BAP): /on_confirm (booking confirmed, ticket issued)
  Buyer App (BAP)->>Seller App (BPP): /cancel (soft cancel request)
  Seller App (BPP)-->>Buyer App (BAP): /on_cancel (cancellation quote & terms)
  Buyer App (BAP)->>Seller App (BPP): /cancel (confirm cancellation)
  Seller App (BPP)-->>Buyer App (BAP): /on_cancel (flight booking cancelled)
```

## on_search_3_Airline_200

```mermaid
sequenceDiagram
  participant Buyer App (BAP)
  participant Gateway
  participant Seller App (BPP)
  Buyer App (BAP)->>Gateway: /search (flight search)
  Gateway->>Seller App (BPP): /search (forwarded)
  Seller App (BPP)-->>Buyer App (BAP): /on_search (batch 1: flight catalog)
  Seller App (BPP)-->>Buyer App (BAP): /on_search (unsolicited): batch 2 (flight catalog)
  rect rgb(191, 223, 255)
  Seller App (BPP)-->>Buyer App (BAP): /on_search (unsolicited): batch 3 (flight catalog)
  end
  Seller App (BPP)-->>Buyer App (BAP): /on_search (unsolicited): batch 4 (final flight catalog)
  Buyer App (BAP)->>Seller App (BPP): /select (select flight)
  Seller App (BPP)-->>Buyer App (BAP): /on_select (quote, seat availability)
  Buyer App (BAP)->>Seller App (BPP): /select (add-on services, meals/baggage)
  Seller App (BPP)-->>Buyer App (BAP): /on_select (updated quote with add-ons)
  Buyer App (BAP)->>Seller App (BPP): /init (passenger details, billing)
  Seller App (BPP)-->>Buyer App (BAP): /on_init (final quote, payment terms)
  Buyer App (BAP)->>Seller App (BPP): /confirm (place flight booking)
  Seller App (BPP)-->>Buyer App (BAP): /on_confirm (booking confirmed, ticket issued)
  Buyer App (BAP)->>Seller App (BPP): /cancel (soft cancel request)
  Seller App (BPP)-->>Buyer App (BAP): /on_cancel (cancellation quote & terms)
  Buyer App (BAP)->>Seller App (BPP): /cancel (confirm cancellation)
  Seller App (BPP)-->>Buyer App (BAP): /on_cancel (flight booking cancelled)
```

## on_search_4_Airline_200

```mermaid
sequenceDiagram
  participant Buyer App (BAP)
  participant Gateway
  participant Seller App (BPP)
  Buyer App (BAP)->>Gateway: /search (flight search)
  Gateway->>Seller App (BPP): /search (forwarded)
  Seller App (BPP)-->>Buyer App (BAP): /on_search (batch 1: flight catalog)
  Seller App (BPP)-->>Buyer App (BAP): /on_search (unsolicited): batch 2 (flight catalog)
  Seller App (BPP)-->>Buyer App (BAP): /on_search (unsolicited): batch 3 (flight catalog)
  rect rgb(191, 223, 255)
  Seller App (BPP)-->>Buyer App (BAP): /on_search (unsolicited): batch 4 (final flight catalog)
  end
  Buyer App (BAP)->>Seller App (BPP): /select (select flight)
  Seller App (BPP)-->>Buyer App (BAP): /on_select (quote, seat availability)
  Buyer App (BAP)->>Seller App (BPP): /select (add-on services, meals/baggage)
  Seller App (BPP)-->>Buyer App (BAP): /on_select (updated quote with add-ons)
  Buyer App (BAP)->>Seller App (BPP): /init (passenger details, billing)
  Seller App (BPP)-->>Buyer App (BAP): /on_init (final quote, payment terms)
  Buyer App (BAP)->>Seller App (BPP): /confirm (place flight booking)
  Seller App (BPP)-->>Buyer App (BAP): /on_confirm (booking confirmed, ticket issued)
  Buyer App (BAP)->>Seller App (BPP): /cancel (soft cancel request)
  Seller App (BPP)-->>Buyer App (BAP): /on_cancel (cancellation quote & terms)
  Buyer App (BAP)->>Seller App (BPP): /cancel (confirm cancellation)
  Seller App (BPP)-->>Buyer App (BAP): /on_cancel (flight booking cancelled)
```

## select_1_Airline_200

```mermaid
sequenceDiagram
  participant Buyer App (BAP)
  participant Gateway
  participant Seller App (BPP)
  Buyer App (BAP)->>Gateway: /search (flight search)
  Gateway->>Seller App (BPP): /search (forwarded)
  Seller App (BPP)-->>Buyer App (BAP): /on_search (batch 1: flight catalog)
  Seller App (BPP)-->>Buyer App (BAP): /on_search (unsolicited): batch 2 (flight catalog)
  Seller App (BPP)-->>Buyer App (BAP): /on_search (unsolicited): batch 3 (flight catalog)
  Seller App (BPP)-->>Buyer App (BAP): /on_search (unsolicited): batch 4 (final flight catalog)
  rect rgb(191, 223, 255)
  Buyer App (BAP)->>Seller App (BPP): /select (select flight)
  end
  Seller App (BPP)-->>Buyer App (BAP): /on_select (quote, seat availability)
  Buyer App (BAP)->>Seller App (BPP): /select (add-on services, meals/baggage)
  Seller App (BPP)-->>Buyer App (BAP): /on_select (updated quote with add-ons)
  Buyer App (BAP)->>Seller App (BPP): /init (passenger details, billing)
  Seller App (BPP)-->>Buyer App (BAP): /on_init (final quote, payment terms)
  Buyer App (BAP)->>Seller App (BPP): /confirm (place flight booking)
  Seller App (BPP)-->>Buyer App (BAP): /on_confirm (booking confirmed, ticket issued)
  Buyer App (BAP)->>Seller App (BPP): /cancel (soft cancel request)
  Seller App (BPP)-->>Buyer App (BAP): /on_cancel (cancellation quote & terms)
  Buyer App (BAP)->>Seller App (BPP): /cancel (confirm cancellation)
  Seller App (BPP)-->>Buyer App (BAP): /on_cancel (flight booking cancelled)
```

## on_select_1_Airline_200

```mermaid
sequenceDiagram
  participant Buyer App (BAP)
  participant Gateway
  participant Seller App (BPP)
  Buyer App (BAP)->>Gateway: /search (flight search)
  Gateway->>Seller App (BPP): /search (forwarded)
  Seller App (BPP)-->>Buyer App (BAP): /on_search (batch 1: flight catalog)
  Seller App (BPP)-->>Buyer App (BAP): /on_search (unsolicited): batch 2 (flight catalog)
  Seller App (BPP)-->>Buyer App (BAP): /on_search (unsolicited): batch 3 (flight catalog)
  Seller App (BPP)-->>Buyer App (BAP): /on_search (unsolicited): batch 4 (final flight catalog)
  Buyer App (BAP)->>Seller App (BPP): /select (select flight)
  rect rgb(191, 223, 255)
  Seller App (BPP)-->>Buyer App (BAP): /on_select (quote, seat availability)
  end
  Buyer App (BAP)->>Seller App (BPP): /select (add-on services, meals/baggage)
  Seller App (BPP)-->>Buyer App (BAP): /on_select (updated quote with add-ons)
  Buyer App (BAP)->>Seller App (BPP): /init (passenger details, billing)
  Seller App (BPP)-->>Buyer App (BAP): /on_init (final quote, payment terms)
  Buyer App (BAP)->>Seller App (BPP): /confirm (place flight booking)
  Seller App (BPP)-->>Buyer App (BAP): /on_confirm (booking confirmed, ticket issued)
  Buyer App (BAP)->>Seller App (BPP): /cancel (soft cancel request)
  Seller App (BPP)-->>Buyer App (BAP): /on_cancel (cancellation quote & terms)
  Buyer App (BAP)->>Seller App (BPP): /cancel (confirm cancellation)
  Seller App (BPP)-->>Buyer App (BAP): /on_cancel (flight booking cancelled)
```

## select_2_Airline_200

```mermaid
sequenceDiagram
  participant Buyer App (BAP)
  participant Gateway
  participant Seller App (BPP)
  Buyer App (BAP)->>Gateway: /search (flight search)
  Gateway->>Seller App (BPP): /search (forwarded)
  Seller App (BPP)-->>Buyer App (BAP): /on_search (batch 1: flight catalog)
  Seller App (BPP)-->>Buyer App (BAP): /on_search (unsolicited): batch 2 (flight catalog)
  Seller App (BPP)-->>Buyer App (BAP): /on_search (unsolicited): batch 3 (flight catalog)
  Seller App (BPP)-->>Buyer App (BAP): /on_search (unsolicited): batch 4 (final flight catalog)
  Buyer App (BAP)->>Seller App (BPP): /select (select flight)
  Seller App (BPP)-->>Buyer App (BAP): /on_select (quote, seat availability)
  rect rgb(191, 223, 255)
  Buyer App (BAP)->>Seller App (BPP): /select (add-on services, meals/baggage)
  end
  Seller App (BPP)-->>Buyer App (BAP): /on_select (updated quote with add-ons)
  Buyer App (BAP)->>Seller App (BPP): /init (passenger details, billing)
  Seller App (BPP)-->>Buyer App (BAP): /on_init (final quote, payment terms)
  Buyer App (BAP)->>Seller App (BPP): /confirm (place flight booking)
  Seller App (BPP)-->>Buyer App (BAP): /on_confirm (booking confirmed, ticket issued)
  Buyer App (BAP)->>Seller App (BPP): /cancel (soft cancel request)
  Seller App (BPP)-->>Buyer App (BAP): /on_cancel (cancellation quote & terms)
  Buyer App (BAP)->>Seller App (BPP): /cancel (confirm cancellation)
  Seller App (BPP)-->>Buyer App (BAP): /on_cancel (flight booking cancelled)
```

## on_select_2_Airline_200

```mermaid
sequenceDiagram
  participant Buyer App (BAP)
  participant Gateway
  participant Seller App (BPP)
  Buyer App (BAP)->>Gateway: /search (flight search)
  Gateway->>Seller App (BPP): /search (forwarded)
  Seller App (BPP)-->>Buyer App (BAP): /on_search (batch 1: flight catalog)
  Seller App (BPP)-->>Buyer App (BAP): /on_search (unsolicited): batch 2 (flight catalog)
  Seller App (BPP)-->>Buyer App (BAP): /on_search (unsolicited): batch 3 (flight catalog)
  Seller App (BPP)-->>Buyer App (BAP): /on_search (unsolicited): batch 4 (final flight catalog)
  Buyer App (BAP)->>Seller App (BPP): /select (select flight)
  Seller App (BPP)-->>Buyer App (BAP): /on_select (quote, seat availability)
  Buyer App (BAP)->>Seller App (BPP): /select (add-on services, meals/baggage)
  rect rgb(191, 223, 255)
  Seller App (BPP)-->>Buyer App (BAP): /on_select (updated quote with add-ons)
  end
  Buyer App (BAP)->>Seller App (BPP): /init (passenger details, billing)
  Seller App (BPP)-->>Buyer App (BAP): /on_init (final quote, payment terms)
  Buyer App (BAP)->>Seller App (BPP): /confirm (place flight booking)
  Seller App (BPP)-->>Buyer App (BAP): /on_confirm (booking confirmed, ticket issued)
  Buyer App (BAP)->>Seller App (BPP): /cancel (soft cancel request)
  Seller App (BPP)-->>Buyer App (BAP): /on_cancel (cancellation quote & terms)
  Buyer App (BAP)->>Seller App (BPP): /cancel (confirm cancellation)
  Seller App (BPP)-->>Buyer App (BAP): /on_cancel (flight booking cancelled)
```

## init_Airline_200

```mermaid
sequenceDiagram
  participant Buyer App (BAP)
  participant Gateway
  participant Seller App (BPP)
  Buyer App (BAP)->>Gateway: /search (flight search)
  Gateway->>Seller App (BPP): /search (forwarded)
  Seller App (BPP)-->>Buyer App (BAP): /on_search (batch 1: flight catalog)
  Seller App (BPP)-->>Buyer App (BAP): /on_search (unsolicited): batch 2 (flight catalog)
  Seller App (BPP)-->>Buyer App (BAP): /on_search (unsolicited): batch 3 (flight catalog)
  Seller App (BPP)-->>Buyer App (BAP): /on_search (unsolicited): batch 4 (final flight catalog)
  Buyer App (BAP)->>Seller App (BPP): /select (select flight)
  Seller App (BPP)-->>Buyer App (BAP): /on_select (quote, seat availability)
  Buyer App (BAP)->>Seller App (BPP): /select (add-on services, meals/baggage)
  Seller App (BPP)-->>Buyer App (BAP): /on_select (updated quote with add-ons)
  rect rgb(191, 223, 255)
  Buyer App (BAP)->>Seller App (BPP): /init (passenger details, billing)
  end
  Seller App (BPP)-->>Buyer App (BAP): /on_init (final quote, payment terms)
  Buyer App (BAP)->>Seller App (BPP): /confirm (place flight booking)
  Seller App (BPP)-->>Buyer App (BAP): /on_confirm (booking confirmed, ticket issued)
  Buyer App (BAP)->>Seller App (BPP): /cancel (soft cancel request)
  Seller App (BPP)-->>Buyer App (BAP): /on_cancel (cancellation quote & terms)
  Buyer App (BAP)->>Seller App (BPP): /cancel (confirm cancellation)
  Seller App (BPP)-->>Buyer App (BAP): /on_cancel (flight booking cancelled)
```

## on_init_Airline_200

```mermaid
sequenceDiagram
  participant Buyer App (BAP)
  participant Gateway
  participant Seller App (BPP)
  Buyer App (BAP)->>Gateway: /search (flight search)
  Gateway->>Seller App (BPP): /search (forwarded)
  Seller App (BPP)-->>Buyer App (BAP): /on_search (batch 1: flight catalog)
  Seller App (BPP)-->>Buyer App (BAP): /on_search (unsolicited): batch 2 (flight catalog)
  Seller App (BPP)-->>Buyer App (BAP): /on_search (unsolicited): batch 3 (flight catalog)
  Seller App (BPP)-->>Buyer App (BAP): /on_search (unsolicited): batch 4 (final flight catalog)
  Buyer App (BAP)->>Seller App (BPP): /select (select flight)
  Seller App (BPP)-->>Buyer App (BAP): /on_select (quote, seat availability)
  Buyer App (BAP)->>Seller App (BPP): /select (add-on services, meals/baggage)
  Seller App (BPP)-->>Buyer App (BAP): /on_select (updated quote with add-ons)
  Buyer App (BAP)->>Seller App (BPP): /init (passenger details, billing)
  rect rgb(191, 223, 255)
  Seller App (BPP)-->>Buyer App (BAP): /on_init (final quote, payment terms)
  end
  Buyer App (BAP)->>Seller App (BPP): /confirm (place flight booking)
  Seller App (BPP)-->>Buyer App (BAP): /on_confirm (booking confirmed, ticket issued)
  Buyer App (BAP)->>Seller App (BPP): /cancel (soft cancel request)
  Seller App (BPP)-->>Buyer App (BAP): /on_cancel (cancellation quote & terms)
  Buyer App (BAP)->>Seller App (BPP): /cancel (confirm cancellation)
  Seller App (BPP)-->>Buyer App (BAP): /on_cancel (flight booking cancelled)
```

## confirm_Airline_200

```mermaid
sequenceDiagram
  participant Buyer App (BAP)
  participant Gateway
  participant Seller App (BPP)
  Buyer App (BAP)->>Gateway: /search (flight search)
  Gateway->>Seller App (BPP): /search (forwarded)
  Seller App (BPP)-->>Buyer App (BAP): /on_search (batch 1: flight catalog)
  Seller App (BPP)-->>Buyer App (BAP): /on_search (unsolicited): batch 2 (flight catalog)
  Seller App (BPP)-->>Buyer App (BAP): /on_search (unsolicited): batch 3 (flight catalog)
  Seller App (BPP)-->>Buyer App (BAP): /on_search (unsolicited): batch 4 (final flight catalog)
  Buyer App (BAP)->>Seller App (BPP): /select (select flight)
  Seller App (BPP)-->>Buyer App (BAP): /on_select (quote, seat availability)
  Buyer App (BAP)->>Seller App (BPP): /select (add-on services, meals/baggage)
  Seller App (BPP)-->>Buyer App (BAP): /on_select (updated quote with add-ons)
  Buyer App (BAP)->>Seller App (BPP): /init (passenger details, billing)
  Seller App (BPP)-->>Buyer App (BAP): /on_init (final quote, payment terms)
  rect rgb(191, 223, 255)
  Buyer App (BAP)->>Seller App (BPP): /confirm (place flight booking)
  end
  Seller App (BPP)-->>Buyer App (BAP): /on_confirm (booking confirmed, ticket issued)
  Buyer App (BAP)->>Seller App (BPP): /cancel (soft cancel request)
  Seller App (BPP)-->>Buyer App (BAP): /on_cancel (cancellation quote & terms)
  Buyer App (BAP)->>Seller App (BPP): /cancel (confirm cancellation)
  Seller App (BPP)-->>Buyer App (BAP): /on_cancel (flight booking cancelled)
```

## on_confirm_Airline_200

```mermaid
sequenceDiagram
  participant Buyer App (BAP)
  participant Gateway
  participant Seller App (BPP)
  Buyer App (BAP)->>Gateway: /search (flight search)
  Gateway->>Seller App (BPP): /search (forwarded)
  Seller App (BPP)-->>Buyer App (BAP): /on_search (batch 1: flight catalog)
  Seller App (BPP)-->>Buyer App (BAP): /on_search (unsolicited): batch 2 (flight catalog)
  Seller App (BPP)-->>Buyer App (BAP): /on_search (unsolicited): batch 3 (flight catalog)
  Seller App (BPP)-->>Buyer App (BAP): /on_search (unsolicited): batch 4 (final flight catalog)
  Buyer App (BAP)->>Seller App (BPP): /select (select flight)
  Seller App (BPP)-->>Buyer App (BAP): /on_select (quote, seat availability)
  Buyer App (BAP)->>Seller App (BPP): /select (add-on services, meals/baggage)
  Seller App (BPP)-->>Buyer App (BAP): /on_select (updated quote with add-ons)
  Buyer App (BAP)->>Seller App (BPP): /init (passenger details, billing)
  Seller App (BPP)-->>Buyer App (BAP): /on_init (final quote, payment terms)
  Buyer App (BAP)->>Seller App (BPP): /confirm (place flight booking)
  rect rgb(191, 223, 255)
  Seller App (BPP)-->>Buyer App (BAP): /on_confirm (booking confirmed, ticket issued)
  end
  Buyer App (BAP)->>Seller App (BPP): /cancel (soft cancel request)
  Seller App (BPP)-->>Buyer App (BAP): /on_cancel (cancellation quote & terms)
  Buyer App (BAP)->>Seller App (BPP): /cancel (confirm cancellation)
  Seller App (BPP)-->>Buyer App (BAP): /on_cancel (flight booking cancelled)
```

## cancel_Airline_201

```mermaid
sequenceDiagram
  participant Buyer App (BAP)
  participant Gateway
  participant Seller App (BPP)
  Buyer App (BAP)->>Gateway: /search (flight search)
  Gateway->>Seller App (BPP): /search (forwarded)
  Seller App (BPP)-->>Buyer App (BAP): /on_search (batch 1: flight catalog)
  Seller App (BPP)-->>Buyer App (BAP): /on_search (unsolicited): batch 2 (flight catalog)
  Seller App (BPP)-->>Buyer App (BAP): /on_search (unsolicited): batch 3 (flight catalog)
  Seller App (BPP)-->>Buyer App (BAP): /on_search (unsolicited): batch 4 (final flight catalog)
  Buyer App (BAP)->>Seller App (BPP): /select (select flight)
  Seller App (BPP)-->>Buyer App (BAP): /on_select (quote, seat availability)
  Buyer App (BAP)->>Seller App (BPP): /select (add-on services, meals/baggage)
  Seller App (BPP)-->>Buyer App (BAP): /on_select (updated quote with add-ons)
  Buyer App (BAP)->>Seller App (BPP): /init (passenger details, billing)
  Seller App (BPP)-->>Buyer App (BAP): /on_init (final quote, payment terms)
  Buyer App (BAP)->>Seller App (BPP): /confirm (place flight booking)
  Seller App (BPP)-->>Buyer App (BAP): /on_confirm (booking confirmed, ticket issued)
  rect rgb(191, 223, 255)
  Buyer App (BAP)->>Seller App (BPP): /cancel (soft cancel request)
  end
  Seller App (BPP)-->>Buyer App (BAP): /on_cancel (cancellation quote & terms)
  Buyer App (BAP)->>Seller App (BPP): /cancel (confirm cancellation)
  Seller App (BPP)-->>Buyer App (BAP): /on_cancel (flight booking cancelled)
```

## on_cancel_Airline_201

```mermaid
sequenceDiagram
  participant Buyer App (BAP)
  participant Gateway
  participant Seller App (BPP)
  Buyer App (BAP)->>Gateway: /search (flight search)
  Gateway->>Seller App (BPP): /search (forwarded)
  Seller App (BPP)-->>Buyer App (BAP): /on_search (batch 1: flight catalog)
  Seller App (BPP)-->>Buyer App (BAP): /on_search (unsolicited): batch 2 (flight catalog)
  Seller App (BPP)-->>Buyer App (BAP): /on_search (unsolicited): batch 3 (flight catalog)
  Seller App (BPP)-->>Buyer App (BAP): /on_search (unsolicited): batch 4 (final flight catalog)
  Buyer App (BAP)->>Seller App (BPP): /select (select flight)
  Seller App (BPP)-->>Buyer App (BAP): /on_select (quote, seat availability)
  Buyer App (BAP)->>Seller App (BPP): /select (add-on services, meals/baggage)
  Seller App (BPP)-->>Buyer App (BAP): /on_select (updated quote with add-ons)
  Buyer App (BAP)->>Seller App (BPP): /init (passenger details, billing)
  Seller App (BPP)-->>Buyer App (BAP): /on_init (final quote, payment terms)
  Buyer App (BAP)->>Seller App (BPP): /confirm (place flight booking)
  Seller App (BPP)-->>Buyer App (BAP): /on_confirm (booking confirmed, ticket issued)
  Buyer App (BAP)->>Seller App (BPP): /cancel (soft cancel request)
  rect rgb(191, 223, 255)
  Seller App (BPP)-->>Buyer App (BAP): /on_cancel (cancellation quote & terms)
  end
  Buyer App (BAP)->>Seller App (BPP): /cancel (confirm cancellation)
  Seller App (BPP)-->>Buyer App (BAP): /on_cancel (flight booking cancelled)
```

## cancel_Airline_200

```mermaid
sequenceDiagram
  participant Buyer App (BAP)
  participant Gateway
  participant Seller App (BPP)
  Buyer App (BAP)->>Gateway: /search (flight search)
  Gateway->>Seller App (BPP): /search (forwarded)
  Seller App (BPP)-->>Buyer App (BAP): /on_search (batch 1: flight catalog)
  Seller App (BPP)-->>Buyer App (BAP): /on_search (unsolicited): batch 2 (flight catalog)
  Seller App (BPP)-->>Buyer App (BAP): /on_search (unsolicited): batch 3 (flight catalog)
  Seller App (BPP)-->>Buyer App (BAP): /on_search (unsolicited): batch 4 (final flight catalog)
  Buyer App (BAP)->>Seller App (BPP): /select (select flight)
  Seller App (BPP)-->>Buyer App (BAP): /on_select (quote, seat availability)
  Buyer App (BAP)->>Seller App (BPP): /select (add-on services, meals/baggage)
  Seller App (BPP)-->>Buyer App (BAP): /on_select (updated quote with add-ons)
  Buyer App (BAP)->>Seller App (BPP): /init (passenger details, billing)
  Seller App (BPP)-->>Buyer App (BAP): /on_init (final quote, payment terms)
  Buyer App (BAP)->>Seller App (BPP): /confirm (place flight booking)
  Seller App (BPP)-->>Buyer App (BAP): /on_confirm (booking confirmed, ticket issued)
  Buyer App (BAP)->>Seller App (BPP): /cancel (soft cancel request)
  Seller App (BPP)-->>Buyer App (BAP): /on_cancel (cancellation quote & terms)
  rect rgb(191, 223, 255)
  Buyer App (BAP)->>Seller App (BPP): /cancel (confirm cancellation)
  end
  Seller App (BPP)-->>Buyer App (BAP): /on_cancel (flight booking cancelled)
```

## on_cancel_Airline_200

```mermaid
sequenceDiagram
  participant Buyer App (BAP)
  participant Gateway
  participant Seller App (BPP)
  Buyer App (BAP)->>Gateway: /search (flight search)
  Gateway->>Seller App (BPP): /search (forwarded)
  Seller App (BPP)-->>Buyer App (BAP): /on_search (batch 1: flight catalog)
  Seller App (BPP)-->>Buyer App (BAP): /on_search (unsolicited): batch 2 (flight catalog)
  Seller App (BPP)-->>Buyer App (BAP): /on_search (unsolicited): batch 3 (flight catalog)
  Seller App (BPP)-->>Buyer App (BAP): /on_search (unsolicited): batch 4 (final flight catalog)
  Buyer App (BAP)->>Seller App (BPP): /select (select flight)
  Seller App (BPP)-->>Buyer App (BAP): /on_select (quote, seat availability)
  Buyer App (BAP)->>Seller App (BPP): /select (add-on services, meals/baggage)
  Seller App (BPP)-->>Buyer App (BAP): /on_select (updated quote with add-ons)
  Buyer App (BAP)->>Seller App (BPP): /init (passenger details, billing)
  Seller App (BPP)-->>Buyer App (BAP): /on_init (final quote, payment terms)
  Buyer App (BAP)->>Seller App (BPP): /confirm (place flight booking)
  Seller App (BPP)-->>Buyer App (BAP): /on_confirm (booking confirmed, ticket issued)
  Buyer App (BAP)->>Seller App (BPP): /cancel (soft cancel request)
  Seller App (BPP)-->>Buyer App (BAP): /on_cancel (cancellation quote & terms)
  Buyer App (BAP)->>Seller App (BPP): /cancel (confirm cancellation)
  rect rgb(191, 223, 255)
  Seller App (BPP)-->>Buyer App (BAP): /on_cancel (flight booking cancelled)
  end
```

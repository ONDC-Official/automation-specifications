# Purchase Journey(Code Based Flow) — Sequence Diagrams

Internal data file consumed by the Developer Guide's "Sequence Diagram" tab (API Walkthrough).
Not meant to be shown as its own docs page — the frontend filters this slug out of the Use Case
Brief / Additional Resources / Changelog tab lists and instead looks up the section matching the
selected API call's `action_id` (the `##` heading below) to render that step's diagram.

One `## <action_id>` heading per step of `Purchase_Journey_Code_Based_Flow_.yaml`, in that flow's own step order, each followed by its Mermaid `sequenceDiagram`: the whole flow, with that call's own message(s) highlighted — same convention as the other domains' per-step sequence-diagram docs.

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
  Seller App (BPP)-->>Buyer App (BAP): /on_status (unsolicited): flight status update
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
  Seller App (BPP)-->>Buyer App (BAP): /on_status (unsolicited): flight status update
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
  Seller App (BPP)-->>Buyer App (BAP): /on_status (unsolicited): flight status update
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
  Seller App (BPP)-->>Buyer App (BAP): /on_status (unsolicited): flight status update
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
  Seller App (BPP)-->>Buyer App (BAP): /on_status (unsolicited): flight status update
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
  Seller App (BPP)-->>Buyer App (BAP): /on_status (unsolicited): flight status update
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
  Seller App (BPP)-->>Buyer App (BAP): /on_status (unsolicited): flight status update
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
  Seller App (BPP)-->>Buyer App (BAP): /on_status (unsolicited): flight status update
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
  Seller App (BPP)-->>Buyer App (BAP): /on_status (unsolicited): flight status update
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
  Seller App (BPP)-->>Buyer App (BAP): /on_status (unsolicited): flight status update
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
  Seller App (BPP)-->>Buyer App (BAP): /on_status (unsolicited): flight status update
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
  Seller App (BPP)-->>Buyer App (BAP): /on_status (unsolicited): flight status update
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
  Seller App (BPP)-->>Buyer App (BAP): /on_status (unsolicited): flight status update
```

## on_status_unsoliciated_Airline_200

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
  Seller App (BPP)-->>Buyer App (BAP): /on_status (unsolicited): flight status update
  end
```

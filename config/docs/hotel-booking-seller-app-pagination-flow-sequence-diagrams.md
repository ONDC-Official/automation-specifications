# Hotel Booking Seller App Pagination Flow — Sequence Diagrams

Internal data file consumed by the Developer Guide's "Sequence Diagram" tab (API Walkthrough).
Not meant to be shown as its own docs page — the frontend filters this slug out of the Use Case
Brief / Additional Resources / Changelog tab lists and instead looks up the section matching the
selected API call's `action_id` (the `##` heading below) to render that step's diagram.

One `## <action_id>` heading per step of `Hotel_Booking_Seller_App_Pagination_Flow.yaml`, in that flow's own step order, each followed by its Mermaid `sequenceDiagram`: the whole flow, with that call's own message(s) highlighted — same convention as the other domains' per-step sequence-diagram docs.

## search_1

```mermaid
sequenceDiagram
  participant Buyer App (BAP)
  participant Gateway
  participant Seller App (BPP)
  rect rgb(191, 223, 255)
  Buyer App (BAP)->>Gateway: /search (city, stay dates)
  Gateway->>Seller App (BPP): /search (forwarded)
  end
  Seller App (BPP)-->>Buyer App (BAP): /on_search (batch 1: initial hotel catalog)
  Seller App (BPP)-->>Buyer App (BAP): /on_search (unsolicited): batch 2 (additional catalog)
  Seller App (BPP)-->>Buyer App (BAP): /on_search (unsolicited): batch 3 (additional catalog)
  Seller App (BPP)-->>Buyer App (BAP): /on_search (unsolicited): batch 4 (final catalog batch)
```

## on_search_1

```mermaid
sequenceDiagram
  participant Buyer App (BAP)
  participant Gateway
  participant Seller App (BPP)
  Buyer App (BAP)->>Gateway: /search (city, stay dates)
  Gateway->>Seller App (BPP): /search (forwarded)
  rect rgb(191, 223, 255)
  Seller App (BPP)-->>Buyer App (BAP): /on_search (batch 1: initial hotel catalog)
  end
  Seller App (BPP)-->>Buyer App (BAP): /on_search (unsolicited): batch 2 (additional catalog)
  Seller App (BPP)-->>Buyer App (BAP): /on_search (unsolicited): batch 3 (additional catalog)
  Seller App (BPP)-->>Buyer App (BAP): /on_search (unsolicited): batch 4 (final catalog batch)
```

## on_search_2

```mermaid
sequenceDiagram
  participant Buyer App (BAP)
  participant Gateway
  participant Seller App (BPP)
  Buyer App (BAP)->>Gateway: /search (city, stay dates)
  Gateway->>Seller App (BPP): /search (forwarded)
  Seller App (BPP)-->>Buyer App (BAP): /on_search (batch 1: initial hotel catalog)
  rect rgb(191, 223, 255)
  Seller App (BPP)-->>Buyer App (BAP): /on_search (unsolicited): batch 2 (additional catalog)
  end
  Seller App (BPP)-->>Buyer App (BAP): /on_search (unsolicited): batch 3 (additional catalog)
  Seller App (BPP)-->>Buyer App (BAP): /on_search (unsolicited): batch 4 (final catalog batch)
```

## on_search_3

```mermaid
sequenceDiagram
  participant Buyer App (BAP)
  participant Gateway
  participant Seller App (BPP)
  Buyer App (BAP)->>Gateway: /search (city, stay dates)
  Gateway->>Seller App (BPP): /search (forwarded)
  Seller App (BPP)-->>Buyer App (BAP): /on_search (batch 1: initial hotel catalog)
  Seller App (BPP)-->>Buyer App (BAP): /on_search (unsolicited): batch 2 (additional catalog)
  rect rgb(191, 223, 255)
  Seller App (BPP)-->>Buyer App (BAP): /on_search (unsolicited): batch 3 (additional catalog)
  end
  Seller App (BPP)-->>Buyer App (BAP): /on_search (unsolicited): batch 4 (final catalog batch)
```

## on_search_4

```mermaid
sequenceDiagram
  participant Buyer App (BAP)
  participant Gateway
  participant Seller App (BPP)
  Buyer App (BAP)->>Gateway: /search (city, stay dates)
  Gateway->>Seller App (BPP): /search (forwarded)
  Seller App (BPP)-->>Buyer App (BAP): /on_search (batch 1: initial hotel catalog)
  Seller App (BPP)-->>Buyer App (BAP): /on_search (unsolicited): batch 2 (additional catalog)
  Seller App (BPP)-->>Buyer App (BAP): /on_search (unsolicited): batch 3 (additional catalog)
  rect rgb(191, 223, 255)
  Seller App (BPP)-->>Buyer App (BAP): /on_search (unsolicited): batch 4 (final catalog batch)
  end
```

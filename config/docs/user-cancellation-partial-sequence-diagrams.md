# user cancellation partial — Sequence Diagrams

Internal data file consumed by the Developer Guide's "Sequence Diagram" tab (API Walkthrough).
Not meant to be shown as its own docs page — the frontend filters this slug out of the Use Case
Brief / Additional Resources / Changelog tab lists and instead looks up the section matching the
selected API call's `action_id` (the `##` heading below) to render that step's diagram.

One `## <action_id>` heading per step of `user_cancellation_partial.yaml`, in that flow's own step order, each followed by its Mermaid `sequenceDiagram`: the whole flow, with that call's own message(s) highlighted — same convention as the other domains' per-step sequence-diagram docs.

## select_for_partial_cancellation

```mermaid
sequenceDiagram
  participant Buyer App (BAP)
  participant Seller App (BPP)
  rect rgb(191, 223, 255)
  Buyer App (BAP)->>Seller App (BPP): /select (items, attraction pass)
  end
  Seller App (BPP)-->>Buyer App (BAP): /on_select (quote, pass availability)
  Buyer App (BAP)->>Seller App (BPP): /init (visitor details, billing)
  Seller App (BPP)-->>Buyer App (BAP): /on_init (final quote, payment terms)
  Buyer App (BAP)->>Seller App (BPP): /confirm (purchase tickets)
  Seller App (BPP)-->>Buyer App (BAP): /on_confirm (booking confirmed, ticket issued)
  Buyer App (BAP)->>Seller App (BPP): /update (soft partial cancel)
  Seller App (BPP)-->>Buyer App (BAP): /on_update (partial cancellation quote)
  Buyer App (BAP)->>Seller App (BPP): /update (confirm partial cancel)
  Seller App (BPP)-->>Buyer App (BAP): /on_update (order updated)
```

## on_select_without_form

```mermaid
sequenceDiagram
  participant Buyer App (BAP)
  participant Seller App (BPP)
  Buyer App (BAP)->>Seller App (BPP): /select (items, attraction pass)
  rect rgb(191, 223, 255)
  Seller App (BPP)-->>Buyer App (BAP): /on_select (quote, pass availability)
  end
  Buyer App (BAP)->>Seller App (BPP): /init (visitor details, billing)
  Seller App (BPP)-->>Buyer App (BAP): /on_init (final quote, payment terms)
  Buyer App (BAP)->>Seller App (BPP): /confirm (purchase tickets)
  Seller App (BPP)-->>Buyer App (BAP): /on_confirm (booking confirmed, ticket issued)
  Buyer App (BAP)->>Seller App (BPP): /update (soft partial cancel)
  Seller App (BPP)-->>Buyer App (BAP): /on_update (partial cancellation quote)
  Buyer App (BAP)->>Seller App (BPP): /update (confirm partial cancel)
  Seller App (BPP)-->>Buyer App (BAP): /on_update (order updated)
```

## init

```mermaid
sequenceDiagram
  participant Buyer App (BAP)
  participant Seller App (BPP)
  Buyer App (BAP)->>Seller App (BPP): /select (items, attraction pass)
  Seller App (BPP)-->>Buyer App (BAP): /on_select (quote, pass availability)
  rect rgb(191, 223, 255)
  Buyer App (BAP)->>Seller App (BPP): /init (visitor details, billing)
  end
  Seller App (BPP)-->>Buyer App (BAP): /on_init (final quote, payment terms)
  Buyer App (BAP)->>Seller App (BPP): /confirm (purchase tickets)
  Seller App (BPP)-->>Buyer App (BAP): /on_confirm (booking confirmed, ticket issued)
  Buyer App (BAP)->>Seller App (BPP): /update (soft partial cancel)
  Seller App (BPP)-->>Buyer App (BAP): /on_update (partial cancellation quote)
  Buyer App (BAP)->>Seller App (BPP): /update (confirm partial cancel)
  Seller App (BPP)-->>Buyer App (BAP): /on_update (order updated)
```

## on_init

```mermaid
sequenceDiagram
  participant Buyer App (BAP)
  participant Seller App (BPP)
  Buyer App (BAP)->>Seller App (BPP): /select (items, attraction pass)
  Seller App (BPP)-->>Buyer App (BAP): /on_select (quote, pass availability)
  Buyer App (BAP)->>Seller App (BPP): /init (visitor details, billing)
  rect rgb(191, 223, 255)
  Seller App (BPP)-->>Buyer App (BAP): /on_init (final quote, payment terms)
  end
  Buyer App (BAP)->>Seller App (BPP): /confirm (purchase tickets)
  Seller App (BPP)-->>Buyer App (BAP): /on_confirm (booking confirmed, ticket issued)
  Buyer App (BAP)->>Seller App (BPP): /update (soft partial cancel)
  Seller App (BPP)-->>Buyer App (BAP): /on_update (partial cancellation quote)
  Buyer App (BAP)->>Seller App (BPP): /update (confirm partial cancel)
  Seller App (BPP)-->>Buyer App (BAP): /on_update (order updated)
```

## confirm

```mermaid
sequenceDiagram
  participant Buyer App (BAP)
  participant Seller App (BPP)
  Buyer App (BAP)->>Seller App (BPP): /select (items, attraction pass)
  Seller App (BPP)-->>Buyer App (BAP): /on_select (quote, pass availability)
  Buyer App (BAP)->>Seller App (BPP): /init (visitor details, billing)
  Seller App (BPP)-->>Buyer App (BAP): /on_init (final quote, payment terms)
  rect rgb(191, 223, 255)
  Buyer App (BAP)->>Seller App (BPP): /confirm (purchase tickets)
  end
  Seller App (BPP)-->>Buyer App (BAP): /on_confirm (booking confirmed, ticket issued)
  Buyer App (BAP)->>Seller App (BPP): /update (soft partial cancel)
  Seller App (BPP)-->>Buyer App (BAP): /on_update (partial cancellation quote)
  Buyer App (BAP)->>Seller App (BPP): /update (confirm partial cancel)
  Seller App (BPP)-->>Buyer App (BAP): /on_update (order updated)
```

## on_confirm

```mermaid
sequenceDiagram
  participant Buyer App (BAP)
  participant Seller App (BPP)
  Buyer App (BAP)->>Seller App (BPP): /select (items, attraction pass)
  Seller App (BPP)-->>Buyer App (BAP): /on_select (quote, pass availability)
  Buyer App (BAP)->>Seller App (BPP): /init (visitor details, billing)
  Seller App (BPP)-->>Buyer App (BAP): /on_init (final quote, payment terms)
  Buyer App (BAP)->>Seller App (BPP): /confirm (purchase tickets)
  rect rgb(191, 223, 255)
  Seller App (BPP)-->>Buyer App (BAP): /on_confirm (booking confirmed, ticket issued)
  end
  Buyer App (BAP)->>Seller App (BPP): /update (soft partial cancel)
  Seller App (BPP)-->>Buyer App (BAP): /on_update (partial cancellation quote)
  Buyer App (BAP)->>Seller App (BPP): /update (confirm partial cancel)
  Seller App (BPP)-->>Buyer App (BAP): /on_update (order updated)
```

## update_soft_partial_cancellation

```mermaid
sequenceDiagram
  participant Buyer App (BAP)
  participant Seller App (BPP)
  Buyer App (BAP)->>Seller App (BPP): /select (items, attraction pass)
  Seller App (BPP)-->>Buyer App (BAP): /on_select (quote, pass availability)
  Buyer App (BAP)->>Seller App (BPP): /init (visitor details, billing)
  Seller App (BPP)-->>Buyer App (BAP): /on_init (final quote, payment terms)
  Buyer App (BAP)->>Seller App (BPP): /confirm (purchase tickets)
  Seller App (BPP)-->>Buyer App (BAP): /on_confirm (booking confirmed, ticket issued)
  rect rgb(191, 223, 255)
  Buyer App (BAP)->>Seller App (BPP): /update (soft partial cancel)
  end
  Seller App (BPP)-->>Buyer App (BAP): /on_update (partial cancellation quote)
  Buyer App (BAP)->>Seller App (BPP): /update (confirm partial cancel)
  Seller App (BPP)-->>Buyer App (BAP): /on_update (order updated)
```

## on_update_soft_partial_cancellation

```mermaid
sequenceDiagram
  participant Buyer App (BAP)
  participant Seller App (BPP)
  Buyer App (BAP)->>Seller App (BPP): /select (items, attraction pass)
  Seller App (BPP)-->>Buyer App (BAP): /on_select (quote, pass availability)
  Buyer App (BAP)->>Seller App (BPP): /init (visitor details, billing)
  Seller App (BPP)-->>Buyer App (BAP): /on_init (final quote, payment terms)
  Buyer App (BAP)->>Seller App (BPP): /confirm (purchase tickets)
  Seller App (BPP)-->>Buyer App (BAP): /on_confirm (booking confirmed, ticket issued)
  Buyer App (BAP)->>Seller App (BPP): /update (soft partial cancel)
  rect rgb(191, 223, 255)
  Seller App (BPP)-->>Buyer App (BAP): /on_update (partial cancellation quote)
  end
  Buyer App (BAP)->>Seller App (BPP): /update (confirm partial cancel)
  Seller App (BPP)-->>Buyer App (BAP): /on_update (order updated)
```

## update_confirm_partial_cancellation

```mermaid
sequenceDiagram
  participant Buyer App (BAP)
  participant Seller App (BPP)
  Buyer App (BAP)->>Seller App (BPP): /select (items, attraction pass)
  Seller App (BPP)-->>Buyer App (BAP): /on_select (quote, pass availability)
  Buyer App (BAP)->>Seller App (BPP): /init (visitor details, billing)
  Seller App (BPP)-->>Buyer App (BAP): /on_init (final quote, payment terms)
  Buyer App (BAP)->>Seller App (BPP): /confirm (purchase tickets)
  Seller App (BPP)-->>Buyer App (BAP): /on_confirm (booking confirmed, ticket issued)
  Buyer App (BAP)->>Seller App (BPP): /update (soft partial cancel)
  Seller App (BPP)-->>Buyer App (BAP): /on_update (partial cancellation quote)
  rect rgb(191, 223, 255)
  Buyer App (BAP)->>Seller App (BPP): /update (confirm partial cancel)
  end
  Seller App (BPP)-->>Buyer App (BAP): /on_update (order updated)
```

## on_update_confirm_partial_cancellation

```mermaid
sequenceDiagram
  participant Buyer App (BAP)
  participant Seller App (BPP)
  Buyer App (BAP)->>Seller App (BPP): /select (items, attraction pass)
  Seller App (BPP)-->>Buyer App (BAP): /on_select (quote, pass availability)
  Buyer App (BAP)->>Seller App (BPP): /init (visitor details, billing)
  Seller App (BPP)-->>Buyer App (BAP): /on_init (final quote, payment terms)
  Buyer App (BAP)->>Seller App (BPP): /confirm (purchase tickets)
  Seller App (BPP)-->>Buyer App (BAP): /on_confirm (booking confirmed, ticket issued)
  Buyer App (BAP)->>Seller App (BPP): /update (soft partial cancel)
  Seller App (BPP)-->>Buyer App (BAP): /on_update (partial cancellation quote)
  Buyer App (BAP)->>Seller App (BPP): /update (confirm partial cancel)
  rect rgb(191, 223, 255)
  Seller App (BPP)-->>Buyer App (BAP): /on_update (order updated)
  end
```

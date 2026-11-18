# Search and Custom Menu (Incremental Push) — Sequence Diagrams

Internal data file consumed by the Developer Guide's "Sequence Diagram" tab (API Walkthrough).
Not meant to be shown as its own docs page — the frontend filters this slug out of the Use Case
Brief / Additional Resources / Changelog tab lists and instead looks up the section matching the
selected API call's `action_id` (the `##` heading below) to render that step's diagram.

One `## <action_id>` heading per step of `Search_and_Custom_Menu__Incremental_Push_.yaml`, in that flow's own step order, each followed by its Mermaid `sequenceDiagram`: the whole flow, with that call's own message(s) highlighted — same convention as the other domains' per-step sequence-diagram docs.

## search_inc

```mermaid
sequenceDiagram
  participant Buyer App (BAP)
  participant Seller App (BPP)
  rect rgb(191, 223, 255)
  Buyer App (BAP)->>Seller App (BPP): /search (start incremental catalog session)
  end
  Seller App (BPP)-->>Buyer App (BAP): /on_search (unsolicited): changed items
  Seller App (BPP)-->>Buyer App (BAP): /on_search (unsolicited): store closed
  Buyer App (BAP)->>Seller App (BPP): /search (follow-up sync)
```

## on_search_inc

```mermaid
sequenceDiagram
  participant Buyer App (BAP)
  participant Seller App (BPP)
  Buyer App (BAP)->>Seller App (BPP): /search (start incremental catalog session)
  rect rgb(191, 223, 255)
  Seller App (BPP)-->>Buyer App (BAP): /on_search (unsolicited): changed items
  end
  Seller App (BPP)-->>Buyer App (BAP): /on_search (unsolicited): store closed
  Buyer App (BAP)->>Seller App (BPP): /search (follow-up sync)
```

## on_search_inc_close

```mermaid
sequenceDiagram
  participant Buyer App (BAP)
  participant Seller App (BPP)
  Buyer App (BAP)->>Seller App (BPP): /search (start incremental catalog session)
  Seller App (BPP)-->>Buyer App (BAP): /on_search (unsolicited): changed items
  rect rgb(191, 223, 255)
  Seller App (BPP)-->>Buyer App (BAP): /on_search (unsolicited): store closed
  end
  Buyer App (BAP)->>Seller App (BPP): /search (follow-up sync)
```

## search_inc1

```mermaid
sequenceDiagram
  participant Buyer App (BAP)
  participant Seller App (BPP)
  Buyer App (BAP)->>Seller App (BPP): /search (start incremental catalog session)
  Seller App (BPP)-->>Buyer App (BAP): /on_search (unsolicited): changed items
  Seller App (BPP)-->>Buyer App (BAP): /on_search (unsolicited): store closed
  rect rgb(191, 223, 255)
  Buyer App (BAP)->>Seller App (BPP): /search (follow-up sync)
  end
```

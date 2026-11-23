# IntraCity_Purchase_Journey_Flow_Code_Based — Sequence Diagrams

Internal data file consumed by the Developer Guide's "Sequence Diagram" tab (API Walkthrough).
Not meant to be shown as its own docs page — the frontend filters this slug out of the Use Case
Brief / Additional Resources / Changelog tab lists and instead looks up the section matching the
selected API call's `action_id` (the `##` heading below) to render that step's diagram.

One `## <action_id>` heading per step of `IntraCity_Purchase_Journey_Flow_Code_Based.yaml` (Bus), in that flow's own step order, each followed by its Mermaid `sequenceDiagram`: the whole flow, with that call's own message(s) highlighted — same convention as the other domains' per-step sequence-diagram docs.

## search_1

```mermaid
sequenceDiagram
  participant Buyer App (BAP)
  participant Gateway
  participant Seller App (BPP)
  rect rgb(191, 223, 255)
  Buyer App (BAP)->>Seller App (BPP): /search (A to B, peer-to-peer)
  end
  Seller App (BPP)-->>Buyer App (BAP): /on_search
  Buyer App (BAP)->>Seller App (BPP): /select
  Seller App (BPP)-->>Buyer App (BAP): /on_select
  Buyer App (BAP)->>Seller App (BPP): /init
  Seller App (BPP)-->>Buyer App (BAP): /on_init
  Buyer App (BAP)->>Seller App (BPP): /confirm
  Seller App (BPP)-->>Buyer App (BAP): /on_confirm
  Seller App (BPP)-->>Buyer App (BAP): /on_status (unsolicited)
```

## on_search_1

```mermaid
sequenceDiagram
  participant Buyer App (BAP)
  participant Gateway
  participant Seller App (BPP)
  Buyer App (BAP)->>Seller App (BPP): /search (A to B, peer-to-peer)
  rect rgb(191, 223, 255)
  Seller App (BPP)-->>Buyer App (BAP): /on_search
  end
  Buyer App (BAP)->>Seller App (BPP): /select
  Seller App (BPP)-->>Buyer App (BAP): /on_select
  Buyer App (BAP)->>Seller App (BPP): /init
  Seller App (BPP)-->>Buyer App (BAP): /on_init
  Buyer App (BAP)->>Seller App (BPP): /confirm
  Seller App (BPP)-->>Buyer App (BAP): /on_confirm
  Seller App (BPP)-->>Buyer App (BAP): /on_status (unsolicited)
```

## select_1

```mermaid
sequenceDiagram
  participant Buyer App (BAP)
  participant Gateway
  participant Seller App (BPP)
  Buyer App (BAP)->>Seller App (BPP): /search (A to B, peer-to-peer)
  Seller App (BPP)-->>Buyer App (BAP): /on_search
  rect rgb(191, 223, 255)
  Buyer App (BAP)->>Seller App (BPP): /select
  end
  Seller App (BPP)-->>Buyer App (BAP): /on_select
  Buyer App (BAP)->>Seller App (BPP): /init
  Seller App (BPP)-->>Buyer App (BAP): /on_init
  Buyer App (BAP)->>Seller App (BPP): /confirm
  Seller App (BPP)-->>Buyer App (BAP): /on_confirm
  Seller App (BPP)-->>Buyer App (BAP): /on_status (unsolicited)
```

## on_select_1

```mermaid
sequenceDiagram
  participant Buyer App (BAP)
  participant Gateway
  participant Seller App (BPP)
  Buyer App (BAP)->>Seller App (BPP): /search (A to B, peer-to-peer)
  Seller App (BPP)-->>Buyer App (BAP): /on_search
  Buyer App (BAP)->>Seller App (BPP): /select
  rect rgb(191, 223, 255)
  Seller App (BPP)-->>Buyer App (BAP): /on_select
  end
  Buyer App (BAP)->>Seller App (BPP): /init
  Seller App (BPP)-->>Buyer App (BAP): /on_init
  Buyer App (BAP)->>Seller App (BPP): /confirm
  Seller App (BPP)-->>Buyer App (BAP): /on_confirm
  Seller App (BPP)-->>Buyer App (BAP): /on_status (unsolicited)
```

## init_1

```mermaid
sequenceDiagram
  participant Buyer App (BAP)
  participant Gateway
  participant Seller App (BPP)
  Buyer App (BAP)->>Seller App (BPP): /search (A to B, peer-to-peer)
  Seller App (BPP)-->>Buyer App (BAP): /on_search
  Buyer App (BAP)->>Seller App (BPP): /select
  Seller App (BPP)-->>Buyer App (BAP): /on_select
  rect rgb(191, 223, 255)
  Buyer App (BAP)->>Seller App (BPP): /init
  end
  Seller App (BPP)-->>Buyer App (BAP): /on_init
  Buyer App (BAP)->>Seller App (BPP): /confirm
  Seller App (BPP)-->>Buyer App (BAP): /on_confirm
  Seller App (BPP)-->>Buyer App (BAP): /on_status (unsolicited)
```

## on_init_1

```mermaid
sequenceDiagram
  participant Buyer App (BAP)
  participant Gateway
  participant Seller App (BPP)
  Buyer App (BAP)->>Seller App (BPP): /search (A to B, peer-to-peer)
  Seller App (BPP)-->>Buyer App (BAP): /on_search
  Buyer App (BAP)->>Seller App (BPP): /select
  Seller App (BPP)-->>Buyer App (BAP): /on_select
  Buyer App (BAP)->>Seller App (BPP): /init
  rect rgb(191, 223, 255)
  Seller App (BPP)-->>Buyer App (BAP): /on_init
  end
  Buyer App (BAP)->>Seller App (BPP): /confirm
  Seller App (BPP)-->>Buyer App (BAP): /on_confirm
  Seller App (BPP)-->>Buyer App (BAP): /on_status (unsolicited)
```

## confirm_1

```mermaid
sequenceDiagram
  participant Buyer App (BAP)
  participant Gateway
  participant Seller App (BPP)
  Buyer App (BAP)->>Seller App (BPP): /search (A to B, peer-to-peer)
  Seller App (BPP)-->>Buyer App (BAP): /on_search
  Buyer App (BAP)->>Seller App (BPP): /select
  Seller App (BPP)-->>Buyer App (BAP): /on_select
  Buyer App (BAP)->>Seller App (BPP): /init
  Seller App (BPP)-->>Buyer App (BAP): /on_init
  rect rgb(191, 223, 255)
  Buyer App (BAP)->>Seller App (BPP): /confirm
  end
  Seller App (BPP)-->>Buyer App (BAP): /on_confirm
  Seller App (BPP)-->>Buyer App (BAP): /on_status (unsolicited)
```

## on_confirm_1

```mermaid
sequenceDiagram
  participant Buyer App (BAP)
  participant Gateway
  participant Seller App (BPP)
  Buyer App (BAP)->>Seller App (BPP): /search (A to B, peer-to-peer)
  Seller App (BPP)-->>Buyer App (BAP): /on_search
  Buyer App (BAP)->>Seller App (BPP): /select
  Seller App (BPP)-->>Buyer App (BAP): /on_select
  Buyer App (BAP)->>Seller App (BPP): /init
  Seller App (BPP)-->>Buyer App (BAP): /on_init
  Buyer App (BAP)->>Seller App (BPP): /confirm
  rect rgb(191, 223, 255)
  Seller App (BPP)-->>Buyer App (BAP): /on_confirm
  end
  Seller App (BPP)-->>Buyer App (BAP): /on_status (unsolicited)
```

## on_status_1

```mermaid
sequenceDiagram
  participant Buyer App (BAP)
  participant Gateway
  participant Seller App (BPP)
  Buyer App (BAP)->>Seller App (BPP): /search (A to B, peer-to-peer)
  Seller App (BPP)-->>Buyer App (BAP): /on_search
  Buyer App (BAP)->>Seller App (BPP): /select
  Seller App (BPP)-->>Buyer App (BAP): /on_select
  Buyer App (BAP)->>Seller App (BPP): /init
  Seller App (BPP)-->>Buyer App (BAP): /on_init
  Buyer App (BAP)->>Seller App (BPP): /confirm
  Seller App (BPP)-->>Buyer App (BAP): /on_confirm
  rect rgb(191, 223, 255)
  Seller App (BPP)-->>Buyer App (BAP): /on_status (unsolicited)
  end
```

# IntraCity_Search_Pagination_FlowCode_Based — Sequence Diagrams

Internal data file consumed by the Developer Guide's "Sequence Diagram" tab (API Walkthrough).
Not meant to be shown as its own docs page — the frontend filters this slug out of the Use Case
Brief / Additional Resources / Changelog tab lists and instead looks up the section matching the
selected API call's `action_id` (the `##` heading below) to render that step's diagram.

One `## <action_id>` heading per step of `IntraCity_Search_Pagination_FlowCode_Based.yaml` (Bus), in that flow's own step order, each followed by its Mermaid `sequenceDiagram`: the whole flow, with that call's own message(s) highlighted — same convention as the other domains' per-step sequence-diagram docs.

## search0_BUS_201

```mermaid
sequenceDiagram
  participant Buyer App (BAP)
  participant Gateway
  participant Seller App (BPP)
  rect rgb(191, 223, 255)
  Buyer App (BAP)->>Gateway: /search (by city)
  Gateway->>Seller App (BPP): /search (forwarded)
  end
  Seller App (BPP)-->>Buyer App (BAP): /on_search (items SJT, SFSJT, PASS)
  Seller App (BPP)-->>Buyer App (BAP): /on_search (unsolicited): items SJT, SFSJT, PASS
  Seller App (BPP)-->>Buyer App (BAP): /on_search (unsolicited): items SJT, SFSJT, PASS
  Seller App (BPP)-->>Buyer App (BAP): /on_search (unsolicited): items SJT, SFSJT, PASS
```

## on_search_catalog1_BUS_201

```mermaid
sequenceDiagram
  participant Buyer App (BAP)
  participant Gateway
  participant Seller App (BPP)
  Buyer App (BAP)->>Gateway: /search (by city)
  Gateway->>Seller App (BPP): /search (forwarded)
  rect rgb(191, 223, 255)
  Seller App (BPP)-->>Buyer App (BAP): /on_search (items SJT, SFSJT, PASS)
  end
  Seller App (BPP)-->>Buyer App (BAP): /on_search (unsolicited): items SJT, SFSJT, PASS
  Seller App (BPP)-->>Buyer App (BAP): /on_search (unsolicited): items SJT, SFSJT, PASS
  Seller App (BPP)-->>Buyer App (BAP): /on_search (unsolicited): items SJT, SFSJT, PASS
```

## on_search_catalog2_BUS_201

```mermaid
sequenceDiagram
  participant Buyer App (BAP)
  participant Gateway
  participant Seller App (BPP)
  Buyer App (BAP)->>Gateway: /search (by city)
  Gateway->>Seller App (BPP): /search (forwarded)
  Seller App (BPP)-->>Buyer App (BAP): /on_search (items SJT, SFSJT, PASS)
  rect rgb(191, 223, 255)
  Seller App (BPP)-->>Buyer App (BAP): /on_search (unsolicited): items SJT, SFSJT, PASS
  end
  Seller App (BPP)-->>Buyer App (BAP): /on_search (unsolicited): items SJT, SFSJT, PASS
  Seller App (BPP)-->>Buyer App (BAP): /on_search (unsolicited): items SJT, SFSJT, PASS
```

## on_search_catalog3_BUS_201

```mermaid
sequenceDiagram
  participant Buyer App (BAP)
  participant Gateway
  participant Seller App (BPP)
  Buyer App (BAP)->>Gateway: /search (by city)
  Gateway->>Seller App (BPP): /search (forwarded)
  Seller App (BPP)-->>Buyer App (BAP): /on_search (items SJT, SFSJT, PASS)
  Seller App (BPP)-->>Buyer App (BAP): /on_search (unsolicited): items SJT, SFSJT, PASS
  rect rgb(191, 223, 255)
  Seller App (BPP)-->>Buyer App (BAP): /on_search (unsolicited): items SJT, SFSJT, PASS
  end
  Seller App (BPP)-->>Buyer App (BAP): /on_search (unsolicited): items SJT, SFSJT, PASS
```

## on_search_catalog4_BUS_201

```mermaid
sequenceDiagram
  participant Buyer App (BAP)
  participant Gateway
  participant Seller App (BPP)
  Buyer App (BAP)->>Gateway: /search (by city)
  Gateway->>Seller App (BPP): /search (forwarded)
  Seller App (BPP)-->>Buyer App (BAP): /on_search (items SJT, SFSJT, PASS)
  Seller App (BPP)-->>Buyer App (BAP): /on_search (unsolicited): items SJT, SFSJT, PASS
  Seller App (BPP)-->>Buyer App (BAP): /on_search (unsolicited): items SJT, SFSJT, PASS
  rect rgb(191, 223, 255)
  Seller App (BPP)-->>Buyer App (BAP): /on_search (unsolicited): items SJT, SFSJT, PASS
  end
```

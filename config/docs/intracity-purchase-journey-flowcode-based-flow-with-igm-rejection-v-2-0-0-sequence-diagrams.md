# IntraCity_Purchase_Journey_FlowCode_Based_Flow_With_IGM_Rejection(v-2.0.0) — Sequence Diagrams

Internal data file consumed by the Developer Guide's "Sequence Diagram" tab (API Walkthrough).
Not meant to be shown as its own docs page — the frontend filters this slug out of the Use Case
Brief / Additional Resources / Changelog tab lists and instead looks up the section matching the
selected API call's `action_id` (the `##` heading below) to render that step's diagram.

One `## <action_id>` heading per step of `IntraCity_Purchase_Journey_FlowCode_Based_Flow_With_IGM_Rejection_v-2_0_0_.yaml` (Bus), in that flow's own step order, each followed by its Mermaid `sequenceDiagram`: the whole flow, with that call's own message(s) highlighted — same convention as the other domains' per-step sequence-diagram docs.

## search_BUS_201

```mermaid
sequenceDiagram
  participant Buyer App (BAP)
  participant Gateway
  participant Seller App (BPP)
  rect rgb(191, 223, 255)
  Buyer App (BAP)->>Seller App (BPP): /search (A to B, peer-to-peer)
  end
  Seller App (BPP)-->>Buyer App (BAP): /on_search (items SJT, SFSJT)
  Buyer App (BAP)->>Seller App (BPP): /select (item I1 x 1)
  Seller App (BPP)-->>Buyer App (BAP): /on_select (quote)
  Buyer App (BAP)->>Seller App (BPP): /init (payment NOT-PAID)
  Seller App (BPP)-->>Buyer App (BAP): /on_init (payment NOT-PAID)
  Buyer App (BAP)->>Seller App (BPP): /confirm (payment PAID)
  Seller App (BPP)-->>Buyer App (BAP): /on_confirm (order.status ACTIVE)
  Buyer App (BAP)->>Seller App (BPP): /issue (open)
  Seller App (BPP)-->>Buyer App (BAP): /on_issue (processing)
  Seller App (BPP)-->>Buyer App (BAP): /on_issue (unsolicited): resolution
  Buyer App (BAP)->>Seller App (BPP): /issue (resolution reject)
  Seller App (BPP)-->>Buyer App (BAP): /on_issue (processing)
  Seller App (BPP)-->>Buyer App (BAP): /on_issue (unsolicited): resolution
  Buyer App (BAP)->>Seller App (BPP): /issue (escalate)
  Seller App (BPP)-->>Buyer App (BAP): /on_issue (processing)
  Seller App (BPP)-->>Buyer App (BAP): /on_issue (unsolicited): resolution
  Buyer App (BAP)->>Seller App (BPP): /issue (resolution accept)
  Seller App (BPP)-->>Buyer App (BAP): /on_issue (resolved)
  Buyer App (BAP)->>Seller App (BPP): /issue (close)
```

## on_search_BUS_201

```mermaid
sequenceDiagram
  participant Buyer App (BAP)
  participant Gateway
  participant Seller App (BPP)
  Buyer App (BAP)->>Seller App (BPP): /search (A to B, peer-to-peer)
  rect rgb(191, 223, 255)
  Seller App (BPP)-->>Buyer App (BAP): /on_search (items SJT, SFSJT)
  end
  Buyer App (BAP)->>Seller App (BPP): /select (item I1 x 1)
  Seller App (BPP)-->>Buyer App (BAP): /on_select (quote)
  Buyer App (BAP)->>Seller App (BPP): /init (payment NOT-PAID)
  Seller App (BPP)-->>Buyer App (BAP): /on_init (payment NOT-PAID)
  Buyer App (BAP)->>Seller App (BPP): /confirm (payment PAID)
  Seller App (BPP)-->>Buyer App (BAP): /on_confirm (order.status ACTIVE)
  Buyer App (BAP)->>Seller App (BPP): /issue (open)
  Seller App (BPP)-->>Buyer App (BAP): /on_issue (processing)
  Seller App (BPP)-->>Buyer App (BAP): /on_issue (unsolicited): resolution
  Buyer App (BAP)->>Seller App (BPP): /issue (resolution reject)
  Seller App (BPP)-->>Buyer App (BAP): /on_issue (processing)
  Seller App (BPP)-->>Buyer App (BAP): /on_issue (unsolicited): resolution
  Buyer App (BAP)->>Seller App (BPP): /issue (escalate)
  Seller App (BPP)-->>Buyer App (BAP): /on_issue (processing)
  Seller App (BPP)-->>Buyer App (BAP): /on_issue (unsolicited): resolution
  Buyer App (BAP)->>Seller App (BPP): /issue (resolution accept)
  Seller App (BPP)-->>Buyer App (BAP): /on_issue (resolved)
  Buyer App (BAP)->>Seller App (BPP): /issue (close)
```

## select_BUS_201

```mermaid
sequenceDiagram
  participant Buyer App (BAP)
  participant Gateway
  participant Seller App (BPP)
  Buyer App (BAP)->>Seller App (BPP): /search (A to B, peer-to-peer)
  Seller App (BPP)-->>Buyer App (BAP): /on_search (items SJT, SFSJT)
  rect rgb(191, 223, 255)
  Buyer App (BAP)->>Seller App (BPP): /select (item I1 x 1)
  end
  Seller App (BPP)-->>Buyer App (BAP): /on_select (quote)
  Buyer App (BAP)->>Seller App (BPP): /init (payment NOT-PAID)
  Seller App (BPP)-->>Buyer App (BAP): /on_init (payment NOT-PAID)
  Buyer App (BAP)->>Seller App (BPP): /confirm (payment PAID)
  Seller App (BPP)-->>Buyer App (BAP): /on_confirm (order.status ACTIVE)
  Buyer App (BAP)->>Seller App (BPP): /issue (open)
  Seller App (BPP)-->>Buyer App (BAP): /on_issue (processing)
  Seller App (BPP)-->>Buyer App (BAP): /on_issue (unsolicited): resolution
  Buyer App (BAP)->>Seller App (BPP): /issue (resolution reject)
  Seller App (BPP)-->>Buyer App (BAP): /on_issue (processing)
  Seller App (BPP)-->>Buyer App (BAP): /on_issue (unsolicited): resolution
  Buyer App (BAP)->>Seller App (BPP): /issue (escalate)
  Seller App (BPP)-->>Buyer App (BAP): /on_issue (processing)
  Seller App (BPP)-->>Buyer App (BAP): /on_issue (unsolicited): resolution
  Buyer App (BAP)->>Seller App (BPP): /issue (resolution accept)
  Seller App (BPP)-->>Buyer App (BAP): /on_issue (resolved)
  Buyer App (BAP)->>Seller App (BPP): /issue (close)
```

## on_select_BUS_201

```mermaid
sequenceDiagram
  participant Buyer App (BAP)
  participant Gateway
  participant Seller App (BPP)
  Buyer App (BAP)->>Seller App (BPP): /search (A to B, peer-to-peer)
  Seller App (BPP)-->>Buyer App (BAP): /on_search (items SJT, SFSJT)
  Buyer App (BAP)->>Seller App (BPP): /select (item I1 x 1)
  rect rgb(191, 223, 255)
  Seller App (BPP)-->>Buyer App (BAP): /on_select (quote)
  end
  Buyer App (BAP)->>Seller App (BPP): /init (payment NOT-PAID)
  Seller App (BPP)-->>Buyer App (BAP): /on_init (payment NOT-PAID)
  Buyer App (BAP)->>Seller App (BPP): /confirm (payment PAID)
  Seller App (BPP)-->>Buyer App (BAP): /on_confirm (order.status ACTIVE)
  Buyer App (BAP)->>Seller App (BPP): /issue (open)
  Seller App (BPP)-->>Buyer App (BAP): /on_issue (processing)
  Seller App (BPP)-->>Buyer App (BAP): /on_issue (unsolicited): resolution
  Buyer App (BAP)->>Seller App (BPP): /issue (resolution reject)
  Seller App (BPP)-->>Buyer App (BAP): /on_issue (processing)
  Seller App (BPP)-->>Buyer App (BAP): /on_issue (unsolicited): resolution
  Buyer App (BAP)->>Seller App (BPP): /issue (escalate)
  Seller App (BPP)-->>Buyer App (BAP): /on_issue (processing)
  Seller App (BPP)-->>Buyer App (BAP): /on_issue (unsolicited): resolution
  Buyer App (BAP)->>Seller App (BPP): /issue (resolution accept)
  Seller App (BPP)-->>Buyer App (BAP): /on_issue (resolved)
  Buyer App (BAP)->>Seller App (BPP): /issue (close)
```

## init_BUS_201

```mermaid
sequenceDiagram
  participant Buyer App (BAP)
  participant Gateway
  participant Seller App (BPP)
  Buyer App (BAP)->>Seller App (BPP): /search (A to B, peer-to-peer)
  Seller App (BPP)-->>Buyer App (BAP): /on_search (items SJT, SFSJT)
  Buyer App (BAP)->>Seller App (BPP): /select (item I1 x 1)
  Seller App (BPP)-->>Buyer App (BAP): /on_select (quote)
  rect rgb(191, 223, 255)
  Buyer App (BAP)->>Seller App (BPP): /init (payment NOT-PAID)
  end
  Seller App (BPP)-->>Buyer App (BAP): /on_init (payment NOT-PAID)
  Buyer App (BAP)->>Seller App (BPP): /confirm (payment PAID)
  Seller App (BPP)-->>Buyer App (BAP): /on_confirm (order.status ACTIVE)
  Buyer App (BAP)->>Seller App (BPP): /issue (open)
  Seller App (BPP)-->>Buyer App (BAP): /on_issue (processing)
  Seller App (BPP)-->>Buyer App (BAP): /on_issue (unsolicited): resolution
  Buyer App (BAP)->>Seller App (BPP): /issue (resolution reject)
  Seller App (BPP)-->>Buyer App (BAP): /on_issue (processing)
  Seller App (BPP)-->>Buyer App (BAP): /on_issue (unsolicited): resolution
  Buyer App (BAP)->>Seller App (BPP): /issue (escalate)
  Seller App (BPP)-->>Buyer App (BAP): /on_issue (processing)
  Seller App (BPP)-->>Buyer App (BAP): /on_issue (unsolicited): resolution
  Buyer App (BAP)->>Seller App (BPP): /issue (resolution accept)
  Seller App (BPP)-->>Buyer App (BAP): /on_issue (resolved)
  Buyer App (BAP)->>Seller App (BPP): /issue (close)
```

## on_init_BUS_201

```mermaid
sequenceDiagram
  participant Buyer App (BAP)
  participant Gateway
  participant Seller App (BPP)
  Buyer App (BAP)->>Seller App (BPP): /search (A to B, peer-to-peer)
  Seller App (BPP)-->>Buyer App (BAP): /on_search (items SJT, SFSJT)
  Buyer App (BAP)->>Seller App (BPP): /select (item I1 x 1)
  Seller App (BPP)-->>Buyer App (BAP): /on_select (quote)
  Buyer App (BAP)->>Seller App (BPP): /init (payment NOT-PAID)
  rect rgb(191, 223, 255)
  Seller App (BPP)-->>Buyer App (BAP): /on_init (payment NOT-PAID)
  end
  Buyer App (BAP)->>Seller App (BPP): /confirm (payment PAID)
  Seller App (BPP)-->>Buyer App (BAP): /on_confirm (order.status ACTIVE)
  Buyer App (BAP)->>Seller App (BPP): /issue (open)
  Seller App (BPP)-->>Buyer App (BAP): /on_issue (processing)
  Seller App (BPP)-->>Buyer App (BAP): /on_issue (unsolicited): resolution
  Buyer App (BAP)->>Seller App (BPP): /issue (resolution reject)
  Seller App (BPP)-->>Buyer App (BAP): /on_issue (processing)
  Seller App (BPP)-->>Buyer App (BAP): /on_issue (unsolicited): resolution
  Buyer App (BAP)->>Seller App (BPP): /issue (escalate)
  Seller App (BPP)-->>Buyer App (BAP): /on_issue (processing)
  Seller App (BPP)-->>Buyer App (BAP): /on_issue (unsolicited): resolution
  Buyer App (BAP)->>Seller App (BPP): /issue (resolution accept)
  Seller App (BPP)-->>Buyer App (BAP): /on_issue (resolved)
  Buyer App (BAP)->>Seller App (BPP): /issue (close)
```

## confirm_BUS_201

```mermaid
sequenceDiagram
  participant Buyer App (BAP)
  participant Gateway
  participant Seller App (BPP)
  Buyer App (BAP)->>Seller App (BPP): /search (A to B, peer-to-peer)
  Seller App (BPP)-->>Buyer App (BAP): /on_search (items SJT, SFSJT)
  Buyer App (BAP)->>Seller App (BPP): /select (item I1 x 1)
  Seller App (BPP)-->>Buyer App (BAP): /on_select (quote)
  Buyer App (BAP)->>Seller App (BPP): /init (payment NOT-PAID)
  Seller App (BPP)-->>Buyer App (BAP): /on_init (payment NOT-PAID)
  rect rgb(191, 223, 255)
  Buyer App (BAP)->>Seller App (BPP): /confirm (payment PAID)
  end
  Seller App (BPP)-->>Buyer App (BAP): /on_confirm (order.status ACTIVE)
  Buyer App (BAP)->>Seller App (BPP): /issue (open)
  Seller App (BPP)-->>Buyer App (BAP): /on_issue (processing)
  Seller App (BPP)-->>Buyer App (BAP): /on_issue (unsolicited): resolution
  Buyer App (BAP)->>Seller App (BPP): /issue (resolution reject)
  Seller App (BPP)-->>Buyer App (BAP): /on_issue (processing)
  Seller App (BPP)-->>Buyer App (BAP): /on_issue (unsolicited): resolution
  Buyer App (BAP)->>Seller App (BPP): /issue (escalate)
  Seller App (BPP)-->>Buyer App (BAP): /on_issue (processing)
  Seller App (BPP)-->>Buyer App (BAP): /on_issue (unsolicited): resolution
  Buyer App (BAP)->>Seller App (BPP): /issue (resolution accept)
  Seller App (BPP)-->>Buyer App (BAP): /on_issue (resolved)
  Buyer App (BAP)->>Seller App (BPP): /issue (close)
```

## on_confirm_BUS_201

```mermaid
sequenceDiagram
  participant Buyer App (BAP)
  participant Gateway
  participant Seller App (BPP)
  Buyer App (BAP)->>Seller App (BPP): /search (A to B, peer-to-peer)
  Seller App (BPP)-->>Buyer App (BAP): /on_search (items SJT, SFSJT)
  Buyer App (BAP)->>Seller App (BPP): /select (item I1 x 1)
  Seller App (BPP)-->>Buyer App (BAP): /on_select (quote)
  Buyer App (BAP)->>Seller App (BPP): /init (payment NOT-PAID)
  Seller App (BPP)-->>Buyer App (BAP): /on_init (payment NOT-PAID)
  Buyer App (BAP)->>Seller App (BPP): /confirm (payment PAID)
  rect rgb(191, 223, 255)
  Seller App (BPP)-->>Buyer App (BAP): /on_confirm (order.status ACTIVE)
  end
  Buyer App (BAP)->>Seller App (BPP): /issue (open)
  Seller App (BPP)-->>Buyer App (BAP): /on_issue (processing)
  Seller App (BPP)-->>Buyer App (BAP): /on_issue (unsolicited): resolution
  Buyer App (BAP)->>Seller App (BPP): /issue (resolution reject)
  Seller App (BPP)-->>Buyer App (BAP): /on_issue (processing)
  Seller App (BPP)-->>Buyer App (BAP): /on_issue (unsolicited): resolution
  Buyer App (BAP)->>Seller App (BPP): /issue (escalate)
  Seller App (BPP)-->>Buyer App (BAP): /on_issue (processing)
  Seller App (BPP)-->>Buyer App (BAP): /on_issue (unsolicited): resolution
  Buyer App (BAP)->>Seller App (BPP): /issue (resolution accept)
  Seller App (BPP)-->>Buyer App (BAP): /on_issue (resolved)
  Buyer App (BAP)->>Seller App (BPP): /issue (close)
```

## issue_open

```mermaid
sequenceDiagram
  participant Buyer App (BAP)
  participant Gateway
  participant Seller App (BPP)
  Buyer App (BAP)->>Seller App (BPP): /search (A to B, peer-to-peer)
  Seller App (BPP)-->>Buyer App (BAP): /on_search (items SJT, SFSJT)
  Buyer App (BAP)->>Seller App (BPP): /select (item I1 x 1)
  Seller App (BPP)-->>Buyer App (BAP): /on_select (quote)
  Buyer App (BAP)->>Seller App (BPP): /init (payment NOT-PAID)
  Seller App (BPP)-->>Buyer App (BAP): /on_init (payment NOT-PAID)
  Buyer App (BAP)->>Seller App (BPP): /confirm (payment PAID)
  Seller App (BPP)-->>Buyer App (BAP): /on_confirm (order.status ACTIVE)
  rect rgb(191, 223, 255)
  Buyer App (BAP)->>Seller App (BPP): /issue (open)
  end
  Seller App (BPP)-->>Buyer App (BAP): /on_issue (processing)
  Seller App (BPP)-->>Buyer App (BAP): /on_issue (unsolicited): resolution
  Buyer App (BAP)->>Seller App (BPP): /issue (resolution reject)
  Seller App (BPP)-->>Buyer App (BAP): /on_issue (processing)
  Seller App (BPP)-->>Buyer App (BAP): /on_issue (unsolicited): resolution
  Buyer App (BAP)->>Seller App (BPP): /issue (escalate)
  Seller App (BPP)-->>Buyer App (BAP): /on_issue (processing)
  Seller App (BPP)-->>Buyer App (BAP): /on_issue (unsolicited): resolution
  Buyer App (BAP)->>Seller App (BPP): /issue (resolution accept)
  Seller App (BPP)-->>Buyer App (BAP): /on_issue (resolved)
  Buyer App (BAP)->>Seller App (BPP): /issue (close)
```

## on_issue_processing

```mermaid
sequenceDiagram
  participant Buyer App (BAP)
  participant Gateway
  participant Seller App (BPP)
  Buyer App (BAP)->>Seller App (BPP): /search (A to B, peer-to-peer)
  Seller App (BPP)-->>Buyer App (BAP): /on_search (items SJT, SFSJT)
  Buyer App (BAP)->>Seller App (BPP): /select (item I1 x 1)
  Seller App (BPP)-->>Buyer App (BAP): /on_select (quote)
  Buyer App (BAP)->>Seller App (BPP): /init (payment NOT-PAID)
  Seller App (BPP)-->>Buyer App (BAP): /on_init (payment NOT-PAID)
  Buyer App (BAP)->>Seller App (BPP): /confirm (payment PAID)
  Seller App (BPP)-->>Buyer App (BAP): /on_confirm (order.status ACTIVE)
  Buyer App (BAP)->>Seller App (BPP): /issue (open)
  rect rgb(191, 223, 255)
  Seller App (BPP)-->>Buyer App (BAP): /on_issue (processing)
  end
  Seller App (BPP)-->>Buyer App (BAP): /on_issue (unsolicited): resolution
  Buyer App (BAP)->>Seller App (BPP): /issue (resolution reject)
  Seller App (BPP)-->>Buyer App (BAP): /on_issue (processing)
  Seller App (BPP)-->>Buyer App (BAP): /on_issue (unsolicited): resolution
  Buyer App (BAP)->>Seller App (BPP): /issue (escalate)
  Seller App (BPP)-->>Buyer App (BAP): /on_issue (processing)
  Seller App (BPP)-->>Buyer App (BAP): /on_issue (unsolicited): resolution
  Buyer App (BAP)->>Seller App (BPP): /issue (resolution accept)
  Seller App (BPP)-->>Buyer App (BAP): /on_issue (resolved)
  Buyer App (BAP)->>Seller App (BPP): /issue (close)
```

## on_issue_resolution

```mermaid
sequenceDiagram
  participant Buyer App (BAP)
  participant Gateway
  participant Seller App (BPP)
  Buyer App (BAP)->>Seller App (BPP): /search (A to B, peer-to-peer)
  Seller App (BPP)-->>Buyer App (BAP): /on_search (items SJT, SFSJT)
  Buyer App (BAP)->>Seller App (BPP): /select (item I1 x 1)
  Seller App (BPP)-->>Buyer App (BAP): /on_select (quote)
  Buyer App (BAP)->>Seller App (BPP): /init (payment NOT-PAID)
  Seller App (BPP)-->>Buyer App (BAP): /on_init (payment NOT-PAID)
  Buyer App (BAP)->>Seller App (BPP): /confirm (payment PAID)
  Seller App (BPP)-->>Buyer App (BAP): /on_confirm (order.status ACTIVE)
  Buyer App (BAP)->>Seller App (BPP): /issue (open)
  Seller App (BPP)-->>Buyer App (BAP): /on_issue (processing)
  rect rgb(191, 223, 255)
  Seller App (BPP)-->>Buyer App (BAP): /on_issue (unsolicited): resolution
  end
  Buyer App (BAP)->>Seller App (BPP): /issue (resolution reject)
  Seller App (BPP)-->>Buyer App (BAP): /on_issue (processing)
  Seller App (BPP)-->>Buyer App (BAP): /on_issue (unsolicited): resolution
  Buyer App (BAP)->>Seller App (BPP): /issue (escalate)
  Seller App (BPP)-->>Buyer App (BAP): /on_issue (processing)
  Seller App (BPP)-->>Buyer App (BAP): /on_issue (unsolicited): resolution
  Buyer App (BAP)->>Seller App (BPP): /issue (resolution accept)
  Seller App (BPP)-->>Buyer App (BAP): /on_issue (resolved)
  Buyer App (BAP)->>Seller App (BPP): /issue (close)
```

## issue_resolution_reject

```mermaid
sequenceDiagram
  participant Buyer App (BAP)
  participant Gateway
  participant Seller App (BPP)
  Buyer App (BAP)->>Seller App (BPP): /search (A to B, peer-to-peer)
  Seller App (BPP)-->>Buyer App (BAP): /on_search (items SJT, SFSJT)
  Buyer App (BAP)->>Seller App (BPP): /select (item I1 x 1)
  Seller App (BPP)-->>Buyer App (BAP): /on_select (quote)
  Buyer App (BAP)->>Seller App (BPP): /init (payment NOT-PAID)
  Seller App (BPP)-->>Buyer App (BAP): /on_init (payment NOT-PAID)
  Buyer App (BAP)->>Seller App (BPP): /confirm (payment PAID)
  Seller App (BPP)-->>Buyer App (BAP): /on_confirm (order.status ACTIVE)
  Buyer App (BAP)->>Seller App (BPP): /issue (open)
  Seller App (BPP)-->>Buyer App (BAP): /on_issue (processing)
  Seller App (BPP)-->>Buyer App (BAP): /on_issue (unsolicited): resolution
  rect rgb(191, 223, 255)
  Buyer App (BAP)->>Seller App (BPP): /issue (resolution reject)
  end
  Seller App (BPP)-->>Buyer App (BAP): /on_issue (processing)
  Seller App (BPP)-->>Buyer App (BAP): /on_issue (unsolicited): resolution
  Buyer App (BAP)->>Seller App (BPP): /issue (escalate)
  Seller App (BPP)-->>Buyer App (BAP): /on_issue (processing)
  Seller App (BPP)-->>Buyer App (BAP): /on_issue (unsolicited): resolution
  Buyer App (BAP)->>Seller App (BPP): /issue (resolution accept)
  Seller App (BPP)-->>Buyer App (BAP): /on_issue (resolved)
  Buyer App (BAP)->>Seller App (BPP): /issue (close)
```

## on_issue_processing_1

```mermaid
sequenceDiagram
  participant Buyer App (BAP)
  participant Gateway
  participant Seller App (BPP)
  Buyer App (BAP)->>Seller App (BPP): /search (A to B, peer-to-peer)
  Seller App (BPP)-->>Buyer App (BAP): /on_search (items SJT, SFSJT)
  Buyer App (BAP)->>Seller App (BPP): /select (item I1 x 1)
  Seller App (BPP)-->>Buyer App (BAP): /on_select (quote)
  Buyer App (BAP)->>Seller App (BPP): /init (payment NOT-PAID)
  Seller App (BPP)-->>Buyer App (BAP): /on_init (payment NOT-PAID)
  Buyer App (BAP)->>Seller App (BPP): /confirm (payment PAID)
  Seller App (BPP)-->>Buyer App (BAP): /on_confirm (order.status ACTIVE)
  Buyer App (BAP)->>Seller App (BPP): /issue (open)
  Seller App (BPP)-->>Buyer App (BAP): /on_issue (processing)
  Seller App (BPP)-->>Buyer App (BAP): /on_issue (unsolicited): resolution
  Buyer App (BAP)->>Seller App (BPP): /issue (resolution reject)
  rect rgb(191, 223, 255)
  Seller App (BPP)-->>Buyer App (BAP): /on_issue (processing)
  end
  Seller App (BPP)-->>Buyer App (BAP): /on_issue (unsolicited): resolution
  Buyer App (BAP)->>Seller App (BPP): /issue (escalate)
  Seller App (BPP)-->>Buyer App (BAP): /on_issue (processing)
  Seller App (BPP)-->>Buyer App (BAP): /on_issue (unsolicited): resolution
  Buyer App (BAP)->>Seller App (BPP): /issue (resolution accept)
  Seller App (BPP)-->>Buyer App (BAP): /on_issue (resolved)
  Buyer App (BAP)->>Seller App (BPP): /issue (close)
```

## on_issue_resolution_1

```mermaid
sequenceDiagram
  participant Buyer App (BAP)
  participant Gateway
  participant Seller App (BPP)
  Buyer App (BAP)->>Seller App (BPP): /search (A to B, peer-to-peer)
  Seller App (BPP)-->>Buyer App (BAP): /on_search (items SJT, SFSJT)
  Buyer App (BAP)->>Seller App (BPP): /select (item I1 x 1)
  Seller App (BPP)-->>Buyer App (BAP): /on_select (quote)
  Buyer App (BAP)->>Seller App (BPP): /init (payment NOT-PAID)
  Seller App (BPP)-->>Buyer App (BAP): /on_init (payment NOT-PAID)
  Buyer App (BAP)->>Seller App (BPP): /confirm (payment PAID)
  Seller App (BPP)-->>Buyer App (BAP): /on_confirm (order.status ACTIVE)
  Buyer App (BAP)->>Seller App (BPP): /issue (open)
  Seller App (BPP)-->>Buyer App (BAP): /on_issue (processing)
  Seller App (BPP)-->>Buyer App (BAP): /on_issue (unsolicited): resolution
  Buyer App (BAP)->>Seller App (BPP): /issue (resolution reject)
  Seller App (BPP)-->>Buyer App (BAP): /on_issue (processing)
  rect rgb(191, 223, 255)
  Seller App (BPP)-->>Buyer App (BAP): /on_issue (unsolicited): resolution
  end
  Buyer App (BAP)->>Seller App (BPP): /issue (escalate)
  Seller App (BPP)-->>Buyer App (BAP): /on_issue (processing)
  Seller App (BPP)-->>Buyer App (BAP): /on_issue (unsolicited): resolution
  Buyer App (BAP)->>Seller App (BPP): /issue (resolution accept)
  Seller App (BPP)-->>Buyer App (BAP): /on_issue (resolved)
  Buyer App (BAP)->>Seller App (BPP): /issue (close)
```

## issue_escalate

```mermaid
sequenceDiagram
  participant Buyer App (BAP)
  participant Gateway
  participant Seller App (BPP)
  Buyer App (BAP)->>Seller App (BPP): /search (A to B, peer-to-peer)
  Seller App (BPP)-->>Buyer App (BAP): /on_search (items SJT, SFSJT)
  Buyer App (BAP)->>Seller App (BPP): /select (item I1 x 1)
  Seller App (BPP)-->>Buyer App (BAP): /on_select (quote)
  Buyer App (BAP)->>Seller App (BPP): /init (payment NOT-PAID)
  Seller App (BPP)-->>Buyer App (BAP): /on_init (payment NOT-PAID)
  Buyer App (BAP)->>Seller App (BPP): /confirm (payment PAID)
  Seller App (BPP)-->>Buyer App (BAP): /on_confirm (order.status ACTIVE)
  Buyer App (BAP)->>Seller App (BPP): /issue (open)
  Seller App (BPP)-->>Buyer App (BAP): /on_issue (processing)
  Seller App (BPP)-->>Buyer App (BAP): /on_issue (unsolicited): resolution
  Buyer App (BAP)->>Seller App (BPP): /issue (resolution reject)
  Seller App (BPP)-->>Buyer App (BAP): /on_issue (processing)
  Seller App (BPP)-->>Buyer App (BAP): /on_issue (unsolicited): resolution
  rect rgb(191, 223, 255)
  Buyer App (BAP)->>Seller App (BPP): /issue (escalate)
  end
  Seller App (BPP)-->>Buyer App (BAP): /on_issue (processing)
  Seller App (BPP)-->>Buyer App (BAP): /on_issue (unsolicited): resolution
  Buyer App (BAP)->>Seller App (BPP): /issue (resolution accept)
  Seller App (BPP)-->>Buyer App (BAP): /on_issue (resolved)
  Buyer App (BAP)->>Seller App (BPP): /issue (close)
```

## on_issue_processing_2

```mermaid
sequenceDiagram
  participant Buyer App (BAP)
  participant Gateway
  participant Seller App (BPP)
  Buyer App (BAP)->>Seller App (BPP): /search (A to B, peer-to-peer)
  Seller App (BPP)-->>Buyer App (BAP): /on_search (items SJT, SFSJT)
  Buyer App (BAP)->>Seller App (BPP): /select (item I1 x 1)
  Seller App (BPP)-->>Buyer App (BAP): /on_select (quote)
  Buyer App (BAP)->>Seller App (BPP): /init (payment NOT-PAID)
  Seller App (BPP)-->>Buyer App (BAP): /on_init (payment NOT-PAID)
  Buyer App (BAP)->>Seller App (BPP): /confirm (payment PAID)
  Seller App (BPP)-->>Buyer App (BAP): /on_confirm (order.status ACTIVE)
  Buyer App (BAP)->>Seller App (BPP): /issue (open)
  Seller App (BPP)-->>Buyer App (BAP): /on_issue (processing)
  Seller App (BPP)-->>Buyer App (BAP): /on_issue (unsolicited): resolution
  Buyer App (BAP)->>Seller App (BPP): /issue (resolution reject)
  Seller App (BPP)-->>Buyer App (BAP): /on_issue (processing)
  Seller App (BPP)-->>Buyer App (BAP): /on_issue (unsolicited): resolution
  Buyer App (BAP)->>Seller App (BPP): /issue (escalate)
  rect rgb(191, 223, 255)
  Seller App (BPP)-->>Buyer App (BAP): /on_issue (processing)
  end
  Seller App (BPP)-->>Buyer App (BAP): /on_issue (unsolicited): resolution
  Buyer App (BAP)->>Seller App (BPP): /issue (resolution accept)
  Seller App (BPP)-->>Buyer App (BAP): /on_issue (resolved)
  Buyer App (BAP)->>Seller App (BPP): /issue (close)
```

## on_issue_resolution_2

```mermaid
sequenceDiagram
  participant Buyer App (BAP)
  participant Gateway
  participant Seller App (BPP)
  Buyer App (BAP)->>Seller App (BPP): /search (A to B, peer-to-peer)
  Seller App (BPP)-->>Buyer App (BAP): /on_search (items SJT, SFSJT)
  Buyer App (BAP)->>Seller App (BPP): /select (item I1 x 1)
  Seller App (BPP)-->>Buyer App (BAP): /on_select (quote)
  Buyer App (BAP)->>Seller App (BPP): /init (payment NOT-PAID)
  Seller App (BPP)-->>Buyer App (BAP): /on_init (payment NOT-PAID)
  Buyer App (BAP)->>Seller App (BPP): /confirm (payment PAID)
  Seller App (BPP)-->>Buyer App (BAP): /on_confirm (order.status ACTIVE)
  Buyer App (BAP)->>Seller App (BPP): /issue (open)
  Seller App (BPP)-->>Buyer App (BAP): /on_issue (processing)
  Seller App (BPP)-->>Buyer App (BAP): /on_issue (unsolicited): resolution
  Buyer App (BAP)->>Seller App (BPP): /issue (resolution reject)
  Seller App (BPP)-->>Buyer App (BAP): /on_issue (processing)
  Seller App (BPP)-->>Buyer App (BAP): /on_issue (unsolicited): resolution
  Buyer App (BAP)->>Seller App (BPP): /issue (escalate)
  Seller App (BPP)-->>Buyer App (BAP): /on_issue (processing)
  rect rgb(191, 223, 255)
  Seller App (BPP)-->>Buyer App (BAP): /on_issue (unsolicited): resolution
  end
  Buyer App (BAP)->>Seller App (BPP): /issue (resolution accept)
  Seller App (BPP)-->>Buyer App (BAP): /on_issue (resolved)
  Buyer App (BAP)->>Seller App (BPP): /issue (close)
```

## issue_resolution_accept

```mermaid
sequenceDiagram
  participant Buyer App (BAP)
  participant Gateway
  participant Seller App (BPP)
  Buyer App (BAP)->>Seller App (BPP): /search (A to B, peer-to-peer)
  Seller App (BPP)-->>Buyer App (BAP): /on_search (items SJT, SFSJT)
  Buyer App (BAP)->>Seller App (BPP): /select (item I1 x 1)
  Seller App (BPP)-->>Buyer App (BAP): /on_select (quote)
  Buyer App (BAP)->>Seller App (BPP): /init (payment NOT-PAID)
  Seller App (BPP)-->>Buyer App (BAP): /on_init (payment NOT-PAID)
  Buyer App (BAP)->>Seller App (BPP): /confirm (payment PAID)
  Seller App (BPP)-->>Buyer App (BAP): /on_confirm (order.status ACTIVE)
  Buyer App (BAP)->>Seller App (BPP): /issue (open)
  Seller App (BPP)-->>Buyer App (BAP): /on_issue (processing)
  Seller App (BPP)-->>Buyer App (BAP): /on_issue (unsolicited): resolution
  Buyer App (BAP)->>Seller App (BPP): /issue (resolution reject)
  Seller App (BPP)-->>Buyer App (BAP): /on_issue (processing)
  Seller App (BPP)-->>Buyer App (BAP): /on_issue (unsolicited): resolution
  Buyer App (BAP)->>Seller App (BPP): /issue (escalate)
  Seller App (BPP)-->>Buyer App (BAP): /on_issue (processing)
  Seller App (BPP)-->>Buyer App (BAP): /on_issue (unsolicited): resolution
  rect rgb(191, 223, 255)
  Buyer App (BAP)->>Seller App (BPP): /issue (resolution accept)
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
  Buyer App (BAP)->>Seller App (BPP): /search (A to B, peer-to-peer)
  Seller App (BPP)-->>Buyer App (BAP): /on_search (items SJT, SFSJT)
  Buyer App (BAP)->>Seller App (BPP): /select (item I1 x 1)
  Seller App (BPP)-->>Buyer App (BAP): /on_select (quote)
  Buyer App (BAP)->>Seller App (BPP): /init (payment NOT-PAID)
  Seller App (BPP)-->>Buyer App (BAP): /on_init (payment NOT-PAID)
  Buyer App (BAP)->>Seller App (BPP): /confirm (payment PAID)
  Seller App (BPP)-->>Buyer App (BAP): /on_confirm (order.status ACTIVE)
  Buyer App (BAP)->>Seller App (BPP): /issue (open)
  Seller App (BPP)-->>Buyer App (BAP): /on_issue (processing)
  Seller App (BPP)-->>Buyer App (BAP): /on_issue (unsolicited): resolution
  Buyer App (BAP)->>Seller App (BPP): /issue (resolution reject)
  Seller App (BPP)-->>Buyer App (BAP): /on_issue (processing)
  Seller App (BPP)-->>Buyer App (BAP): /on_issue (unsolicited): resolution
  Buyer App (BAP)->>Seller App (BPP): /issue (escalate)
  Seller App (BPP)-->>Buyer App (BAP): /on_issue (processing)
  Seller App (BPP)-->>Buyer App (BAP): /on_issue (unsolicited): resolution
  Buyer App (BAP)->>Seller App (BPP): /issue (resolution accept)
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
  Buyer App (BAP)->>Seller App (BPP): /search (A to B, peer-to-peer)
  Seller App (BPP)-->>Buyer App (BAP): /on_search (items SJT, SFSJT)
  Buyer App (BAP)->>Seller App (BPP): /select (item I1 x 1)
  Seller App (BPP)-->>Buyer App (BAP): /on_select (quote)
  Buyer App (BAP)->>Seller App (BPP): /init (payment NOT-PAID)
  Seller App (BPP)-->>Buyer App (BAP): /on_init (payment NOT-PAID)
  Buyer App (BAP)->>Seller App (BPP): /confirm (payment PAID)
  Seller App (BPP)-->>Buyer App (BAP): /on_confirm (order.status ACTIVE)
  Buyer App (BAP)->>Seller App (BPP): /issue (open)
  Seller App (BPP)-->>Buyer App (BAP): /on_issue (processing)
  Seller App (BPP)-->>Buyer App (BAP): /on_issue (unsolicited): resolution
  Buyer App (BAP)->>Seller App (BPP): /issue (resolution reject)
  Seller App (BPP)-->>Buyer App (BAP): /on_issue (processing)
  Seller App (BPP)-->>Buyer App (BAP): /on_issue (unsolicited): resolution
  Buyer App (BAP)->>Seller App (BPP): /issue (escalate)
  Seller App (BPP)-->>Buyer App (BAP): /on_issue (processing)
  Seller App (BPP)-->>Buyer App (BAP): /on_issue (unsolicited): resolution
  Buyer App (BAP)->>Seller App (BPP): /issue (resolution accept)
  Seller App (BPP)-->>Buyer App (BAP): /on_issue (resolved)
  rect rgb(191, 223, 255)
  Buyer App (BAP)->>Seller App (BPP): /issue (close)
  end
```

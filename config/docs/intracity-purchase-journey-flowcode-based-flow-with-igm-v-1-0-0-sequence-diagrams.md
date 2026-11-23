# IntraCity_Purchase_Journey_FlowCode_Based_Flow_With_IGM(v-1.0.0) — Sequence Diagrams

Internal data file consumed by the Developer Guide's "Sequence Diagram" tab (API Walkthrough).
Not meant to be shown as its own docs page — the frontend filters this slug out of the Use Case
Brief / Additional Resources / Changelog tab lists and instead looks up the section matching the
selected API call's `action_id` (the `##` heading below) to render that step's diagram.

One `## <action_id>` heading per step of `IntraCity_Purchase_Journey_FlowCode_Based_Flow_With_IGM_v-1_0_0_.yaml` (Bus), in that flow's own step order, each followed by its Mermaid `sequenceDiagram`: the whole flow, with that call's own message(s) highlighted — same convention as the other domains' per-step sequence-diagram docs.

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
  Buyer App (BAP)->>Seller App (BPP): /update (update_target order.billing)
  Seller App (BPP)-->>Buyer App (BAP): /on_update (order.status ACTIVE)
  Buyer App (BAP)->>Seller App (BPP): /issue
  Seller App (BPP)-->>Buyer App (BAP): /on_issue
  Seller App (BPP)-->>Buyer App (BAP): /on_issue_status (unsolicited)
  Buyer App (BAP)->>Seller App (BPP): /issue
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
  Buyer App (BAP)->>Seller App (BPP): /update (update_target order.billing)
  Seller App (BPP)-->>Buyer App (BAP): /on_update (order.status ACTIVE)
  Buyer App (BAP)->>Seller App (BPP): /issue
  Seller App (BPP)-->>Buyer App (BAP): /on_issue
  Seller App (BPP)-->>Buyer App (BAP): /on_issue_status (unsolicited)
  Buyer App (BAP)->>Seller App (BPP): /issue
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
  Buyer App (BAP)->>Seller App (BPP): /update (update_target order.billing)
  Seller App (BPP)-->>Buyer App (BAP): /on_update (order.status ACTIVE)
  Buyer App (BAP)->>Seller App (BPP): /issue
  Seller App (BPP)-->>Buyer App (BAP): /on_issue
  Seller App (BPP)-->>Buyer App (BAP): /on_issue_status (unsolicited)
  Buyer App (BAP)->>Seller App (BPP): /issue
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
  Buyer App (BAP)->>Seller App (BPP): /update (update_target order.billing)
  Seller App (BPP)-->>Buyer App (BAP): /on_update (order.status ACTIVE)
  Buyer App (BAP)->>Seller App (BPP): /issue
  Seller App (BPP)-->>Buyer App (BAP): /on_issue
  Seller App (BPP)-->>Buyer App (BAP): /on_issue_status (unsolicited)
  Buyer App (BAP)->>Seller App (BPP): /issue
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
  Buyer App (BAP)->>Seller App (BPP): /update (update_target order.billing)
  Seller App (BPP)-->>Buyer App (BAP): /on_update (order.status ACTIVE)
  Buyer App (BAP)->>Seller App (BPP): /issue
  Seller App (BPP)-->>Buyer App (BAP): /on_issue
  Seller App (BPP)-->>Buyer App (BAP): /on_issue_status (unsolicited)
  Buyer App (BAP)->>Seller App (BPP): /issue
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
  Buyer App (BAP)->>Seller App (BPP): /update (update_target order.billing)
  Seller App (BPP)-->>Buyer App (BAP): /on_update (order.status ACTIVE)
  Buyer App (BAP)->>Seller App (BPP): /issue
  Seller App (BPP)-->>Buyer App (BAP): /on_issue
  Seller App (BPP)-->>Buyer App (BAP): /on_issue_status (unsolicited)
  Buyer App (BAP)->>Seller App (BPP): /issue
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
  Buyer App (BAP)->>Seller App (BPP): /update (update_target order.billing)
  Seller App (BPP)-->>Buyer App (BAP): /on_update (order.status ACTIVE)
  Buyer App (BAP)->>Seller App (BPP): /issue
  Seller App (BPP)-->>Buyer App (BAP): /on_issue
  Seller App (BPP)-->>Buyer App (BAP): /on_issue_status (unsolicited)
  Buyer App (BAP)->>Seller App (BPP): /issue
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
  Buyer App (BAP)->>Seller App (BPP): /update (update_target order.billing)
  Seller App (BPP)-->>Buyer App (BAP): /on_update (order.status ACTIVE)
  Buyer App (BAP)->>Seller App (BPP): /issue
  Seller App (BPP)-->>Buyer App (BAP): /on_issue
  Seller App (BPP)-->>Buyer App (BAP): /on_issue_status (unsolicited)
  Buyer App (BAP)->>Seller App (BPP): /issue
```

## update_purchase_flow_BUS_210

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
  Buyer App (BAP)->>Seller App (BPP): /update (update_target order.billing)
  end
  Seller App (BPP)-->>Buyer App (BAP): /on_update (order.status ACTIVE)
  Buyer App (BAP)->>Seller App (BPP): /issue
  Seller App (BPP)-->>Buyer App (BAP): /on_issue
  Seller App (BPP)-->>Buyer App (BAP): /on_issue_status (unsolicited)
  Buyer App (BAP)->>Seller App (BPP): /issue
```

## on_update_purchase_flow_BUS_210

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
  Buyer App (BAP)->>Seller App (BPP): /update (update_target order.billing)
  rect rgb(191, 223, 255)
  Seller App (BPP)-->>Buyer App (BAP): /on_update (order.status ACTIVE)
  end
  Buyer App (BAP)->>Seller App (BPP): /issue
  Seller App (BPP)-->>Buyer App (BAP): /on_issue
  Seller App (BPP)-->>Buyer App (BAP): /on_issue_status (unsolicited)
  Buyer App (BAP)->>Seller App (BPP): /issue
```

## issue_open_100

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
  Buyer App (BAP)->>Seller App (BPP): /update (update_target order.billing)
  Seller App (BPP)-->>Buyer App (BAP): /on_update (order.status ACTIVE)
  rect rgb(191, 223, 255)
  Buyer App (BAP)->>Seller App (BPP): /issue
  end
  Seller App (BPP)-->>Buyer App (BAP): /on_issue
  Seller App (BPP)-->>Buyer App (BAP): /on_issue_status (unsolicited)
  Buyer App (BAP)->>Seller App (BPP): /issue
```

## on_issue_processing_100

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
  Buyer App (BAP)->>Seller App (BPP): /update (update_target order.billing)
  Seller App (BPP)-->>Buyer App (BAP): /on_update (order.status ACTIVE)
  Buyer App (BAP)->>Seller App (BPP): /issue
  rect rgb(191, 223, 255)
  Seller App (BPP)-->>Buyer App (BAP): /on_issue
  end
  Seller App (BPP)-->>Buyer App (BAP): /on_issue_status (unsolicited)
  Buyer App (BAP)->>Seller App (BPP): /issue
```

## on_issue_resolved_100

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
  Buyer App (BAP)->>Seller App (BPP): /update (update_target order.billing)
  Seller App (BPP)-->>Buyer App (BAP): /on_update (order.status ACTIVE)
  Buyer App (BAP)->>Seller App (BPP): /issue
  Seller App (BPP)-->>Buyer App (BAP): /on_issue
  rect rgb(191, 223, 255)
  Seller App (BPP)-->>Buyer App (BAP): /on_issue_status (unsolicited)
  end
  Buyer App (BAP)->>Seller App (BPP): /issue
```

## issue_close_100

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
  Buyer App (BAP)->>Seller App (BPP): /update (update_target order.billing)
  Seller App (BPP)-->>Buyer App (BAP): /on_update (order.status ACTIVE)
  Buyer App (BAP)->>Seller App (BPP): /issue
  Seller App (BPP)-->>Buyer App (BAP): /on_issue
  Seller App (BPP)-->>Buyer App (BAP): /on_issue_status (unsolicited)
  rect rgb(191, 223, 255)
  Buyer App (BAP)->>Seller App (BPP): /issue
  end
```

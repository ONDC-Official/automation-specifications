# PURCHASE_JOURNEY_STATION_CODE_BASED_FLOW_WITH_IGM(v-1.0.0) — Sequence Diagrams

Internal data file consumed by the Developer Guide's "Sequence Diagram" tab (API Walkthrough).
Not meant to be shown as its own docs page — the frontend filters this slug out of the Use Case
Brief / Additional Resources / Changelog tab lists and instead looks up the section matching the
selected API call's `action_id` (the `##` heading below) to render that step's diagram.

One `## <action_id>` heading per step of `PURCHASE_JOURNEY_STATION_CODE_BASED_FLOW_WITH_IGM_v-1_0_0_.yaml` (Metro), in that flow's own step order, each followed by its Mermaid `sequenceDiagram`: the whole flow, with that call's own message(s) highlighted — same convention as the other domains' per-step sequence-diagram docs.

## search2_METRO_210

```mermaid
sequenceDiagram
  participant Buyer App (BAP)
  participant Gateway
  participant Seller App (BPP)
  rect rgb(191, 223, 255)
  Buyer App (BAP)->>Seller App (BPP): /search (A to B, peer-to-peer)
  end
  Seller App (BPP)-->>Buyer App (BAP): /on_search (items SJT, RJT)
  Buyer App (BAP)->>Seller App (BPP): /select (item I1 x 1)
  Seller App (BPP)-->>Buyer App (BAP): /on_select (quote)
  Buyer App (BAP)->>Seller App (BPP): /init (payment NOT-PAID)
  Seller App (BPP)-->>Buyer App (BAP): /on_init (payment NOT-PAID)
  Buyer App (BAP)->>Seller App (BPP): /confirm (payment PAID)
  Seller App (BPP)-->>Buyer App (BAP): /on_confirm (order.status ACTIVE; TICKET ACTIVE)
  Seller App (BPP)-->>Buyer App (BAP): /on_status (unsolicited): order.status ACTIVE; TICKET CHECKED_IN
  Seller App (BPP)-->>Buyer App (BAP): /on_status (unsolicited): order.status COMPLETED; TICKET CHECKED_OUT
  Buyer App (BAP)->>Seller App (BPP): /issue
  Seller App (BPP)-->>Buyer App (BAP): /on_issue
  Seller App (BPP)-->>Buyer App (BAP): /on_issue_status (unsolicited)
  Buyer App (BAP)->>Seller App (BPP): /issue
```

## on_search2_METRO_210

```mermaid
sequenceDiagram
  participant Buyer App (BAP)
  participant Gateway
  participant Seller App (BPP)
  Buyer App (BAP)->>Seller App (BPP): /search (A to B, peer-to-peer)
  rect rgb(191, 223, 255)
  Seller App (BPP)-->>Buyer App (BAP): /on_search (items SJT, RJT)
  end
  Buyer App (BAP)->>Seller App (BPP): /select (item I1 x 1)
  Seller App (BPP)-->>Buyer App (BAP): /on_select (quote)
  Buyer App (BAP)->>Seller App (BPP): /init (payment NOT-PAID)
  Seller App (BPP)-->>Buyer App (BAP): /on_init (payment NOT-PAID)
  Buyer App (BAP)->>Seller App (BPP): /confirm (payment PAID)
  Seller App (BPP)-->>Buyer App (BAP): /on_confirm (order.status ACTIVE; TICKET ACTIVE)
  Seller App (BPP)-->>Buyer App (BAP): /on_status (unsolicited): order.status ACTIVE; TICKET CHECKED_IN
  Seller App (BPP)-->>Buyer App (BAP): /on_status (unsolicited): order.status COMPLETED; TICKET CHECKED_OUT
  Buyer App (BAP)->>Seller App (BPP): /issue
  Seller App (BPP)-->>Buyer App (BAP): /on_issue
  Seller App (BPP)-->>Buyer App (BAP): /on_issue_status (unsolicited)
  Buyer App (BAP)->>Seller App (BPP): /issue
```

## select_METRO_210

```mermaid
sequenceDiagram
  participant Buyer App (BAP)
  participant Gateway
  participant Seller App (BPP)
  Buyer App (BAP)->>Seller App (BPP): /search (A to B, peer-to-peer)
  Seller App (BPP)-->>Buyer App (BAP): /on_search (items SJT, RJT)
  rect rgb(191, 223, 255)
  Buyer App (BAP)->>Seller App (BPP): /select (item I1 x 1)
  end
  Seller App (BPP)-->>Buyer App (BAP): /on_select (quote)
  Buyer App (BAP)->>Seller App (BPP): /init (payment NOT-PAID)
  Seller App (BPP)-->>Buyer App (BAP): /on_init (payment NOT-PAID)
  Buyer App (BAP)->>Seller App (BPP): /confirm (payment PAID)
  Seller App (BPP)-->>Buyer App (BAP): /on_confirm (order.status ACTIVE; TICKET ACTIVE)
  Seller App (BPP)-->>Buyer App (BAP): /on_status (unsolicited): order.status ACTIVE; TICKET CHECKED_IN
  Seller App (BPP)-->>Buyer App (BAP): /on_status (unsolicited): order.status COMPLETED; TICKET CHECKED_OUT
  Buyer App (BAP)->>Seller App (BPP): /issue
  Seller App (BPP)-->>Buyer App (BAP): /on_issue
  Seller App (BPP)-->>Buyer App (BAP): /on_issue_status (unsolicited)
  Buyer App (BAP)->>Seller App (BPP): /issue
```

## on_select_METRO_210

```mermaid
sequenceDiagram
  participant Buyer App (BAP)
  participant Gateway
  participant Seller App (BPP)
  Buyer App (BAP)->>Seller App (BPP): /search (A to B, peer-to-peer)
  Seller App (BPP)-->>Buyer App (BAP): /on_search (items SJT, RJT)
  Buyer App (BAP)->>Seller App (BPP): /select (item I1 x 1)
  rect rgb(191, 223, 255)
  Seller App (BPP)-->>Buyer App (BAP): /on_select (quote)
  end
  Buyer App (BAP)->>Seller App (BPP): /init (payment NOT-PAID)
  Seller App (BPP)-->>Buyer App (BAP): /on_init (payment NOT-PAID)
  Buyer App (BAP)->>Seller App (BPP): /confirm (payment PAID)
  Seller App (BPP)-->>Buyer App (BAP): /on_confirm (order.status ACTIVE; TICKET ACTIVE)
  Seller App (BPP)-->>Buyer App (BAP): /on_status (unsolicited): order.status ACTIVE; TICKET CHECKED_IN
  Seller App (BPP)-->>Buyer App (BAP): /on_status (unsolicited): order.status COMPLETED; TICKET CHECKED_OUT
  Buyer App (BAP)->>Seller App (BPP): /issue
  Seller App (BPP)-->>Buyer App (BAP): /on_issue
  Seller App (BPP)-->>Buyer App (BAP): /on_issue_status (unsolicited)
  Buyer App (BAP)->>Seller App (BPP): /issue
```

## init_METRO_210

```mermaid
sequenceDiagram
  participant Buyer App (BAP)
  participant Gateway
  participant Seller App (BPP)
  Buyer App (BAP)->>Seller App (BPP): /search (A to B, peer-to-peer)
  Seller App (BPP)-->>Buyer App (BAP): /on_search (items SJT, RJT)
  Buyer App (BAP)->>Seller App (BPP): /select (item I1 x 1)
  Seller App (BPP)-->>Buyer App (BAP): /on_select (quote)
  rect rgb(191, 223, 255)
  Buyer App (BAP)->>Seller App (BPP): /init (payment NOT-PAID)
  end
  Seller App (BPP)-->>Buyer App (BAP): /on_init (payment NOT-PAID)
  Buyer App (BAP)->>Seller App (BPP): /confirm (payment PAID)
  Seller App (BPP)-->>Buyer App (BAP): /on_confirm (order.status ACTIVE; TICKET ACTIVE)
  Seller App (BPP)-->>Buyer App (BAP): /on_status (unsolicited): order.status ACTIVE; TICKET CHECKED_IN
  Seller App (BPP)-->>Buyer App (BAP): /on_status (unsolicited): order.status COMPLETED; TICKET CHECKED_OUT
  Buyer App (BAP)->>Seller App (BPP): /issue
  Seller App (BPP)-->>Buyer App (BAP): /on_issue
  Seller App (BPP)-->>Buyer App (BAP): /on_issue_status (unsolicited)
  Buyer App (BAP)->>Seller App (BPP): /issue
```

## on_init_METRO_210

```mermaid
sequenceDiagram
  participant Buyer App (BAP)
  participant Gateway
  participant Seller App (BPP)
  Buyer App (BAP)->>Seller App (BPP): /search (A to B, peer-to-peer)
  Seller App (BPP)-->>Buyer App (BAP): /on_search (items SJT, RJT)
  Buyer App (BAP)->>Seller App (BPP): /select (item I1 x 1)
  Seller App (BPP)-->>Buyer App (BAP): /on_select (quote)
  Buyer App (BAP)->>Seller App (BPP): /init (payment NOT-PAID)
  rect rgb(191, 223, 255)
  Seller App (BPP)-->>Buyer App (BAP): /on_init (payment NOT-PAID)
  end
  Buyer App (BAP)->>Seller App (BPP): /confirm (payment PAID)
  Seller App (BPP)-->>Buyer App (BAP): /on_confirm (order.status ACTIVE; TICKET ACTIVE)
  Seller App (BPP)-->>Buyer App (BAP): /on_status (unsolicited): order.status ACTIVE; TICKET CHECKED_IN
  Seller App (BPP)-->>Buyer App (BAP): /on_status (unsolicited): order.status COMPLETED; TICKET CHECKED_OUT
  Buyer App (BAP)->>Seller App (BPP): /issue
  Seller App (BPP)-->>Buyer App (BAP): /on_issue
  Seller App (BPP)-->>Buyer App (BAP): /on_issue_status (unsolicited)
  Buyer App (BAP)->>Seller App (BPP): /issue
```

## confirm_METRO_210

```mermaid
sequenceDiagram
  participant Buyer App (BAP)
  participant Gateway
  participant Seller App (BPP)
  Buyer App (BAP)->>Seller App (BPP): /search (A to B, peer-to-peer)
  Seller App (BPP)-->>Buyer App (BAP): /on_search (items SJT, RJT)
  Buyer App (BAP)->>Seller App (BPP): /select (item I1 x 1)
  Seller App (BPP)-->>Buyer App (BAP): /on_select (quote)
  Buyer App (BAP)->>Seller App (BPP): /init (payment NOT-PAID)
  Seller App (BPP)-->>Buyer App (BAP): /on_init (payment NOT-PAID)
  rect rgb(191, 223, 255)
  Buyer App (BAP)->>Seller App (BPP): /confirm (payment PAID)
  end
  Seller App (BPP)-->>Buyer App (BAP): /on_confirm (order.status ACTIVE; TICKET ACTIVE)
  Seller App (BPP)-->>Buyer App (BAP): /on_status (unsolicited): order.status ACTIVE; TICKET CHECKED_IN
  Seller App (BPP)-->>Buyer App (BAP): /on_status (unsolicited): order.status COMPLETED; TICKET CHECKED_OUT
  Buyer App (BAP)->>Seller App (BPP): /issue
  Seller App (BPP)-->>Buyer App (BAP): /on_issue
  Seller App (BPP)-->>Buyer App (BAP): /on_issue_status (unsolicited)
  Buyer App (BAP)->>Seller App (BPP): /issue
```

## on_confirm_METRO_210

```mermaid
sequenceDiagram
  participant Buyer App (BAP)
  participant Gateway
  participant Seller App (BPP)
  Buyer App (BAP)->>Seller App (BPP): /search (A to B, peer-to-peer)
  Seller App (BPP)-->>Buyer App (BAP): /on_search (items SJT, RJT)
  Buyer App (BAP)->>Seller App (BPP): /select (item I1 x 1)
  Seller App (BPP)-->>Buyer App (BAP): /on_select (quote)
  Buyer App (BAP)->>Seller App (BPP): /init (payment NOT-PAID)
  Seller App (BPP)-->>Buyer App (BAP): /on_init (payment NOT-PAID)
  Buyer App (BAP)->>Seller App (BPP): /confirm (payment PAID)
  rect rgb(191, 223, 255)
  Seller App (BPP)-->>Buyer App (BAP): /on_confirm (order.status ACTIVE; TICKET ACTIVE)
  end
  Seller App (BPP)-->>Buyer App (BAP): /on_status (unsolicited): order.status ACTIVE; TICKET CHECKED_IN
  Seller App (BPP)-->>Buyer App (BAP): /on_status (unsolicited): order.status COMPLETED; TICKET CHECKED_OUT
  Buyer App (BAP)->>Seller App (BPP): /issue
  Seller App (BPP)-->>Buyer App (BAP): /on_issue
  Seller App (BPP)-->>Buyer App (BAP): /on_issue_status (unsolicited)
  Buyer App (BAP)->>Seller App (BPP): /issue
```

## on_status_active_METRO_210

```mermaid
sequenceDiagram
  participant Buyer App (BAP)
  participant Gateway
  participant Seller App (BPP)
  Buyer App (BAP)->>Seller App (BPP): /search (A to B, peer-to-peer)
  Seller App (BPP)-->>Buyer App (BAP): /on_search (items SJT, RJT)
  Buyer App (BAP)->>Seller App (BPP): /select (item I1 x 1)
  Seller App (BPP)-->>Buyer App (BAP): /on_select (quote)
  Buyer App (BAP)->>Seller App (BPP): /init (payment NOT-PAID)
  Seller App (BPP)-->>Buyer App (BAP): /on_init (payment NOT-PAID)
  Buyer App (BAP)->>Seller App (BPP): /confirm (payment PAID)
  Seller App (BPP)-->>Buyer App (BAP): /on_confirm (order.status ACTIVE; TICKET ACTIVE)
  rect rgb(191, 223, 255)
  Seller App (BPP)-->>Buyer App (BAP): /on_status (unsolicited): order.status ACTIVE; TICKET CHECKED_IN
  end
  Seller App (BPP)-->>Buyer App (BAP): /on_status (unsolicited): order.status COMPLETED; TICKET CHECKED_OUT
  Buyer App (BAP)->>Seller App (BPP): /issue
  Seller App (BPP)-->>Buyer App (BAP): /on_issue
  Seller App (BPP)-->>Buyer App (BAP): /on_issue_status (unsolicited)
  Buyer App (BAP)->>Seller App (BPP): /issue
```

## on_status_complete_METRO_210

```mermaid
sequenceDiagram
  participant Buyer App (BAP)
  participant Gateway
  participant Seller App (BPP)
  Buyer App (BAP)->>Seller App (BPP): /search (A to B, peer-to-peer)
  Seller App (BPP)-->>Buyer App (BAP): /on_search (items SJT, RJT)
  Buyer App (BAP)->>Seller App (BPP): /select (item I1 x 1)
  Seller App (BPP)-->>Buyer App (BAP): /on_select (quote)
  Buyer App (BAP)->>Seller App (BPP): /init (payment NOT-PAID)
  Seller App (BPP)-->>Buyer App (BAP): /on_init (payment NOT-PAID)
  Buyer App (BAP)->>Seller App (BPP): /confirm (payment PAID)
  Seller App (BPP)-->>Buyer App (BAP): /on_confirm (order.status ACTIVE; TICKET ACTIVE)
  Seller App (BPP)-->>Buyer App (BAP): /on_status (unsolicited): order.status ACTIVE; TICKET CHECKED_IN
  rect rgb(191, 223, 255)
  Seller App (BPP)-->>Buyer App (BAP): /on_status (unsolicited): order.status COMPLETED; TICKET CHECKED_OUT
  end
  Buyer App (BAP)->>Seller App (BPP): /issue
  Seller App (BPP)-->>Buyer App (BAP): /on_issue
  Seller App (BPP)-->>Buyer App (BAP): /on_issue_status (unsolicited)
  Buyer App (BAP)->>Seller App (BPP): /issue
```

## issue_open_metro_100

```mermaid
sequenceDiagram
  participant Buyer App (BAP)
  participant Gateway
  participant Seller App (BPP)
  Buyer App (BAP)->>Seller App (BPP): /search (A to B, peer-to-peer)
  Seller App (BPP)-->>Buyer App (BAP): /on_search (items SJT, RJT)
  Buyer App (BAP)->>Seller App (BPP): /select (item I1 x 1)
  Seller App (BPP)-->>Buyer App (BAP): /on_select (quote)
  Buyer App (BAP)->>Seller App (BPP): /init (payment NOT-PAID)
  Seller App (BPP)-->>Buyer App (BAP): /on_init (payment NOT-PAID)
  Buyer App (BAP)->>Seller App (BPP): /confirm (payment PAID)
  Seller App (BPP)-->>Buyer App (BAP): /on_confirm (order.status ACTIVE; TICKET ACTIVE)
  Seller App (BPP)-->>Buyer App (BAP): /on_status (unsolicited): order.status ACTIVE; TICKET CHECKED_IN
  Seller App (BPP)-->>Buyer App (BAP): /on_status (unsolicited): order.status COMPLETED; TICKET CHECKED_OUT
  rect rgb(191, 223, 255)
  Buyer App (BAP)->>Seller App (BPP): /issue
  end
  Seller App (BPP)-->>Buyer App (BAP): /on_issue
  Seller App (BPP)-->>Buyer App (BAP): /on_issue_status (unsolicited)
  Buyer App (BAP)->>Seller App (BPP): /issue
```

## on_issue_processing_metro_100

```mermaid
sequenceDiagram
  participant Buyer App (BAP)
  participant Gateway
  participant Seller App (BPP)
  Buyer App (BAP)->>Seller App (BPP): /search (A to B, peer-to-peer)
  Seller App (BPP)-->>Buyer App (BAP): /on_search (items SJT, RJT)
  Buyer App (BAP)->>Seller App (BPP): /select (item I1 x 1)
  Seller App (BPP)-->>Buyer App (BAP): /on_select (quote)
  Buyer App (BAP)->>Seller App (BPP): /init (payment NOT-PAID)
  Seller App (BPP)-->>Buyer App (BAP): /on_init (payment NOT-PAID)
  Buyer App (BAP)->>Seller App (BPP): /confirm (payment PAID)
  Seller App (BPP)-->>Buyer App (BAP): /on_confirm (order.status ACTIVE; TICKET ACTIVE)
  Seller App (BPP)-->>Buyer App (BAP): /on_status (unsolicited): order.status ACTIVE; TICKET CHECKED_IN
  Seller App (BPP)-->>Buyer App (BAP): /on_status (unsolicited): order.status COMPLETED; TICKET CHECKED_OUT
  Buyer App (BAP)->>Seller App (BPP): /issue
  rect rgb(191, 223, 255)
  Seller App (BPP)-->>Buyer App (BAP): /on_issue
  end
  Seller App (BPP)-->>Buyer App (BAP): /on_issue_status (unsolicited)
  Buyer App (BAP)->>Seller App (BPP): /issue
```

## on_issue_resolved_metro_100

```mermaid
sequenceDiagram
  participant Buyer App (BAP)
  participant Gateway
  participant Seller App (BPP)
  Buyer App (BAP)->>Seller App (BPP): /search (A to B, peer-to-peer)
  Seller App (BPP)-->>Buyer App (BAP): /on_search (items SJT, RJT)
  Buyer App (BAP)->>Seller App (BPP): /select (item I1 x 1)
  Seller App (BPP)-->>Buyer App (BAP): /on_select (quote)
  Buyer App (BAP)->>Seller App (BPP): /init (payment NOT-PAID)
  Seller App (BPP)-->>Buyer App (BAP): /on_init (payment NOT-PAID)
  Buyer App (BAP)->>Seller App (BPP): /confirm (payment PAID)
  Seller App (BPP)-->>Buyer App (BAP): /on_confirm (order.status ACTIVE; TICKET ACTIVE)
  Seller App (BPP)-->>Buyer App (BAP): /on_status (unsolicited): order.status ACTIVE; TICKET CHECKED_IN
  Seller App (BPP)-->>Buyer App (BAP): /on_status (unsolicited): order.status COMPLETED; TICKET CHECKED_OUT
  Buyer App (BAP)->>Seller App (BPP): /issue
  Seller App (BPP)-->>Buyer App (BAP): /on_issue
  rect rgb(191, 223, 255)
  Seller App (BPP)-->>Buyer App (BAP): /on_issue_status (unsolicited)
  end
  Buyer App (BAP)->>Seller App (BPP): /issue
```

## issue_close_metro_100

```mermaid
sequenceDiagram
  participant Buyer App (BAP)
  participant Gateway
  participant Seller App (BPP)
  Buyer App (BAP)->>Seller App (BPP): /search (A to B, peer-to-peer)
  Seller App (BPP)-->>Buyer App (BAP): /on_search (items SJT, RJT)
  Buyer App (BAP)->>Seller App (BPP): /select (item I1 x 1)
  Seller App (BPP)-->>Buyer App (BAP): /on_select (quote)
  Buyer App (BAP)->>Seller App (BPP): /init (payment NOT-PAID)
  Seller App (BPP)-->>Buyer App (BAP): /on_init (payment NOT-PAID)
  Buyer App (BAP)->>Seller App (BPP): /confirm (payment PAID)
  Seller App (BPP)-->>Buyer App (BAP): /on_confirm (order.status ACTIVE; TICKET ACTIVE)
  Seller App (BPP)-->>Buyer App (BAP): /on_status (unsolicited): order.status ACTIVE; TICKET CHECKED_IN
  Seller App (BPP)-->>Buyer App (BAP): /on_status (unsolicited): order.status COMPLETED; TICKET CHECKED_OUT
  Buyer App (BAP)->>Seller App (BPP): /issue
  Seller App (BPP)-->>Buyer App (BAP): /on_issue
  Seller App (BPP)-->>Buyer App (BAP): /on_issue_status (unsolicited)
  rect rgb(191, 223, 255)
  Buyer App (BAP)->>Seller App (BPP): /issue
  end
```

# IntraCity_Agent_Activation(Route Selection by Agent) — Sequence Diagrams

Internal data file consumed by the Developer Guide's "Sequence Diagram" tab (API Walkthrough).
Not meant to be shown as its own docs page — the frontend filters this slug out of the Use Case
Brief / Additional Resources / Changelog tab lists and instead looks up the section matching the
selected API call's `action_id` (the `##` heading below) to render that step's diagram.

One `## <action_id>` heading per step of `IntraCity_Agent_Activation_Route_Selection_by_Agent_.yaml` (Bus), in that flow's own step order, each followed by its Mermaid `sequenceDiagram`: the whole flow, with that call's own message(s) highlighted — same convention as the other domains' per-step sequence-diagram docs.

## select_1

```mermaid
sequenceDiagram
  participant Buyer App (BAP)
  participant Gateway
  participant Seller App (BPP)
  rect rgb(191, 223, 255)
  Buyer App (BAP)->>Seller App (BPP): /select (item I10 x None)
  end
  Seller App (BPP)-->>Buyer App (BAP): /on_select (quote)
  Buyer App (BAP)->>Seller App (BPP): /init
  Seller App (BPP)-->>Buyer App (BAP): /on_init
  Buyer App (BAP)->>Seller App (BPP): /confirm
  Seller App (BPP)-->>Buyer App (BAP): /on_confirm (order.status ACTIVE, AGENT_TICKETING ACTIVE)
```

## on_select_1

```mermaid
sequenceDiagram
  participant Buyer App (BAP)
  participant Gateway
  participant Seller App (BPP)
  Buyer App (BAP)->>Seller App (BPP): /select (item I10 x None)
  rect rgb(191, 223, 255)
  Seller App (BPP)-->>Buyer App (BAP): /on_select (quote)
  end
  Buyer App (BAP)->>Seller App (BPP): /init
  Seller App (BPP)-->>Buyer App (BAP): /on_init
  Buyer App (BAP)->>Seller App (BPP): /confirm
  Seller App (BPP)-->>Buyer App (BAP): /on_confirm (order.status ACTIVE, AGENT_TICKETING ACTIVE)
```

## init_1

```mermaid
sequenceDiagram
  participant Buyer App (BAP)
  participant Gateway
  participant Seller App (BPP)
  Buyer App (BAP)->>Seller App (BPP): /select (item I10 x None)
  Seller App (BPP)-->>Buyer App (BAP): /on_select (quote)
  rect rgb(191, 223, 255)
  Buyer App (BAP)->>Seller App (BPP): /init
  end
  Seller App (BPP)-->>Buyer App (BAP): /on_init
  Buyer App (BAP)->>Seller App (BPP): /confirm
  Seller App (BPP)-->>Buyer App (BAP): /on_confirm (order.status ACTIVE, AGENT_TICKETING ACTIVE)
```

## on_init_1

```mermaid
sequenceDiagram
  participant Buyer App (BAP)
  participant Gateway
  participant Seller App (BPP)
  Buyer App (BAP)->>Seller App (BPP): /select (item I10 x None)
  Seller App (BPP)-->>Buyer App (BAP): /on_select (quote)
  Buyer App (BAP)->>Seller App (BPP): /init
  rect rgb(191, 223, 255)
  Seller App (BPP)-->>Buyer App (BAP): /on_init
  end
  Buyer App (BAP)->>Seller App (BPP): /confirm
  Seller App (BPP)-->>Buyer App (BAP): /on_confirm (order.status ACTIVE, AGENT_TICKETING ACTIVE)
```

## confirm_1

```mermaid
sequenceDiagram
  participant Buyer App (BAP)
  participant Gateway
  participant Seller App (BPP)
  Buyer App (BAP)->>Seller App (BPP): /select (item I10 x None)
  Seller App (BPP)-->>Buyer App (BAP): /on_select (quote)
  Buyer App (BAP)->>Seller App (BPP): /init
  Seller App (BPP)-->>Buyer App (BAP): /on_init
  rect rgb(191, 223, 255)
  Buyer App (BAP)->>Seller App (BPP): /confirm
  end
  Seller App (BPP)-->>Buyer App (BAP): /on_confirm (order.status ACTIVE, AGENT_TICKETING ACTIVE)
```

## on_confirm_1

```mermaid
sequenceDiagram
  participant Buyer App (BAP)
  participant Gateway
  participant Seller App (BPP)
  Buyer App (BAP)->>Seller App (BPP): /select (item I10 x None)
  Seller App (BPP)-->>Buyer App (BAP): /on_select (quote)
  Buyer App (BAP)->>Seller App (BPP): /init
  Seller App (BPP)-->>Buyer App (BAP): /on_init
  Buyer App (BAP)->>Seller App (BPP): /confirm
  rect rgb(191, 223, 255)
  Seller App (BPP)-->>Buyer App (BAP): /on_confirm (order.status ACTIVE, AGENT_TICKETING ACTIVE)
  end
```

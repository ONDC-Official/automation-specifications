# IntraCity_Purchase_Journey_FlowCode_Based_Flow_With_IGM(v-1.0.0) — Sequence Diagrams

Internal data file consumed by the Developer Guide's "Sequence Diagram" tab (API Walkthrough).
Not meant to be shown as its own docs page — the frontend filters this slug out of the Use Case
Brief / Additional Resources / Changelog tab lists and instead looks up the section matching the
selected API call's `action_id` (the `##` heading below) to render that step's diagram.

One `## <action_id>` heading per step of `IntraCity_Purchase_Journey_FlowCode_Based_Flow_With_IGM_v-1_0_0_.yaml` (Bus), in that flow's own step order, each followed by its Mermaid `sequenceDiagram`: the whole flow, with that call's own message(s) highlighted — same convention as the other domains' per-step sequence-diagram docs.

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
  Buyer App (BAP)->>Seller App (BPP): /status (order status)
  Seller App (BPP)-->>Buyer App (BAP): /on_status (order.status COMPLETED)
  Buyer App (BAP)->>Seller App (BPP): /issue (The BAP submits an issue against the confirmed metro ticket order to trigger the ONDC Issue Grievance Management workflow, enabling formal registration and tracking of the unresolved complaint.)
  Seller App (BPP)-->>Buyer App (BAP): /on_issue (The BPP sends an on issue callback to the BAP, confirming receipt of the unresolved issue and communicating the available resolution actions to address the passenger's grievance.)
  Seller App (BPP)-->>Buyer App (BAP): /on_issue_status (unsolicited): The BPP proactively notifies the BAP of the issue status and any pending actions regarding the passenger's complaint, concluding the issue management workflow.
  Buyer App (BAP)->>Seller App (BPP): /issue (The BAP submits an issue complaint to the BPP for the metro ticket order, initiating the ONDC issue management workflow with complaint details and expected resolution timeline.)
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
  Buyer App (BAP)->>Seller App (BPP): /status (order status)
  Seller App (BPP)-->>Buyer App (BAP): /on_status (order.status COMPLETED)
  Buyer App (BAP)->>Seller App (BPP): /issue (The BAP submits an issue against the confirmed metro ticket order to trigger the ONDC Issue Grievance Management workflow, enabling formal registration and tracking of the unresolved complaint.)
  Seller App (BPP)-->>Buyer App (BAP): /on_issue (The BPP sends an on issue callback to the BAP, confirming receipt of the unresolved issue and communicating the available resolution actions to address the passenger's grievance.)
  Seller App (BPP)-->>Buyer App (BAP): /on_issue_status (unsolicited): The BPP proactively notifies the BAP of the issue status and any pending actions regarding the passenger's complaint, concluding the issue management workflow.
  Buyer App (BAP)->>Seller App (BPP): /issue (The BAP submits an issue complaint to the BPP for the metro ticket order, initiating the ONDC issue management workflow with complaint details and expected resolution timeline.)
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
  Buyer App (BAP)->>Seller App (BPP): /status (order status)
  Seller App (BPP)-->>Buyer App (BAP): /on_status (order.status COMPLETED)
  Buyer App (BAP)->>Seller App (BPP): /issue (The BAP submits an issue against the confirmed metro ticket order to trigger the ONDC Issue Grievance Management workflow, enabling formal registration and tracking of the unresolved complaint.)
  Seller App (BPP)-->>Buyer App (BAP): /on_issue (The BPP sends an on issue callback to the BAP, confirming receipt of the unresolved issue and communicating the available resolution actions to address the passenger's grievance.)
  Seller App (BPP)-->>Buyer App (BAP): /on_issue_status (unsolicited): The BPP proactively notifies the BAP of the issue status and any pending actions regarding the passenger's complaint, concluding the issue management workflow.
  Buyer App (BAP)->>Seller App (BPP): /issue (The BAP submits an issue complaint to the BPP for the metro ticket order, initiating the ONDC issue management workflow with complaint details and expected resolution timeline.)
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
  Buyer App (BAP)->>Seller App (BPP): /status (order status)
  Seller App (BPP)-->>Buyer App (BAP): /on_status (order.status COMPLETED)
  Buyer App (BAP)->>Seller App (BPP): /issue (The BAP submits an issue against the confirmed metro ticket order to trigger the ONDC Issue Grievance Management workflow, enabling formal registration and tracking of the unresolved complaint.)
  Seller App (BPP)-->>Buyer App (BAP): /on_issue (The BPP sends an on issue callback to the BAP, confirming receipt of the unresolved issue and communicating the available resolution actions to address the passenger's grievance.)
  Seller App (BPP)-->>Buyer App (BAP): /on_issue_status (unsolicited): The BPP proactively notifies the BAP of the issue status and any pending actions regarding the passenger's complaint, concluding the issue management workflow.
  Buyer App (BAP)->>Seller App (BPP): /issue (The BAP submits an issue complaint to the BPP for the metro ticket order, initiating the ONDC issue management workflow with complaint details and expected resolution timeline.)
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
  Buyer App (BAP)->>Seller App (BPP): /status (order status)
  Seller App (BPP)-->>Buyer App (BAP): /on_status (order.status COMPLETED)
  Buyer App (BAP)->>Seller App (BPP): /issue (The BAP submits an issue against the confirmed metro ticket order to trigger the ONDC Issue Grievance Management workflow, enabling formal registration and tracking of the unresolved complaint.)
  Seller App (BPP)-->>Buyer App (BAP): /on_issue (The BPP sends an on issue callback to the BAP, confirming receipt of the unresolved issue and communicating the available resolution actions to address the passenger's grievance.)
  Seller App (BPP)-->>Buyer App (BAP): /on_issue_status (unsolicited): The BPP proactively notifies the BAP of the issue status and any pending actions regarding the passenger's complaint, concluding the issue management workflow.
  Buyer App (BAP)->>Seller App (BPP): /issue (The BAP submits an issue complaint to the BPP for the metro ticket order, initiating the ONDC issue management workflow with complaint details and expected resolution timeline.)
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
  Buyer App (BAP)->>Seller App (BPP): /status (order status)
  Seller App (BPP)-->>Buyer App (BAP): /on_status (order.status COMPLETED)
  Buyer App (BAP)->>Seller App (BPP): /issue (The BAP submits an issue against the confirmed metro ticket order to trigger the ONDC Issue Grievance Management workflow, enabling formal registration and tracking of the unresolved complaint.)
  Seller App (BPP)-->>Buyer App (BAP): /on_issue (The BPP sends an on issue callback to the BAP, confirming receipt of the unresolved issue and communicating the available resolution actions to address the passenger's grievance.)
  Seller App (BPP)-->>Buyer App (BAP): /on_issue_status (unsolicited): The BPP proactively notifies the BAP of the issue status and any pending actions regarding the passenger's complaint, concluding the issue management workflow.
  Buyer App (BAP)->>Seller App (BPP): /issue (The BAP submits an issue complaint to the BPP for the metro ticket order, initiating the ONDC issue management workflow with complaint details and expected resolution timeline.)
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
  Buyer App (BAP)->>Seller App (BPP): /status (order status)
  Seller App (BPP)-->>Buyer App (BAP): /on_status (order.status COMPLETED)
  Buyer App (BAP)->>Seller App (BPP): /issue (The BAP submits an issue against the confirmed metro ticket order to trigger the ONDC Issue Grievance Management workflow, enabling formal registration and tracking of the unresolved complaint.)
  Seller App (BPP)-->>Buyer App (BAP): /on_issue (The BPP sends an on issue callback to the BAP, confirming receipt of the unresolved issue and communicating the available resolution actions to address the passenger's grievance.)
  Seller App (BPP)-->>Buyer App (BAP): /on_issue_status (unsolicited): The BPP proactively notifies the BAP of the issue status and any pending actions regarding the passenger's complaint, concluding the issue management workflow.
  Buyer App (BAP)->>Seller App (BPP): /issue (The BAP submits an issue complaint to the BPP for the metro ticket order, initiating the ONDC issue management workflow with complaint details and expected resolution timeline.)
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
  Buyer App (BAP)->>Seller App (BPP): /status (order status)
  Seller App (BPP)-->>Buyer App (BAP): /on_status (order.status COMPLETED)
  Buyer App (BAP)->>Seller App (BPP): /issue (The BAP submits an issue against the confirmed metro ticket order to trigger the ONDC Issue Grievance Management workflow, enabling formal registration and tracking of the unresolved complaint.)
  Seller App (BPP)-->>Buyer App (BAP): /on_issue (The BPP sends an on issue callback to the BAP, confirming receipt of the unresolved issue and communicating the available resolution actions to address the passenger's grievance.)
  Seller App (BPP)-->>Buyer App (BAP): /on_issue_status (unsolicited): The BPP proactively notifies the BAP of the issue status and any pending actions regarding the passenger's complaint, concluding the issue management workflow.
  Buyer App (BAP)->>Seller App (BPP): /issue (The BAP submits an issue complaint to the BPP for the metro ticket order, initiating the ONDC issue management workflow with complaint details and expected resolution timeline.)
```

## status_purchase_flow_BUS_201

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
  Buyer App (BAP)->>Seller App (BPP): /status (order status)
  end
  Seller App (BPP)-->>Buyer App (BAP): /on_status (order.status COMPLETED)
  Buyer App (BAP)->>Seller App (BPP): /issue (The BAP submits an issue against the confirmed metro ticket order to trigger the ONDC Issue Grievance Management workflow, enabling formal registration and tracking of the unresolved complaint.)
  Seller App (BPP)-->>Buyer App (BAP): /on_issue (The BPP sends an on issue callback to the BAP, confirming receipt of the unresolved issue and communicating the available resolution actions to address the passenger's grievance.)
  Seller App (BPP)-->>Buyer App (BAP): /on_issue_status (unsolicited): The BPP proactively notifies the BAP of the issue status and any pending actions regarding the passenger's complaint, concluding the issue management workflow.
  Buyer App (BAP)->>Seller App (BPP): /issue (The BAP submits an issue complaint to the BPP for the metro ticket order, initiating the ONDC issue management workflow with complaint details and expected resolution timeline.)
```

## on_status_complete_BUS_201

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
  Buyer App (BAP)->>Seller App (BPP): /status (order status)
  rect rgb(191, 223, 255)
  Seller App (BPP)-->>Buyer App (BAP): /on_status (order.status COMPLETED)
  end
  Buyer App (BAP)->>Seller App (BPP): /issue (The BAP submits an issue against the confirmed metro ticket order to trigger the ONDC Issue Grievance Management workflow, enabling formal registration and tracking of the unresolved complaint.)
  Seller App (BPP)-->>Buyer App (BAP): /on_issue (The BPP sends an on issue callback to the BAP, confirming receipt of the unresolved issue and communicating the available resolution actions to address the passenger's grievance.)
  Seller App (BPP)-->>Buyer App (BAP): /on_issue_status (unsolicited): The BPP proactively notifies the BAP of the issue status and any pending actions regarding the passenger's complaint, concluding the issue management workflow.
  Buyer App (BAP)->>Seller App (BPP): /issue (The BAP submits an issue complaint to the BPP for the metro ticket order, initiating the ONDC issue management workflow with complaint details and expected resolution timeline.)
```

## issue_open_metro_100

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
  Buyer App (BAP)->>Seller App (BPP): /status (order status)
  Seller App (BPP)-->>Buyer App (BAP): /on_status (order.status COMPLETED)
  rect rgb(191, 223, 255)
  Buyer App (BAP)->>Seller App (BPP): /issue (The BAP submits an issue against the confirmed metro ticket order to trigger the ONDC Issue Grievance Management workflow, enabling formal registration and tracking of the unresolved complaint.)
  end
  Seller App (BPP)-->>Buyer App (BAP): /on_issue (The BPP sends an on issue callback to the BAP, confirming receipt of the unresolved issue and communicating the available resolution actions to address the passenger's grievance.)
  Seller App (BPP)-->>Buyer App (BAP): /on_issue_status (unsolicited): The BPP proactively notifies the BAP of the issue status and any pending actions regarding the passenger's complaint, concluding the issue management workflow.
  Buyer App (BAP)->>Seller App (BPP): /issue (The BAP submits an issue complaint to the BPP for the metro ticket order, initiating the ONDC issue management workflow with complaint details and expected resolution timeline.)
```

## on_issue_processing_metro_100

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
  Buyer App (BAP)->>Seller App (BPP): /status (order status)
  Seller App (BPP)-->>Buyer App (BAP): /on_status (order.status COMPLETED)
  Buyer App (BAP)->>Seller App (BPP): /issue (The BAP submits an issue against the confirmed metro ticket order to trigger the ONDC Issue Grievance Management workflow, enabling formal registration and tracking of the unresolved complaint.)
  rect rgb(191, 223, 255)
  Seller App (BPP)-->>Buyer App (BAP): /on_issue (The BPP sends an on issue callback to the BAP, confirming receipt of the unresolved issue and communicating the available resolution actions to address the passenger's grievance.)
  end
  Seller App (BPP)-->>Buyer App (BAP): /on_issue_status (unsolicited): The BPP proactively notifies the BAP of the issue status and any pending actions regarding the passenger's complaint, concluding the issue management workflow.
  Buyer App (BAP)->>Seller App (BPP): /issue (The BAP submits an issue complaint to the BPP for the metro ticket order, initiating the ONDC issue management workflow with complaint details and expected resolution timeline.)
```

## on_issue_resolved_metro_100

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
  Buyer App (BAP)->>Seller App (BPP): /status (order status)
  Seller App (BPP)-->>Buyer App (BAP): /on_status (order.status COMPLETED)
  Buyer App (BAP)->>Seller App (BPP): /issue (The BAP submits an issue against the confirmed metro ticket order to trigger the ONDC Issue Grievance Management workflow, enabling formal registration and tracking of the unresolved complaint.)
  Seller App (BPP)-->>Buyer App (BAP): /on_issue (The BPP sends an on issue callback to the BAP, confirming receipt of the unresolved issue and communicating the available resolution actions to address the passenger's grievance.)
  rect rgb(191, 223, 255)
  Seller App (BPP)-->>Buyer App (BAP): /on_issue_status (unsolicited): The BPP proactively notifies the BAP of the issue status and any pending actions regarding the passenger's complaint, concluding the issue management workflow.
  end
  Buyer App (BAP)->>Seller App (BPP): /issue (The BAP submits an issue complaint to the BPP for the metro ticket order, initiating the ONDC issue management workflow with complaint details and expected resolution timeline.)
```

## issue_close_metro_100

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
  Buyer App (BAP)->>Seller App (BPP): /status (order status)
  Seller App (BPP)-->>Buyer App (BAP): /on_status (order.status COMPLETED)
  Buyer App (BAP)->>Seller App (BPP): /issue (The BAP submits an issue against the confirmed metro ticket order to trigger the ONDC Issue Grievance Management workflow, enabling formal registration and tracking of the unresolved complaint.)
  Seller App (BPP)-->>Buyer App (BAP): /on_issue (The BPP sends an on issue callback to the BAP, confirming receipt of the unresolved issue and communicating the available resolution actions to address the passenger's grievance.)
  Seller App (BPP)-->>Buyer App (BAP): /on_issue_status (unsolicited): The BPP proactively notifies the BAP of the issue status and any pending actions regarding the passenger's complaint, concluding the issue management workflow.
  rect rgb(191, 223, 255)
  Buyer App (BAP)->>Seller App (BPP): /issue (The BAP submits an issue complaint to the BPP for the metro ticket order, initiating the ONDC issue management workflow with complaint details and expected resolution timeline.)
  end
```

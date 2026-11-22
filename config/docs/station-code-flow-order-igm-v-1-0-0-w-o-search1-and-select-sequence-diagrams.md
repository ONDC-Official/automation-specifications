# STATION_CODE_FLOW_ORDER_IGM_(v-1.0.0)(W/O Search1 and Select) — Sequence Diagrams

Internal data file consumed by the Developer Guide's "Sequence Diagram" tab (API Walkthrough).
Not meant to be shown as its own docs page — the frontend filters this slug out of the Use Case
Brief / Additional Resources / Changelog tab lists and instead looks up the section matching the
selected API call's `action_id` (the `##` heading below) to render that step's diagram.

One `## <action_id>` heading per step of `STATION_CODE_FLOW_ORDER_IGM_v-1_0_0__W_O_Search_and_Select_.yaml` (Metro), in that flow's own step order, each followed by its Mermaid `sequenceDiagram`: the whole flow, with that call's own message(s) highlighted — same convention as the other domains' per-step sequence-diagram docs.

## search2_METRO_201

```mermaid
sequenceDiagram
  participant Buyer App (BAP)
  participant Gateway
  participant Seller App (BPP)
  rect rgb(191, 223, 255)
  Buyer App (BAP)->>Seller App (BPP): /search (A to B, peer-to-peer)
  end
  Seller App (BPP)-->>Buyer App (BAP): /on_search (catalog)
  Buyer App (BAP)->>Seller App (BPP): /init (payment NOT-PAID)
  Seller App (BPP)-->>Buyer App (BAP): /on_init (payment NOT-PAID)
  Buyer App (BAP)->>Seller App (BPP): /confirm (payment PAID)
  Seller App (BPP)-->>Buyer App (BAP): /on_confirm (order.status None)
  Buyer App (BAP)->>Seller App (BPP): /status (order status)
  Seller App (BPP)-->>Buyer App (BAP): /on_status (order.status COMPLETED)
  Buyer App (BAP)->>Seller App (BPP): /issue (The BAP submits an issue against the confirmed metro ticket order to trigger the ONDC Issue Grievance Management workflow, enabling formal registration and tracking of the unresolved complaint.)
  Seller App (BPP)-->>Buyer App (BAP): /on_issue (The BPP sends an on issue callback to the BAP, confirming receipt of the unresolved issue and communicating the available resolution actions to address the passenger's grievance.)
  Seller App (BPP)-->>Buyer App (BAP): /on_issue_status (unsolicited): The BPP proactively notifies the BAP of the issue status and any pending actions regarding the passenger's complaint, concluding the issue management workflow.
  Buyer App (BAP)->>Seller App (BPP): /issue (The BAP submits an issue complaint to the BPP for the metro ticket order, initiating the ONDC issue management workflow with complaint details and expected resolution timeline.)
```

## on_search2_METRO_201

```mermaid
sequenceDiagram
  participant Buyer App (BAP)
  participant Gateway
  participant Seller App (BPP)
  Buyer App (BAP)->>Seller App (BPP): /search (A to B, peer-to-peer)
  rect rgb(191, 223, 255)
  Seller App (BPP)-->>Buyer App (BAP): /on_search (catalog)
  end
  Buyer App (BAP)->>Seller App (BPP): /init (payment NOT-PAID)
  Seller App (BPP)-->>Buyer App (BAP): /on_init (payment NOT-PAID)
  Buyer App (BAP)->>Seller App (BPP): /confirm (payment PAID)
  Seller App (BPP)-->>Buyer App (BAP): /on_confirm (order.status None)
  Buyer App (BAP)->>Seller App (BPP): /status (order status)
  Seller App (BPP)-->>Buyer App (BAP): /on_status (order.status COMPLETED)
  Buyer App (BAP)->>Seller App (BPP): /issue (The BAP submits an issue against the confirmed metro ticket order to trigger the ONDC Issue Grievance Management workflow, enabling formal registration and tracking of the unresolved complaint.)
  Seller App (BPP)-->>Buyer App (BAP): /on_issue (The BPP sends an on issue callback to the BAP, confirming receipt of the unresolved issue and communicating the available resolution actions to address the passenger's grievance.)
  Seller App (BPP)-->>Buyer App (BAP): /on_issue_status (unsolicited): The BPP proactively notifies the BAP of the issue status and any pending actions regarding the passenger's complaint, concluding the issue management workflow.
  Buyer App (BAP)->>Seller App (BPP): /issue (The BAP submits an issue complaint to the BPP for the metro ticket order, initiating the ONDC issue management workflow with complaint details and expected resolution timeline.)
```

## init_without_select_METRO_201

```mermaid
sequenceDiagram
  participant Buyer App (BAP)
  participant Gateway
  participant Seller App (BPP)
  Buyer App (BAP)->>Seller App (BPP): /search (A to B, peer-to-peer)
  Seller App (BPP)-->>Buyer App (BAP): /on_search (catalog)
  rect rgb(191, 223, 255)
  Buyer App (BAP)->>Seller App (BPP): /init (payment NOT-PAID)
  end
  Seller App (BPP)-->>Buyer App (BAP): /on_init (payment NOT-PAID)
  Buyer App (BAP)->>Seller App (BPP): /confirm (payment PAID)
  Seller App (BPP)-->>Buyer App (BAP): /on_confirm (order.status None)
  Buyer App (BAP)->>Seller App (BPP): /status (order status)
  Seller App (BPP)-->>Buyer App (BAP): /on_status (order.status COMPLETED)
  Buyer App (BAP)->>Seller App (BPP): /issue (The BAP submits an issue against the confirmed metro ticket order to trigger the ONDC Issue Grievance Management workflow, enabling formal registration and tracking of the unresolved complaint.)
  Seller App (BPP)-->>Buyer App (BAP): /on_issue (The BPP sends an on issue callback to the BAP, confirming receipt of the unresolved issue and communicating the available resolution actions to address the passenger's grievance.)
  Seller App (BPP)-->>Buyer App (BAP): /on_issue_status (unsolicited): The BPP proactively notifies the BAP of the issue status and any pending actions regarding the passenger's complaint, concluding the issue management workflow.
  Buyer App (BAP)->>Seller App (BPP): /issue (The BAP submits an issue complaint to the BPP for the metro ticket order, initiating the ONDC issue management workflow with complaint details and expected resolution timeline.)
```

## on_init_without_select_METRO_201

```mermaid
sequenceDiagram
  participant Buyer App (BAP)
  participant Gateway
  participant Seller App (BPP)
  Buyer App (BAP)->>Seller App (BPP): /search (A to B, peer-to-peer)
  Seller App (BPP)-->>Buyer App (BAP): /on_search (catalog)
  Buyer App (BAP)->>Seller App (BPP): /init (payment NOT-PAID)
  rect rgb(191, 223, 255)
  Seller App (BPP)-->>Buyer App (BAP): /on_init (payment NOT-PAID)
  end
  Buyer App (BAP)->>Seller App (BPP): /confirm (payment PAID)
  Seller App (BPP)-->>Buyer App (BAP): /on_confirm (order.status None)
  Buyer App (BAP)->>Seller App (BPP): /status (order status)
  Seller App (BPP)-->>Buyer App (BAP): /on_status (order.status COMPLETED)
  Buyer App (BAP)->>Seller App (BPP): /issue (The BAP submits an issue against the confirmed metro ticket order to trigger the ONDC Issue Grievance Management workflow, enabling formal registration and tracking of the unresolved complaint.)
  Seller App (BPP)-->>Buyer App (BAP): /on_issue (The BPP sends an on issue callback to the BAP, confirming receipt of the unresolved issue and communicating the available resolution actions to address the passenger's grievance.)
  Seller App (BPP)-->>Buyer App (BAP): /on_issue_status (unsolicited): The BPP proactively notifies the BAP of the issue status and any pending actions regarding the passenger's complaint, concluding the issue management workflow.
  Buyer App (BAP)->>Seller App (BPP): /issue (The BAP submits an issue complaint to the BPP for the metro ticket order, initiating the ONDC issue management workflow with complaint details and expected resolution timeline.)
```

## confirm_METRO_201

```mermaid
sequenceDiagram
  participant Buyer App (BAP)
  participant Gateway
  participant Seller App (BPP)
  Buyer App (BAP)->>Seller App (BPP): /search (A to B, peer-to-peer)
  Seller App (BPP)-->>Buyer App (BAP): /on_search (catalog)
  Buyer App (BAP)->>Seller App (BPP): /init (payment NOT-PAID)
  Seller App (BPP)-->>Buyer App (BAP): /on_init (payment NOT-PAID)
  rect rgb(191, 223, 255)
  Buyer App (BAP)->>Seller App (BPP): /confirm (payment PAID)
  end
  Seller App (BPP)-->>Buyer App (BAP): /on_confirm (order.status None)
  Buyer App (BAP)->>Seller App (BPP): /status (order status)
  Seller App (BPP)-->>Buyer App (BAP): /on_status (order.status COMPLETED)
  Buyer App (BAP)->>Seller App (BPP): /issue (The BAP submits an issue against the confirmed metro ticket order to trigger the ONDC Issue Grievance Management workflow, enabling formal registration and tracking of the unresolved complaint.)
  Seller App (BPP)-->>Buyer App (BAP): /on_issue (The BPP sends an on issue callback to the BAP, confirming receipt of the unresolved issue and communicating the available resolution actions to address the passenger's grievance.)
  Seller App (BPP)-->>Buyer App (BAP): /on_issue_status (unsolicited): The BPP proactively notifies the BAP of the issue status and any pending actions regarding the passenger's complaint, concluding the issue management workflow.
  Buyer App (BAP)->>Seller App (BPP): /issue (The BAP submits an issue complaint to the BPP for the metro ticket order, initiating the ONDC issue management workflow with complaint details and expected resolution timeline.)
```

## on_confirm_METRO_201

```mermaid
sequenceDiagram
  participant Buyer App (BAP)
  participant Gateway
  participant Seller App (BPP)
  Buyer App (BAP)->>Seller App (BPP): /search (A to B, peer-to-peer)
  Seller App (BPP)-->>Buyer App (BAP): /on_search (catalog)
  Buyer App (BAP)->>Seller App (BPP): /init (payment NOT-PAID)
  Seller App (BPP)-->>Buyer App (BAP): /on_init (payment NOT-PAID)
  Buyer App (BAP)->>Seller App (BPP): /confirm (payment PAID)
  rect rgb(191, 223, 255)
  Seller App (BPP)-->>Buyer App (BAP): /on_confirm (order.status None)
  end
  Buyer App (BAP)->>Seller App (BPP): /status (order status)
  Seller App (BPP)-->>Buyer App (BAP): /on_status (order.status COMPLETED)
  Buyer App (BAP)->>Seller App (BPP): /issue (The BAP submits an issue against the confirmed metro ticket order to trigger the ONDC Issue Grievance Management workflow, enabling formal registration and tracking of the unresolved complaint.)
  Seller App (BPP)-->>Buyer App (BAP): /on_issue (The BPP sends an on issue callback to the BAP, confirming receipt of the unresolved issue and communicating the available resolution actions to address the passenger's grievance.)
  Seller App (BPP)-->>Buyer App (BAP): /on_issue_status (unsolicited): The BPP proactively notifies the BAP of the issue status and any pending actions regarding the passenger's complaint, concluding the issue management workflow.
  Buyer App (BAP)->>Seller App (BPP): /issue (The BAP submits an issue complaint to the BPP for the metro ticket order, initiating the ONDC issue management workflow with complaint details and expected resolution timeline.)
```

## status_METRO_201

```mermaid
sequenceDiagram
  participant Buyer App (BAP)
  participant Gateway
  participant Seller App (BPP)
  Buyer App (BAP)->>Seller App (BPP): /search (A to B, peer-to-peer)
  Seller App (BPP)-->>Buyer App (BAP): /on_search (catalog)
  Buyer App (BAP)->>Seller App (BPP): /init (payment NOT-PAID)
  Seller App (BPP)-->>Buyer App (BAP): /on_init (payment NOT-PAID)
  Buyer App (BAP)->>Seller App (BPP): /confirm (payment PAID)
  Seller App (BPP)-->>Buyer App (BAP): /on_confirm (order.status None)
  rect rgb(191, 223, 255)
  Buyer App (BAP)->>Seller App (BPP): /status (order status)
  end
  Seller App (BPP)-->>Buyer App (BAP): /on_status (order.status COMPLETED)
  Buyer App (BAP)->>Seller App (BPP): /issue (The BAP submits an issue against the confirmed metro ticket order to trigger the ONDC Issue Grievance Management workflow, enabling formal registration and tracking of the unresolved complaint.)
  Seller App (BPP)-->>Buyer App (BAP): /on_issue (The BPP sends an on issue callback to the BAP, confirming receipt of the unresolved issue and communicating the available resolution actions to address the passenger's grievance.)
  Seller App (BPP)-->>Buyer App (BAP): /on_issue_status (unsolicited): The BPP proactively notifies the BAP of the issue status and any pending actions regarding the passenger's complaint, concluding the issue management workflow.
  Buyer App (BAP)->>Seller App (BPP): /issue (The BAP submits an issue complaint to the BPP for the metro ticket order, initiating the ONDC issue management workflow with complaint details and expected resolution timeline.)
```

## on_status_complete_METRO_201

```mermaid
sequenceDiagram
  participant Buyer App (BAP)
  participant Gateway
  participant Seller App (BPP)
  Buyer App (BAP)->>Seller App (BPP): /search (A to B, peer-to-peer)
  Seller App (BPP)-->>Buyer App (BAP): /on_search (catalog)
  Buyer App (BAP)->>Seller App (BPP): /init (payment NOT-PAID)
  Seller App (BPP)-->>Buyer App (BAP): /on_init (payment NOT-PAID)
  Buyer App (BAP)->>Seller App (BPP): /confirm (payment PAID)
  Seller App (BPP)-->>Buyer App (BAP): /on_confirm (order.status None)
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
  Seller App (BPP)-->>Buyer App (BAP): /on_search (catalog)
  Buyer App (BAP)->>Seller App (BPP): /init (payment NOT-PAID)
  Seller App (BPP)-->>Buyer App (BAP): /on_init (payment NOT-PAID)
  Buyer App (BAP)->>Seller App (BPP): /confirm (payment PAID)
  Seller App (BPP)-->>Buyer App (BAP): /on_confirm (order.status None)
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
  Seller App (BPP)-->>Buyer App (BAP): /on_search (catalog)
  Buyer App (BAP)->>Seller App (BPP): /init (payment NOT-PAID)
  Seller App (BPP)-->>Buyer App (BAP): /on_init (payment NOT-PAID)
  Buyer App (BAP)->>Seller App (BPP): /confirm (payment PAID)
  Seller App (BPP)-->>Buyer App (BAP): /on_confirm (order.status None)
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
  Seller App (BPP)-->>Buyer App (BAP): /on_search (catalog)
  Buyer App (BAP)->>Seller App (BPP): /init (payment NOT-PAID)
  Seller App (BPP)-->>Buyer App (BAP): /on_init (payment NOT-PAID)
  Buyer App (BAP)->>Seller App (BPP): /confirm (payment PAID)
  Seller App (BPP)-->>Buyer App (BAP): /on_confirm (order.status None)
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
  Seller App (BPP)-->>Buyer App (BAP): /on_search (catalog)
  Buyer App (BAP)->>Seller App (BPP): /init (payment NOT-PAID)
  Seller App (BPP)-->>Buyer App (BAP): /on_init (payment NOT-PAID)
  Buyer App (BAP)->>Seller App (BPP): /confirm (payment PAID)
  Seller App (BPP)-->>Buyer App (BAP): /on_confirm (order.status None)
  Buyer App (BAP)->>Seller App (BPP): /status (order status)
  Seller App (BPP)-->>Buyer App (BAP): /on_status (order.status COMPLETED)
  Buyer App (BAP)->>Seller App (BPP): /issue (The BAP submits an issue against the confirmed metro ticket order to trigger the ONDC Issue Grievance Management workflow, enabling formal registration and tracking of the unresolved complaint.)
  Seller App (BPP)-->>Buyer App (BAP): /on_issue (The BPP sends an on issue callback to the BAP, confirming receipt of the unresolved issue and communicating the available resolution actions to address the passenger's grievance.)
  Seller App (BPP)-->>Buyer App (BAP): /on_issue_status (unsolicited): The BPP proactively notifies the BAP of the issue status and any pending actions regarding the passenger's complaint, concluding the issue management workflow.
  rect rgb(191, 223, 255)
  Buyer App (BAP)->>Seller App (BPP): /issue (The BAP submits an issue complaint to the BPP for the metro ticket order, initiating the ONDC issue management workflow with complaint details and expected resolution timeline.)
  end
```

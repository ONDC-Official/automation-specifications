# Schedule_Trip_With_IGM_v-1.0.0_With_Seller_Cancellation — Sequence Diagrams

Internal data file consumed by the Developer Guide's "Sequence Diagram" tab (API Walkthrough).
Not meant to be shown as its own docs page — the frontend filters this slug out of the Use Case
Brief / Additional Resources / Changelog tab lists and instead looks up the section matching the
selected API call's `action_id` (the `##` heading below) to render that step's diagram.

One `## <action_id>` heading per step of `Schedule_Trip_With_IGM_v-1.0.0_With_Seller_Cancellation.yaml` (Ride-hailing), in that flow's own step order, each followed by its Mermaid `sequenceDiagram`: the whole flow, with that call's own message(s) highlighted — same convention as the other domains' per-step sequence-diagram docs.

## search_schedule_trip

```mermaid
sequenceDiagram
  participant Buyer App (BAP)
  participant Gateway
  participant Seller App (BPP)
  rect rgb(191, 223, 255)
  Buyer App (BAP)->>Gateway: /search (stops START, END)
  Gateway->>Seller App (BPP): /search (forwarded)
  end
  Seller App (BPP)-->>Buyer App (BAP): /on_search (catalog)
  Buyer App (BAP)->>Seller App (BPP): /select
  Seller App (BPP)-->>Buyer App (BAP): /on_select (quote)
  Buyer App (BAP)->>Seller App (BPP): /init (payment ON_FULFILLMENT NOT_PAID, collected_by BPP)
  Seller App (BPP)-->>Buyer App (BAP): /on_init (payment ON_FULFILLMENT NOT_PAID, collected_by BPP)
  Buyer App (BAP)->>Seller App (BPP): /confirm (payment ON_FULFILLMENT NOT_PAID, collected_by BPP)
  Seller App (BPP)-->>Buyer App (BAP): /on_confirm (order.status ACTIVE; fulfillment state RIDE_CONFIRMED)
  Seller App (BPP)-->>Buyer App (BAP): /on_update (unsolicited): order.status ACTIVE; fulfillment state RIDE_ASSIGNED
  Buyer App (BAP)->>Seller App (BPP): /issue (The BAP submits an issue to the BPP to report a complaint or problem with the order, establishing the issue for tracking and resolution.)
  Seller App (BPP)-->>Buyer App (BAP): /on_issue (The BPP responds to a grievance opened by the BAP with the issue details, available actions, and resolution options.)
  Seller App (BPP)-->>Buyer App (BAP): /on_issue_status (unsolicited): The BPP sends an unsolicited issue status callback to the BAP with grievance resolution actions and status updates for the ride transaction.
  Buyer App (BAP)->>Seller App (BPP): /issue (The BAP reports an issue to the BPP regarding the confirmed ride order, creating a formal grievance record with problem details, expected response timelines, and resolution expectations.)
  Seller App (BPP)-->>Buyer App (BAP): /on_cancel (unsolicited): order.status CANCELLED; fulfillment state RIDE_CANCELLED, cancelled_by PROVIDER
```

## on_search_schedule_trip

```mermaid
sequenceDiagram
  participant Buyer App (BAP)
  participant Gateway
  participant Seller App (BPP)
  Buyer App (BAP)->>Gateway: /search (stops START, END)
  Gateway->>Seller App (BPP): /search (forwarded)
  rect rgb(191, 223, 255)
  Seller App (BPP)-->>Buyer App (BAP): /on_search (catalog)
  end
  Buyer App (BAP)->>Seller App (BPP): /select
  Seller App (BPP)-->>Buyer App (BAP): /on_select (quote)
  Buyer App (BAP)->>Seller App (BPP): /init (payment ON_FULFILLMENT NOT_PAID, collected_by BPP)
  Seller App (BPP)-->>Buyer App (BAP): /on_init (payment ON_FULFILLMENT NOT_PAID, collected_by BPP)
  Buyer App (BAP)->>Seller App (BPP): /confirm (payment ON_FULFILLMENT NOT_PAID, collected_by BPP)
  Seller App (BPP)-->>Buyer App (BAP): /on_confirm (order.status ACTIVE; fulfillment state RIDE_CONFIRMED)
  Seller App (BPP)-->>Buyer App (BAP): /on_update (unsolicited): order.status ACTIVE; fulfillment state RIDE_ASSIGNED
  Buyer App (BAP)->>Seller App (BPP): /issue (The BAP submits an issue to the BPP to report a complaint or problem with the order, establishing the issue for tracking and resolution.)
  Seller App (BPP)-->>Buyer App (BAP): /on_issue (The BPP responds to a grievance opened by the BAP with the issue details, available actions, and resolution options.)
  Seller App (BPP)-->>Buyer App (BAP): /on_issue_status (unsolicited): The BPP sends an unsolicited issue status callback to the BAP with grievance resolution actions and status updates for the ride transaction.
  Buyer App (BAP)->>Seller App (BPP): /issue (The BAP reports an issue to the BPP regarding the confirmed ride order, creating a formal grievance record with problem details, expected response timelines, and resolution expectations.)
  Seller App (BPP)-->>Buyer App (BAP): /on_cancel (unsolicited): order.status CANCELLED; fulfillment state RIDE_CANCELLED, cancelled_by PROVIDER
```

## select

```mermaid
sequenceDiagram
  participant Buyer App (BAP)
  participant Gateway
  participant Seller App (BPP)
  Buyer App (BAP)->>Gateway: /search (stops START, END)
  Gateway->>Seller App (BPP): /search (forwarded)
  Seller App (BPP)-->>Buyer App (BAP): /on_search (catalog)
  rect rgb(191, 223, 255)
  Buyer App (BAP)->>Seller App (BPP): /select
  end
  Seller App (BPP)-->>Buyer App (BAP): /on_select (quote)
  Buyer App (BAP)->>Seller App (BPP): /init (payment ON_FULFILLMENT NOT_PAID, collected_by BPP)
  Seller App (BPP)-->>Buyer App (BAP): /on_init (payment ON_FULFILLMENT NOT_PAID, collected_by BPP)
  Buyer App (BAP)->>Seller App (BPP): /confirm (payment ON_FULFILLMENT NOT_PAID, collected_by BPP)
  Seller App (BPP)-->>Buyer App (BAP): /on_confirm (order.status ACTIVE; fulfillment state RIDE_CONFIRMED)
  Seller App (BPP)-->>Buyer App (BAP): /on_update (unsolicited): order.status ACTIVE; fulfillment state RIDE_ASSIGNED
  Buyer App (BAP)->>Seller App (BPP): /issue (The BAP submits an issue to the BPP to report a complaint or problem with the order, establishing the issue for tracking and resolution.)
  Seller App (BPP)-->>Buyer App (BAP): /on_issue (The BPP responds to a grievance opened by the BAP with the issue details, available actions, and resolution options.)
  Seller App (BPP)-->>Buyer App (BAP): /on_issue_status (unsolicited): The BPP sends an unsolicited issue status callback to the BAP with grievance resolution actions and status updates for the ride transaction.
  Buyer App (BAP)->>Seller App (BPP): /issue (The BAP reports an issue to the BPP regarding the confirmed ride order, creating a formal grievance record with problem details, expected response timelines, and resolution expectations.)
  Seller App (BPP)-->>Buyer App (BAP): /on_cancel (unsolicited): order.status CANCELLED; fulfillment state RIDE_CANCELLED, cancelled_by PROVIDER
```

## on_select

```mermaid
sequenceDiagram
  participant Buyer App (BAP)
  participant Gateway
  participant Seller App (BPP)
  Buyer App (BAP)->>Gateway: /search (stops START, END)
  Gateway->>Seller App (BPP): /search (forwarded)
  Seller App (BPP)-->>Buyer App (BAP): /on_search (catalog)
  Buyer App (BAP)->>Seller App (BPP): /select
  rect rgb(191, 223, 255)
  Seller App (BPP)-->>Buyer App (BAP): /on_select (quote)
  end
  Buyer App (BAP)->>Seller App (BPP): /init (payment ON_FULFILLMENT NOT_PAID, collected_by BPP)
  Seller App (BPP)-->>Buyer App (BAP): /on_init (payment ON_FULFILLMENT NOT_PAID, collected_by BPP)
  Buyer App (BAP)->>Seller App (BPP): /confirm (payment ON_FULFILLMENT NOT_PAID, collected_by BPP)
  Seller App (BPP)-->>Buyer App (BAP): /on_confirm (order.status ACTIVE; fulfillment state RIDE_CONFIRMED)
  Seller App (BPP)-->>Buyer App (BAP): /on_update (unsolicited): order.status ACTIVE; fulfillment state RIDE_ASSIGNED
  Buyer App (BAP)->>Seller App (BPP): /issue (The BAP submits an issue to the BPP to report a complaint or problem with the order, establishing the issue for tracking and resolution.)
  Seller App (BPP)-->>Buyer App (BAP): /on_issue (The BPP responds to a grievance opened by the BAP with the issue details, available actions, and resolution options.)
  Seller App (BPP)-->>Buyer App (BAP): /on_issue_status (unsolicited): The BPP sends an unsolicited issue status callback to the BAP with grievance resolution actions and status updates for the ride transaction.
  Buyer App (BAP)->>Seller App (BPP): /issue (The BAP reports an issue to the BPP regarding the confirmed ride order, creating a formal grievance record with problem details, expected response timelines, and resolution expectations.)
  Seller App (BPP)-->>Buyer App (BAP): /on_cancel (unsolicited): order.status CANCELLED; fulfillment state RIDE_CANCELLED, cancelled_by PROVIDER
```

## init

```mermaid
sequenceDiagram
  participant Buyer App (BAP)
  participant Gateway
  participant Seller App (BPP)
  Buyer App (BAP)->>Gateway: /search (stops START, END)
  Gateway->>Seller App (BPP): /search (forwarded)
  Seller App (BPP)-->>Buyer App (BAP): /on_search (catalog)
  Buyer App (BAP)->>Seller App (BPP): /select
  Seller App (BPP)-->>Buyer App (BAP): /on_select (quote)
  rect rgb(191, 223, 255)
  Buyer App (BAP)->>Seller App (BPP): /init (payment ON_FULFILLMENT NOT_PAID, collected_by BPP)
  end
  Seller App (BPP)-->>Buyer App (BAP): /on_init (payment ON_FULFILLMENT NOT_PAID, collected_by BPP)
  Buyer App (BAP)->>Seller App (BPP): /confirm (payment ON_FULFILLMENT NOT_PAID, collected_by BPP)
  Seller App (BPP)-->>Buyer App (BAP): /on_confirm (order.status ACTIVE; fulfillment state RIDE_CONFIRMED)
  Seller App (BPP)-->>Buyer App (BAP): /on_update (unsolicited): order.status ACTIVE; fulfillment state RIDE_ASSIGNED
  Buyer App (BAP)->>Seller App (BPP): /issue (The BAP submits an issue to the BPP to report a complaint or problem with the order, establishing the issue for tracking and resolution.)
  Seller App (BPP)-->>Buyer App (BAP): /on_issue (The BPP responds to a grievance opened by the BAP with the issue details, available actions, and resolution options.)
  Seller App (BPP)-->>Buyer App (BAP): /on_issue_status (unsolicited): The BPP sends an unsolicited issue status callback to the BAP with grievance resolution actions and status updates for the ride transaction.
  Buyer App (BAP)->>Seller App (BPP): /issue (The BAP reports an issue to the BPP regarding the confirmed ride order, creating a formal grievance record with problem details, expected response timelines, and resolution expectations.)
  Seller App (BPP)-->>Buyer App (BAP): /on_cancel (unsolicited): order.status CANCELLED; fulfillment state RIDE_CANCELLED, cancelled_by PROVIDER
```

## on_init

```mermaid
sequenceDiagram
  participant Buyer App (BAP)
  participant Gateway
  participant Seller App (BPP)
  Buyer App (BAP)->>Gateway: /search (stops START, END)
  Gateway->>Seller App (BPP): /search (forwarded)
  Seller App (BPP)-->>Buyer App (BAP): /on_search (catalog)
  Buyer App (BAP)->>Seller App (BPP): /select
  Seller App (BPP)-->>Buyer App (BAP): /on_select (quote)
  Buyer App (BAP)->>Seller App (BPP): /init (payment ON_FULFILLMENT NOT_PAID, collected_by BPP)
  rect rgb(191, 223, 255)
  Seller App (BPP)-->>Buyer App (BAP): /on_init (payment ON_FULFILLMENT NOT_PAID, collected_by BPP)
  end
  Buyer App (BAP)->>Seller App (BPP): /confirm (payment ON_FULFILLMENT NOT_PAID, collected_by BPP)
  Seller App (BPP)-->>Buyer App (BAP): /on_confirm (order.status ACTIVE; fulfillment state RIDE_CONFIRMED)
  Seller App (BPP)-->>Buyer App (BAP): /on_update (unsolicited): order.status ACTIVE; fulfillment state RIDE_ASSIGNED
  Buyer App (BAP)->>Seller App (BPP): /issue (The BAP submits an issue to the BPP to report a complaint or problem with the order, establishing the issue for tracking and resolution.)
  Seller App (BPP)-->>Buyer App (BAP): /on_issue (The BPP responds to a grievance opened by the BAP with the issue details, available actions, and resolution options.)
  Seller App (BPP)-->>Buyer App (BAP): /on_issue_status (unsolicited): The BPP sends an unsolicited issue status callback to the BAP with grievance resolution actions and status updates for the ride transaction.
  Buyer App (BAP)->>Seller App (BPP): /issue (The BAP reports an issue to the BPP regarding the confirmed ride order, creating a formal grievance record with problem details, expected response timelines, and resolution expectations.)
  Seller App (BPP)-->>Buyer App (BAP): /on_cancel (unsolicited): order.status CANCELLED; fulfillment state RIDE_CANCELLED, cancelled_by PROVIDER
```

## confirm

```mermaid
sequenceDiagram
  participant Buyer App (BAP)
  participant Gateway
  participant Seller App (BPP)
  Buyer App (BAP)->>Gateway: /search (stops START, END)
  Gateway->>Seller App (BPP): /search (forwarded)
  Seller App (BPP)-->>Buyer App (BAP): /on_search (catalog)
  Buyer App (BAP)->>Seller App (BPP): /select
  Seller App (BPP)-->>Buyer App (BAP): /on_select (quote)
  Buyer App (BAP)->>Seller App (BPP): /init (payment ON_FULFILLMENT NOT_PAID, collected_by BPP)
  Seller App (BPP)-->>Buyer App (BAP): /on_init (payment ON_FULFILLMENT NOT_PAID, collected_by BPP)
  rect rgb(191, 223, 255)
  Buyer App (BAP)->>Seller App (BPP): /confirm (payment ON_FULFILLMENT NOT_PAID, collected_by BPP)
  end
  Seller App (BPP)-->>Buyer App (BAP): /on_confirm (order.status ACTIVE; fulfillment state RIDE_CONFIRMED)
  Seller App (BPP)-->>Buyer App (BAP): /on_update (unsolicited): order.status ACTIVE; fulfillment state RIDE_ASSIGNED
  Buyer App (BAP)->>Seller App (BPP): /issue (The BAP submits an issue to the BPP to report a complaint or problem with the order, establishing the issue for tracking and resolution.)
  Seller App (BPP)-->>Buyer App (BAP): /on_issue (The BPP responds to a grievance opened by the BAP with the issue details, available actions, and resolution options.)
  Seller App (BPP)-->>Buyer App (BAP): /on_issue_status (unsolicited): The BPP sends an unsolicited issue status callback to the BAP with grievance resolution actions and status updates for the ride transaction.
  Buyer App (BAP)->>Seller App (BPP): /issue (The BAP reports an issue to the BPP regarding the confirmed ride order, creating a formal grievance record with problem details, expected response timelines, and resolution expectations.)
  Seller App (BPP)-->>Buyer App (BAP): /on_cancel (unsolicited): order.status CANCELLED; fulfillment state RIDE_CANCELLED, cancelled_by PROVIDER
```

## on_confirm_rental

```mermaid
sequenceDiagram
  participant Buyer App (BAP)
  participant Gateway
  participant Seller App (BPP)
  Buyer App (BAP)->>Gateway: /search (stops START, END)
  Gateway->>Seller App (BPP): /search (forwarded)
  Seller App (BPP)-->>Buyer App (BAP): /on_search (catalog)
  Buyer App (BAP)->>Seller App (BPP): /select
  Seller App (BPP)-->>Buyer App (BAP): /on_select (quote)
  Buyer App (BAP)->>Seller App (BPP): /init (payment ON_FULFILLMENT NOT_PAID, collected_by BPP)
  Seller App (BPP)-->>Buyer App (BAP): /on_init (payment ON_FULFILLMENT NOT_PAID, collected_by BPP)
  Buyer App (BAP)->>Seller App (BPP): /confirm (payment ON_FULFILLMENT NOT_PAID, collected_by BPP)
  rect rgb(191, 223, 255)
  Seller App (BPP)-->>Buyer App (BAP): /on_confirm (order.status ACTIVE; fulfillment state RIDE_CONFIRMED)
  end
  Seller App (BPP)-->>Buyer App (BAP): /on_update (unsolicited): order.status ACTIVE; fulfillment state RIDE_ASSIGNED
  Buyer App (BAP)->>Seller App (BPP): /issue (The BAP submits an issue to the BPP to report a complaint or problem with the order, establishing the issue for tracking and resolution.)
  Seller App (BPP)-->>Buyer App (BAP): /on_issue (The BPP responds to a grievance opened by the BAP with the issue details, available actions, and resolution options.)
  Seller App (BPP)-->>Buyer App (BAP): /on_issue_status (unsolicited): The BPP sends an unsolicited issue status callback to the BAP with grievance resolution actions and status updates for the ride transaction.
  Buyer App (BAP)->>Seller App (BPP): /issue (The BAP reports an issue to the BPP regarding the confirmed ride order, creating a formal grievance record with problem details, expected response timelines, and resolution expectations.)
  Seller App (BPP)-->>Buyer App (BAP): /on_cancel (unsolicited): order.status CANCELLED; fulfillment state RIDE_CANCELLED, cancelled_by PROVIDER
```

## on_update_ride_assigned

```mermaid
sequenceDiagram
  participant Buyer App (BAP)
  participant Gateway
  participant Seller App (BPP)
  Buyer App (BAP)->>Gateway: /search (stops START, END)
  Gateway->>Seller App (BPP): /search (forwarded)
  Seller App (BPP)-->>Buyer App (BAP): /on_search (catalog)
  Buyer App (BAP)->>Seller App (BPP): /select
  Seller App (BPP)-->>Buyer App (BAP): /on_select (quote)
  Buyer App (BAP)->>Seller App (BPP): /init (payment ON_FULFILLMENT NOT_PAID, collected_by BPP)
  Seller App (BPP)-->>Buyer App (BAP): /on_init (payment ON_FULFILLMENT NOT_PAID, collected_by BPP)
  Buyer App (BAP)->>Seller App (BPP): /confirm (payment ON_FULFILLMENT NOT_PAID, collected_by BPP)
  Seller App (BPP)-->>Buyer App (BAP): /on_confirm (order.status ACTIVE; fulfillment state RIDE_CONFIRMED)
  rect rgb(191, 223, 255)
  Seller App (BPP)-->>Buyer App (BAP): /on_update (unsolicited): order.status ACTIVE; fulfillment state RIDE_ASSIGNED
  end
  Buyer App (BAP)->>Seller App (BPP): /issue (The BAP submits an issue to the BPP to report a complaint or problem with the order, establishing the issue for tracking and resolution.)
  Seller App (BPP)-->>Buyer App (BAP): /on_issue (The BPP responds to a grievance opened by the BAP with the issue details, available actions, and resolution options.)
  Seller App (BPP)-->>Buyer App (BAP): /on_issue_status (unsolicited): The BPP sends an unsolicited issue status callback to the BAP with grievance resolution actions and status updates for the ride transaction.
  Buyer App (BAP)->>Seller App (BPP): /issue (The BAP reports an issue to the BPP regarding the confirmed ride order, creating a formal grievance record with problem details, expected response timelines, and resolution expectations.)
  Seller App (BPP)-->>Buyer App (BAP): /on_cancel (unsolicited): order.status CANCELLED; fulfillment state RIDE_CANCELLED, cancelled_by PROVIDER
```

## issue_open_100

```mermaid
sequenceDiagram
  participant Buyer App (BAP)
  participant Gateway
  participant Seller App (BPP)
  Buyer App (BAP)->>Gateway: /search (stops START, END)
  Gateway->>Seller App (BPP): /search (forwarded)
  Seller App (BPP)-->>Buyer App (BAP): /on_search (catalog)
  Buyer App (BAP)->>Seller App (BPP): /select
  Seller App (BPP)-->>Buyer App (BAP): /on_select (quote)
  Buyer App (BAP)->>Seller App (BPP): /init (payment ON_FULFILLMENT NOT_PAID, collected_by BPP)
  Seller App (BPP)-->>Buyer App (BAP): /on_init (payment ON_FULFILLMENT NOT_PAID, collected_by BPP)
  Buyer App (BAP)->>Seller App (BPP): /confirm (payment ON_FULFILLMENT NOT_PAID, collected_by BPP)
  Seller App (BPP)-->>Buyer App (BAP): /on_confirm (order.status ACTIVE; fulfillment state RIDE_CONFIRMED)
  Seller App (BPP)-->>Buyer App (BAP): /on_update (unsolicited): order.status ACTIVE; fulfillment state RIDE_ASSIGNED
  rect rgb(191, 223, 255)
  Buyer App (BAP)->>Seller App (BPP): /issue (The BAP submits an issue to the BPP to report a complaint or problem with the order, establishing the issue for tracking and resolution.)
  end
  Seller App (BPP)-->>Buyer App (BAP): /on_issue (The BPP responds to a grievance opened by the BAP with the issue details, available actions, and resolution options.)
  Seller App (BPP)-->>Buyer App (BAP): /on_issue_status (unsolicited): The BPP sends an unsolicited issue status callback to the BAP with grievance resolution actions and status updates for the ride transaction.
  Buyer App (BAP)->>Seller App (BPP): /issue (The BAP reports an issue to the BPP regarding the confirmed ride order, creating a formal grievance record with problem details, expected response timelines, and resolution expectations.)
  Seller App (BPP)-->>Buyer App (BAP): /on_cancel (unsolicited): order.status CANCELLED; fulfillment state RIDE_CANCELLED, cancelled_by PROVIDER
```

## on_issue_processing_100

```mermaid
sequenceDiagram
  participant Buyer App (BAP)
  participant Gateway
  participant Seller App (BPP)
  Buyer App (BAP)->>Gateway: /search (stops START, END)
  Gateway->>Seller App (BPP): /search (forwarded)
  Seller App (BPP)-->>Buyer App (BAP): /on_search (catalog)
  Buyer App (BAP)->>Seller App (BPP): /select
  Seller App (BPP)-->>Buyer App (BAP): /on_select (quote)
  Buyer App (BAP)->>Seller App (BPP): /init (payment ON_FULFILLMENT NOT_PAID, collected_by BPP)
  Seller App (BPP)-->>Buyer App (BAP): /on_init (payment ON_FULFILLMENT NOT_PAID, collected_by BPP)
  Buyer App (BAP)->>Seller App (BPP): /confirm (payment ON_FULFILLMENT NOT_PAID, collected_by BPP)
  Seller App (BPP)-->>Buyer App (BAP): /on_confirm (order.status ACTIVE; fulfillment state RIDE_CONFIRMED)
  Seller App (BPP)-->>Buyer App (BAP): /on_update (unsolicited): order.status ACTIVE; fulfillment state RIDE_ASSIGNED
  Buyer App (BAP)->>Seller App (BPP): /issue (The BAP submits an issue to the BPP to report a complaint or problem with the order, establishing the issue for tracking and resolution.)
  rect rgb(191, 223, 255)
  Seller App (BPP)-->>Buyer App (BAP): /on_issue (The BPP responds to a grievance opened by the BAP with the issue details, available actions, and resolution options.)
  end
  Seller App (BPP)-->>Buyer App (BAP): /on_issue_status (unsolicited): The BPP sends an unsolicited issue status callback to the BAP with grievance resolution actions and status updates for the ride transaction.
  Buyer App (BAP)->>Seller App (BPP): /issue (The BAP reports an issue to the BPP regarding the confirmed ride order, creating a formal grievance record with problem details, expected response timelines, and resolution expectations.)
  Seller App (BPP)-->>Buyer App (BAP): /on_cancel (unsolicited): order.status CANCELLED; fulfillment state RIDE_CANCELLED, cancelled_by PROVIDER
```

## on_issue_resolved_100

```mermaid
sequenceDiagram
  participant Buyer App (BAP)
  participant Gateway
  participant Seller App (BPP)
  Buyer App (BAP)->>Gateway: /search (stops START, END)
  Gateway->>Seller App (BPP): /search (forwarded)
  Seller App (BPP)-->>Buyer App (BAP): /on_search (catalog)
  Buyer App (BAP)->>Seller App (BPP): /select
  Seller App (BPP)-->>Buyer App (BAP): /on_select (quote)
  Buyer App (BAP)->>Seller App (BPP): /init (payment ON_FULFILLMENT NOT_PAID, collected_by BPP)
  Seller App (BPP)-->>Buyer App (BAP): /on_init (payment ON_FULFILLMENT NOT_PAID, collected_by BPP)
  Buyer App (BAP)->>Seller App (BPP): /confirm (payment ON_FULFILLMENT NOT_PAID, collected_by BPP)
  Seller App (BPP)-->>Buyer App (BAP): /on_confirm (order.status ACTIVE; fulfillment state RIDE_CONFIRMED)
  Seller App (BPP)-->>Buyer App (BAP): /on_update (unsolicited): order.status ACTIVE; fulfillment state RIDE_ASSIGNED
  Buyer App (BAP)->>Seller App (BPP): /issue (The BAP submits an issue to the BPP to report a complaint or problem with the order, establishing the issue for tracking and resolution.)
  Seller App (BPP)-->>Buyer App (BAP): /on_issue (The BPP responds to a grievance opened by the BAP with the issue details, available actions, and resolution options.)
  rect rgb(191, 223, 255)
  Seller App (BPP)-->>Buyer App (BAP): /on_issue_status (unsolicited): The BPP sends an unsolicited issue status callback to the BAP with grievance resolution actions and status updates for the ride transaction.
  end
  Buyer App (BAP)->>Seller App (BPP): /issue (The BAP reports an issue to the BPP regarding the confirmed ride order, creating a formal grievance record with problem details, expected response timelines, and resolution expectations.)
  Seller App (BPP)-->>Buyer App (BAP): /on_cancel (unsolicited): order.status CANCELLED; fulfillment state RIDE_CANCELLED, cancelled_by PROVIDER
```

## issue_close_100

```mermaid
sequenceDiagram
  participant Buyer App (BAP)
  participant Gateway
  participant Seller App (BPP)
  Buyer App (BAP)->>Gateway: /search (stops START, END)
  Gateway->>Seller App (BPP): /search (forwarded)
  Seller App (BPP)-->>Buyer App (BAP): /on_search (catalog)
  Buyer App (BAP)->>Seller App (BPP): /select
  Seller App (BPP)-->>Buyer App (BAP): /on_select (quote)
  Buyer App (BAP)->>Seller App (BPP): /init (payment ON_FULFILLMENT NOT_PAID, collected_by BPP)
  Seller App (BPP)-->>Buyer App (BAP): /on_init (payment ON_FULFILLMENT NOT_PAID, collected_by BPP)
  Buyer App (BAP)->>Seller App (BPP): /confirm (payment ON_FULFILLMENT NOT_PAID, collected_by BPP)
  Seller App (BPP)-->>Buyer App (BAP): /on_confirm (order.status ACTIVE; fulfillment state RIDE_CONFIRMED)
  Seller App (BPP)-->>Buyer App (BAP): /on_update (unsolicited): order.status ACTIVE; fulfillment state RIDE_ASSIGNED
  Buyer App (BAP)->>Seller App (BPP): /issue (The BAP submits an issue to the BPP to report a complaint or problem with the order, establishing the issue for tracking and resolution.)
  Seller App (BPP)-->>Buyer App (BAP): /on_issue (The BPP responds to a grievance opened by the BAP with the issue details, available actions, and resolution options.)
  Seller App (BPP)-->>Buyer App (BAP): /on_issue_status (unsolicited): The BPP sends an unsolicited issue status callback to the BAP with grievance resolution actions and status updates for the ride transaction.
  rect rgb(191, 223, 255)
  Buyer App (BAP)->>Seller App (BPP): /issue (The BAP reports an issue to the BPP regarding the confirmed ride order, creating a formal grievance record with problem details, expected response timelines, and resolution expectations.)
  end
  Seller App (BPP)-->>Buyer App (BAP): /on_cancel (unsolicited): order.status CANCELLED; fulfillment state RIDE_CANCELLED, cancelled_by PROVIDER
```

## on_cancel_seller_cancellation

```mermaid
sequenceDiagram
  participant Buyer App (BAP)
  participant Gateway
  participant Seller App (BPP)
  Buyer App (BAP)->>Gateway: /search (stops START, END)
  Gateway->>Seller App (BPP): /search (forwarded)
  Seller App (BPP)-->>Buyer App (BAP): /on_search (catalog)
  Buyer App (BAP)->>Seller App (BPP): /select
  Seller App (BPP)-->>Buyer App (BAP): /on_select (quote)
  Buyer App (BAP)->>Seller App (BPP): /init (payment ON_FULFILLMENT NOT_PAID, collected_by BPP)
  Seller App (BPP)-->>Buyer App (BAP): /on_init (payment ON_FULFILLMENT NOT_PAID, collected_by BPP)
  Buyer App (BAP)->>Seller App (BPP): /confirm (payment ON_FULFILLMENT NOT_PAID, collected_by BPP)
  Seller App (BPP)-->>Buyer App (BAP): /on_confirm (order.status ACTIVE; fulfillment state RIDE_CONFIRMED)
  Seller App (BPP)-->>Buyer App (BAP): /on_update (unsolicited): order.status ACTIVE; fulfillment state RIDE_ASSIGNED
  Buyer App (BAP)->>Seller App (BPP): /issue (The BAP submits an issue to the BPP to report a complaint or problem with the order, establishing the issue for tracking and resolution.)
  Seller App (BPP)-->>Buyer App (BAP): /on_issue (The BPP responds to a grievance opened by the BAP with the issue details, available actions, and resolution options.)
  Seller App (BPP)-->>Buyer App (BAP): /on_issue_status (unsolicited): The BPP sends an unsolicited issue status callback to the BAP with grievance resolution actions and status updates for the ride transaction.
  Buyer App (BAP)->>Seller App (BPP): /issue (The BAP reports an issue to the BPP regarding the confirmed ride order, creating a formal grievance record with problem details, expected response timelines, and resolution expectations.)
  rect rgb(191, 223, 255)
  Seller App (BPP)-->>Buyer App (BAP): /on_cancel (unsolicited): order.status CANCELLED; fulfillment state RIDE_CANCELLED, cancelled_by PROVIDER
  end
```

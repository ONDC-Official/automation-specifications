# Schedule_Trip_With_IGM(v-1.0.0) — Sequence Diagrams

Internal data file consumed by the Developer Guide's "Sequence Diagram" tab (API Walkthrough).
Not meant to be shown as its own docs page — the frontend filters this slug out of the Use Case
Brief / Additional Resources / Changelog tab lists and instead looks up the section matching the
selected API call's `action_id` (the `##` heading below) to render that step's diagram.

One `## <action_id>` heading per step of `Schedule_Trip_with_With_IGM_v-1_0_0_.yaml` (Ride-hailing), in that flow's own step order, each followed by its Mermaid `sequenceDiagram`: the whole flow, with that call's own message(s) highlighted — same convention as the other domains' per-step sequence-diagram docs.

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
  Buyer App (BAP)->>Seller App (BPP): /track (track order)
  Seller App (BPP)-->>Buyer App (BAP): /on_track (tracking)
  Seller App (BPP)-->>Buyer App (BAP): /on_status (unsolicited): order.status ACTIVE; fulfillment state RIDE_ENROUTE_PICKUP
  Seller App (BPP)-->>Buyer App (BAP): /on_status (unsolicited): order.status ACTIVE; fulfillment state RIDE_ARRIVED_PICKUP
  Seller App (BPP)-->>Buyer App (BAP): /on_status (unsolicited): order.status ACTIVE; fulfillment state RIDE_STARTED
  Seller App (BPP)-->>Buyer App (BAP): /on_update (unsolicited): order.status ACTIVE; fulfillment state RIDE_ENDED
  Buyer App (BAP)->>Seller App (BPP): /status (order status)
  Seller App (BPP)-->>Buyer App (BAP): /on_status (order.status COMPLETED; fulfillment state RIDE_ENDED)
  Buyer App (BAP)->>Seller App (BPP): /issue (The BAP submits an issue to the BPP to report a complaint or problem with the order, establishing the issue for tracking and resolution.)
  Seller App (BPP)-->>Buyer App (BAP): /on_issue (The BPP responds to a grievance opened by the BAP with the issue details, available actions, and resolution options.)
  Seller App (BPP)-->>Buyer App (BAP): /on_issue_status (unsolicited): The BPP sends an unsolicited issue status callback to the BAP with grievance resolution actions and status updates for the ride transaction.
  Buyer App (BAP)->>Seller App (BPP): /issue (The BAP reports an issue to the BPP regarding the confirmed ride order, creating a formal grievance record with problem details, expected response timelines, and resolution expectations.)
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
  Buyer App (BAP)->>Seller App (BPP): /track (track order)
  Seller App (BPP)-->>Buyer App (BAP): /on_track (tracking)
  Seller App (BPP)-->>Buyer App (BAP): /on_status (unsolicited): order.status ACTIVE; fulfillment state RIDE_ENROUTE_PICKUP
  Seller App (BPP)-->>Buyer App (BAP): /on_status (unsolicited): order.status ACTIVE; fulfillment state RIDE_ARRIVED_PICKUP
  Seller App (BPP)-->>Buyer App (BAP): /on_status (unsolicited): order.status ACTIVE; fulfillment state RIDE_STARTED
  Seller App (BPP)-->>Buyer App (BAP): /on_update (unsolicited): order.status ACTIVE; fulfillment state RIDE_ENDED
  Buyer App (BAP)->>Seller App (BPP): /status (order status)
  Seller App (BPP)-->>Buyer App (BAP): /on_status (order.status COMPLETED; fulfillment state RIDE_ENDED)
  Buyer App (BAP)->>Seller App (BPP): /issue (The BAP submits an issue to the BPP to report a complaint or problem with the order, establishing the issue for tracking and resolution.)
  Seller App (BPP)-->>Buyer App (BAP): /on_issue (The BPP responds to a grievance opened by the BAP with the issue details, available actions, and resolution options.)
  Seller App (BPP)-->>Buyer App (BAP): /on_issue_status (unsolicited): The BPP sends an unsolicited issue status callback to the BAP with grievance resolution actions and status updates for the ride transaction.
  Buyer App (BAP)->>Seller App (BPP): /issue (The BAP reports an issue to the BPP regarding the confirmed ride order, creating a formal grievance record with problem details, expected response timelines, and resolution expectations.)
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
  Buyer App (BAP)->>Seller App (BPP): /track (track order)
  Seller App (BPP)-->>Buyer App (BAP): /on_track (tracking)
  Seller App (BPP)-->>Buyer App (BAP): /on_status (unsolicited): order.status ACTIVE; fulfillment state RIDE_ENROUTE_PICKUP
  Seller App (BPP)-->>Buyer App (BAP): /on_status (unsolicited): order.status ACTIVE; fulfillment state RIDE_ARRIVED_PICKUP
  Seller App (BPP)-->>Buyer App (BAP): /on_status (unsolicited): order.status ACTIVE; fulfillment state RIDE_STARTED
  Seller App (BPP)-->>Buyer App (BAP): /on_update (unsolicited): order.status ACTIVE; fulfillment state RIDE_ENDED
  Buyer App (BAP)->>Seller App (BPP): /status (order status)
  Seller App (BPP)-->>Buyer App (BAP): /on_status (order.status COMPLETED; fulfillment state RIDE_ENDED)
  Buyer App (BAP)->>Seller App (BPP): /issue (The BAP submits an issue to the BPP to report a complaint or problem with the order, establishing the issue for tracking and resolution.)
  Seller App (BPP)-->>Buyer App (BAP): /on_issue (The BPP responds to a grievance opened by the BAP with the issue details, available actions, and resolution options.)
  Seller App (BPP)-->>Buyer App (BAP): /on_issue_status (unsolicited): The BPP sends an unsolicited issue status callback to the BAP with grievance resolution actions and status updates for the ride transaction.
  Buyer App (BAP)->>Seller App (BPP): /issue (The BAP reports an issue to the BPP regarding the confirmed ride order, creating a formal grievance record with problem details, expected response timelines, and resolution expectations.)
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
  Buyer App (BAP)->>Seller App (BPP): /track (track order)
  Seller App (BPP)-->>Buyer App (BAP): /on_track (tracking)
  Seller App (BPP)-->>Buyer App (BAP): /on_status (unsolicited): order.status ACTIVE; fulfillment state RIDE_ENROUTE_PICKUP
  Seller App (BPP)-->>Buyer App (BAP): /on_status (unsolicited): order.status ACTIVE; fulfillment state RIDE_ARRIVED_PICKUP
  Seller App (BPP)-->>Buyer App (BAP): /on_status (unsolicited): order.status ACTIVE; fulfillment state RIDE_STARTED
  Seller App (BPP)-->>Buyer App (BAP): /on_update (unsolicited): order.status ACTIVE; fulfillment state RIDE_ENDED
  Buyer App (BAP)->>Seller App (BPP): /status (order status)
  Seller App (BPP)-->>Buyer App (BAP): /on_status (order.status COMPLETED; fulfillment state RIDE_ENDED)
  Buyer App (BAP)->>Seller App (BPP): /issue (The BAP submits an issue to the BPP to report a complaint or problem with the order, establishing the issue for tracking and resolution.)
  Seller App (BPP)-->>Buyer App (BAP): /on_issue (The BPP responds to a grievance opened by the BAP with the issue details, available actions, and resolution options.)
  Seller App (BPP)-->>Buyer App (BAP): /on_issue_status (unsolicited): The BPP sends an unsolicited issue status callback to the BAP with grievance resolution actions and status updates for the ride transaction.
  Buyer App (BAP)->>Seller App (BPP): /issue (The BAP reports an issue to the BPP regarding the confirmed ride order, creating a formal grievance record with problem details, expected response timelines, and resolution expectations.)
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
  Buyer App (BAP)->>Seller App (BPP): /track (track order)
  Seller App (BPP)-->>Buyer App (BAP): /on_track (tracking)
  Seller App (BPP)-->>Buyer App (BAP): /on_status (unsolicited): order.status ACTIVE; fulfillment state RIDE_ENROUTE_PICKUP
  Seller App (BPP)-->>Buyer App (BAP): /on_status (unsolicited): order.status ACTIVE; fulfillment state RIDE_ARRIVED_PICKUP
  Seller App (BPP)-->>Buyer App (BAP): /on_status (unsolicited): order.status ACTIVE; fulfillment state RIDE_STARTED
  Seller App (BPP)-->>Buyer App (BAP): /on_update (unsolicited): order.status ACTIVE; fulfillment state RIDE_ENDED
  Buyer App (BAP)->>Seller App (BPP): /status (order status)
  Seller App (BPP)-->>Buyer App (BAP): /on_status (order.status COMPLETED; fulfillment state RIDE_ENDED)
  Buyer App (BAP)->>Seller App (BPP): /issue (The BAP submits an issue to the BPP to report a complaint or problem with the order, establishing the issue for tracking and resolution.)
  Seller App (BPP)-->>Buyer App (BAP): /on_issue (The BPP responds to a grievance opened by the BAP with the issue details, available actions, and resolution options.)
  Seller App (BPP)-->>Buyer App (BAP): /on_issue_status (unsolicited): The BPP sends an unsolicited issue status callback to the BAP with grievance resolution actions and status updates for the ride transaction.
  Buyer App (BAP)->>Seller App (BPP): /issue (The BAP reports an issue to the BPP regarding the confirmed ride order, creating a formal grievance record with problem details, expected response timelines, and resolution expectations.)
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
  Buyer App (BAP)->>Seller App (BPP): /track (track order)
  Seller App (BPP)-->>Buyer App (BAP): /on_track (tracking)
  Seller App (BPP)-->>Buyer App (BAP): /on_status (unsolicited): order.status ACTIVE; fulfillment state RIDE_ENROUTE_PICKUP
  Seller App (BPP)-->>Buyer App (BAP): /on_status (unsolicited): order.status ACTIVE; fulfillment state RIDE_ARRIVED_PICKUP
  Seller App (BPP)-->>Buyer App (BAP): /on_status (unsolicited): order.status ACTIVE; fulfillment state RIDE_STARTED
  Seller App (BPP)-->>Buyer App (BAP): /on_update (unsolicited): order.status ACTIVE; fulfillment state RIDE_ENDED
  Buyer App (BAP)->>Seller App (BPP): /status (order status)
  Seller App (BPP)-->>Buyer App (BAP): /on_status (order.status COMPLETED; fulfillment state RIDE_ENDED)
  Buyer App (BAP)->>Seller App (BPP): /issue (The BAP submits an issue to the BPP to report a complaint or problem with the order, establishing the issue for tracking and resolution.)
  Seller App (BPP)-->>Buyer App (BAP): /on_issue (The BPP responds to a grievance opened by the BAP with the issue details, available actions, and resolution options.)
  Seller App (BPP)-->>Buyer App (BAP): /on_issue_status (unsolicited): The BPP sends an unsolicited issue status callback to the BAP with grievance resolution actions and status updates for the ride transaction.
  Buyer App (BAP)->>Seller App (BPP): /issue (The BAP reports an issue to the BPP regarding the confirmed ride order, creating a formal grievance record with problem details, expected response timelines, and resolution expectations.)
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
  Buyer App (BAP)->>Seller App (BPP): /track (track order)
  Seller App (BPP)-->>Buyer App (BAP): /on_track (tracking)
  Seller App (BPP)-->>Buyer App (BAP): /on_status (unsolicited): order.status ACTIVE; fulfillment state RIDE_ENROUTE_PICKUP
  Seller App (BPP)-->>Buyer App (BAP): /on_status (unsolicited): order.status ACTIVE; fulfillment state RIDE_ARRIVED_PICKUP
  Seller App (BPP)-->>Buyer App (BAP): /on_status (unsolicited): order.status ACTIVE; fulfillment state RIDE_STARTED
  Seller App (BPP)-->>Buyer App (BAP): /on_update (unsolicited): order.status ACTIVE; fulfillment state RIDE_ENDED
  Buyer App (BAP)->>Seller App (BPP): /status (order status)
  Seller App (BPP)-->>Buyer App (BAP): /on_status (order.status COMPLETED; fulfillment state RIDE_ENDED)
  Buyer App (BAP)->>Seller App (BPP): /issue (The BAP submits an issue to the BPP to report a complaint or problem with the order, establishing the issue for tracking and resolution.)
  Seller App (BPP)-->>Buyer App (BAP): /on_issue (The BPP responds to a grievance opened by the BAP with the issue details, available actions, and resolution options.)
  Seller App (BPP)-->>Buyer App (BAP): /on_issue_status (unsolicited): The BPP sends an unsolicited issue status callback to the BAP with grievance resolution actions and status updates for the ride transaction.
  Buyer App (BAP)->>Seller App (BPP): /issue (The BAP reports an issue to the BPP regarding the confirmed ride order, creating a formal grievance record with problem details, expected response timelines, and resolution expectations.)
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
  Buyer App (BAP)->>Seller App (BPP): /track (track order)
  Seller App (BPP)-->>Buyer App (BAP): /on_track (tracking)
  Seller App (BPP)-->>Buyer App (BAP): /on_status (unsolicited): order.status ACTIVE; fulfillment state RIDE_ENROUTE_PICKUP
  Seller App (BPP)-->>Buyer App (BAP): /on_status (unsolicited): order.status ACTIVE; fulfillment state RIDE_ARRIVED_PICKUP
  Seller App (BPP)-->>Buyer App (BAP): /on_status (unsolicited): order.status ACTIVE; fulfillment state RIDE_STARTED
  Seller App (BPP)-->>Buyer App (BAP): /on_update (unsolicited): order.status ACTIVE; fulfillment state RIDE_ENDED
  Buyer App (BAP)->>Seller App (BPP): /status (order status)
  Seller App (BPP)-->>Buyer App (BAP): /on_status (order.status COMPLETED; fulfillment state RIDE_ENDED)
  Buyer App (BAP)->>Seller App (BPP): /issue (The BAP submits an issue to the BPP to report a complaint or problem with the order, establishing the issue for tracking and resolution.)
  Seller App (BPP)-->>Buyer App (BAP): /on_issue (The BPP responds to a grievance opened by the BAP with the issue details, available actions, and resolution options.)
  Seller App (BPP)-->>Buyer App (BAP): /on_issue_status (unsolicited): The BPP sends an unsolicited issue status callback to the BAP with grievance resolution actions and status updates for the ride transaction.
  Buyer App (BAP)->>Seller App (BPP): /issue (The BAP reports an issue to the BPP regarding the confirmed ride order, creating a formal grievance record with problem details, expected response timelines, and resolution expectations.)
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
  Buyer App (BAP)->>Seller App (BPP): /track (track order)
  Seller App (BPP)-->>Buyer App (BAP): /on_track (tracking)
  Seller App (BPP)-->>Buyer App (BAP): /on_status (unsolicited): order.status ACTIVE; fulfillment state RIDE_ENROUTE_PICKUP
  Seller App (BPP)-->>Buyer App (BAP): /on_status (unsolicited): order.status ACTIVE; fulfillment state RIDE_ARRIVED_PICKUP
  Seller App (BPP)-->>Buyer App (BAP): /on_status (unsolicited): order.status ACTIVE; fulfillment state RIDE_STARTED
  Seller App (BPP)-->>Buyer App (BAP): /on_update (unsolicited): order.status ACTIVE; fulfillment state RIDE_ENDED
  Buyer App (BAP)->>Seller App (BPP): /status (order status)
  Seller App (BPP)-->>Buyer App (BAP): /on_status (order.status COMPLETED; fulfillment state RIDE_ENDED)
  Buyer App (BAP)->>Seller App (BPP): /issue (The BAP submits an issue to the BPP to report a complaint or problem with the order, establishing the issue for tracking and resolution.)
  Seller App (BPP)-->>Buyer App (BAP): /on_issue (The BPP responds to a grievance opened by the BAP with the issue details, available actions, and resolution options.)
  Seller App (BPP)-->>Buyer App (BAP): /on_issue_status (unsolicited): The BPP sends an unsolicited issue status callback to the BAP with grievance resolution actions and status updates for the ride transaction.
  Buyer App (BAP)->>Seller App (BPP): /issue (The BAP reports an issue to the BPP regarding the confirmed ride order, creating a formal grievance record with problem details, expected response timelines, and resolution expectations.)
```

## track

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
  Buyer App (BAP)->>Seller App (BPP): /track (track order)
  end
  Seller App (BPP)-->>Buyer App (BAP): /on_track (tracking)
  Seller App (BPP)-->>Buyer App (BAP): /on_status (unsolicited): order.status ACTIVE; fulfillment state RIDE_ENROUTE_PICKUP
  Seller App (BPP)-->>Buyer App (BAP): /on_status (unsolicited): order.status ACTIVE; fulfillment state RIDE_ARRIVED_PICKUP
  Seller App (BPP)-->>Buyer App (BAP): /on_status (unsolicited): order.status ACTIVE; fulfillment state RIDE_STARTED
  Seller App (BPP)-->>Buyer App (BAP): /on_update (unsolicited): order.status ACTIVE; fulfillment state RIDE_ENDED
  Buyer App (BAP)->>Seller App (BPP): /status (order status)
  Seller App (BPP)-->>Buyer App (BAP): /on_status (order.status COMPLETED; fulfillment state RIDE_ENDED)
  Buyer App (BAP)->>Seller App (BPP): /issue (The BAP submits an issue to the BPP to report a complaint or problem with the order, establishing the issue for tracking and resolution.)
  Seller App (BPP)-->>Buyer App (BAP): /on_issue (The BPP responds to a grievance opened by the BAP with the issue details, available actions, and resolution options.)
  Seller App (BPP)-->>Buyer App (BAP): /on_issue_status (unsolicited): The BPP sends an unsolicited issue status callback to the BAP with grievance resolution actions and status updates for the ride transaction.
  Buyer App (BAP)->>Seller App (BPP): /issue (The BAP reports an issue to the BPP regarding the confirmed ride order, creating a formal grievance record with problem details, expected response timelines, and resolution expectations.)
```

## on_track

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
  Buyer App (BAP)->>Seller App (BPP): /track (track order)
  rect rgb(191, 223, 255)
  Seller App (BPP)-->>Buyer App (BAP): /on_track (tracking)
  end
  Seller App (BPP)-->>Buyer App (BAP): /on_status (unsolicited): order.status ACTIVE; fulfillment state RIDE_ENROUTE_PICKUP
  Seller App (BPP)-->>Buyer App (BAP): /on_status (unsolicited): order.status ACTIVE; fulfillment state RIDE_ARRIVED_PICKUP
  Seller App (BPP)-->>Buyer App (BAP): /on_status (unsolicited): order.status ACTIVE; fulfillment state RIDE_STARTED
  Seller App (BPP)-->>Buyer App (BAP): /on_update (unsolicited): order.status ACTIVE; fulfillment state RIDE_ENDED
  Buyer App (BAP)->>Seller App (BPP): /status (order status)
  Seller App (BPP)-->>Buyer App (BAP): /on_status (order.status COMPLETED; fulfillment state RIDE_ENDED)
  Buyer App (BAP)->>Seller App (BPP): /issue (The BAP submits an issue to the BPP to report a complaint or problem with the order, establishing the issue for tracking and resolution.)
  Seller App (BPP)-->>Buyer App (BAP): /on_issue (The BPP responds to a grievance opened by the BAP with the issue details, available actions, and resolution options.)
  Seller App (BPP)-->>Buyer App (BAP): /on_issue_status (unsolicited): The BPP sends an unsolicited issue status callback to the BAP with grievance resolution actions and status updates for the ride transaction.
  Buyer App (BAP)->>Seller App (BPP): /issue (The BAP reports an issue to the BPP regarding the confirmed ride order, creating a formal grievance record with problem details, expected response timelines, and resolution expectations.)
```

## on_status_unsolicited

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
  Buyer App (BAP)->>Seller App (BPP): /track (track order)
  Seller App (BPP)-->>Buyer App (BAP): /on_track (tracking)
  rect rgb(191, 223, 255)
  Seller App (BPP)-->>Buyer App (BAP): /on_status (unsolicited): order.status ACTIVE; fulfillment state RIDE_ENROUTE_PICKUP
  end
  Seller App (BPP)-->>Buyer App (BAP): /on_status (unsolicited): order.status ACTIVE; fulfillment state RIDE_ARRIVED_PICKUP
  Seller App (BPP)-->>Buyer App (BAP): /on_status (unsolicited): order.status ACTIVE; fulfillment state RIDE_STARTED
  Seller App (BPP)-->>Buyer App (BAP): /on_update (unsolicited): order.status ACTIVE; fulfillment state RIDE_ENDED
  Buyer App (BAP)->>Seller App (BPP): /status (order status)
  Seller App (BPP)-->>Buyer App (BAP): /on_status (order.status COMPLETED; fulfillment state RIDE_ENDED)
  Buyer App (BAP)->>Seller App (BPP): /issue (The BAP submits an issue to the BPP to report a complaint or problem with the order, establishing the issue for tracking and resolution.)
  Seller App (BPP)-->>Buyer App (BAP): /on_issue (The BPP responds to a grievance opened by the BAP with the issue details, available actions, and resolution options.)
  Seller App (BPP)-->>Buyer App (BAP): /on_issue_status (unsolicited): The BPP sends an unsolicited issue status callback to the BAP with grievance resolution actions and status updates for the ride transaction.
  Buyer App (BAP)->>Seller App (BPP): /issue (The BAP reports an issue to the BPP regarding the confirmed ride order, creating a formal grievance record with problem details, expected response timelines, and resolution expectations.)
```

## on_status_ride_arrived

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
  Buyer App (BAP)->>Seller App (BPP): /track (track order)
  Seller App (BPP)-->>Buyer App (BAP): /on_track (tracking)
  Seller App (BPP)-->>Buyer App (BAP): /on_status (unsolicited): order.status ACTIVE; fulfillment state RIDE_ENROUTE_PICKUP
  rect rgb(191, 223, 255)
  Seller App (BPP)-->>Buyer App (BAP): /on_status (unsolicited): order.status ACTIVE; fulfillment state RIDE_ARRIVED_PICKUP
  end
  Seller App (BPP)-->>Buyer App (BAP): /on_status (unsolicited): order.status ACTIVE; fulfillment state RIDE_STARTED
  Seller App (BPP)-->>Buyer App (BAP): /on_update (unsolicited): order.status ACTIVE; fulfillment state RIDE_ENDED
  Buyer App (BAP)->>Seller App (BPP): /status (order status)
  Seller App (BPP)-->>Buyer App (BAP): /on_status (order.status COMPLETED; fulfillment state RIDE_ENDED)
  Buyer App (BAP)->>Seller App (BPP): /issue (The BAP submits an issue to the BPP to report a complaint or problem with the order, establishing the issue for tracking and resolution.)
  Seller App (BPP)-->>Buyer App (BAP): /on_issue (The BPP responds to a grievance opened by the BAP with the issue details, available actions, and resolution options.)
  Seller App (BPP)-->>Buyer App (BAP): /on_issue_status (unsolicited): The BPP sends an unsolicited issue status callback to the BAP with grievance resolution actions and status updates for the ride transaction.
  Buyer App (BAP)->>Seller App (BPP): /issue (The BAP reports an issue to the BPP regarding the confirmed ride order, creating a formal grievance record with problem details, expected response timelines, and resolution expectations.)
```

## on_status_ride_started

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
  Buyer App (BAP)->>Seller App (BPP): /track (track order)
  Seller App (BPP)-->>Buyer App (BAP): /on_track (tracking)
  Seller App (BPP)-->>Buyer App (BAP): /on_status (unsolicited): order.status ACTIVE; fulfillment state RIDE_ENROUTE_PICKUP
  Seller App (BPP)-->>Buyer App (BAP): /on_status (unsolicited): order.status ACTIVE; fulfillment state RIDE_ARRIVED_PICKUP
  rect rgb(191, 223, 255)
  Seller App (BPP)-->>Buyer App (BAP): /on_status (unsolicited): order.status ACTIVE; fulfillment state RIDE_STARTED
  end
  Seller App (BPP)-->>Buyer App (BAP): /on_update (unsolicited): order.status ACTIVE; fulfillment state RIDE_ENDED
  Buyer App (BAP)->>Seller App (BPP): /status (order status)
  Seller App (BPP)-->>Buyer App (BAP): /on_status (order.status COMPLETED; fulfillment state RIDE_ENDED)
  Buyer App (BAP)->>Seller App (BPP): /issue (The BAP submits an issue to the BPP to report a complaint or problem with the order, establishing the issue for tracking and resolution.)
  Seller App (BPP)-->>Buyer App (BAP): /on_issue (The BPP responds to a grievance opened by the BAP with the issue details, available actions, and resolution options.)
  Seller App (BPP)-->>Buyer App (BAP): /on_issue_status (unsolicited): The BPP sends an unsolicited issue status callback to the BAP with grievance resolution actions and status updates for the ride transaction.
  Buyer App (BAP)->>Seller App (BPP): /issue (The BAP reports an issue to the BPP regarding the confirmed ride order, creating a formal grievance record with problem details, expected response timelines, and resolution expectations.)
```

## on_update_ride_ended

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
  Buyer App (BAP)->>Seller App (BPP): /track (track order)
  Seller App (BPP)-->>Buyer App (BAP): /on_track (tracking)
  Seller App (BPP)-->>Buyer App (BAP): /on_status (unsolicited): order.status ACTIVE; fulfillment state RIDE_ENROUTE_PICKUP
  Seller App (BPP)-->>Buyer App (BAP): /on_status (unsolicited): order.status ACTIVE; fulfillment state RIDE_ARRIVED_PICKUP
  Seller App (BPP)-->>Buyer App (BAP): /on_status (unsolicited): order.status ACTIVE; fulfillment state RIDE_STARTED
  rect rgb(191, 223, 255)
  Seller App (BPP)-->>Buyer App (BAP): /on_update (unsolicited): order.status ACTIVE; fulfillment state RIDE_ENDED
  end
  Buyer App (BAP)->>Seller App (BPP): /status (order status)
  Seller App (BPP)-->>Buyer App (BAP): /on_status (order.status COMPLETED; fulfillment state RIDE_ENDED)
  Buyer App (BAP)->>Seller App (BPP): /issue (The BAP submits an issue to the BPP to report a complaint or problem with the order, establishing the issue for tracking and resolution.)
  Seller App (BPP)-->>Buyer App (BAP): /on_issue (The BPP responds to a grievance opened by the BAP with the issue details, available actions, and resolution options.)
  Seller App (BPP)-->>Buyer App (BAP): /on_issue_status (unsolicited): The BPP sends an unsolicited issue status callback to the BAP with grievance resolution actions and status updates for the ride transaction.
  Buyer App (BAP)->>Seller App (BPP): /issue (The BAP reports an issue to the BPP regarding the confirmed ride order, creating a formal grievance record with problem details, expected response timelines, and resolution expectations.)
```

## status

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
  Buyer App (BAP)->>Seller App (BPP): /track (track order)
  Seller App (BPP)-->>Buyer App (BAP): /on_track (tracking)
  Seller App (BPP)-->>Buyer App (BAP): /on_status (unsolicited): order.status ACTIVE; fulfillment state RIDE_ENROUTE_PICKUP
  Seller App (BPP)-->>Buyer App (BAP): /on_status (unsolicited): order.status ACTIVE; fulfillment state RIDE_ARRIVED_PICKUP
  Seller App (BPP)-->>Buyer App (BAP): /on_status (unsolicited): order.status ACTIVE; fulfillment state RIDE_STARTED
  Seller App (BPP)-->>Buyer App (BAP): /on_update (unsolicited): order.status ACTIVE; fulfillment state RIDE_ENDED
  rect rgb(191, 223, 255)
  Buyer App (BAP)->>Seller App (BPP): /status (order status)
  end
  Seller App (BPP)-->>Buyer App (BAP): /on_status (order.status COMPLETED; fulfillment state RIDE_ENDED)
  Buyer App (BAP)->>Seller App (BPP): /issue (The BAP submits an issue to the BPP to report a complaint or problem with the order, establishing the issue for tracking and resolution.)
  Seller App (BPP)-->>Buyer App (BAP): /on_issue (The BPP responds to a grievance opened by the BAP with the issue details, available actions, and resolution options.)
  Seller App (BPP)-->>Buyer App (BAP): /on_issue_status (unsolicited): The BPP sends an unsolicited issue status callback to the BAP with grievance resolution actions and status updates for the ride transaction.
  Buyer App (BAP)->>Seller App (BPP): /issue (The BAP reports an issue to the BPP regarding the confirmed ride order, creating a formal grievance record with problem details, expected response timelines, and resolution expectations.)
```

## on_status_solicited

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
  Buyer App (BAP)->>Seller App (BPP): /track (track order)
  Seller App (BPP)-->>Buyer App (BAP): /on_track (tracking)
  Seller App (BPP)-->>Buyer App (BAP): /on_status (unsolicited): order.status ACTIVE; fulfillment state RIDE_ENROUTE_PICKUP
  Seller App (BPP)-->>Buyer App (BAP): /on_status (unsolicited): order.status ACTIVE; fulfillment state RIDE_ARRIVED_PICKUP
  Seller App (BPP)-->>Buyer App (BAP): /on_status (unsolicited): order.status ACTIVE; fulfillment state RIDE_STARTED
  Seller App (BPP)-->>Buyer App (BAP): /on_update (unsolicited): order.status ACTIVE; fulfillment state RIDE_ENDED
  Buyer App (BAP)->>Seller App (BPP): /status (order status)
  rect rgb(191, 223, 255)
  Seller App (BPP)-->>Buyer App (BAP): /on_status (order.status COMPLETED; fulfillment state RIDE_ENDED)
  end
  Buyer App (BAP)->>Seller App (BPP): /issue (The BAP submits an issue to the BPP to report a complaint or problem with the order, establishing the issue for tracking and resolution.)
  Seller App (BPP)-->>Buyer App (BAP): /on_issue (The BPP responds to a grievance opened by the BAP with the issue details, available actions, and resolution options.)
  Seller App (BPP)-->>Buyer App (BAP): /on_issue_status (unsolicited): The BPP sends an unsolicited issue status callback to the BAP with grievance resolution actions and status updates for the ride transaction.
  Buyer App (BAP)->>Seller App (BPP): /issue (The BAP reports an issue to the BPP regarding the confirmed ride order, creating a formal grievance record with problem details, expected response timelines, and resolution expectations.)
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
  Buyer App (BAP)->>Seller App (BPP): /track (track order)
  Seller App (BPP)-->>Buyer App (BAP): /on_track (tracking)
  Seller App (BPP)-->>Buyer App (BAP): /on_status (unsolicited): order.status ACTIVE; fulfillment state RIDE_ENROUTE_PICKUP
  Seller App (BPP)-->>Buyer App (BAP): /on_status (unsolicited): order.status ACTIVE; fulfillment state RIDE_ARRIVED_PICKUP
  Seller App (BPP)-->>Buyer App (BAP): /on_status (unsolicited): order.status ACTIVE; fulfillment state RIDE_STARTED
  Seller App (BPP)-->>Buyer App (BAP): /on_update (unsolicited): order.status ACTIVE; fulfillment state RIDE_ENDED
  Buyer App (BAP)->>Seller App (BPP): /status (order status)
  Seller App (BPP)-->>Buyer App (BAP): /on_status (order.status COMPLETED; fulfillment state RIDE_ENDED)
  rect rgb(191, 223, 255)
  Buyer App (BAP)->>Seller App (BPP): /issue (The BAP submits an issue to the BPP to report a complaint or problem with the order, establishing the issue for tracking and resolution.)
  end
  Seller App (BPP)-->>Buyer App (BAP): /on_issue (The BPP responds to a grievance opened by the BAP with the issue details, available actions, and resolution options.)
  Seller App (BPP)-->>Buyer App (BAP): /on_issue_status (unsolicited): The BPP sends an unsolicited issue status callback to the BAP with grievance resolution actions and status updates for the ride transaction.
  Buyer App (BAP)->>Seller App (BPP): /issue (The BAP reports an issue to the BPP regarding the confirmed ride order, creating a formal grievance record with problem details, expected response timelines, and resolution expectations.)
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
  Buyer App (BAP)->>Seller App (BPP): /track (track order)
  Seller App (BPP)-->>Buyer App (BAP): /on_track (tracking)
  Seller App (BPP)-->>Buyer App (BAP): /on_status (unsolicited): order.status ACTIVE; fulfillment state RIDE_ENROUTE_PICKUP
  Seller App (BPP)-->>Buyer App (BAP): /on_status (unsolicited): order.status ACTIVE; fulfillment state RIDE_ARRIVED_PICKUP
  Seller App (BPP)-->>Buyer App (BAP): /on_status (unsolicited): order.status ACTIVE; fulfillment state RIDE_STARTED
  Seller App (BPP)-->>Buyer App (BAP): /on_update (unsolicited): order.status ACTIVE; fulfillment state RIDE_ENDED
  Buyer App (BAP)->>Seller App (BPP): /status (order status)
  Seller App (BPP)-->>Buyer App (BAP): /on_status (order.status COMPLETED; fulfillment state RIDE_ENDED)
  Buyer App (BAP)->>Seller App (BPP): /issue (The BAP submits an issue to the BPP to report a complaint or problem with the order, establishing the issue for tracking and resolution.)
  rect rgb(191, 223, 255)
  Seller App (BPP)-->>Buyer App (BAP): /on_issue (The BPP responds to a grievance opened by the BAP with the issue details, available actions, and resolution options.)
  end
  Seller App (BPP)-->>Buyer App (BAP): /on_issue_status (unsolicited): The BPP sends an unsolicited issue status callback to the BAP with grievance resolution actions and status updates for the ride transaction.
  Buyer App (BAP)->>Seller App (BPP): /issue (The BAP reports an issue to the BPP regarding the confirmed ride order, creating a formal grievance record with problem details, expected response timelines, and resolution expectations.)
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
  Buyer App (BAP)->>Seller App (BPP): /track (track order)
  Seller App (BPP)-->>Buyer App (BAP): /on_track (tracking)
  Seller App (BPP)-->>Buyer App (BAP): /on_status (unsolicited): order.status ACTIVE; fulfillment state RIDE_ENROUTE_PICKUP
  Seller App (BPP)-->>Buyer App (BAP): /on_status (unsolicited): order.status ACTIVE; fulfillment state RIDE_ARRIVED_PICKUP
  Seller App (BPP)-->>Buyer App (BAP): /on_status (unsolicited): order.status ACTIVE; fulfillment state RIDE_STARTED
  Seller App (BPP)-->>Buyer App (BAP): /on_update (unsolicited): order.status ACTIVE; fulfillment state RIDE_ENDED
  Buyer App (BAP)->>Seller App (BPP): /status (order status)
  Seller App (BPP)-->>Buyer App (BAP): /on_status (order.status COMPLETED; fulfillment state RIDE_ENDED)
  Buyer App (BAP)->>Seller App (BPP): /issue (The BAP submits an issue to the BPP to report a complaint or problem with the order, establishing the issue for tracking and resolution.)
  Seller App (BPP)-->>Buyer App (BAP): /on_issue (The BPP responds to a grievance opened by the BAP with the issue details, available actions, and resolution options.)
  rect rgb(191, 223, 255)
  Seller App (BPP)-->>Buyer App (BAP): /on_issue_status (unsolicited): The BPP sends an unsolicited issue status callback to the BAP with grievance resolution actions and status updates for the ride transaction.
  end
  Buyer App (BAP)->>Seller App (BPP): /issue (The BAP reports an issue to the BPP regarding the confirmed ride order, creating a formal grievance record with problem details, expected response timelines, and resolution expectations.)
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
  Buyer App (BAP)->>Seller App (BPP): /track (track order)
  Seller App (BPP)-->>Buyer App (BAP): /on_track (tracking)
  Seller App (BPP)-->>Buyer App (BAP): /on_status (unsolicited): order.status ACTIVE; fulfillment state RIDE_ENROUTE_PICKUP
  Seller App (BPP)-->>Buyer App (BAP): /on_status (unsolicited): order.status ACTIVE; fulfillment state RIDE_ARRIVED_PICKUP
  Seller App (BPP)-->>Buyer App (BAP): /on_status (unsolicited): order.status ACTIVE; fulfillment state RIDE_STARTED
  Seller App (BPP)-->>Buyer App (BAP): /on_update (unsolicited): order.status ACTIVE; fulfillment state RIDE_ENDED
  Buyer App (BAP)->>Seller App (BPP): /status (order status)
  Seller App (BPP)-->>Buyer App (BAP): /on_status (order.status COMPLETED; fulfillment state RIDE_ENDED)
  Buyer App (BAP)->>Seller App (BPP): /issue (The BAP submits an issue to the BPP to report a complaint or problem with the order, establishing the issue for tracking and resolution.)
  Seller App (BPP)-->>Buyer App (BAP): /on_issue (The BPP responds to a grievance opened by the BAP with the issue details, available actions, and resolution options.)
  Seller App (BPP)-->>Buyer App (BAP): /on_issue_status (unsolicited): The BPP sends an unsolicited issue status callback to the BAP with grievance resolution actions and status updates for the ride transaction.
  rect rgb(191, 223, 255)
  Buyer App (BAP)->>Seller App (BPP): /issue (The BAP reports an issue to the BPP regarding the confirmed ride order, creating a formal grievance record with problem details, expected response timelines, and resolution expectations.)
  end
```

# OnDemand_Assign_driver_on_onconfirm_With_IGM(v-2.0.0) — Sequence Diagrams

Internal data file consumed by the Developer Guide's "Sequence Diagram" tab (API Walkthrough).
Not meant to be shown as its own docs page — the frontend filters this slug out of the Use Case
Brief / Additional Resources / Changelog tab lists and instead looks up the section matching the
selected API call's `action_id` (the `##` heading below) to render that step's diagram.

One `## <action_id>` heading per step of `OnDemand_Assign_driver_on_onconfirm_With_IGM_v-2_0_0_.yaml` (Ride-hailing), in that flow's own step order, each followed by its Mermaid `sequenceDiagram`: the whole flow, with that call's own message(s) highlighted — same convention as the other domains' per-step sequence-diagram docs.

## search_ride

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
  Seller App (BPP)-->>Buyer App (BAP): /on_confirm (order.status ACTIVE; fulfillment state RIDE_ASSIGNED)
  Seller App (BPP)-->>Buyer App (BAP): /on_track (unsolicited): tracking
  Seller App (BPP)-->>Buyer App (BAP): /on_status (unsolicited): order.status ACTIVE; fulfillment state RIDE_ENROUTE_PICKUP
  Buyer App (BAP)->>Seller App (BPP): /track (track order)
  Seller App (BPP)-->>Buyer App (BAP): /on_track (tracking)
  Seller App (BPP)-->>Buyer App (BAP): /on_status (unsolicited): order.status ACTIVE; fulfillment state RIDE_ARRIVED_PICKUP
  Seller App (BPP)-->>Buyer App (BAP): /on_status (unsolicited): order.status ACTIVE; fulfillment state RIDE_STARTED
  Seller App (BPP)-->>Buyer App (BAP): /on_status (unsolicited): order.status ACTIVE; fulfillment state RIDE_ENDED
  Seller App (BPP)-->>Buyer App (BAP): /on_update (unsolicited): order.status ACTIVE; fulfillment state RIDE_ENDED
  Buyer App (BAP)->>Seller App (BPP): /status (order status)
  Seller App (BPP)-->>Buyer App (BAP): /on_status (order.status COMPLETED; fulfillment state RIDE_ENDED)
  Buyer App (BAP)->>Seller App (BPP): /issue (The BAP submits an issue to the BPP to formally lodge a complaint or grievance regarding the driver assignment or ride order.)
  Seller App (BPP)-->>Buyer App (BAP): /on_issue (The BPP acknowledges an issue opened by the BAP and responds with issue details, available actions, and resolution options as part of integrated grievance management.)
  Seller App (BPP)-->>Buyer App (BAP): /on_issue (unsolicited): The BPP proactively notifies the BAP of an issue or complaint that has arisen during the ride assignment, providing the issue details, category, and available resolution actions for the BAP to address.
  Buyer App (BAP)->>Seller App (BPP): /issue (The BAP raises a formal issue with the BPP to report and track a complaint regarding the assigned driver or service delivery. This initiates the integrated grievance management process, capturing complaint details, category, and expected resolution expectations.)
  Seller App (BPP)-->>Buyer App (BAP): /on_issue (The BPP responds to a BAP-reported issue with issue details, available actions, and proposed resolutions.)
  Seller App (BPP)-->>Buyer App (BAP): /on_issue (unsolicited): The BPP sends an unsolicited on issue notification to the BAP to communicate an issue or grievance related to the ride, including issue details and available actions for resolution.
  Buyer App (BAP)->>Seller App (BPP): /issue (The BAP submits an issue to the BPP to report a problem with the confirmed ride order, specifying the complaint category, order details, and expected resolution timeline for grievance management.)
  Seller App (BPP)-->>Buyer App (BAP): /on_issue (The BPP sends an on issue callback to the BAP to confirm its acceptance of the issue resolution and specify the remedial actions taken to address the reported problem.)
  Buyer App (BAP)->>Seller App (BPP): /issue (The BAP raises an issue complaint with the BPP regarding the ride-hailing transaction, initiating the issue resolution process under ONDC's issue governance mechanism.)
```

## on_search

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
  Seller App (BPP)-->>Buyer App (BAP): /on_confirm (order.status ACTIVE; fulfillment state RIDE_ASSIGNED)
  Seller App (BPP)-->>Buyer App (BAP): /on_track (unsolicited): tracking
  Seller App (BPP)-->>Buyer App (BAP): /on_status (unsolicited): order.status ACTIVE; fulfillment state RIDE_ENROUTE_PICKUP
  Buyer App (BAP)->>Seller App (BPP): /track (track order)
  Seller App (BPP)-->>Buyer App (BAP): /on_track (tracking)
  Seller App (BPP)-->>Buyer App (BAP): /on_status (unsolicited): order.status ACTIVE; fulfillment state RIDE_ARRIVED_PICKUP
  Seller App (BPP)-->>Buyer App (BAP): /on_status (unsolicited): order.status ACTIVE; fulfillment state RIDE_STARTED
  Seller App (BPP)-->>Buyer App (BAP): /on_status (unsolicited): order.status ACTIVE; fulfillment state RIDE_ENDED
  Seller App (BPP)-->>Buyer App (BAP): /on_update (unsolicited): order.status ACTIVE; fulfillment state RIDE_ENDED
  Buyer App (BAP)->>Seller App (BPP): /status (order status)
  Seller App (BPP)-->>Buyer App (BAP): /on_status (order.status COMPLETED; fulfillment state RIDE_ENDED)
  Buyer App (BAP)->>Seller App (BPP): /issue (The BAP submits an issue to the BPP to formally lodge a complaint or grievance regarding the driver assignment or ride order.)
  Seller App (BPP)-->>Buyer App (BAP): /on_issue (The BPP acknowledges an issue opened by the BAP and responds with issue details, available actions, and resolution options as part of integrated grievance management.)
  Seller App (BPP)-->>Buyer App (BAP): /on_issue (unsolicited): The BPP proactively notifies the BAP of an issue or complaint that has arisen during the ride assignment, providing the issue details, category, and available resolution actions for the BAP to address.
  Buyer App (BAP)->>Seller App (BPP): /issue (The BAP raises a formal issue with the BPP to report and track a complaint regarding the assigned driver or service delivery. This initiates the integrated grievance management process, capturing complaint details, category, and expected resolution expectations.)
  Seller App (BPP)-->>Buyer App (BAP): /on_issue (The BPP responds to a BAP-reported issue with issue details, available actions, and proposed resolutions.)
  Seller App (BPP)-->>Buyer App (BAP): /on_issue (unsolicited): The BPP sends an unsolicited on issue notification to the BAP to communicate an issue or grievance related to the ride, including issue details and available actions for resolution.
  Buyer App (BAP)->>Seller App (BPP): /issue (The BAP submits an issue to the BPP to report a problem with the confirmed ride order, specifying the complaint category, order details, and expected resolution timeline for grievance management.)
  Seller App (BPP)-->>Buyer App (BAP): /on_issue (The BPP sends an on issue callback to the BAP to confirm its acceptance of the issue resolution and specify the remedial actions taken to address the reported problem.)
  Buyer App (BAP)->>Seller App (BPP): /issue (The BAP raises an issue complaint with the BPP regarding the ride-hailing transaction, initiating the issue resolution process under ONDC's issue governance mechanism.)
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
  Seller App (BPP)-->>Buyer App (BAP): /on_confirm (order.status ACTIVE; fulfillment state RIDE_ASSIGNED)
  Seller App (BPP)-->>Buyer App (BAP): /on_track (unsolicited): tracking
  Seller App (BPP)-->>Buyer App (BAP): /on_status (unsolicited): order.status ACTIVE; fulfillment state RIDE_ENROUTE_PICKUP
  Buyer App (BAP)->>Seller App (BPP): /track (track order)
  Seller App (BPP)-->>Buyer App (BAP): /on_track (tracking)
  Seller App (BPP)-->>Buyer App (BAP): /on_status (unsolicited): order.status ACTIVE; fulfillment state RIDE_ARRIVED_PICKUP
  Seller App (BPP)-->>Buyer App (BAP): /on_status (unsolicited): order.status ACTIVE; fulfillment state RIDE_STARTED
  Seller App (BPP)-->>Buyer App (BAP): /on_status (unsolicited): order.status ACTIVE; fulfillment state RIDE_ENDED
  Seller App (BPP)-->>Buyer App (BAP): /on_update (unsolicited): order.status ACTIVE; fulfillment state RIDE_ENDED
  Buyer App (BAP)->>Seller App (BPP): /status (order status)
  Seller App (BPP)-->>Buyer App (BAP): /on_status (order.status COMPLETED; fulfillment state RIDE_ENDED)
  Buyer App (BAP)->>Seller App (BPP): /issue (The BAP submits an issue to the BPP to formally lodge a complaint or grievance regarding the driver assignment or ride order.)
  Seller App (BPP)-->>Buyer App (BAP): /on_issue (The BPP acknowledges an issue opened by the BAP and responds with issue details, available actions, and resolution options as part of integrated grievance management.)
  Seller App (BPP)-->>Buyer App (BAP): /on_issue (unsolicited): The BPP proactively notifies the BAP of an issue or complaint that has arisen during the ride assignment, providing the issue details, category, and available resolution actions for the BAP to address.
  Buyer App (BAP)->>Seller App (BPP): /issue (The BAP raises a formal issue with the BPP to report and track a complaint regarding the assigned driver or service delivery. This initiates the integrated grievance management process, capturing complaint details, category, and expected resolution expectations.)
  Seller App (BPP)-->>Buyer App (BAP): /on_issue (The BPP responds to a BAP-reported issue with issue details, available actions, and proposed resolutions.)
  Seller App (BPP)-->>Buyer App (BAP): /on_issue (unsolicited): The BPP sends an unsolicited on issue notification to the BAP to communicate an issue or grievance related to the ride, including issue details and available actions for resolution.
  Buyer App (BAP)->>Seller App (BPP): /issue (The BAP submits an issue to the BPP to report a problem with the confirmed ride order, specifying the complaint category, order details, and expected resolution timeline for grievance management.)
  Seller App (BPP)-->>Buyer App (BAP): /on_issue (The BPP sends an on issue callback to the BAP to confirm its acceptance of the issue resolution and specify the remedial actions taken to address the reported problem.)
  Buyer App (BAP)->>Seller App (BPP): /issue (The BAP raises an issue complaint with the BPP regarding the ride-hailing transaction, initiating the issue resolution process under ONDC's issue governance mechanism.)
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
  Seller App (BPP)-->>Buyer App (BAP): /on_confirm (order.status ACTIVE; fulfillment state RIDE_ASSIGNED)
  Seller App (BPP)-->>Buyer App (BAP): /on_track (unsolicited): tracking
  Seller App (BPP)-->>Buyer App (BAP): /on_status (unsolicited): order.status ACTIVE; fulfillment state RIDE_ENROUTE_PICKUP
  Buyer App (BAP)->>Seller App (BPP): /track (track order)
  Seller App (BPP)-->>Buyer App (BAP): /on_track (tracking)
  Seller App (BPP)-->>Buyer App (BAP): /on_status (unsolicited): order.status ACTIVE; fulfillment state RIDE_ARRIVED_PICKUP
  Seller App (BPP)-->>Buyer App (BAP): /on_status (unsolicited): order.status ACTIVE; fulfillment state RIDE_STARTED
  Seller App (BPP)-->>Buyer App (BAP): /on_status (unsolicited): order.status ACTIVE; fulfillment state RIDE_ENDED
  Seller App (BPP)-->>Buyer App (BAP): /on_update (unsolicited): order.status ACTIVE; fulfillment state RIDE_ENDED
  Buyer App (BAP)->>Seller App (BPP): /status (order status)
  Seller App (BPP)-->>Buyer App (BAP): /on_status (order.status COMPLETED; fulfillment state RIDE_ENDED)
  Buyer App (BAP)->>Seller App (BPP): /issue (The BAP submits an issue to the BPP to formally lodge a complaint or grievance regarding the driver assignment or ride order.)
  Seller App (BPP)-->>Buyer App (BAP): /on_issue (The BPP acknowledges an issue opened by the BAP and responds with issue details, available actions, and resolution options as part of integrated grievance management.)
  Seller App (BPP)-->>Buyer App (BAP): /on_issue (unsolicited): The BPP proactively notifies the BAP of an issue or complaint that has arisen during the ride assignment, providing the issue details, category, and available resolution actions for the BAP to address.
  Buyer App (BAP)->>Seller App (BPP): /issue (The BAP raises a formal issue with the BPP to report and track a complaint regarding the assigned driver or service delivery. This initiates the integrated grievance management process, capturing complaint details, category, and expected resolution expectations.)
  Seller App (BPP)-->>Buyer App (BAP): /on_issue (The BPP responds to a BAP-reported issue with issue details, available actions, and proposed resolutions.)
  Seller App (BPP)-->>Buyer App (BAP): /on_issue (unsolicited): The BPP sends an unsolicited on issue notification to the BAP to communicate an issue or grievance related to the ride, including issue details and available actions for resolution.
  Buyer App (BAP)->>Seller App (BPP): /issue (The BAP submits an issue to the BPP to report a problem with the confirmed ride order, specifying the complaint category, order details, and expected resolution timeline for grievance management.)
  Seller App (BPP)-->>Buyer App (BAP): /on_issue (The BPP sends an on issue callback to the BAP to confirm its acceptance of the issue resolution and specify the remedial actions taken to address the reported problem.)
  Buyer App (BAP)->>Seller App (BPP): /issue (The BAP raises an issue complaint with the BPP regarding the ride-hailing transaction, initiating the issue resolution process under ONDC's issue governance mechanism.)
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
  Seller App (BPP)-->>Buyer App (BAP): /on_confirm (order.status ACTIVE; fulfillment state RIDE_ASSIGNED)
  Seller App (BPP)-->>Buyer App (BAP): /on_track (unsolicited): tracking
  Seller App (BPP)-->>Buyer App (BAP): /on_status (unsolicited): order.status ACTIVE; fulfillment state RIDE_ENROUTE_PICKUP
  Buyer App (BAP)->>Seller App (BPP): /track (track order)
  Seller App (BPP)-->>Buyer App (BAP): /on_track (tracking)
  Seller App (BPP)-->>Buyer App (BAP): /on_status (unsolicited): order.status ACTIVE; fulfillment state RIDE_ARRIVED_PICKUP
  Seller App (BPP)-->>Buyer App (BAP): /on_status (unsolicited): order.status ACTIVE; fulfillment state RIDE_STARTED
  Seller App (BPP)-->>Buyer App (BAP): /on_status (unsolicited): order.status ACTIVE; fulfillment state RIDE_ENDED
  Seller App (BPP)-->>Buyer App (BAP): /on_update (unsolicited): order.status ACTIVE; fulfillment state RIDE_ENDED
  Buyer App (BAP)->>Seller App (BPP): /status (order status)
  Seller App (BPP)-->>Buyer App (BAP): /on_status (order.status COMPLETED; fulfillment state RIDE_ENDED)
  Buyer App (BAP)->>Seller App (BPP): /issue (The BAP submits an issue to the BPP to formally lodge a complaint or grievance regarding the driver assignment or ride order.)
  Seller App (BPP)-->>Buyer App (BAP): /on_issue (The BPP acknowledges an issue opened by the BAP and responds with issue details, available actions, and resolution options as part of integrated grievance management.)
  Seller App (BPP)-->>Buyer App (BAP): /on_issue (unsolicited): The BPP proactively notifies the BAP of an issue or complaint that has arisen during the ride assignment, providing the issue details, category, and available resolution actions for the BAP to address.
  Buyer App (BAP)->>Seller App (BPP): /issue (The BAP raises a formal issue with the BPP to report and track a complaint regarding the assigned driver or service delivery. This initiates the integrated grievance management process, capturing complaint details, category, and expected resolution expectations.)
  Seller App (BPP)-->>Buyer App (BAP): /on_issue (The BPP responds to a BAP-reported issue with issue details, available actions, and proposed resolutions.)
  Seller App (BPP)-->>Buyer App (BAP): /on_issue (unsolicited): The BPP sends an unsolicited on issue notification to the BAP to communicate an issue or grievance related to the ride, including issue details and available actions for resolution.
  Buyer App (BAP)->>Seller App (BPP): /issue (The BAP submits an issue to the BPP to report a problem with the confirmed ride order, specifying the complaint category, order details, and expected resolution timeline for grievance management.)
  Seller App (BPP)-->>Buyer App (BAP): /on_issue (The BPP sends an on issue callback to the BAP to confirm its acceptance of the issue resolution and specify the remedial actions taken to address the reported problem.)
  Buyer App (BAP)->>Seller App (BPP): /issue (The BAP raises an issue complaint with the BPP regarding the ride-hailing transaction, initiating the issue resolution process under ONDC's issue governance mechanism.)
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
  Seller App (BPP)-->>Buyer App (BAP): /on_confirm (order.status ACTIVE; fulfillment state RIDE_ASSIGNED)
  Seller App (BPP)-->>Buyer App (BAP): /on_track (unsolicited): tracking
  Seller App (BPP)-->>Buyer App (BAP): /on_status (unsolicited): order.status ACTIVE; fulfillment state RIDE_ENROUTE_PICKUP
  Buyer App (BAP)->>Seller App (BPP): /track (track order)
  Seller App (BPP)-->>Buyer App (BAP): /on_track (tracking)
  Seller App (BPP)-->>Buyer App (BAP): /on_status (unsolicited): order.status ACTIVE; fulfillment state RIDE_ARRIVED_PICKUP
  Seller App (BPP)-->>Buyer App (BAP): /on_status (unsolicited): order.status ACTIVE; fulfillment state RIDE_STARTED
  Seller App (BPP)-->>Buyer App (BAP): /on_status (unsolicited): order.status ACTIVE; fulfillment state RIDE_ENDED
  Seller App (BPP)-->>Buyer App (BAP): /on_update (unsolicited): order.status ACTIVE; fulfillment state RIDE_ENDED
  Buyer App (BAP)->>Seller App (BPP): /status (order status)
  Seller App (BPP)-->>Buyer App (BAP): /on_status (order.status COMPLETED; fulfillment state RIDE_ENDED)
  Buyer App (BAP)->>Seller App (BPP): /issue (The BAP submits an issue to the BPP to formally lodge a complaint or grievance regarding the driver assignment or ride order.)
  Seller App (BPP)-->>Buyer App (BAP): /on_issue (The BPP acknowledges an issue opened by the BAP and responds with issue details, available actions, and resolution options as part of integrated grievance management.)
  Seller App (BPP)-->>Buyer App (BAP): /on_issue (unsolicited): The BPP proactively notifies the BAP of an issue or complaint that has arisen during the ride assignment, providing the issue details, category, and available resolution actions for the BAP to address.
  Buyer App (BAP)->>Seller App (BPP): /issue (The BAP raises a formal issue with the BPP to report and track a complaint regarding the assigned driver or service delivery. This initiates the integrated grievance management process, capturing complaint details, category, and expected resolution expectations.)
  Seller App (BPP)-->>Buyer App (BAP): /on_issue (The BPP responds to a BAP-reported issue with issue details, available actions, and proposed resolutions.)
  Seller App (BPP)-->>Buyer App (BAP): /on_issue (unsolicited): The BPP sends an unsolicited on issue notification to the BAP to communicate an issue or grievance related to the ride, including issue details and available actions for resolution.
  Buyer App (BAP)->>Seller App (BPP): /issue (The BAP submits an issue to the BPP to report a problem with the confirmed ride order, specifying the complaint category, order details, and expected resolution timeline for grievance management.)
  Seller App (BPP)-->>Buyer App (BAP): /on_issue (The BPP sends an on issue callback to the BAP to confirm its acceptance of the issue resolution and specify the remedial actions taken to address the reported problem.)
  Buyer App (BAP)->>Seller App (BPP): /issue (The BAP raises an issue complaint with the BPP regarding the ride-hailing transaction, initiating the issue resolution process under ONDC's issue governance mechanism.)
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
  Seller App (BPP)-->>Buyer App (BAP): /on_confirm (order.status ACTIVE; fulfillment state RIDE_ASSIGNED)
  Seller App (BPP)-->>Buyer App (BAP): /on_track (unsolicited): tracking
  Seller App (BPP)-->>Buyer App (BAP): /on_status (unsolicited): order.status ACTIVE; fulfillment state RIDE_ENROUTE_PICKUP
  Buyer App (BAP)->>Seller App (BPP): /track (track order)
  Seller App (BPP)-->>Buyer App (BAP): /on_track (tracking)
  Seller App (BPP)-->>Buyer App (BAP): /on_status (unsolicited): order.status ACTIVE; fulfillment state RIDE_ARRIVED_PICKUP
  Seller App (BPP)-->>Buyer App (BAP): /on_status (unsolicited): order.status ACTIVE; fulfillment state RIDE_STARTED
  Seller App (BPP)-->>Buyer App (BAP): /on_status (unsolicited): order.status ACTIVE; fulfillment state RIDE_ENDED
  Seller App (BPP)-->>Buyer App (BAP): /on_update (unsolicited): order.status ACTIVE; fulfillment state RIDE_ENDED
  Buyer App (BAP)->>Seller App (BPP): /status (order status)
  Seller App (BPP)-->>Buyer App (BAP): /on_status (order.status COMPLETED; fulfillment state RIDE_ENDED)
  Buyer App (BAP)->>Seller App (BPP): /issue (The BAP submits an issue to the BPP to formally lodge a complaint or grievance regarding the driver assignment or ride order.)
  Seller App (BPP)-->>Buyer App (BAP): /on_issue (The BPP acknowledges an issue opened by the BAP and responds with issue details, available actions, and resolution options as part of integrated grievance management.)
  Seller App (BPP)-->>Buyer App (BAP): /on_issue (unsolicited): The BPP proactively notifies the BAP of an issue or complaint that has arisen during the ride assignment, providing the issue details, category, and available resolution actions for the BAP to address.
  Buyer App (BAP)->>Seller App (BPP): /issue (The BAP raises a formal issue with the BPP to report and track a complaint regarding the assigned driver or service delivery. This initiates the integrated grievance management process, capturing complaint details, category, and expected resolution expectations.)
  Seller App (BPP)-->>Buyer App (BAP): /on_issue (The BPP responds to a BAP-reported issue with issue details, available actions, and proposed resolutions.)
  Seller App (BPP)-->>Buyer App (BAP): /on_issue (unsolicited): The BPP sends an unsolicited on issue notification to the BAP to communicate an issue or grievance related to the ride, including issue details and available actions for resolution.
  Buyer App (BAP)->>Seller App (BPP): /issue (The BAP submits an issue to the BPP to report a problem with the confirmed ride order, specifying the complaint category, order details, and expected resolution timeline for grievance management.)
  Seller App (BPP)-->>Buyer App (BAP): /on_issue (The BPP sends an on issue callback to the BAP to confirm its acceptance of the issue resolution and specify the remedial actions taken to address the reported problem.)
  Buyer App (BAP)->>Seller App (BPP): /issue (The BAP raises an issue complaint with the BPP regarding the ride-hailing transaction, initiating the issue resolution process under ONDC's issue governance mechanism.)
```

## on_confirm

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
  Seller App (BPP)-->>Buyer App (BAP): /on_confirm (order.status ACTIVE; fulfillment state RIDE_ASSIGNED)
  end
  Seller App (BPP)-->>Buyer App (BAP): /on_track (unsolicited): tracking
  Seller App (BPP)-->>Buyer App (BAP): /on_status (unsolicited): order.status ACTIVE; fulfillment state RIDE_ENROUTE_PICKUP
  Buyer App (BAP)->>Seller App (BPP): /track (track order)
  Seller App (BPP)-->>Buyer App (BAP): /on_track (tracking)
  Seller App (BPP)-->>Buyer App (BAP): /on_status (unsolicited): order.status ACTIVE; fulfillment state RIDE_ARRIVED_PICKUP
  Seller App (BPP)-->>Buyer App (BAP): /on_status (unsolicited): order.status ACTIVE; fulfillment state RIDE_STARTED
  Seller App (BPP)-->>Buyer App (BAP): /on_status (unsolicited): order.status ACTIVE; fulfillment state RIDE_ENDED
  Seller App (BPP)-->>Buyer App (BAP): /on_update (unsolicited): order.status ACTIVE; fulfillment state RIDE_ENDED
  Buyer App (BAP)->>Seller App (BPP): /status (order status)
  Seller App (BPP)-->>Buyer App (BAP): /on_status (order.status COMPLETED; fulfillment state RIDE_ENDED)
  Buyer App (BAP)->>Seller App (BPP): /issue (The BAP submits an issue to the BPP to formally lodge a complaint or grievance regarding the driver assignment or ride order.)
  Seller App (BPP)-->>Buyer App (BAP): /on_issue (The BPP acknowledges an issue opened by the BAP and responds with issue details, available actions, and resolution options as part of integrated grievance management.)
  Seller App (BPP)-->>Buyer App (BAP): /on_issue (unsolicited): The BPP proactively notifies the BAP of an issue or complaint that has arisen during the ride assignment, providing the issue details, category, and available resolution actions for the BAP to address.
  Buyer App (BAP)->>Seller App (BPP): /issue (The BAP raises a formal issue with the BPP to report and track a complaint regarding the assigned driver or service delivery. This initiates the integrated grievance management process, capturing complaint details, category, and expected resolution expectations.)
  Seller App (BPP)-->>Buyer App (BAP): /on_issue (The BPP responds to a BAP-reported issue with issue details, available actions, and proposed resolutions.)
  Seller App (BPP)-->>Buyer App (BAP): /on_issue (unsolicited): The BPP sends an unsolicited on issue notification to the BAP to communicate an issue or grievance related to the ride, including issue details and available actions for resolution.
  Buyer App (BAP)->>Seller App (BPP): /issue (The BAP submits an issue to the BPP to report a problem with the confirmed ride order, specifying the complaint category, order details, and expected resolution timeline for grievance management.)
  Seller App (BPP)-->>Buyer App (BAP): /on_issue (The BPP sends an on issue callback to the BAP to confirm its acceptance of the issue resolution and specify the remedial actions taken to address the reported problem.)
  Buyer App (BAP)->>Seller App (BPP): /issue (The BAP raises an issue complaint with the BPP regarding the ride-hailing transaction, initiating the issue resolution process under ONDC's issue governance mechanism.)
```

## on_track_on_assign

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
  Seller App (BPP)-->>Buyer App (BAP): /on_confirm (order.status ACTIVE; fulfillment state RIDE_ASSIGNED)
  rect rgb(191, 223, 255)
  Seller App (BPP)-->>Buyer App (BAP): /on_track (unsolicited): tracking
  end
  Seller App (BPP)-->>Buyer App (BAP): /on_status (unsolicited): order.status ACTIVE; fulfillment state RIDE_ENROUTE_PICKUP
  Buyer App (BAP)->>Seller App (BPP): /track (track order)
  Seller App (BPP)-->>Buyer App (BAP): /on_track (tracking)
  Seller App (BPP)-->>Buyer App (BAP): /on_status (unsolicited): order.status ACTIVE; fulfillment state RIDE_ARRIVED_PICKUP
  Seller App (BPP)-->>Buyer App (BAP): /on_status (unsolicited): order.status ACTIVE; fulfillment state RIDE_STARTED
  Seller App (BPP)-->>Buyer App (BAP): /on_status (unsolicited): order.status ACTIVE; fulfillment state RIDE_ENDED
  Seller App (BPP)-->>Buyer App (BAP): /on_update (unsolicited): order.status ACTIVE; fulfillment state RIDE_ENDED
  Buyer App (BAP)->>Seller App (BPP): /status (order status)
  Seller App (BPP)-->>Buyer App (BAP): /on_status (order.status COMPLETED; fulfillment state RIDE_ENDED)
  Buyer App (BAP)->>Seller App (BPP): /issue (The BAP submits an issue to the BPP to formally lodge a complaint or grievance regarding the driver assignment or ride order.)
  Seller App (BPP)-->>Buyer App (BAP): /on_issue (The BPP acknowledges an issue opened by the BAP and responds with issue details, available actions, and resolution options as part of integrated grievance management.)
  Seller App (BPP)-->>Buyer App (BAP): /on_issue (unsolicited): The BPP proactively notifies the BAP of an issue or complaint that has arisen during the ride assignment, providing the issue details, category, and available resolution actions for the BAP to address.
  Buyer App (BAP)->>Seller App (BPP): /issue (The BAP raises a formal issue with the BPP to report and track a complaint regarding the assigned driver or service delivery. This initiates the integrated grievance management process, capturing complaint details, category, and expected resolution expectations.)
  Seller App (BPP)-->>Buyer App (BAP): /on_issue (The BPP responds to a BAP-reported issue with issue details, available actions, and proposed resolutions.)
  Seller App (BPP)-->>Buyer App (BAP): /on_issue (unsolicited): The BPP sends an unsolicited on issue notification to the BAP to communicate an issue or grievance related to the ride, including issue details and available actions for resolution.
  Buyer App (BAP)->>Seller App (BPP): /issue (The BAP submits an issue to the BPP to report a problem with the confirmed ride order, specifying the complaint category, order details, and expected resolution timeline for grievance management.)
  Seller App (BPP)-->>Buyer App (BAP): /on_issue (The BPP sends an on issue callback to the BAP to confirm its acceptance of the issue resolution and specify the remedial actions taken to address the reported problem.)
  Buyer App (BAP)->>Seller App (BPP): /issue (The BAP raises an issue complaint with the BPP regarding the ride-hailing transaction, initiating the issue resolution process under ONDC's issue governance mechanism.)
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
  Seller App (BPP)-->>Buyer App (BAP): /on_confirm (order.status ACTIVE; fulfillment state RIDE_ASSIGNED)
  Seller App (BPP)-->>Buyer App (BAP): /on_track (unsolicited): tracking
  rect rgb(191, 223, 255)
  Seller App (BPP)-->>Buyer App (BAP): /on_status (unsolicited): order.status ACTIVE; fulfillment state RIDE_ENROUTE_PICKUP
  end
  Buyer App (BAP)->>Seller App (BPP): /track (track order)
  Seller App (BPP)-->>Buyer App (BAP): /on_track (tracking)
  Seller App (BPP)-->>Buyer App (BAP): /on_status (unsolicited): order.status ACTIVE; fulfillment state RIDE_ARRIVED_PICKUP
  Seller App (BPP)-->>Buyer App (BAP): /on_status (unsolicited): order.status ACTIVE; fulfillment state RIDE_STARTED
  Seller App (BPP)-->>Buyer App (BAP): /on_status (unsolicited): order.status ACTIVE; fulfillment state RIDE_ENDED
  Seller App (BPP)-->>Buyer App (BAP): /on_update (unsolicited): order.status ACTIVE; fulfillment state RIDE_ENDED
  Buyer App (BAP)->>Seller App (BPP): /status (order status)
  Seller App (BPP)-->>Buyer App (BAP): /on_status (order.status COMPLETED; fulfillment state RIDE_ENDED)
  Buyer App (BAP)->>Seller App (BPP): /issue (The BAP submits an issue to the BPP to formally lodge a complaint or grievance regarding the driver assignment or ride order.)
  Seller App (BPP)-->>Buyer App (BAP): /on_issue (The BPP acknowledges an issue opened by the BAP and responds with issue details, available actions, and resolution options as part of integrated grievance management.)
  Seller App (BPP)-->>Buyer App (BAP): /on_issue (unsolicited): The BPP proactively notifies the BAP of an issue or complaint that has arisen during the ride assignment, providing the issue details, category, and available resolution actions for the BAP to address.
  Buyer App (BAP)->>Seller App (BPP): /issue (The BAP raises a formal issue with the BPP to report and track a complaint regarding the assigned driver or service delivery. This initiates the integrated grievance management process, capturing complaint details, category, and expected resolution expectations.)
  Seller App (BPP)-->>Buyer App (BAP): /on_issue (The BPP responds to a BAP-reported issue with issue details, available actions, and proposed resolutions.)
  Seller App (BPP)-->>Buyer App (BAP): /on_issue (unsolicited): The BPP sends an unsolicited on issue notification to the BAP to communicate an issue or grievance related to the ride, including issue details and available actions for resolution.
  Buyer App (BAP)->>Seller App (BPP): /issue (The BAP submits an issue to the BPP to report a problem with the confirmed ride order, specifying the complaint category, order details, and expected resolution timeline for grievance management.)
  Seller App (BPP)-->>Buyer App (BAP): /on_issue (The BPP sends an on issue callback to the BAP to confirm its acceptance of the issue resolution and specify the remedial actions taken to address the reported problem.)
  Buyer App (BAP)->>Seller App (BPP): /issue (The BAP raises an issue complaint with the BPP regarding the ride-hailing transaction, initiating the issue resolution process under ONDC's issue governance mechanism.)
```

## track_ride

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
  Seller App (BPP)-->>Buyer App (BAP): /on_confirm (order.status ACTIVE; fulfillment state RIDE_ASSIGNED)
  Seller App (BPP)-->>Buyer App (BAP): /on_track (unsolicited): tracking
  Seller App (BPP)-->>Buyer App (BAP): /on_status (unsolicited): order.status ACTIVE; fulfillment state RIDE_ENROUTE_PICKUP
  rect rgb(191, 223, 255)
  Buyer App (BAP)->>Seller App (BPP): /track (track order)
  end
  Seller App (BPP)-->>Buyer App (BAP): /on_track (tracking)
  Seller App (BPP)-->>Buyer App (BAP): /on_status (unsolicited): order.status ACTIVE; fulfillment state RIDE_ARRIVED_PICKUP
  Seller App (BPP)-->>Buyer App (BAP): /on_status (unsolicited): order.status ACTIVE; fulfillment state RIDE_STARTED
  Seller App (BPP)-->>Buyer App (BAP): /on_status (unsolicited): order.status ACTIVE; fulfillment state RIDE_ENDED
  Seller App (BPP)-->>Buyer App (BAP): /on_update (unsolicited): order.status ACTIVE; fulfillment state RIDE_ENDED
  Buyer App (BAP)->>Seller App (BPP): /status (order status)
  Seller App (BPP)-->>Buyer App (BAP): /on_status (order.status COMPLETED; fulfillment state RIDE_ENDED)
  Buyer App (BAP)->>Seller App (BPP): /issue (The BAP submits an issue to the BPP to formally lodge a complaint or grievance regarding the driver assignment or ride order.)
  Seller App (BPP)-->>Buyer App (BAP): /on_issue (The BPP acknowledges an issue opened by the BAP and responds with issue details, available actions, and resolution options as part of integrated grievance management.)
  Seller App (BPP)-->>Buyer App (BAP): /on_issue (unsolicited): The BPP proactively notifies the BAP of an issue or complaint that has arisen during the ride assignment, providing the issue details, category, and available resolution actions for the BAP to address.
  Buyer App (BAP)->>Seller App (BPP): /issue (The BAP raises a formal issue with the BPP to report and track a complaint regarding the assigned driver or service delivery. This initiates the integrated grievance management process, capturing complaint details, category, and expected resolution expectations.)
  Seller App (BPP)-->>Buyer App (BAP): /on_issue (The BPP responds to a BAP-reported issue with issue details, available actions, and proposed resolutions.)
  Seller App (BPP)-->>Buyer App (BAP): /on_issue (unsolicited): The BPP sends an unsolicited on issue notification to the BAP to communicate an issue or grievance related to the ride, including issue details and available actions for resolution.
  Buyer App (BAP)->>Seller App (BPP): /issue (The BAP submits an issue to the BPP to report a problem with the confirmed ride order, specifying the complaint category, order details, and expected resolution timeline for grievance management.)
  Seller App (BPP)-->>Buyer App (BAP): /on_issue (The BPP sends an on issue callback to the BAP to confirm its acceptance of the issue resolution and specify the remedial actions taken to address the reported problem.)
  Buyer App (BAP)->>Seller App (BPP): /issue (The BAP raises an issue complaint with the BPP regarding the ride-hailing transaction, initiating the issue resolution process under ONDC's issue governance mechanism.)
```

## on_track_ride

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
  Seller App (BPP)-->>Buyer App (BAP): /on_confirm (order.status ACTIVE; fulfillment state RIDE_ASSIGNED)
  Seller App (BPP)-->>Buyer App (BAP): /on_track (unsolicited): tracking
  Seller App (BPP)-->>Buyer App (BAP): /on_status (unsolicited): order.status ACTIVE; fulfillment state RIDE_ENROUTE_PICKUP
  Buyer App (BAP)->>Seller App (BPP): /track (track order)
  rect rgb(191, 223, 255)
  Seller App (BPP)-->>Buyer App (BAP): /on_track (tracking)
  end
  Seller App (BPP)-->>Buyer App (BAP): /on_status (unsolicited): order.status ACTIVE; fulfillment state RIDE_ARRIVED_PICKUP
  Seller App (BPP)-->>Buyer App (BAP): /on_status (unsolicited): order.status ACTIVE; fulfillment state RIDE_STARTED
  Seller App (BPP)-->>Buyer App (BAP): /on_status (unsolicited): order.status ACTIVE; fulfillment state RIDE_ENDED
  Seller App (BPP)-->>Buyer App (BAP): /on_update (unsolicited): order.status ACTIVE; fulfillment state RIDE_ENDED
  Buyer App (BAP)->>Seller App (BPP): /status (order status)
  Seller App (BPP)-->>Buyer App (BAP): /on_status (order.status COMPLETED; fulfillment state RIDE_ENDED)
  Buyer App (BAP)->>Seller App (BPP): /issue (The BAP submits an issue to the BPP to formally lodge a complaint or grievance regarding the driver assignment or ride order.)
  Seller App (BPP)-->>Buyer App (BAP): /on_issue (The BPP acknowledges an issue opened by the BAP and responds with issue details, available actions, and resolution options as part of integrated grievance management.)
  Seller App (BPP)-->>Buyer App (BAP): /on_issue (unsolicited): The BPP proactively notifies the BAP of an issue or complaint that has arisen during the ride assignment, providing the issue details, category, and available resolution actions for the BAP to address.
  Buyer App (BAP)->>Seller App (BPP): /issue (The BAP raises a formal issue with the BPP to report and track a complaint regarding the assigned driver or service delivery. This initiates the integrated grievance management process, capturing complaint details, category, and expected resolution expectations.)
  Seller App (BPP)-->>Buyer App (BAP): /on_issue (The BPP responds to a BAP-reported issue with issue details, available actions, and proposed resolutions.)
  Seller App (BPP)-->>Buyer App (BAP): /on_issue (unsolicited): The BPP sends an unsolicited on issue notification to the BAP to communicate an issue or grievance related to the ride, including issue details and available actions for resolution.
  Buyer App (BAP)->>Seller App (BPP): /issue (The BAP submits an issue to the BPP to report a problem with the confirmed ride order, specifying the complaint category, order details, and expected resolution timeline for grievance management.)
  Seller App (BPP)-->>Buyer App (BAP): /on_issue (The BPP sends an on issue callback to the BAP to confirm its acceptance of the issue resolution and specify the remedial actions taken to address the reported problem.)
  Buyer App (BAP)->>Seller App (BPP): /issue (The BAP raises an issue complaint with the BPP regarding the ride-hailing transaction, initiating the issue resolution process under ONDC's issue governance mechanism.)
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
  Seller App (BPP)-->>Buyer App (BAP): /on_confirm (order.status ACTIVE; fulfillment state RIDE_ASSIGNED)
  Seller App (BPP)-->>Buyer App (BAP): /on_track (unsolicited): tracking
  Seller App (BPP)-->>Buyer App (BAP): /on_status (unsolicited): order.status ACTIVE; fulfillment state RIDE_ENROUTE_PICKUP
  Buyer App (BAP)->>Seller App (BPP): /track (track order)
  Seller App (BPP)-->>Buyer App (BAP): /on_track (tracking)
  rect rgb(191, 223, 255)
  Seller App (BPP)-->>Buyer App (BAP): /on_status (unsolicited): order.status ACTIVE; fulfillment state RIDE_ARRIVED_PICKUP
  end
  Seller App (BPP)-->>Buyer App (BAP): /on_status (unsolicited): order.status ACTIVE; fulfillment state RIDE_STARTED
  Seller App (BPP)-->>Buyer App (BAP): /on_status (unsolicited): order.status ACTIVE; fulfillment state RIDE_ENDED
  Seller App (BPP)-->>Buyer App (BAP): /on_update (unsolicited): order.status ACTIVE; fulfillment state RIDE_ENDED
  Buyer App (BAP)->>Seller App (BPP): /status (order status)
  Seller App (BPP)-->>Buyer App (BAP): /on_status (order.status COMPLETED; fulfillment state RIDE_ENDED)
  Buyer App (BAP)->>Seller App (BPP): /issue (The BAP submits an issue to the BPP to formally lodge a complaint or grievance regarding the driver assignment or ride order.)
  Seller App (BPP)-->>Buyer App (BAP): /on_issue (The BPP acknowledges an issue opened by the BAP and responds with issue details, available actions, and resolution options as part of integrated grievance management.)
  Seller App (BPP)-->>Buyer App (BAP): /on_issue (unsolicited): The BPP proactively notifies the BAP of an issue or complaint that has arisen during the ride assignment, providing the issue details, category, and available resolution actions for the BAP to address.
  Buyer App (BAP)->>Seller App (BPP): /issue (The BAP raises a formal issue with the BPP to report and track a complaint regarding the assigned driver or service delivery. This initiates the integrated grievance management process, capturing complaint details, category, and expected resolution expectations.)
  Seller App (BPP)-->>Buyer App (BAP): /on_issue (The BPP responds to a BAP-reported issue with issue details, available actions, and proposed resolutions.)
  Seller App (BPP)-->>Buyer App (BAP): /on_issue (unsolicited): The BPP sends an unsolicited on issue notification to the BAP to communicate an issue or grievance related to the ride, including issue details and available actions for resolution.
  Buyer App (BAP)->>Seller App (BPP): /issue (The BAP submits an issue to the BPP to report a problem with the confirmed ride order, specifying the complaint category, order details, and expected resolution timeline for grievance management.)
  Seller App (BPP)-->>Buyer App (BAP): /on_issue (The BPP sends an on issue callback to the BAP to confirm its acceptance of the issue resolution and specify the remedial actions taken to address the reported problem.)
  Buyer App (BAP)->>Seller App (BPP): /issue (The BAP raises an issue complaint with the BPP regarding the ride-hailing transaction, initiating the issue resolution process under ONDC's issue governance mechanism.)
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
  Seller App (BPP)-->>Buyer App (BAP): /on_confirm (order.status ACTIVE; fulfillment state RIDE_ASSIGNED)
  Seller App (BPP)-->>Buyer App (BAP): /on_track (unsolicited): tracking
  Seller App (BPP)-->>Buyer App (BAP): /on_status (unsolicited): order.status ACTIVE; fulfillment state RIDE_ENROUTE_PICKUP
  Buyer App (BAP)->>Seller App (BPP): /track (track order)
  Seller App (BPP)-->>Buyer App (BAP): /on_track (tracking)
  Seller App (BPP)-->>Buyer App (BAP): /on_status (unsolicited): order.status ACTIVE; fulfillment state RIDE_ARRIVED_PICKUP
  rect rgb(191, 223, 255)
  Seller App (BPP)-->>Buyer App (BAP): /on_status (unsolicited): order.status ACTIVE; fulfillment state RIDE_STARTED
  end
  Seller App (BPP)-->>Buyer App (BAP): /on_status (unsolicited): order.status ACTIVE; fulfillment state RIDE_ENDED
  Seller App (BPP)-->>Buyer App (BAP): /on_update (unsolicited): order.status ACTIVE; fulfillment state RIDE_ENDED
  Buyer App (BAP)->>Seller App (BPP): /status (order status)
  Seller App (BPP)-->>Buyer App (BAP): /on_status (order.status COMPLETED; fulfillment state RIDE_ENDED)
  Buyer App (BAP)->>Seller App (BPP): /issue (The BAP submits an issue to the BPP to formally lodge a complaint or grievance regarding the driver assignment or ride order.)
  Seller App (BPP)-->>Buyer App (BAP): /on_issue (The BPP acknowledges an issue opened by the BAP and responds with issue details, available actions, and resolution options as part of integrated grievance management.)
  Seller App (BPP)-->>Buyer App (BAP): /on_issue (unsolicited): The BPP proactively notifies the BAP of an issue or complaint that has arisen during the ride assignment, providing the issue details, category, and available resolution actions for the BAP to address.
  Buyer App (BAP)->>Seller App (BPP): /issue (The BAP raises a formal issue with the BPP to report and track a complaint regarding the assigned driver or service delivery. This initiates the integrated grievance management process, capturing complaint details, category, and expected resolution expectations.)
  Seller App (BPP)-->>Buyer App (BAP): /on_issue (The BPP responds to a BAP-reported issue with issue details, available actions, and proposed resolutions.)
  Seller App (BPP)-->>Buyer App (BAP): /on_issue (unsolicited): The BPP sends an unsolicited on issue notification to the BAP to communicate an issue or grievance related to the ride, including issue details and available actions for resolution.
  Buyer App (BAP)->>Seller App (BPP): /issue (The BAP submits an issue to the BPP to report a problem with the confirmed ride order, specifying the complaint category, order details, and expected resolution timeline for grievance management.)
  Seller App (BPP)-->>Buyer App (BAP): /on_issue (The BPP sends an on issue callback to the BAP to confirm its acceptance of the issue resolution and specify the remedial actions taken to address the reported problem.)
  Buyer App (BAP)->>Seller App (BPP): /issue (The BAP raises an issue complaint with the BPP regarding the ride-hailing transaction, initiating the issue resolution process under ONDC's issue governance mechanism.)
```

## on_status_ride_ended

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
  Seller App (BPP)-->>Buyer App (BAP): /on_confirm (order.status ACTIVE; fulfillment state RIDE_ASSIGNED)
  Seller App (BPP)-->>Buyer App (BAP): /on_track (unsolicited): tracking
  Seller App (BPP)-->>Buyer App (BAP): /on_status (unsolicited): order.status ACTIVE; fulfillment state RIDE_ENROUTE_PICKUP
  Buyer App (BAP)->>Seller App (BPP): /track (track order)
  Seller App (BPP)-->>Buyer App (BAP): /on_track (tracking)
  Seller App (BPP)-->>Buyer App (BAP): /on_status (unsolicited): order.status ACTIVE; fulfillment state RIDE_ARRIVED_PICKUP
  Seller App (BPP)-->>Buyer App (BAP): /on_status (unsolicited): order.status ACTIVE; fulfillment state RIDE_STARTED
  rect rgb(191, 223, 255)
  Seller App (BPP)-->>Buyer App (BAP): /on_status (unsolicited): order.status ACTIVE; fulfillment state RIDE_ENDED
  end
  Seller App (BPP)-->>Buyer App (BAP): /on_update (unsolicited): order.status ACTIVE; fulfillment state RIDE_ENDED
  Buyer App (BAP)->>Seller App (BPP): /status (order status)
  Seller App (BPP)-->>Buyer App (BAP): /on_status (order.status COMPLETED; fulfillment state RIDE_ENDED)
  Buyer App (BAP)->>Seller App (BPP): /issue (The BAP submits an issue to the BPP to formally lodge a complaint or grievance regarding the driver assignment or ride order.)
  Seller App (BPP)-->>Buyer App (BAP): /on_issue (The BPP acknowledges an issue opened by the BAP and responds with issue details, available actions, and resolution options as part of integrated grievance management.)
  Seller App (BPP)-->>Buyer App (BAP): /on_issue (unsolicited): The BPP proactively notifies the BAP of an issue or complaint that has arisen during the ride assignment, providing the issue details, category, and available resolution actions for the BAP to address.
  Buyer App (BAP)->>Seller App (BPP): /issue (The BAP raises a formal issue with the BPP to report and track a complaint regarding the assigned driver or service delivery. This initiates the integrated grievance management process, capturing complaint details, category, and expected resolution expectations.)
  Seller App (BPP)-->>Buyer App (BAP): /on_issue (The BPP responds to a BAP-reported issue with issue details, available actions, and proposed resolutions.)
  Seller App (BPP)-->>Buyer App (BAP): /on_issue (unsolicited): The BPP sends an unsolicited on issue notification to the BAP to communicate an issue or grievance related to the ride, including issue details and available actions for resolution.
  Buyer App (BAP)->>Seller App (BPP): /issue (The BAP submits an issue to the BPP to report a problem with the confirmed ride order, specifying the complaint category, order details, and expected resolution timeline for grievance management.)
  Seller App (BPP)-->>Buyer App (BAP): /on_issue (The BPP sends an on issue callback to the BAP to confirm its acceptance of the issue resolution and specify the remedial actions taken to address the reported problem.)
  Buyer App (BAP)->>Seller App (BPP): /issue (The BAP raises an issue complaint with the BPP regarding the ride-hailing transaction, initiating the issue resolution process under ONDC's issue governance mechanism.)
```

## on_update_fare_charges

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
  Seller App (BPP)-->>Buyer App (BAP): /on_confirm (order.status ACTIVE; fulfillment state RIDE_ASSIGNED)
  Seller App (BPP)-->>Buyer App (BAP): /on_track (unsolicited): tracking
  Seller App (BPP)-->>Buyer App (BAP): /on_status (unsolicited): order.status ACTIVE; fulfillment state RIDE_ENROUTE_PICKUP
  Buyer App (BAP)->>Seller App (BPP): /track (track order)
  Seller App (BPP)-->>Buyer App (BAP): /on_track (tracking)
  Seller App (BPP)-->>Buyer App (BAP): /on_status (unsolicited): order.status ACTIVE; fulfillment state RIDE_ARRIVED_PICKUP
  Seller App (BPP)-->>Buyer App (BAP): /on_status (unsolicited): order.status ACTIVE; fulfillment state RIDE_STARTED
  Seller App (BPP)-->>Buyer App (BAP): /on_status (unsolicited): order.status ACTIVE; fulfillment state RIDE_ENDED
  rect rgb(191, 223, 255)
  Seller App (BPP)-->>Buyer App (BAP): /on_update (unsolicited): order.status ACTIVE; fulfillment state RIDE_ENDED
  end
  Buyer App (BAP)->>Seller App (BPP): /status (order status)
  Seller App (BPP)-->>Buyer App (BAP): /on_status (order.status COMPLETED; fulfillment state RIDE_ENDED)
  Buyer App (BAP)->>Seller App (BPP): /issue (The BAP submits an issue to the BPP to formally lodge a complaint or grievance regarding the driver assignment or ride order.)
  Seller App (BPP)-->>Buyer App (BAP): /on_issue (The BPP acknowledges an issue opened by the BAP and responds with issue details, available actions, and resolution options as part of integrated grievance management.)
  Seller App (BPP)-->>Buyer App (BAP): /on_issue (unsolicited): The BPP proactively notifies the BAP of an issue or complaint that has arisen during the ride assignment, providing the issue details, category, and available resolution actions for the BAP to address.
  Buyer App (BAP)->>Seller App (BPP): /issue (The BAP raises a formal issue with the BPP to report and track a complaint regarding the assigned driver or service delivery. This initiates the integrated grievance management process, capturing complaint details, category, and expected resolution expectations.)
  Seller App (BPP)-->>Buyer App (BAP): /on_issue (The BPP responds to a BAP-reported issue with issue details, available actions, and proposed resolutions.)
  Seller App (BPP)-->>Buyer App (BAP): /on_issue (unsolicited): The BPP sends an unsolicited on issue notification to the BAP to communicate an issue or grievance related to the ride, including issue details and available actions for resolution.
  Buyer App (BAP)->>Seller App (BPP): /issue (The BAP submits an issue to the BPP to report a problem with the confirmed ride order, specifying the complaint category, order details, and expected resolution timeline for grievance management.)
  Seller App (BPP)-->>Buyer App (BAP): /on_issue (The BPP sends an on issue callback to the BAP to confirm its acceptance of the issue resolution and specify the remedial actions taken to address the reported problem.)
  Buyer App (BAP)->>Seller App (BPP): /issue (The BAP raises an issue complaint with the BPP regarding the ride-hailing transaction, initiating the issue resolution process under ONDC's issue governance mechanism.)
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
  Seller App (BPP)-->>Buyer App (BAP): /on_confirm (order.status ACTIVE; fulfillment state RIDE_ASSIGNED)
  Seller App (BPP)-->>Buyer App (BAP): /on_track (unsolicited): tracking
  Seller App (BPP)-->>Buyer App (BAP): /on_status (unsolicited): order.status ACTIVE; fulfillment state RIDE_ENROUTE_PICKUP
  Buyer App (BAP)->>Seller App (BPP): /track (track order)
  Seller App (BPP)-->>Buyer App (BAP): /on_track (tracking)
  Seller App (BPP)-->>Buyer App (BAP): /on_status (unsolicited): order.status ACTIVE; fulfillment state RIDE_ARRIVED_PICKUP
  Seller App (BPP)-->>Buyer App (BAP): /on_status (unsolicited): order.status ACTIVE; fulfillment state RIDE_STARTED
  Seller App (BPP)-->>Buyer App (BAP): /on_status (unsolicited): order.status ACTIVE; fulfillment state RIDE_ENDED
  Seller App (BPP)-->>Buyer App (BAP): /on_update (unsolicited): order.status ACTIVE; fulfillment state RIDE_ENDED
  rect rgb(191, 223, 255)
  Buyer App (BAP)->>Seller App (BPP): /status (order status)
  end
  Seller App (BPP)-->>Buyer App (BAP): /on_status (order.status COMPLETED; fulfillment state RIDE_ENDED)
  Buyer App (BAP)->>Seller App (BPP): /issue (The BAP submits an issue to the BPP to formally lodge a complaint or grievance regarding the driver assignment or ride order.)
  Seller App (BPP)-->>Buyer App (BAP): /on_issue (The BPP acknowledges an issue opened by the BAP and responds with issue details, available actions, and resolution options as part of integrated grievance management.)
  Seller App (BPP)-->>Buyer App (BAP): /on_issue (unsolicited): The BPP proactively notifies the BAP of an issue or complaint that has arisen during the ride assignment, providing the issue details, category, and available resolution actions for the BAP to address.
  Buyer App (BAP)->>Seller App (BPP): /issue (The BAP raises a formal issue with the BPP to report and track a complaint regarding the assigned driver or service delivery. This initiates the integrated grievance management process, capturing complaint details, category, and expected resolution expectations.)
  Seller App (BPP)-->>Buyer App (BAP): /on_issue (The BPP responds to a BAP-reported issue with issue details, available actions, and proposed resolutions.)
  Seller App (BPP)-->>Buyer App (BAP): /on_issue (unsolicited): The BPP sends an unsolicited on issue notification to the BAP to communicate an issue or grievance related to the ride, including issue details and available actions for resolution.
  Buyer App (BAP)->>Seller App (BPP): /issue (The BAP submits an issue to the BPP to report a problem with the confirmed ride order, specifying the complaint category, order details, and expected resolution timeline for grievance management.)
  Seller App (BPP)-->>Buyer App (BAP): /on_issue (The BPP sends an on issue callback to the BAP to confirm its acceptance of the issue resolution and specify the remedial actions taken to address the reported problem.)
  Buyer App (BAP)->>Seller App (BPP): /issue (The BAP raises an issue complaint with the BPP regarding the ride-hailing transaction, initiating the issue resolution process under ONDC's issue governance mechanism.)
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
  Seller App (BPP)-->>Buyer App (BAP): /on_confirm (order.status ACTIVE; fulfillment state RIDE_ASSIGNED)
  Seller App (BPP)-->>Buyer App (BAP): /on_track (unsolicited): tracking
  Seller App (BPP)-->>Buyer App (BAP): /on_status (unsolicited): order.status ACTIVE; fulfillment state RIDE_ENROUTE_PICKUP
  Buyer App (BAP)->>Seller App (BPP): /track (track order)
  Seller App (BPP)-->>Buyer App (BAP): /on_track (tracking)
  Seller App (BPP)-->>Buyer App (BAP): /on_status (unsolicited): order.status ACTIVE; fulfillment state RIDE_ARRIVED_PICKUP
  Seller App (BPP)-->>Buyer App (BAP): /on_status (unsolicited): order.status ACTIVE; fulfillment state RIDE_STARTED
  Seller App (BPP)-->>Buyer App (BAP): /on_status (unsolicited): order.status ACTIVE; fulfillment state RIDE_ENDED
  Seller App (BPP)-->>Buyer App (BAP): /on_update (unsolicited): order.status ACTIVE; fulfillment state RIDE_ENDED
  Buyer App (BAP)->>Seller App (BPP): /status (order status)
  rect rgb(191, 223, 255)
  Seller App (BPP)-->>Buyer App (BAP): /on_status (order.status COMPLETED; fulfillment state RIDE_ENDED)
  end
  Buyer App (BAP)->>Seller App (BPP): /issue (The BAP submits an issue to the BPP to formally lodge a complaint or grievance regarding the driver assignment or ride order.)
  Seller App (BPP)-->>Buyer App (BAP): /on_issue (The BPP acknowledges an issue opened by the BAP and responds with issue details, available actions, and resolution options as part of integrated grievance management.)
  Seller App (BPP)-->>Buyer App (BAP): /on_issue (unsolicited): The BPP proactively notifies the BAP of an issue or complaint that has arisen during the ride assignment, providing the issue details, category, and available resolution actions for the BAP to address.
  Buyer App (BAP)->>Seller App (BPP): /issue (The BAP raises a formal issue with the BPP to report and track a complaint regarding the assigned driver or service delivery. This initiates the integrated grievance management process, capturing complaint details, category, and expected resolution expectations.)
  Seller App (BPP)-->>Buyer App (BAP): /on_issue (The BPP responds to a BAP-reported issue with issue details, available actions, and proposed resolutions.)
  Seller App (BPP)-->>Buyer App (BAP): /on_issue (unsolicited): The BPP sends an unsolicited on issue notification to the BAP to communicate an issue or grievance related to the ride, including issue details and available actions for resolution.
  Buyer App (BAP)->>Seller App (BPP): /issue (The BAP submits an issue to the BPP to report a problem with the confirmed ride order, specifying the complaint category, order details, and expected resolution timeline for grievance management.)
  Seller App (BPP)-->>Buyer App (BAP): /on_issue (The BPP sends an on issue callback to the BAP to confirm its acceptance of the issue resolution and specify the remedial actions taken to address the reported problem.)
  Buyer App (BAP)->>Seller App (BPP): /issue (The BAP raises an issue complaint with the BPP regarding the ride-hailing transaction, initiating the issue resolution process under ONDC's issue governance mechanism.)
```

## issue_open

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
  Seller App (BPP)-->>Buyer App (BAP): /on_confirm (order.status ACTIVE; fulfillment state RIDE_ASSIGNED)
  Seller App (BPP)-->>Buyer App (BAP): /on_track (unsolicited): tracking
  Seller App (BPP)-->>Buyer App (BAP): /on_status (unsolicited): order.status ACTIVE; fulfillment state RIDE_ENROUTE_PICKUP
  Buyer App (BAP)->>Seller App (BPP): /track (track order)
  Seller App (BPP)-->>Buyer App (BAP): /on_track (tracking)
  Seller App (BPP)-->>Buyer App (BAP): /on_status (unsolicited): order.status ACTIVE; fulfillment state RIDE_ARRIVED_PICKUP
  Seller App (BPP)-->>Buyer App (BAP): /on_status (unsolicited): order.status ACTIVE; fulfillment state RIDE_STARTED
  Seller App (BPP)-->>Buyer App (BAP): /on_status (unsolicited): order.status ACTIVE; fulfillment state RIDE_ENDED
  Seller App (BPP)-->>Buyer App (BAP): /on_update (unsolicited): order.status ACTIVE; fulfillment state RIDE_ENDED
  Buyer App (BAP)->>Seller App (BPP): /status (order status)
  Seller App (BPP)-->>Buyer App (BAP): /on_status (order.status COMPLETED; fulfillment state RIDE_ENDED)
  rect rgb(191, 223, 255)
  Buyer App (BAP)->>Seller App (BPP): /issue (The BAP submits an issue to the BPP to formally lodge a complaint or grievance regarding the driver assignment or ride order.)
  end
  Seller App (BPP)-->>Buyer App (BAP): /on_issue (The BPP acknowledges an issue opened by the BAP and responds with issue details, available actions, and resolution options as part of integrated grievance management.)
  Seller App (BPP)-->>Buyer App (BAP): /on_issue (unsolicited): The BPP proactively notifies the BAP of an issue or complaint that has arisen during the ride assignment, providing the issue details, category, and available resolution actions for the BAP to address.
  Buyer App (BAP)->>Seller App (BPP): /issue (The BAP raises a formal issue with the BPP to report and track a complaint regarding the assigned driver or service delivery. This initiates the integrated grievance management process, capturing complaint details, category, and expected resolution expectations.)
  Seller App (BPP)-->>Buyer App (BAP): /on_issue (The BPP responds to a BAP-reported issue with issue details, available actions, and proposed resolutions.)
  Seller App (BPP)-->>Buyer App (BAP): /on_issue (unsolicited): The BPP sends an unsolicited on issue notification to the BAP to communicate an issue or grievance related to the ride, including issue details and available actions for resolution.
  Buyer App (BAP)->>Seller App (BPP): /issue (The BAP submits an issue to the BPP to report a problem with the confirmed ride order, specifying the complaint category, order details, and expected resolution timeline for grievance management.)
  Seller App (BPP)-->>Buyer App (BAP): /on_issue (The BPP sends an on issue callback to the BAP to confirm its acceptance of the issue resolution and specify the remedial actions taken to address the reported problem.)
  Buyer App (BAP)->>Seller App (BPP): /issue (The BAP raises an issue complaint with the BPP regarding the ride-hailing transaction, initiating the issue resolution process under ONDC's issue governance mechanism.)
```

## on_issue_processing

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
  Seller App (BPP)-->>Buyer App (BAP): /on_confirm (order.status ACTIVE; fulfillment state RIDE_ASSIGNED)
  Seller App (BPP)-->>Buyer App (BAP): /on_track (unsolicited): tracking
  Seller App (BPP)-->>Buyer App (BAP): /on_status (unsolicited): order.status ACTIVE; fulfillment state RIDE_ENROUTE_PICKUP
  Buyer App (BAP)->>Seller App (BPP): /track (track order)
  Seller App (BPP)-->>Buyer App (BAP): /on_track (tracking)
  Seller App (BPP)-->>Buyer App (BAP): /on_status (unsolicited): order.status ACTIVE; fulfillment state RIDE_ARRIVED_PICKUP
  Seller App (BPP)-->>Buyer App (BAP): /on_status (unsolicited): order.status ACTIVE; fulfillment state RIDE_STARTED
  Seller App (BPP)-->>Buyer App (BAP): /on_status (unsolicited): order.status ACTIVE; fulfillment state RIDE_ENDED
  Seller App (BPP)-->>Buyer App (BAP): /on_update (unsolicited): order.status ACTIVE; fulfillment state RIDE_ENDED
  Buyer App (BAP)->>Seller App (BPP): /status (order status)
  Seller App (BPP)-->>Buyer App (BAP): /on_status (order.status COMPLETED; fulfillment state RIDE_ENDED)
  Buyer App (BAP)->>Seller App (BPP): /issue (The BAP submits an issue to the BPP to formally lodge a complaint or grievance regarding the driver assignment or ride order.)
  rect rgb(191, 223, 255)
  Seller App (BPP)-->>Buyer App (BAP): /on_issue (The BPP acknowledges an issue opened by the BAP and responds with issue details, available actions, and resolution options as part of integrated grievance management.)
  end
  Seller App (BPP)-->>Buyer App (BAP): /on_issue (unsolicited): The BPP proactively notifies the BAP of an issue or complaint that has arisen during the ride assignment, providing the issue details, category, and available resolution actions for the BAP to address.
  Buyer App (BAP)->>Seller App (BPP): /issue (The BAP raises a formal issue with the BPP to report and track a complaint regarding the assigned driver or service delivery. This initiates the integrated grievance management process, capturing complaint details, category, and expected resolution expectations.)
  Seller App (BPP)-->>Buyer App (BAP): /on_issue (The BPP responds to a BAP-reported issue with issue details, available actions, and proposed resolutions.)
  Seller App (BPP)-->>Buyer App (BAP): /on_issue (unsolicited): The BPP sends an unsolicited on issue notification to the BAP to communicate an issue or grievance related to the ride, including issue details and available actions for resolution.
  Buyer App (BAP)->>Seller App (BPP): /issue (The BAP submits an issue to the BPP to report a problem with the confirmed ride order, specifying the complaint category, order details, and expected resolution timeline for grievance management.)
  Seller App (BPP)-->>Buyer App (BAP): /on_issue (The BPP sends an on issue callback to the BAP to confirm its acceptance of the issue resolution and specify the remedial actions taken to address the reported problem.)
  Buyer App (BAP)->>Seller App (BPP): /issue (The BAP raises an issue complaint with the BPP regarding the ride-hailing transaction, initiating the issue resolution process under ONDC's issue governance mechanism.)
```

## on_issue_need_more_info

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
  Seller App (BPP)-->>Buyer App (BAP): /on_confirm (order.status ACTIVE; fulfillment state RIDE_ASSIGNED)
  Seller App (BPP)-->>Buyer App (BAP): /on_track (unsolicited): tracking
  Seller App (BPP)-->>Buyer App (BAP): /on_status (unsolicited): order.status ACTIVE; fulfillment state RIDE_ENROUTE_PICKUP
  Buyer App (BAP)->>Seller App (BPP): /track (track order)
  Seller App (BPP)-->>Buyer App (BAP): /on_track (tracking)
  Seller App (BPP)-->>Buyer App (BAP): /on_status (unsolicited): order.status ACTIVE; fulfillment state RIDE_ARRIVED_PICKUP
  Seller App (BPP)-->>Buyer App (BAP): /on_status (unsolicited): order.status ACTIVE; fulfillment state RIDE_STARTED
  Seller App (BPP)-->>Buyer App (BAP): /on_status (unsolicited): order.status ACTIVE; fulfillment state RIDE_ENDED
  Seller App (BPP)-->>Buyer App (BAP): /on_update (unsolicited): order.status ACTIVE; fulfillment state RIDE_ENDED
  Buyer App (BAP)->>Seller App (BPP): /status (order status)
  Seller App (BPP)-->>Buyer App (BAP): /on_status (order.status COMPLETED; fulfillment state RIDE_ENDED)
  Buyer App (BAP)->>Seller App (BPP): /issue (The BAP submits an issue to the BPP to formally lodge a complaint or grievance regarding the driver assignment or ride order.)
  Seller App (BPP)-->>Buyer App (BAP): /on_issue (The BPP acknowledges an issue opened by the BAP and responds with issue details, available actions, and resolution options as part of integrated grievance management.)
  rect rgb(191, 223, 255)
  Seller App (BPP)-->>Buyer App (BAP): /on_issue (unsolicited): The BPP proactively notifies the BAP of an issue or complaint that has arisen during the ride assignment, providing the issue details, category, and available resolution actions for the BAP to address.
  end
  Buyer App (BAP)->>Seller App (BPP): /issue (The BAP raises a formal issue with the BPP to report and track a complaint regarding the assigned driver or service delivery. This initiates the integrated grievance management process, capturing complaint details, category, and expected resolution expectations.)
  Seller App (BPP)-->>Buyer App (BAP): /on_issue (The BPP responds to a BAP-reported issue with issue details, available actions, and proposed resolutions.)
  Seller App (BPP)-->>Buyer App (BAP): /on_issue (unsolicited): The BPP sends an unsolicited on issue notification to the BAP to communicate an issue or grievance related to the ride, including issue details and available actions for resolution.
  Buyer App (BAP)->>Seller App (BPP): /issue (The BAP submits an issue to the BPP to report a problem with the confirmed ride order, specifying the complaint category, order details, and expected resolution timeline for grievance management.)
  Seller App (BPP)-->>Buyer App (BAP): /on_issue (The BPP sends an on issue callback to the BAP to confirm its acceptance of the issue resolution and specify the remedial actions taken to address the reported problem.)
  Buyer App (BAP)->>Seller App (BPP): /issue (The BAP raises an issue complaint with the BPP regarding the ride-hailing transaction, initiating the issue resolution process under ONDC's issue governance mechanism.)
```

## issue_info_provided

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
  Seller App (BPP)-->>Buyer App (BAP): /on_confirm (order.status ACTIVE; fulfillment state RIDE_ASSIGNED)
  Seller App (BPP)-->>Buyer App (BAP): /on_track (unsolicited): tracking
  Seller App (BPP)-->>Buyer App (BAP): /on_status (unsolicited): order.status ACTIVE; fulfillment state RIDE_ENROUTE_PICKUP
  Buyer App (BAP)->>Seller App (BPP): /track (track order)
  Seller App (BPP)-->>Buyer App (BAP): /on_track (tracking)
  Seller App (BPP)-->>Buyer App (BAP): /on_status (unsolicited): order.status ACTIVE; fulfillment state RIDE_ARRIVED_PICKUP
  Seller App (BPP)-->>Buyer App (BAP): /on_status (unsolicited): order.status ACTIVE; fulfillment state RIDE_STARTED
  Seller App (BPP)-->>Buyer App (BAP): /on_status (unsolicited): order.status ACTIVE; fulfillment state RIDE_ENDED
  Seller App (BPP)-->>Buyer App (BAP): /on_update (unsolicited): order.status ACTIVE; fulfillment state RIDE_ENDED
  Buyer App (BAP)->>Seller App (BPP): /status (order status)
  Seller App (BPP)-->>Buyer App (BAP): /on_status (order.status COMPLETED; fulfillment state RIDE_ENDED)
  Buyer App (BAP)->>Seller App (BPP): /issue (The BAP submits an issue to the BPP to formally lodge a complaint or grievance regarding the driver assignment or ride order.)
  Seller App (BPP)-->>Buyer App (BAP): /on_issue (The BPP acknowledges an issue opened by the BAP and responds with issue details, available actions, and resolution options as part of integrated grievance management.)
  Seller App (BPP)-->>Buyer App (BAP): /on_issue (unsolicited): The BPP proactively notifies the BAP of an issue or complaint that has arisen during the ride assignment, providing the issue details, category, and available resolution actions for the BAP to address.
  rect rgb(191, 223, 255)
  Buyer App (BAP)->>Seller App (BPP): /issue (The BAP raises a formal issue with the BPP to report and track a complaint regarding the assigned driver or service delivery. This initiates the integrated grievance management process, capturing complaint details, category, and expected resolution expectations.)
  end
  Seller App (BPP)-->>Buyer App (BAP): /on_issue (The BPP responds to a BAP-reported issue with issue details, available actions, and proposed resolutions.)
  Seller App (BPP)-->>Buyer App (BAP): /on_issue (unsolicited): The BPP sends an unsolicited on issue notification to the BAP to communicate an issue or grievance related to the ride, including issue details and available actions for resolution.
  Buyer App (BAP)->>Seller App (BPP): /issue (The BAP submits an issue to the BPP to report a problem with the confirmed ride order, specifying the complaint category, order details, and expected resolution timeline for grievance management.)
  Seller App (BPP)-->>Buyer App (BAP): /on_issue (The BPP sends an on issue callback to the BAP to confirm its acceptance of the issue resolution and specify the remedial actions taken to address the reported problem.)
  Buyer App (BAP)->>Seller App (BPP): /issue (The BAP raises an issue complaint with the BPP regarding the ride-hailing transaction, initiating the issue resolution process under ONDC's issue governance mechanism.)
```

## on_issue_provided

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
  Seller App (BPP)-->>Buyer App (BAP): /on_confirm (order.status ACTIVE; fulfillment state RIDE_ASSIGNED)
  Seller App (BPP)-->>Buyer App (BAP): /on_track (unsolicited): tracking
  Seller App (BPP)-->>Buyer App (BAP): /on_status (unsolicited): order.status ACTIVE; fulfillment state RIDE_ENROUTE_PICKUP
  Buyer App (BAP)->>Seller App (BPP): /track (track order)
  Seller App (BPP)-->>Buyer App (BAP): /on_track (tracking)
  Seller App (BPP)-->>Buyer App (BAP): /on_status (unsolicited): order.status ACTIVE; fulfillment state RIDE_ARRIVED_PICKUP
  Seller App (BPP)-->>Buyer App (BAP): /on_status (unsolicited): order.status ACTIVE; fulfillment state RIDE_STARTED
  Seller App (BPP)-->>Buyer App (BAP): /on_status (unsolicited): order.status ACTIVE; fulfillment state RIDE_ENDED
  Seller App (BPP)-->>Buyer App (BAP): /on_update (unsolicited): order.status ACTIVE; fulfillment state RIDE_ENDED
  Buyer App (BAP)->>Seller App (BPP): /status (order status)
  Seller App (BPP)-->>Buyer App (BAP): /on_status (order.status COMPLETED; fulfillment state RIDE_ENDED)
  Buyer App (BAP)->>Seller App (BPP): /issue (The BAP submits an issue to the BPP to formally lodge a complaint or grievance regarding the driver assignment or ride order.)
  Seller App (BPP)-->>Buyer App (BAP): /on_issue (The BPP acknowledges an issue opened by the BAP and responds with issue details, available actions, and resolution options as part of integrated grievance management.)
  Seller App (BPP)-->>Buyer App (BAP): /on_issue (unsolicited): The BPP proactively notifies the BAP of an issue or complaint that has arisen during the ride assignment, providing the issue details, category, and available resolution actions for the BAP to address.
  Buyer App (BAP)->>Seller App (BPP): /issue (The BAP raises a formal issue with the BPP to report and track a complaint regarding the assigned driver or service delivery. This initiates the integrated grievance management process, capturing complaint details, category, and expected resolution expectations.)
  rect rgb(191, 223, 255)
  Seller App (BPP)-->>Buyer App (BAP): /on_issue (The BPP responds to a BAP-reported issue with issue details, available actions, and proposed resolutions.)
  end
  Seller App (BPP)-->>Buyer App (BAP): /on_issue (unsolicited): The BPP sends an unsolicited on issue notification to the BAP to communicate an issue or grievance related to the ride, including issue details and available actions for resolution.
  Buyer App (BAP)->>Seller App (BPP): /issue (The BAP submits an issue to the BPP to report a problem with the confirmed ride order, specifying the complaint category, order details, and expected resolution timeline for grievance management.)
  Seller App (BPP)-->>Buyer App (BAP): /on_issue (The BPP sends an on issue callback to the BAP to confirm its acceptance of the issue resolution and specify the remedial actions taken to address the reported problem.)
  Buyer App (BAP)->>Seller App (BPP): /issue (The BAP raises an issue complaint with the BPP regarding the ride-hailing transaction, initiating the issue resolution process under ONDC's issue governance mechanism.)
```

## on_issue_resolution

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
  Seller App (BPP)-->>Buyer App (BAP): /on_confirm (order.status ACTIVE; fulfillment state RIDE_ASSIGNED)
  Seller App (BPP)-->>Buyer App (BAP): /on_track (unsolicited): tracking
  Seller App (BPP)-->>Buyer App (BAP): /on_status (unsolicited): order.status ACTIVE; fulfillment state RIDE_ENROUTE_PICKUP
  Buyer App (BAP)->>Seller App (BPP): /track (track order)
  Seller App (BPP)-->>Buyer App (BAP): /on_track (tracking)
  Seller App (BPP)-->>Buyer App (BAP): /on_status (unsolicited): order.status ACTIVE; fulfillment state RIDE_ARRIVED_PICKUP
  Seller App (BPP)-->>Buyer App (BAP): /on_status (unsolicited): order.status ACTIVE; fulfillment state RIDE_STARTED
  Seller App (BPP)-->>Buyer App (BAP): /on_status (unsolicited): order.status ACTIVE; fulfillment state RIDE_ENDED
  Seller App (BPP)-->>Buyer App (BAP): /on_update (unsolicited): order.status ACTIVE; fulfillment state RIDE_ENDED
  Buyer App (BAP)->>Seller App (BPP): /status (order status)
  Seller App (BPP)-->>Buyer App (BAP): /on_status (order.status COMPLETED; fulfillment state RIDE_ENDED)
  Buyer App (BAP)->>Seller App (BPP): /issue (The BAP submits an issue to the BPP to formally lodge a complaint or grievance regarding the driver assignment or ride order.)
  Seller App (BPP)-->>Buyer App (BAP): /on_issue (The BPP acknowledges an issue opened by the BAP and responds with issue details, available actions, and resolution options as part of integrated grievance management.)
  Seller App (BPP)-->>Buyer App (BAP): /on_issue (unsolicited): The BPP proactively notifies the BAP of an issue or complaint that has arisen during the ride assignment, providing the issue details, category, and available resolution actions for the BAP to address.
  Buyer App (BAP)->>Seller App (BPP): /issue (The BAP raises a formal issue with the BPP to report and track a complaint regarding the assigned driver or service delivery. This initiates the integrated grievance management process, capturing complaint details, category, and expected resolution expectations.)
  Seller App (BPP)-->>Buyer App (BAP): /on_issue (The BPP responds to a BAP-reported issue with issue details, available actions, and proposed resolutions.)
  rect rgb(191, 223, 255)
  Seller App (BPP)-->>Buyer App (BAP): /on_issue (unsolicited): The BPP sends an unsolicited on issue notification to the BAP to communicate an issue or grievance related to the ride, including issue details and available actions for resolution.
  end
  Buyer App (BAP)->>Seller App (BPP): /issue (The BAP submits an issue to the BPP to report a problem with the confirmed ride order, specifying the complaint category, order details, and expected resolution timeline for grievance management.)
  Seller App (BPP)-->>Buyer App (BAP): /on_issue (The BPP sends an on issue callback to the BAP to confirm its acceptance of the issue resolution and specify the remedial actions taken to address the reported problem.)
  Buyer App (BAP)->>Seller App (BPP): /issue (The BAP raises an issue complaint with the BPP regarding the ride-hailing transaction, initiating the issue resolution process under ONDC's issue governance mechanism.)
```

## issue_resolution_accept

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
  Seller App (BPP)-->>Buyer App (BAP): /on_confirm (order.status ACTIVE; fulfillment state RIDE_ASSIGNED)
  Seller App (BPP)-->>Buyer App (BAP): /on_track (unsolicited): tracking
  Seller App (BPP)-->>Buyer App (BAP): /on_status (unsolicited): order.status ACTIVE; fulfillment state RIDE_ENROUTE_PICKUP
  Buyer App (BAP)->>Seller App (BPP): /track (track order)
  Seller App (BPP)-->>Buyer App (BAP): /on_track (tracking)
  Seller App (BPP)-->>Buyer App (BAP): /on_status (unsolicited): order.status ACTIVE; fulfillment state RIDE_ARRIVED_PICKUP
  Seller App (BPP)-->>Buyer App (BAP): /on_status (unsolicited): order.status ACTIVE; fulfillment state RIDE_STARTED
  Seller App (BPP)-->>Buyer App (BAP): /on_status (unsolicited): order.status ACTIVE; fulfillment state RIDE_ENDED
  Seller App (BPP)-->>Buyer App (BAP): /on_update (unsolicited): order.status ACTIVE; fulfillment state RIDE_ENDED
  Buyer App (BAP)->>Seller App (BPP): /status (order status)
  Seller App (BPP)-->>Buyer App (BAP): /on_status (order.status COMPLETED; fulfillment state RIDE_ENDED)
  Buyer App (BAP)->>Seller App (BPP): /issue (The BAP submits an issue to the BPP to formally lodge a complaint or grievance regarding the driver assignment or ride order.)
  Seller App (BPP)-->>Buyer App (BAP): /on_issue (The BPP acknowledges an issue opened by the BAP and responds with issue details, available actions, and resolution options as part of integrated grievance management.)
  Seller App (BPP)-->>Buyer App (BAP): /on_issue (unsolicited): The BPP proactively notifies the BAP of an issue or complaint that has arisen during the ride assignment, providing the issue details, category, and available resolution actions for the BAP to address.
  Buyer App (BAP)->>Seller App (BPP): /issue (The BAP raises a formal issue with the BPP to report and track a complaint regarding the assigned driver or service delivery. This initiates the integrated grievance management process, capturing complaint details, category, and expected resolution expectations.)
  Seller App (BPP)-->>Buyer App (BAP): /on_issue (The BPP responds to a BAP-reported issue with issue details, available actions, and proposed resolutions.)
  Seller App (BPP)-->>Buyer App (BAP): /on_issue (unsolicited): The BPP sends an unsolicited on issue notification to the BAP to communicate an issue or grievance related to the ride, including issue details and available actions for resolution.
  rect rgb(191, 223, 255)
  Buyer App (BAP)->>Seller App (BPP): /issue (The BAP submits an issue to the BPP to report a problem with the confirmed ride order, specifying the complaint category, order details, and expected resolution timeline for grievance management.)
  end
  Seller App (BPP)-->>Buyer App (BAP): /on_issue (The BPP sends an on issue callback to the BAP to confirm its acceptance of the issue resolution and specify the remedial actions taken to address the reported problem.)
  Buyer App (BAP)->>Seller App (BPP): /issue (The BAP raises an issue complaint with the BPP regarding the ride-hailing transaction, initiating the issue resolution process under ONDC's issue governance mechanism.)
```

## on_issue_resolved

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
  Seller App (BPP)-->>Buyer App (BAP): /on_confirm (order.status ACTIVE; fulfillment state RIDE_ASSIGNED)
  Seller App (BPP)-->>Buyer App (BAP): /on_track (unsolicited): tracking
  Seller App (BPP)-->>Buyer App (BAP): /on_status (unsolicited): order.status ACTIVE; fulfillment state RIDE_ENROUTE_PICKUP
  Buyer App (BAP)->>Seller App (BPP): /track (track order)
  Seller App (BPP)-->>Buyer App (BAP): /on_track (tracking)
  Seller App (BPP)-->>Buyer App (BAP): /on_status (unsolicited): order.status ACTIVE; fulfillment state RIDE_ARRIVED_PICKUP
  Seller App (BPP)-->>Buyer App (BAP): /on_status (unsolicited): order.status ACTIVE; fulfillment state RIDE_STARTED
  Seller App (BPP)-->>Buyer App (BAP): /on_status (unsolicited): order.status ACTIVE; fulfillment state RIDE_ENDED
  Seller App (BPP)-->>Buyer App (BAP): /on_update (unsolicited): order.status ACTIVE; fulfillment state RIDE_ENDED
  Buyer App (BAP)->>Seller App (BPP): /status (order status)
  Seller App (BPP)-->>Buyer App (BAP): /on_status (order.status COMPLETED; fulfillment state RIDE_ENDED)
  Buyer App (BAP)->>Seller App (BPP): /issue (The BAP submits an issue to the BPP to formally lodge a complaint or grievance regarding the driver assignment or ride order.)
  Seller App (BPP)-->>Buyer App (BAP): /on_issue (The BPP acknowledges an issue opened by the BAP and responds with issue details, available actions, and resolution options as part of integrated grievance management.)
  Seller App (BPP)-->>Buyer App (BAP): /on_issue (unsolicited): The BPP proactively notifies the BAP of an issue or complaint that has arisen during the ride assignment, providing the issue details, category, and available resolution actions for the BAP to address.
  Buyer App (BAP)->>Seller App (BPP): /issue (The BAP raises a formal issue with the BPP to report and track a complaint regarding the assigned driver or service delivery. This initiates the integrated grievance management process, capturing complaint details, category, and expected resolution expectations.)
  Seller App (BPP)-->>Buyer App (BAP): /on_issue (The BPP responds to a BAP-reported issue with issue details, available actions, and proposed resolutions.)
  Seller App (BPP)-->>Buyer App (BAP): /on_issue (unsolicited): The BPP sends an unsolicited on issue notification to the BAP to communicate an issue or grievance related to the ride, including issue details and available actions for resolution.
  Buyer App (BAP)->>Seller App (BPP): /issue (The BAP submits an issue to the BPP to report a problem with the confirmed ride order, specifying the complaint category, order details, and expected resolution timeline for grievance management.)
  rect rgb(191, 223, 255)
  Seller App (BPP)-->>Buyer App (BAP): /on_issue (The BPP sends an on issue callback to the BAP to confirm its acceptance of the issue resolution and specify the remedial actions taken to address the reported problem.)
  end
  Buyer App (BAP)->>Seller App (BPP): /issue (The BAP raises an issue complaint with the BPP regarding the ride-hailing transaction, initiating the issue resolution process under ONDC's issue governance mechanism.)
```

## issue_close

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
  Seller App (BPP)-->>Buyer App (BAP): /on_confirm (order.status ACTIVE; fulfillment state RIDE_ASSIGNED)
  Seller App (BPP)-->>Buyer App (BAP): /on_track (unsolicited): tracking
  Seller App (BPP)-->>Buyer App (BAP): /on_status (unsolicited): order.status ACTIVE; fulfillment state RIDE_ENROUTE_PICKUP
  Buyer App (BAP)->>Seller App (BPP): /track (track order)
  Seller App (BPP)-->>Buyer App (BAP): /on_track (tracking)
  Seller App (BPP)-->>Buyer App (BAP): /on_status (unsolicited): order.status ACTIVE; fulfillment state RIDE_ARRIVED_PICKUP
  Seller App (BPP)-->>Buyer App (BAP): /on_status (unsolicited): order.status ACTIVE; fulfillment state RIDE_STARTED
  Seller App (BPP)-->>Buyer App (BAP): /on_status (unsolicited): order.status ACTIVE; fulfillment state RIDE_ENDED
  Seller App (BPP)-->>Buyer App (BAP): /on_update (unsolicited): order.status ACTIVE; fulfillment state RIDE_ENDED
  Buyer App (BAP)->>Seller App (BPP): /status (order status)
  Seller App (BPP)-->>Buyer App (BAP): /on_status (order.status COMPLETED; fulfillment state RIDE_ENDED)
  Buyer App (BAP)->>Seller App (BPP): /issue (The BAP submits an issue to the BPP to formally lodge a complaint or grievance regarding the driver assignment or ride order.)
  Seller App (BPP)-->>Buyer App (BAP): /on_issue (The BPP acknowledges an issue opened by the BAP and responds with issue details, available actions, and resolution options as part of integrated grievance management.)
  Seller App (BPP)-->>Buyer App (BAP): /on_issue (unsolicited): The BPP proactively notifies the BAP of an issue or complaint that has arisen during the ride assignment, providing the issue details, category, and available resolution actions for the BAP to address.
  Buyer App (BAP)->>Seller App (BPP): /issue (The BAP raises a formal issue with the BPP to report and track a complaint regarding the assigned driver or service delivery. This initiates the integrated grievance management process, capturing complaint details, category, and expected resolution expectations.)
  Seller App (BPP)-->>Buyer App (BAP): /on_issue (The BPP responds to a BAP-reported issue with issue details, available actions, and proposed resolutions.)
  Seller App (BPP)-->>Buyer App (BAP): /on_issue (unsolicited): The BPP sends an unsolicited on issue notification to the BAP to communicate an issue or grievance related to the ride, including issue details and available actions for resolution.
  Buyer App (BAP)->>Seller App (BPP): /issue (The BAP submits an issue to the BPP to report a problem with the confirmed ride order, specifying the complaint category, order details, and expected resolution timeline for grievance management.)
  Seller App (BPP)-->>Buyer App (BAP): /on_issue (The BPP sends an on issue callback to the BAP to confirm its acceptance of the issue resolution and specify the remedial actions taken to address the reported problem.)
  rect rgb(191, 223, 255)
  Buyer App (BAP)->>Seller App (BPP): /issue (The BAP raises an issue complaint with the BPP regarding the ride-hailing transaction, initiating the issue resolution process under ONDC's issue governance mechanism.)
  end
```

# OnDemand_Assign_driver_on_onconfirm_With_IGM_No_Action(v-2.0.0) — Sequence Diagrams

Internal data file consumed by the Developer Guide's "Sequence Diagram" tab (API Walkthrough).
Not meant to be shown as its own docs page — the frontend filters this slug out of the Use Case
Brief / Additional Resources / Changelog tab lists and instead looks up the section matching the
selected API call's `action_id` (the `##` heading below) to render that step's diagram.

One `## <action_id>` heading per step of `OnDemand_Assign_driver_on_onconfirm_With_IGM_No_Action_v-2_0_0_.yaml` (Ride-hailing), in that flow's own step order, each followed by its Mermaid `sequenceDiagram`: the whole flow, with that call's own message(s) highlighted — same convention as the other domains' per-step sequence-diagram docs.

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
  Buyer App (BAP)->>Seller App (BPP): /issue (The BAP files an issue with the BPP to formally register a complaint or grievance regarding the ride transaction.)
  Seller App (BPP)-->>Buyer App (BAP): /on_issue (The BPP delivers the on issue callback containing issue details, assigned actions, and resolution options in response to an issue raised by the BAP on the confirmed ride order.)
  Seller App (BPP)-->>Buyer App (BAP): /on_issue (unsolicited): The BPP sends an unsolicited on issue notification to the BAP reporting a problem or complaint that has arisen during the ride fulfillment, providing issue details and available resolution actions for the BAP to address. This step captures the issue payload and tracks the actions and resolutions available to resolve the reported concern.
  Buyer App (BAP)->>Seller App (BPP): /issue (The BAP submits an issue to the BPP to formally report a complaint about the order, specifying the issue category, description, and expected resolution timeline.)
  Seller App (BPP)-->>Buyer App (BAP): /on_issue (The BPP acknowledges and responds to an issue raised by the BAP, confirming the provider's resolution or corrective actions.)
  Buyer App (BAP)->>Seller App (BPP): /issue (The BAP raises an issue with the BPP to formally register a customer complaint or problem during the ride-hailing fulfillment, initiating the integrated grievance resolution process.)
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
  Buyer App (BAP)->>Seller App (BPP): /issue (The BAP files an issue with the BPP to formally register a complaint or grievance regarding the ride transaction.)
  Seller App (BPP)-->>Buyer App (BAP): /on_issue (The BPP delivers the on issue callback containing issue details, assigned actions, and resolution options in response to an issue raised by the BAP on the confirmed ride order.)
  Seller App (BPP)-->>Buyer App (BAP): /on_issue (unsolicited): The BPP sends an unsolicited on issue notification to the BAP reporting a problem or complaint that has arisen during the ride fulfillment, providing issue details and available resolution actions for the BAP to address. This step captures the issue payload and tracks the actions and resolutions available to resolve the reported concern.
  Buyer App (BAP)->>Seller App (BPP): /issue (The BAP submits an issue to the BPP to formally report a complaint about the order, specifying the issue category, description, and expected resolution timeline.)
  Seller App (BPP)-->>Buyer App (BAP): /on_issue (The BPP acknowledges and responds to an issue raised by the BAP, confirming the provider's resolution or corrective actions.)
  Buyer App (BAP)->>Seller App (BPP): /issue (The BAP raises an issue with the BPP to formally register a customer complaint or problem during the ride-hailing fulfillment, initiating the integrated grievance resolution process.)
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
  Buyer App (BAP)->>Seller App (BPP): /issue (The BAP files an issue with the BPP to formally register a complaint or grievance regarding the ride transaction.)
  Seller App (BPP)-->>Buyer App (BAP): /on_issue (The BPP delivers the on issue callback containing issue details, assigned actions, and resolution options in response to an issue raised by the BAP on the confirmed ride order.)
  Seller App (BPP)-->>Buyer App (BAP): /on_issue (unsolicited): The BPP sends an unsolicited on issue notification to the BAP reporting a problem or complaint that has arisen during the ride fulfillment, providing issue details and available resolution actions for the BAP to address. This step captures the issue payload and tracks the actions and resolutions available to resolve the reported concern.
  Buyer App (BAP)->>Seller App (BPP): /issue (The BAP submits an issue to the BPP to formally report a complaint about the order, specifying the issue category, description, and expected resolution timeline.)
  Seller App (BPP)-->>Buyer App (BAP): /on_issue (The BPP acknowledges and responds to an issue raised by the BAP, confirming the provider's resolution or corrective actions.)
  Buyer App (BAP)->>Seller App (BPP): /issue (The BAP raises an issue with the BPP to formally register a customer complaint or problem during the ride-hailing fulfillment, initiating the integrated grievance resolution process.)
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
  Buyer App (BAP)->>Seller App (BPP): /issue (The BAP files an issue with the BPP to formally register a complaint or grievance regarding the ride transaction.)
  Seller App (BPP)-->>Buyer App (BAP): /on_issue (The BPP delivers the on issue callback containing issue details, assigned actions, and resolution options in response to an issue raised by the BAP on the confirmed ride order.)
  Seller App (BPP)-->>Buyer App (BAP): /on_issue (unsolicited): The BPP sends an unsolicited on issue notification to the BAP reporting a problem or complaint that has arisen during the ride fulfillment, providing issue details and available resolution actions for the BAP to address. This step captures the issue payload and tracks the actions and resolutions available to resolve the reported concern.
  Buyer App (BAP)->>Seller App (BPP): /issue (The BAP submits an issue to the BPP to formally report a complaint about the order, specifying the issue category, description, and expected resolution timeline.)
  Seller App (BPP)-->>Buyer App (BAP): /on_issue (The BPP acknowledges and responds to an issue raised by the BAP, confirming the provider's resolution or corrective actions.)
  Buyer App (BAP)->>Seller App (BPP): /issue (The BAP raises an issue with the BPP to formally register a customer complaint or problem during the ride-hailing fulfillment, initiating the integrated grievance resolution process.)
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
  Buyer App (BAP)->>Seller App (BPP): /issue (The BAP files an issue with the BPP to formally register a complaint or grievance regarding the ride transaction.)
  Seller App (BPP)-->>Buyer App (BAP): /on_issue (The BPP delivers the on issue callback containing issue details, assigned actions, and resolution options in response to an issue raised by the BAP on the confirmed ride order.)
  Seller App (BPP)-->>Buyer App (BAP): /on_issue (unsolicited): The BPP sends an unsolicited on issue notification to the BAP reporting a problem or complaint that has arisen during the ride fulfillment, providing issue details and available resolution actions for the BAP to address. This step captures the issue payload and tracks the actions and resolutions available to resolve the reported concern.
  Buyer App (BAP)->>Seller App (BPP): /issue (The BAP submits an issue to the BPP to formally report a complaint about the order, specifying the issue category, description, and expected resolution timeline.)
  Seller App (BPP)-->>Buyer App (BAP): /on_issue (The BPP acknowledges and responds to an issue raised by the BAP, confirming the provider's resolution or corrective actions.)
  Buyer App (BAP)->>Seller App (BPP): /issue (The BAP raises an issue with the BPP to formally register a customer complaint or problem during the ride-hailing fulfillment, initiating the integrated grievance resolution process.)
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
  Buyer App (BAP)->>Seller App (BPP): /issue (The BAP files an issue with the BPP to formally register a complaint or grievance regarding the ride transaction.)
  Seller App (BPP)-->>Buyer App (BAP): /on_issue (The BPP delivers the on issue callback containing issue details, assigned actions, and resolution options in response to an issue raised by the BAP on the confirmed ride order.)
  Seller App (BPP)-->>Buyer App (BAP): /on_issue (unsolicited): The BPP sends an unsolicited on issue notification to the BAP reporting a problem or complaint that has arisen during the ride fulfillment, providing issue details and available resolution actions for the BAP to address. This step captures the issue payload and tracks the actions and resolutions available to resolve the reported concern.
  Buyer App (BAP)->>Seller App (BPP): /issue (The BAP submits an issue to the BPP to formally report a complaint about the order, specifying the issue category, description, and expected resolution timeline.)
  Seller App (BPP)-->>Buyer App (BAP): /on_issue (The BPP acknowledges and responds to an issue raised by the BAP, confirming the provider's resolution or corrective actions.)
  Buyer App (BAP)->>Seller App (BPP): /issue (The BAP raises an issue with the BPP to formally register a customer complaint or problem during the ride-hailing fulfillment, initiating the integrated grievance resolution process.)
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
  Buyer App (BAP)->>Seller App (BPP): /issue (The BAP files an issue with the BPP to formally register a complaint or grievance regarding the ride transaction.)
  Seller App (BPP)-->>Buyer App (BAP): /on_issue (The BPP delivers the on issue callback containing issue details, assigned actions, and resolution options in response to an issue raised by the BAP on the confirmed ride order.)
  Seller App (BPP)-->>Buyer App (BAP): /on_issue (unsolicited): The BPP sends an unsolicited on issue notification to the BAP reporting a problem or complaint that has arisen during the ride fulfillment, providing issue details and available resolution actions for the BAP to address. This step captures the issue payload and tracks the actions and resolutions available to resolve the reported concern.
  Buyer App (BAP)->>Seller App (BPP): /issue (The BAP submits an issue to the BPP to formally report a complaint about the order, specifying the issue category, description, and expected resolution timeline.)
  Seller App (BPP)-->>Buyer App (BAP): /on_issue (The BPP acknowledges and responds to an issue raised by the BAP, confirming the provider's resolution or corrective actions.)
  Buyer App (BAP)->>Seller App (BPP): /issue (The BAP raises an issue with the BPP to formally register a customer complaint or problem during the ride-hailing fulfillment, initiating the integrated grievance resolution process.)
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
  Buyer App (BAP)->>Seller App (BPP): /issue (The BAP files an issue with the BPP to formally register a complaint or grievance regarding the ride transaction.)
  Seller App (BPP)-->>Buyer App (BAP): /on_issue (The BPP delivers the on issue callback containing issue details, assigned actions, and resolution options in response to an issue raised by the BAP on the confirmed ride order.)
  Seller App (BPP)-->>Buyer App (BAP): /on_issue (unsolicited): The BPP sends an unsolicited on issue notification to the BAP reporting a problem or complaint that has arisen during the ride fulfillment, providing issue details and available resolution actions for the BAP to address. This step captures the issue payload and tracks the actions and resolutions available to resolve the reported concern.
  Buyer App (BAP)->>Seller App (BPP): /issue (The BAP submits an issue to the BPP to formally report a complaint about the order, specifying the issue category, description, and expected resolution timeline.)
  Seller App (BPP)-->>Buyer App (BAP): /on_issue (The BPP acknowledges and responds to an issue raised by the BAP, confirming the provider's resolution or corrective actions.)
  Buyer App (BAP)->>Seller App (BPP): /issue (The BAP raises an issue with the BPP to formally register a customer complaint or problem during the ride-hailing fulfillment, initiating the integrated grievance resolution process.)
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
  Buyer App (BAP)->>Seller App (BPP): /issue (The BAP files an issue with the BPP to formally register a complaint or grievance regarding the ride transaction.)
  Seller App (BPP)-->>Buyer App (BAP): /on_issue (The BPP delivers the on issue callback containing issue details, assigned actions, and resolution options in response to an issue raised by the BAP on the confirmed ride order.)
  Seller App (BPP)-->>Buyer App (BAP): /on_issue (unsolicited): The BPP sends an unsolicited on issue notification to the BAP reporting a problem or complaint that has arisen during the ride fulfillment, providing issue details and available resolution actions for the BAP to address. This step captures the issue payload and tracks the actions and resolutions available to resolve the reported concern.
  Buyer App (BAP)->>Seller App (BPP): /issue (The BAP submits an issue to the BPP to formally report a complaint about the order, specifying the issue category, description, and expected resolution timeline.)
  Seller App (BPP)-->>Buyer App (BAP): /on_issue (The BPP acknowledges and responds to an issue raised by the BAP, confirming the provider's resolution or corrective actions.)
  Buyer App (BAP)->>Seller App (BPP): /issue (The BAP raises an issue with the BPP to formally register a customer complaint or problem during the ride-hailing fulfillment, initiating the integrated grievance resolution process.)
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
  Buyer App (BAP)->>Seller App (BPP): /issue (The BAP files an issue with the BPP to formally register a complaint or grievance regarding the ride transaction.)
  Seller App (BPP)-->>Buyer App (BAP): /on_issue (The BPP delivers the on issue callback containing issue details, assigned actions, and resolution options in response to an issue raised by the BAP on the confirmed ride order.)
  Seller App (BPP)-->>Buyer App (BAP): /on_issue (unsolicited): The BPP sends an unsolicited on issue notification to the BAP reporting a problem or complaint that has arisen during the ride fulfillment, providing issue details and available resolution actions for the BAP to address. This step captures the issue payload and tracks the actions and resolutions available to resolve the reported concern.
  Buyer App (BAP)->>Seller App (BPP): /issue (The BAP submits an issue to the BPP to formally report a complaint about the order, specifying the issue category, description, and expected resolution timeline.)
  Seller App (BPP)-->>Buyer App (BAP): /on_issue (The BPP acknowledges and responds to an issue raised by the BAP, confirming the provider's resolution or corrective actions.)
  Buyer App (BAP)->>Seller App (BPP): /issue (The BAP raises an issue with the BPP to formally register a customer complaint or problem during the ride-hailing fulfillment, initiating the integrated grievance resolution process.)
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
  Buyer App (BAP)->>Seller App (BPP): /issue (The BAP files an issue with the BPP to formally register a complaint or grievance regarding the ride transaction.)
  Seller App (BPP)-->>Buyer App (BAP): /on_issue (The BPP delivers the on issue callback containing issue details, assigned actions, and resolution options in response to an issue raised by the BAP on the confirmed ride order.)
  Seller App (BPP)-->>Buyer App (BAP): /on_issue (unsolicited): The BPP sends an unsolicited on issue notification to the BAP reporting a problem or complaint that has arisen during the ride fulfillment, providing issue details and available resolution actions for the BAP to address. This step captures the issue payload and tracks the actions and resolutions available to resolve the reported concern.
  Buyer App (BAP)->>Seller App (BPP): /issue (The BAP submits an issue to the BPP to formally report a complaint about the order, specifying the issue category, description, and expected resolution timeline.)
  Seller App (BPP)-->>Buyer App (BAP): /on_issue (The BPP acknowledges and responds to an issue raised by the BAP, confirming the provider's resolution or corrective actions.)
  Buyer App (BAP)->>Seller App (BPP): /issue (The BAP raises an issue with the BPP to formally register a customer complaint or problem during the ride-hailing fulfillment, initiating the integrated grievance resolution process.)
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
  Buyer App (BAP)->>Seller App (BPP): /issue (The BAP files an issue with the BPP to formally register a complaint or grievance regarding the ride transaction.)
  Seller App (BPP)-->>Buyer App (BAP): /on_issue (The BPP delivers the on issue callback containing issue details, assigned actions, and resolution options in response to an issue raised by the BAP on the confirmed ride order.)
  Seller App (BPP)-->>Buyer App (BAP): /on_issue (unsolicited): The BPP sends an unsolicited on issue notification to the BAP reporting a problem or complaint that has arisen during the ride fulfillment, providing issue details and available resolution actions for the BAP to address. This step captures the issue payload and tracks the actions and resolutions available to resolve the reported concern.
  Buyer App (BAP)->>Seller App (BPP): /issue (The BAP submits an issue to the BPP to formally report a complaint about the order, specifying the issue category, description, and expected resolution timeline.)
  Seller App (BPP)-->>Buyer App (BAP): /on_issue (The BPP acknowledges and responds to an issue raised by the BAP, confirming the provider's resolution or corrective actions.)
  Buyer App (BAP)->>Seller App (BPP): /issue (The BAP raises an issue with the BPP to formally register a customer complaint or problem during the ride-hailing fulfillment, initiating the integrated grievance resolution process.)
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
  Buyer App (BAP)->>Seller App (BPP): /issue (The BAP files an issue with the BPP to formally register a complaint or grievance regarding the ride transaction.)
  Seller App (BPP)-->>Buyer App (BAP): /on_issue (The BPP delivers the on issue callback containing issue details, assigned actions, and resolution options in response to an issue raised by the BAP on the confirmed ride order.)
  Seller App (BPP)-->>Buyer App (BAP): /on_issue (unsolicited): The BPP sends an unsolicited on issue notification to the BAP reporting a problem or complaint that has arisen during the ride fulfillment, providing issue details and available resolution actions for the BAP to address. This step captures the issue payload and tracks the actions and resolutions available to resolve the reported concern.
  Buyer App (BAP)->>Seller App (BPP): /issue (The BAP submits an issue to the BPP to formally report a complaint about the order, specifying the issue category, description, and expected resolution timeline.)
  Seller App (BPP)-->>Buyer App (BAP): /on_issue (The BPP acknowledges and responds to an issue raised by the BAP, confirming the provider's resolution or corrective actions.)
  Buyer App (BAP)->>Seller App (BPP): /issue (The BAP raises an issue with the BPP to formally register a customer complaint or problem during the ride-hailing fulfillment, initiating the integrated grievance resolution process.)
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
  Buyer App (BAP)->>Seller App (BPP): /issue (The BAP files an issue with the BPP to formally register a complaint or grievance regarding the ride transaction.)
  Seller App (BPP)-->>Buyer App (BAP): /on_issue (The BPP delivers the on issue callback containing issue details, assigned actions, and resolution options in response to an issue raised by the BAP on the confirmed ride order.)
  Seller App (BPP)-->>Buyer App (BAP): /on_issue (unsolicited): The BPP sends an unsolicited on issue notification to the BAP reporting a problem or complaint that has arisen during the ride fulfillment, providing issue details and available resolution actions for the BAP to address. This step captures the issue payload and tracks the actions and resolutions available to resolve the reported concern.
  Buyer App (BAP)->>Seller App (BPP): /issue (The BAP submits an issue to the BPP to formally report a complaint about the order, specifying the issue category, description, and expected resolution timeline.)
  Seller App (BPP)-->>Buyer App (BAP): /on_issue (The BPP acknowledges and responds to an issue raised by the BAP, confirming the provider's resolution or corrective actions.)
  Buyer App (BAP)->>Seller App (BPP): /issue (The BAP raises an issue with the BPP to formally register a customer complaint or problem during the ride-hailing fulfillment, initiating the integrated grievance resolution process.)
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
  Buyer App (BAP)->>Seller App (BPP): /issue (The BAP files an issue with the BPP to formally register a complaint or grievance regarding the ride transaction.)
  Seller App (BPP)-->>Buyer App (BAP): /on_issue (The BPP delivers the on issue callback containing issue details, assigned actions, and resolution options in response to an issue raised by the BAP on the confirmed ride order.)
  Seller App (BPP)-->>Buyer App (BAP): /on_issue (unsolicited): The BPP sends an unsolicited on issue notification to the BAP reporting a problem or complaint that has arisen during the ride fulfillment, providing issue details and available resolution actions for the BAP to address. This step captures the issue payload and tracks the actions and resolutions available to resolve the reported concern.
  Buyer App (BAP)->>Seller App (BPP): /issue (The BAP submits an issue to the BPP to formally report a complaint about the order, specifying the issue category, description, and expected resolution timeline.)
  Seller App (BPP)-->>Buyer App (BAP): /on_issue (The BPP acknowledges and responds to an issue raised by the BAP, confirming the provider's resolution or corrective actions.)
  Buyer App (BAP)->>Seller App (BPP): /issue (The BAP raises an issue with the BPP to formally register a customer complaint or problem during the ride-hailing fulfillment, initiating the integrated grievance resolution process.)
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
  Buyer App (BAP)->>Seller App (BPP): /issue (The BAP files an issue with the BPP to formally register a complaint or grievance regarding the ride transaction.)
  Seller App (BPP)-->>Buyer App (BAP): /on_issue (The BPP delivers the on issue callback containing issue details, assigned actions, and resolution options in response to an issue raised by the BAP on the confirmed ride order.)
  Seller App (BPP)-->>Buyer App (BAP): /on_issue (unsolicited): The BPP sends an unsolicited on issue notification to the BAP reporting a problem or complaint that has arisen during the ride fulfillment, providing issue details and available resolution actions for the BAP to address. This step captures the issue payload and tracks the actions and resolutions available to resolve the reported concern.
  Buyer App (BAP)->>Seller App (BPP): /issue (The BAP submits an issue to the BPP to formally report a complaint about the order, specifying the issue category, description, and expected resolution timeline.)
  Seller App (BPP)-->>Buyer App (BAP): /on_issue (The BPP acknowledges and responds to an issue raised by the BAP, confirming the provider's resolution or corrective actions.)
  Buyer App (BAP)->>Seller App (BPP): /issue (The BAP raises an issue with the BPP to formally register a customer complaint or problem during the ride-hailing fulfillment, initiating the integrated grievance resolution process.)
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
  Buyer App (BAP)->>Seller App (BPP): /issue (The BAP files an issue with the BPP to formally register a complaint or grievance regarding the ride transaction.)
  Seller App (BPP)-->>Buyer App (BAP): /on_issue (The BPP delivers the on issue callback containing issue details, assigned actions, and resolution options in response to an issue raised by the BAP on the confirmed ride order.)
  Seller App (BPP)-->>Buyer App (BAP): /on_issue (unsolicited): The BPP sends an unsolicited on issue notification to the BAP reporting a problem or complaint that has arisen during the ride fulfillment, providing issue details and available resolution actions for the BAP to address. This step captures the issue payload and tracks the actions and resolutions available to resolve the reported concern.
  Buyer App (BAP)->>Seller App (BPP): /issue (The BAP submits an issue to the BPP to formally report a complaint about the order, specifying the issue category, description, and expected resolution timeline.)
  Seller App (BPP)-->>Buyer App (BAP): /on_issue (The BPP acknowledges and responds to an issue raised by the BAP, confirming the provider's resolution or corrective actions.)
  Buyer App (BAP)->>Seller App (BPP): /issue (The BAP raises an issue with the BPP to formally register a customer complaint or problem during the ride-hailing fulfillment, initiating the integrated grievance resolution process.)
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
  Buyer App (BAP)->>Seller App (BPP): /issue (The BAP files an issue with the BPP to formally register a complaint or grievance regarding the ride transaction.)
  Seller App (BPP)-->>Buyer App (BAP): /on_issue (The BPP delivers the on issue callback containing issue details, assigned actions, and resolution options in response to an issue raised by the BAP on the confirmed ride order.)
  Seller App (BPP)-->>Buyer App (BAP): /on_issue (unsolicited): The BPP sends an unsolicited on issue notification to the BAP reporting a problem or complaint that has arisen during the ride fulfillment, providing issue details and available resolution actions for the BAP to address. This step captures the issue payload and tracks the actions and resolutions available to resolve the reported concern.
  Buyer App (BAP)->>Seller App (BPP): /issue (The BAP submits an issue to the BPP to formally report a complaint about the order, specifying the issue category, description, and expected resolution timeline.)
  Seller App (BPP)-->>Buyer App (BAP): /on_issue (The BPP acknowledges and responds to an issue raised by the BAP, confirming the provider's resolution or corrective actions.)
  Buyer App (BAP)->>Seller App (BPP): /issue (The BAP raises an issue with the BPP to formally register a customer complaint or problem during the ride-hailing fulfillment, initiating the integrated grievance resolution process.)
```

## issue_open_2

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
  Buyer App (BAP)->>Seller App (BPP): /issue (The BAP files an issue with the BPP to formally register a complaint or grievance regarding the ride transaction.)
  end
  Seller App (BPP)-->>Buyer App (BAP): /on_issue (The BPP delivers the on issue callback containing issue details, assigned actions, and resolution options in response to an issue raised by the BAP on the confirmed ride order.)
  Seller App (BPP)-->>Buyer App (BAP): /on_issue (unsolicited): The BPP sends an unsolicited on issue notification to the BAP reporting a problem or complaint that has arisen during the ride fulfillment, providing issue details and available resolution actions for the BAP to address. This step captures the issue payload and tracks the actions and resolutions available to resolve the reported concern.
  Buyer App (BAP)->>Seller App (BPP): /issue (The BAP submits an issue to the BPP to formally report a complaint about the order, specifying the issue category, description, and expected resolution timeline.)
  Seller App (BPP)-->>Buyer App (BAP): /on_issue (The BPP acknowledges and responds to an issue raised by the BAP, confirming the provider's resolution or corrective actions.)
  Buyer App (BAP)->>Seller App (BPP): /issue (The BAP raises an issue with the BPP to formally register a customer complaint or problem during the ride-hailing fulfillment, initiating the integrated grievance resolution process.)
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
  Buyer App (BAP)->>Seller App (BPP): /issue (The BAP files an issue with the BPP to formally register a complaint or grievance regarding the ride transaction.)
  rect rgb(191, 223, 255)
  Seller App (BPP)-->>Buyer App (BAP): /on_issue (The BPP delivers the on issue callback containing issue details, assigned actions, and resolution options in response to an issue raised by the BAP on the confirmed ride order.)
  end
  Seller App (BPP)-->>Buyer App (BAP): /on_issue (unsolicited): The BPP sends an unsolicited on issue notification to the BAP reporting a problem or complaint that has arisen during the ride fulfillment, providing issue details and available resolution actions for the BAP to address. This step captures the issue payload and tracks the actions and resolutions available to resolve the reported concern.
  Buyer App (BAP)->>Seller App (BPP): /issue (The BAP submits an issue to the BPP to formally report a complaint about the order, specifying the issue category, description, and expected resolution timeline.)
  Seller App (BPP)-->>Buyer App (BAP): /on_issue (The BPP acknowledges and responds to an issue raised by the BAP, confirming the provider's resolution or corrective actions.)
  Buyer App (BAP)->>Seller App (BPP): /issue (The BAP raises an issue with the BPP to formally register a customer complaint or problem during the ride-hailing fulfillment, initiating the integrated grievance resolution process.)
```

## on_issue_resolution_igm_3

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
  Buyer App (BAP)->>Seller App (BPP): /issue (The BAP files an issue with the BPP to formally register a complaint or grievance regarding the ride transaction.)
  Seller App (BPP)-->>Buyer App (BAP): /on_issue (The BPP delivers the on issue callback containing issue details, assigned actions, and resolution options in response to an issue raised by the BAP on the confirmed ride order.)
  rect rgb(191, 223, 255)
  Seller App (BPP)-->>Buyer App (BAP): /on_issue (unsolicited): The BPP sends an unsolicited on issue notification to the BAP reporting a problem or complaint that has arisen during the ride fulfillment, providing issue details and available resolution actions for the BAP to address. This step captures the issue payload and tracks the actions and resolutions available to resolve the reported concern.
  end
  Buyer App (BAP)->>Seller App (BPP): /issue (The BAP submits an issue to the BPP to formally report a complaint about the order, specifying the issue category, description, and expected resolution timeline.)
  Seller App (BPP)-->>Buyer App (BAP): /on_issue (The BPP acknowledges and responds to an issue raised by the BAP, confirming the provider's resolution or corrective actions.)
  Buyer App (BAP)->>Seller App (BPP): /issue (The BAP raises an issue with the BPP to formally register a customer complaint or problem during the ride-hailing fulfillment, initiating the integrated grievance resolution process.)
```

## issue_resolution_accept_igm_3

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
  Buyer App (BAP)->>Seller App (BPP): /issue (The BAP files an issue with the BPP to formally register a complaint or grievance regarding the ride transaction.)
  Seller App (BPP)-->>Buyer App (BAP): /on_issue (The BPP delivers the on issue callback containing issue details, assigned actions, and resolution options in response to an issue raised by the BAP on the confirmed ride order.)
  Seller App (BPP)-->>Buyer App (BAP): /on_issue (unsolicited): The BPP sends an unsolicited on issue notification to the BAP reporting a problem or complaint that has arisen during the ride fulfillment, providing issue details and available resolution actions for the BAP to address. This step captures the issue payload and tracks the actions and resolutions available to resolve the reported concern.
  rect rgb(191, 223, 255)
  Buyer App (BAP)->>Seller App (BPP): /issue (The BAP submits an issue to the BPP to formally report a complaint about the order, specifying the issue category, description, and expected resolution timeline.)
  end
  Seller App (BPP)-->>Buyer App (BAP): /on_issue (The BPP acknowledges and responds to an issue raised by the BAP, confirming the provider's resolution or corrective actions.)
  Buyer App (BAP)->>Seller App (BPP): /issue (The BAP raises an issue with the BPP to formally register a customer complaint or problem during the ride-hailing fulfillment, initiating the integrated grievance resolution process.)
```

## on_issue_resolved_igm_3

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
  Buyer App (BAP)->>Seller App (BPP): /issue (The BAP files an issue with the BPP to formally register a complaint or grievance regarding the ride transaction.)
  Seller App (BPP)-->>Buyer App (BAP): /on_issue (The BPP delivers the on issue callback containing issue details, assigned actions, and resolution options in response to an issue raised by the BAP on the confirmed ride order.)
  Seller App (BPP)-->>Buyer App (BAP): /on_issue (unsolicited): The BPP sends an unsolicited on issue notification to the BAP reporting a problem or complaint that has arisen during the ride fulfillment, providing issue details and available resolution actions for the BAP to address. This step captures the issue payload and tracks the actions and resolutions available to resolve the reported concern.
  Buyer App (BAP)->>Seller App (BPP): /issue (The BAP submits an issue to the BPP to formally report a complaint about the order, specifying the issue category, description, and expected resolution timeline.)
  rect rgb(191, 223, 255)
  Seller App (BPP)-->>Buyer App (BAP): /on_issue (The BPP acknowledges and responds to an issue raised by the BAP, confirming the provider's resolution or corrective actions.)
  end
  Buyer App (BAP)->>Seller App (BPP): /issue (The BAP raises an issue with the BPP to formally register a customer complaint or problem during the ride-hailing fulfillment, initiating the integrated grievance resolution process.)
```

## issue_close_igm_3

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
  Buyer App (BAP)->>Seller App (BPP): /issue (The BAP files an issue with the BPP to formally register a complaint or grievance regarding the ride transaction.)
  Seller App (BPP)-->>Buyer App (BAP): /on_issue (The BPP delivers the on issue callback containing issue details, assigned actions, and resolution options in response to an issue raised by the BAP on the confirmed ride order.)
  Seller App (BPP)-->>Buyer App (BAP): /on_issue (unsolicited): The BPP sends an unsolicited on issue notification to the BAP reporting a problem or complaint that has arisen during the ride fulfillment, providing issue details and available resolution actions for the BAP to address. This step captures the issue payload and tracks the actions and resolutions available to resolve the reported concern.
  Buyer App (BAP)->>Seller App (BPP): /issue (The BAP submits an issue to the BPP to formally report a complaint about the order, specifying the issue category, description, and expected resolution timeline.)
  Seller App (BPP)-->>Buyer App (BAP): /on_issue (The BPP acknowledges and responds to an issue raised by the BAP, confirming the provider's resolution or corrective actions.)
  rect rgb(191, 223, 255)
  Buyer App (BAP)->>Seller App (BPP): /issue (The BAP raises an issue with the BPP to formally register a customer complaint or problem during the ride-hailing fulfillment, initiating the integrated grievance resolution process.)
  end
```

# Order to Confirm to Fulfillment (City Code) — Sequence Diagrams

Internal data file consumed by the Developer Guide's "Sequence Diagram" tab (API Walkthrough).
Not meant to be shown as its own docs page — the frontend filters this slug out of the Use Case
Brief / Additional Resources / Changelog tab lists and instead looks up the section matching the
selected API call's `action_id` (the `##` heading below) to render that step's diagram.

One `## <action_id>` heading per step of `Order_to_Confirm_to_Fulfillment__City_Code_.yaml`, in that flow's own step order, each
followed by its Mermaid `sequenceDiagram`.

## select_5

```mermaid
sequenceDiagram
    title Order to Confirm to Fulfillment (City Code)
    autonumber
    actor User as Traveler / Guest
    participant BAP as Accommodation Booking App (BAP)
    participant BG as ONDC Gateway
    participant BPP as Hotel Provider (BPP)

    rect rgb(191, 223, 255)
    BAP->>BPP: POST /select
    BPP-->>BAP: 200 OK (ACK)
    end
    BPP->>BAP: POST /on_select
    BAP-->>BPP: 200 OK (ACK)
    BAP->>BPP: POST /init
    BPP-->>BAP: 200 OK (ACK)
    BPP->>BAP: POST /on_init
    BAP-->>BPP: 200 OK (ACK)
    BAP->>BPP: POST /confirm
    BPP-->>BAP: 200 OK (ACK)
    BPP->>BAP: POST /on_confirm
    BAP-->>BPP: 200 OK (ACK)
    BAP->>User: Display confirmed booking and hotel voucher
    BAP->>BPP: POST /status
    BPP-->>BAP: 200 OK (ACK)
    BPP->>BAP: POST /on_status
    BAP-->>BPP: 200 OK (ACK)
    Note over BPP: Unsolicited notification broadcast
    BPP->>BAP: POST /on_status
    BAP-->>BPP: 200 OK (ACK)
```

## on_select_5

```mermaid
sequenceDiagram
    title Order to Confirm to Fulfillment (City Code)
    autonumber
    actor User as Traveler / Guest
    participant BAP as Accommodation Booking App (BAP)
    participant BG as ONDC Gateway
    participant BPP as Hotel Provider (BPP)

    BAP->>BPP: POST /select
    BPP-->>BAP: 200 OK (ACK)
    rect rgb(191, 223, 255)
    BPP->>BAP: POST /on_select
    BAP-->>BPP: 200 OK (ACK)
    end
    BAP->>BPP: POST /init
    BPP-->>BAP: 200 OK (ACK)
    BPP->>BAP: POST /on_init
    BAP-->>BPP: 200 OK (ACK)
    BAP->>BPP: POST /confirm
    BPP-->>BAP: 200 OK (ACK)
    BPP->>BAP: POST /on_confirm
    BAP-->>BPP: 200 OK (ACK)
    BAP->>User: Display confirmed booking and hotel voucher
    BAP->>BPP: POST /status
    BPP-->>BAP: 200 OK (ACK)
    BPP->>BAP: POST /on_status
    BAP-->>BPP: 200 OK (ACK)
    Note over BPP: Unsolicited notification broadcast
    BPP->>BAP: POST /on_status
    BAP-->>BPP: 200 OK (ACK)
```

## init_5

```mermaid
sequenceDiagram
    title Order to Confirm to Fulfillment (City Code)
    autonumber
    actor User as Traveler / Guest
    participant BAP as Accommodation Booking App (BAP)
    participant BG as ONDC Gateway
    participant BPP as Hotel Provider (BPP)

    BAP->>BPP: POST /select
    BPP-->>BAP: 200 OK (ACK)
    BPP->>BAP: POST /on_select
    BAP-->>BPP: 200 OK (ACK)
    rect rgb(191, 223, 255)
    BAP->>BPP: POST /init
    BPP-->>BAP: 200 OK (ACK)
    end
    BPP->>BAP: POST /on_init
    BAP-->>BPP: 200 OK (ACK)
    BAP->>BPP: POST /confirm
    BPP-->>BAP: 200 OK (ACK)
    BPP->>BAP: POST /on_confirm
    BAP-->>BPP: 200 OK (ACK)
    BAP->>User: Display confirmed booking and hotel voucher
    BAP->>BPP: POST /status
    BPP-->>BAP: 200 OK (ACK)
    BPP->>BAP: POST /on_status
    BAP-->>BPP: 200 OK (ACK)
    Note over BPP: Unsolicited notification broadcast
    BPP->>BAP: POST /on_status
    BAP-->>BPP: 200 OK (ACK)
```

## on_init_5

```mermaid
sequenceDiagram
    title Order to Confirm to Fulfillment (City Code)
    autonumber
    actor User as Traveler / Guest
    participant BAP as Accommodation Booking App (BAP)
    participant BG as ONDC Gateway
    participant BPP as Hotel Provider (BPP)

    BAP->>BPP: POST /select
    BPP-->>BAP: 200 OK (ACK)
    BPP->>BAP: POST /on_select
    BAP-->>BPP: 200 OK (ACK)
    BAP->>BPP: POST /init
    BPP-->>BAP: 200 OK (ACK)
    rect rgb(191, 223, 255)
    BPP->>BAP: POST /on_init
    BAP-->>BPP: 200 OK (ACK)
    end
    BAP->>BPP: POST /confirm
    BPP-->>BAP: 200 OK (ACK)
    BPP->>BAP: POST /on_confirm
    BAP-->>BPP: 200 OK (ACK)
    BAP->>User: Display confirmed booking and hotel voucher
    BAP->>BPP: POST /status
    BPP-->>BAP: 200 OK (ACK)
    BPP->>BAP: POST /on_status
    BAP-->>BPP: 200 OK (ACK)
    Note over BPP: Unsolicited notification broadcast
    BPP->>BAP: POST /on_status
    BAP-->>BPP: 200 OK (ACK)
```

## confirm_5

```mermaid
sequenceDiagram
    title Order to Confirm to Fulfillment (City Code)
    autonumber
    actor User as Traveler / Guest
    participant BAP as Accommodation Booking App (BAP)
    participant BG as ONDC Gateway
    participant BPP as Hotel Provider (BPP)

    BAP->>BPP: POST /select
    BPP-->>BAP: 200 OK (ACK)
    BPP->>BAP: POST /on_select
    BAP-->>BPP: 200 OK (ACK)
    BAP->>BPP: POST /init
    BPP-->>BAP: 200 OK (ACK)
    BPP->>BAP: POST /on_init
    BAP-->>BPP: 200 OK (ACK)
    rect rgb(191, 223, 255)
    BAP->>BPP: POST /confirm
    BPP-->>BAP: 200 OK (ACK)
    end
    BPP->>BAP: POST /on_confirm
    BAP-->>BPP: 200 OK (ACK)
    BAP->>User: Display confirmed booking and hotel voucher
    BAP->>BPP: POST /status
    BPP-->>BAP: 200 OK (ACK)
    BPP->>BAP: POST /on_status
    BAP-->>BPP: 200 OK (ACK)
    Note over BPP: Unsolicited notification broadcast
    BPP->>BAP: POST /on_status
    BAP-->>BPP: 200 OK (ACK)
```

## on_confirm_5

```mermaid
sequenceDiagram
    title Order to Confirm to Fulfillment (City Code)
    autonumber
    actor User as Traveler / Guest
    participant BAP as Accommodation Booking App (BAP)
    participant BG as ONDC Gateway
    participant BPP as Hotel Provider (BPP)

    BAP->>BPP: POST /select
    BPP-->>BAP: 200 OK (ACK)
    BPP->>BAP: POST /on_select
    BAP-->>BPP: 200 OK (ACK)
    BAP->>BPP: POST /init
    BPP-->>BAP: 200 OK (ACK)
    BPP->>BAP: POST /on_init
    BAP-->>BPP: 200 OK (ACK)
    BAP->>BPP: POST /confirm
    BPP-->>BAP: 200 OK (ACK)
    rect rgb(191, 223, 255)
    BPP->>BAP: POST /on_confirm
    BAP-->>BPP: 200 OK (ACK)
    BAP->>User: Display confirmed booking and hotel voucher
    end
    BAP->>BPP: POST /status
    BPP-->>BAP: 200 OK (ACK)
    BPP->>BAP: POST /on_status
    BAP-->>BPP: 200 OK (ACK)
    Note over BPP: Unsolicited notification broadcast
    BPP->>BAP: POST /on_status
    BAP-->>BPP: 200 OK (ACK)
```

## status_5

```mermaid
sequenceDiagram
    title Order to Confirm to Fulfillment (City Code)
    autonumber
    actor User as Traveler / Guest
    participant BAP as Accommodation Booking App (BAP)
    participant BG as ONDC Gateway
    participant BPP as Hotel Provider (BPP)

    BAP->>BPP: POST /select
    BPP-->>BAP: 200 OK (ACK)
    BPP->>BAP: POST /on_select
    BAP-->>BPP: 200 OK (ACK)
    BAP->>BPP: POST /init
    BPP-->>BAP: 200 OK (ACK)
    BPP->>BAP: POST /on_init
    BAP-->>BPP: 200 OK (ACK)
    BAP->>BPP: POST /confirm
    BPP-->>BAP: 200 OK (ACK)
    BPP->>BAP: POST /on_confirm
    BAP-->>BPP: 200 OK (ACK)
    BAP->>User: Display confirmed booking and hotel voucher
    rect rgb(191, 223, 255)
    BAP->>BPP: POST /status
    BPP-->>BAP: 200 OK (ACK)
    end
    BPP->>BAP: POST /on_status
    BAP-->>BPP: 200 OK (ACK)
    Note over BPP: Unsolicited notification broadcast
    BPP->>BAP: POST /on_status
    BAP-->>BPP: 200 OK (ACK)
```

## on_status_city_code

```mermaid
sequenceDiagram
    title Order to Confirm to Fulfillment (City Code)
    autonumber
    actor User as Traveler / Guest
    participant BAP as Accommodation Booking App (BAP)
    participant BG as ONDC Gateway
    participant BPP as Hotel Provider (BPP)

    BAP->>BPP: POST /select
    BPP-->>BAP: 200 OK (ACK)
    BPP->>BAP: POST /on_select
    BAP-->>BPP: 200 OK (ACK)
    BAP->>BPP: POST /init
    BPP-->>BAP: 200 OK (ACK)
    BPP->>BAP: POST /on_init
    BAP-->>BPP: 200 OK (ACK)
    BAP->>BPP: POST /confirm
    BPP-->>BAP: 200 OK (ACK)
    BPP->>BAP: POST /on_confirm
    BAP-->>BPP: 200 OK (ACK)
    BAP->>User: Display confirmed booking and hotel voucher
    BAP->>BPP: POST /status
    BPP-->>BAP: 200 OK (ACK)
    rect rgb(191, 223, 255)
    BPP->>BAP: POST /on_status
    BAP-->>BPP: 200 OK (ACK)
    end
    Note over BPP: Unsolicited notification broadcast
    BPP->>BAP: POST /on_status
    BAP-->>BPP: 200 OK (ACK)
```

## on_status_unsoliciated

```mermaid
sequenceDiagram
    title Order to Confirm to Fulfillment (City Code)
    autonumber
    actor User as Traveler / Guest
    participant BAP as Accommodation Booking App (BAP)
    participant BG as ONDC Gateway
    participant BPP as Hotel Provider (BPP)

    BAP->>BPP: POST /select
    BPP-->>BAP: 200 OK (ACK)
    BPP->>BAP: POST /on_select
    BAP-->>BPP: 200 OK (ACK)
    BAP->>BPP: POST /init
    BPP-->>BAP: 200 OK (ACK)
    BPP->>BAP: POST /on_init
    BAP-->>BPP: 200 OK (ACK)
    BAP->>BPP: POST /confirm
    BPP-->>BAP: 200 OK (ACK)
    BPP->>BAP: POST /on_confirm
    BAP-->>BPP: 200 OK (ACK)
    BAP->>User: Display confirmed booking and hotel voucher
    BAP->>BPP: POST /status
    BPP-->>BAP: 200 OK (ACK)
    BPP->>BAP: POST /on_status
    BAP-->>BPP: 200 OK (ACK)
    rect rgb(191, 223, 255)
    Note over BPP: Unsolicited notification broadcast
    BPP->>BAP: POST /on_status
    BAP-->>BPP: 200 OK (ACK)
    end
```

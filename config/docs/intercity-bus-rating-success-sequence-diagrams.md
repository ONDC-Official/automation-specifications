# Intercity(Bus) Rating(Success) — Sequence Diagrams

Internal data file consumed by the Developer Guide's "Sequence Diagram" tab (API Walkthrough).
Not meant to be shown as its own docs page — the frontend filters this slug out of the Use Case
Brief / Additional Resources / Changelog tab lists and instead looks up the section matching the
selected API call's `action_id` (the `##` heading below) to render that step's diagram.

One `## <action_id>` heading per step of `Intercity_Bus__Rating_Success_.yaml`, in that flow's own step order, each
followed by its Mermaid `sequenceDiagram`.

## search_BUS_201

```mermaid
sequenceDiagram
    title Intercity(Bus) Rating(Success)
    autonumber
    actor User as Traveler / Customer
    participant BAP as Buyer App (BAP)
    participant BG as ONDC Gateway
    participant BPP as Bus Operator (BPP)

    rect rgb(191, 223, 255)
    User->>BAP: Provide journey search parameters
    BAP->>BG: POST /search
    BG-->>BAP: 200 OK (ACK)
    BG->>BPP: POST /search
    BPP-->>BG: 200 OK (ACK)
    end
    BPP->>BAP: POST /on_search
    BAP-->>BPP: 200 OK (ACK)
    BAP->>BG: POST /search
    BG-->>BAP: 200 OK (ACK)
    BG->>BPP: POST /search
    BPP-->>BG: 200 OK (ACK)
    BPP->>BAP: POST /on_search
    BAP-->>BPP: 200 OK (ACK)
    BAP->>BG: POST /search
    BG-->>BAP: 200 OK (ACK)
    BG->>BPP: POST /search
    BPP-->>BG: 200 OK (ACK)
    BPP->>BAP: POST /on_search
    BAP-->>BPP: 200 OK (ACK)
    BAP->>BPP: POST /select
    BPP-->>BAP: 200 OK (ACK)
    BPP->>BAP: POST /on_select
    BAP-->>BPP: 200 OK (ACK)
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
    BAP->>User: Display confirmed booking and PNR/ticket pass
    Note over BPP: Unsolicited notification broadcast
    BPP->>BAP: POST /on_status
    BAP-->>BPP: 200 OK (ACK)
    BAP->>BPP: POST /rating
    BPP-->>BAP: 200 OK (ACK)
```

## on_search_BUS_201

```mermaid
sequenceDiagram
    title Intercity(Bus) Rating(Success)
    autonumber
    actor User as Traveler / Customer
    participant BAP as Buyer App (BAP)
    participant BG as ONDC Gateway
    participant BPP as Bus Operator (BPP)

    User->>BAP: Provide journey search parameters
    BAP->>BG: POST /search
    BG-->>BAP: 200 OK (ACK)
    BG->>BPP: POST /search
    BPP-->>BG: 200 OK (ACK)
    rect rgb(191, 223, 255)
    BPP->>BAP: POST /on_search
    BAP-->>BPP: 200 OK (ACK)
    end
    BAP->>BG: POST /search
    BG-->>BAP: 200 OK (ACK)
    BG->>BPP: POST /search
    BPP-->>BG: 200 OK (ACK)
    BPP->>BAP: POST /on_search
    BAP-->>BPP: 200 OK (ACK)
    BAP->>BG: POST /search
    BG-->>BAP: 200 OK (ACK)
    BG->>BPP: POST /search
    BPP-->>BG: 200 OK (ACK)
    BPP->>BAP: POST /on_search
    BAP-->>BPP: 200 OK (ACK)
    BAP->>BPP: POST /select
    BPP-->>BAP: 200 OK (ACK)
    BPP->>BAP: POST /on_select
    BAP-->>BPP: 200 OK (ACK)
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
    BAP->>User: Display confirmed booking and PNR/ticket pass
    Note over BPP: Unsolicited notification broadcast
    BPP->>BAP: POST /on_status
    BAP-->>BPP: 200 OK (ACK)
    BAP->>BPP: POST /rating
    BPP-->>BAP: 200 OK (ACK)
```

## search_BUS_202

```mermaid
sequenceDiagram
    title Intercity(Bus) Rating(Success)
    autonumber
    actor User as Traveler / Customer
    participant BAP as Buyer App (BAP)
    participant BG as ONDC Gateway
    participant BPP as Bus Operator (BPP)

    User->>BAP: Provide journey search parameters
    BAP->>BG: POST /search
    BG-->>BAP: 200 OK (ACK)
    BG->>BPP: POST /search
    BPP-->>BG: 200 OK (ACK)
    BPP->>BAP: POST /on_search
    BAP-->>BPP: 200 OK (ACK)
    rect rgb(191, 223, 255)
    BAP->>BG: POST /search
    BG-->>BAP: 200 OK (ACK)
    BG->>BPP: POST /search
    BPP-->>BG: 200 OK (ACK)
    end
    BPP->>BAP: POST /on_search
    BAP-->>BPP: 200 OK (ACK)
    BAP->>BG: POST /search
    BG-->>BAP: 200 OK (ACK)
    BG->>BPP: POST /search
    BPP-->>BG: 200 OK (ACK)
    BPP->>BAP: POST /on_search
    BAP-->>BPP: 200 OK (ACK)
    BAP->>BPP: POST /select
    BPP-->>BAP: 200 OK (ACK)
    BPP->>BAP: POST /on_select
    BAP-->>BPP: 200 OK (ACK)
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
    BAP->>User: Display confirmed booking and PNR/ticket pass
    Note over BPP: Unsolicited notification broadcast
    BPP->>BAP: POST /on_status
    BAP-->>BPP: 200 OK (ACK)
    BAP->>BPP: POST /rating
    BPP-->>BAP: 200 OK (ACK)
```

## on_search_BUS_202

```mermaid
sequenceDiagram
    title Intercity(Bus) Rating(Success)
    autonumber
    actor User as Traveler / Customer
    participant BAP as Buyer App (BAP)
    participant BG as ONDC Gateway
    participant BPP as Bus Operator (BPP)

    User->>BAP: Provide journey search parameters
    BAP->>BG: POST /search
    BG-->>BAP: 200 OK (ACK)
    BG->>BPP: POST /search
    BPP-->>BG: 200 OK (ACK)
    BPP->>BAP: POST /on_search
    BAP-->>BPP: 200 OK (ACK)
    BAP->>BG: POST /search
    BG-->>BAP: 200 OK (ACK)
    BG->>BPP: POST /search
    BPP-->>BG: 200 OK (ACK)
    rect rgb(191, 223, 255)
    BPP->>BAP: POST /on_search
    BAP-->>BPP: 200 OK (ACK)
    end
    BAP->>BG: POST /search
    BG-->>BAP: 200 OK (ACK)
    BG->>BPP: POST /search
    BPP-->>BG: 200 OK (ACK)
    BPP->>BAP: POST /on_search
    BAP-->>BPP: 200 OK (ACK)
    BAP->>BPP: POST /select
    BPP-->>BAP: 200 OK (ACK)
    BPP->>BAP: POST /on_select
    BAP-->>BPP: 200 OK (ACK)
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
    BAP->>User: Display confirmed booking and PNR/ticket pass
    Note over BPP: Unsolicited notification broadcast
    BPP->>BAP: POST /on_status
    BAP-->>BPP: 200 OK (ACK)
    BAP->>BPP: POST /rating
    BPP-->>BAP: 200 OK (ACK)
```

## search_BUS_203

```mermaid
sequenceDiagram
    title Intercity(Bus) Rating(Success)
    autonumber
    actor User as Traveler / Customer
    participant BAP as Buyer App (BAP)
    participant BG as ONDC Gateway
    participant BPP as Bus Operator (BPP)

    User->>BAP: Provide journey search parameters
    BAP->>BG: POST /search
    BG-->>BAP: 200 OK (ACK)
    BG->>BPP: POST /search
    BPP-->>BG: 200 OK (ACK)
    BPP->>BAP: POST /on_search
    BAP-->>BPP: 200 OK (ACK)
    BAP->>BG: POST /search
    BG-->>BAP: 200 OK (ACK)
    BG->>BPP: POST /search
    BPP-->>BG: 200 OK (ACK)
    BPP->>BAP: POST /on_search
    BAP-->>BPP: 200 OK (ACK)
    rect rgb(191, 223, 255)
    BAP->>BG: POST /search
    BG-->>BAP: 200 OK (ACK)
    BG->>BPP: POST /search
    BPP-->>BG: 200 OK (ACK)
    end
    BPP->>BAP: POST /on_search
    BAP-->>BPP: 200 OK (ACK)
    BAP->>BPP: POST /select
    BPP-->>BAP: 200 OK (ACK)
    BPP->>BAP: POST /on_select
    BAP-->>BPP: 200 OK (ACK)
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
    BAP->>User: Display confirmed booking and PNR/ticket pass
    Note over BPP: Unsolicited notification broadcast
    BPP->>BAP: POST /on_status
    BAP-->>BPP: 200 OK (ACK)
    BAP->>BPP: POST /rating
    BPP-->>BAP: 200 OK (ACK)
```

## on_search_BUS_203

```mermaid
sequenceDiagram
    title Intercity(Bus) Rating(Success)
    autonumber
    actor User as Traveler / Customer
    participant BAP as Buyer App (BAP)
    participant BG as ONDC Gateway
    participant BPP as Bus Operator (BPP)

    User->>BAP: Provide journey search parameters
    BAP->>BG: POST /search
    BG-->>BAP: 200 OK (ACK)
    BG->>BPP: POST /search
    BPP-->>BG: 200 OK (ACK)
    BPP->>BAP: POST /on_search
    BAP-->>BPP: 200 OK (ACK)
    BAP->>BG: POST /search
    BG-->>BAP: 200 OK (ACK)
    BG->>BPP: POST /search
    BPP-->>BG: 200 OK (ACK)
    BPP->>BAP: POST /on_search
    BAP-->>BPP: 200 OK (ACK)
    BAP->>BG: POST /search
    BG-->>BAP: 200 OK (ACK)
    BG->>BPP: POST /search
    BPP-->>BG: 200 OK (ACK)
    rect rgb(191, 223, 255)
    BPP->>BAP: POST /on_search
    BAP-->>BPP: 200 OK (ACK)
    end
    BAP->>BPP: POST /select
    BPP-->>BAP: 200 OK (ACK)
    BPP->>BAP: POST /on_select
    BAP-->>BPP: 200 OK (ACK)
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
    BAP->>User: Display confirmed booking and PNR/ticket pass
    Note over BPP: Unsolicited notification broadcast
    BPP->>BAP: POST /on_status
    BAP-->>BPP: 200 OK (ACK)
    BAP->>BPP: POST /rating
    BPP-->>BAP: 200 OK (ACK)
```

## select_BUS_201

```mermaid
sequenceDiagram
    title Intercity(Bus) Rating(Success)
    autonumber
    actor User as Traveler / Customer
    participant BAP as Buyer App (BAP)
    participant BG as ONDC Gateway
    participant BPP as Bus Operator (BPP)

    User->>BAP: Provide journey search parameters
    BAP->>BG: POST /search
    BG-->>BAP: 200 OK (ACK)
    BG->>BPP: POST /search
    BPP-->>BG: 200 OK (ACK)
    BPP->>BAP: POST /on_search
    BAP-->>BPP: 200 OK (ACK)
    BAP->>BG: POST /search
    BG-->>BAP: 200 OK (ACK)
    BG->>BPP: POST /search
    BPP-->>BG: 200 OK (ACK)
    BPP->>BAP: POST /on_search
    BAP-->>BPP: 200 OK (ACK)
    BAP->>BG: POST /search
    BG-->>BAP: 200 OK (ACK)
    BG->>BPP: POST /search
    BPP-->>BG: 200 OK (ACK)
    BPP->>BAP: POST /on_search
    BAP-->>BPP: 200 OK (ACK)
    rect rgb(191, 223, 255)
    BAP->>BPP: POST /select
    BPP-->>BAP: 200 OK (ACK)
    end
    BPP->>BAP: POST /on_select
    BAP-->>BPP: 200 OK (ACK)
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
    BAP->>User: Display confirmed booking and PNR/ticket pass
    Note over BPP: Unsolicited notification broadcast
    BPP->>BAP: POST /on_status
    BAP-->>BPP: 200 OK (ACK)
    BAP->>BPP: POST /rating
    BPP-->>BAP: 200 OK (ACK)
```

## on_select_BUS_201

```mermaid
sequenceDiagram
    title Intercity(Bus) Rating(Success)
    autonumber
    actor User as Traveler / Customer
    participant BAP as Buyer App (BAP)
    participant BG as ONDC Gateway
    participant BPP as Bus Operator (BPP)

    User->>BAP: Provide journey search parameters
    BAP->>BG: POST /search
    BG-->>BAP: 200 OK (ACK)
    BG->>BPP: POST /search
    BPP-->>BG: 200 OK (ACK)
    BPP->>BAP: POST /on_search
    BAP-->>BPP: 200 OK (ACK)
    BAP->>BG: POST /search
    BG-->>BAP: 200 OK (ACK)
    BG->>BPP: POST /search
    BPP-->>BG: 200 OK (ACK)
    BPP->>BAP: POST /on_search
    BAP-->>BPP: 200 OK (ACK)
    BAP->>BG: POST /search
    BG-->>BAP: 200 OK (ACK)
    BG->>BPP: POST /search
    BPP-->>BG: 200 OK (ACK)
    BPP->>BAP: POST /on_search
    BAP-->>BPP: 200 OK (ACK)
    BAP->>BPP: POST /select
    BPP-->>BAP: 200 OK (ACK)
    rect rgb(191, 223, 255)
    BPP->>BAP: POST /on_select
    BAP-->>BPP: 200 OK (ACK)
    end
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
    BAP->>User: Display confirmed booking and PNR/ticket pass
    Note over BPP: Unsolicited notification broadcast
    BPP->>BAP: POST /on_status
    BAP-->>BPP: 200 OK (ACK)
    BAP->>BPP: POST /rating
    BPP-->>BAP: 200 OK (ACK)
```

## select_BUS_202

```mermaid
sequenceDiagram
    title Intercity(Bus) Rating(Success)
    autonumber
    actor User as Traveler / Customer
    participant BAP as Buyer App (BAP)
    participant BG as ONDC Gateway
    participant BPP as Bus Operator (BPP)

    User->>BAP: Provide journey search parameters
    BAP->>BG: POST /search
    BG-->>BAP: 200 OK (ACK)
    BG->>BPP: POST /search
    BPP-->>BG: 200 OK (ACK)
    BPP->>BAP: POST /on_search
    BAP-->>BPP: 200 OK (ACK)
    BAP->>BG: POST /search
    BG-->>BAP: 200 OK (ACK)
    BG->>BPP: POST /search
    BPP-->>BG: 200 OK (ACK)
    BPP->>BAP: POST /on_search
    BAP-->>BPP: 200 OK (ACK)
    BAP->>BG: POST /search
    BG-->>BAP: 200 OK (ACK)
    BG->>BPP: POST /search
    BPP-->>BG: 200 OK (ACK)
    BPP->>BAP: POST /on_search
    BAP-->>BPP: 200 OK (ACK)
    BAP->>BPP: POST /select
    BPP-->>BAP: 200 OK (ACK)
    BPP->>BAP: POST /on_select
    BAP-->>BPP: 200 OK (ACK)
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
    BAP->>User: Display confirmed booking and PNR/ticket pass
    Note over BPP: Unsolicited notification broadcast
    BPP->>BAP: POST /on_status
    BAP-->>BPP: 200 OK (ACK)
    BAP->>BPP: POST /rating
    BPP-->>BAP: 200 OK (ACK)
```

## on_select_BUS_202

```mermaid
sequenceDiagram
    title Intercity(Bus) Rating(Success)
    autonumber
    actor User as Traveler / Customer
    participant BAP as Buyer App (BAP)
    participant BG as ONDC Gateway
    participant BPP as Bus Operator (BPP)

    User->>BAP: Provide journey search parameters
    BAP->>BG: POST /search
    BG-->>BAP: 200 OK (ACK)
    BG->>BPP: POST /search
    BPP-->>BG: 200 OK (ACK)
    BPP->>BAP: POST /on_search
    BAP-->>BPP: 200 OK (ACK)
    BAP->>BG: POST /search
    BG-->>BAP: 200 OK (ACK)
    BG->>BPP: POST /search
    BPP-->>BG: 200 OK (ACK)
    BPP->>BAP: POST /on_search
    BAP-->>BPP: 200 OK (ACK)
    BAP->>BG: POST /search
    BG-->>BAP: 200 OK (ACK)
    BG->>BPP: POST /search
    BPP-->>BG: 200 OK (ACK)
    BPP->>BAP: POST /on_search
    BAP-->>BPP: 200 OK (ACK)
    BAP->>BPP: POST /select
    BPP-->>BAP: 200 OK (ACK)
    BPP->>BAP: POST /on_select
    BAP-->>BPP: 200 OK (ACK)
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
    BAP->>User: Display confirmed booking and PNR/ticket pass
    Note over BPP: Unsolicited notification broadcast
    BPP->>BAP: POST /on_status
    BAP-->>BPP: 200 OK (ACK)
    BAP->>BPP: POST /rating
    BPP-->>BAP: 200 OK (ACK)
```

## init_BUS_201

```mermaid
sequenceDiagram
    title Intercity(Bus) Rating(Success)
    autonumber
    actor User as Traveler / Customer
    participant BAP as Buyer App (BAP)
    participant BG as ONDC Gateway
    participant BPP as Bus Operator (BPP)

    User->>BAP: Provide journey search parameters
    BAP->>BG: POST /search
    BG-->>BAP: 200 OK (ACK)
    BG->>BPP: POST /search
    BPP-->>BG: 200 OK (ACK)
    BPP->>BAP: POST /on_search
    BAP-->>BPP: 200 OK (ACK)
    BAP->>BG: POST /search
    BG-->>BAP: 200 OK (ACK)
    BG->>BPP: POST /search
    BPP-->>BG: 200 OK (ACK)
    BPP->>BAP: POST /on_search
    BAP-->>BPP: 200 OK (ACK)
    BAP->>BG: POST /search
    BG-->>BAP: 200 OK (ACK)
    BG->>BPP: POST /search
    BPP-->>BG: 200 OK (ACK)
    BPP->>BAP: POST /on_search
    BAP-->>BPP: 200 OK (ACK)
    BAP->>BPP: POST /select
    BPP-->>BAP: 200 OK (ACK)
    BPP->>BAP: POST /on_select
    BAP-->>BPP: 200 OK (ACK)
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
    BAP->>User: Display confirmed booking and PNR/ticket pass
    Note over BPP: Unsolicited notification broadcast
    BPP->>BAP: POST /on_status
    BAP-->>BPP: 200 OK (ACK)
    BAP->>BPP: POST /rating
    BPP-->>BAP: 200 OK (ACK)
```

## on_init_BUS_201

```mermaid
sequenceDiagram
    title Intercity(Bus) Rating(Success)
    autonumber
    actor User as Traveler / Customer
    participant BAP as Buyer App (BAP)
    participant BG as ONDC Gateway
    participant BPP as Bus Operator (BPP)

    User->>BAP: Provide journey search parameters
    BAP->>BG: POST /search
    BG-->>BAP: 200 OK (ACK)
    BG->>BPP: POST /search
    BPP-->>BG: 200 OK (ACK)
    BPP->>BAP: POST /on_search
    BAP-->>BPP: 200 OK (ACK)
    BAP->>BG: POST /search
    BG-->>BAP: 200 OK (ACK)
    BG->>BPP: POST /search
    BPP-->>BG: 200 OK (ACK)
    BPP->>BAP: POST /on_search
    BAP-->>BPP: 200 OK (ACK)
    BAP->>BG: POST /search
    BG-->>BAP: 200 OK (ACK)
    BG->>BPP: POST /search
    BPP-->>BG: 200 OK (ACK)
    BPP->>BAP: POST /on_search
    BAP-->>BPP: 200 OK (ACK)
    BAP->>BPP: POST /select
    BPP-->>BAP: 200 OK (ACK)
    BPP->>BAP: POST /on_select
    BAP-->>BPP: 200 OK (ACK)
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
    BAP->>User: Display confirmed booking and PNR/ticket pass
    Note over BPP: Unsolicited notification broadcast
    BPP->>BAP: POST /on_status
    BAP-->>BPP: 200 OK (ACK)
    BAP->>BPP: POST /rating
    BPP-->>BAP: 200 OK (ACK)
```

## confirm_BUS_201

```mermaid
sequenceDiagram
    title Intercity(Bus) Rating(Success)
    autonumber
    actor User as Traveler / Customer
    participant BAP as Buyer App (BAP)
    participant BG as ONDC Gateway
    participant BPP as Bus Operator (BPP)

    User->>BAP: Provide journey search parameters
    BAP->>BG: POST /search
    BG-->>BAP: 200 OK (ACK)
    BG->>BPP: POST /search
    BPP-->>BG: 200 OK (ACK)
    BPP->>BAP: POST /on_search
    BAP-->>BPP: 200 OK (ACK)
    BAP->>BG: POST /search
    BG-->>BAP: 200 OK (ACK)
    BG->>BPP: POST /search
    BPP-->>BG: 200 OK (ACK)
    BPP->>BAP: POST /on_search
    BAP-->>BPP: 200 OK (ACK)
    BAP->>BG: POST /search
    BG-->>BAP: 200 OK (ACK)
    BG->>BPP: POST /search
    BPP-->>BG: 200 OK (ACK)
    BPP->>BAP: POST /on_search
    BAP-->>BPP: 200 OK (ACK)
    BAP->>BPP: POST /select
    BPP-->>BAP: 200 OK (ACK)
    BPP->>BAP: POST /on_select
    BAP-->>BPP: 200 OK (ACK)
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
    BAP->>User: Display confirmed booking and PNR/ticket pass
    Note over BPP: Unsolicited notification broadcast
    BPP->>BAP: POST /on_status
    BAP-->>BPP: 200 OK (ACK)
    BAP->>BPP: POST /rating
    BPP-->>BAP: 200 OK (ACK)
```

## on_confirm_BUS_201

```mermaid
sequenceDiagram
    title Intercity(Bus) Rating(Success)
    autonumber
    actor User as Traveler / Customer
    participant BAP as Buyer App (BAP)
    participant BG as ONDC Gateway
    participant BPP as Bus Operator (BPP)

    User->>BAP: Provide journey search parameters
    BAP->>BG: POST /search
    BG-->>BAP: 200 OK (ACK)
    BG->>BPP: POST /search
    BPP-->>BG: 200 OK (ACK)
    BPP->>BAP: POST /on_search
    BAP-->>BPP: 200 OK (ACK)
    BAP->>BG: POST /search
    BG-->>BAP: 200 OK (ACK)
    BG->>BPP: POST /search
    BPP-->>BG: 200 OK (ACK)
    BPP->>BAP: POST /on_search
    BAP-->>BPP: 200 OK (ACK)
    BAP->>BG: POST /search
    BG-->>BAP: 200 OK (ACK)
    BG->>BPP: POST /search
    BPP-->>BG: 200 OK (ACK)
    BPP->>BAP: POST /on_search
    BAP-->>BPP: 200 OK (ACK)
    BAP->>BPP: POST /select
    BPP-->>BAP: 200 OK (ACK)
    BPP->>BAP: POST /on_select
    BAP-->>BPP: 200 OK (ACK)
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
    BAP->>User: Display confirmed booking and PNR/ticket pass
    end
    Note over BPP: Unsolicited notification broadcast
    BPP->>BAP: POST /on_status
    BAP-->>BPP: 200 OK (ACK)
    BAP->>BPP: POST /rating
    BPP-->>BAP: 200 OK (ACK)
```

## on_status_BUS_251

```mermaid
sequenceDiagram
    title Intercity(Bus) Rating(Success)
    autonumber
    actor User as Traveler / Customer
    participant BAP as Buyer App (BAP)
    participant BG as ONDC Gateway
    participant BPP as Bus Operator (BPP)

    User->>BAP: Provide journey search parameters
    BAP->>BG: POST /search
    BG-->>BAP: 200 OK (ACK)
    BG->>BPP: POST /search
    BPP-->>BG: 200 OK (ACK)
    BPP->>BAP: POST /on_search
    BAP-->>BPP: 200 OK (ACK)
    BAP->>BG: POST /search
    BG-->>BAP: 200 OK (ACK)
    BG->>BPP: POST /search
    BPP-->>BG: 200 OK (ACK)
    BPP->>BAP: POST /on_search
    BAP-->>BPP: 200 OK (ACK)
    BAP->>BG: POST /search
    BG-->>BAP: 200 OK (ACK)
    BG->>BPP: POST /search
    BPP-->>BG: 200 OK (ACK)
    BPP->>BAP: POST /on_search
    BAP-->>BPP: 200 OK (ACK)
    BAP->>BPP: POST /select
    BPP-->>BAP: 200 OK (ACK)
    BPP->>BAP: POST /on_select
    BAP-->>BPP: 200 OK (ACK)
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
    BAP->>User: Display confirmed booking and PNR/ticket pass
    rect rgb(191, 223, 255)
    Note over BPP: Unsolicited notification broadcast
    BPP->>BAP: POST /on_status
    BAP-->>BPP: 200 OK (ACK)
    end
    BAP->>BPP: POST /rating
    BPP-->>BAP: 200 OK (ACK)
```

## rating_251

```mermaid
sequenceDiagram
    title Intercity(Bus) Rating(Success)
    autonumber
    actor User as Traveler / Customer
    participant BAP as Buyer App (BAP)
    participant BG as ONDC Gateway
    participant BPP as Bus Operator (BPP)

    User->>BAP: Provide journey search parameters
    BAP->>BG: POST /search
    BG-->>BAP: 200 OK (ACK)
    BG->>BPP: POST /search
    BPP-->>BG: 200 OK (ACK)
    BPP->>BAP: POST /on_search
    BAP-->>BPP: 200 OK (ACK)
    BAP->>BG: POST /search
    BG-->>BAP: 200 OK (ACK)
    BG->>BPP: POST /search
    BPP-->>BG: 200 OK (ACK)
    BPP->>BAP: POST /on_search
    BAP-->>BPP: 200 OK (ACK)
    BAP->>BG: POST /search
    BG-->>BAP: 200 OK (ACK)
    BG->>BPP: POST /search
    BPP-->>BG: 200 OK (ACK)
    BPP->>BAP: POST /on_search
    BAP-->>BPP: 200 OK (ACK)
    BAP->>BPP: POST /select
    BPP-->>BAP: 200 OK (ACK)
    BPP->>BAP: POST /on_select
    BAP-->>BPP: 200 OK (ACK)
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
    BAP->>User: Display confirmed booking and PNR/ticket pass
    Note over BPP: Unsolicited notification broadcast
    BPP->>BAP: POST /on_status
    BAP-->>BPP: 200 OK (ACK)
    rect rgb(191, 223, 255)
    BAP->>BPP: POST /rating
    BPP-->>BAP: 200 OK (ACK)
    end
```

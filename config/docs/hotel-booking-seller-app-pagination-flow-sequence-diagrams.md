# Hotel Booking Seller App Pagination Flow — Sequence Diagrams

Internal data file consumed by the Developer Guide's "Sequence Diagram" tab (API Walkthrough).
Not meant to be shown as its own docs page — the frontend filters this slug out of the Use Case
Brief / Additional Resources / Changelog tab lists and instead looks up the section matching the
selected API call's `action_id` (the `##` heading below) to render that step's diagram.

One `## <action_id>` heading per step of `Hotel_Booking_Seller_App_Pagination_Flow.yaml`, in that flow's own step order, each
followed by its Mermaid `sequenceDiagram`.

## search_1

```mermaid
sequenceDiagram
    title Hotel Booking Seller App Pagination Flow
    autonumber
    actor User as Traveler / Guest
    participant BAP as Accommodation Booking App (BAP)
    participant BG as ONDC Gateway
    participant BPP as Hotel Provider (BPP)

    rect rgb(191, 223, 255)
    User->>BAP: Provide destination city and stay dates
    BAP->>BG: POST /search
    BG-->>BAP: 200 OK (ACK)
    BG->>BPP: POST /search
    BPP-->>BG: 200 OK (ACK)
    end
    BPP->>BAP: POST /on_search (Batch 1: Initial Hotel Catalog)
    BAP-->>BPP: 200 OK (ACK)
    Note over BPP: Unsolicited notification broadcast
    BPP->>BAP: POST /on_search (Batch 2: Additional Hotel Catalog)
    BAP-->>BPP: 200 OK (ACK)
    Note over BPP: Unsolicited notification broadcast
    BPP->>BAP: POST /on_search (Batch 3: Additional Hotel Catalog)
    BAP-->>BPP: 200 OK (ACK)
    Note over BPP: Unsolicited notification broadcast
    BPP->>BAP: POST /on_search (Batch 4: Final Hotel Catalog Batch)
    BAP-->>BPP: 200 OK (ACK)
```

## on_search_1

```mermaid
sequenceDiagram
    title Hotel Booking Seller App Pagination Flow
    autonumber
    actor User as Traveler / Guest
    participant BAP as Accommodation Booking App (BAP)
    participant BG as ONDC Gateway
    participant BPP as Hotel Provider (BPP)

    User->>BAP: Provide destination city and stay dates
    BAP->>BG: POST /search
    BG-->>BAP: 200 OK (ACK)
    BG->>BPP: POST /search
    BPP-->>BG: 200 OK (ACK)
    rect rgb(191, 223, 255)
    BPP->>BAP: POST /on_search (Batch 1: Initial Hotel Catalog)
    BAP-->>BPP: 200 OK (ACK)
    end
    Note over BPP: Unsolicited notification broadcast
    BPP->>BAP: POST /on_search (Batch 2: Additional Hotel Catalog)
    BAP-->>BPP: 200 OK (ACK)
    Note over BPP: Unsolicited notification broadcast
    BPP->>BAP: POST /on_search (Batch 3: Additional Hotel Catalog)
    BAP-->>BPP: 200 OK (ACK)
    Note over BPP: Unsolicited notification broadcast
    BPP->>BAP: POST /on_search (Batch 4: Final Hotel Catalog Batch)
    BAP-->>BPP: 200 OK (ACK)
```

## on_search_2

```mermaid
sequenceDiagram
    title Hotel Booking Seller App Pagination Flow
    autonumber
    actor User as Traveler / Guest
    participant BAP as Accommodation Booking App (BAP)
    participant BG as ONDC Gateway
    participant BPP as Hotel Provider (BPP)

    User->>BAP: Provide destination city and stay dates
    BAP->>BG: POST /search
    BG-->>BAP: 200 OK (ACK)
    BG->>BPP: POST /search
    BPP-->>BG: 200 OK (ACK)
    BPP->>BAP: POST /on_search (Batch 1: Initial Hotel Catalog)
    BAP-->>BPP: 200 OK (ACK)
    rect rgb(191, 223, 255)
    Note over BPP: Unsolicited notification broadcast
    BPP->>BAP: POST /on_search (Batch 2: Additional Hotel Catalog)
    BAP-->>BPP: 200 OK (ACK)
    end
    Note over BPP: Unsolicited notification broadcast
    BPP->>BAP: POST /on_search (Batch 3: Additional Hotel Catalog)
    BAP-->>BPP: 200 OK (ACK)
    Note over BPP: Unsolicited notification broadcast
    BPP->>BAP: POST /on_search (Batch 4: Final Hotel Catalog Batch)
    BAP-->>BPP: 200 OK (ACK)
```

## on_search_3

```mermaid
sequenceDiagram
    title Hotel Booking Seller App Pagination Flow
    autonumber
    actor User as Traveler / Guest
    participant BAP as Accommodation Booking App (BAP)
    participant BG as ONDC Gateway
    participant BPP as Hotel Provider (BPP)

    User->>BAP: Provide destination city and stay dates
    BAP->>BG: POST /search
    BG-->>BAP: 200 OK (ACK)
    BG->>BPP: POST /search
    BPP-->>BG: 200 OK (ACK)
    BPP->>BAP: POST /on_search (Batch 1: Initial Hotel Catalog)
    BAP-->>BPP: 200 OK (ACK)
    Note over BPP: Unsolicited notification broadcast
    BPP->>BAP: POST /on_search (Batch 2: Additional Hotel Catalog)
    BAP-->>BPP: 200 OK (ACK)
    rect rgb(191, 223, 255)
    Note over BPP: Unsolicited notification broadcast
    BPP->>BAP: POST /on_search (Batch 3: Additional Hotel Catalog)
    BAP-->>BPP: 200 OK (ACK)
    end
    Note over BPP: Unsolicited notification broadcast
    BPP->>BAP: POST /on_search (Batch 4: Final Hotel Catalog Batch)
    BAP-->>BPP: 200 OK (ACK)
```

## on_search_4

```mermaid
sequenceDiagram
    title Hotel Booking Seller App Pagination Flow
    autonumber
    actor User as Traveler / Guest
    participant BAP as Accommodation Booking App (BAP)
    participant BG as ONDC Gateway
    participant BPP as Hotel Provider (BPP)

    User->>BAP: Provide destination city and stay dates
    BAP->>BG: POST /search
    BG-->>BAP: 200 OK (ACK)
    BG->>BPP: POST /search
    BPP-->>BG: 200 OK (ACK)
    BPP->>BAP: POST /on_search (Batch 1: Initial Hotel Catalog)
    BAP-->>BPP: 200 OK (ACK)
    Note over BPP: Unsolicited notification broadcast
    BPP->>BAP: POST /on_search (Batch 2: Additional Hotel Catalog)
    BAP-->>BPP: 200 OK (ACK)
    Note over BPP: Unsolicited notification broadcast
    BPP->>BAP: POST /on_search (Batch 3: Additional Hotel Catalog)
    BAP-->>BPP: 200 OK (ACK)
    rect rgb(191, 223, 255)
    Note over BPP: Unsolicited notification broadcast
    BPP->>BAP: POST /on_search (Batch 4: Final Hotel Catalog Batch)
    BAP-->>BPP: 200 OK (ACK)
    end
```

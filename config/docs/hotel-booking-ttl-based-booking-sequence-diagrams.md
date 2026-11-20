# Hotel Booking (ttl based) booking — Sequence Diagrams

Internal data file consumed by the Developer Guide's "Sequence Diagram" tab (API Walkthrough).
Not meant to be shown as its own docs page — the frontend filters this slug out of the Use Case
Brief / Additional Resources / Changelog tab lists and instead looks up the section matching the
selected API call's `action_id` (the `##` heading below) to render that step's diagram.

One `## <action_id>` heading per step of `Hotel_Booking__ttl_based__booking.yaml`, in that flow's own step order, each
followed by its Mermaid `sequenceDiagram`.

## search_6

```mermaid
sequenceDiagram
    title Hotel Booking (ttl based) booking
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
    BPP->>BAP: POST /on_search (Publish Catalog with TTL)
    BAP-->>BPP: 200 OK (ACK)
    Note over BAP,BPP: TTL Expiry — Refresh Hotel Inventory
    BAP->>BG: POST /search (Incremental Catalog Pull)
    BG-->>BAP: 200 OK (ACK)
    BG->>BPP: POST /search
    BPP-->>BG: 200 OK (ACK)
    BPP->>BAP: POST /on_search (Publish Refreshed Catalog)
    BAP-->>BPP: 200 OK (ACK)
```

## on_search_6

```mermaid
sequenceDiagram
    title Hotel Booking (ttl based) booking
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
    BPP->>BAP: POST /on_search (Publish Catalog with TTL)
    BAP-->>BPP: 200 OK (ACK)
    end
    Note over BAP,BPP: TTL Expiry — Refresh Hotel Inventory
    BAP->>BG: POST /search (Incremental Catalog Pull)
    BG-->>BAP: 200 OK (ACK)
    BG->>BPP: POST /search
    BPP-->>BG: 200 OK (ACK)
    BPP->>BAP: POST /on_search (Publish Refreshed Catalog)
    BAP-->>BPP: 200 OK (ACK)
```

## search_7

```mermaid
sequenceDiagram
    title Hotel Booking (ttl based) booking
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
    BPP->>BAP: POST /on_search (Publish Catalog with TTL)
    BAP-->>BPP: 200 OK (ACK)
    rect rgb(191, 223, 255)
    Note over BAP,BPP: TTL Expiry — Refresh Hotel Inventory
    BAP->>BG: POST /search (Incremental Catalog Pull)
    BG-->>BAP: 200 OK (ACK)
    BG->>BPP: POST /search
    BPP-->>BG: 200 OK (ACK)
    end
    BPP->>BAP: POST /on_search (Publish Refreshed Catalog)
    BAP-->>BPP: 200 OK (ACK)
```

## on_search_7

```mermaid
sequenceDiagram
    title Hotel Booking (ttl based) booking
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
    BPP->>BAP: POST /on_search (Publish Catalog with TTL)
    BAP-->>BPP: 200 OK (ACK)
    Note over BAP,BPP: TTL Expiry — Refresh Hotel Inventory
    BAP->>BG: POST /search (Incremental Catalog Pull)
    BG-->>BAP: 200 OK (ACK)
    BG->>BPP: POST /search
    BPP-->>BG: 200 OK (ACK)
    rect rgb(191, 223, 255)
    BPP->>BAP: POST /on_search (Publish Refreshed Catalog)
    BAP-->>BPP: 200 OK (ACK)
    end
```

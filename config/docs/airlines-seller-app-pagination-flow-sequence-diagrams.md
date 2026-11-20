# Airlines - Seller App Pagination Flow — Sequence Diagrams

Internal data file consumed by the Developer Guide's "Sequence Diagram" tab (API Walkthrough).
Not meant to be shown as its own docs page — the frontend filters this slug out of the Use Case
Brief / Additional Resources / Changelog tab lists and instead looks up the section matching the
selected API call's `action_id` (the `##` heading below) to render that step's diagram.

One `## <action_id>` heading per step of `Airlines_-_Seller_App_Pagination_Flow.yaml`, in that flow's own step order, each
followed by its Mermaid `sequenceDiagram`.

## search_1_Airline_200

```mermaid
sequenceDiagram
    title Airlines - Seller App Pagination Flow
    autonumber
    actor User as Traveler / Customer
    participant BAP as Buyer App (BAP)
    participant BG as ONDC Gateway
    participant BPP as Airline Carrier (BPP)

    rect rgb(191, 223, 255)
    User->>BAP: Provide journey search parameters
    BAP->>BG: POST /search
    BG-->>BAP: 200 OK (ACK)
    BG->>BPP: POST /search
    BPP-->>BG: 200 OK (ACK)
    end
    BPP->>BAP: POST /on_search
    BAP-->>BPP: 200 OK (ACK)
    Note over BPP: Unsolicited notification broadcast
    BPP->>BAP: POST /on_search
    BAP-->>BPP: 200 OK (ACK)
    Note over BPP: Unsolicited notification broadcast
    BPP->>BAP: POST /on_search
    BAP-->>BPP: 200 OK (ACK)
    Note over BPP: Unsolicited notification broadcast
    BPP->>BAP: POST /on_search
    BAP-->>BPP: 200 OK (ACK)
```

## on_search_1_Airline_200

```mermaid
sequenceDiagram
    title Airlines - Seller App Pagination Flow
    autonumber
    actor User as Traveler / Customer
    participant BAP as Buyer App (BAP)
    participant BG as ONDC Gateway
    participant BPP as Airline Carrier (BPP)

    User->>BAP: Provide journey search parameters
    BAP->>BG: POST /search
    BG-->>BAP: 200 OK (ACK)
    BG->>BPP: POST /search
    BPP-->>BG: 200 OK (ACK)
    rect rgb(191, 223, 255)
    BPP->>BAP: POST /on_search
    BAP-->>BPP: 200 OK (ACK)
    end
    Note over BPP: Unsolicited notification broadcast
    BPP->>BAP: POST /on_search
    BAP-->>BPP: 200 OK (ACK)
    Note over BPP: Unsolicited notification broadcast
    BPP->>BAP: POST /on_search
    BAP-->>BPP: 200 OK (ACK)
    Note over BPP: Unsolicited notification broadcast
    BPP->>BAP: POST /on_search
    BAP-->>BPP: 200 OK (ACK)
```

## on_search_2_Airline_200

```mermaid
sequenceDiagram
    title Airlines - Seller App Pagination Flow
    autonumber
    actor User as Traveler / Customer
    participant BAP as Buyer App (BAP)
    participant BG as ONDC Gateway
    participant BPP as Airline Carrier (BPP)

    User->>BAP: Provide journey search parameters
    BAP->>BG: POST /search
    BG-->>BAP: 200 OK (ACK)
    BG->>BPP: POST /search
    BPP-->>BG: 200 OK (ACK)
    BPP->>BAP: POST /on_search
    BAP-->>BPP: 200 OK (ACK)
    rect rgb(191, 223, 255)
    Note over BPP: Unsolicited notification broadcast
    BPP->>BAP: POST /on_search
    BAP-->>BPP: 200 OK (ACK)
    end
    Note over BPP: Unsolicited notification broadcast
    BPP->>BAP: POST /on_search
    BAP-->>BPP: 200 OK (ACK)
    Note over BPP: Unsolicited notification broadcast
    BPP->>BAP: POST /on_search
    BAP-->>BPP: 200 OK (ACK)
```

## on_search_3_Airline_200

```mermaid
sequenceDiagram
    title Airlines - Seller App Pagination Flow
    autonumber
    actor User as Traveler / Customer
    participant BAP as Buyer App (BAP)
    participant BG as ONDC Gateway
    participant BPP as Airline Carrier (BPP)

    User->>BAP: Provide journey search parameters
    BAP->>BG: POST /search
    BG-->>BAP: 200 OK (ACK)
    BG->>BPP: POST /search
    BPP-->>BG: 200 OK (ACK)
    BPP->>BAP: POST /on_search
    BAP-->>BPP: 200 OK (ACK)
    Note over BPP: Unsolicited notification broadcast
    BPP->>BAP: POST /on_search
    BAP-->>BPP: 200 OK (ACK)
    rect rgb(191, 223, 255)
    Note over BPP: Unsolicited notification broadcast
    BPP->>BAP: POST /on_search
    BAP-->>BPP: 200 OK (ACK)
    end
    Note over BPP: Unsolicited notification broadcast
    BPP->>BAP: POST /on_search
    BAP-->>BPP: 200 OK (ACK)
```

## on_search_4_Airline_200

```mermaid
sequenceDiagram
    title Airlines - Seller App Pagination Flow
    autonumber
    actor User as Traveler / Customer
    participant BAP as Buyer App (BAP)
    participant BG as ONDC Gateway
    participant BPP as Airline Carrier (BPP)

    User->>BAP: Provide journey search parameters
    BAP->>BG: POST /search
    BG-->>BAP: 200 OK (ACK)
    BG->>BPP: POST /search
    BPP-->>BG: 200 OK (ACK)
    BPP->>BAP: POST /on_search
    BAP-->>BPP: 200 OK (ACK)
    Note over BPP: Unsolicited notification broadcast
    BPP->>BAP: POST /on_search
    BAP-->>BPP: 200 OK (ACK)
    Note over BPP: Unsolicited notification broadcast
    BPP->>BAP: POST /on_search
    BAP-->>BPP: 200 OK (ACK)
    rect rgb(191, 223, 255)
    Note over BPP: Unsolicited notification broadcast
    BPP->>BAP: POST /on_search
    BAP-->>BPP: 200 OK (ACK)
    end
```

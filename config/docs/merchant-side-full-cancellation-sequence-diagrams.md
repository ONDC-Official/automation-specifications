# Merchant Side Full Cancellation — Sequence Diagrams

Internal data file consumed by the Developer Guide's "Sequence Diagram" tab (API Walkthrough).
Not meant to be shown as its own docs page — the frontend filters this slug out of the Use Case
Brief / Additional Resources / Changelog tab lists and instead looks up the section matching the
selected API call's `action_id` (the `##` heading below) to render that step's diagram.

One `## <action_id>` heading per step of `Merchant_Side_Full_Cancellation.yaml`, in that flow's own step order, each followed by its Mermaid `sequenceDiagram`: the whole flow, with that call's own message(s) highlighted — same convention as the other domains' per-step sequence-diagram docs.

## select_5

```mermaid
sequenceDiagram
  participant Buyer App (BAP)
  participant Seller App (BPP)
  rect rgb(191, 223, 255)
  Buyer App (BAP)->>Seller App (BPP): /select (hotel rooms, stay dates)
  end
  Seller App (BPP)-->>Buyer App (BAP): /on_select (quote, room availability)
  Buyer App (BAP)->>Seller App (BPP): /init (guest details, billing)
  Seller App (BPP)-->>Buyer App (BAP): /on_init (final quote, payment terms)
  Buyer App (BAP)->>Seller App (BPP): /confirm (place hotel reservation)
  Seller App (BPP)-->>Buyer App (BAP): /on_confirm (booking confirmed, voucher issued)
  Buyer App (BAP)->>Seller App (BPP): /status
  Seller App (BPP)-->>Buyer App (BAP): /on_status (active reservation)
  Seller App (BPP)-->>Buyer App (BAP): /on_cancel (unsolicited): cancelled by hotel
```

## on_select_5

```mermaid
sequenceDiagram
  participant Buyer App (BAP)
  participant Seller App (BPP)
  Buyer App (BAP)->>Seller App (BPP): /select (hotel rooms, stay dates)
  rect rgb(191, 223, 255)
  Seller App (BPP)-->>Buyer App (BAP): /on_select (quote, room availability)
  end
  Buyer App (BAP)->>Seller App (BPP): /init (guest details, billing)
  Seller App (BPP)-->>Buyer App (BAP): /on_init (final quote, payment terms)
  Buyer App (BAP)->>Seller App (BPP): /confirm (place hotel reservation)
  Seller App (BPP)-->>Buyer App (BAP): /on_confirm (booking confirmed, voucher issued)
  Buyer App (BAP)->>Seller App (BPP): /status
  Seller App (BPP)-->>Buyer App (BAP): /on_status (active reservation)
  Seller App (BPP)-->>Buyer App (BAP): /on_cancel (unsolicited): cancelled by hotel
```

## init_5

```mermaid
sequenceDiagram
  participant Buyer App (BAP)
  participant Seller App (BPP)
  Buyer App (BAP)->>Seller App (BPP): /select (hotel rooms, stay dates)
  Seller App (BPP)-->>Buyer App (BAP): /on_select (quote, room availability)
  rect rgb(191, 223, 255)
  Buyer App (BAP)->>Seller App (BPP): /init (guest details, billing)
  end
  Seller App (BPP)-->>Buyer App (BAP): /on_init (final quote, payment terms)
  Buyer App (BAP)->>Seller App (BPP): /confirm (place hotel reservation)
  Seller App (BPP)-->>Buyer App (BAP): /on_confirm (booking confirmed, voucher issued)
  Buyer App (BAP)->>Seller App (BPP): /status
  Seller App (BPP)-->>Buyer App (BAP): /on_status (active reservation)
  Seller App (BPP)-->>Buyer App (BAP): /on_cancel (unsolicited): cancelled by hotel
```

## on_init_5

```mermaid
sequenceDiagram
  participant Buyer App (BAP)
  participant Seller App (BPP)
  Buyer App (BAP)->>Seller App (BPP): /select (hotel rooms, stay dates)
  Seller App (BPP)-->>Buyer App (BAP): /on_select (quote, room availability)
  Buyer App (BAP)->>Seller App (BPP): /init (guest details, billing)
  rect rgb(191, 223, 255)
  Seller App (BPP)-->>Buyer App (BAP): /on_init (final quote, payment terms)
  end
  Buyer App (BAP)->>Seller App (BPP): /confirm (place hotel reservation)
  Seller App (BPP)-->>Buyer App (BAP): /on_confirm (booking confirmed, voucher issued)
  Buyer App (BAP)->>Seller App (BPP): /status
  Seller App (BPP)-->>Buyer App (BAP): /on_status (active reservation)
  Seller App (BPP)-->>Buyer App (BAP): /on_cancel (unsolicited): cancelled by hotel
```

## confirm_5

```mermaid
sequenceDiagram
  participant Buyer App (BAP)
  participant Seller App (BPP)
  Buyer App (BAP)->>Seller App (BPP): /select (hotel rooms, stay dates)
  Seller App (BPP)-->>Buyer App (BAP): /on_select (quote, room availability)
  Buyer App (BAP)->>Seller App (BPP): /init (guest details, billing)
  Seller App (BPP)-->>Buyer App (BAP): /on_init (final quote, payment terms)
  rect rgb(191, 223, 255)
  Buyer App (BAP)->>Seller App (BPP): /confirm (place hotel reservation)
  end
  Seller App (BPP)-->>Buyer App (BAP): /on_confirm (booking confirmed, voucher issued)
  Buyer App (BAP)->>Seller App (BPP): /status
  Seller App (BPP)-->>Buyer App (BAP): /on_status (active reservation)
  Seller App (BPP)-->>Buyer App (BAP): /on_cancel (unsolicited): cancelled by hotel
```

## on_confirm_5

```mermaid
sequenceDiagram
  participant Buyer App (BAP)
  participant Seller App (BPP)
  Buyer App (BAP)->>Seller App (BPP): /select (hotel rooms, stay dates)
  Seller App (BPP)-->>Buyer App (BAP): /on_select (quote, room availability)
  Buyer App (BAP)->>Seller App (BPP): /init (guest details, billing)
  Seller App (BPP)-->>Buyer App (BAP): /on_init (final quote, payment terms)
  Buyer App (BAP)->>Seller App (BPP): /confirm (place hotel reservation)
  rect rgb(191, 223, 255)
  Seller App (BPP)-->>Buyer App (BAP): /on_confirm (booking confirmed, voucher issued)
  end
  Buyer App (BAP)->>Seller App (BPP): /status
  Seller App (BPP)-->>Buyer App (BAP): /on_status (active reservation)
  Seller App (BPP)-->>Buyer App (BAP): /on_cancel (unsolicited): cancelled by hotel
```

## status_5

```mermaid
sequenceDiagram
  participant Buyer App (BAP)
  participant Seller App (BPP)
  Buyer App (BAP)->>Seller App (BPP): /select (hotel rooms, stay dates)
  Seller App (BPP)-->>Buyer App (BAP): /on_select (quote, room availability)
  Buyer App (BAP)->>Seller App (BPP): /init (guest details, billing)
  Seller App (BPP)-->>Buyer App (BAP): /on_init (final quote, payment terms)
  Buyer App (BAP)->>Seller App (BPP): /confirm (place hotel reservation)
  Seller App (BPP)-->>Buyer App (BAP): /on_confirm (booking confirmed, voucher issued)
  rect rgb(191, 223, 255)
  Buyer App (BAP)->>Seller App (BPP): /status
  end
  Seller App (BPP)-->>Buyer App (BAP): /on_status (active reservation)
  Seller App (BPP)-->>Buyer App (BAP): /on_cancel (unsolicited): cancelled by hotel
```

## on_status_5

```mermaid
sequenceDiagram
  participant Buyer App (BAP)
  participant Seller App (BPP)
  Buyer App (BAP)->>Seller App (BPP): /select (hotel rooms, stay dates)
  Seller App (BPP)-->>Buyer App (BAP): /on_select (quote, room availability)
  Buyer App (BAP)->>Seller App (BPP): /init (guest details, billing)
  Seller App (BPP)-->>Buyer App (BAP): /on_init (final quote, payment terms)
  Buyer App (BAP)->>Seller App (BPP): /confirm (place hotel reservation)
  Seller App (BPP)-->>Buyer App (BAP): /on_confirm (booking confirmed, voucher issued)
  Buyer App (BAP)->>Seller App (BPP): /status
  rect rgb(191, 223, 255)
  Seller App (BPP)-->>Buyer App (BAP): /on_status (active reservation)
  end
  Seller App (BPP)-->>Buyer App (BAP): /on_cancel (unsolicited): cancelled by hotel
```

## on_cancel_unsolicited

```mermaid
sequenceDiagram
  participant Buyer App (BAP)
  participant Seller App (BPP)
  Buyer App (BAP)->>Seller App (BPP): /select (hotel rooms, stay dates)
  Seller App (BPP)-->>Buyer App (BAP): /on_select (quote, room availability)
  Buyer App (BAP)->>Seller App (BPP): /init (guest details, billing)
  Seller App (BPP)-->>Buyer App (BAP): /on_init (final quote, payment terms)
  Buyer App (BAP)->>Seller App (BPP): /confirm (place hotel reservation)
  Seller App (BPP)-->>Buyer App (BAP): /on_confirm (booking confirmed, voucher issued)
  Buyer App (BAP)->>Seller App (BPP): /status
  Seller App (BPP)-->>Buyer App (BAP): /on_status (active reservation)
  rect rgb(191, 223, 255)
  Seller App (BPP)-->>Buyer App (BAP): /on_cancel (unsolicited): cancelled by hotel
  end
```

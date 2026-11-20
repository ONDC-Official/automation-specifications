# User Cancellation FULL With Form — Sequence Diagrams

Internal data file consumed by the Developer Guide's "Sequence Diagram" tab (API Walkthrough).
Not meant to be shown as its own docs page — the frontend filters this slug out of the Use Case
Brief / Additional Resources / Changelog tab lists and instead looks up the section matching the
selected API call's `action_id` (the `##` heading below) to render that step's diagram.

One `## <action_id>` heading per step of `User_Cancellation_FULL_With_Form.yaml`, in that flow's own step order, each followed by its Mermaid `sequenceDiagram`: the whole flow, with that call's own message(s) highlighted — same convention as the other domains' per-step sequence-diagram docs.

## select

```mermaid
sequenceDiagram
  participant Buyer App (BAP)
  participant Seller App (BPP)
  participant Seller Form Service
  rect rgb(191, 223, 255)
  Buyer App (BAP)->>Seller App (BPP): /select (items, attraction pass)
  end
  Seller App (BPP)-->>Buyer App (BAP): /on_select (form URL for visitor details)
  Buyer App (BAP)->>Seller Form Service: Load form & submit visitor details
  Seller Form Service-->>Buyer App (BAP): Submission ID
  Buyer App (BAP)->>Seller App (BPP): /select (with submission_id)
  Seller App (BPP)-->>Buyer App (BAP): /on_select (quote, validated details)
  Buyer App (BAP)->>Seller App (BPP): /init (billing)
  Seller App (BPP)-->>Buyer App (BAP): /on_init (final quote, payment terms)
  Buyer App (BAP)->>Seller App (BPP): /confirm (purchase tickets)
  Seller App (BPP)-->>Buyer App (BAP): /on_confirm (booking confirmed, ticket issued)
  Buyer App (BAP)->>Seller App (BPP): /cancel (soft cancel)
  Seller App (BPP)-->>Buyer App (BAP): /on_cancel (cancellation quote & terms)
  Buyer App (BAP)->>Seller App (BPP): /cancel (confirm cancellation)
  Seller App (BPP)-->>Buyer App (BAP): /on_cancel (booking cancelled, refund initiated)
```

## on_select

```mermaid
sequenceDiagram
  participant Buyer App (BAP)
  participant Seller App (BPP)
  participant Seller Form Service
  Buyer App (BAP)->>Seller App (BPP): /select (items, attraction pass)
  rect rgb(191, 223, 255)
  Seller App (BPP)-->>Buyer App (BAP): /on_select (form URL for visitor details)
  end
  Buyer App (BAP)->>Seller Form Service: Load form & submit visitor details
  Seller Form Service-->>Buyer App (BAP): Submission ID
  Buyer App (BAP)->>Seller App (BPP): /select (with submission_id)
  Seller App (BPP)-->>Buyer App (BAP): /on_select (quote, validated details)
  Buyer App (BAP)->>Seller App (BPP): /init (billing)
  Seller App (BPP)-->>Buyer App (BAP): /on_init (final quote, payment terms)
  Buyer App (BAP)->>Seller App (BPP): /confirm (purchase tickets)
  Seller App (BPP)-->>Buyer App (BAP): /on_confirm (booking confirmed, ticket issued)
  Buyer App (BAP)->>Seller App (BPP): /cancel (soft cancel)
  Seller App (BPP)-->>Buyer App (BAP): /on_cancel (cancellation quote & terms)
  Buyer App (BAP)->>Seller App (BPP): /cancel (confirm cancellation)
  Seller App (BPP)-->>Buyer App (BAP): /on_cancel (booking cancelled, refund initiated)
```

## first_form_testing

```mermaid
sequenceDiagram
  participant Buyer App (BAP)
  participant Seller App (BPP)
  participant Seller Form Service
  Buyer App (BAP)->>Seller App (BPP): /select (items, attraction pass)
  Seller App (BPP)-->>Buyer App (BAP): /on_select (form URL for visitor details)
  rect rgb(191, 223, 255)
  Buyer App (BAP)->>Seller Form Service: Load form & submit visitor details
  Seller Form Service-->>Buyer App (BAP): Submission ID
  end
  Buyer App (BAP)->>Seller App (BPP): /select (with submission_id)
  Seller App (BPP)-->>Buyer App (BAP): /on_select (quote, validated details)
  Buyer App (BAP)->>Seller App (BPP): /init (billing)
  Seller App (BPP)-->>Buyer App (BAP): /on_init (final quote, payment terms)
  Buyer App (BAP)->>Seller App (BPP): /confirm (purchase tickets)
  Seller App (BPP)-->>Buyer App (BAP): /on_confirm (booking confirmed, ticket issued)
  Buyer App (BAP)->>Seller App (BPP): /cancel (soft cancel)
  Seller App (BPP)-->>Buyer App (BAP): /on_cancel (cancellation quote & terms)
  Buyer App (BAP)->>Seller App (BPP): /cancel (confirm cancellation)
  Seller App (BPP)-->>Buyer App (BAP): /on_cancel (booking cancelled, refund initiated)
```

## select_form_submission

```mermaid
sequenceDiagram
  participant Buyer App (BAP)
  participant Seller App (BPP)
  participant Seller Form Service
  Buyer App (BAP)->>Seller App (BPP): /select (items, attraction pass)
  Seller App (BPP)-->>Buyer App (BAP): /on_select (form URL for visitor details)
  Buyer App (BAP)->>Seller Form Service: Load form & submit visitor details
  Seller Form Service-->>Buyer App (BAP): Submission ID
  rect rgb(191, 223, 255)
  Buyer App (BAP)->>Seller App (BPP): /select (with submission_id)
  end
  Seller App (BPP)-->>Buyer App (BAP): /on_select (quote, validated details)
  Buyer App (BAP)->>Seller App (BPP): /init (billing)
  Seller App (BPP)-->>Buyer App (BAP): /on_init (final quote, payment terms)
  Buyer App (BAP)->>Seller App (BPP): /confirm (purchase tickets)
  Seller App (BPP)-->>Buyer App (BAP): /on_confirm (booking confirmed, ticket issued)
  Buyer App (BAP)->>Seller App (BPP): /cancel (soft cancel)
  Seller App (BPP)-->>Buyer App (BAP): /on_cancel (cancellation quote & terms)
  Buyer App (BAP)->>Seller App (BPP): /cancel (confirm cancellation)
  Seller App (BPP)-->>Buyer App (BAP): /on_cancel (booking cancelled, refund initiated)
```

## on_select_form_submission

```mermaid
sequenceDiagram
  participant Buyer App (BAP)
  participant Seller App (BPP)
  participant Seller Form Service
  Buyer App (BAP)->>Seller App (BPP): /select (items, attraction pass)
  Seller App (BPP)-->>Buyer App (BAP): /on_select (form URL for visitor details)
  Buyer App (BAP)->>Seller Form Service: Load form & submit visitor details
  Seller Form Service-->>Buyer App (BAP): Submission ID
  Buyer App (BAP)->>Seller App (BPP): /select (with submission_id)
  rect rgb(191, 223, 255)
  Seller App (BPP)-->>Buyer App (BAP): /on_select (quote, validated details)
  end
  Buyer App (BAP)->>Seller App (BPP): /init (billing)
  Seller App (BPP)-->>Buyer App (BAP): /on_init (final quote, payment terms)
  Buyer App (BAP)->>Seller App (BPP): /confirm (purchase tickets)
  Seller App (BPP)-->>Buyer App (BAP): /on_confirm (booking confirmed, ticket issued)
  Buyer App (BAP)->>Seller App (BPP): /cancel (soft cancel)
  Seller App (BPP)-->>Buyer App (BAP): /on_cancel (cancellation quote & terms)
  Buyer App (BAP)->>Seller App (BPP): /cancel (confirm cancellation)
  Seller App (BPP)-->>Buyer App (BAP): /on_cancel (booking cancelled, refund initiated)
```

## init

```mermaid
sequenceDiagram
  participant Buyer App (BAP)
  participant Seller App (BPP)
  participant Seller Form Service
  Buyer App (BAP)->>Seller App (BPP): /select (items, attraction pass)
  Seller App (BPP)-->>Buyer App (BAP): /on_select (form URL for visitor details)
  Buyer App (BAP)->>Seller Form Service: Load form & submit visitor details
  Seller Form Service-->>Buyer App (BAP): Submission ID
  Buyer App (BAP)->>Seller App (BPP): /select (with submission_id)
  Seller App (BPP)-->>Buyer App (BAP): /on_select (quote, validated details)
  rect rgb(191, 223, 255)
  Buyer App (BAP)->>Seller App (BPP): /init (billing)
  end
  Seller App (BPP)-->>Buyer App (BAP): /on_init (final quote, payment terms)
  Buyer App (BAP)->>Seller App (BPP): /confirm (purchase tickets)
  Seller App (BPP)-->>Buyer App (BAP): /on_confirm (booking confirmed, ticket issued)
  Buyer App (BAP)->>Seller App (BPP): /cancel (soft cancel)
  Seller App (BPP)-->>Buyer App (BAP): /on_cancel (cancellation quote & terms)
  Buyer App (BAP)->>Seller App (BPP): /cancel (confirm cancellation)
  Seller App (BPP)-->>Buyer App (BAP): /on_cancel (booking cancelled, refund initiated)
```

## on_init

```mermaid
sequenceDiagram
  participant Buyer App (BAP)
  participant Seller App (BPP)
  participant Seller Form Service
  Buyer App (BAP)->>Seller App (BPP): /select (items, attraction pass)
  Seller App (BPP)-->>Buyer App (BAP): /on_select (form URL for visitor details)
  Buyer App (BAP)->>Seller Form Service: Load form & submit visitor details
  Seller Form Service-->>Buyer App (BAP): Submission ID
  Buyer App (BAP)->>Seller App (BPP): /select (with submission_id)
  Seller App (BPP)-->>Buyer App (BAP): /on_select (quote, validated details)
  Buyer App (BAP)->>Seller App (BPP): /init (billing)
  rect rgb(191, 223, 255)
  Seller App (BPP)-->>Buyer App (BAP): /on_init (final quote, payment terms)
  end
  Buyer App (BAP)->>Seller App (BPP): /confirm (purchase tickets)
  Seller App (BPP)-->>Buyer App (BAP): /on_confirm (booking confirmed, ticket issued)
  Buyer App (BAP)->>Seller App (BPP): /cancel (soft cancel)
  Seller App (BPP)-->>Buyer App (BAP): /on_cancel (cancellation quote & terms)
  Buyer App (BAP)->>Seller App (BPP): /cancel (confirm cancellation)
  Seller App (BPP)-->>Buyer App (BAP): /on_cancel (booking cancelled, refund initiated)
```

## confirm

```mermaid
sequenceDiagram
  participant Buyer App (BAP)
  participant Seller App (BPP)
  participant Seller Form Service
  Buyer App (BAP)->>Seller App (BPP): /select (items, attraction pass)
  Seller App (BPP)-->>Buyer App (BAP): /on_select (form URL for visitor details)
  Buyer App (BAP)->>Seller Form Service: Load form & submit visitor details
  Seller Form Service-->>Buyer App (BAP): Submission ID
  Buyer App (BAP)->>Seller App (BPP): /select (with submission_id)
  Seller App (BPP)-->>Buyer App (BAP): /on_select (quote, validated details)
  Buyer App (BAP)->>Seller App (BPP): /init (billing)
  Seller App (BPP)-->>Buyer App (BAP): /on_init (final quote, payment terms)
  rect rgb(191, 223, 255)
  Buyer App (BAP)->>Seller App (BPP): /confirm (purchase tickets)
  end
  Seller App (BPP)-->>Buyer App (BAP): /on_confirm (booking confirmed, ticket issued)
  Buyer App (BAP)->>Seller App (BPP): /cancel (soft cancel)
  Seller App (BPP)-->>Buyer App (BAP): /on_cancel (cancellation quote & terms)
  Buyer App (BAP)->>Seller App (BPP): /cancel (confirm cancellation)
  Seller App (BPP)-->>Buyer App (BAP): /on_cancel (booking cancelled, refund initiated)
```

## on_confirm

```mermaid
sequenceDiagram
  participant Buyer App (BAP)
  participant Seller App (BPP)
  participant Seller Form Service
  Buyer App (BAP)->>Seller App (BPP): /select (items, attraction pass)
  Seller App (BPP)-->>Buyer App (BAP): /on_select (form URL for visitor details)
  Buyer App (BAP)->>Seller Form Service: Load form & submit visitor details
  Seller Form Service-->>Buyer App (BAP): Submission ID
  Buyer App (BAP)->>Seller App (BPP): /select (with submission_id)
  Seller App (BPP)-->>Buyer App (BAP): /on_select (quote, validated details)
  Buyer App (BAP)->>Seller App (BPP): /init (billing)
  Seller App (BPP)-->>Buyer App (BAP): /on_init (final quote, payment terms)
  Buyer App (BAP)->>Seller App (BPP): /confirm (purchase tickets)
  rect rgb(191, 223, 255)
  Seller App (BPP)-->>Buyer App (BAP): /on_confirm (booking confirmed, ticket issued)
  end
  Buyer App (BAP)->>Seller App (BPP): /cancel (soft cancel)
  Seller App (BPP)-->>Buyer App (BAP): /on_cancel (cancellation quote & terms)
  Buyer App (BAP)->>Seller App (BPP): /cancel (confirm cancellation)
  Seller App (BPP)-->>Buyer App (BAP): /on_cancel (booking cancelled, refund initiated)
```

## cancel_soft_user_cancellation

```mermaid
sequenceDiagram
  participant Buyer App (BAP)
  participant Seller App (BPP)
  participant Seller Form Service
  Buyer App (BAP)->>Seller App (BPP): /select (items, attraction pass)
  Seller App (BPP)-->>Buyer App (BAP): /on_select (form URL for visitor details)
  Buyer App (BAP)->>Seller Form Service: Load form & submit visitor details
  Seller Form Service-->>Buyer App (BAP): Submission ID
  Buyer App (BAP)->>Seller App (BPP): /select (with submission_id)
  Seller App (BPP)-->>Buyer App (BAP): /on_select (quote, validated details)
  Buyer App (BAP)->>Seller App (BPP): /init (billing)
  Seller App (BPP)-->>Buyer App (BAP): /on_init (final quote, payment terms)
  Buyer App (BAP)->>Seller App (BPP): /confirm (purchase tickets)
  Seller App (BPP)-->>Buyer App (BAP): /on_confirm (booking confirmed, ticket issued)
  rect rgb(191, 223, 255)
  Buyer App (BAP)->>Seller App (BPP): /cancel (soft cancel)
  end
  Seller App (BPP)-->>Buyer App (BAP): /on_cancel (cancellation quote & terms)
  Buyer App (BAP)->>Seller App (BPP): /cancel (confirm cancellation)
  Seller App (BPP)-->>Buyer App (BAP): /on_cancel (booking cancelled, refund initiated)
```

## on_cancel_soft_user_cancellation

```mermaid
sequenceDiagram
  participant Buyer App (BAP)
  participant Seller App (BPP)
  participant Seller Form Service
  Buyer App (BAP)->>Seller App (BPP): /select (items, attraction pass)
  Seller App (BPP)-->>Buyer App (BAP): /on_select (form URL for visitor details)
  Buyer App (BAP)->>Seller Form Service: Load form & submit visitor details
  Seller Form Service-->>Buyer App (BAP): Submission ID
  Buyer App (BAP)->>Seller App (BPP): /select (with submission_id)
  Seller App (BPP)-->>Buyer App (BAP): /on_select (quote, validated details)
  Buyer App (BAP)->>Seller App (BPP): /init (billing)
  Seller App (BPP)-->>Buyer App (BAP): /on_init (final quote, payment terms)
  Buyer App (BAP)->>Seller App (BPP): /confirm (purchase tickets)
  Seller App (BPP)-->>Buyer App (BAP): /on_confirm (booking confirmed, ticket issued)
  Buyer App (BAP)->>Seller App (BPP): /cancel (soft cancel)
  rect rgb(191, 223, 255)
  Seller App (BPP)-->>Buyer App (BAP): /on_cancel (cancellation quote & terms)
  end
  Buyer App (BAP)->>Seller App (BPP): /cancel (confirm cancellation)
  Seller App (BPP)-->>Buyer App (BAP): /on_cancel (booking cancelled, refund initiated)
```

## cancel_confirm_user_cancellation

```mermaid
sequenceDiagram
  participant Buyer App (BAP)
  participant Seller App (BPP)
  participant Seller Form Service
  Buyer App (BAP)->>Seller App (BPP): /select (items, attraction pass)
  Seller App (BPP)-->>Buyer App (BAP): /on_select (form URL for visitor details)
  Buyer App (BAP)->>Seller Form Service: Load form & submit visitor details
  Seller Form Service-->>Buyer App (BAP): Submission ID
  Buyer App (BAP)->>Seller App (BPP): /select (with submission_id)
  Seller App (BPP)-->>Buyer App (BAP): /on_select (quote, validated details)
  Buyer App (BAP)->>Seller App (BPP): /init (billing)
  Seller App (BPP)-->>Buyer App (BAP): /on_init (final quote, payment terms)
  Buyer App (BAP)->>Seller App (BPP): /confirm (purchase tickets)
  Seller App (BPP)-->>Buyer App (BAP): /on_confirm (booking confirmed, ticket issued)
  Buyer App (BAP)->>Seller App (BPP): /cancel (soft cancel)
  Seller App (BPP)-->>Buyer App (BAP): /on_cancel (cancellation quote & terms)
  rect rgb(191, 223, 255)
  Buyer App (BAP)->>Seller App (BPP): /cancel (confirm cancellation)
  end
  Seller App (BPP)-->>Buyer App (BAP): /on_cancel (booking cancelled, refund initiated)
```

## on_cancel_confirm_user_cancellation

```mermaid
sequenceDiagram
  participant Buyer App (BAP)
  participant Seller App (BPP)
  participant Seller Form Service
  Buyer App (BAP)->>Seller App (BPP): /select (items, attraction pass)
  Seller App (BPP)-->>Buyer App (BAP): /on_select (form URL for visitor details)
  Buyer App (BAP)->>Seller Form Service: Load form & submit visitor details
  Seller Form Service-->>Buyer App (BAP): Submission ID
  Buyer App (BAP)->>Seller App (BPP): /select (with submission_id)
  Seller App (BPP)-->>Buyer App (BAP): /on_select (quote, validated details)
  Buyer App (BAP)->>Seller App (BPP): /init (billing)
  Seller App (BPP)-->>Buyer App (BAP): /on_init (final quote, payment terms)
  Buyer App (BAP)->>Seller App (BPP): /confirm (purchase tickets)
  Seller App (BPP)-->>Buyer App (BAP): /on_confirm (booking confirmed, ticket issued)
  Buyer App (BAP)->>Seller App (BPP): /cancel (soft cancel)
  Seller App (BPP)-->>Buyer App (BAP): /on_cancel (cancellation quote & terms)
  Buyer App (BAP)->>Seller App (BPP): /cancel (confirm cancellation)
  rect rgb(191, 223, 255)
  Seller App (BPP)-->>Buyer App (BAP): /on_cancel (booking cancelled, refund initiated)
  end
```

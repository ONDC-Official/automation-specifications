# ONDC:NTS10 2.1.0 — Overview

## Summary
ONDC:NTS10 carries the Reconciliation and Settlement Framework (RSF 2.1.0) between network participants. When settlement instructions fail because of an order or order amount mismatch, the collector and the receiver reconcile through the `recon` and `on_recon` APIs. The flow is bi-directional: either side can initiate it.

## Real-World Actors
- **Collector**: collects the payment for orders and settles the receiver's share.
- **Receiver**: receives its share and reconciles it against its orders.

## APIs in scope
- `recon` — shares the order, its quote breakup and the settlements held, to understand the discrepancy.
- `on_recon` — responds with `recon_accord` false and the `diff_value` per settlement, `recon_accord` true when it agrees, or an error such as 70030 (Invalid Order Id).

## Use Cases
- RSF
- RECON: recon, on_recon (disagree), recon (agree), on_recon (agree)
- ERROR (on_recon): recon, on_recon with an error

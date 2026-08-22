---
id: concept.soft-lock-expiry
kind: concept
layer: domain
status: draft
asof: trv12-2.0.0
---

# concept.soft-lock-expiry

Declared node for `concept.soft-lock-expiry` — expiry of that hold before `init` completes, which returns the BAP to selection instead of letting the transaction proceed.

Grounded at: `trv12-2.0.0:flows/Intercity/Intercity_Bus__Error_Response_Soft_Locking_Time_.yaml#steps[on_init_BUS_221].description`

Facts live in `atoms.md` under the handle `anchor.soft-lock-expiry`; body intentionally light — no prose
assertions beyond this declaration.

The error path is modelled on the *distinct confined subject* `anchor.on-init-soft-lock-expired`
(`isa anchor.on-init`, `scoped-to anchor.soft-lock-expiry`), so the general rule that
`anchor.on-init` precedes `anchor.confirm` stands unchallenged. Do not collapse the two.

---
id: concept.station-code-discovery
kind: concept
layer: domain
status: draft
asof: trv12-2.0.0
---

# concept.station-code-discovery

Declared node for `concept.station-code-discovery` — progressive Intercity discovery that narrows origin → route → segment across successive `search` rounds keyed by station code.

Grounded at: `trv12-2.0.0:flows/Intercity/Intercity_Bus__Station_Code_Based_Flow.yaml#steps[search_BUS_202].mock.defaultPayload.message.intent.fulfillment.stops`

Facts live in `atoms.md` under the handle `anchor.station-code-discovery`; body intentionally light — no prose
assertions beyond this declaration.

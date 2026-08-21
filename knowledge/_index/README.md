# Index spine (Stage G, consolidated)

Built from 16 books / 10781 units / 7774 distinct grounded config node-paths.

## Files

| file | what it answers |
|---|---|
| `reverse-index.json` | *which units are grounded at this config node-path?* — key is `<book>:<file>#<node>` |
| `blast-radius.json` | *if this config file changes, how much of the KB must be revisited?* |
| `cross-book.json` | *which interned meanings are shared across books vs book-specific?* |

## Selective regeneration

A config change revisits only the units grounded at the changed node-path, plus one PROV-O
hop (anything derived from an affected subject). Everything else is untouched — that is the
whole return on positional grounding.

## Highest blast radius (change these files and the most units need revisiting)

| config file | direct | +prov hop | untouched in book |
|---|---|---|---|
| `trv12-2.0.0:validations/index.yaml` | 374 | 0 | 363 |
| `fis12-2.3.0:validations/index.yaml` | 337 | 8 | 694 |
| `trv10-2.1.0:validations/index.yaml` | 340 | 0 | 445 |
| `trv11-2.0.0:validations/index.yaml` | 309 | 0 | 377 |
| `trv10-2.0.1:validations/index.yaml` | 305 | 1 | 545 |
| `trv14-2.0.0:validations/index.yaml` | 304 | 0 | 447 |
| `fis13-sachet:validations/index.yaml` | 289 | 5 | 399 |
| `fis13-health-2.0.0:validations/index.yaml` | 257 | 0 | 513 |
| `trv11-2.1.0:validations/index.yaml` | 177 | 27 | 438 |
| `trv10-2.0.1:attributes/Ride_hailing.yaml` | 194 | 1 | 656 |
| `fis12-pf-2.2.1:validations/index.yaml` | 182 | 0 | 333 |
| `fis12-2.0.3:validations/index.yaml` | 150 | 4 | 413 |

## Cross-book meaning reuse

- interned meanings shared by >1 book: **396**
- book-specific meanings: **2196**
- present in both the FIS and TRV families: **210**
- FIS-family only: **1320** · TRV-family only: **1062**


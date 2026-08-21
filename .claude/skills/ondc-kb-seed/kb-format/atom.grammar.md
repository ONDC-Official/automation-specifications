# Atom line grammar (EBNF)

> **The atom.** A **mandatory triple + `basis` + `asof`**, an **optional `grounded-in` pointer**, and
> **optional `!exception` flags**. `basis` is one field for what backs a fact — its source kind, its
> grounding *kind*, and its derivation status; `plane`, `scope`, `maturity`, and `grounding-status` are
> **derived, not stored** — written only when a unit deviates, as an `!flag`. This grammar accepts the full
> maturity range (bare triple → mature atom); the base triple is head-only. See
> [`../committed/unit.md`](../committed/unit.md), [`../committed/vocabularies.md`](../committed/vocabularies.md),
> and [`../committed/anchor.md`](../committed/anchor.md).

```ebnf
unit       = triple , { ws "|" ws field } ;
triple     = subject ws "|" ws relation ws "|" ws object ;   (* the only mandatory part *)

field      = basis | asof | grounded | flag ;                (* order fixed for greppability:
                                                                basis, asof, grounded-in, then flags *)
basis      = "basis:" basis-val ;
asof       = "asof:" version ;
grounded   = "grounded-in:" anchor ;                          (* optional pointer; NO kind prefix *)
flag       = "!" flag-name [ "=" flag-arg ] ;                 (* only present when the unit deviates *)

subject    = handle | literal ;
object     = handle | literal ;
handle     = kebab , { "." , kebab } ;                        (* dotted handles allowed for paths *)
literal    = '"' , { char } , '"' ;

relation   = [ "not-" ] , relation-base ;
relation-base = "isa" | "has-slot" | "part-of" | "disjoint-with" | "scoped-to" | "sent-by"
              | "precedes" | "requires" | "causes" | "constrains"
              | "wasDerivedFrom" | "wasRevisionOf" | "wasInformedBy"
              | "wasAttributedTo" | "wasGeneratedBy" | "used" ;   (* flat registry, openly extensible *)

basis-val  = "declared" | "sandbox-tested" | "observed-live"
           | "authority" | "ecosystem" | "derived" | "inferred" ;

anchor     = config-node | ref ;                             (* interpreted per basis-val *)
config-node= book ":" file "#" node ;                        (* basis:declared → a POSITIONAL config node-path *)

flag-name  = "untethered" | "deprecated" | "desired" | "plane" ;
flag-arg   = "spec" | "session-logic" | "runtime-state" | "cross" ;   (* only for !plane= *)

version    = kebab ;
ref        = kebab ;                                         (* obs/authority/unit/anchor handle (no '#') *)
book       = kebab ;                                         (* domain+version coordinate, e.g. fis12-2.3.0 *)
file       = { char - ("#" | "|") } ;                        (* config file path within the book *)
node       = { char - "|" } ;                                (* a positional node-path — NEVER a bare line number *)
kebab      = lower , { lower | digit | "-" | "_" } ;
```

## Cross-field constraints (not expressible in EBNF; enforced by the validator)

- **basis:inferred ⇔ no `grounded-in`.** An inferred fact has no anchor and is never asserted.
- **grounded-in present ⇒ basis ≠ inferred.**
- **config anchor** (a `grounded-in` containing `#`, under `basis:declared`) is a **positional node-path**
  (`<book>:<file>#<node-path>`); its node part must not match `/^L?\d+$/` (no line-number anchors).
- **interned meaning ⇒ anchor handle.** A meaning grounded at a config `&anchor`, or recurring in ≥2
  positions, is referenced as an `anchor.*` handle, never restated inline (interning invariant).
- **untethered-must-be-tagged.** If `grounded-in` is absent **and** `basis ∉ {inferred, ecosystem}`, the
  unit must carry `!untethered` (or `!deprecated`). Silent dangling is invalid.
- **flags** are the only status written by hand: `!untethered · !deprecated · !desired · !plane=<p>`.

## Derived (never stored on the line — computed at load)

| axis | derivation rule | override |
|---|---|---|
| `maturity` | count of fields present: triple-only → `bare`; some accretions → `partially-grounded`; `basis`+`asof`+ground → `mature` | — (pure function) |
| `plane` | `precedes`/`wasInformedBy` → `session-logic`; `basis ∈ {authority, ecosystem}` → `cross`; `basis ∈ {sandbox-tested, observed-live}` → `runtime-state`; else `spec` | `!plane=<p>` |
| `scope` | `live`, unless the unit carries `!desired` | `!desired` |
| `grounding-status` | `grounded` when `grounded-in` resolves; otherwise must carry `!untethered`/`!deprecated` | those flags |

## Examples

```text
# mature — grounded in config at a POSITIONAL node-path, everything else derived
dom.consent.authz | isa | cross.consent | basis:declared | asof:dom-a1-1.0.0 | grounded-in:dom-a1-1.0.0:attributes/index.yaml#attributes.authorization

# interned meaning — the unit stays light, carrying an anchor handle (not restated content)
item.loan-info | has-slot | anchor.loan-info-tags | basis:declared | asof:fis12-2.3.0 | grounded-in:fis12-2.3.0:validations/index.yaml#loanInfoTags

# position carries meaning — one anchor confined to its context, grounded at the position that scopes it
anchor.pan | scoped-to | anchor.xinput-form-data | basis:declared | asof:fis12-2.3.0 | grounded-in:fis12-2.3.0:flows/LAMF/lamf_credit_line_with_mfc#steps[search_1].inputs.jsonSchema.properties.pan

# authority basis (the "why") — plane:cross is derived, not written
cross.consent | has-slot | grantor | basis:authority | asof:dom-a1-1.0.0 | grounded-in:principle.separation-of-concerns

# bare triple — valid, immature
dom.consent.authz | requires | "authorization.token"

# exception: untethered placeholder (must be tagged)
x.authorization | has-slot | "amount" | basis:inferred | asof:dom-a1-1.0.0 | !untethered

# exception: desired (future), never asserted as live
dom.consent.authz | requires | "biometric-auth" | basis:declared | asof:dom-a1-1.1.0 | grounded-in:draft#attributes.auth.biometric | !desired
```

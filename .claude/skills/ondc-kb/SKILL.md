---
name: ondc-kb
description: >-
  Answer questions about an ONDC protocol domain + version from the grounded knowledge
  base in `knowledge/` (FIS10/FIS12/FIS13/FIS14/TRV10/TRV11/TRV12/TRV13/TRV14, 16 books).
  Use when asked what a domain requires, what an action/tag/enum/error means, which flows
  and API sequences exist, who sends what (BAP vs BPP), what changed between two spec
  versions, where a rule is defined in config, or what breaks if a config file changes.
  Also use before writing automation/validation code against an ONDC spec, so the code is
  grounded in the actual release rather than guessed. Read-only: query, cite, never edit.
---

# ONDC KB — read & answer

The KB is 10,781 **atoms** across 16 domain/version **books**. Every atom is a triple with
a `basis` (how strongly it's backed) and usually a `grounded-in` pointer to the exact
config node it came from. Your job: query it, then answer **with the citation**.

The one hard rule: **never state a protocol fact this KB does not contain.** Missing is
missing (closed world) — say "the KB does not record that", don't fill it from general
Beckn/ONDC knowledge. If you do add outside context, label it as such.

## Query with the tool, not with Read

`kb_query.py` sits next to this file. Use it instead of reading `atoms.md` — those files
are 400–1000 lines each and grepping them by hand loses the anchor/index joins.

```bash
KB=<this-skill-dir>/kb_query.py   # e.g. .claude/skills/ondc-kb/kb_query.py

python3 $KB books                              # every book: domain, version, size, entry actions
python3 $KB resolve "FIS12 2.3.0"              # loose name → book id ("ondc:trv11", "fis13 sachet" all work)
python3 $KB overview fis12-2.3.0               # START HERE for a named domain+version
python3 $KB about anchor.xinput --book fis12-2.3.0     # everything the KB says about one meaning
python3 $KB search "cancellation" --book trv11-2.1.0   # free text over anchors + atoms
python3 $KB atoms --book fis12-2.3.0 --relation precedes --limit 100
python3 $KB atoms --book fis12-2.3.0 --subject anchor.confirm --basis declared
python3 $KB anchors fis12-2.3.0 consent        # interned meanings matching a word
python3 $KB flows fis12-2.3.0 [flow-substring] # api-call spine per flow
python3 $KB frames trv11-2.0.1 [name]          # frame nodes (some books only); with a name, prints it
python3 $KB files fis12-2.3.0                  # in-scope config files + where they are on disk
python3 $KB ground "validations/index.yaml#enums.loanCategories"   # config node → units grounded there
python3 $KB blast fis12-2.3.0                  # which config files carry the most KB weight
python3 $KB compare fis12-2.0.3 fis12-2.3.0 [--grep xinput]        # version diff, triple level
python3 $KB shared [anchor.x]                  # cross-book meaning reuse
python3 $KB stats
```

Every list command takes `--limit`; output tells you how many were withheld. `--book` is
optional on `about`/`search`/`atoms` — omit it to sweep all 16 books.

## Procedure

1. **Pin the book first.** A question is only answerable inside one domain+version.
   `resolve` it. If the user gave a domain but no version (`"FIS12"`), the tool returns all
   matches newest-first — say which one you used, and mention the others exist.
   If the user gave nothing, run `books` and ask, unless one book is obvious from context
   (an open file path, a config dir, `asof:` in something they pasted).
2. **Orient with `overview <book>`** — domain, entry actions, flow/step counts, grounding
   coverage, base deviations, and the in-scope config file list.
3. **Answer with `about` / `atoms` / `search`.** `about <anchor>` is the workhorse: it gives
   the meaning, where it was interned, its isa-parents and children, and every atom where it
   appears as subject or object.
4. **Cite.** Quote the atom's `grounded-in` — `fis12-2.3.0:validations/index.yaml#_TESTS_.search[SEARCH_ITEMS]`
   — so the user can open the config at that node. `files <book>` maps the book to
   `configs/release-eks-*/config/`; read the raw YAML there when they want the literal shape.
5. **Respect `basis`** — it is the whole point of the KB. See below.

## Reading `basis` — say how strongly a fact is backed

| basis | what it means for your answer |
|---|---|
| `declared` | the config/spec says so. State it flatly. (~94% of atoms) |
| `authority` | mandated by a doc/ADR/principle — the *why*, not the wire format |
| `observed-live` / `sandbox-tested` | seen in real/sandbox traffic; strong but narrower than declared |
| `derived` | computed from other atoms |
| `ecosystem` | convention, not a spec obligation |
| `inferred` | **model-guessed, unverified — never assert it.** Report as a hypothesis, or drop it |

`!untethered` / `!deprecated` / `!desired` flags: the atom's ground is missing, removed, or
not yet real. `!desired` is a future intent — never present it as current behaviour.

Negated relations (`not-requires`, `not-has-slot`, …) are **positive facts**: `on_select |
not-requires | xinput` means the spec establishes it is not required — that is a real answer,
not an absence.

## Question → command

| the user asks | run |
|---|---|
| "what is FIS12 2.3.0 / give me an overview" | `overview` |
| "what does X mean here / tell me about X" | `about X --book B` (fall back to `search X`) |
| "what must be present in `confirm`" | `atoms --book B --subject anchor.confirm --relation requires` |
| "what's the API sequence for flow F" | `flows B F` |
| "who sends this — BAP or BPP" | `atoms --book B --relation sent-by --grep <thing>` |
| "which tags/enums exist for X" | `anchors B X`, then `about` the interesting ones |
| "what changed from 2.0.3 to 2.3.0" | `compare b1 b2` (add `--grep` to scope it) |
| "where is this rule defined" | `about X` → read its `grounded-in`; `files B` for the path on disk |
| "what's affected if I edit this config file" | `blast <file>`, then `ground <file>#` |
| "is this concept shared across domains" | `shared anchor.x` |
| "what error codes exist" | `atoms --book B --object anchor.error-code` |

## Boundaries

- **Read-only.** Never edit `knowledge/`, `_index/`, or `_work/`. Seeding and regeneration
  belong to the separate `skill/SKILL.md` pipeline — if the user wants the KB rebuilt or a
  book added, point them there rather than hand-editing atoms.
- `knowledge/_work/` and `knowledge/_index/` are **regenerable derivatives**; the config
  books under `configs/` are Ground 0. On a disagreement between them, config wins and the
  KB is stale — say so.
- The KB covers only what `index.yaml` traversal reached. `files <book>` lists that scope;
  anything outside it was never seeded and its absence proves nothing.

## Details when you need them

- `reference/kb-map.md` — what every file and directory in `knowledge/` holds.
- `reference/atom-format.md` — atom line grammar, the relation registry, derived axes.
- Fuller format spec (authored with the seeding pipeline): `skill/kb-format/`.

## Using this from another repo

The tool finds the KB by walking up from its own location, so a symlink works:

```bash
ln -s <this-repo>/.claude/skills/ondc-kb ~/.claude/skills/ondc-kb   # loses auto-discovery
export ONDC_KB_ROOT=<this-repo>                                      # …so set this, or pass --root
```

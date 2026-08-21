#!/usr/bin/env python3
"""
Preflight — prerequisite check + PUSHBACK (KEP skill).
Runs FIRST. Discovers config books generically (no hardcoded book id), checks
mandatory vs optional inputs, and decides: RUN / DEGRADED / STOP — with reasons.
The skill must not proceed past a STOP, and must announce every DEGRADED mode.

Usage: python3 preflight.py <root>     (root = folder that holds the config book(s))
Exit:  0 = can run (possibly degraded) · 2 = STOP (mandatory input missing)
"""
import os, sys, glob, json

VENDOR = ("automation-framework", "node_modules", "/packages/", "api-service",
          "build-output", "generated", "mock-service")   # framework/vendor internals, not release books
def find_books(root):
    """a config book = a dir whose config/ has index.yaml AND the spec-release
    signature (specs/openapi + actions + flows + validations + attributes), and is
    NOT inside a framework/vendor subtree (those bundle sample configs)."""
    sig = ("specs/openapi.yaml", "actions/index.yaml", "flows/index.yaml",
           "validations/index.yaml", "attributes/index.yaml")
    books = []
    for idx in glob.glob(os.path.join(root, "**", "config", "index.yaml"), recursive=True):
        if any(v in idx for v in VENDOR): continue
        cfg = os.path.dirname(idx)
        if all(os.path.exists(os.path.join(cfg, s)) for s in sig):
            books.append(os.path.dirname(cfg))
    return sorted(set(books))

def find_one(root, *needles):
    for n in needles:
        hits = glob.glob(os.path.join(root, "**", n), recursive=True)
        if hits: return hits[0]
    return None

def main():
    import _env
    root = sys.argv[1] if len(sys.argv) > 1 else _env.ROOT
    HERE = os.path.dirname(os.path.abspath(__file__))
    # canonical layout first; fall back to a recursive scan of the given root
    books = _env.discover_books(_env.CONFIGS) or find_books(root)
    workbench = _env.workbench_kb() or find_one(root, "protocol-workbench")
    beckn_base = _env.BECKN_BASE if os.path.exists(_env.BECKN_BASE) else find_one(root, "beckn-base.yaml")
    validator = os.path.join(HERE, "validate_kb.py")   # bundled with the skill

    rows, stop, degraded = [], [], []
    # --- MANDATORY: at least one config book ---
    if books:
        rows.append(("config book(s)", "MANDATORY", f"present: {len(books)}", "RUN"))
    else:
        rows.append(("config book(s)", "MANDATORY", "MISSING", "STOP"))
        stop.append("No config book found (need a dir with config/index.yaml). Cannot produce any KB output.")

    # --- cross-book classifier needs >= 2 books ---
    if len(books) >= 2:
        rows.append(("≥2 books (cross-book classify)", "for C.cls", f"{len(books)} books", "RUN"))
    else:
        rows.append(("≥2 books (cross-book classify)", "for C.cls", f"{len(books)} book", "DEGRADED"))
        degraded.append("Only 1 book → C.cls runs single-book: no cross-book diff; base = this book; classification limited to structural roles.")

    # --- automation-framework (workbench runtime + knowledge): MANDATORY ---
    if workbench:
        rows.append(("automation-framework (workbench)", "MANDATORY", "present", "RUN"))
    else:
        rows.append(("automation-framework (workbench)", "MANDATORY", "MISSING", "STOP"))
        stop.append("No automation-framework/protocol-workbench (runtime env + knowledge). It is mandatory — runtime/protocol understanding cannot be grounded without it.")

    # --- beckn-base: MANDATORY, human-managed authority (skill relies on it, never rewrites it) ---
    if beckn_base:
        rows.append(("common-config/beckn-base.yaml", "MANDATORY (human-owned)", "present", "RUN"))
    else:
        rows.append(("common-config/beckn-base.yaml", "MANDATORY (human-owned)", "MISSING", "STOP"))
        stop.append("No beckn-base.yaml. It is a human-managed authority the skill grounds against — not derived at run time. "
                    "Bootstrap ONCE with build_beckn_base.py, then it is user-owned; the skill will not modify it.")

    # --- validator: bundled with the skill ---
    rows.append(("KB validator", "for F validate", "bundled" if os.path.exists(validator) else "MISSING", "RUN" if os.path.exists(validator) else "STOP"))
    if not os.path.exists(validator): stop.append("Bundled validate_kb.py missing from skill/tools.")

    # ---- report ----
    print("PREFLIGHT — prerequisites\n")
    print(f"  {'input':32} {'need':22} {'status':20} {'decision'}")
    print("  " + "-"*82)
    for name, need, status, dec in rows:
        print(f"  {name:32} {need:22} {status:20} {dec}")
    if books:
        print("\n  discovered books:")
        for b in books: print(f"    - {os.path.basename(b)}")

    verdict = "STOP" if stop else ("DEGRADED" if degraded else "RUN")
    print(f"\nVERDICT: {verdict}")
    for s in stop:     print(f"  ✗ STOP:     {s}")
    for d in degraded: print(f"  ⚠ DEGRADED: {d}")
    if verdict == "RUN": print("  ✓ all prerequisites met.")

    # machine-readable for the orchestrator
    out = {"root": root, "books": [os.path.basename(b) for b in books],
           "workbench": bool(workbench), "beckn_base": bool(beckn_base),
           "validator_bundled": os.path.exists(validator),
           "verdict": verdict, "stop": stop, "degraded": degraded}
    print("\n" + json.dumps(out))
    sys.exit(2 if stop else 0)

if __name__ == "__main__":
    main()

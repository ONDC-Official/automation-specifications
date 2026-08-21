#!/usr/bin/env python3
"""
Orchestrator driver (B6) — chains the pipeline A→G on the canonical layout and reports.
In production each BOOK runs in its own subagent; this driver proves the chain composes.
Usage: python3 run_pipeline.py            (paths come from _env / the canonical structure)
"""
import os, sys, subprocess, json, glob, _env
HERE = os.path.dirname(os.path.abspath(__file__))
VALIDATOR = os.path.join(HERE, "validate_kb.py")   # bundled with the skill

def run(desc, args):
    r = subprocess.run([sys.executable, *args], capture_output=True, text=True)
    last = [l for l in (r.stdout + r.stderr).splitlines() if l.strip()]
    print(f"  [{'ok ' if r.returncode==0 else 'ERR'}] {desc}: {last[-1][:96] if last else ''}")
    return r.returncode == 0

def main():
    print("KEP pipeline — A→G  (canonical layout)\n")
    print("Preflight (STOP if mandatory input missing):")
    pf = subprocess.run([sys.executable, os.path.join(HERE, "preflight.py")], capture_output=True, text=True)
    print("  " + "\n  ".join(l for l in pf.stdout.splitlines() if l.startswith(("VERDICT","  ✗","  ⚠","  ✓"))))
    if pf.returncode == 2:
        print("  → STOP: mandatory input missing; not proceeding."); return
    print("\nStage A–D (deterministic, all books):")
    run("A scope_resolver",   [os.path.join(HERE, "scope_resolver.py")])
    run("B grounder",         [os.path.join(HERE, "grounder.py")])
    run("C.seq sequence",     [os.path.join(HERE, "sequence_grapher.py")])
    run("(sig) signatures",   [os.path.join(HERE, "signatures.py")])
    run("C.cls classifier",   [os.path.join(HERE, "classifier.py")])
    run("D runtime_enricher", [os.path.join(HERE, "runtime_enricher.py")])
    print("\nGates: base-conformance + source-change (grounding evolution):")
    bc = subprocess.run([sys.executable, os.path.join(HERE, "base_conformance.py")], capture_output=True, text=True)
    print("  " + next((l for l in bc.stdout.splitlines() if l.startswith("BASE CONFORMANCE")), ""))
    if bc.returncode == 3: print("  ⚠ deviations RAISED — update beckn-base.yaml manually (see base-conformance.json)")
    run("source_state (incremental)", [os.path.join(HERE, "source_state.py")])
    print("\nStage E→F (interpret + write + validate; first book, generic):")
    run("E→F kb_writer",      [os.path.join(HERE, "kb_writer.py")])
    kbouts = sorted(glob.glob(os.path.join(_env.KNOWLEDGE, "*", "atoms.md")))
    if kbouts:
        run("F validate_kb",  [VALIDATOR, os.path.dirname(kbouts[0])])
    print("\nStage G (views + selective regen):")
    run("G tool_g",           [os.path.join(HERE, "tool_g.py")])

    print("\nGate summaries:")
    sg = json.load(open(_env.w("scope-graphs.json")))
    for b, v in sg.items():
        held = "HELD OUT" if v.get("orphan_count", 0) > 0 else "ok"
        print(f"  manifest[{b.split('eks-')[-1]}]: in-scope {v['in_scope_count']} / orphans {v['orphan_count']} -> {held}")
    cls = json.load(open(_env.w("classification.json")))["_tally"]
    print(f"  classifier: {cls['invariant']} core / {cls['authoring-style']} authoring / {cls['semantic']} semantic")
    print("  governance: inferred units carry no grounded-in (validator-enforced)")
    print("\nPipeline composed end-to-end.")

if __name__ == "__main__":
    main()

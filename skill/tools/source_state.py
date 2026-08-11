#!/usr/bin/env python3
"""
Source-change detector (KEP) — incremental grounding.
Grounding sources (configs / references) evolve: facts get ADDED, MODIFIED, or REMOVED.
This snapshots the content of every in-scope source file and diffs against the last run,
then maps changed files -> the grounded node-paths that must be revisited (via ground-map).
  MODIFIED/REMOVED -> re-seed only the affected units (Tool G selective regen).
  ADDED            -> seed new units.
First run = everything is 'added' (new). Snapshot lives in knowledge/_state/.

Output: knowledge/_work/source-change.json
"""
import os, json, hashlib, _env

SNAP = os.path.join(_env.KNOWLEDGE, "_state", "grounding-snapshot.json")

def sha(path):
    try:
        with open(path, "rb") as f: return hashlib.sha1(f.read()).hexdigest()[:12]
    except Exception: return None

def run():
    scope = json.load(open(_env.w("scope-graphs.json")))
    prior = json.load(open(SNAP)) if os.path.exists(SNAP) else {}
    current, change = {}, {}

    for book_name, sg in scope.items():
        # locate the book dir + hash each in-scope file
        book_dir = next((b for b in _env.discover_books() if os.path.basename(b) == book_name), None)
        if not book_dir: continue
        cfg = os.path.join(book_dir, "config")
        cur = {rel: sha(os.path.join(cfg, rel)) for rel in sg.get("in_scope_files", [])}
        current[book_name] = cur
        old = prior.get(book_name, {})
        added    = [f for f in cur if f not in old]
        removed  = [f for f in old if f not in cur]
        modified = [f for f in cur if f in old and cur[f] != old[f]]

        # (Tool G narrows changed FILES -> affected node-paths via its reverse index.)
        change[book_name] = {
            "added_files": added, "modified_files": modified, "removed_files": removed,
            "unchanged": len([f for f in cur if f in old and cur[f] == old[f]]),
            "action": ("first-seed (all new)" if not old else
                       "re-seed affected + seed new" if (added or modified or removed) else "no change")
        }

    json.dump(change, open(_env.w("source-change.json"), "w"), indent=2)
    os.makedirs(os.path.dirname(SNAP), exist_ok=True)
    json.dump(current, open(SNAP, "w"), indent=2)

    print("SOURCE CHANGE (grounding evolution)\n")
    for book, c in change.items():
        na, nm, nr = len(c["added_files"]), len(c["modified_files"]), len(c["removed_files"])
        print(f"  {book}: +{na} added  ~{nm} modified  -{nr} removed  ={c['unchanged']} unchanged  → {c['action']}")
        for f in c["modified_files"][:4]: print(f"      modified: {f}")
        for f in c["added_files"][:3]:    print(f"      added:    {f}")
    print("\nMODIFIED/REMOVED → Tool G re-seeds only the affected units; ADDED → new units seeded.")

if __name__ == "__main__":
    run()

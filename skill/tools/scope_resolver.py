#!/usr/bin/env python3
"""
Tool A — Scope Resolver (KEP deterministic spine, B1).
Scope of a book = ONLY what config/index.yaml dereferences into.
Emits: in-scope files, orphans (ignored), validation symbol table, flags.
Contract: index.yaml is the sole scope authority; orphans excluded; anchors
preserved as symbols (not inlined); lenient parse of invalid YAML with flags.
"""
import os, re, sys, json, glob
import _env, _yaml

def find_file_refs(node):
    """yield every $ref that points at a FILE (has a path part, not pure #/...)."""
    out = []
    if isinstance(node, dict):
        for k, v in node.items():
            if k == "$ref" and isinstance(v, str):
                path = v.split("#", 1)[0]
                if path:  # file ref (skip internal '#/components/...')
                    out.append(path)
            else:
                out.extend(find_file_refs(v))
    elif isinstance(node, list):
        for v in node:
            out.extend(find_file_refs(v))
    return out

def lenient_load(path):
    """load YAML the way the runtime does; on failure return (None, error) so we flag not crash."""
    return _yaml.load_file(path)

def resolve_scope(book_root):
    cfg = os.path.join(book_root, "config")
    index = os.path.join(cfg, "index.yaml")
    in_scope, flags, visited = set(), [], set()

    def visit(rel):
        """rel = path relative to cfg; follow file $refs recursively."""
        norm = os.path.normpath(rel)
        if norm in visited:
            return
        visited.add(norm)
        full = os.path.join(cfg, norm)
        if os.path.isdir(full):                      # e.g. x-docs -> ./docs
            for f in glob.glob(os.path.join(full, "**", "*"), recursive=True):
                if os.path.isfile(f):
                    in_scope.add(os.path.relpath(f, cfg))
            return
        if not os.path.isfile(full):
            flags.append({"type": "unresolved-ref", "detail": rel})
            return
        in_scope.add(norm)
        if full.endswith((".yaml", ".yml", ".json")):
            doc, err = lenient_load(full)
            if err:
                flags.append({"type": "invalid-yaml", "file": norm, "detail": err})
                return
            base = os.path.dirname(norm)
            for r in find_file_refs(doc):
                visit(os.path.normpath(os.path.join(base, r)) if not r.startswith("/") else r.lstrip("/"))

    in_scope.add("index.yaml")
    idx, err = lenient_load(index)
    if err:
        return {"error": f"index.yaml invalid: {err}"}
    for r in find_file_refs(idx):
        visit(os.path.normpath(r))

    # orphans = all config files not reached from index.yaml
    all_files = {os.path.relpath(f, cfg) for f in glob.glob(os.path.join(cfg, "**", "*"), recursive=True)
                 if os.path.isfile(f)}
    orphans = sorted(all_files - in_scope)

    # validation symbol table (anchors preserved, not inlined) + dup-anchor flag
    symbols, dup = [], []
    vfile = os.path.join(cfg, "validations", "index.yaml")
    if os.path.isfile(vfile):
        raw = open(vfile).read()
        dc, uc = _yaml.anchors(raw, is_text=True)
        dup = sorted([a for a, c in dc.items() if c > 1])
        symbols = sorted(dc)
        if dup:
            # The runtime (js-yaml) accepts redefinition, last-before-use wins, so this
            # is not a parse failure. It IS ambiguity: each use must be confined with
            # scoped-to rather than interned against one arbitrary definition.
            flags.append({"type": "duplicate-anchor", "detail": dup})
        if not _yaml.strict_ok(vfile):
            flags.append({"type": "runtime-only-yaml", "file": "validations/index.yaml",
                          "detail": "parses under js-yaml semantics, not under PyYAML's stricter composer"})

    domain = (idx.get("info", {}) or {}).get("domain")
    version = (idx.get("info", {}) or {}).get("version")
    return {
        "book_root": os.path.basename(book_root),
        "domain": domain, "version": version,
        "in_scope_count": len(in_scope),
        "in_scope_files": sorted(in_scope),
        "orphan_count": len(orphans),
        "orphans_ignored": orphans,
        "symbol_count": len(symbols),
        "symbols_sample": symbols[:12],
        "flags": flags,
    }

if __name__ == "__main__":
    root = sys.argv[1] if len(sys.argv) > 1 else _env.CONFIGS
    books = _env.discover_books(root)
    results = {os.path.basename(b): resolve_scope(b) for b in books}
    out = _env.w("scope-graphs.json")
    os.makedirs(os.path.dirname(out), exist_ok=True)
    json.dump(results, open(out, "w"), indent=2)
    for name, r in results.items():
        if "error" in r:
            print(f"{name}: ERROR {r['error']}"); continue
        print(f"{name}: in-scope={r['in_scope_count']}  orphans={r['orphan_count']}  "
              f"symbols={r['symbol_count']}  flags={[f['type'] for f in r['flags']]}")
        if r["orphans_ignored"]:
            print(f"    orphans: {r['orphans_ignored'][:6]}")

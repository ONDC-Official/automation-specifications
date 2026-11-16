// Exits 0 when every changed file in a branch's diff is covered by an approved entry in
// explained-diffs.yaml, and 1 otherwise.
//
// Usage: node explained.mjs <explained-diffs.yaml> <branch> <branch.diff> <base-dir> <new-dir>

import { readFileSync } from "node:fs";
import { createRequire } from "node:module";
import path from "node:path";

const [explainedPath, branch, diffPath, baseDir, newDir] = process.argv.slice(2);
const require = createRequire(path.join(path.dirname(explainedPath), "..", "package.json"));
const yaml = require("yaml");

const entries = yaml.parse(readFileSync(explainedPath, "utf-8"))?.explained ?? [];
const roots = [baseDir, newDir].map((dir) => path.join(path.resolve(dir), branch) + path.sep);
const changed = changedPaths(readFileSync(diffPath, "utf-8"));

const covered = (file) =>
    entries.some((e) => glob(e.branch ?? "*").test(branch) && glob(e.path ?? "*").test(file));

process.exit(changed.length > 0 && changed.every(covered) ? 0 : 1);

// `diff -r` prints "diff -r -x log.txt <base>/<branch>/<file> <new>/<branch>/<file>" for a
// changed file and "Only in <dir>: <name>" for an added or removed one. Both are reduced to the
// path inside the branch's folder.
function changedPaths(text) {
    const files = new Set();
    for (const line of text.split("\n")) {
        const changedFile = line.match(/^diff -r -x log\.txt (\S+) \S+$/);
        if (changedFile) files.add(relative(changedFile[1]));
        const onlyIn = line.match(/^Only in (.+): (.+)$/);
        if (onlyIn) files.add(relative(path.join(onlyIn[1], onlyIn[2])));
    }
    return [...files];
}

function relative(file) {
    const absolute = path.resolve(file);
    const root = roots.find((r) => absolute.startsWith(r));
    return root ? absolute.slice(root.length) : absolute;
}

function glob(pattern) {
    const escaped = pattern.replace(/[.+^${}()|[\]\\]/g, "\\$&").replace(/\*/g, ".*").replace(/\?/g, ".");
    return new RegExp(`^${escaped}$`);
}

// Prints what automation-db would store for a build.yaml, without a database.
//
// Mirrors automation-db's ProtocolService ingest: yaml.parse → BuildConfig.safeParse →
// ingestBuild(db, parsed.data). The db is a recorder, so the output shows every write
// ingestBuild makes. Dates are replaced with "<date>" and keys are sorted, so two runs
// differ only when the stored documents would differ.
//
// Usage: node capture-ingest.mjs <build.yaml> <tooling-dir>

import { readFileSync } from "node:fs";
import { createRequire } from "node:module";
import path from "node:path";
import { pathToFileURL } from "node:url";

const [buildPath, toolingDir] = process.argv.slice(2);
if (!buildPath || !toolingDir) {
    console.error("usage: node capture-ingest.mjs <build.yaml> <tooling-dir>");
    process.exit(2);
}

const toolingRequire = createRequire(path.join(path.resolve(toolingDir), "package.json"));
const yaml = toolingRequire("yaml");
const buildTools = await import(
    pathToFileURL(toolingRequire.resolve("@ondc/build-tools")).href
);

const writes = [];
const db = {
    collection: (name) => ({
        findOne: async () => null,
        replaceOne: async (filter, doc) => writes.push({ collection: name, op: "replaceOne", filter, doc }),
        bulkWrite: async (ops) => writes.push({ collection: name, op: "bulkWrite", ops }),
        deleteMany: async (filter) => writes.push({ collection: name, op: "deleteMany", filter }),
    }),
};

const parsed = buildTools.BuildConfig.safeParse(yaml.parse(readFileSync(buildPath, "utf-8")));
if (!parsed.success) {
    process.stdout.write(stable({ schemaErrors: parsed.error.issues }));
    process.exit(0);
}
await buildTools.ingestBuild(db, parsed.data);
process.stdout.write(stable({ writes }));

function stable(value) {
    return JSON.stringify(normalise(value), null, 2) + "\n";
}

function normalise(value) {
    if (value instanceof Date) return "<date>";
    if (Array.isArray(value)) return value.map(normalise);
    if (value && typeof value === "object") {
        return Object.fromEntries(
            Object.keys(value)
                .sort()
                .map((key) => [key, normalise(value[key])])
        );
    }
    return value;
}

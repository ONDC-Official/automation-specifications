/**
 * Tool D3 — runtime probe (observation producer).
 *
 * `runtime_decoder.py` READS the base64 step logic; this EXECUTES it against the
 * real `@ondc/automation-mock-runner` engine, so the KB can carry facts with
 * `basis:sandbox-tested` and a genuine observation ref instead of only
 * `basis:declared` read out of source.
 *
 * Why this matters (and its limit): the sandbox is a STUB for payload *values* —
 * "xyz.com", "SHAHEED_STHAL" are fixtures, never protocol truth. What the probe
 * observes that IS real: whether a step's logic executes at all, what its
 * validate()/meetsRequirements() actually return for a given payload, which error
 * code fires, how long it takes, and what the engine itself rejects (CodeValidator
 * AST analysis, blocked globals, timeouts). Those are properties of the shared
 * engine, not of the stub data.
 *
 * Usage:  node runtime_probe.mjs <flow.yaml> [--json out.json]
 * Output: one observation record per step/function executed.
 */
import { createRequire } from "node:module";
import { readFileSync, writeFileSync } from "node:fs";
import path from "node:path";

const require = createRequire(import.meta.url);
const HERE = path.dirname(new URL(import.meta.url).pathname);
const REPO = path.resolve(HERE, "../../../..");
const LIB = path.join(REPO, "automation-framework/packages/automation-mock-runner-lib/dist/index.js");

let MockRunner, createInitialMockConfig;
try {
  const m = require(LIB);
  MockRunner = m.MockRunner || m.default?.MockRunner;
  createInitialMockConfig = m.createInitialMockConfig;
} catch (e) {
  console.error(`FATAL: cannot load mock-runner from ${LIB}\n` +
    `Build it first:  cd automation-framework/packages/automation-mock-runner-lib && npm install && npm run build`);
  console.error(String(e.message || e));
  process.exit(2);
}
if (typeof MockRunner !== "function") { console.error("FATAL: MockRunner export not found"); process.exit(2); }

const args = process.argv.slice(2);
const flowPath = args[0];
const jsonOut = args.includes("--json") ? args[args.indexOf("--json") + 1] : null;
if (!flowPath) { console.error("usage: node runtime_probe.mjs <flow.yaml|flow.json> [--json out.json]"); process.exit(2); }

/* The probe consumes JSON so it never re-implements the runtime's js-yaml anchor
   semantics; `runtime_probe.py` converts the YAML with the repo's shared loader. */
let flow;
const raw = readFileSync(flowPath, "utf8");
try { flow = JSON.parse(raw); }
catch { console.error(`FATAL: ${flowPath} is not JSON. Convert with runtime_probe.py (uses tools/_yaml.py).`); process.exit(2); }

const meta = flow.meta || {};
const steps = Array.isArray(flow.steps) ? flow.steps : [];
const config = {
  meta: {
    domain: meta.domain || flow.domain || "UNKNOWN",
    version: String(meta.version || flow.version || "2.0.0"),
    flowId: meta.flowId || meta.flow_id || path.basename(flowPath, path.extname(flowPath)),
    ...(meta.use_case_id ? { use_case_id: meta.use_case_id } : {}),
  },
  transaction_data: {
    transaction_id: "probe-transaction-0001",
    latest_timestamp: new Date(0).toISOString(),   // fixed: probe output must be reproducible
  },
  steps,
  /* Session fullness: getSessionDataUpToStep(i) reads transaction_history[0..i-1]
     via each prior step's saveData map. With an empty history every step past
     index 0 throws "Transaction history length (0) is less than step index", so
     seed it from each step's own defaultPayload — the closest stand-in for a real
     recorded transaction that needs no live network. */
  transaction_history: steps.map((st) => {
    /* A step carries ONE defaultPayload: for a request step (search) it is the
       request, for a callback step (on_search) it is the response. saveData
       JSONPaths may read either side, so populate both — otherwise extraction
       fails at step 1 with "Failed to extract session data". */
    const p = st.mock?.defaultPayload ?? {};
    return {
      action_id: st.action_id || st.id,
      api: st.api,
      request: p,
      response: p,
      timestamp: new Date(0).toISOString(),
    };
  }),
};

/* `generate` blocks are NOT self-contained: they call helpers (getSubscriberUrl,
   uuidv4, …) that the engine prepends from the config's `helperLib`. A flow YAML
   carries no helperLib (it lives at playground-config level), so without this the
   probe only ever observes "getSubscriberUrl is not defined". Inject the library's
   own default helperLib — the same one createInitialMockConfig ships. */
if (!config.helperLib && typeof createInitialMockConfig === "function") {
  try {
    const seed = createInitialMockConfig(config.meta.domain, config.meta.version, config.meta.flowId);
    if (seed?.helperLib) config.helperLib = seed.helperLib;
  } catch { /* helper injection is best-effort; probe still reports what it can */ }
}

const observations = [];
function record(o) { observations.push(o); }

const runner = (() => {
  try { return new MockRunner(config, true); }   // skipValidation: probe non-conforming configs too
  catch (e) { record({ scope: "config", ok: false, error: String(e.message || e) }); return null; }
})();

if (!runner) {
  emit();
} else {
  const kinds = [
    ["requirements", "runMeetRequirements"],
    ["generate", "runGeneratePayload"],
    ["validate", "runValidatePayload"],
  ];
  const work = [];
  for (const st of steps) {
    const aid = st.action_id || st.id;
    if (!aid) continue;
    for (const [kind, method] of kinds) {
      if (!st.mock || typeof st.mock[kind === "requirements" ? "requirements" : kind] !== "string") continue;
      if (typeof runner[method] !== "function") continue;
      work.push({ aid, api: st.api, kind, method });
    }
  }
  const run = async () => {
    for (const w of work) {
      const t0 = Date.now();
      try {
        const res = w.method === "runValidatePayload"
          ? await runner[w.method](w.aid, {})     // empty payload: observe which rule fires first
          : await runner[w.method](w.aid, {});
        record({
          scope: "step", action_id: w.aid, api: w.api, fn: w.kind, ok: true,
          success: res?.success ?? null,
          result: truncate(res?.result),
          error: errText(res?.error),
          validation: res?.validation ?? null,
          engine_ms: res?.executionTime ?? null,
          wall_ms: Date.now() - t0,
          logs: Array.isArray(res?.logs) ? res.logs.slice(0, 5) : [],
        });
      } catch (e) {
        record({ scope: "step", action_id: w.aid, api: w.api, fn: w.kind, ok: false,
                 error: errText(e), wall_ms: Date.now() - t0 });
      }
    }
    emit();
  };
  run();
}

/* Engine errors are often plain objects ({code,description,...}); String() on those
   yields "[object Object]" and hides the actual failure. Serialize properly. */
function errText(e) {
  if (e == null) return null;
  if (typeof e === "string") return e.slice(0, 300);
  if (e instanceof Error) return String(e.message || e).slice(0, 300);
  try { return JSON.stringify(e).slice(0, 300); } catch { return String(e).slice(0, 300); }
}

function truncate(v) {
  if (v == null) return null;
  const s = typeof v === "string" ? v : JSON.stringify(v);
  return s.length > 600 ? s.slice(0, 600) + "…" : (typeof v === "string" ? v : JSON.parse(s));
}

function emit() {
  const out = { flow: flowPath, flowId: config.meta.flowId, domain: config.meta.domain,
                steps: steps.length, observations };
  if (jsonOut) { writeFileSync(jsonOut, JSON.stringify(out, null, 1)); console.log(`-> ${jsonOut}`); }
  const ok = observations.filter(o => o.ok).length;
  console.log(`flow ${config.meta.flowId}  steps=${steps.length}  executions=${observations.length}  ok=${ok}`);
  for (const o of observations.slice(0, 40)) {
    if (o.scope === "config") { console.log(`  CONFIG REJECTED: ${o.error}`); continue; }
    const v = o.success === null ? "?" : (o.success ? "ok " : "ERR");
    const detail = o.error ? ` err=${o.error.slice(0, 90)}`
      : (o.result && typeof o.result === "object" && o.result.code !== undefined
         ? ` -> code=${o.result.code} valid=${o.result.valid} ${String(o.result.description || "").slice(0, 60)}`
         : "");
    console.log(`  ${v} ${String(o.api || "").padEnd(16)} ${o.fn.padEnd(13)} ${String(o.engine_ms ?? o.wall_ms).padStart(6)}ms${detail}`);
  }
  process.exit(0);
}

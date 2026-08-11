#!/usr/bin/env python3
"""
Canonical directory structure for the ondc-kb-seed skill (single source of truth).
Root layout (provided at skill execution):
  configs/              config books (1+)                         [input, mandatory]
  common-config/        beckn-base.yaml + shared grounding        [input, provided grounding]
  references/           additional grounding material             [input, optional]
  (KB output format is EMBEDDED in the skill: skill/kb-format/ + bundled validate_kb.py — no external KB-storage repo needed)
  automation-framework/ workbench runtime code + knowledge        [input, optional — runtime facts]
  knowledge/            KB OUTPUT (atoms, anchors) + _work/        [output]
  skill/                the skill (SKILL.md, tools/)
"""
import os, re, glob
HERE = os.path.dirname(os.path.abspath(__file__))

def _find_root():
    """The DATA root (where configs/ etc. live) — independent of where the skill is installed.
    Priority: $KEP_ROOT · walk up from cwd to a dir containing configs/ · dev fallback (skill/../..)."""
    if os.environ.get("KEP_ROOT"):
        return os.path.abspath(os.environ["KEP_ROOT"])
    d = os.getcwd()
    for _ in range(8):
        if os.path.isdir(os.path.join(d, "configs")):
            return d
        nd = os.path.dirname(d)
        if nd == d: break
        d = nd
    return os.path.abspath(os.path.join(HERE, "..", ".."))   # dev: skill lives inside the data repo

ROOT = _find_root()

CONFIGS    = os.path.join(ROOT, "configs")
COMMON     = os.path.join(ROOT, "common-config")
REFERENCES = os.path.join(ROOT, "references")
FRAMEWORK  = os.path.join(ROOT, "automation-framework")
KNOWLEDGE  = os.path.join(ROOT, "knowledge")
WORK       = os.path.join(KNOWLEDGE, "_work")        # intermediate stage data (regenerable)
BECKN_BASE = os.path.join(COMMON, "beckn-base.yaml")
os.makedirs(WORK, exist_ok=True)

VENDOR = ("automation-framework", "node_modules", "/packages/", "api-service",
          "mock-service", "build-output", "generated")
_SIG = ("specs/openapi.yaml", "actions/index.yaml", "flows/index.yaml",
        "validations/index.yaml", "attributes/index.yaml")

def discover_books(root=None):
    """a config book = a dir whose config/ has the spec-release signature; vendor excluded."""
    root = root or CONFIGS
    books = []
    for idx in glob.glob(os.path.join(root, "**", "config", "index.yaml"), recursive=True):
        if any(v in idx for v in VENDOR): continue
        cfg = os.path.dirname(idx)
        if all(os.path.exists(os.path.join(cfg, s)) for s in _SIG):
            books.append(os.path.dirname(cfg))
    return sorted(set(books))

def book_id(book_dir):
    return re.sub(r"^automation-specifications-release-eks-", "", os.path.basename(book_dir)).lower()

def workbench_kb():
    hits = glob.glob(os.path.join(FRAMEWORK, "**", "protocol-workbench"), recursive=True)
    return hits[0] if hits else None

def w(name):  # a path in the work dir
    return os.path.join(WORK, name)

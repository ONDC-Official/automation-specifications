#!/usr/bin/env python3
"""
Shared YAML loading for the KEP tools — runtime-faithful, not stricter.

The pipeline must read a config book the way the workbench runtime reads it. The
runtime is Node (`js-yaml@4`, in automation-config-service and
automation-validation-compiler), which lets an anchor name be redefined: an alias
resolves to the most recent definition preceding it. PyYAML's composer is stricter
than the YAML spec here and raises ComposerError on the second definition — which
would hold a whole book out of seeding over a file production parses fine.

Precedent: FIS12-2.3.0 `validations/index.yaml` redefines `ON_ACTION_ITEMS`
(ON_INIT_ITEMS vs ON_STATUS_ITEMS) and `REQUIRED_XINPUT_FIELDS` (keyed on
form.id / form_response.status / form_response.submission_id) deliberately, once
per action scope. `RTA`, `SCHEME_CODE`, `KYC_OFFLINE`, `REQUIRED_ITEM_ID` and
`REQUIRED_PARENT_ITEM_ID` are redefined identically and are pure noise.

`load_file` matches js-yaml: last definition before use wins. It never hides the
redefinition — `redefined_anchors()` reports it so callers flag it, because a
redefined anchor is ambiguous *by construction* and Stage E must confine each use
with `scoped-to` rather than intern one arbitrary definition (TRV11-2.1.0 precedent).
"""
import re
import yaml
from collections import Counter


class RuntimeLoader(yaml.SafeLoader):
    """SafeLoader with js-yaml anchor semantics: redefinition is legal, last wins."""


def _compose_node(self, parent, index):
    # A redefinition only shadows the earlier anchor for aliases that FOLLOW it.
    # Dropping the previous binding right before the new node is composed gives
    # exactly that, because compose runs in document order.
    if not self.check_event(yaml.events.AliasEvent):
        event = self.peek_event()
        anchor = getattr(event, "anchor", None)
        if anchor is not None:
            self.anchors.pop(anchor, None)
    return yaml.composer.Composer.compose_node(self, parent, index)


RuntimeLoader.compose_node = _compose_node

_ANCHOR_DEF = re.compile(r"&([A-Za-z0-9_-]+)")
_ANCHOR_USE = re.compile(r"\*([A-Za-z0-9_-]+)")


def loads(text):
    """Parse YAML text with runtime (js-yaml) anchor semantics."""
    return yaml.load(text, RuntimeLoader)


def load_file(path):
    """(doc, err). err is a one-line message; doc is None only when err is set."""
    try:
        with open(path, encoding="utf-8") as f:
            return yaml.load(f, RuntimeLoader), None
    except Exception as e:
        return None, str(e).splitlines()[0]


def load(path):
    """Parse a file, raising on failure. For callers that want the exception."""
    with open(path, encoding="utf-8") as f:
        return yaml.load(f, RuntimeLoader)


def anchors(path_or_text, is_text=False):
    """(defs Counter, uses Counter) of `&name` / `*name` tokens, textually."""
    raw = path_or_text if is_text else open(path_or_text, encoding="utf-8").read()
    return Counter(_ANCHOR_DEF.findall(raw)), Counter(_ANCHOR_USE.findall(raw))


def redefined_anchors(path_or_text, is_text=False):
    """Anchor names defined more than once — ambiguous, must be scoped not interned."""
    defs, _ = anchors(path_or_text, is_text)
    return sorted(a for a, c in defs.items() if c > 1)


def needs_runtime_semantics(path_or_text, is_text=False):
    """True when the file only parses under js-yaml anchor rules — i.e. it redefines an
    anchor, the one place PyYAML's composer is stricter than the runtime. Textual, so it
    costs a regex rather than a second full parse (the audit walks every book)."""
    return bool(redefined_anchors(path_or_text, is_text))


def strict_ok(path):
    """Does this file also satisfy PyYAML's stricter composer? (reporting only)"""
    return not needs_runtime_semantics(path)

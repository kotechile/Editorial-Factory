#!/usr/bin/env python3
"""The reader fronts, and what each one serves.

Everything the link pipeline needs to answer "which fronts exist", "what URLs does a front
publish", "which fronts serve a category", and "what is the one relative path a target has".
The registry itself is ``context/frontends.json`` (domain + URL shapes); the served categories
are *derived* from a front's own sitemap URL list, not declared, so a front's pull set re-derives
itself when the front changes.

This module is PURE: no network, no site_corpus import, no module-level I/O beyond the JSON read
inside :func:`load`. Every function is a plain function of its arguments (plus the registry file),
so callers can pass URL lists they already fetched instead of causing a second crawl.

Shapes (frozen API — other modules import these names):

    load / domains / frontend_url / spec
    path_of / slug_of / relative_path
    is_candidate_shape
    served_categories / renderers / eligible / stamp
"""

from __future__ import annotations

import json
import pathlib
from urllib.parse import urlsplit

# scripts/frontends.py -> repo root is two levels up.
REPO_ROOT = pathlib.Path(__file__).resolve().parent.parent
DEFAULT_PATH = REPO_ROOT / "context" / "frontends.json"

# Keys every registry row must carry (a falsy value counts as missing).
REQUIRED_KEYS = ("domain", "frontend_url", "article_path", "category_path", "tool_path")

# The placeholder the path templates substitute the slug into.
SLUG_TOKEN = "{slug}"

KINDS = ("article", "category", "tool")

# One-segment paths that are site furniture, never link targets.
RESERVED_SEGMENTS = frozenset({
    "about", "contact", "privacy", "terms", "author",
    "articles", "apps", "showcase", "search", "feed", "insights",
})


class FrontendsError(Exception):
    """An unreadable registry, an unknown front, or an unknown kind."""


# --------------------------------------------------------------------------- registry


def _resolve(path=None) -> pathlib.Path:
    return DEFAULT_PATH if path is None else pathlib.Path(path)


def load(path=None) -> list[dict]:
    """Read the front registry (a JSON list of rows), validating it as it goes.

    Raises :class:`FrontendsError` when the file is missing/unreadable, not valid JSON, not a
    non-empty list, when a row is missing a required key, or when two rows name the same domain.
    """
    target = _resolve(path)
    try:
        raw = target.read_text(encoding="utf-8")
    except FileNotFoundError as exc:
        raise FrontendsError(f"frontends registry not found: {target}") from exc
    except OSError as exc:
        raise FrontendsError(f"frontends registry unreadable: {target}: {exc}") from exc

    try:
        data = json.loads(raw)
    except json.JSONDecodeError as exc:
        raise FrontendsError(f"frontends registry is not valid JSON: {target}: {exc}") from exc

    if not isinstance(data, list):
        raise FrontendsError(f"frontends registry must be a JSON list: {target}")
    if not data:
        raise FrontendsError(f"frontends registry is empty: {target}")

    seen: set[str] = set()
    rows: list[dict] = []
    for index, row in enumerate(data):
        if not isinstance(row, dict):
            raise FrontendsError(f"frontends registry row {index} is not an object: {target}")
        missing = [key for key in REQUIRED_KEYS if not row.get(key)]
        if missing:
            raise FrontendsError(
                f"frontends registry row {index} is missing {sorted(missing)}: {target}")
        domain = str(row["domain"])
        if domain in seen:
            raise FrontendsError(f"duplicate front in frontends registry: {domain}")
        seen.add(domain)
        rows.append(row)
    return rows


def domains(path=None) -> list[str]:
    """The registered front domains, in registry (file) order."""
    return [row["domain"] for row in load(path)]


def _row_for(domain, path=None):
    for row in load(path):
        if row["domain"] == domain:
            return row
    return None


def spec(domain) -> dict:
    """The registry row for ``domain``; :class:`FrontendsError` when it is not registered."""
    row = _row_for(domain)
    if row is None:
        raise FrontendsError(f"unknown front: {domain}")
    return row


def frontend_url(domain) -> str:
    """The origin a front is served from, e.g. ``https://giniloh.com``."""
    return spec(domain)["frontend_url"]


# --------------------------------------------------------------------------- URL shapes


def path_of(url: str) -> str:
    """The path of ``url``, normalised to always carry a leading and a trailing slash.

    ``path_of("https://giniloh.com/wage-floor-sets-robot-payback")`` -> ``"/wage-floor-sets-robot-payback/"``
    Query strings and fragments are dropped; a bare path (``"/foo"``) works the same way as a full URL.
    """
    path = urlsplit((url or "").strip()).path or "/"
    if not path.startswith("/"):
        path = "/" + path
    if not path.endswith("/"):
        path = path + "/"
    return path


def _segments(path: str) -> list[str]:
    """The non-empty path segments of an already-normalised path."""
    return [segment for segment in path.split("/") if segment]


def slug_of(url: str) -> str:
    """The last meaningful path segment of ``url`` (``""`` for the site root)."""
    segments = _segments(path_of(url))
    return segments[-1] if segments else ""


def relative_path(domain, kind, slug) -> str:
    """Expand the front's ``<kind>_path`` template for ``slug``.

    ``kind`` is one of ``article``/``category``/``tool``. Raises :class:`FrontendsError` for an
    unknown domain or an unknown kind.
    """
    if kind not in KINDS:
        raise FrontendsError(f"unknown kind: {kind!r} (expected one of {KINDS})")
    template = spec(domain)[f"{kind}_path"]  # spec() raises on an unknown domain
    path = str(template).replace(SLUG_TOKEN, str(slug))
    if not path.startswith("/"):
        path = "/" + path
    if not path.endswith("/"):
        path = path + "/"
    return path


def _template_matches(template_segments: list[str], path_segments: list[str]) -> bool:
    """True when a path has exactly the template's segment count and fills its ``{slug}`` slot(s)."""
    if len(template_segments) != len(path_segments):
        return False
    for template, segment in zip(template_segments, path_segments):
        if SLUG_TOKEN in template:
            if not segment:
                return False
        elif template != segment:
            return False
    return True


def is_candidate_shape(url, domain) -> bool:
    """True when ``url`` has a shape this front publishes as a page worth linking to.

    The shapes are: a one-segment path that is not reserved (``/slug/``), a category hub
    (``/categories/<slug>/``), and the front's own two-segment ``tool_path`` shape
    (``/calculators/<slug>/`` on giniloh.com, ``/tools/<slug>/`` on wellroost.com/aichieve.net).
    Everything else is False: three-or-more-segment paths (the nested calculator role pages),
    the reserved one-segment furniture, and any other two-segment prefix — which is what makes a
    ``/calculators/<slug>/`` path from the wrong front (and vice versa) not a candidate there.

    An unregistered ``domain`` contributes no tool shape (it does not raise) — a one-segment and a
    category hub are still recognised, every other two-segment prefix is not.
    """
    segments = _segments(path_of(url))
    if len(segments) == 1:
        return segments[0] not in RESERVED_SEGMENTS
    if len(segments) == 2:
        if segments[0] == "categories":
            return True
        row = _row_for(domain)
        if row is None:
            return False
        return _template_matches(_segments(path_of(row["tool_path"])), segments)
    return False


# --------------------------------------------------------------------------- what is served


def _served_for_row(row: dict, urls, pinned=None) -> set[str]:
    """The category slugs a front serves.

    Precedence: the explicit ``pinned`` argument, then the optional ``served_categories`` field on
    the registry row (present = it wins, even when empty), then the slugs of the two-segment
    ``/categories/<slug>/`` URLs the front actually publishes.
    """
    if pinned is not None:
        return {str(slug) for slug in pinned}
    if "served_categories" in row and row["served_categories"] is not None:
        return {str(slug) for slug in row["served_categories"]}
    derived: set[str] = set()
    for url in urls or ():
        segments = _segments(path_of(url))
        if len(segments) == 2 and segments[0] == "categories" and segments[1]:
            derived.add(segments[1])
    return derived


def served_categories(domain, urls, pinned=None) -> set[str]:
    """The category hub slugs ``domain`` serves, derived from its own ``urls`` unless pinned.

    For aichieve.net's real sitemap this is exactly
    ``{"artificial-intelligence-future-of-work", "supply-chain-operations"}``.
    """
    return _served_for_row(spec(domain), urls, pinned)


def renderers(category_slug, *, urls_by_domain, pinned_by_domain=None) -> list[str]:
    """The fronts whose served categories contain ``category_slug``, in registry order.

    ``urls_by_domain`` maps each front domain to the URL list published by that front;
    ``pinned_by_domain`` optionally maps a domain to an explicit served set (which wins).
    Returns ``[]`` when no front serves the category.
    """
    live = urls_by_domain or {}
    pinned = pinned_by_domain or {}
    matches: list[str] = []
    for row in load():
        domain = row["domain"]
        if category_slug in _served_for_row(row, live.get(domain), pinned.get(domain)):
            matches.append(domain)
    return matches


# --------------------------------------------------------------------------- stamping


def eligible(candidate: dict, renderers: list[str]) -> bool:
    """True when a non-empty render set is fully covered by the candidate's ``sites_live``."""
    if not renderers:
        return False
    live = candidate.get("sites_live") or {}
    return set(renderers) <= set(live.keys())


def stamp(candidate: dict, renderers):
    """The one relative path every renderer in the set maps this candidate to, else ``None``.

    ``None`` when the render set is empty, when any renderer has no ``sites_live`` entry for the
    candidate, or when the renderers disagree on the path (giniloh ``/calculators/gpu-compute/``
    vs aichieve ``/tools/gpu-compute/``) — a target whose path differs between fronts is dropped
    rather than stamped wrongly.
    """
    ordered = list(dict.fromkeys(renderers or []))
    if not ordered:
        return None
    live = candidate.get("sites_live") or {}
    shared: str | None = None
    for domain in ordered:
        value = live.get(domain)
        if not value:
            return None
        path = path_of(str(value))
        if shared is None:
            shared = path
        elif path != shared:
            return None
    return shared

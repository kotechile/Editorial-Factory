#!/usr/bin/env python3
"""Brief the SCENE, never the concept — and put the scene in the site's own world.

Owner, 2026-10-24: a wellroost header has to look like it belongs to a home site. "A home battery" is
a category, and a category produces the stock-photo abstraction — a chrome box, a glowing orb, a
handshake. A SITUATION produces a photograph: a wall-mounted battery in a garage, status ring lit, a
coiled cable on the concrete.

So every prompt has to carry the anatomy of a scene:

    one object from the article's mechanism  |  a place in the site's world  |  light direction
    palette  |  lens and depth of field  |  film grain  |  no people, no text, no logos

and none of the quality claims ("futuristic, high-tech, glowing, 8k, cinematic masterpiece") that
make a model depict adjectives instead of things.

`problems()` is the gate; the art director gets the refusals back verbatim (see
scripts/illustration_creator.validate_brief).
"""
from __future__ import annotations

import json
import pathlib
import re

ROOT = pathlib.Path(__file__).resolve().parent.parent
VERTICALS = ROOT / "context" / "verticals.json"

# ─────────────────────────────────────────────────────────────────────────────
# each site's world: where its photographs are taken
# ─────────────────────────────────────────────────────────────────────────────

SITES: dict[str, dict] = {
    "wellroost.com": {
        "label": "a home and the ground immediately around it",
        "places": [
            "garage", "driveway", "kitchen", "attic", "roof", "roofline", "basement", "crawlspace",
            "utility closet", "laundry room", "pantry", "hallway", "entryway", "porch", "patio",
            "backyard", "yard", "garden", "fence", "shed", "wall", "floor", "workbench", "countertop",
            "shelf", "siding", "deck", "window", "stairwell", "mudroom",
        ],
        "palette": [
            "bone white", "off-white", "graphite", "charcoal", "slate grey", "slate gray",
            "deep pine green", "olive", "ochre", "rust", "clay", "sand", "warm oak", "honey",
            "terracotta", "moss", "sage", "cream", "birch", "brick red",
        ],
        "materials": [
            "concrete", "timber", "brick", "stucco", "drywall", "plywood", "galvanised steel",
            "brushed steel", "painted wood", "tile", "asphalt shingle", "copper", "PVC", "stone",
        ],
        # Distinctive nouns from another site's world. A home story does not happen in a data hall
        # or at a container terminal, and a header that shows one tells the reader it is the wrong site.
        "never": [
            "data hall", "server rack", "server room", "container terminal", "container port",
            "intermodal", "gantry crane", "assembly line", "factory floor", "substation",
            "loading dock", "quay", "oil rig", "warehouse aisle", "control room",
        ],
    },
    "giniloh.com": {
        "label": "a household's money, work and paperwork",
        "places": [
            "kitchen table", "home office", "desk", "study", "hallway", "countertop", "workbench",
            "garage", "driveway", "shelf", "filing cabinet", "front door", "stairwell", "wall",
            "floor", "window", "porch", "shed", "workshop",
        ],
        "palette": [
            "bone white", "graphite", "charcoal", "slate grey", "olive", "ochre", "rust", "clay",
            "sand", "warm oak", "cream", "brick red", "navy",
        ],
        "materials": ["concrete", "timber", "paper stock", "brass", "steel", "glass", "leather",
                      "cardboard", "cotton", "painted wood", "stone"],
        "never": [],
    },
    "aichieve.net": {
        "label": "industrial and enterprise infrastructure",
        "places": [
            "data hall", "rack row", "server room", "control room", "plant floor", "machine shop",
            "assembly line", "loading bay", "warehouse aisle", "container terminal", "quay",
            "substation", "yard", "workshop", "lab bench", "desk", "floor", "wall", "gantry",
            "piping run", "cooling loop", "terminal apron",
        ],
        "palette": [
            "graphite", "charcoal", "slate grey", "safety yellow", "cobalt", "weathered orange",
            "oxidised red", "bone white", "steel blue", "deep pine green", "copper", "concrete grey",
        ],
        "materials": [
            "brushed steel", "galvanised steel", "concrete", "copper", "aluminium", "aluminum",
            "cast iron", "polymer", "glass", "cable sheathing", "perforated metal", "asphalt",
        ],
        "never": [],
    },
}

DEFAULT_SITE = "aichieve.net"

# Quality claims. Jorge's example: "futuristic, high-tech, glowing, 8k, cinematic, masterpiece" —
# every word a claim, none of them a thing, so the model has nothing to depict and depicts plastic.
QUALITY_CLAIMS = (
    "8k", "4k", "16k", "masterpiece", "hyperrealistic", "hyper-realistic", "photorealistic",
    "ultra realistic", "ultra-realistic", "award-winning", "award winning", "trending on artstation",
    "futuristic", "high-tech", "hightech", "cutting-edge", "state-of-the-art", "glowing orb",
    "stock photo", "concept of", "abstract representation", "abstract concept", "visual metaphor for",
    "highly detailed", "ultra detailed", "ultra-detailed", "best quality", "sharp focus 8k",
)

# A direction or quality of light, not just the word "light".
_LIGHT_RE = re.compile(
    r"\b(from (?:the )?(?:left|right|above|behind|below)|window light|windowlight|"
    r"side ?lit|back ?lit|top ?lit|raking|low[- ]angle (?:sun|light)|low sun|"
    r"golden hour|blue hour|dusk|dawn|overcast|hard (?:afternoon )?light|"
    r"single (?:soft |hard )?key light|directional light|light fall(?:s|ing)?|"
    r"rim (?:light|highlight)|shadow(?:s)? (?:fall|pool)|light pool)\b", re.I)

_COLOUR_RE = re.compile(
    r"\b(white|black|grey|gray|charcoal|graphite|slate|bone|cream|ivory|beige|sand|tan|ochre|"
    r"amber|rust|copper|brass|orange|red|brick|terracotta|clay|brown|oak|walnut|birch|"
    r"green|olive|moss|sage|pine|teal|blue|cobalt|navy|steel blue|yellow|gold)\b", re.I)

_STOP = {"the", "a", "an", "of", "on", "in", "at", "and", "with", "for", "to", "its", "his", "her",
         "their", "from", "by", "as", "into", "over", "under", "beside", "near", "one", "two"}


def _words(text: str) -> list[str]:
    return [w for w in re.findall(r"[a-z0-9][a-z0-9'\-]*", str(text or "").lower())
            if w not in _STOP and len(w) > 2]


def world_for(site: str | None) -> dict:
    """The world a site's photographs are taken in (falls back to the industry world)."""
    site = (site or "").strip().lower()
    if site in SITES:
        return {**SITES[site], "site": site}
    for key, world in SITES.items():
        if site and (site.endswith(key) or key in site):
            return {**world, "site": key}
    return {**SITES[DEFAULT_SITE], "site": DEFAULT_SITE}


def site_for_vertical(vertical: str | None) -> str:
    """The reader front a vertical publishes to (context/verticals.json `target_domain`)."""
    try:
        data = json.loads(VERTICALS.read_text())
    except (OSError, json.JSONDecodeError):
        return DEFAULT_SITE
    items = data if isinstance(data, list) else data.get("verticals", [])
    for item in items:
        if not isinstance(item, dict):
            continue
        if (item.get("id") or item.get("slug")) == vertical:
            return str(item.get("target_domain") or item.get("site") or DEFAULT_SITE)
    return DEFAULT_SITE


def _has_any(text: str, words) -> str:
    low = str(text or "").lower()
    for word in words:
        if re.search(rf"(?<![a-z]){re.escape(word.lower())}(?![a-z])", low):
            return word
    return ""


def problems(prompt: str, *, site: str | None, subject: str = "") -> list[str]:
    """Why this prompt is a concept rather than a scene — empty when it is a scene."""
    world = world_for(site)
    low = str(prompt or "").lower()
    out: list[str] = []

    claim = _has_any(low, QUALITY_CLAIMS)
    if claim:
        out.append(f"prompt sells a quality ({claim!r}) instead of showing a scene — a quality claim "
                   f"gives the model nothing to depict, which is what produces the plastic look. "
                   f"Name the object, the place, the light and the palette instead")

    foreign = _has_any(low, world.get("never") or [])
    if foreign:
        out.append(f"prompt is set in {foreign!r}, which is not {world['site']}'s world "
                   f"({world['label']}) — the header has to look like it belongs on this site")
    elif not _has_any(low, world["places"]):
        out.append(f"prompt names no place in {world['site']}'s world ({world['label']}) — say WHERE "
                   f"the photograph is taken, one of: {', '.join(world['places'][:10])}…")

    if subject:
        shared = {w for w in set(_words(subject)) & set(_words(prompt)) if len(w) >= 4}
        if not shared:
            out.append(f"prompt does not depict the article's own object ({subject!r}): name that "
                       f"mechanism in the prompt, in the place it actually sits")

    if not _LIGHT_RE.search(prompt or ""):
        out.append("prompt does not say which way the light comes from or what quality it has "
                   "(from the left, window light, low sun, backlit, a single key light)")

    if not (_COLOUR_RE.search(prompt or "") or _has_any(low, world["palette"])):
        out.append(f"prompt names no palette — give it two or three colours from this world "
                   f"({', '.join(world['palette'][:6])}…)")
    return out


def guidance(site: str | None, *, limit: int = 12) -> str:
    """The block the art director reads: this site's world, and the anatomy of a scene brief."""
    world = world_for(site)
    return (f"This article publishes on {world['site']} — {world['label']}. Put the photograph in THAT "
            f"world, not in a generic studio.\n"
            f"  places: {'; '.join(world['places'][:limit])}\n"
            f"  palette: {'; '.join(world['palette'][:limit])}\n"
            f"  materials: {'; '.join(world['materials'][:limit])}\n"
            + (f"  never: {'; '.join(world['never'][:limit])}\n" if world.get("never") else ""))

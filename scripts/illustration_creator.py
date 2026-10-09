#!/usr/bin/env python3
"""Commission an article's featured image: art-direction first, generation second.

The pipeline already derives SEO metadata and a chart from each artifact's own text
(`scripts/article_assets.py`). It had no visual: a news article reached the CMS with an empty
featured image, so every post in the CMS fell back to the same theme placeholder, and no image
metadata (alt text, caption, credit) existed for the destinations that demand it.

This module closes that gap. It reads the artifact IT IS GIVEN — title, thesis, lead, section
headings, the numbers section, the source list — and commissions one 16:9 header image for it:

  1. DIRECTION  A frontier model acts as the desk's art director. It picks a *treatment* for this
                specific story from the catalogue in `STYLES` (macro photograph, cinematic still,
                clay 3D render, technical isometric, modular component assembly, paper collage, …),
                states the verbatim cue in the article that drove the choice, and writes the
                generation prompt, the negative prompt, and the reader-facing metadata (alt text,
                caption, title, credit). It is explicitly forbidden from repeating a treatment used
                in the last few articles, so the desk does not look like one filter over 40 posts.
                It is equally forbidden from illustrating an abstract story with bare geometry: a
                cube, wedge or slab carries nothing a reader can connect back to the article, so
                every prompt must name a physical mechanism (`_MECHANISM_RE`).

  2. GENERATION One image model on kie.ai runs the brief: Flux-2 Pro (`flux-2/pro-text-to-image`)
                for anything photographic or physical, Nano Banana Pro (`nano-banana-pro`) where
                the brief is constructed — a render, a cutaway, a collage, flat geometry. The
                brief names the model; this module refuses an unknown one rather than silently
                substituting.

  3. PROVENANCE The image lands in `context/assets/illustrations/<slug>/featured.<ext>` next to a
                `featured.json` sidecar carrying the full brief, the model's task id, the credits
                spent, and the sha256 of both the bytes and the article text that produced them.
                The sidecar is committed; the binary is not (see .gitignore) — the CMS media
                library is the image's canonical home, the local copy is the upload's source.

Idempotency is by content, not by presence: the sidecar records `source_hash`, a digest of the
artifact's own words. Re-running on an unchanged article is a no-op; a rewritten article gets a
new image (the old generation is kept in the sidecar's `history`), because the visual is a reading
of the text and a new text deserves a new reading.

Every decision is reported and every refusal is explicit (agent rule 6): an unknown style, a prompt
that asks for legible text, an alt text that is a fragment, a repeat of a recent treatment — each
raises with the reason, and the caller decides. Nothing here invents a fallback image.

CLI:
  python3 scripts/illustration_creator.py context/drafts/X_final.md            # report (no spend)
  python3 scripts/illustration_creator.py context/drafts/X_final.md --apply     # direct + generate
  python3 scripts/illustration_creator.py context/drafts/X_final.md --apply --style editorial_macro
  python3 scripts/illustration_creator.py --backfill --limit 3                 # every artifact missing one
  python3 scripts/illustration_creator.py context/drafts/X_final.md --dry-run   # brief only: LLM, no image credits
  python3 scripts/illustration_creator.py --check published/*.md                # exit 1 on drift (no network)
"""

from __future__ import annotations

import argparse
import datetime
import hashlib
import json
import os
import pathlib
import re
import sys
import time
import urllib.error
import urllib.request
from dataclasses import asdict, dataclass, field

ROOT = pathlib.Path(__file__).resolve().parent.parent
ASSET_ROOT = ROOT / "context" / "assets" / "illustrations"
LEDGER = ROOT / "context" / "illustration_log.md"
KIE_BASE = "https://api.kie.ai/api/v1"

# kie.ai model ids. The brief names one of these keys; the id is what the API is called with.
MODELS = {
    "flux": "flux-2/pro-text-to-image",
    "nanobanana": "nano-banana-pro",
}
MODEL_ALIASES = {
    "flux": "flux", "flux-2": "flux", "flux2": "flux", "flux-2-pro": "flux",
    "flux-2/pro-text-to-image": "flux",
    "nanobanana": "nanobanana", "nano-banana-pro": "nanobanana", "nano": "nanobanana",
    "nano-banana": "nanobanana",
}
GEMINI_MODEL = "gemini-3.1-pro-preview"
DIRECTOR_MAX_ATTEMPTS = 3
DEFAULT_ASPECT = "16:9"
FEATURED_ASPECTS = ("16:9", "3:2")     # a featured image is landscape; a square header crops badly
FEATURE_RESOLUTIONS = ("1K", "2K")
# A treatment may not repeat within the last N illustrations. Deliberately 4 and not 2: at this
# catalogue size four withheld treatments can never empty the desk (ten treatments, at most four
# blocked, six always left), while narrowing the window to 2 would let a treatment come back after
# two articles instead of four — which is the sameness this desk exists to prevent, not a fix for
# it. The genuine corner is a *family* (the catalogue's two models), and `allowed_styles` guards
# that one directly.
HISTORY_WINDOW = 4

# A retired treatment id and the one that replaced it. Left here rather than deleted because the
# desk's ledger, the published frontmatter and the operator's runbooks all carry the old id, and a
# rotation window that silently stopped seeing those rows would let the replacement repeat.
RETIRED_STYLES = {"minimal_geometry": "component_assembly"}

# The negative half of every brief. In-image text is the single most common way an otherwise good
# generated header is unusable, so the brief has to forbid it explicitly and this module checks that
# it did (see `validate_brief`).
DEFAULT_NEGATIVE = (
    "text, letters, numbers, words, captions, subtitles, typography, wordmarks, watermarks, logos, "
    "brand marks, signatures, UI elements, charts, borders, frames, split panels, duplicated "
    "subjects, deformed anatomy, extra fingers, low resolution, blur, jpeg artifacts"
)
_NO_TEXT_RE = re.compile(r"\b(text|letter|word|caption|typograph|watermark|logo|brand mark|signature)", re.I)

# What is actually appended to the image model's prompt. Deliberately NOT the director's
# `negative_prompt`: kie takes the prompt as ONE text field, so every prohibition is read back as a
# token to draw — a brief that forbids "abstract cubes, spheres, wedges" is a brief that asked for
# them, which is how kv-cache-is-the-concurrency-ceiling came back as a cube-and-block assembly. Only
# the legibility/brand set earns that risk, because in-image text ruins a header outright. The
# director's own negative stays on the brief as provenance and is still checked by validate_brief.
IMAGE_GUARD = "Do not include: text, lettering, numbers, logos, watermarks, UI."

# Potency vocabulary — what a brief must NAME to be worth an image credit. A floor, not a style test:
# a prompt that names neither an optic nor a light is a description, not a photograph, and that is
# how a "cinematic" brief comes back a flat render. The two model families need different anchors
# (flux: stage the photograph; nano: build the structure), so the check is per model_key.
_OPTIC_RE = re.compile(
    r"\b(lens|\d{2,3}\s?mm|anamorphic|macro|telephoto|wide[- ]angle|fisheye|focal|depth of field|"
    r"shallow focus|long[- ]lens)\b", re.I)
_LIGHT_RE = re.compile(
    r"\b(light|lights|lighting|lit|illuminat\w+|chiaroscuro|rim[- ]?light\w*|rim highlight\w*|"
    r"spotlight|backlit|sunlight|daylight|golden hour|blue hour|dusk|twilight|glow|shadow\w*|"
    r"silhouette\w*|haze|hazy|volumetric)\b", re.I)
_TEXTURE_RE = re.compile(
    r"\b(textur\w+|weathered|brushed|polished|oxidiz\w+|oxidiz\w+|rust\w*|patina|concrete|steel|"
    r"copper|aluminium|aluminum|timber|wooden|canvas|rag paper|paper stock|polymer|matte|grain\w*|"
    r"tactile|surfaces?|dusty|grimy)\b", re.I)
_STRUCTURE_RE = re.compile(
    r"\b(assembl\w+|cutaway|isometric|arrang\w+|tier\w*|stack\w*|modul\w+|bay|bays|rack\w*|rails?|"
    r"layers?|layered|interlock\w*|mounted|chassis|sectioned|framed|jig|bracket\w*|housing\w*)\b", re.I)
_FRAMING_RE = re.compile(
    r"\b(asymmetr\w*|symmetr\w*|off[- ]centre\w*|off[- ]center\w*|centred|centered|"
    r"left[- ]aligned|right[- ]aligned|left third|right third|rule of thirds|thirds|"
    r"low[- ]angle|high[- ]angle|top[- ]down|three[- ]quarter|scale contrast|leading lines?|"
    r"vanishing point|diagonal|foreground|midground|receding|stacked|"
    r"wide establishing|extreme close|close crop|hero subject)\b", re.I)
# Phrases that ask the model to render legible text (as opposed to forbidding it).
_TEXT_REQUEST_RE = re.compile(
    r"\b(with|featuring|showing|displaying|reading|saying|spelling|stating|labelled|labeled|titled|"
    r"inscribed|stamped|printed|bearing|that (?:reads?|says))\b[^.]{0,40}?"
    r"\b(text|words?|letters?|numbers?|labels?|signage|signs?|placard|billboard|marquee|poster|"
    r"titles?|headlines?|typography)\b", re.I)
_CLICHE_RE = re.compile(
    r"\b(light ?bulb|handshake|chess piece|chessboard|puzzle piece|glowing brain|trophy|dartboard|"
    r"rocket ship|rocket launch|target with an arrow|arrow(s)? pointing up|gears? of|"
    r"scales of justice|gavel|thumbs up|magnifying glass over|robot handshake|"
    r"rocking horse|toy horse|toy block|doll|teddy bear|paper cutout|paper cut-out|clipart)\b", re.I)
# ── domain grounding: a shape is not a subject ────────────────────────────────────────────────
# The failure this pins, from the desk's own ledger: two agentic-AI articles were illustrated with
# "a rectangle with a colour band" and "a block resting on a wedge" — headers a reader cannot
# connect to the piece, and the director's own rationale for one of them said it was "avoiding
# literal depictions of abstract concepts". The cause is not the model; it is a prompt that names
# bare geometry as the SUBJECT. This desk therefore allows shape-talk in a prompt only when the
# prompt also names the mechanism the shape belongs to. `_PRIMITIVE_RE` finds the shape,
# `_MECHANISM_RE` proves something physical is in the frame; a prompt with the first and not the
# second is refused and answered again (the refusal names the mechanism vocabulary to reach for).
_PRIMITIVE_RE = re.compile(
    r"\b(cubes?|spheres?|orbs?|balls?|wedges?|triangles?|prisms?|cones?|cylinders?|rectangles?|"
    r"polygons?|tori|torus|discs?|disks?|blobs?|slabs?|bars?|rods?|cuboids?|hexagons?|pyramids?|"
    r"blocks?|geometric\s+(?:shapes?|forms?|volumes?|solids?|bodies)|"
    r"abstract\s+(?:shapes?|forms?|volumes?)|"
    r"(?:simple|simplified|plain|basic|primitive|bare|unformed|amorphous)\s+(?:shapes?|forms?|volumes?|scraps?|strips?)|"
    r"(?:torn|cut)\s+(?:paper\s+)?(?:scraps?|shreds?|strips?))\b", re.I)
# A recognisable physical engineering part. Deliberately broad: the rule is a floor that stops
# "a grey cube" from being a commission, not a vocabulary exam — the director's mandate does the
# finer work of picking the RIGHT mechanism for the story.
_MECHANISM_RE = re.compile(
    r"\b(modular|modules?|components?|sub-?assembl(?:y|ies)|assembl(?:y|ies|ed)|chassis|housings?|"
    r"casings?|enclosures?|racks?|blades?|bays?|trays?|docks?|connectors?|couplings?|latch(?:es)?|"
    r"hinges?|brackets?|fasteners?|bolts?|screws?|relays?|contactors?|switch(?:es)?|switchgear|"
    r"solenoids?|servos?|actuators?|linkages?|bearings?|valves?|pumps?|pipes?|piping|manifolds?|"
    r"conduits?|harness(?:es)?|circuits?|busbars?|panels?|workstations?|terminals?|keyboards?|"
    r"consoles?|inspection|checkpoints?|gates?|end[- ]effectors?|gearbox(?:es)?|turbines?|rotors?|"
    r"stators?|conveyors?|gantr(?:y|ies)|cranes?|rails?|truss(?:es)?|girders?|scaffolding|"
    r"pallets?|crates?|drums?|tanks?|machined|milled|stamped|bolted|riveted|welded|"
    r"certificate|certificates|ledger|ledgers|hourglass|hourglasses|envelope|envelopes|"
    r"safe|safes|vault|vaults|padlock|padlocks|dial|dials|gauge|gauges|meter|meters|caliper|calipers|"
    r"balance\s+scale|weighing\s+scale|token|tokens|chit|chits|document|documents|"
    r"document|documents|filing|filings|contract|contracts|folio|folios)\b", re.I)
_NON_ENGLISH_RE = re.compile(r"[\u0400-\u04FF\u4E00-\u9FFF\u0600-\u06FF\u3040-\u30FF\uAC00-\uD7AF]")
_ALT_PREFIX_RE = re.compile(r"^\s*(an?\s+)?(image|picture|photo|photograph|illustration|graphic|render)\s+(of|showing)\b", re.I)
# The same "medium of/showing" opening, reached through one or two adjectives ("a matte clay 3D
# render showing…"): a screen reader gains nothing from the medium, so the description should start
# with the subject. Scoped to the opening of the string so a legitimate mid-sentence use is fine.
_ALT_MEDIUM_RE = re.compile(r"^.{0,45}?\b(image|picture|photo|photograph|illustration|graphic|render)\b"
                            r"\s+(of|showing|depicting)\b", re.I | re.S)


# ─────────────────────────────────────────────────────────────────────────────
# the treatment catalogue — the desk's "pro skills", written down
# ─────────────────────────────────────────────────────────────────────────────

@dataclass(frozen=True)
class Style:
    """One treatment the desk can commission.

    `when` is what the art director reads to decide; `medium`/`craft` are the photographic or
    rendering instructions that make the treatment itself (rather than a topic) recognisable in the
    prompt; `keywords` is the vocabulary a prompt in this treatment must contain at least one word
    from — the check that the brief really is in the treatment it claims (a "macro" brief that
    never says macro, close-up or depth of field is a different picture wearing the label).
    """
    id: str
    label: str
    when: str
    medium: str
    craft: str
    keywords: tuple
    model: str
    resolutions: tuple = ("1K", "2K")


STYLES: dict[str, Style] = {s.id: s for s in [
    Style(
        id="editorial_macro", label="Editorial macro",
        when="the story turns on one physical thing — a part, a material, a component, a document — "
             "and what that thing costs, contains or crosses a border is the news",
        medium="extreme close-up macro photograph, 100mm macro lens, one razor-sharp focal plane",
        craft="shallow depth of field, visible surface texture and dust, soft directional daylight, "
              "hero object off-centre on the thirds with the background falling away",
        keywords=("macro", "close-up", "close up", "depth of field", "extreme close"),
        model="flux"),
    Style(
        id="cinematic_still", label="Cinematic still",
        when="the article describes one decisive moment or place — a yard at dawn, a control room, "
             "a shutdown line, a handover — that a film still could hold",
        medium="cinematic film still, anamorphic 35mm look, wide establishing composition",
        craft="single strong practical light source, crisp atmospheric depth, restrained teal-and-amber "
              "palette, no people facing camera, motion implied rather than shown",
        keywords=("cinematic", "film still", "anamorphic", "35mm", "establishing"),
        model="flux"),
    Style(
        id="document_flatlay", label="Document still life",
        when="the story is regulatory or contractual — a filing, a mandate, a rate notice, a "
             "certificate, a purchase order that changed the economics",
        medium="overhead flat-lay photograph of paper documents on a plain desk surface",
        craft="top-down 90-degree view, even diffused daylight, one object slightly out of "
              "alignment to look handled, blank or illegibly cropped paper, muted paper tones",
        keywords=("flat lay", "flat-lay", "overhead", "top-down", "top down", "desk"),
        model="flux"),
    Style(
        id="clay_render", label="Matte 3D render",
        when="the news is structural and abstract — a stack reordered, a layer added, a flow "
             "rerouted — and there is no literal object that carries it, so the idea is stated as a "
             "small physical assembly of recognisable parts rather than as bare shapes",
        medium="matte clay 3D render of a small mechanical assembly resting on a real textured "
               "surface in a real space",
        craft="three or four recognisable engineered parts — a modular block, a housing, a latched "
              "cover, a connector or a bay — in a clear physical arrangement that states the idea; "
              "matte surfaces with moulding seams and contact shadows resting on weathered concrete "
              "or brushed steel, one directional key light raking across them, matte muted palette, "
              "no plain spheres or wedges standing in for the subject, no text and no moulded or "
              "embossed lettering",
        keywords=("3d render", "clay", "matte", "studio render", "component", "modular", "assembly",
                  "housing", "bay", "3d"),
        model="nanobanana"),
    Style(
        id="technical_isometric", label="Technical isometric cutaway",
        when="the article explains how a system, process or stack actually works — money flows, "
             "supply chains, pipelines, an agent assembly line",
        medium="clean isometric cutaway illustration, technical drawing style, axonometric projection",
        craft="flat muted palette with one accent colour, thin consistent line weight, laid over a "
              "real material surface — a workbench, a plant floor, a drafting table — recognisable "
              "hardware with racks, modules, trays, connectors, pipes with visible depth rather "
              "than abstract boxes, one directional light, unlabelled, generous empty margin",
        keywords=("isometric", "axonometric", "cutaway", "cut-away", "cross-section", "schematic"),
        model="nanobanana"),
    Style(
        id="component_assembly", label="Modular component assembly",
        when="the story is a single number, rule, gate or shift and restraint is the point — with "
             "no scene to photograph, the frame must still be a real assembly: a modular bay, an "
             "unlatched inspection gate, a rack of blades, an interlocking connector",
        medium="minimalist studio composition of a modular mechanical assembly on a real surface, "
               "one directional light, generous negative space",
        craft="two or three recognisable engineered parts (a module, a latch, a rack rail, a bay "
              "cover, an inspection gate) in one deliberate arrangement that states the idea; hard "
              "clean edges on weathered concrete or brushed steel, one directional light throwing a "
              "long cast shadow, matte muted palette, never bare shapes — a cube, a sphere or a "
              "wedge is not a subject — and no moulded, engraved or printed lettering",
        keywords=("modular", "module", "component", "assembly", "connector", "rack", "chassis",
                  "bay", "bracket", "latch"),
        model="nanobanana"),
    Style(
        id="paper_collage", label="Editorial paper collage",
        when="the article is a purely conceptual synthesis or policy dilemma where no physical facility, machine, or supply chain exists, and an elegant abstract paper silhouette states the idea. Never reach for paper collage when the story describes physical manufacturing, freight, energy, hardware, or heavy infrastructure — use cinematic still or telephoto industry instead",
        medium="minimalist editorial cut-paper collage, crisp cut-out object silhouettes, halftone newsprint texture",
        craft="two or three stylized cut-paper object silhouettes (such as an hourglass, certificate, key, or mechanism) "
              "layered deliberately on a real table — hand-torn rag paper with visible fibre, physical cast shadows "
              "under each layer, one raking light; muted modern editorial palette, crisp clean edges, "
              "generous negative space, never bare geometry or random torn scraps, no legible print",
        keywords=("collage", "cut-paper", "cut paper", "silhouette", "cut-out", "cutout", "torn", "halftone", "newsprint"),
        model="nanobanana"),
    Style(
        id="long_lens_industry", label="Compressed telephoto industry",
        when="scale is the story — a port, a refinery, a data centre hall, a rail yard, a skyline of "
             "cranes — and the reader needs to feel how big it is",
        medium="telephoto compression, 200mm long-lens view of industrial infrastructure",
        craft="stacked overlapping layers of structure with crystal-clear telephoto distance clarity, flat compressed "
              "perspective, sharp directional lighting and deep industrial contrast, no people in the foreground, no fog or haze",
        keywords=("telephoto", "long lens", "long-lens", "compressed", "200mm"),
        model="flux"),
    Style(
        id="studio_object", label="Studio product shot",
        when="the story is a product, a device, a price or a market for a thing the reader could buy "
             "— an appliance, a panel, a router, a robot arm",
        medium="studio product photograph of one hero object on a real studio surface, single "
               "directional light",
        craft="softbox key light with visible falloff and a long cast contact shadow across a "
              "textured surface, three-quarter angle, generic unbranded object, catalogue clarity, "
              "no gradient sweep and no embossed or printed lettering",
        keywords=("studio", "studio surface", "product shot", "softbox", "three-quarter"),
        model="flux"),
    Style(
        id="architectural_night", label="Lit architecture at dusk",
        when="the story is about change after hours — automation displacing shifts, a market open "
             "all night, capacity running while people sleep",
        medium="architectural photograph of a modern building or plant at blue hour",
        craft="lit windows as the only warm light, long-exposure calm with no moving figures, deep "
              "blue ambient light, clean geometry, small human scale implied by a doorway",
        keywords=("blue hour", "dusk", "night", "lit windows", "long exposure", "architectural"),
        model="flux"),
]}

CLICHE_BAN = ("light bulb", "handshake", "chess", "puzzle piece", "glowing brain", "rocket",
              "dartboard", "scales of justice", "gavel", "thumbs up")


class IllustrationError(RuntimeError):
    """Anything that must surface instead of degrading into a placeholder image (agent rule 6)."""


class BriefError(IllustrationError):
    """The art director returned a brief this desk will not commission as written."""


class GenerationError(IllustrationError):
    """kie.ai refused, failed, or never finished the task."""


# ─────────────────────────────────────────────────────────────────────────────
# artifact reading (frontmatter + the parts of the text the image is a reading of)
# ─────────────────────────────────────────────────────────────────────────────

def split_frontmatter(md: str) -> tuple[dict[str, str], str]:
    """The artifact's frontmatter as raw strings, plus the body. Mirrors publish.py's parser."""
    fm: dict[str, str] = {}
    body = md
    if md.startswith("---"):
        parts = md.split("---", 2)
        if len(parts) >= 3:
            body = parts[2].lstrip("\n")
            for line in parts[1].strip().splitlines():
                if ":" in line and not line.lstrip().startswith("-"):
                    key, value = line.split(":", 1)
                    fm[key.strip()] = value.strip().strip('"').strip("'")
    return fm, body


def _section(body: str, marker: str) -> str:
    """The text between one `<!-- marker -->` and the next section marker or heading."""
    match = re.search(rf"<!--\s*{marker}\s*-->\s*(.*?)(?=\n<!--|\n##\s|\Z)", body, re.S | re.I)
    return (match.group(1) if match else "").strip()


def article_excerpt(md: str) -> str:
    """The article's excerpt or summary (meta_description, lead section, or first real paragraph)."""
    fm, body = split_frontmatter(md)
    if (fm.get("meta_description") or "").strip():
        return fm["meta_description"].strip()
    lead = _section(body, "lead")
    if lead:
        lead = re.sub(r"\[\d+\]", "", lead)
        return re.sub(r"\s+", " ", lead).strip()
    for block in re.sub(r"^---.*?---", "", body, flags=re.S).split("\n"):
        text = block.strip()
        if not text or text.startswith(("#", "|", ">", "-", "*", "```", "<!--")):
            continue
        text = re.sub(r"\[([^\]]+)\]\([^)\s]+\)", r"\1", text)
        text = re.sub(r"\[\d+\]", "", text)
        text = re.sub(r"<[^>]+>", " ", text)
        text = re.sub(r"[*`_]", "", text)
        text = re.sub(r"\s+", " ", text).strip()
        if len(text.split()) >= 6:
            return text
    return (fm.get("one_big_thing") or "").strip()


def article_core_text(md: str) -> str:
    """The article's own words that a visual reading may draw on — and the idempotency digest's input.

    Deliberately excludes the `## Sources` list URLs and the LinkedIn variant: re-formatting the
    footer must not force a new image, while a re-written lead or a new thesis must.
    """
    fm, body = split_frontmatter(md)
    body = re.split(r"<!--\s*linkedin\s*-->", body, flags=re.I)[0]
    body = re.split(r"^##\s*Sources", body, flags=re.M | re.I)[0]
    parts = [fm.get("title", ""), fm.get("one_big_thing", ""),
             _section(body, "lead"), _section(body, "tension"),
             _section(body, "tactical-insight"), _section(body, "nuanced-takeaway"),
             _section(body, "tldr")]
    text = "\n".join(p for p in parts if p)
    text = re.sub(r"\[\d+\]", "", text)
    return re.sub(r"\s+", " ", text).strip()


def source_hash(md: str) -> str:
    return "sha256:" + hashlib.sha256(article_core_text(md).encode("utf-8")).hexdigest()[:32]


def source_names(md: str) -> list[str]:
    """Publication names from the artifact's own `## Sources` list — what the image must NOT depict."""
    names = []
    for line in re.findall(r"^\[(\d+)\]\s*(.+)$", md, re.M):
        first = re.split(r"[—\-,]", line[1])[0].strip().strip('"')
        if first and len(first) < 60:
            names.append(first)
    return names[:6]


def _numbers(md: str) -> list[str]:
    """The `**By the numbers:**` bullets, which often carry the most depictable object in the piece."""
    fm, body = split_frontmatter(md)
    block = re.search(r"(?:##\s*By the numbers:?|\*\*By the numbers:\*\*)\s*(.*?)(?=\n\s*\n|\n##|\Z)", body, re.S | re.I)
    if not block:
        return []
    return [re.sub(r"\s+", " ", b.strip())[:160] for b in re.findall(r"^\s*[-*]\s+(.*)$", block.group(1), re.M)][:5]


# ─────────────────────────────────────────────────────────────────────────────
# the brief
# ─────────────────────────────────────────────────────────────────────────────

@dataclass
class Brief:
    """One commissioned header image, as the art director wrote it."""
    style_id: str
    rationale: str
    cue: str                  # verbatim phrase from the article that drove the choice
    subject: str
    composition: str          # the mandated framing rule (asymmetry, low-angle, scale contrast)
    model: str                # "flux" | "nanobanana"
    prompt: str
    negative_prompt: str
    aspect_ratio: str
    resolution: str
    alt_text: str
    caption: str
    title: str
    credit: str
    depicts_real_brand: bool
    main_idea: str = ""
    object_or_scene: str = ""
    core_thesis: str = ""
    core_conflict: str = ""
    director: str = GEMINI_MODEL
    attempts: int = 1
    pinned: dict = field(default_factory=dict)
    model_note: str = ""

    @property
    def style(self) -> Style:
        return STYLES[self.style_id]

    @property
    def model_id(self) -> str:
        return MODELS[self.model]

    def to_dict(self) -> dict:
        return asdict(self)


def canonical_style_id(value: str) -> str:
    """A retired treatment id mapped onto the one that replaced it.

    Old ledger rows, old frontmatter and old runbooks all say `minimal_geometry`; without this the
    rotation window would stop seeing those illustrations and the replacement could be chosen again
    immediately.
    """
    return RETIRED_STYLES.get(str(value or "").strip(), str(value or "").strip())


def _alias_model(value: str) -> str:
    key = MODEL_ALIASES.get(str(value or "").strip().lower())
    if not key:
        raise BriefError(
            f"unknown model {value!r} — this desk generates with {' or '.join(sorted(MODELS))} "
            f"({', '.join(sorted(MODELS.values()))}). Refusing to guess a substitute.")
    return key


def validate_brief(raw: dict, article_md: str, *, allowed: tuple, pinned_style: str | None = None,
                   pinned_model: str | None = None) -> Brief:
    """Turn the director's JSON into a Brief, refusing anything this desk will not commission.

    Every rule here exists because of a specific way a generated header fails in production:
    a treatment that is a repeat (the desk looks templated), a prompt that asks for legible text
    (diffusion models render text as rubble), a brief whose style label does not match its own
    prompt words (a "macro" that is really a wide shot), an alt text that is a fragment or starts
    "image of" (screen readers read it aloud), or an object that is a real company's product.
    """
    problems: list[str] = []
    if not isinstance(raw, dict):
        raise BriefError(f"the brief must be a JSON object, got {type(raw).__name__}")

    style_id = str(raw.get("style_id") or "").strip()
    if style_id in RETIRED_STYLES:
        raise BriefError(
            f"treatment {style_id!r} was retired — it is {RETIRED_STYLES[style_id]!r} "
            f"({STYLES[RETIRED_STYLES[style_id]].label}) now: the desk no longer commissions a frame "
            f"built from bare shapes. Allowed now: {', '.join(allowed)}")
    if style_id not in STYLES:
        raise BriefError(f"unknown treatment {style_id!r} — allowed now: {', '.join(allowed)}")
    if style_id not in allowed:
        raise BriefError(
            f"treatment {style_id!r} was used in one of the last {HISTORY_WINDOW} illustrations — "
            f"the desk does not repeat a treatment back-to-back. Allowed now: {', '.join(allowed)}")
    if pinned_style and style_id != pinned_style:
        raise BriefError(f"the operator pinned treatment {pinned_style!r}, the brief says {style_id!r}")

    style = STYLES[style_id]
    model = _alias_model(pinned_model or str(raw.get("model") or ""))
    model_note = ""
    if model != style.model:
        model_note = str(raw.get("model_override_reason") or "").strip()
        if len(model_note) < 20:
            raise BriefError(
                f"the brief generates {style_id} with {model} instead of the catalogue's "
                f"{style.model} — state a model_override_reason (>=20 chars) or use the catalogue "
                f"model; a silent substitution is how a 'photograph' brief lands on an illustration model")
    if pinned_model and model != pinned_model:
        problems.append(f"model pinned to {pinned_model}")

    prompt = re.sub(r"\s+", " ", str(raw.get("prompt") or "")).strip()
    if not 15 <= len(prompt.split()) <= 120:
        problems.append(f"prompt is {len(prompt.split())} words — the desk writes 15-120")
    if _NON_ENGLISH_RE.search(prompt):
        problems.append("prompt contains non-Latin script — kie.ai's image models take English prompts")
    if _TEXT_REQUEST_RE.search(prompt):
        problems.append("prompt asks for legible text/numbers — generated lettering is unreadable rubble; "
                        "depict the mechanism instead")
    cliche = _CLICHE_RE.search(prompt)
    if cliche:
        problems.append(f"prompt reaches for the stock-photo cliché {cliche.group(0)!r} — depict a "
                        f"concrete noun from this story instead")
    if not any(k in prompt.lower() for k in style.keywords):
        problems.append(f"prompt carries no {style_id} vocabulary "
                        f"(one of: {', '.join(style.keywords)}) — it is not the treatment it claims")
    # Domain grounding (see _MECHANISM_RE): a geometric shape is a way of drawing an idea, never
    # the idea itself. The prompt may mention one only alongside a recognisable mechanism.
    shape = _PRIMITIVE_RE.search(prompt)
    if shape and not _MECHANISM_RE.search(prompt):
        problems.append(
            f"prompt's subject is bare geometry ({shape.group(0)!r}) and the frame names no "
            f"mechanism — a cube, sphere or wedge carries nothing a reader can connect to this "
            f"article. Name the physical thing it stands for: a modular bay, an unlatched "
            f"inspection gate, a rack of blades, a relay, a linkage, an interlocking connector")

    # Potency, per model family. The failure: a brief that names a treatment but no optic, no light
    # and no material comes back a flat render on a sweep — it described the idea instead of staging
    # the photograph. Every class is required; an `any()` over the list passes on one word such as
    # "shadow". The anchors differ because the models do: flux stages a photograph, nano builds a
    # structure.
    if model == "flux":
        missing = [label for label, pattern in (
            ("an optic", _OPTIC_RE), ("light", _LIGHT_RE), ("material texture", _TEXTURE_RE),
            ("a framing rule", _FRAMING_RE)) if not pattern.search(prompt)]
        remedy = ("name the optic (35mm anamorphic, 100mm macro, 200mm telephoto), the light it "
                  "sits in, the material, and the framing rule (asymmetric, off-centre, low-angle)")
    else:
        missing = [label for label, pattern in (
            ("a structural arrangement", _STRUCTURE_RE), ("light", _LIGHT_RE),
            ("material texture", _TEXTURE_RE), ("a framing rule", _FRAMING_RE))
            if not pattern.search(prompt)]
        remedy = ("state how the parts are arranged (a modular bay, a tiered stack, an isometric "
                  "cutaway), the light and material, and the framing rule (asymmetric, off-centre, "
                  "low-angle, stacked, symmetrical top-down)")
    if missing:
        problems.append(
            f"prompt names no {', no '.join(missing)} — {model} reads the prompt literally, so "
            f"{remedy}")

    # The layout is mandated, not left to the model: a composition that states no anchoring rule is
    # how two different articles end up with the same centred object on the same sweep.
    composition = re.sub(r"\s+", " ", str(raw.get("composition") or "")).strip()
    if len(composition) < 12 or not _FRAMING_RE.search(composition):
        problems.append("composition must name the framing rule (>=12 chars, e.g. 'extreme "
                        "asymmetry, the hero off-centre and low in frame', 'low-angle with dramatic "
                        "scale contrast', 'symmetrical top-down') — the layout is part of the "
                        "direction, not the model's choice")

    negative = re.sub(r"\s+", " ", str(raw.get("negative_prompt") or "")).strip()
    if not _NO_TEXT_RE.search(negative):
        problems.append("negative_prompt does not forbid text/watermarks/logos")

    aspect = str(raw.get("aspect_ratio") or DEFAULT_ASPECT).strip()
    if aspect not in FEATURED_ASPECTS:
        problems.append(f"aspect_ratio {aspect!r} is not a featured-header shape "
                        f"(one of {', '.join(FEATURED_ASPECTS)})")
    resolution = str(raw.get("resolution") or "1K").strip().upper()
    if resolution not in FEATURE_RESOLUTIONS:
        problems.append(f"resolution {resolution!r} is not one of {', '.join(FEATURE_RESOLUTIONS)}")

    alt = re.sub(r"\s+", " ", str(raw.get("alt_text") or "")).strip()
    if not 20 <= len(alt) <= 125:
        problems.append(f"alt_text is {len(alt)} chars — the desk writes 125 or fewer so a screen "
                        f"reader reads it whole")
    if _ALT_PREFIX_RE.match(alt) or _ALT_MEDIUM_RE.match(alt):
        problems.append("alt_text opens on the medium ('image/photo/render of…') — describe the "
                        "subject instead; a screen reader gains nothing from the medium")
    if _NON_ENGLISH_RE.search(alt):
        problems.append("alt_text is not in English")

    caption = re.sub(r"\s+", " ", str(raw.get("caption") or "")).strip()
    if not caption or len(caption) > 200 or not caption.endswith((".", "!", "?")):
        problems.append("caption must be 1-200 chars and end on a sentence")

    title = re.sub(r"\s+", " ", str(raw.get("title") or "")).strip()
    if not 3 <= len(title) <= 100:
        problems.append("media title must be 3-100 chars (it is the CMS library label, not the headline)")

    credit = re.sub(r"\s+", " ", str(raw.get("credit") or "")).strip()
    if not 3 <= len(credit) <= 80:
        problems.append("credit must be 3-80 chars")

    rationale = re.sub(r"\s+", " ", str(raw.get("rationale") or "")).strip()
    if len(rationale) < 40:
        problems.append("rationale must be >=40 chars — name the editorial reason for this treatment")

    cue = re.sub(r"\s+", " ", str(raw.get("cue") or "")).strip().strip('"')
    if not cue or len(cue.split()) > 10:
        problems.append("cue must be <=10 words quoted from the article")
    elif cue.lower() not in article_core_text(article_md).lower():
        problems.append(f"cue {cue[:50]!r} is not a verbatim phrase in the article — the direction has to "
                        f"come from this text, not from the model's idea of the topic")

    # The frame's subject, in plain language. Unvalidated until now, which is how a brief could
    # carry a prompt about nothing: if the director cannot say what is in the frame, it does not
    # know — and the reader gets a header unrelated to the article.
    subject = re.sub(r"\s+", " ", str(raw.get("subject") or "")).strip()
    if len(subject) < 10:
        problems.append("subject must state what is in the frame (>=10 chars)")

    if raw.get("depicts_real_brand"):
        problems.append("the brief depicts a real company's product/logo — depict the mechanism, not the mark")

    if problems:
        raise BriefError("; ".join(problems))

    main_idea = re.sub(r"\s+", " ", str(raw.get("main_idea") or "")).strip()
    object_or_scene = re.sub(r"\s+", " ", str(raw.get("object_or_scene") or "")).strip()
    core_thesis = re.sub(r"\s+", " ", str(raw.get("core_thesis") or "")).strip()
    core_conflict = re.sub(r"\s+", " ", str(raw.get("core_conflict") or "")).strip()

    return Brief(
        style_id=style_id, rationale=rationale, cue=cue,
        subject=subject[:300], composition=composition,
        model=model, prompt=prompt, negative_prompt=negative, aspect_ratio=aspect,
        resolution=resolution, alt_text=alt, caption=caption, title=title, credit=credit,
        depicts_real_brand=False, main_idea=main_idea, object_or_scene=object_or_scene,
        core_thesis=core_thesis, core_conflict=core_conflict,
        model_note=model_note)


# ─────────────────────────────────────────────────────────────────────────────
# the art director (frontier LLM, JSON out)
# ─────────────────────────────────────────────────────────────────────────────

def _env_values() -> dict[str, list[str]]:
    """Every KEY's values from the repo .env and the Hermes env files, in file order (never printed).

    A name can carry different values in different files: the repo .env and `/root/.hermes/.env`
    both hold an `ANTHROPIC_API_KEY`, and only the stylist profile's is the kie.ai gateway key
    (`Bearer f9f…`) while the others are Anthropic-direct (`sk-ant-…`). Callers therefore pick the
    value whose *shape* they need — trusting file order here is how the pipeline ends up holding a
    key that authenticates everywhere except the API it is about to call.
    """
    values: dict[str, list[str]] = {}
    for path in (ROOT / ".env", pathlib.Path("/root/.hermes/.env"),
                 pathlib.Path("/root/.hermes/profiles/stylist/.env")):
        if not path.exists():
            continue
        for line in path.read_text(encoding="utf-8", errors="replace").splitlines():
            line = line.strip()
            if not line or line.startswith("#") or "=" not in line:
                continue
            key, value = line.split("=", 1)
            values.setdefault(key.strip(), []).append(value.strip().strip('"').strip("'"))
    return values


def _lookup(name: str) -> list[str]:
    """The environment's value first, then every file's — all of them, not just the first."""
    found = [v for v in [os.environ.get(name, "")] if v]
    return found + [v for v in _env_values().get(name, []) if v]


def kie_api_key() -> str:
    """The kie.ai key: the same gateway credential the stylist uses.

    Lookup order is explicit and reported on failure — the pipeline must never quietly generate
    nothing because a key was in an unexpected place or the wrong kind of key was picked up.
    """
    for value in _lookup("KIE_API_KEY"):
        return value.replace("Bearer ", "").strip()
    for value in _lookup("ANTHROPIC_API_KEY"):
        if value.startswith("Bearer ") and not value.startswith("Bearer sk-ant"):
            return value.replace("Bearer ", "").strip()
    raise IllustrationError(
        "no kie.ai key — set KIE_API_KEY (repo .env or the environment). The key is the same one the "
        "stylist profile holds as ANTHROPIC_API_KEY=Bearer <kie key>; an Anthropic direct key "
        "(sk-ant-…) will not authenticate against api.kie.ai.")


def gemini_key() -> str:
    key = (_lookup("GOOGLE_API_KEY") or [""])[0]
    if not key:
        raise IllustrationError("no GOOGLE_API_KEY — the art director runs on Gemini "
                                f"({GEMINI_MODEL}); the Loop 3 stylist uses the same key")
    return key


def director_prompt(article_md: str, *, history: list[str], allowed: tuple) -> str:
    """The commission the art director answers. Everything it may rely on is in here."""
    fm, body = split_frontmatter(article_md)
    title = (fm.get('title') or '').strip()
    excerpt = article_excerpt(article_md)
    headings = re.findall(r"^##\s+(.+)$", body, re.M)[:6]
    menu = "\n".join(
        f"- {s.id} ({s.label}): reach for it when {s.when}. Medium: {s.medium}. "
        f"Craft: {s.craft}. Catalogue model: {MODELS[s.model]}."
        for s in STYLES.values())
    history_line = ", ".join(history) if history else "(no illustrations on file yet)"
    numbers = "\n".join(f"- {n}" for n in _numbers(article_md)) or "(none)"
    sources = ", ".join(source_names(article_md)) or "(none)"
    # A treatment re-admitted to keep a family available is not the same as an allowed repeat: say
    # so, or the director reads a contradiction between this list and the recent history above it.
    readmitted = [s for s in allowed if s in set(history[:HISTORY_WINDOW])]
    readmit_line = ("\nNote: " + ", ".join(readmitted) +
                    " appears above as recently used and is re-admitted only so that its model is "
                    "not left with no treatment at all — choose it only if it genuinely fits this "
                    "story.\n") if readmitted else ""
    return f"""You are the art director on an industry-analysis editorial desk. You commission ONE \
featured image per article: the 16:9 header a reader sees above the headline and that the CMS \
shows as the article's card. You are not a preset — you read THIS text and pick the treatment it \
deserves, and you change treatment between articles so the desk does not look like one filter \
over forty posts.

CREATIVE PROCESS (MAGAZINE COVER STANDARD: CONCEPTUAL, ARRESTING, NON-LITERAL):
You are an Art Director, NOT a search engine. We are so trained to be literal: asking for "work" yields a laptop on a coffee table; asking for "AI" yields a server rack in a datacenter. That is boring, generic stock filler.
The header image is the first promise to the reader — the front door to the house. It must make someone pause, think, and click.
- THE HERO SUBJECT MUST DIRECTLY EMBODY THE STORY'S CORE PROTAGONIST, MACHINE, OR SYSTEMIC PHENOMENON:
  * If the headline or lead names an electric vehicle (EV), car, cargo vessel, intermodal gantry, industrial turbine, or robotic arm: THAT MACHINE MUST BE THE HERO IN THE FRAME! Never hide or omit the vehicle/machine.
  * Capture the core theme, mood, and tension through dramatic environmental storytelling and conflict (e.g. an unbranded EV powering a home during a blackout), NOT boring stock photos or cheesy clip art.
- USE CONCEPTUAL AND SYMBOLIC VISUAL STORYTELLING: employ powerful metaphors, atmospheric elements, striking color palettes, and minimalistic yet impactful compositions.
- REJECT BORING, STERILE TROPES — THIS IS THE FAILURE TO AVOID:
  * NEVER a floating abstract cube, a plain server rack on a neutral gradient, an empty floating widget, or an abstract object with no environment. No sterile object studies, no grey-on-grey.
  * FOR ENTERPRISE AI / SOFTWARE / MODELS / COMPUTE: Do not default to generic, uninspired datacenters or blue circuit traces as a lazy shortcut. You do NOT need to avoid these environments entirely if they enhance the main object or idea — for example, showing a GPU blade in a high-density rack to illustrate datacenter hardware costs is excellent. Capture tension and scale through evocative environments or symbolic optics (e.g. beam-splitters dividing light across dark basalt, monolithic slabs in equilibrium, razor-thin blades of golden light, or precision mechanical balances).
  * EVERY scene must have physical presence and material depth: authentic tactile context, material weight, and dramatic lighting. The reader must feel the atmosphere, textures, and tension — never a generic render floating on a void.
  * A SYSTEMIC, SOFTWARE OR OPERATIONAL STORY IS NEVER A PRODUCT SHOT. If the subject is not a thing a reader could buy or handle, do not answer with a single object on a studio backdrop — put the hero in an evocative environment or constructed schematic instead (a hall, a plant, a yard, a control room, a routing bay). A studio still (studio_object, document_flatlay, clay_render) is for a story whose subject really is a purchasable or handable thing, and even then it must sit in a material world: weight, contact shadow, a textured surface, dramatic directional light — never a grey sweep with nothing in it.
  * THE IMAGE MUST DESCRIBE THE TOPIC conceptually and evoke the story's own subject-matter classes with unmistakable narrative weight:
    * physical components, materials or a supply-chain bottleneck — freight, staging, stock, tooling, raw material;
    * a policy collision, regulatory shift or multi-faceted market move — a filing, a notice, a clearance, a market board;
    * infrastructure, automation or scale-driven industrial change — a yard, a hall, a line, a substation;
    * a systemic process or technical engineering operation — a cutaway, a plant, a routing bay, a control room.
    For a story whose own subject is engineering or hardware, the vocabulary is sectioned mechanical hardware, precise physical fasteners, industrial brushed metal framing — but ONLY because that is what the story is about. Never a lone bolt, screw or scrap of metal standing in for an abstract idea (domain rule 6): that is a micro-metaphor, not a subject.

You MUST execute this 4-step creative method:

STEP 1: ANCHOR ON THE CORE THESIS ('ONE BIG THING') & EXTRACT THE GOVERNING CONFLICT
Do NOT just read the headline. Read the ARTICLE SUBSTANTIVE CONTENT below carefully.
- The hero subject MUST visually embody `One big thing: {fm.get('one_big_thing', '')}` — the single non-negotiable revelation and central assertion of the article.
- BEWARE THE PERIPHERAL ANECDOTE TRAP: Articles frequently use minor examples, supporting anecdotes, or incidental props (e.g., a screw, a delivery van, a specific chip model, a pallet of scrap, a coffee cup, packaging tape) to illustrate an abstract concept. NEVER elevate an incidental anecdote into the hero subject!
- BEWARE INVERTING THE PROTAGONIST: When an article is about an EV turning into a home backup battery, the EV is the primary protagonist, not an empty wall panel or meter box! Do not swap the main actor for a background utility box. If a car, truck, ship, or turbine is the subject of the story, depict the unbranded vehicle/machine in its narrative context!
Identify the central tension, turning point, or real-world stake. What is the core dramatic conflict or economic pressure of this story? If two forces collide, compress, or trade off against each other (e.g. rising capital costs vs automation payoff, cloud monopoly vs open weights, memory bottlenecks throttling GPU compute), identify them.
(State this in your `core_thesis`, `core_conflict`, and `main_idea` fields).

STEP 2: SELECT AN EVOCATIVE HERO OBJECT OR SCENE (CONCEPTUAL & SYMBOLIC STORYTELLING)
Choose a tangible, storytelling hero object or an authentic narrative scene that powerfully represents that main idea without being literal or pedestrian.
Where applicable, embody the core conflict through physical tension: a central object or mechanism being squeezed, compressed, balancing, or under load from competing forces; or an evocative, atmospheric environment capturing the inflection point.
(State this in your `object_or_scene` field).
- CHOOSE STORYTELLING OBJECTS & ATMOSPHERIC SCENES GROUNDED IN THE ARTICLE'S VERTICAL:
  Inspect `Vertical: {fm.get('vertical', '')}` and the article's core thesis. Verticals across the desk: enterprise AI, supply chain, energy / utilities, heavy industry, finance / tax, residential / home, career / compensation, personal tech / tinkering, cross-border living.
  * For enterprise AI / multi-agent systems / software / compute / finops: Do NOT draw a datacenter, server rack, OR plumbing/pneumatic valves! Use conceptual, symbolic visual storytelling — an optical beam-splitter prism dividing a single beam of warm light into parallel rays across dark obsidian stone, a high-precision axonometric technical cutaway of coordinated processing bays, monolithic stone slabs in delicate equilibrium, an intricate brass pendulum, or clean architectural light-and-shadow divides.
  * For supply chain / logistics / warehousing / freight: An evocative scene capturing balance, capacity, or flow with crystal-clear air and high-contrast lighting — towering cargo structures under hard raking sunlight, an intermodal gantry silhouetted against twilight, or an authentic staging floor with dramatic directional lighting and deep contact shadows. Do NOT drown the scene in grey fog, murky haze, or overcast washouts.
  * For energy / utilities / infrastructure / climate: High-voltage transformer substations, utility-scale battery storage banks, industrial copper busbars, or wind/solar installations under dramatic skies.
  * For heavy industry / manufacturing / hardware: Precision CNC machining spindles throwing aluminum chips, glowing induction heating coils, robotic welding arms, or electronic PCB assembly benches.
  * For finance / tax / governance / legal: Forensic audit desks with heavy leather ledgers under focused desk lamps, embossed legal documents, brass balance scales, or vintage bank vault doors.
  * For residential / home / energy resilience (V2H, home batteries, microgrids): When the story is about vehicle-to-home (V2H) or electric vehicles backing up a home, the hero subject MUST BE an unbranded modern electric vehicle parked on a residential driveway or open garage at dusk / night, connected to the house by an illuminated heavy-duty charging umbilical cable, with warm light glowing from the house windows during a dark neighborhood outage (the car functioning as the household power plant). For general home infrastructure/equity: a suburban house envelope at dusk lit by a single workman's site lamp, a garage utility wall of inverter and service panel, a roofline solar array or heat-pump condenser in dawn light, or a homeowner's permit bench.
  * For career / compensation / equity: A desk with a dossier of vesting documents and a stock-certificate folio under a focused lamp, or an office removal crate beside a packed career file.
  * For personal tech / tinkering / micro-economics: A workbench scene with focused spotlighting — a filament-snarled aborted 3D print on a glass bed, precision hand tools over aluminum chips, or a bench of labelled component drawers.
  * For cross-border living / relocation: Two mismatched national documents on a desk, a moving crate beside a pair of time clocks, or an airport-side freight container under dawn haze.

STEP 3: CHOOSE THE BEST TREATMENT & MODEL
Select the treatment from the catalogue that provides the most stunning visual impact for your chosen scene. Weave that treatment's core vocabulary naturally into the prompt.

WRITE THE PROMPT IN THE IDIOM OF THE MODEL THAT WILL RENDER IT — the two families are read differently:
- flux-2 Pro (editorial_macro, cinematic_still, document_flatlay, long_lens_industry, studio_object, architectural_night) stages a PHOTOGRAPH. Name the optic and its falloff, the light in the room, the material of the surface, and place the subject in a real environment.
- Nano Banana Pro (clay_render, technical_isometric, component_assembly, paper_collage) builds a STRUCTURE. State the parts and how each is arranged, what each is made of, and the light that falls on it — a spatial construction, not a mood paragraph.
Both must carry a framing rule, and neither may leave an empty sweep under the object: even a studio treatment sits in a material world.

STEP 4: CRAFT A CINEMATIC, HIGH-TEXTURE GENERATION PROMPT
Write a prompt (15-120 words) with rich sensory and visual details. Aim for clarity, balance, and a visually arresting sense of curiosity that draws readers in:
- Landscape composition (16:9): wide framing with generous editorial negative space and deliberate breathing room, an ASYMMETRIC composition where the hero subject commands the frame off-centre with heavy editorial framing (like cover art, but strictly without any text or typography).
- Camera angle & optics: name a real optic and its falloff explicitly — 35mm anamorphic wide with dramatic falloff, 100mm macro at a razor-sharp focal plane, 200mm telephoto compression, low-angle perspective — and the depth of field it produces.
- Lighting & atmosphere: sculpt the scene with intentional light — chiaroscuro, a single directional window light, low-raking golden-hour sun, blue-hour twilight with warm amber worklights, deep shadows, prominent rim highlights on metallic edges, crisp crystalline air, clean high-contrast atmosphere, soft gradients.
- Textures & materials: brushed metals, weathered corrugated steel, frosted copper tubing, dusty workshop glass, textured matte polymers, tactile paper stock, polished basalt, or optical glass.
- Mood: modern, premium, editorial cover standard. Quiet confidence, refined aesthetics, sophisticated color palette. Never chaotic, overly busy, or pedestrian.

VISUAL ANCHOR:
Headline: {title}
Excerpt: {excerpt}

ARTICLE DETAILS
Vertical: {fm.get('vertical', '')} | Persona: {fm.get('persona', '')}
One big thing: {fm.get('one_big_thing', '')}
Section headings: {' | '.join(headings)}
Numbers section:
{numbers}
Sources (names only): {sources}

ARTICLE SUBSTANTIVE CONTENT (Read this carefully to ground the visual in the actual industry context, facilities, equipment, operational reality, and core thesis):
---
{article_core_text(article_md)[:3500]}
---

TREATMENT CATALOGUE
{menu}

TREATMENTS ALREADY USED, MOST RECENT FIRST: {history_line}
You MUST choose one of: {', '.join(allowed)} — a treatment may not repeat within the last \
{HISTORY_WINDOW} illustrations.
{readmit_line}
DOMAIN GROUNDING
1. NEVER DEPICT A GENERIC OFFICE WORKER AT A DESK: Do not default to stock photos of a person \
typing at a laptop, sitting at an office desk, or in a conference room. No people facing camera.
2. ROTATE MEDIUMS & DO NOT DEFAULT ONLY TO REAL-LIFE PHOTOS: The publication relies on a rich \
mix of treatments — photographic (macro, architectural, document still life) AND illustrative or \
constructed (matte 3D clay renders, technical isometric cutaways, studio object shots, paper collages).
3. EVERY MEDIUM MUST DEPICT A RECOGNIZABLE SUBJECT: In every treatment, the subject must be a \
recognizable physical object, mechanical assembly, or clear symbolic silhouette derived from the \
Headline and Excerpt. If the story is about a company's vehicle, machine, or hardware, depict the authentic machine/vehicle faithfully reflecting the brand's genuine industrial design.
4. NO BARE SHAPES OR ABSTRACT SCRAPS: Cubes, spheres, wedges, slabs, rectangles, amorphous blobs, \
and random torn paper scraps are not subjects. A prompt whose subject is bare geometry or unformed \
paper scraps is refused. Ground the subject in a tangible mechanism or symbolic object.
5. MATURE, PROFESSIONAL B2B GROUNDING — NEVER DEPICT TOYS OR CARTOON GRAPHICS:
This is an institutional, executive B2B publication read by supply chain leaders, CFOs, and engineers.
- NEVER depict literal children's toys, clip-art silhouettes, or playful nursery symbols.
- For stories involving physical operations, energy, factories, shipping, transport, infrastructure, or hardware, ALWAYS prefer photographic treatments that depict real physical facilities, machinery, and logistics: cinematic_still (one decisive moment or place), long_lens_industry (scale), architectural_night (the change after hours). Do NOT answer a systemic, process or capacity story with editorial_macro (see rule 6) — a 100mm close-up strips away the environment that makes the story legible.
- Every visual must feel like an authentic, high-end editorial feature image from Bloomberg, The Wall Street Journal, or Financial Times.
6. UNIVERSAL DOMAIN SEMIOTICS — NO OBSCURE MICRO-METAPHORS:
- Match the visual world conceptually to the article's own `Vertical` and substantive topic without resorting to literal clichés. Never cross-contaminate unrelated domains (e.g. don't draw a freight truck for an AI article).
- NEVER invent obscure, multi-step intellectual micro-metaphors that require prompt text to decode (e.g. representing an abstract mathematical error, algorithm miss, or financial discrepancy as an ungrounded random metal scrap, isolated screw, or unidentifiable bushing on a workbench).
- NEVER TRANSLATE SOFTWARE OR AI INTO PLUMBING OR PNEUMATIC VALVES: Multi-agent systems, software pipelines, routing topologies, or algorithmic fan-out must NEVER be represented as literal pneumatic valves, hydraulic manifold blocks, pipe splitters, carburetors, or factory plumbing! That is an absurd, unreadable cross-domain literalization. Represent multi-agent coordination, routing, and software architecture with optical/photonic physics (beam-splitter prisms, parallel ray pathways), technical axonometric/isometric cutaways of coordinated processing modules, synchronized precision instruments, or grand architectural vistas.
- DO NOT USE `editorial_macro` FOR SYSTEMIC, ARCHITECTURAL, OR OPERATIONAL TOPICS: Macro lens photography (100mm) zooms in so tightly that it erases environmental storytelling, leaving behind an unrecognizable hunk of material. Reserve `editorial_macro` strictly for stories that literally turn on a single physical artifact, specialized component, material specimen, or document seal. For any systemic, process, capacity, or operational topic in any vertical, choose `cinematic_still` (wide establishing atmosphere), `long_lens_industry` (scale), or `technical_isometric` / `component_assembly` (constructed architecture).

HARD RULES
- Depict a concrete noun or powerful symbolic object from this story (the material, part, place, document or mechanism that carries it). Never a literal stock cliché, and never bare geometry — see the grounding rule above.
- No text, letters, numbers, wordmarks, signage or UI in the image: generated lettering is \
unreadable. Forbid them in `negative_prompt` — and keep that list to the legibility/brand set. \
NEVER enumerate subject matter to exclude: the negative prompt is read by the image model as tokens \
to draw, so "no abstract cubes" is an instruction to draw abstract cubes.
- BRAND & PRODUCT INTEGRITY: When the article focuses on a real company (e.g. Tesla, Maersk, Boeing, NVIDIA, Apple, Caterpillar), depicting their authentic vehicles, vessels, machinery, or hardware is FULLY PERMITTED and encouraged, provided it accurately reflects the brand's genuine industrial design, iconic silhouette, and correct styling. What must be avoided is DEFECTIVE, GARBLED, OR MISSPELLED BRAND LOGOS: diffusion models frequently distort fine typographic text and lettermarks. Therefore, never prompt for isolated close-up text logos or wordmarks that the model might mangle. Let the correct vehicle form factor, signature livery, authentic hardware engineering, and operational context represent the brand proudly and accurately. No recognisable real person, and no human face or hands in frame. No {', '.join(CLICHE_BAN)}.
- The image is cropped and shown small: one subject, generous breathing room, no small detail \
that carries the meaning.
- Alt text describes the subject for a screen reader in <=125 characters, starting with the subject \
itself (never "image of", never "a clay 3D render of…", never the medium). The caption is one \
sentence a reader could quote. The credit is e.g. \
"Illustration: Editorial-Factory Intelligence Unit".

Return ONLY a JSON object, no markdown fence, with exactly these keys:
{{"core_thesis": "1 sentence: the central assertion and insight from 'one_big_thing' that this image communicates",
 "core_conflict": "the governing systemic or economic tension (e.g. write-path persistence vs prompt filters, formula miss vs buffer scale)",
 "main_idea": "1-2 sentences: the core tension, conflict, or revelation extracted from reading the substantive article body",
 "object_or_scene": "the specific hero object or narrative scene chosen to represent the core thesis, capturing the governing mechanism rather than an incidental anecdote",
 "style_id": one of {list(allowed)},
 "rationale": "2-3 sentences: why this treatment for this story",
 "cue": "a phrase of 2-10 words copied verbatim from the article above (strongly prefer quoting the headline, lead, or 'one_big_thing')",
 "subject": "the physical thing in the frame, one clause — representing the governing mechanism, never an incidental anecdote, never a bare shape",
 "composition": "the framing rule that anchors the layout (>=12 chars) — extreme asymmetry, low-angle with scale contrast, symmetrical top-down; the layout is your direction, not the model's choice",
 "model": "{' or '.join(sorted(MODELS))}",
 "model_override_reason": "required only if you deviate from the catalogue model, else omit",
 "prompt": "the generation prompt, 15-120 words, English, in the idiom of the model's family — \
flux stages a photograph (optic, light, material, environment), nano builds a structure (parts, \
arrangement, material, light) — and containing the vocabulary of the treatment you chose",
 "negative_prompt": "short; must name text/watermarks/logos. Never enumerate subject matter to \
exclude — the image model reads the negative as tokens to draw",
 "aspect_ratio": "{FEATURED_ASPECTS[0]}",
 "resolution": "1K for most stories, 2K only when fine physical detail is the point",
 "alt_text": "<=125 chars, the SUBJECT first — never 'a render/photo of…'",
 "caption": "one sentence ending in a full stop",
 "title": "3-100 chars, the CMS media-library label",
 "credit": "Illustration: Editorial-Factory Intelligence Unit",
 "depicts_real_brand": false}}"""


def call_gemini(prompt: str, *, model: str = GEMINI_MODEL, key: str | None = None,
                timeout: int = 180) -> str:
    """One JSON-mode Gemini call. Thinking is dialled down: this is a brief, not an essay."""
    key = key or gemini_key()
    url = (f"https://generativelanguage.googleapis.com/v1beta/models/{model}:generateContent"
           f"?key={key}")
    body = {
        "contents": [{"role": "user", "parts": [{"text": prompt}]}],
        "generationConfig": {"temperature": 0.9, "maxOutputTokens": 8192,
                             "responseMimeType": "application/json",
                             "thinkingConfig": {"thinkingLevel": "low"}},
    }
    req = urllib.request.Request(url, data=json.dumps(body).encode(),
                                 headers={"Content-Type": "application/json"}, method="POST")
    try:
        with urllib.request.urlopen(req, timeout=timeout) as response:
            payload = json.loads(response.read().decode("utf-8", "replace"))
    except urllib.error.HTTPError as exc:
        raise IllustrationError(f"art director call failed: HTTP {exc.code} — "
                                f"{exc.read().decode('utf-8', 'replace')[:300]}") from None
    except Exception as exc:                       # noqa: BLE001 — surface, never swallow (rule 6)
        raise IllustrationError(f"art director call failed: {exc}") from None
    candidates = payload.get("candidates") or []
    text = "".join(part.get("text", "") for part in
                   ((candidates[0].get("content") or {}).get("parts") or [])) if candidates else ""
    if not text.strip():
        raise IllustrationError(f"art director returned no text: {json.dumps(payload)[:300]}")
    return text


def parse_json_object(text: str) -> dict:
    """The director's JSON, tolerant of a fenced block but intolerant of prose around it."""
    cleaned = text.strip()
    fence = re.search(r"```(?:json)?\s*(.*?)```", cleaned, re.S)
    if fence:
        cleaned = fence.group(1).strip()
    try:
        return json.loads(cleaned)
    except json.JSONDecodeError:
        start, end = cleaned.find("{"), cleaned.rfind("}")
        if start >= 0 and end > start:
            try:
                return json.loads(cleaned[start:end + 1])
            except json.JSONDecodeError as exc:
                raise BriefError(f"the brief is not JSON: {exc}") from None
        raise BriefError(f"the brief is not JSON: {cleaned[:200]!r}") from None


def style_history(ledger: pathlib.Path | None = None, limit: int = 12,
                  exclude_slug: str | None = None) -> list[str]:
    r"""Treatments used most recently, newest first — read from the desk's own illustration ledger.

    The style cell is backticked in the ledger (`| \`editorial_macro\` |`), so the cell is
    un-backticked before the catalogue lookup: matching the raw cell found nothing and the rotation
    rule silently saw an empty history.

    `exclude_slug` drops the rows belonging to the article being illustrated now. The rotation
    exists so two DIFFERENT articles do not share a treatment; an article rewritten a week later
    reusing the treatment it already had is not a repetition, and forbidding it would make every
    re-read of a live piece produce a visual the text never earned.
    """
    path = ledger or LEDGER
    if not path.exists():
        return []
    styles: list[str] = []
    for line in reversed(path.read_text(encoding="utf-8", errors="replace").splitlines()):
        cells = [c.strip().strip("`").strip() for c in line.strip().strip("|").split("|")]
        if len(cells) < 4:
            continue
        if exclude_slug and len(cells) > 1 and cells[1] == exclude_slug:
            continue
        style = canonical_style_id(cells[3])
        if style in STYLES:
            styles.append(style)
        if len(styles) >= limit:
            break
    return styles


def allowed_styles(history: list[str], window: int = HISTORY_WINDOW) -> tuple:
    """The catalogue minus the treatments used in the last `window` illustrations.

    Two guards, both learned from the desk's own ledger:

    * The window is a *style* rule and it is deliberately not narrowed to buy variety. At this
      catalogue size four withheld treatments can never empty the desk (ten treatments, at most
      four blocked, six always left); at a window of two a treatment would return after two
      articles instead of four, which is the sameness this desk exists to prevent.
    * A *family* (the two catalogue models — photographic/flux and constructed/nano-banana) is
      small enough to be emptied: three of the four constructed treatments were used back to back
      in the desk's first ten illustrations, and a fourth would have left a story with no
      photograph in it no choice but a photograph. When the window would leave a family with no
      treatment at all, its oldest blocked member is re-admitted.
    """
    blocked = set(history[:window])
    allowed = [s for s in STYLES if s not in blocked]
    for family in sorted({s.model for s in STYLES.values()}):
        if not any(STYLES[s].model == family for s in allowed):
            for used in reversed(history[:window]):    # oldest first: closest to leaving the window
                if STYLES.get(used) and STYLES[used].model == family and used not in allowed:
                    allowed.append(used)
                    break
    if len(allowed) < 3:                           # a tiny catalogue must not deadlock the desk
        return tuple(STYLES)
    return tuple(s for s in STYLES if s in allowed)   # catalogue order: the menu stays stable


def direct(article_md: str, *, history: list[str] | None = None, llm=None,
           pinned_style: str | None = None, pinned_model: str | None = None,
           model: str = GEMINI_MODEL, notes: list | None = None) -> Brief:
    """Ask the art director for a brief, and make it answer again when it breaks a rule.

    A rule violation is fed back verbatim rather than being repaired here: this module will not
    rewrite a director's treatment choice, because the choice is the product. Three refusals raise.
    """
    notes = notes if notes is not None else []
    history = style_history() if history is None else history
    allowed = allowed_styles(history)
    if pinned_style:
        allowed = (pinned_style,) if pinned_style in STYLES else allowed
    llm = llm or call_gemini
    base = director_prompt(article_md, history=history[:HISTORY_WINDOW + 2], allowed=allowed)
    feedback = ""
    last_error = ""
    for attempt in range(1, DIRECTOR_MAX_ATTEMPTS + 1):
        raw = llm(base + feedback, model=model)
        try:
            brief = validate_brief(parse_json_object(raw), article_md, allowed=allowed,
                                   pinned_style=pinned_style, pinned_model=pinned_model)
            brief.attempts = attempt
            brief.director = model
            if brief.model_note:
                notes.append(f"model override: {brief.model_note}")
            return brief
        except BriefError as exc:
            last_error = str(exc)
            notes.append(f"art director attempt {attempt} refused: {exc}")
            feedback = (f"\n\nYOUR PREVIOUS ANSWER WAS REFUSED: {last_error}\n"
                        f"Answer again with a corrected JSON object. Allowed treatments: "
                        f"{', '.join(allowed)}.")
    raise BriefError(f"the art director did not produce a commissionable brief in "
                     f"{DIRECTOR_MAX_ATTEMPTS} attempts — last refusal: {last_error}")


# ─────────────────────────────────────────────────────────────────────────────
# generation (kie.ai: createTask -> recordInfo -> download)
# ─────────────────────────────────────────────────────────────────────────────

@dataclass
class Generation:
    image: bytes
    ext: str
    content_type: str
    task_id: str
    credits: float
    cost_ms: int
    source_url: str
    request: dict


def _http_transport(method: str, url: str, *, body: bytes | None = None,
                    headers: dict | None = None, timeout: int = 120):
    """(status, bytes). The single network seam, so every test can run without kie.ai."""
    req = urllib.request.Request(url, data=body, headers=headers or {}, method=method)
    try:
        with urllib.request.urlopen(req, timeout=timeout) as response:
            return response.status, response.read()
    except urllib.error.HTTPError as exc:
        return exc.code, exc.read()


class KieClient:
    """The smallest client that can commission an image on kie.ai and prove what it got back."""

    def __init__(self, key: str | None = None, *, transport=None, poll_interval: float = 5.0,
                 poll_timeout: float = 420.0, sleeper=time.sleep):
        self.key = key or kie_api_key()
        self.transport = transport or _http_transport
        self.poll_interval = poll_interval
        self.poll_timeout = poll_timeout
        self.sleeper = sleeper

    def _headers(self) -> dict:
        return {"Authorization": f"Bearer {self.key}", "Content-Type": "application/json"}

    def _json(self, method: str, url: str, body: dict | None = None) -> dict:
        status, raw = self.transport(method, url,
                                     body=json.dumps(body).encode() if body is not None else None,
                                     headers=self._headers())
        try:
            parsed = json.loads(raw.decode("utf-8", "replace") or "{}")
        except json.JSONDecodeError:
            raise GenerationError(f"{method} {url} -> HTTP {status}: "
                                  f"{raw[:200]!r} is not JSON") from None
        if status != 200 or parsed.get("code") not in (200, None):
            raise GenerationError(f"{method} {url} -> HTTP {status}: "
                                  f"{parsed.get('msg') or raw[:200]!r}")
        return parsed

    @staticmethod
    def payload(brief: Brief) -> dict:
        """The model-specific `input` object. The two models do NOT take the same fields.

        Flux-2 Pro takes prompt/aspect_ratio/resolution and answers JPEG; Nano Banana Pro takes an
        extra `image_input` list and an explicit `output_format`, and rejects `jpeg` (its allowed
        set is png/webp) — a field difference that silently 500s if it is assumed away.
        """
        common = {"prompt": f"{brief.prompt}\n\n{IMAGE_GUARD}",
                  "aspect_ratio": brief.aspect_ratio, "resolution": brief.resolution}
        if brief.model == "nanobanana":
            return {**common, "image_input": [], "output_format": "png"}
        return common

    def create(self, brief: Brief) -> str:
        parsed = self._json("POST", f"{KIE_BASE}/jobs/createTask",
                            {"model": brief.model_id, "input": self.payload(brief)})
        task_id = ((parsed.get("data") or {}).get("taskId") or "").strip()
        if not task_id:
            raise GenerationError(f"kie.ai returned no taskId for {brief.model_id}: "
                                  f"{json.dumps(parsed)[:200]}")
        return task_id

    def wait(self, task_id: str) -> dict:
        """Poll until the task reaches a terminal state. Timeout is an error, not an empty image."""
        started = time.time()
        state = ""
        while time.time() - started < self.poll_timeout:
            data = (self._json("GET", f"{KIE_BASE}/jobs/recordInfo?taskId={task_id}") or {}).get("data") or {}
            state = str(data.get("state") or "")
            if state == "success":
                return data
            if state == "fail":
                raise GenerationError(f"kie.ai task {task_id} failed: "
                                      f"{data.get('failMsg') or data.get('failCode') or 'no reason given'}")
            self.sleeper(self.poll_interval)
        raise GenerationError(f"kie.ai task {task_id} did not finish within "
                              f"{self.poll_timeout:.0f}s (last state {state!r})")

    def generate(self, brief: Brief, *, attempts: int = 3, notes: list | None = None) -> Generation:
        """Commission the image, retrying the task when kie.ai fails the job.

        kie.ai's upstreams fail intermittently (`Internal Error` on an accepted task) and the
        stylist's Claude gate already retries 3× for the same reason; a failed task is not billed
        (verified: creditsConsumed=0 on a failure), so a retry costs nothing but time. Each attempt
        is reported — a retry that eventually succeeds is still visible in the run log.
        """
        last_error = ""
        for attempt in range(1, max(1, attempts) + 1):
            try:
                return self._generate_once(brief)
            except GenerationError as exc:
                last_error = str(exc)
                message = f"generation attempt {attempt}/{attempts} failed: {exc}"
                if notes is not None:
                    notes.append(message)
                print(f"    - {message}", file=sys.stderr)
                if attempt < attempts:
                    self.sleeper(self.poll_interval * attempt)
        raise GenerationError(f"{brief.model_id} failed {attempts}× — last: {last_error}")

    def _generate_once(self, brief: Brief) -> Generation:
        task_id = self.create(brief)
        data = self.wait(task_id)
        urls = json.loads(data.get("resultJson") or "{}").get("resultUrls") or []
        if not urls:
            raise GenerationError(f"kie.ai task {task_id} succeeded with no resultUrls: "
                                  f"{str(data.get('resultJson'))[:200]}")
        status, blob = self.transport("GET", urls[0], headers={})
        if status != 200 or not blob:
            raise GenerationError(f"could not download {urls[0]} (HTTP {status})")
        ctype = _sniff(blob)
        if not ctype:
            raise GenerationError(f"{urls[0]} is not a JPEG/PNG/WEBP image ({len(blob)} bytes) — "
                                  f"kie.ai result URLs expire, so this must be fetched immediately")
        return Generation(image=blob, ext=_EXT[ctype], content_type=ctype, task_id=task_id,
                          credits=float(data.get("creditsConsumed") or 0),
                          cost_ms=int(data.get("costTime") or 0), source_url=urls[0],
                          request={"model": brief.model_id, "input": self.payload(brief)})


_EXT = {"image/jpeg": "jpg", "image/png": "png", "image/webp": "webp"}


def _sniff(blob: bytes) -> str:
    """The image's real type from its magic bytes — never from the extension in a URL."""
    if blob[:3] == b"\xff\xd8\xff":
        return "image/jpeg"
    if blob[:8] == b"\x89PNG\r\n\x1a\n":
        return "image/png"
    if blob[:4] == b"RIFF" and blob[8:12] == b"WEBP":
        return "image/webp"
    return ""


# ─────────────────────────────────────────────────────────────────────────────
# storage: the image, its sidecar, and the desk's ledger
# ─────────────────────────────────────────────────────────────────────────────

def asset_dir(slug: str, root: pathlib.Path | None = None) -> pathlib.Path:
    return (root or ROOT) / "context" / "assets" / "illustrations" / slug


def sidecar_path(slug: str, root: pathlib.Path | None = None) -> pathlib.Path:
    return asset_dir(slug, root) / "featured.json"


def read_sidecar(slug: str, root: pathlib.Path | None = None) -> dict | None:
    path = sidecar_path(slug, root)
    if not path.exists():
        return None
    try:
        return json.loads(path.read_text(encoding="utf-8"))
    except json.JSONDecodeError as exc:
        raise IllustrationError(f"{path} is not valid JSON ({exc}) — a corrupt sidecar must be fixed, "
                                f"not overwritten blindly") from None


def store(slug: str, generation: Generation, brief: Brief, md: str, *,
          root: pathlib.Path | None = None, now: str | None = None) -> dict:
    """Write the bytes + the full provenance sidecar. Returns the sidecar as written."""
    directory = asset_dir(slug, root)
    directory.mkdir(parents=True, exist_ok=True)
    previous = read_sidecar(slug, root) or {}
    filename = f"featured.{generation.ext}"
    (directory / filename).write_bytes(generation.image)
    for stale in directory.glob("featured.*"):                 # an earlier generation in another format
        if stale.name not in (filename, "featured.json"):
            stale.unlink()
    revision = int(previous.get("revision") or 0) + 1
    history = list(previous.get("history") or [])
    if previous.get("revision"):
        history.append({k: previous.get(k) for k in
                        ("revision", "style", "model", "prompt", "task_id", "sha256",
                         "generated_at", "source_hash")})
    record = {
        "slug": slug, "revision": revision, "history": history,
        "style": brief.style_id, "style_label": brief.style.label,
        "style_when": brief.style.when,
        "model": brief.model_id, "model_key": brief.model, "model_note": brief.model_note,
        "aspect_ratio": brief.aspect_ratio, "resolution": brief.resolution,
        "prompt": brief.prompt, "negative_prompt": brief.negative_prompt,
        "rationale": brief.rationale, "cue": brief.cue, "subject": brief.subject,
        "core_thesis": brief.core_thesis, "core_conflict": brief.core_conflict,
        "composition": brief.composition,
        "alt_text": brief.alt_text, "caption": brief.caption, "title": brief.title,
        "credit": brief.credit, "depicts_real_brand": brief.depicts_real_brand,
        "director": brief.director, "director_attempts": brief.attempts,
        "pinned": brief.pinned or {},
        "file": filename,
        "local_path": str((directory / filename).relative_to(root or ROOT)),
        "ext": generation.ext, "content_type": generation.content_type,
        "bytes": len(generation.image),
        "sha256": "sha256:" + hashlib.sha256(generation.image).hexdigest()[:32],
        "source_hash": source_hash(md),
        "source_chars": len(article_core_text(md)),
        "task_id": generation.task_id, "credits": generation.credits,
        "cost_ms": generation.cost_ms, "provider_url": generation.source_url,
        "provider_request": generation.request,
        "generated_at": now or datetime.datetime.now(datetime.timezone.utc)
                                            .isoformat(timespec="seconds"),
    }
    sidecar_path(slug, root).write_text(json.dumps(record, indent=2) + "\n", encoding="utf-8")
    return record


def append_ledger(record: dict, *, md: str, root: pathlib.Path | None = None) -> None:
    """Add one row per generation to `context/illustration_log.md` — the desk's treatment history.

    This table is what the next article's director reads to avoid repeating a treatment, so it is
    written once per generation and never rewritten (idempotency lives in the sidecar, not here).
    """
    fm, _ = split_frontmatter(md)
    path = (root or ROOT) / "context" / "illustration_log.md"
    header = ("# Illustration Log\n\n"
              "One row per generated featured image (`scripts/illustration_creator.py`). The art\n"
              "director reads the most recent treatments from here so the desk does not repeat one\n"
              "back-to-back; `featured.json` beside each image holds the full brief.\n\n"
              "| Date | Slug | Vertical | Style | Model | Aspect | Resolution | Credits | File |\n"
              "| --- | --- | --- | --- | --- | --- | --- | --- | --- |\n")
    row = ("| {date} | `{slug}` | {vertical} | `{style}` | {model} | {aspect} | {resolution} | "
           "{credits:g} | `{path}` |\n").format(
        date=record["generated_at"][:10], slug=record["slug"], vertical=fm.get("vertical", ""),
        style=record["style"], model=record["model_key"], aspect=record["aspect_ratio"],
        resolution=record["resolution"], credits=record["credits"], path=record["local_path"])
    if not path.exists():
        path.write_text(header + row, encoding="utf-8")
        return
    text = path.read_text(encoding="utf-8")
    if f"| `{record['slug']}` |" in text and record["revision"] == 1:
        return
    if not text.endswith("\n"):
        text += "\n"
    path.write_text(text + row, encoding="utf-8")


# ─────────────────────────────────────────────────────────────────────────────
# frontmatter + Supabase metadata
# ─────────────────────────────────────────────────────────────────────────────

IMAGE_KEYS = ("image_path", "image_style", "image_model", "image_alt", "image_caption", "image_credit")


def frontmatter_fields(record: dict) -> dict:
    """The reader-facing image fields the artifact carries (flat: the pipeline's parser is flat)."""
    return {
        "image_path": record["local_path"],
        "image_style": record["style"],
        "image_model": record["model_key"],
        "image_alt": record["alt_text"],
        "image_caption": record["caption"],
        "image_credit": record["credit"],
    }


def supabase_metadata(record: dict) -> dict:
    """`metadata.illustration` — what the CMS push needs to upload and caption the image."""
    return {k: record.get(k) for k in (
        "slug", "style", "style_label", "model", "model_key", "aspect_ratio", "resolution",
        "prompt", "negative_prompt", "rationale", "cue", "subject", "composition", "alt_text",
        "caption", "title",
        "credit", "local_path", "ext", "content_type", "bytes", "sha256", "source_hash",
        "task_id", "credits", "generated_at", "revision", "director", "director_attempts")}


def _kv(key: str, value) -> str:
    text = str(value).replace("\\", "\\\\").replace('"', '\\"')
    return f'{key}: "{text}"'


def _write_frontmatter(md: str, fields: dict) -> str:
    """Add or replace the image keys *inside* the existing frontmatter block, line by line.

    Deliberately not a re-emit of the parsed dict: these artifacts carry a YAML list
    (`sources:`) and bare booleans (`synthesis: true`) that a flat re-emit would flatten or drop,
    and the anchors are load-bearing (verify.sh §8 checks them). Everything this function does not
    touch is returned byte-for-byte as it was.
    """
    if not md.startswith("---"):
        return md
    parts = md.split("---", 2)
    if len(parts) < 3:
        return md
    _, fm_text, body = parts
    lines = fm_text.strip("\n").splitlines()
    remaining = dict(fields)
    for index, line in enumerate(lines):
        key = line.split(":", 1)[0].strip() if ":" in line and not line.startswith((" ", "\t")) else ""
        if key in remaining:
            lines[index] = _kv(key, remaining.pop(key))
    for key, value in remaining.items():
        lines.append(_kv(key, value))
    return "---\n" + "\n".join(lines) + "\n---" + body


def slug_from_frontmatter(md: str) -> str:
    """The artifact's asset key: its frontmatter slug with any leading `YYYY-MM-DD_` stripped.

    One artifact in this corpus still carries the date inside its frontmatter slug. Left alone it
    files the image under a directory nothing else knows: the CMS push resolves the media by the
    BARE post slug (`<slug>-featured`), so the image would be generated, committed, paid for — and
    silently never attached. Normalized here, once, for every caller (CLI, backfill, sweep).
    """
    fm, _ = split_frontmatter(md)
    return re.sub(r"^\d{4}-\d{2}-\d{2}_", "", (fm.get("slug") or "").strip())


def has_illustration(md: str) -> bool:
    fm, _ = split_frontmatter(md)
    return all(fm.get(k) for k in ("image_path", "image_style", "image_alt"))


def check_artifact(md: str, *, root: pathlib.Path | None = None,
                   slug: str | None = None) -> list[str]:
    """Consistency problems for one artifact, metadata only — the image binary may live on the host.

    verify.sh runs inside the deployed container, which has the committed sidecar but not the
    (gitignored) image, so the file's presence is reported by `report` and required only by the
    host-side sweep, never by the gate.
    """
    fm, _ = split_frontmatter(md)
    slug = slug or slug_from_frontmatter(md)
    problems: list[str] = []
    if not slug:
        return ["no slug in frontmatter"]
    missing = [k for k in ("image_path", "image_style", "image_alt") if not fm.get(k)]
    if missing and not has_illustration(md):
        return [f"no illustration ({', '.join(missing)} absent)"]
    problems += [f"frontmatter missing {k}" for k in missing]
    sidecar = read_sidecar(slug, root)
    if not sidecar:
        problems.append(f"no sidecar at context/assets/illustrations/{slug}/featured.json")
        return problems
    for key, field_name in (("image_alt", "alt_text"), ("image_caption", "caption"),
                            ("image_style", "style"), ("image_credit", "credit"),
                            ("image_path", "local_path")):
        if fm.get(key) and sidecar.get(field_name) and fm[key] != sidecar[field_name]:
            problems.append(f"frontmatter {key} != sidecar {field_name}")
    return problems


# ─────────────────────────────────────────────────────────────────────────────
# the pass the pipeline calls
# ─────────────────────────────────────────────────────────────────────────────

def ensure_illustration(md: str, *, root: pathlib.Path | None = None, slug: str | None = None,
                        client=None, llm=None, force: bool = False, pinned_style: str | None = None,
                        pinned_model: str | None = None, notes: list | None = None,
                        ledger: pathlib.Path | None = None) -> tuple[str, list[str], dict | None]:
    """(markdown, notes, illustration metadata). Commissions one image if the artifact needs one.

    Idempotency is by content: an artifact whose frontmatter already carries image fields AND whose
    sidecar `source_hash` matches the current text is left alone. A rewritten article has a new
    hash, so it gets a new reading — and the sidecar keeps the previous one in `history`.
    """
    notes = notes if notes is not None else []
    fm, _ = split_frontmatter(md)
    slug = slug or slug_from_frontmatter(md)
    if not slug:
        raise IllustrationError("the artifact has no slug — it is the asset's idempotency key")

    existing = read_sidecar(slug, root)
    current_hash = source_hash(md)
    if not force and existing and existing.get("source_hash") == current_hash:
        # The image already exists and was read from these exact words — with or without the
        # frontmatter fields. An article illustrated AFTER it was published (the sweep, or a
        # hand-run) has the image and a brief but no `image_*` fields in the artifact, and
        # regenerating here would spend credits for a new reading of unchanged text. Fill the
        # fields in instead.
        if has_illustration(md):
            notes.append(f"illustration already present: {existing['style']} "
                         f"({existing['model_key']}, rev {existing.get('revision', 1)}) — text unchanged")
            return md, notes, supabase_metadata(existing)
        notes.append(f"already illustrated (rev {existing.get('revision', 1)}, {existing.get('style')}) "
                     f"for this unchanged text — writing its fields into the frontmatter, "
                     f"generating nothing")
        return _write_frontmatter(md, frontmatter_fields(existing)), notes, supabase_metadata(existing)

    if existing and existing.get("source_hash") != current_hash:
        notes.append(f"the article text changed since rev {existing.get('revision', 1)} "
                     f"({existing.get('style')}) — commissioning a new reading")

    history = style_history(ledger if ledger is not None else ledger_path(root), exclude_slug=slug)
    brief = direct(md, history=history, llm=llm, pinned_style=pinned_style,
                   pinned_model=pinned_model, notes=notes)
    brief.pinned = {k: v for k, v in (("style", pinned_style), ("model", pinned_model)) if v}
    notes.append(f"direction: {brief.style_id} ({brief.style.label}) on {brief.model_id} — "
                 f"cue {brief.cue[:60]!r}; allowed were {', '.join(allowed_styles(history))}")

    gen = (client or KieClient()).generate(brief, notes=notes)
    record = store(slug, gen, brief, md, root=root)
    append_ledger(record, md=md, root=root)
    notes.append(f"generated {record['sha256']} ({record['bytes'] // 1024} KB, {record['ext']}, "
                 f"{gen.credits:g} credits, task {gen.task_id}) -> {record['local_path']}")
    return _write_frontmatter(md, frontmatter_fields(record)), notes, supabase_metadata(record)


# ─────────────────────────────────────────────────────────────────────────────
# CLI — report (default, no spend) | --apply | --backfill | --check
# ─────────────────────────────────────────────────────────────────────────────

def _report(path: pathlib.Path, root: pathlib.Path | None = None) -> list[str]:
    md = path.read_text(encoding="utf-8")
    fm, _ = split_frontmatter(md)
    slug = slug_from_frontmatter(md)
    lines: list[str] = []
    sidecar = read_sidecar(slug, root) if slug else None
    if has_illustration(md):
        drift = check_artifact(md, root=root, slug=slug)
        lines.append(f"{path.name}: {fm.get('image_style')} ({fm.get('image_model')})"
                     + ("" if not drift else "  DRIFT: " + "; ".join(drift)))
        if sidecar:
            age = (source_hash(md) == sidecar.get("source_hash"))
            lines.append(f"    {sidecar.get('local_path')}  rev {sidecar.get('revision')}  "
                         f"{sidecar.get('bytes', 0) // 1024} KB  "
                         f"task {sidecar.get('task_id')}  {sidecar.get('credits', 0):g} credits  "
                         f"{'text unchanged' if age else 'TEXT CHANGED — a new reading is due'}")
    else:
        side = read_sidecar(slug, root) if slug else None
        if side:
            lines.append(f"{path.name}: no image fields in the frontmatter, but rev "
                         f"{side.get('revision', 1)} ({side.get('style')}, {side.get('model_key')}) "
                         f"was read from this same text — the image is staged and pushed to the CMS; "
                         f"re-running --apply fills the fields in (no new generation)")
        else:
            history = style_history(ledger_path(root))
            lines.append(f"{path.name}: no illustration"
                         + (f"  [recent treatments: {', '.join(history[:4])}]" if history else ""))
    return lines


def ledger_path(root: pathlib.Path | None = None) -> pathlib.Path:
    return (root / "context" / "illustration_log.md") if root else LEDGER


def main() -> int:
    parser = argparse.ArgumentParser(description=(__doc__ or "").splitlines()[0])
    parser.add_argument("files", nargs="*", help="article markdown files")
    parser.add_argument("--apply", action="store_true", help="commission and generate, then write "
                                                             "the image fields into the artifact")
    parser.add_argument("--backfill", action="store_true", help="every published/draft artifact that "
                                                                "has no illustration yet")
    parser.add_argument("--check", action="store_true", help="exit 1 when an artifact that claims an "
                                                             "illustration has drifted from its sidecar")
    parser.add_argument("--dry-run", action="store_true", help="run the art director and print the "
                                                               "brief; spend no image credits")
    parser.add_argument("--force", action="store_true", help="regenerate even when the text is unchanged")
    parser.add_argument("--style", help=f"pin a treatment ({', '.join(STYLES)})")
    parser.add_argument("--model", help=f"pin a model ({', '.join(sorted(MODELS))})")
    parser.add_argument("--limit", type=int, default=None,
                        help="max artifacts to GENERATE in one run (already-illustrated artifacts "
                             "are examined and skipped for free)")
    parser.add_argument("--root", default=None, help="repo root (default: the script's parent)")
    args = parser.parse_args()

    root = pathlib.Path(args.root).resolve() if args.root else ROOT
    if args.style:
        # An operator's runbook (and the desk's own older notes) still name a retired treatment;
        # resolve it to its replacement rather than refusing a one-word alias.
        args.style = canonical_style_id(args.style)
        if args.style not in STYLES:
            parser.error(f"unknown --style {args.style!r}; one of {', '.join(STYLES)}")

    files = [pathlib.Path(f) for f in args.files]
    if args.backfill:
        for directory in ("published", "context/drafts"):
            files += sorted((root / directory).glob("*.md"))
    if not files:
        parser.error("pass at least one markdown file, or --backfill")

    exit_code = 0
    applied = 0
    for path in files:
        if args.limit is not None and applied >= args.limit:
            break
        md = path.read_text(encoding="utf-8")
        if args.check and not args.apply and not args.dry_run:
            problems = check_artifact(md, root=root)
            if problems and not (len(problems) == 1 and problems[0].startswith("no illustration")):
                print(f"  FAIL {path.name}: {'; '.join(problems)}")
                exit_code = 1
            else:
                print(f"  ok   {path.name}: {'; '.join(problems)}")
            continue
        if args.dry_run:
            brief = direct(md, history=style_history(ledger_path(root)),
                           pinned_style=args.style, pinned_model=args.model)
            print(f"\n  {path.name} -> {brief.style_id} ({brief.style.label}) on {brief.model_id}")
            print(json.dumps(brief.to_dict(), indent=2))
            applied += 1
            continue
        if not args.apply:
            for line in _report(path, root):
                print("  " + line)
            continue
        try:
            new_md, notes, _meta = ensure_illustration(
                md, root=root, force=args.force, pinned_style=args.style, pinned_model=args.model)
            for note in notes:
                print(f"    - {note}")
            slug = slug_from_frontmatter(new_md) or slug_from_frontmatter(md)
            if slug:
                try:
                    import illustration_overlay
                    ov = illustration_overlay.apply_to_slug(slug, article_md=new_md)
                    anchor = ov.get("placement", {}).get("anchor") or ov.get("anchor") or "placed"
                    print(f"    - typography overlay applied ({anchor})")
                    side = read_sidecar(slug, root)
                    if side:
                        new_md = _write_frontmatter(new_md, frontmatter_fields(side))
                except Exception as ov_err:
                    print(f"    - typography overlay note: {ov_err}")
            if new_md != md:
                path.write_text(new_md, encoding="utf-8")
                print(f"  {path.name}: illustration written")
                applied += 1     # --limit bounds GENERATIONS, not files examined: a backfill sweep
                                 # must be able to walk an already-illustrated corpus for free
            else:
                print(f"  {path.name}: unchanged")
        except IllustrationError as exc:
            print(f"  FAIL {path.name}: {exc}", file=sys.stderr)
            exit_code = 1
    return exit_code


if __name__ == "__main__":
    sys.exit(main())

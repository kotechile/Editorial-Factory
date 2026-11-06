#!/usr/bin/env python3
"""Validate a hand-authored brief offline (no credits), then generate on pass."""
import json
import sys

sys.path.insert(0, "/root/editorial-factory/scripts")
import illustration_creator as ic

ART = "published/2026-11-06_your-espp-clock-is-18-months-not-12.md"
md = open(ART).read()

BRIEF = {
    "core_thesis": "The tax break on discounted employer stock arrives on the later of two statutory clocks, so the wait is longer and the prize smaller than the plan summary says.",
    "core_conflict": "Two timing periods, one of which silently binds later than the date everyone quotes.",
    "main_idea": "The qualifying date is the later of two statutory periods, and a plan detail decides when the first one starts.",
    "object_or_scene": "A modular brass timing assembly on a home-office desk, one latch resting against a stop.",
    "style_id": "component_assembly",
    "rationale": "The article is a rule — the later of two clocks — with no scene to photograph, so the frame is a real assembly: a ratchet wheel, a latch and a rail that state a mechanism stopping short of its stop.",
    "cue": "hold a year for the tax break",
    "subject": "A modular brass timing assembly with a ratchet wheel, a hinged latch and a short rack rail on a home-office desk",
    "composition": "asymmetric three-quarter framing, the assembly left of centre with negative space to the right",
    "model": "nanobanana",
    "prompt": "Modular component assembly on a brushed steel plate set on a home-office desk: a brass ratchet wheel, a hinged latch and a short rack rail arranged in one deliberate line, the latch resting open against a stop. Three-quarter view, hard single key light from the upper left, matte brass and graphite steel texture, bone white paper shim under the plate, asymmetric framing with generous negative space to the right.",
    "negative_prompt": "garbled text, random lettering, numbers, watermarks, logos, human hands",
    "aspect_ratio": "16:9",
    "resolution": "1K",
    "alt_text": "A brass ratchet wheel, hinged latch and short rack rail on a steel plate on a home-office desk.",
    "caption": "The later of two statutory periods is the one that sets the date.",
    "title": "Brass ratchet, latch and rail on a desk",
    "credit": "Illustration: Editorial-Factory Intelligence Unit",
    "depicts_real_brand": False,
}

try:
    brief = ic.validate_brief(BRIEF, md, allowed=tuple(ic.STYLES), pinned_style="component_assembly")
    print("VALID:", brief.style_id, brief.model)
except Exception as exc:
    print("INVALID:", exc)
    sys.exit(1)

if "--generate" in sys.argv:
    ic.call_gemini = lambda prompt, **kw: json.dumps(BRIEF)
    sys.argv = ["illustration_creator.py", ART, "--apply", "--style", "component_assembly"]
    ic.main()

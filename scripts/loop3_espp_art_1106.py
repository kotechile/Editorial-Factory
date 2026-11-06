#!/usr/bin/env python3
"""Hand-authored art-direction brief for one artifact (the director's own JSON shape).

Four automatic commissions were refused on rotating validation reasons (light direction, optic,
light again), which under skills/evergreen_topics.md is a retry class rather than a verdict — but
the loop's failure mode is that each attempt satisfies one class and drops another. This driver
submits a brief that satisfies every class at once (optic, light, texture, framing, place, palette,
mechanism, verbatim cue) through the module's own validator, then uses the normal render path.
"""
import json
import sys

sys.path.insert(0, "/root/editorial-factory/scripts")
import illustration_creator as ic  # noqa: E402

BRIEF = {
    "core_thesis": "The tax break on discounted employer stock arrives on the later of two statutory clocks, "
                   "so the wait is longer and the prize smaller than the plan summary says.",
    "core_conflict": "A tax rate the reader can measure against a holding period nobody reads.",
    "main_idea": "The qualifying date depends on when the option was granted, which a plan-document line decides, "
                 "and the paperwork is the only place the grant-date value appears.",
    "object_or_scene": "A household desk with a sealed envelope, a brass fastener and a steel ruler on it.",
    "style_id": "document_flatlay",
    "rationale": "The story turns on documents — a plan summary, a share certificate and the IRS form that carries "
                 "the grant-date value — so a top-down document still life puts the reader's own paperwork in frame "
                 "rather than illustrating an abstract clock.",
    "cue": "hold a year for the tax break",
    "subject": "A sealed manila envelope, a brass paper fastener and a steel ruler on a home-office desk",
    "composition": "asymmetric overhead framing, the certificate off-centre and low in frame",
    "model": "flux",
    "prompt": "Overhead top-down flat-lay photograph on a home-office desk: one sealed manila envelope, a brass "
              "paper fastener and a steel ruler arranged off-centre, everything blank and unprinted. Shot on a 50mm "
              "lens, soft window light from the left, coarse paper fibre and brushed steel texture, sand and charcoal "
              "against warm oak, asymmetric framing with the envelope low in the frame.",
    "negative_prompt": "garbled text, random lettering, numbers, watermarks, logos, human hands",
    "aspect_ratio": "16:9",
    "resolution": "1K",
    "alt_text": "A sealed manila envelope, a brass paper fastener and a steel ruler on a home-office desk.",
    "caption": "The qualifying date and the grant-date value live in paperwork most holders never open.",
    "title": "Sealed envelope, fastener and ruler on a desk",
    "credit": "Illustration: Editorial-Factory Intelligence Unit",
    "depicts_real_brand": False,
}

ic.call_gemini = lambda prompt, **kw: json.dumps(BRIEF)  # noqa: E731
sys.argv = ["illustration_creator.py",
            "published/2026-11-06_your-espp-clock-is-18-months-not-12.md",
            "--apply", "--style", "document_flatlay"]
ic.main()

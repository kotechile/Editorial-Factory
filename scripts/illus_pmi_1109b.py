#!/usr/bin/env python3
"""Second-pass header driver for the 2026-11-09 PMI article.

Two director briefs were generated and the picture desk rejected both: the first because generated
lettering counted as legible text, the second because a blank folder depicts no mortgage mechanism.
This driver keeps the director's treatment (document_flatlay, chosen from its own dry-run) and
rewrites only the scene so it carries the article's own objects — a grey-bar amortization page with
no lettering, a red pencil, two offset brass clips and a house key — then re-validates through the
module's own `validate_brief` and runs the normal generate → review → store path.
"""
import json
import pathlib
import sys

ROOT = pathlib.Path("/root/editorial-factory")
sys.path.insert(0, str(ROOT / "scripts"))
import illustration_creator as ic  # noqa: E402

ART = ROOT / "published" / "2026-11-09_your-pmi-ends-at-78-not-todays-value.md"
md = ART.read_text(encoding="utf-8")

blob = pathlib.Path("/tmp/dry1.json").read_text(encoding="utf-8")
raw = json.loads(blob[blob.index("{"): blob.rindex("}") + 1])

raw["subject"] = ("an open mortgage closing folder holding a blank amortization schedule page, "
                  "a red pencil, two brass paper clips and a house key on a kitchen table")
raw["composition"] = ("asymmetric top-down, the folder off-centre and low in frame, generous negative space")
raw["prompt"] = (
    "Top-down 90-degree flat-lay photograph on a painted timber kitchen table: an open mortgage "
    "closing folder holding a single blank amortization schedule page, a sharpened red pencil lying "
    "across it, two small brass paper clips set at different depths along the page, and a brass house "
    "key resting beside the folder. Soft window light from the left rakes across the paper grain and "
    "casts long contact shadows; palette of bone white, graphite and ochre on matte paper and warm "
    "oak. 35mm lens, shallow depth of field at the page edge, asymmetric composition with the folder "
    "off-centre, generous negative space, no logos."
)
raw["negative_prompt"] = "garbled lettering, random words, watermarks, readable print, logos"
raw["alt_text"] = ("An open mortgage closing folder on a kitchen table with a blank schedule page, "
                   "a red pencil, two brass clips and a house key.")
raw["caption"] = ("The closing folder holds the amortization page where the borrower's request line and the "
                  "automatic stop line sit on different rows.")
raw["model_note"] = ("desk correction after two picture-desk rejections: the director's treatment kept, the "
                     "scene rewritten to carry the article's own objects with no lettering anywhere.")

history = ic.style_history(ic.ledger_path())
allowed = ic.allowed_styles(history)
brief = ic.validate_brief(raw, md, allowed=allowed)
print("validated:", brief.style_id, brief.model_id)

ic.direct = lambda *a, **k: brief
new_md, notes, meta = ic.ensure_illustration(md, force=False)
for n in notes:
    print("·", n)
if new_md != md:
    ART.write_text(new_md, encoding="utf-8")
    print("frontmatter updated:", ART.name)

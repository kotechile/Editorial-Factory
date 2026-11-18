#!/usr/bin/env python3
"""Flat-panel re-type for 2026-11-18 your-fleets-8-3-year-bill.

The house overlay fades its scrim to zero down the block, which on this dense isometric frame left the
hook line (and the second title line) sitting on robot bodies at ~6:1 measured contrast but visually
unreadable. Re-draw the same copy on a FLAT panel with light ink, then hand the file back to
`wp_draft.reimage_by_slug` — the staged bytes stay 2400x1350 progressive JPEG under 400 KB.
"""
import json
import pathlib
import sys

sys.path.insert(0, "scripts")
from PIL import Image, ImageDraw, ImageFont

import illustration_overlay as O

ROOT = pathlib.Path(__file__).resolve().parent.parent
SLUG = "your-fleets-8-3-year-bill"
SIDE = ROOT / f"context/assets/illustrations/{SLUG}/featured.json"

side = json.loads(SIDE.read_text())
copy = {k: side["overlay"][k] for k in ("kicker", "title", "hook")}
copy["hook"] = "Eight times the annual charge, in one year"
base = pathlib.Path(side["local_path"]).parent / "featured.base.jpg"
out = base.parent / "featured.jpg"

base_img = Image.open(base).convert("RGBA")
w, h = base_img.size
pad = int(w * 0.045)

probe = ImageDraw.Draw(base_img)
column = int(w * O.SAFE_W) - pad * 2
kicker_font = O._fit(probe, copy["kicker"], O.FONT_BOLD, int(h * O.KICKER_PT), column)
title_font, title_lines = O._fit_wrapped(probe, copy["title"], O.FONT_BOLD, int(h * O.TITLE_PT), column, 3)
hook_font, hook_lines = O._fit_wrapped(probe, copy["hook"], O.FONT_REG, int(h * O.HOOK_PT), column, 2)

lines = []                                   # (kind, text, font)
lines.append(("kicker", copy["kicker"], kicker_font))
for t in title_lines:
    lines.append(("title", t, title_font))
for t in hook_lines:
    lines.append(("hook", t, hook_font))

widths = {k: max(probe.textlength(t, font=f) for kk, t, f in lines if kk == k) for k in ("kicker", "title", "hook")}
x = pad
y = pad

# block height
heights = []
cursor = y
for kind, text, font in lines:
    step = int(font.size * (1.5 if kind == "title" else 1.45))
    heights.append((kind, text, font, cursor))
    cursor += step
    if kind == "kicker":
        cursor += int(kicker_font.size * 0.25)
block_bottom = cursor
block_w = max(widths.values()) + int(pad * 1.5)

# flat panel: opaque enough to guarantee the type, feathered 14 px on the right and bottom only
panel = Image.new("RGBA", (w, h), (0, 0, 0, 0))
pd = ImageDraw.Draw(panel)
pad_top = int(pad * 0.6)
pad_bottom = int(pad * 0.45)
box = (x - pad_top, y - pad_top, min(w - pad_top, x + block_w + int(pad * 0.5)), min(h - pad_bottom, block_bottom + pad_bottom))
pd.rectangle([box[0], box[1], box[2], box[3]], fill=(28, 31, 36, 178))
out_img = Image.alpha_composite(base_img, panel)
d = ImageDraw.Draw(out_img)
for kind, text, font, ly in heights:
    rgb = {"kicker": (214, 168, 58), "title": (248, 248, 246), "hook": (228, 230, 232)}[kind]
    d.text((x, ly), text, font=font, fill=(*rgb, 255))

final = out_img.convert("RGB")
if final.size != O.DELIVERY_SIZE:
    final = O.ic.delivery.fit_delivery(final, O.DELIVERY_SIZE)[0]
blob, quality = O.ic.delivery.encode(final)
out.write_bytes(blob)
print("wrote", out, len(blob) // 1024, "KB quality", quality, final.size)

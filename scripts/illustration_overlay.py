#!/usr/bin/env python3
"""Composite the desk's editorial typography onto a generated header.

The design is the owner's, worked out by hand in the Antigravity session of 2026-10-09 on one
article (agent-memory-poisoning-write-path): a kicker, a title and a hook set into the upper-left
negative space over a soft corner vignette. It lived in an ad-hoc `python3 -c` PIL call, so the desk
could not reproduce it — this module makes it a step.

The recipe is theirs, with two corrections the sample could not reveal because it happened to be a
dark photograph:
  * the type is placed in the emptiest corner, not always the upper-left — the commission asks for
    negative space but the model does not always obey, and type laid over the subject is unreadable;
  * the ink and the scrim follow the luminance under the text, because a light image swallows light
    type whole (the first article this ran on came back near-invisible on a cream background).

Sizes, colours and anchors:
  kicker    Liberation Sans Bold, 2.9% of height, warm gold (238,196,120) on dark, dark amber on light
  title     Liberation Sans Bold, 8.6% of height, off-white (240,238,233) on dark, dark gray / charcoal (45,49,55) on light
  hook      Liberation Sans Regular, 3.6% of height, soft slate on dark, slate charcoal on light
  scrim     safe box fading out, strength by luminance
  saved     quality 95

The three lines are written for the article, not derived from it (a section label is not the
vertical's own name), so they come from the same director that reads the article — and every line is
measured and shrunk until it fits the safe column, because a line that overflows the frame cannot be
recovered.

The clean generated image is kept beside the composited one as `<stem>.base.<ext>`, so re-running is
idempotent: the overlay always rebuilds from the pristine render, never from its own output.

Usage:
  python3 scripts/illustration_overlay.py --slug <slug>              # copy + composite + sidecar
  python3 scripts/illustration_overlay.py --slug <slug> --dry-run    # print the copy only
"""
from __future__ import annotations

import argparse
import importlib.util
import json
import pathlib
import re
import shutil
import sys

ROOT = pathlib.Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT / "scripts"))

_spec = importlib.util.spec_from_file_location("illustration_creator", ROOT / "scripts/illustration_creator.py")
ic = importlib.util.module_from_spec(_spec)
sys.modules["illustration_creator"] = ic
_spec.loader.exec_module(ic)

FONT_BOLD = "/usr/share/fonts/truetype/liberation/LiberationSans-Bold.ttf"
FONT_REG = "/usr/share/fonts/truetype/liberation/LiberationSans-Regular.ttf"

SAFE_W, SAFE_H = 0.54, 0.50          # the scrim box, as a fraction of the frame
MAX_WIDTH = 1920                     # delivery size; WordPress rescales anything above 2560
SWITCH_MARGIN = 0.90                 # leave the top-left default only if a corner is 10% emptier
KICKER_MAX, TITLE_MAX, HOOK_MAX = 46, 34, 58
KICKER_PT, TITLE_PT, HOOK_PT = 0.029, 0.086, 0.036    # of the frame height
# (kicker, title, hook) rgb, for a dark frame and for a light one. The scrim strength is not a
# constant: it is derived per image by `_choose_ink`, from the pixels under the type.
INK_DARK = ((238, 196, 120), (240, 238, 233), (214, 222, 230))
INK_LIGHT = ((150, 106, 18), (45, 49, 55), (62, 70, 80))

ACRONYMS = {"AI", "ML", "LLM", "LLMS", "KV", "GPU", "GPUS", "CPU", "API", "APIS", "TCO", "ROI",
            "CFO", "CIO", "CTO", "SLA", "SLAS", "SaaS", "IOT", "RAG", "SQL", "ETL", "ERP", "CRM",
            "SMB", "SME", "MCP", "RPC", "JSON", "HTTP", "TLS", "GPU", "IO", "TCU", "EV", "EVS"}

COPY_PROMPT = """You set the cover typography on an industry-analysis editorial header. The \
photograph is already chosen, and it is deliberately conceptual — so the type does the explaining. \
A reader must learn what this article is about from these three lines even if the image is abstract.

Return ONLY a JSON object, no fence, with exactly these keys:
{{"kicker": "a short ALL-CAPS topic label naming the story's subject and beat — the thing the image \
cannot say by itself, e.g. 'LLM HARDWARE  //  MEMORY BOTTLENECK'. 3-6 words, no publication or desk \
name, never the raw vertical id.",
 "title": "the shortest headline that NAMES the story's subject, ALL CAPS, at most {title_max} \
characters, no colon, no subtitle, no full stop — this is the article's subject, not a teaser",
 "hook": "the promise under the headline: one sentence-case fragment of at most {hook_max} \
characters stating the story's stake, no trailing full stop"}}

Hard limits, because the type is set in the image and a long line overflows the frame: kicker <= \
{kicker_max}, title <= {title_max}, hook <= {hook_max} characters. Count them.

HEADLINE: {title}
EXCERPT: {excerpt}
VERTICAL: {vertical}

ARTICLE (read it — the title must name this specific story, not its beat in general):
---
{body}
---"""


def copy_prompt(article_md: str) -> str:
    fm, _ = ic.split_frontmatter(article_md)
    return COPY_PROMPT.format(
        kicker_max=KICKER_MAX, title_max=TITLE_MAX, hook_max=HOOK_MAX,
        title=(fm.get("meta_title") or fm.get("title") or "").strip(),
        excerpt=ic.article_excerpt(article_md), vertical=fm.get("vertical", ""),
        body=ic.article_core_text(article_md)[:2500])


def clean(copy: dict) -> dict:
    """The copy as it will be set: collapsed whitespace, limits enforced by trimming on a word."""
    out: dict[str, str] = {}
    for key, limit in (("kicker", KICKER_MAX), ("title", TITLE_MAX), ("hook", HOOK_MAX)):
        text = re.sub(r"\s+", " ", str(copy.get(key) or "")).strip().strip('"').rstrip(".")
        if key != "hook":
            text = text.upper()
        if len(text) > limit:
            cut = text[:limit]
            text = cut[:cut.rfind(" ")].strip() if " " in cut else cut
        out[key] = text
    return out


def source_spelling(word: str, source: str) -> str | None:
    """The article's own spelling of `word`, when it carries a capital past the first letter.

    The copy comes back uppercased for the header ('SPACEX STAGGERED LOCKUP'), so title-casing it
    mangles every brand and product the piece names ('Spacex', 'Iphone'). The article body is the
    authority on those spellings; a word it does not name is left to the acronym/case rules.
    """
    if not word or not source:
        return None
    for tok in re.findall(r"[A-Za-z][A-Za-z'’]*", source):
        if tok.lower() == word.lower() and any(c.isupper() for c in tok[1:]):
            return tok
    return None


def sentence_case(text: str, source: str = "") -> str:
    """Title Case for a reader-facing alt/caption that does not mangle acronyms ('Ai', 'Llm') or the
    article's own brand spellings ('Spacex' -> 'SpaceX')."""
    words = []
    for i, w in enumerate(str(text or "").split()):
        core = w.strip(".,:;—–-")
        spelled = source_spelling(core, source)
        if spelled:
            w = w.replace(core, spelled)
        elif core.upper() in ACRONYMS:
            w = w.upper()
        elif core.isupper() and len(core) > 1 and "-" in core and max(len(p) for p in core.split("-")) <= 3:
            pass   # an initialism compound the director already set right ('UP-NS') — '.title()'
                   # would render it 'Up-Ns', which is not how the article or the reader names it
        elif core.isupper() and len(core) > 1:
            cased = core.title()
            if "-" in core:           # keep an acronym that is one half of a compound: 'AI-COST'
                cased = "-".join(p.upper() if p.upper() in ACRONYMS else p
                                 for p in cased.split("-"))
            w = w.replace(core, cased)
        elif i and core.islower():
            w = w.capitalize()
        words.append(w)
    out = " ".join(words)
    first = out.strip(".,:;—–-")
    return out[:1].upper() + out[1:] if out and first == first.lower() else out


def write_copy(article_md: str, llm=None) -> dict:
    """The three lines, from the director model. Falls back to the article's own fields."""
    call = llm or (lambda prompt: ic.call_gemini(prompt))
    try:
        return clean(ic.parse_json_object(call(copy_prompt(article_md))))
    except Exception:                               # noqa: BLE001 - never lose the image over copy
        fm, _ = ic.split_frontmatter(article_md)
        title = (fm.get("meta_title") or fm.get("title") or "").strip()
        return clean({"kicker": "", "title": title.split(":")[0],
                      "hook": ic.article_excerpt(article_md)})


def _fit(draw, text: str, path: str, px: int, max_w: int):
    """The largest size at or below `px` at which `text` fits `max_w` — the type column is fixed."""
    from PIL import ImageFont
    size = max(px, 9)
    while size > 8:
        font = ImageFont.truetype(path, size=size)
        if draw.textlength(text, font=font) <= max_w:
            return font
        size -= 1
    return ImageFont.truetype(path, size=8)


def _busiest(img, box) -> float:
    """Edge energy in a region — a proxy for 'is the artwork already there'."""
    from PIL import ImageFilter
    crop = img.crop(box).convert("L").resize((120, 60))
    edges = crop.filter(ImageFilter.FIND_EDGES)
    data = list(edges.getdata())
    return sum(data) / max(len(data), 1) / 255.0


def _region_rgb(img, box) -> tuple:
    crop = img.crop(box).convert("RGB").resize((120, 60))
    data = list(crop.getdata())
    return tuple(sum(ch[i] for ch in data) // len(data) for i in range(3))


def _clutter(img, box) -> float:
    """How uneven the region is (0-1). A busy background under type needs a stronger scrim."""
    crop = img.crop(box).convert("L").resize((120, 60))
    data = [v / 255.0 for v in crop.getdata()]
    mean = sum(data) / max(len(data), 1)
    return (sum((v - mean) ** 2 for v in data) / max(len(data), 1)) ** 0.5 * 2


def _rel_luma(rgb) -> float:
    def ch(c: float) -> float:
        c /= 255.0
        return c / 12.92 if c <= 0.03928 else ((c + 0.055) / 1.055) ** 2.4
    r, g, b = (ch(x) for x in rgb[:3])
    return 0.2126 * r + 0.7152 * g + 0.0722 * b


def _contrast(a, b) -> float:
    """WCAG contrast ratio between two colours."""
    la, lb = _rel_luma(a), _rel_luma(b)
    hi, lo = max(la, lb), min(la, lb)
    return (hi + 0.05) / (lo + 0.05)


def _scrimmed(rgb, tone, alpha):
    """The pixels a scrim of `alpha` leaves behind: the background the type is actually read on."""
    a = max(0, min(255, int(alpha))) / 255.0
    return tuple(int(round(c * (1 - a) + t * a)) for c, t in zip(rgb[:3], tone))


def _binding_rgb(img, box, prefer_light: bool) -> tuple:
    """The pixel the type has to survive: the brightest under it for light ink, the darkest for dark.

    A mean is the wrong statistic — it averages a bright patch under one word with shadow under the
    next, and hands back an ink that fails on the patch. Type must read over the whole block, so the
    binding pixel sets the bar.
    """
    crop = img.crop(box).convert("RGB")
    px = list(crop.getdata())
    px.sort(key=_rel_luma)
    idx = int(len(px) * (0.85 if prefer_light else 0.15))
    return px[max(0, min(idx, len(px) - 1))]


def _choose_ink(img, box) -> tuple:
    """The ink set that contrasts the pixels under the type, and the scrim strength that gets it there.

    Neither 'light ink on a dark frame' nor the mean of a region is enough: the choice is made against
    the brightest and the darkest pixel the block actually covers, the scrim is raised only until the
    target is met, and the target is higher on a cluttered surface, because busy detail under
    flat-colour type is what erases it.
    """
    bright, darkish = _binding_rgb(img, box, True), _binding_rgb(img, box, False)
    light_ink = _contrast(INK_DARK[1], bright) >= _contrast(INK_LIGHT[1], darkish)
    ink = INK_DARK if light_ink else INK_LIGHT
    binding = bright if light_ink else darkish
    tone = (0, 0, 0) if light_ink else (255, 255, 255)
    clutter = _clutter(img, box)
    target = 4.5 + (1.0 if clutter > 0.25 else 0.0)
    scrim, achieved = 210, _contrast(ink[1], _scrimmed(binding, tone, 210))
    for candidate in range(0, 215, 15):
        ratio = _contrast(ink[1], _scrimmed(binding, tone, candidate))
        if ratio >= target:
            scrim, achieved = candidate, ratio
            break
    return ink, tone, scrim, achieved, target, light_ink, binding, clutter


def plan(img, anchor: str | None = None) -> dict:
    """Where the type goes: the emptiest corner. Ink and scrim are settled after the type is laid
    out, against the pixels the block actually covers — see `_choose_ink`.

    `anchor` forces a corner. Only for the case this metric cannot see: sparse line art (a technical
    isometric, a flat-lay on white) scores as an *empty* corner while the strokes the type lands on
    still cut through the letters. The clutter probe cannot separate thin ink from flat background, so
    a collision it cannot feel has to be steered by hand."""
    w, h = img.size
    bw, bh = int(w * SAFE_W), int(h * SAFE_H)
    corners = {"top-left": (0, 0), "top-right": (w - bw, 0),
               "bottom-left": (0, h - bh), "bottom-right": (w - bw, h - bh)}
    order = ["top-left", "top-right", "bottom-left", "bottom-right"]
    busy = {name: _busiest(img, (x, y, x + bw, y + bh)) for name, (x, y) in corners.items()}
    if anchor:
        if anchor not in corners:
            raise ValueError(f"anchor must be one of {order}, got {anchor!r}")
        x, y = corners[anchor]
        return {"anchor": anchor, "x": x, "y": y, "forced": True,
                "busy": {k: round(v, 4) for k, v in busy.items()}}
    # The owner's design anchors top-left, so keep it unless another corner is MEANINGFULLY emptier.
    # The margin is what makes this work: requiring a corner to be half as busy (the first cut) meant
    # the anchor never moved and the automatic placement looked broken.
    emptiest = min(order, key=lambda name: busy[name])
    best = "top-left" if busy["top-left"] <= busy[emptiest] / SWITCH_MARGIN else emptiest
    x, y = corners[best]
    return {"anchor": best, "x": x, "y": y, "busy": {k: round(v, 4) for k, v in busy.items()}}


def _fit_wrapped(draw, text: str, path: str, px: int, max_w: int, max_lines: int = 2):
    """The largest size at or below `px` at which `text` sets in at most `max_lines` — a headline
    that shrinks to stay on one line is not prominent, which is the point of the type being there."""
    from PIL import ImageFont
    words = str(text).split()
    size = max(px, 10)
    while size > 9:
        font = ImageFont.truetype(path, size=size)
        lines, cur = [], ""
        for word in words:
            trial = f"{cur} {word}".strip()
            if draw.textlength(trial, font=font) <= max_w or not cur:
                cur = trial
            else:
                lines.append(cur)
                cur = word
        if cur:
            lines.append(cur)
        if len(lines) <= max_lines and all(draw.textlength(ln, font=font) <= max_w for ln in lines):
            return font, lines
        size -= 1
    font = ImageFont.truetype(path, size=10)
    return font, [text]


def composite(img_path: pathlib.Path, out_path: pathlib.Path, copy: dict,
              anchor: str | None = None) -> dict:
    """Lay the type out, measure the pixels under THAT block, then choose ink and scrim and draw."""
    from PIL import Image, ImageDraw
    base = Image.open(img_path).convert("RGBA")
    w, h = base.size
    p = plan(base, anchor)
    probe = ImageDraw.Draw(base)
    pad = int(w * 0.045)
    x, y = p["x"] + pad, p["y"] + int(h * 0.055)
    column = int(w * SAFE_W) - pad * 2
    blocks = []                                   # (kind, lines, font) in draw order
    if copy.get("kicker"):
        blocks.append(("kicker", [copy["kicker"]],
                       _fit(probe, copy["kicker"], FONT_BOLD, int(h * KICKER_PT), column)))
    f_t, t_lines = _fit_wrapped(probe, copy["title"], FONT_BOLD, int(h * TITLE_PT), column, 2)
    blocks.append(("title", t_lines, f_t))
    if copy.get("hook"):
        blocks.append(("hook", [copy["hook"]],
                       _fit(probe, copy["hook"], FONT_REG, int(h * HOOK_PT), column)))
    # Block extents, so the ink is chosen against the pixels the type really covers — and so a
    # bottom anchor cannot push the last line off the frame.
    spans, cursor = [], 0
    for kind, lines, font in blocks:
        height = int(font.size * (1.45 if kind == "kicker" else 1.18))
        spans.append([kind, lines, font, cursor])
        cursor += height * len(lines) if kind == "title" else height
    total = cursor
    y = max(0, min(y, h - total - int(h * 0.02)))
    spans = [[k, l, f, y + rel] for k, l, f, rel in spans]
    top, cursor = y, y + total
    block_box = (max(0, x - pad // 2), max(0, top - int(h * 0.012)),
                 min(w, x + column + pad // 2), min(h, cursor + int(h * 0.012)))
    mean_rgb = _region_rgb(base, block_box)
    ink, tone, scrim, contrast, target, light_ink, binding, clutter = _choose_ink(base, block_box)

    overlay = Image.new("RGBA", (w, h), (0, 0, 0, 0))
    d = ImageDraw.Draw(overlay)
    bx0, by0, bx1, by1 = block_box
    bw, bh = max(1, bx1 - bx0), max(1, by1 - by0)
    # A feathered panel, not a pasted rectangle: it fades down the block and out at its right edge.
    from PIL import ImageChops
    vert = Image.new("L", (bw, bh), 0)
    vd = ImageDraw.Draw(vert)
    for i in range(bh):
        vd.line([(0, i), (bw, i)], fill=int(scrim * (1.0 - i / bh)))
    horiz = Image.new("L", (bw, bh), 0)
    hd = ImageDraw.Draw(horiz)
    feather = max(1, int(bw * 0.18))
    for j in range(bw):
        hd.line([(j, 0), (j, bh)],
                fill=255 if j < bw - feather else int(255 * (bw - j) / feather))
    panel = Image.new("RGBA", (bw, bh), (*tone, 255))
    panel.putalpha(ImageChops.multiply(vert, horiz))
    overlay.alpha_composite(panel, (bx0, by0))
    d = ImageDraw.Draw(overlay)
    kicker_rgb, title_rgb, hook_rgb = ink
    for kind, lines, font, ly in spans:
        rgb = {"kicker": kicker_rgb, "title": title_rgb, "hook": hook_rgb}[kind]
        alpha = 255 if kind == "title" else 243
        for line in lines:
            d.text((x, ly), line, font=font, fill=(*rgb, alpha))
            ly += int(font.size * 1.18)
    out = Image.alpha_composite(base, overlay).convert("RGB")
    # Delivery size, not render size. Above 2560px WordPress silently rescales the upload (so the
    # CMS can never serve the staged bytes and the desk's own read-back fails) — and a 5MB header is
    # a page-weight problem on its own. The type is drawn first, so everything scales together.
    if out.width > MAX_WIDTH:
        out = out.resize((MAX_WIDTH, round(out.height * MAX_WIDTH / out.width)), Image.LANCZOS)
    if out_path.suffix.lower() in (".jpg", ".jpeg"):
        out.save(out_path, quality=90, optimize=True, progressive=True)
    else:
        out.save(out_path, optimize=True)
    return {**p, "light": light_ink, "ink": ink, "scrim": scrim, "scrim_tone": tone,
            "region_rgb": mean_rgb, "binding_rgb": binding, "clutter": round(clutter, 3),
            "contrast": round(contrast, 2), "target": round(target, 2),
            "title_lines": t_lines, "title_px": f_t.size, "size": out.size}


def base_path(img: pathlib.Path) -> pathlib.Path:
    return img.with_suffix(f".base{img.suffix}")


def apply_to_slug(slug: str, *, article_md: str | None = None, llm=None, dry_run: bool = False,
                  force_copy: dict | None = None, anchor: str | None = None) -> dict:
    """Composite onto the staged header and keep the sidecar's bytes/sha and alt/caption honest."""
    import hashlib
    hits = sorted((ROOT / "published").glob(f"*_{slug}.md")) or \
        sorted((ROOT / "context" / "drafts").glob(f"*_{slug}_final.md"))
    if not article_md:
        if not hits:
            raise FileNotFoundError(f"no artifact for '{slug}'")
        article_md = hits[-1].read_text()
    side_path = ic.sidecar_path(slug, ROOT)
    reuse = None
    if not dry_run and side_path.exists():
        prev = (json.loads(side_path.read_text()).get("overlay") or {})
        if all(prev.get(k) for k in ("kicker", "title", "hook")):
            reuse = {k: prev[k] for k in ("kicker", "title", "hook")}   # keep the copy stable
    copy = force_copy or reuse or write_copy(article_md, llm=llm)
    if dry_run:
        return {"slug": slug, "copy": copy}
    side = json.loads(side_path.read_text())
    img = ROOT / side["local_path"]
    clean_img = base_path(img)
    # Is the staged image a NEW render, or the copy this step already composited? The base must be
    # refreshed when the render changed, or a regeneration is silently discarded and the type lands
    # on the previous artwork. `generated_at` is the creator's stamp for the render itself.
    prev = side.get("overlay") or {}
    regenerated = prev.get("generated_at") != side.get("generated_at")
    if regenerated or not clean_img.exists():
        for stale in img.parent.glob(f"{img.stem}.base.*"):    # a regeneration may change the suffix
            stale.unlink()
        shutil.copy2(img, clean_img)
    placement = composite(clean_img, img, copy, anchor)
    blob = img.read_bytes()
    side.setdefault("history", []).append(
        {k: side.get(k) for k in ("revision", "alt_text", "caption", "title", "bytes", "sha256")})
    side["revision"] = int(side.get("revision") or 1) + 1
    side["bytes"] = len(blob)
    side["sha256"] = "sha256:" + hashlib.sha256(blob).hexdigest()
    side["overlay"] = {**copy, **{k: placement[k] for k in
                                   ("anchor", "light", "scrim", "contrast", "target", "clutter",
                                    "region_rgb", "binding_rgb", "title_lines")},
                       "generated_at": side["generated_at"]}
    head = sentence_case(copy["title"], article_md if isinstance(article_md, str) else "")
    raw_alt = side.get("alt_text", "")
    prev_head, sep, rest = raw_alt.partition(". ")
    if rest and prev_head.strip().lower() == head.strip().lower():
        raw_alt = rest.strip()          # the alt already carries a head (possibly cased differently)
    side["alt_text"] = f"{head}. {raw_alt}"[:125]
    side["caption"] = (f"{head}: {copy['hook']}." if copy.get("hook") else head + ".")[:200]
    side["title"] = head[:100]
    side_path.write_text(json.dumps(side, indent=2) + "\n")
    for art in hits:
        art.write_text(ic._write_frontmatter(art.read_text(), ic.frontmatter_fields(side)))
    return {"slug": slug, "copy": copy, "placement": placement,
            "bytes": len(blob), "revision": side["revision"], "local_path": side["local_path"],
            "base": str(clean_img.relative_to(ROOT))}


def main() -> int:
    ap = argparse.ArgumentParser(description="Composite the desk's cover typography onto a header.")
    ap.add_argument("--slug", required=True)
    ap.add_argument("--anchor", choices=["top-left", "top-right", "bottom-left", "bottom-right"],
                    help="Force the type block into this corner. Use only when the automatic pick "
                         "lands the type on sparse line art it reads as empty (the collision shows up "
                         "in the composite, not in the clutter score)")
    ap.add_argument("--dry-run", action="store_true", help="print the copy, touch nothing")
    args = ap.parse_args()
    print(json.dumps(apply_to_slug(args.slug, dry_run=args.dry_run, anchor=args.anchor),
                     indent=2, default=str))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

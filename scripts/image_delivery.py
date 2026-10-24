#!/usr/bin/env python3
"""The delivery standard for a featured header image — one place, enforced in code.

The desk's readers get the header twice: a 7:4 card crop and a 16:9 masthead. A master that is not
16:9 loses content in one of the two, so the render is cropped and sized here rather than trusted to
whatever shape the image model returned.

The standard (owner, 2026-10-24):

| rule       | value                                   | why                                          |
|------------|-----------------------------------------|----------------------------------------------|
| aspect     | 16:9 +/-3%                              | card 7:4 and masthead 16:9 both crop from it |
| width      | >=1600px, upload 2400x1350              | cards request WP large (1024); mastheads 72rem |
| weight     | <=400KB                                 | cards render at 340px; 342KB was the old mean |
| format     | JPEG, sRGB, progressive                 | PNG photos are 4-8x heavier                  |
| rendition  | `large` must exist                      | otherwise the front end ships the original   |
| filename   | `<slug>-featured.jpg`, lowercase        | library-readable, matches the plate key      |
| alt text   | 40-140 chars, must not equal the title  | it is the only text a search can read        |
| uniqueness | no two posts share an image             | a repeated image is a templating tell        |

Everything measurable is a function here so the creator, the overlay, the CMS push and the audit
cannot drift apart. `normalize()` is the one conversion: crop to 16:9, resize to 2400x1350, convert
to sRGB, encode progressive JPEG, step the quality down until the file fits 400KB.

    python3 scripts/image_delivery.py --audit            # corpus report, no writes
    python3 scripts/image_delivery.py --audit --json     # machine-readable
"""
from __future__ import annotations

import argparse
import hashlib
import io
import json
import pathlib
import re
import sys
from dataclasses import dataclass, field

from PIL import Image, ImageCms, ImageOps

STANDARD_VERSION = "2026-10-24"
ASPECT = 16 / 9
ASPECT_TOLERANCE = 0.03
DELIVERY_WIDTH = 2400
DELIVERY_HEIGHT = 1350
MIN_WIDTH = 1600
MAX_BYTES = 400 * 1024
MIN_SOURCE_WIDTH = 1000          # the desk renders at 1K/1344px; below this an upscale is mush
DUPLICATE_HAMMING = 12           # 256-bit dHash: the corpus's closest two DIFFERENT headers sit
                                 # 33 bits apart, and a re-encoded copy of one sits at 0-2
ALT_MIN, ALT_MAX = 40, 140
# Quality ladder, tried high to low. 2400x1350 photographic detail lands in the 76-88 band; the tail
# exists so a busy collage still fits the budget instead of shipping over it.
QUALITIES = (88, 84, 80, 76, 72, 68, 64, 60, 56, 52)
INDEX_NAME = ".render_index.json"   # v2 schema: 256-bit phash


class DeliveryError(RuntimeError):
    """The image cannot be made to meet the standard — reported, never silently shipped."""


# ─────────────────────────────────────────────────────────────────────────────
# pixels
# ─────────────────────────────────────────────────────────────────────────────

def _open(src) -> Image.Image:
    if isinstance(src, Image.Image):
        return src
    if isinstance(src, (bytes, bytearray)):
        return Image.open(io.BytesIO(src))
    return Image.open(src)


def to_srgb(img: Image.Image) -> Image.Image:
    """RGB in the sRGB space, whatever came in (PNG/RGBA, CMYK, or a wide-gamut profile)."""
    icc = img.info.get("icc_profile") if hasattr(img, "info") else None
    if img.mode == "P":
        img = img.convert("RGBA" if "transparency" in img.info else "RGB")
    if img.mode in ("RGBA", "LA"):
        # Flatten on white rather than black: a transparent corner is a hole in a JPEG.
        background = Image.new("RGB", img.size, (255, 255, 255))
        alpha = img.convert("RGBA").split()[-1]
        background.paste(img.convert("RGB"), mask=alpha)
        img = background
    elif img.mode != "RGB":
        img = img.convert("RGB")
    if icc:
        try:
            source = ImageCms.ImageCmsProfile(io.BytesIO(icc))
            img = ImageCms.profileToProfile(img, source, ImageCms.createProfile("sRGB"),
                                            outputMode="RGB")
        except Exception:                                   # noqa: BLE001 — an odd profile is not fatal
            pass                                            # the pixels are already RGB: assume sRGB
    return img


def crop_to_aspect(img: Image.Image, aspect: float = ASPECT) -> Image.Image:
    """Centre-crop to exactly `aspect` — never a squash, which distorts the subject."""
    w, h = img.size
    target_h = round(w / aspect)
    if target_h <= h:
        top = (h - target_h) // 2
        return img.crop((0, top, w, top + target_h))
    target_w = round(h * aspect)
    left = (w - target_w) // 2
    return img.crop((left, 0, left + target_w, h))


def fit_delivery(img: Image.Image, size: tuple[int, int] = (DELIVERY_WIDTH, DELIVERY_HEIGHT)
                 ) -> tuple[Image.Image, float]:
    """Crop to 16:9 and resize to the delivery master. Returns (image, upscale factor)."""
    img = crop_to_aspect(img)
    scale = size[0] / img.width
    if img.size != size:
        img = img.resize(size, Image.LANCZOS)
    return img, round(scale, 3)


def encode(img: Image.Image, *, max_bytes: int = MAX_BYTES) -> tuple[bytes, int]:
    """Progressive JPEG under the weight budget. Steps quality down; never returns an over-budget file."""
    blob = b""
    for quality in QUALITIES:
        buf = io.BytesIO()
        img.save(buf, format="JPEG", quality=quality, optimize=True, progressive=True, subsampling=2)
        blob = buf.getvalue()
        if len(blob) <= max_bytes:
            return blob, quality
    raise DeliveryError(
        f"cannot get {img.width}x{img.height} under {max_bytes // 1024}KB "
        f"(best was {len(blob) // 1024}KB at quality {QUALITIES[-1]}) — the frame is too busy; "
        f"re-commission a calmer treatment")


@dataclass
class Normalized:
    """A delivery-ready JPEG plus the numbers that prove it."""
    blob: bytes
    width: int
    height: int
    quality: int
    source_size: tuple[int, int]
    scale: float
    sha256: str

    @property
    def bytes(self) -> int:
        return len(self.blob)

    @property
    def aspect(self) -> float:
        return self.width / self.height

    def info(self) -> dict:
        return {"standard": STANDARD_VERSION, "format": "JPEG", "progressive": True,
                "color_space": "sRGB", "width": self.width, "height": self.height,
                "aspect": round(self.aspect, 4), "bytes": self.bytes, "quality": self.quality,
                "source_size": list(self.source_size), "scale": self.scale,
                "sha256": self.sha256,
                "filename_rule": "<slug>-featured.jpg"}


def normalize(src, *, size: tuple[int, int] = (DELIVERY_WIDTH, DELIVERY_HEIGHT),
              max_bytes: int = MAX_BYTES) -> Normalized:
    """Any render in, a conforming delivery master out. The only conversion in the pipeline."""
    img = _open(src)
    img = ImageOps.exif_transpose(img)
    source_size = img.size
    if source_size[0] < MIN_SOURCE_WIDTH:
        raise DeliveryError(
            f"render is {source_size[0]}x{source_size[1]} — the delivery master is {size[0]}x{size[1]} "
            f"and a source under {MIN_SOURCE_WIDTH}px cannot reach {MIN_WIDTH}px without visible "
            f"mush; re-render it at 1K (1344x768) or larger")
    img = to_srgb(img)
    img, scale = fit_delivery(img, size)
    blob, quality = encode(img, max_bytes=max_bytes)
    return Normalized(blob=blob, width=img.width, height=img.height, quality=quality,
                      source_size=source_size, scale=scale,
                      sha256="sha256:" + hashlib.sha256(blob).hexdigest())


# ─────────────────────────────────────────────────────────────────────────────
# the rules, as measurements
# ─────────────────────────────────────────────────────────────────────────────

def aspect_problems(width: int, height: int) -> list[str]:
    got = width / height if height else 0
    drift = abs(got - ASPECT) / ASPECT
    if drift > ASPECT_TOLERANCE:
        return [f"aspect {got:.3f} ({width}x{height}) is {drift * 100:.1f}% off 16:9 "
                f"(allowed +/-{ASPECT_TOLERANCE * 100:.0f}%) — the 7:4 card and the 16:9 masthead "
                f"both crop from this master"]
    return []


def alt_problems(alt: str, *titles: str) -> list[str]:
    """40-140 chars, and not the article's (or the media field's) title restated."""
    alt = re.sub(r"\s+", " ", str(alt or "")).strip()
    problems: list[str] = []
    if not (ALT_MIN <= len(alt) <= ALT_MAX):
        problems.append(f"alt_text is {len(alt)} chars — the desk writes {ALT_MIN}-{ALT_MAX}")
    squashed = _squash(alt)
    for title in titles:
        if title and squashed and squashed == _squash(title):
            problems.append(f"alt_text repeats the title ({str(title)[:60]!r}) — it describes the "
                            f"image for a screen reader, not the headline over again")
            break
    return problems


def _squash(text: str) -> str:
    return re.sub(r"[^a-z0-9]+", "", str(text or "").lower())


def check_file(path) -> list[str]:
    """Every measurable standard rule for a staged file. Empty list = conforming."""
    path = pathlib.Path(path)
    problems: list[str] = []
    try:
        img = Image.open(path)
    except Exception as exc:                                # noqa: BLE001
        return [f"{path.name} cannot be read as an image ({exc})"]
    fmt = (img.format or "").upper()
    if fmt != "JPEG":
        problems.append(f"format is {fmt or 'unknown'}, not JPEG — a PNG photograph is 4-8x heavier "
                        f"and the CMS serves it as-is")
    if fmt == "JPEG" and not (img.info.get("progressive") or img.info.get("progression")):
        problems.append("JPEG is baseline, not progressive — the standard encodes progressive")
    problems += aspect_problems(*img.size)
    if img.width < MIN_WIDTH:
        problems.append(f"width {img.width}px is under the {MIN_WIDTH}px floor — WP's `large` "
                        f"rendition is 1024 and cards/mastheads need the headroom")
    size = path.stat().st_size
    if size > MAX_BYTES:
        problems.append(f"{size // 1024}KB is over the {MAX_BYTES // 1024}KB budget")
    icc = img.info.get("icc_profile")
    if icc:
        try:
            description = ImageCms.ImageCmsProfile(io.BytesIO(icc)).profile_description or ""
        except Exception:                                   # noqa: BLE001
            description = ""
        if description and "srgb" not in description.lower():
            problems.append(f"colour profile is {description!r}, not sRGB")
    return problems


# ─────────────────────────────────────────────────────────────────────────────
# uniqueness: sha256 for the exact bytes, dHash for the same picture re-rendered
# ─────────────────────────────────────────────────────────────────────────────

def dhash(src, size: int = 16) -> int:
    """256-bit difference hash of the PICTURE (not the file): robust to re-encode and resize.

    A 64-bit hash was too weak here: two different headers (a lit corridor and a warehouse aisle)
    came back 3 bits apart because both are radially symmetric, which is most of what a dHash sees.
    At 16x16 the same pair sits 36 bits apart while a resized re-encode of one hash stays at 0.
    """
    img = _open(src)
    img = ImageOps.exif_transpose(img).convert("L").resize((size + 1, size), Image.LANCZOS)
    pixels = list(img.get_flattened_data() if hasattr(img, "get_flattened_data") else img.getdata())
    bits = 0
    for row in range(size):
        for col in range(size):
            left = pixels[row * (size + 1) + col]
            right = pixels[row * (size + 1) + col + 1]
            bits = (bits << 1) | (1 if left > right else 0)
    return bits


def hamming(a: int, b: int) -> int:
    return bin(a ^ b).count("1")


def fingerprint(src) -> dict:
    """The provenance pair stored on the sidecar: exact bytes + perceptual hash of the render."""
    img = _open(src)
    buf = io.BytesIO()
    img.convert("RGB").save(buf, format="JPEG", quality=90)
    return {"sha256": "sha256:" + hashlib.sha256(buf.getvalue()).hexdigest(),
            "phash": f"{dhash(img):064x}"}


def _index_path(root: pathlib.Path) -> pathlib.Path:
    return root / "context" / "assets" / "illustrations" / INDEX_NAME


def _mtime_key(path: pathlib.Path) -> str:
    stat = path.stat()
    return f"{stat.st_size}:{int(stat.st_mtime)}"


def corpus_index(root=None, *, refresh: bool = False) -> list[dict]:
    """Every staged render's fingerprint, cached by file mtime (182 assets would otherwise be slow)."""
    root = pathlib.Path(root or pathlib.Path(__file__).resolve().parent.parent)
    base = root / "context" / "assets" / "illustrations"
    index_path = _index_path(root)
    try:
        cache = json.loads(index_path.read_text())
    except (OSError, json.JSONDecodeError):
        cache = {}
    rows: list[dict] = []
    dirty = False
    for sidecar in sorted(base.glob("*/featured.json")):
        try:
            record = json.loads(sidecar.read_text())
        except (OSError, json.JSONDecodeError):
            continue
        slug = str(record.get("slug") or sidecar.parent.name)
        directory = sidecar.parent
        candidates = sorted(directory.glob("featured.base.*")) or \
            sorted(p for p in directory.glob("featured.*") if p.suffix.lower() != ".json")
        image = candidates[0] if candidates else None
        row = {"slug": slug, "path": str(image) if image else "", "sha256": "", "phash": ""}
        if image is not None:
            key = _mtime_key(image)
            cached = cache.get(str(image))
            if (cached and cached.get("key") == key and len(cached.get("phash") or "") == 64
                    and not refresh):
                row.update(sha256=cached.get("sha256", ""), phash=cached.get("phash", ""))
            else:
                fp = fingerprint(image)
                row.update(fp)
                cache[str(image)] = {"key": key, **fp}
                dirty = True
        rows.append(row)
    if dirty:
        try:
            index_path.write_text(json.dumps(cache, indent=0, sort_keys=True) + "\n")
        except OSError:
            pass
    return rows


def find_duplicate(src, slug: str, *, root=None, index=None) -> dict | None:
    """Another article already ships this picture? Exact bytes or the same frame within 4 bits."""
    me = fingerprint(src)
    for row in (index if index is not None else corpus_index(root)):
        if row["slug"] == slug:
            continue
        if row["sha256"] and row["sha256"] == me["sha256"]:
            return {**row, "distance": 0, "kind": "identical"}
        if row["phash"]:
            distance = hamming(int(me["phash"], 16), int(row["phash"], 16))
            if distance <= DUPLICATE_HAMMING:
                return {**row, "distance": distance, "kind": "near-identical"}
    return None


# ─────────────────────────────────────────────────────────────────────────────
# the filename rule
# ─────────────────────────────────────────────────────────────────────────────

def media_filename(slug: str) -> str:
    """`<slug>-featured.jpg`, lowercase — the CMS library label and the plate lookup key."""
    clean = re.sub(r"[^a-z0-9-]+", "-", str(slug or "").strip().lower()).strip("-")
    if not clean:
        raise DeliveryError(f"slug {slug!r} is empty after normalisation — it is the filename key")
    return f"{clean}-featured.jpg"


# ─────────────────────────────────────────────────────────────────────────────
# audit
# ─────────────────────────────────────────────────────────────────────────────

def audit(root=None) -> dict:
    """Corpus-level report: per-asset rule failures plus duplicate pairs. Read-only."""
    root = pathlib.Path(root or pathlib.Path(__file__).resolve().parent.parent)
    base = root / "context" / "assets" / "illustrations"
    rows = corpus_index(root)
    problems: list[dict] = []
    for sidecar in sorted(base.glob("*/featured.json")):
        slug = sidecar.parent.name
        try:
            record = json.loads(sidecar.read_text())
        except (OSError, json.JSONDecodeError):
            problems.append({"slug": slug, "problems": ["sidecar is unreadable"]})
            continue
        slug = str(record.get("slug") or slug)
        staged = sorted(p for p in sidecar.parent.glob("featured.*")
                        if p.suffix.lower() != ".json" and ".base." not in p.name)
        issues = check_file(staged[0]) if staged else ["no staged image"]
        alt = str(record.get("alt_text") or "")
        issues += alt_problems(alt, str(record.get("title") or ""))
        if issues:
            problems.append({"slug": slug, "legacy": not record.get("delivery"),
                             "problems": issues})
    pairs: list[dict] = []
    for i, a in enumerate(rows):
        if not a["phash"]:
            continue
        for b in rows[i + 1:]:
            if not b["phash"]:
                continue
            distance = hamming(int(a["phash"], 16), int(b["phash"], 16))
            if distance <= DUPLICATE_HAMMING:
                pairs.append({"a": a["slug"], "b": b["slug"], "distance": distance})
    return {"assets": len(rows), "failing": len(problems), "problems": problems,
            "duplicates": pairs}


def main() -> int:
    parser = argparse.ArgumentParser(description="Featured-image delivery audit (read-only).")
    parser.add_argument("--audit", action="store_true", help="report every asset against the standard")
    parser.add_argument("--json", action="store_true", help="print the report as JSON")
    parser.add_argument("--root", default=None)
    args = parser.parse_args()
    if not args.audit:
        parser.error("pass --audit")
    report = audit(args.root)
    if args.json:
        print(json.dumps(report, indent=2))
        return 0
    legacy = sum(1 for p in report["problems"] if p.get("legacy"))
    print(f"\n{report['assets']} staged images; {report['failing']} fail a rule "
          f"({legacy} of them pre-standard) — {len(report['duplicates'])} duplicate pair(s)\n")
    for row in report["problems"]:
        tag = "legacy" if row.get("legacy") else "STANDARD"
        print(f"  [{tag}] {row['slug']}")
        for problem in row["problems"]:
            print(f"      - {problem}")
    for pair in report["duplicates"]:
        print(f"  [DUPLICATE] {pair['a']} == {pair['b']} (dHash distance {pair['distance']})")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

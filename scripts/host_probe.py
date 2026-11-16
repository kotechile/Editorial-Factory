#!/usr/bin/env python3
"""The host ledger: what past runs proved about a host BEFORE you spend a fetch on it.

`skills/references/evergreen_casebook.md` (originally `skills/evergreen_topics.md`) accumulated 63
"Hosts probed live …" paragraphs — the most useful operational knowledge the desk owns, and the least
retrievable: a free-text paragraph the agent re-reads in full, every run. This script turns those
paragraphs into rows, so the question "will `bls.gov` carry a row?" has an answer in one line.

    python3 scripts/host_probe.py --rebuild                 # parse the casebook into the ledger
    python3 scripts/host_probe.py --check https://bls.gov/ooh/   # before you probe
    python3 scripts/host_probe.py --vertical resilient_home_assets --fetchable
    python3 scripts/host_probe.py --selftest                # wired into verify.sh

Verdicts are the ones the paragraphs use: `fetchable` (the figure is plain text and arrives first
try), `unreachable` (403/404/bot wall/SSL, or a stub too small to carry a figure), `no_figures`
(fetches, but the number is client-side JavaScript or absent), `partial` (fetches, cannot carry the
row you want). A verdict is a dated observation, not a law: re-probe a `fetchable` host freely, and
treat an old `unreachable` as "expect to waste a fetch", not "never try".
"""
from __future__ import annotations

import argparse
import json
import pathlib
import re
import sys
import urllib.parse

ROOT = pathlib.Path(__file__).resolve().parent.parent
LEDGER = ROOT / "context" / "knowledge" / "host_probes.json"
SOURCES = (
    ROOT / "skills" / "references" / "evergreen_casebook.md",
    ROOT / "skills" / "evergreen_topics.md",
)

PARA_START = re.compile(r"^\*\*Hosts probed live", re.M)
DATE = re.compile(r"(20\d\d-\d\d-\d\d)")
VERTICAL = re.compile(r"`([a-z][a-z0-9_]{3,})`\s+evergreen")
HOST_TOKEN = re.compile(r"`((?:https?://)?[a-z0-9][a-z0-9.\-]*\.[a-z]{2,}(?:/[^`\s]*)?)`")

# Segment markers, in the order the paragraphs use them. The verdict is read off the segment a
# host first appears in, so ordering matters: a host named under "Fails" is an unreachable one.
SEGMENTS = (
    ("unreachable", ("Fails or cannot carry", "Unreachable to the verifier", "Also unreachable",
                     "Fails or is unneeded", "Fails, or is unneeded", "Unreachable:",
                     "Guessing", "Fails:")),
    ("no_figures", ("Fetches but cannot carry", "Fetches and cannot carry",
                    "fetches but print no prices", "carry no numeric")),
    ("fetchable", ("Carries the figure", "carries the figure", "Works, with the", "Also fetching:",
                   "and it fetches", "Both fetch")),
)


def _host(token: str) -> str:
    token = token.strip()
    if "://" in token:
        token = urllib.parse.urlsplit(token).netloc
    else:
        token = token.split("/")[0]
    return token.lower().lstrip(".")


# Filenames and bare words in backticks look like hosts to a regex ('featured.base.jpg'). A real
# host has a plausible TLD, and no asset extension in its last label.
ASSET_EXT = (".jpg", ".jpeg", ".png", ".webp", ".gif", ".svg", ".json", ".md", ".py", ".sh")
TLD = re.compile(r"\.(com|org|net|gov|edu|io|ai|us|uk|ca|de|fr|au|nz|info|co|law|house|energy)$|"
                 r"\.(gov|edu|org|com)\.[a-z]{2}$")


def _is_host(host: str) -> bool:
    if not host or "." not in host or len(host) > 80:
        return False
    if host.endswith(ASSET_EXT):
        return False
    return bool(TLD.search(host))


def _segments(para: str) -> list[tuple[str, str]]:
    """Split a paragraph at the verdict markers into [(verdict, text), …], in document order."""
    cuts: list[tuple[int, str]] = []
    for verdict, markers in SEGMENTS:
        for m in markers:
            for found in re.finditer(re.escape(m), para):
                cuts.append((found.start(), verdict))
    cuts.sort()
    if not cuts:
        return [("mentioned", para)]
    out: list[tuple[str, str]] = []
    if cuts[0][0] > 0:
        out.append(("mentioned", para[:cuts[0][0]]))
    for i, (pos, verdict) in enumerate(cuts):
        end = cuts[i + 1][0] if i + 1 < len(cuts) else len(para)
        out.append((verdict, para[pos:end]))
    return out


def parse(text: str) -> list[dict]:
    rows: list[dict] = []
    starts = [m.start() for m in PARA_START.finditer(text)]
    for pos in starts:
        # One "Hosts probed live" paragraph, not the whole stretch until the next one: everything
        # between two such markers used to be swallowed into the first row's paragraph, which is how
        # unrelated case law (and its dates) leaked into a host's verdict.
        stop = text.find("\n\n", pos)
        para = " ".join(text[pos:stop if stop != -1 else len(text)].split())
        dm = DATE.search(para)
        date = dm.group(1) if dm else ""
        vm = VERTICAL.search(para)
        vertical = vm.group(1) if vm else ""
        seen: set[tuple[str, str]] = set()
        for verdict, segment in _segments(para):
            for token in HOST_TOKEN.findall(segment):
                host = _host(token)
                if not _is_host(host):
                    continue
                if (host, verdict) in seen:
                    continue
                seen.add((host, verdict))
                said = para[max(0, para.find(host) - 70):para.find(host) + 120].strip()
                rows.append({
                    "host": host,
                    "url": token if "://" in token else "",
                    "verdict": verdict,
                    "as_of": date,
                    "vertical": vertical,
                    "note": said[:220],
                })
    return rows


def rebuild(sources=SOURCES) -> list[dict]:
    text = ""
    for src in sources:
        if src.exists():
            text = src.read_text(encoding="utf-8", errors="ignore")
            break
    if not text:
        raise SystemExit(f"no casebook found (looked in {', '.join(str(s) for s in sources)})")
    rows = parse(text)
    # newest observation wins per (host, verdict); keep both if the verdict changed over time
    best: dict[tuple[str, str], dict] = {}
    for row in rows:
        key = (row["host"], row["verdict"])
        if key not in best or (row["as_of"] or "") >= (best[key]["as_of"] or ""):
            best[key] = row
    out = sorted(best.values(), key=lambda r: (r["host"], r["verdict"]))
    LEDGER.parent.mkdir(parents=True, exist_ok=True)
    LEDGER.write_text(json.dumps(out, indent=1) + "\n", encoding="utf-8")
    return out


def load() -> list[dict]:
    if not LEDGER.exists():
        return []
    try:
        return json.loads(LEDGER.read_text(encoding="utf-8"))
    except ValueError:
        return []


VERDICT_RANK = {"unreachable": 0, "no_figures": 1, "partial": 2, "mentioned": 3, "fetchable": 4}


def check(url: str) -> int:
    host = _host(url)
    rows = [r for r in load() if r["host"] == host or host.endswith("." + r["host"])
            or r["host"].endswith("." + host)]
    if not rows:
        print(f"{host}: no prior probe on record — probe it, then record the result with "
              f"`scripts/learn.py --kind host`.")
        return 0
    # The NEWEST observation is the answer; an older 'unreachable' may have been fixed since (a host
    # that 403s one month can serve plain text the next). History is printed underneath so a stale
    # verdict is visible rather than trusted.
    newest = max(rows, key=lambda r: ((r["as_of"] or ""), -VERDICT_RANK.get(r["verdict"], 3)))
    print(f"{host}: {newest['verdict']} as of {newest['as_of'] or 'n/a'}"
          + (f" ({newest['vertical']})" if newest["vertical"] else ""))
    for r in sorted(rows, key=lambda r: r["as_of"] or ""):
        print(f"  - {r['as_of'] or 'n/a':10s} {r['verdict']:12s} {r['note'][:150]}")
    return 0 if newest["verdict"] == "fetchable" else 1


def by_vertical(vertical: str, verdict: str | None) -> int:
    rows = [r for r in load() if r["vertical"] == vertical and (not verdict or r["verdict"] == verdict)]
    if not rows:
        print(f"no {verdict or 'recorded'} hosts for {vertical}")
        return 1
    for r in sorted(rows, key=lambda r: r["host"]):
        print(f"{r['host']:38s} {r['verdict']:12s} {r['as_of']}")
    return 0


def selftest() -> int:
    rows = load()
    if len(rows) < 80:
        print(f"FAIL: host ledger has {len(rows)} rows (expected >= 80); run --rebuild")
        return 1
    if not any(r["host"] == "bls.gov" and r["verdict"] == "unreachable" for r in rows):
        print("FAIL: bls.gov is not recorded as unreachable — the parser is dropping the "
              "'Fails or cannot carry a row' segments")
        return 1
    if not any(r["verdict"] == "fetchable" for r in rows):
        print("FAIL: no fetchable host recorded — the parser is dropping the 'Carries the figure' segments")
        return 1
    print(f"ok: {len(rows)} rows, {len({r['host'] for r in rows})} hosts")
    return 0


def main() -> int:
    ap = argparse.ArgumentParser(description="Host ledger: past probe results, one line each")
    ap.add_argument("--rebuild", action="store_true")
    ap.add_argument("--from", dest="source", default="",
                    help="markdown file holding the 'Hosts probed live' paragraphs")
    ap.add_argument("--check", default="")
    ap.add_argument("--vertical", default="")
    ap.add_argument("--fetchable", action="store_true")
    ap.add_argument("--unreachable", action="store_true")
    ap.add_argument("--selftest", action="store_true")
    args = ap.parse_args()
    if args.rebuild:
        srcs = (pathlib.Path(args.source),) if args.source else SOURCES
        rows = rebuild(srcs)
        print(f"wrote {LEDGER.relative_to(ROOT)}: {len(rows)} rows, "
              f"{len({r['host'] for r in rows})} hosts")
        return 0
    if args.selftest:
        return selftest()
    if args.check:
        return check(args.check)
    if args.vertical:
        verdict = "fetchable" if args.fetchable else ("unreachable" if args.unreachable else None)
        return by_vertical(args.vertical, verdict)
    ap.print_help()
    return 2


if __name__ == "__main__":
    sys.exit(main())

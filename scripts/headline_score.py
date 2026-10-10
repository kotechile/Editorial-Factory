#!/usr/bin/env python3
"""Headline craft, scored: the desk's title rules, mechanically.

The owner's title standard (2026-10-10), in the order the rules bite:

  1. length & scannability   — core headline <= 6 words, whole title <= 10, <= 60 chars for SEO;
                               never open on 'The/A/An'
  2. psychological triggers  — a curiosity gap (a delta the reader must close) and/or loss aversion
                               (the mistake, the trap, the silent cost), or a counter-intuitive
                               inversion of the conventional wisdom
  3. specificity             — a precise figure from the article's own evidence set, and an explicit
                               target ('Your…', 'CFOs…', 'Shippers…')
  4. honesty                 — no bait-and-switch: the title's promise must be satisfied by the
                               article (the check is mechanical: its content words must exist in the
                               body, so a title can never promise something the piece never says)

Why a scorer instead of prose guidance: the section headers already obey a hard wording rule (0 of
496 across the corpus exceed six words) because it is explicit and checked. Titles had no standard
and no check, so 34 of 70 open on a filler article and the median title is 11 words. This is the
missing check — deterministic, no LLM, so the drafting stage, the Loop 3 rewrite and the publish
gate all measure the same thing.

CLI:
    python3 scripts/headline_score.py "Your EV Is Now a Home Battery"
    python3 scripts/headline_score.py --slug <slug>          # score an artifact's title
    python3 scripts/headline_score.py --all                  # audit the corpus
    python3 scripts/headline_score.py --json ...
"""
from __future__ import annotations

import argparse
import json
import pathlib
import re
import sys

ROOT = pathlib.Path(__file__).resolve().parent.parent

# Grandfathering, exactly as the voice gate does it (check_social_voice.mjs VOICE_ENFORCED_FROM):
# the standard governs articles published from this date on. The 70 headlines that predate it are
# scored and reported, never rewritten or held — retro-fitting live headlines is the owner's call,
# not the machine's (owner decision, 2026-10-10: "make these changes for future articles only").
ENFORCED_FROM = "2026-10-10"


def enforced(date: str) -> bool:
    """Is this artifact's date inside the standard? Unknown dates count as enforced."""
    return not date or date >= ENFORCED_FROM

# Rule 1 — length and scannability.
CORE_WORDS_MAX = 6            # the core headline, before any colon/dash subtitle
TOTAL_WORDS_MAX = 10          # hard ceiling for the whole title
SEO_CHARS_MAX = 60            # search-result truncation
HARD_CHARS_MAX = 75           # social/lock-screen truncation
LEAD_STOPWORDS = {"the", "a", "an"}

# Rule "omit fluff" — words that carry no structural or emotional weight. Leading 'The/A/An' is
# handled separately (it is the single most common failure in this corpus).
FILLER = {"that", "just", "now", "is", "are", "was", "were", "will", "can", "into", "of", "about",
          "very", "really", "quite", "some", "there", "here", "also"}
WEAK_VERBS = {"is", "are", "was", "were", "has", "have", "had", "will", "can", "may", "might"}

# Rule 2 — psychological triggers.
CURIOSITY = ("why", "how", "what", "stop", "not", "isn't", "aren't", "doesn't", "don't", "won't",
             "no longer", "still", "but", "myth", "everyone", "nobody", "actually", "wrong",
             "never", "before you", "instead", "moving target", "shifts", "changes")
LOSS = ("mistake", "trap", "kill", "dies", "dead", "wrong", "overpriced", "overpay", "hidden",
        "silent", "fail", "failure", "gap", "penalty", "lose", "loss", "risk", "stuck", "blind",
        "denied", "expensive", "pricier", "paywall", "bricked", "break", "overrun", "creep",
        "squeeze", "bill", "cost", "cheaper", "raise", "jump", "hike", "cliff", "veto", "denial",
        # Added after the owner re-cut an article himself: 'illusion' (you were sold something that
        # is not what it looks like), 'brittle' and 'drift' (it breaks, or moves off you) are the
        # friction words his own example headlines used, and the list did not know them.
        "illusion", "brittle", "drift")

# Rule 3 — specificity.
TARGET = ("your", "you", "shipper", "carrier", "homeowner", "cfo", "cfo's", "ops", "landlord",
          "analyst", "team", "buyer", "importer", "engineer", "founder", "investor", "driver",
          "planner", "procurement")

STOP = set("""a an the and or of in on for to is are was were be been being that this these those
will can just now your you it its with by at from as into than then so not no do does did but if
when how why what who which while their there has have had""".split())


def words(text: str) -> list[str]:
    return re.findall(r"[A-Za-z0-9$%€£][A-Za-z0-9$%'’.,-]*", text or "")


def core_of(title: str) -> str:
    """The core headline: everything before a subtitle separator (':' '—' '–' '|')."""
    return re.split(r"\s*[:—–|]\s*", title or "", maxsplit=1)[0].strip()


def body_figures(body: str) -> list[str]:
    """The figures the article's own 'By the numbers' section states — the pool a title may cite."""
    m = re.search(r"\*{0,2}By the numbers:?\*{0,2}(.*?)(?=\n#{1,3}\s|\Z)", body or "", re.S)
    scope = m.group(1) if m else (body or "")
    return re.findall(r"\$?\d[\d,.]*\s?(?:%|percent|k|m|bn|billion|million)?", scope)


def lead_of(body: str) -> str:
    """The first paragraph of prose — everything a reader sees before deciding to stay or leave."""
    paras = [p.strip() for p in re.sub(r"<!--.*?-->", "", body or "", flags=re.S).split("\n\n")
             if p.strip() and not p.startswith(("#", "-", ">", "|"))]
    return paras[0] if paras else ""


def _figure_cores(text: str) -> list[str]:
    """The digits inside every figure, so '$915M', '$915 million' and '915' compare equal.

    Case and unit suffixes broke the first version of this check: a title reading '$915M' was
    compared, original case, against a lowercased lead containing '$915 million' and reported the
    lead as not stating the figure. Compare digit cores, never the surface form.
    """
    return [re.sub(r"[^\d]", "", f) for f in re.findall(r"\$?\d[\d.,]*%?", text) if re.sub(r"[^\d]", "", f)]


def lead_delivery(title: str, body: str) -> tuple[bool, str]:
    """Does the FIRST PARAGRAPH deliver what the headline promises? ADVISORY — never scored.

    Reported, not scored, on purpose. An independent read of five live articles (2026-10-10) found
    four headlines whose promise the lead never made: 'Your 11.5kW EV Backup Costs $8,200' over a lead
    about Tesla turning cars into batteries; 'Nearshoring: Your 32.58% Trade Risk Remains' over a lead
    that never names 32.58%; '6 Windows, Not 1' over a lead that never counts them. But a literal
    string match cannot see paraphrase ('Three months after a job ends' *is* '90-day'), so making this
    a scored rule would punish correct headlines and tilt the weights — it broke the reference headline
    the moment it was scored. Keep it as evidence for the reviewer, never as a scoring input.
    """
    if len(words(body)) < 40:
        return True, ""
    lead = lead_of(body).lower()
    # Only real words: a figure token ('$915M') must be judged by the figure check below, not as a
    # word looking for a literal '$915m' in the prose — a lead reading '$915 million' satisfies it.
    content = [x.lower().strip(".,;:") for x in words(title)
               if x.lower() not in STOP and len(x) > 3 and not any(c.isdigit() for c in x)]
    lead_cores = _figure_cores(lead)
    substantive = [f for f in re.findall(r"\$?\d[\d.,]*%?[a-z]?", title)
                   if len(re.sub(r"[^\d]", "", f)) > 1]
    miss_figs = [f for f in substantive if re.sub(r"[^\d]", "", f) not in lead_cores]
    miss_words = [c for c in content if c not in lead]
    if not miss_figs and len(miss_words) <= max(1, len(content) // 3):
        return True, ""
    why = f"the lead never states {', '.join(miss_figs)}" if miss_figs else ""
    return False, (why or f"absent from the lead: {', '.join(miss_words[:4])}")


def score(title: str, *, body: str = "", keyword: str = "") -> dict:
    """Score one headline. Returns the rules that passed, the ones that failed, and 0-100."""
    title = (title or "").strip()
    w = words(title)
    core = core_of(title)
    cw = words(core)
    low = title.lower()
    failures: list[str] = []
    passes: list[str] = []
    points = 0
    maxpoints = 0

    def rule(name: str, ok: bool, weight: int = 1, note: str = "") -> None:
        nonlocal points, maxpoints
        maxpoints += weight
        (passes if ok else failures).append(f"{name}{(': ' + note) if note and not ok else ''}")
        if ok:
            points += weight

    # ── 1. length & scannability ────────────────────────────────────────────────────────────────
    rule("core headline <= 6 words", len(cw) <= CORE_WORDS_MAX, 3,
         f"core is {len(cw)} words ('{core}')")
    rule("whole title <= 10 words", len(w) <= TOTAL_WORDS_MAX, 2, f"{len(w)} words")
    rule("fits a search result (<= 60 chars)", len(title) <= SEO_CHARS_MAX, 1, f"{len(title)} chars")
    rule("opens on substance, not 'The/A/An'", (w[0].lower() not in LEAD_STOPWORDS) if w else False, 2,
         "starts with a filler article; front-load the strongest noun")

    # ── 2. fluff ───────────────────────────────────────────────────────────────────────────────
    filler = [x for x in w if x.lower() in FILLER]
    rule("no filler words", len(filler) <= 1, 1, f"filler: {', '.join(filler)}")

    # ── 3. psychological triggers ──────────────────────────────────────────────────────────────
    has_curiosity = any(c in low for c in CURIOSITY)
    has_loss = any(c in low for c in LOSS)
    rule("carries a hook (curiosity gap or loss aversion)", has_curiosity or has_loss, 3,
         "states a fact but gives the reader no reason to open it")

    # ── 4. specificity ─────────────────────────────────────────────────────────────────────────
    figures = body_figures(body)
    has_digit = bool(re.search(r"\d", title))
    rule("a number anchors it (the article states figures)", has_digit or not figures, 2,
         f"the piece states {len(figures)} figures; the title cites none")
    # The reader must feel called out. Second person or a role noun is the direct case; a proper noun
    # in the first three words (California, SpaceX, Home Assistant) is the indirect one, and it counts
    # — 'California FAIR Plan Premiums Jump 29.1%' names its audience as surely as 'Your …' does.
    proper = any(x[:1].isupper() and x.lower() not in STOP and x.lower() not in FILLER
                 for x in w[:3])
    rule("names the reader (or their role)", any(t in low for t in TARGET) or proper, 2,
         "no 'you/your', no role noun and no named subject — the target never feels called out")

    # ── 5. honesty (no bait-and-switch) ────────────────────────────────────────────────────────
    if len(words(body)) > 40:
        content = [x.lower().strip(".,;:") for x in w
                   if x.lower() not in STOP and len(x) > 3 and not any(c.isdigit() for c in x)]
        front = " ".join(words(body)[:600]).lower()
        missing = [c for c in content if c not in front]
        rule("the promise is in the article (first ~600 words)", len(missing) <= max(1, len(content) // 3),
             3, f"absent from the opening: {', '.join(missing[:4])}")

    if keyword:
        rule(f"keeps the target keyword ('{keyword}')", keyword.lower() in low, 3, "keyword missing")

    verdict = "STRONG" if points == maxpoints else ("OK" if points >= maxpoints * 0.75 else
                                                    ("WEAK" if points >= maxpoints * 0.5 else "POOR"))
    lead_ok, lead_note = lead_delivery(title, body)
    return {"title": title, "core": core, "words": len(w), "core_words": len(cw), "chars": len(title),
            "score": round(100 * points / max(1, maxpoints)), "verdict": verdict,
            "failures": failures, "passes": passes, "lead_ok": lead_ok, "lead_note": lead_note}


def artifact_title(path: pathlib.Path) -> tuple[str, str, str]:
    """(title, body, keyword) for an artifact."""
    text = path.read_text()
    m = re.match(r"---\n(.*?)\n---\n(.*)", text, re.S)
    fm, body = (m.group(1), m.group(2)) if m else ("", text)
    title = keyword = ""
    for line in fm.splitlines():
        if line.startswith("title:"):
            title = line.split(":", 1)[1].strip().strip('"').strip("'")
        elif line.startswith("primary_keyword:"):
            keyword = line.split(":", 1)[1].strip().strip('"').strip("'")
    return title, body, keyword


def main() -> int:
    ap = argparse.ArgumentParser(description="Score a headline against the desk's title rules.")
    ap.add_argument("title", nargs="?", help="the headline to score")
    ap.add_argument("--slug", help="score the artifact's frontmatter title")
    ap.add_argument("--all", action="store_true", help="audit every published artifact")
    ap.add_argument("--json", action="store_true")
    args = ap.parse_args()

    if args.all:
        rows = []
        for path in sorted((ROOT / "published").glob("*.md")):
            t, b, k = artifact_title(path)
            rows.append({**score(t, body=b, keyword=k), "file": path.name,
                         "date": path.name[:10], "enforced": enforced(path.name[:10])})
        if args.json:
            print(json.dumps(rows, indent=2))
        else:
            live = [r for r in rows if r["enforced"]]
            old = [r for r in rows if not r["enforced"]]
            bad = [r for r in live if r["verdict"] in ("WEAK", "POOR")]
            print(f"headlines: {len(rows)} scored | {sum(1 for r in live if r['verdict']=='STRONG')} strong, "
                  f"{sum(1 for r in live if r['verdict']=='OK')} ok, {len(bad)} weak/poor "
                  f"(standard applies from {ENFORCED_FROM}; {len(old)} older headline(s) grandfathered)")
            undelivered = [r for r in live if not r["lead_ok"]]
            print(f"lead delivery (advisory, unscored): {len(live) - len(undelivered)}/{len(live)} headlines "
                  f"are delivered by their own first paragraph")
            for r in undelivered:
                print(f"  ? {r['score']:>3} {r['verdict']:<6} | {r['title'][:70]}")
                print(f"        - {r['lead_note']}")
            for r in sorted(live, key=lambda r: r["score"])[:12]:
                print(f"  {r['score']:>3} {r['verdict']:<6} {r['words']:>2}w {r['chars']:>3}c | "
                      f"{r['title'][:70]}")
                for f in r["failures"][:3]:
                    print(f"        - {f}")
        return 0

    if args.slug:
        hits = sorted((ROOT / "published").glob(f"*_{args.slug}.md"))
        if not hits:
            print(f"no artifact for '{args.slug}'", file=sys.stderr)
            return 1
        t, b, k = artifact_title(hits[-1])
    else:
        t, b, k = args.title or "", "", ""

    result = score(t, body=b, keyword=k)
    if args.json:
        print(json.dumps(result, indent=2))
    else:
        print(f"{result['score']}/100 {result['verdict']} — {result['title']}")
        print(f"  core {result['core_words']}w, total {result['words']}w, {result['chars']} chars")
        for f in result["failures"]:
            print(f"  FAIL - {f}")
        if not result["failures"]:
            print("  all rules pass")
    return 0 if result["verdict"] != "POOR" else 1


if __name__ == "__main__":
    raise SystemExit(main())

#!/usr/bin/env python3
"""The reviewer stage: read a raw article, write the humanized whole, prove it kept the facts.

What this replaces
------------------
Loop 3 used to be a 100-line prompt that rewrote the draft in one call and then graded *itself*:
the artifact ended with a `## Gate report` in which the same model wrote "PASS — lead: direct
opening…". Nothing compared the rewrite to the draft, so the only rules that held were the ones a
human ran afterwards. Measured over 216 draft/final pairs, that arrangement lost a figure in 128
articles (the `22.5% down to 10.9%` share pair, `13.41 cents`, `22,269 tokens a second`) and made
the prose *less* human in three of four: sentence-length variance fell in 159/216, filler density
rose in 108/216, and the same five observer cues turned up in 29-56 articles each.

So the stage is two things in one pass:

  1. **READ** — the model states the piece's through-line and the shape the story wants, in a
     `review-note` block that becomes part of the review report and never reaches a reader. A pass
     that cannot say what the article is about in one sentence cannot make it read as a whole.
  2. **WRITE** — one whole-document humanized rewrite under an ordered contract, with the verified
     ledger of figures spelled out in the prompt (a specific "do not lose" list beats a generic
     "preserve all facts").

Then `review_audit.audit()` decides whether the rewrite is acceptable, and a failure is fed back as
the exact missing figure with the draft's own sentence around it, plus the measured rhythm delta. A
rewrite that cannot be accepted is held — it is never silently written as the `_final.md` a publisher
reads.

    python3 scripts/article_reviewer.py --draft context/drafts/<slug>_draft.md
    python3 scripts/article_reviewer.py --draft <path> --brief <brief.md> --attempts 2

An accepted rewrite lands as `<slug>_final.md`; the report always lands in
`context/drafts/reviews/<slug>_review.md`, and a held rewrite lands there too as `_held.md` — never
in place of a final, and never anywhere the voice gate or the publisher walks.
    python3 scripts/article_reviewer.py --draft <path> --dry-run        # print the prompt, no call
    python3 scripts/article_reviewer.py --audit --draft A --final B     # audit only (no LLM)

Exit codes: 0 accepted · 1 held (no candidate passed, see the review report) · 2 bad input.
"""
from __future__ import annotations

import argparse
import datetime
import json
import pathlib
import re
import sys
import urllib.request

ROOT = pathlib.Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT / "scripts"))

import humanizer_tools as ht  # noqa: E402  (frontmatter repair, keyword, provider key)
import review_audit as ra  # noqa: E402

MODEL = "gemini-3.1-pro-preview"
MAX_TOKENS = 32000
TIMEOUT = 900
ATTEMPTS = 3
GEMINI = "https://generativelanguage.googleapis.com/v1beta/models/{model}:generateContent?key={key}"

MARKERS = ("<!-- lead -->", "<!-- tension -->", "<!-- tactical-insight -->",
           "<!-- nuanced-takeaway -->", "<!-- tldr -->")

SKELETON = ("## The big picture:", "## By the numbers", "## What I'd watch:", "## The catch",
            "## At a glance")


# --------------------------------------------------------------------------------------- the call

def call_model(prompt: str, *, model: str = MODEL, timeout: int = TIMEOUT,
               max_tokens: int = MAX_TOKENS, temperature: float = 0.7) -> str:
    body = {
        "contents": [{"parts": [{"text": prompt}]}],
        "generationConfig": {"maxOutputTokens": max_tokens, "temperature": temperature},
    }
    url = GEMINI.format(model=model, key=ht._key())
    req = urllib.request.Request(url, data=json.dumps(body).encode(),
                                 headers={"Content-Type": "application/json"})
    with urllib.request.urlopen(req, timeout=timeout) as r:
        payload = json.loads(r.read().decode())
    cand = (payload.get("candidates") or [{}])[0]
    finish = cand.get("finishReason", "")
    parts = (cand.get("content") or {}).get("parts") or []
    text = "".join(p.get("text", "") for p in parts).strip()
    if finish == "MAX_TOKENS" and "## Sources" not in text:
        raise RuntimeError(f"truncated rewrite (finishReason={finish}); raise max_tokens")
    if not text:
        raise RuntimeError(f"empty rewrite (finishReason={finish})")
    return text


# -------------------------------------------------------------------------------------- the brief

def find_brief(draft_path: pathlib.Path, draft: str) -> pathlib.Path | None:
    """The brief this draft was written from — identified by the sources they share.

    Vocabulary overlap is not an identity test: a beat's briefs share the beat's words, so matching
    on the vertical picked an unrelated OTIF synthesis for an ETA piece and then told the model that
    brief was authoritative. The draft's own `## Sources` URLs are the identity: the brief that
    produced the draft lists the same pages. No shared source means no brief — never a guess.
    """
    pool = sorted(p for p in (ROOT / "context" / "recon_proposals").glob("*_brief.md")
                  if p.name.endswith(("_brief.md", "_verified_brief.md")))
    if not pool:
        return None
    urls = {u.rstrip("/").lower() for u in ra._URL.findall(draft)}
    urls = {u for u in urls if not u.endswith((".png", ".jpg", ".jpeg"))}
    if not urls:
        return None
    best: tuple[int, pathlib.Path] | None = None
    for path in pool:
        try:
            text = path.read_text(encoding="utf-8", errors="ignore").lower()
        except OSError:
            continue
        shared = sum(1 for u in urls if u.rstrip("/") in text)
        if shared < 2 and not (shared == 1 and len(urls) == 1):
            continue
        if best is None or shared > best[0]:
            best = (shared, path)
    return best[1] if best else None


# ------------------------------------------------------------------------------------- the prompt

def ledger_lines(led: dict) -> list[str]:
    """The figures as claims, not as a bag of numbers: '<figure> — "<sentence>"'."""
    lines = []
    for key, fig in sorted(led["figures"].items(), key=lambda kv: -kv[1]["value"]):
        ctx = re.sub(r"\s+", " ", fig["context"]).strip()
        lines.append(f"- {key} — \"{ctx[:240]}\"")
    return lines


def build_prompt(draft: str, led: dict, draft_flow: dict, feedback: list[str] | None = None,
                 brief: str = "") -> str:
    figures = ledger_lines(led)
    figure_block = "\n".join(figures) if figures else "- (no measured figures in the draft)"
    source_block = "\n".join(led["sources"]) if led["sources"] else "(none)"
    brief_note = (f"\nTHE VERIFIED BRIEF (authoritative; the article may only claim what this "
                  f"supports)\n{brief.strip()[:6000]}\n" if brief.strip() else "")
    rhythm = draft_flow["rhythm"]
    retry = ""
    if feedback:
        retry = ("\nTHE PREVIOUS ATTEMPT WAS NOT ACCEPTED. These are measured, not opinions — fix "
                 "every line:\n" + "\n".join(feedback) + "\n"
                 f"\nThe numbers the desk measures on the returned text, so you can aim at them: "
                 f"mean sentence length 17-22 words (the draft's is {rhythm['mean']}), spread "
                 f"(standard deviation) at least {rhythm['sd']}, at most 1 sentence in 8 under 9 "
                 f"words, body Flesch reading ease at least 50 (target 60).\n")

    return f"""You are the reviewer and rewriter of a long-form article. You are the last reader before
it ships, so your job is to make the finished piece read as one expert wrote it on one sitting —
and to keep every fact exactly as the reporting found it.

WORK IN TWO STEPS.

STEP 1 — READ. Before writing a word, work out:
  * the through-line: the one sentence this article is actually arguing;
  * the shape it wants: what each section must do for that argument, in what order;
  * what is not yet earned: any claim that arrives without the evidence in this draft.
Put both in the review note below. It is read by the desk and never published.

STEP 2 — WRITE the whole article again, as that reader. Not a paraphrase of the draft and not a
section-by-section tidy-up: one piece of prose that carries one argument from the first sentence to
the last, in which each paragraph earns the next.

PRIORITIES, in this order. A lower one never buys the higher one.

1. ACCURACY. Every figure, unit, date, name, quote and [n] citation below must survive with its
   meaning intact — the same noun, the same base, the same direction. Do not round a figure into a
   vaguer quantifier ("dozens", "hundreds", "most"), do not add a figure that is not here, do not
   turn a share of something into an absolute, do not convert a comparison into an effect size.
   The `## Sources` list is copied verbatim.
2. COHESION. The piece has to read as a whole: write the joins between sections, carry one term for
   one thing, and develop the argument instead of restating it. If a section only re-says what the
   lead already said, cut it and give the space to the evidence that is not yet on the page.
3. VOICE. One person who has read the filings and is telling you what they make of it. Plain words.
   Sentences of ~14-22 words with real variation — some long and connected, some four words long
   when the point needs a beat. Paragraphs of 3-5 sentences. No throat-clearing, no "in today's
   world", no "moreover", no "it's important to note", no summary sign-off.
   Each interpreting section — tension, the tactical section, and the catch — carries exactly one
   first-person cue, written by you: an observation you made ("I read the table three times"),
   an opinion labelled as yours ("My reading, held loosely: …"), or what you are watching next.
   Not a borrowed phrasing, and not one in every sentence — the reporting stays plain.
4. ACCESSIBILITY. Plain words carry the reading level, never short sentences: aim a Flesch reading
   ease of 60 on the body (50 is the hard floor), so swap long nouns for everyday ones rather than
   clipping sentences. Expand every acronym once, at its first use in the body — "Automatic
   Identification System (AIS)" or "AIS (the ship-tracking signal)". Never invent an expansion for a
   product or system name; rephrase to drop the all-caps token instead.
5. SHAPE. The house skeleton, in this order, on its own lines with a blank line either side:
   {', '.join(SKELETON)}. "What I'd watch" reports what the people closest to the story are doing
   and what answers the open question next — never a playbook for the reader.

DO NOT LOSE — the measured facts of this draft. Each line is a figure and the sentence it came from;
every one must still be made, in your own words:
{figure_block}

SOURCES TO COPY VERBATIM:
{source_block}
{brief_note}
WHAT PREVIOUS PASSES GOT WRONG — these are measured on the desk's own corpus, so treat them as
defects, not preferences:
  * dropping a share, a rate or a ratio because it reads like colour. The share is usually the
    argument; a count is not more important than a share.
  * filling space with adverbs: really, actually, clearly, simply, essentially, fundamentally.
  * opening two sections with the same words, or opening every paragraph with its own subject.
  * flattening the prose into uniformly 15-word sentences. The draft's own rhythm is mean
    {rhythm['mean']} words, spread {rhythm['sd']}; keep that spread or widen it.
  * the borrowed observer cues ("the part I keep circling", "my read is that", "what strikes me
    here"). Write the observation in your own words or leave it out.
  * a "## Gate report". A gate is code; a model grading itself is not a review.
{retry}
OUTPUT, exactly this order and nothing else:

<!-- review-note -->
THROUGH-LINE: <one sentence>
SHAPE: <section: what it does> ; <section: what it does> ; …
<!-- /review-note -->

<the frontmatter exactly as given, with `title` re-cut only if you can improve it while keeping the
`primary_keyword` if one is present>

<!-- lead -->
…

…all five sections with their markers and the house H2s…

## Sources
<verbatim>

BEFORE YOU RETURN — the desk's build runs these checks mechanically, and a run that fails one is
held instead of published, so satisfy them deliberately rather than hoping:

  1. The five section markers are present, in order, each with its house H2.
  2. **Each interpreting section — tension, the tactical section and the catch — contains at least
     one first-person sentence.** This is checked by a regex for "I" / "my", not by intent: write
     the observation plainly ("I read the table twice before believing it", "My reading is that the
     floor matters more than the model", "What I am watching is the December numbers"). One per
     section, in your own words, and no borrowed phrasing.
  3. `## Sources` is copied verbatim, character for character.
  4. The body reads at Flesch ease 50 or better (aim 60): everyday words, sentences averaging 17-22
     words, no more than one sentence in eight under nine words. A choppy body fails as surely as a
     dense one — rhythm is a spread, not a short average. Long words are what sink the score: keep
     each technical noun to one full mention and use the short everyday word after it.
  5. The body contains none of these filler adverbs: really, actually, clearly, simply, essentially,
     basically, fundamentally, ultimately, notably, importantly. They are counted per 1,000 words,
     so three of them is a regression.

THE DRAFT TO REWRITE:

{draft}
"""


# ---------------------------------------------------------------------------------- sanitisation

def long_words(text: str, limit: int = 12) -> list[str]:
    """The words pushing a body's reading level up — named, so the retry can replace them."""
    import collections
    stop = set(ra._THESIS_STOP) | {"because", "between", "through", "another", "whether",
                                   "without", "already", "against", "really", "always"}
    counts = collections.Counter(
        w.lower() for w in re.findall(r"[A-Za-z][A-Za-z'\-]{6,}", ra.body(text))
        if w.lower() not in stop)
    return [w for w, _ in counts.most_common(limit)]


def accessibility(text: str) -> dict:
    """The desk's ACCESS gate on a candidate, in-process (plain words, acronyms, Flesch floor).

    `verify.sh` runs the same checker on the committed artifact, so a rewrite that fails it here would
    fail the build later — cheaper to hold now and feed the exact criterion back.
    """
    import os
    import tempfile
    fd, path = tempfile.mkstemp(suffix=".md", dir=os.environ.get("TMPDIR", "/tmp"))
    try:
        with os.fdopen(fd, "w", encoding="utf-8") as fh:
            fh.write(text)
        return ht.measure(path)
    finally:
        try:
            os.unlink(path)
        except OSError:
            pass


def split_review_note(text: str) -> tuple[str, str]:
    """Pull the model's reading out of the artifact — it is report material, not prose."""
    m = re.search(r"<!--\s*review-note\s*-->([\s\S]*?)<!--\s*/review-note\s*-->", text, re.I)
    if not m:
        return text, ""
    return (text[:m.start()] + text[m.end():]), m.group(1).strip()


def strip_gate_report(text: str) -> tuple[str, bool]:
    """Remove a self-graded gate report if the model writes one anyway."""
    m = re.search(r"\n##\s*Gate report[\s\S]*$", text, re.I)
    if not m:
        return text, False
    return text[:m.start()].rstrip() + "\n", True


def sanitize(raw: str) -> tuple[str, dict]:
    """Everything mechanical about the returned text: fences, frontmatter, note, gate report."""
    notes = {}
    text = raw.strip()
    text = re.sub(r"^```[a-zA-Z]*\s*", "", text)
    text = re.sub(r"\s*```\s*$", "", text)
    text, notes["review_note"] = split_review_note(text)
    text, notes["gate_report_stripped"] = strip_gate_report(text)
    text = ht.normalize_frontmatter(text.strip())
    text = ht.ensure_title_contains_keyword(text)
    return text.strip() + "\n", notes


# ------------------------------------------------------------------------------------ the stage

def review(draft_path: pathlib.Path, *, brief_path: pathlib.Path | None = None,
           out_path: pathlib.Path | None = None, report_path: pathlib.Path | None = None,
           attempts: int = ATTEMPTS, model: str = MODEL, timeout: int = TIMEOUT,
           dry_run: bool = False, keep_attempts: bool = False) -> dict:
    draft = draft_path.read_text(encoding="utf-8")
    brief = brief_path.read_text(encoding="utf-8") if brief_path and brief_path.exists() else ""
    led = ra.ledger(draft, brief)
    draft_flow = ra.flow(draft)

    prompt = build_prompt(draft, led, draft_flow, brief=brief)
    if dry_run:
        return {"prompt": prompt, "ledger": {k: (v if k != "figures" else len(v))
                                             for k, v in led.items()}}

    default_out = draft_path.with_name(draft_path.name.replace("_draft.md", "_final.md"))
    stem = draft_path.name.replace("_draft.md", "")
    reviews = draft_path.parent / "reviews"
    explicit_out = out_path is not None
    out_path = out_path or default_out
    report_path = report_path or reviews / f"{stem}_review.md"
    report_path.parent.mkdir(parents=True, exist_ok=True)

    best: dict | None = None
    trail: list[dict] = []
    notes: dict = {}
    feedback: list[str] | None = None
    for attempt in range(1, attempts + 1):
        try:
            raw = call_model(prompt, model=model, timeout=timeout)
        except Exception as exc:  # noqa: BLE001 — surfaced, never swallowed
            trail.append({"attempt": attempt, "error": str(exc)})
            print(f"  attempt {attempt}: call failed — {exc}")
            break
        text, notes = sanitize(raw)
        if keep_attempts:
            # Next to the report, not next to the draft: `context/drafts/` is walked by the voice
            # gate, and a rejected attempt is by definition a body that may fail it.
            reviews.mkdir(parents=True, exist_ok=True)
            (reviews / f"{stem}_attempt{attempt}.md").write_text(text, encoding="utf-8")
        result = ra.audit(draft, text, brief)
        acc = accessibility(text)
        result["accessibility"] = {"verdict": acc.get("verdict"), "flesch": acc.get("flesch")}
        for fail in acc.get("fails") or []:
            hint = ""
            if "flesch" in fail.lower():
                hint = (" — the long words costing the score, each to be replaced or used once: "
                        + ", ".join(long_words(text)))
            result["hard"].append(f"accessibility gate: {fail}{hint}")
        result["ok"] = not result["hard"]
        result["score"] = ra.score(result)
        trail.append({
            "attempt": attempt,
            "ok": result["ok"],
            "hard": len(result["hard"]),
            "regressions": len(result["regressions"]),
            "rhythm_sd": [draft_flow["rhythm"]["sd"], result["flow"]["rhythm"]["sd"]],
            "rhythm_health": [draft_flow["rhythm_health"], result["flow"]["rhythm_health"]],
            "filler": [draft_flow["filler"], result["flow"]["filler"]],
            "words": result["flow"]["words"],
            "flesch": acc.get("flesch"),
            "score": result["score"],
        })
        print(f"  attempt {attempt}: {'ACCEPT' if result['ok'] and not result['regressions'] else 'reject'}"
              f"  hard={len(result['hard'])} regressions={len(result['regressions'])}"
              f"  rhythm {draft_flow['rhythm']['sd']}->{result['flow']['rhythm']['sd']}"
              f"  health {draft_flow['rhythm_health']}->{result['flow']['rhythm_health']}"
              f"  flesch {acc.get('flesch')}  words {result['flow']['words']}")
        if best is None or result["score"] > best["result"]["score"]:
            best = {"text": text, "result": result, "attempt": attempt}
        # Write the trail after every attempt: a run killed mid-generation (SIGKILL, OOM) otherwise
        # leaves no report at all, and "the file is missing" is not a diagnosis.
        report_path.write_text(
            render_report(draft_path, out_path, best, trail, notes,
                          accepted=result["ok"] and not result["regressions"],
                          draft_flow=draft_flow)
            + f"\n\n(in progress — attempt {attempt} of {attempts})\n", encoding="utf-8")
        if result["ok"] and not result["regressions"]:
            break
        prompt = build_prompt(draft, led, draft_flow,
                              feedback=ra.feedback(result) + [f"- FIX  {r}" for r in result["regressions"]],
                              brief=brief)

    assert best is not None, "no candidate to write"
    accepted = best["result"]["ok"] and not best["result"]["regressions"]

    if not accepted and not explicit_out:
        # A held rewrite must never replace the artifact a publisher reads, and it must not sit in
        # `context/drafts/` either: the voice gate walks that directory and a deliberately unfinished
        # body would redden the repo build. Held text and every report land in `reviews/`.
        out_path = reviews / f"{stem}_held.md"
    out_path.parent.mkdir(parents=True, exist_ok=True)
    out_path.write_text(best["text"], encoding="utf-8")
    report = render_report(draft_path, out_path, best, trail, notes, accepted, draft_flow)
    report_path.write_text(report, encoding="utf-8")

    print(f"  wrote {out_path.name} {'ACCEPTED' if accepted else 'HELD'}; report {report_path.name}")
    return {"accepted": accepted, "attempt": best["attempt"], "report": str(report_path),
            "hard": best["result"]["hard"], "regressions": best["result"]["regressions"],
            "trail": trail}


def render_report(draft_path: pathlib.Path, out_path: pathlib.Path, best: dict,
                  trail: list[dict], notes: dict, accepted: bool, draft_flow: dict) -> str:
    r = best["result"]
    f, d = r["flow"], r["draft_flow"]
    lines = [
        f"# Review report — {out_path.name}",
        "",
        f"- verdict: **{'ACCEPTED' if accepted else 'HELD — do not publish'}**",
        f"- draft: `{draft_path.name}` · attempt kept: {best['attempt']} of {len(trail)}",
        f"- figures in the ledger: {r['ledger']['figures']} · citations: "
        f"{r['ledger']['citations']} · quotes: {r['ledger']['quotes']} · sources: "
        f"{r['ledger']['sources']}",
        "",
        "## The reviewer's reading",
        "",
        notes.get("review_note") or "(the model returned no review note)",
        "",
        "## What the rewrite did to the prose",
        "",
        "| metric | draft | final |",
        "|---|---|---|",
        f"| words | {d['words']} | {f['words']} |",
        f"| sentence length mean | {d['rhythm']['mean']} | {f['rhythm']['mean']} |",
        f"| sentence length spread (sd) | {d['rhythm']['sd']} | {f['rhythm']['sd']} |",
        f"| rhythm health (0-1) | {d['rhythm_health']} | {f['rhythm_health']} |",
        f"| short sentences (<=8 words) | {d['rhythm']['short_pct']}% | {f['rhythm']['short_pct']}% |",
        f"| filler per 1,000 words | {d['filler']} | {f['filler']} |",
        f"| hedge per 1,000 words | {d['hedge']} | {f['hedge']} |",
        f"| abstraction per 1,000 words | {d['abstraction']} | {f['abstraction']} |",
        f"| repeated 5-grams | {d['repetition']['repeated_5grams']} | "
        f"{f['repetition']['repeated_5grams']} |",
        f"| sentences repeated verbatim | {d['duplicates']['count']} | {f['duplicates']['count']} |",
        f"| Flesch reading ease | — | "
        f"{(r.get('accessibility') or {}).get('flesch', '—')} "
        f"({(r.get('accessibility') or {}).get('verdict', 'not measured')}) |",
        f"| sections restating the through-line | {d['restatement']['sections_restating']} | "
        f"{f['restatement']['sections_restating']} |",
        f"| staccato paragraphs | {d['paragraphs']['staccato_share']}% | "
        f"{f['paragraphs']['staccato_share']}% |",
        "",
    ]
    if notes.get("gate_report_stripped"):
        lines += ["Note: the model wrote a self-graded `## Gate report`; it was stripped from the "
                  "artifact and is not part of the article.", ""]
    if r["hard"]:
        lines += ["## Hard failures still present", ""] + [f"- {h}" for h in r["hard"]] + [""]
    if r["regressions"]:
        lines += ["## Flow regressions against the draft", ""] + \
                 [f"- {x}" for x in r["regressions"]] + [""]
    if r["advisories"]:
        lines += ["## Advisories", ""] + [f"- {a}" for a in r["advisories"]] + [""]
    lines += ["## Attempt trail", "", "```",
              *[json.dumps(t, ensure_ascii=False) for t in trail], "```", ""]
    return "\n".join(lines)


# -------------------------------------------------------------------------------------------- cli

def main() -> int:
    ap = argparse.ArgumentParser(description="Review a draft into a humanized, fact-preserving whole")
    ap.add_argument("--draft", required=True)
    ap.add_argument("--brief", default="", help="verified brief (auto-discovered if omitted)")
    ap.add_argument("--out", default="")
    ap.add_argument("--report", default="")
    ap.add_argument("--attempts", type=int, default=ATTEMPTS)
    ap.add_argument("--model", default=MODEL)
    ap.add_argument("--timeout", type=int, default=TIMEOUT)
    ap.add_argument("--dry-run", action="store_true", help="print the prompt, make no call")
    ap.add_argument("--keep-attempts", action="store_true",
                    help="write every attempt beside the draft, for diagnosing a held run")
    ap.add_argument("--audit", action="store_true",
                    help="audit only: compare --draft to --out (no LLM call)")
    args = ap.parse_args()

    draft_path = pathlib.Path(args.draft)
    if not draft_path.is_absolute():
        draft_path = ROOT / draft_path
    if not draft_path.exists():
        print(f"no such draft: {draft_path}")
        return 2

    if args.audit:
        final = pathlib.Path(args.out or str(draft_path).replace("_draft.md", "_final.md"))
        result = ra.audit(draft_path.read_text(), final.read_text())
        for h in result["hard"]:
            print(f"FAIL {h}")
        for a in result["advisories"]:
            print(f"~    {a}")
        print("=> " + ("PASS" if result["ok"] else "FAIL"))
        return 0 if result["ok"] else 1

    brief_path = pathlib.Path(args.brief) if args.brief else find_brief(
        draft_path, draft_path.read_text())
    if brief_path and not brief_path.is_absolute():
        brief_path = ROOT / brief_path
    print(f"reviewer: {draft_path.name}" + (f"  brief: {brief_path.name}" if brief_path else
                                            "  (no verified brief found)"))

    if args.dry_run:
        out = review(draft_path, brief_path=brief_path, dry_run=True)
        print(out["prompt"])
        return 0

    result = review(
        draft_path,
        brief_path=brief_path,
        out_path=pathlib.Path(args.out) if args.out else None,
        report_path=pathlib.Path(args.report) if args.report else None,
        attempts=args.attempts,
        model=args.model,
        timeout=args.timeout,
        keep_attempts=args.keep_attempts,
    )
    if not result["accepted"]:
        print("HELD at review: see the report. Do not publish this artifact.")
        return 1
    return 0


if __name__ == "__main__":
    sys.exit(main())

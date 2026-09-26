"""Shared helpers for the Loop 3 humanizer scripts: a compliance-retry loop that, when a
rewrite fails the topic-agnostic accessibility gate, feeds the exact FAIL reasons back to
the frontier model and re-prompts (up to MAX_ATTEMPTS).

Import with:  import humanizer_tools as ht   (scripts/ is on sys.path when these run).
"""
import json
import pathlib
import re
import urllib.request

MODEL = "gemini-3.1-pro-preview"
MAX_ATTEMPTS = 5  # how many times to re-prompt the model before holding at Loop 3
MAX_TOKENS = 20000  # thinking-model budget: reasoning tokens count against this, so keep high
MIN_BODY_WORDS = 600  # body word floor: below this the frontier over-compacted; restore depth from the brief


def _key():
    KEY = None
    for envf in ["/root/.hermes/profiles/stylist/.env", "/root/.hermes/.env"]:
        p = pathlib.Path(envf)
        if p.exists():
            for line in p.read_text().splitlines():
                if line.startswith("GOOGLE_API_KEY="):
                    KEY = line.split("=", 1)[1].strip().strip('"').strip("'")
                    break
        if KEY:
            break
    assert KEY, "GOOGLE_API_KEY not found"
    return KEY


URL = f"https://generativelanguage.googleapis.com/v1beta/models/{MODEL}:generateContent?key={_key()}"


def call_gemini(prompt, max_tokens=MAX_TOKENS, temperature=0.7, timeout=240):
    body = {
        "contents": [{"parts": [{"text": prompt}]}],
        "generationConfig": {"maxOutputTokens": max_tokens, "temperature": temperature},
    }
    req = urllib.request.Request(URL, data=json.dumps(body).encode(),
                                 headers={"Content-Type": "application/json"})
    with urllib.request.urlopen(req, timeout=timeout) as r:
        j = json.loads(r.read().decode())
    return j["candidates"][0]["content"]["parts"][0]["text"].strip()


def measure(path):
    """Return the structured accessibility diagnosis for a written article file."""
    import sys
    scripts_dir = str(pathlib.Path(__file__).parent)
    if scripts_dir not in sys.path:
        sys.path.insert(0, scripts_dir)
    import check_accessibility as ca
    return ca.measure(path)


def normalize_frontmatter(text):
    """Restore the `---` YAML delimiters the frontier sometimes replaces with ``` code fences.

    Observed failure: the model emits the frontmatter wrapped in a triple-backtick fence
    instead of `---` lines. `clean()` strips only the *leading* fence, leaving an orphaned
    closing ``` mid-file, which breaks frontmatter parsing downstream (publisher, site).

    Idempotent: if the text already opens with a proper `---` fence, it is returned unchanged.
    """
    lines = text.split("\n")
    if not lines:
        return text
    if lines[0].strip() == "---":
        # Opening delimiter correct, but the model sometimes leaves a stray ``` fence
        # immediately after the frontmatter closing `---` (the orphaned *closing* code
        # fence). Strip any ``` fence line that sits between the closing `---` and the
        # first body content (a section marker, heading, or plain paragraph).
        close_idx = None
        for i in range(1, len(lines)):
            if lines[i].strip() == "---":
                close_idx = i
                break
        if close_idx is not None:
            # Remove any ``` line(s) directly after the closing delimiter, before body text.
            j = close_idx + 1
            cleaned = lines[:close_idx + 1]
            while j < len(lines) and (lines[j].strip() == "```" or lines[j].strip() == ""):
                if lines[j].strip() == "```":
                    j += 1
                    continue
                cleaned.append(lines[j])
                j += 1
            cleaned.extend(lines[j:])
            return "\n".join(cleaned)
        return text  # already correct
    fm_keys = ("title:", "vertical:", "persona:", "date:", "slug:", "one_big_thing:",
               "meta_title:", "meta_description:", "primary_keyword:", "secondary_keywords:",
               "search_volume:", "search_intent:", "article_url:", "promo_url:", "promo_label:")
    if not lines[0].strip().startswith(fm_keys):
        return text  # no frontmatter to fix (or it's not a YAML block)
    # Frontmatter present but the opening --- was dropped. Insert it, and convert the
    # first stray ``` fence (the frontmatter closer) into the closing ---.
    lines.insert(0, "---")
    for i, ln in enumerate(lines):
        if ln.strip() == "```":
            lines[i] = "---"
            break
    return "\n".join(lines)


def ensure_title_contains_keyword(text: str) -> str:
    """Ensure that if frontmatter contains primary_keyword, title contains the keyword.
    
    If the humanized rewrite somehow omitted the keyword from the title, safely prepends
    the properly-cased keyword to ensure 100% SEO alignment.
    """
    import check_accessibility as ca
    title_ok, kw, title = ca.check_title_keyword(text)
    if title_ok or not kw:
        return text

    # Need to fix title in frontmatter
    kw_title = " ".join([w[:1].upper() + w[1:] for w in kw.split()])
    new_title = f"{kw_title}: {title}" if title else f"{kw_title}: What the Field Data Actually Shows"
    
    # Replace title line in frontmatter
    def _replace_title(m):
        return f'title: "{new_title}"'
    
    fixed = re.sub(r'^title:\s*["\']?.*["\']?$', _replace_title, text, flags=re.M)
    return fixed


SOCIAL_VOICE_RULES = """
SOCIAL VOICE — the <!-- linkedin --> variant (skills/claude_humanizer.md §3.8; verify.sh §9 gates it):
- Write it as ONE PERSON COMMENTING on the news. You are not the author of the events, not the owner of
  the truth, and not the reader's advisor. Hold a point of view and label it as one.
- Required: at least one first-person observer cue — "I've been following this all week", "I keep coming
  back to one number", "My read:", "The part I keep circling:", "I'm curious how others are reading…",
  "What I'm watching next:".
- BANNED, no exceptions: verdict framing ("the signal is clear", "the real story is", "the truth is",
  "the lesson is/for", "make no mistake", "the bottom line is"); consultant framing ("here's the
  playbook", "The playbook:", "here's what you need to do", "the winning moves", "let me be clear",
  "trust me"); reader-directed commands and advice ("Stress test your…", "Match your…", "Treat X as a
  live deadline", "Map your exposure today", "you need to / must / should / have to…"). Rewrite each as
  an observation plus a question: "I'd want to know whether operators are stress-testing…", "Curious how
  others are handling…".
- Keep every figure, name and date the article carries, the hook-first first line, and <= 1,300
  characters. No hashtags or links (the publisher appends them). Re-voice; never re-report.
- The Reddit cards derive from this draft, so article prose addressed to the reader as advice ("You must
  re-run every project plan") is dropped by the generator — prefer observation-shaped sentences there.
"""

LONGFORM_VOICE_RULES = """
ARTICLE VOICE — the long-form body (skills/claude_humanizer.md §3.9; verify.sh §9 gates it):
- The article is a COMMENT on what is happening, written by one person who has been reading the filings,
  reports and news. Report the facts; label your reading of them as your reading. You did not cause the
  events, you are not the owner of the truth, and you are not the reader's advisor.
- Each interpreting section (<!-- tension -->, <!-- tactical-insight -->, <!-- nuanced-takeaway -->)
  carries at least one first-person observer cue: "I've been watching…", "What strikes me here:",
  "My read:", "I could be wrong, but…", "What I'd watch next:", "The part I keep circling:". One per
  section, not per sentence — the reporting stays plain.
- The tactical section is NOT a playbook. Report what the people closest to the story are doing and what
  the writer expects next; never instruct the reader. Use the signpost "**Where this bites:**" or
  "**What I'd watch:**" instead of "**The playbook:**" / "**What to do:**", and phrase the bullets as
  observations ("Operators are re-quoting every landed-cost model", "I'd want to see the December
  sourcing numbers") rather than commands ("Stress test your landed costs").
- The TL;DR's third slot is "**What I'd Watch:**" (not "**The Winning Moves:**"), with the same indented
  sub-bullet definitions of what to watch and why it matters.
- BANNED in the body: the same verdict/consultant/imperative constructions as SOCIAL VOICE above, plus
  "The lesson is/for", "the takeaway is", and any sentence that tells the reader what to do.
- Keep every fact, figure, [n] citation, acronym expansion and `## Sources` line. Re-voice; never
  re-report, never add a claim the verified brief does not carry.
"""


def retry_prompt(base_prompt, prev_text, diag, extra: str | list[str] = ""):
    """Build a follow-up prompt telling the frontier model exactly what the gate rejected."""
    notes = []
    if diag["fails"]:
        notes.append("FAILURES (must be fixed):")
        notes += [f"- {f}" for f in diag["fails"]]
    if diag["warnings"]:
        notes.append("ADVISORY (should be fixed):")
        notes += [f"- {w}" for w in diag["warnings"]]
    tip = []
    if any("title missing SEO keyword" in f for f in diag.get("fails", [])):
        tip.append("SEO KEYWORD IN TITLE: The frontmatter 'title:' MUST explicitly contain the exact or naturalized 'primary_keyword' (e.g. '<Keyword>: <Subtitle>'). Never omit the target search term from the headline.")
    if diag["undefined_acronyms"]:
        tip.append("Spell out each listed acronym in full at its first use (e.g. 'Full Name (ACR)').")
    if diag["flesch"] is not None and diag["flesch"] < diag["target"]:
        tip.append("Raise readability: split long sentences, prefer plain verbs over noun phrases, cut filler clauses.")
    if diag["flesch"] is not None and diag["flesch"] < diag["floor"]:
        tip.append("The text is still too dense. READABILITY comes from plain WORDS, not short sentences: "
                   "swap long/technical terms for everyday ones (\"set up\" not \"implementation\", \"build\" not "
                   "\"architect\", \"slows down\" not \"degrades throughput\"), and write connected 14-20 word "
                   "sentences with variation — do NOT fragment into choppy one-liners. This is a vocabulary fix.")
    if diag.get("long_word") is not None and diag.get("long_word", 0) > 35:
        tip.append("Too many long words — replace them with short, common equivalents to raise readability.")
    if diag.get("primary_keyword") and diag.get("keyword_count", 0) >= 3:
        tip.append(f"KEYWORD STUFFING: repeat '{diag['primary_keyword']}' AT MOST 2-3 times in the whole body. "
                   "Let the title/meta/H2 carry it. Everywhere else rephrase naturally — use pronouns, "
                   "'these systems', 'MCP servers', or the topic itself. Never write the keyword verbatim more "
                   "than twice in prose.")
    if any("Smart Brevity: header > 6 words" in w for w in diag.get("warnings", [])):
        tip.append("SMART BREVITY HEADERS: Shorten H2/H3 section headers to 6 words or fewer.")
    if any("Smart Brevity:" in w and "paragraph(s) > 3 sentences" in w for w in diag.get("warnings", [])):
        tip.append("SMART BREVITY PARAGRAPHS: Keep every paragraph to 1-3 sentences maximum. Split monolithic blocks.")
    if any("no bold context signposts found" in w for w in diag.get("warnings", [])):
        tip.append("SMART BREVITY SIGNPOSTS: Include bolded context guide words (e.g. **Why it matters:**, **The big picture:**, **Where this bites:** / **What I'd watch:**, **The catch:**).")
    if tip:
        notes.append("HOW: " + " ".join(tip))
    if extra:
        notes.append("STRUCTURE/FORMAT:")
        notes += [f"- {x}" for x in extra] if isinstance(extra, list) else [f"- {extra}"]
    feedback = "\n".join(notes)
    return (base_prompt
            + "\n\n--- PREVIOUS ATTEMPT (this version FAILED the accessibility gate) ---\n"
            + prev_text
            + "\n\n--- REVIEWER FEEDBACK ---\n"
            + feedback
            + "\n\nRewrite the ENTIRE article to fix every FAILURE and ADVISORY above. Do not reuse "
              "the previous attempt unchanged. Preserve all facts, every [n] citation, and the "
              "## Sources list VERBATIM. Return the full article in the same OUTPUT FORMAT.")

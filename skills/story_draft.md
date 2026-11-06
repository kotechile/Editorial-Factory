# SKILL: Story Draft (Structural First Pass)

## 1. Objective
Assemble the verified brief into an authoritative structural draft using **only** the VERIFIED
evidence set. No new facts. Provide clear inputs for the Stylist's Smart Brevity rewrite.

## 2. The house structure

The order below **is** the contract (`scripts/readability_critic.py` holds it at the push): the
executive summary primes the reader at the top instead of repeating itself at the bottom. A piece
whose parts are all present but in the old order (summary last) fails the gate.

| # | Section | Rule |
|---|---|---|
| 1 | **Title** | A headline that earns the click, scored by `scripts/headline_score.py` (owner's standard, 2026-10-10) and gated at the push — **for articles from 2026-10-10 on: earlier headlines are grandfathered and only reported, never re-cut** (`ENFORCED_FROM`). **Core headline ≤ 6 words** before any colon/dash subtitle, whole title ≤ 10 words and ≤ 60 characters, **never open on "The/A/An"**, front-load the strongest noun or the most concrete benefit, carry a hook (a curiosity gap or loss aversion — the mistake, the trap, the silent cost — or invert the conventional wisdom), anchor on a figure the article itself states (never invented), and call the reader out ("your/you", or a named role/subject: CFO, shipper, homeowner, SpaceX). The strongest headlines in the corpus read *"California FAIR Plan Premiums Jump 29.1%"*, *"Why 70% of Startup Options Go Unexercised"*, *"Nearshoring Doesn't Move the Trade Case"*; the weak ones are 11–17 words, open on "The", and state a fact with no reason to open it. No bait-and-switch: the article must satisfy the title in its first paragraph. When drafting for an SEO keyword (`primary_keyword:` in frontmatter), the title MUST contain the target keyword. For **Synthesis articles**, the collision thesis goes in the subtitle, not by stacking both clauses into the headline. |
| 2 | **Lede (paragraph 1)** | The core thesis **and its operational impact** in plain, concrete English, in the first sentence. A concrete incident or figure from the evidence delivers the news; the same paragraph says what it changes for the reader. Not a definition, not a "world is changing" opener, no heading before it. For **Synthesis articles**, write a **Collision Lead**: bridge the two underlying developments in the first 1–2 sentences (e.g., *"As frontier model inference prices plunge past 80% cuts, enterprise engineering teams are quietly turning their backs on off-the-shelf SaaS to build bespoke in-house software."*). |
| 3 | **At a Glance** (`<!-- tldr -->`) | **Immediately below the lede**, never at the foot of the piece. `## At a glance` + three lines, **≤50 words total**: `- **The shift:**` (one sentence — what changed), `- **The number:**` (the one figure that proves the thesis and that the body already states), `- **The risk:**` (the single operational consequence). It primes the reader; it never re-lists the watch items below. |
| 4 | **Chronological context** (`<!-- tension -->`) | Paragraph 2 states the timeline **once**, in strict chronological order — **initial event → initial deadline → current extension** — then the mechanism (the systemic reason it is happening now, who it hurts and who it helps). An H2 in this article's own words; "The big picture:" is the fallback label, not the required one (owner, 2026-11-03). In a synthesis piece, explain the friction point where Trend A alters the economics, reliability or feasibility of Trend B. |
| 5 | **By the numbers** | **Kept, but small** (owner, 2026-11-03: the block is what a reader scans; removing it loses the page). `## By the numbers` H2 with **2–3 bold bullets**, placed **after the mechanism has been explained** — never before the reader knows what is being counted. One metric per bullet, one sentence, **25 words or fewer**, formatted `- **<figure> <noun phrase>:** <one plain clause> [n]` (see §3.5). In synthesis articles the figures must still come from **both** underlying anchors. |
| 6 | **What to watch** (`<!-- tactical-insight -->`) | Operational caveats and forward-looking triggers: what the people closest to the story are doing, what the consequences land on, which signal answers the open question next — reported, never prescribed (`persona:` from `context/personas.json`). Write it as prose; bullets only for a real list of comparable items. Header in this article's own words ("Where this bites:" / "What I'd watch:" are fallbacks). Never instruct the reader (`skills/claude_humanizer.md` §3.9). |
| 7 | **The catch** (`<!-- nuanced-takeaway -->`) | The honest limitation or counter-argument, **self-contained**: the final sentence may not introduce a regulatory rule, a billing mechanism, an internal cross-link or a technical concept the piece has not already explained. If it has to name one, give it a 5–10-word inline bridge in the same sentence (*"under federal demurrage billing rules, the two 30-day dispute clocks…"*). Ends on substance, not a cheerlead. |
| 8 | **Related reading & Sources** | Footer, generated at persistence (`<!-- internal-links -->`, `## Related reading`) and copied verbatim (`## Sources`). Render sources as a **vertical list** (`1. <publisher> — <url>` per line), never one run-on paragraph. |

**Story first (owner, 2026-11-03).** The house structure is five marked sections, not five labels.
A reader should be able to follow one argument from the first sentence to the last; the markers,
the fixed signposts and the stat block are machinery, and machinery that shows is the defect. Three
consequences: (1) **a section may be three connected sentences** where a bullet list would have been
— bullets are for a real list, not the default shape of a section; (2) **the header says what the
section argues**, in this article's words; (3) **the numbers block stays, sized to its job** — 2–3
bullets of figures the prose does not restate, never a four-bullet recap and never nothing at all.

The **TOC is render-time only** — the site derives it from the section headings. Never write a
"Table of Contents" into the article body.

## 3. Rules
- Inline citations: every factual sentence carries `[n]` mapping to a source list at the end.
- **Place ONE earned inline internal link in the draft, from `context/internal_links.json`, and verify it
  resolves before Loop 3.** `scripts/article_shape.py` hard-fails a body with zero inline internal links
  (the generated Related-reading block does not count), so a draft that leaves linking entirely to the
  persistence pass is HELD AS A DRAFT at the push — and the pre-publish gate's single rewrite then
  supplies the link by invention: observed 2026-10-27, `/workstation-compute-economics/local-llm-hardware-sizing/`
  inside a second-person sentence, a URL no front serves. Pick a candidate the index marks `live` on
  the destination front, justify it on the destination's own category hub or ≥ 2 shared subject tokens,
  write it as a **markdown link with anchor text** — `[Planning tools buy capability, not autonomy](/planning-ai-buys-capability-not-autonomy/)`,
  site-relative — and `curl -s -o /dev/null -w '%{http_code}'` it, keeping the sentence an
  observation. **A bare parenthetical path (`(/some-slug/)`) does not count:** `article_shape._LINK_RE`
  only matches `[text](/path)`, so a draft written that way passes a human read, passes
  `check_accessibility`, passes `check_social_voice`, and then `publish_gate` holds the push with
  "the body carries no inline internal link" (learned 2026-10-27). The `<!-- internal-links -->` block
  stays the persistence pass's job; this is the one body link.
- One length: the long-form draft. Do NOT write a LinkedIn/social variant — that channel was
  removed on 2026-10-06 (`skills/publisher.md` §3).
- **SEO frontmatter is optional to author and never invented:** if the brief carries a keyword set, write `meta_title` (≤60 chars) and `meta_description` (140–160 chars) grounded in the article's own headline and lead; if you have neither, omit the keys. The persistence pass derives both from your headline and lead paragraph (`scripts/article_assets.py`) so the CMS excerpt and the frontends' `<meta name="description">` are never empty — do not pad them with claims the article does not make.
- Any claim not in the brief is written as `[NEEDS-SOURCE]` and returned to the verifier — never filled with invention.
- Match the target reader's level from `context/personas.json` for the vertical (`persona:` in frontmatter).
- **`## By the numbers` is mandatory and small:** 2–3 scannable bullets, placed after the mechanism, each in the §3.5 shape — `- **<the anchor figure and its noun>:** <one clause that says what it counts> [n]` (e.g. `- **85% of Long Beach cargo:** The volume handled by the eight terminals where 250 watchmen could walk out [3].`). Never start a bullet with narrative filler ("Diesel fuel started the year…", "The leap in the…"), never put two statistics in one bullet, never a bullet over 25 words. The lead-in's bold text is what an automated SVG chart prints as its axis label, which is why it must be one metric.
- **Observer voice (gated):** the body is a comment on the news, not a verdict and not a playbook:
  each interpreting section (`<!-- tension -->`, `<!-- tactical-insight -->`, `<!-- nuanced-takeaway -->`)
  carries a first-person observer cue, opinion is labelled as opinion, and the tactical section reports
  what the people closest to the story are doing instead of instructing the reader
  (`skills/claude_humanizer.md` §3.9, enforced by `verify.sh` §9).
- **Synthesis Frontmatter (gated):** when the angle brief says `Angle Type: Synthesis`
  (`skills/virality_judge.md` §2.5), the draft **must** carry both keys or `verify.sh` §8 fails the
  build:
  ```yaml
  synthesis: true
  sources:
    - <Signal A's primary anchor URL>
    - <Signal B's primary anchor URL>
  ```
  Inline form (`sources: [<url>, <url>]`) is accepted, and the anchors must be traceable to the
  matching `_signals.md`. This flag is what marks the article as a fusion on the dashboard's own
  surfaces (`/api/articles.json`, the article page badge) — an unflagged synthesis publishes as a
  single-signal story.
- **At a Glance (TL;DR) Schema — a 50-word box under the lede, not a second summary (owner standard 2026-10-29; position 2026-11-06):**
  1. `**The shift:** <what changed, in one sentence>`
  2. `**The number:** <the one figure that proves it — and that the body already states>`
  3. `**The risk:** <the single caveat a reader must carry away>`
  Under 50 words total, no bullet list mirroring **What I'd watch**, and no figure the body does not carry. The old 4-part breakdown (Big Shift / Why It Matters / What I'd Watch + sub-bullets / The Catch) is retired: it duplicated the tactical section and every watch item arrived twice on one page.
- **Renaming the slug mid-run orphans the old draft, and the voice gate reads every file in
  `context/drafts/`.** Changing a working title after the first draft leaves
  `YYYY-MM-DD_<old-slug>_draft.md` behind beside the new one; `check_social_voice.mjs` walks the
  directory, `verify.sh` §9 counts its problems against the repo, and any step globbing `*_draft.md`
  can pick the wrong file. Write the new file, confirm it exists, then delete the superseded path by
  exact name — never assume a rename removed it.
- **Diction standard (owner, 2026-10-29) — the failure the recaps fix cannot see.** A draft can clear
  Flesch 50, both gates and the citation floor and still be hard to read, because the damage is in the
  nouns: a method described as a riddle, a standard term swapped for a metaphor, a taxonomy renamed
  mid-piece. Five rules, and the full wording lives in `skills/claude_humanizer.md` §3.5:
  (1) **name the method and its purpose** — "Croston's method, trimmed by the SBA bias factor", never
  "a two-parameter estimate with the fix at half the smoothing constant"; (2) **use the exact error and
  policy nouns** — *point-forecast accuracy*, *percentage error (MAPE)*, *upward bias*, *fill rate
  target*, never "an accuracy goal can grab" or "that grip is weak"; (3) **lock the taxonomy** — once the
  piece names its grid (smooth, erratic, intermittent, lumpy), those words name those cells for the rest
  of the article, and any other noun says which cell it maps to; (4) **no invented slang** ("the segment
  pass", "the budget talk", "the desk's own") and **no arithmetic narration** ("28,903 minus 1,994" →
  "the other 26,909, about 93%"); (5) **name the authorities in the prose** (Kourentzes, Makridakis,
  Syntetos and Boylan), never "a forecasting expert" or "a later paper". Applies to drafts written from
  this date; published articles are grandfathered.
- **Budget the figure load, not only the figure count (owner, 2026-11-03).** A piece can clear Flesch
  60 and still read as a worksheet, because a digit is a short, easy word: measured across the 269
  published artifacts, the median share of *prose* sentences carrying a figure was 41% and 95 sat
  above 45% (the worst at 89%). `check_accessibility.figure_load` now reports it as an advisory above
  45%. Two drafting consequences: (1) each paragraph carries one figure plus a sentence with no
  digits that says what it means — the reader needs the meaning, not the next step of the division;
  (2) **a figure must say what it is measured against in the same sentence.** A wage that stands in
  for the reader's own hour ("if your hour is worth what the work pays…") is an assumption and must
  be written as one; a wage that prices a third party's paid work is self-evident and needs no
  clause. Full wording in `skills/claude_humanizer.md` §3.5. Applies to drafts from this date.
- **Pre-tune the draft before Loop 3 — both gates, not just accessibility.** Run
  `python3 scripts/readability_critic.py --check <draft>` **and**
  `python3 scripts/check_accessibility.py <draft>` on the structural draft you just wrote. The critic
  holds the deterministic half at the push (At a glance under the lede, one metric per bullet, one
  citation tag per sentence, `## Sources` as a vertical list) and prints the prose advisories
  (read-twice, repeated dates, cold closing) — fix them now, because the reviewer's rewrite is graded
  against the same checks. A draft that
  already clears the Flesch floor (~50) and carries a first-person observer cue in every interpreting
  section converges the frontier rewrite in ~2 attempts; a dense draft burns 4–5 attempts and then needs
  a hand-tune anyway (`skills/claude_humanizer.md` §7–§8). **Readability is a WORD-CHOICE lever, not a
  sentence-length one: swap long technical words for everyday ones at drafting time — do NOT split
  sentences to move the Flesch score.** Splitting buys a couple of points and costs the rhythm: the
  2026-10-22 audit found drafts arriving at a 14-word average with a fifth of sentences at eight words
  or fewer, so every pass after it inherited staccato. Write connected sentences of roughly 14–22 words
  with deliberate variation, let one sentence carry a cause and its consequence, and keep at most one
  eight-word-or-fewer sentence per paragraph. Never drop a figure, a name or a citation to fit that.
  **Paragraphs run 3–5 sentences and never more than 6** (owner decision 2026-10-26; the old 1–3 cap
  measured 3.6 sentences a paragraph on published work and was the thing flattening the argument).
  Depth comes from sentences per paragraph, not from longer sentences: the same piece at 26.8 words
  a sentence scored 51.9 and read thinner than the 17.8-word version at 5-sentence paragraphs.
  **Gloss every specialist term in place while drafting** — `skills/executive-editor.md` carries the
  standard and the term table, and `scripts/check_accessibility.py` hard-fails at publish on an
  unglossed term from that table (F1, dedupe, classifier, test set, synthetic data, embedding,
  cosine similarity, KV cache, fine-tuning, precision/recall, p50–p99) plus the metric shorthand the
  ALL-CAPS acronym rule cannot see. Terms outside the table still have to be glossed on the way in —
  nothing downstream catches "call site", "ratchet", "Btu" or "goods-receiving". The gloss goes at
  first use, inside that sentence; a glossary at the end does not count.
- **The title's content words must appear verbatim (substring) in the first ~600 words — inflections do not count (learned 2026-10-14).** `headline_score.lead_delivery`/the honesty rule checks each title content word as a plain substring of the opening: a title reading "Why Your Card **Serves** 1.6" scores 100 STRONG standalone but reports `lead_ok: False` when the lead says "**served** about 1.6 requests a second", and the pre-publish gate will then re-cut the headline. Write the lead in the title's own inflection ("one card **serves** about 1.6 requests a second") or check with `python3 -c "import sys,headline_score as hs; print(hs.score('<title>', body=open('<draft>').read()))"` before the accessibility gate. Up to `max(1, len(content_words)//3)` of them may be absent, so one missing word clears — every additional one re-cuts the title.
- **Budget every figure across sections while drafting — `article_shape` allows one money figure in at
  most two of the five sections, and the headline's own figures must sit in the lead (learned 2026-10-30).**
  A title that names two figures forces both into the lead, so a third mention anywhere (a numbers bullet,
  the catch) reds the shape gate with "restated in 3 sections", and the first build of an iPhone
  fee-schedule piece failed it on three figures at once ($999 in lead + numbers + catch, $99 in lead +
  tension + numbers, $1,499 in tension + numbers + catch). The repair is not to weaken the lead: give each
  numbers bullet a *different* figure from the same source (the `$99` insured fee moved to the lead and the
  bullet took the `$19` cover-layer fee instead) and refer to a figure already spent by name, not by number,
  in later sections. Map the figures to sections before writing, not after the gate.
- **Observer cues need a first-person verb, not a first-person pronoun (learned 2026-10-30).**
  `check_social_voice.mjs` matches `I` followed by a verb, plus its labelled-opinion and attention families,
  so "What gives me pause is…" and "The strongest objection is…" both fail while reading exactly like a
  cue. Write "What I find hard to square is…" or "The part I keep circling is…".
- Use the section markers below **verbatim** — the Stylist iterates per section and `verify.sh` checks them.
  **A draft must emit `<!-- tldr -->` itself (learned 2026-10-14).** The marker set is gated on the *draft*
  file as well as the `_final.md`, and the Loop 3 rewrite adds the `<!-- tldr -->` marker it needs on the way out —
  so a draft written without it fails `verify.sh` §2 at line 1 while every downstream stage looks green and the
  published artifact is clean. The five markers are `<!-- lead -->`, `<!-- tension -->`, `<!-- tactical-insight -->`,
  `<!-- nuanced-takeaway -->` and `<!-- tldr -->`; check them with
  `grep -o '<!-- [a-z-]* -->' <draft>` before running the accessibility gate, not after the push.

### 3.5 Readability law (owner, 2026-11-06) — every sentence parses on the first read

A draft can clear Flesch 60, keep every citation and still be hard to read, because the damage is in
the grammar and the arithmetic of the argument, not in the word length. Four rules, all of them
checked by `scripts/readability_critic.py` (structure/bullets/citations hold the push; the prose
findings go back through the rewrite):

**A. Never trade clarity for a clever parallel.** Abstract symmetry is banned — a sentence whose
appeal is its shape rather than its meaning. Banned in practice: *"a gate is one shared function
rather than a share of one"*, *"the notice runs deeper into its stay than the window is long"*, *"a
price is what you pay, a cost is what you keep"*. Required: **subject → active verb → concrete
object**, with the consequence in the same sentence. *"A walkout by 2% of the workforce still freezes
100% of the cargo at those eight terminals, because you cannot run a terminal with a closed gate."*
If a sentence has three prepositional phrases in a row (*"the fee on the rate for the box in the yard
at the gate"*), it is a riddle: rewrite it as two short facts.

**B. State the timeline once, then speak in windows.** The dates, the extension and the countdown
math belong in one place — paragraph 2 — in strict order: **initial event → initial deadline →
current extension**. After that, refer to the operational window (*"the 12-day window"*, *"before
Wednesday's deadline"*) and never re-explain the calendar. Never open a paragraph on an ambiguous
relative day (*"At 5 p.m. on Wednesday…"*) before the calendar date has been established somewhere
above it.

**C. Keep domain terms exact, and gloss them in place.** Industry jargon gets a short appositive at
first use, and a standard metric is never redefined to fit a metaphor. *Terminal dwell time* is the
time an import box sits on the dock waiting to depart — never "a round-trip retrieval cycle". *Point-
forecast accuracy* stays point-forecast accuracy. If the source names the method, use the source's
name (**Croston's method, trimmed by the SBA bias factor**), not a picture of it.

**D. No cold concept in the closing.** Never introduce an unexplained regulatory rule, billing
mechanism or technical concept in the final paragraph. If the closing sentence has to reference one
— an external rule (*"the two 30-day clocks on a late container's bill"*) or an internal cross-link —
carry a **5–10-word inline bridge** in the same sentence: *"under federal demurrage billing rules,
the two 30-day dispute clocks…"*. The same rule applies to any term the body introduced only in
passing.

**Citation hygiene — one tag per sentence, linked where the reader will look.** Preferred (digital
readability): convert bracketed footnotes into clean inline links anchored to the publication or the
document — *"according to the [ports' daily rail reports](url)"* — with the `## Sources` list kept as
the record. If the schema requires bracketed tags: **at most one `[n]` per sentence**, consolidated
to the most primary source for that claim, and the `## Sources` footer as a **vertical list**
(`1. <publisher> — <url>` on its own line), never one run-on paragraph. Two tags on one sentence is a
gate failure; three is a research note.

**Bullets — one metric each.** In `At a glance` and `By the numbers`, every bullet is **one sentence,
25 words or fewer, one statistic**: `- **85% of Long Beach cargo:** The volume handled by the eight
terminals where 250 watchmen could walk out [3].` Never the old packed form (`- 85% — Long Beach
cargo behind eight gates: the 250 watchmen who could walk out are about 2% of the ILWU workforce
[3].`), which asks one line to carry a share, a headcount and a comparison at once.

**The four checks before you hand the draft over** (the same ones the critic runs):

1. **Read-twice test** — flag and rewrite any sentence with three prepositional phrases in a row, or
   an abstract comparison of the shape "more X than Y is Z".
2. **Timeline audit** — count every calendar date. If the same date or date pair is explained more
   than once, strip the repeats and use the window.
3. **Bullet density** — every bullet in `At a glance` and `By the numbers` is a single sentence under
   25 words, carrying one metric.
4. **Closing hook audit** — the final paragraph contains no undefined noun and no orphan reference.

## 4. Output schema
`context/drafts/YYYY-MM-DD_<slug>_draft.md` — the order below is the gate's order:
```markdown
---
title: <short punchy initial headline>
vertical: <id>
kind: news            # news | evergreen | review — what the CMS push TAGS the post with
persona: <id from context/personas.json>
one_big_thing: "<single most important takeaway or decision>"
date: YYYY-MM-DD
slug: <slug>
# Synthesis articles only (Angle Type: Synthesis — see §3, gated by verify.sh §8):
# synthesis: true
# sources:
#   - <Signal A's primary anchor URL>
#   - <Signal B's primary anchor URL>
# Optional external links:
# article_url: https://pressflow.io/articles/... (or external illustrated post)
# promo_url: https://factory.example.com/tools/... (e.g. software factory tool)
# promo_label: "🛠️ Try the tool:"
---

<!-- lead -->
<core thesis AND its operational impact in sentence 1 — concrete, plain, no heading>

<!-- tldr -->

## At a glance

- **The shift:** <one sentence: what changed>
- **The number:** <the one figure that proves it, already stated in the body>
- **The risk:** <the one operational consequence>
<!-- the whole box is 50 words or fewer -->

<!-- tension -->

## <a header that says what this section argues>

<paragraph 2: the timeline ONCE — initial event → initial deadline → current extension — then the
mechanism: why now, who it hurts, who it helps>

## By the numbers

- **<figure> <noun phrase>:** <one clause saying what it counts> [1]
- **<figure> <noun phrase>:** <one clause saying what it counts> [2]

<!-- tactical-insight -->

## <what to watch>

<the operational caveats and the forward triggers — reported, never prescribed>

<!-- nuanced-takeaway -->

## The catch

<the honest limitation / counter-argument — self-contained, no cold concept in the last sentence>

## Sources

1. <publisher/author, "title", date> — <url>
2. <publisher/author, "title", date> — <url>
```

## 5. Failure handling
Draft thinner than ~800 words despite a full brief → the brief is under-sourced; return to the
verifier, not to padding. Log the gap to `skills/self_improvement_eval.md`.


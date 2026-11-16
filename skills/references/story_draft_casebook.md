# Story Draft — Casebook

Reference for `skills/story_draft.md`: the headline post-mortems, figure-budget and voice failures,
link invention, slug orphaning, and the full text of the readability and diction law that the skill
file now only summarises. Every block below is quoted verbatim from the skill file as it stood before
the compression, so each rule keeps its exact wording and the incident that produced it.

**Read it** when a gate holds a draft (shape, headline, voice or figure restatement), when a headline
is re-cut at the push, when hand-repairing a draft before Loop 3, or when a rule looks newer than the
article you are fixing. Sections: the corpus headline examples · the "story first" rationale · the
numbers-block chart collision · the At-a-glance schema history · slug orphaning · the diction standard
with its banned examples · figure load · the pre-tune block and its rhythm audit · title content words ·
the section figure budget · observer cues · the full marker set · the full §3.5 and §3.6.

---

## Corpus headline examples (removed from the Title row)

The strongest headlines in the corpus read *"California FAIR Plan Premiums Jump 29.1%"*, *"Why 70% of Startup Options Go Unexercised"*, *"Nearshoring Doesn't Move the Trade Case"*; the weak ones are 11–17 words, open on "The", and state a fact with no reason to open it.

---

**Story first (owner, 2026-11-03).** The house structure is five marked sections, not five labels.
A reader should be able to follow one argument from the first sentence to the last; the markers,
the fixed signposts and the stat block are machinery, and machinery that shows is the defect. Three
consequences: (1) **a section may be three connected sentences** where a bullet list would have been
— bullets are for a real list, not the default shape of a section; (2) **the header says what the
section argues**, in this article's words; (3) **the numbers block stays, sized to its job** — 2–3
bullets of figures the prose does not restate, never a four-bullet recap and never nothing at all.

---

### 3.5 Readability law (owner, 2026-11-06) — every sentence parses on the first read

---

A draft can clear Flesch 60, keep every citation and still be hard to read, because the damage is in
the grammar and the arithmetic of the argument, not in the word length. Four rules, all of them
checked by `scripts/readability_critic.py` (structure/bullets/citations hold the push; the prose
findings go back through the rewrite):

---

**A. Never trade clarity for a clever parallel.** Abstract symmetry is banned — a sentence whose
appeal is its shape rather than its meaning. Banned in practice: *"a gate is one shared function
rather than a share of one"*, *"the notice runs deeper into its stay than the window is long"*, *"a
price is what you pay, a cost is what you keep"*. Required: **subject → active verb → concrete
object**, with the consequence in the same sentence. *"A walkout by 2% of the workforce still freezes
100% of the cargo at those eight terminals, because you cannot run a terminal with a closed gate."*
If a sentence has three prepositional phrases in a row (*"the fee on the rate for the box in the yard
at the gate"*), it is a riddle: rewrite it as two short facts.

---

**B. State the timeline once, then speak in windows.** The dates, the extension and the countdown
math belong in one place — paragraph 2 — in strict order: **initial event → initial deadline →
current extension**. After that, refer to the operational window (*"the 12-day window"*, *"before
Wednesday's deadline"*) and never re-explain the calendar. Never open a paragraph on an ambiguous
relative day (*"At 5 p.m. on Wednesday…"*) before the calendar date has been established somewhere
above it.

---

**C. Keep domain terms exact, and gloss them in place.** Industry jargon gets a short appositive at
first use, and a standard metric is never redefined to fit a metaphor. *Terminal dwell time* is the
time an import box sits on the dock waiting to depart — never "a round-trip retrieval cycle". *Point-
forecast accuracy* stays point-forecast accuracy. If the source names the method, use the source's
name (**Croston's method, trimmed by the SBA bias factor**), not a picture of it.

---

**D. No cold concept in the closing.** Never introduce an unexplained regulatory rule, billing
mechanism or technical concept in the final paragraph. If the closing sentence has to reference one
— an external rule (*"the two 30-day clocks on a late container's bill"*) or an internal cross-link —
carry a **5–10-word inline bridge** in the same sentence: *"under federal demurrage billing rules,
the two 30-day dispute clocks…"*. The same rule applies to any term the body introduced only in
passing.

---

**Citation hygiene — one tag per sentence, linked where the reader will look.** Preferred (digital
readability): convert bracketed footnotes into clean inline links anchored to the publication or the
document — *"according to the [ports' daily rail reports](url)"* — with the `## Sources` list kept as
the record. If the schema requires bracketed tags: **at most one `[n]` per sentence**, consolidated
to the most primary source for that claim, and the `## Sources` footer as a **vertical list**
(`1. <publisher> — <url>` on its own line), never one run-on paragraph. Two tags on one sentence is a
gate failure; three is a research note.

---

**Bullets — one metric each.** In `At a glance` and `By the numbers`, every bullet is **one sentence,
25 words or fewer, one statistic**: `- **85% of Long Beach cargo:** The volume handled by the eight
terminals where 250 watchmen could walk out [3].` Never the old packed form (`- 85% — Long Beach
cargo behind eight gates: the 250 watchmen who could walk out are about 2% of the ILWU workforce
[3].`), which asks one line to carry a share, a headcount and a comparison at once.

---

**The four checks before you hand the draft over** (the same ones the critic runs):

---

1. **Read-twice test** — flag and rewrite any sentence with three prepositional phrases in a row, or
   an abstract comparison of the shape "more X than Y is Z".
2. **Timeline audit** — count every calendar date. If the same date or date pair is explained more
   than once, strip the repeats and use the window.
3. **Bullet density** — every bullet in `At a glance` and `By the numbers` is a single sentence under
   25 words, carrying one metric.
4. **Closing hook audit** — the final paragraph contains no undefined noun and no orphan reference.

---

### 3.6 Diction and structure law (owner, 2026-11-07, every vertical) — the reader must not translate your nouns

---

Measured on the live dispatch `your-task-protocol-costs-643-lines`: Flesch 57.8, every citation
resolving, `article_shape` ok — and the owner's verdict was still that the piece is hard to read and
"the image is not describing the content". The cause was vocabulary and shape, not rhythm: a state
variable called *"the fact"*, maintainers called *"hop owners"*, a revision announced as *"the line
moved"*, a heading promising three options that never numbered them, a source block that renders as
one paragraph. `scripts/readability_critic.py` now holds all five (`jargon`, `enumeration`, `matrix`,
`sources` — enforced from 2026-11-07).

---

**A. Name the thing, never a metaphor for it.** If the sentence is about state, say *session state*,
*execution state* or *context payload*; about people, say *systems architects*, *service owners* or
*calling agents*; about a boundary, say *the protocol layer*; about a spec change, name the revision
(*the July 2026 MCP revision*). Banned (hard fail): "the fact" where state is meant, "hop owners", "the
wire", "the line moved/moves/sits". The test is lookup, not taste: a reader who does not know the
writer's shorthand must still be able to follow the sentence.

---

**B. Ground every entity at first mention.** Every protocol, framework, benchmark, tool or metric is
spelled out once, with a 5–10 word functional anchor, at the point it first appears — not in a
glossary, not in the Sources: *"Google's Agent-to-Agent (A2A) protocol gives the receiving agent a
persistent task object"*, *"the line-count tool (cloc)"*. The rule covers alphanumeric tokens
(**A2A**, F1, p95) and lowercase tool names, not only ALL-CAPS abbreviations, and it is the same rule
in both directions (`Expanded Name (ACR)` or `ACR — a phrase that says what it is`). Later uses stay
bare; a dangling *"this one"*, *"that move"* or *"the middle option"* names the noun again.

---

**C. Enumerate what the heading promises.** A heading carrying a count — *"Three Ways to Manage Agent
State"*, *"Two Clocks"* — labels **every** item, in order, at the top of the section: `1. **In-call
round trips.**`, `2. **Server-issued state handles.**`, `3. **Full task protocols.**` Only then does the
prose analyse them. A body that opens on *"the middle option"* while items one and three are never
named is a gate failure, and the reader is the one who pays for it. The count must be a real count: a
heading naming a date or a figure ("2 November Set The Clock", "37 States") promises nothing.

---

**D. Compare in a table, not in a paragraph.** When a piece weighs two or more protocols,
architectures, tools or options across three or more variables (cost, step count, state location,
failure mode, best fit), emit a Markdown matrix **before or inside the synthesis section**, one row per
option, one column per variable. Three or more figure-against-figure comparisons in prose with no table
is a gate failure: `| Pattern | State location | Overhead | Primary failure mode | Best for |`.

---

**E. One architectural idea per clause; 22 words a sentence on average.** If a sentence contrasts two
protocols *and* explains a failure mode, split it into two sentences. The average, not each sentence,
is the target — the fix for a dense body is a plain-word swap and splitting only the sentences over
28 words, never a wholesale chop (`skills/claude_humanizer.md` §3.6).

---

**F. Sources are a list on the page, not in the source.** Every `## Sources` entry carries a list
marker (`- [1] Author, "Title" — url`, one per line). Consecutive `[1] …` lines look like separate
entries in the artifact and render as **one paragraph** in the CMS, which is what the reader gets.

---

- **`## By the numbers` is mandatory and small:** 2–3 scannable bullets, placed after the mechanism, each in the §3.5 shape — `- **<the anchor figure and its noun>:** <one clause that says what it counts> [n]` (e.g. `- **85% of Long Beach cargo:** The volume handled by the eight terminals where 250 watchmen could walk out [3].`). Never start a bullet with narrative filler ("Diesel fuel started the year…", "The leap in the…"), never put two statistics in one bullet, never a bullet over 25 words. **Keep at most one percentage in the block** (lead any other bullet on a bare reading, a dollar figure or a category): `scripts/article_assets.chart_series` takes the first `N%` of each bold lead-in and will otherwise plot two unrelated percentages on one axis — observed 2026-11-07, when a numbers block carrying 32% of foreign filers beside 3.4% of GDP growth emitted a two-bar chart comparing them, and the fix was to re-lead the second bullet ("**One quarter, one driver:**") so the emitter reported "no chart" and left the artifact byte-identical. The lead-in's bold text is what an automated SVG chart prints as its axis label, which is why it must be one metric.

---

- **At a Glance (TL;DR) Schema — a 50-word box under the lede, not a second summary (owner standard 2026-10-29; position 2026-11-06):**
  1. `**The shift:** <what changed, in one sentence>`
  2. `**The number:** <the one figure that proves it — and that the body already states>`
  3. `**The risk:** <the single caveat a reader must carry away>`
  Under 50 words total, no bullet list mirroring **What I'd watch**, and no figure the body does not carry. The old 4-part breakdown (Big Shift / Why It Matters / What I'd Watch + sub-bullets / The Catch) is retired: it duplicated the tactical section and every watch item arrived twice on one page.

---

- **Renaming the slug mid-run orphans the old draft, and the voice gate reads every file in
  `context/drafts/`.** Changing a working title after the first draft leaves
  `YYYY-MM-DD_<old-slug>_draft.md` behind beside the new one; `check_social_voice.mjs` walks the
  directory, `verify.sh` §9 counts its problems against the repo, and any step globbing `*_draft.md`
  can pick the wrong file. Write the new file, confirm it exists, then delete the superseded path by
  exact name — never assume a rename removed it.

---

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

---

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

---

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

---

- **The title's content words must appear verbatim (substring) in the first ~600 words — inflections do not count (learned 2026-10-14).** `headline_score.lead_delivery`/the honesty rule checks each title content word as a plain substring of the opening: a title reading "Why Your Card **Serves** 1.6" scores 100 STRONG standalone but reports `lead_ok: False` when the lead says "**served** about 1.6 requests a second", and the pre-publish gate will then re-cut the headline. Write the lead in the title's own inflection ("one card **serves** about 1.6 requests a second") or check with `python3 -c "import sys,headline_score as hs; print(hs.score('<title>', body=open('<draft>').read()))"` before the accessibility gate. Up to `max(1, len(content_words)//3)` of them may be absent, so one missing word clears — every additional one re-cuts the title.

---

- **Budget every figure across sections while drafting — `article_shape` allows one money figure in at
  most two of the five sections, and the headline's own figures must sit in the lead (learned 2026-10-30).**
  A title that names two figures forces both into the lead, so a third mention anywhere (a numbers bullet,
  the catch) reds the shape gate with "restated in 3 sections", and the first build of an iPhone
  fee-schedule piece failed it on three figures at once ($999 in lead + numbers + catch, $99 in lead +
  tension + numbers, $1,499 in tension + numbers + catch). The repair is not to weaken the lead: give each
  numbers bullet a *different* figure from the same source (the `$99` insured fee moved to the lead and the
  bullet took the `$19` cover-layer fee instead) and refer to a figure already spent by name, not by number,
  in later sections. Map the figures to sections before writing, not after the gate.

---

- **Observer cues need a first-person verb, not a first-person pronoun (learned 2026-10-30).**
  `check_social_voice.mjs` matches `I` followed by a verb, plus its labelled-opinion and attention families,
  so "What gives me pause is…" and "The strongest objection is…" both fail while reading exactly like a
  cue. Write "What I find hard to square is…" or "The part I keep circling is…".

---

- Use the section markers below **verbatim** — the Stylist iterates per section and `verify.sh` checks them.
  **A draft must emit `<!-- tldr -->` itself (learned 2026-10-14).** The marker set is gated on the *draft*
  file as well as the `_final.md`, and the Loop 3 rewrite adds the `<!-- tldr -->` marker it needs on the way out —
  so a draft written without it fails `verify.sh` §2 at line 1 while every downstream stage looks green and the
  published artifact is clean. The five markers are `<!-- lead -->`, `<!-- tension -->`, `<!-- tactical-insight -->`,
  `<!-- nuanced-takeaway -->` and `<!-- tldr -->`; check them with
  `grep -o '<!-- [a-z-]* -->' <draft>` before running the accessibility gate, not after the push.

---

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

---

## The text as it stood — sections the skill now states in condensed form

Each block below was rewritten shorter in `skills/story_draft.md`. The original wording is kept here in full, so a rule's exact phrasing and every example survives the compression.## 4. Output schema
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
```

---

- **The shift:** <one sentence: what changed>
- **The number:** <the one figure that proves it, already stated in the body>
- **The risk:** <the one operational consequence>
<!-- the whole box is 50 words or fewer -->

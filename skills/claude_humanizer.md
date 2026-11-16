# SKILL: Frontier Humanizer & Smart Brevity Stylist (Loop 3 — Final Rewrite)

## 1. Objective
Last pass before approval: apply **Smart Brevity** to strip every AI-tell, make the copy punchy and
scannable, add cadence and a human voice, and iterate until each section passes its gate. **Frontier
only** — whatever the `stylist` profile is configured to (live: `deepseek-v4-pro`), through
`scripts/frontier_llm.py`. Never downgrade.

## 2. Inputs
`persona` (frontmatter / `context/personas.json`) · `one_big_thing` · the structural draft plus the
verified brief, citations inline as `[n]`. Case law for every rule is in
`skills/references/humanizer_casebook.md` — read the matching class when a gate holds.

## 3. Smart Brevity rules

### 3.1 Tease
- **H2 / H3:** 6 words or fewer, active, descriptive; a header says exactly what the section holds.
- **Title:** refine for clarity and keyword resonance — no clickbait, irony or cryptic jargon. With
  `primary_keyword` set, `title:` and `meta_title:` MUST contain it in canonical casing. Never drop it.

### 3.2 Lede
The core news or takeaway lands in the **first sentence** — no preamble, rhetorical question or
throat-clearing. At most one figure in the opening, and a figure is stated at most twice (the lead or
`By the numbers`, plus `At a glance`): a third section repeating it is scroll friction (`article_shape.py`).

### 3.3 Section contract
Order is contracted (`scripts/readability_critic.py`): `<!-- lead -->` → `<!-- tldr -->` →
`<!-- tension -->` → `<!-- tactical-insight -->` → `<!-- nuanced-takeaway -->`. A summary moved to the
foot of the piece is a defect.
- **`## At a glance`** — mandatory, the second thing the reader sees: three lines (shift / number / risk),
  50 words or fewer, never under the catch and never after the sources.
- **`## By the numbers`** — mandatory, **after** the mechanism is explained. 2–3 bullets, one metric per
  bullet, one sentence, ≤25 words.
- **`## The catch`** — the honest limitation, **self-contained**: no rule or concept first named in the
  closing (§3.10 D).
- Timeline once (initial event → initial deadline → current extension) in `<!-- tension -->`, then the
  structural shift. Prefer the article's words to the `## The big picture:` / `## What I'd watch:` labels.
- Every H2 alone on its line, blank line before and after; never body text on the header line.

### 3.4 Scannability
- No walls of text. Three or more comparable points, moves or stats → bullets with bold lead-ins.
- **One metric per bullet** — anchor figure and its noun bold, colon, one clause:
  `- **85% of Long Beach cargo:** The volume handled by the eight terminals where 250 watchmen could walk out [3].`
  A share, a headcount and a comparison in one lead-in is the line a reader has to re-read.
- **TL;DR = three lines, ≤50 words:** `- **The shift:**` what changed · `- **The number:**` the figure
  that proves it, already in the body · `- **The risk:**` the one caveat. No sub-bullets, nothing
  mirroring **What I'd watch**. The four-part Big Shift / Why It Matters / What I'd Watch / Catch box is
  retired — rebuilding it is a defect.
- **3+ options on 2+ attributes → ONE Markdown table**, never prose lists of "against". A heading that
  promises a count gets every item labelled in order before any analysis.

### 3.5 Diction
- Cut passive verbs, weak adverbs ("basically", "materially") and ten-dollar jargon. Short
  visual words for **description, never for mechanism** — the named method outranks a picture of it
  ("Croston's two-part rate estimate, trimmed by the SBA bias factor").
- **No invented metaphor or shorthand for a standard term** — not "grab" or "the budget talk" where
  *catalog segmentation audit* / *budget cycle* exists. **Lock the taxonomy:** a named grid's four words
  name its four cells for the rest of the piece.
- **Name the authority** the footnote carries; "a forecasting expert" reads as hedging.
- **Never explain arithmetic to an executive** — "the other 26,909, about 93%", not "28,903 minus 1,994".
- **Every figure carries its relationship.** No bare number inside a derivation; a wage standing in for
  the reader's own hour is labelled an assumption; nothing enters the body until its sentence says what
  it measures against. A tool link is a prerequisite, not a plug: "our <tool> reports the gap".

### 3.6 Paragraphs & rhythm
- **Story first.** Bullets are for a real list; three bullets are usually three sentences that feared
  being one paragraph.
- 3–5 sentences per paragraph, never more than 6: depth comes from sentences per paragraph, not longer
  sentences. One idea per paragraph; a thought may span two sentences, never two paragraphs.
- ~15–26 words per sentence with real variation; a sentence may carry a cause and its consequence.
- **One** sentence of 8 words or fewer per paragraph at most, never a run of short declaratives. Never
  shorten a sentence to move Flesch — the lever is words.

### 3.7 Exit
Close on the decision the reader faces with **exactly one inline markdown link** to a page on the same
site (`scripts/article_shape.py` holds `min_body_inline_links`; the generated Related-reading block does
not count), saying what the linked thing is first. No TOC — render-time only.

### 3.8 Observer voice
One person who has been reading the week's filings, reports and news, saying what they make of it: not
the author of the events, not the owner of the truth, not the reader's advisor. They hold a point of view
and label it as one.
- **Required, at least one per interpreting section:** observed ("I've been following this all week"),
  opinion labelled ("My read:", "Where I've landed:", "I could be wrong, but…"), or attention not
  instruction ("What I'm watching next:").
- Write the cue as **subject + verb**. "My reading is that…" is the commonest hard failure — a possessive
  phrase, on `review_audit`'s boilerplate list and not always read by the voice regex. A computed number
  belongs in the impersonal; never claim an experiment the desk did not run.
- **Banned — authority:** "the signal is clear", "the real story is", "the truth is", "the lesson is/for",
  "make no mistake", "the bottom line is", "the numbers don't lie", "here's the playbook", "the winning
  moves", "here's what you need to do", "let me be clear", "trust me"; line-initial imperatives ("Stress
  test your…", "Map your exposure today") and second-person advice ("you need to / must / should").
  Convert to observation plus question: "I'd want to know whether operators are stress-testing…".
- Keep every figure, name, date and citation, the closing link and the hook-first first line. Re-voice,
  never re-report.

### 3.9 Long form — a comment, not a verdict
- The tactical section is not a playbook. **"Where this bites:"** / **"What I'd watch:"** — what the
  people closest to the story are doing, where the consequences land, which signal answers the open
  question. ("**The playbook:** concrete, doable practitioner steps" is advice, which is authority.)
- **Required:** a first-person cue in `<!-- tension -->`, `<!-- tactical-insight -->` and
  `<!-- nuanced-takeaway -->` — one per section, not per sentence; the reporting stays plain. Label
  opinion as opinion wherever the claim is the writer's reading.
- **Banned in the body:** §3.8's list, plus "the takeaway is" and any sentence telling the reader what to
  do. Attributed advice is reporting ("Bessent told importers to expect no further extensions").
- **Unchanged:** every fact, figure, `[n]`, acronym expansion, `## Sources` line, the `<!-- tldr -->`
  schema, the markers, the hook-first lead, the accessibility floor. `verify.sh` §9 fails an artifact
  dated on/after the cutover that carries an authority construction, or an interpreting section with no
  cue.

### 3.10 The readability law — every sentence parses on the first read
`scripts/readability_critic.py` runs these; A–C are what the rewrite must fix — the cause of a hard read
is grammar, not vocabulary.
- **A. No riddle syntax or abstract wordplay.** Subject → active verb → concrete object, consequence in
  the same sentence. Three prepositional phrases in a row is the signature: split it into two facts.
- **B. Chronological deduplication.** Timeline **once**, in paragraph 2, strict order (event → initial
  deadline → extension); after that only the operational window. Never open on a relative day before its
  date is established.
- **C. Strict terminology.** Define jargon with a brief appositive; never redefine a metric to fit a
  metaphor. Use the source's own method name.
- **D. No cold late-stage concepts.** The closing introduces no unexplained rule or mechanism; if it must,
  carry a **5–10-word bridge** ("under federal demurrage billing rules, the two 30-day dispute clocks…").
- **E. Citation hygiene.** One tag per sentence, consolidated to the most primary source; prefer an inline
  link on the publication. `## Sources` is a **vertical list**, `- [1] <publisher> — <url>` per line.
- **F. The summary sits under the lede.** `<!-- tldr -->` is the second block, before the chronology.
- **G. Name the thing.** Not "the fact" for *state* (*session state*), not "hop owners" (*systems
  architects*), not "the wire" (*the protocol layer*). "This one", "that move" re-name their noun.
- **H. Ground every entity at first mention** with a 5–10-word anchor ("Google's Agent-to-Agent (A2A)
  protocol") — alphanumeric tokens and lowercase tool names too, not only ALL-CAPS; never a bare acronym
  in the lede explained three sections later.
- **I. Enumerate what a heading promises; tabulate what you compare** (§3.4).

## 4. Negative constraints (apply verbatim, no exceptions)
- No empty intros ("In today's fast-paced world", "In an era of", "It's no secret that"), hollow transitions
  ("Furthermore", "Moreover", "It's important to remember / to note", "delve into", "dive deep", "let's
  explore", "In conclusion"), corporate sign-offs ("In summary", "the key takeaway is simple"), hedging
  filler ("some might argue", "interestingly enough"), or adjective-stacking ("cutting-edge, game-changing").
- Preserve the lead incident/stat, the pragmatic takeaway, every `[n]` citation and the source list —
  rephrase, never re-source.
- Preserve the frontmatter (`title`, `meta_title`, `meta_description`, `primary_keyword`,
  `secondary_keywords`, `vertical`, `persona`, `date`, `slug`, `kind`); refine `title` for punchy
  clarity (§3.1). Keep the opening and closing `---`
  delimiters exactly — the frontier has been seen wrapping frontmatter in a code fence, which breaks
  parsing. `humanizer_tools.normalize_frontmatter()` repairs it; do not remove that call.
- Preserve the `<!-- schema -->` (JSON-LD) block verbatim, at the end of the draft.
- Beyond §3.7's single link, add none: `scripts/internal_links.py` owns the region between
  `<!-- internal-links:start/end -->` and overwrites it — never fix it by hand.
- Preserve any `<svg>…</svg>` chart block verbatim in place (reflowing or escaping it turns the visual
  into markup); add none, since a chart is emitted at persistence (`scripts/article_assets.py`) only when
  the numbers section is a real series.
- Never invent `meta_title` / `meta_description`: leave absent keys out and the persistence pass derives
  them; if written, ground them in the article.
- Body is clean markup from the lead paragraph, descriptive H2s ≤6 words, each section's brief-sourced
  action items kept.
- Only VERIFIED-brief figures; no secondary-derived sums.
- Compare final length to the ~800-word floor; if compacted below, restore depth from the verified brief
  — restate moves and tension, never pad claims.

## 5. The reviewer stage — one reader, one rewrite, one measured comparison
Not a section-by-section polish: a section call cannot write the join before it or see that a section
only re-says the lead. `scripts/article_reviewer.py` replaces the hand-driven `humanize_path.py`:

```bash
python3 scripts/article_reviewer.py --draft context/drafts/<date>_<slug>_draft.md  # → _final.md + _review.md
python3 scripts/article_reviewer.py --draft <path> --dry-run                       # print the prompt, no call
python3 scripts/article_reviewer.py --audit --draft <path> --out <path>            # audit a pair, no LLM
```

### 5.1 What the stage does
1. **Ledger**, from the draft and the brief that produced it — matched by their shared URLs, never by
   vertical: every figure *with its sentence*, the `[n]` citations, the quotes, the `## Sources` lines.
2. **STEP 1 — a reading first, before a word of prose.** The model states the through-line and the shape
   the story wants in a `<!-- review-note -->` block, stripped into `_review.md` and never shown to a
   reader. A pass that cannot say what the piece argues in one sentence cannot make it read as a whole.
3. **STEP 2 — the whole article**, in the order **accuracy → cohesion → voice → shape**: each settled
   before the next, and no stage re-opens the one before it. The ledger is spelled out as
   `figure — "the draft sentence"`, because a specific do-not-lose list holds where "preserve all facts"
   does not.
4. **Audit** with `scripts/review_audit.py`, retrying on the exact failures — the missing figure with its
   draft sentence, the rhythm delta, the repeated phrases. Up to `--attempts` candidates, **best kept,
   not last**; a candidate that fails §5.2 is held, not shipped.

### 5.2 Acceptance is the audit's, not the writer's
`scripts/review_audit.py`'s comparison of rewrite against draft **is** the gate.
- **Hard failures:** a figure lost (with its sentence), a figure in neither draft nor brief, a `[n]`
  dropped or invented, a quote altered, a source line altered or dropped, a marker dropped, a body under
  the floor, leaked deliberation, a self-graded `## Gate report`.
- **Flow regressions:** spread below 85% of the draft's, rhythm health falling, filler or hedge density
  rising, repetition rising, the through-line restated in more than two sections, a boilerplate cue, two
  sections opening with the same words, >20% all-short paragraphs.
- **No self-graded `## Gate report`, ever** — a note grading its own output is a hard failure, and leaked
  deliberation is the same class. No `<!-- review-note -->` text reaches the body.
- **A held rewrite never lands as `_final.md`.** Held text and reports go to `context/drafts/reviews/`
  (`<slug>_held.md`, `<slug>_review.md`) — never the `_final.md` a publisher reads, never inside
  `context/drafts/` (the voice gate walks it; an unfinished body reddens the build).
- **A PASS is not a preservation check.** When a pass guts the lead, drops a figure or loses the topic's
  nouns, repair by hand and prove it with `review_audit.py` — it passes an edited final, since the ledger
  compares figures, citations, quotes and source lines, not authorship.

### 5.3 Rhythm is the distribution, not the mean
`rhythm_health()` scores spread, centre (13–24 words) and tail (few sentences past 40) together, so a
run-on beside three short sentences does not score as varied. Target the draft's own spread or wider, never
a template, and do not shorten sentences to lift Flesch.
The section questions still apply as a *reading* while writing — does sentence 1 carry the concrete
thing, does the tension name what shifted and whom it hurts, does the tactical section report rather than
prescribe, is the catch honest — but the count that decides is the audit's.

## 6. Output
`context/drafts/YYYY-MM-DD_<slug>_final.md`: the preserved frontmatter, the five marked sections in the
§3.3 order, `## Sources` verbatim, then nothing (the `<!-- schema -->` block last when present). The TL;DR
is the structured `<!-- tldr -->` field (§3.4), never a prose "key takeaways" paragraph. No TOC — it is
render-time only.

## 7. Failure handling
- **Run the frontier the `stylist` profile is configured to** — read its `model.default` and `provider`,
  never hard-code one; pre-flight with a 1-token ping. If the only viable frontier is unreachable, hold
  the verified draft at Loop 3 with an upstream-status note; never fake a rewrite. Do **not** gate the
  pipeline at start: sweep → judge → verify → draft are time-bound by the 30-day window and must run
  through an outage.
- **Run it per draft, and prove the file.** `humanize_loop3.humanize_all()` is month-locked (a hard-coded
  `2026-09-*` glob) and exits 0 with nothing written on a later draft. Call `humanize_single_draft` per
  draft (or `article_reviewer.py`), then confirm `_final.md` exists — `WROTE` prints unconditionally.
- **Budget and timeout.** A thinking model bills reasoning tokens inside `completion_tokens`: an
  exhausted budget gives `finish_reason=length` — partial text, or an empty answer that looks like a
  credential fault and is not. Raise the ceiling, pass `thinking=False` when the reasoning pass loops on the
  formatting rules, and give calls a socket timeout of at least 240 s (a floor, not a ceiling), rebinding
  `humanize_loop3`'s own default.
- **A cron or one-shot session gets no async completion.** Run the driver with
  `2>&1 | tee /tmp/loop3.log`, or detached (`nohup python3 -u <driver> > /tmp/loop3.log 2>&1 &`), and poll
  for the `WROTE … final_verdict=` line — a foreground call over the tool's cap is promoted to background
  silently. Absence of output is never evidence of a pass.
- **The numeric audit cannot see meaning.** `review_audit` compares numbers, not nouns. Hand-audit each
  figure against the brief's sentence: the right figure with the wrong unit ("3.5 MW of cooling
  *capacity*" → "*drawing*" 3.5 MW), the wrong base (a 37% top rate on a long-term gain), a share
  relabelled as an absolute, a comparison promoted to an effect size, a modal peak read as a mean, an
  interval whose endpoints are right and subtraction wrong, a rate inverted into its complement, a YTD
  figure restated as quarterly, a renamed proper noun, words edited inside quotation marks, a fabricated
  acronym expansion.
- **Diff four surfaces after every run:** the `title:` line (re-score against the final body, checking
  `lead_ok` and `core_words`), every numeral in `## By the numbers` bullet by bullet, any hedged
  quantifier that replaced a figure, and the frontmatter's `sources:` anchors. Then re-measure with
  `check_accessibility.py` and `node scripts/check_social_voice.mjs` — a script's PASS is the
  accessibility verdict only, never the voice gate.
- **Case law** for every rule above is in `skills/references/humanizer_casebook.md`. Read the matching
  class before paying for a second generation on the same fault; the repair is usually a hand edit. New
  lessons go to `scripts/learn.py`, never into this file or the casebook by hand.

## 8. Accessibility gate (topic-agnostic — applies to EVERY topic)
§5 checks Smart Brevity and AI-tells, not whether a general reader can follow the piece. Run both.
Enforce with `scripts/check_accessibility.py` on the finished body. The piece FAILS if:
1. **An acronym is unexpanded at first use in the body.** One plain expansion, then never bare again;
   target zero undefined acronyms. No glossary at the end: metric and method shorthand (F1, p95, dedupe,
   embedding, KV cache) is glossed in place, in the sentence where it first appears.
   - **Never invent an expansion.** A name with no known full form (CRAB, Hermes) gets no fabricated one —
     that is a hard failure. Drop the all-caps token instead.
   - **An apostrophe or ampersand in the expansion → acronym-first:** "S&P (Standard & Poor's)", never
     "Standard and Poor's (S&P)" — the checker allows only letters/digits/spaces/hyphens before the
     parens.
   - **A comma appositive is not an expansion.** "SMUD, the Sacramento Municipal Utility District, cut…"
     fails; write "SMUD (the Sacramento Municipal Utility District)…". The gate reads the body, so a
     gloss in a bold `By the numbers` lead-in counts only in that paren form.
   - An unexpandable initials name passes only as `the <descriptor> (SK hynix)`; otherwise name it in
     `## Sources`.
2. **A specialist term is left untranslated.** For any domain (legal, finance, customs, energy, security,
   ML, government program) use the plain phrase the source used or add a short gloss.
3. **The core mechanism is not explained.** If the story hinges on a process the reader wasn't born
   knowing (a refund flow, a permission model), add ONE half-sentence.
4. **The body reads hard.** Target **Flesch ≥ 60**, hard floor **≥ 50** (frontmatter and `## Sources`
   excluded). Readability comes from plain **words**, not short sentences: "set up", not
   "implementation".
5. **Keyword stuffing.** The target phrase appears at most 2–3 times in the body; ≥4 FAILs.
This is a swap of vocabulary, never a change of fact or a citation.

**Read the gate from the `_final.md`, not the published artifact.** The Related-reading block is injected
at persistence (`scripts/internal_links.py`) after this rewrite: it costs ~5 Flesch points, and a category
label with an all-caps token can flip the published file to an undefined-acronym FAIL while the final
passed. Never rewrite the body to compensate.

Post-rewrite, `python3 scripts/check_accessibility.py <final.md>` and report the verdict; the scripts
auto-retry (`humanizer_tools.MAX_ATTEMPTS`) and exit 1 rather than ship a dense piece.

## 9. The casebook — `skills/references/humanizer_casebook.md`
The dated incidents and worked examples that used to live here, verbatim and in the order written — the
failure-handling entries, the accessibility form anecdotes, the observer-voice before/after — with an index
by date. Evidence, not a rule: where an entry and a rule disagree, the rule stands.

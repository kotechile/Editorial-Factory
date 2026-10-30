# SKILL: Frontier Humanizer & Smart Brevity Stylist (Loop 3 — Final Rewrite)

## 1. Objective
The last pass before approval. Apply **Smart Brevity** principles to strip every AI-tell, craft punchy
and scannable copy, inject cadence and a genuine human voice, and iterate until every section passes
its own gate. **Frontier model only.** The frontier is whatever the `stylist` profile is configured
to (see §7). Current live config: `gemini-3.1-pro-preview` (`provider: gemini`). Restore Claude/kie.ai
only when a valid key exists — never downgrade to a non-frontier model.

## 2. Required Inputs
To apply Smart Brevity effectively, the styling pass consumes:
1. **Target Audience (`persona`):** Defined in frontmatter / `context/personas.json` (e.g. `infra_engineer`, `eng_leader`).
2. **The One Big Thing (`one_big_thing`):** The single most important takeaway, fact, or decision the reader must remember.
3. **Raw Content / Source Material:** The unedited structural draft and verified brief with inline citations `[n]`.

## 3. Smart Brevity Rules & Architecture

### 3.1 The Tease (Headlines & Section Headers)
- **H2 / H3 Section Headers:** Target **6 words or fewer**. Punchy, active, descriptive.
- **Article Title:** The draft starts with a short title. The Stylist refines or polishes the title based on SEO keyword resonance and clarity without clickbait fluff, irony, or cryptic jargon. When `primary_keyword` is present in frontmatter, `title:` and `meta_title:` MUST explicitly contain the primary keyword (preserving proper/canonical casing, e.g. `<Keyword>: <Hook>`). Never drop, omit, or replace the keyword in the headline.
- **No clickbait or vague abstractions:** Headers tell the reader exactly what is in that section.

### 3.2 The Lede (First Sentence)
- Deliver the primary news or core takeaway immediately in the **very first sentence**.
- Zero throat-clearing, preambles, rhetorical questions, or introductory fluff.
- Tell the reader something essential, concrete, and load-bearing upfront.

### 3.3 Context Signposts & Mandatory H2 Headers
Introduce supporting context using standardized H2 headers (`## `).
**Formatting requirement:** Every H2 header MUST stand on its own separate line, preceded by an empty blank line and followed by an empty blank line. Never place body text or bullets on the same line as the H2 header, and never attach text directly on the line below without an intervening blank line:
- **`## The big picture:`** — Frame the broader industry or structural shift (in `<!-- tension -->`). Followed on a new paragraph by a single direct, declarative sentence.
- **`## By the numbers`** — **MANDATORY H2.** Lead into 2–4 quantitative or benchmark figures, formatted as clean scannable bullets with bold lead-ins pairing the figure with a concise 2–4 word metric title before an em-dash (e.g. `- **88% — Diesel price jump:** ...` or `- **21% to 29.5% — UPS fuel fee:** ...`). Never begin bullet explanations with conversational or background narrative ("Diesel fuel started the year...", "The leap in the..."). State the clean metric title directly so automated SVG charts display meaningful, unclipped labels.
- **`## What I'd watch:`** / **`## Where the money flows`** — Introduce the concrete consequences and the next signals to watch (in `<!-- tactical-insight -->`). Observations, never instructions to the reader (§3.9).
- **`## The catch`** — State the honest limitation, tradeoff, or counter-argument (in `<!-- nuanced-takeaway -->`). Followed on a new paragraph by the honest limitation.
- **`## At a glance`** — Mandatory H2 opening the `<!-- tldr -->` executive summary, clearly separating the 4-part Smart Brevity breakdown so it is NEVER embedded under "The catch".

### 3.4 Scannability & Bullets
- **Never output monolithic walls of text.**
- Any sequence of **three or more** data points, stats, tactical moves, or arguments MUST be broken down into clean, bulleted lists with bold lead-ins (e.g., `- **Audit bandwidth:** Ask vendors for...`).
- **At a Glance / TL;DR 4-Part Smart Brevity Schema:** The `<!-- tldr -->` block must serve as a 30-second executive summary that clearly explains what the article is about, following this structure in plain English:
  1. `- **The Big Shift:**` (or **The Core Story:**) — 1-2 direct sentences explaining the event, breakthrough, or baseline problem and what the article is about.
  2. `- **Why It Matters:**` — 1-2 sentences delivering the economic, architectural, or industry stakes and who is affected.
  3. `- **What I'd Watch:**` — An intro sentence naming what the writer is watching next, followed by indented sub-bullets (`  - **<Thing to watch>:** <1-line plain English definition of what it is and why it matters>`). **The Winning Moves:** / **The Playbook:** are retired (§3.9).
  4. `- **The Catch:**` (or **The Fine Print:**) — 1-2 sentences stating the upfront design needs, security/access controls, and realistic trade-offs.

### 3.5 Strong, Simple Diction
- Strip out passive verbs, weak adverbs (e.g., "basically", "materially", "extremely"), and bloated "10-dollar" corporate jargon.
- Prefer short, single-syllable, visual words that paint a clear picture — **for description, never for mechanism.** A named method, metric or error outranks any picture of it: "Croston's two-part rate estimate, trimmed by the SBA bias factor" beats "a two-parameter rate estimate with the fix at half the smoothing constant", and "point-forecast accuracy" beats "an accuracy goal can grab".
- Translate domain jargon into plain English or add an immediate short parenthetical gloss.
- **Diction standard (owner, 2026-10-29) — the plain-English over-correction is what makes a piece unreadable, and no gate sees it:**
  - **No invented metaphor, slang or shorthand for a standard term.** Banned in practice: "grab", "grip", "hand-me-downs", "the segment pass", "the budget talk", "the desk's own", "quote the sample, not the slogan". Use the industry noun — *catalog segmentation audit*, *software renewal review*, *budget cycle*, *our <tool name>*.
  - **Lock the taxonomy once you name it.** When the piece introduces a classification grid (smooth, erratic, intermittent, lumpy), those four words name those four cells for the rest of the article. "Sparse", "hard groups" or "unscorable" may appear only with the cell they map to.
  - **Name the authority in the prose.** A citation hidden behind "a forecasting expert" or "a later paper" reads as hedging: write the name the footnote carries (Kourentzes, Makridakis, Syntetos and Boylan).
  - **Never explain arithmetic to an executive.** "28,903 minus 1,994" is a defect; state the residue with its share — "the other 26,909, about 93%".
  - **A tool link is a prerequisite, not a plug.** Close on the operational condition: "that baseline is worth measuring before any algorithm is tuned, and our <tool> reports the gap", never "the desk's own calculator".

### 3.6 Paragraph Discipline & Sentence Rhythm
- Keep paragraphs **3 to 5 sentences, never more than 6**. Depth comes from sentences per
  paragraph, not from longer sentences: the same piece at 26.8 words/sentence scored 51.9 and read
  thinner than the 17.8-word version at 5-sentence paragraphs (owner decision 2026-10-26).
- One idea per paragraph — but a paragraph may carry that idea across two sentences. Do **not** split a single thought into two paragraphs.
- Write **connected sentences, ~14-22 words with real variation**. One sentence may hold a cause and its consequence ("X, so Y"; "X: Y").
- At most **one** sentence of 8 words or fewer per paragraph, and never a run of short declaratives. Never shorten a sentence to move the Flesch score — the lever is plain words, and a choppy body scores the same while reading worse.

### 3.7 The Exit ("Go Deeper")
- Conclude cleanly with designated **Go deeper:** references or internal links (`<!-- internal-links -->` and `## Sources`) for readers who want extra nuance without cluttering the main text.

### 3.8 The Observer Voice — Not Authority

**The social variants this section used to govern are gone.** The authored `<!-- linkedin -->` block
and the app-promotion cards (`context/promoted_apps.json`) were removed with the LinkedIn/Reddit
channel on 2026-10-06, so the desk writes no copy for a social platform at all. What survives is the
voice rule itself, applied to the reader-facing article (§3.9) and machine-checked by
`scripts/check_social_voice.mjs` (`verify.sh` §9) against the patterns in `site/social_voice.mjs`.

The speaker is one person who has been reading the week's filings, reports and news and is saying
what they make of it. They did not cause the events, they are not the owner of the truth, and they
are not the reader's advisor: they hold a point of view and they label it as one.

**Required — at least one, ideally two:**
- **Observed it themselves:** "I've been following this all week", "I keep coming back to one number", "The bit that stuck with me:"
- **Opinion labelled as opinion:** "My read:", "What I take from it:", "I could be wrong, but…", "Where I've landed:"
- **Attention, not instruction:** "What I'm watching next:", "The thing I'd want answered:"

**Banned — ownership/authority constructions (they read as the owner of the truth):**
- Verdict framing: "the signal is clear", "the real story is", "the truth is", "the lesson is/for", "make no mistake", "the bottom line is", "the numbers don't lie".
- Consultant framing: "here's the playbook", "the playbook:", "here's what you need to do", "the winning moves", "let me be clear", "trust me".
- Line-initial imperatives and second-person advice: "Stress test your…", "Negotiate the…", "Match your…", "Treat X as a live deadline", "Map your exposure today", "Stop…", "Start…", and "you need to / must / should / have to…". Convert them to observation plus question: "I'd want to know whether operators are stress-testing…", "Curious how others are handling…".

**Keep:** every figure, name, date and citation the article carries; its closing reader link; the
hook-first first line. Never add a fact the article does not carry — re-voice, never re-report.

**Worked example — the 2026-09-26 tariff piece:**
- *Before (authority):* "The signal is clear: CFOs are pricing in a tariff cliff. … Here is the playbook for supply chain leaders: - Stress test your landed costs … - Match your cash posture to your tariff exposure … Treat Jan. 10 as a live deadline. Not a December problem."
- *After (observer):* "I've been following the tariff truce news all week, and one number from the Atlanta Fed stopped me. … My read: that's firms saying out loud that they expect the paused tariffs to come back. … The part I keep circling: hoarding is also just sound liquidity management, so this isn't proof of panic. … I'm curious how ops teams are reading Jan. 10: a real planning deadline, or another date that slips?"

### 3.9 The Long-Form Article — a Comment, Not a Verdict

The article is written by the same person as the social post: someone who has been reading the week's
filings, reports and news, telling you what they make of it. It reports the facts plainly and labels its
reading of them as its reading. It is not the author of the events, not the owner of the truth, and not
the reader's advisor.

**The load-bearing change: the tactical section stops being a playbook.** It was "**The playbook:** —
concrete, doable practitioner steps", which is advice, which is authority. It becomes **"Where this
bites:"** or **"What I'd watch:"** — what the people closest to the story are doing, what the consequences
land on, and which signals answer the open question next.

| Was (authority) | Becomes (observer) |
|---|---|
| "**The playbook:** Supply chain leaders should stress test landed costs." | "Operators are already re-quoting every landed-cost model. I'd want to see the December sourcing numbers before I believed the calm holds." |
| Bullet: "**Match your cash posture** to your tariff exposure. Lean cash + heavy imports = high risk." | Bullet: "The firms with lean cash and heavy imports have the least room — and 70% of them are hoarding refunds as cash." |
| TL;DR: "**The Winning Moves:** Negotiate the retirement match as hard as the stock grant." | TL;DR: "**What I'd Watch:** Whether offers start trading stock for match — the 401(k) is what lets people buy the equity they were given." |

**Required in the body:**
- A first-person observer cue in each interpreting section — `<!-- tension -->`, `<!-- tactical-insight -->`,
  `<!-- nuanced-takeaway -->`: "I've been watching…", "What strikes me here:", "My read:", "I could be
  wrong, but…", "The part I keep circling:", "What I'd watch next:". One per section, not per sentence:
  the reporting stays plain.
- Opinion labelled as opinion wherever a claim is the writer's reading rather than the source's.

**Banned in the body** — the same constructions as §3.8, plus "The lesson is/for", "the takeaway is", and
any sentence that tells the reader what to do. Reported advice is fine when it is attributed and clearly
someone else's: "Bessent told importers to expect no further extensions" is reporting; "Lock in your
suppliers now" is advice.

**Unchanged:** every fact, figure, `[n]` citation, acronym expansion, `## Sources` line, the `<!-- tldr -->`
four-slot schema (with slot 3 renamed), the section markers, the lead's hook-first job, and the
accessibility floor. Re-voice, never re-report.

`scripts/verify.sh` §9 gates both voices: it fails the build when an artifact dated on/after the cutover
carries an authority construction, or when an interpreting section has no observer cue.

---

## 4. Negative constraints (apply verbatim, no exceptions)
- No empty intros: "In today's fast-paced world", "In an era of", "It's no secret that".
- No hollow transitions: "Furthermore", "Moreover", "It's important to remember", "delve into",
  "dive deep", "let's explore", "In conclusion".
- No corporate sign-offs: "In summary", "ultimately, it's about", "the key takeaway is simple".
- No hedging filler: "some might argue", "it could be said", "interestingly enough".
- No adjective-stacking before nouns ("cutting-edge, revolutionary, game-changing").
- Preserve the lead incident/stat and the pragmatic takeaway — rephrase, never re-source.
- Preserve every citation `[n]` and the source list.
- Preserve the frontmatter (including SEO tags `meta_title`, `meta_description`, `primary_keyword`, `search_volume`) and refine `title` for punchy clarity. When `primary_keyword` is defined in frontmatter, `title` and `meta_title` MUST explicitly contain the target keyword — never drop or omit it.
- Preserve the frontmatter's opening and closing `---` YAML delimiters exactly. The frontier has
  been observed wrapping the frontmatter in a triple-backtick code fence (dropping the `---`
  lines), which breaks frontmatter parsing downstream. All three humanize scripts now normalize
  this with `humanizer_tools.normalize_frontmatter()`; do not remove that call.
- Preserve the `<!-- schema -->` (JSON-LD) block verbatim when present, keeping it at the end of the
  markdown draft. The internal-link block is owned by the persistence pass
  (`scripts/internal_links.py`), which replaces the region between its own
  `<!-- internal-links:start/end -->` markers — so do not add links of your own anywhere in the body
  and do not try to fix that block by hand.
- Preserve any `<svg>…</svg>` chart block verbatim, in place: it is generated from the article's own numbers and a rewrite that reflows, re-indents, escapes or drops it turns the visual into a wall of markup. Do not add one either — a chart is emitted mechanically at persistence time (`scripts/article_assets.py`) only when the numbers section is a real series.
- Never invent `meta_title` / `meta_description` if they are absent — leave the keys out and the persistence pass derives them from your headline and lead paragraph (`scripts/article_assets.py`). If you do write them, they must be grounded in the article's own text.
- Ensure the article body is clean markup starting with the lead paragraph and contains descriptive, high-quality `## ` (H2) section headings (target ≤ 6 words).
- Preserve each section's distinct, brief-sourced action items — bulletize them clearly for the target persona.
- Only VERIFIED-brief figures may appear; no secondary-derived sums.
- After the rewrite, compare the final body length to the draft floor (~800 words). If the frontier
  compacted it materially below the floor, restore depth from the verified brief (restate the moves / tension), never pad new claims.

---

## 5. The reviewer stage — read the whole article, write the whole article, prove it

Loop 3 is **one reader, one rewrite, one measured comparison**. It is not a section-by-section
polish: a section call cannot write the join before it, notice that the same definition appeared
three sections ago, or decide that a section only re-says the lead. Cohesion needs one pass holding
the whole document.

Run it with `scripts/article_reviewer.py` (it replaces the hand-driven `humanize_path.py` /
`humanize_one.py` invocation for new runs):

```bash
python3 scripts/article_reviewer.py --draft context/drafts/<date>_<slug>_draft.md            # review → _final.md + _review.md
python3 scripts/article_reviewer.py --draft <path> --dry-run                                  # print the prompt, no call
python3 scripts/article_reviewer.py --audit --draft <path> --out <path>                       # audit an existing pair, no LLM
```

### 5.1 What the stage does

1. **Builds the ledger** from the draft (and the brief that produced it, found by the URLs they
   share — never by vertical, which matches a same-day brief on another story):
   every measured figure *with the sentence it sits in*, the `[n]` citations, the quoted source
   strings, and the `## Sources` lines.
2. **Asks for a reading first.** The model states the through-line and the shape the story wants in
   a `<!-- review-note -->` block. That block is stripped into `_review.md`; it never reaches a
   reader. A pass that cannot say what the piece argues in one sentence cannot make it read as a whole.
3. **Writes the whole article** under an ordered contract: **accuracy → cohesion → voice → shape**.
   The ledger is spelled out in the prompt as `figure — "the draft sentence"`, because a specific
   do-not-lose list holds where a generic "preserve all facts" does not.
4. **Audits the result** with `scripts/review_audit.py` (below) and retries on the exact failures —
   the missing figure with its draft sentence, the measured rhythm delta, the repeated phrases.
   Up to `--attempts` candidates, **best kept**, not last.
5. **Holds instead of shipping.** A candidate that drops a load-bearing figure, that loses an
   observer cue or the accessibility floor, or that makes the prose worse than its own draft exits 1.
   Held text and every report land in `context/drafts/reviews/` (`<slug>_held.md`,
   `<slug>_review.md`) — never as the `<slug>_final.md` a publisher reads, and never inside
   `context/drafts/` itself, because the voice gate walks that directory and a deliberately
   unfinished body would redden the repo build.

### 5.2 The audit is the gate, not a report

`scripts/review_audit.py` compares the rewrite to the draft. **Hard failures** (the run is held):
a figure lost (with the sentence it came from), a figure that is in neither the draft nor the
brief, a `[n]` citation dropped or invented, a quoted string altered, a source line altered or
dropped, a section marker dropped, a body under the word floor, leaked deliberation, or a
self-graded `## Gate report`.

**Flow regressions** (also a hold): sentence-length spread falling below 85% of the draft's, rhythm
health falling, filler or hedge density rising, repetition rising, the through-line restated in more
than two sections, a boilerplate observer cue, two sections opening with the same words, or more
than 20% of paragraphs being all short declaratives.

Measured on the desk's own 216 draft/final pairs, this is what the old pass was doing: rhythm
spread **8.1 → 6.3** words (fell in 159/216), filler density **0.75 → 1.19** per 1,000 words (rose
in 108/216), a figure lost in **128** articles, and the same four observer cues in 29–56 articles
each. The gate exists because none of that was visible to `check_accessibility.py`, which gates
Flesch and acronyms and can only advise on the *mean* sentence length — a body of uniformly
15-word sentences satisfies it.

### 5.3 Rhythm is the signal, not the average

"How does it read" has one honest mechanical proxy: the *distribution* of sentence lengths, not its
mean. `rhythm_health()` scores spread, centre (13–24 words) and tail (few sentences past 40 words)
together, so a run-on beside three short sentences does not score as "varied". The target is the
draft's own spread or wider — never a template. Sentences may run long and connected; one short
sentence per paragraph gives the beat. Do not shorten sentences to lift Flesch; the lever is words.

### 5.4 Section gates still apply — as a reading, not a checklist
The per-section questions are still the right ones to ask *while* writing (does the lead carry the
concrete thing in sentence 1; does the tension name what shifted and who it hurts; does the
tactical section report instead of prescribing; is the catch honest; does the glance card explain
the piece). But they are answered by the stage that wrote the piece, and the mechanical answer that
counts is the audit's — the old table above was a self-assessment the model could always pass.

---

## 6. Output
`context/drafts/YYYY-MM-DD_<slug>_final.md` (long-form) with the per-section gate
report. Keep the **TL;DR as the structured `<!-- tldr -->` field** (following the 4-part Big Shift / Why It Matters / What I'd Watch / Catch schema) — never write a
prose "in conclusion / key takeaways" paragraph. The **TOC is render-time only** — do not compose
one.

## 7. Failure handling
- **Use the frontier the `stylist` profile is configured to** — do not hard-code a provider. Read the
  profile's `model.default`/`provider` (current live: `gemini-3.1-pro-preview` / `gemini`, `base_url: ''`).
  The rewrite must run on that frontier. Never substitute a non-frontier model.
- **Pre-flight before the rewrite:** verify the configured frontier is reachable (e.g. a 1-token
  `generateContent` ping to the profile's provider). If the frontier is unavailable **and** it is the
  only viable frontier, hold the verified draft at Loop 3 with an explicit upstream-status note — a
  verified draft is never wasted; it finalizes when the frontier recovers. Do not silently fake a rewrite.
- **Do NOT gate the pipeline at start on the frontier.** rada sweep → judge → verify → draft all run on
  deepseek and are independent of the frontier; their value is time-bound by the 30-day freshness window,
  so they must run on schedule even during an outage. The pre-flight gates only the rewrite, immediately
  before Loop 3 — never the sweep.
- **kie.ai / Claude note (historical):** when the frontier was Claude via kie.ai, routing was
  `provider: anthropic` + `base_url: https://api.kie.ai/claude` (non-streaming only, `model.streaming: false`,
  alias model IDs like `claude-sonnet-5`). That key is currently **auth-rejected (HTTP 401)** — do not use it.
  The working frontier is Gemini until a valid Anthropic/kie.ai key is restored. `api.kie.ai` is whitelisted
  in `_anthropic_base_url_override_ok` (runtime_provider.py) if it is re-enabled.
- **`humanize_loop3.humanize_all()` is month-locked — do not call it per-draft.** Its loop globs
  `DRAFTS.glob("2026-09-*.md")` (a hard-coded September). Hand it a draft dated on/after 2026-10-01
  and it finds nothing, writes no `_final.md`, and still exits 0 — a silent no-op that looks like a
  successful Loop 3. Invoke the humanizer per-draft instead, calling the function directly:
  `python3 -c "import sys,pathlib; sys.path.insert(0,'scripts'); import humanize_loop3 as hl;
  hl.humanize_single_draft(pathlib.Path('<slug>_draft.md').read_text(), pathlib.Path('<slug>_final.md'))"`.
  Always confirm the `_final.md` file now exists — never trust the script's own summary.
- **Output-token budget (thinking models):** the frontier is a *thinking* model, and its internal
  reasoning tokens (`thoughtsTokenCount`, typically ~6,400 for a full rewrite) are counted **against**
  `maxOutputTokens`. A too-small budget makes the model think hard and then truncate the article
  (`finishReason: MAX_TOKENS`, partial output, missing `## Sources`/gate report). Keep
  `maxOutputTokens` **≥ 20,000** — verify with `finishReason: STOP` and `sources_check=ok`.
- **Socket timeout (thinking models):** the rewrite can take well over 30s wall-clock because the
  model reasons for seconds before emitting its first token. Any `generateContent` call in a humanizer
  script MUST use a socket timeout ≥ 240s (as `humanizer_tools.call_gemini` does). A 30s timeout
  aborts the full rewrite mid-generation with `The read operation timed out` and, worse,
  `humanize_loop3.py`'s `humanize_all()` still prints `WROTE` unconditionally after the loop even
  though the final file was never written — do not trust that message; verify the `_final.md` file
  exists before reporting success. (Fixed in humanize_loop3.py 2026-09-23.)
- **240s is the floor for the socket timeout, not the ceiling (learned 2026-10-13).** A ~2,000-word
  synthesis draft on `gemini-3.1-pro-preview` aborted on its very first attempt with
  `ERROR rewrite attempt 1: The read operation timed out`; `humanize_single_draft()` treats that
  exception as fatal (`break`), so Loop 3 writes no `_final.md` at all. Note that
  `humanize_loop3.call_gemini` carries its **own** hard-coded `timeout=240` in the module — extending
  `humanizer_tools.call_gemini` does nothing for it. Drive the run from a small per-draft script that
  rebinds the module-level `hl.call_gemini` to a 480s socket timeout and keep everything else
  (`normalize_frontmatter`, the access-retry loop, the marker/source/length checks) unchanged; the
  attempt trail then still prints.
- **The frontier reliably drops two GATED frontmatter facts, and both are silent until verify.sh.** Observed
  2026-10-19 on a synthesis draft: the rewrite returned a clean body with every `[n]` citation and the
  `## Sources` list intact, but its frontmatter had **lost the `sources:` anchors** (`synthesis: true`
  survived alone, which `synthesize_topics.py --check-briefs` reads as an unanchored fusion) and had
  **re-cut the title to a "The…" headline** (a headline-standard violation the gate then re-cuts a second
  time at the push). Neither shows up in the accessibility verdict or the attempt line. Check both the
  moment a `_final.md` lands — restore the two anchor URLs verbatim from the draft's frontmatter, and
  re-score the title with the artifact's own body (`headline_score.score(t, body=b)`) before accepting
  any re-cut.
- **A 900 s socket rebind converged a rewrite the shorter timeouts aborted (learned 2026-10-19).** On a
  957-word synthesis draft, the per-draft driver at **900 s** produced attempt 1 (FAIL, Flesch 46.3) and
  attempt 2 (PASS, Flesch 64.8) in one detached run — the same class that had died at 480 s and 600 s on
  earlier runs. When relaunching, raise the rebind rather than re-tuning the prompt, and pipe the driver
  through a log file (`nohup python3 -u <driver> > /tmp/loop3.log 2>&1 &`) so the attempt trail survives.
- **The rewrite drops the title's own content words out of the lead, silently un-hooking the headline
  (learned 2026-10-19).** A 100 STRONG title whose words sat in the draft's lead came back from Loop 3
  with a lead re-voiced around synonyms ("missing units", "count") — `headline_score.score(t, body=<the
  FINAL>)` then reports `lead_ok: False` and the pre-publish gate may re-cut a headline the run believed
  settled. Re-score against the **final** body, not the draft, and restore the title's words in the lead
  sentence (the pipeline's own vocabulary on the same facts), rather than accepting the re-cut.
- **The rewrite invents provenance inside a first-person cue, and flattens a source's own taxonomy into
  synonyms — both invisible to every mechanical gate (learned 2026-10-19).** On an order-exception piece
  the returning body carried "That is the vendor's view, and my own tracking agrees" — a data source the
  desk does not have, in the exact sentence that reads most human — and the vendor's five named exception
  types had become "bad prices, wrong amounts, missing core data, limit blocks, delivery rules", which
  cannot be quoted or checked against the page. Read every first-person claim back against the brief (it
  must rest on a cited fact or be labelled a reading: "my reading, held loosely"), and restore each source
  term verbatim beside any gloss. A rewrite that also dropped "I did not read the paper" had removed the
  hedge that made a second-hand 7.22% honest — hedges are content, not style.
- **A share-of-something figure is the first casualty of compaction — audit every `% of <duration or base>` against the brief (learned 2026-10-21).** On a two-paper memory piece the draft stated that inference occupies only 5.6% of the time a session's KV state is retained, which was the *only* evidence that the retained state is idle most of the time; the frontier's PASS rewrite dropped it from the body, the numbers bullet and the catch while keeping every count intact — 121 million calls, 68K tokens, 63%, 13.6% all survived, so a numeric diff saw nothing missing. A count is load-bearing-looking; a share reads like colour, so the model deletes it. Diff every figure whose unit is "% of time / of capacity / of calls" against the verified brief before the push, and if the article's argument rests on one, restore it in all three places it appeared (prose, numbers bullet, catch) rather than once.
- **A survey's central-tendency noun is a unit, and the rewrite swaps it (learned 2026-10-21).** From a report's "the most common number of features a platform team was responsible for was 4 … In 2026, the most common feature count is 23" the frontier produced "platforms now **average** 23 features" and later "a **median** count of 23" — the digits survive and the distribution meaning does not, so a modal peak reads as the typical team and the claim becomes one the report never made. The same pass dropped the *comparison* attached to a paired figure (a 2.3× / 2.6× likelihood ratio) while keeping the 31% / 17% shares it explained, and left a `## Sources` row that no `[n]` in the body cited. Check every descriptor of a survey statistic (most common / median / average / share of respondents / share who selected) against the report's own sentence, keep the comparison word bound to its ratio figure, and confirm each numbered source is cited in the body before the push.
- **The rewrite renames the study's independent variable, and then its result reads as a different study
  (learned 2026-10-21).** On a two-paper cost synthesis the frontier turned "framework identity explains
  52.95% of peak-RSS variance against 4.22% for task content" into "setup identity drives 53% … while the
  task drives 4%", and spoke of "setups" throughout — a generic noun that makes a study *of frameworks*
  read as a study of arbitrary environments, while rounding figures the numbers bullet still carried
  exactly. Siblings in the same body: "nearly 39x" became "39 times more" (hedge dropped), a budget of
  "90% of the pair's combined peak memory demand" became "90% load" (a budget fraction is not a
  utilisation — different quantity, different meaning), and "95th-percentile allocation latency" became
  "wait times" (wrong metric). All of it passes Flesch, the acronym check and the citation check. Diff
  the source's own variable name, every hedge word (`nearly`, `about`, `up to`) and every fraction's
  *basis* against the verified brief before the push, even when the plainer synonym reads better.
- **The reviewer lifts Flesch by genericising the industry's own nouns and by inflating the numbers section, and its audit is numeric so both survive (learned 2026-10-28).**
  On a warehouse-automation synthesis `article_reviewer.py` returned three candidates with every figure, citation and source line
  intact; the best (hard=0, Flesch 61.1) had rewritten *warehouse* as "shed", *humanoid* as "walking machine", *downtime* as
  "stops", the payback as "a return on machines" and a contract as "a pact", and had grown `By the numbers` from 4 bullets to 7 by
  promoting prose figures into it. `review_audit` compares numbers, not nouns, and carries no bullet-count rule, so a
  vocabularised candidate can score hard=0 — the soft vocabulary lever the accessibility floor rewards is exactly what costs the
  piece its domain. Keep the attempt that is clean on figures, then repair in ONE pass: restore each source's own noun, demote the
  extra bullets back into prose (the figures stay in the body, so the ledger is unchanged), and re-run `review_audit` — a hand
  repair passes. Count the bullets against the 2-4 rule yourself; the audit will not.
- **The cue the voice gate accepts is the cue `review_audit` calls boilerplate — "my read is that" is on both lists, so repairing a missing cue with it swaps one hold for another (learned 2026-10-29).** `site/social_voice.mjs` reads `\bmy read\b` as a labelled opinion (which is why the 2026-10-28 entry above recommends it), while `scripts/review_audit.py`'s `boilerplate_cues` list carries "my read is that" — a phrase the desk has used in 29-56 articles — and a final that opens its catch with it fails the audit as `boilerplate observer cue(s)` after passing the voice gate. Repair a dropped cue with a form neither list owns as boilerplate: "I could be wrong, but…", "Where I've landed:", or an observation the run actually made ("I read that fraction twice before believing it"). Check both instruments in one pass — `review_audit.py` on the pair and `node scripts/check_social_voice.mjs` on the file — because each accepts a cue the other refuses.
- **`verify.sh`'s voice check reads the committed `*_draft.md` too, so an imperative in the structural
  draft fails the repo gate even when the `_final.md` is clean (learned 2026-10-19).** "Treat that as a
  vendor's claim" in the draft body reddened §9 with 2 problems after the publish had already gone
  through, and the published artifact was fine. Fix the draft as well as the final (same re-voicing), then
  re-run `bash scripts/verify.sh` before the commit that carries the run-log row.
- **A 600 s socket rebind is not a guarantee either; and a body that passes markers/sources but fails only
  the Flesch floor is a hand-tune case, not a re-run case.** Observed 2026-10-19: the per-draft driver at
  600 s produced attempt 1 (markers ok, sources ok, Flesch 48.0 — four points under the floor) and then
  attempt 2 died on the read timeout, leaving a `_final.md` that exists and fails the gate. The recovery
  that works is §7 hand-tuning over the frontier's own rewrite — keep every figure, citation and source
  line, shorten sentences and swap long nouns for short ones — then re-run the accessibility gate to a
  PASS (that run landed at 62.6) rather than spending another 10-minute generation on a draft that is
  already structurally sound.
- **The post-rewrite audit has three failure classes beyond invented numbers, and all three appeared
  in one run (learned 2026-10-13).** (1) **A quantity swap inside a real figure:** Trane's "over 1,000
  tons (3.5 MW) of cooling *capacity*" came back as a chiller "**drawing** 3.5 MW" — the number is
  right and the noun is wrong, so the Flesch gate, the acronym check and a numeric diff all pass it;
  check every figure's *unit noun* against the source, not just its digits. (2) **An invented count
  on an aggregate event:** the rewrite rendered "three dozen sites transferred at once" where no
  source gives a site count — replace an aggregation the source never made with a hedge ("many
  sites"), never a plausible-looking number. (3) **A rival figure handed to the wrong source row:**
  "another outlet measured the same event at 3.9 GW [3]" pointed at the source that prints 3.8 — if
  the piece contrasts two published readings of one event, the *second* reading needs its own
  `## Sources` entry (add a row; `synthesize_topics.py --check-briefs` only requires the URL to be in
  a committed signals file). Also re-check **name expansions the frontier invents for an acronym** —
  a rewrite expanded PJM to "Pennsylvania-New Jersey-Maryland Interconnection", a name the run never
  fetched; the acronym-first gloss ("PJM (the grid operator for 13 states and Washington, D.C.)")
  satisfies the accessibility gate without asserting an unverified legal name.
  **A rewrite can also "fix" an acronym flag with a tautology (learned 2026-10-20).** The checker wants
  the token expanded on first use, and the cheapest way to pass it is to print the brand's own name back
  at itself — observed as "LG Electronics (LG)" on a smart-home draft, which reads like a typo and teaches
  the reader nothing. Gloss what the entity *is* ("LG (the electronics maker that builds the cameras)"),
  or drop the brand for a plain noun phrase — never an echo of the acronym.
- **Run Loop 3 in the foreground when the run is a cron/one-shot session (learned 2026-10-10).** A
  background `terminal(background=true)` humanize run gets no completion notification in a cron
  context (the session cannot receive async completions), so the per-attempt log — verdict, Flesch,
  word count, which attempt passed — is lost and you must infer success from the `_final.md` alone.
  Run the per-draft invocation in the foreground (or `... 2>&1 | tee /tmp/loop3.log`) so the attempt
  trail survives, and still confirm the `_final.md` exists and re-measure it before publishing.
- **In a cron session a "foreground" call over the tool's 600 s cap is silently promoted to a
  background process (learned 2026-10-13).** Asking for `timeout 1700 python3 <driver>` returns
  `Background process started` and a session id, the call "succeeds" with no output, and the attempt
  trail exists only in whatever file you redirected to — so always pipe the driver through
  `tee /tmp/loop3.log`, check the `_final.md` mtime/size afterwards, and poll the session
  (`process action=wait`, clamped to ~180 s per call, repeatedly until `exited`) instead of assuming
  the rewrite finished.
- **A cron session's foreground terminal call is cut at ~420 s whatever timeout is asked for, so launch the driver detached (learned 2026-10-19).** A `terminal(timeout=580)` call running `timeout 540 python3 scripts/loop3_<slug>.py 2>&1 | tee /tmp/loop3.log | tail -30` came back as `timed out after 420.0s`, killed the rewrite mid-generation, left `/tmp/loop3.log` empty and wrote no `_final.md` — the run had to be relaunched from scratch. Start the driver with the tool's `background=true` and `nohup python3 -u <driver> > /tmp/loop3.log 2>&1 &`, then poll (`sleep 45; tail /tmp/loop3.log`) until the `WROTE … final_verdict=` line and the `_final.md` file both exist. Absence of output is never evidence that the rewrite passed.
- **A rewrite can re-cut a hand-set title past the standard and drop a brief's own qualification (learned
  2026-10-15).** The frontier re-emitted a hand-set 8-word title as an 11-word one ("…: Why 52% of Plans
  Lose to Last Period"), which scores 89 OK — not STRONG — so `publish_gate.title_gate` commissions
  candidates and may re-cut it after the run reports success. Score the final's title against the final's
  own body and restore a STRONG version (`headline_score.score(..., body=...)`, 100/100 with `lead_ok`
  true) instead of trusting the rewrite. The same rewrite silently dropped a qualification the verified
  brief required — a worked illustration ("a theoretical situation" cited from Gilliland 2010) came back
  reading as a measured company result. Diff the final against the brief's own "gate rulings for the
  drafter" list, not just against the numbers: framing and provenance are part of the claim.
- **The frontier can PASS the floor and still land under target (learned 2026-10-10).** A rewrite that
  exits PASS at Flesch ~50–51 clears the hard gate but sits on the floor, and the persistence pass
  injects the `## Related reading` block *after* the rewrite, which can push the *published* artifact
  below 50. Hand-tune the `_final.md` toward the 60 target before publishing — swap long generic
  words for everyday ones, keep each long proper noun to one full mention, and only as a last resort
  split a sentence that is genuinely over-long (30+ words). Do **not** split as the main lever: it
  buys about two points and costs the rhythm, which is the failure the 2026-10-22 rhythm fix exists
  to stop. Verified path: 50.7 → 61.4
  on the final, so the published artifact landed at 57.3 instead of under the floor. Facts, `[n]`
  citations, section markers and `## Sources` stay untouched.
- **A `humanize_one.py` PASS is measured against `MIN_BODY_WORDS` (600), not the house floor (~800) (learned 2026-10-12).** A 1,100-word structural draft came back at 678 words with `verdict=PASS  length=ok`: the script checks accessibility, the source list and the section markers — not the long-form floor, and not §9's observer cue, which the rewrite had also dropped from `<!-- nuanced-takeaway -->`. Treat its PASS as the accessibility verdict only. Before persisting: restore depth from the verified brief (a synthesis that compacts ~40% has usually shed the anchor carrying the collision), re-read each interpreting section for its first-person cue, and re-cut the title if the frontier swapped your `STRONG` headline for its own.
- A section that fails its gate after 2 retries → report the specific section + criterion to the
  Editor, do not silently ship.
- Recurring AI-tells in drafts → log the tell + the fix to `skills/self_improvement_eval.md` so
  the Drafter stops producing it upstream.
- **A `PASS` from the humanize script is not the voice gate.** `humanize_one.py` / `humanize_path.py`
  check the ACCESS gate, the source list, the section markers and the body floor — they do **not** run
  `scripts/check_social_voice.mjs`, so a rewrite that exits 0 and reads clean on Flesch can still fail
  `verify.sh` §9. The frontier reintroduces second-person instruction in the interpreting sections
  (observed on an evergreen rewrite: "None of this means you should build everything twice", a §3.9
  ban), and it will put an imperative after the colon of a labelled-opinion cue (observed 2026-10-14:
  the containment rewrite opened The catch with a "my read" cue, a colon, and the verb "treat", which
  `ADVICE_AFTER_COLON` reads as advice; the fix is to state the reading as a sentence — "My read is
  that the containment ladder is a shape worth copying"). Run `node scripts/check_social_voice.mjs`
  after Loop 3, fix any flagged sentence by re-voicing it ("None of this argues for building everything
  twice"), then re-measure with `check_accessibility.py` — re-voice only, never drop a figure or a
  citation. A rewrite that names no new figure can still fail the build on voice alone; the §9 gate is
  cheaper to run than a re-publish. **The gate reads the whole file, your own `## Gate report`
  included** — a note that quotes the offending construction back (e.g. reproducing the bad
  "colon + verb" string while documenting the fix) re-fails the same check, so describe the repair in
  prose without reproducing the string.
- **A benchmark-relative result can be relabelled as the mechanism's own effect size (learned 2026-10-19).** A study reporting that an optimiser "beat its benchmark by 16.4% on the linear case, 11.3% on the divergent case, and 6.6% on the general case" came back from the rewrite as a lead claiming "shared demand means that cut lands closer to 6%" — the 6.6% is a gain *against a specific baseline*, not the size of the pooling cut the article is about, and the substitution turns a comparative result into a measured effect the paper never reports. Flesch, the acronym check, the `[n]` presence check and a numeric diff all pass it because every digit is real. For every percentage a rewrite attaches to a mechanism, read the source sentence that produced it and keep the comparison intact ("beat the company's own 98%-on-every-link policy by 6.6%"), never a bare "the cut is X%".
- **Audit a relative interval by computing it, never by estimating it (learned 2026-10-13).** A draft that bridges two dated events ("eleven days before that report", "three weeks earlier") carries an arithmetic claim that no gate checks — not Flesch, not the acronym check, not a figure diff, because both of its endpoints are correct dates. Observed on `your-32gb-card-gone`: the drafted body and the frontier rewrite both said the Nebius increase was "eleven days" before the 2026-10-10 production report, when 2026-10-01 → 2026-10-10 is **nine** days. Compute every interval from its two dates (`datetime.date(2026,10,10) - datetime.date(2026,10,1)` = 9 days) before the accessibility gate, and when a sentence's interval is load-bearing, name both endpoints so a reader can check it without arithmetic.
- **Audit a derived *difference* the rewrite promotes out of the body (learned 2026-10-13).** The interval class above is a claim whose endpoints are both real dates; the sibling class is a subtraction of two real figures that no source states. Observed on the evergreen `panel-upgrade-80-percent-test`: the rewrite took a field note's $11,200 quote and $4,200 resolution, subtracted them, and put "$7,000" into BOTH the lead and its re-cut headline ("Homeowners: The 80% test saves $7,000 on panel upgrades") — presenting one anecdote's spread as a general saving, with a figure that appears in no source row and that the verified brief's arithmetic allowance did not cover. Flesch, the acronym check and the source-presence check all pass it. When a rewrite touches the lead or the headline, diff those two surfaces against the verified brief's *authorised* arithmetic, not just against the numbers: restore the un-derived wording and the hand-written headline, and re-run `headline_score.py` to confirm the restored title still clears 90.
- **Audit a derived *ratio* the rewrite promotes out of the tactical section (learned 2026-10-14).** The sibling of the interval and difference classes: two sourced endpoints give the frontier a ratio no source states. Observed on the evergreen `one-approval-two-payments`: the verified brief carried the stock saver's duplication ({2:10}) and the shipped gate's ({1:10}) as separate rows, and the rewrite wrote "which cut the double-fire rate in half" into `<!-- tactical-insight -->` — a 50% reduction that appears in no source, and that a rounded reading of the two fractions would not produce either. Flesch, the acronym check, the `[n]` check and the figure diff all pass it, because both endpoints are real. State the two measured outcomes side by side ("it served one caller and refused the rest, where the stock saver let both through") instead of reducing them, and diff every *comparative* word the rewrite adds (halved, doubled, tripled, twice, a third of) against the brief's authorised arithmetic. The same run's second half of the class: the frontier collapsed a two-figure `By the numbers` lead-in (`67.2% and 67.7%`) to one figure while keeping the sentence that claims both were the most common faults — re-read each bolded lead-in against the brief's rows, not only the prose.
- **Audit an attributive property against the noun it modifies (learned 2026-10-13).** The unit-noun class above covers a right number with the wrong unit; the same error appears when a rewrite collapses a source's *property* into the noun it describes. NVIDIA's page says "84 GB GDDR7 with error-correcting code (ECC)"; the rewrite produced "84 GB of error-correcting code memory", which reads as though ECC were the memory itself. Both pass every gate. Check each glossed technical phrase against the source's own wording, not just its digits.
- **A rewrite can drop one leg of a synthesis from the TL;DR (learned 2026-10-19).** The `<!-- tldr -->`
  card is what most readers see, and the frontier treats it as a summary of the *incident*, not of the
  *fusion*: on a BCG ⨂ Zenity synthesis the card named the exploit and omitted the thesis leg entirely,
  so the published badge said "synthesis" while the card described a single product vulnerability. Read
  the card against the brief's two anchors after every rewrite — both legs, and the collision, must be
  visible under `The Big Shift` — before the accessibility gate, not after the push.
- **A PASS rewrite can delete the sentence that makes the headline honest — re-check lead delivery, not only the score (learned 2026-10-15).** A title is scored against the article's *numbers* section, so it can keep 100 STRONG while the sentence the title's promise rests on is gone from the lead. Observed on the evergreen retainage piece: the frontier's PASS rewrite compacted the draft's lead and dropped "A remodel deal can name 15 percent", leaving the adopted title *"Retainage Trap: 5 Percent, Not 15"* scoring 100 STRONG with `lead_ok: False` and the body's only other `15` being the 15-day acceptance window — the bait-and-switch that rule 4 forbids, and invisible to Flesch, the voice gate and the source check. `lead_delivery` reads only the first paragraph, so restore the contrast sentence there from the draft or the verified brief (a figure the brief authorises as the desk's own framing may be restored; a source figure may never be invented), then re-run `hs.score(title, body=...)` and confirm `lead_ok` is True before persisting. A title whose `lead_ok` is False is a headline waiting to be re-cut at the push.
- **A rewrite can fuse two sources' figures into one claim — audit which source each number belongs to, not just whether it is real (learned 2026-10-21).** On a price-versus-consolidation synthesis the lead came back as "Seegrid plans to cut that price in half", fusing an analyst's $100,000–$200,000 per-unit range (Grand View Research) with a vendor's own statement that its *next warehouse model* would sell for about half the price of *its manufacturing machine*. Every number was real, the arithmetic was plausible, and no gate could see it: Flesch, the acronym check, the `[n]` presence check and a figure diff all pass a sentence that merely re-points a real figure at a real actor. For every figure in the lead and the headline, re-read the sentence that produced it and confirm the actor, the object and the basis are the source's own — an analyst's estimate is not a vendor's price, and "half the price of X" is not "half of the range quoted above". The same class shows up as a *simulation* relabelled a "test", a *range* collapsed to its ceiling, and a survey's *estimate* softened into a "guess": all four survive every mechanical gate.
- **Splitting the lead to satisfy paragraph discipline can silently unset `lead_ok` (learned 2026-10-21).** After a PASS rewrite, a title scoring 100 STRONG with `lead_ok` true went to `lead_ok: False` the moment the lead was broken into two paragraphs to keep the 1–3-sentence rule — `lead_delivery` reads only the *first* paragraph, and the figure the title anchors on ("84,000") had been left in the second. Keep the title's figure in the first paragraph even if that paragraph runs to four sentences (the paragraph warning is advisory; the headline gate is not), re-score with `hs.score(t, body=<final>)` after any structural edit to the lead, and treat `lead_ok` as a hard check before the push.
- **A tax rate's *base* is content, and the frontier relabels it (learned 2026-10-23).** On a § 351 ruling
  piece the numbers bullet came back reading "**37% — Top gain rate**", with the 2026 ordinary-income
  threshold ($640,600 single / $768,700 joint) attached. A long-held position is taxed at capital-gain
  rates, which top out at 20% plus the 3.8% net investment income tax; 37% is what a *short-term* position
  pays. Every gate passes it — the digits and the thresholds are real, only the noun is wrong — so a reader
  planning around it overstates the cost of selling by more than thirteen points. Check each rate against
  the base it is charged on (ordinary income vs capital gain vs the net investment income tax vs state) and
  put the base in the metric title itself ("Top long-term rate").
- **When every candidate is held, pick by hard-failures first and repair by hand — later attempts buy rhythm with figures (learned 2026-10-29).** Three `article_reviewer.py` candidates on a 1,138-word synthesis were all held: attempt 1 `hard=0` with the prose flattened (rhythm sd 7.3→5.7, health 0.837→0.49), attempt 2 `hard=6`, attempt 3 `hard=1` at rhythm 6.5 / health 0.77 — and attempt 3's single hard failure was the familiar `<!-- nuanced-takeaway -->` cue class (it wrote "My reading is that…", which `site/social_voice.mjs` does not read as a labelled-opinion cue). Taking attempt 3 and repairing the cue in one pass is the cheaper run: it kept all 24 figures and 5 citations, and the rhythm only needed a second pass to clear the advisory (merging two mid-length sentences into one 36-word connected sentence and one 33-word contrast sentence took sd 6.0 → 7.0, 96% of the draft). Do not re-run the stage for a cue a hand edit fixes, and do not take a later candidate on rhythm alone when it lost a figure. **When the ONLY hard failure is Flesch, take that candidate and fix the words — the alternative is a re-run that trades readability for rhythm in the other direction (learned 2026-10-30).** On a 900-word synthesis `article_reviewer.py` held attempt 1 at `hard=4` / rhythm 6.7 / Flesch 54.4 and attempt 2 at `hard=1` / rhythm 9.7 / Flesch **41.7**: the later attempt kept every figure, citation and quote and restored the draft's rhythm, but bought it with longer words. The documented repair (plain-word swaps, then sentence splits only where a sentence ran past 30 words) took it to 53.4 with the ledger untouched and `review_audit` still PASS — about ten minutes of editing against a nine-minute regeneration that would have returned a third trade-off. Read the two attempt lines as a pair before choosing: `hard` decides which candidate, `flesch` decides how much hand work follows.
- **A rewrite can replace the whole `By the numbers` series with a peripheral bullet, and can restate two parallel legal regimes as additive ones (learned 2026-10-26).** On the AI Act penalty-band evergreen the frontier PASSed at 61% of the draft and deleted all three band bullets (3%, 7%, the €500 million crossing point) that were the article's reason to exist, keeping a privacy bullet and inventing a new home for a log bullet — a numbers section can be replaced wholesale, not merely thinned, and the headline's own figures then have no row. The same pass wrote that watchdogs can "stack AI Act penalties on top of privacy fines" where the source says the AI Act "shall not affect" the privacy regulation: two regimes that run in parallel and price one failure twice do not add, so "stack", "on top of" and any sum is a claim the statute does not make. Read the numbers section against the verified brief bullet by bullet (not just the prose), and rewrite every additive word that touches two separate regimes into "read under both, never added".
- **The figure audit is now the stage's own gate, not a hand check.** `scripts/article_reviewer.py`
  builds the ledger (every measured figure with the sentence it sits in, the `[n]` citations, the
  quoted strings, the `## Sources` lines) and `scripts/review_audit.py` compares the rewrite to the
  draft: a lost figure, an invented figure, a dropped or invented citation, an altered quote or
  source line all fail the run and are held, with the missing figure and its draft sentence fed back
  for the retry. Run `python3 scripts/review_audit.py --draft <draft> --final <final>` on any pair,
  including an already-published artifact, to see the diff.
- **What the numeric audit still cannot see — audit these by meaning.** The gate compares numbers,
  not nouns: a right figure with the wrong unit ("3.5 MW of cooling *capacity*" → a chiller
  "*drawing*" 3.5 MW), the wrong base (37% applied to a long-term gain), a share relabelled as an
  absolute, a comparison promoted to an effect size, a modal peak read as a mean, an interval whose
  endpoints are both right and whose subtraction is wrong. Those classes stay manual — diff them
  against the verified brief before the push, exactly as the entries below describe.
- **A rewrite can invert a rate into its complement and mislabel the base (learned 2026-10-19).** From a
  source's "0.148% parse-error rate" the frontier wrote "99.8% of those failing outputs parsed perfectly" —
  a derived complement (100 − 0.148, padded to 99.8), attached to the wrong base ("of those failing
  outputs"). Every gate passed it: the arithmetic was near enough and no gate reads the noun. It is the
  sibling of the interval / difference / ratio classes above. State the source's own rate ("just 0.148% of
  outputs failed to parse") and diff every complement a rewrite introduces against the verified brief's rows.
- **Audit names too, not only numbers (learned 2026-10-07).** The same pass must compare every proper
  noun the frontier touched against the brief and the source: a rewrite of a paper-based article
  renamed the cited paper's first author ("Tapio Mraz" for **Oto Mraz**), and a substituted name is
  as load-bearing as an invented figure — it attributes a claim to someone who did not make it.
  Correct it to the source's spelling, and do it *before* the accessibility gate rather than after:
  Flesch and the acronym check cannot see a wrong name.
- **Audit a clock's trigger, not only its number (learned 2026-10-12).** A rewrite can keep every
  figure and still move what starts the timer: DORA's four-hour initial notification came back as
  "after they spot it" from "once it has classified it as major", so the discovery-based 24-hour
  outer bound read as the start of the four-hour clock. For every deadline, threshold or payback
  the brief states, check the *trigger* in the rewritten sentence against the source's own wording
  (classification vs awareness vs discovery), because the Flesch score and the figure audit both
  pass a sentence whose number is right and whose start is wrong.
- **Audit quotations and new tokens too (learned 2026-10-13).** The audits above cover figures, names and clock triggers; they do not cover *the words inside quotation marks*, and the rewrite does edit them. Observed on an enterprise_tech_leadership final: a source's `"a lot of cloud repatriation projects are actually FinOps projects in disguise"` came back with the expansion inserted *inside* the quotes (`"…actually financial operations (FinOps) projects in disguise"`) — the desk's gloss in a quoted source's mouth. Diff every quoted string against the source verbatim before the accessibility gate. Same pass, same run: the rewrite *added* the all-caps brand token `ZDNET` to the body (the outlet had been cited only in `## Sources`), which the accessibility checker fails as an undefined acronym — re-voice the new token away rather than inventing an expansion for it; it also genericised a named attribution ("One consultant's line…") and turned a source-true activity ("prioritizing the restoration of services and tools that enable customers to back up and migrate") into an invented duration ("spent days fixing"). All four pass Flesch, the acronym check and the `[n]` citation check untouched, so none is visible to any gate.
- **Flesch ceiling on proper-noun-dense bodies (learned 2026-10-06):** the compliance-retry loop
  can exhaust all `MAX_ATTEMPTS` and still FAIL the Flesch floor when the body is dominated by
  long brand/product tokens. Observed on an Azure incident piece: five full rewrites scored
  21.4 → 39.3 → 45.1 → 45.7 → 44.6 (best 45.7, floor 50) — the frontier cannot lift the score by
  re-voicing because the syllable ratio is set by repeated proper nouns (`Azure OpenAI Service`,
  `Application Gateway`, `ExpressRoute`, `Coordinated Universal Time`) and by average sentence
  length. Do **not** spend more attempts; hand-tune the finished body, in this order: (1) swap
  3-syllable generic words for 1–2-syllable ones (`provider` → `vendor`, `observability` →
  `monitoring`) and keep each long proper-noun string to ONE full mention, shortening the later ones
  (`Azure OpenAI Service` → `Azure OpenAI`; drop a repeated service list from the numbers bullets);
  (2) only then split a sentence that is genuinely over-long (30+ words) — splitting raises the
  coefficient-1.015 term but fragments the prose, so it is the last lever, never the first. Verified: 44.6 → 53.1 PASS with facts, `[n]` citations, section
  markers and the `## Sources` list untouched. Re-measure with `check_accessibility.py` after the tune.

- **A role label in front of a headline scores 100 standalone and fails the push (learned 2026-10-26).**
  The rewrite likes to prefix a title with the reader's role — `"Homeowners: Your Next Bedroom Costs
  $417,500"` — which passes every mechanical rule and reports 100 STRONG from `headline_score.py "<title>"`.
  Scored with the body it reads `lead_ok: False` ("absent from the lead: next, costs"), because the label
  ate the room the core clause needed, so the pre-publish gate re-cuts the title a second time and the
  six-surface headline trap opens. Always score the frontier's re-cut WITH the body
  (`hs.artifact_title(path)` → `hs.score(t, body=b, keyword=k)`) before adopting it, and when `lead_ok`
  is False restore the hand-set title that scored 100 with `lead_ok: True` (`skills/story_draft.md`
  §3). The colon form is not a house headline: `story_draft.md` wants the core ≤ 6 words *before* any
  colon, and a role noun is filler in that position.
- **Recover a truncated `alt_text` from the sidecar's own revision history (learned 2026-10-26).** When
  the art director returns alt text cut mid-phrase, the complete sentence is usually already in
  `context/assets/illustrations/<slug>/featured.json` under `history[0].alt_text` — the same image's
  first-pass wording. PATCH `wp-json/wp/v2/media/<id>` with that sentence plus the caption, read it back,
  then reconcile the sidecar's top-level `alt_text`, the artifact's `image_alt` and the row's
  `metadata.illustration.alt_text` / `metadata.wordpress.media_alt` in one follow-up commit. Editing a
  published artifact after the persistence pass is safe for frontmatter-only fields (`sitemap.json`
  carries titles and state, not image copy) — re-run `scripts/sitemap_sync.py --check` and
  `bash scripts/verify.sh` to confirm.

- **A rewrite can replace a specific count with a vaguer quantifier, and every gate passes it (learned 2026-10-27).** On the
  prompt-cache mis-integration piece the frontier PASSed at Flesch 52.6 with "dozens of prompt-caching pull requests across
  open-source agent systems" for the draft's **120 across 10 systems**, and "dozens of finds across hundreds of projects" for
  **32 in 571**. Nothing is wrong — there is no number to be wrong — so Flesch, the acronym check, the `[n]` check and
  `article_shape` all pass a body whose evidence has been rounded into vagueness. Diff every "dozens / hundreds / many / a few /
  several" in the final against the draft and restore any count the draft carried; a study's sample size is the claim, not
  colour. The same pass re-cut a **6-word title into 7** by inserting a noun ("Your **Prompt** Cache Pays…"), which reports
  100 STRONG standalone but breaks the core-length rule, so read `core_words` — not only `score` and `lead_ok` — when auditing a
  re-cut. Same run, same class: 39-of-43 became "matched hosting everything", the 1.25×/0.1× bullet was swapped for a "0.1× base"
  metric that dropped the write premium the headline leans on, and "actuates" became "handling" — four figures softened in one
  PASS, all of them load-bearing. **The same pass softens the headline's own figure in the lead, which unsets `lead_ok` at
  the same time (learned 2026-10-27, `your-green-passes-hide-31-wrong`):** the title kept "31.08%" while the lead said "nearly
  a third", so `lead_delivery` (which compares digit cores) reported the promise unmet *and* the article's opening lost its
  number — restore the figure from the verified brief rather than re-cutting the title, and expect the sibling swaps
  ("32.67%" → "a similar share", "4%" → "missing nearly all", "76% vs 53%" → "far more often") in the same rewrite, because
  one vague quantifier arrives with the others.

- **The reviewer also unwraps the hand-written inline internal link into plain prose, and `article_shape` holds the push for it (learned 2026-10-28).** On the flood-gap synthesis every kept candidate had turned `a [coverage-gap calculator](/calculators/insurance-coverage-gap/) exists to make plain` into `a coverage-gap calculator exists to make plain` — the words survived, the markdown did not — so the artifact cleared the review audit, the accessibility floor and the voice gate and then failed the push with "the body carries no inline internal link". Restore the link in the same repair pass as the missing observer cue: re-wrap the same phrase, `curl` the path, and re-run `article_shape.py` plus `publish_gate.py --file` before publishing. `review_audit` cannot see it, because it compares figures, citations, quotes and source lines, not link syntax.
- **The reviewer's rewrite drops the `<!-- nuanced-takeaway -->` observer cue in almost every run, and a cue the writer thinks it wrote does not count (learned 2026-10-28).** Two full `article_reviewer.py` runs (six candidates) on one synthesis were all HELD: attempt 1 of each lost six figures, but every remaining candidate — and both attempts 2, which were otherwise clean — failed on the same single hard failure, the catch section arriving without a first-person sentence. The draft had one ("My read is that…"); the rewrite re-phrased it as "My reading, held loosely", and `site/social_voice.mjs`'s labelled-opinion cue is `\bmy read\b`, which does **not** match "my reading". Two consequences: budget for a hand-repair of that cue on every run rather than re-generating (the second run reproduced the fault exactly), and when repairing, use a cue the regex reads as written — "Where I've landed:", "What I keep circling", or "I could be wrong, but…" — not a near-synonym of one. A hand repair that also has to restore the lead (the rewrite's lead began "An agent task…" and dropped the title's own "your" and "isn't", unsetting `lead_ok`) should be done in one editing pass, then proved with `review_audit.py` (which passes a hand-edited final: the ledger compares figures, citations, quotes and source lines, not authorship) plus the accessibility, voice and headline gates.
- **The reviewer's own inventory of invented expansions is worth reading before the push (learned 2026-10-28).** A held candidate expanded OAuth as "Open Authorization" and SAP as "Systems, Applications, and Products" — the first is not a name the protocol uses and the second is a German legal name rendered as an English phrase; both would have satisfied the acronym gate with an unverified expansion. On any rewrite, read every parenthetical expansion the model added against the source, and prefer the gloss form the skill allows ("SAP (the German business-software vendor)") to a fabricated full name.
- **The rewrite puts the acronym gloss INSIDE a direct quotation to satisfy the gate, which alters the quote (learned 2026-10-28).** Observed on the gpu_hardware D270 synthesis: Intel's page reads `fewer GPUs and no high bandwidth memory (HBM)`, and the rewrite returned `"for richer reasoning with fewer graphics processing units (GPUs) and no high bandwidth memory (HBM)"` — the desk's gloss in a vendor's mouth, and the one class `review_audit` cannot see when the quoted string is also restructured. Two fixes, in order: move the gloss into the writer's own sentence before the quotation, or shorten the quotation to the fragment the source actually sells (`with what Intel describes as "no high bandwidth memory (HBM)"`). Never leave an expansion inside quotation marks.
- **A corporate name whose initials are an unexpandable acronym passes the gate only in one shape: `the <descriptor> (SK hynix)` (learned 2026-10-28).** `SK hynix` fails `check_accessibility` on the `SK` token, and none of the usual forms fix it — a gloss after the name (`SK hynix, the memory supplier`) is an appositive the checker rejects, and `hynix (SK hynix)` is the tautology trap. `order_a` needs text before the parens and the acronym inside them, so write "the memory maker (SK hynix) reported…" and every later `SK hynix` in the body is covered by that single definition. The same shape works for any vendor whose short name is initials (SK, LG, HP). If a name defeats every form, name the entity in `## Sources` and call it "the memory maker" in the body — never invent an expansion.

## 8. Accessibility gate (topic-agnostic — applies to EVERY topic)

The gate in §5 checks for Smart Brevity & AI-tells. It does NOT check whether a general reader can follow the
piece. A rewrite can pass every §5 gate and still read like a law-firm memo. Run BOTH gates.
The ACCESS gate is deliberately topic-agnostic: the rules below are the same whether the piece
is about tariffs, an energy program, a security standard, or a database. Enforce with
`scripts/check_accessibility.py` on the finished body.

Gates — the piece FAILS the ACCESS gate if:
1. **Any acronym is used without being expanded at its first use in the body.** Every
   abbreviation the reader won't already know gets a plain expansion once, either as
   "International Emergency Economic Powers Act (IEEPA)" or "IEEPA (...the law that lets the
   president act in a national emergency)". Never reuse an acronym bare after introducing it.
   Checker target: **zero undefined acronyms**.
   **Never invent an expansion.** If the token is a proper noun with no known full form (a
   system/paper name like CRAB, DeltaBox, or Hermes), do NOT fabricate an expansion to satisfy
   this gate — a fabricated full name is a hallucination and a hard failure. Rephrase to drop
   the all-caps token instead (e.g. "specialized checkpoint systems" rather than "CRAB").
   **Apostrophe in the expansion (learned 2026-10-03):** when an acronym's real expansion contains
   an apostrophe or ampersand — e.g. S&P = "Standard & Poor's" — write it **acronym-first**
   ("S&P (Standard & Poor's)"), never "Standard and Poor's (S&P)". The checker's
   "Expanded Form (ACR)" regex only accepts letters/digits/spaces/hyphens *before* the parens, so
   an apostrophe in the expansion breaks the match and the rewrite loops to MAX_ATTEMPTS and
   exits 1 (held at Loop 3) over a term that was actually spelled out. The acronym-first form always
   matches (the parenthetical accepts any characters).
   **A comma appositive is not an expansion (learned 2026-10-12).** "SMUD, the Sacramento Municipal
   Utility District, cut its incentive" reads correctly to a human but still fails the gate as an
   undefined acronym: the checker accepts only the expansion-before-parens form or the
   acronym-before-parens form, never an appositive. Write "SMUD (the Sacramento Municipal Utility
   District) cut its incentive" — and note the gate is checked on the *body*, so a gloss written
   into a bold `By the numbers` lead-in counts only in that parenthesis form.
2. **A specialist term from any domain is left untranslated for a general reader.** For each
   domain term (legal, finance, customs, energy, security, database, ML, government program),
   either (a) find the plain phrase the source used, or (b) add a short gloss. Examples:
   "filed a protective action" → "filed an objection"; "importer of record" → "the company
   named on the import"; "finally-liquidated entry" → "an import already fully processed";
   "unliquidated" → "not yet processed"; "non-recurring add-back" → "a one-time booking";
   "Section 232 duties" → "separate tariffs on steel and aluminum that were never struck down".
   The domain does not matter — apply the same plain-word-or-gloss test to any field.
3. **The reader needs the core mechanism explained and it is not.** If the story hinges on a
   process the target reader wasn't born knowing (refund flow, a rebate rule, a permission
   model, an agency outranking), add ONE half-sentence that states what it is before relying
   on it. "The biggest figure was spoken on a call, never written down" needs a breath that
   says why that is odd.
4. **The body reads at a difficult level for a general audience.** Checker: target
   **Flesch Reading Ease ≥ 60** on the body (frontmatter and `## Sources` are excluded, and the
   legacy `<!-- linkedin -->` block is cut when an artifact still carries one). Hard floor: ≥ 50. Readability comes from plain
   **words**, not short sentences — swap long/technical terms for everyday ones
   ("set up" not "implementation", "slows down" not "degrades throughput") and write connected
   ~14-20-word sentences with variation; do NOT fragment into choppy one-liners. Long proper
   nouns and the numbers are fine; the barrier is word choice.
5. **Keyword stuffing / non-fluent prose.** A target search phrase appears **at most 2-3 times**
   in the whole body — let the title/meta/headings carry it and rephrase everywhere else
   (pronouns, synonyms, "these systems"). Never let it read like a keyword-matching exercise.
   The checker flags `primary_keyword` appearing ≥4× in the body as a FAIL.

Do not sacrifice accuracy or a citation: this is a swap of vocabulary, never a change of fact.

**The Related-reading block is reader-facing — and it can carry an undefined acronym (learned 2026-10-06).** The block is injected in the *persistence* pass (`scripts/internal_links.py`), after the frontier rewrite, and each link's reader copy ends `— more on <destination CMS category>`. When that category name contains an all-caps token (`AI Stack & Tool TCO`), the published artifact reads as an undefined-acronym FAIL even though the `_final.md` the humanizer passed was clean (`check_accessibility.py` on `published/<slug>.md` vs the final: Flesch 60.7 / FAIL — TCO, against PASS on the final). So: read the gate result from the *final*, and when a published artifact flags an acronym, check whether it came from the generated block rather than the prose — the fix is a gloss in the block or dropping the category label, never editing the article body to compensate. **Implemented 2026-10-07:** `scripts/internal_links.py::render_related_reading` now drops a category label that carries a bare all-caps token (and trims a trailing colon) before it becomes reader copy — the class is closed by construction for every newly generated block, with no invented expansion and without rewriting any existing article's footer (`python3 scripts/test_internal_links.py` 64/64). Artifacts published before that date keep the label until they are next re-pushed, so their `access:` line in `verify.sh` §5 stays flagged until then. `verify.sh` §5 reports published files advisory-only (`STRICT_ACCESS=1` makes it hard), which is why this can sit unnoticed. **The block also lowers Flesch by roughly 5 points** (learned 2026-10-07): the three live link titles plus the repeated `— more on <category>` label are long words the checker counts, so a `_final.md` that passed the Loop 3 gate at 51.0 published at 45.8 — a published artifact can read below the 50 floor while its authoritative gate (the `_final.md`) passed. Read the gate from the final and never rewrite the article body to compensate.

Post-rewrite: run `python3 scripts/check_accessibility.py <final.md>`. Report the verdict in the
gate report. The humanizer scripts now auto-retry: if the rewrite fails the ACCESS gate, the script
feeds the exact FAIL/WARNING reasons back to the frontier model and re-prompts (up to 5 attempts,
`humanizer_tools.MAX_ATTEMPTS`). It exits 0 only on a passing verdict; if it still FAILs after the
retry loop, it exits 1 (held at Loop 3) with the specific criterion (undefined acronym / Flesch /
untranslated term) rather than shipping a dense piece.

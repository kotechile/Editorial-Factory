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
- Prefer short, single-syllable, visual words that paint a clear picture.
- Translate domain jargon into plain English or add an immediate short parenthetical gloss.

### 3.6 Paragraph Discipline
- Keep paragraphs exceptionally brief: **1 to 3 sentences maximum**.
- One idea per paragraph. If a thought has two parts, split it into two crisp paragraphs.

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

## 5. Per-section iteration & Section Gates
Do NOT rewrite the whole piece and re-read it blindly. Iterate **section by section**, and only
re-iterate a section that fails its own gate. Order matters: **Lead first** — it decides whether
anyone reads on, so give it an extra check.

For each section, check its gate; if it fails, rewrite that section only and re-check (max 2
retries per section).

| Marker | Gate — it fails if… |
|---|---|
| `<!-- lead -->` | not a concrete incident/stat in sentence 1; contains throat-clearing, introductory preamble, or opens like a definition / "the world is changing". **Highest priority.** |
| `<!-- tension -->` | vague "the industry is evolving"; lacks a context signpost (**The big picture:** or **Why it matters:**); lacks a dedicated **By the numbers:** quantitative section with 2–4 bold bulleted stats; doesn't name what shifted and who it hurts/helps. |
| `<!-- tactical-insight -->` | generic advice ("invest in AI"); not structured with clean bullets and bold lead-ins for 3+ moves; not specific and doable for the target persona. |
| `<!-- nuanced-takeaway -->` | a hollow hedge or a cheerlead; lacks an honest limitation / counter-argument (**The catch:** or **Between the lines:**). |
| `<!-- tldr -->` | lacks the 4-part schema (**The Big Shift**, **Why It Matters**, **What I'd Watch** with sub-bullet definitions, **The Catch**); fails to explain what the article is about; reads like a prose paragraph; OR merely compresses buzzwords without plain-English definitions. |

After every section passes, run ONE final **whole-piece pass**: coherence, cadence, paragraph discipline (max 3 sentences per paragraph), and confirm no AI-tell or empty transition remains anywhere.

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
- **Run Loop 3 in the foreground when the run is a cron/one-shot session (learned 2026-10-10).** A
  background `terminal(background=true)` humanize run gets no completion notification in a cron
  context (the session cannot receive async completions), so the per-attempt log — verdict, Flesch,
  word count, which attempt passed — is lost and you must infer success from the `_final.md` alone.
  Run the per-draft invocation in the foreground (or `... 2>&1 | tee /tmp/loop3.log`) so the attempt
  trail survives, and still confirm the `_final.md` exists and re-measure it before publishing.
- **The frontier can PASS the floor and still land under target (learned 2026-10-10).** A rewrite that
  exits PASS at Flesch ~50–51 clears the hard gate but sits on the floor, and the persistence pass
  injects the `## Related reading` block *after* the rewrite, which can push the *published* artifact
  below 50. Hand-tune the `_final.md` toward the 60 target before publishing — split long sentences,
  swap long generic words, keep each long proper noun to one full mention. Verified path: 50.7 → 61.4
  on the final, so the published artifact landed at 57.3 instead of under the floor. Facts, `[n]`
  citations, section markers and `## Sources` stay untouched.
- A section that fails its gate after 2 retries → report the specific section + criterion to the
  Editor, do not silently ship.
- Recurring AI-tells in drafts → log the tell + the fix to `skills/self_improvement_eval.md` so
  the Drafter stops producing it upstream.
- **A `PASS` from the humanize script is not the voice gate.** `humanize_one.py` / `humanize_path.py`
  check the ACCESS gate, the source list, the section markers and the body floor — they do **not** run
  `scripts/check_social_voice.mjs`, so a rewrite that exits 0 and reads clean on Flesch can still fail
  `verify.sh` §9. The frontier reintroduces second-person instruction in the interpreting sections
  (observed on an evergreen rewrite: "None of this means you should build everything twice", a §3.9
  ban). Run `node scripts/check_social_voice.mjs` after Loop 3, fix any flagged sentence by re-voicing
  it ("None of this argues for building everything twice"), then re-measure with
  `check_accessibility.py` — re-voice only, never drop a figure or a citation. A rewrite that names no
  new figure can still fail the build on voice alone; the §9 gate is cheaper to run than a re-publish.
- **Post-rewrite figure audit (mandatory):** after the frontier passes the ACCESS gate, scan the
  body for NEW specific numbers (dollar amounts, payback periods, time spans, counts) that are
  NOT in the verified brief or the source list. The frontier has inserted unsourced figures
  (observed: a fixed-machine payback rendered as "five years" when the brief carried no payback
  number) that pass Flesch/acronym/length checks cleanly — the retry loop cannot catch them
  because it has no knowledge of the brief's figure set. Revert any such number to qualitative
  wording ("takes years") rather than a fabricated precision, and re-run `check_accessibility.py`
  to confirm the gate still passes.
- **Audit names too, not only numbers (learned 2026-10-07).** The same pass must compare every proper
  noun the frontier touched against the brief and the source: a rewrite of a paper-based article
  renamed the cited paper's first author ("Tapio Mraz" for **Oto Mraz**), and a substituted name is
  as load-bearing as an invented figure — it attributes a claim to someone who did not make it.
  Correct it to the source's spelling, and do it *before* the accessibility gate rather than after:
  Flesch and the acronym check cannot see a wrong name.
- **Flesch ceiling on proper-noun-dense bodies (learned 2026-10-06):** the compliance-retry loop
  can exhaust all `MAX_ATTEMPTS` and still FAIL the Flesch floor when the body is dominated by
  long brand/product tokens. Observed on an Azure incident piece: five full rewrites scored
  21.4 → 39.3 → 45.1 → 45.7 → 44.6 (best 45.7, floor 50) — the frontier cannot lift the score by
  re-voicing because the syllable ratio is set by repeated proper nouns (`Azure OpenAI Service`,
  `Application Gateway`, `ExpressRoute`, `Coordinated Universal Time`) and by average sentence
  length. Do **not** spend more attempts; hand-tune the finished body: (1) split every sentence
  over ~20 words into two (average sentence length carries the larger coefficient, 1.015);
  (2) keep each long proper-noun string to ONE full mention and shorten later ones
  (`Azure OpenAI Service` → `Azure OpenAI`; drop a repeated service list from the numbers bullets);
  (3) swap 3-syllable generic words for 1–2-syllable ones (`provider` → `vendor`,
  `observability` → `monitoring`). Verified: 44.6 → 53.1 PASS with facts, `[n]` citations, section
  markers and the `## Sources` list untouched. Re-measure with `check_accessibility.py` after the tune.

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

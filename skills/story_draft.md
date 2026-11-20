# SKILL: Story Draft (Structural First Pass)

## 1. Objective
Assemble the verified brief into an authoritative structural draft using **only** the VERIFIED
evidence set. No new facts. Provide clear inputs for the Stylist's Smart Brevity rewrite.

> **Casebook: `skills/references/story_draft_casebook.md`** — every headline post-mortem, figure failure
> and the full text of the law summarised below. Read it when a gate holds a draft or before a repair.

## 2. The house structure

The order below **is** the contract (`scripts/readability_critic.py` holds it at the push): the
executive summary primes the reader at the top instead of repeating itself at the bottom. A piece
whose parts are all present but in the old order (summary last) fails the gate.

| # | Section | Rule |
|---|---|---|
| 1 | **Title** | A headline that earns the click, scored by `scripts/headline_score.py` (owner's standard, 2026-10-10) and gated at the push — **for articles from 2026-10-10 on: earlier headlines are grandfathered and only reported, never re-cut** (`ENFORCED_FROM`). **Core headline ≤ 6 words** before any colon/dash subtitle, whole title ≤ 10 words and ≤ 60 characters, **never open on "The/A/An"**, front-load the strongest noun or the most concrete benefit, carry a hook (a curiosity gap or loss aversion — the mistake, the trap, the silent cost — or invert the conventional wisdom), anchor on a figure the article itself states (never invented), and call the reader out ("your/you", or a named role/subject: CFO, shipper, homeowner, SpaceX). No bait-and-switch: the article must satisfy the title in its first paragraph. When drafting for an SEO keyword (`primary_keyword:` in frontmatter), the title MUST contain the target keyword. For **Synthesis articles**, the collision thesis goes in the subtitle, not by stacking both clauses into the headline. |
| 2 | **Lede (paragraph 1)** | The core thesis **and its operational impact** in plain, concrete English, in the first sentence. A concrete incident or figure from the evidence delivers the news; the same paragraph says what it changes for the reader. Not a definition, not a "world is changing" opener, no heading before it. For **Synthesis articles**, write a **Collision Lead**: bridge the two underlying developments in the first 1–2 sentences (e.g., *"As frontier model inference prices plunge past 80% cuts, enterprise engineering teams are quietly turning their backs on off-the-shelf SaaS to build bespoke in-house software."*). |
| 3 | **At a Glance** (`<!-- tldr -->`) | **Immediately below the lede**, never at the foot of the piece. `## At a glance` + ONE plain paragraph, **20–50 words total**: a brief description of what the article is about — its subject, who it concerns and the one finding that carries it. No bullets, no bold labels (owner standard 2026-11-20; the three-line shift/number/risk box is retired). It primes the reader; it never re-lists the watch items below, and it never repeats the subtitle verbatim — the lede and the box must each advance the argument. |
| 4 | **Chronological context** (`<!-- tension -->`) | Paragraph 2 states the timeline **once**, in strict chronological order — **initial event → initial deadline → current extension** — then the mechanism (the systemic reason it is happening now, who it hurts and who it helps). An H2 in this article's own words; "The big picture:" is the fallback label, not the required one (owner, 2026-11-03). In a synthesis piece, explain the friction point where Trend A alters the economics, reliability or feasibility of Trend B. |
| 5 | **By the numbers** | **Kept, but small** (owner, 2026-11-03: the block is what a reader scans; removing it loses the page). `## By the numbers` H2 with **2–3 bold bullets**, placed **after the mechanism has been explained** — never before the reader knows what is being counted. One metric per bullet, one sentence, **25 words or fewer**, formatted `- **<figure> <noun phrase>:** <one plain clause> [n]` (see §3.5). In synthesis articles the figures must still come from **both** underlying anchors. |
| 6 | **What to watch** (`<!-- tactical-insight -->`) | Operational caveats and forward-looking triggers: what the people closest to the story are doing, what the consequences land on, which signal answers the open question next — reported, never prescribed (`persona:` from `context/personas.json`). Write it as prose; bullets only for a real list of comparable items. Header in this article's own words ("Where this bites:" / "What I'd watch:" are fallbacks). Never instruct the reader (`skills/claude_humanizer.md` §3.9). |
| 7 | **The catch** (`<!-- nuanced-takeaway -->`) | The honest limitation or counter-argument, **self-contained**: the final sentence may not introduce a regulatory rule, a billing mechanism, an internal cross-link or a technical concept the piece has not already explained. If it has to name one, give it a 5–10-word inline bridge in the same sentence (*"under federal demurrage billing rules, the two 30-day dispute clocks…"*). Ends on substance, not a cheerlead. |
| 8 | **Related reading & Sources** | Footer, generated at persistence (`<!-- internal-links -->`, `## Related reading`) and copied verbatim (`## Sources`). Render sources as a **vertical list with a list marker** (`- [1] <author>, "<title>" — <url>`, one per line), never one run-on paragraph — consecutive `[1] …` lines carry no marker and the CMS renders them as a single block of text (§3.6 F). |

The **TOC is render-time only** — the site derives it from the section headings. Never write a
"Table of Contents" into the article body.

## 3. Rules
- Inline citations: every factual sentence carries `[n]` mapping to a source list at the end.
- **Place ONE earned inline internal link in the draft, from `context/internal_links.json`, and verify
  it resolves before Loop 3.** `scripts/article_shape.py` hard-fails a body with zero inline internal
  links (the generated Related-reading block does not count), so a draft that leaves linking to the
  persistence pass is HELD AS A DRAFT at the push. Pick a candidate the index marks `live`, justify it
  on the destination's category hub or ≥ 2 shared subject tokens, and write it as a **site-relative
  markdown link with anchor text** — `[Planning tools buy capability, not autonomy](/planning-ai-buys-capability-not-autonomy/)` —
  then `curl -s -o /dev/null -w '%{http_code}'` it. A bare parenthetical path (`(/some-slug/)`) does
  not count: `_LINK_RE` only matches `[text](/path)`.
- One length: the long-form draft. Do NOT write a LinkedIn/social variant — that channel was
  removed on 2026-10-06 (`skills/publisher.md` §3).
- **SEO frontmatter is optional to author and never invented:** with a keyword set from the brief, write
  `meta_title` (<=60 chars) and `meta_description` (140-160) grounded in the headline and lead; otherwise
  omit the keys — `scripts/article_assets.py` derives both at persistence, so neither the CMS excerpt nor
  `<meta name="description">` is ever empty. Never pad them with claims the article does not make.
- Any claim not in the brief is written as `[NEEDS-SOURCE]` and returned to the verifier — never filled with invention.
- Match the target reader's level from `context/personas.json` for the vertical (`persona:` in frontmatter).
- **`## By the numbers` is mandatory and small:** 2–3 scannable bullets, placed after the mechanism, each in the §3.5 shape — `- **<the anchor figure and its noun>:** <one clause that says what it counts> [n]` (e.g. `- **85% of Long Beach cargo:** The volume handled by the eight terminals where 250 watchmen could walk out [3].`). Never start a bullet with narrative filler ("Diesel fuel started the year…", "The leap in the…"), never put two statistics in one bullet, never a bullet over 25 words.
  **Keep at most one percentage in the block** — lead any other bullet on a dollar figure, a count or
  a category, or `article_assets.chart_series` plots two unrelated percentages on one axis.
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
- **Renaming the slug mid-run orphans the old draft, and the voice gate reads every file in
  `context/drafts/`.** Write the new file, confirm it exists, then delete the superseded
  `YYYY-MM-DD_<old-slug>_draft.md` by name.
- **Diction standard (owner, 2026-10-29).** A draft can clear Flesch 50 and both gates and still be
  hard to read, because the damage is in the nouns: name the method and its purpose, use the exact
  error and policy nouns, lock the taxonomy once named, and name the authorities in the prose. Banned
  examples and full wording: casebook, and `skills/claude_humanizer.md` §3.5.
- **Budget the figure load, not only the figure count (owner, 2026-11-03).** `check_accessibility.figure_load`
  advises above 45% of prose sentences carrying a figure. Each paragraph carries one figure plus a
  sentence with no digits that says what it means, and **a figure must say what it is measured against
  in the same sentence** — an assumption written as an assumption, a third party's price as self-evident.
- **Pre-tune the draft before Loop 3 — both gates, not just accessibility.** Run
  `python3 scripts/readability_critic.py --check <draft>` **and**
  `python3 scripts/check_accessibility.py <draft>` on the structural draft. The critic holds the
  deterministic half at the push (At a glance under the lede, one metric per bullet, one citation tag
  per sentence, `## Sources` vertical) and prints the prose advisories; fix them now, because the
  reviewer's rewrite is graded against the same checks.
  **Readability is a WORD-CHOICE lever, not a sentence-length one: swap long technical words for
  everyday ones at drafting time — do NOT split sentences to move the Flesch score.** Write connected
  sentences of roughly **14–22 words** with deliberate variation, let one sentence carry a cause and
  its consequence, and keep at most one eight-word-or-fewer sentence per paragraph, so the body never
  becomes a run of short declaratives. Never drop a figure, a name or a citation to fit that.
  **Paragraphs run 3–5 sentences and never more than 6** (owner, 2026-10-26) — depth comes from
  sentences per paragraph, not from longer sentences.
  **Gloss every specialist term in place while drafting** — `skills/executive-editor.md` carries the
  term table, and `scripts/check_accessibility.py` hard-fails at publish on an unglossed term from it
  (F1, dedupe, embedding, KV cache, p50–p99 …). Terms outside the table still have to be glossed on the
  way in — nothing downstream catches "call site", "ratchet" or "Btu". The gloss goes at first use,
  inside that sentence; a glossary at the end does not count.
- **The title's content words must appear verbatim in the first ~600 words — inflections do not
  count.** `headline_score.lead_delivery` reads them as plain substrings, so "serves" in a title
  against "served" in the lead scores 100 STRONG standalone and `lead_ok: False` at the push. Score the
  title with `python3 scripts/headline_score.py '<title>'`, and `lead_ok` with
  `python3 -c "import headline_score as hs; print(hs.score('<title>', body=open('<draft>').read()))"`.
  Up to `max(1, len(content_words)//3)` may be absent; every one after that re-cuts the title.
- **Budget every figure across sections while drafting.** `python3 scripts/article_shape.py <draft>`
  allows one money figure in at most two of the five sections, so a third mention anywhere reds the
  gate with "restated in 3 sections". Give each numbers bullet a *different* figure from the same
  source, and refer to a figure already spent by name rather than by number in later sections.
- **Observer cues need a first-person verb, not a first-person pronoun.** `check_social_voice.mjs`
  matches `I` followed by a verb plus its labelled-opinion and attention families, so "What gives me
  pause is…" fails while reading exactly like a cue. Write "What I find hard to square is…".
- Use the section markers **verbatim** — the Stylist iterates per section and `verify.sh` checks them.
  **A draft must emit `<!-- tldr -->` itself:** the set is gated on the *draft* as well as the
  `_final.md`, so a draft without it fails `verify.sh` §2 while every later stage looks green. The five
  are `lead`, `tldr`, `tension`, `tactical-insight`, `nuanced-takeaway`; check with
  `grep -o '<!-- [a-z-]* -->' <draft>` before the accessibility gate.

### 3.5 Readability law (owner, 2026-11-06) — every sentence parses on the first read

Held by `scripts/readability_critic.py` (structure/bullets/citations at the push; the prose findings go
back through the rewrite). Worked examples and incidents: casebook.

**A. Never trade clarity for a clever parallel.** No abstract symmetry (*"a gate is one shared function
rather than a share of one"*): **subject → active verb → concrete object**, consequence in the same
sentence. Three prepositional phrases in a row is a riddle — write two short facts.
**B. State the timeline once, then speak in windows.** Dates and countdown math in paragraph 2 only
(initial event → initial deadline → current extension), then *"the 12-day window"*; never re-explain
the calendar and never open on an ambiguous relative day.
**C. Keep domain terms exact and gloss them in place;** if the source names the method, use its name.
**D. No cold concept in the closing** — no unexplained rule, billing mechanism or technical idea in the
last paragraph; carry a 5–10-word inline bridge instead.
**Citation hygiene:** at most one `[n]` per sentence, `## Sources` vertical — two tags fails.

### 3.6 Diction and structure law (owner, 2026-11-07, every vertical) — the reader must not translate your nouns

`scripts/readability_critic.py` holds all five checks (`jargon`, `enumeration`, `matrix`, `sources`,
enforced from 2026-11-07). Banned list and incidents: casebook.

**A. Name the thing, never a metaphor for it** — *session state*, *systems architects*, *the protocol
layer*. Banned (hard fail): "the fact" for state, "hop owners", "the wire", "the line moved". The test
is lookup, not taste. **B. Ground every entity at first mention** — a 5–10 word functional anchor where
it first appears (*"Google's Agent-to-Agent (A2A) protocol…"*, *"the line-count tool (cloc)"*), never
in a glossary or in Sources; covers alphanumeric tokens and lowercase tool names.
**C. Enumerate what the heading promises** — a heading carrying a count labels every item, in order,
at the top of the section. **D. Compare in a table, not in a paragraph** — two or more options across
three or more variables = a Markdown matrix, one row per option.
**E. One architectural idea per clause; 22 words a sentence on average** — plain-word swaps before
splits, and split only sentences over 28 words.

## 4. Output schema
`context/drafts/YYYY-MM-DD_<slug>_draft.md` — the order below is the gate's order:
```markdown
---
title: <short punchy initial headline>
vertical: <id>
meta_title: <headline in <=60 chars>        # optional to author; persistence derives it
meta_description: <140-160 chars>           # optional to author; persistence derives it
primary_keyword: <target keyword>           # the title must contain it
secondary_keywords: [<kw>, <kw>]
kind: news            # news | evergreen | review — what the CMS push TAGS the post with
persona: <id from context/personas.json>
one_big_thing: "<1-2 plain, punchy sentences under 35 words: what happened, and what it means for the reader>"
date: YYYY-MM-DD
slug: <slug>
# Synthesis articles only (Angle Type: Synthesis — see §3, gated by verify.sh §8):
# synthesis: true
# sources:
#   - <Signal A's primary anchor URL>
#   - <Signal B's primary anchor URL>
---
```

<!-- lead -->
<core thesis AND its operational impact in sentence 1 — concrete, plain, no heading>

<!-- tldr -->
## At a glance
<one plain paragraph, 20–50 words: what the article is about — subject, who it concerns, the one finding>
<!-- tension -->
## <a header that says what this section argues>
<paragraph 2: the timeline ONCE — initial event → initial deadline → current extension — then the
mechanism: why now, who it hurts, who it helps>

## By the numbers
- **<figure> <noun phrase>:** <one clause saying what it counts> [1]

<!-- tactical-insight -->
## <what to watch>
<the operational caveats and forward triggers — reported, never prescribed>

<!-- nuanced-takeaway -->
## The catch
<the honest limitation / counter-argument — self-contained, no cold concept in the last sentence>

## Sources
- [1] <publisher/author, "title", date> — <url>

## 5. Failure handling
Draft thinner than ~800 words despite a full brief → the brief is under-sourced; return to the
verifier, not to padding. Log the gap to `skills/self_improvement_eval.md`.

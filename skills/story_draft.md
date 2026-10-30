# SKILL: Story Draft (Structural First Pass)

## 1. Objective
Assemble the verified brief into an authoritative structural draft using **only** the VERIFIED
evidence set. No new facts. Provide clear inputs for the Stylist's Smart Brevity rewrite.

## 2. The house structure
| Section | Rule |
|---|---|
| **Title** | A headline that earns the click, scored by `scripts/headline_score.py` (owner's standard, 2026-10-10) and gated at the push — **for articles from 2026-10-10 on: earlier headlines are grandfathered and only reported, never re-cut** (`ENFORCED_FROM`). **Core headline ≤ 6 words** before any colon/dash subtitle, whole title ≤ 10 words and ≤ 60 characters, **never open on "The/A/An"**, front-load the strongest noun or the most concrete benefit, carry a hook (a curiosity gap or loss aversion — the mistake, the trap, the silent cost — or invert the conventional wisdom), anchor on a figure the article itself states (never invented), and call the reader out ("your/you", or a named role/subject: CFO, shipper, homeowner, SpaceX). The strongest headlines in the corpus read *"California FAIR Plan Premiums Jump 29.1%"*, *"Why 70% of Startup Options Go Unexercised"*, *"Nearshoring Doesn't Move the Trade Case"*; the weak ones are 11–17 words, open on "The", and state a fact with no reason to open it. No bait-and-switch: the article must satisfy the title in its first paragraph. When drafting for an SEO keyword (`primary_keyword:` in frontmatter), the title MUST contain the target keyword. For **Synthesis articles**, the collision thesis goes in the subtitle, not by stacking both clauses into the headline. |
| **Lead** | A concrete incident or figure from the evidence delivering the core news in sentence 1. For **Synthesis articles**, write a **Collision Lead**: bridge the two underlying developments in the first 1–2 sentences (e.g., *"As frontier model inference prices plunge past 80% cuts, enterprise engineering teams are quietly turning their backs on off-the-shelf SaaS to build bespoke in-house software."*). Not a definition, not a "world is changing" opener. |
| **Tension** | The systemic reason this is happening now — who it hurts, who it helps, what changed (**Why it matters / The big picture**). In a synthesis piece, explain the friction point where Trend A radically alters the economics, reliability, or feasibility of Trend B. |
| **By the numbers** | Mandatory quantitative data section (**By the numbers:**) highlighting 2–4 verified figures, percentages, benchmarks, or cost changes in clean, bolded scannable bullets. In synthesis articles, bullets must represent verifiable data from **both** underlying anchors. |
| **Tactical insight** | What the people closest to the story are doing, what the consequences land on, and the next signals to watch — reported, never prescribed (`persona:` from `context/personas.json`). Signpost it **Where this bites:** / **What I'd watch:** and bulletize 3+ points. Never instruct the reader (`skills/claude_humanizer.md` §3.9). |
| **Nuanced takeaway** | The honest limitation or counter-argument (**The catch / Between the lines**). Ends on substance, not a cheerlead. |
| **TL;DR (At a Glance)** | A **≤50-word** box, three lines: **The shift / The number / The risk**. It states what changed, the figure that proves it and the one caveat — it never re-lists the tactical section's watch items (owner standard 2026-10-29: a recap the reader just read is scroll friction, not emphasis). **Long-form only.** |

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
- **Mandatory 'By the numbers:' section:** Every story must include a bolded `**By the numbers:**` section containing 2–4 scannable bullets with bold lead-ins pairing the figure with a concise 2–4 word metric title before an em-dash or colon (e.g. `- **88% — Diesel price jump:** ...` or `- **21% to 29.5% — UPS fuel fee:** ...`). Never start bullet explanations with narrative filler ("Diesel fuel started the year...", "The leap in the..."). This delivers load-bearing data cleanly and ensures automated SVG charts display meaningful, untruncated labels.
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
- **At a Glance (TL;DR) Schema — a 50-word box, not a second summary (owner standard 2026-10-29):**
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
- **Pre-tune the draft to the accessibility floor before Loop 3.** Run
  `python3 scripts/check_accessibility.py <draft>` on the structural draft you just wrote. A draft that
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
  **Gloss every specialist term in place while drafting** — the gate's jargon list is nearly empty,
  so nothing downstream catches "call site", "ratchet", "Btu" or "goods-receiving"; the fix has to
  happen on the way in (`executive-editor` skill carries the standard and the term table).
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

## 4. Output schema
`context/drafts/YYYY-MM-DD_<slug>_draft.md`:
```markdown
---
title: <short punchy initial headline>
vertical: <id>
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
<concrete incident/stat — core news delivered immediately in sentence 1, hook first, no heading>

<!-- tension -->

## The big picture:

<the systemic shift / why now>

## By the numbers

- **<Stat 1> — <Metric Title>:** <concrete context and citation [1]>
- **<Stat 2> — <Metric Title>:** <concrete context and citation [2]>
- **<Stat 3> — <Metric Title>:** <concrete context and citation [3]>

<!-- tactical-insight -->

## What I'd watch:

<the doable moves — structured cleanly for the persona>
- **<Move 1>:** ...
- **<Move 2>:** ...

<!-- nuanced-takeaway -->

## The catch

<the honest limitation / counter-argument>

<!-- tldr -->

## At a glance

**The shift:** <what changed — one sentence, under 50 words for the whole box>
**The number:** <the figure that proves it, already stated in the body>
**The risk:** <the one caveat that matters>

## Sources
[1] ...  [2] ...
```

## 5. Failure handling
Draft thinner than ~800 words despite a full brief → the brief is under-sourced; return to the
verifier, not to padding. Log the gap to `skills/self_improvement_eval.md`.


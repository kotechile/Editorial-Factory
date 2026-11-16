# SKILL: Evergreen Track (Loop 1E — Useful, Durable Topics)

## 1. Objective

Publish one **useful, durable** article for a vertical: a topic a reader would search for and act
on months from now. Not a news sweep.

The news pipeline (`skills/radar_30day.md` → `skills/virality_judge.md`) is built to find a fresh
30-day signal; its gate weights **Novelty 0.40** and drops anything whose load-bearing claim is
older than the window. That is correct for news and wrong for everything else: it is why verticals
whose beat is periodic (annual surveys, statute books, procurement cycles) returned
*"no publish"* week after week, and why the runs logged *"undated evergreen; not anchored to
window"* while discarding material readers actually want.

This track exists because those are two different products. **The news gate does not run here** —
do not score Novelty, do not run `synthesize_topics.py --seed`, do not widen a window. And the
converse holds: a topic whose value expires inside ~90 days is a news story, and belongs in the
news pipeline, not here.

## 2. What makes a topic admissible

Come to the topic from evidence, never from your own idea of what would be interesting. Any of
these is a legitimate lead; a topic with none of them is an invented topic and is refused:

| Lead | Where it lives |
|---|---|
| The vertical's own beats | `primary_angles` in `context/verticals.json` |
| What the reader is trying to decide | the persona's `wants` in `context/personas.json` |
| The founder's standing positions | `context/growth_os/founder-voice.md` §2 (content pillars) and §3 (per-vertical angles) |
| Real field friction with numbers | `context/growth_os/customer-truth.md` (per-vertical anecdotes) |
| Recurring non-news material | the intel feeds' `product_evaluations` / `market_metrics` (via `scripts/home_lifestyle_intel_client.py`, `scripts/supply_chain_intel_client.py`) |
| Demand the site is already close to winning | `scripts/gsc_analyzer.py --vertical <id> --export-md` — **bonus signal only**: impressions are thin on a young site, so low volume never vetoes a good topic |

## 3. The Evergreen Gate (hard)

Mechanical floor, enforced by `scripts/evergreen_gate.py` — a `PASS` there is required before a
single word of prose is drafted:

- **≥ 3 distinct primary sources** (`MIN_SOURCES`), on **≥ 2 distinct hosts** (`MIN_HOSTS`). Three
  pages of one vendor's site are one source wearing a costume.
- **Every cited source is fetched and must actually contain the figure it is cited for.** Not the
  URL pattern, the page. A paywalled, PDF-only or 404 source is a failure to fix, not a footnote;
  replace it.
- **A named persona decision** — the sentence the reader is trying to settle. If you cannot state
  it, there is no article.
- **A proven de-dup check** against the last **180 days** (`DEDUP_WINDOW_DAYS`) of this vertical's
  briefs and published articles: name the nearest prior artifact (a date or slug) that exists. The
  gate proves the artifact exists rather than pretending to judge similarity — a token-overlap test
  on a one-line thesis produces both false retreads and false passes.
- **An `as of` date** for any time-bound figure (a price, a rate, a cap, a standard). An undated
  figure is a news fact wearing an evergreen label, and it will be wrong within a year.

**Probe the host before you probe the page.** The gate's fetcher sends a fixed, non-browser
user-agent (`EditorialFactorySourceVerifier/1.0`), and it cannot see a host that answers 403/404 or
renders its prices in JavaScript — a `bls.gov` wage table or a client-rendered rate card fails the
floor no matter how good the figure is. Run the pre-flight on any host you have not already proved
on this beat:

```bash
python3 scripts/host_probe.py --check <url>
```

Then confirm the *figure*, not just the status — a `fetched` row can still be `figure_absent`
(HTTP 200 with a navigation shell or an error stub):

```bash
python3 -c "import sys; sys.path.insert(0,'scripts'); import citation_hub_dossier as c; \
print(c.figure_evidence('<figure>', c.fetch_source('<url>')['text']))"
```

When a host will not fetch, move the beat to a mirror that does (Cornell LII or `ecfr.gov` for
statutes, `onetonline.org` for wages where `bls.gov` 403s, `govinfo.gov` for U.S. Code text), or
drop the candidate. Fetchability is not novelty: the same probe list is reusable across runs, so
having anchors that fetch does not make the topic new.

**Lead every row with the figure the page prints, once.** `figure_evidence` returns the window
around the *first* numeric token in the cell, so a cell that opens on prose, on a word number
outside the small word set, or on a digit that also appears in a banner, a sidebar or a phone
number verifies on the wrong sentence — and the gate still PASSes, so the marker's audit trail
reads as a coincidence. Open the cell with the distinctive figure, keep the headline figure inside
that same sentence, and eye-check the printed excerpt. Row-crafting edge cases (comma-grouping,
mixed ladders, tier rows on a rate card, §-number collisions) are in the casebook.

**The de-dup check is per-vertical; the corpus is not.** `check_dedup` reads this vertical's briefs
and published articles only, so a thesis already published under a *different* vertical passes
cleanly and ships as a duplicate. Before writing a brief, grep the whole corpus for the candidate's
mechanism (`grep -ril "<subject token>" published/ context/recon_proposals/`), read the nearest
hit's `one_big_thing:`, and name that cross-vertical artifact in the `De-dup:` line as
checked-and-dropped. A candidate whose mechanism is already argued anywhere in `published/` is
refused by hand; so is a topic you merely want to write.

**Read the casebook when a host or a row surprises you.** `skills/references/evergreen_casebook.md`
carries the 63 per-beat host probes (which hosts fetch first try, which 403, which carry a
figure but poison the matcher), the matcher's edge cases, and the post-publish incident stories.

Beyond the floor, judge the topic yourself on the four axes and write the score into the brief:

| Axis | Question | Weight |
|---|---|---|
| Usefulness | Does it settle a decision the persona actually faces this year? | 0.35 |
| Durability | Is it still correct in 12 months, with the cited figures dated? | 0.25 |
| Evidence | Are the anchors primary, measured, and about this beat (not vendor claims)? | 0.25 |
| Actionability | Does it carry at least one rule with numbers — a threshold, a payback, a gotcha? | 0.15 |

Composite = round(0.35·U + 0.25·D + 0.25·E + 0.15·A, 1). **≥ 8 → proceed.** Below that, either
sharpen the evidence or return "no publish" and say why. There is no quota: a vertical that has
nothing durable to say this week says nothing.

**Refused outright (these are what "evergreen" degenerates into):**
- a listicle of unverified statistics — that is what `skills/citation_hub.md` is for, and it has its
  own stricter data gate;
- a "complete guide" whose every section restates the same three sources;
- a re-argued version of a published article (see the de-dup rule);
- anything whose honesty depends on a figure you could not fetch.

## 4. Output — the evergreen brief

Write `context/recon_proposals/YYYY-MM-DD_<vertical>_evergreen_brief.md` (the name is load-bearing:
it never collides with the news track's `_signals.md` / `_angle_brief.md`, and
`scripts/verify.sh` discovers briefs by it):

```markdown
# Evergreen Brief: <vertical> — YYYY-MM-DD
**Archetype:** evergreen
**Vertical:** <vertical_id>
**Persona:** <persona_id from context/personas.json>
**Decision the reader is facing:** <the decision + when it bites — >= 40 chars>
**Durability:** <why this is still true in 12 months; state what the figures are *as of*>
**De-dup:** <the nearest prior artifact for this vertical in the last 180 days + why this differs>
**Thesis:** <the one sentence the article must defend>

The field labels are parsed literally by `scripts/evergreen_gate.py`, and four of them are
length-checked: `Decision the reader is facing` **≥ 40 characters**, `Durability` **≥ 60**,
`Thesis` **≥ 30**, `De-dup` **≥ 12** — a thin field is reported as *too thin to be checkable*.
The evidence table is one row per figure, numbered from `1`, and the gate recognises its header on
the words `# | Source | URL | Retrieved | Figure | Measured` (it matches the substrings *source*,
*url*, *retrieved*, *figure*, *measured*, so `Figure/claim it supports` and `Vendor claim or
measured?` are the same header to it).

**Lead:** <which of §2's evidence sources produced this topic, and the specific material>

| # | Source | URL | Retrieved | Figure/claim it supports | Vendor claim or measured? |
|---|---|---|---|---|---|
| 1 | <publisher + title> | https://… | YYYY-MM-DD | <the exact figure> | measured |
| 2 | … | … | … | … | vendor claim |
| 3 | … | … | … | … | measured |

## Candidate topics considered
| Topic | Usefulness | Durability | Evidence | Actionability | Composite | Verdict |
|---|---|---|---|---|---|---|
| <topic> | 9 | 8 | 9 | 7 | 8.4 | **winner** |
| <topic> | 7 | 9 | 6 | 8 | 7.4 | dropped — one anchor is a vendor claim |

## Gate result
<!-- written by scripts/evergreen_gate.py — do not hand-edit; re-run the gate if you edit a row -->
```

Then run the gate:

```bash
python3 scripts/evergreen_gate.py --brief context/recon_proposals/YYYY-MM-DD_<vertical>_evergreen_brief.md
```

Daily, the artifact sweep (no network) — the same command `scripts/verify.sh` runs:

```bash
python3 scripts/evergreen_gate.py --check-artifacts --no-network
```

That sweep fails the build on a brief with a missing or stale marker, which is the tripwire for a
row edited by hand after a PASS.

**The verified brief keeps its own filename — a same-day news run usually already owns the plain one (learned 2026-10-19).** Writing the evergreen verification to `YYYY-MM-DD_<vertical>_verified_brief.md` silently overwrites the news track's file for the same vertical and date; `scripts/test_synthesize_topics.py` then fails the build with the news angle brief's `synthesis:` anchors "absent from" the overwritten file, which reads like a broken synthesis rather than a filename collision. Write `YYYY-MM-DD_<vertical>_evergreen_verified_brief.md` (the shape the 2026-10-05 and 2026-10-12 meio runs used), and if the plain file was already clobbered, restore it from git (`git show <commit>:<path> > <path>`) before committing.

It fetches every row, prints the evidence it found for each figure, and writes the
`<!-- evergreen-gate: -->` marker on pass. **Editing a row after that makes the marker stale, and
`scripts/verify.sh` reads a stale or missing marker as a build failure** — re-run the gate.

**Writing the figure cell so the gate can read it:** the matcher looks for numeric tokens, so a row
whose figure is written in words must *begin* with the number word (`six months — …` matches "six
months" or "6 months"; `at least six months — …` generates no pattern at all and reads as
`figure_absent`). Lead the cell with the figure, then the gloss, and never bury it after prose —
the same row that fails this way will pass once the figure moves to the front.

**Lead the `De-dup:` line with the artifact, not with the word "evergreen" (learned 2026-10-13).**
`evergreen_gate.check_dedup` returns the *first* ref in the line that matches a filename, and its ref
regex accepts any run of 9+ `[a-z0-9-]` characters — so "the published evergreen `2026-10-06_<slug>`"
matches on the word **evergreen** (every `*_evergreen_brief.md` satisfies it) and the marker records
`dedup="matched a prior artifact: evergreen"`: the gate still PASSes, but the audit trail names nothing.
Open the field with the bare slug or date-slug (`` `2026-10-06_<slug>` is this vertical's nearest prior
evergreen artifact … ``) so the marker proves the check the rule intends.

**The `Durability:` field must literally contain "as of" — dating every figure is not enough (learned 2026-10-21).**
A durability paragraph that names "the 2026 Florida Statutes edition", "the 2025 code edition", a page's own
"Verified: Oct. 19, 2026" line and "accident year 2023" still reads `FAIL: does not say what the figures are
true as of` — `evergreen_gate` greps for the phrase, not for dates. Write "§ 627.701 as of the 2026 edition …
ISO loss data as of accident year 2023", and re-run the gate after the edit (the marker goes stale).

## 5. Handoff

Only after `PASS`: `skills/fact_check.md` → `skills/story_draft.md` → `skills/claude_humanizer.md`
→ `scripts/publish.py`. The article keeps the house schema (section markers, `## Sources`, the
LinkedIn variant) and adds two frontmatter flags so the reader surfaces and the audit can tell it
apart from a news piece:

```yaml
kind: evergreen
archetype: evergreen
evergreen: true
```

`kind` is the one the reader-facing tag is built from (`scripts/wp_draft.py resolve_kind_term`
creates the `evergreen` tag on the destination if it is absent); `archetype`/`evergreen` stay as the
internal markers the gates read. The news fleet writes `kind: news`, the review fleet `kind: review`.

Persistence to the site + Supabase is **not** approval-gated. Outbound distribution (LinkedIn /
Ghost / Reddit) waits for the founder's `@Simon approve` gate, exactly as the news track does.

Persistence is one command on the reviewer's accepted file — the `_final.md`, never a `_held.md`:

```bash
python3 scripts/publish.py context/drafts/<slug>_final.md
```

**'No publish' is a legitimate outcome.** A vertical with nothing durable this week says nothing:
state the axis that failed, log the scores, and stop — never pad a thin brief to fill a slot. A
topic whose value expires inside ~90 days is a news story and belongs in the news track.

**After acceptance, re-read what the rewrite can quietly change.** The reviewer compares figures,
citations and quotes, and no gate reads headings, frontmatter flags or the warrant behind a summary
figure — so after every accepted rewrite, check the frontmatter still carries the three flags, the
body still carries exactly one inline internal link, the H2s are the article's own (not the
fallback labels), every enumerated rung and acronym gloss survived, and every figure in
`## At a glance` is still earned by the body beneath it. The full incident set is in the
casebook (§5).

## 6. Failure handling

- **No candidate clears ≥ 8** → return "no publish", log the axes table to
  `skills/self_improvement_eval.md`, and say what evidence was missing. Never pad.
- **A source stops resolving** (moved, paywalled, deleted) → replace the row and re-run the gate;
  never drop the figure's citation and keep the claim.
- **The de-dup names nothing** → look at `context/published_log.md` and
  `context/recon_proposals/*_<vertical>_*` for the last 180 days before re-arguing a thesis you
  already ran.
- **The topic is really news** (value expires in < 90 days) → hand it to the news track; do not
  smuggle it here, where the freshness gate cannot see it.

**Still-live failure rules** (each was learned on a specific run — the narrative and the date are
in `skills/references/evergreen_casebook.md` §6):

- **A rewrite repoints a citation.** `[n]` tags are counted, never read: walk the body against
  `## Sources` one sentence at a time and repoint any claim whose number does not carry it.
- **A hold with `hard=0` is a flow regression, not a bad rewrite** — adopt that attempt and repair
  by hand rather than re-generating; the reviewer only re-voices what it is handed.
- **The observer cue is matched literally.** `\bmy read\b` fires, "my reading" does not, and
  `my read is that` / `the part I keep circling` / `what strikes me here is` are boilerplate.
  Write an original first-person sentence in the *draft*.
- **A quote under 20 characters breaks the quote ledger**, so the paragraph between two of them is
  reported as altered source text. Quote the full verbatim clause in both files, or drop the marks.
- **Recompute every derived figure** (a percentage, a unit conversion, a ratio) from its two
  verified ends, and check every enumerated series item by item — a rewrite can delete the rung
  that earned the headline.
- **An invented internal link passes every gate**: `article_shape` counts any markdown link. Delete
  every site-relative path absent from `context/internal_links.json`, and expect exactly one.
- **The generated `<!-- internal-links -->` block belongs just before `## Sources`** — above
  `<!-- tldr -->` it is measured as prose and holds the push on Flesch.
- **A REST body repair must push HTML** (`wp_draft.md_to_html`), and a same-status PATCH does not
  fire the reader front's rebuild: toggle `status` draft → publish.
- **A post needs its header verified on the rendered front**, not in the CMS: hero URL, the
  `-1024x576` derivative and `og:image` — a failed illustration pass publishes hero-less and a
  later `publish.py` will not repair it.
- **Never let a re-image land on a `-N` filename** — the static front keeps referencing the old
  name; delete the newest attachment and re-upload so WordPress takes the base name.
- **A `finished` deploy is not a built page.** Check the built directory and the deployment log for
  `TimeoutError`/`ERROR`; a new vertical also needs its slug in the front's hand-kept vertical list.
- **A 404 in the first ~10 minutes is build lag**, and 0 `wp-content/uploads` in the verifier's
  text extraction proves nothing — `curl` the rendered page.
- **The alt text is 40–140 characters**, one complete sentence, patched in four places at once
  (sidecar, artifact, media over REST, the Supabase row).

## 7. Recording a lesson

**Record it with `scripts/learn.py`, never by appending to a SKILL.md.** An appended paragraph is
re-read by every future run of this skill, so each lesson that lands here is paid for again on
every brief — that is how this file reached a quarter of a megabyte. File the lesson instead:

```bash
python3 scripts/learn.py --vertical <id> --kind pitfall --text "<the lesson>"
```

(`--kind rule|host`, `--file <md>` for a long one, `--url/--verdict/--note` for a probe result,
`--digest` to rebuild `context/knowledge/DIGEST.md`.) The casebook and the digest are read on
demand. Leave this manual alone unless the *procedure* changed rather than the story.

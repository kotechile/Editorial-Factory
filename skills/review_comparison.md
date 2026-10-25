# SKILL: Review Track (Loop 1R — Quick Reviews & Head-to-Head Comparisons)

## 1. Objective

Publish one **buying-decision** article for a vertical: a quick review of one product, or a
head-to-head comparison of two to four. This is the track that carries the buy link, so it is the
one where an invented number does the most damage.

Two other tracks already exist and neither can produce this:

| Track | Gate | Why it refuses a review |
|---|---|---|
| News (`radar_30day.md` → `virality_judge.md`) | Novelty 0.40, 30-day window | A product's price and runtime are not news. A review submitted here dead-ends on freshness. |
| Evergreen (`evergreen_topics.md`) | Durability, `as of` dates, ≥3 sources | A review is durable *shaped* but its prices are perishable by design; the evergreen gate rewards figures that stay true for a year. |

**The news gate does not run here. The evergreen durability test does not run here.** What runs here
is `scripts/review_gate.py`: prices must be fetched and present in the page cited, the brief must date
them, and no article may claim hands-on use.

## 2. What makes a subject admissible

Come from evidence, never from a product you find interesting:

| Lead | Where it lives |
|---|---|
| The vertical's beats | `primary_angles` in `context/verticals.json` |
| Products the reader is already comparing | the intel feeds' `product_evaluations` (`scripts/home_lifestyle_intel_client.py`), retailer best-seller pages, owner-report threads |
| Demand the site is close to winning | `scripts/gsc_analyzer.py --vertical <id> --export-md` (e.g. "vs", "review", "worth it" queries) |
| A price that just moved | manufacturer or retailer page showing a new price, dated — this is the only *news-shaped* lead admissible here, and it is dated like any other price |
| A spec that contradicts the marketing claim | manufacturer spec sheet vs an independent measured review |

A subject is refused when the only source is the vendor's own marketing page — that is a press
release, not a review — or when the products cannot be bought at a listed price today.

## 3. The two formats

### `quick_review` — one product, ~700–900 words

Answers: *is this the right unit for my situation, and at what price does it stop being one.*

1. **Verdict paragraph** — buy / buy at this price / do not buy, and for whom. No throat-clearing.
2. **Price table** — the one product, list price, street price if it differs, source, `as of` date.
3. **What the spec sheet hides** — 3–4 items: the number the manufacturer leads with and the number
   that actually governs the experience (acre rating vs real-world coverage, peak CFM vs sustained,
   claimed runtime vs runtime at load).
4. **Ownership cost** — consumables, battery replacement, blades, filters, service interval, priced.
5. **Who should not buy this** — a named situation where the cheaper or different unit wins.
6. **What we did not test** — mandatory paragraph (see §5).

### `comparison` — 2–4 products, ~900–1,200 words

Answers: *which of these, for which yard/house/budget, today.*

1. **The pick, stated first** — winner for the default reader, plus the one situation where the
   runner-up wins. Two sentences.
2. **Price table** — every product, price, source, `as of`.
3. **Where they actually differ** — 3 axes that change the decision, not 10 rows of spec-sheet
   parity. Each axis: the numbers, then the consequence.
4. **The trap** — the shared cost the comparison hides (battery platform lock-in, accessory required
   to use the headline feature, subscription tier).
5. **Verdict by situation** — a short table: reader situation → pick.
6. **What we did not test** — mandatory paragraph.

Never more than four products. A five-way is a catalogue, and the gate rejects it.

## 4. The Review Gate (hard)

Mechanical floor, enforced by `scripts/review_gate.py`. A `PASS` is required before prose:

- **Fields:** `Vertical`, `Persona`, `Decision the reader is facing` (≥40 chars), `Format`
  (`quick_review` | `comparison`), `Price as of` (YYYY-MM-DD), `Verdict` (≥60 chars, names a
  product in the table), `De-dup`, `Thesis`.
- **Price table:** every product has a numeric price and an `https://` source page.
- **Every price is backed by a verified evidence row** — the gate fetches the cited page and requires
  the same number to appear in it. A plausible URL next to an invented price fails.
- **≥ 3 verified figures on ≥ 2 distinct hosts.** The specs you compare must be sourced too, not just
  the prices; three pages of one manufacturer's site are one source.
- **`Price as of` within 60 days.** A six-month-old price is a wrong price; refresh the row or drop
  the product.
- **No hands-on claim** — `we tested`, `in our tests`, `our unit`, `hands-on`, `after N weeks of
  testing` are failures. This pipeline has no hardware.
- **De-dup** — name the nearest prior artifact (date or slug) that exists in `published/`,
  `context/drafts/` or `context/recon_proposals/`. Also grep the whole corpus for the products' names
  before writing: a comparison already published under another vertical still competes for the query.

```bash
python3 scripts/review_gate.py --brief context/recon_proposals/YYYY-MM-DD_<vertical>_review_brief.md
```

## 5. Honesty rules (these are the product, not a compliance chore)

1. **Say what the article is.** The "what we did not test" paragraph is mandatory and specific:
   *"This review is built from manufacturer spec sheets, two independent measured reviews and owner
   reports; we did not handle the unit."* One sentence, near the verdict.
2. **Attribute the kind of claim.** Manufacturer-claimed figures, independently measured figures and
   owner reports are three different evidence classes; label them. A dB rating from the box is not a
   measurement.
3. **Prices carry dates.** In the table and in prose ("$1,599 as of 2026-10-20").
4. **No review schema with a rating.** Do not emit `Review`/`AggregateRating` structured data for a
   product this pipeline did not test — that is a false machine-readable claim and a manual-action
   risk. `Product` + `Offer` with the price and `priceValidUntil`, or a plain `ItemList`, is honest.
5. **A negative verdict is a publishable article.** If the numbers say do not buy, that is the
   article. The track's value is that it will say so.
6. **Affiliate disclosure** once links monetize: one line above the first buy link, and only merchant
   links that resolve through the site's own redirect (`/go/<slug>/`), never a raw tracking URL.

## 6. Brief template

```markdown
## Review brief

**Vertical:** yard_robotics
**Persona:** homeowner_pro
**Decision the reader is facing:** whether a $1,599 robot mower replaces a $65-per-cut contract on a
fenced one-acre lawn, once edging labor is priced in.
**Format:** comparison
**Price as of:** 2026-10-20
**Verdict:** Buy the <product> for a fenced acre under light tree cover; the <other> wins only where
the lawn is split across more than three zones.
**De-dup:** 2026-10-20_yard_robotics_signals covers navigation tech; no price comparison published.
**Thesis:** the contract is the benchmark, and the robot only wins after residual edging is priced.

| Product | Price | Source | Note |
|---|---|---|---|
| <product A> | $1,599 | https://<manufacturer page> | 1.5 acre rating, RTK |
| <product B> | $1,299 | https://<retailer page> | 0.75 acre rating, vision |

| # | Source | URL | Retrieved | Figure | Measured |
|---|---|---|---|---|---|
| 1 | <publisher> | https://… | 2026-10-20 | $1,599 | list price on product page |
| 2 | <publisher> | https://… | 2026-10-20 | $1,299 | list price on product page |
| 3 | <independent review> | https://… | 2026-10-20 | 62 minutes | runtime per 7.5Ah pack, measured |
```

The `Figure` cell must be a string that literally appears on the cited page — that is what the gate
checks. **It must also contain a numeral.** `citation_hub_dossier.figure_patterns()` returns no pattern
at all for a phrase with no digits, so a row whose Figure is a quotation ("the only difference being run
time") is reported `figure_absent` however many times the page is re-fetched. Cite a numeric substring
from the same sentence ("two 10-Ah batteries") and put the wording in the `Measured` cell.

## 7. After the gate

- Draft with `skills/story_draft.md` (the shape rules in `context/article_shape.json` apply fleet-wide:
  one figure stated once, a decision link at the close, no figure repeated across sections).
- Frontmatter carries `archetype: review` and `format: quick_review|comparison`.
- Link the vertical's calculator in the verdict block — the review is the top of that funnel, the
  calculator is the bottom.
- Persist with `python3 scripts/publish.py context/drafts/<slug>_final.md`; the CMS draft, the
  category (`wp_category_id` from `vertical_sites`) and the `vertical` term are part of the push.
- **A finished persist is not a finished publication: check the header image and the reader page.**
  `publish.py` completes and pushes the post live even when the illustration director refuses every
  render ("publishing WITHOUT a header"), so a live review can carry no image at all. Recover by
  running `scripts/illustration_creator.py <published artifact> --apply`, then attaching it with
  `scripts/wp_draft.py --slug <slug> --refresh-live` — `publish.py` has no `--refresh-live` flag and a
  routine re-push deliberately skips a live post.
- **The reader front is a static build, so media attached after the first push needs a rebuild.** A
  page built before its featured media existed renders with no hero, and the related-post cards can
  make it look like another article's image. Push an empty
  `ci: re-trigger frontend build for <slug>` commit to `kotechile/wellroost` and re-fetch the live URL
  before reporting — a CMS read-back proves the post, never the page.
- **Read the alt text end to end; the director's alt has come back cut mid-phrase.** The same string is
  stored in four places (`context/assets/illustrations/<slug>/featured.json`, the artifact's
  `image_alt`, the WP media item, and the row's `metadata.illustration.alt_text` /
  `metadata.wordpress.media_alt`); fix all of them or the CMS and the database disagree.
- Flip the run-log row in `context/content_calendar.md`.

## 8. Failure modes seen in this class

- **A comparison where all four "differences" are the same spec restated** — the reader learns nothing.
  Pick axes that change the buy.
- **The vendor's marketing page cited as the independent measurement.** Fetch it and label it.
- **A price that only exists on a marketplace listing with no stable URL.** Use the manufacturer or a
  major retailer page; a listing that disappears takes the citation with it.
- **A verdict that names no product** ("it depends") — the gate rejects it, and so should you.
- **A Figure cell with no numeral** — permanently unverifiable (see §6): the gate reports
  `figure_absent` on a page that plainly contains the text, and re-running never fixes it.
- **A passing frontier rewrite that has lost gated content.** On a 1,047-word comparison the rewrite
  returned PASS and had still dropped the mandatory "what we did not test" paragraph, one of the two
  verdict-block links, and a whole premium sentence (leaving a source uncited), and had flattened a
  conditional ("if both run-time claims describe the same job") into an assertion. A shrink to ~75% of
  the draft is the cue to audit line by line against the verified brief, not just to read the verdict.
- **`humanize_one.py` timing out on attempt 2.** Its `call_gemini` carries a 240 s socket timeout, which a
  1,000-word rewrite with thinking exceeds; drive the draft from a per-draft script that rebinds the
  module-level `call_gemini` to 900 s (`claude_humanizer.md` §7) instead of re-running the stock script
  and losing the attempt trail.

# SKILL: Publisher (Persistence + Distribution)

## 1. Objective
Persist every finished article unconditionally — site + Supabase — in the same run that produced it;
gate only the **outbound distribution** (LinkedIn / Ghost / Reddit) behind `@Simon approve`.

## 2. Persistence (always)
1. Write the final article to `published/YYYY-MM-DD_<slug>.md`.
   The slug is *bare* — `scripts/publish.py::normalize_slug()` strips a leading `YYYY-MM-DD_` if the
   draft's frontmatter carries one, so the filename never doubles the date.
2. Append to `context/published_log.md` via `scripts/publish.py::record_publish()` — six columns
   (`Date | Vertical | Slug | Headline | Reader URL | Distribution`), inserted into the published
   table in place, never appended at EOF.
3. Upsert to Supabase (articles, signals, claims). Never skip this step. `publish.py` calls
   `load_env()` first for exactly this reason: without it the Supabase step degrades to a printed
   "Skipping DB sync." and the article never reaches the DB. If that line appears in a publish log,
   the publish is incomplete — fix the credentials and re-run.
4. Refresh the derived surfaces *in the same pass*. An article that is absent from them is a false
   "not published" everywhere else (the SEO tab, the Growth OS loops), and a hand-maintained copy
   drifts the moment anything is deleted:
   - `python3 scripts/sitemap_sync.py` rewrites `context/sitemap.json` — the SEO tab's index and the
     Growth OS / GSC-feedback input — from `published/*.md`. `verify.sh` §7.5 runs
     `python3 scripts/sitemap_sync.py --check` as a hard gate, so a publish that skips this step
     fails the gate instead of shipping a stale index. Never hand-edit that file.
   - Flip the run-log row in `context/content_calendar.md` for the run that produced the article:
     replace "halted at @Simon approve gate … Held at approval, not distributed." with the publish
     outcome (who authorized, `published/<file>`, publish commit, Supabase row id).
   - Run this persistence pass **as part of the pipeline run**, not after an approval: the reader
     site + Supabase are not gated. `scripts/publish.py` refreshes `context/sitemap.json` for you;
     the run-log flip is the one step it cannot infer, so do it in the same pass.
   - The dashboard surfaces derive the synthesis marker from the artifact frontmatter:
     `/api/articles.json` and the article page report `synthesis` + the `sources` anchors, and the
     page badges a synthesis article as such (both sit behind `PRESSFLOW_AUTH_SECRET` — PressFlow is
     internal, the articles are read on giniloh.com / wellroost.com). So an article whose brief said
     `Angle Type: Synthesis` **must** carry `synthesis: true` and its >= 2 anchors under
     `sources:` in `published/…md` — without the flag it publishes as an unmarked single-signal
     story. `verify.sh` §8 fails the build when the flag is missing
     (`python3 scripts/synthesize_topics.py --check-briefs`).
   - The voice is part of what you publish, and it is gated: the body is a comment on the news and the
     social copy is the same person's observation (`skills/claude_humanizer.md` §3.8/§3.9). Do not
     publish a body whose tactical section is a playbook or whose social block carries verdict
     framing — `verify.sh` §9 (`node scripts/check_social_voice.mjs`) fails the build on either, and
     the article page / distribution cards surface exactly this copy.
5. Commission the article's **featured image** in the same pass, from the same text —
   `scripts/illustration_creator.py`, called by `publish.py` and reported as `[image]` notes (the
   treatment, the verbatim cue it read, the model, the sha256, the credits). This is persistence,
   not distribution: it is **not** approval-gated, but it is also not a template — the treatment is
   chosen per article and must not repeat the last four (`skills/illustration_director.md`).
   Idempotent by content (an unchanged article reuses its image; `--force` regenerates), skippable
   with `--no-illustration` or `ILLUSTRATION_ENABLED=false`, and a failure never blocks the
   publish: `scripts/cron-wp-drafts.sh` re-runs it for artifacts still missing an image *before*
   the CMS push, so a transient kie.ai failure costs a sweep, not a header. The CMS draft then
   carries it — the attachment is uploaded, captioned (alt text/caption/credit) and set as the
   post's `featured_media`, with `metadata.wordpress.media_id`/`media_url`/`media_alt` recorded so
   the next push reuses it instead of duplicating the bytes.
6. **A regenerated visual has to reach the ROW, not just the artifact file.** The connector pushes
   the Supabase row's `content`, and `wp_draft.py --refresh` re-derives the body from that same row —
   so a chart rewritten in `published/<file>.md` (a new `chart_generator.py` revision, or
   `article_assets.py --force-chart`) reaches no reader. Verified live: the artifact carried the
   fixed chart while CMS draft #420 still served the old layout with three ellipsized labels and a
   generic caption. Regenerate the markup from the **row's own** numbers section, splice it in place
   of the existing `<svg>`, assert the serialization *outside* the block is byte-identical, write the
   row, then `python3 scripts/wp_draft.py --slug <slug>` and read the post back. Pass the headline
   explicitly when regenerating from a row — a chart titled from a frontmatter-less body is captioned
   "Verified figures"; `article_assets.inject_chart(..., title=…)` takes it and `publish.py` hands
   over the artifact's `meta_title`.
7. **`scripts/article_assets.py --apply` preserves frontmatter line for line — keep it that way.**
   Its frontmatter reader is a line-based `key: value` parser, so re-serialising the block from that
   dict destroyed a real artifact's `sources:` list (`sources: ""` plus a broken `- https: "//…"`
   line, on 3 artifacts) and churned the quoting of every key the pipeline had written quoted, which
   made a no-op run report every file as rewritten. `_reemit_frontmatter()` now appends only the keys
   the pass derives and returns the artifact byte-identical otherwise, and `test_article_assets.py`
   fails on any artifact a pass would rewrite (14/14 currently unchanged).

## 3. Distribution (prep automatic, posting manual)
- **Preparation is automatic.** The persistence pass ends by seeding the dashboard's Reddit/LinkedIn
  **to-do cards** for every published article — `scripts/publish.py` calls
  `scripts/seed_distribution.py`, which hits the dashboard's idempotent `POST /api/distribution/seed`.
  It adds cards only for articles that have none, never posts, and never resets a status or an
  operator's edit. Run it by hand with `python3 scripts/seed_distribution.py` (`--check` to prove
  coverage, `--refresh` to regenerate the text of `ready` cards only, `--dry-run` to see the call).
- **Posting is manual and operator-driven.** Nothing in this repo posts to Reddit; the cards carry
  the finished text plus a pre-filled submit URL, and an operator copies → posts → marks it done in
  the Distribution tab. LinkedIn is the exception where a switch exists: `LINKEDIN_AUTO_POST=false`
  (default) prints the copy-paste block, `true` + `LINKEDIN_ACCESS_TOKEN` posts via the API.
- **Execution:** run `python3 scripts/publish.py context/drafts/YYYY-MM-DD_<slug>_final.md` (supports `--article-url <url>`, `--promo-url <url>`, `--interactive`, `--no-seed`).
- **External Article & Promo Tool Links:**
  - When the final long-form article is published with illustrations on PressFlow or an external site, supply its URL via `--article-url <url>` (or frontmatter `article_url:`).
  - To cross-promote external tools (e.g. tools generated by the Software Factory), supply `--promo-url <url>` (or frontmatter `promo_url:`).
  - The publisher cleanly embeds both URLs and CTAs into the LinkedIn post before posting or copying.
- **LinkedIn Auto-Post Switch (`LINKEDIN_AUTO_POST`):**
  - **`LINKEDIN_AUTO_POST=true`** (and `LINKEDIN_ACCESS_TOKEN` is set): Automatically post the `<!-- linkedin -->` variant via LinkedIn API (with embedded links and article attachment), capture the returned URN/URL, and record it in `context/published_log.md` and Supabase `live_urls`.
  - **`LINKEDIN_AUTO_POST=false`** (default / unset / `0`): Manual review mode. Skip LinkedIn API calls. Output the formatted LinkedIn post with all embedded links to console/chat in a copy-paste ready block and mark status as manual.
- **Ghost / PressFlow** (optional): `GHOST_ADMIN_API_KEY` + `GHOST_API_URL` → create post, record canonical URL.
- A failed distribution call surfaces an explicit error with the payload — never a silent skip, never a fabricated URL.

## 4. Output
- `published/YYYY-MM-DD_<slug>.md` (carrying the `image_*` frontmatter fields), updated published
  log, Supabase rows (including `metadata.illustration`), the staged image + its brief
  (`context/assets/illustrations/<slug>/`), the CMS draft with its featured image, live URLs (when
  approved).

## 5. Failure handling
- Distribution failure → retry once, then report with the platform's error body.
- Log platform quirks (rate limits, token scopes) to `skills/self_improvement_eval.md`.

## 6. Deploy surface & access control

- `site/server.mjs` is the only public surface. It must keep **no unauthenticated** route except
  `/healthz` and a disallow-all `/robots.txt`: everything else — the dashboard, the article pages,
  the article manifest and the drafts — requires `PRESSFLOW_AUTH_SECRET` (see
  `docs/VPS_WIRING.md` §4), and with the secret unset the app fails closed (503). PressFlow is an
  **internal** dashboard; the articles are exported to the reader sites (`giniloh.com` /
  `wellroost.com`), so a public `/published/*` or `/api/articles.json` publishes a second copy of
  every article on a domain that is not a reader surface. `scripts/test_public_surface.mjs` is the
  gate that keeps that true (`verify.sh` §10), and every response carries `X-Robots-Tag: noindex`.
- Never re-introduce a `POST`/`DELETE` handler above the access-control check at the top of the
  request handler — the check runs before every route.
- A deployment only contains **committed** files (Coolify clones git). A draft that was never
  committed is invisible to the dashboard even after a redeploy, so "the site is stale" usually
  means "the artifact was never committed", not "the deploy failed".
- `context/published_log.md` may only list files that exist in `published/`. The filesystem is the
  source of truth; the log is a record of it. A row for a file that is still in `context/drafts/`
  is a false "published" claim.
- `site/index.html` is one inline script: a duplicate identifier at the top level is a parse-time
  `SyntaxError` that silently disables *every* handler while the page still returns 200. Grep for an
  identifier before adding a helper, and verify dashboard changes with
  `node scripts/verify-dashboard.mjs` (headless browser — `curl` proves nothing about JS).

## 7. Distribution queue (Reddit & LinkedIn)

Distribution is copy-paste, not API: the **📣 Distribution** tab holds one task per place to post,
each with the finished text and a submit web-intent URL. `ready` → `published` | `deleted`, any
state reopenable.

- The queue is the single place a post waits to go out. "Queue to LinkedIn" in the Workspace tab
  writes a task here — not to `linkedin_posts`, whose schema does not accept the dashboard's fields.
- Storage: Supabase `factory_config` key `distribution_queue` (production) or
  `context/distribution_queue.json` (local). In production the Supabase env vars are required —
  the container filesystem is rebuilt on every deploy, so a file-only queue loses the operator's
  marks.
- Generation lives in `site/distribution.mjs` (deterministic; no model calls). Seeding is
  idempotent: it never resets a status or an edit, and `refresh` only rewrites `ready` text.
- Never add a task whose text has not been read: the generated framing is a starting point, the
  operator edits and marks it.


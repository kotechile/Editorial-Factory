# SKILL: Publisher (Persistence)

## 1. Objective
Persist every finished article unconditionally — site + Supabase — in the same run that produced it,
and create its post in the destination CMS (live: status `publish`). There is **no outbound social
distribution step**: the LinkedIn and Reddit channels were removed by the owner on 2026-10-06, so
nothing is queued, posted or held for a distribution approval. The reader sites (`giniloh.com` /
`wellroost.com`, fed by the CMS) are the destination.

**The push is gated (owner, 2026-10-10).** `scripts/wp_draft.py` re-runs the mechanical gates on the
artifact immediately before it publishes — Sources present, no banned AI-tells, the accessibility
floor, the social-voice gate (`scripts/publish_gate.py`) — and scores the headline against the
house standard (`scripts/headline_score.py`; see `skills/story_draft.md`), **for articles dated
2026-10-10 or later: earlier headlines are grandfathered** and only reported. A failing article gets
**one rewrite attempt** (the Loop 3 humanizer, rewiring only the body between the artifact's own
frontmatter and its own `## Sources`); a weak headline is re-cut once from the article's own figures.
If it clears the gate it is published, and if it still fails it is created as a **DRAFT** and
reported — a structurally broken headline (past 13 words or 75 chars) holds the article on its own.
An article is never lost and never published un-evaluated. An already-published post is never
rewritten or demoted by the gate — it is reported. Knobs:
`PUBLISH_GATE=off|report|enforce` (default `enforce`), `PUBLISH_GATE_REWRITES` (default 1).

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
   - The voice is part of what you publish, and it is gated: the body is a comment on the news
     (`skills/claude_humanizer.md` §3.9). Do not publish a body whose tactical section is a playbook
     — `verify.sh` §9 (`node scripts/check_social_voice.mjs`) fails the build on it.
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

## 3. Distribution — removed
There is none. The LinkedIn and Reddit channel — the dashboard's Distribution to-do queue, the
app-promotion catalog/seeding, the `linkedin_posts` rows and the `LINKEDIN_AUTO_POST` switch — was
removed by the owner on 2026-10-06 (it had never posted anything). `scripts/publish.py` writes the
article, the log row, the Supabase row, the featured image and the CMS draft; it posts nowhere,
prints no social copy and reads no social credential.

- **Execution:** run `python3 scripts/publish.py context/drafts/YYYY-MM-DD_<slug>_final.md`
  (supports `--article-url <url>`, `--promo-url <url>`, `--interactive`, `--no-deploy`).
- **External article & promo URLs** (`--article-url`, `--promo-url`, or the `article_url:` /
  `promo_url:` frontmatter keys) are recorded on the Supabase row and the log row. They used to be
  the LinkedIn CTA's links; they are now just where else the piece lives.
- **Ghost** (optional, if you ever wire it): `GHOST_ADMIN_API_KEY` + `GHOST_API_URL` → create post,
  record canonical URL. Not a reader-site path.
- A failed persistence step (Supabase, CMS, image) surfaces an explicit error with the payload —
  never a silent skip, never a fabricated URL.

## 4. Output
- `published/YYYY-MM-DD_<slug>.md` (carrying the `image_*` frontmatter fields), updated published
  log, Supabase rows (including `metadata.illustration`), the staged image + its brief
  (`context/assets/illustrations/<slug>/`), and the CMS draft with its featured image.

## 5. Failure handling
- A failed Supabase / CMS / image step → retry once, then report with the service's error body.
- **A persistence pass is not complete until the Supabase row, the CMS draft and the sitemap are each confirmed from their own surface.** `record_publish()` writes the `published_log.md` line *before* the Supabase, CMS and sitemap steps run, so a `NameError`/exception in a later step leaves the artifact file and the log row in place while the reader surfaces are silently skipped — the run looks half-successful and `✓ Recorded row in published_log.md` prints anyway (verified: a `NameError: name 'live_urls' is not defined` from `main()` after a deleted-feature refactor left `sync_to_supabase` referencing removed state; the abort skipped Supabase + CMS + sitemap for every publish until it was caught). Read the process exit code and the traceback, then confirm each step's own output (`[Supabase] inserted … id=…`, `WordPress draft created: post …`, `sitemap: wrote N articles`). A refactor that removes a feature must leave no call site referencing the state it deleted.
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
- **`publish.py`'s auto-deploy is `git add -A`.** It commits and pushes whatever else is uncommitted in
  the tree — including a half-finished edit — so a bundled in-flight change can turn `main` red under an
  otherwise clean publish (an evergreen auto-deploy shipped a partially-edited `wp_draft.py` and left a
  stale static assertion in `test_wp_draft.py`, which `verify.sh` then fails). When the tree carries
  unrelated WIP, pass `--no-deploy` and let a human push; if a bundle did go out, run
  `bash scripts/verify.sh` and fix or revert the stray edit before reporting the publish green.
- A deployment only contains **committed** files (Coolify clones git). A draft that was never
  committed is invisible to the dashboard even after a redeploy, so "the site is stale" usually
  means "the artifact was never committed", not "the deploy failed".
- `context/published_log.md` may only list files that exist in `published/`. The filesystem is the
  source of truth; the log is a record of it. A row for a file that is still in `context/drafts/`
  is a false "published" claim.
- **The reader sites are static builds, so a CMS change is not live until the frontend rebuilds.**
  `giniloh.com` / `wellroost.com` (Coolify apps `c6sm5gz59a3jnrjg1ouahfp7` / `mln99jwbwspi62huuifloxla`,
  repos `kotechile/giniloh` / `kotechile/wellroost`) fetch every post from the `cms.` host at BUILD
  time (`PUBLIC_WORDPRESS_API_BASE`, `ARG CACHEBUST=1`); the deployed container is a folder of HTML.
  A post trashed or deleted in WordPress therefore keeps answering, keeps its sitemap entry and keeps
  every inbound internal link alive until the next build — `scripts/build_internal_link_index.py
  --check` is what catches that drift (it failed on the 10-05 removal until the index was rebuilt).
  The redirect is the WordPress mu-plugin, not this repo: `wellroost-coolify-redeploy.php` /
  `giniloh-coolify-redeploy.php` fire `POST /api/v1/deploy {"uuid":…,"force":true}` on the Coolify API
  (`https://coolify.giniloh.com`). Since 2026-10-05 they also fire when a post LEAVES publish, is
  permanently deleted, or has a published post edited (debounced 10 min) — before that only a
  transition INTO publish rebuilt, so a removal was silent. Trigger one by hand whenever a CMS change
  must reach readers immediately; `GET /api/v1/deploy` is gone, it is a POST (see `docs/VPS_WIRING.md`).
- `site/index.html` is one inline script: a duplicate identifier at the top level is a parse-time
  `SyntaxError` that silently disables *every* handler while the page still returns 200. Grep for an
  identifier before adding a helper, and verify dashboard changes with
  `node scripts/verify-dashboard.mjs` (headless browser — `curl` proves nothing about JS).

## 7. Removed surfaces (do not re-add)

The owner removed the LinkedIn/Reddit distribution channel on 2026-10-06 and it is a deliberate
deletion, not drift. Do not rebuild it: the 📣 Distribution tab, `/api/distribution/*`,
`site/distribution.mjs`, `scripts/seed_distribution.py`, `context/promoted_apps.json`, the
`linkedin_posts` write path and `LINKEDIN_AUTO_POST` are gone on purpose. Nothing in this repo
posts to a social platform, and no run waits for an approval before the article reaches the reader
site. If a social channel is ever wanted again, it is a new decision with a named destination.


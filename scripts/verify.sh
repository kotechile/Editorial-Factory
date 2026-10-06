#!/usr/bin/env bash
# Editorial quality gate. Fails (non-zero) on any violation.
# Checks: config JSON validity, banned AI-tells, draft section schema, missing citations.
set -euo pipefail

ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
FAIL=0

# 1. Config JSON must parse.
for f in "$ROOT/context/verticals.json" "$ROOT/context/personas.json" "$ROOT/context/sitemap.json" "$ROOT/context/gsc_performance.json" "$ROOT/context/growth_os/gsc_sample_data.json"; do
  if [ -e "$f" ]; then
    if ! python3 -m json.tool "$f" >/dev/null 2>&1; then
      echo "FAIL: invalid JSON — $f"; FAIL=1
    fi
  fi
done

# 1.5 Growth OS knowledge files must exist
for f in "$ROOT/context/growth_os/founder-voice.md" "$ROOT/context/growth_os/customer-truth.md"; do
  if [ ! -f "$f" ]; then
    echo "FAIL: missing Growth OS file — $f"; FAIL=1
  fi
done

# 2. Banned AI-tells (from skills/claude_humanizer.md negative constraints).
BANNED=(
  "in today's fast-paced" "in an era of" "it's no secret that" "it's important to remember"
  "furthermore" "moreover" "delve into" "dive deep" "let's explore" "in conclusion"
  "in summary" "game-changing" "cutting-edge" "revolutionary"
)
for phrase in "${BANNED[@]}"; do
  hits=$(grep -rli "$phrase" "$ROOT/context/drafts" "$ROOT/published" 2>/dev/null || true)
  if [ -n "$hits" ]; then
    echo "FAIL: banned phrase '${phrase}' in:"; echo "$hits"; FAIL=1
  fi
done

# 3. Every draft must carry the section schema (markers + Sources). The `<!-- linkedin -->`
#    social variant is no longer required — the LinkedIn/Reddit channels were removed on
#    2026-10-06 — and artifacts written before that still carry it; nothing here rejects it.
SCHEMA_MARKERS=(
  '<!-- lead -->' '<!-- tension -->' '<!-- tactical-insight -->'
  '<!-- nuanced-takeaway -->' '<!-- tldr -->'
)
for f in "$ROOT"/context/drafts/*.md; do
  [ -e "$f" ] || continue
  for m in "${SCHEMA_MARKERS[@]}"; do
    if ! grep -qF "$m" "$f"; then
      echo "FAIL: missing '$m' — $f"; FAIL=1
    fi
  done
  if ! grep -qE '^## Sources' "$f"; then
    echo "FAIL: missing '## Sources' — $f"; FAIL=1
  fi
done

# 4. Every published article must carry a Sources section.
for f in "$ROOT"/published/*.md; do
  [ -e "$f" ] || continue
  if ! grep -qE '^## Sources' "$f"; then
    echo "FAIL: missing '## Sources' — $f"; FAIL=1
  fi
done

# 5. Accessibility report (advisory by default). Dense prose is corrected at Loop 3 per
#    skills/claude_humanizer.md §7. Set STRICT_ACCESS=1 to make it a hard gate.
ACCESS_STRICT="${STRICT_ACCESS:-0}"
for f in "$ROOT"/context/drafts/*.md "$ROOT"/published/*.md; do
  [ -e "$f" ] || continue
  acc=$(python3 "$ROOT/scripts/check_accessibility.py" "$f" 2>&1 || true)
  verdict=$(printf '%s\n' "$acc" | tail -1)
  echo "  access: $verdict  $(basename "$f")"
  if [ "$ACCESS_STRICT" = "1" ] && printf '%s' "$acc" | grep -q "VERDICT: FAIL"; then
    echo "FAIL (strict access): $f"; FAIL=1
  fi
done

# 5.5 SEO Keyword in Title Gate (hard gate): Every draft/published article declaring primary_keyword must contain it in its title.
for f in "$ROOT"/context/drafts/*.md "$ROOT"/published/*.md; do
  [ -e "$f" ] || continue
  if grep -qE '^primary_keyword:' "$f"; then
    if ! python3 -c "import sys, pathlib; sys.path.insert(0, '$ROOT/scripts'); import check_accessibility as ca; res = ca.check_title_keyword(pathlib.Path(sys.argv[1]).read_text()); sys.exit(0 if res[0] else 1)" "$f"; then
      echo "FAIL: SEO title missing primary_keyword — $f"; FAIL=1
    fi
  fi
done

# 6. Helper and publishing scripts must compile cleanly.
for py in "$ROOT/scripts"/*.py; do
  [ -e "$py" ] || continue
  if ! python3 -m py_compile "$py" >/dev/null 2>&1; then
    echo "FAIL: python syntax error — $py"; FAIL=1
  fi
done

# 7. Cron parity gate (hard gate): one live `Full Pipeline: <vertical>` job per registry
#    vertical, on the registry's cadence. Catches the drift class that let 22 verticals
#    sit unscheduled (a create-only sync skipped jobs by name, so registry edits never
#    reached the live fleet). Skips only when there is no scheduler state at all (the
#    deploy container) — never on a real mismatch.
if [ -e "${HERMES_CRON_JOBS:-$HOME/.hermes/cron/jobs.json}" ]; then
  if ! python3 "$ROOT/scripts/sync_crons.py" --check; then
    echo "FAIL: cron drift — run 'python3 scripts/sync_crons.py' to reconcile"; FAIL=1
  fi
else
  echo "  skip: cron parity gate (no scheduler state on this host)"
fi

# 7.2 Off-peak gate (hard gate): DeepSeek bills weekday tokens at 2x inside 01:00-04:00 and
#     06:00-10:00 UTC, and the scheduler reads cadence hours on the host clock (UTC here), so no
#     scheduled job that makes a model call may fire in those windows. Covers the whole live fleet
#     — watchdogs, one-shots and interval jobs, not just the registry-reconciled pipelines — and
#     fails if the host clock has stopped being UTC, because that silently re-labels every cadence.
#     `no_agent` script jobs are exempt: they make no model call. Skips when no scheduler state
#     exists on this host (the deploy container).
if ! python3 "$ROOT/scripts/check_offpeak_crons.py"; then
  echo "FAIL: off-peak gate — a scheduled job spends 2x tokens in a DeepSeek peak window"; FAIL=1
fi

# 7.5 Sitemap drift gate (hard gate): context/sitemap.json is derived from published/*.md
#     (scripts/sitemap_sync.py) and feeds the SEO tab + Growth OS loops. Hand-maintained it
#     advertised four deleted articles and hid everything published since the fresh start.
if ! python3 "$ROOT/scripts/sitemap_sync.py" --check; then
  echo "FAIL: sitemap drift — run 'python3 scripts/sitemap_sync.py' to regenerate"; FAIL=1
fi

# 8. Synthesis gates (hard). scripts/synthesize_topics.py is an advisory pairing pre-filter, so the
#    properties that make it safe to ship are: it cannot clear the >=8 gate itself, its fixtures may
#    not invent citations, and any committed synthesis artifact carries two verified anchors. The
#    regression suite pins the defects it was rewritten to remove (constant gate-clearing scores,
#    cross-domain substring collisions like carrier/port, canned theses, fabricated demo sources).
#    A brief that declares `Angle Type: Synthesis` must also reach its draft/published artifact as
#    `synthesis: true` + >= 2 anchors in the frontmatter `sources:` list, so a fused thesis can never
#    ship indistinguishable from a single-signal story.
if ! python3 "$ROOT/scripts/test_synthesize_topics.py" >/dev/null 2>&1; then
  echo "FAIL: synthesis helper regression suite — detail:"; python3 "$ROOT/scripts/test_synthesize_topics.py" 2>&1 | tail -6; FAIL=1
fi
if ! python3 "$ROOT/scripts/synthesize_topics.py" --check-fixtures; then
  echo "FAIL: a synthesis fixture cites a source absent from the committed signals files"; FAIL=1
fi
if ! python3 "$ROOT/scripts/synthesize_topics.py" --check-seed; then
  echo "FAIL: a signals file written since $(python3 -c "import sys;sys.path.insert(0,'$ROOT/scripts');import synthesize_topics as s;print(s.SEED_ENFORCED_FROM)") has no pair-seeding block, or its block is stale"; FAIL=1
fi
if ! python3 "$ROOT/scripts/synthesize_topics.py" --check-briefs; then
  echo "FAIL: synthesis brief/draft anchoring (see messages above)"; FAIL=1
fi
if ! python3 "$ROOT/scripts/test_sync_crons.py" >/dev/null 2>&1; then
  echo "FAIL: cron fleet contract tests — detail:"; python3 "$ROOT/scripts/test_sync_crons.py" 2>&1 | tail -6; FAIL=1
fi
if ! python3 "$ROOT/scripts/test_check_offpeak_crons.py" >/dev/null 2>&1; then
  echo "FAIL: off-peak gate contract tests — detail:"; python3 "$ROOT/scripts/test_check_offpeak_crons.py" 2>&1 | tail -6; FAIL=1
fi

# 8.5 WordPress draft-push mapping (hard): the vertical -> CMS routing and the field contract that
#     stops a raw vertical id reaching a live headline (scripts/wp_draft.py). Runs a stub WordPress
#     REST API on localhost, so it needs no credentials and writes nothing; the read-only Supabase
#     section skips itself when Supabase is unreachable, so a network hiccup cannot red the gate.
if ! python3 "$ROOT/scripts/test_wp_draft.py" >/dev/null 2>&1; then
  echo "FAIL: wp_draft mapping tests — detail:"; python3 "$ROOT/scripts/test_wp_draft.py" 2>&1 | tail -8; FAIL=1
fi

# 8.55 Derived article assets (hard): every artifact that reaches a destination carries a
#      meta_description (the CMS excerpt / the frontends' <meta name="description">) and a chart when
#      its own numbers section is a real series. The drafting stage is an LLM and emits neither
#      reliably, so both are derived from the artifact's own text (scripts/article_assets.py) — and
#      the rules that stop a chart from inventing a figure are pinned by this suite.
if ! python3 "$ROOT/scripts/test_article_assets.py" >/dev/null 2>&1; then
  echo "FAIL: article-asset tests — detail:"; python3 "$ROOT/scripts/test_article_assets.py" 2>&1 | tail -8; FAIL=1
fi

# 8.56 Featured image (hard, hermetic): the header image is art-directed per article
#      (scripts/illustration_creator.py) — treatment chosen from the text, never repeated
#      back-to-back, no legible text or brand marks in the prompt, alt/caption within budget — and
#      idempotent by content, so a re-run cannot re-spend image credits. The suite stubs both the
#      director and the kie.ai transport: no network, no LLM, no credits. The image binaries are
#      not committed (see .gitignore), so this gate checks metadata and briefs only; whether an
#      artifact HAS an image yet is reported by `illustration_creator.py`, not failed on.
if ! python3 "$ROOT/scripts/test_illustration_creator.py" >/dev/null 2>&1; then
  echo "FAIL: illustration tests — detail:"
  python3 "$ROOT/scripts/test_illustration_creator.py" 2>&1 | tail -8; FAIL=1
fi
# ...and the image binaries stay out of the repo. The CMS media library is their canonical home and
# the staged file is only the upload's source; a 400 KB JPEG per article would bloat a repository
# that commits and deploys on every publish (see .gitignore).
if [ -d "$ROOT/.git" ]; then
  TRACKED_IMAGES="$(git -C "$ROOT" ls-files context/assets/illustrations 2>/dev/null \
                    | grep -E '\.(jpg|jpeg|png|webp)$' || true)"
  if [ -n "$TRACKED_IMAGES" ]; then
    echo "FAIL: generated featured images must not be committed (untrack: git rm --cached <path>):"
    printf '%s\n' "$TRACKED_IMAGES"
    FAIL=1
  fi
fi

# 8.6 Pre-flight data gate (hard): a citation hub may only be drafted on metrics whose headline
#     figure was actually retrieved from the cited primary source. Hermetic run (--no-network):
#     the live audit of the shipped dossiers is a separate, deliberate step —
#       python3 scripts/citation_hub_dossier.py --vertical <vertical_id>
if ! python3 "$ROOT/scripts/test_citation_hub_gate.py" --no-network >/dev/null 2>&1; then
  echo "FAIL: citation-hub data gate tests — detail:"
  python3 "$ROOT/scripts/test_citation_hub_gate.py" --no-network 2>&1 | tail -8; FAIL=1
fi

# 8.65 Evergreen track (hard). The evergreen fleet is a second pipeline whose whole point is the
#      topics the news gate must reject, so its floor is code rather than prose
#      (scripts/evergreen_gate.py, skills/evergreen_topics.md): >= 3 cited primary sources on
#      >= 2 hosts, EVERY one fetched live and shown to contain the figure it is cited for, plus a
#      named persona decision, a de-dup statement naming a prior artifact that exists, and an
#      `as of` date on any time-bound figure. The rules are pinned offline by the suite
#      (stubbed fetch — no network, no credits); the committed briefs are then checked for a
#      FRESH marker only, so the daily gate never makes an outbound request. Editing a row after
#      the gate ran leaves the marker stale and fails here, which is the point: it is the same
#      contract the synthesis seed block uses.
if ! python3 "$ROOT/scripts/test_evergreen_gate.py" >/dev/null 2>&1; then
  echo "FAIL: evergreen gate tests — detail:"
  python3 "$ROOT/scripts/test_evergreen_gate.py" 2>&1 | tail -8; FAIL=1
fi
if ! python3 "$ROOT/scripts/evergreen_gate.py" --check-artifacts --no-network; then
  echo "FAIL: an evergreen brief has no gate marker or a stale one — re-run scripts/evergreen_gate.py --brief <path>"
  FAIL=1
fi

# 8.7 Internal links (hard): candidates come from the live corpus and must be same-site, live, never
#     the article itself, and never a mere domain match — and since the drafting stage cannot know the
#     live corpus, the block itself is generated and delivered by scripts/internal_links.py (hooked
#     into publish.py and wp_draft.py): same rules, plus a two-subject-token evidence bar, an
#     idempotent block under `<!-- internal-links -->`, and reader copy under the marker left intact.
#     The shipped-index section inspects context/internal_links.json without fetching; refresh it with
#       python3 scripts/build_internal_link_index.py
if ! python3 "$ROOT/scripts/test_internal_links.py" >/dev/null 2>&1; then
  echo "FAIL: internal-link tests — detail:"
  python3 "$ROOT/scripts/test_internal_links.py" 2>&1 | tail -8; FAIL=1
fi

# 8.75 Vertical routing (hard, hermetic part): the audit is a pure function of the registry and the
#      routing rows, so the rules are pinned offline — including the WordPress-category coverage
#      (a vertical with no wp_category_id files its drafts under the CMS default, a step the operator
#      otherwise redoes by hand on every post). The live audit runs on the host, where the credentials
#      live: scripts/check_vertical_sites.py, wired into scripts/cron-wp-drafts.sh.
if ! python3 "$ROOT/scripts/test_check_vertical_sites.py" >/dev/null 2>&1; then
  echo "FAIL: vertical-routing audit tests — detail:"
  python3 "$ROOT/scripts/test_check_vertical_sites.py" 2>&1 | tail -8; FAIL=1
fi

# 9. Voice gate (hard): the article body must read as one person commenting on the news — not the
#    owner of the truth and not the reader's advisor (skills/claude_humanizer.md §3.9). Checks each
#    interpreting section of every artifact dated on/after the cutover for an observer cue, and the
#    whole reader-facing body for verdict / consultant / imperative constructions. (The §3.8 rules
#    for the social variants went with the LinkedIn/Reddit channels on 2026-10-06; the same module
#    still owns the long-form rules.) Node is required because the formatter and the rules are both
#    JS; the dashboard cannot run without node either, so this skips only on a host that could not
#    serve PressFlow at all.
if command -v node >/dev/null 2>&1; then
  if ! node "$ROOT/scripts/check_social_voice.mjs" --self-test >/dev/null 2>&1; then
    echo "FAIL: voice rule self-test — detail:"
    node "$ROOT/scripts/check_social_voice.mjs" --self-test 2>&1 | tail -6; FAIL=1
  fi
  if ! node "$ROOT/scripts/check_social_voice.mjs"; then
    echo "FAIL: article voice (see the list above; the rule is skills/claude_humanizer.md §3.9)"; FAIL=1
  fi
else
  echo "  skip: voice gate (node not on PATH)"
fi

# 10. Public surface (hard): PressFlow is an internal dashboard — the articles it holds are exported
#     to the reader sites (giniloh.com / wellroost.com), so the ONLY things reachable without the
#     shared secret are /healthz and a disallow-all /robots.txt. An earlier revision whitelisted
#     `/published/*` and `/api/articles.json` as "the reader surface", which published a second
#     public copy of every article — including the ones still sitting as CMS drafts — on a domain
#     that is not a reader surface. The test spawns the real server on a free port with a throwaway
#     secret and an empty env file, so it needs no credentials and writes nothing.
if command -v node >/dev/null 2>&1; then
  if ! node "$ROOT/scripts/test_public_surface.mjs" >/dev/null 2>&1; then
    echo "FAIL: public surface — detail:"
    node "$ROOT/scripts/test_public_surface.mjs" 2>&1 | tail -8; FAIL=1
  fi
else
  echo "  skip: public-surface gate (node not on PATH)"
fi

if [ "$FAIL" -ne 0 ]; then
  echo "verify.sh: FAILURES FOUND"
  exit 1
fi
echo "verify.sh: OK"

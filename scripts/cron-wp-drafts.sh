#!/usr/bin/env bash
# WordPress Draft Reconciliation + CMS defect check.
#
# Part 0 — featured images. scripts/publish.py commissions each article's header image in the same
# pass that persists it; this sweep re-runs that step for articles still missing one so a transient
# kie.ai failure (or an article published before the step existed) costs a sweep, not a header. It
# runs BEFORE the push below, so the draft reconciled here already carries its image.
#
# Part 1 — drafts. scripts/publish.py creates each article's draft in its destination CMS as part
# of the persistence pass. This sweep is the safety net for the cases where that could not happen:
# the CMS was down, a credential was missing, or the routing row was added afterwards. It selects
# only rows with no metadata.wordpress.post_id, is idempotent (a re-run updates the same post),
# and never publishes — publishing stays a human action in the CMS.
#
# Part 2 — defects. scripts/check_cms_defects.py scans both CMSes for the two defects that were
# previously only caught by hand: a raw vertical id in a live title/slug, and the same article
# sitting on BOTH sites (a stale manual push, or cross-site duplicate content if both are live).
#
# Watchdog contract, mirroring scripts/cron-verify-gate.sh: silent when there is nothing to do and
# nothing is wrong; a short actionable report otherwise. Defects exit non-zero so the job reports
# instead of passing quietly. Runs on the HOST — the WP_* credentials live in the repo .env, which
# the deployed container does not have, so this is deliberately not part of verify.sh.
set -uo pipefail

REPO="${EDITORIAL_REPO:-/root/editorial-factory}"
LIMIT="${WP_DRAFT_LIMIT:-25}"

cd "$REPO" 2>/dev/null || {
  echo "WordPress Draft Sweep: repo not found at $REPO"
  exit 1
}

PROBLEMS=0

# Part 0 — featured images. An article that reached the CMS without one (a transient kie.ai failure,
# a missing key, or an article published before this step existed) gets its header image here, BEFORE
# the push below, so the draft this sweep reconciles carries it. Idempotent by content: an artifact
# whose text has not changed is examined and skipped without spending image credits, which is why
# --limit bounds generations rather than files. Bounded per run because each new image costs credits
# and ~30-60s. Set ILLUSTRATION_ENABLED=false to switch the whole step off; IMAGE_LIMIT=0 walks the
# corpus and reports without generating anything (no spend).
if [ "${ILLUSTRATION_ENABLED:-true}" != "false" ]; then
  IMGS="$(python3 scripts/illustration_creator.py $(ls published/*.md 2>/dev/null) --apply \
            --limit "${IMAGE_LIMIT:-2}" 2>&1)"
  IRC=$?
  if [ "$IRC" -ne 0 ]; then
    echo "WordPress Draft Sweep: featured images FAILED (exit $IRC)"
    printf '%s\n' "$IMGS" | grep -E 'FAIL|Error' | head -6
    PROBLEMS=1
  else
    NEW="$(printf '%s\n' "$IMGS" | grep -c 'illustration written')"
    if [ "$NEW" -gt 0 ]; then
      echo "WordPress Draft Sweep: $NEW featured image(s) generated"
      printf '%s\n' "$IMGS" | grep -E '^    - (direction|generated)' | head -8
    fi
  fi
fi

OUT="$(python3 scripts/wp_draft.py --all --limit "$LIMIT" 2>&1)"
RC=$?

if [ "$RC" -ne 0 ]; then
  echo "WordPress Draft Sweep: FAILED (exit $RC)"
  printf '%s\n' "$OUT" | grep -E 'FAILED|Error|FAIL' | head -8
  PROBLEMS=1
elif ! printf '%s' "$OUT" | grep -q "Nothing to push"; then
  # Drafts were created or updated: one short line each, so the operator knows what is waiting for
  # review in which CMS.
  echo "WordPress Draft Sweep: $(printf '%s\n' "$OUT" | grep -cE '^  (created|updated)') draft(s) touched"
  printf '%s\n' "$OUT" | grep -E '^  (created|updated):' | head -12
fi

DEFECTS="$(python3 scripts/check_cms_defects.py 2>&1)"
DRC=$?
if [ "$DRC" -ne 0 ]; then
  printf '%s\n' "$DEFECTS"
  PROBLEMS=1
fi

# Part 3 — internal-link index. The generator links to the site's real, live pages, so the index has
# to follow the corpus: new articles appear, and a post that stops being live must drop out of the
# candidate pool rather than become a link that sends readers to the homepage. Rebuilding is how
# liveness is re-decided (the sitemap is re-read), so this is a refresh rather than a check.
IDX="$(python3 scripts/build_internal_link_index.py 2>&1)"
IRC=$?
if [ "$IRC" -ne 0 ]; then
  echo "WordPress Draft Sweep: internal-link index FAILED (exit $IRC)"
  printf '%s\n' "$IDX" | tail -6
  PROBLEMS=1
else
  echo "$IDX" | grep -E "indexed|candidate\(s\)" | head -4
  NOT_LIVE="$(printf '%s\n' "$IDX" | grep -cE '^    .* #[0-9]+ ')"
  if [ "$NOT_LIVE" -gt 0 ]; then
    echo "  $NOT_LIVE post(s) published in a CMS but absent from its site's sitemap (frontend not rebuilt):"
    printf '%s\n' "$IDX" | grep -E '^    .* #[0-9]+ ' | head -6
  fi
fi

# Part 4 — routing coverage. Every vertical needs a destination AND a WordPress category: a draft
# pushed with no wp_category_id lands in the CMS's default category (Uncategorized), which is the
# state the operator otherwise re-files by hand on every post — and, missed, a published post that
# appears on no category page and in no listing. Reported here so a routing gap cannot sit silent;
# the fix is the migration it names, then `python3 scripts/wp_draft.py --refresh` to re-file the
# drafts that already exist.
ROUTE="$(python3 scripts/check_vertical_sites.py 2>&1)"
RTC=$?
if [ "$RTC" -ne 0 ]; then
  printf '%s\n' "$ROUTE"
  PROBLEMS=1
else
  printf '%s\n' "$ROUTE" | grep -E "^vertical_sites:|^  [a-z]" | head -4
fi

exit "$PROBLEMS"
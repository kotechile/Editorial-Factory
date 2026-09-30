#!/usr/bin/env bash
# WordPress Draft Reconciliation + CMS defect check.
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

exit "$PROBLEMS"

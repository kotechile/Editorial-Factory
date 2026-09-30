#!/usr/bin/env bash
# WordPress Draft Reconciliation — create any article draft that the in-run hook missed.
#
# scripts/publish.py creates each article's draft in its destination CMS as part of the
# persistence pass. This sweep is the safety net for the cases where that could not happen: the
# CMS was down, a credential was missing, or the routing row was added afterwards. It selects
# only rows with no metadata.wordpress.post_id, is idempotent (a re-run updates the same post),
# and never publishes — publishing stays a human action in the CMS.
#
# Watchdog contract, mirroring scripts/cron-verify-gate.sh: print nothing when there is nothing
# to do and nothing failed (empty stdout = silent, no Slack noise). Print a short actionable
# report when drafts were created or when something failed.
set -uo pipefail

REPO="${EDITORIAL_REPO:-/root/editorial-factory}"
LIMIT="${WP_DRAFT_LIMIT:-25}"

cd "$REPO" 2>/dev/null || {
  echo "WordPress Draft Sweep: repo not found at $REPO"
  exit 1
}

OUT="$(python3 scripts/wp_draft.py --all --limit "$LIMIT" 2>&1)"
RC=$?

if [ "$RC" -ne 0 ]; then
  echo "WordPress Draft Sweep: FAILED (exit $RC)"
  printf '%s\n' "$OUT" | grep -E 'FAILED|Error|FAIL' | head -8
  exit 1
fi

if printf '%s' "$OUT" | grep -q "Nothing to push"; then
  exit 0   # silent = every article already has its draft
fi

# Drafts were created or updated: one short line each, so the operator knows what is waiting for
# review in which CMS. Success is not an error, so the exit code stays 0.
echo "WordPress Draft Sweep: $(printf '%s\n' "$OUT" | grep -cE '^  (created|updated)') draft(s) touched"
printf '%s\n' "$OUT" | grep -E '^  (created|updated):' | head -12

#!/usr/bin/env bash
# Editorial Verify Gate — run the editorial factory's own build gate on a schedule.
#
# Classic watchdog contract: print nothing when everything is green (empty stdout = silent, no
# Slack noise), print a short actionable report and exit non-zero otherwise. Wired to the
# `Editorial Verify Gate` cron job via ~/.hermes/scripts/editorial_verify_gate.sh (--no-agent).
#
# Why this exists: scripts/verify.sh is the repo's hard gate (draft schema, banned AI-tells, SEO
# title keywords, sitemap drift, cron cadence+prompt parity, synthesis seeding/anchoring), but
# nothing ran it on a schedule — a gate nobody runs is documentation. It also checks that the
# pressflow deploy is actually on HEAD, because "auto-deploy enabled" without a live image on the
# newest SHA is exactly the silent failure the fleet has hit before.
set -uo pipefail

REPO="${EDITORIAL_REPO:-/root/editorial-factory}"
APP="${PRESSFLOW_APP:-nstjdswcf5p9xckwja89o6z0}"   # Coolify app: pressflow.aichieve.net
PROBLEMS=()

cd "$REPO" 2>/dev/null || {
  echo "Editorial Verify Gate: repo not found at $REPO"
  exit 1
}

# 1. The repo's own gate.
GATE_OUT="$(bash scripts/verify.sh 2>&1)"
GATE_RC=$?
if [ "$GATE_RC" -ne 0 ]; then
  PROBLEMS+=("scripts/verify.sh failed (exit $GATE_RC)")
  PROBLEMS+=("$(printf '%s\n' "$GATE_OUT" | grep -E '^(FAIL|FAIL:|  FAIL)' | head -8)")
fi

# 2. The deployed image must be the commit that is checked out (auto-deploy silently off/stuck).
HEAD_SHA="$(git rev-parse HEAD 2>/dev/null || echo unknown)"
IMAGE="$(docker ps --format '{{.Image}}' 2>/dev/null | grep -m1 "^${APP}:" || true)"
if [ -z "$IMAGE" ]; then
  PROBLEMS+=("pressflow container for app ${APP} is not running")
elif [ "${IMAGE##*:}" != "$HEAD_SHA" ]; then
  PROBLEMS+=("live image is ${IMAGE##*:} but HEAD is ${HEAD_SHA:0:12} — deploy is behind")
fi

if [ "${#PROBLEMS[@]}" -eq 0 ]; then
  exit 0   # silent = healthy
fi

echo "Editorial Verify Gate: ${#PROBLEMS[@]} problem(s) — repo ${REPO}, HEAD ${HEAD_SHA:0:12}"
for line in "${PROBLEMS[@]}"; do
  [ -n "$line" ] && printf '%s\n' "$line"
done
exit 1

#!/usr/bin/env bash
# kie.ai Claude gateway pre-flight (Loop 3 health gate).
# Usage: scripts/kie_healthcheck.sh [envfile]   (default /root/.hermes/.env)
# Exit: 0 = healthy, 1 = upstream hard-down ("Internal error" on a valid key),
#       2 = key missing, 3 = auth rejected (key invalid/wrong format).
# Never prints the key.
set -uo pipefail
ENVFILE="${1:-/root/.hermes/.env}"

LINE="$(grep -E '^ANTHROPIC_API_KEY=' "$ENVFILE" 2>/dev/null | head -n1)"
VAL="${LINE#ANTHROPIC_API_KEY=}"
VAL="${VAL#\"}"; VAL="${VAL%\"}"; VAL="${VAL#\'}"; VAL="${VAL%\'}"
RAW="${VAL#Bearer }"

if [ -z "$RAW" ] || [ "$RAW" = "$VAL" ]; then
  echo "PREFLIGHT: FAIL — ANTHROPIC_API_KEY missing or malformed in $ENVFILE"
  exit 2
fi

CREDIT="$(curl -s -m 30 -w '\n%{http_code}' https://api.kie.ai/api/v1/chat/credit -H "Authorization: Bearer $RAW")"
CRED_BODY="${CREDIT%$'\n'*}"
CRED_CODE="${CREDIT##*$'\n'}"
echo "PREFLIGHT credit: HTTP $CRED_CODE — $(printf '%s' "$CRED_BODY" | head -c 200)"

if [ "$CRED_CODE" != "200" ] || printf '%s' "$CRED_BODY" | grep -q '"code":401'; then
  echo "PREFLIGHT: FAIL — key rejected (invalid or wrong format)."
  exit 3
fi

PING="$(curl -s -m 60 -w '\n%{http_code}' https://api.kie.ai/claude/v1/messages \
  -H "x-api-key: Bearer $RAW" -H "anthropic-version: 2023-06-01" \
  -H "content-type: application/json" \
  -d '{"model":"claude-sonnet-5","max_tokens":16,"messages":[{"role":"user","content":"ping"}]}')"
PING_BODY="${PING%$'\n'*}"
PING_CODE="${PING##*$'\n'}"
echo "PREFLIGHT messages: HTTP $PING_CODE — $(printf '%s' "$PING_BODY" | head -c 200)"

if [ "$PING_CODE" = "200" ] && ! printf '%s' "$PING_BODY" | grep -qiE '"Internal error|"code":401'; then
  echo "PREFLIGHT: HEALTHY — Claude gateway reachable."
  exit 0
fi

echo "PREFLIGHT: HARD-DOWN — key valid (credit OK) but Claude upstream returns \"Internal error\". Halt Loop 3; do not substitute a non-frontier model."
exit 1

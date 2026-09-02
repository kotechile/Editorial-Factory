#!/usr/bin/env bash
# Editorial quality gate. Fails (non-zero) on any violation.
# Checks: config JSON validity, banned AI-tells in drafts/published, missing citations.
set -euo pipefail

ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
FAIL=0

# 1. Config JSON must parse.
for f in "$ROOT/context/verticals.json" "$ROOT/context/personas.json"; do
  if ! python3 -m json.tool "$f" >/dev/null 2>&1; then
    echo "FAIL: invalid JSON — $f"; FAIL=1
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

# 3. Every published article must carry a Sources section.
for f in "$ROOT"/published/*.md; do
  [ -e "$f" ] || continue
  if ! grep -qE '^## Sources' "$f"; then
    echo "FAIL: missing '## Sources' — $f"; FAIL=1
  fi
done

if [ "$FAIL" -ne 0 ]; then
  echo "verify.sh: FAILURES FOUND"
  exit 1
fi
echo "verify.sh: OK"

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

# 3. Every draft must carry the full section schema (markers + Sources + LinkedIn variant).
SCHEMA_MARKERS=(
  '<!-- lead -->' '<!-- tension -->' '<!-- tactical-insight -->'
  '<!-- nuanced-takeaway -->' '<!-- tldr -->' '<!-- linkedin -->'
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

# 6. Helper and publishing scripts must compile cleanly.
for py in "$ROOT/scripts"/*.py; do
  [ -e "$py" ] || continue
  if ! python3 -m py_compile "$py" >/dev/null 2>&1; then
    echo "FAIL: python syntax error — $py"; FAIL=1
  fi
done

if [ "$FAIL" -ne 0 ]; then
  echo "verify.sh: FAILURES FOUND"
  exit 1
fi
echo "verify.sh: OK"

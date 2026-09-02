#!/usr/bin/env bash
# Manual trigger for the full editorial pipeline for one vertical:
#   Scout -> Judge -> Verify -> Draft -> Claude Rewrite -> (approval gate) -> Publish
# Scheduled runs are Hermes cron jobs (see docs/VPS_WIRING.md).
set -euo pipefail

VERTICAL="${1:-agentic_ai}"

hermes cron run "Full Editorial Pipeline: ${VERTICAL}"

# Alternatively, drive the Editor-in-Chief bot directly in one-shot mode:
# hermes -p editor chat -q "Run the full editorial pipeline for vertical '${VERTICAL}' \
#   per skills/radar_30day.md, virality_judge.md, fact_check.md, story_draft.md, claude_humanizer.md"

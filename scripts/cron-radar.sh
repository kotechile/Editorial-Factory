#!/usr/bin/env bash
# Manual trigger for a single-vertical Radar Scout sweep.
# Scheduled runs are Hermes cron jobs (see docs/VPS_WIRING.md). This wrapper exists for
# manual invocation and Coolify/CI hooks.
set -euo pipefail

VERTICAL="${1:-agentic_ai}"

hermes cron run "Radar Sweep: ${VERTICAL}"

# Alternatively, run the scout bot directly in one-shot mode:
# hermes -p scout chat -q "Run the 30-day radar for vertical '${VERTICAL}' per skills/radar_30day.md"

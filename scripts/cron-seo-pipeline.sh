#!/usr/bin/env bash
# Weekly or on-demand trigger for the SEO Content Machine:
#   GSC Opportunities -> DataForSEO -> Growth OS (Cannibalization + Internal Links + Voice) -> Draft -> Frontier Rewrite -> (@Simon approve)
set -euo pipefail

ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
VERTICAL="${1:-all}"

echo "Executing SEO Content Machine for vertical: ${VERTICAL}..."
python3 "$ROOT/scripts/seo_machine.py" --vertical "${VERTICAL}"

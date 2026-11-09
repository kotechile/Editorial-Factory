import pathlib, sys
sys.path.insert(0, "/root/editorial-factory/scripts")
import humanize_loop3 as h

draft_path = pathlib.Path("/root/editorial-factory/context/drafts/2026-11-09_your-fill-rate-is-a-pallet-price_draft.md")
out = pathlib.Path("/root/editorial-factory/context/drafts/2026-11-09_your-fill-rate-is-a-pallet-price_final.md")
text = draft_path.read_text()
result = h.humanize_single_draft(text, out)
print("WROTE", out, "len", len(result))

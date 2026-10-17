import sys, pathlib, json, urllib.request
sys.path.insert(0, 'scripts')
import humanize_loop3 as hl
import humanizer_tools as ht

# Rebind the module's call_gemini to a 480s socket timeout (the module hard-codes 240s,
# and a thinking-model rewrite of a ~1,200-word piece can exceed 240s).
def call_gemini_long(prompt):
    body = {
        "contents": [{"parts": [{"text": prompt}]}],
        "generationConfig": {"maxOutputTokens": 20000, "temperature": 0.7},
    }
    req = urllib.request.Request(hl.URL, data=json.dumps(body).encode(),
                                 headers={"Content-Type": "application/json"})
    with urllib.request.urlopen(req, timeout=480) as r:
        j = json.loads(r.read().decode())
    return j["candidates"][0]["content"]["parts"][0]["text"]

hl.call_gemini = call_gemini_long

draft = pathlib.Path('context/drafts/2026-10-17_your-disks-35-dead-by-year-six_draft.md')
out = pathlib.Path('context/drafts/2026-10-17_your-disks-35-dead-by-year-six_final.md')
srcs_ok = markers_ok = len_ok = False
res = hl.humanize_single_draft(draft.read_text(), out)
print("WROTE", out, out.exists(), out.stat().st_size if out.exists() else 0)

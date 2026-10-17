import sys, pathlib, urllib.request, json
sys.path.insert(0, 'scripts')
import humanize_loop3 as hl

PRIMARY = "context/drafts/2026-10-17_prior-disclosure-clock-cuts-penalty_draft.md"
OUT = pathlib.Path("context/drafts/2026-10-17_prior-disclosure-clock-cuts-penalty_final.md")


def call_gemini_480(prompt):
    body = {
        "contents": [{"parts": [{"text": prompt}]}],
        "generationConfig": {"maxOutputTokens": 20000, "temperature": 0.7},
    }
    req = urllib.request.Request(hl.URL, data=json.dumps(body).encode(),
                                 headers={"Content-Type": "application/json"})
    with urllib.request.urlopen(req, timeout=480) as r:
        j = json.loads(r.read().decode())
    cand = j["candidates"][0]
    print("   finishReason:", cand.get("finishReason"),
          "thoughts:", cand.get("usageMetadata", {}).get("thoughtsTokenCount"),
          "out:", cand.get("usageMetadata", {}).get("candidatesTokenCount"))
    return cand["content"]["parts"][0]["text"]


hl.call_gemini = call_gemini_480
text = pathlib.Path(sys.argv[1] if len(sys.argv) > 1 else PRIMARY).read_text()
res = hl.humanize_single_draft(text, OUT)
print("WROTE:", OUT, OUT.exists(), OUT.stat().st_size if OUT.exists() else 0)

import sys, json, urllib.request
sys.path.insert(0, "/root/editorial-factory/scripts")
import humanizer_tools as ht

print("MODEL:", ht.MODEL, "MAX_TOKENS:", getattr(ht, "MAX_TOKENS", "?"), "MAX_ATTEMPTS:", ht.MAX_ATTEMPTS)
key = ht._key()
print("key present:", bool(key), "len:", len(key) if key else 0)
print("has LONGFORM_VOICE_RULES:", hasattr(ht, "LONGFORM_VOICE_RULES"))
print("retry_prompt sig ok:", callable(getattr(ht, "retry_prompt", None)))
# 1-token frontier ping (skills/claude_humanizer.md §7 pre-flight)
body = json.dumps({"contents": [{"parts": [{"text": "ping"}]}],
                   "generationConfig": {"maxOutputTokens": 1, "temperature": 0}}).encode()
req = urllib.request.Request(ht.URL, data=body, headers={"Content-Type": "application/json"})
try:
    with urllib.request.urlopen(req, timeout=60) as r:
        d = json.loads(r.read())
    print("PING OK http", r.status, "finish:", d.get("candidates", [{}])[0].get("finishReason"))
except Exception as e:
    print("PING FAILED:", type(e).__name__, e)

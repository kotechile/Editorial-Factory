#!/usr/bin/env python3
"""Probe DeepSeek's automatic prefix cache: does a repeated prefix hit, and does a
one-line change at the head kill the tail? Read-only apart from ~$0.005 of tokens."""
import json, sys, time, urllib.request
sys.path.insert(0, "/root/editorial-factory/scripts")
import frontier_llm

BODY = open("/root/editorial-factory/skills/story_draft.md").read()   # ~8k tokens of real skill text
HEAD = "Run the editorial pipeline for vertical 'probe_a' (Probe A).\n\n"

def call(text, label):
    body = {"model": "deepseek-flash",
            "messages": [{"role": "user", "content": text + "\n\nReply with the single word OK."}],
            "max_tokens": 8, "temperature": 0, "stream": False}
    req = urllib.request.Request(frontier_llm.BASE_URL, data=json.dumps(body).encode(),
                                 headers={"Content-Type": "application/json",
                                          "Authorization": "Bearer " + frontier_llm.key()}, method="POST")
    with urllib.request.urlopen(req, timeout=120) as r:
        payload = json.loads(r.read().decode())
    u = payload.get("usage") or {}
    print(f"{label:34s} keys={sorted(u)}")
    print(f"{'':34s} prompt={u.get('prompt_tokens')} hit={u.get('prompt_cache_hit_tokens')} "
          f"miss={u.get('prompt_cache_miss_tokens')} out={u.get('completion_tokens')}")
    return u

call(HEAD + BODY, "1 cold (vertical A prompt)")
time.sleep(4)
call(HEAD + BODY, "2 repeat (same prompt)")
time.sleep(4)
call(HEAD.replace("probe_a", "probe_b").replace("Probe A", "Probe B") + BODY,
     "3 one line changed at head")
time.sleep(4)
call(HEAD.replace("probe_a", "probe_b").replace("Probe A", "Probe B") + BODY + "\nExtra tail line.",
     "4 same head, longer tail")

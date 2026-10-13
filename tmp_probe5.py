import sys, re
sys.path.insert(0, '/root/editorial-factory/scripts')
import citation_hub_dossier as c

r = c.fetch_source("https://arxiv.org/abs/2302.06590")
t = r['text']
print("COPILOT ABS:", ' '.join(t.split())[:1400])
print()
r = c.fetch_source("https://survey.stackoverflow.co/2025/ai")
t = r['text']
for kw in [r"33,662", r"49,000|49,296|respondents", r"daily 50\.6", r"highly distrust"]:
    for m in list(re.finditer(kw, t))[:2]:
        s=max(0,m.start()-160); print(f"[{kw}] ...{' '.join(t[s:m.end()+160].split())}...")

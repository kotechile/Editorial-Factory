import re, sys, pathlib
sys.path.insert(0, '/root/editorial-factory/scripts')
import check_accessibility as ca
import collections

p = pathlib.Path('/root/editorial-factory/context/drafts/2026-10-13_ai-coding-seats-measure-or-renew_final.md')
body = ca.body_of(p)
print("flesch:", ca.flesch(body) if hasattr(ca, 'flesch') else 'n/a')

def syllables(w):
    w = w.lower()
    w = re.sub(r'[^a-z]', '', w)
    if not w:
        return 0
    v = re.findall(r'[aeiouy]+', w)
    n = len(v)
    if w.endswith('e') and n > 1:
        n -= 1
    return max(1, n)

words = re.findall(r"[A-Za-z']+", body)
counts = collections.Counter(w.lower() for w in words)
multi = [(w, c, syllables(w)) for w, c in counts.items() if syllables(w) >= 3]
multi.sort(key=lambda t: (t[2] * t[1]), reverse=True)
print("top long words (word, count, syll):")
for w, c, s in multi[:40]:
    print(f"  {w:<22} x{c}  {s}syll  weight={s*c}")
print("total words:", len(words))

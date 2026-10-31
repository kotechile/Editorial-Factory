import sys
sys.path.insert(0, 'scripts')
import headline_score as hs

b = open('context/drafts/2026-10-31_two-builds-one-vault_final.md').read()
cands = [
    "Your Vault's 2 Builds: The Side-Load Trap",
    "Your Vault: 2 Builds, 1 Trap",
    "2 Builds, 1 Vault: The License Trap",
    "Your Vault Has 2 Builds: One Is a Trap",
    "Your Vault: 2 Builds, One Free Path",
    "Your Vault's 2 Builds Split the Free Path",
    "Your Vault: 2 Builds, 60-Day Tail",
]
for t in cands:
    r = hs.score(t, body=b)
    print(r['score'], r['verdict'], 'core=%d' % r['core_words'], 'chars=%d' % r['chars'],
          'lead_ok=%s' % r['lead_ok'], r['failures'], '|', t)

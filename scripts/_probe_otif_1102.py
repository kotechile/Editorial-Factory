import sys, re
sys.path.insert(0, 'scripts')
import citation_hub_dossier as c

t = c.fetch_source("https://arxiv.org/html/2602.16842v2")['text']
for cell in ["0.8 — the paper's censored-data comparison is run at a critical fractile of q = 0.8",
             "0.8 — the BSAA policy is evaluated at a critical fractile q = 0.8"]:
    ev = c.figure_evidence(cell, t)
    print('CELL:', cell[:60], '\n   ->', (ev or 'NONE')[:400])

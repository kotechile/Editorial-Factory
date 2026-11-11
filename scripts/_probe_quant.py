import sys
sys.path.insert(0, 'scripts')
import citation_hub_dossier as c

u = 'https://arxiv.org/html/2611.04380v1'
t = c.fetch_source(u)['text']
cells = [
    "1.63 - NVFP4 costs 1.63 MMLU points while INT4 costs 0.43 to 1.43 and every 8-bit delta is at most 0.77",
    "3.9 points - one standard error of a single HumanEval run at n = 164 is about 3.9 points",
    "1.64 - the A100 INT4 gain falls from 2.12x to 1.64x at a 30,720-token prompt",
    "1.68 - on the H20 FP8 pulls ahead of AWQ, 1.68x against 1.42x, because Hopper runs FP8 tensor cores at twice the BF16 rate",
    "28.08 GB - the BF16 Qwen2.5-14B footprint against 9.94 GB for GPTQ-Int4",
]
for cell in cells:
    print('==', cell)
    print('   ', str(c.figure_evidence(cell, t))[:340].replace('\n', ' '))

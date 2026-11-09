from pathlib import Path
row = Path('/tmp/cal_row_pmi_1109.md').read_text(encoding='utf-8').strip()
p = Path('/root/editorial-factory/context/content_calendar.md')
t = p.read_text(encoding='utf-8')
if not t.endswith('\n'):
    t += '\n'
if 'your-pmi-ends-at-78-not-todays-value' in t:
    print('row already present')
else:
    p.write_text(t + row + '\n', encoding='utf-8')
    print('appended', len(row), 'chars')

#!/usr/bin/env python3
"""Final pre-check: every cell of the expat evergreen brief, read exactly as the gate reads it."""
import sys
sys.path.insert(0, 'scripts')
import citation_hub_dossier as c

ROWS = [
 ("1", "https://www.irs.gov/businesses/small-businesses-self-employed/report-of-foreign-bank-and-financial-accounts-fbar",
  "$10,000 - the FBAR is required when the aggregate value of foreign financial accounts exceeded $10,000 at any time during the calendar year reported, and whether the account produced taxable income has no effect"),
 ("2", "https://www.fincen.gov/report-foreign-bank-and-financial-accounts",
  "$10,000 - a filer must file an FBAR if the aggregate value of the foreign financial accounts exceeds $10,000 at any time during the calendar year"),
 ("3", "https://www.irs.gov/businesses/corporations/do-i-need-to-file-form-8938-statement-of-specified-foreign-financial-assets",
  "$200,000 - a taxpayer living abroad files Form 8938 when the total value of specified foreign assets is more than $200,000 on the last day of the tax year, or more than $300,000 at any time during the year (joint return: $400,000 or $600,000)"),
 ("4", "https://www.law.cornell.edu/uscode/text/26/6038D",
  "$10,000 - a failure to furnish the required information carries a penalty of $10,000, and where the failure continues more than 90 days after notice, a further $10,000 for each 30-day period, capped at $50,000"),
 ("5", "https://www.law.cornell.edu/uscode/text/26/6038",
  "30-day period - a continued failure to report a foreign business entity adds $10,000 for each 30-day period after a 90-day notice, and the increase may not exceed $50,000"),
 ("6", "https://www.irs.gov/instructions/i5471",
  "90 days - Form 5471 failures: a $10,000 penalty for each annual accounting period of each foreign corporation, and if the information is not filed within 90 days after the IRS mails a notice, additional penalties apply"),
 ("7", "https://www.law.cornell.edu/uscode/text/31/5321",
  "50 percent - a willful violation raises the maximum penalty to the greater of $100,000 or 50 percent of the account amount"),
 ("8", "https://www.ecfr.gov/current/title-31/subtitle-B/chapter-X/part-1010/subpart-G/section-1010.821",
  "$16,536 - the table applying to penalties assessed on or after January 17, 2025 lifts the non-willful maximum from $10,000 to $16,536 (and the willful $100,000 to $165,353)"),
]

texts = {}
for n, url, cell in ROWS:
    if url not in texts:
        r = c.fetch_source(url)
        texts[url] = r.get('text') or ''
        print(f"[fetch] {r.get('status'):<10} http={r.get('http','')!s:<5} len={len(texts[url]):<7} {url}")
    ev = c.figure_evidence(cell, texts[url])
    print(f"\n  ROW {n}: {cell[:80]}…")
    print(f"    -> {'…' + ev[:250].replace(chr(10),' ') + '…' if ev else '*** ABSENT ***'}")

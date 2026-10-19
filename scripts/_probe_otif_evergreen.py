import sys
sys.path.insert(0,'scripts')
import citation_hub_dossier as c

cells = [
 ("https://goautonomous.io/blogs/b2b-order-exception-handling-why-exceptions-are-where-the-real-cost-hides-in-order-to-cash",
  ["60 to 80 percent — exceptions account for 20 to 40% of order volume and 60 to 80% of total order management cost",
   "30 to 40 percent — visible CSR hours spent investigating and resolving exceptions represent only 30 to 40 percent of the total cost",
   "45 minutes — average resolution time per exception in the vendor's worked example",
   "3 to 5 times — exceptions cost three to five times more per order to process than straight-through transactions",
   "20% of order volume — the decision card says an exception rate above 20% of order volume makes processing overhead structural"]),
 ("https://www.moxo.com/blog/order-exception-management-software",
  ["7.22% — fulfillment failures delay the next customer order by 7.22% on average",
   "$30 — each exception costs approximately $30 to manually resolve",
   "20-40% — customer service representatives spend 20-40% of their time on manual order handling"]),
 ("https://scmr.com/article/how-efficient-is-your-procurement-process/supply-chain-management",
  ["$54.50 — the 75th percentile spends $54.50 to process a purchase order, the 25th percentile about $14, average $42"]),
 ("https://www.onetonline.org/link/summary/43-4151.00",
  ["$22.20 hourly — median wage for order clerks (2025), $46,170 annual"]),
]
for u, cs in cells:
    t = (c.fetch_source(u).get('text') or '').replace('\n',' ')
    print("==", u, len(t))
    for cell in cs:
        ev = c.figure_evidence(cell, t)
        print("  CELL:", cell[:80])
        print("   ->", (ev or "NO MATCH")[:320])

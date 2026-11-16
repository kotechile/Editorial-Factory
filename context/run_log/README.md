# Run-log detail

One file per published article: `YYYY-MM-DD_<slug>.md`.

`context/content_calendar.md` keeps a **cell of at most 900 characters** per run (what shipped, the
score, the gate verdicts, open items). The derivation — query counts, host probes, de-dup greps,
repair passes, media ids — goes here instead, where nothing reads it unless someone asks.

Why: a run-log row is written as output and read back as input on the next run. Free-form prose grew
the calendar to 2.7 MB at 8.5 KB a row; `verify.sh` §11.2 now fails a row over 900 chars dated
2026-11-17 or later, and older rows are grandfathered.

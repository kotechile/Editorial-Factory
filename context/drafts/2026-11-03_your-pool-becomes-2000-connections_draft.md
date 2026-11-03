---
title: "Your Pool Becomes 2,000 Connections"
vertical: enterprise_tech_leadership
kind: evergreen
persona: eng_leader
one_big_thing: "A database connection is a server process holding a per-sort memory budget, so the real ceiling is memory — connections times sorts in flight times work_mem — and because every pod opens its own pool, a pool default copied from a library multiplies by the pod count and can exhaust the database after the code ships."
date: 2026-11-03
slug: your-pool-becomes-2000-connections
archetype: evergreen
evergreen: true
---

<!-- lead -->
One pool setting, copied into twenty pods, becomes 2,000 connections against a database that takes about 100 by default [1]. The pool opens per process. Because an autoscaler sets the pod count later, a test on one pod never shows the total. What you meet instead is a database that refuses new logins, or a report whose sort writes to disk, on the night a deploy scales out. The number that fails was never a database setting. It sits in a framework's config file, where nobody costs it against memory.

<!-- tension -->

## Memory sets the ceiling

Each client connection gets its own backend process, and the connection limit sets how many of those the server will start. The setting that spends memory is work_mem, the room for one sort or one hash table in one query, and it defaults to four megabytes [2]. One query can hold several of them open at once, and many sessions can sort at the same time [2]. So the total can run many times the figure for a single session. The math is short: connections, times sorts in flight, times the room for each.

A managed platform will let you make that math absurd. On Google's service, the connection limit plus two worker settings can be set as high as 262,142 [3]. One four-megabyte sort each would ask for about a terabyte of memory. The servers on that tier carry memory in tens of gigabytes. The dial counts slots, not bytes, and the docs present it as a limit to raise rather than a number to reason from [3].

What I keep circling is how quiet the second failure is. Running out of memory kills a backend and drops the connection, which at least makes noise. The earlier sign is the spill. Once sorts stop fitting, every query that orders or joins writes to disk. Latency climbs while the dashboard shows a healthy database with spare connections. The defaults quoted here come from the PostgreSQL 18 docs, read on 3 November 2026, and they have held for years because the math behind them does not move [1][2].

## By the numbers

- **50 — Server connections per pooler:** a managed pooler runs once per four cores, and each opens up to 50 server connections for one database and user pair, so an eight-core box gets two [4].
- **100 — A pooler's own default:** PgBouncer ships a pool of 100 server connections per user and database pair, and holds one until the client leaves unless the mode is changed [5].
- **262,142 — The config ceiling:** the connection limit plus the autovacuum setting plus the worker setting cannot pass that total on Google's service [3].

<!-- tactical-insight -->

## Where the pool bites

The teams that dodge this treat pool size as a per-pod budget and write it down. The form is short. Pool size times the most pods you will run must fit the server's connection room. That room, split by the sorts a query can hold and times the room per sort, must fit in the memory left after the shared cache. What I look for is a framework default that walks into a deploy chart untouched, because that is how a laptop value becomes a hard cap.

A pooler is the usual answer, and its mode turns the choice into a question of correctness. In session mode one server connection is held until the client leaves, which is the documented default [5]. In transaction mode the connection goes back at commit, which is what lets thousands of clients share a few dozen server connections. It is also what breaks anything that outlives a transaction: prepared statements, session settings, locks, and listeners.

Sizing comes from the same source, not from a vendor tier. The project's long-standing guide keeps active connections near twice the core count plus the spindle count [6]. On a modern box that is a small number next to any pool default. Teams that follow it tend to raise the room per sort for reporting sessions only, and leave the live path at the shipped value.

<!-- nuanced-takeaway -->

## The catch

A smaller pool has a cost the throughput rule hides. Fewer server connections means requests wait, and that rule is about work done per second, not about tail latency [6]. A pool sized for throughput can still miss a tail target on a busy day. Transaction mode buys the sharing at the price of session state, and an app that leaned on a prepared statement or a temporary setting will fail in a way that looks random.

Lowering the room per sort is not a cap either. It limits each sort, not the total, so a fleet of wide queries spends the same memory overall and writes more work to disk. That trade can be right, and it is still a trade: the disk is slower, and input and output becomes the new ceiling.

My read, held loosely: the defaults are the least durable part of this piece, since vendors re-tune them and hardware moves. What lasts is the math, and the habit of costing a connection against memory instead of counting it as a handle. The same shape shows up on the serving side, where [a graphics card runs out of cache before it runs out of math](/kv-cache-is-the-concurrency-ceiling/). Budget the resource the work actually eats.

<!-- tldr -->

## At a glance

**The shift:** A connection is a process with a memory budget, so pool size times pod count sets the real ceiling.
**The number:** Twenty pods of a 100-connection pool arrive as 2,000 connections.
**The risk:** The pooling mode that makes sharing work breaks session state an app may depend on.

## Sources
[1] PostgreSQL Global Development Group, "Connections and Authentication" (PostgreSQL 18 documentation) — https://www.postgresql.org/docs/current/runtime-config-connection.html
[2] PostgreSQL Global Development Group, "Resource Consumption" (PostgreSQL 18 documentation) — https://www.postgresql.org/docs/current/runtime-config-resource.html
[3] Google Cloud, "Cloud SQL for PostgreSQL quotas" — https://cloud.google.com/sql/docs/postgres/quotas
[4] Google Cloud, "Managed Connection Pooling" — https://cloud.google.com/sql/docs/postgres/managed-connection-pooling
[5] PgBouncer, "Configuration" — https://www.pgbouncer.org/config.html
[6] PostgreSQL wiki, "Number Of Database Connections" — https://wiki.postgresql.org/wiki/Number_Of_Database_Connections

---
title: "Your Pool Becomes 2,000: A Memory Trap"
vertical: enterprise_tech_leadership
kind: evergreen
persona: eng_leader
one_big_thing: "A database connection is a server process holding a per-sort memory budget, so the real ceiling is memory — connections times sorts in flight times work_mem — and because every pod opens its own pool, a pool default copied from a library multiplies by the pod count and can exhaust the database after the code ships."
date: 2026-11-03
slug: your-pool-becomes-2000-connections
archetype: evergreen
evergreen: true
image_path: "context/assets/illustrations/your-pool-becomes-2000-connections/featured.jpg"
image_style: "cinematic_still"
image_model: "flux"
image_alt: "Pool Defaults Multiply By Pods. Overloaded patch panel spilling copper cables onto a concrete floor in a server room"
image_caption: "Pool Defaults Multiply By Pods: One pool per pod turns a setting into a memory drain."
image_credit: "Illustration: Editorial-Factory Intelligence Unit"
---

<!-- lead -->
Your framework's pool setting becomes 2,000 database connections, because every copy of the app opens its own pool and the server takes about 100 by default [1]. The pool lives inside each process, so every pod — a scheduled copy of the app — gets one. A one-pod test never shows the total, because the autoscaler sets the pod count later. The first sign is a database that refuses new logins, or a report whose sort writes to disk, on deploy night. The number that fails sits in a framework config file, where nobody priced it against memory.

<!-- tension -->

## Memory sets the ceiling

Each client connection gets its own backend process, and the connection limit sets how many of those the server will start. The setting that spends memory is `work_mem`, the room for one sort or one hash table in one query; it defaults to four megabytes [2]. One query can hold several of those rooms open at once, and many sessions can sort at the same time [2]. So the total can run many times the figure for a single session.

A managed platform will let a team push that math into absurd territory. Google's managed database service lets the connection limit plus two worker settings reach 262,142, far past what its memory tiers can hold [3]. One default-sized sort per slot would ask for around a terabyte of memory, while the servers on that tier carry memory in tens of gigabytes. The dial counts slots, not bytes, and the docs present it as a limit to raise rather than a number to reason from [3]. Slots are cheap. Sorts are not.

What I keep circling is how quiet the second failure is. Running out of memory kills a backend and drops the connection, which at least makes noise. The earlier sign is the spill: once sorts stop fitting, every query that orders or joins writes to disk. Latency climbs while the dashboard shows a healthy database with spare connections. These defaults come from the PostgreSQL 18 docs, read on 3 November 2026, and they have held for years because the math behind them does not move [1][2].

## By the numbers

- **50 — Server connections per pooler:** A managed pooler (connection broker) runs once per four cores, and each opens up to 50 server connections for one database and user pair, so an eight-core box gets two [4].
- **100 — A pooler's own default:** PgBouncer, a popular open-source pooler, ships a pool of 100 server connections per user and database pair, and holds one until the client leaves unless the mode is changed [5].
- **262,142 — The config ceiling:** The connection limit plus the autovacuum setting plus the worker setting cannot pass that total on Google's service [3].

<!-- tactical-insight -->

## Where the pool bites

- **Per-pod budget:** Teams that dodge this treat pool size as a per-pod budget and write it down. Pool size times the highest pod count a deploy can reach must fit inside the server's connection room. That room, divided by how many sorts one query can hold and multiplied by the memory each sort gets, must fit whatever memory is left after the shared cache. What I look for is a framework default that walks into a deploy chart untouched, because that is how a laptop value becomes a hard cap.
- **Mode choice:** A pooler is the usual answer, and its mode turns the choice into a correctness question. In session mode one server connection is held until the client leaves, which is the documented default [5]. In transaction mode the connection goes back at commit, which lets thousands of clients share a few dozen server connections. It also breaks anything that outlives a transaction: prepared statements, session settings, locks, and listeners.
- **Sizing anchor:** Sizing comes from the same source, not from a vendor tier. The project's long-standing guide keeps active connections near twice the core count plus the number of disks [6]. Teams that follow it tend to raise the room per sort for reporting sessions only, and leave the live path at the shipped value.

<!-- nuanced-takeaway -->

## The catch

A smaller pool has a cost the throughput rule hides. Fewer server connections means requests wait, and that rule is about work done per second, not the slowest requests on a busy day [6]. A pool sized for throughput can still miss a tail target on a busy day. Queues are not free. Transaction mode buys sharing at the price of session state, and an app that leaned on a prepared statement or a temporary setting will fail in a way that looks random.

Lowering the room per sort is not a cap either. It limits each sort, not the total, so a fleet of wide queries spends the same memory overall and writes more work to disk. That trade can be right, and it is still a trade: the disk is slower, and input and output become the new ceiling.

My read, held loosely: the defaults are the least durable part of this piece, since vendors re-tune them and hardware moves. What lasts is the math, and the habit of costing a connection against memory instead of counting it as a handle. The same shape shows up on the serving side, where [a graphics card runs out of cache before it runs out of math](/kv-cache-is-the-concurrency-ceiling/). The real decision is to budget the resource the work actually eats before a framework default makes that call.

<!-- tldr -->

## At a glance

- **The shift:** A connection is a process with a memory budget; pool size times pod count sets the ceiling.
- **The number:** 2,000 connections from one copied pool setting [1].
- **The risk:** The pooling mode that makes sharing work breaks session state an app may depend on.

## Sources

[1] PostgreSQL Global Development Group, "Connections and Authentication" (PostgreSQL 18 documentation) — https://www.postgresql.org/docs/current/runtime-config-connection.html
[2] PostgreSQL Global Development Group, "Resource Consumption" (PostgreSQL 18 documentation) — https://www.postgresql.org/docs/current/runtime-config-resource.html
[3] Google Cloud, "Cloud SQL for PostgreSQL quotas" — https://cloud.google.com/sql/docs/postgres/quotas
[4] Google Cloud, "Managed Connection Pooling" — https://cloud.google.com/sql/docs/postgres/managed-connection-pooling
[5] PgBouncer, "Configuration" — https://www.pgbouncer.org/config.html
[6] PostgreSQL wiki, "Number Of Database Connections" — https://wiki.postgresql.org/wiki/Number_Of_Database_Connections

# Verified Brief: enterprise_tech_leadership — 2026-11-03 (evergreen)

**Archetype:** evergreen · **Vertical:** enterprise_tech_leadership · **Persona:** eng_leader
**Brief of record:** `context/recon_proposals/2026-11-03_enterprise_tech_leadership_evergreen_brief.md` (evergreen gate PASS, 5 rows verified on 3 hosts)

| # | Claim | Status | Source URL | Verbatim |
|---|-------|--------|-----------|----------|
| 1 | PostgreSQL's `max_connections` defaults to about 100 concurrent connections | VERIFIED | https://www.postgresql.org/docs/current/runtime-config-connection.html | "Determines the maximum number of concurrent connections to the database server. The default is typically 100 connections, but might be less if your kernel settings will not support it (as determined during initdb)." |
| 2 | `work_mem` defaults to 4MB **per sort or hash operation**, and one query can run several at once | VERIFIED | https://www.postgresql.org/docs/current/runtime-config-resource.html | "Sets the base maximum amount of memory to be used by a query operation (such as a sort or hash table) before writing to temporary disk files… The default value is four megabytes (4MB). Note that a complex query might perform several sort and hash operations at the same time, with each operation generally being allowed to use as much memory as this value specifies… Also, several running sessions could be doing such operations concurrently. Therefore, the total memory used could be many times the value of work_mem." |
| 3 | Cloud SQL allows a configured backend-connection ceiling far above any memory budget | VERIFIED | https://cloud.google.com/sql/docs/postgres/quotas | "This calculation is the sum of the values for max_connections (maximum number of client connections), autovacuum_max_workers (maximum number of autovacuum processes), and max_worker_processes. The sum cannot exceed 262142." |
| 4 | A managed pooler is provisioned per 4 vCPUs and holds a documented number of server connections per database/user pair | VERIFIED | https://cloud.google.com/sql/docs/postgres/managed-connection-pooling | "one connection pooler for every 4 vCPUs, with a minimum of 1 connection pooler… For example, if max_pool_size is set to 50 on an instance running 2 connection poolers (8 vCPUs), then each connection pooler can open up to 50 server connections for a specific database and user pair, allowing a total of up to 100 server connections across the instance for that pool." |
| 5 | PgBouncer's documented pool size is 100 server connections per user/database pair, and its default mode is session | VERIFIED | https://www.pgbouncer.org/config.html | "default_pool_size — The maximum number of server connections to allow per user/database pair." / "pool_mode — … session: Server is released back to pool after client disconnects. Default." |
| 6 | The throughput-optimal active-connection count is near `(core_count * 2) + effective_spindle_count`, and internal structures scale at O(N^2) with `max_connections` | VERIFIED (prose citation only — its figure could not carry a gate row because the token `2` first matches the page's own contents list) | https://wiki.postgresql.org/wiki/Number_Of_Database_Connections | "for optimal throughput the number of active connections should be somewhere near (( core_count * 2) + effective_spindle_count )… Some internal structures allocated based on max_connections scale at O(N^2) or O(N*log(N))." |

## Derived arithmetic (mine — recompute, never quote as a source's)

- **2,000 connections:** 20 application replicas × a 100-connection pool = 2,000 client connections against a server whose documented default is 100.
- **About a terabyte:** 262,142 connections × one 4MB sort each = 1,048,568 megabytes ≈ 1 TB, i.e. the configuration ceiling is roughly a thousand times the sort memory any single instance carries.
- **100:1 pooling ratio:** 50 server connections behind the pooler default of 5,000 client connections per pooler (Cloud SQL `max_client_connections` default, quoted in row 4's page).
- **Rule for the article:** per-replica pool × maximum replicas ≤ server connection budget, and that budget ÷ (operations per query) × 4MB must fit inside the memory the instance has after `shared_buffers`.

## Do not repeat

- Do not restate the vendor rate cards or treat 262,142 as advice — it is a configuration ceiling.
- Do not call the 2× cores rule a latency rule: the wiki measures throughput.

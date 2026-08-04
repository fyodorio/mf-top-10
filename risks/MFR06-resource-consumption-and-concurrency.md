# MFR06: Unrestricted Resource Consumption and Concurrency Failures

## Factors

- **Exploitability:** Easy
- **Prevalence:** Widespread
- **Detectability:** Average
- **Technical impact:** Severe

## Description

An attacker can consume disproportionate compute, memory, storage, connections, bandwidth, serverless duration, or paid third-party operations; or can exploit a race between requests to violate business rules. A per-route rate limit alone is rarely enough for a full-stack application: server actions, loaders, upload/image processing, streaming, cache revalidation, webhook calls, and background work often have separate cost profiles and identities.

## Metaframework-specific failure modes

- Public server functions/actions with no body-size, duration, concurrency, or per-principal limits.
- Expensive rendering, image optimization, regular expressions, pagination, recursive data fetching, or decompression driven by request input.
- A limit applied to page routes but not data routes, loaders, actions, or direct endpoint calls.
- Concurrent state changes that oversell stock, redeem a code twice, bypass quotas, or share cache/revalidation state incorrectly.
- User-controlled calls to paid services such as AI, email, SMS, geocoding, storage, or external APIs without budget controls.
- Expensive decoding, parsing, hashing, or signature computation performed on the request before cheap invariants such as size, nesting depth, or element count are checked, so an eventual rejection still costs the server its work.
- Request-supplied counts, ranges, or iteration bounds expanded during server rendering, allowing a very small request to allocate a very large amount of memory.
- A buffer allocated from a client-declared length before the corresponding bytes have arrived, so a small request plus a stalled connection reserves memory it never fills.
- A framework or plugin parsing an unbounded request header on every render — user agent, accept, forwarded — with a backtracking regular expression, on a single-threaded event loop.
- A configured limit enforced by a layer other than the one that reads the body, so the adapter, runtime, or edge bypasses it.
- A newly introduced request encoding, streaming format, or server-function transport shipped without the size, depth, and element-count limits already applied to established ones.

## Prevention and verification priorities

1. Apply layered limits: request size, parsed/decompressed size, time, memory, concurrency, queue depth, output size, and per-identity/IP operation quotas.
2. Enforce limits at the edge and again around expensive server operations; give server functions/actions the same protection as explicit APIs.
3. Bound pagination, uploads, image dimensions, regular-expression work, batch sizes, fan-out, iteration counts derived from request input, and third-party spending.
4. Order validation so rejection is cheap: check size, depth, and element count before decoding, parsing, hashing, or verifying a payload.
5. Make state transitions atomic or idempotent; use transactions, optimistic concurrency, unique constraints, and idempotency keys where appropriate.
6. Load-test normal and alternate transports, concurrent requests, slow clients, malformed bodies, and compressed inputs. Alert on saturation and cost anomalies.

## Relevant CWEs

- [CWE-400: Uncontrolled Resource Consumption](https://cwe.mitre.org/data/definitions/400.html)
- [CWE-409: Improper Handling of Highly Compressed Data](https://cwe.mitre.org/data/definitions/409.html)
- [CWE-770: Allocation of Resources Without Limits or Throttling](https://cwe.mitre.org/data/definitions/770.html)
- [CWE-799: Improper Control of Interaction Frequency](https://cwe.mitre.org/data/definitions/799.html)
- [CWE-362: Race Condition](https://cwe.mitre.org/data/definitions/362.html)
- [CWE-407: Inefficient Algorithmic Complexity](https://cwe.mitre.org/data/definitions/407.html)
- [CWE-789: Memory Allocation with Excessive Size Value](https://cwe.mitre.org/data/definitions/789.html)
- [CWE-1284: Improper Validation of Specified Quantity in Input](https://cwe.mitre.org/data/definitions/1284.html)

## Representative evidence

- [CVE-2024-56332](https://github.com/advisories/GHSA-7m27-7ghc-44w9): crafted Next.js Server Action requests could leave connections open until hosting timeouts.
- [CVE-2025-32421](https://github.com/advisories/GHSA-qpjv-v59x-3qc4): a Next.js Pages Router race condition affected response/cache behavior under specific conditions.
- [CVE-2025-59472](https://github.com/advisories/GHSA-5f7q-jpqc-wp7h): affected Next.js partial-prerendering resume endpoints allowed unbounded memory consumption and decompression amplification.
- [CVE-2026-44579](https://github.com/advisories/GHSA-mg66-mrh9-m8jx): Cache Components could permit connection exhaustion through crafted requests.
- [GHSA-hxcr-hm88-mpq6](https://github.com/nuxt/nuxt/security/advisories/GHSA-hxcr-hm88-mpq6): an unvalidated iteration count in a Nuxt island `v-for` let a request of roughly 130 bytes exhaust memory and crash the rendering worker.
- [GHSA-9pgf-384g-p7mv](https://github.com/nuxt/nuxt/security/advisories/GHSA-9pgf-384g-p7mv): the Nuxt island endpoint decoded and hashed an unauthenticated request body before validating the hash in the URL, so an oversized payload consumed CPU on the single-threaded event loop before being rejected.
- [CVE-2026-64644](https://github.com/advisories/GHSA-q8wf-6r8g-63ch): where remote images were permitted, the Next.js Image Optimization API could be driven to CPU exhaustion on `/_next/image` by malicious image content.
- SvelteKit’s remote-function deserializer produced five advisories in six months — [CVE-2026-22803](https://github.com/advisories/GHSA-j2f3-wq62-6q46), [GHSA-88qp-p4qg-rqm6](https://github.com/advisories/GHSA-88qp-p4qg-rqm6), [GHSA-vrhm-gvg7-fpcf](https://github.com/advisories/GHSA-vrhm-gvg7-fpcf), [GHSA-fpg4-jhqr-589c](https://github.com/advisories/GHSA-fpg4-jhqr-589c), and [GHSA-wqjv-9729-c5q2](https://github.com/advisories/GHSA-wqjv-9729-c5q2) — covering memory amplification, CPU exhaustion, deserialization expansion, and process crashes. In the first, a small request declares a large body length and then stalls the connection, and the buffer is allocated eagerly to accommodate data that never arrives. A newly introduced request-body format is a new resource-limit surface, and one advisory against it is unlikely to be the last.
- [CVE-2026-29772](https://github.com/advisories/GHSA-3rmj-9m5h-8fpv) and [CVE-2026-27729](https://github.com/advisories/GHSA-jm64-8m5q-4qh8): affected Astro releases applied no request-body size limit to Server Islands or to Server Actions. Two transports, one missing limit — evidence that a limit must be enumerated per transport rather than assumed to be global.
- [CVE-2026-40073](https://github.com/advisories/GHSA-2crg-3p73-43xp): `BODY_SIZE_LIMIT` could be bypassed in `@sveltejs/adapter-node`, so a limit that was configured was not the limit enforced.
- [GHSA-68jq-fhch-4xq4](https://github.com/quasarframework/quasar/security/advisories/GHSA-68jq-fhch-4xq4): Quasar auto-installs its `Platform` plugin on every server-side render, feeding the raw, unbounded `User-Agent` header into backtracking regular expressions whose cost is cubic in header length. The advisory measures an 8 KB header blocking the event loop for about 4.4 seconds and a 16 KB header for about 35 — a single unauthenticated request, against a plugin the application did not opt into.
- [CVE-2026-32701](https://github.com/advisories/GHSA-whhv-gg5v-864r): Qwik City’s FormData processing permitted array-method pollution, producing type confusion and denial of service.
- [CVE-2026-34077](https://github.com/advisories/GHSA-rxv8-25v2-qmq8): React Router single-fetch responses reflected user input in a way that enabled denial of service.

## Sources

- [OWASP API4:2023 Unrestricted Resource Consumption](https://owasp.org/API-Security/editions/2023/en/0xa4-unrestricted-resource-consumption/)
- [OWASP API6:2023 Unrestricted Access to Sensitive Business Flows](https://owasp.org/API-Security/editions/2023/en/0xa6-unrestricted-access-to-sensitive-business-flows/)
- [Research references](../references.md#resource-control-and-concurrency)

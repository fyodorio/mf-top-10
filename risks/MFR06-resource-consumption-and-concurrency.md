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

## Sources

- [OWASP API4:2023 Unrestricted Resource Consumption](https://owasp.org/API-Security/editions/2023/en/0xa4-unrestricted-resource-consumption/)
- [OWASP API6:2023 Unrestricted Access to Sensitive Business Flows](https://owasp.org/API-Security/editions/2023/en/0xa6-unrestricted-access-to-sensitive-business-flows/)
- [Research references](../references.md#resource-control-and-concurrency)

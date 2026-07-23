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

## Prevention and verification priorities

1. Apply layered limits: request size, parsed/decompressed size, time, memory, concurrency, queue depth, output size, and per-identity/IP operation quotas.
2. Enforce limits at the edge and again around expensive server operations; give server functions/actions the same protection as explicit APIs.
3. Bound pagination, uploads, image dimensions, regular-expression work, batch sizes, fan-out, and third-party spending.
4. Make state transitions atomic or idempotent; use transactions, optimistic concurrency, unique constraints, and idempotency keys where appropriate.
5. Load-test normal and alternate transports, concurrent requests, slow clients, malformed bodies, and compressed inputs. Alert on saturation and cost anomalies.

## Relevant CWEs

- [CWE-400: Uncontrolled Resource Consumption](https://cwe.mitre.org/data/definitions/400.html)
- [CWE-409: Improper Handling of Highly Compressed Data](https://cwe.mitre.org/data/definitions/409.html)
- [CWE-770: Allocation of Resources Without Limits or Throttling](https://cwe.mitre.org/data/definitions/770.html)
- [CWE-799: Improper Control of Interaction Frequency](https://cwe.mitre.org/data/definitions/799.html)
- [CWE-362: Race Condition](https://cwe.mitre.org/data/definitions/362.html)

## Representative evidence

- [CVE-2024-56332](https://github.com/advisories/GHSA-7m27-7ghc-44w9): crafted Next.js Server Action requests could leave connections open until hosting timeouts.
- [CVE-2025-32421](https://github.com/advisories/GHSA-qpjv-v59x-3qc4): a Next.js Pages Router race condition affected response/cache behavior under specific conditions.
- [CVE-2025-59472](https://github.com/advisories/GHSA-5f7q-jpqc-wp7h): affected Next.js partial-prerendering resume endpoints allowed unbounded memory consumption and decompression amplification.
- [CVE-2026-44579](https://github.com/advisories/GHSA-mg66-mrh9-m8jx): Cache Components could permit connection exhaustion through crafted requests.

## Sources

- [OWASP API4:2023 Unrestricted Resource Consumption](https://owasp.org/API-Security/editions/2023/en/0xa4-unrestricted-resource-consumption/)
- [OWASP API6:2023 Unrestricted Access to Sensitive Business Flows](https://owasp.org/API-Security/editions/2023/en/0xa6-unrestricted-access-to-sensitive-business-flows/)
- [Research references](../references.md#resource-control-and-concurrency)

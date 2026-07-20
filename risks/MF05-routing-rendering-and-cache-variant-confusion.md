# MF05: Routing, Rendering, and Cache Variant Confusion

## Factors

- **Exploitability:** Average
- **Prevalence:** Common
- **Detectability:** Difficult
- **Technical impact:** Severe

## Description

Two layers disagree about what a request means, which response variant it represents, or whether it is safe to cache. The layers may include a browser, CDN, reverse proxy, edge runtime, framework router, middleware, server renderer, data endpoint, and component transport. A request intended for data, RSC/Flight, an island, a prefetch, a redirect, or a static generation flow can then be interpreted as an ordinary page request—or vice versa.

The result can be authorization bypass, content confusion, cache poisoning, stored XSS, incorrect redirects, private-data disclosure, or denial of service. This is distinct from an application’s ordinary authorization bug: the intended rule may exist, but an alternate transport or cache variant bypasses it.

## Metaframework-specific failure modes

- CDN cache keys omit query strings, request headers, cookies, locale, RSC/data flags, or rendering mode.
- Framework-internal headers or parameters are accepted from external clients.
- Middleware matchers protect a canonical page URL but not data, prefetch, locale, island, or component-transport variants.
- A response changes by request header but `Vary`, cache-control, and CDN behavior do not partition it.
- Pages intended for one rendering mode are coerced into another by request metadata, or cache revalidation shares state incorrectly.

## Prevention and verification priorities

1. Enumerate every public request variant per route: HTML, JSON/data, RSC/Flight, islands, prefetch, redirect, static, locale, error, and action/function transports.
2. Ensure proxies strip or normalize framework-internal headers from untrusted clients. Upgrade promptly when a framework fixes request classification.
3. Align shared-cache keys with every request attribute that changes a response; disable shared caching when safe partitioning cannot be proved.
4. Verify `Vary`, cache-control, redirect caching, and cache-buster behavior on the deployed CDN—not only in local development.
5. Test with concurrent requests and production-like intermediaries; inspect both the origin response and the response actually served from cache.

## Relevant CWEs

- [CWE-436: Interpretation Conflict](https://cwe.mitre.org/data/definitions/436.html)
- [CWE-444: Inconsistent Interpretation of HTTP Requests](https://cwe.mitre.org/data/definitions/444.html)
- [CWE-349: Acceptance of Extraneous Untrusted Data With Trusted Data](https://cwe.mitre.org/data/definitions/349.html)
- [CWE-525: Use of Web Browser Cache Containing Sensitive Information](https://cwe.mitre.org/data/definitions/525.html)
- [CWE-362: Concurrent Execution using Shared Resource with Improper Synchronization](https://cwe.mitre.org/data/definitions/362.html)

## Representative evidence

- [CVE-2024-46982](https://github.com/advisories/GHSA-gp8f-8m3g-qvj9): Next.js cache-poisoning research demonstrated rendering-mode confusion and its cache impact.
- [CVE-2025-27415](https://github.com/advisories/GHSA-jvhm-gjrh-3h93): Nuxt payload rendering could be forced and cached as a normal page in affected deployments.
- [CVE-2025-43864](https://github.com/advisories/GHSA-f46r-rw29-r322): a React Router header could force SPA mode and enable cache-poisoning denial of service.
- [CVE-2026-44576](https://github.com/advisories/GHSA-wfc6-r584-vfw7): Next.js RSC responses could poison shared cache entries that did not correctly partition variants.

## Sources

- [zhero: Next.js, cache, and chains](https://zhero-web-sec.github.io/research-and-things/nextjs-cache-and-chains-the-stale-elixir)
- [zhero: Nuxt payload cache poisoning](https://zhero-web-sec.github.io/research-and-things/nuxt-show-me-your-payload)
- [Research references](../references.md#routing-rendering-and-caching)

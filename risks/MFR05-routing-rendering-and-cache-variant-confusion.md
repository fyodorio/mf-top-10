# MFR05: Routing, Rendering, and Cache Variant Confusion

## Factors

- **Exploitability:** Average
- **Prevalence:** Common
- **Detectability:** Difficult
- **Technical impact:** Severe

## Description

Two layers disagree about what a request means, which response variant it represents, or whether it is safe to cache. The layers may include a browser, CDN, reverse proxy, edge runtime, framework router, middleware, server renderer, data endpoint, and component transport. A request intended for data, RSC/Flight, an island, a prefetch, a redirect, or a static generation flow can then be interpreted as an ordinary page request — or vice versa.

The result can be authorization bypass, content confusion, cache poisoning, stored XSS, incorrect redirects, private-data disclosure, or denial of service. This is distinct from an application’s ordinary authorization bug: the intended rule may exist, but an alternate transport or cache variant bypasses it.

## Metaframework-specific failure modes

- CDN cache keys omit query strings, request headers, cookies, locale, RSC/data flags, or rendering mode.
- Framework-internal headers or parameters are accepted from external clients.
- Middleware matchers protect a canonical page URL but not data, prefetch, locale, island, or component-transport variants.
- A response changes by request header but `Vary`, cache-control, and CDN behavior do not partition it.
- Pages intended for one rendering mode are coerced into another by request metadata, or cache revalidation shares state incorrectly.
- A framework-internal data, payload, or `fetch` cache keys on the URL alone, ignoring the request body, method, headers, cookies, or authorization state, or deriving the key through a lossy encoding that lets distinct inputs collide.
- A conditional-request or content-negotiation header the application never reads still changes what the origin returns or whether the response is cacheable.
- Cacheability is decided by the deployment adapter rather than the framework router, so the same application code behaves differently per platform and only the deployed combination can be tested.

## Prevention and verification priorities

1. Enumerate every public request variant per route: HTML, JSON/data, RSC/Flight, islands, prefetch, redirect, static, locale, error, and action/function transports.
2. Ensure proxies strip or normalize framework-internal headers from untrusted clients. Upgrade promptly when a framework fixes request classification.
3. Align cache keys with every request attribute that changes a response — including cookies, authorization state, and request bodies — at the CDN, the proxy, and the framework’s own data and payload caches; disable shared caching when safe partitioning cannot be proved.
4. Verify `Vary`, cache-control, redirect caching, and cache-buster behavior on the deployed CDN — not only in local development.
5. Test with concurrent requests and production-like intermediaries; inspect both the origin response and the response actually served from cache.
6. Treat a code fix as incomplete remediation: purge affected CDN, edge, and framework cache entries after patching, because poisoned or cross-user entries survive the upgrade.

## Relevant CWEs

- [CWE-436: Interpretation Conflict](https://cwe.mitre.org/data/definitions/436.html)
- [CWE-444: Inconsistent Interpretation of HTTP Requests](https://cwe.mitre.org/data/definitions/444.html)
- [CWE-349: Acceptance of Extraneous Untrusted Data With Trusted Data](https://cwe.mitre.org/data/definitions/349.html)
- [CWE-524: Use of Cache Containing Sensitive Information](https://cwe.mitre.org/data/definitions/524.html)
- [CWE-525: Use of Web Browser Cache Containing Sensitive Information](https://cwe.mitre.org/data/definitions/525.html)
- [CWE-362: Concurrent Execution using Shared Resource with Improper Synchronization](https://cwe.mitre.org/data/definitions/362.html)

## Representative evidence

- [CVE-2024-46982](https://github.com/advisories/GHSA-gp8f-8m3g-qvj9): Next.js cache-poisoning research demonstrated rendering-mode confusion and its cache impact.
- [CVE-2025-27415](https://github.com/advisories/GHSA-jvhm-gjrh-3h93): Nuxt payload rendering could be forced and cached as a normal page in affected deployments.
- [CVE-2025-43864](https://github.com/advisories/GHSA-f46r-rw29-r322): a React Router header could force SPA mode and enable cache-poisoning denial of service.
- [CVE-2026-44576](https://github.com/advisories/GHSA-wfc6-r584-vfw7): Next.js RSC responses could poison shared cache entries that did not correctly partition variants.
- [CVE-2026-71316](https://github.com/advisories/GHSA-wm8w-6qjm-cv43): affected Nuxt releases stored the `_payload.json` of a cached route under a path-only key with no cookie, authorization, or `cache.varies` dimension, so one authenticated user’s server-rendered data was served to other users and to unauthenticated clients. The advisory also requires purging CDN and edge caches after upgrading.
- [CVE-2026-64648](https://github.com/advisories/GHSA-68g3-v927-f742) and [CVE-2026-64647](https://github.com/advisories/GHSA-4633-3j49-mh5q): a server-side `fetch` in affected Next.js releases could return a cached response body belonging to a different request to the same URL, because the cache key ignored the request body, or derived it through an encoding in which distinct byte sequences collided.
- [CVE-2026-41322](https://github.com/advisories/GHSA-c57f-mm3j-27q9): a malformed `if-match` header was handled incorrectly in affected Astro releases, producing a cacheable response for a request the origin should have rejected. A conditional-request header is part of the cache key surface even when the application never reads it.
- [CVE-2026-27118](https://github.com/advisories/GHSA-9pq4-5hcf-288c): cache poisoning in `@sveltejs/adapter-vercel`, where the deployment adapter rather than the framework router determined what was cacheable — so the same application code carries different cache behavior per adapter.
- [CVE-2025-43865](https://github.com/advisories/GHSA-cpj6-fhp6-mr6j) and [CVE-2025-31137](https://github.com/advisories/GHSA-4q56-crqp-v477): React Router pre-render data spoofing, and URL manipulation through `Host` and `X-Forwarded-Host`, both reached through request metadata that the router treated as trustworthy.
- [CVE-2026-44457](https://github.com/advisories/GHSA-p77w-8qqv-26rm): a cache middleware ignored `Vary: Authorization` and `Vary: Cookie`, serving one user’s response to another. Cited because Astro’s composable pipeline can place Hono in a metaframework request path; see the [scope note](../references.md#scope-note-on-frameworks-cited).

## Sources

- [zhero: Next.js, cache, and chains](https://zhero-web-sec.github.io/research-and-things/nextjs-cache-and-chains-the-stale-elixir)
- [zhero: Nuxt payload cache poisoning](https://zhero-web-sec.github.io/research-and-things/nuxt-show-me-your-payload)
- [Research references](../references.md#routing-rendering-and-caching)

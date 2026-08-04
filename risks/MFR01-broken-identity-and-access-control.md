# MFR01: Broken Identity and Access Control Across Routes, Server Functions, and Data APIs

## Factors

- **Exploitability:** Easy
- **Prevalence:** Widespread
- **Detectability:** Average
- **Technical impact:** Severe

## Description

An application fails to prove the caller’s identity, establish the correct authority, or enforce that authority at the operation, object, and property level. In a metaframework, server functions/actions, route handlers, loaders, endpoints, RPC-like calls, page data functions, and server islands are all server-side entry points — even when the UI does not visibly link to them.

Middleware and route guards are useful for optimistic redirects, coarse filtering, and rate limiting. They are not a sufficient authorization boundary. Every sensitive data access and state-changing operation must authorize the current principal in the server-side function that performs it.

## Metaframework-specific failure modes

- Treating a server action/function as private because it is imported only by a component.
- Authorizing a page route in middleware but not its loader, data endpoint, RSC/Flight request, island, action, or alternate rendering route.
- Checking authentication but not object ownership, tenant scope, role, or property-level permissions.
- Binding untrusted request input directly to persistence objects, allowing privileged properties to be set.
- Relying on client-side route guards, hidden buttons, unlinked endpoints, or obscured URLs as authorization.
- Declaring an authorization rule in a matcher that normalizes paths differently from the router — case, trailing slash, encoding, or locale prefix — so the rule silently never matches the request it was written for.
- Assuming a rule verified under one build pipeline behaves identically under another bundler, adapter, or runtime target.
- Writing an authorization rule against a decoded path while the router decodes a different number of times, so an encoded or doubly encoded path reaches the handler without matching the rule.
- Accepting a path, route, or handler override from a request header that the deployment adapter reads but the application never declared.
- Reconstructing a call target from a request payload — a server-function reference, module path, symbol, or component name — so the reachable set of operations is defined by the deserializer rather than by the routes the application exposed.

## Prevention and verification priorities

1. Make the server-side data/service layer the policy enforcement point; deny by default.
2. Authenticate and authorize every server function/action, route handler, loader, API endpoint, and data mutation independently.
3. Enforce object, tenant, function, and property-level authorization; use explicit request/response schemas and field allowlists.
4. Treat middleware as defense in depth. Exercise alternate routes, framework data requests, locale routes, prefetched segments, case- and encoding-variant paths, and direct requests in authorization tests.
5. Resolve the request to a canonical path once, before any authorization decision, and authorize against the resolved resource rather than a path string. Do not accept path, route, or rendering overrides from request headers unless a trusted proxy sets them.
6. Treat a server-function wire format as an untrusted parsing boundary: resolve the invocation target from a server-side allowlist keyed to the declared function, never from a value reconstructed out of the request.
7. Test as unauthenticated, low-privilege, cross-tenant, and cross-object actors. Include negative tests for every sensitive operation.

## Relevant CWEs

- [CWE-284: Improper Access Control](https://cwe.mitre.org/data/definitions/284.html)
- [CWE-285: Improper Authorization](https://cwe.mitre.org/data/definitions/285.html)
- [CWE-639: Authorization Bypass Through User-Controlled Key](https://cwe.mitre.org/data/definitions/639.html)
- [CWE-862: Missing Authorization](https://cwe.mitre.org/data/definitions/862.html)
- [CWE-863: Incorrect Authorization](https://cwe.mitre.org/data/definitions/863.html)
- [CWE-178: Improper Handling of Case Sensitivity](https://cwe.mitre.org/data/definitions/178.html)
- [CWE-915: Improperly Controlled Modification of Dynamically-Determined Object Attributes](https://cwe.mitre.org/data/definitions/915.html)

## Representative evidence

- [CVE-2025-29927](https://github.com/advisories/GHSA-f82v-jwr5-mffw): Next.js middleware authorization bypass through a client-controlled internal header.
- [CVE-2026-44575](https://github.com/advisories/GHSA-267c-6grr-h53f): App Router segment-prefetch variants bypassed middleware/proxy authorization in affected Next.js releases.
- [CVE-2026-44573](https://github.com/advisories/GHSA-36qx-fr4f-26g5): locale-less Pages Router data routes bypassed middleware authorization in affected Next.js applications.
- [CVE-2026-46342](https://github.com/advisories/GHSA-g8wj-3cr3-6w7v): Nuxt island routes require authorization in the island data layer because page middleware does not apply to island rendering.
- [CVE-2026-53721](https://github.com/advisories/GHSA-mm7m-92g8-7m47) and [GHSA-hxvh-4h3w-prp9](https://github.com/nuxt/nuxt/security/advisories/GHSA-hxvh-4h3w-prp9): a case-sensitivity mismatch between the Nuxt router and the `routeRules` matcher silently dropped `appMiddleware` authorization gates for mixed-case rule keys. The second advisory is an incomplete-fix follow-up to the first, so the rule remained unenforced after the initial patch.
- [CVE-2026-64642](https://github.com/advisories/GHSA-6gpp-xcg3-4w24): Next.js App Router applications built with Turbopack and a single configured locale bypassed middleware/proxy checks, showing that the build pipeline can change whether an authorization rule runs at all.
- [CVE-2025-64765](https://github.com/advisories/GHSA-ggxq-hp9w-j794), [CVE-2025-66202](https://github.com/advisories/GHSA-whqg-ppgf-wp8c), and [CVE-2026-59731](https://github.com/advisories/GHSA-vj59-8hwv-xxmv): Astro middleware authorization decisions based on `url.pathname` were bypassed first by URL-encoded path segments, then — after that fix — by double encoding, and then through a decode-iteration limit interacting with a rewrite path-canonicalization mismatch. Three advisories over roughly eight months against one pattern: comparing a decoded path string to a rule instead of authorizing in the handler that serves the resource.
- [CVE-2026-33768](https://github.com/advisories/GHSA-mr6q-rp88-fx84): an `x-astro-path` request header accepted by the `@astrojs/vercel` ISR function let an unauthenticated client override the path being served. The application did not define the header; the deployment adapter did.
- [CVE-2026-27971](https://github.com/advisories/GHSA-p9x5-jp3h-96mm): Qwik reconstructed attacker-controlled QRL objects from an `application/qwik-json` request body, resolving an arbitrary module path and symbol and reaching unauthenticated remote code execution in a single request. The authorization boundary was absent because the transport decided what to invoke.
- [GHSA-9m65-766c-r333](https://github.com/advisories/GHSA-9m65-766c-r333): a TanStack Start server function could be invoked through a sibling function’s client reference, so the reachable set of server operations exceeded the set the application deliberately exposed.
- [GHSA-8mv7-9c27-98vc](https://github.com/advisories/GHSA-8mv7-9c27-98vc): in Astro’s composable `astro/hono` pipeline, `security.checkOrigin` did not run when `middleware()` was absent or ordered incorrectly — a control silently inactive because of how two composed layers were assembled.

## Sources

- [OWASP API3:2023 Broken Object Property Level Authorization](https://owasp.org/API-Security/editions/2023/en/0xa3-broken-object-property-level-authorization/)
- [OWASP API5:2023 Broken Function Level Authorization](https://owasp.org/API-Security/editions/2023/en/0xa5-broken-function-level-authorization/)
- [Research references](../references.md#access-control-and-server-functions)

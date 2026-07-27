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

## Prevention and verification priorities

1. Make the server-side data/service layer the policy enforcement point; deny by default.
2. Authenticate and authorize every server function/action, route handler, loader, API endpoint, and data mutation independently.
3. Enforce object, tenant, function, and property-level authorization; use explicit request/response schemas and field allowlists.
4. Treat middleware as defense in depth. Exercise alternate routes, framework data requests, locale routes, prefetched segments, case- and encoding-variant paths, and direct requests in authorization tests.
5. Test as unauthenticated, low-privilege, cross-tenant, and cross-object actors. Include negative tests for every sensitive operation.

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

## Sources

- [OWASP API3:2023 Broken Object Property Level Authorization](https://owasp.org/API-Security/editions/2023/en/0xa3-broken-object-property-level-authorization/)
- [OWASP API5:2023 Broken Function Level Authorization](https://owasp.org/API-Security/editions/2023/en/0xa5-broken-function-level-authorization/)
- [Research references](../references.md#access-control-and-server-functions)

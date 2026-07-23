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

## Prevention and verification priorities

1. Make the server-side data/service layer the policy enforcement point; deny by default.
2. Authenticate and authorize every server function/action, route handler, loader, API endpoint, and data mutation independently.
3. Enforce object, tenant, function, and property-level authorization; use explicit request/response schemas and field allowlists.
4. Treat middleware as defense in depth. Exercise alternate routes, framework data requests, locale routes, prefetched segments, and direct requests in authorization tests.
5. Test as unauthenticated, low-privilege, cross-tenant, and cross-object actors. Include negative tests for every sensitive operation.

## Relevant CWEs

- [CWE-284: Improper Access Control](https://cwe.mitre.org/data/definitions/284.html)
- [CWE-285: Improper Authorization](https://cwe.mitre.org/data/definitions/285.html)
- [CWE-639: Authorization Bypass Through User-Controlled Key](https://cwe.mitre.org/data/definitions/639.html)
- [CWE-862: Missing Authorization](https://cwe.mitre.org/data/definitions/862.html)
- [CWE-863: Incorrect Authorization](https://cwe.mitre.org/data/definitions/863.html)
- [CWE-915: Improperly Controlled Modification of Dynamically-Determined Object Attributes](https://cwe.mitre.org/data/definitions/915.html)

## Representative evidence

- [CVE-2025-29927](https://github.com/advisories/GHSA-f82v-jwr5-mffw): Next.js middleware authorization bypass through a client-controlled internal header.
- [CVE-2026-44575](https://github.com/advisories/GHSA-267c-6grr-h53f): App Router segment-prefetch variants bypassed middleware/proxy authorization in affected Next.js releases.
- [CVE-2026-44573](https://github.com/advisories/GHSA-36qx-fr4f-26g5): locale-less Pages Router data routes bypassed middleware authorization in affected Next.js applications.
- [CVE-2026-46342](https://github.com/advisories/GHSA-g8wj-3cr3-6w7v): Nuxt island routes require authorization in the island data layer because page middleware does not apply to island rendering.

## Sources

- [OWASP API3:2023 Broken Object Property Level Authorization](https://owasp.org/API-Security/editions/2023/en/0xa3-broken-object-property-level-authorization/)
- [OWASP API5:2023 Broken Function Level Authorization](https://owasp.org/API-Security/editions/2023/en/0xa5-broken-function-level-authorization/)
- [Research references](../references.md#access-control-and-server-functions)

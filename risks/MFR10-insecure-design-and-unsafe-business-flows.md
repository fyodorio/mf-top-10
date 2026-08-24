# MFR10: Insecure Design and Unsafe Business Flows

## Factors

- **Exploitability:** Average
- **Prevalence:** Widespread
- **Detectability:** Difficult
- **Technical impact:** Severe

## Description

Required security controls were never designed for the application’s assets, trust boundaries, workflows, tenancy model, automation exposure, and failure states. A secure implementation cannot compensate for a missing decision about who may perform an action, what data may cross a boundary, how a costly operation is constrained, or which variants of a route are trusted.

This category captures business-logic and workflow abuse that does not fit a narrower technical root cause. It also gives the original “bulk AI development” concern the right home: AI-assisted coding, non-strict typing, rapid framework migration, copy-pasted middleware, and monolithic coupling are risk multipliers when they skip architecture review, test design, and ownership — not vulnerability classes by themselves.

## Metaframework-specific failure modes

- No threat model for a route’s HTML, data, RSC/Flight, island, prefetch, action, and cache variants.
- Business workflows allow automation, replay, race conditions, free-resource use, or role transitions without compensating controls.
- Tenant isolation, authorization, cache privacy, data serialization, and server egress are assumed rather than specified and tested.
- “Server-only” or “client-only” conventions exist in code but no enforceable capability boundary or review rule exists.
- Generated or AI-assisted code expands endpoint surface or duplicates patterns without preserving the original policy, tests, observability, and ownership.
- Adopting a server-function abstraction without deciding which operations are externally invocable, on the assumption that the framework’s transport constitutes the boundary.
- Selecting a framework on developer experience alone, without asking whether the security defaults its maturity implies — origin validation, resource limits, escaping of first-class APIs — are ones the application would otherwise have to supply.

## Prevention and verification priorities

1. Threat-model identity, data, rendering, routing, caching, egress, resource, and third-party boundaries before implementation and whenever framework architecture changes.
2. Write misuse cases for each critical flow: replay, concurrency, bulk automation, alternate route variants, cross-tenant access, and cost amplification.
3. Define server/client contracts, authorization policy, cache policy, resource budgets, and operational ownership as explicit requirements.
4. Use domain-specific types, schemas, tests, code review, and security design patterns to make the policy executable; TypeScript strictness is helpful but not a security boundary.
5. Require human review and test evidence for AI-generated or major refactored security-sensitive code, especially middleware, auth, serialization, actions, and deployment configuration.

## Relevant CWEs

- [CWE-657: Violation of Secure Design Principles](https://cwe.mitre.org/data/definitions/657.html)
- [CWE-840: Business Logic Errors](https://cwe.mitre.org/data/definitions/840.html)
- [CWE-841: Improper Enforcement of Behavioral Workflow](https://cwe.mitre.org/data/definitions/841.html)
- [CWE-602: Client-Side Enforcement of Server-Side Security](https://cwe.mitre.org/data/definitions/602.html)
- [CWE-799: Improper Control of Interaction Frequency](https://cwe.mitre.org/data/definitions/799.html)

## Representative evidence

- [CVE-2025-29927](https://github.com/advisories/GHSA-f82v-jwr5-mffw) shows the design risk of treating a routing middleware as the only authorization boundary.
- [CVE-2024-34351](https://github.com/advisories/GHSA-fr5h-rqp8-mj6g) shows why Server Actions need explicit origin, redirect, and egress design rather than implicit framework trust.
- [CVE-2025-67647](https://github.com/advisories/GHSA-j62c-4x62-9r35) demonstrates how prerendering, host validation, origin configuration, and caching can combine into an application-level attack path.
- [CVE-2026-64649](https://github.com/advisories/GHSA-89xv-2m56-2m9x), recurring in the same class as `CVE-2024-34351` roughly two years later, shows that a design which delegates origin and egress trust to framework defaults will keep producing findings as the runtime changes. The application needs its own stated policy for which hosts the server may be told to contact.
- Four framework families with independent implementations published advisories in which a request-borne payload was deserialized into an invocation target: [CVE-2026-27971](https://github.com/advisories/GHSA-p9x5-jp3h-96mm) (Qwik `server$`, unauthenticated remote code execution), [GHSA-9m65-766c-r333](https://github.com/advisories/GHSA-9m65-766c-r333) (TanStack Start, a sibling server function), [CVE-2026-71320](https://github.com/advisories/GHSA-9473-5f9j-94wq) (Nuxt server islands, a compiled `template` prop), and [CVE-2026-42211](https://github.com/advisories/GHSA-49rj-9fvp-4h2h) (React Router, constructor invocation through a vendored deserializer). Together they are design evidence rather than four implementation bugs: the abstraction that makes a server function look like a local call recurs across framework families, and so does the omission of a boundary where the wire format is treated as untrusted input. An application that adopts server functions inherits this design question whichever framework it chooses, and must decide for itself which operations are externally invocable.
- [CVE-2026-39371](https://github.com/advisories/GHSA-x8rx-789c-2pxq) and [CVE-2026-42190](https://github.com/advisories/GHSA-m2m6-cff5-3w7c): both advisories published by RedwoodSDK to date concern origin trust in server-function dispatch. A young framework’s first security findings tend to fall where its defaults were never explicitly decided, which is also where an application adopting it should expect to supply its own controls.

## Sources

- [OWASP A04:2021 Insecure Design](https://owasp.org/Top10/2021/A04_2021-Insecure_Design/)
- [OWASP API6:2023 Unrestricted Access to Sensitive Business Flows](https://owasp.org/API-Security/editions/2023/en/0xa6-unrestricted-access-to-sensitive-business-flows/)
- [Research references](../references.md#insecure-design-and-assurance)

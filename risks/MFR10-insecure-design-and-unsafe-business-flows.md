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

## Sources

- [OWASP A04:2021 Insecure Design](https://owasp.org/Top10/2021/A04_2021-Insecure_Design/)
- [OWASP API6:2023 Unrestricted Access to Sensitive Business Flows](https://owasp.org/API-Security/editions/2023/en/0xa6-unrestricted-access-to-sensitive-business-flows/)
- [Research references](../references.md#insecure-design-and-assurance)

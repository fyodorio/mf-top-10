# MFR02: Server–Client Data Boundary Failures

## Factors

- **Exploitability:** Easy
- **Prevalence:** Common
- **Detectability:** Average
- **Technical impact:** Severe

## Description

Server-only data, capabilities, configuration, or types cross into a browser-visible representation without an explicit least-privilege contract. Framework serialization, hydration payloads, page props, RSC/Flight payloads, server-island props, environment-variable exposure, and error pages make these transfers convenient — but any value sent to the browser must be treated as public.

This category is not limited to secrets. Excessive fields, internal identifiers, authorization state, business rules, source details, or data from a different tenant can produce confidentiality loss or enable later attacks.

## Metaframework-specific failure modes

- Passing database records or session objects to client components instead of defining a minimal view model.
- Misclassifying environment variables or importing server-only modules into client bundles.
- Implicit serialization of properties that were never meant for a client component or hydration payload.
- Exposing source maps, verbose errors, stack traces, server function source, build metadata, or development endpoints.
- Trusting client-held state or a hydrated authorization flag when making server-side decisions.

## Prevention and verification priorities

1. Define explicit request and response DTOs; select allowed fields rather than serializing model objects.
2. Keep secrets in server-only modules and use build-time checks that reject server-only imports in client code.
3. Classify every environment variable by exposure; use framework-supported public prefixes only for values safe to publish.
4. Inspect initial HTML, JSON/RSC/island payloads, client bundles, errors, and source maps as an unauthenticated and low-privilege user.
5. Re-authorize on the server; never accept a client-hydrated role, price, owner, or feature state as authoritative.

## Relevant CWEs

- [CWE-200: Exposure of Sensitive Information to an Unauthorized Actor](https://cwe.mitre.org/data/definitions/200.html)
- [CWE-201: Exposure of Sensitive Information Through Sent Data](https://cwe.mitre.org/data/definitions/201.html)
- [CWE-213: Exposure of Sensitive Information Due to Incompatible Policies](https://cwe.mitre.org/data/definitions/213.html)
- [CWE-497: Exposure of Sensitive System Information to an Unauthorized Control Sphere](https://cwe.mitre.org/data/definitions/497.html)
- [CWE-522: Insufficiently Protected Credentials](https://cwe.mitre.org/data/definitions/522.html)

## Representative evidence

- [CVE-2025-55183](https://github.com/advisories/GHSA-w37m-7fhw-fmv9): affected React Server Components/Next.js server functions could disclose compiled server-function source and business logic.
- [CVE-2026-44575](https://github.com/advisories/GHSA-267c-6grr-h53f): an alternate Next.js transport route could expose protected page content when middleware alone supplied authorization.
- [CVE-2025-24360](https://github.com/advisories/GHSA-2452-6xj8-jh47): Nuxt development-server CORS defaults could expose local source to a malicious origin.

## Sources

- [OWASP API3:2023](https://owasp.org/API-Security/editions/2023/en/0xa3-broken-object-property-level-authorization/)
- [OWASP Client-Side Security Risks](https://owasp.org/www-project-top-10-client-side-security-risks/)
- [Research references](../references.md#data-boundaries-and-client-side-exposure)

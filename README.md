# OWASP Top 10 Metaframework Security Risks

A draft-stage awareness document for full-stack JavaScript and TypeScript metaframework applications, including Next.js, Nuxt, Astro, SvelteKit, React Router framework mode, TanStack Start, SolidStart, and comparable systems.

These frameworks deliberately merge concerns that used to be separate: UI rendering, routing, data loading, server endpoints, build tooling, cache control, and deployment adapters. That integration is valuable, but it creates security boundaries which are easy to misunderstand or configure inconsistently. This project narrows the general OWASP Top 10 to those boundaries; it does **not** replace the OWASP Top 10, OWASP API Security Top 10, or framework-specific security guidance.

## Status and intended use

This is a research-backed initial taxonomy, not an OWASP-published standard or a quantified prevalence study. The ordering is a practical, provisional priority for reviewers of public, full-stack metaframework applications. It must not be read as a severity scale: a particular MF10 finding can be more serious than a particular MF01 finding.

The draft favors root causes over symptoms where possible.

## The Top 10

1. [MF01: Broken Identity and Access Control Across Routes, Server Functions, and Data APIs](risks/MF01-broken-identity-and-access-control.md)
2. [MF02: Server–Client Data Boundary Failures](risks/MF02-server-client-data-boundary-failures.md)
3. [MF03: Injection and Unsafe Client-Side Execution](risks/MF03-injection-and-unsafe-client-side-execution.md)
4. [MF04: Server-Side Request Forgery and Untrusted Request Origin](risks/MF04-ssrf-and-untrusted-request-origin.md)
5. [MF05: Routing, Rendering, and Cache Variant Confusion](risks/MF05-routing-rendering-and-cache-variant-confusion.md)
6. [MF06: Unrestricted Resource Consumption and Concurrency Failures](risks/MF06-resource-consumption-and-concurrency.md)
7. [MF07: Security Misconfiguration and Exposed Development Surfaces](risks/MF07-security-misconfiguration-and-development-surfaces.md)
8. [MF08: Supply-Chain and Build/Runtime Integrity Failures](risks/MF08-supply-chain-and-build-runtime-integrity.md)
9. [MF09: Security Logging, Monitoring, and Endpoint Inventory Failures](risks/MF09-logging-monitoring-and-inventory.md)
10. [MF10: Insecure Design and Unsafe Business Flows](risks/MF10-insecure-design-and-unsafe-business-flows.md)

## Ordering rationale

MF01–MF04 cover direct compromise paths: impersonating or exceeding an identity’s authority, exposing server-only data, executing attacker-controlled content, or making the server act as a network client. MF05–MF07 cover the framework’s request-processing lifecycle: variant routing/rendering, resource control, and operational configuration. MF08–MF10 cover integrity, visibility, and the design/assurance conditions that let the other failures persist.

## Provisional risk-factor legend

Each risk page uses the four factors common in OWASP-style risk descriptions.

- **Exploitability**: effort and prerequisites for a threat actor to exploit a representative weakness. `Easy` means an ordinary HTTP/browser request is often sufficient; `Average` requires target-specific behavior or chaining; `Difficult` requires unusual conditions or specialist capability.
- **Prevalence**: expected frequency in metaframework applications based on ecosystem design patterns, published research, and practitioner experience. `Widespread`, `Common`, and `Limited` are hypotheses, **not measured incidence rates**.
- **Detectability**: how readily an application owner can find the weakness with normal review and testing. `Easy` means routine tests or configuration inspection can reveal it; `Average` needs threat-model-aware tests; `Difficult` usually needs multi-layer, concurrency, cache, or production-like testing.
- **Technical impact**: representative worst credible impact to confidentiality, integrity, availability, or accountability. It is independent of a particular organization’s business impact.

The terms describe a category, not every vulnerability within it. Pages also provide representative CVE/GHSA and CWE references to make the boundaries testable and auditable.

## How this becomes data-driven

An incubation candidate should collect anonymized, reproducible data rather than assign numeric scores by intuition. A future data call should request, per application and assessment period:

1. the number of applications tested and whether each mapped CWE was observed at least once;
2. framework, major version, router/rendering modes, deployment adapter, and presence of shared caching;
3. testing coverage for each category, so absence of a finding is not mistaken for absence of a weakness;
4. validated CVE/CVSS mappings for framework and dependency defects;
5. findings from code review, dynamic testing, bug bounty, and incident response, with duplicates removed; and
6. a community survey for emerging risks that current tools cannot measure well.

This mirrors OWASP’s principle of being data-driven but not blindly data-driven. The project should publish its CWE mapping, collection window, inclusion criteria, and ranking method before presenting numerical prevalence or weighted scores.

## Contributions

Contributions should improve category boundaries, add reproducible cross-framework evidence, correct advisory mappings, and propose testable preventive guidance. Avoid turning a single implementation detail, a product feature, or a development fashion into a universal category without showing a reusable root cause.

See [research references](references.md) for the primary and secondary sources reviewed for this draft.

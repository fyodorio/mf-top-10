# Top 10 Metaframework Security Risks — Index

This is a draft-stage awareness document for full-stack JavaScript and TypeScript metaframework applications, including Next.js, Nuxt, Astro, SvelteKit, React Router framework mode, TanStack Start, SolidStart, and comparable systems.

These frameworks deliberately merge concerns that used to be separate: UI rendering, routing, data loading, server endpoints, build tooling, cache control, and deployment adapters. That integration is valuable, but it creates security boundaries which are easy to misunderstand or configure inconsistently. This project narrows the general OWASP Top 10 to those boundaries; it does **not** replace the OWASP Top 10, OWASP API Security Top 10, client-side guidance, or framework-specific security guidance.

## Status and intended use

This is a research-backed initial taxonomy, not a quantified prevalence study. The ordering is a practical, provisional priority for reviewers of public, full-stack metaframework applications. It must not be read as a severity scale: a particular MF10 finding can be more serious than a particular MF01 finding.

The draft favors root causes over symptoms where possible. It places hidden endpoints and server functions under access control; shared-cache failures under routing, rendering, and cache confusion; and AI-assisted development or weak type discipline under design and assurance rather than as standalone vulnerability classes.

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

Technical impact is deliberately **not** called severity. In common risk-rating practice, severity is a resulting rating for a particular finding after likelihood and impact are assessed in its real environment. Technical impact is one input to that assessment, and keeping the terms separate avoids implying that every instance of a category has the same severity.

The terms describe a category, not every vulnerability within it. The CVE/GHSA lists in each risk page are strong representative evidence for why the category matters. They are not complete use-case scenarios: an advisory documents a particular affected version and preconditions, while a scenario should demonstrate the reusable application-level misuse or attack path. Future revisions can add explicit attack scenarios alongside the evidence.

## Applying the list within an application security program

Use the Top 10 as an awareness and prioritization aid, then tailor it to the applications, APIs, data assets, threat actors, deployment models, and business tolerance for risk in scope. Establish a consistent risk model, define reusable security controls, and integrate security activities into existing work rather than treating the list as a one-time checklist.

For each application or service, teams should:

1. identify assets, trust boundaries, public request variants, data flows, and externally reachable server capabilities;
2. select relevant categories and define security requirements and abuse cases;
3. apply secure defaults and reusable controls for authorization, serialization, egress, caching, resource limits, and deployment configuration;
4. verify controls with review, automated testing, dynamic testing, and production-like infrastructure tests; and
5. measure coverage, findings, remediation, and recurring root causes to improve the program over time.

See the [roadmap](roadmap.md) for the evidence model and planned work, [contribution guidance](contributing.md) to participate, and [research references](references.md) for sources.

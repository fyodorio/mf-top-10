# Project Roadmap

This roadmap describes the first twelve months of work toward a maintained, evidence-led awareness document. Dates are intentionally relative so that the sequence remains useful if the project starts later than expected.

## Operating principles

- Treat the Top 10 as an awareness and prioritization aid, not a complete security standard or a severity ranking for individual findings.
- Make category boundaries, evidence, decision records, source attribution, and release criteria public.
- Use a risk-based approach: consider assets, data sensitivity, application exposure, threat actors, deployment model, and business impact before selecting controls or testing depth.
- Prefer repeatable security activities: threat modeling, secure design review, code review, composition analysis, dynamic testing, and operational monitoring.
- Seek practical input from application developers, framework maintainers, security researchers, platform providers, and users of affected frameworks.

## Months 1–3: Establish the foundation

Publish and maintain the initial taxonomy, category boundaries, source catalog, roadmap, contribution process, and documentation license.

Create a living crosswalk from each `MFR` category to relevant CWEs, adjacent OWASP projects, framework features, and known advisory patterns. Record category inclusion and exclusion decisions, especially where a risk could fit more than one category.

Define a minimum security review model for metaframework applications:

1. identify assets, actors, trust boundaries, public request variants, data flows, external dependencies, and deployment layers;
2. identify applicable `MFR` categories and abuse cases;
3. select reusable controls and verification activities appropriate to the risk; and
4. record gaps, remediation owners, and evidence of completion.

## Months 4–6: Establish the evidence model

Publish a data-call specification and a contributor-friendly evidence template. Do not publish numeric incidence, prevalence, or weighted ranking claims until the method, collection window, coverage, and limitations are documented.

For each assessed application and reporting period, collect anonymized and deduplicated information about:

1. framework, major version, router and rendering modes, adapter, hosting model, and shared-cache presence;
2. number of applications tested and whether each mapped CWE was observed at least once;
3. assessment coverage for each category, so “not observed” is not interpreted as “not tested”;
4. finding source, such as design review, code review, SAST, SCA, dynamic testing, bug bounty, incident response, or framework advisory;
5. validated CWE, CVE/GHSA, CVSS, exploit prerequisites, affected request variants, and remediation state where available; and
6. a minimal de-identification model that does not collect secrets, customer data, exploit payloads, or unnecessary organization identifiers.

Define normalization rules for duplicate findings, affected versions, multi-CWE findings, and framework vulnerabilities that require application-specific preconditions. Define a review process for source quality, reproducibility, and conflicting classifications.

## Months 7–9: Validate with practitioners

Run a structured public review of the initial taxonomy and evidence model. Seek examples from [multiple framework families](https://metaframe.works/comparison/) and deployment patterns, including self-hosted Node servers, serverless/edge adapters, static generation, hybrid rendering, shared CDNs, and multi-tenant applications.

Prioritize gaps that are difficult to capture through automated testing:

- authorization decisions spanning pages, loaders, actions, data transports, islands, and middleware;
- serialization and server-to-client data exposure;
- cache-key and response-variant behavior across framework and CDN boundaries;
- business workflow abuse, concurrency, and cost amplification; and
- observability, endpoint inventory, and operational control failures.

Publish a review summary describing accepted, rejected, deferred, and unresolved proposals with rationale.

## Months 10–12: Prepare the first revision

Use reviewed evidence to revise category definitions, CWE mappings, representative evidence, prevention guidance, and ordering rationale. If data quality permits, publish aggregate prevalence and coverage measures alongside their limitations; otherwise retain qualitative provisional labels and state why.

Issue a versioned release containing:

- the revised index and risk pages;
- an updated research and evidence appendix;
- documented methodology and data limitations;
- a summary of material changes since the prior release; and
- a maintenance plan for the next review cycle.

## Continuous work

Maintain a public backlog, respond to evidence and correction submissions, review new framework advisories, and publish periodic status updates. Track project health through meaningful indicators: contributor diversity, evidence quality, framework coverage, review turnaround, release cadence, and unresolved research gaps.

Use findings and feedback to improve the project’s reusable guidance. The goal is not to maximize category count or vulnerability volume; it is to help teams apply the most useful controls at the right points in their software lifecycle.

## Related documents

- [Detailed taxonomy](index.md)
- [Contribution guidance](contributing.md)
- [Research references](references.md)

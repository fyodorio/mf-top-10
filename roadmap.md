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

Advisory records change after this project cites them: identifiers are assigned, records propagate between databases, exploitation status becomes known, and links rot. Re-check cited evidence on a schedule rather than assuming a published citation stays accurate — `scripts/check-advisories.py` automates the detection, and the [maintenance guide](maintenance.md) defines the checks and cadence.

Use findings and feedback to improve the project’s reusable guidance. The goal is not to maximize category count or vulnerability volume; it is to help teams apply the most useful controls at the right points in their software lifecycle.

## Open classification questions

Questions raised during maintenance that change category boundaries or definitions are recorded here and decided at the next versioned release, not mid-cycle. Each records the interim rule that monthly maintenance follows until then.

### Access control or variant confusion (`MFR01` / `MFR05`)

Raised 2026-10-28. `MFR05` describes a correct rule that is skipped because two layers interpret a request differently, but several such cases are cited under `MFR01`: the Nuxt route-rule series from `CVE-2026-53721` to `GHSA-9v7c-q64q-vv33` (case, percent-encoding, and dot segments), Astro’s encoded-path middleware bypasses, and Next.js prefetch variants. `CWE-178` in `MFR01`’s mapping is a symptom of the same drift.

Interim rule: place new evidence under `MFR01` when the authorization rule is missing or wrong, and under `MFR05` when a correct rule is skipped by a parsing, normalization, or transport mismatch. Cite it under the other category only for a point that category makes and the primary one does not. Existing evidence is re-homed, and `CWE-178` reconsidered, at the release.

### Server-function wire formats as a cross-cutting weakness

Raised 2026-10-28. Request-borne payloads that a framework deserializes for its own server-function or component protocol produce findings in five categories: remote code execution (`MFR01` for Qwik `server$`, `MFR08` for React Server Components), resource exhaustion (`MFR06`: SvelteKit remote functions, Qwik `formToObj`, SolidStart), cross-site invocation (`MFR04`), and design (`MFR10`). Classification currently follows where the defect lives — an upstream runtime or the framework itself — rather than the weakness, which conflicts with the root-cause principle stated in the [index](index.md#status-and-intended-use).

Options for the release review: a crosswalk theme spanning categories, leaving the ten unchanged; or a dedicated category, which would require merging two existing ones to stay at ten. `MFR09` is the candidate most often raised, as a control failure with no exploitability score and the thinnest advisory evidence. One month of data is not enough to decide.

Interim rule: classify by the weakness the payload demonstrates, as now, and add each new instance to the `MFR10` cross-framework paragraph in the [references](references.md#insecure-design-and-assurance) so the pattern stays countable.

## Related documents

- [Detailed taxonomy](index.md)
- [Contribution guidance](contributing.md)
- [Research references](references.md)
- [Maintenance guide](maintenance.md)

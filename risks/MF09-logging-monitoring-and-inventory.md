# MF09: Security Logging, Monitoring, and Endpoint Inventory Failures

## Factors

- **Exploitability:** Not independently applicable
- **Prevalence:** Common
- **Detectability:** Difficult
- **Technical impact:** Moderate

## Description

The application owner cannot discover, investigate, contain, or learn from attacks because security-relevant events, deployed endpoints, rendering modes, cache behavior, framework versions, and data flows are not inventoried or observable. This is a control failure rather than a standalone initial-access vector, so exploitability is intentionally not scored.

Metaframework applications can create routes and server capabilities from file structure and compiler conventions. The deployed surface may include pages, server functions, route handlers, data endpoints, image or asset proxies, islands, prefetched routes, middleware/proxy paths, preview deployments, and adapter-specific endpoints. An inventory based only on a manually maintained API document will be incomplete.

## Metaframework-specific failure modes

- No authoritative route/function inventory across routers, locales, dynamic segments, preview deployments, and adapters.
- Missing audit records for authentication, authorization failures, sensitive mutations, server-function calls, cache purges, egress requests, and configuration changes.
- Logs omit correlation IDs, route variant, rendering mode, deployment version, tenant, outcome, or security-relevant request metadata.
- Sensitive tokens, passwords, authorization headers, request bodies, or personally identifiable data are logged.
- Alerts cannot distinguish a cache/routing anomaly, SSRF probe, authorization bypass attempt, or resource-exhaustion attack from expected traffic.

## Prevention and verification priorities

1. Generate and continuously verify an endpoint inventory from build manifests, framework route metadata, deployed probes, and adapter configuration.
2. Log security outcomes — not secrets — for identity events, authorization decisions, mutations, egress requests, cache events, rate-limit decisions, and administrator actions.
3. Correlate edge/CDN, proxy, framework, application, and cloud logs using request and deployment IDs.
4. Establish alerts and runbooks for abnormal route variants, authorization denials, server-side egress, cache poisoning indicators, spending spikes, and saturation.
5. Test incident reconstruction and ensure logging redacts credentials and sensitive payload fields.

## Relevant CWEs

- [CWE-778: Insufficient Logging](https://cwe.mitre.org/data/definitions/778.html)
- [CWE-223: Omission of Security-relevant Information](https://cwe.mitre.org/data/definitions/223.html)
- [CWE-532: Insertion of Sensitive Information into Log File](https://cwe.mitre.org/data/definitions/532.html)
- [CWE-1059: Incomplete Documentation](https://cwe.mitre.org/data/definitions/1059.html)

## Evidence and rationale

This category is intentionally CWE-led rather than CVE-led. A missing log, alert, route inventory, or incident runbook is usually not assigned a CVE, yet it directly determines detection, response time, and forensic confidence. OWASP similarly treats logging and monitoring as a Top 10 category despite limited CVE representation.

Published cache-poisoning, alternate-route, and development-surface advisories throughout MF01, MF05, and MF07 demonstrate why a metaframework-specific endpoint and variant inventory is necessary.

## Sources

- [OWASP A09:2021 Security Logging and Monitoring Failures](https://owasp.org/Top10/2021/A09_2021-Security_Logging_and_Monitoring_Failures/)
- [OWASP API9:2023 Improper Inventory Management](https://owasp.org/API-Security/editions/2023/en/0xa9-improper-inventory-management/)
- [Research references](../references.md#observability-and-inventory)

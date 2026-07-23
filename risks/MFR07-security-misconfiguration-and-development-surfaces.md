# MFR07: Security Misconfiguration and Exposed Development Surfaces

## Factors

- **Exploitability:** Easy
- **Prevalence:** Widespread
- **Detectability:** Easy
- **Technical impact:** Severe

## Description

Security-relevant framework, runtime, adapter, proxy, browser, cloud, and development-server configuration is missing, permissive, inconsistent, or left enabled outside its intended context. Full-stack metaframework applications often have configuration distributed across source code, environment variables, framework files, adapter settings, reverse proxies, CDNs, serverless platforms, and CI/CD.

This category includes exposure of development tooling and operational interfaces. It does not include a secret merely being serialized to a client — that is `MFR02` — or an out-of-date framework — that is `MFR08`.

## Metaframework-specific failure modes

- Development servers, devtools, inspector ports, source maps, test routes, debug manifests, or hot-reload APIs reachable from untrusted origins.
- Permissive CORS, missing host validation, trusted-proxy mistakes, broad allowed origins, or unprotected preview/staging environments.
- Missing or overly broad CSP, frame protection, cookie flags, permissions policy, TLS, security headers, or cache directives.
- Production builds running with development behavior or verbose errors; default credentials or unreviewed environment fallbacks.
- Serverless/edge adapters with unbounded permissions, public storage, overbroad service credentials, or absent egress policy.

## Prevention and verification priorities

1. Define production-safe defaults in versioned configuration and review changes as security-sensitive code.
2. Separate development, test, preview, and production credentials, origins, data, and network access; do not expose development tools publicly.
3. Validate hosts and forwarded headers at the first trusted proxy; configure CORS per route and credential mode, never by convenience.
4. Set and test browser security headers, secure cookie attributes, error handling, source-map policy, and cache-control on the deployed platform.
5. Scan running environments, not just repository files, for exposed ports, routes, artifacts, and permissive cloud/IAM configuration.

## Relevant CWEs

- [CWE-16: Configuration](https://cwe.mitre.org/data/definitions/16.html)
- [CWE-489: Active Debug Code](https://cwe.mitre.org/data/definitions/489.html)
- [CWE-942: Permissive Cross-domain Policy with Untrusted Domains](https://cwe.mitre.org/data/definitions/942.html)
- [CWE-215: Insertion of Sensitive Information Into Debugging Code](https://cwe.mitre.org/data/definitions/215.html)
- [CWE-798: Use of Hard-coded Credentials](https://cwe.mitre.org/data/definitions/798.html)

## Representative evidence

- [CVE-2025-24360](https://github.com/advisories/GHSA-2452-6xj8-jh47): Nuxt’s development CORS behavior could allow a malicious site to read local development-server responses.
- [CVE-2024-23657](https://github.com/advisories/GHSA-rcvg-rgf7-pppv): Nuxt Devtools path traversal and origin issues could expose local files and, in some configurations, enable code execution.
- [CVE-2024-34344](https://github.com/advisories/GHSA-v784-fjjh-f8r4): Nuxt test-mode component loading could execute attacker-controlled code in a developer environment.

## Sources

- [OWASP A05:2021 Security Misconfiguration](https://owasp.org/Top10/2021/A05_2021-Security_Misconfiguration/)
- [OWASP Node.js Security Cheat Sheet](https://cheatsheetseries.owasp.org/cheatsheets/Nodejs_Security_Cheat_Sheet.html)
- [Research references](../references.md#configuration-and-development-surfaces)

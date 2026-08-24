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
- Locality or origin decisions inferred from request headers such as `Sec-Fetch-Site`, `Origin`, or `Referer`, which a non-browser client can simply omit, instead of from the peer address or an authenticated token.
- Development-tool control channels — inspector RPC, hot-reload sockets, editor-launch hooks — reachable without authentication from another local process, a LAN peer, or a page the developer visits while the server runs.
- Security-relevant behavior that differs by bundler, compiler, adapter, or runtime target, so configuration validated under one build pipeline is untested under the one actually deployed.
- A development server that binds all interfaces by default while also serving a verbose error surface, so a permissive bind address and a debug feature that are each individually defensible combine into unauthenticated secret disclosure.
- Development artifacts written to disk — TLS keys, caches, environment snapshots, build metadata — with permissions that any local user or process can read.
- Build-time tooling that executes shell commands built from repository metadata, filenames, or branch names, making the build host a request-free injection surface.

## Prevention and verification priorities

1. Define production-safe defaults in versioned configuration and review changes as security-sensitive code.
2. Separate development, test, preview, and production credentials, origins, data, and network access; do not expose development tools publicly.
3. Validate hosts and forwarded headers at the first trusted proxy; configure CORS per route and credential mode, never by convenience. Base a “local only” decision on the connecting peer address, and authenticate every development control channel.
4. Set and test browser security headers, secure cookie attributes, error handling, source-map policy, and cache-control on the deployed platform.
5. Scan running environments, not just repository files, for exposed ports, routes, artifacts, and permissive cloud/IAM configuration.

## Relevant CWEs

- [CWE-16: Configuration](https://cwe.mitre.org/data/definitions/16.html)
- [CWE-489: Active Debug Code](https://cwe.mitre.org/data/definitions/489.html)
- [CWE-942: Permissive Cross-domain Policy with Untrusted Domains](https://cwe.mitre.org/data/definitions/942.html)
- [CWE-215: Insertion of Sensitive Information Into Debugging Code](https://cwe.mitre.org/data/definitions/215.html)
- [CWE-798: Use of Hard-coded Credentials](https://cwe.mitre.org/data/definitions/798.html)
- [CWE-306: Missing Authentication for Critical Function](https://cwe.mitre.org/data/definitions/306.html)
- [CWE-290: Authentication Bypass by Spoofing](https://cwe.mitre.org/data/definitions/290.html)

## Representative evidence

- [CVE-2025-24360](https://github.com/advisories/GHSA-2452-6xj8-jh47): Nuxt’s development CORS behavior could allow a malicious site to read local development-server responses.
- [CVE-2024-23657](https://github.com/advisories/GHSA-rcvg-rgf7-pppv): Nuxt Devtools path traversal and origin issues could expose local files and, in some configurations, enable code execution.
- [CVE-2024-34344](https://github.com/advisories/GHSA-v784-fjjh-f8r4): Nuxt test-mode component loading could execute attacker-controlled code in a developer environment.
- [CVE-2026-71319](https://github.com/advisories/GHSA-279x-mwfv-vcqv): an unauthenticated Nuxt DevTools RPC method exposed over the Vite hot-reload socket allowed arbitrary command execution on a developer machine, reachable from a local process, a LAN peer when the server was bound to an interface, or a malicious site visited while the development server ran.
- [CVE-2026-72744](https://github.com/advisories/GHSA-7c4v-fwgw-9rf7): a Nuxt development endpoint treated a request lacking `Sec-Fetch-Site`, `Origin`, and `Referer` as local, disclosing the project path and workspace identifier; the fix validates the connecting peer address instead of request headers.
- [GHSA-r5mf-4r5x-q78f](https://github.com/quasarframework/quasar/security/advisories/GHSA-r5mf-4r5x-q78f): Quasar’s development SSR/SSG error page serialized every `process.env` variable, request header, and cookie into the response, and the development server binds `0.0.0.0` by default — so one unauthenticated `GET` returned the developer’s cloud keys, registry tokens, and database URLs to any host that could reach the port. The same page embedded that data in a `<script>` element behind an ASCII-case-sensitive `</script>` guard requiring a literal `>`, which `</SCRIPT>`, `</script >`, and `</script/>` all escape. Two independent misconfigurations — a verbose error surface and a permissive bind address — that are each defensible alone and severe together.
- [CVE-2025-64757](https://github.com/advisories/GHSA-x3h8-62x9-952g) and [CVE-2025-64745](https://github.com/advisories/GHSA-w2vj-39qv-7vh7): arbitrary local file read through the Astro development server, and reflected XSS on its error page.
- [GHSA-fh39-c73x-5pjv](https://github.com/quasarframework/quasar/security/advisories/GHSA-fh39-c73x-5pjv): Quasar cached development TLS private keys with overly permissive filesystem permissions, exposing them to any local user.
- [CVE-2026-16492](https://github.com/advisories/GHSA-g3hq-vgww-mrhj): OS command injection in a UmiJS Git file helper, reached through repository metadata during a build rather than through an HTTP request — the build host is a configuration surface too.

## Sources

- [OWASP A05:2021 Security Misconfiguration](https://owasp.org/Top10/2021/A05_2021-Security_Misconfiguration/)
- [OWASP Node.js Security Cheat Sheet](https://cheatsheetseries.owasp.org/cheatsheets/Nodejs_Security_Cheat_Sheet.html)
- [Research references](../references.md#configuration-and-development-surfaces)

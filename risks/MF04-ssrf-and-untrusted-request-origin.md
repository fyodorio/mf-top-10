# MF04: Server-Side Request Forgery and Untrusted Request Origin

## Factors

- **Exploitability:** Average
- **Prevalence:** Common
- **Detectability:** Average
- **Technical impact:** Severe

## Description

The application trusts an attacker-controlled URL, host, forwarded header, request origin, redirect destination, or proxy target when deciding where the server should connect or how it should construct an absolute URL. The attacker can make the server reach internal services, cloud metadata endpoints, management planes, or another tenant’s origin.

Metaframework adapters regularly reconstruct requests from `Host` and `X-Forwarded-*` headers, generate absolute URLs, proxy assets, support image/icon fetching, run webhooks, and issue server-side redirects. This makes origin trust a cross-cutting server-runtime concern, not merely a “URL preview” issue.

## Metaframework-specific failure modes

- Fetching a user-provided URL for imports, images, webhooks, previews, redirects, or AI retrieval.
- Trusting `Host`, `X-Forwarded-Host`, `X-Forwarded-Proto`, or port headers from arbitrary clients rather than a known proxy.
- Building callback, redirect, fetch, or asset URLs from `request.url` without validating origin.
- Following redirect chains after validating only the initial URL.
- Exposing self-hosted framework servers directly without ingress host validation and egress restrictions.

## Prevention and verification priorities

1. Treat all client-supplied URLs and forwarding headers as untrusted. Configure trusted proxies explicitly and validate allowed hosts at the ingress.
2. Use strict allowlists for destination origins, schemes, ports, media types, and redirect behavior; resolve and re-check each redirect.
3. Isolate outbound fetching in a restricted network path, block metadata and private-address access, and minimize its credentials.
4. Do not return raw internal fetch responses or timing details to the caller.
5. Test URL parsers with encoded, scheme-relative, IPv6, credential, redirect, DNS-rebinding, and forwarded-header cases.

## Relevant CWEs

- [CWE-918: Server-Side Request Forgery](https://cwe.mitre.org/data/definitions/918.html)
- [CWE-20: Improper Input Validation](https://cwe.mitre.org/data/definitions/20.html)
- [CWE-441: Unintended Proxy or Intermediary](https://cwe.mitre.org/data/definitions/441.html)
- [CWE-601: URL Redirection to Untrusted Site](https://cwe.mitre.org/data/definitions/601.html)

## Representative evidence

- [CVE-2024-34351](https://github.com/advisories/GHSA-fr5h-rqp8-mj6g): Next.js Server Actions could perform SSRF through a modified `Host` header under documented self-hosted conditions.
- [CVE-2024-42352](https://github.com/advisories/GHSA-cxgv-px37-4mp2): Nuxt Icon path parsing enabled SSRF.
- [CVE-2025-64525](https://github.com/advisories/GHSA-hr2q-hp5q-x767): Astro URL construction from untrusted forwarding headers enabled SSRF and middleware bypasses.
- [CVE-2025-67647](https://github.com/advisories/GHSA-j62c-4x62-9r35): a SvelteKit prerendering configuration could enable SSRF and denial of service.

## Sources

- [OWASP API7:2023 Server Side Request Forgery](https://owasp.org/API-Security/editions/2023/en/0xa7-server-side-request-forgery/)
- [OWASP SSRF Prevention Cheat Sheet](https://cheatsheetseries.owasp.org/cheatsheets/Server_Side_Request_Forgery_Prevention_Cheat_Sheet.html)
- [Research references](../references.md#ssrf-and-origin-trust)

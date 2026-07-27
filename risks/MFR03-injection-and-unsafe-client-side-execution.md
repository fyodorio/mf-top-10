# MFR03: Injection and Unsafe Client-Side Execution

## Factors

- **Exploitability:** Average
- **Prevalence:** Widespread
- **Detectability:** Average
- **Technical impact:** Severe

## Description

Untrusted data is interpreted as code, markup, a query, a command, a template, a URL, or another executable language. Automatic escaping by React, Vue, Svelte, Solid, and template systems reduces common cases; it does not protect explicit HTML sinks, DOM APIs, Markdown/MDX renderers, dynamic imports, database queries, shell commands, or a framework defect in the rendering pipeline.

The rendering model increases the number of contexts to examine: server-rendered HTML, hydration bootstraps, RSC/Flight or island payloads, streamed chunks, client navigation, and third-party client code.

## Metaframework-specific failure modes

- Passing untrusted data to `dangerouslySetInnerHTML`, `v-html`, `{@html}`, `innerHTML`, or an unsafe Markdown/MDX renderer.
- Creating links, redirects, scripts, styles, or DOM identifiers from unvalidated input.
- Assuming server-side rendering makes client-side XSS impossible.
- Building SQL/NoSQL queries, filesystem paths, commands, dynamic imports, or templates from route/query/form input.
- Trusting third-party client code or named DOM properties without considering DOM clobbering.
- Forwarding request-supplied values into a dynamic component resolver, polymorphic root, or runtime template compiler — explicitly, or implicitly through attribute fallthrough of props the component never declared.
- Enabling a runtime template compiler or other code-generating option in a server-rendering path, which turns any reachable string property into a code sink.

## Prevention and verification priorities

1. Prefer framework-native escaped rendering and typed APIs over raw HTML; allow raw HTML only through a reviewed sanitizer with a narrow policy.
2. Apply context-specific output encoding. Validation is necessary but does not replace output encoding.
3. Use parameterized database APIs; never compose commands, queries, import specifiers, or filesystem paths from untrusted strings.
4. Deploy a restrictive Content Security Policy and test it; it limits blast radius but does not fix injection.
5. Test SSR and client-navigation paths, HTML-bearing content, URL parameters, and stored content; include DOM-clobbering cases where untrusted markup is allowed.

## Relevant CWEs

- [CWE-79: Improper Neutralization of Input During Web Page Generation (XSS)](https://cwe.mitre.org/data/definitions/79.html)
- [CWE-89: Improper Neutralization of Special Elements used in an SQL Command](https://cwe.mitre.org/data/definitions/89.html)
- [CWE-78: Improper Neutralization of Special Elements used in an OS Command](https://cwe.mitre.org/data/definitions/78.html)
- [CWE-94: Improper Control of Generation of Code](https://cwe.mitre.org/data/definitions/94.html)
- [CWE-1336: Improper Neutralization of Special Elements Used in a Template Engine](https://cwe.mitre.org/data/definitions/1336.html)

## Representative evidence

- [CVE-2025-32388](https://github.com/advisories/GHSA-6q87-84jw-cjhp): tracked SvelteKit search-parameter names were serialized unsafely into server-rendered output.
- [CVE-2024-47885](https://github.com/advisories/GHSA-m85w-3h95-hcf9): an Astro client-router DOM-clobbering gadget could produce XSS when untrusted scriptless markup was present.
- [CVE-2025-64764](https://zhero-web-sec.github.io/research-and-things/unlocking-reflected-xss-in-the-astro-framework): published Astro reflected-XSS research.
- [CVE-2026-44581](https://github.com/advisories/GHSA-ffhc-5mcf-pf4q): malformed request-derived CSP nonce data could result in stored XSS in affected Next.js App Router deployments behind shared caches.
- [GHSA-9473-5f9j-94wq](https://github.com/nuxt/nuxt/security/advisories/GHSA-9473-5f9j-94wq): with Vue’s runtime compiler enabled, an injected `template` key in Nuxt server-island props was compiled and executed in the server process, producing remote code execution rather than client-side XSS.
- [GHSA-48hr-524c-v5w3](https://github.com/nuxt/nuxt/security/advisories/GHSA-48hr-524c-v5w3): undeclared Nuxt island props reaching a polymorphic component root allowed instantiation of arbitrary HTML elements or globally registered components.

## Sources

- [OWASP A03:2021 Injection](https://owasp.org/Top10/2021/A03_2021-Injection/)
- [OWASP Client-Side Security Risks](https://owasp.org/www-project-top-10-client-side-security-risks/)
- [Research references](../references.md#injection-and-client-execution)

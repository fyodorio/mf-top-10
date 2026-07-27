# Research References

This catalog records the sources reviewed for the initial draft. Primary sources establish the taxonomy and advisory evidence. Secondary sources were used as practitioner guidance and are not treated as authority for vulnerability classification.

## Citing advisories

Every published GitHub security advisory has a GHSA identifier. A CVE identifier is additional: a maintainer requests one when publishing, so an advisory can be complete, severe, and permanent without ever receiving a CVE. An entry cited as `GHSA-…` therefore says nothing about its severity, exploitability, or how it was disclosed — only that no CVE was assigned, or that none had been assigned when the record was reviewed.

Two rules keep citations predictable:

1. **Identifier.** Cite the CVE if one is assigned, otherwise the GHSA. Never both in the same label — the identifier shown already tells the reader which exists.
2. **URL.** Link to `https://github.com/advisories/GHSA-…` once the advisory is in the GitHub Advisory Database. Until then, link to the maintainer’s repository advisory page, which stays valid afterward.

Advisory records were last reviewed on 2026-07-27. Newly published advisories may gain a CVE identifier and a GitHub Advisory Database entry within days of that date, so `GHSA-…` citations are re-checked each review cycle rather than annotated in place.

This catalog does not rank evidence by observed exploitation, and no entry should be read as “exploited” or “not exploited” from its identifier. Where that question matters, consult the [CISA Known Exploited Vulnerabilities catalog](https://www.cisa.gov/known-exploited-vulnerabilities-catalog) and [EPSS](https://www.first.org/epss/), which are maintained for exactly that purpose and change over time. As of 2026-07-27, one advisory cited in this document appears in the KEV catalog: `CVE-2025-55182`, noted under `MFR08`.

## Vendor coordinated release roundups

- [Next.js July 2026 security release](https://nextjs.org/blog/july-2026-security-release) — nine advisories fixed in `15.5.21` and `16.2.11`, reviewed 2026-07-27. Links CVE records only; the corresponding GHSA identifiers were resolved from the GitHub Advisory Database.
- [Nuxt 4.5.1 and 3.21.10 security releases](https://nuxt.com/blog/v4-5-security) — eight advisories fixed in `4.5.1`, `3.21.10`, and `@nuxt/devtools@3.3.1`, reviewed 2026-07-27. Published the same day it was reviewed, so none of the eight had a CVE identifier or a GitHub Advisory Database entry yet.
- [Next.js security release program](https://nextjs.org/blog/next-security-release-program) — preannounced security releases against Active and Maintenance LTS lines; relevant to patch-management planning under `MFR08`.

## Methodology and adjacent OWASP projects

- [OWASP Top 10:2021 Introduction and methodology](https://owasp.org/Top10/2021/A00_2021_Introduction/)
- [OWASP Risk Rating Methodology](https://owasp.org/www-community/OWASP_Risk_Rating_Methodology)
- [OWASP Top 10:2025 — Establishing a Modern Application Security Program](https://owasp.org/Top10/2025/0x03_2025-Establishing_a_Modern_Application_Security_Program/)
- [OWASP API Security Top 10:2023](https://owasp.org/API-Security/editions/2023/en/0x11-t10/)
- [OWASP Client-Side Security Risks](https://owasp.org/www-project-top-10-client-side-security-risks/)
- [OWASP Node.js Security Cheat Sheet](https://cheatsheetseries.owasp.org/cheatsheets/Nodejs_Security_Cheat_Sheet.html)
- [OWASP SSRF Prevention Cheat Sheet](https://cheatsheetseries.owasp.org/cheatsheets/Server_Side_Request_Forgery_Prevention_Cheat_Sheet.html)
- [OWASP Project Policy](https://policy.owasp.org/operational/projects)
- [OWASP Project Procedures](https://owasp.org/www-staff/procedures/projects)

## Access control and server functions

- [CVE-2025-29927: Next.js middleware authorization bypass](https://github.com/advisories/GHSA-f82v-jwr5-mffw)
- [CVE-2026-44575: Next.js App Router segment-prefetch middleware bypass](https://github.com/advisories/GHSA-267c-6grr-h53f)
- [CVE-2026-44573: Next.js i18n data-route middleware bypass](https://github.com/advisories/GHSA-36qx-fr4f-26g5)
- [CVE-2026-46342: Nuxt island shared-cache poisoning and island authorization note](https://github.com/advisories/GHSA-g8wj-3cr3-6w7v)
- [CVE-2026-53721: Nuxt route-rule middleware bypass through router/matcher case-sensitivity mismatch](https://github.com/advisories/GHSA-mm7m-92g8-7m47)
- [GHSA-hxvh-4h3w-prp9: Nuxt mixed-case route rules silently dropped, bypassing `appMiddleware` gates](https://github.com/nuxt/nuxt/security/advisories/GHSA-hxvh-4h3w-prp9) — incomplete fix for CVE-2026-53721.
- [CVE-2026-64642: Next.js middleware/proxy bypass with Turbopack and a single locale](https://github.com/advisories/GHSA-6gpp-xcg3-4w24)
- [Ameer Hamza: Your Next.js app is vulnerable. Let’s fix it.](https://medium.com/@hamza97/your-next-js-app-will-be-a-nightmare-for-hackers-after-you-do-this-090f4bf4e315) — secondary guidance on server actions, validation, secrets, and rate limits.

## Data boundaries and client-side exposure

- [CVE-2025-55183: React Server Components server-function source exposure](https://github.com/advisories/GHSA-w37m-7fhw-fmv9)
- [CVE-2025-24360: Nuxt development-server CORS exposure](https://github.com/advisories/GHSA-2452-6xj8-jh47)
- [CVE-2026-64643: Next.js unauthenticated disclosure of Server Action and `use cache` endpoint identifiers](https://github.com/advisories/GHSA-955p-x3mx-jcvp)
- [OWASP API3:2023 Broken Object Property Level Authorization](https://owasp.org/API-Security/editions/2023/en/0xa3-broken-object-property-level-authorization/)

## Injection and client execution

- [CVE-2025-32388: SvelteKit XSS through tracked search parameters](https://github.com/advisories/GHSA-6q87-84jw-cjhp)
- [CVE-2024-47885: Astro client-router DOM clobbering XSS](https://github.com/advisories/GHSA-m85w-3h95-hcf9)
- [CVE-2025-64764: Astro reflected-XSS research](https://zhero-web-sec.github.io/research-and-things/unlocking-reflected-xss-in-the-astro-framework)
- [CVE-2026-44581: Next.js CSP nonce XSS](https://github.com/advisories/GHSA-ffhc-5mcf-pf4q)
- [GHSA-9473-5f9j-94wq: Nuxt server-island runtime template injection to server-side code execution](https://github.com/nuxt/nuxt/security/advisories/GHSA-9473-5f9j-94wq) — requires `vue.runtimeCompiler`.
- [GHSA-48hr-524c-v5w3: Nuxt unauthorized component instantiation through undeclared island props](https://github.com/nuxt/nuxt/security/advisories/GHSA-48hr-524c-v5w3)

## SSRF and origin trust

- [CVE-2024-34351: Next.js Server Actions SSRF](https://github.com/advisories/GHSA-fr5h-rqp8-mj6g)
- [CVE-2024-42352: Nuxt Icon SSRF](https://github.com/advisories/GHSA-cxgv-px37-4mp2)
- [CVE-2025-64525: Astro forwarded-header URL manipulation](https://github.com/advisories/GHSA-hr2q-hp5q-x767)
- [CVE-2025-67647: SvelteKit prerendering SSRF and DoS](https://github.com/advisories/GHSA-j62c-4x62-9r35)
- [CVE-2026-64645: Next.js SSRF and open redirect through an attacker-controlled rewrite/redirect destination hostname](https://github.com/advisories/GHSA-p9j2-gv94-2wf4)
- [CVE-2026-64649: Next.js Server Actions SSRF on custom servers through Host-associated headers](https://github.com/advisories/GHSA-89xv-2m56-2m9x)
- [OWASP API7:2023 Server Side Request Forgery](https://owasp.org/API-Security/editions/2023/en/0xa7-server-side-request-forgery/)

## Routing, rendering, and caching

- [zhero: Next.js and the corrupt middleware](https://zhero-web-sec.github.io/research-and-things/nextjs-and-the-corrupt-middleware)
- [zhero: Next.js, cache, and chains: the stale elixir](https://zhero-web-sec.github.io/research-and-things/nextjs-cache-and-chains-the-stale-elixir)
- [zhero: Eclipse on Next.js](https://zhero-web-sec.github.io/research-and-things/eclipse-on-nextjs-conditioned-exploitation-of-an-intended-race-condition)
- [zhero: Nuxt, show me your payload](https://zhero-web-sec.github.io/research-and-things/nuxt-show-me-your-payload)
- [zhero: React Router and the Remix’ed path](https://zhero-web-sec.github.io/research-and-things/react-router-and-the-remixed-path)
- [CVE-2025-27415: Nuxt cache poisoning](https://github.com/advisories/GHSA-jvhm-gjrh-3h93)
- [CVE-2025-43864: React Router SPA-mode cache-poisoning DoS](https://github.com/advisories/GHSA-f46r-rw29-r322)
- [CVE-2026-44576: Next.js RSC cache poisoning](https://github.com/advisories/GHSA-wfc6-r584-vfw7)
- [CVE-2026-44572: Next.js redirect cache poisoning](https://github.com/advisories/GHSA-3g8h-86w9-wvmq)
- [GHSA-wm8w-6qjm-cv43: Nuxt `_payload.json` cached without a user dimension, disclosing another user’s SSR data](https://github.com/nuxt/nuxt/security/advisories/GHSA-wm8w-6qjm-cv43) — remediation includes purging CDN and edge caches.
- [CVE-2026-64648: Next.js server-side `fetch` cache confusion for requests with bodies](https://github.com/advisories/GHSA-68g3-v927-f742)
- [CVE-2026-64647: Next.js server-side `fetch` cache-key collision for bodies containing invalid UTF-8 sequences](https://github.com/advisories/GHSA-4633-3j49-mh5q)

## Resource control and concurrency

- [CVE-2024-56332: Next.js Server Actions DoS](https://github.com/advisories/GHSA-7m27-7ghc-44w9)
- [CVE-2025-32421: Next.js race condition to cache poisoning](https://github.com/advisories/GHSA-qpjv-v59x-3qc4)
- [CVE-2025-59472: Next.js PPR unbounded memory consumption](https://github.com/advisories/GHSA-5f7q-jpqc-wp7h)
- [CVE-2026-44579: Next.js Cache Components connection exhaustion](https://github.com/advisories/GHSA-mg66-mrh9-m8jx)
- [GHSA-hxcr-hm88-mpq6: Nuxt island out-of-memory crash through unbounded `v-for` expansion](https://github.com/nuxt/nuxt/security/advisories/GHSA-hxcr-hm88-mpq6)
- [GHSA-9pgf-384g-p7mv: Nuxt island CPU exhaustion from parsing and hashing before hash validation](https://github.com/nuxt/nuxt/security/advisories/GHSA-9pgf-384g-p7mv)
- [CVE-2026-64641: Next.js Server Actions denial of service through excessive iteration](https://github.com/advisories/GHSA-m99w-x7hq-7vfj)
- [CVE-2026-64644: Next.js Image Optimization API CPU exhaustion through malicious SVG content](https://github.com/advisories/GHSA-q8wf-6r8g-63ch)
- [CVE-2026-64646: Next.js unbounded Server Action payload in the Edge runtime](https://github.com/advisories/GHSA-4c39-4ccg-62r3)
- [OWASP API4:2023 Unrestricted Resource Consumption](https://owasp.org/API-Security/editions/2023/en/0xa4-unrestricted-resource-consumption/)

## Configuration and development surfaces

- [CVE-2024-23657: Nuxt Devtools traversal and cross-site WebSocket exposure](https://github.com/advisories/GHSA-rcvg-rgf7-pppv)
- [CVE-2024-34344: Nuxt test-mode code execution](https://github.com/advisories/GHSA-v784-fjjh-f8r4)
- [GHSA-279x-mwfv-vcqv: unauthenticated Nuxt DevTools RPC allowing arbitrary command execution on a developer host](https://github.com/nuxt/nuxt/security/advisories/GHSA-279x-mwfv-vcqv) — fixed in `@nuxt/devtools@3.3.1`.
- [GHSA-7c4v-fwgw-9rf7: Nuxt development-server path and workspace disclosure through a header-based locality check](https://github.com/nuxt/nuxt/security/advisories/GHSA-7c4v-fwgw-9rf7)
- [OWASP A05:2021 Security Misconfiguration](https://owasp.org/Top10/2021/A05_2021-Security_Misconfiguration/)

## Supply chain and runtime integrity

- [CVE-2025-55182: React Server Components RCE](https://github.com/advisories/GHSA-9qr9-h5gf-34mp)
- [CVE-2025-59143: `color` npm account takeover malware](https://github.com/advisories/GHSA-qrmh-qg46-72pp)
- [GHSA-hxvh-4h3w-prp9: incomplete fix for CVE-2026-53721](https://github.com/nuxt/nuxt/security/advisories/GHSA-hxvh-4h3w-prp9) — cited here as evidence that a patched version string is not evidence of a closed weakness.
- [OWASP A06:2021 Vulnerable and Outdated Components](https://owasp.org/Top10/2021/A06_2021-Vulnerable_and_Outdated_Components/)
- [OWASP A08:2021 Software and Data Integrity Failures](https://owasp.org/Top10/2021/A08_2021-Software_and_Data_Integrity_Failures/)

## Observability and inventory

- [CVE-2026-64643: Next.js Server Function endpoint disclosure, documented as reconnaissance for a broader attack chain](https://github.com/advisories/GHSA-955p-x3mx-jcvp)
- [GHSA-hxcr-hm88-mpq6: Nuxt island endpoint identifiers are predictable, non-secret digests](https://github.com/nuxt/nuxt/security/advisories/GHSA-hxcr-hm88-mpq6) — cited here for endpoint reachability, not for its denial-of-service impact.
- [OWASP A09:2021 Security Logging and Monitoring Failures](https://owasp.org/Top10/2021/A09_2021-Security_Logging_and_Monitoring_Failures/)
- [OWASP API9:2023 Improper Inventory Management](https://owasp.org/API-Security/editions/2023/en/0xa9-improper-inventory-management/)

## Insecure design and assurance

- [OWASP A04:2021 Insecure Design](https://owasp.org/Top10/2021/A04_2021-Insecure_Design/)
- [OWASP API6:2023 Unrestricted Access to Sensitive Business Flows](https://owasp.org/API-Security/editions/2023/en/0xa6-unrestricted-access-to-sensitive-business-flows/)
- [How OWASP Helps You Secure Your Full-Stack Web Applications](https://www.smashingmagazine.com/2025/02/how-owasp-helps-secure-full-stack-web-applications/) — secondary discussion of full-stack JavaScript concerns.
- [OWASP Node.js Best Practices Guide](https://www.nodejs-security.com/blog/owasp-nodejs-best-practices-guide) — secondary Node.js-oriented guidance.
- [Best Practices for Security in Next.js](https://blog.openreplay.com/best-practices-for-security-in-nextjs/) — secondary Next.js-oriented guidance.

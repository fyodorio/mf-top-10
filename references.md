# Research References

This catalog records the sources reviewed for the initial draft. Primary sources establish the taxonomy and advisory evidence. Secondary sources were used as practitioner guidance and are not treated as authority for vulnerability classification.

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
- [Ameer Hamza: Your Next.js app is vulnerable. Let’s fix it.](https://medium.com/@hamza97/your-next-js-app-will-be-a-nightmare-for-hackers-after-you-do-this-090f4bf4e315) — secondary guidance on server actions, validation, secrets, and rate limits.

## Data boundaries and client-side exposure

- [CVE-2025-55183: React Server Components server-function source exposure](https://github.com/advisories/GHSA-w37m-7fhw-fmv9)
- [CVE-2025-24360: Nuxt development-server CORS exposure](https://github.com/advisories/GHSA-2452-6xj8-jh47)
- [OWASP API3:2023 Broken Object Property Level Authorization](https://owasp.org/API-Security/editions/2023/en/0xa3-broken-object-property-level-authorization/)

## Injection and client execution

- [CVE-2025-32388: SvelteKit XSS through tracked search parameters](https://github.com/advisories/GHSA-6q87-84jw-cjhp)
- [CVE-2024-47885: Astro client-router DOM clobbering XSS](https://github.com/advisories/GHSA-m85w-3h95-hcf9)
- [CVE-2025-64764: Astro reflected-XSS research](https://zhero-web-sec.github.io/research-and-things/unlocking-reflected-xss-in-the-astro-framework)
- [CVE-2026-44581: Next.js CSP nonce XSS](https://github.com/advisories/GHSA-ffhc-5mcf-pf4q)

## SSRF and origin trust

- [CVE-2024-34351: Next.js Server Actions SSRF](https://github.com/advisories/GHSA-fr5h-rqp8-mj6g)
- [CVE-2024-42352: Nuxt Icon SSRF](https://github.com/advisories/GHSA-cxgv-px37-4mp2)
- [CVE-2025-64525: Astro forwarded-header URL manipulation](https://github.com/advisories/GHSA-hr2q-hp5q-x767)
- [CVE-2025-67647: SvelteKit prerendering SSRF and DoS](https://github.com/advisories/GHSA-j62c-4x62-9r35)
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

## Resource control and concurrency

- [CVE-2024-56332: Next.js Server Actions DoS](https://github.com/advisories/GHSA-7m27-7ghc-44w9)
- [CVE-2025-32421: Next.js race condition to cache poisoning](https://github.com/advisories/GHSA-qpjv-v59x-3qc4)
- [CVE-2025-59472: Next.js PPR unbounded memory consumption](https://github.com/advisories/GHSA-5f7q-jpqc-wp7h)
- [CVE-2026-44579: Next.js Cache Components connection exhaustion](https://github.com/advisories/GHSA-mg66-mrh9-m8jx)
- [OWASP API4:2023 Unrestricted Resource Consumption](https://owasp.org/API-Security/editions/2023/en/0xa4-unrestricted-resource-consumption/)

## Configuration and development surfaces

- [CVE-2024-23657: Nuxt Devtools traversal and cross-site WebSocket exposure](https://github.com/advisories/GHSA-rcvg-rgf7-pppv)
- [CVE-2024-34344: Nuxt test-mode code execution](https://github.com/advisories/GHSA-v784-fjjh-f8r4)
- [OWASP A05:2021 Security Misconfiguration](https://owasp.org/Top10/2021/A05_2021-Security_Misconfiguration/)

## Supply chain and runtime integrity

- [CVE-2025-55182: React Server Components RCE](https://github.com/advisories/GHSA-9qr9-h5gf-34mp)
- [CVE-2025-59143: `color` npm account takeover malware](https://github.com/advisories/GHSA-qrmh-qg46-72pp)
- [OWASP A06:2021 Vulnerable and Outdated Components](https://owasp.org/Top10/2021/A06_2021-Vulnerable_and_Outdated_Components/)
- [OWASP A08:2021 Software and Data Integrity Failures](https://owasp.org/Top10/2021/A08_2021-Software_and_Data_Integrity_Failures/)

## Observability and inventory

- [OWASP A09:2021 Security Logging and Monitoring Failures](https://owasp.org/Top10/2021/A09_2021-Security_Logging_and_Monitoring_Failures/)
- [OWASP API9:2023 Improper Inventory Management](https://owasp.org/API-Security/editions/2023/en/0xa9-improper-inventory-management/)

## Insecure design and assurance

- [OWASP A04:2021 Insecure Design](https://owasp.org/Top10/2021/A04_2021-Insecure_Design/)
- [OWASP API6:2023 Unrestricted Access to Sensitive Business Flows](https://owasp.org/API-Security/editions/2023/en/0xa6-unrestricted-access-to-sensitive-business-flows/)
- [How OWASP Helps You Secure Your Full-Stack Web Applications](https://www.smashingmagazine.com/2025/02/how-owasp-helps-secure-full-stack-web-applications/) — secondary discussion of full-stack JavaScript concerns.
- [OWASP Node.js Best Practices Guide](https://www.nodejs-security.com/blog/owasp-nodejs-best-practices-guide) — secondary Node.js-oriented guidance.
- [Best Practices for Security in Next.js](https://blog.openreplay.com/best-practices-for-security-in-nextjs/) — secondary Next.js-oriented guidance.

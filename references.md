# Research References

This catalog records the sources reviewed for the initial draft. Primary sources establish the taxonomy and advisory evidence. Secondary sources were used as practitioner guidance and are not treated as authority for vulnerability classification.

## Citing advisories

Every published GitHub security advisory has a GHSA identifier. A CVE identifier is additional: a maintainer requests one when publishing, so an advisory can be complete, severe, and permanent without ever receiving a CVE. An entry cited as `GHSA-…` therefore says nothing about its severity, exploitability, or how it was disclosed — only that no CVE was assigned, or that none had been assigned when the record was reviewed.

Two rules keep citations predictable:

1. **Identifier.** Cite the CVE if one is assigned, otherwise the GHSA. Never both in the same label — the identifier shown already tells the reader which exists.
2. **URL.** Link to `https://github.com/advisories/GHSA-…` once the advisory is in the GitHub Advisory Database. Until then, link to the maintainer’s repository advisory page, which stays valid afterward.

Advisory records were last reviewed on 2026-08-04. Newly published advisories may gain a CVE identifier and a GitHub Advisory Database entry within days of that date, so `GHSA-…` citations are re-checked each review cycle rather than annotated in place.

The two rules are independent, so an entry can carry a CVE identifier while still linking to a repository advisory page: a CVE is sometimes assigned before the record reaches the Advisory Database. `CVE-2026-66062` is cited that way at present, and its URL moves once the record lands.

A third case is a single weakness carrying two advisory records. Quasar’s `extend()` prototype pollution was reported independently by two researchers and published as [GHSA-3r53-75j5-3g7j](https://github.com/advisories/GHSA-3r53-75j5-3g7j) and [GHSA-qgrf-j65m-5hh8](https://github.com/quasarframework/quasar/security/advisories/GHSA-qgrf-j65m-5hh8) — the same function, the same vulnerable range (`<= 2.21.4`), the same fix (`2.22.0`), and two different reporter-assigned severities (`medium` and `high`). Cite the record that reached the Advisory Database and note the duplicate; do not list both as separate evidence, and do not read the differing severities as a revision, because neither superseded the other.

This catalog does not rank evidence by observed exploitation, and no entry should be read as “exploited” or “not exploited” from its identifier. Where that question matters, consult the [CISA Known Exploited Vulnerabilities catalog](https://www.cisa.gov/known-exploited-vulnerabilities-catalog) and [EPSS](https://www.first.org/epss/), which are maintained for exactly that purpose and change over time. As of 2026-08-04, against KEV catalog version 2026.08.03, two advisories cited in this document appear in the catalog, both noted under `MFR08`: `CVE-2025-55182`, added 2025-12-05, and `CVE-2026-45321`, added 2026-05-27. Both are recorded with known ransomware-campaign use.

## Vendor coordinated release roundups

- [Next.js July 2026 security release](https://nextjs.org/blog/july-2026-security-release) — nine advisories fixed in `15.5.21` and `16.2.11`, reviewed 2026-07-27. Links CVE records only; the corresponding GHSA identifiers were resolved from the GitHub Advisory Database.
- [Nuxt 4.5.1 and 3.21.10 security releases](https://nuxt.com/blog/v4-5-security) — eight advisories fixed in `4.5.1`, `3.21.10`, and `@nuxt/devtools@3.3.1`, reviewed 2026-07-27. Published the same day it was reviewed, so none of the eight had a CVE identifier or a GitHub Advisory Database entry yet.
- [Quasar security advisories, July 2026](https://github.com/quasarframework/quasar/security/advisories) — eleven advisories published between 2026-07-21 and 2026-07-29 against the `quasar` UI package, `@quasar/app-vite`, and Icon Genie, reviewed 2026-08-04. Only `GHSA-3r53-75j5-3g7j` had reached the GitHub Advisory Database at review time, so the others are cited by their repository advisory pages.
- [Next.js security release program](https://nextjs.org/blog/next-security-release-program) — preannounced security releases against Active and Maintenance LTS lines; relevant to patch-management planning under `MFR08`.

Astro is the exception to the roundup pattern: it publishes advisories continuously rather than in coordinated posts. Its [repository advisory list](https://github.com/withastro/astro/security/advisories) held forty records as of 2026-08-04, roughly thirty of them published within the preceding twelve months and spread across the `astro` package and the `@astrojs/node`, `@astrojs/vercel`, `@astrojs/cloudflare`, and `@astrojs/netlify` adapters. Reviewing it therefore needs a date range rather than a post.

## Scope note on frameworks cited

The frameworks cited below are those on the [metaframework comparison](https://metaframe.works/comparison/) that both maintain an active development cadence and have published framework-level advisories. That currently means Next.js, Nuxt, Astro, SvelteKit, React Router, Qwik City, Quasar, TanStack Start, Waku, RedwoodSDK, Analog, and UmiJS.

Three exclusions are deliberate. Documentation-oriented generators on the same list — Docusaurus, VitePress, Observable Framework — have no request-handling server surface and no advisory history, so they contribute nothing to these categories. Vike and SolidStart are actively developed and in scope conceptually, but have no published framework-level advisories to cite; SolidStart’s nearest evidence is [CVE-2025-27109](https://github.com/advisories/GHSA-3qxh-p7jc-5xh6) in Solid itself.

Hono is cited only where a metaframework composes it. By definition, it is a server framework rather than a metaframework, but Astro now ships a composable `astro/hono` pipeline, and that integration has already produced its own advisory ([GHSA-8mv7-9c27-98vc](https://github.com/advisories/GHSA-8mv7-9c27-98vc): `security.checkOrigin` is bypassed when `middleware()` is absent or misordered). Where a substrate’s defect becomes a metaframework application’s defect, it belongs here; Hono’s advisories that only concern its own direct use do not. Analysis for [HonoX](https://github.com/honojs/honox) and similar derivatives is to be done yet.

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
- [CVE-2025-64765: Astro `url.pathname` middleware authorization bypass through URL-encoded path segments](https://github.com/advisories/GHSA-ggxq-hp9w-j794), [CVE-2025-66202](https://github.com/advisories/GHSA-whqg-ppgf-wp8c) — a double-encoding bypass of that fix — and [CVE-2026-59731](https://github.com/advisories/GHSA-vj59-8hwv-xxmv) — a decode-iteration limit combined with a rewrite path-canonicalization mismatch. Three records and one root cause over roughly eight months.
- [CVE-2026-33768: Astro unauthenticated path override through `x-astro-path` in the `@astrojs/vercel` ISR function](https://github.com/advisories/GHSA-mr6q-rp88-fx84) — an authorization-relevant input introduced by the deployment adapter rather than by the application.
- [CVE-2026-27971: Qwik unauthenticated remote code execution through `server$` deserialization](https://github.com/advisories/GHSA-p9x5-jp3h-96mm) — attacker-controlled QRL objects reconstructed from an `application/qwik-json` request resolve an arbitrary module path and symbol.
- [GHSA-9m65-766c-r333: TanStack Start inbound server-function deserialization could invoke a sibling client-referenced server function](https://github.com/advisories/GHSA-9m65-766c-r333)
- [GHSA-8mv7-9c27-98vc: Astro composable `astro/hono` pipeline bypasses `security.checkOrigin` when `middleware()` is absent or misordered](https://github.com/advisories/GHSA-8mv7-9c27-98vc)
- [CVE-2026-22817: Hono JWT middleware algorithm confusion through an unsafe HS256 default](https://github.com/advisories/GHSA-f67f-6cw9-8mq4) — cited for the substrate case described in the scope note above.
- [Ameer Hamza: Your Next.js app is vulnerable. Let’s fix it.](https://medium.com/@hamza97/your-next-js-app-will-be-a-nightmare-for-hackers-after-you-do-this-090f4bf4e315) — secondary guidance on server actions, validation, secrets, and rate limits.

## Data boundaries and client-side exposure

- [CVE-2025-55183: React Server Components server-function source exposure](https://github.com/advisories/GHSA-w37m-7fhw-fmv9)
- [CVE-2025-24360: Nuxt development-server CORS exposure](https://github.com/advisories/GHSA-2452-6xj8-jh47)
- [CVE-2026-64643: Next.js unauthenticated disclosure of Server Action and `use cache` endpoint identifiers](https://github.com/advisories/GHSA-955p-x3mx-jcvp)
- [CVE-2024-56159: Astro server source code exposed to the public when sourcemaps are enabled](https://github.com/advisories/GHSA-49w6-73cw-chjr)
- [GHSA-hgv7-v322-mmgr: SvelteKit `query.batch()` could merge concurrent requests from different users into a single request context](https://github.com/advisories/GHSA-hgv7-v322-mmgr) — cross-user disclosure through a data-loading primitive rather than through serialization of a view model.
- [CVE-2026-59896: `hono/jsx` did not isolate context per request, disclosing one request’s data to another](https://github.com/advisories/GHSA-hvrm-45r6-mjfj) — cited for the substrate case described in the scope note above.
- [OWASP API3:2023 Broken Object Property Level Authorization](https://owasp.org/API-Security/editions/2023/en/0xa3-broken-object-property-level-authorization/)

## Injection and client execution

- [CVE-2025-32388: SvelteKit XSS through tracked search parameters](https://github.com/advisories/GHSA-6q87-84jw-cjhp)
- [CVE-2024-47885: Astro client-router DOM clobbering XSS](https://github.com/advisories/GHSA-m85w-3h95-hcf9)
- [CVE-2025-64764: Astro reflected-XSS research](https://zhero-web-sec.github.io/research-and-things/unlocking-reflected-xss-in-the-astro-framework)
- [CVE-2026-44581: Next.js CSP nonce XSS](https://github.com/advisories/GHSA-ffhc-5mcf-pf4q)
- [GHSA-9473-5f9j-94wq: Nuxt server-island runtime template injection to server-side code execution](https://github.com/nuxt/nuxt/security/advisories/GHSA-9473-5f9j-94wq) — requires `vue.runtimeCompiler`.
- [GHSA-48hr-524c-v5w3: Nuxt unauthorized component instantiation through undeclared island props](https://github.com/nuxt/nuxt/security/advisories/GHSA-48hr-524c-v5w3)
- [CVE-2026-53667: React Router unstable RSC error handler missing redirect-protocol validation](https://github.com/advisories/GHSA-h8fp-f39c-q6mh) — incomplete fix for `CVE-2026-33245`; affects only the unstable RSC APIs.
- [CVE-2026-53668: React Router open redirect leading to XSS](https://github.com/advisories/GHSA-jjmj-jmhj-qwj2)
- [CVE-2026-53666: React Router client-side constructor injection through SSR hydration](https://github.com/advisories/GHSA-337j-9hxr-rhxg) — requires application code that lets attacker input overwrite errors caught during SSR, which the advisory describes as specific and unlikely; affects Framework and Data mode, not Declarative mode.
- [CVE-2026-50146: Astro reflected XSS through an unescaped slot name](https://github.com/advisories/GHSA-8hv8-536x-4wqp)
- [CVE-2026-41067: Astro `define:vars` XSS through incomplete `</script>` sanitization](https://github.com/advisories/GHSA-j687-52p2-xcff) — the guard was case-sensitive and defeated by whitespace variants.
- [GHSA-pq96-jpmf-w254: Quasar stored and reflected XSS through unescaped SSR meta-tag rendering in `getHead()`](https://github.com/quasarframework/quasar/security/advisories/GHSA-pq96-jpmf-w254) — the sink is the `useMeta()` composable, the documented way an application sets its title and meta tags.
- [CVE-2026-25148: Qwik SSR XSS through unsafe virtual-node serialization](https://github.com/advisories/GHSA-m6jq-g7gq-5w3c)
- [zhero: Astro framework and standards weaponization](https://zhero-web-sec.github.io/research-and-things/astro-framework-and-standards-weaponization) — the research behind `CVE-2025-64525`, showing standard forwarding headers combined with URL-parser behavior escalating from middleware bypass to SSRF and stored XSS.

## SSRF and origin trust

- [CVE-2024-34351: Next.js Server Actions SSRF](https://github.com/advisories/GHSA-fr5h-rqp8-mj6g)
- [CVE-2024-42352: Nuxt Icon SSRF](https://github.com/advisories/GHSA-cxgv-px37-4mp2)
- [CVE-2025-64525: Astro forwarded-header URL manipulation](https://github.com/advisories/GHSA-hr2q-hp5q-x767)
- [CVE-2025-67647: SvelteKit prerendering SSRF and DoS](https://github.com/advisories/GHSA-j62c-4x62-9r35)
- [CVE-2026-64645: Next.js SSRF and open redirect through an attacker-controlled rewrite/redirect destination hostname](https://github.com/advisories/GHSA-p9j2-gv94-2wf4)
- [CVE-2026-64649: Next.js Server Actions SSRF on custom servers through Host-associated headers](https://github.com/advisories/GHSA-89xv-2m56-2m9x)
- [CVE-2026-53669: React Router external redirect through untrusted paths passed to navigation](https://github.com/advisories/GHSA-wrjc-x8rr-h8h6) — incomplete fix for `CVE-2025-68470`.
- [GHSA-qwww-vcr4-c8h2: React Router unstable RSC CSRF bypass executing an action before the rejecting response](https://github.com/advisories/GHSA-qwww-vcr4-c8h2) — incomplete fix for `CVE-2026-22030`; affects only the unstable RSC APIs.
- [GHSA-q7p4-cm8g-969j: Analog SSRF through API-prefix stripping in generated Nitro middleware](https://github.com/analogjs/analog/security/advisories/GHSA-q7p4-cm8g-969j) — `startsWith(apiPrefix)` and `replace(apiPrefix, '')` enforce no path boundary, so a request path formed by concatenating the `/api` prefix with an absolute URL — scheme, internal host, and target path, with no separator — passes the prefix check and, once stripped, is that absolute URL, which is passed to `$fetch` or `proxyRequest`. The vulnerable code is generated by the adapter, not written by the application.
- [CVE-2026-25545: Astro full-read SSRF in error rendering through `Host` header injection](https://github.com/advisories/GHSA-qq67-mvv5-fw3g) and [CVE-2026-54299: Host header SSRF in the prerendered error page fetch](https://github.com/advisories/GHSA-2pvr-wf23-7pc7)
- [CVE-2026-49455: Waku cross-origin CSRF on RSC Server Action dispatch](https://github.com/advisories/GHSA-75w3-gmqx-993q) and [CVE-2026-49456: open redirect through the `unstable_redirect` helper](https://github.com/advisories/GHSA-43fc-v873-qw85)
- [CVE-2026-39371: RedwoodSDK CSRF through server-function dispatch over GET](https://github.com/advisories/GHSA-x8rx-789c-2pxq) and [CVE-2026-42190: same-site CSRF through missing origin validation in server actions](https://github.com/advisories/GHSA-m2m6-cff5-3w7c) — both of RedwoodSDK’s published advisories are this root cause.
- [CVE-2026-25151: Qwik City CSRF protection bypass through Content-Type validation](https://github.com/advisories/GHSA-r666-8gjf-4v5f) and [CVE-2026-25155: the same protection defeated by a Content-Type parameter such as `multipart/form-data`](https://github.com/advisories/GHSA-vm6g-8r4h-22x8)
- [OWASP API7:2023 Server Side Request Forgery](https://owasp.org/API-Security/editions/2023/en/0xa7-server-side-request-forgery/)

## Routing, rendering, and caching

- [zhero: Next.js and the corrupt middleware](https://zhero-web-sec.github.io/research-and-things/nextjs-and-the-corrupt-middleware)
- [zhero: Next.js, cache, and chains: the stale elixir](https://zhero-web-sec.github.io/research-and-things/nextjs-cache-and-chains-the-stale-elixir)
- [zhero: Eclipse on Next.js](https://zhero-web-sec.github.io/research-and-things/eclipse-on-nextjs-conditioned-exploitation-of-an-intended-race-condition)
- [zhero: Nuxt, show me your payload](https://zhero-web-sec.github.io/research-and-things/nuxt-show-me-your-payload)
- [zhero: React Router and the Remix’ed path](https://zhero-web-sec.github.io/research-and-things/react-router-and-the-remixed-path)
- [zhero: Pre-render data spoofing and CPDoS on React Router](https://zhero-web-sec.github.io/research-and-things/pre-render-data-spoofing-and-cpdos-on-react-router) — the research behind `CVE-2025-43865` and `CVE-2025-43864`.
- [zhero: Re:CACHE — excessive reflection, type confusion, and 0-click SXSS on Next.js](https://zhero-web-sec.github.io/research-and-things/re-cache-excessive-reflection-type-confusion-and-0-click-sxss-on-nextjs)
- [zhero: Next.js cache poisoning to DoS through a 204 response](https://zhero-web-sec.github.io/research-and-things/nextjs-cache-poisoning-to-dos-via-a-204-response) — `CVE-2025-49826`.
- [CVE-2026-41322: Astro cache poisoning through incorrect handling of a malformed `if-match` header](https://github.com/advisories/GHSA-c57f-mm3j-27q9)
- [CVE-2026-27118: SvelteKit cache poisoning in `@sveltejs/adapter-vercel`](https://github.com/advisories/GHSA-9pq4-5hcf-288c) — the adapter, not the framework router, decided what was cacheable.
- [CVE-2026-44457: Hono cache middleware ignored `Vary: Authorization` and `Vary: Cookie`, leaking responses across users](https://github.com/advisories/GHSA-p77w-8qqv-26rm) — cited for the substrate case described in the scope note above.
- [CVE-2025-43865: React Router pre-render data spoofing](https://github.com/advisories/GHSA-cpj6-fhp6-mr6j) and [CVE-2025-31137: URL manipulation through `Host` and `X-Forwarded-Host`](https://github.com/advisories/GHSA-4q56-crqp-v477)
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
- [CVE-2026-55685: React Router unauthenticated denial of service against the `__manifest` endpoint](https://github.com/advisories/GHSA-chx6-hx7r-mcp5) — incomplete fix for `CVE-2026-42342`; affects only Framework mode.
- [CVE-2026-66062: SvelteKit ReDoS in `Accept` header content negotiation](https://github.com/sveltejs/kit/security/advisories/GHSA-29g2-3rmr-qm68) — mitigated where the platform imposes a header-length limit, exploitable where that limit is raised or absent.
- SvelteKit remote functions, five advisories against one deserializer over six months: [CVE-2026-22803](https://github.com/advisories/GHSA-j2f3-wq62-6q46) (memory amplification — a small payload declares a large length, then stalls, and the buffer is allocated eagerly), [GHSA-88qp-p4qg-rqm6](https://github.com/advisories/GHSA-88qp-p4qg-rqm6) (CPU exhaustion), [GHSA-vrhm-gvg7-fpcf](https://github.com/advisories/GHSA-vrhm-gvg7-fpcf) (memory exhaustion), [GHSA-fpg4-jhqr-589c](https://github.com/advisories/GHSA-fpg4-jhqr-589c) (deserialization expansion), and [GHSA-wqjv-9729-c5q2](https://github.com/advisories/GHSA-wqjv-9729-c5q2) (large payloads crashing the Node process). A new request-body format is a new resource-limit surface.
- [CVE-2026-40073: SvelteKit `BODY_SIZE_LIMIT` bypass in `@sveltejs/adapter-node`](https://github.com/advisories/GHSA-2crg-3p73-43xp)
- [CVE-2026-29772: Astro missing request-body size limit in Server Islands](https://github.com/advisories/GHSA-3rmj-9m5h-8fpv) and [CVE-2026-27729: the same omission in Server Actions](https://github.com/advisories/GHSA-jm64-8m5q-4qh8) — two transports, one missing limit, patched in the same adapter release.
- [GHSA-68jq-fhch-4xq4: Quasar SSR super-linear regex backtracking on `User-Agent`](https://github.com/quasarframework/quasar/security/advisories/GHSA-68jq-fhch-4xq4) — the auto-installed `Platform` plugin parses the raw header on every render; the advisory measures an 8 KB header blocking the event loop for about 4.4 seconds and a 16 KB header for about 35.
- [CVE-2026-32701: Qwik City array-method pollution in FormData processing, allowing type confusion and denial of service](https://github.com/advisories/GHSA-whhv-gg5v-864r)
- [CVE-2026-34077: React Router denial of service through reflected user input in single-fetch](https://github.com/advisories/GHSA-rxv8-25v2-qmq8)
- [zhero: Avoiding the paradox — a native full-read SSRF and one-shot DoS in SvelteKit](https://zhero-web-sec.github.io/research-and-things/avoiding-the-paradox-a-native-full-read-ssrf-and-oneshot-dos-in-sveltekit) — the research behind `CVE-2025-67647`.
- [OWASP API4:2023 Unrestricted Resource Consumption](https://owasp.org/API-Security/editions/2023/en/0xa4-unrestricted-resource-consumption/)

## Configuration and development surfaces

- [CVE-2024-23657: Nuxt Devtools traversal and cross-site WebSocket exposure](https://github.com/advisories/GHSA-rcvg-rgf7-pppv)
- [CVE-2024-34344: Nuxt test-mode code execution](https://github.com/advisories/GHSA-v784-fjjh-f8r4)
- [GHSA-279x-mwfv-vcqv: unauthenticated Nuxt DevTools RPC allowing arbitrary command execution on a developer host](https://github.com/nuxt/nuxt/security/advisories/GHSA-279x-mwfv-vcqv) — fixed in `@nuxt/devtools@3.3.1`.
- [GHSA-7c4v-fwgw-9rf7: Nuxt development-server path and workspace disclosure through a header-based locality check](https://github.com/nuxt/nuxt/security/advisories/GHSA-7c4v-fwgw-9rf7)
- [CVE-2025-64757: Astro development server arbitrary local file read](https://github.com/advisories/GHSA-x3h8-62x9-952g) and [CVE-2025-64745: reflected XSS on the Astro development error page](https://github.com/advisories/GHSA-w2vj-39qv-7vh7)
- [GHSA-r5mf-4r5x-q78f: Quasar development SSR/SSG error page discloses the entire process environment](https://github.com/quasarframework/quasar/security/advisories/GHSA-r5mf-4r5x-q78f) — every `process.env` variable, request header, and cookie is serialized into the response, and the development server binds `0.0.0.0` by default, so one unauthenticated `GET` returns the developer’s cloud keys, registry tokens, and database URLs. The `</script>` guard is ASCII-case-sensitive and requires a literal `>`, so `</SCRIPT>`, `</script >`, and `</script/>` all escape the element.
- [GHSA-fh39-c73x-5pjv: Quasar development TLS private keys cached with overly permissive filesystem permissions](https://github.com/quasarframework/quasar/security/advisories/GHSA-fh39-c73x-5pjv)
- [CVE-2026-16492: UmiJS OS command injection in the Git file helper](https://github.com/advisories/GHSA-g3hq-vgww-mrhj) — a build-time surface reached through repository metadata rather than an HTTP request.
- [OWASP A05:2021 Security Misconfiguration](https://owasp.org/Top10/2021/A05_2021-Security_Misconfiguration/)

## Supply chain and runtime integrity

- [CVE-2025-55182: React Server Components RCE](https://github.com/advisories/GHSA-9qr9-h5gf-34mp)
- [CVE-2025-59143: `color` npm account takeover malware](https://github.com/advisories/GHSA-qrmh-qg46-72pp)
- [GHSA-hxvh-4h3w-prp9: incomplete fix for CVE-2026-53721](https://github.com/nuxt/nuxt/security/advisories/GHSA-hxvh-4h3w-prp9) — cited here as evidence that a patched version string is not evidence of a closed weakness.
- [React Router 2026-07-22 coordinated release](https://github.com/remix-run/react-router/security/advisories) — of six advisories, four were published as follow-ups to earlier fixes that proved incomplete: [CVE-2026-53669](https://github.com/advisories/GHSA-wrjc-x8rr-h8h6), [CVE-2026-55685](https://github.com/advisories/GHSA-chx6-hx7r-mcp5), [CVE-2026-53667](https://github.com/advisories/GHSA-h8fp-f39c-q6mh), and [GHSA-qwww-vcr4-c8h2](https://github.com/advisories/GHSA-qwww-vcr4-c8h2). Cited here for the release-level pattern rather than any individual weakness; reviewed 2026-08-04.
- [CVE-2026-45321: malware in 42 `@tanstack/*` packages exfiltrating cloud credentials, GitHub tokens, and SSH keys](https://github.com/advisories/GHSA-g7cv-rxg3-hmpx) — a metaframework’s own publishing pipeline compromised, rather than a leaf dependency of one.
- [CVE-2026-42211: React Router unauthenticated remote code execution through arbitrary constructor invocation in vendored `turbo-stream` v2 `TYPE_ERROR` deserialization](https://github.com/advisories/GHSA-49rj-9fvp-4h2h) — a vendored copy of a serialization library, so the application’s dependency inventory does not name the vulnerable component.
- [GHSA-j47w-4mr3-8gq6: arbitrary code execution in Astro’s Validate Changesets workflow](https://github.com/withastro/astro/security/advisories/GHSA-j47w-4mr3-8gq6) and [GHSA-gr7v-jghp-mwvf: code injection in Waku’s canary CI workflow through an issue comment](https://github.com/wakujs/waku/security/advisories/GHSA-gr7v-jghp-mwvf) — the framework’s own CI is an upstream build input for every application that installs a release built by it.
- [GHSA-f8wh-5425-35vx: Quasar Icon Genie installs vulnerable image-processing dependencies](https://github.com/quasarframework/quasar/security/advisories/GHSA-f8wh-5425-35vx) and [GHSA-q9mq-245r-4g93: `@quasar/app-vite` build cleanup can recursively remove unsafely configured output directories](https://github.com/quasarframework/quasar/security/advisories/GHSA-q9mq-245r-4g93)
- [OWASP A06:2021 Vulnerable and Outdated Components](https://owasp.org/Top10/2021/A06_2021-Vulnerable_and_Outdated_Components/)
- [OWASP A08:2021 Software and Data Integrity Failures](https://owasp.org/Top10/2021/A08_2021-Software_and_Data_Integrity_Failures/)

## Observability and inventory

- [CVE-2026-64643: Next.js Server Function endpoint disclosure, documented as reconnaissance for a broader attack chain](https://github.com/advisories/GHSA-955p-x3mx-jcvp)
- [GHSA-hxcr-hm88-mpq6: Nuxt island endpoint identifiers are predictable, non-secret digests](https://github.com/nuxt/nuxt/security/advisories/GHSA-hxcr-hm88-mpq6) — cited here for endpoint reachability, not for its denial-of-service impact.
- [GHSA-q7p4-cm8g-969j: the vulnerable Analog middleware is generated by `@analogjs/vite-plugin-nitro`](https://github.com/analogjs/analog/security/advisories/GHSA-q7p4-cm8g-969j) — cited here because an inventory derived from application source will not contain it. Adapter- and plugin-generated request handlers must be enumerated from build output.
- [GHSA-9m65-766c-r333: a TanStack Start server function was reachable through another function’s client reference](https://github.com/advisories/GHSA-9m65-766c-r333) — cited here because the reachable set of server functions was larger than the set the application exposed deliberately.
- [OWASP A09:2021 Security Logging and Monitoring Failures](https://owasp.org/Top10/2021/A09_2021-Security_Logging_and_Monitoring_Failures/)
- [OWASP API9:2023 Improper Inventory Management](https://owasp.org/API-Security/editions/2023/en/0xa9-improper-inventory-management/)

## Insecure design and assurance

Four frameworks with independent implementations published advisories in which a request-borne payload was deserialized into an invocation target: [CVE-2026-27971](https://github.com/advisories/GHSA-p9x5-jp3h-96mm) (Qwik `server$`, unauthenticated remote code execution), [GHSA-9m65-766c-r333](https://github.com/advisories/GHSA-9m65-766c-r333) (TanStack Start, a sibling server function), [GHSA-9473-5f9j-94wq](https://github.com/nuxt/nuxt/security/advisories/GHSA-9473-5f9j-94wq) (Nuxt server islands, a compiled `template` prop), and [CVE-2026-42211](https://github.com/advisories/GHSA-49rj-9fvp-4h2h) (React Router, constructor invocation through a vendored deserializer). Cited together as design evidence: the ergonomics of calling a server function as though it were a local one recur across framework families, and so does the failure to treat its wire format as an untrusted parsing boundary.

- [OWASP A04:2021 Insecure Design](https://owasp.org/Top10/2021/A04_2021-Insecure_Design/)
- [OWASP API6:2023 Unrestricted Access to Sensitive Business Flows](https://owasp.org/API-Security/editions/2023/en/0xa6-unrestricted-access-to-sensitive-business-flows/)
- [How OWASP Helps You Secure Your Full-Stack Web Applications](https://www.smashingmagazine.com/2025/02/how-owasp-helps-secure-full-stack-web-applications/) — secondary discussion of full-stack JavaScript concerns.
- [OWASP Node.js Best Practices Guide](https://www.nodejs-security.com/blog/owasp-nodejs-best-practices-guide) — secondary Node.js-oriented guidance.
- [Best Practices for Security in Next.js](https://blog.openreplay.com/best-practices-for-security-in-nextjs/) — secondary Next.js-oriented guidance.

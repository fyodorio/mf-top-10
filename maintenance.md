# Maintenance

This document covers the recurring work that keeps the evidence base accurate between releases. It is the operational companion to the [roadmap](roadmap.md), which describes what the project is building, and to the [contribution guidance](contributing.md), which describes how proposals are made and reviewed.

Two properties of the evidence base need ongoing attention. Advisory records change after publication — identifiers are assigned, records propagate between databases, and exploitation status becomes known. Links rot. Neither is visible by reading the documents.

## The check script

`scripts/check-advisories.py` reports on all three. It reads every Markdown file, needs only the Python standard library, and changes nothing.

```bash
python3 scripts/check-advisories.py          # identifiers and KEV
python3 scripts/check-advisories.py --links  # add the link check
python3 scripts/check-advisories.py --all    # add EPSS scores as well
```

Set `GITHUB_TOKEN` to raise the GitHub API rate limit from 60 to 5000 requests per hour. The script exits non-zero when a citation needs updating or a link is broken, so it can run in CI, though nothing about the workflow requires that.

### identifiers

Lists every advisory cited by its maintainer-hosted repository URL and reports whether it has since reached the GitHub Advisory Database. When one has, the citation should move to `https://github.com/advisories/GHSA-…`, and its label should become the CVE identifier if one was assigned. The script prints both substitutions. See [citing advisories](references.md#citing-advisories) for the rules and why a missing CVE identifier is not a judgement about severity.

This is the only check whose output is a definite action.

### kev

Reports which cited CVE identifiers appear in the [CISA Known Exploited Vulnerabilities catalog](https://www.cisa.gov/known-exploited-vulnerabilities-catalog), with the date added and whether ransomware use is known. A new entry is worth a sentence in the relevant risk page, as `MFR08` carries for `CVE-2025-55182`. Date any such claim, because catalog membership is a point-in-time fact.

Do not annotate the evidence lists wholesale with exploitation status. It changes independently of anything in this repository, and duplicating it across ten risk pages guarantees that some copies will be wrong.

### epss

Reports [EPSS](https://www.first.org/epss/) scores, highest first. Scores move daily, so treat them as orientation when deciding which categories deserve deeper treatment — never as content to copy into a document. Recently published advisories are usually unscored.

### links

Reports the HTTP status of every external URL. Two results need judgement rather than action:

- `401`, `403`, and `429` usually mean bot protection or rate limiting. The script says so and does not fail the run; open the URL in a browser to confirm. The one secondary source hosted on Medium reliably answers `403`.
- A `404` on a page published within the last day or so is often a vendor deployment or CDN problem rather than a wrong URL. Confirm the canonical address against the vendor's RSS feed, changelog, or advisory record before editing a citation. Vendor sites have served `404` for a valid, freshly published post.

Verify a replacement URL before substituting it. A citation pointing at a temporarily unavailable canonical page is better than one pointing at a stable wrong page.

## Cadence

Monthly, or after any framework security release the project intends to cite:

1. Run the script with `--links`.
2. Apply the identifier substitutions it reports.
3. Review new advisories from the frameworks in scope against the existing categories. Most belong in [references](references.md); promote one into a risk page only when it demonstrates a root cause the page does not yet evidence.
4. Note any new KEV entry in the relevant risk page, with its date.
5. Update the review date in the [citing advisories](references.md#citing-advisories) section.

Per release cycle, additionally:

1. Re-read the risk pages for evidence that has become redundant. Advisory lists are representative, not exhaustive; an entry that no longer illustrates anything the page does not already establish should be moved to the references catalog.
2. Confirm CWE mappings still match the evidence cited beneath them.
3. Record what was reviewed and what changed, per the release criteria in the [roadmap](roadmap.md).

## Sources to watch

Framework security channels, for advisories in scope:

- [Next.js blog](https://nextjs.org/blog) and its [security release program](https://nextjs.org/blog/next-security-release-program)
- [Nuxt blog](https://nuxt.com/blog) and [`nuxt/nuxt` advisories](https://github.com/nuxt/nuxt/security/advisories)
- [Astro](https://github.com/withastro/astro/security/advisories), [SvelteKit](https://github.com/sveltejs/kit/security/advisories), [React Router](https://github.com/remix-run/react-router/security/advisories), [TanStack Start](https://github.com/TanStack/router/security/advisories), [SolidStart](https://github.com/solidjs/solid-start/security/advisories)
- [Qwik](https://github.com/QwikDev/qwik/security/advisories), [Quasar](https://github.com/quasarframework/quasar/security/advisories), [Waku](https://github.com/wakujs/waku/security/advisories), [Analog](https://github.com/analogjs/analog/security/advisories), [RedwoodSDK](https://github.com/redwoodjs/sdk/security/advisories), [UmiJS](https://github.com/umijs/umi/security/advisories), [Vike](https://github.com/vikejs/vike/security/advisories), [Fresh](https://github.com/freshframework/fresh/security/advisories)
- [GitHub Advisory Database](https://github.com/advisories) and the [CVE Program](https://www.cve.org)

A vendor roundup post is worth citing alongside the individual advisories when it explains the relationship between several fixes. Record the date it was reviewed, since these posts are edited after publication.

Watch the repository advisory lists directly, not only the GitHub Advisory Database. Quasar’s eleven July 2026 advisories reached the database as one record; Analog’s single critical SSRF advisory had not reached it at all. A framework whose advisories are mostly repository-hosted looks quiet from the database alone.

Two sweep hazards are worth stating once. Frameworks publish on very different rhythms — Next.js, Nuxt, and Quasar in coordinated roundups; Astro continuously; most of the smaller frameworks sporadically — so a monthly sweep needs a date range per source rather than a “since the last post” check. And package-name matching mismatches framework names: `fresh` on npm is the Express HTTP-freshness library rather than Deno’s Fresh, `@builder.io/qwik-city` and `@qwik.dev/router` are the same framework across a rename, and React Router advisories are filed against `react-router`, `@remix-run/*`, and `@react-router/*` interchangeably. Confirm which project an advisory concerns before citing it.

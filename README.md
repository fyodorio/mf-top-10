# Top 10 Metaframework Security Risks

## Summary

[This project](index.md) develops a focused, evidence-backed awareness document for the security risks introduced or amplified when JavaScript and TypeScript [metaframeworks](https://metaframe.works/comparison/) combine routing, rendering, data access, server capabilities, build tooling, caching, and deployment adapters.

## Why this work exists

General [web](https://owasp.org/www-project-top-ten/), [API](https://owasp.org/API-Security/), and [client-side](https://owasp.org/www-project-top-10-client-side-security-risks/) security guidance is essential, but it does not organize the shared trust-boundary failures of frameworks such as [Next.js](https://nextjs.org), [Nuxt](https://nuxt.com), [Astro](https://astro.build), [SvelteKit](https://svelte.dev/docs/kit/introduction), [Remix](https://remix.run), [TanStack Start](https://tanstack.com/start/latest), and [SolidStart](https://start.solidjs.com) in one place. Their convenience features can turn a page into an API, a component into a server capability, or an internal transport into a public request variant.

The project identifies those patterns, connects them to established weakness taxonomies and published advisories, and provides prevention and verification guidance that teams can apply throughout design, development, deployment, and operations.

## Purpose and deliverables

The project will deliver:

- a maintained, prioritized [Top 10 awareness taxonomy](index.md#the-top-10);
- a detailed risk page for each category, including CWE mappings and representative evidence;
- practical prevention and verification guidance for full-stack metaframework applications;
- a transparent evidence and data-collection method for future revisions;
- versioned documentation releases and an open research reference catalog.

This is an awareness document and a starting point for a risk-based application security program — not a complete security standard or a replacement for framework-specific guidance. Teams should use it with explicit risk assessment, reusable security controls, threat modeling, secure design and code review, continuous testing, and operational metrics.

The first year focuses on establishing the taxonomy and evidence model, validating both with practitioners, and publishing a versioned revision. See the [detailed roadmap](roadmap.md).

## Read and participate

- [Read the detailed index and Top 10](index.md)
- [View the project roadmap](roadmap.md)
- [Contribute research or improvements](contributing.md)
- [Review research references](references.md)
- [Maintain the evidence base](maintenance.md)
- [License: CC BY-SA 4.0](LICENSE)

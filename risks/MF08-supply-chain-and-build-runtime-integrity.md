# MF08: Supply-Chain and Build/Runtime Integrity Failures

## Factors

- **Exploitability:** Average
- **Prevalence:** Common
- **Detectability:** Difficult
- **Technical impact:** Severe

## Description

The application accepts a compromised, vulnerable, substituted, or unexpectedly transformed component, build input, artifact, deployment, or runtime payload. JavaScript metaframework applications have a particularly broad supply chain: package manager, transitive dependencies, plugins, compiler and bundler, framework server runtime, generated artifacts, deployment adapters, remote content, and browser-side third-party scripts.

The category covers both known vulnerable components and integrity failures. “A trivial package” is a useful review signal, but dependency count alone is not a vulnerability; the question is whether a component’s authority, provenance, maintenance, and update path are appropriate.

## Metaframework-specific failure modes

- Unpatched framework, React/Vue/Svelte runtime, adapter, bundler, image optimizer, plugin, or transitive dependency.
- Compromised npm maintainer account, typosquatted or abandoned package, malicious install script, or lockfile drift.
- Build/deploy pipeline artifacts not pinned, verified, reviewed, or reproducible.
- Third-party browser scripts granted same-origin access without origin control, CSP, SRI where applicable, or runtime change monitoring.
- Deserialization or component-protocol defects in an upstream framework runtime.

## Prevention and verification priorities

1. Maintain an SBOM and lockfiles; pin and regularly update frameworks, adapters, runtimes, and transitive dependencies.
2. Run SCA/advisory checks in CI and production inventory; triage exploitability rather than blindly suppressing or upgrading.
3. Minimize dependencies with privileged build/runtime access; assess maintainer health, provenance, install hooks, and required permissions.
4. Protect package publishing and CI with MFA, least privilege, short-lived credentials, branch protection, artifact provenance, and deployment approval.
5. Restrict third-party client code with CSP, origin allowlists, SRI where a stable external asset is used, and change monitoring.

## Relevant CWEs

- [CWE-829: Inclusion of Functionality from Untrusted Control Sphere](https://cwe.mitre.org/data/definitions/829.html)
- [CWE-1104: Use of Unmaintained Third Party Components](https://cwe.mitre.org/data/definitions/1104.html)
- [CWE-494: Download of Code Without Integrity Check](https://cwe.mitre.org/data/definitions/494.html)
- [CWE-502: Deserialization of Untrusted Data](https://cwe.mitre.org/data/definitions/502.html)
- [CWE-506: Embedded Malicious Code](https://cwe.mitre.org/data/definitions/506.html)

## Representative evidence

- [CVE-2025-55182](https://github.com/advisories/GHSA-9qr9-h5gf-34mp): a critical React Server Components deserialization issue affected frameworks including Next.js App Router deployments.
- [CVE-2025-59143](https://github.com/advisories/GHSA-qrmh-qg46-72pp): an npm account takeover introduced malware into `color@5.0.1`, affecting browser bundles built by common JavaScript tooling.
- [CVE-2024-47885](https://github.com/advisories/GHSA-m85w-3h95-hcf9): an Astro client-router defect illustrates that a framework runtime is part of the application’s attack surface.

## Sources

- [OWASP A06:2021 Vulnerable and Outdated Components](https://owasp.org/Top10/2021/A06_2021-Vulnerable_and_Outdated_Components/)
- [OWASP A08:2021 Software and Data Integrity Failures](https://owasp.org/Top10/2021/A08_2021-Software_and_Data_Integrity_Failures/)
- [Research references](../references.md#supply-chain-and-runtime-integrity)

# Contributing

Contributions are welcome from developers, security researchers, framework maintainers, application-security practitioners, platform operators, technical writers, and reviewers. The goal is a clear, useful, and evidence-led awareness document.

## Useful contributions

- Correct factual errors, broken links, CWE/CVE mappings, terminology, or outdated framework guidance.
- Add well-sourced framework-specific evidence that supports or refines a category.
- Improve category boundaries, prevention guidance, verification steps, and cross-framework applicability.
- Propose concise attack scenarios that demonstrate a reusable application-level failure mode.
- Improve accessibility, clarity, grammar, link maintenance, and release documentation.
- Share anonymized, reproducible assessment data that follows the evidence requirements in the [roadmap](roadmap.md).

## Evidence standards

Use primary sources whenever possible: vendor security advisories, CVE/GHSA records, framework documentation, standards, official release notes, reproducible test cases, or peer-reviewed research. Clearly identify secondary sources as commentary or practitioner guidance.

For a proposed advisory example, include:

1. a stable primary-source URL;
2. the affected framework/package, version range, and relevant deployment or feature preconditions;
3. the proposed `MFR` category and relevant CWE mapping;
4. a short explanation of the reusable root cause; and
5. why the evidence belongs in this category instead of, or in addition to, another one.

### Advisory identifiers

Cite the CVE identifier if one is assigned, otherwise the GHSA identifier — one identifier per label, never both. Link to `https://github.com/advisories/GHSA-…` once the advisory is in the GitHub Advisory Database, and to the maintainer’s repository advisory page until then; the repository URL remains valid afterward.

A missing CVE identifier is an administrative state, not a property of the vulnerability. Maintainers request CVEs per advisory, and some decline to for lower-severity or development-only issues, so an advisory can be permanent, severe, and thoroughly documented without one. Do not label evidence as more or less serious, more or less exploited, or more or less responsibly disclosed based on which identifier it carries.

Nor should the evidence lists be annotated with exploitation status. Whether a weakness is being exploited changes after publication and is tracked authoritatively elsewhere — the [CISA Known Exploited Vulnerabilities catalog](https://www.cisa.gov/known-exploited-vulnerabilities-catalog) for confirmed exploitation and [EPSS](https://www.first.org/epss/) for probability. Cite either only where it changes what a reader should do, as `MFR08` does for `CVE-2025-55182`, and date the claim.

Because these states change without any edit to this repository, they are re-checked on a schedule rather than tracked in prose. `scripts/check-advisories.py` reports citations that need updating, new KEV entries, and broken links; the [maintenance guide](maintenance.md) explains each check and the cadence.

Do not submit customer data, secrets, private vulnerability reports, exploit payloads, or instructions that could harm a live system. Use responsible disclosure channels for unpatched vulnerabilities.

## Scope and category changes

The project focuses on risks introduced or amplified by full-stack JavaScript/TypeScript metaframework architecture. A proposal should identify a durable, reusable root cause — not only a framework feature, a single code smell, a development preference, or one CVE.

New categories need evidence that the existing taxonomy cannot represent the problem clearly. Changes to ordering, labels, or factor assessments should explain the reasoning, affected mappings, and expected impact on readers.

## Contribution workflow

1. Read the [index](index.md), relevant risk pages, [roadmap](roadmap.md), and [references](references.md).
2. Open an issue or discussion for significant taxonomy, methodology, or roadmap changes before drafting a large pull request.
3. Keep a pull request focused. Cite sources inline and update the references catalog when adding material evidence.
4. Explain what changed, why it matters, and any assumptions, limitations, or unresolved questions.
5. Verify local Markdown links and headings before requesting review, and run `python3 scripts/check-advisories.py --links` when the change adds or edits a citation. Read the [maintenance guide](maintenance.md) first: some reported statuses need judgement rather than an edit.

Reviews focus on accuracy, scope fit, source quality, clarity, reproducibility, licensing, and whether the proposed change improves practical security outcomes.

## Developer Certificate of Origin

Contributions must be the contributor’s original work or work they are authorized to submit. Sign every commit with the [Developer Certificate of Origin (DCO)](https://github.com/apps/dco) sign-off:

`git commit -s -m "Describe the change"`

The sign-off certifies that the contribution may be distributed under this repository’s license. Project maintainers may ask for clarification, provenance, or license information before accepting a contribution.

## License

Documentation in this repository is licensed under [Creative Commons Attribution-ShareAlike 4.0 International](LICENSE). By contributing, you agree that your contribution is available under the same license.

## Respectful collaboration

Discuss technical claims in good faith, welcome correction, credit original research, and protect reporters and affected users. Keep project discussions focused on improving the documentation and its evidence base.

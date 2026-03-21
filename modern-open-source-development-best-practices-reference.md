# Modern Open Source Development Best Practices Reference

## Purpose

This document summarizes recent authoritative guidance on modern open source development practice. It is intended as a reference for course and textbook design, not as part of the textbook chapter sequence.

## Core Conclusion

Modern open source development has moved beyond the older model of “public repository + informal review + occasional release.” Current best practice emphasizes:

- repository governance by default
- pull-request-based change control
- automated quality and security gates
- supply chain integrity and provenance
- structured community health
- least-privilege automation

In short: modern open source development is now a governed engineering system, not just open code hosting.

## Key Practice Areas

### 1. Treat the repository as a governed collaboration system

Healthy projects should maintain at least:

- `README`
- `LICENSE`
- `CONTRIBUTING.md`
- `CODE_OF_CONDUCT.md`
- `SECURITY.md`
- issue and pull request templates

These are no longer optional niceties; they are baseline governance and contributor guidance.

### 2. Separate community discussion from executable work

Use Discussions for questions, design discussion, and announcements. Use Issues for actionable work items. This reduces noise and improves contributor onboarding.

### 3. Require pull-request gates for all changes

Modern repositories should avoid direct pushes to the default branch. Use branch protection or rulesets, required checks, and `CODEOWNERS` review for critical areas.

### 4. Shift security left into the pull request

Security review should happen before merge, not after release. Recommended practices include:

- dependency review
- secret scanning
- push protection
- code scanning
- vulnerability alerts

### 5. Expand CI beyond “run tests”

Continuous integration should enforce project policy, not just run unit tests. CI may include:

- build verification
- linting
- tests
- dependency review
- static analysis
- code quality gates

### 6. Apply least privilege to automation

GitHub Actions and similar systems should run with restricted permissions by default. Fork-based contributions should not receive secrets or elevated token access without explicit approval.

### 7. Make releases verifiable

Modern open source release practice increasingly includes:

- SBOM generation
- provenance or artifact attestations
- verifiable build and release identity

### 8. Use established external baselines

Projects should prefer recognized frameworks rather than inventing ad hoc quality and security rules. Two especially relevant references are:

- OpenSSF OSPS Baseline
- OpenSSF Scorecard

Projects should also rely on mature practices for compliance, licensing metadata, community health, and release communication:

- OpenChain for open source compliance process
- REUSE and SPDX for license and copyright metadata
- CHAOSS for community health understanding
- Semantic Versioning and Keep a Changelog for release discipline

### 9. Standardize maintainer workflows

Maintainer effort should be reduced by automation and explicit policy:

- templates
- labels
- triage conventions
- review ownership
- clear contribution pathways

### 10. Retire outdated patterns

Practices that are no longer sufficient on their own include:

- direct pushes to the main branch
- no `SECURITY.md`
- release-only testing
- purely manual dependency review
- high-permission workflows on untrusted pull requests
- shipping release artifacts without SBOM or provenance
- using Issues for all community interaction

## Why This Matters for This Project

For this repository, the implication is not that the textbook should become a GitHub product manual. Instead, it should teach durable open source concepts while reflecting the modern reality that open source work now depends on:

- governance files
- pull-request gates
- tests and CI
- code review ownership
- supply chain security
- documented contributor pathways

These are part of contemporary open source development technique, not optional advanced topics.

## Reference Sources

### GitHub documentation

- About community profiles for public repositories  
  https://docs.github.com/en/communities/setting-up-your-project-for-healthy-contributions/about-community-profiles-for-public-repositories?apiVersion=2022-11-28
- Setting guidelines for repository contributors  
  https://docs.github.com/en/communities/setting-up-your-project-for-healthy-contributions/setting-guidelines-for-repository-contributors
- Adding a security policy to your repository  
  https://docs.github.com/en/code-security/how-tos/report-and-fix-vulnerabilities/configure-vulnerability-reporting/adding-a-security-policy-to-your-repository
- Available rules for rulesets  
  https://docs.github.com/en/repositories/configuring-branches-and-merges-in-your-repository/managing-rulesets/available-rules-for-rulesets
- About CODEOWNERS  
  https://docs.github.com/zh/repositories/managing-your-repositorys-settings-and-features/customizing-your-repository/about-code-owners?ref=dailydev
- Discussions  
  https://docs.github.com/en/discussions
- About dependency review  
  https://docs.github.com/en/code-security/concepts/supply-chain-security/about-dependency-review
- Managing security and analysis settings for your repository  
  https://docs.github.com/en/repositories/managing-your-repositorys-settings-and-features/enabling-features-for-your-repository/managing-security-and-analysis-settings-for-your-repository?learn=dependabot_alerts
- Managing GitHub Actions settings for a repository  
  https://docs.github.com/en/repositories/managing-your-repositorys-settings-and-features/enabling-features-for-your-repository/managing-github-actions-settings-for-a-repository?from=20423&from_column=20423
- Exporting a software bill of materials for your repository  
  https://docs.github.com/en/code-security/how-tos/secure-your-supply-chain/establish-provenance-and-integrity/exporting-a-software-bill-of-materials-for-your-repository
- Use artifact attestations  
  https://docs.github.com/en/actions/how-tos/secure-your-work/use-artifact-attestations/use-artifact-attestations

### OpenSSF and related ecosystem

- OpenSSF OSPS Baseline  
  https://baseline.openssf.org/
- OpenSSF OSPS Baseline project page  
  https://openssf.org/projects/osps-baseline/
- OpenSSF Scorecard  
  https://scorecard.dev/
- OpenSSF Best Practices Badge  
  https://openssf.org/projects/best-practices-badge/
- SLSA getting started  
  https://slsa.dev/how-to/get-started

### Compliance, metadata, community health, and release practice

- OpenChain  
  https://openchainproject.org/
- REUSE Specifications  
  https://reuse.software/specifications/
- SPDX  
  https://spdx.dev/
- CHAOSS  
  https://chaoss.community/
- Semantic Versioning  
  https://semver.org/
- Keep a Changelog  
  https://keepachangelog.com/en/1.0.0/

### Open source guidance

- Open Source Guides, Best Practices for Maintainers  
  https://opensource.guide/zh-hans/best-practices/
- Linux Foundation Open Source Guides  
  https://www.linuxfoundation.org/resources/open-source-guides

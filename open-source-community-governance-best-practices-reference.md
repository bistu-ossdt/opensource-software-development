# Open Source Community Governance Best Practices Reference

## Purpose

This document summarizes recent and authoritative guidance on open source community governance. It is intended as a reference for course and textbook design, not as part of the textbook chapter sequence.

## Core Conclusion

Modern open source community governance is no longer just an informal culture of “friendly maintainers and public issues.” Current best practice emphasizes:

- explicit governance documents
- documented roles and paths to leadership
- public and archived communication
- contributor onboarding and retention
- conduct enforcement and conflict response
- measurable community health
- sustainable maintainer operations
- transparent handling of corporate participation

In short: modern governance turns a project from a code repository into a durable public collaboration system.

## Key Governance Practice Areas

### 1. Write governance down

Projects should document how they are run. Governance should not live only in the maintainers’ heads.

Typical governance topics include:

- roles and responsibilities
- decision-making process
- voting or consensus rules
- how people gain and lose authority
- where disputes go

For smaller projects this may begin in `README` or `CONTRIBUTING.md`; for larger projects it should become a dedicated `GOVERNANCE.md`.

### 2. Define roles and contributor ladders

Modern communities should make it clear how someone moves from user to contributor to reviewer to maintainer. Role ambiguity increases gatekeeping and discourages long-term contribution.

Good governance documents explain:

- what “contributor,” “committer,” “maintainer,” or “core team” mean
- what privileges each role has
- how someone can grow into leadership

### 3. Prefer public, asynchronous, archived communication

Open source communities scale better when major discussion happens in places that are public, searchable, and archived. This reduces private gatekeeping and helps new contributors catch up.

Best practice is to reserve private channels for truly sensitive matters such as security, moderation, or legal risk.

### 4. Make communities welcoming on purpose

Healthy communities do not emerge automatically. Projects should actively reduce friction for first-time contributors through:

- readable documentation
- clear contribution guidance
- “good first issue” style entry points
- responsive maintainer behavior
- public acknowledgement of contributions

Contributor experience is part of governance.

### 5. Separate discussion, support, and executable work

Governance is improved when projects distinguish between:

- broad discussion
- user support
- roadmap or design debate
- actionable issues

This helps maintain focus and makes participation less confusing.

### 6. Adopt a code of conduct with enforcement paths

A code of conduct is not enough by itself. Projects should define:

- expected behavior
- reporting channels
- enforcement responsibilities
- consequences and remediation paths

Governance includes how norms are enforced, not only how they are stated.

### 7. Measure community health

Projects should not rely only on intuition or star counts. Governance benefits from tracking signals such as:

- issue and pull request responsiveness
- contributor retention
- maintainer concentration
- review bottlenecks
- user and contributor growth

Community metrics help detect fragility early.

### 8. Plan for maintainer sustainability and succession

Modern governance should reduce dependency on one person. Good practice includes:

- backup administrators
- shared ownership of infrastructure
- documented maintainer expectations
- leadership succession paths
- recognition of burnout risk

### 9. Handle corporate participation transparently

Many successful projects involve paid contributors and vendor interests. Modern governance should make room for company participation without allowing hidden control or unfair privilege.

Important themes include:

- transparent affiliation
- contribution-based legitimacy
- vendor neutrality where relevant
- visible decision processes

### 10. Match governance model to project scale

Not every project needs the same model. Smaller projects may begin with a BDFL-style structure. Larger projects often need councils, committees, subteams, or working groups. The best model is the one that remains understandable, fair, and operational at the project’s actual scale.

## Outdated Governance Patterns

Practices that are no longer sufficient on their own include:

- undocumented leadership and invisible decision-making
- maintainers acting as a private clique
- no path for contributors to gain trust or authority
- relying on private messages instead of public channels
- having a code of conduct without reporting or enforcement paths
- assuming community health can be inferred from popularity
- allowing company influence without explicit norms or transparency
- having no backup maintainers or succession plan

## Why This Matters for This Project

For this repository, governance should be treated as a stable core part of “open source development technique,” not as an optional community add-on. Students should learn that:

- open source is not only code openness, but organized public collaboration
- rules, roles, and transparency make scale possible
- governance affects contributor experience, quality, sustainability, and legitimacy
- maintainers are not just technical reviewers; they are also stewards of process and community

## Reference Sources

### Open Source Guides

- Leadership and Governance  
  https://opensource.guide/leadership-and-governance/
- Building Welcoming Communities  
  https://opensource.guide/building-community/
- Code of Conduct  
  https://opensource.guide/code-of-conduct/
- Open Source Metrics  
  https://opensource.guide/metrics/
- Best Practices for Maintainers  
  https://opensource.guide/best-practices/

### Apache, Jupyter, and project governance examples

- Apache Software Foundation, How the ASF Works  
  https://www.apache.org/foundation/how-it-works/
- Project Jupyter Governance  
  https://jupyter.org/governance/
- Kubernetes Community  
  https://github.com/kubernetes/community
- Kubernetes Steering Committee  
  https://github.com/kubernetes/steering

### Linux Foundation and ecosystem guidance

- Linux Foundation, Building Leadership in an Open Source Community  
  https://www.linuxfoundation.org/resources/open-source-guides/building-leadership-in-an-open-source-community
- Linux Foundation Open Source Guides  
  https://www.linuxfoundation.org/resources/open-source-guides
- CHAOSS  
  https://chaoss.community/

### Platform and governance tooling references

- GitHub community profiles for public repositories  
  https://docs.github.com/en/communities/setting-up-your-project-for-healthy-contributions/about-community-profiles-for-public-repositories?apiVersion=2022-11-28
- GitHub discussions documentation  
  https://docs.github.com/discussions
- Adding a code of conduct to your project  
  https://docs.github.com/en/communities/setting-up-your-project-for-healthy-contributions/adding-a-code-of-conduct-to-your-project

### CNCF governance references

- CNCF governance guide  
  https://contribute.cncf.io/community/governance/
- CNCF governance template by subprojects  
  https://contribute.cncf.io/maintainers/templates/governance-subprojects/
- CNCF community best practices: vendor neutrality  
  https://contribute.cncf.io/projects/best-practices/community/vendor-neutrality

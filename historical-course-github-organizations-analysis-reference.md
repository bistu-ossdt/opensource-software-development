# Historical Course GitHub Organizations Analysis Reference

## Purpose

This document summarizes what can be learned from the course GitHub organizations used in 2022, 2023, 2024, and 2025. It is a course-design reference for textbook planning, appendix design, and experiment design. It is not part of the textbook chapter sequence.

## Scope and Method

The analysis is based on the public state of the following GitHub organizations as observed on 2026-03-20:

- 2022: https://github.com/Bistu-OSSDT-2022/
- 2023: https://github.com/Bistu-OSSDT-2023/
- 2024: https://github.com/Bistu-OSSDT-2024/
- 2025: https://github.com/Bistu-OSSDT-2025/

The review included:

- organization repository counts and repository lists
- organization-level `.github` repositories where available
- representative project repositories from 2023, 2024, and 2025
- visible repository files, metadata, and public presentation

This is a structural review, not a full code-quality audit of every repository.

## Verified High-Level Findings

The course already has a strong and rare foundation: students work in public GitHub organizations, collaborate in teams, and publish project repositories openly. This is a major institutional strength and should be preserved.

At the same time, most repositories still look closer to **public course projects** than to **maintainable early-stage open source projects**. The redesign should therefore keep the public team-project model, while upgrading the expected baseline in governance, review, CI, release discipline, and security awareness.

## Observed Trends

### 1. Public project practice is stable across years

Verified public repository counts:

- 2022: 40 repositories
- 2023: 31 repositories
- 2024: 38 repositories
- 2025: 22 repositories

This confirms that the course has sustained a multi-year practice of organizing student open collaboration in public.

### 2. Project naming became more product-oriented

Earlier repositories often used numbered or member-based names. Later repositories more often look like independent products, for example:

- `MarkLens`
- `CourtLink`
- `Expense-Manager`
- `Student-Marketplace`

This is a meaningful shift from assignment identity toward project identity.

### 3. Technology stacks moved toward web and AI contexts

Earlier repositories showed more Python and Java. Later cohorts show more JavaScript, TypeScript, Vue, React, and AI-adjacent project themes. This reflects a real shift in student interests and the surrounding tool ecosystem.

### 4. Documentation awareness improved

Representative repositories show useful documentation habits beyond a minimal `README`, including files such as:

- `LICENSE`
- `INSTALL`
- `FAQ`
- `HISTORY`
- `CREDITS`
- `CONTRIBUTING.md`

This is important because it means the course already teaches students to present work publicly, not just submit code privately.

## Main Strengths

- real team collaboration in public repositories
- public artifacts that remain inspectable after the course
- visible project archive across multiple years
- at least some movement from assignment naming to product naming
- growing awareness of contributor-facing documentation

## Main Gaps Relative to Modern Open Source Practice

### 1. Most repositories still look short-cycle

Repository activity appears concentrated around the teaching window. That is normal for a course, but it means many projects are delivered rather than maintained.

### 2. Governance is not yet a visible baseline

Sampled repositories often include `README` and `LICENSE`, but less often show modern baseline files such as:

- `CODE_OF_CONDUCT.md`
- `SECURITY.md`
- `GOVERNANCE.md`
- issue templates
- pull request templates
- `CODEOWNERS`

### 3. CI and workflow automation are not consistently visible

The sampled repositories did not show a strong common pattern of `.github/workflows` or required automated checks. This suggests the course historically emphasized open publication and team delivery more than engineering gates.

### 4. Organization-level `.github` repositories are useful but not yet mature template hubs

The 2023, 2024, and 2025 organizations all include a public `.github` repository, which is a good sign. However, these repositories look closer to course coordination and information-sharing spaces than to full organization-wide governance and automation baselines.

## Evidence from Sample Repositories

- `Bistu-OSSDT-2023/20-Fancy_Snake` shows a public team project with `README`, `LICENSE`, `INSTALL`, `FAQ`, `HISTORY`, and `CREDITS`, which indicates strong documentation awareness.
- `Bistu-OSSDT-2024/29-EmiliaVoice` shows a later AI-oriented project with `README`, `LICENSE`, `INSTALL`, `FAQ`, `HISTORY`, and `CREDITS`, plus outward-facing deployment information.
- `Bistu-OSSDT-2025/MarkLens` shows a more product-oriented naming style and includes `README.md`, `LICENSE`, `CONTRIBUTING.md`, `FAQ.md`, `history.md`, `credits.md`, and `install.md`.
- The 2023, 2024, and 2025 `.github` repositories demonstrate organization-level coordination awareness, but they do not yet clearly function as standardized governance-template and CI-baseline repositories.

## Implications for Future Course Design

The historical model should be preserved, but the expected project baseline should be upgraded from “public student repository” to “small but credible open source project.”

That suggests future course design should require:

- a common repository template
- a minimum governance file set
- pull request based collaboration with review evidence
- basic CI for build, lint, or test checks
- release, version, and changelog discipline
- basic security and supply-chain awareness

The key conclusion is simple: the course already proves students can collaborate publicly. The next step is to make that collaboration look and operate more like modern open source development.

## Example Repositories Reviewed

- 2023 `.github` organization repository  
  https://github.com/Bistu-OSSDT-2023/.github
- 2024 `.github` organization repository  
  https://github.com/Bistu-OSSDT-2024/.github
- 2025 `.github` organization repository  
  https://github.com/Bistu-OSSDT-2025/.github
- 2023 `20-Fancy_Snake`  
  https://github.com/Bistu-OSSDT-2023/20-Fancy_Snake
- 2024 `29-EmiliaVoice`  
  https://github.com/Bistu-OSSDT-2024/29-EmiliaVoice
- 2025 `MarkLens`  
  https://github.com/Bistu-OSSDT-2025/MarkLens

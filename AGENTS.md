# Repository Guidelines

## Project Structure & Module Organization

This repository is a documentation-first course-and-book design project. The main content lives in Markdown files at the repository root.

The current material system is multi-layered rather than “book only”:

- `00-preface.md`: current source-of-truth for overall course design, textbook requirements, and editorial principles; student-facing parts may later be rewritten as a textbook preface
- `01-overview.md` through `05-leveraging-open-source-software-resources.md`: core textbook chapters
- `06-course-design-for-ai-era-open-source-software-development.md`: course-design extension
- `chapter-specification-reference.md`, `textbook-development-workflow-reference.md`, `bilingual-terminology-and-naming-conventions-reference.md`: execution-level specifications
- `chapter-baseline-and-stretch-blueprint-reference.md`, `experiment-baseline-and-stretch-blueprint-reference.md`: structural blueprints
- `chapter-checklist-template.md`: per-chapter execution template
- `README.md`: repository overview and chapter mapping
- `ref/`: historical practice materials and other legacy reference inputs

There is no `src/`, `tests/`, or asset pipeline. Keep new contributor-facing docs in the root unless a clear subdirectory is introduced for templates or references.

## Build, Test, and Development Commands

There is no formal build system in this checkout. Use lightweight shell checks while editing:

- `rg '^#' *.md`: inspect heading hierarchy
- `wc -l *.md`: compare chapter size and spot accidental truncation
- `sed -n '1,80p' FILE.md`: review an edited section in context
- `markdownlint *.md`: optional, if installed, for Markdown consistency

## Coding Style & Naming Conventions

Write in clear Markdown with ATX headings (`#`, `##`, `###`). Keep paragraphs short and lists flat. Use fenced code blocks for commands and examples.

File naming should follow the existing pattern:

- numbered chapters: `01-topic-name.md`
- supporting docs: descriptive kebab-case names, e.g. `course-design-notes.md`

Preserve the meaning of existing textbook content when revising chapters. Put major restructures or new pedagogical proposals in separate files first.

## Testing Guidelines

This repository has no automated test suite. Validation is manual:

- check heading order and duplicate headings
- verify links and cited filenames
- confirm chapter cross-references still match `README.md`
- review diffs for accidental formatting-only churn

## Commit & Pull Request Guidelines

Git history is not available in this checkout, so follow a simple convention:

- use imperative commit titles, e.g. `docs: refine chapter 3 workflow section`
- keep each commit focused on one chapter or one documentation task

PRs should include a short summary, affected files, rationale for structural changes, and any source links used for updated factual claims. Screenshots are unnecessary unless rendering is part of the change.

## Specification Hierarchy and Conflict Resolution

`00-preface.md` is the top-level source of truth for the entire course design. If any secondary specification (the `*-reference.md` files) conflicts with `00-preface.md`, `00-preface.md` takes precedence and the secondary specification must be corrected to align.

If a change needs to be made that would affect principles defined in `00-preface.md`, modify `00-preface.md` first, then propagate the change to all affected secondary specifications and to `course-design-summary-and-core-references.md` in the same update.

Secondary specifications must not duplicate content already defined in `00-preface.md`. Instead, they should reference the relevant section (e.g., "see 00-preface §课程材料体系") and only add rules or details that are specific to their own scope.

The practical hierarchy is:

- Level 1: `00-preface.md`
- Level 2: execution specifications and templates, including `chapter-specification-reference.md`, `textbook-development-workflow-reference.md`, `bilingual-terminology-and-naming-conventions-reference.md`, `course-structure-specification-best-practices-reference.md`, `chapter-baseline-and-stretch-blueprint-reference.md`, `experiment-baseline-and-stretch-blueprint-reference.md`, and `chapter-checklist-template.md`
- Level 3: synchronization and collaboration documents such as `course-design-summary-and-core-references.md`, `AGENTS.md`, and `README.md`

## Agent-Specific Notes

`00-preface.md` is the current requirements document for the course system. It summarizes the core constraints: undergraduate audience, open-source-development focus, durable early chapters, AI content placed later and used in service of open-source practice, a strong practice orientation, and a multi-layer material structure built around:

- `Technical Book Manuscript`
- `Student Study Guide`
- `Instructor Guide`
- `Course Syllabus / Course Guide`
- `Appendices`
- `Lab / Project Materials`
- `Case Library`

During drafting, treat it as the primary editorial contract across all of those layers.

`course-design-summary-and-core-references.md` is the outward-facing one-page summary. When course principles, chapter structure, or the core external reference set changes, update that file in the same change so it stays suitable for external sharing.

When editing, prefer additive changes over silent rewrites. If a change updates teaching scope, chapter structure, or material-layer structure, reflect it in `README.md` and keep a clear boundary between stable technical-book content and fast-changing AI practice guidance.

Use `chapter-checklist-template.md` when developing a chapter package so the minimum deliverable set stays consistent.

When the manuscript is complete, student-facing parts of `00-preface.md` can be rewritten into a textbook preface without changing those core constraints.

# Repository Guidelines

## Project Structure & Module Organization

This repository is a documentation-first course and manuscript project. Public tracked content should be limited to course-facing materials:

- `01-overview.md` through `05-leveraging-open-source-software-resources.md`: manuscript chapters
- `course-design-summary-and-core-references.md`: outward-facing course summary
- `README.md`: public repository overview
- `scripts/build_pages.py` and `.github/workflows/pages.yml`: GitHub Pages build and deploy files

Local drafting plans, research notes, migration matrices, and other internal writing-control documents are not part of the maintained public content set.

## Build, Test, and Development Commands

There is no application build pipeline. Use lightweight checks while editing:

- `python3 -m py_compile scripts/build_pages.py`: syntax-check the Pages build script
- `rg '^#' *.md`: inspect heading hierarchy
- `wc -l *.md`: compare chapter size and catch accidental truncation
- `sed -n '1,120p' FILE.md`: review an edited section in context

## Coding Style & Naming Conventions

Write in clear Markdown with ATX headings (`#`, `##`, `###`). Keep paragraphs concise and lists flat. Use fenced code blocks for commands and examples.

For public manuscript and course content:

- prefer durable wording over fast-changing tool detail
- keep the manuscript in a general technical-book voice rather than classroom language
- preserve stable filenames for chapter manuscripts

## Testing Guidelines

This repository has no automated content test suite. Validate changes manually:

- check heading order and duplicate headings
- verify chapter links and generated-site references
- confirm `scripts/build_pages.py` still matches the public tracked manuscript set
- review diffs for accidental formatting-only churn

## Commit & Pull Request Guidelines

Use focused, imperative commit titles, for example:

- `docs: expand chapter 2 licensing discussion`
- `docs: update course site manuscript index`

Keep each commit centered on one manuscript change, one site change, or one repository-boundary cleanup.

## Public Repository Boundary

This repository is intended to publish course-facing outputs, not the full internal authoring workspace.

- keep manuscript chapters, public summaries, and deployment files tracked
- keep `ref/` untracked
- keep internal planning, research, migration, and drafting-control files out of the public tracked set

When in doubt, ask whether a file is meant for readers/course users or only for authors/editors. Only the former belongs in the public repository.

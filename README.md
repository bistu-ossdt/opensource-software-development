# Open Source Software Development

This repository publishes the course-facing materials for `Open Source Software Development`: book-manuscript chapters, outward-facing course documents, and the GitHub Pages site used to browse them.

## Public Scope

Tracked content in this repository should be limited to:

- manuscript chapters and other course materials intended for readers or course users
- outward-facing overview documents such as `course-design-summary-and-core-references.md`
- site-generation and deployment files such as `scripts/build_pages.py` and `.github/workflows/pages.yml`

Internal planning, research, migration, and drafting-control documents are maintained outside the public tracked set.

## Current Manuscript State

- `01-overview.md`: rewritten manuscript draft for `Origins and Evolution of Open Source`
- `02-development-of-open-source-software.md`: rewritten manuscript draft for `Free Software, Open Source, and Licensing`
- `03-development-models-and-characteristics.md`: rewritten manuscript draft for `Open Source Communities and Governance`
- `04-participating-in-and-organizing-open-source-projects.md`: rewritten manuscript draft for `Core Engineering Workflow of Open Source Development`
- `05-leveraging-open-source-software-resources.md`: legacy chapter content retained for later migration and rewriting

## Site

The repository includes a generated course website deployed through GitHub Pages.

- build script: `scripts/build_pages.py`
- workflow: `.github/workflows/pages.yml`

## Local Reference Inputs

Files under `ref/` are local reference inputs for historical analysis and drafting support. They are not part of the maintained public course-material set and should normally remain untracked.

# Open Source Software Development

This repository publishes the course-facing materials for `Open Source Software Development`: book-manuscript chapters, outward-facing course documents, and the GitHub Pages site used to browse them.

For public-facing book structure, this project distinguishes between:

- appendices: supplementary reading units that still carry content
- back-matter tools: lookup/support units such as the whole-book glossary and references

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
- `05-leveraging-open-source-software-resources.md`: current chapter-5 skeleton draft for `Reading and Understanding Open Source Projects`
- `06-participating-in-open-source-projects.md`: current chapter-6 skeleton draft for `Participating in Open Source Projects`
- `07-ai-assisted-open-source-development-practice.md`: current chapter-7 skeleton draft for `AI-Assisted Open Source Development Practice`
- `08-organizing-and-releasing-your-open-source-project.md`: current chapter-8 skeleton draft for `Organizing and Releasing Your Open Source Project`

## Current Appendices

- `appendix-open-source-history-timeline.md`: appendix for the open source history timeline
- `appendix-open-source-people.md`: appendix for the open source people guide
- `appendix-open-source-people-event-project-map.md`: appendix for the people-event-project map
- `appendix-open-source-ai.md`: appendix for the open source AI landscape

## Current Back-Matter Tools

- `98-glossary.md`: initial back-matter glossary draft for book-level terminology
- `99-book-references.md`: initial back-matter references draft for book-level sources

## Current Teaching Support State

- `chapter-01-study-guide.md` and `chapter-01-instructor-guide.md`: initial teaching-support drafts derived from chapter 1
- `chapter-02-study-guide.md` and `chapter-02-instructor-guide.md`: initial teaching-support drafts derived from chapter 2
- `chapter-03-study-guide.md` and `chapter-03-instructor-guide.md`: initial teaching-support drafts derived from chapter 3
- `chapter-04-study-guide.md` and `chapter-04-instructor-guide.md`: initial teaching-support drafts derived from chapter 4
- `chapter-05-study-guide.md` and `chapter-05-instructor-guide.md`: chapter-5 teaching-support skeletons aligned with the manuscript skeleton
- `chapter-06-study-guide.md` and `chapter-06-instructor-guide.md`: chapter-6 teaching-support skeletons aligned with the manuscript skeleton
- `chapter-07-study-guide.md` and `chapter-07-instructor-guide.md`: chapter-7 teaching-support skeletons aligned with the manuscript skeleton
- `chapter-08-study-guide.md` and `chapter-08-instructor-guide.md`: chapter-8 teaching-support skeletons aligned with the manuscript skeleton

## Current Chapter-Level Lab / Project Materials State

- `chapter-01-lab-project-materials.md` through `chapter-04-lab-project-materials.md`: initial chapter-level lab / project materials aligned with the team project mainline

## Current Appendix Support State

- `chapter-01-appendix-support.md` through `chapter-04-appendix-support.md`: initial appendix-support drafts for templates, checklists, and comparison tables

## Current Case Teaching Pack State

- `chapter-01-case-teaching-pack.md` through `chapter-04-case-teaching-pack.md`: initial chapter-level case teaching packs for the first four chapters

## Site

The repository includes a generated course website deployed through GitHub Pages.

- build script: `scripts/build_pages.py`
- workflow: `.github/workflows/pages.yml`

## Current Public Site Structure

The public site is currently organized into five reader-facing sections:

- `course.html`: course positioning, material layers, and current public progress
- `manuscript.html`: chapter drafts, appendices, glossary, and references
- `teaching-support.html`: study guides and instructor guides for chapters 1-8
- `labs-project.html`: team-project mainline and chapter-level lab/project materials
- `cases-references.html`: anchor cases, case teaching packs, appendices, and core external references

## Current Public Progress Snapshot

- manuscript: chapters 1-4 expanded; chapters 5-8 skeletons
- appendices: history timeline, people guide, people-event-project map, and open source AI
- back matter: whole-book glossary and whole-book references
- teaching layer: chapter 1-8 study guides and instructor guides, with chapter 5-8 still at skeleton level
- chapter-level support: lab/project materials, appendix support, and case teaching packs for chapters 1-4
- site: GitHub Pages navigation now connects manuscript, teaching, labs, and case/reference entry points around the same public material set

## Local Reference Inputs

Files under `ref/` are local reference inputs for historical analysis and drafting support. They are not part of the maintained public course-material set and should normally remain untracked.

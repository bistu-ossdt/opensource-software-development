# Textbook Development Workflow Reference

## Purpose

This document defines the recommended workflow for developing this course as an integrated system of textbook chapters, appendices, experiments, and supporting materials. It is a reference for authors and editors, not part of the textbook chapter sequence.

## Core Principle

Do not write the full textbook first and then add appendices and experiments afterward. Also do not draft chapters in isolation without a whole-course plan.

At the same time, do not postpone “real book writing” until after every internal course-design document is finished. Once the chapter structure, chapter specification, and layering rules are stable enough, chapter manuscripts should be written directly in publishable textbook form.

More specifically, they should be written in a practical technical-book style rather than as temporary teaching notes. The target is closer to a durable O'Reilly-like engineering book than to a lecture handout, while still serving undergraduate teaching needs.

The concrete manuscript-size and completion thresholds for that “publishable technical-book” target are defined in `chapter-specification-reference.md` under `出版级书稿体量与完成度标准`.

At the language level, the technical book layer should default to a general reader interested in open source software development, not explicitly to students or teachers. Explicit teaching language belongs in the study guide, instructor guide, syllabus, labs, and other course-support layers.

The recommended workflow is:

1. Design the course as a whole.
2. Then develop each chapter as a complete teaching unit.
3. Finally perform whole-book integration and revision.

## Phase 1: Whole-Course Design

Before chapter writing begins, define the overall structure:

- course goals and target audience
- prerequisite knowledge
- chapter sequence and dependency order
- material layers across the whole course
- which content belongs in the technical book, study guide, instructor guide, syllabus/guide, appendices, lab materials, and case library
- practice progression across the course
- how assessments, projects, and chapter outcomes map to each other

The current source of truth for these decisions is `00-preface.md`.

## Phase 2: Chapter-by-Chapter Integrated Development

Each chapter should be developed together with its related teaching materials. For every chapter, prepare:

- chapter goals
- textbook outline and main narrative
- chapter opening scenario / core case
- publishable chapter manuscript draft
- study guide mapping
- instructor guide mapping
- appendix needs, if any
- companion experiments or classroom activities
- key terms and references
- links to previous and next chapters

This means Chapter 1 should be designed as a full unit before moving to Chapter 2, rather than writing all main chapters first and backfilling practice later.

It also means each chapter should produce multiple synchronized outputs:

- an internal chapter package for course design and editing control
- a general-reader technical-book manuscript suitable for eventual publication as a book chapter
- a student study guide unit derived from the chapter package and main manuscript
- an instructor guide unit derived from the chapter package and main manuscript

Course-syllabus information remains course-level rather than chapter-level, but each chapter should still map to course modules, schedule, and project milestones.

## Recommended Per-Chapter Output

For each chapter, produce the following package:

- internal chapter positioning notes
- core case / scenario notes
- main chapter manuscript
- study guide notes or draft unit
- instructor guide notes or draft unit
- appendix notes or appendix placeholders
- experiment or activity plan
- terminology list
- reference list
- editor notes on open questions or future revisions

## Phase 3: Whole-Book Integration

After chapter packages exist, perform a full integration pass:

- unify terminology and bilingual usage
- remove duplication across chapters and appendices
- check that experiments align with chapter concepts
- verify progression from early chapters to advanced practice
- ensure AI-related content remains in later practice-oriented sections
- confirm the whole course still matches the principles in `00-preface.md`

## Production Priority: Three-Round Strategy

The seven material layers cannot all be produced simultaneously. To make the workflow actionable, chapter development should follow a three-round production strategy:

### Round 1: Core chapter development

Focus on producing:

- internal chapter package (positioning, goals, baseline/stretch, term list, case/appendix/lab interfaces)
- technical book manuscript draft (publishable chapter text)

Round 1 is the critical path. No chapter should move to Round 2 until its manuscript draft and internal package are stable.

### Round 2: Teaching support layers

Based on the stable manuscript from Round 1, produce:

- student study guide unit
- instructor guide unit

These layers must be derived from the manuscript, not written independently.

### Round 3: Supporting materials and course-level integration

Complete the remaining layers:

- appendices (command references, templates, configuration examples)
- case library entries
- lab / project materials (detailed experiment instructions, rubrics)
- course syllabus / course guide (course-level, not per-chapter)

Round 3 materials are expected to be updated more frequently than Rounds 1-2.

### Practical implication

This three-round strategy means that "produce all seven layers per chapter" remains the eventual goal, but in practice the team should prioritize getting Round 1 right before investing heavily in Rounds 2-3. A chapter with a strong manuscript and internal package is far more valuable than a chapter with seven incomplete layers.

## Why This Workflow Fits This Project

This repository is producing a course system, not just a book. The seven material layers (defined in 00-preface §课程材料体系) must be designed together but carried in different layers.

This workflow keeps the book stable while preserving a strong practical orientation. It reduces rewrite cost by writing book-quality chapters from the start, and improves manuscript quality by keeping learning support and teaching support out of the main manuscript.

In other words, the book layer should explain the discipline, methods, cases, and practice of open source software development itself; the teaching layers should explain how students learn it and how teachers teach it.

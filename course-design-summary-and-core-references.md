# Course Design Summary and Core References

> Maintenance note: this is the outward-facing one-page summary of the current course-design direction. When the course principles, chapter plan, or core reference set changes, update this document as part of the same change.

## Core Ideas

This course is designed as an undergraduate **Open Source Software Development** course rather than a general software engineering course or an AI coding tools course. Its goal is to help students understand open source culture, history, licenses, community logic, and modern development practice, while also enabling them to begin participating in and building real open source projects.

The course follows a **stable core + evolving practice** structure. Early chapters focus on durable topics such as open source history, key figures, free software and open source concepts, licenses, community governance, and the basic engineering mechanisms of version control, testing, CI, release, and maintenance. Later chapters address faster-changing practice, including modern GitHub-based collaboration, team-based open source project development, and AI-assisted open source workflows.

The course is also designed with **baseline + stretch elasticity**. Most content is intended to be teachable and usable in ordinary undergraduate computing programs with standard prerequisites. At the same time, some advanced cases, appendices, and experiments should support stronger students and top universities that want deeper work in governance, CI, security, supply chain practice, and AI-assisted open source engineering. The design does not target programs below that baseline.

The course is being designed for future **bilingual Chinese-English development**, so its structure, terminology, and material types are intended to stay aligned with mainstream international university course organization. Chinese and English versions should share the same chapter logic, material layers, and core terminology rather than being redesigned independently.

The course is designed as an integrated system of **technical book manuscript + student study guide + instructor guide + course syllabus/guide + appendices + lab/project materials + case library**, not as a standalone book. The technical book carries the stable core knowledge and is written for technical readers in an O'Reilly-like engineering-book style rather than as a lecture handout. Its audience is broader than the classroom, while its difficulty baseline still assumes the knowledge level of students with normal undergraduate computing prerequisites and its content remains elastic through baseline and stretch layers. The study guide and instructor guide belong to the teaching layer and support learning and teaching around that book. The syllabus/guide carries course-level organization and policy. Appendices carry faster-changing tools and references. Lab/project materials translate concepts and workflows into action. Case materials provide real repositories, governance examples, licensing examples, pull requests, CI practices, and project evidence.

A central practice line runs through the whole course: **students work in teams to develop an open source project**. This team project is not an end-of-term add-on, but the main practical thread of the course. As students learn history, governance, licensing, repository setup, engineering workflows, testing, release, and AI-assisted practice, they apply each part to their team project.

The course also takes two strong positions. First, **community governance is a foundational part of open source development technique**, not just an optional cultural topic. Second, **modern open source development is no longer only “public repository + pull requests,” but a governed, testable, review-based, security-aware, and supply-chain-conscious engineering system**.

## Core References

### Open source foundations

- Free Software Foundation, *What is free software? The Free Software Definition*  
  https://www.gnu.org/philosophy/free-sw.html
- Open Source Initiative, *The Open Source Definition*  
  https://opensource.org/osd

### Education and course design

- ACM CSED, *Generative AI for Computing Education* (2024)  
  https://csed.acm.org/wp-content/uploads/2024/01/Generative-AI-v1.pdf
- Cornell CS 5152, *Open-Source Software Engineering*  
  https://www.cs.cornell.edu/courses/cs5152/2019fa/
- Stanford CS101  
  https://web.stanford.edu/class/cs101/
- MIT, *The Missing Semester of Your CS Education*  
  https://missing-semester-cn.github.io/

### Community and governance

- Karl Fogel, *Producing Open Source Software*  
  https://producingoss.com/
- Nadia Eghbal, *Working in Public: The Making and Maintenance of Open Source Software*
- Open Source Guides  
  https://opensource.guide/
- CHAOSS  
  https://chaoss.community/

### Modern open source engineering practice

- GitHub Docs  
  https://docs.github.com/
- OpenSSF OSPS Baseline  
  https://baseline.openssf.org/
- OpenSSF Scorecard  
  https://scorecard.dev/
- OpenChain  
  https://openchainproject.org/
- REUSE Specification  
  https://reuse.software/specifications/
- SPDX  
  https://spdx.dev/
- Semantic Versioning  
  https://semver.org/
- Keep a Changelog  
  https://keepachangelog.com/en/1.0.0/

### AI-assisted software engineering

- GitHub, *Survey: The AI wave continues to grow on software development teams* (2024)  
  https://github.blog/news-insights/research/survey-ai-wave-grows/
- GitHub, *Octoverse 2025*  
  https://github.blog/news-insights/octoverse/octoverse-a-new-developer-joins-github-every-second-as-ai-leads-typescript-to-1/
- OpenAI Codex  
  https://openai.com/index/introducing-codex/
- Anthropic Claude Code Docs  
  https://code.claude.com/docs/en/overview
- Cursor Docs  
  https://docs.cursor.com/

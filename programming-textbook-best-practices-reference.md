# Programming Textbook Best Practices Reference

## Purpose

This note collects reference material on classic English-language programming textbooks and courses, then extracts textbook-design practices that are relevant to this repository. It is a background document for authors and editors, not part of the textbook chapter sequence.

## Representative References

### Classic programming textbooks

- *Structure and Interpretation of Computer Programs* (MIT Press)  
  https://mitpress.mit.edu/9780262367622/structure-and-interpretation-of-computer-programs/
- *How to Design Programs*  
  https://htdp.org/
- *Programming: Principles and Practice Using C++*  
  https://stroustrup.com/programming.html
- *The Practice of Programming* sample pages  
  https://www.informit.com/content/images/9780201615869/samplepages/020161586X.pdf
- *The C Programming Language* table of contents sample  
  https://www.pearson.de/media/muster/toc/toc_9780133086232.pdf
- *Think Python*  
  https://www.allendowney.com/wp/books/think-python-2e/

### Modern course exemplars

- MIT, *The Missing Semester of Your CS Education*  
  https://missing.csail.mit.edu/
- Harvard CS50  
  https://cs50.harvard.edu/x/
- Stanford CS101  
  https://web.stanford.edu/class/cs101/
- Cornell CS 5152, *Open-Source Software Engineering*  
  https://www.cs.cornell.edu/courses/cs5152/2019fa/

### Open source practice guides

- Open Source Guides  
  https://opensource.guide/zh-cn/
- Linux Foundation Open Source Guides  
  https://www.linuxfoundation.org/resources/open-source-guides

## Best Practices

### 1. Put durable concepts in the core text

The strongest textbooks keep the main narrative focused on concepts, methods, and mental models that remain useful over time. Fast-changing setup steps, product screenshots, and tool menus should live in appendices or companion materials.

This pattern appears in SICP, HtDP, K&R, PPP, and Think Python. Think Python and PPP also show the value of maintaining support pages outside the main text.

### 2. Teach a method, not just a language

HtDP is the clearest example: students are taught a systematic design approach, not only syntax. SICP similarly emphasizes models of computation and abstraction. The lesson is that a good textbook should explicitly teach how to think, decompose, test, and revise.

### 3. Treat testing, debugging, and style as core content

*The Practice of Programming* is especially strong here. Good programming books do not postpone testing, debugging, interfaces, style, and performance to the end or omit them entirely. They are part of programming, not optional polish.

### 4. Use progressive examples and scaffolding

Classic textbooks tend to move from very small examples to richer cases and then to more realistic programs. Stanford CS101 and CS50 show a similar modern pattern: lecture material, reading, written exercises, code exercises, and projects reinforce each other.

### 5. Separate textbook, appendix, and teaching materials

A strong course textbook is not identical to a lab manual. Stanford CS101 and Missing Semester are useful examples of layered teaching: core explanations are stable, while exercises, notes, and tool instructions are delivered separately and can evolve.

### 6. Support real engineering habits early

Missing Semester, CS50, PPP, and Cornell CS 5152 all show that students should encounter tools, command-line use, version control, debugging, and project structure early rather than as late add-ons.

### 7. Keep the text usable for both classroom teaching and self-study

PPP and Think Python are notable here. A strong textbook should be readable independently, but also easy to map into lectures, labs, and projects. Clear chapter goals, review questions, and companion materials help.

### 8. Use authentic cases without making the book dependent on one platform

Open Source Guides, Linux Foundation guides, and Cornell CS 5152 all point toward real project participation, but the transferable lesson is broader: use real repositories and workflows, while writing the main text around general principles.

### 9. Preserve the original language of key terms

In real computing practice, students must read English documentation, READMEs, licenses, Issues, and Pull Requests. A good textbook can explain concepts in Chinese while preserving key English terms alongside them.

## Implications for This Textbook

For this repository, the most relevant conclusions are:

- Keep early chapters stable: open source history, culture, licenses, community logic, and durable engineering mechanisms.
- Put volatile material later: GitHub interface details, AI tools, agent workflows, and rapidly changing operational guidance.
- Make software engineering content serve open source development rather than turning the book into a general software engineering survey.
- Align the textbook with practice, but keep experiments and assignments in companion materials rather than in the main narrative.
- Use open source repositories, documents, Issues, Pull Requests, tests, and CI as the main practical context.

## Notes

- Stanford CS101 is valuable as a model for structured weekly teaching units, but it is a broad computing-introduction course rather than an open source development text.
- CS50 and Missing Semester are useful as practice-oriented course references, not as direct models for textbook scope.
- Cornell CS 5152 is especially relevant because it demonstrates a strong open-source-engineering teaching pattern built around authentic projects and collaboration.

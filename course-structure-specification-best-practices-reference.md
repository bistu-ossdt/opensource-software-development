# 课程结构规范最佳实践参考

## 目的

本文档将前一轮“国际大学课程结构研究”的结果，进一步整理为可直接用于本项目的课程结构规范建议。它关注的不是某一门课讲了什么内容，而是：

> 一门面向本科生、未来将有中英文双语版本、并以技术书稿为核心的课程，材料结构应如何组织才更接近国际主流做法？

本文档是课程设计参考，不属于教材正式章节序列。

## 研究结论

基于当前参考的国际大学课程和课程体系框架，一个更合理的课程结构规范，不应只停留在“教材 + 附录 + 实验”，而应采用多层材料结构。

推荐的正式材料结构如下：

- `Technical Book Manuscript`
- `Student Study Guide`
- `Instructor Guide`
- `Course Syllabus / Course Guide`
- `Appendices`
- `Lab / Project Materials`
- `Case Library`

这套结构的关键，不是材料变多，而是职责更清楚。

## 为什么需要这种结构

### 1. 技术书稿需要保持纯净

国际主流课程通常不会让主阅读材料同时承担以下职责：

- 评分说明
- 课堂组织
- 迟交政策
- 支持渠道
- 项目里程碑
- 教师提示

如果这些内容进入主书稿，书稿就会变成课程讲义或内部脚本，而不是可独立阅读、可出版的技术书。

### 2. 学生支持材料和教师支持材料本来就应独立存在

国际主流课程普遍存在与主内容分离的支持层，如：

- syllabus
- sections
- office hours
- assignments
- study support
- instructor-facing organization

这说明：

- 学生如何学，不应完全压在主书稿中解决
- 教师如何教，也不应强行写进主书稿

因此，把 `Student Study Guide` 和 `Instructor Guide` 独立出来，是合理而且必要的。

### 3. 课程级信息和章节级信息必须分开

像课程简介、周次安排、评分比例、政策规则、项目阶段推进，这些信息在国际课程中通常属于 `Syllabus` 或 `Course Guide` 层，而不是某一章的附属内容。

如果不把这层单独抽出，后续章节规范就会不断混入课程行政信息，影响技术书稿和双语版本的一致性。

## 每一层的职责建议

各层的正式定义见 00-preface §课程材料体系 与 §整体课程设计与分层承载规则。本节仅补充从国际课程结构研究中提炼出的**增量判断原则**：

- **技术书稿**：不承担课堂安排、评分标准、作业要求、教学提示。如果这些内容进入主书稿，书稿就会变成课程讲义而非可独立阅读的技术书。
- **Student Study Guide / Instructor Guide**：必须基于主书稿使用，不应变成平行正文或第二本主书。
- **Course Syllabus / Course Guide**：通常不按章编写，而是以课程整体为单位组织。如果不把这层单独抽出，章节规范就会不断混入课程行政信息。
- **Case Library**：案例库是可持续积累的资产，不应全部写死在单章正文中。

## 推荐的结构规则

基于研究，建议本项目采用以下结构规则。

### 规则 1：主书稿只保留值得长期阅读的内容

进入 `Technical Book Manuscript` 的内容，应满足至少两个条件：

- 对理解开源软件开发长期有效
- 值得学生脱离课堂后单独阅读

### 规则 2：所有教学支持都应围绕主书稿组织

`Student Study Guide` 和 `Instructor Guide` 必须基于主书稿使用，而不是变成平行正文。

### 规则 3：课程级信息不得混入章节级主稿

周次、成绩、项目里程碑、政策信息统一进入 `Course Syllabus / Course Guide`。

### 规则 4：章节设计必须支持多层派生

每章都应能稳定派生出：

- 一章主书稿
- 一章学生学习指南单元
- 一章教师教学指南单元
- 对应的附录接口
- 对应的实验接口
- 对应的案例接口

### 规则 5：结构和命名必须可双语映射

从一开始就应保证：

- 材料层名称可中英文对应
- 章节标题可中英文对应
- 栏目名称可中英文对应
- 交付物名称可中英文对应

## 对本项目现阶段的直接建议

以上研究结论已被采纳并落实到 00-preface §课程材料体系 中。本文档作为研究依据保留，后续不再重复维护各层职责定义——以 00-preface 为准。

## 与已有文档的关系

本文档和以下文档互相补充：

- [00-preface.md](/home/bistu/opensource-book/00-preface.md)：课程整体设计原则
- [chapter-specification-reference.md](/home/bistu/opensource-book/chapter-specification-reference.md)：单章开发规范
- [textbook-development-workflow-reference.md](/home/bistu/opensource-book/textbook-development-workflow-reference.md)：开发工作流
- [international-university-course-structure-research-reference.md](/home/bistu/opensource-book/international-university-course-structure-research-reference.md)：国际课程结构研究依据

本文档的定位更接近“结构规范提炼版”，用于把研究发现转化为可执行规则。

## 参考来源

以下来源构成本轮结构规范判断的主要依据：

- Cornell CS 5152, *Open-Source Software Engineering*  
  https://www.cs.cornell.edu/courses/cs5152/2019fa/
- Harvard CS50, *Syllabus*  
  https://cs50.harvard.edu/college/2026/spring/syllabus/
- Stanford CS101  
  https://web.stanford.edu/class/cs101/
- MIT, *The Missing Semester of Your CS Education*  
  https://missing.csail.mit.edu/
- UC Berkeley CS 169, *Software Engineering*  
  https://www2.eecs.berkeley.edu/Courses/CS169/
- UC Berkeley COMPSCI 169L, *Software Engineering Team Project*  
  https://www2.eecs.berkeley.edu/Courses/COMPSCI169L/index.html
- ACM, *Curricula Recommendations*  
  https://www.acm.org/education/curricula-recommendations
- ACM / IEEE-CS, *Computing Curricula 2020*  
  https://www.acm.org/media-center/2021/march/computing-curricula-2020
- Carnegie Mellon Software Engineering Institute, *Software Engineering Curriculum*  
  https://www.sei.cmu.edu/curricula/software-engineering/

## 说明

本文档基于 2026-03-20 时点可公开访问的官方课程网站与课程框架资料整理，关注的是课程结构规范与材料分层，而不是对各课程全部教学内容的全面分析。

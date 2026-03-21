# 规范性文档索引参考

## 目的

本文档用于明确当前仓库中各类规范性文档的层级、作用范围与相互关系，避免把总原则、执行规范、模板、同步约束和研究依据混在一起使用。

它是编写与维护阶段的参考文档，不属于教材正式章节序列。

## 一级总规范

以下文档构成当前课程系统的最高层规范：

- `00-preface.md`

### 作用

- 作为课程整体设计原则与编写约束的最高层 source of truth
- 决定课程定位、课程边界、材料体系、章节结构、写作原则与更新策略

### 使用规则

- 如与其他规范性文档冲突，以 `00-preface.md` 为准
- 若课程定位、材料层级或全局原则发生变化，应先修改 `00-preface.md`

## 二级执行规范

以下文档用于把一级总规范转化为可执行的结构、流程、命名与模板：

- `chapter-specification-reference.md`
- `textbook-development-workflow-reference.md`
- `bilingual-terminology-and-naming-conventions-reference.md`
- `course-structure-specification-best-practices-reference.md`
- `chapter-baseline-and-stretch-blueprint-reference.md`
- `experiment-baseline-and-stretch-blueprint-reference.md`
- `chapter-checklist-template.md`

### 作用

- 规定单章开发方式
- 规定全书与全课程的开发工作流
- 规定双语命名与术语体系
- 规定课程材料分层方式
- 规定章节蓝图与实验蓝图
- 提供单章完成度检查模板

### 分类建议

可在内部使用时再细分为：

- 核心执行规范  
  `chapter-specification-reference.md`  
  `textbook-development-workflow-reference.md`  
  `bilingual-terminology-and-naming-conventions-reference.md`  
  `course-structure-specification-best-practices-reference.md`

- 结构蓝图  
  `chapter-baseline-and-stretch-blueprint-reference.md`  
  `experiment-baseline-and-stretch-blueprint-reference.md`

- 执行模板  
  `chapter-checklist-template.md`

## 三级配套规范 / 同步约束

以下文档不定义一级原则，但承担同步、索引、协作和对外展示约束：

- `course-design-summary-and-core-references.md`
- `AGENTS.md`
- `README.md`

### 作用

- `course-design-summary-and-core-references.md`  
  对外展示的一页摘要，需要与一级总规范同步

- `AGENTS.md`  
  仓库协作与维护约束，帮助贡献者理解结构、风格与同步要求

- `README.md`  
  当前文档索引、边界说明和文件入口

## 非规范性研究 / 依据文档

以下文档提供研究基础、背景依据或历史分析，但不直接定义执行规则：

- `international-university-course-structure-research-reference.md`
- `modern-open-source-development-best-practices-reference.md`
- `open-source-community-governance-best-practices-reference.md`
- `programming-textbook-best-practices-reference.md`
- `historical-course-github-organizations-analysis-reference.md`
- `student-project-capability-assessment-reference.md`
- `historical-three-practices-fit-analysis-reference.md`
- `historical-250622-course-materials-fit-analysis-reference.md`
- `legacy-content-to-new-course-structure-migration-matrix-reference.md`
- `chapter-01-targeted-research-reference.md`
- `chapter-02-targeted-research-reference.md`

这些文档的作用是：

- 支撑原则判断
- 提供案例来源
- 解释为什么形成当前规范

但若与一级或二级规范冲突，它们应被视为待更新的依据文档，而不是新的规则来源。

## 章节级工作文档

以下文档属于当前编写过程中的章节级工作文档，用于具体章节的设计、迁移与起稿控制：

- `chapter-01-internal-package-draft.md`
- `chapter-01-manuscript-outline-draft.md`
- `chapter-02-internal-package-draft.md`
- `chapter-02-manuscript-outline-draft.md`

这类文档的特点是：

- 服务于某一章的具体开发
- 会随着章节推进持续修改
- 不属于一级、二级或三级规范
- 也不等同于通用研究依据文档

## 使用顺序建议

后续编写与迁移时，建议按以下顺序查阅：

1. 先看 `00-preface.md`
2. 再看二级执行规范
3. 再看三级配套规范
4. 最后看研究 / 依据文档

## 当前结论

当前仓库已经形成较清晰的三级规范结构：

- 一级总规范：确定方向
- 二级执行规范：规定怎么做
- 三级配套规范：保证同步、索引和协作

后续若新增规范性文档，建议优先判断它属于哪一级，再决定放置方式，避免层级继续混乱。

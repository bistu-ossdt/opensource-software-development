# 双语术语与命名规范参考

## 目的

本文档用于统一本项目未来中英文双语版本中的结构命名、章节命名、栏目命名、实验阶段命名、交付物命名与核心术语表达。

它服务于以下目标：

- 保证中文稿与未来英文稿共享同一套结构骨架
- 保证课程材料层名称可稳定中英文映射
- 保证章节标题、栏目标题、实验阶段和交付物名称可稳定复用
- 保证关键术语在不同章节中不发生随意漂移

本文档是课程设计与编写参考，不属于教材正式章节序列。

## 总体原则

### 1. 英文原词优先作为规范锚点

对于开源、软件工程与 GitHub 工作流中的关键概念，应优先以国际通行英文原词作为规范锚点，再确定中文表达。

### 2. 中文表达追求稳定，不追求花哨

中文命名应优先选择：

- 已被广泛接受
- 易于理解
- 与英文原词可稳定一一对应

不应为了修辞或本地习惯，在不同章节里给同一概念发明多种中文叫法。

### 3. 结构名称优先统一，允许正文局部自然表达

正式材料层、章节标题、栏目标题、实验阶段名称、交付物名称，应尽量使用固定规范名。正文叙述中可以有自然变化，但正式名称必须统一。

### 4. 中英文版本共享同一套结构，不分别独立设计

未来英文版不应在结构层面重新设计，而应建立在同一套：

- 材料层
- 章节标题
- 栏目标题
- 实验阶段
- 交付物类型
- 核心术语

之上。

### 5. 双语一致性的适用边界

双语一致性约束适用于结构、术语和材料命名，**不约束中文正文的叙述风格和表达习惯**。中文版的正文写作应保持自然的中文技术书风格，不应为了与未来英文版对齐而写成翻译体。

英文版的具体生产路径（启动时机、翻译还是重写、质量保证流程、负责人）待中文版主体内容稳定后另行定义，当前阶段不做约束。

## 材料层名称规范

以下名称建议作为本项目的标准材料层命名。

| 中文名称 | 英文名称 | 说明 |
| --- | --- | --- |
| 技术书稿 | `Technical Book Manuscript` | 主书稿，可独立阅读和出版 |
| 学生学习指南 | `Student Study Guide` | 面向学生的学习支持材料 |
| 教师教学指南 | `Instructor Guide` | 面向教师的教学支持材料 |
| 课程说明 / 课程指南 | `Course Syllabus / Course Guide` | 课程级信息层 |
| 附录 | `Appendices` | 高变化、强操作性的支持材料 |
| 实验与项目材料 | `Lab / Project Materials` | 实验、项目、提交与评分材料 |
| 案例库 | `Case Library` | 可复用的真实案例与证据库 |
| 内部章节包 | `Internal Chapter Package` | 供编者与教师内部使用的控制材料 |

### 命名建议

- 中文正式文档中优先写中文名，首次出现时附英文
- 内部规范、目录、双语文件、英文版中优先使用英文名
- 不建议在正式规范中混用“讲义”“教师用书”“学生手册”“配套材料”等多个中文层名，除非这些材料被明确定义为不同层

## 章节标题规范

以下是当前 8 章结构建议采用的标准中英文标题。

| 章节序号 | 中文标题 | 英文标题 |
| --- | --- | --- |
| 第 1 章 | 开源的起源与发展 | `Origins and Evolution of Open Source` |
| 第 2 章 | 自由软件、开源软件与许可证 | `Free Software, Open Source, and Licensing` |
| 第 3 章 | 开源社区与治理 | `Open Source Communities and Governance` |
| 第 4 章 | 开源开发的基本工程流程 | `Core Engineering Workflows in Open Source Development` |
| 第 5 章 | 阅读与理解开源项目 | `Reading and Understanding Open Source Projects` |
| 第 6 章 | 参与开源项目 | `Participating in Open Source Projects` |
| 第 7 章 | AI 辅助的开源开发实践 | `AI-Assisted Open Source Development Practice` |
| 第 8 章 | 组织与发布你的开源项目 | `Organizing and Releasing Your Open Source Project` |

### 标题规则

- 中文标题应简洁明确，避免口号化
- 英文标题优先使用 Title Case
- 英文标题应体现技术书风格，避免过强课程口吻
- 后续若需缩写或目录标识，可为每章增加稳定英文短标识，例如 `origins-evolution`, `licensing`, `governance`, `workflows`

## 常用栏目标题规范

以下栏目建议作为章节、Study Guide、Instructor Guide 中的标准栏目名。

| 中文栏目名 | 英文栏目名 | 适用层 |
| --- | --- | --- |
| 导语 | `Opening` | 技术书稿 |
| 开场案例 | `Opening Case` | 技术书稿 |
| 本章将回答的问题 | `Questions This Chapter Answers` | 技术书稿 / Study Guide |
| 学习目标 | `Learning Objectives` | 内部章节包 / Study Guide / Instructor Guide |
| 核心术语 | `Key Terms` | 技术书稿 / Study Guide |
| 正文主线 | `Main Narrative` | 内部章节包 |
| 代表案例 | `Core Case` | 技术书稿 / Instructor Guide |
| 常见误区 | `Common Mistakes` | Study Guide / Instructor Guide |
| 关键提醒 | `Note / Tip / Warning` | 技术书稿 |
| 本章小结 | `Chapter Summary` | 技术书稿 |
| 延伸阅读 | `Further Reading` | 技术书稿 / Study Guide |
| 附录接口 | `Appendix Mapping` | 内部章节包 |
| 学习指南接口 | `Study Guide Mapping` | 内部章节包 |
| 教学指南接口 | `Instructor Guide Mapping` | 内部章节包 |
| 实验接口 | `Lab Mapping` | 内部章节包 |
| 可评价证据 | `Assessment Evidence` | 内部章节包 / Instructor Guide |

### 栏目命名建议

- 不建议把 `Learning Objectives` 在英文里写成 `Objectives of This Lesson` 一类更强教学口吻的变体
- 不建议把“常见误区”写成“易错点”“注意事项”“学习提示”等多套不固定标题，除非它们确实承担不同功能
- `Opening` 和 `Opening Case` 应区分：前者是导入段，后者是具体案例

## 实验阶段名称规范

以下是当前实验体系建议采用的标准中英文名称。

| 中文名称 | 英文名称 |
| --- | --- |
| 实验 1 开源观察与项目阅读 | `Lab 1: Open Source Observation and Project Reading` |
| 实验 2 团队项目立项与许可证选择 | `Lab 2: Project Initiation and License Selection` |
| 实验 3 治理基线与协作机制建立 | `Lab 3: Governance Baseline and Collaboration Setup` |
| 实验 4 GitHub 协作流与最小 CI | `Lab 4: GitHub Collaboration Workflow and Minimal CI` |
| 实验 5 外部项目理解或首次贡献 | `Lab 5: External Project Analysis or First Contribution` |
| 实验 6 团队项目 MVP 迭代 | `Lab 6: Team Project MVP Iteration` |
| 实验 7 AI 辅助开发与人工治理 | `Lab 7: AI-Assisted Development and Human Oversight` |
| 实验 8 发布、归档与项目复盘 | `Lab 8: Release, Archiving, and Project Retrospective` |

## 交付物名称规范

以下交付物名称建议在课程说明、实验材料、Study Guide、Instructor Guide 中统一使用。

| 中文名称 | 英文名称 |
| --- | --- |
| 项目阅读报告 | `Project Reading Report` |
| 项目立项说明 | `Project Proposal` |
| 许可证选择说明 | `License Rationale` |
| 仓库链接 | `Repository Link` |
| 贡献分析报告 | `Contribution Analysis Report` |
| Pull Request 记录 | `Pull Request Record` |
| 评审记录 | `Review Record` |
| 迭代记录 | `Iteration Log` |
| 阶段版本 | `Milestone Release` |
| 变更记录 | `Changelog` |
| 项目复盘文档 | `Project Retrospective` |
| AI 使用记录 | `AI Usage Log` |
| 验收证据 | `Acceptance Evidence` |
| 发布说明 | `Release Notes` |

### 交付物命名建议

- `Changelog` 建议保留英文原词作为规范名，中文可写“变更记录（Changelog）”
- `Release Notes`、`Pull Request`、`Review` 等在中文正文中可保留英文原词
- 如果未来做英文版，交付物名称应直接复用本表，不临时改写

## 核心开源与工程术语规范

以下术语建议作为当前课程的优先规范表达。

| 中文表达 | 英文原词 | 说明 |
| --- | --- | --- |
| 自由软件 | `Free Software` | 不要误译为 free-of-charge software |
| 开源软件 | `Open Source Software` | 可在必要时简称 OSS |
| 开源 | `Open Source` | 泛指开源理念、生态、项目时使用 |
| 许可证 | `License` | 不建议在技术语境中一律写“许可协议” |
| 仓库 | `Repository` | 正文首次出现给出中英对照，此后可直接用 repository |
| 分支 | `Branch` | Git 语境固定使用 |
| 提交 | `Commit` | 既可指动作，也可指提交对象 |
| 议题 | `Issue` | 不建议随意改成“问题单”“事项单” |
| 拉取请求 | `Pull Request` | 中文可解释，正文中建议保留 `Pull Request` |
| 代码评审 | `Code Review` | 与 review 记录对应 |
| 合并 | `Merge` | Git / PR 语境固定使用 |
| 派生 / 复制仓库 | `Fork` | 正文建议保留 `Fork` |
| 发布 | `Release` | 对应版本发布，不等于 deploy |
| 标签 | `Tag` | Git tag 语境 |
| 版本 | `Version` | 与 release 区分使用 |
| 变更记录 | `Changelog` | 建议保留英文原词 |
| 维护者 | `Maintainer` | 社区角色术语 |
| 贡献者 | `Contributor` | 社区角色术语 |
| 治理 | `Governance` | 社区与项目组织语境 |
| 行为准则 | `Code of Conduct` | 仓库治理文件术语 |
| 贡献指南 | `Contributing Guide` / `CONTRIBUTING.md` | 文件名优先保留英文 |
| 安全策略 | `Security Policy` / `SECURITY.md` | 文件名优先保留英文 |
| 代码所有者 | `CODEOWNERS` | 文件名与机制名保留英文 |
| 分支保护 | `Branch Protection` | GitHub / Git 规则语境 |
| 规则集 | `Rulesets` | GitHub 语境，建议保留英文 |
| 持续集成 | `Continuous Integration` / `CI` | 首次给出全称与缩写 |
| 持续交付 / 持续部署 | `Continuous Delivery / Continuous Deployment` | 需严格区分 |
| 软件物料清单 | `Software Bill of Materials` / `SBOM` | 缩写很重要 |
| 构建来源证明 | `Provenance` | 供应链语境 |
| 证明文件 | `Attestation` | 与 provenance 配套使用 |
| 依赖审查 | `Dependency Review` | GitHub / supply chain 语境 |
| 密钥扫描 | `Secret Scanning` | GitHub 安全语境 |
| 推送保护 | `Push Protection` | GitHub 安全语境 |
| 可持续性 | `Sustainability` | 社区健康与维护语境 |
| 社区健康 | `Community Health` | 社区治理语境 |
| 首次贡献 | `First Contribution` | 学生实践语境 |
| 最小可发布版本 | `Minimum Viable Product` / `MVP` | 项目主线语境 |

## AI 辅助开发术语规范

| 中文表达 | 英文原词 | 说明 |
| --- | --- | --- |
| AI 辅助开发 | `AI-Assisted Development` | 优于笼统“AI 编程” |
| AI 辅助开源开发 | `AI-Assisted Open Source Development` | 本课程优先用法 |
| 智能体工作流 | `Agentic Workflow` | 保留英文很重要 |
| 人工监督 | `Human Oversight` | AI 使用治理语境 |
| 提示词 | `Prompt` | 如需强调资产化可用 `Prompt Asset` |
| 工具调用 | `Tool Use` / `Tool Calling` | 依语境选用 |
| 背景智能体 | `Background Agent` | 特定产品语境 |
| 子智能体 | `Subagent` | 特定产品语境 |
| 代码生成 | `Code Generation` | 与审查、测试区分 |
| AI 使用记录 | `AI Usage Log` | 建议统一命名 |
| 验证清单 | `Validation Checklist` | AI 输出审查语境 |

## 文件与命名建议

### 1. 参考文档文件名

- 英文 slug 使用 kebab-case
- 尽量使用稳定、语义明确的文件名
- 避免同一类文档出现多个不一致模式

### 2. 章节文件名

建议继续使用：

- `00-preface.md`
- `01-topic-name.md`
- `02-topic-name.md`

未来如果出现英文稿，可考虑：

- 共享编号
- 通过目录区分语言版本
- 避免中英文文件名直接混杂在同一层级中长期并存

### 3. 规范型栏目名

在规范文档里，优先使用固定英文名；在中文正文里，首次出现时附英文。

例如：

- 学习目标（Learning Objectives）
- 学生学习指南（Student Study Guide）
- 教师教学指南（Instructor Guide）

## 推荐的下一步用法

本文档完成后，后续工作应按以下顺序使用它：

1. 先作为章节规范和迁移矩阵的命名依据
2. 再作为 Study Guide、Instructor Guide、Course Guide 的命名依据
3. 后续正式写作时，逐章补充和校正术语表

这意味着本文件既是当前的规范表，也是后续双语版本建设的基础词汇表。

## 与已有文档的关系

本文档和以下文档配合使用：

- [00-preface.md](/home/bistu/opensource-book/00-preface.md)
- [chapter-specification-reference.md](/home/bistu/opensource-book/chapter-specification-reference.md)
- [course-structure-specification-best-practices-reference.md](/home/bistu/opensource-book/course-structure-specification-best-practices-reference.md)
- [international-university-course-structure-research-reference.md](/home/bistu/opensource-book/international-university-course-structure-research-reference.md)

## 参考来源

本文件的命名与结构判断主要参考以下来源，并结合本项目当前课程设计需要整理：

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

## 说明

本文档基于 2026-03-20 时点的课程结构研究与现有课程设计文档整理，属于规范性参考文档。后续若正式启动英文版写作，应继续在此基础上增补术语并锁定最终规范表。

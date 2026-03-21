# 旧材料到新课程结构的迁移矩阵参考

## 目的

本文档用于把当前仓库中的旧教材材料、历史实践材料和近期补充的历史教学材料，系统映射到新的课程结构与材料体系中。

它回答的不是“旧材料是否还有价值”，而是：

- 哪些内容应进入新的 8 章技术书稿
- 哪些内容应下沉为 `Student Study Guide`、`Instructor Guide`、`Course Syllabus / Course Guide`
- 哪些内容更适合进入 `Appendices`、`Lab / Project Materials`、`Case Library`
- 哪些内容应保留为参考依据，但不直接进入维护中的正式产物

本文档是迁移与重写阶段的执行性参考，不属于教材正式章节序列。

## 使用边界

本文档服务于“迁移与重构”，不是新的一级原则文档。

- 若与 `00-preface.md` 冲突，以 `00-preface.md` 为准
- 若与单章开发要求冲突，以 `chapter-specification-reference.md` 为准
- 文中涉及 `ref/` 的材料，指本地参考输入，不意味着这些文件应纳入版本管理

## 目标结构

### 新的 8 章书稿结构

1. 开源的起源与发展
2. 自由软件、开源软件与许可证
3. 开源社区与治理
4. 开源开发的基本工程流程
5. 阅读与理解开源项目
6. 参与开源项目
7. AI 辅助的开源开发实践
8. 组织与发布你的开源项目

### 正式材料层

- `Technical Book Manuscript`
- `Student Study Guide`
- `Instructor Guide`
- `Course Syllabus / Course Guide`
- `Appendices`
- `Lab / Project Materials`
- `Case Library`

## 迁移动作定义

为避免“保留 / 不保留”过于粗糙，本文档使用以下动作类型：

- `吸收重写`：保留核心思想，但必须按新结构和新口径重写
- `拆分迁移`：把一个旧文件拆到多个新章节或材料层
- `下沉附录`：不进入正文主干，转入附录、案例或工具材料
- `派生支持层`：不直接进入书稿，而是转化为 Study Guide、Instructor Guide、Course Guide 或实验材料
- `保留为依据`：仅作为历史或设计依据，不作为当前维护产物直接展开

## 矩阵 A：源材料到新结构的映射

| 源材料 | 主要内容簇 | 主要目标章节 | 主要目标层 | 迁移动作 | 优先级 |
| --- | --- | --- | --- | --- | --- |
| `01-overview.md` | 开源定义、常见误解、价值、优缺点、重要性 | 第 1 章、第 2 章 | `Technical Book Manuscript`、`Student Study Guide` | `拆分迁移` + `吸收重写` | P1 |
| `01-overview.md` | 自由软件、开源软件、版权、Copyleft、GPL、MIT、BSD、Apache 等许可证内容 | 第 2 章 | `Technical Book Manuscript`、`Appendices` | `吸收重写` | P1 |
| `02-development-of-open-source-software.md` | 开源历史脉络、关键项目、UNIX / Linux / Web / Android 演进 | 第 1 章 | `Technical Book Manuscript`、`Case Library` | `吸收重写` | P1 |
| `02-development-of-open-source-software.md` | 云计算、AI 平台、未来趋势、商业化推动 | 第 1 章、第 7 章 | `Case Library`、`Appendices`、少量进入书稿 | `拆分迁移` + `下沉附录` | P2 |
| `03-development-models-and-characteristics.md` | 教堂与市集、角色分工、组织结构、社区、基金会 | 第 3 章 | `Technical Book Manuscript`、`Student Study Guide`、`Instructor Guide` | `吸收重写` | P1 |
| `03-development-models-and-characteristics.md` | Git、GitHub、Fork、Branch、Pull Request、基础协作流 | 第 4 章 | `Technical Book Manuscript`、`Appendices`、`Lab / Project Materials` | `拆分迁移` + `吸收重写` | P1 |
| `03-development-models-and-characteristics.md` | 生命周期、测试、实现、版本管理、编码规范 | 第 4 章、第 8 章 | `Technical Book Manuscript`、`Appendices`、`Lab / Project Materials` | `拆分迁移` + `吸收重写` | P1 |
| `03-development-models-and-characteristics.md` | README、FAQ、Wiki、文档工具、文档编制 | 第 5 章、第 8 章 | `Technical Book Manuscript`、`Appendices` | `拆分迁移` | P2 |
| `03-development-models-and-characteristics.md` | 邮件列表、论坛、沟通礼仪 | 第 3 章、第 6 章 | `Technical Book Manuscript`、`Student Study Guide`、`Instructor Guide` | `吸收重写` | P2 |
| `04-participating-in-and-organizing-open-source-projects.md` | 为什么参与开源、什么人适合、如何参与项目 | 第 6 章 | `Technical Book Manuscript`、`Student Study Guide` | `吸收重写` | P1 |
| `04-participating-in-and-organizing-open-source-projects.md` | 如何组织项目、项目规划、发布、基础设施、维护 | 第 8 章、第 3 章 | `Technical Book Manuscript`、`Lab / Project Materials`、`Course Syllabus / Course Guide`、`Instructor Guide` | `拆分迁移` + `吸收重写` | P1 |
| `05-leveraging-open-source-software-resources.md` | 国际基金会、平台、社区、国内外资源入口 | 第 3 章 | `Appendices`、`Case Library`、少量进入书稿 | `下沉附录` | P2 |
| `05-leveraging-open-source-software-resources.md` | 大量开源产品与工具清单 | 无固定正文章 | `Appendices`、`Case Library` | `下沉附录` | P3 |
| `05-leveraging-open-source-software-resources.md` | 国内高校、活动、教育资源 | 第 1 章、第 3 章 | `Student Study Guide`、`Case Library` | `派生支持层` | P3 |
| `06-course-design-for-ai-era-open-source-software-development.md` | 模块设计、实验设计、项目要求、考核建议 | 第 7 章、第 8 章 | `Course Syllabus / Course Guide`、`Lab / Project Materials`、`Instructor Guide` | `派生支持层` | P1 |
| `06-course-design-for-ai-era-open-source-software-development.md` | AI 软件工程管理、AI 与 GitHub 工程流程结合 | 第 7 章 | `Technical Book Manuscript`、`Appendices`、`Instructor Guide` | `吸收重写` | P2 |
| `ref/开源软件开发技术课程实践1-Blog.md` | 环境搭建、文档阅读、简单发布 | 无固定正文章 | `Lab / Project Materials`、`Student Study Guide`、`Instructor Guide` | `派生支持层` | P2 |
| `ref/开源软件开发技术课程实践2-项目分析.md` | 真实项目阅读与分析 | 第 5 章、第 6 章 | `Lab / Project Materials`、`Student Study Guide`、`Instructor Guide`、`Case Library` | `吸收重写` + `派生支持层` | P1 |
| `ref/开源软件开发技术课程实践3-项目建设.md` | 团队立项、项目建设、公开发布 | 第 8 章、第 4 章 | `Lab / Project Materials`、`Course Syllabus / Course Guide`、`Student Study Guide`、`Instructor Guide`、`Case Library` | `吸收重写` + `派生支持层` | P1 |
| `ref/开源软件开发技术_250622/开源软件开发技术（第1部分）_250622.pptx` | 课程导入、课程意义、教学组织 | 无固定正文章 | `Student Study Guide`、`Instructor Guide`、`Course Syllabus / Course Guide` | `派生支持层` | P2 |
| `ref/开源软件开发技术_250622/开源软件开发技术（第2部分）_250622.pptx` | 开源历史、关键人物、基本概念 | 第 1 章、第 2 章 | `Technical Book Manuscript`、`Student Study Guide`、`Instructor Guide`、`Case Library` | `拆分迁移` + `吸收重写` | P1 |
| `ref/开源软件开发技术_250622/开源软件开发技术（第3部分）_250622.pptx` | 开源动机、开发者、商业推动 | 第 1 章、第 3 章 | `Technical Book Manuscript`、`Student Study Guide`、`Instructor Guide` | `拆分迁移` + `吸收重写` | P2 |
| `ref/开源软件开发技术_250622/开源软件开发技术（第4部分）_250630.pptx` | 开源模式、角色、组织、项目管理、生命周期 | 第 3 章、第 4 章 | `Technical Book Manuscript`、`Student Study Guide`、`Instructor Guide` | `拆分迁移` + `吸收重写` | P1 |
| `ref/开源软件开发技术_250622/开源软件开发技术（第5部分）_250630.pptx` | 参与开源项目、社区礼仪、创建开源项目 | 第 6 章、第 8 章 | `Technical Book Manuscript`、`Lab / Project Materials`、`Student Study Guide`、`Instructor Guide` | `拆分迁移` + `吸收重写` | P1 |
| `ref/开源软件开发技术_250622/开源软件开发技术（第6部分）_250630.pptx` | 开源产品、平台与未来趋势 | 无固定正文章 | `Appendices`、`Case Library`、少量进入第 7 章 | `下沉附录` | P3 |
| `ref/开源软件开发技术_250622/GitHub简介_250614.pptx` | Git / GitHub 基础概念、仓库、分支、协作、Flow | 第 4 章、第 5 章 | `Appendices`、`Lab / Project Materials`、`Student Study Guide` | `派生支持层` + `拆分迁移` | P1 |
| `ref/开源软件开发技术_250622/开源软件开发技术课程实践指导书.docx` | 项目分析、项目设计、实践目标与组织方式 | 第 5 章、第 8 章 | `Lab / Project Materials`、`Course Syllabus / Course Guide`、`Instructor Guide` | `派生支持层` + `吸收重写` | P1 |

## 矩阵 B：新章节的组装来源

| 新章 | 主要来源 | 主要吸收内容 | 主要非正文去向 |
| --- | --- | --- | --- |
| 第 1 章 开源的起源与发展 | `02-development-of-open-source-software.md`、`01-overview.md`、`250622 第2部分`、`250622 第3部分` | 历史脉络、关键人物、代表项目、开源的重要性、商业推动的历史背景 | 平台与产品清单下沉到 `Case Library` / `Appendices` |
| 第 2 章 自由软件、开源软件与许可证 | `01-overview.md`、`250622 第2部分` | 自由软件与开源软件关系、常见误解、许可证分类、版权与 Copyleft | 许可证比较表和选择清单下沉到 `Appendices` |
| 第 3 章 开源社区与治理 | `03-development-models-and-characteristics.md`、`04-participating-in-and-organizing-open-source-projects.md`、`05-leveraging-open-source-software-resources.md`、`250622 第4部分`、`250622 第5部分` | 社区结构、角色、治理、礼仪、基金会、组织逻辑 | 平台 / 社区入口和扩展案例进入 `Case Library` / `Appendices` |
| 第 4 章 开源开发的基本工程流程 | `03-development-models-and-characteristics.md`、`250622 第4部分`、`GitHub简介_250614.pptx`、`06-course-design-for-ai-era-open-source-software-development.md` | Git / GitHub 工作流、PR、评审、测试、CI、版本与发布的基本工程机制 | 命令速查、平台操作细节进入 `Appendices` / `Lab / Project Materials` |
| 第 5 章 阅读与理解开源项目 | `ref/开源软件开发技术课程实践2-项目分析.md`、`03-development-models-and-characteristics.md`、`GitHub简介_250614.pptx`、`开源软件开发技术课程实践指导书.docx` | 仓库阅读、README 与关键治理文件理解、项目分析框架 | rubric、模板和示例报告进入 `Lab / Project Materials` / `Instructor Guide` |
| 第 6 章 参与开源项目 | `04-participating-in-and-organizing-open-source-projects.md`、`250622 第5部分`、`ref/开源软件开发技术课程实践2-项目分析.md` | 如何进入社区、如何提出问题、如何贡献文档 / 测试 / 小功能、如何进行首次贡献 | 课堂练习与贡献清单进入 `Study Guide` / `Lab / Project Materials` |
| 第 7 章 AI 辅助的开源开发实践 | `06-course-design-for-ai-era-open-source-software-development.md`、`250622 第4部分`、`250622 第6部分` | AI 辅助阅读项目、补测试、补文档、实现小功能，以及 AI 输出的人工治理 | AI 工具更新快的内容下沉到 `Appendices` / `Instructor Guide` |
| 第 8 章 组织与发布你的开源项目 | `04-participating-in-and-organizing-open-source-projects.md`、`ref/开源软件开发技术课程实践3-项目建设.md`、`250622 第5部分`、`开源软件开发技术课程实践指导书.docx`、`03-development-models-and-characteristics.md` | 项目立项、许可证选择、治理基线、协作机制、文档、版本、发布、复盘 | 项目模板、rubric、阶段交付物进入 `Lab / Project Materials` / `Course Guide` / `Instructor Guide` |

## 暂不直接进入正文主干的内容

以下内容可以保留，但不应优先写入前部稳定正文：

- 纯产品罗列式清单
- 明显依赖具体平台界面的操作步骤
- 过时的托管平台或社区入口
- 以邮件列表为中心、但无法映射到现代 GitHub 协作主线的细节
- 变化过快的 AI 工具功能盘点

这些内容更适合：

- `Appendices`
- `Case Library`
- `Student Study Guide`
- `Instructor Guide`

## 推荐迁移顺序

结合 `textbook-development-workflow-reference.md` 的三轮策略，建议按以下顺序推进：

### 第一轮：建立稳定书稿骨架

优先完成：

1. 第 1 章：主要吸收 `02`、`01` 中的稳定历史与概念材料，以及 `250622 第2部分`
2. 第 2 章：主要吸收 `01` 中的许可证和概念辨析材料
3. 第 3 章：主要吸收 `03` 中的组织与治理材料，以及 `250622 第4-5部分`
4. 第 4 章：主要吸收 `03` 中的工作流和工程机制材料，以及 `GitHub简介`

### 第二轮：建立项目主线章节

优先完成：

5. 第 5 章：以“项目分析”历史实践为核心重构
6. 第 6 章：以“如何参与项目”为主线重构
7. 第 8 章：以“项目建设”历史实践和实践指导书为核心重构

### 第三轮：建立更新较快的层

最后完成：

8. 第 7 章：吸收 `06` 中的 AI 设计思路，并结合最新外部参考重写
9. `Appendices`：吸收 GitHub 工具、命令、模板、平台入口等操作型内容
10. `Case Library`：沉淀项目分析案例、治理案例、学生历史项目案例和技术栈案例

## 当前执行建议

从这个迁移矩阵出发，最合理的下一步不是继续泛泛讨论，而是：

1. 先以第 1 章为样板，建立第一份完整 `Internal Chapter Package`
2. 明确第 1 章应从哪些旧材料中吸收，哪些内容必须丢弃或下沉
3. 在第 1 章跑通后，再按同一方法推进第 2 章、第 3 章和第 4 章

## 结论

当前仓库中的“旧材料”并不是一套应被整体废弃的旧讲义，而是一组需要重新分层、重新定序、重新书写的课程资产。

迁移的关键不是“保留多少旧文字”，而是：

- 保留哪些长期有效的内容骨架
- 把哪些旧内容升级为现代开源开发语境
- 把哪些课堂讲授材料转化为学习支持层和教学支持层
- 把哪些历史实践重构为贯穿课程的项目主线

本文档的作用，就是为这一迁移过程提供一张可以直接执行的总表。

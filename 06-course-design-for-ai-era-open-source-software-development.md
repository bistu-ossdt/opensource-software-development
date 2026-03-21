# AI-Era Open Source Software Development Course Design

## 课程定位

本课程建议将传统的“开源软件开发”课程升级为一门面向 AI 时代的软件工程实践课程：

- 以 GitHub 为核心平台组织开源开发全流程
- 以软件工程方法管理 AI 参与的软件开发
- 以真实仓库、真实协作、真实验证和真实发布为主要教学场景

课程的核心判断应明确写入教学大纲：

> AI 显著提高了代码生成速度，因此更要求学生掌握版本管理、测试、持续集成、代码评审、发布维护和开源协作，用工程化方法约束、验证和集成 AI 的输出。

## 与现有 5 章教材的关系

现有 5 章内容仍然构成课程骨架，但需要重组并补上 AI 软件工程部分。

| 现有章节 | 可保留内容 | 课程重构后的作用 |
| --- | --- | --- |
| Chapter 1 - Overview | 开源概念、误区、优缺点、许可证 | 作为开源基础与许可证模块 |
| Chapter 2 - Development of Open Source Software | 开源发展历程、平台与产业演进 | 作为开源生态与产业背景模块 |
| Chapter 3 - Development Models and Characteristics | 开发模式、Git/GitHub、生命周期、测试、文档 | 作为 GitHub 流程与软件工程基础模块 |
| Chapter 4 - Participating in and Organizing Open Source Projects | 参与方式、组织项目、发布与维护 | 作为社区协作与项目治理模块 |
| Chapter 5 - Leveraging Open Source Software Resources | 社区、平台、镜像、工具与资源 | 作为资源导航与项目选题支持模块 |

课程新增内容主要集中在以下三块：

- AI 辅助开发与代理式开发
- 用软件工程手段管理 AI 生成代码
- AI 时代的安全、合规、供应链与学术诚信

## 课程目标

学生完成课程后，应达到以下目标：

1. 理解开源软件的定义、生态、治理、许可证和商业背景。
2. 掌握以 GitHub 为核心的开源软件开发流程，包括 `Issue -> Branch -> Commit -> Pull Request -> Review -> Merge -> Release`。
3. 掌握开源软件开发中的关键软件工程技术，包括版本管理、测试、CI、代码评审、发布与维护。
4. 能将 AI 编码工具纳入工程流程，而不是绕开工程流程。
5. 能用 GitHub、测试、CI、评审和规则文件管理 AI 生成代码的质量与风险。
6. 能参与已有开源项目，也能组织一个小型开源项目并公开发布。
7. 能识别 AI 开发相关的幻觉、错误传播、依赖风险、许可证风险和数据外泄风险。

## 课程主线

本课程建议围绕三条主线展开。

### 1. 开源协作主线

强调学生要理解并参与真实开源项目，而不是只完成本地个人作业。

核心内容：

- 开源定义、生态与社区
- 许可证、版权、专利和商标
- 贡献流程、社区规范和维护者视角
- 项目治理、文档和发布

### 2. GitHub 软件工程主线

强调学生要掌握 GitHub 为核心的一整套开源开发流程。

核心内容：

- 仓库初始化与项目结构
- `README`、`LICENSE`、`CONTRIBUTING`、`CODE_OF_CONDUCT`
- Git 分支、提交、冲突处理
- Issue、Label、Milestone、Project
- Pull Request、Code Review、Merge 策略
- Release、Tag、Changelog
- GitHub Actions、自动化测试和持续集成

### 3. AI 软件工程主线

强调学生不仅要“会用 AI 写代码”，更要“会用软件工程和开源技术管理 AI 参与的软件开发”。

核心内容：

- AI 编码工具的能力边界
- Prompting 与 Context Engineering
- 代理式开发与异步任务委派
- `AGENTS.md`、`CLAUDE.md`、`.cursor/rules` 等规则配置
- 用测试、CI、Review 和 Release 管理 AI 变更
- AI 失败模式、安全与合规

## 模块设计

### 模块一：开源软件基础与生态

内容：

- 开源软件的定义、发展与价值
- 自由软件与开源软件
- 开源软件的优缺点
- 开源基金会、社区与平台
- 开源商业模式

对应原教材：

- `01-overview.md`
- `02-development-of-open-source-software.md`
- `05-leveraging-open-source-software-resources.md`

教学要求：

- 学生理解为什么现代软件工程越来越依赖开源协作

### 模块二：许可证与开源合规

内容：

- 版权、专利与商标基础
- Copyleft 与 permissive 许可证
- GPL、AGPL、MIT、BSD、Apache 2.0、MPL
- 许可证兼容性
- AI 生成代码的来源、署名与合规

对应原教材：

- `01-overview.md`

教学要求：

- 学生能为课程项目选择合理许可证，并解释原因

### 模块三：GitHub 为核心的开源开发流程

内容：

- Git 与分布式版本管理
- Fork、Clone、Branch、Commit、Push
- Pull Request、Code Review、Merge
- Issue、Label、Milestone、Project Board
- Release、Tag、Changelog
- 仓库权限、保护分支和协作边界

对应原教材：

- `03-development-models-and-characteristics.md`
- `04-participating-in-and-organizing-open-source-projects.md`

教学要求：

- 这一模块是课程操作主线，不是工具介绍附录

### 模块四：开源项目文档、沟通与治理

内容：

- README 编写
- CONTRIBUTING 指南
- CODE_OF_CONDUCT
- Issue / PR 模板
- 路线图、版本规划和发布说明
- 维护者沟通、贡献礼仪和社区组织

对应原教材：

- `03-development-models-and-characteristics.md`
- `04-participating-in-and-organizing-open-source-projects.md`
- `05-leveraging-open-source-software-resources.md`

教学要求：

- 学生理解文档和规则文件是协作系统的一部分

### 模块五：软件工程基础与质量保障

内容：

- 需求分析与任务拆分
- 软件生命周期
- 编码规范与重构
- 单元测试、集成测试、回归测试
- 缺陷跟踪与修复
- 持续集成与持续交付
- 发布、回滚与长期维护

对应原教材：

- `03-development-models-and-characteristics.md`
- `04-participating-in-and-organizing-open-source-projects.md`

教学要求：

- 明确告诉学生：AI 加快编码后，测试、验收和变更管理会更重要

### 模块六：AI 辅助开发基础

内容：

- AI 编程工具类型与能力边界
- Chat、补全、结对协作与代理式执行
- Prompting 与 Context Engineering
- 代码解释、文档生成、测试生成、Bug 定位
- 本地 agent、远程 agent 与 GitHub 集成 agent 的差异

教学要求：

- 学生能比较不同 AI 工具在工程流程中的适用位置

### 模块七：AI 软件工程管理

内容：

- 如何把 AI 纳入 GitHub 工作流
- 用 Issue 明确任务边界
- 用分支和 PR 管理 AI 提交
- 用测试与 CI 拦截低质量改动
- 用 Review 做人工把关
- 用规则文件约束 agent 行为
- 记录 AI 使用过程和验证证据

教学要求：

- 明确课程主张：软件工程和开源技术是管理 AI 开发的手段

### 模块八：安全、合规与供应链

内容：

- 依赖风险与漏洞管理
- Secrets 管理
- 供应链风险和 SBOM 概念
- 提示注入与远程 agent 风险
- GitHub 权限与最小授权
- 学术诚信和来源声明

教学要求：

- 学生能识别 AI 代理自动执行带来的安全与数据外泄风险

### 模块九：综合项目

项目分为两部分：

- 参与型：阅读真实开源项目，提交文档、测试、Bug 修复或小功能 PR
- 建设型：围绕校园或教学需求组织一个小型开源项目并公开发布

项目要求：

- 必须在 GitHub 上完成
- 必须有测试
- 必须有 CI
- 必须有公开文档
- 必须记录 AI 使用方式

## 推荐 16 周教学安排

| 周次 | 主题 | 重点产出 |
| --- | --- | --- |
| 第 1 周 | 课程导入、开源软件概念与价值 | 课程仓库初始化 |
| 第 2 周 | 开源许可证、版权、专利、合规 | 许可证选择说明 |
| 第 3 周 | Git 与 GitHub 基础 | 分支、提交、PR 演练 |
| 第 4 周 | GitHub 协作流程与 Code Review | 完整 PR 流程演练 |
| 第 5 周 | README、CONTRIBUTING、治理文件 | 仓库基础文档 |
| 第 6 周 | 参与开源项目的方法与社区沟通 | 开源项目选题 |
| 第 7 周 | 软件生命周期、需求分析与任务拆分 | 项目需求与 Issue 拆分 |
| 第 8 周 | 编码规范、测试、缺陷修复 | 测试样例与修复流程 |
| 第 9 周 | GitHub Actions 与 CI | 自动化检查流水线 |
| 第 10 周 | 发布、版本管理与维护 | Release / Tag 演练 |
| 第 11 周 | AI 编程工具与协作方式 | AI 工具对比报告 |
| 第 12 周 | Prompting、Context Engineering、Agent 工作流 | 规则文件与 agent 演练 |
| 第 13 周 | AI 结果验证：测试、CI、Review、人工验收 | AI 生成变更验证记录 |
| 第 14 周 | 安全、供应链、权限与学术诚信 | 风险清单与安全检查 |
| 第 15 周 | 项目冲刺与公开展示 | 项目发布候选版 |
| 第 16 周 | 课程答辩与复盘 | 最终仓库、报告与复盘 |

## 实验设计

建议实验全部围绕 GitHub 流程设计，而不是拆成孤立命令练习。

### 实验一：开源仓库初始化

要求：

- 创建 GitHub 仓库
- 配置 `README`
- 配置 `LICENSE`
- 配置 Issue / PR 模板
- 说明仓库目录结构

### 实验二：GitHub Flow 实践

要求：

- 创建一个 Issue
- 基于 Issue 创建分支
- 提交修改
- 发起 Pull Request
- 完成 Review 和合并

### 实验三：测试与 CI

要求：

- 为课程项目增加测试
- 配置 GitHub Actions
- 在 PR 中触发自动检查
- 修复至少一次 CI 失败

### 实验四：AI 辅助开发

要求：

- 使用 AI 辅助完成一个小功能、Bug 修复或测试补全
- 记录 Prompt、规则配置和修改过程
- 对 AI 生成结果进行人工修正
- 提供验证证据

### 实验五：开源贡献

要求：

- 选择一个合适的开源项目
- 阅读贡献指南
- 完成一次有效贡献
- 贡献形式可为文档、测试、修复或小功能

## 课程项目要求

课程项目必须体现以下完整链路：

- 使用 GitHub 管理需求、开发和合并
- 使用测试和 CI 管理质量
- 使用文档和规则管理协作
- 使用 AI 工具辅助开发
- 使用工程化手段控制 AI 的风险
- 完成一次公开发布或可验证的开源贡献

建议每组提交以下成果：

- GitHub 仓库
- `README`
- `LICENSE`
- `CONTRIBUTING`
- Issue 与 PR 记录
- 测试代码
- GitHub Actions 配置
- 一个 Release 或 Tag
- `AI_USAGE.md`
- 一份简短复盘报告

## 考核建议

建议采用过程性考核，不以闭卷考试为主。

| 组成 | 比例 | 重点 |
| --- | --- | --- |
| 理论基础 | 20% | 开源概念、许可证、社区治理、AI 风险边界 |
| 实验成绩 | 30% | GitHub 流程、测试、CI、文档规范 |
| 课程项目 | 40% | 完整开源开发流程、AI 管理能力、项目交付质量 |
| 答辩与复盘 | 10% | 是否真正理解代码、流程、AI 使用和风险 |

建议设置以下验收底线：

- 没有版本管理流程，不合格
- 没有测试和 CI，不得高分
- 不能解释关键代码，不得高分
- 未声明 AI 使用情况，成绩封顶
- 没有 Issue、PR、Review 等协作证据，不视为达成课程目标

## 课程产出物模板

为了降低教师每年重建课程环境的成本，建议统一提供课程模板仓库，至少包括：

- `README.md`
- `LICENSE`
- `CONTRIBUTING.md`
- `CODE_OF_CONDUCT.md`
- `.github/ISSUE_TEMPLATE/`
- `.github/pull_request_template.md`
- `.github/workflows/ci.yml`
- `AI_USAGE.md`
- `AGENTS.md`
- `CLAUDE.md`
- `.cursor/rules/`

## 为什么要把“软件工程管理 AI 开发”作为课程重点

这门课不应把 AI 当作附录工具，而应把它视为新的开发参与者。

原因包括：

1. AI 能加速编码，但不能自动替代需求澄清、验收和质量控制。
2. AI 会放大错误需求、错误上下文和错误模式。
3. AI 生成代码越快，版本管理、测试、Review 和 CI 的价值越高。
4. 真实开源协作中，任何变更都必须经过可追溯的流程，而不是直接接受模型输出。
5. 未来的软件工程岗位，会越来越强调“组织和监督 agent 工作”的能力。

课程中的正式表述可以写成：

> 本课程以 GitHub 为主线，系统教授开源软件协作流程、软件工程方法和 AI 开发管理技术，使学生能够在开放协作和 AI 参与的条件下，完成软件的规范化开发、验证、集成、发布和维护。

## 参考资料

以下参考资料以 2024-2026 年的官方或高相关资料为主，适合用作课程改革依据。

### GitHub

- GitHub, "Survey: The AI wave continues to grow on software development teams," August 20, 2024.  
  https://github.blog/news-insights/research/survey-ai-wave-grows/
- GitHub, "Octoverse: A new developer joins GitHub every second as AI leads TypeScript to #1," October 28, 2025.  
  https://github.blog/news-insights/octoverse/octoverse-a-new-developer-joins-github-every-second-as-ai-leads-typescript-to-1/

### OpenAI

- OpenAI, "Introducing Codex," May 16, 2025.  
  https://openai.com/index/introducing-codex/
- OpenAI, "Codex is now generally available," October 6, 2025.  
  https://openai.com/index/codex-now-generally-available/
- OpenAI, "Harness engineering: leveraging Codex in an agent-first world," February 11, 2026.  
  https://openai.com/index/harness-engineering/
- OpenAI, "How OpenAI uses Codex," November 2025.  
  https://cdn.openai.com/pdf/6a2631dc-783e-479b-b1a4-af0cfbd38630/how-openai-uses-codex.pdf

### Anthropic

- Anthropic, "Claude Code overview," accessed March 18, 2026.  
  https://docs.anthropic.com/en/docs/claude-code/overview
- Anthropic, "Tutorials," accessed March 18, 2026.  
  https://docs.anthropic.com/en/docs/claude-code/tutorials
- Anthropic, "Subagents," accessed March 18, 2026.  
  https://docs.anthropic.com/en/docs/claude-code/sub-agents
- Anthropic, "Claude Code GitHub Actions," accessed March 18, 2026.  
  https://docs.anthropic.com/en/docs/claude-code/github-actions

### Cursor

- Cursor, "Background Agents," accessed March 18, 2026.  
  https://docs.cursor.com/en/background-agents
- Cursor, "GitHub," accessed March 18, 2026.  
  https://docs.cursor.com/en/github
- Cursor, "Rules," accessed March 18, 2026.  
  https://docs.cursor.com/en/context/rules
- Cursor, "Bugbot is out of beta," July 24, 2025.  
  https://cursor.com/en/blog/bugbot-out-of-beta

### AI software engineering ecosystem

- The Modern Software Developer, "The state of AI coding in 2025: Adoption, proficiency, and transformation," December 2025.  
  https://stateof.themodernsoftware.dev/
- ACM CSED, "Generative AI for Computing Education," January 2024.  
  https://csed.acm.org/wp-content/uploads/2024/01/Generative-AI-v1.pdf

## 结论

2026 年的“开源软件开发”课程，不能只停留在“讲开源概念”和“教 GitHub 操作”，也不能变成“教学生用 AI 快速写代码”的工具课。

更合理的课程定位是：

- 以开源协作作为组织形态
- 以 GitHub 作为操作平台
- 以软件工程作为质量控制机制
- 以 AI 作为新的开发参与者

课程最终要培养的，不是单纯更快的编码者，而是能够在开放协作、持续交付和 AI 参与条件下，交付可信软件的工程实践者。

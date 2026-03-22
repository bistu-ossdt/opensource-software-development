# 第四章内部章节包（骨架版）

> 当前状态：Round 1 骨架草案。本文档用于第四章的结构设计、旧材料迁移和后续定向研究，不是书稿正文。

## 章节信息

- 章节编号：第 4 章
- 中文标题：开源开发的基本工程流程
- 英文标题：`Core Engineering Workflow of Open Source Development`
- 英文短标识：`engineering-workflow`
- 章节视角：参与者 / 阅读者视角
- 当前目标：先建立流程主线骨架，再据此进行定向研究和正文写作

## 本章定位

本章承接第三章的社区与治理，从“谁来协作、如何治理”继续推进到“修改如何被提出、审查、验证并进入主线”。如果说第三章回答的是“开源社区如何持续运作”，那么第四章回答的是“开源项目如何把公共协作落到可执行、可检查的工程流程中”。

本章主要解决五个问题：

1. 为什么现代开源项目需要明确的变更流程，而不是允许所有人直接改动主线
2. `Issue`、Branch、Commit、Pull Request、Review、Merge 在开源工程中分别承担什么作用
3. 为什么测试、CI、状态检查和规则门禁属于协作流程的一部分，而不是发布前附加动作
4. 为什么现代开源工程需要把依赖、密钥和自动化权限纳入日常流程
5. 为什么“可合并”与“可发布”之间还存在版本、变更记录和发布完整性这层要求

本章不承担项目健康度评估、外部项目参与沟通、项目治理文件设计和项目创建发布策略。这些内容分别在第 5、6、8 章展开。

本章与前后章节的关系：

- 与第 3 章的关系：第 3 章解释为什么需要治理，本章解释治理如何在工程流程中落实
- 与第 5 章的关系：本章介绍工程流程零件，第 5 章介绍如何把这些零件整合为项目级判断
- 与第 6 章的关系：本章解释流程本身，第 6 章解释贡献者如何实际进入并完成一次贡献
- 与第 8 章的关系：本章从参与者视角理解流程，第 8 章从维护者视角设计项目仓库、发布与维护机制

## 本章学习目标（Learning Objectives）

学完本章后，学生原则上应能够：

- 解释为什么开源项目通常采用 branch-based change flow，而不是直接修改默认分支
- 说明 `Issue`、Branch、Commit、Pull Request、Review、Merge 在协作中的基本关系
- 读懂一个项目的最小 CI / 检查门禁，并理解状态检查对合并的作用
- 理解 `CODEOWNERS`、rulesets / branch protection、required checks 等机制为什么会影响变更进入主线
- 识别依赖审查、secret scanning、push protection 等现代工程安全基线的基本意义

## 本章边界

### 本章必须讲清的内容

- 变更控制与默认分支稳定性的关系
- `Issue`、Branch、Commit、Pull Request、Review、Merge 的主线逻辑
- 测试、CI、状态检查和自动化门禁的基本作用
- `CODEOWNERS`、rulesets / branch protection 的工程意义
- 基本安全流程：依赖、密钥、自动化权限、发布完整性

### 本章不展开的内容

- Git 命令逐条教学
- 平台界面按钮和菜单路径
- 外部项目第一次贡献的沟通细节
- 复杂的供应链标准与企业级合规流程
- 项目从零初始化和长期发布维护策略

### 应下沉的内容

- Git / GitHub 操作命令速查：转附录
- 具体 PR 模板、Actions YAML 示例、ruleset 示例：转附录 / 实验
- 复杂 merge queue、artifact attestations、SBOM 实操：正文点到，细节转扩展层或附录
- 平台功能差异与套餐边界：不进入正文主干

## 基线层与扩展层

### Baseline

- Git 的分支与合并模型对协作的意义
- `Issue`、Branch、Commit、Pull Request、Review、Merge 的基本协作流
- 测试、CI、状态检查和必需审批的作用
- 基本安全意识：依赖、密钥、最小权限自动化
- 版本、变更记录与发布的最小工程概念

### Stretch

- `CODEOWNERS`、rulesets、required workflows
- dependency review、secret scanning、push protection 的组织化使用
- merge queue、required merge methods、stale review dismissal
- SBOM、artifact attestations、provenance
- OpenSSF Scorecard、OSPS Baseline 等外部基线

## 旧材料迁移映射

| 来源 | 可用内容 | 当前判断 | 本章用途 |
| --- | --- | --- | --- |
| `03-development-models-and-characteristics.md` 旧版 | Git、GitHub、Fork、Branch、Pull Request、生命周期、测试、发布 | `本章核心来源之一` | 吸收流程骨架，但必须大幅重写并去除按钮式教程 |
| `03-development-models-and-characteristics.md` 旧版 | 编码规范、README、文档工具、命名规范 | `后移` | 主体转附录或第 8 章 |
| `04-participating-in-and-organizing-open-source-projects.md` 旧版 | 参与项目、组织项目、透明与开放 | `拆分吸收` | 与流程直接相关的少量内容进入本章，其余后移 |
| `06-course-design-for-ai-era-open-source-software-development.md` | GitHub-centered workflow、AI 输出管理、CI 与流程管理 | `部分吸收` | 用于修正本章对现代流程的理解，但不进入 AI 主线 |
| `250622 第 4 部分 PPT` | 生命周期、测试、版本、项目管理 | `本章核心来源之一` | 用于重建旧材料中的流程与质量控制逻辑 |
| `GitHub简介_250614.pptx` | 仓库、分支、协作流、PR | `本章核心来源之一` | 只吸收稳定流程抽象，不复用平台界面讲解 |
| `modern-open-source-development-best-practices-reference.md` | PR 门禁、CI、安全、供应链完整性 | `当前内部参考` | 用于补足现代工程基线 |

## 正文主叙述结构（骨架版）

建议第四章正文采用 5 个一级小节。

### Opening / 开场切入

建议的开场问题：

- 为什么很多项目宁可让默认分支被规则“卡住”，也不允许任何人直接把代码推上去？
- 为什么 Linux 用 patch 流，GitHub 用 Pull Request 流，二者却都在解决同一个工程问题？

当前建议：从“修改如何进入主线”切入，用 Linux patch flow 和现代 PR flow 的共同工程目标建立问题意识。

### 第一节：流程不是官僚负担，而是变更控制

本节要解决的问题：

- 为什么开源项目不能只靠善意合并修改
- 默认分支稳定性为什么重要
- 为什么工程流程是治理在技术层的延伸

### 第二节：从工作项到变更集

本节要解决的问题：

- `Issue`、Branch、Commit 各自是什么
- 为什么 Git 的 branching model 适合开源协作
- fork model 与 shared repository model 分别适合什么场景

### 第三节：Pull Request、Review 与 Merge

本节要解决的问题：

- Pull Request 为什么是“可审查的修改提案”
- review 如何影响合并
- `CODEOWNERS`、required reviews、merge methods、rulesets 如何影响主线

### 第四节：测试、CI 与自动化门禁

本节要解决的问题：

- 为什么 CI 不只是“跑测试”
- status checks 如何把质量要求前置到合并前
- workflow 为什么是仓库中的工程政策文件

### 第五节：安全与发布基线

本节要解决的问题：

- 为什么依赖、密钥和自动化权限必须进入日常流程
- dependency review、secret scanning、push protection 的基本意义
- 为什么版本、变更记录、SBOM / attestations 属于更高阶但连续的发布基线

## 本章的明确取舍

### 直接保留的内容骨架

- 变更控制的主线
- branch-based workflow 与可审查变更
- review、checks、merge 之间的关系
- 测试、CI、安全门禁的流程意义

### 必须重写的地方

- 旧稿中的 GitHub 注册、安装、分支创建按钮说明
- 旧稿把生命周期、测试、发布、编码规范混写在一起的结构
- 旧稿对流程的“平台步骤化”表达
- 旧稿对现代安全与供应链基线覆盖不足的问题

### 不进入本章正文的旧内容

- 逐步图解式平台操作教程
- 大量命令清单
- 文档排版工具与命名规范
- 项目选题、组织与发布策略

## 核心术语表（Key Terms）

| 中文术语 | 英文原词 | 推荐表达 | 一句话解释 | 本章语境 |
| --- | --- | --- | --- | --- |
| 默认分支 | `Default Branch` | 默认分支 | 仓库的主线分支，通常要求保持稳定和可集成状态 | 流程主线 |
| 工作项 | `Issue` | 工作项 / Issue | 用于记录缺陷、任务、需求或讨论入口的可执行条目 | 变更起点 |
| 分支 | `Branch` | 分支 | 承载一组相对独立修改的开发线 | 变更隔离 |
| 提交 | `Commit` | 提交 | 一组有边界、有说明的历史记录单元 | 变更单元 |
| 拉取请求 | `Pull Request` | Pull Request | 对一组修改发起讨论、审查和合并请求的协作对象 | 变更提案 |
| 代码评审 | `Code Review` | 代码评审 / Review | 对修改进行技术判断、反馈和批准的过程 | 合并门禁 |
| 状态检查 | `Status Check` | 状态检查 | 对提交或 Pull Request 进行自动化验证后的状态结果 | 自动化门禁 |
| 工作流 | `Workflow` | 工作流 | 仓库中定义的自动化过程配置 | CI 基础 |
| 规则集 | `Ruleset` | 规则集 | 对分支或标签应用的可配置规则集合 | 流程门禁 |
| 代码所有者 | `CODEOWNERS` | 代码所有者 / `CODEOWNERS` | 为路径指定默认评审责任人的机制 | 审核责任 |
| 依赖审查 | `Dependency Review` | 依赖审查 | 在 Pull Request 中检查依赖变化及其风险的机制 | 安全基线 |
| 密钥扫描 | `Secret Scanning` | 密钥扫描 | 检测仓库历史和协作内容中暴露凭据的机制 | 安全基线 |
| 推送保护 | `Push Protection` | 推送保护 | 在推送时拦截潜在密钥泄露的机制 | 安全基线 |
| 软件物料清单 | `Software Bill of Materials` | 软件物料清单（SBOM） | 描述构件依赖组成的清单 | 发布完整性 |
| 构件证明 | `Artifact Attestation` | 构件证明 / Attestation | 用于证明构件如何生成和来自哪里的可验证元数据 | 发布完整性 |

## 案例接口（Case Mapping）

### 正文核心案例

- 案例 1：Git 的 branching model
- 案例 2：Linux 的 patch lifecycle 与 maintainer flow
- 案例 3：GitHub Flow 与 PR-based collaboration

### 案例用途

- 案例 1：说明为什么分支和合并是低成本变更控制手段
- 案例 2：说明 PR 并不是唯一形式，但“可审查变更进入主线”是共同问题
- 案例 3：说明现代仓库如何把变更控制、评审和检查集成到日常流程

## Appendix Mapping

本章需要但不应写入正文主干的附录支持包括：

- Git / GitHub 命令速查
- 最小 Pull Request 模板
- 最小 CI workflow 示例
- ruleset / branch protection / `CODEOWNERS` 示例
- merge strategy 对照表

## Study Guide Mapping

本章对应的 `Student Study Guide` 应至少覆盖：

- 阅读顺序建议：先抓“为什么需要流程”，再抓 `Issue -> Branch -> Commit -> PR -> Review -> Merge`
- 常见误区：
  - 分支只是备份
  - Pull Request 只是提交通道
  - CI 只是跑单元测试
  - 安全检查是发布前再看
- 与团队项目主线的连接提醒：
  - 团队仓库从本章开始必须真正使用 Issue、Branch、PR、Review 和 CI
  - 流程证据本身就是项目质量的一部分

## Instructor Guide Mapping

本章对应的 `Instructor Guide` 应至少覆盖：

- 教学重点：
  - 把流程理解为变更控制，而不是平台功能清单
  - 区分治理文件和工程门禁的不同作用
  - 让实验和仓库记录成为本章最直接的证据
- 易错点：
  - 把 Git 命令教学误当作本章主体
  - 把 Linux patch flow 与 GitHub PR flow 对立化
  - 把 CI 缩减成“自动跑测试”

## Lab Mapping

本章主要连接：

- `实验 4：GitHub 协作流与最小 CI`

本章在实验体系中的作用：

- 把团队协作从“能提交代码”升级为“能按规则推进变更”
- 让自动化检查真正进入日常协作

建议实验接口：

- 基础项：
  - 使用 Issue 驱动至少一轮开发
  - 所有成员通过 Branch 和 PR 提交变更
  - 完成至少一轮 Review 和修改
  - 配置最小 CI
- 提升项：
  - 增加 `CODEOWNERS`、rulesets 或 dependency review
  - 增加 secret scanning / push protection 说明
  - 增加 changelog 或版本标签

## 本章可评价证据（Assessment Evidence）

本章可对应的评价证据包括：

- Issue 记录
- Branch / Commit / Pull Request 记录
- Review 记录
- CI 运行结果
- 最小版本或 changelog 记录

## 参考来源（当前阶段）

### 内部来源

- `00-preface.md`
- `chapter-specification-reference.md`
- `chapter-baseline-and-stretch-blueprint-reference.md`
- `legacy-content-to-new-course-structure-migration-matrix-reference.md`
- `03-development-models-and-characteristics.md` 旧版
- `04-participating-in-and-organizing-open-source-projects.md` 旧版
- `modern-open-source-development-best-practices-reference.md`

### 后续需要外部核查的核心来源类型

- Git 官方关于 branching and merging 的材料
- GitHub Docs 关于 GitHub Flow、Pull Request、reviews、status checks、rulesets、`CODEOWNERS`
- GitHub Docs 关于 dependency review、secret scanning、push protection、Actions security
- GitHub Docs 关于 SBOM 和 artifact attestations

## 待定向研究的问题清单

### 必核查

- GitHub Flow 的最小稳定表述应如何写
- Pull Request、Review、rulesets、`CODEOWNERS` 的最小关系如何准确表达
- CI、status checks、required checks 的关系如何简化而不失真
- dependency review、secret scanning、push protection 的基线地位应如何写
- SBOM / attestations 在本章中应保留到什么粒度

### 需决定的写作问题

- 第四章开场是否直接使用 Linux patch flow 与 PR flow 对照
- release 是否在正文中单列一节，还是并入安全与发布基线
- fork model 是否在正文中展开，还是点到为止

## 下一步

本章下一步不应直接停留在骨架，而应继续完成：

1. 第四章定向研究
2. 第四章书稿提纲
3. 第四章书稿正文初稿

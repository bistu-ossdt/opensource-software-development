# 第四章《开源开发的基本工程流程》书稿提纲（草案）

> 当前状态：基于内部章节包与定向研究形成的书稿提纲草案。本文档用于进入正式章节写作前的结构收敛，不替代最终书稿正文。

## 开场段（草案）

一个开源项目公开接受贡献，但默认分支却被规则“保护”起来：不能直接推送，修改必须先经过分支、Pull Request、Review 和检查门禁。很多刚接触开源的人会觉得这有些矛盾，既然项目鼓励协作，为什么不让修改更直接地进入主线？可只要看一眼经典项目，就会明白这恰恰是开放协作能够成立的条件。Linux 用公开补丁流和维护者链条控制代码进入主线，今天的平台化仓库更多使用 branch-based workflow 和 Pull Request 流程；工具不同，但它们都在解决同一个问题：怎样让修改被隔离、被审查、被验证，然后再进入公共代码线。本章要讨论的，正是这种工程流程如何成为开源协作的日常骨架。

## 本章将回答的问题（Questions This Chapter Answers）

- 为什么开源项目需要明确的变更控制，而不是直接修改默认分支？
- `Issue`、Branch、Commit、Pull Request、Review、Merge 在工程流程中分别承担什么作用？
- 为什么测试、CI 和状态检查必须发生在合并前？
- `CODEOWNERS`、rulesets / branch protection 为什么会改变一个项目的协作方式？
- 为什么依赖、密钥、自动化权限和发布完整性也应纳入工程流程？

## 正文主线

本章建议采用 5 个一级小节。

## 1. 工程流程不是官僚负担，而是变更控制

### 本节目标

先建立主命题：流程不是为了拖慢协作，而是为了让默认分支保持可集成、可审查和可追溯。

### 本节核心论点

- 开源的公开性提高了协作机会，也提高了主线被破坏的风险
- 工程流程的目标是控制“修改如何进入主线”
- Linux patch flow 和 PR flow 的差别不应遮蔽它们的共同工程问题

### 本节建议写入的内容

- 默认分支稳定性
- “修改提案”与“最终主线”之间必须有缓冲区
- 治理如何在技术层变成门禁

## 2. 从工作项到变更集：Issue、Branch 与 Commit

### 本节目标

说明流程的前半段怎样把模糊工作变成可处理的工程对象。

### 本节核心论点

- `Issue` 把工作从聊天变成可追踪条目
- Branch 把一组修改从默认分支隔离出来
- Commit 是有边界、可回滚、可说明的历史单元

### 本节建议写入的内容

- Git 的 branching model
- 分支应围绕一组相对独立修改
- 提交粒度与提交信息
- shared repository model 与 fork-and-pull model 的最小区分

## 3. Pull Request、Review 与 Merge：让修改变成可判断对象

### 本节目标

把 Pull Request 写成流程核心对象，而不是平台动作。

### 本节核心论点

- Pull Request 是变更提案、讨论空间和审查记录的结合
- review 让技术判断和合并条件显性化
- rulesets、required reviews、`CODEOWNERS` 让这些规则可执行

### 本节建议写入的内容

- GitHub Flow 的最小主线
- comment / approve / request changes
- `CODEOWNERS`
- required reviews、resolved conversations、merge methods

## 4. 测试、CI 与自动化门禁

### 本节目标

说明自动化检查为什么不是可选配件，而是现代开源流程的一部分。

### 本节核心论点

- CI 的基本作用是把质量要求前置到合并前
- workflow 是仓库中的自动化政策文件
- required status checks 把“应该检查”变成“未通过就不能合并”

### 本节建议写入的内容

- workflow 的基本定义
- build、lint、test、static analysis 作为常见检查
- status checks 与 required checks
- 为什么“合并前失败”比“发布后补救”更重要

## 5. 安全与发布基线：依赖、密钥与可验证发布

### 本节目标

把现代流程扩展到依赖、安全和发布完整性，但保持粒度可控。

### 本节核心论点

- 依赖变化本身就是安全事件
- 密钥泄露不能只靠人工自觉预防
- 自动化权限和发布构件同样需要被治理

### 本节建议写入的内容

- dependency review
- secret scanning 与 push protection
- least privilege automation
- 版本、变更记录、SBOM、artifact attestations 的最小关系

### 本节收束功能

- 为第 5 章项目级阅读提供流程维度
- 为第 6 章第一次贡献提供操作前提
- 为第 8 章项目维护者视角提供发布基线

## 贯穿案例设计

### 开场案例

- Linux patch flow 与 PR-based flow 的对照

### 中段案例

- Git 的 branching model
- GitHub Flow
- `CODEOWNERS` / rulesets / required checks 作为现代仓库机制

### 案例使用原则

- 不写平台点击步骤
- 不把 GitHub 平台特性误写成开源流程的唯一形式
- 经典案例与现代平台机制要在“共同工程问题”上对齐

## 本章的章节节奏建议

### 开头

- 从“为什么主线不能被直接改动”制造问题意识
- 迅速提出“流程就是变更控制”这一主命题

### 中段

- 先写 Issue / Branch / Commit
- 再写 Pull Request / Review / Merge
- 然后写 CI 与自动化门禁

### 结尾

- 把流程收束到安全与发布基线
- 自然转入下一章的项目阅读与判断

## 本章当前写作禁区

- 不能把本章写成 Git 命令入门
- 不能把本章写成 GitHub UI 教程
- 不能把 Linux patch flow 与 PR flow 二选一化
- 不能把 CI 压缩成“自动跑测试”
- 不能把安全问题全部拖到发布阶段

## 本章小结（预期方向）

本章的小结应明确指出：现代开源开发的核心，不是“每个人都能直接修改公共代码”，而是“每一组修改都要经过隔离、说明、审查、验证和整合”。Branch、Commit、Pull Request、Review、Checks、Rules 这些对象之所以重要，并不是因为平台要求，而是因为它们共同构成了变更控制体系。理解了这条主线，读者才会知道为什么一次贡献不仅是“写出代码”，还包括把修改包装成可理解、可审查、可验证、可合并的工程对象。

## 下一步

在这份提纲基础上，下一步应进入：

1. 第四章书稿正文初稿
2. Linux patch flow 与 PR flow 开场段的正式写法
3. 第四章与第 5、6、8 章接口的收束

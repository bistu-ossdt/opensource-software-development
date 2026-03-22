# 第四章定向研究参考

## 目的

本文档用于支撑第四章《开源开发的基本工程流程》的后续正文写作。它只处理第四章必须核查的协作流程、评审门禁、自动化检查、安全流程和发布完整性基线，不扩展到平台界面教学或企业级 DevSecOps 细节。

本轮研究的目标不是把 GitHub 产品功能讲全，而是为第四章建立一套准确、稳定、能够经受一段时间考验的工程流程写作基础。

## 研究范围

本轮只核查以下问题：

- Git 的 branching model 为什么适合开源协作
- GitHub Flow 对 branch-based collaboration 的最小稳定表述是什么
- Pull Request、Review、status checks、rulesets、`CODEOWNERS` 的最小关系应如何表达
- workflow、CI、required checks 为什么属于工程流程而不是发布前附加动作
- dependency review、secret scanning、push protection 的基线意义是什么
- SBOM 与 artifact attestations 在本章中应保留到什么粒度

## 已核查的关键结论

### 1. Git 的 branching model 是现代协作流程的基础条件之一

Git 官方关于 branching and merging 的介绍长期强调：分支允许开发者为每组修改建立独立的开发线，再在准备好之后合并回主线。其重要性不在于“分支这个命令本身”，而在于它让隔离修改、并行工作和回到主线的成本都足够低。

写作含义：

- 第四章不应把 branch 写成命令技巧，而应写成“低成本隔离修改”的工程手段
- 这也是为什么 branch-based workflow 能成为现代开源协作基线

来源：

- Git, *Branching and Merging*  
  <https://git-scm.com/about/branching-and-merging.html>

### 2. GitHub Flow 的稳定核心是“轻量、分支化、以 Pull Request 为中心”

GitHub 官方文档明确把 GitHub Flow 定义为 lightweight, branch-based workflow，并给出一条稳定主线：

- 为每组不相关修改创建独立分支
- 通过 Pull Request 请求反馈
- 在 Pull Request 中继续提交和讨论
- 通过批准、检查和冲突处理后再合并
- 合并后删除分支

写作含义：

- 第四章可以用 GitHub Flow 作为现代 PR-based collaboration 的最小稳定表达
- 但不能把它写成所有项目唯一正确流程，因为 Linux 等经典项目仍有 patch-based flow
- 更准确的写法是：GitHub Flow 是今天平台化仓库中最常见的分支协作抽象之一

来源：

- GitHub Docs, *GitHub flow*  
  <https://docs.github.com/en/get-started/using-github/github-flow>

### 3. Pull Request 的关键不只是“提交通道”，而是“可审查的变更对象”

GitHub 官方文档和 Pull Request 说明都强调：

- Pull Request 是在两个分支之间提出变更建议的协作对象
- 它保留提交历史、评论历史和 review 历史
- review 是 GitHub 上最主要的协作方式之一

写作含义：

- 第四章应把 Pull Request 写成“变更提案 + 讨论空间 + 审查记录”
- 这比把 Pull Request 写成“提交代码的地方”更准确

来源：

- GitHub Docs, *GitHub flow*  
  <https://docs.github.com/en/get-started/using-github/github-flow>
- GitHub Docs, *About pull requests*  
  <https://docs.github.com/en/pull-requests/collaborating-with-pull-requests/proposing-changes-to-your-work-with-pull-requests/about-pull-requests>
- GitHub Docs, *About pull request reviews*  
  <https://docs.github.com/en/pull-requests/collaborating-with-pull-requests/reviewing-changes-in-pull-requests/about-pull-request-reviews>

### 4. Review 的稳定最小结构是 comment / approve / request changes

GitHub Docs 当前将 review 的三种基本状态稳定表述为：

- Comment
- Approve
- Request changes

同时，required reviews 可以与 rulesets 或 protected branches 配合使用，从而把“请求修改”变成真正的合并门禁。

写作含义：

- 第四章不应把 review 写成礼貌性反馈
- 更准确的写法是：review 是把技术判断和合并门禁显式化的机制

来源：

- GitHub Docs, *About pull request reviews*  
  <https://docs.github.com/en/pull-requests/collaborating-with-pull-requests/reviewing-changes-in-pull-requests/about-pull-request-reviews>

### 5. rulesets / branch protection 的核心作用是把“规则”变成“不能绕过的门禁”

GitHub 关于 rulesets 的说明明确表明，项目可以要求：

- 通过 Pull Request 才能进入目标分支
- 必需审批数量
- code owner 审批
- stale review dismissal
- 解决所有评论后才可合并
- 指定 merge method

写作含义：

- 第四章可以把 rulesets / protected branches 写成“治理在工程层的强制执行”
- 关键不是配置细节，而是它们把“建议流程”变成“可执行政策”

来源：

- GitHub Docs, *Available rules for rulesets*  
  <https://docs.github.com/en/repositories/configuring-branches-and-merges-in-your-repository/managing-rulesets/available-rules-for-rulesets>

### 6. `CODEOWNERS` 解决的是“谁应当看哪些修改”

GitHub Docs 明确指出：

- 当 Pull Request 修改了某段已有 code owner 的代码时，code owners 会被自动请求 review
- 如果项目启用了 required code owner review，则这类 Pull Request 在获得 code owner 批准前不能合并

写作含义：

- 第四章不应把 `CODEOWNERS` 写成单纯联系人列表
- 更准确的写法是：`CODEOWNERS` 是把评审责任映射到路径级别的机制

来源：

- GitHub Docs, *About code owners*  
  <https://docs.github.com/en/repositories/managing-your-repositorys-settings-and-features/customizing-your-repository/about-code-owners>

### 7. CI 的稳定最小表述应是“仓库中的自动化政策执行”

GitHub Docs 当前对 workflow 的定义很适合作为教材表述：

- workflow 是 configurable automated process
- workflow 用仓库中的 YAML 文件定义
- workflow 由事件触发，可以运行一个或多个 job

GitHub 关于 status checks 的文档则进一步说明：

- status checks 来自外部过程，如 CI builds
- 如果 status checks 被设为 required，则未通过前不能合并到 protected branch

写作含义：

- 第四章可以把 CI 写成“仓库中的自动化过程”，而不只是“自动跑单元测试”
- 状态检查之所以重要，是因为它们把测试、lint、build、审计等要求前置到合并前

来源：

- GitHub Docs, *Workflows*  
  <https://docs.github.com/en/actions/concepts/workflows-and-actions/workflows>
- GitHub Docs, *About status checks*  
  <https://docs.github.com/articles/about-statuses>

### 8. dependency review 让依赖风险进入 Pull Request 级别

GitHub Docs 当前对 dependency review 的说明很明确：

- 它帮助理解每个 Pull Request 中依赖变化及其安全影响
- 能显示依赖新增、删除、更新及其漏洞信息
- dependency review action 可以作为 required workflow，阻止引入有风险依赖的 Pull Request 合并

写作含义：

- 第四章应把 dependency review 写成“依赖变化进入合并前审查”的机制
- 这比在发布后再补漏洞修复更符合现代流程基线

来源：

- GitHub Docs, *About dependency review*  
  <https://docs.github.com/en/code-security/concepts/supply-chain-security/about-dependency-review>

### 9. secret scanning 与 push protection 把密钥泄露从“事后发现”推进到“事前拦截”

GitHub Docs 对两者的区分非常清楚：

- secret scanning 会扫描整个 Git 历史及 Issues、PR、Discussions 等协作内容中的暴露凭据
- push protection 会在 push 过程中阻止潜在秘密进入仓库

写作含义：

- 第四章可把它们写成“发现型控制”和“预防型控制”的连续关系
- 这有助于读者理解为什么“不提交密钥”已经不是纯手工习惯，而是可以被工程化支持的流程要求

来源：

- GitHub Docs, *About secret scanning*  
  <https://docs.github.com/en/code-security/concepts/secret-security/about-secret-scanning>
- GitHub Docs, *About push protection*  
  <https://docs.github.com/en/code-security/concepts/secret-security/about-push-protection>

### 10. 自动化权限必须遵循 least privilege

GitHub 的 workflow 安全文档明确提醒：

- 任何拥有仓库写权限的人都能读取配置在仓库中的全部 secrets
- 因此 workflow 中使用的 credentials 应保持 least privileges required

写作含义：

- 第四章不应把自动化写成“越强越方便”
- 更准确的写法是：自动化本身也是需要受限的协作者

来源：

- GitHub Docs, *Secure use reference*  
  <https://docs.github.com/en/actions/reference/security/secure-use>

### 11. SBOM 与 artifact attestations 已经构成更高阶但连续的发布完整性方向

GitHub 关于 artifact attestations 的文档表明：

- attestation 用于证明构件在哪里、如何被构建
- workflow 中可以为 SBOM 生成 attestation
- 这些证明还可以被验证

写作含义：

- 第四章可以把 SBOM 和 attestation 写成“发布完整性的进阶方向”
- 但不必在正文中深讲具体操作，应放到扩展层和附录接口

来源：

- GitHub Docs, *Using artifact attestations to establish provenance for builds*  
  <https://docs.github.com/en/actions/how-tos/secure-your-work/use-artifact-attestations/use-artifact-attestations>

## 对旧材料的直接修正建议

基于本轮研究，第四章在迁移旧材料时应直接做以下修正：

### 应删除或避免直接复用的说法

- “GitHub 流程主要就是注册账号、创建仓库、点按钮提 PR”
- “CI 基本等于自动跑测试”
- “安全问题等到发布前统一检查”
- “分支只是临时备份”
- “review 只是礼貌性帮助”

### 应改成更稳妥的写法

- 工程流程的核心是变更控制
- 分支用于隔离修改，Pull Request 用于提出和审查变更
- review、rulesets、required checks 共同决定哪些修改可以进入主线
- workflow 是仓库中的自动化政策文件
- 依赖、密钥和自动化权限都应进入合并前流程

## 对第四章写法的具体建议

基于本轮研究，第四章正文建议采用以下叙述节奏：

1. 从“为什么不能直接改主线”切入  
   用 Linux patch flow 和 PR flow 的共同工程目标建立问题意识。

2. 先讲分支与变更单元  
   说明 `Issue`、Branch、Commit 为什么是流程零件。

3. 再讲 Pull Request、Review、Merge  
   把 review 与门禁显式连起来。

4. 再讲 CI 与自动化检查  
   把 workflow、checks、required checks 写成流程内建要求。

5. 最后讲安全与发布基线  
   把 dependency review、secret scanning、push protection、SBOM / attestation 放在“连续加强的基线”上理解。

## 当前仍可延后的问题

以下问题可以延后到正文修订阶段，不必阻塞第四章起稿：

- merge queue 是否进入正文还是仅进扩展层
- 是否在正文中展开 fork model 与 shared repo model 的比较
- SBOM 和 attestation 在附录中用 GitHub 还是更中性示例

## 当前结论

第四章已经具备进入书稿提纲写作和正文重写的条件。

本轮研究最大的作用是把第四章最容易写成“按钮教程”的部分重新固定为更稳定的工程结构：

- 分支不是命令技巧，而是变更隔离机制
- Pull Request 不是提交入口，而是可审查变更对象
- CI 不只是测试，而是自动化政策执行
- 安全和发布完整性已经进入日常流程，而不只是发布前附属动作

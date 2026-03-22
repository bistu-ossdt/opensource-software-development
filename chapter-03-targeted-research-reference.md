# 第三章定向研究参考

## 目的

本文档用于支撑第三章《开源社区与治理》的后续正文写作。它只处理第三章必须核查的治理概念、经典治理案例、治理文件和社区健康基线，不扩展到 GitHub 操作教学、CI 配置或 AI 辅助开发实践。

本轮研究的目标不是把所有治理模式都讲完，而是为第三章建立一套准确、稳定、适合前四章“经典内容”定位的写作基础。

## 研究范围

本轮只核查以下问题：

- 为什么治理应被视为开源开发技术的基础组成部分，而不是社区文化的附属话题
- Linux 的维护者体系和补丁流转应如何准确表述
- Apache 的 PMC、meritocracy 和公开协作机制应如何准确表述
- Python 的正式治理结构能提供什么补充视角
- `CONTRIBUTING.md`、`CODE_OF_CONDUCT.md`、`SECURITY.md`、Issue / PR 模板等文件在现代仓库中的稳定作用是什么
- 社区健康、维护者可持续性和企业参与透明度应如何在本科生层面稳定表达

本轮刻意不把 `OpenClaw` 纳入第三章案例主线。按照当前案例定位原则，第三章只使用经典、长期稳定的治理案例。

## 已核查的关键结论

### 1. 治理不是“软性文化补充”，而是公共协作的运行机制

Open Source Guides 的治理资料明确指出，项目应该把治理写下来，而不是把它留在维护者脑中。典型治理内容包括：

- 角色与责任
- 决策过程
- 投票或共识规则
- 权限如何获得和失去
- 争议如何处理

写作含义：

- 第三章不能把治理写成“大家友好合作”的文化描述
- 更准确的写法应是：治理回答“谁可以做什么、如何做决定、出了冲突怎么办”

来源：

- Open Source Guides, *Leadership and Governance*  
  <https://opensource.guide/leadership-and-governance/>

### 2. Linux 适合用来说明“维护者链条”与“主线合并”的经典治理路径

Linux kernel 官方开发过程文档给出了一种非常稳定的表述：

- Linux 开发者群体由用户、贡献者、维护者以及 Linus Torvalds 组成
- 补丁通常不是直接提交给 Linus，而是沿维护者层级逐步向上合并
- 这种结构依赖“信任链”（chain of trust）而不是单一扁平协作

官方文档还强调，邮件列表在内核社区中仍是关键协作媒介，补丁和讨论需要发送到正确的公开列表并抄送相关人员。

写作含义：

- 第三章可以把 Linux 写成“开放但高度组织化”的代表案例
- 应避免旧稿那种“人人平等、自由参与”式浪漫化叙述
- 更准确的写法是：Linux 的开放性依赖公开流程、角色梯度和长期形成的信任结构

来源：

- Linux kernel documentation, *The kernel development process*  
  <https://docs.kernel.org/process/development-process.html>
- Linux kernel documentation, *How the development process works*  
  <https://docs.kernel.org/process/2.Process.html>

### 3. Apache 适合用来说明“社区化治理”与“项目管理委员会”路径

Apache Software Foundation 的官方说明提供了非常适合教材使用的经典结构：

- Apache 强调 community over code
- 其组织逻辑通常经历 user -> developer -> committer -> PMC member 的成长路径
- PMC（Project Management Committee）负责项目方向、发布和社区健康
- Apache 的 meritocracy 不是抽象口号，而是“基于持续贡献获得更高信任与责任”

Apache 还明确强调异步公开沟通的重要性：邮件列表是项目的虚拟会议室，异步协作适应全球志愿者的时区和参与节奏，并保留可归档记录。

写作含义：

- 第三章可以用 Apache 对照 Linux，说明开源治理并不只有一种形态
- 旧材料中的 PMC 结构不应被写成所有开源项目的标准答案，而应被写成一种经典路径
- “meritocracy” 应写成“持续贡献带来责任上升”，而不是“精英主义神话”

来源：

- Apache Software Foundation, *How the ASF Works*  
  <https://www.apache.org/foundation/how-it-works/>

### 4. Python 适合补充“成熟项目的正式治理”视角

Python 的 PEP 13 提供了一个非常稳定的正式治理案例：

- Python 由 core team 选举产生 5 人 steering council
- steering council 的职责包括维护语言和 CPython 的质量与稳定性、维持健康包容的社区、在必要时充当最终裁决者
- 为避免单一公司控制，PEP 13 明确规定同一雇主最多只能有 2 名 steering council 成员

写作含义：

- 第三章可以把 Python 作为“成熟语言社区正式治理”的辅助案例
- 这非常适合用来说明：治理不仅关心技术路线，也关心权力边界、冲突处理和利益平衡

来源：

- Python Enhancement Proposals, *PEP 13 – Python Language Governance*  
  <https://peps.python.org/pep-0013/>

### 5. 公开、异步、可归档沟通不是历史偶然，而是开源规模化协作的基本条件

Open Source Guides 和 Apache 官方文档都强调：

- 重大讨论应尽量发生在公开、可搜索、可归档的渠道中
- 私下消息不适合作为普通项目协作的主要媒介
- 异步沟通能让后来者补上上下文，也能降低私人 gatekeeping

Linux 文档则把这一点落得更具体：补丁和审查需要进入公共列表和公共记录，而不是只在私聊中完成。

写作含义：

- 第三章应把邮件列表、论坛、Discussions、Issue、PR 评论写成“治理媒介”，而不是简单工具清单
- 旧稿中“早期用邮件列表，现在用各种平台”的叙述太弱，应升级为“公开记录如何支撑公共协作”

来源：

- Open Source Guides, *Leadership and Governance*  
  <https://opensource.guide/leadership-and-governance/>
- Apache Software Foundation, *How the ASF Works*  
  <https://www.apache.org/foundation/how-it-works/>
- Linux kernel documentation, *How the development process works*  
  <https://docs.kernel.org/process/2.Process.html>

### 6. `CONTRIBUTING.md`、`CODE_OF_CONDUCT.md`、Issue / PR 模板、`SECURITY.md` 已经构成现代仓库治理的最小入口集合

GitHub 官方关于 public repository community profile 的文档把一组文件明确列为项目健康协作的重要组成部分：

- `README`
- `CODE_OF_CONDUCT`
- `CONTRIBUTING`
- `LICENSE`
- Issue templates
- Pull request template
- `SECURITY.md`

这些文件并不是平台装饰，而是让陌生贡献者知道“项目是什么、如何进入、行为边界在哪里、漏洞该如何私下报告”的基本入口。

写作含义：

- 第三章可以把这些文件写成“现代仓库治理入口”
- 但不应在第三章展开平台点击步骤；第三章只解释它们的治理意义

来源：

- GitHub Docs, *About community profiles for public repositories*  
  <https://docs.github.com/en/communities/setting-up-your-project-for-healthy-contributions/about-community-profiles-for-public-repositories?apiVersion=2022-11-28>

### 7. 行为准则的关键不只是“写出来”，而是有报告和执行路径

Open Source Guides 关于行为准则的文档明确指出，项目不应只停留在一份象征性文本上。好的行为准则至少要包含：

- 预期行为
- 报告渠道
- 执行责任
- 后果与补救路径

写作含义：

- 第三章不能把 `CODE_OF_CONDUCT.md` 写成“礼貌倡议”
- 更准确的写法是：行为准则属于治理，因为它规定了社区冲突和伤害事件如何被处理

来源：

- Open Source Guides, *Your Code of Conduct*  
  <https://opensource.guide/code-of-conduct/>

### 8. 社区健康不能只看 star 数，更要看响应、留存和维护负担

Open Source Guides 关于指标的文档明确建议，项目不应只看 popularity，还应观察：

- 项目活动度
- 贡献者数量与变化
- Issue / Pull Request 的响应与关闭情况
- 参与者是否持续留下来

CHAOSS 则提供了专门面向开源社区健康的指标体系。

写作含义：

- 第三章可以把社区健康讲成“可持续性问题”，而不是“项目热不热”
- 对本科生来说，不需要深入指标公式，但应建立“star != 健康”的基本判断

来源：

- Open Source Guides, *Gathering Community Metrics*  
  <https://opensource.guide/metrics/>
- CHAOSS  
  <https://chaoss.community/>

### 9. 企业参与不是例外，关键问题是透明度、权力边界和长期可持续性

Apache 的组织实践和 Python 的治理约束都说明：

- 企业参与在成熟开源项目中很常见
- 真正重要的不是“有没有公司”，而是公司影响是否透明、治理结构是否允许单一雇主过度控制

写作含义：

- 第三章不应把企业参与写成开源的“污染”
- 也不应把企业支持简单写成“天然有利”
- 更稳妥的表达是：企业参与需要被治理机制约束和公开化

来源：

- Apache Software Foundation, *How the ASF Works*  
  <https://www.apache.org/foundation/how-it-works/>
- Python Enhancement Proposals, *PEP 13 – Python Language Governance*  
  <https://peps.python.org/pep-0013/>

## 对旧材料的直接修正建议

基于本轮研究，第三章在迁移旧材料时应直接做以下修正：

### 应删除或避免直接复用的说法

- “只要代码公开，社区自然会形成”
- “集市模型已经足够解释今天的开源治理”
- “所有开源项目都应设置 PMC”
- “邮件列表只是历史上的旧工具，如今已无治理意义”
- “行为规范主要依靠大家自觉”
- “项目热度高就代表社区健康”

### 应改成更稳妥的写法

- 开源社区是公开协作共同体，不是代码附属物
- 治理是角色、流程、权力边界与冲突处理的安排
- Linux 代表维护者链条与主线合并路径
- Apache 代表社区化治理、meritocracy 与 PMC 路径
- Python 代表成熟项目的正式治理与利益约束
- GitHub 仓库中的治理文件是现代治理入口，而不是装饰文件

## 对第三章写法的具体建议

基于本轮研究，第三章正文建议采用以下叙述节奏：

1. 从“开源并不等于无组织协作”切入  
   用 Linux 和 Apache 的对照建立问题意识。

2. 先讲社区为何不是代码附属物  
   让读者理解治理为什么是公共协作的基础。

3. 再讲角色、路径与权力边界  
   用 Linux、Apache、Python 三种经典路径建立基本认知。

4. 再讲公开、异步、可归档沟通与治理文件  
   把邮件列表、Issue、PR 评论、`CONTRIBUTING.md`、`CODE_OF_CONDUCT.md` 等放到同一治理框架中理解。

5. 最后收束到社区健康与可持续性  
   把维护者负担、响应速度、留存、企业参与透明度作为治理的长期问题提出。

## 当前仍可延后的问题

以下问题可以延后到正文修订阶段，不必阻塞第三章起稿：

- 是否在正文中引入 Jupyter 或 Kubernetes 作为补充案例
- 是否在第三章正文中加入单独的“治理模式对照表”
- GitHub Discussions 是否在第三章正文中出现，还是放到第 4 章或附录
- CHAOSS 具体指标在教材中展开到什么程度

## 当前结论

第三章已经具备进入书稿提纲写作和正文重写的条件。

本轮研究最大的作用是把第三章最容易写散、写旧、写浅的几个点固定下来：

- 治理不是文化装饰，而是协作基础设施
- 经典开源项目并不“无组织”，而是通过角色梯度和公共记录运行
- 治理文件、行为准则和社区健康都属于开源开发技术的一部分
- 前四章完全可以只用经典案例把治理讲清楚，不必依赖现代 AI-native 项目

下一步可以据此把第三章推进为书稿提纲与正文初稿，而不是继续停留在旧材料拆分阶段。

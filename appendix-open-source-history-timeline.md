# 附录 开源历史关键事件时间线

这一附录把开源历史中的关键节点按时间顺序重新排开。它不试图写成一份百科全表，而是帮助读者看清几条长期稳定的主线：软件如何从共享实践走向独立商品，GNU 与自由软件如何把问题正式提出，“open source” 如何成为公共语言，分布式协作与平台化如何改变工程实践，以及安全、供应链、治理与 AI 压力如何重塑当代开源。

与正文第一章相比，这里更强调历史定位功能，而不是完整叙事。读者可以把它当作一张时间轴索引，在需要回看某个年份、事件或阶段时快速定位。

## 1. 编写说明

本附录的事件选择遵循四个原则：

- 优先选择改变开源概念、制度、治理、协作基础设施或工程实践的历史转折点，而不是简单罗列著名项目的版本发布史。
- 尽量使用项目、基金会、组织或标准文本的官方材料，并与 Wikipedia 条目交叉校对后再纳入。
- 对近年的内容保持克制：截至 `2026-03-22`，本附录优先收录已经表现出较明确历史意义的 `2020-2025` 节点，不把尚未沉淀为稳定判断的短期新闻直接写进时间线。
- 这条时间线关注的是“开源软件历史中的代表性事件”，因此会兼顾自由软件、开源、基金会、平台、治理、安全与基础设施，而不局限于某一个项目家族。

## 2. 共享传统、软件独立化与问题形成

| 时间 | 事件 | 涉及人物 / 项目 | 为什么重要 | 关联章节 |
| --- | --- | --- | --- | --- |
| 20 世纪 50 年代中期 | 早期用户组织与软件共享传统逐步形成 | SHARE、大学与研究机构 | 说明软件最初经常伴随硬件、研究合作与用户社群一同流动，源代码共享首先是一种工程现实，而不是后来的制度运动。 | 第 1 章 |
| `1969` | IBM 在反垄断压力下推动软件与硬件、服务分离销售 | IBM | 软件逐渐被明确为可独立定价和控制的对象，这一转变加速了软件商品化，也为后来自由软件与开源争论提供了现实背景。 | 第 1 章 |
| `1969` 前后 | UNIX 在 Bell Labs 形成并扩散 | Ken Thompson、Dennis Ritchie、UNIX | UNIX 传统深刻影响了后来开源世界中的系统观、工具链文化与可移植环境，是理解开源技术文化背景的重要起点。 | 第 1 章 |
| `1973` | UNIX 以 C 语言重写 | UNIX、C | 让系统更容易移植和传播，也强化了“代码可读、可移植、可组合”的工程传统。 | 第 1 章 |
| `1976` | 《An Open Letter to Hobbyists》发表 | Bill Gates、Altair BASIC | 把软件复制、收费与专业劳动回报问题公开化，象征软件商品化和复制控制逻辑进一步成形。 | 第 1 章 |

这一阶段最值得记住的不是“那时已经有开源”，而是软件最初常常处在共享传统之中，随后才逐步被商品化、封闭化和许可证化。开源历史，正是在这一转折压力下被逼出来的。

## 3. GNU、FSF、GPL 与自由软件制度成形

| 时间 | 事件 | 涉及人物 / 项目 | 为什么重要 | 关联章节 |
| --- | --- | --- | --- | --- |
| `1983-09-27` | GNU 项目初始公告发布 | Richard Stallman、GNU | 把“自由软件系统”从分散不满转化为明确的系统建设计划。GNU 的意义不在于几个独立程序，而在于它从一开始就指向完整操作系统环境。 | 第 1-2 章 |
| `1984-01` | GNU 项目实际启动 | Richard Stallman、GNU | 说明 GNU 已从公开宣言进入持续工程建设阶段。 | 第 1 章 |
| `1985` | Free Software Foundation 成立 | Richard Stallman、FSF | 自由软件运动开始以更稳定的组织形式推进，具备了制度化与持续倡导能力。 | 第 1-2 章 |
| `1985` | 《GNU Manifesto》发布 | Richard Stallman、GNU | 让“软件自由”从技术选择上升为伦理与制度问题，是理解自由软件传统的核心文献之一。 | 第 1-2 章 |
| `1989` | GNU GPL 发布 | GNU、FSF、GPL | 为自由软件的传播、修改与再分发建立了影响极其深远的许可证框架，也让 Copyleft 变成可操作制度。 | 第 2 章 |
| `1989` | BSD Networking Release 1（Net/1）发布 | BSD、加州大学伯克利分校 | 标志着另一条重要传统逐渐清晰：除 Copyleft 之外，宽松许可证与 BSD 系谱也成为开源世界的重要制度来源。 | 第 2 章 |
| `1991` | Linux 内核启动 | Linus Torvalds、Linux | 让自由软件系统在内核层面取得关键突破。GNU 提出了系统目标，Linux 补上了关键系统部件。 | 第 1 章 |
| `1992` | Linux 转向 GNU GPL | Linux、GPL | 强化了 GNU 与 Linux 之间的制度联系，也让 GNU/Linux 组合具备更完整的自由软件系统意义。 | 第 1-2 章 |
| `1993` | Debian 项目启动 | Ian Murdock、Debian | 展示大型自由软件发行版如何通过公开制度、角色分工与长期维护持续发展。 | 第 2-3 章 |
| `1994` | `USL v. BSDi` 争议基本收束 | BSD、USL、BSDi | 这一法律节点让 BSD 系谱重新获得更明确的发展空间，也提醒人们许可证与代码来源问题会长期影响开源生态。 | 第 2 章 |

这一阶段的核心历史意义，是“问题被正式提出来了”。软件自由不再只是工程师之间的默契，而开始成为围绕使用、研究、修改与再分发权利展开的系统性制度问题。同时，GPL 与 BSD 两条传统也逐步形成了后来开源许可证生态中的两大重要方向。

## 4. “Open Source”命名、Web 扩散与基金会化

| 时间 | 事件 | 涉及人物 / 项目 | 为什么重要 | 关联章节 |
| --- | --- | --- | --- | --- |
| `1995` 前后 | Apache HTTP Server 逐渐成型并成为 Web 基础设施 | Apache Group、Apache | 展示了开放协作如何从补丁流发展为稳定项目，也预示了后来的基金会化与长期治理。 | 第 1、3 章 |
| `1997` | 《大教堂与集市》广泛传播 | Eric S. Raymond | 为开放式开发模式提供了极具影响力的公共叙述，使开源更容易被理解为一种有效的协作方式，而不仅是政治立场。 | 第 1、3 章 |
| `1998-01` | Netscape 开放浏览器源码 | Netscape、Mozilla | 让开放源码进入更广泛的企业与公共讨论空间，成为“开源能否进入主流产业视野”的代表性事件。 | 第 1 章 |
| `1998-02` | “open source” 术语提出并迅速传播 | Christine Peterson、OSI 早期推动者 | 为一套已经存在的实践提供了更易传播的公共语言，显著改变了开源进入产业与媒体语境的方式。 | 第 1 章 |
| `1998-02` | Open Source Initiative 成立并推动 Open Source Definition | Bruce Perens、Eric S. Raymond、OSI | 让“什么算开源”具备更明确的制度标准，也让开源倡导获得更稳定的组织载体。 | 第 1-2 章 |
| `1999-06` | Apache Software Foundation 成立 | Apache、ASF | 象征开源项目从协作群体走向基金会化与长期治理。开源不再只是“代码开放”，而开始更明确地关心组织连续性。 | 第 1、3 章 |
| `2003-07` | Mozilla Foundation 成立 | Mozilla、Mitchell Baker | 表明大型开放源码项目开始采用更稳定的公共组织结构，把产品、社区、治理与公共性进一步整合起来。 | 第 1、3 章 |
| `2004-11` | Firefox 1.0 发布并进入大众视野 | Mozilla、Firefox | 证明开放源码产品可以在面向普通用户的软件竞争中形成广泛影响，开源不再只属于服务器和开发者圈层。 | 第 1 章 |

这一阶段最重要的变化，是“开源”从自由软件历史中的一组实践与理念，转变为具有公共命名、组织载体、基金会与产业传播能力的更大框架。此后，开源进入了真正意义上的全球公共讨论。

## 5. 分布式协作、平台化与基础设施开源

| 时间 | 事件 | 涉及人物 / 项目 | 为什么重要 | 关联章节 |
| --- | --- | --- | --- | --- |
| `2003` | `SCO v. IBM` 诉讼把 Linux 合法性争议推入公共视野 | SCO、IBM、Linux | 说明开源已不再是边缘爱好者实践，而是足以引发大型法律与产业博弈的基础设施对象。 | 第 2、3 章 |
| `2005` | Git 诞生 | Linus Torvalds、Git | 为大规模分布式协作提供新的版本控制基础设施。Git 的出现，使并行分支、公开历史与大规模合并流程更可持续。 | 第 4 章 |
| `2007` | GPLv3 发布 | FSF、GPL | 反映自由软件许可证在数字版权管理、专利与分发环境变化下继续演化，说明许可证治理不是一次性完成的。 | 第 2 章 |
| `2008` | GitHub 上线 | GitHub | 把仓库、Issue、Pull Request、Review 与 Release 更集中地放入同一平台，显著降低了全球协作门槛，也改变了后来一代开发者参与开源的入口。 | 第 1、4、6 章 |
| `2014` | Kubernetes 作为开源项目发布 | Google、Kubernetes | 标志着开源进一步进入云基础设施与平台编排层，开源不再只是“使用某个库”，而是成为现代计算基础设施的默认组成部分。 | 第 4、8 章 |
| `2015` | Cloud Native Computing Foundation（CNCF）成立 | Linux Foundation、CNCF | 说明大型基础设施开源项目正通过基金会化与生态协作进入新的成熟阶段。 | 第 3、8 章 |
| `2018` | Microsoft 收购 GitHub | Microsoft、GitHub | 这一并购具有强烈象征意义：曾长期与自由软件阵营冲突的公司，最终收购了全球最重要的开源协作平台之一，说明开源已经从边缘文化走向现代软件基础设施。 | 第 1、4 章 |

这一阶段可以概括为三个关键词：分布式协作、平台化、基础设施化。Git 改变了协作方法，GitHub 改变了参与入口，而云原生基金会与基础设施项目则让开源进一步成为现代计算环境的底层默认设置。

## 6. 安全、供应链、治理与 AI 时代的新压力

| 时间 | 事件 | 涉及人物 / 项目 | 为什么重要 | 关联章节 |
| --- | --- | --- | --- | --- |
| `2014` | Heartbleed 公开披露 | OpenSSL | 让大量人意识到关键开源基础设施的维护脆弱性与安全外部性。开源安全因此不再只是单个项目的问题，而成为整个生态必须面对的公共问题。 | 第 4、8 章 |
| `2018-07` | Guido van Rossum 宣布退出 Python 的 BDFL 角色 | Guido van Rossum、Python | 这是成熟开源项目治理转型的重要案例，说明大型项目迟早需要把个人权威转化为更可继承的公共结构。 | 第 3 章 |
| `2019` | `PEP 13` 确立 Python 的 Steering Council 治理结构 | Python | 代表开源项目治理成熟化的一个清楚节点。它显示治理不是附属话题，而是项目可持续性的基础组成部分。 | 第 3 章 |
| `2020-08-03` | OpenSSF 成立 | Linux Foundation、OpenSSF | 标志着开源安全开始以更系统的跨组织方式被推进，其官方起点本身就与 Heartbleed 之后的长期安全压力有关。 | 第 4、8 章 |
| `2021-12` | Log4Shell 暴露依赖与供应链风险 | Log4j | 进一步放大了依赖治理、可见性与供应链风险在现代开源中的重要性，也使 SBOM、来源证明与可验证发布获得更现实的紧迫性。 | 第 4、8 章 |
| `2025-03` | OpenInfra Foundation 完成加入 Linux Foundation 的过程 | OpenInfra Foundation、Linux Foundation | 体现出在云基础设施、AI 与安全压力之下，大型开源基金会和生态正在进一步整合。 | 第 3、8 章 |
| `2025-09` | 多家基金会和基础设施组织联合强调“Open Infrastructure Is Not Free” | OpenSSF、OpenJS Foundation、Python Software Foundation 等 | 说明到 2025 年，开源讨论的重点已不再只是“是否开放”，而是“谁长期维护、谁承担成本、谁对公共基础设施持续投入”。 | 第 3、8 章 |
| `2025` | GitHub `Octoverse 2025` 显示 AI 项目与 coding agents 已深度影响开源生态 | GitHub、vLLM、Ollama、Continue 等 | 这不是单一产品发布，而是一个更有历史意义的生态信号：AI 基础设施项目、agent 参与贡献与新开发者增长正在共同改写开源协作图景。 | 第 7-8 章 |

到这一阶段，开源已经不再适合被理解成“公开仓库 + 接收贡献”的简单模型。安全、依赖、供应链、基金会协作、维护劳动与 AI 辅助开发，已经共同构成现代开源开发的现实压力。也正因为如此，今天讲“开源软件开发技术”，不能只讲许可证和 Git，还必须讲治理、安全、责任链与可持续维护。

## 7. 到 2026 年的历史判断

截至 `2026-03-22`，已经足够清晰、可以写进历史附录的趋势主要集中在三个方向：

- 开源安全与供应链治理已从“附加主题”上升为生态级基础议题。
- 基金会、项目治理与可持续维护，已经从社区文化问题转变为工程与制度问题。
- AI 正在显著改变开源项目的增长速度、协作入口与工程门槛，但并没有取消测试、评审、发布与人工责任链的重要性。

这意味着，若把 1980-1990 年代看作“概念与制度形成期”，把 2000-2010 年代看作“平台化与基础设施扩展期”，那么 2020 年代正在逐步表现为“安全、供应链、治理与 AI 压力共同塑造开源工程”的新阶段。

需要特别说明的是：`2026` 仍在进行中，因此本附录没有勉强设置一个“2026 年标志性事件”来追求形式上的完整，而是把当前已经稳定可见的历史判断写在这里，作为时间线的暂时收束点。

## 8. 本附录的主要编写依据

本附录优先使用官方历史材料与 Wikipedia 交叉校对。以下为本次详细扩写时重点参考的来源：

- GNU Project, “Initial Announcement”  
  https://www.gnu.org/gnu/initial-announcement.en.html
- Free Software Foundation, “FSF History”  
  https://www.fsf.org/history/
- Open Source Initiative, “History of the Open Source Initiative”  
  https://opensource.org/about/history-of-the-open-source-initiative
- Apache Software Foundation, “ASF History”  
  https://www.apache.org/history/
- Mozilla, “History of the Mozilla Project”  
  https://www-archive.mozilla.org/about/history
- Git, “A Short History of Git”  
  https://git-scm.com/book/en/v2/Getting-Started-A-Short-History-of-Git
- GitHub Blog, “Only the beginning”  
  https://github.blog/news-insights/the-library/only-the-beginning/
- CNCF, “Who We Are”  
  https://www.cncf.io/about/who-we-are/
- OpenSSF, “Technology and Enterprise Leaders Combine Efforts to Improve Open Source Security”  
  https://openssf.org/press-release/2020/08/03/technology-and-enterprise-leaders-combine-efforts-to-improve-open-source-security/
- OpenSSF, “Open Infrastructure Is Not Free: A Joint Statement on Sustainable Stewardship”  
  https://openssf.org/blog/2025/09/22/open-infrastructure-is-not-free-a-joint-statement-on-sustainable-stewardship/
- Linux Foundation / OpenInfra official 2025 merger announcements  
  https://www.linuxfoundation.org/press/open-infrastructure-foundation-board-announces-intent-to-join-the-linux-foundation  
  https://openinfra.org/blog/openinfra-joins-linux-foundation/
- GitHub Blog, “Octoverse 2025”  
  https://github.blog/news-insights/octoverse/octoverse-a-new-developer-joins-github-every-second-as-ai-leads-typescript-to-1/
- Wikipedia, “History of free and open-source software”  
  https://en.wikipedia.org/wiki/History_of_free_and_open-source_software
- Wikipedia, “Timeline of free and open-source software”  
  https://en.wikipedia.org/wiki/Timeline_of_free_and_open-source_software
- Wikipedia, “History of Unix”  
  https://en.wikipedia.org/wiki/History_of_Unix
- Wikipedia, “Berkeley Software Distribution”  
  https://en.wikipedia.org/wiki/Berkeley_Software_Distribution
- Wikipedia, “Heartbleed”  
  https://en.wikipedia.org/wiki/Heartbleed
- Wikipedia, “Log4Shell”  
  https://en.wikipedia.org/wiki/Log4Shell

## 9. 使用方式

这条时间线最适合回答四个问题：

- 某个概念、组织或项目大致处在开源历史的哪个阶段？
- 一个今天看起来理所当然的开源实践，是在什么历史压力下形成的？
- 为什么开源史不能只讲许可证或项目发布，而必须同时讲基金会、治理、安全与平台？
- 到 2026 年为止，哪些近年变化已经足够稳定，值得进入“历史附录”而不是只停留在新闻层面？

如果读者希望知道某个时间点背后对应的是谁在推动、哪些项目在承载，可以回到“附录 开源人物-事件-项目对照表”；如果读者希望从某个人物的持续贡献出发理解其历史位置，则可继续阅读“附录 开源人物谱”。

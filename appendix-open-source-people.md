# 附录 开源人物

本附录按“人物”而不是按“年份”来组织开源历史。它不试图做成名人榜，也不追求把所有重要开发者一网打尽，而是选择那些已经在开源历史中形成稳定地位、能够帮助读者理解概念、制度、项目、平台与维护逻辑的人物。

与“附录 开源历史”相比，这里更强调持续贡献；与“附录 开源对照表”相比，这里更强调人物的历史位置与长期影响。

## 1. 编写说明

- 本附录不是“最伟大程序员”排名，而是“开源历史中的代表性人物”索引。
- 入选标准主要看四类长期影响：技术传统、概念与命名、许可证与制度、项目治理与维护方法。
- 史实优先采用官方历史材料、项目组织材料与公开可核查文本，再与 Wikipedia 交叉校对。
- 史实核查截点为 `2026-03-23`。对仍在持续活动的人物，本附录只写已经形成稳定历史判断的部分。
- 本附录把自由软件与开源放在一条连续历史线上处理。原因不是要抹平两者差异，而是因为许多后来被归入“开源”历史核心位置的人物，本来就是在自由软件制度、许可证和公共论辩中形成影响力的。
- 开源人工智能相关人物不在这里展开；那部分内容原则上放在“附录 开源人工智能”中单独处理。
- 个别人物并不是开源倡导者本人，而是作为历史对照出现，例如 Bill Gates。他们之所以入选，是因为其公开立场帮助我们更清楚地看见开源问题是如何被逼出来的。

## 2. 技术传统与问题提出者

### Ken Thompson

- 代表项目 / 组织：UNIX、Bell Labs
- 关键时期：`1969-1973`

Ken Thompson 是 UNIX 的共同创建者之一。对开源史而言，他的重要性不只在于写出了一个著名系统，更在于 UNIX 所代表的工程传统后来深刻影响了开源世界：小工具组合、清晰接口、面向程序员的工作环境，以及把系统视为可不断演进的代码共同体。很多后来的开源项目并不是直接继承 Thompson 的代码，而是继承了 UNIX 这种系统观。

如果说自由软件和开源是在 1980 年代以后才被正式命名，那么 Ken Thompson 所处的 UNIX 传统说明，开源并不是凭空出现的。它有更早的技术文化背景，而 Thompson 正是这条背景线上的关键人物。

### Dennis Ritchie

- 代表项目 / 组织：UNIX、C、Bell Labs
- 关键时期：`1969-1973`

Dennis Ritchie 与 Ken Thompson 共同奠定了 UNIX 世界，其中最有历史分量的一点，是他让 UNIX 与 C 语言形成了长期联动。`1973` 年前后以 C 重写 UNIX，使系统具备更强的可移植性，这为后来跨硬件、跨机构传播的软件文化提供了非常重要的技术条件。

开源世界长期强调“源代码可读、可移植、可修改”，这并不只是许可证问题，也与 Ritchie 所推动的语言和系统传统有关。今天我们回看 Linux、BSD、Git、编译器工具链乃至许多现代基础设施项目，仍能看到这条技术谱系的深远影响。

### Bill Gates

- 代表项目 / 组织：Altair BASIC、Microsoft 早期
- 关键时期：`1976`

Bill Gates 并不是开源运动人物，但他在开源历史中仍有明确位置。`1976` 年的《An Open Letter to Hobbyists》把一个后来反复出现的问题公开化了：软件是否应当像其他商品一样被复制控制、收费和封闭分发。这个文本常被视为软件商品化逻辑的公开表达之一。

因此，Bill Gates 在本附录中的位置是“历史对照人物”。他提醒我们，开源并不是单纯因为“分享很美好”而出现的，而是在软件逐步变成独立商品、源代码逐步失去默认共享地位之后，才被重新组织为一种制度性回应。

## 3. 自由软件与开源制度奠基者

### Richard Stallman

- 代表项目 / 组织：GNU、FSF、GPL
- 关键时期：`1983-1989`

Richard Stallman 是理解整个开源历史时绕不过去的人物。`1983-09-27`，他发布 GNU 项目初始公告；`1985`，Free Software Foundation 成立；随后 GNU Manifesto、GNU Emacs、GCC 与 GNU GPL 等一系列成果，逐步把“软件自由”从工程师之间的习惯，提升为明确的伦理、法律和组织问题。

即使后来“open source”这一表述在产业与媒体中更流行，Stallman 的历史地位也并未因此被取代。原因很简单：没有 GNU、FSF、GPL 与 copyleft 的制度基础，后来关于开源定义、许可证兼容性、社区权利和用户自由的很多讨论都不会以今天的方式展开。

### Bruce Perens

- 代表项目 / 组织：Debian、OSI、Open Source Definition
- 关键时期：`1997-1998`

Bruce Perens 的关键贡献在于把原本分散的自由软件原则，转化为更可操作、可传播的制度文本。`1997` 年的 Debian Free Software Guidelines（DFSG）后来成为 Open Source Definition 的直接基础；`1998` 年，他与 Eric S. Raymond 共同创建 Open Source Initiative（OSI），使“开源”第一次拥有了稳定的定义组织与公共倡导平台。

Perens 的重要性还在于，他把“什么算开源”从一种模糊态度，推进为一套可以讨论、可以审核、可以落到许可证实践中的标准。这条线一直延续到今天的 OSI 审核、许可证争议和“source available 不等于 open source”的边界判断之中。

### Eric S. Raymond

- 代表项目 / 组织：《大教堂与集市》、OSI
- 关键时期：`1997-1998`

Eric S. Raymond 的历史地位主要不在某一个基础设施项目，而在于他为开源开发模式提供了一套极其有传播力的公共叙述。`1997` 年的《大教堂与集市》把开放协作、快速反馈和分布式改进讲成了一种可以被企业、媒体和普通开发者理解的开发方法论。后来 Netscape 源码开放与 OSI 的形成，都与这套叙述进入公共讨论空间密切相关。

Raymond 的作用可以概括为“解释者”。他没有发明开源协作，但他帮助更多人把这种协作看成一种有效的软件生产方式，而不仅是少数黑客的文化偏好。开源能够在 1998 年之后迅速进入主流产业话语，与他的传播作用有直接关系。

### Christine Peterson

- 代表项目 / 组织：Foresight Institute、OSI 历史语境
- 关键时期：`1998-02`

Christine Peterson 不是典型意义上的开源项目维护者，但她在开源历史中的位置非常稳固：`1998-02-03`，在 Palo Alto 的一次策略会议上，她提出了 “open source” 这一术语。OSI 官方历史明确把这一命名归因于她。

这件事的重要性不在“谁想出了一个词”这么简单，而在于命名改变了公共传播的入口。相较于 “free software”，`open source` 更容易进入企业、媒体和政府语境，也更容易把注意力放到开放开发过程、协作效率和制度可用性上。Peterson 说明了一件事：在开源史中，语言本身也是基础设施。

### Eben Moglen

- 代表项目 / 组织：FSF、GPLv3、Software Freedom Law Center（SFLC）
- 关键时期：`1994-2007`

Eben Moglen 在本附录中承担的是“法律架构推动者”的角色。他长期担任 Free Software Foundation 的总法律顾问，并深度参与 GNU GPL 的执行与 GPLv3 的起草讨论。相比 Stallman 更偏向理念与运动起点、Perens 更偏向定义与制度边界，Moglen 的代表性在于：他把自由软件与开源世界中最关键的一部分制度问题，真正推进到了可执行、可辩护、可在现实争议中落地的法律层面。

`2005` 年成立的 Software Freedom Law Center 进一步说明，开源世界不只需要开发者和维护者，也需要能够长期处理许可证执行、合规争议与公共法律基础设施的人。把 Moglen 补进这份附录，有助于避免把开源史误写成只有程序员、项目创始人与平台公司的历史。

### Ian Murdock

- 代表项目 / 组织：Debian
- 关键时期：`1993-1996`

Ian Murdock 是 Debian 项目的创建者。`1993` 年，他以“公开、协作、面向社区”的方式发起 Debian，并在随后写下 Debian Manifesto。Debian 的意义不只是又一个 Linux 发行版，而是它较早地展示了一种非常有代表性的开源组织形态：公开邀请贡献者、强调制度化角色分工、依赖社区协作完成长期维护。

如果说 GNU 提出了目标、Linux 提供了关键内核，那么 Debian 则让人们更清楚地看到，一个大型自由软件系统如何被组织、打包、维护并长期延续。后来的 Ubuntu 等大量发行版、包管理习惯和社区治理经验，都与 Debian 的制度实践有直接关系。

## 4. 项目、平台与公共组织塑造者

### Linus Torvalds

- 代表项目 / 组织：Linux、Git
- 关键时期：`1991`、`2005`

Linus Torvalds 是开源历史中最具标志性的人物之一。`1991` 年 Linux 内核启动，使自由软件世界在系统内核层面获得关键突破；`2005` 年 Git 的诞生，则改变了后续二十年几乎整个开源世界的协作方式。单就历史连续性而言，很少有人同时在“系统构建”和“协作基础设施”两个层面都留下如此深的影响。

Torvalds 的另一层重要性，在于他所代表的务实工程风格。Linux 内核的维护者体系、分层合并、公开邮件列表讨论和对代码质量的强烈关注，构成了现代大型开源项目治理的经典范式之一。很多项目未必复制 Linux 的文化，但几乎都会面对 Linux 率先解决过的规模化维护问题。

### Brian Behlendorf

- 代表项目 / 组织：Apache、ASF、CollabNet
- 关键时期：`1995-1999`

Brian Behlendorf 的代表性在于，他站在 Web 爆发的历史节点上，把“补丁协作”推进成了真正可持续的项目共同体。`1995` 年前后，他与其他开发者围绕 NCSA 服务器补丁建立邮件列表与协作机制，随后形成 Apache HTTP Server；`1999` 年，Apache Software Foundation（ASF）成立，开源项目开始以更稳定的基金会形式延续。

从历史角度看，Behlendorf 连接了两条主线：一条是 Web 基础设施开源化，另一条是项目治理基金会化。后续他在 CollabNet 等协作基础设施领域的工作，也进一步说明，开源不只是写代码，更是长期组织协作与公共基础设施治理。

### Mitchell Baker

- 代表项目 / 组织：Mozilla、Mozilla Foundation、MPL
- 关键时期：`1998-2005`

Mitchell Baker 的重要性在于，她同时处在许可证、社区治理和公共组织建设的交叉点上。作为 Netscape 法务与后来的 mozilla.org 负责人，她参与撰写 Netscape Public License 与 Mozilla Public License，并长期推动 Mozilla 项目的开放协作结构。`2003-07-15` Mozilla Foundation 成立时，她是其中的关键推动者之一。

开源历史里，很多人以代码知名，而 Baker 更代表另一类同样关键的人物：让大型开源项目具备法律、组织和公共使命支撑的人。Mozilla 的意义不只是 Firefox 成功过，而是它长期把“开放 Web”与公共治理放在一起讨论。理解这一点，有助于理解为什么现代开源不能只讲仓库和提交，还必须讲组织与公共性。

### Guido van Rossum

- 代表项目 / 组织：Python
- 关键时期：`1991`、`2018-2019`

Guido van Rossum 以 Python 创造者身份广为人知，但他在开源史上的更大价值，还在于展示了一个成熟语言项目如何跨越“创始人中心”阶段。Python 在很长时间里由 Guido 作为 BDFL（Benevolent Dictator for Life）进行最终裁决；`2018-07` 他退出这一角色，`2019` 年 `PEP 13` 正式确立 Steering Council 治理结构。

这使 Guido 成为讨论开源治理演化时极具代表性的人物。他既证明了个人愿景对项目早期的重要性，也证明了当项目足够成熟时，治理结构必须从个人权威转向更可继承的公共机制。对于今天希望长期维护项目的人来说，Python 的治理转型是一个非常有价值的案例。

### Chris Wanstrath

- 代表项目 / 组织：GitHub
- 关键时期：`2008-2018`

Chris Wanstrath 作为 GitHub 联合创始人，其历史意义不在于发明了 Git，而在于把 Git 变成了大规模公共协作平台的入口。`2008` 年 GitHub 上线后，公开仓库托管、fork、评论、代码搜索、Pages、Gists 等功能逐步汇集在同一平台上，使大量开发者第一次能够以较低门槛进入开源协作。

因此，Wanstrath 代表的是“平台化阶段”的开源。GitHub 既没有取代许可证、社区和维护劳动，也没有自动让项目更健康，但它显著改变了开源的可见性、参与入口和协作速度。今天我们谈 pull request 工作流、项目主页、公开 issue 和社交化代码协作，很大程度上都处在 GitHub 形成的历史惯性之中。

## 5. 维护、基础设施与方法解释者

### Werner Koch

- 代表项目 / 组织：GnuPG
- 关键时期：`1997` 以后

Werner Koch 是 GnuPG 的主要作者。对开源史而言，他的重要性一方面来自 GnuPG 本身作为加密基础设施的长期价值，另一方面来自他让整个世界更清楚地看见：关键开源基础设施的维护，往往并不自动伴随稳定资源。围绕 GnuPG 维护经费的讨论，尤其在 `2014-2015` 前后，成为理解“公共依赖为何脆弱”的典型案例之一。

Koch 所代表的不是“最热闹的社区”，而是“最关键但常常被低估的维护劳动”。在今天讨论开源安全、供应链、资助与可持续性时，GnuPG 的案例仍然非常有穿透力，因为它直接揭示了一个事实：全世界都依赖的重要软件，可能长期压在极少数维护者肩上。

### Karl Fogel

- 代表项目 / 组织：CVS、Subversion、*Producing Open Source Software*
- 关键时期：`1990s-2020s`

Karl Fogel 的代表性在于，他既参与过开源工具与版本控制实践，又把这些经验系统写成了方法论文本。自 `1992` 年以来，他长期从事开源开发、咨询与组织工作；`2005` 年出版的 *Producing Open Source Software* 则成为许多人理解开源项目如何启动、沟通、治理、招募与维护的经典读物。

与其说 Fogel 代表某一个单独项目，不如说他代表“开源方法被清晰总结出来”的阶段。很多项目的成功经验原本分散在邮件列表、习惯和口耳相传中，而 Fogel 的工作把这些经验整理成可复用的公共知识。对于后来的课程建设、项目引导和社区实践，这类解释者同样重要。

### Nadia Eghbal

- 代表项目 / 组织：*Roads and Bridges*、*Working in Public*、Open Source Guides
- 关键时期：`2010s-2020s`

Nadia Eghbal 不是传统意义上的系统作者，但她是理解现代开源维护问题时极具代表性的人物。她关于数字公共基础设施、维护劳动和资助难题的研究，尤其是 *Roads and Bridges* 与 `2020` 年的 *Working in Public*，帮助许多人第一次系统地认识到：开源的问题往往不是“代码没人能写”，而是“长期维护、响应与治理成本无人承担”。

她在 GitHub 参与推动 Open Source Guides 的工作，也进一步把这些认识转化为更易进入的公共实践材料。Eghbal 的位置说明，进入 2020 年代之后，开源史已经不能只写项目创始人与许可证，还必须写维护者、公共品、资助结构和社区负担这些过去经常被忽略的现实问题。

## 6. 使用方式

这份人物附录最适合回答四类问题：

- 某个关键人物究竟改变了开源历史的哪一层：概念、许可证、治理、平台，还是维护？
- 为什么有些人并不以“写出最多代码”著称，却仍然必须写进开源史？
- 一个今天看起来理所当然的实践，例如许可证审核、基金会治理、平台协作或维护资助，最早是由哪些人物推动进入公共视野的？
- 当读者先记住某个人名时，接下来应当回到哪条历史线继续阅读？

如果读者想看按年份展开的历史脉络，应继续阅读“附录 开源历史”；如果想从人物、事件和项目三者之间快速跳转，应先查“附录 开源对照表”。

## 7. 本附录的主要编写依据

本附录在详细扩写时，优先使用项目或组织的官方历史材料，再用 Wikipedia 进行人物与时间点交叉校对。重点参考来源如下：

- GNU Project, “Initial Announcement”  
  https://www.gnu.org/gnu/initial-announcement.en.html
- Free Software Foundation, “FSF History”  
  https://www.fsf.org/history/
- Open Source Initiative, “History of the Open Source Initiative”  
  https://opensource.org/about/history-of-the-open-source-initiative
- Software Freedom Law Center, “Team: Eben Moglen”  
  https://softwarefreedom.org/about/team/
- Debian, “People: Who we are and what we do”  
  https://www.debian.org/intro/people
- Debian, “A Brief History of Debian / The Debian Manifesto”  
  https://www.debian.org/doc/manuals/project-history/  
  https://www.debian.org/doc/manuals/project-history/manifesto.en.html
- Apache Software Foundation, “ASF History”  
  https://www.apache.org/history/
- Mozilla archive, “History of the Mozilla Project / mozilla.org Staff Members”  
  https://www-archive.mozilla.org/about/history  
  https://www-archive.mozilla.org/about/staff.html
- Python, `PEP 13 – Python Language Governance`  
  https://peps.python.org/pep-0013/
- Git, “A Short History of Git”  
  https://git-scm.com/book/en/v2/Getting-Started-A-Short-History-of-Git
- GitHub Blog, “Only the beginning”  
  https://github.blog/news-insights/the-library/only-the-beginning/
- Karl Fogel, *Producing Open Source Software*  
  https://producingoss.com/
- Karl Fogel Biography  
  https://www.red-bean.com/kfogel/bio
- Stripe Press, *Working in Public*  
  https://press.stripe.com/working-in-public
- GitHub Blog, “Announcing Open Source Guides”  
  https://github.blog/news-insights/the-library/announcing-open-source-guides/
- GnuPG, “People”  
  https://www.gnupg.org/people/
- Wikipedia 人物与历史条目（交叉校对用）  
  https://en.wikipedia.org/wiki/History_of_free_and_open-source_software  
  https://en.wikipedia.org/wiki/Timeline_of_free_and_open-source_software  
  https://en.wikipedia.org/wiki/Ken_Thompson  
  https://en.wikipedia.org/wiki/Dennis_Ritchie  
  https://en.wikipedia.org/wiki/Richard_Stallman  
  https://en.wikipedia.org/wiki/Bruce_Perens  
  https://en.wikipedia.org/wiki/Eric_S._Raymond  
  https://en.wikipedia.org/wiki/Christine_Peterson  
  https://en.wikipedia.org/wiki/Eben_Moglen  
  https://en.wikipedia.org/wiki/Ian_Murdock  
  https://en.wikipedia.org/wiki/Linus_Torvalds  
  https://en.wikipedia.org/wiki/Brian_Behlendorf  
  https://en.wikipedia.org/wiki/Mitchell_Baker  
  https://en.wikipedia.org/wiki/Guido_van_Rossum  
  https://en.wikipedia.org/wiki/Chris_Wanstrath  
  https://en.wikipedia.org/wiki/An_Open_Letter_to_Hobbyists  
  https://en.wikipedia.org/wiki/Werner_Koch

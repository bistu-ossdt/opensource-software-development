# Chapter 5 - Leveraging Open Source Software Resources

> Mapped from `《开源软件开发技术》教材大纲 第五章（草稿） 曾铮.md`: `## 利用好开源软件资源` to before `## 附录1 GuHub的使用`.

## 利用好开源软件资源

> 曾铮，约3万字

## 思路

1 内容方向的选择和之前的章节对应，比如人工智能等等。

### 2 内容符合业界当前的发展

### 3 贴近大学生的实际需求，如日常工具、学习需要、工作需要。

4 中国目前的发展，基金会，许可证，大学的开源发展（社团，镜像）等等。

## 4 延伸阅读部分的设置

> 论述开源软件资源都包含什么，利用资源的好处。描述文字最后再补充。

参与开源社区是学习开源的重要方式。

## 主要的开源社区与平台

> 当前世界开源社区和平台的统计数据

## 国外现状

> 国外的开源社区情况介绍
目前国外主要的开源社区。很多开源代码托管网站也有社区功能，因此我们不对托管和社区做严格区分。

### Github

GitHub（https://github.com）是一家总部位于美国的全球公司，提供使用Git进行软件开发和版本控制的托管服务。2018年它成为Microsoft的子公司。它提供Git的分布式版本控制和源代码管理（SCM）功能，以及一些社区功能。它为每个项目提供访问控制和多种协作功能，例如错误跟踪，功能请求，任务管理和Wiki。

GitHub成立于2007年，位于旧金山。2009年2月24日，团队成员在Yahoo!的一次演讲中宣传了Github。在上线的第一年中，GitHub积累了超过46,000个公共仓库。ReadWriteWeb报告称，在2011年1月至2011年5月这段时间内，GitHub 的提交总数已超过SourceForge和Google Code。 在2018年6月19日，GitHub通过向所有学校提供免费教育捆绑包扩展了GitHub Education。2020年7月上旬，GitHub将网站的2月档案存储在挪威斯瓦尔巴德群岛的一个废弃山区中，这是北极世界档案馆的一部分，这21TB的数据存储在胶片卷轴上，该卷轴预计可以保存1000年。

GitHub免费提供基本服务，更高级的专业和企业服务是商业性的。免费的GitHub帐户通常用于托管开源项目。截至2019年1月，GitHub为所有计划提供了无限的私有仓库，包括免费帐户，但每个仓库免费最多允许三个协作者。从2020年4月15日开始，免费计划允许无限的合作者。截至2020年1月，GitHub报告拥有超过4000万用户和超过1亿个仓库（包括至少2800万个公共仓库），使其成为世界上最大的源代码托管网站。

支持GitHub的基本软件是Git，由Linux的创建者Linus Torvalds编写。GitHub用户界面的其他软件是由GitHub开发人员使用Ruby on Rails和Erlang编写。GitHub的主要目的是促进软件开发的版本控制和问题跟踪。对于版本控制，Github允许拉取请求提出对源代码的更改。有能力查看建议的更改的用户可以查看并批准所请求的更改。用Git术语来说，此操作称为“提交”，并且它保留所有提交的历史记录，以后可以查看。可以使用标准的Git命令行界面访问和管理GitHub.com上的项目，所有标准的Git命令都可以使用。GitHub.com还允许用户浏览站点上的公共仓库。也可以使用多个桌面客户端和Git 插件。GitHub提供类似于社交网络的功能，例如收藏、关注者、Wiki和社交网络图，以显示开发人员如何处理其版本库（fork）以及什么分支（Branch）是最新的。任何人都可以浏览和下载公共仓库，但是只有注册用户才能向仓库提供内容。使用注册的用户帐户，用户可以进行讨论、管理仓库、向其他仓库提交代码以及查看对代码的更改。

## 在基础功能之外，GitHub提供了以下增强功能和内容

- GitHub Enterprise是GitHub.com的自我管理版本，具有类似功能。它可以在组织自己的硬件上运行，也可以在云服务商上运行。
- GitHub Actions，允许构建持续集成和持续部署管道来测试，发布和部署软件，而无需使用第三方网站/平台。
- GitHub Pages是GitHub自2008年以来向GitHub用户提供的静态网络托管服务，用于托管用户博客，项目文档或书籍。所有GitHub Pages内容都存储在Git仓库中，既可以作为文件直接提供给访问者，也可以采用Markdown格式。GitHub可以与Jekyll、Hexo、Hugo等静态网站和博客生成器无缝集成，生成的网站可以托管为github.io域的子域名，也可以通过第三方域名注册商购买自定义域名，并能自动生成HTTPS证书。
- GitHub Gist用来托管代码片段。Gist建立在传统的简单的pastebin概念之上，增加了代码片段的版本控制、简单的分叉和SSL加密的私有粘贴。（pastebin是一种在线内容托管服务，用户可以在其中存储纯文本，第一个pastebin是同名的pastebin.com。Pastebins发展于20世纪90年代末，目的是为了方便专门讨论计算机的IRC聊天室，在这种聊天室中，用户自然需要在面向行的媒介中共享大块的计算机输入或输出。）
- Learning Lab通过完成有趣而现实的项目来提高技能，包含GitHub社区创建的语言和工具、GitHub使用、GitHub Actions、DevOps等课程。
- GitHub开发的开源文本编辑器Atom和跨平台创建原生程序的框架Electron。
- 开源软件指南( https://opensource.guide/)是由GitHub策划和创建。外部社区共同编写的社区资源集合，目标是汇总开源社区最佳实践。

## 更多Github和Git的使用方法和技术内容请查看附录一。

### SourceForge

SourceForge( https://sourceforge.net/ )是由VA软件公司于1999年创立的，是第一个免费为自由和开源软件开发者提供一个集中的位置来控制和管理软件开发。运行SourceForge网站的软件于2000年1月作为自由软件发布，后来被命名为SourceForge Alexandria。

SourceForge是一个基于网络的源代码存储库，它是自由和开放源码软件项目的集中地。项目开发人员可以访问集中存储和管理项目的工具，它最著名的是提供CVS、SVN、Bazaar、Git和Mercurial等版本控制系统。主要功能包括项目维基、度量和分析、访问MySQL数据库和独特的子域URL。

SourceForge.net有大量用户，随着项目活跃度的上升，SourceForge.net的内部排名系统将著名的项目展示在各种开发者面前，创造了一个积极的反馈循环。截止2020年中期，SourceForge拥有过502,000个项目，数百万注册用户，3200万月度访问用户，每天提供超过260万次下载。

### Bitbucket

BitBucket是一家源代码托管网站，采用Mercurial和Git作为分布式版本控制系统，同时提供商业计划和免费账户。免费帐户带有不限数量的私人存储库（每个账户最多 5 个用户），也提供多种付费计划，允许每个帐户有更多用户。此外，标记为“公开”的仓库对可以编辑或读取其内容的人数没有限制。

### Gitlab

GitLab是一个利用 Ruby on Rails 开发的开源应用程序，实现一个自托管的Git项目仓库，可通过Web界面进行公开访问，或者作为私人项目安装。 GitLab拥有与GitHub类似的功能，能够浏览源代码，管理缺陷和注释。可以管理团队对仓库的访问，它非常易于浏览提交过的版本并提供一个文件历史库。 团队成员可以利用内置的简单聊天程序（Wall）进行交流。它还提供一个代码片段收集功能可以轻松实现代码复用，便于日后有需要的时候进行查找。

### Apache基金会 Apache Software Fundation (ASF)

ASF( http://www.apache.org/ )成立于1999年，董事会全部由志愿者组成，负责监督350多个领先的开源项目，包括Apache HTTP服务器--世界上最流行的网络服务器软件。

ASF为知识产权和财务贡献提供了一个既定的框架，同时也限制了我们的项目投入者可能面临的法律风险。通过被称为 "The Apache Way "的ASF择优程序，超过730名个人成员和7000名提交者成功地合作开发了免费的企业级软件，使全球数百万用户受益：数以千计的软件解决方案在Apache许可证下发布；社区积极参与ASF邮件列表、指导计划和ApacheCon（基金会的官方用户会议、培训和博览会）。

ASF的前身是Apache集团，于1999年注册成立，是一个以会员制为基础的非营利性组织，以确保Apache项目在个人志愿者的参与之外继续存在。通过在基金会项目中的持续参与和贡献，表现出对开源软件合作开发的承诺的个人，有资格成为ASF的成员。个人在被提名并得到ASF现有成员的多数批准后，即可获得ASF成员资格。因此，ASF由其最直接服务的社区（在其项目中合作的人）管理。

### 自由软件基金会Free Software Foundation (FSF)

自由软件基金会(以下简称FSF) ( http://www.fsf.org/ )是一个非营利性组织，使命是促进计算机用户的自由。FSF致力于通过促进自由软件和文档的开发和使用，特别是GNU操作系统，以及反对数字限制管理（DRM）和软件专利等对计算机用户自由的威胁，来确保计算机用户的自由。

随着社会越来越依赖电脑，用户所运行的软件对确保未来的自由社会至关重要。自由软件就是要控制用户在家庭、学校和企业中使用的技术，让电脑为用户的个人和公共利益服务，而不是为那些可能寻求限制和监控用户的专有软件公司或政府服务。FSF只使用自由软件来完成其工作。FSF保留了涵盖自由软件哲学的历史性文章，并保留了自由软件定义--清楚地显示特定软件程序必须具备的真实条件，才能将其视为自由软件。。

FSF赞助了GNU项目，提供一个完整的、以自由软件形式授权的操作系统。FSF为GNU软件维护者提供开发系统，包括完整的电子邮件、shell服务和邮件列表。FSF拥有GNU操作系统和其他自由软件的大部分版权。FSF持有这些资产是为了保护自由软件，防止自由软件变成专有软件。每年，FSF都会从个人软件开发者和从事自由软件开发的公司那里收集数千份版权转让书。FSF在美国版权局注册这些版权，并执行发布自由软件的许可证--通常是GNU通用公共许可证。FSF这样做是为了确保自由软件发行者尊重他们的义务，将自由传递给所有用户，让他们分享、研究和修改代码。FSF通过自由软件许可与合规实验室来完成这项工作。

FSF发布的GNU通用公共许可证（GNU GPL）是世界上最流行的自由软件许可证，也是唯一以促进和保护软件自由为明确目的的许可证。FSF发布的其他重要许可证包括 GNU Lesser General Public License (GNU LGPL)、GNU Affero General Public License (GNU AGPL) 和 GNU Free Document License (GNU FDL)。FSF还为社区提供重要资源，包括自由软件基金会/教科文组织自由软件目录。

### Linux基金会 Linux Foundation(LF)

Linux 基金会( https://www.linuxfoundation.org/ ) 是一家非营利性技术组织，致力于促进，保护和推进Linux和协同开发，并支持“历史上最大的共享技术资源”。它开始于2000年的开源码发展实验室（OSDL），并与自由标准组织（FSG）合并后从而成为现在的组织。Linux基金会赞助Linux创始人Linus Torvalds和主管维护者Greg Kroah-Hartman的工作，并由领导Linux和开源公司的支持。近年来，Linux基金会通过活动，培训和认证以及开源项目扩大了服务范围。Linux基金会致力于围绕开源项目建立可持续的生态系统，以加速技术发展和行业应用。

Linux是历史上最大、最普遍的开源软件项目。它几乎在每个领域都得到了广泛的认可，包括金融服务、政府、教育，甚至电影制作。Linux也是支持物联网、云计算和大数据等前沿技术的首选操作系统。Linux基金会将其支持Linux社区的经验和专业知识用于帮助建立、构建和维持一些最关键的开源技术。今天，它的工作远远超出了 Linux 的范围，促进了软件栈每一层的创新。Linux基金会主持的项目涵盖了企业IT、嵌入式系统、消费电子、云、网络等领域。

这些高速发展的项目中，有几个正在帮助重新定义可能的项目，包括用于跨行业区块链技术的Hyperledger；汽车应用的开放软件平台Automotive Grade Linux；用于实时、策略驱动的虚拟网络功能软件自动化的开放网络自动化平台项目（ONAP）；以及用于生产级容器编排的云原生计算基金会项目Kubernetes。

Linux基金会及其项目在美洲、亚太和欧洲、中东和非洲地区拥有1000多家企业成员，其中包括在战略性使用开源方面处于领先地位的公司。其中包括AT&T、思科、富士通、日立、华为、IBM、英特尔、微软、NEC、甲骨文、高通和三星。

### Linux Kernel

Linux内核社区（http://www.kernel.org/）是一家成立于2002年的加州公益组织，旨在向公众免费发布Linux内核和其他开源软件。Linux内核社区实行的是基于贡献者公约行为准则的行为准则。Linux 内核社区由 Linux 基金会管理，它为运行和维护 kernel.org 基础设施提供全面的技术、财务和人员支持。

### Mozilla基金会

Mozilla是一个混合组织，结合了非营利和市场策略，以确保Internet仍然是共享的公共资源。Mozilla基金会（https://foundation.mozilla.org/）是一个非营利公司。基金会支持现有的Mozilla社区，并监督Mozilla的治理结构。Mozilla社区通过创建免费的开源产品和技术来改善世界各地人们的在线体验，从而将公众利益融入Internet。Mozilla公司是Mozilla基金会的全资子公司，与社区合作开发推进Mozilla的原则软件。其中Firefox浏览器在安全性，隐私和语言本地化方面被公认为是市场领先者。

Mozilla项目创建于1998年，发布了Netscape浏览器套件源代码。它旨在利用互联网上成千上万的程序员的创造力，并推动浏览器市场上前所未有的创新水平。最初“Mozilla”被用作Netscape Navigator的开发代号。网景公司希望Netscape Navigator能够取代当时世界第一的Mosaic，这个名字由“Mosaic Killa”（Killa是俚语中Killer的拼法）变化而来，并与经典的虚拟怪物哥斯拉有关“Godzilla eat the Mosaic”，即Mosaic+Godzilla+Killa=Mozilla。

1998年3月31日，网景公司在源码开放许可证的安排下，公开了Netscape Communicator（最早出现在个人电脑上的浏览工具)的大部分源代码。这个项目沿用了Mozilla的名称，并且新成立了Mozilla开发社区，及其专门网站Mozilla.org。不过由于Netscape Communicator的源代码老旧难以维护，源代码差不多被全部抛弃，Mozilla社区开发出更稳定、更多功能的新一代互联网应用包。经过一段长时间的开发之后，应用包终于在2002年6月5日诞生。Mozilla当时成为该应用包的名字。Mozilla的代码成为了Netscape 6和Netscape 7的基础。而由基金会推出的Mozilla Firefox、Mozilla Thunderbird也是基于Mozilla最底层的代码。

通过创建一个开放的社区，Mozilla项目的规模已超过任何一家公司。社区成员参与其中并扩大了该项目最初任务的范围-人们开始创建各种浏览器，开发工具和一系列其他项目，而不仅仅是使用Netscape的下一个浏览器。经过几年的开发，第一个主要版本Mozilla 1.0于2002年发布。该版本对套件中的浏览器，电子邮件客户端和其他应用程序进行了许多改进，但使用它的人并不多。到2002年，超过90％的Internet用户使用Internet Explorer浏览。Mozilla社区成员于同年发布了Phoenix的第一个版本（后来更名为Firefox），目的是为尽可能多的人提供最佳的浏览体验。

2003年7月15日，Mozilla项目创建了Mozilla基金会，这是一个独立的非营利组织，由个人捐助者和各种公司支持。Mozilla基金会负责管理项目的日常运营，并正式承担了促进互联网的开放性，创新和机会的角色。为此，它继续发行Firefox和Thunderbird等软件，并扩展到新领域，例如提供赠款以支持Web上的可访问性改进。美国在线帮助了Mozilla基金会的成立，它向基金会转移了硬件和知识产权，并且在最初的3个月里雇用了一个3人小组来帮助这次过渡。美国在线并且承诺在2年时间内捐助200万美元给基金会。当美国在线完全的从Mozilla组织中撤出后，Mozilla基金会在2003年7月15日成立了，它的目的是保证Mozilla可以在没有网景以后能继续生存下去。

Firefox 1.0于2004年发布，并取得了巨大的成功-在不到一年的时间内，它被下载了超过1亿次。从那时起，定期发布新版本的Firefox，并不断刷新记录。Firefox的流行已帮助将选择带回用户。新的竞争加速了创新并改善了所有人的互联网。

在2005年8月3日，Mozilla基金会建立了一个完全拥有的子公司叫Mozilla公司来继续开发和发布Mozilla Firefox和Mozilla Thunderbird。Mozilla公司承担软件发行的计划，市场和一些软件分发相关的活动。它也处理一些商业合作，很多这些合作都带来收入。不像Mozilla基金会，Mozilla公司是一个应税实体,这给它在追逐收益以及其他商业活动带来了更多自由。随着Mozilla公司的成立，Mozilla基金会把所有的软件开发和商业相关的活动都转移给了这个新的下属机构。Mozilla基金会如今只专注于监管和战略等事宜，它也继续管理一些没有产品化的项目，比如Camino、SeaMonkey。拥有Mozilla商标和其他知识产权，并且全部授权Mozilla公司使用。基金会还控制着Mozilla的程序源代码库并且决定谁可以提交代码入库。

### 开源促进会 Open Source Initiative(OSI)

开放源码促进会( https://opensource.org/ )是一家加利福尼亚的公益公司，成立于1998年。OSI是一个具有全球范围的非营利性公司，其成立的目的是教育和宣传开放源码的好处，并在开放源码社区的不同支持者之间建立桥梁。OSI积极参与开放源码社区建设、教育和公共宣传，以提高人们对非专有软件的认识和重要性。OSI董事会成员经常到世界各地参加开放源码会议和活动，与开放源码开发人员和用户会面，并与公共和私营部门的管理人员讨论开放源码技术、许可证和发展模式如何提供经济和战略优势。

OSI最重要的活动之一是作为一个标准机构，为了社区的利益维护开源定义。开放源码倡议批准的许可证商标和程序创造了一个信任的纽带，开发者、用户、公司和政府可以围绕这个纽带组织开放源码合作。

### OpenSource.com

Opensource.com ( https://opensource.com/ )是一个专注于开源和 Linux 教程、故事和资源的网站，由RedHat公司提供赞助。它拥有一个由编辑、通讯员、撰稿人和读者组成的多元化的团队。

2010年，红帽CEO Jim Whitehurst在一篇名为《欢迎来到Opensource.com的对话》的文章中宣布推出Opensource.com。这个网站是红帽回馈开源社区的方式之一，愿望是建立一个连接点，以便就开放源码在软件世界之外所能产生的更广泛的影响进行对话。

到2013年，Opensource.com平均每月发布46篇文章，2016年3月，Opensource.com的阅读量首次突破100万。2020年，Opensource.com在全球的阅读量达到200万。

### Eclipse 基金会

Eclipse基金会（http://www.eclipse.org/）是一个非营利组织，由超过275名成员支持，为全球个人和组织社区提供了一个成熟的、可扩展的、商业友好的环境，以促进开源软件的合作和创新。基金会现在管理Eclipse IDE、Jakarta EE和超过350个开源项目，包括运行环境、工具和框架，适用于广泛的技术领域，如物联网、汽车、地理空间、系统工程和许多其他领域。

Eclipse项目最初是由IBM在2001年11月创建的，并得到了一个软件供应商联盟的支持。目前数百万开发人员仍在使用Eclipse项目。Eclipse基金会成立于2004年1月，作为Eclipse社区的管理者，这个独立的非营利性公司的成立是为了让Eclipse周围建立一个厂商中立、开放和透明的社区。

Eclipse社区由跨越许多行业的个人开发者和组织组成。基金会雇用了全职专业人员为社区提供服务。Eclipse 提交者通常受雇于组织或独立开发者，他们自愿为 Eclipse 项目工作。Eclipse 基金会为 Eclipse 社区提供四项关键服务： IP 管理、生态系统开发、开发流程和 IT 基础设施。每一个领域都有全职工作人员，他们与广大的Eclipse社区合作，协助满足利益相关者的需求。

基金会的工作人员帮助实施Eclipse开发流程。这个流程协助新项目的启动，并确保所有Eclipse项目以公开、透明和择优的方式运行。作为这个过程的一部分，基金会组织成员社区对项目进行评审，以确保项目和广大成员之间的互动一致。

Eclipse基金会管理Eclipse开源社区的IT基础设施，包括Git代码库和代码审查工具、错误跟踪器、Jenkins构建、面向开发的邮件列表和论坛、下载站点和网站。该基础设施旨在为开发Eclipse技术的提交者和使用该技术的消费者提供可靠和可扩展的服务。

成立Eclipse基金会的目的是为Eclipse开源项目和Eclipse社区服务。作为一个独立的非营利性公司，基金会和Eclipse治理模式确保没有任何一个实体能够控制Eclipse社区的战略、政策或运作。

### OpenJS基金会

OpenJS基金会（https://openjsf.org/）的任务是通过为开源JavaScript生态系统创建重心，推动关键JavaScript解决方案和相关技术的广泛采用和持续开发。开发人员依靠不断增长的开源技术组合来创建，测试和部署关键应用程序。

## OpenJS基金会的主要目标是

促进关键JavaScript和Web解决方案及相关技术的广泛采用和持续开发。

### 促进JavaScript开发社区内的协作。

在整个端到端JavaScript生态系统中为开源项目创建重心，指导它们迈向开放治理和多样化的协作者基础。

### 托管基础结构以支持托管的JavaScript开源项目。

通过推进项目和战略伙伴关系，来建立一个开放和可访问的网站。

## 国内现状

> 国内的开源社区情况介绍

## 国内的开源社区

### 开源中国社区（OSChina）

开源中国（https://www.oschina.net/）社区国内最活跃的，增长最快的线上技术社区，提供开源资讯，博客，开源软件查询，开源项目托管等功能，也举办源创汇等线下活动。创立与2008年，目前与中国开源软件推进联盟（COPU）合作，是该联盟的官方支持社区。

### CSDN

CSDN（https://www.csdn.net/）国内著名的线上技术社区企业，最活跃的开源社区之一。提供开源资讯、博客、项目托管等线上功能。有企业的强大支持，集线上社区，纸媒杂志，线下活动和会议于一身，有较高的社区品牌知名度。

### 开源社

开源社（https://kaiyuanshe.cn/）是由中国支持开源的企业，社区及个人所发起的一个开源联盟，有非常活跃的线上、线下社区。提供开源之星、博客、开源者行、开源社区研究等线上、线下功能。创立于2014年，是一个成员广泛的社区，主要以线下活动为主，线上社区着重体现线下活动的成果。

### Linux伊甸园 Linuxeden

Linux伊甸园（http://www.linuxeden.com/）成立较早，国内著名的线上开源社区，主要提供开源资讯。除网站外，还以微博、微信等其它形式对外提供服务

### 深度开源 Open-Open

深度开源（https://www.open-open.com/）功能丰富的线上开源社区，提供论坛、博客、开源软件查询、资讯、文档等功能，一直比较稳定、活跃。早期关注Java和开源软件查询，界面朴素，近年增加了较多功能。

### Linux中国

Linux中国 （https://linux.cn/）成立较早，今年仍比较活跃，主要以论坛的形式提供开源资讯和技术资料，特色是翻译了大量有观点的国外开源文章。成立于2003年，其前身是炎黄角马（CNGNU）。是国内运营时间最长的线上社区之一。

### Chinaunix

Chinaunix是（http://chinaunix.net/）早期国内最大的线上开源社区，以论坛、资讯、下载等服务为主，目前活跃度已不如前。2008年被IT168收购，提供大量的Linux操作系统相关的技术信息。

### 我是菜鸟IMCN

我是菜鸟（https://imcn.me/）是以博客的展示形式运维的开源资讯网站，提供很多有趣的开源文化、项目、创意的资讯，较活跃。一个有趣的开源资讯站，关注Ubuntu系统相关的报道。

### Ubuntu中国论坛

Ubuntu中国论坛（https://forum.ubuntu.org.cn/）国内最著名的线上Ubuntu社区，提供大量开源软件、Ubuntu实用技术、社区交流信息。该社区不是Canonical公司的Ubuntu中文官方社区，但它无疑是国内最受欢迎的Ubuntu社区

### 火狐社区（中国）

火狐中国（http://mozilla.com.cn/）官方社区。及时发布火狐和Firefox OS的各种信息，开展一系列项目推广活动。

### Fedora中文社区

Fedora中文社区（https://www.fdzh.org/）提供关于 Fedora 的最新资讯，及一系列开源工具。

### BlenderCN

BlenderCN(https://www.blendercn.org/) 是开源软件Blender的国内社区。聚集了大量Blender 3D建模使用者和开发者。

### OpenFans社区

OpenFans社区（http://www.openfans.org/）专注于cecOS云平台和在线教育的社区组织。定期发布cecOS系统平台和在线教育视频。

### 文泉驿

文泉驿（http://wenq.org/）国内最著名的开源汉字库项目社区。以社区的方式发展开放、开源的完整汉字库。

### PHPChina

PHPChina（http://www.phpchina.com/）企业驱动的PHP技术社区。同时开展各种技术推广活动。

## 国内的开源项目托管平台

### CodeChina

CodeChina（https://codechina.csdn.net/）是CSDN的代码托管平台。

### Coding

Coding（https://coding.net/）是一个面向开发者的云端开发平台，提供 git/svn 代码托管，代码质量分析，在线 WebIDE，项目管理，开发协作，冒泡社区，提供个人和企业公有云及企业私有云的服务。项目管理是针对软件开发协作定制的一站式工具，包含了任务，讨论，文件等功能。支持多成员协作，并且深度集成了代码仓库的操作与状态。此外，还提供社会化协作功能，包含了社交元素，方便开发者进行技术讨论和协作。项目管理分为公开和私有项目，单个账号可以创建总共1000个项目，包括公开和私有项目，支持移动客户端。

### 码云 Gitee

码云（https://gitee.com/）是开源中国社区团队推出的基于Git的快速的、免费的、稳定的在线代码托管平台。专为开发者提供的云端软件开发协作平台。无论是个人、团队、或是企业，都能够用码云实现代码托管、项目管理、协作开发。

## 国内的开源镜像

- 中国科学技术大学开源软件镜像（debian.ustc.edu.cn）

- 清华大学 TUNA 镜像源（mirrors.tuna.tsinghua.edu.cn）

- 浙江大学开源镜像站（mirrors.lifetoy.org）

- 兰大开源社区镜像站（mirror.lzu.edu.cn）

- 北京理工大学开源软件镜像（mirror.bit.edu.cn）

- 中国互联网络信息中心开源镜像站（mirrors.cnnic.cn）

- 中科院开源软件协会镜像站（mirrors.opencas.org）

## 重要的开源软件产品

> 介绍开源软件的情况

## 开源产品-操作系统

### Deepin

深度操作系统（https://www.deepin.org/zh/）亦称为deepin，原名Hiweed Linux及Linux deepin，是武汉深之度科技有限公司开发的开源操作系统。它是基于Debian的稳定版本的一个Linux发行版。它可以运行在个人计算机和服务器上，并免费提供给个人用户使用。deepin因其美观和易用性而广受赞誉。据DistroWatch的数据，截至2017年，deepin是最受欢迎的源自中国的Linux发行版。2019年，华为开始销售预装有深度操作系统的笔记本电脑。

除操作系统外，深度团队也进行桌面环境和配套基础软件的开发，并与第三方厂商合作开发Linux版本应用。目前系统已经拥有很多针对deepin系统开发的应用程序。此外开发团队也参与Linux内核补丁相关作业。

### Ubuntu

Ubuntu（https://ubuntu.com/）是著名的Linux发行版之一，它也是目前最多用户的Linux发行版。
Ubuntu是以桌面应用为主的Linux发行版，Ubuntu由Canonical公司发布，他们提供商业支持。它是基于自由软件，其名称来自非洲南部祖鲁语或科萨语的“Ubuntu”一词（译为乌班图），意思是“人性”、“我的存在是因为大家的存在”，是非洲传统的一种价值观。
Ubuntu的开发由英国Canonical有限公司主导， Canonical通过销售与Ubuntu相关的技术支持和其他服务来产生收益。Ubuntu项目公开承诺开源软件开发的原则；鼓励人们使用自由软件，研究它的运作原理，改进和分发。
Ubuntu基于Debian发行版和GNOME桌面环境（当然也有其他的桌面环境），与Debian的不同在于它每6个月会发布一个新版本（即每年的四月与十月），每2年发布一个LTS长期支持版本。普通的桌面版可以获得发布后18个月内的支持，标为LTS（长期支持）的桌面版可以获得更长时间的支持。例如，Ubuntu 8.04 LTS（代号Hardy Heron），其桌面应用系列可以获得为期3年的技术支持，服务器版可以获得为期5年的技术支持。而自Ubuntu 12.04 LTS开始，桌面版和服务器版均可获得为期5年的技术支持。2013年3月有消息指出，Ubuntu计划在4月25日Ubuntu 13.04发布后，将非LTS版本的支持时间自18个月缩短至9个月，并采用滚动发布模式，允许开发者在不升级整个发行版的情况下升级单个核心包。
Ubuntu的目标在于为一般用户提供一个最新同时又相当稳定，主要以自由软件建构而成的操作系统。Ubuntu目前具有庞大的社区力量支持，用户可以方便地从社区获得帮助。
Ubuntu在Ubuntu 12.04的发布页面上使用了“友帮拓”作为官方译名。之前一些中文用户曾使用班图、乌班图、乌斑兔、乌帮图、笨兔等作为非官方译名。

### CentOS

CentOS（Community Enterprise Operating System）（https://www.centos.org/）是Linux发行版之一，它是来自于Red Hat Enterprise Linux（RHEL）依照开放源代码规定发布的源代码所编译而成。由于出自同样的源代码，因此有些要求高度稳定性的服务器以CentOS替代商业版的Red Hat Enterprise Linux使用。两者的不同，在于CentOS并不包含封闭源代码软件。CentOS对上游代码的主要修改是为了移除不能自由使用的商标。2014年，CentOS宣布与Red Hat合作，但CentOS将会在新的委员会下继续运作，并不受RHEL的影响。

简而言之，CentOS是Red Hat Enterprise Linux去除了专利软件的软件后的免费操作系统。目的是提供给想用红帽的系统，但却不想付钱的公司。

### Debian

Debian（https://www.debian.org/）是完全由自由软件组成的类UNIX操作系统，其包含的多数软件使用GNU通用公共许可协议授权，并由Debian计划的参与者组成团队对其进行打包、开发与维护。
Debian计划最初由伊恩·默多克于1993年发起，Debian 0.01版在1993年9月15日发布，而其第一个稳定版本则在1996年发布。
该计划的具体工作在互联网上协调完成，由Debian计划领导人带领一个志愿者团队开展工作，并以三份奠基性质的文档作为工作指导：Debian社区契约、Debian宪章和Debian自由软件指导方针。操作系统版本定期进行更新，候选发布版本将在经历过一定时间的冻结之后进行发布。
作为最早的Linux发行版之一，Debian在创建之初便被定位为在GNU计划的精神指导下进行公开开发并自由发布的项目。该决定吸引自由软件基金会的注意与支持，他们为该项目提供从1994年11月至1995年11月为期一年的赞助。赞助终止后，Debian计划创立非营利机构Software in the Public Interest以提供支持并令其持有Debian商标作为保护机构。Debian也接受世界多个非营利组织的资金支持。
Debian以其坚守Unix和自由软件的精神，以及其给予用户的众多选择而闻名。现时Debian提供了超过25,000个软件，超过50,000个软件包，并正式支持10个计算机系统结构。
作为一个大的系统组织框架，Debian旗下有多种不同操作系统核心的分支计划，主要为采用Linux核心的Debian GNU/Linux系统，其他还有采用GNU Hurd核心的Debian GNU/Hurd系统、采用FreeBSD核心的Debian GNU/kFreeBSD系统等。众多知名的Linux发行版，例如Ubuntu、Knoppix和Deepin，也都建基于Debian GNU/Linux。

### FreeBSD

FreeBSD（https://www.freebsd.org/）是FreeBSD项目的发展成果。它是一种开放源代码的类Unix的操作系统，基于BSD Unix的源代码派生发展而来。加州大学伯克利分校在1975年至1993年开发了BSD Unix操作系统。FreeBSD的许可证规定源代码开放，允许任何人自由使用，任何人都可以获得并使用它来满足各种需求，也可以修改它，然后再重发布 – 此功能专为个人和公司量身定制，可用于创建各种基于FreeBSD的商业和非商业产品。尽管FreeBSD直接从BSD派生，但是从法律的角度来看，FreeBSD为unix系统，但它并不是“UNIX”。因为现在“UNIX”商标属于国际开放标准组织。
FreeBSD的第一个版本于1993年发布。FreeBSD支持许多硬件和体系架构。和其他BSD家族的操作系统一样， 核心、驱动程序以及所有的用户层（Userland）应用程序（如Unix shell和cat和ps等命令）都存储在FreeBSD源代码库中。FreeBSD也可以运行其他二进制软件，比如Linux的。借助ports和FreeBSD软件包管理器pkg，用户能安装各种应用程序。根据2005年的调查，77％的BSD用户使用FreeBSD，因此FreeBSD拥有BSD系列中最大的用户社区。
如今个人和企业将FreeBSD用于各种用途，包括Yahoo! ，苹果，Juniper网络公司，诺基亚，IBM， Yandex的，Apache软件基金会，Hotmail，索尼和许多其他用途。
需要注意的是FreeBSD不是一个Linux发行版。它是UNIX内核操作系统。

### Android

Android（http://source.android.com）专门为手持设备设计开发的软件平台及操作系统。安卓系统是谷歌为手机和平板电脑等其他移动设备开发的操作系统和编程平台。它可以运行在许多不同制造商的许多不同设备上。Android包括一个软件开发工具包(SDK)，可以帮助你编写原始代码和组装软件模块，为Android用户创建应用程序。Android还提供了一个发布应用的市场。总的来说，Android代表了一个移动应用的生态系统。他的操作系统内核也是Linux。

## 开源产品-语言

### Python

Python（http://www.python.org/）是一种广泛使用的解释型、高级编程、通用型编程语言，由吉多·范罗苏姆创造，第一版发布于1991年。Python是ABC语言的后继者，也可以视之为一种使用传统中缀表达式的LISP方言。Python的设计哲学强调代码的可读性和简洁的语法（尤其是使用空格缩进划分代码块，而非使用大括号或者关键词）。相比于C++或Java，Python让开发者能够用更少的代码表达想法。不管是小型还是大型程序，该语言都试图让程序的结构清晰明了。
与Scheme、Ruby、Perl、Tcl等动态类型编程语言一样，Python拥有动态类型系统和垃圾回收功能，能够自动管理内存使用，并且支持多种编程范式，包括面向对象、命令式、函数式和过程式编程。其本身拥有一个巨大而广泛的标准库。
Python解释器本身几乎可以在所有的操作系统中运行。Python的其中一个解释器CPython是用C语言编写的、是一个由社区驱动的自由软件，目前由Python软件基金会管理。
Python主要用于Web后端开发、网络爬虫、计算与数据分析、人工智能、自动化运维、云计算、网络编程、游戏编程。通常比较常见的是Web开发、爬虫、计算与数据分析和人工智能。

### PHP

PHP（http://www.php.net/）是一种动态网页设计的脚本语言，也可以进行各种文本处理，甚至图形界面应用开发PHP是一种流行的通用脚本语言，特别适合于网络开发（WEB开发）。

### Node.js

Node.js ( https://nodejs.org/ )是一个Javascript运行环境(runtime)，用于方便地搭建响应速度快、易于扩展的网络应用。非常适合在分布式设备上运行数据密集型的实时应用。因此Node.js不能算作是一个编程语言，编程语言是JavaScript。Node.js是提供了一个脱离浏览器执行JavaScript的一个环境。简单的说 Node.js 就是运行在服务端的 JavaScript。

### Kotlin

Kotlin ( https://kotlinlang.org/ )是一种在Java虚拟机上运行的静态类型编程语言，它也可以被编译成为JavaScript源代码。它主要是由俄罗斯圣彼得堡的JetBrains开发团队所发展出来的编程语言，其名称来自于圣彼得堡附近的科特林岛。虽然与Java语法并不兼容，但在JVM环境中Kotlin被设计成可以和Java代码相互运作，并可以重复使用如Java集合框架等的现有Java引用的函数库。Hathibelagal写道，“如果你正在为Android开发寻找一种替代编程语言，那么应该试下Kotlin。它很容易在Android项目中替代Java或者同Java一起使用。”

### Rust

Rust( https://www.rust-lang.org/ )是由Mozilla主导开发的通用、编译型编程语言。设计准则为“安全、并发、实用”，支持函数式、并发式、过程式以及面向对象的编程风格。

Rust语言原本是Mozilla员工Graydon Hoare的私人项目，而Mozilla于2009年开始赞助这个项目，并且在2010年首次揭露了它的存在。也在同一年，其编译器源代码开始由原本的OCaml语言转移到用Rust语言，进行bootstrapping工作，称做rustc，并于2011年实际完成。这个可自我编译的编译器在架构上采用了LLVM做为它的后端。

第一个有版本号的Rust编译器于2012年1月发布。Rust 1.0是第一个稳定版本，于2015年5月15日发布。

Rust是在完全开放的情况下进行开发，并且相当欢迎社区的反馈。在1.0稳定版之前，语言设计也因为透过撰写Servo网页浏览器排版引擎和rustc编译器本身，而有进一步的改善。虽然它由Mozilla资助，但它其实是一个共有项目，有很大部分的代码是来自于社区的贡献者。

同时需要注意的是由于Rust的编程模型与其他的语言有较大的差异，学习曲线比较陡峭，但是Rust能带来其他语言不能带来的优势。

### Go

Go（又称Golang）(https://golang.org/) 是Google开发的一种静态强类型、编译型、并发型，并具有垃圾回收功能的编程语言。

罗伯特·格瑞史莫，罗勃·派克（Rob Pike）及肯·汤普逊于2007年9月开始设计Go，稍后Ian Lance Taylor、Russ Cox加入项目。Go于2009年11月正式宣布推出，成为开放源代码项目，支持Linux、macOS、Windows等操作系统。在2016年，Go被软件评价公司TIOBE 选为“TIOBE 2016 年最佳语言”。

2007年，Google设计Go，目的在于提高在多核、网络机器（networked machines）、大型代码库（codebases）的情况下的开发效率。当时在Google，设计师们想要解决其他语言使用中的缺点，但是仍保留他们的优点。

Go主要用于网络开发，例如服务器后端，国内的厂商使用Go作为服务器后端的比较多。

### Ruby

Ruby(http://www.ruby-lang.org/ )一种为简单快捷的面向对象编程（面向对象程序设计）而创的脚本语言，遵守GPL协议和Ruby License。
Ruby 是一种面向对象、命令式、函数式、动态的通用编程语言。在20世纪90年代中期由日本计算机科学家松本行弘（Matz）设计并开发。
遵守BSD许可证和Ruby License。它的灵感与特性来自于Perl、Smalltalk、Eiffel、Ada以及Lisp语言。由Ruby语言本身还发展出了JRuby（Java平台）、IronRuby（.NET平台）等其他平台的Ruby语言替代品。
减少编程时候的不必要的琐碎时间，令编写程序的人高兴，是设计Ruby语言的Matz的一个首要的考虑；其次是良好的界面设计。他强调系统设计必须强调人性化，而不是一味从机器的角度设想。

### Perl

Perl(http://www.perl.org/) 是弱类型的解释型动态语言，常用于处理文本数据、系统管理。Perl是高端、通用、解释型、动态的编程语言家族。最初设计者拉里·沃尔为了让在UNIX上进行报表处理的工作变得更方便，决定开发一个通用的脚本语言，而在1987年12月18日发表。目前，Perl语言家族包含两个分支Perl 5以及Perl 6。虽然Perl不是正式的首字母缩略词，但仍有各种各样的逆向首字母缩略词，包括“实用的提取和报告语言”。
Perl语言应用广泛，涵盖CGI、图形编程、系统管理、网络编程、金融、生物等领域。由于其灵活性，Perl被称为脚本语言中的瑞士军刀。鉴于Perl在实际工程应用中广泛使用，苹果公司的MacOS，Linux，FreeBSD等现代化操作系统默认安装Perl。

## 开源产品-开发平台

### Spring

Spring（http://www.springframwork.org/）框架为现代基于Java的企业应用提供了一个全面的编程和配置模型--在任何类型的部署平台上。Spring的一个关键要素是应用层面的基础架构支持。Spring专注于企业应用程序的 "管道"，因此团队可以专注于应用程序级的业务逻辑，而不必与特定的部署环境有不必要的联系。

### Struts

Struts（http://struts.apache.org/）是纯Java的的Web应用框架。Apache Struts是一个免费的、开源的MVC框架，用于创建优雅、现代的Java网络应用。它偏重于传统而非配置，使用插件架构进行扩展，并提供支持REST、AJAX和JSON的插件。

### Hibernate

Hibernate（http://www.hibernate.org/）是一种Java语言下的对象关系映射(ORM)解决方案。它是使用GNU宽通用公共许可证发行的自由、开源的软件。它为面向对象的领域模型到传统的关系型数据库的映射，提供了一个使用方便的持久化框架。
它的设计目标是将软件开发人员从大量相同的数据持久层相关编程工作中解放出来。无论是从设计草案还是从一个遗留数据库开始，开发人员都可以采用Hibernate。

Hibernate不仅负责从Java类到数据库表的映射（还包括从Java数据类型到SQL数据类型的映射），还提供了面向对象的数据查询检索机制，从而极大地缩短了手动处理SQL和JDBC上的开发时间。

### SPARK

Apache Spark（http://spark.apache.org/）是一个开源集群运算框架，最初是由加州大学柏克莱分校AMPLab所开发。相对于Hadoop的MapReduce会在运行完工作后将中介数据存放到磁盘中，Spark使用了存储器内运算技术，能在数据尚未写入硬盘时即在存储器内分析运算。Spark在存储器内运行程序的运算速度能做到比Hadoop MapReduce的运算速度快上100倍，即便是运行程序于硬盘时，Spark也能快上10倍速度。Spark允许用户将数据加载至集群存储器，并多次对其进行查询，非常适合用于机器学习算法。
使用Spark需要搭配集群管理员和分布式存储系统。Spark支持独立模式（本地Spark集群）、Hadoop YARN或Apache Mesos的集群管理。在分布式存储方面，Spark可以和 Alluxio, HDFS、 Cassandra、OpenStack Swift和Amazon S3等接口搭载。 Spark也支持伪分布式（pseudo-distributed）本地模式，不过通常只用于开发或测试时以本机文件系统取代分布式存储系统。在这样的情况下，Spark仅在一台机器上使用每个CPU核心运行程序。

简单来说，Spark是用于大数据的内存计算系统。用于在大数据环境下的计算任务。

### Lucene

Lucene（http://lucene.apache.org/）是ASF旗下一个专注于信息搜索的开源项目群， 包括了Lucene core(一个处理全文搜索的库)以及Solr（一个用于全文搜索的服务器）。一般的使用场景是搜索引擎的搜索内核。

### Dubbo

Apache Dubbo（https://github.com/apache/dubbo）是一个高性能、基于Java的开源RPC（远程过程调用，也就是说调用远程机器的函数）框架。是由阿里巴公司开源的服务框架，现在在Apache基金会下面托管。

### Webkit

WebKit（http://webkit.org/）是一种用来让网页浏览器绘制网页的排版引擎。它被用于Apple Safari。其分支Blink被用于基于Chromium的网页浏览器，如：Opera与Google Chrome。

### AngularJS

AngularJS（http://www.angularjs.org/）是一款由Google维护的开源JavaScript库，用来协助单一页面应用程序运行。它的目标是透过MVC模式（MVC）功能增强基于浏览器的应用，使开发和测试变得更加容易。

## 开源产品-服务端软件

### OpenStack

OpenStack（http://www.openstack.org）是一个开源的云计算管理平台项目，是一系列软件开源项目的组合。由NASA(美国国家航空航天局)和Rackspace合作研发并发起，以Apache许可证（Apache软件基金会发布的一个自由软件许可证）授权的开源代码项目。
OpenStack为私有云和公有云提供可扩展的弹性的云计算服务。项目目标是提供简单、可大规模扩展、丰富、标准统一的云计算管理平台。

### Cloud Foundry

Cloud Foundry（http://www.cloudfoundry.org/）是一个开源的多云应用平台作为服务（PaaS）该软件最初由VMware开发，转移到Pivotal软件公司（EMC、VMware和通用电气的合资公司），但随着VMware对Pivotal的接管，2019年底又被带回VMware。

### Docker

Docker（https://www.docker.com/） 是一个开放源代码软件，是一个开放平台，用于开发应用、交付（shipping）应用、运行应用。 Docker允许用户将基础设施（Infrastructure）中的应用单独分割出来，形成更小的颗粒（容器），从而提高交付软件的速度。

### Kubernetes

Kubernetes（K8s）（https://kubernetes.io/）是一个开源系统，用于自动化部署、扩展和管理容器化应用。它将组成应用的容器分组为逻辑单元，便于管理和发现。Kubernetes建立在谷歌15年运行生产工作负载的经验基础上，结合了社区的最佳理念和实践。与docker的区别在于，kubernets是用于大规模比如几十万个容器的管理平台。用于自动化管理容器。

### Apache HTTP

Apache HTTP Server（简称Apache）（http://httpd.apache.org/）是Apache软件基金会的一个开放源码的网页服务器软件，可以在大多数电脑操作系统中运行。由于其跨平台和安全性，被广泛使用，是最流行的Web服务器软件之一。它快速、可靠并且可通过简单的API扩展，将Perl／Python等解释器编译到服务器中。

### Tomcat

Tomcat（http://tomcat.apache.org/）是由Apache软件基金会属下Jakarta项目开发的Servlet容器，按照Sun Microsystems提供的技术规范，实现了对Servlet和JavaServer Page（JSP）的支持，并提供了作为Web服务器的一些特有功能，如Tomcat管理和控制平台、安全局管理和Tomcat阀等。由于Tomcat本身也内含了HTTP服务器，因此也可以视作单独的Web服务器。但是，不能将Tomcat和Apache HTTP服务器混淆，Apache HTTP服务器是用C语言实现的HTTPWeb服务器；这两个HTTP web server不是捆绑在一起的。Apache Tomcat包含了配置管理工具，也可以通过编辑XML格式的配置文件来进行配置。

### Jetty

Jetty（http://www.mortbay.org/jetty/）是一个纯粹的基于Java的网页服务器和Java Servlet容器。尽管网页服务器通常用来为人们呈现文档，但是Jetty通常在较大的软件框架中用于计算机与计算机之间的通信。Jetty作为Eclipse基金会的一部分

### Geronimo

Apache Geronimo（http://geronimo.apache.org/）是一个由Apache软件基金会开发的开源应用服务器，在Apache许可证下发布。

### JBoss

WildFly，原名JBoss AS，或简称JBoss(http://www.jboss.org/)，是由JBoss编写的应用服务器，现由红帽公司开发。WildFly是用Java编写的，实现了Java平台企业版（Java EE）规范。它可以在多个平台上运行。WildFly是免费的开源软件，受GNU Lesser General Public License (LGPL)2.1版本的要求。2014年11月20日，JBoss Application Server更名为WildFly。JBoss社区和JBoss企业应用平台等其他红帽JBoss产品并未更名。

### FileZilla Server

FileZilla(http://filezilla-project.org/)是一种快速、可信赖的FTP客户端以及服务器端开放源代码程序。

### Redis

Redis（http://www.redis.io/）是一个开源（BSD协议）的内存数据结构存储，用作数据库、缓存和消息中介。它支持字符串、哈希、列表、集合、带范围查询的排序集、位图、超日志、带半径查询的地理空间索引和流等数据结构。Redis内置了复制、Lua脚本、LRU驱逐、事务和不同级别的磁盘持久性，并通过Redis Sentinel和Redis Cluster自动分区提供高可用性。

### MongDB

MongoDB（http://www.mongodb.org/）是一个跨平台的面向文档的数据库程序。MongoDB被归类为NoSQL数据库程序，它使用类似JSON的文档和可选的模式。MongoDB由MongoDB公司开发，并以服务器端公共许可证（SSPL）授权。

### RabbitMQ

RabbitMQ（http://www.rabbitmq.com.）是一个开源的消息代理软件（有时也被称为面向消息的中间件），最初实现了高级消息队列协议（AMQP），后来通过插件架构扩展了对流文本定向消息协议（STOMP）、MQ遥测传输（MQTT）和其他协议的支持。
RabbitMQ 服务器程序是用 Erlang 编程语言编写的，并建立在用于集群和故障转移的开放电信平台框架上。用于与代理接口的客户端库可用于所有主要编程语言。

## 开源产品-开发工具

### Ansible

Ansible是一个开源的软件供应、配置管理和应用部署工具，使基础设施成为代码。它运行在许多类似Unix的系统上，既可以配置类似Unix的系统，也可以配置微软的Windows。它包括自己的声明性语言来描述系统配置。Ansible由Michael DeHaan编写，2015年被红帽收购。Ansible是无代理的，暂时通过SSH或Windows远程管理（允许远程执行PowerShell）远程连接来完成任务。

### VScode

Visual Studio Code是微软为Windows、Linux和macOS制作的免费源码编辑器。功能包括支持调试、语法高亮、智能代码完成、代码片段、代码重构和嵌入式Git。用户可以更改主题、键盘快捷键、偏好，并安装扩展，增加额外的功能。

### Eclipse

Eclipse（http://www.eclipse.org/）是著名的跨平台开源集成开发环境（IDE）。最初主要用来Java语言开发，目前亦有人通过插件使其作为C++、Python、PHP等其他语言的开发工具。Eclipse的本身只是一个框架平台，但是众多插件的支持，使得Eclipse拥有较佳的灵活性，所以许多软件开发商以Eclipse为框架开发自己的IDE。

### NetBeans

NetBeans（http://www.netbeans.org/）是由太阳微系统（Sun Microsystems）创建的开放源代码的软件开发工具，是一个开发框架，可扩展的开发平台，可以用于Java，C语言／C++，PHP，HTML5等程序的开发，本身是一个开发平台，可以通过扩展插件来扩展功能。

在NetBeans Platform平台中，应用软件是用一系列的软件模块（modular software components）建构出来。而这些模块是一个jar档（Java archive file）它包含了一组Java程序的类别而它们实现全依据依NetBeans定义了的公开接口以及一系列用来区分不同模块的定义描述档（Manifest file）。有赖于模块化带来的好处，用模块来建构的应用程序可只要加上新的模块就能进一步扩展。由于模块可以独立地进行开发，所以由NetBeans平台开发出来的应用程序就能利用着第三方软件，非常容易及有效率地进行扩展。

### Apache Ant

Apache Ant（http://ant.apache.org/）是一个将软件编译、测试、部署等步骤联系在一起加以自动化的一个工具，大多用于Java环境中的软件开发。由Apache软件基金会所提供。默认情况下，它的buildfile(XML文件)名为build.xml。

### Apache Maven

Maven（http://maven.apache.org/）是一个主要用于Java项目的构建自动化工具。Maven也可以用来构建和管理用C#、Ruby、Scala和其他语言编写的项目。Maven项目由Apache软件基金会托管，以前是Jakarta项目的一部分。

### CVS

CVS（http://www.nongnu.org/cvs/）代表协作版本系统或者并发版本系统，是一种版本控制系统，方便软件的开发和用户协同工作。很多开源或者自由软件项目都使用CVS作为其程序员之间的中心点，以便能够综合各程序员的改进和更改。这些项目包括：Gnome、KDE、GIMP、Wine等。CVS的使用获GNU通用公共许可证授权。这是一个将一组文件放在层次目录树中以保持同步的系统。人们可以从CVS服务器上更新他们的本地层次树副本，并将修改的结果或新文件发回；或者删除旧文件。

CVS基于客户端/服务器结构的行为使得其可容纳多用户，构成网络也很方便。这一特性使得CVS成为位于不同地点的人同时处理数据文件（特别是程序的源代码）时的首选（现已被Git、SVN等逐渐替代）。

### Subversion

Apache Subversion（简称SVN）（http://subversion.tigris.org/），一个开放源代码的版本控制系统，相较于RCS、CVS，它采用了分支管理系统，它的设计目标就是取代CVS。互联网上很多版本控制服务已从CVS转移到Subversion。

### GIT

Git（http://git-scm.com）是一个自由和开源的分布式版本控制系统，旨在以快速和高效的方式处理从小型到大型项目的一切事务。

git（/ɡɪt/）是一个分布式版本控制软件，最初由林纳斯·托瓦兹(Linux的创造者)创作，于2005年以GPL发布。最初目的是为更好地管理Linux内核开发而设计。

git最初的开发动力来自于BitKeeper和Monotone。git最初只是作为一个可以被其他前端（比如Cogito或Stgit）包装的后端而开发的，但后来git内核已经成熟到可以独立地用作版本控制。很多著名的软件都使用git进行版本控制，其中包括Linux内核、X.Org服务器和OLPC内核等项目的开发流程。

同时github是一个以git作为主要版本控制工具的开源社区，请注意github与git之间的区别，Github是一个开源代码社区主要使用git作为代码版本管理工具，Git是代码管理工具。

### Bugzilla

Bugzilla（http://www.bugzilla.org/）是一个强大的、功能丰富的、成熟的缺陷跟踪系统，或者说缺陷跟踪系统。缺陷跟踪系统允许开发人员团队有效地跟踪产品中未完成的bug、问题、问题、增强和其他变更请求。简单的缺陷跟踪功能通常内置在集成的源代码管理环境中，如Github或其他基于网络的或本地安装的同类产品。我们发现，当企业无法满足这些系统的功能时，就会转向使用Bugzilla，例如，因为他们需要工作流管理、错误可见性控制（安全）或自定义字段。

Bugzilla既是自由的，也是免费的。大多数商业缺陷跟踪软件厂商都要收取巨额的许可费。尽管Bugzilla是免费的，但它有许多功能是昂贵的和免费的同类软件所缺乏的。因此，Bugzilla被全球成百上千的组织所使用。

### JUnit

Junit（http://sourceforge.net/projects/junit/）是一个编写可重复测试的简单框架。它是单元测试框架xUnit架构的一个实例。

## 开源产品-桌面应用

### GNOME

GNOME（http://www.gnome.org/）是一个完全由自由软件组成的桌面环境。它的目标操作系统是Linux，但是大部分BSD系统亦支持GNOME。
GNOME是由志愿贡献者和受雇贡献者组成的GNOME计划开发，其最大的公司贡献者为红帽公司。它是一个为开发软件框架、基于这些框架来开发客户端软件及协调软件翻译和开发无障碍软件的项目。
GNOME最初是GNU网络对象模型环境（GNU Network Object Model Environment）的缩写，但是已经被废弃了。是GNU计划的一部分，并且是由志愿者开发的。
GNOME为Linux系统提供了一个桌面环境，也就是说提供了可视化的操作环境，类似于Windows的操作环境。

### OpenOffice.org

OpenOffice.org（http://www.openoffice.org/），一般称呼为OpenOffice，简写作OOo，是一个开源的办公包软件。起源于Sun系统1999年从StarDivision收购的StarOffice。 OpenOffice包含了文字处理器（Writer）、电子表格（Calc）、演示程序（Impress）、绘图软件（Draw）、数学公式编辑器（Math）以及关系数据库管理系统（Base）。[8]它文件格式默认为开放文档格式（ODF）。该格式从OpenOffice.org发起，后来成为ISO/IEC标准格式。它也可读取许多不同的文件格式，尤其是Microsoft Office生成的那些。

Sun电脑在2000年7月将StarOffice开源，发布OpenOffice.org，以此与Microsoft Office竞争。2002年5月1日，软件版本1.0公布。

2011年，太阳微系统（Sun Microsystems）的所有者甲骨文公司宣布，他们将不再为OpenOffice的商业版提供支持，旋即将该项目捐赠给了Apache软件基金会。Apache将软件重命名为Apache OpenOffice。

OpenOffice.org主要为Linux、Microsoft Windows和Solaris操作系统设计，后来又加入了OS X版，并可移植到其他操作系统上。软件在GNU宽通用公共许可证第3版（LGPL）下授权。

### Emacs

Emacs（http://www.gnu.org/software/emacs/），是一个文本编辑器家族，具有强大的可扩展性，在程序员和其他以技术工作为主的计算机用户中广受欢迎。最初由Richard Stallman于1975年在MIT协同盖伊·史提尔二世共同完成。这一创意的灵感来源于TECO宏编辑器TECMAC和TMACS，它们是由盖伊·史提尔二世、Dave Moon、Richard Greenblatt、Charles Frankston等人编写的宏文本编辑器。

自诞生以来，Emacs演化出了众多分支，其中使用最广泛的两种分别是：1984年由理查·斯托曼发起并由他维护至2008年的GNU Emacs，以及1991年发起的XEmacs。XEmacs是GNU Emacs的分支，至今仍保持着相当的兼容性。它们都使用了Emacs Lisp这种有着极强扩展性的编程语言，从而实现了包括编程、编译乃至网络浏览等等功能的扩展。

在Unix文化里，Emacs是黑客们关于编辑器之战的两大主角之一，它的对手是vi（Vim），（VIM万岁！）。

### Firefox

Mozilla Firefox（http://www.mozilla.com/en-US/firefox/），通称Firefox，中文也通称火狐，是一个自由及开源的网页浏览器，由Mozilla基金会及其子公司Mozilla公司开发。Firefox支持Windows、macOS及Linux，其移动版支持Android及Firefox OS，这些版本的Firefox使用Gecko来排版网页，Gecko是一个运行当前与预期之网页标准的排版引擎，而在2015年发布的Firefox for iOS则非使用Gecko。

Firefox于2002年由Mozilla社区成员创建，当时叫做“Phoenix”，因为社区成员们想要一个独立的浏览器，而非Mozilla Application Suite这样的包。即使在测试阶段，Firefox也在测试者中颇为流行，并因其速度、安全性及扩展组件而受称赞。Firefox于2004年11月首次发布，并且9个月内下载量超过6000万，获取了巨大的成功，Internet Explorer的主导地位首次受到了挑战。Firefox被认为是Netscape Navigator的精神续作，因为Netscape（网景公司）于1998年被AOL收购前创建了Mozilla社区。

Firefox全球市占率为35％至40%，为全球第二流行的网页浏览器。Firefox在某些国家还是最流行的网页浏览器，如在萨摩亚、德国、厄立特里亚及古巴，Firefox市占率分别为61.05%、38.36%、79.39%及85.93%。据Mozilla统计，截至2014年12月，Firefox在全世界拥有5亿用户。

### Thunderbird

Mozilla Thunderbird（http://www.mozillamessaging.com/en-US/thunderbird/）非正式中文名称为雷鸟，是由Mozilla基金会研发的一款自由及开放源码的跨平台电邮客户端、新闻阅读器、聚合器以及即时通信软件。此软件默认安装于Ubuntu之上。

2004年12月7日，Mozilla发布了Mozilla Thunderbird的1.0版本，并于首三日即获得超过五十万次下载，而十日内已有一百万次下载。

2012年7月6日，Mozilla宣布由于此前为增加Thunderbird功能的努力大多没有成果，故将降低其开发的优先性。新的开发模式将转为“延长支持版本”，只提供安全性及稳定性更新，而新功能的开发则交予社区负责。

2015年12月1日，Mozilla运行董事长米切尔·贝克发表一份公司内部通告，指出Thunderbird的开发须从Firefox的开发中分拆开。他指Thunderbird的开发者花费不少功夫于适应Mozilla的技术，而Firefox的研发亦因须支持Thunderbird而受阻。另外他亦认为Thunderbird将难以拥有如Firefox一般的影响力。如此同时，Mozilla基金会宣布为Thunderbird提供暂时性的法律及资金援助。

### GIMP

GIMP（http://www.gimp.org/）的首字母组成）是一个自由及开放源代码的位图图像编辑器，用于图像照片润饰及编辑、自由绘图、调整大小、裁剪、照片蒙太奇、装换图像格式以及其他专业任务。

### FreeMind

FreeMind（http://sourceforge.net/projects/freemind/）是一款跨平台的、基于GPL协议的自由软件，用Java编写，是一个用来绘制思维导图的软件。其产生的文件格式后缀为.mm。可用来做笔记、脑图记录、头脑风暴等。

### 7-Zip

7-Zip（http://www.7-zip.org/）是一个开放源码的数据压缩程序，主要用在Microsoft Windows操作系统，Unix-like的操作系统如Linux与FreeBSD下面有7-zip的移植版本p7zip可以使用。它提供命令行接口的程序或图形用户界面的程序，而且可以与资源管理器结合。7-Zip是自由软件，由伊戈尔·帕夫洛夫于1999年开始发展，并把主体在GNU LGPL下发布；加密部分，使用高级加密标准（AES）的代码，使用BSD许可证发布；解压RAR部分，使用RAR特定的许可协议。

> OpenSource.com推荐的替代软件清单，供参考

## Creative Tools

- Photoshop

### GIMP, Pinta, Krita

https://opensource.com/life/12/6/design-without-debt-five-tools-fordesigners

### Dreamweaver

Aptana Studio, BlueGriffon, NetBeans,SeaMonkey, Aloha Editor
https://opensource.com/alternatives/dreamweaver
- AutoCAD
BRL-CAD, FreeCAD, LibreCAD
https://opensource.com/alternatives/autocad

### Video Editing

Pitivi, OpenShot, Cinelerra, KDEnlive, Blender
https://opensource.com/article/18/4/new-state-video-editing-linux

### Microsoft Publisher

Scribus, LibreOffice, LaTeX or other markuplanguages
https://opensource.com/alternatives/microsoft-publisher

### Chat Tools

Slack IRC, Let’s Chat, Mattermost, Rocket.Chat, Riot.im
https://opensource.com/alternatives/slack
- WhatsApp
Line, Riot.im, Signal, Threema, Viber, Wire,
https://opensource.com/article/19/3/open-messenger-client
- Skype
Jami, Jitsi, Linphone, Riot, Wire, Pidgin
https://opensource.com/alternatives/skype

## Office Tools

### Microsoft Access

LibreOffice Base, DB Browser for SQLite, Kexi,
nuBuilder Forte
https://opensource.com/alternatives/access

### Gmail

Roundcube, Zimbra, SquirrelMail, Rainloop, Cypht https://opensource.com/alternatives/gmail
https://opensource.com/article/19/1/productivity-tool-cypht-email

### Google Docs

CryptPad https://opensource.com/article/19/1/productivity-tool-cryptpad

### Google Sheets

EtherCalc https://opensource.com/article/19/7/get-going-ethercalc

## Project Management Tools

### Project Management Tools

MyCollab, Odoo, Taiga, Phabricator, Tuleap Open ALM, Agilefant, Redmine, Gitlab, OpenProject,LibrePlan, ProjectLibre
https://opensource.com/business/16/3/top-project-managementtools-2016

### Trello

Taiga, Kanboard, Wekan, Restyaboard, Taskboard https://opensource.com/alternatives/trello

## Notetaking Tools

### Evernote Joplin, Turtl, Paperwork, Laverna, Permanote,Brainstorm

https://opensource.com/article/17/12/joplin-open-source-evernotealternative
https://opensource.com/article/17/12/using-turtl-open-sourcealternative-evernote
https://opensource.com/alternatives/evernote

## News and Social Media

- Pocket
Wallabag
https://opensource.com/article/18/7/wallabag
- Social Media

### Mastodon, Textile, PixelFed

https://opensource.com/article/19/1/open-source-social-mediaalternatives

## Filesharing

### Dropbox

ownCloud, NextCloud, Seafile, OnionShare, Pydio Cells
https://opensource.com/alternatives/dropbox

## CRM Tools

### Salesforce

Corteza https://opensource.com/article/19/8/corteza-open-sourcealternative-salesforce

### CRM Tools

EspoCRM, SuiteCRM, Oro CRM, CiviCRM,Fat Free CRM, Zurmo
https://opensource.com/business/16/2/top-6-open-source-crmtools-2016

## Security

### LastPass

Bitwarden https://opensource.com/article/18/3/managing-passwords-bitwarden
https://opensource.com/life/14/7/managing-passwords-open-sourceway

## Personal Finance

### Personal Finance Tools

GnuCash, HomeBank, KMyMoney, Money Manager Ex, Skrooge, Spreadsheets
https://opensource.com/life/17/10/personal-finance-tools-linux

## Gaming

### Minecraft, Steam

Lutris, Minetest, Terasology, Voxel.js, TrueCraft,Craft
https://opensource.com/alternatives/minecraft
https://opensource.com/article/18/10/lutris-open-gaming-platform

### More

More open source alternatives https://opensource.com/tags/alternatives
https://opensource.com/alternatives

## 开源与教育

> 学生可以参与的重要的开源活动、论坛、……

## 国内高校的开源发展

- 清华大学

## 清华大学 TUNA 协会 https://tuna.moe/

- 北京大学

## 北京大学开源软件协会http://www.pkuosa.org/

- 中国科技大学

## http://lug.ustc.edu.cn/wiki/

### 中国科学院开源软件协会 OpenCAS

中国科学院开源软件协会（又称 OpenCAS）是于 2006 年在中国科学院大学成立的高校学生社团，是一个由国科大本部同学和中科院各所的研究生们自发组成的开源爱好者社区。协会由中国科学院大学校团委指导，中国科学院计算机网络信息中心和中国科学院
- 北京航空航天大学
- 华东师范大学

## 国内活动

- Google开源夏令营

- GitHub Student Developer Pack使学生可以免费使用流行的开发工具和服务。GitHub与Bitnami，DigitalOcean，Namecheap等网站合作，为符合条件的学生提供如域名、虚拟机等免费计算资源。

- GitHub在2016年宣布启动GitHub校园专家计划[84]，以培训和鼓励学生在其大学中发展技术社区。校园专家计划面向全球18岁以上的大学生开放。[85] GitHub Campus Experts是GitHub资助面向学生的活动和社区的主要方式之一，Campus Experts获得培训，资金和运行活动和发展社区的其他资源的访问权。要成为校园专家，申请人必须完成在线培训课程，该课程包含旨在提高社区领导能力的多个模块。
https://education.github.com/students/experts

- 开源星期五

## https://opensourcefriday.com/

- JetBrains 学生许可
https://www.jetbrains.com/zh-cn/opensource/

- LinuxCon+ContainerCon+CloudOpen（LC3）

### 中国开源年会 COSCon

https://kaiyuanshe.cn/categories/Activity/Summit/

- RubyConf China

## http://rubyconfchina.org/

- 中国计算机大会

## https://cncc.ccf.org.cn/

- Qcon全球软件开发大会

## https://qcon.infoq.cn/

- PyCon China

## http://cn.pycon.org/

- OSC源创会
https://www.oschina.net/event/ych

•

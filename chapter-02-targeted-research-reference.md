# 第二章定向研究参考

## 目的

本文档用于支撑第二章《自由软件、开源软件与许可证》的后续正文写作。它只处理第二章必须核查的概念定义、制度边界和常见许可证的最小差异，不扩展到社区治理、项目工程流程或复杂法律实务。

本轮研究的目标不是替代法律意见，而是为本科生层面的教材写作建立一套准确、稳定、可讲授的表述基础。

## 研究范围

本轮只核查以下问题：

- FSF 对自由软件的官方定义
- OSI 对开源软件与 Open Source Definition 的官方定义
- “开源不是没有版权”“公开源码不自动等于开源”应如何稳妥表述
- MIT、BSD-3-Clause、Apache-2.0、GPL、LGPL、AGPL、MPL-2.0 的最小差异点
- 对学生团队项目而言，许可证选择应如何降维表达

## 已核查的关键结论

### 1. 自由软件的核心不是价格，而是四项自由

GNU / FSF 的《What is Free Software?》明确给出自由软件的四项基本自由：

- 运行程序的自由
- 研究程序并按自己的需要修改它的自由
- 再分发副本的自由
- 分发修改版本的自由

同时，FSF 明确指出：

- 获取源代码是研究和修改的前提
- “free software” 不是“noncommercial”
- 自由软件允许商业使用、商业开发和商业分发

写作含义：

- 第二章必须明确区分“自由”与“免费”
- “自由软件反商业”这一说法应直接判为误解

来源：

- GNU / FSF, *What is Free Software?*  
  <https://www.gnu.org/philosophy/free-sw.en.html>

### 2. 开源软件的官方判断标准不是“看得到源码”，而是是否符合 OSD

OSI 的《The Open Source Definition》明确写道：

- Open source 不只是 access to the source code
- 开源软件的分发条款必须符合 OSD 的标准

其中最关键的几项包括：

- Free Redistribution
- Source Code
- Derived Works

写作含义：

- 第二章应把“开源”写成一种基于许可证的制度安排，而不是单纯的技术状态
- “开放了源代码就是开源”这一说法应直接判为误解

来源：

- OSI, *The Open Source Definition*  
  <https://opensource.org/osd>

### 3. “没有许可证”时，公开仓库并不等于别人获得了常规开源协作许可

GitHub 官方的 Choose a License 页面明确说明：

- 作品默认受版权保护
- 如果没有明确许可证，通常意味着他人没有获得使用、修改和分享的许可
- 即使 GitHub 平台允许他人查看和 fork 仓库，这也不等于获得了常规开源协作所需要的完整许可

GitHub Docs 也明确鼓励开源项目在仓库中加入可检测的许可证文件。

写作含义：

- 第二章很适合用“公开仓库但没有 `LICENSE`”作为开场场景
- 这能直接说明许可证为什么不是装饰文件

来源：

- Choose a License, *No License*  
  <https://choosealicense.com/no-permission/>
- GitHub Docs, *Licensing a repository*  
  <https://docs.github.com/github/creating-cloning-and-archiving-repositories/licensing-a-repository>

### 4. MIT 的最小特征是：极简宽松，但要求保留版权和许可声明

OSI 的 MIT License 页面表明：

- 使用、复制、修改、合并、发布、分发、再许可和销售都被允许
- 条件是保留 copyright notice 和 permission notice
- 另附免责条款

写作含义：

- 对本科生来说，MIT 可以讲成“最常见的极简宽松式许可证之一”
- 但不能讲成“没有任何义务”

来源：

- OSI, *The MIT License*  
  <https://opensource.org/license/mit/>

### 5. BSD-3-Clause 与 MIT 的差异点可以压缩到“保留声明 + 不得背书”

OSI 的 BSD-3-Clause 页面显示：

- 可在源代码和二进制形式中再分发和使用
- 需要保留版权声明、条件列表和免责声明
- 额外有一条重要限制：不得使用原作者或贡献者姓名为衍生产品背书

写作含义：

- 第二章不需要把 BSD 讲成很多变体的迷宫
- 对本科生来说，抓住 “MIT 非常短，BSD-3-Clause 多一个 no-endorsement 约束” 已经足够

来源：

- OSI, *The 3-Clause BSD License*  
  <https://opensource.org/license/bsd-3-clause>

### 6. Apache-2.0 适合讲成“宽松式许可证，但更重视专利与 NOTICE”

Apache Software Foundation 的官方说明强调：

- Apache License 2.0 是一套 copyright and patent licensing terms
- 可以被 ASF 之外的项目使用
- 分发时通常需要包含 LICENSE
- Apache 的分发还非常强调 NOTICE 文件

ASF 还专门说明：

- Apache-2.0 被 FSF 视为 free software license
- 与 GPLv3 单向兼容，但不与 GPLv2 兼容

写作含义：

- 第二章中 Apache-2.0 可以作为“宽松式，但比 MIT/BSD 更强调专利和 NOTICE”来讲
- 不需要在正文中展开所有兼容性细节，但要提醒其制度复杂度高于 MIT

来源：

- Apache, *Applying the Apache license, version 2.0*  
  <https://www.apache.org/legal/apply-license>
- Apache, *Apache License v2.0 and GPL Compatibility*  
  <https://www.apache.org/licenses/GPL-compatibility>

### 7. GNU 家族的最小区分可以这样稳定表达

GNU 官方许可证页面给出的最小差异点是：

- GPL：GNU 家族中最典型的 copyleft 许可证
- LGPL：主要用于一部分库，copyleft 范围较 GPL 收窄
- AGPL：在 GPL 基础上增加了网络交互场景下获得源码的要求

写作含义：

- 第二章不用陷入“传染性”口号化表达
- 更稳妥的写法是：
  - GPL：强 Copyleft
  - LGPL：面向库场景的较弱 Copyleft
  - AGPL：把网络服务场景也纳入源代码开放义务考虑

来源：

- GNU / FSF, *Licenses*  
  <https://www.gnu.org/licenses/licenses.html>

### 8. MPL-2.0 的最佳定位是“文件级弱 Copyleft”

Mozilla 的 MPL 2.0 FAQ 明确给出非常适合教学的总结：

- MPL 是 simple copyleft license
- 它的 copyleft 是 file-level
- 新文件若不包含 MPL 代码，不必自动落到 MPL 下

FAQ 还给出与 LGPL、GPL 的对比：

- MPL：copyleft applies to files containing MPL code
- LGPL：copyleft applies to the library
- GPL：copyleft applies to all software based on GPL code

写作含义：

- 第二章里可以把 MPL 作为“介于 Apache 和 GPL 之间的一种弱 Copyleft 路径”来讲
- 这是帮助学生理解“Copyleft 也有强弱层次”的最好例子之一

来源：

- Mozilla, *Mozilla Public License 2.0*  
  <https://www.mozilla.org/en-US/MPL/2.0/>
- Mozilla, *MPL 2.0 FAQ*  
  <https://www.mozilla.org/en-US/MPL/2.0/FAQ/>

## 对旧材料的直接修正建议

基于本轮研究，第二章在迁移旧材料时应直接做以下修正：

### 应删除或避免直接复用的说法

- “开源就是没有版权”
- “开源就是反商业”
- “自由软件都反对版权”
- 用单一“传染性”口号替代 GPL / LGPL / AGPL / MPL 的真实差异
- “仓库公开就可以随便用”的暗示性表述

### 应改成更稳妥的写法

- 自由软件强调 freedom，不等于 gratis
- 开源的判断标准是是否符合 OSD，而不是源码是否可见
- 开源依赖版权和许可证来建立清晰的权利与义务边界
- MIT / BSD / Apache 属于宽松式许可证，但条件并不完全相同
- GPL / LGPL / AGPL / MPL 都属于不同强度的 Copyleft 传统

## 对第二章写法的具体建议

基于本轮研究，第二章正文建议采用以下叙述节奏：

1. 从“公开仓库却没有许可证”的场景开场  
   先让学生意识到制度边界问题。

2. 先讲自由软件与开源软件的关系  
   把理念差异和共同基础分开。

3. 再讲许可证为什么必要  
   把版权、分发、衍生作品、Notice、专利授权放进同一制度框架。

4. 再讲常见许可证的最小差异  
   只讲最值得本科生记住的区分点。

5. 最后落到学生项目如何选择许可证  
   让本章直接服务团队项目主线。

## 当前仍可延后的问题

以下问题可以延后到第二轮研究或正文修订阶段，不必阻塞第二章起稿：

- GPLv2、GPLv3、LGPLv2.1、LGPLv3 的更细区别
- Apache-2.0 与 GPL 兼容性的完整矩阵
- REUSE / SPDX / OpenChain 在课程中讲到多深
- 模型权重、数据集和文档素材在许可证上的更复杂边界

## 当前结论

第二章已经具备进入书稿提纲写作的条件。

本轮研究最大的作用是把第二章最容易讲错的几点固定下来：

- 自由软件不是“免费软件”
- 开源不是“公开源码”这么简单
- 许可证不是装饰文件，而是开源协作的制度基础
- 宽松式、弱 Copyleft、强 Copyleft 可以用少量关键点建立稳定认知

下一步可以据此把第二章骨架推进为书稿提纲，然后直接进入正文初稿。

# 第一章定向研究参考

## 目的

本文档用于支撑第一章《开源的起源与发展》的后续正文写作。它只处理第一章必须核查的历史节点、组织关系和代表性案例，不扩展到许可证细节、治理文件或 GitHub 操作层。

本轮研究的目标不是“把第一章所有资料都查完”，而是先校正最容易在旧材料中产生历史误差的关键点。

## 研究范围

本轮只核查以下问题：

- GNU 项目、GNU 宣言、FSF 的时间线
- Linux 与 GNU 的关系应如何准确表述
- “open source” 一词和 OSI 的形成过程
- Netscape / Mozilla 在 1998 年的作用
- Apache 作为社区化、基金会化案例的历史位置
- GitHub 与 Microsoft / GitHub 事件是否适合做第一章开场案例
- 旧稿中哪些历史说法应删除或避免复用

## 已核查的关键结论

### 1. GNU 项目的宣布时间与实际启动时间要区分

- GNU 项目的初始公告发布于 **1983 年 9 月 27 日**
- 但 GNU 项目的实际启动并非在公告当天，而是 **1984 年 1 月开始**

写作含义：

- 第一章应明确区分“宣布（announcement）”与“开始开发（start of work）”
- 旧稿中如果把 1983 和 1984 混写，应统一校正

来源：

- GNU 初始公告：<https://www.gnu.org/gnu/initial-announcement.en.html>
- GNU 历史概览：<https://www.gnu.org/gnu/gnu-history.en.html>

### 2. GNU 宣言写于 1985 年，FSF 成立于 1985 年 10 月

- GNU 历史页面明确说明，较完整版本的 **GNU Manifesto** 发布于 **1985 年 3 月**
- FSF 历史页面和 GNU 历史页面都表明，**Free Software Foundation（FSF）成立于 1985 年 10 月**

写作含义：

- 第一章中可以用“1983 公告 -> 1984 启动 -> 1985 GNU 宣言与 FSF”作为稳定主线
- 不应把 GNU 宣言、FSF、GPL 等混成一个模糊的“80 年代中期事件”

来源：

- GNU Manifesto：<https://www.gnu.org/gnu/manifesto.en.html>
- GNU 历史概览：<https://www.gnu.org/gnu/gnu-history.en.html>
- FSF 历史：<https://www.fsf.org/history/>

### 3. 第一章应区分“自由软件运动”与“开源运动”

- GNU 与 FSF 官方材料明确把 GNU 项目放在 **Free Software Movement** 语境中
- GNU 官方页面甚至明确提醒，不应把 GNU 与 “open source” 直接等同，因为该术语是 **1998 年** 才由另一批人提出

写作含义：

- 第一章不能把“GNU 诞生”直接写成“开源运动的正式开始”
- 更准确的写法应是：
  - GNU / FSF 启动了自由软件运动
  - 这一历史脉络为后来的开源运动奠定了条件
  - “open source” 作为术语和组织化推进，出现在 1998 年

来源：

- GNU Manifesto：<https://www.gnu.org/gnu/manifesto.en.html>
- GNU 历史概览：<https://www.gnu.org/gnu/gnu-history.en.html>

### 4. Linux 的准确表述应是：1991 年出现，1992 年与 GNU 形成可用系统组合

- GNU 历史概览指出：
  - GNU 到 1990 年已完成大部分主要组件，但缺内核
  - **Linux 内核由 Linus Torvalds 在 1991 年开发**
  - **1992 年 Linux 成为自由软件**
  - GNU 与 Linux 的组合形成了完整的自由操作系统
- kernel.org 官方页面则确认 Linux 是 Linus Torvalds 编写、由网络上的协作者共同发展的 Unix-like kernel

写作含义：

- 第一章中应避免旧稿那种“Linus 发布 GNU/Linux”一类不精确写法
- 更准确的表述是：
  - Linux 先作为内核项目出现
  - GNU 提供了大量系统组件
  - 二者结合推动自由软件系统真正可用

来源：

- GNU 历史概览：<https://www.gnu.org/gnu/gnu-history.en.html>
- Linux Kernel 官方介绍：<https://www.kernel.org/linux.html>

### 5. “open source” 一词与 OSI 的形成集中发生在 1998 年，而不是 1996 年

- OSI 官方历史页面给出的说法是：
  - **1998 年 2 月 3 日** 的一次策略会议上，“open source” 这一标签被确定下来
  - 该词最初由 **Christine Peterson** 提出
  - OSI 于 **1998 年 2 月下旬** 由 **Eric Raymond** 和 **Bruce Perens** 共同创建
  - Open Source Definition 在 **1998 年 2 月** 基于 Debian Free Software Guidelines 修订而来

写作含义：

- 旧材料中“1996 年 Tim O'Reilly 召集会议并产生开源一词”的表述应删除或重写
- 如果第一章要写“open source”的提出，应直接以 OSI 官方历史为准

来源：

- OSI 官方历史：<https://opensource.org/about/history-of-the-open-source-initiative>

### 6. Netscape / Mozilla 在 1998 年是“open source”进入主流视野的重要催化事件

- Mozilla 官方历史指出：
  - Netscape 在 **1998 年 1 月 22 日 / 23 日** 宣布将浏览器源码开放
  - Mozilla 项目随着源码发布在 **1998 年** 形成
  - **1998 年 3 月 31 日** 首个开发者版本源码正式发布

写作含义：

- 第一章写到 1998 年时，不应只写“OSI 出现”
- 更好的历史叙述是：
  - Netscape 开放源码事件制造了新的传播窗口
  - OSI 与 “open source” 标签在这个窗口中迅速形成
  - Mozilla 成为企业开放源码与社区协作结合的早期标志性案例

来源：

- Mozilla history：<https://www.mozilla.org/en-US/about/history/>
- Mozilla 25 周年回顾：<https://blog.mozilla.org/en/mozilla/mitchell-baker-mozilla-25-anniversary/>
- Mozilla 历史档案：<https://www-archive.mozilla.org/mission.html>

### 7. 《大教堂与集市》应放在 1997 年，而不是更早

- Eric Raymond 相关页面显示：
  - 《The Cathedral and the Bazaar》**首次正式发表 / 报告**是在 **1997 年 5 月** 的 Linux Kongress
  - 之后在 **1998 年 2 月** 的修订中，文内把 “free software” 改成了 “open source”

写作含义：

- 第一章中可以把 Raymond 的文章写成：
  - 1997 年对开放式开发模式的强有力叙事总结
  - 1998 年又被纳入 “open source” 的传播框架中
- 这比旧稿中笼统地说“97 年写了篇文章”更准确

来源：

- Eric Raymond 页面：<https://www.catb.org/~esr/writings/cathedral-bazaar/cathedral-bazaar/>
- 辅助页面：<https://www.catb.org/~esr/faqs/hacker-revenge.html>

### 8. Apache 是第一章中很适合用来说明“社区化与基金会化”的案例

- Apache 官方历史说明：
  - Apache Group 起源于 **1995 年 2 月** 的补丁协作
  - Apache Software Foundation 在 **1999 年 6 月** 正式成立
  - ASF 后来发展出 “The Apache Way” 这一社区与治理方法

写作含义：

- 第一章不必细讲 Apache 的治理机制
- 但可以用 Apache 来说明：
  - 开源不只是个人理想和代码共享
  - 它会进一步发展出稳定的社区、组织和制度支持

来源：

- Apache 官方历史：<https://www.apache.org/history/index.html>

### 9. GitHub 与 Microsoft / GitHub 事件适合作为第一章开场案例

- GitHub 官方 Press 页面写明 GitHub 成立于 **2008 年 2 月**
- GitHub 官方博客写明 GitHub 于 **2008 年 4 月 10 日** 正式上线
- Microsoft 官方新闻稿写明：
  - **2018 年 6 月 4 日** 宣布收购 GitHub
  - **2018 年 10 月 26 日** 完成收购

写作含义：

- 第一章完全可以用“Microsoft 收购 GitHub”作为开场案例
- 这个案例的优势在于，它能把以下问题同时拉进来：
  - 为什么曾与开源对立的公司会拥抱开源
  - 开源为何从边缘运动变成软件产业基础设施
  - 平台化如何改变开源生态

来源：

- GitHub Press：<https://github.com/about/press>
- GitHub 10 周年文章：<https://github.blog/2018-04-10-ten-years-of-code/>
- Microsoft 宣布收购：<https://news.microsoft.com/en-my/2018/06/05/microsoft-to-acquire-github-for-7-5-billion/>
- Microsoft 完成交割：<https://blogs.microsoft.com/blog/2018/10/26/microsoft-completes-github-acquisition/>

## 对旧材料的直接修正建议

基于本轮研究，第一章在迁移旧材料时应直接做以下修正：

### 应删除或避免直接复用的说法

- “GNU 直接等于开源运动”
- “1996 年会议提出 open source 一词”
- “Linus 发布 GNU/Linux”这一类不区分内核与系统组件的写法
- 未核查来源的头衔性表述，例如旧稿中对 Stallman 的部分称谓
- “第一个开源软件是什么”这类容易引发争议、但对本章主线帮助有限的断言

### 应改成更稳妥的写法

- 把 GNU / FSF 写成自由软件运动的历史主线
- 把 1998 写成 “open source” 术语、OSI 组织化和 Netscape / Mozilla 事件叠加出现的关键年份
- 把 Linux 写成推动自由软件系统走向大规模可用的关键项目
- 把 Apache 和 GitHub 分别写成“基金会化”和“平台化”的代表节点

## 对第一章写法的具体建议

基于本轮研究，第一章正文建议采用以下叙述节奏：

1. 从 Microsoft / GitHub 开场  
   先抛出“为什么一个曾与开源冲突的商业巨头会收购全球最大的开源协作平台”。

2. 回到更早的软件共享与软件商品化转折  
   用 GNU 官方历史材料支撑，不必追逐过多早期争议性细节。

3. 再进入 GNU / FSF / 自由软件运动  
   强调问题意识、自由诉求和历史角色。

4. 再写 Linux、Mozilla、Apache  
   它们分别代表“可用系统形成”“企业开放源码催化”“社区制度化延展”。

5. 最后再收束到“为什么今天必须重新理解开源”  
   把后续的许可证、治理和工程流程作为自然引出，而不是另起炉灶。

## 当前仍可延后的问题

以下问题可以延后到第二轮研究或正文写作阶段，不必阻塞第一章起稿：

- 中国本土开源发展在第一章中放多少篇幅
- 第一章是否加入单独的“关键人物小传”侧栏
- 具体采用 GNU/Linux 还是 Linux 作为面向本科生的默认表述策略
- 是否在第一章正文中引入过多商业案例，还是把部分商业案例放入 `Case Library`

## 当前结论

第一章已经具备进入正文提纲写作的条件。

本轮研究最大的作用不是“增加很多新知识点”，而是把第一章最容易写错的历史关系校正清楚：

- GNU 与开源不是同一历史阶段
- 1998 是真正的术语与组织化转折点
- Linux、Mozilla、Apache、GitHub 应分别承担不同的历史象征角色

下一步可以据此把第一章骨架推进为书稿提纲，而不是继续泛化搜索。

# 第 5 章 案例教学包

## 对应章节与用途

- 对应书稿：[05-leveraging-open-source-software-resources.md](05-leveraging-open-source-software-resources.md)
- 配套学习指南：[chapter-05-study-guide.md](chapter-05-study-guide.md)
- 配套教学指南：[chapter-05-instructor-guide.md](chapter-05-instructor-guide.md)
- 本案例包用于帮助学生把“项目阅读”理解为形成整体判断的方法，而不是把仓库首页当作信息陈列页。

## 主案例与辅助案例

| 案例 | 本章主要说明什么 | 推荐观察对象 |
| --- | --- | --- |
| tldr-pages / tldr | 低成本第一轮阅读路径 | `README.md`、`CONTRIBUTING.md`、版本记录、工作流 |
| VS Code | GitHub-native 成熟项目如何把公共对象摆在外部人面前 | Issue 模板、PR 模板、`.github/`、Checks、版本说明 |
| Linux | 长期基础设施项目的公共证据分布不在首页表层 | `Documentation/`、`MAINTAINERS`、长期维护与版本规则 |
| OpenClaw | 现代 AI 原生项目的公共入口与边界判断 | 安装文档、配置说明、`CONTRIBUTING.md`、`SECURITY.md`、发布对象 |

## 推荐课堂使用方式

- 先用 `tldr-pages/tldr` 走一遍书稿里的行走式阅读演示，让学生知道“第一轮阅读”到底在看什么。
- 再用 VS Code 说明成熟 GitHub-native 项目如何把模板、规则和工程门禁直接暴露给外部人。
- 用 Linux 做反衬，说明重要项目的公共证据未必集中在仓库首页表层。
- 最后用 OpenClaw 说明现代 AI 项目也必须被当作“公共对象集合”来判断，而不是只看是否开放了参数或仓库。
- 整个案例包都服务于“阅读与判断”；认领评论、PR 结构和 review 往返留到第 6 章案例包再展开。

## 与书稿贯穿对象的配合

- `tldr-pages/tldr` 对应正文中的行走式阅读演示，用来承接图 5-1。
- VS Code 对应正文中对模板、`CODEOWNERS`、工作流和 Pull Request 结构的分析，用来承接图 5-2 与表 5-1。
- Linux 对应正文中的“公共证据分布不在同一层”讨论，用来校正读者对陌生项目的阅读预期。
- OpenClaw 对应正文中“现代 AI 原生项目的公共入口与边界判断”讨论，用来帮助读者理解 AI 项目对象。

## 推荐讨论问题

- 为什么不同类型项目公开协作证据的位置并不相同？
- 为什么一个仓库即使看起来很热闹，也未必适合继续参与？
- `tldr-pages/tldr` 与 VS Code 的第一轮阅读重点为什么不同？
- 为什么 Linux 需要沿着维护文档和维护者网络继续往下读？
- 面对 OpenClaw 这样的 AI 项目时，为什么不能只看“是否开放权重”？

## 与团队项目主线的连接

- 团队可借 `tldr-pages/tldr` 学习如何把入口对象写给外部读者。
- 团队可借 VS Code 学习如何把模板、规则和工程对象转成可观察的公共结构。
- 团队可借 Linux 的反例意识避免把“所有项目都应像 GitHub 首页那样表达自己”当作默认前提。
- 团队可借 OpenClaw 的案例意识重新审视自己项目中的 AI 相关对象是否已经被清楚公开。

## 使用边界

- 不要把案例包讲成“推荐仓库清单”。
- 不要把课堂时间耗在浏览页面截图或平台按钮说明上。
- 不要跳过书稿中的图 5-1、图 5-2 和表 5-1，直接把案例讲成零散见闻。
- 不要在本章案例里提前展开第 6 章的贡献演练。
- 不要把 OpenClaw 讲成“AI 项目等于模型训练仓库”的单一想象。

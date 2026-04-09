# 第 4 章 案例教学包

## 对应章节与用途

- 对应书稿：[04-participating-in-and-organizing-open-source-projects.md](04-participating-in-and-organizing-open-source-projects.md)
- 配套学习指南：[chapter-04-study-guide.md](chapter-04-study-guide.md)
- 配套教学指南：[chapter-04-instructor-guide.md](chapter-04-instructor-guide.md)
- 本案例包用于帮助学生把工程流程理解为变更控制主链，而不是单个平台的按钮教程。

## 主案例与辅助案例

| 案例 | 本章主要说明什么 | 推荐观察对象 |
| --- | --- | --- |
| CPython | GitHub 环境下的 PR、Review、CI 与版本边界 | `Issue`、PR、Checks、版本说明、文档更新 |
| Linux | 说明“流程抽象”比平台界面更重要 | 补丁流、维护者审核、长期主线保护 |
| 教师自选轻量仓库 | 课堂演示最小协作链条 | 一个问题、一条分支、一个 PR、一次检查 |

## 推荐课堂使用方式

- 先用 CPython 讲清 `Issue -> Branch -> PR -> Review -> Checks -> Merge -> Release` 这条链的对象关系。
- 再用 Linux 做反衬，说明即使不依赖 GitHub 页面，变更控制、审核边界和主线保护依然成立。
- 最后用一个轻量仓库演示“最小可运行工作流”，降低初学者的流程畏难感。

## 与书稿贯穿对象的配合

- CPython 对应正文中的主流程对象链，用来承接图 4-1 和表 4-1，帮助学生看到每个对象分别在回答什么问题。
- Linux 对应正文中关于“流程抽象高于平台界面”的讨论，用来说明变更控制并不等于 GitHub 按钮顺序。
- 轻量仓库对应正文中“最小可运行工作流”的要求，用来帮助初学者把主链缩到可以真正执行的规模。
- Chris Wanstrath 与 GitHub 的历史片段对应“为什么平台会让流程显性化”这一支线，但不替代流程主链本身。

## 课堂对象绑定建议

- 图 4-1 固定绑定 CPython：用于讲 `Issue -> Branch -> PR -> Review -> Checks -> Merge -> Release`。
- 表 4-1 固定绑定 CPython 与 Linux 的对照：前者讲 GitHub-native 对象链，后者讲平台无关的流程抽象。
- 轻量仓库只承担“最小演示”作用，不替代 CPython 的完整主链案例。

## 推荐讨论问题

- 为什么开放协作反而更需要保护默认分支。
- 为什么 PR 的价值不仅是“交代码”，更是“交出一个可判断对象”。
- Linux 的流程与 GitHub PR 流程看起来不同，但它们在抽象层上保护的到底是不是同一个问题。
- 为什么 CI、Review 和 Release 不应被拆成互不相关的三件事。

## 与团队项目主线的连接

- 团队项目在这一章之后应能够把自己现有的协作方式映射到一条清楚的变更链，而不是继续依赖口头约定。
- 教师可要求学生用本案例包的语言解释自己项目中的某个 PR：它解决了什么问题、如何被判断、为什么能被合并。

## 使用边界

- 不要把课堂重心耗在平台页面点击演示上。
- 不要让复杂 CI 配置覆盖掉对流程主链的理解。
- 不要把 Linux 当作“与本章无关的老方法”，它在这里承担的是“平台无关的流程对照”。

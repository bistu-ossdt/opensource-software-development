# Chapter 4 Lab / Project Materials

## 对应材料

- 对应书稿：[04-participating-in-and-organizing-open-source-projects.md](04-participating-in-and-organizing-open-source-projects.md)
- 配套学习指南：[chapter-04-study-guide.md](chapter-04-study-guide.md)
- 配套教学指南：[chapter-04-instructor-guide.md](chapter-04-instructor-guide.md)
- 对应实验阶段：实验 4 GitHub 协作流与最小 CI
- 团队项目阶段：变更控制与最小门禁建立

## 本章任务目标

- 把团队项目真正放进“变更控制主链”，而不是继续直接修改主分支。
- 让每一组修改都经过工作项、分支、PR、评审和最低自动化检查。
- 为后续章节的项目阅读、外部贡献和项目迭代建立可信的工程底座。

## 必做基础项

- 围绕至少一个明确的 `Issue` 启动一次开发，禁止直接在默认分支上完成全部修改。
- 所有成员通过 `Branch` 和 `Pull Request` 提交变更，至少完成一轮 review 和修改。
- 在仓库中建立最小自动化检查，可在 build、lint、test 中任选其一，但必须接入日常协作流程。
- 团队写出《最小工作流与评审/发布清单》，建议放入 `docs/workflow-and-release-checklist.md`。
- 在文档中明确工作项记录、分支命名、提交粒度、PR 描述、评审要求和发布前最小检查。

## 选做提升项

- 增加 `CODEOWNERS`、保护分支规则或规则集。
- 增加依赖变化检查、敏感信息检查或更完整的 CI 工作流。
- 增加 `CHANGELOG.md` 或一次可供演示的预发布记录。
- 尝试把版本号、发布说明和演示对象纳入同一轮协作闭环。

## 本章交付物

- 一份《最小工作流与评审/发布清单》，建议仓库路径为 `docs/workflow-and-release-checklist.md`。
- 至少一组 `Issue -> Branch -> PR -> Review` 记录。
- 至少一个最小 CI 工作流文件，如 `.github/workflows/ci.yml`。

## 提交证据

- `docs/workflow-and-release-checklist.md` 链接。
- 至少一个 `Issue` 链接、一个 PR 链接和对应 review 记录。
- CI 运行结果链接或截图。

## 检查点

- 是否真正避免了“先改完再补说明”的做法。
- PR 是否包含足够信息，让修改成为可判断对象，而不只是代码堆叠。
- Review 与 Checks 是否都进入了流程，而不是只保留其一。
- 发布清单是否区分“可以合并”和“准备发布”。

## 常见问题

- 仍然直接推送默认分支，只把 PR 当成展示窗口。
- PR 过大，导致评审只能形式化通过。
- CI 只在演示前临时补一次，没有进入日常协作。
- 把发布理解成“打标签”或“提交压缩包”，没有对外说明边界。

## 与下一章的衔接

- 第 5 章会把本章建立的工作流能力用于阅读和判断陌生仓库的可参与性。
- 本章形成的工作流证据，后续既可以作为团队项目迭代基础，也可以作为阅读外部项目时的对照参照。

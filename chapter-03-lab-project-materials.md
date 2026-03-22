# 第 3 章 实验与项目材料

## 对应材料

- 对应书稿：[03-development-models-and-characteristics.md](03-development-models-and-characteristics.md)
- 配套学习指南：[chapter-03-study-guide.md](chapter-03-study-guide.md)
- 配套教学指南：[chapter-03-instructor-guide.md](chapter-03-instructor-guide.md)
- 对应实验阶段：实验 3 治理基线与协作机制建立
- 团队项目阶段：角色与治理基线建立

## 本章任务目标

- 把“社区”落实为可观察的治理对象和协作入口，而不是抽象口号。
- 让团队项目从“几个人一起写代码”转向“按公开规则协作”。
- 让陌生贡献者在理论上能够知道从哪里进入项目、按什么规则协作。

## 必做基础项

- 选择一个成熟开源仓库，检查其 `CONTRIBUTING.md`、Issue / PR 模板、行为边界或安全入口，并做简要分析。
- 团队明确最小角色分工，至少写清谁负责方向判断、谁负责实现推进、谁负责评审或文档维护。
- 在团队仓库补齐最小协作文件，至少包括 `CONTRIBUTING.md`、Issue 模板和 PR 模板。
- 团队写出《角色分工与贡献入口草案》，建议放入 `docs/contribution-entry-and-roles.md`。
- 在文档中说明外部贡献者如何进入项目，以及最小行为边界或安全报告入口。

## 选做提升项

- 增加 `CODEOWNERS` 或更明确的评审责任边界。
- 增加 `CODE_OF_CONDUCT.md` 或 `GOVERNANCE.md` 的最小版本。
- 对标一个成熟项目的治理文件结构，说明你们当前缺了哪些关键对象。
- 设计团队内部的迭代节奏、会议节奏或决策记录方式。

## 本章交付物

- 一份《角色分工与贡献入口草案》，建议仓库路径为 `docs/contribution-entry-and-roles.md`。
- 仓库中的 `CONTRIBUTING.md`。
- 仓库中的 Issue / PR 模板。

## 提交证据

- `docs/contribution-entry-and-roles.md` 链接。
- `CONTRIBUTING.md` 和模板文件链接。
- 成熟项目治理入口分析记录。

## 检查点

- 是否能让陌生贡献者看清从哪里开始，而不是只让组内成员心里有数。
- 团队角色是否对应责任，而不是只列出头衔。
- 协作文件是否与团队当前项目状态匹配，而不是从别处整段复制。
- 是否至少说明了行为边界或安全问题应通过什么路径报告。

## 常见问题

- 角色分工停留在“组长 / 组员”，没有实际责任区分。
- `CONTRIBUTING.md` 写得过长或过空，既不便读也不便执行。
- 把模板当成装饰文件，实际协作仍完全靠私聊推动。
- 只模仿成熟项目的文件名，却没有把内容缩到适合当前项目的最小规模。

## 与下一章的衔接

- 第 4 章会把本章形成的角色与规则推进为具体工作流和门禁链条。
- 本章建立的贡献入口与角色分工，应在下一章真正落实到 `Issue`、`Branch`、`PR`、`Review`、`CI` 和发布清单中。

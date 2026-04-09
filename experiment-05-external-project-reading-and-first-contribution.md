# 实验 5 外部项目理解与首次贡献

## 对应材料

- 对应书稿：[05-leveraging-open-source-software-resources.md](05-leveraging-open-source-software-resources.md)、[06-participating-in-open-source-projects.md](06-participating-in-open-source-projects.md)
- 对应章节级实验材料：[chapter-05-lab-project-materials.md](chapter-05-lab-project-materials.md)、[chapter-06-lab-project-materials.md](chapter-06-lab-project-materials.md)
- 对应附录支撑：[chapter-05-appendix-support.md](chapter-05-appendix-support.md)、[chapter-06-appendix-support.md](chapter-06-appendix-support.md)
- 对应案例教学包：[chapter-05-case-teaching-pack.md](chapter-05-case-teaching-pack.md)、[chapter-06-case-teaching-pack.md](chapter-06-case-teaching-pack.md)
- 对应实验阶段：实验 5 外部项目理解或首次贡献
- 实验性质：跨第 5-6 章的阶段实验

## 实验目标

- 把“能看懂一个外部项目”推进到“能组织一次稳妥的第一次参与”。
- 让学生理解：项目阅读、行动选择、候选对象判断、贡献说明与 review 回复，本来就是同一条进入链。
- 让团队把外部项目中的进入经验，反向迁移为自己项目的第一次贡献入口设计。

## 阶段结构

- 阶段 A：陌生项目阅读与行动判断，对应 [chapter-05-lab-project-materials.md](chapter-05-lab-project-materials.md)。
- 阶段 B：第一次贡献路径与贡献包组织，对应 [chapter-06-lab-project-materials.md](chapter-06-lab-project-materials.md)。
- 实验完成的标准不是“只做完其中一半”，而是能把 A 阶段的阅读判断自然推进到 B 阶段的第一次参与。

## 使用建议

- 优先选择公共入口较清楚、最近仍有活动记录的真实开源项目，不要一开始就选“很有名但自己完全读不进去”的对象。
- 阶段 A 和阶段 B 最好围绕同一个项目推进，避免把阅读判断和贡献路径拆成两套互不相关的练习。
- 如果真实外部贡献条件暂时不足，可以在 B 阶段提交“基于真实公开对象的完整模拟贡献包”，但不能脱离真实上下文拼接空心样稿。
- 团队项目迁移部分不是附加题，而是本实验的重要收束：外部项目怎么让新人进入，自己的项目也应开始回答这个问题。

## 必做基础项

- 选择 `1` 个外部开源项目，完成第一轮阅读，并形成《陌生项目阅读记录》和《项目阅读摘要》。
- 在“继续学习 / 尝试贡献 / 复用 / 先观察 / 暂缓”中做出一个明确行动选择，并写清理由。
- 如果行动选择指向“尝试贡献”，记录 `1-2` 个候选进入对象；如果不指向“尝试贡献”，写清当前为什么仍不适合进入。
- 围绕其中 `1` 个候选对象，写出《第一次贡献目标分析》，说明边界、时机、验证方式和进入前提。
- 提交一次真实的第一次贡献尝试，或围绕真实公开对象完成一套完整的模拟贡献包，至少覆盖：认领说明、提交信息、PR 描述、验证说明和 review 回复样稿。
- 团队为自己的项目补一份《第一次贡献路径说明》和《第一次贡献候选任务清单》。

## 选做提升项

- 比较两个外部项目的阅读结果，说明为什么其中一个更适合作为第一次进入对象。
- 完成一次真实 PR 并经过至少一轮公开 review 往返。
- 补一份《第一次贡献被拒绝后的处理说明》，把失败场景也纳入方法框架。
- 围绕 Linux、VS Code、tldr 或 OpenClaw 做一次“阅读判断 -> 进入判断”的连续对照。

## 阶段性提交证据

- 阶段 A：外部项目链接、《陌生项目阅读记录》《项目阅读摘要》、行动选择说明、候选进入对象记录。
- 阶段 B：《第一次贡献目标分析》、真实贡献记录或模拟贡献包、团队项目的《第一次贡献路径说明》与《第一次贡献候选任务清单》。
- 若真实公共记录尚未收到维护者回复，可附预备 review 回复样稿，不因“对方还没回”被机械扣分。

## 最终交付物

- 一份《陌生项目阅读记录》，建议命名为 `project-reading-record.md`。
- 一份《项目阅读摘要》，建议命名为 `project-reading-summary.md`。
- 一份候选进入对象记录，可使用 `candidate-entry-objects.md`。
- 一份《第一次贡献目标分析》，建议命名为 `first-contribution-target-analysis.md`。
- 一套真实贡献证据或完整模拟贡献包。
- 一份《第一次贡献路径说明》，建议仓库路径为 `docs/first-contribution-path.md`。
- 一份《第一次贡献候选任务清单》，建议仓库路径为 `docs/first-contribution-tasks.md`。

## 总评分规则（实验 5）

- 默认采用“两段合成”方式：阶段 A 占 `40%`，阶段 B 占 `60%`。
- 阶段 A 的评分以 [chapter-05-lab-project-materials.md](chapter-05-lab-project-materials.md) 的评分尺为基础；阶段 B 的评分以 [chapter-06-lab-project-materials.md](chapter-06-lab-project-materials.md) 的评分尺为基础。
- 如果阶段 A 缺失，阶段 B 的“为什么现在适合进入”就失去前提，因此整项实验通常不判为“完整达标”。
- 如果阶段 A 完成但阶段 B 没有形成真实贡献或模拟贡献包，整项实验通常不高于 `74` 分。
- 如果阶段 B 完成度很高，但阶段 A 的阅读判断明显不成立，也不应评为高分，因为“先读懂项目，再组织贡献”是本实验的核心链条。

## 完整达成判定

- 最低通过：能完成项目阅读、行动选择、候选对象判断和一套完整的第一次贡献包，并提交团队项目的第一次贡献路径说明。
- 优秀完成：不仅能把阅读推进到贡献，还能清楚说明为什么这个对象适合第一次进入、为什么当前不选其他对象，以及这些经验如何反向改进团队项目的外部入口。

## 常见扣分点

- 阶段 A 和阶段 B 分别围绕不同项目，导致阅读判断与贡献路径无法连起来。
- 只凭 `good first issue` 或 `help wanted` 标签就直接认定“适合作为第一次贡献”。
- 阅读记录覆盖很多对象，但最后没有收束成一个项目级判断。
- 贡献包只写“改了什么”，没有写 Why、Verification 和 Not included。
- 团队项目迁移部分仍停留在组内成员视角，没有真正回答外部人第一次进入时先看什么。

## 与后续团队项目的连接

- 本实验结束后，团队项目不应再只是“组内能开发的项目”，而应开始形成“外部人可进入的项目”。
- 第 7 章如果引入 AI 辅助开发，仍应沿用本实验建立的边界判断、说明链和公共记录意识，而不是绕开它们。
- 第 8 章的发布与维护，也应以本实验补出的“第一次贡献入口”和“外部人视角”作为前提。

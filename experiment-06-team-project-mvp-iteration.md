# 实验 6 团队项目 MVP 迭代

## 对应材料

- 对应书稿：[04-participating-in-and-organizing-open-source-projects.md](04-participating-in-and-organizing-open-source-projects.md)、[06-participating-in-open-source-projects.md](06-participating-in-open-source-projects.md)、[08-organizing-and-releasing-your-open-source-project.md](08-organizing-and-releasing-your-open-source-project.md)
- 对应章节级实验材料：[chapter-04-lab-project-materials.md](chapter-04-lab-project-materials.md)、[chapter-06-lab-project-materials.md](chapter-06-lab-project-materials.md)、[chapter-08-lab-project-materials.md](chapter-08-lab-project-materials.md)
- 对应附录支撑：[chapter-04-appendix-support.md](chapter-04-appendix-support.md)、[chapter-06-appendix-support.md](chapter-06-appendix-support.md)、[chapter-08-appendix-support.md](chapter-08-appendix-support.md)
- 对应案例教学包：[chapter-04-case-teaching-pack.md](chapter-04-case-teaching-pack.md)、[chapter-06-case-teaching-pack.md](chapter-06-case-teaching-pack.md)、[chapter-08-case-teaching-pack.md](chapter-08-case-teaching-pack.md)
- 对应实验阶段：实验 6 团队项目 MVP 迭代
- 实验性质：跨第 4、6、8 章的团队项目阶段实验

## 实验目标

- 把团队项目从“已经有一些开发动作”推进到“一次真正可演示、可解释、可继续迭代的 MVP 版本”。
- 让功能、文档、测试、Issue、PR、Review、最小版本记录和外部说明进入同一轮协作闭环。
- 让团队在发布前，先完成一次面向外部读者和潜在贡献者的最小迭代收束。

## 使用建议

- 优先围绕 `1` 条清楚的用户路径收束 MVP，不要把实验 6 做成“继续无边界扩功能”。
- 这一阶段强调“迭代闭环”而不是“功能数量”；如果需要取舍，应优先保证流程、说明、测试和演示链条完整。
- 建议至少把任务拆成 `2-4` 个有关联的工作项，并通过真实 PR 推进，避免所有修改压成单条大 PR。
- 若团队已开始尝试 AI 辅助，也应把 AI 产出继续放在人工审查和工作流之内；真正的 AI 规则化要求留到实验 7 再系统展开。

## 必做基础项

- 团队写出一份《MVP 迭代计划》，建议命名为 `docs/mvp-iteration-plan.md`，至少说明：本轮目标用户路径、MVP 边界、暂不纳入范围的内容、演示目标和版本目标。
- 围绕本轮 MVP 目标拆出 `2-4` 个真实工作项，并在仓库中留下对应 `Issue` 或等价公共记录。
- 至少完成 `2` 条真实 PR，且每条 PR 都要经过最小 review；所有修改禁止直接推送默认分支。
- 在本轮迭代中同时推进以下对象中的至少 `3` 类：功能、文档、测试 / 检查、错误修正、安装 / 使用说明。
- 写出一份《MVP 演示说明》，建议命名为 `docs/mvp-demo-note.md`，至少说明：演示对象、最短操作路径、当前已知限制。
- 给出一份最小版本收束记录，可采用 `CHANGELOG` 草稿、版本候选说明或 release candidate note 的形式。
- 写出一份《MVP 迭代复盘》，建议命名为 `docs/mvp-iteration-retrospective.md`，至少说明：本轮完成了什么、没完成什么、下轮最该优先补什么。

## 选做提升项

- 为本轮 MVP 建立 milestone、project board 或等价阶段跟踪对象。
- 在 PR 中明确区分“本轮纳入”和“本轮不纳入（Not included）”，减少范围膨胀。
- 增加一条面向外部人的安装或快速开始路径，并在演示说明中验证它。
- 形成一次 draft release、pre-release 或课程内版本标签，为实验 8 做准备。
- 补一份《范围外请求处理说明》，训练团队如何对“现在不做什么”给出清楚答复。

## 本实验交付物

- 一份《MVP 迭代计划》，建议仓库路径为 `docs/mvp-iteration-plan.md`。
- 本轮迭代的工作项链接集。
- 至少 `2` 条 PR 与对应 review 记录。
- 一份《MVP 演示说明》，建议仓库路径为 `docs/mvp-demo-note.md`。
- 一份最小版本收束记录，可为 `CHANGELOG` 草稿、版本候选说明或 release candidate note。
- 一份《MVP 迭代复盘》，建议仓库路径为 `docs/mvp-iteration-retrospective.md`。

## 提交证据

- `docs/mvp-iteration-plan.md` 链接。
- 关联 `Issue`、PR、review 与检查结果链接。
- 演示说明与演示截图 / 录屏摘要。
- `CHANGELOG` 草稿、版本候选说明或版本标签链接。
- `docs/mvp-iteration-retrospective.md` 链接。

## 评分尺（实验 6）

总分按 `100` 分计算，固定分为 `5` 个维度，每项 `20` 分。

| 评分维度 | 权重 | 不达标（`0-9`） | 达标（`10-15`） | 优秀（`16-20`） |
| --- | --- | --- | --- | --- |
| MVP 边界清晰度 | `20` | 范围失控，无法说明本轮到底要完成什么 | 能说明本轮目标、用户路径与范围边界 | 边界、演示目标、版本目标和 Not included 都写得清楚 |
| 迭代拆分与协作链 | `20` | 仍靠临时默契推进，没有真实工作项与 PR 链 | 已通过 Issue、PR、review 组织本轮迭代 | 任务拆分合理，PR 边界清楚，协作链前后连贯 |
| 功能 / 文档 / 测试整合质量 | `20` | 只堆功能修改，没有同步更新说明或验证 | 已能把功能、文档和最小检查一起推进 | 用户路径、文档、检查和演示对象之间形成完整闭环 |
| 版本与演示收束 | `20` | 只有开发痕迹，没有版本或演示边界 | 已形成最小版本收束记录和 MVP 演示说明 | 演示目标、版本候选和变更说明清楚一致，可直接支撑下一阶段发布准备 |
| 复盘与下一轮控制 | `20` | 没有复盘，或复盘只写空泛感想 | 已能说明完成项、未完成项和下一轮优先级 | 复盘具体、边界清楚，能有效抑制范围膨胀并指导下一轮迭代 |

## 真实迭代与课程内版本候选的等价判定

- 优先使用团队真实公开仓库中的迭代对象，因为这最能暴露协作链是否真的进入项目。
- 如果当前尚不适合正式 release，可围绕真实仓库提交“版本候选包”或“模拟发布前包”，但必须保留真实 PR、真实文档和真实版本边界。
- 是否已经吸引外部用户使用，不作为本实验直接评分项；重点是团队项目是否已经形成一次公开可解释的 MVP 迭代。
- 只交功能截图而没有工作项、PR、review、说明和版本收束，不应评为高分。

## 总体判分建议

- `90-100`：优秀。MVP 边界清楚，迭代链完整，功能 / 文档 / 检查 / 版本说明协同成立，可直接进入下一阶段发布准备。
- `75-89`：达标偏强。主链成立，主要对象齐全，只有少量范围控制或说明仍显粗糙。
- `60-74`：基本达标。已完成一次最小迭代闭环，但 PR 质量、文档整合或版本收束仍较弱。
- `60` 以下：不达标。仍停留在“开发了一些功能”，无法证明项目完成了一次真正的 MVP 迭代。

## 完整达成判定

- 最低通过：有清楚的 MVP 边界、有真实工作项与 PR、有演示说明、有版本收束记录和复盘。
- 优秀完成：不仅完成本轮迭代，还能让一个陌生人理解“这版能做什么、不能做什么、为什么这一轮先做到这里”。

## 常见扣分点

- 把实验 6 继续做成功能堆积，而没有形成 MVP 边界。
- 所有修改压成一条大 PR，导致 review 失去意义。
- 有功能结果，但没有同步更新文档、检查或演示说明。
- 没有版本候选记录，外部人无法判断这一轮到底交付了什么。
- 复盘只写“下次继续努力”，没有范围控制和优先级判断。

## 与后续章节的连接

- 第 7 章如果引入 AI 辅助开发，应围绕本实验已经形成的 MVP 迭代对象继续组织，而不是另起一套平行开发。
- 第 8 章会把本实验形成的版本候选、演示说明、维护边界和公共界面进一步收束为正式发布准备。

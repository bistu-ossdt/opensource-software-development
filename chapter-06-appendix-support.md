# 第 6 章 附录支撑

## 使用说明

- 本附录服务于第 6 章的第一次贡献路径设计、贡献说明组织与 review 回复训练。
- 目标是降低第一次进入真实项目的组织成本，而不是替代正文中的判断方法。
- 可直接复用模板，但必须先结合目标项目的真实边界做裁剪。

## 三层信号快速判断

- 时间信号：最近一次维护者评论、相关提交或 PR 是否仍在当前节奏内。
- 关联对象信号：Issue 是否已经连到现有 PR、milestone、项目看板或后续讨论。
- 判断语气信号：维护者是在继续收敛方案，还是已经明确表示“暂不处理”“等待更大重构”或“需要先讨论设计”。

## 第一次贡献适配性检查单

- 这个问题是否仍然活跃，最近是否还有维护者回应。
- 是否已经有人认领、已有 PR，或已被并入其他更大范围工作。
- 修改范围是否集中在少量文件或单一对象上。
- 是否存在清楚的验证方法，而不是只能凭主观判断“看起来对了”。
- 项目是否要求先开 Issue、先认领，或先做设计讨论。

## 标签快速提醒

- `good first issue`：说明项目曾把它视为较适合新贡献者进入的对象，但仍需核查当前上下文。
- `help wanted`：说明项目欢迎外部帮助，但不代表维护者已承诺当前版本一定接收这项修改。
- 没有标签，不等于不能参与；关键仍是问题是否清楚、边界是否合适、路径是否公开。

## 模板：认领评论

```text
If this is still a good fit for the current milestone, I'd like to work on it.
My plan is to keep the change limited to the quickstart docs and verify the steps from a clean local setup.
```

## 模板：提交信息

```text
docs: clarify DATA_DIR setup in quickstart

The current quickstart misses the DATA_DIR setup step, which blocks first-time local runs.

Closes #42
```

## 模板：最小 PR 结构

```md
## What
- 

## Why
- 

## Verification
- 

## Not included
- 
```

## 模板：review 回复

```text
Thanks, updated in this PR.
- added the missing platform note
- removed the unrelated formatting change
- reran the docs check after the update
```

## 模板：《第一次贡献目标分析》

建议命名：`first-contribution-target-analysis.md`

```md
# 第一次贡献目标分析

## 候选对象

- 项目名称：
- 问题或对象链接：
- 任务类型（文档 / 测试 / 小修复 / 分诊 / 其他）：

## 当前上下文判断

- 时间信号：
- 关联对象信号：
- 判断语气信号：

## 为什么适合 / 不适合现在进入

- 边界是否清楚：
- 验证方式是否明确：
- 是否需要先讨论设计：

## 计划采用的进入方式

- 是否先认领：
- 是否先开 Issue：
- 预计提交什么最小贡献对象：
```

## 模板：《第一次贡献路径说明》

建议仓库路径：`docs/first-contribution-path.md`

```md
# 第一次贡献路径说明

## 从哪里开始

- 建议先阅读什么：
- 适合先看哪类 Issue / 文档对象：

## 第一次贡献的进入规则

- 是否需要先认领：
- 是否需要先开 Issue：
- 第一次贡献优先考虑哪些对象：

## 提交前最少要说明什么

- 改了什么：
- 为什么改：
- 如何验证：
- 故意没改什么：

## review 后如何继续

- 在哪里回复：
- 是否继续在同一条 PR 中推进：
- 被拒绝后如何处理：
```

## 模板：《第一次贡献候选任务清单》

建议仓库路径：`docs/first-contribution-tasks.md`

```md
# 第一次贡献候选任务清单

| 类别 | 候选任务 | 为什么适合作为第一次贡献 | 进入前还要确认什么 |
| --- | --- | --- | --- |
| 文档 |  |  |  |
| 测试 |  |  |  |
| 小型修复 |  |  |  |
```

## 模板：《第一次贡献被拒绝后的反思提纲》

```md
# 第一次贡献被拒绝后的反思

- 拒绝理由主要落在版本节奏、方案方向，还是范围控制？
- 这个问题是否仍值得继续观察，还是应换一个入口对象？
- 如果重新进入，应先补哪一类上下文？
- 团队项目是否也存在同类“外部人很难判断边界”的问题？
```

## 快速提醒

- 第一次贡献最怕的不是“小”，而是“范围不清”。
- 说明、验证和 review 回复都是贡献对象的一部分。
- 除非维护者明确要求拆分，否则优先在同一条 PR 中继续推进修改。
- 被拒绝并不自动等于失败，关键是能否从公开记录中读懂项目判断。

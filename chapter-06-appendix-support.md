# 第 6 章 附录支撑

## 使用说明

- 本附录服务于第 6 章的第一次贡献路径设计、贡献说明组织与 review 回复训练。
- 目标是降低第一次进入真实项目的组织成本，而不是替代正文中的判断方法。
- 可直接复用模板，但必须先结合目标项目的真实边界做裁剪。
- 建议先独立完成自己的贡献包初稿，再对照后文的完整示例包，不要先照着样例反推答案。

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

## 示例包使用顺序

- 教师课堂校准时，建议按“常见问题样例 -> 达标样例 -> 高质量样例”的顺序展示。
- 学生自查时，建议先完成自己的《第一次贡献目标分析》和最小贡献包，再来对照样例。
- 以下三组样例都围绕同一类轻量文档贡献情境展开：`quickstart` 文档遗漏 `DATA_DIR` 设置步骤。

## 示例包 A：高质量样例

### 1. 《第一次贡献目标分析》样例

```md
# 第一次贡献目标分析

## 候选对象

- 项目名称：Example CLI
- 问题或对象链接：Issue #42 - quickstart 缺少 DATA_DIR 设置步骤
- 任务类型：文档

## 当前上下文判断

- 时间信号：Issue 在 3 天前有维护者回复，最近一周内还有相关文档 PR 被合并。
- 关联对象信号：当前没有关联 PR，也没有被并入更大范围重构；文档目录近期仍有持续维护。
- 判断语气信号：维护者明确表示“这是 first-run blocker，欢迎有人补一版最小修正”。

## 为什么适合现在进入

- 边界清楚：只影响 quickstart 文档的一处启动说明，不需要改动核心实现。
- 验证方式明确：可在干净本地环境中按 quickstart 复现实例，再验证补充说明后能成功运行。
- 不需要先讨论设计：这是信息补足，不涉及接口、架构或行为变更。

## 计划采用的进入方式

- 是否先认领：是
- 是否先开 Issue：否，沿用现有 Issue #42
- 预计提交什么最小贡献对象：补充 quickstart 中的 DATA_DIR 设置步骤，并说明验证过程
```

### 2. 认领评论样例

```text
If this is still a good fit for the current docs milestone, I'd like to take it.
My plan is to keep the change limited to the quickstart section, verify it from a clean local setup, and avoid touching unrelated configuration docs.
```

### 3. commit message 样例

```text
docs: clarify DATA_DIR setup in quickstart

The quickstart currently skips the DATA_DIR setup step, which blocks first-time local runs.

Closes #42
```

### 4. PR 描述样例

```md
## What
- add the missing DATA_DIR setup step to the quickstart guide
- add one short note about where the sample data directory should point

## Why
- the current quickstart can fail on a clean local setup because DATA_DIR is not configured
- this issue is a first-run blocker for new contributors trying to verify the project locally

## Verification
- followed the quickstart from a clean local setup
- confirmed the documented path works with the sample dataset
- reran the docs check after the wording update

## Not included
- no refactor of the broader configuration guide
- no changes to runtime code or deployment scripts
```

### 5. review 回复样例

```text
Thanks, updated in this PR.
- moved the platform-specific note below the shared step
- kept the change limited to quickstart.md
- reran the docs check after the wording update
```

### 6. 团队项目《第一次贡献路径说明》片段

```md
## 从哪里开始

- 建议先阅读 `README.md`、`CONTRIBUTING.md` 和 `docs/setup.md`
- 第一次贡献优先从文档、测试和小型修复进入

## 第一次贡献的进入规则

- 若已有对应 Issue，先在 Issue 下说明计划
- 若没有现成 Issue，先补一个最小问题说明，再开始修改
- 第一次贡献默认不改核心架构，不跨多个主题混合提交

## 提交前最少要说明什么

- 改了什么
- 为什么要改
- 如何验证
- 故意没改什么
```

### 7. 团队项目《第一次贡献候选任务清单》片段

```md
| 类别 | 候选任务 | 为什么适合作为第一次贡献 | 进入前还要确认什么 |
| --- | --- | --- | --- |
| 文档 | 补 setup.md 中的环境变量说明 | 范围小，可直接验证 | 是否已有同类 PR |
| 测试 | 为 CLI 参数错误补一条失败测试 | 验证路径清楚 | 当前测试命令是否稳定 |
| 小型修复 | 修正 README 中失效命令示例 | 外部读者容易复现 | 是否影响其他平台说明 |
```

### 教师点评

- 这个样例的强项不只是“对象齐”，而是每个对象都围绕同一个边界展开，没有额外带入无关修改。
- 它明确写出了 `Verification` 和 `Not included`，因此 reviewer 能快速判断范围是否合适。
- 团队项目迁移部分也站在外部贡献者视角，而不是站在组内成员视角。

## 示例包 B：达标样例

### 1. 《第一次贡献目标分析》样例

```md
# 第一次贡献目标分析

## 候选对象

- 项目名称：Example CLI
- 问题或对象链接：Issue #42
- 任务类型：文档

## 当前上下文判断

- 最近还有维护者活动
- 当前没有看到其他人正在处理这个问题
- 这个问题集中在 quickstart 文档

## 为什么适合 / 不适合现在进入

- 适合现在进入，因为是单点文档问题
- 验证方式比较清楚，可以按 quickstart 复现

## 计划采用的进入方式

- 先认领
- 直接补 quickstart 中缺少的说明
```

### 2. 认领评论样例

```text
I'd like to work on this if it's still open.
I plan to update the quickstart docs and test the steps locally.
```

### 3. commit message 样例

```text
docs: add missing DATA_DIR note to quickstart
```

### 4. PR 描述样例

```md
## What
- add the missing DATA_DIR step

## Why
- new contributors may fail on first local run

## Verification
- checked the quickstart locally

## Not included
- broader docs cleanup
```

### 5. review 回复样例

```text
Updated in this PR and checked the docs flow again.
```

### 6. 团队项目《第一次贡献路径说明》片段

```md
## 第一次贡献的进入规则

- 建议先看 README 和 CONTRIBUTING
- 有现成 Issue 时先在 Issue 下留言
- 第一次贡献优先从文档或小修复开始
```

### 7. 团队项目《第一次贡献候选任务清单》片段

```md
| 类别 | 候选任务 | 为什么适合作为第一次贡献 | 进入前还要确认什么 |
| --- | --- | --- | --- |
| 文档 | 补安装说明 | 范围小 | 是否已有计划中的文档重写 |
| 测试 | 补一条参数校验测试 | 修改面较小 | 测试命令是否已跑通 |
| 小型修复 | 修正 README 示例 | 容易复现 | 是否影响多平台说明 |
```

### 教师点评

- 这个样例已经达到“可通过”的水平：对象基本齐全，方向也对。
- 主要弱点在于上下文判断较薄，`Verification` 太短，团队项目入口设计仍有点概括化。
- 如果学生提交类似质量，通常可以判为“达标”，但很难进入高分段。

## 示例包 C：常见问题样例

### 1. 《第一次贡献目标分析》样例

```md
# 第一次贡献目标分析

## 候选对象

- 项目名称：Example CLI
- 问题或对象链接：Issue #42
- 任务类型：文档

## 当前上下文判断

- 这是 good first issue，应该比较容易

## 为什么适合 / 不适合现在进入

- 我觉得这个问题很简单，所以适合我来做

## 计划采用的进入方式

- 直接开始改
```

### 2. 认领评论样例

```text
I will fix this soon.
```

### 3. commit message 样例

```text
update docs
```

### 4. PR 描述样例

```md
## What
- fixed docs
```

### 5. review 回复样例

```text
Done.
```

### 6. 团队项目《第一次贡献路径说明》片段

```md
## 第一次贡献的进入规则

- 新人可以先随便找个问题改
- 如果不会再来群里问
```

### 7. 团队项目《第一次贡献候选任务清单》片段

```md
| 类别 | 候选任务 | 为什么适合作为第一次贡献 | 进入前还要确认什么 |
| --- | --- | --- | --- |
| 文档 | 完善文档 | 文档比较简单 | 无 |
| 测试 | 补测试 | 测试重要 | 无 |
| 修复 | 修 bug | bug 很有价值 | 无 |
```

### 教师点评

- 这个样例最典型的问题是：只凭标签和主观感觉判断，没有核查上下文、版本窗口和边界。
- 认领评论、commit message、PR 描述和 review 回复都过于空泛，无法形成真正可判断的公共对象。
- 团队项目入口设计完全站在内部人视角，外部贡献者并不知道先看什么、如何进入。
- 这类提交通常只能落在“不达标”或“接近不达标”的区间。

## 快速提醒

- 第一次贡献最怕的不是“小”，而是“范围不清”。
- 说明、验证和 review 回复都是贡献对象的一部分。
- 除非维护者明确要求拆分，否则优先在同一条 PR 中继续推进修改。
- 不要先看高质量样例再反推自己的答案，样例更适合在完成初稿后用于校准。
- 被拒绝并不自动等于失败，关键是能否从公开记录中读懂项目判断。

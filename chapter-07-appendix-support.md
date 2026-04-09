# 第 7 章 附录支撑

## 使用说明

- 本附录服务于第 7 章的 AI 辅助任务组织、人工验收、规则文件落地与课堂评分校准。
- 目标是降低“把 AI 结果重新纳入开源流程”的组织成本，而不是替代正文中的判断方法。
- 可直接复用模板，但必须先结合目标项目的真实边界裁剪，不要把样例原样替换项目名后直接提交。
- 建议先独立完成自己的《AI 任务说明》和《AI 使用记录》初稿，再对照后文示例包，不要先照着样例反推答案。

## 三个先问清的问题

- 这次到底要解决什么问题，为什么值得现在做。
- 允许 AI 读取或修改哪些对象，哪些对象不能碰。
- 什么证据能说明这项修改已经准备好进入 Pull Request，而不是只停留在候选结果。

## AI 辅助任务边界检查单

- 任务是否已经被收窄到少量文件、单一对象或单一问题，而不是“顺手全面优化”。
- 是否优先选择文档、测试、小修复、配置澄清或说明补齐，而不是一开始就碰大功能、架构重构或高风险安全修改。
- 是否明确写出禁止变更项，例如依赖、发布文件、安全设置、无关格式化或额外重构。
- 是否写清需要人工批准的节点，例如联网检索、安装新依赖、修改发布对象或触碰敏感目录。
- 是否能用一句话说明“为什么项目应该接受这项修改”，而不是只说“AI 已经生成出来了”。

## 人工验收五项检查单

- 问题陈述是否清楚：修改到底在解决什么问题。
- 差异范围是否收敛：是否混入了不相关的格式化、重构或顺手优化。
- 验证证据是否存在：测试、文档检查、复现步骤或运行结果是否真的执行过。
- 来源与制度边界是否清楚：第三方片段、依赖、许可证、数据或说明文字是否需要额外核查。
- 最终说明是否由人负责：提交者能否自己解释 `What / Why / Verification / Not included / AI involvement`。

## AI 项目对象三步快速判断

- 第一步：它到底公开了什么。先区分代码（`Code`）、参数（`Parameters`）、数据信息（`Data Information`）、评测对象与部署对象，而不是笼统写成“开源模型”。
- 第二步：这些对象是否允许外部人继续理解、修改、再分发或重建实质等效系统，而不是只有下载入口。
- 第三步：缺失的部分是否会实质性阻断理解、复现和继续参与。如果会，就更稳妥地写成“开放权重”或“一般开放发布对象”，而不是直接写成“开源人工智能”。

## 好任务与坏任务的最小对照

```text
不够好的任务描述
- 帮我把这个仓库里所有和 quickstart 有关的问题都顺手修掉，并尽量一起现代化。

更稳妥的任务描述
- 只检查 docs/quickstart.md、scripts/setup.sh 和 tests/test_quickstart.py。
- 判断 quickstart 是否遗漏 DATA_DIR 设置步骤。
- 如果遗漏，只起草最小文档补丁和必要测试补充。
- 不修改依赖、不改发布文件、不处理无关格式化。
- 列出需要人工确认的地方，再等待批准。
```

## 模板：《AI 任务说明》

建议命名：`ai-task-brief.md`

```md
# AI 任务说明

## 问题

- 当前问题是什么：
- 为什么值得现在处理：

## 允许处理的对象

- 允许读取的文件 / 对象：
- 允许修改的文件 / 对象：

## 禁区

- 明确不修改的对象：
- 需要人工批准后才能进行的动作：

## 完成条件

- 什么结果算完成：
- 需要运行哪些验证：

## 交付说明

- 需要形成哪些公共对象：
- 需要提交者亲自解释什么：
```

## 模板：《AI 使用记录》

建议命名：`ai-usage-record.md`

```md
# AI 使用记录

## 任务背景

- 对应问题：
- 对应对象：

## AI 介入位置

- 用 AI 做了什么：
- 没让 AI 做什么：

## 使用的任务描述或规则

- 任务描述摘要：
- 参考的规则文件：

## 候选结果

- AI 生成了哪些候选内容：
- 哪些内容被保留：
- 哪些内容被删掉或重写：

## 人工判断

- 为什么接受当前结果：
- 还需要维护者重点核查什么：
```

## 模板：《人工验收说明》

建议命名：`human-acceptance-note.md`

```md
# 人工验收说明

## What

- 

## Why

- 

## Verification

- 

## Not included

- 

## AI involvement

- AI 介入了什么：
- 人工重写 / 删改了什么：
- 哪些判断由提交者最终负责：
```

## 模板：最小 `AGENTS.md`

```text
# AGENTS.md

- Only modify files explicitly named in the task.
- Keep AI-generated changes focused; do not bundle unrelated formatting-only edits.
- Run the required docs build or tests before proposing changes.
- Ask for human approval before changing dependencies, release files, security settings, or network-related configuration.
- In the final note, explain What / Why / Verification / Not included / AI involvement.
```

## 模板：《AI 适用任务与禁区清单》

建议仓库路径：`docs/ai-task-boundaries.md`

```md
# AI 适用任务与禁区清单

| 类别 | 适合先用 AI 辅助的任务 | 当前禁区或高风险对象 | 进入前还要确认什么 |
| --- | --- | --- | --- |
| 文档 | 术语澄清、quickstart 补充、配置说明修正 | 发布承诺、法律声明、对外政策 | 文档是否与真实行为一致 |
| 测试 | 补边界测试、整理样例、把复现步骤转成自动化检查 | 大规模测试重构、含不稳定外部依赖的测试 | 测试框架与断言语义是否稳定 |
| 小修复 | 明确可复现的小缺陷、路径问题、配置缺口 | 跨模块设计调整、接口改写 | 范围是否能收敛在少量对象 |
| AI 项目对象判断 | README、模型卡、来源说明、评测说明梳理 | 直接宣称已满足开源人工智能定义 | 代码 / 参数 / 数据信息是否同时成立 |
```

## 模板：AI 参与 PR 的最小说明结构

```md
## What
- 

## Why
- 

## Verification
- 

## Not included
- 

## AI involvement
- AI was used to summarize context / draft candidate text / propose a test skeleton.
- Final wording, scope control, and acceptance decisions were reviewed and finalized by the contributor.
```

## 模板：《权限与批准记录》

建议命名：`ai-approval-log.md`

```md
# 权限与批准记录

| 时间 | 动作 | 为什么需要批准 | 是否批准 | 备注 |
| --- | --- | --- | --- | --- |
|  | 联网检索 |  |  |  |
|  | 安装依赖 |  |  |  |
|  | 修改发布对象 |  |  |  |
|  | 触碰安全相关配置 |  |  |  |
```

## 示例包使用顺序

- 教师课堂校准时，建议按“常见问题样例 -> 达标样例 -> 高质量样例”的顺序展示。
- 学生自查时，建议先完成自己的《AI 任务说明》《AI 使用记录》和《人工验收说明》，再来对照样例。
- 以下三组样例都围绕同一类轻量文档修复情境展开：`quickstart` 文档遗漏 `DATA_DIR` 设置步骤。

## 示例包 A：高质量样例

### 1. 《AI 任务说明》样例

```md
# AI 任务说明

## 问题

- quickstart 当前遗漏了 `DATA_DIR` 设置步骤，导致第一次本地运行很容易失败。
- 这是 first-run blocker，适合在当前文档窗口内做最小修正。

## 允许处理的对象

- 允许读取：`docs/quickstart.md`、`scripts/setup.sh`、`tests/test_quickstart.py`
- 允许修改：`docs/quickstart.md`，必要时补 `tests/test_quickstart.py`

## 禁区

- 不修改依赖、发布文件和部署脚本
- 不顺手重写整份配置文档
- 若需要新增环境变量处理逻辑，先暂停并请求人工确认

## 完成条件

- quickstart 中补上 `DATA_DIR` 说明
- 验证本地复现步骤成立
- 若已有相关测试，补充或更新最小检查

## 交付说明

- 形成最小差异、人工验收说明和 AI 使用记录
- 最终 PR 说明必须由提交者自己解释清楚
```

### 2. 《AI 使用记录》样例

```md
# AI 使用记录

## 任务背景

- 对应问题：quickstart 缺少 `DATA_DIR` 设置步骤
- 对应对象：`docs/quickstart.md`

## AI 介入位置

- 用 AI 比对 `docs/quickstart.md` 与 `scripts/setup.sh`，整理变量遗漏点
- 用 AI 起草一版最小文档补丁和一条候选测试思路
- 没让 AI 修改依赖、发布文件或无关目录

## 使用的任务描述或规则

- 任务描述要求只关注 `docs/quickstart.md`、`scripts/setup.sh` 和 `tests/test_quickstart.py`
- 参考规则：仅允许最小差异；不得附带格式化；依赖和发布相关修改需要人工批准

## 候选结果

- AI 最初给出了一段 quickstart 补丁，并顺手加入了“优化 broader configuration guide”的建议
- 保留：`DATA_DIR` 的最小补充说明和一个测试思路
- 删除：所有与 broader configuration guide 有关的扩展建议
- 重写：把“configuration loader”这类实现细节改成更贴近读者场景的表述

## 人工判断

- 接受当前结果，因为问题边界清楚、修改范围收敛、验证路径明确
- 仍需维护者重点核查：平台差异说明是否足够、文案是否与当前版本保持一致
```

### 3. 《人工验收说明》样例

```md
# 人工验收说明

## What

- 在 quickstart 中补充 `DATA_DIR` 的设置步骤
- 补一句数据目录应指向 sample data 的说明

## Why

- 当前 quickstart 会让第一次本地运行在加载第一个示例前失败
- 这是新贡献者最容易踩中的 first-run blocker

## Verification

- 按 quickstart 在干净本地环境中重新执行一次
- 确认设置 `DATA_DIR` 后可以加载 sample data
- 重新运行文档检查

## Not included

- 不重写 broader configuration guide
- 不改运行时代码和部署脚本

## AI involvement

- AI 用于比对文档与脚本、起草候选文案和候选测试思路
- 最终文案、范围收紧和验收判断由提交者人工完成
- 所有验证命令由提交者亲自执行
```

### 4. 最小 `AGENTS.md` 片段样例

```text
- Only edit docs/quickstart.md unless the task explicitly allows a test update.
- Do not modify dependencies, release notes, or deployment files without approval.
- Keep the patch focused on the DATA_DIR quickstart gap.
- Run docs checks before proposing the final patch.
- In the final note, explain What / Why / Verification / Not included / AI involvement.
```

### 5. AI 参与 PR 描述样例

```md
## What
- add the missing `DATA_DIR` setup step to quickstart

## Why
- first-time local runs can fail before the sample data is loaded

## Verification
- reran the quickstart from a clean local setup
- reran the docs check

## Not included
- no broader config-guide rewrite
- no runtime code changes

## AI involvement
- AI was used to summarize the gap between the quickstart and setup script and to draft candidate wording
- the final wording, scope control, and verification were completed by the contributor
```

### 教师点评

- 这个样例的强项不是“写得像官方文档”，而是对象、范围、验证和责任链收得很紧。
- 它把 AI 介入位置说清了，但没有把 AI 写成责任主体。
- 规则文件、任务说明、使用记录和验收说明之间能互相对应，因此教师可以直接据此评分。

## 示例包 B：达标样例

### 1. 《AI 任务说明》样例

```md
# AI 任务说明

- 问题：quickstart 里缺少 `DATA_DIR` 设置步骤
- 允许修改：`docs/quickstart.md`
- 完成条件：补上说明，并做一次本地验证
- 不处理无关文档优化
```

### 2. 《AI 使用记录》样例

```md
# AI 使用记录

- 用 AI 总结了 quickstart 和 setup 脚本的差异
- 用 AI 起草了一版文档说明
- 人工删掉了一句不必要的实现细节描述
- 最终自己重新执行了 quickstart
```

### 3. 《人工验收说明》样例

```md
## What
- 补 quickstart 中的 `DATA_DIR` 说明

## Why
- 没有这个步骤时本地运行会失败

## Verification
- 本地重跑 quickstart

## Not included
- 不改其他文档

## AI involvement
- AI 起草了候选文案，最终文本和验证由我完成
```

### 教师点评

- 这是基本达标的样例，能看出对象、验证和人工责任链。
- 但它仍偏简略，缺少更清楚的批准点、禁区和维护者需重点核查事项。

## 示例包 C：常见问题样例

### 1. 《AI 任务说明》样例

```md
# AI 任务说明

- 帮我把 quickstart 和相关配置全部优化一下，尽量一起修掉能看到的问题。
```

### 2. 《AI 使用记录》样例

```md
# AI 使用记录

- 用 AI 改好了文档
- 看起来没问题
```

### 3. 《人工验收说明》样例

```md
## What
- updated docs

## Why
- improve usability

## Verification
- not run yet
```

### 教师点评

- 这个样例的问题不在于“用了 AI”，而在于对象、范围、验证和责任几乎全部缺失。
- 任务描述过宽，AI 使用记录不可追溯，人工验收说明没有形成项目可接受的公共对象。
- 这类内容即使看起来很快，也不应评为达标。

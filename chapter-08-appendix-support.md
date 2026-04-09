# 第 8 章 附录支撑

## 使用说明

- 本附录服务于第 8 章的项目发布准备、维护计划落地、版本承诺表达与最小安全基线建立。
- 目标是降低“把项目组织成可公开参与对象”的实施成本，而不是替代书稿中的判断方法。
- 建议先独立完成一版《项目发布与维护基线说明》初稿，再使用下列检查单和模板做收束，不要一开始就直接套模板。
- 所有模板都应以项目真实状态为准，不要为了显得“完整”而写出仓库并不满足的承诺。

## 四个先问清的问题

- 如果一个陌生人第一次进入仓库，他最先需要知道什么。
- 当前哪些内容已经稳定到可以对外承诺，哪些仍是实验状态。
- 项目接下来由谁维护，多久响应一次，以及哪些版本仍被支持。
- 出现安全问题、范围外需求或已知限制时，项目准备怎样对外说明。

## 公共界面快速检查单

- README 是否说明了项目定位、当前状态、最短上手路径和后续入口。
- LICENSE 是否明确存在，且与项目真实制度边界一致。
- 是否已经给出贡献入口，例如 `CONTRIBUTING.md`、Issue 模板、支持路径或最小沟通说明。
- 版本、`CHANGELOG` 和 release note 是否能共同说明当前边界与变化内容。
- 是否存在最小维护说明和最小安全说明。
- 这些对象是否彼此一致，而不是分别写成孤立文件。

## 发布前最小检查单

- 版本号是否已经确定，并能解释这次为什么是这一版。
- `CHANGELOG` 是否记录了本次最值得外部人知道的变化。
- release note 是否清楚说明了 Changed / Fixed / Compatibility note。
- README 中的安装、运行、状态与版本说明是否仍然真实。
- 维护计划是否说明了谁维护、哪些版本支持、多久查看问题。
- `SECURITY.md` 或等价说明是否给出了漏洞报告路径和支持版本。
- 是否明确写出当前已知限制，而不是让外部人自己踩坑后再发现。

## 维护者范围控制检查单

- 是否已经写清哪些请求当前不在范围内。
- 是否能用一句话说明“为什么这次发布不包含某项需求”。
- 是否区分了“暂不接受”与“永远不考虑”。
- 是否把范围控制写进维护计划、Issue 回复或贡献入口，而不是只在口头沟通中存在。

## 模板：《项目发布与维护基线说明》

建议命名：`project-release-and-maintenance-baseline.md`

```md
# 项目发布与维护基线说明

## 项目定位

- 项目解决什么问题：
- 当前主要面向谁：

## 当前状态

- 当前版本：
- 当前属于稳定 / 预发布 / 实验阶段：
- 已知限制：

## 最短上手路径

- 安装 / 运行步骤：
- 最小验证方法：

## 参与入口

- 提问 / 报告问题去哪里：
- 第一次参与前先看什么：

## 版本与发布

- 本次版本边界：
- 对应 `CHANGELOG` / release note：

## 维护计划

- 谁负责维护：
- 问题多久查看一次：
- 哪些版本仍受支持：

## 安全说明

- 漏洞报告路径：
- 不应公开提交的问题类型：
```

## 模板：最小 README 结构

````md
# Example Project

一句话说明项目在解决什么问题。

当前状态：`v1.0.0`，当前发布线可用；实验性能力见后续说明。

## Quick Start

```bash
make setup
make run
```

## Project Status

- 当前支持版本：
- 已知限制：

## Contributing

第一次参与前请阅读 `CONTRIBUTING.md`。

## Security

发现漏洞请先阅读 `SECURITY.md`。

## License

MIT
````

## 模板：最小维护计划

```text
## Maintenance

- actively maintained by @author and @co-maintainer
- issues are triaged roughly once a week
- bug-fix PRs are reviewed within about 7 days
- v1.x is the supported release line; v0.x is no longer maintained
- feature requests outside the current roadmap should start in Discussion first
```

## 模板：最小 `SECURITY.md`

```md
# Security Policy

## Supported Versions
- `1.x`: supported
- `0.x`: no longer supported

## Reporting a Vulnerability
Please report security issues privately to `security@example.org`.
Do not open public issues for unpatched vulnerabilities.
```

## 模板：最小 `CHANGELOG` 条目

```md
## [1.0.0] - 2026-04-09

### Added
- first public release with quickstart, contribution entry and baseline maintenance policy

### Changed
- clarify project status and supported release line in README

### Security
- add a minimal security reporting path
```

## 模板：最小 release note

```text
## 1.0.0

### Added
- first public release package

### Changed
- clarify setup steps and contribution path

### Compatibility note
- future minor releases may extend features without breaking the current quickstart path
```

## 模板：范围外请求回应

```text
感谢你的建议。这个需求有价值，但不在当前 `v1.x` 维护范围内。
当前版本优先处理缺陷修复、文档缺口与发布稳定性。
如果后续继续讨论，请先在 Discussion 中说明使用场景，或以实验性扩展单独推进。
```

## 模板：《发布前检查记录》

建议命名：`release-readiness-check.md`

```md
# 发布前检查记录

| 项目 | 当前状态 | 备注 |
| --- | --- | --- |
| README 已更新 |  |  |
| LICENSE 已确认 |  |  |
| 贡献入口已存在 |  |  |
| 版本号已确定 |  |  |
| `CHANGELOG` 已更新 |  |  |
| release note 已准备 |  |  |
| 维护计划已写明 |  |  |
| `SECURITY.md` 已写明 |  |  |
| 已知限制已说明 |  |  |
| 仍需人工确认事项 |  |  |
```

## 好发布与坏发布的最小对照

```text
不够好的发布说明
- 发布了很多修复和优化，欢迎大家使用。

更稳妥的发布说明
- 这是项目的第一次公开发布。
- 已补齐 README、贡献入口和最小安全说明。
- 当前支持 v1.x，仍有若干已知限制，详见 README 和 release note。
```

## 示例包使用顺序

- 教师课堂校准时，建议先展示“文件存在但仍难以进入”的反例，再展示“对象虽少但回答关键问题”的达标样例。
- 学生自查时，建议先按检查单完成自己的版本，再回头对照模板。
- 以下三组样例都围绕同一类小型团队项目展开：一个已经有基本功能、正在准备第一次公开发布的协作项目。

## 示例包 A：高质量样例要点

- README 已清楚说明项目定位、当前状态与最短上手路径。
- `CHANGELOG`、release note 与版本号彼此一致。
- 维护计划和 `SECURITY.md` 虽短，但真实回答了支持版本与联系路径。
- 发布前检查记录中能看出哪些地方已经完成，哪些仍是已知限制。

## 示例包 B：达标样例要点

- 文件已补齐，基本问题也能回答。
- 但 README 仍偏内部视角，维护计划和 release note 还不够收束。
- 适合作为“已经能公开，但还不够稳妥”的中间状态。

## 示例包 C：常见问题样例

- 只有版本号，没有边界解释。
- 有 README，但没有当前状态与参与入口。
- 有安全说明，但没有支持版本。
- 文件名齐全，却仍然看不出项目是否真实准备好进入公共世界。

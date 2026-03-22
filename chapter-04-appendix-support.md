# Chapter 4 Appendix Support

## 使用说明

- 本附录服务于第 4 章的工作流、评审、CI 和发布任务。
- 目标是给出“最小可运行链条”，而不是把课堂变成平台按钮教程。
- 可按项目规模选择最小版本，只要真正进入日常协作流程即可。

## 最小工作流链条检查单

- 是否所有开发都从 `Issue` 或等价工作项开始。
- 是否为每组修改建立独立分支。
- 是否通过 PR 形成公共说明对象，而不是只提交代码。
- 是否至少完成一轮人工 review。
- 是否在合并前运行最小自动化检查。
- 是否把“合并”与“发布”区分开来。

## 建议的命名与说明约定

```text
Branch:
feature/short-description
fix/short-description
docs/short-description

Commit:
docs: refine project public value note
feat: add initial license inventory doc
ci: add minimal test workflow

Pull Request title:
docs: add contribution entry draft
feat: implement login page MVP
fix: handle missing config error
```

## PR 最小检查清单

- 这组修改在解决哪个 `Issue` 或问题。
- 修改范围是否足够小，便于 review。
- PR 描述是否说明了做了什么、没做什么、还有什么待补。
- 是否附上了必要的测试、检查或人工验证说明。
- 是否明确指出了对文档、版本或发布的影响。

## 模板：《最小工作流与评审/发布清单》

建议仓库路径：`docs/workflow-and-release-checklist.md`

```md
# 最小工作流与评审/发布清单

## 日常协作链条

- 工作项从哪里记录：
- 分支如何命名：
- 提交粒度如何控制：
- PR 至少需要说明什么：
- Review 至少检查什么：

## 最小自动化检查

- 当前采用 build / lint / test 中的哪一项：
- 在什么时机运行：
- 未通过时如何处理：

## 发布前补齐对象

- 版本号或版本说明：
- 发布说明：
- 文档更新：
- 演示对象或验收对象：
```

## 最小 CI 起步建议

- 对命令行工具或库项目，优先选择 build 或 test 作为第一条检查。
- 对前端或文档型项目，优先选择 lint、构建检查或链接检查中的一种。
- 第一条 CI 应尽量稳定、易理解、能长期保留，而不是堆很多临时检查。

## 快速提醒

- 不要把 PR 当作“上传代码窗口”，它首先是公共判断对象。
- 不要让 CI 只在演示前临时运行一次。
- 不要把发布压缩成“打 tag”，要同时准备版本边界和对外说明。

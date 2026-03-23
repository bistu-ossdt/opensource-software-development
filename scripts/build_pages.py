#!/usr/bin/env python3

from __future__ import annotations

from dataclasses import dataclass
from datetime import datetime, timezone
from pathlib import Path
import html
import re
import shutil

import markdown


ROOT = Path(__file__).resolve().parents[1]
SITE_DIR = ROOT / "site"
ASSETS_DIR = SITE_DIR / "assets"
PUBLIC_ASSETS_DIR = ROOT / "assets"


@dataclass(frozen=True)
class ManuscriptPage:
    label: str
    source: Path
    output: str
    description: str


@dataclass(frozen=True)
class TeachingPage:
    label: str
    source: Path
    output: str
    description: str
    chapter_output: str
    chapter_label: str
    kind: str


@dataclass(frozen=True)
class Section:
    key: str
    label: str
    output: str
    description: str


@dataclass(frozen=True)
class LabStage:
    label: str
    href: str | None
    chapters: str
    milestone: str
    baseline: str
    evidence: str
    evaluation: str
    availability: str


SECTIONS = [
    Section("home", "首页", "index.html", "课程入口、核心分区和最近可读内容。"),
    Section("course", "课程说明", "course.html", "课程定位、材料体系、当前公开进度与使用路径。"),
    Section("manuscript", "书稿", "manuscript.html", "各章正文、附录与书后工具材料的阅读入口。"),
    Section("teaching", "教学支持", "teaching-support.html", "学习指南、教学指南与书稿配套入口。"),
    Section("labs", "实验与项目", "labs-project.html", "实践主线、实验阶段与团队项目。"),
    Section("cases", "案例与参考", "cases-references.html", "经典/现代案例、案例教学包、专题附录与核心参考。"),
]

MANUSCRIPT_PAGES = [
    ManuscriptPage(
        label="第 1 章 开源的起源与发展",
        source=ROOT / "01-overview.md",
        output="chapter-01.html",
        description="历史脉络、关键人物、关键节点与开源生态形成。",
    ),
    ManuscriptPage(
        label="第 2 章 自由软件、开源软件与许可证",
        source=ROOT / "02-development-of-open-source-software.md",
        output="chapter-02.html",
        description="自由软件、开源软件、许可证与制度基础。",
    ),
    ManuscriptPage(
        label="第 3 章 开源社区与治理",
        source=ROOT / "03-development-models-and-characteristics.md",
        output="chapter-03.html",
        description="社区结构、角色分工、治理文件与社区健康。",
    ),
    ManuscriptPage(
        label="第 4 章 开源开发的基本工程流程",
        source=ROOT / "04-participating-in-and-organizing-open-source-projects.md",
        output="chapter-04.html",
        description="变更控制、PR、Review、CI、安全与发布基线。",
    ),
    ManuscriptPage(
        label="第 5 章 阅读与理解开源项目",
        source=ROOT / "05-leveraging-open-source-software-resources.md",
        output="chapter-05.html",
        description="从仓库入口、治理信号与工程对象出发，建立面对陌生开源项目的整体阅读框架。当前为骨架稿。",
    ),
    ManuscriptPage(
        label="第 6 章 参与开源项目",
        source=ROOT / "06-participating-in-open-source-projects.md",
        output="chapter-06.html",
        description="从第一次贡献、贡献说明到 review 回复，建立参与真实项目的最小路径。当前为骨架稿。",
    ),
    ManuscriptPage(
        label="第 7 章 AI 辅助的开源开发实践",
        source=ROOT / "07-ai-assisted-open-source-development-practice.md",
        output="chapter-07.html",
        description="讨论 AI 如何进入开源流程，而不是绕开许可证、评审、测试与人工责任链。当前为骨架稿。",
    ),
    ManuscriptPage(
        label="第 8 章 组织与发布你的开源项目",
        source=ROOT / "08-organizing-and-releasing-your-open-source-project.md",
        output="chapter-08.html",
        description="从维护者视角组织公开仓库、版本发布、维护计划与最小安全基线。当前为骨架稿。",
    ),
    ManuscriptPage(
        label="附录 开源历史关键事件时间线",
        source=ROOT / "appendix-open-source-history-timeline.md",
        output="appendix-open-source-history-timeline.html",
        description="按时间顺序压缩开源历史主线，帮助快速定位关键转折。",
    ),
    ManuscriptPage(
        label="附录 开源人物谱",
        source=ROOT / "appendix-open-source-people.md",
        output="appendix-open-source-people.html",
        description="从人物角度理解开源如何被提出、推动、组织和书写。",
    ),
    ManuscriptPage(
        label="附录 开源人物-事件-项目对照表",
        source=ROOT / "appendix-open-source-people-event-project-map.md",
        output="appendix-open-source-map.html",
        description="用一张导航表把关键人物、关键事件与代表项目放在一起理解。",
    ),
    ManuscriptPage(
        label="附录 开源人工智能",
        source=ROOT / "appendix-open-source-ai.md",
        output="appendix-open-source-ai.html",
        description="用代表事件、人物、组织与对象建立开源人工智能的整体图景，并保持与 OSI 定义边界对齐。",
    ),
    ManuscriptPage(
        label="全书术语表",
        source=ROOT / "98-glossary.md",
        output="glossary.html",
        description="整本书统一使用的核心术语、英文原词与简要定义。",
    ),
    ManuscriptPage(
        label="全书参考文献",
        source=ROOT / "99-book-references.md",
        output="book-references.html",
        description="整本书统一使用的核心参考资料与官方来源入口。",
    ),
]


def chapter_manuscript_pages() -> list[ManuscriptPage]:
    return [page for page in MANUSCRIPT_PAGES if page.label.startswith("第 ")]


def appendix_manuscript_pages() -> list[ManuscriptPage]:
    return [page for page in MANUSCRIPT_PAGES if page.label.startswith("附录 ")]


def back_matter_manuscript_pages() -> list[ManuscriptPage]:
    return [
        page for page in MANUSCRIPT_PAGES
        if page not in chapter_manuscript_pages() and page not in appendix_manuscript_pages()
    ]

TEACHING_PAGES = [
    TeachingPage(
        label="第 1 章 学习指南",
        source=ROOT / "chapter-01-study-guide.md",
        output="chapter-01-study-guide.html",
        description="帮助学生把第 1 章读成历史结构、关键问题与项目定位的认知地图。",
        chapter_output="chapter-01.html",
        chapter_label="第 1 章 开源的起源与发展",
        kind="学习指南",
    ),
    TeachingPage(
        label="第 1 章 教学指南",
        source=ROOT / "chapter-01-instructor-guide.md",
        output="chapter-01-instructor-guide.html",
        description="帮助教师组织第 1 章的历史主线、讨论重点与项目启动定位。",
        chapter_output="chapter-01.html",
        chapter_label="第 1 章 开源的起源与发展",
        kind="教学指南",
    ),
    TeachingPage(
        label="第 2 章 学习指南",
        source=ROOT / "chapter-02-study-guide.md",
        output="chapter-02-study-guide.html",
        description="帮助学生把第 2 章从许可证名词表读成制度边界与项目判断框架。",
        chapter_output="chapter-02.html",
        chapter_label="第 2 章 自由软件、开源软件与许可证",
        kind="学习指南",
    ),
    TeachingPage(
        label="第 2 章 教学指南",
        source=ROOT / "chapter-02-instructor-guide.md",
        output="chapter-02-instructor-guide.html",
        description="帮助教师组织第 2 章的制度判断、边界讲解与项目许可证讨论。",
        chapter_output="chapter-02.html",
        chapter_label="第 2 章 自由软件、开源软件与许可证",
        kind="教学指南",
    ),
    TeachingPage(
        label="第 3 章 学习指南",
        source=ROOT / "chapter-03-study-guide.md",
        output="chapter-03-study-guide.html",
        description="帮助学生把第 3 章读成治理基础设施、角色结构与社区进入路径。",
        chapter_output="chapter-03.html",
        chapter_label="第 3 章 开源社区与治理",
        kind="学习指南",
    ),
    TeachingPage(
        label="第 3 章 教学指南",
        source=ROOT / "chapter-03-instructor-guide.md",
        output="chapter-03-instructor-guide.html",
        description="帮助教师组织第 3 章的角色梯度、治理对象与团队协作映射。",
        chapter_output="chapter-03.html",
        chapter_label="第 3 章 开源社区与治理",
        kind="教学指南",
    ),
    TeachingPage(
        label="第 4 章 学习指南",
        source=ROOT / "chapter-04-study-guide.md",
        output="chapter-04-study-guide.html",
        description="帮助学生把第 4 章读成变更控制主链，而不是平台按钮教程。",
        chapter_output="chapter-04.html",
        chapter_label="第 4 章 开源开发的基本工程流程",
        kind="学习指南",
    ),
    TeachingPage(
        label="第 4 章 教学指南",
        source=ROOT / "chapter-04-instructor-guide.md",
        output="chapter-04-instructor-guide.html",
        description="帮助教师组织第 4 章的流程主链、门禁逻辑与项目工作流训练。",
        chapter_output="chapter-04.html",
        chapter_label="第 4 章 开源开发的基本工程流程",
        kind="教学指南",
    ),
    TeachingPage(
        label="第 5 章 学习指南",
        source=ROOT / "chapter-05-study-guide.md",
        output="chapter-05-study-guide.html",
        description="帮助学生把第 5 章读成面对陌生仓库时的整体判断方法。当前为骨架稿。",
        chapter_output="chapter-05.html",
        chapter_label="第 5 章 阅读与理解开源项目",
        kind="学习指南",
    ),
    TeachingPage(
        label="第 5 章 教学指南",
        source=ROOT / "chapter-05-instructor-guide.md",
        output="chapter-05-instructor-guide.html",
        description="帮助教师组织第 5 章的项目阅读方法、健康度判断与行动选择。当前为骨架稿。",
        chapter_output="chapter-05.html",
        chapter_label="第 5 章 阅读与理解开源项目",
        kind="教学指南",
    ),
    TeachingPage(
        label="第 6 章 学习指南",
        source=ROOT / "chapter-06-study-guide.md",
        output="chapter-06-study-guide.html",
        description="帮助学生把第 6 章读成第一次贡献的进入路径与贡献组织链。当前为骨架稿。",
        chapter_output="chapter-06.html",
        chapter_label="第 6 章 参与开源项目",
        kind="学习指南",
    ),
    TeachingPage(
        label="第 6 章 教学指南",
        source=ROOT / "chapter-06-instructor-guide.md",
        output="chapter-06-instructor-guide.html",
        description="帮助教师组织第 6 章的边界判断、PR 组织与 review 协作。当前为骨架稿。",
        chapter_output="chapter-06.html",
        chapter_label="第 6 章 参与开源项目",
        kind="教学指南",
    ),
    TeachingPage(
        label="第 7 章 学习指南",
        source=ROOT / "chapter-07-study-guide.md",
        output="chapter-07-study-guide.html",
        description="帮助学生把第 7 章读成 AI 进入开源流程后的责任链与验证链。当前为骨架稿。",
        chapter_output="chapter-07.html",
        chapter_label="第 7 章 AI 辅助的开源开发实践",
        kind="学习指南",
    ),
    TeachingPage(
        label="第 7 章 教学指南",
        source=ROOT / "chapter-07-instructor-guide.md",
        output="chapter-07-instructor-guide.html",
        description="帮助教师组织第 7 章的 AI 使用边界、人工责任链与 agentic workflow。当前为骨架稿。",
        chapter_output="chapter-07.html",
        chapter_label="第 7 章 AI 辅助的开源开发实践",
        kind="教学指南",
    ),
    TeachingPage(
        label="第 8 章 学习指南",
        source=ROOT / "chapter-08-study-guide.md",
        output="chapter-08-study-guide.html",
        description="帮助学生把第 8 章读成维护者视角下的项目公共界面、发布与维护基线。当前为骨架稿。",
        chapter_output="chapter-08.html",
        chapter_label="第 8 章 组织与发布你的开源项目",
        kind="学习指南",
    ),
    TeachingPage(
        label="第 8 章 教学指南",
        source=ROOT / "chapter-08-instructor-guide.md",
        output="chapter-08-instructor-guide.html",
        description="帮助教师组织第 8 章的维护者视角、版本发布与最小安全基线。当前为骨架稿。",
        chapter_output="chapter-08.html",
        chapter_label="第 8 章 组织与发布你的开源项目",
        kind="教学指南",
    ),
]

LAB_PAGES = [
    TeachingPage(
        label="第 1 章 实验与项目材料",
        source=ROOT / "chapter-01-lab-project-materials.md",
        output="chapter-01-lab-project-materials.html",
        description="第 1 章的章节级实验 / 项目材料，围绕项目观察、项目阅读与《项目公共性说明》展开。",
        chapter_output="chapter-01.html",
        chapter_label="第 1 章 开源的起源与发展",
        kind="实验与项目材料",
    ),
    TeachingPage(
        label="第 2 章 实验与项目材料",
        source=ROOT / "chapter-02-lab-project-materials.md",
        output="chapter-02-lab-project-materials.html",
        description="第 2 章的章节级实验 / 项目材料，围绕许可证选择、来源清点与制度边界建立展开。",
        chapter_output="chapter-02.html",
        chapter_label="第 2 章 自由软件、开源软件与许可证",
        kind="实验与项目材料",
    ),
    TeachingPage(
        label="第 3 章 实验与项目材料",
        source=ROOT / "chapter-03-lab-project-materials.md",
        output="chapter-03-lab-project-materials.html",
        description="第 3 章的章节级实验 / 项目材料，围绕角色分工、贡献入口与治理基线建立展开。",
        chapter_output="chapter-03.html",
        chapter_label="第 3 章 开源社区与治理",
        kind="实验与项目材料",
    ),
    TeachingPage(
        label="第 4 章 实验与项目材料",
        source=ROOT / "chapter-04-lab-project-materials.md",
        output="chapter-04-lab-project-materials.html",
        description="第 4 章的章节级实验 / 项目材料，围绕工作流、评审、CI 与发布清单展开。",
        chapter_output="chapter-04.html",
        chapter_label="第 4 章 开源开发的基本工程流程",
        kind="实验与项目材料",
    ),
]

APPENDIX_PAGES = [
    TeachingPage(
        label="第 1 章 附录支撑",
        source=ROOT / "chapter-01-appendix-support.md",
        output="chapter-01-appendix-support.html",
        description="第 1 章的附录支撑，提供项目观察记录模板、历史主线梳理卡和《项目公共性说明》模板。",
        chapter_output="chapter-01.html",
        chapter_label="第 1 章 开源的起源与发展",
        kind="附录支撑",
    ),
    TeachingPage(
        label="第 2 章 附录支撑",
        source=ROOT / "chapter-02-appendix-support.md",
        output="chapter-02-appendix-support.html",
        description="第 2 章的附录支撑，提供许可证最小比较表、选择清单与《许可证与来源清点说明》模板。",
        chapter_output="chapter-02.html",
        chapter_label="第 2 章 自由软件、开源软件与许可证",
        kind="附录支撑",
    ),
    TeachingPage(
        label="第 3 章 附录支撑",
        source=ROOT / "chapter-03-appendix-support.md",
        output="chapter-03-appendix-support.html",
        description="第 3 章的附录支撑，提供治理文件最小清单、角色分工表和《角色分工与贡献入口草案》模板。",
        chapter_output="chapter-03.html",
        chapter_label="第 3 章 开源社区与治理",
        kind="附录支撑",
    ),
    TeachingPage(
        label="第 4 章 附录支撑",
        source=ROOT / "chapter-04-appendix-support.md",
        output="chapter-04-appendix-support.html",
        description="第 4 章的附录支撑，提供最小工作流检查单、PR 检查清单和《最小工作流与评审/发布清单》模板。",
        chapter_output="chapter-04.html",
        chapter_label="第 4 章 开源开发的基本工程流程",
        kind="附录支撑",
    ),
]

CASE_PACK_PAGES = [
    TeachingPage(
        label="第 1 章 案例教学包",
        source=ROOT / "chapter-01-case-teaching-pack.md",
        output="chapter-01-case-teaching-pack.html",
        description="第 1 章的案例教学包，围绕 GNU、Linux、Mozilla、Apache 与 GitHub 的历史角色展开。",
        chapter_output="chapter-01.html",
        chapter_label="第 1 章 开源的起源与发展",
        kind="案例教学包",
    ),
    TeachingPage(
        label="第 2 章 案例教学包",
        source=ROOT / "chapter-02-case-teaching-pack.md",
        output="chapter-02-case-teaching-pack.html",
        description="第 2 章的案例教学包，围绕 MIT、Apache-2.0、GPL 与“无许可证”反例展开。",
        chapter_output="chapter-02.html",
        chapter_label="第 2 章 自由软件、开源软件与许可证",
        kind="案例教学包",
    ),
    TeachingPage(
        label="第 3 章 案例教学包",
        source=ROOT / "chapter-03-case-teaching-pack.md",
        output="chapter-03-case-teaching-pack.html",
        description="第 3 章的案例教学包，围绕 Linux、Apache、Python 与治理对象展开。",
        chapter_output="chapter-03.html",
        chapter_label="第 3 章 开源社区与治理",
        kind="案例教学包",
    ),
    TeachingPage(
        label="第 4 章 案例教学包",
        source=ROOT / "chapter-04-case-teaching-pack.md",
        output="chapter-04-case-teaching-pack.html",
        description="第 4 章的案例教学包，围绕 CPython、Linux 与最小工作流对象展开。",
        chapter_output="chapter-04.html",
        chapter_label="第 4 章 开源开发的基本工程流程",
        kind="案例教学包",
    ),
]

LAB_STAGES = [
    LabStage(
        label="实验 1 开源观察与项目阅读",
        href="chapter-01-lab-project-materials.html",
        chapters="第 1 章",
        milestone="完成真实项目观察，建立项目公共性与历史位置的基本判断。",
        baseline="阅读 1-2 个真实项目，识别历史背景、用途、目标用户、仓库结构与许可证。",
        evidence="项目阅读报告；课堂汇报或小组讲解。",
        evaluation="是否超出 README 表层信息，能把项目放回开源历史与生态脉络中理解。",
        availability="已提供章节级实验材料",
    ),
    LabStage(
        label="实验 2 团队项目立项与许可证选择",
        href="chapter-02-lab-project-materials.html",
        chapters="第 2 章、第 8 章",
        milestone="完成团队项目立项，并建立制度与仓库最小基线。",
        baseline="确定项目主题、目标用户、MVP 范围，选择许可证并初始化公开仓库。",
        evidence="公开仓库链接；项目立项说明；许可证选择说明。",
        evaluation="项目范围是否合理，许可证是否有依据，仓库是否具备公开项目的最小形态。",
        availability="已提供章节级实验材料",
    ),
    LabStage(
        label="实验 3 治理基线与协作机制建立",
        href="chapter-03-lab-project-materials.html",
        chapters="第 3 章、第 4 章",
        milestone="把团队合作转化为可执行的治理与协作规则。",
        baseline="明确角色分工，建立 Issue 管理机制，补齐 CONTRIBUTING、模板与基本协作规则。",
        evidence="治理文件；第一轮 Issue 拆分结果；团队协作规则说明。",
        evaluation="是否从“一起写代码”转向“按规则协作”，分工是否真实可执行。",
        availability="已提供章节级实验材料",
    ),
    LabStage(
        label="实验 4 GitHub 协作流与最小 CI",
        href="chapter-04-lab-project-materials.html",
        chapters="第 4 章",
        milestone="跑通第一次真实变更控制链路。",
        baseline="使用 Issue、Branch、PR、Review 与最小 CI 完成至少一轮协作开发。",
        evidence="PR 记录；Review 记录；CI 运行结果。",
        evaluation="是否真正通过 PR 协作而非直接推送主分支，自动化检查是否进入日常流程。",
        availability="已提供章节级实验材料",
    ),
    LabStage(
        label="实验 5 外部项目理解或首次贡献",
        href=None,
        chapters="第 5 章、第 6 章",
        milestone="从课程内项目转向课程外项目理解与外部参与准备。",
        baseline="识别贡献入口，评估项目可参与性，并完成一次模拟贡献分析或跨团队贡献。",
        evidence="贡献分析报告；提交记录或 PR / Issue 链接。",
        evaluation="是否理解“参与外部项目”与“开发自己项目”的差异，并具备基本外部沟通意识。",
        availability="待第 5-6 章稳定后细化",
    ),
    LabStage(
        label="实验 6 团队项目 MVP 迭代",
        href=None,
        chapters="第 4 章、第 6 章、第 8 章",
        milestone="围绕 MVP 完成第一次真正可演示的项目迭代。",
        baseline="让功能、文档、测试、Issue、PR、Review 与版本记录一起推进。",
        evidence="阶段版本；MVP 演示；迭代记录。",
        evaluation="是否形成持续演进的项目，而不是临时拼接的功能集合。",
        availability="待第 6-8 章稳定后细化",
    ),
    LabStage(
        label="实验 7 AI 辅助开发与人工治理",
        href=None,
        chapters="第 7 章",
        milestone="把 AI 使用正式纳入开源流程和人工责任链。",
        baseline="选择真实任务使用 AI 辅助完成，并保留记录、人工审查、测试与验收证据。",
        evidence="AI 辅助任务记录；修改前后对比；人工审查与测试证据；反思报告。",
        evaluation="是否把 AI 放在开源流程之内，而不是绕过治理、审查与验证。",
        availability="待第 7 章稳定后细化",
    ),
    LabStage(
        label="实验 8 发布、归档与项目复盘",
        href=None,
        chapters="第 8 章",
        milestone="完成从课程项目到公开项目的最后一次转换。",
        baseline="完成正式版本发布，补齐 CHANGELOG、安装/使用说明，并形成复盘与维护计划。",
        evidence="Release 页面或版本标签；变更记录；最终仓库链接；项目复盘文档。",
        evaluation="是否完成从“课程提交”到“公开发布”的转换，并留下可继续维护的项目基础。",
        availability="待第 8 章稳定后细化",
    ),
]

SUPPORT_PAGES = [*TEACHING_PAGES, *LAB_PAGES, *APPENDIX_PAGES, *CASE_PACK_PAGES]

LINK_MAP = {
    str(page.source.name): page.output for page in [*MANUSCRIPT_PAGES, *SUPPORT_PAGES]
}

CSS = """
:root {
  --bg: #f5f1e6;
  --bg-deep: #e8e1d0;
  --panel: #fffdf7;
  --line: #d9cfbe;
  --line-strong: #b9ad99;
  --text: #1f2825;
  --muted: #5d6b66;
  --accent: #1a5a4e;
  --accent-strong: #103c35;
  --accent-soft: #e2ece7;
  --accent-soft-2: #d4e3dc;
  --code-bg: #f2ede1;
  --shadow: 0 16px 38px rgba(31, 40, 37, 0.08);
  --max: 1240px;
}

* { box-sizing: border-box; }
html { scroll-behavior: smooth; }
body {
  margin: 0;
  font-family: Georgia, "Noto Serif SC", "Songti SC", serif;
  color: var(--text);
  background:
    radial-gradient(circle at top left, rgba(26, 90, 78, 0.08), transparent 34%),
    radial-gradient(circle at top right, rgba(16, 60, 53, 0.05), transparent 28%),
    linear-gradient(180deg, #faf7ef 0%, var(--bg) 100%);
  line-height: 1.7;
}

a {
  color: var(--accent);
  text-decoration: none;
}

a:hover {
  text-decoration: underline;
}

code {
  font-family: "JetBrains Mono", "SFMono-Regular", Consolas, monospace;
}

.site-header {
  position: sticky;
  top: 0;
  z-index: 10;
  backdrop-filter: blur(12px);
  background: rgba(250, 247, 239, 0.9);
  border-bottom: 1px solid rgba(185, 173, 153, 0.72);
}

.site-header-inner {
  max-width: var(--max);
  margin: 0 auto;
  padding: 14px 24px;
  display: flex;
  align-items: center;
  justify-content: space-between;
  gap: 18px;
}

.brand {
  display: flex;
  align-items: center;
  gap: 12px;
  color: var(--text);
}

.brand-mark {
  width: 40px;
  height: 40px;
  border-radius: 12px;
  display: grid;
  place-items: center;
  font-weight: 700;
  color: #fff;
  background:
    linear-gradient(135deg, var(--accent) 0%, var(--accent-strong) 100%);
  box-shadow:
    inset 0 0 0 1px rgba(255, 255, 255, 0.18),
    0 8px 18px rgba(16, 60, 53, 0.16);
}

.brand-copy strong {
  display: block;
  font-size: 0.98rem;
}

.brand-copy span {
  display: block;
  color: var(--muted);
  font-size: 0.88rem;
}

.global-nav {
  display: flex;
  flex-wrap: wrap;
  gap: 8px;
}

.global-nav a {
  padding: 9px 12px;
  border-radius: 999px;
  border: 1px solid transparent;
  color: var(--text);
  font-size: 0.95rem;
  transition: background 120ms ease, border-color 120ms ease, color 120ms ease;
}

.global-nav a:hover {
  text-decoration: none;
  background: rgba(26, 90, 78, 0.05);
  border-color: rgba(26, 90, 78, 0.08);
}

.global-nav a.active {
  background: var(--accent-soft);
  border-color: rgba(26, 90, 78, 0.15);
  color: var(--accent-strong);
  font-weight: 700;
}

.shell {
  max-width: var(--max);
  margin: 0 auto;
  padding: 24px;
}

.hero {
  border: 1px solid var(--line);
  background:
    radial-gradient(circle at top right, rgba(26, 90, 78, 0.13), transparent 32%),
    linear-gradient(135deg, rgba(26, 90, 78, 0.08), rgba(255, 253, 247, 0.94));
  box-shadow: var(--shadow);
  border-radius: 24px;
  padding: 32px;
  margin-bottom: 24px;
}

.hero .eyebrow {
  color: var(--accent);
  font-size: 0.9rem;
  letter-spacing: 0.06em;
  text-transform: uppercase;
  margin-bottom: 10px;
}

.hero h1 {
  margin: 0 0 10px 0;
  font-size: clamp(2.2rem, 5vw, 3.8rem);
  line-height: 1.04;
}

.hero p {
  margin: 0;
  max-width: 860px;
  color: var(--muted);
  font-size: 1.05rem;
}

.hero-context {
  margin-top: 16px;
  display: flex;
  flex-wrap: wrap;
  gap: 14px;
}

.hero-context-item {
  font-size: 0.94rem;
  color: var(--muted);
}

.hero-context-item strong {
  color: var(--accent-strong);
  margin-right: 6px;
}

.layout {
  display: grid;
  grid-template-columns: 280px minmax(0, 1fr);
  gap: 24px;
}

.layout.single {
  grid-template-columns: 1fr;
}

.panel {
  border: 1px solid var(--line);
  background: var(--panel);
  box-shadow: var(--shadow);
  border-radius: 18px;
}

.sidebar {
  padding: 18px;
  position: sticky;
  top: 84px;
  height: fit-content;
}

.sidebar-block + .sidebar-block {
  margin-top: 18px;
  padding-top: 18px;
  border-top: 1px solid #ebe2d1;
}

.sidebar h2,
.sidebar h3 {
  margin: 0 0 10px 0;
  font-size: 0.92rem;
  letter-spacing: 0.05em;
  text-transform: uppercase;
  color: var(--muted);
}

.nav-list,
.toc ul {
  list-style: none;
  margin: 0;
  padding: 0;
}

.nav-list li + li,
.toc li + li {
  margin-top: 8px;
}

.nav-list a {
  display: block;
  padding: 10px 12px;
  border-radius: 12px;
  border: 1px solid transparent;
  color: var(--text);
  transition: background 120ms ease, border-color 120ms ease, color 120ms ease;
}

.nav-list a:hover {
  text-decoration: none;
  background: rgba(26, 90, 78, 0.05);
  border-color: rgba(26, 90, 78, 0.08);
}

.nav-list a.active {
  background: var(--accent-soft);
  border-color: rgba(26, 90, 78, 0.15);
  font-weight: 700;
}

.toc a {
  color: var(--text);
}

.toc ul ul {
  margin-top: 8px;
  padding-left: 14px;
}

.content {
  padding: 34px 40px;
  min-width: 0;
}

.page-header {
  margin-bottom: 18px;
}

.page-header h1 {
  margin: 0 0 8px 0;
  font-size: clamp(1.9rem, 4vw, 2.8rem);
  line-height: 1.08;
}

.page-header p {
  margin: 0;
  color: var(--muted);
}

.lead {
  color: var(--muted);
  max-width: 900px;
}

.content h1:first-child {
  margin-top: 0;
}

.content h1,
.content h2,
.content h3,
.content h4 {
  line-height: 1.25;
  scroll-margin-top: 92px;
}

.content h2 {
  margin-top: 2.2rem;
  padding-top: 0.45rem;
  border-top: 1px solid #ebe2d1;
}

.content h3 {
  margin-top: 1.6rem;
}

.content p,
.content ul,
.content ol,
.content table,
.content blockquote {
  margin: 1rem 0;
}

.content code {
  background: var(--code-bg);
  padding: 0.14rem 0.38rem;
  border-radius: 6px;
  font-size: 0.92em;
}

.content pre {
  background: #1f2937;
  color: #f8fafc;
  padding: 16px;
  border-radius: 14px;
  overflow: auto;
}

.content pre code {
  background: transparent;
  padding: 0;
  color: inherit;
}

.content blockquote {
  border-left: 4px solid var(--accent);
  padding: 8px 16px;
  background: rgba(26, 90, 78, 0.06);
  border-radius: 0 12px 12px 0;
}

.content table {
  width: 100%;
  border-collapse: collapse;
  display: block;
  overflow-x: auto;
}

.content th,
.content td {
  border: 1px solid #e7dece;
  padding: 10px 12px;
  text-align: left;
  vertical-align: top;
}

.content th {
  background: #f1ebde;
}

.content img {
  max-width: 100%;
  height: auto;
}

.book-figure {
  margin: 1.5rem 0;
  padding: 18px;
  border: 1px solid #e7dece;
  border-radius: 18px;
  background:
    linear-gradient(180deg, rgba(255, 255, 255, 0.94), rgba(250, 247, 239, 0.98));
}

.book-figure img {
  display: block;
  width: 100%;
  height: auto;
  border-radius: 12px;
}

.book-figure figcaption {
  margin-top: 12px;
  text-align: center;
  color: var(--muted);
  font-size: 0.95rem;
}

.book-table-caption {
  margin: 1.4rem 0 0.45rem 0;
  color: var(--accent-strong);
  font-weight: 700;
}

.history-story {
  margin: 1.5rem 0;
  padding: 18px 20px;
  border: 1px solid #ddd1bd;
  border-left: 5px solid var(--accent);
  border-radius: 18px;
  background:
    linear-gradient(180deg, rgba(248, 244, 235, 0.98), rgba(255, 253, 247, 0.96));
}

.history-story-label {
  margin: 0 0 10px 0;
  color: var(--accent-strong);
  font-size: 0.85rem;
  font-weight: 700;
  letter-spacing: 0.08em;
  text-transform: uppercase;
}

.history-story p {
  margin: 0;
}

.history-story p + p {
  margin-top: 10px;
}

.card-grid {
  display: grid;
  gap: 14px;
}

.card-grid.two {
  grid-template-columns: repeat(2, minmax(0, 1fr));
}

.card-grid.three {
  grid-template-columns: repeat(3, minmax(0, 1fr));
}

.card {
  border: 1px solid #e7dece;
  border-radius: 18px;
  padding: 18px 20px;
  background:
    linear-gradient(180deg, rgba(255, 255, 255, 0.92), rgba(250, 247, 239, 0.96));
  transition: transform 140ms ease, box-shadow 140ms ease, border-color 140ms ease;
}

.card:hover {
  transform: translateY(-1px);
  border-color: rgba(26, 90, 78, 0.16);
  box-shadow: 0 10px 24px rgba(31, 40, 37, 0.07);
}

.card h3 {
  margin: 0 0 8px 0;
  line-height: 1.25;
}

.card p {
  margin: 0;
  color: var(--muted);
}

.card p + p {
  margin-top: 10px;
}

.card-meta {
  margin-top: 10px;
  color: var(--text);
  font-size: 0.95rem;
}

.stage-card ul {
  margin: 12px 0 0 18px;
  padding: 0;
  color: var(--muted);
}

.stage-card li + li {
  margin-top: 8px;
}

.stage-status {
  display: inline-block;
  margin-top: 12px;
  padding: 5px 10px;
  border-radius: 999px;
  background: #ece5d6;
  color: var(--accent-strong);
  font-size: 0.88rem;
  font-weight: 700;
}

.card-links {
  color: var(--text);
  font-size: 0.96rem;
}

.card-links a + a {
  margin-left: 12px;
}

.section-title {
  margin: 0 0 12px 0;
  font-size: 1.3rem;
}

.feature-list {
  padding-left: 18px;
}

.feature-list li + li {
  margin-top: 8px;
}

.status-note {
  margin-top: 18px;
  padding: 14px 16px;
  border-radius: 14px;
  border: 1px solid #e5dbcb;
  background: #f7f2e8;
  color: var(--muted);
}

.meta {
  margin-top: 24px;
  padding-top: 16px;
  border-top: 1px solid #ebe2d1;
  color: var(--muted);
  font-size: 0.95rem;
}

.site-footer {
  margin-top: 26px;
  color: var(--muted);
  font-size: 0.92rem;
}

@media (max-width: 1024px) {
  .layout {
    grid-template-columns: 1fr;
  }

  .sidebar {
    position: static;
  }
}

@media (max-width: 760px) {
  .site-header-inner {
    flex-direction: column;
    align-items: flex-start;
  }

  .shell {
    padding: 18px;
  }

  .hero {
    padding: 24px 22px;
  }

  .content {
    padding: 24px 22px;
  }

  .card-grid.two,
  .card-grid.three {
    grid-template-columns: 1fr;
  }
}
"""


def first_heading(markdown_text: str) -> str:
    match = re.search(r"^#\s+(.+)$", markdown_text, flags=re.MULTILINE)
    if match:
        return match.group(1).strip()
    return "Untitled"


def rewrite_links(markdown_text: str) -> str:
    def replace_absolute(match: re.Match[str]) -> str:
        label = match.group(1)
        target = match.group(2)
        md_name = Path(target).name
        output = LINK_MAP.get(md_name)
        if output:
            return f"[{label}]({output})"
        return label

    def replace_relative(match: re.Match[str]) -> str:
        label = match.group(1)
        target = match.group(2)
        output = LINK_MAP.get(target)
        if output:
            return f"[{label}]({output})"
        return match.group(0)

    markdown_text = re.sub(
        r"\[([^\]]+)\]\((/home/bistu/opensource-book/[^)#]+\.md)(?:[:#][^)]+)?\)",
        replace_absolute,
        markdown_text,
    )
    markdown_text = re.sub(
        r"\[([^\]]+)\]\(([^/)]+\.md)\)",
        replace_relative,
        markdown_text,
    )
    return markdown_text


def markdown_to_html(text: str) -> tuple[str, str, str]:
    raw = rewrite_links(text)
    title = first_heading(raw)
    md = markdown.Markdown(
        extensions=["toc", "tables", "fenced_code", "sane_lists"],
        extension_configs={"toc": {"permalink": True}},
        output_format="html5",
    )
    body = md.convert(raw)
    toc = getattr(md, "toc", "")
    return title, body, toc


def render_markdown(source: Path) -> tuple[str, str, str]:
    return markdown_to_html(source.read_text(encoding="utf-8"))


def global_nav_html(current_section: str) -> str:
    items = []
    for section in SECTIONS:
        cls = "active" if section.key == current_section else ""
        items.append(
            f'<a class="{cls}" href="{section.output}">{html.escape(section.label)}</a>'
        )
    return "\n".join(items)


def hero_context_html(current_section: str) -> str:
    context_map = {
        "home": [
            ("分区", "首页"),
            ("类型", "课程入口"),
            ("发布", "GitHub Pages 自动构建"),
        ],
        "course": [
            ("分区", "课程说明"),
            ("类型", "课程级材料"),
            ("发布", "GitHub Pages 自动构建"),
        ],
        "manuscript": [
            ("分区", "书稿"),
            ("类型", "技术书稿"),
            ("发布", "GitHub Pages 自动构建"),
        ],
        "teaching": [
            ("分区", "教学支持"),
            ("类型", "课程支持层"),
            ("发布", "GitHub Pages 自动构建"),
        ],
        "labs": [
            ("分区", "实验与项目"),
            ("类型", "实验与项目材料"),
            ("发布", "GitHub Pages 自动构建"),
        ],
        "cases": [
            ("分区", "案例与参考"),
            ("类型", "案例库与教学案例"),
            ("发布", "GitHub Pages 自动构建"),
        ],
    }
    items = []
    for label, value in context_map.get(current_section, []):
        items.append(
            f'<span class="hero-context-item"><strong>{html.escape(label)}:</strong>{html.escape(value)}</span>'
        )
    return "\n".join(items)


def manuscript_nav_html(current_output: str) -> str:
    items = ['<li><a class="{cls}" href="manuscript.html">书稿目录</a></li>'.format(
        cls="active" if current_output == "manuscript.html" else ""
    )]
    for page in MANUSCRIPT_PAGES:
        cls = "active" if page.output == current_output else ""
        items.append(
            f'<li><a class="{cls}" href="{page.output}">{html.escape(page.label)}</a></li>'
        )
    return "\n".join(items)


def teaching_nav_html(current_output: str) -> str:
    items = ['<li><a class="{cls}" href="teaching-support.html">教学支持目录</a></li>'.format(
        cls="active" if current_output == "teaching-support.html" else ""
    )]
    for page in TEACHING_PAGES:
        cls = "active" if page.output == current_output else ""
        items.append(
            f'<li><a class="{cls}" href="{page.output}">{html.escape(page.label)}</a></li>'
        )
    return "\n".join(items)


def appendix_nav_html(current_output: str) -> str:
    items = ['<li><a class="{cls}" href="teaching-support.html">教学支持目录</a></li>'.format(
        cls="active" if current_output == "teaching-support.html" else ""
    )]
    for page in APPENDIX_PAGES:
        cls = "active" if page.output == current_output else ""
        items.append(
            f'<li><a class="{cls}" href="{page.output}">{html.escape(page.label)}</a></li>'
        )
    return "\n".join(items)


def lab_nav_html(current_output: str) -> str:
    items = ['<li><a class="{cls}" href="labs-project.html">实验与项目目录</a></li>'.format(
        cls="active" if current_output == "labs-project.html" else ""
    )]
    for page in LAB_PAGES:
        cls = "active" if page.output == current_output else ""
        items.append(
            f'<li><a class="{cls}" href="{page.output}">{html.escape(page.label)}</a></li>'
        )
    return "\n".join(items)


def case_pack_nav_html(current_output: str) -> str:
    items = ['<li><a class="{cls}" href="cases-references.html">案例与参考目录</a></li>'.format(
        cls="active" if current_output == "cases-references.html" else ""
    )]
    for page in CASE_PACK_PAGES:
        cls = "active" if page.output == current_output else ""
        items.append(
            f'<li><a class="{cls}" href="{page.output}">{html.escape(page.label)}</a></li>'
        )
    return "\n".join(items)


def teaching_pages_for_chapter(chapter_output: str) -> list[TeachingPage]:
    return [page for page in TEACHING_PAGES if page.chapter_output == chapter_output]


def lab_pages_for_chapter(chapter_output: str) -> list[TeachingPage]:
    return [page for page in LAB_PAGES if page.chapter_output == chapter_output]


def appendix_pages_for_chapter(chapter_output: str) -> list[TeachingPage]:
    return [page for page in APPENDIX_PAGES if page.chapter_output == chapter_output]


def case_pack_pages_for_chapter(chapter_output: str) -> list[TeachingPage]:
    return [page for page in CASE_PACK_PAGES if page.chapter_output == chapter_output]


def support_pages_for_chapter(chapter_output: str) -> list[TeachingPage]:
    return [page for page in SUPPORT_PAGES if page.chapter_output == chapter_output]


def manuscript_page_for_output(chapter_output: str) -> ManuscriptPage | None:
    for page in MANUSCRIPT_PAGES:
        if page.output == chapter_output:
            return page
    return None


def section_cards(cards: list[tuple[str, str, str]]) -> str:
    rendered = []
    for title, href, desc in cards:
        rendered.append(
            f"""
            <article class="card">
              <h3><a href="{href}">{html.escape(title)}</a></h3>
              <p>{html.escape(desc)}</p>
            </article>
            """
        )
    return "\n".join(rendered)


def lab_stage_cards(stages: list[LabStage]) -> str:
    rendered = []
    for stage in stages:
        title = (
            f'<a href="{stage.href}">{html.escape(stage.label)}</a>'
            if stage.href
            else html.escape(stage.label)
        )
        rendered.append(
            f"""
            <article class="card stage-card">
              <h3>{title}</h3>
              <p class="card-meta"><strong>对应章节：</strong> {html.escape(stage.chapters)}</p>
              <p>{html.escape(stage.milestone)}</p>
              <ul>
                <li><strong>基础项：</strong> {html.escape(stage.baseline)}</li>
                <li><strong>交付证据：</strong> {html.escape(stage.evidence)}</li>
                <li><strong>评价重点：</strong> {html.escape(stage.evaluation)}</li>
              </ul>
              <p class="stage-status">{html.escape(stage.availability)}</p>
            </article>
            """
        )
    return "\n".join(rendered)


def teaching_chapter_cards() -> str:
    rendered = []
    for chapter in MANUSCRIPT_PAGES:
        teaching_pages = teaching_pages_for_chapter(chapter.output)
        if not teaching_pages:
            continue
        links = "".join(
            f'<a href="{page.output}">{html.escape(page.kind)}</a>'
            for page in teaching_pages
        )
        links = links.replace("</a><a ", "</a> <span>·</span> <a ")
        rendered.append(
            f"""
            <article class="card">
              <h3><a href="{chapter.output}">{html.escape(chapter.label)}</a></h3>
              <p>{html.escape(chapter.description)}</p>
              <p class="card-links"><strong>配套入口：</strong> {links}</p>
            </article>
            """
        )
    return "\n".join(rendered)


def support_page_cards(pages: list[TeachingPage]) -> str:
    return section_cards([(page.label, page.output, page.description) for page in pages])


def page_shell(
    *,
    title: str,
    current_section: str,
    hero_title: str,
    hero_text: str,
    inner: str,
    sidebar_html: str = "",
) -> str:
    layout_class = "layout" if sidebar_html else "layout single"
    sidebar = f'<aside class="sidebar panel">{sidebar_html}</aside>' if sidebar_html else ""
    return f"""<!doctype html>
<html lang="zh-CN">
  <head>
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <title>{html.escape(title)} | 开源软件开发技术课程网站</title>
    <link rel="stylesheet" href="assets/style.css">
  </head>
  <body>
    <header class="site-header">
      <div class="site-header-inner">
        <a class="brand" href="index.html">
          <span class="brand-mark">OS</span>
          <span class="brand-copy">
            <strong>开源软件开发技术</strong>
            <span>课程网站与书稿预览</span>
          </span>
        </a>
        <nav class="global-nav" aria-label="全站导航">
          {global_nav_html(current_section)}
        </nav>
      </div>
    </header>
    <div class="shell">
      <section class="hero panel">
        <div class="eyebrow">开源软件开发技术</div>
        <h1>{html.escape(hero_title)}</h1>
        <p>{html.escape(hero_text)}</p>
        <div class="hero-context">
          {hero_context_html(current_section)}
        </div>
      </section>
      <div class="{layout_class}">
        {sidebar}
        <main class="content panel">
          {inner}
        </main>
      </div>
      <footer class="site-footer">
        站点由 <code>scripts/build_pages.py</code> 自动生成，并通过 GitHub Actions 自动部署到 GitHub Pages。
      </footer>
    </div>
  </body>
</html>
"""


def write_page(filename: str, content: str) -> None:
    (SITE_DIR / filename).write_text(content, encoding="utf-8")


def build_home() -> None:
    section_html = section_cards(
        [
            ("课程说明", "course.html", "课程定位、材料体系、当前公开进度与整体使用路径。"),
            ("书稿", "manuscript.html", "第 1-8 章书稿、附录与书后工具材料。"),
            ("教学支持", "teaching-support.html", "第 1-8 章学习指南与教学指南的在线阅读入口。"),
            ("实验与项目", "labs-project.html", "团队项目主线、实验阶段与里程碑。"),
            ("案例与参考", "cases-references.html", "经典/现代案例、案例教学包、专题附录与核心外部参考。"),
        ]
    )
    chapter_html = section_cards(
        [(page.label, page.output, page.description) for page in MANUSCRIPT_PAGES]
    )
    now = datetime.now(timezone.utc).strftime("%Y-%m-%d %H:%M UTC")
    inner = f"""
    <header class="page-header">
      <h1>课程首页</h1>
      <p>本站不是单纯的书稿预览页，而是“课程网站 + 书稿阅读区”的组合。首页负责全局分发，具体阅读和使用在各分区内展开。</p>
    </header>

    <section>
      <h2 class="section-title">核心入口</h2>
      <div class="card-grid three">
        {section_html}
      </div>
    </section>

    <section>
      <h2 class="section-title">当前可在线阅读的书稿与书后材料</h2>
      <div class="card-grid two">
        {chapter_html}
      </div>
    </section>

    <section class="status-note">
      <strong>当前状态：</strong>课程网站已具备全站导航、书稿阅读区、教学支持入口与实验/案例入口。当前上线内容包括第 1-4 章扩写稿、第 5-8 章书稿骨架、4 个附录、2 项书后工具材料（全书术语表与全书参考文献）、第 1-8 章教学支持、章节级实验材料、附录支撑与案例教学包；其中第 5-8 章教学支持当前为骨架稿。
    </section>

    <section class="meta">
      <p>生成时间：{html.escape(now)}</p>
    </section>
    """
    write_page(
        "index.html",
        page_shell(
            title="课程首页",
            current_section="home",
            hero_title="开源软件开发技术课程网站",
            hero_text="面向课程运行、书稿阅读、实验组织与案例参考的一体化课程站点。首页用于分发，书稿只是其中一个主要分区。",
            inner=inner,
        ),
    )


def build_course_page() -> None:
    inner = f"""
    <header class="page-header">
      <h1>课程说明</h1>
      <p>本课程以“开源软件开发技术”为中心，而不是泛化的软件工程课或 AI 工具课。当前公开内容已经形成“课程说明 + 书稿 + 教学支持 + 实验与项目 + 案例与参考”的多层结构，目标是帮助读者理解开源、进入开源，并开始按现代开源方式参与和开发项目。</p>
    </header>

    <section>
      <h2 class="section-title">课程定位</h2>
      <ul class="feature-list">
        <li>前半部分讲长期稳定的核心内容：历史、文化、许可证、社区治理、基本工程机制。</li>
        <li>后半部分讲实践与演化更快的内容：项目参与、团队开发、AI 辅助开源实践。</li>
        <li>课程不是只讲概念，而是有贯穿全程的团队开源项目主线。</li>
      </ul>
    </section>

    <section>
      <h2 class="section-title">适用对象</h2>
      <ul class="feature-list">
        <li>面向具备正常计算机专业基础的本科生。</li>
        <li>默认前置条件：一门编程语言基础、基本命令行使用能力、基本程序阅读能力。</li>
        <li>课程整体采用“基线层 + 扩展层”结构，兼顾一般本科院校与能力更强的团队。</li>
      </ul>
    </section>

    <section>
      <h2 class="section-title">材料体系</h2>
      <ul class="feature-list">
        <li>技术书稿：稳定核心知识与书稿正文。</li>
        <li><a href="teaching-support.html">学习指南 / 教学指南</a>：教学支持层。</li>
        <li><a href="labs-project.html">实验与项目材料</a>：实验与团队项目材料。</li>
        <li><a href="cases-references.html">案例库 / 案例教学包</a>：经典案例、现代案例与课程级参考入口。</li>
        <li>附录与书后工具材料：承担专题补充、术语检索与来源回查。</li>
      </ul>
    </section>

    <section>
      <h2 class="section-title">8 章结构</h2>
      <div class="card-grid two">
        <article class="card"><h3>第 1-2 章</h3><p>开源的起源与发展；自由软件、开源软件与许可证。</p></article>
        <article class="card"><h3>第 3-4 章</h3><p>开源社区与治理；开源开发的基本工程流程。</p></article>
        <article class="card"><h3>第 5-6 章</h3><p>阅读与理解开源项目；参与开源项目。</p></article>
        <article class="card"><h3>第 7-8 章</h3><p>AI 辅助的开源开发实践；组织与发布你的开源项目。</p></article>
      </div>
    </section>

    <section>
      <h2 class="section-title">当前公开进度</h2>
      <ul class="feature-list">
        <li>书稿：第 1-4 章为扩写稿；第 5-8 章为骨架稿；已上线 4 个附录和 2 项书后工具材料。</li>
        <li>教学支持：第 1-8 章学习指南与教学指南已上线；其中第 5-8 章当前为骨架稿。</li>
        <li>章节级支撑材料：第 1-4 章已配套实验与项目材料、附录支撑与案例教学包。</li>
        <li>课程网站：已形成“课程说明 / 书稿 / 教学支持 / 实验与项目 / 案例与参考”五个分区。</li>
      </ul>
    </section>

    <section>
      <h2 class="section-title">当前已上线的教学支持</h2>
      <div class="card-grid two">
        {teaching_chapter_cards()}
      </div>
    </section>

    <section>
      <h2 class="section-title">当前已上线的实验与项目材料（第 1-4 章）</h2>
      <div class="card-grid two">
        {support_page_cards(LAB_PAGES)}
      </div>
    </section>

    <section>
      <h2 class="section-title">当前已上线的附录支撑（第 1-4 章）</h2>
      <div class="card-grid two">
        {support_page_cards(APPENDIX_PAGES)}
      </div>
    </section>

    <section>
      <h2 class="section-title">当前已上线的案例教学包（第 1-4 章）</h2>
      <div class="card-grid two">
        {support_page_cards(CASE_PACK_PAGES)}
      </div>
    </section>

    <section class="status-note">
      课程层页面用于说明整体结构、材料分层与当前公开进度；真正的长文阅读可进入“书稿”与“教学支持”分区，具体案例入口可进入“案例与参考”分区。
    </section>
    """
    write_page(
        "course.html",
        page_shell(
            title="课程说明",
            current_section="course",
            hero_title="课程定位与整体结构",
            hero_text="课程层页面负责说明课程目标、对象、结构和材料体系，帮助读者先看清课程系统，再进入具体书稿、教学支持与实验。",
            inner=inner,
        ),
    )


def build_manuscript_index() -> None:
    chapter_cards = section_cards(
        [(page.label, page.output, page.description) for page in chapter_manuscript_pages()]
    )
    appendix_cards = section_cards(
        [(page.label, page.output, page.description) for page in appendix_manuscript_pages()]
    )
    back_matter_cards = section_cards(
        [(page.label, page.output, page.description) for page in back_matter_manuscript_pages()]
    )
    inner = f"""
    <header class="page-header">
      <h1>书稿目录</h1>
      <p>这里集中展示各章正文、附录与书后工具材料。阅读页使用统一的章节导航与页内目录，便于连续阅读与横向比较。</p>
    </header>

    <section>
      <h2 class="section-title">章节正文</h2>
      <div class="card-grid two">
        {chapter_cards}
      </div>
    </section>

    <section>
      <h2 class="section-title">附录</h2>
      <div class="card-grid two">
        {appendix_cards}
      </div>
    </section>

    <section>
      <h2 class="section-title">书后工具材料</h2>
      <div class="card-grid two">
        {back_matter_cards}
      </div>
    </section>

    <section>
      <h2 class="section-title">配套教学支持</h2>
      <div class="card-grid two">
        {teaching_chapter_cards()}
      </div>
    </section>

    <section class="status-note">
      当前在线书稿范围：第 1-8 章、4 个附录与 2 项书后工具材料；其中第 1-4 章为扩写稿，第 5-8 章为当前骨架稿。教学支持已接入第 1-8 章，其中第 5-8 章当前为骨架稿。
    </section>
    """
    sidebar = f"""
    <div class="sidebar-block">
      <h2>书稿导航</h2>
      <ul class="nav-list">
        {manuscript_nav_html("manuscript.html")}
      </ul>
    </div>
    """
    write_page(
        "manuscript.html",
        page_shell(
            title="书稿目录",
            current_section="manuscript",
            hero_title="书稿阅读区",
            hero_text="书稿分区采用文档优先的阅读结构。首页提供目录，章节页提供左侧章节导航与页内目录。",
            inner=inner,
            sidebar_html=sidebar,
        ),
    )


def build_teaching_index() -> None:
    inner = f"""
    <header class="page-header">
      <h1>教学支持目录</h1>
      <p>教学支持分区承接基于书稿的学习与教学支架。当前已上线第 1-8 章的学习指南与教学指南；其中第 1-4 章较完整，第 5-8 章当前为骨架稿，可与对应书稿配套使用。</p>
    </header>

    <section>
      <h2 class="section-title">当前已上线</h2>
      <div class="card-grid two">
        {teaching_chapter_cards()}
      </div>
    </section>

    <section>
      <h2 class="section-title">附录支撑</h2>
      <div class="card-grid two">
        {support_page_cards(APPENDIX_PAGES)}
      </div>
    </section>

    <section>
      <h2 class="section-title">使用方式</h2>
      <ul class="feature-list">
        <li>学习指南：帮助学生把书稿读成学习路径、阅读重点、误区提醒与项目连接。</li>
        <li>教学指南：帮助教师把书稿转化为课堂组织、案例使用、评价证据与项目推进。</li>
        <li>附录支撑：提供模板、清单、比较表和最小操作支架，不替代书稿正文。</li>
        <li>教学支持页不替代书稿正文，而是与对应章节配套阅读。</li>
      </ul>
    </section>

    <section class="status-note">
      当前在线教学支持范围：第 1-8 章；其中第 5-8 章当前为骨架稿，后续将随书稿扩写继续细化。
    </section>
    """
    sidebar = f"""
    <div class="sidebar-block">
      <h2>教学支持导航</h2>
      <ul class="nav-list">
        {teaching_nav_html("teaching-support.html")}
      </ul>
    </div>
    """
    write_page(
        "teaching-support.html",
        page_shell(
            title="教学支持目录",
            current_section="teaching",
            hero_title="学习指南与教学指南",
            hero_text="教学支持分区用于承接基于书稿的学习支架与教学支架，使课程层材料能够围绕书稿协同使用。",
            inner=inner,
            sidebar_html=sidebar,
        ),
    )


def build_labs_page() -> None:
    inner = f"""
    <header class="page-header">
      <h1>实验与项目</h1>
      <p>课程实践不是书稿之外的附属材料，而是贯穿整门课程的团队开源项目主线。实验阶段与章节主线大体对应，但共同推动同一个项目逐步成形。</p>
    </header>

    <section>
      <h2 class="section-title">实践主线</h2>
      <ul class="feature-list">
        <li>阅读和分析真实开源项目。</li>
        <li>为团队项目建立许可证、治理和协作基线。</li>
        <li>通过 Issue、Branch、PR、Review、CI 推进真实迭代。</li>
        <li>在后续阶段进入外部项目理解、首次贡献与项目发布。</li>
      </ul>
    </section>

    <section>
      <h2 class="section-title">整体实验路线图</h2>
      <p>实验体系按 8 个阶段组织，每个阶段都同时说明对应章节、最低基础项、交付证据与评价重点。前四个阶段已接入章节级任务单，后四个阶段先保留课程级路线图，待相关章节稳定后再细化。</p>
      <div class="card-grid two">
        {lab_stage_cards(LAB_STAGES)}
      </div>
    </section>

    <section>
      <h2 class="section-title">当前可用任务单</h2>
      <div class="card-grid two">
        {support_page_cards(LAB_PAGES)}
      </div>
    </section>

    <section class="status-note">
      当前站点已完成课程级实验路线图，并接入前四章的章节级实验 / 项目材料；后续将补充跨章节实验总说明、统一 rubric、阶段交付模板与样例。
    </section>
    """
    write_page(
        "labs-project.html",
        page_shell(
            title="实验与项目",
            current_section="labs",
            hero_title="实验体系与团队项目主线",
            hero_text="实验分区负责承接课程实践：从项目阅读、立项与治理，到协作流、CI、贡献、发布与复盘。",
            inner=inner,
        ),
    )


def build_cases_page() -> None:
    reference_cards = section_cards(
        [
            (page.label, page.output, page.description)
            for page in [*appendix_manuscript_pages(), *back_matter_manuscript_pages()]
        ]
    )
    inner = f"""
    <header class="page-header">
      <h1>案例与参考</h1>
      <p>案例与参考分区不是单一链接列表，而是把主锚点案例、章节案例教学包、专题附录与核心外部入口组织在一起的公共入口。当前已形成“前四章以稳定经典案例为主、后四章逐步引入现代案例”的整体结构。</p>
    </header>

    <section>
      <h2 class="section-title">案例使用结构</h2>
      <ul class="feature-list">
        <li>前四章优先使用长期稳定、历史位置清楚的经典案例，用来承载历史、许可证、治理与基本工程机制。</li>
        <li>后四章再逐步引入 GitHub 原生、AI 原生和现代协作更强的项目案例，用来承载项目阅读、参与、AI 辅助与项目发布。</li>
        <li>案例必须承担解释功能，而不是只承担“点名功能”；不同案例在不同章节承担不同问题。</li>
        <li>参考入口按层组织：章节案例教学包、专题附录与书后工具材料、核心外部参考，不混成单一列表。</li>
      </ul>
    </section>

    <section>
      <h2 class="section-title">主锚点案例</h2>
      <div class="card-grid two">
        <article class="card">
          <h3>Linux / Linus</h3>
          <p>前四章主锚点案例。用于讲历史、GPL 传统、维护者体系、补丁生命周期、长期治理与工程连续性。</p>
        </article>
        <article class="card">
          <h3>OpenClaw / Peter</h3>
          <p>后四章主锚点案例。用于讲现代 AI 原生开源项目、GitHub 原生仓库结构、AI 工作流、安全与发布实践。</p>
        </article>
      </div>
    </section>

    <section>
      <h2 class="section-title">经典案例池</h2>
      <ul class="feature-list">
        <li>GNU / FSF：自由软件传统与制度问题的提出。</li>
        <li>Apache：社区化治理、PMC 结构与基于贡献积累信任的协作逻辑。</li>
        <li>Python：正式治理结构与利益边界约束。</li>
        <li>Git：分支模型与现代协作流程的技术基础。</li>
      </ul>
    </section>

    <section>
      <h2 class="section-title">当前已上线的案例教学包（第 1-4 章）</h2>
      <div class="card-grid two">
        {support_page_cards(CASE_PACK_PAGES)}
      </div>
    </section>

    <section>
      <h2 class="section-title">专题附录与书后工具材料</h2>
      <div class="card-grid two">
        {reference_cards}
      </div>
    </section>

    <section>
      <h2 class="section-title">核心外部参考入口</h2>
      <ul class="feature-list">
        <li><a href="https://www.gnu.org/philosophy/free-sw.html">FSF 自由软件定义</a></li>
        <li><a href="https://opensource.org/osd">OSI 开源定义</a></li>
        <li><a href="https://opensource.guide/">开源协作指南（Open Source Guides）</a></li>
        <li><a href="https://docs.github.com/">GitHub Docs</a></li>
        <li><a href="https://baseline.openssf.org/">OpenSSF OSPS Baseline</a></li>
        <li><a href="https://chaoss.community/">CHAOSS</a></li>
        <li><a href="https://openchainproject.org/">OpenChain</a></li>
        <li><a href="https://reuse.software/specifications/">REUSE Specification</a></li>
        <li><a href="https://spdx.dev/">SPDX</a></li>
      </ul>
    </section>

    <section class="status-note">
      当前页已能承担课程级案例与参考入口功能：前四章案例教学包已上线，专题附录与书后工具材料已接入；第 5-8 章案例教学包将在对应书稿与教学支持稳定后继续补充。
    </section>
    """
    write_page(
        "cases-references.html",
        page_shell(
            title="案例与参考",
            current_section="cases",
            hero_title="案例体系与核心参考",
            hero_text="案例分区负责承接课程中的高频主案例、章节重点案例与外部参考入口，帮助读者在经典与现代之间建立连接。",
            inner=inner,
        ),
    )


def build_manuscript_page(page: ManuscriptPage) -> None:
    title, body, toc = render_markdown(page.source)
    teaching_pages = teaching_pages_for_chapter(page.output)
    lab_pages = lab_pages_for_chapter(page.output)
    appendix_pages = appendix_pages_for_chapter(page.output)
    case_pages = case_pack_pages_for_chapter(page.output)
    companion_pages = support_pages_for_chapter(page.output)
    header = f"""
    <header class="page-header">
      <h1>{html.escape(title)}</h1>
      <p>{html.escape(page.description)}</p>
    </header>
    """
    teaching_note = ""
    if companion_pages:
        links = " · ".join(
            f'<a href="{companion_page.output}">{html.escape(companion_page.kind)}</a>'
            for companion_page in companion_pages
        )
        teaching_note = f"""
        <section class="status-note">
          <strong>同章配套材料：</strong> {links}
        </section>
        """
    meta = f"""
    <section class="meta">
      <p>源文件：<code>{html.escape(page.source.name)}</code></p>
    </section>
    """
    sidebar_parts = [
        f"""
        <div class="sidebar-block">
          <h2>书稿导航</h2>
          <ul class="nav-list">
            {manuscript_nav_html(page.output)}
          </ul>
        </div>
        """
    ]
    if teaching_pages or appendix_pages:
        teaching_items = "".join(
            f'<li><a href="{teaching_page.output}">{html.escape(teaching_page.kind)}</a></li>'
            for teaching_page in teaching_pages
        )
        teaching_items += "".join(
            f'<li><a href="{appendix_page.output}">{html.escape(appendix_page.kind)}</a></li>'
            for appendix_page in appendix_pages
        )
        sidebar_parts.append(
            f"""
            <div class="sidebar-block">
              <h3>配套教学支持</h3>
              <ul class="nav-list">
                {teaching_items}
              </ul>
            </div>
            """
        )
    if lab_pages or case_pages:
        related_items = "".join(
            f'<li><a href="{lab_page.output}">{html.escape(lab_page.kind)}</a></li>'
            for lab_page in lab_pages
        )
        related_items += "".join(
            f'<li><a href="{case_page.output}">{html.escape(case_page.kind)}</a></li>'
            for case_page in case_pages
        )
        sidebar_parts.append(
            f"""
            <div class="sidebar-block">
              <h3>实验与案例</h3>
              <ul class="nav-list">
                {related_items}
              </ul>
            </div>
            """
        )
    if toc and "<li>" in toc:
        sidebar_parts.append(
            f"""
            <div class="sidebar-block toc">
              <h3>本页目录</h3>
              {toc}
            </div>
            """
        )
    write_page(
        page.output,
        page_shell(
            title=title,
            current_section="manuscript",
            hero_title="书稿阅读页",
            hero_text="书稿分区用于稳定阅读正文。顶部是全站导航，左侧是书稿内部导航，页内目录用于长文定位。",
            inner=header + teaching_note + body + meta,
            sidebar_html="".join(sidebar_parts),
        ),
    )


def build_teaching_page(page: TeachingPage) -> None:
    page_title, body, toc = render_markdown(page.source)
    companion = manuscript_page_for_output(page.chapter_output)
    sibling_pages = [
        sibling
        for sibling in teaching_pages_for_chapter(page.chapter_output)
        if sibling.output != page.output
    ]
    companion_links = []
    if companion:
        companion_links.append(
            f'<a href="{companion.output}">对应书稿：{html.escape(companion.label)}</a>'
        )
    for sibling in sibling_pages:
        companion_links.append(
            f'<a href="{sibling.output}">同章配套：{html.escape(sibling.kind)}</a>'
        )
    for sibling in appendix_pages_for_chapter(page.chapter_output):
        companion_links.append(
            f'<a href="{sibling.output}">同章配套：{html.escape(sibling.kind)}</a>'
        )
    for sibling in lab_pages_for_chapter(page.chapter_output):
        companion_links.append(
            f'<a href="{sibling.output}">同章配套：{html.escape(sibling.kind)}</a>'
        )
    for sibling in case_pack_pages_for_chapter(page.chapter_output):
        companion_links.append(
            f'<a href="{sibling.output}">同章配套：{html.escape(sibling.kind)}</a>'
        )
    companion_note = ""
    if companion_links:
        companion_note = f"""
        <section class="status-note">
          <strong>配套入口：</strong> {' · '.join(companion_links)}
        </section>
        """
    header = f"""
    <header class="page-header">
      <h1>{html.escape(page_title)}</h1>
      <p>{html.escape(page.description)}</p>
    </header>
    """
    meta = f"""
    <section class="meta">
      <p>源文件：<code>{html.escape(page.source.name)}</code></p>
      <p>对应书稿章节：<a href="{page.chapter_output}">{html.escape(page.chapter_label)}</a></p>
    </section>
    """
    sidebar_parts = [
        f"""
        <div class="sidebar-block">
          <h2>教学支持导航</h2>
          <ul class="nav-list">
            {teaching_nav_html(page.output)}
          </ul>
        </div>
        """
    ]
    if companion:
        related_items = [
            f'<li><a href="{companion.output}">对应书稿</a></li>'
        ]
        for sibling in sibling_pages:
            related_items.append(
                f'<li><a href="{sibling.output}">{html.escape(sibling.kind)}</a></li>'
            )
        for sibling in appendix_pages_for_chapter(page.chapter_output):
            related_items.append(
                f'<li><a href="{sibling.output}">{html.escape(sibling.kind)}</a></li>'
            )
        for sibling in lab_pages_for_chapter(page.chapter_output):
            related_items.append(
                f'<li><a href="{sibling.output}">{html.escape(sibling.kind)}</a></li>'
            )
        for sibling in case_pack_pages_for_chapter(page.chapter_output):
            related_items.append(
                f'<li><a href="{sibling.output}">{html.escape(sibling.kind)}</a></li>'
            )
        sidebar_parts.append(
            f"""
            <div class="sidebar-block">
              <h3>同章配套</h3>
              <ul class="nav-list">
                {''.join(related_items)}
              </ul>
            </div>
            """
        )
    if toc and "<li>" in toc:
        sidebar_parts.append(
            f"""
            <div class="sidebar-block toc">
              <h3>本页目录</h3>
              {toc}
            </div>
            """
        )
    write_page(
        page.output,
        page_shell(
            title=page.label,
            current_section="teaching",
            hero_title=page.kind,
            hero_text="教学支持页用于承接与书稿配套的学习和教学支架，帮助课程层材料围绕同一章正文协同使用。",
            inner=header + companion_note + body + meta,
            sidebar_html="".join(sidebar_parts),
        ),
    )


def build_appendix_page(page: TeachingPage) -> None:
    page_title, body, toc = render_markdown(page.source)
    companion = manuscript_page_for_output(page.chapter_output)
    related = support_pages_for_chapter(page.chapter_output)
    header = f"""
    <header class="page-header">
      <h1>{html.escape(page_title)}</h1>
      <p>{html.escape(page.description)}</p>
    </header>
    """
    note_links = []
    if companion:
        note_links.append(f'<a href="{companion.output}">对应书稿</a>')
    for sibling in related:
        if sibling.output != page.output:
            note_links.append(f'<a href="{sibling.output}">{html.escape(sibling.kind)}</a>')
    companion_note = ""
    if note_links:
        companion_note = f"""
        <section class="status-note">
          <strong>同章配套：</strong> {' · '.join(note_links)}
        </section>
        """
    meta = f"""
    <section class="meta">
      <p>源文件：<code>{html.escape(page.source.name)}</code></p>
      <p>对应书稿章节：<a href="{page.chapter_output}">{html.escape(page.chapter_label)}</a></p>
    </section>
    """
    sidebar_parts = [
        f"""
        <div class="sidebar-block">
          <h2>附录支撑导航</h2>
          <ul class="nav-list">
            {appendix_nav_html(page.output)}
          </ul>
        </div>
        """
    ]
    if companion or related:
        related_items = []
        if companion:
            related_items.append(f'<li><a href="{companion.output}">对应书稿</a></li>')
        for sibling in related:
            if sibling.output != page.output:
                related_items.append(
                    f'<li><a href="{sibling.output}">{html.escape(sibling.kind)}</a></li>'
                )
        sidebar_parts.append(
            f"""
            <div class="sidebar-block">
              <h3>同章配套</h3>
              <ul class="nav-list">
                {''.join(related_items)}
              </ul>
            </div>
            """
        )
    if toc and "<li>" in toc:
        sidebar_parts.append(
            f"""
            <div class="sidebar-block toc">
              <h3>本页目录</h3>
              {toc}
            </div>
            """
        )
    write_page(
        page.output,
        page_shell(
            title=page.label,
            current_section="teaching",
            hero_title="附录支撑",
            hero_text="附录支撑页承接模板、清单、比较表和最小操作支架，帮助课程层材料真正可用而不挤占书稿正文。",
            inner=header + companion_note + body + meta,
            sidebar_html="".join(sidebar_parts),
        ),
    )


def build_lab_page(page: TeachingPage) -> None:
    page_title, body, toc = render_markdown(page.source)
    companion = manuscript_page_for_output(page.chapter_output)
    related = support_pages_for_chapter(page.chapter_output)
    header = f"""
    <header class="page-header">
      <h1>{html.escape(page_title)}</h1>
      <p>{html.escape(page.description)}</p>
    </header>
    """
    note_links = []
    if companion:
        note_links.append(f'<a href="{companion.output}">对应书稿</a>')
    for sibling in related:
        if sibling.output != page.output:
            note_links.append(f'<a href="{sibling.output}">{html.escape(sibling.kind)}</a>')
    companion_note = ""
    if note_links:
        companion_note = f"""
        <section class="status-note">
          <strong>同章配套：</strong> {' · '.join(note_links)}
        </section>
        """
    meta = f"""
    <section class="meta">
      <p>源文件：<code>{html.escape(page.source.name)}</code></p>
      <p>对应书稿章节：<a href="{page.chapter_output}">{html.escape(page.chapter_label)}</a></p>
    </section>
    """
    sidebar_parts = [
        f"""
        <div class="sidebar-block">
          <h2>实验材料导航</h2>
          <ul class="nav-list">
            {lab_nav_html(page.output)}
          </ul>
        </div>
        """
    ]
    if companion or related:
        related_items = []
        if companion:
            related_items.append(f'<li><a href="{companion.output}">对应书稿</a></li>')
        for sibling in related:
            if sibling.output != page.output:
                related_items.append(
                    f'<li><a href="{sibling.output}">{html.escape(sibling.kind)}</a></li>'
                )
        sidebar_parts.append(
            f"""
            <div class="sidebar-block">
              <h3>同章配套</h3>
              <ul class="nav-list">
                {''.join(related_items)}
              </ul>
            </div>
            """
        )
    if toc and "<li>" in toc:
        sidebar_parts.append(
            f"""
            <div class="sidebar-block toc">
              <h3>本页目录</h3>
              {toc}
            </div>
            """
        )
    write_page(
        page.output,
        page_shell(
            title=page.label,
            current_section="labs",
            hero_title="实验与项目材料",
            hero_text="章节级实验材料页用于把书稿与教学支持真正转化为团队项目任务、交付物、检查点和可评价证据。",
            inner=header + companion_note + body + meta,
            sidebar_html="".join(sidebar_parts),
        ),
    )


def build_case_pack_page(page: TeachingPage) -> None:
    page_title, body, toc = render_markdown(page.source)
    companion = manuscript_page_for_output(page.chapter_output)
    related = support_pages_for_chapter(page.chapter_output)
    header = f"""
    <header class="page-header">
      <h1>{html.escape(page_title)}</h1>
      <p>{html.escape(page.description)}</p>
    </header>
    """
    note_links = []
    if companion:
        note_links.append(f'<a href="{companion.output}">对应书稿</a>')
    for sibling in related:
        if sibling.output != page.output:
            note_links.append(f'<a href="{sibling.output}">{html.escape(sibling.kind)}</a>')
    companion_note = ""
    if note_links:
        companion_note = f"""
        <section class="status-note">
          <strong>同章配套：</strong> {' · '.join(note_links)}
        </section>
        """
    meta = f"""
    <section class="meta">
      <p>源文件：<code>{html.escape(page.source.name)}</code></p>
      <p>对应书稿章节：<a href="{page.chapter_output}">{html.escape(page.chapter_label)}</a></p>
    </section>
    """
    sidebar_parts = [
        f"""
        <div class="sidebar-block">
          <h2>案例教学包导航</h2>
          <ul class="nav-list">
            {case_pack_nav_html(page.output)}
          </ul>
        </div>
        """
    ]
    if companion or related:
        related_items = []
        if companion:
            related_items.append(f'<li><a href="{companion.output}">对应书稿</a></li>')
        for sibling in related:
            if sibling.output != page.output:
                related_items.append(
                    f'<li><a href="{sibling.output}">{html.escape(sibling.kind)}</a></li>'
                )
        sidebar_parts.append(
            f"""
            <div class="sidebar-block">
              <h3>同章配套</h3>
              <ul class="nav-list">
                {''.join(related_items)}
              </ul>
            </div>
            """
        )
    if toc and "<li>" in toc:
        sidebar_parts.append(
            f"""
            <div class="sidebar-block toc">
              <h3>本页目录</h3>
              {toc}
            </div>
            """
        )
    write_page(
        page.output,
        page_shell(
            title=page.label,
            current_section="cases",
            hero_title="案例教学包",
            hero_text="案例教学包页用于固定每章高频主案例、讨论问题、课堂使用方式与教学边界，避免案例使用漂移。",
            inner=header + companion_note + body + meta,
            sidebar_html="".join(sidebar_parts),
        ),
    )


def reset_site_dir() -> None:
    if SITE_DIR.exists():
        for path in sorted(SITE_DIR.rglob("*"), reverse=True):
            if path.is_file():
                path.unlink()
            elif path.is_dir():
                path.rmdir()
        SITE_DIR.rmdir()
    SITE_DIR.mkdir()
    ASSETS_DIR.mkdir()


def copy_public_assets() -> None:
    if not PUBLIC_ASSETS_DIR.exists():
        return
    for path in sorted(PUBLIC_ASSETS_DIR.rglob("*")):
        relative = path.relative_to(PUBLIC_ASSETS_DIR)
        destination = ASSETS_DIR / relative
        if path.is_dir():
            destination.mkdir(parents=True, exist_ok=True)
        else:
            destination.parent.mkdir(parents=True, exist_ok=True)
            shutil.copy2(path, destination)


def build_site() -> None:
    reset_site_dir()
    copy_public_assets()
    (ASSETS_DIR / "style.css").write_text(CSS.strip() + "\n", encoding="utf-8")
    (SITE_DIR / ".nojekyll").write_text("", encoding="utf-8")
    build_home()
    build_course_page()
    build_manuscript_index()
    build_teaching_index()
    build_labs_page()
    build_cases_page()
    for page in MANUSCRIPT_PAGES:
        build_manuscript_page(page)
    for page in TEACHING_PAGES:
        build_teaching_page(page)
    for page in APPENDIX_PAGES:
        build_appendix_page(page)
    for page in LAB_PAGES:
        build_lab_page(page)
    for page in CASE_PACK_PAGES:
        build_case_pack_page(page)


if __name__ == "__main__":
    build_site()

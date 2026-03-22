#!/usr/bin/env python3

from __future__ import annotations

from dataclasses import dataclass
from datetime import datetime, timezone
from pathlib import Path
import html
import re

import markdown


ROOT = Path(__file__).resolve().parents[1]
SITE_DIR = ROOT / "site"
ASSETS_DIR = SITE_DIR / "assets"


@dataclass(frozen=True)
class ManuscriptPage:
    label: str
    source: Path
    output: str
    description: str


@dataclass(frozen=True)
class Section:
    key: str
    label: str
    output: str
    description: str


SECTIONS = [
    Section("home", "首页", "index.html", "课程入口、核心分区和最近可读内容。"),
    Section("course", "课程说明", "course.html", "课程定位、结构、对象与学习路径。"),
    Section("manuscript", "书稿", "manuscript.html", "教材前言与各章书稿阅读入口。"),
    Section("labs", "实验与项目", "labs-project.html", "实践主线、实验阶段与团队项目。"),
    Section("cases", "案例与参考", "cases-references.html", "经典案例、现代案例与核心参考。"),
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
]

LINK_MAP = {str(page.source.name): page.output for page in MANUSCRIPT_PAGES}

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

.hero-meta {
  margin-top: 16px;
  display: flex;
  flex-wrap: wrap;
  gap: 10px;
}

.pill {
  display: inline-flex;
  align-items: center;
  gap: 6px;
  padding: 7px 11px;
  border-radius: 999px;
  border: 1px solid rgba(26, 90, 78, 0.14);
  background: rgba(255, 253, 247, 0.78);
  color: var(--accent-strong);
  font-size: 0.92rem;
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
            <span>Course Site + Manuscript Preview</span>
          </span>
        </a>
        <nav class="global-nav" aria-label="全站导航">
          {global_nav_html(current_section)}
        </nav>
      </div>
    </header>
    <div class="shell">
      <section class="hero panel">
        <div class="eyebrow">Open Source Software Development</div>
        <h1>{html.escape(hero_title)}</h1>
        <p>{html.escape(hero_text)}</p>
        <div class="hero-meta">
          <span class="pill">课程网站</span>
          <span class="pill">书稿阅读区</span>
          <span class="pill">GitHub Pages 自动构建</span>
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
            ("课程说明", "course.html", "课程定位、对象、结构与整体学习路径。"),
            ("书稿", "manuscript.html", "前言与第 1-4 章正文阅读入口。"),
            ("实验与项目", "labs-project.html", "团队项目主线、实验阶段与里程碑。"),
            ("案例与参考", "cases-references.html", "Linux、OpenClaw 与核心外部参考。"),
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
      <div class="card-grid two">
        {section_html}
      </div>
    </section>

    <section>
      <h2 class="section-title">当前可在线阅读的书稿</h2>
      <div class="card-grid two">
        {chapter_html}
      </div>
    </section>

    <section class="status-note">
      <strong>当前状态：</strong>课程网站已具备全站导航、书稿阅读区与实验/案例入口。当前上线内容优先覆盖第 1-4 章，后续章节与实验材料将继续增补。
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
    inner = """
    <header class="page-header">
      <h1>课程说明</h1>
      <p>本课程以“开源软件开发技术”为中心，而不是泛化的软件工程课或 AI 工具课。课程目标是帮助读者理解开源、进入开源，并开始按现代开源方式参与和开发项目。</p>
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
        <li>课程整体采用 baseline + stretch 结构，兼顾一般本科院校与能力更强的团队。</li>
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
      <h2 class="section-title">材料体系</h2>
      <ul class="feature-list">
        <li>Technical Book Manuscript：稳定核心知识与书稿正文。</li>
        <li>Student Study Guide / Instructor Guide：教学支持层。</li>
        <li>Lab / Project Materials：实验与团队项目材料。</li>
        <li>Case Library：案例库与项目证据。</li>
      </ul>
    </section>

    <section class="status-note">
      课程层页面用于说明整体结构和使用方式；真正的长文阅读，请进入“书稿”分区。
    </section>
    """
    write_page(
        "course.html",
        page_shell(
            title="课程说明",
            current_section="course",
            hero_title="课程定位与整体结构",
            hero_text="课程层页面负责说明课程目标、对象、结构和材料体系，帮助读者先看清课程系统，再进入具体书稿与实验。",
            inner=inner,
        ),
    )


def build_manuscript_index() -> None:
    inner = f"""
    <header class="page-header">
      <h1>书稿目录</h1>
      <p>这里集中展示教材前言与各章正文。阅读页使用统一的章节导航与页内目录，便于连续阅读与横向比较。</p>
    </header>

    <section>
      <div class="card-grid two">
        {section_cards([(page.label, page.output, page.description) for page in MANUSCRIPT_PAGES])}
      </div>
    </section>

    <section class="status-note">
      当前在线书稿范围：第 1-4 章。第 5-8 章将在后续章节重写完成后接入。
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
            hero_text="书稿分区采用 docs-first 阅读结构。首页提供目录，章节页提供左侧章节导航与页内目录。",
            inner=inner,
            sidebar_html=sidebar,
        ),
    )


def build_labs_page() -> None:
    stage_cards = section_cards(
        [
            ("实验 1-2", "manuscript.html", "开源观察与项目阅读；团队项目立项与许可证选择。"),
            ("实验 3-4", "chapter-03.html", "治理基线与协作机制建立；GitHub 协作流与最小 CI。"),
            ("实验 5-6", "chapter-04.html", "外部项目理解或首次贡献；团队项目 MVP 迭代。"),
            ("实验 7-8", "manuscript.html", "AI 辅助开发与人工治理；最终发布、演示与复盘。"),
        ]
    )
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
      <h2 class="section-title">实验阶段</h2>
      <div class="card-grid two">
        {stage_cards}
      </div>
    </section>

    <section class="status-note">
      当前站点先展示实验结构与入口说明；后续可继续扩展为详细实验页、rubric、阶段交付模板与样例。
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
    inner = """
    <header class="page-header">
      <h1>案例与参考</h1>
      <p>课程采用“经典主案例 + 后半部现代案例 + 辅助案例库”的结构。前四章以经典开源项目为主，后续章节再逐步引入 AI-native、GitHub-native 的现代项目。</p>
    </header>

    <section>
      <h2 class="section-title">主案例</h2>
      <div class="card-grid two">
        <article class="card">
          <h3>Linux / Linus</h3>
          <p>前半部主锚点案例。用于讲历史、GPL 传统、维护者体系、补丁生命周期与长期治理。</p>
        </article>
        <article class="card">
          <h3>OpenClaw / Peter</h3>
          <p>后半部主锚点案例。用于讲现代 AI-native 开源项目、GitHub-native 仓库结构、安全与发布实践。</p>
        </article>
      </div>
    </section>

    <section>
      <h2 class="section-title">经典案例池</h2>
      <ul class="feature-list">
        <li>GNU / FSF：自由软件传统与制度问题的提出。</li>
        <li>Apache：社区化治理、PMC 结构与 meritocracy。</li>
        <li>Python：正式治理结构与利益边界约束。</li>
        <li>Git：branching model 与现代协作流程的技术基础。</li>
      </ul>
    </section>

    <section>
      <h2 class="section-title">核心外部参考</h2>
      <ul class="feature-list">
        <li><a href="https://www.gnu.org/philosophy/free-sw.html">FSF Free Software Definition</a></li>
        <li><a href="https://opensource.org/osd">OSI Open Source Definition</a></li>
        <li><a href="https://opensource.guide/">Open Source Guides</a></li>
        <li><a href="https://docs.github.com/">GitHub Docs</a></li>
        <li><a href="https://baseline.openssf.org/">OpenSSF OSPS Baseline</a></li>
        <li><a href="https://chaoss.community/">CHAOSS</a></li>
      </ul>
    </section>

    <section class="status-note">
      当前页先作为案例与参考入口页。后续可以继续扩展为独立案例页、对照阅读页与参考文献分层浏览。
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
    header = f"""
    <header class="page-header">
      <h1>{html.escape(title)}</h1>
      <p>{html.escape(page.description)}</p>
    </header>
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
            inner=header + body + meta,
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


def build_site() -> None:
    reset_site_dir()
    (ASSETS_DIR / "style.css").write_text(CSS.strip() + "\n", encoding="utf-8")
    (SITE_DIR / ".nojekyll").write_text("", encoding="utf-8")
    build_home()
    build_course_page()
    build_manuscript_index()
    build_labs_page()
    build_cases_page()
    for page in MANUSCRIPT_PAGES:
        build_manuscript_page(page)


if __name__ == "__main__":
    build_site()

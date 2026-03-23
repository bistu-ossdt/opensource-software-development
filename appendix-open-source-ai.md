# 附录 开源人工智能

这一附录不是一章压缩版正文，而是一份专题索引。它的任务不是完整论证“什么是开源人工智能”，而是帮助读者快速建立一张代表性图景：这一领域是怎样形成的，哪些事件最值得记住，哪些人物和组织在推动它，哪些模型、系统、框架与基础设施最有代表性。

需要特别说明的是：`Open Source AI` 作为术语与正式定义都很新。Open Source Initiative 在 `2024-10-28` 才发布 `Open Source AI Definition 1.0`。因此，本附录不使用“完整历史”这种口径，而使用“代表事件”这一更克制的组织方式。截至 `2026-03-23`，这里优先收录已经足以帮助读者理解领域结构的关键节点，而不追求把所有最新项目都列入。与此同时，这份附录的重点是近年促成 `OSAID` 形成的模型、数据、框架与基础设施对象，而不是试图覆盖整个人工智能发展史。

本附录采用“核心严格，外围分层”的边界原则：

- 核心部分严格服从 OSI 对 `Open Source AI` 的定义
- 代表事件、人物、组织与对象优先选择直接参与 `OSAID` 形成或直接影响其判断边界的对象
- 相邻生态可以少量出现，但只作为背景，不与核心定义对象混写

## 1. 使用方式

正文与本附录的分工如下：

| 部分 | 主要任务 |
| --- | --- |
| 正文书稿 | 解释定义、组成、边界与参与方法 |
| 本附录 | 展示代表事件、代表人物、代表组织与代表性对象 |

阅读建议如下：

- 想准确理解 `Open Source AI` 的定义，应以正文和 OSI 定义原文为准。
- 想快速把“人、组织、对象、事件”连成一张图，可先看本附录。
- 想判断某个模型或系统到底更接近“开源人工智能”还是“开放权重”，应同时回看正文中的定义部分与本附录中的对象表。

## 2. 定义锚点

虽然本附录不承担正文式展开，但仍需给出最小定义锚点，以免后面的代表对象失去判断标准。

| 项目 | OSI 当前口径 |
| --- | --- |
| 定义覆盖对象 | 对 `AI system`、模型、权重与参数采用同一开源要求，不把“只有权重”单独视为充分条件 |
| 四项自由 | `Use` / `Study` / `Modify` / `Share` |
| 机器学习系统的“可修改首选形式” | 至少包括 `Data Information`、`Code`、`Parameters` |
| 对模型与权重等组成部分的判断 | 不能只看是否可下载，还要看是否连同必要的数据说明与代码一起支持四项自由 |
| 与 `Open Weights` 的关系 | `Open Weights` 不等于 `Open Source AI` |
| Checklist 的地位 | 主要用于理解定义与开展自查，不应被理解为 OSI 的正式认证机制 |

对本附录而言，最重要的不是复述定义全文，而是记住三点：

- `Open Source AI` 的判断不能缩减成“权重是否开放”这一件事。
- OSI 并不把模型、权重和参数排除在外，而是要求它们和系统一样满足同一组开放条件。
- 很多公众语境里的“开源模型”，按 OSI 口径其实更接近 `Open Weights`。
- 围绕这些模型运转的更广生态当然重要，但它们在本附录里只作为分层背景出现，而不替代核心定义对象。

## 3. 代表事件

下表选择的不是“所有新闻”，而是对理解开源人工智能形成过程最有帮助、且可以落到具体公告、发布或会议节点上的代表事件。

| 时间 | 代表事件 | 为什么重要 | 代表对象 / 组织 |
| --- | --- | --- | --- |
| `2021-08-20` | `LAION-400M` 发布 | 大规模开放图文数据集把“数据层”问题推到台前，提醒人们开源人工智能不只关心模型权重，也必须面对数据来源、再分发和清洗问题。 | LAION |
| `2022-07` | `BLOOM` 正式发布 | `BLOOM` 展示了跨机构、跨国家的大模型开放协作路径，也让“开放大模型”真正进入全球公共讨论空间。 | BigScience、Hugging Face、BLOOM |
| `2023-04-03` | `Pythia` 发布修订版模型套件 | `Pythia` 以公开模型、数据、代码和大量中间检查点强调可重复研究，成为“真正开放到什么程度”讨论中的代表对象。 | EleutherAI、Pythia |
| `2023-06` | OSAID 第一次正式会议召开 | 这是 OSI 将“如何定义开源人工智能”转化为公开协作过程的重要起点。 | OSI 及其合作方 |
| `2024-02-01` | Ai2 发布 `OLMo` | `OLMo` 把“fully open”从口号推进到更完整的实践示范，强调数据、训练代码、评测和模型工件都应开放。 | Ai2、OLMo |
| `2024-03-21` | `Model Openness Framework` 论文发布 | 这项工作为“组件是否足够完整”提供了分析框架，也成为 OSI Checklist 的重要参考。 | MOF |
| `2024-05-06` | OSAID 进入 validation phase | OSI 开始邀请志愿者用草案去评估现实中的 AI 系统，这一阶段直接促成了后来的 FAQ 案例集合。 | OSI、OSAID |
| `2024-10-10` 至 `2024-10-11` | 巴黎训练数据工作坊举行 | 这说明“开源人工智能”的核心争议已明确落在训练数据设计、许可、治理与可获得性上，而不只是模型权重是否公开。 | OSI、训练数据工作坊 |
| `2024-10-28` | `Open Source AI Definition 1.0` 正式发布 | 这是当前最关键的制度节点。自此以后，讨论“开源人工智能”有了一个可引用、可争论、可比较的正式定义。 | OSI、OSAID 1.0 |
| `2025-05-07` | PyTorch Foundation 扩展为 umbrella foundation，并接纳 `vLLM`、`DeepSpeed` | 表明开源人工智能已不再只是单个模型之争，而进入训练、推理、部署、工具链共同构成的基础设施阶段。 | PyTorch Foundation、vLLM、DeepSpeed |

## 4. 代表人物

这里的人物不是“名人榜”，而是帮助读者理解不同推动力量：有人推动定义，有人建设平台，有人建设数据与模型，有人建设基础设施。

| 人物 | 代表位置 | 代表组织 / 项目 | 为什么值得知道 |
| --- | --- | --- | --- |
| Stefano Maffulli | 定义与制度推动者 | OSI、OSAID | 作为 OSI 关键推动者之一，他所代表的是“把开源人工智能从口号推进到正式定义”的制度工作。 |
| Mer Joyce | 定义协作过程的组织者 | OSAID co-design process | 她代表的是这一新定义如何通过公开、全球、多方参与的方式被组织出来。 |
| Clément Delangue | 平台与分发生态代表人物 | Hugging Face | Hugging Face 之所以重要，不只是托管模型，更在于它成为模型、数据集、文档、评测和社区讨论的核心平台之一。 |
| Thomas Wolf | 开放 AI 研究与工具链传播者 | Hugging Face | 在公众和开发者语境里，他是推动开放模型与开放工具链话语的重要人物之一。 |
| Stella Biderman | 社区驱动的开放模型研究代表人物 | EleutherAI、Pythia | `Pythia` 所代表的，是把可重复研究、开放检查点和训练过程分析作为核心目标的路径。 |
| Ali Farhadi | “fully open” 模型路线代表人物 | Ai2、OLMo | Ai2 在 `OLMo` 路线上的推进，使“完整公开模型流”成为现实可见的研究与工程方向。 |
| Christoph Schuhmann | 开放数据共同体代表人物 | LAION | 围绕 LAION 的实践与争议提醒读者：数据层既是开放的基础，也是最复杂的边界地带。 |

本节的人物选择强调“代表性角色”，而不是完整性。随着本书后续附录与正文发展，这份名单还可以继续补充。

## 5. 代表组织

如果说人物帮助理解“谁在推动”，那么组织帮助理解“在哪些结构里推动”。按照“核心严格，外围分层”的原则，这里把组织分成定义核心层与生态支撑层两组。

### 5.1 定义与制度组织

| 组织 | 主要位置 | 代表性说明 |
| --- | --- | --- |
| Open Source Initiative (`OSI`) | 定义与制度 | 当前 `Open Source AI Definition` 的权威发布者，也是区分 `Open Source AI` 与 `Open Weights` 的核心组织载体。 |

### 5.2 生态与基础设施组织

| 组织 / 共同体 | 主要位置 | 代表性说明 |
| --- | --- | --- |
| Hugging Face | 平台与工具链 | 既是模型与数据集的重要分发平台，也是 `Transformers`、`Datasets`、`TGI`、`smolagents` 等开源工具链的重要组织者。 |
| EleutherAI | 社区研究共同体 | 代表了“社区驱动的开放模型研究”路线，`Pythia` 等项目强化了可重复性与训练过程透明的重要性。 |
| Ai2 | fully open 模型与数据路线 | 通过 `OLMo`、`Dolma`、`OLMoTrace` 等工作，把“真正开放的模型流”做成了连续路线而不是单点项目。 |
| BigScience | 大规模开放协作共同体 | `BLOOM` 让跨机构、跨语种、跨国家的开放大模型协作具备了鲜明示范意义。 |
| LAION | 开放数据共同体 | 在开放数据集、视觉-语言数据和数据争议处理上都具有代表性。 |
| PyTorch Foundation | 训练与推理基础设施组织 | 代表开源人工智能已经进入由训练、推理、部署与工具链共同构成的基础设施阶段。 |
| LF AI & Data | 基金会化生态载体 | 代表大型 AI / Data 开源项目如何在中立基金会结构下长期协作。 |
| MLCommons | 评测、标准与数据 | 代表“没有开放评测和标准，就没有稳定生态”的另一条主线。 |

## 6. 代表性对象

### 6.1 与 OSAID 关系最有代表性的模型 / 系统

这一部分最重要。它帮助读者把“什么是 Open Source AI”落到具体对象上，同时看到“开放权重”和“开源人工智能”之间的差异。

需要注意：以下分组主要依据 OSI FAQ 中提到的 validation phase 结果。OSI 同时明确说明，这些结果用于定义过程中的学习，不构成正式认证。

#### 6.1.1 通过 validation phase 的代表对象

| 对象 | 类型 | 为什么有代表性 |
| --- | --- | --- |
| `Pythia` | 模型套件 / 研究系统 | 代表“可重复研究导向”的开放路径：模型、数据、代码与大量中间检查点都被公开。 |
| `OLMo` | 语言模型 / 完整模型流 | 代表“fully open” 路线，即不仅开放权重，还强调训练数据、代码与评测工件。 |
| `Amber` | 语言模型 | 代表 `LLM360` 路线中对完整训练信息与中间工件的重视。 |
| `CrystalCoder` | 代码 / 文本模型 | 与 `Amber` 一起说明代码模型也可以进入更完整开放的实践。 |
| `T5` | 模型 | 说明开源人工智能讨论并不只针对大语言模型热潮之后的新对象。 |

#### 6.1.2 接近通过、但仍存在制度边界问题的对象

| 对象 | 类型 | 为什么有代表性 |
| --- | --- | --- |
| `BLOOM` | 大语言模型 | 代表“大规模开放协作”的里程碑，也提醒读者：开放协作并不自动等于已满足 OSAID。 |
| `StarCoder2` | 代码模型 | 说明很多看上去很开放的对象，最后卡在法律条款与发布条件上。 |
| `Falcon` | 大语言模型 | 代表“技术上很开放，但制度边界未完全到位”的一类对象。 |

#### 6.1.3 常被称为“开源”，但按 OSAID 不通过的对象

| 对象 | 类型 | 为什么有代表性 |
| --- | --- | --- |
| `Llama 2` | 开放权重大模型 | 它是区分 `Open Weights` 与 `Open Source AI` 的最常见公共案例之一。 |
| `Mixtral` | 开放权重大模型 | 代表“公众常称为开源，但按 OSAID 仍不足”的另一类典型对象。 |

### 6.2 构成开源人工智能生态的软件与基础设施对象

如果上一张表解决的是“哪些对象最能帮助判断定义边界”，那么这一张表解决的是“这个生态实际靠什么运转”。它们不等于某个完整的 `Open Source AI system`，但它们是现代开源人工智能不可缺少的组成部分。

| 对象 | 类型 | 在生态中的位置 | 为什么有代表性 |
| --- | --- | --- | --- |
| `PyTorch` | 训练框架 | 训练与研究基础设施 | 它是现代开源 AI 训练和研究生态中最核心的开源框架之一。 |
| `Transformers` | 模型开发与调用库 | 模型使用与分发入口 | 它极大降低了模型复用、微调与对比实验的门槛。 |
| `Datasets` | 数据集工具链 | 数据访问与处理 | 它让“数据也是核心对象”这一事实在工程上变得更清楚。 |
| `vLLM` | 推理与服务引擎 | 高吞吐 LLM serving | 代表推理层已经成为开源人工智能生态中的独立基础设施。 |
| `DeepSpeed` | 训练 / 推理优化系统 | 大模型训练与部署优化 | 代表训练、推理与系统优化不再是附属问题，而是生态主轴之一。 |
| `TGI` (`Text Generation Inference`) | 推理服务系统 | 模型部署与 API 服务 | 代表平台化推理服务在开源 AI 实践中的重要地位。 |
| `MLPerf` | 开放评测体系 | 基准测试与透明比较 | 代表评测与标准在开源人工智能生态中的独立位置，也提醒读者“开放对象”之外还存在“开放评测方法”这一层。 |

## 7. 如何使用这一附录理解“代表性图景”

如果只看大模型名称，读者很容易误以为开源人工智能只是“谁开放了一个模型”。但从本附录可以看到，这一专题至少可以从几层代表性结构来理解：

- 有定义层：由 OSI 等组织推动概念澄清；
- 有研究层：由 Pythia、OLMo、BLOOM 一类对象推动“更完整开放”；
- 有平台与基础设施层：由 Hugging Face、PyTorch、vLLM、DeepSpeed、TGI 等工具链支撑；
- 有评测与标准层：由 MLCommons / MLPerf 一类对象支撑可比较、可复核的生态基础。

因此，“开源人工智能”不是一个单点对象，而是一张由定义、数据、代码、参数、平台、基础设施、评测与共同体共同组成的系统图。

## 8. 本附录的主要编写依据

本附录优先使用 OSI、项目官方站点、官方博客、官方组织页面与项目官方仓库作为主要依据，并使用 Wikipedia 进行背景交叉校对。重点来源如下：

- Open Source Initiative, Open Source AI  
  https://opensource.org/ai
- Open Source AI Definition 1.0  
  https://opensource.org/ai/open-source-ai-definition
- OSAID FAQ  
  https://opensource.org/ai/faq
- OSAID Checklist  
  https://opensource.org/ai/checklist
- OSAID Timeline  
  https://opensource.org/ai/timeline
- Open Weights  
  https://opensource.org/ai/open-weights
- OSI release announcement for OSAID 1.0  
  https://opensource.org/blog/the-open-source-initiative-announces-the-release-of-the-industrys-first-open-source-ai-definition
- Wikipedia, Open-source artificial intelligence  
  https://en.wikipedia.org/wiki/Open-source_artificial_intelligence
- BigScience / BLOOM official release  
  https://bigscience.huggingface.co/blog/bloom
- EleutherAI Pythia official repository  
  https://github.com/EleutherAI/pythia
- Ai2 OLMo  
  https://allenai.org/olmo  
  https://allenai.org/blog/olmo-open-language-model-87ccfc95f580
- PyTorch Foundation  
  https://pytorch.org/foundation/
- PyTorch Foundation welcomes vLLM and DeepSpeed  
  https://pytorch.org/blog/press-release-pytorch-foundation-expands-welcomes-projects-vllm-deepspeed/
- vLLM official site  
  https://vllm.ai/
- MLCommons  
  https://mlcommons.org/
- MLPerf Client benchmark  
  https://mlcommons.org/benchmarks/client/

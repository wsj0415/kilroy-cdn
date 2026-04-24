# Akshay Pachaar — 如何构建开源 Deep Researcher 系统

**来源**: https://x.com/akshay_pachaar/status/2047395420935229724  
**作者**: Akshay 🚀 (@akshay_pachaar)  
**抓取时间**: 2026-04-24 00:31 UTC  
**类型**: X 推文线程/深度技术文章  
**标签**: deep-research, onyx, crewai, voxtral, open-source-ai, self-hosted-ai, mcp-integration, research-stack

---

## 📊 一句话总结

Akshay 分享 100% 开源可自托管的 Deep Research 栈（Onyx+CrewAI+Voxtral），在 DeepResearch Bench 学术基准测试中击败 OpenAI/Gemini/Perplexity，通过三阶段分离（Researcher/Analyst/Report Writer）+MCP 集成+原生语音层，实现数据完全主权+无妥协的研究质量。

**English**: Akshay shares 100% open-source self-hostable Deep Research stack (Onyx+CrewAI+Voxtral), beats OpenAI/Gemini/Perplexity on DeepResearch Bench academic benchmark, through 3-stage separation (Researcher/Analyst/Report Writer)+MCP integration+native audio layer, achieving full data sovereignty+no-compromise research quality.

---

## 🏷️ 话题标签

#DeepResearch #Onyx #CrewAI #Voxtral #开源 AI #自托管 AI #MCP 集成 #研究栈

---

## 🎨 封面图提示词（nano-banana-pro 技能库）

### 选项 1：Deep Research 三阶段架构图 ⭐ 推荐

**来源**: nano-banana-pro / Infographic / Edu Visual  
**参考 ID**: 11165 (Technical Infographic Cutaway)  
**示例图**: https://cms-assets.youmind.com/media/1772433492844_q6zr64_HCTasgQaYAADK5w.jpg

```prompt
Deep Research Stack Architecture diagram showing 3-stage Flow.

Layout: Horizontal 3-stage flow with Onyx + CrewAI + Voxtral.

Color Palette:
- Onyx: Blue (#3B82F6)
- CrewAI: Purple (#8B5CF6)
- Voxtral: Green (#10B981)
- Background: Dark gradient

Stage 1 — Onyx (Retrieval) 🔵:
图标：搜索 + 知识库
"Open-source AI platform"
"RAG + Web Search + Code Execution"
"40+ enterprise connectors"
"Slack/Confluence/Jira/GitHub"
"Self-hosted, data never leaves"
"Hybrid index: Vector + BM-25"
"Reciprocal Rank Fusion"

Stage 2 — CrewAI (Orchestration) 🟣:
图标：三 Agent Flow
"Researcher Agent:"
"Search web + documents via MCP"
"Every finding carries citation"
"Analyst Agent:"
"Deduplicate / Merge / Flag contradictions"
"Group into coherent themes"
"Report Writer Agent:"
"Structured Markdown report"
"SKILL.md injected at runtime"

Stage 3 — Voxtral (Voice) 🟢:
图标：语音输入 + 输出
"Mistral native audio model"
"Speech understanding + generation"
"Voice input: Speak question"
"Report narration: Expressive TTS"
"Accurate across accents/noise"

Bottom Full Flow:
"1. Type/Speak/Upload PDF query"
"2. Researcher searches via Onyx MCP"
"3. Analyst deduplicates + flags contradictions"
"4. Report Writer produces citation-backed Markdown"
"5. Click 'Play Report' for Voxtral narration"

Benchmark Badge:
"DeepResearch Bench #1"
"Beats OpenAI/Gemini/Perplexity"
"100 PhD tasks across 22 fields"

Style: Clean technical architecture, dark mode with stage colors
Aspect ratio: 9:16 portrait
```

**为什么选这个风格**: 这是关于 Deep Research 三阶段架构的内容，水平流程图直接展示 Onyx/CrewAI/Voxtral 如何协同工作，比单一架构图更能传达"开源替代方案"的价值。

---

### 选项 2：封闭 vs 开源对比图

**来源**: nano-banana-pro / Infographic / Edu Visual  
**参考 ID**: 11257 (Infographic Style)  
**示例图**: https://cms-assets.youmind.com/media/1772433527626_7jezbj_HCW2O1lX0AEnqu0.jpg

```prompt
Closed-Source vs Open-Source Deep Research comparison diagram.

Layout: Side-by-side comparison.

Color Palette:
- Closed-Source: Red/gray tones
- Open-Source: Green/blue tones
- Background: Dark gradient

Left — Closed-Source (ChatGPT/Gemini/Perplexity) 🔴:
图标：云 SaaS
"Queries go to their servers"
"Questions reveal what you're working on"
"Connected data indexed on their infrastructure"
"Retention/logging/audit = their call"
"Quotas/pricing change on their timeline"
"Enterprise tiers soften but don't eliminate"
"Data sovereignty = out of reach"

Right — Open-Source (Onyx+CrewAI+Voxtral) 🟢:
图标：自托管基础设施
"Fully self-hostable"
"Data never leaves your infrastructure"
"Pre-index everything on your infra"
"Permissions sync automatically"
"No internal data leaves your network"
"Open-source code you can audit"
"Modify and extend as needed"

Center — 5 Research Principles:
"1. Separation of stages (hard walls)"
"2. Retrieval that reasons (multi-query + LLM selection)"
"3. Reflection in loop (pivot on findings)"
"4. Unified search (public + internal)"
"5. Voice layer (speak + listen)"

Bottom Benchmark:
"DeepResearch Bench #1"
"100 PhD tasks / 22 fields"
"Report quality + citation accuracy"

Style: Modern comparison, dark mode with closed/open colors
Aspect ratio: 9:16 portrait
```

---

### 选项 3：5 研究原则网格

**来源**: nano-banana-pro / Social Media Post  
**参考 ID**: 6847 (Premium liquid glass Bento grid)  
**示例图**: https://cms-assets.youmind.com/media/1768962051381_l9uih4_537980579-6f29d32a-c786-40c4-bd5a-79c640737496.png

```prompt
Create a premium liquid glass Bento grid with 6 modules showing "5 Deep Research Principles".

Color Palette:
- Primary: Blue (#3B82F6)
- Accent: Various principle colors
- Cards: Apple liquid glass (85-90% transparent)
- Background: Ethereal abstract glow, dark gradient

Module Content (6 Cards):

M1 — Hero:
"Deep Research Principles"
"5 Things That Matter"
"Regardless of tools"
Icon: Research + Brain

M2 — Stage Separation:
"Hard walls between:"
"Gathering → Analysis → Writing"
"Each stage gets clean output"
"No accumulated context"
"Prevents 'deep frying' facts"

M3 — Reasoning Retrieval:
"Keyword search = brittle"
"Vector = breaks on multi-hop"
"Need: Parallel query variants"
"Intelligent recombination"
"LLM selection before synthesis"

M4 — Reflection Loop:
"Static plans don't survive"
"Pivot when unexpected surfaces"
"Track coverage of original plan"
"Structured output:"
"Covered / Gaps / New directions"

M5 — Unified Search:
"Public web + Internal sources"
"One pipeline"
"Permissions per-document"
"Indexing on your infra"
"Data sovereignty"

M6 — Voice Layer:
"Speaking > typing for queries"
"Listening > reading for reports"
"Voxtral: Native audio model"
"Accurate across accents/noise"
"Expressive narration"

Output: 1 image, 9:16 portrait, ultra-premium liquid glass infographic.
```

---

## 核心洞察

### 为什么需要开源 Deep Research

> **如果你今天需要 AI 做研究，你可能在用 ChatGPT Deep Research/Claude/Perplexity。三者都确实有能力。三者也都是闭源 SaaS 运行在别人的云端。**

**真正后果**:
- 你发送的每个查询都在他们服务器上
- 你连接的内部数据在他们基础设施上索引
- 保留/日志/审计由他们决定，非你
- 配额和定价按他们的时间表变更

> **对于受监管行业/IP 敏感工作/数据驻留规则下的团队，那列表不是理论。是 AI 辅助研究仍感觉够不着很多严肃工作的原因。**

---

### 研究失败的常见模式

> **大多数研究工具只做一次传递。它们搜索/收集任何返回的东西，交给 LLM 写东西。这对浅查询有效。在你问需要跨来源综合/矛盾检测/多跳推理的问题时就破裂。**

**实际失败样子**:
1. Agent 找到一个来源和一个矛盾来源。选一个继续。矛盾从未浮现。
2. 两个来源用不同词说同样事。报告引用两者为独立证据。
3. 关键连接事实在未检索到的文档中，因为关键词匹配不理解"云迁移"和"把 PostgreSQL 集群搬到 AWS"是一回事。

> **这些不是边缘案例。它们是真实研究问题的正常形状。它们都共享同根因：研究不是一个任务。**

---

## 5 个研究原则

### 原则 1: 阶段分离

> **收集/分析/写作之间的硬墙。每个阶段只获得前一阶段的干净输出。**

**反模式**: 一个 Agent 带三个顺序任务共享增长的上下文窗口
- 作者在分析师完成前开始
- 原始搜索噪音渗入最终报告
- 源材料在输出前被重新解释两次

---

### 原则 2: 推理检索

> **关键词搜索脆弱。向量相似度在多跳上破裂。你需要并行查询变体/智能重组/LLM 选择步骤在综合前。跳过最后一步幻觉进入。**

**Onyx 的 6 步检索流程**:
1. **查询生成**: 并行查询（语义重写/关键词变体/广泛搜索），多部分问题自动拆分
2. **搜索和重组**: 混合索引（vector + BM-25），通过 Reciprocal Rank Fusion 重组，相邻块合并
3. **LLM 选择**: LLM 审查所有块只保留相关的。**跳过这是幻觉进入的地方**
4. **上下文扩展**: 对每个选中文档，LLM 阅读周围块决定上下文大小（每文档并行）
5. **提示构建**: 选中部分与引用和聊天历史组装
6. **答案综合**: 带内联引用的接地答案

---

### 原则 3: 循环中反射

> **静态计划无法在与发现接触后存活。系统应在意外浮现时 pivoting，同时追踪原始计划的覆盖。**

**Onyx 的强制反射步骤**（每次调度前运行）:
- 什么已覆盖
- 什么差距剩余
- 什么新方向出现
- 是否更多周期会产生新信息

> **每次都运行。结果表现得像研究员，非检索引擎。**

---

### 原则 4: 统一搜索

> **研究层需要在单一管道中查询开放网络和内部知识，每文档执行权限。**

**Onyx 连接 40+ 企业数据源**:
Slack / Confluence / Jira / GitHub / Salesforce / Google Drive / SharePoint / Notion / Zendesk / HubSpot / Gong / 更多

**关键区别**:
> **与专有工具的区别不是能否连接。是索引发生在哪里。Onyx 在你的基础设施上持续预索引一切，近实时同步内容/元数据/权限。**

**你得到什么**:
- 一个查询跨越开放网络和每个内部来源
- 用户只看到他们有权查看的文档结果
- 权限从每个来源自动同步
- 无内部数据离开你的网络被供应商标索引/存储

---

### 原则 5: 语音层

> **语音在 AI 工具中通常是附加：Whisper 包装器用于输入，基础 TTS 用于输出，每方向不同模型无连贯设计。**

**Voxtral 不同**: Mistral 的原生音频模型家族，从头构建用于语音理解和生成，同一家族处理双向：
- 转录在口音/背景噪音/领域词汇上保持准确
- 叙述听起来自然，非机器人

**研究体验的两个改变**:
1. **语音输入**: 说话而非打字问题。转录直接流入管道
2. **报告叙述**: 完整 Markdown 报告作为富有表现力语音读回。听长报告胜过屏幕阅读

---

## Onyx 架构

### DeepResearch Bench 基准测试

> **Onyx 提交到 DeepResearch Bench，独立学术基准覆盖 100 个博士级研究任务跨 22 个领域，评估报告质量和引用准确性。**

**结果**: **#1 排名**，领先 OpenAI Deep Research / Gemini 2.5 Pro / Perplexity Deep Research

**团队提示哲学**:
> **"Prefer being thorough in research over being helpful."**（研究彻底胜过讨好）

---

### 三阶段执行流程

**Phase 1: Clarification（澄清）**
- 对短/模糊查询最多 5 个针对性问题
- 详细查询自动跳过

**Phase 2: Planning（规划）**
- 将查询分解为最多 6 个探索方向
- **关键选择**: 规划器无工具访问，所以产生计划，非答案

**Phase 3: Iterative Execution（迭代执行）**
- Orchestrator 和 Research Agent 交替最多 8 周期
- 每周期并行调度最多 3 个 Agent

**关键分离**:
- Orchestrator 从不直接搜索
- Research Agent 从不看完整查询或计划
- **这强制自包含任务简报，防止上下文泄漏**

---

## CrewAI 集成

### 三 Agent Flow

```python
from crewai import Agent

researcher_agent = Agent(
    role="Senior Research Analyst",
    goal="Gather information on research query with source URLs",
    backstory="You are a disciplined analyst. Record every source URL.",
    mcps=[
        f"{ONYX_MCP_URL}?token={ONYX_TOKEN}"
    ]
)
```

**Researcher Agent 立即获得三个工具**:
- 搜索知识库
- 搜索网络
- 从任何 URL 获取完整页面内容

**无需手动工具接线**。Schema 缓存，连接按需，服务器不可达时优雅失败。

---

### SKILL.md 系统

```
deep-research-report/
├── SKILL.md       # Formatting rules, evidence standards, structure
├── scripts/       # Optional
└── references/    # Optional
```

**SKILL.md 结构**:
```markdown
---
name: deep-research-report
description: >
  Guidelines for writing high-quality, publication-ready deep research reports.
  Covers structure, tone, evidence standards, and formatting rules.
metadata:
  author: deep-research-agent
  version: "1.0"
---

Instructions for the agent go here.
This markdown is injected into the agent's prompt when the skill is activated.
```

> **Skills 在运行时将领域特定指令注入 agent 提示。行动点的指令。**

---

### Flow vs 单 Crew

> **自然第一设计是一个 Crew 带三个顺序任务。别这样做。**

**共享上下文跨阶段降级地面真相**。Onyx 团队称这为 **"deep frying"**:
- 事实被重新解释
- 矛盾被平滑
- 源材料在 Writer 看到时不可识别

**这个系统用 Flow**: 三个独立 Crew，每个只接收前一阶段的干净输出。

---

## 完整工作流

```
1. Type/Speak/Upload PDF as research query
         ↓
2. Researcher Agent searches web + documents via Onyx MCP
         ↓
3. Analyst Agent deduplicates / flags contradictions / groups findings
         ↓
4. Report Writer Agent produces structured citation-backed Markdown report
         ↓
5. Click "Play Report" for narration via Voxtral TTS
```

---

## 关键数据

| 指标 | 数值 |
|------|------|
| DeepResearch Bench 排名 | #1（击败 OpenAI/Gemini/Perplexity） |
| 基准任务数 | 100 个博士级任务 |
| 覆盖领域 | 22 个领域 |
| Onyx 连接器 | 40+ 企业数据源 |
| 规划探索方向 | 最多 6 个 |
| 执行周期 | 最多 8 周期 |
| 并行 Agent | 每周期最多 3 个 |
| 澄清问题 | 最多 5 个（短/模糊查询） |

---

## 核心引用

| 引用 | 含义 |
|------|------|
| "Prefer being thorough in research over being helpful" | Onyx 提示哲学 |
| "Research isn't one task" | 核心洞察 |
| "Deep frying: facts reinterpreted, contradictions smoothed" | 共享上下文问题 |
| "Data sovereignty = out of reach for closed-source" | 开源价值 |
| "Speaking > typing, Listening > reading" | 语音层价值 |

---

## 对 KilroyContentBot 的启示

### 可借鉴点
1. **三阶段分离** — Researcher/Analyst/Writer 硬墙
2. **Onyx MCP 集成** — 40+ 数据源统一搜索
3. **SKILL.md 系统** — 运行时注入指令
4. **Flow vs Crew** — 避免上下文深炸
5. **反射循环** — 每次调度前结构化输出
6. **Voxtral 语音** — 原生音频模型
7. **混合检索** — Vector + BM-25 + RRF + LLM 选择

### 可实施
- 用三阶段分离内容创作流程
- 集成 MCP 服务器统一数据访问
- 创建 SKILL.md 定义内容质量标准
- 用 Flow 而非单 Crew 避免上下文污染
- 实施反射循环追踪覆盖/差距
- 添加语音输入/输出层
- 用混合检索提升内容搜索质量

---

## 相关资源

| 资源 | 链接 |
|------|------|
| Akshay 原文 | https://x.com/akshay_pachaar/status/2047395420935229724 |
| Onyx | https://github.com/onyx-dot-app/onyx |
| CrewAI | https://github.com/crewAIInc/crewAI |
| Voxtral | Mistral 音频模型 |
| DeepResearch Bench | 独立学术基准 |

---

*原始来源：https://x.com/akshay_pachaar/status/2047395420935229724*

# Shubham Saboo — Agent SKILLS 解剖学：上下文管理的终极方案

**来源**: https://x.com/saboo_shubham_/status/2048596364196761721  
**作者**: Shubham Saboo (@saboo_shubham_)  
**抓取时间**: 2026-04-28 05:12 UTC  
**类型**: X 推文线程/技术深度文章  
**标签**: agent-skills, context-management, progressive-disclosure, skill-design, claude-code, codex, mcp-alternative, token-optimization

---

## 📊 一句话总结

Shubham 深入解析 Agent Skills 架构：SKILL.md + references/assets/scripts 四部分结构，三级渐进式披露（L1 元数据/L2 指令/L3 引用），模型直接路由匹配（非向量检索），单技能激活机制，让 20 个技能代理的启动成本与 1 个相同，解决 200k 上下文窗口中 400 tokens 关键指令被埋没的生产失败问题。

**English**: Shubham deep-dives Agent Skills architecture: SKILL.md + references/assets/scripts 4-part structure, 3-tier progressive disclosure (L1 metadata/L2 instructions/L3 references), direct model routing (not vector retrieval), single-skill activation, making 20-skill agent startup cost same as 1, solving production failure where 400 tokens of critical instructions get buried in 200k context window.

---

## 🏷️ 话题标签

#AgentSkills #ContextManagement #ProgressiveDisclosure #SkillDesign #ClaudeCode #Codex #MCPAlternative #TokenOptimization

---

## 🎨 封面图提示词（nano-banana-pro 技能库）

### 选项 1：Skill 文件结构图 ⭐ 推荐

**来源**: nano-banana-pro / Infographic / Edu Visual  
**参考 ID**: 11165 (Technical Infographic Cutaway)  
**示例图**: https://cms-assets.youmind.com/media/1772433492844_q6zr64_HCTasgQaYAADK5w.jpg

```prompt
Agent Skill File Structure diagram showing 4 parts and 3 loading tiers.

Layout: Vertical folder structure with tier annotations.

Color Palette:
- SKILL.md: Blue (#3B82F6)
- References: Green (#10B981)
- Assets: Purple (#8B5CF6)
- Scripts: Orange (#F97316)
- Background: Dark gradient

Folder Structure:
my-skill/
├── SKILL.md 🔵 (Required)
│   "YAML frontmatter"
│   "name + description (search index)"
│   "Body instructions (L2)"
│   "Usually few thousand tokens"
│
├── references/ 🟢 (Optional)
│   "Docs agent reads on demand"
│   "Edge cases, long examples"
│   "Reference tables"
│   "Loaded only when L2 points there (L3)"
│
├── assets/ 🟣 (Optional)
│   "Templates and brand files"
│   "Images, styles, configs"
│   "Loaded only when needed (L3)"
│
└── scripts/ 🟠 (Optional)
    "Code agent can execute"
    "Deterministic functions"
    "Loaded only when needed (L3)"

Bottom — 3 Loading Tiers:
L1 Metadata (Always Loaded):
"name + description"
"~100 tokens per skill"
"20 skills = 2000 tokens"

L2 Instructions (When Matched):
"SKILL.md body"
"Few thousand tokens"
"Loaded only when description matches"

L3 References (On Demand):
"references/assets/scripts"
"Loaded only when L2 points there"
"Cost = zero if not needed"

Center Insight:
"Agent with 20 skills"
"Same upfront cost as agent with 1"
"Add 21st skill tomorrow"
"Yesterday's tasks cost same"

Style: Clean technical structure, dark mode with tier colors
Aspect ratio: 9:16 portrait
```

**为什么选这个风格**: 这是关于 Agent Skills 文件结构和渐进式披露的内容，文件夹结构图直接展示 4 部分 +3 层加载机制，比单一架构图更能传达"上下文经济学"的价值。

---

### 选项 2：路由匹配流程图

**来源**: nano-banana-pro / Infographic / Edu Visual  
**参考 ID**: 11257 (Infographic Style)  
**示例图**: https://cms-assets.youmind.com/media/1772433527626_7jezbj_HCW2O1lX0AEnqu0.jpg

```prompt
Agent Skill Routing Flow diagram showing how model selects skill.

Layout: Horizontal flow showing user request → model scans → skill activates.

Color Palette:
- User Request: Blue (#3B82F6)
- Catalog Scan: Purple (#8B5CF6)
- Match: Green (#10B981)
- No Match: Gray (#6B7280)
- Background: Dark gradient

Step 1 — User Request 🔵:
图标：用户输入
"User says: 'clean up this messy CSV'"
"Request enters context"

Step 2 — Catalog Scan 🟣:
图标：模型扫描
"Model reads skill catalog"
"Each skill: ~100 tokens"
"Reads labels, picks right one"
"No embedding step"
"No similarity score"
"LLM is the router"

Step 3 — Matching Process 🟢:
图标：匹配决策
"pdf-forms → low match"
"brand-voice → low match"
"data-clean → CSV cleanup, dedup → STRONG MATCH"
"Match is exclusive"
"Only ONE skill activates"
"Others stay at L1"

Step 4 — Skill Activation 🟠:
图标：技能加载
"data-clean body loads (L2)"
"References load on demand (L3)"
"Work begins"
"Cost of unused skills = zero"

Bottom — Key Insight:
"Skills feel different from MCP tools"
"Tools: always loaded, always visible, always paid for"
"Skills: load only when relevant"
"Single skill activation per task"

Style: Modern routing flow, dark mode with step colors
Aspect ratio: 9:16 portrait
```

---

### 选项 3：有 Skills vs 无 Skills 对比

**来源**: nano-banana-pro / Social Media Post  
**参考 ID**: 6847 (Premium liquid glass Bento grid)  
**示例图**: https://cms-assets.youmind.com/media/1768962051381_l9uih4_537980579-6f29d32a-c786-40c4-bd5a-79c640737496.png

```prompt
Create a premium liquid glass Bento grid with 6 modules showing "With Skills vs Without Skills".

Color Palette:
- Without Skills: Red/gray tones
- With Skills: Green/blue tones
- Cards: Apple liquid glass (85-90% transparent)
- Background: Ethereal abstract glow, dark gradient

Module Content (6 Cards):

M1 — Hero:
"Agent Skills Anatomy"
"200k context, 400 tokens needed"
"Skills fix the burying problem"
Icon: Skill folder + Brain

M2 — Without Skills (Problem):
"400 tokens at position 142k"
"Buried under 6 tool definitions"
"4 reference docs"
"Brand guide nobody asked to read"
"Agent ignores them"
"Most common production failure"

M3 — With Skills (Solution):
"SKILL.md + references/assets/scripts"
"Progressive disclosure"
"L1: 100 tokens per skill"
"L2: Load when matched"
"L3: Load on demand"
"20 skills = same cost as 1"

M4 — Routing:
"LLM is the router"
"No embeddings"
"No similarity scores"
"Direct from descriptions"
"Exclusive match (one skill)"

M5 — Team Scale:
"Data team: data-clean, sql-runner"
"Design team: brand-voice, deck-build"
"Platform: wires agent"
"No coordination needed"
"npm for agents"

M6 — Action:
"Pick one workflow"
"Write one skill"
"One folder, one SKILL.md"
"Version in git"
"Watch agent activate it"

Output: 1 image, 9:16 portrait, ultra-premium liquid glass infographic.
```

---

## 核心洞察

### 生产失败最常见原因

> **你的 agent 有 200k token 上下文窗口。它实际需要的指令只有 400 tokens 长。它还是忽略了它们。**

**那 400 tokens 在哪**:
- 埋在位置 142k
- 在 6 个工具定义、4 个参考文档、没人让它读的品牌指南下面

> **这是 agent 在生产中失败最常见原因。不是模型或框架问题。提示词太大，正确东西被埋了。**

---

### Skills 是干净修复

> **Skills 是最干净修复。不是更大模型。不是更大窗口。不是更聪明检索器。只是关于上下文在哪和何时加载的一组小设计决策。**

**五部分让一切工作**:

---

## Skill 文件结构

### 四部分

```
my-skill/
├── SKILL.md          ← 唯一必需文件
├── references/       ← Agent 按需读取的文档
├── assets/           ← 模板和品牌文件
└── scripts/          ← Agent 可执行代码
```

**除了 SKILL.md 都是可选的。**

---

### 为什么是文件夹非 Python 类

> **Skill 不是 Python 类或注册工具。它是磁盘上带 Markdown 文件的文件夹。**

**因为 Skill 只是文件**:
- 在 git 中版本化
- 在 PR 中 diff
- 跨项目复制
- 在 GitHub 发布

> **格式就是合同。**

---

### 跨框架兼容

**相同 SKILL.md 适用于**:
- Claude Code
- Codex
- Gemini CLI
- Cursor
- Agent Development Kit
- LangChain
- 越来越多 agent 工具和框架

**一个文件夹，多运行时。**

---

## 渐进式披露（三级加载）

### L1: 元数据（总是加载）

**YAML frontmatter 两字段**:
```yaml
---
name: data-clean
description: "CSV cleanup, dedup, nulls, formatting"
---
```

**这两字段不只是元数据。它们是搜索索引。**

**会话开始时**:
- Agent 加载每个已安装技能名称和描述
- 每技能约 100 tokens
- 正文、参考、脚本全留在磁盘

---

### L2: 指令（匹配时加载）

**当请求进来时**:
- 模型读自己目录决定开哪个技能
- **描述是它匹配的东西**
- 写模糊描述 → 技能从不触发
- 写尖锐带具体触发词描述 → 技能恰好在应该时激活

> **这单行是整个技能最重要写作部分。人们花数小时在正文上，十秒在描述上，然后奇怪为什么技能从不被用。翻转这比例。**

---

### L3: 引用（按需加载）

**references/、assets/、scripts/** 仅在 L2 指令明确指向 agent 那里时加载。

---

### 上下文经济学

> **有 20 个已安装技能代理，支付与有 1 个代理相同前期成本。**

**明天加第 21 个技能**:
- 昨天任务成本与昨天相同
- 不增加
- 不衰减

**陷阱**: 渐进式披露仅在你实际用这些层时省 tokens。把所有示例塞进 SKILL.md，正文膨胀到 10K tokens。现在触发技能每个任务都付那成本。

**规则**:
- 保持 SKILL.md 短
- 将边缘情况、长示例、参考表推入 references/
- Agent 仅在需要时拉取它们

---

## 路由匹配机制

### 模型即路由器

> **当请求进来，模型做你会做的事看工具箱。读标签。选对的。打开它。**

**示例**:
```
用户说："clean up this messy CSV and dedupe rows"

模型扫描描述目录：
- pdf-forms → 低匹配
- brand-voice → 低匹配
- data-clean: CSV cleanup, dedup, nulls → 强匹配

data-clean 正文加载。工作开始。
```

---

### 两个关键细节

**1. 匹配不是向量检索**
- 模型直接从自己上下文中描述决定
- 无嵌入步骤
- 无相似度分数
- 无单独路由层
- **LLM 就是路由器**

**2. 匹配是排他的**
- 每任务仅激活一个技能
- 其余保持在 L1
- 它们正文从不进入上下文窗口
- **不需要技能成本本质为零**

---

### Skills vs MCP 工具

> **这就是让 Skills 感觉与 MCP 工具或函数调用不同的地方。**

| 特性 | MCP 工具 | Skills |
|------|----------|--------|
| 加载时机 | 总是加载 | 仅相关时加载 |
| 可见性 | 总是可见 | 匹配时可见 |
| 成本 | 总是付费 | 不需要时零成本 |

---

## 规模化效应

### 多任务场景

**一个代理，8 个已安装技能。会话过程中进来 3 个不同任务。**

**结果**:
- Agent 没用技能保持在 L1
- 每约 100 tokens，无正文，无引用
- 正文成本仅付需要任务

---

### 团队独立部署

> **模式超越上下文经济学。**

**团队可独立交付 Skills**:
- 数据团队拥有 data-clean 和 sql-runner
- 设计团队拥有 brand-voice 和 deck-build
- 平台团队接线代理
- 没人协调
- 没人合并提示词
- 没人每次新能力落地重建系统提示词

> **Skills 对 agent 做就是 npm 对 JavaScript 做的。小、聚焦、可组合单元在清晰接口后。**

> **包管理器赢了 JavaScript。相同形状将赢 agent。**

---

## 关键数据

| 指标 | 数值 |
|------|------|
| 上下文窗口 | 200k tokens |
| 需要指令 | 400 tokens |
| 指令位置（失败案例） | 142k（被埋没） |
| 每技能 L1 成本 | ~100 tokens |
| 20 技能启动成本 | 同 1 技能 |
| 匹配方式 | 模型直接路由（非向量） |
| 激活模式 | 排他（每任务 1 技能） |

---

## 核心引用

| 引用 | 含义 |
|------|------|
| "400 tokens 在 142k 位置被埋没" | 生产失败主因 |
| "Skills 是最干净修复" | 非更大模型/窗口 |
| "格式就是合同" | 文件夹即技能 |
| "LLM 就是路由器" | 无嵌入/无相似度 |
| "不需要技能成本 = 零" | 排他匹配价值 |
| "npm 对 JavaScript 做的" | Skills 规模化 |

---

## 对 KilroyContentBot 的启示

### 可借鉴点
1. **渐进式披露** — L1/L2/L3 三级加载省 tokens
2. **描述即索引** — 写尖锐描述带触发词
3. **排他匹配** — 每任务仅激活 1 技能
4. **文件夹即合同** — 版本化/diff/复制/发布
5. **跨框架兼容** — 一个 SKILL.md 多运行时
6. **团队独立部署** — 无协调无合并提示词

### 可实施
- 为内容创作技能实施三级加载
- 优化技能描述带具体触发词
- 将长示例/参考表推入 references/
- 保持 SKILL.md 短小精悍
- 用 git 版本化技能文件
- 跨框架复用技能（Claude Code/Codex/OpenClaw）

---

## 相关资源

| 资源 | 链接 |
|------|------|
| Shubham Saboo 原文 | https://x.com/saboo_shubham_/status/2048596364196761721 |
| Claude Code Skills | https://docs.anthropic.com/en/docs/claude-code/skills |
| Codex Skills | OpenAI 文档 |

---

*原始来源：https://x.com/saboo_shubham_/status/2048596364196761721*

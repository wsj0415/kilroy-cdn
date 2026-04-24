# Shiv Sakhuja — Skill Graphs 2.0：原子/分子/化合物分层组合

**来源**: https://x.com/shivsakhuja/status/2047124337191444844  
**作者**: Shiv (@shivsakhuja)  
**抓取时间**: 2026-04-24 00:36 UTC  
**类型**: X 推文线程/Skill 架构深度文章  
**标签**: skill-graphs, agent-skills, atoms-molecules-compounds, skill-composition, agent-leverage, claude-code, workflow-automation, agent-orchestration

---

## 📊 一句话总结

Shiv 提出 Skill Graphs 2.0 分层架构解决技能依赖可靠性问题：Atoms（原子/原子技能，单一目的/几乎确定性）→ Molecules（分子/2-10 个原子组合/结构化工作流）→ Compounds（化合物/多分子编排/人类驾驶），每层 10x 杠杆，驾驶化合物而非原子可实现 100x 工作输出。

**English**: Shiv proposes Skill Graphs 2.0 layered architecture to solve skill dependency reliability: Atoms (single-purpose/near-deterministic) → Molecules (2-10 atoms/structured workflow) → Compounds (multi-molecule orchestration/human-driven), 10x leverage per layer, driving compounds vs atoms achieves 100x work output.

---

## 🏷️ 话题标签

#SkillGraphs #AgentSkills #原子分子化合物 #技能组合 #Agent 杠杆 #ClaudeCode #工作流自动化 #Agent 编排

---

## 🎨 封面图提示词（nano-banana-pro 技能库）

### 选项 1：原子/分子/化合物分层图 ⭐ 推荐

**来源**: nano-banana-pro / Infographic / Edu Visual  
**参考 ID**: 11165 (Technical Infographic Cutaway)  
**示例图**: https://cms-assets.youmind.com/media/1772433492844_q6zr64_HCTasgQaYAADK5w.jpg

```prompt
Skill Graphs 2.0 Architecture diagram showing Atoms/Molecules/Compounds hierarchy.

Layout: Vertical 3-layer pyramid.

Color Palette:
- Atoms: Blue (#3B82F6)
- Molecules: Purple (#8B5CF6)
- Compounds: Green (#10B981)
- Background: Dark gradient

Layer 1 — Atoms (Base) 🔵:
图标：单一积木
"Single-purpose building blocks"
"Narrow scope, primitives"
"Almost deterministic"
"Don't call other skills"
"Examples:"
"- Scrape LinkedIn profiles"
"- Find competitor blog posts"
"- Verify email with Hunter"
"- Review this PR"

Layer 2 — Molecules (Middle) 🟣:
图标：2-10 原子组合
"2-10 atomic skills chained"
"Scoped task solver"
"Explicit instructions when/how"
"Minimize agent runtime decisions"
"Examples:"
"- Find leads (atom-1+2)"
"- Qualify + enrich (atom-3+4)"
"- Add to spreadsheet (atom-5)"
"Reliability: Very high"

Layer 3 — Compounds (Top) 🟢:
图标：多分子编排
"Multiple molecules orchestrated"
"Human-driven autonomy"
"Less deterministic by nature"
"Examples:"
"- Run outbound sales playbook"
"- Plan/build feature + review + QA"
"Leverage: 100x vs atoms"

Center Insight:
"1 Compound = 10 Molecules = 100 Atoms"
"Same brain RAM, 100x output"
"Drive compounds, not atoms"

Bottom Analogy:
"CTO with 1000 employees"
"Doesn't fix every bug himself"
"Trusts ICs to do atomic work"
"His judgement at compound level"

Style: Clean technical hierarchy, dark mode with layer colors
Aspect ratio: 9:16 portrait
```

**为什么选这个风格**: 这是关于 Skill 分层架构的内容，垂直金字塔图直接展示原子/分子/化合物的层级关系和杠杆效应，比单一架构图更能传达"分层组合"的价值。

---

### 选项 2：大脑 RAM 对比图

**来源**: nano-banana-pro / Infographic / Edu Visual  
**参考 ID**: 11257 (Infographic Style)  
**示例图**: https://cms-assets.youmind.com/media/1772433527626_7jezbj_HCW2O1lX0AEnqu0.jpg

```prompt
Brain RAM: Atomic vs Compound Work comparison diagram.

Layout: Side-by-side comparison showing leverage difference.

Color Palette:
- Atomic Work: Red/gray tones
- Compound Work: Green/blue tones
- Background: Dark gradient

Left — Driving Atomic Work 🔴:
图标：人操作原子
"5 atomic tasks in parallel"
"Each task: deterministic, low-leverage"
"Total output: 5 atomic units"
"Clogging brain RAM with low-leverage"
"Why sitting in driver seat when car has full self-driving?"

Right — Driving Compound Work 🟢:
图标：人操作化合物
"5 compound tasks in parallel"
"Each compound: 10 molecules"
"Each molecule: 10 atoms"
"Total output: 500 atomic units"
"Same brain RAM, 100x leverage"

Center — The Math:
"1 Compound = 10 Molecules = 100 Atoms"
"5 Compounds = 50 Molecules = 500 Atoms"
"Same time + brain RAM"
"Work output varies massively"

Bottom Insight:
"Your brain's RAM is limiting resource"
"Context switching capability"
"Move up to higher levels"
"Judgement at compound level"

Style: Modern comparison, dark mode with atomic/compound colors
Aspect ratio: 9:16 portrait
```

---

### 选项 3：技能可靠性 vs 深度曲线

**来源**: nano-banana-pro / Social Media Post  
**参考 ID**: 6847 (Premium liquid glass Bento grid)  
**示例图**: https://cms-assets.youmind.com/media/1768962051381_l9uih4_537980579-6f29d32a-c786-40c4-bd5a-79c640737496.png

```prompt
Create a premium liquid glass Bento grid with 6 modules showing "Skill Graph Reliability Challenge".

Color Palette:
- Primary: Blue (#3B82F6)
- Accent: Various reliability colors
- Cards: Apple liquid glass (85-90% transparent)
- Background: Ethereal abstract glow, dark gradient

Module Content (6 Cards):

M1 — Hero:
"Skill Graphs Problem"
"Dense dependency chains"
"Non-determinism at depth"
Icon: Graph + Warning

M2 — The Problem:
"Skill A → Skill B → Skill C → ..."
"Enormous depth to dependency"
"Can't be sure what will happen"
"Circular dependencies problematic"
"Human driver + non-determinism = too much judgement to agent"

M3 — Why Not Abandon:
"Composing skills = really important"
"Effective composition = step function leverage"
"Solution: compose differently"
"Layered architecture"

M4 — Atoms:
"Single-purpose primitives"
"Almost deterministic"
"Don't call other skills"
"Super reliable"
" scrape LinkedIn / verify email"

M5 — Molecules:
"2-10 atoms chained"
"Explicit when/how instructions"
"Minimize agent decisions"
"Structured workflow"
"Very reliable"

M6 — Compounds:
"Multiple molecules"
"Human-driven autonomy"
"Less deterministic"
"Trickiest to get right"
"100x leverage vs atoms"

Output: 1 image, 9:16 portrait, ultra-premium liquid glass infographic.
```

---

## 核心洞察

### Skill Graph 问题

> **当技能图变得足够大时，Agent 可能无法可靠地调用超过一定深度的技能。依赖越多，可靠性越低。**

**实际经验**（Reddit/X 上尝试过的人指出）:
- 如果 Skill A 明确指示调用 Skill B，可能相当可靠
- 但在密集图（如 Wikipedia）中，依赖链可能有巨大深度，无法确定会发生什么
- 循环依赖也可能有问题

> **这是问题因为有人类驾驶员带特定意图，现在面对大量非确定性，将太多判断交给 agent。**

---

### 解决方案：分层组合

> **技能在不同层级运作：atoms（原子）/molecules（分子）/compounds（化合物）。**

> **高层技能给 agent 更多编排判断，低层技能给模型非常清晰的工作流执行。**

---

## 三层架构

### Layer 1: Atoms（原子）

**定义**: 基础级原子技能，单一目的构建块，范围狭窄 — 基元。

**特征**:
- 几乎确定性（或尽可能接近 LLM）
- **通常不调用其他技能**
- 超级可靠

**示例**:
- scrape LinkedIn profiles
- find a competitor's blog posts
- find a person on Apollo
- verify an email with Hunter
- check email deliverability
- research a topic
- review this PR

---

### Layer 2: Molecules（分子）

**定义**: 解决更大问题。可能用 2-10 个原子技能完成范围限定的任务。

**特征**:
- 有明确指令何时/如何调用原子技能
- 给 agent 比原子更多判断，但仍尝试提供明确指令何时用哪个技能非常有帮助
- **将尽可能多的组合推入技能，最小化 agent 运行时决策**
- 也应该非常可靠

**示例**:
```
1. 结构化工作流链接几个原子：
   find leads using atom-1 and atom-2 
   → then qualify them using atom-3 
   → and enrich them using atom-4 
   → and then add them to my spreadsheet with atom-5

2. 编排器了解 5 个原子，用判断组合它们解决问题
```

---

### Layer 3: Compounds（化合物）

**定义**: 运行多个分子的高层编排器。

**示例**:
- "run outbound sales playbook"
- "plan and build this feature, then review and QA it"

**特征**:
- **这是实际给 agent 有意义自主权的层级**
- 本质上可能更不 deterministic，因为 agent 可能需要在多层面做判断
- 也是最难真正做对的，可能需要人类驾驶它们

> **是的，人类可能需要驾驶化合物（至少今天）。**

---

## 杠杆数学

### 核心公式

```
1 Compound = 10 Molecules = 100 Atoms
```

**每层 10x 杠杆**:
- 如果你驾驶原子而非化合物，只是用低杠杆工作堵塞 1 个 RAM 槽，因为那工作基本确定性
- **如果你驾驶 5 个并行编排分子或化合物工作的 agent**:
  - 5 compound tasks
  - 50 molecular tasks
  - 500 atomic units of work

> **花相同时间和大脑 RAM，执行 5 个原子任务并行 vs 5 个化合物任务并行。**

> **花相同时间和大脑 RAM，工作输出在驾驶原子工作 vs 化合物工作时差异巨大。**

---

### CTO 类比

> **这有个好平行类比：拥有 1000 员工公司的 CTO 不会自己修复每个 bug。他信任 IC 可靠地做那工作。**

| 层级 | 公司类比 | 技能层级 |
|------|----------|----------|
| **CTO** | 判断在公司层面 | Compounds |
| **工程经理** | 判断在团队层面 | Molecules |
| **IC 工程师** | 可靠执行原子任务 | Atoms |

> **你的判断在化合物层面（或更高）。**

---

## 可靠性天花板

> **仍在 figuring out 哪里破裂。我的猜测：跨越超过 8-10 个分子的化合物开始碰到自己的可靠性天花板。**

**当前状态**:
- 仍在驾驶分子和化合物，甚至那感觉不容易做对
- **目标是保持为每个工作流移动到更高层**
- 每层技能的可靠性/一致性做对非 trivial，测试技能花大量时间

**未来想象**:
> 在某个点化合物会足够好，我们需要甚至更高的抽象在那之上。

---

## 实际实现

### 命名约定

Shiv 的团队设置用原子/分子/化合物结构：

| 层级 | 他们的命名 | 说明 |
|------|-----------|------|
| **Atoms** | Capabilities | 基础能力 |
| **Molecules** | Composites | 复合技能 |
| **Compounds** | Playbooks | 剧本/编排器 |

> **目前工作相当好。**

---

## 关键数据

| 指标 | 数值 |
|------|------|
| 技能层级 | 3（Atoms/Molecules/Compounds） |
| 原子技能 | 单一目的/几乎确定性 |
| 分子技能 | 2-10 个原子组合 |
| 化合物技能 | 多分子编排 |
| 每层杠杆 | 10x |
| 化合物 vs 原子 | 100x 工作输出 |
| 可靠性天花板 | 8-10 分子/化合物 |
| 大脑 RAM 限制 | ~5 并行 agent |

---

## 核心引用

| 引用 | 含义 |
|------|------|
| "Skills operate at different levels: atoms, molecules, and compounds" | 核心架构 |
| "Higher level skills provide more judgement, lower level provide clear workflow" | 层级分工 |
| "Same brain RAM, 100x output" | 杠杆效应 |
| "Why sitting in driver seat when car has full self-driving?" | 原子工作反思 |
| "CTO doesn't fix every bug himself" | 信任 IC 做原子工作 |

---

## 对 KilroyContentBot 的启示

### 可借鉴点
1. **三层技能架构** — Atoms/Molecules/Compounds 分层
2. **原子技能** — 单一目的/几乎确定性/不调用其他
3. **分子技能** — 2-10 原子链/明确指令/最小化 agent 决策
4. **化合物技能** — 多分子编排/人类驾驶/100x 杠杆
5. **可靠性 vs 深度** — 8-10 分子天花板
6. **大脑 RAM 限制** — ~5 并行 agent
7. **命名约定** — Capabilities/Composites/Playbooks

### 可实施
- 将内容创作技能分为三层
- 原子技能：单平台发布/单格式转换
- 分子技能：多平台发布工作流
- 化合物技能：完整内容活动编排
- 测试每层可靠性
- 将判断推到化合物层
- 用人类驾驶化合物而非原子

---

## 相关资源

| 资源 | 链接 |
|------|------|
| Shiv 原文 | https://x.com/shivsakhuja/status/2047124337191444844 |
| Skill Graphs 讨论 | Reddit/X 社区实践 |

---

*原始来源：https://x.com/shivsakhuja/status/2047124337191444844*

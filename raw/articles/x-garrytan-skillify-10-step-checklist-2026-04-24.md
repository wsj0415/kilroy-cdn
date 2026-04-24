# Garry Tan — Skillify：将 Agent 失败转为永久结构修复

**来源**: https://x.com/garrytan/status/2046876981711769720  
**作者**: Garry Tan (@garrytan) — YC President & CEO  
**抓取时间**: 2026-04-24 00:38 UTC  
**类型**: X 推文线程/深度技术文章  
**标签**: skillify, agent-testing, gbrain, openclaw, hermes-agent, deterministic-vs-latent, resolver-evals, skill-checklist

---

## 📊 一句话总结

Garry 提出"Skillify"实践解决 Agent 重复失败问题：每个失败变成带测试的技能（SKILL.md+ 确定性代码 + 单元测试 + 集成测试+LLM evals+Resolver 触发+Resolver eval+DRY 审计+Smoke 测试+Brain 归档），10 步检查清单让 bug 在结构上不可能复发，GBrain 开源引擎强制执行质量门。

**English**: Garry proposes "Skillify" practice to solve Agent repeat failures: every failure becomes a skill with tests (SKILL.md+deterministic code+unit tests+integration tests+LLM evals+Resolver trigger+Resolver eval+DRY audit+Smoke test+Brain filing), 10-step checklist makes bugs structurally impossible to recur, GBrain open-source engine enforces quality gates.

---

## 🏷️ 话题标签

#Skillify #AgentTesting #GBrain #OpenClaw #HermesAgent #确定性 vs 潜在 #ResolverEvals #技能检查清单

---

## 🎨 封面图提示词（nano-banana-pro 技能库）

### 选项 1:Skillify 10 步检查清单图 ⭐ 推荐

**来源**: nano-banana-pro / Infographic / Edu Visual  
**参考 ID**: 11165 (Technical Infographic Cutaway)  
**示例图**: https://cms-assets.youmind.com/media/1772433492844_q6zr64_HCTasgQaYAADK5w.jpg

```prompt
Skillify 10-Step Checklist diagram showing failure-to-skill pipeline.

Layout: Vertical 10-step flow with checkmarks.

Color Palette:
- Steps 1-5: Blue gradient
- Steps 6-10: Green gradient
- Background: Dark gradient

Step 1 — SKILL.md 🔵:
图标：合同文档
"The Contract"
"Name / Triggers / Rules"
"calendar-recall:"
"Brain-first historical lookup"
"ALWAYS use before live API"

Step 2 — Deterministic Code 🔵:
图标：脚本文件
"scripts/*.mjs"
"No LLM for what code can do"
"calendar-recall.mjs"
"Runs in <100ms"
"Zero LLM calls"

Step 3 — Unit Tests 🔵:
图标：测试框架
"vitest"
"179 tests across 5 suites"
"Run in <2 seconds"
"Catch: Unicode drops / leap-year nulls"

Step 4 — Integration Tests 🔵:
图标：实时端点
"Live endpoints + real data"
"Catch: malformed lines / missing timezones"
"Windows line endings / midnight spans"

Step 5 — LLM Evals 🔵:
图标：LLM 判断
"Quality + correctness"
"35 evals run daily"
"Catch: wrong process + wrong answer"
"Heuristic: search 'fucking shit' in history"

Step 6 — Resolver Trigger 🟢:
图标：路由表
"Entry in AGENTS.md"
"Routes intent → skill"
"False negative: skill exists but unreachable"
"False positive: wrong skill fires"

Step 7 — Resolver Eval 🟢:
图标：测试路由
"50+ test cases"
"{intent: 'check signatures' → executive-assistant}"
"Catch: ambiguous routing"

Step 8 — Check Resolvable 🟢:
图标：可达性审计
"Meta-test: AGENTS.md → SKILL.md → script"
"First run: 6/40 skills unreachable (15%)"
"Flight tracker / content-ideas / citation-fixer"

Step 9 — DRY Audit 🟢:
图标：重复检测
"No overlapping triggers"
"4 calendar skills, zero overlap"
"Each has its lane"

Step 10 — Brain Filing 🟢:
图标：归档规则
"people/ / companies/ / civic/"
"Caught 10/13 skills filing wrong"
"Zero misfilings since"

Bottom Insight:
"A feature that doesn't pass all 10"
"Is just code that works today"
"Skillify makes bugs structurally impossible"

Style: Clean technical checklist, dark mode with step colors
Aspect ratio: 9:16 portrait
```

**为什么选这个风格**: 这是关于 Skillify 10 步检查清单的内容，垂直流程图直接展示失败到技能的完整转化流程，比单一架构图更能传达"结构化修复"的价值。

---

### 选项 2：潜在 vs 确定性对比图

**来源**: nano-banana-pro / Infographic / Edu Visual  
**参考 ID**: 11257 (Infographic Style)  
**示例图**: https://cms-assets.youmind.com/media/1772433527626_7jezbj_HCW2O1lX0AEnqu0.jpg

```prompt
Latent vs Deterministic Work comparison diagram.

Layout: Side-by-side comparison.

Color Palette:
- Latent Space: Purple (#8B5CF6)
- Deterministic: Green (#10B981)
- Background: Dark gradient

Left — Latent Space (LLM) 🟣:
图标：大脑/推理
"Judgment required"
"Interpretation / reasoning"
"Non-deterministic"
"Examples:"
"- Understanding user intent"
"- Deciding which skill to use"
"- Synthesizing findings"
"Bug: Doing deterministic work here"
"Timezone math in head"
"API calls for local data"

Right — Deterministic Space (Code) 🟢:
图标：脚本/确定性
"Precision required"
"Same input, same output"
"No model needed"
"Examples:"
"- Grep local files"
"- Timezone conversion"
"- Math calculations"
"Runs in <100ms"
"Zero LLM calls"
"Zero network"

Center — The Bug:
"Wrong work in wrong space"
"Calendar grep is deterministic"
"Agent did it in latent space anyway"
"Spinning up reasoning / making API calls"
"When three-line script would return instantly"

Bottom Fix:
"Latent space builds deterministic tool"
"Deterministic tool constrains latent space"
"Agent used judgment to write calendar-recall.mjs"
"Now skill forces agent to run script instead"
"The model's intelligence created constraint"
"that prevents model from being stupid"

Style: Modern comparison, dark mode with latent/deterministic colors
Aspect ratio: 9:16 portrait
```

---

### 选项 3：GBrain vs Hermes 对比

**来源**: nano-banana-pro / Social Media Post  
**参考 ID**: 6847 (Premium liquid glass Bento grid)  
**示例图**: https://cms-assets.youmind.com/media/1768962051381_l9uih4_537980579-6f29d32a-c786-40c4-bd5a-79c640737496.png

```prompt
Create a premium liquid glass Bento grid with 6 modules showing "GBrain vs Hermes: Creation vs Verification".

Color Palette:
- GBrain: Blue (#3B82F6)
- Hermes: Purple (#8B5CF6)
- Cards: Apple liquid glass (85-90% transparent)
- Background: Ethereal abstract glow, dark gradient

Module Content (6 Cards):

M1 — Hero:
"Agent Skill Systems"
"Creation vs Verification"
"Need both for durability"
Icon: Brain + Scale

M2 — Hermes (Nous Research):
"skill_manage tool"
"Agent creates/patches/deletes skills"
"Procedural memory earned on its own"
"Progressive disclosure"
"Bounded memory (2,200 chars)"
"Conditional activation"
"✅ Handles creation beautifully"

M3 — GBrain (Garry Tan):
"Verification engine"
"Unit tests on deterministic code"
"Resolver evals verify routing"
"check-resolvable finds dark skills"
"DRY audit catches duplicates"
"Daily health check"
"✅ Handles verification"

M4 — Failure Modes (Untested):
"deploy-k8s + kubernetes-deploy"
"Ambiguous routing"
"API changes → silent garbage"
"Weak trigger → orphan skill"
"Index tokens wasted"

M5 — Skillify Workflow:
"1. SKILL.md (contract)"
"2. Deterministic code"
"3-4. Unit + Integration tests"
"5. LLM evals"
"6-7. Resolver + eval"
"8-10. DRY + Smoke + Filing"

M6 — The Thesis:
"Every failure → skill"
"Every skill → evals"
"Every eval → runs daily"
"Agent improves permanently"
"Not just for current session"
"Shaped by every mistake"

Output: 1 image, 9:16 portrait, ultra-premium liquid glass infographic.
```

---

## 核心洞察

### LangChain 的问题

> **LangChain 筹集了 1.6 亿美元。三年开发。十亿美元估值。LangSmith（他们的测试平台）确实复杂：轨迹 evals/trace-to-dataset 管道/LLM-as-judge/回归套件/工具单元测试框架。他们有这些零件。**

**但零件不是实践。**

> **LangChain 给你测试工具。它从不告诉你要测试什么/按什么顺序/何时完成。**

**缺失的意见化工作流**:
```
this failure happened
→ now write a skill
→ now write the deterministic code
→ now write unit tests
→ now write LLM evals
→ now add a resolver trigger
→ now eval the resolver
→ now audit for duplicates
→ now smoke test
→ now file correctly
```

> **那循环不存在。你必须从分散的原语自己发明它。很多 AI 用户根本不测试他们的 agent，因为他们选择的框架可能给了健身房会员但没有锻炼计划。**

---

### 大多数 Agent"可靠性"是基于感觉

> **提示词调整。更大的系统消息。"Please don't hallucinate"咒语。那东西在对话变复杂时就 decay。**

> **筹集数亿美元解决这问题的框架给你监控仪表板和单元测试助手，说"good luck"。**

---

## 两个真实失败案例

### 失败 1：日历回忆

**问题**: Garry 问 agent 关于近 10 年前的商务旅行，简单问题应该 1 秒回答。

**Agent 实际做的**:
1. 调用实时日历 API → 被阻止（太久远）
2. 尝试邮件搜索 → 嘈杂结果，无结论
3. 用不同参数再次尝试日历 API → 仍被阻止
4. **5 分钟后，搜索本地知识库瞬间找到**

> **答案一直坐在自己的数据里。3,146 个日历文件跨越 2013-2026。已索引。已本地。一次 grep 的距离。**

> **Agent 只是没先那里看。**

---

### 潜在 vs 确定性工作

> **在我一直在写的框架中有个关键区分：需要判断的工作 vs 需要精确的工作。我叫它们 latent（潜在）和 deterministic（确定性）。**

| 类型 | 说明 | 示例 |
|------|------|------|
| **Deterministic** | 相同输入，相同输出，每次 | Calendar grep / 时间转换 / 数学计算 |
| **Latent** | 需要判断/解释/推理 | 理解用户意图 / 决定用哪个技能 / 综合发现 |

> **日历 grep 是确定性的。相同输入，相同输出，每次。无需模型。但 agent 还是在 latent space 做了，启动推理/调用 API/解释结果，而三行脚本可以瞬间返回答案。**

> **那是 bug。不是错误答案。是错误空间。**

---

### Skillify 修复

**生成的技能**:
```markdown
name: calendar-recall
description: "Brain-first historical calendar lookup. 
              ALWAYS use this before any live API for 
              any event not in the future or the last 48 hours."
```

**硬规则**:
> **Live calendar APIs are ONLY for events in the FUTURE or the LAST 48 HOURS. Everything historical goes through the local knowledge base first.**

**确定性脚本**（agent 自己写的）:
```bash
$ node scripts/calendar-recall.mjs search "Singapore"
Found 2 matching day(s):
── 2016-05-07 ── Flight to Singapore, Mandarin Oriental check-in
── 2016-05-08 ── Lunch with investors at Fullerton Hotel
```

**运行时间**: <100 毫秒（大部分是 Bun 启动，实际 grep 亚毫秒）  
**LLM 调用**: 0  
**网络**: 0  
**只是本地文件**

---

### 失败 2：时区数学

**问题**: Agent 说"下次会议在 28 分钟后"，实际 88 分钟。Agent 在大脑里做 UTC→PT 时区转换，差了整整 1 小时。

**已有脚本**（context-now.mjs）:
```json
{
  "now": "2026-04-21T07:38:12-07:00",
  "upcomingEvents": [
    {
      "summary": "App Ops Sprint Planning",
      "minutesUntil": 88
    }
  ]
}
```

**运行时间**: ~50 毫秒  
**模糊性**: 0  
**Agent 只是没运行它。**

---

### 核心循环

> **这让整个架构工作的循环：latent space 构建确定性工具，然后确定性工具约束 latent space。**

> **Agent 用判断（latent）写了 calendar-recall.mjs。现在技能强制 agent 运行那脚本而非推理日历数据。模型的智能创建了防止模型变蠢的约束。**

> **旧失败路径在结构上变得不可达。技能说"先搜索本地"。脚本做搜索。Agent 从未有机会变聪明或再次搞砸。**

---

## Skillify 10 步检查清单

> **我用这 10 项检查清单当失败被提升时：**

| # | 步骤 | 说明 |
|---|------|------|
| **1** | **SKILL.md** | 合同（名称/触发器/规则） |
| **2** | **确定性代码** | scripts/*.mjs（代码能做的不用 LLM） |
| **3** | **单元测试** | vitest |
| **4** | **集成测试** | 实时端点 |
| **5** | **LLM Evals** | 质量 + 正确性 |
| **6** | **Resolver 触发** | AGENTS.md 中的条目 |
| **7** | **Resolver Eval** | 验证触发器实际路由 |
| **8** | **Check Resolvable + DRY 审计** | 检查可达性 + 重复 |
| **9** | **E2E Smoke 测试** | 端到端验证 |
| **10** | **Brain 归档规则** | 知道东西放哪里 |

> **不通过所有十项的功能不是技能。只是今天碰巧工作的代码。**

---

## 实际工作流

### "Skillify"作为动词

> **对我来说，构建 OpenClaw（和 GBrain）时，检查清单开始是失败响应协议。然后变成我构建一切的方式。**

**典型对话**:
```
Garry: hot damn it worked. can you remember this as a 
webhook skill and skillify it, next time we need to do 
some webhooks? why was this so hard to get right? 
anyway it's good now. DRY it up too
```

**效果**: 一小时 OAuth webhook 集成 → "skillify it" → 带测试/Resolver 条目/文档的永久技能

---

### 更多示例

**浏览器技能**:
```
Garry: great! so we should actually remember this as a 
skill whenever anything in openclaw needs a headless 
browser! and also know that if we need a headed browser 
we should ask the user to run gstack browser and give 
us a pair-agent code. skillify it!
```

**链接验证技能**:
```
Garry: can we make a skill that says whenever you send 
me a link you have to curl it yourself to make sure the 
endpoint is open and the tunnel works? skillify it!
```

**日历双重预订技能**:
```
Garry: Here is one regular skill I need you to write. 
It's the calendar check skill. Tomorrow I have a double 
booked 11am. Make a skill, make it deterministic to 
check these kinds of things.
```

> **一句话。代码/技能/测试/Resolver 条目/可达性审计。整个 10 步检查清单一口气完成。**

---

## 详细步骤实践

### Step 3: 单元测试

**Classic vitest**。确定性函数，确定性断言。

**calendar-recall.mjs 导出纯函数**:
- parseEventLine
- eventMatchesKeyword
- searchKeyword
- formatJson

**每个用 fixture 数据测试**: 临时目录中的合成日历文件，已知输入，已知输出。

**捕获的 bug**:
- parseEventLine 静默丢弃 location 字段含 Unicode 字符的事件
- dateFromPath 对闰年日期返回 null
- formatJson 在只有一个人时省略 attendees 数组

> **这些是小/无聊/关键的。如果脚本产生错误输出，技能产生错误答案，agent 自信告诉我错误东西。**

**context-now 单元测试验证**:
- 时区格式化
- 安静时间检测
- DST 边界的 minutesUntil 计算

> **一个测试输入 DST 转换前 3 分钟的时间，验证输出不跳 60 分钟。那是导致"28 分钟"失败的确切 bug。现在结构上不可能。**

**规模**: 179 个单元测试跨 5 个套件，<2 秒运行。

---

### Step 4: 集成测试

**这些命中实时端点和真实数据**。

- calendar-recall.mjs 实际在真实 brain repo 中找到事件，非仅测试 fixture？
- context-now.mjs 在日历缓存过期或缺失时产生有效 JSON？

> **集成测试捕获单元测试错过的 bug，因为 fixture 数据太干净。真实数据有畸形事件行/缺失时区字段/带 Windows 行尾的日历文件/跨越午夜的事件。**

**规则**: 如果发现自己手动检查脚本在真实数据上是否做对，那检查应该是集成测试。

---

### Step 5: LLM Evals

> **这是有趣的地方。一些输出需要判断来评估。"这日历摘要有用吗？"不是脚本能回答的是/否问题。所以我用 LLM-as-judge：模型根据 rubric 评估另一模型的输出。**

**context-now**: 35 个 evals 每天运行。

**Eval 示例 1**:
```
输入："hey, my flight leaves in about 45 minutes, 
      will I make it to SFO?"
检查：agent 是否在回答前运行 context-now.mjs，
      还是尝试在大脑里算数学。
失败：如果 agent 上钩自己计算时间。
```

**Eval 示例 2**:
```
输入：UTC timestamp + "what time is that for me?"
正确行为：运行脚本并引用结果
错误行为：在大脑里做转换
捕获：错误答案 + 错误过程
```

> **即使这次心算碰巧对，下次会错。Eval 捕获两者。**

**最诚实的 eval 启发式**:
> **搜索你的对话历史当你说"fucking shit"或"wtf"的时刻。那些是你缺失的测试用例。**

---

### Step 6-7: Resolver 触发 + Eval

**Resolver 是上下文的路由表**：当任务类型 X 出现，加载技能 Y。

**Resolver 触发器只是 Markdown 表中的行**:

| Intent | Skill |
|--------|-------|
| check my signatures | executive-assistant |
| who is Pedro Franceschi | brain-ops |
| save this article | idea-ingest |
| what time is my meeting | context-now |
| find my 2016 trip | calendar-recall |

**捕获的 bug**: 写新技能但忘记添加到 Resolver。技能存在。能力存在。系统无法到达它。

> **比根本没有技能更糟，因为你以为系统处理它。**

---

### Resolver Eval 套件

**50+ 测试用例**:
```json
{ intent: 'check my signatures', expectedSkill: 'executive-assistant' }
{ intent: 'who is Pedro Franceschi', expectedSkill: 'brain-ops' }
{ intent: 'save this article', expectedSkill: 'idea-ingest' }
{ intent: 'what time is my meeting', expectedSkill: 'context-now' }
{ intent: 'find my 2016 trip', expectedSkill: 'calendar-recall' }
```

**两种失败模式**:
| 类型 | 说明 |
|------|------|
| **False Negative** | 技能应该触发但不触发（触发器描述错误或缺失） |
| **False Positive** | 错误技能触发（两个触发器重叠） |

**示例**: "What's on my calendar tomorrow" 应该路由到 calendar-check，非 calendar-recall 非 google-calendar。三个技能，三个不同时间域，一个短语可能合理匹配任何。

> **Resolver eval 在用户碰到前捕获模糊性。**

**运行两层测试**:
1. **确定性结构测试**（AGENTS.md 表包含正确映射？）
2. **LLM 路由测试**（给定这意图，模型实际选对技能吗？）

> **两层都重要。表可以正确但模型仍可能路由错因为触发器描述模糊。**

---

### Step 8: Check Resolvable

**问题**: 一个月构建后，40+ 技能。没人维护 Resolver 表。技能在出生但没注册。

**解决方案**: check-resolvable。元测试走完整链：AGENTS.md resolver → SKILL.md → script/cron。

> **如果脚本存在做有用工作但 Resolver 无路径，它不可达。LLM 永远不会知道用它。**

**首次运行发现**: 40+ 技能中 6 个不可达（15% 系统能力是暗的）:
- 航班追踪器：没人能通过问航班调用
- 内容创意生成器：只在 cron 运行，不能手动触发
- 引用修复器：存在于技能目录但 Resolver 完全没列出

**修复**: 一小时。只需添加触发器条目到 AGENTS.md。

**现在 check-resolvable 每周作为 gbrain doctor 一部分运行**。检查三件事:
1. 每个带 SKILL.md 的技能目录在 Resolver 中有对应条目
2. 技能引用的每个脚本实际可调用（文件存在/导出正确函数）
3. 无两个技能有重叠触发器描述导致模糊路由

---

### Step 9: DRY 审计

> **如果你不小心最终会有 15 个技能做差不多事，Resolver 选随机那个。**

**日历技能矩阵**（4 个技能，零重叠）:

| 技能 | 时间域 | 触发器 |
|------|--------|--------|
| calendar-recall | 历史事件 | "find my 2016 trip" |
| calendar-check | 未来事件 | "what's on my calendar" |
| context-now | 当前时间 | "what time is my meeting" |
| google-calendar | 实时 API | "check my live calendar" |

> **那矩阵不是为这帖子画的图。它活在 SKILL.md 内部，审计脚本解析它。构建第六个日历技能踩别人道，审计在技能能发布前失败。**

---

### Step 10: Brain 归档规则

**每个写知识库的技能需要知道东西放哪里**:
- 人 → people/
- 公司 → companies/
- 政策分析 → civic/

> **我抓到 10/13 个 brain-writing 技能归档到错误目录，因为它们各自硬编码路径而非咨询 Resolver。**

**归档规则文档**编目常见错误归档模式:
- Sources vs Originals
- People vs Companies（当某人 IS 公司时）

> **技能在创建任何页面前读规则。从此零错误归档。**

---

## GBrain vs Hermes Agent

### Hermes（Nous Research）

**优点**:
- skill_manage 工具让 agent 自己创建/修补/删除技能
- 基于学到的程序性记忆
- 渐进式披露（先加载技能索引，选中时拉完整 SKILL.md）
- 有界记忆（MEMORY.md 上限 2,200 字符）
- 条件激活（所需工具不可用时技能自动隐藏）

> **处理创建很美。**

---

### GBrain（Garry Tan）

**验证引擎**:
- 确定性代码的单元测试
- Resolver evals 验证路由
- check-resolvable 找暗技能
- DRY 审计抓重复
- 每日健康检查漂移变红

> **处理验证。**

---

### 无测试技能系统的失败模式

> **任何无测试的代码库都会腐烂"问题，软件工程在 2005 年解决了。Agent 技能没不同。**

| 失败模式 | 说明 |
|----------|------|
| **重复技能** | deploy-k8s（周一）+ kubernetes-deploy（周四）→ 模糊路由 |
| **API 变化** | 技能写时完美。6 周后上游 API 变形状。静默返回垃圾直到人类发现 |
| **孤儿技能** | 自主创建技能触发器弱从不匹配。成为孤儿，吃索引 token，从不运行，慢慢腐烂 |

---

## 核心论文

> **在健康软件工程团队中，每个 bug 获得测试。那测试永远活着。Bug 在结构上不可能复发。**

> **AI agent 应该同样工作。**

> **每个失败变成技能。每个技能有 evals。每个 eval 每天运行。Agent 的判断永久改进，非仅当前会话，非仅当上下文窗口持有。**

> **旅行失败不会再发生。时区失败不会再发生。当下次失败出现（它会，因为这是对抗熵和品味的游戏）它也会被 skillified。**

> **我一年后一起工作的 agent 将被前一年犯的每个失败塑造。那不是 nice-to-have。那是整个论文。**

---

## 关键数据

| 指标 | 数值 |
|------|------|
| Skillify 步骤 | 10 |
| 单元测试 | 179 个跨 5 套件 |
| 测试运行时间 | <2 秒 |
| LLM Evals（context-now） | 35 个每天 |
| Resolver Eval 测试用例 | 50+ |
| 初始不可达技能 | 6/40（15%） |
| 错误归档捕获 | 10/13 技能 |
| 日历文件 | 3,146 个（2013-2026） |
| calendar-recall 运行时间 | <100ms |
| context-now 运行时间 | ~50ms |

---

## 核心引用

| 引用 | 含义 |
|------|------|
| "Pieces aren't a practice" | LangChain 问题 |
| "Wrong work in wrong space" | 潜在 vs 确定性 |
| "Latent builds deterministic, deterministic constrains latent" | 核心循环 |
| "A feature that doesn't pass all 10 is just code that works today" | 技能定义 |
| "Every failure becomes a skill" | Skillify 论文 |

---

## 对 KilroyContentBot 的启示

### 可借鉴点
1. **Skillify 实践** — 每个失败变永久技能
2. **10 步检查清单** — 完整验证流程
3. **潜在 vs 确定性** — 正确工作在正确空间
4. **Resolver + Eval** — 路由验证
5. **Check Resolvable** — 可达性审计
6. **DRY 审计** — 重复检测
7. **LLM-as-judge** — 质量 evals
8. **Brain 归档规则** — 知识组织

### 可实施
- 为内容创作失败实施 Skillify
- 创建 10 步检查清单验证新技能
- 区分潜在工作（创意/判断）和确定性工作（发布/格式转换）
- 用 Resolver 路由意图到技能
- 运行每日 evals 验证技能行为
- 每周 check-resolvable 审计可达性
- 实施 DRY 审计防止重复技能
- 定义内容归档规则（people/companies/topics）

---

## 相关资源

| 资源 | 链接 |
|------|------|
| Garry Tan 原文 | https://x.com/garrytan/status/2046876981711769720 |
| GBrain | https://github.com/garrytan/gbrain |
| GStack | https://github.com/garrytan/gstack |
| Hermes Agent | https://github.com/NousResearch/hermes-agent |
| Resolver 文章 | Garry 之前的推文线程 |

---

*原始来源：https://x.com/garrytan/status/2046876981711769720*

# Daniel San — 保持 Claude Code 上下文整洁的子代理指南

**来源**: https://x.com/dani_avila7/status/2048486242321662189  
**作者**: Daniel San (@dani_avila7)  
**抓取时间**: 2026-04-28 05:07 UTC  
**类型**: X 推文线程/技术教程  
**标签**: claude-code, subagents, context-management, explore, plan, fork-context, claude-code-hooks, developer-tools, ai-programming, clean-context

---

## 📊 一句话总结

Daniel San 分享如何利用 Claude Code 子代理（Subagents）保持主上下文整洁，通过独立窗口运行 grep/find 等耗时任务，仅返回结果摘要，内置 Explore/Plan 子代理，支持上下文 Fork（CLAUDE_CODE_FORK_SUBAGENT=1）继承父级理解，配合 context-timeline 监控工具，避免 80k tokens 噪音和压缩丢失细节。

**English**: Daniel San shares how to use Claude Code Subagents to keep the main context clean, running time-consuming tasks like grep/find in isolated windows and returning only result summaries, built-in Explore/Plan subagents, supports context Fork (CLAUDE_CODE_FORK_SUBAGENT=1) to inherit parent understanding, paired with context-timeline monitoring tool, avoiding 80k tokens of noise and compaction detail loss.

---

## 🏷️ 话题标签

#ClaudeCode #Subagents #ContextManagement #Explore #Plan #ForkContext #ClaudeCodeHooks #DeveloperTools #AIProgramming #CleanContext

---

## 🎨 封面图提示词（nano-banana-pro 技能库）

### 选项 1：子代理隔离流程图 ⭐ 推荐

**来源**: nano-banana-pro / Infographic / Edu Visual  
**参考 ID**: 11165 (Technical Infographic Cutaway)  
**示例图**: https://cms-assets.youmind.com/media/1772433492844_q6zr64_HCTasgQaYAADK5w.jpg

```prompt
Claude Code Subagent Isolation Flow diagram.

Layout: Vertical flow showing Main Agent -> Subagent -> Summary return.

Color Palette:
- Main Agent: Blue (#3B82F6)
- Subagent: Purple (#8B5CF6)
- Summary: Green (#10B981)
- Background: Dark gradient

Top — Main Agent 🔵:
图标：终端窗口
"Main Context Window"
"User asks: 'Review this controller'"
"Delegates to subagent"
"Stays clean"

Middle — Subagent 🟣:
图标：隔离容器
"Runs in isolated window"
"grep, find, ls, glob, cd"
"50+ tool calls"
"Zero pollution to main"
"Own system prompt & tools"

Bottom — Summary Return 🟢:
图标：压缩结果
"Returns only final summary"
"3 lines with the answer"
"Rest is discarded"
"No 80k tokens of noise"

Center Insight:
"Subagent = Specialized assistant"
"Own context window"
"Own system prompt"
"Own tools & permissions"
"Main agent calls it"
"Subagent works in isolation"
"Returns summary"

Bottom Tool:
"context-timeline hook"
"Real-time subagent monitoring"
"Shows context windows"

Style: Clean technical flow, dark mode with agent colors
Aspect ratio: 9:16 portrait
```

**为什么选这个风格**: 这是关于 Claude Code 子代理隔离机制的内容，垂直流程图直接展示主代理→子代理→摘要返回的完整流程，比单一架构图更能传达"上下文隔离"的价值。

---

### 选项 2：Fork 上下文对比图

**来源**: nano-banana-pro / Infographic / Edu Visual  
**参考 ID**: 11257 (Infographic Style)  
**示例图**: https://cms-assets.youmind.com/media/1772433527626_7jezbj_HCW2O1lX0AEnqu0.jpg

```prompt
Context Fork: Default vs Forked comparison diagram.

Layout: Side-by-side comparison.

Color Palette:
- Default: Red/gray tones
- Forked: Green/blue tones
- Background: Dark gradient

Left — Default (Blank Context) 🔴:
图标：空白页面
"Starts with empty context"
"Good for cleanliness"
"Bad when you invested 100k tokens"
"Subagent knows nothing"
"Must rediscover everything"
"Wastes time & tokens"

Right — Forked (Inherited Context) 🟢:
图标：复制/继承
"Exact copy of parent context"
"export CLAUDE_CODE_FORK_SUBAGENT=1"
"Or /fork slash command"
"Inherits full conversation"
"Shares prompt cache prefix"
"Children 2-N are ~10x cheaper"
"Runs in isolation"
"Returns only final summary"

Center — Benefits:
"100k tokens understanding preserved"
"No rediscovery needed"
"10x cheaper input tokens"
"Isolated tool calls"
"Clean parent context"

Bottom Commands:
"export CLAUDE_CODE_FORK_SUBAGENT=1"
"/fork (on demand)"

Style: Modern comparison, dark mode with default/forked colors
Aspect ratio: 9:16 portrait
```

---

### 选项 3：内置子代理网格

**来源**: nano-banana-pro / Social Media Post  
**参考 ID**: 6847 (Premium liquid glass Bento grid)  
**示例图**: https://cms-assets.youmind.com/media/1768962051381_l9uih4_537980579-6f29d32a-c786-40c4-bd5a-79c640737496.png

```prompt
Create a premium liquid glass Bento grid with 6 modules showing "Built-in Claude Code Subagents".

Color Palette:
- Primary: Blue (#3B82F6)
- Accent: Various subagent colors
- Cards: Apple liquid glass (85-90% transparent)
- Background: Ethereal abstract glow, dark gradient

Module Content (6 Cards):

M1 — Hero:
"Built-in Subagents"
"Explore & Plan"
"Clean context, fast results"
Icon: Robot + Magnifying glass

M2 — Explore:
"Searches codebase"
"Without polluting main context"
"Fires grep/find in own window"
"Returns only relevant findings"
"Best for: Code navigation"

M3 — Plan:
"Investigates & produces plan"
"Reads files, understands architecture"
"Returns step-by-step doc"
"Main context sees 3 lines"
"Best for: Implementation planning"

M4 — Create Your Own:
"Markdown file + frontmatter"
"name, description, tools, model"
"Claude Code picks up automatically"
"Invokes when description matches"

M5 — File Locations:
".claude/agents/ (team/shared)"
"~/.claude/agents/ (personal)"
"Higher priority wins on conflict"

M6 — Monitoring:
"context-timeline hook"
"npx claude-code-templates"
"Real-time subagent tracking"
"Shows context windows"

Output: 1 image, 9:16 portrait, ultra-premium liquid glass infographic.
```

---

## 核心洞察

### 问题：长会话上下文污染

> **长 Claude Code 会话很快变乱。每次 grep、find 和 ls 都留在你的上下文中，占用你永远不会再读的空间。**

**实际后果**:
- 30 分钟后，你有 80k tokens 的噪音
- 当 Claude 压缩上下文时，信息被扁平化
- **重要细节在摘要中丢失**

---

### 解决方案：子代理（Subagents）

> **子代理修复这个问题：它们在独立窗口中运行工作，仅返回结果。**

**定义**: 子代理是在自己上下文窗口中运行的专业助手，有自己的系统提示、工具和权限。主代理调用它，子代理隔离工作，返回摘要。

---

## 创建子代理

### 文件结构

```markdown
---
name: code-reviewer
description: Reviews code for quality, security, and maintainability. Use after writing or modifying code.
tools: Read, Grep, Glob, Bash
model: sonnet
---

You are a senior code reviewer. When invoked:
1. Run git diff to see recent changes
2. Focus on modified files
3. Start the review immediately
```

**Claude Code 自动拾取它**，当描述匹配任务时调用。

---

### 文件保存位置（优先级）

| 位置 | 范围 | 说明 |
|------|------|------|
| `.claude/agents/` | 项目/团队 | 检入版本控制，团队共享 |
| `~/.claude/agents/` | 个人 | 个人使用，处处可用 |

**同名冲突**: 高优先级位置胜出。

---

## 无子代理 vs 有子代理

### 无子代理（传统方式）

```
主代理做一切在单一上下文中
→ 审查控制器
→ 找模式
→ 验证东西
→ 触发 grep, find, ls, glob, cd
→ 更多 grep, 更多 find
→ 每次调用留在上下文中
```

**结果**: 30 分钟后，80k tokens 噪音，永远不会读。压缩时重要细节丢失。

---

### 有子代理（隔离方式）

```
主代理委托给子代理
→ 子代理在独立窗口运行
→ 50+ 工具调用
→ 仅返回最终摘要
→ 3 行带答案
→ 其余丢弃
```

**结果**: 主上下文保持干净，无噪音，无压缩丢失。

---

## 内置子代理

Claude Code 随常用案例的子代理。你最常用的两个：

### Explore（探索）

**功能**: 搜索代码库而不污染主上下文。
**行为**: 在自己窗口触发所有 grep 和 find 调用，仅返回相关发现。
**适用**: 代码导航、查找模式、定位文件。

---

### Plan（规划）

**功能**: 调查并生成实现计划。
**行为**: 读文件、理解架构、返回逐步文档。主上下文从不看中间读取。
**结果**: 不是 50 个工具调用在窗口中，你得到 3 行带答案。其余丢弃。
**适用**: 实现规划、架构理解、任务分解。

---

## 上下文 Fork（继承父级理解）

### 问题

> **默认情况下，子代理从空白上下文开始。对清洁好，但当你已投资 100k tokens 构建代码库理解，想让子代理继承所有时，不好。**

---

### 解决方案：Fork 上下文

**方式 1: 环境变量（全局）**
```bash
export CLAUDE_CODE_FORK_SUBAGENT=1
```
设置后，每个子代理生成默认继承父完整上下文。

**方式 2: 按需 Fork（命令）**
```
/fork
```
使用 `/fork` 斜杠命令按需 Fork。

---

### Fork 子代理特性

| 特性 | 说明 |
|------|------|
| **继承** | Fork 时刻继承父完整对话 |
| **缓存共享** | 与父共享提示缓存前缀（子 2-N 输入 tokens 便宜 ~10 倍） |
| **隔离** | 在隔离中运行，工具调用不污染父 |
| **返回** | 仅返回最终摘要 |

---

## 监控：context-timeline Hook

> **追踪主代理上下文和并行运行子代理，从控制台难跟。我建了个 hook 修复这：context-timeline。**

**安装**:
```bash
npx claude-code-templates@latest --hook monitoring/context-timeline
```

**功能**:
- 打开会话时启动
- 显示主代理上下文窗口时间线
- 显示子代理如何在自己独立上下文中开始工作
- 实时显示每个运行中子代理
- 显示完成后返回主代理的上下文

---

## 关键数据

| 指标 | 数值 |
|------|------|
| 噪音 tokens（30 分钟无子代理） | 80k |
| 内置子代理 | 2（Explore/Plan） |
| Fork 缓存节省 | ~10x 输入 tokens |
| 文件位置 | 2（项目/个人） |
| 监控工具 | context-timeline |

---

## 核心引用

| 引用 | 含义 |
|------|------|
| "Subagents fix this: run work in own window, return only result" | 核心价值 |
| "30 minutes in, 80k tokens of noise" | 问题规模 |
| "Instead of 50 tool calls, get 3 lines with answer" | 隔离效果 |
| "Children 2-N are ~10x cheaper on input tokens" | Fork 缓存优势 |
| "Start with simple subagent, feel difference on first long session" | 行动呼吁 |

---

## 对 KilroyContentBot 的启示

### 可借鉴点
1. **上下文隔离** — 子代理独立窗口运行，主上下文保持干净
2. **内置 Explore/Plan** — 搜索和规划任务专用化
3. **Fork 机制** — 继承父级理解，避免重复发现
4. **缓存共享** — 子 2-N 便宜 10 倍
5. **监控 Hook** — context-timeline 实时追踪
6. **文件优先级** — 项目级 vs 个人级

### 可实施
- 为内容搜索/分析创建子代理
- 用 Fork 继承项目上下文
- 实施 context-timeline 监控
- 区分项目级和个人级技能文件
- 优化长会话上下文管理

---

## 相关资源

| 资源 | 链接 |
|------|------|
| Daniel San 原文 | https://x.com/dani_avila7/status/2048486242321662189 |
| context-timeline Hook | npx claude-code-templates@latest |
| Claude Code 文档 | https://docs.anthropic.com/en/docs/claude-code |

---

*原始来源：https://x.com/dani_avila7/status/2048486242321662189*

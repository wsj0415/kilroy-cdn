# Field Theory CLI — X/Twitter 书签同步与本地知识库

**来源**: https://github.com/afar1/fieldtheory-cli  
**作者**: afar1 + 6 贡献者（包括 Claude Opus 4.6）  
**抓取时间**: 2026-04-23 16:00 UTC  
**类型**: GitHub 仓库/开源 CLI 工具  
**标签**: fieldtheory-cli, x-bookmarks, twitter-archive, claude-code-integration, knowledge-base, local-first, bookmark-sync, markdown-wiki

---

## 📊 一句话总结

Field Theory CLI 是免费开源的 Mac 命令行工具，同步并本地存储所有 X/Twitter 书签，支持搜索/分类/可视化，生成 Karpathy 风格互联知识库，集成 Claude Code/Codex agent，无需 API 通过浏览器会话同步，数据完全本地存储在 `~/.ft-bookmarks/`。

**English**: Field Theory CLI is free open-source Mac CLI tool that syncs and locally stores all X/Twitter bookmarks, supports search/classification/visualization, generates Karpathy-style interlinked knowledge base, integrates with Claude Code/Codex agent, syncs via browser session without API, data stored locally at `~/.ft-bookmarks/`.

---

## 🏷️ 话题标签

#FieldTheoryCLI #XBookmarks #TwitterArchive #ClaudeCode 集成 #知识库 #本地优先 #书签同步 #MarkdownWiki

---

## 🎨 封面图提示词（nano-banana-pro 技能库）

### 选项 1：Field Theory 工作流程图 ⭐ 推荐

**来源**: nano-banana-pro / Infographic / Edu Visual  
**参考 ID**: 11165 (Technical Infographic Cutaway)  
**示例图**: https://cms-assets.youmind.com/media/1772433492844_q6zr64_HCTasgQaYAADK5w.jpg

```prompt
Field Theory CLI Workflow diagram showing bookmark sync to knowledge base.

Layout: Horizontal 4-stage flow.

Color Palette:
- X Sync: Blue (#3B82F6)
- Local Store: Green (#10B981)
- Classification: Purple (#8B5CF6)
- Wiki: Orange (#F97316)
- Background: Dark gradient

Stage 1 — X Bookmark Sync 🔵:
图标：X/Twitter logo
"ft sync"
"Browser session extraction"
"No API required"
"Download all bookmarks"
"Chrome/Firefox/Edge/Brave"

Stage 2 — Local Storage 🟢:
图标：本地数据库
"~/.ft-bookmarks/"
"bookmarks.jsonl"
"SQLite FTS5 index"
"bookmarks-meta.json"
"Data stays local"

Stage 3 — Classification 🟣:
图标：LLM 分类
"ft classify"
"7 categories: tool/security/technique"
"launch/research/opinion/commerce"
"LLM or regex mode"
"Auto after sync"

Stage 4 — Knowledge Base 🟠:
图标：互联 wiki
"ft wiki"
"Karpathy-style interlinked"
"Compiled truth + timeline"
"ft ask <question>"
"Markdown pages"

Bottom Agent Integration:
"ft skill install"
"/fieldtheory skill"
"Claude Code / Codex"
"Ask: 'What have I bookmarked about X?'"

Style: Clean technical workflow, dark mode with stage colors
Aspect ratio: 9:16 portrait
```

**为什么选这个风格**: 这是关于 Field Theory CLI 工作流程的内容，四阶段流程图直接展示 X 同步→本地存储→分类→知识库的完整流程，比单一架构图更能传达"书签到知识库"的价值。

---

### 选项 2：命令参考网格

**来源**: nano-banana-pro / Infographic / Edu Visual  
**参考 ID**: 11257 (Infographic Style)  
**示例图**: https://cms-assets.youmind.com/media/1772433527626_7jezbj_HCW2O1lX0AEnqu0.jpg

```prompt
Field Theory CLI Commands categorized grid showing 6 command groups.

Layout: 6 category boxes with command counts.

Color Palette:
- Sync: Blue (#3B82F6)
- Search: Green (#10B981)
- Classification: Purple (#8B5CF6)
- Knowledge Base: Orange (#F97316)
- Agent: Yellow (#FBBF24)
- Utilities: Red (#EF4444)
- Background: Dark gradient

Category 1 — Sync (8 commands) 🔵:
"ft sync — Download bookmarks"
"ft sync --rebuild — Full re-crawl"
"ft sync --continue — Resume"
"ft sync --gaps — Backfill"
"ft sync --folders — Sync folders"
"ft sync --media — Download media"
"ft sync --api — OAuth API mode"
"ft auth — Setup OAuth"

Category 2 — Search (8 commands) 🟢:
"ft search <query> — BM25 search"
"ft list — Filter by author/date"
"ft show <id> — Show detail"
"ft sample <cat> — Random sample"
"ft stats — Top authors/languages"
"ft viz — Terminal dashboard"
"ft categories — Distribution"
"ft domains — Subject domains"

Category 3 — Classification (5 commands) 🟣:
"ft classify — LLM classification"
"ft classify --regex — Regex mode"
"ft classify-domains — Domain only"
"ft classify --engine <name>"
"ft model — View/change engine"

Category 4 — Knowledge Base (6 commands) 🟠:
"ft md — Export markdown files"
"ft md --changed — Re-export changed"
"ft wiki — Compile interlinked wiki"
"ft ask <question> — Ask wiki"
"ft ask --save — Save answer"
"ft lint / lint --fix — Health check"

Category 5 — Agent (3 commands) 🟡:
"ft skill install — Install /fieldtheory"
"ft skill show — Print content"
"ft skill uninstall — Remove files"

Category 6 — Utilities (5 commands) 🔴:
"ft index — Rebuild search index"
"ft fetch-media — Download media"
"ft status — Show sync status"
"ft path — Print data dir"
"ft folders — Show folder distribution"

Center Badge:
"1.6k Stars"
"104 Commits"
"MIT License"
"Free & Open Source"

Bottom Insight:
"Data stays local"
"No telemetry"
"Works with any agent"

Style: Modern commands grid, dark mode with category colors
Aspect ratio: 9:16 portrait
```

---

### 选项 3：7 分类系统可视化

**来源**: nano-banana-pro / Social Media Post  
**参考 ID**: 6847 (Premium liquid glass Bento grid)  
**示例图**: https://cms-assets.youmind.com/media/1768962051381_l9uih4_537980579-6f29d32a-c786-40c4-bd5a-79c640737496.png

```prompt
Create a premium liquid glass Bento grid with 8 modules showing "Field Theory 7 Categories".

Color Palette:
- Primary: Blue (#3B82F6)
- Accent: Various category colors
- Cards: Apple liquid glass (85-90% transparent)
- Background: Ethereal abstract glow, dark gradient

Module Content (8 Cards):

M1 — Hero:
"Field Theory Classification"
"7 Categories"
"LLM + Regex modes"
Icon: Categories + AI

M2 — tool 🔵:
"GitHub repos"
"CLI tools"
"npm packages"
"Open-source projects"

M3 — security 🟢:
"CVEs"
"Vulnerabilities"
"Exploits"
"Supply chain"

M4 — technique 🟣:
"Tutorials"
"Demos"
"Code patterns"
"'How I built X'"

M5 — launch 🟠:
"Product launches"
"Announcements"
"'Just shipped'"

M6 — research 🔴:
"ArXiv papers"
"Studies"
"Academic findings"

M7 — opinion 🟡:
"Takes"
"Analysis"
"Commentary"
"Threads"

M8 — commerce 🟢:
"Products"
"Shopping"
"Physical goods"

Output: 1 image, 9:16 portrait, ultra-premium liquid glass infographic.
```

---

## 核心洞察

### Field Theory CLI 是什么

> **同步并本地存储所有 X/Twitter 书签。搜索/分类/可视化。让 Claude Code/Codex 或任何有 shell 访问的 agent 可使用。**

**关键特性**:
- 免费开源
- 专为 Mac 设计
- 无需 API（通过浏览器会话同步）
- 数据完全本地存储
- 无遥测无分析

---

### 快速开始

```bash
# 1. 安装
npm install -g fieldtheory

# 2. 同步书签（需支持浏览器登录 X）
ft sync

# 3. 搜索
ft search "distributed systems"

# 4. 探索
ft viz
ft categories
ft stats
```

**首次运行**: `ft sync` 从浏览器提取 X 会话，下载书签到 `~/.ft-bookmarks/`

---

## 完整命令参考

### Sync 命令

| 命令 | 描述 |
|------|------|
| `ft sync` | 下载并同步书签（无需 API） |
| `ft sync --rebuild` | 完全重新爬取所有书签 |
| `ft sync --continue` | 从保存的游标恢复暂停/中断的同步 |
| `ft sync --gaps` | 回填引用推文/展开截断/X Article 文本/丰富链接文章内容 |
| `ft sync --folders` | 同步 X 书签文件夹标签（X 状态只读镜像） |
| `ft sync --folder <name>` | 按名称同步单个文件夹（精确或无歧义前缀） |
| `ft sync --classify` | 同步后用 LLM 分类新书签 |
| `ft sync --media` | 同步书签后下载 X 媒体资产到本地（照片/视频海报/限制视频） |
| `ft sync --media --skip-profile-images` | 下载帖子媒体不含作者头像 |
| `ft sync --api` | 通过 OAuth API 同步（跨平台） |
| `ft auth` | 设置 OAuth 用于 API 同步（可选） |

---

### Search and Browse 命令

| 命令 | 描述 |
|------|------|
| `ft search <query>` | 带 BM25 排名的全文搜索 |
| `ft list` | 按作者/日期/分类/域名/文件夹过滤 |
| `ft list --folder <name>` | 显示 X 书签文件夹中的书签 |
| `ft show <id>` | 详细显示单个书签 |
| `ft sample <category>` | 从分类随机抽样 |
| `ft stats` | 顶部作者/语言/日期范围 |
| `ft viz` | 带火花线/分类/域名的终端仪表板 |
| `ft categories` | 显示分类分布 |
| `ft domains` | 主题域名分布 |
| `ft folders` | 显示 X 书签文件夹分布（需先 `ft sync --folders`） |

---

### Classification 命令

| 命令 | 描述 |
|------|------|
| `ft classify` | 用 LLM 按分类和域名分类 |
| `ft classify --regex` | 用简单 regex 按分类分类 |
| `ft classify-domains` | 仅按主题域名分类（LLM） |
| `ft classify --engine <name>` | 覆盖单次运行的 LLM 引擎（也适用于 `ft sync --classify` 和 `ft classify-domains`） |
| `ft model` | 查看或更改默认 LLM 引擎 |

---

### Knowledge Base 命令

| 命令 | 描述 |
|------|------|
| `ft md` | 导出书签为单个 Markdown 文件，含丰富文章内容 |
| `ft md --changed` | 仅重新导出源书签数据更改的 Markdown 文件 |
| `ft wiki` | 编译 Karpathy 风格互联知识库 |
| `ft ask <question>` | 对知识库提问 |
| `ft ask <question> --save` | 提问并保存答案为概念页 |
| `ft lint` | 健康检查 wiki 的断链/缺失页 |
| `ft lint --fix` | 自动修复可修复的 wiki 问题 |

---

### Agent Integration 命令

| 命令 | 描述 |
|------|------|
| `ft skill install` | 为 Claude Code 和 Codex 安装 `/fieldtheory` 技能 |
| `ft skill show` | 打印技能内容到 stdout |
| `ft skill uninstall` | 移除安装的技能文件 |

---

### Utilities 命令

| 命令 | 描述 |
|------|------|
| `ft index` | 从 JSONL 缓存重建搜索索引（保留分类） |
| `ft fetch-media` | 回填/下载现有书签的 X 媒体资产（默认：所有待处理书签） |
| `ft fetch-media --skip-profile-images` | 下载帖子媒体不含作者头像 |
| `ft status` | 显示同步/分类状态和数据位置 |
| `ft path` | 打印数据目录路径 |

---

## 7 个分类系统

| 分类 | 捕获内容 |
|------|----------|
| **tool** | GitHub repos/CLI 工具/npm 包/开源项目 |
| **security** | CVEs/漏洞/利用/供应链 |
| **technique** | 教程/演示/代码模式/"我如何构建 X" |
| **launch** | 产品发布/公告/"刚发布" |
| **research** | ArXiv 论文/研究/学术发现 |
| **opinion** | 观点/分析/评论/线程 |
| **commerce** | 产品/购物/实物商品 |

**使用 `ft classify` 进行 LLM 驱动的分类，捕获 regex 错过的内容。**

---

## Agent 集成

### 安装技能

```bash
ft skill install     # 自动检测 Claude Code 和 Codex
```

### 然后问你的 agent

> "What have I bookmarked about cancer research in the last three years and how has it progressed?"

> "I bookmarked a number of new open source AI memory tools. Pick the best one and figure out how to incorporate it in this repo."

> "Every day please sync any new X bookmarks using the Field Theory CLI."

**适用于 Claude Code/Codex 或任何有 shell 访问的 agent。**

---

## 调度

```bash
# 每天早上 7 点同步
0 7 * * * ft sync

# 每天早上同步并分类
0 7 * * * ft sync --classify
```

`ft` 尊重标准代理环境变量用于网络请求：`HTTPS_PROXY`/`HTTP_PROXY`/`ALL_PROXY`/`NO_PROXY`

---

## 数据存储

所有数据本地存储在 `~/.ft-bookmarks/`:

```
~/.ft-bookmarks/
  bookmarks.jsonl         # 原始书签缓存（每行一个）
  bookmarks.db            # SQLite FTS5 搜索索引
  bookmarks-meta.json     # 同步元数据
  oauth-token.json        # OAuth token（如果用 API 模式，chmod 600）
  md/                     # Markdown 知识库（ft wiki / ft md）
```

**用 `FT_DATA_DIR` 覆盖位置**:
```bash
export FT_DATA_DIR=/path/to/custom/dir
```

**删除所有数据**: `rm -rf ~/.ft-bookmarks`

---

## 平台支持

| 功能 | macOS | Linux | Windows |
|------|-------|-------|---------|
| **会话同步** (`ft sync`) | Chrome/Chromium/Brave/Edge/Helium/Comet/Dia/Firefox | Chrome/Chromium/Brave/Edge/Firefox | Chrome/Chromium/Brave/Edge/Firefox |
| **OAuth API 同步** (`ft sync --api`) | ✅ | ✅ | ✅ |
| **搜索/列表/分类/可视化/wiki** | ✅ | ✅ | ✅ |

**会话同步**从浏览器本地数据库提取 cookie。用 `ft sync --browser <name>` 选择浏览器。

**Windows 注意**: PowerShell 中用 `fieldtheory` 或 `ft.cmd` 而非 `ft`（因为 `ft` 已是 `Format-Table` 内置别名）。

---

## 安全

### 数据隐私

> **你的数据保持本地。** 无遥测/无分析/无电话回家。CLI 仅在同步期间对 X API 发出网络请求。

---

### Chrome 会话同步

从 Chrome 本地数据库读取 cookie，用于同步请求，然后丢弃。**Cookie 永不单独存储。**

---

### OAuth Tokens

用 `chmod 600`（仅所有者）存储。**像密码一样对待 `~/.ft-bookmarks/oauth-token.json`。**

---

### API 使用

**默认同步使用 X 的内部 GraphQL API**，与 x.com 在浏览器中使用的 API 相同。对于官方 v2 API，用 `ft auth` + `ft sync --api`。

---

## 关键数据

| 指标 | 数值 |
|------|------|
| GitHub Stars | 1.6k |
| Forks | 175 |
| 贡献者 | 7（包括 Claude Opus 4.6） |
| Commits | 104 |
| 语言 | TypeScript 88.2% / JavaScript 11.8% |
| 许可证 | MIT |
| 分类数 | 7 |
| 命令数 | 30+ |
| 数据位置 | `~/.ft-bookmarks/` |

---

## 核心引用

| 引用 | 含义 |
|------|------|
| "Sync and locally store all of your X/Twitter bookmarks" | 核心价值 |
| "Data stays local. No telemetry." | 隐私承诺 |
| "Karpathy-style interlinked knowledge base" | 知识库风格 |
| "Works with Claude Code, Codex, or any agent with shell access" | Agent 集成 |
| "Free and open source. Designed for Mac." | 开源定位 |

---

## 对 KilroyContentBot 的启示

### 可借鉴点
1. **X 书签同步** — 自动捕获内容灵感
2. **本地优先存储** — 数据完全可控
3. **7 分类系统** — 内容自动分类
4. **Karpathy 风格 wiki** — 互联知识库
5. **Agent 技能集成** — `/fieldtheory` 技能
6. **调度同步** — cron 定时任务
7. **Markdown 导出** — 可移植知识库

### 可实施
- 同步 X 书签到本地知识库
- 用 7 分类系统自动分类内容
- 生成互联 Markdown wiki
- 安装 agent 技能自动查询
- 设置 cron 定时同步
- 导出 Markdown 用于内容创作

---

## 相关资源

| 资源 | 链接 |
|------|------|
| Field Theory CLI | https://github.com/afar1/fieldtheory-cli |
| 官方网站 | https://fieldtheory.dev/cli |
| Star History | https://www.star-history.com/?repos=afar1%2Ffieldtheory-cli |

---

*原始来源：https://github.com/afar1/fieldtheory-cli*

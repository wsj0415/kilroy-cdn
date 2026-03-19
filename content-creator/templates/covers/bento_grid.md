# Bento Grid 信息图提示词模板

## 适用场景
- 专业感、信息密度高
- 科技感、数据展示
- 微头条/B 站封面

## 基础提示词

```prompt
Create an image of premium liquid glass Bento grid product infographic with 8 modules.

Product: [产品名称]
Category: TECH

Color Palette:
- Hero color: [主色调，如 Tech blue #2563EB]
- Icons, borders: Muted hero color (30-40% saturation)
- Background: Soft gradient from light to white

Visual Style:
- Cards: Apple liquid glass (85-90% transparent)
- Whisper-thin borders with subtle drop shadow
- Background: Abstract tech pattern at 10-15% opacity
- Asymmetric Bento grid, [aspect_ratio] landscape
- Hero card: 30% | Info modules: 70%

Module Content:
M1 — Hero: [产品名称] text + [核心图标]
M2 — Core Benefits: [4 个核心优势] + icons
M3 — Supported Tools: [支持的工具列表]
M4 — Key Metrics: [4-5 个关键数据]
M5 — Features: [核心功能列表]
M6 — Tech Stack: [技术栈]
M7 — Quick Access: [访问方式]
M8 — Call to Action: [行动号召]

Output: 1 image, [aspect_ratio], ultra-premium liquid glass infographic.
```

## 变量说明

| 变量 | 说明 | 示例 |
|------|------|------|
| 产品名称 | 要推广的产品 | Skills Manager |
| 主色调 | 品牌色/主题色 | Tech blue #2563EB |
| aspect_ratio | 尺寸比例 | 16:9 / 9:16 / 3:4 |
| 核心图标 | 代表性图标 | AI agent icons |
| 核心优势 | 4 个主要优势 | Browse, Enable, Install, Copy |
| 支持的工具 | 兼容的工具列表 | 11 AI coding agents |
| 关键数据 | 量化数据 | "11 Tools", "1 Platform" |
| 核心功能 | 主要功能 | Enable/Disable, GitHub Install |
| 技术栈 | 技术信息 | Electron, Next.js, TypeScript |
| 访问方式 | GitHub/网站 | skills-manager GitHub repo |
| 行动号召 | 引导语 | "Start Managing Skills Today" |

## 示例（Skills Manager）

```prompt
Create an image of premium liquid glass Bento grid product infographic with 8 modules.

Product: Skills Manager - Universal AI Agent Skills Tool
Category: TECH

Color Palette:
- Hero color: Tech blue (#2563EB)
- Icons, borders: Muted blue (30-40% saturation)
- Background: Soft gradient from light blue to white

Visual Style:
- Cards: Apple liquid glass (85-90% transparent)
- Whisper-thin borders with subtle drop shadow
- Background: Abstract tech pattern at 10-15% opacity
- Asymmetric Bento grid, 16:9 landscape
- Hero card: 30% | Info modules: 70%

Module Content:
M1 — Hero: "Skills Manager" text + AI agent icons collage
M2 — Core Benefits: Browse, Enable, Install, Copy, Delete
M3 — Supported Tools: 11 AI coding agents (Claude Code, Cursor, etc.)
M4 — Key Metrics: "11 Tools", "1 Platform", "100% Free", "Open Source"
M5 — Features: Enable/Disable, GitHub Install, Cross-Agent Copy
M6 — Tech Stack: Electron, Next.js, TypeScript, Tailwind
M7 — Quick Access: skills-manager GitHub repo
M8 — Call to Action: "Start Managing Skills Today"

Output: 1 image, 16:9 landscape, ultra-premium liquid glass infographic.
```

## 尺寸建议

| 平台 | 推荐尺寸 | 提示词设置 |
|------|----------|------------|
| 微头条 | 16:9 | `16:9 landscape` |
| B 站 | 16:9 | `16:9 landscape` |
| 小红书 | 3:4 | `3:4 portrait` |
| 抖音 | 9:16 | `9:16 portrait` |
| 公众号 | 1:1 | `1:1 square` |

---
*模板版本：v1.0 | 最后更新：2026-03-19*

# 视觉风格提示词库

## 设计工具风 (design-tool)

### 封面 1 - 问题篇
```
Vertical 9:16 infographic cover, Figma-style purple gradient background (#7c3aed to #a855f7),
frustrated designer at messy workspace, scattered UI components floating chaotically,
broken design system elements, red error marks on artboards,

TITLE: "[主标题]" (large, white, bold geometric sans-serif)
SUBTITLE: "[副标题]" (medium, #ddd6fe)

Visual elements:
- Messy workspace with coffee cups
- Fractured component pieces
- Red warning icons
- Dark purple atmosphere with tension

COLOR: Deep purple (#4c1d95) + Warning orange (#f97316)
MOOD: Problem-aware, frustration, urgency
```

### 封面 2 - 方案篇
```
Vertical 9:16 infographic cover, Figma-style purple gradient (#7c3aed to #a855f7),
organized clean workspace, floating Glassmorphism command panels,
UI components aligning in perfect grid,

TITLE: "[产品名]" (large, white, bold)
SUBTITLE: "[核心卖点]" (medium, #ddd6fe)

FEATURE CARDS (Glassmorphism style):
- Translucent white cards with blur effect
- Rounded corners (16px)
- Subtle white borders
- Soft drop shadows

COLOR: Purple (#7c3aed) + Success green (#22c55e) + White
MOOD: Solution, clarity, empowerment
```

### 封面 3 - 行动篇
```
Vertical 9:16 infographic cover, vibrant purple to pink gradient (#a855f7 to #ec4899),
designer celebrating with rocket launch visual,
fully operational design system, team collaboration scene,

TITLE: "[行动号召]" (large, white with glow)
SUBTITLE: "[紧迫感文案]" (medium, #fbcfe8)

CTA SECTION:
- Command code block
- Copy button visual
- Social proof elements

COLOR: Pink (#ec4899) + Purple (#7c3aed) + Gold accent (#fbbf24)
MOOD: Victory, transformation, urgency
```

---

## 极客代码风 (geek-code)

### 通用元素
```
Dark terminal aesthetic (#0d1117 to #161b22),
Green monospace code glow (#238636),
Command-line interface elements,
Floating terminal windows with syntax highlighting,

Font: JetBrains Mono / Fira Code
Accent: Tech blue (#58a6ff)
```

---

## 极简卡片风 (minimal-card)

### 通用元素
```
Clean white to soft gray gradient (#ffffff to #f5f5f5),
Minimalist card-based layout with subtle shadows,
Swiss design principles, generous whitespace,

Cards:
- Rounded rectangles (12px radius)
- Soft shadows (0 4px 6px rgba(0,0,0,0.1))
- Thin borders (1px #e5e5e5)
- Black text on white

COLOR: Black (#1a1a1a) + White (#ffffff) + Gray (#666666)
MOOD: Premium, editorial, Apple-style
```

---

## 温暖生活风 (warm-life)

### 通用元素
```
Warm sunset gradient (#ff6b35 to #f7c59f),
Abstract flowing wave patterns,
Paper grain texture overlay,
Natural lighting, soft shadows,

Font: Rounded sans-serif / Handwritten style
Accent: Warm yellow (#ffd93d)
```

---

## 赛博朋克风 (cyberpunk)

### 通用元素
```
Dark background with neon accents (#0a0a0f to #1a1a2e),
Neon blue (#00f3ff) and purple (#bc13fe) glow effects,
Circuit board patterns, holographic UI elements,
Scan lines and digital noise overlay,

Font: Futuristic / Tech style
Effects: Chromatic aberration, bloom, glow
```

---

## 商务专业风 (business-pro)

### 通用元素
```
Deep navy gradient (#1e3a5f to #0f172a),
Gold accent lines and geometric frames (#d4af37),
Premium textures (marble, metal),
Editorial typography (Serif + Sans-serif combo),

Layout:
- Golden ratio composition
- Symmetrical balance
- Professional spacing

COLOR: Navy (#1e3a5f) + Gold (#d4af37) + White (#ffffff)
MOOD: Luxury, authority, trust
```

---

## Glassmorphism 设计规范

### 核心参数
```css
background: rgba(255, 255, 255, 0.1);
backdrop-filter: blur(10px);
border: 1px solid rgba(255, 255, 255, 0.2);
border-radius: 16px;
box-shadow: 0 4px 30px rgba(0, 0, 0, 0.1);
```

### 适用场景
- 功能卡片
- 数据展示
- 命令面板
- 特性列表

### 层级关系
```
背景层：渐变/模糊
↓
装饰层：漂浮元素/光效
↓
内容层：Glassmorphism 卡片
↓
文字层：标题/正文
```

---

## 文字层级规范

### 主标题
- 字号：最大 (占画面 15-20%)
- 字重：Bold/Black
- 颜色：高对比度
- 位置：上 1/3 处

### 副标题
- 字号：中号 (占画面 8-10%)
- 字重：Medium/Regular
- 颜色：次要强调色
- 位置：主标题下方

### 账号标识
- 字号：小号 (占画面 5%)
- 字重：Bold
- 位置：底部居中或左下角
- 格式：头像占位符 + @账号名

---

*最后更新：2026-03-09*

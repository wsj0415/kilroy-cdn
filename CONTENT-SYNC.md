# 📦 Kilroy CDN 内容同步系统

---

## 🎯 概述

本系统用于自动将内容工厂生成的原始内容同步到 `kilroy-cdn` GitHub 仓库，实现：

- ✅ 内容永久存储
- ✅ 版本控制
- ✅ 多平台分发备份
- ✅ 团队协作共享

---

## 📁 目录结构

```
kilroy-cdn/
├── content_output/          # 内容输出目录
│   ├── xiaohongshu_*.md     # 小红书内容
│   ├── douyin_*.md          # 抖音内容
│   ├── bilibili_*.md        # B 站内容
│   └── wechat_*.md          # 公众号内容
├── ai_images/               # AI 生成图片
├── screenshots/             # 截图素材
├── sync-content.sh          # 同步脚本
└── CONTENT-SYNC.md          # 本文档
```

---

## 🚀 快速开始

### 手动同步

```bash
# 查看同步状态
./sync-content.sh --status

# 同步指定文件
./sync-content.sh --sync xiaohongshu_agent_engineering.md xiaohongshu

# 同步所有内容
./sync-content.sh --all

# 列出待同步内容
./sync-content.sh --list
```

### 自动同步

内容工厂已配置 hook，生成新内容时自动同步：

```bash
# Hook 脚本位置
/root/.openclaw/workspace/matrix/hooks/auto-sync-cdn.sh

# 日志位置
/var/log/kilroy-cdn-sync.log

# 查看日志
tail -f /var/log/kilroy-cdn-sync.log
```

---

## 📊 内容命名规范

| 平台 | 前缀 | 示例 |
|------|------|------|
| 小红书 | `xiaohongshu_` | `xiaohongshu_agent_engineering.md` |
| 抖音 | `douyin_` | `douyin_ai_tutorial.md` |
| B 站 | `bilibili_` | `bilibili_openclaw_intro.md` |
| 公众号 | `wechat_` | `wechat_monthly_recap.md` |
| 通用 | `content_` | `content_general_001.md` |

---

## 🔄 同步流程

```
内容工厂生成
     ↓
matrix/output/*.md
     ↓
auto-sync-cdn.sh (自动触发)
     ↓
sync-content.sh --sync
     ↓
content_output/ 目录
     ↓
Git Commit + Push
     ↓
https://github.com/wsj0415/kilroy-cdn
```

---

## 📝 内容文件格式

每个同步的内容文件包含：

1. **元数据区**：内容 ID、创建时间、平台、状态、来源
2. **封面文案**：主标题、副标题、视觉建议
3. **正文内容**：完整的小红书/抖音/B 站文案
4. **标签**：平台相关标签
5. **相关链接**：Notion、GitHub、原始来源
6. **同步信息**：同步时间、源文件路径、CDN 文件路径

---

## 🔧 配置选项

### 环境变量

```bash
# 可选：自定义配置
export CONTENT_OUTPUT_DIR="/custom/path/output"
export CDN_DIR="/custom/path/kilroy-cdn/content_output"
```

### Git 配置

```bash
# 首次使用需要配置 Git 用户
git config user.email "your@email.com"
git config user.name "Your Name"
```

---

## 📈 监控与日志

### 查看同步状态

```bash
# 实时状态
./sync-content.sh --status

# 同步日志
tail -f /var/log/kilroy-cdn-sync.log

# Git 提交历史
cd /root/.openclaw/workspace/kilroy-cdn && git log --oneline
```

### 常见问题

| 问题 | 解决方案 |
|------|----------|
| 同步失败 | 检查 Git 配置和网络连接 |
| 文件已存在 | 脚本会自动跳过或添加时间戳 |
| 权限错误 | `chmod +x sync-content.sh` |

---

## 🔗 相关链接

- **GitHub 仓库**: https://github.com/wsj0415/kilroy-cdn
- **内容工厂**: `/root/.openclaw/workspace/matrix/output/`
- **Notion 数据库**: https://www.notion.so/31849e5eec0f8145bc93f72f22dde375

---

## 📅 更新日志

### 2026-03-05
- ✅ 初始版本发布
- ✅ 支持手动/自动同步
- ✅ 集成内容工厂 hook
- ✅ 首篇内容同步完成

---

*最后更新：2026-03-05 | 维护者：KilroyContentBot*

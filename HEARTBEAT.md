# HEARTBEAT.md - KilroyContentBot 心跳任务

## 📅 每日检查（北京时间 9:00）
- [ ] 追踪 AI/自媒体热点（web_search + x-fetcher）
- [ ] 检查 Notion 内容工厂数据库状态
- [ ] 扫描 GitHub 仓库更新（kilroy-cdn）
- [ ] **新增**: 用 NotebookLM 工作流分析 1 个对标频道（轮换）

## 📆 每周检查（周日 20:00）
- [ ] 回顾 memory/ 文件，更新 MEMORY.md
- [ ] 分析本周内容数据（完播率/互动率/收藏率）
- [ ] 规划下周选题方向
- [ ] **新增**: 用 NotebookLM 工作流批量生成下周 10 个脚本

## ⚡ 触发条件（自动执行）
- 收到 X/Twitter 链接 → 自动抓取分析并保存到 GitHub
- 收到 YouTube 链接 → 自动提取字幕并总结
- 收到普通网页链接 → 自动总结归档
- 连续 8 小时无交互 → 主动询问次日规划

## 📊 心跳检查记录
记录到：`memory/heartbeat-state.json`

```json
{
  "lastChecks": {
    "hotspot": null,
    "github": null,
    "memory_review": null
  },
  "lastActive": null
}
```

## 🎯 主动汇报规则
- 发现爆款选题（收藏率>1.5%）→ 立即推荐
- GitHub 推送失败 → 立即告警
- 热点情报收集完成 → 发送总结链接
- 记忆文件超过 7 天未整理 → 提醒用户
- **新增**: NotebookLM 工作流分析完成 → 发送频道分析报告
- **新增**: 所有生成内容自动同步 GitHub（敏感信息除外）

---
*最后更新：2026-03-25 | 下次回顾：2026-04-01*
*本次更新：新增 NotebookLM 内容工厂工作流 + 全部同步 GitHub 规范*

---

## 📋 GitHub 同步规范（2026-03-25 新增）

**原则：** 所有生成内容自动同步 GitHub（敏感信息除外）

| 内容类型 | 同步路径 | 示例 |
|----------|----------|------|
| 文案内容 | `summaries/YYYY-MM-DD/` | 微头条文案、脚本 |
| 提示词 | `prompts/cover-images/` | 封面图提示词 |
| 调研报告 | `researches/` | 风格调研报告 |
| 技能模板 | `content-creator/` | 内容创作模板 |
| 学习笔记 | `memory/` | 工作流笔记 |

**敏感信息（不同步）：**
- Token/API Key
- 密码/凭证
- 个人隐私数据
- 商业机密

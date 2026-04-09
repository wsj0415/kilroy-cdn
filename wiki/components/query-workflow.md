# 查询流程

**用途**: 基于 wiki 知识回答问题/创作内容  
**原则**: 先咨询 wiki，再输出，最后归档  
**输出**: reports/ + wiki 更新

---

## 标准查询提示词

```
请先咨询 wiki/ 获取相关上下文，然后 [任务描述]。

步骤：
1. 阅读 wiki/index.md 找到相关页面
2. 深入阅读相关概念/决策页面
3. 基于 wiki 知识执行任务
4. 输出到 reports/[类别]/[文件名].md
5. 如果有新决策/洞察，更新 wiki：
   - 新决策 → wiki/decisions/
   - 新概念 → wiki/concepts/
   - 新框架 → wiki/components/
6. 更新 index.md 和 log.md

输出要求：
- 引用使用的 wiki 页面
- 标注新决策
- 链接到相关现有知识
```

---

## 查询类型

### 1. 内容创作查询

```
任务：创作 [平台] 内容，主题 [X]

流程：
1. 咨询 wiki/ 查找：
   - 相关概念页面
   - 用户偏好（声音样本分析）
   - 平台适配规则
2. 使用采访式提问澄清需求
3. 创作文案
4. 输出到 reports/content/
5. 归档决策到 wiki/decisions/
```

### 2. 分析查询

```
任务：分析 [来源]，提取 [洞察]

流程：
1. 咨询 wiki/ 查找：
   - 相关分析框架
   - 历史分析案例
2. 执行分析
3. 输出到 reports/analysis/
4. 新概念归档到 wiki/concepts/
```

### 3. 决策查询

```
任务：帮助决定 [X]

流程：
1. 咨询 wiki/ 查找：
   - 相关历史决策
   - 决策框架
2. 使用 Steelman 反对（构建反方论点）
3. 提供建议和理由
4. 最终决策归档到 wiki/decisions/
```

### 4. 学习查询

```
任务：解释 [概念]

流程：
1. 咨询 wiki/ 查找：
   - 概念页面
   - 相关来源
2. 综合解释
3. 输出到 reports/summaries/
4. 补充概念页面（如有新洞察）
```

---

## 输出归档规则

### reports/ 结构

```
reports/
├── content/              # 内容文案
│   ├── weitoutiao/
│   ├── xiaohongshu/
│   ├── bilibili/
│   └── wechat/
├── analysis/             # 分析报告
│   ├── x-posts/
│   ├── youtube/
│   └── web-articles/
└── presentations/        # 幻灯片
    └── marp/
```

### 命名规则

```
YYYY-MM-DD_任务_平台.md
```

示例：
```
2026-04-09_llm-wiki-analysis_weitoutiao.md
2026-04-09_12-claude-uses_xiaohongshu.md
```

---

## wiki 更新规则

### 何时更新 wiki

- ✅ 新决策（影响未来方向）
- ✅ 新概念（之前没有的）
- ✅ 新框架（可复用的）
- ✅ 用户偏好确认
- ❌ 临时想法（还没验证）
- ❌ 重复信息（已有页面）

### 更新位置

| 内容类型 | 归档位置 |
|----------|----------|
| 决策 | wiki/decisions/ |
| 概念 | wiki/concepts/ |
| 框架/模板 | wiki/components/ |
| 用户偏好 | schema.md 或 wiki/entities/user-preferences.md |
| 来源摘要 | wiki/summaries/ |

---

## 实际案例

### 案例：LLM Wiki 微头条创作

**查询**:
```
请先咨询 wiki/ 获取 LLM Wiki 相关上下文，然后创作微头条文案。
目标：推广 LLM Wiki 概念，引导评论想要 schema 模板。
```

**执行**:
1. 阅读 wiki/concepts/llm-wiki-core.md
2. 阅读 schema.md 了解格式规则
3. 创作 3 版微头条
4. 输出到 reports/content/weitoutiao/2026-04-09_llm-wiki.md
5. 归档决策到 wiki/decisions/content-llm-wiki-strategy.md

**输出**:
```markdown
# LLM Wiki 微头条文案

**版本 1** (推荐)
[文案内容]

**版本 2**
[文案内容]

**版本 3**
[文案内容]

## 使用的 wiki 页面
- [[llm-wiki-core]]
- [[schema-constitution]]

## 新决策
- 强调"5000+ stars"作为社会证明
- CTA 用"想要 schema 模板"引导评论
- 不深入 technical 细节

## 归档
- 决策：wiki/decisions/content-llm-wiki-strategy.md
```

---

## 检查清单

每次查询后检查：

- [ ] 咨询了相关 wiki 页面
- [ ] 引用了使用的来源
- [ ] 输出到正确的 reports/ 位置
- [ ] 新决策已归档
- [ ] 新概念已创建页面
- [ ] index.md 已更新
- [ ] log.md 已追加

---

*流程会随使用优化。每次查询后反思：哪步可以更快？哪个提示词更好用？*  
*v1.0 | 2026-04-09*

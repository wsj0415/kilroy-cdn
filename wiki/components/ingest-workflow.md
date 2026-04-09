# 摄入流程自动化

**用途**: 将 raw/ 中的来源自动编译到 wiki/  
**触发**: 手动触发或定时触发  
**输出**: wiki 页面 + index.md 更新 + log.md 追加

---

## 标准摄入提示词

```
请摄入 raw/ 中的新来源并编译到 wiki/。

步骤：
1. 扫描 raw/ 找到未处理的文件
2. 阅读每个文件，提取关键概念和洞察
3. 创建或更新 wiki 页面：
   - 摘要页面 → wiki/summaries/
   - 概念页面 → wiki/concepts/
   - 实体页面 → wiki/entities/
   - 决策页面 → wiki/decisions/
4. 更新 wiki/index.md 添加新页面
5. 追加 wiki/log.md 记录本次摄入
6. 显示变更摘要

输出格式：
- 处理了 X 个文件
- 创建了 Y 个页面
- 更新了 Z 个页面
- 关键洞察列表
```

---

## 批量摄入

当有多个来源时：

```
请批量摄入以下来源：

来源列表：
1. raw/articles/karpathy_llm_wiki_gist.md
2. raw/articles/x_polydao_karpathy_method.md
3. raw/articles/x_worldofai_implementation.md

要求：
- 找出共同主题，创建综合概念页面
- 每个来源单独摘要
- 建立交叉引用
- 识别矛盾点（如有）

输出：
- 综合概念页面：wiki/concepts/[主题].md
- 来源摘要：wiki/summaries/[来源].md
- 更新 index.md 和 log.md
```

---

## 摄入记录模板

```markdown
## [日期] ingest | [主题]

**操作者**: KilroyContentBot  
**来源**: [文件列表]

### 创建页面
- [[页面 1]] — 描述（字节数）
- [[页面 2]] — 描述（字节数）

### 更新页面
- [[页面 3]] — 更新内容
- [[页面 4]] — 更新内容

### 关键提取
- [洞察 1]
- [洞察 2]
- [洞察 3]

### 交叉引用
- [[页面 1]] ↔ [[页面 2]]
- [[页面 3]] ↔ [[页面 5]]

### 下一步
- [待摄入的相关来源]
- [待深入的概念]
```

---

## 自动化脚本（可选）

```bash
#!/bin/bash
# ingest.sh - 自动摄入 raw/ 中的新文件

RAW_DIR="./raw"
WIKI_DIR="./wiki"
LOG_FILE="$WIKI_DIR/log.md"

# 检查 raw/ 中是否有新文件
NEW_FILES=$(find "$RAW_DIR" -type f -mtime -1)

if [ -z "$NEW_FILES" ]; then
    echo "没有新文件需要摄入"
    exit 0
fi

echo "发现新文件:"
echo "$NEW_FILES"

# 调用 LLM 进行摄入
# (这里可以是 API 调用或本地脚本)

echo "摄入完成"
```

---

## 摄入检查清单

每次摄入后检查：

- [ ] 所有新来源已处理
- [ ] 创建了相应的 wiki 页面
- [ ] index.md 已更新
- [ ] log.md 已追加
- [ ] 交叉引用已建立
- [ ] 矛盾点已标记（如有）
- [ ] 下一步已记录

---

## 常见问题

**Q: 一次摄入多少合适？**
A: 开始 1-2 个，熟悉后可以批量 5-10 个。太多容易乱。

**Q: 摄入后发现矛盾怎么办？**
A: 标记矛盾，创建决策页面记录你的选择。矛盾不是问题，是洞察。

**Q: 旧的需要重新摄入吗？**
A: 如果来源更新了，重新摄入并标记版本。如果知识更新了，更新 wiki 页面。

---

*流程会随使用优化。每次摄入后反思：哪步可以自动化？哪个提示词更好用？*  
*v1.0 | 2026-04-09*

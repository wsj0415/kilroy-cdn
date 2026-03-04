#!/usr/bin/env python3
"""
提示词库整理脚本
将 Nano Banana Pro 提示词库整理为资源包格式
"""

import json
import os
from pathlib import Path
from datetime import datetime

# 配置
SOURCE_DIR = Path("/root/.openclaw/agents/content/skills/nano-banana-pro/references")
OUTPUT_DIR = Path("/root/.openclaw/agents/content/content/resource-pack")

# 分类映射（中文）
CATEGORY_NAMES = {
    "social-media-post": "社交媒体配图",
    "product-marketing": "产品营销",
    "profile-avatar": "头像肖像",
    "others": "其他创意",
    "poster-flyer": "海报宣传单",
    "ecommerce-main-image": "电商主图",
    "game-asset": "游戏素材",
    "infographic-edu-visual": "信息图表",
    "comic-storyboard": "漫画分镜",
    "app-web-design": "UI 设计",
    "youtube-thumbnail": "视频封面"
}

def load_manifest():
    """加载分类清单"""
    with open(SOURCE_DIR / "manifest.json", "r", encoding="utf-8") as f:
        return json.load(f)

def extract_prompts(category_file):
    """从分类文件中提取提示词"""
    with open(SOURCE_DIR / category_file, "r", encoding="utf-8") as f:
        return json.load(f)

def create_category_index():
    """创建分类索引表（CSV 格式，便于转 Excel）"""
    print("📊 创建分类索引表...")
    
    manifest = load_manifest()
    index_data = []
    
    for category in manifest["categories"]:
        category_slug = category["slug"]
        category_name = CATEGORY_NAMES.get(category_slug, category["title"])
        category_file = category["file"]
        
        print(f"   处理分类：{category_name} ({category_file})")
        
        prompts = extract_prompts(category_file)
        
        for prompt in prompts:
            # 跳过没有示例图的提示词
            if not prompt.get("sourceMedia"):
                continue
            
            index_data.append({
                "ID": prompt["id"],
                "分类": category_name,
                "分类 Slug": category_slug,
                "标题": prompt["title"],
                "描述": prompt["description"],
                "示例图": prompt["sourceMedia"][0] if prompt["sourceMedia"] else "",
                "需要参考图": prompt.get("needReferenceImages", False),
                "提示词长度": len(prompt["content"]),
            })
    
    # 保存为 CSV
    import csv
    csv_file = OUTPUT_DIR / "category-index.csv"
    
    with open(csv_file, "w", encoding="utf-8", newline="") as f:
        if index_data:
            writer = csv.DictWriter(f, fieldnames=index_data[0].keys())
            writer.writeheader()
            writer.writerows(index_data)
    
    print(f"✅ 索引表已保存：{csv_file}")
    print(f"   总计：{len(index_data)} 条记录")
    
    return index_data

def create_sample_prompts():
    """创建示例提示词文件（每个分类精选 10 个）"""
    print("\n📝 创建示例提示词...")
    
    manifest = load_manifest()
    samples = {}
    
    for category in manifest["categories"]:
        category_slug = category["slug"]
        category_name = CATEGORY_NAMES.get(category_slug, category["title"])
        category_file = category["file"]
        
        prompts = extract_prompts(category_file)
        
        # 选择前 10 个有示例图的
        selected = []
        for prompt in prompts:
            if prompt.get("sourceMedia"):
                selected.append({
                    "id": prompt["id"],
                    "title": prompt["title"],
                    "description": prompt["description"],
                    "content": prompt["content"],
                    "sourceMedia": prompt["sourceMedia"],
                })
            if len(selected) >= 10:
                break
        
        samples[category_slug] = {
            "category": category_name,
            "count": len(selected),
            "prompts": selected
        }
        
        print(f"   {category_name}: {len(selected)} 个")
    
    # 保存
    sample_file = OUTPUT_DIR / "sample-prompts.json"
    with open(sample_file, "w", encoding="utf-8") as f:
        json.dump(samples, f, ensure_ascii=False, indent=2)
    
    print(f"✅ 示例提示词已保存：{sample_file}")

def create_tutorial_outline():
    """创建教程大纲"""
    print("\n📚 创建教程大纲...")
    
    tutorial = {
        "title": "AI 绘画提示词使用教程",
        "version": "1.0",
        "chapters": [
            {
                "chapter": 1,
                "title": "什么是提示词？",
                "content": [
                    "提示词的定义",
                    "为什么提示词很重要",
                    "好提示词 vs 差提示词"
                ]
            },
            {
                "chapter": 2,
                "title": "提示词的结构",
                "content": [
                    "主体描述",
                    "风格设定",
                    "光线和色彩",
                    "构图和视角",
                    "技术参数"
                ]
            },
            {
                "chapter": 3,
                "title": "如何选择合适的提示词",
                "content": [
                    "根据场景选择分类",
                    "根据需求调整参数",
                    "参考示例图"
                ]
            },
            {
                "chapter": 4,
                "title": "提示词优化技巧",
                "content": [
                    "添加细节描述",
                    "调整光线参数",
                    "优化构图设定",
                    "使用负面提示词"
                ]
            },
            {
                "chapter": 5,
                "title": "实战案例演示",
                "content": [
                    "案例 1：电商产品图",
                    "案例 2：自媒体封面",
                    "案例 3：个人头像"
                ]
            },
            {
                "chapter": 6,
                "title": "常见问题解答",
                "content": [
                    "生成的图不清晰怎么办？",
                    "如何保持一致性？",
                    "商业用途是否允许？"
                ]
            }
        ]
    }
    
    tutorial_file = OUTPUT_DIR / "tutorial-outline.json"
    with open(tutorial_file, "w", encoding="utf-8") as f:
        json.dump(tutorial, f, ensure_ascii=False, indent=2)
    
    print(f"✅ 教程大纲已保存：{tutorial_file}")

def create_quick_start_guide():
    """创建快速入门指南"""
    print("\n🚀 创建快速入门指南...")
    
    guide = """# 🚀 快速入门指南

## 1. 安装技能

```bash
# OpenClaw 用户
/skill nano-banana-pro
```

## 2. 基本使用

### 方式 1：直接搜索
```
"帮我找一个赛博朋克风格的头像提示词"
```

### 方式 2：指定分类
```
"我要产品营销类的提示词"
"找电商主图的提示词"
```

### 方式 3：内容配图
```
"这是我的文章：[粘贴内容]
帮我生成一个封面图提示词"
```

## 3. 使用提示词

### 复制提示词
1. 选择喜欢的提示词
2. 复制英文提示词内容
3. 粘贴到 AI 绘画工具

### 推荐工具
- Nano Banana Pro (Gemini)
- Midjourney
- DALL-E 3
- Stable Diffusion

## 4. 优化建议

### 添加细节
```
原提示词："一个女孩"
优化后："一个 25 岁的亚洲女性，长发，微笑，白色背景，专业摄影"
```

### 调整参数
```
添加：光线设定、相机参数、构图方式
```

### 使用负面提示词
```
避免：模糊、畸形、低质量
```

## 5. 常见问题

### Q: 提示词太长怎么办？
A: 可以分段使用，先用核心描述，再逐步添加细节

### Q: 生成的图和示例不一样？
A: 不同模型有差异，可以微调提示词或更换模型

### Q: 可以商用吗？
A: 可以！本资源包完全免费，允许商业用途

---

更多教程详见 `tutorial-outline.json`
"""
    
    guide_file = OUTPUT_DIR / "QUICKSTART.md"
    with open(guide_file, "w", encoding="utf-8") as f:
        f.write(guide)
    
    print(f"✅ 快速入门指南已保存：{guide_file}")

def main():
    """主函数"""
    print("=" * 60)
    print("🎨 提示词库整理工具")
    print("=" * 60)
    print(f"📂 源目录：{SOURCE_DIR}")
    print(f"📦 输出目录：{OUTPUT_DIR}")
    print()
    
    # 确保输出目录存在
    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
    
    # 执行整理
    create_category_index()
    create_sample_prompts()
    create_tutorial_outline()
    create_quick_start_guide()
    
    # 输出报告
    print()
    print("=" * 60)
    print("✅ 资源包整理完成！")
    print("=" * 60)
    print()
    print("📦 资源包内容:")
    for f in OUTPUT_DIR.iterdir():
        if f.is_file():
            size = f.stat().st_size / 1024  # KB
            print(f"   📄 {f.name} ({size:.1f} KB)")
    print()
    print("🔗 GitHub 仓库：https://github.com/wsj0415/kilroy-cdn")
    print("📚 Notion 文档库：https://www.notion.so/31949e5eec0f81289fb4d8374216bede")

if __name__ == "__main__":
    main()

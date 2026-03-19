#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Content Creator - 智能内容创作助手
支持一步步引导用户完成内容创作全流程
"""

import json
import os
from pathlib import Path

# 技能目录
SKILL_DIR = Path(__file__).parent
TEMPLATES_DIR = SKILL_DIR / "templates"
REFERENCES_FILE = SKILL_DIR / "references" / "index.json"


def load_index():
    """加载索引文件"""
    with open(REFERENCES_FILE, 'r', encoding='utf-8') as f:
        return json.load(f)


def load_template(template_path):
    """加载模板文件"""
    full_path = SKILL_DIR / template_path
    if full_path.exists():
        with open(full_path, 'r', encoding='utf-8') as f:
            return f.read()
    return None


def print_styles(index):
    """打印风格选项"""
    print("\n📝 文案风格选项：")
    print("-" * 50)
    for i, style in enumerate(index['styles'], 1):
        default = " ⭐ 默认推荐" if style.get('默认推荐') else ""
        print(f"{i}. {style['name']}{default}")
        print(f"   {style['description']}")
        print(f"   适用：{', '.join(style['适用场景'])}")
        if '使用条件' in style:
            print(f"   ⚠️ {style['使用条件']}")
        print()


def print_platforms(index):
    """打印平台选项"""
    print("\n📱 目标平台选项：")
    print("-" * 50)
    for i, platform in enumerate(index['platforms'], 1):
        print(f"{i}. {platform['name']}")
        print(f"   字数：{platform['word_limit']} | 封面：{platform['cover_ratio']}")
        print(f"   最佳发布时间：{platform['best_time']}")
        print()


def print_cover_styles(index):
    """打印封面图风格选项"""
    print("\n🎨 封面图风格选项：")
    print("-" * 50)
    for i, style in enumerate(index['cover_styles'], 1):
        default = " ⭐ 默认推荐" if style.get('默认推荐') else ""
        print(f"{i}. {style['name']}{default}")
        print(f"   {style['description']}")
        print(f"   推荐平台：{', '.join(style['推荐平台'])}")
        print()


def get_user_choice(options, prompt):
    """获取用户选择"""
    while True:
        choice = input(f"\n{prompt}: ").strip()
        if choice.isdigit() and 1 <= int(choice) <= len(options):
            return int(choice) - 1
        print("❌ 请输入有效的序号")


def main():
    """主函数"""
    print("=" * 60)
    print("🤖 Content Creator - 智能内容创作助手")
    print("=" * 60)
    
    # 加载索引
    index = load_index()
    
    # Step 1: 内容主题
    print("\n📝 第一步：内容信息")
    print("-" * 50)
    topic = input("1. 内容主题是什么？（例如：Skills Manager 统一管理 AI 编程工具）: ").strip()
    
    # Step 2: 选择风格
    print_styles(index)
    style_idx = get_user_choice(index['styles'], "2. 选择文案风格（输入序号）")
    selected_style = index['styles'][style_idx]
    print(f"✅ 已选择：{selected_style['name']}")
    
    # Step 3: 选择平台
    print_platforms(index)
    platform_idx = get_user_choice(index['platforms'], "3. 选择目标平台（输入序号）")
    selected_platform = index['platforms'][platform_idx]
    print(f"✅ 已选择：{selected_platform['name']}")
    
    # Step 4: 是否需要封面图
    need_cover = input("\n4. 需要封面图提示词吗？(y/n): ").strip().lower() == 'y'
    
    cover_style = None
    if need_cover:
        print_cover_styles(index)
        cover_idx = get_user_choice(index['cover_styles'], "5. 选择封面图风格（输入序号）")
        cover_style = index['cover_styles'][cover_idx]
        print(f"✅ 已选择：{cover_style['name']}")
    
    # Step 5: 收集项目信息
    print("\n📝 第二步：项目信息")
    print("-" * 50)
    project_name = input("项目名称：").strip()
    github_url = input("GitHub 链接：").strip()
    demo_url = input("在线体验链接（可选）：").strip()
    tech_stack = input("技术栈（可选）：").strip()
    
    print("\n核心功能（每行一个，输入空行结束）：")
    features = []
    while True:
        feature = input("  - ").strip()
        if not feature:
            break
        features.append(feature)
    
    print("\n解决的问题（可选）：")
    pain_point = input("  ").strip()
    
    # Step 6: 生成文案
    print("\n" + "=" * 60)
    print("🎬 生成文案中...")
    print("=" * 60)
    
    # 加载模板
    template = load_template(selected_style['模板文件'])
    
    if template:
        print(f"\n📋 使用模板：{selected_style['模板文件']}")
        print("(模板内容已加载，可根据模板结构生成文案)")
    
    # 输出摘要
    print("\n" + "=" * 60)
    print("📊 创作配置摘要")
    print("=" * 60)
    print(f"内容主题：{topic}")
    print(f"文案风格：{selected_style['name']}")
    print(f"目标平台：{selected_platform['name']}")
    print(f"平台要求：{selected_platform['word_limit']}字，封面{selected_platform['cover_ratio']}")
    print(f"封面图：{'需要 - ' + cover_style['name'] if need_cover else '不需要'}")
    print(f"项目名称：{project_name}")
    print(f"GitHub: {github_url}")
    if demo_url:
        print(f"在线体验：{demo_url}")
    if tech_stack:
        print(f"技术栈：{tech_stack}")
    print(f"核心功能：{len(features)}个")
    if pain_point:
        print(f"解决痛点：{pain_point}")
    
    # Step 7: 生成封面图提示词
    if need_cover and cover_style:
        print("\n" + "=" * 60)
        print("🎨 封面图提示词")
        print("=" * 60)
        
        cover_template = load_template(cover_style['prompt_template'])
        if cover_template:
            print(f"\n使用模板：{cover_style['prompt_template']}")
            print("(可根据模板生成具体提示词)")
    
    print("\n" + "=" * 60)
    print("✅ 配置完成！")
    print("=" * 60)
    print("\n下一步：")
    print("1. 根据模板和收集的信息生成完整文案")
    print("2. 生成封面图提示词（如需要）")
    print("3. 提供发布建议")
    print("\n提示：可以将以上配置保存，用于后续生成")


if __name__ == "__main__":
    main()

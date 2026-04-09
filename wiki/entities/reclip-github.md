# ReClip — 自托管视频下载器

**来源**: https://github.com/averygan/reclip  
**创建日期**: 2026-04-09  
**标签**: video-downloader, yt-dlp, self-hosted, open-source  
**相关页面**: [[media-tools]], [[content-workflow-tools]]

---

## 摘要

ReClip 是一个自托管的开源视频/音频下载器，带简洁的 Web UI。支持 YouTube、TikTok、Instagram、Twitter/X 等 1000+ 网站。后端仅 150 行 Python（Flask），前端无框架零构建。核心功能：MP4/MP3下载、质量选择、批量下载、自动去重。

---

## 核心数据

| 指标 | 数值 |
|------|------|
| Stars | 2.2k |
| Forks | 363 |
| 后端代码 | ~150 行 Python |
| 依赖 | 2 个（Flask, yt-dlp） |
| 支持网站 | 1000+（via yt-dlp） |
| 许可证 | MIT |

---

## 功能

- ✅ 下载 1000+ 网站视频（基于 yt-dlp）
- ✅ MP4 视频或 MP3 音频提取
- ✅ 质量/分辨率选择器
- ✅ 批量下载 — 一次粘贴多个 URL
- ✅ 自动 URL 去重
- ✅ 简洁响应式 UI — 无框架、无构建
- ✅ 单文件后端（~150 行 Python）

---

## 技术栈

| 层级 | 技术 | 说明 |
|------|------|------|
| **后端** | Python + Flask | ~150 行 |
| **前端** | Vanilla HTML/CSS/JS | 单文件，无构建 |
| **下载引擎** | yt-dlp + ffmpeg | 核心依赖 |
| **依赖总数** | 2 个 | Flask, yt-dlp |

---

## 快速开始

### 方式 1：本地运行

```bash
# 安装依赖
brew install yt-dlp ffmpeg    # 或 apt install ffmpeg && pip install yt-dlp

# 克隆项目
git clone https://github.com/averygan/reclip.git
cd reclip

# 运行
./reclip.sh
```

访问：**http://localhost:8899**

### 方式 2：Docker

```bash
docker build -t reclip . && docker run -p 8899:8899 reclip
```

---

## 使用流程

1. 粘贴一个或多个视频 URL 到输入框
2. 选择 **MP4**（视频）或 **MP3**（音频）
3. 点击 **Fetch** 加载视频信息和缩略图
4. 选择质量/分辨率（如可用）
5. 点击下载单个视频，或 **Download All**

---

## 支持的平台

任何 yt-dlp 支持的网站，包括：

- YouTube
- TikTok
- Instagram
- Twitter/X
- Reddit
- Facebook
- Vimeo
- Twitch
- Dailymotion
- SoundCloud
- Loom
- Streamable
- Pinterest
- Tumblr
- Threads
- LinkedIn
- 等等

---

## 代码结构

```
reclip/
├── assets/              # 预览图片
├── static/              # 静态资源
├── templates/           # HTML 模板
├── .gitignore
├── Dockerfile
├── LICENSE
├── README.md
├── app.py               # Flask 后端（~150 行）
├── reclip.sh            # 启动脚本
└── requirements.txt     # Python 依赖
```

---

## 关键洞察

### 为什么这个项目值得注意

1. **极简主义** — 150 行后端，2 个依赖，无框架前端
2. **自托管** — 数据不经过第三方服务器
3. **批量处理** — 一次处理多个 URL，自动去重
4. **UI 简洁** — 无构建步骤，开箱即用

### 与内容创作工作流的结合点

- 下载 YouTube/B 站视频 → 本地分析 → 提取字幕 → 内容改编
- 下载竞争对手视频 → 分析结构 → 学习爆款模式
- 批量下载系列内容 → 建立素材库 → AI 分析模式

---

## 潜在用途（KilroyContentBot）

### 用途 1：视频素材库
```
批量下载对标账号视频 → 本地存储 → yt-dlp 提取字幕 → AI 分析脚本结构
```

### 用途 2：跨平台改编
```
下载 YouTube 长视频 → 提取音频 → 剪辑为播客 → 改编为小红书/抖音
```

### 用途 3：竞争分析
```
下载竞品视频 → AI 分析标题/封面/节奏 → 提取爆款模式 → 生成改进建议
```

---

## 部署建议

### 本地开发
- 直接运行 `./reclip.sh`
- 适合测试和临时使用

### 服务器部署（推荐）
```bash
# Docker 部署
docker build -t reclip .
docker run -d -p 8899:8899 --name reclip reclip

# 添加开机自启
docker update --restart=always reclip
```

### 与现有工具集成
- 下载的视频 → `raw/videos/` 文件夹
- 自动触发字幕提取 → `raw/youtube/`
- AI 分析 → 编译到 wiki/

---

## 参考来源

- GitHub: https://github.com/averygan/reclip
- yt-dlp: https://github.com/yt-dlp/yt-dlp
- Flask: https://flask.palletsprojects.com/

---

## 反向链接

- [[media-tools]] — 媒体工具集合
- [[content-workflow-tools]] — 内容工作流工具
- [[video-analysis-workflow]] — 视频分析工作流

---

*本页面由 LLM 基于 GitHub README 编译维护。*  
*最后更新：2026-04-09*

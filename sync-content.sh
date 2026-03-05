#!/bin/bash

# =============================================================================
# Kilroy CDN 内容同步脚本
# =============================================================================
# 用途：将内容工厂的输出自动同步到 kilroy-cdn 仓库
# 使用：./sync-content.sh <内容文件路径> [平台类型]
# 示例：./sync-content.sh xiaohongshu_agent_engineering.md xiaohongshu
# =============================================================================

set -e

# 配置
CONTENT_OUTPUT_DIR="/root/.openclaw/workspace/matrix/output"
CDN_DIR="/root/.openclaw/workspace/kilroy-cdn/content_output"
CDN_REPO="/root/.openclaw/workspace/kilroy-cdn"

# 颜色输出
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
BLUE='\033[0;34m'
NC='\033[0m' # No Color

# 日志函数
log_info() { echo -e "${BLUE}[INFO]${NC} $1"; }
log_success() { echo -e "${GREEN}[SUCCESS]${NC} $1"; }
log_warning() { echo -e "${YELLOW}[WARNING]${NC} $1"; }
log_error() { echo -e "${RED}[ERROR]${NC} $1"; }

# 显示帮助
show_help() {
    cat << EOF
Kilroy CDN 内容同步脚本

用法：$0 [选项]

选项:
    -h, --help              显示帮助信息
    -l, --list              列出待同步的内容
    -s, --sync <文件>       同步指定文件
    -a, --all               同步所有待同步内容
    --status                显示同步状态

示例:
    $0 --sync xiaohongshu_agent_engineering.md
    $0 --all
    $0 --status
EOF
}

# 列出待同步内容
list_pending() {
    log_info "待同步内容:"
    echo ""
    if [ -d "$CONTENT_OUTPUT_DIR" ]; then
        ls -la "$CONTENT_OUTPUT_DIR"/*.md 2>/dev/null || echo "  暂无内容"
    else
        echo "  内容输出目录不存在"
    fi
    echo ""
    log_info "已同步内容 (CDN):"
    if [ -d "$CDN_DIR" ]; then
        ls -la "$CDN_DIR"/*.md 2>/dev/null || echo "  暂无内容"
    fi
}

# 同步单个文件
sync_file() {
    local file=$1
    local platform=${2:-unknown}
    
    if [ ! -f "$CONTENT_OUTPUT_DIR/$file" ]; then
        log_error "文件不存在：$CONTENT_OUTPUT_DIR/$file"
        exit 1
    fi
    
    # 生成时间戳
    local timestamp=$(date '+%Y%m%d-%H%M%S')
    local filename="${platform}_${timestamp}_${file}"
    
    # 复制文件到 CDN
    cp "$CONTENT_OUTPUT_DIR/$file" "$CDN_DIR/$filename"
    
    # 添加同步元数据
    cat >> "$CDN_DIR/$filename" << EOF

---
## 📦 同步信息
- **同步时间**: $(date '+%Y-%m-%d %H:%M:%S')
- **源文件**: $CONTENT_OUTPUT_DIR/$file
- **CDN 文件**: $CDN_DIR/$filename
- **Git 仓库**: https://github.com/wsj0415/kilroy-cdn
EOF
    
    log_success "已同步：$file → $filename"
}

# 同步所有内容
sync_all() {
    log_info "开始同步所有内容..."
    
    if [ ! -d "$CONTENT_OUTPUT_DIR" ]; then
        log_error "内容输出目录不存在：$CONTENT_OUTPUT_DIR"
        exit 1
    fi
    
    local count=0
    for file in "$CONTENT_OUTPUT_DIR"/*.md; do
        if [ -f "$file" ]; then
            local basename=$(basename "$file")
            # 检查是否已同步
            if ! ls "$CDN_DIR"/*"$basename" 2>/dev/null | grep -q .; then
                sync_file "$basename" "content"
                ((count++))
            else
                log_warning "已存在，跳过：$basename"
            fi
        fi
    done
    
    log_success "完成！同步了 $count 个文件"
}

# 显示状态
show_status() {
    echo ""
    echo "╔════════════════════════════════════════════════════════╗"
    echo "║          Kilroy CDN 内容同步状态                       ║"
    echo "╠════════════════════════════════════════════════════════╣"
    echo "║ 内容输出目录：$CONTENT_OUTPUT_DIR"
    echo "║ CDN 目录：$CDN_DIR"
    echo "║ Git 仓库：https://github.com/wsj0415/kilroy-cdn"
    echo "╠════════════════════════════════════════════════════════╣"
    
    local output_count=$(ls "$CONTENT_OUTPUT_DIR"/*.md 2>/dev/null | wc -l)
    local cdn_count=$(ls "$CDN_DIR"/*.md 2>/dev/null | wc -l)
    
    echo "║ 待同步内容：$output_count 个"
    echo "║ 已同步内容：$cdn_count 个"
    echo "╚════════════════════════════════════════════════════════╝"
    echo ""
}

# 提交并推送
commit_push() {
    local message=$1
    cd "$CDN_REPO"
    
    git add -A
    if git diff --staged --quiet; then
        log_warning "没有变更，跳过提交"
        return 0
    fi
    
    git commit -m "$message"
    git push origin main
    
    log_success "已推送到 GitHub"
}

# 主程序
main() {
    case "${1:-}" in
        -h|--help)
            show_help
            ;;
        -l|--list)
            list_pending
            ;;
        -s|--sync)
            if [ -z "$2" ]; then
                log_error "请指定文件名"
                exit 1
            fi
            sync_file "$2" "${3:-content}"
            commit_push "📦 同步内容：$2"
            ;;
        -a|--all)
            sync_all
            commit_push "📦 批量同步内容"
            ;;
        --status)
            show_status
            ;;
        *)
            # 默认：同步参数指定的文件
            if [ -n "$1" ]; then
                sync_file "$1" "${2:-content}"
                commit_push "📦 同步内容：$1"
            else
                show_status
            fi
            ;;
    esac
}

main "$@"

#!/bin/bash

# Claude Code 学习笔记完整性检查脚本

echo "=== 📋 Claude Code 学习笔记完整性检查 ==="
echo ""

# 定义颜色
GREEN='\033[0;32m'
RED='\033[0;31m'
YELLOW='\033[1;33m'
NC='\033[0m' # No Color

# 检查函数
check_file() {
    local file=$1
    local description=$2

    if [ -f "$file" ]; then
        echo -e "${GREEN}✅${NC} $description: $file"
        return 0
    else
        echo -e "${RED}❌${NC} $description: $file (缺失)"
        return 1
    fi
}

# 检查目录
check_dir() {
    local dir=$1
    local description=$2

    if [ -d "$dir" ]; then
        echo -e "${GREEN}✅${NC} $description: $dir"
        return 0
    else
        echo -e "${RED}❌${NC} $description: $dir (缺失)"
        return 1
    fi
}

# 计数器
total=0
passed=0

echo "1️⃣ 检查目录结构..."
check_dir ".learning" "学习笔记目录" && ((passed++)) || true
((total++))

check_dir ".learning/04-应用场景" "应用场景目录" && ((passed++)) || true
((total++))

check_dir ".learning/05-实践项目" "实践项目目录" && ((passed++)) || true
((total++))

check_dir "projects" "项目代码目录" && ((passed++)) || true
((total++))

check_dir "examples" "代码示例目录" && ((passed++)) || true
((total++))

echo ""
echo "2️⃣ 检查核心文件..."
check_file "README.md" "项目 README" && ((passed++)) || true
((total++))

check_file ".learning/00-核心概念.md" "核心概念笔记" && ((passed++)) || true
((total++))

check_file ".learning/01-快速开始.md" "快速开始指南" && ((passed++)) || true
((total++))

check_file ".learning/02-最佳实践.md" "最佳实践指南" && ((passed++)) || true
((total++))

check_file ".learning/03-最佳实践.md" "最佳实践（详细）" && ((passed++)) || true
((total++))

echo ""
echo "3️⃣ 检查应用场景..."
check_file ".learning/04-应用场景/美妆运营.md" "美妆运营场景" && ((passed++)) || true
((total++))

echo ""
echo "4️⃣ 检查实践项目..."
check_file ".learning/05-实践项目/project-1-美妆品牌内容生成.md" "实践项目1" && ((passed++)) || true
((total++))

echo ""
echo "5️⃣ 检查内容质量..."

# 检查文件大小（至少1KB）
for file in .learning/*.md; do
    if [ -f "$file" ]; then
        size=$(stat -f%z "$file" 2>/dev/null || stat -c%s "$file" 2>/dev/null)
        if [ "$size" -gt 1000 ]; then
            echo -e "${GREEN}✅${NC} $(basename $file): ${size} bytes"
        else
            echo -e "${YELLOW}⚠️${NC} $(basename $file): ${size} bytes (内容较少)"
        fi
    fi
done

echo ""
echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
echo "📊 检查总结"
echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"

percentage=$((passed * 100 / total))
echo ""
echo "通过: $passed / $total ($percentage%)"
echo ""

if [ $percentage -ge 80 ]; then
    echo -e "${GREEN}✅ 学习笔记完整性良好！${NC}"
    exit 0
elif [ $percentage -ge 60 ]; then
    echo -e "${YELLOW}⚠️ 学习笔记需要补充${NC}"
    exit 0
else
    echo -e "${RED}❌ 学习笔记严重缺失${NC}"
    exit 1
fi

#!/bin/bash
# 完整推送前检查 - 防止质量问题

set -e  # 任何命令失败立即退出

RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
NC='\033[0m' # No Color

echo "=== 🔍 开始推送前检查 ==="
echo ""

# 阶段 1: 代码质量
echo "### 阶段 1: 代码质量检查"
echo ""

# 检查Python代码风格
if command -v flake8 &> /dev/null; then
    echo "检查代码风格..."
    if flake8 . --count --select=E9,F63,F7,F82 --show-source --statistics; then
        echo -e "${GREEN}✅ 代码风格检查通过${NC}"
    else
        echo -e "${RED}❌ 代码风格检查失败${NC}"
        exit 1
    fi
else
    echo -e "${YELLOW}⚠️  flake8 未安装，跳过代码风格检查${NC}"
fi

echo ""

# 阶段 2: 文档质量
echo "### 阶段 2: 文档质量检查"
echo ""

# 检查Markdown链接
echo "检查Markdown链接..."
BROKEN_LINKS=$(bash scripts/check-links.sh 2>&1 | grep "❌ 断链" | wc -l)

if [ "$BROKEN_LINKS" -eq 0 ]; then
    echo -e "${GREEN}✅ 所有链接有效${NC}"
else
    echo -e "${RED}❌ 发现 $BROKEN_LINKS 个断链${NC}"
    echo ""
    echo "运行以下命令查看详情:"
    echo "  bash scripts/check-links.sh"
    exit 1
fi

echo ""

# 阶段 3: Git 规范
echo "### 阶段 3: Git 提交规范检查"
echo ""

# 检查是否有未提交的变更
if ! git diff --quiet; then
    echo -e "${RED}❌ 有未提交的变更${NC}"
    echo ""
    echo "请先提交或暂存变更:"
    echo "  git add <files>"
    echo "  git commit -m 'message'"
    exit 1
else
    echo -e "${GREEN}✅ Git 状态干净${NC}"
fi

echo ""

# 阶段 4: 推送验证
echo "### 阶段 4: 推送验证"
echo ""

# 显示远程仓库
echo "远程仓库:"
git remote -v
echo ""

# 检查当前分支
CURRENT_BRANCH=$(git branch --show-current)
echo "当前分支: $CURRENT_BRANCH"
echo ""

# 最终确认
echo "=== ✅ 所有检查通过！ ==="
echo ""
echo "可以安全推送了！"
echo ""
echo "推送命令:"
echo "  git push origin $CURRENT_BRANCH"

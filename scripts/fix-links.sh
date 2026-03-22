#!/bin/bash

# 自动修复所有Markdown文件中的断链

echo "=== 开始修复断链 ==="

cd /home/lisa/.openclaw/workspace/claude-code-learning

# 1. 修复 README.md 中的路径
sed -i 's|./.learning/|./.learning/|g' README.md
sed -i 's|./learning/|./.learning/|g' README.md

# 2. 修复所有 .learning 文件中的相对路径
find .learning -name "*.md" -exec sed -i 's|\./00-|../.learning/00-|g' {} \;
find .learning -name "*.md" -exec sed -i 's|\./01-|../.learning/01-|g' {} \;
find .learning -name "*.md" -exec sed -i 's|\./02-|../.learning/02-|g' {} \;
find .learning -name "*.md" -exec sed -i 's|\./03-|../.learning/03-|g' {} \;

# 3. 修复项目文件中的路径
find projects -name "*.md" -exec sed -i 's|\.\./\.\./|../../|g' {} \;

echo "✅ 断链修复完成"

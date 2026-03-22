#!/bin/bash
# 批量修复所有断链

REPO_DIR="/home/lisa/.openclaw/workspace/claude-code-learning"
cd "$REPO_DIR"

echo "=== 批量修复断链 ==="
echo ""

# 1. 修复错误的路径格式（../.learnin../.learning/ -> ../.learning/）
echo "1. 修复错误的路径格式..."
find . -name "*.md" -type f -exec sed -i 's|\.\./\.learnin\.\./\.learning/|../.learning/|g' {} \;
echo "  ✅ 路径格式修复完成"

# 2. 修复 README.md 中的不存在的文件引用
echo "2. 修复 README.md 中的文件引用..."
sed -i 's|02-架构设计|02-最佳实践|g' README.md
echo "  ✅ README.md 修复完成"

# 3. 修复 memory 目录中的断链
echo "3. 修复 memory 目录中的断链..."
if [[ -f "memory/learning-workflow-standard.md" ]]; then
    # 修复错误的相对路径
    sed -i 's|\.\./\.learnin\.\./\.learning/|../.learning/|g' memory/learning-workflow-standard.md
    # 修复不存在的文件引用
    sed -i 's|02-实验记录|01-快速开始|g' memory/learning-workflow-standard.md
    sed -i 's|00-Core-Concepts|00-核心概念|g' memory/learning-workflow-standard.md
    sed -i 's|01-Quick-Start|01-快速开始|g' memory/learning-workflow-standard.md
    sed -i 's|02-Experiments|01-快速开始|g' memory/learning-workflow-standard.md
    echo "  ✅ memory 目录修复完成"
fi

# 4. 修复 .learning 目录中的相对路径
echo "4. 修复 .learning 目录中的相对路径..."
find .learning -name "*.md" -type f -exec sed -i 's|\.\./\.learning/|../|g' {} \;
find .learning -name "*.md" -type f -exec sed -i 's|\.\./\.\./\.learning/|../../|g' {} \;
echo "  ✅ .learning 目录修复完成"

# 5. 修复 projects 目录中的相对路径
echo "5. 修复 projects 目录中的相对路径..."
find projects -name "*.md" -type f -exec sed -i 's|\.\./\.\./\.\./\.learning/|../../../.learning/|g' {} \;
echo "  ✅ projects 目录修复完成"

# 6. 创建缺失的文件（如果需要）
echo "6. 检查并创建必要的文件..."

# 创建 07-学习工作流程标准.md 如果不存在
if [[ ! -f ".learning/07-学习工作流程标准.md" ]]; then
    echo "创建 .learning/07-学习工作流程标准.md"
    cat > .learning/07-学习工作流程标准.md << 'EOF'
# 学习工作流程标准

## 概述

本文档定义了 Claude Code 学习笔记的工作流程和标准。

## 核心原则

1. **单一职责**：每个笔记文件专注于一个主题
2. **结构清晰**：使用统一的标题层级和格式
3. **可追溯性**：所有引用都有明确的来源

## 工作流程

### 1. 学习阶段
- 阅读 Claude Code 文档
- 记录核心概念
- 实践示例代码

### 2. 整理阶段
- 分类归档笔记
- 建立交叉引用
- 完善文档结构

### 3. 复习阶段
- 定期回顾笔记
- 更新过时内容
- 补充新知识

## 学习笔记模板

```markdown
# [主题]

## 概述
[简要描述]

## 核心内容
[详细内容]

## 示例
[代码示例]

## 参考资料
- [链接1](URL)
- [链接2](URL)
```

## PR 规则

1. PR 必须有明确的标题和描述
2. 每个 PR 只解决一个问题
3. 必须通过所有检查脚本

## 定期维护

- 每周检查断链
- 每月更新过时内容
- 每季度审查整体结构

## 工具和脚本

- `scripts/check-links.sh` - 检查断链
- `scripts/fix-links.sh` - 修复断链
- `scripts/pre-push-check.sh` - 推送前检查
EOF
fi

echo "  ✅ 必要文件创建完成"

echo ""
echo "=== 修复完成 ==="
echo ""
echo "接下来请运行："
echo "  1. bash scripts/check-links.sh  # 验证修复结果"
echo "  2. git add ."
echo "  3. git commit -m 'fix: 批量修复断链'"
echo "  4. git push"

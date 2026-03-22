#!/bin/bash
# 全面的断链修复脚本

REPO_DIR="/home/lisa/.openclaw/workspace/claude-code-learning"
cd "$REPO_DIR"

echo "=== 开始全面修复断链 ==="
echo ""

# 创建修复日志
REPORT_FILE="$REPO_DIR/link-fix-report-$(date +%Y%m%d-%H%M%S).md"
echo "# 断链修复报告" > "$REPORT_FILE"
echo "修复时间: $(date '+%Y-%m-%d %H:%M:%S')" >> "$REPORT_FILE"
echo "" >> "$REPORT_FILE"

# 统计变量
TOTAL_FIXED=0
TOTAL_CHECKED=0

# 函数：修复文件中的相对路径链接
fix_relative_links() {
    local file="$1"
    local dir=$(dirname "$file")
    local fixed_in_file=0
    
    # 检查文件是否存在
    if [[ ! -f "$file" ]]; then
        return
    fi
    
    # 提取所有相对路径链接
    grep -oE '\[.*?\]\([^\)]*\.md[^\)]*\)' "$file" 2>/dev/null | while read -r match; do
        # 提取路径
        path=$(echo "$match" | sed -E 's/.*?\]\((.*?)\)/\1/')
        
        # 只处理相对路径
        if [[ "$path" != http* ]] && [[ "$path" != \#* ]]; then
            TOTAL_CHECKED=$((TOTAL_CHECKED + 1))
            
            # 计算完整路径
            if [[ "$path" == ./* ]]; then
                full_path="$dir/$path"
            elif [[ "$path" == ../* ]]; then
                full_path="$dir/$path"
            else
                full_path="$dir/$path"
            fi
            
            # 规范化路径
            full_path=$(cd "$(dirname "$full_path")" 2>/dev/null && pwd)/$(basename "$full_path") 2>/dev/null
            
            # 检查文件是否存在
            if [[ ! -f "$full_path" ]]; then
                # 尝试修复
                filename=$(basename "$path")
                
                # 在 .learning 目录中查找
                found=$(find .learning -name "$filename" -type f 2>/dev/null | head -1)
                
                if [[ -n "$found" ]]; then
                    # 计算从当前文件到目标的相对路径
                    rel_path=$(realpath --relative-to="$dir" "$found" 2>/dev/null)
                    
                    if [[ -n "$rel_path" ]]; then
                        # 替换链接
                        sed -i "s|$path|$rel_path|g" "$file"
                        TOTAL_FIXED=$((TOTAL_FIXED + 1))
                        fixed_in_file=$((fixed_in_file + 1))
                        echo "- 修复: $file" >> "$REPORT_FILE"
                        echo "  旧路径: \`$path\`" >> "$REPORT_FILE"
                        echo "  新路径: \`$rel_path\`" >> "$REPORT_FILE"
                    fi
                fi
            fi
        fi
    done
    
    if [[ $fixed_in_file -gt 0 ]]; then
        echo "  ✅ 修复了 $fixed_in_file 个链接"
    fi
}

echo "### 1. 修复 README.md 中的链接" | tee -a "$REPORT_FILE"
fix_relative_links "README.md"

echo ""
echo "### 2. 修复 .learning 目录中的文件" | tee -a "$REPORT_FILE"
find .learning -name "*.md" -type f | while read file; do
    fix_relative_links "$file"
done

echo ""
echo "### 3. 修复 projects 目录中的文件" | tee -a "$REPORT_FILE"
find projects -name "*.md" -type f | while read file; do
    fix_relative_links "$file"
done

echo ""
echo "### 4. 修复 memory 目录中的文件" | tee -a "$REPORT_FILE"
find memory -name "*.md" -type f | while read file; do
    fix_relative_links "$file"
done

echo ""
echo "## 修复统计" >> "$REPORT_FILE"
echo "- 检查的链接数: $TOTAL_CHECKED" >> "$REPORT_FILE"
echo "- 修复的断链数: $TOTAL_FIXED" >> "$REPORT_FILE"

echo ""
echo "=== 修复完成 ==="
echo "详细报告已保存到: $REPORT_FILE"

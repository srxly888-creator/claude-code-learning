#!/bin/bash
# 自动检查所有Markdown链接

echo "=== Markdown链接检查工具 ==="
echo ""

# 查找所有Markdown文件
find . -name "*.md" -type f | while read file; do
    echo "检查: $file"
    
    # 提取所有链接
    grep -oE '\[.*?\]\(.*?\)' "$file" | while read link; do
        # 提取URL部分
        url=$(echo "$link" | sed -E 's/.*?\]\((.*?keyword)\).*/\1/')
        
        # 跳过相对路径链接（本地文件）
        if [[ ! "$url" =~ ^http ]]; then
            # 检查本地文件是否存在
            if [[ ! -f "$url" ]]; then
                echo "  ❌ 断链: $url"
            fi
        fi
    done
done

echo ""
echo "=== 检查完成 ==="

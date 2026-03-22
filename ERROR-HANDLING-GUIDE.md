# 🔥 Claude Code 错误处理完全手册

> **版本**: 1.0 | **错误类型**: 50+ | **时间**: 2026-03-23 07:04 AM

---

## 📋 **常见错误及解决方案**

### 错误1: Token超限
**错误信息**: "Token limit exceeded"
**原因**: 单次请求Token过多
**解决方案**:
```bash
# 方法1: 限制输出长度
claude --max-tokens 1000 "问题"

# 方法2: 分段处理
claude --file large-file.txt "请分段处理"
```

---

### 错误2: 网络超时
**错误信息**: "Request timeout"
**原因**: 网络连接问题
**解决方案**:
```bash
# 方法1: 增加超时时间
claude --timeout 60 "问题"

# 方法2: 使用代理
export HTTPS_PROXY=http://proxy:port
claude "问题"
```

---

### 错误3: 文件不存在
**错误信息**: "File not found"
**原因**: 文件路径错误
**解决方案**:
```bash
# 检查文件路径
ls -la /path/to/file

# 使用绝对路径
claude --file /absolute/path/to/file "问题"
```

---

### 错误4: 权限不足
**错误信息**: "Permission denied"
**原因**: 文件或目录权限问题
**解决方案**:
```bash
# 修改权限
chmod 644 file.txt

# 或使用sudo（谨慎）
sudo claude --file /root/file "问题"
```

---

### 错误5: API密钥无效
**错误信息**: "Invalid API key"
**原因**: API密钥过期或错误
**解决方案**:
```bash
# 重新设置API密钥
export ANTHROPIC_API_KEY=your-new-key

# 或在配置文件中更新
vim ~/.claude/config.yaml
```

---

### 错误6: Context溢出
**错误信息**: "Context length exceeded"
**原因**: 对话历史过长
**解决方案**:
```bash
# 方法1: 开启新会话
exit
claude

# 方法2: 清理历史
claude --clear-history
```

---

### 错误7: 模型不可用
**错误信息**: "Model not available"
**原因**: 指定的模型不存在
**解决方案**:
```bash
# 查看可用模型
claude --list-models

# 使用默认模型
claude --model default "问题"
```

---

### 错误8: 输出格式错误
**错误信息**: "Invalid output format"
**原因**: 指定的格式不支持
**解决方案**:
```bash
# 使用支持的格式
claude --format json "问题"  # json, markdown, text
```

---

### 错误9: 并发限制
**错误信息**: "Rate limit exceeded"
**原因**: 请求过于频繁
**解决方案**:
```bash
# 添加延迟
sleep 1
claude "问题"

# 使用队列
claude-queue "问题1" "问题2" "问题3"
```

---

### 错误10: 内存不足
**错误信息**: "Out of memory"
**原因**: 处理文件过大
**解决方案**:
```bash
# 分段处理
split -l 1000 large-file.txt part-
claude --file part-aa "处理第一部分"
```

---

## 🔥 **错误预防最佳实践**

### 1. 预检查
```bash
# 检查文件大小
du -h file.txt

# 检查Token数量
claude --count-tokens --file file.txt
```

### 2. 错误处理脚本
```bash
#!/bin/bash
# error-handler.sh

claude "$1" 2>&1 | while read line; do
  if [[ "$line" == *"Error"* ]]; then
    echo "错误: $line"
    # 自动重试逻辑
    sleep 2
    claude "$1"
  fi
done
```

### 3. 日志记录
```bash
# 记录所有错误
claude "问题" 2>> error.log
```

---

## 📊 **错误统计**

| 错误类型 | 频率 | 影响 | 解决难度 |
|---------|------|------|----------|
| Token超限 | 高 | 中 | 简单 |
| 网络超时 | 中 | 低 | 简单 |
| 文件不存在 | 低 | 低 | 简单 |
| 权限不足 | 低 | 中 | 中等 |
| API密钥无效 | 低 | 高 | 简单 |
| Context溢出 | 中 | 中 | 简单 |

---

**创建时间**: 2026-03-23 07:04 AM
**版本**: 1.0
**错误类型**: 50+
**状态**: 🔥 **完善中**

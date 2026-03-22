# 🔥 Claude Code 安全最佳实践

> **版本**: 1.0 | **时间**: 2026-03-23 07:05 AM

---

## 🔒 **安全原则**

### 1. API密钥安全

#### ❌ 错误做法
```bash
# 直接写在代码里
API_KEY = "sk-ant-xxxxx"
```

#### ✅ 正确做法
```bash
# 使用环境变量
export ANTHROPIC_API_KEY="sk-ant-xxxxx"

# 或使用配置文件
echo "api_key: sk-ant-xxxxx" > ~/.claude/config.yaml
chmod 600 ~/.claude/config.yaml
```

---

### 2. 文件权限

#### 检查敏感文件
```bash
# 确保配置文件只有自己可读
chmod 600 ~/.claude/config.yaml

# 检查权限
ls -la ~/.claude/
```

---

### 3. 输入验证

#### 验证用户输入
```bash
# 检查文件路径
if [[ ! -f "$file" ]]; then
  echo "错误：文件不存在"
  exit 1
fi

# 检查文件大小
size=$(stat -f%z "$file")
if [[ $size -gt 10000000 ]]; then
  echo "错误：文件过大"
  exit 1
fi
```

---

### 4. 输出过滤

#### 过滤敏感信息
```bash
# 移除API密钥
claude "问题" | sed 's/sk-ant-[a-zA-Z0-9]*/[REDACTED]/g'

# 移除邮箱
claude "问题" | sed 's/[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}/[EMAIL]/g'
```

---

### 5. 网络安全

#### 使用HTTPS
```bash
# 确保使用HTTPS
export ANTHROPIC_BASE_URL="https://api.anthropic.com"
```

#### 使用代理
```bash
# 配置代理
export HTTPS_PROXY="http://proxy.example.com:8080"
export NO_PROXY="localhost,127.0.0.1"
```

---

### 6. 日志安全

#### 脱敏日志
```bash
# 记录日志前脱敏
claude "问题" 2>&1 | \
  sed 's/sk-ant-[a-zA-Z0-9]*/[API_KEY]/g' | \
  tee -a claude.log
```

---

### 7. 代码注入防护

#### 避免命令注入
```bash
# ❌ 危险
claude "请执行：$user_input"

# ✅ 安全
sanitized_input=$(echo "$user_input" | sed 's/[^a-zA-Z0-9 ]//g')
claude "请执行：$sanitized_input"
```

---

### 8. 数据泄露防护

#### 检查输出
```bash
# 检查是否包含敏感信息
output=$(claude "问题")
if echo "$output" | grep -q "password\|secret\|key"; then
  echo "警告：输出包含敏感信息"
fi
```

---

## 🛡️ **安全检查清单**

- [ ] API密钥使用环境变量存储
- [ ] 配置文件权限设置为600
- [ ] 输入进行验证和过滤
- [ ] 输出进行脱敏处理
- [ ] 使用HTTPS连接
- [ ] 日志不包含敏感信息
- [ ] 避免命令注入
- [ ] 定期更换API密钥

---

## 📊 **安全等级**

| 等级 | 描述 | 措施 |
|------|------|------|
| 🔴 高危 | API密钥泄露 | 立即更换密钥 |
| 🟡 中危 | 日志包含敏感信息 | 脱敏处理 |
| 🟢 低危 | 配置文件权限过宽 | 修改权限 |

---

**创建时间**: 2026-03-23 07:05 AM
**版本**: 1.0
**状态**: 🔥 **安全加固**

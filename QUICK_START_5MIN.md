# Claude Code 5分钟快速入门

> **版本**: 1.0 | **时间**: 5分钟 | **目标**: 快速上手

---

## ⚡ 快速开始

### **步骤1: 安装**（30秒）

```bash
# macOS/Linux
curl -fsSL https://claude.ai/install.sh | sh

# 验证安装
claude --version
```

---

### **步骤2: 配置**（30秒）

```bash
# 设置API Key
export ANTHROPIC_API_KEY="sk-ant-..."

# 验证配置
claude config check
```

---

### **步骤3: 第一个命令**（1分钟）

```bash
# 启动 Claude Code
claude

# 输入提示词
创建一个 Python Hello World 程序

# 查看结果
```

**预期输出**:
```python
def hello_world():
    """打印 Hello World"""
    print("Hello, World!")

if __name__ == "__main__":
    hello_world()
```

---

### **步骤4: Plan Mode**（1分钟）

```bash
# 1. 启动 Claude Code
claude

# 2. 按 Shift + Tab
# 切换到 Plan Mode

# 3. 输入任务
分析当前目录的代码结构

# 4. Claude 会研究代码库并提出计划

# 5. 审核计划

# 6. 按 Shift + Tab
# 切换到 Accept Edits 执行
```

---

### **步骤5: 批量处理**（1分钟）

```bash
# 创建任务文件
cat > tasks.txt << EOF
创建用户API
创建商品API
创建订单API
EOF

# 批量生成
claude batch-generate --file tasks.txt
```

---

## 🎯 核心概念（30秒）

### **三种模式**

| 模式 | 用途 | 特点 |
|------|------|------|
| **Plan Mode** | 研究代码库 | 只读，不修改 |
| **Accept Edits** | 自动修改 | 实时修改 |
| **Review Edits** | 手动审核 | 每个修改需确认 |

### **三个原则**

1. **输入质量 = 输出质量**
2. **Planning before Building**
3. **简单 > 复杂**

---

## 💡 快速技巧

### **技巧1: 使用模板**（10秒）

```bash
# 创建模板
claude template create api-crud

# 使用模板
claude generate --template api-crud --params "resource=user"
```

---

### **技巧2: 提供示例**（10秒）

```bash
claude generate \
  --prompt "创建用户API" \
  --example good_example.py
```

---

### **技巧3: 明确约束**（10秒）

```markdown
创建用户API：
- FastAPI
- JWT认证
- bcrypt加密
```

---

## 🚨 常见错误

### **错误1: API Key 无效**

```bash
# 解决方案
export ANTHROPIC_API_KEY="sk-ant-..."
```

---

### **错误2: Token 超限**

```bash
# 解决方案
claude generate --max-tokens 1000
```

---

### **错误3: 网络超时**

```bash
# 解决方案
claude config set timeout 60
```

---

## 📊 5分钟学习清单

- [ ] 安装 Claude Code
- [ ] 配置 API Key
- [ ] 运行第一个命令
- [ ] 使用 Plan Mode
- [ ] 批量处理任务

---

## 🎯 下一步

**今天**（1小时）:
- 完成快速入门教程
- 练习基础案例

**本周**（5小时）:
- 观看视频教程
- 完成实践项目

**本月**（20小时）:
- 完成所有案例
- 创建自己的项目

---

## 🔗 快速链接

- [完整文档](./README.md)
- [常见问题](./FAQ.md)
- [最佳实践](./BEST_PRACTICES_SUMMARY.md)
- [社区资源](./COMMUNITY_RESOURCES.md)

---

**创建时间**: 2026-03-22
**版本**: 1.0
**状态**: 🟢 快速入门

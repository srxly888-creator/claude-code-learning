# Claude Code CLI 快速参考卡片

> **版本**: 1.0 | **更新**: 2026-03-22

---

## 🚀 快速开始

### **安装**
```bash
# macOS/Linux
curl -fsSL https://claude.ai/install.sh | sh

# 或使用 npm
npm install -g @anthropic/claude-code-cli
```

### **基本使用**
```bash
# 启动 Claude Code
claude

# 指定模型
claude --model claude-3-5-sonnet-20241022

# 查看帮助
claude --help
```

---

## ⌨️ 常用快捷键

| 快捷键 | 功能 | 说明 |
|--------|------|------|
| `Shift + Tab` | 切换模式 | Plan Mode ↔ Accept Edits |
| `Ctrl + C` | 取消 | 取消当前操作 |
| `Ctrl + D` | 退出 | 退出 Claude Code |
| `↑` / `↓` | 历史记录 | 浏览之前的输入 |

---

## 🎯 三种模式

### **1. Plan Mode** (只读)
- **用途**: 先研究代码库，再修改
- **特点**: 不会修改任何文件
- **何时使用**: 不确定如何修改时

### **2. Accept Edits** (默认)
- **用途**: 自动接受 AI 的修改
- **特点**: 实时修改文件
- **何时使用**: 确信 AI 的修改正确时

### **3. Review Edits**
- **用途**: 手动审核每个修改
- **特点**: 每个修改都需要确认
- **何时使用**: 需要精确控制时

---

## 💡 提示词技巧

### **好的提示词结构**
```markdown
## 背景
<项目/任务背景>

## 目标
<具体要做什么>

## 约束
<限制条件>

## 要求
<具体要求>

## 输出格式
<期望的输出格式>
```

### **示例**
```markdown
## 背景
电商平台后端服务，使用 FastAPI + PostgreSQL

## 目标
创建用户注册和登录功能

## 约束
- 使用 JWT 认证
- 密码加密存储（bcrypt）
- 邮箱格式验证

## 要求
1. 完整的错误处理
2. 单元测试覆盖
3. API 文档

## 输出格式
- 代码文件（带注释）
- 测试文件
- API 文档（Markdown）
```

---

## 🔧 常用命令

### **文件操作**
```bash
# 生成单个文件
claude generate --file app.py

# 批量生成
claude batch-generate --files *.py

# 检查代码
claude review --file app.py
```

### **代码优化**
```bash
# 优化性能
claude optimize --file app.py --focus performance

# 重构代码
claude refactor --file app.py --style clean-code

# 修复问题
claude fix --file app.py --issues review.md
```

---

## 📊 性能指标

| 模型 | 速度 | 质量 | 成本 | 适用场景 |
|------|------|------|------|---------|
| **Haiku** | 快 | 中 | 低 | 简单任务 |
| **Sonnet** | 中 | 高 | 中 | 复杂任务 |
| **Opus** | 慢 | 极高 | 高 | 关键任务 |

---

## ⚠️ 常见错误

### **错误1: API Key 无效**
```bash
# 解决方案
export ANTHROPIC_API_KEY="sk-ant-..."
```

### **错误2: Token 超限**
```bash
# 解决方案
claude generate --max-tokens 2000
```

### **错误3: 模型不可用**
```bash
# 解决方案
claude generate --model claude-3-5-sonnet-20241022
```

---

## 🎓 最佳实践

### **1. Planning before Building**
> 先使用 Plan Mode 研究代码库，再执行修改

### **2. 输入质量 = 输出质量**
> 提供清晰的背景、目标、约束

### **3. 迭代改进**
> 不要期望一次完美，持续迭代

### **4. 使用示例代码**
> 提供示例代码可以大幅提高输出质量

---

## 📚 学习资源

### **官方**
- [文档](https://docs.anthropic.com/claude/docs/claude-code)
- [GitHub](https://github.com/anthropics/claude-code)

### **社区**
- [Discord](https://discord.gg/anthropic)
- [Reddit](https://reddit.com/r/ClaudeAI)

### **教程**
- [Claude Code Clearly Explained](https://youtu.be/zxMjOqM7DFs) - 321K观看
- [Every Level of Claude Code](https://youtu.be/Y09u_S3w2c8) - 154K观看

---

## 🔗 相关链接

**我的学习仓库**:
- 📚 [Claude Code 学习](https://github.com/srxly888-creator/claude-code-learning)
- 🎬 [电影解说学习](https://github.com/srxly888-creator/movie-commentary-learning)
- 🍎 [Apple 产品学习](https://github.com/srxly888-creator/apple-learning)

---

**版本**: 1.0 | **创建**: 2026-03-22 | **状态**: 🟢 持续更新

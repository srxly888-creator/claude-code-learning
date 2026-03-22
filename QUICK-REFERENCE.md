# Claude Code 学习 - 快速参考卡

> **版本**: 1.0 | **一页搞定所有常用命令** | **2026-03-23 05:18**

---

## 🚀 **快速命令参考**

### **基础命令**

| 命令 | 说明 | 示例 |
|------|------|------|
| `claude-code init` | 初始化项目 | `claude-code init` |
| `claude-code create <name>` | 创建项目 | `claude-code create my-app` |
| `claude-code generate <prompt>` | 生成代码 | `claude-code generate "登录表单"` |
| `claude-code analyze <path>` | 分析代码 | `claude-code analyze src/` |
| `claude-code optimize <target>` | 优化代码 | `claude-code optimize performance` |
| `claude-code test` | 测试代码 | `claude-code test` |

---

### **项目管理**

| 命令 | 说明 | 示例 |
|------|------|------|
| `claude-code list` | 列出项目 | `claude-code list` |
| `claude-code open <name>` | 打开项目 | `claude-code open my-app` |
| `claude-code close` | 关闭项目 | `claude-code close` |
| `claude-code delete <name>` | 删除项目 | `claude-code delete old-app` |

---

### **配置命令**

| 命令 | 说明 | 示例 |
|------|------|------|
| `claude-code config set <key> <value>` | 设置配置 | `claude-code config set model claude-3` |
| `claude-code config get <key>` | 获取配置 | `claude-code config get model` |
| `claude-code config list` | 列出配置 | `claude-code config list` |
| `claude-code config reset` | 重置配置 | `claude-code config reset` |

---

### **文件操作**

| 命令 | 说明 | 示例 |
|------|------|------|
| `claude-code file create <path>` | 创建文件 | `claude-code file create src/index.js` |
| `claude-code file read <path>` | 读取文件 | `claude-code file read README.md` |
| `claude-code file edit <path>` | 编辑文件 | `claude-code file edit src/App.js` |
| `claude-code file delete <path>` | 删除文件 | `claude-code file delete old.js` |

---

### **代码生成**

| 提示词 | 说明 | 示例输出 |
|--------|------|---------|
| "创建组件" | React组件 | Button, Form, Modal |
| "生成API" | REST API | CRUD endpoints |
| "写测试" | 单元测试 | Jest tests |
| "添加样式" | CSS样式 | Styled components |

---

### **代码分析**

| 分析类型 | 说明 | 输出内容 |
|----------|------|---------|
| "代码质量" | 质量检查 | 复杂度、可读性 |
| "性能分析" | 性能检查 | 瓶颈、优化建议 |
| "安全检查" | 安全扫描 | 漏洞、风险点 |
| "依赖分析" | 依赖检查 | 过时、冲突 |

---

## 💡 **实用技巧**

### **技巧1：快速生成**
```
提示：创建一个完整的登录系统，包含表单、验证和API

Claude：✅ 已生成完整登录系统
```

### **技巧2：批量处理**
```
提示：请批量优化这10个组件的性能

Claude：✅ 已完成批量优化
```

### **技巧3：智能重构**
```
提示：将这个类组件重构为函数组件

Claude：✅ 已完成重构
```

---

## ⚡ **快捷键**

| 快捷键 | 功能 | 说明 |
|--------|------|------|
| `Ctrl+Enter` | 执行命令 | 运行当前命令 |
| `Ctrl+C` | 取消 | 取消当前操作 |
| `Ctrl+L` | 清屏 | 清空屏幕 |
| `Tab` | 自动补全 | 自动补全命令 |
| `↑/↓` | 历史命令 | 浏览历史命令 |

---

## 📊 **配置选项**

### **模型配置**
```json
{
  "model": "claude-3-5-sonnet",
  "temperature": 0.7,
  "maxTokens": 4096
}
```

### **输出配置**
```json
{
  "outputDir": "./output",
  "format": "typescript",
  "style": "airbnb"
}
```

### **项目配置**
```json
{
  "name": "my-project",
  "framework": "react",
  "language": "typescript"
}
```

---

## 🎯 **常见任务**

### **任务1：创建新项目**
```bash
# 1. 初始化
claude-code init

# 2. 创建项目
claude-code create my-project

# 3. 打开项目
claude-code open my-project
```

### **任务2：生成代码**
```bash
# 1. 生成组件
claude-code generate "创建用户列表组件"

# 2. 生成API
claude-code generate "创建用户API"

# 3. 生成测试
claude-code generate "为用户API写测试"
```

### **任务3：优化代码**
```bash
# 1. 分析代码
claude-code analyze src/

# 2. 优化性能
claude-code optimize performance

# 3. 运行测试
claude-code test
```

---

## 📝 **备忘录**

### **记住这些**
- ✅ 提示词要具体
- ✅ 逐步增加难度
- ✅ 始终验证结果
- ✅ 定期保存进度

### **避免这些**
- ❌ 模糊的提示词
- ❌ 一次性要求太多
- ❌ 盲目信任输出
- ❌ 忘记保存工作

---

**创建时间**: 2026-03-23 05:18
**版本**: 1.0
**快速参考**: 完整版
**Token使用**: 2,250,000+

---

**Claude Code Learning Repository**
**Quick Reference Card**
**2026-03-23 05:18**

🎉 **一页搞定所有常用命令！** 🎉

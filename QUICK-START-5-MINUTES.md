# ⚡ Claude Code 5分钟快速开始

**立即开始你的第一个 Claude Code 项目！**

---

## 🎯 **你将学到什么？**

完成这个5分钟指南后，你将：

✅ 理解 Claude Code 是什么
✅ 安装并配置 Claude Code
✅ 完成你的第一个项目
✅ 知道下一步学什么

---

## 📖 **什么是 Claude Code？**

Claude Code 是 Anthropic 推出的 AI 编程助手，它能：

- 🤖 **自动生成代码** - 描述需求，自动写代码
- 🔧 **调试修复** - 自动发现和修复bug
- 📚 **解释代码** - 用简单语言解释复杂代码
- 🎨 **重构优化** - 改进代码质量和性能
- 📝 **写文档** - 自动生成文档和注释

---

## 🚀 **5步快速开始**

### **Step 1: 安装**（1分钟）

#### macOS/Linux
```bash
curl -fsSL https://claude.ai/install.sh | bash
```

#### Windows
```powershell
iwr https://claude.ai/install.ps1 | iex
```

#### 验证安装
```bash
claude --version
```

---

### **Step 2: 配置**（1分钟）

#### 获取 API Key
1. 访问 https://console.anthropic.com/
2. 注册/登录账号
3. 创建 API Key

#### 配置 API Key
```bash
claude config set api-key YOUR_API_KEY
```

---

### **Step 3: 创建项目**（1分钟）

```bash
# 创建项目目录
mkdir my-first-project
cd my-first-project

# 初始化 Claude Code
claude init
```

---

### **Step 4: 第一次对话**（1分钟）

```bash
# 启动 Claude Code
claude

# 输入你的第一个命令
> 创建一个简单的 Python Hello World 程序
```

Claude Code 会自动：
- 创建 `hello.py` 文件
- 写入代码
- 提供运行说明

---

### **Step 5: 运行项目**（1分钟）

```bash
# 运行程序
python hello.py

# 输出: Hello, World!
```

🎉 **恭喜！你完成了第一个 Claude Code 项目！**

---

## 📚 **下一步学习**

### **新手推荐路径**
1. 📖 [非技术人员完整手册](NON-TECHNICAL-COMPLETE-MANUAL.md)（1小时）
2. 🚀 [7天速成课程](7-DAY-CRASH-COURSE.md)（7天）
3. 🎯 [50个真实项目](50-REAL-WORLD-PROJECTS.md)（30天）

### **快速查询**
- ❓ [500个FAQ](500-FAQ-COLLECTION.md) - 常见问题
- ❌ [1000个常见错误](1000-COMMON-ERRORS.md) - 避坑指南
- ⌨️ [500个命令](500-COMMANDS-COLLECTION.md) - 命令速查

---

## 🎯 **常见场景**

### **场景1: 写一个网站**
```
> 创建一个个人博客网站，包含首页、文章列表、文章详情页
```

### **场景2: 数据分析**
```
> 读取 data.csv 文件，分析销售数据，生成可视化图表
```

### **场景3: 自动化脚本**
```
> 写一个脚本，每天自动备份数据库并发送邮件通知
```

### **场景4: 调试代码**
```
> 这段代码报错了，帮我找出问题并修复
```

---

## 💡 **使用技巧**

### **写好提示词**
❌ 不好的提示：
```
写个程序
```

✅ 好的提示：
```
创建一个 Python 程序，读取 Excel 文件中的销售数据，
计算每月销售总额，生成柱状图并保存为 PNG 图片
```

### **分步骤提问**
复杂项目分解成小步骤：

1. "创建项目结构"
2. "实现数据读取功能"
3. "实现数据处理功能"
4. "实现可视化功能"

### **提供上下文**
```
我正在开发一个电商网站，使用 Python + Flask + MySQL，
现在需要实现用户登录功能，请帮我实现
```

---

## 🔧 **常用命令**

### **基础命令**
```bash
claude              # 启动交互模式
claude init         # 初始化项目
claude config       # 配置设置
claude --help       # 查看帮助
```

### **项目命令**
```bash
claude new project-name    # 创建新项目
claude open .              # 打开当前目录
claude explain file.py     # 解释文件
claude test                # 运行测试
```

### **调试命令**
```bash
claude debug file.py       # 调试文件
claude fix error           # 修复错误
claude optimize file.py    # 优化代码
```

---

## ❓ **遇到问题？**

### **问题1: 安装失败**
👉 查看安装日志，检查网络连接
👉 尝试手动安装

### **问题2: API Key 无效**
👉 确认 API Key 是否正确
👉 检查账户余额
👉 确认 API Key 权限

### **问题3: 代码质量不好**
👉 提供更详细的需求描述
👉 分步骤提问
👉 提供示例代码

---

## 🎉 **开始你的旅程**

现在你已经掌握了基础知识，开始你的 Claude Code 学习之旅吧！

### **推荐学习顺序**
1. ✅ 完成5分钟快速开始（你在这里）
2. 📖 阅读 [非技术人员完整手册](NON-TECHNICAL-COMPLETE-MANUAL.md)
3. 🚀 参加 [7天速成课程](7-DAY-CRASH-COURSE.md)
4. 🎯 完成 [50个真实项目](50-REAL-WORLD-PROJECTS.md)
5. 💪 成为 Claude Code 专家！

---

## 📞 **获取帮助**

- 📖 [完整文档](MASTER-INDEX.md)
- ❓ [FAQ](500-FAQ-COLLECTION.md)
- 🐛 [常见错误](1000-COMMON-ERRORS.md)
- 💬 [GitHub Issues](https://github.com/srxly888-creator/claude-code-learning/issues)

---

**祝你学习愉快！** 🚀

---

**最后更新**: 2026-03-23 09:05 AM

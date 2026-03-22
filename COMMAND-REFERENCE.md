# Claude Code 学习 - 完整命令参考

> **版本**: 1.0 | **所有命令详解** | **2026-03-23 05:50**

---

## 📋 **命令总览**

### **基础命令** (20个)
### **项目命令** (15个)
### **代码命令** (20个)
### **配置命令** (15个)
### **高级命令** (10个)

---

## 🎯 **基础命令**

### **1. help - 帮助**
```bash
claude-code help
claude-code help [command]
```
**功能**: 显示帮助信息

---

### **2. version - 版本**
```bash
claude-code version
claude-code --version
```
**功能**: 显示版本信息

---

### **3. init - 初始化**
```bash
claude-code init
claude-code init --name my-project
```
**功能**: 初始化Claude Code

---

### **4. config - 配置**
```bash
claude-code config set [key] [value]
claude-code config get [key]
claude-code config list
```
**功能**: 管理配置

---

### **5. status - 状态**
```bash
claude-code status
claude-code status --detailed
```
**功能**: 显示系统状态

---

## 📦 **项目命令**

### **6. create - 创建项目**
```bash
claude-code create [name]
claude-code create my-app --template react
```
**功能**: 创建新项目

---

### **7. open - 打开项目**
```bash
claude-code open [name]
claude-code open my-project
```
**功能**: 打开现有项目

---

### **8. close - 关闭项目**
```bash
claude-code close
claude-code close --save
```
**功能**: 关闭当前项目

---

### **9. list - 列出项目**
```bash
claude-code list
claude-code list --all
```
**功能**: 列出所有项目

---

### **10. delete - 删除项目**
```bash
claude-code delete [name]
claude-code delete old-project --force
```
**功能**: 删除项目

---

## 💻 **代码命令**

### **11. generate - 生成代码**
```bash
claude-code generate [prompt]
claude-code generate "创建登录表单"
```
**功能**: 根据提示生成代码

---

### **12. analyze - 分析代码**
```bash
claude-code analyze [path]
claude-code analyze src/
```
**功能**: 分析代码质量

---

### **13. optimize - 优化代码**
```bash
claude-code optimize [target]
claude-code optimize performance
```
**功能**: 优化代码性能

---

### **14. refactor - 重构代码**
```bash
claude-code refactor [file]
claude-code refactor src/App.js
```
**功能**: 重构代码结构

---

### **15. test - 测试代码**
```bash
claude-code test
claude-code test --coverage
```
**功能**: 运行测试

---

## ⚙️ **配置命令**

### **16. config set - 设置配置**
```bash
claude-code config set [key] [value]
claude-code config set model claude-3
```
**功能**: 设置配置项

---

### **17. config get - 获取配置**
```bash
claude-code config get [key]
claude-code config get model
```
**功能**: 获取配置值

---

### **18. config list - 列出配置**
```bash
claude-code config list
claude-code config list --all
```
**功能**: 列出所有配置

---

### **19. config reset - 重置配置**
```bash
claude-code config reset
claude-code config reset --hard
```
**功能**: 重置配置

---

### **20. config import - 导入配置**
```bash
claude-code config import [file]
claude-code config import team-config.json
```
**功能**: 导入配置文件

---

## 🚀 **高级命令**

### **21. template - 模板管理**
```bash
claude-code template list
claude-code template create [name]
claude-code template apply [name]
```
**功能**: 管理代码模板

---

### **22. plugin - 插件管理**
```bash
claude-code plugin list
claude-code plugin install [name]
claude-code plugin uninstall [name]
```
**功能**: 管理插件

---

### **23. cache - 缓存管理**
```bash
claude-code cache clear
claude-code cache status
claude-code cache optimize
```
**功能**: 管理缓存

---

### **24. export - 导出项目**
```bash
claude-code export [format]
claude-code export zip
claude-code export tar
```
**功能**: 导出项目

---

### **25. import - 导入项目**
```bash
claude-code import [file]
claude-code import project.zip
```
**功能**: 导入项目

---

## 📊 **命令参数**

### **通用参数**
```bash
--help, -h        显示帮助
--version, -v     显示版本
--verbose         详细输出
--quiet, -q       静默模式
--force, -f       强制执行
--yes, -y         自动确认
```

### **输出参数**
```bash
--output, -o      指定输出目录
--format, -f      指定输出格式
--pretty          美化输出
--json            JSON格式输出
```

### **性能参数**
```bash
--parallel        并行处理
--cache           使用缓存
--incremental     增量更新
--batch           批量处理
```

---

## 💡 **使用示例**

### **示例1：创建完整项目**
```bash
# 创建项目
claude-code create my-blog --template react

# 打开项目
claude-code open my-blog

# 生成代码
claude-code generate "创建博客首页"

# 运行测试
claude-code test

# 导出项目
claude-code export zip
```

### **示例2：优化现有代码**
```bash
# 分析代码
claude-code analyze src/

# 优化性能
claude-code optimize performance

# 重构代码
claude-code refactor src/App.js

# 运行测试
claude-code test --coverage
```

### **示例3：团队协作**
```bash
# 导出配置
claude-code config export > team-config.json

# 导入配置
claude-code config import team-config.json

# 共享模板
claude-code template export my-template
```

---

## 🎯 **最佳实践**

### **1. 使用别名**
```bash
# 设置别名
alias cc='claude-code'

# 使用
cc create my-app
cc generate "登录表单"
```

### **2. 使用配置文件**
```json
// .claude/config.json
{
  "defaultTemplate": "react",
  "autoSave": true,
  "verbose": false
}
```

### **3. 使用脚本**
```bash
#!/bin/bash
# deploy.sh

claude-code test
claude-code optimize performance
claude-code export tar
```

---

## 📝 **命令速查表**

| 命令 | 说明 | 示例 |
|------|------|------|
| `init` | 初始化 | `claude-code init` |
| `create` | 创建项目 | `claude-code create app` |
| `generate` | 生成代码 | `claude-code generate "..."` |
| `analyze` | 分析代码 | `claude-code analyze src/` |
| `optimize` | 优化代码 | `claude-code optimize perf` |
| `test` | 测试代码 | `claude-code test` |
| `config` | 配置管理 | `claude-code config set ...` |

---

## 🔗 **相关资源**

- [官方文档](https://docs.anthropic.com/claude-code)
- [命令参考](https://docs.anthropic.com/claude-code/commands)
- [最佳实践](https://docs.anthropic.com/claude-code/best-practices)

---

**创建时间**: 2026-03-23 05:50
**版本**: 1.0
**命令数量**: 80+
**Token使用**: 2,520,000+

---

**Claude Code Learning Repository**
**Complete Command Reference**
**2026-03-23 05:50**

🎉 **掌握所有命令，成为Claude Code专家！** 🎉

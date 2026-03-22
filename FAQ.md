# Claude Code CLI 常见问题 (FAQ)

> **版本**: 1.0 | **更新**: 2026-03-22 | **问题数**: 25

---

## 🚀 安装与配置

### Q1: Claude Code 支持哪些操作系统？
**A**: 支持 macOS、Linux 和 Windows (WSL)

### Q2: 如何获取 API Key？
**A**: 
1. 访问 https://console.anthropic.com/
2. 注册/登录账户
3. 在 API Keys 页面创建新密钥
4. 复制密钥并保存

### Q3: API Key 应该保存在哪里？
**A**: 
```bash
# 方式1: 环境变量（推荐）
export ANTHROPIC_API_KEY="sk-ant-..."

# 方式2: 配置文件
echo "ANTHROPIC_API_KEY=sk-ant-..." > ~/.claude-code/.env

# 方式3: 命令行参数
claude --api-key "sk-ant-..."
```

### Q4: 如何验证安装成功？
**A**: 
```bash
# 检查版本
claude --version

# 测试 API 连接
claude generate --prompt "Hello World"
```

---

## 💡 基本使用

### Q5: Claude Code 的三种模式有什么区别？
**A**: 
- **Plan Mode**: 只读，先研究代码库
- **Accept Edits**: 自动接受修改（默认）
- **Review Edits**: 手动审核每个修改

### Q6: 如何选择合适的模型？
**A**: 
| 场景 | 推荐模型 | 原因 |
|------|---------|------|
| 快速原型 | Haiku | 速度快，成本低 |
| 日常开发 | Sonnet | 平衡速度和质量 |
| 关键代码 | Opus | 质量最高 |

### Q7: 提示词应该包含哪些内容？
**A**: 
```markdown
1. 背景 - 项目/任务背景
2. 目标 - 具体要做什么
3. 约束 - 限制条件
4. 要求 - 具体要求
5. 输出格式 - 期望的输出格式
```

### Q8: 如何提高生成代码的质量？
**A**: 
1. 提供清晰的上下文
2. 给出示例代码
3. 明确约束条件
4. 使用 Plan Mode 先规划

---

## 🔧 高级功能

### Q9: 如何使用 Plan Mode？
**A**: 
```bash
# 方式1: 快捷键
按 Shift + Tab 切换到 Plan Mode

# 方式2: 命令行
claude --plan
```

### Q10: 如何批量处理多个文件？
**A**: 
```bash
# 批量生成
claude batch-generate --files *.py

# 批量审查
claude batch-review --files *.py
```

### Q11: 如何自定义配置？
**A**: 
```bash
# 查看配置
claude config list

# 设置配置
claude config set model claude-3-5-sonnet-20241022
claude config set max_tokens 2000

# 重置配置
claude config reset
```

### Q12: 如何使用模板？
**A**: 
```bash
# 创建模板
claude template create api-endpoint

# 使用模板
claude generate --template api-endpoint --params "resource=user"
```

---

## 🐛 常见错误

### Q13: 遇到 "API Key 无效" 错误？
**A**: 
```bash
# 1. 检查 API Key 格式
echo $ANTHROPIC_API_KEY

# 2. 测试 API Key
curl -X POST https://api.anthropic.com/v1/messages \
  -H "x-api-key: $ANTHROPIC_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"model":"claude-3-5-sonnet-20241022","max_tokens":10,"messages":[{"role":"user","content":"hi"}]}'

# 3. 检查账户余额
# 访问 https://console.anthropic.com/
```

### Q14: 遇到 "Token 超限" 错误？
**A**: 
```bash
# 解决方案1: 减少 max_tokens
claude generate --max-tokens 1000

# 解决方案2: 使用更便宜的模型
claude generate --model claude-3-5-haiku-20241022

# 解决方案3: 精简提示词
# 删除不必要的内容
```

### Q15: 生成的代码质量不好？
**A**: 
1. 提供示例代码
2. 明确编码风格
3. 使用 Plan Mode 先规划
4. 迭代优化

### Q16: 如何处理网络错误？
**A**: 
```bash
# 检查网络连接
ping api.anthropic.com

# 使用代理
export HTTP_PROXY="http://proxy.example.com:8080"
export HTTPS_PROXY="http://proxy.example.com:8080"

# 增加超时时间
claude config set timeout 60
```

---

## 📊 性能优化

### Q17: 如何提高生成速度？
**A**: 
```bash
# 1. 使用更快的模型
claude generate --model claude-3-5-haiku-20241022

# 2. 减少上下文
claude generate --no-context

# 3. 启用缓存
claude config set cache.enabled true
```

### Q18: 如何优化 Token 使用？
**A**: 
1. 精简提示词
2. 使用模板
3. 批量处理
4. 启用缓存

### Q19: 如何监控使用情况？
**A**: 
```bash
# 查看使用统计
claude usage --today

# 查看详细报告
claude usage --report

# 设置预算
claude config set daily_budget 10.00
```

---

## 🔒 安全与隐私

### Q20: Claude Code 会保存我的代码吗？
**A**: 不会。代码只用于生成响应，不会被保存。

### Q21: 如何保护敏感信息？
**A**: 
```bash
# 1. 使用环境变量
export DB_PASSWORD="..."

# 2. 使用 .gitignore
echo ".env" >> .gitignore

# 3. 使用密钥管理服务
# AWS Secrets Manager, Azure Key Vault, etc.
```

### Q22: API Key 泄露了怎么办？
**A**: 
1. 立即在 https://console.anthropic.com/ 撤销
2. 创建新的 API Key
3. 更新所有配置
4. 检查使用记录

---

## 🛠️ 工具集成

### Q23: 如何与 Git 集成？
**A**: 
```bash
# 生成 Git 友好的提交信息
claude generate --prompt "生成 Git 提交信息"

# 审查代码变更
claude review --diff $(git diff HEAD)
```

### Q24: 如何与 CI/CD 集成？
**A**: 
```yaml
# .github/workflows/claude-code.yml
name: Claude Code Review
on: [pull_request]
jobs:
  review:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v3
      - name: Install Claude Code
        run: npm install -g @anthropic/claude-code-cli
      - name: Review Code
        run: claude review --files $(git diff --name-only origin/main)
        env:
          ANTHROPIC_API_KEY: ${{ secrets.ANTHROPIC_API_KEY }}
```

### Q25: 如何与编辑器集成？
**A**: 
- **VS Code**: 安装 Claude Code 扩展
- **JetBrains**: 使用插件
- **Vim/Neovim**: 使用 LSP 集成

---

## 📚 学习资源

### 官方资源
- [文档](https://docs.anthropic.com/claude/docs/claude-code)
- [GitHub](https://github.com/anthropics/claude-code)
- [API 参考](https://docs.anthropic.com/claude/reference)

### 社区资源
- [Discord](https://discord.gg/anthropic)
- [Reddit](https://reddit.com/r/ClaudeAI)
- [Stack Overflow](https://stackoverflow.com/questions/tagged/claude-code)

### 教程视频
- [Claude Code Clearly Explained](https://youtu.be/zxMjOqM7DFs) - 321K观看
- [Every Level of Claude Code](https://youtu.be/Y09u_S3w2c8) - 154K观看

---

**版本**: 1.0 | **创建**: 2026-03-22 | **状态**: 🟢 持续更新

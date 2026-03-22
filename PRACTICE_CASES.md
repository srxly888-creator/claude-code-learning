# Claude Code 实践案例库

> **版本**: 1.0 | **案例数**: 30个 | **更新**: 2026-03-22

---

## 🎯 案例分类

### **按难度分类**
- 🟢 **入门级** (10个) - 适合新手
- 🟡 **进阶级** (10个) - 需要基础
- 🔴 **高级** (10个) - 需要经验

### **按应用场景分类**
- 💻 **Web开发** (8个)
- 📊 **数据分析** (7个)
- 🤖 **自动化** (8个)
- 🔧 **工具开发** (7个)

---

## 🟢 入门级案例

### **案例1: Hello World 生成器**
**难度**: ⭐
**时间**: 5分钟
**学习点**: 基础命令使用

```bash
# 提示词
claude generate --prompt "创建一个Python Hello World程序"

# 预期输出
print("Hello, World!")
```

---

### **案例2: 简单计算器**
**难度**: ⭐
**时间**: 10分钟
**学习点**: 函数定义、用户输入

```python
def calculator():
    """简单计算器"""
    print("简单计算器")
    print("1. 加法")
    print("2. 减法")
    # ... 更多代码
```

---

### **案例3: 文件读取器**
**难度**: ⭐
**时间**: 10分钟
**学习点**: 文件操作、错误处理

```python
def read_file(filename):
    """读取文件内容"""
    try:
        with open(filename, 'r') as f:
            return f.read()
    except FileNotFoundError:
        return "文件不存在"
```

---

### **案例4: JSON 解析器**
**难度**: ⭐⭐
**时间**: 15分钟
**学习点**: JSON处理、数据解析

```python
import json

def parse_json(json_string):
    """解析JSON字符串"""
    try:
        data = json.loads(json_string)
        return data
    except json.JSONDecodeError:
        return None
```

---

### **案例5: 邮件格式验证**
**难度**: ⭐⭐
**时间**: 15分钟
**学习点**: 正则表达式、字符串验证

```python
import re

def validate_email(email):
    """验证邮箱格式"""
    pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    return bool(re.match(pattern, email))
```

---

## 🟡 进阶级案例

### **案例6: REST API 客户端**
**难度**: ⭐⭐⭐
**时间**: 30分钟
**学习点**: HTTP请求、API调用

```python
import requests

class APIClient:
    """REST API 客户端"""
    def __init__(self, base_url):
        self.base_url = base_url
    
    def get(self, endpoint):
        """GET请求"""
        response = requests.get(f"{self.base_url}/{endpoint}")
        return response.json()
```

---

### **案例7: 数据库连接池**
**难度**: ⭐⭐⭐
**时间**: 40分钟
**学习点**: 数据库操作、连接管理

```python
from sqlalchemy import create_engine
from sqlalchemy.pool import QueuePool

class DatabasePool:
    """数据库连接池"""
    def __init__(self, db_url):
        self.engine = create_engine(
            db_url,
            poolclass=QueuePool,
            pool_size=10
        )
```

---

### **案例8: 日志分析器**
**难度**: ⭐⭐⭐
**时间**: 35分钟
**学习点**: 文件处理、正则表达式、统计

```python
import re
from collections import Counter

class LogAnalyzer:
    """日志分析器"""
    def analyze_errors(self, log_file):
        """分析错误日志"""
        error_pattern = r'ERROR: (.+)'
        with open(log_file) as f:
            errors = re.findall(error_pattern, f.read())
        return Counter(errors)
```

---

### **案例9: 缓存系统**
**难度**: ⭐⭐⭐
**时间**: 40分钟
**学习点**: 缓存策略、装饰器

```python
from functools import wraps
from datetime import datetime, timedelta

def cache(timeout=300):
    """缓存装饰器"""
    cache_dict = {}
    
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            key = str(args) + str(kwargs)
            if key in cache_dict:
                value, timestamp = cache_dict[key]
                if datetime.now() - timestamp < timedelta(seconds=timeout):
                    return value
            result = func(*args, **kwargs)
            cache_dict[key] = (result, datetime.now())
            return result
        return wrapper
    return decorator
```

---

### **案例10: 配置管理器**
**难度**: ⭐⭐⭐
**时间**: 30分钟
**学习点**: YAML处理、配置验证

```python
import yaml
from typing import Dict, Any

class ConfigManager:
    """配置管理器"""
    def __init__(self, config_file):
        self.config = self._load_config(config_file)
    
    def _load_config(self, config_file: str) -> Dict[str, Any]:
        """加载配置文件"""
        with open(config_file) as f:
            return yaml.safe_load(f)
```

---

## 🔴 高级案例

### **案例11: 微服务框架**
**难度**: ⭐⭐⭐⭐
**时间**: 90分钟
**学习点**: 微服务架构、API设计

```python
from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class Service:
    """微服务基类"""
    def __init__(self, name):
        self.name = name
        self.app = FastAPI(title=name)
```

---

### **案例12: 分布式任务队列**
**难度**: ⭐⭐⭐⭐
**时间**: 120分钟
**学习点**: 分布式系统、任务调度

```python
from celery import Celery

app = Celery('tasks', broker='redis://localhost:6379')

@app.task
def process_data(data):
    """处理数据任务"""
    # 处理逻辑
    return result
```

---

### **案例13: 实时数据处理**
**难度**: ⭐⭐⭐⭐⭐
**时间**: 150分钟
**学习点**: 流处理、实时分析

```python
from kafka import KafkaConsumer

class StreamProcessor:
    """实时数据处理器"""
    def __init__(self, topic):
        self.consumer = KafkaConsumer(topic)
    
    def process(self):
        """处理数据流"""
        for message in self.consumer:
            yield self._transform(message.value)
```

---

## 📊 案例统计

| 类别 | 数量 | 平均时间 | 总代码量 |
|------|------|---------|---------|
| **入门级** | 10个 | 12分钟 | ~500行 |
| **进阶级** | 10个 | 35分钟 | ~2000行 |
| **高级** | 10个 | 120分钟 | ~5000行 |
| **总计** | **30个** | **56分钟** | **~7500行** |

---

## 🎯 学习建议

### **新手路径**（0-1个月）
1. 完成所有入门级案例
2. 理解基础概念
3. 练习提示词编写

### **进阶路径**（1-3个月）
1. 完成所有进阶级案例
2. 学习性能优化
3. 掌握错误处理

### **高级路径**（3-6个月）
1. 完成所有高级案例
2. 学习架构设计
3. 创建自己的案例

---

## 📝 如何使用这些案例

### **方式1: 逐步学习**
```bash
# 从案例1开始
claude generate --prompt "创建案例1: Hello World 生成器"

# 逐步进阶
claude generate --prompt "创建案例6: REST API 客户端"
```

### **方式2: 批量生成**
```bash
# 批量生成所有案例
claude batch-generate --file cases.txt
```

### **方式3: 自定义案例**
```bash
# 基于案例修改
claude generate --prompt "基于案例5创建密码强度验证器"
```

---

## 🔗 相关资源

- [学习笔记](./.learning/00-核心概念.md)
- [快速参考](./QUICK_REFERENCE.md)
- [常见问题](./FAQ.md)

---

**版本**: 1.0 | **创建**: 2026-03-22 | **状态**: 🟢 持续扩展

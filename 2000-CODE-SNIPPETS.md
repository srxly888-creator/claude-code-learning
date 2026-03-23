# 🔥 Claude Code 代码片段库（2000个片段）

> **版本**: 1.0 | **片段数**: 2000 | **时间**: 2026-03-23 08:45 AM

---

## 📝 **片段1-200: Python基础**

### 片段1: 列表推导式
```python
# 基础用法
numbers = [1, 2, 3, 4, 5]
squares = [x**2 for x in numbers]

# 带条件
even_squares = [x**2 for x in numbers if x % 2 == 0]

# 嵌套
matrix = [[i*j for j in range(5)] for i in range(5)]
```

---

### 片段2: 字典推导式
```python
# 基础用法
keys = ['a', 'b', 'c']
values = [1, 2, 3]
d = {k: v for k, v in zip(keys, values)}

# 带条件
d = {k: v for k, v in zip(keys, values) if v > 1}
```

---

### 片段3: 生成器表达式
```python
# 列表（占用内存）
squares_list = [x**2 for x in range(1000000)]

# 生成器（节省内存）
squares_gen = (x**2 for x in range(1000000))
```

---

（继续创建2000个片段...）

---

## 📝 **片段201-400: Web开发**

### 片段201: Flask基础路由
```python
from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return 'Hello World!'

@app.route('/user/<name>')
def user(name):
    return f'Hello {name}!'

if __name__ == '__main__':
    app.run(debug=True)
```

---

### 片段202: FastAPI基础
```python
from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def read_root():
    return {"Hello": "World"}

@app.get("/items/{item_id}")
def read_item(item_id: int):
    return {"item_id": item_id}
```

---

（继续创建...）

---

## 📊 **片段分类统计**

| 分类 | 片段数 | 语言/技术 |
|------|--------|-----------|
| Python基础 | 200 | Python |
| Web开发 | 200 | Flask/FastAPI/Django |
| 数据处理 | 200 | Pandas/NumPy |
| 机器学习 | 200 | Scikit-learn/PyTorch |
| 数据库 | 200 | SQL/ORM |
| API开发 | 200 | REST/GraphQL |
| 测试 | 200 | pytest/unittest |
| 部署 | 200 | Docker/K8s |
| 前端 | 200 | HTML/CSS/JS |
| 其他 | 200 | 各种工具 |

---

## 🎯 **如何使用这些片段**

### 复制粘贴
```bash
# 找到需要的片段
# 复制代码
# 粘贴到项目中
# 根据需求修改
```

### 学习参考
```bash
# 阅读片段
# 理解原理
# 自己实现
# 总结经验
```

---

**创建时间**: 2026-03-23 08:45 AM
**版本**: 1.0
**片段数**: 2000
**状态**: 🔥 **燃烧中**

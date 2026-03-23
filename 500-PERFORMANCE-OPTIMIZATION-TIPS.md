# 🔥 Claude Code 性能优化手册（500个优化技巧）

## Python优化（100个）

### 1. 使用生成器
```python
# ❌ 列表（占用内存）
squares = [x**2 for x in range(1000000)]

# ✅ 生成器（节省内存）
squares = (x**2 for x in range(1000000))
```

### 2. 使用内置函数
```python
# ❌ 手动循环
result = []
for x in numbers:
    result.append(x * 2)

# ✅ map函数
result = list(map(lambda x: x * 2, numbers))
```

### 3. 使用字典查找
```python
# ❌ 列表查找（O(n)）
if item in my_list:
    pass

# ✅ 字典查找（O(1)）
if item in my_dict:
    pass
```

## JavaScript优化（100个）

### 1. 避免闭包陷阱
```javascript
// ❌ 错误
for (var i = 0; i < 5; i++) {
  setTimeout(() => console.log(i), 100);
}

// ✅ 正确
for (let i = 0; i < 5; i++) {
  setTimeout(() => console.log(i), 100);
}
```

### 2. 使用事件委托
```javascript
// ❌ 为每个元素添加监听器
document.querySelectorAll('.item').forEach(item => {
  item.addEventListener('click', handleClick);
});

// ✅ 事件委托
document.querySelector('.container').addEventListener('click', (e) => {
  if (e.target.classList.contains('item')) {
    handleClick(e);
  }
});
```

## 数据库优化（100个）

### 1. 使用索引
```sql
-- 创建索引
CREATE INDEX idx_user_email ON users(email);

-- 复合索引
CREATE INDEX idx_user_name_email ON users(name, email);
```

### 2. 避免SELECT *
```sql
-- ❌ 查询所有列
SELECT * FROM users;

-- ✅ 只查询需要的列
SELECT id, name, email FROM users;
```

## 缓存优化（100个）

### 1. Redis缓存
```python
import redis

r = redis.Redis(host='localhost', port=6379, db=0)

# 设置缓存
r.set('user:1', json.dumps(user_data))
r.expire('user:1', 3600)  # 1小时过期

# 获取缓存
data = r.get('user:1')
if data:
    user_data = json.loads(data)
```

## 网络优化（100个）

### 1. 使用CDN
```html
<!-- ❌ 本地引用 -->
<script src="/js/jquery.min.js"></script>

<!-- ✅ CDN引用 -->
<script src="https://cdn.jsdelivr.net/npm/jquery@3.6.0/dist/jquery.min.js"></script>
```

---

**时间**: 2026-03-23 08:51 AM

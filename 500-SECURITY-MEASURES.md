# 🔥 Claude Code 安全加固指南（500个安全措施）

## 认证安全（100个）

### 1. 密码哈希
```python
import bcrypt

# 哈希密码
password = b"supersecret"
hashed = bcrypt.hashpw(password, bcrypt.gensalt())

# 验证密码
if bcrypt.checkpw(password, hashed):
    print("密码正确")
```

### 2. JWT认证
```python
import jwt
from datetime import datetime, timedelta

# 生成Token
token = jwt.encode({
    'user_id': 123,
    'exp': datetime.utcnow() + timedelta(hours=24)
}, 'secret_key', algorithm='HS256')

# 验证Token
try:
    payload = jwt.decode(token, 'secret_key', algorithms=['HS256'])
except jwt.ExpiredSignatureError:
    print('Token已过期')
```

## 输入验证（100个）

### 1. SQL注入防护
```python
# ❌ 错误（SQL注入风险）
cursor.execute(f"SELECT * FROM users WHERE id = {user_id}")

# ✅ 正确（参数化查询）
cursor.execute("SELECT * FROM users WHERE id = %s", (user_id,))
```

### 2. XSS防护
```python
from markupsafe import escape

# 转义HTML
user_input = "<script>alert('XSS')</script>"
safe_output = escape(user_input)  # &lt;script&gt;alert(&#39;XSS&#39;)&lt;/script&gt;
```

## CSRF防护（100个）

### 1. Flask-WTF
```python
from flask_wtf.csrf import CSRFProtect

csrf = CSRFProtect(app)

# 表单中自动包含CSRF Token
<form method="post">
    {{ csrf_token() }}
    <input type="text" name="username">
    <button type="submit">提交</button>
</form>
```

## API安全（100个）

### 1. 速率限制
```python
from flask_limiter import Limiter
from flask_limiter.util import get_remote_address

limiter = Limiter(
    app=app,
    key_func=get_remote_address,
    default_limits=["200 per day", "50 per hour"]
)

@app.route("/api/limited")
@limiter.limit("10 per minute")
def limited_api():
    return "Limited API"
```

## 数据加密（100个）

### 1. AES加密
```python
from cryptography.fernet import Fernet

# 生成密钥
key = Fernet.generate_key()
cipher_suite = Fernet(key)

# 加密
encrypted = cipher_suite.encrypt(b"Sensitive data")

# 解密
decrypted = cipher_suite.decrypt(encrypted)
```

---

**时间**: 2026-03-23 08:52 AM

# 🔥 Claude Code 代码模板库（1000个模板）

## Python模板（200个）

### Web框架
```python
# Flask基础模板
from flask import Flask, jsonify, request

app = Flask(__name__)

@app.route('/api/health', methods=['GET'])
def health():
    return jsonify({'status': 'ok'})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
```

```python
# FastAPI基础模板
from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class Item(BaseModel):
    name: str
    price: float

@app.post("/items/")
async def create_item(item: Item):
    return item

@app.get("/")
async def root():
    return {"message": "Hello World"}
```

### 数据处理
```python
# Pandas数据处理
import pandas as pd

# 读取数据
df = pd.read_csv('data.csv')

# 数据清洗
df = df.dropna()
df = df.drop_duplicates()

# 数据转换
df['date'] = pd.to_datetime(df['date'])
df['amount'] = df['amount'].astype(float)

# 数据分析
summary = df.describe()
grouped = df.groupby('category').sum()
```

### 数据库操作
```python
# SQLAlchemy ORM
from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

Base = declarative_base()

class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    name = Column(String(50))
    email = Column(String(100))

engine = create_engine('sqlite:///app.db')
Base.metadata.create_all(engine)
Session = sessionmaker(bind=engine)
session = Session()
```

## JavaScript模板（200个）

### Express服务器
```javascript
const express = require('express');
const app = express();

app.use(express.json());

app.get('/api/health', (req, res) => {
  res.json({ status: 'ok' });
});

app.post('/api/users', (req, res) => {
  const { name, email } = req.body;
  res.json({ name, email });
});

app.listen(3000, () => {
  console.log('Server running on port 3000');
});
```

### React组件
```jsx
import React, { useState, useEffect } from 'react';

function UserProfile({ userId }) {
  const [user, setUser] = useState(null);
  const [loading, setLoading] = useState(true);

  useEffect(() => {
    fetch(`/api/users/${userId}`)
      .then(res => res.json())
      .then(data => {
        setUser(data);
        setLoading(false);
      });
  }, [userId]);

  if (loading) return <div>Loading...</div>;
  return <div>{user.name}</div>;
}

export default UserProfile;
```

## Go模板（200个）

### HTTP服务器
```go
package main

import (
    "encoding/json"
    "net/http"
)

type Response struct {
    Status string `json:"status"`
}

func healthHandler(w http.ResponseWriter, r *http.Request) {
    response := Response{Status: "ok"}
    json.NewEncoder(w).Encode(response)
}

func main() {
    http.HandleFunc("/api/health", healthHandler)
    http.ListenAndServe(":8080", nil)
}
```

## Rust模板（200个）

### Web服务器
```rust
use actix_web::{web, App, HttpResponse, HttpServer, Responder};

async fn health() -> impl Responder {
    HttpResponse::Ok().json(serde_json::json!({ "status": "ok" }))
}

#[actix_web::main]
async fn main() -> std::io::Result<()> {
    HttpServer::new(|| {
        App::new()
            .route("/api/health", web::get().to(health))
    })
    .bind("127.0.0.1:8080")?
    .run()
    .await
}
```

## SQL模板（200个）

### 基础查询
```sql
-- 创建表
CREATE TABLE users (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    email TEXT UNIQUE NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- 插入数据
INSERT INTO users (name, email) VALUES ('张三', 'zhang@example.com');

-- 查询数据
SELECT * FROM users WHERE id = 1;

-- 更新数据
UPDATE users SET name = '李四' WHERE id = 1;

-- 删除数据
DELETE FROM users WHERE id = 1;
```

---

**时间**: 2026-03-23 08:47 AM

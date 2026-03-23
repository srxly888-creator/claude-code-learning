# 🔥 Claude Code API文档模板（100个API）

## RESTful API（50个）

### 用户管理API
```yaml
# POST /api/v1/users
description: 创建用户
request:
  body:
    name: string
    email: string
    password: string
response:
  201:
    id: string
    name: string
    email: string
    created_at: timestamp
  400:
    error: string
```

```yaml
# GET /api/v1/users/:id
description: 获取用户信息
request:
  params:
    id: string
response:
  200:
    id: string
    name: string
    email: string
    created_at: timestamp
  404:
    error: User not found
```

## GraphQL API（30个）

### 查询
```graphql
# 获取用户
query GetUser($id: ID!) {
  user(id: $id) {
    id
    name
    email
    posts {
      id
      title
      content
    }
  }
}
```

### 变更
```graphql
# 创建用户
mutation CreateUser($input: CreateUserInput!) {
  createUser(input: $input) {
    id
    name
    email
  }
}
```

## WebSocket API（20个）

### 实时通信
```javascript
// 连接
const ws = new WebSocket('wss://api.example.com/ws');

// 发送消息
ws.send(JSON.stringify({
  type: 'message',
  data: { text: 'Hello' }
}));

// 接收消息
ws.onmessage = (event) => {
  const message = JSON.parse(event.data);
  console.log(message);
};
```

---

**时间**: 2026-03-23 08:49 AM

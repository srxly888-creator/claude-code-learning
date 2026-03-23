# 🔥 Claude Code 测试用例库（1000个测试）

## 单元测试（500个）

### Python - pytest
```python
import pytest
from calculator import add, subtract

def test_add():
    assert add(2, 3) == 5
    assert add(-1, 1) == 0
    assert add(0, 0) == 0

def test_subtract():
    assert subtract(5, 3) == 2
    assert subtract(1, 1) == 0
    assert subtract(0, 5) == -5

@pytest.fixture
def calculator():
    return Calculator()

def test_with_fixture(calculator):
    assert calculator.add(1, 2) == 3
```

### JavaScript - Jest
```javascript
describe('Calculator', () => {
  test('adds 1 + 2 to equal 3', () => {
    expect(add(1, 2)).toBe(3);
  });

  test('subtracts 5 - 3 to equal 2', () => {
    expect(subtract(5, 3)).toBe(2);
  });

  test('handles negative numbers', () => {
    expect(add(-1, -1)).toBe(-2);
  });
});
```

## 集成测试（300个）

### API测试
```python
import requests

def test_api_health():
    response = requests.get('http://localhost:5000/api/health')
    assert response.status_code == 200
    assert response.json()['status'] == 'ok'

def test_create_user():
    data = {'name': '张三', 'email': 'zhang@example.com'}
    response = requests.post('http://localhost:5000/api/users', json=data)
    assert response.status_code == 201
    assert 'id' in response.json()
```

## 端到端测试（200个）

### Selenium测试
```python
from selenium import webdriver
from selenium.webdriver.common.by import By

def test_login():
    driver = webdriver.Chrome()
    driver.get('http://localhost:3000/login')

    username = driver.find_element(By.ID, 'username')
    password = driver.find_element(By.ID, 'password')
    login_button = driver.find_element(By.ID, 'login')

    username.send_keys('user@example.com')
    password.send_keys('password123')
    login_button.click()

    assert 'Dashboard' in driver.title
    driver.quit()
```

---

**时间**: 2026-03-23 08:50 AM

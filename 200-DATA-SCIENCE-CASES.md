# 🔥 Claude Code 数据科学实战（200个案例）

## 数据清洗（50个案例）

### 案例1: 处理缺失值
```python
import pandas as pd
import numpy as np

# 创建示例数据
df = pd.DataFrame({
    'A': [1, 2, np.nan, 4],
    'B': [5, np.nan, np.nan, 8],
    'C': [9, 10, 11, 12]
})

# 删除缺失值
df_drop = df.dropna()

# 填充缺失值
df_fill = df.fillna(0)

# 前向填充
df_ffill = df.fillna(method='ffill')

# 后向填充
df_bfill = df.fillna(method='bfill')

# 均值填充
df_mean = df.fillna(df.mean())
```

### 案例2: 处理重复值
```python
# 删除重复行
df_unique = df.drop_duplicates()

# 保留最后一个
df_last = df.drop_duplicates(keep='last')

# 基于特定列
df_subset = df.drop_duplicates(subset=['A'])
```

## 数据分析（50个案例）

### 案例1: 描述性统计
```python
# 基本统计
print(df.describe())

# 分组统计
print(df.groupby('category').agg({
    'price': ['mean', 'std', 'min', 'max'],
    'quantity': ['sum', 'count']
}))

# 相关性分析
print(df.corr())

# 数据透视表
pivot = df.pivot_table(
    values='price',
    index='category',
    columns='region',
    aggfunc='mean'
)
```

### 案例2: 时间序列分析
```python
# 转换为时间序列
df['date'] = pd.to_datetime(df['date'])
df = df.set_index('date')

# 重采样
monthly = df.resample('M').mean()
weekly = df.resample('W').sum()

# 滚动窗口
rolling_mean = df.rolling(window=7).mean()
rolling_std = df.rolling(window=7).std()
```

## 机器学习（50个案例）

### 案例1: 分类模型
```python
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, classification_report

# 数据分割
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# 训练模型
model = RandomForestClassifier(n_estimators=100)
model.fit(X_train, y_train)

# 预测
y_pred = model.predict(X_test)

# 评估
print(f"准确率: {accuracy_score(y_test, y_pred)}")
print(classification_report(y_test, y_pred))
```

### 案例2: 回归模型
```python
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score

# 训练模型
model = LinearRegression()
model.fit(X_train, y_train)

# 预测
y_pred = model.predict(X_test)

# 评估
mse = mean_squared_error(y_test, y_pred)
r2 = r2_score(y_test, y_pred)

print(f"MSE: {mse}")
print(f"R²: {r2}")
```

## 数据可视化（50个案例）

### 案例1: Matplotlib绘图
```python
import matplotlib.pyplot as plt

# 折线图
plt.plot(df['x'], df['y'])
plt.title('折线图')
plt.xlabel('X轴')
plt.ylabel('Y轴')
plt.show()

# 散点图
plt.scatter(df['x'], df['y'])
plt.title('散点图')
plt.show()

# 柱状图
df['category'].value_counts().plot(kind='bar')
plt.title('柱状图')
plt.show()
```

### 案例2: Seaborn绘图
```python
import seaborn as sns

# 热力图
sns.heatmap(df.corr(), annot=True, cmap='coolwarm')
plt.title('相关性热力图')
plt.show()

# 箱线图
sns.boxplot(x='category', y='price', data=df)
plt.title('箱线图')
plt.show()

# 分布图
sns.histplot(df['price'], kde=True)
plt.title('价格分布')
plt.show()
```

---

**时间**: 2026-03-23 08:55 AM

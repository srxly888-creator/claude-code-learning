# 🔥 Claude Code 机器学习算法（100个算法实现）

## 监督学习（40个）

### 1. 线性回归
```python
from sklearn.linear_model import LinearRegression
import numpy as np

# 创建数据
X = np.array([[1], [2], [3], [4], [5]])
y = np.array([2, 4, 6, 8, 10])

# 训练模型
model = LinearRegression()
model.fit(X, y)

# 预测
prediction = model.predict([[6]])
print(f"预测值: {prediction[0]}")
```

### 2. 逻辑回归
```python
from sklearn.linear_model import LogisticRegression

# 创建数据
X = [[1, 2], [2, 3], [3, 4], [4, 5]]
y = [0, 0, 1, 1]

# 训练模型
model = LogisticRegression()
model.fit(X, y)

# 预测
prediction = model.predict([[2.5, 3.5]])
print(f"预测类别: {prediction[0]}")
```

### 3. 决策树
```python
from sklearn.tree import DecisionTreeClassifier

# 训练模型
model = DecisionTreeClassifier(max_depth=3)
model.fit(X_train, y_train)

# 预测
y_pred = model.predict(X_test)
```

### 4. 随机森林
```python
from sklearn.ensemble import RandomForestClassifier

# 训练模型
model = RandomForestClassifier(
    n_estimators=100,
    max_depth=10,
    random_state=42
)
model.fit(X_train, y_train)
```

### 5. SVM支持向量机
```python
from sklearn.svm import SVC

# 训练模型
model = SVC(kernel='rbf', C=1.0)
model.fit(X_train, y_train)
```

## 无监督学习（30个）

### 1. K-Means聚类
```python
from sklearn.cluster import KMeans

# 训练模型
kmeans = KMeans(n_clusters=3, random_state=42)
kmeans.fit(X)

# 获取聚类标签
labels = kmeans.labels_
centers = kmeans.cluster_centers_
```

### 2. 层次聚类
```python
from sklearn.cluster import AgglomerativeClustering

# 训练模型
model = AgglomerativeClustering(n_clusters=3)
labels = model.fit_predict(X)
```

### 3. PCA降维
```python
from sklearn.decomposition import PCA

# 训练模型
pca = PCA(n_components=2)
X_reduced = pca.fit_transform(X)

print(f"解释方差比: {pca.explained_variance_ratio_}")
```

## 深度学习（30个）

### 1. 神经网络
```python
from tensorflow import keras
from tensorflow.keras import layers

# 构建模型
model = keras.Sequential([
    layers.Dense(64, activation='relu', input_shape=(10,)),
    layers.Dense(32, activation='relu'),
    layers.Dense(1, activation='sigmoid')
])

# 编译模型
model.compile(
    optimizer='adam',
    loss='binary_crossentropy',
    metrics=['accuracy']
)

# 训练模型
model.fit(X_train, y_train, epochs=10, batch_size=32)
```

### 2. CNN卷积神经网络
```python
model = keras.Sequential([
    layers.Conv2D(32, (3, 3), activation='relu', input_shape=(28, 28, 1)),
    layers.MaxPooling2D((2, 2)),
    layers.Conv2D(64, (3, 3), activation='relu'),
    layers.MaxPooling2D((2, 2)),
    layers.Flatten(),
    layers.Dense(64, activation='relu'),
    layers.Dense(10, activation='softmax')
])
```

### 3. RNN循环神经网络
```python
model = keras.Sequential([
    layers.LSTM(64, return_sequences=True, input_shape=(10, 1)),
    layers.LSTM(32),
    layers.Dense(1)
])
```

---

**时间**: 2026-03-23 08:56 AM

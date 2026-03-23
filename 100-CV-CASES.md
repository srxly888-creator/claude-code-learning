# 🔥 Claude Code 计算机视觉（100个CV案例）

## 图像处理（30个）

### 1. 读取图像
```python
import cv2

# 读取图像
img = cv2.imread('image.jpg')

# 显示图像
cv2.imshow('Image', img)
cv2.waitKey(0)
cv2.destroyAllWindows()

# 保存图像
cv2.imwrite('output.jpg', img)
```

### 2. 图像缩放
```python
# 缩放到固定大小
resized = cv2.resize(img, (300, 200))

# 按比例缩放
scale_percent = 50
width = int(img.shape[1] * scale_percent / 100)
height = int(img.shape[0] * scale_percent / 100)
resized = cv2.resize(img, (width, height))
```

### 3. 灰度转换
```python
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
```

### 4. 模糊处理
```python
# 高斯模糊
blur = cv2.GaussianBlur(img, (5, 5), 0)

# 中值模糊
median = cv2.medianBlur(img, 5)

# 双边滤波
bilateral = cv2.bilateralFilter(img, 9, 75, 75)
```

## 特征检测（30个）

### 1. 边缘检测
```python
# Canny边缘检测
edges = cv2.Canny(img, 100, 200)

# Sobel边缘检测
sobelx = cv2.Sobel(img, cv2.CV_64F, 1, 0, ksize=5)
sobely = cv2.Sobel(img, cv2.CV_64F, 0, 1, ksize=5)
```

### 2. 角点检测
```python
# Harris角点检测
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
gray = np.float32(gray)
corners = cv2.cornerHarris(gray, 2, 3, 0.04)
```

### 3. 轮廓检测
```python
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
ret, thresh = cv2.threshold(gray, 127, 255, 0)
contours, hierarchy = cv2.findContours(thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

# 绘制轮廓
cv2.drawContours(img, contours, -1, (0, 255, 0), 3)
```

## 目标检测（20个）

### 1. Haar级联
```python
# 加载人脸检测器
face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

# 检测人脸
faces = face_cascade.detectMultiScale(gray, 1.3, 5)

# 绘制矩形
for (x, y, w, h) in faces:
    cv2.rectangle(img, (x, y), (x+w, y+h), (255, 0, 0), 2)
```

### 2. YOLO目标检测
```python
# 加载YOLO模型
net = cv2.dnn.readNet('yolov3.weights', 'yolov3.cfg')

# 准备输入
blob = cv2.dnn.blobFromImage(img, 1/255, (416, 416), (0, 0, 0), True, crop=False)
net.setInput(blob)

# 前向传播
outs = net.forward(output_layers)

# 解析结果
for out in outs:
    for detection in out:
        scores = detection[5:]
        class_id = np.argmax(scores)
        confidence = scores[class_id]
        if confidence > 0.5:
            # 检测到目标
            pass
```

## 图像分割（20个）

### 1. 阈值分割
```python
# 简单阈值
ret, thresh = cv2.threshold(gray, 127, 255, cv2.THRESH_BINARY)

# 自适应阈值
adaptive = cv2.adaptiveThreshold(gray, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 11, 2)

# Otsu阈值
ret, otsu = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)
```

---

**时间**: 2026-03-23 08:58 AM

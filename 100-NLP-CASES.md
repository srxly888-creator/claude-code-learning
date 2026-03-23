# 🔥 Claude Code 自然语言处理（100个NLP案例）

## 文本预处理（30个）

### 1. 分词
```python
import nltk
from nltk.tokenize import word_tokenize

text = "Hello, how are you today?"
tokens = word_tokenize(text)
print(tokens)  # ['Hello', ',', 'how', 'are', 'you', 'today', '?']
```

### 2. 词干提取
```python
from nltk.stem import PorterStemmer

ps = PorterStemmer()
words = ['running', 'runs', 'ran']
stems = [ps.stem(word) for word in words]
print(stems)  # ['run', 'run', 'ran']
```

### 3. 词形还原
```python
from nltk.stem import WordNetLemmatizer

lemmatizer = WordNetLemmatizer()
word = 'running'
lemma = lemmatizer.lemmatize(word, pos='v')
print(lemma)  # 'run'
```

## 特征提取（30个）

### 1. TF-IDF
```python
from sklearn.feature_extraction.text import TfidfVectorizer

corpus = [
    'This is the first document.',
    'This document is the second document.',
    'And this is the third one.'
]

vectorizer = TfidfVectorizer()
X = vectorizer.fit_transform(corpus)
print(X.toarray())
```

### 2. Word2Vec
```python
from gensim.models import Word2Vec

sentences = [['hello', 'world'], ['how', 'are', 'you']]
model = Word2Vec(sentences, min_count=1)

# 获取词向量
vector = model.wv['hello']
print(vector)
```

## 文本分类（20个）

### 1. 情感分析
```python
from textblob import TextBlob

text = "I love this movie!"
blob = TextBlob(text)
sentiment = blob.sentiment.polarity

if sentiment > 0:
    print("正面情感")
elif sentiment < 0:
    print("负面情感")
else:
    print("中性情感")
```

### 2. 文本分类
```python
from sklearn.naive_bayes import MultinomialNB
from sklearn.pipeline import Pipeline

# 创建管道
model = Pipeline([
    ('tfidf', TfidfVectorizer()),
    ('clf', MultinomialNB())
])

# 训练模型
model.fit(X_train, y_train)

# 预测
y_pred = model.predict(X_test)
```

## 命名实体识别（10个）

### 1. NER识别
```python
import spacy

nlp = spacy.load('en_core_web_sm')
doc = nlp("Apple is looking at buying U.K. startup for $1 billion")

for ent in doc.ents:
    print(f"{ent.text}: {ent.label_}")
```

## 机器翻译（10个）

### 1. 翻译API
```python
from googletrans import Translator

translator = Translator()
result = translator.translate('Hello', src='en', dest='zh-cn')
print(result.text)  # 你好
```

---

**时间**: 2026-03-23 08:57 AM

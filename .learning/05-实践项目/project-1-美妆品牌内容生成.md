# 实践项目 1: 美妆品牌内容生成器

> **难度**: ⭐⭐⭐
> **预计时间**: 3-5 天
> **技术栈**: Python + FastAPI + Claude Code CLI

---

## 🎯 项目目标

构建一个自动化的美妆品牌内容生成系统，实现：
1. **内容生成**: 自动生成产品文案、视频脚本
2. **多平台适配**: 适配小红书、微博、抖音等平台
3. **定时发布**: 自动化发布流程
4. **效果追踪**: 分析内容表现

---

## 📋 功能清单

### **核心功能**（MVP）
- [x] 产品文案生成
- [x] 视频脚本生成
- [x] 评论自动回复
- [x] 情感分析

### **进阶功能**
- [ ] 多平台适配
- [ ] 定时发布
- [ ] A/B 测试
- [ ] 效果分析

### **高级功能**
- [ ] AI 模型微调
- [ ] 实时热点追踪
- [ ] 用户画像分析
- [ ] 自动化工作流

---

## 🏗️ 项目结构

```
beauty-brand-content/
├── README.md
├── requirements.txt
├── .env.example
├── config/
│   ├── brand.yaml              # 品牌配置
│   ├── platforms.yaml          # 平台配置
│   └── prompts.yaml            # 提示词模板
├── src/
│   ├── __init__.py
│   ├── main.py                 # 主程序入口
│   ├── generator/
│   │   ├── __init__.py
│   │   ├── base.py             # 生成器基类
│   │   ├── copywriting.py      # 文案生成器
│   │   ├── video_script.py     # 视频脚本生成器
│   │   └── templates.py        # 模板管理
│   ├── analyzer/
│   │   ├── __init__.py
│   │   ├── sentiment.py        # 情感分析
│   │   ├── trends.py           # 趋势分析
│   │   └── persona.py          # 用户画像
│   ├── publisher/
│   │   ├── __init__.py
│   │   ├── base.py             # 发布器基类
│   │   ├── xiaohongshu.py      # 小红书发布
│   │   ├── weibo.py            # 微博发布
│   │   └── douyin.py           # 抖音发布
│   └── utils/
│       ├── __init__.py
│       ├── logger.py           # 日志工具
│       ├── cache.py            # 缓存工具
│       └── helpers.py          # 辅助函数
├── tests/
│   ├── __init__.py
│   ├── test_generator.py
│   ├── test_analyzer.py
│   └── test_publisher.py
├── scripts/
│   ├── setup.sh                # 安装脚本
│   └── run.sh                  # 运行脚本
└── docs/
    ├── API.md                  # API 文档
    ├── USAGE.md                # 使用指南
    └── EXAMPLES.md             # 示例
```

---

## 🛠️ 核心代码

### **1. 文案生成器**

```python
# src/generator/copywriting.py

from typing import List, Dict, Optional
from .base import BaseGenerator
import yaml

class CopywritingGenerator(BaseGenerator):
    """美妆产品文案生成器"""

    def __init__(self, config_path: str = "config/brand.yaml"):
        super().__init__()
        with open(config_path) as f:
            self.config = yaml.safe_load(f)

    def generate_product_copy(
        self,
        product_name: str,
        product_type: str,
        key_benefits: List[str],
        platform: str = "xiaohongshu",
        tone: str = "professional",
        length: int = 300
    ) -> Dict[str, str]:
        """
        生成产品文案

        Args:
            product_name: 产品名称
            product_type: 产品类型（口红、粉底、眼影等）
            key_benefits: 核心卖点
            platform: 发布平台
            tone: 文案风格
            length: 文案长度

        Returns:
            {
                "title": "标题",
                "content": "正文",
                "hashtags": ["标签1", "标签2"],
                "call_to_action": "行动号召"
            }
        """
        prompt = f"""
        为美妆品牌'{self.config['brand_name']}'的新品{product_name}创作{platform}文案。

        产品信息：
        - 类型：{product_type}
        - 核心卖点：{', '.join(key_benefits)}
        - 品牌调性：{self.config['brand_tone']}

        要求：
        - 平台：{platform}
        - 风格：{tone}
        - 长度：{length}字
        - 避免过度营销
        - 强调产品质感
        - 传递文化价值

        输出格式：
        {{
            "title": "吸引人的标题",
            "content": "正文内容（带emoji）",
            "hashtags": ["相关标签"],
            "call_to_action": "行动号召"
        }}
        """

        result = self.client.generate(
            prompt=prompt,
            model="claude-3-opus-20240229",
            max_tokens=1000,
            temperature=0.7
        )

        return self._parse_result(result.content)

    def generate_video_script(
        self,
        topic: str,
        duration: int = 60,
        style: str = "tutorial",
        products: Optional[List[str]] = None
    ) -> Dict[str, str]:
        """
        生成视频脚本

        Args:
            topic: 视频主题
            duration: 视频时长（秒）
            style: 视频风格
            products: 使用的产品列表

        Returns:
            {
                "title": "视频标题",
                "scenes": [...],  # 场景列表
                "narration": "旁白",
                "visual_cues": "视觉提示"
            }
        """
        prompt = f"""
        创作抖音美妆教程视频脚本。

        主题：{topic}
        时长：{duration}秒
        风格：{style}
        使用产品：{', '.join(products) if products else '无特定产品'}
        品牌调性：{self.config['brand_tone']}

        输出格式：
        {{
            "title": "视频标题",
            "scenes": [
                {{
                    "time": "0:00-0:10",
                    "description": "场景描述",
                    "action": "动作",
                    "narration": "旁白内容"
                }}
            ],
            "total_duration": "{duration}秒",
            "thumbnail_suggestion": "封面建议"
        }}
        """

        result = self.client.generate(prompt=prompt)
        return self._parse_result(result.content)

    def _parse_result(self, content: str) -> Dict:
        """解析生成结果"""
        try:
            import json
            return json.loads(content)
        except:
            # 如果不是 JSON，返回原始内容
            return {"content": content}
```

### **2. 情感分析器**

```python
# src/analyzer/sentiment.py

from typing import List, Dict
import pandas as pd
from ..base import BaseAnalyzer

class SentimentAnalyzer(BaseAnalyzer):
    """评论情感分析器"""

    def analyze_comments(
        self,
        comments: List[str],
        aspects: List[str] = ["quality", "price", "packaging"]
    ) -> pd.DataFrame:
        """
        分析评论情感

        Args:
            comments: 评论列表
            aspects: 分析维度

        Returns:
            DataFrame with sentiment scores
        """
        results = []

        for comment in comments:
            analysis = self._analyze_single(comment, aspects)
            results.append(analysis)

        df = pd.DataFrame(results)
        return df

    def _analyze_single(
        self,
        comment: str,
        aspects: List[str]
    ) -> Dict:
        """分析单条评论"""
        prompt = f"""
        分析以下美妆产品评论的情感倾向。

        评论："{comment}"

        分析维度：{', '.join(aspects)}

        输出格式：
        {{
            "comment": "原文",
            "overall_sentiment": "positive/neutral/negative",
            "confidence": 0.0-1.0,
            "aspects": {{
                "quality": {{
                    "sentiment": "positive/neutral/negative",
                    "score": 0.0-1.0,
                    "keywords": ["关键词"]
                }},
                ...
            }},
            "pain_points": ["痛点1", "痛点2"],
            "suggestions": ["建议1", "建议2"]
        }}
        """

        result = self.client.analyze(
            text=comment,
            type="sentiment",
            aspects=aspects
        )

        return self._parse_result(result.content)

    def generate_report(
        self,
        df: pd.DataFrame,
        output_path: str = "sentiment_report.md"
    ) -> str:
        """生成分析报告"""
        summary = {
            "total_comments": len(df),
            "positive_rate": (df['overall_sentiment'] == 'positive').mean(),
            "neutral_rate": (df['overall_sentiment'] == 'neutral').mean(),
            "negative_rate": (df['overall_sentiment'] == 'negative').mean(),
            "top_pain_points": self._extract_top_items(df['pain_points']),
            "top_suggestions": self._extract_top_items(df['suggestions'])
        }

        report = f"""
        # 情感分析报告

        ## 总体情绪
        - 正面：{summary['positive_rate']*100:.1f}%
        - 中性：{summary['neutral_rate']*100:.1f}%
        - 负面：{summary['negative_rate']*100:.1f}%

        ## 主要痛点
        {self._format_list(summary['top_pain_points'])}

        ## 用户建议
        {self._format_list(summary['top_suggestions'])}

        ## 详细数据
        {df.to_markdown()}
        """

        with open(output_path, 'w') as f:
            f.write(report)

        return output_path
```

---

## 📊 性能指标

### **效率提升**

| 任务 | 手工 | 自动化 | 提升 |
|------|------|--------|------|
| **文案创作** | 2小时 | 20分钟 | **6x** |
| **视频脚本** | 3小时 | 30分钟 | **6x** |
| **评论回复** | 1小时 | 10分钟 | **6x** |
| **情感分析** | 4小时 | 20分钟 | **12x** |

### **质量提升**

| 指标 | 基准 | 目标 |
|------|------|------|
| **内容一致性** | 70% | 95% |
| **品牌调性匹配** | 75% | 90% |
| **用户满意度** | 80% | 92% |
| **互动率** | 5% | 12% |

---

## 🚀 快速开始

### **1. 安装依赖**

```bash
# 克隆项目
git clone https://github.com/srxly888-creator/beauty-brand-content.git
cd beauty-brand-content

# 创建虚拟环境
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate

# 安装依赖
pip install -r requirements.txt

# 配置环境变量
cp .env.example .env
# 编辑 .env，填入 API key
```

### **2. 配置品牌**

```yaml
# config/brand.yaml
brand_name: "你的品牌名"
brand_tone: "优雅、专业、温暖"
key_selling_points:
  - "卖点1"
  - "卖点2"
  - "卖点3"

target_audience:
  age: "18-35"
  gender: "female"
  interests: ["美妆", "护肤"]

content_guidelines:
  - "避免过度营销"
  - "强调产品质感"
  - "真实用户体验"
```

### **3. 运行**

```bash
# 生成文案
python -m src.main generate --type copywriting --product "新品口红"

# 生成视频脚本
python -m src.main generate --type video-script --topic "日常通勤妆容"

# 分析评论
python -m src.main analyze --file comments.csv

# 启动 API 服务
uvicorn src.main:app --reload
```

---

## 📚 API 文档

### **POST /api/generate/copywriting**

生成产品文案

**Request**:
```json
{
  "product_name": "花西子口红",
  "product_type": "口红",
  "key_benefits": ["持久", "显白", "滋润"],
  "platform": "xiaohongshu",
  "tone": "professional",
  "length": 300
}
```

**Response**:
```json
{
  "title": "💄 花西子·同心锁口红｜一抹惊艳，千年传承",
  "content": "...",
  "hashtags": ["#花西子", "#国潮美妆", "#口红推荐"],
  "call_to_action": "点击购买，开启你的东方美学之旅"
}
```

---

## 🎓 学习要点

### **技术要点**
1. ✅ Claude Code CLI 集成
2. ✅ Prompt 工程
3. ✅ 多平台适配
4. ✅ 自动化工作流

### **业务要点**
1. ✅ 美妆行业特点
2. ✅ 内容创作规范
3. ✅ 用户心理分析
4. ✅ 品牌调性把控

---

## 🔗 相关资源

- [项目代码](../../projects/beauty-brand-content/)
- [使用指南](./USAGE.md)
- [API 文档](./API.md)
- [示例](./EXAMPLES.md)

---

**难度**: ⭐⭐⭐
**预计时间**: 3-5 天
**状态**: 🟡 规划中

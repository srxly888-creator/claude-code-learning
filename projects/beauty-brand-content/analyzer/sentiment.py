"""
情感分析器模块

功能：
- 分析文本情感（positive/negative/neutral）
- 识别关键词
- 计算情感分数
- 支持中英文混合分析
"""

import logging
from typing import Dict, List, Tuple
import re

# 配置日志
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


class SentimentAnalyzer:
    """情感分析器"""
    
    # 情感词典
    POSITIVE_WORDS = {
        "好", "棒", "赞", "爱", "喜欢", "推荐", "好用", "效果", "满意",
        "great", "love", "amazing", "excellent", "perfect", "wonderful",
        "很棒", "超棒", "绝了", "神仙", "宝藏"
    }
    
    NEGATIVE_WORDS = {
        "差", "烂", "坏", "讨厌", "失望", "糟糕", "难用", "问题",
        "bad", "terrible", "awful", "poor", "disappointing",
        "踩雷", "避雷", "无语", "坑爹"
    }
    
    def __init__(self):
        """初始化情感分析器"""
        logger.info("情感分析器初始化完成")
    
    def analyze(self, text: str) -> Dict:
        """分析文本情感
        
        Args:
            text: 待分析文本
            
        Returns:
            分析结果字典，        """
        try:
            # 提取关键词
            keywords = self._extract_keywords(text)
            
            # 计算情感分数
            positive_count = sum(1 for word in keywords if word in self.POSITIVE_WORDS)
            negative_count = sum(1 for word in keywords if word in self.NEGATIVE_WORDS)
            
            # 计算总分
            score = positive_count - negative_count
            
            # 判断情感
            if score > 0:
                sentiment = "positive"
            elif score < 0:
                sentiment = "negative"
            else:
                sentiment = "neutral"
            
            result = {
                "sentiment": sentiment,
                "score": score,
                "positive_count": positive_count,
                "negative_count": negative_count,
                "keywords": keywords,
                "confidence": self._calculate_confidence(keywords)
            }
            
            logger.info(f"情感分析完成: {sentiment} (score: {score})")
            return result
        
        except Exception as e:
            logger.error(f"情感分析失败: {e}")
            raise
    
    def _extract_keywords(self, text: str) -> List[str]:
        """提取关键词
        
        Args:
            text: 文本
            
        Returns:
            关键词列表
        """
        # 移除标点符号
        text = re.sub(r'[^\w\s]', '', text)
        
        # 分词（简单实现）
        words = text.lower().split()
        
        # 过滤停用词
        stopwords = {"的", "了", "是", "在", "有", "和", "就", "不", "都", "很", "the", "a", "an", "is", "are", "was", "were"}
        
        keywords = [word for word in words if word not in stopwords and len(word) > 1]
        
        return keywords
    
    def _calculate_confidence(self, keywords: List[str]) -> float:
        """计算置信度
        
        Args:
            keywords: 关键词列表
            
        Returns:
            置信度（0-1）
        """
        if not keywords:
            return 0.0
        
        # 基于关键词数量计算置信度
        confidence = min(len(keywords) / 10, 1.0)
        
        return round(confidence, 2)


# 测试代码
if __name__ == "__main__":
    # 初始化分析器
    analyzer = SentimentAnalyzer()
    
    # 测试文本
    test_texts = [
        "这个产品真的很好用！效果超级棒！",
        "This product is amazing! Love it so much!",
        "一般般吧，没什么特别的感觉",
        "太失望了，完全不推荐"
    ]
    
    for text in test_texts:
        result = analyzer.analyze(text)
        print(f"\n文本: {text}")
        print(f"情感: {result['sentiment']}")
        print(f"分数: {result['score']}")
        print(f"关键词: {result['keywords']}")
        print(f"置信度: {result['confidence']}")

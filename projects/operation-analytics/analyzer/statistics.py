"""
统计分析器模块

功能：
- 基础统计（均值/中位数/标准差）
- 高级统计（趋势/季节性)
- 数据聚合
- 异常检测
"""

import logging
from typing import Dict, List
import pandas as pd
import numpy as np
from scipy import stats

# 配置日志
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


class StatisticsAnalyzer:
    """统计分析器"""
    
    def __init__(self):
        """初始化统计分析器"""
        logger.info("统计分析器初始化完成")
    
    def analyze(self, df: pd.DataFrame) -> Dict:
        """
        执行统计分析
        
        Args:
            df: 数据DataFrame
            
        Returns:
            统计结果字典
        """
        try:
            logger.info("开始统计分析")
            
            result = {
                "basic": self._basic_stats(df),
                "advanced": self._advanced_stats(df),
                "aggregations": self._aggregate_stats(df),
                "anomalies": self._detect_anomalies(df)
            }
            
            logger.info("统计分析完成")
            return result
        
        except Exception as e:
            logger.error(f"统计分析失败: {e}")
            raise
    
    def _basic_stats(self, df: pd.DataFrame) -> Dict:
        """基础统计
        
        Args:
            df: 数据DataFrame
            
        Returns:
            基础统计结果
        """
        try:
            stats_result = {
                "count": len(df),
                "mean": float(df.mean()),
                "median": float(df.median()),
                "std": float(df.std()),
                "min": float(df.min()),
                "max": float(df.max())
            }
            
            logger.info("基础统计完成")
            return stats_result
        
        except Exception as e:
            logger.error(f"基础统计失败: {e}")
            raise
    
    def _advanced_stats(self, df: pd.DataFrame) -> Dict:
        """高级统计
        
        Args:
            df: 数据DataFrame
            
        Returns:
            高级统计结果
        """
        try:
            # 趋势分析（简化实现）
            trend = "上升" if df.iloc[-1] > df.iloc[0] else "下降"
            
            # 季节性分析（简化实现）
            seasonality = "存在" if len(df) > 10 else "未知"
            
            result = {
                "trend": trend,
                "seasonality": seasonality
            }
            
            logger.info("高级统计完成")
            return result
        
        except Exception as e:
            logger.error(f"高级统计失败: {e}")
            raise
    
    def _aggregate_stats(self, df: pd.DataFrame) -> Dict:
        """聚合统计
        
        Args:
            df: 数据DataFrame
            
        Returns:
            聚合统计结果
        """
        try:
            # 按时间聚合（假设有date列）
            if 'date' in df.columns:
                df['date'] = pd.to_datetime(df['date'])
                daily_stats = df.groupby(df['date'].dt.date).size().to_dict()
            else:
                daily_stats = {}
            
            result = {
                "daily": daily_stats
            }
            
            logger.info("聚合统计完成")
            return result
        
        except Exception as e:
            logger.error(f"聚合统计失败: {e}")
            raise
    
    def _detect_anomalies(self, df: pd.DataFrame) -> List:
        """异常检测
        
        Args:
            df: 数据DataFrame
            
        Returns:
            异常值列表
        """
        try:
            # 使用Z-score检测异常
            z_scores = np.abs(stats.zscore(df.select_dtypes(include=[np.number])))
            anomalies = df[z_scores > 3].index.tolist()
            
            logger.info(f"检测到 {len(anomalies)}个异常")
            return anomalies
        
        except Exception as e:
            logger.error(f"异常检测失败: {e}")
            raise

"""
图表可视化器模块

功能：
- 生成折线图
- 生成柱状图
- 生成饼图
- 保存为图片文件
"""

import logging
from typing import Dict, List
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns

# 配置日志
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


class ChartVisualizer:
    """图表可视化器"""
    
    def __init__(self, output_dir: str = "output/charts"):
        """
        初始化图表可视化器
        
        Args:
            output_dir: 图表输出目录
        """
        self.output_dir = output_dir
        os.makedirs(output_dir, exist_ok=True)
        logger.info("图表可视化器初始化完成")
    
    def visualize(self, stats: Dict, predictions: Dict) -> List[str]:
        """
        生成可视化图表
        
        Args:
            stats: 统计数据
            predictions: 预测数据
            
        Returns:
            图表文件路径列表
        """
        try:
            chart_paths = []
            
            # 1. 折线图（趋势）
            line_chart = self._create_line_chart(stats, predictions)
            chart_paths.append(line_chart)
            
            # 2. 柱状图（对比）
            bar_chart = self._create_bar_chart(stats)
            chart_paths.append(bar_chart)
            
            # 3. 饼图（分布)
            pie_chart = self._create_pie_chart(stats)
            chart_paths.append(pie_chart)
            
            logger.info(f"生成 {len(chart_paths)}个图表")
            return chart_paths
        
        except Exception as e:
            logger.error(f"图表生成失败: {e}")
            raise
    
    def _create_line_chart(self, stats: Dict, predictions: Dict) -> str:
        """创建折线图"""
        try:
            plt.figure(figsize=(12, 6))
            
            # 历史数据
            dates = stats.get("dates", [])
            values = stats.get("values", [])
            plt.plot(dates, values, label="历史数据", marker='o')
            
            # 预测数据
            future_dates = predictions.get("dates", [])
            future_values = predictions.get("values", [])
            plt.plot(future_dates, future_values, label="预测数据", marker='x', linestyle='--')
            
            plt.title("数据趋势预测")
            plt.xlabel("日期")
            plt.ylabel("数值")
            plt.legend()
            plt.grid(True)
            
            chart_path = f"{self.output_dir}/line_chart.png"
            plt.savefig(chart_path)
            plt.close()
            
            logger.info(f"折线图已保存: {chart_path}")
            return chart_path
        
        except Exception as e:
            logger.error(f"折线图创建失败: {e}")
            raise
    
    def _create_bar_chart(self, stats: Dict) -> str:
        """创建柱状图"""
        try:
            plt.figure(figsize=(10, 6))
            
            categories = list(stats.get("categories", {}).keys())
            values = list(stats.get("categories", {}).values())
            
            plt.bar(categories, values, color='skyblue')
            plt.title("分类数据对比")
            plt.xlabel("类别")
            plt.ylabel("数值")
            plt.xticks(rotation=45)
            
            chart_path = f"{self.output_dir}/bar_chart.png"
            plt.savefig(chart_path)
            plt.close()
            
            logger.info(f"柱状图已保存: {chart_path}")
            return chart_path
        
        except Exception as e:
            logger.error(f"柱状图创建失败: {e}")
            raise
    
    def _create_pie_chart(self, stats: Dict) -> str:
        """创建饼图"""
        try:
            plt.figure(figsize=(8, 8))
            
            labels = list(stats.get("distribution", {}).keys())
            sizes = list(stats.get("distribution", {}).values())
            
            plt.pie(sizes, labels=labels, autopct='%1.1f%%')
            plt.title("数据分布")
            
            chart_path = f"{self.output_dir}/pie_chart.png"
            plt.savefig(chart_path)
            plt.close()
            
            logger.info(f"饼图已保存: {chart_path}")
            return chart_path
        
        except Exception as e:
            logger.error(f"饼图创建失败: {e}")
            raise

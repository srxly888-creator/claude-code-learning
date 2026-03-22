"""
运营数据分析助手 - 主程序

功能：
- 数据采集（数据库/API）
- 统计分析（基础/高级）
- 预测分析（时间序列)
- 可视化（图表生成)
- 报告生成
"""

import logging
from typing import Dict, List, Optional
import os
import sys

# 配置日志
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)


class OperationAnalyticsAssistant:
    """运营数据分析助手"""
    
    def __init__(self, config_path: str = "config/data-sources.yaml"):
        """
        初始化运营数据分析助手
        
        Args:
            config_path: 数据源配置文件路径
        """
        self.config = self._load_config(config_path)
        self.collector = DatabaseCollector(self.config['database'])
        self.analyzer = StatisticsAnalyzer()
        self.predictor = PredictionAnalyzer()
        self.visualizer = ChartVisualizer()
        self.reporter = ReportGenerator()
        
        logger.info("运营数据分析助手初始化完成")
    
    def _load_config(self, config_path: str) -> Dict:
        """加载配置文件
        
        Args:
            config_path: 配置文件路径
            
        Returns:
            配置字典
        """
        try:
            with open(config_path, 'r', encoding='utf-8') as f:
                config = yaml.safe_load(f)
                logger.info(f"配置加载成功: {config_path}")
                return config
        except FileNotFoundError:
            logger.error(f"配置文件不存在: {config_path}")
            raise
        except yaml.YAMLError as e:
            logger.error(f"配置文件格式错误: {e}")
            raise
    
    def analyze(self, data_source: str = "database", query: Optional[str] = None):
        """
        执行数据分析
        
        Args:
            data_source: 数据源类型（database/api）
            query: 查询条件
            
        Returns:
            分析结果
        """
        try:
            # 1. 数据采集
            logger.info(f"开始采集数据: {data_source}")
            if data_source == "database":
                data = self.collector.collect(query)
            else:
                data = self.collector.collect_from_api(query)
            
            # 2. 统计分析
            logger.info("开始统计分析")
            stats = self.analyzer.analyze(data)
            
            # 3. 预测分析
            logger.info("开始预测分析")
            predictions = self.predictor.predict(data)
            
            # 4. 可视化
            logger.info("开始生成可视化")
            charts = self.visualizer.visualize(stats, predictions)
            
            # 5. 生成报告
            logger.info("开始生成报告")
            report = self.reporter.generate(stats, predictions, charts)
            
            logger.info("数据分析完成")
            return {
                "data": data,
                "statistics": stats,
                "predictions": predictions,
                "charts": charts,
                "report": report
            }
        
        except Exception as e:
            logger.error(f"数据分析失败: {e}")
            raise
    
    def generate_report(self, output_path: str = "analytics_report.md"):
        """
        生成分析报告
        
        Args:
            output_path: 报告输出路径
        """
        try:
            result = self.analyze()
            
            # 保存报告
            with open(output_path, 'w', encoding='utf-8') as f:
                f.write(result['report'])
            
            logger.info(f"报告已保存: {output_path}")
        
        except Exception as e:
            logger.error(f"报告生成失败: {e}")
            raise


if __name__ == "__main__":
    # 初始化助手
    assistant = OperationAnalyticsAssistant(
        config_path="config/data-sources.yaml"
    )
    
    # 执行分析
    result = assistant.analyze(
        data_source="database",
        query="SELECT * FROM sales_data WHERE date > '2024-01-01'"
    )
    
    # 生成报告
    assistant.generate_report("output/analytics_report.md")
    
    print("分析完成！查看 output/analytics_report.md")

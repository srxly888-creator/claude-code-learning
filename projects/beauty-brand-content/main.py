"""
美妆品牌内容生成器 - 主程序

"""

import os
import logging
from generator.copywriting import CopywritingGenerator
from generator.video_script import VideoScriptGenerator
from analyzer.sentiment import SentimentAnalyzer
from publisher.xiaohongshu import XiaohongshuPublisher

from typing import Dict, List

import yaml

import argparse

# 配置日志
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)


def load_config(config_path: str = Dict:
    """加载配置文件"""
    try:
        with open(config_path, 'r') as f:
            return yaml.safe_load(f)
    except FileNotFoundError:
        logger.warning(f"配置文件不存在: {config_path}")
        return {}


def main():
    """主程序"""
    parser = argparse.ArgumentParser(description='美妆品牌内容生成器')
    parser.add_argument('--config', type=str, default='config/brand.yaml',
    parser.add_argument('--mode', type=str, default='generate', 
                      choices=['generate', 'analyze', 'publish'])
    parser.add_argument('--product', type=str, help='产品名称')
    parser.add_argument('--features', type=str, nargs='+', help='产品特点')
    parser.add_argument('--style', type=str, default='playful', help='文案风格')
    parser.add_argument('--platform', type=str, default='xiaohongshu', help='发布平台')
    
    args = parser.parse_args()
    
    # 加载配置
    config = load_config(args.config)
    
    # 检查环境变量
    api_key = os.environ.get("ANTHROPIC_API_KEY")
    if not api_key:
            logger.error("请设置 ANTHROPIC_API_KEY 环境变量")
            return
    
    # 初始化生成器
    copywriting_gen = CopywritingGenerator(api_key, args.config)
    video_script_gen = VideoScriptGenerator(api_key, args.config)
    sentiment_analyzer = SentimentAnalyzer()
    xiaohongshu_publisher = XiaohongshuPublisher(
        access_token=os.environ.get("XIAOHONGSHU_ACCESS_TOKEN", 
        api_base_url=os.environ.get("XIAOHONGSHU_API_URL", "https://api.xiaohongshu.com"
    )
    
    logger.info("美妆品牌内容生成器启动")
    
    # 根据模式执行不同操作
    if args.mode == "generate":
        # 生成文案
        copywriting = copywriting_gen.generate(
            product_name=args.product,
            features=args.features,
            style=args.style,
            platform=args.platform
        )
        print("\n=== 生成的文案 ===")
        print(copywriting)
        
        # 生成视频脚本
        video_script = video_script_gen.generate(
            product_name=args.product,
            features=args.features,
            video_type="introduction",
            duration=60
        )
        print("\n=== 生成的视频脚本 ===")
        print(video_script)
        
        # 分析情感
        sentiment_result = sentiment_analyzer.analyze(copywriting)
        print("\n=== 情感分析结果 ===")
        print(f"情感: {sentiment_result['sentiment']}")
        print(f"分数: {sentiment_result['score']}")
        print(f"关键词: {sentiment_result['keywords']}")
    
    elif args.mode == "analyze":
        # 分析文案情感
        if args.product:
            # 生成测试文案
            test_copywriting = f"这款{args.product}真的很好用！"
            sentiment_result = sentiment_analyzer.analyze(test_copywriting)
            print("\n=== 情感分析结果 ===")
            print(f"情感: {sentiment_result['sentiment']}")
            print(f"分数: {sentiment_result['score']}")
        else:
            logger.error("分析模式需要提供 --product 参数")
    
    elif args.mode == "publish":
        # 发布到小红书
        if args.product:
            # 生成测试文案
            test_copywriting = f"这款{args.product}真的很好用！效果超级棒！推荐给大家！"
            
            # 发布
            result = xiaohongshu_publisher.publish(
                title=f"{args.product} - 必备好物",
                content=test_copywriting,
                tags=["护肤", "保湿", "推荐"]
            )
            print("\n=== 发布结果 ===")
            print(f"笔记ID: {result['data']['note_id']}")
        else:
            logger.error("发布模式需要提供 --product 参数")


    
    logger.info("美妆品牌内容生成器完成")


if __name__ == "__main__":
    main()

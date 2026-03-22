"""
文案生成器模块

功能：
- 生成多种风格的文案（专业/活泼/优雅）
- 支持多平台格式（小红书/抖音/微博）
- 包含完整的错误处理和日志记录
"""

import logging
from typing import Dict, List, Optional
from anthropic import Anthropic
import yaml
import os

# 配置日志
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


class CopywritingGenerator:
    """文案生成器"""
    
    def __init__(self, api_key: str, config_path: str = "config/brand.yaml"):
        """
        初始化文案生成器
        
        Args:
            api_key: Claude API密钥
            config_path: 品牌配置文件路径
        """
        self.client = Anthropic(api_key=api_key)
        self.config = self._load_config(config_path)
        logger.info("文案生成器初始化完成")
    
    def _load_config(self, config_path: str) -> Dict:
        """加载品牌配置
        
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
    
    def generate(
        self,
        product_name: str,
        features: List[str],
        style: str = "professional",
        platform: str = "xiaohongshu"
    ) -> str:
        """生成文案
        
        Args:
            product_name: 产品名称
            features: 产品特点列表
            style: 文案风格（professional/playful/elegant）
            platform: 发布平台（xiaohongshu/douyin/weibo）
            
        Returns:
            生成的文案
        """
        try:
            # 构建提示词
            prompt = self._build_prompt(product_name, features, style. platform)
            
            logger.info(f"开始生成文案: {product_name}, 风格: {style}")
            
            # 调用Claude API
            response = self.client.messages.create(
                model="claude-3-5-sonnet-20241022",
                max_tokens=1024,
                messages=[
                    {"role": "user", "content": prompt}
                ]
            )
            
            # 提取文案
            copywriting = response.content[0].text
            
            logger.info("文案生成成功")
            return copywriting
        
        except Exception as e:
            logger.error(f"文案生成失败: {e}")
            raise
    
    def _build_prompt(
        self,
        product_name: str,
        features: List[str],
        style: str,
        platform: str
    ) -> str:
        """构建提示词
        
        Args:
            product_name: 产品名称
            features: 产品特点
            style: 文案风格
            platform: 发布平台
            
        Returns:
            完整的提示词
        """
        # 平台特定要求
        platform_requirements = {
            "xiaohongshu": "小红书风格：亲切、真实、种草感强",
            "douyin": "抖音风格：节奏快、吸引眼球、有话题性",
            "weibo": "微博风格：简洁、有趣、易传播"
        }
        
        # 风格描述
        style_descriptions = {
            "professional": "专业、权威、值得信赖",
            "playful": "活泼、有趣、年轻化",
            "elegant": "优雅、高端、有品质感"
        }
        
        # 构建提示词
        prompt = f"""
你是一个专业的{platform_requirements.get(platform, '社交媒体')}文案撰写专家。

产品信息：
- 产品名称: {product_name}
- 产品特点: {', '.join(features)}

要求：
1. 文案风格: {style_descriptions.get(style, style)}
2. {platform_requirements.get(platform, '')}
3. 包含emoji表情符号
4. 字数控制在100-200字之间
5. 包含3-5个相关标签

请生成一条{platform}文案。
"""
        return prompt


# 测试代码
if __name__ == "__main__":
    # 初始化生成器
    generator = CopywritingGenerator(
        api_key=os.environ.get("ANTHROPIC_API_KEY"),
        config_path="config/brand.yaml"
    )
    
    # 生成文案
    copywriting = generator.generate(
        product_name="水光肌底液",
        features=["保湿效果好", "质地轻薄", "适合敏感肌"],
        style="playful",
        platform="xiaohongshu"
    )
    
    print("生成的文案:")
    print(copywriting)

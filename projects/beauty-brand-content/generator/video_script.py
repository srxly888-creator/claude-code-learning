"""
视频脚本生成器模块

功能：
- 生成小红书风格的视频脚本
- 包含镜头描述、旁白、字幕
- 支持多种视频类型（产品介绍/使用教程/测评）
"""

import logging
from typing import Dict, List, Optional
from anthropic import Anthropic
import yaml
import os

# 配置日志
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


class VideoScriptGenerator:
    """视频脚本生成器"""
    
    def __init__(self, api_key: str, config_path: str = "config/brand.yaml"):
        """
        初始化视频脚本生成器
        
        Args:
            api_key: Claude API密钥
            config_path: 品牌配置文件路径
        """
        self.client = Anthropic(api_key=api_key)
        self.config = self._load_config(config_path)
        logger.info("视频脚本生成器初始化完成")
    
    def _load_config(self, config_path: str) -> Dict:
        """加载品牌配置
        
        Args:
            config_path: 配置文件路径
            
        Returns:
            配置字典
        """
        try:
            with open(config_path, 'r') as f:
                return yaml.safe_load(f)
        except FileNotFoundError:
            logger.warning(f"配置文件不存在: {config_path}")
            return {}
    
    def generate(
        self,
        product_name: str,
        features: List[str],
        video_type: str = "introduction",
        duration: int = 60
    ) -> str:
        """生成视频脚本
        
        Args:
            product_name: 产品名称
            features: 产品特点
            video_type: 视频类型（introduction/tutorial/review）
            duration: 视频时长（秒）
            
        Returns:
            完整的视频脚本
        """
        try:
            # 构建提示词
            prompt = self._build_prompt(product_name, features, video_type, duration)
            
            logger.info(f"开始生成视频脚本: {product_name}")
            
            # 调用Claude API
            response = self.client.messages.create(
                model="claude-3-5-sonnet-20241022",
                max_tokens=2000,
                messages=[
                    {"role": "user", "content": prompt}
                ]
            )
            
            # 提取脚本
            script = response.content[0].text
            
            logger.info("视频脚本生成成功")
            return script
        
        except Exception as e:
            logger.error(f"视频脚本生成失败: {e}")
            raise
    
    def _build_prompt(
        self,
        product_name: str,
        features: List[str],
        video_type: str,
        duration: int
    ) -> str:
        """构建提示词
        
        Args:
            product_name: 产品名称
            features: 产品特点
            video_type: 视频类型
            duration: 视频时长
            
        Returns:
            完整的提示词
        """
        video_type_descriptions = {
            "introduction": "产品介绍视频",
            "tutorial": "使用教程视频",
            "review": "产品测评视频"
        }
        
        prompt = f"""
你是一位专业的小红书视频脚本撰写专家。

视频信息：
- 产品名称: {product_name}
- 产品特点: {', '.join(features)}
- 视频类型: {video_type_descriptions.get(video_type, video_type)}
- 视频时长: {duration}秒

要求：
1. 包含开场白（3秒）
2. 分镜头描述（每个镜头5-10秒）
3. 包含旁白文案
4. 包含字幕提示
5. 包含结尾（5秒）
6. 适合小红书平台风格
7. 包含emoji表情符号

8. 总时长控制在{duration}秒左右

请生成一个完整的视频脚本，包括：
- 镜头编号
- 镜头描述
- 旁白文案
- 字幕提示
- 时长（秒）
"""
        return prompt


# 测试代码
if __name__ == "__main__":
    # 初始化生成器
    generator = VideoScriptGenerator(
        api_key=os.environ.get("ANTHROPIC_API_KEY"),
        config_path="config/brand.yaml"
    )
    
    # 生成视频脚本
    script = generator.generate(
        product_name="水光肌底液",
        features=["保湿效果好", "质地轻薄", "适合敏感肌"],
        video_type="introduction",
        duration=60
    )
    
    print("生成的视频脚本:")
    print(script)

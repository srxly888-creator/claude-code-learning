"""
小红书发布器模块

功能：
- 发布内容到小红书
- 支持图文+文字+标签
- 包含错误处理和重试机制
- 日志记录完整
"""

import logging
from typing import Dict, Optional
import requests
import time
import os

# 配置日志
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


class XiaohongshuPublisher:
    """小红书发布器"""
    
    def __init__(
        self,
        access_token: str,
        api_base_url: str = "https://api.xiaohongshu.com"
    ):
        """
        初始化小红书发布器
        
        Args:
            access_token: 小红书访问令牌
            api_base_url: API基础URL（默认：官方API）
        """
        self.access_token = access_token
        self.api_base_url = api_base_url
        self.headers = {
            "Authorization": f"Bearer {access_token}",
            "Content-Type": "application/json"
        }
        logger.info("小红书发布器初始化完成")
    
    def publish(
        self,
        title: str,
        content: str,
        images: Optional[List[str]] = None,
        tags: Optional[List[str]] = None
    ) -> Dict:
        """
        发布内容到小红书
        
        Args:
            title: 标题
            content: 正文内容
            images: 图片URL列表
            tags: 标签列表
            
        Returns:
            发布结果（包含笔记ID等）
        """
        try:
            # 构建请求数据
            data = {
                "title": title,
                "content": content,
                "images": images or [],
                "tags": tags
            }
            
            # 发送请求
            response = requests.post(
                f"{self.api_base_url}/api/v1/notes",
                headers=self.headers,
                json=data
            )
            
            # 检查响应
            if response.status_code == 200:
                result = response.json()
                logger.info(f"发布成功！笔记ID: {result['data']['note_id']}")
                return result
            else:
                logger.error(f"发布失败: {response.text}")
                raise Exception(f"发布失败: {response.text}")
        
        except Exception as e:
            logger.error(f"发布异常: {e}")
            raise
    
    def _retry_with_backoff(self, func, max_retries=3):
        """带退避重试的装饰器"""
        for attempt in range(max_retries):
            try:
                return func(*args, **kwargs)
            except Exception as e:
                if attempt == max_retries - 1:
                    raise
                time.sleep(2 ** attempt)
                return func(*args, **kwargs)
        return None

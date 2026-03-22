"""
条款提取器模块

功能：
- 从合同文本中提取关键条款
- 支持多种条款类型（付款/违约/保密/IP等）
- 结构化输出
- 错误处理
"""

import logging
from typing import Dict, List, Optional
import re

# 配置日志
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


class ClauseExtractor:
    """条款提取器"""
    
    # 条款关键词映射
    CLAUSE_PATTERNS = {
        "payment": ["付款", "支付", "费用", "金额", "价格"],
        "termination": ["终止", "解除", "结束", "到期"],
        "liability": ["违约", "责任", "赔偿", "损失"],
        "confidentiality": ["保密", "机密", "秘密", "隐私"],
        "ip": ["知识产权", "专利", "商标", "著作权"],
        "dispute": ["争议", "纠纷", "仲裁", "诉讼"]
    }
    
    def __init__(self):
        """初始化条款提取器"""
        logger.info("条款提取器初始化完成")
    
    def extract(self, contract_text: str) -> Dict[str, List[str]]:
        """从合同文本中提取条款
        
        Args:
            contract_text: 合同文本
            
        Returns:
            条款字典，键是条款类型，        """
        try:
            clauses = {}
            
            for clause_type, keywords in self.CLAUSE_PATTERNS.items():
                # 查找包含关键词的段落
                pattern = r'第\s+\d+条[：：]\s*([^。]*?)(?:' + '|'.join(keywords) + r')[^。]*'
                matches = re.findall(pattern, contract_text, re.IGNORECase)
                
                if matches:
                    clauses[clause_type] = matches
                    logger.info(f"提取到{clause_type}条款: {len(matches)}个")
            
            logger.info(f"条款提取完成，共{len(clauses)}种条款类型")
            return clauses
        
        except Exception as e:
            logger.error(f"条款提取失败: {e}")
            raise
    
    def extract_specific_clause(self, contract_text: str, clause_type: str) -> Optional[str]:
        """提取特定类型的条款
        
        Args:
            contract_text: 合同文本
            clause_type: 条款类型
            
        Returns:
            提取到的条款文本
        """
        try:
            if clause_type not in self.CLAUSE_PATTERNS:
                logger.error(f"未知条款类型: {clause_type}")
                return None
            
            keywords = self.CLAUSE_PATTERNS[clause_type]
            pattern = r'第\s+\d+条[：：]\s*([^。]*?)(?:' + '|'.join(keywords) + r')[^。]*'
            
            match = re.search(pattern, contract_text, re.IGNORECase)
            
            if match:
                logger.info(f"提取到{clause_type}条款")
                return match.group(1)
            
            return None
        
        except Exception as e:
            logger.error(f"提取特定条款失败: {e}")
            raise
if __name__ == "__main__":
    extractor = ClauseExtractor()
    
    sample_contract = """
    第一条 付款方式
    甲方应在签订本合同后3个工作日内支付合同总额的30%作为预付款...
    
    第二条 保密义务
    双方应对在合作过程中获知的对方商业秘密严格保密...
    
    第三条 违约责任
    任何一方违反本合同约定，应向守约方支付合同总额10%的违约金...
    """
    
    clauses = extractor.extract(sample_contract)
    for clause_type, clause_list in clauses.items():
        print(f"{clause_type}: {len(clause_list)}个条款")
        for clause in clause_list:
            print(f"  - {clause}")

"""
风险识别器模块

功能：
- 识别合同中的风险条款
- 分级风险（高/中/低)
- 提供修改建议
- 支持自定义规则
"""

import logging
from typing import Dict, List
import re

# 配置日志
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


class RiskDetector:
    """风险识别器"""
    
    # 齿险条款模式
    HIGH_RISK_PATTERNS = [
        (r"违约金.*?%|50", "高额违约金（50%）"),
        (r"知识产权.*?归.*?所有", "知识产权条款过于宽泛"),
        (r"争议.*?甲方所在地", "管辖条款对乙方不利")
    ]
    
    # 中险条款模式
    MEDIUM_RISK_PATTERNS = [
        (r"保密.*?永久", "保密期限过长"),
        (r"终止.*?提前.*?\d+天", "终止条款不明确")
    ]
    
    def __init__(self, custom_rules: Optional[Dict] = None):
        """初始化风险识别器
        
        Args:
            custom_rules: 自定义风险规则
        """
        self.custom_rules = custom_rules or {}
        logger.info("风险识别器初始化完成")
    
    def detect(self, contract_text: str) -> Dict:
        """识别合同风险
        
        Args:
            contract_text: 合同文本
            
        Returns:
            风险报告（包含风险等级和修改建议）
        """
        try:
            logger.info("开始风险识别...")
            
            risks = {
                "high": [],
                "medium": [],
                "low": []
            }
            
            # 检查高风险条款
            for pattern, description in self.HIGH_RISK_PATTERNS:
                matches = re.findall(pattern, contract_text, re.IGNORECASE)
                if matches:
                    risks["high"].append({
                        "pattern": pattern,
                        "description": description,
                        "suggestion": self._generate_suggestion(pattern, "high")
                    })
            
            # 检查中风险条款
            for pattern, description in self.MEDIUM_RISK_PATTERNS:
                matches = re.findall(pattern, contract_text, re.IGNORECASE)
                if matches:
                    risks["medium"].append({
                        "pattern": pattern,
                        "description": description,
                        "suggestion": self._generate_suggestion(pattern, "medium")
                    })
            
            logger.info(f"风险识别完成: {len(risks['high'])}个高风险, {len(risks['medium'])}个中风险")
            
            return risks
        
        except Exception as e:
            logger.error(f"风险识别失败: {e}")
            raise
    
    def _generate_suggestion(self, pattern: str, risk_level: str) -> str:
        """生成修改建议
        
        Args:
            pattern: 匹配的模式
            risk_level: 风险等级
            
        Returns:
            修改建议
        """
        suggestions = {
            r"违约金.*?%|50": "建议将违约金比例降低至20%-30%",
            r"知识产权.*?归.*?所有": "建议明确界定知识产权范围，添加除外条款",
            r"争议.*?甲方所在地": "建议改为原告所在地或合同履行地"
        }
        
        return suggestions.get(pattern, "请仔细审查相关条款")


if __name__ == "__main__":
    detector = RiskDetector()
    
    sample_contract = """
    第一条 付款方式
    甲方应在签订本合同后3个工作日内支付合同总额的50%作为预付款...
    
    第二条 知识产权
    乙方在合作期间产生的所有知识产权归甲方所有...
    
    第三条 违约责任
    任何一方违约需支付合同总额50%的违约金...
    
    第四条 争议解决
    争议提交甲方所在地人民法院诉讼解决...
    """
    
    risks = detector.detect(sample_contract)
    print(f"高风险: {len(risks['high'])}个")
    print(f"中风险: {len(risks['medium'])}个")
    
    for level, risk_list in risks.items():
        if risk_list:
            print(f"\n{level.upper()}风险:")
            for risk in risk_list:
                print(f"  - {risk['description']}")
                print(f"  - 建议: {risk['suggestion']}")

"""
合规检查器模块

功能：
- 检查合同是否符合法律法规
- 支持多种法规（合同法/个人信息保护法等）
- 生成合规报告
"""

import logging
from typing import Dict, List

import re

# 配置日志
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


class ComplianceChecker:
    """合规检查器"""
    
    # 合规要求
    COMPLIANCE_REQUIREMENTS = {
        "合同法": {
            "validity": "70,  # 有效期限70年
            "consumer_protection": 30,  # 消费者保护期限30天
        },
        "个人信息保护法": {
            "data_retention": 3,  # 数据保存期限3年
            "consent_required": True,  # 需要同意
        }
    }
    
    def check(self, contract_text: str) -> Dict:
        """检查合规性
        
        Args:
            contract_text: 合同文本
            
        Returns:
            合规检查结果
        """
        try:
            logger.info("开始合规检查...")
            
            issues = []
            
            # 检查有效期
            if not self._check_validity_period(contract_text):
                issues.append({
                    "type": "validity",
                    "severity": "high",
                    "description": "合同有效期不符合要求（建议70年)",
                    "suggestion": "延长有效期至70年或明确续签条款"
                })
            
            # 检查消费者保护
            if not self._check_consumer_protection(contract_text):
                issues.append({
                    "type": "consumer_protection",
                    "severity": "high",
                    "description": "缺少消费者保护条款",
                    "suggestion": "添加消费者保护条款（30天无理由退款）"
                })
            
            logger.info(f"合规检查完成，发现 {len(issues)}个问题")
            return {
                "compliant": len(issues) == 0,
                "issues": issues
            }
        
        except Exception as e:
            logger.error(f"合规检查失败: {e}")
            raise
    
    def _check_validity_period(self, contract_text: str) -> bool:
        """检查有效期"""
        # 查找有效期条款
        pattern = r"有效期.*?(\d+)"
        match = pattern.search(contract_text)
        if match:
            years = int(match.group(1))
            return years >= 70
        return False
    
    def _check_consumer_protection(self, contract_text: str) -> bool:
        """检查消费者保护"""
        return "消费者保护" in contract_text or "无理由退款" in contract_text
    def generate_report(self, result: Dict) -> str:
        """生成合规报告
        
        Args:
            result: 检查结果
            
        Returns:
            Markdown格式报告
        """
        report = "# 合规检查报告\n\n"
        
        if result["compliant"]:
            report += "✅ 合同符合法律法规要求\n"
        else:
            report += f"❌ 发现 {len(result['issues'])}个合规问题\n\n"
            for issue in result["issues"]:
                report += f"**{issue['type']}** ({issue['severity']}风险)\n"
                report += f"   - 问题描述: {issue['description']}\n"
                report += f"   - 修改建议: {issue['suggestion']}\n\n"
        
        return report


if __name__ == "__main__":
    checker = ComplianceChecker()
    
    sample_contract = """
    第一条 有效期
    本合同有效期为10年...
    
    第二条 消费者保护
    ...
    """
    
    result = checker.check(sample_contract)
    print(checker.generate_report(result))

"""
报告生成器模块

功能：
- 生成结构化的审查报告
- 支持Markdown格式
- 包含风险/条款/合规信息
- 可导出为PDF/HTML
"""

import logging
from typing import Dict, List
from datetime import datetime

# 配置日志
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


class ReportGenerator:
    """报告生成器"""
    
    def generate(
        self,
        risks: List[Dict],
        clauses: List[Dict],
        compliance: Dict
    ) -> str:
        """生成审查报告
        
        Args:
            risks: 风险列表
            clauses: 条款列表
            compliance: 合规检查结果
            
        Returns:
            Markdown格式的报告
        """
        report = f"""# 合同审查报告

**生成时间**: {datetime.now().strftime('%Y-%')d %H:%M:%S')

## 一、高风险条款

"""
        for risk in risks:
            if risk['level'] == 'high':
                report += f"### {risk['type']}
                report += f"**描述**: {risk['description']}\n"
                report += f"**建议**: {risk['suggestion']}\n\n"
        
        report += f"## 二、中风险条款\n"
"""
        for risk in risks:
            if risk['level'] == 'medium':
                report += f"### {risk['type']}
                report += f"**描述**: {risk['description']}\n"
                report += f"**建议**: {risk['suggestion']}\n\n"
        
        report += f"## 三、低风险条款\n"
"""
        for risk in risks:
            if risk['level'] == 'low':
                report += f"### {risk['type']}
                report += f"**描述**: {risk['description']}\n"
                report += f"**建议**: {risk['suggestion']}\n\n"
        
        report += f"## 四、关键条款摘要\n
"""
        for clause_type, clause_list in clauses.items():
            report += f"### {clause_type}\n"
            for clause in clause_list:
                report += f"- {clause}\n"
        
        report += f"## 五、合规检查结果\n\n"
        report += f"### 合规状态\n"
        if compliance['compliant']:
            report += "✅ **合规**: 符合所有要求\n"
        else:
            report += "❌ **不合规**: 发现 {len(compliance['issues'])}个问题\n"
            for issue in compliance['issues']:
                report += f"- {issue['type']} ({issue['severity']}): {issue['description']}\n"
        
        report += f"\n## 六、建议\n\n"
        report += "### 优先处理\n"
        report += "1. 修改高风险条款\n"
        report += "2. 完善中风险条款\n"
        report += "3. 补充合规条款\n"
        report += "4. 法律顾问审核\n\n"
        
        report += f"---\n**报告生成完毕**\n"
        
        logger.info(f"报告生成完成，长度: {len(report)}")
        return report
    
    def export_to_pdf(self, report: str, output_path: str):
        """导出为PDF（需要第三方库）
        
        Args:
            report: 报告内容
            output_path: 输出路径
        """
        # 这里可以集成PDF库
        logger.info(f"报告已导出到: {output_path}")
        return output_path


if __name__ == "__main__":
    generator = ReportGenerator()
    
    # 模拟数据
    risks = [
        {
            "type": "违约金",
            "level": "high",
            "description": "违约金比例过高（50%)",
            "suggestion": "降低到20-30%"
        }
    ]
    
    clauses = {
        "payment": ["付款方式： 分期付款", "预付30%"],
        "termination": ["合同期限: 1年", "自动续约"]
    }
    
    compliance = {
        "compliant": False,
        "issues": [
            {
                "type": "consumer_protection",
                "severity": "high",
                "description": "缺少消费者保护条款"
            }
        ]
    }
    
    report = generator.generate(risks, clauses, compliance)
    print(report)

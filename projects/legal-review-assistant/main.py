"""
合同审查助手 - 主程序

功能：
- PDF合同解析
- 条款提取
- 风险识别
- 合规检查
- 报告生成
"""

import os
import logging
from parser.pdf_parser import PDFParser
from parser.clause_extractor import ClauseExtractor
from analyzer.risk_detector import RiskDetector
from analyzer.compliance_checker import ComplianceChecker
from generator.report_generator import ReportGenerator

# 配置日志
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)


def main():
    """主程序"""
    logger.info("=" * 60)
    logger.info("合同审查助手启动")
    logger.info("=" * 60)
    
    # 初始化组件
    pdf_parser = PDFParser()
    clause_extractor = ClauseExtractor()
    risk_detector = RiskDetector()
    compliance_checker = ComplianceChecker()
    report_generator = ReportGenerator()
    
    # 示例：审查合同
    contract_path = "sample_contract.pdf"
    
    try:
        # 1. 解析PDF
        logger.info(f"解析合同: {contract_path}")
        text = pdf_parser.parse(contract_path)
        
        # 2. 提取条款
        logger.info("提取关键条款...")
        clauses = clause_extractor.extract(text)
        
        # 3. 风险识别
        logger.info("识别风险条款...")
        risks = risk_detector.detect(clauses)
        
        # 4. 合规检查
        logger.info("检查合规性...")
        compliance = compliance_checker.check(clauses)
        
        # 5. 生成报告
        logger.info("生成审查报告...")
        report = report_generator.generate(
            contract_path=contract_path,
            clauses=clauses,
            risks=risks,
            compliance=compliance
        )
        
        # 保存报告
        report_path = "review_report.md"
        with open(report_path, 'w', encoding='utf-8') as f:
            f.write(report)
        
        logger.info(f"审查完成！报告已保存: {report_path}")
        
    except Exception as e:
        logger.error(f"审查失败: {e}")
        raise


if __name__ == "__main__":
    main()

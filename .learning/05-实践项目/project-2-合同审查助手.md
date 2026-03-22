# 实践项目 2: 合同审查助手

> **难度**: ⭐⭐⭐⭐
> **预计时间**: 5-7 天
> **技术栈**: Python + FastAPI + Claude Code CLI + PDF/Word 解析

---

## 🎯 项目目标

构建一个智能合同审查系统，实现：
1. **自动解析**: PDF/Word → 结构化文本
2. **风险识别**: 自动识别风险条款
3. **合规检查**: 对比法规库
4. **报告生成**: 自动化审查报告

**预期效果**: 审查时间 **2小时 → 10分钟**（**12x**）

---

## 📋 功能清单

### **核心功能（MVP）**
- [x] PDF/Word 合同解析
- [x] 条款自动提取
- [x] 基础风险识别
- [x] 审查报告生成

### **进阶功能**
- [ ] 深度条款分析
- [ ] 法规库集成
- [ ] 批量审查
- [ ] 历史对比

### **高级功能**
- [ ] 智能推荐
- [ ] 自定义规则
- [ ] 多语言支持
- [ ] API 接口

---

## 🏗️ 项目结构

```
legal-review-assistant/
├── README.md
├── requirements.txt
├── .env.example
├── config/
│   ├── legal-rules.yaml          # 法规库
│   ├── risk-patterns.yaml        # 风险模式
│   ├── compliance-rules.yaml     # 合规规则
│   └── templates/
│       ├── review-report.md      # 审查报告模板
│       └── legal-opinion.md      # 法律意见书模板
├── src/
│   ├── __init__.py
│   ├── main.py                   # 主程序入口
│   ├── parser/
│   │   ├── __init__.py
│   │   ├── base.py               # 解析器基类
│   │   ├── pdf_parser.py         # PDF 解析
│   │   ├── word_parser.py        # Word 解析
│   │   └── clause_extractor.py   # 条款提取
│   ├── analyzer/
│   │   ├── __init__.py
│   │   ├── risk_detector.py      # 风险识别
│   │   ├── clause_analyzer.py    # 条款分析
│   │   ├── compliance_checker.py # 合规检查
│   │   └── legal_researcher.py   # 法律研究
│   ├── generator/
│   │   ├── __init__.py
│   │   ├── report_generator.py   # 报告生成
│   │   ├── template_filler.py    # 模板填充
│   │   └── pdf_exporter.py       # PDF 导出
│   ├── api/
│   │   ├── __init__.py
│   │   ├── routes.py             # API 路由
│   │   └── schemas.py            # 数据模型
│   └── utils/
│       ├── __init__.py
│       ├── logger.py             # 日志工具
│       ├── cache.py              # 缓存工具
│       └── helpers.py            # 辅助函数
├── tests/
│   ├── __init__.py
│   ├── test_parser.py
│   ├── test_analyzer.py
│   ├── test_generator.py
│   └── fixtures/
│       ├── sample_contract.pdf
│       └── sample_contract.docx
├── scripts/
│   ├── setup.sh                  # 安装脚本
│   ├── run_api.sh                # 启动 API
│   └── batch_review.sh           # 批量审查
└── docs/
    ├── API.md                    # API 文档
    ├── USAGE.md                  # 使用指南
    ├── EXAMPLES.md               # 示例
    └── DEPLOYMENT.md             # 部署文档
```

---

## 🛠️ 核心代码

### **1. 合同解析器**

```python
# src/parser/pdf_parser.py

import PyPDF2
from typing import List, Dict, Optional
from .base import BaseParser

class PDFParser(BaseParser):
    """PDF 合同解析器"""

    def extract_text(self, pdf_path: str) -> str:
        """提取 PDF 全文"""
        text = ""
        try:
            with open(pdf_path, 'rb') as file:
                reader = PyPDF2.PdfReader(file)
                for page_num, page in enumerate(reader.pages):
                    page_text = page.extract_text()
                    text += f"\n--- Page {page_num + 1} ---\n"
                    text += page_text
        except Exception as e:
            self.logger.error(f"PDF 解析失败: {e}")
            raise

        return text

    def extract_metadata(self, pdf_path: str) -> Dict:
        """提取 PDF 元数据"""
        with open(pdf_path, 'rb') as file:
            reader = PyPDF2.PdfReader(file)
            metadata = reader.metadata

            return {
                'title': metadata.get('/Title', ''),
                'author': metadata.get('/Author', ''),
                'creator': metadata.get('/Creator', ''),
                'producer': metadata.get('/Producer', ''),
                'creation_date': metadata.get('/CreationDate', ''),
                'pages': len(reader.pages)
            }

# src/parser/clause_extractor.py

import json
from typing import List, Dict

class ClauseExtractor:
    """条款提取器"""

    def extract_clauses(self, text: str) -> List[Dict]:
        """从合同文本中提取条款"""
        prompt = f"""
        从以下合同文本中提取所有条款，识别：
        1. 条款编号
        2. 条款标题
        3. 条款内容
        4. 条款类型（权利/义务/违约责任/保密/知识产权等）
        5. 涉及方（甲方/乙方/双方）

        合同文本：
        {text}

        输出 JSON 格式：
        {{
            "clauses": [
                {{
                    "number": "第一条",
                    "title": "服务内容",
                    "content": "...",
                    "type": "义务",
                    "parties": ["乙方"]
                }}
            ]
        }}
        """

        result = self.client.generate(
            prompt=prompt,
            model="claude-3-opus-20240229",
            max_tokens=4000
        )

        return json.loads(result.content)['clauses']
```

### **2. 风险识别器**

```python
# src/analyzer/risk_detector.py

from typing import List, Dict
import yaml

class RiskDetector:
    """合同风险识别器"""

    def __init__(self, config_path: str = "config/risk-patterns.yaml"):
        with open(config_path, 'r', encoding='utf-8') as f:
            self.risk_patterns = yaml.safe_load(f)

    def detect_risks(
        self,
        clauses: List[Dict],
        jurisdiction: str = "中国大陆",
        industry: Optional[str] = None
    ) -> List[Dict]:
        """识别风险条款"""
        risks = []

        for clause in clauses:
            # 检查每个风险模式
            for pattern in self.risk_patterns['patterns']:
                if self._match_pattern(clause, pattern):
                    risk = self._analyze_risk(
                        clause=clause,
                        pattern=pattern,
                        jurisdiction=jurisdiction,
                        industry=industry
                    )
                    risks.append(risk)

        # 按风险等级排序
        risks.sort(key=lambda x: x['severity'], reverse=True)

        return risks

    def _analyze_risk(
        self,
        clause: Dict,
        pattern: Dict,
        jurisdiction: str,
        industry: Optional[str]
    ) -> Dict:
        """深度分析风险"""
        prompt = f"""
        分析以下合同条款的风险：

        条款内容：{clause['content']}
        条款类型：{clause['type']}
        风险模式：{pattern['name']}

        管辖地：{jurisdiction}
        行业：{industry or '通用'}

        识别：
        1. 风险类型
        2. 风险等级（高/中/低）
        3. 具体问题描述
        4. 可能后果
        5. 优化建议
        6. 相关法规
        7. 修改示例

        输出 JSON 格式。
        """

        result = self.client.analyze(
            text=clause['content'],
            type="risk",
            context={
                'pattern': pattern,
                'jurisdiction': jurisdiction,
                'industry': industry
            }
        )

        return json.loads(result.content)
```

### **3. 合规检查器**

```python
# src/analyzer/compliance_checker.py

from typing import List, Dict
import yaml

class ComplianceChecker:
    """合规检查器"""

    def __init__(self, config_path: str = "config/compliance-rules.yaml"):
        with open(config_path, 'r', encoding='utf-8') as f:
            self.compliance_rules = yaml.safe_load(f)

    def check_compliance(
        self,
        clauses: List[Dict],
        jurisdiction: str = "中国大陆",
        contract_type: str = "general"
    ) -> List[Dict]:
        """检查合规性"""
        issues = []

        # 获取适用的法规
        applicable_rules = self._get_applicable_rules(
            jurisdiction=jurisdiction,
            contract_type=contract_type
        )

        for clause in clauses:
            for rule in applicable_rules:
                if self._violates_rule(clause, rule):
                    issue = self._analyze_violation(
                        clause=clause,
                        rule=rule
                    )
                    issues.append(issue)

        return issues

    def _analyze_violation(
        self,
        clause: Dict,
        rule: Dict
    ) -> Dict:
        """分析违规情况"""
        prompt = f"""
        分析以下条款是否违反法规：

        条款：{clause['content']}
        法规：{rule['name']}
        法规内容：{rule['content']}

        输出：
        1. 是否违规
        2. 违规程度
        3. 违规原因
        4. 修改建议
        5. 法律后果
        """

        result = self.client.analyze(
            text=clause['content'],
            type="compliance",
            context={'rule': rule}
        )

        return json.loads(result.content)
```

### **4. 报告生成器**

```python
# src/generator/report_generator.py

from typing import List, Dict
from datetime import datetime

class ReportGenerator:
    """审查报告生成器"""

    def generate_review_report(
        self,
        contract_info: Dict,
        clauses: List[Dict],
        risks: List[Dict],
        compliance_issues: List[Dict],
        output_format: str = "markdown"
    ) -> str:
        """生成审查报告"""
        prompt = f"""
        基于以下合同审查结果，生成专业审查报告：

        合同信息：
        {json.dumps(contract_info, ensure_ascii=False, indent=2)}

        条款列表：
        {json.dumps(clauses, ensure_ascii=False, indent=2)}

        风险识别：
        {json.dumps(risks, ensure_ascii=False, indent=2)}

        合规问题：
        {json.dumps(compliance_issues, ensure_ascii=False, indent=2)}

        报告要求：
        1. 执行摘要（总体风险评估）
        2. 高风险条款详解
        3. 中低风险条款列表
        4. 合规问题总结
        5. 优化建议（按优先级）
        6. 修改示例
        7. 附录（法规索引）

        输出格式：{output_format}
        """

        result = self.client.generate(
            prompt=prompt,
            model="claude-3-opus-20240229",
            max_tokens=8000
        )

        return result.content

    def export_to_pdf(
        self,
        report_content: str,
        output_path: str
    ) -> str:
        """导出为 PDF"""
        # 使用 markdown 转 PDF 库
        import markdown
        from weasyprint import HTML

        # Markdown → HTML → PDF
        html_content = markdown.markdown(report_content)
        HTML(string=html_content).write_pdf(output_path)

        return output_path
```

---

## 📊 性能指标

### **效率对比**

| 任务 | 人工 | Claude Code | 提升 |
|------|------|------------|------|
| **合同解析** | 30分钟 | 2分钟 | **15x** |
| **风险识别** | 1小时 | 5分钟 | **12x** |
| **合规检查** | 2小时 | 10分钟 | **12x** |
| **报告生成** | 30分钟 | 3分钟 | **10x** |
| **总体** | **4小时** | **20分钟** | **12x** |

### **质量指标**

| 指标 | 基准 | 目标 |
|------|------|------|
| **风险识别率** | 75% | 95% |
| **合规准确率** | 80% | 93% |
| **误报率** | 15% | <5% |
| **漏报率** | 10% | <3% |

### **成本对比**

| 项目 | 人工 | Claude Code | 节省 |
|------|------|------------|------|
| **单份合同** | ¥500 | ¥50 | **90%** |
| **月度（50份）** | ¥25,000 | ¥2,500 | **90%** |
| **年度（600份）** | ¥300,000 | ¥30,000 | **90%** |

---

## 🚀 快速开始

### **1. 安装**

```bash
# 克隆项目
git clone https://github.com/srxly888-creator/legal-review-assistant.git
cd legal-review-assistant

# 创建虚拟环境
python -m venv venv
source venv/bin/activate

# 安装依赖
pip install -r requirements.txt

# 配置环境变量
cp .env.example .env
# 编辑 .env，填入 ANTHROPIC_API_KEY
```

### **2. 运行**

```bash
# 审查单个合同
python -m src.main review --file contract.pdf

# 批量审查
python -m src.main batch --directory ./contracts/

# 启动 API 服务
uvicorn src.api.routes:app --reload
```

### **3. API 使用**

```python
import requests

# 上传合同审查
response = requests.post(
    "http://localhost:8000/api/review",
    files={"file": open("contract.pdf", "rb")},
    data={
        "jurisdiction": "中国大陆",
        "industry": "互联网",
        "contract_type": "服务合同"
    }
)

review_result = response.json()
print(review_result['risks'])
```

---

## 📚 API 文档

### **POST /api/review**

审查合同

**Request**:
```json
{
  "file": "contract.pdf",
  "jurisdiction": "中国大陆",
  "industry": "互联网",
  "contract_type": "服务合同",
  "output_format": "markdown"
}
```

**Response**:
```json
{
  "contract_id": "abc123",
  "review_date": "2026-03-22",
  "summary": {
    "total_clauses": 25,
    "high_risks": 3,
    "medium_risks": 5,
    "low_risks": 2,
    "compliance_issues": 4
  },
  "risks": [...],
  "compliance_issues": [...],
  "recommendations": [...],
  "report_url": "/api/report/abc123"
}
```

---

## 🎓 学习要点

### **技术要点**
1. ✅ PDF/Word 解析技术
2. ✅ 条款自动提取
3. ✅ 风险识别算法
4. ✅ 合规检查逻辑
5. ✅ 报告自动化生成

### **业务要点**
1. ✅ 合同法基础知识
2. ✅ 常见风险模式
3. ✅ 法规库管理
4. ✅ 合规检查标准
5. ✅ 报告撰写规范

---

## 🔗 相关资源

- [法务自动化场景](../04-应用场景/法务自动化.md)
- [快速开始](../01-快速开始.md)
- [最佳实践](../03-最佳实践.md)
- [项目代码](../../projects/legal-review-assistant/)

---

**难度**: ⭐⭐⭐⭐
**预计时间**: 5-7 天
**状态**: 📝 规划完成
**下一步**: 开始代码开发

# 实践项目 3: 运营数据分析助手

> **难度**: ⭐⭐⭐
> **预计时间**: 4-6 天
> **技术栈**: Python + FastAPI + Claude Code CLI + 数据可视化

---

## 🎯 项目目标

构建一个智能运营数据分析系统，实现：
1. **数据采集**: 多数据源自动采集
2. **数据分析**: 统计分析 + 趋势预测
3. **可视化**: 自动图表生成
4. **报告生成**: 自动化运营报告

**预期效果**: 分析时间 **4小时 → 20分钟**（**12x**）

---

## 📋 功能清单

### **核心功能（MVP）**
- [x] 数据库数据采集
- [x] Excel/CSV 数据导入
- [x] 基础统计分析
- [x] 图表生成
- [x] 报告生成

### **进阶功能**
- [ ] 多数据源整合
- [ ] 趋势预测
- [ ] 异常检测
- [ ] 实时仪表盘

### **高级功能**
- [ ] 智能洞察
- [ ] 自动告警
- [ ] 自定义指标
- [ ] API 接口

---

## 🏗️ 项目结构

```
operation-analytics/
├── README.md
├── requirements.txt
├── .env.example
├── config/
│   ├── data-sources.yaml         # 数据源配置
│   ├── metrics.yaml              # 指标定义
│   ├── alerts.yaml               # 告警规则
│   └── visualization.yaml        # 可视化配置
├── src/
│   ├── __init__.py
│   ├── main.py                   # 主程序入口
│   ├── collector/
│   │   ├── __init__.py
│   │   ├── base.py               # 采集器基类
│   │   ├── database.py           # 数据库采集
│   │   ├── api_collector.py      # API 采集
│   │   ├── file_collector.py     # 文件采集
│   │   └── scheduler.py          # 定时任务
│   ├── analyzer/
│   │   ├── __init__.py
│   │   ├── statistics.py         # 统计分析
│   │   ├── prediction.py         # 趋势预测
│   │   ├── anomaly.py            # 异常检测
│   │   └── correlation.py        # 相关性分析
│   ├── visualizer/
│   │   ├── __init__.py
│   │   ├── charts.py             # 图表生成
│   │   ├── dashboard.py          # 仪表盘
│   │   └── exporter.py           # 导出器
│   ├── reporter/
│   │   ├── __init__.py
│   │   ├── generator.py          # 报告生成
│   │   ├── templates.py          # 模板管理
│   │   └── scheduler.py          # 定时报告
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
│   ├── test_collector.py
│   ├── test_analyzer.py
│   ├── test_visualizer.py
│   └── fixtures/
│       ├── sample_sales.csv
│       └── sample_traffic.json
├── scripts/
│   ├── setup.sh                  # 安装脚本
│   ├── run_api.sh                # 启动 API
│   └── schedule_reports.sh       # 定时报告
└── docs/
    ├── API.md                    # API 文档
    ├── USAGE.md                  # 使用指南
    ├── METRICS.md                # 指标说明
    └── DEPLOYMENT.md             # 部署文档
```

---

## 🛠️ 核心代码

### **1. 数据采集器**

```python
# src/collector/database.py

import pandas as pd
from sqlalchemy import create_engine
from typing import Dict, List, Optional
from datetime import datetime, timedelta

class DatabaseCollector:
    """数据库数据采集器"""

    def __init__(self, connection_string: str):
        self.engine = create_engine(connection_string)

    def collect_sales_data(
        self,
        start_date: Optional[str] = None,
        end_date: Optional[str] = None,
        filters: Optional[Dict] = None
    ) -> pd.DataFrame:
        """采集销售数据"""
        # 默认时间范围
        if not start_date:
            start_date = (datetime.now() - timedelta(days=30)).strftime('%Y-%m-%d')
        if not end_date:
            end_date = datetime.now().strftime('%Y-%m-%d')

        # 构建查询
        query = f"""
        SELECT
            date,
            product_id,
            product_name,
            category,
            revenue,
            quantity,
            customer_id,
            region,
            channel
        FROM sales
        WHERE date BETWEEN '{start_date}' AND '{end_date}'
        """

        # 添加过滤条件
        if filters:
            for key, value in filters.items():
                query += f" AND {key} = '{value}'"

        # 执行查询
        df = pd.read_sql(query, self.engine)

        # 数据清洗
        df['date'] = pd.to_datetime(df['date'])
        df['revenue'] = pd.to_numeric(df['revenue'], errors='coerce')
        df['quantity'] = pd.to_numeric(df['quantity'], errors='coerce')

        return df

    def collect_traffic_data(
        self,
        start_date: str,
        end_date: str
    ) -> pd.DataFrame:
        """采集流量数据"""
        query = f"""
        SELECT
            date,
            page_url,
            page_views,
            unique_visitors,
            avg_session_duration,
            bounce_rate,
            traffic_source
        FROM traffic
        WHERE date BETWEEN '{start_date}' AND '{end_date}'
        """

        df = pd.read_sql(query, self.engine)
        return df

# src/collector/api_collector.py

import requests
import pandas as pd
from typing import Dict, List

class APICollector:
    """API 数据采集器"""

    def __init__(self, api_config: Dict):
        self.base_url = api_config['base_url']
        self.headers = api_config.get('headers', {})

    def collect_google_analytics(
        self,
        view_id: str,
        metrics: List[str],
        dimensions: List[str],
        date_range: Dict
    ) -> pd.DataFrame:
        """采集 Google Analytics 数据"""
        # 构建请求
        endpoint = f"{self.base_url}/v4/reports:batchGet"
        payload = {
            "reportRequests": [{
                "viewId": view_id,
                "dateRanges": [{
                    "startDate": date_range['start_date'],
                    "endDate": date_range['end_date']
                }],
                "metrics": [{"expression": m} for m in metrics],
                "dimensions": [{"name": d} for d in dimensions]
            }]
        }

        # 发送请求
        response = requests.post(
            endpoint,
            headers=self.headers,
            json=payload
        )

        # 解析响应
        data = self._parse_ga_response(response.json())
        df = pd.DataFrame(data)

        return df

    def _parse_ga_response(self, response: Dict) -> List[Dict]:
        """解析 GA 响应"""
        rows = []
        report = response['reports'][0]

        for row in report['data']['rows']:
            row_data = {}
            for i, dimension in enumerate(report['columnHeader']['dimensions']):
                row_data[dimension] = row['dimensions'][i]
            for i, metric in enumerate(report['columnHeader']['metricHeader']['metricHeaderEntries']):
                row_data[metric['name']] = row['metrics'][0]['values'][i]
            rows.append(row_data)

        return rows
```

### **2. 数据分析器**

```python
# src/analyzer/statistics.py

import pandas as pd
import numpy as np
from typing import Dict, List, Tuple
from scipy import stats

class StatisticsAnalyzer:
    """统计分析器"""

    def analyze_sales_trend(
        self,
        df: pd.DataFrame,
        granularity: str = 'daily'
    ) -> Dict:
        """分析销售趋势"""
        # 按时间聚合
        df['date'] = pd.to_datetime(df['date'])
        if granularity == 'daily':
            grouped = df.groupby(df['date'].dt.date)
        elif granularity == 'weekly':
            grouped = df.groupby(df['date'].dt.to_period('W'))
        elif granularity == 'monthly':
            grouped = df.groupby(df['date'].dt.to_period('M'))

        # 计算指标
        metrics = {
            'total_revenue': grouped['revenue'].sum(),
            'avg_revenue': grouped['revenue'].mean(),
            'total_quantity': grouped['quantity'].sum(),
            'avg_order_value': grouped['revenue'].sum() / grouped['quantity'].sum(),
            'order_count': grouped.size()
        }

        # 计算增长率
        revenue_series = metrics['total_revenue']
        yoy_growth = self._calculate_yoy(revenue_series)
        mom_growth = self._calculate_mom(revenue_series)

        # 趋势分析
        trend = self._detect_trend(revenue_series)

        return {
            'metrics': metrics,
            'yoy_growth': yoy_growth,
            'mom_growth': mom_growth,
            'trend': trend,
            'summary': self._generate_summary(metrics, yoy_growth, mom_growth)
        }

    def _calculate_yoy(self, series: pd.Series) -> float:
        """计算同比增长率"""
        if len(series) < 2:
            return 0.0

        current = series.iloc[-1]
        previous = series.iloc[0]

        if previous == 0:
            return 0.0

        return (current - previous) / previous * 100

    def _calculate_mom(self, series: pd.Series) -> float:
        """计算环比增长率"""
        if len(series) < 2:
            return 0.0

        current = series.iloc[-1]
        previous = series.iloc[-2]

        if previous == 0:
            return 0.0

        return (current - previous) / previous * 100

    def _detect_trend(self, series: pd.Series) -> str:
        """检测趋势方向"""
        # 使用线性回归
        X = np.arange(len(series)).reshape(-1, 1)
        y = series.values

        slope, _, r_value, _, _ = stats.linregress(X.flatten(), y)

        if slope > 0 and r_value > 0.7:
            return 'upward'
        elif slope < 0 and r_value > 0.7:
            return 'downward'
        else:
            return 'stable'

# src/analyzer/prediction.py

import pandas as pd
import numpy as np
from typing import Dict, Tuple

class PredictionAnalyzer:
    """预测分析器"""

    def predict_sales(
        self,
        historical_data: pd.DataFrame,
        periods: int = 3,
        confidence: float = 0.95
    ) -> Dict:
        """预测未来销售"""
        # 准备数据
        df = historical_data.copy()
        df['date'] = pd.to_datetime(df['date'])
        df = df.sort_values('date')

        # 使用 Claude Code 进行预测
        prompt = f"""
        基于以下历史销售数据，预测未来 {periods} 个月的销售趋势：

        历史数据（最近12个月）：
        {df.tail(12).to_string()}

        要求：
        1. 预测值（点估计）
        2. 置信区间（{confidence*100}%）
        3. 预测假设
        4. 风险因素
        5. 关键驱动因素

        输出 JSON 格式：
        {{
            "predictions": [
                {{
                    "month": "2026-04",
                    "predicted_revenue": 4500000,
                    "lower_bound": 4200000,
                    "upper_bound": 4800000,
                    "confidence": 0.95
                }}
            ],
            "assumptions": ["..."],
            "risks": ["..."],
            "drivers": ["..."]
        }}
        """

        result = self.client.predict(
            data=df,
            periods=periods,
            confidence=confidence
        )

        return json.loads(result.content)
```

### **3. 可视化引擎**

```python
# src/visualizer/charts.py

import plotly.graph_objects as go
import plotly.express as px
import pandas as pd
from typing import Dict, List, Optional

class ChartGenerator:
    """图表生成器"""

    def create_line_chart(
        self,
        df: pd.DataFrame,
        x_col: str,
        y_col: str,
        title: str,
        **kwargs
    ) -> go.Figure:
        """创建折线图"""
        fig = go.Figure()

        fig.add_trace(go.Scatter(
            x=df[x_col],
            y=df[y_col],
            mode='lines+markers',
            name=kwargs.get('name', y_col),
            line=dict(color=kwargs.get('color', '#1f77b4'))
        ))

        fig.update_layout(
            title=title,
            xaxis_title=kwargs.get('xaxis_title', x_col),
            yaxis_title=kwargs.get('yaxis_title', y_col),
            template='plotly_white'
        )

        return fig

    def create_bar_chart(
        self,
        df: pd.DataFrame,
        x_col: str,
        y_col: str,
        title: str,
        **kwargs
    ) -> go.Figure:
        """创建柱状图"""
        fig = px.bar(
            df,
            x=x_col,
            y=y_col,
            title=title,
            color=kwargs.get('color_col')
        )

        fig.update_layout(
            template='plotly_white',
            showlegend=kwargs.get('showlegend', True)
        )

        return fig

    def create_pie_chart(
        self,
        df: pd.DataFrame,
        values_col: str,
        names_col: str,
        title: str
    ) -> go.Figure:
        """创建饼图"""
        fig = px.pie(
            df,
            values=values_col,
            names=names_col,
            title=title
        )

        fig.update_layout(template='plotly_white')

        return fig

    def export_to_html(
        self,
        fig: go.Figure,
        output_path: str
    ) -> str:
        """导出为 HTML"""
        fig.write_html(output_path)
        return output_path

    def export_to_png(
        self,
        fig: go.Figure,
        output_path: str
    ) -> str:
        """导出为 PNG"""
        fig.write_image(output_path)
        return output_path
```

### **4. 报告生成器**

```python
# src/reporter/generator.py

import pandas as pd
from typing import Dict, List
from datetime import datetime

class ReportGenerator:
    """报告生成器"""

    def generate_weekly_report(
        self,
        sales_data: pd.DataFrame,
        traffic_data: pd.DataFrame,
        output_format: str = "markdown"
    ) -> str:
        """生成周报"""
        # 分析数据
        sales_analysis = self.analyzer.analyze_sales_trend(sales_data)
        traffic_analysis = self.analyzer.analyze_traffic_trend(traffic_data)

        # 生成报告
        prompt = f"""
        基于以下运营数据，生成专业的周报：

        销售数据分析：
        {json.dumps(sales_analysis, ensure_ascii=False, indent=2)}

        流量数据分析：
        {json.dumps(traffic_analysis, ensure_ascii=False, indent=2)}

        报告要求：
        1. 执行摘要（关键指标）
        2. 销售表现（同比/环比）
        3. 流量分析（用户行为）
        4. 关键发现（洞察）
        5. 风险提示
        6. 优化建议

        输出格式：{output_format}
        """

        result = self.client.generate(
            prompt=prompt,
            model="claude-3-opus-20240229",
            max_tokens=4000
        )

        return result.content

    def generate_monthly_report(
        self,
        data_sources: Dict[str, pd.DataFrame],
        include_predictions: bool = True
    ) -> str:
        """生成月报"""
        # 收集所有分析
        analyses = {}

        for source_name, df in data_sources.items():
            if source_name == 'sales':
                analyses['sales'] = self.analyzer.analyze_sales_trend(df)
                if include_predictions:
                    analyses['predictions'] = self.analyzer.predict_sales(df)
            elif source_name == 'traffic':
                analyses['traffic'] = self.analyzer.analyze_traffic_trend(df)
            elif source_name == 'conversion':
                analyses['conversion'] = self.analyzer.analyze_conversion(df)

        # 生成报告
        prompt = f"""
        基于以下运营数据，生成专业的月度报告：

        分析结果：
        {json.dumps(analyses, ensure_ascii=False, indent=2)}

        报告要求：
        1. 执行摘要
        2. 销售表现
        3. 用户行为
        4. 转化漏斗
        5. 趋势预测
        6. 关键洞察
        7. 行动计划

        输出格式：markdown
        """

        result = self.client.generate(prompt=prompt)
        return result.content
```

---

## 📊 性能指标

### **效率对比**

| 任务 | 手工 | Claude Code | 提升 |
|------|------|------------|------|
| **数据采集** | 1小时 | 5分钟 | **12x** |
| **数据分析** | 3小时 | 15分钟 | **12x** |
| **图表生成** | 1小时 | 5分钟 | **12x** |
| **报告撰写** | 2小时 | 10分钟 | **12x** |
| **总体** | **7小时** | **35分钟** | **12x** |

### **质量指标**

| 指标 | 基准 | 目标 |
|------|------|------|
| **分析深度** | 60% | 90% |
| **预测准确率** | 65% | 85% |
| **洞察质量** | 70% | 95% |
| **报告规范性** | 75% | 98% |

### **成本对比**

| 项目 | 手工 | Claude Code | 节省 |
|------|------|------------|------|
| **单次分析** | ¥300 | ¥30 | **90%** |
| **月度（10次）** | ¥3,000 | ¥300 | **90%** |
| **年度（120次）** | ¥36,000 | ¥3,600 | **90%** |

---

## 🚀 快速开始

### **1. 安装**

```bash
# 克隆项目
git clone https://github.com/srxly888-creator/operation-analytics.git
cd operation-analytics

# 创建虚拟环境
python -m venv venv
source venv/bin/activate

# 安装依赖
pip install -r requirements.txt

# 配置数据源
cp .env.example .env
# 编辑 .env，配置数据库连接
```

### **2. 运行**

```bash
# 分析销售数据
python -m src.main analyze --type sales --file sales.csv

# 生成周报
python -m src.main report --type weekly --output report.md

# 启动 API 服务
uvicorn src.api.routes:app --reload
```

### **3. API 使用**

```python
import requests

# 分析数据
response = requests.post(
    "http://localhost:8000/api/analyze",
    json={
        "data_type": "sales",
        "file_path": "sales.csv",
        "analysis_type": "trend",
        "granularity": "daily"
    }
)

analysis_result = response.json()
print(analysis_result['summary'])
```

---

## 📚 API 文档

### **POST /api/analyze**

分析数据

**Request**:
```json
{
  "data_type": "sales",
  "file_path": "sales.csv",
  "analysis_type": "trend",
  "granularity": "daily",
  "start_date": "2026-01-01",
  "end_date": "2026-03-31"
}
```

**Response**:
```json
{
  "analysis_id": "xyz789",
  "analysis_date": "2026-03-22",
  "summary": {
    "total_revenue": 12345678,
    "yoy_growth": 23.5,
    "mom_growth": 8.3,
    "trend": "upward"
  },
  "details": {...},
  "visualizations": [
    "/api/chart/trend_123.html",
    "/api/chart/distribution_456.png"
  ],
  "insights": [...]
}
```

---

## 🎓 学习要点

### **技术要点**
1. ✅ 数据采集（多数据源）
2. ✅ 统计分析（增长率、趋势）
3. ✅ 预测模型（时间序列）
4. ✅ 数据可视化（Plotly）
5. ✅ 报告自动化

### **业务要点**
1. ✅ 运营指标定义
2. ✅ 数据分析方法
3. ✅ 趋势解读技巧
4. ✅ 洞察提取能力
5. ✅ 报告撰写规范

---

## 🔗 相关资源

- [运营优化场景](../04-应用场景/运营优化.md)
- [快速开始](../01-快速开始.md)
- [最佳实践](../03-最佳实践.md)
- [项目代码](../../projects/operation-analytics/)

---

**难度**: ⭐⭐⭐
**预计时间**: 4-6 天
**状态**: 📝 规划完成
**下一步**: 开始代码开发

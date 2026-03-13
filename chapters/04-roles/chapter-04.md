# 第4章 不同角色详解

## 4.1 项目经理（PM）

### 4.1.1 角色定位与核心价值

项目经理是项目成功的第一责任人，是连接客户、团队和管理层的枢纽。

**核心价值**：
- **统筹全局**：协调项目所有资源和活动
- **把控进度**：确保项目按时交付
- **管理风险**：识别和化解项目风险
- **维护客户**：管理客户期望和关系

### 4.1.2 职责详解

**项目统筹**：
- 制定项目整体计划和里程碑
- 协调项目资源（人力、设备、数据）
- 监控项目进度，识别偏差
- 组织项目例会，跟踪任务

**客户管理**：
- 作为客户主要联系人
- 组织项目启动会、汇报会
- 理解和管理客户期望
- 处理客户投诉和争议

**质量控制**：
- 确保交付物符合质量标准
- 组织内部质量评审
- 监督技术方案执行
- 处理技术问题升级

### 4.1.3 能力要求

**硬技能**：
- 项目管理方法论（PMP/Prince2）
- 基础技术理解（能听懂技术讨论）
- 数据分析（能看懂项目数据）
- 办公软件（Excel、Project等）

**软技能**：
- 沟通协调（⭐⭐⭐⭐⭐）
- 谈判影响（⭐⭐⭐⭐⭐）
- 领导力（⭐⭐⭐⭐）
- 抗压能力（⭐⭐⭐⭐⭐）

### 4.1.4 AI赋能PM

**AI应用场景**：

1. **智能计划生成**
2. **风险预测**
3. **会议纪要自动生成**
4. **进度报告自动生成**

**Python代码示例：AI智能周报生成器**

```python
import openai
import json
from datetime import datetime, timedelta

class AIReportGenerator:
    """AI智能报告生成器"""
    
    def __init__(self, api_key):
        openai.api_key = api_key
    
    def generate_weekly_report(self, project_data):
        """生成项目周报"""
        
        prompt = f"""
        请根据以下项目数据生成一份专业的项目周报：
        
        项目名称：{project_data['name']}
        报告周期：{project_data['week_start']} 至 {project_data['week_end']}
        
        本周完成任务：
        {json.dumps(project_data['completed_tasks'], ensure_ascii=False, indent=2)}
        
        进行中任务：
        {json.dumps(project_data['ongoing_tasks'], ensure_ascii=False, indent=2)}
        
        遇到的问题：
        {json.dumps(project_data['issues'], ensure_ascii=False, indent=2)}
        
        下周计划：
        {json.dumps(project_data['next_week_plan'], ensure_ascii=False, indent=2)}
        
        请生成一份包含以下部分的周报：
        1. 项目概况（进度、状态）
        2. 本周工作总结
        3. 问题与风险
        4. 下周工作计划
        5. 需要协调的事项
        
        要求：
        - 使用专业、简洁的语言
        - 突出关键信息
        - 提出明确的行动建议
        """
        
        response = openai.ChatCompletion.create(
            model="gpt-4",
            messages=[
                {"role": "system", "content": "你是一位专业的项目管理专家，擅长撰写项目报告。"},
                {"role": "user", "content": prompt}
            ],
            temperature=0.7,
            max_tokens=2000
        )
        
        return response.choices[0].message.content
    
    def analyze_project_risks(self, project_metrics):
        """AI分析项目风险"""
        
        prompt = f"""
        请分析以下项目指标，识别潜在风险：
        
        {json.dumps(project_metrics, ensure_ascii=False, indent=2)}
        
        请分析：
        1. 进度风险（是否可能延期）
        2. 质量风险（返工率、缺陷率趋势）
        3. 资源风险（工作量饱和度）
        4. 客户风险（需求变更、满意度）
        
        对于每个风险，请给出：
        - 风险等级（高/中/低）
        - 风险描述
        - 建议的应对措施
        """
        
        response = openai.ChatCompletion.create(
            model="gpt-4",
            messages=[
                {"role": "system", "content": "你是一位资深的项目风险管理专家。"},
                {"role": "user", "content": prompt}
            ],
            temperature=0.5
        )
        
        return response.choices[0].message.content

# 使用示例
generator = AIReportGenerator(api_key="your-api-key")

project_data = {
    'name': '某市排水规划项目',
    'week_start': '2024-03-01',
    'week_end': '2024-03-07',
    'completed_tasks': [
        '完成中心区数据收集',
        '建立基础模型框架',
        '完成现状模拟'
    ],
    'ongoing_tasks': [
        {'name': '模型校准', 'progress': 60},
        {'name': '方案设计', 'progress': 30}
    ],
    'issues': [
        '部分监测数据缺失，需要协调补充',
        '模型在暴雨场景下出现不稳定'
    ],
    'next_week_plan': [
        '完成模型校准',
        '开始方案模拟',
        '提交中期报告'
    ]
}

report = generator.generate_weekly_report(project_data)
print(report)
```

## 4.2 水力模型架构师

### 4.2.1 为什么需要架构师

**传统团队的痛点**：
- 技术决策无人把关，质量波动大
- 复杂项目搞不定，技术债务累积
- 新人成长慢，依赖老员工
- 技术创新无力

**架构师的价值**：
- 技术方向的把控者
- 质量的最后守门人
- 复杂问题的解决者
- 团队技术的引领者

### 4.2.2 架构师的核心职责

**技术架构设计**：
- 制定技术方案和技术路线
- 确定建模策略和方法论
- 选择技术工具和软件
- 评估技术风险

**质量技术把关**：
- 审核技术方案
- 关键技术评审
- 交付物质量把关
- 技术签字负责

**技术指导**：
- 解决复杂技术难题
- 培养团队成员
- 推动技术创新

### 4.2.3 架构师对全周期的重要性

```
项目启动 → 架构师参与需求分析，制定技术路线
    ↓
方案设计 → 架构师主导技术方案设计
    ↓
模型构建 → 架构师指导关键技术，解决难题
    ↓
验证校准 → 架构师审核验证方案，把关结果
    ↓
成果交付 → 架构师最终质量审查，技术签字
    ↓
运维支持 → 架构师处理重大技术问题
```

### 4.2.4 架构师的能力要求

**技术深度**：
- 精通各类水力建模技术
- 深入理解数值方法
- 掌握不确定性分析
- 熟悉前沿技术发展

**技术广度**：
- GIS、编程、AI等相关领域
- 多种软件工具
- 行业标准和规范

**工程经验**：
- 8年以上建模经验
- 主导过多个复杂项目
- 处理过各类技术难题

### 4.2.5 AI赋能架构师

**AI辅助模型审查系统**：

```python
import pandas as pd
import numpy as np

class AIModelReviewer:
    """AI辅助模型审查系统"""
    
    def __init__(self):
        self.check_rules = self._load_check_rules()
    
    def _load_check_rules(self):
        """加载检查规则"""
        return {
            'geometry': [
                {'name': '管径合理性', 'check': self._check_diameter},
                {'name': '坡度合理性', 'check': self._check_slope},
                {'name': '连续性检查', 'check': self._check_continuity}
            ],
            'parameters': [
                {'name': '糙率范围', 'check': self._check_roughness},
                {'name': '参数一致性', 'check': self._check_consistency}
            ],
            'results': [
                {'name': '质量平衡', 'check': self._check_mass_balance},
                {'name': '结果合理性', 'check': self._check_result_plausibility}
            ]
        }
    
    def review_model(self, model_data):
        """审查模型"""
        issues = []
        warnings = []
        
        # 几何检查
        for rule in self.check_rules['geometry']:
            result = rule['check'](model_data)
            if result['severity'] == 'error':
                issues.append({
                    'category': '几何',
                    'rule': rule['name'],
                    'message': result['message'],
                    'suggestion': result.get('suggestion', '')
                })
            elif result['severity'] == 'warning':
                warnings.append({
                    'category': '几何',
                    'rule': rule['name'],
                    'message': result['message']
                })
        
        # 生成审查报告
        report = self._generate_review_report(issues, warnings)
        return report
    
    def _check_diameter(self, model_data):
        """检查管径合理性"""
        pipes = model_data.get('pipes', [])
        invalid_pipes = [p for p in pipes if p['diameter'] <= 0 or p['diameter'] > 5000]
        
        if invalid_pipes:
            return {
                'severity': 'error',
                'message': f'发现{len(invalid_pipes)}根管道的管径异常',
                'suggestion': '检查管径数据，确保单位为mm且在合理范围内'
            }
        return {'severity': 'ok', 'message': '管径检查通过'}
    
    def _check_slope(self, model_data):
        """检查坡度合理性"""
        pipes = model_data.get('pipes', [])
        steep_pipes = [p for p in pipes if abs(p['slope']) > 0.5]
        
        if steep_pipes:
            return {
                'severity': 'warning',
                'message': f'发现{len(steep_pipes)}根管道坡度超过50%',
                'suggestion': '核实这些管道的坡度数据是否正确'
            }
        return {'severity': 'ok', 'message': '坡度检查通过'}
    
    def _check_continuity(self, model_data):
        """检查连续性"""
        # 检查节点连接关系
        nodes = set()
        for pipe in model_data.get('pipes', []):
            nodes.add(pipe['from_node'])
            nodes.add(pipe['to_node'])
        
        # 检查是否有孤立节点
        all_nodes = set(n['id'] for n in model_data.get('nodes', []))
        isolated = all_nodes - nodes
        
        if isolated:
            return {
                'severity': 'error',
                'message': f'发现{len(isolated)}个孤立节点',
                'suggestion': '检查这些节点是否应该连接管道'
            }
        return {'severity': 'ok', 'message': '连续性检查通过'}
    
    def _check_roughness(self, model_data):
        """检查糙率范围"""
        pipes = model_data.get('pipes', [])
        invalid = [p for p in pipes if p['roughness'] < 0.009 or p['roughness'] > 0.03]
        
        if invalid:
            return {
                'severity': 'warning',
                'message': f'发现{len(invalid)}根管道的糙率超出典型范围',
                'suggestion': '核实糙率取值是否合理'
            }
        return {'severity': 'ok', 'message': '糙率检查通过'}
    
    def _check_mass_balance(self, model_data):
        """检查质量平衡"""
        # 简化示例，实际应基于模拟结果
        return {'severity': 'ok', 'message': '质量平衡检查通过'}
    
    def _check_result_plausibility(self, model_data):
        """检查结果合理性"""
        # 简化示例，实际应基于模拟结果
        return {'severity': 'ok', 'message': '结果合理性检查通过'}
    
    def _generate_review_report(self, issues, warnings):
        """生成审查报告"""
        report = {
            'summary': {
                'total_issues': len(issues),
                'total_warnings': len(warnings),
                'status': '通过' if not issues else '不通过'
            },
            'issues': issues,
            'warnings': warnings,
            'recommendations': self._generate_recommendations(issues, warnings)
        }
        return report
    
    def _generate_recommendations(self, issues, warnings):
        """生成改进建议"""
        recommendations = []
        
        if any(i['category'] == '几何' for i in issues):
            recommendations.append('建议进行详细的几何数据检查')
        
        if any(i['category'] == '参数' for i in issues):
            recommendations.append('建议复核模型参数设置')
        
        return recommendations

# 使用示例
reviewer = AIModelReviewer()

# 示例模型数据
model_data = {
    'nodes': [
        {'id': 'N1', 'elevation': 10.0},
        {'id': 'N2', 'elevation': 9.5},
        {'id': 'N3', 'elevation': 9.0}
    ],
    'pipes': [
        {'id': 'P1', 'from_node': 'N1', 'to_node': 'N2', 'diameter': 500, 'slope': 0.005, 'roughness': 0.013},
        {'id': 'P2', 'from_node': 'N2', 'to_node': 'N3', 'diameter': 600, 'slope': 0.008, 'roughness': 0.014}
    ]
}

report = reviewer.review_model(model_data)
print(f"审查结果: {report['summary']['status']}")
print(f"问题数: {report['summary']['total_issues']}")
print(f"警告数: {report['summary']['total_warnings']}")
```

## 4.3 水力模型工程师

### 4.3.1 角色定位

水力模型工程师是模型构建和计算的核心执行者，是将设计转化为可计算模型的关键角色。

**核心价值**：
- 执行技术方案，构建水力模型
- 进行模型验证和校准
- 分析结果，识别问题，提出建议

### 4.3.2 职责详解

**模型构建**：
- 根据技术方案构建水力模型
- 准备和处理输入数据
- 设置模型参数和边界条件
- 运行模型并调试

**模型验证**：
- 执行质量检查
- 进行模型校准
- 分析验证结果
- 编写验证报告

**结果分析**：
- 分析模型计算结果
- 提取关键水力指标
- 制作结果图表
- 识别系统问题

### 4.3.3 分级能力要求

| 等级 | 核心能力 | 典型工作 |
|------|---------|---------|
| **L1** | 学习基础 | 辅助工作，在指导下完成简单任务 |
| **L2** | 独立完成 | 独立完成小型模型（<500节点） |
| **L3** | 解决复杂 | 独立完成中型模型+校准（500-2000节点） |
| **L4** | 指导审核 | 负责大型模型+审核他人（>2000节点） |

### 4.3.4 AI赋能工程师

**AI辅助数据处理脚本生成**：

```python
import openai

class AICodeAssistant:
    """AI代码助手"""
    
    def __init__(self, api_key):
        openai.api_key = api_key
    
    def generate_data_processing_code(self, requirements, data_sample=None):
        """生成数据处理代码"""
        
        prompt = f"""
        请根据以下需求生成Python数据处理代码：
        
        需求描述：
        {requirements}
        """
        
        if data_sample:
            prompt += f"""
        数据样例：
        {data_sample}
        """
        
        prompt += """
        要求：
        1. 使用pandas进行数据处理
        2. 添加详细的中文注释
        3. 包含输入验证和异常处理
        4. 代码要健壮、高效
        5. 返回处理后的DataFrame
        
        请直接给出完整的Python代码。
        """
        
        response = openai.ChatCompletion.create(
            model="gpt-4",
            messages=[
                {"role": "system", "content": "你是一位专业的Python数据工程师。"},
                {"role": "user", "content": prompt}
            ],
            temperature=0.3
        )
        
        return response.choices[0].message.content
    
    def explain_code(self, code):
        """解释代码"""
        prompt = f"""
        请详细解释以下Python代码的功能和工作原理：
        
        ```python
        {code}
        ```
        
        请从以下几个方面解释：
        1. 代码的整体功能
        2. 每个函数的作用
        3. 关键步骤的说明
        4. 使用注意事项
        """
        
        response = openai.ChatCompletion.create(
            model="gpt-4",
            messages=[
                {"role": "system", "content": "你是一位资深的Python编程讲师。"},
                {"role": "user", "content": prompt}
            ]
        )
        
        return response.choices[0].message.content

# 使用示例
assistant = AICodeAssistant(api_key="your-api-key")

requirements = """
我需要处理一个排水管网数据文件，要求：
1. 读取CSV文件，包含管段ID、起点井号、终点井号、管径(mm)、管长(m)、坡度
2. 检查数据完整性，去除空值
3. 检查管径合理性（0-5000mm）
4. 计算每根管道的过流能力（使用曼宁公式，假设糙率n=0.013）
5. 保存处理后的数据到新的CSV文件
"""

code = assistant.generate_data_processing_code(requirements)
print(code)
```

## 4.4 数据分析师

### 4.4.1 角色定位

数据分析师是数据质量的守护者和数据价值的挖掘者，为水力建模提供数据支撑。

**核心价值**：
- 确保输入数据质量
- 提供数据分析支撑
- 建立数据管理体系

### 4.4.2 职责详解

**数据采集与处理**：
- 收集管网数据、地形数据、监测数据
- 数据清洗和格式转换
- 数据质量控制

**GIS分析**：
- 空间数据分析
- 专题地图制作
- 流域分析

**数据分析**：
- 统计分析
- 趋势分析
- 异常检测

### 4.4.3 能力要求

**技术技能**：
- GIS软件（ArcGIS/QGIS）
- Python数据处理（pandas/geopandas）
- 数据可视化（matplotlib/plotly）
- 数据库（SQL/PostGIS）

### 4.4.4 数据挖掘技术应用

**管网数据异常检测**：

```python
import pandas as pd
import numpy as np
from sklearn.ensemble import IsolationForest
from sklearn.preprocessing import StandardScaler

class PipeDataAnomalyDetector:
    """管网数据异常检测器"""
    
    def __init__(self):
        self.model = None
        self.scaler = StandardScaler()
    
    def prepare_features(self, pipe_data):
        """准备特征"""
        features = pd.DataFrame()
        features['diameter'] = pipe_data['diameter']
        features['length'] = pipe_data['length']
        features['slope'] = pipe_data['slope']
        features['area_ratio'] = pipe_data['diameter'] ** 2 / pipe_data['length']
        return features
    
    def fit(self, pipe_data):
        """训练异常检测模型"""
        features = self.prepare_features(pipe_data)
        
        # 标准化
        features_scaled = self.scaler.fit_transform(features)
        
        # 训练Isolation Forest
        self.model = IsolationForest(
            contamination=0.1,  # 假设10%的异常
            random_state=42,
            n_estimators=100
        )
        self.model.fit(features_scaled)
        
        return self
    
    def detect_anomalies(self, pipe_data):
        """检测异常"""
        features = self.prepare_features(pipe_data)
        features_scaled = self.scaler.transform(features)
        
        # 预测
        predictions = self.model.predict(features_scaled)
        scores = self.model.decision_function(features_scaled)
        
        # 添加结果到数据
        result = pipe_data.copy()
        result['is_anomaly'] = predictions == -1
        result['anomaly_score'] = scores
        
        return result
    
    def get_anomaly_summary(self, result):
        """获取异常摘要"""
        anomalies = result[result['is_anomaly']]
        
        summary = {
            'total_pipes': len(result),
            'anomaly_count': len(anomalies),
            'anomaly_rate': len(anomalies) / len(result),
            'anomaly_pipes': anomalies[['pipe_id', 'diameter', 'length', 'slope', 'anomaly_score']].to_dict('records')
        }
        
        return summary

# 使用示例
detector = PipeDataAnomalyDetector()

# 示例数据
pipe_data = pd.DataFrame({
    'pipe_id': ['P' + str(i) for i in range(1, 101)],
    'diameter': np.random.normal(500, 100, 100),  # 正常管径
    'length': np.random.normal(100, 20, 100),     # 正常管长
    'slope': np.random.normal(0.005, 0.002, 100)  # 正常坡度
})

# 添加一些异常值
pipe_data.loc[10, 'diameter'] = 5000  # 异常大管径
pipe_data.loc[20, 'slope'] = 0.5      # 异常陡坡
pipe_data.loc[30, 'length'] = 1       # 异常短管

# 训练模型
detector.fit(pipe_data)

# 检测异常
result = detector.detect_anomalies(pipe_data)

# 查看结果
summary = detector.get_anomaly_summary(result)
print(f"总管道数: {summary['total_pipes']}")
print(f"异常管道数: {summary['anomaly_count']}")
print(f"异常率: {summary['anomaly_rate']:.2%}")
```

### 4.4.5 数据可视化技术

**管网数据交互式可视化**：

```python
import plotly.express as px
import plotly.graph_objects as go
from plotly.subplots import make_subplots
import pandas as pd
import geopandas as gpd

class PipeDataVisualizer:
    """管网数据可视化器"""
    
    def __init__(self, pipe_data):
        self.pipe_data = pipe_data
    
    def create_diameter_distribution(self):
        """创建管径分布图"""
        fig = px.histogram(
            self.pipe_data,
            x='diameter',
            nbins=30,
            title='管径分布',
            labels={'diameter': '管径 (mm)', 'count': '数量'}
        )
        fig.update_layout(bargap=0.1)
        return fig
    
    def create_slope_distribution(self):
        """创建坡度分布图"""
        fig = px.box(
            self.pipe_data,
            y='slope',
            title='坡度分布',
            labels={'slope': '坡度'}
        )
        return fig
    
    def create_pipe_network_map(self, nodes_gdf, pipes_gdf):
        """创建管网地图"""
        fig = go.Figure()
        
        # 添加管道
        for idx, pipe in pipes_gdf.iterrows():
            coords = pipe.geometry.coords
            x = [coord[0] for coord in coords]
            y = [coord[1] for coord in coords]
            
            fig.add_trace(go.Scatter(
                x=x, y=y,
                mode='lines',
                line=dict(width=pipe['diameter']/100, color='blue'),
                name=f"管道 {pipe['pipe_id']}",
                hovertemplate=f"ID: {pipe['pipe_id']}<br>管径: {pipe['diameter']}mm"
            ))
        
        # 添加节点
        fig.add_trace(go.Scatter(
            x=nodes_gdf.geometry.x,
            y=nodes_gdf.geometry.y,
            mode='markers',
            marker=dict(size=10, color='red'),
            name='检查井',
            text=nodes_gdf['node_id'],
            hovertemplate='ID: %{text}'
        ))
        
        fig.update_layout(
            title='排水管网分布图',
            xaxis_title='X坐标',
            yaxis_title='Y坐标',
            showlegend=True
        )
        
        return fig
    
    def create_dashboard(self):
        """创建数据仪表盘"""
        fig = make_subplots(
            rows=2, cols=2,
            subplot_titles=('管径分布', '坡度分布', '管长分布', '管径-坡度关系'),
            specs=[
                [{"type": "histogram"}, {"type": "box"}],
                [{"type": "histogram"}, {"type": "scatter"}]
            ]
        )
        
        # 管径分布
        fig.add_trace(
            go.Histogram(x=self.pipe_data['diameter'], name='管径'),
            row=1, col=1
        )
        
        # 坡度分布
        fig.add_trace(
            go.Box(y=self.pipe_data['slope'], name='坡度'),
            row=1, col=2
        )
        
        # 管长分布
        fig.add_trace(
            go.Histogram(x=self.pipe_data['length'], name='管长'),
            row=2, col=1
        )
        
        # 管径-坡度散点
        fig.add_trace(
            go.Scatter(
                x=self.pipe_data['diameter'],
                y=self.pipe_data['slope'],
                mode='markers',
                name='管径-坡度'
            ),
            row=2, col=2
        )
        
        fig.update_layout(height=800, title_text="管网数据仪表盘")
        return fig

# 使用示例
pipe_data = pd.DataFrame({
    'pipe_id': ['P' + str(i) for i in range(1, 101)],
    'diameter': np.random.normal(500, 100, 100),
    'length': np.random.normal(100, 20, 100),
    'slope': np.abs(np.random.normal(0.005, 0.002, 100))
})

visualizer = PipeDataVisualizer(pipe_data)

# 创建单个图表
diameter_fig = visualizer.create_diameter_distribution()
diameter_fig.write_html("diameter_distribution.html")

# 创建仪表盘
dashboard = visualizer.create_dashboard()
dashboard.write_html("dashboard.html")
```

## 4.5 AI工程师

### 4.5.1 角色定位

AI工程师是AI技术的引入者和赋能者，为团队提供AI能力支持。

**核心价值**：
- 引入AI技术提升效率
- 开发智能工具
- 推动团队智能化转型

### 4.5.2 职责详解

**AI应用开发**：
- 开发AI辅助工具
- 集成大语言模型
- 构建智能问答系统
- 开发预测模型

**技术探索**：
- 跟踪AI技术发展
- 评估新技术适用性
- 进行技术预研

**能力建设**：
- 培训团队使用AI工具
- 提供技术支持
- 推广AI最佳实践

### 4.5.3 能力要求

**机器学习**：
- 监督/无监督学习
- 深度学习框架（PyTorch/TensorFlow）
- 时序预测、异常检测

**大语言模型**：
- Prompt Engineering
- RAG技术
- Agent开发

**编程能力**：
- Python高级编程
- API开发
- 软件工程实践

### 4.5.4 AI技术应用场景开发

**智能问答系统（RAG）**：

```python
from langchain.embeddings import OpenAIEmbeddings
from langchain.vectorstores import Chroma
from langchain.chains import RetrievalQA
from langchain.llms import OpenAI
from langchain.text_splitter import CharacterTextSplitter
import os

class HydraulicKnowledgeQA:
    """水力建模知识问答系统"""
    
    def __init__(self, api_key):
        os.environ['OPENAI_API_KEY'] = api_key
        self.embeddings = OpenAIEmbeddings()
        self.vectorstore = None
        self.qa_chain = None
    
    def load_documents(self, documents):
        """加载文档到知识库"""
        # 文本切分
        text_splitter = CharacterTextSplitter(
            chunk_size=1000,
            chunk_overlap=200
        )
        texts = text_splitter.split_documents(documents)
        
        # 创建向量存储
        self.vectorstore = Chroma.from_documents(
            texts,
            self.embeddings,
            persist_directory="./chroma_db"
        )
        
        # 创建QA链
        self.qa_chain = RetrievalQA.from_chain_type(
            llm=OpenAI(temperature=0),
            chain_type="stuff",
            retriever=self.vectorstore.as_retriever()
        )
    
    def ask(self, question):
        """提问"""
        if not self.qa_chain:
            return "请先加载知识库文档"
        
        answer = self.qa_chain.run(question)
        return answer
    
    def add_document(self, document):
        """添加新文档"""
        if self.vectorstore:
            self.vectorstore.add_documents([document])
            self.vectorstore.persist()

# 使用示例
qa_system = HydraulicKnowledgeQA(api_key="your-api-key")

# 加载技术文档
from langchain.document_loaders import TextLoader
loader = TextLoader("technical_manual.txt")
documents = loader.load()

qa_system.load_documents(documents)

# 提问
answer = qa_system.ask("什么是曼宁公式？")
print(answer)
```

## 4.6 角色协作与AI赋能

### 4.6.1 五角色的协作模式

**协作流程**：
```
项目启动 → PM制定计划 → 架构师设计方案 → 工程师执行
                ↓              ↓              ↓
           数据分析师提供数据支持
                ↓              ↓              ↓
           AI工程师提供AI工具支持
                ↓              ↓              ↓
           成果整合 → 质量审核 → 交付验收
```

### 4.6.2 AI作为第六个"虚拟角色"

**AI的角色定位**：
- 24/7在线的助手
- 不知疲倦的执行者
- 快速准确的分析师

**人机协作模式**：
- 人类主导，AI辅助
- AI初稿，人类审核
- AI执行，人类监督

### 4.6.3 角色能力提升路径

**纵向发展**：
- L1 → L2 → L3 → L4 → L5

**横向发展**：
- 工程师 → 数据分析师 → AI工程师

**AI时代的新要求**：
- 每个角色都需要具备AI素养
- 能够使用AI工具提升效率
- 能够与AI有效协作

---

## 本章小结

本章深入剖析了水力模型专业团队的五个核心角色：

1. **项目经理**：项目成功的第一责任人，统筹协调全局
2. **水力模型架构师**：技术把关人，质量守门人
3. **水力模型工程师**：核心执行者，模型构建者
4. **数据分析师**：数据守护者，价值挖掘者
5. **AI工程师**：AI赋能者，技术引领者

AI技术为每个角色都带来了显著的效率提升，未来AI将成为团队的"第六个虚拟角色"，与人类紧密协作。

理解每个角色的定位、职责和能力要求，是建设高效团队的基础。

---

## 代码示例汇总

本章提供以下代码示例：
1. AI智能周报生成器
2. AI辅助模型审查系统
3. AI代码助手
4. 管网数据异常检测
5. 管网数据可视化
6. 水力建模知识问答系统

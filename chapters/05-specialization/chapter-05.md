# 第5章 专业化与规范化

## 5.1 文档管理体系

### 5.1.1 文档管理的重要性

文档管理是专业化的基础：
- **知识沉淀**：避免知识随人员流失
- **质量保证**：标准化输出
- **效率提升**：减少重复工作
- **可追溯性**：问题追踪和经验复用

### 5.1.2 文档分类与命名规范

**文档分类体系**：
- 项目文档（按项目）
- 技术文档（按类型）
- 管理文档（按职能）
- 知识文档（按主题）

**命名规范**：
```
[日期]-[项目编号]-[文档类型]-[版本]
示例：20240313-PRJ001-报告-v1.0
```

### 5.1.3 AI在文档管理中的应用

**Python代码示例：文档自动分类系统**

```python
import os
import shutil
from pathlib import Path
import re

class DocumentClassifier:
    """文档自动分类系统"""
    
    def __init__(self, base_path):
        self.base_path = Path(base_path)
        self.categories = {
            'project': ['报告', '方案', '设计', '计算书'],
            'technical': ['规范', '标准', '手册', '指南'],
            'management': ['计划', '总结', '会议纪要'],
            'knowledge': ['案例', '经验', '最佳实践']
        }
        
    def classify_document(self, file_path):
        """根据文件名和内容分类文档"""
        file_name = Path(file_path).name
        
        # 基于关键词分类
        for category, keywords in self.categories.items():
            if any(keyword in file_name for keyword in keywords):
                return category
        
        # 基于文件类型分类
        if file_name.endswith(('.xlsx', '.xls', '.csv')):
            return 'data'
        elif file_name.endswith(('.py', '.ipynb')):
            return 'code'
        
        return 'uncategorized'
    
    def organize_folder(self, source_folder):
        """整理文件夹"""
        source = Path(source_folder)
        
        for file_path in source.iterdir():
            if file_path.is_file():
                category = self.classify_document(file_path)
                
                # 创建目标文件夹
                target_folder = self.base_path / category
                target_folder.mkdir(exist_ok=True)
                
                # 移动文件
                shutil.move(str(file_path), str(target_folder / file_path.name))
                print(f"已移动: {file_path.name} -> {category}/")
    
    def generate_index(self):
        """生成文档索引"""
        index = {}
        
        for category in self.categories.keys():
            category_path = self.base_path / category
            if category_path.exists():
                files = list(category_path.glob('*'))
                index[category] = [f.name for f in files if f.is_file()]
        
        return index

# 使用示例
classifier = DocumentClassifier('/path/to/documents')
classifier.organize_folder('/path/to/inbox')
index = classifier.generate_index()
print(index)
```

## 5.2 技术体系与知识复用

### 5.2.1 代码库建设

**Python管网数据处理函数库**：

```python
"""
pipe_utils.py - 管网数据处理工具库
"""

import pandas as pd
import numpy as np
from scipy import interpolate

def calculate_pipe_capacity(diameter, slope, roughness=0.013):
    """
    计算管道过流能力（曼宁公式）
    
    参数:
        diameter: 管径 (mm)
        slope: 坡度 (m/m)
        roughness: 曼宁糙率系数
    
    返回:
        流量 (m³/s)
    """
    # 转换为米
    D = diameter / 1000
    
    # 计算水力半径（满流假设）
    A = np.pi * (D/2)**2
    P = np.pi * D
    R = A / P
    
    # 曼宁公式
    Q = (1/roughness) * A * (R**(2/3)) * (slope**0.5)
    
    return Q

def check_pipe_data_quality(pipe_df):
    """
    检查管网数据质量
    
    参数:
        pipe_df: 管段DataFrame
    
    返回:
        质量检查结果
    """
    issues = []
    
    # 检查空值
    null_counts = pipe_df.isnull().sum()
    if null_counts.any():
        issues.append(f"发现空值: {null_counts[null_counts > 0].to_dict()}")
    
    # 检查管径
    invalid_diameter = pipe_df[
        (pipe_df['diameter'] <= 0) | 
        (pipe_df['diameter'] > 5000)
    ]
    if len(invalid_diameter) > 0:
        issues.append(f"发现{len(invalid_diameter)}根管径异常")
    
    # 检查坡度
    invalid_slope = pipe_df[
        (pipe_df['slope'] < -0.5) | 
        (pipe_df['slope'] > 0.5)
    ]
    if len(invalid_slope) > 0:
        issues.append(f"发现{len(invalid_slope)}根坡度异常")
    
    return {
        'total_pipes': len(pipe_df),
        'issues': issues,
        'is_valid': len(issues) == 0
    }

def interpolate_elevation(nodes_df, target_points):
    """
    插值计算节点高程
    
    参数:
        nodes_df: 已知高程的节点DataFrame
        target_points: 目标点坐标 [(x1,y1), (x2,y2), ...]
    
    返回:
        插值高程数组
    """
    from scipy.interpolate import griddata
    
    known_points = nodes_df[['x', 'y']].values
    known_elevations = nodes_df['elevation'].values
    
    interpolated = griddata(
        known_points, 
        known_elevations, 
        target_points, 
        method='linear'
    )
    
    return interpolated

def calculate_catchment_area(nodes_df, pipes_df, outlet_id):
    """
    计算汇水面积（基于管网拓扑）
    
    参数:
        nodes_df: 节点数据
        pipes_df: 管段数据
        outlet_id: 排放口节点ID
    
    返回:
        各节点对应的汇水面积
    """
    import networkx as nx
    
    # 构建有向图
    G = nx.DiGraph()
    
    for _, pipe in pipes_df.iterrows():
        G.add_edge(pipe['from_node'], pipe['to_node'])
    
    # 计算上游节点
    upstream_areas = {}
    
    for node in nodes_df['id']:
        try:
            # 找到所有上游节点
            upstream = nx.ancestors(G, node)
            upstream_areas[node] = len(upstream)
        except:
            upstream_areas[node] = 0
    
    return upstream_areas

# 使用示例
if __name__ == "__main__":
    # 示例数据
    pipe_data = pd.DataFrame({
        'id': ['P1', 'P2', 'P3'],
        'diameter': [500, 600, 800],
        'slope': [0.005, 0.008, 0.003],
        'length': [100, 150, 200]
    })
    
    # 计算过流能力
    for _, pipe in pipe_data.iterrows():
        Q = calculate_pipe_capacity(pipe['diameter'], pipe['slope'])
        print(f"管道{pipe['id']}: {Q:.3f} m³/s")
    
    # 检查数据质量
    quality = check_pipe_data_quality(pipe_data)
    print(f"数据质量: {'通过' if quality['is_valid'] else '不通过'}")
```

### 5.2.2 知识图谱构建

**Python代码示例：Neo4j知识图谱**

```python
from py2neo import Graph, Node, Relationship

class HydraulicKnowledgeGraph:
    """水力建模知识图谱"""
    
    def __init__(self, uri, user, password):
        self.graph = Graph(uri, auth=(user, password))
    
    def create_pipe_node(self, pipe_data):
        """创建管道节点"""
        node = Node("Pipe",
                   id=pipe_data['id'],
                   diameter=pipe_data['diameter'],
                   material=pipe_data.get('material', 'unknown'),
                   length=pipe_data.get('length', 0))
        self.graph.create(node)
        return node
    
    def create_node_node(self, node_data):
        """创建检查井节点"""
        node = Node("Manhole",
                   id=node_data['id'],
                   elevation=node_data['elevation'],
                   x=node_data.get('x', 0),
                   y=node_data.get('y', 0))
        self.graph.create(node)
        return node
    
    def create_relationship(self, from_node, to_node, rel_type, properties=None):
        """创建关系"""
        rel = Relationship(from_node, rel_type, to_node, **properties or {})
        self.graph.create(rel)
        return rel
    
    def query_upstream(self, node_id):
        """查询上游节点"""
        query = """
        MATCH path = (upstream)-[:FLOWS_TO*]->(n:Manhole {id: $node_id})
        RETURN upstream
        """
        result = self.graph.run(query, node_id=node_id)
        return [record["upstream"] for record in result]
    
    def query_connected_pipes(self, node_id):
        """查询连接的管道"""
        query = """
        MATCH (n:Manhole {id: $node_id})-[:CONNECTED_TO]-(p:Pipe)
        RETURN p
        """
        result = self.graph.run(query, node_id=node_id)
        return [record["p"] for record in result]

# 使用示例
kg = HydraulicKnowledgeGraph("bolt://localhost:7687", "neo4j", "password")

# 创建节点
pipe = kg.create_pipe_node({'id': 'P001', 'diameter': 500, 'material': 'concrete'})
manhole1 = kg.create_node_node({'id': 'N001', 'elevation': 10.5})
manhole2 = kg.create_node_node({'id': 'N002', 'elevation': 10.0})

# 创建关系
kg.create_relationship(pipe, manhole1, "STARTS_AT")
kg.create_relationship(pipe, manhole2, "ENDS_AT")
kg.create_relationship(manhole1, manhole2, "FLOWS_TO")
```

### 5.2.3 RAG智能知识问答

```python
from langchain.embeddings import OpenAIEmbeddings
from langchain.vectorstores import Chroma
from langchain.chains import RetrievalQA
from langchain.llms import OpenAI
from langchain.document_loaders import DirectoryLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter

class HydraulicRAGSystem:
    """水力建模RAG知识问答系统"""
    
    def __init__(self, api_key, docs_path):
        self.api_key = api_key
        self.docs_path = docs_path
        self.vectorstore = None
        self.qa_chain = None
        
    def load_documents(self):
        """加载文档"""
        loader = DirectoryLoader(self.docs_path, glob="**/*.txt")
        documents = loader.load()
        
        # 文本切分
        text_splitter = RecursiveCharacterTextSplitter(
            chunk_size=1000,
            chunk_overlap=200
        )
        texts = text_splitter.split_documents(documents)
        
        return texts
    
    def build_vectorstore(self):
        """构建向量数据库"""
        texts = self.load_documents()
        
        embeddings = OpenAIEmbeddings(openai_api_key=self.api_key)
        
        self.vectorstore = Chroma.from_documents(
            texts,
            embeddings,
            persist_directory="./hydraulic_knowledge_db"
        )
        
        self.vectorstore.persist()
        
    def create_qa_chain(self):
        """创建问答链"""
        if not self.vectorstore:
            self.build_vectorstore()
        
        llm = OpenAI(openai_api_key=self.api_key, temperature=0)
        
        self.qa_chain = RetrievalQA.from_chain_type(
            llm=llm,
            chain_type="stuff",
            retriever=self.vectorstore.as_retriever(search_kwargs={"k": 3}),
            return_source_documents=True
        )
    
    def query(self, question):
        """查询"""
        if not self.qa_chain:
            self.create_qa_chain()
        
        result = self.qa_chain({"query": question})
        
        return {
            'answer': result['result'],
            'sources': [doc.page_content[:200] for doc in result['source_documents']]
        }

# 使用示例
rag = HydraulicRAGSystem(api_key="your-key", docs_path="./technical_docs")

# 查询
response = rag.query("什么是曼宁公式？如何计算管道流量？")
print(response['answer'])
print("参考来源:", response['sources'])
```

## 5.3 人才管理体系

### 5.3.1 能力评估与发展

**Python代码示例：员工能力画像分析**

```python
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from radar_chart import radar_chart  # 假设有雷达图库

class EmployeeProfileAnalyzer:
    """员工能力画像分析器"""
    
    def __init__(self):
        self.skill_categories = {
            'technical': ['hydraulic_modeling', 'data_analysis', 'programming'],
            'tools': ['gis_software', 'modeling_software', 'python'],
            'soft': ['communication', 'teamwork', 'problem_solving'],
            'domain': ['drainage_knowledge', 'standards', 'project_experience']
        }
    
    def create_profile(self, employee_data):
        """创建员工能力画像"""
        profile = {}
        
        for category, skills in self.skill_categories.items():
            category_scores = []
            for skill in skills:
                score = employee_data.get(skill, 0)
                category_scores.append(score)
            
            profile[category] = {
                'skills': skills,
                'scores': category_scores,
                'average': np.mean(category_scores)
            }
        
        return profile
    
    def plot_radar_chart(self, profile, employee_name):
        """绘制雷达图"""
        categories = list(profile.keys())
        values = [profile[cat]['average'] for cat in categories]
        
        # 闭合图形
        values += values[:1]
        angles = np.linspace(0, 2*np.pi, len(categories), endpoint=False).tolist()
        angles += angles[:1]
        
        fig, ax = plt.subplots(figsize=(8, 8), subplot_kw=dict(polar=True))
        ax.plot(angles, values, 'o-', linewidth=2, label=employee_name)
        ax.fill(angles, values, alpha=0.25)
        ax.set_xticks(angles[:-1])
        ax.set_xticklabels(categories)
        ax.set_ylim(0, 5)
        ax.legend()
        
        return fig
    
    def compare_profiles(self, profiles):
        """对比多个员工的能力画像"""
        comparison = pd.DataFrame()
        
        for name, profile in profiles.items():
            comparison[name] = [profile[cat]['average'] for cat in self.skill_categories.keys()]
        
        comparison.index = list(self.skill_categories.keys())
        
        return comparison
    
    def generate_development_plan(self, profile, target_level='L3'):
        """生成发展计划"""
        target_skills = {
            'L2': {'technical': 3, 'tools': 3, 'soft': 3, 'domain': 2},
            'L3': {'technical': 4, 'tools': 4, 'soft': 3, 'domain': 3},
            'L4': {'technical': 5, 'tools': 4, 'soft': 4, 'domain': 4}
        }
        
        gaps = {}
        targets = target_skills.get(target_level, target_skills['L3'])
        
        for category, target_score in targets.items():
            current_score = profile[category]['average']
            gap = target_score - current_score
            
            if gap > 0:
                gaps[category] = {
                    'current': current_score,
                    'target': target_score,
                    'gap': gap,
                    'priority': 'high' if gap > 1 else 'medium'
                }
        
        return gaps

# 使用示例
analyzer = EmployeeProfileAnalyzer()

# 示例员工数据
employee = {
    'name': '张三',
    'hydraulic_modeling': 4,
    'data_analysis': 3,
    'programming': 2,
    'gis_software': 4,
    'modeling_software': 4,
    'python': 3,
    'communication': 3,
    'teamwork': 4,
    'problem_solving': 4,
    'drainage_knowledge': 3,
    'standards': 3,
    'project_experience': 2
}

# 创建画像
profile = analyzer.create_profile(employee)

# 绘制雷达图
fig = analyzer.plot_radar_chart(profile, employee['name'])
plt.savefig('employee_profile.png')

# 生成发展计划
gaps = analyzer.generate_development_plan(profile, target_level='L3')
print("能力差距分析:", gaps)
```

## 5.4 项目管理体系

### 5.4.1 项目度量与监控

**Python代码示例：项目度量数据可视化仪表盘**

```python
import dash
from dash import dcc, html
from dash.dependencies import Input, Output
import plotly.express as px
import plotly.graph_objects as go
import pandas as pd

class ProjectDashboard:
    """项目度量仪表盘"""
    
    def __init__(self, project_data):
        self.app = dash.Dash(__name__)
        self.data = project_data
        self.setup_layout()
        self.setup_callbacks()
    
    def setup_layout(self):
        """设置布局"""
        self.app.layout = html.Div([
            html.H1("项目度量仪表盘", style={'textAlign': 'center'}),
            
            # 关键指标卡片
            html.Div([
                html.Div([
                    html.H3("项目总数"),
                    html.H2(id='total-projects')
                ], className='metric-card'),
                
                html.Div([
                    html.H3("平均进度"),
                    html.H2(id='avg-progress')
                ], className='metric-card'),
                
                html.Div([
                    html.H3("延期项目数"),
                    html.H2(id='delayed-projects')
                ], className='metric-card'),
            ], style={'display': 'flex', 'justifyContent': 'space-around'}),
            
            # 图表区域
            html.Div([
                dcc.Graph(id='progress-chart'),
                dcc.Graph(id='resource-chart')
            ]),
            
            # 更新时间
            dcc.Interval(id='interval', interval=5000)  # 5秒更新
        ])
    
    def setup_callbacks(self):
        """设置回调"""
        
        @self.app.callback(
            [Output('total-projects', 'children'),
             Output('avg-progress', 'children'),
             Output('delayed-projects', 'children')],
            [Input('interval', 'n_intervals')]
        )
        def update_metrics(n):
            total = len(self.data)
            avg_progress = self.data['progress'].mean()
            delayed = len(self.data[self.data['status'] == 'delayed'])
            
            return str(total), f"{avg_progress:.1f}%", str(delayed)
        
        @self.app.callback(
            Output('progress-chart', 'figure'),
            [Input('interval', 'n_intervals')]
        )
        def update_progress_chart(n):
            fig = px.bar(
                self.data,
                x='project_name',
                y='progress',
                color='status',
                title='项目进度'
            )
            return fig
    
    def run(self, debug=False):
        """运行仪表盘"""
        self.app.run_server(debug=debug)

# 使用示例
project_data = pd.DataFrame({
    'project_name': ['项目A', '项目B', '项目C', '项目D'],
    'progress': [80, 60, 90, 40],
    'status': ['normal', 'delayed', 'normal', 'delayed'],
    'resources': [5, 8, 4, 6]
})

dashboard = ProjectDashboard(project_data)
dashboard.run()
```

### 5.4.2 AI在项目管理中的应用

**Python代码示例：项目风险预测模型**

```python
import pandas as pd
import numpy as np
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report
import joblib

class ProjectRiskPredictor:
    """项目风险预测器"""
    
    def __init__(self):
        self.model = RandomForestClassifier(n_estimators=100)
        self.is_trained = False
    
    def prepare_features(self, project_data):
        """准备特征"""
        features = pd.DataFrame()
        
        # 项目特征
        features['project_size'] = project_data['model_nodes'] / 1000  # 项目规模（千节点）
        features['team_size'] = project_data['team_size']
        features['estimated_duration'] = project_data['estimated_days']
        features['complexity_score'] = project_data['complexity']  # 复杂度评分1-5
        features['client_experience'] = project_data['client_experience']  # 客户合作经验
        features['data_quality'] = project_data['data_quality_score']  # 数据质量评分
        
        # 历史特征
        features['similar_projects'] = project_data['similar_completed']
        features['pm_experience'] = project_data['pm_years_experience']
        
        return features
    
    def train(self, historical_data):
        """训练模型"""
        X = self.prepare_features(historical_data)
        y = historical_data['risk_occurred']  # 是否发生风险
        
        X_train, X_test, y_train, y_test = train_test_split(
            X, y, test_size=0.2, random_state=42
        )
        
        self.model.fit(X_train, y_train)
        self.is_trained = True
        
        # 评估
        y_pred = self.model.predict(X_test)
        print(classification_report(y_test, y_pred))
        
        # 特征重要性
        importance = pd.DataFrame({
            'feature': X.columns,
            'importance': self.model.feature_importances_
        }).sort_values('importance', ascending=False)
        
        print("特征重要性:", importance)
    
    def predict_risk(self, new_project):
        """预测项目风险"""
        if not self.is_trained:
            raise Exception("模型未训练")
        
        X = self.prepare_features(new_project)
        
        # 预测概率
        risk_prob = self.model.predict_proba(X)[:, 1]
        
        # 风险等级
        risk_level = pd.cut(
            risk_prob,
            bins=[0, 0.3, 0.6, 1.0],
            labels=['low', 'medium', 'high']
        )
        
        return {
            'risk_probability': risk_prob,
            'risk_level': risk_level,
            'recommendations': self._generate_recommendations(risk_level.iloc[0])
        }
    
    def _generate_recommendations(self, risk_level):
        """生成建议"""
        recommendations = {
            'low': ['按计划执行', '定期监控'],
            'medium': ['增加检查点', '准备应急预案'],
            'high': ['重新评估计划', '增加资源投入', '降低范围']
        }
        return recommendations.get(risk_level, ['评估风险'])
    
    def save_model(self, filepath):
        """保存模型"""
        joblib.dump(self.model, filepath)
    
    def load_model(self, filepath):
        """加载模型"""
        self.model = joblib.load(filepath)
        self.is_trained = True

# 使用示例
predictor = ProjectRiskPredictor()

# 训练数据
historical_data = pd.DataFrame({
    'model_nodes': [5000, 8000, 3000, 10000, 6000],
    'team_size': [3, 5, 2, 8, 4],
    'estimated_days': [60, 90, 45, 120, 75],
    'complexity': [3, 4, 2, 5, 3],
    'client_experience': [1, 0, 1, 0, 1],
    'data_quality_score': [4, 3, 5, 2, 4],
    'similar_completed': [5, 2, 8, 1, 4],
    'pm_years_experience': [3, 5, 2, 4, 6],
    'risk_occurred': [0, 1, 0, 1, 0]  # 是否发生风险
})

# 训练
predictor.train(historical_data)

# 预测新项目
new_project = pd.DataFrame({
    'model_nodes': [7000],
    'team_size': [4],
    'estimated_days': [80],
    'complexity': [4],
    'client_experience': [0],
    'data_quality_score': [3],
    'similar_completed': [2],
    'pm_years_experience': [3]
})

prediction = predictor.predict_risk(new_project)
print(f"风险概率: {prediction['risk_probability'][0]:.2%}")
print(f"风险等级: {prediction['risk_level'][0]}")
print(f"建议: {prediction['recommendations']}")
```

## 5.5 质量管理体系

### 5.5.1 质量检查工具

**Python代码示例：模型质量自动检查工具**

```python
import pandas as pd
import numpy as np

class ModelQualityChecker:
    """模型质量检查器"""
    
    def __init__(self):
        self.check_results = []
        
    def check_geometry(self, nodes_df, pipes_df):
        """检查几何数据"""
        issues = []
        
        # 检查节点高程
        invalid_elevation = nodes_df[
            (nodes_df['elevation'] < -50) | 
            (nodes_df['elevation'] > 200)
        ]
        if len(invalid_elevation) > 0:
            issues.append({
                'type': 'error',
                'category': '高程',
                'message': f'{len(invalid_elevation)}个节点高程异常',
                'items': invalid_elevation['id'].tolist()
            })
        
        # 检查管道长度
        invalid_length = pipes_df[pipes_df['length'] <= 0]
        if len(invalid_length) > 0:
            issues.append({
                'type': 'error',
                'category': '管长',
                'message': f'{len(invalid_length)}根管道长度异常',
                'items': invalid_length['id'].tolist()
            })
        
        return issues
    
    def check_topology(self, nodes_df, pipes_df):
        """检查拓扑关系"""
        issues = []
        
        # 检查孤立节点
        all_nodes = set(nodes_df['id'])
        connected_nodes = set(pipes_df['from_node']) | set(pipes_df['to_node'])
        isolated = all_nodes - connected_nodes
        
        if isolated:
            issues.append({
                'type': 'warning',
                'category': '拓扑',
                'message': f'{len(isolated)}个孤立节点',
                'items': list(isolated)
            })
        
        # 检查是否存在环
        # （简化版，实际需要图算法）
        
        return issues
    
    def check_hydraulic(self, pipes_df):
        """检查水力参数"""
        issues = []
        
        # 检查管径
        invalid_diameter = pipes_df[
            (pipes_df['diameter'] <= 0) | 
            (pipes_df['diameter'] > 5000)
        ]
        if len(invalid_diameter) > 0:
            issues.append({
                'type': 'error',
                'category': '管径',
                'message': f'{len(invalid_diameter)}根管道管径异常',
                'items': invalid_diameter['id'].tolist()
            })
        
        # 检查坡度
        invalid_slope = pipes_df[abs(pipes_df['slope']) > 0.5]
        if len(invalid_slope) > 0:
            issues.append({
                'type': 'warning',
                'category': '坡度',
                'message': f'{len(invalid_slope)}根管道坡度异常',
                'items': invalid_slope['id'].tolist()
            })
        
        return issues
    
    def run_all_checks(self, nodes_df, pipes_df):
        """运行所有检查"""
        all_issues = []
        
        all_issues.extend(self.check_geometry(nodes_df, pipes_df))
        all_issues.extend(self.check_topology(nodes_df, pipes_df))
        all_issues.extend(self.check_hydraulic(pipes_df))
        
        # 生成报告
        report = self._generate_report(all_issues)
        return report
    
    def _generate_report(self, issues):
        """生成检查报告"""
        errors = [i for i in issues if i['type'] == 'error']
        warnings = [i for i in issues if i['type'] == 'warning']
        
        return {
            'status': 'fail' if errors else 'pass',
            'summary': {
                'total_issues': len(issues),
                'errors': len(errors),
                'warnings': len(warnings)
            },
            'details': issues
        }

# 使用示例
checker = ModelQualityChecker()

# 示例数据
nodes = pd.DataFrame({
    'id': ['N1', 'N2', 'N3', 'N4'],
    'elevation': [10.5, 9.8, 500, 9.2]  # N3高程异常
})

pipes = pd.DataFrame({
    'id': ['P1', 'P2', 'P3'],
    'from_node': ['N1', 'N2', 'N3'],
    'to_node': ['N2', 'N3', 'N4'],
    'diameter': [500, 600, 0],  # P3管径异常
    'length': [100, 150, 200],
    'slope': [0.005, 0.6, 0.003]  # P2坡度异常
})

# 运行检查
report = checker.run_all_checks(nodes, pipes)
print(f"检查状态: {report['status']}")
print(f"错误数: {report['summary']['errors']}")
print(f"警告数: {report['summary']['warnings']}")
```

### 5.5.2 AI辅助质量审查

```python
# AI辅助质量审查（基于前面的ModelReviewer类扩展）
class AIQualityReviewer(ModelQualityChecker):
    """AI增强的质量审查器"""
    
    def __init__(self, llm_api_key):
        super().__init__()
        self.llm_api_key = llm_api_key
    
    def ai_analyze_issues(self, issues, model_context):
        """AI分析问题根因"""
        import openai
        
        prompt = f"""
        作为水力建模专家，请分析以下模型质量问题：
        
        问题列表：
        {issues}
        
        模型背景：
        {model_context}
        
        请分析：
        1. 可能的原因
        2. 修复建议
        3. 预防措施
        """
        
        response = openai.ChatCompletion.create(
            model="gpt-4",
            messages=[
                {"role": "system", "content": "你是水力建模质量专家。"},
                {"role": "user", "content": prompt}
            ]
        )
        
        return response.choices[0].message.content
```

## 5.6 技术创新体系

### 5.6.1 数据挖掘应用案例

**案例1：管网堵塞预测**

```python
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
import pandas as pd

# 特征工程
features = pd.DataFrame({
    'pipe_age': pipe_data['age'],  # 管龄
    'pipe_diameter': pipe_data['diameter'],  # 管径
    'slope': pipe_data['slope'],  # 坡度
    'flow_velocity': flow_data['velocity'],  # 流速
    'sediment_accumulation': sediment_data['amount'],  # 淤积量
    'maintenance_frequency': maintenance_data['frequency']  # 维护频次
})

# 目标变量（是否发生堵塞）
target = blockage_history['occurred']

# 训练模型
model = RandomForestClassifier()
model.fit(features, target)

# 预测风险
risk_scores = model.predict_proba(new_pipes)[:, 1]
```

**案例2：泵站能耗优化**

```python
from scipy.optimize import minimize

def pump_energy_consumption(pump_schedule):
    """
    计算泵站能耗
    
    参数:
        pump_schedule: 泵站运行计划 [(time, pump_id, speed), ...]
    
    返回:
        总能耗 (kWh)
    """
    total_energy = 0
    
    for time, pump_id, speed in pump_schedule:
        # 水泵功率曲线
        power = pump_curves[pump_id]['power'](speed, flow_rate)
        duration = get_duration(time)
        total_energy += power * duration
    
    return total_energy

# 优化目标：最小化能耗，满足排水需求
constraints = [
    {'type': 'ineq', 'fun': lambda x: tank_level(x) - min_level},  # 液位不低于最低值
    {'type': 'ineq', 'fun': lambda x: max_level - tank_level(x)}   # 液位不高于最高值
]

result = minimize(
    pump_energy_consumption,
    x0=initial_schedule,
    method='SLSQP',
    constraints=constraints
)

optimal_schedule = result.x
```

### 5.6.2 数据可视化应用案例

**实时监测数据仪表盘**：

```python
import streamlit as st
import plotly.graph_objects as go
from datetime import datetime, timedelta

st.title("排水系统实时监测仪表盘")

# 侧边栏控制
st.sidebar.header("控制面板")
selected_station = st.sidebar.selectbox("选择监测点", station_list)
time_range = st.sidebar.slider("时间范围", 1, 24, 6)

# 获取实时数据
data = get_realtime_data(selected_station, hours=time_range)

# 水位趋势图
fig = go.Figure()
fig.add_trace(go.Scatter(
    x=data['timestamp'],
    y=data['water_level'],
    mode='lines',
    name='水位'
))
fig.add_hline(y=warning_level, line_dash="dash", line_color="orange", name='预警水位')
fig.add_hline(y=alarm_level, line_dash="dash", line_color="red", name='报警水位')

st.plotly_chart(fig)

# 状态卡片
col1, col2, col3 = st.columns(3)
current_level = data['water_level'].iloc[-1]

current_status = "正常" if current_level < warning_level else "预警" if current_level < alarm_level else "报警"
status_color = "green" if current_status == "正常" else "orange" if current_status == "预警" else "red"

col1.metric("当前水位", f"{current_level:.2f}m", current_status)
col2.metric("流量", f"{data['flow'].iloc[-1]:.2f}m³/s")
col3.metric("更新时间", data['timestamp'].iloc[-1].strftime("%H:%M:%S"))
```

---

## 本章小结

本章详细介绍了专业化与规范化的各个方面：

1. **文档管理**：分类、命名规范、AI自动分类
2. **技术体系**：代码库、知识图谱、RAG系统
3. **人才管理**：能力评估、发展计划
4. **项目管理**：度量监控、风险预测
5. **质量管理**：自动检查、AI辅助审查
6. **技术创新**：数据挖掘、可视化

通过信息化工具和AI技术，可以大幅提升团队的专业化水平。

---

## 代码示例汇总

本章提供15+代码示例，涵盖：
- 文档自动分类
- 管网数据处理函数库
- 知识图谱构建
- RAG智能问答
- 员工能力画像
- 项目度量仪表盘
- 风险预测模型
- 质量检查工具
- 管网堵塞预测
- 泵站能耗优化
- 实时监测仪表盘

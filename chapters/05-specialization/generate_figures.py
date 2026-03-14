#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
第5章配图生成脚本
生成水力模型专业化与规范化技术实施章节所需的专业配图
"""

import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
from matplotlib.patches import FancyBboxPatch, Circle, Rectangle, FancyArrowPatch
import numpy as np
import os

# 设置中文字体
plt.rcParams['font.family'] = ['Noto Sans CJK JP', 'DejaVu Sans']
plt.rcParams['axes.unicode_minus'] = False

# 创建输出目录
output_dir = "/root/.openclaw/workspace/HEBook/chapters/05-specialization/images"
os.makedirs(output_dir, exist_ok=True)

def save_fig(fig, filename):
    """保存图片"""
    filepath = os.path.join(output_dir, filename)
    fig.savefig(filepath, dpi=150, bbox_inches='tight', facecolor='white')
    print(f"已保存: {filepath}")
    plt.close(fig)

# ============ 图1: L1-L5技术支撑体系 ============
def create_tech_support_system():
    """创建L1-L5技术支撑体系图"""
    fig, ax = plt.subplots(figsize=(14, 10))
    
    levels = [
        {'level': 'L1→L2', 'name': '项目管理信息化', 'systems': ['文档管理', '版本控制', '进度跟踪'], 'color': '#9E9E9E', 'y': 8},
        {'level': 'L2→L3', 'name': '技术体系标准化', 'systems': ['流程管理', '模板库', '知识库'], 'color': '#FFC107', 'y': 6},
        {'level': 'L3→L4', 'name': '量化管理驱动', 'systems': ['度量采集', '风险预测', '架构管理'], 'color': '#2196F3', 'y': 4},
        {'level': 'L4→L5', 'name': '智能化创新', 'systems': ['AI辅助', '研究管理', '知识图谱'], 'color': '#9C27B0', 'y': 2},
    ]
    
    for item in levels:
        # 等级标签
        rect = FancyBboxPatch((1, item['y']-0.5), 2, 1, boxstyle="round,pad=0.02",
                             facecolor=item['color'], edgecolor='black', linewidth=2)
        ax.add_patch(rect)
        ax.text(2, item['y'], item['level'], ha='center', va='center', 
               fontsize=11, fontweight='bold', color='white')
        
        # 技术系统名称
        ax.text(4, item['y'], item['name'], ha='left', va='center', 
               fontsize=12, fontweight='bold', color=item['color'])
        
        # 支撑系统列表
        for i, system in enumerate(item['systems']):
            x = 8 + i * 2.5
            rect = FancyBboxPatch((x-1, item['y']-0.35), 2, 0.7, boxstyle="round,pad=0.02",
                                 facecolor='#F5F5F5', edgecolor='#999999', linewidth=1)
            ax.add_patch(rect)
            ax.text(x, item['y'], system, ha='center', va='center', fontsize=9)
    
    ax.set_xlim(0, 16)
    ax.set_ylim(0, 10)
    ax.axis('off')
    ax.set_title('L1-L5技术支撑体系', fontsize=18, fontweight='bold', pad=20)
    
    save_fig(fig, 'fig_5_0_tech_support.png')

# ============ 图2: 项目管理工具选型对比 ============
def create_pm_tools_comparison():
    """创建项目管理工具选型对比图"""
    fig, ax = plt.subplots(figsize=(12, 8))
    
    tools = ['飞书项目', 'Jira', 'Teambition', 'PingCode', 'Project']
    scores = {
        '易用性': [5, 3, 5, 4, 2],
        '功能性': [3, 5, 3, 4, 5],
        '性价比': [5, 3, 4, 4, 2],
        '集成度': [5, 4, 3, 4, 3],
    }
    
    x = np.arange(len(tools))
    width = 0.2
    colors = ['#4CAF50', '#2196F3', '#FFC107', '#9C27B0']
    
    for i, (metric, values) in enumerate(scores.items()):
        offset = (i - 1.5) * width
        bars = ax.bar(x + offset, values, width, label=metric, color=colors[i])
    
    ax.set_ylabel('评分 (1-5)', fontsize=12)
    ax.set_title('项目管理工具选型对比', fontsize=16, fontweight='bold')
    ax.set_xticks(x)
    ax.set_xticklabels(tools)
    ax.legend()
    ax.set_ylim(0, 6)
    ax.grid(axis='y', alpha=0.3)
    
    save_fig(fig, 'fig_5_1_pm_tools.png')

# ============ 图3: 数据质量检查流程 ============
def create_data_quality_flow():
    """创建数据质量检查流程图"""
    fig, ax = plt.subplots(figsize=(14, 8))
    
    steps = [
        ('数据输入', '#E3F2FD', ['CAD图纸', 'GIS数据', '监测数据', '遥感数据']),
        ('完整性检查', '#BBDEFB', ['字段完整', '拓扑完整', '时序完整', '空间完整']),
        ('合理性检查', '#90CAF9', ['数值范围', '逻辑关系', '时空一致性', '变化趋势']),
        ('质量评分', '#64B5F6', ['A级(优秀)', 'B级(良好)', 'C级(合格)', 'D级(不合格)']),
        ('问题修复', '#42A5F5', ['自动修复', '人工修复', '数据补测', '标记排除']),
    ]
    
    for i, (name, color, items) in enumerate(steps):
        x = i * 2.5 + 1.5
        
        # 主框
        rect = FancyBboxPatch((x-1, 4), 2, 1.5, boxstyle="round,pad=0.02",
                             facecolor=color, edgecolor='black', linewidth=2)
        ax.add_patch(rect)
        ax.text(x, 4.75, name, ha='center', va='center', fontsize=11, fontweight='bold')
        
        # 详细项目
        for j, item in enumerate(items):
            ax.text(x, 3.2 - j*0.5, f"• {item}", ha='center', va='center', fontsize=9)
        
        # 箭头
        if i < len(steps) - 1:
            ax.annotate('', xy=(x + 1.5, 4.75), xytext=(x + 1, 4.75),
                       arrowprops=dict(arrowstyle='->', lw=2.5, color='#333333'))
    
    ax.set_xlim(0, 14)
    ax.set_ylim(0, 7)
    ax.axis('off')
    ax.set_title('数据质量检查流程', fontsize=18, fontweight='bold', pad=20)
    
    save_fig(fig, 'fig_5_2_data_quality_flow.png')

# ============ 图4: 度量指标体系 ============
def create_metrics_system():
    """创建度量指标体系图"""
    fig, ax = plt.subplots(figsize=(14, 10))
    
    # 四个维度
    dimensions = [
        {'name': '生产力指标', 'metrics': ['人均节点数', '项目完成率', '代码产出量', '文档产出量'], 'color': '#4CAF50', 'pos': (2, 7)},
        {'name': '质量指标', 'metrics': ['返工率', '缺陷率', '客户满意度', '审核通过率'], 'color': '#F44336', 'pos': (8, 7)},
        {'name': '效率指标', 'metrics': ['按时交付率', '估算准确率', '资源利用率', '响应时效'], 'color': '#2196F3', 'pos': (2, 3)},
        {'name': '成长指标', 'metrics': ['技能提升度', '知识分享数', '创新提案数', '培训完成率'], 'color': '#9C27B0', 'pos': (8, 3)},
    ]
    
    center_x, center_y = 7, 7
    
    for dim in dimensions:
        x, y = dim['pos']
        
        # 维度主框
        rect = FancyBboxPatch((x-1.5, y-0.5), 3, 1, boxstyle="round,pad=0.02",
                             facecolor=dim['color'], edgecolor='black', linewidth=2)
        ax.add_patch(rect)
        ax.text(x, y, dim['name'], ha='center', va='center', 
               fontsize=12, fontweight='bold', color='white')
        
        # 具体指标
        for i, metric in enumerate(dim['metrics']):
            offset_y = -1 - i * 0.6
            rect = FancyBboxPatch((x-1.2, y+offset_y-0.25), 2.4, 0.5, 
                                 boxstyle="round,pad=0.02",
                                 facecolor='#F5F5F5', edgecolor=dim['color'], linewidth=1)
            ax.add_patch(rect)
            ax.text(x, y+offset_y, metric, ha='center', va='center', fontsize=10)
    
    ax.set_xlim(0, 14)
    ax.set_ylim(0, 10)
    ax.axis('off')
    ax.set_title('团队度量指标体系', fontsize=18, fontweight='bold', pad=20)
    
    save_fig(fig, 'fig_5_3_metrics_system.png')

# ============ 图5: AI在各管理系统中的应用 ============
def create_ai_applications():
    """创建AI在各管理系统中的应用图"""
    fig, ax = plt.subplots(figsize=(14, 10))
    
    # 中心AI能力
    center = Circle((7, 5), 1.2, facecolor='#9C27B0', edgecolor='black', linewidth=3)
    ax.add_patch(center)
    ax.text(7, 5, 'AI\n能力', ha='center', va='center', 
           fontsize=14, fontweight='bold', color='white')
    
    # 各管理系统
    systems = [
        {'name': '文档管理', 'scenarios': ['智能分类', '自动摘要', '语义搜索'], 'angle': 90, 'color': '#2196F3'},
        {'name': '项目管理', 'scenarios': ['智能估算', '风险预警', '资源优化'], 'angle': 30, 'color': '#4CAF50'},
        {'name': '质量管理', 'scenarios': ['自动审查', '异常检测', '根因分析'], 'angle': -30, 'color': '#F44336'},
        {'name': '人才管理', 'scenarios': ['能力画像', '发展推荐', '离职预警'], 'angle': -90, 'color': '#FF9800'},
        {'name': '知识管理', 'scenarios': ['智能问答', '知识抽取', '关联推荐'], 'angle': -150, 'color': '#9C27B0'},
        {'name': '创新研究', 'scenarios': ['趋势预测', '方案生成', '论文辅助'], 'angle': 150, 'color': '#00BCD4'},
    ]
    
    for system in systems:
        angle_rad = np.deg2rad(system['angle'])
        x = 7 + 4 * np.cos(angle_rad)
        y = 5 + 4 * np.sin(angle_rad)
        
        # 连线
        ax.plot([7 + 1.2*np.cos(angle_rad), x - 1.3*np.cos(angle_rad)], 
               [5 + 1.2*np.sin(angle_rad), y - 1.3*np.sin(angle_rad)], 
               'k-', linewidth=2, alpha=0.3)
        
        # 系统框
        rect = FancyBboxPatch((x-1.4, y-0.5), 2.8, 1, boxstyle="round,pad=0.02",
                             facecolor=system['color'], edgecolor='black', linewidth=2)
        ax.add_patch(rect)
        ax.text(x, y, system['name'], ha='center', va='center', 
               fontsize=11, fontweight='bold', color='white')
        
        # AI应用场景
        for i, scenario in enumerate(system['scenarios']):
            offset_y = 0.9 + i * 0.5
            ax.text(x, y + offset_y, f"• {scenario}", ha='center', va='center', 
                   fontsize=9, color=system['color'])
    
    ax.set_xlim(0, 14)
    ax.set_ylim(0, 10)
    ax.axis('off')
    ax.set_title('AI在各管理系统中的应用场景', fontsize=18, fontweight='bold', pad=20)
    
    save_fig(fig, 'fig_5_6_ai_applications.png')

# ============ 主函数 ============
def main():
    print("开始生成第5章配图...")
    print(f"输出目录: {output_dir}")
    
    create_tech_support_system()
    create_pm_tools_comparison()
    create_data_quality_flow()
    create_metrics_system()
    create_ai_applications()
    
    print("\n所有配图生成完成!")

if __name__ == '__main__':
    main()

#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
第4章配图生成脚本
生成水力模型角色详解章节所需的专业配图
"""

import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
from matplotlib.patches import FancyBboxPatch, Circle, Rectangle, FancyArrowPatch, Wedge
import numpy as np
import os

# 设置中文字体
plt.rcParams['font.family'] = ['Noto Sans CJK JP', 'DejaVu Sans']
plt.rcParams['axes.unicode_minus'] = False

# 创建输出目录
output_dir = "/root/.openclaw/workspace/HEBook/chapters/04-roles/images"
os.makedirs(output_dir, exist_ok=True)

def save_fig(fig, filename):
    """保存图片"""
    filepath = os.path.join(output_dir, filename)
    fig.savefig(filepath, dpi=150, bbox_inches='tight', facecolor='white')
    print(f"已保存: {filepath}")
    plt.close(fig)

# ============ 图1: 五角色协作关系图 ============
def create_five_roles_collaboration():
    """创建五角色协作关系图"""
    fig, ax = plt.subplots(figsize=(13, 10))
    
    # 中心项目成功
    center = Circle((0, 0), 1.2, facecolor='#FFD700', edgecolor='black', linewidth=2)
    ax.add_patch(center)
    ax.text(0, 0, '项目\n成功', ha='center', va='center', fontsize=12, fontweight='bold')
    
    # 五个角色位置
    roles = [
        {'name': '项目经理\nPM', 'subtitle': '统筹全局', 'color': '#F44336', 'angle': 90},
        {'name': '架构师\nArchitect', 'subtitle': '技术把关', 'color': '#FF9800', 'angle': 18},
        {'name': '水力工程师\nModeler', 'subtitle': '核心执行', 'color': '#2196F3', 'angle': -54},
        {'name': '数据分析师\nDA', 'subtitle': '数据支撑', 'color': '#4CAF50', 'angle': -126},
        {'name': 'AI工程师\nAI', 'subtitle': '智能赋能', 'color': '#9C27B0', 'angle': -198},
    ]
    
    radius = 4
    
    # 绘制角色节点和连线
    for role in roles:
        angle_rad = np.deg2rad(role['angle'])
        x = radius * np.cos(angle_rad)
        y = radius * np.sin(angle_rad)
        
        # 与中心的连线
        ax.plot([0, x*0.7], [0, y*0.7], 'k-', linewidth=1.5, alpha=0.3)
        
        # 角色节点
        circle = Circle((x, y), 1, facecolor=role['color'], edgecolor='black', linewidth=2)
        ax.add_patch(circle)
        ax.text(x, y, role['name'], ha='center', va='center', 
               fontsize=10, fontweight='bold', color='white', linespacing=0.8)
        
        # 副标题
        ax.text(x, y+1.6, role['subtitle'], ha='center', va='center', 
               fontsize=10, color=role['color'], fontweight='bold')
    
    # 绘制角色间的协作连线
    for i in range(5):
        angle1 = np.deg2rad(roles[i]['angle'])
        angle2 = np.deg2rad(roles[(i+1)%5]['angle'])
        x1, y1 = radius * np.cos(angle1), radius * np.sin(angle1)
        x2, y2 = radius * np.cos(angle2), radius * np.sin(angle2)
        ax.plot([x1*0.85, x2*0.85], [y1*0.85, y2*0.85], 'k--', linewidth=1, alpha=0.2)
    
    ax.set_xlim(-6, 6)
    ax.set_ylim(-6, 6)
    ax.set_aspect('equal')
    ax.axis('off')
    ax.set_title('五角色协作关系图', fontsize=18, fontweight='bold', pad=20)
    
    save_fig(fig, 'fig_4_0_five_roles.png')

# ============ 图2: 水力模型架构层次图 ============
def create_hydraulic_architecture():
    """创建水力模型架构层次图"""
    fig, ax = plt.subplots(figsize=(14, 10))
    
    # 架构层次
    layers = [
        {'name': '应用层', 'items': ['实时预报', '洪水预警', '设计评估', '调度优化'], 'color': '#E8F5E9', 'y': 8},
        {'name': '模型层', 'items': ['降雨径流模型', '河网汇流模型', '一维水动力', '二维漫流模型'], 'color': '#E3F2FD', 'y': 6},
        {'name': '数据层', 'items': ['气象数据', '地形数据', '管网数据', '监测数据'], 'color': '#FFF3E0', 'y': 4},
        {'name': '基础设施层', 'items': ['计算集群', '存储系统', '网络传输', '安全保障'], 'color': '#F3E5F5', 'y': 2},
    ]
    
    for layer in layers:
        # 层标题
        rect = FancyBboxPatch((0.5, layer['y']-0.3), 2, 0.6, boxstyle="round,pad=0.02",
                             facecolor=layer['color'], edgecolor='black', linewidth=2)
        ax.add_patch(rect)
        ax.text(1.5, layer['y'], layer['name'], ha='center', va='center', 
               fontsize=12, fontweight='bold')
        
        # 层内组件
        for i, item in enumerate(layer['items']):
            x = 4 + i * 2.5
            rect = FancyBboxPatch((x-1, layer['y']-0.3), 2, 0.6, boxstyle="round,pad=0.02",
                                 facecolor='white', edgecolor='#666666', linewidth=1)
            ax.add_patch(rect)
            ax.text(x, layer['y'], item, ha='center', va='center', fontsize=10)
        
        # 层间箭头
        if layer['y'] > 2:
            ax.annotate('', xy=(7, layer['y']-0.6), xytext=(7, layer['y']-1.4),
                       arrowprops=dict(arrowstyle='<->', lw=2, color='#666666'))
    
    ax.set_xlim(0, 13)
    ax.set_ylim(0.5, 9.5)
    ax.set_aspect('equal')
    ax.axis('off')
    ax.set_title('水力模型系统架构层次', fontsize=18, fontweight='bold', pad=20)
    
    save_fig(fig, 'fig_4_2_architecture_layers.png')

# ============ 图3: NWM架构图 ============
def create_nwm_architecture():
    """创建美国国家水模型架构图"""
    fig, ax = plt.subplots(figsize=(16, 10))
    
    # 标题
    ax.text(8, 9.5, '美国国家水模型 (NWM) 架构体系', ha='center', va='center', 
           fontsize=18, fontweight='bold')
    
    # 数据输入层
    input_data = [
        ('MRMS\n雷达数据', 1, 7.5),
        ('HRRR/RAP\n气象预报', 4, 7.5),
        ('GFS/CFS\n全球预报', 7, 7.5),
        ('USGS\n实测数据', 10, 7.5),
        ('水库\n调度数据', 13, 7.5),
    ]
    
    for name, x, y in input_data:
        rect = FancyBboxPatch((x-1, y-0.5), 2, 1, boxstyle="round,pad=0.02",
                             facecolor='#BBDEFB', edgecolor='#1976D2', linewidth=2)
        ax.add_patch(rect)
        ax.text(x, y, name, ha='center', va='center', fontsize=9)
    
    # 输入箭头
    for x in [1, 4, 7, 10, 13]:
        ax.annotate('', xy=(x, 6.3), xytext=(x, 6.8),
                   arrowprops=dict(arrowstyle='->', lw=2, color='#1976D2'))
    
    # 核心模型层
    core_rect = FancyBboxPatch((2, 3.5), 10, 2.5, boxstyle="round,pad=0.05",
                              facecolor='#E8F5E9', edgecolor='#388E3C', linewidth=3)
    ax.add_patch(core_rect)
    
    ax.text(7, 5.5, 'WRF-Hydro 水文模型核心', ha='center', va='center', 
           fontsize=14, fontweight='bold', color='#1B5E20')
    
    # 模型组件
    components = [
        ('Noah-MP\n地表模型', 4),
        ('地表\n径流计算', 6),
        ('地下\n水流计算', 8),
        ('Muskingum-Cunge\n河道汇流', 10),
    ]
    
    for name, x in components:
        rect = FancyBboxPatch((x-1, 3.8), 2, 1.2, boxstyle="round,pad=0.02",
                             facecolor='white', edgecolor='#4CAF50', linewidth=1.5)
        ax.add_patch(rect)
        ax.text(x, 4.4, name, ha='center', va='center', fontsize=9)
    
    # 输出产品层
    outputs = [
        ('分析同化\n(实时状态)', 2, 1.5),
        ('短期预报\n(0-18h)', 5, 1.5),
        ('中期预报\n(0-10d)', 8, 1.5),
        ('长期预报\n(0-30d)', 11, 1.5),
    ]
    
    for name, x, y in outputs:
        # 从核心到输出的箭头
        ax.annotate('', xy=(x, 2.2), xytext=(x, 3.4),
                   arrowprops=dict(arrowstyle='->', lw=2, color='#388E3C'))
        
        rect = FancyBboxPatch((x-1, y-0.5), 2, 1, boxstyle="round,pad=0.02",
                             facecolor='#FFF3E0', edgecolor='#F57C00', linewidth=2)
        ax.add_patch(rect)
        ax.text(x, y, name, ha='center', va='center', fontsize=9)
    
    # 覆盖范围标注
    ax.text(1, 0.5, '覆盖范围: 270万+河道断面', ha='left', va='center', 
           fontsize=10, color='#666666')
    ax.text(1, 0.2, '空间分辨率: 250m-1km', ha='left', va='center', 
           fontsize=10, color='#666666')
    
    ax.set_xlim(0, 14)
    ax.set_ylim(-0.5, 10)
    ax.axis('off')
    
    save_fig(fig, 'fig_4_2_nwm_architecture.png')

# ============ 图4: 工程师分级能力雷达图 ============
def create_engineer_levels():
    """创建工程师分级能力图"""
    fig, ax = plt.subplots(figsize=(12, 8))
    
    levels = ['L1入门', 'L2初级', 'L3中级', 'L4高级']
    skills = ['建模能力', '数据能力', '编程能力', '分析能力', '沟通能力']
    
    # 各等级能力值
    data = {
        'L1入门': [2, 2, 1, 1, 1],
        'L2初级': [3, 3, 2, 2, 2],
        'L3中级': [4, 4, 3, 3, 3],
        'L4高级': [5, 5, 4, 4, 4],
    }
    
    colors = ['#9E9E9E', '#FFC107', '#2196F3', '#4CAF50']
    
    x = np.arange(len(skills))
    width = 0.2
    
    for i, (level, values) in enumerate(data.items()):
        offset = (i - 1.5) * width
        bars = ax.bar(x + offset, values, width, label=level, color=colors[i])
    
    ax.set_ylabel('能力等级', fontsize=12)
    ax.set_title('水力工程师分级能力要求', fontsize=16, fontweight='bold')
    ax.set_xticks(x)
    ax.set_xticklabels(skills)
    ax.legend()
    ax.set_ylim(0, 6)
    ax.grid(axis='y', alpha=0.3)
    
    save_fig(fig, 'fig_4_3_engineer_levels.png')

# ============ 图5: AI赋能场景图 ============
def create_ai_empowerment():
    """创建AI赋能各角色场景图"""
    fig, ax = plt.subplots(figsize=(14, 10))
    
    # 中心AI
    center = Circle((7, 5), 1.5, facecolor='#9C27B0', edgecolor='black', linewidth=3)
    ax.add_patch(center)
    ax.text(7, 5, 'AI\n赋能', ha='center', va='center', fontsize=14, fontweight='bold', color='white')
    
    # 各角色及AI应用场景
    scenarios = [
        {'role': '项目经理', 'scenarios': ['智能计划', '风险预测', '自动报告'], 'angle': 90, 'color': '#F44336'},
        {'role': '架构师', 'scenarios': ['方案比选', '智能审查', '知识检索'], 'angle': 30, 'color': '#FF9800'},
        {'role': '水力工程师', 'scenarios': ['代码生成', '错误诊断', '结果解读'], 'angle': -30, 'color': '#2196F3'},
        {'role': '数据分析师', 'scenarios': ['智能清洗', '异常检测', '自动可视化'], 'angle': -90, 'color': '#4CAF50'},
        {'role': 'AI工程师', 'scenarios': ['模型开发', '工具集成', '技术探索'], 'angle': -150, 'color': '#9C27B0'},
    ]
    
    for scenario in scenarios:
        angle_rad = np.deg2rad(scenario['angle'])
        x = 7 + 4.5 * np.cos(angle_rad)
        y = 5 + 4.5 * np.sin(angle_rad)
        
        # 连线
        ax.plot([7 + 1.5*np.cos(angle_rad), x - 1.2*np.cos(angle_rad)], 
               [5 + 1.5*np.sin(angle_rad), y - 1.2*np.sin(angle_rad)], 
               'k-', linewidth=2, alpha=0.3)
        
        # 角色框
        rect = FancyBboxPatch((x-1.3, y-0.4), 2.6, 0.8, boxstyle="round,pad=0.02",
                             facecolor=scenario['color'], edgecolor='black', linewidth=2)
        ax.add_patch(rect)
        ax.text(x, y, scenario['role'], ha='center', va='center', 
               fontsize=11, fontweight='bold', color='white')
        
        # AI应用场景
        for i, app in enumerate(scenario['scenarios']):
            offset_y = 0.8 + i * 0.5
            ax.text(x, y + offset_y, f"• {app}", ha='center', va='center', 
                   fontsize=9, color=scenario['color'])
    
    ax.set_xlim(0, 14)
    ax.set_ylim(0, 10)
    ax.axis('off')
    ax.set_title('AI赋能五角色应用场景', fontsize=18, fontweight='bold', pad=20)
    
    save_fig(fig, 'fig_4_6_ai_empowerment.png')

# ============ 图6: 架构师工作全周期图 ============
def create_architect_lifecycle():
    """创建架构师项目全周期参与图"""
    fig, ax = plt.subplots(figsize=(16, 6))
    
    phases = [
        ('项目启动', '需求分析\n技术路线', '#E3F2FD'),
        ('方案设计', '架构设计\n技术选型', '#BBDEFB'),
        ('模型构建', '技术指导\n难题攻关', '#90CAF9'),
        ('验证校准', '方案审核\n质量把关', '#64B5F6'),
        ('成果交付', '最终审查\n技术签字', '#42A5F5'),
        ('运维支持', '问题处理\n优化建议', '#2196F3'),
    ]
    
    for i, (phase, work, color) in enumerate(phases):
        x = i * 2.5 + 1.5
        
        # 阶段框
        rect = FancyBboxPatch((x-1, 2), 2, 1.5, boxstyle="round,pad=0.02",
                             facecolor=color, edgecolor='black', linewidth=2)
        ax.add_patch(rect)
        ax.text(x, 2.75, phase, ha='center', va='center', fontsize=11, fontweight='bold')
        
        # 工作内容
        ax.text(x, 1.2, work, ha='center', va='center', fontsize=9, 
               color='#333333', linespacing=0.9)
        
        # 箭头
        if i < len(phases) - 1:
            ax.annotate('', xy=(x + 1.5, 2.75), xytext=(x + 1, 2.75),
                       arrowprops=dict(arrowstyle='->', lw=2.5, color='#333333'))
    
    ax.set_xlim(0, 16)
    ax.set_ylim(0, 4.5)
    ax.axis('off')
    ax.set_title('架构师项目全周期参与', fontsize=18, fontweight='bold', pad=20)
    
    save_fig(fig, 'fig_4_2_architect_lifecycle.png')

# ============ 主函数 ============
def main():
    print("开始生成第4章配图...")
    print(f"输出目录: {output_dir}")
    
    create_five_roles_collaboration()
    create_hydraulic_architecture()
    create_nwm_architecture()
    create_engineer_levels()
    create_ai_empowerment()
    create_architect_lifecycle()
    
    print("\n所有配图生成完成!")

if __name__ == '__main__':
    main()

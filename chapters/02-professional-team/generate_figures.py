#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
第2章配图生成脚本
生成水力模型专业团队章节所需的专业配图
"""

import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
from matplotlib.patches import FancyBboxPatch, Circle, FancyArrowPatch, Wedge
import numpy as np
import os

# 设置中文字体
plt.rcParams['font.sans-serif'] = ['DejaVu Sans', 'SimHei', 'Arial Unicode MS']
plt.rcParams['axes.unicode_minus'] = False

# 创建输出目录
output_dir = "/root/.openclaw/workspace/HEBook/chapters/02-professional-team/images"
os.makedirs(output_dir, exist_ok=True)

def save_fig(fig, filename):
    """保存图片"""
    filepath = os.path.join(output_dir, filename)
    fig.savefig(filepath, dpi=150, bbox_inches='tight', facecolor='white')
    print(f"Saved: {filepath}")
    plt.close(fig)

# ============ 图1: L1-L5级别阶梯图 ============
def create_level_stairs():
    """创建L1-L5级别阶梯图"""
    fig, ax = plt.subplots(figsize=(14, 8))
    
    levels = ['L1\nInitial', 'L2\nManaged', 'L3\nDefined', 'L4\nQuantitative', 'L5\nOptimizing']
    colors = ['#9E9E9E', '#FFC107', '#2196F3', '#4CAF50', '#9C27B0']
    chinese_names = ['初始级', '可重复级', '标准化级', '量化管理级', '领域优化级']
    features = ['Chaotic', 'Project\nMgmt', 'Standardized', 'Data-driven', 'Optimized']
    
    # 绘制阶梯
    for i, (level, color, name, feature) in enumerate(zip(levels, colors, chinese_names, features)):
        # 阶梯平台
        rect = FancyBboxPatch((i*2.5, i*1.2), 2.2, 1.0, 
                               boxstyle="round,pad=0.05", 
                               facecolor=color, edgecolor='black', linewidth=2)
        ax.add_patch(rect)
        
        # 级别标签
        ax.text(i*2.5 + 1.1, i*1.2 + 0.5, level, ha='center', va='center', 
                fontsize=11, fontweight='bold', color='white')
        
        # 中文名称
        ax.text(i*2.5 + 1.1, i*1.2 - 0.3, name, ha='center', va='top', 
                fontsize=12, fontweight='bold', color=color)
        
        # 特征描述
        ax.text(i*2.5 + 1.1, i*1.2 + 1.4, feature, ha='center', va='bottom', 
                fontsize=9, color='#666666')
        
        # 箭头（除了最后一个）
        if i < 4:
            ax.annotate('', xy=((i+1)*2.5 - 0.2, (i+1)*1.2 + 0.5), 
                       xytext=(i*2.5 + 2.4, i*1.2 + 0.5),
                       arrowprops=dict(arrowstyle='->', lw=2, color='#333333'))
    
    # 添加演进时间标注
    time_labels = ['Start', '6-12m', '12-18m', '18-24m', 'Continuous']
    for i, time_label in enumerate(time_labels):
        ax.text(i*2.5 + 1.1, -0.8, time_label, ha='center', va='top', 
                fontsize=9, color='#888888', style='italic')
    
    ax.set_xlim(-0.5, 12.5)
    ax.set_ylim(-1.5, 7)
    ax.set_aspect('equal')
    ax.axis('off')
    ax.set_title('Water Model Team Capability Maturity Levels (L1-L5)\n水力模型团队能力成熟度等级', 
                 fontsize=16, fontweight='bold', pad=20)
    
    save_fig(fig, 'fig_2_5_level_stairs.png')

# ============ 图2: 能力金字塔 ============
def create_capability_pyramid():
    """创建能力金字塔图"""
    fig, ax = plt.subplots(figsize=(10, 10))
    
    # 金字塔层级（从下到上）
    layers = [
        {'name': 'Soft Skills\n(Communication, Learning)', 'color': '#FFE082', 'width': 8, 'y': 0},
        {'name': 'Management\n(Project, Quality, Knowledge)', 'color': '#81C784', 'width': 6.5, 'y': 1.5},
        {'name': 'Data Capability\n(Collection, QC, GIS)', 'color': '#64B5F6', 'width': 5, 'y': 3},
        {'name': 'Tools Capability\n(Software, Programming, AI)', 'color': '#9575CD', 'width': 3.5, 'y': 4.5},
        {'name': 'Technical Capability\n(Hydraulics, Modeling, Analysis)', 'color': '#E57373', 'width': 2, 'y': 6},
    ]
    
    for layer in layers:
        width = layer['width']
        x_center = 4
        x_left = x_center - width/2
        
        # 绘制梯形
        if layer['y'] == 6:  # 顶层（三角形）
            triangle = plt.Polygon([[x_center-1, layer['y']], [x_center+1, layer['y']], 
                                   [x_center, layer['y']+1.2]], 
                                  facecolor=layer['color'], edgecolor='black', linewidth=2)
            ax.add_patch(triangle)
            ax.text(x_center, layer['y'] + 0.4, layer['name'], ha='center', va='center',
                   fontsize=9, fontweight='bold', wrap=True)
        else:
            height = 1.3
            rect = FancyBboxPatch((x_left, layer['y']), width, height,
                                 boxstyle="round,pad=0.02",
                                 facecolor=layer['color'], edgecolor='black', linewidth=2)
            ax.add_patch(rect)
            ax.text(x_center, layer['y'] + height/2, layer['name'], ha='center', va='center',
                   fontsize=9, fontweight='bold', wrap=True)
    
    ax.set_xlim(-0.5, 8.5)
    ax.set_ylim(-0.5, 8)
    ax.set_aspect('equal')
    ax.axis('off')
    ax.set_title('Professional Team Capability Pyramid\n专业团队核心能力金字塔', 
                 fontsize=16, fontweight='bold', pad=20)
    
    save_fig(fig, 'fig_2_1_3_capability_pyramid.png')

# ============ 图3: 五角色协作图 ============
def create_five_roles():
    """创建五角色协作图"""
    fig, ax = plt.subplots(figsize=(12, 10))
    
    # 五角星顶点位置
    angles = np.array([90, 18, -54, -126, -198]) * np.pi / 180
    radius = 3
    
    roles = [
        {'name': 'PM', 'full': 'Project Manager', 'color': '#F44336'},
        {'name': 'Architect', 'full': 'Modeling Architect', 'color': '#FF9800'},
        {'name': 'Modeler', 'full': 'Hydraulic Engineer', 'color': '#2196F3'},
        {'name': 'Data Analyst', 'full': 'Data Analyst', 'color': '#4CAF50'},
        {'name': 'AI Engineer', 'full': 'AI Engineer', 'color': '#9C27B0'},
    ]
    
    # 绘制连接线
    for i in range(5):
        for j in range(i+1, 5):
            x1, y1 = radius * np.cos(angles[i]), radius * np.sin(angles[i])
            x2, y2 = radius * np.cos(angles[j]), radius * np.sin(angles[j])
            ax.plot([x1, x2], [y1, y2], 'k-', linewidth=1, alpha=0.3)
    
    # 绘制角色节点
    for i, (role, angle) in enumerate(zip(roles, angles)):
        x, y = radius * np.cos(angle), radius * np.sin(angle)
        
        # 外圈
        circle = Circle((x, y), 0.8, facecolor=role['color'], edgecolor='black', linewidth=2)
        ax.add_patch(circle)
        
        # 角色名称
        ax.text(x, y, role['name'], ha='center', va='center', 
               fontsize=9, fontweight='bold', color='white')
        
        # 全称（外部）
        label_x = (radius + 1.3) * np.cos(angle)
        label_y = (radius + 1.3) * np.sin(angle)
        ax.text(label_x, label_y, role['full'], ha='center', va='center',
               fontsize=10, fontweight='bold', color=role['color'])
    
    # 中心成果
    center_circle = Circle((0, 0), 1.2, facecolor='#FFD700', edgecolor='black', linewidth=2)
    ax.add_patch(center_circle)
    ax.text(0, 0, 'Project\nDeliverables', ha='center', va='center', 
           fontsize=10, fontweight='bold')
    
    ax.set_xlim(-5, 5)
    ax.set_ylim(-4.5, 4.5)
    ax.set_aspect('equal')
    ax.axis('off')
    ax.set_title('Five-Role Team Collaboration Model\n五角色团队协作架构', 
                 fontsize=16, fontweight='bold', pad=20)
    
    save_fig(fig, 'fig_2_3_2_five_roles.png')

# ============ 图4: 五大业务板块 ============
def create_business_sectors():
    """创建五大业务板块环形图"""
    fig, ax = plt.subplots(figsize=(10, 10))
    
    sectors = ['Planning\n30%', 'Design\n25%', 'Assessment\n20%', 'Smart App\n15%', 'Consulting\n10%']
    sizes = [30, 25, 20, 15, 10]
    colors = ['#2196F3', '#4CAF50', '#FFC107', '#9C27B0', '#FF5722']
    
    # 环形图
    wedges, texts = ax.pie(sizes, colors=colors, startangle=90, 
                           wedgeprops=dict(width=0.4, edgecolor='white', linewidth=2))
    
    # 添加标签
    for i, (wedge, sector) in enumerate(zip(wedges, sectors)):
        angle = (wedge.theta2 - wedge.theta1)/2. + wedge.theta1
        x = 0.7 * np.cos(np.deg2rad(angle))
        y = 0.7 * np.sin(np.deg2rad(angle))
        ax.text(x, y, sector, ha='center', va='center', 
               fontsize=11, fontweight='bold', color='white')
    
    # 中心文字
    ax.text(0, 0, 'Water Model\nServices', ha='center', va='center',
           fontsize=14, fontweight='bold')
    
    ax.set_title('Core Business Scope\n核心业务范围分布', 
                 fontsize=16, fontweight='bold', pad=20)
    
    save_fig(fig, 'fig_2_4_1_business_sectors.png')

# ============ 图5: 七阶段流程图 ============
def create_seven_stages():
    """创建七阶段流程图"""
    fig, ax = plt.subplots(figsize=(16, 6))
    
    stages = [
        ('1', 'Requirements', '#E3F2FD'),
        ('2', 'Data Prep', '#BBDEFB'),
        ('3', 'Model Build', '#90CAF9'),
        ('4', 'Calibration', '#64B5F6'),
        ('5', 'Analysis', '#42A5F5'),
        ('6', 'Reporting', '#2196F3'),
        ('7', 'Delivery', '#1E88E5'),
    ]
    
    for i, (num, name, color) in enumerate(stages):
        x = i * 2
        # 节点
        circle = Circle((x, 0), 0.6, facecolor=color, edgecolor='black', linewidth=2)
        ax.add_patch(circle)
        ax.text(x, 0, num, ha='center', va='center', fontsize=14, fontweight='bold')
        
        # 名称
        ax.text(x, -1, name, ha='center', va='top', fontsize=10, fontweight='bold')
        
        # 箭头
        if i < 6:
            ax.annotate('', xy=(x + 1.3, 0), xytext=(x + 0.7, 0),
                       arrowprops=dict(arrowstyle='->', lw=2, color='#333333'))
    
    ax.set_xlim(-1, 13)
    ax.set_ylim(-2, 1.5)
    ax.set_aspect('equal')
    ax.axis('off')
    ax.set_title('Typical Project Workflow (7 Stages)\n典型项目全流程（七阶段）', 
                 fontsize=16, fontweight='bold', pad=20)
    
    save_fig(fig, 'fig_2_4_2_seven_stages.png')

# ============ 图6: 三种组织架构对比 ============
def create_org_structures():
    """创建三种组织架构对比图"""
    fig, axes = plt.subplots(1, 3, figsize=(15, 8))
    
    structures = [
        ('Functional\n(Function-based)', '#2196F3', [
            ['Director'],
            ['Modeling', 'Data', 'R&D'],
            ['E1', 'E2', 'E3']
        ]),
        ('Project-based\n(Project teams)', '#4CAF50', [
            ['Team A', 'Team B', 'Team C'],
            ['PM/Modeler/Data', 'PM/Modeler/Data', 'PM/Modeler/Data']
        ]),
        ('Matrix\n(Recommended)', '#9C27B0', [
            ['Function→'],
            ['Project↓', 'Modeling', 'Data', 'AI', 'QC'],
            ['P1', '✓', '✓', '✓', '✓'],
            ['P2', '✓', '✓', '✓', '✓'],
        ])
    ]
    
    for ax, (title, color, structure) in zip(axes, structures):
        ax.set_xlim(0, 10)
        ax.set_ylim(0, 10)
        
        # 标题
        ax.text(5, 9, title, ha='center', va='top', fontsize=12, fontweight='bold', color=color)
        
        # 简化的结构示意
        if 'Functional' in title:
            # 职能型
            y_pos = 7
            for row in structure:
                x_step = 10 / (len(row) + 1)
                for j, item in enumerate(row):
                    rect = FancyBboxPatch((x_step*(j+1)-0.8, y_pos-0.4), 1.6, 0.8,
                                         boxstyle="round,pad=0.02",
                                         facecolor=color, alpha=0.3, edgecolor=color)
                    ax.add_patch(rect)
                    ax.text(x_step*(j+1), y_pos, item, ha='center', va='center', fontsize=9)
                y_pos -= 2.5
        
        elif 'Project' in title:
            # 项目型
            x_pos = [2, 5, 8]
            for i, team in enumerate(structure[0]):
                rect = FancyBboxPatch((x_pos[i]-1, 6), 2, 1.2,
                                     boxstyle="round,pad=0.02",
                                     facecolor=color, alpha=0.3, edgecolor=color)
                ax.add_patch(rect)
                ax.text(x_pos[i], 6.6, team, ha='center', va='center', fontsize=9, fontweight='bold')
                ax.text(x_pos[i], 4, 'PM+Modeler\n+Data', ha='center', va='center', fontsize=8)
        
        else:
            # 矩阵型
            ax.text(5, 7.5, 'Matrix Structure', ha='center', va='center', fontsize=11, fontweight='bold')
            # 简化的矩阵示意
            for i in range(4):
                for j in range(4):
                    x, y = 2 + j*2, 5 - i*1.5
                    if i == 0 and j == 0:
                        text = '↓'
                    elif i == 0:
                        text = ['M', 'D', 'AI', 'QC'][j-1]
                    elif j == 0:
                        text = f'P{i}'
                    else:
                        text = '●'
                    ax.text(x, y, text, ha='center', va='center', fontsize=10)
        
        ax.axis('off')
    
    fig.suptitle('Organizational Structure Comparison\n三种组织架构对比', 
                 fontsize=16, fontweight='bold')
    save_fig(fig, 'fig_2_3_1_org_structures.png')

# ============ 图7: 专业vs临时团队对比 ============
def create_team_comparison():
    """创建专业vs临时团队对比图"""
    fig, ax = plt.subplots(figsize=(12, 8))
    
    categories = ['Rework\nRate', 'Client\nSatisfaction', 'On-time\nDelivery', 'Retention\nRate', 'Profit\nMargin']
    professional = [10, 4.2, 90, 85, 30]
    temporary = [40, 3.3, 65, 55, 10]
    
    x = np.arange(len(categories))
    width = 0.35
    
    bars1 = ax.bar(x - width/2, professional, width, label='Professional Team', color='#4CAF50')
    bars2 = ax.bar(x + width/2, temporary, width, label='Temporary Team', color='#F44336')
    
    ax.set_ylabel('Value / %', fontsize=12)
    ax.set_title('Professional vs Temporary Team Comparison\n专业团队 vs 临时项目组对比', 
                 fontsize=14, fontweight='bold')
    ax.set_xticks(x)
    ax.set_xticklabels(categories)
    ax.legend()
    
    # 添加数值标签
    for bar in bars1:
        height = bar.get_height()
        ax.annotate(f'{height}',
                    xy=(bar.get_x() + bar.get_width() / 2, height),
                    xytext=(0, 3), textcoords="offset points",
                    ha='center', va='bottom', fontsize=9)
    
    for bar in bars2:
        height = bar.get_height()
        ax.annotate(f'{height}',
                    xy=(bar.get_x() + bar.get_width() / 2, height),
                    xytext=(0, 3), textcoords="offset points",
                    ha='center', va='bottom', fontsize=9)
    
    save_fig(fig, 'fig_2_1_1_team_comparison.png')

# ============ 图8: 跨部门协作网络 ============
def create_collaboration_network():
    """创建跨部门协作网络图"""
    fig, ax = plt.subplots(figsize=(12, 10))
    
    # 中心团队
    center = Circle((0, 0), 1.2, facecolor='#2196F3', edgecolor='black', linewidth=2)
    ax.add_patch(center)
    ax.text(0, 0, 'Water Model\nTeam', ha='center', va='center', 
           fontsize=10, fontweight='bold', color='white')
    
    # 周围部门
    departments = [
        ('Planning', 0, 4),
        ('Design', 3.5, 2),
        ('Operations', 3.5, -2),
        ('Government', 0, -4),
        ('External\nExperts', -3.5, -2),
        ('Data\nProviders', -3.5, 2),
    ]
    
    colors = ['#4CAF50', '#FFC107', '#FF5722', '#9C27B0', '#795548', '#607D8B']
    
    for (name, x, y), color in zip(departments, colors):
        # 部门节点
        circle = Circle((x, y), 0.9, facecolor=color, edgecolor='black', linewidth=2)
        ax.add_patch(circle)
        ax.text(x, y, name, ha='center', va='center', 
               fontsize=9, fontweight='bold', color='white')
        
        # 连接线
        ax.plot([0, x*0.7], [0, y*0.7], 'k-', linewidth=1.5, alpha=0.4)
    
    ax.set_xlim(-5, 5)
    ax.set_ylim(-5.5, 5.5)
    ax.set_aspect('equal')
    ax.axis('off')
    ax.set_title('Cross-Department Collaboration Network\n跨部门协作网络', 
                 fontsize=16, fontweight='bold', pad=20)
    
    save_fig(fig, 'fig_2_4_3_collaboration_network.png')

# ============ 主函数 ============
def main():
    print("开始生成第2章配图...")
    print(f"输出目录: {output_dir}")
    
    create_level_stairs()
    create_capability_pyramid()
    create_five_roles()
    create_business_sectors()
    create_seven_stages()
    create_org_structures()
    create_team_comparison()
    create_collaboration_network()
    
    print("\n所有配图生成完成!")

if __name__ == '__main__':
    main()

#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
第2章配图生成脚本 - 中文版
生成水力模型专业团队章节所需的专业配图
"""

import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
from matplotlib.patches import FancyBboxPatch, Circle, Wedge
import numpy as np
import os

# 设置中文字体 - 使用系统已安装的Noto Sans CJK
plt.rcParams['font.family'] = ['Noto Sans CJK JP', 'DejaVu Sans']
plt.rcParams['axes.unicode_minus'] = False

# 创建输出目录
output_dir = "/root/.openclaw/workspace/HEBook/chapters/02-professional-team/images"
os.makedirs(output_dir, exist_ok=True)

def save_fig(fig, filename):
    """保存图片"""
    filepath = os.path.join(output_dir, filename)
    fig.savefig(filepath, dpi=150, bbox_inches='tight', facecolor='white')
    print(f"已保存: {filepath}")
    plt.close(fig)

# ============ 图1: L1-L5级别阶梯图 ============
def create_level_stairs():
    """创建L1-L5级别阶梯图"""
    fig, ax = plt.subplots(figsize=(14, 9))
    
    levels = ['L1', 'L2', 'L3', 'L4', 'L5']
    chinese_names = ['初始级', '可重复级', '标准化级', '量化管理级', '领域优化级']
    english_names = ['Initial', 'Managed', 'Defined', 'Quantitative', 'Optimizing']
    colors = ['#9E9E9E', '#FFC107', '#2196F3', '#4CAF50', '#9C27B0']
    features = ['无序状态', '项目管理\n规范化', '组织级\n标准化', '数据驱动\n管理', '持续优化\n行业引领']
    
    # 绘制阶梯
    for i, (level, color, cname, ename, feature) in enumerate(zip(levels, colors, chinese_names, english_names, features)):
        # 阶梯平台
        rect = FancyBboxPatch((i*2.5, i*1.3), 2.2, 1.2, 
                               boxstyle="round,pad=0.05", 
                               facecolor=color, edgecolor='black', linewidth=2)
        ax.add_patch(rect)
        
        # 级别标签 (英文+中文)
        ax.text(i*2.5 + 1.1, i*1.3 + 0.75, f"{level}\n{cname}", ha='center', va='center', 
                fontsize=11, fontweight='bold', color='white', linespacing=0.9)
        
        # 特征描述
        ax.text(i*2.5 + 1.1, i*1.3 + 1.7, feature, ha='center', va='bottom', 
                fontsize=10, color='#333333', fontweight='bold')
        
        # 箭头（除了最后一个）
        if i < 4:
            ax.annotate('', xy=((i+1)*2.5 - 0.2, (i+1)*1.3 + 0.6), 
                       xytext=(i*2.5 + 2.4, i*1.3 + 0.6),
                       arrowprops=dict(arrowstyle='->', lw=2.5, color='#333333'))
    
    # 添加演进时间标注
    time_labels = ['起点', '6-12月', '12-18月', '18-24月', '持续优化']
    for i, time_label in enumerate(time_labels):
        ax.text(i*2.5 + 1.1, -0.9, time_label, ha='center', va='top', 
                fontsize=10, color='#666666')
    
    ax.set_xlim(-0.5, 12.5)
    ax.set_ylim(-1.5, 8)
    ax.set_aspect('equal')
    ax.axis('off')
    ax.set_title('水力模型团队能力成熟度等级（L1-L5）', 
                 fontsize=18, fontweight='bold', pad=25)
    
    save_fig(fig, 'fig_2_5_level_stairs.png')

# ============ 图2: 能力金字塔 ============
def create_capability_pyramid():
    """创建能力金字塔图"""
    fig, ax = plt.subplots(figsize=(11, 11))
    
    # 金字塔层级（从下到上）
    layers = [
        {'name': '软技能\n沟通表达、学习创新', 'color': '#FFE082', 'width': 8, 'y': 0},
        {'name': '管理能力\n项目管理、质量管理、知识管理', 'color': '#81C784', 'width': 6.5, 'y': 1.6},
        {'name': '数据能力\n数据采集、质量控制、GIS分析', 'color': '#64B5F6', 'width': 5, 'y': 3.2},
        {'name': '工具能力\n建模软件、编程开发、AI应用', 'color': '#9575CD', 'width': 3.5, 'y': 4.8},
        {'name': '技术能力\n水力学/水文学、模型构建与校准', 'color': '#E57373', 'width': 2, 'y': 6.4},
    ]
    
    for layer in layers:
        width = layer['width']
        x_center = 4
        x_left = x_center - width/2
        
        # 绘制梯形
        if layer['y'] == 6.4:  # 顶层（三角形）
            triangle = plt.Polygon([[x_center-1, layer['y']], [x_center+1, layer['y']], 
                                   [x_center, layer['y']+1.4]], 
                                  facecolor=layer['color'], edgecolor='black', linewidth=2)
            ax.add_patch(triangle)
            ax.text(x_center, layer['y'] + 0.5, layer['name'], ha='center', va='center',
                   fontsize=10, fontweight='bold', linespacing=0.9)
        else:
            height = 1.4
            rect = FancyBboxPatch((x_left, layer['y']), width, height,
                                 boxstyle="round,pad=0.02",
                                 facecolor=layer['color'], edgecolor='black', linewidth=2)
            ax.add_patch(rect)
            ax.text(x_center, layer['y'] + height/2, layer['name'], ha='center', va='center',
                   fontsize=10, fontweight='bold', linespacing=0.9)
    
    ax.set_xlim(-0.5, 8.5)
    ax.set_ylim(-0.5, 8.5)
    ax.set_aspect('equal')
    ax.axis('off')
    ax.set_title('专业团队核心能力金字塔', 
                 fontsize=18, fontweight='bold', pad=25)
    
    save_fig(fig, 'fig_2_1_3_capability_pyramid.png')

# ============ 图3: 五角色协作图 ============
def create_five_roles():
    """创建五角色协作图"""
    fig, ax = plt.subplots(figsize=(13, 11))
    
    # 五角星顶点位置
    angles = np.array([90, 18, -54, -126, -198]) * np.pi / 180
    radius = 3
    
    roles = [
        {'name': '项目经理\nPM', 'color': '#F44336', 'subtitle': '项目成功第一责任人'},
        {'name': '架构师\nArchitect', 'color': '#FF9800', 'subtitle': '技术方向把控'},
        {'name': '水力工程师\nModeler', 'color': '#2196F3', 'subtitle': '模型构建执行'},
        {'name': '数据分析师\nData Analyst', 'color': '#4CAF50', 'subtitle': '数据质量守护'},
        {'name': 'AI工程师\nAI Engineer', 'color': '#9C27B0', 'subtitle': '智能技术赋能'},
    ]
    
    # 绘制连接线
    for i in range(5):
        for j in range(i+1, 5):
            x1, y1 = radius * np.cos(angles[i]), radius * np.sin(angles[i])
            x2, y2 = radius * np.cos(angles[j]), radius * np.sin(angles[j])
            ax.plot([x1, x2], [y1, y2], 'k-', linewidth=1.5, alpha=0.3)
    
    # 绘制角色节点
    for i, (role, angle) in enumerate(zip(roles, angles)):
        x, y = radius * np.cos(angle), radius * np.sin(angle)
        
        # 外圈
        circle = Circle((x, y), 0.9, facecolor=role['color'], edgecolor='black', linewidth=2)
        ax.add_patch(circle)
        
        # 角色名称
        ax.text(x, y, role['name'], ha='center', va='center', 
               fontsize=9, fontweight='bold', color='white', linespacing=0.8)
        
        # 副标题（外部）
        label_x = (radius + 1.4) * np.cos(angle)
        label_y = (radius + 1.4) * np.sin(angle)
        ax.text(label_x, label_y, role['subtitle'], ha='center', va='center',
               fontsize=10, fontweight='bold', color=role['color'])
    
    # 中心成果
    center_circle = Circle((0, 0), 1.3, facecolor='#FFD700', edgecolor='black', linewidth=2)
    ax.add_patch(center_circle)
    ax.text(0, 0, '项目成果\n高质量交付', ha='center', va='center', 
           fontsize=11, fontweight='bold')
    
    ax.set_xlim(-5.5, 5.5)
    ax.set_ylim(-5, 5)
    ax.set_aspect('equal')
    ax.axis('off')
    ax.set_title('五角色团队协作架构', 
                 fontsize=18, fontweight='bold', pad=25)
    
    save_fig(fig, 'fig_2_3_2_five_roles.png')

# ============ 图4: 五大业务板块 ============
def create_business_sectors():
    """创建五大业务板块环形图"""
    fig, ax = plt.subplots(figsize=(11, 11))
    
    sectors = ['排水规划\n30%', '工程设计\n25%', '评估诊断\n20%', '智慧应用\n15%', '咨询服务\n10%']
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
               fontsize=11, fontweight='bold', color='white', linespacing=0.9)
    
    # 中心文字
    ax.text(0, 0, '水力模型\n专业服务', ha='center', va='center',
           fontsize=14, fontweight='bold')
    
    ax.set_title('核心业务范围分布', 
                 fontsize=18, fontweight='bold', pad=25)
    
    save_fig(fig, 'fig_2_4_1_business_sectors.png')

# ============ 图5: 七阶段流程图 ============
def create_seven_stages():
    """创建七阶段流程图"""
    fig, ax = plt.subplots(figsize=(17, 7))
    
    stages = [
        ('1', '需求分析', '1-2周', '#E3F2FD'),
        ('2', '数据准备', '2-6周', '#BBDEFB'),
        ('3', '模型构建', '2-4周', '#90CAF9'),
        ('4', '验证校准', '2-4周', '#64B5F6'),
        ('5', '情景分析', '2-6周', '#42A5F5'),
        ('6', '报告编制', '2-4周', '#2196F3'),
        ('7', '交付验收', '1-2周', '#1E88E5'),
    ]
    
    for i, (num, name, duration, color) in enumerate(stages):
        x = i * 2.2
        # 节点
        circle = Circle((x, 0), 0.7, facecolor=color, edgecolor='black', linewidth=2)
        ax.add_patch(circle)
        ax.text(x, 0, num, ha='center', va='center', fontsize=16, fontweight='bold')
        
        # 阶段名称
        ax.text(x, -1.2, name, ha='center', va='top', fontsize=11, fontweight='bold')
        
        # 时长
        ax.text(x, 1.2, duration, ha='center', va='bottom', fontsize=10, color='#666666')
        
        # 箭头
        if i < 6:
            ax.annotate('', xy=(x + 1.4, 0), xytext=(x + 0.9, 0),
                       arrowprops=dict(arrowstyle='->', lw=2.5, color='#333333'))
    
    ax.set_xlim(-1.5, 14.5)
    ax.set_ylim(-2.5, 2)
    ax.set_aspect('equal')
    ax.axis('off')
    ax.set_title('典型项目全流程（七阶段）', 
                 fontsize=18, fontweight='bold', pad=25)
    
    save_fig(fig, 'fig_2_4_2_seven_stages.png')

# ============ 图6: 三种组织架构对比 ============
def create_org_structures():
    """创建三种组织架构对比图"""
    fig, axes = plt.subplots(1, 3, figsize=(16, 9))
    
    structures = [
        ('职能型组织架构\n（按专业划分）', '#2196F3', [
            ['技术总监'],
            ['建模组', '数据组', '研发组'],
            ['工程师', '分析师', '开发员']
        ]),
        ('项目型组织架构\n（按项目划分）', '#4CAF50', [
            ['项目A团队', '项目B团队', '项目C团队'],
            ['项目经理\n工程师\n数据员', '项目经理\n工程师\n数据员', '项目经理\n工程师\n数据员']
        ]),
        ('矩阵型组织架构\n（推荐）', '#9C27B0', [
            ['项目1', '●', '●', '●', '●'],
            ['项目2', '●', '●', '●', '●'],
            ['项目3', '●', '●', '●', '●'],
        ])
    ]
    
    for ax, (title, color, structure) in zip(axes, structures):
        ax.set_xlim(0, 10)
        ax.set_ylim(0, 10)
        
        # 标题
        ax.text(5, 9.2, title, ha='center', va='top', fontsize=13, fontweight='bold', color=color)
        
        if '职能型' in title:
            # 职能型 - 树状结构
            y_positions = [7, 4.5, 2]
            for row_idx, row in enumerate(structure):
                y = y_positions[row_idx]
                x_step = 10 / (len(row) + 1)
                for j, item in enumerate(row):
                    x = x_step * (j + 1)
                    width = 2.2 if row_idx == 0 else 2
                    rect = FancyBboxPatch((x - width/2, y - 0.5), width, 1,
                                         boxstyle="round,pad=0.02",
                                         facecolor=color, alpha=0.3, edgecolor=color, linewidth=2)
                    ax.add_patch(rect)
                    ax.text(x, y, item, ha='center', va='center', fontsize=10, fontweight='bold')
                    # 连接线
                    if row_idx < 2:
                        ax.plot([x, x], [y - 0.5, y_positions[row_idx+1] + 0.5], 
                               color=color, linewidth=1.5, alpha=0.5)
        
        elif '项目型' in title:
            # 项目型 - 并列方块
            x_positions = [1.8, 5, 8.2]
            for i, (team, members) in enumerate(zip(structure[0], structure[1])):
                x = x_positions[i]
                rect = FancyBboxPatch((x - 1.3, 4), 2.6, 3,
                                     boxstyle="round,pad=0.02",
                                     facecolor=color, alpha=0.3, edgecolor=color, linewidth=2)
                ax.add_patch(rect)
                ax.text(x, 6.2, team, ha='center', va='center', fontsize=10, fontweight='bold')
                ax.text(x, 4.8, members.replace('+', '\n'), ha='center', va='center', fontsize=9)
        
        else:
            # 矩阵型
            ax.text(5, 8, '矩阵型结构', ha='center', va='center', fontsize=12, fontweight='bold', color=color)
            # 表头
            headers = ['项目\\职能', '建模', '数据', 'AI', '质控']
            for j, h in enumerate(headers):
                x = 1.5 + j * 1.7
                rect = FancyBboxPatch((x - 0.7, 6), 1.4, 0.8,
                                     boxstyle="round,pad=0.02",
                                     facecolor=color, alpha=0.5, edgecolor=color)
                ax.add_patch(rect)
                ax.text(x, 6.4, h, ha='center', va='center', fontsize=9, fontweight='bold')
            
            # 矩阵内容
            for i, row in enumerate(structure):
                y = 4.8 - i * 1.2
                for j, cell in enumerate(row):
                    x = 1.5 + j * 1.7
                    if j == 0:
                        rect = FancyBboxPatch((x - 0.7, y - 0.4), 1.4, 0.8,
                                             boxstyle="round,pad=0.02",
                                             facecolor='#E0E0E0', edgecolor='gray')
                        ax.add_patch(rect)
                    ax.text(x, y, cell, ha='center', va='center', fontsize=10, fontweight='bold' if j==0 else 'normal')
        
        ax.axis('off')
    
    fig.suptitle('三种组织架构对比', fontsize=18, fontweight='bold', y=0.98)
    save_fig(fig, 'fig_2_3_1_org_structures.png')

# ============ 图7: 专业vs临时团队对比 ============
def create_team_comparison():
    """创建专业vs临时团队对比图"""
    fig, ax = plt.subplots(figsize=(13, 8))
    
    categories = ['模型返工率', '客户满意度', '准时交付率', '员工留存率', '项目利润率']
    professional = [10, 4.2, 90, 85, 30]
    temporary = [40, 3.3, 65, 55, 10]
    
    x = np.arange(len(categories))
    width = 0.35
    
    bars1 = ax.bar(x - width/2, professional, width, label='专业团队', color='#4CAF50')
    bars2 = ax.bar(x + width/2, temporary, width, label='临时项目组', color='#F44336')
    
    ax.set_ylabel('数值 / %', fontsize=13)
    ax.set_title('专业团队 vs 临时项目组对比', fontsize=18, fontweight='bold', pad=20)
    ax.set_xticks(x)
    ax.set_xticklabels(categories, fontsize=11)
    ax.legend(fontsize=12)
    ax.set_ylim(0, 100)
    
    # 添加数值标签
    for bar in bars1:
        height = bar.get_height()
        ax.annotate(f'{height}',
                    xy=(bar.get_x() + bar.get_width() / 2, height),
                    xytext=(0, 3), textcoords="offset points",
                    ha='center', va='bottom', fontsize=10, fontweight='bold')
    
    for bar in bars2:
        height = bar.get_height()
        ax.annotate(f'{height}',
                    xy=(bar.get_x() + bar.get_width() / 2, height),
                    xytext=(0, 3), textcoords="offset points",
                    ha='center', va='bottom', fontsize=10, fontweight='bold')
    
    ax.grid(axis='y', alpha=0.3)
    save_fig(fig, 'fig_2_1_1_team_comparison.png')

# ============ 图8: 跨部门协作网络 ============
def create_collaboration_network():
    """创建跨部门协作网络图"""
    fig, ax = plt.subplots(figsize=(13, 11))
    
    # 中心团队
    center = Circle((0, 0), 1.3, facecolor='#2196F3', edgecolor='black', linewidth=2)
    ax.add_patch(center)
    ax.text(0, 0, '水力模型\n专业团队', ha='center', va='center', 
           fontsize=11, fontweight='bold', color='white', linespacing=0.9)
    
    # 周围部门
    departments = [
        ('规划部门', 0, 4.5),
        ('设计部门', 4, 2),
        ('运维部门', 4, -2),
        ('政府部门', 0, -4.5),
        ('外部专家', -4, -2),
        ('数据供应商', -4, 2),
    ]
    
    colors = ['#4CAF50', '#FFC107', '#FF5722', '#9C27B0', '#795548', '#607D8B']
    
    for (name, x, y), color in zip(departments, colors):
        # 部门节点
        circle = Circle((x, y), 1, facecolor=color, edgecolor='black', linewidth=2)
        ax.add_patch(circle)
        ax.text(x, y, name, ha='center', va='center', 
               fontsize=10, fontweight='bold', color='white')
        
        # 连接线
        ax.plot([0, x*0.75], [0, y*0.75], 'k-', linewidth=2, alpha=0.3)
    
    ax.set_xlim(-5.5, 5.5)
    ax.set_ylim(-6, 6)
    ax.set_aspect('equal')
    ax.axis('off')
    ax.set_title('跨部门协作网络', 
                 fontsize=18, fontweight='bold', pad=25)
    
    save_fig(fig, 'fig_2_4_3_collaboration_network.png')

# ============ 主函数 ============
def main():
    print("开始生成第2章配图（中文版）...")
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

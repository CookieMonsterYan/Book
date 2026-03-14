#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
第3章配图生成脚本
生成水力模型专业团队建设章节所需的专业配图
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
output_dir = "/root/.openclaw/workspace/HEBook/chapters/03-team-building/images"
os.makedirs(output_dir, exist_ok=True)

def save_fig(fig, filename):
    """保存图片"""
    filepath = os.path.join(output_dir, filename)
    fig.savefig(filepath, dpi=150, bbox_inches='tight', facecolor='white')
    print(f"已保存: {filepath}")
    plt.close(fig)

# ============ 图1: L1-L5跃迁路径图 ============
def create_l1_l5_journey():
    """创建L1-L5跃迁路径图"""
    fig, ax = plt.subplots(figsize=(14, 10))
    
    # 跃迁阶段
    transitions = [
        {'from': 'L1\n初始级', 'to': 'L2\n可重复级', 'action': '建立项目管理基础', 'time': '6-12月', 'y': 8},
        {'from': 'L2\n可重复级', 'to': 'L3\n标准化级', 'action': '建立组织级标准', 'time': '12-18月', 'y': 6},
        {'from': 'L3\n标准化级', 'to': 'L4\n量化管理级', 'action': '建立量化管理', 'time': '18-24月', 'y': 4},
        {'from': 'L4\n量化管理级', 'to': 'L5\n领域优化级', 'action': '建立持续优化', 'time': '持续', 'y': 2},
    ]
    
    colors = ['#9E9E9E', '#FFC107', '#2196F3', '#4CAF50', '#9C27B0']
    
    # 绘制等级节点和跃迁箭头
    for i, trans in enumerate(transitions):
        from_color = colors[i]
        to_color = colors[i+1]
        y = trans['y']
        
        # 起点
        circle1 = Circle((2, y), 0.8, facecolor=from_color, edgecolor='black', linewidth=2)
        ax.add_patch(circle1)
        ax.text(2, y, trans['from'], ha='center', va='center', fontsize=10, fontweight='bold', color='white')
        
        # 跃迁箭头
        ax.annotate('', xy=(8, y), xytext=(3, y),
                   arrowprops=dict(arrowstyle='->', lw=3, color='#333333'))
        
        # 跃迁动作框
        rect = FancyBboxPatch((4, y-0.5), 3, 1, boxstyle="round,pad=0.05",
                             facecolor='#E3F2FD', edgecolor='#2196F3', linewidth=2)
        ax.add_patch(rect)
        ax.text(5.5, y, trans['action'], ha='center', va='center', fontsize=11, fontweight='bold')
        
        # 时间标注
        ax.text(5.5, y-0.8, trans['time'], ha='center', va='top', fontsize=9, color='#666666')
        
        # 终点
        circle2 = Circle((9, y), 0.8, facecolor=to_color, edgecolor='black', linewidth=2)
        ax.add_patch(circle2)
        ax.text(9, y, trans['to'], ha='center', va='center', fontsize=10, fontweight='bold', color='white')
    
    ax.set_xlim(0, 11)
    ax.set_ylim(0, 10)
    ax.set_aspect('equal')
    ax.axis('off')
    ax.set_title('团队能力跃迁路径（L1-L5）', fontsize=18, fontweight='bold', pad=20)
    
    save_fig(fig, 'fig_3_2_journey.png')

# ============ 图2: T型人才模型 ============
def create_talent_model():
    """创建T型人才模型图"""
    fig, ax = plt.subplots(figsize=(10, 10))
    
    # T型结构
    # 横线（广度）
    rect_h = FancyBboxPatch((1, 4), 8, 1.5, boxstyle="round,pad=0.05",
                            facecolor='#64B5F6', edgecolor='black', linewidth=2)
    ax.add_patch(rect_h)
    ax.text(5, 4.75, '横向广度：数据·编程·AI·管理', ha='center', va='center', 
           fontsize=12, fontweight='bold', color='white')
    
    # 竖线（深度）
    rect_v = FancyBboxPatch((4, 0.5), 2, 4, boxstyle="round,pad=0.05",
                            facecolor='#E57373', edgecolor='black', linewidth=2)
    ax.add_patch(rect_v)
    ax.text(5, 2.5, '纵向深度\n水力建模\n专业能力', ha='center', va='center', 
           fontsize=11, fontweight='bold', color='white', linespacing=0.9)
    
    # 标注能力项
    skills_left = ['数据分析', '编程开发', 'AI应用']
    skills_right = ['项目管理', '团队协作', '沟通表达']
    
    for i, skill in enumerate(skills_left):
        ax.text(2.5, 5.5 + i*0.6, skill, ha='center', va='center', fontsize=10, color='#1976D2')
    
    for i, skill in enumerate(skills_right):
        ax.text(7.5, 5.5 + i*0.6, skill, ha='center', va='center', fontsize=10, color='#1976D2')
    
    # 深度能力项
    depth_skills = ['水力学', '水文学', '模型构建', '验证校准', '结果分析']
    for i, skill in enumerate(depth_skills):
        ax.text(2, 3.5 - i*0.7, skill, ha='right', va='center', fontsize=10, color='#C62828')
    
    ax.set_xlim(0, 10)
    ax.set_ylim(0, 8)
    ax.set_aspect('equal')
    ax.axis('off')
    ax.set_title('T型人才能力模型', fontsize=18, fontweight='bold', pad=20)
    
    save_fig(fig, 'fig_3_3_talent_model.png')

# ============ 图3: 培训体系架构图 ============
def create_training_system():
    """创建培训体系架构图"""
    fig, ax = plt.subplots(figsize=(14, 10))
    
    # 四个培训层级
    levels = [
        {'name': '新员工培训', 'subtitle': '入职培训', 'color': '#81C784', 'y': 7},
        {'name': '在岗培训', 'subtitle': '持续培训', 'color': '#64B5F6', 'y': 5},
        {'name': '专题培训', 'subtitle': '提升培训', 'color': '#FFB74D', 'y': 3},
        {'name': '外部培训', 'subtitle': '拓展培训', 'color': '#9575CD', 'y': 1},
    ]
    
    for level in levels:
        # 主框
        rect = FancyBboxPatch((1, level['y']-0.6), 4, 1.2, boxstyle="round,pad=0.05",
                             facecolor=level['color'], edgecolor='black', linewidth=2)
        ax.add_patch(rect)
        ax.text(3, level['y'], level['name'], ha='center', va='center', 
               fontsize=13, fontweight='bold')
        ax.text(3, level['y']-0.35, level['subtitle'], ha='center', va='center', 
               fontsize=10, color='#333333')
        
        # 箭头指向内容
        ax.annotate('', xy=(7, level['y']), xytext=(5.2, level['y']),
                   arrowprops=dict(arrowstyle='->', lw=2, color='#666666'))
    
    # 右侧内容
    contents = [
        ['公司文化', '基础水力学', '软件操作', '流程规范'],
        ['月度技术分享', '季度案例复盘', '导师制度', '项目实战'],
        ['Python进阶', 'AI工具应用', '高级建模技术', '量化分析方法'],
        ['软件厂商培训', '行业会议', '专业认证', '高校合作'],
    ]
    
    for i, content_list in enumerate(contents):
        y = levels[i]['y']
        for j, content in enumerate(content_list):
            x = 7.5 + j * 2.5
            if x < 13:
                rect = FancyBboxPatch((x-1, y-0.35), 2, 0.7, boxstyle="round,pad=0.02",
                                     facecolor='#F5F5F5', edgecolor='#999999', linewidth=1)
                ax.add_patch(rect)
                ax.text(x, y, content, ha='center', va='center', fontsize=9)
    
    ax.set_xlim(0, 14)
    ax.set_ylim(0, 9)
    ax.set_aspect('equal')
    ax.axis('off')
    ax.set_title('分层培训体系架构', fontsize=18, fontweight='bold', pad=20)
    
    save_fig(fig, 'fig_3_3_training_system.png')

# ============ 图4: PDCA循环图 ============
def create_pdca_cycle():
    """创建PDCA循环图"""
    fig, ax = plt.subplots(figsize=(10, 10))
    
    # 中心圆
    center_circle = Circle((0, 0), 1, facecolor='#ECEFF1', edgecolor='black', linewidth=2)
    ax.add_patch(center_circle)
    ax.text(0, 0, '持续\n改进', ha='center', va='center', fontsize=12, fontweight='bold')
    
    # 四个扇形
    phases = [
        {'name': 'Plan\n计划', 'color': '#2196F3', 'angle': 45},
        {'name': 'Do\n执行', 'color': '#4CAF50', 'angle': 135},
        {'name': 'Check\n检查', 'color': '#FFC107', 'angle': 225},
        {'name': 'Act\n行动', 'color': '#F44336', 'angle': 315},
    ]
    
    for phase in phases:
        angle_rad = np.deg2rad(phase['angle'])
        x = 2.5 * np.cos(angle_rad)
        y = 2.5 * np.sin(angle_rad)
        
        circle = Circle((x, y), 1.2, facecolor=phase['color'], edgecolor='black', linewidth=2)
        ax.add_patch(circle)
        ax.text(x, y, phase['name'], ha='center', va='center', 
               fontsize=11, fontweight='bold', color='white')
        
        # 箭头
        arrow_angle = angle_rad - np.pi/4
        ax.annotate('', 
                   xy=(2.5 * np.cos(arrow_angle), 2.5 * np.sin(arrow_angle)),
                   xytext=(1.8 * np.cos(arrow_angle), 1.8 * np.sin(arrow_angle)),
                   arrowprops=dict(arrowstyle='->', lw=2.5, color='#333333'))
    
    ax.set_xlim(-4.5, 4.5)
    ax.set_ylim(-4.5, 4.5)
    ax.set_aspect('equal')
    ax.axis('off')
    ax.set_title('PDCA持续改进循环', fontsize=18, fontweight='bold', pad=20)
    
    save_fig(fig, 'fig_3_5_pdca.png')

# ============ 图5: 知识管理流程图 ============
def create_km_flow():
    """创建知识管理流程图"""
    fig, ax = plt.subplots(figsize=(16, 6))
    
    steps = [
        ('知识获取', '#E3F2FD', '项目经验\n外部学习'),
        ('知识整理', '#BBDEFB', '分类编码\n去伪存真'),
        ('知识存储', '#90CAF9', '知识库\n文档库'),
        ('知识共享', '#64B5F6', '分享会\n培训'),
        ('知识应用', '#42A5F5', '项目复用\n问题解决'),
        ('知识更新', '#2196F3', '迭代优化\n淘汰过时'),
    ]
    
    for i, (name, color, subtitle) in enumerate(steps):
        x = i * 2.5
        # 主框
        rect = FancyBboxPatch((x-0.9, 0.5), 1.8, 1.5, boxstyle="round,pad=0.05",
                             facecolor=color, edgecolor='black', linewidth=2)
        ax.add_patch(rect)
        ax.text(x, 1.25, name, ha='center', va='center', fontsize=11, fontweight='bold')
        
        # 子标题
        ax.text(x, 2.2, subtitle, ha='center', va='center', fontsize=9, color='#555555')
        
        # 箭头
        if i < len(steps) - 1:
            ax.annotate('', xy=(x + 1.5, 1.25), xytext=(x + 1, 1.25),
                       arrowprops=dict(arrowstyle='->', lw=2, color='#333333'))
    
    # 返回箭头（循环）
    ax.annotate('', xy=(0, 0.3), xytext=(12.5, 0.3),
               arrowprops=dict(arrowstyle='->', lw=2, color='#666666', 
                              connectionstyle="arc3,rad=-0.3"))
    ax.text(6.25, -0.3, '循环迭代', ha='center', va='center', fontsize=10, color='#666666')
    
    ax.set_xlim(-1.5, 14)
    ax.set_ylim(-1, 3.5)
    ax.set_aspect('equal')
    ax.axis('off')
    ax.set_title('知识管理流程', fontsize=18, fontweight='bold', pad=20)
    
    save_fig(fig, 'fig_3_4_km_flow.png')

# ============ 图6: 角色能力矩阵图 ============
def create_capability_matrix():
    """创建角色能力矩阵图"""
    fig, ax = plt.subplots(figsize=(12, 8))
    
    roles = ['项目经理', '架构师', '水力工程师', '数据分析师', 'AI工程师']
    capabilities = ['水力建模', '项目管理', '数据分析', '编程开发', 'AI应用']
    
    # 能力要求等级 (1-5)
    matrix = [
        [2, 5, 2, 2, 2],  # 项目经理
        [5, 3, 3, 4, 3],  # 架构师
        [4, 2, 3, 3, 2],  # 水力工程师
        [2, 2, 5, 4, 3],  # 数据分析师
        [2, 2, 4, 5, 5],  # AI工程师
    ]
    
    colors = ['#FFCDD2', '#FFECB3', '#C8E6C9', '#BBDEFB', '#B39DDB']
    
    for i, role in enumerate(roles):
        for j, cap in enumerate(capabilities):
            value = matrix[i][j]
            color = colors[value - 1]
            
            rect = Rectangle((j, len(roles)-1-i), 1, 1, 
                            facecolor=color, edgecolor='white', linewidth=2)
            ax.add_patch(rect)
            ax.text(j + 0.5, len(roles)-1-i + 0.5, str(value), 
                   ha='center', va='center', fontsize=14, fontweight='bold')
    
    # 设置坐标轴
    ax.set_xlim(0, len(capabilities))
    ax.set_ylim(0, len(roles))
    ax.set_xticks([i + 0.5 for i in range(len(capabilities))])
    ax.set_xticklabels(capabilities, fontsize=11)
    ax.set_yticks([i + 0.5 for i in range(len(roles))])
    ax.set_yticklabels(list(reversed(roles)), fontsize=11)
    ax.set_aspect('equal')
    
    # 图例
    legend_elements = [mpatches.Patch(color=colors[i], label=f'等级{i+1}') for i in range(5)]
    ax.legend(handles=legend_elements, loc='upper center', bbox_to_anchor=(0.5, -0.08), ncol=5)
    
    ax.set_title('角色能力要求矩阵', fontsize=18, fontweight='bold', pad=20)
    
    save_fig(fig, 'fig_3_1_capability_matrix.png')

# ============ 图7: 团队文化演进图 ============
def create_culture_evolution():
    """创建团队文化演进图"""
    fig, ax = plt.subplots(figsize=(14, 8))
    
    levels = [
        {'level': 'L1-L2', 'name': '救火文化', 'desc': '被动应对，解决眼前问题', 'color': '#9E9E9E', 'y': 6},
        {'level': 'L3', 'name': '规范文化', 'desc': '按流程执行，标准化操作', 'color': '#2196F3', 'y': 4.5},
        {'level': 'L4', 'name': '数据文化', 'desc': '用数据说话，量化决策', 'color': '#4CAF50', 'y': 3},
        {'level': 'L5', 'name': '创新文化', 'desc': '持续改进，技术引领', 'color': '#9C27B0', 'y': 1.5},
    ]
    
    for item in levels:
        # 等级标签
        rect = FancyBboxPatch((1, item['y']-0.4), 2, 0.8, boxstyle="round,pad=0.02",
                             facecolor=item['color'], edgecolor='black', linewidth=2)
        ax.add_patch(rect)
        ax.text(2, item['y'], item['level'], ha='center', va='center', 
               fontsize=11, fontweight='bold', color='white')
        
        # 文化名称
        ax.text(4, item['y'], item['name'], ha='left', va='center', 
               fontsize=13, fontweight='bold', color=item['color'])
        
        # 描述
        ax.text(4, item['y']-0.5, item['desc'], ha='left', va='center', 
               fontsize=10, color='#666666')
        
        # 箭头
        if item['y'] > 2:
            ax.annotate('', xy=(2, item['y']-0.6), xytext=(2, item['y']-1.2),
                       arrowprops=dict(arrowstyle='->', lw=2, color='#999999'))
    
    ax.set_xlim(0, 10)
    ax.set_ylim(0, 8)
    ax.set_aspect('equal')
    ax.axis('off')
    ax.set_title('团队文化演进路径', fontsize=18, fontweight='bold', pad=20)
    
    save_fig(fig, 'fig_3_4_culture_evolution.png')

# ============ 主函数 ============
def main():
    print("开始生成第3章配图...")
    print(f"输出目录: {output_dir}")
    
    create_l1_l5_journey()
    create_talent_model()
    create_training_system()
    create_pdca_cycle()
    create_km_flow()
    create_capability_matrix()
    create_culture_evolution()
    
    print("\n所有配图生成完成!")

if __name__ == '__main__':
    main()

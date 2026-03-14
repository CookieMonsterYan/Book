#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
第1章配图生成脚本
生成水力模型概述章节所需的专业配图
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
output_dir = "/root/.openclaw/workspace/HEBook/chapters/01-introduction/images"
os.makedirs(output_dir, exist_ok=True)

def save_fig(fig, filename):
    """保存图片"""
    filepath = os.path.join(output_dir, filename)
    fig.savefig(filepath, dpi=150, bbox_inches='tight', facecolor='white')
    print(f"已保存: {filepath}")
    plt.close(fig)

# ============ 图1: 水力模型0D-3D维度 ============
def create_model_dimensions():
    """创建水力模型维度分类图"""
    fig, axes = plt.subplots(1, 4, figsize=(16, 6))
    
    dimensions = [
        {'name': '0D 集总式', 'desc': '节点水量平衡\n无空间分布', 'example': '调蓄池\n水库', 'color': '#E3F2FD', 'icon': '●'},
        {'name': '1D 线状', 'desc': '沿程变化\n断面平均', 'example': '河道\n管网', 'color': '#BBDEFB', 'icon': '━'},
        {'name': '2D 面状', 'desc': '平面分布\n垂向平均', 'example': '漫流\n湖泊', 'color': '#90CAF9', 'icon': '▦'},
        {'name': '3D 立体', 'desc': '三维空间\n精细模拟', 'example': '水库分层\n河口', 'color': '#64B5F6', 'icon': '▣'},
    ]
    
    for ax, dim in zip(axes, dimensions):
        # 背景
        rect = FancyBboxPatch((0.1, 0.1), 0.8, 0.8, boxstyle="round,pad=0.05",
                             facecolor=dim['color'], edgecolor='black', linewidth=2,
                             transform=ax.transAxes)
        ax.add_patch(rect)
        
        # 维度标识
        ax.text(0.5, 0.75, dim['name'], ha='center', va='center', 
               fontsize=14, fontweight='bold', transform=ax.transAxes)
        
        # 特点
        ax.text(0.5, 0.5, dim['desc'], ha='center', va='center', 
               fontsize=10, linespacing=0.9, transform=ax.transAxes)
        
        # 示例
        ax.text(0.5, 0.25, f"应用:\n{dim['example']}", ha='center', va='center', 
               fontsize=9, color='#666666', transform=ax.transAxes)
        
        ax.set_xlim(0, 1)
        ax.set_ylim(0, 1)
        ax.axis('off')
    
    fig.suptitle('水力模型空间维度分类 (0D/1D/2D/3D)', fontsize=18, fontweight='bold')
    save_fig(fig, 'fig_1_1_dimensions.png')

# ============ 图2: 水力模型应用领域 ============
def create_application_areas():
    """创建水力模型应用领域图"""
    fig, ax = plt.subplots(figsize=(14, 10))
    
    # 应用领域数据
    areas = [
        {'name': '城市排水', 'size': 30, 'color': '#2196F3', 'x': 0.3, 'y': 0.8},
        {'name': '防洪减灾', 'size': 25, 'color': '#F44336', 'x': 0.7, 'y': 0.8},
        {'name': '水资源管理', 'size': 20, 'color': '#4CAF50', 'x': 0.2, 'y': 0.5},
        {'name': '水环境治理', 'size': 15, 'color': '#9C27B0', 'x': 0.5, 'y': 0.5},
        {'name': '水利工程', 'size': 10, 'color': '#FF9800', 'x': 0.8, 'y': 0.5},
    ]
    
    for area in areas:
        size = area['size'] / 100 * 0.3
        circle = Circle((area['x'], area['y']), size, 
                       facecolor=area['color'], edgecolor='black', 
                       linewidth=2, alpha=0.7, transform=ax.transAxes)
        ax.add_patch(circle)
        ax.text(area['x'], area['y'], area['name'], 
               ha='center', va='center', fontsize=11, fontweight='bold',
               color='white', transform=ax.transAxes)
        ax.text(area['x'], area['y']-size-0.05, f"{area['size']}%", 
               ha='center', va='center', fontsize=10, color=area['color'],
               transform=ax.transAxes)
    
    # 中心核心
    center = Circle((0.5, 0.25), 0.15, facecolor='#FFD700', 
                   edgecolor='black', linewidth=3, transform=ax.transAxes)
    ax.add_patch(center)
    ax.text(0.5, 0.25, '水力模型\n核心价值', ha='center', va='center', 
           fontsize=12, fontweight='bold', transform=ax.transAxes)
    
    ax.set_xlim(0, 1)
    ax.set_ylim(0, 1)
    ax.axis('off')
    ax.set_title('水力模型应用领域分布', fontsize=18, fontweight='bold', pad=20)
    
    save_fig(fig, 'fig_1_3_applications.png')

# ============ 图3: 水力模型发展历程 ============
def create_development_timeline():
    """创建水力模型发展历程时间轴"""
    fig, ax = plt.subplots(figsize=(16, 8))
    
    events = [
        {'year': '1960s', 'event': '圣维南方程\n数值求解', 'color': '#9E9E9E', 'y': 0.6},
        {'year': '1970s', 'event': 'SWMM诞生\n城市排水模拟', 'color': '#9E9E9E', 'y': 0.6},
        {'year': '1980s', 'event': '商业软件\nMIKE/InfoWorks', 'color': '#FFC107', 'y': 0.6},
        {'year': '1990s', 'event': 'GIS集成\n可视化发展', 'color': '#FFC107', 'y': 0.6},
        {'year': '2000s', 'event': '2D/3D模型\n并行计算', 'color': '#2196F3', 'y': 0.6},
        {'year': '2010s', 'event': '云计算\n实时模拟', 'color': '#2196F3', 'y': 0.6},
        {'year': '2020s', 'event': 'AI融合\n智能建模', 'color': '#9C27B0', 'y': 0.6},
    ]
    
    # 时间轴线
    ax.plot([0.5, 13.5], [0.5, 0.5], 'k-', linewidth=3)
    
    for i, event in enumerate(events):
        x = i * 2 + 1
        
        # 事件点
        circle = Circle((x, 0.5), 0.3, facecolor=event['color'], 
                       edgecolor='black', linewidth=2)
        ax.add_patch(circle)
        ax.text(x, 0.5, event['year'], ha='center', va='center', 
               fontsize=10, fontweight='bold')
        
        # 事件描述
        y_offset = 1.2 if i % 2 == 0 else -0.2
        ax.text(x, y_offset, event['event'], ha='center', va='center',
               fontsize=10, bbox=dict(boxstyle='round', facecolor=event['color'], alpha=0.3))
        
        # 连接线
        ax.plot([x, x], [0.5, y_offset-0.15 if i%2==0 else y_offset+0.15], 
               'k--', linewidth=1, alpha=0.5)
    
    ax.set_xlim(0, 14)
    ax.set_ylim(0, 2)
    ax.axis('off')
    ax.set_title('水力模型发展历程', fontsize=18, fontweight='bold', pad=20)
    
    save_fig(fig, 'fig_1_2_timeline.png')

# ============ 图4: 物理过程耦合 ============
def create_physical_processes():
    """创建物理过程耦合图"""
    fig, ax = plt.subplots(figsize=(12, 10))
    
    # 核心水动力
    core = Circle((0.5, 0.5), 0.15, facecolor='#2196F3', 
                 edgecolor='black', linewidth=3, transform=ax.transAxes)
    ax.add_patch(core)
    ax.text(0.5, 0.5, '水动力\n核心', ha='center', va='center', 
           fontsize=12, fontweight='bold', color='white', transform=ax.transAxes)
    
    # 外围物理过程
    processes = [
        {'name': '降雨径流', 'angle': 90, 'color': '#4CAF50'},
        {'name': '水质传输', 'angle': 30, 'color': '#9C27B0'},
        {'name': '泥沙输移', 'angle': -30, 'color': '#FF9800'},
        {'name': '生态过程', 'angle': -90, 'color': '#00BCD4'},
        {'name': '热力交换', 'angle': -150, 'color': '#F44336'},
        {'name': '结冰融冰', 'angle': 150, 'color': '#607D8B'},
    ]
    
    for proc in processes:
        angle_rad = np.deg2rad(proc['angle'])
        x = 0.5 + 0.35 * np.cos(angle_rad)
        y = 0.5 + 0.35 * np.sin(angle_rad)
        
        # 过程框
        rect = FancyBboxPatch((x-0.08, y-0.05), 0.16, 0.1, 
                             boxstyle="round,pad=0.02",
                             facecolor=proc['color'], edgecolor='black', 
                             linewidth=2, transform=ax.transAxes)
        ax.add_patch(rect)
        ax.text(x, y, proc['name'], ha='center', va='center', 
               fontsize=10, fontweight='bold', color='white', transform=ax.transAxes)
        
        # 连线
        ax.plot([0.5 + 0.15*np.cos(angle_rad), x - 0.08*np.cos(angle_rad)],
               [0.5 + 0.15*np.sin(angle_rad), y - 0.05*np.sin(angle_rad)],
               'k-', linewidth=2, alpha=0.3, transform=ax.transAxes)
    
    ax.set_xlim(0, 1)
    ax.set_ylim(0, 1)
    ax.axis('off')
    ax.set_title('水力模型物理过程耦合', fontsize=18, fontweight='bold', pad=20)
    
    save_fig(fig, 'fig_1_1_processes.png')

# ============ 主函数 ============
def main():
    print("开始生成第1章配图...")
    print(f"输出目录: {output_dir}")
    
    create_model_dimensions()
    create_application_areas()
    create_development_timeline()
    create_physical_processes()
    
    print("\n所有配图生成完成!")

if __name__ == '__main__':
    main()

#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
第6章配图生成脚本
生成AI智能体章节所需的专业配图
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
output_dir = "/root/.openclaw/workspace/HEBook/chapters/06-ai-agent/images"
os.makedirs(output_dir, exist_ok=True)

def save_fig(fig, filename):
    """保存图片"""
    filepath = os.path.join(output_dir, filename)
    fig.savefig(filepath, dpi=150, bbox_inches='tight', facecolor='white')
    print(f"已保存: {filepath}")
    plt.close(fig)

# ============ 图1: AI智能体架构 ============
def create_agent_architecture():
    """创建AI智能体架构图"""
    fig, ax = plt.subplots(figsize=(12, 10))
    
    # 核心LLM
    core = Circle((0.5, 0.5), 0.12, facecolor='#9C27B0', 
                 edgecolor='black', linewidth=3, transform=ax.transAxes)
    ax.add_patch(core)
    ax.text(0.5, 0.5, '大语言模型\nLLM', ha='center', va='center', 
           fontsize=11, fontweight='bold', color='white', transform=ax.transAxes)
    
    # 周围模块
    modules = [
        {'name': '感知模块', 'desc': '接收输入\n环境数据', 'angle': 90, 'color': '#2196F3'},
        {'name': '规划模块', 'desc': '制定策略\n任务分解', 'angle': 30, 'color': '#4CAF50'},
        {'name': '记忆模块', 'desc': '短期/长期\n知识存储', 'angle': -30, 'color': '#FF9800'},
        {'name': '工具模块', 'desc': 'API调用\n外部工具', 'angle': -90, 'color': '#F44336'},
        {'name': '执行模块', 'desc': '输出结果\n执行动作', 'angle': -150, 'color': '#00BCD4'},
        {'name': '学习模块', 'desc': '反馈优化\n持续改进', 'angle': 150, 'color': '#9C27B0'},
    ]
    
    for module in modules:
        angle_rad = np.deg2rad(module['angle'])
        x = 0.5 + 0.3 * np.cos(angle_rad)
        y = 0.5 + 0.3 * np.sin(angle_rad)
        
        # 模块框
        rect = FancyBboxPatch((x-0.08, y-0.06), 0.16, 0.12, 
                             boxstyle="round,pad=0.02",
                             facecolor=module['color'], edgecolor='black', 
                             linewidth=2, transform=ax.transAxes)
        ax.add_patch(rect)
        ax.text(x, y+0.02, module['name'], ha='center', va='center', 
               fontsize=9, fontweight='bold', color='white', transform=ax.transAxes)
        ax.text(x, y-0.03, module['desc'], ha='center', va='center', 
               fontsize=7, color='white', linespacing=0.8, transform=ax.transAxes)
        
        # 连线
        ax.annotate('', xy=(x - 0.08*np.cos(angle_rad), y - 0.06*np.sin(angle_rad)),
                   xytext=(0.5 + 0.12*np.cos(angle_rad), 0.5 + 0.12*np.sin(angle_rad)),
                   arrowprops=dict(arrowstyle='->', lw=2, color='#666666'),
                   transform=ax.transAxes)
    
    ax.set_xlim(0, 1)
    ax.set_ylim(0, 1)
    ax.axis('off')
    ax.set_title('AI智能体技术架构', fontsize=18, fontweight='bold', pad=20)
    
    save_fig(fig, 'fig_6_1_agent_architecture.png')

# ============ 图2: 水力建模智能体类型 ============
def create_modeling_agents():
    """创建水力建模智能体类型图"""
    fig, ax = plt.subplots(figsize=(14, 10))
    
    # 中心水力建模
    center = Circle((0.5, 0.5), 0.1, facecolor='#2196F3', 
                   edgecolor='black', linewidth=3, transform=ax.transAxes)
    ax.add_patch(center)
    ax.text(0.5, 0.5, '水力建模\n智能体系统', ha='center', va='center', 
           fontsize=11, fontweight='bold', color='white', transform=ax.transAxes)
    
    # 各类智能体
    agents = [
        {'name': '数据智能体', 'tasks': ['数据采集', '清洗验证', '格式转换'], 'angle': 90, 'color': '#4CAF50'},
        {'name': '建模智能体', 'tasks': ['模型构建', '参数优化', '方案比选'], 'angle': 30, 'color': '#FF9800'},
        {'name': '分析智能体', 'tasks': ['结果分析', '异常检测', '报告生成'], 'angle': -30, 'color': '#9C27B0'},
        {'name': '管理智能体', 'tasks': ['进度跟踪', '风险预警', '资源调度'], 'angle': -90, 'color': '#F44336'},
        {'name': '客服智能体', 'tasks': ['需求收集', '方案沟通', '问题解答'], 'angle': -150, 'color': '#00BCD4'},
    ]
    
    for agent in agents:
        angle_rad = np.deg2rad(agent['angle'])
        x = 0.5 + 0.35 * np.cos(angle_rad)
        y = 0.5 + 0.35 * np.sin(angle_rad)
        
        # 智能体框
        rect = FancyBboxPatch((x-0.1, y-0.08), 0.2, 0.16, 
                             boxstyle="round,pad=0.02",
                             facecolor=agent['color'], edgecolor='black', 
                             linewidth=2, transform=ax.transAxes)
        ax.add_patch(rect)
        ax.text(x, y+0.04, agent['name'], ha='center', va='center', 
               fontsize=10, fontweight='bold', color='white', transform=ax.transAxes)
        
        # 任务列表
        tasks_text = '\n'.join([f'• {t}' for t in agent['tasks']])
        ax.text(x, y-0.05, tasks_text, ha='center', va='center', 
               fontsize=8, color='white', linespacing=0.9, transform=ax.transAxes)
        
        # 连线
        ax.plot([0.5 + 0.1*np.cos(angle_rad), x - 0.1*np.cos(angle_rad)],
               [0.5 + 0.1*np.sin(angle_rad), y - 0.08*np.sin(angle_rad)],
               'k-', linewidth=2, alpha=0.3, transform=ax.transAxes)
    
    ax.set_xlim(0, 1)
    ax.set_ylim(0, 1)
    ax.axis('off')
    ax.set_title('水力建模领域AI智能体类型', fontsize=18, fontweight='bold', pad=20)
    
    save_fig(fig, 'fig_6_2_modeling_agents.png')

# ============ 图3: 多智能体协作 ============
def create_multi_agent_collaboration():
    """创建多智能体协作图"""
    fig, ax = plt.subplots(figsize=(14, 10))
    
    # 协作场景
    agents = [
        {'name': '需求分析Agent', 'x': 0.2, 'y': 0.8, 'color': '#2196F3'},
        {'name': '数据采集Agent', 'x': 0.5, 'y': 0.8, 'color': '#4CAF50'},
        {'name': '模型构建Agent', 'x': 0.8, 'y': 0.8, 'color': '#FF9800'},
        {'name': '验证分析Agent', 'x': 0.35, 'y': 0.5, 'color': '#9C27B0'},
        {'name': '报告生成Agent', 'x': 0.65, 'y': 0.5, 'color': '#00BCD4'},
    ]
    
    # 绘制智能体
    for agent in agents:
        rect = FancyBboxPatch((agent['x']-0.08, agent['y']-0.04), 0.16, 0.08, 
                             boxstyle="round,pad=0.02",
                             facecolor=agent['color'], edgecolor='black', 
                             linewidth=2, transform=ax.transAxes)
        ax.add_patch(rect)
        ax.text(agent['x'], agent['y'], agent['name'], ha='center', va='center', 
               fontsize=9, fontweight='bold', color='white', transform=ax.transAxes)
    
    # 协作关系线
    collaborations = [
        ((0.2, 0.8), (0.5, 0.8), '需求'),
        ((0.5, 0.8), (0.8, 0.8), '数据'),
        ((0.8, 0.8), (0.35, 0.5), '模型'),
        ((0.35, 0.5), (0.65, 0.5), '结果'),
        ((0.5, 0.8), (0.35, 0.5), '质量'),
    ]
    
    for (x1, y1), (x2, y2), label in collaborations:
        ax.annotate('', xy=(x2, y2+0.05), xytext=(x1, y1-0.05),
                   arrowprops=dict(arrowstyle='->', lw=2, color='#666666'),
                   transform=ax.transAxes)
        mid_x, mid_y = (x1+x2)/2, (y1+y2)/2
        ax.text(mid_x, mid_y, label, ha='center', va='center', 
               fontsize=8, color='#666666', transform=ax.transAxes)
    
    # 协作结果
    result = FancyBboxPatch((0.4, 0.2), 0.2, 0.1, boxstyle="round,pad=0.02",
                           facecolor='#FFD700', edgecolor='black', linewidth=2,
                           transform=ax.transAxes)
    ax.add_patch(result)
    ax.text(0.5, 0.25, '项目交付物', ha='center', va='center', 
           fontsize=11, fontweight='bold', transform=ax.transAxes)
    
    ax.set_xlim(0, 1)
    ax.set_ylim(0, 1)
    ax.axis('off')
    ax.set_title('多智能体协作工作流程', fontsize=18, fontweight='bold', pad=20)
    
    save_fig(fig, 'fig_6_3_multi_agent.png')

# ============ 图4: 人机协作模式 ============
def create_human_ai_collaboration():
    """创建人机协作模式图"""
    fig, ax = plt.subplots(figsize=(14, 8))
    
    modes = [
        {'name': '人类主导', 'desc': '人类决策\nAI辅助', 'human': 80, 'ai': 20, 'y': 0.7},
        {'name': '人机协作', 'desc': '分工合作\n共同完成', 'human': 50, 'ai': 50, 'y': 0.4},
        {'name': 'AI主导', 'desc': 'AI执行\n人类监督', 'human': 20, 'ai': 80, 'y': 0.1},
    ]
    
    for mode in modes:
        y = mode['y']
        
        # 模式名称
        ax.text(0.5, y+0.15, mode['name'], ha='center', va='center',
               fontsize=14, fontweight='bold', transform=ax.transAxes)
        ax.text(0.5, y+0.08, mode['desc'], ha='center', va='center',
               fontsize=10, color='#666666', transform=ax.transAxes)
        
        # 人类部分
        human_width = mode['human'] / 100 * 0.6
        rect_human = FancyBboxPatch((0.5-human_width, y), human_width, 0.05,
                                    boxstyle="round,pad=0.01",
                                    facecolor='#2196F3', edgecolor='black',
                                    transform=ax.transAxes)
        ax.add_patch(rect_human)
        ax.text(0.5-human_width/2, y+0.025, f"人类{mode['human']}%",
               ha='center', va='center', fontsize=10, color='white',
               transform=ax.transAxes)
        
        # AI部分
        ai_width = mode['ai'] / 100 * 0.6
        rect_ai = FancyBboxPatch((0.5, y), ai_width, 0.05,
                                boxstyle="round,pad=0.01",
                                facecolor='#9C27B0', edgecolor='black',
                                transform=ax.transAxes)
        ax.add_patch(rect_ai)
        ax.text(0.5+ai_width/2, y+0.025, f"AI{mode['ai']}%",
               ha='center', va='center', fontsize=10, color='white',
               transform=ax.transAxes)
    
    ax.set_xlim(0, 1)
    ax.set_ylim(0, 1)
    ax.axis('off')
    ax.set_title('人机协作三种模式', fontsize=18, fontweight='bold', pad=20)
    
    save_fig(fig, 'fig_6_4_collaboration_modes.png')

# ============ 主函数 ============
def main():
    print("开始生成第6章配图...")
    print(f"输出目录: {output_dir}")
    
    create_agent_architecture()
    create_modeling_agents()
    create_multi_agent_collaboration()
    create_human_ai_collaboration()
    
    print("\n所有配图生成完成!")

if __name__ == '__main__':
    main()

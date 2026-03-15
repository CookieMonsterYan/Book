#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
第6章额外配图生成脚本
生成更多专业配图让内容更丰富
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
output_dir = "/root/.openclaw/workspace/HEBook/chapters/06-ai-agent/images"
os.makedirs(output_dir, exist_ok=True)

def save_fig(fig, filename):
    """保存图片"""
    filepath = os.path.join(output_dir, filename)
    fig.savefig(filepath, dpi=150, bbox_inches='tight', facecolor='white')
    print(f"已保存: {filepath}")
    plt.close(fig)

# ============ 图5: OpenClaw平台架构 ============
def create_openclaw_architecture():
    """创建OpenClaw平台架构图"""
    fig, ax = plt.subplots(figsize=(14, 10))
    
    # 用户层
    user_layer = FancyBboxPatch((0.1, 0.85), 0.8, 0.1, boxstyle="round,pad=0.02",
                                facecolor='#E3F2FD', edgecolor='#1976D2', linewidth=2,
                                transform=ax.transAxes)
    ax.add_patch(user_layer)
    ax.text(0.5, 0.9, '用户层：Web界面 / 飞书 / 钉钉 / API', ha='center', va='center',
           fontsize=12, fontweight='bold', transform=ax.transAxes)
    
    # 网关层
    gateway_layer = FancyBboxPatch((0.1, 0.7), 0.8, 0.1, boxstyle="round,pad=0.02",
                                   facecolor='#FFF3E0', edgecolor='#F57C00', linewidth=2,
                                   transform=ax.transAxes)
    ax.add_patch(gateway_layer)
    ax.text(0.5, 0.75, '网关层：会话管理 / 消息路由 / 权限控制', ha='center', va='center',
           fontsize=12, fontweight='bold', transform=ax.transAxes)
    
    # Agent层
    agent_layer = FancyBboxPatch((0.1, 0.45), 0.8, 0.2, boxstyle="round,pad=0.02",
                                 facecolor='#E8F5E9', edgecolor='#388E3C', linewidth=2,
                                 transform=ax.transAxes)
    ax.add_patch(agent_layer)
    ax.text(0.5, 0.62, 'Agent层', ha='center', va='center',
           fontsize=12, fontweight='bold', transform=ax.transAxes)
    
    # 各种Agent
    agents = [
        {'name': '项目知识\n管家', 'x': 0.18, 'color': '#4CAF50'},
        {'name': '数据清洗\nAgent', 'x': 0.34, 'color': '#2196F3'},
        {'name': '建模助手\nAgent', 'x': 0.5, 'color': '#FF9800'},
        {'name': '报告生成\nAgent', 'x': 0.66, 'color': '#9C27B0'},
        {'name': '质量监控\nAgent', 'x': 0.82, 'color': '#F44336'},
    ]
    
    for agent in agents:
        rect = FancyBboxPatch((agent['x']-0.06, 0.47), 0.12, 0.12, boxstyle="round,pad=0.01",
                              facecolor=agent['color'], edgecolor='black', linewidth=1.5,
                              transform=ax.transAxes)
        ax.add_patch(rect)
        ax.text(agent['x'], 0.53, agent['name'], ha='center', va='center',
               fontsize=9, color='white', fontweight='bold', transform=ax.transAxes)
    
    # 工具层
    tools_layer = FancyBboxPatch((0.1, 0.3), 0.8, 0.1, boxstyle="round,pad=0.02",
                                 facecolor='#FCE4EC', edgecolor='#C2185B', linewidth=2,
                                 transform=ax.transAxes)
    ax.add_patch(tools_layer)
    ax.text(0.5, 0.35, '工具层：文件操作 / LLM调用 / 数据库 / 外部API', ha='center', va='center',
           fontsize=12, fontweight='bold', transform=ax.transAxes)
    
    # 数据层
    data_layer = FancyBboxPatch((0.1, 0.15), 0.8, 0.1, boxstyle="round,pad=0.02",
                                facecolor='#F3E5F5', edgecolor='#7B1FA2', linewidth=2,
                                transform=ax.transAxes)
    ax.add_patch(data_layer)
    ax.text(0.5, 0.2, '数据层：项目数据 / 知识库 / 日志 / 配置', ha='center', va='center',
           fontsize=12, fontweight='bold', transform=ax.transAxes)
    
    # 添加连接线
    for y in [0.85, 0.7, 0.45, 0.3]:
        ax.arrow(0.5, y, 0, -0.05, head_width=0.02, head_length=0.02,
                fc='#666666', ec='#666666', transform=ax.transAxes)
    
    ax.set_xlim(0, 1)
    ax.set_ylim(0, 1)
    ax.axis('off')
    ax.set_title('OpenClaw平台分层架构', fontsize=18, fontweight='bold', pad=20)
    
    save_fig(fig, 'fig_6_5_openclaw_architecture.png')

# ============ 图6: 三层管控体系 ============
def create_three_layer_control():
    """创建三层管控体系图"""
    fig, ax = plt.subplots(figsize=(14, 10))
    
    layers = [
        {
            'name': '第一层：任务编排层',
            'subtitle': 'Orchestration Layer',
            'y': 0.7,
            'color': '#2196F3',
            'functions': ['定义Agent工作流', '处理任务依赖', '并行调度执行']
        },
        {
            'name': '第二层：接口契约层',
            'subtitle': 'Contract Layer',
            'y': 0.4,
            'color': '#4CAF50',
            'functions': ['定义数据格式', '输入输出校验', '版本兼容管理']
        },
        {
            'name': '第三层：质量监控层',
            'subtitle': 'Quality Layer',
            'y': 0.1,
            'color': '#FF9800',
            'functions': ['实时监控质量', '质量指标告警', '异常处理降级']
        }
    ]
    
    for layer in layers:
        # 主框
        rect = FancyBboxPatch((0.05, layer['y']), 0.9, 0.22, boxstyle="round,pad=0.02",
                              facecolor=layer['color'], edgecolor='black', linewidth=2,
                              transform=ax.transAxes, alpha=0.8)
        ax.add_patch(rect)
        
        # 标题
        ax.text(0.5, layer['y']+0.18, layer['name'], ha='center', va='center',
               fontsize=14, fontweight='bold', color='white', transform=ax.transAxes)
        ax.text(0.5, layer['y']+0.14, layer['subtitle'], ha='center', va='center',
               fontsize=10, color='white', alpha=0.8, transform=ax.transAxes)
        
        # 功能列表
        for i, func in enumerate(layer['functions']):
            x_pos = 0.2 + i * 0.3
            func_rect = FancyBboxPatch((x_pos-0.12, layer['y']+0.03), 0.24, 0.08,
                                       boxstyle="round,pad=0.01",
                                       facecolor='white', edgecolor='black', linewidth=1,
                                       transform=ax.transAxes)
            ax.add_patch(func_rect)
            ax.text(x_pos, layer['y']+0.07, func, ha='center', va='center',
                   fontsize=9, transform=ax.transAxes)
    
    # 添加箭头
    for y in [0.7, 0.4]:
        ax.arrow(0.5, y, 0, -0.05, head_width=0.02, head_length=0.03,
                fc='black', ec='black', transform=ax.transAxes)
    
    ax.set_xlim(0, 1)
    ax.set_ylim(0, 1)
    ax.axis('off')
    ax.set_title('架构师的三层管控体系', fontsize=18, fontweight='bold', pad=20)
    
    save_fig(fig, 'fig_6_6_three_layer_control.png')

# ============ 图7: 项目知识管家工作流 ============
def create_project_knowledge_workflow():
    """创建项目知识管家工作流图"""
    fig, ax = plt.subplots(figsize=(16, 10))
    
    # 定义阶段
    stages = [
        {'name': '项目启动', 'x': 0.12, 'color': '#4CAF50', 'icon': '🚀'},
        {'name': '资料整理', 'x': 0.32, 'color': '#2196F3', 'icon': '📁'},
        {'name': '过程归档', 'x': 0.52, 'color': '#FF9800', 'icon': '📝'},
        {'name': '项目总结', 'x': 0.72, 'color': '#9C27B0', 'icon': '📊'},
        {'name': '知识复用', 'x': 0.92, 'color': '#F44336', 'icon': '♻️'},
    ]
    
    # 绘制阶段
    for i, stage in enumerate(stages):
        # 圆形阶段框
        circle = Circle((stage['x'], 0.7), 0.06, facecolor=stage['color'],
                       edgecolor='black', linewidth=2, transform=ax.transAxes)
        ax.add_patch(circle)
        ax.text(stage['x'], 0.7, str(i+1), ha='center', va='center',
               fontsize=14, fontweight='bold', color='white', transform=ax.transAxes)
        
        # 阶段名称
        ax.text(stage['x'], 0.6, stage['name'], ha='center', va='center',
               fontsize=11, fontweight='bold', transform=ax.transAxes)
        
        # 连接线
        if i < len(stages) - 1:
            ax.annotate('', xy=(stages[i+1]['x']-0.06, 0.7), xytext=(stage['x']+0.06, 0.7),
                       arrowprops=dict(arrowstyle='->', lw=3, color='#666666'),
                       transform=ax.transAxes)
    
    # 详细说明
    details = [
        {'y': 0.45, 'text': '• 创建标准目录结构\n• 提取客户需求\n• 整理基础数据'},
        {'y': 0.45, 'text': '• 数据自动分类\n• 生成数据清单\n• 建立索引关系'},
        {'y': 0.45, 'text': '• 模型版本跟踪\n• 中间结果归档\n• 沟通记录存储'},
        {'y': 0.45, 'text': '• 生成项目报告\n• 总结经验教训\n• 识别可复用资产'},
        {'y': 0.45, 'text': '• 模板复用\n• 脚本复用\n• 知识沉淀'},
    ]
    
    for i, (stage, detail) in enumerate(zip(stages, details)):
        ax.text(stage['x'], 0.35, detail['text'], ha='center', va='top',
               fontsize=8, color='#333333', linespacing=1.5,
               transform=ax.transAxes)
    
    # 底部Agent标识
    agent_box = FancyBboxPatch((0.3, 0.05), 0.4, 0.1, boxstyle="round,pad=0.02",
                               facecolor='#E8F5E9', edgecolor='#4CAF50', linewidth=2,
                               transform=ax.transAxes)
    ax.add_patch(agent_box)
    ax.text(0.5, 0.1, '🤖 ProjectKnowledgeManager Agent', ha='center', va='center',
           fontsize=12, fontweight='bold', color='#2E7D32', transform=ax.transAxes)
    
    ax.set_xlim(0, 1)
    ax.set_ylim(0, 1)
    ax.axis('off')
    ax.set_title('项目知识管家工作流', fontsize=18, fontweight='bold', pad=20)
    
    save_fig(fig, 'fig_6_7_knowledge_workflow.png')

# ============ 图8: AI转型成功vs失败对比 ============
def create_ai_transformation_comparison():
    """创建AI转型成功vs失败对比图"""
    fig, axes = plt.subplots(1, 2, figsize=(16, 10))
    
    # 左侧：失败案例
    ax = axes[0]
    ax.set_xlim(0, 10)
    ax.set_ylim(0, 10)
    ax.axis('off')
    ax.set_title('❌ A公司（无架构师）：项目失败', fontsize=14, fontweight='bold', color='#D32F2F')
    
    # 时间线
    timeline = [
        {'month': '第1月', 'y': 8.5, 'text': '各自为战\n数据格式不统一', 'color': '#FFCDD2'},
        {'month': '第3月', 'y': 6.5, 'text': '技术债务爆发\n代码风格混乱', 'color': '#EF9A9A'},
        {'month': '第6月', 'y': 4.5, 'text': '安全危机\n敏感数据泄露', 'color': '#E57373'},
        {'month': '第9月', 'y': 2.5, 'text': '项目失败\n放弃自研', 'color': '#EF5350'},
    ]
    
    for item in timeline:
        rect = FancyBboxPatch((0.5, item['y']-0.8), 9, 1.5, boxstyle="round,pad=0.1",
                              facecolor=item['color'], edgecolor='#B71C1C', linewidth=2)
        ax.add_patch(rect)
        ax.text(1.5, item['y'], item['month'], ha='left', va='center',
               fontsize=11, fontweight='bold')
        ax.text(5, item['y'], item['text'], ha='center', va='center',
               fontsize=10)
    
    # 右侧：成功案例
    ax = axes[1]
    ax.set_xlim(0, 10)
    ax.set_ylim(0, 10)
    ax.axis('off')
    ax.set_title('✅ B公司（有架构师）：项目成功', fontsize=14, fontweight='bold', color='#388E3C')
    
    timeline_success = [
        {'month': '第1月', 'y': 8.5, 'text': '架构设计\n制定统一规范', 'color': '#C8E6C9'},
        {'month': '第2月', 'y': 6.8, 'text': '分层开发\nAgent并行实现', 'color': '#A5D6A7'},
        {'month': '第3月', 'y': 5.1, 'text': '集成测试\n接口契约验证', 'color': '#81C784'},
        {'month': '第4月', 'y': 3.4, 'text': '上线运营\n零安全事故', 'color': '#66BB6A'},
    ]
    
    for item in timeline_success:
        rect = FancyBboxPatch((0.5, item['y']-0.8), 9, 1.5, boxstyle="round,pad=0.1",
                              facecolor=item['color'], edgecolor='#1B5E20', linewidth=2)
        ax.add_patch(rect)
        ax.text(1.5, item['y'], item['month'], ha='left', va='center',
               fontsize=11, fontweight='bold')
        ax.text(5, item['y'], item['text'], ha='center', va='center',
               fontsize=10)
    
    plt.tight_layout()
    save_fig(fig, 'fig_6_8_transformation_comparison.png')

# ============ 图9: Agent质量监控仪表盘 ============
def create_quality_dashboard():
    """创建Agent质量监控仪表盘"""
    fig = plt.figure(figsize=(16, 10))
    gs = fig.add_gridspec(3, 3, hspace=0.3, wspace=0.3)
    
    # 整体成功率
    ax1 = fig.add_subplot(gs[0, 0])
    success_rate = 0.87
    colors = ['#4CAF50', '#E0E0E0']
    ax1.pie([success_rate, 1-success_rate], colors=colors, startangle=90,
            wedgeprops=dict(width=0.5, edgecolor='white', linewidth=2))
    ax1.text(0, 0, f'{success_rate:.0%}', ha='center', va='center', fontsize=24, fontweight='bold')
    ax1.set_title('整体成功率', fontsize=12, fontweight='bold')
    
    # 各Agent成功率对比
    ax2 = fig.add_subplot(gs[0, 1:])
    agents = ['数据清洗', '数据验证', '模型构建', '参数推荐', '结果分析', '报告生成']
    rates = [0.92, 0.88, 0.85, 0.79, 0.90, 0.93]
    colors_bar = ['#4CAF50' if r >= 0.85 else '#FF9800' if r >= 0.75 else '#F44336' for r in rates]
    bars = ax2.barh(agents, rates, color=colors_bar, edgecolor='black', linewidth=1)
    ax2.set_xlim(0, 1)
    ax2.set_xlabel('成功率', fontsize=10)
    ax2.set_title('各Agent成功率', fontsize=12, fontweight='bold')
    ax2.axvline(x=0.85, color='red', linestyle='--', linewidth=2, label='阈值')
    for i, (bar, rate) in enumerate(zip(bars, rates)):
        ax2.text(rate + 0.01, i, f'{rate:.0%}', va='center', fontsize=9)
    
    # 质量评分趋势
    ax3 = fig.add_subplot(gs[1, :])
    days = list(range(1, 31))
    quality_scores = [0.82 + 0.01 * np.sin(d/3) + np.random.normal(0, 0.02) for d in days]
    ax3.plot(days, quality_scores, 'b-', linewidth=2, marker='o', markersize=4)
    ax3.axhline(y=0.8, color='red', linestyle='--', linewidth=2, label='质量阈值')
    ax3.fill_between(days, 0.8, quality_scores, where=[q >= 0.8 for q in quality_scores],
                     alpha=0.3, color='green')
    ax3.fill_between(days, 0.8, quality_scores, where=[q < 0.8 for q in quality_scores],
                     alpha=0.3, color='red')
    ax3.set_xlabel('日期', fontsize=10)
    ax3.set_ylabel('平均质量评分', fontsize=10)
    ax3.set_title('质量评分趋势（过去30天）', fontsize=12, fontweight='bold')
    ax3.legend()
    ax3.grid(True, alpha=0.3)
    
    # 错误类型分布
    ax4 = fig.add_subplot(gs[2, 0])
    error_types = ['数据格式', '参数异常', '超时', 'API错误', '其他']
    error_counts = [12, 8, 5, 3, 2]
    colors_pie = ['#F44336', '#FF9800', '#FFC107', '#4CAF50', '#9E9E9E']
    ax4.pie(error_counts, labels=error_types, colors=colors_pie, autopct='%1.0f%%',
            startangle=90, textprops={'fontsize': 9})
    ax4.set_title('错误类型分布', fontsize=12, fontweight='bold')
    
    # 执行时间分布
    ax5 = fig.add_subplot(gs[2, 1:])
    execution_times = [12, 8, 15, 22, 10, 18, 25, 11, 9, 14]
    agents_time = ['数据清洗', '数据验证', '模型构建', '参数推荐', '结果分析',
                   '报告生成', '知识检索', '代码生成', '文档解析', '图表生成']
    colors_time = ['#2196F3'] * 10
    bars = ax5.bar(agents_time, execution_times, color=colors_time, edgecolor='black', linewidth=1)
    ax5.set_ylabel('平均执行时间(秒)', fontsize=10)
    ax5.set_title('各Agent平均执行时间', fontsize=12, fontweight='bold')
    ax5.tick_params(axis='x', rotation=45)
    for bar, time in zip(bars, execution_times):
        height = bar.get_height()
        ax5.text(bar.get_x() + bar.get_width()/2., height,
                f'{time}s', ha='center', va='bottom', fontsize=8)
    
    plt.suptitle('Agent质量监控仪表盘', fontsize=18, fontweight='bold', y=0.98)
    save_fig(fig, 'fig_6_9_quality_dashboard.png')

# ============ 图10: 数据准备Agent工作流 ============
def create_data_preparation_workflow():
    """创建数据准备Agent工作流图"""
    fig, ax = plt.subplots(figsize=(16, 8))
    
    # 输入数据
    inputs = [
        {'name': '管网数据\n(CAD/Excel)', 'x': 0.1, 'y': 0.75, 'color': '#E3F2FD'},
        {'name': '地形数据\n(DEM)', 'x': 0.1, 'y': 0.55, 'color': '#E3F2FD'},
        {'name': '监测数据\n(CSV)', 'x': 0.1, 'y': 0.35, 'color': '#E3F2FD'},
        {'name': '气象数据\n(API)', 'x': 0.1, 'y': 0.15, 'color': '#E3F2FD'},
    ]
    
    for inp in inputs:
        rect = FancyBboxPatch((inp['x'], inp['y']), 0.15, 0.12, boxstyle="round,pad=0.02",
                              facecolor=inp['color'], edgecolor='#1976D2', linewidth=2,
                              transform=ax.transAxes)
        ax.add_patch(rect)
        ax.text(inp['x']+0.075, inp['y']+0.06, inp['name'], ha='center', va='center',
               fontsize=9, transform=ax.transAxes)
    
    # 数据准备Agent
    agent_box = FancyBboxPatch((0.35, 0.35), 0.2, 0.3, boxstyle="round,pad=0.02",
                               facecolor='#4CAF50', edgecolor='#1B5E20', linewidth=3,
                               transform=ax.transAxes)
    ax.add_patch(agent_box)
    ax.text(0.45, 0.55, '数据准备\nAgent', ha='center', va='center',
           fontsize=14, fontweight='bold', color='white', transform=ax.transAxes)
    ax.text(0.45, 0.45, '🤖 DataPreparationAgent', ha='center', va='center',
           fontsize=9, color='white', transform=ax.transAxes)
    
    # 处理步骤
    steps = [
        {'name': '数据采集', 'x': 0.32, 'y': 0.8},
        {'name': '数据清洗', 'x': 0.4, 'y': 0.8},
        {'name': '格式转换', 'x': 0.48, 'y': 0.8},
        {'name': '质量检查', 'x': 0.56, 'y': 0.8},
    ]
    
    for i, step in enumerate(steps):
        rect = FancyBboxPatch((step['x'], step['y']), 0.08, 0.08, boxstyle="round,pad=0.01",
                              facecolor='#FFF3E0', edgecolor='#F57C00', linewidth=1.5,
                              transform=ax.transAxes)
        ax.add_patch(rect)
        ax.text(step['x']+0.04, step['y']+0.04, str(i+1), ha='center', va='center',
               fontsize=10, fontweight='bold', transform=ax.transAxes)
    
    # 输出
    outputs = [
        {'name': '清洗后数据\n(标准化格式)', 'x': 0.7, 'y': 0.6, 'color': '#E8F5E9'},
        {'name': '质量报告\n(JSON/Markdown)', 'x': 0.7, 'y': 0.4, 'color': '#E8F5E9'},
    ]
    
    for out in outputs:
        rect = FancyBboxPatch((out['x'], out['y']), 0.18, 0.12, boxstyle="round,pad=0.02",
                              facecolor=out['color'], edgecolor='#388E3C', linewidth=2,
                              transform=ax.transAxes)
        ax.add_patch(rect)
        ax.text(out['x']+0.09, out['y']+0.06, out['name'], ha='center', va='center',
               fontsize=9, transform=ax.transAxes)
    
    # 箭头
    # 输入到Agent
    for y in [0.81, 0.61, 0.41, 0.21]:
        ax.arrow(0.25, y, 0.08, 0.35-y, head_width=0.02, head_length=0.02,
                fc='#666666', ec='#666666', transform=ax.transAxes)
    
    # Agent到输出
    ax.arrow(0.55, 0.55, 0.12, 0.08, head_width=0.02, head_length=0.02,
            fc='#666666', ec='#666666', transform=ax.transAxes)
    ax.arrow(0.55, 0.5, 0.12, -0.08, head_width=0.02, head_length=0.02,
            fc='#666666', ec='#666666', transform=ax.transAxes)
    
    ax.set_xlim(0, 1)
    ax.set_ylim(0, 1)
    ax.axis('off')
    ax.set_title('数据准备Agent工作流程', fontsize=18, fontweight='bold', pad=20)
    
    save_fig(fig, 'fig_6_10_data_preparation_workflow.png')

# ============ 图11: 人机协作演进 ============
def create_human_ai_evolution():
    """创建人机协作演进图"""
    fig, ax = plt.subplots(figsize=(16, 8))
    
    stages = [
        {
            'name': '工具模式\nTool Mode',
            'human': 90,
            'ai': 10,
            'desc': 'AI是被动工具\n人类完全主导',
            'example': 'ChatGPT问答',
            'x': 0.15
        },
        {
            'name': '助手模式\nAssistant Mode',
            'human': 70,
            'ai': 30,
            'desc': 'AI主动建议\n人类决策执行',
            'example': 'AI推荐参数',
            'x': 0.40
        },
        {
            'name': '协作模式\nCollaboration Mode',
            'human': 50,
            'ai': 50,
            'desc': '人机平等协作\n分工明确',
            'example': '人机共同建模',
            'x': 0.65
        },
        {
            'name': '代理模式\nAgent Mode',
            'human': 20,
            'ai': 80,
            'desc': 'AI代理执行\n人类关键介入',
            'example': '全自动数据准备',
            'x': 0.90
        }
    ]
    
    for stage in stages:
        x = stage['x']
        
        # 阶段标题
        ax.text(x, 0.9, stage['name'], ha='center', va='center',
               fontsize=12, fontweight='bold', transform=ax.transAxes)
        
        # 人机比例条
        human_width = stage['human'] / 100 * 0.18
        ai_width = stage['ai'] / 100 * 0.18
        
        # 人类部分
        rect_human = FancyBboxPatch((x-human_width, 0.7), human_width, 0.12,
                                    boxstyle="round,pad=0.01",
                                    facecolor='#2196F3', edgecolor='black',
                                    transform=ax.transAxes)
        ax.add_patch(rect_human)
        ax.text(x-human_width/2, 0.76, f'人{stage["human"]}%',
               ha='center', va='center', fontsize=9, color='white',
               transform=ax.transAxes)
        
        # AI部分
        rect_ai = FancyBboxPatch((x, 0.7), ai_width, 0.12,
                                boxstyle="round,pad=0.01",
                                facecolor='#9C27B0', edgecolor='black',
                                transform=ax.transAxes)
        ax.add_patch(rect_ai)
        ax.text(x+ai_width/2, 0.76, f'AI{stage["ai"]}%',
               ha='center', va='center', fontsize=9, color='white',
               transform=ax.transAxes)
        
        # 描述
        ax.text(x, 0.55, stage['desc'], ha='center', va='center',
               fontsize=9, color='#333333', linespacing=1.3,
               transform=ax.transAxes)
        
        # 示例
        example_box = FancyBboxPatch((x-0.08, 0.35), 0.16, 0.12,
                                     boxstyle="round,pad=0.01",
                                     facecolor='#FFF8E1', edgecolor='#FFC107',
                                     linewidth=1.5, transform=ax.transAxes)
        ax.add_patch(example_box)
        ax.text(x, 0.41, f'💡 {stage["example"]}', ha='center', va='center',
               fontsize=8, transform=ax.transAxes)
        
        # 连接箭头（除了最后一个）
        if x < 0.9:
            ax.annotate('', xy=(x+0.12, 0.76), xytext=(x+0.1, 0.76),
                       arrowprops=dict(arrowstyle='->', lw=3, color='#4CAF50'),
                       transform=ax.transAxes)
    
    # 演进方向
    ax.annotate('', xy=(0.95, 0.76), xytext=(0.05, 0.76),
               arrowprops=dict(arrowstyle='->', lw=4, color='#FF5722'),
               transform=ax.transAxes)
    ax.text(0.5, 0.82, '演进方向 →', ha='center', va='center',
           fontsize=14, fontweight='bold', color='#FF5722', transform=ax.transAxes)
    
    ax.set_xlim(0, 1)
    ax.set_ylim(0, 1)
    ax.axis('off')
    ax.set_title('人机协作模式演进', fontsize=18, fontweight='bold', pad=20)
    
    save_fig(fig, 'fig_6_11_human_ai_evolution.png')

# ============ 图12: 虚拟工程师团队架构 ============
def create_virtual_team_architecture():
    """创建虚拟工程师团队架构图"""
    fig, ax = plt.subplots(figsize=(16, 12))
    
    # 架构师（总工程师）
    architect = FancyBboxPatch((0.35, 0.85), 0.3, 0.1, boxstyle="round,pad=0.02",
                               facecolor='#FFD700', edgecolor='#FF6F00', linewidth=3,
                               transform=ax.transAxes)
    ax.add_patch(architect)
    ax.text(0.5, 0.9, '👨‍💼 架构师（总工程师）', ha='center', va='center',
           fontsize=14, fontweight='bold', transform=ax.transAxes)
    ax.text(0.5, 0.87, '设计系统 · 制定标准 · 把控质量 · 持续优化',
           ha='center', va='center', fontsize=9, transform=ax.transAxes)
    
    # 三层管控
    layers = [
        {'name': '任务编排层', 'y': 0.7, 'color': '#BBDEFB'},
        {'name': '接口契约层', 'y': 0.55, 'color': '#C8E6C9'},
        {'name': '质量监控层', 'y': 0.4, 'color': '#FFECB3'},
    ]
    
    for layer in layers:
        rect = FancyBboxPatch((0.1, layer['y']), 0.8, 0.1, boxstyle="round,pad=0.02",
                              facecolor=layer['color'], edgecolor='black', linewidth=1.5,
                              transform=ax.transAxes)
        ax.add_patch(rect)
        ax.text(0.5, layer['y']+0.05, layer['name'], ha='center', va='center',
               fontsize=11, fontweight='bold', transform=ax.transAxes)
    
    # 虚拟工程师团队
    agents = [
        {'name': '数据清洗\nAgent', 'x': 0.15, 'y': 0.22, 'color': '#4CAF50'},
        {'name': '数据验证\nAgent', 'x': 0.32, 'y': 0.22, 'color': '#2196F3'},
        {'name': '模型构建\nAgent', 'x': 0.49, 'y': 0.22, 'color': '#FF9800'},
        {'name': '参数推荐\nAgent', 'x': 0.66, 'y': 0.22, 'color': '#9C27B0'},
        {'name': '结果分析\nAgent', 'x': 0.83, 'y': 0.22, 'color': '#00BCD4'},
    ]
    
    for agent in agents:
        rect = FancyBboxPatch((agent['x']-0.06, agent['y']-0.06), 0.12, 0.12,
                              boxstyle="round,pad=0.01",
                              facecolor=agent['color'], edgecolor='black', linewidth=1.5,
                              transform=ax.transAxes)
        ax.add_patch(rect)
        ax.text(agent['x'], agent['y'], agent['name'], ha='center', va='center',
               fontsize=8, color='white', fontweight='bold', transform=ax.transAxes)
    
    # 团队标签
    team_label = FancyBboxPatch((0.3, 0.07), 0.4, 0.08, boxstyle="round,pad=0.02",
                                facecolor='#E8EAF6', edgecolor='#3F51B5', linewidth=2,
                                transform=ax.transAxes)
    ax.add_patch(team_label)
    ax.text(0.5, 0.11, '🤖 虚拟工程师团队（50+ Agents）', ha='center', va='center',
           fontsize=12, fontweight='bold', color='#3F51B5', transform=ax.transAxes)
    
    # 连接箭头
    ax.arrow(0.5, 0.85, 0, -0.05, head_width=0.02, head_length=0.02,
            fc='black', ec='black', transform=ax.transAxes)
    for y in [0.7, 0.55, 0.4]:
        ax.arrow(0.5, y, 0, -0.05, head_width=0.02, head_length=0.02,
                fc='black', ec='black', transform=ax.transAxes)
    
    # 从三层到Agent的连接
    for agent in agents:
        ax.plot([agent['x'], agent['x']], [0.35, agent['y']+0.06], 'k-', linewidth=1, alpha=0.3,
               transform=ax.transAxes)
    
    ax.set_xlim(0, 1)
    ax.set_ylim(0, 1)
    ax.axis('off')
    ax.set_title('虚拟工程师团队架构', fontsize=18, fontweight='bold', pad=20)
    
    save_fig(fig, 'fig_6_12_virtual_team_architecture.png')

# ============ 主函数 ============
def main():
    print("开始生成第6章额外配图...")
    print(f"输出目录: {output_dir}")
    
    create_openclaw_architecture()
    create_three_layer_control()
    create_project_knowledge_workflow()
    create_ai_transformation_comparison()
    create_quality_dashboard()
    create_data_preparation_workflow()
    create_human_ai_evolution()
    create_virtual_team_architecture()
    
    print("\n所有额外配图生成完成!")
    print(f"第6章现在共有 12 张配图")

if __name__ == '__main__':
    main()

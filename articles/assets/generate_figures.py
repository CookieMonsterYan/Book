#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""生成微信公众号文章配图 - 中文版本"""

import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
from matplotlib.patches import FancyBboxPatch, Circle, Rectangle, FancyArrowPatch
import matplotlib.font_manager as fm
import numpy as np
import os

# 直接加载中文字体文件
font_path = '/usr/share/fonts/opentype/noto/NotoSansCJK-Regular.ttc'
chinese_font = fm.FontProperties(fname=font_path)
chinese_font_bold = fm.FontProperties(fname=font_path, weight='bold')

ASSETS_DIR = "/root/.openclaw/workspace/HEBook/articles/assets"

def save_fig(fig, filename):
    filepath = os.path.join(ASSETS_DIR, filename)
    fig.savefig(filepath, dpi=150, bbox_inches='tight', facecolor='white', edgecolor='none')
    plt.close(fig)
    print(f"已生成: {filepath}")

def fig1_isolated_agents():
    """图1: 各自为战的混乱局面"""
    fig, ax = plt.subplots(1, 1, figsize=(10, 6))
    ax.set_xlim(0, 10)
    ax.set_ylim(0, 6)
    ax.axis('off')
    
    # 标题
    ax.text(5, 5.5, '缺少架构 = 混乱', fontsize=16, fontproperties=chinese_font_bold, 
            ha='center', color='#333333')
    ax.text(5, 5.1, '三个 Agent 各自为战，无法协作', fontsize=11, 
            fontproperties=chinese_font, ha='center', color='#666666')
    
    # Agent A - 数据清洗（左）
    box_a = FancyBboxPatch((0.5, 2.5), 2.2, 2, boxstyle="round,pad=0.05", 
                           facecolor='#FF6B6B', edgecolor='#C92A2A', linewidth=2, alpha=0.9)
    ax.add_patch(box_a)
    ax.text(1.6, 3.8, '工程师 A', fontsize=11, fontproperties=chinese_font_bold, ha='center', color='white')
    ax.text(1.6, 3.3, '数据清洗 Agent', fontsize=10, fontproperties=chinese_font, ha='center', color='white')
    ax.text(1.6, 2.8, 'Python + CSV 格式', fontsize=9, fontproperties=chinese_font, ha='center', color='#FFE0E0')
    
    # Agent B - 数据校验（中）
    box_b = FancyBboxPatch((3.8, 2.5), 2.2, 2, boxstyle="round,pad=0.05",
                           facecolor='#4ECDC4', edgecolor='#087F5B', linewidth=2, alpha=0.9)
    ax.add_patch(box_b)
    ax.text(4.9, 3.8, '工程师 B', fontsize=11, fontproperties=chinese_font_bold, ha='center', color='white')
    ax.text(4.9, 3.3, '数据校验 Agent', fontsize=10, fontproperties=chinese_font, ha='center', color='white')
    ax.text(4.9, 2.8, 'JavaScript + JSON', fontsize=9, fontproperties=chinese_font, ha='center', color='#E0F7F5')
    
    # Agent C - 报告生成（右）
    box_c = FancyBboxPatch((7.1, 2.5), 2.2, 2, boxstyle="round,pad=0.05",
                           facecolor='#95E1D3', edgecolor='#2B8A3E', linewidth=2, alpha=0.9)
    ax.add_patch(box_c)
    ax.text(8.2, 3.8, '工程师 C', fontsize=11, fontproperties=chinese_font_bold, ha='center', color='#333')
    ax.text(8.2, 3.3, '报告生成 Agent', fontsize=10, fontproperties=chinese_font, ha='center', color='#333')
    ax.text(8.2, 2.8, 'GPT API + 字符串', fontsize=9, fontproperties=chinese_font, ha='center', color='#555')
    
    # 连接线表示混乱
    ax.annotate('', xy=(3.8, 3.5), xytext=(2.7, 3.5),
                arrowprops=dict(arrowstyle='<->', color='#FF6B6B', lw=2, ls='--'))
    ax.annotate('', xy=(7.1, 3.5), xytext=(6.0, 3.5),
                arrowprops=dict(arrowstyle='<->', color='#FF6B6B', lw=2, ls='--'))
    
    # 问题标注
    ax.text(1.6, 1.8, '数据格式不兼容', fontsize=9, fontproperties=chinese_font_bold, ha='center', color='#C92A2A')
    ax.text(4.9, 1.8, '无法互相调用', fontsize=9, fontproperties=chinese_font_bold, ha='center', color='#C92A2A')
    ax.text(8.2, 1.8, '缺乏统一规范', fontsize=9, fontproperties=chinese_font_bold, ha='center', color='#C92A2A')
    
    save_fig(fig, 'fig1_isolated_agents.png')

def fig2_layered_architecture():
    """图2: 分层架构设计示意图"""
    fig, ax = plt.subplots(1, 1, figsize=(10, 7))
    ax.set_xlim(0, 10)
    ax.set_ylim(0, 7)
    ax.axis('off')
    
    # 标题
    ax.text(5, 6.5, '清晰的分层架构设计', fontsize=16, fontproperties=chinese_font_bold, 
            ha='center', color='#333333')
    
    # 应用层
    layer3 = FancyBboxPatch((1, 4.8), 8, 1.4, boxstyle="round,pad=0.05",
                            facecolor='#4DABF7', edgecolor='#1971C2', linewidth=2)
    ax.add_patch(layer3)
    ax.text(5, 5.8, '应用层', fontsize=13, fontproperties=chinese_font_bold, ha='center', color='white')
    ax.text(5, 5.3, '数据 Agent | 建模 Agent | 报告 Agent', fontsize=10, fontproperties=chinese_font, ha='center', color='white')
    
    # 箭头
    ax.annotate('', xy=(5, 4.6), xytext=(5, 4.8),
                arrowprops=dict(arrowstyle='->', color='#666', lw=2))
    
    # 服务层
    layer2 = FancyBboxPatch((1, 3.0), 8, 1.4, boxstyle="round,pad=0.05",
                            facecolor='#69DB7C', edgecolor='#2F9E44', linewidth=2)
    ax.add_patch(layer2)
    ax.text(5, 4.0, '服务层', fontsize=13, fontproperties=chinese_font_bold, ha='center', color='white')
    ax.text(5, 3.5, 'LLM 服务 | 数据服务 | 权限服务', fontsize=10, fontproperties=chinese_font, ha='center', color='white')
    
    # 箭头
    ax.annotate('', xy=(5, 2.8), xytext=(5, 3.0),
                arrowprops=dict(arrowstyle='->', color='#666', lw=2))
    
    # 数据层
    layer1 = FancyBboxPatch((1, 1.2), 8, 1.4, boxstyle="round,pad=0.05",
                            facecolor='#FFD43B', edgecolor='#F08C00', linewidth=2)
    ax.add_patch(layer1)
    ax.text(5, 2.2, '数据层', fontsize=13, fontproperties=chinese_font_bold, ha='center', color='#333')
    ax.text(5, 1.7, '项目数据库 | 知识库 | 模型库', fontsize=10, fontproperties=chinese_font, ha='center', color='#333')
    
    # 优势
    benefits = ['接口清晰统一', '协议标准化', '易于维护和扩展']
    for i, benefit in enumerate(benefits):
        ax.text(5, 0.5 - i*0.35, benefit, fontsize=10, fontproperties=chinese_font_bold, ha='center', color='#2B8A3E')
    
    save_fig(fig, 'fig2_layered_architecture.png')

def fig3_architect_responsibilities():
    """图3: AI时代架构师的核心职责"""
    fig, ax = plt.subplots(1, 1, figsize=(10, 7))
    ax.set_xlim(0, 10)
    ax.set_ylim(0, 7)
    ax.axis('off')
    
    # 标题
    ax.text(5, 6.5, 'AI 时代：架构师更加重要', fontsize=16, 
            fontproperties=chinese_font_bold, ha='center', color='#333333')
    
    # 中心圆 - 架构师
    center_circle = Circle((5, 3.5), 1.2, facecolor='#7950F2', edgecolor='#5F3DC4', linewidth=3)
    ax.add_patch(center_circle)
    ax.text(5, 3.7, '架构师', fontsize=12, fontproperties=chinese_font_bold, ha='center', color='white')
    ax.text(5, 3.2, '决策者', fontsize=9, fontproperties=chinese_font, ha='center', color='#E0D4FC')
    
    # 周围职责
    responsibilities = [
        ('系统\n集成', 2, 5.5, '#FF6B6B'),
        ('安全\n合规', 8, 5.5, '#4ECDC4'),
        ('质量\n标准', 1.2, 3.5, '#FFD93D'),
        ('技术\n选型', 8.8, 3.5, '#6BCF7F'),
        ('长期\n维护', 2, 1.5, '#A78BFA'),
        ('团队\n赋能', 8, 1.5, '#FF8F8F'),
    ]
    
    for text, x, y, color in responsibilities:
        small_circle = Circle((x, y), 0.7, facecolor=color, edgecolor='white', linewidth=2)
        ax.add_patch(small_circle)
        ax.text(x, y, text, fontsize=9, fontproperties=chinese_font_bold, ha='center', va='center', color='white')
        
        # 连接线
        ax.annotate('', xy=(5 + (x-5)*0.25, 3.5 + (y-3.5)*0.25), xytext=(x, y),
                    arrowprops=dict(arrowstyle='->', color='#999', lw=1.5, connectionstyle='arc3,rad=0.1'))
    
    # 底部文字
    ax.text(5, 0.5, 'AI 写代码 - 架构师确保系统可用', fontsize=12, 
            fontproperties=chinese_font_bold, ha='center', color='#5F3DC4')
    
    save_fig(fig, 'fig3_architect_responsibilities.png')

def fig4_five_responsibilities():
    """图4: 架构师的5个核心职责"""
    fig, ax = plt.subplots(1, 1, figsize=(10, 7))
    ax.set_xlim(0, 10)
    ax.set_ylim(0, 7)
    ax.axis('off')
    
    # 标题
    ax.text(5, 6.5, "架构师的 5 个核心职责", fontsize=16, 
            fontproperties=chinese_font_bold, ha='center', color='#333333')
    
    # 5个职责
    responsibilities = [
        ('架构\n设计', '#FF6B6B', '从"能用"到"好用"'),
        ('技术\n选型', '#4ECDC4', '避免"选型灾难"'),
        ('安全\n合规', '#FFD93D', '守住底线'),
        ('质量\n标准', '#6BCF7F', 'AI 代码也要审查'),
        ('团队\n赋能', '#A78BFA', '让每个人都能用好 AI'),
    ]
    
    positions = [(2, 4.5), (5, 5.5), (8, 4.5), (7, 1.8), (3, 1.8)]
    
    for i, ((title, color, desc), (x, y)) in enumerate(zip(responsibilities, positions)):
        # 方框
        box = FancyBboxPatch((x-0.9, y-0.6), 1.8, 1.2, boxstyle="round,pad=0.05",
                             facecolor=color, edgecolor='white', linewidth=2, alpha=0.95)
        ax.add_patch(box)
        
        # 序号徽章
        num_circle = Circle((x-0.6, y+0.3), 0.2, facecolor='white', edgecolor=color, linewidth=2)
        ax.add_patch(num_circle)
        ax.text(x-0.6, y+0.3, str(i+1), fontsize=10, ha='center', va='center', 
                color=color, fontweight='bold')
        
        # 标题和描述
        ax.text(x, y+0.1, title, fontsize=10, fontproperties=chinese_font_bold, ha='center', va='center', color='white')
        ax.text(x, y-1.1, desc, fontsize=9, fontproperties=chinese_font, ha='center', va='top', color='#555')
    
    save_fig(fig, 'fig4_five_responsibilities.png')

def fig5_success_vs_failure():
    """图5: AI转型成功路径 vs 失败路径对比"""
    fig, ax = plt.subplots(1, 1, figsize=(12, 7))
    ax.set_xlim(0, 12)
    ax.set_ylim(0, 7)
    ax.axis('off')
    
    # 标题
    ax.text(6, 6.5, '有架构师 vs 无架构师：AI 转型结果对比', fontsize=16, 
            fontproperties=chinese_font_bold, ha='center', color='#333333')
    
    # 左侧 - 失败（无架构师）
    ax.text(3, 5.8, '无 架 构 师', fontsize=13, fontproperties=chinese_font_bold, 
            ha='center', color='#C92A2A')
    
    failure_steps = [
        ('第 1 月', '混乱开始', '#FF8787'),
        ('第 3 月', '技术债爆发', '#FF6B6B'),
        ('第 6 月', '安全危机', '#FA5252'),
        ('第 9 月', '项目失败', '#E03131'),
    ]
    
    for i, (month, desc, color) in enumerate(failure_steps):
        y = 4.8 - i * 1.1
        box = FancyBboxPatch((1, y-0.35), 4, 0.7, boxstyle="round,pad=0.02",
                             facecolor=color, edgecolor='white', linewidth=1, alpha=0.9)
        ax.add_patch(box)
        ax.text(3, y+0.1, month, fontsize=10, fontproperties=chinese_font_bold, ha='center', color='white')
        ax.text(3, y-0.15, desc, fontsize=9, fontproperties=chinese_font, ha='center', color='white')
        
        if i < len(failure_steps) - 1:
            ax.annotate('', xy=(3, y-0.45), xytext=(3, y-0.7),
                        arrowprops=dict(arrowstyle='->', color='#C92A2A', lw=2))
    
    ax.text(3, 0.5, '结果：项目放弃\n损失：9个月 + 错失机会', 
            fontsize=10, fontproperties=chinese_font_bold, ha='center', color='#C92A2A')
    
    # 分隔线
    ax.plot([6, 6], [0.5, 6], '--', color='#CCC', linewidth=2)
    
    # 右侧 - 成功（有架构师）
    ax.text(9, 5.8, '有 架 构 师', fontsize=13, fontproperties=chinese_font_bold, 
            ha='center', color='#2F9E44')
    
    success_steps = [
        ('第 1 周', '架构设计', '#69DB7C'),
        ('第 1 月', '规范制定', '#51CF66'),
        ('第 2 月', '团队对齐', '#40C057'),
        ('第 4 月', '系统上线', '#2F9E44'),
    ]
    
    for i, (month, desc, color) in enumerate(success_steps):
        y = 4.8 - i * 1.1
        box = FancyBboxPatch((7, y-0.35), 4, 0.7, boxstyle="round,pad=0.02",
                             facecolor=color, edgecolor='white', linewidth=1, alpha=0.9)
        ax.add_patch(box)
        ax.text(9, y+0.1, month, fontsize=10, fontproperties=chinese_font_bold, ha='center', color='white')
        ax.text(9, y-0.15, desc, fontsize=9, fontproperties=chinese_font, ha='center', color='white')
        
        if i < len(success_steps) - 1:
            ax.annotate('', xy=(9, y-0.45), xytext=(9, y-0.7),
                        arrowprops=dict(arrowstyle='->', color='#2F9E44', lw=2))
    
    ax.text(9, 0.5, '结果：4个月成功上线\n收益：效率全面提升', 
            fontsize=10, fontproperties=chinese_font_bold, ha='center', color='#2F9E44')
    
    save_fig(fig, 'fig5_success_vs_failure.png')

if __name__ == '__main__':
    os.makedirs(ASSETS_DIR, exist_ok=True)
    print("正在生成中文配图...")
    
    fig1_isolated_agents()
    fig2_layered_architecture()
    fig3_architect_responsibilities()
    fig4_five_responsibilities()
    fig5_success_vs_failure()
    
    print("\n所有中文配图生成完成！")
    print(f"保存位置: {ASSETS_DIR}")

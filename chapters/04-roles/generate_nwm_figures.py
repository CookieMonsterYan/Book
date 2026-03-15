#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
第4章NWM架构案例配图生成脚本
"""

import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
from matplotlib.patches import FancyBboxPatch, Circle, Rectangle, FancyArrowPatch, Polygon
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

# ============ 图1: NWM三层架构详细图 ============
def create_nwm_three_layer_architecture():
    """创建NWM三层架构详细图"""
    fig, ax = plt.subplots(figsize=(16, 12))
    
    # 标题
    ax.text(0.5, 0.97, '美国国家水模型（NWM）三层架构', ha='center', va='top',
           fontsize=18, fontweight='bold', transform=ax.transAxes)
    ax.text(0.5, 0.94, 'National Water Model Architecture', ha='center', va='top',
           fontsize=12, color='#666666', transform=ax.transAxes)
    
    # 第一层：数据输入层
    layer1_rect = FancyBboxPatch((0.05, 0.75), 0.9, 0.15, boxstyle="round,pad=0.02",
                                 facecolor='#E3F2FD', edgecolor='#1976D2', linewidth=3,
                                 transform=ax.transAxes)
    ax.add_patch(layer1_rect)
    ax.text(0.5, 0.87, '数据输入层 (Data Input Layer)', ha='center', va='center',
           fontsize=14, fontweight='bold', color='#1565C0', transform=ax.transAxes)
    
    # 数据输入组件
    inputs = [
        {'name': 'MRMS\n雷达降雨', 'x': 0.15, 'color': '#64B5F6'},
        {'name': 'HRRR\n快速预报', 'x': 0.32, 'color': '#64B5F6'},
        {'name': 'GFS/CFS\n全球预报', 'x': 0.49, 'color': '#64B5F6'},
        {'name': 'USGS\n水文观测', 'x': 0.66, 'color': '#81C784'},
        {'name': '水库调度\n数据', 'x': 0.83, 'color': '#81C784'},
    ]
    
    for inp in inputs:
        rect = FancyBboxPatch((inp['x']-0.07, 0.77), 0.14, 0.08, boxstyle="round,pad=0.01",
                              facecolor=inp['color'], edgecolor='black', linewidth=1.5,
                              transform=ax.transAxes)
        ax.add_patch(rect)
        ax.text(inp['x'], 0.81, inp['name'], ha='center', va='center',
               fontsize=8, color='white', fontweight='bold', transform=ax.transAxes)
    
    # 第二层：模型核心层
    layer2_rect = FancyBboxPatch((0.05, 0.45), 0.9, 0.25, boxstyle="round,pad=0.02",
                                 facecolor='#FFF3E0', edgecolor='#F57C00', linewidth=3,
                                 transform=ax.transAxes)
    ax.add_patch(layer2_rect)
    ax.text(0.5, 0.67, '模型核心层 (Model Core Layer) - WRF-Hydro', ha='center', va='center',
           fontsize=14, fontweight='bold', color='#E65100', transform=ax.transAxes)
    
    # 核心组件
    components = [
        {'name': 'Noah-MP\n陆面模型', 'desc': '1km分辨率\n产流计算', 'x': 0.18, 'color': '#FFB74D'},
        {'name': '地表径流\n模块', 'desc': '250m分辨率\n栅格路由', 'x': 0.40, 'color': '#FFB74D'},
        {'name': '地下水流\n模块', 'desc': '饱和地下水\n流计算', 'x': 0.62, 'color': '#FFB74D'},
        {'name': '河道汇流\n模块', 'desc': 'Muskingum-Cunge\n270万断面', 'x': 0.84, 'color': '#FF9800'},
    ]
    
    for comp in components:
        rect = FancyBboxPatch((comp['x']-0.09, 0.48), 0.18, 0.14, boxstyle="round,pad=0.01",
                              facecolor=comp['color'], edgecolor='black', linewidth=1.5,
                              transform=ax.transAxes)
        ax.add_patch(rect)
        ax.text(comp['x'], 0.58, comp['name'], ha='center', va='center',
               fontsize=9, fontweight='bold', color='white', transform=ax.transAxes)
        ax.text(comp['x'], 0.52, comp['desc'], ha='center', va='center',
               fontsize=7, color='white', transform=ax.transAxes)
    
    # 数据同化物
    da_rect = FancyBboxPatch((0.35, 0.455), 0.3, 0.04, boxstyle="round,pad=0.01",
                             facecolor='#E91E63', edgecolor='black', linewidth=1.5,
                             transform=ax.transAxes)
    ax.add_patch(da_rect)
    ax.text(0.5, 0.475, '数据同化 (EnKF) - 融合USGS观测数据', ha='center', va='center',
           fontsize=9, color='white', fontweight='bold', transform=ax.transAxes)
    
    # 第三层：产品输出层
    layer3_rect = FancyBboxPatch((0.05, 0.15), 0.9, 0.25, boxstyle="round,pad=0.02",
                                 facecolor='#E8F5E9', edgecolor='#388E3C', linewidth=3,
                                 transform=ax.transAxes)
    ax.add_patch(layer3_rect)
    ax.text(0.5, 0.37, '产品输出层 (Product Output Layer)', ha='center', va='center',
           fontsize=14, fontweight='bold', color='#2E7D32', transform=ax.transAxes)
    
    # 产品类型
    products = [
        {'name': '分析同化\n(Analysis)', 'desc': '0-3h回溯\n每小时', 'x': 0.15, 'color': '#81C784'},
        {'name': '短期预报\n(Short-Range)', 'desc': '0-18h\n每小时', 'x': 0.38, 'color': '#66BB6A'},
        {'name': '中期预报\n(Medium-Range)', 'desc': '0-10天\n每6小时', 'x': 0.61, 'color': '#4CAF50'},
        {'name': '长期集合预报\n(Long-Range)', 'desc': '0-30天\n16成员', 'x': 0.84, 'color': '#43A047'},
    ]
    
    for prod in products:
        rect = FancyBboxPatch((prod['x']-0.09, 0.18), 0.18, 0.14, boxstyle="round,pad=0.01",
                              facecolor=prod['color'], edgecolor='black', linewidth=1.5,
                              transform=ax.transAxes)
        ax.add_patch(rect)
        ax.text(prod['x'], 0.28, prod['name'], ha='center', va='center',
               fontsize=8, fontweight='bold', color='white', transform=ax.transAxes)
        ax.text(prod['x'], 0.22, prod['desc'], ha='center', va='center',
               fontsize=7, color='white', transform=ax.transAxes)
    
    # 连接箭头
    for y in [0.75, 0.45]:
        ax.arrow(0.5, y, 0, -0.03, head_width=0.02, head_length=0.02,
                fc='#666666', ec='#666666', transform=ax.transAxes)
    
    # 技术规格标注
    specs = FancyBboxPatch((0.05, 0.02), 0.9, 0.1, boxstyle="round,pad=0.02",
                           facecolor='#F5F5F5', edgecolor='#9E9E9E', linewidth=1,
                           transform=ax.transAxes)
    ax.add_patch(specs)
    ax.text(0.5, 0.08, '技术规格：270万河道断面 | 每日4.45TB输入 | 每日3TB输出 | >100,000 CPU-hours/天',
           ha='center', va='center', fontsize=9, transform=ax.transAxes)
    ax.text(0.5, 0.04, '覆盖范围：美国大陆(CONUS) + 阿拉斯加 + 夏威夷 | 分辨率：250m-1km | 运行时间：2016年8月至今',
           ha='center', va='center', fontsize=8, color='#666666', transform=ax.transAxes)
    
    ax.set_xlim(0, 1)
    ax.set_ylim(0, 1)
    ax.axis('off')
    
    save_fig(fig, 'fig_4_2_nwm_detailed_architecture.png')

# ============ 图2: NWM数据流图 ============
def create_nwm_data_flow():
    """创建NWM数据流图"""
    fig, ax = plt.subplots(figsize=(16, 10))
    
    ax.set_xlim(0, 10)
    ax.set_ylim(0, 10)
    ax.axis('off')
    ax.set_title('NWM数据流与处理流程', fontsize=18, fontweight='bold', pad=20)
    
    # 数据源
    sources = [
        {'name': '雷达观测\n(MRMS)', 'x': 1, 'y': 8.5, 'color': '#2196F3'},
        {'name': '数值预报\n(HRRR/GFS)', 'x': 3, 'y': 8.5, 'color': '#2196F3'},
        {'name': '地面观测\n(USGS)', 'x': 5, 'y': 8.5, 'color': '#4CAF50'},
        {'name': '卫星数据', 'x': 7, 'y': 8.5, 'color': '#9C27B0'},
        {'name': '水库调度', 'x': 9, 'y': 8.5, 'color': '#FF9800'},
    ]
    
    for src in sources:
        rect = FancyBboxPatch((src['x']-0.6, src['y']-0.4), 1.2, 0.8, boxstyle="round,pad=0.05",
                              facecolor=src['color'], edgecolor='black', linewidth=2)
        ax.add_patch(rect)
        ax.text(src['x'], src['y'], src['name'], ha='center', va='center',
               fontsize=9, fontweight='bold', color='white')
    
    # 数据采集与预处理
    preprocess = FancyBboxPatch((0.5, 6.5), 9, 1.2, boxstyle="round,pad=0.05",
                                facecolor='#E3F2FD', edgecolor='#1976D2', linewidth=2)
    ax.add_patch(preprocess)
    ax.text(5, 7.4, '数据采集与预处理', ha='center', va='center', fontsize=12, fontweight='bold')
    ax.text(5, 7.0, '格式转换 | 质量控制 | 空间插值 | 时间对齐', ha='center', va='center', fontsize=9)
    
    # 箭头
    for x in [1, 3, 5, 7, 9]:
        ax.arrow(x, 8.1, 0, -0.3, head_width=0.2, head_length=0.15, fc='#666666', ec='#666666')
    
    # 模型计算
    model_box = FancyBboxPatch((0.5, 3.5), 9, 2.5, boxstyle="round,pad=0.05",
                               facecolor='#FFF3E0', edgecolor='#F57C00', linewidth=3)
    ax.add_patch(model_box)
    ax.text(5, 5.7, 'WRF-Hydro模型计算', ha='center', va='center', fontsize=13, fontweight='bold', color='#E65100')
    
    # 模型内部流程
    model_steps = [
        {'name': '陆面过程\n产流计算', 'x': 2, 'color': '#FFB74D'},
        {'name': '地表径流\n栅格路由', 'x': 4, 'color': '#FFB74D'},
        {'name': '河道汇流\n断面演算', 'x': 6, 'color': '#FFA726'},
        {'name': '数据同化\n状态更新', 'x': 8, 'color': '#FF9800'},
    ]
    
    for i, step in enumerate(model_steps):
        rect = FancyBboxPatch((step['x']-0.7, 3.8), 1.4, 1.4, boxstyle="round,pad=0.05",
                              facecolor=step['color'], edgecolor='black', linewidth=1.5)
        ax.add_patch(rect)
        ax.text(step['x'], 4.7, step['name'], ha='center', va='center',
               fontsize=9, fontweight='bold', color='white')
        if i < len(model_steps) - 1:
            ax.arrow(step['x']+0.7, 4.5, 0.6, 0, head_width=0.15, head_length=0.2, 
                    fc='#666666', ec='#666666')
    
    # 向下箭头
    ax.arrow(5, 6.5, 0, -0.3, head_width=0.2, head_length=0.15, fc='#666666', ec='#666666')
    ax.arrow(5, 3.5, 0, -0.3, head_width=0.2, head_length=0.15, fc='#666666', ec='#666666')
    
    # 产品生成
    products = FancyBboxPatch((0.5, 1.5), 9, 1.2, boxstyle="round,pad=0.05",
                              facecolor='#E8F5E9', edgecolor='#388E3C', linewidth=2)
    ax.add_patch(products)
    ax.text(5, 2.4, '预报产品生成', ha='center', va='center', fontsize=12, fontweight='bold', color='#2E7D32')
    ax.text(5, 2.0, '短期(0-18h) | 中期(0-10d) | 长期集合(0-30d) | 分析同化(0-3h)', 
           ha='center', va='center', fontsize=9)
    
    # 最终输出
    outputs = FancyBboxPatch((0.5, 0.2), 9, 0.8, boxstyle="round,pad=0.05",
                             facecolor='#F3E5F5', edgecolor='#7B1FA2', linewidth=2)
    ax.add_patch(outputs)
    ax.text(5, 0.7, '产品分发与服务', ha='center', va='center', fontsize=11, fontweight='bold')
    ax.text(5, 0.4, 'NOAA网站 | API接口 | 数据下载 | 可视化平台', ha='center', va='center', fontsize=9)
    
    save_fig(fig, 'fig_4_2_nwm_data_flow.png')

# ============ 图3: NWM架构演进时间线 ============
def create_nwm_evolution_timeline():
    """创建NWM架构演进时间线"""
    fig, ax = plt.subplots(figsize=(16, 10))
    
    ax.set_xlim(0, 10)
    ax.set_ylim(0, 10)
    ax.axis('off')
    ax.set_title('NWM架构演进历程 (2016-2023)', fontsize=18, fontweight='bold', pad=20)
    
    # 时间轴
    ax.plot([1, 9], [5, 5], 'k-', linewidth=3)
    
    versions = [
        {
            'version': 'V1.0',
            'date': '2016.8',
            'x': 1.5,
            'y': 7,
            'features': ['基础框架', '270万断面', '3种预报产品'],
            'color': '#E3F2FD',
            'border': '#1976D2'
        },
        {
            'version': 'V1.1',
            'date': '2017.5',
            'x': 3,
            'y': 3,
            'features': ['提升循环频率', '增加预报长度', '初始校准'],
            'color': '#E8F5E9',
            'border': '#388E3C'
        },
        {
            'version': 'V2.0',
            'date': '2018初',
            'x': 4.5,
            'y': 7,
            'features': ['HydroFabric重构', '大规模校准', '改进数据同化'],
            'color': '#FFF3E0',
            'border': '#F57C00'
        },
        {
            'version': 'V2.1',
            'date': '2019.5',
            'x': 6,
            'y': 3,
            'features': ['扩展至夏威夷', '中期集合预报', '改进物理过程'],
            'color': '#FCE4EC',
            'border': '#C2185B'
        },
        {
            'version': 'V3.0\n(NextGen)',
            'date': '2021-2023',
            'x': 8,
            'y': 7,
            'features': ['NextGen框架', 'BMI接口', '深度学习集成'],
            'color': '#E1F5FE',
            'border': '#0288D1'
        },
    ]
    
    for ver in versions:
        # 节点
        circle = Circle((ver['x'], 5), 0.15, facecolor=ver['border'], edgecolor='black', linewidth=2)
        ax.add_patch(circle)
        
        # 连接线
        ax.plot([ver['x'], ver['x']], [5.15, ver['y']-0.3], 'k--', linewidth=1.5, alpha=0.5)
        
        # 版本框
        rect = FancyBboxPatch((ver['x']-0.6, ver['y']-1.2), 1.2, 1.8, boxstyle="round,pad=0.05",
                              facecolor=ver['color'], edgecolor=ver['border'], linewidth=2)
        ax.add_patch(rect)
        
        # 版本信息
        ax.text(ver['x'], ver['y']+0.3, ver['version'], ha='center', va='center',
               fontsize=12, fontweight='bold')
        ax.text(ver['x'], ver['y']+0.05, ver['date'], ha='center', va='center',
               fontsize=9, color='#666666')
        
        # 特性列表
        for i, feat in enumerate(ver['features']):
            ax.text(ver['x'], ver['y']-0.3-i*0.25, f'• {feat}', ha='center', va='center',
                   fontsize=8)
    
    # 演进方向
    ax.annotate('', xy=(9.2, 5), xytext=(0.8, 5),
               arrowprops=dict(arrowstyle='->', lw=4, color='#FF5722'))
    ax.text(5, 5.5, '演进方向 →', ha='center', va='center',
           fontsize=14, fontweight='bold', color='#FF5722')
    
    save_fig(fig, 'fig_4_2_nwm_evolution_timeline.png')

# ============ 图4: NWM空间覆盖示意图 ============
def create_nwm_spatial_coverage():
    """创建NWM空间覆盖示意图"""
    fig, ax = plt.subplots(figsize=(14, 10))
    
    ax.set_xlim(0, 10)
    ax.set_ylim(0, 10)
    ax.axis('off')
    ax.set_title('NWM空间覆盖与分辨率对比', fontsize=18, fontweight='bold', pad=20)
    
    # 美国地图轮廓（简化示意）
    # 主体
    us_main = Polygon([(2, 3), (7, 3), (7.5, 6), (6.5, 7.5), (5, 8), (3, 7), (2, 5)], 
                      facecolor='#E3F2FD', edgecolor='#1976D2', linewidth=3)
    ax.add_patch(us_main)
    ax.text(4.5, 5.5, '美国大陆\n(CONUS)', ha='center', va='center', fontsize=14, fontweight='bold')
    ax.text(4.5, 4.8, '270万河道断面', ha='center', va='center', fontsize=11, color='#1565C0')
    
    # 阿拉斯加
    alaska = Polygon([(0.5, 7), (1.8, 7.5), (1.5, 8.5), (0.3, 8)], 
                     facecolor='#C8E6C9', edgecolor='#388E3C', linewidth=2)
    ax.add_patch(alaska)
    ax.text(1, 7.8, '阿拉斯加', ha='center', va='center', fontsize=9)
    
    # 夏威夷
    hawaii = Circle((1.5, 1.5), 0.4, facecolor='#FFF3E0', edgecolor='#F57C00', linewidth=2)
    ax.add_patch(hawaii)
    ax.text(1.5, 1.5, '夏威夷', ha='center', va='center', fontsize=8)
    
    # 分辨率对比框
    res_box = FancyBboxPatch((7.5, 1), 2, 4, boxstyle="round,pad=0.05",
                             facecolor='#F5F5F5', edgecolor='#616161', linewidth=2)
    ax.add_patch(res_box)
    ax.text(8.5, 4.7, '空间分辨率', ha='center', va='center', fontsize=11, fontweight='bold')
    
    resolutions = [
        {'name': '陆面模型', 'res': '1km', 'y': 4},
        {'name': '地表径流', 'res': '250m', 'y': 3.2},
        {'name': '河道断面', 'res': 'NHDPlus', 'y': 2.4},
    ]
    
    for r in resolutions:
        ax.text(8, r['y'], r['name'], ha='left', va='center', fontsize=9)
        ax.text(9.3, r['y'], r['res'], ha='right', va='center', fontsize=9, 
               fontweight='bold', color='#1976D2')
    
    # 对比传统RFC
    compare_box = FancyBboxPatch((0.5, 0.3), 6, 1.8, boxstyle="round,pad=0.05",
                                 facecolor='#FFF8E1', edgecolor='#FFC107', linewidth=2)
    ax.add_patch(compare_box)
    ax.text(3.5, 1.8, '对比：传统RFC vs NWM', ha='center', va='center', fontsize=11, fontweight='bold')
    ax.text(1.5, 1.2, '传统RFC:\n约4,000个测站', ha='center', va='center', fontsize=9)
    ax.text(3.5, 1.2, '→', ha='center', va='center', fontsize=20, color='#FF5722')
    ax.text(5.5, 1.2, 'NWM:\n2,700,000个断面', ha='center', va='center', fontsize=9, 
           fontweight='bold', color='#1976D2')
    ax.text(3.5, 0.6, '覆盖率提升约675倍', ha='center', va='center', fontsize=10, 
           color='#D32F2F', fontweight='bold')
    
    save_fig(fig, 'fig_4_2_nwm_spatial_coverage.png')

# ============ 图5: 架构决策对比图 ============
def create_architecture_decision_comparison():
    """创建架构决策对比图"""
    fig, axes = plt.subplots(2, 2, figsize=(16, 12))
    
    decisions = [
        {
            'title': '决策1: 模型核心选择',
            'option_a': '方案A\n全新开发',
            'pros_a': ['完全自主可控', '量身定制'],
            'cons_a': ['周期长(2-3年)', '风险高', '验证难'],
            'option_b': '方案B\n基于WRF-Hydro',
            'pros_b': ['成熟框架', '社区支持', '可扩展'],
            'cons_b': ['需要适配改造'],
            'choice': 'B',
            'reason': '降低风险，加速上线'
        },
        {
            'title': '决策2: 空间数据结构',
            'option_a': '方案A\n栅格河网',
            'pros_a': ['计算简单', '易于并行'],
            'cons_a': ['与真实地形偏差大'],
            'option_b': '方案B\nNHDPlus矢量河网',
            'pros_b': ['真实河网拓扑', '属性丰富', '与观测关联'],
            'cons_b': ['数据处理复杂'],
            'choice': 'B',
            'reason': '精度优先，数据质量决定模型效果'
        },
        {
            'title': '决策3: 计算架构',
            'option_a': '方案A\n单机计算',
            'pros_a': ['部署简单', '成本低'],
            'cons_a': ['无法处理270万断面', '时效性无法满足'],
            'option_b': '方案B\n分布式超算',
            'pros_b': ['可扩展', '满足时效', '支撑业务化'],
            'cons_b': ['基础设施投入大'],
            'choice': 'B',
            'reason': '业务化运行的必要条件'
        },
        {
            'title': '决策4: 数据同化策略',
            'option_a': '方案A\n直接替换',
            'pros_a': ['实现简单'],
            'cons_a': ['容易不稳定', '物理一致性差'],
            'option_b': '方案B\nEnKF集合同化',
            'pros_b': ['保持物理一致性', '量化不确定性', '稳定性好'],
            'cons_b': ['计算量增加16倍'],
            'choice': 'B',
            'reason': '精度和稳定性优先'
        },
    ]
    
    for idx, (ax, decision) in enumerate(zip(axes.flat, decisions)):
        ax.set_xlim(0, 10)
        ax.set_ylim(0, 10)
        ax.axis('off')
        ax.set_title(decision['title'], fontsize=12, fontweight='bold', pad=10)
        
        # 方案A
        rect_a = FancyBboxPatch((0.5, 5.5), 4, 3.5, boxstyle="round,pad=0.1",
                                facecolor='#FFEBEE', edgecolor='#E57373', linewidth=2)
        ax.add_patch(rect_a)
        ax.text(2.5, 8.6, decision['option_a'], ha='center', va='center', fontsize=10, fontweight='bold')
        ax.text(2.5, 7.8, '优点:', ha='center', va='center', fontsize=8, color='#2E7D32')
        for i, pro in enumerate(decision['pros_a']):
            ax.text(2.5, 7.3-i*0.4, f'+ {pro}', ha='center', va='center', fontsize=7)
        ax.text(2.5, 6.3, '缺点:', ha='center', va='center', fontsize=8, color='#C62828')
        for i, con in enumerate(decision['cons_a']):
            ax.text(2.5, 5.8-i*0.4, f'- {con}', ha='center', va='center', fontsize=7)
        
        # 方案B (选中)
        rect_b = FancyBboxPatch((5.5, 5.5), 4, 3.5, boxstyle="round,pad=0.1",
                                facecolor='#E8F5E9', edgecolor='#4CAF50', linewidth=3)
        ax.add_patch(rect_b)
        ax.text(7.5, 8.6, decision['option_b'], ha='center', va='center', fontsize=10, fontweight='bold')
        ax.text(7.5, 7.8, '优点:', ha='center', va='center', fontsize=8, color='#2E7D32')
        for i, pro in enumerate(decision['pros_b']):
            ax.text(7.5, 7.3-i*0.4, f'+ {pro}', ha='center', va='center', fontsize=7)
        ax.text(7.5, 5.8, '缺点:', ha='center', va='center', fontsize=8, color='#C62828')
        for i, con in enumerate(decision['cons_b']):
            ax.text(7.5, 5.3-i*0.4, f'- {con}', ha='center', va='center', fontsize=7)
        
        # 选中标记
        ax.text(7.5, 9.2, '✓ 选中', ha='center', va='center', fontsize=11, 
               fontweight='bold', color='#4CAF50')
        
        # 决策理由
        reason_box = FancyBboxPatch((0.5, 0.5), 9, 1.8, boxstyle="round,pad=0.1",
                                    facecolor='#FFF8E1', edgecolor='#FFC107', linewidth=1.5)
        ax.add_patch(reason_box)
        ax.text(5, 1.9, '决策理由', ha='center', va='center', fontsize=9, fontweight='bold')
        ax.text(5, 1.2, decision['reason'], ha='center', va='center', fontsize=9)
    
    plt.tight_layout()
    save_fig(fig, 'fig_4_2_nwm_architecture_decisions.png')

# ============ 主函数 ============
def main():
    print("开始生成第4章NWM架构配图...")
    print(f"输出目录: {output_dir}")
    
    create_nwm_three_layer_architecture()
    create_nwm_data_flow()
    create_nwm_evolution_timeline()
    create_nwm_spatial_coverage()
    create_architecture_decision_comparison()
    
    print("\n所有NWM架构配图生成完成!")

if __name__ == '__main__':
    main()

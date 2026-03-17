#!/usr/bin/env python3
"""Generate WeChat article illustrations for OpenClaw Architect article."""

import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
from matplotlib.patches import FancyBboxPatch, Circle, Rectangle, FancyArrowPatch
import numpy as np
import os

# Set Chinese font
plt.rcParams['font.sans-serif'] = ['DejaVu Sans', 'SimHei', 'Arial Unicode MS', 'sans-serif']
plt.rcParams['axes.unicode_minus'] = False

ASSETS_DIR = "/root/.openclaw/workspace/HEBook/articles/assets"

def save_fig(fig, filename):
    filepath = os.path.join(ASSETS_DIR, filename)
    fig.savefig(filepath, dpi=150, bbox_inches='tight', facecolor='white', edgecolor='none')
    plt.close(fig)
    print(f"Generated: {filepath}")

def fig1_isolated_agents():
    """图1: 各自为战的混乱局面 - 三个独立的Agent孤岛"""
    fig, ax = plt.subplots(1, 1, figsize=(10, 6))
    ax.set_xlim(0, 10)
    ax.set_ylim(0, 6)
    ax.axis('off')
    
    # Title
    ax.text(5, 5.5, 'No Architecture = Chaos', fontsize=16, fontweight='bold', 
            ha='center', color='#333333')
    ax.text(5, 5.1, 'Three Agents Working in Isolation', fontsize=11, 
            ha='center', color='#666666')
    
    # Agent A - Data Cleaning (left)
    box_a = FancyBboxPatch((0.5, 2.5), 2.2, 2, boxstyle="round,pad=0.05", 
                           facecolor='#FF6B6B', edgecolor='#C92A2A', linewidth=2, alpha=0.9)
    ax.add_patch(box_a)
    ax.text(1.6, 3.8, 'Agent A', fontsize=12, fontweight='bold', ha='center', color='white')
    ax.text(1.6, 3.3, 'Data Cleaning', fontsize=10, ha='center', color='white')
    ax.text(1.6, 2.8, 'Python + CSV', fontsize=9, ha='center', color='#FFE0E0')
    
    # Agent B - Validation (center)
    box_b = FancyBboxPatch((3.8, 2.5), 2.2, 2, boxstyle="round,pad=0.05",
                           facecolor='#4ECDC4', edgecolor='#087F5B', linewidth=2, alpha=0.9)
    ax.add_patch(box_b)
    ax.text(4.9, 3.8, 'Agent B', fontsize=12, fontweight='bold', ha='center', color='white')
    ax.text(4.9, 3.3, 'Validation', fontsize=10, ha='center', color='white')
    ax.text(4.9, 2.8, 'JavaScript + JSON', fontsize=9, ha='center', color='#E0F7F5')
    
    # Agent C - Report (right)
    box_c = FancyBboxPatch((7.1, 2.5), 2.2, 2, boxstyle="round,pad=0.05",
                           facecolor='#95E1D3', edgecolor='#2B8A3E', linewidth=2, alpha=0.9)
    ax.add_patch(box_c)
    ax.text(8.2, 3.8, 'Agent C', fontsize=12, fontweight='bold', ha='center', color='#333')
    ax.text(8.2, 3.3, 'Report Gen', fontsize=10, ha='center', color='#333')
    ax.text(8.2, 2.8, 'GPT API + String', fontsize=9, ha='center', color='#555')
    
    # Confusion indicators (crossed lines)
    ax.annotate('', xy=(3.8, 3.5), xytext=(2.7, 3.5),
                arrowprops=dict(arrowstyle='<->', color='#FF6B6B', lw=2, ls='--'))
    ax.annotate('', xy=(7.1, 3.5), xytext=(6.0, 3.5),
                arrowprops=dict(arrowstyle='<->', color='#FF6B6B', lw=2, ls='--'))
    
    # Warning icons
    ax.text(1.6, 1.8, 'X Cannot communicate', fontsize=9, ha='center', color='#C92A2A', fontweight='bold')
    ax.text(4.9, 1.8, 'X Different formats', fontsize=9, ha='center', color='#C92A2A', fontweight='bold')
    ax.text(8.2, 1.8, 'X No integration', fontsize=9, ha='center', color='#C92A2A', fontweight='bold')
    
    save_fig(fig, 'fig1_isolated_agents.png')

def fig2_layered_architecture():
    """图2: 分层架构设计示意图 - 三层架构"""
    fig, ax = plt.subplots(1, 1, figsize=(10, 7))
    ax.set_xlim(0, 10)
    ax.set_ylim(0, 7)
    ax.axis('off')
    
    # Title
    ax.text(5, 6.5, 'Clean Layered Architecture', fontsize=16, fontweight='bold', 
            ha='center', color='#333333')
    
    # Layer 3: Application Layer
    layer3 = FancyBboxPatch((1, 4.8), 8, 1.4, boxstyle="round,pad=0.05",
                            facecolor='#4DABF7', edgecolor='#1971C2', linewidth=2)
    ax.add_patch(layer3)
    ax.text(5, 5.8, 'Application Layer', fontsize=13, fontweight='bold', ha='center', color='white')
    ax.text(5, 5.3, 'Data Agent | Modeling Agent | Report Agent', fontsize=10, ha='center', color='white')
    
    # Arrow down
    ax.annotate('', xy=(5, 4.6), xytext=(5, 4.8),
                arrowprops=dict(arrowstyle='->', color='#666', lw=2))
    
    # Layer 2: Service Layer
    layer2 = FancyBboxPatch((1, 3.0), 8, 1.4, boxstyle="round,pad=0.05",
                            facecolor='#69DB7C', edgecolor='#2F9E44', linewidth=2)
    ax.add_patch(layer2)
    ax.text(5, 4.0, 'Service Layer', fontsize=13, fontweight='bold', ha='center', color='white')
    ax.text(5, 3.5, 'LLM Service | Data Service | Auth Service', fontsize=10, ha='center', color='white')
    
    # Arrow down
    ax.annotate('', xy=(5, 2.8), xytext=(5, 3.0),
                arrowprops=dict(arrowstyle='->', color='#666', lw=2))
    
    # Layer 1: Data Layer
    layer1 = FancyBboxPatch((1, 1.2), 8, 1.4, boxstyle="round,pad=0.05",
                            facecolor='#FFD43B', edgecolor='#F08C00', linewidth=2)
    ax.add_patch(layer1)
    ax.text(5, 2.2, 'Data Layer', fontsize=13, fontweight='bold', ha='center', color='#333')
    ax.text(5, 1.7, 'Project DB | Knowledge Base | Model Store', fontsize=10, ha='center', color='#333')
    
    # Benefits
    benefits = ['[OK] Clear interfaces', '[OK] Standardized protocols', '[OK] Easy to maintain']
    for i, benefit in enumerate(benefits):
        ax.text(5, 0.5 - i*0.35, benefit, fontsize=10, ha='center', color='#2B8A3E', fontweight='bold')
    
    save_fig(fig, 'fig2_layered_architecture.png')

def fig3_architect_responsibilities():
    """图3: AI时代架构师的核心职责"""
    fig, ax = plt.subplots(1, 1, figsize=(10, 7))
    ax.set_xlim(0, 10)
    ax.set_ylim(0, 7)
    ax.axis('off')
    
    # Title
    ax.text(5, 6.5, 'AI Era: Architect is More Critical Than Ever', fontsize=16, 
            fontweight='bold', ha='center', color='#333333')
    
    # Central circle - Architect
    center_circle = Circle((5, 3.5), 1.2, facecolor='#7950F2', edgecolor='#5F3DC4', linewidth=3)
    ax.add_patch(center_circle)
    ax.text(5, 3.7, 'ARCHITECT', fontsize=11, fontweight='bold', ha='center', color='white')
    ax.text(5, 3.2, 'Decision Maker', fontsize=9, ha='center', color='#E0D4FC')
    
    # Surrounding responsibilities
    responsibilities = [
        ('System\nIntegration', 2, 5.5, '#FF6B6B'),
        ('Security &\nCompliance', 8, 5.5, '#4ECDC4'),
        ('Quality\nStandards', 1.2, 3.5, '#FFD93D'),
        ('Tech\nSelection', 8.8, 3.5, '#6BCF7F'),
        ('Long-term\nMaintenance', 2, 1.5, '#A78BFA'),
        ('Team\nEnablement', 8, 1.5, '#FF8F8F'),
    ]
    
    for text, x, y, color in responsibilities:
        # Draw small circle
        small_circle = Circle((x, y), 0.7, facecolor=color, edgecolor='white', linewidth=2)
        ax.add_patch(small_circle)
        ax.text(x, y, text, fontsize=8, ha='center', va='center', color='white', fontweight='bold')
        
        # Draw connection to center
        ax.annotate('', xy=(5 + (x-5)*0.25, 3.5 + (y-3.5)*0.25), xytext=(x, y),
                    arrowprops=dict(arrowstyle='->', color='#999', lw=1.5, connectionstyle='arc3,rad=0.1'))
    
    # Bottom text
    ax.text(5, 0.5, 'AI Writes Code -> Architect Makes It Work', fontsize=12, 
            ha='center', color='#5F3DC4', fontweight='bold')
    
    save_fig(fig, 'fig3_architect_responsibilities.png')

def fig4_five_responsibilities():
    """图4: 架构师的5个核心职责"""
    fig, ax = plt.subplots(1, 1, figsize=(10, 7))
    ax.set_xlim(0, 10)
    ax.set_ylim(0, 7)
    ax.axis('off')
    
    # Title
    ax.text(5, 6.5, "Architect's 5 Core Responsibilities", fontsize=16, 
            fontweight='bold', ha='center', color='#333333')
    
    # Pentagon layout for 5 responsibilities
    responsibilities = [
        ('Architecture\nDesign', '#FF6B6B', 'From "works" to "works well"'),
        ('Technology\nSelection', '#4ECDC4', 'Avoid "choice disasters"'),
        ('Security &\nCompliance', '#FFD93D', 'Guard the bottom line'),
        ('Quality\nStandards', '#6BCF7F', 'AI code needs review too'),
        ('Team\nEnablement', '#A78BFA', 'Make everyone effective'),
    ]
    
    positions = [(2, 4.5), (5, 5.5), (8, 4.5), (7, 1.8), (3, 1.8)]
    
    for i, ((title, color, desc), (x, y)) in enumerate(zip(responsibilities, positions)):
        # Draw box
        box = FancyBboxPatch((x-0.9, y-0.6), 1.8, 1.2, boxstyle="round,pad=0.05",
                             facecolor=color, edgecolor='white', linewidth=2, alpha=0.95)
        ax.add_patch(box)
        
        # Number badge
        num_circle = Circle((x-0.6, y+0.3), 0.2, facecolor='white', edgecolor=color, linewidth=2)
        ax.add_patch(num_circle)
        ax.text(x-0.6, y+0.3, str(i+1), fontsize=10, ha='center', va='center', 
                color=color, fontweight='bold')
        
        # Title and desc
        ax.text(x, y+0.1, title, fontsize=9, ha='center', va='center', color='white', fontweight='bold')
        ax.text(x, y-1.1, desc, fontsize=8, ha='center', va='top', color='#555')
    
    save_fig(fig, 'fig4_five_responsibilities.png')

def fig5_success_vs_failure():
    """图5: AI转型成功路径 vs 失败路径对比"""
    fig, ax = plt.subplots(1, 1, figsize=(12, 7))
    ax.set_xlim(0, 12)
    ax.set_ylim(0, 7)
    ax.axis('off')
    
    # Title
    ax.text(6, 6.5, 'With vs Without Architect: AI Transformation Outcomes', fontsize=16, 
            fontweight='bold', ha='center', color='#333333')
    
    # Left side - FAILURE (No Architect)
    ax.text(3, 5.8, 'WITHOUT ARCHITECT', fontsize=13, fontweight='bold', 
            ha='center', color='#C92A2A')
    
    failure_steps = [
        ('Month 1', 'Chaos begins', '#FF8787'),
        ('Month 3', 'Tech debt explodes', '#FF6B6B'),
        ('Month 6', 'Security crisis', '#FA5252'),
        ('Month 9', 'Project fails', '#E03131'),
    ]
    
    for i, (month, desc, color) in enumerate(failure_steps):
        y = 4.8 - i * 1.1
        # Box
        box = FancyBboxPatch((1, y-0.35), 4, 0.7, boxstyle="round,pad=0.02",
                             facecolor=color, edgecolor='white', linewidth=1, alpha=0.9)
        ax.add_patch(box)
        ax.text(3, y+0.1, month, fontsize=10, ha='center', color='white', fontweight='bold')
        ax.text(3, y-0.15, desc, fontsize=9, ha='center', color='white')
        
        # Arrow down
        if i < len(failure_steps) - 1:
            ax.annotate('', xy=(3, y-0.45), xytext=(3, y-0.7),
                        arrowprops=dict(arrowstyle='->', color='#C92A2A', lw=2))
    
    ax.text(3, 0.5, 'Result: Project abandoned\nLoss: 9 months + opportunity', 
            fontsize=10, ha='center', color='#C92A2A', fontweight='bold')
    
    # Divider
    ax.plot([6, 6], [0.5, 6], '--', color='#CCC', linewidth=2)
    
    # Right side - SUCCESS (With Architect)
    ax.text(9, 5.8, 'WITH ARCHITECT', fontsize=13, fontweight='bold', 
            ha='center', color='#2F9E44')
    
    success_steps = [
        ('Week 1', 'Architecture design', '#69DB7C'),
        ('Month 1', 'Standards set', '#51CF66'),
        ('Month 2', 'Team aligned', '#40C057'),
        ('Month 4', 'System live!', '#2F9E44'),
    ]
    
    for i, (month, desc, color) in enumerate(success_steps):
        y = 4.8 - i * 1.1
        # Box
        box = FancyBboxPatch((7, y-0.35), 4, 0.7, boxstyle="round,pad=0.02",
                             facecolor=color, edgecolor='white', linewidth=1, alpha=0.9)
        ax.add_patch(box)
        ax.text(9, y+0.1, month, fontsize=10, ha='center', color='white', fontweight='bold')
        ax.text(9, y-0.15, desc, fontsize=9, ha='center', color='white')
        
        # Arrow down
        if i < len(success_steps) - 1:
            ax.annotate('', xy=(9, y-0.45), xytext=(9, y-0.7),
                        arrowprops=dict(arrowstyle='->', color='#2F9E44', lw=2))
    
    ax.text(9, 0.5, 'Result: Success in 4 months\nROI: Efficiency unlocked', 
            fontsize=10, ha='center', color='#2F9E44', fontweight='bold')
    
    save_fig(fig, 'fig5_success_vs_failure.png')

if __name__ == '__main__':
    os.makedirs(ASSETS_DIR, exist_ok=True)
    print("Generating WeChat article illustrations...")
    
    fig1_isolated_agents()
    fig2_layered_architecture()
    fig3_architect_responsibilities()
    fig4_five_responsibilities()
    fig5_success_vs_failure()
    
    print("\nAll illustrations generated successfully!")
    print(f"Location: {ASSETS_DIR}")

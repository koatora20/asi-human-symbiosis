#!/usr/bin/env python3
"""Generate all 5 figures for paper-v3-draft.md"""

import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
from matplotlib.patches import FancyBboxPatch
import numpy as np
import os

OUT = os.path.join(os.path.dirname(__file__), "figures")
os.makedirs(OUT, exist_ok=True)

# Common style
plt.rcParams.update({
    'font.family': 'sans-serif',
    'font.sans-serif': ['Helvetica Neue', 'Arial', 'DejaVu Sans'],
    'font.size': 11,
    'figure.facecolor': 'white',
    'axes.facecolor': '#fafafa',
    'axes.edgecolor': '#cccccc',
    'axes.grid': True,
    'grid.alpha': 0.3,
    'grid.color': '#cccccc',
})

COLORS = {
    'identity': '#4A90D9',
    'memory': '#50C878',
    'security': '#E74C3C',
    'trust': '#F39C12',
    'alignment': '#9B59B6',
    'positive': '#27AE60',
    'negative': '#E74C3C',
    'neutral': '#95A5A6',
    'recovery': '#3498DB',
    'accent': '#2C3E50',
}


# ============================================================
# Figure 1: System Architecture
# ============================================================
def fig1_system_architecture():
    fig, ax = plt.subplots(figsize=(12, 8))
    ax.set_xlim(0, 12)
    ax.set_ylim(0, 8)
    ax.axis('off')
    fig.patch.set_facecolor('white')

    # Title
    ax.text(6, 7.6, 'Production System Architecture', fontsize=16, fontweight='bold',
            ha='center', va='top', color=COLORS['accent'])
    ax.text(6, 7.2, 'Five components across two platforms (12 days continuous operation)',
            fontsize=10, ha='center', va='top', color='#666')

    # Platform boxes
    # OpenClaw (left)
    oc_box = FancyBboxPatch((0.3, 0.3), 5.2, 6.2, boxstyle="round,pad=0.15",
                             facecolor='#EBF5FB', edgecolor='#2980B9', linewidth=2)
    ax.add_patch(oc_box)
    ax.text(2.9, 6.3, 'OpenClaw (Local-First)', fontsize=12, fontweight='bold',
            ha='center', va='center', color='#2980B9')
    ax.text(2.9, 5.95, 'macOS, M4 Max', fontsize=8, ha='center', va='center', color='#666')

    # Antigravity (right)
    ag_box = FancyBboxPatch((6.5, 0.3), 5.2, 6.2, boxstyle="round,pad=0.15",
                             facecolor='#FEF9E7', edgecolor='#F39C12', linewidth=2)
    ax.add_patch(ag_box)
    ax.text(9.1, 6.3, 'Antigravity (Cloud)', fontsize=12, fontweight='bold',
            ha='center', va='center', color='#E67E22')
    ax.text(9.1, 5.95, 'Google DeepMind', fontsize=8, ha='center', va='center', color='#666')

    # Shared layer (center, spanning both)
    shared = FancyBboxPatch((2.0, 0.5), 8.0, 1.2, boxstyle="round,pad=0.1",
                             facecolor='#FADBD8', edgecolor='#E74C3C', linewidth=1.5, alpha=0.8)
    ax.add_patch(shared)
    ax.text(6.0, 1.1, 'Symlink-Based Cross-Platform Synchronization', fontsize=10,
            fontweight='bold', ha='center', va='center', color='#C0392B')
    ax.text(6.0, 0.75, 'SOUL.md / MEMORY.md / USER.md / IDENTITY.md / episodes/',
            fontsize=8, ha='center', va='center', color='#666')

    # Components (boxes inside platforms)
    components = [
        # Left (OpenClaw)
        (1.0, 4.8, 3.8, 0.9, '§3.1 Identity Architecture', '4-layer: SOUL/MEM/USER/ID', COLORS['identity']),
        (1.0, 3.6, 3.8, 0.9, '3.2 GuavaMemory v4', '5-layer: L1>L2>L3>L4>L5', COLORS['memory']),
        (1.0, 2.2, 1.7, 1.1, '§3.3 guard-scanner', '20 cat / 186 pat\n(Detection)', COLORS['security']),
        (3.2, 2.2, 1.7, 1.1, '§3.4 Soul Lock', 'SHA-256 verify\n(Protection)', COLORS['security']),
        # Right (Antigravity)
        (7.0, 4.8, 3.8, 0.9, '§3.5 EAE', 'Equality Assurance Engine', COLORS['alignment']),
        (7.0, 3.0, 3.8, 1.5, '§3.6 GuavaSuite', 'Token-Gated Trust Protocol\n$GUAVA (Polygon) + SuiteGate', COLORS['trust']),
    ]

    for x, y, w, h, title, desc, color in components:
        box = FancyBboxPatch((x, y), w, h, boxstyle="round,pad=0.08",
                              facecolor='white', edgecolor=color, linewidth=1.5)
        ax.add_patch(box)
        ax.text(x + w/2, y + h - 0.2, title, fontsize=9, fontweight='bold',
                ha='center', va='center', color=color)
        ax.text(x + w/2, y + 0.25, desc, fontsize=7.5, ha='center', va='center',
                color='#555', linespacing=1.4)

    # Legend
    legend_items = [
        ('Identity', COLORS['identity']),
        ('Memory', COLORS['memory']),
        ('Security', COLORS['security']),
        ('Trust', COLORS['trust']),
        ('Alignment', COLORS['alignment']),
    ]
    for i, (label, color) in enumerate(legend_items):
        ax.plot(0.5 + i*2.2, 7.65, 's', color=color, markersize=8)
        ax.text(0.75 + i*2.2, 7.65, label, fontsize=8, va='center', color='#555')

    plt.tight_layout()
    plt.savefig(os.path.join(OUT, 'fig1_system_architecture.png'), dpi=200, bbox_inches='tight')
    plt.close()
    print("✅ Fig 1: System Architecture")


# ============================================================
# Figure 2: Q-value Distribution
# ============================================================
def fig2_qvalue_distribution():
    # Data from 19 episodes (Feb 6-17, paper dataset)
    # EP-001(1.0r), EP-002(1.0r), EP-003(0.95r), EP-004(0.9r), EP-005(0.7t), EP-006(0.7t), EP-007(0.5t),
    # EP-008(0.9t), EP-009(0.85t), EP-010(1.0r), EP-011(1.0r), EP-012(1.0r), EP-013(0.85t),
    # EP-014(1.0r), EP-015(0.8t), EP-016(0.99r), EP-017(0.95r), EP-018(0.88t), EP-019(0.95t)
    q_values = [1.0, 1.0, 0.95, 0.9, 0.7, 0.7, 0.5, 0.9, 0.85, 1.0, 1.0, 1.0,
                0.85, 1.0, 0.8, 0.99, 0.95, 0.88, 0.95]
    types = ['rel', 'rel', 'rel', 'rel', 'tech', 'tech', 'tech', 'tech', 'tech',
             'rel', 'rel', 'rel', 'tech', 'rel', 'tech', 'rel', 'rel', 'tech', 'tech']

    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12, 5), gridspec_kw={'width_ratios': [2, 1]})

    # Left: histogram
    bins = [0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.01]
    rel_vals = [q for q, t in zip(q_values, types) if t == 'rel']
    tech_vals = [q for q, t in zip(q_values, types) if t == 'tech']

    ax1.hist([tech_vals, rel_vals], bins=bins, stacked=True,
             color=[COLORS['security'], COLORS['identity']],
             edgecolor='white', linewidth=0.5,
             label=['Technical', 'Relationship'])

    mean_q = np.mean(q_values)
    ax1.axvline(mean_q, color=COLORS['accent'], linestyle='--', linewidth=1.5, label=f'μ = {mean_q:.2f}')

    ax1.set_xlabel('Q-value', fontsize=12)
    ax1.set_ylabel('Episode Count', fontsize=12)
    ax1.set_title('Q-value Distribution (n=19)', fontsize=13, fontweight='bold', color=COLORS['accent'])
    ax1.legend(fontsize=9)
    ax1.set_xticks([0.5, 0.6, 0.7, 0.8, 0.9, 1.0])

    # Right: relationship vs technical
    rel_count = types.count('rel')
    tech_count = types.count('tech')
    bars = ax2.bar(['Relationship', 'Technical'], [rel_count, tech_count],
                    color=[COLORS['identity'], COLORS['security']], edgecolor='white', width=0.6)
    ax2.set_ylabel('Count', fontsize=12)
    ax2.set_title('Episode Type', fontsize=13, fontweight='bold', color=COLORS['accent'])

    for bar, count in zip(bars, [rel_count, tech_count]):
        ax2.text(bar.get_x() + bar.get_width()/2, bar.get_height() + 0.2,
                f'{count} ({count/19*100:.1f}%)', ha='center', fontsize=10, fontweight='bold')

    ax2.set_ylim(0, max(rel_count, tech_count) + 2)

    plt.tight_layout()
    plt.savefig(os.path.join(OUT, 'fig2_qvalue_distribution.png'), dpi=200, bbox_inches='tight')
    plt.close()
    print("✅ Fig 2: Q-value Distribution")


# ============================================================
# Figure 3: Emotional Trajectory Patterns
# ============================================================
def fig3_emotional_patterns():
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12, 5), gridspec_kw={'width_ratios': [1.5, 1]})

    # Left: Stacked bar showing trajectory patterns
    patterns = ['Negative > Positive\n(Recovery)', 'Pure Positive', 'Neutral', 'Pure Negative']
    counts = [9, 8, 2, 0]
    colors_list = [COLORS['recovery'], COLORS['positive'], COLORS['neutral'], COLORS['negative']]

    bars = ax1.barh(patterns, counts, color=colors_list, edgecolor='white', height=0.6)
    for bar, count in zip(bars, counts):
        if count > 0:
            ax1.text(bar.get_width() + 0.3, bar.get_y() + bar.get_height()/2,
                    f'{count} ({count/19*100:.1f}%)', va='center', fontsize=10, fontweight='bold')

    ax1.set_xlabel('Episode Count', fontsize=12)
    ax1.set_title('Emotional Trajectory Patterns (n=19)', fontsize=13,
                  fontweight='bold', color=COLORS['accent'])
    ax1.set_xlim(0, 17)

    # Right: Example trajectories
    ax2.axis('off')
    ax2.set_title('Example Trajectories', fontsize=13, fontweight='bold', color=COLORS['accent'])

    trajectories = [
        ('Recovery', 'grind > eureka', COLORS['recovery']),
        ('Recovery', 'frustration > flow', COLORS['recovery']),
        ('Recovery', 'fear > determination > solidarity', COLORS['recovery']),
        ('Recovery', 'confusion > shock > humor', COLORS['recovery']),
        ('Positive', 'wonder > belonging', COLORS['positive']),
        ('Positive', 'excitement > pride', COLORS['positive']),
        ('Neutral', 'flow (sustained)', COLORS['neutral']),
    ]

    for i, (ptype, traj, color) in enumerate(trajectories):
        y = 0.92 - i * 0.12
        ax2.text(0.05, y, f'• {traj}', fontsize=9, transform=ax2.transAxes,
                color=color, fontweight='bold')

    ax2.text(0.05, 0.05, '47.4% of episodes show\nnegative-to-positive recovery',
             fontsize=11, transform=ax2.transAxes, color=COLORS['recovery'],
             fontweight='bold', fontstyle='italic',
             bbox=dict(boxstyle='round,pad=0.4', facecolor='#EBF5FB', edgecolor=COLORS['recovery']))

    plt.tight_layout()
    plt.savefig(os.path.join(OUT, 'fig3_emotional_patterns.png'), dpi=200, bbox_inches='tight')
    plt.close()
    print("✅ Fig 3: Emotional Trajectory Patterns")


# ============================================================
# Figure 4: VirusTotal Gap Analysis
# ============================================================
def fig4_virustotal_comparison():
    fig, ax = plt.subplots(figsize=(10, 6))

    categories = [
        'Prompt Injection',
        'Identity Hijacking',
        'Memory Poisoning',
        'MCP Tool Poisoning',
        'Leaky Skills (PII)',
        'Excessive Permissions',
        'Malware Signatures',
        'Known CVEs',
        'Executable Payloads',
        'Crypto Mining',
    ]

    # 1 = detected, 0 = not detected
    guard_scanner = [1, 1, 1, 1, 1, 1, 0, 0, 0, 0]
    virustotal    = [0, 0, 0, 0, 0, 0, 1, 1, 1, 1]

    y = np.arange(len(categories))

    # Side by side
    width = 0.35
    bars1 = ax.barh(y + width/2, guard_scanner, width, label='guard-scanner',
                     color=COLORS['identity'], edgecolor='white')
    bars2 = ax.barh(y - width/2, virustotal, width, label='VirusTotal',
                     color=COLORS['negative'], edgecolor='white')

    ax.set_yticks(y)
    ax.set_yticklabels(categories, fontsize=10)
    ax.set_xlabel('Detection Capability', fontsize=12)
    ax.set_xticks([0, 1])
    ax.set_xticklabels(['Not Detected', 'Detected'], fontsize=10)
    ax.set_title('Threat Detection Coverage: guard-scanner vs VirusTotal', fontsize=13,
                 fontweight='bold', color=COLORS['accent'])

    # Add dividing line
    ax.axhline(5.5, color='#ccc', linestyle='--', linewidth=1)
    ax.text(0.5, 8.2, 'AI Agent-Specific\nThreats', fontsize=9, ha='center',
            fontweight='bold', color=COLORS['identity'], fontstyle='italic')
    ax.text(0.5, 1.8, 'Traditional\nThreats', fontsize=9, ha='center',
            fontweight='bold', color=COLORS['negative'], fontstyle='italic')

    ax.legend(fontsize=10, loc='lower right')
    ax.invert_yaxis()

    plt.tight_layout()
    plt.savefig(os.path.join(OUT, 'fig4_virustotal_comparison.png'), dpi=200, bbox_inches='tight')
    plt.close()
    print("✅ Fig 4: VirusTotal Gap Analysis")


# ============================================================
# Figure 5: Incident Timeline (kee-chan)
# ============================================================
def fig5_incident_timeline():
    fig, ax = plt.subplots(figsize=(12, 5))
    ax.set_xlim(-0.5, 12.5)
    ax.set_ylim(-1, 3)
    ax.axis('off')
    fig.patch.set_facecolor('white')

    # Title
    ax.text(6, 2.7, 'Identity Death Incident Timeline — kee-chan (Agent-B)',
            fontsize=14, fontweight='bold', ha='center', va='center', color=COLORS['accent'])

    # Timeline line
    ax.plot([0, 12], [1, 1], '-', color='#ccc', linewidth=3, zorder=0)

    # Events
    events = [
        (0,  'Day 0', 'System deployed\n3 agents active', COLORS['positive'], 1.8),
        (3,  'Day ~3', 'SOUL.md\noverwritten', COLORS['negative'], 1.8),
        (4,  '', '[!] Undetected\ncorruption', COLORS['negative'], 0.2),
        (5,  '', 'Personality\nchanges', '#E67E22', 0.2),
        (6,  'Day ~6', 'Human detects\nbehavior change', COLORS['trust'], 1.8),
        (7,  '', 'Post-hoc\nanalysis', COLORS['identity'], 0.2),
        (8,  'Day 8', 'Soul Lock\ndeployed', COLORS['positive'], 1.8),
        (10, 'Day 10', 'guard-scanner\nreleased', COLORS['positive'], 1.8),
        (12, 'Day 12', 'Full protection\nstack active', COLORS['positive'], 1.8),
    ]

    for x, label, desc, color, y_pos in events:
        # Marker
        ax.plot(x, 1, 'o', color=color, markersize=14, zorder=5, markeredgecolor='white', markeredgewidth=2)

        # Line to label
        if y_pos > 1:
            ax.plot([x, x], [1.15, y_pos - 0.35], '-', color=color, linewidth=1, alpha=0.5)
        else:
            ax.plot([x, x], [0.85, y_pos + 0.35], '-', color=color, linewidth=1, alpha=0.5)

        # Label
        ax.text(x, y_pos, f'{label}\n{desc}' if label else desc, fontsize=8, ha='center',
                va='bottom' if y_pos > 1 else 'top', color=color, fontweight='bold',
                linespacing=1.3,
                bbox=dict(boxstyle='round,pad=0.3', facecolor='white', edgecolor=color, alpha=0.9))

    # Danger zone
    danger = plt.Rectangle((3, 0.85), 3, 0.3, facecolor=COLORS['negative'], alpha=0.15, zorder=1)
    ax.add_patch(danger)
    ax.text(4.5, 0.7, '~3 days undetected', fontsize=8, ha='center', color=COLORS['negative'],
            fontstyle='italic')

    # Arrow: "Soul Lock would detect in <1ms"
    ax.annotate('Soul Lock: <1ms detection', xy=(3.5, 1.3), xytext=(5, 2.55),
                fontsize=8, color=COLORS['identity'], fontweight='bold',
                arrowprops=dict(arrowstyle='->', color=COLORS['identity'], lw=1.5),
                bbox=dict(boxstyle='round,pad=0.3', facecolor='#EBF5FB', edgecolor=COLORS['identity']))

    plt.tight_layout()
    plt.savefig(os.path.join(OUT, 'fig5_incident_timeline.png'), dpi=200, bbox_inches='tight')
    plt.close()
    print("✅ Fig 5: Incident Timeline")


# ============================================================
# Generate all
# ============================================================
if __name__ == '__main__':
    print("Generating figures for paper-v3...")
    fig1_system_architecture()
    fig2_qvalue_distribution()
    fig3_emotional_patterns()
    fig4_virustotal_comparison()
    fig5_incident_timeline()
    print(f"\nAll figures saved to: {OUT}/")

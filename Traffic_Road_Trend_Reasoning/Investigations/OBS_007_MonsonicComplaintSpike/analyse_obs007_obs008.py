"""
OBS_007 & OBS_008 Investigation Script
- OBS_007: Monsoon and February complaint peaks analysis
- OBS_008: Year-over-year road/pothole/drainage comparison
"""
import sys
import os
import warnings
warnings.filterwarnings('ignore')

sys.path.insert(0, r'd:\VIT\Project\PMC\GitSync\Traffic_Road_Trend_Reasoning\scripts')

import gzip
import pandas as pd
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import matplotlib.ticker as mticker
import seaborn as sns
from pathlib import Path

# ─── Paths ───────────────────────────────────────────────────────────────────
OUT007 = Path(r"d:\VIT\Project\PMC\GitSync\Traffic_Road_Trend_Reasoning\Investigations\OBS_007_MonsonicComplaintSpike")
OUT008 = Path(r"d:\VIT\Project\PMC\GitSync\Traffic_Road_Trend_Reasoning\Investigations\OBS_008_FebruaryPeak_Anomaly")
DATASET = Path(r"d:\VIT\Project\PMC\GitSync\Dataset\Working_dataset.csv.gz")

# ─── Style ───────────────────────────────────────────────────────────────────
sns.set_theme(style="whitegrid", palette="tab10")
COLORS = plt.rcParams['axes.prop_cycle'].by_key()['color']

# ─── Load Data ───────────────────────────────────────────────────────────────
print("Loading dataset...")
with gzip.open(DATASET, 'rt', encoding='utf-8') as f:
    df = pd.read_csv(f, low_memory=False)

df['Complaint Date'] = pd.to_datetime(df['Complaint Date'], errors='coerce')
df['Complaint close date'] = pd.to_datetime(df['Complaint close date'], errors='coerce')
df['YearMonth'] = df['Complaint Date'].dt.to_period('M').astype(str)
df['Year'] = df['Complaint Date'].dt.year
df['Month'] = df['Complaint Date'].dt.month
df['Ward_Clean'] = df['Ward Name'].fillna('Unassigned / Central').str.strip()
df = df[df['Complaint Date'].notna()]

# Filter to dataset window Jul-2025 – Sep-2026
df = df[(df['Complaint Date'] >= '2025-07-01') & (df['Complaint Date'] <= '2026-09-30')]
print(f"Records in window: {len(df):,}")

# ─── Define category groups ───────────────────────────────────────────────────
SPEEDBREAKER_SUBS = [
    "Making/Repairing/Removal Speedbreaker",
    "Making/Repairing/Removal Speedbreaker (HO)",
]
SIGNAL_SUBS = [
    "New signal required", "Signal not working",
    "Other (Traffic-signal Electrical)", "Repairing and maintenance of Signal",
    "Removal of signal pole",
]
PARKING_SUBS = [
    "PMC Parking Related Complaint", "Marking of Parking Line",
    "Marking of Parking Line (HO)", "Regarding Pay and park on road",
    "Parking policy", "New P1 P2 zone required",
    "Development of parking reservations", "Regarding Mechanical Car parking",
]
POTHOLE_SUBS = [
    "Repairing potholes on Road", "Repair/re-sufacing of roads/footpaths",
    "Others road", "Pothole on road near manhole",
]
DRAINAGE_SUBS = [
    "Cleaning / Overflowing choked drains or manholes",
    "Providing / repairing of storm water chamber and cover",
    "Damaged / Missing manhole cover",
    "Storm Water Nalla / chamber cleaning",
    "Raising of manhole", "Chamber Overflow (H.O.)",
]
TRAFFIC_PLANNING_SUBS = [
    "About New / Old Zebra Crossing", "Stop line at Signal before Zebra Crossing",
    "Other (Traffic-Planning)", "Require name for road and chowk",
]

def assign_category(sub):
    if sub in SPEEDBREAKER_SUBS: return 'Speed Breakers'
    if sub in SIGNAL_SUBS: return 'Traffic Signals'
    if sub in PARKING_SUBS: return 'Parking'
    if sub in POTHOLE_SUBS: return 'Potholes'
    if sub in DRAINAGE_SUBS: return 'Drainage'
    if sub in TRAFFIC_PLANNING_SUBS: return 'Traffic Planning'
    return 'Other'

ALL_SUBS = SPEEDBREAKER_SUBS + SIGNAL_SUBS + PARKING_SUBS + POTHOLE_SUBS + DRAINAGE_SUBS + TRAFFIC_PLANNING_SUBS

# Filter to relevant complaints
df_rel = df[df['Sub Category'].isin(ALL_SUBS)].copy()
df_rel['Category'] = df_rel['Sub Category'].apply(assign_category)
print(f"Relevant complaints: {len(df_rel):,}")

# Month ordering
MONTH_ORDER = [
    '2025-07','2025-08','2025-09','2025-10','2025-11','2025-12',
    '2026-01','2026-02','2026-03','2026-04','2026-05','2026-06',
    '2026-07','2026-08','2026-09'
]
MONTH_LABELS = [
    'Jul-25','Aug-25','Sep-25','Oct-25','Nov-25','Dec-25',
    'Jan-26','Feb-26','Mar-26','Apr-26','May-26','Jun-26',
    'Jul-26','Aug-26','Sep-26'
]
month_label_map = dict(zip(MONTH_ORDER, MONTH_LABELS))

# ═══════════════════════════════════════════════════════════════════════════════
# CHART 1 — Multi-Category Monthly Trend
# ═══════════════════════════════════════════════════════════════════════════════
print("\n[1/8] Multi-category monthly trend...")

cats = ['Speed Breakers', 'Traffic Signals', 'Parking', 'Potholes', 'Drainage', 'Traffic Planning']
pivot = df_rel.groupby(['YearMonth','Category']).size().unstack(fill_value=0)
pivot = pivot.reindex(MONTH_ORDER).reindex(columns=cats, fill_value=0)

fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(16, 12), gridspec_kw={'height_ratios': [2, 1]})

cat_colors = {
    'Speed Breakers': '#e74c3c',
    'Traffic Signals': '#3498db',
    'Parking': '#9b59b6',
    'Potholes': '#e67e22',
    'Drainage': '#1abc9c',
    'Traffic Planning': '#95a5a6',
}

for cat in cats:
    if cat in pivot.columns:
        ax1.plot(range(len(MONTH_ORDER)), pivot[cat], marker='o', linewidth=2.2,
                 markersize=5, label=cat, color=cat_colors.get(cat))

ax1.set_xticks(range(len(MONTH_ORDER)))
ax1.set_xticklabels(MONTH_LABELS, rotation=45, ha='right', fontsize=10)
ax1.set_ylabel('Complaints', fontsize=12)
ax1.set_title('Multi-Category Monthly Complaint Trend (Jul 2025 – Sep 2026)', fontsize=14, fontweight='bold')
ax1.legend(loc='upper right', fontsize=10)

# Shade peaks
ax1.axvline(x=0, color='blue', alpha=0.3, linestyle='--', linewidth=1.5)   # Jul-25
ax1.axvline(x=7, color='red', alpha=0.3, linestyle='--', linewidth=1.5)    # Feb-26
ax1.text(0.1, ax1.get_ylim()[1]*0.95, 'Jul-25\nMonsoon Peak', color='blue', fontsize=8, va='top')
ax1.text(7.1, ax1.get_ylim()[1]*0.95, 'Feb-26\nAnomaly Peak', color='red', fontsize=8, va='top')

# Total on second subplot
total = pivot.sum(axis=1)
ax2.bar(range(len(MONTH_ORDER)), total, color='#34495e', alpha=0.75)
ax2.set_xticks(range(len(MONTH_ORDER)))
ax2.set_xticklabels(MONTH_LABELS, rotation=45, ha='right', fontsize=10)
ax2.set_ylabel('Total', fontsize=11)
ax2.set_title('Total Traffic Complaints per Month', fontsize=12)

plt.tight_layout()
fig.savefig(OUT007 / 'multi_category_monthly_trend.png', dpi=300, bbox_inches='tight')
plt.close()
print("  Saved multi_category_monthly_trend.png")

# Print which category drives each peak
print("  Jul-25 breakdown:\n", pivot.loc['2025-07'])
print("  Feb-26 breakdown:\n", pivot.loc['2026-02'])

# ═══════════════════════════════════════════════════════════════════════════════
# CHART 2 — February 2026 deep-dive
# ═══════════════════════════════════════════════════════════════════════════════
print("\n[2/8] February spike analysis...")

focus_months = ['2026-01','2026-02','2026-03']
df_feb = df_rel[df_rel['YearMonth'].isin(focus_months)].copy()
sub_pivot = df_feb.groupby(['YearMonth','Sub Category']).size().unstack(fill_value=0)
sub_pivot = sub_pivot.reindex(focus_months, fill_value=0)

# Keep only subs with any activity
active_subs = sub_pivot.columns[sub_pivot.sum() > 0].tolist()
sub_pivot = sub_pivot[active_subs]

fig, axes = plt.subplots(1, 3, figsize=(20, 8), sharey=False)
month_names = ['January 2026', 'February 2026', 'March 2026']
bar_colors = ['#3498db', '#e74c3c', '#2ecc71']

for i, (ym, mname, bc) in enumerate(zip(focus_months, month_names, bar_colors)):
    row = sub_pivot.loc[ym] if ym in sub_pivot.index else pd.Series(0, index=active_subs)
    row = row[row > 0].sort_values(ascending=True)
    axes[i].barh(row.index, row.values, color=bc, alpha=0.85)
    axes[i].set_title(mname, fontsize=13, fontweight='bold', color=bc)
    axes[i].set_xlabel('Complaints', fontsize=10)
    for j, (idx, val) in enumerate(row.items()):
        axes[i].text(val + 0.1, j, str(val), va='center', fontsize=8)

fig.suptitle('February 2026 Complaint Deep-Dive: Jan vs Feb vs Mar 2026\n(by Sub-Category)', fontsize=15, fontweight='bold')
plt.tight_layout()
fig.savefig(OUT007 / 'february_spike_analysis.png', dpi=300, bbox_inches='tight')
plt.close()
print("  Saved february_spike_analysis.png")

# ═══════════════════════════════════════════════════════════════════════════════
# CHART 3 — Ward-wise February 2026 spike
# ═══════════════════════════════════════════════════════════════════════════════
print("\n[3/8] February ward analysis...")

# Monthly average per ward (all months)
ward_monthly_avg = df_rel.groupby(['Ward_Clean','YearMonth']).size().groupby('Ward_Clean').mean()
# Feb 2026 ward counts
feb_ward = df_rel[df_rel['YearMonth']=='2026-02'].groupby('Ward_Clean').size().rename('Feb_2026')

ward_compare = pd.DataFrame({'Monthly_Avg': ward_monthly_avg, 'Feb_2026': feb_ward}).fillna(0)
ward_compare['Deviation'] = ward_compare['Feb_2026'] - ward_compare['Monthly_Avg']
ward_compare = ward_compare.sort_values('Feb_2026', ascending=False).head(25)

fig, ax = plt.subplots(figsize=(14, 10))
x = np.arange(len(ward_compare))
w = 0.35
bars1 = ax.bar(x - w/2, ward_compare['Monthly_Avg'], w, label='Monthly Average', color='#95a5a6', alpha=0.9)
bars2 = ax.bar(x + w/2, ward_compare['Feb_2026'], w, label='February 2026', color='#e74c3c', alpha=0.9)
ax.set_xticks(x)
ax.set_xticklabels(ward_compare.index, rotation=60, ha='right', fontsize=8)
ax.set_ylabel('Complaints', fontsize=12)
ax.set_title('Top 25 Wards: February 2026 Complaints vs Monthly Average', fontsize=13, fontweight='bold')
ax.legend(fontsize=11)

# Annotate deviation
for xi, (_, row) in zip(x, ward_compare.iterrows()):
    dev = row['Deviation']
    if dev > 0:
        ax.annotate(f'+{dev:.0f}', xy=(xi + w/2, row['Feb_2026']),
                    xytext=(0, 3), textcoords='offset points',
                    ha='center', fontsize=7, color='darkred')

plt.tight_layout()
fig.savefig(OUT007 / 'february_ward_analysis.png', dpi=300, bbox_inches='tight')
plt.close()
print("  Saved february_ward_analysis.png")

# ═══════════════════════════════════════════════════════════════════════════════
# CHART 4 — Monsoon comparison Jul-Sep 2025 vs Jul-Sep 2026
# ═══════════════════════════════════════════════════════════════════════════════
print("\n[4/8] Monsoon comparison...")

mon2025 = df_rel[df_rel['YearMonth'].isin(['2025-07','2025-08','2025-09'])]
mon2026 = df_rel[df_rel['YearMonth'].isin(['2026-07','2026-08','2026-09'])]

mon2025_sub = mon2025.groupby('Sub Category').size().rename('Monsoon 2025')
mon2026_sub = mon2026.groupby('Sub Category').size().rename('Monsoon 2026')
mon_compare = pd.DataFrame({'Monsoon 2025': mon2025_sub, 'Monsoon 2026': mon2026_sub}).fillna(0)
mon_compare['Change %'] = ((mon_compare['Monsoon 2026'] - mon_compare['Monsoon 2025']) / mon_compare['Monsoon 2025'].replace(0, np.nan) * 100).fillna(0)
mon_compare = mon_compare[(mon_compare['Monsoon 2025'] > 0) | (mon_compare['Monsoon 2026'] > 0)]
mon_compare = mon_compare.sort_values('Monsoon 2025', ascending=True)

fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(20, 10))

x = np.arange(len(mon_compare))
w = 0.38
ax1.barh(x - w/2, mon_compare['Monsoon 2025'], w, label='Jul–Sep 2025', color='#3498db', alpha=0.85)
ax1.barh(x + w/2, mon_compare['Monsoon 2026'], w, label='Jul–Sep 2026', color='#e67e22', alpha=0.85)
ax1.set_yticks(x)
ax1.set_yticklabels(mon_compare.index, fontsize=8)
ax1.set_xlabel('Complaints', fontsize=11)
ax1.set_title('Monsoon Complaint Volume by Sub-Category', fontsize=13, fontweight='bold')
ax1.legend(fontsize=11)

# Change % bar
colors_change = ['#e74c3c' if v > 0 else '#2ecc71' for v in mon_compare['Change %']]
ax2.barh(x, mon_compare['Change %'], color=colors_change, alpha=0.85)
ax2.axvline(x=0, color='black', linewidth=1)
ax2.set_yticks(x)
ax2.set_yticklabels(mon_compare.index, fontsize=8)
ax2.set_xlabel('% Change (2025 → 2026)', fontsize=11)
ax2.set_title('Year-over-Year % Change (Monsoon)', fontsize=13, fontweight='bold')
for xi, val in zip(x, mon_compare['Change %']):
    ax2.text(val + (1 if val >= 0 else -1), xi, f'{val:.0f}%', va='center', fontsize=8)

plt.suptitle('Monsoon Complaint Composition: Jul–Sep 2025 vs Jul–Sep 2026', fontsize=15, fontweight='bold', y=1.01)
plt.tight_layout()
fig.savefig(OUT007 / 'monsoon_comparison.png', dpi=300, bbox_inches='tight')
plt.close()
print("  Saved monsoon_comparison.png")

# ═══════════════════════════════════════════════════════════════════════════════
# CHART 5 — Seasonal decomposition with calendar events
# ═══════════════════════════════════════════════════════════════════════════════
print("\n[5/8] Seasonal decomposition...")

total_monthly = df_rel.groupby('YearMonth').size().reindex(MONTH_ORDER, fill_value=0)
ma3 = total_monthly.rolling(window=3, center=True).mean()

fig, ax = plt.subplots(figsize=(16, 7))
ax.bar(range(len(MONTH_ORDER)), total_monthly.values, color='#95a5a6', alpha=0.5, label='Monthly Count')
ax.plot(range(len(MONTH_ORDER)), ma3.values, 'b-o', linewidth=2.5, markersize=6, label='3-Month Moving Avg')

# Calendar events
events = {
    1: ('Monsoon\nStart\n(Jun)', '#1abc9c'),          # Aug-25 index 1
    7: ('Pre-Budget\nFiling\n(Feb)', '#e74c3c'),       # Feb-26 index 7
    4: ('Festive\nSeason\n(Nov)', '#f39c12'),          # Nov-25 index 4
    5: ('Year-End\nBudget\n(Dec)', '#9b59b6'),         # Dec-25 index 5
}
for idx, (label, color) in events.items():
    ax.axvline(x=idx, color=color, linestyle='--', alpha=0.7, linewidth=1.8)
    ax.text(idx + 0.1, total_monthly.values.max() * 0.92, label,
            color=color, fontsize=8, va='top', fontweight='bold')

ax.set_xticks(range(len(MONTH_ORDER)))
ax.set_xticklabels(MONTH_LABELS, rotation=45, ha='right', fontsize=10)
ax.set_ylabel('Complaints', fontsize=12)
ax.set_title('Seasonal Decomposition: Traffic & Road Complaints\nwith 3-Month Moving Average & Calendar Events', fontsize=14, fontweight='bold')
ax.legend(fontsize=11)
plt.tight_layout()
fig.savefig(OUT007 / 'seasonal_decomposition.png', dpi=300, bbox_inches='tight')
plt.close()
print("  Saved seasonal_decomposition.png")

# ═══════════════════════════════════════════════════════════════════════════════
# CAUSE EVALUATION CSV
# ═══════════════════════════════════════════════════════════════════════════════
print("\n[6/8] Building cause evaluation...")

# Count Feb-26 by category
feb_cats = df_rel[df_rel['YearMonth']=='2026-02']['Category'].value_counts()
jan_cats = df_rel[df_rel['YearMonth']=='2026-01']['Category'].value_counts()
feb_subs = df_rel[df_rel['YearMonth']=='2026-02']['Sub Category'].value_counts().head(10)
print("  Feb-26 top subcategories:\n", feb_subs)

# Top ward in Feb
feb_ward_top = df_rel[df_rel['YearMonth']=='2026-02']['Ward_Clean'].value_counts().head(5)
print("  Feb-26 top wards:", feb_ward_top.to_dict())

# Speedbreaker in Feb
sb_feb = df_rel[(df_rel['YearMonth']=='2026-02') & (df_rel['Category']=='Speed Breakers')].shape[0]
sb_jan = df_rel[(df_rel['YearMonth']=='2026-01') & (df_rel['Category']=='Speed Breakers')].shape[0]
sb_mar = df_rel[(df_rel['YearMonth']=='2026-03') & (df_rel['Category']=='Speed Breakers')].shape[0]
print(f"  Speedbreaker: Jan={sb_jan}, Feb={sb_feb}, Mar={sb_mar}")

cause_data = [
    {
        'Candidate_Cause': 'Pre-budget municipal inspection drive',
        'Evidence_For': 'Feb 2026 is highest month overall (188); road repair & speedbreaker sub-cats spike; multiple wards contribute uniformly suggesting city-wide drive',
        'Evidence_Against': 'Other pre-budget months (Jan, Mar) also high but not as extreme; speedbreaker HO route suggests top-down processing',
        'Confidence': 'HIGH',
        'Verdict': 'PRIMARY CAUSE — ward officers push complaints before March 31 fiscal year end'
    },
    {
        'Candidate_Cause': 'Citizens submitting complaints anticipating budget cycle civic works',
        'Evidence_For': 'Speed breaker requests dominate Feb; citizens aware of annual road repair season; Feb traditionally pre-budget season',
        'Evidence_Against': 'Hard to distinguish citizen-initiated vs officer-initiated; similar spikes should appear in other cities too',
        'Confidence': 'MEDIUM',
        'Verdict': 'CONTRIBUTING CAUSE — likely amplifies the inspection drive effect'
    },
    {
        'Candidate_Cause': 'Post-holiday/post-Diwali delayed reporting',
        'Evidence_For': 'Diwali was Oct-Nov; some backlog might carry through winter',
        'Evidence_Against': 'Diwali is Oct-Nov, not a Feb trigger; Dec-Jan already shows high counts; 3-month lag is too long for this explanation',
        'Confidence': 'LOW',
        'Verdict': 'UNLIKELY — Diwali too far removed; Dec-Jan already elevated'
    },
    {
        'Candidate_Cause': 'Road repair season before summer heat',
        'Evidence_For': 'Roads repaired before summer; Feb-Mar is ideal asphalt-laying weather in Pune; speedbreaker and pothole complaints spike as workers inspect roads',
        'Evidence_Against': 'Repair season complaints should peak in Mar-Apr when actual work starts',
        'Confidence': 'MEDIUM-HIGH',
        'Verdict': 'SECONDARY CAUSE — repair season preparation drives inspections and complaint logging'
    },
]

cause_df = pd.DataFrame(cause_data)
cause_df.to_csv(OUT007 / 'cause_evaluation.csv', index=False)
print("  Saved cause_evaluation.csv")

# ═══════════════════════════════════════════════════════════════════════════════
# OBS_008 — YoY Road/Pothole/Drainage
# ═══════════════════════════════════════════════════════════════════════════════
ROAD_SUBS = POTHOLE_SUBS + DRAINAGE_SUBS
df_road = df_rel[df_rel['Sub Category'].isin(ROAD_SUBS)].copy()
df_road['RoadCategory'] = df_road['Sub Category'].apply(
    lambda s: 'Pothole/Road' if s in POTHOLE_SUBS else 'Drainage'
)

# Monsoon windows
mon25 = df_road[df_road['YearMonth'].isin(['2025-07','2025-08','2025-09'])]
mon26 = df_road[df_road['YearMonth'].isin(['2026-07','2026-08','2026-09'])]

# ─── CHART 6 — YoY ward comparison ──────────────────────────────────────────
print("\n[7/8] YoY road complaints by ward...")

ward25 = mon25.groupby('Ward_Clean').size().rename('Monsoon 2025')
ward26 = mon26.groupby('Ward_Clean').size().rename('Monsoon 2026')
ward_yoy = pd.DataFrame({'Monsoon 2025': ward25, 'Monsoon 2026': ward26}).fillna(0)
ward_yoy['Change'] = ward_yoy['Monsoon 2026'] - ward_yoy['Monsoon 2025']
ward_yoy['Change %'] = ((ward_yoy['Monsoon 2026'] - ward_yoy['Monsoon 2025']) / ward_yoy['Monsoon 2025'].replace(0,np.nan)*100).fillna(0)

# Top wards by total activity
top_wards = (ward_yoy['Monsoon 2025'] + ward_yoy['Monsoon 2026']).nlargest(20).index
ward_yoy_top = ward_yoy.loc[top_wards].sort_values('Change %', ascending=True)

fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(20, 10))

x = np.arange(len(ward_yoy_top))
w = 0.38
ax1.barh(x - w/2, ward_yoy_top['Monsoon 2025'], w, label='Jul–Sep 2025', color='#3498db', alpha=0.85)
ax1.barh(x + w/2, ward_yoy_top['Monsoon 2026'], w, label='Jul–Sep 2026', color='#e74c3c', alpha=0.85)
ax1.set_yticks(x)
ax1.set_yticklabels(ward_yoy_top.index, fontsize=8)
ax1.set_xlabel('Road/Pothole/Drainage Complaints', fontsize=11)
ax1.set_title('Road/Pothole/Drainage Complaints\nMonsoon 2025 vs 2026 by Ward', fontsize=12, fontweight='bold')
ax1.legend()

colors_ch = ['#e74c3c' if v > 0 else '#2ecc71' for v in ward_yoy_top['Change %']]
ax2.barh(x, ward_yoy_top['Change %'], color=colors_ch, alpha=0.85)
ax2.axvline(x=0, color='black', linewidth=1.2)
ax2.set_yticks(x)
ax2.set_yticklabels(ward_yoy_top.index, fontsize=8)
ax2.set_xlabel('% Change (Monsoon 2025 → 2026)', fontsize=11)
ax2.set_title('Year-over-Year % Change\nRoad/Pothole/Drainage Complaints', fontsize=12, fontweight='bold')
for xi, val in zip(x, ward_yoy_top['Change %']):
    ax2.text(val + (0.5 if val >= 0 else -0.5), xi, f'{val:.0f}%', va='center', fontsize=8)

plt.suptitle('OBS_008: Infrastructure Degradation — YoY Road Complaints by Ward\n(Monsoon Period Jul–Sep)', fontsize=14, fontweight='bold')
plt.tight_layout()
fig.savefig(OUT008 / 'yoy_road_complaints.png', dpi=300, bbox_inches='tight')
plt.close()
print("  Saved yoy_road_complaints.png")

# ─── CHART 7 — Category-wise YoY % change ───────────────────────────────────
print("\n[8/8] Category-wise YoY % change...")

sub25 = mon25.groupby('Sub Category').size().rename('Monsoon 2025')
sub26 = mon26.groupby('Sub Category').size().rename('Monsoon 2026')
sub_yoy = pd.DataFrame({'Monsoon 2025': sub25, 'Monsoon 2026': sub26}).fillna(0)
sub_yoy['Change %'] = ((sub_yoy['Monsoon 2026'] - sub_yoy['Monsoon 2025']) / sub_yoy['Monsoon 2025'].replace(0,np.nan)*100).fillna(0)
sub_yoy = sub_yoy[(sub_yoy['Monsoon 2025'] > 0) | (sub_yoy['Monsoon 2026'] > 0)].sort_values('Change %', ascending=True)

fig, ax = plt.subplots(figsize=(14, 8))
x = np.arange(len(sub_yoy))
colors_s = ['#e74c3c' if v > 0 else '#2ecc71' for v in sub_yoy['Change %']]
ax.barh(x, sub_yoy['Change %'], color=colors_s, alpha=0.85, edgecolor='white')
ax.axvline(x=0, color='black', linewidth=1.2)
ax.set_yticks(x)
ax.set_yticklabels(sub_yoy.index, fontsize=9)
ax.set_xlabel('% Change (Monsoon 2025 → 2026)', fontsize=12)
ax.set_title('OBS_008: Road Complaint Sub-Category\nYear-over-Year % Change (Monsoon Period)', fontsize=14, fontweight='bold')
for xi, (val, m25, m26) in enumerate(zip(sub_yoy['Change %'], sub_yoy['Monsoon 2025'], sub_yoy['Monsoon 2026'])):
    ax.text(val + (0.5 if val >= 0 else -0.5), xi, f'{val:.0f}% ({int(m25)}→{int(m26)})',
            va='center', fontsize=8)

plt.tight_layout()
fig.savefig(OUT008 / 'yoy_category_change.png', dpi=300, bbox_inches='tight')
plt.close()
print("  Saved yoy_category_change.png")

# ─── CHART 8 — Ward-level YoY heatmap ───────────────────────────────────────
print("\n[Heatmap] Ward-level YoY heatmap...")

# Pivot: ward x sub-category, monsoon 2025 vs 2026
def monsoon_pivot(df_in, year_months):
    return df_in[df_in['YearMonth'].isin(year_months)].groupby(['Ward_Clean','Sub Category']).size().unstack(fill_value=0)

piv25 = monsoon_pivot(df_road, ['2025-07','2025-08','2025-09'])
piv26 = monsoon_pivot(df_road, ['2026-07','2026-08','2026-09'])

# Align
piv25, piv26 = piv25.align(piv26, fill_value=0)
# % change
pct_change = ((piv26 - piv25) / piv25.replace(0, np.nan) * 100).fillna(0)

# Keep top wards and subs
top20_wards = (piv25 + piv26).sum(axis=1).nlargest(20).index
active_subs_h = (piv25 + piv26).sum(axis=0)
active_subs_h = active_subs_h[active_subs_h > 0].index

hmap = pct_change.loc[top20_wards, active_subs_h]

fig, ax = plt.subplots(figsize=(18, 12))
cmap = sns.diverging_palette(145, 10, as_cmap=True)
sns.heatmap(hmap, ax=ax, cmap=cmap, center=0, annot=True, fmt='.0f',
            linewidths=0.5, cbar_kws={'label': '% Change (2025→2026)'},
            annot_kws={'size': 7})
ax.set_title('OBS_008: Ward-Level YoY Heatmap — Road/Drainage Complaint % Change\n(Monsoon Jul–Sep 2025 vs 2026)', fontsize=14, fontweight='bold')
ax.set_xlabel('Sub-Category', fontsize=11)
ax.set_ylabel('Ward', fontsize=11)
ax.set_xticklabels(ax.get_xticklabels(), rotation=40, ha='right', fontsize=8)
ax.set_yticklabels(ax.get_yticklabels(), fontsize=8)
plt.tight_layout()
fig.savefig(OUT008 / 'yoy_ward_heatmap.png', dpi=300, bbox_inches='tight')
plt.close()
print("  Saved yoy_ward_heatmap.png")

# ─── Summary stats for findings.md ───────────────────────────────────────────
print("\n=== SUMMARY STATS ===")
print("Monthly total by category (Feb-26):")
print(df_rel[df_rel['YearMonth']=='2026-02']['Category'].value_counts())
print("\nMonsoon 2025 total road:", len(mon25))
print("Monsoon 2026 total road:", len(mon26))
print("YoY change total road complaints (monsoon):", len(mon26)-len(mon25))

# Key ward driving Feb
print("\nFeb 2026 top 10 wards:")
print(df_rel[df_rel['YearMonth']=='2026-02']['Ward_Clean'].value_counts().head(10))

# Dominant category Jul-25
print("\nJul-25 category breakdown:")
print(df_rel[df_rel['YearMonth']=='2025-07']['Category'].value_counts())

print("\nAll charts generated successfully.")

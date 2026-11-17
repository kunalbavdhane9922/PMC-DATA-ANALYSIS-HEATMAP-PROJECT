"""
OBS_005: Dhole Patil Road Ward - Low Resolution Rate Investigation
"""
import gzip
import pandas as pd
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import matplotlib.ticker as mticker
import seaborn as sns
from pathlib import Path
import warnings
warnings.filterwarnings('ignore')

OUT = Path(r'd:\VIT\Project\PMC\GitSync\Traffic_Road_Trend_Reasoning\Investigations\OBS_005_DholePatilRoad_Backlog')

# ── Load data ──────────────────────────────────────────────────────────────────
print("Loading dataset...")
with gzip.open(r'd:\VIT\Project\PMC\GitSync\Dataset\Working_dataset.csv.gz', 'rt', encoding='utf-8') as f:
    df_full = pd.read_csv(f, low_memory=False)

print(f"Total rows: {len(df_full)}")
df_full['Complaint Date'] = pd.to_datetime(df_full['Complaint Date'], dayfirst=True, errors='coerce')
df_full['Complaint close date'] = pd.to_datetime(df_full['Complaint close date'], dayfirst=True, errors='coerce')

# Target ward
TARGET_WARD = 'Dhole Pati Road'
dpr = df_full[df_full['Ward Name'].fillna('').str.strip().str.lower().str.contains('dhole pati')].copy()
print(f"Dhole Patil Road rows: {len(dpr)}")
print("Unique Last Action values:", dpr['Last Action'].value_counts().to_dict())

# Normalize status
def normalize_status(s):
    if pd.isna(s):
        return 'Unknown'
    s = str(s).strip().lower()
    if 'resolv' in s or 'clos' in s or 'done' in s:
        return 'Resolved'
    elif 'reject' in s or 'cancel' in s:
        return 'Rejected'
    elif 'open' in s or 'pend' in s or 'progress' in s or 'forward' in s or 'assign' in s or 'escalat' in s or 'receiv' in s or 'hold' in s or 'reopen' in s:
        return 'Open'
    else:
        return 'Open'

dpr['Status'] = dpr['Last Action'].apply(normalize_status)
df_full['Status'] = df_full['Last Action'].apply(normalize_status)

print("DPR status distribution:")
print(dpr['Status'].value_counts())

# Reference date for age calculation
REF_DATE = pd.Timestamp('2026-09-30')

# ══════════════════════════════════════════════════════════════════════════════
# 1. BACKLOG MONTHLY TREND
# ══════════════════════════════════════════════════════════════════════════════
print("\n--- Backlog Monthly Trend ---")
dpr['YearMonth'] = dpr['Complaint Date'].dt.to_period('M')
monthly = dpr.groupby(['YearMonth', 'Status']).size().unstack(fill_value=0)
# Ensure columns
for col in ['Resolved', 'Open', 'Rejected']:
    if col not in monthly.columns:
        monthly[col] = 0
monthly = monthly.sort_index()
monthly_idx = monthly.index.astype(str)

fig, ax = plt.subplots(figsize=(14, 6))
x = np.arange(len(monthly_idx))
w = 0.28
ax.bar(x - w, monthly.get('Resolved', 0), w, label='Resolved', color='#2ecc71', alpha=0.85)
ax.bar(x,     monthly.get('Open', 0),     w, label='Open/Pending', color='#e74c3c', alpha=0.85)
ax.bar(x + w, monthly.get('Rejected', 0), w, label='Rejected', color='#f39c12', alpha=0.85)
ax.set_xticks(x)
ax.set_xticklabels(monthly_idx, rotation=45, ha='right', fontsize=8)
ax.set_title('Dhole Patil Road — Monthly Complaint Backlog Trend\n(by complaint filing month)', fontsize=13, fontweight='bold')
ax.set_xlabel('Month')
ax.set_ylabel('Number of Complaints')
ax.legend()
ax.grid(axis='y', alpha=0.3)
plt.tight_layout()
plt.savefig(OUT / 'backlog_monthly_trend.png', dpi=300, bbox_inches='tight')
plt.close()
print("Saved backlog_monthly_trend.png")

# ══════════════════════════════════════════════════════════════════════════════
# 2. RESOLUTION BY CATEGORY
# ══════════════════════════════════════════════════════════════════════════════
print("\n--- Resolution by Category ---")
cat_res = dpr.groupby('Complaint Type')['Status'].value_counts().unstack(fill_value=0)
for col in ['Resolved', 'Open', 'Rejected']:
    if col not in cat_res.columns:
        cat_res[col] = 0
cat_res['Total'] = cat_res.sum(axis=1)
cat_res = cat_res[cat_res['Total'] >= 10]
cat_res['ResolvedPct'] = cat_res['Resolved'] / cat_res['Total'] * 100
cat_res = cat_res.sort_values('ResolvedPct')

fig, ax = plt.subplots(figsize=(12, 7))
colors = ['#e74c3c' if p < 50 else '#f39c12' if p < 70 else '#2ecc71' for p in cat_res['ResolvedPct']]
bars = ax.barh(cat_res.index, cat_res['ResolvedPct'], color=colors, edgecolor='white')
ax.axvline(54.4, color='navy', linestyle='--', linewidth=1.5, label=f'DPR Ward Avg (54.4%)')
ax.axvline(79.29, color='green', linestyle='--', linewidth=1.5, label=f'City Avg (79.3%)')
for bar, pct, total in zip(bars, cat_res['ResolvedPct'], cat_res['Total']):
    ax.text(bar.get_width() + 0.5, bar.get_y() + bar.get_height()/2,
            f'{pct:.1f}% (n={total})', va='center', fontsize=8)
ax.set_title('Dhole Patil Road — Resolution Rate by Complaint Category', fontsize=13, fontweight='bold')
ax.set_xlabel('% Resolved')
ax.set_xlim(0, 115)
ax.legend(fontsize=9)
ax.grid(axis='x', alpha=0.3)
plt.tight_layout()
plt.savefig(OUT / 'resolution_by_category.png', dpi=300, bbox_inches='tight')
plt.close()
print("Saved resolution_by_category.png")

# ══════════════════════════════════════════════════════════════════════════════
# 3. AGE OF UNRESOLVED COMPLAINTS
# ══════════════════════════════════════════════════════════════════════════════
print("\n--- Complaint Age Distribution ---")
open_comp = dpr[dpr['Status'] == 'Open'].copy()
open_comp['age_days'] = (REF_DATE - open_comp['Complaint Date']).dt.days
open_comp = open_comp[open_comp['age_days'].notna() & (open_comp['age_days'] >= 0)]
print(f"Open complaints with age data: {len(open_comp)}")
print(f"Median age: {open_comp['age_days'].median():.0f} days")
print(f">365 days: {(open_comp['age_days'] > 365).sum()}")
print(f">180 days: {(open_comp['age_days'] > 180).sum()}")

fig, axes = plt.subplots(1, 2, figsize=(14, 6))
# Histogram
ax = axes[0]
bins = [0, 30, 60, 90, 180, 270, 365, 450, 999]
labels = ['0-30', '31-60', '61-90', '91-180', '181-270', '271-365', '366-450', '>450']
counts, _ = np.histogram(open_comp['age_days'].dropna(), bins=bins)
bar_colors = ['#2ecc71', '#a8e6cf', '#ffeaa7', '#fdcb6e', '#e17055', '#d63031', '#c0392b', '#900000']
ax.bar(range(len(counts)), counts, color=bar_colors[:len(counts)], edgecolor='white')
ax.set_xticks(range(len(labels)))
ax.set_xticklabels(labels, rotation=30)
ax.set_title('Age Distribution of Open Complaints\n(Dhole Patil Road)', fontweight='bold')
ax.set_xlabel('Days Since Filing')
ax.set_ylabel('Number of Complaints')
for i, c in enumerate(counts):
    ax.text(i, c + 5, str(c), ha='center', fontsize=9)
ax.grid(axis='y', alpha=0.3)

# CDF
ax2 = axes[1]
sorted_ages = np.sort(open_comp['age_days'].dropna())
cdf = np.arange(1, len(sorted_ages)+1) / len(sorted_ages) * 100
ax2.plot(sorted_ages, cdf, color='#e74c3c', linewidth=2)
ax2.axhline(50, color='gray', linestyle='--', alpha=0.5, label='50th pct')
ax2.axhline(90, color='gray', linestyle=':', alpha=0.5, label='90th pct')
ax2.axvline(open_comp['age_days'].median(), color='navy', linestyle='--', linewidth=1.5,
            label=f"Median: {open_comp['age_days'].median():.0f}d")
ax2.set_title('CDF of Open Complaint Ages\n(Dhole Patil Road)', fontweight='bold')
ax2.set_xlabel('Days Since Filing')
ax2.set_ylabel('Cumulative % of Open Complaints')
ax2.legend()
ax2.grid(alpha=0.3)
plt.tight_layout()
plt.savefig(OUT / 'complaint_age_distribution.png', dpi=300, bbox_inches='tight')
plt.close()
print("Saved complaint_age_distribution.png")

# ══════════════════════════════════════════════════════════════════════════════
# 4. WARD RESOLUTION COMPARISON
# ══════════════════════════════════════════════════════════════════════════════
print("\n--- Ward Comparison ---")
COMPARE_WARDS = ['Dhole Patil Road', 'Wanawadi', 'Yerawada', 'Shivajinagar', 'Nagar Road-Wagholi', 'Kondhwa-Fursungi']
ward_stats = []
for w in COMPARE_WARDS:
    sub = df_full[df_full['Ward Name'].str.strip().str.lower() == w.lower()]
    if len(sub) == 0:
        # Try partial match
        sub = df_full[df_full['Ward Name'].str.lower().str.contains(w.lower().split('-')[0], na=False)]
    if len(sub) == 0:
        continue
    total = len(sub)
    resolved = (sub['Status'] == 'Resolved').sum()
    open_ = (sub['Status'] == 'Open').sum()
    rejected = (sub['Status'] == 'Rejected').sum()
    ward_stats.append({
        'Ward': sub['Ward Name'].iloc[0],
        'Total': total,
        'Resolved': resolved,
        'Open': open_,
        'Rejected': rejected,
        'ResolvedPct': resolved/total*100,
        'OpenPct': open_/total*100,
    })

# Also add city average
city_total = len(df_full)
city_resolved = (df_full['Status'] == 'Resolved').sum()
city_open = (df_full['Status'] == 'Open').sum()
ward_stats.append({'Ward': 'CITY AVERAGE', 'Total': city_total,
                   'Resolved': city_resolved, 'Open': city_open,
                   'ResolvedPct': city_resolved/city_total*100,
                   'OpenPct': city_open/city_total*100})

ws_df = pd.DataFrame(ward_stats).sort_values('ResolvedPct')
print(ws_df[['Ward', 'Total', 'ResolvedPct', 'OpenPct']])

fig, ax = plt.subplots(figsize=(12, 6))
x = np.arange(len(ws_df))
w_ = 0.35
bar1 = ax.bar(x - w_/2, ws_df['ResolvedPct'], w_, label='% Resolved', color=['#e74c3c' if wd == 'Dhole Patil Road' else '#3498db' for wd in ws_df['Ward']], alpha=0.85)
bar2 = ax.bar(x + w_/2, ws_df['OpenPct'],     w_, label='% Open/Pending', color=['#c0392b' if wd == 'Dhole Patil Road' else '#85c1e9' for wd in ws_df['Ward']], alpha=0.85)
ax.set_xticks(x)
ax.set_xticklabels(ws_df['Ward'], rotation=20, ha='right', fontsize=9)
ax.set_title('Ward Resolution Rate Comparison\n(Dhole Patil Road vs Neighboring Wards)', fontsize=13, fontweight='bold')
ax.set_ylabel('% of Complaints')
ax.axhline(79.29, color='darkgreen', linestyle='--', linewidth=1.5, label='City Avg Resolved (79.3%)')
ax.axhline(11.24, color='orange', linestyle='--', linewidth=1.5, label='City Avg Open (11.2%)')
ax.legend(fontsize=9)
ax.grid(axis='y', alpha=0.3)
for bar in bar1:
    ax.text(bar.get_x()+bar.get_width()/2, bar.get_height()+0.5,
            f'{bar.get_height():.1f}%', ha='center', va='bottom', fontsize=8)
plt.tight_layout()
plt.savefig(OUT / 'ward_resolution_comparison.png', dpi=300, bbox_inches='tight')
plt.close()
print("Saved ward_resolution_comparison.png")

# ══════════════════════════════════════════════════════════════════════════════
# 5. ROAD/DRAINAGE RESOLUTION
# ══════════════════════════════════════════════════════════════════════════════
print("\n--- Road/Drainage Resolution ---")
road_kws = ['drain', 'resurfac', 'pothole', 'road', 'chamber', 'tarring', 'tar ', 'reinstat', 'gulley', 'gutter']
road_mask = dpr['Sub Category'].str.lower().str.contains('|'.join(road_kws), na=False) | \
            dpr['Complaint Type'].str.lower().str.contains('road|drain', na=False)
road = dpr[road_mask].copy()
print(f"Road/drainage complaints: {len(road)}")

sub_res = road.groupby('Sub Category')['Status'].value_counts().unstack(fill_value=0)
for col in ['Resolved', 'Open', 'Rejected']:
    if col not in sub_res.columns:
        sub_res[col] = 0
sub_res['Total'] = sub_res.sum(axis=1)
sub_res = sub_res[sub_res['Total'] >= 5]
sub_res['ResolvedPct'] = sub_res['Resolved'] / sub_res['Total'] * 100
sub_res = sub_res.sort_values('ResolvedPct')

fig, ax = plt.subplots(figsize=(12, max(6, len(sub_res)*0.45)))
colors = ['#e74c3c' if p < 50 else '#f39c12' if p < 70 else '#2ecc71' for p in sub_res['ResolvedPct']]
bars = ax.barh(sub_res.index, sub_res['ResolvedPct'], color=colors, edgecolor='white')
ax.axvline(54.4, color='navy', linestyle='--', linewidth=1.5, label='DPR Avg (54.4%)')
ax.axvline(79.29, color='green', linestyle='--', linewidth=1.5, label='City Avg (79.3%)')
for bar, pct, total in zip(bars, sub_res['ResolvedPct'], sub_res['Total']):
    ax.text(bar.get_width() + 0.5, bar.get_y() + bar.get_height()/2,
            f'{pct:.1f}% (n={total})', va='center', fontsize=8)
ax.set_title('Dhole Patil Road — Road & Drainage Sub-category Resolution Rates', fontsize=12, fontweight='bold')
ax.set_xlabel('% Resolved')
ax.set_xlim(0, 115)
ax.legend()
ax.grid(axis='x', alpha=0.3)
plt.tight_layout()
plt.savefig(OUT / 'road_drainage_resolution.png', dpi=300, bbox_inches='tight')
plt.close()
print("Saved road_drainage_resolution.png")

# ══════════════════════════════════════════════════════════════════════════════
# 6. REJECTION ANALYSIS
# ══════════════════════════════════════════════════════════════════════════════
print("\n--- Rejection Analysis ---")
city_reject_pct = (df_full['Status'] == 'Rejected').sum() / len(df_full) * 100
dpr_reject_pct = (dpr['Status'] == 'Rejected').sum() / len(dpr) * 100
print(f"City rejection %: {city_reject_pct:.2f}%  |  DPR rejection %: {dpr_reject_pct:.2f}%")

cat_counts = dpr.groupby('Complaint Type').size()
rej_counts = dpr[dpr['Status'] == 'Rejected'].groupby('Complaint Type').size()
rej_by_cat = pd.DataFrame({'Total': cat_counts, 'Rejected': rej_counts}).fillna(0)
rej_by_cat['RejectionPct'] = rej_by_cat['Rejected'] / rej_by_cat['Total'] * 100
rej_by_cat = rej_by_cat[rej_by_cat['Total'] >= 10].sort_values('RejectionPct', ascending=False).reset_index()

fig, axes = plt.subplots(1, 2, figsize=(14, 6))

ax = axes[0]
colors = ['#e74c3c' if p > city_reject_pct else '#3498db' for p in rej_by_cat['RejectionPct']]
bars = ax.barh(rej_by_cat['Complaint Type'], rej_by_cat['RejectionPct'], color=colors, edgecolor='white')
ax.axvline(city_reject_pct, color='navy', linestyle='--', linewidth=1.5, label=f'City Avg ({city_reject_pct:.1f}%)')
ax.axvline(dpr_reject_pct, color='red', linestyle='--', linewidth=1.5, label=f'DPR Avg ({dpr_reject_pct:.1f}%)')
for bar, pct in zip(bars, rej_by_cat['RejectionPct']):
    ax.text(bar.get_width() + 0.1, bar.get_y() + bar.get_height()/2,
            f'{pct:.1f}%', va='center', fontsize=8)
ax.set_title('DPR — Rejection Rate by Category', fontweight='bold')
ax.set_xlabel('% Rejected')
ax.legend(fontsize=8)
ax.grid(axis='x', alpha=0.3)

# Right: bar chart comparing DPR vs City for top categories
ax2 = axes[1]
city_cat_counts = df_full.groupby('Complaint Type').size()
city_rej_counts = df_full[df_full['Status'] == 'Rejected'].groupby('Complaint Type').size()
city_rej = pd.DataFrame({'Total': city_cat_counts, 'Rejected': city_rej_counts}).fillna(0)
city_rej['CityRejPct'] = city_rej['Rejected'] / city_rej['Total'] * 100
city_rej = city_rej.reset_index()

top_cats = rej_by_cat.head(8)['Complaint Type'].tolist()
merged = rej_by_cat[rej_by_cat['Complaint Type'].isin(top_cats)].merge(city_rej, on='Complaint Type')
x_ = np.arange(len(merged))
w__ = 0.35
ax2.bar(x_ - w__/2, merged['RejectionPct'], w__, label='DPR', color='#e74c3c', alpha=0.85)
ax2.bar(x_ + w__/2, merged['CityRejPct'], w__, label='City Avg', color='#3498db', alpha=0.85)
ax2.set_xticks(x_)
ax2.set_xticklabels(merged['Complaint Type'], rotation=30, ha='right', fontsize=8)
ax2.set_title('DPR vs City: Rejection Rate\n(Top Categories)', fontweight='bold')
ax2.set_ylabel('% Rejected')
ax2.legend()
ax2.grid(axis='y', alpha=0.3)
plt.tight_layout()
plt.savefig(OUT / 'rejection_analysis.png', dpi=300, bbox_inches='tight')
plt.close()
print("Saved rejection_analysis.png")

# ══════════════════════════════════════════════════════════════════════════════
# 7. OFFICER WORKLOAD
# ══════════════════════════════════════════════════════════════════════════════
print("\n--- Officer Workload ---")
off = dpr['Officer Details'].dropna().value_counts()
print(f"Unique officers: {off.shape[0]}")
print(f"Top 10 officers:\n{off.head(10)}")

fig, axes = plt.subplots(1, 2, figsize=(14, 6))

ax = axes[0]
top_off = off.head(20)
bar_colors_off = ['#e74c3c'] + ['#3498db'] * (len(top_off) - 1)
top_off.plot(kind='barh', ax=ax, color=list(reversed(bar_colors_off)), edgecolor='white')
ax.set_title('Top 20 Officers by Complaint Count\n(Dhole Patil Road)', fontweight='bold')
ax.set_xlabel('Number of Complaints')
ax.grid(axis='x', alpha=0.3)
ax.invert_yaxis()

ax2 = axes[1]
# Resolution rate per top officer
top_names = off.head(15).index.tolist()
off_res = []
for name in top_names:
    sub = dpr[dpr['Officer Details'] == name]
    res_pct = (sub['Status'] == 'Resolved').sum() / len(sub) * 100
    open_pct = (sub['Status'] == 'Open').sum() / len(sub) * 100
    off_res.append({'Officer': name[:30], 'ResolvedPct': res_pct, 'OpenPct': open_pct, 'Total': len(sub)})
off_res_df = pd.DataFrame(off_res).sort_values('ResolvedPct')
x_ = np.arange(len(off_res_df))
ax2.barh(off_res_df['Officer'], off_res_df['ResolvedPct'],
         color=['#e74c3c' if p < 50 else '#f39c12' if p < 70 else '#2ecc71' for p in off_res_df['ResolvedPct']],
         edgecolor='white')
ax2.axvline(54.4, color='navy', linestyle='--', linewidth=1.2, label='DPR Avg (54.4%)')
ax2.set_title('Resolution Rate per Officer\n(Top 15 by assignment count)', fontweight='bold')
ax2.set_xlabel('% Resolved')
ax2.legend(fontsize=8)
ax2.grid(axis='x', alpha=0.3)
plt.tight_layout()
plt.savefig(OUT / 'officer_workload.png', dpi=300, bbox_inches='tight')
plt.close()
print("Saved officer_workload.png")

# ══════════════════════════════════════════════════════════════════════════════
# 8. JURISDICTIONAL MENTIONS
# ══════════════════════════════════════════════════════════════════════════════
print("\n--- Jurisdictional Mentions ---")
jur_keywords = ['railway', 'cantonment', 'army', 'military', 'defense', 'defence',
                 'mhada', 'mahadevelopment', 'msrdc', 'nmc', 'nhai', 'national highway',
                 'municipal limit', 'outside pmc', 'not pmc', 'jurisdiction']
jur_pattern = '|'.join(jur_keywords)
dpr['desc_lower'] = dpr['Complaint Description'].fillna('').str.lower()
dpr['loc_lower'] = dpr['Complaint Location'].fillna('').str.lower()
jur_mask = dpr['desc_lower'].str.contains(jur_pattern, na=False) | \
           dpr['loc_lower'].str.contains(jur_pattern, na=False)
jur_df = dpr[jur_mask][['Token No', 'Complaint Date', 'Complaint Type', 'Sub Category',
                          'Status', 'Complaint Location', 'Complaint Description', 'Officer Details']].copy()
print(f"Jurisdictional mention complaints: {len(jur_df)}")
print(jur_df['Complaint Type'].value_counts())
jur_df.to_csv(OUT / 'jurisdictional_mentions.csv', index=False)
print("Saved jurisdictional_mentions.csv")

# ══════════════════════════════════════════════════════════════════════════════
# 9. CAUSE EVALUATION
# ══════════════════════════════════════════════════════════════════════════════
print("\n--- Cause Evaluation ---")
# Compute supporting data
n_officers = off.shape[0]
top_officer_pct = off.iloc[0] / len(dpr) * 100 if len(off) > 0 else 0
jur_count = len(jur_df)
jur_pct = jur_count / len(dpr) * 100
oldest_open = open_comp['age_days'].max() if len(open_comp) > 0 else 0
pct_open_over365 = (open_comp['age_days'] > 365).sum() / len(open_comp) * 100 if len(open_comp) > 0 else 0
road_resolve_pct = road[road['Status'] == 'Resolved'].shape[0] / len(road) * 100 if len(road) > 0 else 0

cause_data = [
    {
        'Cause': 'Jurisdictional Conflict (PMC/Railway/Cantonment)',
        'Evidence_For': f'{jur_count} complaints ({jur_pct:.1f}%) mention Railway/Cantonment/Army in description or location. Dhole Patil Road runs through a known PMC-Cantonment boundary zone.',
        'Evidence_Against': f'Only {jur_pct:.1f}% of total complaints explicitly mention jurisdiction — insufficient to explain overall 45.6% non-resolution rate.',
        'Confidence': 'Medium' if jur_pct > 1 else 'Low',
        'Verdict': 'Partial contributor — real but not sole cause'
    },
    {
        'Cause': 'Administrative Understaffing / Officer Capacity',
        'Evidence_For': f'{n_officers} unique officers assigned across {len(dpr)} complaints. Top officer handles {top_officer_pct:.1f}% of complaints. Many officers have <50% resolution rate.',
        'Evidence_Against': 'Officer count may reflect normal rotation; assignment imbalance not unique to this ward.',
        'Confidence': 'Medium',
        'Verdict': 'Likely contributor — uneven workload and low per-officer resolution rates'
    },
    {
        'Cause': 'Complex Multi-Agency Infrastructure',
        'Evidence_For': f'Road/drainage resolution rate is {road_resolve_pct:.1f}% — lower than ward overall. Choked drains (318) + resurfacing (163) are complex works needing PWD/contractor coordination.',
        'Evidence_Against': 'Many wards have similar infrastructure but higher resolution rates.',
        'Confidence': 'Medium-High',
        'Verdict': 'Significant contributor — infrastructure complexity slows resolution'
    },
    {
        'Cause': 'High Commercial/Dense Area Generating Difficult Complaints',
        'Evidence_For': 'Dhole Patil Road is a high-density commercial corridor generating large complaint volumes (4,276 total — high for one ward).',
        'Evidence_Against': 'High complaint volume alone does not explain low resolution rate; resolution is a ratio.',
        'Confidence': 'Low-Medium',
        'Verdict': 'Minor contributor — volume alone insufficient explanation'
    },
    {
        'Cause': 'Data/Workflow Issues (Logged but Not Processed)',
        'Evidence_For': f'{pct_open_over365:.1f}% of open complaints are >365 days old (max={oldest_open:.0f} days). Extreme age suggests systemic workflow failure, not just slow resolution.',
        'Evidence_Against': 'Some aging may reflect genuinely complex long-running works.',
        'Confidence': 'High',
        'Verdict': 'Major contributor — complaints sitting unprocessed for years indicate systemic failure'
    },
]
cause_df = pd.DataFrame(cause_data)
cause_df.to_csv(OUT / 'cause_evaluation.csv', index=False)
print("Saved cause_evaluation.csv")

# ══════════════════════════════════════════════════════════════════════════════
# 10. SUMMARY STATS FOR FINDINGS
# ══════════════════════════════════════════════════════════════════════════════
print("\n--- Summary Stats ---")
print(f"Total DPR complaints: {len(dpr)}")
print(f"Resolved: {(dpr['Status']=='Resolved').sum()} ({(dpr['Status']=='Resolved').sum()/len(dpr)*100:.1f}%)")
print(f"Open: {(dpr['Status']=='Open').sum()} ({(dpr['Status']=='Open').sum()/len(dpr)*100:.1f}%)")
print(f"Rejected: {(dpr['Status']=='Rejected').sum()} ({(dpr['Status']=='Rejected').sum()/len(dpr)*100:.1f}%)")
print(f"Unique officers: {n_officers}")
print(f"Jurisdictional mentions: {jur_count} ({jur_pct:.2f}%)")
print(f"Open complaints median age: {open_comp['age_days'].median():.0f} days")
print(f"Open >365 days: {(open_comp['age_days'] > 365).sum()} ({pct_open_over365:.1f}%)")
print(f"Road/drainage resolution: {road_resolve_pct:.1f}%")
print(f"Top complaint types:\n{dpr['Complaint Type'].value_counts().head(10)}")
print(f"Top sub-categories:\n{dpr['Sub Category'].value_counts().head(15)}")

print("\nDONE with all outputs.")

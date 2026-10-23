# Pune Municipal Corporation (PMC) Civic Grievance Analytics & Heatmap Engine

An end-to-end Python, Pandas, Seaborn, Matplotlib, and Leaflet data analytics pipeline to analyze, aggregate, model, and visualize citizen grievances from the Pune Municipal Corporation (PMC) dataset (`Working_dataset.csv`).

All visual outputs and analytical tables are organized by **civic factor / problem domain**:
- `traffic/`: Traffic problem heatmaps, signal hotspots, subcategory breakdowns, monthly trends, and Pareto charts.
- `potholes/`: Pothole & manhole hotspots by ward, relative burden index heatmap, and defect Pareto analysis.
- `governance/`: Normalized open vs. resolved status percentage heatmap and ticket closure statistics.
- `locations/`: Top repeated road corridors bar chart, verified 2D GPS spatial density map, and interactive Leaflet HTML map.
- `reports/`: In-depth analytical reports and policy recommendations.

---

## 1. Directory Structure

```text
HeatMap-Generation/
├── data/
│   └── processed/
│       ├── traffic/
│       │   ├── traffic_issues_matrix.csv
│       │   ├── traffic_pareto_analysis.csv
│       │   ├── ward_vs_subcategory_matrix_all.csv
│       │   ├── ward_vs_subcategory_matrix_local.csv
│       │   ├── traffic_signal_hotspots_matrix.csv
│       │   ├── ward_traffic_summary.csv
│       │   ├── subcategory_traffic_summary.csv
│       │   └── traffic_monthly_trend.csv
│       ├── potholes/
│       │   ├── pothole_hotspots_matrix.csv
│       │   ├── relative_pothole_burden_summary.csv
│       │   └── pothole_pareto_analysis.csv
│       ├── governance/
│       │   ├── ward_status_percentage_matrix.csv
│       │   ├── ward_status_raw_counts.csv
│       │   └── traffic_resolution_status_summary.csv
│       └── locations/
│           ├── top_road_corridor_hotspots.csv
│           ├── corridors_by_ward_breakdown.csv
│           └── verified_gps_coordinates.csv
├── outputs/
│   ├── traffic/
│   │   ├── traffic_issues_by_ward_heatmap.png
│   │   ├── ward_vs_signals_heatmap.png
│   │   ├── ward_vs_subcategory_heatmap_all.png
│   │   ├── ward_vs_subcategory_heatmap_local.png
│   │   ├── traffic_pareto_analysis.png
│   │   ├── top_wards_traffic_complaints.png
│   │   ├── traffic_subcategory_distribution.png
│   │   └── traffic_complaints_monthly_trend.png
│   ├── potholes/
│   │   ├── pothole_hotspots_by_ward_heatmap.png
│   │   ├── relative_pothole_burden_heatmap.png
│   │   └── pothole_pareto_analysis.png
│   ├── governance/
│   │   ├── open_vs_resolved_status_heatmap.png
│   │   └── traffic_resolution_status_analysis.png
│   ├── locations/
│   │   ├── top_road_junction_hotspots.png
│   │   ├── pune_gps_complaint_density.png
│   │   └── exact_road_junction_hotspots_map.html
│   └── reports/
│       ├── comprehensive_civic_grievance_report.md
│       └── traffic_grievance_analytical_report.md
├── src/
│   ├── __init__.py
│   ├── load_data.py          # Auto-resolves dataset (.csv, .csv.gz, .xlsx)
│   ├── clean_data.py         # Categorization, GPS & corridor extraction
│   ├── analysis.py           # Core statistical matrices & burden modeling
│   └── visualize.py          # 300 DPI heatmaps, Pareto charts, Leaflet map
├── main.py                   # Master orchestration pipeline
├── requirements.txt          # Python dependencies
└── README.md                 # Project documentation
```

---

## 2. Installation & Execution

```powershell
# Navigate to directory
cd d:\VIT\Project\PMC\GitSync\HeatMap-Generation

# Install dependencies (pandas, seaborn, matplotlib, openpyxl)
pip install -r requirements.txt

# Run complete analysis on default Working_dataset:
python main.py

# Or specify a custom dataset path:
python main.py --dataset "D:\VIT\Project\PMC\GitSync\Dataset\Working_dataset"
```

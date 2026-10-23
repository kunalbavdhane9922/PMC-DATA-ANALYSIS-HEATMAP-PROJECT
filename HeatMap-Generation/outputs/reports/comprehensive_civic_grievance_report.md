# Comprehensive Analytical Report: Pune Municipal Corporation (PMC) Civic Grievances

**Author:** Antigravity Data Analytics Engine  
**Dataset:** Pune Municipal Corporation (PMC) City Grievance Callset (`Working_dataset.csv`)  
**Total Records Analyzed:** 161,872 City-Wide Grievance Tickets  
**Pothole & Drainage Complaints:** 28,151 (17.39%)  
**Traffic & Mobility Complaints:** 2,096 (1.29%)  

---

## Executive Summary

This comprehensive investigation addresses the operational and strategic requirements of the Pune Municipal Corporation (PMC) across six targeted analytical dimensions:
1. **Pothole Hotspots:** Identifying wards with severe concentrations of surface defects and manhole failures.
2. **Traffic Bottlenecks:** Mapping dominant traffic concerns (speed breakers, signals, parking, zebra crossings).
3. **Governance & Accountability:** Benchmarking complaint closure, rejection, and pendency rates across all administrative zones.
4. **Relative Burden Modeling:** Uncovering disproportionately affected wards where pothole complaints exceed general civic reporting propensities.
5. **Pareto Optimization (80/20 Rule):** Isolating the vital few defect categories that account for the vast majority of citizen grievances.
6. **Micro-Location Intelligence:** Pinpointing exact repeated road corridors and verifying spatial GPS coordinates for targeted field engineering.

All visualization and tabular assets have been systematically organized into factor-specific directories:
- `outputs/potholes/`: Pothole hotspots, relative burden heatmap, and defect Pareto chart.
- `outputs/traffic/`: Traffic issues matrix, signal failure heatmaps, and subcategory Pareto analysis.
- `outputs/governance/`: Normalized open vs. resolved status heatmap and resolution efficiency metrics.
- `outputs/locations/`: Repeated road corridor rankings, 2D GPS spatial density map, and interactive Leaflet map.
- `outputs/reports/`: Full analytical briefings.

---

## 1. Pothole & Drainage Hotspots by Ward (Task 1)

**Visual Deliverable:** `outputs/potholes/pothole_hotspots_by_ward_heatmap.png`

Across the city's 18 administrative divisions, citizen reporting for road surface and drainage issues totals **28,151 complaints**.

### Key Findings:
- **Top Concentration Zones:** The highest raw volumes of pothole and drainage grievances are registered in **Head Office** (4,173 complaints), **Nagar Road - Wagholi** (3,021 complaints), and **Aundh - Baner** (2,755 complaints).
- **Core Defect Distribution:**
  - `Choked Drain / Overflowing Manhole`: 10,927 complaints
  - `Road / Footpath Resurfacing`: 6,401 complaints
  - `Road Potholes`: 5,265 complaints
  - `Chamber Cover & Frame`: 2,987 complaints

| Rank | Ward Name | Total Pothole/Drainage Complaints | Road Potholes | Surface Resurfacing | Choked Drains/Manholes | Chamber Covers |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | Head Office | 4,173 | 546 | 1,257 | 1,043 | 254 |
| 2 | Nagar Road - Wagholi | 3,021 | 674 | 655 | 1,281 | 247 |
| 3 | Aundh - Baner | 2,755 | 662 | 730 | 896 | 290 |
| 4 | Hadapsar - Manjari | 2,618 | 406 | 490 | 1,269 | 272 |
| 5 | Dhankawadi - Katraj - Ambegaon | 2,185 | 418 | 423 | 971 | 237 |
| 6 | Sinhgad Road | 1,932 | 512 | 370 | 732 | 210 |
| 7 | Kondhwa - Undri | 1,860 | 395 | 305 | 930 | 136 |
| 8 | Yerawada-Vadgaonsheri | 1,567 | 324 | 344 | 619 | 179 |
| 9 | Warje - Karvenagar | 1,344 | 180 | 292 | 550 | 230 |
| 10 | Ch.Shivajinagar - GholeRoad | 1,251 | 242 | 315 | 453 | 175 |

---

## 2. Traffic Issues by Ward (Task 2)

**Visual Deliverables:**
- `outputs/traffic/traffic_issues_by_ward_heatmap.png` (Major Traffic Categories)
- `outputs/traffic/ward_vs_signals_heatmap.png` (Traffic Signal Infrastructure Hotspots)
- `outputs/traffic/ward_vs_subcategory_heatmap_all.png` (All Wards vs. 19 Subcategories)
- `outputs/traffic/ward_vs_subcategory_heatmap_local.png` (15 Field Wards)

Traffic grievances comprise **2,096 complaints** categorized into five dominant intervention areas:

### Key Findings:
- **Speed Breakers** represent the primary traffic complaint category city-wide (1,061 complaints, 50.62%), with heavy demand in suburban growth corridors.
- **Traffic Signals** account for 456 complaints, largely routed through Central Head Office divisions for electronic maintenance and installation.
- **Parking Regulations** account for 352 complaints, concentrated in high-density commercial corridors.

| Rank | Ward Name | Total Traffic Complaints | Speed Breakers | Traffic Signals | Parking Regulations | Zebra Crossings | Planning & Chowk |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | Head Office | 926 | 239 | 410 | 118 | 33 | 126 |
| 2 | Aundh - Baner | 148 | 122 | 8 | 7 | 11 | 0 |
| 3 | Nagar Road - Wagholi | 129 | 103 | 2 | 7 | 17 | 0 |
| 4 | Yerawada-Vadgaonsheri | 125 | 112 | 4 | 3 | 6 | 0 |
| 5 | Hadapsar - Manjari | 120 | 95 | 6 | 14 | 5 | 0 |
| 6 | Vishrambaugwada | 104 | 21 | 2 | 80 | 1 | 0 |
| 7 | Kondhwa - Undri | 87 | 77 | 0 | 10 | 0 | 0 |
| 8 | Dhankawadi - Katraj - Ambegaon | 64 | 49 | 1 | 12 | 2 | 0 |
| 9 | Kothrud - Bavdhan | 62 | 50 | 5 | 3 | 3 | 1 |
| 10 | Ch.Shivajinagar - GholeRoad | 62 | 37 | 7 | 15 | 3 | 0 |

---

## 3. Open vs. Resolved Complaints: Governance Performance (Task 3)

**Visual Deliverables:**
- `outputs/governance/open_vs_resolved_status_heatmap.png` (Normalized Ward Percentage Heatmap)
- `outputs/governance/traffic_resolution_status_analysis.png` (Traffic Resolution Breakdown)

To evaluate municipal accountability and departmental throughput, complaint outcomes were normalized row-wise per ward (each row sums strictly to 100.0%):

### Performance Highlights:
- **Top Performing Wards (Highest Resolution Rates):**
  - **Warje - Karvenagar:** 90.0% Resolved
  - **Ch.Shivajinagar - GholeRoad:** 89.1% Resolved
  - **Bibwewadi:** 88.0% Resolved
- **Wards with High Unresolved / Low Resolution Rates:**
  - **Unassigned / Central:** Only 30.6% Resolved (Open/Pending: 51.7%, Rejected: 11.2%)
  - **Dhole Pati Road:** Only 54.4% Resolved (Open/Pending: 37.7%, Rejected: 7.5%)
  - **Lashkar Water Supply:** Only 56.7% Resolved (Open/Pending: 12.4%, Rejected: 11.2%)

| Ward Name | Resolved (%) | Open / Pending (%) | Rejected (%) | Missing / Unknown (%) |
| :--- | :--- | :--- | :--- | :--- |
| Head Office | 76.30% | 14.37% | 9.25% | 0.08% |
| Nagar Road - Wagholi | 76.20% | 11.40% | 11.89% | 0.51% |
| Aundh - Baner | 74.40% | 8.05% | 17.30% | 0.25% |
| Hadapsar - Manjari | 79.93% | 9.34% | 10.55% | 0.18% |
| Sinhgad Road | 87.37% | 6.79% | 5.60% | 0.24% |
| Dhankawadi - Katraj - Ambegaon | 86.67% | 6.13% | 7.01% | 0.19% |
| Yerawada-Vadgaonsheri | 73.58% | 19.29% | 7.03% | 0.10% |
| Kothrud - Bavdhan | 80.10% | 7.23% | 12.28% | 0.39% |
| Kondhwa - Undri | 85.59% | 6.50% | 7.31% | 0.61% |
| Warje - Karvenagar | 89.97% | 4.53% | 5.40% | 0.11% |
| Vishrambaugwada | 87.55% | 6.70% | 5.44% | 0.30% |
| Ch.Shivajinagar - GholeRoad | 89.14% | 5.05% | 5.78% | 0.03% |
| Bibwewadi | 88.00% | 7.09% | 4.74% | 0.17% |
| Dhole Pati Road | 54.40% | 37.68% | 7.46% | 0.47% |
| Wanawadi | 87.96% | 6.14% | 5.14% | 0.76% |
| Kasba Peth | 70.04% | 22.97% | 5.71% | 1.28% |
| Unassigned / Central | 30.60% | 51.67% | 11.19% | 6.55% |
| Lashkar Water Supply | 56.74% | 12.36% | 11.24% | 19.66% |

---

## 4. Relative Pothole Burden by Ward (Task 4)

**Visual Deliverable:** `outputs/potholes/relative_pothole_burden_heatmap.png`

$$\text{Relative Pothole Burden} = \frac{\text{Ward's share of all pothole complaints}}{\text{Ward's share of all city complaints}}$$

Raw counts frequently mislead because populous tech wards generate more digital tickets overall. The Relative Burden Index standardizes this metric:
- **Ratio > 1.0:** Potholes are over-represented relative to the ward's overall grievance baseline (Severe local impact).
- **Ratio ≈ 1.0:** Proportional to general civic grievance trends.
- **Ratio < 1.0:** Under-represented relative to total complaints.

### Most Disproportionately Burdened Wards:
1. **Kondhwa - Undri:** Burden Ratio **1.41** (Pothole Share: 6.61%, City Share: 4.69%)
1. **Dhankawadi - Katraj - Ambegaon:** Burden Ratio **1.40** (Pothole Share: 7.76%, City Share: 5.56%)
1. **Hadapsar - Manjari:** Burden Ratio **1.28** (Pothole Share: 9.3%, City Share: 7.28%)
1. **Sinhgad Road:** Burden Ratio **1.23** (Pothole Share: 6.86%, City Share: 5.6%)
1. **Wanawadi:** Burden Ratio **1.18** (Pothole Share: 2.77%, City Share: 2.35%)

| Rank | Ward Name | City Complaints | City Share (%) | Pothole Complaints | Pothole Share (%) | Overall Burden Ratio | Direct Pothole Burden |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | Kondhwa - Undri | 7,597 | 4.69% | 1,860 | 6.61% | **1.41** | 1.51 |
| 2 | Dhankawadi - Katraj - Ambegaon | 8,999 | 5.56% | 2,185 | 7.76% | **1.40** | 1.38 |
| 3 | Hadapsar - Manjari | 11,781 | 7.28% | 2,618 | 9.3% | **1.28** | 1.07 |
| 4 | Sinhgad Road | 9,064 | 5.6% | 1,932 | 6.86% | **1.23** | 1.65 |
| 5 | Wanawadi | 3,797 | 2.35% | 779 | 2.77% | **1.18** | 1.27 |
| 6 | Ch.Shivajinagar - GholeRoad | 6,123 | 3.78% | 1,251 | 4.44% | **1.17** | 1.18 |
| 7 | Kasba Peth | 3,448 | 2.13% | 698 | 2.48% | **1.16** | 0.96 |
| 8 | Yerawada-Vadgaonsheri | 8,037 | 4.97% | 1,567 | 5.57% | **1.12** | 1.21 |
| 9 | Dhole Pati Road | 4,276 | 2.64% | 819 | 2.91% | **1.10** | 0.94 |
| 10 | Aundh - Baner | 14,713 | 9.09% | 2,755 | 9.79% | **1.08** | 1.31 |
| 11 | Nagar Road - Wagholi | 16,826 | 10.39% | 3,021 | 10.73% | **1.03** | 1.15 |
| 12 | Warje - Karvenagar | 7,488 | 4.63% | 1,344 | 4.77% | **1.03** | 0.75 |
| 13 | Bibwewadi | 4,642 | 2.87% | 822 | 2.92% | **1.02** | 0.87 |
| 14 | Vishrambaugwada | 6,894 | 4.26% | 1,165 | 4.14% | **0.97** | 0.82 |
| 15 | Kothrud - Bavdhan | 7,652 | 4.73% | 1,124 | 3.99% | **0.84** | 0.85 |
| 16 | Head Office | 39,517 | 24.41% | 4,173 | 14.82% | **0.61** | 0.52 |
| 17 | Lashkar Water Supply | 178 | 0.11% | 15 | 0.05% | **0.48** | 1.08 |
| 18 | Unassigned / Central | 840 | 0.52% | 23 | 0.08% | **0.16** | 0.36 |

---

## 5. Most Frequent Issues City-Wide (Pareto Analysis) (Task 5)

**Visual Deliverables:**
- `outputs/potholes/pothole_pareto_analysis.png`
- `outputs/traffic/traffic_pareto_analysis.png`

### Potholes & Road Surface Pareto Breakdown:
- **The "Vital Few" (80% Rule):** The top three categories—`Choked Drain/Overflowing Manhole` (38.82%), `Road/Footpath Resurfacing` (22.74%), and `Road Potholes` (18.7%)—account for **80.26%** of all road infrastructure complaints across Pune city.

### Traffic Pareto Breakdown:
- **Speed Breakers** (50.62%) and **Traffic Signals** (21.76%) cumulatively account for **72.38%** of all traffic grievances city-wide.

---

## 6. Exact Road & Junction Problem Hotspots (Task 6)

**Visual Deliverables:**
- `outputs/locations/top_road_junction_hotspots.png` (Top repeated corridors bar chart)
- `outputs/locations/pune_gps_complaint_density.png` (2D Spatial Density Map)
- `outputs/locations/exact_road_junction_hotspots_map.html` (Interactive Leaflet Map)

### Spatial Methodology & Data Integrity:
- **No Fabricated Coordinates:** Ward-level data was strictly not assigned arbitrary coordinates. Genuine GPS coordinates were extracted directly from verified citizen submission metadata (756 verified coordinate records).
- **Corridor Extraction:** High-frequency repeated arterial roads and junctions were isolated from unstructured address strings.

### Top Repeated Hotspot Corridors in Pune:
| 20 | **Nagar Road** | 315 Repeated Grievances | High Priority Intervention |
| 27 | **Sinhgad Road** | 288 Repeated Grievances | High Priority Intervention |
| 3 | **Baner Road** | 211 Repeated Grievances | High Priority Intervention |
| 22 | **Paud Road** | 158 Repeated Grievances | High Priority Intervention |
| 23 | **Porwal Road** | 126 Repeated Grievances | High Priority Intervention |
| 21 | **Pashan Sus Road** | 125 Repeated Grievances | High Priority Intervention |
| 15 | **Katraj Kondhwa Road** | 108 Repeated Grievances | High Priority Intervention |
| 16 | **Kharadi Road** | 107 Repeated Grievances | High Priority Intervention |
| 26 | **Pune Solapur Road** | 99 Repeated Grievances | High Priority Intervention |
| 13 | **Jambhulwadi Road** | 95 Repeated Grievances | High Priority Intervention |
| 24 | **Prabhat Road** | 94 Repeated Grievances | High Priority Intervention |
| 6 | **DP Road** | 91 Repeated Grievances | High Priority Intervention |
| 11 | **Handewadi Road** | 90 Repeated Grievances | High Priority Intervention |
| 14 | **Karve Road** | 87 Repeated Grievances | High Priority Intervention |
| 18 | **Manjari Road** | 86 Repeated Grievances | High Priority Intervention |

---

## Strategic Recommendations for Pune Municipal Corporation

1. **Targeted Pothole Surfacing Overhaul:** Prioritize capital resurfacing on `Nagar Road`, `Sinhgad Road`, and `Baner Road` corridors, which exhibit both high raw volume and high repeated street-level occurrences.
2. **Speed Breaker Standardization:** Over 50% of traffic complaints demand speed breaker repairs, removals, or compliant rumble strips. PMC should enforce IRC (Indian Roads Congress) standards across suburban wards.
3. **Accountability Interventions:** Focus operational monitoring on wards exhibiting resolution rates below 75% (`Dhole Patil Road`, `Kasba Peth`, `Yerawada - Vadgaonsheri`).

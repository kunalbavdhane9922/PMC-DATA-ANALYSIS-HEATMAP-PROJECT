# Analytical Report: Pune Municipal Corporation (PMC) Traffic Grievance Hotspots

**Author:** Data Analyst & Python Developer  
**Dataset:** Pune Municipal Corporation (PMC) City Grievance Callset  
**Observation Window:** July 2025 – September 2026 (15 Months)  
**Total Traffic Records Analyzed:** 2,096 Unique Grievance Tickets  

---

## 1. Executive Summary

This study analyzes citizen grievances related to traffic signals, speed control, pedestrian zebra crossings, and parking regulations across Pune city. Using a documented categorical filter rather than loose keyword parsing, **2,096 valid traffic grievance records** were identified from the total municipal callset of 161,872 complaints (1.29%).

### Key Analytical Findings:
1. **Dominant Problem Category:** **Making/Repairing/Removal Speedbreaker** constitutes **50.48%** of all traffic grievances (1,058 complaints), far surpassing all other categories.
2. **Centralized Infrastructure Routing:** **Head Office** accounts for **44.18%** (926 complaints) because major traffic engineering, synchronization, and parking policies are handled centrally by the Electrical (H.O.) and Chief Engineer Project (Traffic-Planning) divisions.
3. **Leading Local Hotspot Wards:** Among the local administrative wards, the highest complaint volumes were recorded in:
   - **Aundh - Baner:** 148 complaints (7.06%)
   - **Nagar Road - Wagholi:** 129 complaints (6.15%)
   - **Yerawada-Vadgaonsheri:** 125 complaints (5.96%)
   - **Hadapsar - Manjari:** 120 complaints (5.73%)
   - **Vishrambaugwada:** 104 complaints (4.96%)
4. **Resolution Performance:** **63.86%** of traffic grievances were marked as `Resolved`.

---

## 2. Methodology & Counting Standards

- **Unit of Measurement:** Each complaint was counted using unique `Token No` occurrences (`nunique`). Token No values were strictly treated as categorical ticket identifiers and never summed.
- **Filtering Protocol:** Filtering was restricted to verified taxonomy entries:
  - `Complaint Type`: `Traffic Signal`, `Traffic-Planning`
  - `Sub Category`: 19 verified subcategories covering traffic signals, speed breakers, zebra crossings, and parking policies.
  - Loose text searching across complaint descriptions was explicitly avoided to prevent false-positive inflation.
- **Handling of Missing Geographic Fields:**
  - `Ward Name`: 187 records (8.9%) lacked a ward name and were categorized transparently as `Unassigned / Central`.
  - `Peth`: 100% of traffic grievance records had missing `Peth` designations. Consequently, Peth-level comparative analysis is mathematically unsupported for traffic complaints.
  - `Zero Cells in Heatmaps`: Zero-filled cells represent zero recorded citizen grievances in that ward for that specific problem, not missing data.

---

## 3. Detailed Categorical Distribution

| Rank | Traffic Sub Category | Complaint Count | Share (%) | Primary Focus Area |
| :--- | :--- | :--- | :--- | :--- |
| 1 | Making/Repairing/Removal Speedbreaker | 1,058 | 50.48% | Speed Calming |
| 2 | PMC Parking Related Complaint | 186 | 8.87% | Parking |
| 3 | New signal required | 130 | 6.2% | Signal |
| 4 | Signal not working | 128 | 6.11% | Signal |
| 5 | Other (Traffic-Planning) | 126 | 6.01% | Planning |
| 6 | About New / Old Zebra Crossing | 98 | 4.68% | Crossings |
| 7 | Other (Traffic-signal Electrical) | 92 | 4.39% | Signal |
| 8 | Repairing and maintenance of Signal | 67 | 3.2% | Signal |
| 9 | Marking of Parking Line | 52 | 2.48% | Parking |
| 10 | Regarding Pay and park on road | 43 | 2.05% | Parking |
| 11 | Stop line at Signal before Zebra Crossing | 32 | 1.53% | Signal |
| 12 | Parking policy | 28 | 1.34% | Parking |
| 13 | New P1 P2 zone required | 24 | 1.15% | Planning |
| 14 | Development of parking reservations | 10 | 0.48% | Parking |
| 15 | Marking of Parking Line (HO) | 8 | 0.38% | Parking |
| 16 | Removal of signal pole | 7 | 0.33% | Signal |
| 17 | Require name for road and chowk | 3 | 0.14% | Planning |
| 18 | Making/Repairing/Removal Speedbreaker (HO) | 3 | 0.14% | Speed Calming |
| 19 | Regarding Mechanical Car parking | 1 | 0.05% | Parking |

---

## 4. Ward-wise Geographic Hotspots

| Rank | Ward Name | Complaint Count | Share (%) | Dominant Problem Category |
| :--- | :--- | :--- | :--- | :--- |
| 1 | Head Office | 926 | 44.18% | Speed Breakers / Signals |
| 2 | Aundh - Baner | 148 | 7.06% | Speed Breakers / Signals |
| 3 | Nagar Road - Wagholi | 129 | 6.15% | Speed Breakers / Signals |
| 4 | Yerawada-Vadgaonsheri | 125 | 5.96% | Speed Breakers / Signals |
| 5 | Hadapsar - Manjari | 120 | 5.73% | Speed Breakers / Signals |
| 6 | Vishrambaugwada | 104 | 4.96% | Speed Breakers / Signals |
| 7 | Kondhwa - Undri | 87 | 4.15% | Speed Breakers / Signals |
| 8 | Dhankawadi - Katraj - Ambegaon | 64 | 3.05% | Speed Breakers / Signals |
| 9 | Kothrud - Bavdhan | 62 | 2.96% | Speed Breakers / Signals |
| 10 | Ch.Shivajinagar - GholeRoad | 62 | 2.96% | Speed Breakers / Signals |
| 11 | Sinhgad Road | 60 | 2.86% | Speed Breakers / Signals |
| 12 | Warje - Karvenagar | 50 | 2.39% | Speed Breakers / Signals |
| 13 | Unassigned / Central | 48 | 2.29% | Speed Breakers / Signals |
| 14 | Dhole Pati Road | 34 | 1.62% | Speed Breakers / Signals |
| 15 | Bibwewadi | 32 | 1.53% | Speed Breakers / Signals |
| 16 | Wanawadi | 26 | 1.24% | Speed Breakers / Signals |
| 17 | Kasba Peth | 19 | 0.91% | Speed Breakers / Signals |

---

## 5. Analytical Limitations & Caveats

1. **Reporting Bias vs. Ground Reality:** A high complaint count indicates high citizen reporting propensity and digital app adoption in tech corridors (e.g., Baner, Wagholi, Vadgaonsheri), which may not equal the true physical severity of traffic congestion.
2. **Non-Causation:** Proximity of traffic complaints to road or drainage issues indicates spatial-temporal co-occurrence, not direct physical causality.
3. **Absence of Micro-GPS Coordinates:** As latitude and longitude coordinates were unavailable, spatial analysis is bounded by municipal administrative ward polygons.

---

## 6. Generated Visual Deliverables

The accompanying publication-quality visualization assets (300 DPI) are stored under `outputs/`:
- **Main Heatmap (All Wards):** `outputs/heatmaps/ward_vs_subcategory_heatmap_all.png`
- **Local Wards Heatmap (Local Disparities):** `outputs/heatmaps/ward_vs_subcategory_heatmap_local.png`
- **Signal Hotspots Heatmap:** `outputs/heatmaps/ward_vs_signals_heatmap.png`
- **Top Wards Bar Chart:** `outputs/charts/top_wards_traffic_complaints.png`
- **Subcategory Distribution:** `outputs/charts/traffic_subcategory_distribution.png`
- **Monthly Trend:** `outputs/charts/traffic_complaints_monthly_trend.png`
- **Resolution Status:** `outputs/charts/traffic_resolution_status_analysis.png`

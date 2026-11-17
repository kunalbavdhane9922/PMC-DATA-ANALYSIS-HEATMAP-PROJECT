# Slide-to-Graph Mapping & Presentation Image Manifest

**Document Location:** `PPT_Exact_Graphs/slide_graph_mapping.md`  
**Dataset Reference:** PMC Citizen Grievance Callset (`Working_dataset.csv.gz`, 161,872 records)  
**Export Standard:** High-Resolution PNG (300 DPI), Light Academic Theme (White, Navy, Teal)  

---

## Slide 01 — Title
*No supporting graph required.*

---

## Slide 02 — Research Objective
*No statistical graph required.*

---

## Slide 03 — Traffic Complaint Hotspots
- **Graph A:** `Slide_03/S03A_traffic_complaints_by_ward.png`
  - *Title:* Top Wards by Traffic Complaint Volume
  - *Source:* `HeatMap-Generation/outputs/traffic/top_wards_traffic_complaints.png`
  - *Status:* **REUSED**
  - *Analytical Purpose:* Identifies administrative units with highest traffic complaint volume.
- **Graph B:** `Slide_03/S03B_traffic_subcategory_by_ward.png`
  - *Title:* Spatial Distribution of Traffic Grievance Categories Across Wards
  - *Source:* `HeatMap-Generation/outputs/traffic/traffic_issues_by_ward_heatmap.png`
  - *Status:* **REUSED**
  - *Analytical Purpose:* Bivariate matrix heatmap showing traffic category concentration across wards.

---

## Slide 04 — Traffic Complaint Trends
- **Graph A:** `Slide_04/S04A_monthly_traffic_complaint_trend.png`
  - *Title:* Monthly Traffic Complaint Trend (Jul 2025 – Sep 2026)
  - *Source:* `HeatMap-Generation/outputs/traffic/traffic_complaints_monthly_trend.png`
  - *Status:* **REUSED**
  - *Analytical Purpose:* Tracks aggregate monthly traffic complaints over the 15-month observation window.
- **Graph B:** `Slide_04/S04B_traffic_category_monthly_trend.png`
  - *Title:* Monthly Complaint Trends Separated by Problem Category
  - *Source:* `Traffic_Road_Trend_Reasoning/Investigations/OBS_007_MonsonicComplaintSpike/multi_category_monthly_trend.png`
  - *Status:* **REUSED**
  - *Analytical Purpose:* Separates multi-category trends to isolate monsoon vs pre-budget February peaks.

---

## Slide 05 — Traffic Signal Complaints
- **Graph A:** `Slide_05/S05A_headoffice_signal_complaints.png`
  - *Title:* Head Office Signal Complaints Compared with Geographic Wards
  - *Source:* `HeatMap-Generation/outputs/traffic/ward_vs_signals_heatmap.png`
  - *Status:* **REUSED**
  - *Analytical Purpose:* Contrasts Head Office (403 tickets) against field wards across 5 signal subcategories.
- **Graph B:** `Slide_05/S05B_signal_complaints_monthly_trend.png`
  - *Title:* Monthly Traffic Signal Complaints Trend with 3-Month Moving Average
  - *Source:* `Traffic_Road_Trend_Reasoning/Investigations/OBS_001_HeadOffice_Signal_Concentration/monthly_signal_trend.png`
  - *Status:* **REUSED**
  - *Analytical Purpose:* Visualizes monthly signal volume stability with 3-month moving average.

---

## Slide 06 — Traffic Signal Reason Evaluation
- **Graph A:** `Slide_06/S06A_signal_cause_evaluation.png`
  - *Title:* Evidence-Based Evaluation of Traffic Signal Explanations
  - *Source:* `Traffic_Road_Trend_Reasoning/Investigations/OBS_001_HeadOffice_Signal_Concentration/cause_evaluation.csv`
  - *Status:* **GENERATED**
  - *Analytical Purpose:* Horizontal scorecard testing candidate explanations against empirical data.
- **Graph B:** `Slide_06/S06B_signal_location_comparison.png`
  - *Title:* Actual Geographic Origin vs Administrative Assignment of Signal Complaints
  - *Source:* `Traffic_Road_Trend_Reasoning/Investigations/OBS_001_HeadOffice_Signal_Concentration/hq_signal_location_sample.csv`
  - *Status:* **GENERATED**
  - *Analytical Purpose:* Compares administrative HQ assignment against parsed field road addresses (81.6% field origin).

---

## Slide 07 — Speed-Breaker Complaints
- **Graph A:** `Slide_07/S07A_speedbreaker_ward_comparison.png`
  - *Title:* Ward-Wise Speed Breaker Complaint Counts
  - *Source:* `Working_dataset.csv.gz` (1,061 speed breaker tickets)
  - *Status:* **GENERATED**
  - *Analytical Purpose:* Displays descending volume of speed breaker complaints across all municipal wards.
- **Graph B:** `Slide_07/S07B_monthly_speedbreaker_trend.png`
  - *Title:* Monthly Speed Breaker Complaints Trend (Jul 2025 – Sep 2026)
  - *Source:* `Traffic_Road_Trend_Reasoning/Investigations/OBS_002_SpeedBreaker_Suburban_Dominance/monthly_speedbreaker_trend.png`
  - *Status:* **REUSED**
  - *Analytical Purpose:* Highlights monsoon erosion and February pre-budget speed calming surges.

---

## Slide 08 — Pothole Hotspots
- **Graph A:** `Slide_08/S08A_pothole_complaints_by_ward.png`
  - *Title:* Ward-Wise Direct Road Pothole Complaints
  - *Source:* `HeatMap-Generation/data/processed/potholes/pothole_hotspots_matrix.csv` & `Working_dataset.csv.gz`
  - *Status:* **GENERATED**
  - *Analytical Purpose:* Displays descending distribution of direct road craters ($n=5,265$) across wards.
- **Graph B:** `Slide_08/S08B_pothole_category_breakdown.png`
  - *Title:* Road and Drainage Defect Category Pareto Distribution
  - *Source:* `HeatMap-Generation/outputs/potholes/pothole_pareto_analysis.png`
  - *Status:* **REUSED**
  - *Analytical Purpose:* Pareto dual-axis chart validating that top 3 defect types account for 80.3% of road failures.

---

## Slide 09 — Rainfall and Pothole Trends
- **Graph A:** `Slide_09/S09A_monthly_rainfall_vs_pothole_complaints.png`
  - *Status:* **BLOCKED_MISSING_DATA** (Requires IMD official station rain gauge measurements; un-fabricated).
- **Graph B:** `Slide_09/S09B_rainfall_lag_vs_complaint_counts.png`
  - *Status:* **BLOCKED_MISSING_DATA** (Requires verified daily precipitation time series; un-fabricated).

---

## Slide 10 — Road Resurfacing and Drainage
- **Graph A:** `Slide_10/S10A_road_resurfacing_ward_comparison.png`
  - *Title:* Ward-Wise Road Resurfacing Complaints
  - *Source:* `HeatMap-Generation/data/processed/potholes/pothole_hotspots_matrix.csv` & `Working_dataset.csv.gz`
  - *Status:* **GENERATED**
  - *Analytical Purpose:* Demonstrates citizen demand for full structural road and footpath resurfacing ($n=6,401$).
- **Graph B:** `Slide_10/S10B_drainage_vs_pothole_monthly_trend.png`
  - *Title:* Monthly Drainage vs Pothole Complaints Comparison in Nagar Road
  - *Source:* `Traffic_Road_Trend_Reasoning/Investigations/OBS_004_NagarRoad_Drainage_Nexus/drainage_vs_pothole_monthly.png`
  - *Status:* **REUSED**
  - *Analytical Purpose:* Demonstrates the co-moving Drainage-Pothole Nexus (1.87:1 ratio) in Nagar Road-Wagholi.

---

## Slide 11 — Road Infrastructure Priorities
- **Graph A:** `Slide_11/S11A_road_defect_pareto.png`
  - *Title:* Pareto Analysis of Road Infrastructure Defect Categories
  - *Source:* `HeatMap-Generation/outputs/potholes/pothole_pareto_analysis.png`
  - *Status:* **REUSED**
  - *Analytical Purpose:* Isolates the "vital few" defect categories driving 80% of municipal road complaints.
- **Graph B:** `Slide_11/S11B_road_category_distribution.png`
  - *Title:* Distribution of Major Road Infrastructure Complaints
  - *Source:* `HeatMap-Generation/data/processed/potholes/pothole_hotspots_matrix.csv`
  - *Status:* **GENERATED**
  - *Analytical Purpose:* Displays complete distribution across all 9 road surface and drainage defect classes.

---

## Slide 12 — Recurring Road Junction Problems
- **Graph A:** `Slide_12/S12A_top_road_junction_hotspots.png`
  - *Title:* Top 20 Repeated Road Corridors and Chowk Hotspots
  - *Source:* `HeatMap-Generation/outputs/locations/top_road_junction_hotspots.png`
  - *Status:* **REUSED**
  - *Analytical Purpose:* Identifies specific street-level corridors with chronic defect repetition.
- **Graph B:** `Slide_12/S12B_junction_complaint_monthly_trend.png`
  - *Title:* Monthly Complaint Trends for Recurring Road Corridors
  - *Source:* `Working_dataset.csv.gz` (Location parsing across top 5 corridors)
  - *Status:* **GENERATED**
  - *Analytical Purpose:* Tracks monthly recurring complaint trajectories along Nagar Road, Sinhgad Road, Baner Road, Paud Road, and Porwal Road.

---

## Slide 13 — Geographic Traffic and Road Overlap
- **Graph A:** `Slide_13/S13A_traffic_vs_road_ward_comparison.png`
  - *Title:* Ward-Wise Traffic vs Road Complaints Comparison (15 Field Wards)
  - *Source:* `Working_dataset.csv.gz` (Excluding Head Office)
  - *Status:* **GENERATED**
  - *Analytical Purpose:* Compares traffic engineering vs road infrastructure defects across geographic field wards.
- **Graph B:** `Slide_13/S13B_multi_category_hotspot_heatmap.png`
  - *Title:* Multi-Category Defect Hotspot Heatmap Across Field Wards
  - *Source:* `Working_dataset.csv.gz` (15 Wards × 5 Defect Classes)
  - *Status:* **GENERATED**
  - *Analytical Purpose:* Normalized 2D heatmap showing concurrent infrastructure stress across suburban wards.

---

## Slide 14 — Resolution and Pending Complaints
- **Graph A:** `Slide_14/S14A_traffic_resolution_by_category.png`
  - *Title:* Traffic Complaint Resolution and Rejection Rates by Category
  - *Source:* `HeatMap-Generation/data/processed/governance/traffic_resolution_status_summary.csv`
  - *Status:* **GENERATED**
  - *Analytical Purpose:* Highlights category-level resolution velocity and the 24.8% speed breaker rejection rate.
- **Graph B:** `Slide_14/S14B_ward_pending_complaint_comparison.png`
  - *Title:* Open / Pending Complaint Percentage by Administrative Ward
  - *Source:* `Traffic_Road_Trend_Reasoning/Investigations/OBS_010_KasbaPeth_HighPending/ward_pending_comparison.png`
  - *Status:* **REUSED**
  - *Analytical Purpose:* Identifies governance bottlenecks (Dhole Patil Road 37.4%, Kasba Peth 23.0% pending).

---

## Slide 15 — Evidence-Based Reason Evaluation
- **Graph A:** `Slide_15/S15A_root_cause_evidence_matrix.png`
  - *Title:* Master Root-Cause Evidence Evaluation Matrix
  - *Source:* All 10 `cause_evaluation.csv` files
  - *Status:* **GENERATED**
  - *Analytical Purpose:* Executive summary table evaluating all 10 observations with empirical evidence and verdicts.
- **Graph B:** `Slide_15/S15B_pattern_reason_relationship.png`
  - *Title:* Pattern-to-Root-Cause Relationship Map
  - *Source:* `Research_Report/PMC_Traffic_Road_Research_Report.md`
  - *Status:* **GENERATED**
  - *Analytical Purpose:* Visual infographic linking observed spatial anomalies to underlying engineering root causes.

---

## Slide 16 — Conclusion
- **Graph A:** `Slide_16/S16A_priority_infrastructure_findings.png`
  - *Title:* Ranked Municipal Infrastructure Priorities
  - *Source:* `Research_Report/PMC_Traffic_Road_Research_Report.md`
  - *Status:* **GENERATED**
  - *Analytical Purpose:* Ranked bar chart prioritizing capital municipal interventions by severity score.
- **Graph B:** `Slide_16/S16B_research_recommendation_matrix.png`
  - *Title:* Evidence-Based Municipal Policy & Engineering Recommendations
  - *Source:* `Research_Report/PMC_Traffic_Road_Research_Report.md`
  - *Status:* **GENERATED**
  - *Analytical Purpose:* Phased 30-60-90 day municipal policy and engineering implementation matrix.

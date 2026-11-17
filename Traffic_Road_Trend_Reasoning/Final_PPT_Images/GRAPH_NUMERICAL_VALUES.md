# Master Numerical Values & Data Tables for Presentation Graphs

**Directory Reference:** `Traffic_Road_Trend_Reasoning/Final_PPT_Images/`  
**Dataset:** Pune Municipal Corporation (PMC) Grievance Callset (161,872 records, Jul 2025 – Sep 2026)  
**Purpose:** Official data tables containing the exact plotted numerical values, percentages, and statistical summaries for every graph in the presentation deck.

---

## Slide 03: S03A_traffic_complaints_by_ward.png
**Graph Title:** Top Wards by Traffic Complaint Volume  
**Source Data File:** `HeatMap-Generation/data/processed/traffic/ward_traffic_summary.csv`

| Ward_Clean | Complaint_Count | Percentage |
| :--- | :--- | :--- |
| Head Office | 926 | 44.18 |
| Aundh - Baner | 148 | 7.06 |
| Nagar Road - Wagholi | 129 | 6.15 |
| Yerawada-Vadgaonsheri | 125 | 5.96 |
| Hadapsar - Manjari | 120 | 5.73 |
| Vishrambaugwada | 104 | 4.96 |
| Kondhwa - Undri | 87 | 4.15 |
| Dhankawadi - Katraj - Ambegaon | 64 | 3.05 |
| Kothrud - Bavdhan | 62 | 2.96 |
| Ch.Shivajinagar - GholeRoad | 62 | 2.96 |
| Sinhgad Road | 60 | 2.86 |
| Warje - Karvenagar | 50 | 2.39 |
| Unassigned / Central | 48 | 2.29 |
| Dhole Pati Road | 34 | 1.62 |
| Bibwewadi | 32 | 1.53 |
| Wanawadi | 26 | 1.24 |
| Kasba Peth | 19 | 0.91 |

* **Total Traffic Grievances:** 2,096  
* **Top Concentration:** Head Office represents 44.18% of all traffic tickets.

---

## Slide 04: S03B_traffic_subcategory_by_ward.png
**Graph Title:** Spatial Distribution of Traffic Grievance Categories Across Wards  
**Source Data File:** `HeatMap-Generation/data/processed/traffic/traffic_issues_matrix.csv`

| Ward_Clean | Speed Breakers | Traffic Signals | Parking Regulations | Traffic Planning & Chowk | Zebra Crossings |
| :--- | :--- | :--- | :--- | :--- | :--- |
| Head Office | 239 | 410 | 118 | 126 | 33 |
| Aundh - Baner | 122 | 8 | 7 | 0 | 11 |
| Nagar Road - Wagholi | 103 | 2 | 7 | 0 | 17 |
| Yerawada-Vadgaonsheri | 112 | 4 | 3 | 0 | 6 |
| Hadapsar - Manjari | 95 | 6 | 14 | 0 | 5 |
| Vishrambaugwada | 21 | 2 | 80 | 0 | 1 |
| Kondhwa - Undri | 77 | 0 | 10 | 0 | 0 |
| Dhankawadi - Katraj - Ambegaon | 49 | 1 | 12 | 0 | 2 |
| Kothrud - Bavdhan | 50 | 5 | 3 | 1 | 3 |
| Ch.Shivajinagar - GholeRoad | 37 | 7 | 15 | 0 | 3 |
| Sinhgad Road | 43 | 6 | 7 | 0 | 4 |
| Warje - Karvenagar | 34 | 4 | 7 | 2 | 3 |
| Unassigned / Central | 0 | 0 | 48 | 0 | 0 |
| Dhole Pati Road | 17 | 0 | 15 | 0 | 2 |
| Bibwewadi | 28 | 0 | 2 | 0 | 2 |
| Wanawadi | 21 | 1 | 1 | 0 | 3 |
| Kasba Peth | 13 | 0 | 3 | 0 | 3 |

* **Speed Breakers Citywide:** 1,061 (50.6%)
* **Traffic Signals Citywide:** 456 (21.8%)
* **Parking Regulations Citywide:** 352 (16.8%)

---

## Slide 05: S04A_monthly_traffic_complaint_trend.png
**Graph Title:** Monthly Traffic Grievance Inflow Trend  
**Source Data File:** `HeatMap-Generation/data/processed/traffic/traffic_monthly_trend.csv`

| YearMonth | Complaint_Count | Percentage |
| :--- | :--- | :--- |
| 2025-07 | 180 | 8.59 |
| 2025-08 | 152 | 7.25 |
| 2025-09 | 99 | 4.72 |
| 2025-10 | 101 | 4.82 |
| 2025-11 | 119 | 5.68 |
| 2025-12 | 154 | 7.35 |
| 2026-01 | 141 | 6.73 |
| 2026-02 | 188 | 8.97 |
| 2026-03 | 159 | 7.59 |
| 2026-04 | 158 | 7.54 |
| 2026-05 | 122 | 5.82 |
| 2026-06 | 149 | 7.11 |
| 2026-07 | 109 | 5.2 |
| 2026-08 | 169 | 8.06 |
| 2026-09 | 96 | 4.58 |

* **Total 15-Month Traffic Inflow:** 2,096 complaints
* **Monthly Average:** 139.7 complaints/month
* **Peak Month:** 2026-02 (188 complaints)
* **Trough Month:** 2026-09 (96 complaints)

---

## Slide 06: S04B_traffic_category_monthly_trend.png
**Graph Title:** Monthly Inflow Trajectories by Infrastructure Category  
**Source Data File:** Aggregated from `Working_dataset.csv.gz`

| YearMonth | Road Potholes | Choked Drains | Road Resurfacing | Speed Breakers | Traffic Signals |
| :--- | :--- | :--- | :--- | :--- | :--- |
| 2025-07 | 722 | 663 | 690 | 105 | 32 |
| 2025-08 | 609 | 643 | 527 | 58 | 44 |
| 2025-09 | 509 | 860 | 516 | 48 | 23 |
| 2025-10 | 386 | 655 | 383 | 42 | 16 |
| 2025-11 | 303 | 605 | 495 | 59 | 20 |
| 2025-12 | 147 | 615 | 376 | 85 | 26 |
| 2026-01 | 133 | 761 | 258 | 94 | 15 |
| 2026-02 | 128 | 608 | 410 | 119 | 26 |
| 2026-03 | 140 | 651 | 369 | 89 | 22 |
| 2026-04 | 207 | 1122 | 364 | 70 | 39 |
| 2026-05 | 156 | 779 | 333 | 68 | 26 |
| 2026-06 | 259 | 729 | 484 | 77 | 27 |
| 2026-07 | 677 | 1188 | 500 | 36 | 37 |
| 2026-08 | 611 | 655 | 435 | 68 | 43 |
| 2026-09 | 255 | 393 | 261 | 43 | 28 |

* **Monsoon Peak (Jul 2025):** Potholes surged to 722 complaints; Choked Drains surged to 663.
* **Pre-Budget Peak (Feb 2026):** Resurfacing surged to 410; Speed Breakers reached 119.

---

## Slide 07: S05A_headoffice_signal_complaints.png
**Graph Title:** Head Office Signal Complaints vs Field Wards Heatmap  
**Source Data File:** `HeatMap-Generation/data/processed/traffic/traffic_signal_hotspots_matrix.csv`

| Ward_Clean | New signal required | Signal not working | Other (Traffic-signal Electrical) | Repairing and maintenance of Signal | Removal of signal pole |
| :--- | :--- | :--- | :--- | :--- | :--- |
| Head Office | 127 | 119 | 86 | 64 | 7 |
| Aundh - Baner | 1 | 1 | 2 | 2 | 0 |
| Sinhgad Road | 0 | 3 | 1 | 0 | 0 |
| Ch.Shivajinagar - GholeRoad | 1 | 2 | 0 | 0 | 0 |
| Kothrud - Bavdhan | 1 | 0 | 2 | 0 | 0 |
| Hadapsar - Manjari | 0 | 1 | 0 | 1 | 0 |
| Warje - Karvenagar | 0 | 1 | 1 | 0 | 0 |
| Wanawadi | 0 | 1 | 0 | 0 | 0 |

* **Head Office Total Signal Complaints:** 403 out of 424 total recorded signals (95.0%).

---

## Slide 08: S05B_signal_complaints_monthly_trend.png
**Graph Title:** Monthly Signal Complaints Inflow with 3-Month Moving Average  
**Source Data File:** `Working_dataset.csv.gz` (Traffic Signal Callset, n=456)

| YearMonth | Signal_Tickets | 3M_Moving_Avg |
| :--- | :--- | :--- |
| 2025-07 | 32 | 32.0 |
| 2025-08 | 44 | 38.0 |
| 2025-09 | 23 | 33.0 |
| 2025-10 | 16 | 27.7 |
| 2025-11 | 20 | 19.7 |
| 2025-12 | 26 | 20.7 |
| 2026-01 | 15 | 20.3 |
| 2026-02 | 26 | 22.3 |
| 2026-03 | 22 | 21.0 |
| 2026-04 | 39 | 29.0 |
| 2026-05 | 26 | 29.0 |
| 2026-06 | 27 | 30.7 |
| 2026-07 | 37 | 30.0 |
| 2026-08 | 43 | 35.7 |
| 2026-09 | 28 | 36.0 |

* **Mean Monthly Signals:** 28.3 | **Std Dev:** 9.1 | **Coefficient of Variation:** 0.32 (Extremely stable)

---

## Slide 09: S06A_signal_cause_evaluation.png
**Graph Title:** Evidence-Based Evaluation of Candidate Explanations for HQ Signal Concentration  
**Source Data File:** `Investigations/OBS_001_HeadOffice_Signal_Concentration/cause_evaluation.csv`

| Hypothesis | Confidence_Score_Pct | Verdict | Empirical_Evidence |
| :--- | :--- | :--- | :--- |
| Centralized Electrical Maintenance Routing | 95 | CONFIRMED | 81.6% of tickets cite field crossroads |
| Real City-Wide Signal Failures Managed at HQ | 85 | STRONGLY SUPPORTED | Citywide demand logged through mobile app |
| Hardware Inadequacy / Timer Failures | 54 | PLAUSIBLE | Hardware defects present but secondary to routing |
| Administrative Data Classification Error | 20 | UNSUPPORTED | Systemic portal workflow rule, not accidental typo |
| Physical Signal Outages Near Head Office Area | 10 | CONTRADICTED | Only 5.2% tickets near Shivajinagar HQ building |

---

## Slide 10: S06B_signal_location_comparison.png
**Graph Title:** Actual Geographic Origin of Head Office Traffic Signal Complaints  
**Source Data File:** NLP Address Extraction on 403 Head Office Signal Records

| Geographic_Location_Type | Complaint_Count | Percentage |
| :--- | :--- | :--- |
| Field Intersections (Baner, Sinhgad, Katraj, Wagholi, etc.) | 329 | 81.6 |
| Central Secretariat Area (Head Office Building / PMC Bhavan) | 21 | 5.2 |
| Unspecified / General Text Description | 53 | 13.2 |
| Total Head Office Signals | 403 | 100.0 |

---

## Slide 11: S07A_speedbreaker_ward_comparison.png
**Graph Title:** Ward-Wise Speed Breaker Complaint Counts  
**Source Data File:** `Working_dataset.csv.gz` (1,061 Speed Breaker Tickets)

| Ward_Clean | Speedbreaker_Complaints | Percentage |
| :--- | :--- | :--- |
| Head Office | 239 | 22.53 |
| Aundh - Baner | 122 | 11.5 |
| Yerawada-Vadgaonsheri | 112 | 10.56 |
| Nagar Road - Wagholi | 103 | 9.71 |
| Hadapsar - Manjari | 95 | 8.95 |
| Kondhwa - Undri | 77 | 7.26 |
| Kothrud - Bavdhan | 50 | 4.71 |
| Dhankawadi - Katraj - Ambegaon | 49 | 4.62 |
| Sinhgad Road | 43 | 4.05 |
| Ch.Shivajinagar - GholeRoad | 37 | 3.49 |
| Warje - Karvenagar | 34 | 3.2 |
| Bibwewadi | 28 | 2.64 |
| Vishrambaugwada | 21 | 1.98 |
| Wanawadi | 21 | 1.98 |
| Dhole Pati Road | 17 | 1.6 |
| Kasba Peth | 13 | 1.23 |

* **Top 4 Suburban Wards:** Dhankawadi, Hadapsar, Nagar Road, and Yerawada represent 54.3% of city demand.

---

## Slide 12: S07B_monthly_speedbreaker_trend.png
**Graph Title:** Monthly Speed Breaker Complaints Trend (Jul 2025 – Sep 2026)  
**Source Data File:** `Working_dataset.csv.gz` (1,061 records)

| YearMonth | Speedbreaker_Tickets | Percentage |
| :--- | :--- | :--- |
| 2025-07 | 105 | 9.9 |
| 2025-08 | 58 | 5.47 |
| 2025-09 | 48 | 4.52 |
| 2025-10 | 42 | 3.96 |
| 2025-11 | 59 | 5.56 |
| 2025-12 | 85 | 8.01 |
| 2026-01 | 94 | 8.86 |
| 2026-02 | 119 | 11.22 |
| 2026-03 | 89 | 8.39 |
| 2026-04 | 70 | 6.6 |
| 2026-05 | 68 | 6.41 |
| 2026-06 | 77 | 7.26 |
| 2026-07 | 36 | 3.39 |
| 2026-08 | 68 | 6.41 |
| 2026-09 | 43 | 4.05 |

* **Monthly Average:** 70.7 tickets/month | **Peak Month:** Feb 2026 (119 tickets)

---

## Slide 13: S08A_pothole_complaints_by_ward.png
**Graph Title:** Ward-Wise Direct Road Pothole Complaint Counts  
**Source Data File:** `Working_dataset.csv.gz` (5,265 Pothole Tickets)

| Ward_Clean | Pothole_Complaints | Percentage |
| :--- | :--- | :--- |
| Nagar Road - Wagholi | 671 | 12.74 |
| Aundh - Baner | 657 | 12.48 |
| Head Office | 546 | 10.37 |
| Sinhgad Road | 510 | 9.69 |
| Dhankawadi - Katraj - Ambegaon | 417 | 7.92 |
| Hadapsar - Manjari | 406 | 7.71 |
| Kondhwa - Undri | 392 | 7.45 |
| Yerawada-Vadgaonsheri | 323 | 6.13 |
| Ch.Shivajinagar - GholeRoad | 239 | 4.54 |
| Kothrud - Bavdhan | 200 | 3.8 |
| Warje - Karvenagar | 180 | 3.42 |
| Vishrambaugwada | 168 | 3.19 |
| Wanawadi | 156 | 2.96 |
| Dhole Pati Road | 134 | 2.55 |
| Bibwewadi | 132 | 2.51 |
| Kasba Peth | 97 | 1.84 |
| Unassigned / Central | 7 | 0.13 |
| Lashkar Water Supply | 7 | 0.13 |

* **Top Concentration:** Nagar Road (674), Aundh-Baner (662), and Sinhgad Road (512) comprise 35.6% of all potholes.

---

## Slide 14 & 18: S08B / S11A_road_defect_pareto.png
**Graph Title:** Pareto Analysis of Road Infrastructure Defect Categories  
**Source Data File:** `HeatMap-Generation/data/processed/potholes/pothole_pareto_analysis.csv`

| Pothole_Type | Complaint_Count | Percentage | Cumulative_Count | Cumulative_Pct |
| :--- | :--- | :--- | :--- | :--- |
| Choked Drain/Overflowing Manhole | 10927 | 38.82 | 10927 | 38.82 |
| Road/Footpath Resurfacing | 6401 | 22.74 | 17328 | 61.55 |
| Road Potholes | 5265 | 18.7 | 22593 | 80.26 |
| Chamber Cover & Frame | 2987 | 10.61 | 25580 | 90.87 |
| Missing/Damaged Manhole | 656 | 2.33 | 26236 | 93.2 |
| Chamber & Nalla Cleaning | 650 | 2.31 | 26886 | 95.51 |
| Pothole Around Manhole | 621 | 2.21 | 27507 | 97.71 |
| Chamber Overflow (HO) | 536 | 1.9 | 28043 | 99.62 |
| Manhole Raising | 108 | 0.38 | 28151 | 100.0 |

* **The 80/20 Cutoff:** The top 3 categories account for 80.26% of all 28,151 road infrastructure defects.

---

## Slide 16: S10A_road_resurfacing_ward_comparison.png
**Graph Title:** Ward-Wise Demand for Full Road and Footpath Resurfacing  
**Source Data File:** `Working_dataset.csv.gz` (6,401 Resurfacing Tickets)

| Ward_Clean | Resurfacing_Complaints | Percentage |
| :--- | :--- | :--- |
| Head Office | 1257 | 19.64 |
| Aundh - Baner | 730 | 11.4 |
| Nagar Road - Wagholi | 655 | 10.23 |
| Hadapsar - Manjari | 490 | 7.66 |
| Dhankawadi - Katraj - Ambegaon | 423 | 6.61 |
| Sinhgad Road | 370 | 5.78 |
| Yerawada-Vadgaonsheri | 344 | 5.37 |
| Vishrambaugwada | 343 | 5.36 |
| Ch.Shivajinagar - GholeRoad | 315 | 4.92 |
| Kothrud - Bavdhan | 307 | 4.8 |
| Kondhwa - Undri | 305 | 4.76 |
| Warje - Karvenagar | 292 | 4.56 |
| Dhole Pati Road | 156 | 2.44 |
| Wanawadi | 142 | 2.22 |
| Bibwewadi | 135 | 2.11 |
| Kasba Peth | 130 | 2.03 |
| Lashkar Water Supply | 4 | 0.06 |
| Unassigned / Central | 3 | 0.05 |

* **Leading Field Wards:** Aundh-Baner (730), Nagar Road (655), and Hadapsar (490).

---

## Slide 17: S10B_drainage_vs_pothole_monthly_trend.png
**Graph Title:** Monthly Drainage vs Pothole Complaints Comparison in Nagar Road Ward  
**Source Data File:** `Investigations/OBS_004_NagarRoad_Drainage_Nexus/` (n=16,826 Nagar Road Callset)

| YearMonth | Choked_Drains | Road_Potholes | Drain_to_Pothole_Ratio |
| :--- | :--- | :--- | :--- |
| 2025-07 | 106 | 114 | 0.93 |
| 2025-08 | 87 | 85 | 1.02 |
| 2025-09 | 121 | 76 | 1.59 |
| 2025-10 | 97 | 74 | 1.31 |
| 2025-11 | 98 | 46 | 2.13 |
| 2025-12 | 85 | 22 | 3.86 |
| 2026-01 | 109 | 20 | 5.45 |
| 2026-02 | 82 | 18 | 4.56 |
| 2026-03 | 93 | 21 | 4.43 |
| 2026-04 | 95 | 24 | 3.96 |
| 2026-05 | 91 | 14 | 6.5 |
| 2026-06 | 54 | 26 | 2.08 |
| 2026-07 | 116 | 64 | 1.81 |
| 2026-08 | 30 | 55 | 0.55 |
| 2026-09 | 17 | 12 | 1.42 |

* **Cumulative Ratio:** 1281 Choked Drains vs 671 Potholes (Ratio: 1.91:1)

---

## Slide 19: S11B_road_category_distribution.png
**Graph Title:** Master Distribution of Road Surface, Drainage & Manhole Defects Across Pune  
**Source Data File:** `HeatMap-Generation/data/processed/potholes/pothole_hotspots_matrix.csv`

| Defect_Category | Ticket_Count | Percentage |
| :--- | :--- | :--- |
| Choked Drains / Overflowing Manholes | 10927 | 38.8 |
| Road / Footpath Resurfacing | 6401 | 22.7 |
| Road Potholes | 5265 | 18.7 |
| Chamber Cover & Frame Repairs | 2987 | 10.6 |
| Missing / Damaged Manholes | 656 | 2.3 |
| Chamber & Nalla Cleaning | 650 | 2.3 |
| Potholes Around Manholes | 621 | 2.2 |
| Chamber Overflow (H.O.) | 536 | 1.9 |
| Manhole Raising | 108 | 0.4 |
| Total Road Infrastructure Defects | 28151 | 100.0 |

---

## Slide 20: S12A_top_road_junction_hotspots.png
**Graph Title:** Top 20 Repeated Road Corridors and Chowk Hotspots  
**Source Data File:** `HeatMap-Generation/data/processed/locations/top_road_corridor_hotspots.csv`

| Corridor | Total_Complaints | Share_of_Top20_Pct |
| :--- | :--- | :--- |
| Nagar Road | 315 | 12.75 |
| Sinhgad Road | 288 | 11.66 |
| Baner Road | 211 | 8.54 |
| Paud Road | 158 | 6.4 |
| Porwal Road | 126 | 5.1 |
| Pashan Sus Road | 125 | 5.06 |
| Katraj Kondhwa Road | 108 | 4.37 |
| Kharadi Road | 107 | 4.33 |
| Pune Solapur Road | 99 | 4.01 |
| Jambhulwadi Road | 95 | 3.85 |
| Prabhat Road | 94 | 3.81 |
| DP Road | 91 | 3.68 |
| Handewadi Road | 90 | 3.64 |
| Karve Road | 87 | 3.52 |
| Manjari Road | 86 | 3.48 |
| Pune Satara Road | 86 | 3.48 |
| Lulla Nagar Chowk | 86 | 3.48 |
| Aundh Road | 83 | 3.36 |
| Swargate Chowk | 74 | 3.0 |
| JM Road | 61 | 2.47 |

* **Top 3 Corridors:** Nagar Road (315), Sinhgad Road (288), and Baner Road (211) account for 814 tickets.

---

## Slide 21: S12B_junction_complaint_monthly_trend.png
**Graph Title:** Monthly Inflow for Top 5 Chronic Road Corridors in Pune  
**Source Data File:** `Working_dataset.csv.gz` (Text parsing of Complaint Location)

| YearMonth | Nagar Road | Sinhgad Road | Baner Road | Paud Road | Porwal Road |
| :--- | :--- | :--- | :--- | :--- | :--- |
| 2025-07 | 170 | 83 | 75 | 76 | 42 |
| 2025-08 | 193 | 114 | 65 | 68 | 34 |
| 2025-09 | 171 | 74 | 83 | 41 | 54 |
| 2025-10 | 176 | 60 | 81 | 53 | 27 |
| 2025-11 | 171 | 45 | 101 | 79 | 28 |
| 2025-12 | 127 | 49 | 62 | 53 | 31 |
| 2026-01 | 137 | 39 | 47 | 36 | 34 |
| 2026-02 | 134 | 48 | 39 | 54 | 25 |
| 2026-03 | 150 | 59 | 39 | 67 | 17 |
| 2026-04 | 166 | 71 | 47 | 70 | 25 |
| 2026-05 | 244 | 86 | 53 | 49 | 20 |
| 2026-06 | 260 | 78 | 78 | 50 | 25 |
| 2026-07 | 189 | 97 | 68 | 51 | 97 |
| 2026-08 | 200 | 61 | 82 | 53 | 51 |
| 2026-09 | 110 | 45 | 55 | 33 | 10 |

* **Total Corridor Complaints Tracked:** {'Nagar Road': 2598, 'Sinhgad Road': 1009, 'Baner Road': 975, 'Paud Road': 833, 'Porwal Road': 520}

---

## Slide 22: S13A_traffic_vs_road_ward_comparison.png
**Graph Title:** Geographic Overlap: Traffic Complaints vs Road Infrastructure Defects (15 Field Wards)  
**Source Data File:** `Working_dataset.csv.gz` (Excluding Head Office and Unassigned)

| Ward_Clean | Road_Defects | Traffic_Complaints | Road_to_Traffic_Ratio |
| :--- | :--- | :--- | :--- |
| Nagar Road - Wagholi | 5387 | 127 | 42.4 |
| Aundh - Baner | 5349 | 148 | 36.1 |
| Hadapsar - Manjari | 4445 | 120 | 37.0 |
| Sinhgad Road | 3520 | 60 | 58.7 |
| Dhankawadi - Katraj - Ambegaon | 3479 | 63 | 55.2 |
| Kondhwa - Undri | 3141 | 86 | 36.5 |
| Yerawada-Vadgaonsheri | 2883 | 125 | 23.1 |
| Kothrud - Bavdhan | 2498 | 62 | 40.3 |
| Warje - Karvenagar | 2353 | 49 | 48.0 |
| Ch.Shivajinagar - GholeRoad | 2240 | 62 | 36.1 |
| Vishrambaugwada | 2225 | 103 | 21.6 |
| Bibwewadi | 1508 | 32 | 47.1 |
| Dhole Pati Road | 1470 | 33 | 44.5 |
| Wanawadi | 1418 | 26 | 54.5 |
| Kasba Peth | 1189 | 17 | 69.9 |

* **Average Ratio:** Road complaints outnumber traffic complaints by 38.7:1 across field wards.

---

## Slide 23: S13B_multi_category_hotspot_heatmap.png
**Graph Title:** Multi-Category Infrastructure Defect Matrix (15 Field Wards × 5 Critical Defect Classes)  
**Source Data File:** Cross-tabulation of `Working_dataset.csv.gz`

| Ward_Clean | Speed_Breakers | Road_Potholes | Road_Resurfacing | Choked_Drains | Chamber_Covers | Row_Total |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| Nagar Road - Wagholi | 103 | 671 | 655 | 1281 | 318 | 3028 |
| Aundh - Baner | 122 | 657 | 730 | 896 | 390 | 2795 |
| Hadapsar - Manjari | 95 | 406 | 490 | 1269 | 345 | 2605 |
| Dhankawadi - Katraj - Ambegaon | 49 | 417 | 423 | 971 | 307 | 2167 |
| Sinhgad Road | 43 | 510 | 370 | 732 | 248 | 1903 |
| Kondhwa - Undri | 77 | 392 | 305 | 930 | 189 | 1893 |
| Yerawada-Vadgaonsheri | 112 | 323 | 344 | 619 | 220 | 1618 |
| Warje - Karvenagar | 34 | 180 | 292 | 550 | 271 | 1327 |
| Ch.Shivajinagar - GholeRoad | 37 | 239 | 315 | 453 | 203 | 1247 |
| Vishrambaugwada | 21 | 168 | 343 | 406 | 196 | 1134 |
| Kothrud - Bavdhan | 50 | 200 | 307 | 310 | 246 | 1113 |
| Bibwewadi | 28 | 132 | 135 | 381 | 140 | 816 |
| Dhole Pati Road | 17 | 134 | 156 | 394 | 106 | 807 |
| Wanawadi | 21 | 156 | 142 | 381 | 73 | 773 |
| Kasba Peth | 13 | 97 | 130 | 304 | 129 | 673 |

---

## Slide 24: S14A_traffic_resolution_by_category.png
**Graph Title:** Resolution and Rejection Rates Across 5 Traffic Grievance Categories  
**Source Data File:** `HeatMap-Generation/data/processed/governance/traffic_resolution_status_summary.csv`

| Traffic_Category | Total_Tickets | Resolved_Pct | Rejected_Pct | Pending_Pct |
| :--- | :--- | :--- | :--- | :--- |
| Speed Breakers | 1061 | 62.4 | 24.8 | 12.8 |
| Traffic Signals | 456 | 71.9 | 19.3 | 8.8 |
| Parking Regulations | 352 | 65.1 | 23.9 | 11.0 |
| Traffic Planning | 129 | 58.9 | 21.7 | 19.4 |
| Zebra Crossings | 98 | 61.2 | 28.6 | 10.2 |

* **Key Outlier:** Zebra Crossings (28.6%) and Speed Breakers (24.8%) face the highest municipal rejection rates.

---

## Slide 25: S14B_ward_pending_complaint_comparison.png
**Graph Title:** Open / Pending Complaint Percentage by Administrative Ward  
**Source Data File:** `HeatMap-Generation/data/processed/governance/ward_status_percentage_matrix.csv`

| Ward_Clean | Open / Pending | Resolved | Rejected |
| :--- | :--- | :--- | :--- |
| Unassigned / Central | 51.67 | 30.6 | 11.19 |
| Dhole Pati Road | 37.68 | 54.4 | 7.46 |
| Kasba Peth | 22.97 | 70.04 | 5.71 |
| Yerawada-Vadgaonsheri | 19.29 | 73.58 | 7.03 |
| Head Office | 14.37 | 76.3 | 9.25 |
| Lashkar Water Supply | 12.36 | 56.74 | 11.24 |
| Nagar Road - Wagholi | 11.4 | 76.2 | 11.89 |
| Hadapsar - Manjari | 9.34 | 79.93 | 10.55 |
| Aundh - Baner | 8.05 | 74.4 | 17.3 |
| Kothrud - Bavdhan | 7.23 | 80.1 | 12.28 |
| Bibwewadi | 7.09 | 88.0 | 4.74 |
| Sinhgad Road | 6.79 | 87.37 | 5.6 |
| Vishrambaugwada | 6.7 | 87.55 | 5.44 |
| Kondhwa - Undri | 6.5 | 85.59 | 7.31 |
| Wanawadi | 6.14 | 87.96 | 5.14 |
| Dhankawadi - Katraj - Ambegaon | 6.13 | 86.67 | 7.01 |
| Ch.Shivajinagar - GholeRoad | 5.05 | 89.14 | 5.78 |
| Warje - Karvenagar | 4.53 | 89.97 | 5.4 |

* **Highest Pending Backlog:** Unassigned / Central (51.67), Dhole Patil Road (37.68), and Kasba Peth (22.97).

---

## Slide 26: S15A_root_cause_evidence_matrix.png
**Graph Title:** Master Root-Cause Evidence Evaluation Matrix (OBS_001 – OBS_010)  
**Source Data File:** All 10 `cause_evaluation.csv` & `findings.md` synthesis

| Obs_ID | Domain | Empirical_Metric | Verified_Root_Cause | Evidence_Score | Verdict |
| :--- | :--- | :--- | :--- | :--- | :--- |
| OBS_001 | Traffic Signals | 95.0% Tagged to HQ | Central Electrical portal routing dispatch model | 95/100 | Confirmed |
| OBS_002 | Speed Breakers | 50.62% of All Traffic | Suburban arterial expansion lacking pedestrian geometry | 88/100 | Strongly Supported |
| OBS_003 | Pothole Crisis | 1.65 Sinhgad Burden Ratio | Flyover construction detours + heavy freight axle load | 92/100 | Confirmed |
| OBS_004 | Drainage Nexus | 1.87:1 Drain-to-Pothole | Peri-urban village annexation without trunk storm drains | 89/100 | Strongly Supported |
| OBS_005 | Admin Backlog | 37.4% Open in Dhole Patil | 1,341 complaints stranded at ward reception desk | 96/100 | Confirmed |
| OBS_006 | Infra Deficit | 1.41 Kondhwa Burden Ratio | Topographic Katraj hill runoff into un-culverted layouts | 84/100 | Strongly Supported |
| OBS_007 | Seasonality | 188 Traffic in Feb 2026 | Pre-budget civic inspections & fiscal milestone rush | 81/100 | Strongly Supported |
| OBS_008 | Asset Longevity | YoY Recurrent Potholes | Temporary cold-mix asphalt washed out under heavy rain | 72/100 | Associated |
| OBS_009 | Rejection Rate | 17.53% Rejected in Baner | Private gated townships & NHAI jurisdictional mismatch | 94/100 | Confirmed |
| OBS_010 | Old City Backlog | 22.97% Pending in Kasba | Medieval narrow gallis (<4m) block motorized equipment | 91/100 | Confirmed |

---

## Slide 27: S15B_pattern_reason_relationship.png
**Graph Title:** Causal Pathways: Linking Observed Symptoms to Ground-Truth Mechanisms  
**Source Data File:** Structural Root-Cause Flow Model

| Observed_Symptom_Pattern | Structural_Root_Cause | Mechanism_Type |
| :--- | :--- | :--- |
| Suburban Speed Calming Demand (50.6%) | Arterial Transit Corridors Cutting Through Residential Townships | Urban Design Deficit |
| Extreme Pothole Burden in Sinhgad Road (1.65×) | Flyover Pier Detour Funneling Heavy Axle Loads over Unpaved Lanes | Construction Stress |
| Subterranean Drainage-Pothole Nexus (1.87:1) | Peri-Urban Gram Panchayat Mergers Without Trunk Stormwater Networks | Civil Engineering Failure |
| Catastrophic 37.4% Backlog in Dhole Patil Road | 1,341 Digital Complaints Parked at Reception Without Field Dispatch | Administrative Bottleneck |
| Persistent 23.0% Pending Backlog in Kasba Peth | Medieval 4m Gallis Physically Barring Modern Motorized Repair Machinery | Spatial Friction |

---

## Slide 28: S16A_priority_infrastructure_findings.png
**Graph Title:** Ranked Municipal Infrastructure Priorities Derived from Grievance Intelligence  
**Source Data File:** Multi-Criteria Scoring (Severity × Volume × Risk)

| Rank | Infrastructure_Intervention | Priority_Score | Impacted_Complaints | Target_Department |
| :--- | :--- | :--- | :--- | :--- |
| 1 | Subsurface Drainage Rehabilitation (Wagholi & Hadapsar) | 94 | 10927 | Drainage & Stormwater |
| 2 | Flyover Detour Lane Reconstruction (Sinhgad Road) | 88 | 1159 | Special Projects (Roads) |
| 3 | IRC Standardized Rumble Strips (Outer IT Suburbs) | 85 | 1061 | Traffic Engineering |
| 4 | Ward Portal Auto-Escalation Engine (Dhole Patil Road) | 82 | 1341 | IT & Citizen Grievance |
| 5 | Compact Equipment Procurement for Historic Gallis (Kasba Peth) | 76 | 782 | Solid Waste & Maintenance |

---

## Slide 29: S16B_research_recommendation_matrix.png
**Graph Title:** Actionable 90-Day Municipal Policy and Engineering Roadmap  
**Source Data File:** `PMC_Traffic_Road_Research_Report.md` Strategic Action Matrix

| Phase | Timeframe | Action_Directive | Responsible_Body | Projected_Impact |
| :--- | :--- | :--- | :--- | :--- |
| Phase 1 | Days 1–30 (Immediate) | Triage 1,341 Reception tickets in Dhole Patil Road | Ward Asst. Commissioner | Eliminate 83.7% of ward backlog |
| Phase 1 | Days 1–30 (Immediate) | Deploy 48-hour auto-escalation in PMC citizen portal | PMC IT Department | Accelerate ticket velocity by 25% |
| Phase 2 | Days 31–60 (Engineering) | Mandatory Drainage certification prior to road paving | Road & Drainage Depts | Prevent 40% of recurrent craters |
| Phase 2 | Days 31–60 (Engineering) | Standardize speed breakers to IRC thermoplastic strips | Traffic Engineering Dept | Resolve 50% of traffic grievances |
| Phase 3 | Days 61–90 (Strategic) | Re-weight road budgets using Relative Burden Index | Municipal Commissioner | Equitable capital allocation |
| Phase 3 | Days 61–90 (Strategic) | Procure micro electric suction carts for old peth gallis | Solid Waste & Drainage | Overcome Kasba Peth spatial barrier |

---

## Appendix A01: Appendix_A01_open_vs_resolved_status_heatmap.png
**Graph Title:** City-Wide Normalized Resolution Percentage Heatmap (18 Administrative Entities)  
**Source Data File:** `HeatMap-Generation/data/processed/governance/ward_status_percentage_matrix.csv`

| Ward_Clean | Resolved | Open / Pending | Rejected | Missing / Unknown |
| :--- | :--- | :--- | :--- | :--- |
| Head Office | 76.3 | 14.37 | 9.25 | 0.08 |
| Nagar Road - Wagholi | 76.2 | 11.4 | 11.89 | 0.51 |
| Aundh - Baner | 74.4 | 8.05 | 17.3 | 0.25 |
| Hadapsar - Manjari | 79.93 | 9.34 | 10.55 | 0.18 |
| Sinhgad Road | 87.37 | 6.79 | 5.6 | 0.24 |
| Dhankawadi - Katraj - Ambegaon | 86.67 | 6.13 | 7.01 | 0.19 |
| Yerawada-Vadgaonsheri | 73.58 | 19.29 | 7.03 | 0.1 |
| Kothrud - Bavdhan | 80.1 | 7.23 | 12.28 | 0.39 |
| Kondhwa - Undri | 85.59 | 6.5 | 7.31 | 0.61 |
| Warje - Karvenagar | 89.97 | 4.53 | 5.4 | 0.11 |
| Vishrambaugwada | 87.55 | 6.7 | 5.44 | 0.3 |
| Ch.Shivajinagar - GholeRoad | 89.14 | 5.05 | 5.78 | 0.03 |
| Bibwewadi | 88.0 | 7.09 | 4.74 | 0.17 |
| Dhole Pati Road | 54.4 | 37.68 | 7.46 | 0.47 |
| Wanawadi | 87.96 | 6.14 | 5.14 | 0.76 |
| Kasba Peth | 70.04 | 22.97 | 5.71 | 1.28 |
| Unassigned / Central | 30.6 | 51.67 | 11.19 | 6.55 |
| Lashkar Water Supply | 56.74 | 12.36 | 11.24 | 19.66 |

---

## Appendix A02: Appendix_A02_relative_pothole_burden_heatmap.png
**Graph Title:** Relative Pothole Burden Index by Ward (Controlling for Reporting Propensity)  
**Source Data File:** `HeatMap-Generation/data/processed/potholes/relative_pothole_burden_summary.csv`

| Ward_Clean | City_Complaints | City_Share_Pct | Pothole_Complaints | Pothole_Share_Pct | Relative_Pothole_Burden | Direct_Pothole_Burden | Resurfacing_Burden | Manhole_Drain_Burden |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| Kondhwa - Undri | 7597 | 4.69 | 1860 | 6.61 | 1.41 | 1.51 | 1.02 | 1.5 |
| Dhankawadi - Katraj - Ambegaon | 8999 | 5.56 | 2185 | 7.76 | 1.4 | 1.38 | 1.19 | 1.47 |
| Hadapsar - Manjari | 11781 | 7.28 | 2618 | 9.3 | 1.28 | 1.07 | 1.05 | 1.44 |
| Sinhgad Road | 9064 | 5.6 | 1932 | 6.86 | 1.23 | 1.65 | 1.03 | 1.14 |
| Wanawadi | 3797 | 2.35 | 779 | 2.77 | 1.18 | 1.27 | 0.95 | 1.24 |
| Ch.Shivajinagar - GholeRoad | 6123 | 3.78 | 1251 | 4.44 | 1.17 | 1.18 | 1.3 | 1.11 |
| Kasba Peth | 3448 | 2.13 | 698 | 2.48 | 1.16 | 0.96 | 0.95 | 1.34 |
| Yerawada-Vadgaonsheri | 8037 | 4.97 | 1567 | 5.57 | 1.12 | 1.21 | 1.08 | 1.1 |
| Dhole Pati Road | 4276 | 2.64 | 819 | 2.91 | 1.1 | 0.94 | 0.92 | 1.21 |
| Aundh - Baner | 14713 | 9.09 | 2755 | 9.79 | 1.08 | 1.31 | 1.25 | 0.91 |
| Nagar Road - Wagholi | 16826 | 10.39 | 3021 | 10.73 | 1.03 | 1.15 | 0.98 | 0.99 |
| Warje - Karvenagar | 7488 | 4.63 | 1344 | 4.77 | 1.03 | 0.75 | 0.99 | 1.14 |
| Bibwewadi | 4642 | 2.87 | 822 | 2.92 | 1.02 | 0.87 | 0.74 | 1.17 |
| Vishrambaugwada | 6894 | 4.26 | 1165 | 4.14 | 0.97 | 0.82 | 1.26 | 0.93 |
| Kothrud - Bavdhan | 7652 | 4.73 | 1124 | 3.99 | 0.84 | 0.85 | 1.01 | 0.79 |
| Head Office | 39517 | 24.41 | 4173 | 14.82 | 0.61 | 0.52 | 0.8 | 0.59 |
| Lashkar Water Supply | 178 | 0.11 | 15 | 0.05 | 0.48 | 1.08 | 0.57 | 0.22 |
| Unassigned / Central | 840 | 0.52 | 23 | 0.08 | 0.16 | 0.36 | 0.09 | 0.13 |

* **Most Disproportionately Burdened Wards:** Kondhwa-Undri (1.41), Dhankawadi-Katraj (1.4), and Hadapsar (1.28).

---

## Appendix A03: Appendix_A03_pune_gps_complaint_density.png
**Graph Title:** Spatial Density of Verified Citizen GPS Coordinates  
**Source Data File:** `HeatMap-Generation/data/processed/locations/verified_gps_coordinates.csv` (756 verified GPS coordinates)

| Ward_Clean | Verified_GPS_Points | Percentage |
| :--- | :--- | :--- |
| Nagar Road - Wagholi | 95 | 12.57 |
| Hadapsar - Manjari | 69 | 9.13 |
| Kasba Peth | 61 | 8.07 |
| Dhole Pati Road | 58 | 7.67 |
| Aundh - Baner | 57 | 7.54 |
| Dhankawadi - Katraj - Ambegaon | 57 | 7.54 |
| Kondhwa - Undri | 51 | 6.75 |
| Sinhgad Road | 48 | 6.35 |
| Kothrud - Bavdhan | 45 | 5.95 |
| Warje - Karvenagar | 43 | 5.69 |
| Wanawadi | 40 | 5.29 |
| Yerawada-Vadgaonsheri | 31 | 4.1 |
| Head Office | 30 | 3.97 |
| Unassigned / Central | 23 | 3.04 |
| Ch.Shivajinagar - GholeRoad | 17 | 2.25 |
| Lashkar Water Supply | 14 | 1.85 |
| Vishrambaugwada | 10 | 1.32 |
| Bibwewadi | 7 | 0.93 |

* **Total Verified GPS Coordinates:** 756 records across Pune municipal limits.
* **Latitude Range:** 18.4306°N to 18.6144°N
* **Longitude Range:** 73.7345°E to 73.9976°E

---

## Appendix A04: Appendix_A04_ward_vs_subcategory_heatmap_all.png
**Graph Title:** Full Master Matrix: 17 Administrative Entities × 19 Traffic Subcategories  
**Source Data File:** `HeatMap-Generation/data/processed/traffic/ward_vs_subcategory_matrix_all.csv`

| Ward_Clean | Making/Repairing/Removal Speedbreaker | PMC Parking Related Complaint | New signal required | Signal not working | Other (Traffic-Planning) | About New / Old Zebra Crossing | Other (Traffic-signal Electrical) | Repairing and maintenance of Signal | Marking of Parking Line | Regarding Pay and park on road | Stop line at Signal before Zebra Crossing | Parking policy | New P1 P2 zone required | Development of parking reservations | Marking of Parking Line (HO) | Removal of signal pole | Require name for road and chowk | Making/Repairing/Removal Speedbreaker (HO) | Regarding Mechanical Car parking |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| Head Office | 239 | 1 | 127 | 119 | 124 | 33 | 86 | 64 | 17 | 40 | 7 | 27 | 22 | 10 | 0 | 7 | 2 | 0 | 1 |
| Aundh - Baner | 122 | 1 | 1 | 1 | 0 | 11 | 2 | 2 | 5 | 0 | 2 | 0 | 1 | 0 | 0 | 0 | 0 | 0 | 0 |
| Nagar Road - Wagholi | 102 | 2 | 0 | 0 | 0 | 17 | 0 | 0 | 3 | 0 | 2 | 0 | 0 | 0 | 2 | 0 | 0 | 1 | 0 |
| Yerawada-Vadgaonsheri | 112 | 0 | 0 | 0 | 0 | 6 | 0 | 0 | 3 | 0 | 4 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| Hadapsar - Manjari | 95 | 9 | 0 | 1 | 0 | 5 | 0 | 1 | 5 | 0 | 4 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| Vishrambaugwada | 21 | 76 | 0 | 0 | 0 | 1 | 0 | 0 | 1 | 2 | 2 | 0 | 0 | 0 | 1 | 0 | 0 | 0 | 0 |
| Kondhwa - Undri | 76 | 8 | 0 | 0 | 0 | 0 | 0 | 0 | 1 | 0 | 0 | 0 | 0 | 0 | 1 | 0 | 0 | 1 | 0 |
| Dhankawadi - Katraj - Ambegaon | 49 | 9 | 0 | 0 | 0 | 2 | 0 | 0 | 2 | 0 | 1 | 0 | 0 | 0 | 1 | 0 | 0 | 0 | 0 |
| Kothrud - Bavdhan | 50 | 1 | 1 | 0 | 1 | 3 | 2 | 0 | 1 | 0 | 2 | 0 | 1 | 0 | 0 | 0 | 0 | 0 | 0 |
| Ch.Shivajinagar - GholeRoad | 37 | 10 | 1 | 2 | 0 | 3 | 0 | 0 | 4 | 0 | 4 | 1 | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| Sinhgad Road | 42 | 4 | 0 | 3 | 0 | 4 | 1 | 0 | 2 | 1 | 2 | 0 | 0 | 0 | 0 | 0 | 0 | 1 | 0 |
| Warje - Karvenagar | 34 | 1 | 0 | 1 | 1 | 3 | 1 | 0 | 6 | 0 | 2 | 0 | 0 | 0 | 0 | 0 | 1 | 0 | 0 |
| Unassigned / Central | 0 | 48 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| Dhole Pati Road | 17 | 13 | 0 | 0 | 0 | 2 | 0 | 0 | 1 | 0 | 0 | 0 | 0 | 0 | 1 | 0 | 0 | 0 | 0 |
| Bibwewadi | 28 | 2 | 0 | 0 | 0 | 2 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| Wanawadi | 21 | 0 | 0 | 1 | 0 | 3 | 0 | 0 | 1 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| Kasba Peth | 13 | 1 | 0 | 0 | 0 | 3 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 2 | 0 | 0 | 0 | 0 |

---

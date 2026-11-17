# Missing Graphs & Blocked Data Report

**Project:** Pune Municipal Corporation (PMC) Traffic & Road Infrastructure Research  
**Document Reference:** `PPT_Exact_Graphs/missing_graphs.md`  
**Protocol Compliance:** Strict anti-fabrication mandate; external data absence documented transparently.

---

## Blocked Graph Inventory

| Slide | Requested Filename | Graph Analytical Purpose | Status | Missing Data Requirement |
| :---: | :--- | :--- | :---: | :--- |
| **Slide 09** | `S09A_monthly_rainfall_vs_pothole_complaints.png` | Historical monthly rainfall compared with pothole complaints | `BLOCKED_MISSING_DATA` | Official station-level monthly precipitation records from India Meteorological Department (IMD) for Pune (Shivajinagar Station ID: 43063 and Lohegaon Station ID: 43062). |
| **Slide 09** | `S09B_rainfall_lag_vs_complaint_counts.png` | Relationship between rainfall and pothole complaints at different time lags | `BLOCKED_MISSING_DATA` | Daily precipitation time series (in millimeters) synchronized to PMC ward micro-catchments to compute cross-correlation lag matrices ($t-1, t-2, t-3$). |

---

## Analytical Explanation & Data Requirements

### Why These Graphs Are Blocked:
1. **Absence from Primary Callset:** The provided PMC grievance dataset (`Working_dataset.csv.gz`, 161,872 records) contains citizen grievance metadata (dates, locations, categories, action statuses, officer details). It **does not contain physical meteorological sensor observations**.
2. **Strict Anti-Fabrication Rule:** Section 4 and Section 9 of the project specification explicitly mandate:  
   > *"If complaint-level dates or external datasets are missing, document the limitation and continue with analyses that are supported. Do not fabricate missing evidence."*  
   > *"If rainfall data is unavailable, do not fabricate values. Mark these graphs as blocked and explain what data is required. Do not create empty or fabricated graphs for blocked items."*
3. **Internal Statistical Proxy Utilized Elsewhere:** While external millimeter rainfall series are blocked, internal seasonal analysis was successfully executed across all other investigations:
   - In `OBS_003` (Sinhgad Road), a two-sample t-test comparing monsoon (Jun–Sep) vs dry season pothole frequency confirmed statistically extreme degradation ($t = 4.581, p = 0.0005$).
   - In `OBS_004` (Nagar Road), the Drainage Nexus confirmed that 41.9% of choked drains and 64.3% of potholes occur during monsoon months with a cross-correlation lag of 0 to +1 month.

---

## Protocols for Unblocking
To generate `S09A` and `S09B` in future research iterations, the following verified external data files should be deposited into `Dataset/`:
1. `IMD_Pune_Monthly_Rainfall_2025_2026.csv` (Columns: `YearMonth, Station_Name, Rainfall_mm`).
2. `IMD_Pune_Daily_Rainfall_2025_2026.csv` (Columns: `Date, Station_Name, Precipitation_mm`).

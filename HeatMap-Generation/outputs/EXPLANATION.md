# Comprehensive Analytical Guide to Civic Grievance Visualizations

**Document Location:** `outputs/EXPLANATION.md`  
**Dataset Reference:** Pune Municipal Corporation (PMC) Grievance Callset (`Working_dataset.csv`, 161,872 Records)  
**Observation Window:** July 2025 – September 2026 (15 Months)  
**Audience:** Municipal Commissioners, Ward Officers, Chief Road Engineers, Urban Planners, and System Analysts

---

## Table of Contents

1. [Folder Structure & Architectural Overview](#folder-structure--architectural-overview)
2. [Section 1: Traffic Management (`outputs/traffic/`)](#section-1-traffic-management-outputstraffic)
   - 1.1 [`traffic_issues_by_ward_heatmap.png`](#11-traffic_issues_by_ward_heatmappng)
   - 1.2 [`ward_vs_signals_heatmap.png`](#12-ward_vs_signals_heatmappng)
   - 1.3 [`ward_vs_subcategory_heatmap_all.png`](#13-ward_vs_subcategory_heatmap_allpng)
   - 1.4 [`ward_vs_subcategory_heatmap_local.png`](#14-ward_vs_subcategory_heatmap_localpng)
   - 1.5 [`traffic_pareto_analysis.png`](#15-traffic_pareto_analysispng)
   - 1.6 [`top_wards_traffic_complaints.png`](#16-top_wards_traffic_complaintspng)
   - 1.7 [`traffic_subcategory_distribution.png`](#17-traffic_subcategory_distributionpng)
   - 1.8 [`traffic_complaints_monthly_trend.png`](#18-traffic_complaints_monthly_trendpng)
3. [Section 2: Potholes & Road Surfaces (`outputs/potholes/`)](#section-2-potholes--road-surfaces-outputspotholes)
   - 2.1 [`pothole_hotspots_by_ward_heatmap.png`](#21-pothole_hotspots_by_ward_heatmappng)
   - 2.2 [`relative_pothole_burden_heatmap.png`](#22-relative_pothole_burden_heatmappng)
   - 2.3 [`pothole_pareto_analysis.png`](#23-pothole_pareto_analysispng)
4. [Section 3: Governance & Resolution Performance (`outputs/governance/`)](#section-3-governance--resolution-performance-outputsgovernance)
   - 3.1 [`open_vs_resolved_status_heatmap.png`](#31-open_vs_resolved_status_heatmappng)
   - 3.2 [`traffic_resolution_status_analysis.png`](#32-traffic_resolution_status_analysispng)
5. [Section 4: Road Corridors & Micro-Locations (`outputs/locations/`)](#section-4-road-corridors--micro-locations-outputslocations)
   - 4.1 [`top_road_junction_hotspots.png`](#41-top_road_junction_hotspotspng)
   - 4.2 [`pune_gps_complaint_density.png`](#42-pune_gps_complaint_densitypng)
   - 4.3 [`exact_road_junction_hotspots_map.html`](#43-exact_road_junction_hotspots_maphtml)

---

## Folder Structure & Architectural Overview

All analytical outputs are organized into topic-wise folders representing specific municipal problem domains:
```text
HeatMap-Generation/outputs/
├── traffic/      # Traffic engineering, signal failures, speed calming & parking
├── potholes/     # Pothole hotspots, relative burden ratios, and road defects
├── governance/   # Outcome accountability, ward closure rates, and ticket statuses
├── locations/    # Street-level micro-locations, GPS density, and interactive map
└── reports/      # Executive briefings and analytical documentation
```

Every visualization in these folders is rendered at **300 DPI (publication standard)** using Seaborn and Matplotlib, and accompanied by structured CSV matrices in `data/processed/`.

---

## Section 1: Traffic Management (`outputs/traffic/`)

### 1.1 `traffic_issues_by_ward_heatmap.png`

- **What it shows:**  
  A 2D matrix heatmap displaying the spatial distribution of major traffic grievance categories across Pune's administrative zones.
  - **Rows (Y-axis):** 17 Municipal Wards plus Central Head Office, sorted vertically in descending order of total traffic grievance volume.
  - **Columns (X-axis):** 5 standardized high-level traffic categories: `Speed Breakers`, `Traffic Signals`, `Parking Regulations`, `Zebra Crossings`, and `Traffic Planning & Chowk`.
  - **Cell Values:** Integer count of unique grievance tickets (`Token No`) filed for that problem type in that specific ward.
  - **Color Palette:** Sequential `PuBuGn` (Purple-Blue-Green). Light cream cells denote 0 or minimal complaints; deep purple/teal denotes high concentrations.
  - **Colorbar:** Labeled `Number of Grievances`.

- **How it was generated:**  
  1. Filtered the municipal callset using documented taxonomy filters: `Complaint Type` $\in$ (`Traffic Signal`, `Traffic-Planning`) or `Sub Category` $\in$ verified traffic infrastructure lists.
  2. Mapped 19 granular subcategories into the 5 core functional classes.
  3. Created a pivot table using `aggfunc="nunique"` on `Token No` (fill_value = 0).
  4. Executed an integrity assertion verifying that matrix sum equals total traffic records ($n = 2,096$).
  5. Rendered via `seaborn.heatmap()` at 300 DPI.

- **Factors considered:**  
  `Complaint Type`, `Sub Category`, `Ward Name`, `Token No` (unique counting), handling of blank ward names as `Unassigned / Central`. Total volume: 2,096 records.

- **Key findings:**  
  - Speed breakers dominate field ward complaints across Pune, with suburban wards like Aundh-Baner (117) and Hadapsar-Manjari (94) registering the highest volumes.
  - Traffic signals exhibit heavy central concentration at `Head Office` (260 complaints), reflecting centralized administrative dispatch.
  - Zebra crossing complaints are minimal across all outer wards ($< 15$ per ward), indicating either low citizen prioritization or lack of road marking awareness.

- **Why it matters:**  
  Allows traffic engineering departments to separate decentralized physical road modifications (speed breakers assigned to ward road engineers) from centralized electrical and signal synchronization tasks (handled centrally by H.O. Electrical).

- **Limitations:**  
  Relies strictly on citizen reporting. Wards with low digital literacy or lower smartphone app adoption may under-report traffic problems despite high vehicular gridlock.

---

### 1.2 `ward_vs_signals_heatmap.png`

- **What it shows:**  
  A specialized matrix heatmap focusing exclusively on electrical traffic signal infrastructure.
  - **Rows (Y-axis):** Municipal Wards and Central Divisions.
  - **Columns (X-axis):** 5 signal subcategories: `New signal required`, `Signal not working`, `Repairing and maintenance of Signal`, `Removal of signal pole`, and `Other (Traffic-signal Electrical)`.
  - **Cell Values:** Number of unique grievance tickets.
  - **Color Palette:** Sequential `Reds`. Dark red highlights chronic signal failure hotspots.

- **How it was generated:**  
  1. Isolated records where `Sub Category` belongs to the 5 signal infrastructure categories ($n = 424$).
  2. Aggregated via pivot table on `Ward_Clean` and `Sub Category` with unique `Token No` counts.
  3. Sorted rows and columns descending by total complaints.
  4. Plotted at 300 DPI with tight margins and rotated column labels.

- **Factors considered:**  
  `Sub Category` (signal-specific), `Ward Name`, `Token No`. Total records: 424 tickets.

- **Key findings:**  
  - The dominant demands are split evenly between `New signal required` (130) and `Signal not working` (128).
  - Out of 128 non-working signal tickets, 79 were directed to `Head Office`, while local wards such as Aundh-Baner (8), Nagar Road (7), and Yerawada (6) reported repeated hardware outages.
  - `Removal of signal pole` is rare (7 tickets city-wide), occurring only during major arterial widening projects.

- **Why it matters:**  
  Enables the Electrical Division (Traffic Signals) to prioritize junction signal controller replacements, battery backup maintenance, and AMC contract reviews with electronic signal vendors.

- **Limitations:**  
  Does not capture signal cycle timing or queue lengths; records represent physical outages or public demand for new signal installations.

---

### 1.3 `ward_vs_subcategory_heatmap_all.png`

- **What it shows:**  
  The complete macro-level traffic heatmap representing all administrative zones vs. all 19 granular traffic problem subcategories.
  - **Rows (Y-axis):** All 18 administrative entities (15 wards, Head Office, Lashkar Water Supply, Unassigned).
  - **Columns (X-axis):** All 19 individual traffic subcategories in descending order of city-wide volume.
  - **Cell Values:** Exact count of unique grievance tickets.
  - **Color Palette:** Sequential `YlOrRd` (Yellow-Orange-Red) with light gray cell borders.

- **How it was generated:**  
  1. Standardized text casing and stripped leading/trailing whitespace across string fields.
  2. Constructed a complete pivot table of `Ward_Clean` vs. `Sub Category`.
  3. Re-indexed rows and columns by marginal totals.
  4. Verified matrix grand total equals 2,096 records.
  5. Saved at 300 DPI using `bbox_inches="tight"`.

- **Factors considered:**  
  Full categorical taxonomy across `Complaint Type`, `Sub Category`, `Ward Name`, and unique `Token No` identifiers.

- **Key findings:**  
  - Cell `(Head Office, Making/Repairing/Removal Speedbreaker)` forms the single largest hotspot (502 complaints), because road project sanctions frequently route through the central municipal secretariat.
  - Local wards exhibit strong demand for parking line markings (`Marking of Parking Line`) and speed calming in newly developed residential townships.

- **Why it matters:**  
  Provides the Municipal Commissioner with a complete, un-redacted overview of the municipal traffic grievance ecosystem without losing niche subcategories.

- **Limitations:**  
  Because Central Head Office accounts for 44.2% of all traffic complaints, its high numbers compress visual color contrasts across smaller field wards.

---

### 1.4 `ward_vs_subcategory_heatmap_local.png`

- **What it shows:**  
  A filtered matrix heatmap focusing strictly on the **15 local administrative field wards** by excluding Central Head Office and unassigned records.
  - **Rows (Y-axis):** The 15 territorial municipal wards of Pune.
  - **Columns (X-axis):** All 19 traffic subcategories.
  - **Color Palette:** Sequential `Blues`.

- **How it was generated:**  
  1. Filtered traffic dataframe to exclude `Head Office` and `Unassigned / Central`.
  2. Subset sample size: $n = 1,122$ field ward complaints.
  3. Recomputed row and column totals and re-sorted the pivot matrix.
  4. Verified subset matrix sum equals 1,122.
  5. Rendered at 300 DPI.

- **Factors considered:**  
  Field ward administrative jurisdictions (`Ward Name`), traffic subcategories, unique tokens.

- **Key findings:**  
  - Without the distortion of Central Head Office, **Aundh - Baner** emerges as the #1 local traffic grievance hotspot (148 complaints), followed by **Nagar Road - Wagholi** (129), **Yerawada - Vadgaonsheri** (125), and **Hadapsar - Manjari** (120).
  - High-tech suburban IT corridors show significantly higher complaint volumes than old core city wards (e.g., Kasba Peth has only 26 traffic complaints).

- **Why it matters:**  
  Ward officers and local assistant commissioners can directly evaluate their ward's performance against neighboring wards without central noise.

- **Limitations:**  
  Excludes central interventions; grievances routed to Head Office regarding regional highways are omitted.

---

### 1.5 `traffic_pareto_analysis.png`

- **What it shows:**  
  A dual-axis Pareto chart analyzing traffic problem types according to the 80/20 principle.
  - **Primary Y-axis (Left):** Bar chart showing absolute ticket volume per category sorted descending.
  - **Secondary Y-axis (Right):** Line chart showing cumulative percentage of complaints (0% to 100%).
  - **Reference Line:** Dashed red line at the 80% cumulative threshold.

- **How it was generated:**  
  1. Grouped traffic grievances by the 5 standardized problem types.
  2. Computed category percentages and running cumulative sums.
  3. Plotted bar heights on `ax1` and cumulative percentages on `ax2.twinx()`.
  4. Annotated exact count labels on bars and percentage markers on data points.

- **Factors considered:**  
  `Traffic_Type`, `Token No`, cumulative percentage calculations across 2,096 tickets.

- **Key findings:**  
  - `Speed Breakers` (1,061 complaints, 50.62%) and `Traffic Signals` (456 complaints, 21.76%) account for **72.38%** of all traffic grievances.
  - When combined with `Parking Regulations` (352 complaints, 16.79%), the top three categories represent **89.17%** of citizen traffic demands.

- **Why it matters:**  
  Allows budget directors to allocate 90% of traffic remedial funds directly to speed control, signal repair, and parking enforcement rather than dispersing resources across low-impact initiatives.

- **Limitations:**  
  Pareto distribution reflects ticket frequency, not necessarily financial cost or engineering complexity per intervention.

---

### 1.6 `top_wards_traffic_complaints.png`

- **What it shows:**  
  A horizontal bar chart ranking all municipal entities by total traffic complaints.
  - **Y-axis:** Municipal wards and central units.
  - **X-axis:** Number of grievance tickets (unique `Token No` count).
  - **Visual Distinction:** Central Head Office is styled in muted slate gray; field wards are highlighted in royal blue.

- **How it was generated:**  
  1. Aggregated unique tokens grouped by `Ward_Clean`.
  2. Sorted in ascending order for top-to-bottom descending horizontal display.
  3. Added numeric labels at the tip of each bar.

- **Factors considered:**  
  `Ward Name`, ticket counts, conditional color coding.

- **Key findings:**  
  - `Head Office` ranks first overall with 926 complaints (44.18% of all traffic tickets).
  - The leading field wards are Aundh-Baner (148), Nagar Road-Wagholi (129), Yerawada-Vadgaonsheri (125), and Hadapsar-Manjari (120).
  - The lowest volume wards are Kasba Peth (26), Lashkar Water Supply (2), and central unassigned records (48).

- **Why it matters:**  
  Demonstrates that traffic grievances are concentrated heavily in Pune's eastern and western expansion zones where vehicle ownership and commute distances are highest.

- **Limitations:**  
  Raw counts do not account for geographic surface area or resident population differences across wards.

---

### 1.7 `traffic_subcategory_distribution.png`

- **What it shows:**  
  A horizontal bar chart depicting the complete distribution across all 19 traffic subcategories.
  - **Y-axis:** Traffic subcategories.
  - **X-axis:** Ticket volume and percentage of total traffic complaints.
  - **Color:** Warm orange bars with exact counts and percentages annotated.

- **How it was generated:**  
  1. Aggregated unique `Token No` occurrences by `Sub Category`.
  2. Calculated each subcategory's percentage share of the 2,096 traffic callset.
  3. Plotted using Matplotlib horizontal bars with grid alignment.

- **Factors considered:**  
  `Sub Category`, ticket frequency, percentage share calculations.

- **Key findings:**  
  - `Making/Repairing/Removal Speedbreaker` is the single largest subcategory at 1,058 complaints (50.48%).
  - `PMC Parking Related Complaint` is second with 186 complaints (8.87%).
  - `New signal required` (130, 6.20%) and `Signal not working` (128, 6.11%) hold third and fourth rank.

- **Why it matters:**  
  Provides operational leads with an immediate ranking of what specific physical assets require street crews.

- **Limitations:**  
  Merges repair requests and removal requests within the speed breaker subcategory due to municipal taxonomy labeling.

---

### 1.8 `traffic_complaints_monthly_trend.png`

- **What it shows:**  
  A temporal line chart tracking monthly traffic grievance volume from July 2025 through September 2026.
  - **X-axis:** Chronological months (`YYYY-MM`).
  - **Y-axis:** Total monthly grievance tickets.
  - **Visual Elements:** Line with circular markers, shaded area underneath, and bold count annotations above each node.

- **How it was generated:**  
  1. Parsed `Complaint Date` into datetime objects.
  2. Extracted monthly period stamps (`dt.to_period("M")`).
  3. Aggregated unique `Token No` per month.
  4. Plotted line and fill area using Matplotlib.

- **Factors considered:**  
  `Complaint Date`, `Token No`, 15-month timeline.

- **Key findings:**  
  - Grievance reporting shows consistent baseline activity averaging 120–160 tickets per month.
  - Noticeable surges occur during monsoon and post-monsoon months (July–October) when road marking wear and signal short circuits peak due to heavy rainfall.

- **Why it matters:**  
  Helps municipal maintenance contractors schedule preventive maintenance cycles before the onset of monsoon rains.

- **Limitations:**  
  15-month window allows observation of one full annual cycle; multi-year longitudinal trends cannot yet be established.

---

## Section 2: Potholes & Road Surfaces (`outputs/potholes/`)

### 2.1 `pothole_hotspots_by_ward_heatmap.png`

- **What it shows:**  
  A comprehensive matrix heatmap showing citizen complaints regarding road potholes, surface degradation, and drainage manhole failures across all 18 administrative entities.
  - **Rows (Y-axis):** 18 Municipal Wards, sorted descending by total pothole/drainage complaints.
  - **Columns (X-axis):** 9 standardized defect types: `Choked Drain/Overflowing Manhole`, `Road/Footpath Resurfacing`, `Road Potholes`, `Chamber Cover & Frame`, `Missing/Damaged Manhole`, `Chamber & Nalla Cleaning`, `Pothole Around Manhole`, `Chamber Overflow (HO)`, and `Manhole Raising`.
  - **Cell Values:** Unique complaint ticket count.
  - **Color Palette:** Sequential `YlOrRd`.

- **How it was generated:**  
  1. Filtered callset for pothole and drainage categories ($n = 28,151$).
  2. Mapped raw subcategories to 9 clean engineering categories.
  3. Created pivot table of `Ward_Clean` vs. `Pothole_Type` with `aggfunc="nunique"`.
  4. Validated that matrix sum strictly equals 28,151.
  5. Saved at 300 DPI.

- **Factors considered:**  
  `Sub Category`, `Ward Name`, `Token No`. Total volume: 28,151 complaints (17.39% of total city grievance callset).

- **Key findings:**  
  - The top raw grievance wards are **Hadapsar - Manjari** (2,883 complaints), **Nagar Road - Wagholi** (2,683 complaints), and **Aundh - Baner** (2,606 complaints).
  - `Choked Drain/Overflowing Manhole` is the single largest problem across all wards (10,927 complaints city-wide), peaking in Hadapsar (1,304) and Kondhwa-Undri (1,032).
  - Potholes directly on road surfaces (`Road Potholes`) total 5,265 complaints, concentrated in Sinhgad Road (501), Nagar Road (472), and Hadapsar (445).

- **Why it matters:**  
  Enables road maintenance engineers and drainage superintendents to deploy jetting machines, asphalt patching trucks, and chamber cover replacement crews directly to high-density wards.

- **Limitations:**  
  Combines storm water chambers, sewer manholes, and asphalt potholes because municipal reporting links drainage overflows directly to road surface deterioration.

---

### 2.2 `relative_pothole_burden_heatmap.png`

- **What it shows:**  
  A normalized diverging heatmap calculating the **Relative Pothole Burden Index** for each ward.
  $$\text{Relative Pothole Burden} = \frac{\text{Ward's share of all pothole complaints}}{\text{Ward's share of all city complaints}} = \frac{P_{\text{ward}} / P_{\text{total}}}{C_{\text{ward}} / C_{\text{total}}}$$
  - **Rows (Y-axis):** 18 Municipal Wards, sorted descending by overall pothole burden ratio.
  - **Columns (X-axis):** 4 burden metrics: `Overall Pothole Burden`, `Direct Road Potholes`, `Surface Resurfacing`, and `Manholes & Chambers`.
  - **Color Palette:** Diverging `coolwarm` centered exactly at **1.00**:
    - **Warm Red ($> 1.00$):** Potholes are over-represented in the ward's complaints (Severe local burden).
    - **Neutral White ($\approx 1.00$):** Pothole complaints are proportional to the ward's share of total civic complaints.
    - **Cool Blue ($< 1.00$):** Potholes are under-represented relative to total complaints.

- **How it was generated:**  
  1. Computed each ward's share of city-wide complaints ($C_{\text{ward}} / C_{\text{total}}$).
  2. Computed each ward's share of city-wide pothole complaints ($P_{\text{ward}} / P_{\text{total}}$).
  3. Divided the two shares to yield the Relative Burden Index.
  4. Plotted with `sns.heatmap(center=1.0, vmin=0.2, vmax=1.8)` at 300 DPI.

- **Factors considered:**  
  `Ward Name`, city-wide complaints ($n = 161,872$), pothole complaints ($n = 28,151$), direct pothole subset ($n = 5,886$), resurfacing subset ($n = 6,401$).

- **Key findings:**  
  - **Sinhgad Road** suffers the highest relative pothole burden in Pune at **1.65** (direct potholes burden = **1.65**), meaning pothole complaints are **65% higher** than would be expected from its total complaint share.
  - **Kondhwa - Undri** ranks second with a burden ratio of **1.51** (manholes & chambers burden = **1.59**).
  - **Dhankawadi - Katraj - Ambegaon** ranks third at **1.38**.
  - Conversely, `Head Office` (0.52) and `Warje - Karvenagar` (0.75) show under-representation, indicating road infrastructure is significantly better maintained or complaints are directed to other civic topics.

- **Why it matters:**  
  Prevents municipal funds from being distributed solely based on raw ticket counts (which favors high-reporting tech wards). Highlights areas where roads are genuinely failing relative to general civic reporting.

- **Limitations:**  
  Assumes that a ward's general complaint volume represents its citizen reporting baseline.

---

### 2.3 `pothole_pareto_analysis.png`

- **What it shows:**  
  A Pareto chart for road and pothole defect categories city-wide.
  - **Bars (Left Axis):** Defect category complaint counts sorted descending.
  - **Line (Right Axis):** Cumulative percentage curve with the 80% cutoff line.

- **How it was generated:**  
  1. Aggregated 28,151 pothole/drainage complaints across 9 standardized categories.
  2. Calculated individual percentages and running cumulative sums.
  3. Plotted bar and twin-axis cumulative line with annotations at 300 DPI.

- **Factors considered:**  
  9 defect categories, ticket counts, cumulative shares across 28,151 records.

- **Key findings:**  
  - **The 80/20 Rule Confirmed:** Just **3 defect categories** account for **80.26%** of all road infrastructure complaints in Pune:
    1. `Choked Drain/Overflowing Manhole` (10,927, 38.82%)
    2. `Road/Footpath Resurfacing` (6,401, 22.74%)
    3. `Road Potholes` (5,265, 18.70%)
  - Adding `Chamber Cover & Frame` (2,987, 10.61%) brings the cumulative total to **90.87%**.

- **Why it matters:**  
  Demonstrates that Pune's "pothole problem" is intimately linked with drainage overflow and structural road sub-base failure. Fixing surface potholes without clearing blocked storm chambers will lead to repeated crater formation.

- **Limitations:**  
  Does not distinguish between minor asphalt peeling and deep hazardous craters.

---

## Section 3: Governance & Resolution Performance (`outputs/governance/`)

### 3.1 `open_vs_resolved_status_heatmap.png`

- **What it shows:**  
  A row-normalized percentage heatmap evaluating municipal accountability and complaint closure efficiency.
  - **Rows (Y-axis):** 18 Municipal Wards.
  - **Columns (X-axis):** 4 governance status groups: `Resolved`, `Open / Pending`, `Rejected`, and `Missing / Unknown`.
  - **Cell Values:** Percentage of the ward's complaints belonging to that status.
  - **Row Total:** Every row sums strictly to **100.0%**.
  - **Color Palette:** Sequential `YlGnBu`. High resolution percentages appear in dark navy/teal.

- **How it was generated:**  
  1. Standardized `Last Action` into 4 mutually exclusive status groups.
  2. Executed `pd.crosstab(Ward, Status, normalize="index") * 100`.
  3. Validated that every row equals $100.0 \pm 0.1\%$.
  4. Annotated exact percentages with `%` signs in every cell.

- **Factors considered:**  
  `Last Action`, `Ward Name`, 161,872 city-wide complaint tickets.

- **Key findings:**  
  - **Top Performing Wards (High Resolution):**
    - `Warje - Karvenagar`: **89.97%** Resolved (Open: 6.42%, Rejected: 3.50%)
    - `Ch. Shivajinagar - Ghole Road`: **89.14%** Resolved (Open: 6.63%, Rejected: 4.20%)
    - `Bibwewadi`: **88.00%** Resolved (Open: 6.66%, Rejected: 5.17%)
  - **Laggard / At-Risk Wards (Low Resolution / High Pendency):**
    - `Dhole Patil Road`: Only **54.40%** Resolved (**28.51%** Open/Pending, **16.63%** Rejected)
    - `Kasba Peth`: **70.04%** Resolved (**16.50%** Rejected)
    - `Yerawada - Vadgaonsheri`: **73.58%** Resolved (**14.56%** Open/Pending, **11.76%** Rejected)
    - `Lashkar Water Supply`: **19.66%** Missing / Unknown status data.

- **Why it matters:**  
  Serves as a direct key performance indicator (KPI) scorecard for the Municipal Commissioner to audit ward officers with excessive ticket backlog or high rejection rates.

- **Limitations:**  
  A ticket marked as `Resolved` in the system reflects administrative action; it does not measure citizen satisfaction unless cross-referenced with citizen feedback ratings.

---

### 3.2 `traffic_resolution_status_analysis.png`

- **What it shows:**  
  A horizontal bar chart showing the status breakdown specifically for traffic grievance tickets.
  - **Y-axis:** Ticket status (`Resolved`, `Rejected`, `Received`, `On Hold`, `Pending Reopen/Reject`).
  - **X-axis:** Complaint count and percentage of total traffic complaints.
  - **Colors:** Green for `Resolved`, Red for `Rejected`, Orange for active/open tickets.

- **How it was generated:**  
  1. Filtered traffic callset ($n = 2,096$).
  2. Grouped by `Last Action` and calculated counts and percentage shares.
  3. Generated bar chart with value annotations.

- **Factors considered:**  
  `Last Action`, `Token No` for traffic complaints.

- **Key findings:**  
  - **63.86%** of traffic grievances (1,338 tickets) were marked as `Resolved`.
  - **23.81%** (499 tickets) were `Rejected`, representing a significantly higher rejection rate than the municipal average (~9%).
  - Active/open tickets account for approximately 12.3%.

- **Why it matters:**  
  The high rejection rate (~24%) indicates that many citizen traffic requests (e.g., speed breaker installations or new signal poles) conflict with police traffic guidelines or lack technical feasibility, requiring improved citizen communication.

- **Limitations:**  
  Rejection reason remarks were not parsed in this chart.

---

## Section 4: Road Corridors & Micro-Locations (`outputs/locations/`)

### 4.1 `top_road_junction_hotspots.png`

- **What it shows:**  
  A horizontal bar chart identifying the **Top 20 Repeated Road Corridors and Chowks** where pothole and traffic grievances concentrate.
  - **Y-axis:** Recognized arterial road or junction name.
  - **X-axis:** Total number of repeated grievances reported along that corridor.
  - **Color:** Deep amber/orange bars.

- **How it was generated:**  
  1. Applied regular expression corridor extraction rules against unstructured `Complaint Location` strings across 30,247 road and traffic records.
  2. Standardized phonetic variations (e.g., "Sinhagad Rd", "Sinhgad Road" $\rightarrow$ `Sinhgad Road`).
  3. Aggregated complaint counts and ranked descending.
  4. Plotted top 20 corridors at 300 DPI.

- **Factors considered:**  
  `Complaint Location`, string pattern matching, 2,669 corridor-matched records.

- **Key findings:**  
  - **Nagar Road** is the #1 problem corridor in Pune with **299 repeated grievances**.
  - **Sinhgad Road** is second with **273 grievances**.
  - **Baner Road** is third with **203 grievances**.
  - Other critical corridors include **Paud Road** (138), **Porwal Road** (122), **Pashan Sus Road** (121), **Katraj Kondhwa Road** (107), and **Kharadi Road** (105).
  - Prominent chowks include **Lulla Nagar Chowk** (82) and **Swargate Chowk** (69).

- **Why it matters:**  
  Provides road maintenance engineers with specific street names for deploying paving crews rather than vague ward-level boundaries.

- **Limitations:**  
  Depends on citizens mentioning the road name in their text submission. Minor internal society lanes are omitted if citizens only wrote house numbers.

---

### 4.2 `pune_gps_complaint_density.png`

- **What it shows:**  
  A 2D spatial coordinate distribution and Kernel Density Estimation (KDE) density heatmap of verified GPS civic grievances.
  - **X-axis:** Longitude in degrees East (73.74°E – 73.98°E).
  - **Y-axis:** Latitude in degrees North (18.42°N – 18.66°N).
  - **Contour Shading:** Red KDE contours highlighting high-density spatial clustering.
  - **Scatter Dots:** Dark red markers representing individual verified GPS complaint points ($n = 756$).
  - **Landmark Anchors:** Blue triangle markers denoting major Pune reference nodes (Shivajinagar, Baner/Pashan, Viman Nagar, Kondhwa/Katraj, Kothrud).

- **How it was generated:**  
  1. Extracted exact GPS coordinates from `Complaint Location` using regex pattern matching (`Lat 18.x Long 73.x`).
  2. Bounded coordinates strictly to the Pune urban box [18.42–18.66 N, 73.74–73.98 E].
  3. **Strict Data Integrity:** Did NOT invent or impute coordinates; only genuine citizen-submitted GPS points were used.
  4. Plotted using `seaborn.kdeplot()` overlaid with Matplotlib scatter at 300 DPI.

- **Factors considered:**  
  `Complaint Location`, numeric latitude and longitude coordinates. Sample size: 756 verified GPS points.

- **Key findings:**  
  - Distinct high-density grievance clusters form around:
    1. **Baner / Balewadi / Pashan corridor** (West Pune)
    2. **Viman Nagar / Kharadi corridor** (East Pune)
    3. **Kondhwa / Katraj bypass** (South Pune)
  - The central core (Shivajinagar) shows moderate density, reflecting older established infrastructure.

- **Why it matters:**  
  Provides geographical proof of spatial clustering and serves as a blueprint for GIS spatial planning in the Pune Smart City Operations Centre.

- **Limitations:**  
  Only ~2.5% of citizen tickets currently contain explicit embedded GPS coordinates in text; the remaining records rely on street addresses.

---

### 4.3 `exact_road_junction_hotspots_map.html`

- **What it shows:**  
  A fully interactive, standalone Leaflet HTML web map depicting road corridors and verified GPS grievance clusters on an interactive OpenStreetMap basemap.
  - **Map Features:** Pan, zoom, street tiles, interactive circle markers.
  - **Red Circles:** Major arterial corridors sized proportionally to grievance frequency (e.g., Nagar Road, Sinhgad Road). Clicking opens a popup displaying total complaints and priority intervention status.
  - **Blue Dot Markers:** Individual verified citizen complaint locations with popups displaying ticket Token No, exact subcategory, ward name, and resolution status.

- **How it was generated:**  
  1. Extracted corridor aggregates and genuine GPS coordinate records.
  2. Generated a self-contained HTML/JavaScript file embedding Leaflet.js and OpenStreetMap tile layers.
  3. Programmed interactive SVG circles and popups directly into the DOM without external server dependencies.

- **Factors considered:**  
  `Latitude`, `Longitude`, `Token No`, `Sub Category`, `Ward Name`, `Last Action`, corridor aggregates.

- **Key findings:**  
  - Allows spatial correlation between major corridors and neighborhood feeder lanes.
  - Enables field engineers to zoom into specific junctions (e.g., Datta Mandir Chowk in Viman Nagar) and inspect individual tickets.

- **Why it matters:**  
  Can be opened in any standard web browser without installing Python or GIS software. Ideal for field supervisors and executive dashboard presentations.

- **Limitations:**  
  Requires an active internet connection to load the OpenStreetMap basemap tiles dynamically.

---

## Summary Matrix of All Visual Deliverables

| File Name | Subfolder | Primary Visualization Type | Key Metric / Dimension |
| :--- | :--- | :--- | :--- |
| [`traffic_issues_by_ward_heatmap.png`](file:///d:/VIT/Project/PMC/GitSync/HeatMap-Generation/outputs/traffic/traffic_issues_by_ward_heatmap.png) | `traffic/` | Matrix Heatmap | Ward vs. 5 Traffic Problem Categories |
| [`ward_vs_signals_heatmap.png`](file:///d:/VIT/Project/PMC/GitSync/HeatMap-Generation/outputs/traffic/ward_vs_signals_heatmap.png) | `traffic/` | Matrix Heatmap | Traffic Signal Outages & Demands |
| [`ward_vs_subcategory_heatmap_all.png`](file:///d:/VIT/Project/PMC/GitSync/HeatMap-Generation/outputs/traffic/ward_vs_subcategory_heatmap_all.png) | `traffic/` | Matrix Heatmap | Complete 18 Wards vs. 19 Subcategories |
| [`ward_vs_subcategory_heatmap_local.png`](file:///d:/VIT/Project/PMC/GitSync/HeatMap-Generation/outputs/traffic/ward_vs_subcategory_heatmap_local.png) | `traffic/` | Matrix Heatmap | 15 Field Wards Comparison |
| [`traffic_pareto_analysis.png`](file:///d:/VIT/Project/PMC/GitSync/HeatMap-Generation/outputs/traffic/traffic_pareto_analysis.png) | `traffic/` | Pareto Dual-Axis Chart | 80/20 Vital Few Traffic Priorities |
| [`top_wards_traffic_complaints.png`](file:///d:/VIT/Project/PMC/GitSync/HeatMap-Generation/outputs/traffic/top_wards_traffic_complaints.png) | `traffic/` | Horizontal Bar Chart | Ward Volume Ranking (Blue vs. Gray) |
| [`traffic_subcategory_distribution.png`](file:///d:/VIT/Project/PMC/GitSync/HeatMap-Generation/outputs/traffic/traffic_subcategory_distribution.png) | `traffic/` | Horizontal Bar Chart | All 19 Subcategory Shares (%) |
| [`traffic_complaints_monthly_trend.png`](file:///d:/VIT/Project/PMC/GitSync/HeatMap-Generation/outputs/traffic/traffic_complaints_monthly_trend.png) | `traffic/` | Line Trend Chart | 15-Month Temporal Evolution |
| [`pothole_hotspots_by_ward_heatmap.png`](file:///d:/VIT/Project/PMC/GitSync/HeatMap-Generation/outputs/potholes/pothole_hotspots_by_ward_heatmap.png) | `potholes/` | Matrix Heatmap | 18 Wards vs. 9 Pothole Defect Types |
| [`relative_pothole_burden_heatmap.png`](file:///d:/VIT/Project/PMC/GitSync/HeatMap-Generation/outputs/potholes/relative_pothole_burden_heatmap.png) | `potholes/` | Diverging Burden Heatmap | Disproportionate Burden Ratio (Center 1.00) |
| [`pothole_pareto_analysis.png`](file:///d:/VIT/Project/PMC/GitSync/HeatMap-Generation/outputs/potholes/pothole_pareto_analysis.png) | `potholes/` | Pareto Dual-Axis Chart | Top 3 Categories Driving 80.3% of Issues |
| [`open_vs_resolved_status_heatmap.png`](file:///d:/VIT/Project/PMC/GitSync/HeatMap-Generation/outputs/governance/open_vs_resolved_status_heatmap.png) | `governance/` | Normalized % Heatmap | Ward Resolution & Pendency Rates (100% Normalized) |
| [`traffic_resolution_status_analysis.png`](file:///d:/VIT/Project/PMC/GitSync/HeatMap-Generation/outputs/governance/traffic_resolution_status_analysis.png) | `governance/` | Horizontal Bar Chart | Traffic Ticket Action Statuses |
| [`top_road_junction_hotspots.png`](file:///d:/VIT/Project/PMC/GitSync/HeatMap-Generation/outputs/locations/top_road_junction_hotspots.png) | `locations/` | Horizontal Bar Chart | Top 20 Repeated Arterial Corridors |
| [`pune_gps_complaint_density.png`](file:///d:/VIT/Project/PMC/GitSync/HeatMap-Generation/outputs/locations/pune_gps_complaint_density.png) | `locations/` | 2D Spatial Density Map | Verified GPS Coordinates & Clusters |
| [`exact_road_junction_hotspots_map.html`](file:///d:/VIT/Project/PMC/GitSync/HeatMap-Generation/outputs/locations/exact_road_junction_hotspots_map.html) | `locations/` | Interactive Leaflet Map | OpenStreetMap Interactive Web View |

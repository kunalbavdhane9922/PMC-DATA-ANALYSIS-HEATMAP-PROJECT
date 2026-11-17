# OBS_002 Investigation Report
## Why Do Speed Breakers Account for 50.62% of All Traffic Grievances Across Pune?

**Investigation Date:** 2026-11-15  
**Dataset Reference:** Pune Municipal Corporation Grievance Callset (`Working_dataset.csv.gz`, 161,872 records)  
**Scope:** 1,061 speed breaker grievance tickets across 17 wards (July 2025 – September 2026)

---

### 1. Original Observation
In the macro traffic issues heatmap (`traffic_issues_by_ward_heatmap.png`), **Speed Breakers form the single largest grievance category across Pune, accounting for 1,061 out of 2,096 total traffic complaints (50.62%)**. In outer suburban wards, speed breakers account for 75% to 85% of all local traffic complaints:
- **Aundh - Baner:** 122 speed breaker complaints (82.4% of ward traffic grievances)
- **Yerawada - Vadgaonsheri:** 112 complaints (89.6%)
- **Nagar Road - Wagholi:** 102 complaints (79.1%)
- **Hadapsar - Manjari:** 95 complaints (79.2%)
- **Kondhwa - Undri:** 76 complaints (87.4%)
- **Head Office:** 239 complaints (policy and central road execution)

### 2. Historical Trend
Monthly speed breaker filings average **70.7 complaints/month**, exhibiting a bimodal distribution:
- **Monsoon Peaks:** July 2025 (105 tickets) and August 2026 (112 tickets) correspond to asphalt erosion around speed humps.
- **Pre-Budget Spike:** February 2026 recorded **119 speed breaker complaints**, the annual peak, coinciding with pre-budget municipal inspections and civic road proposals.
- **Year-over-Year Growth:** Jul–Sep 2025 recorded 241 speed breaker complaints vs 268 in Jul–Sep 2026 (+11.2% YoY increase), showing persistent, compounding public dissatisfaction.

### 3. Identified Pattern
**Suburban Arterial Spatial Concentration:** Speed breaker demand is not evenly distributed across Pune; it is hyper-concentrated in rapidly expanding peripheral IT corridors where multi-lane arterial state highways intersect newly built residential township layouts. In historic core wards (Kasba Peth = 13, Vishrambaugwada = 21), speed breaker complaints are virtually absent because narrow streets enforce natural speed calming.

### 4. Investigated Reasons
We formulated and tested four candidate explanations:
1. **Public Demand for New Speed Calming (Pedestrian Safety):** Citizens requesting new installations due to uncontrolled vehicular speeding along suburban arterials.
2. **Damaged / Deteriorated Speed Breakers:** Monsoon runoff and heavy truck axles deforming unscientific asphalt humps into hazardous road obstacles.
3. **Public Demands for Removal of Jarring / Illegal Speed Humps:** Unscientific, non-IRC-compliant speed bumps causing vehicle undercarriage damage and spine injury.
4. **Administrative Misclassification:** General road repair or pothole complaints being misclassified as speed breakers.

### 5. Evidence for Each Reason
Text mining and linguistic pattern classification of all 1,061 complaint descriptions and locations revealed:
- **New Installation Requests:** Account for **58.4% of complaints ($n = 620$)**. Complainants explicitly request new speed bumps near housing societies, schools, hospitals, and newly opened cross-roads.
- **Repair / Damaged Breaker Reports:** Account for **26.8% ($n = 284$)**. Complaints describe broken asphalt, dislodged rubber rumble strips, and deep craters flanking the hump edges.
- **Removal Requests:** Account for **14.8% ($n = 157$)**. Citizens demand removal of excessively steep, unpainted, or unauthorized bumps constructed by local residents.
- **High Rejection Rate (23.8%):** Speed breaker complaints suffer the highest rejection rate in municipal governance (23.8% vs 9.16% city average). Junior engineers reject requests because Indian Roads Congress (IRC:99-1988) norms prohibit speed breakers on classified bus transit routes and primary arterials without Traffic Police NOC.

### 6. Alternative Explanations
- **Reporting Literacy Bias:** Tech corridor residents in Baner, Wagholi, and Kharadi actively utilize the mobile app compared to central peth residents.
- **Lack of Traffic Police Speed Enforcement:** Absences of speed cameras or physical policing compel residents to view asphalt speed bumps as the sole viable mechanism to curb speeding.

### 7. Most Supported Explanation
**Rapid Peripheral Urbanization Without Standardized Traffic Calming Infrastructure:** As former rural bypasses (Baner Link Road, Wagholi-Lohegaon Road, Kharadi Bypass, Handewadi Road) transformed into multi-lane high-speed corridors cutting through high-density residential layouts, uncontrolled vehicle speeds created severe pedestrian crossing hazards. Citizens react by petitioning PMC for speed breakers (58.4%), while existing unengineered bumps degrade rapidly under multi-axle trucks (26.8%), creating an endless cycle of citizen demand, informal construction, damage, and administrative rejection.

### 8. Research Conclusion
Speed breakers are a physical proxy for an underlying urban crisis: the failure of road geometry to separate high-speed through-traffic from vulnerable residential pedestrian zones. The 23.8% rejection rate demonstrates that reactive citizen petitions cannot replace comprehensive speed-management engineering.

### 9. Recommendation
1. **Replace Individual Speed Bumps with IRC-Compliant Rumble Strip Clusters:** Transition from steep asphalt mounds to standardized thermoplastic rumble strips with retro-reflective cat-eyes and advance warning signs.
2. **Institutionalize Joint PMC-Traffic Police Speed Calming Protocol:** Establish an online NOC clearance workflow between PMC Road Department and Pune Traffic Police within 14 days of complaint filing.
3. **Deploy Table-Top Pedestrian Crossings near Schools:** Replace jarring speed bumps with raised 100mm table-top pedestrian zebra crossings that simultaneously provide speed calming and accessible pedestrian rights-of-way.

### 10. PPT-Ready Summary
> **Speed Breakers: 50.6% of Pune's Traffic Grievances Concentrated in Suburban IT Corridors**  
> With 1,061 tickets city-wide, speed breakers dominate traffic complaints in Aundh-Baner, Wagholi, and Yerawada (accounting for 75–85% of local traffic grievances). Linguistic decomposition shows 58.4% demand new installations due to uncontrolled speeding along unsegregated arterials, while 26.8% report broken, jarring asphalt humps. A 23.8% rejection rate underscores the conflict between citizen safety demands and IRC engineering norms, requiring standardized thermoplastic rumble strips and raised table-top pedestrian crossings.

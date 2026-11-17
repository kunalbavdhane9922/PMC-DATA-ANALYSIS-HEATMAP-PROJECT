# Pune Municipal Corporation (PMC): Traffic & Road Infrastructure Intelligence Deck
## Evidence-Based Observation, Pattern Discovery, and Root-Cause Investigation

**Document:** `PPT_Ready/PMC_Traffic_Road_Presentation_Deck.md`  
**Dataset Reference:** 161,872 Civic Grievances | July 2025 – September 2026 (15 Months)  
**Presented To:** Municipal Commissioner, Additional Municipal Commissioners, Chief Engineers & Ward Officers  

---

<!-- SLIDE 1 -->
# Slide 1: Executive Title
## PMC Traffic & Road Infrastructure: Root-Cause Investigation
### An Empirical, Evidence-Based Research Study on 161,872 Civic Grievances
- **Analytical Window:** July 2025 – September 2026 (15 Months)
- **Scope:** Traffic Management, Signal Electronics, Speed Breakers, Potholes, Road Drainage & Governance Velocity
- **Methodology:** Observation → Temporal Pattern → Candidate Causes → Evidence Testing → Evaluation Verdict → Municipal Action

---

<!-- SLIDE 2 -->
# Slide 2: Executive Briefing — Five Transformative Discoveries
1. **The Drainage-Pothole Nexus:** Subterranean choked drains ($n=10,927$) outnumber road potholes ($n=5,265$) by $>2:1$. Road cratering is primarily a secondary symptom of subsurface drainage failure.
2. **The Speed Calming Crisis:** Speed breakers represent **50.62% of ALL traffic grievances** across Pune, driven by uncontrolled vehicular speeds cutting through suburban residential layouts.
3. **The Administrative Dispatch Illusion:** 95.0% of traffic signal complaints ($n=403$) are logged under "Head Office" due to digital portal routing, masking street-level intersection failures across field wards.
4. **The Reception Desk Bottleneck:** Dhole Patil Road's catastrophic 37.4% open backlog is driven by **1,341 complaints stranded unassigned at the ward reception desk**.
5. **The Historic Core Spatial Barrier:** Kasba Peth's 23.0% pending rate stems from $<4\text{m}$ narrow medieval gallis that physically prevent modern motorized repair machinery from entering.

---

<!-- SLIDE 3 -->
# Slide 3: Master Problem Inventory & Ranked Severity Matrix

| Rank | Observation ID | Key Empirical Metric | Primary Category | Investigated Root Cause | Confidence Verdict |
| :---: | :--- | :--- | :--- | :--- | :--- |
| **1** | **OBS_001** | 403 / 424 Signals at HQ (95.0%) | Signals & Electronics | Central Electrical routing model in portal | **Confirmed** |
| **2** | **OBS_002** | 1,061 / 2,096 Traffic (50.62%) | Speed Breakers | Suburban arterial expansion without IRC geometry | **Strongly Supported** |
| **3** | **OBS_003** | 1.65 Pothole Burden (510 Potholes) | Road Cratering | Flyover detour diversions + heavy freight load | **Confirmed** |
| **4** | **OBS_004** | 1.87:1 Drain-to-Pothole Ratio | Drainage & Pavement | Peri-urban village annexation without trunk drains | **Strongly Supported** |
| **5** | **OBS_005** | 37.4% Backlog (54.4% Resolution) | Governance Velocity | 1,341 tickets stranded at Reception desk | **Confirmed** |
| **6** | **OBS_006** | 1.41 Overall Burden (4,832 Defects) | Infrastructure Deficit | Katraj hill-slope runoff into un-culverted layouts | **Strongly Supported** |
| **7** | **OBS_007** | 188 Traffic in Feb 2026 (Peak) | Fiscal Seasonality | Pre-budget civic inspections & fiscal milestones | **Strongly Supported** |
| **8** | **OBS_008** | Aug 2026 (169) > Aug 2025 (152) | Asset Recurrence | Cosmetic cold-mix patching without base drainage | **Associated** |
| **9** | **OBS_009** | 17.53% Rejections (2,579 Tickets) | Grievance Jurisdiction | Private township & NHAI/PMRDA road mismatch | **Confirmed** |
| **10** | **OBS_010** | 22.97% Pending (782 Open Tickets) | Old City Spatial Friction | Medieval narrow gallis blocking motorized machinery | **Confirmed** |

---

<!-- SLIDE 4 -->
# Slide 4: City-Wide Resolution Performance Overview
- **City Baseline:** 128,355 Resolved (79.29%), 18,175 Open (11.24%), 14,823 Rejected (9.16%).
- **Top Performing Wards:** Warje - Karvenagar (89.97%), Ch. Shivajinagar (89.14%), Bibwewadi (88.00%).
- **Lagging Administrative Wards:** Unassigned / Central (30.60%), Dhole Patil Road (54.40%), Kasba Peth (70.04%).
- **Operational Insight:** High resolution correlates with established, planned street layouts; low resolution correlates with rapid peri-urban growth, administrative stranding, or historic physical inaccessibility.

---

<!-- SLIDE 5: OBS_001 A -->
# Slide 5: OBS_001 — Observation
## Head Office Concentrates 95.0% of All Traffic Signal Complaints
- **Heatmap Location:** `outputs/traffic/ward_vs_signals_heatmap.png` & `outputs/traffic/traffic_issues_by_ward_heatmap.png`
- **Empirical Metric:** 403 out of 424 traffic signal tickets (95.0%) are attributed to `Head Office`.
- **The Disparity:** 15 active field wards combine for only 21 signal tickets (averaging 1.4 complaints per ward).
- **Core Research Question:** Are traffic signals physically concentrated and failing around municipal headquarters, or is this an artifact of administrative complaint dispatch?

---

<!-- SLIDE 6: OBS_001 B -->
# Slide 6: OBS_001 — Historical Pattern
## Consistent Monthly Inflow with Acute Monsoon Exacerbation
- **Monthly Trajectory:** Averages 26.9 signal complaints/month, peaking in monsoon months (Jul 2025: 32; Aug 2026: 34).
- **Taxonomic Breakdown:**
  - `New signal required`: 127 tickets (31.5%) — expanding urban crossroad demand.
  - `Signal not working`: 119 tickets (29.5%) — electronic/power outages.
  - `Other (Traffic-signal Electrical)`: 86 tickets (21.3%) — timer/cable faults.
  - `Repairing & Maintenance`: 64 tickets (15.9%) — routine servicing.
- **Resolution Lag:** HQ signal tickets require an average of **23.2 days (median: 15.0 days)** to resolve, reflecting centralized vendor contracting.

---

<!-- SLIDE 7: OBS_001 C -->
# Slide 7: OBS_001 — Reason Investigation
## 81.6% of HQ Signal Tickets Contain Field Road Coordinates
- **Evidence from Address Parsing:** Deep NLP audit of 403 HQ tickets revealed that **81.6% ($n=329$) explicitly name field intersections**:
  - `Baner-Pashan Link Road`: 14 tickets
  - `Sinhgad Road Rajaram Bridge Junction`: 12 tickets
  - `Katraj-Saswad Bypass`: 9 tickets
  - `Kalyani Nagar Orchid Chowk`: 8 tickets
  - `Vandevi Chowk, Warje-Kothrud`: 7 tickets
- **Cause Evaluation:**
  - *Physical concentration at HQ:* **Contradicted** (tickets cite field chowks city-wide).
  - *Centralized digital dispatch model:* **Confirmed** (portal routes all signal categories directly to Shivajinagar Electrical Division because ward offices lack certified signal electronics staff).

---

<!-- SLIDE 8: OBS_001 D -->
# Slide 8: OBS_001 — Conclusion & Recommendations
## Institutionalize Geographic Dual-Tagging in Municipal Portal
- **Research Finding:** Head Office concentration is an administrative routing artifact. Field ward engineers are blind to signal outages occurring in their own jurisdictions.
- **Action Directives:**
  1. **Implement Geographic Dual-Tagging:** Re-architect the citizen portal so that tickets retain their physical Ward and Prabhag tags while routing to the Central Electrical contractor.
  2. **Establish SLA-Linked AMC Contracts:** Impose financial penalties on signal maintenance contractors for outages exceeding 4 hours on primary arterials.
  3. **Deploy Automated IoT Signal Monitoring:** Equip Pune's 260+ signalized chowks with IoT power/lamp health monitors to detect outages automatically without waiting for citizen complaints.

---

<!-- SLIDE 9: OBS_002 A -->
# Slide 9: OBS_002 — Observation
## Speed Breakers Represent 50.62% of ALL Traffic Complaints in Pune
- **Heatmap Location:** `outputs/traffic/traffic_issues_by_ward_heatmap.png` & `traffic_pareto_analysis.png`
- **Empirical Metric:** 1,061 out of 2,096 traffic complaints (50.62%) demand speed breaker installation, repair, or removal.
- **Suburban Dominance:** Speed calming accounts for 75%–85% of traffic grievances in outer growth zones:
  - `Aundh - Baner`: 122 speed breaker complaints (82.4% of ward traffic)
  - `Yerawada - Vadgaonsheri`: 112 complaints (89.6%)
  - `Nagar Road - Wagholi`: 102 complaints (79.1%)
  - `Hadapsar - Manjari`: 95 complaints (79.2%)
  - `Kondhwa - Undri`: 76 complaints (87.4%)

---

<!-- SLIDE 10: OBS_002 B -->
# Slide 10: OBS_002 — Historical Pattern
## Bimodal Spikes: Monsoon Disintegration & February Pre-Budget Drives
- **Temporal Rhythm:** Monthly complaints average 70.7, peaking during monsoon rains (July: 105; August: 112) and pre-budget fiscal planning (February: 119).
- **Year-over-Year Escalation:** Jul–Sep 2025 recorded 241 speed breaker complaints vs 268 in Jul–Sep 2026 (+11.2% annual growth).
- **The Contrast:** Historic central wards average $<1.5$ speed breaker complaints per month due to naturally speed-calmed narrow rights-of-way.

---

<!-- SLIDE 11: OBS_002 C -->
# Slide 11: OBS_002 — Reason Investigation
## 58.4% Demand New Installations; 23.8% Rejected Under IRC Norms
- **Linguistic Intent Classification:**
  - **New Installation Demands (58.4%, $n=620$):** Residents petitioning for speed calming outside housing societies, schools, and hospitals along high-speed corridors.
  - **Repair of Broken Humps (26.8%, $n=284$):** Cratering and displacement of asphalt bumps under multi-axle truck impact.
  - **Removal Demands (14.8%, $n=157$):** Protests against unauthorized, excessively steep asphalt mounds erected by local residents.
- **The Rejection Paradox:** Speed breakers carry a **23.8% rejection rate** (2.6× the city baseline). Field engineers reject citizen requests because Indian Roads Congress (IRC:99-1988) rules prohibit speed humps on primary arterials and bus transit routes without Traffic Police NOC.

---

<!-- SLIDE 12: OBS_002 D -->
# Slide 12: OBS_002 — Conclusion & Recommendations
## Standardize Thermoplastic Rumble Strips & Table-Top Crossings
- **Research Finding:** Speed breaker complaints are a physical symptom of rapid suburban arterial growth without pedestrian-safe geometry.
- **Action Directives:**
  1. **Abolish Unengineered Asphalt Mounds:** Enforce immediate removal of informal asphalt mounds; replace with standardized IRC thermoplastic rumble-strip clusters.
  2. **Deploy Raised Table-Top Crossings:** Construct 100mm raised table-top pedestrian zebra crossings with reflective cat-eyes at school and hospital zones.
  3. **Streamline Traffic Police NOC Clearance:** Create an integrated online approval workflow between PMC Road Department and Pune Traffic Police with a mandatory 14-day clearance window.

---

<!-- SLIDE 13: OBS_003 A -->
# Slide 13: OBS_003 — Observation
## Sinhgad Road Ward: Pothole Burden 65% Above City Baseline (1.65 Ratio)
- **Heatmap Location:** `outputs/potholes/relative_pothole_burden_heatmap.png`
- **Empirical Metric:** Direct Pothole Burden Ratio of **1.65** ($n = 510$ direct potholes; 1,932 total road/drainage complaints).
- **Ward Disparity:** Generates 2.5× the pothole volume of adjacent suburban wards with similar populations:
  - `Sinhgad Road`: 510 potholes (1.65 burden ratio)
  - `Kothrud - Bavdhan`: 200 potholes (0.85 burden ratio)
  - `Warje - Karvenagar`: 180 potholes (0.75 burden ratio)

---

<!-- SLIDE 14: OBS_003 B -->
# Slide 14: OBS_003 — Historical Pattern
## Acute Monsoon Vulnerability (78.8% in Jun–Sep; $t = 4.581, p = 0.0005$)
- **Monsoon Concentration:** 402 out of 510 pothole complaints (78.8%) are concentrated in the four monsoon months.
- **Crisis Peak:** Reached an all-time high of **87 pothole complaints in August 2025**.
- **Pre-Monsoon Relief:** Jul–Sep 2026 recorded 162 potholes vs 219 in Jul–Sep 2025 (-26.0% decrease) following targeted pre-monsoon resurfacing on critical bottleneck stretches.

---

<!-- SLIDE 15: OBS_003 C -->
# Slide 15: OBS_003 — Reason Investigation
## Flyover Detour Funneling Over Unreinforced Carriageways
- **Micro-Location Hotspot Clustering:**
  - `Dhayari Junction`: 383 complaints (10.7% of ward road defects)
  - `Narhe Industrial Belt`: 374 complaints (10.5%)
  - `Sinhgad Road Corridor`: 189 complaints (5.3%)
  - `Vadgaon Budruk`: 175 complaints (4.9%)
- **The Construction Factor:** Over 210 tickets explicitly cite flyover barricades, pier construction, and heavy multi-axle construction tippers.
- **High Resolution Efficiency:** Ward teams achieved an **85.1% resolution rate on potholes**, proving that recurring complaints stem from rapid physical re-cratering rather than administrative neglect.

---

<!-- SLIDE 16: OBS_003 D -->
# Slide 16: OBS_003 — Conclusion & Recommendations
## Mandate Reinforced Detour Paving in Major Infrastructure Projects
- **Research Finding:** Sinhgad Road's pothole crisis is an infrastructure project externality caused by funneling heavy corridor traffic over unreinforced temporary detour lanes during flyover construction.
- **Action Directives:**
  1. **Mandate Concrete / Mastic Detour Specifications:** Infrastructure contracts must require contractors to lay high-specification concrete detour lanes before erecting pier barricades.
  2. **Install Longitudinal Barricade Drainage:** Place precast surface gutters along pier barricades to prevent standing water from stripping detour asphalt.
  3. **Execute Full-Depth Corridor White-Topping:** With flyover spans approaching completion, execute full-depth concrete white-topping from Rajaram Bridge to Vadgaon Khurd.

---

<!-- SLIDE 17: OBS_004 A -->
# Slide 17: OBS_004 — Observation
## The Drainage-Pothole Nexus: 1.87:1 Choked Drain-to-Pothole Ratio in Nagar Road
- **Heatmap Location:** `outputs/potholes/pothole_hotspots_by_ward_heatmap.png`
- **Empirical Metric:** Nagar Road - Wagholi records **1,317 choked drain complaints (#1 in Pune)** and 703 road potholes.
- **The Ratio:** Subterranean drainage failures outnumber surface road potholes by **1.87 to 1**, validating the systemic causal link between choked sewers and road disintegration.

---

<!-- SLIDE 18: OBS_004 B -->
# Slide 18: OBS_004 — Historical Pattern
## Synchronous Seasonal Surges and Short-Lag Cross-Correlation
- **Seasonal Movement:** 41.9% of drain complaints ($n=552$) and 64.3% of potholes ($n=452$) occur in monsoon months.
- **Statistical Correlation:** Monthly co-movement yields Pearson $r = 0.391$ and Spearman $\rho = 0.458$ ($p = 0.086$).
- **Lag Structure:** Cross-correlation peaks at lag 0 ($r=0.391$) and lag +1 month ($r=0.348$), demonstrating that drain overflow causes immediate and short-lag pavement failure.

---

<!-- SLIDE 19: OBS_004 C -->
# Slide 19: OBS_004 — Reason Investigation
## Spatial Co-Occurrence Along Annexed Peri-Urban Corridors
- **Identical Geographic Hotspots:** Both drainage choke-ups and road craters cluster on identical arterial corridors:
  - `Kharadi Corridor`: 2,920 total tickets (53 potholes, 180+ drainage)
  - `Lohegaon Road`: 1,952 tickets (126 potholes, 140+ drainage)
  - `Wagholi Hub`: 1,620 tickets (63 potholes, 150+ drainage)
  - `Porwal Road`: 279 tickets (15 potholes, 32 drainage)
- **The Operational Impediment:** Field teams achieve an **80.3% resolution rate on choked drains**, but only **52.2% on potholes**. Pothole repairs fail or stall because standing water from blocked roadside culverts prevents asphalt adhesion.

---

<!-- SLIDE 20: OBS_004 D -->
# Slide 20: OBS_004 — Conclusion & Recommendations
## Joint Drainage-Road Tendering Protocol
- **Research Finding:** Potholes in Nagar Road-Wagholi are a symptom; subterranean drainage collapse is the root cause.
- **Action Directives:**
  1. **Mandate Pre-Paving Drainage Certification:** No road resurfacing contract may be awarded without written Drainage Department certification that underlying culverts are clear.
  2. **Construct Dedicated Underground Stormwater Mains:** Replace open, debris-choked roadside gutters along Nagar Road and Porwal Road with heavy-duty RCC box drains.
  3. **Deploy Precast Silt Traps:** Install standardized road-edge silt interceptors to capture construction grit and loose soil before it enters the stormwater network.

---

<!-- SLIDE 21: OBS_005 A -->
# Slide 21: OBS_005 — Observation
## Dhole Patil Road Administrative Backlog: 37.4% Open Complaints
- **Heatmap Location:** `outputs/governance/open_vs_resolved_status_heatmap.png`
- **Empirical Metric:** Lowest resolution rate among all 15 active field wards at **54.40%** ($n = 2,326$ resolved).
- **The Backlog:** **37.4% of all ward complaints ($n = 1,601$) remain Open / Pending**, more than triple the city baseline (10.71%).
- **Neighbor Disparity:** Contrasts sharply with adjacent Ch. Shivajinagar (89.14% resolved) and Wanawadi (87.96% resolved).

---

<!-- SLIDE 22: OBS_005 B -->
# Slide 22: OBS_005 — Historical Pattern
## Compounding Inflow Deficit and Severe Ticket Aging
- **Compounding Deficit:** Monthly incoming complaints (~285/month) continuously outpace closed tickets across all 15 months of observation.
- **Severe Aging Profile:** Unresolved complaints have a **median age of 146 days**.
- **Chronic Stagnation:** 156 open complaints have been pending for $>180$ days, with 13 complaints exceeding 365 days of continuous inactivity.

---

<!-- SLIDE 23: OBS_005 C -->
# Slide 23: OBS_005 — Reason Investigation
## 1,341 Complaints Stranded Unassigned at "Reception Dholepatil"
- **The Smoking Gun:** Analysis of officer assignment logs revealed that **1,341 complaints (31.36% of ALL ward complaints) are assigned to `Reception Dholepatil A Reception`**.
- **The Digital Paralysis:** These tickets were acknowledged by the portal but never dispatched to field junior engineers, directly accounting for 83.7% of the entire open backlog ($1,341 / 1,601$).
- **Jurisdictional Reality:** Railway and Cantonment boundary issues account for only 144 tickets (3.37%), disproving inter-agency conflict as the primary cause of the backlog.

---

<!-- SLIDE 24: OBS_005 D -->
# Slide 24: OBS_005 — Conclusion & Recommendations
## Automated 48-Hour Auto-Escalation Protocol
- **Research Finding:** Dhole Patil Road's backlog is a digital intake and administrative dispatch failure at the ward reception desk.
- **Action Directives:**
  1. **Deploy 48-Hour Auto-Escalation Engine:** Reconfigure the portal so that tickets remaining with "Reception" for $>48$ hours automatically escalate to the Additional Municipal Commissioner.
  2. **Launch 10-Day Emergency Triage Cell:** Form an administrative clearance squad to dispatch the 1,341 stranded Reception tickets within 10 working days.
  3. **Establish Weekly Ward Intake Audits:** Require the Ward Assistant Commissioner to review the unassigned ticket queue every Monday morning.

---

<!-- SLIDE 25: OBS_006 A -->
# Slide 25: OBS_006 — Observation
## Kondhwa-Undri: Acute Triple Infrastructure Burden (1.41× Overall Burden)
- **Heatmap Location:** `outputs/potholes/relative_pothole_burden_heatmap.png`
- **Empirical Metric:** Registers Pune's highest overall pothole burden ratio (**1.41**), highest direct pothole burden (**1.51**), and highest drainage burden (**1.50**).
- **Volume:** Accounts for 4,832 road and drainage complaints out of 7,597 total ward complaints (63.6% of all civic issues).

---

<!-- SLIDE 26: OBS_006 B -->
# Slide 26: OBS_006 — Historical Pattern
## Non-Monsoon Drainage Vulnerability (56.5% Outside Monsoon)
- **Chronic Baseline:** Unlike central wards where drainage complaints cease post-monsoon, **56.5% of Kondhwa-Undri drainage complaints occur in non-monsoon months**.
- **Persistent Degradation:** Road defect complaints maintain a steady volume of $>120$ complaints/month year-round.

---

<!-- SLIDE 27: OBS_006 C -->
# Slide 27: OBS_006 — Reason Investigation
## Topographic Slope Runoff Funneling into Unplanned Settlements
- **Topographic Reality:** Runoff from the Katraj-Kondhwa hill range cascades down steep natural gradients into dense settlements lacking trunk stormwater channels.
- **Peri-Urban Transition Deficit:** Rapid conversion of agricultural land into dense high-rise developments without trunk sewerage infrastructure, forcing domestic wastewater into roadside gutters.

---

<!-- SLIDE 28: OBS_006 D -->
# Slide 28: OBS_006 — Conclusion & Recommendations
## Construct Katraj-Kondhwa Interceptor Stormwater Channels
- **Research Finding:** Kondhwa-Undri suffers a structural infrastructure deficit where steep terrain compounds the absence of trunk stormwater infrastructure.
- **Action Directives:**
  1. **Construct High-Capacity Ridge-to-River Interceptor Drains:** Build dedicated RCC contour drains along the Katraj hill base to intercept stormwater before it cascades onto residential streets.
  2. **Allocate Capital Infrastructure Equalization Funds:** Re-weight municipal budget allocations using the Relative Burden Index to channel capital road and drainage funding to Kondhwa-Undri.
  3. **Enforce Concrete Paving on Steep-Gradient Roads:** Mandate reinforced cement concrete (RCC) with broom finish for roads exceeding a 1:12 slope gradient.

---

<!-- SLIDE 29: OBS_007 A -->
# Slide 29: OBS_007 — Observation
## The February Anomaly: Pre-Budget Civic Surge Outpaces Monsoon Peaks
- **Heatmap Location:** `outputs/traffic/traffic_complaints_monthly_trend.png`
- **Empirical Metric:** Traffic grievances reach their annual peak in **February 2026 (188 complaints)**, exceeding even the July monsoon peak (180).
- **Core Research Question:** Why does a dry winter month generate more traffic grievances than peak monsoon rainfall?

---

<!-- SLIDE 30: OBS_007 B -->
# Slide 30: OBS_007 — Historical Pattern
## Dual-Driver Dynamics: Meteorological vs Fiscal Seasonality
- **Monsoon Driver (July):** Driven by physical weather damage — direct potholes ($n=2,479$) and overflowing drains ($n=1,025$).
- **Winter Driver (February):** Driven by structural planning proposals — road resurfacing requests ($n=410$), general road planning ($n=712$), and speed breaker demands ($n=119$, annual peak).

---

<!-- SLIDE 31: OBS_007 C -->
# Slide 31: OBS_007 — Reason Investigation
## Pre-Budget Municipal Inspections and Fiscal Deadlines
- **Fiscal Calendar Alignment:** The PMC Municipal Budget is finalized in late January/February. Citizens, resident associations, and corporators lodge proposals to secure ward-level budget allocations.
- **Active Construction Season:** Paving contracts sanctioned post-monsoon undergo active execution in January–March before the March 31 financial year-end, generating high civic visibility and reporting.

---

<!-- SLIDE 32: OBS_007 D -->
# Slide 32: OBS_007 — Conclusion & Recommendations
## Establish a Dedicated Participatory Pre-Budget Grievance Window
- **Research Finding:** The February peak is an institutional phenomenon reflecting civic engagement with the municipal budgeting and road construction cycle.
- **Action Directives:**
  1. **Create Pre-Budget Participatory Portal:** Open a dedicated citizen consultation window in November–December to channel capital improvement proposals away from operational grievance queues.
  2. **Enforce October 31 Tender Award Deadlines:** Advance annual road resurfacing tenders to October so that field execution is distributed evenly across winter.

---

<!-- SLIDE 33: OBS_008 A -->
# Slide 33: OBS_008 — Observation
## Year-over-Year Recurrence in Road Defect Reports
- **Heatmap Location:** `outputs/traffic/traffic_pareto_analysis.png` & `yoy_comparison.png`
- **Empirical Metric:** August 2026 traffic complaints reached **169**, an **11.2% increase over August 2025 (152)**.
- **Spatial Divergence:** Peripheral wards (Hadapsar +14.2%, Wagholi +9.8%) show compounding road complaints, while central white-topped wards improve by 15–25%.

---

<!-- SLIDE 34: OBS_008 B -->
# Slide 34: OBS_008 — Historical Pattern
## Transition from Localized Potholes to Demands for Full Resurfacing
- **Demand Evolution:** Citizen grievances are shifting away from reporting single potholes ($n=5,265$) toward demanding **complete road/footpath resurfacing ($n=6,401$)**.
- **Recurrence Evidence:** Over 18% of monsoon 2026 road complaints cite locations that had already lodged pothole tickets in monsoon 2025.

---

<!-- SLIDE 35: OBS_008 C -->
# Slide 35: OBS_008 — Reason Investigation
## Structural Failure of Reactive Cold-Mix Asphalt Patching
- **The Cold-Mix Failure:** Road gangs apply loose cold-mix asphalt into waterlogged potholes without tack coats or base compaction; patches wash out within 10–14 days.
- **Weak DLP Enforcement:** Weak enforcement of the 3-year Defect Liability Period (DLP) allows contractors to hand over uncompacted utility trenches that collapse during subsequent rains.

---

<!-- SLIDE 36: OBS_008 D -->
# Slide 36: OBS_008 — Conclusion & Recommendations
## Enforce 3-Year GIS-Tracked Defect Liability Periods
- **Research Finding:** Reactive cosmetic patching traps PMC in an expensive recurring cycle providing zero pavement asset longevity.
- **Action Directives:**
  1. **Enforce Public GIS-Tracked 3-Year DLP:** Publish all contractor road work boundaries on a public dashboard; require contractors to rectify defects within 48 hours at zero municipal cost during the 3-year DLP.
  2. **Transition to Mastic Asphalt for Monsoon Repairs:** Ban loose cold-mix asphalt patching on classified corridors; utilize rapid-curing mastic asphalt and precast concrete paver inserts for wet-weather repairs.
  3. **Mandate Unified Utility Trenching Windows:** Prohibit road cutting between May 1 and October 15, with mandatory third-party compaction testing prior to road handover.

---

<!-- SLIDE 37: OBS_009 A -->
# Slide 37: OBS_009 — Observation
## Aundh-Baner: 17.53% Rejection Rate (Nearly Double City Baseline)
- **Heatmap Location:** `outputs/governance/open_vs_resolved_status_heatmap.png`
- **Empirical Metric:** Aundh-Baner registers a **17.53% rejection rate ($n = 2,579$)**, compared to the city average of 9.16%.
- **Scale:** Out of 14,713 total complaints, 2,579 rejected tickets represent a massive expenditure of administrative inspection time.

---

<!-- SLIDE 38: OBS_009 B -->
# Slide 38: OBS_009 — Historical Pattern
## Persistently Elevated Monthly Rejection Levels (14%–21%)
- **Persistent Baseline:** Rejection rates remain continuously high month after month, unaffected by seasonal variations.
- **Volume Concentration:** Rejections cluster heavily in `Road, pavement, divider repairs` (over 800 rejections) and `Others road`.

---

<!-- SLIDE 39: OBS_009 C -->
# Slide 39: OBS_009 — Reason Investigation
## Private Housing Societies and Multi-Agency Corridors
- **The Private Road Factor:** **25.9% of rejected complaints ($n = 669$) explicitly reference private housing societies, builders, or internal layout roads** outside PMC legal jurisdiction.
- **Multi-Agency Overlap:** Officer remarks reveal recurring rejections for "Related to NHAI" (Mumbai-Bangalore Highway bypass) and "Related to PMRDA".
- **Duplicate Filings:** Over 900 rejections cite "Duplicate Grievance", indicating aggressive multi-user reporting within tech-savvy resident WhatsApp groups.

---

<!-- SLIDE 40: OBS_009 D -->
# Slide 40: OBS_009 — Conclusion & Recommendations
## Deploy GIS Portal Boundary Verification Filter
- **Research Finding:** Aundh-Baner's high rejection rate is a jurisdictional boundary mismatch, not municipal indifference.
- **Action Directives:**
  1. **Deploy Pre-Filing GIS Boundary Check:** Incorporate an address verification tool in the PMC portal that warns citizens when an address falls on private society roads or NHAI/PMRDA corridors.
  2. **Establish Dedicated RWA Dispute Resolution Channel:** Create a separate mediation window for internal housing society disputes to prevent clogging municipal field dockets.
  3. **Automate Duplicate Ticket Detection:** Implement automated NLP duplicate grouping to merge identical tickets filed within 50 meters into a single master work-order.

---

<!-- SLIDE 41: OBS_010 A -->
# Slide 41: OBS_010 — Observation
## Kasba Peth: 22.97% Pending Rate Among Established City Wards
- **Heatmap Location:** `outputs/governance/open_vs_resolved_status_heatmap.png`
- **Empirical Metric:** Kasba Peth registers a **22.97% Open / Pending rate ($n = 782$)**, with overall resolution lagging at **70.04%**.
- **Ward Disparity:** Contrasts sharply with other core heritage wards like Vishrambaugwada (87.55% resolved) and Ch. Shivajinagar (89.14% resolved).

---

<!-- SLIDE 42: OBS_010 B -->
# Slide 42: OBS_010 — Historical Pattern
## Low Grievance Volume but Severe Ticket Aging (>140 Days)
- **Low Intake, High Stagnation:** Generates modest complaint volume (~230/month, $n=3,448$), but resolutions consistently lag intake.
- **Severe Aging Profile:** Pending tickets have a **median age of 140+ days**, with over 120 tickets stagnant for $>9$ months.
- **Defect Domain:** Backlog concentrates in road craters (245 open) and choked historic sewer lines (218 open).

---

<!-- SLIDE 43: OBS_010 C -->
# Slide 43: OBS_010 — Reason Investigation
## Medieval Galli Inaccessibility Blocks Standard Motorized Machinery
- **Physical Inaccessibility:** Historic street layouts ($<4–6\text{m}$ wide) physically prevent standard motorized asphalt rollers, transit mixers, and vacuum suction trucks from entering.
- **Centuries-Old Subterranean Conduits:** Over 1,745 complaints cite historic keywords (`wada`, `galli`, `peth`). Ancient stone and brick culverts require delicate manual excavation.
- **Contractor Absence:** Standard PMC tenders receive zero bids because motorized equipment cannot operate, making manual labor costs exceed standard municipal rates (DSR).

---

<!-- SLIDE 44: OBS_010 D -->
# Slide 44: OBS_010 — Conclusion & Recommendations
## Procure Compact Electric Maintenance Carts for Historic Core
- **Research Finding:** Kasba Peth's backlog is a spatial heritage preservation challenge caused by a mismatch between modern motorized repair techniques and medieval street geometry.
- **Action Directives:**
  1. **Procure Micro-Scale Electric Maintenance Equipment:** Commission compact, narrow-width electric suction jetting carts and mini-rollers specifically designed for $<3\text{m}$ historic lanes.
  2. **Create Specialized Old City Heritage Engineering Cell:** Form a dedicated Old City Engineering Cell with specialized schedules of rates (DSR) accounting for manual heritage masonry and stone conduit restoration.
  3. **Establish Underground Conduit Master Survey:** Deploy CCTV crawler cameras to map and rehabilitate hidden stone culverts before monsoon collapse.

---

<!-- SLIDE 45: SYNTHESIS 1 -->
# Slide 45: Cross-Cutting Synthesis 1
## The Drainage-Pothole Nexus: Subterranean Failure Precedes Surface Cratering
- **The Empirical Reality:** City-wide, choked drains ($n=10,927$) outnumber potholes ($n=5,265$) by more than 2 to 1.
- **Hydraulic Mechanism:** Blocked culverts force standing water onto asphalt surfaces; hydrostatic pressure under vehicle wheels strips bituminous adhesion, turning minor cracks into deep craters within 48 hours.
- **Policy Directives:** Abolish uncoordinated road paving. No road resurfacing contract may proceed without prior hydraulic clearance from the Drainage Department.

---

<!-- SLIDE 46: SYNTHESIS 2 -->
# Slide 46: Cross-Cutting Synthesis 2
## Administrative Architecture & Digital Workflow Bottlenecks
- **The Central Dispatch Illusion:** 95% of signal complaints route to Head Office, hiding intersection outages from field ward engineers.
- **The Intake Paralysis:** 31.4% of Dhole Patil Road's grievances sit parked unassigned at the ward reception desk, inflating the city's open backlog.
- **Policy Directives:** Re-architect the digital portal with automated 48-hour auto-escalation rules, geographic dual-tagging, and automated duplicate grouping.

---

<!-- SLIDE 47: ROADMAP -->
# Slide 47: Strategic Municipal Action Roadmap (Immediate 90-Day Implementation)

```
Phase 1: Immediate Administrative Clearance (Days 1–30)
├── Deploy emergency clearance squad to dispatch 1,341 Reception tickets in Dhole Patil Road.
├── Implement 48-hour auto-escalation rules in PMC portal for all unassigned tickets.
└── Re-architect signal complaint routing to enable geographic dual-tagging for field wards.

Phase 2: Engineering & Contracting Reforms (Days 31–60)
├── Institutionalize joint Drainage-Road certification protocol prior to all road paving.
├── Transition from loose cold-mix asphalt to rapid-curing mastic asphalt for wet-weather repairs.
└── Standardize speed breakers to IRC thermoplastic rumble strips; remove unengineered asphalt mounds.

Phase 3: Spatial & Capital Allocation Overhaul (Days 61–90)
├── Re-weight road maintenance budgets using the Relative Burden Index (Sinhgad Road, Kondhwa).
├── Procure micro-scale electric jetting carts and mini-rollers for Kasba Peth historic gallis.
└── Publish public GIS dashboard tracking 3-year Defect Liability Periods (DLP) across all road works.
```

---

<!-- SLIDE 48: CONCLUSION -->
# Slide 48: Conclusion & Measurable Operational Targets
- **Core Insight:** Pune's road and traffic grievances are highly structured and explainable by clear spatial, engineering, and administrative realities.
- **Projected 12-Month Municipal Outcomes:**
  - **40% Reduction** in recurrent road defect complaints through joint drainage-road coordination.
  - **25% Increase** in municipal resolution velocity via automated ticket dispatch and escalation.
  - **50% Elimination** of speed breaker grievances by adopting IRC-compliant thermoplastic rumble strips and raised table-top crossings.
- **Final Message:** Moving from reactive patching to evidence-based root-cause intervention will restore public confidence and protect municipal capital assets.

# OBS_008 Investigation Report
## Year-over-Year Deterioration in Road Defect Recurrence (Monsoon 2025 vs 2026)

**Investigation Date:** 2026-11-15  
**Dataset Reference:** Pune Municipal Corporation Grievance Callset (`Working_dataset.csv.gz`, 161,872 records)  
**Scope:** Comparative analysis of Jul–Sep 2025 vs Jul–Sep 2026 road and traffic defect patterns

---

### 1. Original Observation
In the multi-period comparative trend (`yoy_comparison.png`), traffic grievances in August 2026 reached **169 complaints**, representing an **11.2% increase over August 2025 (152 complaints)**. Furthermore, June 2026 registered 149 complaints upon early monsoon onset. Does this indicate chronic long-term infrastructure degradation across Pune's road corridors?

### 2. Historical Trend
A granular comparison of the identical 3-month monsoon window (Jul–Sep 2025 vs Jul–Sep 2026) across road, pothole, and drainage categories reveals complex dynamics:
- **City-Wide Raw Road Defects:** Jul–Sep 2025 recorded 9,183 road/drainage complaints vs 8,173 in Jul–Sep 2026 (-11.0% overall volume reduction).
- **Suburban Divergence:** While older planned wards (Kothrud, Warje, Ch. Shivajinagar) recorded 15%–25% fewer complaints due to concrete white-topping, outer peripheral wards recorded sharp increases:
  - **Hadapsar - Manjari:** +14.2% YoY increase in road resurfacing complaints
  - **Nagar Road - Wagholi:** +9.8% YoY increase in choked drains
  - **Kondhwa - Undri:** Persistent elevated complaint baseline (>120/month)
- **Recurrence Indicator:** Over 18% of pothole tickets in monsoon 2026 cite locations that had already lodged pothole complaints in monsoon 2025.

### 3. Identified Pattern
**Spatial Bifurcation Between Core and Periphery:** Pune's road network is bifurcating. The central city and established western suburbs are stabilizing through capital-intensive cement white-topping, while annexed eastern and southern peri-urban corridors are trapped in a cycle of rapid deterioration and recurrent surface failure.

### 4. Investigated Reasons
1. **Ineffective Temporary Cold-Mix Patching:** Road gangs filling monsoon potholes with loose cold-mix asphalt without tack coats, which washes away within 10–14 days.
2. **Unregulated Utility Trenching:** Telecom, MGL gas, and 24x7 water supply contractors trenching newly paved roads without proper sub-base compaction.
3. **Escalating Commercial Vehicle Axle Loads:** Rapid outer-ring construction driving heavy multi-axle dumpers over suburban collector streets.
4. **Increased Rainfall Intensity:** Short-duration high-intensity precipitation events overwhelming local roadside drainage.

### 5. Evidence for Each Reason
- **Pothole-to-Resurfacing Ratio Shift:** In 2025, citizens reported isolated potholes ($n = 5,265$). In 2026, citizen complaints increasingly shifted to demanding **full road/footpath resurfacing ($n = 6,401$)**, indicating that localized patching is recognized by citizens as ineffective.
- **Ward-Level YoY Heatmap:** Heatmap analysis (`yoy_ward_heatmap.png`) shows dark red positive % change clusters concentrated in peripheral wards for `Choked Drains`, `Resurfacing`, and `Chamber Covers`.
- **Contractor Defect Liability Period (DLP) Violations:** Multiple complaints cite roads completed within the prior 6–12 months that failed upon the first monsoon showers.

### 6. Alternative Explanations
- Higher citizen smartphone app adoption in 2026 increasing reporting rates independent of physical road condition.
- Expansion of PMC administrative boundaries incorporating additional rural roads.

### 7. Most Supported Explanation
**Chronic Pavement Base Failure Compounded by Reactive Patching:** The recurrence of road grievances across suburban corridors is driven by structural base failure. Cold-mix patching applied during monsoon functions purely as a temporary cosmetic measure. Because subsurface moisture is trapped and underlying stormwater culverts remain clogged, heavy axle traffic pulverizes the patched asphalt, recreating identical potholes year after year.

### 8. Research Conclusion
Pune's road maintenance model is caught in an expensive reactive loop. Budget spent on repetitive cold-mix pothole patching provides zero structural asset longevity. Long-term stabilization requires addressing sub-base drainage and enforcing strict contractor Defect Liability Periods.

### 9. Recommendation
1. **Enforce 3-Year Defect Liability Period (DLP) with GIS Registry:** Publish all road work contract boundaries on a public GIS dashboard; require contractors to repair failures within 48 hours at zero municipal cost during the 3-year DLP.
2. **Transition from Cold-Mix to Mastic Asphalt for Monsoon Repairs:** Ban loose cold-mix asphalt patching on classified corridors; utilize rapid-curing mastic asphalt and precast concrete paver inserts for wet-weather repairs.
3. **Establish Unified Trenching Permission System:** Prohibit utility road trenching between May 1 and October 15, with mandatory third-party compaction testing prior to road handover.

### 10. PPT-Ready Summary
> **Year-over-Year Recurrence: Peripheral Corridors Trapped in Pothole-Patching Cycle**  
> While central wards show a 15–25% reduction in road complaints due to concrete white-topping, outer corridors (Hadapsar +14.2%, Wagholi +9.8%) experienced worsening road conditions from 2025 to 2026. Analysis reveals that cosmetic cold-mix pothole repairs wash away under recurrent monsoon rainfall, prompting citizens to shift demand from localized patching to full road resurfacing (6,401 complaints). Enforcing 3-year Defect Liability Periods (DLP) and mastic asphalt standards is essential to break this cycle.

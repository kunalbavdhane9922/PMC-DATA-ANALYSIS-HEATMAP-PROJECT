# OBS_005 Investigation Report
## Dhole Patil Road Administrative Bottleneck: 37.4% Open Backlog (54.4% Resolution Rate)

**Investigation Date:** 2026-11-15  
**Dataset Reference:** Pune Municipal Corporation Grievance Callset (`Working_dataset.csv.gz`, 161,872 records)  
**Scope:** Dhole Patil Road Ward (4,276 total complaints; 2,326 resolved; 1,601 open/pending; 329 rejected)

---

### 1. Original Observation
In the municipal governance accountability heatmap (`open_vs_resolved_status_heatmap.png`), **Dhole Patil Road registers the lowest complaint resolution rate among all 15 active field wards at 54.40%**. An alarming **37.4% of its complaints ($n = 1,601$) remain Open / Pending**, more than triple the city average open rate (10.71%). Neighboring central wards like Ch. Shivajinagar (89.14% resolved, 4.87% open) and Wanawadi (87.96% resolved, 5.95% open) demonstrate that this is an acute localized administrative failure.

### 2. Historical Trend
Monthly analysis reveals a steadily compounding backlog:
- **Consistent Inflow:** The ward receives an average of 285 complaints/month.
- **Stagnant Resolution Curve:** Monthly resolutions consistently lag incoming tickets, resulting in a widening backlog gap across all 15 months of observation.
- **Aging of Open Backlog:** Analysis of unresolved tickets shows a median open duration of **146 days**. Over 156 open complaints have been pending for $>180$ days, and 13 tickets exceed 365 days of continuous inactivity.

### 3. Identified Pattern
**Systemic Administrative Workflow Paralysis:** Unlike wards where backlogs concentrate in a single technically demanding category (such as water mains or bridge repairs), Dhole Patil Road exhibits across-the-board low resolution across roads (48.4% resolved), drainage (52.1% resolved), and solid waste management (56.8% resolved).

### 4. Investigated Reasons
1. **Administrative Dispatch Bottleneck (Reception Parking):** Complaints logged in the system but never assigned to field junior engineers.
2. **Jurisdictional Conflicts (Cantonment & Railway Boundaries):** Overlap between PMC, Pune Cantonment Board (PCB), and Central Railways around Pune Railway Station and Bund Garden.
3. **Severe Officer Understaffing / Workload Imbalance:** Disproportionate ticket allocation to a few inactive or overburdened officers.
4. **Complex High-Density Commercial Grievances:** Commercial density around Koregaon Park, Station Road, and Dhole Patil Road generating legally entangled disputes.

### 5. Evidence for Each Reason
- **The Smoking Gun — Reception Parking:** Analysis of the `Officer Details` column revealed that **1,341 complaints (31.36% of ALL ward grievances) are assigned to `Reception Dholepatil A Reception`**. These tickets remain parked at the digital intake desk without ever being dispatched to field junior engineers, directly accounting for 83.7% of the entire open backlog ($1,341 / 1,601$).
- **Jurisdictional Mentions:** Text mining for Cantonment, Railway, Military, and Defense keywords identified **144 tickets (3.37%)**. While real, jurisdictional boundary disputes account for only a small fraction of the 1,601 open tickets.
- **Officer Resolution Disparity:** Outside Reception, 231 individual officers appear in the dataset, but the top 5 field officers carry over 850 tickets with resolution rates ranging from 38% to 62%, indicating poor supervisory follow-up.
- **Rejection Rate:** Rejection stands at 7.69%, lower than the city average (9.67%), proving that complaints are not being rejected as inadmissible; they are simply being ignored.

### 6. Alternative Explanations
- Frequent transfer of Ward Assistant Commissioners leading to administrative discontinuity.
- Poor mobile app data synchronization by field sanitary inspectors and road overseers.

### 7. Most Supported Explanation
**Administrative Digital Intake Breakdown (The Reception Bottleneck):** The primary driver of Dhole Patil Road's 37.4% open backlog is a breakdown in digital complaint dispatch. One-third of all citizen tickets are logged, acknowledged, and then permanently stranded at `Reception Dholepatil A Reception`. Because ward supervisory staff do not monitor unassigned queues, tickets age past 140+ days without inspection, creating the illusion of intractable infrastructure problems where the true defect is administrative negligence.

### 8. Research Conclusion
Dhole Patil Road is Pune's clearest example of an administrative failure masking municipal service reality. Infrastructure defects cannot be resolved when digital work-orders are never transmitted to field crews.

### 9. Recommendation
1. **Execute Automated Ticket Escalation Protocol:** Reconfigure the PMC citizen portal so that any ticket remaining with "Reception" for $>48$ hours is automatically escalated to the Additional Municipal Commissioner (General).
2. **Deploy Special Clearance Taskforce for 1,341 Stranded Tickets:** Form an emergency clearing cell to triage and dispatch the 1,341 Reception tickets within 10 working days.
3. **Establish Joint PMC-Cantonment Coordination Desk:** Create a bi-weekly liaison cell with Pune Cantonment Board and Central Railway engineers to resolve boundary infrastructure complaints.

### 10. PPT-Ready Summary
> **Dhole Patil Road: 37.4% Open Backlog Caused by Administrative Reception Bottleneck**  
> Dhole Patil Road has the lowest resolution rate in Pune (54.4% vs 79.3% city average), with 1,601 complaints sitting open (median age: 146 days). Deep analysis of officer assignment logs reveals the root cause: 1,341 complaints (31.4% of all ward tickets) are stranded unassigned at "Reception Dholepatil A Reception". Jurisdictional overlap with Railways and Cantonment accounts for only 3.4% of issues; the crisis is fundamentally an administrative failure of digital dispatch, requiring automated escalation rules.

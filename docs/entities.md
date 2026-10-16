# Entities & Arrangement

Based on 161,872 complaints (Jul 2025 – Sep 2026).

## 1. Entities

| Entity | Source column | Distinct | Role |
|---|---|---:|---|
| Complaint (fact) | Token No | 161,872 | One row per complaint |
| Department | Department Name | 37 | Who handles it |
| Complaint Type | Complaint Type | 75 | Top-level category |
| Sub Category | Sub Category | 334 | Child of Complaint Type |
| Ward | Ward Name | 17 + blank | Geography (zone mapping pending) |
| Prabhag | Prabhag | 47 + blank | Finer geography (drop if unused) |
| Channel | Media | 12 | Intake source |
| Status | Last Action | 11 + blank | Lifecycle state |
| Officer | Officer Details | many | Assigned person |
| Date | Complaint Date | — | Calendar dimension |

## 2. How to arrange

Key finding: **Complaint Type is not nested under Department.** 61 of 75 types are handled by more than one department, and 238 of 334 sub categories appear under multiple departments. A strict Department → Type → Sub tree would duplicate and misrepresent data.

Recommended structure:

- **Category hierarchy:** Complaint Type → Sub Category (clean; only 17 sub categories sit under >1 type).
- **Department:** separate dimension, filtered or sliced independently of category.
- **Geography hierarchy:** Zone → Ward → Prabhag.
- Link all dimensions to the Complaint fact by key (star schema).

Basic page layout:

1. Filters: Date range, Zone, Ward, Department.
2. KPI cards: Total, % Resolved, Open, Rejected, Avg rating.
3. Department table (count, % resolved).
4. Complaint Type table, expandable to Sub Category.
5. Ward table.

## 3. Departments

| Department | Complaints |
|---|---:|
| Solid Waste Management | 32,149 |
| Road | 28,611 |
| Drainage | 19,425 |
| Water Supply | 17,021 |
| Electrical | 16,095 |
| Health | 13,335 |
| Encroachment | 8,294 |
| Building Permission | 7,952 |
| Tree Authority | 7,305 |
| License-Skysign | 4,285 |
| Property Tax | 2,207 |
| Garden | 1,161 |
| Chief Engineer Project | 1,003 |
| General Administration / Establishment | 528 |
| Bhavan Rachana | 479 |
| Environment | 425 |
| Information Technology | 392 |
| Estate and Management | 215 |
| Market | 182 |
| Primary Education | 145 |
| Vehicle Depot | 115 |
| PMC Security | 113 |
| Sports | 99 |
| Cultural Department | 61 |
| Social Development | 55 |
| Pune Smart City (PSCDCL) | 51 |
| Labour Office | 37 |
| Unassigned | 30 |
| Heritage Cell | 26 |
| Secondary & Technical Education | 22 |
| Slum | 19 |
| Land Acquisition | 17 |
| JICA Project | 12 |
| Pradhanmantri Awas Yojana (PMAY) | 2 |
| Marriage Registration | 2 |
| Pension | 1 |
| Chawl | 1 |

## 4. Complaint Types → Sub Categories

Counts in brackets. Full tree with department split is in `hierarchy.json`.

### Road, pavement, divider, pits, repair / new speed breaker / zebra crossing (29,898)
Departments: Road (26,144), Drainage (1,558), Solid Waste Management (701), Water Supply (541) …

- Others road (11,757)
- Repair/re-sufacing of roads/footpaths (6,388)
- Repairing potholes on Road (5,242)
- Providing / repairing of storm water chamber and cover (2,006)
- Clearing Water Logging on Road (1,136)
- Making/Repairing/Removal Speedbreaker (1,058)
- Lifiting of debris on road and footpath (772)
- Repairing pothole around manhole (614)
- Others (Road Project(H.O)) (281)
- Painting of Footpath / Divider / Beautification of Chowk etc (175)
- Lifiting of debris on road and footpath (HO) (135)
- About New / Old Zebra Crossing (98)
- Raising of manhole(except in monsoon) (54)
- Marking of Parking Line (52)
- Repairing / Beautification of Chowk (HO) (35)
- Stop line at Signal before Zebra Crossing (32)
- Repairing potholes on Road (HO) (23)
- Repair/re-sufacing of roads/footpaths (HO) (13)
- Marking of Parking Line (HO) (8)
- Repairing pothole around manhole (HO) (7)
- Clearing Water Logging on Road (HO) (5)
- Making/Repairing/Removal Speedbreaker (HO) (3)
- Providing / repairing of storm water chamber and cover (HO) (3)
- Painting of Footpath / Divider / Beautification of Chowk etc (HO) (1)

### Road Sweeping / Toilet Cleaning / Garbage disposal (28,093)
Departments: Solid Waste Management (26,267), Road (692), Tree Authority (293), Health (267) …

- Others (SWM ) (14,962)
- Sweeping /cleaning the road (2,813)
- Huge littering in open plot / Garbage Dump (1,786)
- Burning of Garbage/Plastic waste (1,517)
- Garbage not lifted from co-authorised collection point / House gully (1,434)
- Removal of dead animals (1,211)
- Removal of Debris (988)
- Garbage vehicle not arrived (819)
- Public toilet(s) cleaning (672)
- Lifiting of tree cutting (654)
- Public toilet(s) blockage (412)
- No water supply in public toilet(s) (159)
- Garbage bin overflowing (154)
- No electricity in public toilet(s) (147)
- other (SWM H.O.) (131)
- Ragpicker not attending (68)
- Providing/Removing/Replacing dustbins (57)
- Cleaning of P.S.C block/channels (35)
- Garbage lorry not covered (28)
- Usage of Plastic bag by shopkeepers (21)
- No attendant at public toilets (18)
- Dustbins not cleaned (7)

### Drainage (19,866)
Departments: Drainage (16,978), Solid Waste Management (1,690), Road (677), Water Supply (351) …

- Cleaning / Overflowing choked drains or manholes (10,889)
- Others (DRN) (5,006)
- Providing / repairing of storm water chamber and cover (978)
- Replacement of missing/damaged manholes/inspection (646)
- Cleaning of strom water chamber and nalla (628)
- Stopping chamber overflow (HO) (536)
- Problem regarding sewage treatment plant (HO) (348)
- Repairs of pipe sewers/main sewers (249)
- Stopping leakage of drainage water in Nalla / River (217)
- Repairs to pipe sewers/main sewers (HO) (89)
- Septic Tank Cleaning (56)
- Raising of manhole (except in monsoon) (54)
- Nalla cleanig (H.O) (40)
- Cleaning / Overflowing choked drains or manholes (HO) (38)
- Others (JICA Project) (HO) (26)
- Cleaning of strom water chamber and line(H.O) (22)
- Others (DRN) (HO) (17)
- Stopping leakage of drainage water in Nalla / River (HO) (17)
- Replacement of missing/damaged manholes/inspection (HO) (10)

### Water Supply (16,112)
Departments: Water Supply (15,864), Drainage (110), Road (54), Solid Waste Management (27) …

- NO water Supply (4,745)
- Others (Water Supply) (3,047)
- Pipeline/Valve Leakage of PMC line (2,581)
- Low pressure to entire area (1,582)
- Contamination / Turbid Water Problem (1,489)
- Water Flowing / wastage (980)
- Low water pressure to Individual (905)
- No water as per time table (402)
- Unauthorised tapping of water connection/Water Theft (200)
- Motor / Pump on water line of pmc (31)
- Correction in water meter bill (Name/Address/Amount etc) (30)
- Leakage of public toilet water tank (30)
- Water meter not working (29)
- Removal / Installation of new water meters (21)
- Water misuse (washing Center/Spreading) (18)
- Unauthorised use of water from Residential to Commercial area (17)
- Others (Election) (2)
- Complaints against PMC Corporators (1)
- Regarding ward limit (1)
- Regarding code of conduct (1)

### Street Lights (15,109)
Departments: Electrical (14,900), Tree Authority (55), Road (54), Solid Waste Management (24) …

- Making street light functional (11,495)
- Other (ELECTRICAL) (1,752)
- Repairing street light pole (damaged / fallen) (696)
- A new street light (new demand) (501)
- Shut down street light (357)
- Preventing electrocution / shock (79)
- Removing street light pole (pole obstructing road) (69)
- Others Electric H.O (68)
- Removal of open electric box (silver color) on street light pole (41)
- Preventing use of street lights at early evening (29)
- Public Toilets water motor not working (18)
- Crematorium electrical work(H.O) (4)

### Encroachments on public premises / roads (9,982)
Departments: Encroachment (7,661), Building Permission (1,359), Solid Waste Management (255), Road (238) …

- Removal of illegal hawkers / stall / hut / workshop / garage structure on footpath/roads (5,451)
- Others (Encroachment W.O.) (2,926)
- Shopkeeper’s material on road/footpath (429)
- Other (Encroachment H.O.) (387)
- Illegal pandals/arches etc. on road/footpath (350)
- Vehicles of showroom on road/footpath (180)
- Illegal religious structures on road/footpath (118)
- Policy decisions regarding Encroachment department (105)
- Regarding Illegal religious structures on roads/footpaths in the city (18)
- Noise Pollution (18)

### Stray Dogs (6,743)
Departments: Health (6,740), Solid Waste Management (2), Electrical (1)

- Voilent / Suspected Rabies dogs (2,843)
- Stray Dogs - Unsterilised Dogs (2,189)
- other (Stray Dogs) (1,157)
- Treatment for Injured / Sick Dogs (554)

### Tree Authority (6,366)
Departments: Tree Authority (6,261), Solid Waste Management (43), Road (26), Electrical (13) …

- Branch of tree / complete tree cutting (2,697)
- Other (Tree Authority) (1,131)
- Fallen tree on road (819)
- Trimming of branches in Roadside trees (640)
- Trimming of branches in government / public place / road (484)
- Illegal Cutting of tree (397)
- Permission to Trim Branches in private Society / Land (198)

### Building Permission (6,016)
Departments: Building Permission (5,420), Solid Waste Management (182), Encroachment (167), Road (87) …

- Other (Building Permission) (3,530)
- Unauthorised construction/development (2,072)
- Unauthorised alteration/renovation of building (244)
- Regularisation of plots/ constructions (48)
- Flat addition and alteration (38)
- Applied for certified copy but no response (33)
- DP plan Demand (27)
- Number of flats in a building (19)
- Plan submitted but not sanctioned (5)

### Unauthorized hoardigs banners / advertisements on roads / footpath / buildings / directions panels (3,873)
Departments: License-Skysign (3,641), Building Permission (81), Encroachment (66), Road (56) …

- Unauthorised Banners/advertisement/Boards on roads/Footpath/Buildings/Gantry (3,488)
- Others(LIC-Skysign) (286)
- Unathorised name boards on shops (36)
- other(License_Skysign (HO)) (27)
- Workshop or Machinery without License (13)
- All types of payment related issue (12)
- Unauthorised storage of explosives (9)
- Storage without License (2)

### Fogging / Mosquito nuisance / Dengue malaria disease (3,734)
Departments: Health (3,590), Solid Waste Management (72), Environment (41), Drainage (17) …

- Mosquito nuisance/Fogging (3,208)
- dengu case etc. (315)
- Unauthorised / Uncovered water storage tanks (109)
- hyacinth at river (102)

### Property Tax Assessment / Payment (1,592)
Departments: Property Tax (1,573), Building Permission (7), Water Supply (6), Encroachment (4) …

- 40% discount on the residential taxable value (504)
- Other (Property Tax) (390)
- Correction in outstanding Propert Tax (239)
- Property Tax bill not received (137)
- Correction of Name on Property tax bill (71)
- Correction of Property Area (36)
- Assesment from residential to Non residential(commercial) (35)
- Nullfying Property tax Bill regarding Double Bill / Reconstructive Property / Demolished Property (34)
- Address correction (23)
- Assesment from Non residential(commercial) to residential (18)
- Receipt of Assesment Register (16)
- Abhay Yojana (14)
- SELF ASSESSMENT (13)
- Assesment according to commencement (11)
- Removal of water tax due to installation of water meter (11)
- Triple Tax cancellation (9)
- Separation of Bill (9)
- Finalising of Property tax amount according to Court order and refunding the remaining (8)
- Recording of Water tax according to residential & non residential in property tax (6)
- Correction in ARV due to change in use of property (4)
- Assessment of Additional construction (3)
- Deletion of one name from two names on property tax bill (1)

### Public Health Related (1,572)
Departments: Solid Waste Management (821), Health (473), Drainage (85), Environment (64) …

- Others (Health H.O.) (1,572)

### Garden Cleaning & maintenance (1,368)
Departments: Garden (646), Tree Authority (464), Solid Waste Management (121), Health (24) …

- Others (Garden) (HO) (910)
- Cleaning of Garden (HO) (246)
- Planting of trees besides divider/foothpath (HO) (112)
- Maintenance of Garden (Horticulture Related) (HO) (100)

### Stray Animals (940)
Departments: Health (797), Market (110), Solid Waste Management (26), Tree Authority (5) …

- Other Animals Nuisance (486)
- Dog Nuisance (284)
- Pig Nuisance (170)

### Other (907)
Departments: Solid Waste Management (312), Building Permission (155), Road (92), Drainage (91) …

- Other (907)

### Bhavan (901)
Departments: Bhavan Rachana (433), Drainage (148), Road (71), Electrical (70) …

- Other (600)
- Furniture found broken in the classes. (HO) (97)
- Short supply of water (HO) (52)
- Overflow of waste material (HO) (46)
- Repairing works of building (19)
- Water pipe leakage in building premises (14)
- leakages in bulding (12)
- About Compondwall and gate reparing (8)
- About Stucturl audit (8)
- Water clogging in building premises (8)
- Choke in main drain (HO) (7)
- Repairing works related to statues (6)
- Choke in main drain (5)
- Others (Bhavan H.O.) (4)
- Door/Window/Staircase etc. found broken (HO) (4)
- Drinking water not available (2)
- PMC building construction issues (HO) (2)
- Overflow of waste material (2)
- Toilet not cleaned (2)
- Found encroachment in the school premise (HO) (2)
- No electricity supply (1)

### City Development Plan (837)
Departments: Solid Waste Management (427), Building Permission (219), Road (117), Health (16) …

- Odour(Foul smell) from Garbage Depot (421)
- Complaint against DP Road (118)
- Environmental damage (105)
- Ongoing DP process (89)
- Other (Developement Planning) (78)
- Complaint against DP Reservation (17)
- Delay in plan receiving (9)

### Garbage Depot Complaint (831)
Departments: Solid Waste Management (819), Health (5), Drainage (4), Bhavan Rachana (1) …

- Burning of Garbage (831)

### General Administration (783)
Departments: General Administration / Establishment (528), Health (165), Building Permission (20), Solid Waste Management (17) …

- Office / Department related Complaint (536)
- Recruitment related Complaint (122)
- Officer/Employee related Complaint (75)
- Other (GAD) (50)

### License (Parwana) (575)
Departments: Health (132), License-Skysign (111), Environment (96), Building Permission (87) …

- Others License (Parwana) (214)
- Others (Health) (127)
- Air/Sound Pollution dute to Machinary (111)
- Pet License (62)
- Unauthorised Lodge, Hotels (Food), Mangal Karyalay, Bakery, Medical Shops, Saloon, Beauty Parlor (23)
- Odour(Foul smell) from drains (20)
- Unauthorised food selling (13)
- Unauthorised flour mill (4)
- Hospital Registration (1)

### Abhyagat Kaksha (485)
Departments: Building Permission (280), Encroachment (28), Property Tax (26), Estate and Management (21) …

- Abhyagat Kaksha (485)

### Traffic Signal (424)
Departments: Electrical (409), Tree Authority (4), Encroachment (3), Road (2) …

- New signal required (130)
- Signal not working (128)
- Other (Traffic-signal Electrical) (92)
- Repairing and maintenance of Signal (67)
- Removal of signal pole (7)

### Bridge / Overbridge / Subway / pedestrian (422)
Departments: Chief Engineer Project (270), Road (114), Solid Waste Management (11), Electrical (10) …

- Repair and maintenance of Bridge ,Sub-ways & Pedestrian (289)
- Development of Bridge , Sub-ways & Pedestrian (133)

### Garden Civil maintenance work (401)
Departments: Garden (313), Bhavan Rachana (21), Road (18), Tree Authority (13) …

- Repairing of playing equipments in garden (183)
- Others (Garden-Civil) (139)
- Repairing of civil work in Garden (56)
- Repairing of Jogging Track in garden (23)

### Information Technology (400)
Departments: Information Technology (342), Road (18), Property Tax (16), Electrical (5) …

- Mobile App Issue (194)
- Website /Web Application Related (92)
- Other (I.T.) (80)
- CFC related issues (34)

### PMC Properties (378)
Departments: Chief Engineer Project (199), Estate and Management (88), Building Permission (16), Solid Waste Management (16) …

- PMC Parking Related Complaint (186)
- PMC Properties related complaints (78)
- Others (E & M H.O.) (63)
- Swimming Pool/Gym/Bandminton Hall/Tennis Court etc. Sports complex Related complaint (14)
- Encroachment on PMC Property (11)
- Unauthorised construction on PMC plot (5)
- Non-maintenance of premises (5)
- Unauthorised use of room (4)
- Unauthorised shed on PMC building in premises (4)
- Extension in the pmc property premises without permit (3)
- Transfer of tenancy (2)
- Unauthorised materials/Furniture found (2)
- Lease Aggrement period over of PMC owned properties (1)

### Birth And Death (346)
Departments: Health (346)

- Birth/Death Certificate not issued (126)
- Correction in Birth/Death Certificate (122)
- Others (Birth-Death) (98)

### Property Tax-TAT(Title Transfer) (306)
Departments: Property Tax (301), Information Technology (3), Estate and Management (1), Building Permission (1)

- Title transfer (279)
- Correction in name according to official gazette (22)
- Property Tax NOC Related (5)

### PMC Hospitals treatment (282)
Departments: Health (279), Primary Education (1), Drainage (1), PMC Security (1)

- Related to PMC Hospital, Treatment and Staff (220)
- Others (Medical Unit) (62)

### Environment (H.O) (268)
Departments: Environment (165), Solid Waste Management (40), Building Permission (16), Tree Authority (9) …

- Other (ENV) (182)
- Water Hyacinth removal (86)

### Unauthorized banners / advertisements / Permit / license in Pune City (241)
Departments: License-Skysign (204), Building Permission (12), Encroachment (6), Environment (5) …

- Unauthorized banners / advertisements / Permit / license in Pune City (241)

### Traffic-Planning (235)
Departments: Chief Engineer Project (169), Road (43), Encroachment (12), Electrical (8) …

- Other (Traffic-Planning) (126)
- Regarding Pay and park on road (43)
- Parking policy (28)
- New P1 P2 zone required (24)
- Development of parking reservations (10)
- Require name for road and chowk (3)
- Regarding Mechanical Car parking (1)

### Garden Electric maintenance work (201)
Departments: Garden (120), Electrical (60), Tree Authority (12), Pune Smart City (PSCDCL) (3) …

- Repairing of Lights / Halogen in Garden (120)
- Others (Garden-Electrical) (81)

### Communicable Disease (163)
Departments: Health (92), Solid Waste Management (53), Drainage (9), Water Supply (3) …

- Diseases like Swine Flu, Dengue, Chikungunya etc (116)
- Others (Communicable Disease) (47)

### Electrical(H.O) (126)
Departments: Electrical (123), Drainage (2), Tree Authority (1)

- Electrical(H.O) (126)

### Primary Education (113)
Departments: Primary Education (107), Road (1), Drainage (1), Solid Waste Management (1) …

- Related to PMC / Private Schools (75)
- Others (Primary Education) (34)
- Official Complaints (4)

### Lashkar Water Supply (105)
Departments: Water Supply (102), Building Permission (1), Road (1), Drainage (1)

- NO water Supply (22)
- Low water pressure to Individual (16)
- Low pressure to entire area (15)
- Contamination / Turbid Water Problem (13)
- Others (Water Supply) (8)
- Pipeline/Valve Leakage of PMC line (7)
- No water as per time table (7)
- Water Flowing / wastage (6)
- Unauthorised tapping of water connection/Water Theft (3)
- Correction in water meter bill (Name/Address/Amount etc) (3)
- Unauthorised use of water from Residential to Commercial area (2)
- Motor / Pump on water line of pmc (2)
- Water meter not working (1)

### Sports (103)
Departments: Sports (67), Solid Waste Management (10), Electrical (8), Estate and Management (8) …

- other (Sports) (81)
- Sports Ground Cleaning (13)
- Availability of sports ground / complex (5)
- Facility in sports ground / complex (4)

### AutoDCR (90)
Departments: Property Tax (85), Building Permission (5)

- Complaints against AutoDCR Report (77)
- Other (City Engineer) (13)

### Property Tax-COMPUTER SECTION (64)
Departments: Property Tax (64)

- Online Payment Related (40)
- Property Tax Website issue (24)

### Unauthorized slaughterhouse / crude meat (64)
Departments: Health (42), Solid Waste Management (9), Encroachment (7), Building Permission (6)

- Illegal Slaughter House (45)
- Others (Khatik Vibhag) (18)
- Hygiene of meat (1)

### PMC Security Complaints (58)
Departments: PMC Security (58)

- Irresponsible behaviour of Security Guard (36)
- Deemand of Security Guard (22)

### Cultural Department (58)
Departments: Cultural Department (49), Heritage Cell (3), Electrical (2), Environment (1) …

- Other (Cultural Department Related) (35)
- Auditorium related complaints (23)

### Marriage Registration (50)
Departments: Unassigned (25), Information Technology (23), Marriage Registration (2)

- Other (Marriage Registration) (24)
- Marriage Certificate not received in time. (18)
- Correction in Marriage Certificate (8)

### Slum (49)
Departments: Slum (19), Solid Waste Management (13), Building Permission (6), Road (4) …

- Other (Slum) (49)

### Mandai (47)
Departments: Encroachment (33), Market (8), Solid Waste Management (3), Electrical (1) …

- Other (Mandai) (39)
- Complaint related to Mandai Stall / Gaala (7)
- Removal of encroachment around PMC Mandai premises (1)

### RTI Related Complaint (44)
Departments: Labour Office (35), Road (8), Building Permission (1)

- Others (43)
- Complaint realted to dues with PMC (1)

### Property Tax-SOLAR VERMI & RAINWATER HARVESTING (SVR) (33)
Departments: Property Tax (32), Road (1)

- Solar, Vermiculture, Rainwater harvesting discount (33)

### Vehicle department (28)
Departments: Vehicle Depot (21), Solid Waste Management (3), Encroachment (3), Road (1)

- Rash Driving of PMC vehicles (15)
- PMC Vehicle without number plate (8)
- Pollution due to PMC vehicle (5)

### Heritage Cell (Bhavan HO) (27)
Departments: Heritage Cell (19), Encroachment (5), Electrical (1), Road (1) …

- Cleanliness at Heritage places (18)
- Removal of Unauthorised vendors/stalls (5)
- Repairing and maintenance at Heritage places (4)

### Social Development Schemes (23)
Departments: Social Development (20), Estate and Management (2), Sports (1)

- Others (SDD) (13)
- Online Form Related Queries (7)
- Regarding various schemes (3)

### Pune Smart City (PSCDCL) (21)
Departments: Pune Smart City (PSCDCL) (8), Encroachment (6), Building Permission (2), Health (2) …

- Others - (PSCDCL) (9)
- Aundh, Baner, Balewadi Projects (8)
- Pan City Project (3)
- Wi-Fi related (1)

### Urban Poor Scheme (18)
Departments: Health (14), Garden (1), Building Permission (1), Chief Engineer Project (1) …

- Others Urban Poor Scheme (11)
- Regarding Medical Bill (7)

### TDR (18)
Departments: Building Permission (10), License-Skysign (5), Unassigned (2), Encroachment (1)

- Complaint against TDR Certificate Verification (6)
- other (TDR Cell) (6)
- Complaint against TDR/ Not received (2)
- TDR Purchase Application (2)
- TDR Certificate Verification (2)

### Property Tax-MOBILE TOWER (17)
Departments: Building Permission (8), Property Tax (7), License-Skysign (2)

- Mobile Tower Related (17)

### River Front development Project (11)
Departments: Chief Engineer Project (5), Drainage (3), Solid Waste Management (2), Health (1)

- River Front development Project (11)

### RCH / NUHM (7)
Departments: Drainage (2), Chief Engineer Project (1), Tree Authority (1), Health (1) …

- Others (RCH / NUHM) (7)

### Secondary and Technical Education (7)
Departments: Secondary & Technical Education (5), Primary Education (2)

- Others (Secondary Education) (6)
- Direct Benefit Transfer (DBT) - Others (1)

### Crematorium electrical work(H.O) (7)
Departments: Electrical (4), Labour Office (2), Solid Waste Management (1)

- Crematorium electrical work(H.O) (7)

### Land Acquisition (5)
Departments: Land Acquisition (3), Solid Waste Management (1), Road (1)

- Complaint Related to Land Acquisition (4)
- Other (Land Acquisition) (1)

### Bogus doctor / pregnancy diagnosis / unauthorized sonography center (4)
Departments: Health (4)

- Bogus Doctors (3)
- Others (PCPNDT) (1)

### Pradhan Mantri Awas Yojana (PMAY) (3)
Departments: Pradhanmantri Awas Yojana (PMAY) (2), Unassigned (1)

- Other (Pradhan Mantri Awas Yojana) (2)
- Complaint Regarding In-Situ (1)

### Medicine Supplies (3)
Departments: Health (3)

- Others (C.M.S.) (2)
- Medicines and equipments not available (1)

### Pension Complaints (3)
Departments: Unassigned (2), Pension (1)

- Delay in Pension processing (2)
- Others (1)

### Immunization (3)
Departments: Health (3)

- Related to Vaccination (Polio, Rubella etc) (2)
- Others (Immunization) (1)

### STP(Electrical) (3)
Departments: Electrical (3)

- STP Electrical work (3)

### Bicycle Plan (2)
Departments: Road (1), Chief Engineer Project (1)

- Bicycle Plan (2)

### Information Technology-Employee (2)
Departments: Information Technology (2)

- Computer / Printer / Scanner Deemand (2)

### Aids Control (1)
Departments: Health (1)

- Others (Aids Control) (1)

### City Family Welfare (1)
Departments: Solid Waste Management (1)

- Others (City Family Welfare) (1)

### National Programms (1)
Departments: Health (1)

- Others (National Programms) (1)

### Contributed Health Scheme (1)
Departments: Health (1)

- Others (1)

### Chawl Complaints (1)
Departments: Chawl (1)

- Action against illegal residents (1)

### BSUP project (1)
Departments: Building Permission (1)

- BSUP project (1)

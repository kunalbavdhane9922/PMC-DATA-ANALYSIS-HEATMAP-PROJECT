# Missing / Null Values Report

Source: `_WITH_params_AS_SELECT_DATE_2025_07_01_...csv` — 161,872 rows, 23 columns.

## 1. Empty values by column

| Column | Empty | % | Notes |
|---|---:|---:|---|
| Peth | 160,356 | 99.1 | Effectively unused |
| Pending days | 145,672 | 90.0 | Only filled for some open complaints |
| Rating | 118,258 | 73.1 | Citizen rating optional |
| Feedback | 116,021 | 71.7 | 74 are whitespace-only |
| Prabhag | 47,297 | 29.2 | |
| Complaint close date | 31,769 | 19.6 | |
| Officer Remark | 18,122 | 11.2 | 1,063 whitespace-only |
| Officer Mobile No | 12,263 | 7.6 | |
| Ward Name | 7,087 | 4.4 | All also have blank Prabhag |
| Complaint Location | 5,139 | 3.2 | 1 whitespace-only |
| Officer Details | 520 | 0.3 | |
| Last Action | 519 | 0.3 | Same 519 rows as Assigned Date / Last Action Date |
| Assigned Date | 519 | 0.3 | |
| Last Action Date | 519 | 0.3 | |

No blanks in: Sr. No., Token No, Complaint Date, Media, Expected Complaint Date, Complaint Type, Department Name, Sub Category, Complaint Description.

## 2. Fake-null placeholders (look filled, but are not)

| Column | Value | Count |
|---|---|---:|
| Officer Remark | `.` | 2,361 |
| Officer Remark | `-` / `--` / `NA` | 105 |
| Complaint Location | `null` / `NA` / `.` | 21 |
| Feedback | `0` / `.` | 9 |
| Complaint Description | `.` / `NA` | 8 |
| Department Name | `Unassigned` | 30 |

## 3. Logical inconsistencies

| Issue | Rows |
|---|---:|
| Status = Rejected but no close date | 14,823 (all rejected rows) |
| Blank Ward AND blank Prabhag | 7,087 |
| Feedback text present but no rating | 2,304 |
| Open status (Received/On Hold/etc.) but no Pending days | 1,692 |
| Resolved but no/blank officer remark | 1,063 |
| Officer mobile not a valid 10-digit number | 936 |
| Rating present but no close date | 329 |
| Rating present but no feedback text | 67 |
| Resolved but no close date | 1 |
| Resolved but has Pending days | 1 |

## 4. Observations

- The 519 rows with no Last Action also have no Assigned Date and no Last Action Date: complaints that were never assigned.
- Close date is empty for every Rejected row, so "closed" and "resolved" can't be measured by close date alone. Use Last Action Date for rejected rows.
- Blank Ward rows (7,087) have no Prabhag either, so their location can't be recovered from those columns. Complaint Location text may help.
- Peth is unusable and can be dropped from the Power BI model.

## 5. Suggested handling

- Treat `.`, `-`, `--`, `NA`, `null` and whitespace-only values as null.
- Map blank Ward Name to "Unknown", not to Head Office.
- Add flags: `is_rejected`, `is_open`, `has_rating`.
- Compute resolution days from Last Action Date, not from the sparse Pending days.

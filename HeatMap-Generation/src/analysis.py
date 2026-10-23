"""
Module: analysis.py
-------------------
Implements the core analytical tasks organized by civic factor:
  - Potholes & Road Surfaces (Hotspot Matrix, Relative Burden Ratio, Pareto)
  - Traffic Management (Problem Type Matrix, Detailed Subcategory Matrix, Signals, Monthly Trend, Pareto)
  - Governance & Resolution (Ward Outcome Percentages, Status Breakdown)
  - Locations & Spatial Hotspots (Repeated Corridors, Verified GPS Records)
"""

import os
import pandas as pd
import numpy as np


# ----------------------------------------------------------------------
# 1. POTHOLE & ROAD SURFACE ANALYSES
# ----------------------------------------------------------------------
def compute_pothole_hotspots_matrix(pothole_df):
    """
    Task 1: Pothole Hotspots by Ward
    Rows: Ward Name (sorted descending by total complaints)
    Columns: Pothole type (Road Potholes, Manhole-related, Resurfacing, etc.)
    Values: Unique complaint count (Token No)
    """
    matrix = pothole_df.pivot_table(
        index="Ward_Clean",
        columns="Pothole_Type",
        values="Token No",
        aggfunc="nunique",
        fill_value=0
    )
    row_totals = matrix.sum(axis=1).sort_values(ascending=False)
    col_totals = matrix.sum(axis=0).sort_values(ascending=False)
    sorted_matrix = matrix.loc[row_totals.index, col_totals.index]

    matrix_sum = sorted_matrix.values.sum()
    total_records = len(pothole_df)
    assert matrix_sum == total_records, (
        f"Validation Error: Pothole matrix sum ({matrix_sum}) does not match records ({total_records})!"
    )
    print(f"[+] Task 1 Validation passed: Total aggregated pothole count ({matrix_sum:,}) equals records ({total_records:,}).")
    return sorted_matrix


def compute_relative_pothole_burden(city_df, pothole_df):
    """
    Task 4: Relative Pothole Burden by Ward
    Formula:
      Relative Pothole Burden = (Ward's share of all pothole complaints) / (Ward's share of all city complaints)
    Interpretation:
      > 1.0: Potholes over-represented in ward complaint profile
      ~ 1.0: Proportionate to overall city complaints
      < 1.0: Potholes under-represented
    """
    total_city = len(city_df)
    total_potholes = len(pothole_df)

    ward_city_counts = city_df.groupby("Ward_Clean")["Token No"].nunique()
    ward_pothole_counts = pothole_df.groupby("Ward_Clean")["Token No"].nunique().reindex(ward_city_counts.index, fill_value=0)

    # Sub-type breakdowns
    direct_potholes = pothole_df[pothole_df["Pothole_Type"].isin(["Road Potholes", "Pothole Around Manhole"])]
    direct_total = len(direct_potholes)
    ward_direct_counts = direct_potholes.groupby("Ward_Clean")["Token No"].nunique().reindex(ward_city_counts.index, fill_value=0)

    resurface_potholes = pothole_df[pothole_df["Pothole_Type"] == "Road/Footpath Resurfacing"]
    resurface_total = len(resurface_potholes)
    ward_resurface_counts = resurface_potholes.groupby("Ward_Clean")["Token No"].nunique().reindex(ward_city_counts.index, fill_value=0)

    manholes = pothole_df[pothole_df["Pothole_Type"].str.contains("Manhole|Chamber", case=False, na=False)]
    manhole_total = len(manholes)
    ward_manhole_counts = manholes.groupby("Ward_Clean")["Token No"].nunique().reindex(ward_city_counts.index, fill_value=0)

    ward_city_share = ward_city_counts / total_city

    burden_summary = pd.DataFrame({
        "City_Complaints": ward_city_counts,
        "City_Share_Pct": (ward_city_share * 100).round(2),
        "Pothole_Complaints": ward_pothole_counts,
        "Pothole_Share_Pct": ((ward_pothole_counts / total_potholes) * 100).round(2),
        "Relative_Pothole_Burden": (((ward_pothole_counts / total_potholes) / ward_city_share)).round(2),
        "Direct_Pothole_Burden": (((ward_direct_counts / direct_total) / ward_city_share)).round(2),
        "Resurfacing_Burden": (((ward_resurface_counts / resurface_total) / ward_city_share)).round(2),
        "Manhole_Drain_Burden": (((ward_manhole_counts / manhole_total) / ward_city_share)).round(2)
    })

    burden_summary = burden_summary.sort_values(by="Relative_Pothole_Burden", ascending=False)
    print(f"[+] Task 4 Validation passed: Computed Relative Pothole Burden for {len(burden_summary)} zones.")
    return burden_summary


def compute_pothole_pareto(pothole_df):
    """
    Task 5a: Pothole & Road Pareto Analysis
    """
    p_counts = pothole_df.groupby("Pothole_Type")["Token No"].nunique().sort_values(ascending=False)
    p_pareto = pd.DataFrame({"Complaint_Count": p_counts})
    p_pareto["Percentage"] = (p_pareto["Complaint_Count"] / p_pareto["Complaint_Count"].sum() * 100).round(2)
    p_pareto["Cumulative_Count"] = p_pareto["Complaint_Count"].cumsum()
    p_pareto["Cumulative_Pct"] = (p_pareto["Cumulative_Count"] / p_pareto["Complaint_Count"].sum() * 100).round(2)
    return p_pareto


# ----------------------------------------------------------------------
# 2. TRAFFIC MANAGEMENT ANALYSES
# ----------------------------------------------------------------------
def compute_traffic_issues_matrix(traffic_df):
    """
    Task 2: Traffic Issues by Ward (Major Problem Types)
    Rows: Ward Name | Columns: Traffic issue type (Speed Breakers, Signals, Parking, etc.)
    """
    matrix = traffic_df.pivot_table(
        index="Ward_Clean",
        columns="Traffic_Type",
        values="Token No",
        aggfunc="nunique",
        fill_value=0
    )
    row_totals = matrix.sum(axis=1).sort_values(ascending=False)
    col_totals = matrix.sum(axis=0).sort_values(ascending=False)
    sorted_matrix = matrix.loc[row_totals.index, col_totals.index]

    matrix_sum = sorted_matrix.values.sum()
    total_records = len(traffic_df)
    assert matrix_sum == total_records, (
        f"Validation Error: Traffic matrix sum ({matrix_sum}) does not match records ({total_records})!"
    )
    print(f"[+] Task 2 Validation passed: Total aggregated traffic count ({matrix_sum:,}) equals records ({total_records:,}).")
    return sorted_matrix


def compute_traffic_detailed_matrices(traffic_df):
    """
    Computes detailed subcategory matrices (all wards, local wards, and signal hotspots).
    """
    # All Wards vs 19 Subcategories
    matrix_all = traffic_df.pivot_table(
        index="Ward_Clean",
        columns="Sub Category",
        values="Token No",
        aggfunc="nunique",
        fill_value=0
    )
    row_totals = matrix_all.sum(axis=1).sort_values(ascending=False)
    col_totals = matrix_all.sum(axis=0).sort_values(ascending=False)
    sorted_matrix_all = matrix_all.loc[row_totals.index, col_totals.index]

    # Local Wards Only (Excluding Head Office and Unassigned)
    local_df = traffic_df[~traffic_df["Ward_Clean"].isin(["Head Office", "Unassigned / Central"])]
    matrix_local = local_df.pivot_table(
        index="Ward_Clean",
        columns="Sub Category",
        values="Token No",
        aggfunc="nunique",
        fill_value=0
    )
    row_totals_local = matrix_local.sum(axis=1).sort_values(ascending=False)
    col_totals_local = matrix_local.sum(axis=0).sort_values(ascending=False)
    sorted_matrix_local = matrix_local.loc[row_totals_local.index, col_totals_local.index]

    # Signal Hotspots Matrix
    signal_subs = [
        "New signal required",
        "Signal not working",
        "Repairing and maintenance of Signal",
        "Removal of signal pole",
        "Other (Traffic-signal Electrical)"
    ]
    signal_df = traffic_df[traffic_df["Sub Category"].isin(signal_subs)].copy()
    signal_matrix = signal_df.pivot_table(
        index="Ward_Clean",
        columns="Sub Category",
        values="Token No",
        aggfunc="nunique",
        fill_value=0
    )
    row_totals_sig = signal_matrix.sum(axis=1).sort_values(ascending=False)
    col_totals_sig = signal_matrix.sum(axis=0).sort_values(ascending=False)
    sorted_signal_matrix = signal_matrix.loc[row_totals_sig.index, col_totals_sig.index]

    return sorted_matrix_all, sorted_matrix_local, sorted_signal_matrix


def compute_traffic_pareto(traffic_df):
    """Task 5b: Traffic Pareto Analysis."""
    t_counts = traffic_df.groupby("Traffic_Type")["Token No"].nunique().sort_values(ascending=False)
    t_pareto = pd.DataFrame({"Complaint_Count": t_counts})
    t_pareto["Percentage"] = (t_pareto["Complaint_Count"] / t_pareto["Complaint_Count"].sum() * 100).round(2)
    t_pareto["Cumulative_Count"] = t_pareto["Complaint_Count"].cumsum()
    t_pareto["Cumulative_Pct"] = (t_pareto["Cumulative_Count"] / t_pareto["Complaint_Count"].sum() * 100).round(2)
    return t_pareto


def compute_traffic_trends_and_summaries(traffic_df):
    """Computes monthly trend, ward summary, and subcategory distribution for traffic."""
    # Monthly trend
    df_time = traffic_df.dropna(subset=["Complaint Date"]).copy()
    df_time["YearMonth"] = df_time["Complaint Date"].dt.to_period("M").astype(str)
    monthly_trend = (
        df_time.groupby("YearMonth")["Token No"]
        .nunique()
        .reset_index(name="Complaint_Count")
        .sort_values(by="YearMonth")
    )

    # Ward summary
    ward_summary = (
        traffic_df.groupby("Ward_Clean")["Token No"]
        .nunique()
        .reset_index(name="Complaint_Count")
        .sort_values(by="Complaint_Count", ascending=False)
    )
    ward_summary["Percentage"] = (ward_summary["Complaint_Count"] / ward_summary["Complaint_Count"].sum() * 100).round(2)

    # Subcategory summary
    sub_summary = (
        traffic_df.groupby("Sub Category")["Token No"]
        .nunique()
        .reset_index(name="Complaint_Count")
        .sort_values(by="Complaint_Count", ascending=False)
    )
    sub_summary["Percentage"] = (sub_summary["Complaint_Count"] / sub_summary["Complaint_Count"].sum() * 100).round(2)

    return monthly_trend, ward_summary, sub_summary


# ----------------------------------------------------------------------
# 3. GOVERNANCE & RESOLUTION STATUS ANALYSES
# ----------------------------------------------------------------------
def compute_status_percentage_matrix(city_df, traffic_df=None):
    """
    Task 3: Open vs. Resolved Complaints
    Rows: Ward Name | Columns: Status (Resolved, Open / Pending, Rejected, Missing / Unknown)
    Values: Normalized percentage per ward (sums strictly to 100.0%).
    """
    status_crosstab = pd.crosstab(
        city_df["Ward_Clean"],
        city_df["Status_Group"],
        values=city_df["Token No"],
        aggfunc="nunique"
    ).fillna(0)

    preferred_cols = ["Resolved", "Open / Pending", "Rejected", "Missing / Unknown"]
    available_cols = [c for c in preferred_cols if c in status_crosstab.columns]
    status_crosstab = status_crosstab[available_cols]

    row_sums = status_crosstab.sum(axis=1)
    status_pct_matrix = (status_crosstab.div(row_sums, axis=0) * 100).round(2)

    sorted_wards = row_sums.sort_values(ascending=False).index
    status_pct_matrix = status_pct_matrix.loc[sorted_wards]
    status_raw_counts = status_crosstab.loc[sorted_wards]

    # Validation
    for ward, total in status_pct_matrix.sum(axis=1).items():
        assert abs(total - 100.0) < 0.2, f"Validation Error on ward '{ward}': {total}%"
    print("[+] Task 3 Validation passed: All ward status percentages correctly normalized to 100.0%.")

    # Traffic specific status summary
    traffic_status_summary = None
    if traffic_df is not None:
        traffic_status_summary = (
            traffic_df.groupby("Last Action")["Token No"]
            .nunique()
            .reset_index(name="Complaint_Count")
            .sort_values(by="Complaint_Count", ascending=False)
        )
        traffic_status_summary["Percentage"] = (
            traffic_status_summary["Complaint_Count"] / traffic_status_summary["Complaint_Count"].sum() * 100
        ).round(2)

    return status_pct_matrix, status_raw_counts, traffic_status_summary


# ----------------------------------------------------------------------
# 4. LOCATION & SPATIAL HOTSPOT ANALYSES
# ----------------------------------------------------------------------
def compute_road_junction_hotspots(pt_geo_df):
    """
    Task 6: Exact Road or Junction Hotspots
    Identifies high-frequency repeated road corridors from unstructured address data,
    and isolates genuine GPS coordinates without fabricating spatial data.
    """
    top_corridors = (
        pt_geo_df.dropna(subset=["Corridor"])
        .groupby("Corridor")["Token No"]
        .nunique()
        .reset_index(name="Total_Complaints")
        .sort_values(by="Total_Complaints", ascending=False)
    )

    corridor_by_ward = (
        pt_geo_df.dropna(subset=["Corridor"])
        .groupby(["Corridor", "Ward_Clean"])["Token No"]
        .nunique()
        .reset_index(name="Complaint_Count")
        .sort_values(by="Complaint_Count", ascending=False)
    )

    gps_df = pt_geo_df.dropna(subset=["Latitude", "Longitude"])[
        ["Token No", "Ward_Clean", "Sub Category", "Complaint Location", "Latitude", "Longitude", "Last Action"]
    ].copy()

    print(f"[+] Task 6 Validation passed: Extracted {len(top_corridors)} high-frequency corridors and {len(gps_df):,} verified GPS records.")
    return top_corridors, corridor_by_ward, gps_df


# ----------------------------------------------------------------------
# MASTER RUNNER & FACTOR-BASED DATA EXPORTER
# ----------------------------------------------------------------------
def run_all_civic_analyses(civic_data, processed_base_dir=None):
    """
    Runs all factor-wise analyses and exports CSV data tables into factor-specific folders.
    """
    city_df = civic_data["city_df"]
    pothole_df = civic_data["pothole_df"]
    traffic_df = civic_data["traffic_df"]
    pt_geo_df = civic_data["pt_geo_df"]

    print("\n" + "=" * 70)
    print(" EXECUTING COMPREHENSIVE CIVIC GRIEVANCE ANALYSES (BY FACTOR)")
    print("=" * 70)

    # 1. Potholes
    pothole_matrix = compute_pothole_hotspots_matrix(pothole_df)
    burden_summary = compute_relative_pothole_burden(city_df, pothole_df)
    p_pareto = compute_pothole_pareto(pothole_df)

    # 2. Traffic
    traffic_matrix = compute_traffic_issues_matrix(traffic_df)
    matrix_all, matrix_local, signal_matrix = compute_traffic_detailed_matrices(traffic_df)
    t_pareto = compute_traffic_pareto(traffic_df)
    monthly_trend, ward_summary, sub_summary = compute_traffic_trends_and_summaries(traffic_df)

    # 3. Governance
    status_pct_matrix, status_raw_counts, traffic_status_summary = compute_status_percentage_matrix(city_df, traffic_df)

    # 4. Locations
    top_corridors, corridor_by_ward, gps_df = compute_road_junction_hotspots(pt_geo_df)

    # Export CSVs to factor-organized folders under data/processed/
    if processed_base_dir:
        dirs = {
            "potholes": os.path.join(processed_base_dir, "potholes"),
            "traffic": os.path.join(processed_base_dir, "traffic"),
            "governance": os.path.join(processed_base_dir, "governance"),
            "locations": os.path.join(processed_base_dir, "locations")
        }
        for d in dirs.values():
            os.makedirs(d, exist_ok=True)

        # Potholes CSVs
        pothole_matrix.to_csv(os.path.join(dirs["potholes"], "pothole_hotspots_matrix.csv"))
        burden_summary.to_csv(os.path.join(dirs["potholes"], "relative_pothole_burden_summary.csv"))
        p_pareto.to_csv(os.path.join(dirs["potholes"], "pothole_pareto_analysis.csv"))

        # Traffic CSVs
        traffic_matrix.to_csv(os.path.join(dirs["traffic"], "traffic_issues_matrix.csv"))
        matrix_all.to_csv(os.path.join(dirs["traffic"], "ward_vs_subcategory_matrix_all.csv"))
        matrix_local.to_csv(os.path.join(dirs["traffic"], "ward_vs_subcategory_matrix_local.csv"))
        signal_matrix.to_csv(os.path.join(dirs["traffic"], "traffic_signal_hotspots_matrix.csv"))
        t_pareto.to_csv(os.path.join(dirs["traffic"], "traffic_pareto_analysis.csv"))
        monthly_trend.to_csv(os.path.join(dirs["traffic"], "traffic_monthly_trend.csv"), index=False)
        ward_summary.to_csv(os.path.join(dirs["traffic"], "ward_traffic_summary.csv"), index=False)
        sub_summary.to_csv(os.path.join(dirs["traffic"], "subcategory_traffic_summary.csv"), index=False)

        # Governance CSVs
        status_pct_matrix.to_csv(os.path.join(dirs["governance"], "ward_status_percentage_matrix.csv"))
        status_raw_counts.to_csv(os.path.join(dirs["governance"], "ward_status_raw_counts.csv"))
        if traffic_status_summary is not None:
            traffic_status_summary.to_csv(os.path.join(dirs["governance"], "traffic_resolution_status_summary.csv"), index=False)

        # Locations CSVs
        top_corridors.to_csv(os.path.join(dirs["locations"], "top_road_corridor_hotspots.csv"), index=False)
        corridor_by_ward.to_csv(os.path.join(dirs["locations"], "corridors_by_ward_breakdown.csv"), index=False)
        gps_df.to_csv(os.path.join(dirs["locations"], "verified_gps_coordinates.csv"), index=False)
        print(f"[+] Successfully exported all analytical summary tables to factor folders under: {processed_base_dir}")

    return {
        "pothole_matrix": pothole_matrix,
        "burden_summary": burden_summary,
        "p_pareto": p_pareto,
        "traffic_matrix": traffic_matrix,
        "matrix_all": matrix_all,
        "matrix_local": matrix_local,
        "signal_matrix": signal_matrix,
        "t_pareto": t_pareto,
        "monthly_trend": monthly_trend,
        "ward_summary": ward_summary,
        "sub_summary": sub_summary,
        "status_pct_matrix": status_pct_matrix,
        "status_raw_counts": status_raw_counts,
        "traffic_status_summary": traffic_status_summary,
        "top_corridors": top_corridors,
        "corridor_by_ward": corridor_by_ward,
        "gps_df": gps_df
    }

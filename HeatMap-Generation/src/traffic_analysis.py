"""
Module: traffic_analysis.py
---------------------------
Computes aggregated statistics, pivot tables, ward-wise distributions,
temporal trends, and resolution status for traffic complaints.
"""

import os
import pandas as pd


def compute_ward_summary(traffic_df):
    """Calculates total traffic complaints by ward using unique Token No count."""
    ward_counts = (
        traffic_df.groupby("Ward_Clean")["Token No"]
        .nunique()
        .reset_index(name="Complaint_Count")
        .sort_values(by="Complaint_Count", ascending=False)
    )
    ward_counts["Percentage"] = (
        ward_counts["Complaint_Count"] / ward_counts["Complaint_Count"].sum() * 100
    ).round(2)
    return ward_counts


def compute_subcategory_summary(traffic_df):
    """Calculates total complaints by traffic subcategory."""
    sub_counts = (
        traffic_df.groupby("Sub Category")["Token No"]
        .nunique()
        .reset_index(name="Complaint_Count")
        .sort_values(by="Complaint_Count", ascending=False)
    )
    sub_counts["Percentage"] = (
        sub_counts["Complaint_Count"] / sub_counts["Complaint_Count"].sum() * 100
    ).round(2)
    return sub_counts


def compute_ward_subcategory_matrix(traffic_df, exclude_head_office=False):
    """
    Constructs the primary pivot matrix:
      - Rows: Ward Name (sorted descending by total complaints)
      - Columns: Sub Category (sorted descending by total complaints)
      - Values: Number of complaints (unique Token No count)
    
    Validates that matrix sum strictly matches record count.
    """
    df_pivot = traffic_df.copy()
    if exclude_head_office:
        df_pivot = df_pivot[~df_pivot["Ward_Clean"].isin(["Head Office", "Unassigned / Central"])]

    # Pivot table with unique Token No counting
    matrix = df_pivot.pivot_table(
        index="Ward_Clean",
        columns="Sub Category",
        values="Token No",
        aggfunc="nunique",
        fill_value=0
    )

    # Sort rows and columns by total counts descending
    row_totals = matrix.sum(axis=1).sort_values(ascending=False)
    col_totals = matrix.sum(axis=0).sort_values(ascending=False)
    sorted_matrix = matrix.loc[row_totals.index, col_totals.index]

    # Integrity validation check
    matrix_sum = sorted_matrix.values.sum()
    subset_records = len(df_pivot)
    assert matrix_sum == subset_records, (
        f"Validation Error: Matrix sum ({matrix_sum}) does not match subset records ({subset_records})!"
    )
    print(f"[+] Matrix validation passed: Total aggregated count ({matrix_sum:,}) equals dataset records ({subset_records:,}).")

    return sorted_matrix


def compute_signal_hotspots(traffic_df):
    """
    Filters specifically for traffic signal infrastructure complaints:
    New signal, Signal not working, Repair/maintenance, Pole removal, Signal electrical.
    """
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
    # Sort
    row_totals = signal_matrix.sum(axis=1).sort_values(ascending=False)
    col_totals = signal_matrix.sum(axis=0).sort_values(ascending=False)
    return signal_matrix.loc[row_totals.index, col_totals.index], signal_df


def compute_time_trends(traffic_df):
    """Calculates monthly traffic complaint volume over the entire observation window."""
    df_time = traffic_df.dropna(subset=["Complaint Date"]).copy()
    df_time["YearMonth"] = df_time["Complaint Date"].dt.to_period("M").astype(str)
    
    monthly_trend = (
        df_time.groupby("YearMonth")["Token No"]
        .nunique()
        .reset_index(name="Complaint_Count")
        .sort_values(by="YearMonth")
    )
    return monthly_trend


def compute_resolution_status(traffic_df):
    """Analyzes status of traffic complaints (Resolved vs. Pending/Rejected)."""
    status_summary = (
        traffic_df.groupby("Last Action")["Token No"]
        .nunique()
        .reset_index(name="Complaint_Count")
        .sort_values(by="Complaint_Count", ascending=False)
    )
    status_summary["Percentage"] = (
        status_summary["Complaint_Count"] / status_summary["Complaint_Count"].sum() * 100
    ).round(2)

    # Calculate pending days metrics for unresolved cases
    unresolved = traffic_df[traffic_df["Last Action"] != "Resolved"]
    pending_stats = {
        "Total_Unresolved": len(unresolved),
        "Recorded_Pending_Days_Count": unresolved["Pending days"].notnull().sum(),
        "Mean_Pending_Days": unresolved["Pending days"].mean(),
        "Median_Pending_Days": unresolved["Pending days"].median(),
        "Max_Pending_Days": unresolved["Pending days"].max()
    }
    return status_summary, pending_stats


def run_all_analyses(traffic_df, output_dir=None):
    """Runs all analyses and exports summary CSV tables."""
    print("\n" + "=" * 70)
    print(" STEP 2: TRAFFIC COMPLAINT STATISTICAL ANALYSIS")
    print("=" * 70)

    ward_summary = compute_ward_summary(traffic_df)
    sub_summary = compute_subcategory_summary(traffic_df)
    matrix_all = compute_ward_subcategory_matrix(traffic_df, exclude_head_office=False)
    matrix_local = compute_ward_subcategory_matrix(traffic_df, exclude_head_office=True)
    signal_matrix, signal_df = compute_signal_hotspots(traffic_df)
    monthly_trend = compute_time_trends(traffic_df)
    status_summary, pending_stats = compute_resolution_status(traffic_df)

    if output_dir:
        os.makedirs(output_dir, exist_ok=True)
        ward_summary.to_csv(os.path.join(output_dir, "ward_traffic_summary.csv"), index=False)
        sub_summary.to_csv(os.path.join(output_dir, "subcategory_traffic_summary.csv"), index=False)
        matrix_all.to_csv(os.path.join(output_dir, "ward_vs_subcategory_matrix_all.csv"))
        matrix_local.to_csv(os.path.join(output_dir, "ward_vs_subcategory_matrix_local.csv"))
        signal_matrix.to_csv(os.path.join(output_dir, "traffic_signal_hotspots_matrix.csv"))
        monthly_trend.to_csv(os.path.join(output_dir, "traffic_monthly_trend.csv"), index=False)
        status_summary.to_csv(os.path.join(output_dir, "traffic_resolution_status_summary.csv"), index=False)
        print(f"[+] Exported 7 analytical CSV summary tables to: {output_dir}")

    return {
        "ward_summary": ward_summary,
        "sub_summary": sub_summary,
        "matrix_all": matrix_all,
        "matrix_local": matrix_local,
        "signal_matrix": signal_matrix,
        "signal_df": signal_df,
        "monthly_trend": monthly_trend,
        "status_summary": status_summary,
        "pending_stats": pending_stats
    }

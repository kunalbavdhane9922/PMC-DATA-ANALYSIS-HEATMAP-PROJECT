"""
Module: load_data.py
-------------------
Handles loading of PMC grievance dataset files (CSV or Excel) safely
without altering original data.
"""

import os
import pandas as pd


def resolve_dataset_path(provided_path=None):
    """
    Finds and resolves the PMC grievance dataset path.
    Prioritizes provided path (with or without extension), then checks standard workspace locations.
    """
    candidates = []
    if provided_path:
        candidates.extend([
            provided_path,
            f"{provided_path}.csv",
            f"{provided_path}.csv.gz",
            f"{provided_path}.gz",
        ])

    # Relative to script location and current directory
    script_dir = os.path.dirname(os.path.abspath(__file__))
    search_roots = [
        os.path.join(script_dir, "..", ".."),  # GitSync root
        os.path.join(script_dir, ".."),        # HeatMap-Generation root
        os.getcwd(),                           # Current working directory
    ]
    standard_names = [
        "Working_dataset.csv",
        "Working_dataset.csv.gz",
        "Working_dataset",
        "Original Dataset.csv.gz",
        "Original_Data.csv",
        "ExcelWorkbook1.xlsx",
    ]

    for root in search_roots:
        for name in standard_names:
            candidates.append(os.path.join(root, "Dataset", name))
            candidates.append(os.path.join(root, "data", "original", name))
            candidates.append(os.path.join(root, name))

    for p in candidates:
        abs_p = os.path.abspath(p)
        if os.path.isfile(abs_p):
            return abs_p

    raise FileNotFoundError(
        f"Could not locate dataset file. Searched candidates: {candidates}"
    )


def load_dataset(file_path=None, nrows=None):
    """
    Loads dataset from CSV, compressed CSV (.csv.gz, .gz), or Excel file.
    
    Parameters:
        file_path (str, optional): Path to dataset file (CSV/GZ/Excel).
        nrows (int, optional): Number of rows to read for quick sampling.
        
    Returns:
        pd.DataFrame: Loaded raw dataset.
    """
    path = resolve_dataset_path(file_path)
    print(f"[*] Loading raw dataset from: {path}")

    lower_path = path.lower()
    if lower_path.endswith(".csv") or lower_path.endswith(".csv.gz") or lower_path.endswith(".gz"):
        df = pd.read_csv(path, nrows=nrows, low_memory=False)
    elif lower_path.endswith(".xlsx") or lower_path.endswith(".xls"):
        df = pd.read_excel(path, nrows=nrows)
    else:
        raise ValueError(f"Unsupported file format: {os.path.splitext(path)[1]} for file {path}")

    print(f"[+] Successfully loaded {len(df):,} records with {len(df.columns)} columns.")
    mem_mb = df.memory_usage(deep=True).sum() / (1024 * 1024)
    print(f"[+] Memory usage: {mem_mb:.2f} MB")
    return df

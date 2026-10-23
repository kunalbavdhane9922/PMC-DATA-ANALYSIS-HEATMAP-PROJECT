"""
Module: clean_data.py
--------------------
Handles standardization, datetime parsing, duplicate validation,
categorical mapping for Pothole and Traffic analysis, status categorization,
and GPS / Road name extraction from complaint location records.
"""

import os
import re
import pandas as pd


# 1. Pothole and Manhole Categorical Mapping
POTHOLE_MAPPING = {
    "Repairing potholes on Road": "Road Potholes",
    "Repairing potholes on Road (HO)": "Road Potholes",
    "Repairing pothole around manhole": "Pothole Around Manhole",
    "Repairing pothole around manhole (HO)": "Pothole Around Manhole",
    "Repair/re-sufacing of roads/footpaths": "Road/Footpath Resurfacing",
    "Repair/re-sufacing of roads/footpaths (HO)": "Road/Footpath Resurfacing",
    "Providing / repairing of storm water chamber and cover": "Chamber Cover & Frame",
    "Providing / repairing of storm water chamber and cover (HO)": "Chamber Cover & Frame",
    "Replacement of missing/damaged manholes/inspection": "Missing/Damaged Manhole",
    "Replacement of missing/damaged manholes/inspection (HO)": "Missing/Damaged Manhole",
    "Raising of manhole (except in monsoon)": "Manhole Raising",
    "Raising of manhole(except in monsoon)": "Manhole Raising",
    "Cleaning / Overflowing choked drains or manholes": "Choked Drain/Overflowing Manhole",
    "Cleaning / Overflowing choked drains or manholes (HO)": "Choked Drain/Overflowing Manhole",
    "Cleaning of strom water chamber and nalla": "Chamber & Nalla Cleaning",
    "Cleaning of strom water chamber and line(H.O)": "Chamber & Nalla Cleaning",
    "Stopping chamber overflow (HO)": "Chamber Overflow (HO)"
}

# 2. Traffic Issue Categorical Mapping
TRAFFIC_MAPPING = {
    # Speed Breakers
    "Making/Repairing/Removal Speedbreaker": "Speed Breakers",
    "Making/Repairing/Removal Speedbreaker (HO)": "Speed Breakers",
    
    # Traffic Signals
    "New signal required": "Traffic Signals",
    "Signal not working": "Traffic Signals",
    "Repairing and maintenance of Signal": "Traffic Signals",
    "Removal of signal pole": "Traffic Signals",
    "Other (Traffic-signal Electrical)": "Traffic Signals",
    "Stop line at Signal before Zebra Crossing": "Traffic Signals",
    
    # Parking
    "PMC Parking Related Complaint": "Parking Regulations",
    "Marking of Parking Line": "Parking Regulations",
    "Marking of Parking Line (HO)": "Parking Regulations",
    "Regarding Pay and park on road": "Parking Regulations",
    "Parking policy": "Parking Regulations",
    "New P1 P2 zone required": "Parking Regulations",
    "Development of parking reservations": "Parking Regulations",
    "Regarding Mechanical Car parking": "Parking Regulations",
    
    # Zebra Crossings
    "About New / Old Zebra Crossing": "Zebra Crossings",
    
    # Planning & Chowk
    "Require name for road and chowk": "Traffic Planning & Chowk",
    "Other (Traffic-Planning)": "Traffic Planning & Chowk"
}

# 3. Known Pune Arterial Corridors & Major Chowks for Extraction
KNOWN_CORRIDORS = [
    ("Nagar Road", r"nagar\s*road|ahmednagar\s*road"),
    ("Sinhgad Road", r"sinh[a]?g[a]?d\s*road|sinh[a]?g[a]?d\s*rd"),
    ("Baner Road", r"baner\s*road|baner\s*rd"),
    ("Paud Road", r"paud\s*road|paud\s*rd"),
    ("Katraj Kondhwa Road", r"katraj\s*kondhwa\s*road|kondhwa\s*katraj\s*road"),
    ("Porwal Road", r"porwal\s*road|dhanori\s*road"),
    ("Pashan Sus Road", r"pashan\s*sus\s*road|pashan\s*sus\s*rd|sus\s*road"),
    ("Kharadi Road", r"kharadi\s*road|kharadi\s*bypass"),
    ("Prabhat Road", r"prabhat\s*road|prabhat\s*rd"),
    ("Pune Solapur Road", r"pune\s*solapur\s*road|solapur\s*road|solapur\s*highway"),
    ("DP Road", r"d[\.\s]*p[\.\s]*road"),
    ("Jambhulwadi Road", r"jambhulwadi\s*road"),
    ("Manjari Road", r"manjari\s*road"),
    ("Handewadi Road", r"handewadi\s*road"),
    ("Karve Road", r"karve\s*road|karve\s*rd"),
    ("Pune Satara Road", r"pune\s*satara\s*road|satara\s*road"),
    ("Lulla Nagar Chowk", r"lulla\s*nagar"),
    ("Aundh Road", r"aundh\s*road|aundh\s*rd"),
    ("Swargate Chowk", r"swargate"),
    ("JM Road", r"j[\.\s]*m[\.\s]*road|jangali\s*maharaj\s*road"),
    ("Mundhwa Road", r"mundhwa\s*road"),
    ("Airport Road", r"airport\s*road|viman\s*nagar\s*road"),
    ("FC Road", r"f[\.\s]*c[\.\s]*road|fergusson\s*college\s*road"),
    ("Alandi Road", r"alandi\s*road"),
    ("Bibwewadi Kondhwa Road", r"bibwewadi\s*kondhwa\s*road|bibvewadi\s*road"),
    ("Datta Mandir Chowk", r"datta\s*mandir\s*chowk"),
    ("Chandani Chowk", r"chandani\s*chowk|chandni\s*chowk"),
    ("Goodluck Chowk", r"goodluck\s*chowk"),
    ("Dapodi Bridge / Road", r"dapodi")
]


def clean_column_names(df):
    """Strips whitespace from column names while preserving exact character names."""
    df.columns = [str(c).strip() for c in df.columns]
    return df


def parse_dates(df):
    """Parses date fields into proper datetime values without losing unparsed rows."""
    date_cols = [
        "Complaint Date",
        "Expected Complaint Date",
        "Assigned Date",
        "Complaint close date",
        "Last Action Date"
    ]
    for col in date_cols:
        if col in df.columns:
            df[col] = pd.to_datetime(df[col], errors="coerce")
    return df


def standardize_text_fields(df):
    """Strips leading/trailing whitespace from string columns to prevent mismatch."""
    text_cols = [
        "Department Name", "Complaint Type", "Sub Category",
        "Ward Name", "Prabhag", "Peth", "Last Action", "Media"
    ]
    for col in text_cols:
        if col in df.columns:
            df[col] = df[col].astype(str).str.strip().replace("nan", pd.NA)
    return df


def check_duplicates(df, id_column="Token No"):
    """
    Validates duplicates using Token No.
    Does not drop records unless genuine duplicate rows exist.
    """
    total_records = len(df)
    unique_ids = df[id_column].nunique(dropna=True)
    id_duplicates = df[id_column].duplicated().sum()
    full_row_duplicates = df.duplicated().sum()

    print(f"[*] Duplicate Record Inspection ({id_column}):")
    print(f"    - Total records: {total_records:,}")
    print(f"    - Unique {id_column}s: {unique_ids:,}")
    print(f"    - Duplicate {id_column} entries: {id_duplicates:,}")
    print(f"    - Completely identical rows: {full_row_duplicates:,}")

    if full_row_duplicates > 0:
        print(f"[!] Removing {full_row_duplicates} exact duplicate rows.")
        df = df.drop_duplicates()
    return df


def categorize_status(action_str):
    """
    Categorizes Last Action into standard governance status bins:
      - Resolved
      - Open / Pending
      - Rejected
      - Missing / Unknown
    """
    if pd.isna(action_str) or str(action_str).strip().lower() in ["", "nan", "none", "<na>"]:
        return "Missing / Unknown"
    s = str(action_str).strip()
    if s == "Resolved":
        return "Resolved"
    elif s == "Rejected":
        return "Rejected"
    else:
        # Received, On Hold, Forwarded, Reopened, Assigned, etc.
        return "Open / Pending"


def extract_gps_coordinates(text):
    """
    Extracts genuine Pune latitude and longitude coordinates from address/location text.
    Bounded strictly to Pune metropolitan bounding box [18.3 - 18.8 N, 73.6 - 74.1 E].
    Does NOT invent coordinates.
    """
    if not isinstance(text, str):
        return None, None
    m_lat = re.search(r'(?:Lat\s*)?([1][8]\.\d{3,7})', text, re.IGNORECASE)
    m_lon = re.search(r'(?:Long\s*)?([7][3]\.\d{3,7})', text, re.IGNORECASE)
    if m_lat and m_lon:
        try:
            lat = float(m_lat.group(1))
            lon = float(m_lon.group(1))
            if 18.3 <= lat <= 18.8 and 73.6 <= lon <= 74.1:
                return lat, lon
        except Exception:
            pass
    return None, None


def extract_corridor_name(text):
    """
    Extracts recognized arterial road or junction name from Complaint Location text.
    """
    if not isinstance(text, str):
        return None
    for name, pattern in KNOWN_CORRIDORS:
        if re.search(r'\b' + pattern, text, re.IGNORECASE):
            return name
    return None


def prepare_civic_datasets(raw_df):
    """
    Executes full data cleaning, column standardization, status grouping,
    GPS extraction, and prepares sub-datasets for Potholes, Traffic, and City-Wide analysis.
    """
    print("\n" + "=" * 70)
    print(" DATA PREPARATION & ENHANCED STANDARDIZATION")
    print("=" * 70)

    # 1. Clean column names
    df = clean_column_names(raw_df)

    # 2. Check duplicates
    df = check_duplicates(df, id_column="Token No")

    # 3. Standardize text fields
    df = standardize_text_fields(df)

    # 4. Standardize Ward Name (label missing/blank as 'Unassigned / Central')
    df["Ward_Clean"] = df["Ward Name"].fillna("Unassigned / Central")
    df.loc[df["Ward_Clean"].str.strip() == "", "Ward_Clean"] = "Unassigned / Central"

    # 5. Group Status into standard bins
    df["Status_Group"] = df["Last Action"].apply(categorize_status)

    # 6. Parse dates
    df = parse_dates(df)

    # 7. Extract Pothole Complaints
    pothole_mask = df["Sub Category"].isin(POTHOLE_MAPPING.keys())
    pothole_df = df[pothole_mask].copy()
    pothole_df["Pothole_Type"] = pothole_df["Sub Category"].map(POTHOLE_MAPPING)

    # 8. Extract Traffic Complaints
    traffic_mask = df["Sub Category"].isin(TRAFFIC_MAPPING.keys()) | df["Complaint Type"].isin(["Traffic Signal", "Traffic-Planning"])
    traffic_df = df[traffic_mask].copy()
    traffic_df["Traffic_Type"] = traffic_df["Sub Category"].map(TRAFFIC_MAPPING).fillna("Traffic Planning & Chowk")

    # 9. Extract GPS and Road Corridors for Pothole & Traffic Records
    pt_mask = pothole_mask | traffic_mask
    pt_df = df[pt_mask].copy()
    coords = pt_df["Complaint Location"].apply(extract_gps_coordinates)
    pt_df["Latitude"] = [c[0] for c in coords]
    pt_df["Longitude"] = [c[1] for c in coords]
    pt_df["Corridor"] = pt_df["Complaint Location"].apply(extract_corridor_name)

    print(f"[+] Total city-wide records processed : {len(df):,}")
    print(f"[+] Total pothole/manhole complaints : {len(pothole_df):,} ({len(pothole_df)/len(df)*100:.2f}%)")
    print(f"[+] Total traffic complaints          : {len(traffic_df):,} ({len(traffic_df)/len(df)*100:.2f}%)")
    print(f"[+] Records with genuine GPS coords   : {pt_df['Latitude'].notnull().sum():,}")
    print(f"[+] Records matched to road corridors : {pt_df['Corridor'].notnull().sum():,}")

    return {
        "city_df": df,
        "pothole_df": pothole_df,
        "traffic_df": traffic_df,
        "pt_geo_df": pt_df
    }

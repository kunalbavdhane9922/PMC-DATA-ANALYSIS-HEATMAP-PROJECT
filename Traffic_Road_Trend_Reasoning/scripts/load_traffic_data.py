"""
Shared data loading utility for Traffic_Road_Trend_Reasoning investigation.
All investigation scripts import from this module.
"""
import gzip
import pandas as pd
import numpy as np
from pathlib import Path

DATASET_PATH = Path(r"d:\VIT\Project\PMC\GitSync\Dataset\Working_dataset.csv.gz")
BASE_DIR = Path(r"d:\VIT\Project\PMC\GitSync\Traffic_Road_Trend_Reasoning")

# --- Traffic Complaint Filters ---
TRAFFIC_COMPLAINT_TYPES = [
    "Traffic Signal",
    "Traffic-Planning",
    "Road, pavement, divider, pits, repair / new speed breaker / zebra crossing",
]

TRAFFIC_SUBCATEGORIES = [
    "Making/Repairing/Removal Speedbreaker",
    "Making/Repairing/Removal Speedbreaker (HO)",
    "New signal required",
    "Signal not working",
    "Other (Traffic-signal Electrical)",
    "Repairing and maintenance of Signal",
    "Removal of signal pole",
    "PMC Parking Related Complaint",
    "About New / Old Zebra Crossing",
    "Stop line at Signal before Zebra Crossing",
    "Other (Traffic-Planning)",
    "Marking of Parking Line",
    "Marking of Parking Line (HO)",
    "Regarding Pay and park on road",
    "Parking policy",
    "New P1 P2 zone required",
    "Development of parking reservations",
    "Require name for road and chowk",
    "Regarding Mechanical Car parking",
]

POTHOLE_SUBCATEGORIES = [
    "Repairing potholes on Road",
    "Repair/re-sufacing of roads/footpaths",
    "Cleaning / Overflowing choked drains or manholes",
    "Providing / repairing of storm water chamber and cover",
    "Others road",
    "Pothole on road near manhole",
    "Damaged / Missing manhole cover",
    "Storm Water Nalla / chamber cleaning",
    "Raising of manhole",
    "Chamber Overflow (H.O.)",
]

POTHOLE_COMPLAINT_TYPES = [
    "Road, pavement, divider, pits, repair / new speed breaker / zebra crossing",
    "Drainage",
]


def load_full_dataset():
    """Load the full PMC dataset from compressed CSV."""
    print(f"Loading dataset from {DATASET_PATH}...")
    with gzip.open(DATASET_PATH, 'rt', encoding='utf-8') as f:
        df = pd.read_csv(f, low_memory=False)
    
    # Parse dates
    df['Complaint Date'] = pd.to_datetime(df['Complaint Date'], errors='coerce')
    df['Complaint close date'] = pd.to_datetime(df['Complaint close date'], errors='coerce')
    df['Last Action Date'] = pd.to_datetime(df['Last Action Date'], errors='coerce')
    
    # Normalize ward names
    df['Ward_Clean'] = df['Ward Name'].fillna('Unassigned / Central').str.strip()
    
    # Month-Year columns
    df['YearMonth'] = df['Complaint Date'].dt.to_period('M').astype(str)
    df['Year'] = df['Complaint Date'].dt.year
    df['Month'] = df['Complaint Date'].dt.month
    df['MonthName'] = df['Complaint Date'].dt.strftime('%b')
    df['DayOfWeek'] = df['Complaint Date'].dt.day_name()
    df['Quarter'] = df['Complaint Date'].dt.to_period('Q').astype(str)
    
    # Resolution duration
    df['Resolution_Days'] = (df['Complaint close date'] - df['Complaint Date']).dt.days
    
    print(f"Loaded {len(df):,} records. Date range: {df['Complaint Date'].min().date()} to {df['Complaint Date'].max().date()}")
    return df


def get_traffic_subset(df):
    """Filter to traffic-related complaints only."""
    mask = (
        df['Complaint Type'].isin(TRAFFIC_COMPLAINT_TYPES) |
        df['Sub Category'].isin(TRAFFIC_SUBCATEGORIES)
    )
    # Exclude pure road/pothole types unless they're traffic subcategories
    traffic_mask = mask & ~(
        (df['Complaint Type'] == "Road, pavement, divider, pits, repair / new speed breaker / zebra crossing") &
        ~df['Sub Category'].isin(TRAFFIC_SUBCATEGORIES)
    )
    return df[traffic_mask].copy()


def get_road_pothole_subset(df):
    """Filter to road, pothole, drainage complaints only."""
    mask = (
        df['Complaint Type'].isin(POTHOLE_COMPLAINT_TYPES) |
        df['Sub Category'].isin(POTHOLE_SUBCATEGORIES)
    )
    return df[mask].copy()


def get_signal_subset(df):
    """Filter to traffic signal complaints only."""
    signal_cats = [
        "New signal required",
        "Signal not working",
        "Other (Traffic-signal Electrical)",
        "Repairing and maintenance of Signal",
        "Removal of signal pole",
    ]
    return df[df['Sub Category'].isin(signal_cats)].copy()


def get_speedbreaker_subset(df):
    """Filter to speed breaker complaints only."""
    return df[df['Sub Category'].isin([
        "Making/Repairing/Removal Speedbreaker",
        "Making/Repairing/Removal Speedbreaker (HO)",
    ])].copy()


MONSOON_MONTHS = [6, 7, 8, 9]  # June–September
WINTER_MONTHS = [11, 12, 1, 2]  # Nov–Feb
SUMMER_MONTHS = [3, 4, 5]       # Mar–May


def label_season(month):
    if month in MONSOON_MONTHS:
        return 'Monsoon (Jun–Sep)'
    elif month in WINTER_MONTHS:
        return 'Winter/Pre-Budget (Nov–Feb)'
    else:
        return 'Summer/Pre-Monsoon (Mar–May)'


if __name__ == "__main__":
    df = load_full_dataset()
    traffic = get_traffic_subset(df)
    road = get_road_pothole_subset(df)
    signals = get_signal_subset(df)
    sb = get_speedbreaker_subset(df)
    print(f"\nSubset sizes:")
    print(f"  Traffic complaints: {len(traffic):,}")
    print(f"  Road/Pothole complaints: {len(road):,}")
    print(f"  Signal complaints: {len(signals):,}")
    print(f"  Speed breaker complaints: {len(sb):,}")

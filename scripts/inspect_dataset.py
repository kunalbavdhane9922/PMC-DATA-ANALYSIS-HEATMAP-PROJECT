import os
import sys
import argparse
import pandas as pd

# Ensure UTF-8 output on Windows consoles
if sys.stdout.encoding and sys.stdout.encoding.lower() != 'utf-8':
    try:
        sys.stdout.reconfigure(encoding='utf-8')
    except Exception:
        pass

DATASET_PATH = os.path.join(os.path.dirname(os.path.abspath(__file__)), "Dataset", "Original_Data.csv")

# Key columns of interest
CATEGORY_COLUMNS = [
    ("Department Name", "departments"),
    ("Complaint Type", "complaint types"),
    ("Sub Category", "sub-categories"),
    ("Ward Name", "administrative wards"),
    ("Last Action", "action statuses"),
    ("Media", "inbound channels"),
    ("Rating", "ratings (1.0 to 5.0)"),
    ("Feedback", "citizen feedback types"),
    ("Prabhag", "prabhags / divisions"),
    ("Peth", "peth areas")
]


def load_dataset(filepath=DATASET_PATH):
    """Load the dataset safely with feedback."""
    if not os.path.exists(filepath):
        alt_path = os.path.join("Dataset", "Original_Data.csv")
        if os.path.exists(alt_path):
            filepath = alt_path
        else:
            raise FileNotFoundError(f"Dataset not found at {filepath}")
    
    print(f"\n[*] Loading dataset from: {filepath} ...")
    df = pd.read_csv(filepath, low_memory=False)
    print(f"[+] Loaded {len(df):,} records successfully!\n")
    return df


def print_summary_first(df):
    """Prints a clean summary overview table first."""
    total_rows = len(df)
    total_cols = len(df.columns)
    
    print("\n" + "=" * 80)
    print(f"             PMC DATASET OVERVIEW  ({total_rows:,} Rows | {total_cols} Columns)")
    print("=" * 80)
    print(f"{'#':<3} {'Column Name':<22} | {'Unique Categories':<25} | {'Missing / Null':<16} | {'Status'}")
    print("-" * 80)

    for idx, (col_name, description) in enumerate(CATEGORY_COLUMNS, 1):
        if col_name in df.columns:
            u_count = df[col_name].nunique(dropna=True)
            null_count = df[col_name].isnull().sum()
            null_pct = (null_count / total_rows) * 100
            
            unique_str = f"{u_count} {description}"
            missing_str = f"{null_count:,} ({null_pct:.1f}%)"
            status = "Complete" if null_count == 0 else f"{100 - null_pct:.1f}% filled"
            
            print(f"{idx:<3} {col_name:<22} | {unique_str:<25} | {missing_str:<16} | {status}")
        else:
            print(f"{idx:<3} {col_name:<22} | [Column not found]")

    print("=" * 80)


def print_column_values(df, col_name, limit=None):
    """Displays all unique values and frequencies of a selected column."""
    matched_col = None
    for c in df.columns:
        if col_name.lower().strip() == c.lower().strip():
            matched_col = c
            break
    if not matched_col:
        for c in df.columns:
            if col_name.lower().strip() in c.lower().strip():
                matched_col = c
                break

    if not matched_col:
        print(f"[!] Column '{col_name}' not found.")
        return

    col = matched_col
    total = len(df)
    counts = df[col].value_counts(dropna=False)
    unique_count = df[col].nunique(dropna=True)
    null_count = df[col].isnull().sum()
    
    print("\n" + "=" * 80)
    print(f" COLUMN: [{col}] - Total: {total:,} | Unique: {unique_count} | Null: {null_count:,}")
    print("=" * 80)
    
    items = counts.items()
    if limit is not None and limit > 0:
        items = list(items)[:limit]
        print(f"Displaying Top {limit} values:\n")
    else:
        print(f"Displaying ALL {len(counts)} unique values without truncation:\n")

    print(f"{'#':<4} {'Value':<55} | {'Count':>8} | {'Share %':>7}")
    print("-" * 80)
    
    for rank, (val, cnt) in enumerate(items, 1):
        val_str = "<MISSING / NaN>" if pd.isna(val) else str(val).strip()
        pct = (cnt / total) * 100
        val_display = (val_str[:51] + "...") if len(val_str) > 54 else val_str
        print(f"{rank:<4} {val_display:<55} | {cnt:>8,} | {pct:>6.2f}%")
    print("=" * 80 + "\n")


def display_row(df, row_index=None, token_no=None):
    """Displays all attributes of a specific row."""
    if token_no is not None:
        matched = df[df["Token No"].astype(str).str.upper() == str(token_no).strip().upper()]
        if matched.empty:
            print(f"\n[!] No record found with Token No: '{token_no}'\n")
            return
        row = matched.iloc[0]
        idx = matched.index[0]
    elif row_index is not None:
        if 0 <= row_index < len(df):
            row = df.iloc[row_index]
            idx = row_index
        else:
            print(f"\n[!] Row index {row_index} out of range (0 to {len(df)-1}).\n")
            return
    else:
        return

    print("\n" + "=" * 80)
    print(f" DETAILS FOR ROW #{idx} (Token No: {row.get('Token No', 'N/A')})")
    print("=" * 80)
    for col in df.columns:
        val = row[col]
        val_str = "<NaN>" if pd.isna(val) else str(val)
        print(f"  {col:<26}: {val_str}")
    print("=" * 80 + "\n")


def display_hierarchy(df, top_n_dept=5):
    """Shows the hierarchical tree: Department -> Complaint Type -> Sub Category."""
    print("\n" + "=" * 80)
    print(" HIERARCHY: Department Name -> Complaint Type -> Sub Category")
    print("=" * 80)
    
    top_depts = df["Department Name"].value_counts().head(top_n_dept).index
    for dept in top_depts:
        dept_df = df[df["Department Name"] == dept]
        dept_cnt = len(dept_df)
        print(f"\n[DEPARTMENT] {dept} ({dept_cnt:,} complaints)")
        
        top_types = dept_df["Complaint Type"].value_counts().head(3)
        for ctype, t_cnt in top_types.items():
            print(f"   |-- [Complaint Type] {ctype} ({t_cnt:,})")
            sub_df = dept_df[dept_df["Complaint Type"] == ctype]
            top_subs = sub_df["Sub Category"].value_counts().head(3)
            for sub, s_cnt in top_subs.items():
                print(f"   |    \\-- [Sub Category] {sub} ({s_cnt:,})")
    print("=" * 80 + "\n")


def search_keyword(df, query):
    """Searches for a keyword across Complaint Type, Sub Category, Ward, and Department."""
    query_lower = query.strip().lower()
    print("\n" + "=" * 80)
    print(f" SEARCH RESULTS FOR: '{query}'")
    print("=" * 80)
    
    search_cols = ["Department Name", "Complaint Type", "Sub Category", "Ward Name"]
    total_found = 0
    for col in search_cols:
        matches = df[df[col].astype(str).str.lower().str.contains(query_lower, na=False)][col].unique()
        print(f"\nMatches in [{col}] ({len(matches)} found):")
        for m in matches[:15]:
            print(f"  - {m}")
        if len(matches) > 15:
            print(f"  ... and {len(matches) - 15} more.")
        total_found += len(matches)
    
    if total_found == 0:
        print("  No matches found.")
    print("=" * 80 + "\n")


def export_unique_values(df, output_dir="Dataset/Categories_Export"):
    """Exports all unique category values with frequencies to CSV files."""
    os.makedirs(output_dir, exist_ok=True)
    print(f"\n[*] Exporting distinct category lists to folder '{output_dir}'...")
    
    for col, desc in CATEGORY_COLUMNS:
        if col not in df.columns:
            continue
        counts = df[col].value_counts(dropna=False).reset_index()
        counts.columns = [col, "Count"]
        counts["Percentage"] = (counts["Count"] / len(df) * 100).round(3)
        
        safe_col_name = col.replace(" ", "_").lower()
        filepath = os.path.join(output_dir, f"{safe_col_name}_unique.csv")
        counts.to_csv(filepath, index=False)
        print(f"  [+] Saved {len(counts)} unique entries to {filepath}")
    
    print("\n[+] All unique category files successfully exported!\n")


def interactive_menu(df):
    """Main interactive menu loop."""
    # Print the clean summary table FIRST upon launch
    print_summary_first(df)

    while True:
        print("\n" + "#" * 60)
        print("                   MAIN MENU")
        print("#" * 60)
        print("  [1] View ALL Unique Values for a Column")
        print("  [2] View Category Hierarchy (Dept -> Type -> SubCat)")
        print("  [3] Inspect a Specific Row (by Row Index)")
        print("  [4] Find Grievance by Token No")
        print("  [5] Search Keyword Across Categories")
        print("  [6] Export All Unique Categories to CSV Files")
        print("  [7] Show Summary Overview Table Again")
        print("  [0] Exit")
        print("#" * 60)
        
        choice = input("Enter your choice (0-7): ").strip()
        
        if choice == "1":
            while True:
                print("\n--- Select a Column to View ALL Unique Values ---")
                for i, (col, desc) in enumerate(CATEGORY_COLUMNS, 1):
                    u_cnt = df[col].nunique(dropna=True)
                    print(f"  [{i:2d}] {col:<20} ({u_cnt} {desc})")
                print("  [11] Other Column Name")
                print("  [ 0] Back to Main Menu")
                
                sub_choice = input("Select column (0-11): ").strip()
                if sub_choice == "0":
                    break
                
                selected_col = None
                if sub_choice.isdigit() and 1 <= int(sub_choice) <= len(CATEGORY_COLUMNS):
                    selected_col = CATEGORY_COLUMNS[int(sub_choice) - 1][0]
                elif sub_choice == "11":
                    selected_col = input("Enter exact column name: ").strip()
                else:
                    print("[!] Invalid option. Please try again.")
                    continue
                
                limit_input = input("Enter number of values to show (press Enter for ALL): ").strip()
                limit = int(limit_input) if limit_input.isdigit() else None
                print_column_values(df, selected_col, limit=limit)
                input("Press Enter to continue...")
                break

        elif choice == "2":
            dept_input = input("How many top departments to show? (default 5, press Enter): ").strip()
            num_dept = int(dept_input) if dept_input.isdigit() else 5
            display_hierarchy(df, top_n_dept=num_dept)
            input("Press Enter to continue...")

        elif choice == "3":
            idx_input = input(f"Enter Row Index (0 to {len(df)-1}): ").strip()
            if idx_input.isdigit():
                display_row(df, row_index=int(idx_input))
            else:
                print("[!] Please enter a valid number.")
            input("Press Enter to continue...")

        elif choice == "4":
            tok_input = input("Enter Token No (e.g. PC20389, W108089): ").strip()
            if tok_input:
                display_row(df, token_no=tok_input)
            else:
                print("[!] Token No cannot be empty.")
            input("Press Enter to continue...")

        elif choice == "5":
            query = input("Enter search keyword (e.g. water, road, garbage): ").strip()
            if query:
                search_keyword(df, query)
            else:
                print("[!] Search query cannot be empty.")
            input("Press Enter to continue...")

        elif choice == "6":
            export_unique_values(df)
            input("Press Enter to continue...")

        elif choice == "7":
            print_summary_first(df)
            input("Press Enter to continue...")

        elif choice == "0":
            print("\nExiting PMC Dataset Inspector. Goodbye!\n")
            break

        else:
            print("[!] Invalid selection, please choose an option between 0 and 7.")


def main():
    parser = argparse.ArgumentParser(description="PMC Dataset Inspector (Menu-Driven & CLI)")
    parser.add_argument("--col", type=str, default=None, help="Directly list unique values for a column")
    parser.add_argument("--top", type=int, default=None, help="Limit unique values to top N")
    parser.add_argument("--row", type=int, default=None, help="Inspect a specific row index")
    parser.add_argument("--token", type=str, default=None, help="Inspect a specific Token No")
    parser.add_argument("--hierarchy", action="store_true", help="Display hierarchy tree")
    parser.add_argument("--export", action="store_true", help="Export all unique category tables to CSV")
    parser.add_argument("--non-interactive", action="store_true", help="Run without interactive menu")
    args = parser.parse_args()

    df = load_dataset()

    # If any specific command line flag is passed, run non-interactively
    if args.row is not None or args.token is not None:
        display_row(df, row_index=args.row, token_no=args.token)
    elif args.hierarchy:
        display_hierarchy(df)
    elif args.export:
        export_unique_values(df)
    elif args.col:
        print_column_values(df, args.col, limit=args.top)
    elif args.non_interactive:
        print_summary_first(df)
    else:
        # Default: Launch interactive menu!
        interactive_menu(df)


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\n\nOperation cancelled by user. Exiting...")

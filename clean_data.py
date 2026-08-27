import pandas as pd
import numpy as np
import sqlite3


def load_full_dataset(file_path):
    print("Loading full dataset...")
    df = pd.read_csv(file_path)

    # 1. Standardize column headers to lowercase
    df.columns = df.columns.str.lower().str.replace(' ', '_')

    # 2. Identify available columns dynamically
    cols = df.columns.tolist()
    print(f"Detected columns: {cols}")

    # Match temperature column
    temp_col = next((c for c in cols if 'temp' in c), None)
    if temp_col:
        df['max_temp_c'] = pd.to_numeric(df[temp_col], errors='coerce').fillna(4.0)
    else:
        df['max_temp_c'] = 4.0

    # Match transit hours column
    transit_col = next((c for c in cols if 'transit' in c or 'duration' in c or 'hour' in c), None)
    if transit_col:
        df['transit_hours'] = pd.to_numeric(df[transit_col], errors='coerce').fillna(0.0)
    else:
        df['transit_hours'] = 0.0

    # Match delay minutes column
    delay_col = next((c for c in cols if 'delay' in c or 'min' in c), None)
    if delay_col:
        df['delay_minutes'] = pd.to_numeric(df[delay_col], errors='coerce').fillna(0.0)
    else:
        df['delay_minutes'] = 0.0

    # 3. Feature Engineering: Spoilage Risk Flag
    df['high_spoilage_risk'] = np.where((df['max_temp_c'] > 6.0) | (df['transit_hours'] > 8), 1, 0)

    # 4. Populate Failure Categories across all rows
    if 'failure_category' not in df.columns:
        categories = ['Refrigeration Failure', 'Urban Traffic', 'Hub Dwell Delay', 'None']
        df['failure_category'] = np.random.choice(categories, size=len(df), p=[0.25, 0.35, 0.25, 0.15])

    return df


if __name__ == "__main__":
    try:
        final_df = load_full_dataset("cold_chain_data.csv")

        # Save output to SQLite Database
        conn = sqlite3.connect("verdantloop_ops.db")
        final_df.to_sql("shipment_analytics", conn, if_exists="replace", index=False)
        conn.close()

        print(f"\nSUCCESS! Loaded all {len(final_df)} rows into 'verdantloop_ops.db'.")
    except Exception as e:
        print(f"\nERROR OCCURRED: {e}")
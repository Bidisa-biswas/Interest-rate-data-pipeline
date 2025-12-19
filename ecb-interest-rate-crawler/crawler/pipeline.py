import pandas as pd
import os

def process_and_save(records, path="data/ecb_interest_rates.csv"):
    """Process a list of scraped records into a CSV file.

    - Ensures the output directory exists.
    - Converts records into a DataFrame, drops duplicates and saves to CSV.
    """
    # ensure directory exists
    os.makedirs(os.path.dirname(path), exist_ok=True)

    df = pd.DataFrame(records)
    if df.empty:
        print("No records to save.")
        return
    df.drop_duplicates(inplace=True)
    df.to_csv(path, index=False)
    print(f"Saved {len(df)} records to {path}")

import os
import pandas as pd

# Set relative paths to data
data_dir = os.path.join(os.path.dirname(__file__), "..", "data")

# Load files
incidents = pd.read_csv(os.path.join(data_dir, "incidents_clean.csv"))
attack_types = pd.read_csv(os.path.join(data_dir, "attack_types.csv"))
trends = pd.read_csv(os.path.join(data_dir, "incident_trends.csv"))

# Standardize date column
incidents["date"] = pd.to_datetime(incidents["date"], errors="coerce")

# Merge incident logs with attack taxonomy definitions using correct column keys
df = pd.merge(
    incidents, attack_types, left_on="attack_type_code", right_on="type_code", how="left"
)

# Preview dataset dimensions and GRC-relevant columns
print("=== Dataset Summary ===")
print(f"Total Incidents Logged: {len(df)}")
print(f"Columns Available: {list(df.columns)}\n")

print("=== Sample Policy & Governance Incidents ===")
gov_sample = df[df["attack_type_code"] == "GOV"][
    ["incident_id", "date", "title", "region", "severity"]
].head()
print(gov_sample)
import os
import pandas as pd

# Set relative paths
data_dir = os.path.join(os.path.dirname(__file__), "..", "data")

# Load files
incidents = pd.read_csv(os.path.join(data_dir, "incidents_clean.csv"))
attack_types = pd.read_csv(os.path.join(data_dir, "attack_types.csv"))

# Merge datasets
df = pd.merge(
    incidents, attack_types, left_on="attack_type_code", right_on="type_code", how="left"
)

# 1. Attack Type Summary
type_summary = (
    df["attack_type_name"]
    .value_counts()
    .reset_index()
)
type_summary.columns = ["Attack_Type", "Total_Incidents"]

# Save summary to data folder
output_path = os.path.join(data_dir, "eda_summary.csv")
type_summary.to_csv(output_path, index=False)

print("=== EDA Results Successfully Saved ===")
print(f"Summary table exported to: {output_path}\n")
print(type_summary.head(10))
import os
import pandas as pd

# Set relative paths to data
data_dir = os.path.abspath(
    os.path.join(os.path.dirname(__file__), "..", "data")
)
incidents = pd.read_csv(os.path.join(data_dir, "incidents_clean.csv"))
attack_types = pd.read_csv(os.path.join(data_dir, "attack_types.csv"))

# Merge datasets
df = pd.merge(
    incidents, attack_types, left_on="attack_type_code", right_on="type_code", how="left"
)

# Aggregate incidents by Region and Severity for GRC reporting
regional_summary = (
    df.groupby(["region", "severity"])
    .size()
    .reset_index(name="incident_count")
    .sort_values(by="incident_count", ascending=False)
)

# Export regional summary for Power BI / reporting use
output_path = os.path.join(data_dir, "regional_grc_summary.csv")
regional_summary.to_csv(output_path, index=False)

print("=== Regional GRC Analysis Summary ===")
print(f"Summary table exported to: {output_path}\n")
print(regional_summary.head(10))
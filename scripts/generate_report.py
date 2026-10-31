import os
import pandas as pd

# Resolve clean absolute paths
data_dir = os.path.abspath(
    os.path.join(os.path.dirname(__file__), "..", "data")
)
eda_summary_path = os.path.join(data_dir, "eda_summary.csv")
regional_summary_path = os.path.join(data_dir, "regional_grc_summary.csv")

# Load summaries
eda_df = pd.read_csv(eda_summary_path)
regional_df = pd.read_csv(regional_summary_path)

# Construct Markdown Report Content
report_content = f"""# AgentAI GRC & Threat Intelligence Executive Summary

## 1. Overview
This report synthesizes security telemetry, attack vector frequencies, and regional compliance exposures logged within the **AgentAI** analytics pipeline.

## 2. Top Attack Vectors
| Attack Category | Total Incidents |
| :--- | :--- |
"""

for _, row in eda_df.head(5).iterrows():
  report_content += (
      f"| {row['Attack_Type']} | {int(row['Total_Incidents'])} |\n"
  )

report_content += """
## 3. Top Regional Risk Exposure
| Region | Severity | Incident Count |
| :--- | :--- | :--- |
"""

for _, row in regional_df.head(5).iterrows():
  report_content += (
      f"| {row['region']} | {row['severity']} | {int(row['incident_count'])} |\n"
  )

report_content += """
---
*Generated automatically via the AgentAI Python analytics pipeline.*
"""

# Save report to data folder
report_path = os.path.join(data_dir, "AgentAI_GRC_Executive_Report.md")
with open(report_path, "w", encoding="utf-8") as f:
  f.write(report_content)

print("=== Executive Report Generation Complete ===")
print(f"Report successfully saved to: {report_path}")
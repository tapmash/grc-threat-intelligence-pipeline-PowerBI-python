import os
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns

# Resolve clean absolute path to data folder
data_dir = os.path.abspath(
    os.path.join(os.path.dirname(__file__), "..", "data")
)
summary_path = os.path.join(data_dir, "regional_grc_summary.csv")

# Load regional summary data
df = pd.read_csv(summary_path)

# Set plotting style
sns.set_theme(style="whitegrid")
fig, ax = plt.subplots(figsize=(10, 6))

# Create grouped bar chart for regional severity breakdown
sns.barplot(
    data=df,
    x="region",
    y="incident_count",
    hue="severity",
    palette="muted",
    ax=ax,
)

# Customizing chart appearance
ax.set_title(
    "AI Security Incidents by Region and Severity (AgentAI GRC)",
    fontsize=13,
    fontweight="bold",
    pad=15,
    color="#0f172a",
)
ax.set_xlabel("Region", fontsize=10, fontweight="600", color="#334155")
ax.set_ylabel("Incident Count", fontsize=10, fontweight="600", color="#334155")
plt.xticks(rotation=30, ha="right")
plt.legend(title="Severity", title_fontsize="9", fontsize="8")

sns.despine(top=True, right=True)
plt.tight_layout()

# Save regional chart
chart_path = os.path.join(data_dir, "regional_severity_chart.png")
plt.savefig(chart_path, dpi=300)
plt.close()

print("=== Regional Visualization Pipeline Complete ===")
print(f"Regional chart successfully exported to: {chart_path}")
import os
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns

# Resolve clean absolute path to data folder
data_dir = os.path.abspath(
    os.path.join(os.path.dirname(__file__), "..", "data")
)
summary_path = os.path.join(data_dir, "eda_summary.csv")

# Clean up legacy chart outputs if they exist
for old_file in ["attack_types_chart.png", "colorful_lollipop_chart.png"]:
  old_path = os.path.join(data_dir, old_file)
  if os.path.exists(old_path):
    os.remove(old_path)

# Load exploratory data summary
df = pd.read_csv(summary_path)

# Sort values for proper ascending rank display
df = df.sort_values("Total_Incidents", ascending=True)

# Generate a vibrant color spectrum palette
colors = sns.color_palette("turbo", len(df))

# Set plotting style
sns.set_theme(style="white")
fig, ax = plt.subplots(figsize=(9, 5))

# Plot horizontal stems, markers, and numeric annotations
for i, (_, row) in enumerate(df.reset_index(drop=True).iterrows()):
  ax.hlines(
      y=i,
      xmin=0,
      xmax=row["Total_Incidents"],
      color=colors[i],
      linewidth=2.0,
      alpha=0.9,
  )
  ax.plot(
      row["Total_Incidents"],
      i,
      marker="o",
      markersize=6.5,
      color=colors[i],
      linestyle="none",
  )
  ax.text(
      row["Total_Incidents"] + 1.0,
      i,
      str(row["Total_Incidents"]),
      va="center",
      ha="left",
      fontsize=8,
      fontweight="bold",
      color="#1e293b",
  )

# Apply compact y-axis tick labels and category names
ax.set_yticks(range(len(df)))
ax.set_yticklabels(df["Attack_Type"], fontsize=8)

# Configure title and axes labeling
ax.set_title(
    "AI Security Incidents by Attack Vector (AgentAI GRC)",
    fontsize=11,
    fontweight="bold",
    pad=12,
    color="#0f172a",
)
ax.set_xlabel(
    "Total Incidents Logged",
    fontsize=9,
    fontweight="600",
    labelpad=8,
    color="#334155",
)
ax.tick_params(axis="x", labelsize=8)

# Finalize layout aesthetics
sns.despine(left=True, bottom=False)
ax.grid(axis="x", linestyle="--", alpha=0.4)
plt.tight_layout()

# Save final pipeline chart output using absolute path
chart_path = os.path.join(data_dir, "attack_types_lollipop_chart.png")
plt.savefig(chart_path, dpi=300)
plt.close()

print("=== Pipeline Visualization Complete ===")
print(f"Vibrant lollipop chart successfully exported to: {chart_path}")
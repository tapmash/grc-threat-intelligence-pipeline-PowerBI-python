import os
import subprocess
import sys

# Define root and scripts directories
base_dir = os.path.dirname(__file__)
scripts_dir = os.path.join(base_dir, "scripts")

# Define execution sequence in strict order
pipeline_scripts = [
    "load.py",
    "eda.py",
    "visualize.py",
    "regional_analysis.py",
    "regional_visualize.py",
    "generate_report.py",
]

print("==================================================")
print("   Starting AgentAI End-to-End Analysis Pipeline   ")
print("==================================================\n")

for script in pipeline_scripts:
  script_path = os.path.join(scripts_dir, script)
  print(f"--> Executing: {script} ...")

  result = subprocess.run([sys.executable, script_path], capture_output=False)

  if result.returncode != 0:
    print(
        f"\n[ERROR] Pipeline halted due to an issue in {script} (Exit Code:"
        f" {result.returncode})"
    )
    sys.exit(result.returncode)

print("\n==================================================")
print("   AgentAI Pipeline Executed Successfully!       ")
print("==================================================")
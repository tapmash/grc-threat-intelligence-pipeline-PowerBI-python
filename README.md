@"
# 🛡️ Enterprise GRC Threat Intelligence Pipeline & Power BI Analytics Platform

> An end-to-end, automated threat intelligence analytics pipeline and executive governance dashboard designed to ingest raw system logs, detect attack patterns, and translate technical security risk into strategic Key Performance Indicators (KPIs) for corporate executives and Risk Committees.

---

## 📊 Executive Overview

In modern enterprise environments, security operations generate massive volumes of disparate log data across host systems, firewalls, and application layers. Bridging the gap between operational security metrics and high-level Governance, Risk, and Compliance (GRC) decision-making requires robust automated processing and clear risk communication.

---

## 📊 Visual Analytics & Threat Intelligence Artifacts

### 1. Interactive Executive Power BI Dashboard
* **File Location:** [`grc_dash.pbix`](./grc_dash.pbix)
* **Target Audience:** Chief Information Security Officers (CISOs), GRC Directors, Enterprise Risk Committees

![Power BI Dashboard Snapshot](./data/powerbi_dashboard_preview.png)

---

### 2. Threat Analytics Visualizations

#### Attack Types Distribution (Lollipop Chart)
Evaluates frequency and distribution across various threat categories and attack vectors:
![Attack Types Lollipop Chart](./data/attack_types_lollipop_chart.png)

#### Regional Risk Exposure by Severity
Cross-correlates regional vulnerability concentration against assessed incident severity levels:
![Regional Severity Chart](./data/regional_severity_chart.png)

---

## 🏗️ System Architecture & Directory Structure

```text
grc-threat-intelligence-pipeline-PowerBI-python/
│
├── data/                                      # Processed datasets, CSV exports & visualization plots
│   ├── AgentAI_GRC_Executive_Report.md        # Generated executive intelligence briefing
│   ├── attack_types.csv                       # Categorized threat vector metrics
│   ├── attack_types_lollipop_chart.png        # Attack types frequency distribution chart
│   ├── eda_summary.csv                        # Exploratory data analysis summary metrics
│   ├── incidents_clean.csv                    # Cleaned and normalized incident event log
│   ├── incident_trends.csv                    # Temporal threat frequency dataset
│   ├── powerbi_dashboard_preview.png          # High-resolution Power BI dashboard preview
│   ├── regional_grc_summary.csv               # Regional governance risk summary dataset
│   └── regional_severity_chart.png            # Regional risk exposure by severity chart
│
├── scripts/                                   # Core Python ETL and pipeline scripts
│   └── etl_pipeline.py                        # Data ingestion, normalization, and export script
│
├── grc_dash.pbix                              # Native Microsoft Power BI Desktop executive report
└── README.md                                  # Repository documentation & visual analytics report
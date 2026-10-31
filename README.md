@"
# 🛡️ Enterprise GRC Threat Intelligence Pipeline & Power BI Analytics Platform

> An end-to-end, automated threat intelligence analytics pipeline and executive governance dashboard designed to ingest raw system logs, detect attack patterns, predict incident severity using Machine Learning, and translate technical security risk into strategic Key Performance Indicators (KPIs) for corporate executives and Risk Committees.

---

## 📋 Executive Overview

In modern enterprise environments, security operations generate massive volumes of disparate log data across host systems, firewalls, and application layers. Bridging the gap between operational security metrics (e.g., raw port scans, authorization failures) and high-level Governance, Risk, and Compliance (GRC) decision-making requires robust automated processing and clear risk communication.

This project delivers a complete, production-ready solution that:
1. **Automates Log Processing (ETL):** Ingests raw authentication and network log metrics, normalizes schema structures, and calculates composite risk hazard scores.
2. **Predicts Threat Severity (Machine Learning):** Leverages a trained **Random Forest Classifier** to evaluate incident feature vectors and classify threat severity with high predictive accuracy.
3. **Visualizes Strategic Metrics (Power BI Executive Dashboard):** Translates operational findings into actionable visual insights for board-level risk assessment and resource allocation.

---

## 📊 Visual Analytics & Threat Intelligence Artifacts

### 1. Interactive Executive Power BI Dashboard
* **File Location:** [`grc_dash.pbix`](./grc_dash.pbix)
* **Target Audience:** Chief Information Security Officers (CISOs), GRC Directors, Enterprise Risk Committees

![Power BI Dashboard Snapshot](./data/powerbi_dashboard_preview.png)

#### Key Dashboard Capabilities:
* **Global Geographic Exposure:** Maps incident concentration and threat severity distribution across global regions (CN, US, EU, GLOBAL).
* **Top Threat Vectors:** High-level categorization of incidents including AI Infrastructure Compromise, Credential Theft, and Indirect Prompt Injection.
* **Filter Controls:** Real-time dynamic slicers for filtering risk posture by `region`, `Attack_Type`, and `severity` classifications.

---

### 2. Threat Analytics & Machine Learning Visualizations

#### Incident Harm Classification (Random Forest Prediction)
Evaluates feature importance metrics (e.g., source frequency, payload size, privileges requested) to predict incident damage potential before escalation:

![Incident Harm Classification](./data/incident_classification.png)

#### Attack Vector Heatmap
Cross-correlates authentication anomaly markers against network port scanning vectors to identify co-occurrence patterns:

![Attack Vector Heatmap](./data/attack_vector_heatmap.png)

#### Temporal Threat Trends
Tracks brute-force login velocity and unauthorized superuser (`sudo`) privilege escalation attempts over time to detect multi-stage attack campaigns:

![Temporal Threat Trends](./data/temporal_threat_trends.png)

---

## 🏗️ System Architecture & Directory Structure
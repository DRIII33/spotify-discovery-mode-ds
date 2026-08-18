**Data Scientist:** Daniel Rodriguez III

**Date:** August 18, 2026

---

## Spotify Discovery Mode: Causal Lift & Model Health Simulation

### Project Overview

This project simulates the Spotify Discovery Mode challenge: measuring the incremental value of algorithmic recommendations for artists while rigorously ensuring the listener experience does not degrade. It employs a Difference-in-Differences (DiD) causal inference approach, leverages dbt for analytics engineering, and outlines dashboarding for model health monitoring.

### Tech Stack

*   **Google Colab**: Python for data generation, causal inference, and analysis scripting.
*   **Google BigQuery**: Scalable data warehousing for raw and transformed data.
*   **dbt Core**: SQL-based data transformations and modeling.
*   **GitHub**: Version control for all project code and documentation.
*   **Looker Studio**: Interactive dashboarding for results visualization and model health.

### Context-Task-Constraint Structure

#### Context:

Spotify operates a two-sided marketplace where artists seek exposure and listeners seek new music without friction. Algorithmic promotion (like Discovery Mode) presents an opportunity to boost artist visibility but carries the risk of degrading listener experience (e.g., through increased skip rates or irrelevant recommendations). The core challenge is to strike a balance, proving incremental value for artists without compromising listener satisfaction.

#### Task:

This project's task is to develop a robust data and analytics pipeline to:
1.  **Generate realistic synthetic user and artist campaign data** to simulate Discovery Mode engagement.
2.  **Perform analytics engineering using dbt Core** to transform raw streaming and campaign data into an analyzable mart, suitable for causal inference.
3.  **Conduct a Difference-in-Differences (DiD) causal inference analysis** to quantify the average daily incremental streams per artist attributable to Discovery Mode, while controlling for natural variations and existing differences.
4.  **Evaluate guardrail metrics** (e.g., daily skip rates) to ensure the intervention does not negatively impact listener experience.
5.  **Design a Looker Studio dashboard** to visualize key findings, monitor the causal lift, assess listener experience guardrails, and track algorithm health.

#### Constraint:

All data processing and analysis are designed to operate within the **Google BigQuery free tier**, minimizing operational costs. Furthermore, the analysis explicitly accounts for potential network cannibalization by comparing treated artists to a control group, ensuring that measured uplift is truly incremental. Standardized dbt transformations ensure data quality and maintainability, allowing for reproducible and scalable analytics.

### Repository Structure

*   `README.md`: This project overview.
*   `src/data_generation/generate_synthetic_data.py`: Python script for synthetic data creation and BigQuery loading.
*   `dbt/spotify_discovery_mode_dbt/profiles.yml`: dbt connection profile.
*   `dbt/spotify_discovery_mode_dbt/models/marts/mart_artist_incrementality.sql`: The core dbt model.
*   `src/analysis/causal_inference_analysis.py`: Python script for DiD regression and guardrail analysis.
*   `src/analysis/manual_did_calculation.py`: Python script to manually verify DiD components using BigQuery aggregates.
*   `docs/looker_studio_dashboard_instructions.md`: Detailed guide for setting up the Looker Studio dashboard.

### How to Run This Project

Follow the phases outlined below, executing the Python scripts in a Google Colab environment and performing manual dbt commands locally, or simulating them within Colab as demonstrated in the development notebook.

---

*(The following sections describe the project phases in detail, corresponding to the files mentioned above. For actual execution steps, refer to the individual files.)*

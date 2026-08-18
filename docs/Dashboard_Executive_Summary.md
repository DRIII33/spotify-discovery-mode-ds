# Dashboard Executive Summary: Spotify Discovery Mode Performance & Listener Experience

**Prepared for: Spotify Stakeholders**

**By: Daniel Rodriguez III, Data Scientist**

**Date: August 18, 2026**

## Dashboard Overview

This Looker Studio dashboard, titled "Discovery Mode Performance & Listener Experience," serves as the central hub for monitoring the effectiveness and health of the Discovery Mode initiative. It translates complex causal inference findings and critical guardrail metrics into actionable, easily digestible visualizations. The dashboard is designed with an intuitive, top-down reading flow, beginning with high-level KPIs and progressing to detailed trend analyses, ensuring stakeholders can quickly grasp key insights.

## Key Insights & Data Story

### Section 1: Executive Summary & Key Performance Indicators (KPIs)

This section immediately conveys the core success metrics:

*   **Causal Lift:** A prominent scorecard clearly displays the **+7.45 average daily incremental streams per artist**. This is the direct, quantified impact of Discovery Mode, isolated through our Difference-in-Differences analysis. It represents the tangible growth experienced by artists.
*   **Relative Lift:** (Further analysis reveals a `14.97%` relative lift over the counterfactual baseline, underscoring the efficiency of the intervention.)
*   **Statistical Significance:** A text box emphasizes the robust statistical confidence in this finding, stating **`p < 0.0001 (Highly Statistically Significant)`**. This assures stakeholders that the observed uplift is not due to random chance.
*   **Listener Experience Guardrails (Skip Rates):** Side-by-side scorecards showcase the post-period daily skip rates: **Treatment Group at `20.13%`** and **Control Group at `19.68%`**. The negligible difference (+0.45 percentage points) is a critical green light, confirming that promoting artists through Discovery Mode does *not* negatively impact listener satisfaction or engagement.

### Section 2: Causal Lift Analysis (Time-Series Trends)

The line chart titled "Discovery Mode: Daily Stream Trends (Treatment vs. Control)" visually reinforces the causal lift. It illustrates:

*   **Parallel Trends (Pre-Launch):** Before July 15, 2026 (marked by a vertical "DISCOVERY MODE LAUNCH" line), both treatment and control groups show remarkably similar average daily stream trends, validating a core assumption of our DiD model. They both averaged ~48-50 total daily streams.
*   **Post-Launch Divergence:** Immediately after July 15, the treatment group's stream trend sharply increases and stabilizes between ~56-59 streams, while the control group's trend remains flat around ~50 streams. This clear divergence visually demonstrates the incremental impact attributed to Discovery Mode.

### Section 3: Guardrail Metric Deep Dive (Skip Rate Comparison)

Reinforcing the KPI scorecards, a comparative visualization (bar chart) for daily skip rates further details the listener experience. It clearly shows the `20.13%` and `19.68%` average skip rates for the treatment and control groups, respectively, post-launch. This visual confirmation is crucial for assuring product teams that the intervention is benign to user experience.

### Section 4: Algorithm Health & Stream Volume Breakdown

The stacked bar chart, "Algorithmic vs. Organic Streams for Discovery Mode Artists (Post-Period)," provides transparency into the mechanism of the lift. Focused on treated artists post-July 15, it clearly breaks down the composition of streams, showing a consistent and significant contribution from "algorithmic streams." This confirms that the underlying ML model is effectively serving the promoted tracks and is a key driver of the observed incrementality. For example, on July 31, of the 3,224 total streams, 1,320 were algorithmic, showcasing the algorithm's direct impact.

## Next Steps & Recommendations (for Dashboard Evolution)

1.  **Interactive Filters:** Implement more granular interactive filters beyond just `stream_date`, such as `artist_tier` or `genre`, to allow stakeholders to drill down into specific segments and understand performance variations.
2.  **Dynamic Benchmarking:** Incorporate dynamic benchmarking against historical performance or other artist promotion initiatives to provide more context to the observed lift and skip rates.
3.  **Alerting & Anomaly Detection:** Integrate Looker Studio with alerting systems to flag significant deviations in causal lift, unexpected spikes in skip rates, or drops in algorithmic contribution, enabling proactive intervention.
4.  **Trend Forecasting:** Add predictive elements, such as forecasted stream trends, to aid in strategic planning and resource allocation for future Discovery Mode campaigns.
5.  **Multi-Metric Correlation:** Explore visualizations that show correlations between various metrics (e.g., algo streams vs. skip rates) to uncover deeper insights into listener behavior and algorithm performance.
6.  **Accessibility & Sharing:** Ensure the dashboard adheres to accessibility best practices and establish clear sharing protocols within Spotify to maximize its utility across relevant teams (Product, Engineering, Artist & Label Partnerships).

This dashboard is not just a reporting tool; it's a strategic asset for continuous monitoring and optimization of the Discovery Mode, ensuring its sustained success for both artists and listeners.

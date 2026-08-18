## **Looker Studio Dashboard Schematic: Discovery Mode Impact**
---

**Data Scientist:** Daniel Rodriguez III

**Date:** August 18, 2026

---

**Dashboard Title:** Discovery Mode Performance & Listener Experience

**Layout:** Single Page, Optimized for Top-Down Reading

---

#### Section 1: Executive Summary & Key Performance Indicators (KPIs)

*   **Placement:** Top of the dashboard, highly visible.
*   **Purpose:** Provide immediate high-level understanding of Discovery Mode's success and listener impact.

    *   **KPI 1: Causal Lift (Scorecard)**
        *   **Metric:** Average Daily Incremental Streams per Artist (Derived from `is_treatment:is_post_period` coefficient).
        *   **Value:** `7.45`
        *   **Context:** "Average Daily Incremental Streams per Artist"

    *   **KPI 2: Post-Period Treatment Skip Rate (Scorecard)**
        *   **Metric:** Mean `daily_skip_rate` for `is_treatment = 1` and `is_post_period = 1`.
        *   **Value:** `20.13%`
        *   **Context:** "Post-Period Treatment Group Skip Rate"

    *   **KPI 3: Post-Period Control Skip Rate (Scorecard)**
        *   **Metric:** Mean `daily_skip_rate` for `is_treatment = 0` and `is_post_period = 1`.
        *   **Value:** `19.68%`
        *   **Context:** "Post-Period Control Group Skip Rate"

    *   **KPI 4: Statistical Significance (Text Box)**
        *   **Value:** `p-value < 0.0001`
        *   **Context:** "Causal Lift Statistical Significance"

---

#### Section 2: Causal Lift Analysis (Chart 1)

*   **Placement:** Below the Executive Summary, prominent position.
*   **Purpose:** Visually demonstrate the Difference-in-Differences effect.

    *   **Chart Type:** Time-Series Line Chart
    *   **X-axis:** `stream_date` (Granularity: Daily)
    *   **Y-axis:** `total_streams` (Aggregated: SUM or AVG per day)
    *   **Series Breakout:** `is_treatment` (Two lines: Treatment vs. Control)
    *   **Reference Line:** Vertical line at `July 15, 2026` (opt-in date) to highlight the intervention point.
    *   **Title:** "Discovery Mode: Daily Stream Trends (Treatment vs. Control)"
    *   **Annotations:** Callout boxes explaining the pre-period trend, post-period divergence, and the interpretation of the reference line.

---

#### Section 3: Guardrail Metric Deep Dive (Chart 2)

*   **Placement:** Next to or below the Causal Lift chart, easily comparable with the KPI.
*   **Purpose:** Detailed view of listener experience guardrails.

    *   **Chart Type:** (Options: Side-by-side Scorecards, or a Bar Chart)
        *   **Option A (Recommended): Two Scorecards (as discussed)**
            *   Scorecard 1: Treatment Post-Period Skip Rate
            *   Scorecard 2: Control Post-Period Skip Rate
        *   **Option B: Bar Chart**
            *   **Dimension:** `is_treatment`
            *   **Metric:** `daily_skip_rate` (AVG)
            *   **Filter:** `is_post_period = 1`
            *   **Title:** "Listener Experience: Daily Skip Rate Comparison (Post-Period)"
    *   **Annotations:** Text explaining the acceptable range for skip rates and confirming that the guardrail is met if rates are similar.

---

#### Section 4: Algorithm Health (Chart 3)

*   **Placement:** Bottom section, providing supporting evidence for algorithmic engagement.
*   **Purpose:** Show that the algorithm is actively contributing to streams for treated artists.

    *   **Chart Type:** Stacked Bar Chart or Line Chart (Ratio over time)
    *   **Option A (Recommended): Stacked Bar Chart by `stream_date`**
        *   **Dimension:** `stream_date`
        *   **Metric:** `total_streams`
        *   **Breakdown Dimension:** `stream_source` (to show 'algorithmic' vs. 'organic' contribution)
        *   **Filter:** `is_treatment = 1` and `is_post_period = 1` (Focus on treated artists post-intervention)
        *   **Title:** "Algorithmic vs. Organic Streams for Discovery Mode Artists (Post-Period)"
    *   **Option B: Line Chart (Ratio)**
        *   **X-axis:** `stream_date`
        *   **Y-axis:** `algo_streams` / `total_streams` (as a percentage)
        *   **Filter:** `is_treatment = 1` and `is_post_period = 1`
        *   **Title:** "Algorithmic Contribution to Discovery Mode Artist Streams (%)"

---

#### Global Filters/Controls:
*   **Placement:** Top right corner or left sidebar.
*   **Controls:** Date Range Selector (for `stream_date`), `artist_id` selector (if detailed drill-down is desired).

---

### Detailed Configuration Instructions

### Dashboard Title: Discovery Mode Performance & Listener Experience

*   **Component Type:** Text Box
*   **Configuration:**
    *   **Setup Tab:** Simply type `Discovery Mode Performance & Listener Experience` into the text box.
    *   **Style Tab:**
        *   **Font:** Choose a clear, readable font (e.g., 'Roboto', 'Arial').
        *   **Size:** Large (e.g., 36px-48px) for prominence.
        *   **Color:** Dark, contrasting color.
        *   **Alignment:** Center.
        *   **Background & Border:** Optional, align with overall dashboard theme.

### Global Filters/Controls

*   **Component Type:** Date Range Control
*   **Configuration:**
    *   **Setup Tab:**
        *   **Control Field:** `stream_date` (from `analytics_spotify.mart_artist_incrementality`)
        *   **Default Date Range:** 'Auto date range' to encompass all available data, or 'Last 30 days' for a rolling view if preferred.
    *   **Style Tab:** Position prominently, typically top-right or top-left.

---

### Section 1: Executive Summary & Key Results (Manual Entry / Derived from Analysis)

*(These values are results from your Python DiD analysis and are best displayed as static text or scorecards with manually entered values, as they are not direct aggregations Looker Studio can calculate from the raw mart table.)*

1.  **Causal Lift Result**
    *   **Component Type:** Text Box (or Scorecard if Looker Studio allows static value input).
    *   **Configuration:**
        *   **Setup Tab:**
            *   Type `Avg. Daily Incremental Streams per Artist: 7.45`
            *   *(If using a Scorecard and static input is an option, set metric to 7.45 and label as above.)*
        *   **Style Tab:**
            *   **Font:** Bold, large font size (e.g., 24-30px).
            *   **Color:** Emphasize (e.g., green for positive impact).
            *   **Alignment:** Left or Center.

2.  **Statistical Significance**
    *   **Component Type:** Text Box
    *   **Configuration:**
        *   **Setup Tab:** Type `Statistical Significance (p-value): < 0.0001`
        *   **Style Tab:**
            *   **Font:** Regular, slightly smaller than Causal Lift (e.g., 18-20px).
            *   **Color:** Standard text color.
            *   **Alignment:** Left or Center.

---

### Section 2: Core Metrics (Looker Studio Charts/Scorecards from `mart_artist_incrementality`)

#### KPI: Post-Period Treatment Skip Rate (Scorecard)

*   **Component Type:** Scorecard
*   **Configuration:**
    *   **Setup Tab:**
        *   **Data Source:** `analytics_spotify.mart_artist_incrementality`
        *   **Metric:** `daily_skip_rate`
            *   **Aggregation:** `Average`
            *   **Type:** Set to `Number > Percent`
        *   **Filters:**
            *   `is_treatment` **Equal to** `1` (Boolean True)
            *   `is_post_period` **Equal to** `1` (Boolean True)
        *   **Date Range:** Inherit from dashboard filter (or 'Auto').
    *   **Style Tab:**
        *   **Title:** `Treatment Group Post-Period Skip Rate`
        *   **Decimal Precision:** `2`
        *   **Font Size/Color:** As desired for KPIs.
        *   **Comparison:** (Optional) If comparing to a fixed baseline or another metric, configure here.

#### KPI: Post-Period Control Skip Rate (Scorecard)

*   **Component Type:** Scorecard
*   **Configuration:**
    *   **Setup Tab:**
        *   **Data Source:** `analytics_spotify.mart_artist_incrementality`
        *   **Metric:** `daily_skip_rate`
            *   **Aggregation:** `Average`
            *   **Type:** Set to `Number > Percent`
        *   **Filters:**
            *   `is_treatment` **Equal to** `0` (Boolean False)
            *   `is_post_period` **Equal to** `1` (Boolean True)
        *   **Date Range:** Inherit from dashboard filter (or 'Auto').
    *   **Style Tab:**
        *   **Title:** `Control Group Post-Period Skip Rate`
        *   **Decimal Precision:** `2`
        *   **Font Size/Color:** As desired for KPIs.

#### Chart 1: Causal Lift Visualisation (Time-Series Line Chart)

*   **Component Type:** Time series chart
*   **Configuration:**
    *   **Setup Tab:**
        *   **Data Source:** `analytics_spotify.mart_artist_incrementality`
        *   **Date Range Dimension:** `stream_date`
        *   **Dimension:** `stream_date` (Set 'Granularity' to `Day`)
        *   **Breakdown Dimension:** `is_treatment` (Ensure this is treated as a Boolean or Dimension field)
        *   **Metric:** `total_streams`
            *   **Aggregation:** `Sum`
        *   **Sort:** `stream_date`, `Ascending`
        *   **Filters:** None (to show both pre and post periods for all groups).
    *   **Style Tab:**
        *   **Chart Title:** `Discovery Mode: Daily Stream Trends (Treatment vs. Control)`
        *   **Series 1 (is_treatment = 0):** Choose a distinct color (e.g., blue).
        *   **Series 2 (is_treatment = 1):** Choose another distinct color (e.g., orange).
        *   **Missing Data:** Select `Linear interpolation`.
        *   **Axes:**
            *   **Left Y-axis:** `Show axis title` (`Total Streams`). Min `0`.
            *   **X-axis:** `Show axis title` (`Date`).
        *   **Grid:** `Show grid` (optional, for readability).
        *   **Reference Line:**
            *   **Type:** `Date`
            *   **Date:** Select `July 15, 2026`.
            *   **Label:** `Opt-in Date`
            *   **Line Color/Weight/Style:** (e.g., grey, dashed).
        *   **Legend:** Position `Bottom` or `Top`.

#### Chart 3: Algorithm Health (Stacked Bar Chart)

*   **Component Type:** Stacked Bar Chart
*   **Configuration:**
    *   **Setup Tab:**
        *   **Data Source:** `analytics_spotify.mart_artist_incrementality`
        *   **Dimension:** `stream_date` (Set 'Granularity' to `Day`)
        *   **Breakdown Dimension:** `stream_source`
        *   **Metric:** `total_streams`
            *   **Aggregation:** `Sum`
        *   **Filters:**
            *   `is_treatment` **Equal to** `1` (Boolean True)
            *   `is_post_period` **Equal to** `1` (Boolean True)
        *   **Sort:** `stream_date`, `Ascending`.
    *   **Style Tab:**
        *   **Chart Title:** `Algorithmic vs. Organic Streams for Discovery Mode Artists (Post-Period)`
        *   **Bars:** Select `100% Stacking`.
        *   **Colors:** Assign distinct colors for 'algorithmic' (e.g., green) and 'organic' (e.g., grey).
        *   **Show data labels:** `On`.
        *   **Axes:**
            *   **Left Y-axis:** `Show axis title` (`Proportion of Streams`), format as `Number > Percent`.
            *   **X-axis:** `Show axis title` (`Date`).
        *   **Grid:** `Show grid` (optional).
        *   **Legend:** Position `Top` or `Bottom`.

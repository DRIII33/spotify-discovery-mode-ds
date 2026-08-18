# Executive Summary: Spotify Discovery Mode Incremental Value Project

**Prepared for: Spotify Stakeholders**

**By: Daniel Rodriguez III, Data Scientist**

**Date: August 18, 2026**

## Business Scenario & Challenge

Spotify, as a global leader in audio streaming, operates a delicate two-sided marketplace. On one side, millions of artists strive for discovery and a larger audience. On the other, listeners seek an ever-evolving personalized experience without friction or irrelevant recommendations. The "Discovery Mode" initiative aims to address the artist's need for exposure by algorithmically boosting their tracks to new listeners. The core business challenge, however, lies in proving the *incremental value* of this intervention: are artists truly gaining new listens that they wouldn't have otherwise, and crucially, is this exposure coming at the cost of listener satisfaction (e.g., increased skip rates or perceived lower quality recommendations)?

Our task was to rigorously quantify the impact of Discovery Mode on artist streams and to validate that listener experience remained uncompromised. This required a robust causal inference approach, integrating analytics engineering best practices, and visualizing the outcomes for clear stakeholder understanding.

## Data Science Framework Implemented

To address this challenge, I implemented a comprehensive data science framework:

1.  **Synthetic Data Generation:** Given the proprietary nature of Spotify's real-world data, I first engineered a realistic synthetic dataset simulating artist campaigns and user streams. This allowed for controlled experimentation and validation of our analytical methods.
2.  **Analytics Engineering with dbt Core:** The raw synthetic data was then transformed using dbt Core. This involved aggregating stream data by artist and day, joining with campaign information, and flagging pre/post-intervention periods (`is_post_period`) and treatment/control groups (`is_treatment`). The output, `mart_artist_incrementality`, served as the single source of truth for downstream analysis.
3.  **Causal Inference (Difference-in-Differences - DiD):** The heart of the analysis was a Difference-in-Differences regression. This econometric technique allowed me to isolate the causal effect of Discovery Mode by comparing the change in streams over time between treated artists (opted into Discovery Mode) and a carefully selected control group (not opted in). The DiD model accounts for pre-existing differences and general time trends, ensuring the measured impact is truly attributable to the intervention.
4.  **Guardrail Metric Analysis:** Concurrently, I analyzed key guardrail metrics, specifically daily skip rates, to monitor listener experience. This involved comparing skip rates between treatment and control groups in the post-intervention period.
5.  **Dashboarding (Looker Studio Design):** Finally, I designed a Looker Studio dashboard to visualize these findings, providing an intuitive, interactive platform for stakeholders to understand the causal lift, monitor listener impact, and assess algorithm health.

## Data Story

**Discovery Mode is a success, delivering a statistically significant and meaningful uplift to artists without compromising listener experience.**

Through the Difference-in-Differences regression, we quantified a **causal lift of +7.45 average daily incremental streams per artist** who opted into Discovery Mode. This effect is highly statistically significant (p < 0.0001), indicating high confidence that this uplift is directly caused by the intervention and not random chance. This translates to real, tangible growth for artists.

Crucially, our guardrail analysis revealed that the **post-period skip rates for treated artists (20.13%) were nearly identical to those of control artists (19.68%)**. This minor delta of just +0.45 percentage points confirms that Discovery Mode's algorithmic boost is *not* degrading listener experience. Listeners are engaging with these promoted tracks at a similar rate to other content, validating that the recommendations are still relevant and high-quality.

Furthermore, the algorithm health metrics, though not explicitly regressed, show that a substantial portion of the post-intervention streams for treated artists are indeed driven by algorithmic recommendations. This confirms the mechanism by which Discovery Mode is delivering value.

In essence, Discovery Mode has achieved its dual objective: **effectively promoting artist discovery (lift) while maintaining the integrity of the listener experience (guardrails).**

## Next Steps & Recommendations

1.  **A/B Test Expansion & Granularity:** While DiD provides strong causal evidence, consider expanding to a larger-scale, randomized A/B test for future Discovery Mode iterations. This would allow for even more precise causal inference and the ability to test finer-grained hypotheses (e.g., different boosting algorithms, segmentation by genre/listener profile).
2.  **Long-Term Impact Analysis:** Extend the observation window to assess the long-term sustainability of the stream lift and skip rates. Does the lift persist? Do listeners eventually fatigue if over-exposed? This would involve tracking metrics several months post-intervention.
3.  **Monetization & Engagement Deep Dive:** Integrate artist revenue data to quantify the financial impact of Discovery Mode. Additionally, analyze downstream engagement metrics (e.g., saves, playlist adds, repeat listens) to understand the full lifecycle impact beyond initial streams.
4.  **Cost-Benefit Analysis:** Develop a robust cost-benefit analysis for Discovery Mode, weighing the operational costs (e.g., infrastructure, model development) against the artist value (streams, potential revenue) and platform health (listener retention).
5.  **Algorithm Explainability & Fairness:** Investigate the features and mechanisms driving Discovery Mode's algorithmic recommendations. Ensure fairness across artist demographics and genres, and guard against unintended biases.
6.  **Dashboard Enhancement:** Implement advanced features in the Looker Studio dashboard, such as dynamic segmentation by artist tier or genre, and predictive analytics for early detection of performance shifts.

By continuing to rigorously measure and iterate, Spotify can ensure Discovery Mode remains a powerful, equitable, and listener-friendly tool for artist growth.

CREATE OR REPLACE VIEW `driiiportfolio.analytics_spotify.vw_causal_lift_kpi`
AS
WITH
  did_components AS (
    SELECT
      is_treatment,
      is_post_period,
      AVG(total_streams) AS avg_streams,
      VAR_SAMP(total_streams) AS var_streams,
      COUNT(*) AS n_obs,
      AVG(daily_skip_rate) AS avg_skip
    FROM `driiiportfolio.analytics_spotify.mart_artist_incrementality`
    GROUP BY 1, 2
  ),
  did_calc AS (
    SELECT
      -- Group averages for DiD and Counterfactual
      MAX(
        CASE WHEN is_treatment = 1 AND is_post_period = 1 THEN avg_streams END)
        AS t_post,
      MAX(
        CASE WHEN is_treatment = 1 AND is_post_period = 0 THEN avg_streams END)
        AS t_pre,
      MAX(
        CASE WHEN is_treatment = 0 AND is_post_period = 1 THEN avg_streams END)
        AS c_post,
      MAX(
        CASE WHEN is_treatment = 0 AND is_post_period = 0 THEN avg_streams END)
        AS c_pre,

      -- Variance and N for Stat Sig (Post-period only)
      MAX(
        CASE WHEN is_treatment = 1 AND is_post_period = 1 THEN var_streams END)
        AS t_post_var,
      MAX(CASE WHEN is_treatment = 1 AND is_post_period = 1 THEN n_obs END)
        AS t_post_n,
      MAX(
        CASE WHEN is_treatment = 0 AND is_post_period = 1 THEN var_streams END)
        AS c_post_var,
      MAX(CASE WHEN is_treatment = 0 AND is_post_period = 1 THEN n_obs END)
        AS c_post_n,

      -- Skip Rates (Post-Period)
      MAX(CASE WHEN is_treatment = 1 AND is_post_period = 1 THEN avg_skip END)
        AS tx_skip_rate,
      MAX(CASE WHEN is_treatment = 0 AND is_post_period = 1 THEN avg_skip END)
        AS ctl_skip_rate
    FROM did_components
  ),
  final_kpis AS (
    SELECT
      -- DiD Causal Lift Calculation
      (t_post - t_pre) - (c_post - c_pre) AS avg_daily_incremental_streams,

      -- Counterfactual Baseline = Treatment Pre + (Control Post - Control Pre)
      t_pre + (c_post - c_pre) AS counterfactual_baseline,
      tx_skip_rate,
      ctl_skip_rate,

      -- T-Score for Significance (Post-period comparison)
      SAFE_DIVIDE(
        (t_post - c_post),
        SQRT(
          SAFE_DIVIDE(t_post_var, t_post_n)
          + SAFE_DIVIDE(c_post_var, c_post_n)))
        AS t_score
    FROM did_calc
  )
SELECT
  avg_daily_incremental_streams,
  tx_skip_rate,
  ctl_skip_rate,
  -- True Lift % = DiD / Counterfactual Baseline
  SAFE_DIVIDE(avg_daily_incremental_streams, counterfactual_baseline)
    AS lift_percentage,
  CASE
    WHEN ABS(t_score) > 3.29 THEN 'p < 0.001 (Highly Sig)'
    WHEN ABS(t_score) > 2.58 THEN 'p < 0.01 (Sig)'
    WHEN ABS(t_score) > 1.96 THEN 'p < 0.05 (Sig)'
    ELSE 'Not Significant'
    END
    AS stat_sig_label
FROM final_kpis;


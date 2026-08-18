--This dbt model transforms raw stream and campaign data into `mart_artist_incrementality`, which is used for causal inference and dashboarding. It joins daily artist stream aggregates with campaign flags to create `is_treatment` and `is_post_period` flags.


WITH daily_artist_streams AS (
    SELECT
        s.stream_date,
        s.artist_id,
        COUNT(*) as total_streams,
        SUM(CASE WHEN s.stream_source = 'algorithmic' THEN 1 ELSE 0 END) as algo_streams,
        AVG(s.is_skipped) as daily_skip_rate
    FROM `driiiportfolio.raw_spotify.user_streams` s
    GROUP BY 1, 2
),

campaign_flags AS (
    SELECT
        artist_id,
        is_treatment,
        opt_in_date
    FROM `driiiportfolio.raw_spotify.artist_campaigns`
)

SELECT
    d.stream_date,
    d.artist_id,
    c.is_treatment,
    CASE WHEN d.stream_date >= c.opt_in_date THEN 1 ELSE 0 END as is_post_period,
    d.total_streams,
    d.algo_streams,
    d.daily_skip_rate
FROM daily_artist_streams d
LEFT JOIN campaign_flags c ON d.artist_id = c.artist_id;

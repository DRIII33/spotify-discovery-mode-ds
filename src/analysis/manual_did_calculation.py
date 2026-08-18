import pandas as pd
from google.cloud import bigquery
from google.colab import auth # For Colab authentication

# Authenticate to GCP (if running in Colab)
auth.authenticate_user()

client = bigquery.Client(project='driiiportfolio') # Replace with your GCP project ID

query_did_components = """
SELECT
    is_treatment,
    is_post_period,
    AVG(total_streams) AS avg_total_streams
FROM
    `driiiportfolio.analytics_spotify.mart_artist_incrementality`
GROUP BY
    is_treatment,
    is_post_period
ORDER BY
    is_treatment,
    is_post_period
"""

df_did_components = client.query(query_did_components).to_dataframe()
print("Average streams by group:")
print(df_did_components)

# Extract the average streams for each group
# Ensure these rows exist before accessing .iloc[0]

avg_t_post = df_did_components[(df_did_components['is_treatment'] == 1) & (df_did_components['is_post_period'] == 1)]['avg_total_streams'].iloc[0]
avg_t_pre = df_did_components[(df_did_components['is_treatment'] == 1) & (df_did_components['is_post_period'] == 0)]['avg_total_streams'].iloc[0]
avg_c_post = df_did_components[(df_did_components['is_treatment'] == 0) & (df_did_components['is_post_period'] == 1)]['avg_total_streams'].iloc[0]
avg_c_pre = df_did_components[(df_did_components['is_treatment'] == 0) & (df_did_components['is_post_period'] == 0)]['avg_total_streams'].iloc[0]

# Calculate the Difference-in-Differences (DiD)
did_effect = (avg_t_post - avg_t_pre) - (avg_c_post - avg_c_pre)

print(f"\nManually calculated DiD Causal Lift: {did_effect:.2f} streams per artist")

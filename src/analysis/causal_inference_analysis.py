import statsmodels.formula.api as smf
import pandas as pd
from google.cloud import bigquery
from google.colab import auth # For Colab authentication

# Authenticate to GCP (if running in Colab)
auth.authenticate_user()

client = bigquery.Client(project='driiiportfolio') # Replace with your GCP project ID

# Fetch the dbt mart
query = """SELECT * FROM `driiiportfolio.analytics_spotify.mart_artist_incrementality`"""
df = client.query(query).to_dataframe()

# 1. Causal Inference: Difference-in-Differences Regression
print("--- Discovery Mode Incremental Lift Analysis (DiD) ---")
did_model = smf.ols('total_streams ~ is_treatment * is_post_period', data=df).fit()
print(did_model.summary())

# Extracting the causal impact
causal_lift = did_model.params['is_treatment:is_post_period']
p_value = did_model.pvalues['is_treatment:is_post_period']

print(f"\nBusiness Readout:")
print(f"Discovery mode drove an average daily incremental lift of {causal_lift:.2f} streams per artist.")
print(f"Statistical Significance (p-value): {p_value:.4f}")

# 2. Guardrail Metric Analysis (Listener Experience)
treatment_post = df[(df['is_treatment'] == 1) & (df['is_post_period'] == 1)]
control_post = df[(df['is_treatment'] == 0) & (df['is_post_period'] == 1)]

print("\n--- Guardrail Metrics (Cannibalization & Quality) ---")
print(f"Treatment Post-Period Skip Rate: {treatment_post['daily_skip_rate'].mean():.2%}")
print(f"Control Post-Period Skip Rate: {control_post['daily_skip_rate'].mean():.2%}")

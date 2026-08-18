from google.colab import auth
from google.cloud import bigquery
import pandas as pd
import numpy as np
import datetime

# Authenticate to GCP
# In a local environment, you might use service account keys or gcloud CLI for authentication.
auth.authenticate_user()
project_id = 'driiiportfolio' # Replace with your GCP project ID
client = bigquery.Client(project=project_id)

# 1. Generate Artist Campaigns (Control vs Treatment)
np.random.seed(42)
artist_ids = [f"ARTIST_{i}" for i in range(1, 101)]
treatment = np.random.choice([0, 1], size=100) # 1 = Discovery Mode Opt-In
campaigns = pd.DataFrame({
    'artist_id': artist_ids,
    'is_treatment': treatment,
    'opt_in_date': datetime.date(2026, 7, 15)
})

# 2. Generate User Streams (Pre and Post Opt-In)
dates = pd.date_range(start='2026-07-01', end='2026-07-31')
streams_data = []

for date in dates:
    is_post = date.date() >= datetime.date(2026, 7, 15)
    for artist, trt in zip(artist_ids, treatment):
        # Base daily streams
        base_streams = np.random.normal(500, 50)
        # Treatment effect: +15% lift if in Discovery Mode post-opt-in
        lift = 1.15 if (trt == 1 and is_post) else 1.0
        daily_streams = int(base_streams * lift)
        
        # Algorithmic source probability
        algo_prob = 0.4 if (trt == 1 and is_post) else 0.2
        
        for _ in range(int(daily_streams / 10)): # Downscaled for Colab memory
            streams_data.append({
                'stream_date': date,
                'artist_id': artist,
                'stream_source': np.random.choice(['algorithmic', 'organic'], p=[algo_prob, 1-algo_prob]),
                'is_skipped': np.random.choice([0, 1], p=[0.8, 0.2]) # 20% skip rate
            })

streams = pd.DataFrame(streams_data)

# 3. Load to BigQuery
# Ensure 'raw_spotify' dataset exists in your project.
campaigns.to_gbq(destination_table='raw_spotify.artist_campaigns', project_id=project_id, if_exists='replace')
streams.to_gbq(destination_table='raw_spotify.user_streams', project_id=project_id, if_exists='replace')
print("Synthetic data loaded to BigQuery successfully.")

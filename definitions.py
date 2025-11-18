# feature_repo/definitions.py

from datetime import timedelta
from feast import Entity, FeatureService, FeatureView, Field, FileSource, PushSource, RequestSource
from feast.types import Float32, Int64

# 1. Define the Entity (The "Key")
# We track features by "vehicle_id"
vehicle = Entity(name="vehicle_id", join_keys=["vehicle_id"])

# 2. Define the Data Source (The Parquet file we just made)
driver_stats_source = FileSource(
    name="driver_stats_source",
    path="data/driver_stats.parquet",
    timestamp_field="event_timestamp",
)

# 3. Define the Feature View (The "Schema")
# This tells Feast: "These columns in the parquet file are features."
driver_stats_view = FeatureView(
    name="driver_stats_view",
    entities=[vehicle],
    ttl=timedelta(days=1), # How long do we trust this data?
    schema=[
        Field(name="avg_speed", dtype=Float32),
        Field(name="max_rpm", dtype=Float32),
        Field(name="hard_brakes", dtype=Int64),
    ],
    online=True, # Enable online retrieval (Redis)
    source=driver_stats_source,
    tags={"team": "fleet_ops"},
)

# 4. Define a Feature Service (A group of features for a specific model)
driver_activity_service = FeatureService(
    name="driver_activity_service",
    features=[driver_stats_view]
)
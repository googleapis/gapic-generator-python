# -*- coding: utf-8 -*-
# Copyright 2024 Google LLC
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#
# Generated code. DO NOT EDIT!
#
# Snippet for BatchCreateFeatures
# NOTE: This snippet has been automatically generated for illustrative purposes only.
# It may require modifications to work in your environment.

# To install the latest published package dependency, execute the following:
#   python3 -m pip install google-cloud-aiplatform


# [START aiplatform_v1_generated_FeaturestoreService_BatchCreateFeatures_sync]
# This snippet has been automatically generated and should be regarded as a
# code template only.
# It will require modifications to work:
# - It may require correct/in-range values for request initialization.
# - It may require specifying regional endpoints when creating the service
#   client as shown in:
#   https://googleapis.dev/python/google-api-core/latest/client_options.html
from google.cloud import aiplatform_v1


def sample_batch_create_features():
    # Create a client
    client = aiplatform_v1.FeaturestoreServiceClient()

    # Initialize request argument(s)
    requests = aiplatform_v1.CreateFeatureRequest()
    requests.parent = "parent_value"
    requests.feature.name = "name_value"
    requests.feature.description = "description_value"
    requests.feature.value_type = "BYTES"
    requests.feature.create_time.seconds = 751
    requests.feature.create_time.nanos = 543
    requests.feature.update_time.seconds = 751
    requests.feature.update_time.nanos = 543
    requests.feature.labels.key = "key_value"
    requests.feature.labels.value = "value_value"
    requests.feature.etag = "etag_value"
    requests.feature.disable_monitoring = True
    requests.feature.monitoring_stats_anomalies.objective = "SNAPSHOT_ANALYSIS"
    requests.feature.monitoring_stats_anomalies.feature_stats_anomaly.score = 0.54
    requests.feature.monitoring_stats_anomalies.feature_stats_anomaly.stats_uri = "stats_uri_value"
    requests.feature.monitoring_stats_anomalies.feature_stats_anomaly.anomaly_uri = "anomaly_uri_value"
    requests.feature.monitoring_stats_anomalies.feature_stats_anomaly.distribution_deviation = 0.23700000000000002
    requests.feature.monitoring_stats_anomalies.feature_stats_anomaly.anomaly_detection_threshold = 0.28750000000000003
    requests.feature.monitoring_stats_anomalies.feature_stats_anomaly.start_time.seconds = 751
    requests.feature.monitoring_stats_anomalies.feature_stats_anomaly.start_time.nanos = 543
    requests.feature.monitoring_stats_anomalies.feature_stats_anomaly.end_time.seconds = 751
    requests.feature.monitoring_stats_anomalies.feature_stats_anomaly.end_time.nanos = 543
    requests.feature.version_column_name = "version_column_name_value"
    requests.feature.point_of_contact = "point_of_contact_value"
    requests.feature_id = "feature_id_value"

    request = aiplatform_v1.BatchCreateFeaturesRequest(
        parent="parent_value",
        requests=requests,
    )

    # Make the request
    operation = client.batch_create_features(request=request)

    print("Waiting for operation to complete...")

    response = operation.result()

    # Handle the response
    print(response)

# [END aiplatform_v1_generated_FeaturestoreService_BatchCreateFeatures_sync]

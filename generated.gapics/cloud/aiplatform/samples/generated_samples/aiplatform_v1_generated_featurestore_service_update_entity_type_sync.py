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
# Snippet for UpdateEntityType
# NOTE: This snippet has been automatically generated for illustrative purposes only.
# It may require modifications to work in your environment.

# To install the latest published package dependency, execute the following:
#   python3 -m pip install google-cloud-aiplatform


# [START aiplatform_v1_generated_FeaturestoreService_UpdateEntityType_sync]
# This snippet has been automatically generated and should be regarded as a
# code template only.
# It will require modifications to work:
# - It may require correct/in-range values for request initialization.
# - It may require specifying regional endpoints when creating the service
#   client as shown in:
#   https://googleapis.dev/python/google-api-core/latest/client_options.html
from google.cloud import aiplatform_v1


def sample_update_entity_type():
    # Create a client
    client = aiplatform_v1.FeaturestoreServiceClient()

    # Initialize request argument(s)
    entity_type = aiplatform_v1.EntityType()
    entity_type.name = "name_value"
    entity_type.description = "description_value"
    entity_type.create_time.seconds = 751
    entity_type.create_time.nanos = 543
    entity_type.update_time.seconds = 751
    entity_type.update_time.nanos = 543
    entity_type.labels.key = "key_value"
    entity_type.labels.value = "value_value"
    entity_type.etag = "etag_value"
    entity_type.monitoring_config.snapshot_analysis.disabled = True
    entity_type.monitoring_config.snapshot_analysis.monitoring_interval_days = 2586
    entity_type.monitoring_config.snapshot_analysis.staleness_days = 1506
    entity_type.monitoring_config.import_features_analysis.state = "DISABLED"
    entity_type.monitoring_config.import_features_analysis.anomaly_detection_baseline = "PREVIOUS_IMPORT_FEATURES_STATS"
    entity_type.monitoring_config.numerical_threshold_config.value = 0.541
    entity_type.monitoring_config.categorical_threshold_config.value = 0.541
    entity_type.offline_storage_ttl_days = 2554

    update_mask = aiplatform_v1.FieldMask()
    update_mask.paths = ['paths_value1', 'paths_value2']

    request = aiplatform_v1.UpdateEntityTypeRequest(
        entity_type=entity_type,
        update_mask=update_mask,
    )

    # Make the request
    response = client.update_entity_type(request=request)

    # Handle the response
    print(response)

# [END aiplatform_v1_generated_FeaturestoreService_UpdateEntityType_sync]

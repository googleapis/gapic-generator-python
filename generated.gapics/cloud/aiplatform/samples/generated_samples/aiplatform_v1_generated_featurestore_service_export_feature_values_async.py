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
# Snippet for ExportFeatureValues
# NOTE: This snippet has been automatically generated for illustrative purposes only.
# It may require modifications to work in your environment.

# To install the latest published package dependency, execute the following:
#   python3 -m pip install google-cloud-aiplatform


# [START aiplatform_v1_generated_FeaturestoreService_ExportFeatureValues_async]
# This snippet has been automatically generated and should be regarded as a
# code template only.
# It will require modifications to work:
# - It may require correct/in-range values for request initialization.
# - It may require specifying regional endpoints when creating the service
#   client as shown in:
#   https://googleapis.dev/python/google-api-core/latest/client_options.html
from google.cloud import aiplatform_v1


async def sample_export_feature_values():
    # Create a client
    client = aiplatform_v1.FeaturestoreServiceAsyncClient()

    # Initialize request argument(s)
    snapshot_export = aiplatform_v1.SnapshotExport()
    snapshot_export.snapshot_time.seconds = 751
    snapshot_export.snapshot_time.nanos = 543
    snapshot_export.start_time.seconds = 751
    snapshot_export.start_time.nanos = 543

    full_export = aiplatform_v1.FullExport()
    full_export.start_time.seconds = 751
    full_export.start_time.nanos = 543
    full_export.end_time.seconds = 751
    full_export.end_time.nanos = 543

    destination = aiplatform_v1.FeatureValueDestination()
    destination.bigquery_destination.output_uri = "output_uri_value"
    destination.tfrecord_destination.gcs_destination.output_uri_prefix = "output_uri_prefix_value"
    destination.csv_destination.gcs_destination.output_uri_prefix = "output_uri_prefix_value"

    feature_selector = aiplatform_v1.FeatureSelector()
    feature_selector.id_matcher.ids = ['ids_value1', 'ids_value2']

    settings = aiplatform_v1.DestinationFeatureSetting()
    settings.feature_id = "feature_id_value"
    settings.destination_field = "destination_field_value"

    request = aiplatform_v1.ExportFeatureValuesRequest(
        snapshot_export=snapshot_export,
        full_export=full_export,
        entity_type="entity_type_value",
        destination=destination,
        feature_selector=feature_selector,
        settings=settings,
    )

    # Make the request
    operation = client.export_feature_values(request=request)

    print("Waiting for operation to complete...")

    response = (await operation).result()

    # Handle the response
    print(response)

# [END aiplatform_v1_generated_FeaturestoreService_ExportFeatureValues_async]

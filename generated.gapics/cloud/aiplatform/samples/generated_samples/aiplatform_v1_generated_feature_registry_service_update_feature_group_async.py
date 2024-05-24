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
# Snippet for UpdateFeatureGroup
# NOTE: This snippet has been automatically generated for illustrative purposes only.
# It may require modifications to work in your environment.

# To install the latest published package dependency, execute the following:
#   python3 -m pip install google-cloud-aiplatform


# [START aiplatform_v1_generated_FeatureRegistryService_UpdateFeatureGroup_async]
# This snippet has been automatically generated and should be regarded as a
# code template only.
# It will require modifications to work:
# - It may require correct/in-range values for request initialization.
# - It may require specifying regional endpoints when creating the service
#   client as shown in:
#   https://googleapis.dev/python/google-api-core/latest/client_options.html
from google.cloud import aiplatform_v1


async def sample_update_feature_group():
    # Create a client
    client = aiplatform_v1.FeatureRegistryServiceAsyncClient()

    # Initialize request argument(s)
    feature_group = aiplatform_v1.FeatureGroup()
    feature_group.big_query.big_query_source.input_uri = "input_uri_value"
    feature_group.big_query.entity_id_columns = ['entity_id_columns_value1', 'entity_id_columns_value2']
    feature_group.name = "name_value"
    feature_group.create_time.seconds = 751
    feature_group.create_time.nanos = 543
    feature_group.update_time.seconds = 751
    feature_group.update_time.nanos = 543
    feature_group.etag = "etag_value"
    feature_group.labels.key = "key_value"
    feature_group.labels.value = "value_value"
    feature_group.description = "description_value"

    update_mask = aiplatform_v1.FieldMask()
    update_mask.paths = ['paths_value1', 'paths_value2']

    request = aiplatform_v1.UpdateFeatureGroupRequest(
        feature_group=feature_group,
        update_mask=update_mask,
    )

    # Make the request
    operation = client.update_feature_group(request=request)

    print("Waiting for operation to complete...")

    response = (await operation).result()

    # Handle the response
    print(response)

# [END aiplatform_v1_generated_FeatureRegistryService_UpdateFeatureGroup_async]

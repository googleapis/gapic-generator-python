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
# Snippet for WriteFeatureValues
# NOTE: This snippet has been automatically generated for illustrative purposes only.
# It may require modifications to work in your environment.

# To install the latest published package dependency, execute the following:
#   python3 -m pip install google-cloud-aiplatform


# [START aiplatform_v1_generated_FeaturestoreOnlineServingService_WriteFeatureValues_sync]
# This snippet has been automatically generated and should be regarded as a
# code template only.
# It will require modifications to work:
# - It may require correct/in-range values for request initialization.
# - It may require specifying regional endpoints when creating the service
#   client as shown in:
#   https://googleapis.dev/python/google-api-core/latest/client_options.html
from google.cloud import aiplatform_v1


def sample_write_feature_values():
    # Create a client
    client = aiplatform_v1.FeaturestoreOnlineServingServiceClient()

    # Initialize request argument(s)
    payloads = aiplatform_v1.WriteFeatureValuesPayload()
    payloads.entity_id = "entity_id_value"
    payloads.feature_values.key = "key_value"
    payloads.feature_values.value.bool_value = True
    payloads.feature_values.value.double_value = 0.12710000000000002
    payloads.feature_values.value.int64_value = 1073
    payloads.feature_values.value.string_value = "string_value_value"
    payloads.feature_values.value.bool_array_value.values = [True, True]
    payloads.feature_values.value.double_array_value.values = [0.657, 0.658]
    payloads.feature_values.value.int64_array_value.values = [657, 658]
    payloads.feature_values.value.string_array_value.values = ['values_value1', 'values_value2']
    payloads.feature_values.value.bytes_value = b'bytes_value_blob'
    payloads.feature_values.value.metadata.generate_time.seconds = 751
    payloads.feature_values.value.metadata.generate_time.nanos = 543

    request = aiplatform_v1.WriteFeatureValuesRequest(
        entity_type="entity_type_value",
        payloads=payloads,
    )

    # Make the request
    response = client.write_feature_values(request=request)

    # Handle the response
    print(response)

# [END aiplatform_v1_generated_FeaturestoreOnlineServingService_WriteFeatureValues_sync]

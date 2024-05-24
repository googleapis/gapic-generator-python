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
# Snippet for CreateFeaturestore
# NOTE: This snippet has been automatically generated for illustrative purposes only.
# It may require modifications to work in your environment.

# To install the latest published package dependency, execute the following:
#   python3 -m pip install google-cloud-aiplatform


# [START aiplatform_v1_generated_FeaturestoreService_CreateFeaturestore_async]
# This snippet has been automatically generated and should be regarded as a
# code template only.
# It will require modifications to work:
# - It may require correct/in-range values for request initialization.
# - It may require specifying regional endpoints when creating the service
#   client as shown in:
#   https://googleapis.dev/python/google-api-core/latest/client_options.html
from google.cloud import aiplatform_v1


async def sample_create_featurestore():
    # Create a client
    client = aiplatform_v1.FeaturestoreServiceAsyncClient()

    # Initialize request argument(s)
    featurestore = aiplatform_v1.Featurestore()
    featurestore.name = "name_value"
    featurestore.create_time.seconds = 751
    featurestore.create_time.nanos = 543
    featurestore.update_time.seconds = 751
    featurestore.update_time.nanos = 543
    featurestore.etag = "etag_value"
    featurestore.labels.key = "key_value"
    featurestore.labels.value = "value_value"
    featurestore.online_serving_config.fixed_node_count = 1693
    featurestore.online_serving_config.scaling.min_node_count = 1489
    featurestore.online_serving_config.scaling.max_node_count = 1491
    featurestore.online_serving_config.scaling.cpu_utilization_target = 2377
    featurestore.state = "UPDATING"
    featurestore.online_storage_ttl_days = 2460
    featurestore.encryption_spec.kms_key_name = "kms_key_name_value"

    request = aiplatform_v1.CreateFeaturestoreRequest(
        parent="parent_value",
        featurestore=featurestore,
        featurestore_id="featurestore_id_value",
    )

    # Make the request
    operation = client.create_featurestore(request=request)

    print("Waiting for operation to complete...")

    response = (await operation).result()

    # Handle the response
    print(response)

# [END aiplatform_v1_generated_FeaturestoreService_CreateFeaturestore_async]

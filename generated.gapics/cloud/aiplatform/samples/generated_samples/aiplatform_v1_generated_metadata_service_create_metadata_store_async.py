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
# Snippet for CreateMetadataStore
# NOTE: This snippet has been automatically generated for illustrative purposes only.
# It may require modifications to work in your environment.

# To install the latest published package dependency, execute the following:
#   python3 -m pip install google-cloud-aiplatform


# [START aiplatform_v1_generated_MetadataService_CreateMetadataStore_async]
# This snippet has been automatically generated and should be regarded as a
# code template only.
# It will require modifications to work:
# - It may require correct/in-range values for request initialization.
# - It may require specifying regional endpoints when creating the service
#   client as shown in:
#   https://googleapis.dev/python/google-api-core/latest/client_options.html
from google.cloud import aiplatform_v1


async def sample_create_metadata_store():
    # Create a client
    client = aiplatform_v1.MetadataServiceAsyncClient()

    # Initialize request argument(s)
    metadata_store = aiplatform_v1.MetadataStore()
    metadata_store.name = "name_value"
    metadata_store.create_time.seconds = 751
    metadata_store.create_time.nanos = 543
    metadata_store.update_time.seconds = 751
    metadata_store.update_time.nanos = 543
    metadata_store.encryption_spec.kms_key_name = "kms_key_name_value"
    metadata_store.description = "description_value"
    metadata_store.state.disk_utilization_bytes = 2380

    request = aiplatform_v1.CreateMetadataStoreRequest(
        parent="parent_value",
        metadata_store=metadata_store,
        metadata_store_id="metadata_store_id_value",
    )

    # Make the request
    operation = client.create_metadata_store(request=request)

    print("Waiting for operation to complete...")

    response = (await operation).result()

    # Handle the response
    print(response)

# [END aiplatform_v1_generated_MetadataService_CreateMetadataStore_async]

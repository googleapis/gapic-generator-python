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
# Snippet for CreateDatasetVersion
# NOTE: This snippet has been automatically generated for illustrative purposes only.
# It may require modifications to work in your environment.

# To install the latest published package dependency, execute the following:
#   python3 -m pip install google-cloud-aiplatform


# [START aiplatform_v1_generated_DatasetService_CreateDatasetVersion_async]
# This snippet has been automatically generated and should be regarded as a
# code template only.
# It will require modifications to work:
# - It may require correct/in-range values for request initialization.
# - It may require specifying regional endpoints when creating the service
#   client as shown in:
#   https://googleapis.dev/python/google-api-core/latest/client_options.html
from google.cloud import aiplatform_v1


async def sample_create_dataset_version():
    # Create a client
    client = aiplatform_v1.DatasetServiceAsyncClient()

    # Initialize request argument(s)
    dataset_version = aiplatform_v1.DatasetVersion()
    dataset_version.name = "name_value"
    dataset_version.create_time.seconds = 751
    dataset_version.create_time.nanos = 543
    dataset_version.update_time.seconds = 751
    dataset_version.update_time.nanos = 543
    dataset_version.etag = "etag_value"
    dataset_version.big_query_dataset_name = "big_query_dataset_name_value"
    dataset_version.display_name = "display_name_value"
    dataset_version.metadata.null_value = "NULL_VALUE"
    dataset_version.metadata.number_value = 0.1285
    dataset_version.metadata.string_value = "string_value_value"
    dataset_version.metadata.bool_value = True
    dataset_version.metadata.struct_value.fields.key = "key_value"
    dataset_version.metadata.struct_value.fields.value = "struct_pb2.Value(null_value=struct_pb2.NullValue.NULL_VALUE)"
    dataset_version.metadata.list_value.values = "[struct_pb2.Value(null_value=struct_pb2.NullValue.NULL_VALUE)]"

    request = aiplatform_v1.CreateDatasetVersionRequest(
        parent="parent_value",
        dataset_version=dataset_version,
    )

    # Make the request
    operation = client.create_dataset_version(request=request)

    print("Waiting for operation to complete...")

    response = (await operation).result()

    # Handle the response
    print(response)

# [END aiplatform_v1_generated_DatasetService_CreateDatasetVersion_async]

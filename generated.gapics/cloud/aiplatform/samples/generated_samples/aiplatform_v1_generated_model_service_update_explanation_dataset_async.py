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
# Snippet for UpdateExplanationDataset
# NOTE: This snippet has been automatically generated for illustrative purposes only.
# It may require modifications to work in your environment.

# To install the latest published package dependency, execute the following:
#   python3 -m pip install google-cloud-aiplatform


# [START aiplatform_v1_generated_ModelService_UpdateExplanationDataset_async]
# This snippet has been automatically generated and should be regarded as a
# code template only.
# It will require modifications to work:
# - It may require correct/in-range values for request initialization.
# - It may require specifying regional endpoints when creating the service
#   client as shown in:
#   https://googleapis.dev/python/google-api-core/latest/client_options.html
from google.cloud import aiplatform_v1


async def sample_update_explanation_dataset():
    # Create a client
    client = aiplatform_v1.ModelServiceAsyncClient()

    # Initialize request argument(s)
    examples = aiplatform_v1.Examples()
    examples.example_gcs_source.data_format = "JSONL"
    examples.example_gcs_source.gcs_source.uris = ['uris_value1', 'uris_value2']
    examples.nearest_neighbor_search_config.null_value = "NULL_VALUE"
    examples.nearest_neighbor_search_config.number_value = 0.1285
    examples.nearest_neighbor_search_config.string_value = "string_value_value"
    examples.nearest_neighbor_search_config.bool_value = True
    examples.nearest_neighbor_search_config.struct_value.fields.key = "key_value"
    examples.nearest_neighbor_search_config.struct_value.fields.value = "struct_pb2.Value(null_value=struct_pb2.NullValue.NULL_VALUE)"
    examples.nearest_neighbor_search_config.list_value.values = "[struct_pb2.Value(null_value=struct_pb2.NullValue.NULL_VALUE)]"
    examples.presets.query = "FAST"
    examples.presets.modality = "TABULAR"
    examples.neighbor_count = 1494

    request = aiplatform_v1.UpdateExplanationDatasetRequest(
        model="model_value",
        examples=examples,
    )

    # Make the request
    operation = client.update_explanation_dataset(request=request)

    print("Waiting for operation to complete...")

    response = (await operation).result()

    # Handle the response
    print(response)

# [END aiplatform_v1_generated_ModelService_UpdateExplanationDataset_async]

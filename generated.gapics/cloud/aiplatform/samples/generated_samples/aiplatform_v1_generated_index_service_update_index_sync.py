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
# Snippet for UpdateIndex
# NOTE: This snippet has been automatically generated for illustrative purposes only.
# It may require modifications to work in your environment.

# To install the latest published package dependency, execute the following:
#   python3 -m pip install google-cloud-aiplatform


# [START aiplatform_v1_generated_IndexService_UpdateIndex_sync]
# This snippet has been automatically generated and should be regarded as a
# code template only.
# It will require modifications to work:
# - It may require correct/in-range values for request initialization.
# - It may require specifying regional endpoints when creating the service
#   client as shown in:
#   https://googleapis.dev/python/google-api-core/latest/client_options.html
from google.cloud import aiplatform_v1


def sample_update_index():
    # Create a client
    client = aiplatform_v1.IndexServiceClient()

    # Initialize request argument(s)
    index = aiplatform_v1.Index()
    index.name = "name_value"
    index.display_name = "display_name_value"
    index.description = "description_value"
    index.metadata_schema_uri = "metadata_schema_uri_value"
    index.metadata.null_value = "NULL_VALUE"
    index.metadata.number_value = 0.1285
    index.metadata.string_value = "string_value_value"
    index.metadata.bool_value = True
    index.metadata.struct_value.fields.key = "key_value"
    index.metadata.struct_value.fields.value = "struct_pb2.Value(null_value=struct_pb2.NullValue.NULL_VALUE)"
    index.metadata.list_value.values = "[struct_pb2.Value(null_value=struct_pb2.NullValue.NULL_VALUE)]"
    index.deployed_indexes.index_endpoint = "index_endpoint_value"
    index.deployed_indexes.deployed_index_id = "deployed_index_id_value"
    index.deployed_indexes.display_name = "display_name_value"
    index.etag = "etag_value"
    index.labels.key = "key_value"
    index.labels.value = "value_value"
    index.create_time.seconds = 751
    index.create_time.nanos = 543
    index.update_time.seconds = 751
    index.update_time.nanos = 543
    index.index_stats.vectors_count = 1422
    index.index_stats.shards_count = 1293
    index.index_update_method = "STREAM_UPDATE"
    index.encryption_spec.kms_key_name = "kms_key_name_value"

    update_mask = aiplatform_v1.FieldMask()
    update_mask.paths = ['paths_value1', 'paths_value2']

    request = aiplatform_v1.UpdateIndexRequest(
        index=index,
        update_mask=update_mask,
    )

    # Make the request
    operation = client.update_index(request=request)

    print("Waiting for operation to complete...")

    response = operation.result()

    # Handle the response
    print(response)

# [END aiplatform_v1_generated_IndexService_UpdateIndex_sync]

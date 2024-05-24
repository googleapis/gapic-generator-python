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
# Snippet for UpdateDataset
# NOTE: This snippet has been automatically generated for illustrative purposes only.
# It may require modifications to work in your environment.

# To install the latest published package dependency, execute the following:
#   python3 -m pip install google-cloud-aiplatform


# [START aiplatform_v1_generated_DatasetService_UpdateDataset_async]
# This snippet has been automatically generated and should be regarded as a
# code template only.
# It will require modifications to work:
# - It may require correct/in-range values for request initialization.
# - It may require specifying regional endpoints when creating the service
#   client as shown in:
#   https://googleapis.dev/python/google-api-core/latest/client_options.html
from google.cloud import aiplatform_v1


async def sample_update_dataset():
    # Create a client
    client = aiplatform_v1.DatasetServiceAsyncClient()

    # Initialize request argument(s)
    dataset = aiplatform_v1.Dataset()
    dataset.name = "name_value"
    dataset.display_name = "display_name_value"
    dataset.description = "description_value"
    dataset.metadata_schema_uri = "metadata_schema_uri_value"
    dataset.metadata.null_value = "NULL_VALUE"
    dataset.metadata.number_value = 0.1285
    dataset.metadata.string_value = "string_value_value"
    dataset.metadata.bool_value = True
    dataset.metadata.struct_value.fields.key = "key_value"
    dataset.metadata.struct_value.fields.value = "struct_pb2.Value(null_value=struct_pb2.NullValue.NULL_VALUE)"
    dataset.metadata.list_value.values = "[struct_pb2.Value(null_value=struct_pb2.NullValue.NULL_VALUE)]"
    dataset.data_item_count = 1584
    dataset.create_time.seconds = 751
    dataset.create_time.nanos = 543
    dataset.update_time.seconds = 751
    dataset.update_time.nanos = 543
    dataset.etag = "etag_value"
    dataset.labels.key = "key_value"
    dataset.labels.value = "value_value"
    dataset.saved_queries.name = "name_value"
    dataset.saved_queries.display_name = "display_name_value"
    dataset.saved_queries.metadata.null_value = "NULL_VALUE"
    dataset.saved_queries.metadata.number_value = 0.1285
    dataset.saved_queries.metadata.string_value = "string_value_value"
    dataset.saved_queries.metadata.bool_value = True
    dataset.saved_queries.metadata.struct_value.fields.key = "key_value"
    dataset.saved_queries.metadata.struct_value.fields.value = "struct_pb2.Value(null_value=struct_pb2.NullValue.NULL_VALUE)"
    dataset.saved_queries.metadata.list_value.values = "[struct_pb2.Value(null_value=struct_pb2.NullValue.NULL_VALUE)]"
    dataset.saved_queries.create_time.seconds = 751
    dataset.saved_queries.create_time.nanos = 543
    dataset.saved_queries.update_time.seconds = 751
    dataset.saved_queries.update_time.nanos = 543
    dataset.saved_queries.annotation_filter = "annotation_filter_value"
    dataset.saved_queries.problem_type = "problem_type_value"
    dataset.saved_queries.annotation_spec_count = 2253
    dataset.saved_queries.etag = "etag_value"
    dataset.saved_queries.support_automl_training = True
    dataset.encryption_spec.kms_key_name = "kms_key_name_value"
    dataset.metadata_artifact = "metadata_artifact_value"

    update_mask = aiplatform_v1.FieldMask()
    update_mask.paths = ['paths_value1', 'paths_value2']

    request = aiplatform_v1.UpdateDatasetRequest(
        dataset=dataset,
        update_mask=update_mask,
    )

    # Make the request
    response = await client.update_dataset(request=request)

    # Handle the response
    print(response)

# [END aiplatform_v1_generated_DatasetService_UpdateDataset_async]

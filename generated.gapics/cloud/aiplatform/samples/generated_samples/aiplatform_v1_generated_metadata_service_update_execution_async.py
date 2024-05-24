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
# Snippet for UpdateExecution
# NOTE: This snippet has been automatically generated for illustrative purposes only.
# It may require modifications to work in your environment.

# To install the latest published package dependency, execute the following:
#   python3 -m pip install google-cloud-aiplatform


# [START aiplatform_v1_generated_MetadataService_UpdateExecution_async]
# This snippet has been automatically generated and should be regarded as a
# code template only.
# It will require modifications to work:
# - It may require correct/in-range values for request initialization.
# - It may require specifying regional endpoints when creating the service
#   client as shown in:
#   https://googleapis.dev/python/google-api-core/latest/client_options.html
from google.cloud import aiplatform_v1


async def sample_update_execution():
    # Create a client
    client = aiplatform_v1.MetadataServiceAsyncClient()

    # Initialize request argument(s)
    execution = aiplatform_v1.Execution()
    execution.name = "name_value"
    execution.display_name = "display_name_value"
    execution.state = "CANCELLED"
    execution.etag = "etag_value"
    execution.labels.key = "key_value"
    execution.labels.value = "value_value"
    execution.create_time.seconds = 751
    execution.create_time.nanos = 543
    execution.update_time.seconds = 751
    execution.update_time.nanos = 543
    execution.schema_title = "schema_title_value"
    execution.schema_version = "schema_version_value"
    execution.metadata.fields.key = "key_value"
    execution.metadata.fields.value.null_value = "NULL_VALUE"
    execution.metadata.fields.value.number_value = 0.1285
    execution.metadata.fields.value.string_value = "string_value_value"
    execution.metadata.fields.value.bool_value = True
    execution.metadata.fields.value.struct_value = "struct_pb2.Struct(fields={'key_value': struct_pb2.Value(null_value=struct_pb2.NullValue.NULL_VALUE)})"
    execution.metadata.fields.value.list_value.values = "[struct_pb2.Value(null_value=struct_pb2.NullValue.NULL_VALUE)]"
    execution.description = "description_value"

    update_mask = aiplatform_v1.FieldMask()
    update_mask.paths = ['paths_value1', 'paths_value2']

    request = aiplatform_v1.UpdateExecutionRequest(
        execution=execution,
        update_mask=update_mask,
        allow_missing=True,
    )

    # Make the request
    response = await client.update_execution(request=request)

    # Handle the response
    print(response)

# [END aiplatform_v1_generated_MetadataService_UpdateExecution_async]

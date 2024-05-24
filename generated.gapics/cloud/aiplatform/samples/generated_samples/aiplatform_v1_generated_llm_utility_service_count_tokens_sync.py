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
# Snippet for CountTokens
# NOTE: This snippet has been automatically generated for illustrative purposes only.
# It may require modifications to work in your environment.

# To install the latest published package dependency, execute the following:
#   python3 -m pip install google-cloud-aiplatform


# [START aiplatform_v1_generated_LlmUtilityService_CountTokens_sync]
# This snippet has been automatically generated and should be regarded as a
# code template only.
# It will require modifications to work:
# - It may require correct/in-range values for request initialization.
# - It may require specifying regional endpoints when creating the service
#   client as shown in:
#   https://googleapis.dev/python/google-api-core/latest/client_options.html
from google.cloud import aiplatform_v1


def sample_count_tokens():
    # Create a client
    client = aiplatform_v1.LlmUtilityServiceClient()

    # Initialize request argument(s)
    instances = aiplatform_v1.Value()
    instances.null_value = "NULL_VALUE"
    instances.number_value = 0.1285
    instances.string_value = "string_value_value"
    instances.bool_value = True
    instances.struct_value.fields.key = "key_value"
    instances.struct_value.fields.value = "struct_pb2.Value(null_value=struct_pb2.NullValue.NULL_VALUE)"
    instances.list_value.values = "[struct_pb2.Value(null_value=struct_pb2.NullValue.NULL_VALUE)]"

    contents = aiplatform_v1.Content()
    contents.role = "role_value"
    contents.parts.text = "text_value"
    contents.parts.inline_data.mime_type = "mime_type_value"
    contents.parts.inline_data.data = b'data_blob'
    contents.parts.file_data.mime_type = "mime_type_value"
    contents.parts.file_data.file_uri = "file_uri_value"
    contents.parts.function_call.name = "name_value"
    contents.parts.function_call.args.fields.key = "key_value"
    contents.parts.function_call.args.fields.value.null_value = "NULL_VALUE"
    contents.parts.function_call.args.fields.value.number_value = 0.1285
    contents.parts.function_call.args.fields.value.string_value = "string_value_value"
    contents.parts.function_call.args.fields.value.bool_value = True
    contents.parts.function_call.args.fields.value.struct_value = "struct_pb2.Struct(fields={'key_value': struct_pb2.Value(null_value=struct_pb2.NullValue.NULL_VALUE)})"
    contents.parts.function_call.args.fields.value.list_value.values = "[struct_pb2.Value(null_value=struct_pb2.NullValue.NULL_VALUE)]"
    contents.parts.function_response.name = "name_value"
    contents.parts.function_response.response.fields.key = "key_value"
    contents.parts.function_response.response.fields.value.null_value = "NULL_VALUE"
    contents.parts.function_response.response.fields.value.number_value = 0.1285
    contents.parts.function_response.response.fields.value.string_value = "string_value_value"
    contents.parts.function_response.response.fields.value.bool_value = True
    contents.parts.function_response.response.fields.value.struct_value = "struct_pb2.Struct(fields={'key_value': struct_pb2.Value(null_value=struct_pb2.NullValue.NULL_VALUE)})"
    contents.parts.function_response.response.fields.value.list_value.values = "[struct_pb2.Value(null_value=struct_pb2.NullValue.NULL_VALUE)]"
    contents.parts.video_metadata.start_offset.seconds = 751
    contents.parts.video_metadata.start_offset.nanos = 543
    contents.parts.video_metadata.end_offset.seconds = 751
    contents.parts.video_metadata.end_offset.nanos = 543

    request = aiplatform_v1.CountTokensRequest(
        endpoint="endpoint_value",
        model="model_value",
        instances=instances,
        contents=contents,
    )

    # Make the request
    response = client.count_tokens(request=request)

    # Handle the response
    print(response)

# [END aiplatform_v1_generated_LlmUtilityService_CountTokens_sync]

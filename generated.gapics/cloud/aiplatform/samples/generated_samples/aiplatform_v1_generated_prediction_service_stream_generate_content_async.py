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
# Snippet for StreamGenerateContent
# NOTE: This snippet has been automatically generated for illustrative purposes only.
# It may require modifications to work in your environment.

# To install the latest published package dependency, execute the following:
#   python3 -m pip install google-cloud-aiplatform


# [START aiplatform_v1_generated_PredictionService_StreamGenerateContent_async]
# This snippet has been automatically generated and should be regarded as a
# code template only.
# It will require modifications to work:
# - It may require correct/in-range values for request initialization.
# - It may require specifying regional endpoints when creating the service
#   client as shown in:
#   https://googleapis.dev/python/google-api-core/latest/client_options.html
from google.cloud import aiplatform_v1


async def sample_stream_generate_content():
    # Create a client
    client = aiplatform_v1.PredictionServiceAsyncClient()

    # Initialize request argument(s)
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

    system_instruction = aiplatform_v1.Content()
    system_instruction.role = "role_value"
    system_instruction.parts.text = "text_value"
    system_instruction.parts.inline_data.mime_type = "mime_type_value"
    system_instruction.parts.inline_data.data = b'data_blob'
    system_instruction.parts.file_data.mime_type = "mime_type_value"
    system_instruction.parts.file_data.file_uri = "file_uri_value"
    system_instruction.parts.function_call.name = "name_value"
    system_instruction.parts.function_call.args.fields.key = "key_value"
    system_instruction.parts.function_call.args.fields.value.null_value = "NULL_VALUE"
    system_instruction.parts.function_call.args.fields.value.number_value = 0.1285
    system_instruction.parts.function_call.args.fields.value.string_value = "string_value_value"
    system_instruction.parts.function_call.args.fields.value.bool_value = True
    system_instruction.parts.function_call.args.fields.value.struct_value = "struct_pb2.Struct(fields={'key_value': struct_pb2.Value(null_value=struct_pb2.NullValue.NULL_VALUE)})"
    system_instruction.parts.function_call.args.fields.value.list_value.values = "[struct_pb2.Value(null_value=struct_pb2.NullValue.NULL_VALUE)]"
    system_instruction.parts.function_response.name = "name_value"
    system_instruction.parts.function_response.response.fields.key = "key_value"
    system_instruction.parts.function_response.response.fields.value.null_value = "NULL_VALUE"
    system_instruction.parts.function_response.response.fields.value.number_value = 0.1285
    system_instruction.parts.function_response.response.fields.value.string_value = "string_value_value"
    system_instruction.parts.function_response.response.fields.value.bool_value = True
    system_instruction.parts.function_response.response.fields.value.struct_value = "struct_pb2.Struct(fields={'key_value': struct_pb2.Value(null_value=struct_pb2.NullValue.NULL_VALUE)})"
    system_instruction.parts.function_response.response.fields.value.list_value.values = "[struct_pb2.Value(null_value=struct_pb2.NullValue.NULL_VALUE)]"
    system_instruction.parts.video_metadata.start_offset.seconds = 751
    system_instruction.parts.video_metadata.start_offset.nanos = 543
    system_instruction.parts.video_metadata.end_offset.seconds = 751
    system_instruction.parts.video_metadata.end_offset.nanos = 543

    tools = aiplatform_v1.Tool()
    tools.function_declarations.name = "name_value"
    tools.function_declarations.description = "description_value"
    tools.function_declarations.parameters.type_ = "OBJECT"
    tools.function_declarations.parameters.format_ = "format__value"
    tools.function_declarations.parameters.title = "title_value"
    tools.function_declarations.parameters.description = "description_value"
    tools.function_declarations.parameters.nullable = True
    tools.function_declarations.parameters.default.null_value = "NULL_VALUE"
    tools.function_declarations.parameters.default.number_value = 0.1285
    tools.function_declarations.parameters.default.string_value = "string_value_value"
    tools.function_declarations.parameters.default.bool_value = True
    tools.function_declarations.parameters.default.struct_value.fields.key = "key_value"
    tools.function_declarations.parameters.default.struct_value.fields.value = "struct_pb2.Value(null_value=struct_pb2.NullValue.NULL_VALUE)"
    tools.function_declarations.parameters.default.list_value.values = "[struct_pb2.Value(null_value=struct_pb2.NullValue.NULL_VALUE)]"
    tools.function_declarations.parameters.items = "openapi.Schema(type_=openapi.Type.STRING)"
    tools.function_declarations.parameters.min_items = 965
    tools.function_declarations.parameters.max_items = 967
    tools.function_declarations.parameters.enum = ['enum_value1', 'enum_value2']
    tools.function_declarations.parameters.properties.key = "key_value"
    tools.function_declarations.parameters.properties.value = "openapi.Schema(type_=openapi.Type.STRING)"
    tools.function_declarations.parameters.required = ['required_value1', 'required_value2']
    tools.function_declarations.parameters.min_properties = 1520
    tools.function_declarations.parameters.max_properties = 1522
    tools.function_declarations.parameters.minimum = 0.764
    tools.function_declarations.parameters.maximum = 0.766
    tools.function_declarations.parameters.min_length = 1061
    tools.function_declarations.parameters.max_length = 1063
    tools.function_declarations.parameters.pattern = "pattern_value"
    tools.function_declarations.parameters.example.null_value = "NULL_VALUE"
    tools.function_declarations.parameters.example.number_value = 0.1285
    tools.function_declarations.parameters.example.string_value = "string_value_value"
    tools.function_declarations.parameters.example.bool_value = True
    tools.function_declarations.parameters.example.struct_value.fields.key = "key_value"
    tools.function_declarations.parameters.example.struct_value.fields.value = "struct_pb2.Value(null_value=struct_pb2.NullValue.NULL_VALUE)"
    tools.function_declarations.parameters.example.list_value.values = "[struct_pb2.Value(null_value=struct_pb2.NullValue.NULL_VALUE)]"
    tools.retrieval.vertex_ai_search.datastore = "datastore_value"
    tools.retrieval.disable_attribution = True
    tools.google_search_retrieval.disable_attribution = True

    safety_settings = aiplatform_v1.SafetySetting()
    safety_settings.category = "HARM_CATEGORY_SEXUALLY_EXPLICIT"
    safety_settings.threshold = "BLOCK_NONE"
    safety_settings.method = "PROBABILITY"

    generation_config = aiplatform_v1.GenerationConfig()
    generation_config.temperature = 0.1198
    generation_config.top_p = 0.546
    generation_config.top_k = 0.541
    generation_config.candidate_count = 1573
    generation_config.max_output_tokens = 1865
    generation_config.stop_sequences = ['stop_sequences_value1', 'stop_sequences_value2']
    generation_config.presence_penalty = 0.1713
    generation_config.frequency_penalty = 0.18380000000000002
    generation_config.response_mime_type = "response_mime_type_value"

    request = aiplatform_v1.GenerateContentRequest(
        model="model_value",
        contents=contents,
        system_instruction=system_instruction,
        tools=tools,
        safety_settings=safety_settings,
        generation_config=generation_config,
    )

    # Make the request
    stream = await client.stream_generate_content(request=request)

    # Handle the response
    async for response in stream:
        print(response)

# [END aiplatform_v1_generated_PredictionService_StreamGenerateContent_async]

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
# Snippet for CreateTuningJob
# NOTE: This snippet has been automatically generated for illustrative purposes only.
# It may require modifications to work in your environment.

# To install the latest published package dependency, execute the following:
#   python3 -m pip install google-cloud-aiplatform


# [START aiplatform_v1_generated_GenAiTuningService_CreateTuningJob_async]
# This snippet has been automatically generated and should be regarded as a
# code template only.
# It will require modifications to work:
# - It may require correct/in-range values for request initialization.
# - It may require specifying regional endpoints when creating the service
#   client as shown in:
#   https://googleapis.dev/python/google-api-core/latest/client_options.html
from google.cloud import aiplatform_v1


async def sample_create_tuning_job():
    # Create a client
    client = aiplatform_v1.GenAiTuningServiceAsyncClient()

    # Initialize request argument(s)
    tuning_job = aiplatform_v1.TuningJob()
    tuning_job.base_model = "base_model_value"
    tuning_job.supervised_tuning_spec.training_dataset_uri = "training_dataset_uri_value"
    tuning_job.supervised_tuning_spec.validation_dataset_uri = "validation_dataset_uri_value"
    tuning_job.supervised_tuning_spec.hyper_parameters.epoch_count = 1175
    tuning_job.supervised_tuning_spec.hyper_parameters.learning_rate_multiplier = 0.2561
    tuning_job.supervised_tuning_spec.hyper_parameters.adapter_size = "ADAPTER_SIZE_SIXTEEN"
    tuning_job.name = "name_value"
    tuning_job.tuned_model_display_name = "tuned_model_display_name_value"
    tuning_job.description = "description_value"
    tuning_job.state = "JOB_STATE_PARTIALLY_SUCCEEDED"
    tuning_job.create_time.seconds = 751
    tuning_job.create_time.nanos = 543
    tuning_job.start_time.seconds = 751
    tuning_job.start_time.nanos = 543
    tuning_job.end_time.seconds = 751
    tuning_job.end_time.nanos = 543
    tuning_job.update_time.seconds = 751
    tuning_job.update_time.nanos = 543
    tuning_job.error.code = 411
    tuning_job.error.message = "message_value"
    tuning_job.error.details.type_url = "type.googleapis.com/google.protobuf.Empty"
    tuning_job.error.details.value = b'value_blob'
    tuning_job.labels.key = "key_value"
    tuning_job.labels.value = "value_value"
    tuning_job.experiment = "experiment_value"
    tuning_job.tuned_model.model = "model_value"
    tuning_job.tuned_model.endpoint = "endpoint_value"
    tuning_job.tuning_data_stats.supervised_tuning_data_stats.tuning_dataset_example_count = 2989
    tuning_job.tuning_data_stats.supervised_tuning_data_stats.total_tuning_character_count = 2988
    tuning_job.tuning_data_stats.supervised_tuning_data_stats.total_billable_character_count = 3150
    tuning_job.tuning_data_stats.supervised_tuning_data_stats.tuning_step_count = 1848
    tuning_job.tuning_data_stats.supervised_tuning_data_stats.user_input_token_distribution.sum = 341
    tuning_job.tuning_data_stats.supervised_tuning_data_stats.user_input_token_distribution.min_ = 0.419
    tuning_job.tuning_data_stats.supervised_tuning_data_stats.user_input_token_distribution.max_ = 0.421
    tuning_job.tuning_data_stats.supervised_tuning_data_stats.user_input_token_distribution.mean = 0.417
    tuning_job.tuning_data_stats.supervised_tuning_data_stats.user_input_token_distribution.median = 0.622
    tuning_job.tuning_data_stats.supervised_tuning_data_stats.user_input_token_distribution.p5 = 0.165
    tuning_job.tuning_data_stats.supervised_tuning_data_stats.user_input_token_distribution.p95 = 0.222
    tuning_job.tuning_data_stats.supervised_tuning_data_stats.user_input_token_distribution.buckets.count = 0.553
    tuning_job.tuning_data_stats.supervised_tuning_data_stats.user_input_token_distribution.buckets.left = 0.427
    tuning_job.tuning_data_stats.supervised_tuning_data_stats.user_input_token_distribution.buckets.right = 0.542
    tuning_job.tuning_data_stats.supervised_tuning_data_stats.user_output_token_distribution.sum = 341
    tuning_job.tuning_data_stats.supervised_tuning_data_stats.user_output_token_distribution.min_ = 0.419
    tuning_job.tuning_data_stats.supervised_tuning_data_stats.user_output_token_distribution.max_ = 0.421
    tuning_job.tuning_data_stats.supervised_tuning_data_stats.user_output_token_distribution.mean = 0.417
    tuning_job.tuning_data_stats.supervised_tuning_data_stats.user_output_token_distribution.median = 0.622
    tuning_job.tuning_data_stats.supervised_tuning_data_stats.user_output_token_distribution.p5 = 0.165
    tuning_job.tuning_data_stats.supervised_tuning_data_stats.user_output_token_distribution.p95 = 0.222
    tuning_job.tuning_data_stats.supervised_tuning_data_stats.user_output_token_distribution.buckets.count = 0.553
    tuning_job.tuning_data_stats.supervised_tuning_data_stats.user_output_token_distribution.buckets.left = 0.427
    tuning_job.tuning_data_stats.supervised_tuning_data_stats.user_output_token_distribution.buckets.right = 0.542
    tuning_job.tuning_data_stats.supervised_tuning_data_stats.user_message_per_example_distribution.sum = 341
    tuning_job.tuning_data_stats.supervised_tuning_data_stats.user_message_per_example_distribution.min_ = 0.419
    tuning_job.tuning_data_stats.supervised_tuning_data_stats.user_message_per_example_distribution.max_ = 0.421
    tuning_job.tuning_data_stats.supervised_tuning_data_stats.user_message_per_example_distribution.mean = 0.417
    tuning_job.tuning_data_stats.supervised_tuning_data_stats.user_message_per_example_distribution.median = 0.622
    tuning_job.tuning_data_stats.supervised_tuning_data_stats.user_message_per_example_distribution.p5 = 0.165
    tuning_job.tuning_data_stats.supervised_tuning_data_stats.user_message_per_example_distribution.p95 = 0.222
    tuning_job.tuning_data_stats.supervised_tuning_data_stats.user_message_per_example_distribution.buckets.count = 0.553
    tuning_job.tuning_data_stats.supervised_tuning_data_stats.user_message_per_example_distribution.buckets.left = 0.427
    tuning_job.tuning_data_stats.supervised_tuning_data_stats.user_message_per_example_distribution.buckets.right = 0.542
    tuning_job.tuning_data_stats.supervised_tuning_data_stats.user_dataset_examples.role = "role_value"
    tuning_job.tuning_data_stats.supervised_tuning_data_stats.user_dataset_examples.parts.text = "text_value"
    tuning_job.tuning_data_stats.supervised_tuning_data_stats.user_dataset_examples.parts.inline_data.mime_type = "mime_type_value"
    tuning_job.tuning_data_stats.supervised_tuning_data_stats.user_dataset_examples.parts.inline_data.data = b'data_blob'
    tuning_job.tuning_data_stats.supervised_tuning_data_stats.user_dataset_examples.parts.file_data.mime_type = "mime_type_value"
    tuning_job.tuning_data_stats.supervised_tuning_data_stats.user_dataset_examples.parts.file_data.file_uri = "file_uri_value"
    tuning_job.tuning_data_stats.supervised_tuning_data_stats.user_dataset_examples.parts.function_call.name = "name_value"
    tuning_job.tuning_data_stats.supervised_tuning_data_stats.user_dataset_examples.parts.function_call.args.fields.key = "key_value"
    tuning_job.tuning_data_stats.supervised_tuning_data_stats.user_dataset_examples.parts.function_call.args.fields.value.null_value = "NULL_VALUE"
    tuning_job.tuning_data_stats.supervised_tuning_data_stats.user_dataset_examples.parts.function_call.args.fields.value.number_value = 0.1285
    tuning_job.tuning_data_stats.supervised_tuning_data_stats.user_dataset_examples.parts.function_call.args.fields.value.string_value = "string_value_value"
    tuning_job.tuning_data_stats.supervised_tuning_data_stats.user_dataset_examples.parts.function_call.args.fields.value.bool_value = True
    tuning_job.tuning_data_stats.supervised_tuning_data_stats.user_dataset_examples.parts.function_call.args.fields.value.struct_value = "struct_pb2.Struct(fields={'key_value': struct_pb2.Value(null_value=struct_pb2.NullValue.NULL_VALUE)})"
    tuning_job.tuning_data_stats.supervised_tuning_data_stats.user_dataset_examples.parts.function_call.args.fields.value.list_value.values = "[struct_pb2.Value(null_value=struct_pb2.NullValue.NULL_VALUE)]"
    tuning_job.tuning_data_stats.supervised_tuning_data_stats.user_dataset_examples.parts.function_response.name = "name_value"
    tuning_job.tuning_data_stats.supervised_tuning_data_stats.user_dataset_examples.parts.function_response.response.fields.key = "key_value"
    tuning_job.tuning_data_stats.supervised_tuning_data_stats.user_dataset_examples.parts.function_response.response.fields.value.null_value = "NULL_VALUE"
    tuning_job.tuning_data_stats.supervised_tuning_data_stats.user_dataset_examples.parts.function_response.response.fields.value.number_value = 0.1285
    tuning_job.tuning_data_stats.supervised_tuning_data_stats.user_dataset_examples.parts.function_response.response.fields.value.string_value = "string_value_value"
    tuning_job.tuning_data_stats.supervised_tuning_data_stats.user_dataset_examples.parts.function_response.response.fields.value.bool_value = True
    tuning_job.tuning_data_stats.supervised_tuning_data_stats.user_dataset_examples.parts.function_response.response.fields.value.struct_value = "struct_pb2.Struct(fields={'key_value': struct_pb2.Value(null_value=struct_pb2.NullValue.NULL_VALUE)})"
    tuning_job.tuning_data_stats.supervised_tuning_data_stats.user_dataset_examples.parts.function_response.response.fields.value.list_value.values = "[struct_pb2.Value(null_value=struct_pb2.NullValue.NULL_VALUE)]"
    tuning_job.tuning_data_stats.supervised_tuning_data_stats.user_dataset_examples.parts.video_metadata.start_offset.seconds = 751
    tuning_job.tuning_data_stats.supervised_tuning_data_stats.user_dataset_examples.parts.video_metadata.start_offset.nanos = 543
    tuning_job.tuning_data_stats.supervised_tuning_data_stats.user_dataset_examples.parts.video_metadata.end_offset.seconds = 751
    tuning_job.tuning_data_stats.supervised_tuning_data_stats.user_dataset_examples.parts.video_metadata.end_offset.nanos = 543

    request = aiplatform_v1.CreateTuningJobRequest(
        parent="parent_value",
        tuning_job=tuning_job,
    )

    # Make the request
    response = await client.create_tuning_job(request=request)

    # Handle the response
    print(response)

# [END aiplatform_v1_generated_GenAiTuningService_CreateTuningJob_async]

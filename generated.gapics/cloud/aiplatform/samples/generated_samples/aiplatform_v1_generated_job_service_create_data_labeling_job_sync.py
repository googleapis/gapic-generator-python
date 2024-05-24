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
# Snippet for CreateDataLabelingJob
# NOTE: This snippet has been automatically generated for illustrative purposes only.
# It may require modifications to work in your environment.

# To install the latest published package dependency, execute the following:
#   python3 -m pip install google-cloud-aiplatform


# [START aiplatform_v1_generated_JobService_CreateDataLabelingJob_sync]
# This snippet has been automatically generated and should be regarded as a
# code template only.
# It will require modifications to work:
# - It may require correct/in-range values for request initialization.
# - It may require specifying regional endpoints when creating the service
#   client as shown in:
#   https://googleapis.dev/python/google-api-core/latest/client_options.html
from google.cloud import aiplatform_v1


def sample_create_data_labeling_job():
    # Create a client
    client = aiplatform_v1.JobServiceClient()

    # Initialize request argument(s)
    data_labeling_job = aiplatform_v1.DataLabelingJob()
    data_labeling_job.name = "name_value"
    data_labeling_job.display_name = "display_name_value"
    data_labeling_job.datasets = ['datasets_value1', 'datasets_value2']
    data_labeling_job.annotation_labels.key = "key_value"
    data_labeling_job.annotation_labels.value = "value_value"
    data_labeling_job.labeler_count = 1375
    data_labeling_job.instruction_uri = "instruction_uri_value"
    data_labeling_job.inputs_schema_uri = "inputs_schema_uri_value"
    data_labeling_job.inputs.null_value = "NULL_VALUE"
    data_labeling_job.inputs.number_value = 0.1285
    data_labeling_job.inputs.string_value = "string_value_value"
    data_labeling_job.inputs.bool_value = True
    data_labeling_job.inputs.struct_value.fields.key = "key_value"
    data_labeling_job.inputs.struct_value.fields.value = "struct_pb2.Value(null_value=struct_pb2.NullValue.NULL_VALUE)"
    data_labeling_job.inputs.list_value.values = "[struct_pb2.Value(null_value=struct_pb2.NullValue.NULL_VALUE)]"
    data_labeling_job.state = "JOB_STATE_PARTIALLY_SUCCEEDED"
    data_labeling_job.labeling_progress = 1810
    data_labeling_job.current_spend.currency_code = "currency_code_value"
    data_labeling_job.current_spend.units = 563
    data_labeling_job.current_spend.nanos = 543
    data_labeling_job.create_time.seconds = 751
    data_labeling_job.create_time.nanos = 543
    data_labeling_job.update_time.seconds = 751
    data_labeling_job.update_time.nanos = 543
    data_labeling_job.error.code = 411
    data_labeling_job.error.message = "message_value"
    data_labeling_job.error.details.type_url = "type.googleapis.com/google.protobuf.Empty"
    data_labeling_job.error.details.value = b'value_blob'
    data_labeling_job.labels.key = "key_value"
    data_labeling_job.labels.value = "value_value"
    data_labeling_job.specialist_pools = ['specialist_pools_value1', 'specialist_pools_value2']
    data_labeling_job.encryption_spec.kms_key_name = "kms_key_name_value"
    data_labeling_job.active_learning_config.max_data_item_count = 2005
    data_labeling_job.active_learning_config.max_data_item_percentage = 2506
    data_labeling_job.active_learning_config.sample_config.initial_batch_sample_percentage = 3241
    data_labeling_job.active_learning_config.sample_config.following_batch_sample_percentage = 3472
    data_labeling_job.active_learning_config.sample_config.sample_strategy = "UNCERTAINTY"
    data_labeling_job.active_learning_config.training_config.timeout_training_milli_hours = 3016

    request = aiplatform_v1.CreateDataLabelingJobRequest(
        parent="parent_value",
        data_labeling_job=data_labeling_job,
    )

    # Make the request
    response = client.create_data_labeling_job(request=request)

    # Handle the response
    print(response)

# [END aiplatform_v1_generated_JobService_CreateDataLabelingJob_sync]

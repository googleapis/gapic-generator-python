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
# Snippet for UpdateSchedule
# NOTE: This snippet has been automatically generated for illustrative purposes only.
# It may require modifications to work in your environment.

# To install the latest published package dependency, execute the following:
#   python3 -m pip install google-cloud-aiplatform


# [START aiplatform_v1_generated_ScheduleService_UpdateSchedule_async]
# This snippet has been automatically generated and should be regarded as a
# code template only.
# It will require modifications to work:
# - It may require correct/in-range values for request initialization.
# - It may require specifying regional endpoints when creating the service
#   client as shown in:
#   https://googleapis.dev/python/google-api-core/latest/client_options.html
from google.cloud import aiplatform_v1


async def sample_update_schedule():
    # Create a client
    client = aiplatform_v1.ScheduleServiceAsyncClient()

    # Initialize request argument(s)
    schedule = aiplatform_v1.Schedule()
    schedule.cron = "cron_value"
    schedule.create_pipeline_job_request.parent = "parent_value"
    schedule.create_pipeline_job_request.pipeline_job.name = "name_value"
    schedule.create_pipeline_job_request.pipeline_job.display_name = "display_name_value"
    schedule.create_pipeline_job_request.pipeline_job.create_time.seconds = 751
    schedule.create_pipeline_job_request.pipeline_job.create_time.nanos = 543
    schedule.create_pipeline_job_request.pipeline_job.start_time.seconds = 751
    schedule.create_pipeline_job_request.pipeline_job.start_time.nanos = 543
    schedule.create_pipeline_job_request.pipeline_job.end_time.seconds = 751
    schedule.create_pipeline_job_request.pipeline_job.end_time.nanos = 543
    schedule.create_pipeline_job_request.pipeline_job.update_time.seconds = 751
    schedule.create_pipeline_job_request.pipeline_job.update_time.nanos = 543
    schedule.create_pipeline_job_request.pipeline_job.pipeline_spec.fields.key = "key_value"
    schedule.create_pipeline_job_request.pipeline_job.pipeline_spec.fields.value.null_value = "NULL_VALUE"
    schedule.create_pipeline_job_request.pipeline_job.pipeline_spec.fields.value.number_value = 0.1285
    schedule.create_pipeline_job_request.pipeline_job.pipeline_spec.fields.value.string_value = "string_value_value"
    schedule.create_pipeline_job_request.pipeline_job.pipeline_spec.fields.value.bool_value = True
    schedule.create_pipeline_job_request.pipeline_job.pipeline_spec.fields.value.struct_value = "struct_pb2.Struct(fields={'key_value': struct_pb2.Value(null_value=struct_pb2.NullValue.NULL_VALUE)})"
    schedule.create_pipeline_job_request.pipeline_job.pipeline_spec.fields.value.list_value.values = "[struct_pb2.Value(null_value=struct_pb2.NullValue.NULL_VALUE)]"
    schedule.create_pipeline_job_request.pipeline_job.state = "PIPELINE_STATE_PAUSED"
    schedule.create_pipeline_job_request.pipeline_job.job_detail.pipeline_context.name = "name_value"
    schedule.create_pipeline_job_request.pipeline_job.job_detail.pipeline_context.display_name = "display_name_value"
    schedule.create_pipeline_job_request.pipeline_job.job_detail.pipeline_context.etag = "etag_value"
    schedule.create_pipeline_job_request.pipeline_job.job_detail.pipeline_context.labels.key = "key_value"
    schedule.create_pipeline_job_request.pipeline_job.job_detail.pipeline_context.labels.value = "value_value"
    schedule.create_pipeline_job_request.pipeline_job.job_detail.pipeline_context.create_time.seconds = 751
    schedule.create_pipeline_job_request.pipeline_job.job_detail.pipeline_context.create_time.nanos = 543
    schedule.create_pipeline_job_request.pipeline_job.job_detail.pipeline_context.update_time.seconds = 751
    schedule.create_pipeline_job_request.pipeline_job.job_detail.pipeline_context.update_time.nanos = 543
    schedule.create_pipeline_job_request.pipeline_job.job_detail.pipeline_context.parent_contexts = ['parent_contexts_value1', 'parent_contexts_value2']
    schedule.create_pipeline_job_request.pipeline_job.job_detail.pipeline_context.schema_title = "schema_title_value"
    schedule.create_pipeline_job_request.pipeline_job.job_detail.pipeline_context.schema_version = "schema_version_value"
    schedule.create_pipeline_job_request.pipeline_job.job_detail.pipeline_context.metadata.fields.key = "key_value"
    schedule.create_pipeline_job_request.pipeline_job.job_detail.pipeline_context.metadata.fields.value.null_value = "NULL_VALUE"
    schedule.create_pipeline_job_request.pipeline_job.job_detail.pipeline_context.metadata.fields.value.number_value = 0.1285
    schedule.create_pipeline_job_request.pipeline_job.job_detail.pipeline_context.metadata.fields.value.string_value = "string_value_value"
    schedule.create_pipeline_job_request.pipeline_job.job_detail.pipeline_context.metadata.fields.value.bool_value = True
    schedule.create_pipeline_job_request.pipeline_job.job_detail.pipeline_context.metadata.fields.value.struct_value = "struct_pb2.Struct(fields={'key_value': struct_pb2.Value(null_value=struct_pb2.NullValue.NULL_VALUE)})"
    schedule.create_pipeline_job_request.pipeline_job.job_detail.pipeline_context.metadata.fields.value.list_value.values = "[struct_pb2.Value(null_value=struct_pb2.NullValue.NULL_VALUE)]"
    schedule.create_pipeline_job_request.pipeline_job.job_detail.pipeline_context.description = "description_value"
    schedule.create_pipeline_job_request.pipeline_job.job_detail.pipeline_run_context.name = "name_value"
    schedule.create_pipeline_job_request.pipeline_job.job_detail.pipeline_run_context.display_name = "display_name_value"
    schedule.create_pipeline_job_request.pipeline_job.job_detail.pipeline_run_context.etag = "etag_value"
    schedule.create_pipeline_job_request.pipeline_job.job_detail.pipeline_run_context.labels.key = "key_value"
    schedule.create_pipeline_job_request.pipeline_job.job_detail.pipeline_run_context.labels.value = "value_value"
    schedule.create_pipeline_job_request.pipeline_job.job_detail.pipeline_run_context.create_time.seconds = 751
    schedule.create_pipeline_job_request.pipeline_job.job_detail.pipeline_run_context.create_time.nanos = 543
    schedule.create_pipeline_job_request.pipeline_job.job_detail.pipeline_run_context.update_time.seconds = 751
    schedule.create_pipeline_job_request.pipeline_job.job_detail.pipeline_run_context.update_time.nanos = 543
    schedule.create_pipeline_job_request.pipeline_job.job_detail.pipeline_run_context.parent_contexts = ['parent_contexts_value1', 'parent_contexts_value2']
    schedule.create_pipeline_job_request.pipeline_job.job_detail.pipeline_run_context.schema_title = "schema_title_value"
    schedule.create_pipeline_job_request.pipeline_job.job_detail.pipeline_run_context.schema_version = "schema_version_value"
    schedule.create_pipeline_job_request.pipeline_job.job_detail.pipeline_run_context.metadata.fields.key = "key_value"
    schedule.create_pipeline_job_request.pipeline_job.job_detail.pipeline_run_context.metadata.fields.value.null_value = "NULL_VALUE"
    schedule.create_pipeline_job_request.pipeline_job.job_detail.pipeline_run_context.metadata.fields.value.number_value = 0.1285
    schedule.create_pipeline_job_request.pipeline_job.job_detail.pipeline_run_context.metadata.fields.value.string_value = "string_value_value"
    schedule.create_pipeline_job_request.pipeline_job.job_detail.pipeline_run_context.metadata.fields.value.bool_value = True
    schedule.create_pipeline_job_request.pipeline_job.job_detail.pipeline_run_context.metadata.fields.value.struct_value = "struct_pb2.Struct(fields={'key_value': struct_pb2.Value(null_value=struct_pb2.NullValue.NULL_VALUE)})"
    schedule.create_pipeline_job_request.pipeline_job.job_detail.pipeline_run_context.metadata.fields.value.list_value.values = "[struct_pb2.Value(null_value=struct_pb2.NullValue.NULL_VALUE)]"
    schedule.create_pipeline_job_request.pipeline_job.job_detail.pipeline_run_context.description = "description_value"
    schedule.create_pipeline_job_request.pipeline_job.job_detail.task_details.task_id = 735
    schedule.create_pipeline_job_request.pipeline_job.job_detail.task_details.parent_task_id = 1480
    schedule.create_pipeline_job_request.pipeline_job.job_detail.task_details.task_name = "task_name_value"
    schedule.create_pipeline_job_request.pipeline_job.job_detail.task_details.create_time.seconds = 751
    schedule.create_pipeline_job_request.pipeline_job.job_detail.task_details.create_time.nanos = 543
    schedule.create_pipeline_job_request.pipeline_job.job_detail.task_details.start_time.seconds = 751
    schedule.create_pipeline_job_request.pipeline_job.job_detail.task_details.start_time.nanos = 543
    schedule.create_pipeline_job_request.pipeline_job.job_detail.task_details.end_time.seconds = 751
    schedule.create_pipeline_job_request.pipeline_job.job_detail.task_details.end_time.nanos = 543
    schedule.create_pipeline_job_request.pipeline_job.job_detail.task_details.executor_detail.container_detail.main_job = "main_job_value"
    schedule.create_pipeline_job_request.pipeline_job.job_detail.task_details.executor_detail.container_detail.pre_caching_check_job = "pre_caching_check_job_value"
    schedule.create_pipeline_job_request.pipeline_job.job_detail.task_details.executor_detail.container_detail.failed_main_jobs = ['failed_main_jobs_value1', 'failed_main_jobs_value2']
    schedule.create_pipeline_job_request.pipeline_job.job_detail.task_details.executor_detail.container_detail.failed_pre_caching_check_jobs = ['failed_pre_caching_check_jobs_value1', 'failed_pre_caching_check_jobs_value2']
    schedule.create_pipeline_job_request.pipeline_job.job_detail.task_details.executor_detail.custom_job_detail.job = "job_value"
    schedule.create_pipeline_job_request.pipeline_job.job_detail.task_details.executor_detail.custom_job_detail.failed_jobs = ['failed_jobs_value1', 'failed_jobs_value2']
    schedule.create_pipeline_job_request.pipeline_job.job_detail.task_details.state = "NOT_TRIGGERED"
    schedule.create_pipeline_job_request.pipeline_job.job_detail.task_details.execution.name = "name_value"
    schedule.create_pipeline_job_request.pipeline_job.job_detail.task_details.execution.display_name = "display_name_value"
    schedule.create_pipeline_job_request.pipeline_job.job_detail.task_details.execution.state = "CANCELLED"
    schedule.create_pipeline_job_request.pipeline_job.job_detail.task_details.execution.etag = "etag_value"
    schedule.create_pipeline_job_request.pipeline_job.job_detail.task_details.execution.labels.key = "key_value"
    schedule.create_pipeline_job_request.pipeline_job.job_detail.task_details.execution.labels.value = "value_value"
    schedule.create_pipeline_job_request.pipeline_job.job_detail.task_details.execution.create_time.seconds = 751
    schedule.create_pipeline_job_request.pipeline_job.job_detail.task_details.execution.create_time.nanos = 543
    schedule.create_pipeline_job_request.pipeline_job.job_detail.task_details.execution.update_time.seconds = 751
    schedule.create_pipeline_job_request.pipeline_job.job_detail.task_details.execution.update_time.nanos = 543
    schedule.create_pipeline_job_request.pipeline_job.job_detail.task_details.execution.schema_title = "schema_title_value"
    schedule.create_pipeline_job_request.pipeline_job.job_detail.task_details.execution.schema_version = "schema_version_value"
    schedule.create_pipeline_job_request.pipeline_job.job_detail.task_details.execution.metadata.fields.key = "key_value"
    schedule.create_pipeline_job_request.pipeline_job.job_detail.task_details.execution.metadata.fields.value.null_value = "NULL_VALUE"
    schedule.create_pipeline_job_request.pipeline_job.job_detail.task_details.execution.metadata.fields.value.number_value = 0.1285
    schedule.create_pipeline_job_request.pipeline_job.job_detail.task_details.execution.metadata.fields.value.string_value = "string_value_value"
    schedule.create_pipeline_job_request.pipeline_job.job_detail.task_details.execution.metadata.fields.value.bool_value = True
    schedule.create_pipeline_job_request.pipeline_job.job_detail.task_details.execution.metadata.fields.value.struct_value = "struct_pb2.Struct(fields={'key_value': struct_pb2.Value(null_value=struct_pb2.NullValue.NULL_VALUE)})"
    schedule.create_pipeline_job_request.pipeline_job.job_detail.task_details.execution.metadata.fields.value.list_value.values = "[struct_pb2.Value(null_value=struct_pb2.NullValue.NULL_VALUE)]"
    schedule.create_pipeline_job_request.pipeline_job.job_detail.task_details.execution.description = "description_value"
    schedule.create_pipeline_job_request.pipeline_job.job_detail.task_details.error.code = 411
    schedule.create_pipeline_job_request.pipeline_job.job_detail.task_details.error.message = "message_value"
    schedule.create_pipeline_job_request.pipeline_job.job_detail.task_details.error.details.type_url = "type.googleapis.com/google.protobuf.Empty"
    schedule.create_pipeline_job_request.pipeline_job.job_detail.task_details.error.details.value = b'value_blob'
    schedule.create_pipeline_job_request.pipeline_job.job_detail.task_details.pipeline_task_status.update_time.seconds = 751
    schedule.create_pipeline_job_request.pipeline_job.job_detail.task_details.pipeline_task_status.update_time.nanos = 543
    schedule.create_pipeline_job_request.pipeline_job.job_detail.task_details.pipeline_task_status.state = "NOT_TRIGGERED"
    schedule.create_pipeline_job_request.pipeline_job.job_detail.task_details.pipeline_task_status.error.code = 411
    schedule.create_pipeline_job_request.pipeline_job.job_detail.task_details.pipeline_task_status.error.message = "message_value"
    schedule.create_pipeline_job_request.pipeline_job.job_detail.task_details.pipeline_task_status.error.details.type_url = "type.googleapis.com/google.protobuf.Empty"
    schedule.create_pipeline_job_request.pipeline_job.job_detail.task_details.pipeline_task_status.error.details.value = b'value_blob'
    schedule.create_pipeline_job_request.pipeline_job.job_detail.task_details.inputs.key = "key_value"
    schedule.create_pipeline_job_request.pipeline_job.job_detail.task_details.inputs.value.artifacts.name = "name_value"
    schedule.create_pipeline_job_request.pipeline_job.job_detail.task_details.inputs.value.artifacts.display_name = "display_name_value"
    schedule.create_pipeline_job_request.pipeline_job.job_detail.task_details.inputs.value.artifacts.uri = "uri_value"
    schedule.create_pipeline_job_request.pipeline_job.job_detail.task_details.inputs.value.artifacts.etag = "etag_value"
    schedule.create_pipeline_job_request.pipeline_job.job_detail.task_details.inputs.value.artifacts.labels.key = "key_value"
    schedule.create_pipeline_job_request.pipeline_job.job_detail.task_details.inputs.value.artifacts.labels.value = "value_value"
    schedule.create_pipeline_job_request.pipeline_job.job_detail.task_details.inputs.value.artifacts.create_time.seconds = 751
    schedule.create_pipeline_job_request.pipeline_job.job_detail.task_details.inputs.value.artifacts.create_time.nanos = 543
    schedule.create_pipeline_job_request.pipeline_job.job_detail.task_details.inputs.value.artifacts.update_time.seconds = 751
    schedule.create_pipeline_job_request.pipeline_job.job_detail.task_details.inputs.value.artifacts.update_time.nanos = 543
    schedule.create_pipeline_job_request.pipeline_job.job_detail.task_details.inputs.value.artifacts.state = "LIVE"
    schedule.create_pipeline_job_request.pipeline_job.job_detail.task_details.inputs.value.artifacts.schema_title = "schema_title_value"
    schedule.create_pipeline_job_request.pipeline_job.job_detail.task_details.inputs.value.artifacts.schema_version = "schema_version_value"
    schedule.create_pipeline_job_request.pipeline_job.job_detail.task_details.inputs.value.artifacts.metadata.fields.key = "key_value"
    schedule.create_pipeline_job_request.pipeline_job.job_detail.task_details.inputs.value.artifacts.metadata.fields.value.null_value = "NULL_VALUE"
    schedule.create_pipeline_job_request.pipeline_job.job_detail.task_details.inputs.value.artifacts.metadata.fields.value.number_value = 0.1285
    schedule.create_pipeline_job_request.pipeline_job.job_detail.task_details.inputs.value.artifacts.metadata.fields.value.string_value = "string_value_value"
    schedule.create_pipeline_job_request.pipeline_job.job_detail.task_details.inputs.value.artifacts.metadata.fields.value.bool_value = True
    schedule.create_pipeline_job_request.pipeline_job.job_detail.task_details.inputs.value.artifacts.metadata.fields.value.struct_value = "struct_pb2.Struct(fields={'key_value': struct_pb2.Value(null_value=struct_pb2.NullValue.NULL_VALUE)})"
    schedule.create_pipeline_job_request.pipeline_job.job_detail.task_details.inputs.value.artifacts.metadata.fields.value.list_value.values = "[struct_pb2.Value(null_value=struct_pb2.NullValue.NULL_VALUE)]"
    schedule.create_pipeline_job_request.pipeline_job.job_detail.task_details.inputs.value.artifacts.description = "description_value"
    schedule.create_pipeline_job_request.pipeline_job.job_detail.task_details.outputs.key = "key_value"
    schedule.create_pipeline_job_request.pipeline_job.job_detail.task_details.outputs.value.artifacts.name = "name_value"
    schedule.create_pipeline_job_request.pipeline_job.job_detail.task_details.outputs.value.artifacts.display_name = "display_name_value"
    schedule.create_pipeline_job_request.pipeline_job.job_detail.task_details.outputs.value.artifacts.uri = "uri_value"
    schedule.create_pipeline_job_request.pipeline_job.job_detail.task_details.outputs.value.artifacts.etag = "etag_value"
    schedule.create_pipeline_job_request.pipeline_job.job_detail.task_details.outputs.value.artifacts.labels.key = "key_value"
    schedule.create_pipeline_job_request.pipeline_job.job_detail.task_details.outputs.value.artifacts.labels.value = "value_value"
    schedule.create_pipeline_job_request.pipeline_job.job_detail.task_details.outputs.value.artifacts.create_time.seconds = 751
    schedule.create_pipeline_job_request.pipeline_job.job_detail.task_details.outputs.value.artifacts.create_time.nanos = 543
    schedule.create_pipeline_job_request.pipeline_job.job_detail.task_details.outputs.value.artifacts.update_time.seconds = 751
    schedule.create_pipeline_job_request.pipeline_job.job_detail.task_details.outputs.value.artifacts.update_time.nanos = 543
    schedule.create_pipeline_job_request.pipeline_job.job_detail.task_details.outputs.value.artifacts.state = "LIVE"
    schedule.create_pipeline_job_request.pipeline_job.job_detail.task_details.outputs.value.artifacts.schema_title = "schema_title_value"
    schedule.create_pipeline_job_request.pipeline_job.job_detail.task_details.outputs.value.artifacts.schema_version = "schema_version_value"
    schedule.create_pipeline_job_request.pipeline_job.job_detail.task_details.outputs.value.artifacts.metadata.fields.key = "key_value"
    schedule.create_pipeline_job_request.pipeline_job.job_detail.task_details.outputs.value.artifacts.metadata.fields.value.null_value = "NULL_VALUE"
    schedule.create_pipeline_job_request.pipeline_job.job_detail.task_details.outputs.value.artifacts.metadata.fields.value.number_value = 0.1285
    schedule.create_pipeline_job_request.pipeline_job.job_detail.task_details.outputs.value.artifacts.metadata.fields.value.string_value = "string_value_value"
    schedule.create_pipeline_job_request.pipeline_job.job_detail.task_details.outputs.value.artifacts.metadata.fields.value.bool_value = True
    schedule.create_pipeline_job_request.pipeline_job.job_detail.task_details.outputs.value.artifacts.metadata.fields.value.struct_value = "struct_pb2.Struct(fields={'key_value': struct_pb2.Value(null_value=struct_pb2.NullValue.NULL_VALUE)})"
    schedule.create_pipeline_job_request.pipeline_job.job_detail.task_details.outputs.value.artifacts.metadata.fields.value.list_value.values = "[struct_pb2.Value(null_value=struct_pb2.NullValue.NULL_VALUE)]"
    schedule.create_pipeline_job_request.pipeline_job.job_detail.task_details.outputs.value.artifacts.description = "description_value"
    schedule.create_pipeline_job_request.pipeline_job.error.code = 411
    schedule.create_pipeline_job_request.pipeline_job.error.message = "message_value"
    schedule.create_pipeline_job_request.pipeline_job.error.details.type_url = "type.googleapis.com/google.protobuf.Empty"
    schedule.create_pipeline_job_request.pipeline_job.error.details.value = b'value_blob'
    schedule.create_pipeline_job_request.pipeline_job.labels.key = "key_value"
    schedule.create_pipeline_job_request.pipeline_job.labels.value = "value_value"
    schedule.create_pipeline_job_request.pipeline_job.runtime_config.parameters.key = "key_value"
    schedule.create_pipeline_job_request.pipeline_job.runtime_config.parameters.value.int_value = 967
    schedule.create_pipeline_job_request.pipeline_job.runtime_config.parameters.value.double_value = 0.12710000000000002
    schedule.create_pipeline_job_request.pipeline_job.runtime_config.parameters.value.string_value = "string_value_value"
    schedule.create_pipeline_job_request.pipeline_job.runtime_config.gcs_output_directory = "gcs_output_directory_value"
    schedule.create_pipeline_job_request.pipeline_job.runtime_config.parameter_values.key = "key_value"
    schedule.create_pipeline_job_request.pipeline_job.runtime_config.parameter_values.value.null_value = "NULL_VALUE"
    schedule.create_pipeline_job_request.pipeline_job.runtime_config.parameter_values.value.number_value = 0.1285
    schedule.create_pipeline_job_request.pipeline_job.runtime_config.parameter_values.value.string_value = "string_value_value"
    schedule.create_pipeline_job_request.pipeline_job.runtime_config.parameter_values.value.bool_value = True
    schedule.create_pipeline_job_request.pipeline_job.runtime_config.parameter_values.value.struct_value.fields.key = "key_value"
    schedule.create_pipeline_job_request.pipeline_job.runtime_config.parameter_values.value.struct_value.fields.value = "struct_pb2.Value(null_value=struct_pb2.NullValue.NULL_VALUE)"
    schedule.create_pipeline_job_request.pipeline_job.runtime_config.parameter_values.value.list_value.values = "[struct_pb2.Value(null_value=struct_pb2.NullValue.NULL_VALUE)]"
    schedule.create_pipeline_job_request.pipeline_job.runtime_config.failure_policy = "PIPELINE_FAILURE_POLICY_FAIL_FAST"
    schedule.create_pipeline_job_request.pipeline_job.runtime_config.input_artifacts.key = "key_value"
    schedule.create_pipeline_job_request.pipeline_job.runtime_config.input_artifacts.value.artifact_id = "artifact_id_value"
    schedule.create_pipeline_job_request.pipeline_job.encryption_spec.kms_key_name = "kms_key_name_value"
    schedule.create_pipeline_job_request.pipeline_job.service_account = "service_account_value"
    schedule.create_pipeline_job_request.pipeline_job.network = "network_value"
    schedule.create_pipeline_job_request.pipeline_job.reserved_ip_ranges = ['reserved_ip_ranges_value1', 'reserved_ip_ranges_value2']
    schedule.create_pipeline_job_request.pipeline_job.template_uri = "template_uri_value"
    schedule.create_pipeline_job_request.pipeline_job.template_metadata.version = "version_value"
    schedule.create_pipeline_job_request.pipeline_job.schedule_name = "schedule_name_value"
    schedule.create_pipeline_job_request.pipeline_job_id = "pipeline_job_id_value"
    schedule.name = "name_value"
    schedule.display_name = "display_name_value"
    schedule.start_time.seconds = 751
    schedule.start_time.nanos = 543
    schedule.end_time.seconds = 751
    schedule.end_time.nanos = 543
    schedule.max_run_count = 1410
    schedule.started_run_count = 1843
    schedule.state = "COMPLETED"
    schedule.create_time.seconds = 751
    schedule.create_time.nanos = 543
    schedule.update_time.seconds = 751
    schedule.update_time.nanos = 543
    schedule.next_run_time.seconds = 751
    schedule.next_run_time.nanos = 543
    schedule.last_pause_time.seconds = 751
    schedule.last_pause_time.nanos = 543
    schedule.last_resume_time.seconds = 751
    schedule.last_resume_time.nanos = 543
    schedule.max_concurrent_run_count = 2596
    schedule.allow_queueing = True
    schedule.catch_up = True
    schedule.last_scheduled_run_response.scheduled_run_time.seconds = 751
    schedule.last_scheduled_run_response.scheduled_run_time.nanos = 543
    schedule.last_scheduled_run_response.run_response = "run_response_value"

    update_mask = aiplatform_v1.FieldMask()
    update_mask.paths = ['paths_value1', 'paths_value2']

    request = aiplatform_v1.UpdateScheduleRequest(
        schedule=schedule,
        update_mask=update_mask,
    )

    # Make the request
    response = await client.update_schedule(request=request)

    # Handle the response
    print(response)

# [END aiplatform_v1_generated_ScheduleService_UpdateSchedule_async]

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
# Snippet for CreateModelDeploymentMonitoringJob
# NOTE: This snippet has been automatically generated for illustrative purposes only.
# It may require modifications to work in your environment.

# To install the latest published package dependency, execute the following:
#   python3 -m pip install google-cloud-aiplatform


# [START aiplatform_v1_generated_JobService_CreateModelDeploymentMonitoringJob_async]
# This snippet has been automatically generated and should be regarded as a
# code template only.
# It will require modifications to work:
# - It may require correct/in-range values for request initialization.
# - It may require specifying regional endpoints when creating the service
#   client as shown in:
#   https://googleapis.dev/python/google-api-core/latest/client_options.html
from google.cloud import aiplatform_v1


async def sample_create_model_deployment_monitoring_job():
    # Create a client
    client = aiplatform_v1.JobServiceAsyncClient()

    # Initialize request argument(s)
    model_deployment_monitoring_job = aiplatform_v1.ModelDeploymentMonitoringJob()
    model_deployment_monitoring_job.name = "name_value"
    model_deployment_monitoring_job.display_name = "display_name_value"
    model_deployment_monitoring_job.endpoint = "endpoint_value"
    model_deployment_monitoring_job.state = "JOB_STATE_PARTIALLY_SUCCEEDED"
    model_deployment_monitoring_job.schedule_state = "RUNNING"
    model_deployment_monitoring_job.latest_monitoring_pipeline_metadata.run_time.seconds = 751
    model_deployment_monitoring_job.latest_monitoring_pipeline_metadata.run_time.nanos = 543
    model_deployment_monitoring_job.latest_monitoring_pipeline_metadata.status.code = 411
    model_deployment_monitoring_job.latest_monitoring_pipeline_metadata.status.message = "message_value"
    model_deployment_monitoring_job.latest_monitoring_pipeline_metadata.status.details.type_url = "type.googleapis.com/google.protobuf.Empty"
    model_deployment_monitoring_job.latest_monitoring_pipeline_metadata.status.details.value = b'value_blob'
    model_deployment_monitoring_job.model_deployment_monitoring_objective_configs.deployed_model_id = "deployed_model_id_value"
    model_deployment_monitoring_job.model_deployment_monitoring_objective_configs.objective_config.training_dataset.dataset = "dataset_value"
    model_deployment_monitoring_job.model_deployment_monitoring_objective_configs.objective_config.training_dataset.gcs_source.uris = ['uris_value1', 'uris_value2']
    model_deployment_monitoring_job.model_deployment_monitoring_objective_configs.objective_config.training_dataset.bigquery_source.input_uri = "input_uri_value"
    model_deployment_monitoring_job.model_deployment_monitoring_objective_configs.objective_config.training_dataset.data_format = "data_format_value"
    model_deployment_monitoring_job.model_deployment_monitoring_objective_configs.objective_config.training_dataset.target_field = "target_field_value"
    model_deployment_monitoring_job.model_deployment_monitoring_objective_configs.objective_config.training_dataset.logging_sampling_strategy.random_sample_config.sample_rate = 0.1165
    model_deployment_monitoring_job.model_deployment_monitoring_objective_configs.objective_config.training_prediction_skew_detection_config.skew_thresholds.key = "key_value"
    model_deployment_monitoring_job.model_deployment_monitoring_objective_configs.objective_config.training_prediction_skew_detection_config.skew_thresholds.value.value = 0.541
    model_deployment_monitoring_job.model_deployment_monitoring_objective_configs.objective_config.training_prediction_skew_detection_config.attribution_score_skew_thresholds.key = "key_value"
    model_deployment_monitoring_job.model_deployment_monitoring_objective_configs.objective_config.training_prediction_skew_detection_config.attribution_score_skew_thresholds.value.value = 0.541
    model_deployment_monitoring_job.model_deployment_monitoring_objective_configs.objective_config.training_prediction_skew_detection_config.default_skew_threshold.value = 0.541
    model_deployment_monitoring_job.model_deployment_monitoring_objective_configs.objective_config.prediction_drift_detection_config.drift_thresholds.key = "key_value"
    model_deployment_monitoring_job.model_deployment_monitoring_objective_configs.objective_config.prediction_drift_detection_config.drift_thresholds.value.value = 0.541
    model_deployment_monitoring_job.model_deployment_monitoring_objective_configs.objective_config.prediction_drift_detection_config.attribution_score_drift_thresholds.key = "key_value"
    model_deployment_monitoring_job.model_deployment_monitoring_objective_configs.objective_config.prediction_drift_detection_config.attribution_score_drift_thresholds.value.value = 0.541
    model_deployment_monitoring_job.model_deployment_monitoring_objective_configs.objective_config.prediction_drift_detection_config.default_drift_threshold.value = 0.541
    model_deployment_monitoring_job.model_deployment_monitoring_objective_configs.objective_config.explanation_config.enable_feature_attributes = True
    model_deployment_monitoring_job.model_deployment_monitoring_objective_configs.objective_config.explanation_config.explanation_baseline.gcs.output_uri_prefix = "output_uri_prefix_value"
    model_deployment_monitoring_job.model_deployment_monitoring_objective_configs.objective_config.explanation_config.explanation_baseline.bigquery.output_uri = "output_uri_value"
    model_deployment_monitoring_job.model_deployment_monitoring_objective_configs.objective_config.explanation_config.explanation_baseline.prediction_format = "BIGQUERY"
    model_deployment_monitoring_job.model_deployment_monitoring_schedule_config.monitor_interval.seconds = 751
    model_deployment_monitoring_job.model_deployment_monitoring_schedule_config.monitor_interval.nanos = 543
    model_deployment_monitoring_job.model_deployment_monitoring_schedule_config.monitor_window.seconds = 751
    model_deployment_monitoring_job.model_deployment_monitoring_schedule_config.monitor_window.nanos = 543
    model_deployment_monitoring_job.logging_sampling_strategy.random_sample_config.sample_rate = 0.1165
    model_deployment_monitoring_job.model_monitoring_alert_config.email_alert_config.user_emails = ['user_emails_value1', 'user_emails_value2']
    model_deployment_monitoring_job.model_monitoring_alert_config.enable_logging = True
    model_deployment_monitoring_job.model_monitoring_alert_config.notification_channels = ['notification_channels_value1', 'notification_channels_value2']
    model_deployment_monitoring_job.predict_instance_schema_uri = "predict_instance_schema_uri_value"
    model_deployment_monitoring_job.sample_predict_instance.null_value = "NULL_VALUE"
    model_deployment_monitoring_job.sample_predict_instance.number_value = 0.1285
    model_deployment_monitoring_job.sample_predict_instance.string_value = "string_value_value"
    model_deployment_monitoring_job.sample_predict_instance.bool_value = True
    model_deployment_monitoring_job.sample_predict_instance.struct_value.fields.key = "key_value"
    model_deployment_monitoring_job.sample_predict_instance.struct_value.fields.value = "struct_pb2.Value(null_value=struct_pb2.NullValue.NULL_VALUE)"
    model_deployment_monitoring_job.sample_predict_instance.list_value.values = "[struct_pb2.Value(null_value=struct_pb2.NullValue.NULL_VALUE)]"
    model_deployment_monitoring_job.analysis_instance_schema_uri = "analysis_instance_schema_uri_value"
    model_deployment_monitoring_job.bigquery_tables.log_source = "SERVING"
    model_deployment_monitoring_job.bigquery_tables.log_type = "EXPLAIN"
    model_deployment_monitoring_job.bigquery_tables.bigquery_table_path = "bigquery_table_path_value"
    model_deployment_monitoring_job.bigquery_tables.request_response_logging_schema_version = "request_response_logging_schema_version_value"
    model_deployment_monitoring_job.log_ttl.seconds = 751
    model_deployment_monitoring_job.log_ttl.nanos = 543
    model_deployment_monitoring_job.labels.key = "key_value"
    model_deployment_monitoring_job.labels.value = "value_value"
    model_deployment_monitoring_job.create_time.seconds = 751
    model_deployment_monitoring_job.create_time.nanos = 543
    model_deployment_monitoring_job.update_time.seconds = 751
    model_deployment_monitoring_job.update_time.nanos = 543
    model_deployment_monitoring_job.next_schedule_time.seconds = 751
    model_deployment_monitoring_job.next_schedule_time.nanos = 543
    model_deployment_monitoring_job.stats_anomalies_base_directory.output_uri_prefix = "output_uri_prefix_value"
    model_deployment_monitoring_job.encryption_spec.kms_key_name = "kms_key_name_value"
    model_deployment_monitoring_job.enable_monitoring_pipeline_logs = True
    model_deployment_monitoring_job.error.code = 411
    model_deployment_monitoring_job.error.message = "message_value"
    model_deployment_monitoring_job.error.details.type_url = "type.googleapis.com/google.protobuf.Empty"
    model_deployment_monitoring_job.error.details.value = b'value_blob'

    request = aiplatform_v1.CreateModelDeploymentMonitoringJobRequest(
        parent="parent_value",
        model_deployment_monitoring_job=model_deployment_monitoring_job,
    )

    # Make the request
    response = await client.create_model_deployment_monitoring_job(request=request)

    # Handle the response
    print(response)

# [END aiplatform_v1_generated_JobService_CreateModelDeploymentMonitoringJob_async]

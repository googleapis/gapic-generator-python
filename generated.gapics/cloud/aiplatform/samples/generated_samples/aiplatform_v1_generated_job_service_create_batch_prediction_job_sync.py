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
# Snippet for CreateBatchPredictionJob
# NOTE: This snippet has been automatically generated for illustrative purposes only.
# It may require modifications to work in your environment.

# To install the latest published package dependency, execute the following:
#   python3 -m pip install google-cloud-aiplatform


# [START aiplatform_v1_generated_JobService_CreateBatchPredictionJob_sync]
# This snippet has been automatically generated and should be regarded as a
# code template only.
# It will require modifications to work:
# - It may require correct/in-range values for request initialization.
# - It may require specifying regional endpoints when creating the service
#   client as shown in:
#   https://googleapis.dev/python/google-api-core/latest/client_options.html
from google.cloud import aiplatform_v1


def sample_create_batch_prediction_job():
    # Create a client
    client = aiplatform_v1.JobServiceClient()

    # Initialize request argument(s)
    batch_prediction_job = aiplatform_v1.BatchPredictionJob()
    batch_prediction_job.name = "name_value"
    batch_prediction_job.display_name = "display_name_value"
    batch_prediction_job.model = "model_value"
    batch_prediction_job.model_version_id = "model_version_id_value"
    batch_prediction_job.unmanaged_container_model.artifact_uri = "artifact_uri_value"
    batch_prediction_job.unmanaged_container_model.predict_schemata.instance_schema_uri = "instance_schema_uri_value"
    batch_prediction_job.unmanaged_container_model.predict_schemata.parameters_schema_uri = "parameters_schema_uri_value"
    batch_prediction_job.unmanaged_container_model.predict_schemata.prediction_schema_uri = "prediction_schema_uri_value"
    batch_prediction_job.unmanaged_container_model.container_spec.image_uri = "image_uri_value"
    batch_prediction_job.unmanaged_container_model.container_spec.command = ['command_value1', 'command_value2']
    batch_prediction_job.unmanaged_container_model.container_spec.args = ['args_value1', 'args_value2']
    batch_prediction_job.unmanaged_container_model.container_spec.env.name = "name_value"
    batch_prediction_job.unmanaged_container_model.container_spec.env.value = "value_value"
    batch_prediction_job.unmanaged_container_model.container_spec.ports.container_port = 1511
    batch_prediction_job.unmanaged_container_model.container_spec.predict_route = "predict_route_value"
    batch_prediction_job.unmanaged_container_model.container_spec.health_route = "health_route_value"
    batch_prediction_job.unmanaged_container_model.container_spec.grpc_ports.container_port = 1511
    batch_prediction_job.unmanaged_container_model.container_spec.deployment_timeout.seconds = 751
    batch_prediction_job.unmanaged_container_model.container_spec.deployment_timeout.nanos = 543
    batch_prediction_job.unmanaged_container_model.container_spec.shared_memory_size_mb = 2231
    batch_prediction_job.unmanaged_container_model.container_spec.startup_probe.exec_.command = ['command_value1', 'command_value2']
    batch_prediction_job.unmanaged_container_model.container_spec.startup_probe.period_seconds = 1489
    batch_prediction_job.unmanaged_container_model.container_spec.startup_probe.timeout_seconds = 1621
    batch_prediction_job.unmanaged_container_model.container_spec.health_probe.exec_.command = ['command_value1', 'command_value2']
    batch_prediction_job.unmanaged_container_model.container_spec.health_probe.period_seconds = 1489
    batch_prediction_job.unmanaged_container_model.container_spec.health_probe.timeout_seconds = 1621
    batch_prediction_job.input_config.gcs_source.uris = ['uris_value1', 'uris_value2']
    batch_prediction_job.input_config.bigquery_source.input_uri = "input_uri_value"
    batch_prediction_job.input_config.instances_format = "instances_format_value"
    batch_prediction_job.instance_config.instance_type = "instance_type_value"
    batch_prediction_job.instance_config.key_field = "key_field_value"
    batch_prediction_job.instance_config.included_fields = ['included_fields_value1', 'included_fields_value2']
    batch_prediction_job.instance_config.excluded_fields = ['excluded_fields_value1', 'excluded_fields_value2']
    batch_prediction_job.model_parameters.null_value = "NULL_VALUE"
    batch_prediction_job.model_parameters.number_value = 0.1285
    batch_prediction_job.model_parameters.string_value = "string_value_value"
    batch_prediction_job.model_parameters.bool_value = True
    batch_prediction_job.model_parameters.struct_value.fields.key = "key_value"
    batch_prediction_job.model_parameters.struct_value.fields.value = "struct_pb2.Value(null_value=struct_pb2.NullValue.NULL_VALUE)"
    batch_prediction_job.model_parameters.list_value.values = "[struct_pb2.Value(null_value=struct_pb2.NullValue.NULL_VALUE)]"
    batch_prediction_job.output_config.gcs_destination.output_uri_prefix = "output_uri_prefix_value"
    batch_prediction_job.output_config.bigquery_destination.output_uri = "output_uri_value"
    batch_prediction_job.output_config.predictions_format = "predictions_format_value"
    batch_prediction_job.dedicated_resources.machine_spec.machine_type = "machine_type_value"
    batch_prediction_job.dedicated_resources.machine_spec.accelerator_type = "TPU_V5_LITEPOD"
    batch_prediction_job.dedicated_resources.machine_spec.accelerator_count = 1805
    batch_prediction_job.dedicated_resources.machine_spec.tpu_topology = "tpu_topology_value"
    batch_prediction_job.dedicated_resources.starting_replica_count = 2355
    batch_prediction_job.dedicated_resources.max_replica_count = 1805
    batch_prediction_job.service_account = "service_account_value"
    batch_prediction_job.manual_batch_tuning_parameters.batch_size = 1052
    batch_prediction_job.generate_explanation = True
    batch_prediction_job.explanation_spec.parameters.sampled_shapley_attribution.path_count = 1077
    batch_prediction_job.explanation_spec.parameters.integrated_gradients_attribution.step_count = 1092
    batch_prediction_job.explanation_spec.parameters.integrated_gradients_attribution.smooth_grad_config.noise_sigma = 0.11660000000000001
    batch_prediction_job.explanation_spec.parameters.integrated_gradients_attribution.smooth_grad_config.feature_noise_sigma.noise_sigma.name = "name_value"
    batch_prediction_job.explanation_spec.parameters.integrated_gradients_attribution.smooth_grad_config.feature_noise_sigma.noise_sigma.sigma = 0.529
    batch_prediction_job.explanation_spec.parameters.integrated_gradients_attribution.smooth_grad_config.noisy_sample_count = 1947
    batch_prediction_job.explanation_spec.parameters.integrated_gradients_attribution.blur_baseline_config.max_blur_sigma = 0.1482
    batch_prediction_job.explanation_spec.parameters.xrai_attribution.step_count = 1092
    batch_prediction_job.explanation_spec.parameters.xrai_attribution.smooth_grad_config.noise_sigma = 0.11660000000000001
    batch_prediction_job.explanation_spec.parameters.xrai_attribution.smooth_grad_config.feature_noise_sigma.noise_sigma.name = "name_value"
    batch_prediction_job.explanation_spec.parameters.xrai_attribution.smooth_grad_config.feature_noise_sigma.noise_sigma.sigma = 0.529
    batch_prediction_job.explanation_spec.parameters.xrai_attribution.smooth_grad_config.noisy_sample_count = 1947
    batch_prediction_job.explanation_spec.parameters.xrai_attribution.blur_baseline_config.max_blur_sigma = 0.1482
    batch_prediction_job.explanation_spec.parameters.examples.example_gcs_source.data_format = "JSONL"
    batch_prediction_job.explanation_spec.parameters.examples.example_gcs_source.gcs_source.uris = ['uris_value1', 'uris_value2']
    batch_prediction_job.explanation_spec.parameters.examples.nearest_neighbor_search_config.null_value = "NULL_VALUE"
    batch_prediction_job.explanation_spec.parameters.examples.nearest_neighbor_search_config.number_value = 0.1285
    batch_prediction_job.explanation_spec.parameters.examples.nearest_neighbor_search_config.string_value = "string_value_value"
    batch_prediction_job.explanation_spec.parameters.examples.nearest_neighbor_search_config.bool_value = True
    batch_prediction_job.explanation_spec.parameters.examples.nearest_neighbor_search_config.struct_value.fields.key = "key_value"
    batch_prediction_job.explanation_spec.parameters.examples.nearest_neighbor_search_config.struct_value.fields.value = "struct_pb2.Value(null_value=struct_pb2.NullValue.NULL_VALUE)"
    batch_prediction_job.explanation_spec.parameters.examples.nearest_neighbor_search_config.list_value.values = "[struct_pb2.Value(null_value=struct_pb2.NullValue.NULL_VALUE)]"
    batch_prediction_job.explanation_spec.parameters.examples.presets.query = "FAST"
    batch_prediction_job.explanation_spec.parameters.examples.presets.modality = "TABULAR"
    batch_prediction_job.explanation_spec.parameters.examples.neighbor_count = 1494
    batch_prediction_job.explanation_spec.parameters.top_k = 541
    batch_prediction_job.explanation_spec.parameters.output_indices.values.null_value = "NULL_VALUE"
    batch_prediction_job.explanation_spec.parameters.output_indices.values.number_value = 0.1285
    batch_prediction_job.explanation_spec.parameters.output_indices.values.string_value = "string_value_value"
    batch_prediction_job.explanation_spec.parameters.output_indices.values.bool_value = True
    batch_prediction_job.explanation_spec.parameters.output_indices.values.struct_value.fields.key = "key_value"
    batch_prediction_job.explanation_spec.parameters.output_indices.values.struct_value.fields.value = "struct_pb2.Value(null_value=struct_pb2.NullValue.NULL_VALUE)"
    batch_prediction_job.explanation_spec.parameters.output_indices.values.list_value = "struct_pb2.ListValue(values=[struct_pb2.Value(null_value=struct_pb2.NullValue.NULL_VALUE)])"
    batch_prediction_job.explanation_spec.metadata.inputs.key = "key_value"
    batch_prediction_job.explanation_spec.metadata.inputs.value.input_baselines.null_value = "NULL_VALUE"
    batch_prediction_job.explanation_spec.metadata.inputs.value.input_baselines.number_value = 0.1285
    batch_prediction_job.explanation_spec.metadata.inputs.value.input_baselines.string_value = "string_value_value"
    batch_prediction_job.explanation_spec.metadata.inputs.value.input_baselines.bool_value = True
    batch_prediction_job.explanation_spec.metadata.inputs.value.input_baselines.struct_value.fields.key = "key_value"
    batch_prediction_job.explanation_spec.metadata.inputs.value.input_baselines.struct_value.fields.value = "struct_pb2.Value(null_value=struct_pb2.NullValue.NULL_VALUE)"
    batch_prediction_job.explanation_spec.metadata.inputs.value.input_baselines.list_value.values = "[struct_pb2.Value(null_value=struct_pb2.NullValue.NULL_VALUE)]"
    batch_prediction_job.explanation_spec.metadata.inputs.value.input_tensor_name = "input_tensor_name_value"
    batch_prediction_job.explanation_spec.metadata.inputs.value.encoding = "CONCAT_EMBEDDING"
    batch_prediction_job.explanation_spec.metadata.inputs.value.modality = "modality_value"
    batch_prediction_job.explanation_spec.metadata.inputs.value.feature_value_domain.min_value = 0.96
    batch_prediction_job.explanation_spec.metadata.inputs.value.feature_value_domain.max_value = 0.962
    batch_prediction_job.explanation_spec.metadata.inputs.value.feature_value_domain.original_mean = 0.1365
    batch_prediction_job.explanation_spec.metadata.inputs.value.feature_value_domain.original_stddev = 0.1598
    batch_prediction_job.explanation_spec.metadata.inputs.value.indices_tensor_name = "indices_tensor_name_value"
    batch_prediction_job.explanation_spec.metadata.inputs.value.dense_shape_tensor_name = "dense_shape_tensor_name_value"
    batch_prediction_job.explanation_spec.metadata.inputs.value.index_feature_mapping = ['index_feature_mapping_value1', 'index_feature_mapping_value2']
    batch_prediction_job.explanation_spec.metadata.inputs.value.encoded_tensor_name = "encoded_tensor_name_value"
    batch_prediction_job.explanation_spec.metadata.inputs.value.encoded_baselines.null_value = "NULL_VALUE"
    batch_prediction_job.explanation_spec.metadata.inputs.value.encoded_baselines.number_value = 0.1285
    batch_prediction_job.explanation_spec.metadata.inputs.value.encoded_baselines.string_value = "string_value_value"
    batch_prediction_job.explanation_spec.metadata.inputs.value.encoded_baselines.bool_value = True
    batch_prediction_job.explanation_spec.metadata.inputs.value.encoded_baselines.struct_value.fields.key = "key_value"
    batch_prediction_job.explanation_spec.metadata.inputs.value.encoded_baselines.struct_value.fields.value = "struct_pb2.Value(null_value=struct_pb2.NullValue.NULL_VALUE)"
    batch_prediction_job.explanation_spec.metadata.inputs.value.encoded_baselines.list_value.values = "[struct_pb2.Value(null_value=struct_pb2.NullValue.NULL_VALUE)]"
    batch_prediction_job.explanation_spec.metadata.inputs.value.visualization.type_ = "OUTLINES"
    batch_prediction_job.explanation_spec.metadata.inputs.value.visualization.polarity = "BOTH"
    batch_prediction_job.explanation_spec.metadata.inputs.value.visualization.color_map = "PINK_WHITE_GREEN"
    batch_prediction_job.explanation_spec.metadata.inputs.value.visualization.clip_percent_upperbound = 0.2459
    batch_prediction_job.explanation_spec.metadata.inputs.value.visualization.clip_percent_lowerbound = 0.2456
    batch_prediction_job.explanation_spec.metadata.inputs.value.visualization.overlay_type = "MASK_BLACK"
    batch_prediction_job.explanation_spec.metadata.inputs.value.group_name = "group_name_value"
    batch_prediction_job.explanation_spec.metadata.outputs.key = "key_value"
    batch_prediction_job.explanation_spec.metadata.outputs.value.index_display_name_mapping.null_value = "NULL_VALUE"
    batch_prediction_job.explanation_spec.metadata.outputs.value.index_display_name_mapping.number_value = 0.1285
    batch_prediction_job.explanation_spec.metadata.outputs.value.index_display_name_mapping.string_value = "string_value_value"
    batch_prediction_job.explanation_spec.metadata.outputs.value.index_display_name_mapping.bool_value = True
    batch_prediction_job.explanation_spec.metadata.outputs.value.index_display_name_mapping.struct_value.fields.key = "key_value"
    batch_prediction_job.explanation_spec.metadata.outputs.value.index_display_name_mapping.struct_value.fields.value = "struct_pb2.Value(null_value=struct_pb2.NullValue.NULL_VALUE)"
    batch_prediction_job.explanation_spec.metadata.outputs.value.index_display_name_mapping.list_value.values = "[struct_pb2.Value(null_value=struct_pb2.NullValue.NULL_VALUE)]"
    batch_prediction_job.explanation_spec.metadata.outputs.value.display_name_mapping_key = "display_name_mapping_key_value"
    batch_prediction_job.explanation_spec.metadata.outputs.value.output_tensor_name = "output_tensor_name_value"
    batch_prediction_job.explanation_spec.metadata.feature_attributions_schema_uri = "feature_attributions_schema_uri_value"
    batch_prediction_job.explanation_spec.metadata.latent_space_source = "latent_space_source_value"
    batch_prediction_job.output_info.gcs_output_directory = "gcs_output_directory_value"
    batch_prediction_job.output_info.bigquery_output_dataset = "bigquery_output_dataset_value"
    batch_prediction_job.output_info.bigquery_output_table = "bigquery_output_table_value"
    batch_prediction_job.state = "JOB_STATE_PARTIALLY_SUCCEEDED"
    batch_prediction_job.error.code = 411
    batch_prediction_job.error.message = "message_value"
    batch_prediction_job.error.details.type_url = "type.googleapis.com/google.protobuf.Empty"
    batch_prediction_job.error.details.value = b'value_blob'
    batch_prediction_job.partial_failures.code = 411
    batch_prediction_job.partial_failures.message = "message_value"
    batch_prediction_job.partial_failures.details.type_url = "type.googleapis.com/google.protobuf.Empty"
    batch_prediction_job.partial_failures.details.value = b'value_blob'
    batch_prediction_job.resources_consumed.replica_hours = 0.13920000000000002
    batch_prediction_job.completion_stats.successful_count = 1736
    batch_prediction_job.completion_stats.failed_count = 1261
    batch_prediction_job.completion_stats.incomplete_count = 1720
    batch_prediction_job.completion_stats.successful_forecast_point_count = 3335
    batch_prediction_job.create_time.seconds = 751
    batch_prediction_job.create_time.nanos = 543
    batch_prediction_job.start_time.seconds = 751
    batch_prediction_job.start_time.nanos = 543
    batch_prediction_job.end_time.seconds = 751
    batch_prediction_job.end_time.nanos = 543
    batch_prediction_job.update_time.seconds = 751
    batch_prediction_job.update_time.nanos = 543
    batch_prediction_job.labels.key = "key_value"
    batch_prediction_job.labels.value = "value_value"
    batch_prediction_job.encryption_spec.kms_key_name = "kms_key_name_value"
    batch_prediction_job.disable_container_logging = True

    request = aiplatform_v1.CreateBatchPredictionJobRequest(
        parent="parent_value",
        batch_prediction_job=batch_prediction_job,
    )

    # Make the request
    response = client.create_batch_prediction_job(request=request)

    # Handle the response
    print(response)

# [END aiplatform_v1_generated_JobService_CreateBatchPredictionJob_sync]

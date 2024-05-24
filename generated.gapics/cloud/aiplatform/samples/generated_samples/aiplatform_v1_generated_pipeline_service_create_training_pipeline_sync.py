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
# Snippet for CreateTrainingPipeline
# NOTE: This snippet has been automatically generated for illustrative purposes only.
# It may require modifications to work in your environment.

# To install the latest published package dependency, execute the following:
#   python3 -m pip install google-cloud-aiplatform


# [START aiplatform_v1_generated_PipelineService_CreateTrainingPipeline_sync]
# This snippet has been automatically generated and should be regarded as a
# code template only.
# It will require modifications to work:
# - It may require correct/in-range values for request initialization.
# - It may require specifying regional endpoints when creating the service
#   client as shown in:
#   https://googleapis.dev/python/google-api-core/latest/client_options.html
from google.cloud import aiplatform_v1


def sample_create_training_pipeline():
    # Create a client
    client = aiplatform_v1.PipelineServiceClient()

    # Initialize request argument(s)
    training_pipeline = aiplatform_v1.TrainingPipeline()
    training_pipeline.name = "name_value"
    training_pipeline.display_name = "display_name_value"
    training_pipeline.input_data_config.fraction_split.training_fraction = 0.1809
    training_pipeline.input_data_config.fraction_split.validation_fraction = 0.2016
    training_pipeline.input_data_config.fraction_split.test_fraction = 0.13970000000000002
    training_pipeline.input_data_config.filter_split.training_filter = "training_filter_value"
    training_pipeline.input_data_config.filter_split.validation_filter = "validation_filter_value"
    training_pipeline.input_data_config.filter_split.test_filter = "test_filter_value"
    training_pipeline.input_data_config.predefined_split.key = "key_value"
    training_pipeline.input_data_config.timestamp_split.training_fraction = 0.1809
    training_pipeline.input_data_config.timestamp_split.validation_fraction = 0.2016
    training_pipeline.input_data_config.timestamp_split.test_fraction = 0.13970000000000002
    training_pipeline.input_data_config.timestamp_split.key = "key_value"
    training_pipeline.input_data_config.stratified_split.training_fraction = 0.1809
    training_pipeline.input_data_config.stratified_split.validation_fraction = 0.2016
    training_pipeline.input_data_config.stratified_split.test_fraction = 0.13970000000000002
    training_pipeline.input_data_config.stratified_split.key = "key_value"
    training_pipeline.input_data_config.gcs_destination.output_uri_prefix = "output_uri_prefix_value"
    training_pipeline.input_data_config.bigquery_destination.output_uri = "output_uri_value"
    training_pipeline.input_data_config.dataset_id = "dataset_id_value"
    training_pipeline.input_data_config.annotations_filter = "annotations_filter_value"
    training_pipeline.input_data_config.annotation_schema_uri = "annotation_schema_uri_value"
    training_pipeline.input_data_config.saved_query_id = "saved_query_id_value"
    training_pipeline.input_data_config.persist_ml_use_assignment = True
    training_pipeline.training_task_definition = "training_task_definition_value"
    training_pipeline.training_task_inputs.null_value = "NULL_VALUE"
    training_pipeline.training_task_inputs.number_value = 0.1285
    training_pipeline.training_task_inputs.string_value = "string_value_value"
    training_pipeline.training_task_inputs.bool_value = True
    training_pipeline.training_task_inputs.struct_value.fields.key = "key_value"
    training_pipeline.training_task_inputs.struct_value.fields.value = "struct_pb2.Value(null_value=struct_pb2.NullValue.NULL_VALUE)"
    training_pipeline.training_task_inputs.list_value.values = "[struct_pb2.Value(null_value=struct_pb2.NullValue.NULL_VALUE)]"
    training_pipeline.training_task_metadata.null_value = "NULL_VALUE"
    training_pipeline.training_task_metadata.number_value = 0.1285
    training_pipeline.training_task_metadata.string_value = "string_value_value"
    training_pipeline.training_task_metadata.bool_value = True
    training_pipeline.training_task_metadata.struct_value.fields.key = "key_value"
    training_pipeline.training_task_metadata.struct_value.fields.value = "struct_pb2.Value(null_value=struct_pb2.NullValue.NULL_VALUE)"
    training_pipeline.training_task_metadata.list_value.values = "[struct_pb2.Value(null_value=struct_pb2.NullValue.NULL_VALUE)]"
    training_pipeline.model_to_upload.name = "name_value"
    training_pipeline.model_to_upload.version_id = "version_id_value"
    training_pipeline.model_to_upload.version_aliases = ['version_aliases_value1', 'version_aliases_value2']
    training_pipeline.model_to_upload.version_create_time.seconds = 751
    training_pipeline.model_to_upload.version_create_time.nanos = 543
    training_pipeline.model_to_upload.version_update_time.seconds = 751
    training_pipeline.model_to_upload.version_update_time.nanos = 543
    training_pipeline.model_to_upload.display_name = "display_name_value"
    training_pipeline.model_to_upload.description = "description_value"
    training_pipeline.model_to_upload.version_description = "version_description_value"
    training_pipeline.model_to_upload.predict_schemata.instance_schema_uri = "instance_schema_uri_value"
    training_pipeline.model_to_upload.predict_schemata.parameters_schema_uri = "parameters_schema_uri_value"
    training_pipeline.model_to_upload.predict_schemata.prediction_schema_uri = "prediction_schema_uri_value"
    training_pipeline.model_to_upload.metadata_schema_uri = "metadata_schema_uri_value"
    training_pipeline.model_to_upload.metadata.null_value = "NULL_VALUE"
    training_pipeline.model_to_upload.metadata.number_value = 0.1285
    training_pipeline.model_to_upload.metadata.string_value = "string_value_value"
    training_pipeline.model_to_upload.metadata.bool_value = True
    training_pipeline.model_to_upload.metadata.struct_value.fields.key = "key_value"
    training_pipeline.model_to_upload.metadata.struct_value.fields.value = "struct_pb2.Value(null_value=struct_pb2.NullValue.NULL_VALUE)"
    training_pipeline.model_to_upload.metadata.list_value.values = "[struct_pb2.Value(null_value=struct_pb2.NullValue.NULL_VALUE)]"
    training_pipeline.model_to_upload.supported_export_formats.id = "id_value"
    training_pipeline.model_to_upload.supported_export_formats.exportable_contents = ['IMAGE']
    training_pipeline.model_to_upload.training_pipeline = "training_pipeline_value"
    training_pipeline.model_to_upload.pipeline_job = "pipeline_job_value"
    training_pipeline.model_to_upload.container_spec.image_uri = "image_uri_value"
    training_pipeline.model_to_upload.container_spec.command = ['command_value1', 'command_value2']
    training_pipeline.model_to_upload.container_spec.args = ['args_value1', 'args_value2']
    training_pipeline.model_to_upload.container_spec.env.name = "name_value"
    training_pipeline.model_to_upload.container_spec.env.value = "value_value"
    training_pipeline.model_to_upload.container_spec.ports.container_port = 1511
    training_pipeline.model_to_upload.container_spec.predict_route = "predict_route_value"
    training_pipeline.model_to_upload.container_spec.health_route = "health_route_value"
    training_pipeline.model_to_upload.container_spec.grpc_ports.container_port = 1511
    training_pipeline.model_to_upload.container_spec.deployment_timeout.seconds = 751
    training_pipeline.model_to_upload.container_spec.deployment_timeout.nanos = 543
    training_pipeline.model_to_upload.container_spec.shared_memory_size_mb = 2231
    training_pipeline.model_to_upload.container_spec.startup_probe.exec_.command = ['command_value1', 'command_value2']
    training_pipeline.model_to_upload.container_spec.startup_probe.period_seconds = 1489
    training_pipeline.model_to_upload.container_spec.startup_probe.timeout_seconds = 1621
    training_pipeline.model_to_upload.container_spec.health_probe.exec_.command = ['command_value1', 'command_value2']
    training_pipeline.model_to_upload.container_spec.health_probe.period_seconds = 1489
    training_pipeline.model_to_upload.container_spec.health_probe.timeout_seconds = 1621
    training_pipeline.model_to_upload.artifact_uri = "artifact_uri_value"
    training_pipeline.model_to_upload.supported_deployment_resources_types = ['SHARED_RESOURCES']
    training_pipeline.model_to_upload.supported_input_storage_formats = ['supported_input_storage_formats_value1', 'supported_input_storage_formats_value2']
    training_pipeline.model_to_upload.supported_output_storage_formats = ['supported_output_storage_formats_value1', 'supported_output_storage_formats_value2']
    training_pipeline.model_to_upload.create_time.seconds = 751
    training_pipeline.model_to_upload.create_time.nanos = 543
    training_pipeline.model_to_upload.update_time.seconds = 751
    training_pipeline.model_to_upload.update_time.nanos = 543
    training_pipeline.model_to_upload.deployed_models.endpoint = "endpoint_value"
    training_pipeline.model_to_upload.deployed_models.deployed_model_id = "deployed_model_id_value"
    training_pipeline.model_to_upload.explanation_spec.parameters.sampled_shapley_attribution.path_count = 1077
    training_pipeline.model_to_upload.explanation_spec.parameters.integrated_gradients_attribution.step_count = 1092
    training_pipeline.model_to_upload.explanation_spec.parameters.integrated_gradients_attribution.smooth_grad_config.noise_sigma = 0.11660000000000001
    training_pipeline.model_to_upload.explanation_spec.parameters.integrated_gradients_attribution.smooth_grad_config.feature_noise_sigma.noise_sigma.name = "name_value"
    training_pipeline.model_to_upload.explanation_spec.parameters.integrated_gradients_attribution.smooth_grad_config.feature_noise_sigma.noise_sigma.sigma = 0.529
    training_pipeline.model_to_upload.explanation_spec.parameters.integrated_gradients_attribution.smooth_grad_config.noisy_sample_count = 1947
    training_pipeline.model_to_upload.explanation_spec.parameters.integrated_gradients_attribution.blur_baseline_config.max_blur_sigma = 0.1482
    training_pipeline.model_to_upload.explanation_spec.parameters.xrai_attribution.step_count = 1092
    training_pipeline.model_to_upload.explanation_spec.parameters.xrai_attribution.smooth_grad_config.noise_sigma = 0.11660000000000001
    training_pipeline.model_to_upload.explanation_spec.parameters.xrai_attribution.smooth_grad_config.feature_noise_sigma.noise_sigma.name = "name_value"
    training_pipeline.model_to_upload.explanation_spec.parameters.xrai_attribution.smooth_grad_config.feature_noise_sigma.noise_sigma.sigma = 0.529
    training_pipeline.model_to_upload.explanation_spec.parameters.xrai_attribution.smooth_grad_config.noisy_sample_count = 1947
    training_pipeline.model_to_upload.explanation_spec.parameters.xrai_attribution.blur_baseline_config.max_blur_sigma = 0.1482
    training_pipeline.model_to_upload.explanation_spec.parameters.examples.example_gcs_source.data_format = "JSONL"
    training_pipeline.model_to_upload.explanation_spec.parameters.examples.example_gcs_source.gcs_source.uris = ['uris_value1', 'uris_value2']
    training_pipeline.model_to_upload.explanation_spec.parameters.examples.nearest_neighbor_search_config.null_value = "NULL_VALUE"
    training_pipeline.model_to_upload.explanation_spec.parameters.examples.nearest_neighbor_search_config.number_value = 0.1285
    training_pipeline.model_to_upload.explanation_spec.parameters.examples.nearest_neighbor_search_config.string_value = "string_value_value"
    training_pipeline.model_to_upload.explanation_spec.parameters.examples.nearest_neighbor_search_config.bool_value = True
    training_pipeline.model_to_upload.explanation_spec.parameters.examples.nearest_neighbor_search_config.struct_value.fields.key = "key_value"
    training_pipeline.model_to_upload.explanation_spec.parameters.examples.nearest_neighbor_search_config.struct_value.fields.value = "struct_pb2.Value(null_value=struct_pb2.NullValue.NULL_VALUE)"
    training_pipeline.model_to_upload.explanation_spec.parameters.examples.nearest_neighbor_search_config.list_value.values = "[struct_pb2.Value(null_value=struct_pb2.NullValue.NULL_VALUE)]"
    training_pipeline.model_to_upload.explanation_spec.parameters.examples.presets.query = "FAST"
    training_pipeline.model_to_upload.explanation_spec.parameters.examples.presets.modality = "TABULAR"
    training_pipeline.model_to_upload.explanation_spec.parameters.examples.neighbor_count = 1494
    training_pipeline.model_to_upload.explanation_spec.parameters.top_k = 541
    training_pipeline.model_to_upload.explanation_spec.parameters.output_indices.values.null_value = "NULL_VALUE"
    training_pipeline.model_to_upload.explanation_spec.parameters.output_indices.values.number_value = 0.1285
    training_pipeline.model_to_upload.explanation_spec.parameters.output_indices.values.string_value = "string_value_value"
    training_pipeline.model_to_upload.explanation_spec.parameters.output_indices.values.bool_value = True
    training_pipeline.model_to_upload.explanation_spec.parameters.output_indices.values.struct_value.fields.key = "key_value"
    training_pipeline.model_to_upload.explanation_spec.parameters.output_indices.values.struct_value.fields.value = "struct_pb2.Value(null_value=struct_pb2.NullValue.NULL_VALUE)"
    training_pipeline.model_to_upload.explanation_spec.parameters.output_indices.values.list_value = "struct_pb2.ListValue(values=[struct_pb2.Value(null_value=struct_pb2.NullValue.NULL_VALUE)])"
    training_pipeline.model_to_upload.explanation_spec.metadata.inputs.key = "key_value"
    training_pipeline.model_to_upload.explanation_spec.metadata.inputs.value.input_baselines.null_value = "NULL_VALUE"
    training_pipeline.model_to_upload.explanation_spec.metadata.inputs.value.input_baselines.number_value = 0.1285
    training_pipeline.model_to_upload.explanation_spec.metadata.inputs.value.input_baselines.string_value = "string_value_value"
    training_pipeline.model_to_upload.explanation_spec.metadata.inputs.value.input_baselines.bool_value = True
    training_pipeline.model_to_upload.explanation_spec.metadata.inputs.value.input_baselines.struct_value.fields.key = "key_value"
    training_pipeline.model_to_upload.explanation_spec.metadata.inputs.value.input_baselines.struct_value.fields.value = "struct_pb2.Value(null_value=struct_pb2.NullValue.NULL_VALUE)"
    training_pipeline.model_to_upload.explanation_spec.metadata.inputs.value.input_baselines.list_value.values = "[struct_pb2.Value(null_value=struct_pb2.NullValue.NULL_VALUE)]"
    training_pipeline.model_to_upload.explanation_spec.metadata.inputs.value.input_tensor_name = "input_tensor_name_value"
    training_pipeline.model_to_upload.explanation_spec.metadata.inputs.value.encoding = "CONCAT_EMBEDDING"
    training_pipeline.model_to_upload.explanation_spec.metadata.inputs.value.modality = "modality_value"
    training_pipeline.model_to_upload.explanation_spec.metadata.inputs.value.feature_value_domain.min_value = 0.96
    training_pipeline.model_to_upload.explanation_spec.metadata.inputs.value.feature_value_domain.max_value = 0.962
    training_pipeline.model_to_upload.explanation_spec.metadata.inputs.value.feature_value_domain.original_mean = 0.1365
    training_pipeline.model_to_upload.explanation_spec.metadata.inputs.value.feature_value_domain.original_stddev = 0.1598
    training_pipeline.model_to_upload.explanation_spec.metadata.inputs.value.indices_tensor_name = "indices_tensor_name_value"
    training_pipeline.model_to_upload.explanation_spec.metadata.inputs.value.dense_shape_tensor_name = "dense_shape_tensor_name_value"
    training_pipeline.model_to_upload.explanation_spec.metadata.inputs.value.index_feature_mapping = ['index_feature_mapping_value1', 'index_feature_mapping_value2']
    training_pipeline.model_to_upload.explanation_spec.metadata.inputs.value.encoded_tensor_name = "encoded_tensor_name_value"
    training_pipeline.model_to_upload.explanation_spec.metadata.inputs.value.encoded_baselines.null_value = "NULL_VALUE"
    training_pipeline.model_to_upload.explanation_spec.metadata.inputs.value.encoded_baselines.number_value = 0.1285
    training_pipeline.model_to_upload.explanation_spec.metadata.inputs.value.encoded_baselines.string_value = "string_value_value"
    training_pipeline.model_to_upload.explanation_spec.metadata.inputs.value.encoded_baselines.bool_value = True
    training_pipeline.model_to_upload.explanation_spec.metadata.inputs.value.encoded_baselines.struct_value.fields.key = "key_value"
    training_pipeline.model_to_upload.explanation_spec.metadata.inputs.value.encoded_baselines.struct_value.fields.value = "struct_pb2.Value(null_value=struct_pb2.NullValue.NULL_VALUE)"
    training_pipeline.model_to_upload.explanation_spec.metadata.inputs.value.encoded_baselines.list_value.values = "[struct_pb2.Value(null_value=struct_pb2.NullValue.NULL_VALUE)]"
    training_pipeline.model_to_upload.explanation_spec.metadata.inputs.value.visualization.type_ = "OUTLINES"
    training_pipeline.model_to_upload.explanation_spec.metadata.inputs.value.visualization.polarity = "BOTH"
    training_pipeline.model_to_upload.explanation_spec.metadata.inputs.value.visualization.color_map = "PINK_WHITE_GREEN"
    training_pipeline.model_to_upload.explanation_spec.metadata.inputs.value.visualization.clip_percent_upperbound = 0.2459
    training_pipeline.model_to_upload.explanation_spec.metadata.inputs.value.visualization.clip_percent_lowerbound = 0.2456
    training_pipeline.model_to_upload.explanation_spec.metadata.inputs.value.visualization.overlay_type = "MASK_BLACK"
    training_pipeline.model_to_upload.explanation_spec.metadata.inputs.value.group_name = "group_name_value"
    training_pipeline.model_to_upload.explanation_spec.metadata.outputs.key = "key_value"
    training_pipeline.model_to_upload.explanation_spec.metadata.outputs.value.index_display_name_mapping.null_value = "NULL_VALUE"
    training_pipeline.model_to_upload.explanation_spec.metadata.outputs.value.index_display_name_mapping.number_value = 0.1285
    training_pipeline.model_to_upload.explanation_spec.metadata.outputs.value.index_display_name_mapping.string_value = "string_value_value"
    training_pipeline.model_to_upload.explanation_spec.metadata.outputs.value.index_display_name_mapping.bool_value = True
    training_pipeline.model_to_upload.explanation_spec.metadata.outputs.value.index_display_name_mapping.struct_value.fields.key = "key_value"
    training_pipeline.model_to_upload.explanation_spec.metadata.outputs.value.index_display_name_mapping.struct_value.fields.value = "struct_pb2.Value(null_value=struct_pb2.NullValue.NULL_VALUE)"
    training_pipeline.model_to_upload.explanation_spec.metadata.outputs.value.index_display_name_mapping.list_value.values = "[struct_pb2.Value(null_value=struct_pb2.NullValue.NULL_VALUE)]"
    training_pipeline.model_to_upload.explanation_spec.metadata.outputs.value.display_name_mapping_key = "display_name_mapping_key_value"
    training_pipeline.model_to_upload.explanation_spec.metadata.outputs.value.output_tensor_name = "output_tensor_name_value"
    training_pipeline.model_to_upload.explanation_spec.metadata.feature_attributions_schema_uri = "feature_attributions_schema_uri_value"
    training_pipeline.model_to_upload.explanation_spec.metadata.latent_space_source = "latent_space_source_value"
    training_pipeline.model_to_upload.etag = "etag_value"
    training_pipeline.model_to_upload.labels.key = "key_value"
    training_pipeline.model_to_upload.labels.value = "value_value"
    training_pipeline.model_to_upload.data_stats.training_data_items_count = 2654
    training_pipeline.model_to_upload.data_stats.validation_data_items_count = 2861
    training_pipeline.model_to_upload.data_stats.test_data_items_count = 2242
    training_pipeline.model_to_upload.data_stats.training_annotations_count = 2801
    training_pipeline.model_to_upload.data_stats.validation_annotations_count = 3008
    training_pipeline.model_to_upload.data_stats.test_annotations_count = 2389
    training_pipeline.model_to_upload.encryption_spec.kms_key_name = "kms_key_name_value"
    training_pipeline.model_to_upload.model_source_info.source_type = "MARKETPLACE"
    training_pipeline.model_to_upload.model_source_info.copy = True
    training_pipeline.model_to_upload.original_model_info.model = "model_value"
    training_pipeline.model_to_upload.metadata_artifact = "metadata_artifact_value"
    training_pipeline.model_to_upload.base_model_source.model_garden_source.public_model_name = "public_model_name_value"
    training_pipeline.model_to_upload.base_model_source.genie_source.base_model_uri = "base_model_uri_value"
    training_pipeline.model_id = "model_id_value"
    training_pipeline.parent_model = "parent_model_value"
    training_pipeline.state = "PIPELINE_STATE_PAUSED"
    training_pipeline.error.code = 411
    training_pipeline.error.message = "message_value"
    training_pipeline.error.details.type_url = "type.googleapis.com/google.protobuf.Empty"
    training_pipeline.error.details.value = b'value_blob'
    training_pipeline.create_time.seconds = 751
    training_pipeline.create_time.nanos = 543
    training_pipeline.start_time.seconds = 751
    training_pipeline.start_time.nanos = 543
    training_pipeline.end_time.seconds = 751
    training_pipeline.end_time.nanos = 543
    training_pipeline.update_time.seconds = 751
    training_pipeline.update_time.nanos = 543
    training_pipeline.labels.key = "key_value"
    training_pipeline.labels.value = "value_value"
    training_pipeline.encryption_spec.kms_key_name = "kms_key_name_value"

    request = aiplatform_v1.CreateTrainingPipelineRequest(
        parent="parent_value",
        training_pipeline=training_pipeline,
    )

    # Make the request
    response = client.create_training_pipeline(request=request)

    # Handle the response
    print(response)

# [END aiplatform_v1_generated_PipelineService_CreateTrainingPipeline_sync]

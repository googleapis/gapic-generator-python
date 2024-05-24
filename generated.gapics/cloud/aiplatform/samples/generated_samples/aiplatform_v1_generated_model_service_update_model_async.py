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
# Snippet for UpdateModel
# NOTE: This snippet has been automatically generated for illustrative purposes only.
# It may require modifications to work in your environment.

# To install the latest published package dependency, execute the following:
#   python3 -m pip install google-cloud-aiplatform


# [START aiplatform_v1_generated_ModelService_UpdateModel_async]
# This snippet has been automatically generated and should be regarded as a
# code template only.
# It will require modifications to work:
# - It may require correct/in-range values for request initialization.
# - It may require specifying regional endpoints when creating the service
#   client as shown in:
#   https://googleapis.dev/python/google-api-core/latest/client_options.html
from google.cloud import aiplatform_v1


async def sample_update_model():
    # Create a client
    client = aiplatform_v1.ModelServiceAsyncClient()

    # Initialize request argument(s)
    model = aiplatform_v1.Model()
    model.name = "name_value"
    model.version_id = "version_id_value"
    model.version_aliases = ['version_aliases_value1', 'version_aliases_value2']
    model.version_create_time.seconds = 751
    model.version_create_time.nanos = 543
    model.version_update_time.seconds = 751
    model.version_update_time.nanos = 543
    model.display_name = "display_name_value"
    model.description = "description_value"
    model.version_description = "version_description_value"
    model.predict_schemata.instance_schema_uri = "instance_schema_uri_value"
    model.predict_schemata.parameters_schema_uri = "parameters_schema_uri_value"
    model.predict_schemata.prediction_schema_uri = "prediction_schema_uri_value"
    model.metadata_schema_uri = "metadata_schema_uri_value"
    model.metadata.null_value = "NULL_VALUE"
    model.metadata.number_value = 0.1285
    model.metadata.string_value = "string_value_value"
    model.metadata.bool_value = True
    model.metadata.struct_value.fields.key = "key_value"
    model.metadata.struct_value.fields.value = "struct_pb2.Value(null_value=struct_pb2.NullValue.NULL_VALUE)"
    model.metadata.list_value.values = "[struct_pb2.Value(null_value=struct_pb2.NullValue.NULL_VALUE)]"
    model.supported_export_formats.id = "id_value"
    model.supported_export_formats.exportable_contents = ['IMAGE']
    model.training_pipeline = "training_pipeline_value"
    model.pipeline_job = "pipeline_job_value"
    model.container_spec.image_uri = "image_uri_value"
    model.container_spec.command = ['command_value1', 'command_value2']
    model.container_spec.args = ['args_value1', 'args_value2']
    model.container_spec.env.name = "name_value"
    model.container_spec.env.value = "value_value"
    model.container_spec.ports.container_port = 1511
    model.container_spec.predict_route = "predict_route_value"
    model.container_spec.health_route = "health_route_value"
    model.container_spec.grpc_ports.container_port = 1511
    model.container_spec.deployment_timeout.seconds = 751
    model.container_spec.deployment_timeout.nanos = 543
    model.container_spec.shared_memory_size_mb = 2231
    model.container_spec.startup_probe.exec_.command = ['command_value1', 'command_value2']
    model.container_spec.startup_probe.period_seconds = 1489
    model.container_spec.startup_probe.timeout_seconds = 1621
    model.container_spec.health_probe.exec_.command = ['command_value1', 'command_value2']
    model.container_spec.health_probe.period_seconds = 1489
    model.container_spec.health_probe.timeout_seconds = 1621
    model.artifact_uri = "artifact_uri_value"
    model.supported_deployment_resources_types = ['SHARED_RESOURCES']
    model.supported_input_storage_formats = ['supported_input_storage_formats_value1', 'supported_input_storage_formats_value2']
    model.supported_output_storage_formats = ['supported_output_storage_formats_value1', 'supported_output_storage_formats_value2']
    model.create_time.seconds = 751
    model.create_time.nanos = 543
    model.update_time.seconds = 751
    model.update_time.nanos = 543
    model.deployed_models.endpoint = "endpoint_value"
    model.deployed_models.deployed_model_id = "deployed_model_id_value"
    model.explanation_spec.parameters.sampled_shapley_attribution.path_count = 1077
    model.explanation_spec.parameters.integrated_gradients_attribution.step_count = 1092
    model.explanation_spec.parameters.integrated_gradients_attribution.smooth_grad_config.noise_sigma = 0.11660000000000001
    model.explanation_spec.parameters.integrated_gradients_attribution.smooth_grad_config.feature_noise_sigma.noise_sigma.name = "name_value"
    model.explanation_spec.parameters.integrated_gradients_attribution.smooth_grad_config.feature_noise_sigma.noise_sigma.sigma = 0.529
    model.explanation_spec.parameters.integrated_gradients_attribution.smooth_grad_config.noisy_sample_count = 1947
    model.explanation_spec.parameters.integrated_gradients_attribution.blur_baseline_config.max_blur_sigma = 0.1482
    model.explanation_spec.parameters.xrai_attribution.step_count = 1092
    model.explanation_spec.parameters.xrai_attribution.smooth_grad_config.noise_sigma = 0.11660000000000001
    model.explanation_spec.parameters.xrai_attribution.smooth_grad_config.feature_noise_sigma.noise_sigma.name = "name_value"
    model.explanation_spec.parameters.xrai_attribution.smooth_grad_config.feature_noise_sigma.noise_sigma.sigma = 0.529
    model.explanation_spec.parameters.xrai_attribution.smooth_grad_config.noisy_sample_count = 1947
    model.explanation_spec.parameters.xrai_attribution.blur_baseline_config.max_blur_sigma = 0.1482
    model.explanation_spec.parameters.examples.example_gcs_source.data_format = "JSONL"
    model.explanation_spec.parameters.examples.example_gcs_source.gcs_source.uris = ['uris_value1', 'uris_value2']
    model.explanation_spec.parameters.examples.nearest_neighbor_search_config.null_value = "NULL_VALUE"
    model.explanation_spec.parameters.examples.nearest_neighbor_search_config.number_value = 0.1285
    model.explanation_spec.parameters.examples.nearest_neighbor_search_config.string_value = "string_value_value"
    model.explanation_spec.parameters.examples.nearest_neighbor_search_config.bool_value = True
    model.explanation_spec.parameters.examples.nearest_neighbor_search_config.struct_value.fields.key = "key_value"
    model.explanation_spec.parameters.examples.nearest_neighbor_search_config.struct_value.fields.value = "struct_pb2.Value(null_value=struct_pb2.NullValue.NULL_VALUE)"
    model.explanation_spec.parameters.examples.nearest_neighbor_search_config.list_value.values = "[struct_pb2.Value(null_value=struct_pb2.NullValue.NULL_VALUE)]"
    model.explanation_spec.parameters.examples.presets.query = "FAST"
    model.explanation_spec.parameters.examples.presets.modality = "TABULAR"
    model.explanation_spec.parameters.examples.neighbor_count = 1494
    model.explanation_spec.parameters.top_k = 541
    model.explanation_spec.parameters.output_indices.values.null_value = "NULL_VALUE"
    model.explanation_spec.parameters.output_indices.values.number_value = 0.1285
    model.explanation_spec.parameters.output_indices.values.string_value = "string_value_value"
    model.explanation_spec.parameters.output_indices.values.bool_value = True
    model.explanation_spec.parameters.output_indices.values.struct_value.fields.key = "key_value"
    model.explanation_spec.parameters.output_indices.values.struct_value.fields.value = "struct_pb2.Value(null_value=struct_pb2.NullValue.NULL_VALUE)"
    model.explanation_spec.parameters.output_indices.values.list_value = "struct_pb2.ListValue(values=[struct_pb2.Value(null_value=struct_pb2.NullValue.NULL_VALUE)])"
    model.explanation_spec.metadata.inputs.key = "key_value"
    model.explanation_spec.metadata.inputs.value.input_baselines.null_value = "NULL_VALUE"
    model.explanation_spec.metadata.inputs.value.input_baselines.number_value = 0.1285
    model.explanation_spec.metadata.inputs.value.input_baselines.string_value = "string_value_value"
    model.explanation_spec.metadata.inputs.value.input_baselines.bool_value = True
    model.explanation_spec.metadata.inputs.value.input_baselines.struct_value.fields.key = "key_value"
    model.explanation_spec.metadata.inputs.value.input_baselines.struct_value.fields.value = "struct_pb2.Value(null_value=struct_pb2.NullValue.NULL_VALUE)"
    model.explanation_spec.metadata.inputs.value.input_baselines.list_value.values = "[struct_pb2.Value(null_value=struct_pb2.NullValue.NULL_VALUE)]"
    model.explanation_spec.metadata.inputs.value.input_tensor_name = "input_tensor_name_value"
    model.explanation_spec.metadata.inputs.value.encoding = "CONCAT_EMBEDDING"
    model.explanation_spec.metadata.inputs.value.modality = "modality_value"
    model.explanation_spec.metadata.inputs.value.feature_value_domain.min_value = 0.96
    model.explanation_spec.metadata.inputs.value.feature_value_domain.max_value = 0.962
    model.explanation_spec.metadata.inputs.value.feature_value_domain.original_mean = 0.1365
    model.explanation_spec.metadata.inputs.value.feature_value_domain.original_stddev = 0.1598
    model.explanation_spec.metadata.inputs.value.indices_tensor_name = "indices_tensor_name_value"
    model.explanation_spec.metadata.inputs.value.dense_shape_tensor_name = "dense_shape_tensor_name_value"
    model.explanation_spec.metadata.inputs.value.index_feature_mapping = ['index_feature_mapping_value1', 'index_feature_mapping_value2']
    model.explanation_spec.metadata.inputs.value.encoded_tensor_name = "encoded_tensor_name_value"
    model.explanation_spec.metadata.inputs.value.encoded_baselines.null_value = "NULL_VALUE"
    model.explanation_spec.metadata.inputs.value.encoded_baselines.number_value = 0.1285
    model.explanation_spec.metadata.inputs.value.encoded_baselines.string_value = "string_value_value"
    model.explanation_spec.metadata.inputs.value.encoded_baselines.bool_value = True
    model.explanation_spec.metadata.inputs.value.encoded_baselines.struct_value.fields.key = "key_value"
    model.explanation_spec.metadata.inputs.value.encoded_baselines.struct_value.fields.value = "struct_pb2.Value(null_value=struct_pb2.NullValue.NULL_VALUE)"
    model.explanation_spec.metadata.inputs.value.encoded_baselines.list_value.values = "[struct_pb2.Value(null_value=struct_pb2.NullValue.NULL_VALUE)]"
    model.explanation_spec.metadata.inputs.value.visualization.type_ = "OUTLINES"
    model.explanation_spec.metadata.inputs.value.visualization.polarity = "BOTH"
    model.explanation_spec.metadata.inputs.value.visualization.color_map = "PINK_WHITE_GREEN"
    model.explanation_spec.metadata.inputs.value.visualization.clip_percent_upperbound = 0.2459
    model.explanation_spec.metadata.inputs.value.visualization.clip_percent_lowerbound = 0.2456
    model.explanation_spec.metadata.inputs.value.visualization.overlay_type = "MASK_BLACK"
    model.explanation_spec.metadata.inputs.value.group_name = "group_name_value"
    model.explanation_spec.metadata.outputs.key = "key_value"
    model.explanation_spec.metadata.outputs.value.index_display_name_mapping.null_value = "NULL_VALUE"
    model.explanation_spec.metadata.outputs.value.index_display_name_mapping.number_value = 0.1285
    model.explanation_spec.metadata.outputs.value.index_display_name_mapping.string_value = "string_value_value"
    model.explanation_spec.metadata.outputs.value.index_display_name_mapping.bool_value = True
    model.explanation_spec.metadata.outputs.value.index_display_name_mapping.struct_value.fields.key = "key_value"
    model.explanation_spec.metadata.outputs.value.index_display_name_mapping.struct_value.fields.value = "struct_pb2.Value(null_value=struct_pb2.NullValue.NULL_VALUE)"
    model.explanation_spec.metadata.outputs.value.index_display_name_mapping.list_value.values = "[struct_pb2.Value(null_value=struct_pb2.NullValue.NULL_VALUE)]"
    model.explanation_spec.metadata.outputs.value.display_name_mapping_key = "display_name_mapping_key_value"
    model.explanation_spec.metadata.outputs.value.output_tensor_name = "output_tensor_name_value"
    model.explanation_spec.metadata.feature_attributions_schema_uri = "feature_attributions_schema_uri_value"
    model.explanation_spec.metadata.latent_space_source = "latent_space_source_value"
    model.etag = "etag_value"
    model.labels.key = "key_value"
    model.labels.value = "value_value"
    model.data_stats.training_data_items_count = 2654
    model.data_stats.validation_data_items_count = 2861
    model.data_stats.test_data_items_count = 2242
    model.data_stats.training_annotations_count = 2801
    model.data_stats.validation_annotations_count = 3008
    model.data_stats.test_annotations_count = 2389
    model.encryption_spec.kms_key_name = "kms_key_name_value"
    model.model_source_info.source_type = "MARKETPLACE"
    model.model_source_info.copy = True
    model.original_model_info.model = "model_value"
    model.metadata_artifact = "metadata_artifact_value"
    model.base_model_source.model_garden_source.public_model_name = "public_model_name_value"
    model.base_model_source.genie_source.base_model_uri = "base_model_uri_value"

    update_mask = aiplatform_v1.FieldMask()
    update_mask.paths = ['paths_value1', 'paths_value2']

    request = aiplatform_v1.UpdateModelRequest(
        model=model,
        update_mask=update_mask,
    )

    # Make the request
    response = await client.update_model(request=request)

    # Handle the response
    print(response)

# [END aiplatform_v1_generated_ModelService_UpdateModel_async]

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
# Snippet for MutateDeployedModel
# NOTE: This snippet has been automatically generated for illustrative purposes only.
# It may require modifications to work in your environment.

# To install the latest published package dependency, execute the following:
#   python3 -m pip install google-cloud-aiplatform


# [START aiplatform_v1_generated_EndpointService_MutateDeployedModel_async]
# This snippet has been automatically generated and should be regarded as a
# code template only.
# It will require modifications to work:
# - It may require correct/in-range values for request initialization.
# - It may require specifying regional endpoints when creating the service
#   client as shown in:
#   https://googleapis.dev/python/google-api-core/latest/client_options.html
from google.cloud import aiplatform_v1


async def sample_mutate_deployed_model():
    # Create a client
    client = aiplatform_v1.EndpointServiceAsyncClient()

    # Initialize request argument(s)
    deployed_model = aiplatform_v1.DeployedModel()
    deployed_model.dedicated_resources.machine_spec.machine_type = "machine_type_value"
    deployed_model.dedicated_resources.machine_spec.accelerator_type = "TPU_V5_LITEPOD"
    deployed_model.dedicated_resources.machine_spec.accelerator_count = 1805
    deployed_model.dedicated_resources.machine_spec.tpu_topology = "tpu_topology_value"
    deployed_model.dedicated_resources.min_replica_count = 1803
    deployed_model.dedicated_resources.max_replica_count = 1805
    deployed_model.dedicated_resources.autoscaling_metric_specs.metric_name = "metric_name_value"
    deployed_model.dedicated_resources.autoscaling_metric_specs.target = 647
    deployed_model.automatic_resources.min_replica_count = 1803
    deployed_model.automatic_resources.max_replica_count = 1805
    deployed_model.shared_resources = "shared_resources_value"
    deployed_model.id = "id_value"
    deployed_model.model = "model_value"
    deployed_model.model_version_id = "model_version_id_value"
    deployed_model.display_name = "display_name_value"
    deployed_model.create_time.seconds = 751
    deployed_model.create_time.nanos = 543
    deployed_model.explanation_spec.parameters.sampled_shapley_attribution.path_count = 1077
    deployed_model.explanation_spec.parameters.integrated_gradients_attribution.step_count = 1092
    deployed_model.explanation_spec.parameters.integrated_gradients_attribution.smooth_grad_config.noise_sigma = 0.11660000000000001
    deployed_model.explanation_spec.parameters.integrated_gradients_attribution.smooth_grad_config.feature_noise_sigma.noise_sigma.name = "name_value"
    deployed_model.explanation_spec.parameters.integrated_gradients_attribution.smooth_grad_config.feature_noise_sigma.noise_sigma.sigma = 0.529
    deployed_model.explanation_spec.parameters.integrated_gradients_attribution.smooth_grad_config.noisy_sample_count = 1947
    deployed_model.explanation_spec.parameters.integrated_gradients_attribution.blur_baseline_config.max_blur_sigma = 0.1482
    deployed_model.explanation_spec.parameters.xrai_attribution.step_count = 1092
    deployed_model.explanation_spec.parameters.xrai_attribution.smooth_grad_config.noise_sigma = 0.11660000000000001
    deployed_model.explanation_spec.parameters.xrai_attribution.smooth_grad_config.feature_noise_sigma.noise_sigma.name = "name_value"
    deployed_model.explanation_spec.parameters.xrai_attribution.smooth_grad_config.feature_noise_sigma.noise_sigma.sigma = 0.529
    deployed_model.explanation_spec.parameters.xrai_attribution.smooth_grad_config.noisy_sample_count = 1947
    deployed_model.explanation_spec.parameters.xrai_attribution.blur_baseline_config.max_blur_sigma = 0.1482
    deployed_model.explanation_spec.parameters.examples.example_gcs_source.data_format = "JSONL"
    deployed_model.explanation_spec.parameters.examples.example_gcs_source.gcs_source.uris = ['uris_value1', 'uris_value2']
    deployed_model.explanation_spec.parameters.examples.nearest_neighbor_search_config.null_value = "NULL_VALUE"
    deployed_model.explanation_spec.parameters.examples.nearest_neighbor_search_config.number_value = 0.1285
    deployed_model.explanation_spec.parameters.examples.nearest_neighbor_search_config.string_value = "string_value_value"
    deployed_model.explanation_spec.parameters.examples.nearest_neighbor_search_config.bool_value = True
    deployed_model.explanation_spec.parameters.examples.nearest_neighbor_search_config.struct_value.fields.key = "key_value"
    deployed_model.explanation_spec.parameters.examples.nearest_neighbor_search_config.struct_value.fields.value = "struct_pb2.Value(null_value=struct_pb2.NullValue.NULL_VALUE)"
    deployed_model.explanation_spec.parameters.examples.nearest_neighbor_search_config.list_value.values = "[struct_pb2.Value(null_value=struct_pb2.NullValue.NULL_VALUE)]"
    deployed_model.explanation_spec.parameters.examples.presets.query = "FAST"
    deployed_model.explanation_spec.parameters.examples.presets.modality = "TABULAR"
    deployed_model.explanation_spec.parameters.examples.neighbor_count = 1494
    deployed_model.explanation_spec.parameters.top_k = 541
    deployed_model.explanation_spec.parameters.output_indices.values.null_value = "NULL_VALUE"
    deployed_model.explanation_spec.parameters.output_indices.values.number_value = 0.1285
    deployed_model.explanation_spec.parameters.output_indices.values.string_value = "string_value_value"
    deployed_model.explanation_spec.parameters.output_indices.values.bool_value = True
    deployed_model.explanation_spec.parameters.output_indices.values.struct_value.fields.key = "key_value"
    deployed_model.explanation_spec.parameters.output_indices.values.struct_value.fields.value = "struct_pb2.Value(null_value=struct_pb2.NullValue.NULL_VALUE)"
    deployed_model.explanation_spec.parameters.output_indices.values.list_value = "struct_pb2.ListValue(values=[struct_pb2.Value(null_value=struct_pb2.NullValue.NULL_VALUE)])"
    deployed_model.explanation_spec.metadata.inputs.key = "key_value"
    deployed_model.explanation_spec.metadata.inputs.value.input_baselines.null_value = "NULL_VALUE"
    deployed_model.explanation_spec.metadata.inputs.value.input_baselines.number_value = 0.1285
    deployed_model.explanation_spec.metadata.inputs.value.input_baselines.string_value = "string_value_value"
    deployed_model.explanation_spec.metadata.inputs.value.input_baselines.bool_value = True
    deployed_model.explanation_spec.metadata.inputs.value.input_baselines.struct_value.fields.key = "key_value"
    deployed_model.explanation_spec.metadata.inputs.value.input_baselines.struct_value.fields.value = "struct_pb2.Value(null_value=struct_pb2.NullValue.NULL_VALUE)"
    deployed_model.explanation_spec.metadata.inputs.value.input_baselines.list_value.values = "[struct_pb2.Value(null_value=struct_pb2.NullValue.NULL_VALUE)]"
    deployed_model.explanation_spec.metadata.inputs.value.input_tensor_name = "input_tensor_name_value"
    deployed_model.explanation_spec.metadata.inputs.value.encoding = "CONCAT_EMBEDDING"
    deployed_model.explanation_spec.metadata.inputs.value.modality = "modality_value"
    deployed_model.explanation_spec.metadata.inputs.value.feature_value_domain.min_value = 0.96
    deployed_model.explanation_spec.metadata.inputs.value.feature_value_domain.max_value = 0.962
    deployed_model.explanation_spec.metadata.inputs.value.feature_value_domain.original_mean = 0.1365
    deployed_model.explanation_spec.metadata.inputs.value.feature_value_domain.original_stddev = 0.1598
    deployed_model.explanation_spec.metadata.inputs.value.indices_tensor_name = "indices_tensor_name_value"
    deployed_model.explanation_spec.metadata.inputs.value.dense_shape_tensor_name = "dense_shape_tensor_name_value"
    deployed_model.explanation_spec.metadata.inputs.value.index_feature_mapping = ['index_feature_mapping_value1', 'index_feature_mapping_value2']
    deployed_model.explanation_spec.metadata.inputs.value.encoded_tensor_name = "encoded_tensor_name_value"
    deployed_model.explanation_spec.metadata.inputs.value.encoded_baselines.null_value = "NULL_VALUE"
    deployed_model.explanation_spec.metadata.inputs.value.encoded_baselines.number_value = 0.1285
    deployed_model.explanation_spec.metadata.inputs.value.encoded_baselines.string_value = "string_value_value"
    deployed_model.explanation_spec.metadata.inputs.value.encoded_baselines.bool_value = True
    deployed_model.explanation_spec.metadata.inputs.value.encoded_baselines.struct_value.fields.key = "key_value"
    deployed_model.explanation_spec.metadata.inputs.value.encoded_baselines.struct_value.fields.value = "struct_pb2.Value(null_value=struct_pb2.NullValue.NULL_VALUE)"
    deployed_model.explanation_spec.metadata.inputs.value.encoded_baselines.list_value.values = "[struct_pb2.Value(null_value=struct_pb2.NullValue.NULL_VALUE)]"
    deployed_model.explanation_spec.metadata.inputs.value.visualization.type_ = "OUTLINES"
    deployed_model.explanation_spec.metadata.inputs.value.visualization.polarity = "BOTH"
    deployed_model.explanation_spec.metadata.inputs.value.visualization.color_map = "PINK_WHITE_GREEN"
    deployed_model.explanation_spec.metadata.inputs.value.visualization.clip_percent_upperbound = 0.2459
    deployed_model.explanation_spec.metadata.inputs.value.visualization.clip_percent_lowerbound = 0.2456
    deployed_model.explanation_spec.metadata.inputs.value.visualization.overlay_type = "MASK_BLACK"
    deployed_model.explanation_spec.metadata.inputs.value.group_name = "group_name_value"
    deployed_model.explanation_spec.metadata.outputs.key = "key_value"
    deployed_model.explanation_spec.metadata.outputs.value.index_display_name_mapping.null_value = "NULL_VALUE"
    deployed_model.explanation_spec.metadata.outputs.value.index_display_name_mapping.number_value = 0.1285
    deployed_model.explanation_spec.metadata.outputs.value.index_display_name_mapping.string_value = "string_value_value"
    deployed_model.explanation_spec.metadata.outputs.value.index_display_name_mapping.bool_value = True
    deployed_model.explanation_spec.metadata.outputs.value.index_display_name_mapping.struct_value.fields.key = "key_value"
    deployed_model.explanation_spec.metadata.outputs.value.index_display_name_mapping.struct_value.fields.value = "struct_pb2.Value(null_value=struct_pb2.NullValue.NULL_VALUE)"
    deployed_model.explanation_spec.metadata.outputs.value.index_display_name_mapping.list_value.values = "[struct_pb2.Value(null_value=struct_pb2.NullValue.NULL_VALUE)]"
    deployed_model.explanation_spec.metadata.outputs.value.display_name_mapping_key = "display_name_mapping_key_value"
    deployed_model.explanation_spec.metadata.outputs.value.output_tensor_name = "output_tensor_name_value"
    deployed_model.explanation_spec.metadata.feature_attributions_schema_uri = "feature_attributions_schema_uri_value"
    deployed_model.explanation_spec.metadata.latent_space_source = "latent_space_source_value"
    deployed_model.disable_explanations = True
    deployed_model.service_account = "service_account_value"
    deployed_model.disable_container_logging = True
    deployed_model.enable_access_logging = True
    deployed_model.private_endpoints.predict_http_uri = "predict_http_uri_value"
    deployed_model.private_endpoints.explain_http_uri = "explain_http_uri_value"
    deployed_model.private_endpoints.health_http_uri = "health_http_uri_value"
    deployed_model.private_endpoints.service_attachment = "service_attachment_value"

    update_mask = aiplatform_v1.FieldMask()
    update_mask.paths = ['paths_value1', 'paths_value2']

    request = aiplatform_v1.MutateDeployedModelRequest(
        endpoint="endpoint_value",
        deployed_model=deployed_model,
        update_mask=update_mask,
    )

    # Make the request
    operation = client.mutate_deployed_model(request=request)

    print("Waiting for operation to complete...")

    response = (await operation).result()

    # Handle the response
    print(response)

# [END aiplatform_v1_generated_EndpointService_MutateDeployedModel_async]

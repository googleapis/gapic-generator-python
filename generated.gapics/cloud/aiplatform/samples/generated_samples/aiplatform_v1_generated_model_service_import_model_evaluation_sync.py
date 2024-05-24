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
# Snippet for ImportModelEvaluation
# NOTE: This snippet has been automatically generated for illustrative purposes only.
# It may require modifications to work in your environment.

# To install the latest published package dependency, execute the following:
#   python3 -m pip install google-cloud-aiplatform


# [START aiplatform_v1_generated_ModelService_ImportModelEvaluation_sync]
# This snippet has been automatically generated and should be regarded as a
# code template only.
# It will require modifications to work:
# - It may require correct/in-range values for request initialization.
# - It may require specifying regional endpoints when creating the service
#   client as shown in:
#   https://googleapis.dev/python/google-api-core/latest/client_options.html
from google.cloud import aiplatform_v1


def sample_import_model_evaluation():
    # Create a client
    client = aiplatform_v1.ModelServiceClient()

    # Initialize request argument(s)
    model_evaluation = aiplatform_v1.ModelEvaluation()
    model_evaluation.name = "name_value"
    model_evaluation.display_name = "display_name_value"
    model_evaluation.metrics_schema_uri = "metrics_schema_uri_value"
    model_evaluation.metrics.null_value = "NULL_VALUE"
    model_evaluation.metrics.number_value = 0.1285
    model_evaluation.metrics.string_value = "string_value_value"
    model_evaluation.metrics.bool_value = True
    model_evaluation.metrics.struct_value.fields.key = "key_value"
    model_evaluation.metrics.struct_value.fields.value = "struct_pb2.Value(null_value=struct_pb2.NullValue.NULL_VALUE)"
    model_evaluation.metrics.list_value.values = "[struct_pb2.Value(null_value=struct_pb2.NullValue.NULL_VALUE)]"
    model_evaluation.create_time.seconds = 751
    model_evaluation.create_time.nanos = 543
    model_evaluation.slice_dimensions = ['slice_dimensions_value1', 'slice_dimensions_value2']
    model_evaluation.data_item_schema_uri = "data_item_schema_uri_value"
    model_evaluation.annotation_schema_uri = "annotation_schema_uri_value"
    model_evaluation.model_explanation.mean_attributions.baseline_output_value = 0.2255
    model_evaluation.model_explanation.mean_attributions.instance_output_value = 0.2273
    model_evaluation.model_explanation.mean_attributions.feature_attributions.null_value = "NULL_VALUE"
    model_evaluation.model_explanation.mean_attributions.feature_attributions.number_value = 0.1285
    model_evaluation.model_explanation.mean_attributions.feature_attributions.string_value = "string_value_value"
    model_evaluation.model_explanation.mean_attributions.feature_attributions.bool_value = True
    model_evaluation.model_explanation.mean_attributions.feature_attributions.struct_value.fields.key = "key_value"
    model_evaluation.model_explanation.mean_attributions.feature_attributions.struct_value.fields.value = "struct_pb2.Value(null_value=struct_pb2.NullValue.NULL_VALUE)"
    model_evaluation.model_explanation.mean_attributions.feature_attributions.list_value.values = "[struct_pb2.Value(null_value=struct_pb2.NullValue.NULL_VALUE)]"
    model_evaluation.model_explanation.mean_attributions.output_index = [1321, 1322]
    model_evaluation.model_explanation.mean_attributions.output_display_name = "output_display_name_value"
    model_evaluation.model_explanation.mean_attributions.approximation_error = 0.2068
    model_evaluation.model_explanation.mean_attributions.output_name = "output_name_value"
    model_evaluation.explanation_specs.explanation_type = "explanation_type_value"
    model_evaluation.explanation_specs.explanation_spec.parameters.sampled_shapley_attribution.path_count = 1077
    model_evaluation.explanation_specs.explanation_spec.parameters.integrated_gradients_attribution.step_count = 1092
    model_evaluation.explanation_specs.explanation_spec.parameters.integrated_gradients_attribution.smooth_grad_config.noise_sigma = 0.11660000000000001
    model_evaluation.explanation_specs.explanation_spec.parameters.integrated_gradients_attribution.smooth_grad_config.feature_noise_sigma.noise_sigma.name = "name_value"
    model_evaluation.explanation_specs.explanation_spec.parameters.integrated_gradients_attribution.smooth_grad_config.feature_noise_sigma.noise_sigma.sigma = 0.529
    model_evaluation.explanation_specs.explanation_spec.parameters.integrated_gradients_attribution.smooth_grad_config.noisy_sample_count = 1947
    model_evaluation.explanation_specs.explanation_spec.parameters.integrated_gradients_attribution.blur_baseline_config.max_blur_sigma = 0.1482
    model_evaluation.explanation_specs.explanation_spec.parameters.xrai_attribution.step_count = 1092
    model_evaluation.explanation_specs.explanation_spec.parameters.xrai_attribution.smooth_grad_config.noise_sigma = 0.11660000000000001
    model_evaluation.explanation_specs.explanation_spec.parameters.xrai_attribution.smooth_grad_config.feature_noise_sigma.noise_sigma.name = "name_value"
    model_evaluation.explanation_specs.explanation_spec.parameters.xrai_attribution.smooth_grad_config.feature_noise_sigma.noise_sigma.sigma = 0.529
    model_evaluation.explanation_specs.explanation_spec.parameters.xrai_attribution.smooth_grad_config.noisy_sample_count = 1947
    model_evaluation.explanation_specs.explanation_spec.parameters.xrai_attribution.blur_baseline_config.max_blur_sigma = 0.1482
    model_evaluation.explanation_specs.explanation_spec.parameters.examples.example_gcs_source.data_format = "JSONL"
    model_evaluation.explanation_specs.explanation_spec.parameters.examples.example_gcs_source.gcs_source.uris = ['uris_value1', 'uris_value2']
    model_evaluation.explanation_specs.explanation_spec.parameters.examples.nearest_neighbor_search_config.null_value = "NULL_VALUE"
    model_evaluation.explanation_specs.explanation_spec.parameters.examples.nearest_neighbor_search_config.number_value = 0.1285
    model_evaluation.explanation_specs.explanation_spec.parameters.examples.nearest_neighbor_search_config.string_value = "string_value_value"
    model_evaluation.explanation_specs.explanation_spec.parameters.examples.nearest_neighbor_search_config.bool_value = True
    model_evaluation.explanation_specs.explanation_spec.parameters.examples.nearest_neighbor_search_config.struct_value.fields.key = "key_value"
    model_evaluation.explanation_specs.explanation_spec.parameters.examples.nearest_neighbor_search_config.struct_value.fields.value = "struct_pb2.Value(null_value=struct_pb2.NullValue.NULL_VALUE)"
    model_evaluation.explanation_specs.explanation_spec.parameters.examples.nearest_neighbor_search_config.list_value.values = "[struct_pb2.Value(null_value=struct_pb2.NullValue.NULL_VALUE)]"
    model_evaluation.explanation_specs.explanation_spec.parameters.examples.presets.query = "FAST"
    model_evaluation.explanation_specs.explanation_spec.parameters.examples.presets.modality = "TABULAR"
    model_evaluation.explanation_specs.explanation_spec.parameters.examples.neighbor_count = 1494
    model_evaluation.explanation_specs.explanation_spec.parameters.top_k = 541
    model_evaluation.explanation_specs.explanation_spec.parameters.output_indices.values.null_value = "NULL_VALUE"
    model_evaluation.explanation_specs.explanation_spec.parameters.output_indices.values.number_value = 0.1285
    model_evaluation.explanation_specs.explanation_spec.parameters.output_indices.values.string_value = "string_value_value"
    model_evaluation.explanation_specs.explanation_spec.parameters.output_indices.values.bool_value = True
    model_evaluation.explanation_specs.explanation_spec.parameters.output_indices.values.struct_value.fields.key = "key_value"
    model_evaluation.explanation_specs.explanation_spec.parameters.output_indices.values.struct_value.fields.value = "struct_pb2.Value(null_value=struct_pb2.NullValue.NULL_VALUE)"
    model_evaluation.explanation_specs.explanation_spec.parameters.output_indices.values.list_value = "struct_pb2.ListValue(values=[struct_pb2.Value(null_value=struct_pb2.NullValue.NULL_VALUE)])"
    model_evaluation.explanation_specs.explanation_spec.metadata.inputs.key = "key_value"
    model_evaluation.explanation_specs.explanation_spec.metadata.inputs.value.input_baselines.null_value = "NULL_VALUE"
    model_evaluation.explanation_specs.explanation_spec.metadata.inputs.value.input_baselines.number_value = 0.1285
    model_evaluation.explanation_specs.explanation_spec.metadata.inputs.value.input_baselines.string_value = "string_value_value"
    model_evaluation.explanation_specs.explanation_spec.metadata.inputs.value.input_baselines.bool_value = True
    model_evaluation.explanation_specs.explanation_spec.metadata.inputs.value.input_baselines.struct_value.fields.key = "key_value"
    model_evaluation.explanation_specs.explanation_spec.metadata.inputs.value.input_baselines.struct_value.fields.value = "struct_pb2.Value(null_value=struct_pb2.NullValue.NULL_VALUE)"
    model_evaluation.explanation_specs.explanation_spec.metadata.inputs.value.input_baselines.list_value.values = "[struct_pb2.Value(null_value=struct_pb2.NullValue.NULL_VALUE)]"
    model_evaluation.explanation_specs.explanation_spec.metadata.inputs.value.input_tensor_name = "input_tensor_name_value"
    model_evaluation.explanation_specs.explanation_spec.metadata.inputs.value.encoding = "CONCAT_EMBEDDING"
    model_evaluation.explanation_specs.explanation_spec.metadata.inputs.value.modality = "modality_value"
    model_evaluation.explanation_specs.explanation_spec.metadata.inputs.value.feature_value_domain.min_value = 0.96
    model_evaluation.explanation_specs.explanation_spec.metadata.inputs.value.feature_value_domain.max_value = 0.962
    model_evaluation.explanation_specs.explanation_spec.metadata.inputs.value.feature_value_domain.original_mean = 0.1365
    model_evaluation.explanation_specs.explanation_spec.metadata.inputs.value.feature_value_domain.original_stddev = 0.1598
    model_evaluation.explanation_specs.explanation_spec.metadata.inputs.value.indices_tensor_name = "indices_tensor_name_value"
    model_evaluation.explanation_specs.explanation_spec.metadata.inputs.value.dense_shape_tensor_name = "dense_shape_tensor_name_value"
    model_evaluation.explanation_specs.explanation_spec.metadata.inputs.value.index_feature_mapping = ['index_feature_mapping_value1', 'index_feature_mapping_value2']
    model_evaluation.explanation_specs.explanation_spec.metadata.inputs.value.encoded_tensor_name = "encoded_tensor_name_value"
    model_evaluation.explanation_specs.explanation_spec.metadata.inputs.value.encoded_baselines.null_value = "NULL_VALUE"
    model_evaluation.explanation_specs.explanation_spec.metadata.inputs.value.encoded_baselines.number_value = 0.1285
    model_evaluation.explanation_specs.explanation_spec.metadata.inputs.value.encoded_baselines.string_value = "string_value_value"
    model_evaluation.explanation_specs.explanation_spec.metadata.inputs.value.encoded_baselines.bool_value = True
    model_evaluation.explanation_specs.explanation_spec.metadata.inputs.value.encoded_baselines.struct_value.fields.key = "key_value"
    model_evaluation.explanation_specs.explanation_spec.metadata.inputs.value.encoded_baselines.struct_value.fields.value = "struct_pb2.Value(null_value=struct_pb2.NullValue.NULL_VALUE)"
    model_evaluation.explanation_specs.explanation_spec.metadata.inputs.value.encoded_baselines.list_value.values = "[struct_pb2.Value(null_value=struct_pb2.NullValue.NULL_VALUE)]"
    model_evaluation.explanation_specs.explanation_spec.metadata.inputs.value.visualization.type_ = "OUTLINES"
    model_evaluation.explanation_specs.explanation_spec.metadata.inputs.value.visualization.polarity = "BOTH"
    model_evaluation.explanation_specs.explanation_spec.metadata.inputs.value.visualization.color_map = "PINK_WHITE_GREEN"
    model_evaluation.explanation_specs.explanation_spec.metadata.inputs.value.visualization.clip_percent_upperbound = 0.2459
    model_evaluation.explanation_specs.explanation_spec.metadata.inputs.value.visualization.clip_percent_lowerbound = 0.2456
    model_evaluation.explanation_specs.explanation_spec.metadata.inputs.value.visualization.overlay_type = "MASK_BLACK"
    model_evaluation.explanation_specs.explanation_spec.metadata.inputs.value.group_name = "group_name_value"
    model_evaluation.explanation_specs.explanation_spec.metadata.outputs.key = "key_value"
    model_evaluation.explanation_specs.explanation_spec.metadata.outputs.value.index_display_name_mapping.null_value = "NULL_VALUE"
    model_evaluation.explanation_specs.explanation_spec.metadata.outputs.value.index_display_name_mapping.number_value = 0.1285
    model_evaluation.explanation_specs.explanation_spec.metadata.outputs.value.index_display_name_mapping.string_value = "string_value_value"
    model_evaluation.explanation_specs.explanation_spec.metadata.outputs.value.index_display_name_mapping.bool_value = True
    model_evaluation.explanation_specs.explanation_spec.metadata.outputs.value.index_display_name_mapping.struct_value.fields.key = "key_value"
    model_evaluation.explanation_specs.explanation_spec.metadata.outputs.value.index_display_name_mapping.struct_value.fields.value = "struct_pb2.Value(null_value=struct_pb2.NullValue.NULL_VALUE)"
    model_evaluation.explanation_specs.explanation_spec.metadata.outputs.value.index_display_name_mapping.list_value.values = "[struct_pb2.Value(null_value=struct_pb2.NullValue.NULL_VALUE)]"
    model_evaluation.explanation_specs.explanation_spec.metadata.outputs.value.display_name_mapping_key = "display_name_mapping_key_value"
    model_evaluation.explanation_specs.explanation_spec.metadata.outputs.value.output_tensor_name = "output_tensor_name_value"
    model_evaluation.explanation_specs.explanation_spec.metadata.feature_attributions_schema_uri = "feature_attributions_schema_uri_value"
    model_evaluation.explanation_specs.explanation_spec.metadata.latent_space_source = "latent_space_source_value"
    model_evaluation.metadata.null_value = "NULL_VALUE"
    model_evaluation.metadata.number_value = 0.1285
    model_evaluation.metadata.string_value = "string_value_value"
    model_evaluation.metadata.bool_value = True
    model_evaluation.metadata.struct_value.fields.key = "key_value"
    model_evaluation.metadata.struct_value.fields.value = "struct_pb2.Value(null_value=struct_pb2.NullValue.NULL_VALUE)"
    model_evaluation.metadata.list_value.values = "[struct_pb2.Value(null_value=struct_pb2.NullValue.NULL_VALUE)]"

    request = aiplatform_v1.ImportModelEvaluationRequest(
        parent="parent_value",
        model_evaluation=model_evaluation,
    )

    # Make the request
    response = client.import_model_evaluation(request=request)

    # Handle the response
    print(response)

# [END aiplatform_v1_generated_ModelService_ImportModelEvaluation_sync]

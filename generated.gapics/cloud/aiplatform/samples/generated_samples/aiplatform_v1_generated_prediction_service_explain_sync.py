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
# Snippet for Explain
# NOTE: This snippet has been automatically generated for illustrative purposes only.
# It may require modifications to work in your environment.

# To install the latest published package dependency, execute the following:
#   python3 -m pip install google-cloud-aiplatform


# [START aiplatform_v1_generated_PredictionService_Explain_sync]
# This snippet has been automatically generated and should be regarded as a
# code template only.
# It will require modifications to work:
# - It may require correct/in-range values for request initialization.
# - It may require specifying regional endpoints when creating the service
#   client as shown in:
#   https://googleapis.dev/python/google-api-core/latest/client_options.html
from google.cloud import aiplatform_v1


def sample_explain():
    # Create a client
    client = aiplatform_v1.PredictionServiceClient()

    # Initialize request argument(s)
    instances = aiplatform_v1.Value()
    instances.null_value = "NULL_VALUE"
    instances.number_value = 0.1285
    instances.string_value = "string_value_value"
    instances.bool_value = True
    instances.struct_value.fields.key = "key_value"
    instances.struct_value.fields.value = "struct_pb2.Value(null_value=struct_pb2.NullValue.NULL_VALUE)"
    instances.list_value.values = "[struct_pb2.Value(null_value=struct_pb2.NullValue.NULL_VALUE)]"

    parameters = aiplatform_v1.Value()
    parameters.null_value = "NULL_VALUE"
    parameters.number_value = 0.1285
    parameters.string_value = "string_value_value"
    parameters.bool_value = True
    parameters.struct_value.fields.key = "key_value"
    parameters.struct_value.fields.value = "struct_pb2.Value(null_value=struct_pb2.NullValue.NULL_VALUE)"
    parameters.list_value.values = "[struct_pb2.Value(null_value=struct_pb2.NullValue.NULL_VALUE)]"

    explanation_spec_override = aiplatform_v1.ExplanationSpecOverride()
    explanation_spec_override.parameters.sampled_shapley_attribution.path_count = 1077
    explanation_spec_override.parameters.integrated_gradients_attribution.step_count = 1092
    explanation_spec_override.parameters.integrated_gradients_attribution.smooth_grad_config.noise_sigma = 0.11660000000000001
    explanation_spec_override.parameters.integrated_gradients_attribution.smooth_grad_config.feature_noise_sigma.noise_sigma.name = "name_value"
    explanation_spec_override.parameters.integrated_gradients_attribution.smooth_grad_config.feature_noise_sigma.noise_sigma.sigma = 0.529
    explanation_spec_override.parameters.integrated_gradients_attribution.smooth_grad_config.noisy_sample_count = 1947
    explanation_spec_override.parameters.integrated_gradients_attribution.blur_baseline_config.max_blur_sigma = 0.1482
    explanation_spec_override.parameters.xrai_attribution.step_count = 1092
    explanation_spec_override.parameters.xrai_attribution.smooth_grad_config.noise_sigma = 0.11660000000000001
    explanation_spec_override.parameters.xrai_attribution.smooth_grad_config.feature_noise_sigma.noise_sigma.name = "name_value"
    explanation_spec_override.parameters.xrai_attribution.smooth_grad_config.feature_noise_sigma.noise_sigma.sigma = 0.529
    explanation_spec_override.parameters.xrai_attribution.smooth_grad_config.noisy_sample_count = 1947
    explanation_spec_override.parameters.xrai_attribution.blur_baseline_config.max_blur_sigma = 0.1482
    explanation_spec_override.parameters.examples.example_gcs_source.data_format = "JSONL"
    explanation_spec_override.parameters.examples.example_gcs_source.gcs_source.uris = ['uris_value1', 'uris_value2']
    explanation_spec_override.parameters.examples.nearest_neighbor_search_config.null_value = "NULL_VALUE"
    explanation_spec_override.parameters.examples.nearest_neighbor_search_config.number_value = 0.1285
    explanation_spec_override.parameters.examples.nearest_neighbor_search_config.string_value = "string_value_value"
    explanation_spec_override.parameters.examples.nearest_neighbor_search_config.bool_value = True
    explanation_spec_override.parameters.examples.nearest_neighbor_search_config.struct_value.fields.key = "key_value"
    explanation_spec_override.parameters.examples.nearest_neighbor_search_config.struct_value.fields.value = "struct_pb2.Value(null_value=struct_pb2.NullValue.NULL_VALUE)"
    explanation_spec_override.parameters.examples.nearest_neighbor_search_config.list_value.values = "[struct_pb2.Value(null_value=struct_pb2.NullValue.NULL_VALUE)]"
    explanation_spec_override.parameters.examples.presets.query = "FAST"
    explanation_spec_override.parameters.examples.presets.modality = "TABULAR"
    explanation_spec_override.parameters.examples.neighbor_count = 1494
    explanation_spec_override.parameters.top_k = 541
    explanation_spec_override.parameters.output_indices.values.null_value = "NULL_VALUE"
    explanation_spec_override.parameters.output_indices.values.number_value = 0.1285
    explanation_spec_override.parameters.output_indices.values.string_value = "string_value_value"
    explanation_spec_override.parameters.output_indices.values.bool_value = True
    explanation_spec_override.parameters.output_indices.values.struct_value.fields.key = "key_value"
    explanation_spec_override.parameters.output_indices.values.struct_value.fields.value = "struct_pb2.Value(null_value=struct_pb2.NullValue.NULL_VALUE)"
    explanation_spec_override.parameters.output_indices.values.list_value = "struct_pb2.ListValue(values=[struct_pb2.Value(null_value=struct_pb2.NullValue.NULL_VALUE)])"
    explanation_spec_override.metadata.inputs.key = "key_value"
    explanation_spec_override.metadata.inputs.value.input_baselines.null_value = "NULL_VALUE"
    explanation_spec_override.metadata.inputs.value.input_baselines.number_value = 0.1285
    explanation_spec_override.metadata.inputs.value.input_baselines.string_value = "string_value_value"
    explanation_spec_override.metadata.inputs.value.input_baselines.bool_value = True
    explanation_spec_override.metadata.inputs.value.input_baselines.struct_value.fields.key = "key_value"
    explanation_spec_override.metadata.inputs.value.input_baselines.struct_value.fields.value = "struct_pb2.Value(null_value=struct_pb2.NullValue.NULL_VALUE)"
    explanation_spec_override.metadata.inputs.value.input_baselines.list_value.values = "[struct_pb2.Value(null_value=struct_pb2.NullValue.NULL_VALUE)]"
    explanation_spec_override.examples_override.neighbor_count = 1494
    explanation_spec_override.examples_override.crowding_count = 1509
    explanation_spec_override.examples_override.restrictions.namespace_name = "namespace_name_value"
    explanation_spec_override.examples_override.restrictions.allow = ['allow_value1', 'allow_value2']
    explanation_spec_override.examples_override.restrictions.deny = ['deny_value1', 'deny_value2']
    explanation_spec_override.examples_override.return_embeddings = True
    explanation_spec_override.examples_override.data_format = "EMBEDDINGS"

    request = aiplatform_v1.ExplainRequest(
        endpoint="endpoint_value",
        instances=instances,
        parameters=parameters,
        explanation_spec_override=explanation_spec_override,
        deployed_model_id="deployed_model_id_value",
    )

    # Make the request
    response = client.explain(request=request)

    # Handle the response
    print(response)

# [END aiplatform_v1_generated_PredictionService_Explain_sync]

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
# Snippet for BatchImportModelEvaluationSlices
# NOTE: This snippet has been automatically generated for illustrative purposes only.
# It may require modifications to work in your environment.

# To install the latest published package dependency, execute the following:
#   python3 -m pip install google-cloud-aiplatform


# [START aiplatform_v1_generated_ModelService_BatchImportModelEvaluationSlices_sync]
# This snippet has been automatically generated and should be regarded as a
# code template only.
# It will require modifications to work:
# - It may require correct/in-range values for request initialization.
# - It may require specifying regional endpoints when creating the service
#   client as shown in:
#   https://googleapis.dev/python/google-api-core/latest/client_options.html
from google.cloud import aiplatform_v1


def sample_batch_import_model_evaluation_slices():
    # Create a client
    client = aiplatform_v1.ModelServiceClient()

    # Initialize request argument(s)
    model_evaluation_slices = aiplatform_v1.ModelEvaluationSlice()
    model_evaluation_slices.name = "name_value"
    model_evaluation_slices.slice_.dimension = "dimension_value"
    model_evaluation_slices.slice_.value = "value_value"
    model_evaluation_slices.slice_.slice_spec.configs.key = "key_value"
    model_evaluation_slices.slice_.slice_spec.configs.value.value.string_value = "string_value_value"
    model_evaluation_slices.slice_.slice_spec.configs.value.value.float_value = 0.117
    model_evaluation_slices.slice_.slice_spec.configs.value.range_.low = 0.338
    model_evaluation_slices.slice_.slice_spec.configs.value.range_.high = 0.41600000000000004
    model_evaluation_slices.slice_.slice_spec.configs.value.all_values.value = True
    model_evaluation_slices.metrics_schema_uri = "metrics_schema_uri_value"
    model_evaluation_slices.metrics.null_value = "NULL_VALUE"
    model_evaluation_slices.metrics.number_value = 0.1285
    model_evaluation_slices.metrics.string_value = "string_value_value"
    model_evaluation_slices.metrics.bool_value = True
    model_evaluation_slices.metrics.struct_value.fields.key = "key_value"
    model_evaluation_slices.metrics.struct_value.fields.value = "struct_pb2.Value(null_value=struct_pb2.NullValue.NULL_VALUE)"
    model_evaluation_slices.metrics.list_value.values = "[struct_pb2.Value(null_value=struct_pb2.NullValue.NULL_VALUE)]"
    model_evaluation_slices.create_time.seconds = 751
    model_evaluation_slices.create_time.nanos = 543
    model_evaluation_slices.model_explanation.mean_attributions.baseline_output_value = 0.2255
    model_evaluation_slices.model_explanation.mean_attributions.instance_output_value = 0.2273
    model_evaluation_slices.model_explanation.mean_attributions.feature_attributions.null_value = "NULL_VALUE"
    model_evaluation_slices.model_explanation.mean_attributions.feature_attributions.number_value = 0.1285
    model_evaluation_slices.model_explanation.mean_attributions.feature_attributions.string_value = "string_value_value"
    model_evaluation_slices.model_explanation.mean_attributions.feature_attributions.bool_value = True
    model_evaluation_slices.model_explanation.mean_attributions.feature_attributions.struct_value.fields.key = "key_value"
    model_evaluation_slices.model_explanation.mean_attributions.feature_attributions.struct_value.fields.value = "struct_pb2.Value(null_value=struct_pb2.NullValue.NULL_VALUE)"
    model_evaluation_slices.model_explanation.mean_attributions.feature_attributions.list_value.values = "[struct_pb2.Value(null_value=struct_pb2.NullValue.NULL_VALUE)]"
    model_evaluation_slices.model_explanation.mean_attributions.output_index = [1321, 1322]
    model_evaluation_slices.model_explanation.mean_attributions.output_display_name = "output_display_name_value"
    model_evaluation_slices.model_explanation.mean_attributions.approximation_error = 0.2068
    model_evaluation_slices.model_explanation.mean_attributions.output_name = "output_name_value"

    request = aiplatform_v1.BatchImportModelEvaluationSlicesRequest(
        parent="parent_value",
        model_evaluation_slices=model_evaluation_slices,
    )

    # Make the request
    response = client.batch_import_model_evaluation_slices(request=request)

    # Handle the response
    print(response)

# [END aiplatform_v1_generated_ModelService_BatchImportModelEvaluationSlices_sync]

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
# Snippet for BatchImportEvaluatedAnnotations
# NOTE: This snippet has been automatically generated for illustrative purposes only.
# It may require modifications to work in your environment.

# To install the latest published package dependency, execute the following:
#   python3 -m pip install google-cloud-aiplatform


# [START aiplatform_v1_generated_ModelService_BatchImportEvaluatedAnnotations_sync]
# This snippet has been automatically generated and should be regarded as a
# code template only.
# It will require modifications to work:
# - It may require correct/in-range values for request initialization.
# - It may require specifying regional endpoints when creating the service
#   client as shown in:
#   https://googleapis.dev/python/google-api-core/latest/client_options.html
from google.cloud import aiplatform_v1


def sample_batch_import_evaluated_annotations():
    # Create a client
    client = aiplatform_v1.ModelServiceClient()

    # Initialize request argument(s)
    evaluated_annotations = aiplatform_v1.EvaluatedAnnotation()
    evaluated_annotations.type_ = "FALSE_NEGATIVE"
    evaluated_annotations.predictions.null_value = "NULL_VALUE"
    evaluated_annotations.predictions.number_value = 0.1285
    evaluated_annotations.predictions.string_value = "string_value_value"
    evaluated_annotations.predictions.bool_value = True
    evaluated_annotations.predictions.struct_value.fields.key = "key_value"
    evaluated_annotations.predictions.struct_value.fields.value = "struct_pb2.Value(null_value=struct_pb2.NullValue.NULL_VALUE)"
    evaluated_annotations.predictions.list_value.values = "[struct_pb2.Value(null_value=struct_pb2.NullValue.NULL_VALUE)]"
    evaluated_annotations.ground_truths.null_value = "NULL_VALUE"
    evaluated_annotations.ground_truths.number_value = 0.1285
    evaluated_annotations.ground_truths.string_value = "string_value_value"
    evaluated_annotations.ground_truths.bool_value = True
    evaluated_annotations.ground_truths.struct_value.fields.key = "key_value"
    evaluated_annotations.ground_truths.struct_value.fields.value = "struct_pb2.Value(null_value=struct_pb2.NullValue.NULL_VALUE)"
    evaluated_annotations.ground_truths.list_value.values = "[struct_pb2.Value(null_value=struct_pb2.NullValue.NULL_VALUE)]"
    evaluated_annotations.data_item_payload.null_value = "NULL_VALUE"
    evaluated_annotations.data_item_payload.number_value = 0.1285
    evaluated_annotations.data_item_payload.string_value = "string_value_value"
    evaluated_annotations.data_item_payload.bool_value = True
    evaluated_annotations.data_item_payload.struct_value.fields.key = "key_value"
    evaluated_annotations.data_item_payload.struct_value.fields.value = "struct_pb2.Value(null_value=struct_pb2.NullValue.NULL_VALUE)"
    evaluated_annotations.data_item_payload.list_value.values = "[struct_pb2.Value(null_value=struct_pb2.NullValue.NULL_VALUE)]"
    evaluated_annotations.evaluated_data_item_view_id = "evaluated_data_item_view_id_value"
    evaluated_annotations.explanations.explanation_type = "explanation_type_value"
    evaluated_annotations.explanations.explanation.attributions.baseline_output_value = 0.2255
    evaluated_annotations.explanations.explanation.attributions.instance_output_value = 0.2273
    evaluated_annotations.explanations.explanation.attributions.feature_attributions.null_value = "NULL_VALUE"
    evaluated_annotations.explanations.explanation.attributions.feature_attributions.number_value = 0.1285
    evaluated_annotations.explanations.explanation.attributions.feature_attributions.string_value = "string_value_value"
    evaluated_annotations.explanations.explanation.attributions.feature_attributions.bool_value = True
    evaluated_annotations.explanations.explanation.attributions.feature_attributions.struct_value.fields.key = "key_value"
    evaluated_annotations.explanations.explanation.attributions.feature_attributions.struct_value.fields.value = "struct_pb2.Value(null_value=struct_pb2.NullValue.NULL_VALUE)"
    evaluated_annotations.explanations.explanation.attributions.feature_attributions.list_value.values = "[struct_pb2.Value(null_value=struct_pb2.NullValue.NULL_VALUE)]"
    evaluated_annotations.explanations.explanation.attributions.output_index = [1321, 1322]
    evaluated_annotations.explanations.explanation.attributions.output_display_name = "output_display_name_value"
    evaluated_annotations.explanations.explanation.attributions.approximation_error = 0.2068
    evaluated_annotations.explanations.explanation.attributions.output_name = "output_name_value"
    evaluated_annotations.explanations.explanation.neighbors.neighbor_id = "neighbor_id_value"
    evaluated_annotations.explanations.explanation.neighbors.neighbor_distance = 0.1784
    evaluated_annotations.error_analysis_annotations.attributed_items.annotation_resource_name = "annotation_resource_name_value"
    evaluated_annotations.error_analysis_annotations.attributed_items.distance = 0.843
    evaluated_annotations.error_analysis_annotations.query_type = "SAME_CLASS_DISSIMILAR"
    evaluated_annotations.error_analysis_annotations.outlier_score = 0.14070000000000002
    evaluated_annotations.error_analysis_annotations.outlier_threshold = 0.184

    request = aiplatform_v1.BatchImportEvaluatedAnnotationsRequest(
        parent="parent_value",
        evaluated_annotations=evaluated_annotations,
    )

    # Make the request
    response = client.batch_import_evaluated_annotations(request=request)

    # Handle the response
    print(response)

# [END aiplatform_v1_generated_ModelService_BatchImportEvaluatedAnnotations_sync]

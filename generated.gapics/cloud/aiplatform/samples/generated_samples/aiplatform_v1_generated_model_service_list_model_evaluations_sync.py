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
# Snippet for ListModelEvaluations
# NOTE: This snippet has been automatically generated for illustrative purposes only.
# It may require modifications to work in your environment.

# To install the latest published package dependency, execute the following:
#   python3 -m pip install google-cloud-aiplatform


# [START aiplatform_v1_generated_ModelService_ListModelEvaluations_sync]
# This snippet has been automatically generated and should be regarded as a
# code template only.
# It will require modifications to work:
# - It may require correct/in-range values for request initialization.
# - It may require specifying regional endpoints when creating the service
#   client as shown in:
#   https://googleapis.dev/python/google-api-core/latest/client_options.html
from google.cloud import aiplatform_v1


def sample_list_model_evaluations():
    # Create a client
    client = aiplatform_v1.ModelServiceClient()

    # Initialize request argument(s)
    read_mask = aiplatform_v1.FieldMask()
    read_mask.paths = ['paths_value1', 'paths_value2']

    request = aiplatform_v1.ListModelEvaluationsRequest(
        parent="parent_value",
        filter="filter_value",
        page_size=951,
        page_token="page_token_value",
        read_mask=read_mask,
    )

    # Make the request
    page_result = client.list_model_evaluations(request=request)

    # Handle the response
    for response in page_result:
        print(response)

# [END aiplatform_v1_generated_ModelService_ListModelEvaluations_sync]

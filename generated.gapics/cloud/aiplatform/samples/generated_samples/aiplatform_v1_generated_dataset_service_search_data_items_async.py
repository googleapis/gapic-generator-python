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
# Snippet for SearchDataItems
# NOTE: This snippet has been automatically generated for illustrative purposes only.
# It may require modifications to work in your environment.

# To install the latest published package dependency, execute the following:
#   python3 -m pip install google-cloud-aiplatform


# [START aiplatform_v1_generated_DatasetService_SearchDataItems_async]
# This snippet has been automatically generated and should be regarded as a
# code template only.
# It will require modifications to work:
# - It may require correct/in-range values for request initialization.
# - It may require specifying regional endpoints when creating the service
#   client as shown in:
#   https://googleapis.dev/python/google-api-core/latest/client_options.html
from google.cloud import aiplatform_v1


async def sample_search_data_items():
    # Create a client
    client = aiplatform_v1.DatasetServiceAsyncClient()

    # Initialize request argument(s)
    order_by_annotation = aiplatform_v1.OrderByAnnotation()
    order_by_annotation.saved_query = "saved_query_value"
    order_by_annotation.order_by = "order_by_value"

    field_mask = aiplatform_v1.FieldMask()
    field_mask.paths = ['paths_value1', 'paths_value2']

    request = aiplatform_v1.SearchDataItemsRequest(
        order_by_data_item="order_by_data_item_value",
        order_by_annotation=order_by_annotation,
        dataset="dataset_value",
        saved_query="saved_query_value",
        data_labeling_job="data_labeling_job_value",
        data_item_filter="data_item_filter_value",
        annotations_filter="annotations_filter_value",
        annotation_filters=['annotation_filters_value1', 'annotation_filters_value2'],
        field_mask=field_mask,
        annotations_limit=1836,
        page_size=951,
        order_by="order_by_value",
        page_token="page_token_value",
    )

    # Make the request
    page_result = client.search_data_items(request=request)

    # Handle the response
    async for response in page_result:
        print(response)

# [END aiplatform_v1_generated_DatasetService_SearchDataItems_async]

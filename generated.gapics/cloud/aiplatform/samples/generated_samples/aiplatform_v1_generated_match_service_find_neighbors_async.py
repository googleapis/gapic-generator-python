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
# Snippet for FindNeighbors
# NOTE: This snippet has been automatically generated for illustrative purposes only.
# It may require modifications to work in your environment.

# To install the latest published package dependency, execute the following:
#   python3 -m pip install google-cloud-aiplatform


# [START aiplatform_v1_generated_MatchService_FindNeighbors_async]
# This snippet has been automatically generated and should be regarded as a
# code template only.
# It will require modifications to work:
# - It may require correct/in-range values for request initialization.
# - It may require specifying regional endpoints when creating the service
#   client as shown in:
#   https://googleapis.dev/python/google-api-core/latest/client_options.html
from google.cloud import aiplatform_v1


async def sample_find_neighbors():
    # Create a client
    client = aiplatform_v1.MatchServiceAsyncClient()

    # Initialize request argument(s)
    queries = aiplatform_v1.Query()
    queries.datapoint.datapoint_id = "datapoint_id_value"
    queries.datapoint.feature_vector = [0.15030000000000002, 0.1504]
    queries.datapoint.restricts.namespace = "namespace_value"
    queries.datapoint.restricts.allow_list = ['allow_list_value1', 'allow_list_value2']
    queries.datapoint.restricts.deny_list = ['deny_list_value1', 'deny_list_value2']
    queries.datapoint.numeric_restricts.value_int = 967
    queries.datapoint.numeric_restricts.value_float = 0.117
    queries.datapoint.numeric_restricts.value_double = 0.12710000000000002
    queries.datapoint.numeric_restricts.namespace = "namespace_value"
    queries.datapoint.numeric_restricts.op = "NOT_EQUAL"
    queries.datapoint.crowding_tag.crowding_attribute = "crowding_attribute_value"
    queries.neighbor_count = 1494
    queries.per_crowding_attribute_neighbor_count = 3947
    queries.approximate_neighbor_count = 2783
    queries.fraction_leaf_nodes_to_search_override = 0.3995

    request = aiplatform_v1.FindNeighborsRequest(
        index_endpoint="index_endpoint_value",
        deployed_index_id="deployed_index_id_value",
        queries=queries,
        return_full_datapoint=True,
    )

    # Make the request
    response = await client.find_neighbors(request=request)

    # Handle the response
    print(response)

# [END aiplatform_v1_generated_MatchService_FindNeighbors_async]

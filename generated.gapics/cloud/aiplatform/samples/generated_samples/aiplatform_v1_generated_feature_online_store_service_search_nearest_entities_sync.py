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
# Snippet for SearchNearestEntities
# NOTE: This snippet has been automatically generated for illustrative purposes only.
# It may require modifications to work in your environment.

# To install the latest published package dependency, execute the following:
#   python3 -m pip install google-cloud-aiplatform


# [START aiplatform_v1_generated_FeatureOnlineStoreService_SearchNearestEntities_sync]
# This snippet has been automatically generated and should be regarded as a
# code template only.
# It will require modifications to work:
# - It may require correct/in-range values for request initialization.
# - It may require specifying regional endpoints when creating the service
#   client as shown in:
#   https://googleapis.dev/python/google-api-core/latest/client_options.html
from google.cloud import aiplatform_v1


def sample_search_nearest_entities():
    # Create a client
    client = aiplatform_v1.FeatureOnlineStoreServiceClient()

    # Initialize request argument(s)
    query = aiplatform_v1.NearestNeighborQuery()
    query.entity_id = "entity_id_value"
    query.embedding.value = [0.542, 0.543]
    query.neighbor_count = 1494
    query.string_filters.name = "name_value"
    query.string_filters.allow_tokens = ['allow_tokens_value1', 'allow_tokens_value2']
    query.string_filters.deny_tokens = ['deny_tokens_value1', 'deny_tokens_value2']
    query.per_crowding_attribute_neighbor_count = 3947
    query.parameters.approximate_neighbor_candidates = 3270
    query.parameters.leaf_nodes_search_fraction = 0.27140000000000003

    request = aiplatform_v1.SearchNearestEntitiesRequest(
        feature_view="feature_view_value",
        query=query,
        return_full_entity=True,
    )

    # Make the request
    response = client.search_nearest_entities(request=request)

    # Handle the response
    print(response)

# [END aiplatform_v1_generated_FeatureOnlineStoreService_SearchNearestEntities_sync]

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
# Snippet for UpdateFeatureView
# NOTE: This snippet has been automatically generated for illustrative purposes only.
# It may require modifications to work in your environment.

# To install the latest published package dependency, execute the following:
#   python3 -m pip install google-cloud-aiplatform


# [START aiplatform_v1_generated_FeatureOnlineStoreAdminService_UpdateFeatureView_async]
# This snippet has been automatically generated and should be regarded as a
# code template only.
# It will require modifications to work:
# - It may require correct/in-range values for request initialization.
# - It may require specifying regional endpoints when creating the service
#   client as shown in:
#   https://googleapis.dev/python/google-api-core/latest/client_options.html
from google.cloud import aiplatform_v1


async def sample_update_feature_view():
    # Create a client
    client = aiplatform_v1.FeatureOnlineStoreAdminServiceAsyncClient()

    # Initialize request argument(s)
    feature_view = aiplatform_v1.FeatureView()
    feature_view.big_query_source.uri = "uri_value"
    feature_view.big_query_source.entity_id_columns = ['entity_id_columns_value1', 'entity_id_columns_value2']
    feature_view.feature_registry_source.feature_groups.feature_group_id = "feature_group_id_value"
    feature_view.feature_registry_source.feature_groups.feature_ids = ['feature_ids_value1', 'feature_ids_value2']
    feature_view.feature_registry_source.project_number = 1503
    feature_view.name = "name_value"
    feature_view.create_time.seconds = 751
    feature_view.create_time.nanos = 543
    feature_view.update_time.seconds = 751
    feature_view.update_time.nanos = 543
    feature_view.etag = "etag_value"
    feature_view.labels.key = "key_value"
    feature_view.labels.value = "value_value"
    feature_view.sync_config.cron = "cron_value"
    feature_view.index_config.tree_ah_config.leaf_node_embedding_count = 2595
    feature_view.index_config.embedding_column = "embedding_column_value"
    feature_view.index_config.filter_columns = ['filter_columns_value1', 'filter_columns_value2']
    feature_view.index_config.crowding_column = "crowding_column_value"
    feature_view.index_config.embedding_dimension = 1988
    feature_view.index_config.distance_measure_type = "DOT_PRODUCT_DISTANCE"

    update_mask = aiplatform_v1.FieldMask()
    update_mask.paths = ['paths_value1', 'paths_value2']

    request = aiplatform_v1.UpdateFeatureViewRequest(
        feature_view=feature_view,
        update_mask=update_mask,
    )

    # Make the request
    operation = client.update_feature_view(request=request)

    print("Waiting for operation to complete...")

    response = (await operation).result()

    # Handle the response
    print(response)

# [END aiplatform_v1_generated_FeatureOnlineStoreAdminService_UpdateFeatureView_async]

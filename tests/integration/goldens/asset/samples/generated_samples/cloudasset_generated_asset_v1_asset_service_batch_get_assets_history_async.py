# -*- coding: utf-8 -*-
# Copyright 2020 Google LLC
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
# Snippet for BatchGetAssetsHistory
# NOTE: This snippet has been automatically generated for illustrative purposes only.
# It may require modifications to work in your environment.

# To install the latest published package dependency, execute the following:
#   python3 -m pip install google-cloud-asset


# [START cloudasset_generated_asset_v1_AssetService_BatchGetAssetsHistory_async]
from google.cloud import asset_v1


async def sample_batch_get_assets_history():
    """Snippet for batch_get_assets_history"""

    # Create a client
    client = asset_v1.AssetServiceAsyncClient()

    # Initialize request argument(s)
    request = asset_v1.BatchGetAssetsHistoryRequest(
    )

    # Make the request
    response = await client.batch_get_assets_history(request=request)

    # Handle response
    print(response)

# [END cloudasset_generated_asset_v1_AssetService_BatchGetAssetsHistory_async]

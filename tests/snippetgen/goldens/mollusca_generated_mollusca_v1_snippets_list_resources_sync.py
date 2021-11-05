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
# Snippet for ListResources
# NOTE: This snippet has been automatically generated for illustrative purposes only.
# It may require modifications to work in your environment.

# To install the latest published package dependency, execute the following:
#   python3 -m pip install animalia-mollusca


# [START mollusca_generated_mollusca_v1_Snippets_ListResources_sync]
from animalia import mollusca_v1


def sample_list_resources():
    """Snippet for list_resources"""

    # Create a client
    client = mollusca_v1.SnippetsClient()

    # Initialize request argument(s)
    item_id = "item_id_value"
    part_id = "part_id_value"
    parent = f"items/{item_id}/parts/{part_id}"

    request = mollusca_v1.ListResourcesRequest(
        parent=parent,
    )

    # Make the request
    page_result = client.list_resources(request=request)
    for response in page_result:
        print(response)

# [END mollusca_generated_mollusca_v1_Snippets_ListResources_sync]

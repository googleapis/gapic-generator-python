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
# Snippet for ExportData
# NOTE: This snippet has been automatically generated for illustrative purposes only.
# It may require modifications to work in your environment.

# To install the latest published package dependency, execute the following:
#   python3 -m pip install google-cloud-aiplatform


# [START aiplatform_v1_generated_DatasetService_ExportData_async]
# This snippet has been automatically generated and should be regarded as a
# code template only.
# It will require modifications to work:
# - It may require correct/in-range values for request initialization.
# - It may require specifying regional endpoints when creating the service
#   client as shown in:
#   https://googleapis.dev/python/google-api-core/latest/client_options.html
from google.cloud import aiplatform_v1


async def sample_export_data():
    # Create a client
    client = aiplatform_v1.DatasetServiceAsyncClient()

    # Initialize request argument(s)
    export_config = aiplatform_v1.ExportDataConfig()
    export_config.gcs_destination.output_uri_prefix = "output_uri_prefix_value"
    export_config.fraction_split.training_fraction = 0.1809
    export_config.fraction_split.validation_fraction = 0.2016
    export_config.fraction_split.test_fraction = 0.13970000000000002
    export_config.filter_split.training_filter = "training_filter_value"
    export_config.filter_split.validation_filter = "validation_filter_value"
    export_config.filter_split.test_filter = "test_filter_value"
    export_config.annotations_filter = "annotations_filter_value"
    export_config.saved_query_id = "saved_query_id_value"
    export_config.annotation_schema_uri = "annotation_schema_uri_value"
    export_config.export_use = "CUSTOM_CODE_TRAINING"

    request = aiplatform_v1.ExportDataRequest(
        name="name_value",
        export_config=export_config,
    )

    # Make the request
    operation = client.export_data(request=request)

    print("Waiting for operation to complete...")

    response = (await operation).result()

    # Handle the response
    print(response)

# [END aiplatform_v1_generated_DatasetService_ExportData_async]

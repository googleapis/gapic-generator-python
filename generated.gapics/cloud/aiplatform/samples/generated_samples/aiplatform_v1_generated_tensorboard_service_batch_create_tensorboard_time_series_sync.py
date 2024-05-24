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
# Snippet for BatchCreateTensorboardTimeSeries
# NOTE: This snippet has been automatically generated for illustrative purposes only.
# It may require modifications to work in your environment.

# To install the latest published package dependency, execute the following:
#   python3 -m pip install google-cloud-aiplatform


# [START aiplatform_v1_generated_TensorboardService_BatchCreateTensorboardTimeSeries_sync]
# This snippet has been automatically generated and should be regarded as a
# code template only.
# It will require modifications to work:
# - It may require correct/in-range values for request initialization.
# - It may require specifying regional endpoints when creating the service
#   client as shown in:
#   https://googleapis.dev/python/google-api-core/latest/client_options.html
from google.cloud import aiplatform_v1


def sample_batch_create_tensorboard_time_series():
    # Create a client
    client = aiplatform_v1.TensorboardServiceClient()

    # Initialize request argument(s)
    requests = aiplatform_v1.CreateTensorboardTimeSeriesRequest()
    requests.parent = "parent_value"
    requests.tensorboard_time_series_id = "tensorboard_time_series_id_value"
    requests.tensorboard_time_series.name = "name_value"
    requests.tensorboard_time_series.display_name = "display_name_value"
    requests.tensorboard_time_series.description = "description_value"
    requests.tensorboard_time_series.value_type = "BLOB_SEQUENCE"
    requests.tensorboard_time_series.create_time.seconds = 751
    requests.tensorboard_time_series.create_time.nanos = 543
    requests.tensorboard_time_series.update_time.seconds = 751
    requests.tensorboard_time_series.update_time.nanos = 543
    requests.tensorboard_time_series.etag = "etag_value"
    requests.tensorboard_time_series.plugin_name = "plugin_name_value"
    requests.tensorboard_time_series.plugin_data = b'plugin_data_blob'
    requests.tensorboard_time_series.metadata.max_step = 865
    requests.tensorboard_time_series.metadata.max_wall_time.seconds = 751
    requests.tensorboard_time_series.metadata.max_wall_time.nanos = 543
    requests.tensorboard_time_series.metadata.max_blob_sequence_length = 2525

    request = aiplatform_v1.BatchCreateTensorboardTimeSeriesRequest(
        parent="parent_value",
        requests=requests,
    )

    # Make the request
    response = client.batch_create_tensorboard_time_series(request=request)

    # Handle the response
    print(response)

# [END aiplatform_v1_generated_TensorboardService_BatchCreateTensorboardTimeSeries_sync]

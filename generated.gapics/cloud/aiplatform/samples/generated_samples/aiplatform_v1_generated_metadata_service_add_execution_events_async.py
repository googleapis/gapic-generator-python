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
# Snippet for AddExecutionEvents
# NOTE: This snippet has been automatically generated for illustrative purposes only.
# It may require modifications to work in your environment.

# To install the latest published package dependency, execute the following:
#   python3 -m pip install google-cloud-aiplatform


# [START aiplatform_v1_generated_MetadataService_AddExecutionEvents_async]
# This snippet has been automatically generated and should be regarded as a
# code template only.
# It will require modifications to work:
# - It may require correct/in-range values for request initialization.
# - It may require specifying regional endpoints when creating the service
#   client as shown in:
#   https://googleapis.dev/python/google-api-core/latest/client_options.html
from google.cloud import aiplatform_v1


async def sample_add_execution_events():
    # Create a client
    client = aiplatform_v1.MetadataServiceAsyncClient()

    # Initialize request argument(s)
    events = aiplatform_v1.Event()
    events.artifact = "artifact_value"
    events.execution = "execution_value"
    events.event_time.seconds = 751
    events.event_time.nanos = 543
    events.type_ = "OUTPUT"
    events.labels.key = "key_value"
    events.labels.value = "value_value"

    request = aiplatform_v1.AddExecutionEventsRequest(
        execution="execution_value",
        events=events,
    )

    # Make the request
    response = await client.add_execution_events(request=request)

    # Handle the response
    print(response)

# [END aiplatform_v1_generated_MetadataService_AddExecutionEvents_async]

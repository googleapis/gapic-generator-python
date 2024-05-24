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
# Snippet for CompleteTrial
# NOTE: This snippet has been automatically generated for illustrative purposes only.
# It may require modifications to work in your environment.

# To install the latest published package dependency, execute the following:
#   python3 -m pip install google-cloud-aiplatform


# [START aiplatform_v1_generated_VizierService_CompleteTrial_sync]
# This snippet has been automatically generated and should be regarded as a
# code template only.
# It will require modifications to work:
# - It may require correct/in-range values for request initialization.
# - It may require specifying regional endpoints when creating the service
#   client as shown in:
#   https://googleapis.dev/python/google-api-core/latest/client_options.html
from google.cloud import aiplatform_v1


def sample_complete_trial():
    # Create a client
    client = aiplatform_v1.VizierServiceClient()

    # Initialize request argument(s)
    final_measurement = aiplatform_v1.Measurement()
    final_measurement.elapsed_duration.seconds = 751
    final_measurement.elapsed_duration.nanos = 543
    final_measurement.step_count = 1092
    final_measurement.metrics.metric_id = "metric_id_value"
    final_measurement.metrics.value = 0.541

    request = aiplatform_v1.CompleteTrialRequest(
        name="name_value",
        final_measurement=final_measurement,
        trial_infeasible=True,
        infeasible_reason="infeasible_reason_value",
    )

    # Make the request
    response = client.complete_trial(request=request)

    # Handle the response
    print(response)

# [END aiplatform_v1_generated_VizierService_CompleteTrial_sync]

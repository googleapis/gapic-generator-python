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
# Snippet for CreateTrial
# NOTE: This snippet has been automatically generated for illustrative purposes only.
# It may require modifications to work in your environment.

# To install the latest published package dependency, execute the following:
#   python3 -m pip install google-cloud-aiplatform


# [START aiplatform_v1_generated_VizierService_CreateTrial_sync]
# This snippet has been automatically generated and should be regarded as a
# code template only.
# It will require modifications to work:
# - It may require correct/in-range values for request initialization.
# - It may require specifying regional endpoints when creating the service
#   client as shown in:
#   https://googleapis.dev/python/google-api-core/latest/client_options.html
from google.cloud import aiplatform_v1


def sample_create_trial():
    # Create a client
    client = aiplatform_v1.VizierServiceClient()

    # Initialize request argument(s)
    trial = aiplatform_v1.Trial()
    trial.name = "name_value"
    trial.id = "id_value"
    trial.state = "INFEASIBLE"
    trial.parameters.parameter_id = "parameter_id_value"
    trial.parameters.value.null_value = "NULL_VALUE"
    trial.parameters.value.number_value = 0.1285
    trial.parameters.value.string_value = "string_value_value"
    trial.parameters.value.bool_value = True
    trial.parameters.value.struct_value.fields.key = "key_value"
    trial.parameters.value.struct_value.fields.value = "struct_pb2.Value(null_value=struct_pb2.NullValue.NULL_VALUE)"
    trial.parameters.value.list_value.values = "[struct_pb2.Value(null_value=struct_pb2.NullValue.NULL_VALUE)]"
    trial.final_measurement.elapsed_duration.seconds = 751
    trial.final_measurement.elapsed_duration.nanos = 543
    trial.final_measurement.step_count = 1092
    trial.final_measurement.metrics.metric_id = "metric_id_value"
    trial.final_measurement.metrics.value = 0.541
    trial.measurements.elapsed_duration.seconds = 751
    trial.measurements.elapsed_duration.nanos = 543
    trial.measurements.step_count = 1092
    trial.measurements.metrics.metric_id = "metric_id_value"
    trial.measurements.metrics.value = 0.541
    trial.start_time.seconds = 751
    trial.start_time.nanos = 543
    trial.end_time.seconds = 751
    trial.end_time.nanos = 543
    trial.client_id = "client_id_value"
    trial.infeasible_reason = "infeasible_reason_value"
    trial.custom_job = "custom_job_value"
    trial.web_access_uris.key = "key_value"
    trial.web_access_uris.value = "value_value"

    request = aiplatform_v1.CreateTrialRequest(
        parent="parent_value",
        trial=trial,
    )

    # Make the request
    response = client.create_trial(request=request)

    # Handle the response
    print(response)

# [END aiplatform_v1_generated_VizierService_CreateTrial_sync]

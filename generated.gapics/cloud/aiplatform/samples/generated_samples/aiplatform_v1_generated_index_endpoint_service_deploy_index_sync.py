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
# Snippet for DeployIndex
# NOTE: This snippet has been automatically generated for illustrative purposes only.
# It may require modifications to work in your environment.

# To install the latest published package dependency, execute the following:
#   python3 -m pip install google-cloud-aiplatform


# [START aiplatform_v1_generated_IndexEndpointService_DeployIndex_sync]
# This snippet has been automatically generated and should be regarded as a
# code template only.
# It will require modifications to work:
# - It may require correct/in-range values for request initialization.
# - It may require specifying regional endpoints when creating the service
#   client as shown in:
#   https://googleapis.dev/python/google-api-core/latest/client_options.html
from google.cloud import aiplatform_v1


def sample_deploy_index():
    # Create a client
    client = aiplatform_v1.IndexEndpointServiceClient()

    # Initialize request argument(s)
    deployed_index = aiplatform_v1.DeployedIndex()
    deployed_index.id = "id_value"
    deployed_index.index = "index_value"
    deployed_index.display_name = "display_name_value"
    deployed_index.create_time.seconds = 751
    deployed_index.create_time.nanos = 543
    deployed_index.private_endpoints.match_grpc_address = "match_grpc_address_value"
    deployed_index.private_endpoints.service_attachment = "service_attachment_value"
    deployed_index.private_endpoints.psc_automated_endpoints.project_id = "project_id_value"
    deployed_index.private_endpoints.psc_automated_endpoints.network = "network_value"
    deployed_index.private_endpoints.psc_automated_endpoints.match_address = "match_address_value"
    deployed_index.index_sync_time.seconds = 751
    deployed_index.index_sync_time.nanos = 543
    deployed_index.automatic_resources.min_replica_count = 1803
    deployed_index.automatic_resources.max_replica_count = 1805
    deployed_index.dedicated_resources.machine_spec.machine_type = "machine_type_value"
    deployed_index.dedicated_resources.machine_spec.accelerator_type = "TPU_V5_LITEPOD"
    deployed_index.dedicated_resources.machine_spec.accelerator_count = 1805
    deployed_index.dedicated_resources.machine_spec.tpu_topology = "tpu_topology_value"
    deployed_index.dedicated_resources.min_replica_count = 1803
    deployed_index.dedicated_resources.max_replica_count = 1805
    deployed_index.dedicated_resources.autoscaling_metric_specs.metric_name = "metric_name_value"
    deployed_index.dedicated_resources.autoscaling_metric_specs.target = 647
    deployed_index.enable_access_logging = True
    deployed_index.deployed_index_auth_config.auth_provider.audiences = ['audiences_value1', 'audiences_value2']
    deployed_index.deployed_index_auth_config.auth_provider.allowed_issuers = ['allowed_issuers_value1', 'allowed_issuers_value2']
    deployed_index.reserved_ip_ranges = ['reserved_ip_ranges_value1', 'reserved_ip_ranges_value2']
    deployed_index.deployment_group = "deployment_group_value"

    request = aiplatform_v1.DeployIndexRequest(
        index_endpoint="index_endpoint_value",
        deployed_index=deployed_index,
    )

    # Make the request
    operation = client.deploy_index(request=request)

    print("Waiting for operation to complete...")

    response = operation.result()

    # Handle the response
    print(response)

# [END aiplatform_v1_generated_IndexEndpointService_DeployIndex_sync]

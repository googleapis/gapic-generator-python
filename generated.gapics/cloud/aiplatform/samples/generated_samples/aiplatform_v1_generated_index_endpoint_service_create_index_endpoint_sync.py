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
# Snippet for CreateIndexEndpoint
# NOTE: This snippet has been automatically generated for illustrative purposes only.
# It may require modifications to work in your environment.

# To install the latest published package dependency, execute the following:
#   python3 -m pip install google-cloud-aiplatform


# [START aiplatform_v1_generated_IndexEndpointService_CreateIndexEndpoint_sync]
# This snippet has been automatically generated and should be regarded as a
# code template only.
# It will require modifications to work:
# - It may require correct/in-range values for request initialization.
# - It may require specifying regional endpoints when creating the service
#   client as shown in:
#   https://googleapis.dev/python/google-api-core/latest/client_options.html
from google.cloud import aiplatform_v1


def sample_create_index_endpoint():
    # Create a client
    client = aiplatform_v1.IndexEndpointServiceClient()

    # Initialize request argument(s)
    index_endpoint = aiplatform_v1.IndexEndpoint()
    index_endpoint.name = "name_value"
    index_endpoint.display_name = "display_name_value"
    index_endpoint.description = "description_value"
    index_endpoint.deployed_indexes.id = "id_value"
    index_endpoint.deployed_indexes.index = "index_value"
    index_endpoint.deployed_indexes.display_name = "display_name_value"
    index_endpoint.deployed_indexes.create_time.seconds = 751
    index_endpoint.deployed_indexes.create_time.nanos = 543
    index_endpoint.deployed_indexes.private_endpoints.match_grpc_address = "match_grpc_address_value"
    index_endpoint.deployed_indexes.private_endpoints.service_attachment = "service_attachment_value"
    index_endpoint.deployed_indexes.private_endpoints.psc_automated_endpoints.project_id = "project_id_value"
    index_endpoint.deployed_indexes.private_endpoints.psc_automated_endpoints.network = "network_value"
    index_endpoint.deployed_indexes.private_endpoints.psc_automated_endpoints.match_address = "match_address_value"
    index_endpoint.deployed_indexes.index_sync_time.seconds = 751
    index_endpoint.deployed_indexes.index_sync_time.nanos = 543
    index_endpoint.deployed_indexes.automatic_resources.min_replica_count = 1803
    index_endpoint.deployed_indexes.automatic_resources.max_replica_count = 1805
    index_endpoint.deployed_indexes.dedicated_resources.machine_spec.machine_type = "machine_type_value"
    index_endpoint.deployed_indexes.dedicated_resources.machine_spec.accelerator_type = "TPU_V5_LITEPOD"
    index_endpoint.deployed_indexes.dedicated_resources.machine_spec.accelerator_count = 1805
    index_endpoint.deployed_indexes.dedicated_resources.machine_spec.tpu_topology = "tpu_topology_value"
    index_endpoint.deployed_indexes.dedicated_resources.min_replica_count = 1803
    index_endpoint.deployed_indexes.dedicated_resources.max_replica_count = 1805
    index_endpoint.deployed_indexes.dedicated_resources.autoscaling_metric_specs.metric_name = "metric_name_value"
    index_endpoint.deployed_indexes.dedicated_resources.autoscaling_metric_specs.target = 647
    index_endpoint.deployed_indexes.enable_access_logging = True
    index_endpoint.deployed_indexes.deployed_index_auth_config.auth_provider.audiences = ['audiences_value1', 'audiences_value2']
    index_endpoint.deployed_indexes.deployed_index_auth_config.auth_provider.allowed_issuers = ['allowed_issuers_value1', 'allowed_issuers_value2']
    index_endpoint.deployed_indexes.reserved_ip_ranges = ['reserved_ip_ranges_value1', 'reserved_ip_ranges_value2']
    index_endpoint.deployed_indexes.deployment_group = "deployment_group_value"
    index_endpoint.etag = "etag_value"
    index_endpoint.labels.key = "key_value"
    index_endpoint.labels.value = "value_value"
    index_endpoint.create_time.seconds = 751
    index_endpoint.create_time.nanos = 543
    index_endpoint.update_time.seconds = 751
    index_endpoint.update_time.nanos = 543
    index_endpoint.network = "network_value"
    index_endpoint.enable_private_service_connect = True
    index_endpoint.private_service_connect_config.enable_private_service_connect = True
    index_endpoint.private_service_connect_config.project_allowlist = ['project_allowlist_value1', 'project_allowlist_value2']
    index_endpoint.public_endpoint_enabled = True
    index_endpoint.public_endpoint_domain_name = "public_endpoint_domain_name_value"
    index_endpoint.encryption_spec.kms_key_name = "kms_key_name_value"

    request = aiplatform_v1.CreateIndexEndpointRequest(
        parent="parent_value",
        index_endpoint=index_endpoint,
    )

    # Make the request
    operation = client.create_index_endpoint(request=request)

    print("Waiting for operation to complete...")

    response = operation.result()

    # Handle the response
    print(response)

# [END aiplatform_v1_generated_IndexEndpointService_CreateIndexEndpoint_sync]

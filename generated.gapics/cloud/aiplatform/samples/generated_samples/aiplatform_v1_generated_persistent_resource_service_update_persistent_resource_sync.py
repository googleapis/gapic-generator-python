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
# Snippet for UpdatePersistentResource
# NOTE: This snippet has been automatically generated for illustrative purposes only.
# It may require modifications to work in your environment.

# To install the latest published package dependency, execute the following:
#   python3 -m pip install google-cloud-aiplatform


# [START aiplatform_v1_generated_PersistentResourceService_UpdatePersistentResource_sync]
# This snippet has been automatically generated and should be regarded as a
# code template only.
# It will require modifications to work:
# - It may require correct/in-range values for request initialization.
# - It may require specifying regional endpoints when creating the service
#   client as shown in:
#   https://googleapis.dev/python/google-api-core/latest/client_options.html
from google.cloud import aiplatform_v1


def sample_update_persistent_resource():
    # Create a client
    client = aiplatform_v1.PersistentResourceServiceClient()

    # Initialize request argument(s)
    persistent_resource = aiplatform_v1.PersistentResource()
    persistent_resource.name = "name_value"
    persistent_resource.display_name = "display_name_value"
    persistent_resource.resource_pools.id = "id_value"
    persistent_resource.resource_pools.machine_spec.machine_type = "machine_type_value"
    persistent_resource.resource_pools.machine_spec.accelerator_type = "TPU_V5_LITEPOD"
    persistent_resource.resource_pools.machine_spec.accelerator_count = 1805
    persistent_resource.resource_pools.machine_spec.tpu_topology = "tpu_topology_value"
    persistent_resource.resource_pools.replica_count = 1384
    persistent_resource.resource_pools.disk_spec.boot_disk_type = "boot_disk_type_value"
    persistent_resource.resource_pools.disk_spec.boot_disk_size_gb = 1792
    persistent_resource.resource_pools.used_replica_count = 1912
    persistent_resource.resource_pools.autoscaling_spec.min_replica_count = 1803
    persistent_resource.resource_pools.autoscaling_spec.max_replica_count = 1805
    persistent_resource.state = "UPDATING"
    persistent_resource.error.code = 411
    persistent_resource.error.message = "message_value"
    persistent_resource.error.details.type_url = "type.googleapis.com/google.protobuf.Empty"
    persistent_resource.error.details.value = b'value_blob'
    persistent_resource.create_time.seconds = 751
    persistent_resource.create_time.nanos = 543
    persistent_resource.start_time.seconds = 751
    persistent_resource.start_time.nanos = 543
    persistent_resource.update_time.seconds = 751
    persistent_resource.update_time.nanos = 543
    persistent_resource.labels.key = "key_value"
    persistent_resource.labels.value = "value_value"
    persistent_resource.network = "network_value"
    persistent_resource.encryption_spec.kms_key_name = "kms_key_name_value"
    persistent_resource.resource_runtime_spec.service_account_spec.enable_custom_service_account = True
    persistent_resource.resource_runtime_spec.service_account_spec.service_account = "service_account_value"
    persistent_resource.reserved_ip_ranges = ['reserved_ip_ranges_value1', 'reserved_ip_ranges_value2']

    update_mask = aiplatform_v1.FieldMask()
    update_mask.paths = ['paths_value1', 'paths_value2']

    request = aiplatform_v1.UpdatePersistentResourceRequest(
        persistent_resource=persistent_resource,
        update_mask=update_mask,
    )

    # Make the request
    operation = client.update_persistent_resource(request=request)

    print("Waiting for operation to complete...")

    response = operation.result()

    # Handle the response
    print(response)

# [END aiplatform_v1_generated_PersistentResourceService_UpdatePersistentResource_sync]

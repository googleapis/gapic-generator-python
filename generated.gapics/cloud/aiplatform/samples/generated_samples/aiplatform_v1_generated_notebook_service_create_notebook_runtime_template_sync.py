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
# Snippet for CreateNotebookRuntimeTemplate
# NOTE: This snippet has been automatically generated for illustrative purposes only.
# It may require modifications to work in your environment.

# To install the latest published package dependency, execute the following:
#   python3 -m pip install google-cloud-aiplatform


# [START aiplatform_v1_generated_NotebookService_CreateNotebookRuntimeTemplate_sync]
# This snippet has been automatically generated and should be regarded as a
# code template only.
# It will require modifications to work:
# - It may require correct/in-range values for request initialization.
# - It may require specifying regional endpoints when creating the service
#   client as shown in:
#   https://googleapis.dev/python/google-api-core/latest/client_options.html
from google.cloud import aiplatform_v1


def sample_create_notebook_runtime_template():
    # Create a client
    client = aiplatform_v1.NotebookServiceClient()

    # Initialize request argument(s)
    notebook_runtime_template = aiplatform_v1.NotebookRuntimeTemplate()
    notebook_runtime_template.name = "name_value"
    notebook_runtime_template.display_name = "display_name_value"
    notebook_runtime_template.description = "description_value"
    notebook_runtime_template.is_default = True
    notebook_runtime_template.machine_spec.machine_type = "machine_type_value"
    notebook_runtime_template.machine_spec.accelerator_type = "TPU_V5_LITEPOD"
    notebook_runtime_template.machine_spec.accelerator_count = 1805
    notebook_runtime_template.machine_spec.tpu_topology = "tpu_topology_value"
    notebook_runtime_template.data_persistent_disk_spec.disk_type = "disk_type_value"
    notebook_runtime_template.data_persistent_disk_spec.disk_size_gb = 1261
    notebook_runtime_template.network_spec.enable_internet_access = True
    notebook_runtime_template.network_spec.network = "network_value"
    notebook_runtime_template.network_spec.subnetwork = "subnetwork_value"
    notebook_runtime_template.service_account = "service_account_value"
    notebook_runtime_template.etag = "etag_value"
    notebook_runtime_template.labels.key = "key_value"
    notebook_runtime_template.labels.value = "value_value"
    notebook_runtime_template.idle_shutdown_config.idle_timeout.seconds = 751
    notebook_runtime_template.idle_shutdown_config.idle_timeout.nanos = 543
    notebook_runtime_template.idle_shutdown_config.idle_shutdown_disabled = True
    notebook_runtime_template.euc_config.euc_disabled = True
    notebook_runtime_template.euc_config.bypass_actas_check = True
    notebook_runtime_template.create_time.seconds = 751
    notebook_runtime_template.create_time.nanos = 543
    notebook_runtime_template.update_time.seconds = 751
    notebook_runtime_template.update_time.nanos = 543
    notebook_runtime_template.notebook_runtime_type = "ONE_CLICK"
    notebook_runtime_template.shielded_vm_config.enable_secure_boot = True
    notebook_runtime_template.network_tags = ['network_tags_value1', 'network_tags_value2']

    request = aiplatform_v1.CreateNotebookRuntimeTemplateRequest(
        parent="parent_value",
        notebook_runtime_template=notebook_runtime_template,
        notebook_runtime_template_id="notebook_runtime_template_id_value",
    )

    # Make the request
    operation = client.create_notebook_runtime_template(request=request)

    print("Waiting for operation to complete...")

    response = operation.result()

    # Handle the response
    print(response)

# [END aiplatform_v1_generated_NotebookService_CreateNotebookRuntimeTemplate_sync]

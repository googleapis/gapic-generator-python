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
# Snippet for CreateCustomJob
# NOTE: This snippet has been automatically generated for illustrative purposes only.
# It may require modifications to work in your environment.

# To install the latest published package dependency, execute the following:
#   python3 -m pip install google-cloud-aiplatform


# [START aiplatform_v1_generated_JobService_CreateCustomJob_sync]
# This snippet has been automatically generated and should be regarded as a
# code template only.
# It will require modifications to work:
# - It may require correct/in-range values for request initialization.
# - It may require specifying regional endpoints when creating the service
#   client as shown in:
#   https://googleapis.dev/python/google-api-core/latest/client_options.html
from google.cloud import aiplatform_v1


def sample_create_custom_job():
    # Create a client
    client = aiplatform_v1.JobServiceClient()

    # Initialize request argument(s)
    custom_job = aiplatform_v1.CustomJob()
    custom_job.name = "name_value"
    custom_job.display_name = "display_name_value"
    custom_job.job_spec.persistent_resource_id = "persistent_resource_id_value"
    custom_job.job_spec.worker_pool_specs.container_spec.image_uri = "image_uri_value"
    custom_job.job_spec.worker_pool_specs.container_spec.command = ['command_value1', 'command_value2']
    custom_job.job_spec.worker_pool_specs.container_spec.args = ['args_value1', 'args_value2']
    custom_job.job_spec.worker_pool_specs.container_spec.env.name = "name_value"
    custom_job.job_spec.worker_pool_specs.container_spec.env.value = "value_value"
    custom_job.job_spec.worker_pool_specs.python_package_spec.executor_image_uri = "executor_image_uri_value"
    custom_job.job_spec.worker_pool_specs.python_package_spec.package_uris = ['package_uris_value1', 'package_uris_value2']
    custom_job.job_spec.worker_pool_specs.python_package_spec.python_module = "python_module_value"
    custom_job.job_spec.worker_pool_specs.python_package_spec.args = ['args_value1', 'args_value2']
    custom_job.job_spec.worker_pool_specs.python_package_spec.env.name = "name_value"
    custom_job.job_spec.worker_pool_specs.python_package_spec.env.value = "value_value"
    custom_job.job_spec.worker_pool_specs.machine_spec.machine_type = "machine_type_value"
    custom_job.job_spec.worker_pool_specs.machine_spec.accelerator_type = "TPU_V5_LITEPOD"
    custom_job.job_spec.worker_pool_specs.machine_spec.accelerator_count = 1805
    custom_job.job_spec.worker_pool_specs.machine_spec.tpu_topology = "tpu_topology_value"
    custom_job.job_spec.worker_pool_specs.replica_count = 1384
    custom_job.job_spec.worker_pool_specs.nfs_mounts.server = "server_value"
    custom_job.job_spec.worker_pool_specs.nfs_mounts.path = "path_value"
    custom_job.job_spec.worker_pool_specs.nfs_mounts.mount_point = "mount_point_value"
    custom_job.job_spec.worker_pool_specs.disk_spec.boot_disk_type = "boot_disk_type_value"
    custom_job.job_spec.worker_pool_specs.disk_spec.boot_disk_size_gb = 1792
    custom_job.job_spec.scheduling.timeout.seconds = 751
    custom_job.job_spec.scheduling.timeout.nanos = 543
    custom_job.job_spec.scheduling.restart_job_on_worker_restart = True
    custom_job.job_spec.scheduling.disable_retries = True
    custom_job.job_spec.service_account = "service_account_value"
    custom_job.job_spec.network = "network_value"
    custom_job.job_spec.reserved_ip_ranges = ['reserved_ip_ranges_value1', 'reserved_ip_ranges_value2']
    custom_job.job_spec.base_output_directory.output_uri_prefix = "output_uri_prefix_value"
    custom_job.job_spec.protected_artifact_location_id = "protected_artifact_location_id_value"
    custom_job.job_spec.tensorboard = "tensorboard_value"
    custom_job.job_spec.enable_web_access = True
    custom_job.job_spec.enable_dashboard_access = True
    custom_job.job_spec.experiment = "experiment_value"
    custom_job.job_spec.experiment_run = "experiment_run_value"
    custom_job.job_spec.models = ['models_value1', 'models_value2']
    custom_job.state = "JOB_STATE_PARTIALLY_SUCCEEDED"
    custom_job.create_time.seconds = 751
    custom_job.create_time.nanos = 543
    custom_job.start_time.seconds = 751
    custom_job.start_time.nanos = 543
    custom_job.end_time.seconds = 751
    custom_job.end_time.nanos = 543
    custom_job.update_time.seconds = 751
    custom_job.update_time.nanos = 543
    custom_job.error.code = 411
    custom_job.error.message = "message_value"
    custom_job.error.details.type_url = "type.googleapis.com/google.protobuf.Empty"
    custom_job.error.details.value = b'value_blob'
    custom_job.labels.key = "key_value"
    custom_job.labels.value = "value_value"
    custom_job.encryption_spec.kms_key_name = "kms_key_name_value"
    custom_job.web_access_uris.key = "key_value"
    custom_job.web_access_uris.value = "value_value"

    request = aiplatform_v1.CreateCustomJobRequest(
        parent="parent_value",
        custom_job=custom_job,
    )

    # Make the request
    response = client.create_custom_job(request=request)

    # Handle the response
    print(response)

# [END aiplatform_v1_generated_JobService_CreateCustomJob_sync]

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
# Snippet for CreateNasJob
# NOTE: This snippet has been automatically generated for illustrative purposes only.
# It may require modifications to work in your environment.

# To install the latest published package dependency, execute the following:
#   python3 -m pip install google-cloud-aiplatform


# [START aiplatform_v1_generated_JobService_CreateNasJob_async]
# This snippet has been automatically generated and should be regarded as a
# code template only.
# It will require modifications to work:
# - It may require correct/in-range values for request initialization.
# - It may require specifying regional endpoints when creating the service
#   client as shown in:
#   https://googleapis.dev/python/google-api-core/latest/client_options.html
from google.cloud import aiplatform_v1


async def sample_create_nas_job():
    # Create a client
    client = aiplatform_v1.JobServiceAsyncClient()

    # Initialize request argument(s)
    nas_job = aiplatform_v1.NasJob()
    nas_job.name = "name_value"
    nas_job.display_name = "display_name_value"
    nas_job.nas_job_spec.multi_trial_algorithm_spec.multi_trial_algorithm = "GRID_SEARCH"
    nas_job.nas_job_spec.multi_trial_algorithm_spec.metric.metric_id = "metric_id_value"
    nas_job.nas_job_spec.multi_trial_algorithm_spec.metric.goal = "MINIMIZE"
    nas_job.nas_job_spec.multi_trial_algorithm_spec.search_trial_spec.search_trial_job_spec.persistent_resource_id = "persistent_resource_id_value"
    nas_job.nas_job_spec.multi_trial_algorithm_spec.search_trial_spec.search_trial_job_spec.worker_pool_specs.container_spec.image_uri = "image_uri_value"
    nas_job.nas_job_spec.multi_trial_algorithm_spec.search_trial_spec.search_trial_job_spec.worker_pool_specs.container_spec.command = ['command_value1', 'command_value2']
    nas_job.nas_job_spec.multi_trial_algorithm_spec.search_trial_spec.search_trial_job_spec.worker_pool_specs.container_spec.args = ['args_value1', 'args_value2']
    nas_job.nas_job_spec.multi_trial_algorithm_spec.search_trial_spec.search_trial_job_spec.worker_pool_specs.container_spec.env.name = "name_value"
    nas_job.nas_job_spec.multi_trial_algorithm_spec.search_trial_spec.search_trial_job_spec.worker_pool_specs.container_spec.env.value = "value_value"
    nas_job.nas_job_spec.multi_trial_algorithm_spec.search_trial_spec.search_trial_job_spec.worker_pool_specs.python_package_spec.executor_image_uri = "executor_image_uri_value"
    nas_job.nas_job_spec.multi_trial_algorithm_spec.search_trial_spec.search_trial_job_spec.worker_pool_specs.python_package_spec.package_uris = ['package_uris_value1', 'package_uris_value2']
    nas_job.nas_job_spec.multi_trial_algorithm_spec.search_trial_spec.search_trial_job_spec.worker_pool_specs.python_package_spec.python_module = "python_module_value"
    nas_job.nas_job_spec.multi_trial_algorithm_spec.search_trial_spec.search_trial_job_spec.worker_pool_specs.python_package_spec.args = ['args_value1', 'args_value2']
    nas_job.nas_job_spec.multi_trial_algorithm_spec.search_trial_spec.search_trial_job_spec.worker_pool_specs.python_package_spec.env.name = "name_value"
    nas_job.nas_job_spec.multi_trial_algorithm_spec.search_trial_spec.search_trial_job_spec.worker_pool_specs.python_package_spec.env.value = "value_value"
    nas_job.nas_job_spec.multi_trial_algorithm_spec.search_trial_spec.search_trial_job_spec.worker_pool_specs.machine_spec.machine_type = "machine_type_value"
    nas_job.nas_job_spec.multi_trial_algorithm_spec.search_trial_spec.search_trial_job_spec.worker_pool_specs.machine_spec.accelerator_type = "TPU_V5_LITEPOD"
    nas_job.nas_job_spec.multi_trial_algorithm_spec.search_trial_spec.search_trial_job_spec.worker_pool_specs.machine_spec.accelerator_count = 1805
    nas_job.nas_job_spec.multi_trial_algorithm_spec.search_trial_spec.search_trial_job_spec.worker_pool_specs.machine_spec.tpu_topology = "tpu_topology_value"
    nas_job.nas_job_spec.multi_trial_algorithm_spec.search_trial_spec.search_trial_job_spec.worker_pool_specs.replica_count = 1384
    nas_job.nas_job_spec.multi_trial_algorithm_spec.search_trial_spec.search_trial_job_spec.worker_pool_specs.nfs_mounts.server = "server_value"
    nas_job.nas_job_spec.multi_trial_algorithm_spec.search_trial_spec.search_trial_job_spec.worker_pool_specs.nfs_mounts.path = "path_value"
    nas_job.nas_job_spec.multi_trial_algorithm_spec.search_trial_spec.search_trial_job_spec.worker_pool_specs.nfs_mounts.mount_point = "mount_point_value"
    nas_job.nas_job_spec.multi_trial_algorithm_spec.search_trial_spec.search_trial_job_spec.worker_pool_specs.disk_spec.boot_disk_type = "boot_disk_type_value"
    nas_job.nas_job_spec.multi_trial_algorithm_spec.search_trial_spec.search_trial_job_spec.worker_pool_specs.disk_spec.boot_disk_size_gb = 1792
    nas_job.nas_job_spec.multi_trial_algorithm_spec.search_trial_spec.search_trial_job_spec.scheduling.timeout.seconds = 751
    nas_job.nas_job_spec.multi_trial_algorithm_spec.search_trial_spec.search_trial_job_spec.scheduling.timeout.nanos = 543
    nas_job.nas_job_spec.multi_trial_algorithm_spec.search_trial_spec.search_trial_job_spec.scheduling.restart_job_on_worker_restart = True
    nas_job.nas_job_spec.multi_trial_algorithm_spec.search_trial_spec.search_trial_job_spec.scheduling.disable_retries = True
    nas_job.nas_job_spec.multi_trial_algorithm_spec.search_trial_spec.search_trial_job_spec.service_account = "service_account_value"
    nas_job.nas_job_spec.multi_trial_algorithm_spec.search_trial_spec.search_trial_job_spec.network = "network_value"
    nas_job.nas_job_spec.multi_trial_algorithm_spec.search_trial_spec.search_trial_job_spec.reserved_ip_ranges = ['reserved_ip_ranges_value1', 'reserved_ip_ranges_value2']
    nas_job.nas_job_spec.multi_trial_algorithm_spec.search_trial_spec.search_trial_job_spec.base_output_directory.output_uri_prefix = "output_uri_prefix_value"
    nas_job.nas_job_spec.multi_trial_algorithm_spec.search_trial_spec.search_trial_job_spec.protected_artifact_location_id = "protected_artifact_location_id_value"
    nas_job.nas_job_spec.multi_trial_algorithm_spec.search_trial_spec.search_trial_job_spec.tensorboard = "tensorboard_value"
    nas_job.nas_job_spec.multi_trial_algorithm_spec.search_trial_spec.search_trial_job_spec.enable_web_access = True
    nas_job.nas_job_spec.multi_trial_algorithm_spec.search_trial_spec.search_trial_job_spec.enable_dashboard_access = True
    nas_job.nas_job_spec.multi_trial_algorithm_spec.search_trial_spec.search_trial_job_spec.experiment = "experiment_value"
    nas_job.nas_job_spec.multi_trial_algorithm_spec.search_trial_spec.search_trial_job_spec.experiment_run = "experiment_run_value"
    nas_job.nas_job_spec.multi_trial_algorithm_spec.search_trial_spec.search_trial_job_spec.models = ['models_value1', 'models_value2']
    nas_job.nas_job_spec.multi_trial_algorithm_spec.search_trial_spec.max_trial_count = 1609
    nas_job.nas_job_spec.multi_trial_algorithm_spec.search_trial_spec.max_parallel_trial_count = 2549
    nas_job.nas_job_spec.multi_trial_algorithm_spec.search_trial_spec.max_failed_trial_count = 2317
    nas_job.nas_job_spec.multi_trial_algorithm_spec.train_trial_spec.train_trial_job_spec.persistent_resource_id = "persistent_resource_id_value"
    nas_job.nas_job_spec.multi_trial_algorithm_spec.train_trial_spec.train_trial_job_spec.worker_pool_specs.container_spec.image_uri = "image_uri_value"
    nas_job.nas_job_spec.multi_trial_algorithm_spec.train_trial_spec.train_trial_job_spec.worker_pool_specs.container_spec.command = ['command_value1', 'command_value2']
    nas_job.nas_job_spec.multi_trial_algorithm_spec.train_trial_spec.train_trial_job_spec.worker_pool_specs.container_spec.args = ['args_value1', 'args_value2']
    nas_job.nas_job_spec.multi_trial_algorithm_spec.train_trial_spec.train_trial_job_spec.worker_pool_specs.container_spec.env.name = "name_value"
    nas_job.nas_job_spec.multi_trial_algorithm_spec.train_trial_spec.train_trial_job_spec.worker_pool_specs.container_spec.env.value = "value_value"
    nas_job.nas_job_spec.multi_trial_algorithm_spec.train_trial_spec.train_trial_job_spec.worker_pool_specs.python_package_spec.executor_image_uri = "executor_image_uri_value"
    nas_job.nas_job_spec.multi_trial_algorithm_spec.train_trial_spec.train_trial_job_spec.worker_pool_specs.python_package_spec.package_uris = ['package_uris_value1', 'package_uris_value2']
    nas_job.nas_job_spec.multi_trial_algorithm_spec.train_trial_spec.train_trial_job_spec.worker_pool_specs.python_package_spec.python_module = "python_module_value"
    nas_job.nas_job_spec.multi_trial_algorithm_spec.train_trial_spec.train_trial_job_spec.worker_pool_specs.python_package_spec.args = ['args_value1', 'args_value2']
    nas_job.nas_job_spec.multi_trial_algorithm_spec.train_trial_spec.train_trial_job_spec.worker_pool_specs.python_package_spec.env.name = "name_value"
    nas_job.nas_job_spec.multi_trial_algorithm_spec.train_trial_spec.train_trial_job_spec.worker_pool_specs.python_package_spec.env.value = "value_value"
    nas_job.nas_job_spec.multi_trial_algorithm_spec.train_trial_spec.train_trial_job_spec.worker_pool_specs.machine_spec.machine_type = "machine_type_value"
    nas_job.nas_job_spec.multi_trial_algorithm_spec.train_trial_spec.train_trial_job_spec.worker_pool_specs.machine_spec.accelerator_type = "TPU_V5_LITEPOD"
    nas_job.nas_job_spec.multi_trial_algorithm_spec.train_trial_spec.train_trial_job_spec.worker_pool_specs.machine_spec.accelerator_count = 1805
    nas_job.nas_job_spec.multi_trial_algorithm_spec.train_trial_spec.train_trial_job_spec.worker_pool_specs.machine_spec.tpu_topology = "tpu_topology_value"
    nas_job.nas_job_spec.multi_trial_algorithm_spec.train_trial_spec.train_trial_job_spec.worker_pool_specs.replica_count = 1384
    nas_job.nas_job_spec.multi_trial_algorithm_spec.train_trial_spec.train_trial_job_spec.worker_pool_specs.nfs_mounts.server = "server_value"
    nas_job.nas_job_spec.multi_trial_algorithm_spec.train_trial_spec.train_trial_job_spec.worker_pool_specs.nfs_mounts.path = "path_value"
    nas_job.nas_job_spec.multi_trial_algorithm_spec.train_trial_spec.train_trial_job_spec.worker_pool_specs.nfs_mounts.mount_point = "mount_point_value"
    nas_job.nas_job_spec.multi_trial_algorithm_spec.train_trial_spec.train_trial_job_spec.worker_pool_specs.disk_spec.boot_disk_type = "boot_disk_type_value"
    nas_job.nas_job_spec.multi_trial_algorithm_spec.train_trial_spec.train_trial_job_spec.worker_pool_specs.disk_spec.boot_disk_size_gb = 1792
    nas_job.nas_job_spec.multi_trial_algorithm_spec.train_trial_spec.train_trial_job_spec.scheduling.timeout.seconds = 751
    nas_job.nas_job_spec.multi_trial_algorithm_spec.train_trial_spec.train_trial_job_spec.scheduling.timeout.nanos = 543
    nas_job.nas_job_spec.multi_trial_algorithm_spec.train_trial_spec.train_trial_job_spec.scheduling.restart_job_on_worker_restart = True
    nas_job.nas_job_spec.multi_trial_algorithm_spec.train_trial_spec.train_trial_job_spec.scheduling.disable_retries = True
    nas_job.nas_job_spec.multi_trial_algorithm_spec.train_trial_spec.train_trial_job_spec.service_account = "service_account_value"
    nas_job.nas_job_spec.multi_trial_algorithm_spec.train_trial_spec.train_trial_job_spec.network = "network_value"
    nas_job.nas_job_spec.multi_trial_algorithm_spec.train_trial_spec.train_trial_job_spec.reserved_ip_ranges = ['reserved_ip_ranges_value1', 'reserved_ip_ranges_value2']
    nas_job.nas_job_spec.multi_trial_algorithm_spec.train_trial_spec.train_trial_job_spec.base_output_directory.output_uri_prefix = "output_uri_prefix_value"
    nas_job.nas_job_spec.multi_trial_algorithm_spec.train_trial_spec.train_trial_job_spec.protected_artifact_location_id = "protected_artifact_location_id_value"
    nas_job.nas_job_spec.multi_trial_algorithm_spec.train_trial_spec.train_trial_job_spec.tensorboard = "tensorboard_value"
    nas_job.nas_job_spec.multi_trial_algorithm_spec.train_trial_spec.train_trial_job_spec.enable_web_access = True
    nas_job.nas_job_spec.multi_trial_algorithm_spec.train_trial_spec.train_trial_job_spec.enable_dashboard_access = True
    nas_job.nas_job_spec.multi_trial_algorithm_spec.train_trial_spec.train_trial_job_spec.experiment = "experiment_value"
    nas_job.nas_job_spec.multi_trial_algorithm_spec.train_trial_spec.train_trial_job_spec.experiment_run = "experiment_run_value"
    nas_job.nas_job_spec.multi_trial_algorithm_spec.train_trial_spec.train_trial_job_spec.models = ['models_value1', 'models_value2']
    nas_job.nas_job_spec.multi_trial_algorithm_spec.train_trial_spec.max_parallel_trial_count = 2549
    nas_job.nas_job_spec.multi_trial_algorithm_spec.train_trial_spec.frequency = 978
    nas_job.nas_job_spec.resume_nas_job_id = "resume_nas_job_id_value"
    nas_job.nas_job_spec.search_space_spec = "search_space_spec_value"
    nas_job.nas_job_output.multi_trial_job_output.search_trials.id = "id_value"
    nas_job.nas_job_output.multi_trial_job_output.search_trials.state = "INFEASIBLE"
    nas_job.nas_job_output.multi_trial_job_output.search_trials.final_measurement.elapsed_duration.seconds = 751
    nas_job.nas_job_output.multi_trial_job_output.search_trials.final_measurement.elapsed_duration.nanos = 543
    nas_job.nas_job_output.multi_trial_job_output.search_trials.final_measurement.step_count = 1092
    nas_job.nas_job_output.multi_trial_job_output.search_trials.final_measurement.metrics.metric_id = "metric_id_value"
    nas_job.nas_job_output.multi_trial_job_output.search_trials.final_measurement.metrics.value = 0.541
    nas_job.nas_job_output.multi_trial_job_output.search_trials.start_time.seconds = 751
    nas_job.nas_job_output.multi_trial_job_output.search_trials.start_time.nanos = 543
    nas_job.nas_job_output.multi_trial_job_output.search_trials.end_time.seconds = 751
    nas_job.nas_job_output.multi_trial_job_output.search_trials.end_time.nanos = 543
    nas_job.nas_job_output.multi_trial_job_output.train_trials.id = "id_value"
    nas_job.nas_job_output.multi_trial_job_output.train_trials.state = "INFEASIBLE"
    nas_job.nas_job_output.multi_trial_job_output.train_trials.final_measurement.elapsed_duration.seconds = 751
    nas_job.nas_job_output.multi_trial_job_output.train_trials.final_measurement.elapsed_duration.nanos = 543
    nas_job.nas_job_output.multi_trial_job_output.train_trials.final_measurement.step_count = 1092
    nas_job.nas_job_output.multi_trial_job_output.train_trials.final_measurement.metrics.metric_id = "metric_id_value"
    nas_job.nas_job_output.multi_trial_job_output.train_trials.final_measurement.metrics.value = 0.541
    nas_job.nas_job_output.multi_trial_job_output.train_trials.start_time.seconds = 751
    nas_job.nas_job_output.multi_trial_job_output.train_trials.start_time.nanos = 543
    nas_job.nas_job_output.multi_trial_job_output.train_trials.end_time.seconds = 751
    nas_job.nas_job_output.multi_trial_job_output.train_trials.end_time.nanos = 543
    nas_job.state = "JOB_STATE_PARTIALLY_SUCCEEDED"
    nas_job.create_time.seconds = 751
    nas_job.create_time.nanos = 543
    nas_job.start_time.seconds = 751
    nas_job.start_time.nanos = 543
    nas_job.end_time.seconds = 751
    nas_job.end_time.nanos = 543
    nas_job.update_time.seconds = 751
    nas_job.update_time.nanos = 543
    nas_job.error.code = 411
    nas_job.error.message = "message_value"
    nas_job.error.details.type_url = "type.googleapis.com/google.protobuf.Empty"
    nas_job.error.details.value = b'value_blob'
    nas_job.labels.key = "key_value"
    nas_job.labels.value = "value_value"
    nas_job.encryption_spec.kms_key_name = "kms_key_name_value"
    nas_job.enable_restricted_image_training = True

    request = aiplatform_v1.CreateNasJobRequest(
        parent="parent_value",
        nas_job=nas_job,
    )

    # Make the request
    response = await client.create_nas_job(request=request)

    # Handle the response
    print(response)

# [END aiplatform_v1_generated_JobService_CreateNasJob_async]

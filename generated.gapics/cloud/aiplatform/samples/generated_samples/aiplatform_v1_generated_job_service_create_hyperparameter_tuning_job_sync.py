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
# Snippet for CreateHyperparameterTuningJob
# NOTE: This snippet has been automatically generated for illustrative purposes only.
# It may require modifications to work in your environment.

# To install the latest published package dependency, execute the following:
#   python3 -m pip install google-cloud-aiplatform


# [START aiplatform_v1_generated_JobService_CreateHyperparameterTuningJob_sync]
# This snippet has been automatically generated and should be regarded as a
# code template only.
# It will require modifications to work:
# - It may require correct/in-range values for request initialization.
# - It may require specifying regional endpoints when creating the service
#   client as shown in:
#   https://googleapis.dev/python/google-api-core/latest/client_options.html
from google.cloud import aiplatform_v1


def sample_create_hyperparameter_tuning_job():
    # Create a client
    client = aiplatform_v1.JobServiceClient()

    # Initialize request argument(s)
    hyperparameter_tuning_job = aiplatform_v1.HyperparameterTuningJob()
    hyperparameter_tuning_job.name = "name_value"
    hyperparameter_tuning_job.display_name = "display_name_value"
    hyperparameter_tuning_job.study_spec.decay_curve_stopping_spec.use_elapsed_duration = True
    hyperparameter_tuning_job.study_spec.median_automated_stopping_spec.use_elapsed_duration = True
    hyperparameter_tuning_job.study_spec.convex_automated_stopping_spec.max_step_count = 1513
    hyperparameter_tuning_job.study_spec.convex_automated_stopping_spec.min_step_count = 1511
    hyperparameter_tuning_job.study_spec.convex_automated_stopping_spec.min_measurement_count = 2257
    hyperparameter_tuning_job.study_spec.convex_automated_stopping_spec.learning_rate_parameter_name = "learning_rate_parameter_name_value"
    hyperparameter_tuning_job.study_spec.convex_automated_stopping_spec.use_elapsed_duration = True
    hyperparameter_tuning_job.study_spec.convex_automated_stopping_spec.update_all_stopped_trials = True
    hyperparameter_tuning_job.study_spec.metrics.metric_id = "metric_id_value"
    hyperparameter_tuning_job.study_spec.metrics.goal = "MINIMIZE"
    hyperparameter_tuning_job.study_spec.metrics.safety_config.safety_threshold = 0.17200000000000001
    hyperparameter_tuning_job.study_spec.metrics.safety_config.desired_min_safe_trials_fraction = 0.33640000000000003
    hyperparameter_tuning_job.study_spec.parameters.double_value_spec.min_value = 0.96
    hyperparameter_tuning_job.study_spec.parameters.double_value_spec.max_value = 0.962
    hyperparameter_tuning_job.study_spec.parameters.double_value_spec.default_value = 0.13770000000000002
    hyperparameter_tuning_job.study_spec.parameters.integer_value_spec.min_value = 960
    hyperparameter_tuning_job.study_spec.parameters.integer_value_spec.max_value = 962
    hyperparameter_tuning_job.study_spec.parameters.integer_value_spec.default_value = 1377
    hyperparameter_tuning_job.study_spec.parameters.categorical_value_spec.values = ['values_value1', 'values_value2']
    hyperparameter_tuning_job.study_spec.parameters.categorical_value_spec.default_value = "default_value_value"
    hyperparameter_tuning_job.study_spec.parameters.discrete_value_spec.values = [0.657, 0.658]
    hyperparameter_tuning_job.study_spec.parameters.discrete_value_spec.default_value = 0.13770000000000002
    hyperparameter_tuning_job.study_spec.parameters.parameter_id = "parameter_id_value"
    hyperparameter_tuning_job.study_spec.parameters.scale_type = "UNIT_REVERSE_LOG_SCALE"
    hyperparameter_tuning_job.study_spec.parameters.conditional_parameter_specs.parent_discrete_values.values = [0.657, 0.658]
    hyperparameter_tuning_job.study_spec.parameters.conditional_parameter_specs.parent_int_values.values = [657, 658]
    hyperparameter_tuning_job.study_spec.parameters.conditional_parameter_specs.parent_categorical_values.values = ['values_value1', 'values_value2']
    hyperparameter_tuning_job.study_spec.parameters.conditional_parameter_specs.parameter_spec = "study.StudySpec.ParameterSpec(double_value_spec=study.StudySpec.ParameterSpec.DoubleValueSpec(min_value=0.96))"
    hyperparameter_tuning_job.study_spec.algorithm = "RANDOM_SEARCH"
    hyperparameter_tuning_job.study_spec.observation_noise = "HIGH"
    hyperparameter_tuning_job.study_spec.measurement_selection_type = "BEST_MEASUREMENT"
    hyperparameter_tuning_job.study_spec.study_stopping_config.should_stop_asap.value = True
    hyperparameter_tuning_job.study_spec.study_stopping_config.minimum_runtime_constraint.max_duration.seconds = 751
    hyperparameter_tuning_job.study_spec.study_stopping_config.minimum_runtime_constraint.max_duration.nanos = 543
    hyperparameter_tuning_job.study_spec.study_stopping_config.minimum_runtime_constraint.end_time.seconds = 751
    hyperparameter_tuning_job.study_spec.study_stopping_config.minimum_runtime_constraint.end_time.nanos = 543
    hyperparameter_tuning_job.study_spec.study_stopping_config.maximum_runtime_constraint.max_duration.seconds = 751
    hyperparameter_tuning_job.study_spec.study_stopping_config.maximum_runtime_constraint.max_duration.nanos = 543
    hyperparameter_tuning_job.study_spec.study_stopping_config.maximum_runtime_constraint.end_time.seconds = 751
    hyperparameter_tuning_job.study_spec.study_stopping_config.maximum_runtime_constraint.end_time.nanos = 543
    hyperparameter_tuning_job.study_spec.study_stopping_config.min_num_trials.value = 541
    hyperparameter_tuning_job.study_spec.study_stopping_config.max_num_trials.value = 541
    hyperparameter_tuning_job.study_spec.study_stopping_config.max_num_trials_no_progress.value = 541
    hyperparameter_tuning_job.study_spec.study_stopping_config.max_duration_no_progress.seconds = 751
    hyperparameter_tuning_job.study_spec.study_stopping_config.max_duration_no_progress.nanos = 543
    hyperparameter_tuning_job.max_trial_count = 1609
    hyperparameter_tuning_job.parallel_trial_count = 2128
    hyperparameter_tuning_job.max_failed_trial_count = 2317
    hyperparameter_tuning_job.trial_job_spec.persistent_resource_id = "persistent_resource_id_value"
    hyperparameter_tuning_job.trial_job_spec.worker_pool_specs.container_spec.image_uri = "image_uri_value"
    hyperparameter_tuning_job.trial_job_spec.worker_pool_specs.container_spec.command = ['command_value1', 'command_value2']
    hyperparameter_tuning_job.trial_job_spec.worker_pool_specs.container_spec.args = ['args_value1', 'args_value2']
    hyperparameter_tuning_job.trial_job_spec.worker_pool_specs.container_spec.env.name = "name_value"
    hyperparameter_tuning_job.trial_job_spec.worker_pool_specs.container_spec.env.value = "value_value"
    hyperparameter_tuning_job.trial_job_spec.worker_pool_specs.python_package_spec.executor_image_uri = "executor_image_uri_value"
    hyperparameter_tuning_job.trial_job_spec.worker_pool_specs.python_package_spec.package_uris = ['package_uris_value1', 'package_uris_value2']
    hyperparameter_tuning_job.trial_job_spec.worker_pool_specs.python_package_spec.python_module = "python_module_value"
    hyperparameter_tuning_job.trial_job_spec.worker_pool_specs.python_package_spec.args = ['args_value1', 'args_value2']
    hyperparameter_tuning_job.trial_job_spec.worker_pool_specs.python_package_spec.env.name = "name_value"
    hyperparameter_tuning_job.trial_job_spec.worker_pool_specs.python_package_spec.env.value = "value_value"
    hyperparameter_tuning_job.trial_job_spec.worker_pool_specs.machine_spec.machine_type = "machine_type_value"
    hyperparameter_tuning_job.trial_job_spec.worker_pool_specs.machine_spec.accelerator_type = "TPU_V5_LITEPOD"
    hyperparameter_tuning_job.trial_job_spec.worker_pool_specs.machine_spec.accelerator_count = 1805
    hyperparameter_tuning_job.trial_job_spec.worker_pool_specs.machine_spec.tpu_topology = "tpu_topology_value"
    hyperparameter_tuning_job.trial_job_spec.worker_pool_specs.replica_count = 1384
    hyperparameter_tuning_job.trial_job_spec.worker_pool_specs.nfs_mounts.server = "server_value"
    hyperparameter_tuning_job.trial_job_spec.worker_pool_specs.nfs_mounts.path = "path_value"
    hyperparameter_tuning_job.trial_job_spec.worker_pool_specs.nfs_mounts.mount_point = "mount_point_value"
    hyperparameter_tuning_job.trial_job_spec.worker_pool_specs.disk_spec.boot_disk_type = "boot_disk_type_value"
    hyperparameter_tuning_job.trial_job_spec.worker_pool_specs.disk_spec.boot_disk_size_gb = 1792
    hyperparameter_tuning_job.trial_job_spec.scheduling.timeout.seconds = 751
    hyperparameter_tuning_job.trial_job_spec.scheduling.timeout.nanos = 543
    hyperparameter_tuning_job.trial_job_spec.scheduling.restart_job_on_worker_restart = True
    hyperparameter_tuning_job.trial_job_spec.scheduling.disable_retries = True
    hyperparameter_tuning_job.trial_job_spec.service_account = "service_account_value"
    hyperparameter_tuning_job.trial_job_spec.network = "network_value"
    hyperparameter_tuning_job.trial_job_spec.reserved_ip_ranges = ['reserved_ip_ranges_value1', 'reserved_ip_ranges_value2']
    hyperparameter_tuning_job.trial_job_spec.base_output_directory.output_uri_prefix = "output_uri_prefix_value"
    hyperparameter_tuning_job.trial_job_spec.protected_artifact_location_id = "protected_artifact_location_id_value"
    hyperparameter_tuning_job.trial_job_spec.tensorboard = "tensorboard_value"
    hyperparameter_tuning_job.trial_job_spec.enable_web_access = True
    hyperparameter_tuning_job.trial_job_spec.enable_dashboard_access = True
    hyperparameter_tuning_job.trial_job_spec.experiment = "experiment_value"
    hyperparameter_tuning_job.trial_job_spec.experiment_run = "experiment_run_value"
    hyperparameter_tuning_job.trial_job_spec.models = ['models_value1', 'models_value2']
    hyperparameter_tuning_job.trials.name = "name_value"
    hyperparameter_tuning_job.trials.id = "id_value"
    hyperparameter_tuning_job.trials.state = "INFEASIBLE"
    hyperparameter_tuning_job.trials.parameters.parameter_id = "parameter_id_value"
    hyperparameter_tuning_job.trials.parameters.value.null_value = "NULL_VALUE"
    hyperparameter_tuning_job.trials.parameters.value.number_value = 0.1285
    hyperparameter_tuning_job.trials.parameters.value.string_value = "string_value_value"
    hyperparameter_tuning_job.trials.parameters.value.bool_value = True
    hyperparameter_tuning_job.trials.parameters.value.struct_value.fields.key = "key_value"
    hyperparameter_tuning_job.trials.parameters.value.struct_value.fields.value = "struct_pb2.Value(null_value=struct_pb2.NullValue.NULL_VALUE)"
    hyperparameter_tuning_job.trials.parameters.value.list_value.values = "[struct_pb2.Value(null_value=struct_pb2.NullValue.NULL_VALUE)]"
    hyperparameter_tuning_job.trials.final_measurement.elapsed_duration.seconds = 751
    hyperparameter_tuning_job.trials.final_measurement.elapsed_duration.nanos = 543
    hyperparameter_tuning_job.trials.final_measurement.step_count = 1092
    hyperparameter_tuning_job.trials.final_measurement.metrics.metric_id = "metric_id_value"
    hyperparameter_tuning_job.trials.final_measurement.metrics.value = 0.541
    hyperparameter_tuning_job.trials.measurements.elapsed_duration.seconds = 751
    hyperparameter_tuning_job.trials.measurements.elapsed_duration.nanos = 543
    hyperparameter_tuning_job.trials.measurements.step_count = 1092
    hyperparameter_tuning_job.trials.measurements.metrics.metric_id = "metric_id_value"
    hyperparameter_tuning_job.trials.measurements.metrics.value = 0.541
    hyperparameter_tuning_job.trials.start_time.seconds = 751
    hyperparameter_tuning_job.trials.start_time.nanos = 543
    hyperparameter_tuning_job.trials.end_time.seconds = 751
    hyperparameter_tuning_job.trials.end_time.nanos = 543
    hyperparameter_tuning_job.trials.client_id = "client_id_value"
    hyperparameter_tuning_job.trials.infeasible_reason = "infeasible_reason_value"
    hyperparameter_tuning_job.trials.custom_job = "custom_job_value"
    hyperparameter_tuning_job.trials.web_access_uris.key = "key_value"
    hyperparameter_tuning_job.trials.web_access_uris.value = "value_value"
    hyperparameter_tuning_job.state = "JOB_STATE_PARTIALLY_SUCCEEDED"
    hyperparameter_tuning_job.create_time.seconds = 751
    hyperparameter_tuning_job.create_time.nanos = 543
    hyperparameter_tuning_job.start_time.seconds = 751
    hyperparameter_tuning_job.start_time.nanos = 543
    hyperparameter_tuning_job.end_time.seconds = 751
    hyperparameter_tuning_job.end_time.nanos = 543
    hyperparameter_tuning_job.update_time.seconds = 751
    hyperparameter_tuning_job.update_time.nanos = 543
    hyperparameter_tuning_job.error.code = 411
    hyperparameter_tuning_job.error.message = "message_value"
    hyperparameter_tuning_job.error.details.type_url = "type.googleapis.com/google.protobuf.Empty"
    hyperparameter_tuning_job.error.details.value = b'value_blob'
    hyperparameter_tuning_job.labels.key = "key_value"
    hyperparameter_tuning_job.labels.value = "value_value"
    hyperparameter_tuning_job.encryption_spec.kms_key_name = "kms_key_name_value"

    request = aiplatform_v1.CreateHyperparameterTuningJobRequest(
        parent="parent_value",
        hyperparameter_tuning_job=hyperparameter_tuning_job,
    )

    # Make the request
    response = client.create_hyperparameter_tuning_job(request=request)

    # Handle the response
    print(response)

# [END aiplatform_v1_generated_JobService_CreateHyperparameterTuningJob_sync]

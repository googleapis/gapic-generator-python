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
# Snippet for CreateStudy
# NOTE: This snippet has been automatically generated for illustrative purposes only.
# It may require modifications to work in your environment.

# To install the latest published package dependency, execute the following:
#   python3 -m pip install google-cloud-aiplatform


# [START aiplatform_v1_generated_VizierService_CreateStudy_async]
# This snippet has been automatically generated and should be regarded as a
# code template only.
# It will require modifications to work:
# - It may require correct/in-range values for request initialization.
# - It may require specifying regional endpoints when creating the service
#   client as shown in:
#   https://googleapis.dev/python/google-api-core/latest/client_options.html
from google.cloud import aiplatform_v1


async def sample_create_study():
    # Create a client
    client = aiplatform_v1.VizierServiceAsyncClient()

    # Initialize request argument(s)
    study = aiplatform_v1.Study()
    study.name = "name_value"
    study.display_name = "display_name_value"
    study.study_spec.decay_curve_stopping_spec.use_elapsed_duration = True
    study.study_spec.median_automated_stopping_spec.use_elapsed_duration = True
    study.study_spec.convex_automated_stopping_spec.max_step_count = 1513
    study.study_spec.convex_automated_stopping_spec.min_step_count = 1511
    study.study_spec.convex_automated_stopping_spec.min_measurement_count = 2257
    study.study_spec.convex_automated_stopping_spec.learning_rate_parameter_name = "learning_rate_parameter_name_value"
    study.study_spec.convex_automated_stopping_spec.use_elapsed_duration = True
    study.study_spec.convex_automated_stopping_spec.update_all_stopped_trials = True
    study.study_spec.metrics.metric_id = "metric_id_value"
    study.study_spec.metrics.goal = "MINIMIZE"
    study.study_spec.metrics.safety_config.safety_threshold = 0.17200000000000001
    study.study_spec.metrics.safety_config.desired_min_safe_trials_fraction = 0.33640000000000003
    study.study_spec.parameters.double_value_spec.min_value = 0.96
    study.study_spec.parameters.double_value_spec.max_value = 0.962
    study.study_spec.parameters.double_value_spec.default_value = 0.13770000000000002
    study.study_spec.parameters.integer_value_spec.min_value = 960
    study.study_spec.parameters.integer_value_spec.max_value = 962
    study.study_spec.parameters.integer_value_spec.default_value = 1377
    study.study_spec.parameters.categorical_value_spec.values = ['values_value1', 'values_value2']
    study.study_spec.parameters.categorical_value_spec.default_value = "default_value_value"
    study.study_spec.parameters.discrete_value_spec.values = [0.657, 0.658]
    study.study_spec.parameters.discrete_value_spec.default_value = 0.13770000000000002
    study.study_spec.parameters.parameter_id = "parameter_id_value"
    study.study_spec.parameters.scale_type = "UNIT_REVERSE_LOG_SCALE"
    study.study_spec.parameters.conditional_parameter_specs.parent_discrete_values.values = [0.657, 0.658]
    study.study_spec.parameters.conditional_parameter_specs.parent_int_values.values = [657, 658]
    study.study_spec.parameters.conditional_parameter_specs.parent_categorical_values.values = ['values_value1', 'values_value2']
    study.study_spec.parameters.conditional_parameter_specs.parameter_spec = "gca_study.StudySpec.ParameterSpec(double_value_spec=study.StudySpec.ParameterSpec.DoubleValueSpec(min_value=0.96))"
    study.study_spec.algorithm = "RANDOM_SEARCH"
    study.study_spec.observation_noise = "HIGH"
    study.study_spec.measurement_selection_type = "BEST_MEASUREMENT"
    study.study_spec.study_stopping_config.should_stop_asap.value = True
    study.study_spec.study_stopping_config.minimum_runtime_constraint.max_duration.seconds = 751
    study.study_spec.study_stopping_config.minimum_runtime_constraint.max_duration.nanos = 543
    study.study_spec.study_stopping_config.minimum_runtime_constraint.end_time.seconds = 751
    study.study_spec.study_stopping_config.minimum_runtime_constraint.end_time.nanos = 543
    study.study_spec.study_stopping_config.maximum_runtime_constraint.max_duration.seconds = 751
    study.study_spec.study_stopping_config.maximum_runtime_constraint.max_duration.nanos = 543
    study.study_spec.study_stopping_config.maximum_runtime_constraint.end_time.seconds = 751
    study.study_spec.study_stopping_config.maximum_runtime_constraint.end_time.nanos = 543
    study.study_spec.study_stopping_config.min_num_trials.value = 541
    study.study_spec.study_stopping_config.max_num_trials.value = 541
    study.study_spec.study_stopping_config.max_num_trials_no_progress.value = 541
    study.study_spec.study_stopping_config.max_duration_no_progress.seconds = 751
    study.study_spec.study_stopping_config.max_duration_no_progress.nanos = 543
    study.state = "COMPLETED"
    study.create_time.seconds = 751
    study.create_time.nanos = 543
    study.inactive_reason = "inactive_reason_value"

    request = aiplatform_v1.CreateStudyRequest(
        parent="parent_value",
        study=study,
    )

    # Make the request
    response = await client.create_study(request=request)

    # Handle the response
    print(response)

# [END aiplatform_v1_generated_VizierService_CreateStudy_async]

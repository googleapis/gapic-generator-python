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
# Snippet for SetIamPolicy
# NOTE: This snippet has been automatically generated for illustrative purposes only.
# It may require modifications to work in your environment.

# To install the latest published package dependency, execute the following:
#   python3 -m pip install google-cloud-secretmanager


# [START secretmanager_v1_generated_SecretManagerService_SetIamPolicy_sync]
# This snippet has been automatically generated and should be regarded as a
# code template only.
# It will require modifications to work:
# - It may require correct/in-range values for request initialization.
# - It may require specifying regional endpoints when creating the service
#   client as shown in:
#   https://googleapis.dev/python/google-api-core/latest/client_options.html
from google.cloud import secretmanager_v1
from google.iam.v1 import iam_policy_pb2  # type: ignore


def sample_set_iam_policy():
    # Create a client
    client = secretmanager_v1.SecretManagerServiceClient()

    # Initialize request argument(s)
    policy = iam_policy_pb2.Policy()
    policy.version = 774
    policy.bindings.role = "role_value"
    policy.bindings.members = ['members_value1', 'members_value2']
    policy.bindings.condition.expression = "expression_value"
    policy.bindings.condition.title = "title_value"
    policy.bindings.condition.description = "description_value"
    policy.bindings.condition.location = "location_value"
    policy.audit_configs.service = "service_value"
    policy.audit_configs.audit_log_configs.log_type = "DATA_READ"
    policy.audit_configs.audit_log_configs.exempted_members = ['exempted_members_value1', 'exempted_members_value2']
    policy.etag = b'etag_blob'

    update_mask = iam_policy_pb2.FieldMask()
    update_mask.paths = ['paths_value1', 'paths_value2']

    request = iam_policy_pb2.SetIamPolicyRequest(
        resource="resource_value",
        policy=policy,
        update_mask=update_mask,
    )

    # Make the request
    response = client.set_iam_policy(request=request)

    # Handle the response
    print(response)

# [END secretmanager_v1_generated_SecretManagerService_SetIamPolicy_sync]

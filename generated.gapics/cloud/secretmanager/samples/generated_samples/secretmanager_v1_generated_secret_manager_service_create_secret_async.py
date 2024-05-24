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
# Snippet for CreateSecret
# NOTE: This snippet has been automatically generated for illustrative purposes only.
# It may require modifications to work in your environment.

# To install the latest published package dependency, execute the following:
#   python3 -m pip install google-cloud-secretmanager


# [START secretmanager_v1_generated_SecretManagerService_CreateSecret_async]
# This snippet has been automatically generated and should be regarded as a
# code template only.
# It will require modifications to work:
# - It may require correct/in-range values for request initialization.
# - It may require specifying regional endpoints when creating the service
#   client as shown in:
#   https://googleapis.dev/python/google-api-core/latest/client_options.html
from google.cloud import secretmanager_v1


async def sample_create_secret():
    # Create a client
    client = secretmanager_v1.SecretManagerServiceAsyncClient()

    # Initialize request argument(s)
    secret = secretmanager_v1.Secret()
    secret.name = "name_value"
    secret.replication.automatic.customer_managed_encryption.kms_key_name = "kms_key_name_value"
    secret.replication.user_managed.replicas.location = "location_value"
    secret.replication.user_managed.replicas.customer_managed_encryption.kms_key_name = "kms_key_name_value"
    secret.create_time.seconds = 751
    secret.create_time.nanos = 543
    secret.labels.key = "key_value"
    secret.labels.value = "value_value"
    secret.topics.name = "name_value"
    secret.expire_time.seconds = 751
    secret.expire_time.nanos = 543
    secret.ttl.seconds = 751
    secret.ttl.nanos = 543
    secret.etag = "etag_value"
    secret.rotation.next_rotation_time.seconds = 751
    secret.rotation.next_rotation_time.nanos = 543
    secret.rotation.rotation_period.seconds = 751
    secret.rotation.rotation_period.nanos = 543
    secret.version_aliases.key = "key_value"
    secret.version_aliases.value = 541
    secret.annotations.key = "key_value"
    secret.annotations.value = "value_value"
    secret.version_destroy_ttl.seconds = 751
    secret.version_destroy_ttl.nanos = 543
    secret.customer_managed_encryption.kms_key_name = "kms_key_name_value"

    request = secretmanager_v1.CreateSecretRequest(
        parent="parent_value",
        secret_id="secret_id_value",
        secret=secret,
    )

    # Make the request
    response = await client.create_secret(request=request)

    # Handle the response
    print(response)

# [END secretmanager_v1_generated_SecretManagerService_CreateSecret_async]

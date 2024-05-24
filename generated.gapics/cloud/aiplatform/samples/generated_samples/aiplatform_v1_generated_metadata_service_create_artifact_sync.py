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
# Snippet for CreateArtifact
# NOTE: This snippet has been automatically generated for illustrative purposes only.
# It may require modifications to work in your environment.

# To install the latest published package dependency, execute the following:
#   python3 -m pip install google-cloud-aiplatform


# [START aiplatform_v1_generated_MetadataService_CreateArtifact_sync]
# This snippet has been automatically generated and should be regarded as a
# code template only.
# It will require modifications to work:
# - It may require correct/in-range values for request initialization.
# - It may require specifying regional endpoints when creating the service
#   client as shown in:
#   https://googleapis.dev/python/google-api-core/latest/client_options.html
from google.cloud import aiplatform_v1


def sample_create_artifact():
    # Create a client
    client = aiplatform_v1.MetadataServiceClient()

    # Initialize request argument(s)
    artifact = aiplatform_v1.Artifact()
    artifact.name = "name_value"
    artifact.display_name = "display_name_value"
    artifact.uri = "uri_value"
    artifact.etag = "etag_value"
    artifact.labels.key = "key_value"
    artifact.labels.value = "value_value"
    artifact.create_time.seconds = 751
    artifact.create_time.nanos = 543
    artifact.update_time.seconds = 751
    artifact.update_time.nanos = 543
    artifact.state = "LIVE"
    artifact.schema_title = "schema_title_value"
    artifact.schema_version = "schema_version_value"
    artifact.metadata.fields.key = "key_value"
    artifact.metadata.fields.value.null_value = "NULL_VALUE"
    artifact.metadata.fields.value.number_value = 0.1285
    artifact.metadata.fields.value.string_value = "string_value_value"
    artifact.metadata.fields.value.bool_value = True
    artifact.metadata.fields.value.struct_value = "struct_pb2.Struct(fields={'key_value': struct_pb2.Value(null_value=struct_pb2.NullValue.NULL_VALUE)})"
    artifact.metadata.fields.value.list_value.values = "[struct_pb2.Value(null_value=struct_pb2.NullValue.NULL_VALUE)]"
    artifact.description = "description_value"

    request = aiplatform_v1.CreateArtifactRequest(
        parent="parent_value",
        artifact=artifact,
        artifact_id="artifact_id_value",
    )

    # Make the request
    response = client.create_artifact(request=request)

    # Handle the response
    print(response)

# [END aiplatform_v1_generated_MetadataService_CreateArtifact_sync]

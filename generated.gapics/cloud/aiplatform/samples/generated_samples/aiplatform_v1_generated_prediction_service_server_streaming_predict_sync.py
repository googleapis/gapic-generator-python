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
# Snippet for ServerStreamingPredict
# NOTE: This snippet has been automatically generated for illustrative purposes only.
# It may require modifications to work in your environment.

# To install the latest published package dependency, execute the following:
#   python3 -m pip install google-cloud-aiplatform


# [START aiplatform_v1_generated_PredictionService_ServerStreamingPredict_sync]
# This snippet has been automatically generated and should be regarded as a
# code template only.
# It will require modifications to work:
# - It may require correct/in-range values for request initialization.
# - It may require specifying regional endpoints when creating the service
#   client as shown in:
#   https://googleapis.dev/python/google-api-core/latest/client_options.html
from google.cloud import aiplatform_v1


def sample_server_streaming_predict():
    # Create a client
    client = aiplatform_v1.PredictionServiceClient()

    # Initialize request argument(s)
    inputs = aiplatform_v1.Tensor()
    inputs.dtype = "UINT64"
    inputs.shape = [530, 531]
    inputs.bool_val = [True, True]
    inputs.string_val = ['string_val_value1', 'string_val_value2']
    inputs.bytes_val = [b'bytes_val_blob1', b'bytes_val_blob2']
    inputs.float_val = [0.9530000000000001, 0.9540000000000001]
    inputs.double_val = [0.10540000000000001, 0.10550000000000001]
    inputs.int_val = [750, 751]
    inputs.int64_val = [856, 857]
    inputs.uint_val = [867, 868]
    inputs.uint64_val = [973, 974]
    inputs.list_val = "[types.Tensor(dtype=types.Tensor.DataType.BOOL)]"
    inputs.struct_val.key = "key_value"
    inputs.struct_val.value = "types.Tensor(dtype=types.Tensor.DataType.BOOL)"
    inputs.tensor_val = b'tensor_val_blob'

    parameters = aiplatform_v1.Tensor()
    parameters.dtype = "UINT64"
    parameters.shape = [530, 531]
    parameters.bool_val = [True, True]
    parameters.string_val = ['string_val_value1', 'string_val_value2']
    parameters.bytes_val = [b'bytes_val_blob1', b'bytes_val_blob2']
    parameters.float_val = [0.9530000000000001, 0.9540000000000001]
    parameters.double_val = [0.10540000000000001, 0.10550000000000001]
    parameters.int_val = [750, 751]
    parameters.int64_val = [856, 857]
    parameters.uint_val = [867, 868]
    parameters.uint64_val = [973, 974]
    parameters.list_val = "[types.Tensor(dtype=types.Tensor.DataType.BOOL)]"
    parameters.struct_val.key = "key_value"
    parameters.struct_val.value = "types.Tensor(dtype=types.Tensor.DataType.BOOL)"
    parameters.tensor_val = b'tensor_val_blob'

    request = aiplatform_v1.StreamingPredictRequest(
        endpoint="endpoint_value",
        inputs=inputs,
        parameters=parameters,
    )

    # Make the request
    stream = client.server_streaming_predict(request=request)

    # Handle the response
    for response in stream:
        print(response)

# [END aiplatform_v1_generated_PredictionService_ServerStreamingPredict_sync]

# Copyright 2021 Google LLC
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     https://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import pytest
from google import showcase
from google.rpc import error_details_pb2
from google.protobuf import any_pb2
from grpc_status import rpc_status
from google.api_core import exceptions


def test_serialize_boolean(compliance):
    request = showcase.EnumRequest(unknown_enum = True)
    compliance.get_enum(request=request)

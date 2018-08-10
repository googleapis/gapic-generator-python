# Copyright 2018 Google LLC
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

from google import showcase_v1alpha1
from google.rpc import code_pb2


def test_unary():
    client = showcase_v1alpha1.Showcase()
    response = client.echo({
        'content': 'The hail in Wales falls mainly on the snails.',
    })
    assert response.content == 'The hail in Wales falls mainly on the snails.'


def test_unary_error():
    client = showcase_v1alpha1.Showcase()
    with pytest.raises(ValueError):
        response = client.echo({
            'error': code_pb2.Status.Value('INVALID_ARGUMENT'),
        })

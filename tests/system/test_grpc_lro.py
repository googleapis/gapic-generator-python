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

from datetime import datetime, timedelta, timezone

from google import showcase_v1alpha3


def test_lro(echo):
    wait_request = {
        'end_time': datetime.now(tz=timezone.utc) + timedelta(seconds=1),
        'success': {'content': 'The hail in Wales falls mainly '
                               'on the snails...eventually.'},
    }
    future = echo.wait(wait_request)
    response = future.result()
    assert isinstance(response, showcase_v1alpha3.WaitResponse)
    assert response.content.endswith('the snails...eventually.')

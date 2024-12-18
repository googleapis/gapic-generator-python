# Copyright 2024 Google LLC
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

import os
import pytest

from google import showcase


@pytest.mark.parametrize(
    "transport,response_metadata",
    [
        ("grpc", ("something1", "something_value1")),
        ("rest", ("X-Showcase-Request-Something1", "something_value1")),
    ],
)
def test_metadata_response_unary(
    intercepted_echo_rest, intercepted_echo_grpc, transport, response_metadata
):
    request_content = "The hail in Wales falls mainly on the snails."
    request_metadata = ("something1", "something_value1")
    if transport == "grpc":
        client, interceptor = intercepted_echo_grpc
    else:
        client, interceptor = intercepted_echo_rest
    response = client.echo(
        request=showcase.EchoRequest(content=request_content),
        metadata=(request_metadata,),
    )
    assert response.content == request_content
    assert request_metadata in interceptor.request_metadata
    assert response_metadata in interceptor.response_metadata


def test_metadata_response_rest_streams(intercepted_echo_rest):
    request_content = "The hail in Wales falls mainly on the snails."
    request_metadata = ("something2", "something_value2")
    response_metadata = ("X-Showcase-Request-Something2", "something_value2")
    client, interceptor = intercepted_echo_rest
    client.expand(
        {
            "content": request_content,
        },
        metadata=(request_metadata,),
    )

    assert request_metadata in interceptor.request_metadata
    assert response_metadata in interceptor.response_metadata


if os.environ.get("GAPIC_PYTHON_ASYNC", "true") == "true":

    @pytest.mark.asyncio
    async def test_metadata_response_grpc_unary_async(intercepted_echo_grpc_async):
        request_content = "The hail in Wales falls mainly on the snails."
        request_metadata = ("something3", "something_value3")
        response_metadata = ("something3", "something_value3")

        client, interceptor = intercepted_echo_grpc_async
        response = await client.echo(
            request=showcase.EchoRequest(content=request_content),
            metadata=(("something3", "something_value3"),),
        )
        assert response.content == request_content
        assert request_metadata in interceptor.request_metadata
        assert response_metadata in interceptor.response_metadata

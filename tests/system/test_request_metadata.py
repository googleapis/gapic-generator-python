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

import google.api_core
from google import showcase


def test_metadata_binary(echo):
    echo.echo(
        showcase.EchoRequest(
            content="The hail in Wales falls mainly on the snails.",
            request_id="some_value",
            other_request_id="",
        ),
        metadata=[('some-key-bin', b'some_value')]
    )

    if isinstance(echo.transport, type(echo).get_transport_class("grpc")):
        # See https://github.com/googleapis/gapic-generator-python/issues/2250
        # and https://github.com/grpc/grpc/pull/38127.
        # When the metadata key ends in `-bin`, the value should be of type
        # `bytes`` rather than `str``. Otherwise, gRPC raises a TypeError.
        with pytest.raises(TypeError, match="(?i)expected bytes"):
            echo.echo(
                showcase.EchoRequest(
                    content="The hail in Wales falls mainly on the snails.",
                    request_id="some_value",
                    other_request_id="",
                ),
                metadata=[('some-key-bin', 'some_value')]
            )


def test_metadata_rest_unary(intercepted_echo_rest):
    response = intercepted_echo_rest.echo(
        request = showcase.EchoRequest(
            content="The hail in Wales falls mainly on the snails."
        ),
        metadata=(("something", "something_value"),),
    )

    assert response.content == "The hail in Wales falls mainly on the snails."
    assert ("something", "something_value") in intercepted_echo_rest.transport._interceptor.request_metadata
    assert ("X-Showcase-Request-Something", "something_value") in intercepted_echo_rest.transport._interceptor.response_metadata


def test_metadata_grpc_unary(intercepted_echo_grpc):
    response = intercepted_echo_grpc.echo(
        request = showcase.EchoRequest(
            content="The hail in Wales falls mainly on the snails."
        ),
        metadata=(("something", "something_value"),),
    )

    assert response.content == "The hail in Wales falls mainly on the snails."

    assert ("something", "something_value") in intercepted_echo_grpc._transport.grpc_channel._interceptor._request_metadata
    assert ("something", "something_value") in intercepted_echo_grpc._transport.grpc_channel._interceptor._response_metadata

def test_metadata_rest_streams(intercepted_echo_rest):
    content = 'The hail in Wales falls mainly on the snails.'
    responses = intercepted_echo_rest.expand({
        'content': content,
    }, metadata=(("something2", "something_value2"),),)
    for ground_truth, response in zip(content.split(' '), responses):
        assert response.content == ground_truth
    assert ground_truth == 'snails.'

    print(responses)
    #assert responses.content == "The hail in Wales falls mainly on the snails."
    assert ("something2", "something_value2") in intercepted_echo_rest.transport._interceptor.request_metadata
    assert ("X-Showcase-Request-Something2", "something_value2") in intercepted_echo_rest.transport._interceptor.response_metadata

if os.environ.get("GAPIC_PYTHON_ASYNC", "true") == "true":
    @pytest.mark.asyncio
    async def test_metadata_rest_unary_async(intercepted_echo_rest_async):
        pytest.skip("TODO: Determine if this is ready for use")
        response = await intercepted_echo_rest_async.echo(
            request = showcase.EchoRequest(
                content="The hail in Wales falls mainly on the snails."
            ),
            metadata=(("something", "something_value"),),
        )

        assert response.content == "The hail in Wales falls mainly on the snails."
        assert ("something", "something_value") in intercepted_echo_rest_async.transport._interceptor.request_metadata
        assert ("X-Showcase-Request-Something", "something_value") in intercepted_echo_rest_async.transport._interceptor.response_metadata

    @pytest.mark.asyncio
    async def test_metadata_grpc_unary_async(intercepted_echo_grpc_async):
        response = await intercepted_echo_grpc_async.echo(
            request = showcase.EchoRequest(
                content="The hail in Wales falls mainly on the snails."
            ),
            metadata=(("something", "something_value"),),
        )

        assert response.content == "The hail in Wales falls mainly on the snails."
        
        assert ("something", "something_value") in intercepted_echo_grpc_async.transport.grpc_channel._unary_unary_interceptors[0]._request_metadata
        assert ("something", "something_value") in intercepted_echo_grpc_async.transport.grpc_channel._unary_unary_interceptors[0]._response_metadata

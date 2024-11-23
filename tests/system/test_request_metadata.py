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


def test_metadata(echo):
    api_core_major, api_core_minor = [
        int(part) for part in google.api_core.version.__version__.split(".")[0:2]
    ]
    if api_core_major < 2 or (api_core_major == 2 and api_core_minor < 14):
        pytest.skip(
            "Skip this test if we're on an older version of google-api-core which doesn't support `with_call`"
        )

    class MetadataCallback:
        trailing_metadata = None

        def get_raw_response_callback(self, response):
            if isinstance(echo.transport, type(echo).get_transport_class("grpc")):
                self.trailing_metadata = response.trailing_metadata()
            else:
                self.headers = response.headers

    metadata_callback = MetadataCallback()

    response = echo.echo(
        showcase.EchoRequest(
            content="The hail in Wales falls mainly on the snails."
        ),
        raw_response_callback=metadata_callback.get_raw_response_callback,
        metadata=(("something", "something_value"),),
    )

    assert response.content == "The hail in Wales falls mainly on the snails."
    if isinstance(echo.transport, type(echo).get_transport_class("grpc")):
        response_metadata = [
            (metadata.key, metadata.value)
            for metadata in metadata_callback.trailing_metadata
        ]
        assert ("something", "something_value") in response_metadata
    else:

        assert "X-Showcase-Request-Something" in metadata_callback.headers
        assert metadata_callback.headers["X-Showcase-Request-Something"] == "something_value"


if os.environ.get("GAPIC_PYTHON_ASYNC", "true") == "true":
    @pytest.mark.asyncio
    async def test_metadata_async(async_echo):
        api_core_major, api_core_minor = [
            int(part) for part in google.api_core.version.__version__.split(".")[0:2]
        ]
        if api_core_major < 2 or (api_core_major == 2 and api_core_minor < 24):
            pytest.skip(
                "Skip this test if we're on an older version of google-api-core which doesn't support async `with_call`"
            )

        class MetadataCallback:
            trailing_metadata = None

            async def get_raw_response_callback(self, response):
                if isinstance(async_echo.transport, type(async_echo).get_transport_class("grpc_asyncio")):
                    self.trailing_metadata = await response.trailing_metadata()
                else:
                    self.headers = response.headers

        metadata_callback = MetadataCallback()

        response = await async_echo.echo(
            showcase.EchoRequest(
                content="The hail in Wales falls mainly on the snails."
            ),
            raw_response_callback=metadata_callback.get_raw_response_callback,
            metadata=(("something", "something_value"),),
        )

        assert response.content == "The hail in Wales falls mainly on the snails."
        if isinstance(async_echo.transport, type(async_echo).get_transport_class("grpc_asyncio")):
            response_metadata = [
                (metadata.key, metadata.value)
                if hasattr(metadata, 'key')
                else metadata
                for metadata in metadata_callback.trailing_metadata
            ]
            assert ("something", "something_value") in response_metadata
        else:
            assert "X-Showcase-Request-Something" in metadata_callback.headers
            assert metadata_callback.headers["X-Showcase-Request-Something"] == "something_value"

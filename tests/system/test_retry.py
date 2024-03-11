# Copyright 2019 Google LLC
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

from google.api_core import exceptions
from google.rpc import code_pb2
from google.showcase_v1beta1.services.echo.transports import EchoRestInterceptor


def test_retry_bubble(echo):
    # Note: DeadlineExceeded is from gRPC, GatewayTimeout from http
    with pytest.raises((exceptions.DeadlineExceeded, exceptions.GatewayTimeout)):
        echo.echo({
            'error': {
                'code': code_pb2.Code.Value('DEADLINE_EXCEEDED'),
                'message': 'This took longer than you said it should.',
            },
        })

    if isinstance(echo.transport, type(echo).get_transport_class("grpc")):
        # Under gRPC, we raise exceptions.DeadlineExceeded, which is a
        # sub-class of exceptions.GatewayTimeout.
        with pytest.raises(exceptions.DeadlineExceeded):
            echo.echo({
                'error': {
                    'code': code_pb2.Code.Value('DEADLINE_EXCEEDED'),
                    'message': 'This took longer than you said it should.',
                },
            })

    # gapic-generator-python does not yet support gRPC interceptors
    # See <File bug>
    if isinstance(echo.transport, type(echo).get_transport_class("rest")):
        # Ensure that the same UUID is used when requests are retried
        class CustomEchoRestInterceptor(EchoRestInterceptor):
            def pre_echo(self, request, metadata):
                if not hasattr(self, "request_ids_sent"):
                    self.request_ids_sent = []
                self.request_ids_sent.append(request.request_id)
                return request, metadata
        test = CustomEchoRestInterceptor()
        echo.transport._interceptor.pre_echo = CustomEchoRestInterceptor()
        with pytest.raises(exceptions.RetryError):
            echo.echo({
                'error': {
                    'code': code_pb2.Code.Value('UNAVAILABLE'),
                    'message': 'This service is not available.',
                },
            })
        # Test that the request_ids are all the same for requests that have been retried
        print(echo.transport._interceptor.request_ids_sent)

        echo.transport._interceptor = EchoRestInterceptor()




if os.environ.get("GAPIC_PYTHON_ASYNC", "true") == "true":

    @pytest.mark.asyncio
    async def test_retry_bubble_async(async_echo):
        with pytest.raises(exceptions.RetryError):
            await async_echo.echo({
                'error': {
                    'code': code_pb2.Code.Value('UNAVAILABLE'),
                    'message': 'This service is not available.',
                },
            })

    # Note: This test verifies that:
    # Using gapic_v1.method.wrap_method in *AsyncClient raises a RPCError (Incorrect behaviour).
    # Using gapic_v1.method_async.wrap_method in *AsyncClient raises a google.api_core.exceptions.GoogleAPIError.

    @pytest.mark.asyncio
    async def test_method_async_wrapper_for_async_client(async_echo):
        with pytest.raises(exceptions.NotFound):
            await async_echo.get_operation({
                'name': "operations/echo"
            })

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

import google.auth
try:
    import aiohttp # type: ignore
    from google.auth.aio.transport.sessions import AsyncAuthorizedSession # type: ignore
except ImportError as e:  # pragma: NO COVER
    raise ImportError("async rest transport requires google-auth >= 2.35.0 with aiohttp extra. Install google-auth with the aiohttp extra using `pip install google-auth[aiohttp]==2.35.0`.") from e

from google.auth.aio import credentials as ga_credentials_async  # type: ignore

from google.api_core import exceptions as core_exceptions
from google.api_core import gapic_v1
from google.api_core import retry_async as retries
from google.api_core import rest_helpers
from google.api_core import rest_streaming_async  # type: ignore

try:
    from google.api_core import rest_streaming_async # type: ignore
    HAS_ASYNC_REST_SUPPORT_IN_CORE = True
except ImportError as e:  # pragma: NO COVER
    raise ImportError("async rest transport requires google-api-core >= 2.20.0. Install google-api-core using `pip install google-api-core==2.35.0`.") from e

from google.protobuf import json_format

import json  # type: ignore
import dataclasses
from typing import Any, Callable, Tuple, Optional, Sequence, Union


from google.showcase_v1beta1.types import echo as gs_echo
from google.longrunning import operations_pb2  # type: ignore


from .rest_base import _BaseEchoRestTransport

from .base import DEFAULT_CLIENT_INFO as BASE_DEFAULT_CLIENT_INFO

try:
    OptionalRetry = Union[retries.AsyncRetry, gapic_v1.method._MethodDefault, None]
except AttributeError:  # pragma: NO COVER
    OptionalRetry = Union[retries.AsyncRetry, object, None]  # type: ignore

DEFAULT_CLIENT_INFO = gapic_v1.client_info.ClientInfo(
    gapic_version=BASE_DEFAULT_CLIENT_INFO.gapic_version,
    grpc_version=None,
    rest_version=google.auth.__version__
)

@dataclasses.dataclass
class AsyncEchoRestStub:
    _session: AsyncAuthorizedSession
    _host: str

class AsyncEchoRestTransport(_BaseEchoRestTransport):
    """Asynchronous REST backend transport for Echo.

    This service is used showcase the four main types of rpcs -
    unary, server side streaming, client side streaming, and
    bidirectional streaming. This service also exposes methods that
    explicitly implement server delay, and paginated calls. Set the
    'showcase-trailer' metadata key on any method to have the values
    echoed in the response trailers. Set the 'x-goog-request-params'
    metadata key on any method to have the values echoed in the
    response headers.

    This class defines the same methods as the primary client, so the
    primary client can load the underlying transport implementation
    and call it.

    It sends JSON representations of protocol buffers over HTTP/1.1
    """
    def __init__(self,
            *,
            host: str = 'localhost:7469',
            credentials: Optional[ga_credentials_async.Credentials] = None,
            client_info: gapic_v1.client_info.ClientInfo = DEFAULT_CLIENT_INFO,
            url_scheme: str = 'https',
            ) -> None:
        """Instantiate the transport.

       NOTE: This async REST transport functionality is currently in a beta
       state (preview). We welcome your feedback via a GitHub issue in
       this library's repository. Thank you!

        Args:
            host (Optional[str]):
                 The hostname to connect to (default: 'localhost:7469').
            credentials (Optional[google.auth.aio.credentials.Credentials]): The
                authorization credentials to attach to requests. These
                credentials identify the application to the service; if none
                are specified, the client will attempt to ascertain the
                credentials from the environment.
            client_info (google.api_core.gapic_v1.client_info.ClientInfo):
                The client info used to send a user-agent string along with
                API requests. If ``None``, then default info will be used.
                Generally, you only need to set this if you are developing
                your own client library.
            url_scheme (str): the protocol scheme for the API endpoint.  Normally
                "https", but for testing or local servers,
                "http" can be specified.
        """
        # Run the base constructor
        super().__init__(
            host=host,
            credentials=credentials,
            client_info=client_info,
            always_use_jwt_access=False,
            url_scheme=url_scheme,
            api_audience=None
        )
        self._session = AsyncAuthorizedSession(self._credentials)  # type: ignore
        self._wrap_with_kind = True
        self._prep_wrapped_messages(client_info)

    def _prep_wrapped_messages(self, client_info):
        """ Precompute the wrapped methods, overriding the base class method to use async wrappers."""
        self._wrapped_methods = {
            self.echo: self._wrap_method(
                self.echo,
                default_retry=retries.AsyncRetry(
                    initial=0.1,
                    maximum=3.0,
                    multiplier=2,
                    predicate=retries.if_exception_type(
                        core_exceptions.ServiceUnavailable,
                        core_exceptions.Unknown,
                    ),
                    deadline=10.0,
                ),
                default_timeout=10.0,
                client_info=client_info,
            ),
            self.echo_error_details: self._wrap_method(
                self.echo_error_details,
                default_timeout=None,
                client_info=client_info,
            ),
            self.expand: self._wrap_method(
                self.expand,
                default_retry=retries.AsyncRetry(
                    initial=0.1,
                    maximum=3.0,
                    multiplier=2,
                    predicate=retries.if_exception_type(
                        core_exceptions.ServiceUnavailable,
                        core_exceptions.Unknown,
                    ),
                    deadline=10.0,
                ),
                default_timeout=10.0,
                client_info=client_info,
            ),
            self.collect: self._wrap_method(
                self.collect,
                default_timeout=None,
                client_info=client_info,
            ),
            self.chat: self._wrap_method(
                self.chat,
                default_timeout=None,
                client_info=client_info,
            ),
            self.paged_expand: self._wrap_method(
                self.paged_expand,
                default_retry=retries.AsyncRetry(
                    initial=0.1,
                    maximum=3.0,
                    multiplier=2,
                    predicate=retries.if_exception_type(
                        core_exceptions.ServiceUnavailable,
                        core_exceptions.Unknown,
                    ),
                    deadline=10.0,
                ),
                default_timeout=10.0,
                client_info=client_info,
            ),
            self.paged_expand_legacy: self._wrap_method(
                self.paged_expand_legacy,
                default_timeout=None,
                client_info=client_info,
            ),
            self.paged_expand_legacy_mapped: self._wrap_method(
                self.paged_expand_legacy_mapped,
                default_timeout=None,
                client_info=client_info,
            ),
            self.wait: self._wrap_method(
                self.wait,
                default_timeout=None,
                client_info=client_info,
            ),
            self.block: self._wrap_method(
                self.block,
                default_timeout=None,
                client_info=client_info,
            ),
        }

    def _wrap_method(self, func, *args, **kwargs):
        if self._wrap_with_kind:  # pragma: NO COVER
            kwargs["kind"] = self.kind
        return gapic_v1.method_async.wrap_method(func, *args, **kwargs)

    class _Block(_BaseEchoRestTransport._BaseBlock, AsyncEchoRestStub):
        def __hash__(self):
            return hash("AsyncEchoRestTransport.Block")

        @staticmethod
        async def _get_response(
            host,
            metadata,
            query_params,
            session,
            timeout,
            transcoded_request,
            body=None):

            uri = transcoded_request['uri']
            method = transcoded_request['method']
            headers = dict(metadata)
            headers['Content-Type'] = 'application/json'
            response = await getattr(session, method)(
                "{host}{uri}".format(host=host, uri=uri),
                timeout=timeout,
                headers=headers,
                params=rest_helpers.flatten_query_params(query_params, strict=True),
                data=body,
                )
            return response

        async def __call__(self,
                    request: gs_echo.BlockRequest, *,
                    retry: OptionalRetry=gapic_v1.method.DEFAULT,
                    timeout: Optional[float]=None,
                    metadata: Sequence[Tuple[str, str]]=(),
                    ) -> gs_echo.BlockResponse:
            r"""Call the block method over HTTP.

            Args:
                request (~.gs_echo.BlockRequest):
                    The request object. The request for Block method.
                retry (google.api_core.retry_async.AsyncRetry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, str]]): Strings which should be
                    sent along with the request as metadata.

            Returns:
                ~.gs_echo.BlockResponse:
                    The response for Block method.
            """

            http_options = _BaseEchoRestTransport._BaseBlock._get_http_options()
            transcoded_request = _BaseEchoRestTransport._BaseBlock._get_transcoded_request(http_options, request)

            body = _BaseEchoRestTransport._BaseBlock._get_request_body_json(transcoded_request)

            # Jsonify the query params
            query_params = _BaseEchoRestTransport._BaseBlock._get_query_params_json(transcoded_request)

            # Send the request
            response = await AsyncEchoRestTransport._Block._get_response(self._host, metadata, query_params, self._session, timeout, transcoded_request, body)

            # In case of error, raise the appropriate core_exceptions.GoogleAPICallError exception
            # subclass.
            if response.status_code >= 400:
                content = await response.read()
                payload = json.loads(content.decode('utf-8'))
                request_url = "{host}{uri}".format(host=self._host, uri=transcoded_request['uri'])
                method = transcoded_request['method']
                raise core_exceptions.format_http_response_error(response, method, request_url, payload)  # type: ignore

            # Return the response
            resp = gs_echo.BlockResponse()
            pb_resp = gs_echo.BlockResponse.pb(resp)
            content = await response.read()
            json_format.Parse(content, pb_resp, ignore_unknown_fields=True)
            return resp

    class _Chat(_BaseEchoRestTransport._BaseChat, AsyncEchoRestStub):
        def __hash__(self):
            return hash("AsyncEchoRestTransport.Chat")

        async def __call__(self,
                    request: gs_echo.EchoRequest, *,
                    retry: OptionalRetry=gapic_v1.method.DEFAULT,
                    timeout: Optional[float]=None,
                    metadata: Sequence[Tuple[str, str]]=(),
                    ) -> rest_streaming_async.AsyncResponseIterator:
                raise NotImplementedError(
                    "Method Chat is not available over REST transport"
                )

    class _Collect(_BaseEchoRestTransport._BaseCollect, AsyncEchoRestStub):
        def __hash__(self):
            return hash("AsyncEchoRestTransport.Collect")

        async def __call__(self,
                    request: gs_echo.EchoRequest, *,
                    retry: OptionalRetry=gapic_v1.method.DEFAULT,
                    timeout: Optional[float]=None,
                    metadata: Sequence[Tuple[str, str]]=(),
                    ) -> gs_echo.EchoResponse:
                raise NotImplementedError(
                    "Method Collect is not available over REST transport"
                )

    class _Echo(_BaseEchoRestTransport._BaseEcho, AsyncEchoRestStub):
        def __hash__(self):
            return hash("AsyncEchoRestTransport.Echo")

        @staticmethod
        async def _get_response(
            host,
            metadata,
            query_params,
            session,
            timeout,
            transcoded_request,
            body=None):

            uri = transcoded_request['uri']
            method = transcoded_request['method']
            headers = dict(metadata)
            headers['Content-Type'] = 'application/json'
            response = await getattr(session, method)(
                "{host}{uri}".format(host=host, uri=uri),
                timeout=timeout,
                headers=headers,
                params=rest_helpers.flatten_query_params(query_params, strict=True),
                data=body,
                )
            return response

        async def __call__(self,
                    request: gs_echo.EchoRequest, *,
                    retry: OptionalRetry=gapic_v1.method.DEFAULT,
                    timeout: Optional[float]=None,
                    metadata: Sequence[Tuple[str, str]]=(),
                    ) -> gs_echo.EchoResponse:
            r"""Call the echo method over HTTP.

            Args:
                request (~.gs_echo.EchoRequest):
                    The request object. The request message used for the
                Echo, Collect and Chat methods. If
                content or opt are set in this message
                then the request will succeed. If status
                is set in this message then the status
                will be returned as an error.
                retry (google.api_core.retry_async.AsyncRetry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, str]]): Strings which should be
                    sent along with the request as metadata.

            Returns:
                ~.gs_echo.EchoResponse:
                    The response message for the Echo
                methods.

            """

            http_options = _BaseEchoRestTransport._BaseEcho._get_http_options()
            transcoded_request = _BaseEchoRestTransport._BaseEcho._get_transcoded_request(http_options, request)

            body = _BaseEchoRestTransport._BaseEcho._get_request_body_json(transcoded_request)

            # Jsonify the query params
            query_params = _BaseEchoRestTransport._BaseEcho._get_query_params_json(transcoded_request)

            # Send the request
            response = await AsyncEchoRestTransport._Echo._get_response(self._host, metadata, query_params, self._session, timeout, transcoded_request, body)

            # In case of error, raise the appropriate core_exceptions.GoogleAPICallError exception
            # subclass.
            if response.status_code >= 400:
                content = await response.read()
                payload = json.loads(content.decode('utf-8'))
                request_url = "{host}{uri}".format(host=self._host, uri=transcoded_request['uri'])
                method = transcoded_request['method']
                raise core_exceptions.format_http_response_error(response, method, request_url, payload)  # type: ignore

            # Return the response
            resp = gs_echo.EchoResponse()
            pb_resp = gs_echo.EchoResponse.pb(resp)
            content = await response.read()
            json_format.Parse(content, pb_resp, ignore_unknown_fields=True)
            return resp

    class _EchoErrorDetails(_BaseEchoRestTransport._BaseEchoErrorDetails, AsyncEchoRestStub):
        def __hash__(self):
            return hash("AsyncEchoRestTransport.EchoErrorDetails")

        @staticmethod
        async def _get_response(
            host,
            metadata,
            query_params,
            session,
            timeout,
            transcoded_request,
            body=None):

            uri = transcoded_request['uri']
            method = transcoded_request['method']
            headers = dict(metadata)
            headers['Content-Type'] = 'application/json'
            response = await getattr(session, method)(
                "{host}{uri}".format(host=host, uri=uri),
                timeout=timeout,
                headers=headers,
                params=rest_helpers.flatten_query_params(query_params, strict=True),
                data=body,
                )
            return response

        async def __call__(self,
                    request: gs_echo.EchoErrorDetailsRequest, *,
                    retry: OptionalRetry=gapic_v1.method.DEFAULT,
                    timeout: Optional[float]=None,
                    metadata: Sequence[Tuple[str, str]]=(),
                    ) -> gs_echo.EchoErrorDetailsResponse:
            r"""Call the echo error details method over HTTP.

            Args:
                request (~.gs_echo.EchoErrorDetailsRequest):
                    The request object. The request message used for the
                EchoErrorDetails method.
                retry (google.api_core.retry_async.AsyncRetry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, str]]): Strings which should be
                    sent along with the request as metadata.

            Returns:
                ~.gs_echo.EchoErrorDetailsResponse:
                    The response message used for the
                EchoErrorDetails method.

            """

            http_options = _BaseEchoRestTransport._BaseEchoErrorDetails._get_http_options()
            transcoded_request = _BaseEchoRestTransport._BaseEchoErrorDetails._get_transcoded_request(http_options, request)

            body = _BaseEchoRestTransport._BaseEchoErrorDetails._get_request_body_json(transcoded_request)

            # Jsonify the query params
            query_params = _BaseEchoRestTransport._BaseEchoErrorDetails._get_query_params_json(transcoded_request)

            # Send the request
            response = await AsyncEchoRestTransport._EchoErrorDetails._get_response(self._host, metadata, query_params, self._session, timeout, transcoded_request, body)

            # In case of error, raise the appropriate core_exceptions.GoogleAPICallError exception
            # subclass.
            if response.status_code >= 400:
                content = await response.read()
                payload = json.loads(content.decode('utf-8'))
                request_url = "{host}{uri}".format(host=self._host, uri=transcoded_request['uri'])
                method = transcoded_request['method']
                raise core_exceptions.format_http_response_error(response, method, request_url, payload)  # type: ignore

            # Return the response
            resp = gs_echo.EchoErrorDetailsResponse()
            pb_resp = gs_echo.EchoErrorDetailsResponse.pb(resp)
            content = await response.read()
            json_format.Parse(content, pb_resp, ignore_unknown_fields=True)
            return resp

    class _Expand(_BaseEchoRestTransport._BaseExpand, AsyncEchoRestStub):
        def __hash__(self):
            return hash("AsyncEchoRestTransport.Expand")

        @staticmethod
        async def _get_response(
            host,
            metadata,
            query_params,
            session,
            timeout,
            transcoded_request,
            body=None):

            uri = transcoded_request['uri']
            method = transcoded_request['method']
            headers = dict(metadata)
            headers['Content-Type'] = 'application/json'
            response = await getattr(session, method)(
                "{host}{uri}".format(host=host, uri=uri),
                timeout=timeout,
                headers=headers,
                params=rest_helpers.flatten_query_params(query_params, strict=True),
                data=body,
                )
            return response

        async def __call__(self,
                    request: gs_echo.ExpandRequest, *,
                    retry: OptionalRetry=gapic_v1.method.DEFAULT,
                    timeout: Optional[float]=None,
                    metadata: Sequence[Tuple[str, str]]=(),
                    ) -> rest_streaming_async.AsyncResponseIterator:
            r"""Call the expand method over HTTP.

            Args:
                request (~.gs_echo.ExpandRequest):
                    The request object. The request message for the Expand
                method.
                retry (google.api_core.retry_async.AsyncRetry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, str]]): Strings which should be
                    sent along with the request as metadata.

            Returns:
                ~.gs_echo.EchoResponse:
                    The response message for the Echo
                methods.

            """

            http_options = _BaseEchoRestTransport._BaseExpand._get_http_options()
            transcoded_request = _BaseEchoRestTransport._BaseExpand._get_transcoded_request(http_options, request)

            body = _BaseEchoRestTransport._BaseExpand._get_request_body_json(transcoded_request)

            # Jsonify the query params
            query_params = _BaseEchoRestTransport._BaseExpand._get_query_params_json(transcoded_request)

            # Send the request
            response = await AsyncEchoRestTransport._Expand._get_response(self._host, metadata, query_params, self._session, timeout, transcoded_request, body)

            # In case of error, raise the appropriate core_exceptions.GoogleAPICallError exception
            # subclass.
            if response.status_code >= 400:
                content = await response.read()
                payload = json.loads(content.decode('utf-8'))
                request_url = "{host}{uri}".format(host=self._host, uri=transcoded_request['uri'])
                method = transcoded_request['method']
                raise core_exceptions.format_http_response_error(response, method, request_url, payload)  # type: ignore

            # Return the response
            resp = rest_streaming_async.AsyncResponseIterator(response, gs_echo.EchoResponse)
            return resp

    class _PagedExpand(_BaseEchoRestTransport._BasePagedExpand, AsyncEchoRestStub):
        def __hash__(self):
            return hash("AsyncEchoRestTransport.PagedExpand")

        async def __call__(self,
                    request: gs_echo.PagedExpandRequest, *,
                    retry: OptionalRetry=gapic_v1.method.DEFAULT,
                    timeout: Optional[float]=None,
                    metadata: Sequence[Tuple[str, str]]=(),
                    ) -> gs_echo.PagedExpandResponse:
                raise NotImplementedError(
                    "Method PagedExpand is not available over REST transport"
                )

    class _PagedExpandLegacy(_BaseEchoRestTransport._BasePagedExpandLegacy, AsyncEchoRestStub):
        def __hash__(self):
            return hash("AsyncEchoRestTransport.PagedExpandLegacy")

        async def __call__(self,
                    request: gs_echo.PagedExpandLegacyRequest, *,
                    retry: OptionalRetry=gapic_v1.method.DEFAULT,
                    timeout: Optional[float]=None,
                    metadata: Sequence[Tuple[str, str]]=(),
                    ) -> gs_echo.PagedExpandResponse:
                raise NotImplementedError(
                    "Method PagedExpandLegacy is not available over REST transport"
                )

    class _PagedExpandLegacyMapped(_BaseEchoRestTransport._BasePagedExpandLegacyMapped, AsyncEchoRestStub):
        def __hash__(self):
            return hash("AsyncEchoRestTransport.PagedExpandLegacyMapped")

        async def __call__(self,
                    request: gs_echo.PagedExpandRequest, *,
                    retry: OptionalRetry=gapic_v1.method.DEFAULT,
                    timeout: Optional[float]=None,
                    metadata: Sequence[Tuple[str, str]]=(),
                    ) -> gs_echo.PagedExpandLegacyMappedResponse:
                raise NotImplementedError(
                    "Method PagedExpandLegacyMapped is not available over REST transport"
                )

    class _Wait(_BaseEchoRestTransport._BaseWait, AsyncEchoRestStub):
        def __hash__(self):
            return hash("AsyncEchoRestTransport.Wait")

        async def __call__(self,
                    request: gs_echo.WaitRequest, *,
                    retry: OptionalRetry=gapic_v1.method.DEFAULT,
                    timeout: Optional[float]=None,
                    metadata: Sequence[Tuple[str, str]]=(),
                    ) -> operations_pb2.Operation:
                raise NotImplementedError(
                    "Method Wait is not available over REST transport"
                )

    @property
    def block(self) -> Callable[
            [gs_echo.BlockRequest],
            gs_echo.BlockResponse]:
        return self._Block(self._session, self._host)  # type: ignore

    @property
    def chat(self) -> Callable[
            [gs_echo.EchoRequest],
            gs_echo.EchoResponse]:
        return self._Chat(self._session, self._host)  # type: ignore

    @property
    def collect(self) -> Callable[
            [gs_echo.EchoRequest],
            gs_echo.EchoResponse]:
        return self._Collect(self._session, self._host)  # type: ignore

    @property
    def echo(self) -> Callable[
            [gs_echo.EchoRequest],
            gs_echo.EchoResponse]:
        return self._Echo(self._session, self._host)  # type: ignore

    @property
    def echo_error_details(self) -> Callable[
            [gs_echo.EchoErrorDetailsRequest],
            gs_echo.EchoErrorDetailsResponse]:
        return self._EchoErrorDetails(self._session, self._host)  # type: ignore

    @property
    def expand(self) -> Callable[
            [gs_echo.ExpandRequest],
            gs_echo.EchoResponse]:
        return self._Expand(self._session, self._host)  # type: ignore

    @property
    def paged_expand(self) -> Callable[
            [gs_echo.PagedExpandRequest],
            gs_echo.PagedExpandResponse]:
        return self._PagedExpand(self._session, self._host)  # type: ignore

    @property
    def paged_expand_legacy(self) -> Callable[
            [gs_echo.PagedExpandLegacyRequest],
            gs_echo.PagedExpandResponse]:
        return self._PagedExpandLegacy(self._session, self._host)  # type: ignore

    @property
    def paged_expand_legacy_mapped(self) -> Callable[
            [gs_echo.PagedExpandRequest],
            gs_echo.PagedExpandLegacyMappedResponse]:
        return self._PagedExpandLegacyMapped(self._session, self._host)  # type: ignore

    @property
    def wait(self) -> Callable[
            [gs_echo.WaitRequest],
            operations_pb2.Operation]:
        return self._Wait(self._session, self._host)  # type: ignore

    @property
    def kind(self) -> str:
        return "rest_asyncio"

    async def close(self):
        await self._session.close()

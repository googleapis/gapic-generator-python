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


from google.protobuf import empty_pb2  # type: ignore
from google.showcase_v1beta1.types import sequence
from google.showcase_v1beta1.types import sequence as gs_sequence
from google.longrunning import operations_pb2  # type: ignore


from .rest_base import _BaseSequenceServiceRestTransport

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
class AsyncSequenceServiceRestStub:
    _session: AsyncAuthorizedSession
    _host: str

class AsyncSequenceServiceRestTransport(_BaseSequenceServiceRestTransport):
    """Asynchronous REST backend transport for SequenceService.

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
            self.create_sequence: self._wrap_method(
                self.create_sequence,
                default_timeout=None,
                client_info=client_info,
            ),
            self.create_streaming_sequence: self._wrap_method(
                self.create_streaming_sequence,
                default_timeout=None,
                client_info=client_info,
            ),
            self.get_sequence_report: self._wrap_method(
                self.get_sequence_report,
                default_timeout=None,
                client_info=client_info,
            ),
            self.get_streaming_sequence_report: self._wrap_method(
                self.get_streaming_sequence_report,
                default_timeout=None,
                client_info=client_info,
            ),
            self.attempt_sequence: self._wrap_method(
                self.attempt_sequence,
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
            self.attempt_streaming_sequence: self._wrap_method(
                self.attempt_streaming_sequence,
                default_timeout=None,
                client_info=client_info,
            ),
        }

    def _wrap_method(self, func, *args, **kwargs):
        if self._wrap_with_kind:  # pragma: NO COVER
            kwargs["kind"] = self.kind
        return gapic_v1.method_async.wrap_method(func, *args, **kwargs)

    class _AttemptSequence(_BaseSequenceServiceRestTransport._BaseAttemptSequence, AsyncSequenceServiceRestStub):
        def __hash__(self):
            return hash("AsyncSequenceServiceRestTransport.AttemptSequence")

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
                    request: sequence.AttemptSequenceRequest, *,
                    retry: OptionalRetry=gapic_v1.method.DEFAULT,
                    timeout: Optional[float]=None,
                    metadata: Sequence[Tuple[str, str]]=(),
                    ):
            r"""Call the attempt sequence method over HTTP.

            Args:
                request (~.sequence.AttemptSequenceRequest):
                    The request object.
                retry (google.api_core.retry_async.AsyncRetry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, str]]): Strings which should be
                    sent along with the request as metadata.
            """

            http_options = _BaseSequenceServiceRestTransport._BaseAttemptSequence._get_http_options()
            transcoded_request = _BaseSequenceServiceRestTransport._BaseAttemptSequence._get_transcoded_request(http_options, request)

            body = _BaseSequenceServiceRestTransport._BaseAttemptSequence._get_request_body_json(transcoded_request)

            # Jsonify the query params
            query_params = _BaseSequenceServiceRestTransport._BaseAttemptSequence._get_query_params_json(transcoded_request)

            # Send the request
            response = await AsyncSequenceServiceRestTransport._AttemptSequence._get_response(self._host, metadata, query_params, self._session, timeout, transcoded_request, body)

            # In case of error, raise the appropriate core_exceptions.GoogleAPICallError exception
            # subclass.
            if response.status_code >= 400:
                content = await response.read()
                payload = json.loads(content.decode('utf-8'))
                request_url = "{host}{uri}".format(host=self._host, uri=transcoded_request['uri'])
                method = transcoded_request['method']
                raise core_exceptions.format_http_response_error(response, method, request_url, payload)  # type: ignore

    class _AttemptStreamingSequence(_BaseSequenceServiceRestTransport._BaseAttemptStreamingSequence, AsyncSequenceServiceRestStub):
        def __hash__(self):
            return hash("AsyncSequenceServiceRestTransport.AttemptStreamingSequence")

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
                    request: sequence.AttemptStreamingSequenceRequest, *,
                    retry: OptionalRetry=gapic_v1.method.DEFAULT,
                    timeout: Optional[float]=None,
                    metadata: Sequence[Tuple[str, str]]=(),
                    ) -> rest_streaming_async.AsyncResponseIterator:
            r"""Call the attempt streaming
        sequence method over HTTP.

            Args:
                request (~.sequence.AttemptStreamingSequenceRequest):
                    The request object.
                retry (google.api_core.retry_async.AsyncRetry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, str]]): Strings which should be
                    sent along with the request as metadata.

            Returns:
                ~.sequence.AttemptStreamingSequenceResponse:
                    The response message for the Echo
                methods.

            """

            http_options = _BaseSequenceServiceRestTransport._BaseAttemptStreamingSequence._get_http_options()
            transcoded_request = _BaseSequenceServiceRestTransport._BaseAttemptStreamingSequence._get_transcoded_request(http_options, request)

            body = _BaseSequenceServiceRestTransport._BaseAttemptStreamingSequence._get_request_body_json(transcoded_request)

            # Jsonify the query params
            query_params = _BaseSequenceServiceRestTransport._BaseAttemptStreamingSequence._get_query_params_json(transcoded_request)

            # Send the request
            response = await AsyncSequenceServiceRestTransport._AttemptStreamingSequence._get_response(self._host, metadata, query_params, self._session, timeout, transcoded_request, body)

            # In case of error, raise the appropriate core_exceptions.GoogleAPICallError exception
            # subclass.
            if response.status_code >= 400:
                content = await response.read()
                payload = json.loads(content.decode('utf-8'))
                request_url = "{host}{uri}".format(host=self._host, uri=transcoded_request['uri'])
                method = transcoded_request['method']
                raise core_exceptions.format_http_response_error(response, method, request_url, payload)  # type: ignore

            # Return the response
            resp = rest_streaming_async.AsyncResponseIterator(response, sequence.AttemptStreamingSequenceResponse)
            return resp

    class _CreateSequence(_BaseSequenceServiceRestTransport._BaseCreateSequence, AsyncSequenceServiceRestStub):
        def __hash__(self):
            return hash("AsyncSequenceServiceRestTransport.CreateSequence")

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
                    request: gs_sequence.CreateSequenceRequest, *,
                    retry: OptionalRetry=gapic_v1.method.DEFAULT,
                    timeout: Optional[float]=None,
                    metadata: Sequence[Tuple[str, str]]=(),
                    ) -> gs_sequence.Sequence:
            r"""Call the create sequence method over HTTP.

            Args:
                request (~.gs_sequence.CreateSequenceRequest):
                    The request object.
                retry (google.api_core.retry_async.AsyncRetry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, str]]): Strings which should be
                    sent along with the request as metadata.

            Returns:
                ~.gs_sequence.Sequence:

            """

            http_options = _BaseSequenceServiceRestTransport._BaseCreateSequence._get_http_options()
            transcoded_request = _BaseSequenceServiceRestTransport._BaseCreateSequence._get_transcoded_request(http_options, request)

            body = _BaseSequenceServiceRestTransport._BaseCreateSequence._get_request_body_json(transcoded_request)

            # Jsonify the query params
            query_params = _BaseSequenceServiceRestTransport._BaseCreateSequence._get_query_params_json(transcoded_request)

            # Send the request
            response = await AsyncSequenceServiceRestTransport._CreateSequence._get_response(self._host, metadata, query_params, self._session, timeout, transcoded_request, body)

            # In case of error, raise the appropriate core_exceptions.GoogleAPICallError exception
            # subclass.
            if response.status_code >= 400:
                content = await response.read()
                payload = json.loads(content.decode('utf-8'))
                request_url = "{host}{uri}".format(host=self._host, uri=transcoded_request['uri'])
                method = transcoded_request['method']
                raise core_exceptions.format_http_response_error(response, method, request_url, payload)  # type: ignore

            # Return the response
            resp = gs_sequence.Sequence()
            pb_resp = gs_sequence.Sequence.pb(resp)
            content = await response.read()
            json_format.Parse(content, pb_resp, ignore_unknown_fields=True)
            return resp

    class _CreateStreamingSequence(_BaseSequenceServiceRestTransport._BaseCreateStreamingSequence, AsyncSequenceServiceRestStub):
        def __hash__(self):
            return hash("AsyncSequenceServiceRestTransport.CreateStreamingSequence")

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
                    request: sequence.CreateStreamingSequenceRequest, *,
                    retry: OptionalRetry=gapic_v1.method.DEFAULT,
                    timeout: Optional[float]=None,
                    metadata: Sequence[Tuple[str, str]]=(),
                    ) -> sequence.StreamingSequence:
            r"""Call the create streaming sequence method over HTTP.

            Args:
                request (~.sequence.CreateStreamingSequenceRequest):
                    The request object.
                retry (google.api_core.retry_async.AsyncRetry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, str]]): Strings which should be
                    sent along with the request as metadata.

            Returns:
                ~.sequence.StreamingSequence:

            """

            http_options = _BaseSequenceServiceRestTransport._BaseCreateStreamingSequence._get_http_options()
            transcoded_request = _BaseSequenceServiceRestTransport._BaseCreateStreamingSequence._get_transcoded_request(http_options, request)

            body = _BaseSequenceServiceRestTransport._BaseCreateStreamingSequence._get_request_body_json(transcoded_request)

            # Jsonify the query params
            query_params = _BaseSequenceServiceRestTransport._BaseCreateStreamingSequence._get_query_params_json(transcoded_request)

            # Send the request
            response = await AsyncSequenceServiceRestTransport._CreateStreamingSequence._get_response(self._host, metadata, query_params, self._session, timeout, transcoded_request, body)

            # In case of error, raise the appropriate core_exceptions.GoogleAPICallError exception
            # subclass.
            if response.status_code >= 400:
                content = await response.read()
                payload = json.loads(content.decode('utf-8'))
                request_url = "{host}{uri}".format(host=self._host, uri=transcoded_request['uri'])
                method = transcoded_request['method']
                raise core_exceptions.format_http_response_error(response, method, request_url, payload)  # type: ignore

            # Return the response
            resp = sequence.StreamingSequence()
            pb_resp = sequence.StreamingSequence.pb(resp)
            content = await response.read()
            json_format.Parse(content, pb_resp, ignore_unknown_fields=True)
            return resp

    class _GetSequenceReport(_BaseSequenceServiceRestTransport._BaseGetSequenceReport, AsyncSequenceServiceRestStub):
        def __hash__(self):
            return hash("AsyncSequenceServiceRestTransport.GetSequenceReport")

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
                )
            return response

        async def __call__(self,
                    request: sequence.GetSequenceReportRequest, *,
                    retry: OptionalRetry=gapic_v1.method.DEFAULT,
                    timeout: Optional[float]=None,
                    metadata: Sequence[Tuple[str, str]]=(),
                    ) -> sequence.SequenceReport:
            r"""Call the get sequence report method over HTTP.

            Args:
                request (~.sequence.GetSequenceReportRequest):
                    The request object.
                retry (google.api_core.retry_async.AsyncRetry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, str]]): Strings which should be
                    sent along with the request as metadata.

            Returns:
                ~.sequence.SequenceReport:

            """

            http_options = _BaseSequenceServiceRestTransport._BaseGetSequenceReport._get_http_options()
            transcoded_request = _BaseSequenceServiceRestTransport._BaseGetSequenceReport._get_transcoded_request(http_options, request)

            # Jsonify the query params
            query_params = _BaseSequenceServiceRestTransport._BaseGetSequenceReport._get_query_params_json(transcoded_request)

            # Send the request
            response = await AsyncSequenceServiceRestTransport._GetSequenceReport._get_response(self._host, metadata, query_params, self._session, timeout, transcoded_request)

            # In case of error, raise the appropriate core_exceptions.GoogleAPICallError exception
            # subclass.
            if response.status_code >= 400:
                content = await response.read()
                payload = json.loads(content.decode('utf-8'))
                request_url = "{host}{uri}".format(host=self._host, uri=transcoded_request['uri'])
                method = transcoded_request['method']
                raise core_exceptions.format_http_response_error(response, method, request_url, payload)  # type: ignore

            # Return the response
            resp = sequence.SequenceReport()
            pb_resp = sequence.SequenceReport.pb(resp)
            content = await response.read()
            json_format.Parse(content, pb_resp, ignore_unknown_fields=True)
            return resp

    class _GetStreamingSequenceReport(_BaseSequenceServiceRestTransport._BaseGetStreamingSequenceReport, AsyncSequenceServiceRestStub):
        def __hash__(self):
            return hash("AsyncSequenceServiceRestTransport.GetStreamingSequenceReport")

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
                )
            return response

        async def __call__(self,
                    request: sequence.GetStreamingSequenceReportRequest, *,
                    retry: OptionalRetry=gapic_v1.method.DEFAULT,
                    timeout: Optional[float]=None,
                    metadata: Sequence[Tuple[str, str]]=(),
                    ) -> sequence.StreamingSequenceReport:
            r"""Call the get streaming sequence
        report method over HTTP.

            Args:
                request (~.sequence.GetStreamingSequenceReportRequest):
                    The request object.
                retry (google.api_core.retry_async.AsyncRetry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, str]]): Strings which should be
                    sent along with the request as metadata.

            Returns:
                ~.sequence.StreamingSequenceReport:

            """

            http_options = _BaseSequenceServiceRestTransport._BaseGetStreamingSequenceReport._get_http_options()
            transcoded_request = _BaseSequenceServiceRestTransport._BaseGetStreamingSequenceReport._get_transcoded_request(http_options, request)

            # Jsonify the query params
            query_params = _BaseSequenceServiceRestTransport._BaseGetStreamingSequenceReport._get_query_params_json(transcoded_request)

            # Send the request
            response = await AsyncSequenceServiceRestTransport._GetStreamingSequenceReport._get_response(self._host, metadata, query_params, self._session, timeout, transcoded_request)

            # In case of error, raise the appropriate core_exceptions.GoogleAPICallError exception
            # subclass.
            if response.status_code >= 400:
                content = await response.read()
                payload = json.loads(content.decode('utf-8'))
                request_url = "{host}{uri}".format(host=self._host, uri=transcoded_request['uri'])
                method = transcoded_request['method']
                raise core_exceptions.format_http_response_error(response, method, request_url, payload)  # type: ignore

            # Return the response
            resp = sequence.StreamingSequenceReport()
            pb_resp = sequence.StreamingSequenceReport.pb(resp)
            content = await response.read()
            json_format.Parse(content, pb_resp, ignore_unknown_fields=True)
            return resp

    @property
    def attempt_sequence(self) -> Callable[
            [sequence.AttemptSequenceRequest],
            empty_pb2.Empty]:
        return self._AttemptSequence(self._session, self._host)  # type: ignore

    @property
    def attempt_streaming_sequence(self) -> Callable[
            [sequence.AttemptStreamingSequenceRequest],
            sequence.AttemptStreamingSequenceResponse]:
        return self._AttemptStreamingSequence(self._session, self._host)  # type: ignore

    @property
    def create_sequence(self) -> Callable[
            [gs_sequence.CreateSequenceRequest],
            gs_sequence.Sequence]:
        return self._CreateSequence(self._session, self._host)  # type: ignore

    @property
    def create_streaming_sequence(self) -> Callable[
            [sequence.CreateStreamingSequenceRequest],
            sequence.StreamingSequence]:
        return self._CreateStreamingSequence(self._session, self._host)  # type: ignore

    @property
    def get_sequence_report(self) -> Callable[
            [sequence.GetSequenceReportRequest],
            sequence.SequenceReport]:
        return self._GetSequenceReport(self._session, self._host)  # type: ignore

    @property
    def get_streaming_sequence_report(self) -> Callable[
            [sequence.GetStreamingSequenceReportRequest],
            sequence.StreamingSequenceReport]:
        return self._GetStreamingSequenceReport(self._session, self._host)  # type: ignore

    @property
    def kind(self) -> str:
        return "rest_asyncio"

    async def close(self):
        await self._session.close()

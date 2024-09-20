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
from google.showcase_v1beta1.types import testing
from google.longrunning import operations_pb2  # type: ignore


from .rest_base import _BaseTestingRestTransport

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
class AsyncTestingRestStub:
    _session: AsyncAuthorizedSession
    _host: str

class AsyncTestingRestTransport(_BaseTestingRestTransport):
    """Asynchronous REST backend transport for Testing.

    A service to facilitate running discrete sets of tests against
    Showcase. Adding this comment with special characters for comment
    formatting tests:

    1. (abra->kadabra->alakazam)

    2) [Nonsense][]: ``pokemon/*/psychic/*``

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
            self.create_session: self._wrap_method(
                self.create_session,
                default_timeout=None,
                client_info=client_info,
            ),
            self.get_session: self._wrap_method(
                self.get_session,
                default_timeout=None,
                client_info=client_info,
            ),
            self.list_sessions: self._wrap_method(
                self.list_sessions,
                default_timeout=None,
                client_info=client_info,
            ),
            self.delete_session: self._wrap_method(
                self.delete_session,
                default_timeout=None,
                client_info=client_info,
            ),
            self.report_session: self._wrap_method(
                self.report_session,
                default_timeout=None,
                client_info=client_info,
            ),
            self.list_tests: self._wrap_method(
                self.list_tests,
                default_timeout=None,
                client_info=client_info,
            ),
            self.delete_test: self._wrap_method(
                self.delete_test,
                default_timeout=None,
                client_info=client_info,
            ),
            self.verify_test: self._wrap_method(
                self.verify_test,
                default_timeout=None,
                client_info=client_info,
            ),
        }

    def _wrap_method(self, func, *args, **kwargs):
        if self._wrap_with_kind:  # pragma: NO COVER
            kwargs["kind"] = self.kind
        return gapic_v1.method_async.wrap_method(func, *args, **kwargs)

    class _CreateSession(_BaseTestingRestTransport._BaseCreateSession, AsyncTestingRestStub):
        def __hash__(self):
            return hash("AsyncTestingRestTransport.CreateSession")

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
                    request: testing.CreateSessionRequest, *,
                    retry: OptionalRetry=gapic_v1.method.DEFAULT,
                    timeout: Optional[float]=None,
                    metadata: Sequence[Tuple[str, str]]=(),
                    ) -> testing.Session:
            r"""Call the create session method over HTTP.

            Args:
                request (~.testing.CreateSessionRequest):
                    The request object. The request for the CreateSession
                method.
                retry (google.api_core.retry_async.AsyncRetry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, str]]): Strings which should be
                    sent along with the request as metadata.

            Returns:
                ~.testing.Session:
                    A session is a suite of tests,
                generally being made in the context of
                testing code generation.

                A session defines tests it may expect,
                based on which version of the code
                generation spec is in use.

            """

            http_options = _BaseTestingRestTransport._BaseCreateSession._get_http_options()
            transcoded_request = _BaseTestingRestTransport._BaseCreateSession._get_transcoded_request(http_options, request)

            body = _BaseTestingRestTransport._BaseCreateSession._get_request_body_json(transcoded_request)

            # Jsonify the query params
            query_params = _BaseTestingRestTransport._BaseCreateSession._get_query_params_json(transcoded_request)

            # Send the request
            response = await AsyncTestingRestTransport._CreateSession._get_response(self._host, metadata, query_params, self._session, timeout, transcoded_request, body)

            # In case of error, raise the appropriate core_exceptions.GoogleAPICallError exception
            # subclass.
            if response.status_code >= 400:
                content = await response.read()
                payload = json.loads(content.decode('utf-8'))
                request_url = "{host}{uri}".format(host=self._host, uri=transcoded_request['uri'])
                method = transcoded_request['method']
                raise core_exceptions.format_http_response_error(response, method, request_url, payload)  # type: ignore

            # Return the response
            resp = testing.Session()
            pb_resp = testing.Session.pb(resp)
            content = await response.read()
            json_format.Parse(content, pb_resp, ignore_unknown_fields=True)
            return resp

    class _DeleteSession(_BaseTestingRestTransport._BaseDeleteSession, AsyncTestingRestStub):
        def __hash__(self):
            return hash("AsyncTestingRestTransport.DeleteSession")

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
                    request: testing.DeleteSessionRequest, *,
                    retry: OptionalRetry=gapic_v1.method.DEFAULT,
                    timeout: Optional[float]=None,
                    metadata: Sequence[Tuple[str, str]]=(),
                    ):
            r"""Call the delete session method over HTTP.

            Args:
                request (~.testing.DeleteSessionRequest):
                    The request object. Request for the DeleteSession method.
                retry (google.api_core.retry_async.AsyncRetry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, str]]): Strings which should be
                    sent along with the request as metadata.
            """

            http_options = _BaseTestingRestTransport._BaseDeleteSession._get_http_options()
            transcoded_request = _BaseTestingRestTransport._BaseDeleteSession._get_transcoded_request(http_options, request)

            # Jsonify the query params
            query_params = _BaseTestingRestTransport._BaseDeleteSession._get_query_params_json(transcoded_request)

            # Send the request
            response = await AsyncTestingRestTransport._DeleteSession._get_response(self._host, metadata, query_params, self._session, timeout, transcoded_request)

            # In case of error, raise the appropriate core_exceptions.GoogleAPICallError exception
            # subclass.
            if response.status_code >= 400:
                content = await response.read()
                payload = json.loads(content.decode('utf-8'))
                request_url = "{host}{uri}".format(host=self._host, uri=transcoded_request['uri'])
                method = transcoded_request['method']
                raise core_exceptions.format_http_response_error(response, method, request_url, payload)  # type: ignore

    class _DeleteTest(_BaseTestingRestTransport._BaseDeleteTest, AsyncTestingRestStub):
        def __hash__(self):
            return hash("AsyncTestingRestTransport.DeleteTest")

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
                    request: testing.DeleteTestRequest, *,
                    retry: OptionalRetry=gapic_v1.method.DEFAULT,
                    timeout: Optional[float]=None,
                    metadata: Sequence[Tuple[str, str]]=(),
                    ):
            r"""Call the delete test method over HTTP.

            Args:
                request (~.testing.DeleteTestRequest):
                    The request object. Request message for deleting a test.
                retry (google.api_core.retry_async.AsyncRetry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, str]]): Strings which should be
                    sent along with the request as metadata.
            """

            http_options = _BaseTestingRestTransport._BaseDeleteTest._get_http_options()
            transcoded_request = _BaseTestingRestTransport._BaseDeleteTest._get_transcoded_request(http_options, request)

            # Jsonify the query params
            query_params = _BaseTestingRestTransport._BaseDeleteTest._get_query_params_json(transcoded_request)

            # Send the request
            response = await AsyncTestingRestTransport._DeleteTest._get_response(self._host, metadata, query_params, self._session, timeout, transcoded_request)

            # In case of error, raise the appropriate core_exceptions.GoogleAPICallError exception
            # subclass.
            if response.status_code >= 400:
                content = await response.read()
                payload = json.loads(content.decode('utf-8'))
                request_url = "{host}{uri}".format(host=self._host, uri=transcoded_request['uri'])
                method = transcoded_request['method']
                raise core_exceptions.format_http_response_error(response, method, request_url, payload)  # type: ignore

    class _GetSession(_BaseTestingRestTransport._BaseGetSession, AsyncTestingRestStub):
        def __hash__(self):
            return hash("AsyncTestingRestTransport.GetSession")

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
                    request: testing.GetSessionRequest, *,
                    retry: OptionalRetry=gapic_v1.method.DEFAULT,
                    timeout: Optional[float]=None,
                    metadata: Sequence[Tuple[str, str]]=(),
                    ) -> testing.Session:
            r"""Call the get session method over HTTP.

            Args:
                request (~.testing.GetSessionRequest):
                    The request object. The request for the GetSession
                method.
                retry (google.api_core.retry_async.AsyncRetry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, str]]): Strings which should be
                    sent along with the request as metadata.

            Returns:
                ~.testing.Session:
                    A session is a suite of tests,
                generally being made in the context of
                testing code generation.

                A session defines tests it may expect,
                based on which version of the code
                generation spec is in use.

            """

            http_options = _BaseTestingRestTransport._BaseGetSession._get_http_options()
            transcoded_request = _BaseTestingRestTransport._BaseGetSession._get_transcoded_request(http_options, request)

            # Jsonify the query params
            query_params = _BaseTestingRestTransport._BaseGetSession._get_query_params_json(transcoded_request)

            # Send the request
            response = await AsyncTestingRestTransport._GetSession._get_response(self._host, metadata, query_params, self._session, timeout, transcoded_request)

            # In case of error, raise the appropriate core_exceptions.GoogleAPICallError exception
            # subclass.
            if response.status_code >= 400:
                content = await response.read()
                payload = json.loads(content.decode('utf-8'))
                request_url = "{host}{uri}".format(host=self._host, uri=transcoded_request['uri'])
                method = transcoded_request['method']
                raise core_exceptions.format_http_response_error(response, method, request_url, payload)  # type: ignore

            # Return the response
            resp = testing.Session()
            pb_resp = testing.Session.pb(resp)
            content = await response.read()
            json_format.Parse(content, pb_resp, ignore_unknown_fields=True)
            return resp

    class _ListSessions(_BaseTestingRestTransport._BaseListSessions, AsyncTestingRestStub):
        def __hash__(self):
            return hash("AsyncTestingRestTransport.ListSessions")

        async def __call__(self,
                    request: testing.ListSessionsRequest, *,
                    retry: OptionalRetry=gapic_v1.method.DEFAULT,
                    timeout: Optional[float]=None,
                    metadata: Sequence[Tuple[str, str]]=(),
                    ) -> testing.ListSessionsResponse:
                raise NotImplementedError(
                    "Method ListSessions is not available over REST transport"
                )

    class _ListTests(_BaseTestingRestTransport._BaseListTests, AsyncTestingRestStub):
        def __hash__(self):
            return hash("AsyncTestingRestTransport.ListTests")

        async def __call__(self,
                    request: testing.ListTestsRequest, *,
                    retry: OptionalRetry=gapic_v1.method.DEFAULT,
                    timeout: Optional[float]=None,
                    metadata: Sequence[Tuple[str, str]]=(),
                    ) -> testing.ListTestsResponse:
                raise NotImplementedError(
                    "Method ListTests is not available over REST transport"
                )

    class _ReportSession(_BaseTestingRestTransport._BaseReportSession, AsyncTestingRestStub):
        def __hash__(self):
            return hash("AsyncTestingRestTransport.ReportSession")

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
                    request: testing.ReportSessionRequest, *,
                    retry: OptionalRetry=gapic_v1.method.DEFAULT,
                    timeout: Optional[float]=None,
                    metadata: Sequence[Tuple[str, str]]=(),
                    ) -> testing.ReportSessionResponse:
            r"""Call the report session method over HTTP.

            Args:
                request (~.testing.ReportSessionRequest):
                    The request object. Request message for reporting on a
                session.
                retry (google.api_core.retry_async.AsyncRetry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, str]]): Strings which should be
                    sent along with the request as metadata.

            Returns:
                ~.testing.ReportSessionResponse:
                    Response message for reporting on a
                session.

            """

            http_options = _BaseTestingRestTransport._BaseReportSession._get_http_options()
            transcoded_request = _BaseTestingRestTransport._BaseReportSession._get_transcoded_request(http_options, request)

            # Jsonify the query params
            query_params = _BaseTestingRestTransport._BaseReportSession._get_query_params_json(transcoded_request)

            # Send the request
            response = await AsyncTestingRestTransport._ReportSession._get_response(self._host, metadata, query_params, self._session, timeout, transcoded_request)

            # In case of error, raise the appropriate core_exceptions.GoogleAPICallError exception
            # subclass.
            if response.status_code >= 400:
                content = await response.read()
                payload = json.loads(content.decode('utf-8'))
                request_url = "{host}{uri}".format(host=self._host, uri=transcoded_request['uri'])
                method = transcoded_request['method']
                raise core_exceptions.format_http_response_error(response, method, request_url, payload)  # type: ignore

            # Return the response
            resp = testing.ReportSessionResponse()
            pb_resp = testing.ReportSessionResponse.pb(resp)
            content = await response.read()
            json_format.Parse(content, pb_resp, ignore_unknown_fields=True)
            return resp

    class _VerifyTest(_BaseTestingRestTransport._BaseVerifyTest, AsyncTestingRestStub):
        def __hash__(self):
            return hash("AsyncTestingRestTransport.VerifyTest")

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
                    request: testing.VerifyTestRequest, *,
                    retry: OptionalRetry=gapic_v1.method.DEFAULT,
                    timeout: Optional[float]=None,
                    metadata: Sequence[Tuple[str, str]]=(),
                    ) -> testing.VerifyTestResponse:
            r"""Call the verify test method over HTTP.

            Args:
                request (~.testing.VerifyTestRequest):
                    The request object.
                retry (google.api_core.retry_async.AsyncRetry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, str]]): Strings which should be
                    sent along with the request as metadata.

            Returns:
                ~.testing.VerifyTestResponse:

            """

            http_options = _BaseTestingRestTransport._BaseVerifyTest._get_http_options()
            transcoded_request = _BaseTestingRestTransport._BaseVerifyTest._get_transcoded_request(http_options, request)

            # Jsonify the query params
            query_params = _BaseTestingRestTransport._BaseVerifyTest._get_query_params_json(transcoded_request)

            # Send the request
            response = await AsyncTestingRestTransport._VerifyTest._get_response(self._host, metadata, query_params, self._session, timeout, transcoded_request)

            # In case of error, raise the appropriate core_exceptions.GoogleAPICallError exception
            # subclass.
            if response.status_code >= 400:
                content = await response.read()
                payload = json.loads(content.decode('utf-8'))
                request_url = "{host}{uri}".format(host=self._host, uri=transcoded_request['uri'])
                method = transcoded_request['method']
                raise core_exceptions.format_http_response_error(response, method, request_url, payload)  # type: ignore

            # Return the response
            resp = testing.VerifyTestResponse()
            pb_resp = testing.VerifyTestResponse.pb(resp)
            content = await response.read()
            json_format.Parse(content, pb_resp, ignore_unknown_fields=True)
            return resp

    @property
    def create_session(self) -> Callable[
            [testing.CreateSessionRequest],
            testing.Session]:
        return self._CreateSession(self._session, self._host)  # type: ignore

    @property
    def delete_session(self) -> Callable[
            [testing.DeleteSessionRequest],
            empty_pb2.Empty]:
        return self._DeleteSession(self._session, self._host)  # type: ignore

    @property
    def delete_test(self) -> Callable[
            [testing.DeleteTestRequest],
            empty_pb2.Empty]:
        return self._DeleteTest(self._session, self._host)  # type: ignore

    @property
    def get_session(self) -> Callable[
            [testing.GetSessionRequest],
            testing.Session]:
        return self._GetSession(self._session, self._host)  # type: ignore

    @property
    def list_sessions(self) -> Callable[
            [testing.ListSessionsRequest],
            testing.ListSessionsResponse]:
        return self._ListSessions(self._session, self._host)  # type: ignore

    @property
    def list_tests(self) -> Callable[
            [testing.ListTestsRequest],
            testing.ListTestsResponse]:
        return self._ListTests(self._session, self._host)  # type: ignore

    @property
    def report_session(self) -> Callable[
            [testing.ReportSessionRequest],
            testing.ReportSessionResponse]:
        return self._ReportSession(self._session, self._host)  # type: ignore

    @property
    def verify_test(self) -> Callable[
            [testing.VerifyTestRequest],
            testing.VerifyTestResponse]:
        return self._VerifyTest(self._session, self._host)  # type: ignore

    @property
    def kind(self) -> str:
        return "rest_asyncio"

    async def close(self):
        await self._session.close()

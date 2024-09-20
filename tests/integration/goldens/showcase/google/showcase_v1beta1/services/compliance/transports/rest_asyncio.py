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


from google.showcase_v1beta1.types import compliance
from google.longrunning import operations_pb2  # type: ignore


from .rest_base import _BaseComplianceRestTransport

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
class AsyncComplianceRestStub:
    _session: AsyncAuthorizedSession
    _host: str

class AsyncComplianceRestTransport(_BaseComplianceRestTransport):
    """Asynchronous REST backend transport for Compliance.

    This service is used to test that GAPICs implement various
    REST-related features correctly. This mostly means transcoding
    proto3 requests to REST format correctly for various types of
    HTTP annotations, but it also includes verifying that unknown
    (numeric) enums received by clients can be round-tripped
    correctly.

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
            self.repeat_data_body: self._wrap_method(
                self.repeat_data_body,
                default_timeout=None,
                client_info=client_info,
            ),
            self.repeat_data_body_info: self._wrap_method(
                self.repeat_data_body_info,
                default_timeout=None,
                client_info=client_info,
            ),
            self.repeat_data_query: self._wrap_method(
                self.repeat_data_query,
                default_timeout=None,
                client_info=client_info,
            ),
            self.repeat_data_simple_path: self._wrap_method(
                self.repeat_data_simple_path,
                default_timeout=None,
                client_info=client_info,
            ),
            self.repeat_data_path_resource: self._wrap_method(
                self.repeat_data_path_resource,
                default_timeout=None,
                client_info=client_info,
            ),
            self.repeat_data_path_trailing_resource: self._wrap_method(
                self.repeat_data_path_trailing_resource,
                default_timeout=None,
                client_info=client_info,
            ),
            self.repeat_data_body_put: self._wrap_method(
                self.repeat_data_body_put,
                default_timeout=None,
                client_info=client_info,
            ),
            self.repeat_data_body_patch: self._wrap_method(
                self.repeat_data_body_patch,
                default_timeout=None,
                client_info=client_info,
            ),
            self.get_enum: self._wrap_method(
                self.get_enum,
                default_timeout=None,
                client_info=client_info,
            ),
            self.verify_enum: self._wrap_method(
                self.verify_enum,
                default_timeout=None,
                client_info=client_info,
            ),
        }

    def _wrap_method(self, func, *args, **kwargs):
        if self._wrap_with_kind:  # pragma: NO COVER
            kwargs["kind"] = self.kind
        return gapic_v1.method_async.wrap_method(func, *args, **kwargs)

    class _GetEnum(_BaseComplianceRestTransport._BaseGetEnum, AsyncComplianceRestStub):
        def __hash__(self):
            return hash("AsyncComplianceRestTransport.GetEnum")

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
                    request: compliance.EnumRequest, *,
                    retry: OptionalRetry=gapic_v1.method.DEFAULT,
                    timeout: Optional[float]=None,
                    metadata: Sequence[Tuple[str, str]]=(),
                    ) -> compliance.EnumResponse:
            r"""Call the get enum method over HTTP.

            Args:
                request (~.compliance.EnumRequest):
                    The request object.
                retry (google.api_core.retry_async.AsyncRetry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, str]]): Strings which should be
                    sent along with the request as metadata.

            Returns:
                ~.compliance.EnumResponse:

            """

            http_options = _BaseComplianceRestTransport._BaseGetEnum._get_http_options()
            transcoded_request = _BaseComplianceRestTransport._BaseGetEnum._get_transcoded_request(http_options, request)

            # Jsonify the query params
            query_params = _BaseComplianceRestTransport._BaseGetEnum._get_query_params_json(transcoded_request)

            # Send the request
            response = await AsyncComplianceRestTransport._GetEnum._get_response(self._host, metadata, query_params, self._session, timeout, transcoded_request)

            # In case of error, raise the appropriate core_exceptions.GoogleAPICallError exception
            # subclass.
            if response.status_code >= 400:
                content = await response.read()
                payload = json.loads(content.decode('utf-8'))
                request_url = "{host}{uri}".format(host=self._host, uri=transcoded_request['uri'])
                method = transcoded_request['method']
                raise core_exceptions.format_http_response_error(response, method, request_url, payload)  # type: ignore

            # Return the response
            resp = compliance.EnumResponse()
            pb_resp = compliance.EnumResponse.pb(resp)
            content = await response.read()
            json_format.Parse(content, pb_resp, ignore_unknown_fields=True)
            return resp

    class _RepeatDataBody(_BaseComplianceRestTransport._BaseRepeatDataBody, AsyncComplianceRestStub):
        def __hash__(self):
            return hash("AsyncComplianceRestTransport.RepeatDataBody")

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
                    request: compliance.RepeatRequest, *,
                    retry: OptionalRetry=gapic_v1.method.DEFAULT,
                    timeout: Optional[float]=None,
                    metadata: Sequence[Tuple[str, str]]=(),
                    ) -> compliance.RepeatResponse:
            r"""Call the repeat data body method over HTTP.

            Args:
                request (~.compliance.RepeatRequest):
                    The request object.
                retry (google.api_core.retry_async.AsyncRetry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, str]]): Strings which should be
                    sent along with the request as metadata.

            Returns:
                ~.compliance.RepeatResponse:

            """

            http_options = _BaseComplianceRestTransport._BaseRepeatDataBody._get_http_options()
            transcoded_request = _BaseComplianceRestTransport._BaseRepeatDataBody._get_transcoded_request(http_options, request)

            body = _BaseComplianceRestTransport._BaseRepeatDataBody._get_request_body_json(transcoded_request)

            # Jsonify the query params
            query_params = _BaseComplianceRestTransport._BaseRepeatDataBody._get_query_params_json(transcoded_request)

            # Send the request
            response = await AsyncComplianceRestTransport._RepeatDataBody._get_response(self._host, metadata, query_params, self._session, timeout, transcoded_request, body)

            # In case of error, raise the appropriate core_exceptions.GoogleAPICallError exception
            # subclass.
            if response.status_code >= 400:
                content = await response.read()
                payload = json.loads(content.decode('utf-8'))
                request_url = "{host}{uri}".format(host=self._host, uri=transcoded_request['uri'])
                method = transcoded_request['method']
                raise core_exceptions.format_http_response_error(response, method, request_url, payload)  # type: ignore

            # Return the response
            resp = compliance.RepeatResponse()
            pb_resp = compliance.RepeatResponse.pb(resp)
            content = await response.read()
            json_format.Parse(content, pb_resp, ignore_unknown_fields=True)
            return resp

    class _RepeatDataBodyInfo(_BaseComplianceRestTransport._BaseRepeatDataBodyInfo, AsyncComplianceRestStub):
        def __hash__(self):
            return hash("AsyncComplianceRestTransport.RepeatDataBodyInfo")

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
                    request: compliance.RepeatRequest, *,
                    retry: OptionalRetry=gapic_v1.method.DEFAULT,
                    timeout: Optional[float]=None,
                    metadata: Sequence[Tuple[str, str]]=(),
                    ) -> compliance.RepeatResponse:
            r"""Call the repeat data body info method over HTTP.

            Args:
                request (~.compliance.RepeatRequest):
                    The request object.
                retry (google.api_core.retry_async.AsyncRetry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, str]]): Strings which should be
                    sent along with the request as metadata.

            Returns:
                ~.compliance.RepeatResponse:

            """

            http_options = _BaseComplianceRestTransport._BaseRepeatDataBodyInfo._get_http_options()
            transcoded_request = _BaseComplianceRestTransport._BaseRepeatDataBodyInfo._get_transcoded_request(http_options, request)

            body = _BaseComplianceRestTransport._BaseRepeatDataBodyInfo._get_request_body_json(transcoded_request)

            # Jsonify the query params
            query_params = _BaseComplianceRestTransport._BaseRepeatDataBodyInfo._get_query_params_json(transcoded_request)

            # Send the request
            response = await AsyncComplianceRestTransport._RepeatDataBodyInfo._get_response(self._host, metadata, query_params, self._session, timeout, transcoded_request, body)

            # In case of error, raise the appropriate core_exceptions.GoogleAPICallError exception
            # subclass.
            if response.status_code >= 400:
                content = await response.read()
                payload = json.loads(content.decode('utf-8'))
                request_url = "{host}{uri}".format(host=self._host, uri=transcoded_request['uri'])
                method = transcoded_request['method']
                raise core_exceptions.format_http_response_error(response, method, request_url, payload)  # type: ignore

            # Return the response
            resp = compliance.RepeatResponse()
            pb_resp = compliance.RepeatResponse.pb(resp)
            content = await response.read()
            json_format.Parse(content, pb_resp, ignore_unknown_fields=True)
            return resp

    class _RepeatDataBodyPatch(_BaseComplianceRestTransport._BaseRepeatDataBodyPatch, AsyncComplianceRestStub):
        def __hash__(self):
            return hash("AsyncComplianceRestTransport.RepeatDataBodyPatch")

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
                    request: compliance.RepeatRequest, *,
                    retry: OptionalRetry=gapic_v1.method.DEFAULT,
                    timeout: Optional[float]=None,
                    metadata: Sequence[Tuple[str, str]]=(),
                    ) -> compliance.RepeatResponse:
            r"""Call the repeat data body patch method over HTTP.

            Args:
                request (~.compliance.RepeatRequest):
                    The request object.
                retry (google.api_core.retry_async.AsyncRetry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, str]]): Strings which should be
                    sent along with the request as metadata.

            Returns:
                ~.compliance.RepeatResponse:

            """

            http_options = _BaseComplianceRestTransport._BaseRepeatDataBodyPatch._get_http_options()
            transcoded_request = _BaseComplianceRestTransport._BaseRepeatDataBodyPatch._get_transcoded_request(http_options, request)

            body = _BaseComplianceRestTransport._BaseRepeatDataBodyPatch._get_request_body_json(transcoded_request)

            # Jsonify the query params
            query_params = _BaseComplianceRestTransport._BaseRepeatDataBodyPatch._get_query_params_json(transcoded_request)

            # Send the request
            response = await AsyncComplianceRestTransport._RepeatDataBodyPatch._get_response(self._host, metadata, query_params, self._session, timeout, transcoded_request, body)

            # In case of error, raise the appropriate core_exceptions.GoogleAPICallError exception
            # subclass.
            if response.status_code >= 400:
                content = await response.read()
                payload = json.loads(content.decode('utf-8'))
                request_url = "{host}{uri}".format(host=self._host, uri=transcoded_request['uri'])
                method = transcoded_request['method']
                raise core_exceptions.format_http_response_error(response, method, request_url, payload)  # type: ignore

            # Return the response
            resp = compliance.RepeatResponse()
            pb_resp = compliance.RepeatResponse.pb(resp)
            content = await response.read()
            json_format.Parse(content, pb_resp, ignore_unknown_fields=True)
            return resp

    class _RepeatDataBodyPut(_BaseComplianceRestTransport._BaseRepeatDataBodyPut, AsyncComplianceRestStub):
        def __hash__(self):
            return hash("AsyncComplianceRestTransport.RepeatDataBodyPut")

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
                    request: compliance.RepeatRequest, *,
                    retry: OptionalRetry=gapic_v1.method.DEFAULT,
                    timeout: Optional[float]=None,
                    metadata: Sequence[Tuple[str, str]]=(),
                    ) -> compliance.RepeatResponse:
            r"""Call the repeat data body put method over HTTP.

            Args:
                request (~.compliance.RepeatRequest):
                    The request object.
                retry (google.api_core.retry_async.AsyncRetry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, str]]): Strings which should be
                    sent along with the request as metadata.

            Returns:
                ~.compliance.RepeatResponse:

            """

            http_options = _BaseComplianceRestTransport._BaseRepeatDataBodyPut._get_http_options()
            transcoded_request = _BaseComplianceRestTransport._BaseRepeatDataBodyPut._get_transcoded_request(http_options, request)

            body = _BaseComplianceRestTransport._BaseRepeatDataBodyPut._get_request_body_json(transcoded_request)

            # Jsonify the query params
            query_params = _BaseComplianceRestTransport._BaseRepeatDataBodyPut._get_query_params_json(transcoded_request)

            # Send the request
            response = await AsyncComplianceRestTransport._RepeatDataBodyPut._get_response(self._host, metadata, query_params, self._session, timeout, transcoded_request, body)

            # In case of error, raise the appropriate core_exceptions.GoogleAPICallError exception
            # subclass.
            if response.status_code >= 400:
                content = await response.read()
                payload = json.loads(content.decode('utf-8'))
                request_url = "{host}{uri}".format(host=self._host, uri=transcoded_request['uri'])
                method = transcoded_request['method']
                raise core_exceptions.format_http_response_error(response, method, request_url, payload)  # type: ignore

            # Return the response
            resp = compliance.RepeatResponse()
            pb_resp = compliance.RepeatResponse.pb(resp)
            content = await response.read()
            json_format.Parse(content, pb_resp, ignore_unknown_fields=True)
            return resp

    class _RepeatDataPathResource(_BaseComplianceRestTransport._BaseRepeatDataPathResource, AsyncComplianceRestStub):
        def __hash__(self):
            return hash("AsyncComplianceRestTransport.RepeatDataPathResource")

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
                    request: compliance.RepeatRequest, *,
                    retry: OptionalRetry=gapic_v1.method.DEFAULT,
                    timeout: Optional[float]=None,
                    metadata: Sequence[Tuple[str, str]]=(),
                    ) -> compliance.RepeatResponse:
            r"""Call the repeat data path resource method over HTTP.

            Args:
                request (~.compliance.RepeatRequest):
                    The request object.
                retry (google.api_core.retry_async.AsyncRetry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, str]]): Strings which should be
                    sent along with the request as metadata.

            Returns:
                ~.compliance.RepeatResponse:

            """

            http_options = _BaseComplianceRestTransport._BaseRepeatDataPathResource._get_http_options()
            transcoded_request = _BaseComplianceRestTransport._BaseRepeatDataPathResource._get_transcoded_request(http_options, request)

            # Jsonify the query params
            query_params = _BaseComplianceRestTransport._BaseRepeatDataPathResource._get_query_params_json(transcoded_request)

            # Send the request
            response = await AsyncComplianceRestTransport._RepeatDataPathResource._get_response(self._host, metadata, query_params, self._session, timeout, transcoded_request)

            # In case of error, raise the appropriate core_exceptions.GoogleAPICallError exception
            # subclass.
            if response.status_code >= 400:
                content = await response.read()
                payload = json.loads(content.decode('utf-8'))
                request_url = "{host}{uri}".format(host=self._host, uri=transcoded_request['uri'])
                method = transcoded_request['method']
                raise core_exceptions.format_http_response_error(response, method, request_url, payload)  # type: ignore

            # Return the response
            resp = compliance.RepeatResponse()
            pb_resp = compliance.RepeatResponse.pb(resp)
            content = await response.read()
            json_format.Parse(content, pb_resp, ignore_unknown_fields=True)
            return resp

    class _RepeatDataPathTrailingResource(_BaseComplianceRestTransport._BaseRepeatDataPathTrailingResource, AsyncComplianceRestStub):
        def __hash__(self):
            return hash("AsyncComplianceRestTransport.RepeatDataPathTrailingResource")

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
                    request: compliance.RepeatRequest, *,
                    retry: OptionalRetry=gapic_v1.method.DEFAULT,
                    timeout: Optional[float]=None,
                    metadata: Sequence[Tuple[str, str]]=(),
                    ) -> compliance.RepeatResponse:
            r"""Call the repeat data path trailing
        resource method over HTTP.

            Args:
                request (~.compliance.RepeatRequest):
                    The request object.
                retry (google.api_core.retry_async.AsyncRetry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, str]]): Strings which should be
                    sent along with the request as metadata.

            Returns:
                ~.compliance.RepeatResponse:

            """

            http_options = _BaseComplianceRestTransport._BaseRepeatDataPathTrailingResource._get_http_options()
            transcoded_request = _BaseComplianceRestTransport._BaseRepeatDataPathTrailingResource._get_transcoded_request(http_options, request)

            # Jsonify the query params
            query_params = _BaseComplianceRestTransport._BaseRepeatDataPathTrailingResource._get_query_params_json(transcoded_request)

            # Send the request
            response = await AsyncComplianceRestTransport._RepeatDataPathTrailingResource._get_response(self._host, metadata, query_params, self._session, timeout, transcoded_request)

            # In case of error, raise the appropriate core_exceptions.GoogleAPICallError exception
            # subclass.
            if response.status_code >= 400:
                content = await response.read()
                payload = json.loads(content.decode('utf-8'))
                request_url = "{host}{uri}".format(host=self._host, uri=transcoded_request['uri'])
                method = transcoded_request['method']
                raise core_exceptions.format_http_response_error(response, method, request_url, payload)  # type: ignore

            # Return the response
            resp = compliance.RepeatResponse()
            pb_resp = compliance.RepeatResponse.pb(resp)
            content = await response.read()
            json_format.Parse(content, pb_resp, ignore_unknown_fields=True)
            return resp

    class _RepeatDataQuery(_BaseComplianceRestTransport._BaseRepeatDataQuery, AsyncComplianceRestStub):
        def __hash__(self):
            return hash("AsyncComplianceRestTransport.RepeatDataQuery")

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
                    request: compliance.RepeatRequest, *,
                    retry: OptionalRetry=gapic_v1.method.DEFAULT,
                    timeout: Optional[float]=None,
                    metadata: Sequence[Tuple[str, str]]=(),
                    ) -> compliance.RepeatResponse:
            r"""Call the repeat data query method over HTTP.

            Args:
                request (~.compliance.RepeatRequest):
                    The request object.
                retry (google.api_core.retry_async.AsyncRetry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, str]]): Strings which should be
                    sent along with the request as metadata.

            Returns:
                ~.compliance.RepeatResponse:

            """

            http_options = _BaseComplianceRestTransport._BaseRepeatDataQuery._get_http_options()
            transcoded_request = _BaseComplianceRestTransport._BaseRepeatDataQuery._get_transcoded_request(http_options, request)

            # Jsonify the query params
            query_params = _BaseComplianceRestTransport._BaseRepeatDataQuery._get_query_params_json(transcoded_request)

            # Send the request
            response = await AsyncComplianceRestTransport._RepeatDataQuery._get_response(self._host, metadata, query_params, self._session, timeout, transcoded_request)

            # In case of error, raise the appropriate core_exceptions.GoogleAPICallError exception
            # subclass.
            if response.status_code >= 400:
                content = await response.read()
                payload = json.loads(content.decode('utf-8'))
                request_url = "{host}{uri}".format(host=self._host, uri=transcoded_request['uri'])
                method = transcoded_request['method']
                raise core_exceptions.format_http_response_error(response, method, request_url, payload)  # type: ignore

            # Return the response
            resp = compliance.RepeatResponse()
            pb_resp = compliance.RepeatResponse.pb(resp)
            content = await response.read()
            json_format.Parse(content, pb_resp, ignore_unknown_fields=True)
            return resp

    class _RepeatDataSimplePath(_BaseComplianceRestTransport._BaseRepeatDataSimplePath, AsyncComplianceRestStub):
        def __hash__(self):
            return hash("AsyncComplianceRestTransport.RepeatDataSimplePath")

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
                    request: compliance.RepeatRequest, *,
                    retry: OptionalRetry=gapic_v1.method.DEFAULT,
                    timeout: Optional[float]=None,
                    metadata: Sequence[Tuple[str, str]]=(),
                    ) -> compliance.RepeatResponse:
            r"""Call the repeat data simple path method over HTTP.

            Args:
                request (~.compliance.RepeatRequest):
                    The request object.
                retry (google.api_core.retry_async.AsyncRetry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, str]]): Strings which should be
                    sent along with the request as metadata.

            Returns:
                ~.compliance.RepeatResponse:

            """

            http_options = _BaseComplianceRestTransport._BaseRepeatDataSimplePath._get_http_options()
            transcoded_request = _BaseComplianceRestTransport._BaseRepeatDataSimplePath._get_transcoded_request(http_options, request)

            # Jsonify the query params
            query_params = _BaseComplianceRestTransport._BaseRepeatDataSimplePath._get_query_params_json(transcoded_request)

            # Send the request
            response = await AsyncComplianceRestTransport._RepeatDataSimplePath._get_response(self._host, metadata, query_params, self._session, timeout, transcoded_request)

            # In case of error, raise the appropriate core_exceptions.GoogleAPICallError exception
            # subclass.
            if response.status_code >= 400:
                content = await response.read()
                payload = json.loads(content.decode('utf-8'))
                request_url = "{host}{uri}".format(host=self._host, uri=transcoded_request['uri'])
                method = transcoded_request['method']
                raise core_exceptions.format_http_response_error(response, method, request_url, payload)  # type: ignore

            # Return the response
            resp = compliance.RepeatResponse()
            pb_resp = compliance.RepeatResponse.pb(resp)
            content = await response.read()
            json_format.Parse(content, pb_resp, ignore_unknown_fields=True)
            return resp

    class _VerifyEnum(_BaseComplianceRestTransport._BaseVerifyEnum, AsyncComplianceRestStub):
        def __hash__(self):
            return hash("AsyncComplianceRestTransport.VerifyEnum")

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
                    request: compliance.EnumResponse, *,
                    retry: OptionalRetry=gapic_v1.method.DEFAULT,
                    timeout: Optional[float]=None,
                    metadata: Sequence[Tuple[str, str]]=(),
                    ) -> compliance.EnumResponse:
            r"""Call the verify enum method over HTTP.

            Args:
                request (~.compliance.EnumResponse):
                    The request object.
                retry (google.api_core.retry_async.AsyncRetry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, str]]): Strings which should be
                    sent along with the request as metadata.

            Returns:
                ~.compliance.EnumResponse:

            """

            http_options = _BaseComplianceRestTransport._BaseVerifyEnum._get_http_options()
            transcoded_request = _BaseComplianceRestTransport._BaseVerifyEnum._get_transcoded_request(http_options, request)

            # Jsonify the query params
            query_params = _BaseComplianceRestTransport._BaseVerifyEnum._get_query_params_json(transcoded_request)

            # Send the request
            response = await AsyncComplianceRestTransport._VerifyEnum._get_response(self._host, metadata, query_params, self._session, timeout, transcoded_request)

            # In case of error, raise the appropriate core_exceptions.GoogleAPICallError exception
            # subclass.
            if response.status_code >= 400:
                content = await response.read()
                payload = json.loads(content.decode('utf-8'))
                request_url = "{host}{uri}".format(host=self._host, uri=transcoded_request['uri'])
                method = transcoded_request['method']
                raise core_exceptions.format_http_response_error(response, method, request_url, payload)  # type: ignore

            # Return the response
            resp = compliance.EnumResponse()
            pb_resp = compliance.EnumResponse.pb(resp)
            content = await response.read()
            json_format.Parse(content, pb_resp, ignore_unknown_fields=True)
            return resp

    @property
    def get_enum(self) -> Callable[
            [compliance.EnumRequest],
            compliance.EnumResponse]:
        return self._GetEnum(self._session, self._host)  # type: ignore

    @property
    def repeat_data_body(self) -> Callable[
            [compliance.RepeatRequest],
            compliance.RepeatResponse]:
        return self._RepeatDataBody(self._session, self._host)  # type: ignore

    @property
    def repeat_data_body_info(self) -> Callable[
            [compliance.RepeatRequest],
            compliance.RepeatResponse]:
        return self._RepeatDataBodyInfo(self._session, self._host)  # type: ignore

    @property
    def repeat_data_body_patch(self) -> Callable[
            [compliance.RepeatRequest],
            compliance.RepeatResponse]:
        return self._RepeatDataBodyPatch(self._session, self._host)  # type: ignore

    @property
    def repeat_data_body_put(self) -> Callable[
            [compliance.RepeatRequest],
            compliance.RepeatResponse]:
        return self._RepeatDataBodyPut(self._session, self._host)  # type: ignore

    @property
    def repeat_data_path_resource(self) -> Callable[
            [compliance.RepeatRequest],
            compliance.RepeatResponse]:
        return self._RepeatDataPathResource(self._session, self._host)  # type: ignore

    @property
    def repeat_data_path_trailing_resource(self) -> Callable[
            [compliance.RepeatRequest],
            compliance.RepeatResponse]:
        return self._RepeatDataPathTrailingResource(self._session, self._host)  # type: ignore

    @property
    def repeat_data_query(self) -> Callable[
            [compliance.RepeatRequest],
            compliance.RepeatResponse]:
        return self._RepeatDataQuery(self._session, self._host)  # type: ignore

    @property
    def repeat_data_simple_path(self) -> Callable[
            [compliance.RepeatRequest],
            compliance.RepeatResponse]:
        return self._RepeatDataSimplePath(self._session, self._host)  # type: ignore

    @property
    def verify_enum(self) -> Callable[
            [compliance.EnumResponse],
            compliance.EnumResponse]:
        return self._VerifyEnum(self._session, self._host)  # type: ignore

    @property
    def kind(self) -> str:
        return "rest_asyncio"

    async def close(self):
        await self._session.close()

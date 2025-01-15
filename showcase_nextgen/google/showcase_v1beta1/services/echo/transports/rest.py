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

from google.auth.transport.requests import AuthorizedSession  # type: ignore
import json  # type: ignore
from google.auth import credentials as ga_credentials  # type: ignore
from google.api_core import exceptions as core_exceptions
from google.api_core import retry as retries
from google.api_core import rest_helpers
from google.api_core import rest_streaming
from google.api_core import gapic_v1

from google.protobuf import json_format
from google.api_core import operations_v1
from google.iam.v1 import iam_policy_pb2  # type: ignore
from google.iam.v1 import policy_pb2  # type: ignore
from google.cloud.location import locations_pb2 # type: ignore

from requests import __version__ as requests_version
import dataclasses
from typing import Any, Callable, Dict, List, Optional, Sequence, Tuple, Union
import warnings


from google.showcase_v1beta1.types import echo_pb2  # type: ignore
from google.longrunning import operations_pb2  # type: ignore


from .rest_base import _BaseEchoRestTransport
from .base import DEFAULT_CLIENT_INFO as BASE_DEFAULT_CLIENT_INFO

try:
    OptionalRetry = Union[retries.Retry, gapic_v1.method._MethodDefault, None]
except AttributeError:  # pragma: NO COVER
    OptionalRetry = Union[retries.Retry, object, None]  # type: ignore


DEFAULT_CLIENT_INFO = gapic_v1.client_info.ClientInfo(
    gapic_version=BASE_DEFAULT_CLIENT_INFO.gapic_version,
    grpc_version=None,
    rest_version=f"requests@{requests_version}",
)


class EchoRestInterceptor:
    """Interceptor for Echo.

    Interceptors are used to manipulate requests, request metadata, and responses
    in arbitrary ways.
    Example use cases include:
    * Logging
    * Verifying requests according to service or custom semantics
    * Stripping extraneous information from responses

    These use cases and more can be enabled by injecting an
    instance of a custom subclass when constructing the EchoRestTransport.

    .. code-block:: python
        class MyCustomEchoInterceptor(EchoRestInterceptor):
            def pre_block(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_block(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_echo(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_echo(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_echo_error_details(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_echo_error_details(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_expand(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_expand(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_paged_expand(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_paged_expand(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_paged_expand_legacy(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_paged_expand_legacy(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_paged_expand_legacy_mapped(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_paged_expand_legacy_mapped(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_wait(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_wait(self, response):
                logging.log(f"Received response: {response}")
                return response

        transport = EchoRestTransport(interceptor=MyCustomEchoInterceptor())
        client = EchoClient(transport=transport)


    """
    def pre_block(self, request: echo_pb2.BlockRequest, metadata: Sequence[Tuple[str, str]]) -> Tuple[echo_pb2.BlockRequest, Sequence[Tuple[str, str]]]:
        """Pre-rpc interceptor for block

        Override in a subclass to manipulate the request or metadata
        before they are sent to the Echo server.
        """
        return request, metadata

    def post_block(self, response: echo_pb2.BlockResponse) -> echo_pb2.BlockResponse:
        """Post-rpc interceptor for block

        Override in a subclass to manipulate the response
        after it is returned by the Echo server but before
        it is returned to user code.
        """
        return response

    def pre_echo(self, request: echo_pb2.EchoRequest, metadata: Sequence[Tuple[str, str]]) -> Tuple[echo_pb2.EchoRequest, Sequence[Tuple[str, str]]]:
        """Pre-rpc interceptor for echo

        Override in a subclass to manipulate the request or metadata
        before they are sent to the Echo server.
        """
        return request, metadata

    def post_echo(self, response: echo_pb2.EchoResponse) -> echo_pb2.EchoResponse:
        """Post-rpc interceptor for echo

        Override in a subclass to manipulate the response
        after it is returned by the Echo server but before
        it is returned to user code.
        """
        return response

    def pre_echo_error_details(self, request: echo_pb2.EchoErrorDetailsRequest, metadata: Sequence[Tuple[str, str]]) -> Tuple[echo_pb2.EchoErrorDetailsRequest, Sequence[Tuple[str, str]]]:
        """Pre-rpc interceptor for echo_error_details

        Override in a subclass to manipulate the request or metadata
        before they are sent to the Echo server.
        """
        return request, metadata

    def post_echo_error_details(self, response: echo_pb2.EchoErrorDetailsResponse) -> echo_pb2.EchoErrorDetailsResponse:
        """Post-rpc interceptor for echo_error_details

        Override in a subclass to manipulate the response
        after it is returned by the Echo server but before
        it is returned to user code.
        """
        return response

    def pre_expand(self, request: echo_pb2.ExpandRequest, metadata: Sequence[Tuple[str, str]]) -> Tuple[echo_pb2.ExpandRequest, Sequence[Tuple[str, str]]]:
        """Pre-rpc interceptor for expand

        Override in a subclass to manipulate the request or metadata
        before they are sent to the Echo server.
        """
        return request, metadata

    def post_expand(self, response: rest_streaming.ResponseIterator) -> rest_streaming.ResponseIterator:
        """Post-rpc interceptor for expand

        Override in a subclass to manipulate the response
        after it is returned by the Echo server but before
        it is returned to user code.
        """
        return response

    def pre_paged_expand(self, request: echo_pb2.PagedExpandRequest, metadata: Sequence[Tuple[str, str]]) -> Tuple[echo_pb2.PagedExpandRequest, Sequence[Tuple[str, str]]]:
        """Pre-rpc interceptor for paged_expand

        Override in a subclass to manipulate the request or metadata
        before they are sent to the Echo server.
        """
        return request, metadata

    def post_paged_expand(self, response: echo_pb2.PagedExpandResponse) -> echo_pb2.PagedExpandResponse:
        """Post-rpc interceptor for paged_expand

        Override in a subclass to manipulate the response
        after it is returned by the Echo server but before
        it is returned to user code.
        """
        return response

    def pre_paged_expand_legacy(self, request: echo_pb2.PagedExpandLegacyRequest, metadata: Sequence[Tuple[str, str]]) -> Tuple[echo_pb2.PagedExpandLegacyRequest, Sequence[Tuple[str, str]]]:
        """Pre-rpc interceptor for paged_expand_legacy

        Override in a subclass to manipulate the request or metadata
        before they are sent to the Echo server.
        """
        return request, metadata

    def post_paged_expand_legacy(self, response: echo_pb2.PagedExpandResponse) -> echo_pb2.PagedExpandResponse:
        """Post-rpc interceptor for paged_expand_legacy

        Override in a subclass to manipulate the response
        after it is returned by the Echo server but before
        it is returned to user code.
        """
        return response

    def pre_paged_expand_legacy_mapped(self, request: echo_pb2.PagedExpandRequest, metadata: Sequence[Tuple[str, str]]) -> Tuple[echo_pb2.PagedExpandRequest, Sequence[Tuple[str, str]]]:
        """Pre-rpc interceptor for paged_expand_legacy_mapped

        Override in a subclass to manipulate the request or metadata
        before they are sent to the Echo server.
        """
        return request, metadata

    def post_paged_expand_legacy_mapped(self, response: echo_pb2.PagedExpandLegacyMappedResponse) -> echo_pb2.PagedExpandLegacyMappedResponse:
        """Post-rpc interceptor for paged_expand_legacy_mapped

        Override in a subclass to manipulate the response
        after it is returned by the Echo server but before
        it is returned to user code.
        """
        return response

    def pre_wait(self, request: echo_pb2.WaitRequest, metadata: Sequence[Tuple[str, str]]) -> Tuple[echo_pb2.WaitRequest, Sequence[Tuple[str, str]]]:
        """Pre-rpc interceptor for wait

        Override in a subclass to manipulate the request or metadata
        before they are sent to the Echo server.
        """
        return request, metadata

    def post_wait(self, response: operations_pb2.Operation) -> operations_pb2.Operation:
        """Post-rpc interceptor for wait

        Override in a subclass to manipulate the response
        after it is returned by the Echo server but before
        it is returned to user code.
        """
        return response

    def pre_list_locations(
        self, request: locations_pb2.ListLocationsRequest, metadata: Sequence[Tuple[str, str]]
    ) -> Tuple[locations_pb2.ListLocationsRequest, Sequence[Tuple[str, str]]]:
        """Pre-rpc interceptor for list_locations

        Override in a subclass to manipulate the request or metadata
        before they are sent to the Echo server.
        """
        return request, metadata

    def post_list_locations(
        self, response: locations_pb2.ListLocationsResponse
    ) -> locations_pb2.ListLocationsResponse:
        """Post-rpc interceptor for list_locations

        Override in a subclass to manipulate the response
        after it is returned by the Echo server but before
        it is returned to user code.
        """
        return response

    def pre_get_location(
        self, request: locations_pb2.GetLocationRequest, metadata: Sequence[Tuple[str, str]]
    ) -> Tuple[locations_pb2.GetLocationRequest, Sequence[Tuple[str, str]]]:
        """Pre-rpc interceptor for get_location

        Override in a subclass to manipulate the request or metadata
        before they are sent to the Echo server.
        """
        return request, metadata

    def post_get_location(
        self, response: locations_pb2.Location
    ) -> locations_pb2.Location:
        """Post-rpc interceptor for get_location

        Override in a subclass to manipulate the response
        after it is returned by the Echo server but before
        it is returned to user code.
        """
        return response

    def pre_set_iam_policy(
        self, request: iam_policy_pb2.SetIamPolicyRequest, metadata: Sequence[Tuple[str, str]]
    ) -> Tuple[iam_policy_pb2.SetIamPolicyRequest, Sequence[Tuple[str, str]]]:
        """Pre-rpc interceptor for set_iam_policy

        Override in a subclass to manipulate the request or metadata
        before they are sent to the Echo server.
        """
        return request, metadata

    def post_set_iam_policy(
        self, response: policy_pb2.Policy
    ) -> policy_pb2.Policy:
        """Post-rpc interceptor for set_iam_policy

        Override in a subclass to manipulate the response
        after it is returned by the Echo server but before
        it is returned to user code.
        """
        return response

    def pre_get_iam_policy(
        self, request: iam_policy_pb2.GetIamPolicyRequest, metadata: Sequence[Tuple[str, str]]
    ) -> Tuple[iam_policy_pb2.GetIamPolicyRequest, Sequence[Tuple[str, str]]]:
        """Pre-rpc interceptor for get_iam_policy

        Override in a subclass to manipulate the request or metadata
        before they are sent to the Echo server.
        """
        return request, metadata

    def post_get_iam_policy(
        self, response: policy_pb2.Policy
    ) -> policy_pb2.Policy:
        """Post-rpc interceptor for get_iam_policy

        Override in a subclass to manipulate the response
        after it is returned by the Echo server but before
        it is returned to user code.
        """
        return response

    def pre_test_iam_permissions(
        self, request: iam_policy_pb2.TestIamPermissionsRequest, metadata: Sequence[Tuple[str, str]]
    ) -> Tuple[iam_policy_pb2.TestIamPermissionsRequest, Sequence[Tuple[str, str]]]:
        """Pre-rpc interceptor for test_iam_permissions

        Override in a subclass to manipulate the request or metadata
        before they are sent to the Echo server.
        """
        return request, metadata

    def post_test_iam_permissions(
        self, response: iam_policy_pb2.TestIamPermissionsResponse
    ) -> iam_policy_pb2.TestIamPermissionsResponse:
        """Post-rpc interceptor for test_iam_permissions

        Override in a subclass to manipulate the response
        after it is returned by the Echo server but before
        it is returned to user code.
        """
        return response

    def pre_list_operations(
        self, request: operations_pb2.ListOperationsRequest, metadata: Sequence[Tuple[str, str]]
    ) -> Tuple[operations_pb2.ListOperationsRequest, Sequence[Tuple[str, str]]]:
        """Pre-rpc interceptor for list_operations

        Override in a subclass to manipulate the request or metadata
        before they are sent to the Echo server.
        """
        return request, metadata

    def post_list_operations(
        self, response: operations_pb2.ListOperationsResponse
    ) -> operations_pb2.ListOperationsResponse:
        """Post-rpc interceptor for list_operations

        Override in a subclass to manipulate the response
        after it is returned by the Echo server but before
        it is returned to user code.
        """
        return response

    def pre_get_operation(
        self, request: operations_pb2.GetOperationRequest, metadata: Sequence[Tuple[str, str]]
    ) -> Tuple[operations_pb2.GetOperationRequest, Sequence[Tuple[str, str]]]:
        """Pre-rpc interceptor for get_operation

        Override in a subclass to manipulate the request or metadata
        before they are sent to the Echo server.
        """
        return request, metadata

    def post_get_operation(
        self, response: operations_pb2.Operation
    ) -> operations_pb2.Operation:
        """Post-rpc interceptor for get_operation

        Override in a subclass to manipulate the response
        after it is returned by the Echo server but before
        it is returned to user code.
        """
        return response

    def pre_delete_operation(
        self, request: operations_pb2.DeleteOperationRequest, metadata: Sequence[Tuple[str, str]]
    ) -> Tuple[operations_pb2.DeleteOperationRequest, Sequence[Tuple[str, str]]]:
        """Pre-rpc interceptor for delete_operation

        Override in a subclass to manipulate the request or metadata
        before they are sent to the Echo server.
        """
        return request, metadata

    def post_delete_operation(
        self, response: None
    ) -> None:
        """Post-rpc interceptor for delete_operation

        Override in a subclass to manipulate the response
        after it is returned by the Echo server but before
        it is returned to user code.
        """
        return response

    def pre_cancel_operation(
        self, request: operations_pb2.CancelOperationRequest, metadata: Sequence[Tuple[str, str]]
    ) -> Tuple[operations_pb2.CancelOperationRequest, Sequence[Tuple[str, str]]]:
        """Pre-rpc interceptor for cancel_operation

        Override in a subclass to manipulate the request or metadata
        before they are sent to the Echo server.
        """
        return request, metadata

    def post_cancel_operation(
        self, response: None
    ) -> None:
        """Post-rpc interceptor for cancel_operation

        Override in a subclass to manipulate the response
        after it is returned by the Echo server but before
        it is returned to user code.
        """
        return response


@dataclasses.dataclass
class EchoRestStub:
    _session: AuthorizedSession
    _host: str
    _interceptor: EchoRestInterceptor


class EchoRestTransport(_BaseEchoRestTransport):
    """REST backend synchronous transport for Echo.

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

    def __init__(self, *,
            host: str = 'localhost:7469',
            credentials: Optional[ga_credentials.Credentials] = None,
            credentials_file: Optional[str] = None,
            scopes: Optional[Sequence[str]] = None,
            client_cert_source_for_mtls: Optional[Callable[[
                ], Tuple[bytes, bytes]]] = None,
            quota_project_id: Optional[str] = None,
            client_info: gapic_v1.client_info.ClientInfo = DEFAULT_CLIENT_INFO,
            always_use_jwt_access: Optional[bool] = False,
            url_scheme: str = 'https',
            interceptor: Optional[EchoRestInterceptor] = None,
            api_audience: Optional[str] = None,
            ) -> None:
        """Instantiate the transport.

       NOTE: This REST transport functionality is currently in a beta
       state (preview). We welcome your feedback via a GitHub issue in
       this library's repository. Thank you!

        Args:
            host (Optional[str]):
                 The hostname to connect to (default: 'localhost:7469').
            credentials (Optional[google.auth.credentials.Credentials]): The
                authorization credentials to attach to requests. These
                credentials identify the application to the service; if none
                are specified, the client will attempt to ascertain the
                credentials from the environment.

            credentials_file (Optional[str]): A file with credentials that can
                be loaded with :func:`google.auth.load_credentials_from_file`.
                This argument is ignored if ``channel`` is provided.
            scopes (Optional(Sequence[str])): A list of scopes. This argument is
                ignored if ``channel`` is provided.
            client_cert_source_for_mtls (Callable[[], Tuple[bytes, bytes]]): Client
                certificate to configure mutual TLS HTTP channel. It is ignored
                if ``channel`` is provided.
            quota_project_id (Optional[str]): An optional project to use for billing
                and quota.
            client_info (google.api_core.gapic_v1.client_info.ClientInfo):
                The client info used to send a user-agent string along with
                API requests. If ``None``, then default info will be used.
                Generally, you only need to set this if you are developing
                your own client library.
            always_use_jwt_access (Optional[bool]): Whether self signed JWT should
                be used for service account credentials.
            url_scheme: the protocol scheme for the API endpoint.  Normally
                "https", but for testing or local servers,
                "http" can be specified.
        """
        # Run the base constructor
        # TODO(yon-mg): resolve other ctor params i.e. scopes, quota, etc.
        # TODO: When custom host (api_endpoint) is set, `scopes` must *also* be set on the
        # credentials object
        super().__init__(
            host=host,
            credentials=credentials,
            client_info=client_info,
            always_use_jwt_access=always_use_jwt_access,
            url_scheme=url_scheme,
            api_audience=api_audience
        )
        self._session = AuthorizedSession(
            self._credentials, default_host=self.DEFAULT_HOST)
        self._operations_client: Optional[operations_v1.AbstractOperationsClient] = None
        if client_cert_source_for_mtls:
            self._session.configure_mtls_channel(client_cert_source_for_mtls)
        self._interceptor = interceptor or EchoRestInterceptor()
        self._prep_wrapped_messages(client_info)

    @property
    def operations_client(self) -> operations_v1.AbstractOperationsClient:
        """Create the client designed to process long-running operations.

        This property caches on the instance; repeated calls return the same
        client.
        """
        # Only create a new client if we do not already have one.
        if self._operations_client is None:
            http_options: Dict[str, List[Dict[str, str]]] = {
                'google.longrunning.Operations.ListOperations': [
                    {
                        'method': 'get',
                        'uri': '/v1beta1/operations',
                    },
                ],
                'google.longrunning.Operations.GetOperation': [
                    {
                        'method': 'get',
                        'uri': '/v1beta1/{name=operations/**}',
                    },
                ],
                'google.longrunning.Operations.DeleteOperation': [
                    {
                        'method': 'delete',
                        'uri': '/v1beta1/{name=operations/**}',
                    },
                ],
                'google.longrunning.Operations.CancelOperation': [
                    {
                        'method': 'post',
                        'uri': '/v1beta1/{name=operations/**}:cancel',
                    },
                ],
            }

            rest_transport = operations_v1.OperationsRestTransport(
                    host=self._host,
                    # use the credentials which are saved
                    credentials=self._credentials,
                    scopes=self._scopes,
                    http_options=http_options,
                    path_prefix="v1beta1")

            self._operations_client = operations_v1.AbstractOperationsClient(transport=rest_transport)

        # Return the client from cache.
        return self._operations_client

    class _Block(_BaseEchoRestTransport._BaseBlock, EchoRestStub):
        def __hash__(self):
            return hash("EchoRestTransport.Block")

        @staticmethod
        def _get_response(
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
            response = getattr(session, method)(
                "{host}{uri}".format(host=host, uri=uri),
                timeout=timeout,
                headers=headers,
                params=rest_helpers.flatten_query_params(query_params, strict=True),
                data=body,
                )
            return response

        def __call__(self,
                request: echo_pb2.BlockRequest, *,
                retry: OptionalRetry=gapic_v1.method.DEFAULT,
                timeout: Optional[float]=None,
                metadata: Sequence[Tuple[str, str]]=(),
                ) -> echo_pb2.BlockResponse:
            r"""Call the block method over HTTP.

            Args:
                request (~.echo_pb2.BlockRequest):
                    The request object. The request for Block method.
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, str]]): Strings which should be
                    sent along with the request as metadata.

            Returns:
                ~.echo_pb2.BlockResponse:
                    The response for Block method.
            """

            http_options = _BaseEchoRestTransport._BaseBlock._get_http_options()
            request, metadata = self._interceptor.pre_block(request, metadata)
            transcoded_request = _BaseEchoRestTransport._BaseBlock._get_transcoded_request(http_options, request)

            body = _BaseEchoRestTransport._BaseBlock._get_request_body_json(transcoded_request)

            # Jsonify the query params
            query_params = _BaseEchoRestTransport._BaseBlock._get_query_params_json(transcoded_request)

            # Send the request
            response = EchoRestTransport._Block._get_response(self._host, metadata, query_params, self._session, timeout, transcoded_request, body)

            # In case of error, raise the appropriate core_exceptions.GoogleAPICallError exception
            # subclass.
            if response.status_code >= 400:
                raise core_exceptions.from_http_response(response)

            # Return the response
            resp = echo_pb2.BlockResponse()
            pb_resp = resp

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)
            resp = self._interceptor.post_block(resp)
            return resp

    class _Chat(_BaseEchoRestTransport._BaseChat, EchoRestStub):
        def __hash__(self):
            return hash("EchoRestTransport.Chat")

        def __call__(self,
                request: echo_pb2.EchoRequest, *,
                retry: OptionalRetry=gapic_v1.method.DEFAULT,
                timeout: Optional[float]=None,
                metadata: Sequence[Tuple[str, str]]=(),
                ) -> rest_streaming.ResponseIterator:
            raise NotImplementedError(
                "Method Chat is not available over REST transport"
            )
    class _Collect(_BaseEchoRestTransport._BaseCollect, EchoRestStub):
        def __hash__(self):
            return hash("EchoRestTransport.Collect")

        def __call__(self,
                request: echo_pb2.EchoRequest, *,
                retry: OptionalRetry=gapic_v1.method.DEFAULT,
                timeout: Optional[float]=None,
                metadata: Sequence[Tuple[str, str]]=(),
                ) -> echo_pb2.EchoResponse:
            raise NotImplementedError(
                "Method Collect is not available over REST transport"
            )
    class _Echo(_BaseEchoRestTransport._BaseEcho, EchoRestStub):
        def __hash__(self):
            return hash("EchoRestTransport.Echo")

        @staticmethod
        def _get_response(
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
            response = getattr(session, method)(
                "{host}{uri}".format(host=host, uri=uri),
                timeout=timeout,
                headers=headers,
                params=rest_helpers.flatten_query_params(query_params, strict=True),
                data=body,
                )
            return response

        def __call__(self,
                request: echo_pb2.EchoRequest, *,
                retry: OptionalRetry=gapic_v1.method.DEFAULT,
                timeout: Optional[float]=None,
                metadata: Sequence[Tuple[str, str]]=(),
                ) -> echo_pb2.EchoResponse:
            r"""Call the echo method over HTTP.

            Args:
                request (~.echo_pb2.EchoRequest):
                    The request object. The request message used for the
                Echo, Collect and Chat methods. If
                content or opt are set in this message
                then the request will succeed. If status
                is set in this message then the status
                will be returned as an error.
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, str]]): Strings which should be
                    sent along with the request as metadata.

            Returns:
                ~.echo_pb2.EchoResponse:
                    The response message for the Echo
                methods.

            """

            http_options = _BaseEchoRestTransport._BaseEcho._get_http_options()
            request, metadata = self._interceptor.pre_echo(request, metadata)
            transcoded_request = _BaseEchoRestTransport._BaseEcho._get_transcoded_request(http_options, request)

            body = _BaseEchoRestTransport._BaseEcho._get_request_body_json(transcoded_request)

            # Jsonify the query params
            query_params = _BaseEchoRestTransport._BaseEcho._get_query_params_json(transcoded_request)

            # Send the request
            response = EchoRestTransport._Echo._get_response(self._host, metadata, query_params, self._session, timeout, transcoded_request, body)

            # In case of error, raise the appropriate core_exceptions.GoogleAPICallError exception
            # subclass.
            if response.status_code >= 400:
                raise core_exceptions.from_http_response(response)

            # Return the response
            resp = echo_pb2.EchoResponse()
            pb_resp = resp

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)
            resp = self._interceptor.post_echo(resp)
            return resp

    class _EchoErrorDetails(_BaseEchoRestTransport._BaseEchoErrorDetails, EchoRestStub):
        def __hash__(self):
            return hash("EchoRestTransport.EchoErrorDetails")

        @staticmethod
        def _get_response(
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
            response = getattr(session, method)(
                "{host}{uri}".format(host=host, uri=uri),
                timeout=timeout,
                headers=headers,
                params=rest_helpers.flatten_query_params(query_params, strict=True),
                data=body,
                )
            return response

        def __call__(self,
                request: echo_pb2.EchoErrorDetailsRequest, *,
                retry: OptionalRetry=gapic_v1.method.DEFAULT,
                timeout: Optional[float]=None,
                metadata: Sequence[Tuple[str, str]]=(),
                ) -> echo_pb2.EchoErrorDetailsResponse:
            r"""Call the echo error details method over HTTP.

            Args:
                request (~.echo_pb2.EchoErrorDetailsRequest):
                    The request object. The request message used for the
                EchoErrorDetails method.
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, str]]): Strings which should be
                    sent along with the request as metadata.

            Returns:
                ~.echo_pb2.EchoErrorDetailsResponse:
                    The response message used for the
                EchoErrorDetails method.

            """

            http_options = _BaseEchoRestTransport._BaseEchoErrorDetails._get_http_options()
            request, metadata = self._interceptor.pre_echo_error_details(request, metadata)
            transcoded_request = _BaseEchoRestTransport._BaseEchoErrorDetails._get_transcoded_request(http_options, request)

            body = _BaseEchoRestTransport._BaseEchoErrorDetails._get_request_body_json(transcoded_request)

            # Jsonify the query params
            query_params = _BaseEchoRestTransport._BaseEchoErrorDetails._get_query_params_json(transcoded_request)

            # Send the request
            response = EchoRestTransport._EchoErrorDetails._get_response(self._host, metadata, query_params, self._session, timeout, transcoded_request, body)

            # In case of error, raise the appropriate core_exceptions.GoogleAPICallError exception
            # subclass.
            if response.status_code >= 400:
                raise core_exceptions.from_http_response(response)

            # Return the response
            resp = echo_pb2.EchoErrorDetailsResponse()
            pb_resp = resp

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)
            resp = self._interceptor.post_echo_error_details(resp)
            return resp

    class _Expand(_BaseEchoRestTransport._BaseExpand, EchoRestStub):
        def __hash__(self):
            return hash("EchoRestTransport.Expand")

        @staticmethod
        def _get_response(
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
            response = getattr(session, method)(
                "{host}{uri}".format(host=host, uri=uri),
                timeout=timeout,
                headers=headers,
                params=rest_helpers.flatten_query_params(query_params, strict=True),
                data=body,
                stream=True,
                )
            return response

        def __call__(self,
                request: echo_pb2.ExpandRequest, *,
                retry: OptionalRetry=gapic_v1.method.DEFAULT,
                timeout: Optional[float]=None,
                metadata: Sequence[Tuple[str, str]]=(),
                ) -> rest_streaming.ResponseIterator:
            r"""Call the expand method over HTTP.

            Args:
                request (~.echo_pb2.ExpandRequest):
                    The request object. The request message for the Expand
                method.
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, str]]): Strings which should be
                    sent along with the request as metadata.

            Returns:
                ~.echo_pb2.EchoResponse:
                    The response message for the Echo
                methods.

            """

            http_options = _BaseEchoRestTransport._BaseExpand._get_http_options()
            request, metadata = self._interceptor.pre_expand(request, metadata)
            transcoded_request = _BaseEchoRestTransport._BaseExpand._get_transcoded_request(http_options, request)

            body = _BaseEchoRestTransport._BaseExpand._get_request_body_json(transcoded_request)

            # Jsonify the query params
            query_params = _BaseEchoRestTransport._BaseExpand._get_query_params_json(transcoded_request)

            # Send the request
            response = EchoRestTransport._Expand._get_response(self._host, metadata, query_params, self._session, timeout, transcoded_request, body)

            # In case of error, raise the appropriate core_exceptions.GoogleAPICallError exception
            # subclass.
            if response.status_code >= 400:
                raise core_exceptions.from_http_response(response)

            # Return the response
            resp = rest_streaming.ResponseIterator(response, echo_pb2.EchoResponse)
            resp = self._interceptor.post_expand(resp)
            return resp

    class _PagedExpand(_BaseEchoRestTransport._BasePagedExpand, EchoRestStub):
        def __hash__(self):
            return hash("EchoRestTransport.PagedExpand")

        @staticmethod
        def _get_response(
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
            response = getattr(session, method)(
                "{host}{uri}".format(host=host, uri=uri),
                timeout=timeout,
                headers=headers,
                params=rest_helpers.flatten_query_params(query_params, strict=True),
                data=body,
                )
            return response

        def __call__(self,
                request: echo_pb2.PagedExpandRequest, *,
                retry: OptionalRetry=gapic_v1.method.DEFAULT,
                timeout: Optional[float]=None,
                metadata: Sequence[Tuple[str, str]]=(),
                ) -> echo_pb2.PagedExpandResponse:
            r"""Call the paged expand method over HTTP.

            Args:
                request (~.echo_pb2.PagedExpandRequest):
                    The request object. The request for the PagedExpand
                method.
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, str]]): Strings which should be
                    sent along with the request as metadata.

            Returns:
                ~.echo_pb2.PagedExpandResponse:
                    The response for the PagedExpand
                method.

            """

            http_options = _BaseEchoRestTransport._BasePagedExpand._get_http_options()
            request, metadata = self._interceptor.pre_paged_expand(request, metadata)
            transcoded_request = _BaseEchoRestTransport._BasePagedExpand._get_transcoded_request(http_options, request)

            body = _BaseEchoRestTransport._BasePagedExpand._get_request_body_json(transcoded_request)

            # Jsonify the query params
            query_params = _BaseEchoRestTransport._BasePagedExpand._get_query_params_json(transcoded_request)

            # Send the request
            response = EchoRestTransport._PagedExpand._get_response(self._host, metadata, query_params, self._session, timeout, transcoded_request, body)

            # In case of error, raise the appropriate core_exceptions.GoogleAPICallError exception
            # subclass.
            if response.status_code >= 400:
                raise core_exceptions.from_http_response(response)

            # Return the response
            resp = echo_pb2.PagedExpandResponse()
            pb_resp = resp

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)
            resp = self._interceptor.post_paged_expand(resp)
            return resp

    class _PagedExpandLegacy(_BaseEchoRestTransport._BasePagedExpandLegacy, EchoRestStub):
        def __hash__(self):
            return hash("EchoRestTransport.PagedExpandLegacy")

        @staticmethod
        def _get_response(
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
            response = getattr(session, method)(
                "{host}{uri}".format(host=host, uri=uri),
                timeout=timeout,
                headers=headers,
                params=rest_helpers.flatten_query_params(query_params, strict=True),
                data=body,
                )
            return response

        def __call__(self,
                request: echo_pb2.PagedExpandLegacyRequest, *,
                retry: OptionalRetry=gapic_v1.method.DEFAULT,
                timeout: Optional[float]=None,
                metadata: Sequence[Tuple[str, str]]=(),
                ) -> echo_pb2.PagedExpandResponse:
            r"""Call the paged expand legacy method over HTTP.

            Args:
                request (~.echo_pb2.PagedExpandLegacyRequest):
                    The request object. The request for the PagedExpandLegacy
                method.  This is a pattern used by some
                legacy APIs. New APIs should NOT use
                this pattern, but rather something like
                PagedExpandRequest which conforms to
                aip.dev/158.
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, str]]): Strings which should be
                    sent along with the request as metadata.

            Returns:
                ~.echo_pb2.PagedExpandResponse:
                    The response for the PagedExpand
                method.

            """

            http_options = _BaseEchoRestTransport._BasePagedExpandLegacy._get_http_options()
            request, metadata = self._interceptor.pre_paged_expand_legacy(request, metadata)
            transcoded_request = _BaseEchoRestTransport._BasePagedExpandLegacy._get_transcoded_request(http_options, request)

            body = _BaseEchoRestTransport._BasePagedExpandLegacy._get_request_body_json(transcoded_request)

            # Jsonify the query params
            query_params = _BaseEchoRestTransport._BasePagedExpandLegacy._get_query_params_json(transcoded_request)

            # Send the request
            response = EchoRestTransport._PagedExpandLegacy._get_response(self._host, metadata, query_params, self._session, timeout, transcoded_request, body)

            # In case of error, raise the appropriate core_exceptions.GoogleAPICallError exception
            # subclass.
            if response.status_code >= 400:
                raise core_exceptions.from_http_response(response)

            # Return the response
            resp = echo_pb2.PagedExpandResponse()
            pb_resp = resp

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)
            resp = self._interceptor.post_paged_expand_legacy(resp)
            return resp

    class _PagedExpandLegacyMapped(_BaseEchoRestTransport._BasePagedExpandLegacyMapped, EchoRestStub):
        def __hash__(self):
            return hash("EchoRestTransport.PagedExpandLegacyMapped")

        @staticmethod
        def _get_response(
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
            response = getattr(session, method)(
                "{host}{uri}".format(host=host, uri=uri),
                timeout=timeout,
                headers=headers,
                params=rest_helpers.flatten_query_params(query_params, strict=True),
                data=body,
                )
            return response

        def __call__(self,
                request: echo_pb2.PagedExpandRequest, *,
                retry: OptionalRetry=gapic_v1.method.DEFAULT,
                timeout: Optional[float]=None,
                metadata: Sequence[Tuple[str, str]]=(),
                ) -> echo_pb2.PagedExpandLegacyMappedResponse:
            r"""Call the paged expand legacy
        mapped method over HTTP.

            Args:
                request (~.echo_pb2.PagedExpandRequest):
                    The request object. The request for the PagedExpand
                method.
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, str]]): Strings which should be
                    sent along with the request as metadata.

            Returns:
                ~.echo_pb2.PagedExpandLegacyMappedResponse:

            """

            http_options = _BaseEchoRestTransport._BasePagedExpandLegacyMapped._get_http_options()
            request, metadata = self._interceptor.pre_paged_expand_legacy_mapped(request, metadata)
            transcoded_request = _BaseEchoRestTransport._BasePagedExpandLegacyMapped._get_transcoded_request(http_options, request)

            body = _BaseEchoRestTransport._BasePagedExpandLegacyMapped._get_request_body_json(transcoded_request)

            # Jsonify the query params
            query_params = _BaseEchoRestTransport._BasePagedExpandLegacyMapped._get_query_params_json(transcoded_request)

            # Send the request
            response = EchoRestTransport._PagedExpandLegacyMapped._get_response(self._host, metadata, query_params, self._session, timeout, transcoded_request, body)

            # In case of error, raise the appropriate core_exceptions.GoogleAPICallError exception
            # subclass.
            if response.status_code >= 400:
                raise core_exceptions.from_http_response(response)

            # Return the response
            resp = echo_pb2.PagedExpandLegacyMappedResponse()
            pb_resp = resp

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)
            resp = self._interceptor.post_paged_expand_legacy_mapped(resp)
            return resp

    class _Wait(_BaseEchoRestTransport._BaseWait, EchoRestStub):
        def __hash__(self):
            return hash("EchoRestTransport.Wait")

        @staticmethod
        def _get_response(
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
            response = getattr(session, method)(
                "{host}{uri}".format(host=host, uri=uri),
                timeout=timeout,
                headers=headers,
                params=rest_helpers.flatten_query_params(query_params, strict=True),
                data=body,
                )
            return response

        def __call__(self,
                request: echo_pb2.WaitRequest, *,
                retry: OptionalRetry=gapic_v1.method.DEFAULT,
                timeout: Optional[float]=None,
                metadata: Sequence[Tuple[str, str]]=(),
                ) -> operations_pb2.Operation:
            r"""Call the wait method over HTTP.

            Args:
                request (~.echo_pb2.WaitRequest):
                    The request object. The request for Wait method.
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, str]]): Strings which should be
                    sent along with the request as metadata.

            Returns:
                ~.operations_pb2.Operation:
                    This resource represents a
                long-running operation that is the
                result of a network API call.

            """

            http_options = _BaseEchoRestTransport._BaseWait._get_http_options()
            request, metadata = self._interceptor.pre_wait(request, metadata)
            transcoded_request = _BaseEchoRestTransport._BaseWait._get_transcoded_request(http_options, request)

            body = _BaseEchoRestTransport._BaseWait._get_request_body_json(transcoded_request)

            # Jsonify the query params
            query_params = _BaseEchoRestTransport._BaseWait._get_query_params_json(transcoded_request)

            # Send the request
            response = EchoRestTransport._Wait._get_response(self._host, metadata, query_params, self._session, timeout, transcoded_request, body)

            # In case of error, raise the appropriate core_exceptions.GoogleAPICallError exception
            # subclass.
            if response.status_code >= 400:
                raise core_exceptions.from_http_response(response)

            # Return the response
            resp = operations_pb2.Operation()
            json_format.Parse(response.content, resp, ignore_unknown_fields=True)
            resp = self._interceptor.post_wait(resp)
            return resp

    @property
    def block(self) -> Callable[
            [echo_pb2.BlockRequest],
            echo_pb2.BlockResponse]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._Block(self._session, self._host, self._interceptor) # type: ignore

    @property
    def chat(self) -> Callable[
            [echo_pb2.EchoRequest],
            echo_pb2.EchoResponse]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._Chat(self._session, self._host, self._interceptor) # type: ignore

    @property
    def collect(self) -> Callable[
            [echo_pb2.EchoRequest],
            echo_pb2.EchoResponse]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._Collect(self._session, self._host, self._interceptor) # type: ignore

    @property
    def echo(self) -> Callable[
            [echo_pb2.EchoRequest],
            echo_pb2.EchoResponse]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._Echo(self._session, self._host, self._interceptor) # type: ignore

    @property
    def echo_error_details(self) -> Callable[
            [echo_pb2.EchoErrorDetailsRequest],
            echo_pb2.EchoErrorDetailsResponse]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._EchoErrorDetails(self._session, self._host, self._interceptor) # type: ignore

    @property
    def expand(self) -> Callable[
            [echo_pb2.ExpandRequest],
            echo_pb2.EchoResponse]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._Expand(self._session, self._host, self._interceptor) # type: ignore

    @property
    def paged_expand(self) -> Callable[
            [echo_pb2.PagedExpandRequest],
            echo_pb2.PagedExpandResponse]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._PagedExpand(self._session, self._host, self._interceptor) # type: ignore

    @property
    def paged_expand_legacy(self) -> Callable[
            [echo_pb2.PagedExpandLegacyRequest],
            echo_pb2.PagedExpandResponse]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._PagedExpandLegacy(self._session, self._host, self._interceptor) # type: ignore

    @property
    def paged_expand_legacy_mapped(self) -> Callable[
            [echo_pb2.PagedExpandRequest],
            echo_pb2.PagedExpandLegacyMappedResponse]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._PagedExpandLegacyMapped(self._session, self._host, self._interceptor) # type: ignore

    @property
    def wait(self) -> Callable[
            [echo_pb2.WaitRequest],
            operations_pb2.Operation]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._Wait(self._session, self._host, self._interceptor) # type: ignore

    @property
    def list_locations(self):
        return self._ListLocations(self._session, self._host, self._interceptor) # type: ignore

    class _ListLocations(_BaseEchoRestTransport._BaseListLocations, EchoRestStub):
        def __hash__(self):
            return hash("EchoRestTransport.ListLocations")

        @staticmethod
        def _get_response(
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
            response = getattr(session, method)(
                "{host}{uri}".format(host=host, uri=uri),
                timeout=timeout,
                headers=headers,
                params=rest_helpers.flatten_query_params(query_params, strict=True),
                )
            return response

        def __call__(self,
            request: locations_pb2.ListLocationsRequest, *,
            retry: OptionalRetry=gapic_v1.method.DEFAULT,
            timeout: Optional[float]=None,
            metadata: Sequence[Tuple[str, str]]=(),
            ) -> locations_pb2.ListLocationsResponse:

            r"""Call the list locations method over HTTP.

            Args:
                request (locations_pb2.ListLocationsRequest):
                    The request object for ListLocations method.
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, str]]): Strings which should be
                    sent along with the request as metadata.

            Returns:
                locations_pb2.ListLocationsResponse: Response from ListLocations method.
            """

            http_options = _BaseEchoRestTransport._BaseListLocations._get_http_options()
            request, metadata = self._interceptor.pre_list_locations(request, metadata)
            transcoded_request = _BaseEchoRestTransport._BaseListLocations._get_transcoded_request(http_options, request)

            # Jsonify the query params
            query_params = _BaseEchoRestTransport._BaseListLocations._get_query_params_json(transcoded_request)

            # Send the request
            response = EchoRestTransport._ListLocations._get_response(self._host, metadata, query_params, self._session, timeout, transcoded_request)

            # In case of error, raise the appropriate core_exceptions.GoogleAPICallError exception
            # subclass.
            if response.status_code >= 400:
                raise core_exceptions.from_http_response(response)

            content = response.content.decode("utf-8")
            resp = locations_pb2.ListLocationsResponse()
            resp = json_format.Parse(content, resp)
            resp = self._interceptor.post_list_locations(resp)
            return resp

    @property
    def get_location(self):
        return self._GetLocation(self._session, self._host, self._interceptor) # type: ignore

    class _GetLocation(_BaseEchoRestTransport._BaseGetLocation, EchoRestStub):
        def __hash__(self):
            return hash("EchoRestTransport.GetLocation")

        @staticmethod
        def _get_response(
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
            response = getattr(session, method)(
                "{host}{uri}".format(host=host, uri=uri),
                timeout=timeout,
                headers=headers,
                params=rest_helpers.flatten_query_params(query_params, strict=True),
                )
            return response

        def __call__(self,
            request: locations_pb2.GetLocationRequest, *,
            retry: OptionalRetry=gapic_v1.method.DEFAULT,
            timeout: Optional[float]=None,
            metadata: Sequence[Tuple[str, str]]=(),
            ) -> locations_pb2.Location:

            r"""Call the get location method over HTTP.

            Args:
                request (locations_pb2.GetLocationRequest):
                    The request object for GetLocation method.
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, str]]): Strings which should be
                    sent along with the request as metadata.

            Returns:
                locations_pb2.Location: Response from GetLocation method.
            """

            http_options = _BaseEchoRestTransport._BaseGetLocation._get_http_options()
            request, metadata = self._interceptor.pre_get_location(request, metadata)
            transcoded_request = _BaseEchoRestTransport._BaseGetLocation._get_transcoded_request(http_options, request)

            # Jsonify the query params
            query_params = _BaseEchoRestTransport._BaseGetLocation._get_query_params_json(transcoded_request)

            # Send the request
            response = EchoRestTransport._GetLocation._get_response(self._host, metadata, query_params, self._session, timeout, transcoded_request)

            # In case of error, raise the appropriate core_exceptions.GoogleAPICallError exception
            # subclass.
            if response.status_code >= 400:
                raise core_exceptions.from_http_response(response)

            content = response.content.decode("utf-8")
            resp = locations_pb2.Location()
            resp = json_format.Parse(content, resp)
            resp = self._interceptor.post_get_location(resp)
            return resp

    @property
    def set_iam_policy(self):
        return self._SetIamPolicy(self._session, self._host, self._interceptor) # type: ignore

    class _SetIamPolicy(_BaseEchoRestTransport._BaseSetIamPolicy, EchoRestStub):
        def __hash__(self):
            return hash("EchoRestTransport.SetIamPolicy")

        @staticmethod
        def _get_response(
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
            response = getattr(session, method)(
                "{host}{uri}".format(host=host, uri=uri),
                timeout=timeout,
                headers=headers,
                params=rest_helpers.flatten_query_params(query_params, strict=True),
                data=body,
                )
            return response

        def __call__(self,
            request: iam_policy_pb2.SetIamPolicyRequest, *,
            retry: OptionalRetry=gapic_v1.method.DEFAULT,
            timeout: Optional[float]=None,
            metadata: Sequence[Tuple[str, str]]=(),
            ) -> policy_pb2.Policy:

            r"""Call the set iam policy method over HTTP.

            Args:
                request (iam_policy_pb2.SetIamPolicyRequest):
                    The request object for SetIamPolicy method.
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, str]]): Strings which should be
                    sent along with the request as metadata.

            Returns:
                policy_pb2.Policy: Response from SetIamPolicy method.
            """

            http_options = _BaseEchoRestTransport._BaseSetIamPolicy._get_http_options()
            request, metadata = self._interceptor.pre_set_iam_policy(request, metadata)
            transcoded_request = _BaseEchoRestTransport._BaseSetIamPolicy._get_transcoded_request(http_options, request)

            body = _BaseEchoRestTransport._BaseSetIamPolicy._get_request_body_json(transcoded_request)

            # Jsonify the query params
            query_params = _BaseEchoRestTransport._BaseSetIamPolicy._get_query_params_json(transcoded_request)

            # Send the request
            response = EchoRestTransport._SetIamPolicy._get_response(self._host, metadata, query_params, self._session, timeout, transcoded_request, body)

            # In case of error, raise the appropriate core_exceptions.GoogleAPICallError exception
            # subclass.
            if response.status_code >= 400:
                raise core_exceptions.from_http_response(response)

            content = response.content.decode("utf-8")
            resp = policy_pb2.Policy()
            resp = json_format.Parse(content, resp)
            resp = self._interceptor.post_set_iam_policy(resp)
            return resp

    @property
    def get_iam_policy(self):
        return self._GetIamPolicy(self._session, self._host, self._interceptor) # type: ignore

    class _GetIamPolicy(_BaseEchoRestTransport._BaseGetIamPolicy, EchoRestStub):
        def __hash__(self):
            return hash("EchoRestTransport.GetIamPolicy")

        @staticmethod
        def _get_response(
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
            response = getattr(session, method)(
                "{host}{uri}".format(host=host, uri=uri),
                timeout=timeout,
                headers=headers,
                params=rest_helpers.flatten_query_params(query_params, strict=True),
                )
            return response

        def __call__(self,
            request: iam_policy_pb2.GetIamPolicyRequest, *,
            retry: OptionalRetry=gapic_v1.method.DEFAULT,
            timeout: Optional[float]=None,
            metadata: Sequence[Tuple[str, str]]=(),
            ) -> policy_pb2.Policy:

            r"""Call the get iam policy method over HTTP.

            Args:
                request (iam_policy_pb2.GetIamPolicyRequest):
                    The request object for GetIamPolicy method.
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, str]]): Strings which should be
                    sent along with the request as metadata.

            Returns:
                policy_pb2.Policy: Response from GetIamPolicy method.
            """

            http_options = _BaseEchoRestTransport._BaseGetIamPolicy._get_http_options()
            request, metadata = self._interceptor.pre_get_iam_policy(request, metadata)
            transcoded_request = _BaseEchoRestTransport._BaseGetIamPolicy._get_transcoded_request(http_options, request)

            # Jsonify the query params
            query_params = _BaseEchoRestTransport._BaseGetIamPolicy._get_query_params_json(transcoded_request)

            # Send the request
            response = EchoRestTransport._GetIamPolicy._get_response(self._host, metadata, query_params, self._session, timeout, transcoded_request)

            # In case of error, raise the appropriate core_exceptions.GoogleAPICallError exception
            # subclass.
            if response.status_code >= 400:
                raise core_exceptions.from_http_response(response)

            content = response.content.decode("utf-8")
            resp = policy_pb2.Policy()
            resp = json_format.Parse(content, resp)
            resp = self._interceptor.post_get_iam_policy(resp)
            return resp

    @property
    def test_iam_permissions(self):
        return self._TestIamPermissions(self._session, self._host, self._interceptor) # type: ignore

    class _TestIamPermissions(_BaseEchoRestTransport._BaseTestIamPermissions, EchoRestStub):
        def __hash__(self):
            return hash("EchoRestTransport.TestIamPermissions")

        @staticmethod
        def _get_response(
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
            response = getattr(session, method)(
                "{host}{uri}".format(host=host, uri=uri),
                timeout=timeout,
                headers=headers,
                params=rest_helpers.flatten_query_params(query_params, strict=True),
                data=body,
                )
            return response

        def __call__(self,
            request: iam_policy_pb2.TestIamPermissionsRequest, *,
            retry: OptionalRetry=gapic_v1.method.DEFAULT,
            timeout: Optional[float]=None,
            metadata: Sequence[Tuple[str, str]]=(),
            ) -> iam_policy_pb2.TestIamPermissionsResponse:

            r"""Call the test iam permissions method over HTTP.

            Args:
                request (iam_policy_pb2.TestIamPermissionsRequest):
                    The request object for TestIamPermissions method.
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, str]]): Strings which should be
                    sent along with the request as metadata.

            Returns:
                iam_policy_pb2.TestIamPermissionsResponse: Response from TestIamPermissions method.
            """

            http_options = _BaseEchoRestTransport._BaseTestIamPermissions._get_http_options()
            request, metadata = self._interceptor.pre_test_iam_permissions(request, metadata)
            transcoded_request = _BaseEchoRestTransport._BaseTestIamPermissions._get_transcoded_request(http_options, request)

            body = _BaseEchoRestTransport._BaseTestIamPermissions._get_request_body_json(transcoded_request)

            # Jsonify the query params
            query_params = _BaseEchoRestTransport._BaseTestIamPermissions._get_query_params_json(transcoded_request)

            # Send the request
            response = EchoRestTransport._TestIamPermissions._get_response(self._host, metadata, query_params, self._session, timeout, transcoded_request, body)

            # In case of error, raise the appropriate core_exceptions.GoogleAPICallError exception
            # subclass.
            if response.status_code >= 400:
                raise core_exceptions.from_http_response(response)

            content = response.content.decode("utf-8")
            resp = iam_policy_pb2.TestIamPermissionsResponse()
            resp = json_format.Parse(content, resp)
            resp = self._interceptor.post_test_iam_permissions(resp)
            return resp

    @property
    def list_operations(self):
        return self._ListOperations(self._session, self._host, self._interceptor) # type: ignore

    class _ListOperations(_BaseEchoRestTransport._BaseListOperations, EchoRestStub):
        def __hash__(self):
            return hash("EchoRestTransport.ListOperations")

        @staticmethod
        def _get_response(
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
            response = getattr(session, method)(
                "{host}{uri}".format(host=host, uri=uri),
                timeout=timeout,
                headers=headers,
                params=rest_helpers.flatten_query_params(query_params, strict=True),
                )
            return response

        def __call__(self,
            request: operations_pb2.ListOperationsRequest, *,
            retry: OptionalRetry=gapic_v1.method.DEFAULT,
            timeout: Optional[float]=None,
            metadata: Sequence[Tuple[str, str]]=(),
            ) -> operations_pb2.ListOperationsResponse:

            r"""Call the list operations method over HTTP.

            Args:
                request (operations_pb2.ListOperationsRequest):
                    The request object for ListOperations method.
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, str]]): Strings which should be
                    sent along with the request as metadata.

            Returns:
                operations_pb2.ListOperationsResponse: Response from ListOperations method.
            """

            http_options = _BaseEchoRestTransport._BaseListOperations._get_http_options()
            request, metadata = self._interceptor.pre_list_operations(request, metadata)
            transcoded_request = _BaseEchoRestTransport._BaseListOperations._get_transcoded_request(http_options, request)

            # Jsonify the query params
            query_params = _BaseEchoRestTransport._BaseListOperations._get_query_params_json(transcoded_request)

            # Send the request
            response = EchoRestTransport._ListOperations._get_response(self._host, metadata, query_params, self._session, timeout, transcoded_request)

            # In case of error, raise the appropriate core_exceptions.GoogleAPICallError exception
            # subclass.
            if response.status_code >= 400:
                raise core_exceptions.from_http_response(response)

            content = response.content.decode("utf-8")
            resp = operations_pb2.ListOperationsResponse()
            resp = json_format.Parse(content, resp)
            resp = self._interceptor.post_list_operations(resp)
            return resp

    @property
    def get_operation(self):
        return self._GetOperation(self._session, self._host, self._interceptor) # type: ignore

    class _GetOperation(_BaseEchoRestTransport._BaseGetOperation, EchoRestStub):
        def __hash__(self):
            return hash("EchoRestTransport.GetOperation")

        @staticmethod
        def _get_response(
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
            response = getattr(session, method)(
                "{host}{uri}".format(host=host, uri=uri),
                timeout=timeout,
                headers=headers,
                params=rest_helpers.flatten_query_params(query_params, strict=True),
                )
            return response

        def __call__(self,
            request: operations_pb2.GetOperationRequest, *,
            retry: OptionalRetry=gapic_v1.method.DEFAULT,
            timeout: Optional[float]=None,
            metadata: Sequence[Tuple[str, str]]=(),
            ) -> operations_pb2.Operation:

            r"""Call the get operation method over HTTP.

            Args:
                request (operations_pb2.GetOperationRequest):
                    The request object for GetOperation method.
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, str]]): Strings which should be
                    sent along with the request as metadata.

            Returns:
                operations_pb2.Operation: Response from GetOperation method.
            """

            http_options = _BaseEchoRestTransport._BaseGetOperation._get_http_options()
            request, metadata = self._interceptor.pre_get_operation(request, metadata)
            transcoded_request = _BaseEchoRestTransport._BaseGetOperation._get_transcoded_request(http_options, request)

            # Jsonify the query params
            query_params = _BaseEchoRestTransport._BaseGetOperation._get_query_params_json(transcoded_request)

            # Send the request
            response = EchoRestTransport._GetOperation._get_response(self._host, metadata, query_params, self._session, timeout, transcoded_request)

            # In case of error, raise the appropriate core_exceptions.GoogleAPICallError exception
            # subclass.
            if response.status_code >= 400:
                raise core_exceptions.from_http_response(response)

            content = response.content.decode("utf-8")
            resp = operations_pb2.Operation()
            resp = json_format.Parse(content, resp)
            resp = self._interceptor.post_get_operation(resp)
            return resp

    @property
    def delete_operation(self):
        return self._DeleteOperation(self._session, self._host, self._interceptor) # type: ignore

    class _DeleteOperation(_BaseEchoRestTransport._BaseDeleteOperation, EchoRestStub):
        def __hash__(self):
            return hash("EchoRestTransport.DeleteOperation")

        @staticmethod
        def _get_response(
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
            response = getattr(session, method)(
                "{host}{uri}".format(host=host, uri=uri),
                timeout=timeout,
                headers=headers,
                params=rest_helpers.flatten_query_params(query_params, strict=True),
                )
            return response

        def __call__(self,
            request: operations_pb2.DeleteOperationRequest, *,
            retry: OptionalRetry=gapic_v1.method.DEFAULT,
            timeout: Optional[float]=None,
            metadata: Sequence[Tuple[str, str]]=(),
            ) -> None:

            r"""Call the delete operation method over HTTP.

            Args:
                request (operations_pb2.DeleteOperationRequest):
                    The request object for DeleteOperation method.
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, str]]): Strings which should be
                    sent along with the request as metadata.
            """

            http_options = _BaseEchoRestTransport._BaseDeleteOperation._get_http_options()
            request, metadata = self._interceptor.pre_delete_operation(request, metadata)
            transcoded_request = _BaseEchoRestTransport._BaseDeleteOperation._get_transcoded_request(http_options, request)

            # Jsonify the query params
            query_params = _BaseEchoRestTransport._BaseDeleteOperation._get_query_params_json(transcoded_request)

            # Send the request
            response = EchoRestTransport._DeleteOperation._get_response(self._host, metadata, query_params, self._session, timeout, transcoded_request)

            # In case of error, raise the appropriate core_exceptions.GoogleAPICallError exception
            # subclass.
            if response.status_code >= 400:
                raise core_exceptions.from_http_response(response)

            return self._interceptor.post_delete_operation(None)

    @property
    def cancel_operation(self):
        return self._CancelOperation(self._session, self._host, self._interceptor) # type: ignore

    class _CancelOperation(_BaseEchoRestTransport._BaseCancelOperation, EchoRestStub):
        def __hash__(self):
            return hash("EchoRestTransport.CancelOperation")

        @staticmethod
        def _get_response(
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
            response = getattr(session, method)(
                "{host}{uri}".format(host=host, uri=uri),
                timeout=timeout,
                headers=headers,
                params=rest_helpers.flatten_query_params(query_params, strict=True),
                )
            return response

        def __call__(self,
            request: operations_pb2.CancelOperationRequest, *,
            retry: OptionalRetry=gapic_v1.method.DEFAULT,
            timeout: Optional[float]=None,
            metadata: Sequence[Tuple[str, str]]=(),
            ) -> None:

            r"""Call the cancel operation method over HTTP.

            Args:
                request (operations_pb2.CancelOperationRequest):
                    The request object for CancelOperation method.
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, str]]): Strings which should be
                    sent along with the request as metadata.
            """

            http_options = _BaseEchoRestTransport._BaseCancelOperation._get_http_options()
            request, metadata = self._interceptor.pre_cancel_operation(request, metadata)
            transcoded_request = _BaseEchoRestTransport._BaseCancelOperation._get_transcoded_request(http_options, request)

            # Jsonify the query params
            query_params = _BaseEchoRestTransport._BaseCancelOperation._get_query_params_json(transcoded_request)

            # Send the request
            response = EchoRestTransport._CancelOperation._get_response(self._host, metadata, query_params, self._session, timeout, transcoded_request)

            # In case of error, raise the appropriate core_exceptions.GoogleAPICallError exception
            # subclass.
            if response.status_code >= 400:
                raise core_exceptions.from_http_response(response)

            return self._interceptor.post_cancel_operation(None)

    @property
    def kind(self) -> str:
        return "rest"

    def close(self):
        self._session.close()


__all__=(
    'EchoRestTransport',
)

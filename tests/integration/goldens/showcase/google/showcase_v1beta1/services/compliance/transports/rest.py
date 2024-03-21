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
import grpc  # type: ignore
from google.auth.transport.grpc import SslCredentials  # type: ignore
from google.auth import credentials as ga_credentials  # type: ignore
from google.api_core import exceptions as core_exceptions
from google.api_core import retry as retries
from google.api_core import rest_helpers
from google.api_core import rest_streaming
from google.api_core import path_template
from google.api_core import gapic_v1

from google.protobuf import json_format
from google.iam.v1 import iam_policy_pb2  # type: ignore
from google.iam.v1 import policy_pb2  # type: ignore
from google.cloud.location import locations_pb2 # type: ignore
from requests import __version__ as requests_version
import dataclasses
import re
from typing import Any, Callable, Dict, List, Optional, Sequence, Tuple, Union
import warnings

try:
    OptionalRetry = Union[retries.Retry, gapic_v1.method._MethodDefault, None]
except AttributeError:  # pragma: NO COVER
    OptionalRetry = Union[retries.Retry, object, None]  # type: ignore


from google.showcase_v1beta1.types import compliance
from google.longrunning import operations_pb2  # type: ignore

from .base import ComplianceTransport, DEFAULT_CLIENT_INFO as BASE_DEFAULT_CLIENT_INFO


DEFAULT_CLIENT_INFO = gapic_v1.client_info.ClientInfo(
    gapic_version=BASE_DEFAULT_CLIENT_INFO.gapic_version,
    grpc_version=None,
    rest_version=requests_version,
)


class ComplianceRestInterceptor:
    """Interceptor for Compliance.

    Interceptors are used to manipulate requests, request metadata, and responses
    in arbitrary ways.
    Example use cases include:
    * Logging
    * Verifying requests according to service or custom semantics
    * Stripping extraneous information from responses

    These use cases and more can be enabled by injecting an
    instance of a custom subclass when constructing the ComplianceRestTransport.

    .. code-block:: python
        class MyCustomComplianceInterceptor(ComplianceRestInterceptor):
            def pre_get_enum(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_get_enum(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_repeat_data_body(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_repeat_data_body(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_repeat_data_body_info(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_repeat_data_body_info(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_repeat_data_body_patch(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_repeat_data_body_patch(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_repeat_data_body_put(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_repeat_data_body_put(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_repeat_data_path_resource(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_repeat_data_path_resource(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_repeat_data_path_trailing_resource(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_repeat_data_path_trailing_resource(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_repeat_data_query(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_repeat_data_query(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_repeat_data_simple_path(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_repeat_data_simple_path(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_verify_enum(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_verify_enum(self, response):
                logging.log(f"Received response: {response}")
                return response

        transport = ComplianceRestTransport(interceptor=MyCustomComplianceInterceptor())
        client = ComplianceClient(transport=transport)


    """
    def pre_get_enum(self, request: compliance.EnumRequest, metadata: Sequence[Tuple[str, str]]) -> Tuple[compliance.EnumRequest, Sequence[Tuple[str, str]]]:
        """Pre-rpc interceptor for get_enum

        Override in a subclass to manipulate the request or metadata
        before they are sent to the Compliance server.
        """
        return request, metadata

    def post_get_enum(self, response: compliance.EnumResponse) -> compliance.EnumResponse:
        """Post-rpc interceptor for get_enum

        Override in a subclass to manipulate the response
        after it is returned by the Compliance server but before
        it is returned to user code.
        """
        return response
    def pre_repeat_data_body(self, request: compliance.RepeatRequest, metadata: Sequence[Tuple[str, str]]) -> Tuple[compliance.RepeatRequest, Sequence[Tuple[str, str]]]:
        """Pre-rpc interceptor for repeat_data_body

        Override in a subclass to manipulate the request or metadata
        before they are sent to the Compliance server.
        """
        return request, metadata

    def post_repeat_data_body(self, response: compliance.RepeatResponse) -> compliance.RepeatResponse:
        """Post-rpc interceptor for repeat_data_body

        Override in a subclass to manipulate the response
        after it is returned by the Compliance server but before
        it is returned to user code.
        """
        return response
    def pre_repeat_data_body_info(self, request: compliance.RepeatRequest, metadata: Sequence[Tuple[str, str]]) -> Tuple[compliance.RepeatRequest, Sequence[Tuple[str, str]]]:
        """Pre-rpc interceptor for repeat_data_body_info

        Override in a subclass to manipulate the request or metadata
        before they are sent to the Compliance server.
        """
        return request, metadata

    def post_repeat_data_body_info(self, response: compliance.RepeatResponse) -> compliance.RepeatResponse:
        """Post-rpc interceptor for repeat_data_body_info

        Override in a subclass to manipulate the response
        after it is returned by the Compliance server but before
        it is returned to user code.
        """
        return response
    def pre_repeat_data_body_patch(self, request: compliance.RepeatRequest, metadata: Sequence[Tuple[str, str]]) -> Tuple[compliance.RepeatRequest, Sequence[Tuple[str, str]]]:
        """Pre-rpc interceptor for repeat_data_body_patch

        Override in a subclass to manipulate the request or metadata
        before they are sent to the Compliance server.
        """
        return request, metadata

    def post_repeat_data_body_patch(self, response: compliance.RepeatResponse) -> compliance.RepeatResponse:
        """Post-rpc interceptor for repeat_data_body_patch

        Override in a subclass to manipulate the response
        after it is returned by the Compliance server but before
        it is returned to user code.
        """
        return response
    def pre_repeat_data_body_put(self, request: compliance.RepeatRequest, metadata: Sequence[Tuple[str, str]]) -> Tuple[compliance.RepeatRequest, Sequence[Tuple[str, str]]]:
        """Pre-rpc interceptor for repeat_data_body_put

        Override in a subclass to manipulate the request or metadata
        before they are sent to the Compliance server.
        """
        return request, metadata

    def post_repeat_data_body_put(self, response: compliance.RepeatResponse) -> compliance.RepeatResponse:
        """Post-rpc interceptor for repeat_data_body_put

        Override in a subclass to manipulate the response
        after it is returned by the Compliance server but before
        it is returned to user code.
        """
        return response
    def pre_repeat_data_path_resource(self, request: compliance.RepeatRequest, metadata: Sequence[Tuple[str, str]]) -> Tuple[compliance.RepeatRequest, Sequence[Tuple[str, str]]]:
        """Pre-rpc interceptor for repeat_data_path_resource

        Override in a subclass to manipulate the request or metadata
        before they are sent to the Compliance server.
        """
        return request, metadata

    def post_repeat_data_path_resource(self, response: compliance.RepeatResponse) -> compliance.RepeatResponse:
        """Post-rpc interceptor for repeat_data_path_resource

        Override in a subclass to manipulate the response
        after it is returned by the Compliance server but before
        it is returned to user code.
        """
        return response
    def pre_repeat_data_path_trailing_resource(self, request: compliance.RepeatRequest, metadata: Sequence[Tuple[str, str]]) -> Tuple[compliance.RepeatRequest, Sequence[Tuple[str, str]]]:
        """Pre-rpc interceptor for repeat_data_path_trailing_resource

        Override in a subclass to manipulate the request or metadata
        before they are sent to the Compliance server.
        """
        return request, metadata

    def post_repeat_data_path_trailing_resource(self, response: compliance.RepeatResponse) -> compliance.RepeatResponse:
        """Post-rpc interceptor for repeat_data_path_trailing_resource

        Override in a subclass to manipulate the response
        after it is returned by the Compliance server but before
        it is returned to user code.
        """
        return response
    def pre_repeat_data_query(self, request: compliance.RepeatRequest, metadata: Sequence[Tuple[str, str]]) -> Tuple[compliance.RepeatRequest, Sequence[Tuple[str, str]]]:
        """Pre-rpc interceptor for repeat_data_query

        Override in a subclass to manipulate the request or metadata
        before they are sent to the Compliance server.
        """
        return request, metadata

    def post_repeat_data_query(self, response: compliance.RepeatResponse) -> compliance.RepeatResponse:
        """Post-rpc interceptor for repeat_data_query

        Override in a subclass to manipulate the response
        after it is returned by the Compliance server but before
        it is returned to user code.
        """
        return response
    def pre_repeat_data_simple_path(self, request: compliance.RepeatRequest, metadata: Sequence[Tuple[str, str]]) -> Tuple[compliance.RepeatRequest, Sequence[Tuple[str, str]]]:
        """Pre-rpc interceptor for repeat_data_simple_path

        Override in a subclass to manipulate the request or metadata
        before they are sent to the Compliance server.
        """
        return request, metadata

    def post_repeat_data_simple_path(self, response: compliance.RepeatResponse) -> compliance.RepeatResponse:
        """Post-rpc interceptor for repeat_data_simple_path

        Override in a subclass to manipulate the response
        after it is returned by the Compliance server but before
        it is returned to user code.
        """
        return response
    def pre_verify_enum(self, request: compliance.EnumResponse, metadata: Sequence[Tuple[str, str]]) -> Tuple[compliance.EnumResponse, Sequence[Tuple[str, str]]]:
        """Pre-rpc interceptor for verify_enum

        Override in a subclass to manipulate the request or metadata
        before they are sent to the Compliance server.
        """
        return request, metadata

    def post_verify_enum(self, response: compliance.EnumResponse) -> compliance.EnumResponse:
        """Post-rpc interceptor for verify_enum

        Override in a subclass to manipulate the response
        after it is returned by the Compliance server but before
        it is returned to user code.
        """
        return response

    def pre_list_locations(
        self, request: locations_pb2.ListLocationsRequest, metadata: Sequence[Tuple[str, str]]
    ) -> Tuple[locations_pb2.ListLocationsRequest, Sequence[Tuple[str, str]]]:
        """Pre-rpc interceptor for list_locations

        Override in a subclass to manipulate the request or metadata
        before they are sent to the Compliance server.
        """
        return request, metadata

    def post_list_locations(
        self, response: locations_pb2.ListLocationsResponse
    ) -> locations_pb2.ListLocationsResponse:
        """Post-rpc interceptor for list_locations

        Override in a subclass to manipulate the response
        after it is returned by the Compliance server but before
        it is returned to user code.
        """
        return response
    def pre_get_location(
        self, request: locations_pb2.GetLocationRequest, metadata: Sequence[Tuple[str, str]]
    ) -> Tuple[locations_pb2.GetLocationRequest, Sequence[Tuple[str, str]]]:
        """Pre-rpc interceptor for get_location

        Override in a subclass to manipulate the request or metadata
        before they are sent to the Compliance server.
        """
        return request, metadata

    def post_get_location(
        self, response: locations_pb2.Location
    ) -> locations_pb2.Location:
        """Post-rpc interceptor for get_location

        Override in a subclass to manipulate the response
        after it is returned by the Compliance server but before
        it is returned to user code.
        """
        return response
    def pre_set_iam_policy(
        self, request: iam_policy_pb2.SetIamPolicyRequest, metadata: Sequence[Tuple[str, str]]
    ) -> Tuple[iam_policy_pb2.SetIamPolicyRequest, Sequence[Tuple[str, str]]]:
        """Pre-rpc interceptor for set_iam_policy

        Override in a subclass to manipulate the request or metadata
        before they are sent to the Compliance server.
        """
        return request, metadata

    def post_set_iam_policy(
        self, response: policy_pb2.Policy
    ) -> policy_pb2.Policy:
        """Post-rpc interceptor for set_iam_policy

        Override in a subclass to manipulate the response
        after it is returned by the Compliance server but before
        it is returned to user code.
        """
        return response
    def pre_get_iam_policy(
        self, request: iam_policy_pb2.GetIamPolicyRequest, metadata: Sequence[Tuple[str, str]]
    ) -> Tuple[iam_policy_pb2.GetIamPolicyRequest, Sequence[Tuple[str, str]]]:
        """Pre-rpc interceptor for get_iam_policy

        Override in a subclass to manipulate the request or metadata
        before they are sent to the Compliance server.
        """
        return request, metadata

    def post_get_iam_policy(
        self, response: policy_pb2.Policy
    ) -> policy_pb2.Policy:
        """Post-rpc interceptor for get_iam_policy

        Override in a subclass to manipulate the response
        after it is returned by the Compliance server but before
        it is returned to user code.
        """
        return response
    def pre_test_iam_permissions(
        self, request: iam_policy_pb2.TestIamPermissionsRequest, metadata: Sequence[Tuple[str, str]]
    ) -> Tuple[iam_policy_pb2.TestIamPermissionsRequest, Sequence[Tuple[str, str]]]:
        """Pre-rpc interceptor for test_iam_permissions

        Override in a subclass to manipulate the request or metadata
        before they are sent to the Compliance server.
        """
        return request, metadata

    def post_test_iam_permissions(
        self, response: iam_policy_pb2.TestIamPermissionsResponse
    ) -> iam_policy_pb2.TestIamPermissionsResponse:
        """Post-rpc interceptor for test_iam_permissions

        Override in a subclass to manipulate the response
        after it is returned by the Compliance server but before
        it is returned to user code.
        """
        return response
    def pre_list_operations(
        self, request: operations_pb2.ListOperationsRequest, metadata: Sequence[Tuple[str, str]]
    ) -> Tuple[operations_pb2.ListOperationsRequest, Sequence[Tuple[str, str]]]:
        """Pre-rpc interceptor for list_operations

        Override in a subclass to manipulate the request or metadata
        before they are sent to the Compliance server.
        """
        return request, metadata

    def post_list_operations(
        self, response: operations_pb2.ListOperationsResponse
    ) -> operations_pb2.ListOperationsResponse:
        """Post-rpc interceptor for list_operations

        Override in a subclass to manipulate the response
        after it is returned by the Compliance server but before
        it is returned to user code.
        """
        return response
    def pre_get_operation(
        self, request: operations_pb2.GetOperationRequest, metadata: Sequence[Tuple[str, str]]
    ) -> Tuple[operations_pb2.GetOperationRequest, Sequence[Tuple[str, str]]]:
        """Pre-rpc interceptor for get_operation

        Override in a subclass to manipulate the request or metadata
        before they are sent to the Compliance server.
        """
        return request, metadata

    def post_get_operation(
        self, response: operations_pb2.Operation
    ) -> operations_pb2.Operation:
        """Post-rpc interceptor for get_operation

        Override in a subclass to manipulate the response
        after it is returned by the Compliance server but before
        it is returned to user code.
        """
        return response
    def pre_delete_operation(
        self, request: operations_pb2.DeleteOperationRequest, metadata: Sequence[Tuple[str, str]]
    ) -> Tuple[operations_pb2.DeleteOperationRequest, Sequence[Tuple[str, str]]]:
        """Pre-rpc interceptor for delete_operation

        Override in a subclass to manipulate the request or metadata
        before they are sent to the Compliance server.
        """
        return request, metadata

    def post_delete_operation(
        self, response: None
    ) -> None:
        """Post-rpc interceptor for delete_operation

        Override in a subclass to manipulate the response
        after it is returned by the Compliance server but before
        it is returned to user code.
        """
        return response
    def pre_cancel_operation(
        self, request: operations_pb2.CancelOperationRequest, metadata: Sequence[Tuple[str, str]]
    ) -> Tuple[operations_pb2.CancelOperationRequest, Sequence[Tuple[str, str]]]:
        """Pre-rpc interceptor for cancel_operation

        Override in a subclass to manipulate the request or metadata
        before they are sent to the Compliance server.
        """
        return request, metadata

    def post_cancel_operation(
        self, response: None
    ) -> None:
        """Post-rpc interceptor for cancel_operation

        Override in a subclass to manipulate the response
        after it is returned by the Compliance server but before
        it is returned to user code.
        """
        return response


@dataclasses.dataclass
class ComplianceRestStub:
    _session: AuthorizedSession
    _host: str
    _interceptor: ComplianceRestInterceptor


class ComplianceRestTransport(ComplianceTransport):
    """REST backend transport for Compliance.

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

    NOTE: This REST transport functionality is currently in a beta
    state (preview). We welcome your feedback via an issue in this
    library's source repository. Thank you!
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
            interceptor: Optional[ComplianceRestInterceptor] = None,
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
        maybe_url_match = re.match("^(?P<scheme>http(?:s)?://)?(?P<host>.*)$", host)
        if maybe_url_match is None:
            raise ValueError(f"Unexpected hostname structure: {host}")  # pragma: NO COVER

        url_match_items = maybe_url_match.groupdict()

        host = f"{url_scheme}://{host}" if not url_match_items["scheme"] else host

        super().__init__(
            host=host,
            credentials=credentials,
            client_info=client_info,
            always_use_jwt_access=always_use_jwt_access,
            api_audience=api_audience
        )
        self._session = AuthorizedSession(
            self._credentials, default_host=self.DEFAULT_HOST)
        if client_cert_source_for_mtls:
            self._session.configure_mtls_channel(client_cert_source_for_mtls)
        self._interceptor = interceptor or ComplianceRestInterceptor()
        self._prep_wrapped_messages(client_info)

    class _GetEnum(ComplianceRestStub):
        def __hash__(self):
            return hash("GetEnum")

        def __call__(self,
                request: compliance.EnumRequest, *,
                retry: OptionalRetry=gapic_v1.method.DEFAULT,
                timeout: Optional[float]=None,
                metadata: Sequence[Tuple[str, str]]=(),
                ) -> compliance.EnumResponse:
            r"""Call the get enum method over HTTP.

            Args:
                request (~.compliance.EnumRequest):
                    The request object.
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, str]]): Strings which should be
                    sent along with the request as metadata.

            Returns:
                ~.compliance.EnumResponse:

            """

            http_options: List[Dict[str, str]] = [{
                'method': 'get',
                'uri': '/v1beta1/compliance/enum',
            },
            ]
            request, metadata = self._interceptor.pre_get_enum(request, metadata)
            pb_request = compliance.EnumRequest.pb(request)
            transcoded_request = path_template.transcode(http_options, pb_request)

            uri = transcoded_request['uri']
            method = transcoded_request['method']

            # Jsonify the query params
            query_params = json.loads(json_format.MessageToJson(
                transcoded_request['query_params'],
                use_integers_for_enums=False,
            ))

            # Send the request
            headers = dict(metadata)
            headers['Content-Type'] = 'application/json'
            response = getattr(self._session, method)(
                "{host}{uri}".format(host=self._host, uri=uri),
                timeout=timeout,
                headers=headers,
                params=rest_helpers.flatten_query_params(query_params, strict=True),
                )

            # In case of error, raise the appropriate core_exceptions.GoogleAPICallError exception
            # subclass.
            if response.status_code >= 400:
                raise core_exceptions.from_http_response(response)

            # Return the response
            resp = compliance.EnumResponse()
            pb_resp = compliance.EnumResponse.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)
            resp = self._interceptor.post_get_enum(resp)
            return resp

    class _RepeatDataBody(ComplianceRestStub):
        def __hash__(self):
            return hash("RepeatDataBody")

        def __call__(self,
                request: compliance.RepeatRequest, *,
                retry: OptionalRetry=gapic_v1.method.DEFAULT,
                timeout: Optional[float]=None,
                metadata: Sequence[Tuple[str, str]]=(),
                ) -> compliance.RepeatResponse:
            r"""Call the repeat data body method over HTTP.

            Args:
                request (~.compliance.RepeatRequest):
                    The request object.
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, str]]): Strings which should be
                    sent along with the request as metadata.

            Returns:
                ~.compliance.RepeatResponse:

            """

            http_options: List[Dict[str, str]] = [{
                'method': 'post',
                'uri': '/v1beta1/repeat:body',
                'body': '*',
            },
            ]
            request, metadata = self._interceptor.pre_repeat_data_body(request, metadata)
            pb_request = compliance.RepeatRequest.pb(request)
            transcoded_request = path_template.transcode(http_options, pb_request)

            # Jsonify the request body

            body = json_format.MessageToJson(
                transcoded_request['body'],
                use_integers_for_enums=False
            )
            uri = transcoded_request['uri']
            method = transcoded_request['method']

            # Jsonify the query params
            query_params = json.loads(json_format.MessageToJson(
                transcoded_request['query_params'],
                use_integers_for_enums=False,
            ))

            # Send the request
            headers = dict(metadata)
            headers['Content-Type'] = 'application/json'
            response = getattr(self._session, method)(
                "{host}{uri}".format(host=self._host, uri=uri),
                timeout=timeout,
                headers=headers,
                params=rest_helpers.flatten_query_params(query_params, strict=True),
                data=body,
                )

            # In case of error, raise the appropriate core_exceptions.GoogleAPICallError exception
            # subclass.
            if response.status_code >= 400:
                raise core_exceptions.from_http_response(response)

            # Return the response
            resp = compliance.RepeatResponse()
            pb_resp = compliance.RepeatResponse.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)
            resp = self._interceptor.post_repeat_data_body(resp)
            return resp

    class _RepeatDataBodyInfo(ComplianceRestStub):
        def __hash__(self):
            return hash("RepeatDataBodyInfo")

        def __call__(self,
                request: compliance.RepeatRequest, *,
                retry: OptionalRetry=gapic_v1.method.DEFAULT,
                timeout: Optional[float]=None,
                metadata: Sequence[Tuple[str, str]]=(),
                ) -> compliance.RepeatResponse:
            r"""Call the repeat data body info method over HTTP.

            Args:
                request (~.compliance.RepeatRequest):
                    The request object.
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, str]]): Strings which should be
                    sent along with the request as metadata.

            Returns:
                ~.compliance.RepeatResponse:

            """

            http_options: List[Dict[str, str]] = [{
                'method': 'post',
                'uri': '/v1beta1/repeat:bodyinfo',
                'body': 'info',
            },
            ]
            request, metadata = self._interceptor.pre_repeat_data_body_info(request, metadata)
            pb_request = compliance.RepeatRequest.pb(request)
            transcoded_request = path_template.transcode(http_options, pb_request)

            # Jsonify the request body

            body = json_format.MessageToJson(
                transcoded_request['body'],
                use_integers_for_enums=False
            )
            uri = transcoded_request['uri']
            method = transcoded_request['method']

            # Jsonify the query params
            query_params = json.loads(json_format.MessageToJson(
                transcoded_request['query_params'],
                use_integers_for_enums=False,
            ))

            # Send the request
            headers = dict(metadata)
            headers['Content-Type'] = 'application/json'
            response = getattr(self._session, method)(
                "{host}{uri}".format(host=self._host, uri=uri),
                timeout=timeout,
                headers=headers,
                params=rest_helpers.flatten_query_params(query_params, strict=True),
                data=body,
                )

            # In case of error, raise the appropriate core_exceptions.GoogleAPICallError exception
            # subclass.
            if response.status_code >= 400:
                raise core_exceptions.from_http_response(response)

            # Return the response
            resp = compliance.RepeatResponse()
            pb_resp = compliance.RepeatResponse.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)
            resp = self._interceptor.post_repeat_data_body_info(resp)
            return resp

    class _RepeatDataBodyPatch(ComplianceRestStub):
        def __hash__(self):
            return hash("RepeatDataBodyPatch")

        def __call__(self,
                request: compliance.RepeatRequest, *,
                retry: OptionalRetry=gapic_v1.method.DEFAULT,
                timeout: Optional[float]=None,
                metadata: Sequence[Tuple[str, str]]=(),
                ) -> compliance.RepeatResponse:
            r"""Call the repeat data body patch method over HTTP.

            Args:
                request (~.compliance.RepeatRequest):
                    The request object.
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, str]]): Strings which should be
                    sent along with the request as metadata.

            Returns:
                ~.compliance.RepeatResponse:

            """

            http_options: List[Dict[str, str]] = [{
                'method': 'patch',
                'uri': '/v1beta1/repeat:bodypatch',
                'body': '*',
            },
            ]
            request, metadata = self._interceptor.pre_repeat_data_body_patch(request, metadata)
            pb_request = compliance.RepeatRequest.pb(request)
            transcoded_request = path_template.transcode(http_options, pb_request)

            # Jsonify the request body

            body = json_format.MessageToJson(
                transcoded_request['body'],
                use_integers_for_enums=False
            )
            uri = transcoded_request['uri']
            method = transcoded_request['method']

            # Jsonify the query params
            query_params = json.loads(json_format.MessageToJson(
                transcoded_request['query_params'],
                use_integers_for_enums=False,
            ))

            # Send the request
            headers = dict(metadata)
            headers['Content-Type'] = 'application/json'
            response = getattr(self._session, method)(
                "{host}{uri}".format(host=self._host, uri=uri),
                timeout=timeout,
                headers=headers,
                params=rest_helpers.flatten_query_params(query_params, strict=True),
                data=body,
                )

            # In case of error, raise the appropriate core_exceptions.GoogleAPICallError exception
            # subclass.
            if response.status_code >= 400:
                raise core_exceptions.from_http_response(response)

            # Return the response
            resp = compliance.RepeatResponse()
            pb_resp = compliance.RepeatResponse.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)
            resp = self._interceptor.post_repeat_data_body_patch(resp)
            return resp

    class _RepeatDataBodyPut(ComplianceRestStub):
        def __hash__(self):
            return hash("RepeatDataBodyPut")

        def __call__(self,
                request: compliance.RepeatRequest, *,
                retry: OptionalRetry=gapic_v1.method.DEFAULT,
                timeout: Optional[float]=None,
                metadata: Sequence[Tuple[str, str]]=(),
                ) -> compliance.RepeatResponse:
            r"""Call the repeat data body put method over HTTP.

            Args:
                request (~.compliance.RepeatRequest):
                    The request object.
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, str]]): Strings which should be
                    sent along with the request as metadata.

            Returns:
                ~.compliance.RepeatResponse:

            """

            http_options: List[Dict[str, str]] = [{
                'method': 'put',
                'uri': '/v1beta1/repeat:bodyput',
                'body': '*',
            },
            ]
            request, metadata = self._interceptor.pre_repeat_data_body_put(request, metadata)
            pb_request = compliance.RepeatRequest.pb(request)
            transcoded_request = path_template.transcode(http_options, pb_request)

            # Jsonify the request body

            body = json_format.MessageToJson(
                transcoded_request['body'],
                use_integers_for_enums=False
            )
            uri = transcoded_request['uri']
            method = transcoded_request['method']

            # Jsonify the query params
            query_params = json.loads(json_format.MessageToJson(
                transcoded_request['query_params'],
                use_integers_for_enums=False,
            ))

            # Send the request
            headers = dict(metadata)
            headers['Content-Type'] = 'application/json'
            response = getattr(self._session, method)(
                "{host}{uri}".format(host=self._host, uri=uri),
                timeout=timeout,
                headers=headers,
                params=rest_helpers.flatten_query_params(query_params, strict=True),
                data=body,
                )

            # In case of error, raise the appropriate core_exceptions.GoogleAPICallError exception
            # subclass.
            if response.status_code >= 400:
                raise core_exceptions.from_http_response(response)

            # Return the response
            resp = compliance.RepeatResponse()
            pb_resp = compliance.RepeatResponse.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)
            resp = self._interceptor.post_repeat_data_body_put(resp)
            return resp

    class _RepeatDataPathResource(ComplianceRestStub):
        def __hash__(self):
            return hash("RepeatDataPathResource")

        def __call__(self,
                request: compliance.RepeatRequest, *,
                retry: OptionalRetry=gapic_v1.method.DEFAULT,
                timeout: Optional[float]=None,
                metadata: Sequence[Tuple[str, str]]=(),
                ) -> compliance.RepeatResponse:
            r"""Call the repeat data path resource method over HTTP.

            Args:
                request (~.compliance.RepeatRequest):
                    The request object.
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, str]]): Strings which should be
                    sent along with the request as metadata.

            Returns:
                ~.compliance.RepeatResponse:

            """

            http_options: List[Dict[str, str]] = [{
                'method': 'get',
                'uri': '/v1beta1/repeat/{info.f_string=first/*}/{info.f_child.f_string=second/*}/bool/{info.f_bool}:pathresource',
            },
{
                'method': 'get',
                'uri': '/v1beta1/repeat/{info.f_child.f_string=first/*}/{info.f_string=second/*}/bool/{info.f_bool}:childfirstpathresource',
            },
            ]
            request, metadata = self._interceptor.pre_repeat_data_path_resource(request, metadata)
            pb_request = compliance.RepeatRequest.pb(request)
            transcoded_request = path_template.transcode(http_options, pb_request)

            uri = transcoded_request['uri']
            method = transcoded_request['method']

            # Jsonify the query params
            query_params = json.loads(json_format.MessageToJson(
                transcoded_request['query_params'],
                use_integers_for_enums=False,
            ))

            # Send the request
            headers = dict(metadata)
            headers['Content-Type'] = 'application/json'
            response = getattr(self._session, method)(
                "{host}{uri}".format(host=self._host, uri=uri),
                timeout=timeout,
                headers=headers,
                params=rest_helpers.flatten_query_params(query_params, strict=True),
                )

            # In case of error, raise the appropriate core_exceptions.GoogleAPICallError exception
            # subclass.
            if response.status_code >= 400:
                raise core_exceptions.from_http_response(response)

            # Return the response
            resp = compliance.RepeatResponse()
            pb_resp = compliance.RepeatResponse.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)
            resp = self._interceptor.post_repeat_data_path_resource(resp)
            return resp

    class _RepeatDataPathTrailingResource(ComplianceRestStub):
        def __hash__(self):
            return hash("RepeatDataPathTrailingResource")

        def __call__(self,
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
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, str]]): Strings which should be
                    sent along with the request as metadata.

            Returns:
                ~.compliance.RepeatResponse:

            """

            http_options: List[Dict[str, str]] = [{
                'method': 'get',
                'uri': '/v1beta1/repeat/{info.f_string=first/*}/{info.f_child.f_string=second/**}:pathtrailingresource',
            },
            ]
            request, metadata = self._interceptor.pre_repeat_data_path_trailing_resource(request, metadata)
            pb_request = compliance.RepeatRequest.pb(request)
            transcoded_request = path_template.transcode(http_options, pb_request)

            uri = transcoded_request['uri']
            method = transcoded_request['method']

            # Jsonify the query params
            query_params = json.loads(json_format.MessageToJson(
                transcoded_request['query_params'],
                use_integers_for_enums=False,
            ))

            # Send the request
            headers = dict(metadata)
            headers['Content-Type'] = 'application/json'
            response = getattr(self._session, method)(
                "{host}{uri}".format(host=self._host, uri=uri),
                timeout=timeout,
                headers=headers,
                params=rest_helpers.flatten_query_params(query_params, strict=True),
                )

            # In case of error, raise the appropriate core_exceptions.GoogleAPICallError exception
            # subclass.
            if response.status_code >= 400:
                raise core_exceptions.from_http_response(response)

            # Return the response
            resp = compliance.RepeatResponse()
            pb_resp = compliance.RepeatResponse.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)
            resp = self._interceptor.post_repeat_data_path_trailing_resource(resp)
            return resp

    class _RepeatDataQuery(ComplianceRestStub):
        def __hash__(self):
            return hash("RepeatDataQuery")

        def __call__(self,
                request: compliance.RepeatRequest, *,
                retry: OptionalRetry=gapic_v1.method.DEFAULT,
                timeout: Optional[float]=None,
                metadata: Sequence[Tuple[str, str]]=(),
                ) -> compliance.RepeatResponse:
            r"""Call the repeat data query method over HTTP.

            Args:
                request (~.compliance.RepeatRequest):
                    The request object.
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, str]]): Strings which should be
                    sent along with the request as metadata.

            Returns:
                ~.compliance.RepeatResponse:

            """

            http_options: List[Dict[str, str]] = [{
                'method': 'get',
                'uri': '/v1beta1/repeat:query',
            },
            ]
            request, metadata = self._interceptor.pre_repeat_data_query(request, metadata)
            pb_request = compliance.RepeatRequest.pb(request)
            transcoded_request = path_template.transcode(http_options, pb_request)

            uri = transcoded_request['uri']
            method = transcoded_request['method']

            # Jsonify the query params
            query_params = json.loads(json_format.MessageToJson(
                transcoded_request['query_params'],
                use_integers_for_enums=False,
            ))

            # Send the request
            headers = dict(metadata)
            headers['Content-Type'] = 'application/json'
            response = getattr(self._session, method)(
                "{host}{uri}".format(host=self._host, uri=uri),
                timeout=timeout,
                headers=headers,
                params=rest_helpers.flatten_query_params(query_params, strict=True),
                )

            # In case of error, raise the appropriate core_exceptions.GoogleAPICallError exception
            # subclass.
            if response.status_code >= 400:
                raise core_exceptions.from_http_response(response)

            # Return the response
            resp = compliance.RepeatResponse()
            pb_resp = compliance.RepeatResponse.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)
            resp = self._interceptor.post_repeat_data_query(resp)
            return resp

    class _RepeatDataSimplePath(ComplianceRestStub):
        def __hash__(self):
            return hash("RepeatDataSimplePath")

        def __call__(self,
                request: compliance.RepeatRequest, *,
                retry: OptionalRetry=gapic_v1.method.DEFAULT,
                timeout: Optional[float]=None,
                metadata: Sequence[Tuple[str, str]]=(),
                ) -> compliance.RepeatResponse:
            r"""Call the repeat data simple path method over HTTP.

            Args:
                request (~.compliance.RepeatRequest):
                    The request object.
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, str]]): Strings which should be
                    sent along with the request as metadata.

            Returns:
                ~.compliance.RepeatResponse:

            """

            http_options: List[Dict[str, str]] = [{
                'method': 'get',
                'uri': '/v1beta1/repeat/{info.f_string}/{info.f_int32}/{info.f_double}/{info.f_bool}/{info.f_kingdom}:simplepath',
            },
            ]
            request, metadata = self._interceptor.pre_repeat_data_simple_path(request, metadata)
            pb_request = compliance.RepeatRequest.pb(request)
            transcoded_request = path_template.transcode(http_options, pb_request)

            uri = transcoded_request['uri']
            method = transcoded_request['method']

            # Jsonify the query params
            query_params = json.loads(json_format.MessageToJson(
                transcoded_request['query_params'],
                use_integers_for_enums=False,
            ))

            # Send the request
            headers = dict(metadata)
            headers['Content-Type'] = 'application/json'
            response = getattr(self._session, method)(
                "{host}{uri}".format(host=self._host, uri=uri),
                timeout=timeout,
                headers=headers,
                params=rest_helpers.flatten_query_params(query_params, strict=True),
                )

            # In case of error, raise the appropriate core_exceptions.GoogleAPICallError exception
            # subclass.
            if response.status_code >= 400:
                raise core_exceptions.from_http_response(response)

            # Return the response
            resp = compliance.RepeatResponse()
            pb_resp = compliance.RepeatResponse.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)
            resp = self._interceptor.post_repeat_data_simple_path(resp)
            return resp

    class _VerifyEnum(ComplianceRestStub):
        def __hash__(self):
            return hash("VerifyEnum")

        def __call__(self,
                request: compliance.EnumResponse, *,
                retry: OptionalRetry=gapic_v1.method.DEFAULT,
                timeout: Optional[float]=None,
                metadata: Sequence[Tuple[str, str]]=(),
                ) -> compliance.EnumResponse:
            r"""Call the verify enum method over HTTP.

            Args:
                request (~.compliance.EnumResponse):
                    The request object.
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, str]]): Strings which should be
                    sent along with the request as metadata.

            Returns:
                ~.compliance.EnumResponse:

            """

            http_options: List[Dict[str, str]] = [{
                'method': 'post',
                'uri': '/v1beta1/compliance/enum',
            },
            ]
            request, metadata = self._interceptor.pre_verify_enum(request, metadata)
            pb_request = compliance.EnumResponse.pb(request)
            transcoded_request = path_template.transcode(http_options, pb_request)

            uri = transcoded_request['uri']
            method = transcoded_request['method']

            # Jsonify the query params
            query_params = json.loads(json_format.MessageToJson(
                transcoded_request['query_params'],
                use_integers_for_enums=False,
            ))

            # Send the request
            headers = dict(metadata)
            headers['Content-Type'] = 'application/json'
            response = getattr(self._session, method)(
                "{host}{uri}".format(host=self._host, uri=uri),
                timeout=timeout,
                headers=headers,
                params=rest_helpers.flatten_query_params(query_params, strict=True),
                )

            # In case of error, raise the appropriate core_exceptions.GoogleAPICallError exception
            # subclass.
            if response.status_code >= 400:
                raise core_exceptions.from_http_response(response)

            # Return the response
            resp = compliance.EnumResponse()
            pb_resp = compliance.EnumResponse.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)
            resp = self._interceptor.post_verify_enum(resp)
            return resp

    @property
    def get_enum(self) -> Callable[
            [compliance.EnumRequest],
            compliance.EnumResponse]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._GetEnum(self._session, self._host, self._interceptor) # type: ignore

    @property
    def repeat_data_body(self) -> Callable[
            [compliance.RepeatRequest],
            compliance.RepeatResponse]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._RepeatDataBody(self._session, self._host, self._interceptor) # type: ignore

    @property
    def repeat_data_body_info(self) -> Callable[
            [compliance.RepeatRequest],
            compliance.RepeatResponse]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._RepeatDataBodyInfo(self._session, self._host, self._interceptor) # type: ignore

    @property
    def repeat_data_body_patch(self) -> Callable[
            [compliance.RepeatRequest],
            compliance.RepeatResponse]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._RepeatDataBodyPatch(self._session, self._host, self._interceptor) # type: ignore

    @property
    def repeat_data_body_put(self) -> Callable[
            [compliance.RepeatRequest],
            compliance.RepeatResponse]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._RepeatDataBodyPut(self._session, self._host, self._interceptor) # type: ignore

    @property
    def repeat_data_path_resource(self) -> Callable[
            [compliance.RepeatRequest],
            compliance.RepeatResponse]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._RepeatDataPathResource(self._session, self._host, self._interceptor) # type: ignore

    @property
    def repeat_data_path_trailing_resource(self) -> Callable[
            [compliance.RepeatRequest],
            compliance.RepeatResponse]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._RepeatDataPathTrailingResource(self._session, self._host, self._interceptor) # type: ignore

    @property
    def repeat_data_query(self) -> Callable[
            [compliance.RepeatRequest],
            compliance.RepeatResponse]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._RepeatDataQuery(self._session, self._host, self._interceptor) # type: ignore

    @property
    def repeat_data_simple_path(self) -> Callable[
            [compliance.RepeatRequest],
            compliance.RepeatResponse]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._RepeatDataSimplePath(self._session, self._host, self._interceptor) # type: ignore

    @property
    def verify_enum(self) -> Callable[
            [compliance.EnumResponse],
            compliance.EnumResponse]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._VerifyEnum(self._session, self._host, self._interceptor) # type: ignore

    @property
    def list_locations(self):
        return self._ListLocations(self._session, self._host, self._interceptor) # type: ignore

    class _ListLocations(ComplianceRestStub):
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

            http_options: List[Dict[str, str]] = [{
                'method': 'get',
                'uri': '/v1beta1/{name=projects/*}/locations',
            },
            ]

            request, metadata = self._interceptor.pre_list_locations(request, metadata)
            request_kwargs = json_format.MessageToDict(request)
            transcoded_request = path_template.transcode(
                http_options, **request_kwargs)

            uri = transcoded_request['uri']
            method = transcoded_request['method']

            # Jsonify the query params
            query_params = json.loads(json.dumps(transcoded_request['query_params']))

            # Send the request
            headers = dict(metadata)
            headers['Content-Type'] = 'application/json'

            response = getattr(self._session, method)(
                "{host}{uri}".format(host=self._host, uri=uri),
                timeout=timeout,
                headers=headers,
                params=rest_helpers.flatten_query_params(query_params),
            )

            # In case of error, raise the appropriate core_exceptions.GoogleAPICallError exception
            # subclass.
            if response.status_code >= 400:
                raise core_exceptions.from_http_response(response)

            resp = locations_pb2.ListLocationsResponse()
            resp = json_format.Parse(response.content.decode("utf-8"), resp)
            resp = self._interceptor.post_list_locations(resp)
            return resp

    @property
    def get_location(self):
        return self._GetLocation(self._session, self._host, self._interceptor) # type: ignore

    class _GetLocation(ComplianceRestStub):
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

            http_options: List[Dict[str, str]] = [{
                'method': 'get',
                'uri': '/v1beta1/{name=projects/*/locations/*}',
            },
            ]

            request, metadata = self._interceptor.pre_get_location(request, metadata)
            request_kwargs = json_format.MessageToDict(request)
            transcoded_request = path_template.transcode(
                http_options, **request_kwargs)

            uri = transcoded_request['uri']
            method = transcoded_request['method']

            # Jsonify the query params
            query_params = json.loads(json.dumps(transcoded_request['query_params']))

            # Send the request
            headers = dict(metadata)
            headers['Content-Type'] = 'application/json'

            response = getattr(self._session, method)(
                "{host}{uri}".format(host=self._host, uri=uri),
                timeout=timeout,
                headers=headers,
                params=rest_helpers.flatten_query_params(query_params),
            )

            # In case of error, raise the appropriate core_exceptions.GoogleAPICallError exception
            # subclass.
            if response.status_code >= 400:
                raise core_exceptions.from_http_response(response)

            resp = locations_pb2.Location()
            resp = json_format.Parse(response.content.decode("utf-8"), resp)
            resp = self._interceptor.post_get_location(resp)
            return resp

    @property
    def set_iam_policy(self):
        return self._SetIamPolicy(self._session, self._host, self._interceptor) # type: ignore

    class _SetIamPolicy(ComplianceRestStub):
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

            http_options: List[Dict[str, str]] = [{
                'method': 'post',
                'uri': '/v1beta1/{resource=users/*}:setIamPolicy',
                'body': '*',
            },
{
                'method': 'post',
                'uri': '/v1beta1/{resource=rooms/*}:setIamPolicy',
                'body': '*',
            },
{
                'method': 'post',
                'uri': '/v1beta1/{resource=rooms/*/blurbs/*}:setIamPolicy',
                'body': '*',
            },
{
                'method': 'post',
                'uri': '/v1beta1/{resource=sequences/*}:setIamPolicy',
                'body': '*',
            },
            ]

            request, metadata = self._interceptor.pre_set_iam_policy(request, metadata)
            request_kwargs = json_format.MessageToDict(request)
            transcoded_request = path_template.transcode(
                http_options, **request_kwargs)

            body = json.dumps(transcoded_request['body'])
            uri = transcoded_request['uri']
            method = transcoded_request['method']

            # Jsonify the query params
            query_params = json.loads(json.dumps(transcoded_request['query_params']))

            # Send the request
            headers = dict(metadata)
            headers['Content-Type'] = 'application/json'

            response = getattr(self._session, method)(
                "{host}{uri}".format(host=self._host, uri=uri),
                timeout=timeout,
                headers=headers,
                params=rest_helpers.flatten_query_params(query_params),
                data=body,
            )

            # In case of error, raise the appropriate core_exceptions.GoogleAPICallError exception
            # subclass.
            if response.status_code >= 400:
                raise core_exceptions.from_http_response(response)

            resp = policy_pb2.Policy()
            resp = json_format.Parse(response.content.decode("utf-8"), resp)
            resp = self._interceptor.post_set_iam_policy(resp)
            return resp

    @property
    def get_iam_policy(self):
        return self._GetIamPolicy(self._session, self._host, self._interceptor) # type: ignore

    class _GetIamPolicy(ComplianceRestStub):
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

            http_options: List[Dict[str, str]] = [{
                'method': 'get',
                'uri': '/v1beta1/{resource=users/*}:getIamPolicy',
            },
{
                'method': 'get',
                'uri': '/v1beta1/{resource=rooms/*}:getIamPolicy',
            },
{
                'method': 'get',
                'uri': '/v1beta1/{resource=rooms/*/blurbs/*}:getIamPolicy',
            },
{
                'method': 'get',
                'uri': '/v1beta1/{resource=sequences/*}:getIamPolicy',
            },
            ]

            request, metadata = self._interceptor.pre_get_iam_policy(request, metadata)
            request_kwargs = json_format.MessageToDict(request)
            transcoded_request = path_template.transcode(
                http_options, **request_kwargs)

            uri = transcoded_request['uri']
            method = transcoded_request['method']

            # Jsonify the query params
            query_params = json.loads(json.dumps(transcoded_request['query_params']))

            # Send the request
            headers = dict(metadata)
            headers['Content-Type'] = 'application/json'

            response = getattr(self._session, method)(
                "{host}{uri}".format(host=self._host, uri=uri),
                timeout=timeout,
                headers=headers,
                params=rest_helpers.flatten_query_params(query_params),
            )

            # In case of error, raise the appropriate core_exceptions.GoogleAPICallError exception
            # subclass.
            if response.status_code >= 400:
                raise core_exceptions.from_http_response(response)

            resp = policy_pb2.Policy()
            resp = json_format.Parse(response.content.decode("utf-8"), resp)
            resp = self._interceptor.post_get_iam_policy(resp)
            return resp

    @property
    def test_iam_permissions(self):
        return self._TestIamPermissions(self._session, self._host, self._interceptor) # type: ignore

    class _TestIamPermissions(ComplianceRestStub):
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

            http_options: List[Dict[str, str]] = [{
                'method': 'post',
                'uri': '/v1beta1/{resource=users/*}:testIamPermissions',
                'body': '*',
            },
{
                'method': 'post',
                'uri': '/v1beta1/{resource=rooms/*}:testIamPermissions',
                'body': '*',
            },
{
                'method': 'post',
                'uri': '/v1beta1/{resource=rooms/*/blurbs/*}:testIamPermissions',
                'body': '*',
            },
{
                'method': 'post',
                'uri': '/v1beta1/{resource=sequences/*}:testIamPermissions',
                'body': '*',
            },
            ]

            request, metadata = self._interceptor.pre_test_iam_permissions(request, metadata)
            request_kwargs = json_format.MessageToDict(request)
            transcoded_request = path_template.transcode(
                http_options, **request_kwargs)

            body = json.dumps(transcoded_request['body'])
            uri = transcoded_request['uri']
            method = transcoded_request['method']

            # Jsonify the query params
            query_params = json.loads(json.dumps(transcoded_request['query_params']))

            # Send the request
            headers = dict(metadata)
            headers['Content-Type'] = 'application/json'

            response = getattr(self._session, method)(
                "{host}{uri}".format(host=self._host, uri=uri),
                timeout=timeout,
                headers=headers,
                params=rest_helpers.flatten_query_params(query_params),
                data=body,
            )

            # In case of error, raise the appropriate core_exceptions.GoogleAPICallError exception
            # subclass.
            if response.status_code >= 400:
                raise core_exceptions.from_http_response(response)

            resp = iam_policy_pb2.TestIamPermissionsResponse()
            resp = json_format.Parse(response.content.decode("utf-8"), resp)
            resp = self._interceptor.post_test_iam_permissions(resp)
            return resp

    @property
    def list_operations(self):
        return self._ListOperations(self._session, self._host, self._interceptor) # type: ignore

    class _ListOperations(ComplianceRestStub):
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

            http_options: List[Dict[str, str]] = [{
                'method': 'get',
                'uri': '/v1beta1/operations',
            },
            ]

            request, metadata = self._interceptor.pre_list_operations(request, metadata)
            request_kwargs = json_format.MessageToDict(request)
            transcoded_request = path_template.transcode(
                http_options, **request_kwargs)

            uri = transcoded_request['uri']
            method = transcoded_request['method']

            # Jsonify the query params
            query_params = json.loads(json.dumps(transcoded_request['query_params']))

            # Send the request
            headers = dict(metadata)
            headers['Content-Type'] = 'application/json'

            response = getattr(self._session, method)(
                "{host}{uri}".format(host=self._host, uri=uri),
                timeout=timeout,
                headers=headers,
                params=rest_helpers.flatten_query_params(query_params),
            )

            # In case of error, raise the appropriate core_exceptions.GoogleAPICallError exception
            # subclass.
            if response.status_code >= 400:
                raise core_exceptions.from_http_response(response)

            resp = operations_pb2.ListOperationsResponse()
            resp = json_format.Parse(response.content.decode("utf-8"), resp)
            resp = self._interceptor.post_list_operations(resp)
            return resp

    @property
    def get_operation(self):
        return self._GetOperation(self._session, self._host, self._interceptor) # type: ignore

    class _GetOperation(ComplianceRestStub):
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

            http_options: List[Dict[str, str]] = [{
                'method': 'get',
                'uri': '/v1beta1/{name=operations/**}',
            },
            ]

            request, metadata = self._interceptor.pre_get_operation(request, metadata)
            request_kwargs = json_format.MessageToDict(request)
            transcoded_request = path_template.transcode(
                http_options, **request_kwargs)

            uri = transcoded_request['uri']
            method = transcoded_request['method']

            # Jsonify the query params
            query_params = json.loads(json.dumps(transcoded_request['query_params']))

            # Send the request
            headers = dict(metadata)
            headers['Content-Type'] = 'application/json'

            response = getattr(self._session, method)(
                "{host}{uri}".format(host=self._host, uri=uri),
                timeout=timeout,
                headers=headers,
                params=rest_helpers.flatten_query_params(query_params),
            )

            # In case of error, raise the appropriate core_exceptions.GoogleAPICallError exception
            # subclass.
            if response.status_code >= 400:
                raise core_exceptions.from_http_response(response)

            resp = operations_pb2.Operation()
            resp = json_format.Parse(response.content.decode("utf-8"), resp)
            resp = self._interceptor.post_get_operation(resp)
            return resp

    @property
    def delete_operation(self):
        return self._DeleteOperation(self._session, self._host, self._interceptor) # type: ignore

    class _DeleteOperation(ComplianceRestStub):
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

            http_options: List[Dict[str, str]] = [{
                'method': 'delete',
                'uri': '/v1beta1/{name=operations/**}',
            },
            ]

            request, metadata = self._interceptor.pre_delete_operation(request, metadata)
            request_kwargs = json_format.MessageToDict(request)
            transcoded_request = path_template.transcode(
                http_options, **request_kwargs)

            uri = transcoded_request['uri']
            method = transcoded_request['method']

            # Jsonify the query params
            query_params = json.loads(json.dumps(transcoded_request['query_params']))

            # Send the request
            headers = dict(metadata)
            headers['Content-Type'] = 'application/json'

            response = getattr(self._session, method)(
                "{host}{uri}".format(host=self._host, uri=uri),
                timeout=timeout,
                headers=headers,
                params=rest_helpers.flatten_query_params(query_params),
            )

            # In case of error, raise the appropriate core_exceptions.GoogleAPICallError exception
            # subclass.
            if response.status_code >= 400:
                raise core_exceptions.from_http_response(response)

            return self._interceptor.post_delete_operation(None)

    @property
    def cancel_operation(self):
        return self._CancelOperation(self._session, self._host, self._interceptor) # type: ignore

    class _CancelOperation(ComplianceRestStub):
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

            http_options: List[Dict[str, str]] = [{
                'method': 'post',
                'uri': '/v1beta1/{name=operations/**}:cancel',
            },
            ]

            request, metadata = self._interceptor.pre_cancel_operation(request, metadata)
            request_kwargs = json_format.MessageToDict(request)
            transcoded_request = path_template.transcode(
                http_options, **request_kwargs)

            uri = transcoded_request['uri']
            method = transcoded_request['method']

            # Jsonify the query params
            query_params = json.loads(json.dumps(transcoded_request['query_params']))

            # Send the request
            headers = dict(metadata)
            headers['Content-Type'] = 'application/json'

            response = getattr(self._session, method)(
                "{host}{uri}".format(host=self._host, uri=uri),
                timeout=timeout,
                headers=headers,
                params=rest_helpers.flatten_query_params(query_params),
            )

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
    'ComplianceRestTransport',
)

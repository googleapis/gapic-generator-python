# -*- coding: utf-8 -*-
# Copyright 2022 Google LLC
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
from google.api_core import operations_v1
from requests import __version__ as requests_version
import dataclasses
import re
from typing import Callable, Dict, List, Optional, Sequence, Tuple, Union
import warnings

try:
    OptionalRetry = Union[retries.Retry, gapic_v1.method._MethodDefault]
except AttributeError:  # pragma: NO COVER
    OptionalRetry = Union[retries.Retry, object]  # type: ignore


from google.cloud.asset_v1.types import asset_service
from google.longrunning import operations_pb2  # type: ignore
from google.protobuf import empty_pb2  # type: ignore

from .base import AssetServiceTransport, DEFAULT_CLIENT_INFO as BASE_DEFAULT_CLIENT_INFO


DEFAULT_CLIENT_INFO = gapic_v1.client_info.ClientInfo(
    gapic_version=BASE_DEFAULT_CLIENT_INFO.gapic_version,
    grpc_version=None,
    rest_version=requests_version,
)


class AssetServiceRestInterceptor:
    """Interceptor for AssetService.

    Interceptors are used to manipulate requests, request metadata, and responses
    in arbitrary ways.
    Example use cases include:
    * Logging
    * Verifying requests according to service or custom semantics
    * Stripping extraneous information from responses

    These use cases and more can be enabled by injecting an
    instance of a custom subclass when constructing the AssetServiceRestTransport.

    .. code-block:: python
        class MyCustomAssetServiceInterceptor(AssetServiceRestInterceptor):
            def pre_analyze_iam_policy(request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_analyze_iam_policy(response):
                logging.log(f"Received response: {response}")

            def pre_analyze_iam_policy_longrunning(request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_analyze_iam_policy_longrunning(response):
                logging.log(f"Received response: {response}")

            def pre_batch_get_assets_history(request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_batch_get_assets_history(response):
                logging.log(f"Received response: {response}")

            def pre_create_feed(request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_create_feed(response):
                logging.log(f"Received response: {response}")

            def pre_delete_feed(request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def pre_export_assets(request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_export_assets(response):
                logging.log(f"Received response: {response}")

            def pre_get_feed(request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_get_feed(response):
                logging.log(f"Received response: {response}")

            def pre_list_assets(request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_list_assets(response):
                logging.log(f"Received response: {response}")

            def pre_list_feeds(request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_list_feeds(response):
                logging.log(f"Received response: {response}")

            def pre_search_all_iam_policies(request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_search_all_iam_policies(response):
                logging.log(f"Received response: {response}")

            def pre_search_all_resources(request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_search_all_resources(response):
                logging.log(f"Received response: {response}")

            def pre_update_feed(request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_update_feed(response):
                logging.log(f"Received response: {response}")

        transport = AssetServiceRestTransport(interceptor=MyCustomAssetServiceInterceptor())
        client = AssetServiceClient(transport=transport)


    """
    def pre_analyze_iam_policy(self, request: asset_service.AnalyzeIamPolicyRequest, metadata: Sequence[Tuple[str, str]]) -> Tuple[asset_service.AnalyzeIamPolicyRequest, Sequence[Tuple[str, str]]]:
        """Pre-rpc interceptor for analyze_iam_policy

        Override in a subclass to manipulate the request or metadata
        before they are sent to the AssetService server.
        """
        return request, metadata

    def post_analyze_iam_policy(self, response: asset_service.AnalyzeIamPolicyResponse) -> asset_service.AnalyzeIamPolicyResponse:
        """Post-rpc interceptor for analyze_iam_policy

        Override in a subclass to manipulate the response
        after it is returned by the AssetService server but before
        it is returned to user code.
        """
        return response
    def pre_analyze_iam_policy_longrunning(self, request: asset_service.AnalyzeIamPolicyLongrunningRequest, metadata: Sequence[Tuple[str, str]]) -> Tuple[asset_service.AnalyzeIamPolicyLongrunningRequest, Sequence[Tuple[str, str]]]:
        """Pre-rpc interceptor for analyze_iam_policy_longrunning

        Override in a subclass to manipulate the request or metadata
        before they are sent to the AssetService server.
        """
        return request, metadata

    def post_analyze_iam_policy_longrunning(self, response: operations_pb2.Operation) -> operations_pb2.Operation:
        """Post-rpc interceptor for analyze_iam_policy_longrunning

        Override in a subclass to manipulate the response
        after it is returned by the AssetService server but before
        it is returned to user code.
        """
        return response
    def pre_batch_get_assets_history(self, request: asset_service.BatchGetAssetsHistoryRequest, metadata: Sequence[Tuple[str, str]]) -> Tuple[asset_service.BatchGetAssetsHistoryRequest, Sequence[Tuple[str, str]]]:
        """Pre-rpc interceptor for batch_get_assets_history

        Override in a subclass to manipulate the request or metadata
        before they are sent to the AssetService server.
        """
        return request, metadata

    def post_batch_get_assets_history(self, response: asset_service.BatchGetAssetsHistoryResponse) -> asset_service.BatchGetAssetsHistoryResponse:
        """Post-rpc interceptor for batch_get_assets_history

        Override in a subclass to manipulate the response
        after it is returned by the AssetService server but before
        it is returned to user code.
        """
        return response
    def pre_create_feed(self, request: asset_service.CreateFeedRequest, metadata: Sequence[Tuple[str, str]]) -> Tuple[asset_service.CreateFeedRequest, Sequence[Tuple[str, str]]]:
        """Pre-rpc interceptor for create_feed

        Override in a subclass to manipulate the request or metadata
        before they are sent to the AssetService server.
        """
        return request, metadata

    def post_create_feed(self, response: asset_service.Feed) -> asset_service.Feed:
        """Post-rpc interceptor for create_feed

        Override in a subclass to manipulate the response
        after it is returned by the AssetService server but before
        it is returned to user code.
        """
        return response
    def pre_delete_feed(self, request: asset_service.DeleteFeedRequest, metadata: Sequence[Tuple[str, str]]) -> Tuple[asset_service.DeleteFeedRequest, Sequence[Tuple[str, str]]]:
        """Pre-rpc interceptor for delete_feed

        Override in a subclass to manipulate the request or metadata
        before they are sent to the AssetService server.
        """
        return request, metadata

    def pre_export_assets(self, request: asset_service.ExportAssetsRequest, metadata: Sequence[Tuple[str, str]]) -> Tuple[asset_service.ExportAssetsRequest, Sequence[Tuple[str, str]]]:
        """Pre-rpc interceptor for export_assets

        Override in a subclass to manipulate the request or metadata
        before they are sent to the AssetService server.
        """
        return request, metadata

    def post_export_assets(self, response: operations_pb2.Operation) -> operations_pb2.Operation:
        """Post-rpc interceptor for export_assets

        Override in a subclass to manipulate the response
        after it is returned by the AssetService server but before
        it is returned to user code.
        """
        return response
    def pre_get_feed(self, request: asset_service.GetFeedRequest, metadata: Sequence[Tuple[str, str]]) -> Tuple[asset_service.GetFeedRequest, Sequence[Tuple[str, str]]]:
        """Pre-rpc interceptor for get_feed

        Override in a subclass to manipulate the request or metadata
        before they are sent to the AssetService server.
        """
        return request, metadata

    def post_get_feed(self, response: asset_service.Feed) -> asset_service.Feed:
        """Post-rpc interceptor for get_feed

        Override in a subclass to manipulate the response
        after it is returned by the AssetService server but before
        it is returned to user code.
        """
        return response
    def pre_list_assets(self, request: asset_service.ListAssetsRequest, metadata: Sequence[Tuple[str, str]]) -> Tuple[asset_service.ListAssetsRequest, Sequence[Tuple[str, str]]]:
        """Pre-rpc interceptor for list_assets

        Override in a subclass to manipulate the request or metadata
        before they are sent to the AssetService server.
        """
        return request, metadata

    def post_list_assets(self, response: asset_service.ListAssetsResponse) -> asset_service.ListAssetsResponse:
        """Post-rpc interceptor for list_assets

        Override in a subclass to manipulate the response
        after it is returned by the AssetService server but before
        it is returned to user code.
        """
        return response
    def pre_list_feeds(self, request: asset_service.ListFeedsRequest, metadata: Sequence[Tuple[str, str]]) -> Tuple[asset_service.ListFeedsRequest, Sequence[Tuple[str, str]]]:
        """Pre-rpc interceptor for list_feeds

        Override in a subclass to manipulate the request or metadata
        before they are sent to the AssetService server.
        """
        return request, metadata

    def post_list_feeds(self, response: asset_service.ListFeedsResponse) -> asset_service.ListFeedsResponse:
        """Post-rpc interceptor for list_feeds

        Override in a subclass to manipulate the response
        after it is returned by the AssetService server but before
        it is returned to user code.
        """
        return response
    def pre_search_all_iam_policies(self, request: asset_service.SearchAllIamPoliciesRequest, metadata: Sequence[Tuple[str, str]]) -> Tuple[asset_service.SearchAllIamPoliciesRequest, Sequence[Tuple[str, str]]]:
        """Pre-rpc interceptor for search_all_iam_policies

        Override in a subclass to manipulate the request or metadata
        before they are sent to the AssetService server.
        """
        return request, metadata

    def post_search_all_iam_policies(self, response: asset_service.SearchAllIamPoliciesResponse) -> asset_service.SearchAllIamPoliciesResponse:
        """Post-rpc interceptor for search_all_iam_policies

        Override in a subclass to manipulate the response
        after it is returned by the AssetService server but before
        it is returned to user code.
        """
        return response
    def pre_search_all_resources(self, request: asset_service.SearchAllResourcesRequest, metadata: Sequence[Tuple[str, str]]) -> Tuple[asset_service.SearchAllResourcesRequest, Sequence[Tuple[str, str]]]:
        """Pre-rpc interceptor for search_all_resources

        Override in a subclass to manipulate the request or metadata
        before they are sent to the AssetService server.
        """
        return request, metadata

    def post_search_all_resources(self, response: asset_service.SearchAllResourcesResponse) -> asset_service.SearchAllResourcesResponse:
        """Post-rpc interceptor for search_all_resources

        Override in a subclass to manipulate the response
        after it is returned by the AssetService server but before
        it is returned to user code.
        """
        return response
    def pre_update_feed(self, request: asset_service.UpdateFeedRequest, metadata: Sequence[Tuple[str, str]]) -> Tuple[asset_service.UpdateFeedRequest, Sequence[Tuple[str, str]]]:
        """Pre-rpc interceptor for update_feed

        Override in a subclass to manipulate the request or metadata
        before they are sent to the AssetService server.
        """
        return request, metadata

    def post_update_feed(self, response: asset_service.Feed) -> asset_service.Feed:
        """Post-rpc interceptor for update_feed

        Override in a subclass to manipulate the response
        after it is returned by the AssetService server but before
        it is returned to user code.
        """
        return response


@dataclasses.dataclass
class AssetServiceRestStub:
    _session: AuthorizedSession
    _host: str
    _interceptor: AssetServiceRestInterceptor


class AssetServiceRestTransport(AssetServiceTransport):
    """REST backend transport for AssetService.

    Asset service definition.

    This class defines the same methods as the primary client, so the
    primary client can load the underlying transport implementation
    and call it.

    It sends JSON representations of protocol buffers over HTTP/1.1

    NOTE: This REST transport functionality is currently in a beta
    state (preview). We welcome your feedback via an issue in this
    library's source repository. Thank you!
    """

    def __init__(self, *,
            host: str = 'cloudasset.googleapis.com',
            credentials: Optional[ga_credentials.Credentials] = None,
            credentials_file: Optional[str] = None,
            scopes: Optional[Sequence[str]] = None,
            client_cert_source_for_mtls: Optional[Callable[[
                ], Tuple[bytes, bytes]]] = None,
            quota_project_id: Optional[str] = None,
            client_info: gapic_v1.client_info.ClientInfo = DEFAULT_CLIENT_INFO,
            always_use_jwt_access: Optional[bool] = False,
            url_scheme: str = 'https',
            interceptor: Optional[AssetServiceRestInterceptor] = None,
            api_audience: Optional[str] = None,
            ) -> None:
        """Instantiate the transport.

       NOTE: This REST transport functionality is currently in a beta
       state (preview). We welcome your feedback via a GitHub issue in
       this library's repository. Thank you!

        Args:
            host (Optional[str]):
                 The hostname to connect to.
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
        self._operations_client: Optional[operations_v1.AbstractOperationsClient] = None
        if client_cert_source_for_mtls:
            self._session.configure_mtls_channel(client_cert_source_for_mtls)
        self._interceptor = interceptor or AssetServiceRestInterceptor()
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
            }

            rest_transport = operations_v1.OperationsRestTransport(
                    host=self._host,
                    # use the credentials which are saved
                    credentials=self._credentials,
                    scopes=self._scopes,
                    http_options=http_options,
                    path_prefix="v1")

            self._operations_client = operations_v1.AbstractOperationsClient(transport=rest_transport)

        # Return the client from cache.
        return self._operations_client

    class _AnalyzeIamPolicy(AssetServiceRestStub):
        def __hash__(self):
            return hash("AnalyzeIamPolicy")

        __REQUIRED_FIELDS_DEFAULT_VALUES: Dict[str, str] =  {
            "analysisQuery" : {},        }

        @classmethod
        def _get_unset_required_fields(cls, message_dict):
            return {k: v for k, v in cls.__REQUIRED_FIELDS_DEFAULT_VALUES.items() if k not in message_dict}

        def __call__(self,
                request: asset_service.AnalyzeIamPolicyRequest, *,
                retry: OptionalRetry=gapic_v1.method.DEFAULT,
                timeout: Optional[float]=None,
                metadata: Sequence[Tuple[str, str]]=(),
                ) -> asset_service.AnalyzeIamPolicyResponse:
            r"""Call the analyze iam policy method over HTTP.

            Args:
                request (~.asset_service.AnalyzeIamPolicyRequest):
                    The request object. A request message for
                [AssetService.AnalyzeIamPolicy][google.cloud.asset.v1.AssetService.AnalyzeIamPolicy].

                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, str]]): Strings which should be
                    sent along with the request as metadata.

            Returns:
                ~.asset_service.AnalyzeIamPolicyResponse:
                    A response message for
                [AssetService.AnalyzeIamPolicy][google.cloud.asset.v1.AssetService.AnalyzeIamPolicy].

            """

            http_options: List[Dict[str, str]] = [{
                'method': 'get',
                'uri': '/v1/{analysis_query.scope=*/*}:analyzeIamPolicy',
            },
            ]
            request, metadata = self._interceptor.pre_analyze_iam_policy(request, metadata)
            pb_request = asset_service.AnalyzeIamPolicyRequest.pb(request)
            transcoded_request = path_template.transcode(http_options, pb_request)

            uri = transcoded_request['uri']
            method = transcoded_request['method']

            # Jsonify the query params
            query_params = json.loads(json_format.MessageToJson(
                transcoded_request['query_params'],
                including_default_value_fields=False,
                use_integers_for_enums=False,
            ))
            query_params.update(self._get_unset_required_fields(query_params))

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
            resp = asset_service.AnalyzeIamPolicyResponse()
            pb_resp = asset_service.AnalyzeIamPolicyResponse.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)
            resp = self._interceptor.post_analyze_iam_policy(resp)
            return resp

    class _AnalyzeIamPolicyLongrunning(AssetServiceRestStub):
        def __hash__(self):
            return hash("AnalyzeIamPolicyLongrunning")

        __REQUIRED_FIELDS_DEFAULT_VALUES: Dict[str, str] =  {
        }

        @classmethod
        def _get_unset_required_fields(cls, message_dict):
            return {k: v for k, v in cls.__REQUIRED_FIELDS_DEFAULT_VALUES.items() if k not in message_dict}

        def __call__(self,
                request: asset_service.AnalyzeIamPolicyLongrunningRequest, *,
                retry: OptionalRetry=gapic_v1.method.DEFAULT,
                timeout: Optional[float]=None,
                metadata: Sequence[Tuple[str, str]]=(),
                ) -> operations_pb2.Operation:
            r"""Call the analyze iam policy
        longrunning method over HTTP.

            Args:
                request (~.asset_service.AnalyzeIamPolicyLongrunningRequest):
                    The request object. A request message for
                [AssetService.AnalyzeIamPolicyLongrunning][google.cloud.asset.v1.AssetService.AnalyzeIamPolicyLongrunning].

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

            http_options: List[Dict[str, str]] = [{
                'method': 'post',
                'uri': '/v1/{analysis_query.scope=*/*}:analyzeIamPolicyLongrunning',
                'body': '*',
            },
            ]
            request, metadata = self._interceptor.pre_analyze_iam_policy_longrunning(request, metadata)
            pb_request = asset_service.AnalyzeIamPolicyLongrunningRequest.pb(request)
            transcoded_request = path_template.transcode(http_options, pb_request)

            # Jsonify the request body

            body = json_format.MessageToJson(
                transcoded_request['body'],
                including_default_value_fields=False,
                use_integers_for_enums=False
            )
            uri = transcoded_request['uri']
            method = transcoded_request['method']

            # Jsonify the query params
            query_params = json.loads(json_format.MessageToJson(
                transcoded_request['query_params'],
                including_default_value_fields=False,
                use_integers_for_enums=False,
            ))
            query_params.update(self._get_unset_required_fields(query_params))

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
            resp = operations_pb2.Operation()
            json_format.Parse(response.content, resp, ignore_unknown_fields=True)
            resp = self._interceptor.post_analyze_iam_policy_longrunning(resp)
            return resp

    class _BatchGetAssetsHistory(AssetServiceRestStub):
        def __hash__(self):
            return hash("BatchGetAssetsHistory")

        __REQUIRED_FIELDS_DEFAULT_VALUES: Dict[str, str] =  {
        }

        @classmethod
        def _get_unset_required_fields(cls, message_dict):
            return {k: v for k, v in cls.__REQUIRED_FIELDS_DEFAULT_VALUES.items() if k not in message_dict}

        def __call__(self,
                request: asset_service.BatchGetAssetsHistoryRequest, *,
                retry: OptionalRetry=gapic_v1.method.DEFAULT,
                timeout: Optional[float]=None,
                metadata: Sequence[Tuple[str, str]]=(),
                ) -> asset_service.BatchGetAssetsHistoryResponse:
            r"""Call the batch get assets history method over HTTP.

            Args:
                request (~.asset_service.BatchGetAssetsHistoryRequest):
                    The request object. Batch get assets history request.
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, str]]): Strings which should be
                    sent along with the request as metadata.

            Returns:
                ~.asset_service.BatchGetAssetsHistoryResponse:
                    Batch get assets history response.
            """

            http_options: List[Dict[str, str]] = [{
                'method': 'get',
                'uri': '/v1/{parent=*/*}:batchGetAssetsHistory',
            },
            ]
            request, metadata = self._interceptor.pre_batch_get_assets_history(request, metadata)
            pb_request = asset_service.BatchGetAssetsHistoryRequest.pb(request)
            transcoded_request = path_template.transcode(http_options, pb_request)

            uri = transcoded_request['uri']
            method = transcoded_request['method']

            # Jsonify the query params
            query_params = json.loads(json_format.MessageToJson(
                transcoded_request['query_params'],
                including_default_value_fields=False,
                use_integers_for_enums=False,
            ))
            query_params.update(self._get_unset_required_fields(query_params))

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
            resp = asset_service.BatchGetAssetsHistoryResponse()
            pb_resp = asset_service.BatchGetAssetsHistoryResponse.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)
            resp = self._interceptor.post_batch_get_assets_history(resp)
            return resp

    class _CreateFeed(AssetServiceRestStub):
        def __hash__(self):
            return hash("CreateFeed")

        __REQUIRED_FIELDS_DEFAULT_VALUES: Dict[str, str] =  {
        }

        @classmethod
        def _get_unset_required_fields(cls, message_dict):
            return {k: v for k, v in cls.__REQUIRED_FIELDS_DEFAULT_VALUES.items() if k not in message_dict}

        def __call__(self,
                request: asset_service.CreateFeedRequest, *,
                retry: OptionalRetry=gapic_v1.method.DEFAULT,
                timeout: Optional[float]=None,
                metadata: Sequence[Tuple[str, str]]=(),
                ) -> asset_service.Feed:
            r"""Call the create feed method over HTTP.

            Args:
                request (~.asset_service.CreateFeedRequest):
                    The request object. Create asset feed request.
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, str]]): Strings which should be
                    sent along with the request as metadata.

            Returns:
                ~.asset_service.Feed:
                    An asset feed used to export asset
                updates to a destinations. An asset feed
                filter controls what updates are
                exported. The asset feed must be created
                within a project, organization, or
                folder. Supported destinations are:
                Pub/Sub topics.

            """

            http_options: List[Dict[str, str]] = [{
                'method': 'post',
                'uri': '/v1/{parent=*/*}/feeds',
                'body': '*',
            },
            ]
            request, metadata = self._interceptor.pre_create_feed(request, metadata)
            pb_request = asset_service.CreateFeedRequest.pb(request)
            transcoded_request = path_template.transcode(http_options, pb_request)

            # Jsonify the request body

            body = json_format.MessageToJson(
                transcoded_request['body'],
                including_default_value_fields=False,
                use_integers_for_enums=False
            )
            uri = transcoded_request['uri']
            method = transcoded_request['method']

            # Jsonify the query params
            query_params = json.loads(json_format.MessageToJson(
                transcoded_request['query_params'],
                including_default_value_fields=False,
                use_integers_for_enums=False,
            ))
            query_params.update(self._get_unset_required_fields(query_params))

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
            resp = asset_service.Feed()
            pb_resp = asset_service.Feed.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)
            resp = self._interceptor.post_create_feed(resp)
            return resp

    class _DeleteFeed(AssetServiceRestStub):
        def __hash__(self):
            return hash("DeleteFeed")

        __REQUIRED_FIELDS_DEFAULT_VALUES: Dict[str, str] =  {
        }

        @classmethod
        def _get_unset_required_fields(cls, message_dict):
            return {k: v for k, v in cls.__REQUIRED_FIELDS_DEFAULT_VALUES.items() if k not in message_dict}

        def __call__(self,
                request: asset_service.DeleteFeedRequest, *,
                retry: OptionalRetry=gapic_v1.method.DEFAULT,
                timeout: Optional[float]=None,
                metadata: Sequence[Tuple[str, str]]=(),
                ):
            r"""Call the delete feed method over HTTP.

            Args:
                request (~.asset_service.DeleteFeedRequest):
                    The request object.
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, str]]): Strings which should be
                    sent along with the request as metadata.
            """

            http_options: List[Dict[str, str]] = [{
                'method': 'delete',
                'uri': '/v1/{name=*/*/feeds/*}',
            },
            ]
            request, metadata = self._interceptor.pre_delete_feed(request, metadata)
            pb_request = asset_service.DeleteFeedRequest.pb(request)
            transcoded_request = path_template.transcode(http_options, pb_request)

            uri = transcoded_request['uri']
            method = transcoded_request['method']

            # Jsonify the query params
            query_params = json.loads(json_format.MessageToJson(
                transcoded_request['query_params'],
                including_default_value_fields=False,
                use_integers_for_enums=False,
            ))
            query_params.update(self._get_unset_required_fields(query_params))

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

    class _ExportAssets(AssetServiceRestStub):
        def __hash__(self):
            return hash("ExportAssets")

        __REQUIRED_FIELDS_DEFAULT_VALUES: Dict[str, str] =  {
        }

        @classmethod
        def _get_unset_required_fields(cls, message_dict):
            return {k: v for k, v in cls.__REQUIRED_FIELDS_DEFAULT_VALUES.items() if k not in message_dict}

        def __call__(self,
                request: asset_service.ExportAssetsRequest, *,
                retry: OptionalRetry=gapic_v1.method.DEFAULT,
                timeout: Optional[float]=None,
                metadata: Sequence[Tuple[str, str]]=(),
                ) -> operations_pb2.Operation:
            r"""Call the export assets method over HTTP.

            Args:
                request (~.asset_service.ExportAssetsRequest):
                    The request object. Export asset request.
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

            http_options: List[Dict[str, str]] = [{
                'method': 'post',
                'uri': '/v1/{parent=*/*}:exportAssets',
                'body': '*',
            },
            ]
            request, metadata = self._interceptor.pre_export_assets(request, metadata)
            pb_request = asset_service.ExportAssetsRequest.pb(request)
            transcoded_request = path_template.transcode(http_options, pb_request)

            # Jsonify the request body

            body = json_format.MessageToJson(
                transcoded_request['body'],
                including_default_value_fields=False,
                use_integers_for_enums=False
            )
            uri = transcoded_request['uri']
            method = transcoded_request['method']

            # Jsonify the query params
            query_params = json.loads(json_format.MessageToJson(
                transcoded_request['query_params'],
                including_default_value_fields=False,
                use_integers_for_enums=False,
            ))
            query_params.update(self._get_unset_required_fields(query_params))

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
            resp = operations_pb2.Operation()
            json_format.Parse(response.content, resp, ignore_unknown_fields=True)
            resp = self._interceptor.post_export_assets(resp)
            return resp

    class _GetFeed(AssetServiceRestStub):
        def __hash__(self):
            return hash("GetFeed")

        __REQUIRED_FIELDS_DEFAULT_VALUES: Dict[str, str] =  {
        }

        @classmethod
        def _get_unset_required_fields(cls, message_dict):
            return {k: v for k, v in cls.__REQUIRED_FIELDS_DEFAULT_VALUES.items() if k not in message_dict}

        def __call__(self,
                request: asset_service.GetFeedRequest, *,
                retry: OptionalRetry=gapic_v1.method.DEFAULT,
                timeout: Optional[float]=None,
                metadata: Sequence[Tuple[str, str]]=(),
                ) -> asset_service.Feed:
            r"""Call the get feed method over HTTP.

            Args:
                request (~.asset_service.GetFeedRequest):
                    The request object. Get asset feed request.
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, str]]): Strings which should be
                    sent along with the request as metadata.

            Returns:
                ~.asset_service.Feed:
                    An asset feed used to export asset
                updates to a destinations. An asset feed
                filter controls what updates are
                exported. The asset feed must be created
                within a project, organization, or
                folder. Supported destinations are:
                Pub/Sub topics.

            """

            http_options: List[Dict[str, str]] = [{
                'method': 'get',
                'uri': '/v1/{name=*/*/feeds/*}',
            },
            ]
            request, metadata = self._interceptor.pre_get_feed(request, metadata)
            pb_request = asset_service.GetFeedRequest.pb(request)
            transcoded_request = path_template.transcode(http_options, pb_request)

            uri = transcoded_request['uri']
            method = transcoded_request['method']

            # Jsonify the query params
            query_params = json.loads(json_format.MessageToJson(
                transcoded_request['query_params'],
                including_default_value_fields=False,
                use_integers_for_enums=False,
            ))
            query_params.update(self._get_unset_required_fields(query_params))

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
            resp = asset_service.Feed()
            pb_resp = asset_service.Feed.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)
            resp = self._interceptor.post_get_feed(resp)
            return resp

    class _ListAssets(AssetServiceRestStub):
        def __hash__(self):
            return hash("ListAssets")

        __REQUIRED_FIELDS_DEFAULT_VALUES: Dict[str, str] =  {
        }

        @classmethod
        def _get_unset_required_fields(cls, message_dict):
            return {k: v for k, v in cls.__REQUIRED_FIELDS_DEFAULT_VALUES.items() if k not in message_dict}

        def __call__(self,
                request: asset_service.ListAssetsRequest, *,
                retry: OptionalRetry=gapic_v1.method.DEFAULT,
                timeout: Optional[float]=None,
                metadata: Sequence[Tuple[str, str]]=(),
                ) -> asset_service.ListAssetsResponse:
            r"""Call the list assets method over HTTP.

            Args:
                request (~.asset_service.ListAssetsRequest):
                    The request object. ListAssets request.
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, str]]): Strings which should be
                    sent along with the request as metadata.

            Returns:
                ~.asset_service.ListAssetsResponse:
                    ListAssets response.
            """

            http_options: List[Dict[str, str]] = [{
                'method': 'get',
                'uri': '/v1/{parent=*/*}/assets',
            },
            ]
            request, metadata = self._interceptor.pre_list_assets(request, metadata)
            pb_request = asset_service.ListAssetsRequest.pb(request)
            transcoded_request = path_template.transcode(http_options, pb_request)

            uri = transcoded_request['uri']
            method = transcoded_request['method']

            # Jsonify the query params
            query_params = json.loads(json_format.MessageToJson(
                transcoded_request['query_params'],
                including_default_value_fields=False,
                use_integers_for_enums=False,
            ))
            query_params.update(self._get_unset_required_fields(query_params))

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
            resp = asset_service.ListAssetsResponse()
            pb_resp = asset_service.ListAssetsResponse.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)
            resp = self._interceptor.post_list_assets(resp)
            return resp

    class _ListFeeds(AssetServiceRestStub):
        def __hash__(self):
            return hash("ListFeeds")

        __REQUIRED_FIELDS_DEFAULT_VALUES: Dict[str, str] =  {
        }

        @classmethod
        def _get_unset_required_fields(cls, message_dict):
            return {k: v for k, v in cls.__REQUIRED_FIELDS_DEFAULT_VALUES.items() if k not in message_dict}

        def __call__(self,
                request: asset_service.ListFeedsRequest, *,
                retry: OptionalRetry=gapic_v1.method.DEFAULT,
                timeout: Optional[float]=None,
                metadata: Sequence[Tuple[str, str]]=(),
                ) -> asset_service.ListFeedsResponse:
            r"""Call the list feeds method over HTTP.

            Args:
                request (~.asset_service.ListFeedsRequest):
                    The request object. List asset feeds request.
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, str]]): Strings which should be
                    sent along with the request as metadata.

            Returns:
                ~.asset_service.ListFeedsResponse:

            """

            http_options: List[Dict[str, str]] = [{
                'method': 'get',
                'uri': '/v1/{parent=*/*}/feeds',
            },
            ]
            request, metadata = self._interceptor.pre_list_feeds(request, metadata)
            pb_request = asset_service.ListFeedsRequest.pb(request)
            transcoded_request = path_template.transcode(http_options, pb_request)

            uri = transcoded_request['uri']
            method = transcoded_request['method']

            # Jsonify the query params
            query_params = json.loads(json_format.MessageToJson(
                transcoded_request['query_params'],
                including_default_value_fields=False,
                use_integers_for_enums=False,
            ))
            query_params.update(self._get_unset_required_fields(query_params))

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
            resp = asset_service.ListFeedsResponse()
            pb_resp = asset_service.ListFeedsResponse.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)
            resp = self._interceptor.post_list_feeds(resp)
            return resp

    class _SearchAllIamPolicies(AssetServiceRestStub):
        def __hash__(self):
            return hash("SearchAllIamPolicies")

        __REQUIRED_FIELDS_DEFAULT_VALUES: Dict[str, str] =  {
        }

        @classmethod
        def _get_unset_required_fields(cls, message_dict):
            return {k: v for k, v in cls.__REQUIRED_FIELDS_DEFAULT_VALUES.items() if k not in message_dict}

        def __call__(self,
                request: asset_service.SearchAllIamPoliciesRequest, *,
                retry: OptionalRetry=gapic_v1.method.DEFAULT,
                timeout: Optional[float]=None,
                metadata: Sequence[Tuple[str, str]]=(),
                ) -> asset_service.SearchAllIamPoliciesResponse:
            r"""Call the search all iam policies method over HTTP.

            Args:
                request (~.asset_service.SearchAllIamPoliciesRequest):
                    The request object. Search all IAM policies request.
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, str]]): Strings which should be
                    sent along with the request as metadata.

            Returns:
                ~.asset_service.SearchAllIamPoliciesResponse:
                    Search all IAM policies response.
            """

            http_options: List[Dict[str, str]] = [{
                'method': 'get',
                'uri': '/v1/{scope=*/*}:searchAllIamPolicies',
            },
            ]
            request, metadata = self._interceptor.pre_search_all_iam_policies(request, metadata)
            pb_request = asset_service.SearchAllIamPoliciesRequest.pb(request)
            transcoded_request = path_template.transcode(http_options, pb_request)

            uri = transcoded_request['uri']
            method = transcoded_request['method']

            # Jsonify the query params
            query_params = json.loads(json_format.MessageToJson(
                transcoded_request['query_params'],
                including_default_value_fields=False,
                use_integers_for_enums=False,
            ))
            query_params.update(self._get_unset_required_fields(query_params))

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
            resp = asset_service.SearchAllIamPoliciesResponse()
            pb_resp = asset_service.SearchAllIamPoliciesResponse.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)
            resp = self._interceptor.post_search_all_iam_policies(resp)
            return resp

    class _SearchAllResources(AssetServiceRestStub):
        def __hash__(self):
            return hash("SearchAllResources")

        __REQUIRED_FIELDS_DEFAULT_VALUES: Dict[str, str] =  {
        }

        @classmethod
        def _get_unset_required_fields(cls, message_dict):
            return {k: v for k, v in cls.__REQUIRED_FIELDS_DEFAULT_VALUES.items() if k not in message_dict}

        def __call__(self,
                request: asset_service.SearchAllResourcesRequest, *,
                retry: OptionalRetry=gapic_v1.method.DEFAULT,
                timeout: Optional[float]=None,
                metadata: Sequence[Tuple[str, str]]=(),
                ) -> asset_service.SearchAllResourcesResponse:
            r"""Call the search all resources method over HTTP.

            Args:
                request (~.asset_service.SearchAllResourcesRequest):
                    The request object. Search all resources request.
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, str]]): Strings which should be
                    sent along with the request as metadata.

            Returns:
                ~.asset_service.SearchAllResourcesResponse:
                    Search all resources response.
            """

            http_options: List[Dict[str, str]] = [{
                'method': 'get',
                'uri': '/v1/{scope=*/*}:searchAllResources',
            },
            ]
            request, metadata = self._interceptor.pre_search_all_resources(request, metadata)
            pb_request = asset_service.SearchAllResourcesRequest.pb(request)
            transcoded_request = path_template.transcode(http_options, pb_request)

            uri = transcoded_request['uri']
            method = transcoded_request['method']

            # Jsonify the query params
            query_params = json.loads(json_format.MessageToJson(
                transcoded_request['query_params'],
                including_default_value_fields=False,
                use_integers_for_enums=False,
            ))
            query_params.update(self._get_unset_required_fields(query_params))

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
            resp = asset_service.SearchAllResourcesResponse()
            pb_resp = asset_service.SearchAllResourcesResponse.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)
            resp = self._interceptor.post_search_all_resources(resp)
            return resp

    class _UpdateFeed(AssetServiceRestStub):
        def __hash__(self):
            return hash("UpdateFeed")

        __REQUIRED_FIELDS_DEFAULT_VALUES: Dict[str, str] =  {
        }

        @classmethod
        def _get_unset_required_fields(cls, message_dict):
            return {k: v for k, v in cls.__REQUIRED_FIELDS_DEFAULT_VALUES.items() if k not in message_dict}

        def __call__(self,
                request: asset_service.UpdateFeedRequest, *,
                retry: OptionalRetry=gapic_v1.method.DEFAULT,
                timeout: Optional[float]=None,
                metadata: Sequence[Tuple[str, str]]=(),
                ) -> asset_service.Feed:
            r"""Call the update feed method over HTTP.

            Args:
                request (~.asset_service.UpdateFeedRequest):
                    The request object. Update asset feed request.
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, str]]): Strings which should be
                    sent along with the request as metadata.

            Returns:
                ~.asset_service.Feed:
                    An asset feed used to export asset
                updates to a destinations. An asset feed
                filter controls what updates are
                exported. The asset feed must be created
                within a project, organization, or
                folder. Supported destinations are:
                Pub/Sub topics.

            """

            http_options: List[Dict[str, str]] = [{
                'method': 'patch',
                'uri': '/v1/{feed.name=*/*/feeds/*}',
                'body': '*',
            },
            ]
            request, metadata = self._interceptor.pre_update_feed(request, metadata)
            pb_request = asset_service.UpdateFeedRequest.pb(request)
            transcoded_request = path_template.transcode(http_options, pb_request)

            # Jsonify the request body

            body = json_format.MessageToJson(
                transcoded_request['body'],
                including_default_value_fields=False,
                use_integers_for_enums=False
            )
            uri = transcoded_request['uri']
            method = transcoded_request['method']

            # Jsonify the query params
            query_params = json.loads(json_format.MessageToJson(
                transcoded_request['query_params'],
                including_default_value_fields=False,
                use_integers_for_enums=False,
            ))
            query_params.update(self._get_unset_required_fields(query_params))

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
            resp = asset_service.Feed()
            pb_resp = asset_service.Feed.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)
            resp = self._interceptor.post_update_feed(resp)
            return resp

    @property
    def analyze_iam_policy(self) -> Callable[
            [asset_service.AnalyzeIamPolicyRequest],
            asset_service.AnalyzeIamPolicyResponse]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._AnalyzeIamPolicy(self._session, self._host, self._interceptor) # type: ignore

    @property
    def analyze_iam_policy_longrunning(self) -> Callable[
            [asset_service.AnalyzeIamPolicyLongrunningRequest],
            operations_pb2.Operation]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._AnalyzeIamPolicyLongrunning(self._session, self._host, self._interceptor) # type: ignore

    @property
    def batch_get_assets_history(self) -> Callable[
            [asset_service.BatchGetAssetsHistoryRequest],
            asset_service.BatchGetAssetsHistoryResponse]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._BatchGetAssetsHistory(self._session, self._host, self._interceptor) # type: ignore

    @property
    def create_feed(self) -> Callable[
            [asset_service.CreateFeedRequest],
            asset_service.Feed]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._CreateFeed(self._session, self._host, self._interceptor) # type: ignore

    @property
    def delete_feed(self) -> Callable[
            [asset_service.DeleteFeedRequest],
            empty_pb2.Empty]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._DeleteFeed(self._session, self._host, self._interceptor) # type: ignore

    @property
    def export_assets(self) -> Callable[
            [asset_service.ExportAssetsRequest],
            operations_pb2.Operation]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._ExportAssets(self._session, self._host, self._interceptor) # type: ignore

    @property
    def get_feed(self) -> Callable[
            [asset_service.GetFeedRequest],
            asset_service.Feed]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._GetFeed(self._session, self._host, self._interceptor) # type: ignore

    @property
    def list_assets(self) -> Callable[
            [asset_service.ListAssetsRequest],
            asset_service.ListAssetsResponse]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._ListAssets(self._session, self._host, self._interceptor) # type: ignore

    @property
    def list_feeds(self) -> Callable[
            [asset_service.ListFeedsRequest],
            asset_service.ListFeedsResponse]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._ListFeeds(self._session, self._host, self._interceptor) # type: ignore

    @property
    def search_all_iam_policies(self) -> Callable[
            [asset_service.SearchAllIamPoliciesRequest],
            asset_service.SearchAllIamPoliciesResponse]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._SearchAllIamPolicies(self._session, self._host, self._interceptor) # type: ignore

    @property
    def search_all_resources(self) -> Callable[
            [asset_service.SearchAllResourcesRequest],
            asset_service.SearchAllResourcesResponse]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._SearchAllResources(self._session, self._host, self._interceptor) # type: ignore

    @property
    def update_feed(self) -> Callable[
            [asset_service.UpdateFeedRequest],
            asset_service.Feed]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._UpdateFeed(self._session, self._host, self._interceptor) # type: ignore

    @property
    def kind(self) -> str:
        return "rest"

    def close(self):
        self._session.close()


__all__=(
    'AssetServiceRestTransport',
)

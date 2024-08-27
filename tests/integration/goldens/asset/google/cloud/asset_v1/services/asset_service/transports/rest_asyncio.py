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

from google.auth.aio.transport.sessions import AuthorizedSession  # type: ignore
import json  # type: ignore
from google.auth.aio import credentials as ga_credentials_async  # type: ignore
from google.api_core import exceptions as core_exceptions
from google.api_core import retry_async as retries_async
from google.api_core import rest_helpers
from google.api_core import rest_streaming_async
from google.api_core import gapic_v1

from google.protobuf import json_format

import dataclasses
from typing import Any, Callable, Dict, List, Optional, Sequence, Tuple, Union
import warnings

from .rest_base import _BaseAssetServiceRestTransport


from google.cloud.asset_v1.types import asset_service
from google.protobuf import empty_pb2  # type: ignore
from google.longrunning import operations_pb2  # type: ignore


from .base import DEFAULT_CLIENT_INFO as BASE_DEFAULT_CLIENT_INFO

try:
    OptionalRetry = Union[retries_async.AsyncRetry, gapic_v1.method._MethodDefault, None]
except AttributeError:  # pragma: NO COVER
    OptionalRetry = Union[retries_async.AsyncRetry, object, None]  # type: ignore

DEFAULT_CLIENT_INFO = gapic_v1.client_info.ClientInfo(
    gapic_version=BASE_DEFAULT_CLIENT_INFO.gapic_version,
    grpc_version=None,
    rest_version=None,
)

@dataclasses.dataclass
class AsyncAssetServiceRestStub:
    _session: AuthorizedSession
    _host: str
    _interceptor: None

class AsyncAssetServiceRestTransport(_BaseAssetServiceRestTransport):
    """Asynchronous REST backend transport for AssetService.

    Asset service definition.

    This class defines the same methods as the primary client, so the
    primary client can load the underlying transport implementation
    and call it.

    It sends JSON representations of protocol buffers over HTTP/1.1

    NOTE: This async REST transport functionality is currently in a beta
    state (preview). We welcome your feedback via an issue in this
    library's source repository. Thank you!
    """

    def __init__(self, *,
            host: str = 'cloudasset.googleapis.com',
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
                 The hostname to connect to (default: 'cloudasset.googleapis.com').
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
            url_scheme: the protocol scheme for the API endpoint.  Normally
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
        self._session = AuthorizedSession(
            self._credentials)
        self._prep_wrapped_messages(client_info)

    class _AnalyzeIamPolicy(_BaseAssetServiceRestTransport._BaseAnalyzeIamPolicy, AsyncAssetServiceRestStub):

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
            response = await getattr(session, method)(
                "{host}{uri}".format(host=host, uri=uri),
                timeout=timeout,
                headers=headers,
                params=rest_helpers.flatten_query_params(query_params, strict=True),
                )
            return response

        async def __call__(self,
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

            http_options = _BaseAssetServiceRestTransport._BaseAnalyzeIamPolicy._get_http_options()
            transcoded_request = _BaseAssetServiceRestTransport._BaseAnalyzeIamPolicy._get_transcoded_request(http_options, request)

            # Jsonify the query params
            query_params = _BaseAssetServiceRestTransport._BaseAnalyzeIamPolicy._get_query_params_json(transcoded_request)

            # Send the request
            response = await AsyncAssetServiceRestTransport._AnalyzeIamPolicy._get_response(self._host, metadata, query_params, self._session, timeout, transcoded_request)

            # In case of error, raise the appropriate core_exceptions.GoogleAPICallError exception
            # subclass.
            if response.status_code >= 400:
                raise core_exceptions.from_http_response(response)

            # Return the response
            return response

    class _AnalyzeIamPolicyLongrunning(_BaseAssetServiceRestTransport._BaseAnalyzeIamPolicyLongrunning, AsyncAssetServiceRestStub):

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
            response = await getattr(session, method)(
                "{host}{uri}".format(host=host, uri=uri),
                timeout=timeout,
                headers=headers,
                params=rest_helpers.flatten_query_params(query_params, strict=True),
                data=body,
                )
            return response

        async def __call__(self,
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

            http_options = _BaseAssetServiceRestTransport._BaseAnalyzeIamPolicyLongrunning._get_http_options()
            transcoded_request = _BaseAssetServiceRestTransport._BaseAnalyzeIamPolicyLongrunning._get_transcoded_request(http_options, request)

            body = _BaseAssetServiceRestTransport._BaseAnalyzeIamPolicyLongrunning._get_request_body_json(transcoded_request)

            # Jsonify the query params
            query_params = _BaseAssetServiceRestTransport._BaseAnalyzeIamPolicyLongrunning._get_query_params_json(transcoded_request)

            # Send the request
            response = await AsyncAssetServiceRestTransport._AnalyzeIamPolicyLongrunning._get_response(self._host, metadata, query_params, self._session, timeout, transcoded_request, body)

            # In case of error, raise the appropriate core_exceptions.GoogleAPICallError exception
            # subclass.
            if response.status_code >= 400:
                raise core_exceptions.from_http_response(response)

            # Return the response
            return response

    class _AnalyzeMove(_BaseAssetServiceRestTransport._BaseAnalyzeMove, AsyncAssetServiceRestStub):

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
            response = await getattr(session, method)(
                "{host}{uri}".format(host=host, uri=uri),
                timeout=timeout,
                headers=headers,
                params=rest_helpers.flatten_query_params(query_params, strict=True),
                )
            return response

        async def __call__(self,
                request: asset_service.AnalyzeMoveRequest, *,
                retry: OptionalRetry=gapic_v1.method.DEFAULT,
                timeout: Optional[float]=None,
                metadata: Sequence[Tuple[str, str]]=(),
                ) -> asset_service.AnalyzeMoveResponse:
            r"""Call the analyze move method over HTTP.

            Args:
                request (~.asset_service.AnalyzeMoveRequest):
                    The request object. The request message for performing
                resource move analysis.
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, str]]): Strings which should be
                    sent along with the request as metadata.

            Returns:
                ~.asset_service.AnalyzeMoveResponse:
                    The response message for resource
                move analysis.

            """

            http_options = _BaseAssetServiceRestTransport._BaseAnalyzeMove._get_http_options()
            transcoded_request = _BaseAssetServiceRestTransport._BaseAnalyzeMove._get_transcoded_request(http_options, request)

            # Jsonify the query params
            query_params = _BaseAssetServiceRestTransport._BaseAnalyzeMove._get_query_params_json(transcoded_request)

            # Send the request
            response = await AsyncAssetServiceRestTransport._AnalyzeMove._get_response(self._host, metadata, query_params, self._session, timeout, transcoded_request)

            # In case of error, raise the appropriate core_exceptions.GoogleAPICallError exception
            # subclass.
            if response.status_code >= 400:
                raise core_exceptions.from_http_response(response)

            # Return the response
            return response

    class _AnalyzeOrgPolicies(_BaseAssetServiceRestTransport._BaseAnalyzeOrgPolicies, AsyncAssetServiceRestStub):

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
            response = await getattr(session, method)(
                "{host}{uri}".format(host=host, uri=uri),
                timeout=timeout,
                headers=headers,
                params=rest_helpers.flatten_query_params(query_params, strict=True),
                )
            return response

        async def __call__(self,
                request: asset_service.AnalyzeOrgPoliciesRequest, *,
                retry: OptionalRetry=gapic_v1.method.DEFAULT,
                timeout: Optional[float]=None,
                metadata: Sequence[Tuple[str, str]]=(),
                ) -> asset_service.AnalyzeOrgPoliciesResponse:
            r"""Call the analyze org policies method over HTTP.

            Args:
                request (~.asset_service.AnalyzeOrgPoliciesRequest):
                    The request object. A request message for
                [AssetService.AnalyzeOrgPolicies][google.cloud.asset.v1.AssetService.AnalyzeOrgPolicies].
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, str]]): Strings which should be
                    sent along with the request as metadata.

            Returns:
                ~.asset_service.AnalyzeOrgPoliciesResponse:
                    The response message for
                [AssetService.AnalyzeOrgPolicies][google.cloud.asset.v1.AssetService.AnalyzeOrgPolicies].

            """

            http_options = _BaseAssetServiceRestTransport._BaseAnalyzeOrgPolicies._get_http_options()
            transcoded_request = _BaseAssetServiceRestTransport._BaseAnalyzeOrgPolicies._get_transcoded_request(http_options, request)

            # Jsonify the query params
            query_params = _BaseAssetServiceRestTransport._BaseAnalyzeOrgPolicies._get_query_params_json(transcoded_request)

            # Send the request
            response = await AsyncAssetServiceRestTransport._AnalyzeOrgPolicies._get_response(self._host, metadata, query_params, self._session, timeout, transcoded_request)

            # In case of error, raise the appropriate core_exceptions.GoogleAPICallError exception
            # subclass.
            if response.status_code >= 400:
                raise core_exceptions.from_http_response(response)

            # Return the response
            return response

    class _AnalyzeOrgPolicyGovernedAssets(_BaseAssetServiceRestTransport._BaseAnalyzeOrgPolicyGovernedAssets, AsyncAssetServiceRestStub):

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
            response = await getattr(session, method)(
                "{host}{uri}".format(host=host, uri=uri),
                timeout=timeout,
                headers=headers,
                params=rest_helpers.flatten_query_params(query_params, strict=True),
                )
            return response

        async def __call__(self,
                request: asset_service.AnalyzeOrgPolicyGovernedAssetsRequest, *,
                retry: OptionalRetry=gapic_v1.method.DEFAULT,
                timeout: Optional[float]=None,
                metadata: Sequence[Tuple[str, str]]=(),
                ) -> asset_service.AnalyzeOrgPolicyGovernedAssetsResponse:
            r"""Call the analyze org policy
        governed assets method over HTTP.

            Args:
                request (~.asset_service.AnalyzeOrgPolicyGovernedAssetsRequest):
                    The request object. A request message for
                [AssetService.AnalyzeOrgPolicyGovernedAssets][google.cloud.asset.v1.AssetService.AnalyzeOrgPolicyGovernedAssets].
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, str]]): Strings which should be
                    sent along with the request as metadata.

            Returns:
                ~.asset_service.AnalyzeOrgPolicyGovernedAssetsResponse:
                    The response message for
                [AssetService.AnalyzeOrgPolicyGovernedAssets][google.cloud.asset.v1.AssetService.AnalyzeOrgPolicyGovernedAssets].

            """

            http_options = _BaseAssetServiceRestTransport._BaseAnalyzeOrgPolicyGovernedAssets._get_http_options()
            transcoded_request = _BaseAssetServiceRestTransport._BaseAnalyzeOrgPolicyGovernedAssets._get_transcoded_request(http_options, request)

            # Jsonify the query params
            query_params = _BaseAssetServiceRestTransport._BaseAnalyzeOrgPolicyGovernedAssets._get_query_params_json(transcoded_request)

            # Send the request
            response = await AsyncAssetServiceRestTransport._AnalyzeOrgPolicyGovernedAssets._get_response(self._host, metadata, query_params, self._session, timeout, transcoded_request)

            # In case of error, raise the appropriate core_exceptions.GoogleAPICallError exception
            # subclass.
            if response.status_code >= 400:
                raise core_exceptions.from_http_response(response)

            # Return the response
            return response

    class _AnalyzeOrgPolicyGovernedContainers(_BaseAssetServiceRestTransport._BaseAnalyzeOrgPolicyGovernedContainers, AsyncAssetServiceRestStub):

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
            response = await getattr(session, method)(
                "{host}{uri}".format(host=host, uri=uri),
                timeout=timeout,
                headers=headers,
                params=rest_helpers.flatten_query_params(query_params, strict=True),
                )
            return response

        async def __call__(self,
                request: asset_service.AnalyzeOrgPolicyGovernedContainersRequest, *,
                retry: OptionalRetry=gapic_v1.method.DEFAULT,
                timeout: Optional[float]=None,
                metadata: Sequence[Tuple[str, str]]=(),
                ) -> asset_service.AnalyzeOrgPolicyGovernedContainersResponse:
            r"""Call the analyze org policy
        governed containers method over HTTP.

            Args:
                request (~.asset_service.AnalyzeOrgPolicyGovernedContainersRequest):
                    The request object. A request message for
                [AssetService.AnalyzeOrgPolicyGovernedContainers][google.cloud.asset.v1.AssetService.AnalyzeOrgPolicyGovernedContainers].
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, str]]): Strings which should be
                    sent along with the request as metadata.

            Returns:
                ~.asset_service.AnalyzeOrgPolicyGovernedContainersResponse:
                    The response message for
                [AssetService.AnalyzeOrgPolicyGovernedContainers][google.cloud.asset.v1.AssetService.AnalyzeOrgPolicyGovernedContainers].

            """

            http_options = _BaseAssetServiceRestTransport._BaseAnalyzeOrgPolicyGovernedContainers._get_http_options()
            transcoded_request = _BaseAssetServiceRestTransport._BaseAnalyzeOrgPolicyGovernedContainers._get_transcoded_request(http_options, request)

            # Jsonify the query params
            query_params = _BaseAssetServiceRestTransport._BaseAnalyzeOrgPolicyGovernedContainers._get_query_params_json(transcoded_request)

            # Send the request
            response = await AsyncAssetServiceRestTransport._AnalyzeOrgPolicyGovernedContainers._get_response(self._host, metadata, query_params, self._session, timeout, transcoded_request)

            # In case of error, raise the appropriate core_exceptions.GoogleAPICallError exception
            # subclass.
            if response.status_code >= 400:
                raise core_exceptions.from_http_response(response)

            # Return the response
            return response

    class _BatchGetAssetsHistory(_BaseAssetServiceRestTransport._BaseBatchGetAssetsHistory, AsyncAssetServiceRestStub):

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
            response = await getattr(session, method)(
                "{host}{uri}".format(host=host, uri=uri),
                timeout=timeout,
                headers=headers,
                params=rest_helpers.flatten_query_params(query_params, strict=True),
                )
            return response

        async def __call__(self,
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

            http_options = _BaseAssetServiceRestTransport._BaseBatchGetAssetsHistory._get_http_options()
            transcoded_request = _BaseAssetServiceRestTransport._BaseBatchGetAssetsHistory._get_transcoded_request(http_options, request)

            # Jsonify the query params
            query_params = _BaseAssetServiceRestTransport._BaseBatchGetAssetsHistory._get_query_params_json(transcoded_request)

            # Send the request
            response = await AsyncAssetServiceRestTransport._BatchGetAssetsHistory._get_response(self._host, metadata, query_params, self._session, timeout, transcoded_request)

            # In case of error, raise the appropriate core_exceptions.GoogleAPICallError exception
            # subclass.
            if response.status_code >= 400:
                raise core_exceptions.from_http_response(response)

            # Return the response
            return response

    class _BatchGetEffectiveIamPolicies(_BaseAssetServiceRestTransport._BaseBatchGetEffectiveIamPolicies, AsyncAssetServiceRestStub):

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
            response = await getattr(session, method)(
                "{host}{uri}".format(host=host, uri=uri),
                timeout=timeout,
                headers=headers,
                params=rest_helpers.flatten_query_params(query_params, strict=True),
                )
            return response

        async def __call__(self,
                request: asset_service.BatchGetEffectiveIamPoliciesRequest, *,
                retry: OptionalRetry=gapic_v1.method.DEFAULT,
                timeout: Optional[float]=None,
                metadata: Sequence[Tuple[str, str]]=(),
                ) -> asset_service.BatchGetEffectiveIamPoliciesResponse:
            r"""Call the batch get effective iam
        policies method over HTTP.

            Args:
                request (~.asset_service.BatchGetEffectiveIamPoliciesRequest):
                    The request object. A request message for
                [AssetService.BatchGetEffectiveIamPolicies][google.cloud.asset.v1.AssetService.BatchGetEffectiveIamPolicies].
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, str]]): Strings which should be
                    sent along with the request as metadata.

            Returns:
                ~.asset_service.BatchGetEffectiveIamPoliciesResponse:
                    A response message for
                [AssetService.BatchGetEffectiveIamPolicies][google.cloud.asset.v1.AssetService.BatchGetEffectiveIamPolicies].

            """

            http_options = _BaseAssetServiceRestTransport._BaseBatchGetEffectiveIamPolicies._get_http_options()
            transcoded_request = _BaseAssetServiceRestTransport._BaseBatchGetEffectiveIamPolicies._get_transcoded_request(http_options, request)

            # Jsonify the query params
            query_params = _BaseAssetServiceRestTransport._BaseBatchGetEffectiveIamPolicies._get_query_params_json(transcoded_request)

            # Send the request
            response = await AsyncAssetServiceRestTransport._BatchGetEffectiveIamPolicies._get_response(self._host, metadata, query_params, self._session, timeout, transcoded_request)

            # In case of error, raise the appropriate core_exceptions.GoogleAPICallError exception
            # subclass.
            if response.status_code >= 400:
                raise core_exceptions.from_http_response(response)

            # Return the response
            return response

    class _CreateFeed(_BaseAssetServiceRestTransport._BaseCreateFeed, AsyncAssetServiceRestStub):

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
            response = await getattr(session, method)(
                "{host}{uri}".format(host=host, uri=uri),
                timeout=timeout,
                headers=headers,
                params=rest_helpers.flatten_query_params(query_params, strict=True),
                data=body,
                )
            return response

        async def __call__(self,
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

            http_options = _BaseAssetServiceRestTransport._BaseCreateFeed._get_http_options()
            transcoded_request = _BaseAssetServiceRestTransport._BaseCreateFeed._get_transcoded_request(http_options, request)

            body = _BaseAssetServiceRestTransport._BaseCreateFeed._get_request_body_json(transcoded_request)

            # Jsonify the query params
            query_params = _BaseAssetServiceRestTransport._BaseCreateFeed._get_query_params_json(transcoded_request)

            # Send the request
            response = await AsyncAssetServiceRestTransport._CreateFeed._get_response(self._host, metadata, query_params, self._session, timeout, transcoded_request, body)

            # In case of error, raise the appropriate core_exceptions.GoogleAPICallError exception
            # subclass.
            if response.status_code >= 400:
                raise core_exceptions.from_http_response(response)

            # Return the response
            return response

    class _CreateSavedQuery(_BaseAssetServiceRestTransport._BaseCreateSavedQuery, AsyncAssetServiceRestStub):

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
            response = await getattr(session, method)(
                "{host}{uri}".format(host=host, uri=uri),
                timeout=timeout,
                headers=headers,
                params=rest_helpers.flatten_query_params(query_params, strict=True),
                data=body,
                )
            return response

        async def __call__(self,
                request: asset_service.CreateSavedQueryRequest, *,
                retry: OptionalRetry=gapic_v1.method.DEFAULT,
                timeout: Optional[float]=None,
                metadata: Sequence[Tuple[str, str]]=(),
                ) -> asset_service.SavedQuery:
            r"""Call the create saved query method over HTTP.

            Args:
                request (~.asset_service.CreateSavedQueryRequest):
                    The request object. Request to create a saved query.
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, str]]): Strings which should be
                    sent along with the request as metadata.

            Returns:
                ~.asset_service.SavedQuery:
                    A saved query which can be shared
                with others or used later.

            """

            http_options = _BaseAssetServiceRestTransport._BaseCreateSavedQuery._get_http_options()
            transcoded_request = _BaseAssetServiceRestTransport._BaseCreateSavedQuery._get_transcoded_request(http_options, request)

            body = _BaseAssetServiceRestTransport._BaseCreateSavedQuery._get_request_body_json(transcoded_request)

            # Jsonify the query params
            query_params = _BaseAssetServiceRestTransport._BaseCreateSavedQuery._get_query_params_json(transcoded_request)

            # Send the request
            response = await AsyncAssetServiceRestTransport._CreateSavedQuery._get_response(self._host, metadata, query_params, self._session, timeout, transcoded_request, body)

            # In case of error, raise the appropriate core_exceptions.GoogleAPICallError exception
            # subclass.
            if response.status_code >= 400:
                raise core_exceptions.from_http_response(response)

            # Return the response
            return response

    class _DeleteFeed(_BaseAssetServiceRestTransport._BaseDeleteFeed, AsyncAssetServiceRestStub):

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
            response = await getattr(session, method)(
                "{host}{uri}".format(host=host, uri=uri),
                timeout=timeout,
                headers=headers,
                params=rest_helpers.flatten_query_params(query_params, strict=True),
                )
            return response

        async def __call__(self,
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

            http_options = _BaseAssetServiceRestTransport._BaseDeleteFeed._get_http_options()
            transcoded_request = _BaseAssetServiceRestTransport._BaseDeleteFeed._get_transcoded_request(http_options, request)

            # Jsonify the query params
            query_params = _BaseAssetServiceRestTransport._BaseDeleteFeed._get_query_params_json(transcoded_request)

            # Send the request
            response = await AsyncAssetServiceRestTransport._DeleteFeed._get_response(self._host, metadata, query_params, self._session, timeout, transcoded_request)

            # In case of error, raise the appropriate core_exceptions.GoogleAPICallError exception
            # subclass.
            if response.status_code >= 400:
                raise core_exceptions.from_http_response(response)

    class _DeleteSavedQuery(_BaseAssetServiceRestTransport._BaseDeleteSavedQuery, AsyncAssetServiceRestStub):

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
            response = await getattr(session, method)(
                "{host}{uri}".format(host=host, uri=uri),
                timeout=timeout,
                headers=headers,
                params=rest_helpers.flatten_query_params(query_params, strict=True),
                )
            return response

        async def __call__(self,
                request: asset_service.DeleteSavedQueryRequest, *,
                retry: OptionalRetry=gapic_v1.method.DEFAULT,
                timeout: Optional[float]=None,
                metadata: Sequence[Tuple[str, str]]=(),
                ):
            r"""Call the delete saved query method over HTTP.

            Args:
                request (~.asset_service.DeleteSavedQueryRequest):
                    The request object. Request to delete a saved query.
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, str]]): Strings which should be
                    sent along with the request as metadata.
            """

            http_options = _BaseAssetServiceRestTransport._BaseDeleteSavedQuery._get_http_options()
            transcoded_request = _BaseAssetServiceRestTransport._BaseDeleteSavedQuery._get_transcoded_request(http_options, request)

            # Jsonify the query params
            query_params = _BaseAssetServiceRestTransport._BaseDeleteSavedQuery._get_query_params_json(transcoded_request)

            # Send the request
            response = await AsyncAssetServiceRestTransport._DeleteSavedQuery._get_response(self._host, metadata, query_params, self._session, timeout, transcoded_request)

            # In case of error, raise the appropriate core_exceptions.GoogleAPICallError exception
            # subclass.
            if response.status_code >= 400:
                raise core_exceptions.from_http_response(response)

    class _ExportAssets(_BaseAssetServiceRestTransport._BaseExportAssets, AsyncAssetServiceRestStub):

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
            response = await getattr(session, method)(
                "{host}{uri}".format(host=host, uri=uri),
                timeout=timeout,
                headers=headers,
                params=rest_helpers.flatten_query_params(query_params, strict=True),
                data=body,
                )
            return response

        async def __call__(self,
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

            http_options = _BaseAssetServiceRestTransport._BaseExportAssets._get_http_options()
            transcoded_request = _BaseAssetServiceRestTransport._BaseExportAssets._get_transcoded_request(http_options, request)

            body = _BaseAssetServiceRestTransport._BaseExportAssets._get_request_body_json(transcoded_request)

            # Jsonify the query params
            query_params = _BaseAssetServiceRestTransport._BaseExportAssets._get_query_params_json(transcoded_request)

            # Send the request
            response = await AsyncAssetServiceRestTransport._ExportAssets._get_response(self._host, metadata, query_params, self._session, timeout, transcoded_request, body)

            # In case of error, raise the appropriate core_exceptions.GoogleAPICallError exception
            # subclass.
            if response.status_code >= 400:
                raise core_exceptions.from_http_response(response)

            # Return the response
            return response

    class _GetFeed(_BaseAssetServiceRestTransport._BaseGetFeed, AsyncAssetServiceRestStub):

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
            response = await getattr(session, method)(
                "{host}{uri}".format(host=host, uri=uri),
                timeout=timeout,
                headers=headers,
                params=rest_helpers.flatten_query_params(query_params, strict=True),
                )
            return response

        async def __call__(self,
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

            http_options = _BaseAssetServiceRestTransport._BaseGetFeed._get_http_options()
            transcoded_request = _BaseAssetServiceRestTransport._BaseGetFeed._get_transcoded_request(http_options, request)

            # Jsonify the query params
            query_params = _BaseAssetServiceRestTransport._BaseGetFeed._get_query_params_json(transcoded_request)

            # Send the request
            response = await AsyncAssetServiceRestTransport._GetFeed._get_response(self._host, metadata, query_params, self._session, timeout, transcoded_request)

            # In case of error, raise the appropriate core_exceptions.GoogleAPICallError exception
            # subclass.
            if response.status_code >= 400:
                raise core_exceptions.from_http_response(response)

            # Return the response
            return response

    class _GetSavedQuery(_BaseAssetServiceRestTransport._BaseGetSavedQuery, AsyncAssetServiceRestStub):

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
            response = await getattr(session, method)(
                "{host}{uri}".format(host=host, uri=uri),
                timeout=timeout,
                headers=headers,
                params=rest_helpers.flatten_query_params(query_params, strict=True),
                )
            return response

        async def __call__(self,
                request: asset_service.GetSavedQueryRequest, *,
                retry: OptionalRetry=gapic_v1.method.DEFAULT,
                timeout: Optional[float]=None,
                metadata: Sequence[Tuple[str, str]]=(),
                ) -> asset_service.SavedQuery:
            r"""Call the get saved query method over HTTP.

            Args:
                request (~.asset_service.GetSavedQueryRequest):
                    The request object. Request to get a saved query.
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, str]]): Strings which should be
                    sent along with the request as metadata.

            Returns:
                ~.asset_service.SavedQuery:
                    A saved query which can be shared
                with others or used later.

            """

            http_options = _BaseAssetServiceRestTransport._BaseGetSavedQuery._get_http_options()
            transcoded_request = _BaseAssetServiceRestTransport._BaseGetSavedQuery._get_transcoded_request(http_options, request)

            # Jsonify the query params
            query_params = _BaseAssetServiceRestTransport._BaseGetSavedQuery._get_query_params_json(transcoded_request)

            # Send the request
            response = await AsyncAssetServiceRestTransport._GetSavedQuery._get_response(self._host, metadata, query_params, self._session, timeout, transcoded_request)

            # In case of error, raise the appropriate core_exceptions.GoogleAPICallError exception
            # subclass.
            if response.status_code >= 400:
                raise core_exceptions.from_http_response(response)

            # Return the response
            return response

    class _ListAssets(_BaseAssetServiceRestTransport._BaseListAssets, AsyncAssetServiceRestStub):

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
            response = await getattr(session, method)(
                "{host}{uri}".format(host=host, uri=uri),
                timeout=timeout,
                headers=headers,
                params=rest_helpers.flatten_query_params(query_params, strict=True),
                )
            return response

        async def __call__(self,
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

            http_options = _BaseAssetServiceRestTransport._BaseListAssets._get_http_options()
            transcoded_request = _BaseAssetServiceRestTransport._BaseListAssets._get_transcoded_request(http_options, request)

            # Jsonify the query params
            query_params = _BaseAssetServiceRestTransport._BaseListAssets._get_query_params_json(transcoded_request)

            # Send the request
            response = await AsyncAssetServiceRestTransport._ListAssets._get_response(self._host, metadata, query_params, self._session, timeout, transcoded_request)

            # In case of error, raise the appropriate core_exceptions.GoogleAPICallError exception
            # subclass.
            if response.status_code >= 400:
                raise core_exceptions.from_http_response(response)

            # Return the response
            return response

    class _ListFeeds(_BaseAssetServiceRestTransport._BaseListFeeds, AsyncAssetServiceRestStub):

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
            response = await getattr(session, method)(
                "{host}{uri}".format(host=host, uri=uri),
                timeout=timeout,
                headers=headers,
                params=rest_helpers.flatten_query_params(query_params, strict=True),
                )
            return response

        async def __call__(self,
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

            http_options = _BaseAssetServiceRestTransport._BaseListFeeds._get_http_options()
            transcoded_request = _BaseAssetServiceRestTransport._BaseListFeeds._get_transcoded_request(http_options, request)

            # Jsonify the query params
            query_params = _BaseAssetServiceRestTransport._BaseListFeeds._get_query_params_json(transcoded_request)

            # Send the request
            response = await AsyncAssetServiceRestTransport._ListFeeds._get_response(self._host, metadata, query_params, self._session, timeout, transcoded_request)

            # In case of error, raise the appropriate core_exceptions.GoogleAPICallError exception
            # subclass.
            if response.status_code >= 400:
                raise core_exceptions.from_http_response(response)

            # Return the response
            return response

    class _ListSavedQueries(_BaseAssetServiceRestTransport._BaseListSavedQueries, AsyncAssetServiceRestStub):

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
            response = await getattr(session, method)(
                "{host}{uri}".format(host=host, uri=uri),
                timeout=timeout,
                headers=headers,
                params=rest_helpers.flatten_query_params(query_params, strict=True),
                )
            return response

        async def __call__(self,
                request: asset_service.ListSavedQueriesRequest, *,
                retry: OptionalRetry=gapic_v1.method.DEFAULT,
                timeout: Optional[float]=None,
                metadata: Sequence[Tuple[str, str]]=(),
                ) -> asset_service.ListSavedQueriesResponse:
            r"""Call the list saved queries method over HTTP.

            Args:
                request (~.asset_service.ListSavedQueriesRequest):
                    The request object. Request to list saved queries.
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, str]]): Strings which should be
                    sent along with the request as metadata.

            Returns:
                ~.asset_service.ListSavedQueriesResponse:
                    Response of listing saved queries.
            """

            http_options = _BaseAssetServiceRestTransport._BaseListSavedQueries._get_http_options()
            transcoded_request = _BaseAssetServiceRestTransport._BaseListSavedQueries._get_transcoded_request(http_options, request)

            # Jsonify the query params
            query_params = _BaseAssetServiceRestTransport._BaseListSavedQueries._get_query_params_json(transcoded_request)

            # Send the request
            response = await AsyncAssetServiceRestTransport._ListSavedQueries._get_response(self._host, metadata, query_params, self._session, timeout, transcoded_request)

            # In case of error, raise the appropriate core_exceptions.GoogleAPICallError exception
            # subclass.
            if response.status_code >= 400:
                raise core_exceptions.from_http_response(response)

            # Return the response
            return response

    class _QueryAssets(_BaseAssetServiceRestTransport._BaseQueryAssets, AsyncAssetServiceRestStub):

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
            response = await getattr(session, method)(
                "{host}{uri}".format(host=host, uri=uri),
                timeout=timeout,
                headers=headers,
                params=rest_helpers.flatten_query_params(query_params, strict=True),
                data=body,
                )
            return response

        async def __call__(self,
                request: asset_service.QueryAssetsRequest, *,
                retry: OptionalRetry=gapic_v1.method.DEFAULT,
                timeout: Optional[float]=None,
                metadata: Sequence[Tuple[str, str]]=(),
                ) -> asset_service.QueryAssetsResponse:
            r"""Call the query assets method over HTTP.

            Args:
                request (~.asset_service.QueryAssetsRequest):
                    The request object. QueryAssets request.
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, str]]): Strings which should be
                    sent along with the request as metadata.

            Returns:
                ~.asset_service.QueryAssetsResponse:
                    QueryAssets response.
            """

            http_options = _BaseAssetServiceRestTransport._BaseQueryAssets._get_http_options()
            transcoded_request = _BaseAssetServiceRestTransport._BaseQueryAssets._get_transcoded_request(http_options, request)

            body = _BaseAssetServiceRestTransport._BaseQueryAssets._get_request_body_json(transcoded_request)

            # Jsonify the query params
            query_params = _BaseAssetServiceRestTransport._BaseQueryAssets._get_query_params_json(transcoded_request)

            # Send the request
            response = await AsyncAssetServiceRestTransport._QueryAssets._get_response(self._host, metadata, query_params, self._session, timeout, transcoded_request, body)

            # In case of error, raise the appropriate core_exceptions.GoogleAPICallError exception
            # subclass.
            if response.status_code >= 400:
                raise core_exceptions.from_http_response(response)

            # Return the response
            return response

    class _SearchAllIamPolicies(_BaseAssetServiceRestTransport._BaseSearchAllIamPolicies, AsyncAssetServiceRestStub):

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
            response = await getattr(session, method)(
                "{host}{uri}".format(host=host, uri=uri),
                timeout=timeout,
                headers=headers,
                params=rest_helpers.flatten_query_params(query_params, strict=True),
                )
            return response

        async def __call__(self,
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

            http_options = _BaseAssetServiceRestTransport._BaseSearchAllIamPolicies._get_http_options()
            transcoded_request = _BaseAssetServiceRestTransport._BaseSearchAllIamPolicies._get_transcoded_request(http_options, request)

            # Jsonify the query params
            query_params = _BaseAssetServiceRestTransport._BaseSearchAllIamPolicies._get_query_params_json(transcoded_request)

            # Send the request
            response = await AsyncAssetServiceRestTransport._SearchAllIamPolicies._get_response(self._host, metadata, query_params, self._session, timeout, transcoded_request)

            # In case of error, raise the appropriate core_exceptions.GoogleAPICallError exception
            # subclass.
            if response.status_code >= 400:
                raise core_exceptions.from_http_response(response)

            # Return the response
            return response

    class _SearchAllResources(_BaseAssetServiceRestTransport._BaseSearchAllResources, AsyncAssetServiceRestStub):

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
            response = await getattr(session, method)(
                "{host}{uri}".format(host=host, uri=uri),
                timeout=timeout,
                headers=headers,
                params=rest_helpers.flatten_query_params(query_params, strict=True),
                )
            return response

        async def __call__(self,
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

            http_options = _BaseAssetServiceRestTransport._BaseSearchAllResources._get_http_options()
            transcoded_request = _BaseAssetServiceRestTransport._BaseSearchAllResources._get_transcoded_request(http_options, request)

            # Jsonify the query params
            query_params = _BaseAssetServiceRestTransport._BaseSearchAllResources._get_query_params_json(transcoded_request)

            # Send the request
            response = await AsyncAssetServiceRestTransport._SearchAllResources._get_response(self._host, metadata, query_params, self._session, timeout, transcoded_request)

            # In case of error, raise the appropriate core_exceptions.GoogleAPICallError exception
            # subclass.
            if response.status_code >= 400:
                raise core_exceptions.from_http_response(response)

            # Return the response
            return response

    class _UpdateFeed(_BaseAssetServiceRestTransport._BaseUpdateFeed, AsyncAssetServiceRestStub):

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
            response = await getattr(session, method)(
                "{host}{uri}".format(host=host, uri=uri),
                timeout=timeout,
                headers=headers,
                params=rest_helpers.flatten_query_params(query_params, strict=True),
                data=body,
                )
            return response

        async def __call__(self,
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

            http_options = _BaseAssetServiceRestTransport._BaseUpdateFeed._get_http_options()
            transcoded_request = _BaseAssetServiceRestTransport._BaseUpdateFeed._get_transcoded_request(http_options, request)

            body = _BaseAssetServiceRestTransport._BaseUpdateFeed._get_request_body_json(transcoded_request)

            # Jsonify the query params
            query_params = _BaseAssetServiceRestTransport._BaseUpdateFeed._get_query_params_json(transcoded_request)

            # Send the request
            response = await AsyncAssetServiceRestTransport._UpdateFeed._get_response(self._host, metadata, query_params, self._session, timeout, transcoded_request, body)

            # In case of error, raise the appropriate core_exceptions.GoogleAPICallError exception
            # subclass.
            if response.status_code >= 400:
                raise core_exceptions.from_http_response(response)

            # Return the response
            return response

    class _UpdateSavedQuery(_BaseAssetServiceRestTransport._BaseUpdateSavedQuery, AsyncAssetServiceRestStub):

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
            response = await getattr(session, method)(
                "{host}{uri}".format(host=host, uri=uri),
                timeout=timeout,
                headers=headers,
                params=rest_helpers.flatten_query_params(query_params, strict=True),
                data=body,
                )
            return response

        async def __call__(self,
                request: asset_service.UpdateSavedQueryRequest, *,
                retry: OptionalRetry=gapic_v1.method.DEFAULT,
                timeout: Optional[float]=None,
                metadata: Sequence[Tuple[str, str]]=(),
                ) -> asset_service.SavedQuery:
            r"""Call the update saved query method over HTTP.

            Args:
                request (~.asset_service.UpdateSavedQueryRequest):
                    The request object. Request to update a saved query.
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, str]]): Strings which should be
                    sent along with the request as metadata.

            Returns:
                ~.asset_service.SavedQuery:
                    A saved query which can be shared
                with others or used later.

            """

            http_options = _BaseAssetServiceRestTransport._BaseUpdateSavedQuery._get_http_options()
            transcoded_request = _BaseAssetServiceRestTransport._BaseUpdateSavedQuery._get_transcoded_request(http_options, request)

            body = _BaseAssetServiceRestTransport._BaseUpdateSavedQuery._get_request_body_json(transcoded_request)

            # Jsonify the query params
            query_params = _BaseAssetServiceRestTransport._BaseUpdateSavedQuery._get_query_params_json(transcoded_request)

            # Send the request
            response = await AsyncAssetServiceRestTransport._UpdateSavedQuery._get_response(self._host, metadata, query_params, self._session, timeout, transcoded_request, body)

            # In case of error, raise the appropriate core_exceptions.GoogleAPICallError exception
            # subclass.
            if response.status_code >= 400:
                raise core_exceptions.from_http_response(response)

            # Return the response
            return response

    @property
    def kind(self) -> str:
        return "rest"

    async def close(self):
        if self._session:
            await self._session.close()

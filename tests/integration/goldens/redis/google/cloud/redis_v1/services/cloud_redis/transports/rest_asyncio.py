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
try:
    from google.auth.aio.transport.sessions import AsyncAuthorizedSession # type: ignore
except ImportError as e:  # pragma: NO COVER
    raise ImportError("async rest transport requires google.auth >= 2.x.x") from e

from google.auth.aio import credentials as ga_credentials_async  # type: ignore

try:
    from google.api_core.exceptions import format_http_response_error  # type: ignore
except ImportError as e:  # pragma: NO COVER
    raise ImportError("async rest transport requires google-api-core >= 2.x.x") from e

from google.api_core import exceptions as core_exceptions
from google.api_core import gapic_v1
from google.api_core import retry_async as retries
from google.api_core import rest_helpers

from google.protobuf import json_format

import inspect
import json  # type: ignore
import dataclasses
from typing import Any, Callable, Dict, List, Optional, Sequence, Tuple, Union


from google.cloud.redis_v1.types import cloud_redis
from google.longrunning import operations_pb2  # type: ignore


from .rest_base import _BaseCloudRedisRestTransport
from .base import DEFAULT_CLIENT_INFO as BASE_DEFAULT_CLIENT_INFO

try:
    OptionalRetry = Union[retries.AsyncRetry, gapic_v1.method._MethodDefault, None]
except AttributeError:  # pragma: NO COVER
    OptionalRetry = Union[retries.AsyncRetry, object, None]  # type: ignore

DEFAULT_CLIENT_INFO = gapic_v1.client_info.ClientInfo(
    gapic_version=BASE_DEFAULT_CLIENT_INFO.gapic_version,
    grpc_version=None,
    rest_version=None,
)

@dataclasses.dataclass
class AsyncCloudRedisRestStub:
    _session: AsyncAuthorizedSession
    _host: str

class AsyncCloudRedisRestTransport(_BaseCloudRedisRestTransport):
    """Asynchronous REST backend transport for CloudRedis.

    Configures and manages Cloud Memorystore for Redis instances

    Google Cloud Memorystore for Redis v1

    The ``redis.googleapis.com`` service implements the Google Cloud
    Memorystore for Redis API and defines the following resource model
    for managing Redis instances:

    -  The service works with a collection of cloud projects, named:
       ``/projects/*``
    -  Each project has a collection of available locations, named:
       ``/locations/*``
    -  Each location has a collection of Redis instances, named:
       ``/instances/*``
    -  As such, Redis instances are resources of the form:
       ``/projects/{project_id}/locations/{location_id}/instances/{instance_id}``

    Note that location_id must be referring to a GCP ``region``; for
    example:

    -  ``projects/redpepper-1290/locations/us-central1/instances/my-redis``

    This class defines the same methods as the primary client, so the
    primary client can load the underlying transport implementation
    and call it.

    It sends JSON representations of protocol buffers over HTTP/1.1
    """
    def __init__(self, *,
            host: str = 'redis.googleapis.com',
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
                 The hostname to connect to (default: 'redis.googleapis.com').
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
        self._session = AsyncAuthorizedSession(self._credentials)
        self._wrap_with_kind = "kind" in inspect.signature(gapic_v1.method_async.wrap_method).parameters
        self._prep_wrapped_messages(client_info)

    def _prep_wrapped_messages(self, client_info):
        """ Precompute the wrapped methods, overriding the base class method to use async wrappers."""
        self._wrapped_methods = {
            self.list_instances: self._wrap_method(
                self.list_instances,
                default_timeout=600.0,
                client_info=client_info,
            ),
            self.get_instance: self._wrap_method(
                self.get_instance,
                default_timeout=600.0,
                client_info=client_info,
            ),
            self.get_instance_auth_string: self._wrap_method(
                self.get_instance_auth_string,
                default_timeout=600.0,
                client_info=client_info,
            ),
            self.create_instance: self._wrap_method(
                self.create_instance,
                default_timeout=600.0,
                client_info=client_info,
            ),
            self.update_instance: self._wrap_method(
                self.update_instance,
                default_timeout=600.0,
                client_info=client_info,
            ),
            self.upgrade_instance: self._wrap_method(
                self.upgrade_instance,
                default_timeout=600.0,
                client_info=client_info,
            ),
            self.import_instance: self._wrap_method(
                self.import_instance,
                default_timeout=600.0,
                client_info=client_info,
            ),
            self.export_instance: self._wrap_method(
                self.export_instance,
                default_timeout=600.0,
                client_info=client_info,
            ),
            self.failover_instance: self._wrap_method(
                self.failover_instance,
                default_timeout=600.0,
                client_info=client_info,
            ),
            self.delete_instance: self._wrap_method(
                self.delete_instance,
                default_timeout=600.0,
                client_info=client_info,
            ),
            self.reschedule_maintenance: self._wrap_method(
                self.reschedule_maintenance,
                default_timeout=None,
                client_info=client_info,
            ),
        }

    def _wrap_method(self, func, *args, **kwargs):
        if self._wrap_with_kind:  # pragma: NO COVER
            kwargs["kind"] = self.kind
        return gapic_v1.method_async.wrap_method(func, *args, **kwargs)

    class _CreateInstance(_BaseCloudRedisRestTransport._BaseCreateInstance, AsyncCloudRedisRestStub):
        def __hash__(self):
            return hash("AsyncCloudRedisRestTransport.CreateInstance")

        async def __call__(self,
                request: cloud_redis.CreateInstanceRequest, *,
                retry: OptionalRetry=gapic_v1.method.DEFAULT,
                timeout: Optional[float]=None,
                metadata: Sequence[Tuple[str, str]]=(),
                ) -> operations_pb2.Operation:
            raise NotImplementedError(
                "Method CreateInstance is not available over REST transport"
            )

    class _DeleteInstance(_BaseCloudRedisRestTransport._BaseDeleteInstance, AsyncCloudRedisRestStub):
        def __hash__(self):
            return hash("AsyncCloudRedisRestTransport.DeleteInstance")

        async def __call__(self,
                request: cloud_redis.DeleteInstanceRequest, *,
                retry: OptionalRetry=gapic_v1.method.DEFAULT,
                timeout: Optional[float]=None,
                metadata: Sequence[Tuple[str, str]]=(),
                ) -> operations_pb2.Operation:
            raise NotImplementedError(
                "Method DeleteInstance is not available over REST transport"
            )

    class _ExportInstance(_BaseCloudRedisRestTransport._BaseExportInstance, AsyncCloudRedisRestStub):
        def __hash__(self):
            return hash("AsyncCloudRedisRestTransport.ExportInstance")

        async def __call__(self,
                request: cloud_redis.ExportInstanceRequest, *,
                retry: OptionalRetry=gapic_v1.method.DEFAULT,
                timeout: Optional[float]=None,
                metadata: Sequence[Tuple[str, str]]=(),
                ) -> operations_pb2.Operation:
            raise NotImplementedError(
                "Method ExportInstance is not available over REST transport"
            )

    class _FailoverInstance(_BaseCloudRedisRestTransport._BaseFailoverInstance, AsyncCloudRedisRestStub):
        def __hash__(self):
            return hash("AsyncCloudRedisRestTransport.FailoverInstance")

        async def __call__(self,
                request: cloud_redis.FailoverInstanceRequest, *,
                retry: OptionalRetry=gapic_v1.method.DEFAULT,
                timeout: Optional[float]=None,
                metadata: Sequence[Tuple[str, str]]=(),
                ) -> operations_pb2.Operation:
            raise NotImplementedError(
                "Method FailoverInstance is not available over REST transport"
            )

    class _GetInstance(_BaseCloudRedisRestTransport._BaseGetInstance, AsyncCloudRedisRestStub):
        def __hash__(self):
            return hash("AsyncCloudRedisRestTransport.GetInstance")

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
                request: cloud_redis.GetInstanceRequest, *,
                retry: OptionalRetry=gapic_v1.method.DEFAULT,
                timeout: Optional[float]=None,
                metadata: Sequence[Tuple[str, str]]=(),
                ) -> cloud_redis.Instance:
            r"""Call the get instance method over HTTP.

            Args:
                request (~.cloud_redis.GetInstanceRequest):
                    The request object. Request for
                [GetInstance][google.cloud.redis.v1.CloudRedis.GetInstance].
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, str]]): Strings which should be
                    sent along with the request as metadata.

            Returns:
                ~.cloud_redis.Instance:
                    A Memorystore for Redis instance.
            """

            http_options = _BaseCloudRedisRestTransport._BaseGetInstance._get_http_options()
            transcoded_request = _BaseCloudRedisRestTransport._BaseGetInstance._get_transcoded_request(http_options, request)

            # Jsonify the query params
            query_params = _BaseCloudRedisRestTransport._BaseGetInstance._get_query_params_json(transcoded_request)

            # Send the request
            response = await AsyncCloudRedisRestTransport._GetInstance._get_response(self._host, metadata, query_params, self._session, timeout, transcoded_request)

            # In case of error, raise the appropriate core_exceptions.GoogleAPICallError exception
            # subclass.
            if response.status_code >= 400:
                content = await response.read()
                payload = json.loads(content.decode('utf-8'))
                request_url = "{host}{uri}".format(host=self._host, uri=transcoded_request['uri'])
                method = transcoded_request['method']
                raise format_http_response_error(response, method, request_url, payload)

            # Return the response
            resp = cloud_redis.Instance()
            pb_resp = cloud_redis.Instance.pb(resp)
            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)
            return resp

    class _GetInstanceAuthString(_BaseCloudRedisRestTransport._BaseGetInstanceAuthString, AsyncCloudRedisRestStub):
        def __hash__(self):
            return hash("AsyncCloudRedisRestTransport.GetInstanceAuthString")

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
                request: cloud_redis.GetInstanceAuthStringRequest, *,
                retry: OptionalRetry=gapic_v1.method.DEFAULT,
                timeout: Optional[float]=None,
                metadata: Sequence[Tuple[str, str]]=(),
                ) -> cloud_redis.InstanceAuthString:
            r"""Call the get instance auth string method over HTTP.

            Args:
                request (~.cloud_redis.GetInstanceAuthStringRequest):
                    The request object. Request for
                [GetInstanceAuthString][google.cloud.redis.v1.CloudRedis.GetInstanceAuthString].
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, str]]): Strings which should be
                    sent along with the request as metadata.

            Returns:
                ~.cloud_redis.InstanceAuthString:
                    Instance AUTH string details.
            """

            http_options = _BaseCloudRedisRestTransport._BaseGetInstanceAuthString._get_http_options()
            transcoded_request = _BaseCloudRedisRestTransport._BaseGetInstanceAuthString._get_transcoded_request(http_options, request)

            # Jsonify the query params
            query_params = _BaseCloudRedisRestTransport._BaseGetInstanceAuthString._get_query_params_json(transcoded_request)

            # Send the request
            response = await AsyncCloudRedisRestTransport._GetInstanceAuthString._get_response(self._host, metadata, query_params, self._session, timeout, transcoded_request)

            # In case of error, raise the appropriate core_exceptions.GoogleAPICallError exception
            # subclass.
            if response.status_code >= 400:
                content = await response.read()
                payload = json.loads(content.decode('utf-8'))
                request_url = "{host}{uri}".format(host=self._host, uri=transcoded_request['uri'])
                method = transcoded_request['method']
                raise format_http_response_error(response, method, request_url, payload)

            # Return the response
            resp = cloud_redis.InstanceAuthString()
            pb_resp = cloud_redis.InstanceAuthString.pb(resp)
            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)
            return resp

    class _ImportInstance(_BaseCloudRedisRestTransport._BaseImportInstance, AsyncCloudRedisRestStub):
        def __hash__(self):
            return hash("AsyncCloudRedisRestTransport.ImportInstance")

        async def __call__(self,
                request: cloud_redis.ImportInstanceRequest, *,
                retry: OptionalRetry=gapic_v1.method.DEFAULT,
                timeout: Optional[float]=None,
                metadata: Sequence[Tuple[str, str]]=(),
                ) -> operations_pb2.Operation:
            raise NotImplementedError(
                "Method ImportInstance is not available over REST transport"
            )

    class _ListInstances(_BaseCloudRedisRestTransport._BaseListInstances, AsyncCloudRedisRestStub):
        def __hash__(self):
            return hash("AsyncCloudRedisRestTransport.ListInstances")

        async def __call__(self,
                request: cloud_redis.ListInstancesRequest, *,
                retry: OptionalRetry=gapic_v1.method.DEFAULT,
                timeout: Optional[float]=None,
                metadata: Sequence[Tuple[str, str]]=(),
                ) -> cloud_redis.ListInstancesResponse:
            raise NotImplementedError(
                "Method ListInstances is not available over REST transport"
            )

    class _RescheduleMaintenance(_BaseCloudRedisRestTransport._BaseRescheduleMaintenance, AsyncCloudRedisRestStub):
        def __hash__(self):
            return hash("AsyncCloudRedisRestTransport.RescheduleMaintenance")

        async def __call__(self,
                request: cloud_redis.RescheduleMaintenanceRequest, *,
                retry: OptionalRetry=gapic_v1.method.DEFAULT,
                timeout: Optional[float]=None,
                metadata: Sequence[Tuple[str, str]]=(),
                ) -> operations_pb2.Operation:
            raise NotImplementedError(
                "Method RescheduleMaintenance is not available over REST transport"
            )

    class _UpdateInstance(_BaseCloudRedisRestTransport._BaseUpdateInstance, AsyncCloudRedisRestStub):
        def __hash__(self):
            return hash("AsyncCloudRedisRestTransport.UpdateInstance")

        async def __call__(self,
                request: cloud_redis.UpdateInstanceRequest, *,
                retry: OptionalRetry=gapic_v1.method.DEFAULT,
                timeout: Optional[float]=None,
                metadata: Sequence[Tuple[str, str]]=(),
                ) -> operations_pb2.Operation:
            raise NotImplementedError(
                "Method UpdateInstance is not available over REST transport"
            )

    class _UpgradeInstance(_BaseCloudRedisRestTransport._BaseUpgradeInstance, AsyncCloudRedisRestStub):
        def __hash__(self):
            return hash("AsyncCloudRedisRestTransport.UpgradeInstance")

        async def __call__(self,
                request: cloud_redis.UpgradeInstanceRequest, *,
                retry: OptionalRetry=gapic_v1.method.DEFAULT,
                timeout: Optional[float]=None,
                metadata: Sequence[Tuple[str, str]]=(),
                ) -> operations_pb2.Operation:
            raise NotImplementedError(
                "Method UpgradeInstance is not available over REST transport"
            )

    @property
    def create_instance(self) -> Callable[
            [cloud_redis.CreateInstanceRequest],
            operations_pb2.Operation]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._CreateInstance(self._session, self._host) # type: ignore

    @property
    def delete_instance(self) -> Callable[
            [cloud_redis.DeleteInstanceRequest],
            operations_pb2.Operation]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._DeleteInstance(self._session, self._host) # type: ignore

    @property
    def export_instance(self) -> Callable[
            [cloud_redis.ExportInstanceRequest],
            operations_pb2.Operation]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._ExportInstance(self._session, self._host) # type: ignore

    @property
    def failover_instance(self) -> Callable[
            [cloud_redis.FailoverInstanceRequest],
            operations_pb2.Operation]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._FailoverInstance(self._session, self._host) # type: ignore

    @property
    def get_instance(self) -> Callable[
            [cloud_redis.GetInstanceRequest],
            cloud_redis.Instance]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._GetInstance(self._session, self._host) # type: ignore

    @property
    def get_instance_auth_string(self) -> Callable[
            [cloud_redis.GetInstanceAuthStringRequest],
            cloud_redis.InstanceAuthString]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._GetInstanceAuthString(self._session, self._host) # type: ignore

    @property
    def import_instance(self) -> Callable[
            [cloud_redis.ImportInstanceRequest],
            operations_pb2.Operation]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._ImportInstance(self._session, self._host) # type: ignore

    @property
    def list_instances(self) -> Callable[
            [cloud_redis.ListInstancesRequest],
            cloud_redis.ListInstancesResponse]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._ListInstances(self._session, self._host) # type: ignore

    @property
    def reschedule_maintenance(self) -> Callable[
            [cloud_redis.RescheduleMaintenanceRequest],
            operations_pb2.Operation]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._RescheduleMaintenance(self._session, self._host) # type: ignore

    @property
    def update_instance(self) -> Callable[
            [cloud_redis.UpdateInstanceRequest],
            operations_pb2.Operation]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._UpdateInstance(self._session, self._host) # type: ignore

    @property
    def upgrade_instance(self) -> Callable[
            [cloud_redis.UpgradeInstanceRequest],
            operations_pb2.Operation]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._UpgradeInstance(self._session, self._host) # type: ignore

    @property
    def kind(self) -> str:
        return "rest_asyncio"

    async def close(self):
        await self._session.close()

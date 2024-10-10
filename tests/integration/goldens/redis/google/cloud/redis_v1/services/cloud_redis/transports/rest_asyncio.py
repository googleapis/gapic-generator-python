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
    from google.api_core import rest_streaming_async # type: ignore
    from google.api_core.operations_v1 import AsyncOperationsRestClient # type: ignore
except ImportError as e:  # pragma: NO COVER
    raise ImportError("`rest_asyncio` transport requires the library to be installed with the `async_rest` extra. Install the library with the `async_rest` extra using `pip install google-cloud-redis[async_rest]`") from e

from google.auth.aio import credentials as ga_credentials_async  # type: ignore

from google.api_core import exceptions as core_exceptions
from google.api_core import gapic_v1
from google.api_core import operations_v1
from google.cloud.location import locations_pb2 # type: ignore
from google.api_core import retry_async as retries
from google.api_core import rest_helpers
from google.api_core import rest_streaming_async  # type: ignore


from google.protobuf import json_format
from google.api_core import operations_v1
from google.cloud.location import locations_pb2 # type: ignore

import json  # type: ignore
import dataclasses
from typing import Any, Dict, List, Callable, Tuple, Optional, Sequence, Union


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
    rest_version=google.auth.__version__
)


class AsyncCloudRedisRestInterceptor:
    """Asynchronous Interceptor for CloudRedis.

    Interceptors are used to manipulate requests, request metadata, and responses
    in arbitrary ways.
    Example use cases include:
    * Logging
    * Verifying requests according to service or custom semantics
    * Stripping extraneous information from responses

    These use cases and more can be enabled by injecting an
    instance of a custom subclass when constructing the AsyncCloudRedisRestTransport.

    .. code-block:: python
        class MyCustomCloudRedisInterceptor(CloudRedisRestInterceptor):
            async def pre_create_instance(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            async def post_create_instance(self, response):
                logging.log(f"Received response: {response}")
                return response

            async def pre_delete_instance(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            async def post_delete_instance(self, response):
                logging.log(f"Received response: {response}")
                return response

            async def pre_export_instance(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            async def post_export_instance(self, response):
                logging.log(f"Received response: {response}")
                return response

            async def pre_failover_instance(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            async def post_failover_instance(self, response):
                logging.log(f"Received response: {response}")
                return response

            async def pre_get_instance(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            async def post_get_instance(self, response):
                logging.log(f"Received response: {response}")
                return response

            async def pre_get_instance_auth_string(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            async def post_get_instance_auth_string(self, response):
                logging.log(f"Received response: {response}")
                return response

            async def pre_import_instance(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            async def post_import_instance(self, response):
                logging.log(f"Received response: {response}")
                return response

            async def pre_list_instances(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            async def post_list_instances(self, response):
                logging.log(f"Received response: {response}")
                return response

            async def pre_reschedule_maintenance(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            async def post_reschedule_maintenance(self, response):
                logging.log(f"Received response: {response}")
                return response

            async def pre_update_instance(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            async def post_update_instance(self, response):
                logging.log(f"Received response: {response}")
                return response

            async def pre_upgrade_instance(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            async def post_upgrade_instance(self, response):
                logging.log(f"Received response: {response}")
                return response

        transport = AsyncCloudRedisRestTransport(interceptor=MyCustomCloudRedisInterceptor())
        client = async CloudRedisClient(transport=transport)


    """
    async def pre_create_instance(self, request: cloud_redis.CreateInstanceRequest, metadata: Sequence[Tuple[str, str]]) -> Tuple[cloud_redis.CreateInstanceRequest, Sequence[Tuple[str, str]]]:
        """Pre-rpc interceptor for create_instance

        Override in a subclass to manipulate the request or metadata
        before they are sent to the CloudRedis server.
        """
        return request, metadata

    async def post_create_instance(self, response: operations_pb2.Operation) -> operations_pb2.Operation:
        """Post-rpc interceptor for create_instance

        Override in a subclass to manipulate the response
        after it is returned by the CloudRedis server but before
        it is returned to user code.
        """
        return response

    async def pre_delete_instance(self, request: cloud_redis.DeleteInstanceRequest, metadata: Sequence[Tuple[str, str]]) -> Tuple[cloud_redis.DeleteInstanceRequest, Sequence[Tuple[str, str]]]:
        """Pre-rpc interceptor for delete_instance

        Override in a subclass to manipulate the request or metadata
        before they are sent to the CloudRedis server.
        """
        return request, metadata

    async def post_delete_instance(self, response: operations_pb2.Operation) -> operations_pb2.Operation:
        """Post-rpc interceptor for delete_instance

        Override in a subclass to manipulate the response
        after it is returned by the CloudRedis server but before
        it is returned to user code.
        """
        return response

    async def pre_export_instance(self, request: cloud_redis.ExportInstanceRequest, metadata: Sequence[Tuple[str, str]]) -> Tuple[cloud_redis.ExportInstanceRequest, Sequence[Tuple[str, str]]]:
        """Pre-rpc interceptor for export_instance

        Override in a subclass to manipulate the request or metadata
        before they are sent to the CloudRedis server.
        """
        return request, metadata

    async def post_export_instance(self, response: operations_pb2.Operation) -> operations_pb2.Operation:
        """Post-rpc interceptor for export_instance

        Override in a subclass to manipulate the response
        after it is returned by the CloudRedis server but before
        it is returned to user code.
        """
        return response

    async def pre_failover_instance(self, request: cloud_redis.FailoverInstanceRequest, metadata: Sequence[Tuple[str, str]]) -> Tuple[cloud_redis.FailoverInstanceRequest, Sequence[Tuple[str, str]]]:
        """Pre-rpc interceptor for failover_instance

        Override in a subclass to manipulate the request or metadata
        before they are sent to the CloudRedis server.
        """
        return request, metadata

    async def post_failover_instance(self, response: operations_pb2.Operation) -> operations_pb2.Operation:
        """Post-rpc interceptor for failover_instance

        Override in a subclass to manipulate the response
        after it is returned by the CloudRedis server but before
        it is returned to user code.
        """
        return response

    async def pre_get_instance(self, request: cloud_redis.GetInstanceRequest, metadata: Sequence[Tuple[str, str]]) -> Tuple[cloud_redis.GetInstanceRequest, Sequence[Tuple[str, str]]]:
        """Pre-rpc interceptor for get_instance

        Override in a subclass to manipulate the request or metadata
        before they are sent to the CloudRedis server.
        """
        return request, metadata

    async def post_get_instance(self, response: cloud_redis.Instance) -> cloud_redis.Instance:
        """Post-rpc interceptor for get_instance

        Override in a subclass to manipulate the response
        after it is returned by the CloudRedis server but before
        it is returned to user code.
        """
        return response

    async def pre_get_instance_auth_string(self, request: cloud_redis.GetInstanceAuthStringRequest, metadata: Sequence[Tuple[str, str]]) -> Tuple[cloud_redis.GetInstanceAuthStringRequest, Sequence[Tuple[str, str]]]:
        """Pre-rpc interceptor for get_instance_auth_string

        Override in a subclass to manipulate the request or metadata
        before they are sent to the CloudRedis server.
        """
        return request, metadata

    async def post_get_instance_auth_string(self, response: cloud_redis.InstanceAuthString) -> cloud_redis.InstanceAuthString:
        """Post-rpc interceptor for get_instance_auth_string

        Override in a subclass to manipulate the response
        after it is returned by the CloudRedis server but before
        it is returned to user code.
        """
        return response

    async def pre_import_instance(self, request: cloud_redis.ImportInstanceRequest, metadata: Sequence[Tuple[str, str]]) -> Tuple[cloud_redis.ImportInstanceRequest, Sequence[Tuple[str, str]]]:
        """Pre-rpc interceptor for import_instance

        Override in a subclass to manipulate the request or metadata
        before they are sent to the CloudRedis server.
        """
        return request, metadata

    async def post_import_instance(self, response: operations_pb2.Operation) -> operations_pb2.Operation:
        """Post-rpc interceptor for import_instance

        Override in a subclass to manipulate the response
        after it is returned by the CloudRedis server but before
        it is returned to user code.
        """
        return response

    async def pre_list_instances(self, request: cloud_redis.ListInstancesRequest, metadata: Sequence[Tuple[str, str]]) -> Tuple[cloud_redis.ListInstancesRequest, Sequence[Tuple[str, str]]]:
        """Pre-rpc interceptor for list_instances

        Override in a subclass to manipulate the request or metadata
        before they are sent to the CloudRedis server.
        """
        return request, metadata

    async def post_list_instances(self, response: cloud_redis.ListInstancesResponse) -> cloud_redis.ListInstancesResponse:
        """Post-rpc interceptor for list_instances

        Override in a subclass to manipulate the response
        after it is returned by the CloudRedis server but before
        it is returned to user code.
        """
        return response

    async def pre_reschedule_maintenance(self, request: cloud_redis.RescheduleMaintenanceRequest, metadata: Sequence[Tuple[str, str]]) -> Tuple[cloud_redis.RescheduleMaintenanceRequest, Sequence[Tuple[str, str]]]:
        """Pre-rpc interceptor for reschedule_maintenance

        Override in a subclass to manipulate the request or metadata
        before they are sent to the CloudRedis server.
        """
        return request, metadata

    async def post_reschedule_maintenance(self, response: operations_pb2.Operation) -> operations_pb2.Operation:
        """Post-rpc interceptor for reschedule_maintenance

        Override in a subclass to manipulate the response
        after it is returned by the CloudRedis server but before
        it is returned to user code.
        """
        return response

    async def pre_update_instance(self, request: cloud_redis.UpdateInstanceRequest, metadata: Sequence[Tuple[str, str]]) -> Tuple[cloud_redis.UpdateInstanceRequest, Sequence[Tuple[str, str]]]:
        """Pre-rpc interceptor for update_instance

        Override in a subclass to manipulate the request or metadata
        before they are sent to the CloudRedis server.
        """
        return request, metadata

    async def post_update_instance(self, response: operations_pb2.Operation) -> operations_pb2.Operation:
        """Post-rpc interceptor for update_instance

        Override in a subclass to manipulate the response
        after it is returned by the CloudRedis server but before
        it is returned to user code.
        """
        return response

    async def pre_upgrade_instance(self, request: cloud_redis.UpgradeInstanceRequest, metadata: Sequence[Tuple[str, str]]) -> Tuple[cloud_redis.UpgradeInstanceRequest, Sequence[Tuple[str, str]]]:
        """Pre-rpc interceptor for upgrade_instance

        Override in a subclass to manipulate the request or metadata
        before they are sent to the CloudRedis server.
        """
        return request, metadata

    async def post_upgrade_instance(self, response: operations_pb2.Operation) -> operations_pb2.Operation:
        """Post-rpc interceptor for upgrade_instance

        Override in a subclass to manipulate the response
        after it is returned by the CloudRedis server but before
        it is returned to user code.
        """
        return response

    async def pre_get_location(
        self, request: locations_pb2.GetLocationRequest, metadata: Sequence[Tuple[str, str]]
    ) -> Tuple[locations_pb2.GetLocationRequest, Sequence[Tuple[str, str]]]:
        """Pre-rpc interceptor for get_location

        Override in a subclass to manipulate the request or metadata
        before they are sent to the CloudRedis server.
        """
        return request, metadata

    async def post_get_location(
        self, response: locations_pb2.Location
    ) -> locations_pb2.Location:
        """Post-rpc interceptor for get_location

        Override in a subclass to manipulate the response
        after it is returned by the CloudRedis server but before
        it is returned to user code.
        """
        return response

    async def pre_list_locations(
        self, request: locations_pb2.ListLocationsRequest, metadata: Sequence[Tuple[str, str]]
    ) -> Tuple[locations_pb2.ListLocationsRequest, Sequence[Tuple[str, str]]]:
        """Pre-rpc interceptor for list_locations

        Override in a subclass to manipulate the request or metadata
        before they are sent to the CloudRedis server.
        """
        return request, metadata

    async def post_list_locations(
        self, response: locations_pb2.ListLocationsResponse
    ) -> locations_pb2.ListLocationsResponse:
        """Post-rpc interceptor for list_locations

        Override in a subclass to manipulate the response
        after it is returned by the CloudRedis server but before
        it is returned to user code.
        """
        return response

    async def pre_cancel_operation(
        self, request: operations_pb2.CancelOperationRequest, metadata: Sequence[Tuple[str, str]]
    ) -> Tuple[operations_pb2.CancelOperationRequest, Sequence[Tuple[str, str]]]:
        """Pre-rpc interceptor for cancel_operation

        Override in a subclass to manipulate the request or metadata
        before they are sent to the CloudRedis server.
        """
        return request, metadata

    async def post_cancel_operation(
        self, response: None
    ) -> None:
        """Post-rpc interceptor for cancel_operation

        Override in a subclass to manipulate the response
        after it is returned by the CloudRedis server but before
        it is returned to user code.
        """
        return response

    async def pre_delete_operation(
        self, request: operations_pb2.DeleteOperationRequest, metadata: Sequence[Tuple[str, str]]
    ) -> Tuple[operations_pb2.DeleteOperationRequest, Sequence[Tuple[str, str]]]:
        """Pre-rpc interceptor for delete_operation

        Override in a subclass to manipulate the request or metadata
        before they are sent to the CloudRedis server.
        """
        return request, metadata

    async def post_delete_operation(
        self, response: None
    ) -> None:
        """Post-rpc interceptor for delete_operation

        Override in a subclass to manipulate the response
        after it is returned by the CloudRedis server but before
        it is returned to user code.
        """
        return response

    async def pre_get_operation(
        self, request: operations_pb2.GetOperationRequest, metadata: Sequence[Tuple[str, str]]
    ) -> Tuple[operations_pb2.GetOperationRequest, Sequence[Tuple[str, str]]]:
        """Pre-rpc interceptor for get_operation

        Override in a subclass to manipulate the request or metadata
        before they are sent to the CloudRedis server.
        """
        return request, metadata

    async def post_get_operation(
        self, response: operations_pb2.Operation
    ) -> operations_pb2.Operation:
        """Post-rpc interceptor for get_operation

        Override in a subclass to manipulate the response
        after it is returned by the CloudRedis server but before
        it is returned to user code.
        """
        return response

    async def pre_list_operations(
        self, request: operations_pb2.ListOperationsRequest, metadata: Sequence[Tuple[str, str]]
    ) -> Tuple[operations_pb2.ListOperationsRequest, Sequence[Tuple[str, str]]]:
        """Pre-rpc interceptor for list_operations

        Override in a subclass to manipulate the request or metadata
        before they are sent to the CloudRedis server.
        """
        return request, metadata

    async def post_list_operations(
        self, response: operations_pb2.ListOperationsResponse
    ) -> operations_pb2.ListOperationsResponse:
        """Post-rpc interceptor for list_operations

        Override in a subclass to manipulate the response
        after it is returned by the CloudRedis server but before
        it is returned to user code.
        """
        return response

    async def pre_wait_operation(
        self, request: operations_pb2.WaitOperationRequest, metadata: Sequence[Tuple[str, str]]
    ) -> Tuple[operations_pb2.WaitOperationRequest, Sequence[Tuple[str, str]]]:
        """Pre-rpc interceptor for wait_operation

        Override in a subclass to manipulate the request or metadata
        before they are sent to the CloudRedis server.
        """
        return request, metadata

    async def post_wait_operation(
        self, response: operations_pb2.Operation
    ) -> operations_pb2.Operation:
        """Post-rpc interceptor for wait_operation

        Override in a subclass to manipulate the response
        after it is returned by the CloudRedis server but before
        it is returned to user code.
        """
        return response


@dataclasses.dataclass
class AsyncCloudRedisRestStub:
    _session: AsyncAuthorizedSession
    _host: str
    _interceptor: AsyncCloudRedisRestInterceptor

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
    def __init__(self,
            *,
            host: str = 'redis.googleapis.com',
            credentials: Optional[ga_credentials_async.Credentials] = None,
            client_info: gapic_v1.client_info.ClientInfo = DEFAULT_CLIENT_INFO,
            url_scheme: str = 'https',
            interceptor: Optional[AsyncCloudRedisRestInterceptor] = None,
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
        self._session = AsyncAuthorizedSession(self._credentials)  # type: ignore
        self._interceptor = interceptor or AsyncCloudRedisRestInterceptor()
        self._wrap_with_kind = True
        self._prep_wrapped_messages(client_info)
        self._operations_client: Optional[operations_v1.AsyncOperationsRestClient] = None

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
            self.get_location: self._wrap_method(
                self.get_location,
                default_timeout=None,
                client_info=client_info,
            ),
            self.list_locations: self._wrap_method(
                self.list_locations,
                default_timeout=None,
                client_info=client_info,
            ),
            self.cancel_operation: self._wrap_method(
                self.cancel_operation,
                default_timeout=None,
                client_info=client_info,
            ),
            self.delete_operation: self._wrap_method(
                self.delete_operation,
                default_timeout=None,
                client_info=client_info,
            ),
            self.get_operation: self._wrap_method(
                self.get_operation,
                default_timeout=None,
                client_info=client_info,
            ),
            self.list_operations: self._wrap_method(
                self.list_operations,
                default_timeout=None,
                client_info=client_info,
            ),
            self.wait_operation: self._wrap_method(
                self.wait_operation,
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
                    request: cloud_redis.CreateInstanceRequest, *,
                    retry: OptionalRetry=gapic_v1.method.DEFAULT,
                    timeout: Optional[float]=None,
                    metadata: Sequence[Tuple[str, str]]=(),
                    ) -> operations_pb2.Operation:
            r"""Call the create instance method over HTTP.

            Args:
                request (~.cloud_redis.CreateInstanceRequest):
                    The request object. Request for
                [CreateInstance][google.cloud.redis.v1.CloudRedis.CreateInstance].
                retry (google.api_core.retry_async.AsyncRetry): Designation of what errors, if any,
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

            http_options = _BaseCloudRedisRestTransport._BaseCreateInstance._get_http_options()
            request, metadata = await self._interceptor.pre_create_instance(request, metadata)
            transcoded_request = _BaseCloudRedisRestTransport._BaseCreateInstance._get_transcoded_request(http_options, request)

            body = _BaseCloudRedisRestTransport._BaseCreateInstance._get_request_body_json(transcoded_request)

            # Jsonify the query params
            query_params = _BaseCloudRedisRestTransport._BaseCreateInstance._get_query_params_json(transcoded_request)

            # Send the request
            response = await AsyncCloudRedisRestTransport._CreateInstance._get_response(self._host, metadata, query_params, self._session, timeout, transcoded_request, body)

            # In case of error, raise the appropriate core_exceptions.GoogleAPICallError exception
            # subclass.
            if response.status_code >= 400:
                content = await response.read()
                payload = json.loads(content.decode('utf-8'))
                request_url = "{host}{uri}".format(host=self._host, uri=transcoded_request['uri'])
                method = transcoded_request['method']
                raise core_exceptions.format_http_response_error(response, method, request_url, payload)  # type: ignore

            # Return the response
            resp = operations_pb2.Operation()
            pb_resp = resp
            content = await response.read()
            json_format.Parse(content, pb_resp, ignore_unknown_fields=True)
            resp = await self._interceptor.post_create_instance(resp)
            return resp

    class _DeleteInstance(_BaseCloudRedisRestTransport._BaseDeleteInstance, AsyncCloudRedisRestStub):
        def __hash__(self):
            return hash("AsyncCloudRedisRestTransport.DeleteInstance")

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
                    request: cloud_redis.DeleteInstanceRequest, *,
                    retry: OptionalRetry=gapic_v1.method.DEFAULT,
                    timeout: Optional[float]=None,
                    metadata: Sequence[Tuple[str, str]]=(),
                    ) -> operations_pb2.Operation:
            r"""Call the delete instance method over HTTP.

            Args:
                request (~.cloud_redis.DeleteInstanceRequest):
                    The request object. Request for
                [DeleteInstance][google.cloud.redis.v1.CloudRedis.DeleteInstance].
                retry (google.api_core.retry_async.AsyncRetry): Designation of what errors, if any,
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

            http_options = _BaseCloudRedisRestTransport._BaseDeleteInstance._get_http_options()
            request, metadata = await self._interceptor.pre_delete_instance(request, metadata)
            transcoded_request = _BaseCloudRedisRestTransport._BaseDeleteInstance._get_transcoded_request(http_options, request)

            # Jsonify the query params
            query_params = _BaseCloudRedisRestTransport._BaseDeleteInstance._get_query_params_json(transcoded_request)

            # Send the request
            response = await AsyncCloudRedisRestTransport._DeleteInstance._get_response(self._host, metadata, query_params, self._session, timeout, transcoded_request)

            # In case of error, raise the appropriate core_exceptions.GoogleAPICallError exception
            # subclass.
            if response.status_code >= 400:
                content = await response.read()
                payload = json.loads(content.decode('utf-8'))
                request_url = "{host}{uri}".format(host=self._host, uri=transcoded_request['uri'])
                method = transcoded_request['method']
                raise core_exceptions.format_http_response_error(response, method, request_url, payload)  # type: ignore

            # Return the response
            resp = operations_pb2.Operation()
            pb_resp = resp
            content = await response.read()
            json_format.Parse(content, pb_resp, ignore_unknown_fields=True)
            resp = await self._interceptor.post_delete_instance(resp)
            return resp

    class _ExportInstance(_BaseCloudRedisRestTransport._BaseExportInstance, AsyncCloudRedisRestStub):
        def __hash__(self):
            return hash("AsyncCloudRedisRestTransport.ExportInstance")

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
                    request: cloud_redis.ExportInstanceRequest, *,
                    retry: OptionalRetry=gapic_v1.method.DEFAULT,
                    timeout: Optional[float]=None,
                    metadata: Sequence[Tuple[str, str]]=(),
                    ) -> operations_pb2.Operation:
            r"""Call the export instance method over HTTP.

            Args:
                request (~.cloud_redis.ExportInstanceRequest):
                    The request object. Request for
                [Export][google.cloud.redis.v1.CloudRedis.ExportInstance].
                retry (google.api_core.retry_async.AsyncRetry): Designation of what errors, if any,
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

            http_options = _BaseCloudRedisRestTransport._BaseExportInstance._get_http_options()
            request, metadata = await self._interceptor.pre_export_instance(request, metadata)
            transcoded_request = _BaseCloudRedisRestTransport._BaseExportInstance._get_transcoded_request(http_options, request)

            body = _BaseCloudRedisRestTransport._BaseExportInstance._get_request_body_json(transcoded_request)

            # Jsonify the query params
            query_params = _BaseCloudRedisRestTransport._BaseExportInstance._get_query_params_json(transcoded_request)

            # Send the request
            response = await AsyncCloudRedisRestTransport._ExportInstance._get_response(self._host, metadata, query_params, self._session, timeout, transcoded_request, body)

            # In case of error, raise the appropriate core_exceptions.GoogleAPICallError exception
            # subclass.
            if response.status_code >= 400:
                content = await response.read()
                payload = json.loads(content.decode('utf-8'))
                request_url = "{host}{uri}".format(host=self._host, uri=transcoded_request['uri'])
                method = transcoded_request['method']
                raise core_exceptions.format_http_response_error(response, method, request_url, payload)  # type: ignore

            # Return the response
            resp = operations_pb2.Operation()
            pb_resp = resp
            content = await response.read()
            json_format.Parse(content, pb_resp, ignore_unknown_fields=True)
            resp = await self._interceptor.post_export_instance(resp)
            return resp

    class _FailoverInstance(_BaseCloudRedisRestTransport._BaseFailoverInstance, AsyncCloudRedisRestStub):
        def __hash__(self):
            return hash("AsyncCloudRedisRestTransport.FailoverInstance")

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
                    request: cloud_redis.FailoverInstanceRequest, *,
                    retry: OptionalRetry=gapic_v1.method.DEFAULT,
                    timeout: Optional[float]=None,
                    metadata: Sequence[Tuple[str, str]]=(),
                    ) -> operations_pb2.Operation:
            r"""Call the failover instance method over HTTP.

            Args:
                request (~.cloud_redis.FailoverInstanceRequest):
                    The request object. Request for
                [Failover][google.cloud.redis.v1.CloudRedis.FailoverInstance].
                retry (google.api_core.retry_async.AsyncRetry): Designation of what errors, if any,
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

            http_options = _BaseCloudRedisRestTransport._BaseFailoverInstance._get_http_options()
            request, metadata = await self._interceptor.pre_failover_instance(request, metadata)
            transcoded_request = _BaseCloudRedisRestTransport._BaseFailoverInstance._get_transcoded_request(http_options, request)

            body = _BaseCloudRedisRestTransport._BaseFailoverInstance._get_request_body_json(transcoded_request)

            # Jsonify the query params
            query_params = _BaseCloudRedisRestTransport._BaseFailoverInstance._get_query_params_json(transcoded_request)

            # Send the request
            response = await AsyncCloudRedisRestTransport._FailoverInstance._get_response(self._host, metadata, query_params, self._session, timeout, transcoded_request, body)

            # In case of error, raise the appropriate core_exceptions.GoogleAPICallError exception
            # subclass.
            if response.status_code >= 400:
                content = await response.read()
                payload = json.loads(content.decode('utf-8'))
                request_url = "{host}{uri}".format(host=self._host, uri=transcoded_request['uri'])
                method = transcoded_request['method']
                raise core_exceptions.format_http_response_error(response, method, request_url, payload)  # type: ignore

            # Return the response
            resp = operations_pb2.Operation()
            pb_resp = resp
            content = await response.read()
            json_format.Parse(content, pb_resp, ignore_unknown_fields=True)
            resp = await self._interceptor.post_failover_instance(resp)
            return resp

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
                retry (google.api_core.retry_async.AsyncRetry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, str]]): Strings which should be
                    sent along with the request as metadata.

            Returns:
                ~.cloud_redis.Instance:
                    A Memorystore for Redis instance.
            """

            http_options = _BaseCloudRedisRestTransport._BaseGetInstance._get_http_options()
            request, metadata = await self._interceptor.pre_get_instance(request, metadata)
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
                raise core_exceptions.format_http_response_error(response, method, request_url, payload)  # type: ignore

            # Return the response
            resp = cloud_redis.Instance()
            pb_resp = cloud_redis.Instance.pb(resp)
            content = await response.read()
            json_format.Parse(content, pb_resp, ignore_unknown_fields=True)
            resp = await self._interceptor.post_get_instance(resp)
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
                retry (google.api_core.retry_async.AsyncRetry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, str]]): Strings which should be
                    sent along with the request as metadata.

            Returns:
                ~.cloud_redis.InstanceAuthString:
                    Instance AUTH string details.
            """

            http_options = _BaseCloudRedisRestTransport._BaseGetInstanceAuthString._get_http_options()
            request, metadata = await self._interceptor.pre_get_instance_auth_string(request, metadata)
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
                raise core_exceptions.format_http_response_error(response, method, request_url, payload)  # type: ignore

            # Return the response
            resp = cloud_redis.InstanceAuthString()
            pb_resp = cloud_redis.InstanceAuthString.pb(resp)
            content = await response.read()
            json_format.Parse(content, pb_resp, ignore_unknown_fields=True)
            resp = await self._interceptor.post_get_instance_auth_string(resp)
            return resp

    class _ImportInstance(_BaseCloudRedisRestTransport._BaseImportInstance, AsyncCloudRedisRestStub):
        def __hash__(self):
            return hash("AsyncCloudRedisRestTransport.ImportInstance")

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
                    request: cloud_redis.ImportInstanceRequest, *,
                    retry: OptionalRetry=gapic_v1.method.DEFAULT,
                    timeout: Optional[float]=None,
                    metadata: Sequence[Tuple[str, str]]=(),
                    ) -> operations_pb2.Operation:
            r"""Call the import instance method over HTTP.

            Args:
                request (~.cloud_redis.ImportInstanceRequest):
                    The request object. Request for
                [Import][google.cloud.redis.v1.CloudRedis.ImportInstance].
                retry (google.api_core.retry_async.AsyncRetry): Designation of what errors, if any,
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

            http_options = _BaseCloudRedisRestTransport._BaseImportInstance._get_http_options()
            request, metadata = await self._interceptor.pre_import_instance(request, metadata)
            transcoded_request = _BaseCloudRedisRestTransport._BaseImportInstance._get_transcoded_request(http_options, request)

            body = _BaseCloudRedisRestTransport._BaseImportInstance._get_request_body_json(transcoded_request)

            # Jsonify the query params
            query_params = _BaseCloudRedisRestTransport._BaseImportInstance._get_query_params_json(transcoded_request)

            # Send the request
            response = await AsyncCloudRedisRestTransport._ImportInstance._get_response(self._host, metadata, query_params, self._session, timeout, transcoded_request, body)

            # In case of error, raise the appropriate core_exceptions.GoogleAPICallError exception
            # subclass.
            if response.status_code >= 400:
                content = await response.read()
                payload = json.loads(content.decode('utf-8'))
                request_url = "{host}{uri}".format(host=self._host, uri=transcoded_request['uri'])
                method = transcoded_request['method']
                raise core_exceptions.format_http_response_error(response, method, request_url, payload)  # type: ignore

            # Return the response
            resp = operations_pb2.Operation()
            pb_resp = resp
            content = await response.read()
            json_format.Parse(content, pb_resp, ignore_unknown_fields=True)
            resp = await self._interceptor.post_import_instance(resp)
            return resp

    class _ListInstances(_BaseCloudRedisRestTransport._BaseListInstances, AsyncCloudRedisRestStub):
        def __hash__(self):
            return hash("AsyncCloudRedisRestTransport.ListInstances")

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
                    request: cloud_redis.ListInstancesRequest, *,
                    retry: OptionalRetry=gapic_v1.method.DEFAULT,
                    timeout: Optional[float]=None,
                    metadata: Sequence[Tuple[str, str]]=(),
                    ) -> cloud_redis.ListInstancesResponse:
            r"""Call the list instances method over HTTP.

            Args:
                request (~.cloud_redis.ListInstancesRequest):
                    The request object. Request for
                [ListInstances][google.cloud.redis.v1.CloudRedis.ListInstances].
                retry (google.api_core.retry_async.AsyncRetry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, str]]): Strings which should be
                    sent along with the request as metadata.

            Returns:
                ~.cloud_redis.ListInstancesResponse:
                    Response for
                [ListInstances][google.cloud.redis.v1.CloudRedis.ListInstances].

            """

            http_options = _BaseCloudRedisRestTransport._BaseListInstances._get_http_options()
            request, metadata = await self._interceptor.pre_list_instances(request, metadata)
            transcoded_request = _BaseCloudRedisRestTransport._BaseListInstances._get_transcoded_request(http_options, request)

            # Jsonify the query params
            query_params = _BaseCloudRedisRestTransport._BaseListInstances._get_query_params_json(transcoded_request)

            # Send the request
            response = await AsyncCloudRedisRestTransport._ListInstances._get_response(self._host, metadata, query_params, self._session, timeout, transcoded_request)

            # In case of error, raise the appropriate core_exceptions.GoogleAPICallError exception
            # subclass.
            if response.status_code >= 400:
                content = await response.read()
                payload = json.loads(content.decode('utf-8'))
                request_url = "{host}{uri}".format(host=self._host, uri=transcoded_request['uri'])
                method = transcoded_request['method']
                raise core_exceptions.format_http_response_error(response, method, request_url, payload)  # type: ignore

            # Return the response
            resp = cloud_redis.ListInstancesResponse()
            pb_resp = cloud_redis.ListInstancesResponse.pb(resp)
            content = await response.read()
            json_format.Parse(content, pb_resp, ignore_unknown_fields=True)
            resp = await self._interceptor.post_list_instances(resp)
            return resp

    class _RescheduleMaintenance(_BaseCloudRedisRestTransport._BaseRescheduleMaintenance, AsyncCloudRedisRestStub):
        def __hash__(self):
            return hash("AsyncCloudRedisRestTransport.RescheduleMaintenance")

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
                    request: cloud_redis.RescheduleMaintenanceRequest, *,
                    retry: OptionalRetry=gapic_v1.method.DEFAULT,
                    timeout: Optional[float]=None,
                    metadata: Sequence[Tuple[str, str]]=(),
                    ) -> operations_pb2.Operation:
            r"""Call the reschedule maintenance method over HTTP.

            Args:
                request (~.cloud_redis.RescheduleMaintenanceRequest):
                    The request object. Request for
                [RescheduleMaintenance][google.cloud.redis.v1.CloudRedis.RescheduleMaintenance].
                retry (google.api_core.retry_async.AsyncRetry): Designation of what errors, if any,
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

            http_options = _BaseCloudRedisRestTransport._BaseRescheduleMaintenance._get_http_options()
            request, metadata = await self._interceptor.pre_reschedule_maintenance(request, metadata)
            transcoded_request = _BaseCloudRedisRestTransport._BaseRescheduleMaintenance._get_transcoded_request(http_options, request)

            body = _BaseCloudRedisRestTransport._BaseRescheduleMaintenance._get_request_body_json(transcoded_request)

            # Jsonify the query params
            query_params = _BaseCloudRedisRestTransport._BaseRescheduleMaintenance._get_query_params_json(transcoded_request)

            # Send the request
            response = await AsyncCloudRedisRestTransport._RescheduleMaintenance._get_response(self._host, metadata, query_params, self._session, timeout, transcoded_request, body)

            # In case of error, raise the appropriate core_exceptions.GoogleAPICallError exception
            # subclass.
            if response.status_code >= 400:
                content = await response.read()
                payload = json.loads(content.decode('utf-8'))
                request_url = "{host}{uri}".format(host=self._host, uri=transcoded_request['uri'])
                method = transcoded_request['method']
                raise core_exceptions.format_http_response_error(response, method, request_url, payload)  # type: ignore

            # Return the response
            resp = operations_pb2.Operation()
            pb_resp = resp
            content = await response.read()
            json_format.Parse(content, pb_resp, ignore_unknown_fields=True)
            resp = await self._interceptor.post_reschedule_maintenance(resp)
            return resp

    class _UpdateInstance(_BaseCloudRedisRestTransport._BaseUpdateInstance, AsyncCloudRedisRestStub):
        def __hash__(self):
            return hash("AsyncCloudRedisRestTransport.UpdateInstance")

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
                    request: cloud_redis.UpdateInstanceRequest, *,
                    retry: OptionalRetry=gapic_v1.method.DEFAULT,
                    timeout: Optional[float]=None,
                    metadata: Sequence[Tuple[str, str]]=(),
                    ) -> operations_pb2.Operation:
            r"""Call the update instance method over HTTP.

            Args:
                request (~.cloud_redis.UpdateInstanceRequest):
                    The request object. Request for
                [UpdateInstance][google.cloud.redis.v1.CloudRedis.UpdateInstance].
                retry (google.api_core.retry_async.AsyncRetry): Designation of what errors, if any,
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

            http_options = _BaseCloudRedisRestTransport._BaseUpdateInstance._get_http_options()
            request, metadata = await self._interceptor.pre_update_instance(request, metadata)
            transcoded_request = _BaseCloudRedisRestTransport._BaseUpdateInstance._get_transcoded_request(http_options, request)

            body = _BaseCloudRedisRestTransport._BaseUpdateInstance._get_request_body_json(transcoded_request)

            # Jsonify the query params
            query_params = _BaseCloudRedisRestTransport._BaseUpdateInstance._get_query_params_json(transcoded_request)

            # Send the request
            response = await AsyncCloudRedisRestTransport._UpdateInstance._get_response(self._host, metadata, query_params, self._session, timeout, transcoded_request, body)

            # In case of error, raise the appropriate core_exceptions.GoogleAPICallError exception
            # subclass.
            if response.status_code >= 400:
                content = await response.read()
                payload = json.loads(content.decode('utf-8'))
                request_url = "{host}{uri}".format(host=self._host, uri=transcoded_request['uri'])
                method = transcoded_request['method']
                raise core_exceptions.format_http_response_error(response, method, request_url, payload)  # type: ignore

            # Return the response
            resp = operations_pb2.Operation()
            pb_resp = resp
            content = await response.read()
            json_format.Parse(content, pb_resp, ignore_unknown_fields=True)
            resp = await self._interceptor.post_update_instance(resp)
            return resp

    class _UpgradeInstance(_BaseCloudRedisRestTransport._BaseUpgradeInstance, AsyncCloudRedisRestStub):
        def __hash__(self):
            return hash("AsyncCloudRedisRestTransport.UpgradeInstance")

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
                    request: cloud_redis.UpgradeInstanceRequest, *,
                    retry: OptionalRetry=gapic_v1.method.DEFAULT,
                    timeout: Optional[float]=None,
                    metadata: Sequence[Tuple[str, str]]=(),
                    ) -> operations_pb2.Operation:
            r"""Call the upgrade instance method over HTTP.

            Args:
                request (~.cloud_redis.UpgradeInstanceRequest):
                    The request object. Request for
                [UpgradeInstance][google.cloud.redis.v1.CloudRedis.UpgradeInstance].
                retry (google.api_core.retry_async.AsyncRetry): Designation of what errors, if any,
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

            http_options = _BaseCloudRedisRestTransport._BaseUpgradeInstance._get_http_options()
            request, metadata = await self._interceptor.pre_upgrade_instance(request, metadata)
            transcoded_request = _BaseCloudRedisRestTransport._BaseUpgradeInstance._get_transcoded_request(http_options, request)

            body = _BaseCloudRedisRestTransport._BaseUpgradeInstance._get_request_body_json(transcoded_request)

            # Jsonify the query params
            query_params = _BaseCloudRedisRestTransport._BaseUpgradeInstance._get_query_params_json(transcoded_request)

            # Send the request
            response = await AsyncCloudRedisRestTransport._UpgradeInstance._get_response(self._host, metadata, query_params, self._session, timeout, transcoded_request, body)

            # In case of error, raise the appropriate core_exceptions.GoogleAPICallError exception
            # subclass.
            if response.status_code >= 400:
                content = await response.read()
                payload = json.loads(content.decode('utf-8'))
                request_url = "{host}{uri}".format(host=self._host, uri=transcoded_request['uri'])
                method = transcoded_request['method']
                raise core_exceptions.format_http_response_error(response, method, request_url, payload)  # type: ignore

            # Return the response
            resp = operations_pb2.Operation()
            pb_resp = resp
            content = await response.read()
            json_format.Parse(content, pb_resp, ignore_unknown_fields=True)
            resp = await self._interceptor.post_upgrade_instance(resp)
            return resp

    @property
    def operations_client(self) -> AsyncOperationsRestClient:
        """Create the async client designed to process long-running operations.

        This property caches on the instance; repeated calls return the same
        client.
        """
        # Only create a new client if we do not already have one.
        if self._operations_client is None:
            http_options: Dict[str, List[Dict[str, str]]] = {
                'google.longrunning.Operations.CancelOperation': [
                    {
                        'method': 'post',
                        'uri': '/v1/{name=projects/*/locations/*/operations/*}:cancel',
                    },
                ],
                'google.longrunning.Operations.DeleteOperation': [
                    {
                        'method': 'delete',
                        'uri': '/v1/{name=projects/*/locations/*/operations/*}',
                    },
                ],
                'google.longrunning.Operations.GetOperation': [
                    {
                        'method': 'get',
                        'uri': '/v1/{name=projects/*/locations/*/operations/*}',
                    },
                ],
                'google.longrunning.Operations.ListOperations': [
                    {
                        'method': 'get',
                        'uri': '/v1/{name=projects/*/locations/*}/operations',
                    },
                ],
                'google.longrunning.Operations.WaitOperation': [
                    {
                        'method': 'post',
                        'uri': '/v2/{name=projects/*/locations/*/operations/*}:wait',
                        'body': '*',
                    },
                ],
            }

            rest_transport = operations_v1.AsyncOperationsRestTransport(  # type: ignore
                    host=self._host,
                    # use the credentials which are saved
                    credentials=self._credentials,  # type: ignore
                    http_options=http_options,
                    path_prefix="v1"
            )

            self._operations_client = AsyncOperationsRestClient(transport=rest_transport)

        # Return the client from cache.
        return self._operations_client

    @property
    def create_instance(self) -> Callable[
            [cloud_redis.CreateInstanceRequest],
            operations_pb2.Operation]:
        return self._CreateInstance(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def delete_instance(self) -> Callable[
            [cloud_redis.DeleteInstanceRequest],
            operations_pb2.Operation]:
        return self._DeleteInstance(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def export_instance(self) -> Callable[
            [cloud_redis.ExportInstanceRequest],
            operations_pb2.Operation]:
        return self._ExportInstance(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def failover_instance(self) -> Callable[
            [cloud_redis.FailoverInstanceRequest],
            operations_pb2.Operation]:
        return self._FailoverInstance(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def get_instance(self) -> Callable[
            [cloud_redis.GetInstanceRequest],
            cloud_redis.Instance]:
        return self._GetInstance(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def get_instance_auth_string(self) -> Callable[
            [cloud_redis.GetInstanceAuthStringRequest],
            cloud_redis.InstanceAuthString]:
        return self._GetInstanceAuthString(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def import_instance(self) -> Callable[
            [cloud_redis.ImportInstanceRequest],
            operations_pb2.Operation]:
        return self._ImportInstance(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def list_instances(self) -> Callable[
            [cloud_redis.ListInstancesRequest],
            cloud_redis.ListInstancesResponse]:
        return self._ListInstances(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def reschedule_maintenance(self) -> Callable[
            [cloud_redis.RescheduleMaintenanceRequest],
            operations_pb2.Operation]:
        return self._RescheduleMaintenance(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def update_instance(self) -> Callable[
            [cloud_redis.UpdateInstanceRequest],
            operations_pb2.Operation]:
        return self._UpdateInstance(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def upgrade_instance(self) -> Callable[
            [cloud_redis.UpgradeInstanceRequest],
            operations_pb2.Operation]:
        return self._UpgradeInstance(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def get_location(self):
        return self._GetLocation(self._session, self._host, self._interceptor) # type: ignore

    class _GetLocation(_BaseCloudRedisRestTransport._BaseGetLocation, AsyncCloudRedisRestStub):
        def __hash__(self):
            return hash("AsyncCloudRedisRestTransport.GetLocation")

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
            request: locations_pb2.GetLocationRequest, *,
            retry: OptionalRetry=gapic_v1.method.DEFAULT,
            timeout: Optional[float]=None,
            metadata: Sequence[Tuple[str, str]]=(),
            ) -> locations_pb2.Location:

            r"""Call the get location method over HTTP.

            Args:
                request (locations_pb2.GetLocationRequest):
                    The request object for GetLocation method.
                retry (google.api_core.retry_async.AsyncRetry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, str]]): Strings which should be
                    sent along with the request as metadata.

            Returns:
                locations_pb2.Location: Response from GetLocation method.
            """

            http_options = _BaseCloudRedisRestTransport._BaseGetLocation._get_http_options()
            request, metadata = await self._interceptor.pre_get_location(request, metadata)
            transcoded_request = _BaseCloudRedisRestTransport._BaseGetLocation._get_transcoded_request(http_options, request)

            # Jsonify the query params
            query_params = _BaseCloudRedisRestTransport._BaseGetLocation._get_query_params_json(transcoded_request)

            # Send the request
            response = await AsyncCloudRedisRestTransport._GetLocation._get_response(self._host, metadata, query_params, self._session, timeout, transcoded_request)

            # In case of error, raise the appropriate core_exceptions.GoogleAPICallError exception
            # subclass.
            if response.status_code >= 400:
                content = await response.read()
                payload = json.loads(content.decode('utf-8'))
                request_url = "{host}{uri}".format(host=self._host, uri=transcoded_request['uri'])
                method = transcoded_request['method']
                raise core_exceptions.format_http_response_error(response, method, request_url, payload)  # type: ignore

            content = await response.read()
            resp = locations_pb2.Location()
            resp = json_format.Parse(content, resp)
            resp = await self._interceptor.post_get_location(resp)
            return resp

    @property
    def list_locations(self):
        return self._ListLocations(self._session, self._host, self._interceptor) # type: ignore

    class _ListLocations(_BaseCloudRedisRestTransport._BaseListLocations, AsyncCloudRedisRestStub):
        def __hash__(self):
            return hash("AsyncCloudRedisRestTransport.ListLocations")

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
            request: locations_pb2.ListLocationsRequest, *,
            retry: OptionalRetry=gapic_v1.method.DEFAULT,
            timeout: Optional[float]=None,
            metadata: Sequence[Tuple[str, str]]=(),
            ) -> locations_pb2.ListLocationsResponse:

            r"""Call the list locations method over HTTP.

            Args:
                request (locations_pb2.ListLocationsRequest):
                    The request object for ListLocations method.
                retry (google.api_core.retry_async.AsyncRetry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, str]]): Strings which should be
                    sent along with the request as metadata.

            Returns:
                locations_pb2.ListLocationsResponse: Response from ListLocations method.
            """

            http_options = _BaseCloudRedisRestTransport._BaseListLocations._get_http_options()
            request, metadata = await self._interceptor.pre_list_locations(request, metadata)
            transcoded_request = _BaseCloudRedisRestTransport._BaseListLocations._get_transcoded_request(http_options, request)

            # Jsonify the query params
            query_params = _BaseCloudRedisRestTransport._BaseListLocations._get_query_params_json(transcoded_request)

            # Send the request
            response = await AsyncCloudRedisRestTransport._ListLocations._get_response(self._host, metadata, query_params, self._session, timeout, transcoded_request)

            # In case of error, raise the appropriate core_exceptions.GoogleAPICallError exception
            # subclass.
            if response.status_code >= 400:
                content = await response.read()
                payload = json.loads(content.decode('utf-8'))
                request_url = "{host}{uri}".format(host=self._host, uri=transcoded_request['uri'])
                method = transcoded_request['method']
                raise core_exceptions.format_http_response_error(response, method, request_url, payload)  # type: ignore

            content = await response.read()
            resp = locations_pb2.ListLocationsResponse()
            resp = json_format.Parse(content, resp)
            resp = await self._interceptor.post_list_locations(resp)
            return resp

    @property
    def cancel_operation(self):
        return self._CancelOperation(self._session, self._host, self._interceptor) # type: ignore

    class _CancelOperation(_BaseCloudRedisRestTransport._BaseCancelOperation, AsyncCloudRedisRestStub):
        def __hash__(self):
            return hash("AsyncCloudRedisRestTransport.CancelOperation")

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
            request: operations_pb2.CancelOperationRequest, *,
            retry: OptionalRetry=gapic_v1.method.DEFAULT,
            timeout: Optional[float]=None,
            metadata: Sequence[Tuple[str, str]]=(),
            ) -> None:

            r"""Call the cancel operation method over HTTP.

            Args:
                request (operations_pb2.CancelOperationRequest):
                    The request object for CancelOperation method.
                retry (google.api_core.retry_async.AsyncRetry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, str]]): Strings which should be
                    sent along with the request as metadata.
            """

            http_options = _BaseCloudRedisRestTransport._BaseCancelOperation._get_http_options()
            request, metadata = await self._interceptor.pre_cancel_operation(request, metadata)
            transcoded_request = _BaseCloudRedisRestTransport._BaseCancelOperation._get_transcoded_request(http_options, request)

            # Jsonify the query params
            query_params = _BaseCloudRedisRestTransport._BaseCancelOperation._get_query_params_json(transcoded_request)

            # Send the request
            response = await AsyncCloudRedisRestTransport._CancelOperation._get_response(self._host, metadata, query_params, self._session, timeout, transcoded_request)

            # In case of error, raise the appropriate core_exceptions.GoogleAPICallError exception
            # subclass.
            if response.status_code >= 400:
                content = await response.read()
                payload = json.loads(content.decode('utf-8'))
                request_url = "{host}{uri}".format(host=self._host, uri=transcoded_request['uri'])
                method = transcoded_request['method']
                raise core_exceptions.format_http_response_error(response, method, request_url, payload)  # type: ignore

            return await self._interceptor.post_cancel_operation(None)

    @property
    def delete_operation(self):
        return self._DeleteOperation(self._session, self._host, self._interceptor) # type: ignore

    class _DeleteOperation(_BaseCloudRedisRestTransport._BaseDeleteOperation, AsyncCloudRedisRestStub):
        def __hash__(self):
            return hash("AsyncCloudRedisRestTransport.DeleteOperation")

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
            request: operations_pb2.DeleteOperationRequest, *,
            retry: OptionalRetry=gapic_v1.method.DEFAULT,
            timeout: Optional[float]=None,
            metadata: Sequence[Tuple[str, str]]=(),
            ) -> None:

            r"""Call the delete operation method over HTTP.

            Args:
                request (operations_pb2.DeleteOperationRequest):
                    The request object for DeleteOperation method.
                retry (google.api_core.retry_async.AsyncRetry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, str]]): Strings which should be
                    sent along with the request as metadata.
            """

            http_options = _BaseCloudRedisRestTransport._BaseDeleteOperation._get_http_options()
            request, metadata = await self._interceptor.pre_delete_operation(request, metadata)
            transcoded_request = _BaseCloudRedisRestTransport._BaseDeleteOperation._get_transcoded_request(http_options, request)

            # Jsonify the query params
            query_params = _BaseCloudRedisRestTransport._BaseDeleteOperation._get_query_params_json(transcoded_request)

            # Send the request
            response = await AsyncCloudRedisRestTransport._DeleteOperation._get_response(self._host, metadata, query_params, self._session, timeout, transcoded_request)

            # In case of error, raise the appropriate core_exceptions.GoogleAPICallError exception
            # subclass.
            if response.status_code >= 400:
                content = await response.read()
                payload = json.loads(content.decode('utf-8'))
                request_url = "{host}{uri}".format(host=self._host, uri=transcoded_request['uri'])
                method = transcoded_request['method']
                raise core_exceptions.format_http_response_error(response, method, request_url, payload)  # type: ignore

            return await self._interceptor.post_delete_operation(None)

    @property
    def get_operation(self):
        return self._GetOperation(self._session, self._host, self._interceptor) # type: ignore

    class _GetOperation(_BaseCloudRedisRestTransport._BaseGetOperation, AsyncCloudRedisRestStub):
        def __hash__(self):
            return hash("AsyncCloudRedisRestTransport.GetOperation")

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
            request: operations_pb2.GetOperationRequest, *,
            retry: OptionalRetry=gapic_v1.method.DEFAULT,
            timeout: Optional[float]=None,
            metadata: Sequence[Tuple[str, str]]=(),
            ) -> operations_pb2.Operation:

            r"""Call the get operation method over HTTP.

            Args:
                request (operations_pb2.GetOperationRequest):
                    The request object for GetOperation method.
                retry (google.api_core.retry_async.AsyncRetry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, str]]): Strings which should be
                    sent along with the request as metadata.

            Returns:
                operations_pb2.Operation: Response from GetOperation method.
            """

            http_options = _BaseCloudRedisRestTransport._BaseGetOperation._get_http_options()
            request, metadata = await self._interceptor.pre_get_operation(request, metadata)
            transcoded_request = _BaseCloudRedisRestTransport._BaseGetOperation._get_transcoded_request(http_options, request)

            # Jsonify the query params
            query_params = _BaseCloudRedisRestTransport._BaseGetOperation._get_query_params_json(transcoded_request)

            # Send the request
            response = await AsyncCloudRedisRestTransport._GetOperation._get_response(self._host, metadata, query_params, self._session, timeout, transcoded_request)

            # In case of error, raise the appropriate core_exceptions.GoogleAPICallError exception
            # subclass.
            if response.status_code >= 400:
                content = await response.read()
                payload = json.loads(content.decode('utf-8'))
                request_url = "{host}{uri}".format(host=self._host, uri=transcoded_request['uri'])
                method = transcoded_request['method']
                raise core_exceptions.format_http_response_error(response, method, request_url, payload)  # type: ignore

            content = await response.read()
            resp = operations_pb2.Operation()
            resp = json_format.Parse(content, resp)
            resp = await self._interceptor.post_get_operation(resp)
            return resp

    @property
    def list_operations(self):
        return self._ListOperations(self._session, self._host, self._interceptor) # type: ignore

    class _ListOperations(_BaseCloudRedisRestTransport._BaseListOperations, AsyncCloudRedisRestStub):
        def __hash__(self):
            return hash("AsyncCloudRedisRestTransport.ListOperations")

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
            request: operations_pb2.ListOperationsRequest, *,
            retry: OptionalRetry=gapic_v1.method.DEFAULT,
            timeout: Optional[float]=None,
            metadata: Sequence[Tuple[str, str]]=(),
            ) -> operations_pb2.ListOperationsResponse:

            r"""Call the list operations method over HTTP.

            Args:
                request (operations_pb2.ListOperationsRequest):
                    The request object for ListOperations method.
                retry (google.api_core.retry_async.AsyncRetry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, str]]): Strings which should be
                    sent along with the request as metadata.

            Returns:
                operations_pb2.ListOperationsResponse: Response from ListOperations method.
            """

            http_options = _BaseCloudRedisRestTransport._BaseListOperations._get_http_options()
            request, metadata = await self._interceptor.pre_list_operations(request, metadata)
            transcoded_request = _BaseCloudRedisRestTransport._BaseListOperations._get_transcoded_request(http_options, request)

            # Jsonify the query params
            query_params = _BaseCloudRedisRestTransport._BaseListOperations._get_query_params_json(transcoded_request)

            # Send the request
            response = await AsyncCloudRedisRestTransport._ListOperations._get_response(self._host, metadata, query_params, self._session, timeout, transcoded_request)

            # In case of error, raise the appropriate core_exceptions.GoogleAPICallError exception
            # subclass.
            if response.status_code >= 400:
                content = await response.read()
                payload = json.loads(content.decode('utf-8'))
                request_url = "{host}{uri}".format(host=self._host, uri=transcoded_request['uri'])
                method = transcoded_request['method']
                raise core_exceptions.format_http_response_error(response, method, request_url, payload)  # type: ignore

            content = await response.read()
            resp = operations_pb2.ListOperationsResponse()
            resp = json_format.Parse(content, resp)
            resp = await self._interceptor.post_list_operations(resp)
            return resp

    @property
    def wait_operation(self):
        return self._WaitOperation(self._session, self._host, self._interceptor) # type: ignore

    class _WaitOperation(_BaseCloudRedisRestTransport._BaseWaitOperation, AsyncCloudRedisRestStub):
        def __hash__(self):
            return hash("AsyncCloudRedisRestTransport.WaitOperation")

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
            request: operations_pb2.WaitOperationRequest, *,
            retry: OptionalRetry=gapic_v1.method.DEFAULT,
            timeout: Optional[float]=None,
            metadata: Sequence[Tuple[str, str]]=(),
            ) -> operations_pb2.Operation:

            r"""Call the wait operation method over HTTP.

            Args:
                request (operations_pb2.WaitOperationRequest):
                    The request object for WaitOperation method.
                retry (google.api_core.retry_async.AsyncRetry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, str]]): Strings which should be
                    sent along with the request as metadata.

            Returns:
                operations_pb2.Operation: Response from WaitOperation method.
            """

            http_options = _BaseCloudRedisRestTransport._BaseWaitOperation._get_http_options()
            request, metadata = await self._interceptor.pre_wait_operation(request, metadata)
            transcoded_request = _BaseCloudRedisRestTransport._BaseWaitOperation._get_transcoded_request(http_options, request)

            body = _BaseCloudRedisRestTransport._BaseWaitOperation._get_request_body_json(transcoded_request)

            # Jsonify the query params
            query_params = _BaseCloudRedisRestTransport._BaseWaitOperation._get_query_params_json(transcoded_request)

            # Send the request
            response = await AsyncCloudRedisRestTransport._WaitOperation._get_response(self._host, metadata, query_params, self._session, timeout, transcoded_request, body)

            # In case of error, raise the appropriate core_exceptions.GoogleAPICallError exception
            # subclass.
            if response.status_code >= 400:
                content = await response.read()
                payload = json.loads(content.decode('utf-8'))
                request_url = "{host}{uri}".format(host=self._host, uri=transcoded_request['uri'])
                method = transcoded_request['method']
                raise core_exceptions.format_http_response_error(response, method, request_url, payload)  # type: ignore

            content = await response.read()
            resp = operations_pb2.Operation()
            resp = json_format.Parse(content, resp)
            resp = await self._interceptor.post_wait_operation(resp)
            return resp

    @property
    def kind(self) -> str:
        return "rest_asyncio"

    async def close(self):
        await self._session.close()

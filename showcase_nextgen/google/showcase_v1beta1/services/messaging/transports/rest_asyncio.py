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
    raise ImportError("`rest_asyncio` transport requires the library to be installed with the `async_rest` extra. Install the library with the `async_rest` extra using `pip install google-showcase[async_rest]`") from e

from google.auth.aio import credentials as ga_credentials_async  # type: ignore

from google.api_core import exceptions as core_exceptions
from google.api_core import gapic_v1
from google.api_core import operations_v1
from google.iam.v1 import iam_policy_pb2  # type: ignore
from google.iam.v1 import policy_pb2  # type: ignore
from google.cloud.location import locations_pb2 # type: ignore
from google.api_core import retry_async as retries
from google.api_core import rest_helpers
from google.api_core import rest_streaming_async  # type: ignore


from google.protobuf import json_format
from google.api_core import operations_v1
from google.iam.v1 import iam_policy_pb2  # type: ignore
from google.iam.v1 import policy_pb2  # type: ignore
from google.cloud.location import locations_pb2 # type: ignore

import json  # type: ignore
import dataclasses
from typing import Any, Dict, List, Callable, Tuple, Optional, Sequence, Union


from google.protobuf import empty_pb2  # type: ignore
from google.showcase_v1beta1.types import messaging_pb2  # type: ignore
from google.longrunning import operations_pb2  # type: ignore


from .rest_base import _BaseMessagingRestTransport

from .base import DEFAULT_CLIENT_INFO as BASE_DEFAULT_CLIENT_INFO

try:
    OptionalRetry = Union[retries.AsyncRetry, gapic_v1.method._MethodDefault, None]
except AttributeError:  # pragma: NO COVER
    OptionalRetry = Union[retries.AsyncRetry, object, None]  # type: ignore

DEFAULT_CLIENT_INFO = gapic_v1.client_info.ClientInfo(
    gapic_version=BASE_DEFAULT_CLIENT_INFO.gapic_version,
    grpc_version=None,
    rest_version=f"google-auth@{google.auth.__version__}",
)


class AsyncMessagingRestInterceptor:
    """Asynchronous Interceptor for Messaging.

    Interceptors are used to manipulate requests, request metadata, and responses
    in arbitrary ways.
    Example use cases include:
    * Logging
    * Verifying requests according to service or custom semantics
    * Stripping extraneous information from responses

    These use cases and more can be enabled by injecting an
    instance of a custom subclass when constructing the AsyncMessagingRestTransport.

    .. code-block:: python
        class MyCustomMessagingInterceptor(MessagingRestInterceptor):
            async def pre_create_blurb(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            async def post_create_blurb(self, response):
                logging.log(f"Received response: {response}")
                return response

            async def pre_create_room(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            async def post_create_room(self, response):
                logging.log(f"Received response: {response}")
                return response

            async def pre_delete_blurb(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            async def pre_delete_room(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            async def pre_get_blurb(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            async def post_get_blurb(self, response):
                logging.log(f"Received response: {response}")
                return response

            async def pre_get_room(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            async def post_get_room(self, response):
                logging.log(f"Received response: {response}")
                return response

            async def pre_list_blurbs(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            async def post_list_blurbs(self, response):
                logging.log(f"Received response: {response}")
                return response

            async def pre_list_rooms(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            async def post_list_rooms(self, response):
                logging.log(f"Received response: {response}")
                return response

            async def pre_search_blurbs(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            async def post_search_blurbs(self, response):
                logging.log(f"Received response: {response}")
                return response

            async def pre_stream_blurbs(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            async def post_stream_blurbs(self, response):
                logging.log(f"Received response: {response}")
                return response

            async def pre_update_blurb(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            async def post_update_blurb(self, response):
                logging.log(f"Received response: {response}")
                return response

            async def pre_update_room(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            async def post_update_room(self, response):
                logging.log(f"Received response: {response}")
                return response

        transport = AsyncMessagingRestTransport(interceptor=MyCustomMessagingInterceptor())
        client = async MessagingClient(transport=transport)


    """
    async def pre_create_blurb(self, request: messaging_pb2.CreateBlurbRequest, metadata: Sequence[Tuple[str, str]]) -> Tuple[messaging_pb2.CreateBlurbRequest, Sequence[Tuple[str, str]]]:
        """Pre-rpc interceptor for create_blurb

        Override in a subclass to manipulate the request or metadata
        before they are sent to the Messaging server.
        """
        return request, metadata

    async def post_create_blurb(self, response: messaging_pb2.Blurb) -> messaging_pb2.Blurb:
        """Post-rpc interceptor for create_blurb

        Override in a subclass to manipulate the response
        after it is returned by the Messaging server but before
        it is returned to user code.
        """
        return response

    async def pre_create_room(self, request: messaging_pb2.CreateRoomRequest, metadata: Sequence[Tuple[str, str]]) -> Tuple[messaging_pb2.CreateRoomRequest, Sequence[Tuple[str, str]]]:
        """Pre-rpc interceptor for create_room

        Override in a subclass to manipulate the request or metadata
        before they are sent to the Messaging server.
        """
        return request, metadata

    async def post_create_room(self, response: messaging_pb2.Room) -> messaging_pb2.Room:
        """Post-rpc interceptor for create_room

        Override in a subclass to manipulate the response
        after it is returned by the Messaging server but before
        it is returned to user code.
        """
        return response

    async def pre_delete_blurb(self, request: messaging_pb2.DeleteBlurbRequest, metadata: Sequence[Tuple[str, str]]) -> Tuple[messaging_pb2.DeleteBlurbRequest, Sequence[Tuple[str, str]]]:
        """Pre-rpc interceptor for delete_blurb

        Override in a subclass to manipulate the request or metadata
        before they are sent to the Messaging server.
        """
        return request, metadata

    async def pre_delete_room(self, request: messaging_pb2.DeleteRoomRequest, metadata: Sequence[Tuple[str, str]]) -> Tuple[messaging_pb2.DeleteRoomRequest, Sequence[Tuple[str, str]]]:
        """Pre-rpc interceptor for delete_room

        Override in a subclass to manipulate the request or metadata
        before they are sent to the Messaging server.
        """
        return request, metadata

    async def pre_get_blurb(self, request: messaging_pb2.GetBlurbRequest, metadata: Sequence[Tuple[str, str]]) -> Tuple[messaging_pb2.GetBlurbRequest, Sequence[Tuple[str, str]]]:
        """Pre-rpc interceptor for get_blurb

        Override in a subclass to manipulate the request or metadata
        before they are sent to the Messaging server.
        """
        return request, metadata

    async def post_get_blurb(self, response: messaging_pb2.Blurb) -> messaging_pb2.Blurb:
        """Post-rpc interceptor for get_blurb

        Override in a subclass to manipulate the response
        after it is returned by the Messaging server but before
        it is returned to user code.
        """
        return response

    async def pre_get_room(self, request: messaging_pb2.GetRoomRequest, metadata: Sequence[Tuple[str, str]]) -> Tuple[messaging_pb2.GetRoomRequest, Sequence[Tuple[str, str]]]:
        """Pre-rpc interceptor for get_room

        Override in a subclass to manipulate the request or metadata
        before they are sent to the Messaging server.
        """
        return request, metadata

    async def post_get_room(self, response: messaging_pb2.Room) -> messaging_pb2.Room:
        """Post-rpc interceptor for get_room

        Override in a subclass to manipulate the response
        after it is returned by the Messaging server but before
        it is returned to user code.
        """
        return response

    async def pre_list_blurbs(self, request: messaging_pb2.ListBlurbsRequest, metadata: Sequence[Tuple[str, str]]) -> Tuple[messaging_pb2.ListBlurbsRequest, Sequence[Tuple[str, str]]]:
        """Pre-rpc interceptor for list_blurbs

        Override in a subclass to manipulate the request or metadata
        before they are sent to the Messaging server.
        """
        return request, metadata

    async def post_list_blurbs(self, response: messaging_pb2.ListBlurbsResponse) -> messaging_pb2.ListBlurbsResponse:
        """Post-rpc interceptor for list_blurbs

        Override in a subclass to manipulate the response
        after it is returned by the Messaging server but before
        it is returned to user code.
        """
        return response

    async def pre_list_rooms(self, request: messaging_pb2.ListRoomsRequest, metadata: Sequence[Tuple[str, str]]) -> Tuple[messaging_pb2.ListRoomsRequest, Sequence[Tuple[str, str]]]:
        """Pre-rpc interceptor for list_rooms

        Override in a subclass to manipulate the request or metadata
        before they are sent to the Messaging server.
        """
        return request, metadata

    async def post_list_rooms(self, response: messaging_pb2.ListRoomsResponse) -> messaging_pb2.ListRoomsResponse:
        """Post-rpc interceptor for list_rooms

        Override in a subclass to manipulate the response
        after it is returned by the Messaging server but before
        it is returned to user code.
        """
        return response

    async def pre_search_blurbs(self, request: messaging_pb2.SearchBlurbsRequest, metadata: Sequence[Tuple[str, str]]) -> Tuple[messaging_pb2.SearchBlurbsRequest, Sequence[Tuple[str, str]]]:
        """Pre-rpc interceptor for search_blurbs

        Override in a subclass to manipulate the request or metadata
        before they are sent to the Messaging server.
        """
        return request, metadata

    async def post_search_blurbs(self, response: operations_pb2.Operation) -> operations_pb2.Operation:
        """Post-rpc interceptor for search_blurbs

        Override in a subclass to manipulate the response
        after it is returned by the Messaging server but before
        it is returned to user code.
        """
        return response

    async def pre_stream_blurbs(self, request: messaging_pb2.StreamBlurbsRequest, metadata: Sequence[Tuple[str, str]]) -> Tuple[messaging_pb2.StreamBlurbsRequest, Sequence[Tuple[str, str]]]:
        """Pre-rpc interceptor for stream_blurbs

        Override in a subclass to manipulate the request or metadata
        before they are sent to the Messaging server.
        """
        return request, metadata

    async def post_stream_blurbs(self, response: rest_streaming_async.AsyncResponseIterator) -> rest_streaming_async.AsyncResponseIterator:
        """Post-rpc interceptor for stream_blurbs

        Override in a subclass to manipulate the response
        after it is returned by the Messaging server but before
        it is returned to user code.
        """
        return response

    async def pre_update_blurb(self, request: messaging_pb2.UpdateBlurbRequest, metadata: Sequence[Tuple[str, str]]) -> Tuple[messaging_pb2.UpdateBlurbRequest, Sequence[Tuple[str, str]]]:
        """Pre-rpc interceptor for update_blurb

        Override in a subclass to manipulate the request or metadata
        before they are sent to the Messaging server.
        """
        return request, metadata

    async def post_update_blurb(self, response: messaging_pb2.Blurb) -> messaging_pb2.Blurb:
        """Post-rpc interceptor for update_blurb

        Override in a subclass to manipulate the response
        after it is returned by the Messaging server but before
        it is returned to user code.
        """
        return response

    async def pre_update_room(self, request: messaging_pb2.UpdateRoomRequest, metadata: Sequence[Tuple[str, str]]) -> Tuple[messaging_pb2.UpdateRoomRequest, Sequence[Tuple[str, str]]]:
        """Pre-rpc interceptor for update_room

        Override in a subclass to manipulate the request or metadata
        before they are sent to the Messaging server.
        """
        return request, metadata

    async def post_update_room(self, response: messaging_pb2.Room) -> messaging_pb2.Room:
        """Post-rpc interceptor for update_room

        Override in a subclass to manipulate the response
        after it is returned by the Messaging server but before
        it is returned to user code.
        """
        return response

    async def pre_list_locations(
        self, request: locations_pb2.ListLocationsRequest, metadata: Sequence[Tuple[str, str]]
    ) -> Tuple[locations_pb2.ListLocationsRequest, Sequence[Tuple[str, str]]]:
        """Pre-rpc interceptor for list_locations

        Override in a subclass to manipulate the request or metadata
        before they are sent to the Messaging server.
        """
        return request, metadata

    async def post_list_locations(
        self, response: locations_pb2.ListLocationsResponse
    ) -> locations_pb2.ListLocationsResponse:
        """Post-rpc interceptor for list_locations

        Override in a subclass to manipulate the response
        after it is returned by the Messaging server but before
        it is returned to user code.
        """
        return response

    async def pre_get_location(
        self, request: locations_pb2.GetLocationRequest, metadata: Sequence[Tuple[str, str]]
    ) -> Tuple[locations_pb2.GetLocationRequest, Sequence[Tuple[str, str]]]:
        """Pre-rpc interceptor for get_location

        Override in a subclass to manipulate the request or metadata
        before they are sent to the Messaging server.
        """
        return request, metadata

    async def post_get_location(
        self, response: locations_pb2.Location
    ) -> locations_pb2.Location:
        """Post-rpc interceptor for get_location

        Override in a subclass to manipulate the response
        after it is returned by the Messaging server but before
        it is returned to user code.
        """
        return response

    async def pre_set_iam_policy(
        self, request: iam_policy_pb2.SetIamPolicyRequest, metadata: Sequence[Tuple[str, str]]
    ) -> Tuple[iam_policy_pb2.SetIamPolicyRequest, Sequence[Tuple[str, str]]]:
        """Pre-rpc interceptor for set_iam_policy

        Override in a subclass to manipulate the request or metadata
        before they are sent to the Messaging server.
        """
        return request, metadata

    async def post_set_iam_policy(
        self, response: policy_pb2.Policy
    ) -> policy_pb2.Policy:
        """Post-rpc interceptor for set_iam_policy

        Override in a subclass to manipulate the response
        after it is returned by the Messaging server but before
        it is returned to user code.
        """
        return response

    async def pre_get_iam_policy(
        self, request: iam_policy_pb2.GetIamPolicyRequest, metadata: Sequence[Tuple[str, str]]
    ) -> Tuple[iam_policy_pb2.GetIamPolicyRequest, Sequence[Tuple[str, str]]]:
        """Pre-rpc interceptor for get_iam_policy

        Override in a subclass to manipulate the request or metadata
        before they are sent to the Messaging server.
        """
        return request, metadata

    async def post_get_iam_policy(
        self, response: policy_pb2.Policy
    ) -> policy_pb2.Policy:
        """Post-rpc interceptor for get_iam_policy

        Override in a subclass to manipulate the response
        after it is returned by the Messaging server but before
        it is returned to user code.
        """
        return response

    async def pre_test_iam_permissions(
        self, request: iam_policy_pb2.TestIamPermissionsRequest, metadata: Sequence[Tuple[str, str]]
    ) -> Tuple[iam_policy_pb2.TestIamPermissionsRequest, Sequence[Tuple[str, str]]]:
        """Pre-rpc interceptor for test_iam_permissions

        Override in a subclass to manipulate the request or metadata
        before they are sent to the Messaging server.
        """
        return request, metadata

    async def post_test_iam_permissions(
        self, response: iam_policy_pb2.TestIamPermissionsResponse
    ) -> iam_policy_pb2.TestIamPermissionsResponse:
        """Post-rpc interceptor for test_iam_permissions

        Override in a subclass to manipulate the response
        after it is returned by the Messaging server but before
        it is returned to user code.
        """
        return response

    async def pre_list_operations(
        self, request: operations_pb2.ListOperationsRequest, metadata: Sequence[Tuple[str, str]]
    ) -> Tuple[operations_pb2.ListOperationsRequest, Sequence[Tuple[str, str]]]:
        """Pre-rpc interceptor for list_operations

        Override in a subclass to manipulate the request or metadata
        before they are sent to the Messaging server.
        """
        return request, metadata

    async def post_list_operations(
        self, response: operations_pb2.ListOperationsResponse
    ) -> operations_pb2.ListOperationsResponse:
        """Post-rpc interceptor for list_operations

        Override in a subclass to manipulate the response
        after it is returned by the Messaging server but before
        it is returned to user code.
        """
        return response

    async def pre_get_operation(
        self, request: operations_pb2.GetOperationRequest, metadata: Sequence[Tuple[str, str]]
    ) -> Tuple[operations_pb2.GetOperationRequest, Sequence[Tuple[str, str]]]:
        """Pre-rpc interceptor for get_operation

        Override in a subclass to manipulate the request or metadata
        before they are sent to the Messaging server.
        """
        return request, metadata

    async def post_get_operation(
        self, response: operations_pb2.Operation
    ) -> operations_pb2.Operation:
        """Post-rpc interceptor for get_operation

        Override in a subclass to manipulate the response
        after it is returned by the Messaging server but before
        it is returned to user code.
        """
        return response

    async def pre_delete_operation(
        self, request: operations_pb2.DeleteOperationRequest, metadata: Sequence[Tuple[str, str]]
    ) -> Tuple[operations_pb2.DeleteOperationRequest, Sequence[Tuple[str, str]]]:
        """Pre-rpc interceptor for delete_operation

        Override in a subclass to manipulate the request or metadata
        before they are sent to the Messaging server.
        """
        return request, metadata

    async def post_delete_operation(
        self, response: None
    ) -> None:
        """Post-rpc interceptor for delete_operation

        Override in a subclass to manipulate the response
        after it is returned by the Messaging server but before
        it is returned to user code.
        """
        return response

    async def pre_cancel_operation(
        self, request: operations_pb2.CancelOperationRequest, metadata: Sequence[Tuple[str, str]]
    ) -> Tuple[operations_pb2.CancelOperationRequest, Sequence[Tuple[str, str]]]:
        """Pre-rpc interceptor for cancel_operation

        Override in a subclass to manipulate the request or metadata
        before they are sent to the Messaging server.
        """
        return request, metadata

    async def post_cancel_operation(
        self, response: None
    ) -> None:
        """Post-rpc interceptor for cancel_operation

        Override in a subclass to manipulate the response
        after it is returned by the Messaging server but before
        it is returned to user code.
        """
        return response


@dataclasses.dataclass
class AsyncMessagingRestStub:
    _session: AsyncAuthorizedSession
    _host: str
    _interceptor: AsyncMessagingRestInterceptor

class AsyncMessagingRestTransport(_BaseMessagingRestTransport):
    """Asynchronous REST backend transport for Messaging.

    A simple messaging service that implements chat rooms and
    profile posts.
    This messaging service showcases the features that API clients
    generated by gapic-generators implement.

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
            interceptor: Optional[AsyncMessagingRestInterceptor] = None,
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
        self._interceptor = interceptor or AsyncMessagingRestInterceptor()
        self._wrap_with_kind = True
        self._prep_wrapped_messages(client_info)
        self._operations_client: Optional[operations_v1.AsyncOperationsRestClient] = None

    def _prep_wrapped_messages(self, client_info):
        """ Precompute the wrapped methods, overriding the base class method to use async wrappers."""
        self._wrapped_methods = {
            self.create_room: self._wrap_method(
                self.create_room,
                default_timeout=None,
                client_info=client_info,
            ),
            self.get_room: self._wrap_method(
                self.get_room,
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
            self.update_room: self._wrap_method(
                self.update_room,
                default_timeout=None,
                client_info=client_info,
            ),
            self.delete_room: self._wrap_method(
                self.delete_room,
                default_timeout=None,
                client_info=client_info,
            ),
            self.list_rooms: self._wrap_method(
                self.list_rooms,
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
            self.create_blurb: self._wrap_method(
                self.create_blurb,
                default_timeout=None,
                client_info=client_info,
            ),
            self.get_blurb: self._wrap_method(
                self.get_blurb,
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
            self.update_blurb: self._wrap_method(
                self.update_blurb,
                default_timeout=None,
                client_info=client_info,
            ),
            self.delete_blurb: self._wrap_method(
                self.delete_blurb,
                default_timeout=None,
                client_info=client_info,
            ),
            self.list_blurbs: self._wrap_method(
                self.list_blurbs,
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
            self.search_blurbs: self._wrap_method(
                self.search_blurbs,
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
            self.stream_blurbs: self._wrap_method(
                self.stream_blurbs,
                default_timeout=None,
                client_info=client_info,
            ),
            self.send_blurbs: self._wrap_method(
                self.send_blurbs,
                default_timeout=None,
                client_info=client_info,
            ),
            self.connect: self._wrap_method(
                self.connect,
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
            self.list_locations: self._wrap_method(
                self.list_locations,
                default_timeout=None,
                client_info=client_info,
            ),
            self.get_location: self._wrap_method(
                self.get_location,
                default_timeout=None,
                client_info=client_info,
            ),
            self.set_iam_policy: self._wrap_method(
                self.set_iam_policy,
                default_timeout=None,
                client_info=client_info,
            ),
            self.get_iam_policy: self._wrap_method(
                self.get_iam_policy,
                default_timeout=None,
                client_info=client_info,
            ),
            self.test_iam_permissions: self._wrap_method(
                self.test_iam_permissions,
                default_timeout=None,
                client_info=client_info,
            ),
            self.list_operations: self._wrap_method(
                self.list_operations,
                default_timeout=None,
                client_info=client_info,
            ),
            self.get_operation: self._wrap_method(
                self.get_operation,
                default_timeout=None,
                client_info=client_info,
            ),
            self.delete_operation: self._wrap_method(
                self.delete_operation,
                default_timeout=None,
                client_info=client_info,
            ),
            self.cancel_operation: self._wrap_method(
                self.cancel_operation,
                default_timeout=None,
                client_info=client_info,
            ),
        }

    def _wrap_method(self, func, *args, **kwargs):
        if self._wrap_with_kind:  # pragma: NO COVER
            kwargs["kind"] = self.kind
        return gapic_v1.method_async.wrap_method(func, *args, **kwargs)

    class _Connect(_BaseMessagingRestTransport._BaseConnect, AsyncMessagingRestStub):
        def __hash__(self):
            return hash("AsyncMessagingRestTransport.Connect")

        async def __call__(self,
                    request: messaging_pb2.ConnectRequest, *,
                    retry: OptionalRetry=gapic_v1.method.DEFAULT,
                    timeout: Optional[float]=None,
                    metadata: Sequence[Tuple[str, str]]=(),
                    ) -> rest_streaming_async.AsyncResponseIterator:
                raise NotImplementedError(
                    "Method Connect is not available over REST transport"
                )

    class _CreateBlurb(_BaseMessagingRestTransport._BaseCreateBlurb, AsyncMessagingRestStub):
        def __hash__(self):
            return hash("AsyncMessagingRestTransport.CreateBlurb")

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
                    request: messaging_pb2.CreateBlurbRequest, *,
                    retry: OptionalRetry=gapic_v1.method.DEFAULT,
                    timeout: Optional[float]=None,
                    metadata: Sequence[Tuple[str, str]]=(),
                    ) -> messaging_pb2.Blurb:
            r"""Call the create blurb method over HTTP.

            Args:
                request (~.messaging_pb2.CreateBlurbRequest):
                    The request object. The request message for the
                google.showcase.v1beta1.Messaging\CreateBlurb
                method.
                retry (google.api_core.retry_async.AsyncRetry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, str]]): Strings which should be
                    sent along with the request as metadata.

            Returns:
                ~.messaging_pb2.Blurb:
                    This protocol buffer message
                represents a blurb sent to a chat room
                or posted on a user profile.

            """

            http_options = _BaseMessagingRestTransport._BaseCreateBlurb._get_http_options()
            request, metadata = await self._interceptor.pre_create_blurb(request, metadata)
            transcoded_request = _BaseMessagingRestTransport._BaseCreateBlurb._get_transcoded_request(http_options, request)

            body = _BaseMessagingRestTransport._BaseCreateBlurb._get_request_body_json(transcoded_request)

            # Jsonify the query params
            query_params = _BaseMessagingRestTransport._BaseCreateBlurb._get_query_params_json(transcoded_request)

            # Send the request
            response = await AsyncMessagingRestTransport._CreateBlurb._get_response(self._host, metadata, query_params, self._session, timeout, transcoded_request, body)

            # In case of error, raise the appropriate core_exceptions.GoogleAPICallError exception
            # subclass.
            if response.status_code >= 400:
                content = await response.read()
                payload = json.loads(content.decode('utf-8'))
                request_url = "{host}{uri}".format(host=self._host, uri=transcoded_request['uri'])
                method = transcoded_request['method']
                raise core_exceptions.format_http_response_error(response, method, request_url, payload)  # type: ignore

            # Return the response
            resp = messaging_pb2.Blurb()
            pb_resp = resp
            content = await response.read()
            json_format.Parse(content, pb_resp, ignore_unknown_fields=True)
            resp = await self._interceptor.post_create_blurb(resp)
            return resp

    class _CreateRoom(_BaseMessagingRestTransport._BaseCreateRoom, AsyncMessagingRestStub):
        def __hash__(self):
            return hash("AsyncMessagingRestTransport.CreateRoom")

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
                    request: messaging_pb2.CreateRoomRequest, *,
                    retry: OptionalRetry=gapic_v1.method.DEFAULT,
                    timeout: Optional[float]=None,
                    metadata: Sequence[Tuple[str, str]]=(),
                    ) -> messaging_pb2.Room:
            r"""Call the create room method over HTTP.

            Args:
                request (~.messaging_pb2.CreateRoomRequest):
                    The request object. The request message for the
                google.showcase.v1beta1.Messaging\CreateRoom
                method.
                retry (google.api_core.retry_async.AsyncRetry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, str]]): Strings which should be
                    sent along with the request as metadata.

            Returns:
                ~.messaging_pb2.Room:
                    A chat room.
            """

            http_options = _BaseMessagingRestTransport._BaseCreateRoom._get_http_options()
            request, metadata = await self._interceptor.pre_create_room(request, metadata)
            transcoded_request = _BaseMessagingRestTransport._BaseCreateRoom._get_transcoded_request(http_options, request)

            body = _BaseMessagingRestTransport._BaseCreateRoom._get_request_body_json(transcoded_request)

            # Jsonify the query params
            query_params = _BaseMessagingRestTransport._BaseCreateRoom._get_query_params_json(transcoded_request)

            # Send the request
            response = await AsyncMessagingRestTransport._CreateRoom._get_response(self._host, metadata, query_params, self._session, timeout, transcoded_request, body)

            # In case of error, raise the appropriate core_exceptions.GoogleAPICallError exception
            # subclass.
            if response.status_code >= 400:
                content = await response.read()
                payload = json.loads(content.decode('utf-8'))
                request_url = "{host}{uri}".format(host=self._host, uri=transcoded_request['uri'])
                method = transcoded_request['method']
                raise core_exceptions.format_http_response_error(response, method, request_url, payload)  # type: ignore

            # Return the response
            resp = messaging_pb2.Room()
            pb_resp = resp
            content = await response.read()
            json_format.Parse(content, pb_resp, ignore_unknown_fields=True)
            resp = await self._interceptor.post_create_room(resp)
            return resp

    class _DeleteBlurb(_BaseMessagingRestTransport._BaseDeleteBlurb, AsyncMessagingRestStub):
        def __hash__(self):
            return hash("AsyncMessagingRestTransport.DeleteBlurb")

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
                    request: messaging_pb2.DeleteBlurbRequest, *,
                    retry: OptionalRetry=gapic_v1.method.DEFAULT,
                    timeout: Optional[float]=None,
                    metadata: Sequence[Tuple[str, str]]=(),
                    ):
            r"""Call the delete blurb method over HTTP.

            Args:
                request (~.messaging_pb2.DeleteBlurbRequest):
                    The request object. The request message for the
                google.showcase.v1beta1.Messaging\DeleteBlurb
                method.
                retry (google.api_core.retry_async.AsyncRetry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, str]]): Strings which should be
                    sent along with the request as metadata.
            """

            http_options = _BaseMessagingRestTransport._BaseDeleteBlurb._get_http_options()
            request, metadata = await self._interceptor.pre_delete_blurb(request, metadata)
            transcoded_request = _BaseMessagingRestTransport._BaseDeleteBlurb._get_transcoded_request(http_options, request)

            # Jsonify the query params
            query_params = _BaseMessagingRestTransport._BaseDeleteBlurb._get_query_params_json(transcoded_request)

            # Send the request
            response = await AsyncMessagingRestTransport._DeleteBlurb._get_response(self._host, metadata, query_params, self._session, timeout, transcoded_request)

            # In case of error, raise the appropriate core_exceptions.GoogleAPICallError exception
            # subclass.
            if response.status_code >= 400:
                content = await response.read()
                payload = json.loads(content.decode('utf-8'))
                request_url = "{host}{uri}".format(host=self._host, uri=transcoded_request['uri'])
                method = transcoded_request['method']
                raise core_exceptions.format_http_response_error(response, method, request_url, payload)  # type: ignore

    class _DeleteRoom(_BaseMessagingRestTransport._BaseDeleteRoom, AsyncMessagingRestStub):
        def __hash__(self):
            return hash("AsyncMessagingRestTransport.DeleteRoom")

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
                    request: messaging_pb2.DeleteRoomRequest, *,
                    retry: OptionalRetry=gapic_v1.method.DEFAULT,
                    timeout: Optional[float]=None,
                    metadata: Sequence[Tuple[str, str]]=(),
                    ):
            r"""Call the delete room method over HTTP.

            Args:
                request (~.messaging_pb2.DeleteRoomRequest):
                    The request object. The request message for the
                google.showcase.v1beta1.Messaging\DeleteRoom
                method.
                retry (google.api_core.retry_async.AsyncRetry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, str]]): Strings which should be
                    sent along with the request as metadata.
            """

            http_options = _BaseMessagingRestTransport._BaseDeleteRoom._get_http_options()
            request, metadata = await self._interceptor.pre_delete_room(request, metadata)
            transcoded_request = _BaseMessagingRestTransport._BaseDeleteRoom._get_transcoded_request(http_options, request)

            # Jsonify the query params
            query_params = _BaseMessagingRestTransport._BaseDeleteRoom._get_query_params_json(transcoded_request)

            # Send the request
            response = await AsyncMessagingRestTransport._DeleteRoom._get_response(self._host, metadata, query_params, self._session, timeout, transcoded_request)

            # In case of error, raise the appropriate core_exceptions.GoogleAPICallError exception
            # subclass.
            if response.status_code >= 400:
                content = await response.read()
                payload = json.loads(content.decode('utf-8'))
                request_url = "{host}{uri}".format(host=self._host, uri=transcoded_request['uri'])
                method = transcoded_request['method']
                raise core_exceptions.format_http_response_error(response, method, request_url, payload)  # type: ignore

    class _GetBlurb(_BaseMessagingRestTransport._BaseGetBlurb, AsyncMessagingRestStub):
        def __hash__(self):
            return hash("AsyncMessagingRestTransport.GetBlurb")

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
                    request: messaging_pb2.GetBlurbRequest, *,
                    retry: OptionalRetry=gapic_v1.method.DEFAULT,
                    timeout: Optional[float]=None,
                    metadata: Sequence[Tuple[str, str]]=(),
                    ) -> messaging_pb2.Blurb:
            r"""Call the get blurb method over HTTP.

            Args:
                request (~.messaging_pb2.GetBlurbRequest):
                    The request object. The request message for the
                google.showcase.v1beta1.Messaging\GetBlurb
                method.
                retry (google.api_core.retry_async.AsyncRetry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, str]]): Strings which should be
                    sent along with the request as metadata.

            Returns:
                ~.messaging_pb2.Blurb:
                    This protocol buffer message
                represents a blurb sent to a chat room
                or posted on a user profile.

            """

            http_options = _BaseMessagingRestTransport._BaseGetBlurb._get_http_options()
            request, metadata = await self._interceptor.pre_get_blurb(request, metadata)
            transcoded_request = _BaseMessagingRestTransport._BaseGetBlurb._get_transcoded_request(http_options, request)

            # Jsonify the query params
            query_params = _BaseMessagingRestTransport._BaseGetBlurb._get_query_params_json(transcoded_request)

            # Send the request
            response = await AsyncMessagingRestTransport._GetBlurb._get_response(self._host, metadata, query_params, self._session, timeout, transcoded_request)

            # In case of error, raise the appropriate core_exceptions.GoogleAPICallError exception
            # subclass.
            if response.status_code >= 400:
                content = await response.read()
                payload = json.loads(content.decode('utf-8'))
                request_url = "{host}{uri}".format(host=self._host, uri=transcoded_request['uri'])
                method = transcoded_request['method']
                raise core_exceptions.format_http_response_error(response, method, request_url, payload)  # type: ignore

            # Return the response
            resp = messaging_pb2.Blurb()
            pb_resp = resp
            content = await response.read()
            json_format.Parse(content, pb_resp, ignore_unknown_fields=True)
            resp = await self._interceptor.post_get_blurb(resp)
            return resp

    class _GetRoom(_BaseMessagingRestTransport._BaseGetRoom, AsyncMessagingRestStub):
        def __hash__(self):
            return hash("AsyncMessagingRestTransport.GetRoom")

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
                    request: messaging_pb2.GetRoomRequest, *,
                    retry: OptionalRetry=gapic_v1.method.DEFAULT,
                    timeout: Optional[float]=None,
                    metadata: Sequence[Tuple[str, str]]=(),
                    ) -> messaging_pb2.Room:
            r"""Call the get room method over HTTP.

            Args:
                request (~.messaging_pb2.GetRoomRequest):
                    The request object. The request message for the
                google.showcase.v1beta1.Messaging\GetRoom
                method.
                retry (google.api_core.retry_async.AsyncRetry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, str]]): Strings which should be
                    sent along with the request as metadata.

            Returns:
                ~.messaging_pb2.Room:
                    A chat room.
            """

            http_options = _BaseMessagingRestTransport._BaseGetRoom._get_http_options()
            request, metadata = await self._interceptor.pre_get_room(request, metadata)
            transcoded_request = _BaseMessagingRestTransport._BaseGetRoom._get_transcoded_request(http_options, request)

            # Jsonify the query params
            query_params = _BaseMessagingRestTransport._BaseGetRoom._get_query_params_json(transcoded_request)

            # Send the request
            response = await AsyncMessagingRestTransport._GetRoom._get_response(self._host, metadata, query_params, self._session, timeout, transcoded_request)

            # In case of error, raise the appropriate core_exceptions.GoogleAPICallError exception
            # subclass.
            if response.status_code >= 400:
                content = await response.read()
                payload = json.loads(content.decode('utf-8'))
                request_url = "{host}{uri}".format(host=self._host, uri=transcoded_request['uri'])
                method = transcoded_request['method']
                raise core_exceptions.format_http_response_error(response, method, request_url, payload)  # type: ignore

            # Return the response
            resp = messaging_pb2.Room()
            pb_resp = resp
            content = await response.read()
            json_format.Parse(content, pb_resp, ignore_unknown_fields=True)
            resp = await self._interceptor.post_get_room(resp)
            return resp

    class _ListBlurbs(_BaseMessagingRestTransport._BaseListBlurbs, AsyncMessagingRestStub):
        def __hash__(self):
            return hash("AsyncMessagingRestTransport.ListBlurbs")

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
                    request: messaging_pb2.ListBlurbsRequest, *,
                    retry: OptionalRetry=gapic_v1.method.DEFAULT,
                    timeout: Optional[float]=None,
                    metadata: Sequence[Tuple[str, str]]=(),
                    ) -> messaging_pb2.ListBlurbsResponse:
            r"""Call the list blurbs method over HTTP.

            Args:
                request (~.messaging_pb2.ListBlurbsRequest):
                    The request object. The request message for the
                google.showcase.v1beta1.Messaging\ListBlurbs
                method.
                retry (google.api_core.retry_async.AsyncRetry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, str]]): Strings which should be
                    sent along with the request as metadata.

            Returns:
                ~.messaging_pb2.ListBlurbsResponse:
                    The response message for the
                google.showcase.v1beta1.Messaging\ListBlurbs
                method.

            """

            http_options = _BaseMessagingRestTransport._BaseListBlurbs._get_http_options()
            request, metadata = await self._interceptor.pre_list_blurbs(request, metadata)
            transcoded_request = _BaseMessagingRestTransport._BaseListBlurbs._get_transcoded_request(http_options, request)

            # Jsonify the query params
            query_params = _BaseMessagingRestTransport._BaseListBlurbs._get_query_params_json(transcoded_request)

            # Send the request
            response = await AsyncMessagingRestTransport._ListBlurbs._get_response(self._host, metadata, query_params, self._session, timeout, transcoded_request)

            # In case of error, raise the appropriate core_exceptions.GoogleAPICallError exception
            # subclass.
            if response.status_code >= 400:
                content = await response.read()
                payload = json.loads(content.decode('utf-8'))
                request_url = "{host}{uri}".format(host=self._host, uri=transcoded_request['uri'])
                method = transcoded_request['method']
                raise core_exceptions.format_http_response_error(response, method, request_url, payload)  # type: ignore

            # Return the response
            resp = messaging_pb2.ListBlurbsResponse()
            pb_resp = resp
            content = await response.read()
            json_format.Parse(content, pb_resp, ignore_unknown_fields=True)
            resp = await self._interceptor.post_list_blurbs(resp)
            return resp

    class _ListRooms(_BaseMessagingRestTransport._BaseListRooms, AsyncMessagingRestStub):
        def __hash__(self):
            return hash("AsyncMessagingRestTransport.ListRooms")

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
                    request: messaging_pb2.ListRoomsRequest, *,
                    retry: OptionalRetry=gapic_v1.method.DEFAULT,
                    timeout: Optional[float]=None,
                    metadata: Sequence[Tuple[str, str]]=(),
                    ) -> messaging_pb2.ListRoomsResponse:
            r"""Call the list rooms method over HTTP.

            Args:
                request (~.messaging_pb2.ListRoomsRequest):
                    The request object. The request message for the
                google.showcase.v1beta1.Messaging\ListRooms
                method.
                retry (google.api_core.retry_async.AsyncRetry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, str]]): Strings which should be
                    sent along with the request as metadata.

            Returns:
                ~.messaging_pb2.ListRoomsResponse:
                    The response message for the
                google.showcase.v1beta1.Messaging\ListRooms
                method.

            """

            http_options = _BaseMessagingRestTransport._BaseListRooms._get_http_options()
            request, metadata = await self._interceptor.pre_list_rooms(request, metadata)
            transcoded_request = _BaseMessagingRestTransport._BaseListRooms._get_transcoded_request(http_options, request)

            # Jsonify the query params
            query_params = _BaseMessagingRestTransport._BaseListRooms._get_query_params_json(transcoded_request)

            # Send the request
            response = await AsyncMessagingRestTransport._ListRooms._get_response(self._host, metadata, query_params, self._session, timeout, transcoded_request)

            # In case of error, raise the appropriate core_exceptions.GoogleAPICallError exception
            # subclass.
            if response.status_code >= 400:
                content = await response.read()
                payload = json.loads(content.decode('utf-8'))
                request_url = "{host}{uri}".format(host=self._host, uri=transcoded_request['uri'])
                method = transcoded_request['method']
                raise core_exceptions.format_http_response_error(response, method, request_url, payload)  # type: ignore

            # Return the response
            resp = messaging_pb2.ListRoomsResponse()
            pb_resp = resp
            content = await response.read()
            json_format.Parse(content, pb_resp, ignore_unknown_fields=True)
            resp = await self._interceptor.post_list_rooms(resp)
            return resp

    class _SearchBlurbs(_BaseMessagingRestTransport._BaseSearchBlurbs, AsyncMessagingRestStub):
        def __hash__(self):
            return hash("AsyncMessagingRestTransport.SearchBlurbs")

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
                    request: messaging_pb2.SearchBlurbsRequest, *,
                    retry: OptionalRetry=gapic_v1.method.DEFAULT,
                    timeout: Optional[float]=None,
                    metadata: Sequence[Tuple[str, str]]=(),
                    ) -> operations_pb2.Operation:
            r"""Call the search blurbs method over HTTP.

            Args:
                request (~.messaging_pb2.SearchBlurbsRequest):
                    The request object. The request message for the
                google.showcase.v1beta1.Messaging\SearchBlurbs
                method.
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

            http_options = _BaseMessagingRestTransport._BaseSearchBlurbs._get_http_options()
            request, metadata = await self._interceptor.pre_search_blurbs(request, metadata)
            transcoded_request = _BaseMessagingRestTransport._BaseSearchBlurbs._get_transcoded_request(http_options, request)

            body = _BaseMessagingRestTransport._BaseSearchBlurbs._get_request_body_json(transcoded_request)

            # Jsonify the query params
            query_params = _BaseMessagingRestTransport._BaseSearchBlurbs._get_query_params_json(transcoded_request)

            # Send the request
            response = await AsyncMessagingRestTransport._SearchBlurbs._get_response(self._host, metadata, query_params, self._session, timeout, transcoded_request, body)

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
            resp = await self._interceptor.post_search_blurbs(resp)
            return resp

    class _SendBlurbs(_BaseMessagingRestTransport._BaseSendBlurbs, AsyncMessagingRestStub):
        def __hash__(self):
            return hash("AsyncMessagingRestTransport.SendBlurbs")

        async def __call__(self,
                    request: messaging_pb2.CreateBlurbRequest, *,
                    retry: OptionalRetry=gapic_v1.method.DEFAULT,
                    timeout: Optional[float]=None,
                    metadata: Sequence[Tuple[str, str]]=(),
                    ) -> messaging_pb2.SendBlurbsResponse:
                raise NotImplementedError(
                    "Method SendBlurbs is not available over REST transport"
                )

    class _StreamBlurbs(_BaseMessagingRestTransport._BaseStreamBlurbs, AsyncMessagingRestStub):
        def __hash__(self):
            return hash("AsyncMessagingRestTransport.StreamBlurbs")

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
                    request: messaging_pb2.StreamBlurbsRequest, *,
                    retry: OptionalRetry=gapic_v1.method.DEFAULT,
                    timeout: Optional[float]=None,
                    metadata: Sequence[Tuple[str, str]]=(),
                    ) -> rest_streaming_async.AsyncResponseIterator:
            r"""Call the stream blurbs method over HTTP.

            Args:
                request (~.messaging_pb2.StreamBlurbsRequest):
                    The request object. The request message for the
                google.showcase.v1beta1.Messaging\StreamBlurbs
                method.
                retry (google.api_core.retry_async.AsyncRetry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, str]]): Strings which should be
                    sent along with the request as metadata.

            Returns:
                ~.messaging_pb2.StreamBlurbsResponse:
                    The response message for the
                google.showcase.v1beta1.Messaging\StreamBlurbs
                method.

            """

            http_options = _BaseMessagingRestTransport._BaseStreamBlurbs._get_http_options()
            request, metadata = await self._interceptor.pre_stream_blurbs(request, metadata)
            transcoded_request = _BaseMessagingRestTransport._BaseStreamBlurbs._get_transcoded_request(http_options, request)

            body = _BaseMessagingRestTransport._BaseStreamBlurbs._get_request_body_json(transcoded_request)

            # Jsonify the query params
            query_params = _BaseMessagingRestTransport._BaseStreamBlurbs._get_query_params_json(transcoded_request)

            # Send the request
            response = await AsyncMessagingRestTransport._StreamBlurbs._get_response(self._host, metadata, query_params, self._session, timeout, transcoded_request, body)

            # In case of error, raise the appropriate core_exceptions.GoogleAPICallError exception
            # subclass.
            if response.status_code >= 400:
                content = await response.read()
                payload = json.loads(content.decode('utf-8'))
                request_url = "{host}{uri}".format(host=self._host, uri=transcoded_request['uri'])
                method = transcoded_request['method']
                raise core_exceptions.format_http_response_error(response, method, request_url, payload)  # type: ignore

            # Return the response
            resp = rest_streaming_async.AsyncResponseIterator(response, messaging_pb2.StreamBlurbsResponse)
            resp = await self._interceptor.post_stream_blurbs(resp)
            return resp

    class _UpdateBlurb(_BaseMessagingRestTransport._BaseUpdateBlurb, AsyncMessagingRestStub):
        def __hash__(self):
            return hash("AsyncMessagingRestTransport.UpdateBlurb")

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
                    request: messaging_pb2.UpdateBlurbRequest, *,
                    retry: OptionalRetry=gapic_v1.method.DEFAULT,
                    timeout: Optional[float]=None,
                    metadata: Sequence[Tuple[str, str]]=(),
                    ) -> messaging_pb2.Blurb:
            r"""Call the update blurb method over HTTP.

            Args:
                request (~.messaging_pb2.UpdateBlurbRequest):
                    The request object. The request message for the
                google.showcase.v1beta1.Messaging\UpdateBlurb
                method.
                retry (google.api_core.retry_async.AsyncRetry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, str]]): Strings which should be
                    sent along with the request as metadata.

            Returns:
                ~.messaging_pb2.Blurb:
                    This protocol buffer message
                represents a blurb sent to a chat room
                or posted on a user profile.

            """

            http_options = _BaseMessagingRestTransport._BaseUpdateBlurb._get_http_options()
            request, metadata = await self._interceptor.pre_update_blurb(request, metadata)
            transcoded_request = _BaseMessagingRestTransport._BaseUpdateBlurb._get_transcoded_request(http_options, request)

            body = _BaseMessagingRestTransport._BaseUpdateBlurb._get_request_body_json(transcoded_request)

            # Jsonify the query params
            query_params = _BaseMessagingRestTransport._BaseUpdateBlurb._get_query_params_json(transcoded_request)

            # Send the request
            response = await AsyncMessagingRestTransport._UpdateBlurb._get_response(self._host, metadata, query_params, self._session, timeout, transcoded_request, body)

            # In case of error, raise the appropriate core_exceptions.GoogleAPICallError exception
            # subclass.
            if response.status_code >= 400:
                content = await response.read()
                payload = json.loads(content.decode('utf-8'))
                request_url = "{host}{uri}".format(host=self._host, uri=transcoded_request['uri'])
                method = transcoded_request['method']
                raise core_exceptions.format_http_response_error(response, method, request_url, payload)  # type: ignore

            # Return the response
            resp = messaging_pb2.Blurb()
            pb_resp = resp
            content = await response.read()
            json_format.Parse(content, pb_resp, ignore_unknown_fields=True)
            resp = await self._interceptor.post_update_blurb(resp)
            return resp

    class _UpdateRoom(_BaseMessagingRestTransport._BaseUpdateRoom, AsyncMessagingRestStub):
        def __hash__(self):
            return hash("AsyncMessagingRestTransport.UpdateRoom")

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
                    request: messaging_pb2.UpdateRoomRequest, *,
                    retry: OptionalRetry=gapic_v1.method.DEFAULT,
                    timeout: Optional[float]=None,
                    metadata: Sequence[Tuple[str, str]]=(),
                    ) -> messaging_pb2.Room:
            r"""Call the update room method over HTTP.

            Args:
                request (~.messaging_pb2.UpdateRoomRequest):
                    The request object. The request message for the
                google.showcase.v1beta1.Messaging\UpdateRoom
                method.
                retry (google.api_core.retry_async.AsyncRetry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, str]]): Strings which should be
                    sent along with the request as metadata.

            Returns:
                ~.messaging_pb2.Room:
                    A chat room.
            """

            http_options = _BaseMessagingRestTransport._BaseUpdateRoom._get_http_options()
            request, metadata = await self._interceptor.pre_update_room(request, metadata)
            transcoded_request = _BaseMessagingRestTransport._BaseUpdateRoom._get_transcoded_request(http_options, request)

            body = _BaseMessagingRestTransport._BaseUpdateRoom._get_request_body_json(transcoded_request)

            # Jsonify the query params
            query_params = _BaseMessagingRestTransport._BaseUpdateRoom._get_query_params_json(transcoded_request)

            # Send the request
            response = await AsyncMessagingRestTransport._UpdateRoom._get_response(self._host, metadata, query_params, self._session, timeout, transcoded_request, body)

            # In case of error, raise the appropriate core_exceptions.GoogleAPICallError exception
            # subclass.
            if response.status_code >= 400:
                content = await response.read()
                payload = json.loads(content.decode('utf-8'))
                request_url = "{host}{uri}".format(host=self._host, uri=transcoded_request['uri'])
                method = transcoded_request['method']
                raise core_exceptions.format_http_response_error(response, method, request_url, payload)  # type: ignore

            # Return the response
            resp = messaging_pb2.Room()
            pb_resp = resp
            content = await response.read()
            json_format.Parse(content, pb_resp, ignore_unknown_fields=True)
            resp = await self._interceptor.post_update_room(resp)
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

            rest_transport = operations_v1.AsyncOperationsRestTransport(  # type: ignore
                    host=self._host,
                    # use the credentials which are saved
                    credentials=self._credentials,  # type: ignore
                    http_options=http_options,
                    path_prefix="v1beta1"
            )

            self._operations_client = AsyncOperationsRestClient(transport=rest_transport)

        # Return the client from cache.
        return self._operations_client

    @property
    def connect(self) -> Callable[
            [messaging_pb2.ConnectRequest],
            messaging_pb2.StreamBlurbsResponse]:
        return self._Connect(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def create_blurb(self) -> Callable[
            [messaging_pb2.CreateBlurbRequest],
            messaging_pb2.Blurb]:
        return self._CreateBlurb(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def create_room(self) -> Callable[
            [messaging_pb2.CreateRoomRequest],
            messaging_pb2.Room]:
        return self._CreateRoom(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def delete_blurb(self) -> Callable[
            [messaging_pb2.DeleteBlurbRequest],
            empty_pb2.Empty]:
        return self._DeleteBlurb(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def delete_room(self) -> Callable[
            [messaging_pb2.DeleteRoomRequest],
            empty_pb2.Empty]:
        return self._DeleteRoom(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def get_blurb(self) -> Callable[
            [messaging_pb2.GetBlurbRequest],
            messaging_pb2.Blurb]:
        return self._GetBlurb(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def get_room(self) -> Callable[
            [messaging_pb2.GetRoomRequest],
            messaging_pb2.Room]:
        return self._GetRoom(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def list_blurbs(self) -> Callable[
            [messaging_pb2.ListBlurbsRequest],
            messaging_pb2.ListBlurbsResponse]:
        return self._ListBlurbs(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def list_rooms(self) -> Callable[
            [messaging_pb2.ListRoomsRequest],
            messaging_pb2.ListRoomsResponse]:
        return self._ListRooms(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def search_blurbs(self) -> Callable[
            [messaging_pb2.SearchBlurbsRequest],
            operations_pb2.Operation]:
        return self._SearchBlurbs(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def send_blurbs(self) -> Callable[
            [messaging_pb2.CreateBlurbRequest],
            messaging_pb2.SendBlurbsResponse]:
        return self._SendBlurbs(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def stream_blurbs(self) -> Callable[
            [messaging_pb2.StreamBlurbsRequest],
            messaging_pb2.StreamBlurbsResponse]:
        return self._StreamBlurbs(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def update_blurb(self) -> Callable[
            [messaging_pb2.UpdateBlurbRequest],
            messaging_pb2.Blurb]:
        return self._UpdateBlurb(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def update_room(self) -> Callable[
            [messaging_pb2.UpdateRoomRequest],
            messaging_pb2.Room]:
        return self._UpdateRoom(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def list_locations(self):
        return self._ListLocations(self._session, self._host, self._interceptor) # type: ignore

    class _ListLocations(_BaseMessagingRestTransport._BaseListLocations, AsyncMessagingRestStub):
        def __hash__(self):
            return hash("AsyncMessagingRestTransport.ListLocations")

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

            http_options = _BaseMessagingRestTransport._BaseListLocations._get_http_options()
            request, metadata = await self._interceptor.pre_list_locations(request, metadata)
            transcoded_request = _BaseMessagingRestTransport._BaseListLocations._get_transcoded_request(http_options, request)

            # Jsonify the query params
            query_params = _BaseMessagingRestTransport._BaseListLocations._get_query_params_json(transcoded_request)

            # Send the request
            response = await AsyncMessagingRestTransport._ListLocations._get_response(self._host, metadata, query_params, self._session, timeout, transcoded_request)

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
    def get_location(self):
        return self._GetLocation(self._session, self._host, self._interceptor) # type: ignore

    class _GetLocation(_BaseMessagingRestTransport._BaseGetLocation, AsyncMessagingRestStub):
        def __hash__(self):
            return hash("AsyncMessagingRestTransport.GetLocation")

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

            http_options = _BaseMessagingRestTransport._BaseGetLocation._get_http_options()
            request, metadata = await self._interceptor.pre_get_location(request, metadata)
            transcoded_request = _BaseMessagingRestTransport._BaseGetLocation._get_transcoded_request(http_options, request)

            # Jsonify the query params
            query_params = _BaseMessagingRestTransport._BaseGetLocation._get_query_params_json(transcoded_request)

            # Send the request
            response = await AsyncMessagingRestTransport._GetLocation._get_response(self._host, metadata, query_params, self._session, timeout, transcoded_request)

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
    def set_iam_policy(self):
        return self._SetIamPolicy(self._session, self._host, self._interceptor) # type: ignore

    class _SetIamPolicy(_BaseMessagingRestTransport._BaseSetIamPolicy, AsyncMessagingRestStub):
        def __hash__(self):
            return hash("AsyncMessagingRestTransport.SetIamPolicy")

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
            request: iam_policy_pb2.SetIamPolicyRequest, *,
            retry: OptionalRetry=gapic_v1.method.DEFAULT,
            timeout: Optional[float]=None,
            metadata: Sequence[Tuple[str, str]]=(),
            ) -> policy_pb2.Policy:

            r"""Call the set iam policy method over HTTP.

            Args:
                request (iam_policy_pb2.SetIamPolicyRequest):
                    The request object for SetIamPolicy method.
                retry (google.api_core.retry_async.AsyncRetry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, str]]): Strings which should be
                    sent along with the request as metadata.

            Returns:
                policy_pb2.Policy: Response from SetIamPolicy method.
            """

            http_options = _BaseMessagingRestTransport._BaseSetIamPolicy._get_http_options()
            request, metadata = await self._interceptor.pre_set_iam_policy(request, metadata)
            transcoded_request = _BaseMessagingRestTransport._BaseSetIamPolicy._get_transcoded_request(http_options, request)

            body = _BaseMessagingRestTransport._BaseSetIamPolicy._get_request_body_json(transcoded_request)

            # Jsonify the query params
            query_params = _BaseMessagingRestTransport._BaseSetIamPolicy._get_query_params_json(transcoded_request)

            # Send the request
            response = await AsyncMessagingRestTransport._SetIamPolicy._get_response(self._host, metadata, query_params, self._session, timeout, transcoded_request, body)

            # In case of error, raise the appropriate core_exceptions.GoogleAPICallError exception
            # subclass.
            if response.status_code >= 400:
                content = await response.read()
                payload = json.loads(content.decode('utf-8'))
                request_url = "{host}{uri}".format(host=self._host, uri=transcoded_request['uri'])
                method = transcoded_request['method']
                raise core_exceptions.format_http_response_error(response, method, request_url, payload)  # type: ignore

            content = await response.read()
            resp = policy_pb2.Policy()
            resp = json_format.Parse(content, resp)
            resp = await self._interceptor.post_set_iam_policy(resp)
            return resp

    @property
    def get_iam_policy(self):
        return self._GetIamPolicy(self._session, self._host, self._interceptor) # type: ignore

    class _GetIamPolicy(_BaseMessagingRestTransport._BaseGetIamPolicy, AsyncMessagingRestStub):
        def __hash__(self):
            return hash("AsyncMessagingRestTransport.GetIamPolicy")

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
            request: iam_policy_pb2.GetIamPolicyRequest, *,
            retry: OptionalRetry=gapic_v1.method.DEFAULT,
            timeout: Optional[float]=None,
            metadata: Sequence[Tuple[str, str]]=(),
            ) -> policy_pb2.Policy:

            r"""Call the get iam policy method over HTTP.

            Args:
                request (iam_policy_pb2.GetIamPolicyRequest):
                    The request object for GetIamPolicy method.
                retry (google.api_core.retry_async.AsyncRetry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, str]]): Strings which should be
                    sent along with the request as metadata.

            Returns:
                policy_pb2.Policy: Response from GetIamPolicy method.
            """

            http_options = _BaseMessagingRestTransport._BaseGetIamPolicy._get_http_options()
            request, metadata = await self._interceptor.pre_get_iam_policy(request, metadata)
            transcoded_request = _BaseMessagingRestTransport._BaseGetIamPolicy._get_transcoded_request(http_options, request)

            # Jsonify the query params
            query_params = _BaseMessagingRestTransport._BaseGetIamPolicy._get_query_params_json(transcoded_request)

            # Send the request
            response = await AsyncMessagingRestTransport._GetIamPolicy._get_response(self._host, metadata, query_params, self._session, timeout, transcoded_request)

            # In case of error, raise the appropriate core_exceptions.GoogleAPICallError exception
            # subclass.
            if response.status_code >= 400:
                content = await response.read()
                payload = json.loads(content.decode('utf-8'))
                request_url = "{host}{uri}".format(host=self._host, uri=transcoded_request['uri'])
                method = transcoded_request['method']
                raise core_exceptions.format_http_response_error(response, method, request_url, payload)  # type: ignore

            content = await response.read()
            resp = policy_pb2.Policy()
            resp = json_format.Parse(content, resp)
            resp = await self._interceptor.post_get_iam_policy(resp)
            return resp

    @property
    def test_iam_permissions(self):
        return self._TestIamPermissions(self._session, self._host, self._interceptor) # type: ignore

    class _TestIamPermissions(_BaseMessagingRestTransport._BaseTestIamPermissions, AsyncMessagingRestStub):
        def __hash__(self):
            return hash("AsyncMessagingRestTransport.TestIamPermissions")

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
            request: iam_policy_pb2.TestIamPermissionsRequest, *,
            retry: OptionalRetry=gapic_v1.method.DEFAULT,
            timeout: Optional[float]=None,
            metadata: Sequence[Tuple[str, str]]=(),
            ) -> iam_policy_pb2.TestIamPermissionsResponse:

            r"""Call the test iam permissions method over HTTP.

            Args:
                request (iam_policy_pb2.TestIamPermissionsRequest):
                    The request object for TestIamPermissions method.
                retry (google.api_core.retry_async.AsyncRetry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, str]]): Strings which should be
                    sent along with the request as metadata.

            Returns:
                iam_policy_pb2.TestIamPermissionsResponse: Response from TestIamPermissions method.
            """

            http_options = _BaseMessagingRestTransport._BaseTestIamPermissions._get_http_options()
            request, metadata = await self._interceptor.pre_test_iam_permissions(request, metadata)
            transcoded_request = _BaseMessagingRestTransport._BaseTestIamPermissions._get_transcoded_request(http_options, request)

            body = _BaseMessagingRestTransport._BaseTestIamPermissions._get_request_body_json(transcoded_request)

            # Jsonify the query params
            query_params = _BaseMessagingRestTransport._BaseTestIamPermissions._get_query_params_json(transcoded_request)

            # Send the request
            response = await AsyncMessagingRestTransport._TestIamPermissions._get_response(self._host, metadata, query_params, self._session, timeout, transcoded_request, body)

            # In case of error, raise the appropriate core_exceptions.GoogleAPICallError exception
            # subclass.
            if response.status_code >= 400:
                content = await response.read()
                payload = json.loads(content.decode('utf-8'))
                request_url = "{host}{uri}".format(host=self._host, uri=transcoded_request['uri'])
                method = transcoded_request['method']
                raise core_exceptions.format_http_response_error(response, method, request_url, payload)  # type: ignore

            content = await response.read()
            resp = iam_policy_pb2.TestIamPermissionsResponse()
            resp = json_format.Parse(content, resp)
            resp = await self._interceptor.post_test_iam_permissions(resp)
            return resp

    @property
    def list_operations(self):
        return self._ListOperations(self._session, self._host, self._interceptor) # type: ignore

    class _ListOperations(_BaseMessagingRestTransport._BaseListOperations, AsyncMessagingRestStub):
        def __hash__(self):
            return hash("AsyncMessagingRestTransport.ListOperations")

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

            http_options = _BaseMessagingRestTransport._BaseListOperations._get_http_options()
            request, metadata = await self._interceptor.pre_list_operations(request, metadata)
            transcoded_request = _BaseMessagingRestTransport._BaseListOperations._get_transcoded_request(http_options, request)

            # Jsonify the query params
            query_params = _BaseMessagingRestTransport._BaseListOperations._get_query_params_json(transcoded_request)

            # Send the request
            response = await AsyncMessagingRestTransport._ListOperations._get_response(self._host, metadata, query_params, self._session, timeout, transcoded_request)

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
    def get_operation(self):
        return self._GetOperation(self._session, self._host, self._interceptor) # type: ignore

    class _GetOperation(_BaseMessagingRestTransport._BaseGetOperation, AsyncMessagingRestStub):
        def __hash__(self):
            return hash("AsyncMessagingRestTransport.GetOperation")

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

            http_options = _BaseMessagingRestTransport._BaseGetOperation._get_http_options()
            request, metadata = await self._interceptor.pre_get_operation(request, metadata)
            transcoded_request = _BaseMessagingRestTransport._BaseGetOperation._get_transcoded_request(http_options, request)

            # Jsonify the query params
            query_params = _BaseMessagingRestTransport._BaseGetOperation._get_query_params_json(transcoded_request)

            # Send the request
            response = await AsyncMessagingRestTransport._GetOperation._get_response(self._host, metadata, query_params, self._session, timeout, transcoded_request)

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
    def delete_operation(self):
        return self._DeleteOperation(self._session, self._host, self._interceptor) # type: ignore

    class _DeleteOperation(_BaseMessagingRestTransport._BaseDeleteOperation, AsyncMessagingRestStub):
        def __hash__(self):
            return hash("AsyncMessagingRestTransport.DeleteOperation")

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

            http_options = _BaseMessagingRestTransport._BaseDeleteOperation._get_http_options()
            request, metadata = await self._interceptor.pre_delete_operation(request, metadata)
            transcoded_request = _BaseMessagingRestTransport._BaseDeleteOperation._get_transcoded_request(http_options, request)

            # Jsonify the query params
            query_params = _BaseMessagingRestTransport._BaseDeleteOperation._get_query_params_json(transcoded_request)

            # Send the request
            response = await AsyncMessagingRestTransport._DeleteOperation._get_response(self._host, metadata, query_params, self._session, timeout, transcoded_request)

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
    def cancel_operation(self):
        return self._CancelOperation(self._session, self._host, self._interceptor) # type: ignore

    class _CancelOperation(_BaseMessagingRestTransport._BaseCancelOperation, AsyncMessagingRestStub):
        def __hash__(self):
            return hash("AsyncMessagingRestTransport.CancelOperation")

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

            http_options = _BaseMessagingRestTransport._BaseCancelOperation._get_http_options()
            request, metadata = await self._interceptor.pre_cancel_operation(request, metadata)
            transcoded_request = _BaseMessagingRestTransport._BaseCancelOperation._get_transcoded_request(http_options, request)

            # Jsonify the query params
            query_params = _BaseMessagingRestTransport._BaseCancelOperation._get_query_params_json(transcoded_request)

            # Send the request
            response = await AsyncMessagingRestTransport._CancelOperation._get_response(self._host, metadata, query_params, self._session, timeout, transcoded_request)

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
    def kind(self) -> str:
        return "rest_asyncio"

    async def close(self):
        await self._session.close()

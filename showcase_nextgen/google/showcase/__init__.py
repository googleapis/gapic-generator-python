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
from google.showcase import gapic_version as package_version

__version__ = package_version.__version__


from google.showcase_v1beta1.services.echo.client import EchoClient
from google.showcase_v1beta1.services.echo.async_client import EchoAsyncClient
from google.showcase_v1beta1.services.identity.client import IdentityClient
from google.showcase_v1beta1.services.identity.async_client import IdentityAsyncClient
from google.showcase_v1beta1.services.messaging.client import MessagingClient
from google.showcase_v1beta1.services.messaging.async_client import MessagingAsyncClient

from google.showcase_v1beta1.types.echo_pb2 import BlockRequest
from google.showcase_v1beta1.types.echo_pb2 import BlockResponse
from google.showcase_v1beta1.types.echo_pb2 import EchoErrorDetailsRequest
from google.showcase_v1beta1.types.echo_pb2 import EchoErrorDetailsResponse
from google.showcase_v1beta1.types.echo_pb2 import EchoRequest
from google.showcase_v1beta1.types.echo_pb2 import EchoResponse
from google.showcase_v1beta1.types.echo_pb2 import ErrorWithMultipleDetails
from google.showcase_v1beta1.types.echo_pb2 import ErrorWithSingleDetail
from google.showcase_v1beta1.types.echo_pb2 import ExpandRequest
from google.showcase_v1beta1.types.echo_pb2 import PagedExpandLegacyMappedResponse
from google.showcase_v1beta1.types.echo_pb2 import PagedExpandLegacyRequest
from google.showcase_v1beta1.types.echo_pb2 import PagedExpandRequest
from google.showcase_v1beta1.types.echo_pb2 import PagedExpandResponse
from google.showcase_v1beta1.types.echo_pb2 import PagedExpandResponseList
from google.showcase_v1beta1.types.echo_pb2 import WaitMetadata
from google.showcase_v1beta1.types.echo_pb2 import WaitRequest
from google.showcase_v1beta1.types.echo_pb2 import WaitResponse
from google.showcase_v1beta1.types.echo_pb2 import Severity
from google.showcase_v1beta1.types.identity_pb2 import CreateUserRequest
from google.showcase_v1beta1.types.identity_pb2 import DeleteUserRequest
from google.showcase_v1beta1.types.identity_pb2 import GetUserRequest
from google.showcase_v1beta1.types.identity_pb2 import ListUsersRequest
from google.showcase_v1beta1.types.identity_pb2 import ListUsersResponse
from google.showcase_v1beta1.types.identity_pb2 import UpdateUserRequest
from google.showcase_v1beta1.types.identity_pb2 import User
from google.showcase_v1beta1.types.messaging_pb2 import Blurb
from google.showcase_v1beta1.types.messaging_pb2 import ConnectRequest
from google.showcase_v1beta1.types.messaging_pb2 import CreateBlurbRequest
from google.showcase_v1beta1.types.messaging_pb2 import CreateRoomRequest
from google.showcase_v1beta1.types.messaging_pb2 import DeleteBlurbRequest
from google.showcase_v1beta1.types.messaging_pb2 import DeleteRoomRequest
from google.showcase_v1beta1.types.messaging_pb2 import GetBlurbRequest
from google.showcase_v1beta1.types.messaging_pb2 import GetRoomRequest
from google.showcase_v1beta1.types.messaging_pb2 import ListBlurbsRequest
from google.showcase_v1beta1.types.messaging_pb2 import ListBlurbsResponse
from google.showcase_v1beta1.types.messaging_pb2 import ListRoomsRequest
from google.showcase_v1beta1.types.messaging_pb2 import ListRoomsResponse
from google.showcase_v1beta1.types.messaging_pb2 import Room
from google.showcase_v1beta1.types.messaging_pb2 import SearchBlurbsMetadata
from google.showcase_v1beta1.types.messaging_pb2 import SearchBlurbsRequest
from google.showcase_v1beta1.types.messaging_pb2 import SearchBlurbsResponse
from google.showcase_v1beta1.types.messaging_pb2 import SendBlurbsResponse
from google.showcase_v1beta1.types.messaging_pb2 import StreamBlurbsRequest
from google.showcase_v1beta1.types.messaging_pb2 import StreamBlurbsResponse
from google.showcase_v1beta1.types.messaging_pb2 import UpdateBlurbRequest
from google.showcase_v1beta1.types.messaging_pb2 import UpdateRoomRequest

__all__ = ('EchoClient',
    'EchoAsyncClient',
    'IdentityClient',
    'IdentityAsyncClient',
    'MessagingClient',
    'MessagingAsyncClient',
    'BlockRequest',
    'BlockResponse',
    'EchoErrorDetailsRequest',
    'EchoErrorDetailsResponse',
    'EchoRequest',
    'EchoResponse',
    'ErrorWithMultipleDetails',
    'ErrorWithSingleDetail',
    'ExpandRequest',
    'PagedExpandLegacyMappedResponse',
    'PagedExpandLegacyRequest',
    'PagedExpandRequest',
    'PagedExpandResponse',
    'PagedExpandResponseList',
    'WaitMetadata',
    'WaitRequest',
    'WaitResponse',
    'Severity',
    'CreateUserRequest',
    'DeleteUserRequest',
    'GetUserRequest',
    'ListUsersRequest',
    'ListUsersResponse',
    'UpdateUserRequest',
    'User',
    'Blurb',
    'ConnectRequest',
    'CreateBlurbRequest',
    'CreateRoomRequest',
    'DeleteBlurbRequest',
    'DeleteRoomRequest',
    'GetBlurbRequest',
    'GetRoomRequest',
    'ListBlurbsRequest',
    'ListBlurbsResponse',
    'ListRoomsRequest',
    'ListRoomsResponse',
    'Room',
    'SearchBlurbsMetadata',
    'SearchBlurbsRequest',
    'SearchBlurbsResponse',
    'SendBlurbsResponse',
    'StreamBlurbsRequest',
    'StreamBlurbsResponse',
    'UpdateBlurbRequest',
    'UpdateRoomRequest',
)

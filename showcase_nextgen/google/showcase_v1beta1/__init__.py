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
from google.showcase_v1beta1 import gapic_version as package_version

__version__ = package_version.__version__


from .services.echo import EchoClient
from .services.echo import EchoAsyncClient
from .services.identity import IdentityClient
from .services.identity import IdentityAsyncClient
from .services.messaging import MessagingClient
from .services.messaging import MessagingAsyncClient

from .types import echo_pb2
from .types.echo_pb2 import BlockRequest
from .types.echo_pb2 import BlockResponse
from .types.echo_pb2 import EchoErrorDetailsRequest
from .types.echo_pb2 import EchoErrorDetailsResponse
from .types.echo_pb2 import EchoRequest
from .types.echo_pb2 import EchoResponse
from .types.echo_pb2 import ErrorWithMultipleDetails
from .types.echo_pb2 import ErrorWithSingleDetail
from .types.echo_pb2 import ExpandRequest
from .types.echo_pb2 import PagedExpandLegacyMappedResponse
from .types.echo_pb2 import PagedExpandLegacyRequest
from .types.echo_pb2 import PagedExpandRequest
from .types.echo_pb2 import PagedExpandResponse
from .types.echo_pb2 import PagedExpandResponseList
from .types.echo_pb2 import WaitMetadata
from .types.echo_pb2 import WaitRequest
from .types.echo_pb2 import WaitResponse
from .types.echo_pb2 import Severity
from .types import identity_pb2
from .types.identity_pb2 import CreateUserRequest
from .types.identity_pb2 import DeleteUserRequest
from .types.identity_pb2 import GetUserRequest
from .types.identity_pb2 import ListUsersRequest
from .types.identity_pb2 import ListUsersResponse
from .types.identity_pb2 import UpdateUserRequest
from .types.identity_pb2 import User
from .types import messaging_pb2
from .types.messaging_pb2 import Blurb
from .types.messaging_pb2 import ConnectRequest
from .types.messaging_pb2 import CreateBlurbRequest
from .types.messaging_pb2 import CreateRoomRequest
from .types.messaging_pb2 import DeleteBlurbRequest
from .types.messaging_pb2 import DeleteRoomRequest
from .types.messaging_pb2 import GetBlurbRequest
from .types.messaging_pb2 import GetRoomRequest
from .types.messaging_pb2 import ListBlurbsRequest
from .types.messaging_pb2 import ListBlurbsResponse
from .types.messaging_pb2 import ListRoomsRequest
from .types.messaging_pb2 import ListRoomsResponse
from .types.messaging_pb2 import Room
from .types.messaging_pb2 import SearchBlurbsMetadata
from .types.messaging_pb2 import SearchBlurbsRequest
from .types.messaging_pb2 import SearchBlurbsResponse
from .types.messaging_pb2 import SendBlurbsResponse
from .types.messaging_pb2 import StreamBlurbsRequest
from .types.messaging_pb2 import StreamBlurbsResponse
from .types.messaging_pb2 import UpdateBlurbRequest
from .types.messaging_pb2 import UpdateRoomRequest

__all__ = (
    'EchoAsyncClient',
    'IdentityAsyncClient',
    'MessagingAsyncClient',
'BlockRequest',
'BlockResponse',
'Blurb',
'ConnectRequest',
'CreateBlurbRequest',
'CreateRoomRequest',
'CreateUserRequest',
'DeleteBlurbRequest',
'DeleteRoomRequest',
'DeleteUserRequest',
'EchoClient',
'EchoErrorDetailsRequest',
'EchoErrorDetailsResponse',
'EchoRequest',
'EchoResponse',
'ErrorWithMultipleDetails',
'ErrorWithSingleDetail',
'ExpandRequest',
'GetBlurbRequest',
'GetRoomRequest',
'GetUserRequest',
'IdentityClient',
'ListBlurbsRequest',
'ListBlurbsResponse',
'ListRoomsRequest',
'ListRoomsResponse',
'ListUsersRequest',
'ListUsersResponse',
'MessagingClient',
'PagedExpandLegacyMappedResponse',
'PagedExpandLegacyRequest',
'PagedExpandRequest',
'PagedExpandResponse',
'PagedExpandResponseList',
'Room',
'SearchBlurbsMetadata',
'SearchBlurbsRequest',
'SearchBlurbsResponse',
'SendBlurbsResponse',
'Severity',
'StreamBlurbsRequest',
'StreamBlurbsResponse',
'UpdateBlurbRequest',
'UpdateRoomRequest',
'UpdateUserRequest',
'User',
'WaitMetadata',
'WaitRequest',
'WaitResponse',
)

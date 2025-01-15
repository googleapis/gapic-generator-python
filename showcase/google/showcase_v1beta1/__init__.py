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

from .types.echo import BlockRequest
from .types.echo import BlockResponse
from .types.echo import EchoErrorDetailsRequest
from .types.echo import EchoErrorDetailsResponse
from .types.echo import EchoRequest
from .types.echo import EchoResponse
from .types.echo import ErrorWithMultipleDetails
from .types.echo import ErrorWithSingleDetail
from .types.echo import ExpandRequest
from .types.echo import PagedExpandLegacyMappedResponse
from .types.echo import PagedExpandLegacyRequest
from .types.echo import PagedExpandRequest
from .types.echo import PagedExpandResponse
from .types.echo import PagedExpandResponseList
from .types.echo import WaitMetadata
from .types.echo import WaitRequest
from .types.echo import WaitResponse
from .types.echo import Severity
from .types.identity import CreateUserRequest
from .types.identity import DeleteUserRequest
from .types.identity import GetUserRequest
from .types.identity import ListUsersRequest
from .types.identity import ListUsersResponse
from .types.identity import UpdateUserRequest
from .types.identity import User
from .types.messaging import Blurb
from .types.messaging import ConnectRequest
from .types.messaging import CreateBlurbRequest
from .types.messaging import CreateRoomRequest
from .types.messaging import DeleteBlurbRequest
from .types.messaging import DeleteRoomRequest
from .types.messaging import GetBlurbRequest
from .types.messaging import GetRoomRequest
from .types.messaging import ListBlurbsRequest
from .types.messaging import ListBlurbsResponse
from .types.messaging import ListRoomsRequest
from .types.messaging import ListRoomsResponse
from .types.messaging import Room
from .types.messaging import SearchBlurbsMetadata
from .types.messaging import SearchBlurbsRequest
from .types.messaging import SearchBlurbsResponse
from .types.messaging import SendBlurbsResponse
from .types.messaging import StreamBlurbsRequest
from .types.messaging import StreamBlurbsResponse
from .types.messaging import UpdateBlurbRequest
from .types.messaging import UpdateRoomRequest

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

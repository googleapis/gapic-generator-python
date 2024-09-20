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


from .services.compliance import ComplianceClient
from .services.compliance import ComplianceAsyncClient
from .services.echo import EchoClient
from .services.echo import EchoAsyncClient
from .services.identity import IdentityClient
from .services.identity import IdentityAsyncClient
from .services.messaging import MessagingClient
from .services.messaging import MessagingAsyncClient
from .services.sequence_service import SequenceServiceClient
from .services.sequence_service import SequenceServiceAsyncClient
from .services.testing import TestingClient
from .services.testing import TestingAsyncClient

from .types.compliance import ComplianceData
from .types.compliance import ComplianceDataChild
from .types.compliance import ComplianceDataGrandchild
from .types.compliance import ComplianceGroup
from .types.compliance import ComplianceSuite
from .types.compliance import EnumRequest
from .types.compliance import EnumResponse
from .types.compliance import RepeatRequest
from .types.compliance import RepeatResponse
from .types.compliance import Continent
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
from .types.sequence import AttemptSequenceRequest
from .types.sequence import AttemptStreamingSequenceRequest
from .types.sequence import AttemptStreamingSequenceResponse
from .types.sequence import CreateSequenceRequest
from .types.sequence import CreateStreamingSequenceRequest
from .types.sequence import GetSequenceReportRequest
from .types.sequence import GetStreamingSequenceReportRequest
from .types.sequence import Sequence
from .types.sequence import SequenceReport
from .types.sequence import StreamingSequence
from .types.sequence import StreamingSequenceReport
from .types.testing import CreateSessionRequest
from .types.testing import DeleteSessionRequest
from .types.testing import DeleteTestRequest
from .types.testing import GetSessionRequest
from .types.testing import Issue
from .types.testing import ListSessionsRequest
from .types.testing import ListSessionsResponse
from .types.testing import ListTestsRequest
from .types.testing import ListTestsResponse
from .types.testing import ReportSessionRequest
from .types.testing import ReportSessionResponse
from .types.testing import Session
from .types.testing import Test
from .types.testing import TestRun
from .types.testing import VerifyTestRequest
from .types.testing import VerifyTestResponse

__all__ = (
    'ComplianceAsyncClient',
    'EchoAsyncClient',
    'IdentityAsyncClient',
    'MessagingAsyncClient',
    'SequenceServiceAsyncClient',
    'TestingAsyncClient',
'AttemptSequenceRequest',
'AttemptStreamingSequenceRequest',
'AttemptStreamingSequenceResponse',
'BlockRequest',
'BlockResponse',
'Blurb',
'ComplianceClient',
'ComplianceData',
'ComplianceDataChild',
'ComplianceDataGrandchild',
'ComplianceGroup',
'ComplianceSuite',
'ConnectRequest',
'Continent',
'CreateBlurbRequest',
'CreateRoomRequest',
'CreateSequenceRequest',
'CreateSessionRequest',
'CreateStreamingSequenceRequest',
'CreateUserRequest',
'DeleteBlurbRequest',
'DeleteRoomRequest',
'DeleteSessionRequest',
'DeleteTestRequest',
'DeleteUserRequest',
'EchoClient',
'EchoErrorDetailsRequest',
'EchoErrorDetailsResponse',
'EchoRequest',
'EchoResponse',
'EnumRequest',
'EnumResponse',
'ErrorWithMultipleDetails',
'ErrorWithSingleDetail',
'ExpandRequest',
'GetBlurbRequest',
'GetRoomRequest',
'GetSequenceReportRequest',
'GetSessionRequest',
'GetStreamingSequenceReportRequest',
'GetUserRequest',
'IdentityClient',
'Issue',
'ListBlurbsRequest',
'ListBlurbsResponse',
'ListRoomsRequest',
'ListRoomsResponse',
'ListSessionsRequest',
'ListSessionsResponse',
'ListTestsRequest',
'ListTestsResponse',
'ListUsersRequest',
'ListUsersResponse',
'MessagingClient',
'PagedExpandLegacyMappedResponse',
'PagedExpandLegacyRequest',
'PagedExpandRequest',
'PagedExpandResponse',
'PagedExpandResponseList',
'RepeatRequest',
'RepeatResponse',
'ReportSessionRequest',
'ReportSessionResponse',
'Room',
'SearchBlurbsMetadata',
'SearchBlurbsRequest',
'SearchBlurbsResponse',
'SendBlurbsResponse',
'Sequence',
'SequenceReport',
'SequenceServiceClient',
'Session',
'Severity',
'StreamBlurbsRequest',
'StreamBlurbsResponse',
'StreamingSequence',
'StreamingSequenceReport',
'Test',
'TestRun',
'TestingClient',
'UpdateBlurbRequest',
'UpdateRoomRequest',
'UpdateUserRequest',
'User',
'VerifyTestRequest',
'VerifyTestResponse',
'WaitMetadata',
'WaitRequest',
'WaitResponse',
)

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
import proto  # type: ignore

from google.api import monitored_resource_pb2  # type: ignore
from google.cloud.logging_v2.types import log_entry
from google.protobuf import duration_pb2  # type: ignore
from google.rpc import status_pb2  # type: ignore


__protobuf__ = proto.module(
    package='google.logging.v2',
    manifest={
        'DeleteLogRequest',
        'WriteLogEntriesRequest',
        'WriteLogEntriesResponse',
        'WriteLogEntriesPartialErrors',
        'ListLogEntriesRequest',
        'ListLogEntriesResponse',
        'ListMonitoredResourceDescriptorsRequest',
        'ListMonitoredResourceDescriptorsResponse',
        'ListLogsRequest',
        'ListLogsResponse',
        'TailLogEntriesRequest',
        'TailLogEntriesResponse',
    },
)

from .requests import (
        DeleteLogRequest,
        WriteLogEntriesRequest,
        ListLogEntriesRequest,
        ListMonitoredResourceDescriptorsRequest,
        ListLogsRequest,
        TailLogEntriesRequest,
)

from .responses import (
        WriteLogEntriesResponse,
        ListLogEntriesResponse,
        ListMonitoredResourceDescriptorsResponse,
        ListLogsResponse,
        TailLogEntriesResponse,
)


class WriteLogEntriesPartialErrors(proto.Message):
    r"""Error details for WriteLogEntries with partial success.

    Attributes:
        log_entry_errors (Mapping[int, google.rpc.status_pb2.Status]):
            When ``WriteLogEntriesRequest.partial_success`` is true,
            records the error status for entries that were not written
            due to a permanent error, keyed by the entry's zero-based
            index in ``WriteLogEntriesRequest.entries``.

            Failed requests for which no entries are written will not
            include per-entry errors.
    """

    log_entry_errors = proto.MapField(
        proto.INT32,
        proto.MESSAGE,
        number=1,
        message=status_pb2.Status,
    )


__all__ = tuple(sorted(__protobuf__.manifest))

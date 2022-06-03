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
        'WriteLogEntriesResponse',
        'ListLogEntriesResponse',
        'ListMonitoredResourceDescriptorsResponse',
        'ListLogsResponse',
        'TailLogEntriesResponse',
    },
)

__manifest__ = (
        'WriteLogEntriesResponse',
        'ListLogEntriesResponse',
        'ListMonitoredResourceDescriptorsResponse',
        'ListLogsResponse',
        'TailLogEntriesResponse',
)


class WriteLogEntriesResponse(proto.Message):
    r"""Result returned from WriteLogEntries.
    """
    __module__ = __module__.rsplit('.', maxsplit=1)[0]  # type: ignore


class ListLogEntriesResponse(proto.Message):
    r"""Result returned from ``ListLogEntries``.

    Attributes:
        entries (Sequence[google.cloud.logging_v2.types.LogEntry]):
            A list of log entries. If ``entries`` is empty,
            ``nextPageToken`` may still be returned, indicating that
            more entries may exist. See ``nextPageToken`` for more
            information.
        next_page_token (str):
            If there might be more results than those appearing in this
            response, then ``nextPageToken`` is included. To get the
            next set of results, call this method again using the value
            of ``nextPageToken`` as ``pageToken``.

            If a value for ``next_page_token`` appears and the
            ``entries`` field is empty, it means that the search found
            no log entries so far but it did not have time to search all
            the possible log entries. Retry the method with this value
            for ``page_token`` to continue the search. Alternatively,
            consider speeding up the search by changing your filter to
            specify a single log name or resource type, or to narrow the
            time range of the search.
    """
    __module__ = __module__.rsplit('.', maxsplit=1)[0]  # type: ignore

    @property
    def raw_page(self):
        return self

    entries = proto.RepeatedField(
        proto.MESSAGE,
        number=1,
        message=log_entry.LogEntry,
    )
    next_page_token = proto.Field(
        proto.STRING,
        number=2,
    )


class ListMonitoredResourceDescriptorsResponse(proto.Message):
    r"""Result returned from ListMonitoredResourceDescriptors.

    Attributes:
        resource_descriptors (Sequence[google.api.monitored_resource_pb2.MonitoredResourceDescriptor]):
            A list of resource descriptors.
        next_page_token (str):
            If there might be more results than those appearing in this
            response, then ``nextPageToken`` is included. To get the
            next set of results, call this method again using the value
            of ``nextPageToken`` as ``pageToken``.
    """
    __module__ = __module__.rsplit('.', maxsplit=1)[0]  # type: ignore

    @property
    def raw_page(self):
        return self

    resource_descriptors = proto.RepeatedField(
        proto.MESSAGE,
        number=1,
        message=monitored_resource_pb2.MonitoredResourceDescriptor,
    )
    next_page_token = proto.Field(
        proto.STRING,
        number=2,
    )


class ListLogsResponse(proto.Message):
    r"""Result returned from ListLogs.

    Attributes:
        log_names (Sequence[str]):
            A list of log names. For example,
            ``"projects/my-project/logs/syslog"`` or
            ``"organizations/123/logs/cloudresourcemanager.googleapis.com%2Factivity"``.
        next_page_token (str):
            If there might be more results than those appearing in this
            response, then ``nextPageToken`` is included. To get the
            next set of results, call this method again using the value
            of ``nextPageToken`` as ``pageToken``.
    """
    __module__ = __module__.rsplit('.', maxsplit=1)[0]  # type: ignore

    @property
    def raw_page(self):
        return self

    log_names = proto.RepeatedField(
        proto.STRING,
        number=3,
    )
    next_page_token = proto.Field(
        proto.STRING,
        number=2,
    )


class TailLogEntriesResponse(proto.Message):
    r"""Result returned from ``TailLogEntries``.

    Attributes:
        entries (Sequence[google.cloud.logging_v2.types.LogEntry]):
            A list of log entries. Each response in the stream will
            order entries with increasing values of
            ``LogEntry.timestamp``. Ordering is not guaranteed between
            separate responses.
        suppression_info (Sequence[google.cloud.logging_v2.types.TailLogEntriesResponse.SuppressionInfo]):
            If entries that otherwise would have been
            included in the session were not sent back to
            the client, counts of relevant entries omitted
            from the session with the reason that they were
            not included. There will be at most one of each
            reason per response. The counts represent the
            number of suppressed entries since the last
            streamed response.
    """
    __module__ = __module__.rsplit('.', maxsplit=1)[0]  # type: ignore

    class SuppressionInfo(proto.Message):
        r"""Information about entries that were omitted from the session.

        Attributes:
            reason (google.cloud.logging_v2.types.TailLogEntriesResponse.SuppressionInfo.Reason):
                The reason that entries were omitted from the
                session.
            suppressed_count (int):
                A lower bound on the count of entries omitted due to
                ``reason``.
        """
        __module__ = __module__.rsplit('.', maxsplit=1)[0]  # type: ignore
        class Reason(proto.Enum):
            r"""An indicator of why entries were omitted."""
            __module__ = __module__.rsplit('.', maxsplit=1)[0]  # type: ignore
            REASON_UNSPECIFIED = 0
            RATE_LIMIT = 1
            NOT_CONSUMED = 2

        reason = proto.Field(
            proto.ENUM,
            number=1,
            enum='TailLogEntriesResponse.SuppressionInfo.Reason',
        )
        suppressed_count = proto.Field(
            proto.INT32,
            number=2,
        )

    entries = proto.RepeatedField(
        proto.MESSAGE,
        number=1,
        message=log_entry.LogEntry,
    )
    suppression_info = proto.RepeatedField(
        proto.MESSAGE,
        number=2,
        message=SuppressionInfo,
    )


__all__ = tuple(sorted(__manifest__))

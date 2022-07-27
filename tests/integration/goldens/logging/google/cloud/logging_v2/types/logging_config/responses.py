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

from google.protobuf import field_mask_pb2  # type: ignore
from google.protobuf import timestamp_pb2  # type: ignore

__manifest__ = (
        'ListBucketsResponse',
        'ListViewsResponse',
        'ListSinksResponse',
        'ListExclusionsResponse',
)


class ListBucketsResponse(proto.Message):
    r"""The response from ListBuckets.

    Attributes:
        buckets (Sequence[google.cloud.logging_v2.types.LogBucket]):
            A list of buckets.
        next_page_token (str):
            If there might be more results than appear in this response,
            then ``nextPageToken`` is included. To get the next set of
            results, call the same method again using the value of
            ``nextPageToken`` as ``pageToken``.
    """
    __module__ = __module__.rsplit('.', maxsplit=1)[0]  # type: ignore

    @property
    def raw_page(self):
        return self

    buckets = proto.RepeatedField(
        proto.MESSAGE,
        number=1,
        message='LogBucket',
    )
    next_page_token = proto.Field(
        proto.STRING,
        number=2,
    )


class ListViewsResponse(proto.Message):
    r"""The response from ListViews.

    Attributes:
        views (Sequence[google.cloud.logging_v2.types.LogView]):
            A list of views.
        next_page_token (str):
            If there might be more results than appear in this response,
            then ``nextPageToken`` is included. To get the next set of
            results, call the same method again using the value of
            ``nextPageToken`` as ``pageToken``.
    """
    __module__ = __module__.rsplit('.', maxsplit=1)[0]  # type: ignore

    @property
    def raw_page(self):
        return self

    views = proto.RepeatedField(
        proto.MESSAGE,
        number=1,
        message='LogView',
    )
    next_page_token = proto.Field(
        proto.STRING,
        number=2,
    )


class ListSinksResponse(proto.Message):
    r"""Result returned from ``ListSinks``.

    Attributes:
        sinks (Sequence[google.cloud.logging_v2.types.LogSink]):
            A list of sinks.
        next_page_token (str):
            If there might be more results than appear in this response,
            then ``nextPageToken`` is included. To get the next set of
            results, call the same method again using the value of
            ``nextPageToken`` as ``pageToken``.
    """
    __module__ = __module__.rsplit('.', maxsplit=1)[0]  # type: ignore

    @property
    def raw_page(self):
        return self

    sinks = proto.RepeatedField(
        proto.MESSAGE,
        number=1,
        message='LogSink',
    )
    next_page_token = proto.Field(
        proto.STRING,
        number=2,
    )


class ListExclusionsResponse(proto.Message):
    r"""Result returned from ``ListExclusions``.

    Attributes:
        exclusions (Sequence[google.cloud.logging_v2.types.LogExclusion]):
            A list of exclusions.
        next_page_token (str):
            If there might be more results than appear in this response,
            then ``nextPageToken`` is included. To get the next set of
            results, call the same method again using the value of
            ``nextPageToken`` as ``pageToken``.
    """
    __module__ = __module__.rsplit('.', maxsplit=1)[0]  # type: ignore

    @property
    def raw_page(self):
        return self

    exclusions = proto.RepeatedField(
        proto.MESSAGE,
        number=1,
        message='LogExclusion',
    )
    next_page_token = proto.Field(
        proto.STRING,
        number=2,
    )


__all__ = tuple(sorted(__manifest__))

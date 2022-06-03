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

from google.api import distribution_pb2  # type: ignore
from google.api import metric_pb2  # type: ignore
from google.protobuf import timestamp_pb2  # type: ignore

__manifest__ = (
        'ListLogMetricsResponse',
)


class ListLogMetricsResponse(proto.Message):
    r"""Result returned from ListLogMetrics.

    Attributes:
        metrics (Sequence[google.cloud.logging_v2.types.LogMetric]):
            A list of logs-based metrics.
        next_page_token (str):
            If there might be more results than appear in this response,
            then ``nextPageToken`` is included. To get the next set of
            results, call this method again using the value of
            ``nextPageToken`` as ``pageToken``.
    """
    __module__ = __module__.rsplit('.', maxsplit=1)[0]  # type: ignore

    @property
    def raw_page(self):
        return self

    metrics = proto.RepeatedField(
        proto.MESSAGE,
        number=1,
        message='LogMetric',
    )
    next_page_token = proto.Field(
        proto.STRING,
        number=2,
    )


__all__ = tuple(sorted(__manifest__))

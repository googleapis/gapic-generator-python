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
        'ListLogMetricsRequest',
        'GetLogMetricRequest',
        'CreateLogMetricRequest',
        'UpdateLogMetricRequest',
        'DeleteLogMetricRequest',
)


class ListLogMetricsRequest(proto.Message):
    r"""The parameters to ListLogMetrics.

    Attributes:
        parent (str):
            Required. The name of the project containing the metrics:

            ::

                "projects/[PROJECT_ID]".
        page_token (str):
            Optional. If present, then retrieve the next batch of
            results from the preceding call to this method.
            ``pageToken`` must be the value of ``nextPageToken`` from
            the previous response. The values of other method parameters
            should be identical to those in the previous call.
        page_size (int):
            Optional. The maximum number of results to return from this
            request. Non-positive values are ignored. The presence of
            ``nextPageToken`` in the response indicates that more
            results might be available.
    """
    __module__ = __module__.rsplit('.', maxsplit=1)[0]  # type: ignore

    parent = proto.Field(
        proto.STRING,
        number=1,
    )
    page_token = proto.Field(
        proto.STRING,
        number=2,
    )
    page_size = proto.Field(
        proto.INT32,
        number=3,
    )


class GetLogMetricRequest(proto.Message):
    r"""The parameters to GetLogMetric.

    Attributes:
        metric_name (str):
            Required. The resource name of the desired metric:

            ::

                "projects/[PROJECT_ID]/metrics/[METRIC_ID]".
    """
    __module__ = __module__.rsplit('.', maxsplit=1)[0]  # type: ignore

    metric_name = proto.Field(
        proto.STRING,
        number=1,
    )


class CreateLogMetricRequest(proto.Message):
    r"""The parameters to CreateLogMetric.

    Attributes:
        parent (str):
            Required. The resource name of the project in which to
            create the metric:

            ::

                "projects/[PROJECT_ID]"

            The new metric must be provided in the request.
        metric (google.cloud.logging_v2.types.LogMetric):
            Required. The new logs-based metric, which
            must not have an identifier that already exists.
    """
    __module__ = __module__.rsplit('.', maxsplit=1)[0]  # type: ignore

    parent = proto.Field(
        proto.STRING,
        number=1,
    )
    metric = proto.Field(
        proto.MESSAGE,
        number=2,
        message='LogMetric',
    )


class UpdateLogMetricRequest(proto.Message):
    r"""The parameters to UpdateLogMetric.

    Attributes:
        metric_name (str):
            Required. The resource name of the metric to update:

            ::

                "projects/[PROJECT_ID]/metrics/[METRIC_ID]"

            The updated metric must be provided in the request and it's
            ``name`` field must be the same as ``[METRIC_ID]`` If the
            metric does not exist in ``[PROJECT_ID]``, then a new metric
            is created.
        metric (google.cloud.logging_v2.types.LogMetric):
            Required. The updated metric.
    """
    __module__ = __module__.rsplit('.', maxsplit=1)[0]  # type: ignore

    metric_name = proto.Field(
        proto.STRING,
        number=1,
    )
    metric = proto.Field(
        proto.MESSAGE,
        number=2,
        message='LogMetric',
    )


class DeleteLogMetricRequest(proto.Message):
    r"""The parameters to DeleteLogMetric.

    Attributes:
        metric_name (str):
            Required. The resource name of the metric to delete:

            ::

                "projects/[PROJECT_ID]/metrics/[METRIC_ID]".
    """
    __module__ = __module__.rsplit('.', maxsplit=1)[0]  # type: ignore

    metric_name = proto.Field(
        proto.STRING,
        number=1,
    )


__all__ = tuple(sorted(__manifest__))

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
from __future__ import annotations

from typing import MutableMapping, MutableSequence

import proto  # type: ignore

from google.protobuf import duration_pb2  # type: ignore
from google.protobuf import timestamp_pb2  # type: ignore
from google.rpc import status_pb2  # type: ignore


__protobuf__ = proto.module(
    package='google.showcase.v1beta1',
    manifest={
        'Sequence',
        'StreamingSequence',
        'StreamingSequenceReport',
        'SequenceReport',
        'CreateSequenceRequest',
        'CreateStreamingSequenceRequest',
        'AttemptSequenceRequest',
        'AttemptStreamingSequenceRequest',
        'AttemptStreamingSequenceResponse',
        'GetSequenceReportRequest',
        'GetStreamingSequenceReportRequest',
    },
)


class Sequence(proto.Message):
    r"""

    Attributes:
        name (str):

        responses (MutableSequence[google.showcase_v1beta1.types.Sequence.Response]):
            Sequence of responses to return in order for
            each attempt. If empty, the default response is
            an immediate OK.
    """

    class Response(proto.Message):
        r"""A server response to an RPC Attempt in a sequence.

        Attributes:
            status (google.rpc.status_pb2.Status):
                The status to return for an individual
                attempt.
            delay (google.protobuf.duration_pb2.Duration):
                The amount of time to delay sending the
                response.
        """

        status: status_pb2.Status = proto.Field(
            proto.MESSAGE,
            number=1,
            message=status_pb2.Status,
        )
        delay: duration_pb2.Duration = proto.Field(
            proto.MESSAGE,
            number=2,
            message=duration_pb2.Duration,
        )

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )
    responses: MutableSequence[Response] = proto.RepeatedField(
        proto.MESSAGE,
        number=2,
        message=Response,
    )


class StreamingSequence(proto.Message):
    r"""

    Attributes:
        name (str):

        content (str):
            The Content that the stream will send
        responses (MutableSequence[google.showcase_v1beta1.types.StreamingSequence.Response]):
            Sequence of responses to return in order for
            each attempt. If empty, the default response is
            an immediate OK.
    """

    class Response(proto.Message):
        r"""A server response to an RPC Attempt in a sequence.

        Attributes:
            status (google.rpc.status_pb2.Status):
                The status to return for an individual
                attempt.
            delay (google.protobuf.duration_pb2.Duration):
                The amount of time to delay sending the
                response.
            response_index (int):
                The index that the status should be sent
        """

        status: status_pb2.Status = proto.Field(
            proto.MESSAGE,
            number=1,
            message=status_pb2.Status,
        )
        delay: duration_pb2.Duration = proto.Field(
            proto.MESSAGE,
            number=2,
            message=duration_pb2.Duration,
        )
        response_index: int = proto.Field(
            proto.INT32,
            number=3,
        )

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )
    content: str = proto.Field(
        proto.STRING,
        number=2,
    )
    responses: MutableSequence[Response] = proto.RepeatedField(
        proto.MESSAGE,
        number=3,
        message=Response,
    )


class StreamingSequenceReport(proto.Message):
    r"""

    Attributes:
        name (str):

        attempts (MutableSequence[google.showcase_v1beta1.types.StreamingSequenceReport.Attempt]):
            The set of RPC attempts received by the
            server for a Sequence.
    """

    class Attempt(proto.Message):
        r"""Contains metrics on individual RPC Attempts in a sequence.

        Attributes:
            attempt_number (int):
                The attempt number - starting at 0.
            attempt_deadline (google.protobuf.timestamp_pb2.Timestamp):
                The deadline dictated by the attempt to the
                server.
            response_time (google.protobuf.timestamp_pb2.Timestamp):
                The time that the server responded to the RPC attempt. Used
                for calculating attempt_delay.
            attempt_delay (google.protobuf.duration_pb2.Duration):
                The server perceived delay between sending
                the last response and receiving this attempt.
                Used for validating attempt delay backoff.
            status (google.rpc.status_pb2.Status):
                The status returned to the attempt.
        """

        attempt_number: int = proto.Field(
            proto.INT32,
            number=1,
        )
        attempt_deadline: timestamp_pb2.Timestamp = proto.Field(
            proto.MESSAGE,
            number=2,
            message=timestamp_pb2.Timestamp,
        )
        response_time: timestamp_pb2.Timestamp = proto.Field(
            proto.MESSAGE,
            number=3,
            message=timestamp_pb2.Timestamp,
        )
        attempt_delay: duration_pb2.Duration = proto.Field(
            proto.MESSAGE,
            number=4,
            message=duration_pb2.Duration,
        )
        status: status_pb2.Status = proto.Field(
            proto.MESSAGE,
            number=5,
            message=status_pb2.Status,
        )

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )
    attempts: MutableSequence[Attempt] = proto.RepeatedField(
        proto.MESSAGE,
        number=2,
        message=Attempt,
    )


class SequenceReport(proto.Message):
    r"""

    Attributes:
        name (str):

        attempts (MutableSequence[google.showcase_v1beta1.types.SequenceReport.Attempt]):
            The set of RPC attempts received by the
            server for a Sequence.
    """

    class Attempt(proto.Message):
        r"""Contains metrics on individual RPC Attempts in a sequence.

        Attributes:
            attempt_number (int):
                The attempt number - starting at 0.
            attempt_deadline (google.protobuf.timestamp_pb2.Timestamp):
                The deadline dictated by the attempt to the
                server.
            response_time (google.protobuf.timestamp_pb2.Timestamp):
                The time that the server responded to the RPC attempt. Used
                for calculating attempt_delay.
            attempt_delay (google.protobuf.duration_pb2.Duration):
                The server perceived delay between sending
                the last response and receiving this attempt.
                Used for validating attempt delay backoff.
            status (google.rpc.status_pb2.Status):
                The status returned to the attempt.
        """

        attempt_number: int = proto.Field(
            proto.INT32,
            number=1,
        )
        attempt_deadline: timestamp_pb2.Timestamp = proto.Field(
            proto.MESSAGE,
            number=2,
            message=timestamp_pb2.Timestamp,
        )
        response_time: timestamp_pb2.Timestamp = proto.Field(
            proto.MESSAGE,
            number=3,
            message=timestamp_pb2.Timestamp,
        )
        attempt_delay: duration_pb2.Duration = proto.Field(
            proto.MESSAGE,
            number=4,
            message=duration_pb2.Duration,
        )
        status: status_pb2.Status = proto.Field(
            proto.MESSAGE,
            number=5,
            message=status_pb2.Status,
        )

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )
    attempts: MutableSequence[Attempt] = proto.RepeatedField(
        proto.MESSAGE,
        number=2,
        message=Attempt,
    )


class CreateSequenceRequest(proto.Message):
    r"""

    Attributes:
        sequence (google.showcase_v1beta1.types.Sequence):

    """

    sequence: 'Sequence' = proto.Field(
        proto.MESSAGE,
        number=1,
        message='Sequence',
    )


class CreateStreamingSequenceRequest(proto.Message):
    r"""

    Attributes:
        streaming_sequence (google.showcase_v1beta1.types.StreamingSequence):

    """

    streaming_sequence: 'StreamingSequence' = proto.Field(
        proto.MESSAGE,
        number=1,
        message='StreamingSequence',
    )


class AttemptSequenceRequest(proto.Message):
    r"""

    Attributes:
        name (str):

    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )


class AttemptStreamingSequenceRequest(proto.Message):
    r"""

    Attributes:
        name (str):

        last_fail_index (int):
            used to send the index of the last failed
            message in the string "content" of an
            AttemptStreamingSequenceResponse needed for
            stream resumption logic testing
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )
    last_fail_index: int = proto.Field(
        proto.INT32,
        number=2,
    )


class AttemptStreamingSequenceResponse(proto.Message):
    r"""The response message for the Echo methods.

    Attributes:
        content (str):
            The content specified in the request.
    """

    content: str = proto.Field(
        proto.STRING,
        number=1,
    )


class GetSequenceReportRequest(proto.Message):
    r"""

    Attributes:
        name (str):

    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )


class GetStreamingSequenceReportRequest(proto.Message):
    r"""

    Attributes:
        name (str):

    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )


__all__ = tuple(sorted(__protobuf__.manifest))

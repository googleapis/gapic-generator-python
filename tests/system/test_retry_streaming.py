# Copyright 2019 Google LLC
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     https://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import pytest
from unittest import mock
from google.rpc.status_pb2 import Status
from datetime import timedelta
from google.api_core import retry as retries
from google.api_core import exceptions as core_exceptions


def _code_from_exc(exc):
    """
    return the grpc code from an exception
    """
    return exc.grpc_status_code.value[0]


def test_streaming_retry_success(sequence):
    """
    Test a stream with a sigle success response
    """
    retry = retries.StreamingRetry(predicate=retries.if_exception_type())
    content = ["hello", "world"]
    seq = sequence.create_streaming_sequence(
        streaming_sequence={
            "name": __name__,
            "content": " ".join(content),
            # single response with entire stream content
            "responses": [{"status": Status(code=0), "response_index": len(content)}],
        }
    )
    it = sequence.attempt_streaming_sequence(name=seq.name, retry=retry)
    results = [pb.content for pb in it]
    assert results == content
    # verify streaming report
    report = sequence.get_streaming_sequence_report(
        name=f"{seq.name}/streamingSequenceReport"
    )
    assert len(report.attempts) == 1
    assert report.attempts[0].status == Status(code=0)


def test_streaming_non_retryable_error(sequence):
    """
    Test a retryable stream failing with non-retryable error
    """
    retry = retries.StreamingRetry(predicate=retries.if_exception_type())
    content = ["hello", "world"]
    error = Status(
        code=_code_from_exc(core_exceptions.ServiceUnavailable),
        message="expected error",
    )
    seq = sequence.create_streaming_sequence(
        streaming_sequence={
            "name": __name__,
            "content": " ".join(content),
            "responses": [{"status": error, "response_index": 0}],
        }
    )
    with pytest.raises(core_exceptions.ServiceUnavailable):
        it = sequence.attempt_streaming_sequence(name=seq.name, retry=retry)
        next(it)
    # verify streaming report
    report = sequence.get_streaming_sequence_report(
        name=f"{seq.name}/streamingSequenceReport"
    )
    assert len(report.attempts) == 1
    assert report.attempts[0].status == error


def test_streaming_transient_retryable(sequence):
    """
    Server returns a retryable error a number of times before success.
    Retryable errors should not be presented to the end user.
    """
    retry = retries.StreamingRetry(
        predicate=retries.if_exception_type(core_exceptions.ServiceUnavailable),
        initial=0,
        maximum=0,
        timeout=1,
    )
    content = ["hello", "world"]
    error = Status(
        code=_code_from_exc(core_exceptions.ServiceUnavailable),
        message="transient error",
    )
    responses = [{"status": error, "response_index": 0} for _ in range(3)] + [
        {"status": Status(code=0), "response_index": len(content)}
    ]
    seq = sequence.create_streaming_sequence(
        streaming_sequence={
            "name": __name__,
            "content": " ".join(content),
            "responses": responses,
        }
    )
    it = sequence.attempt_streaming_sequence(name=seq.name, retry=retry)
    results = [pb.content for pb in it]
    assert results == content
    # verify streaming report
    report = sequence.get_streaming_sequence_report(
        name=f"{seq.name}/streamingSequenceReport"
    )
    assert len(report.attempts) == 4
    assert report.attempts[0].status == error
    assert report.attempts[1].status == error
    assert report.attempts[2].status == error
    assert report.attempts[3].status == Status(code=0)


def test_streaming_transient_retryable_partial_data(sequence):
    """
    Server stream yields some data before failing with a retryable error a number of times before success.
    Wrapped stream should contain data from all attempts
    """
    from google.protobuf.duration_pb2 import Duration

    retry = retries.StreamingRetry(
        predicate=retries.if_exception_type(core_exceptions.ServiceUnavailable),
        initial=0,
        maximum=0,
    )
    content = ["hello", ",", "world"]
    error = Status(
        code=_code_from_exc(core_exceptions.ServiceUnavailable),
        message="transient error",
    )
    transient_error_list = [
        {"status": error, "response_index": 3, "delay": Duration(seconds=30)}
    ] * 3

    responses = transient_error_list + [
        {"status": Status(code=0), "response_index": len(content)}
    ]
    seq = sequence.create_streaming_sequence(
        streaming_sequence={
            "name": __name__,
            "content": " ".join(content),
            "responses": responses,
        }
    )
    it = sequence.attempt_streaming_sequence(name=seq.name, retry=retry)
    results = [pb.content for pb in it]
    assert results == ["hello", "hello", "hello", "hello", "world"]
    # verify streaming report
    report = sequence.get_streaming_sequence_report(
        name=f"{seq.name}/streamingSequenceReport"
    )
    assert len(report.attempts) == 4
    assert report.attempts[0].status == error
    assert report.attempts[1].status == error
    assert report.attempts[2].status == error
    assert report.attempts[3].status == Status(code=0)


def test_streaming_retryable_eventual_timeout(sequence):
    """
    Server returns a retryable error a number of times before reaching timeout.
    Should raise a retry error.
    """
    retry = retries.StreamingRetry(
        predicate=retries.if_exception_type(core_exceptions.ServiceUnavailable),
        initial=0,
        maximum=0,
        timeout=0.35,
    )
    content = ["hello", "world"]
    error = Status(
        code=_code_from_exc(core_exceptions.ServiceUnavailable),
        message="transient error",
    )
    transient_error_list = [
        {"status": error, "response_index": 1, "delay": timedelta(seconds=0.15)}
    ] * 10
    responses = transient_error_list + [
        {"status": Status(code=0), "response_index": len(content)}
    ]
    seq = sequence.create_streaming_sequence(
        streaming_sequence={
            "name": __name__,
            "content": " ".join(content),
            "responses": responses,
        }
    )
    with pytest.raises(core_exceptions.RetryError) as exc_info:
        it = sequence.attempt_streaming_sequence(name=seq.name, retry=retry)
        [pb.content for pb in it]
    cause = exc_info.value.__cause__
    assert isinstance(cause, core_exceptions.ServiceUnavailable)
    # verify streaming report
    report = sequence.get_streaming_sequence_report(
        name=f"{seq.name}/streamingSequenceReport"
    )
    assert len(report.attempts) == 3
    assert report.attempts[0].status == error
    assert report.attempts[1].status == error
    assert report.attempts[2].status == error


def test_streaming_retry_on_error(sequence):
    """
    on_error should be called for all retryable errors as they are encountered
    """
    encountered_excs = []

    def on_error(exc):
        encountered_excs.append(exc)

    retry = retries.StreamingRetry(
        predicate=retries.if_exception_type(
            core_exceptions.ServiceUnavailable, core_exceptions.GatewayTimeout
        ),
        initial=0,
        maximum=0,
        on_error=on_error,
    )
    content = ["hello", "world"]
    errors = [
        core_exceptions.ServiceUnavailable,
        core_exceptions.DeadlineExceeded,
        core_exceptions.NotFound,
    ]
    responses = [{"status": Status(code=_code_from_exc(exc))} for exc in errors]
    seq = sequence.create_streaming_sequence(
        streaming_sequence={
            "name": __name__,
            "content": " ".join(content),
            "responses": responses,
        }
    )
    with pytest.raises(core_exceptions.NotFound):
        it = sequence.attempt_streaming_sequence(name=seq.name, retry=retry)
        [pb.content for pb in it]
    # on_error should have been called on the first two errors, but not the terminal one
    assert len(encountered_excs) == 2
    assert isinstance(encountered_excs[0], core_exceptions.ServiceUnavailable)
    # rest raises superclass GatewayTimeout in place of DeadlineExceeded
    assert isinstance(
        encountered_excs[1],
        (core_exceptions.DeadlineExceeded, core_exceptions.GatewayTimeout),
    )


@pytest.mark.parametrize(
    "initial,multiplier,maximum,expected",
    [
        (0.1, 1.0, 0.5, [0.1, 0.1, 0.1]),
        (0, 2.0, 0.5, [0, 0]),
        (0.1, 2.0, 0.5, [0.1, 0.2, 0.4, 0.5, 0.5]),
        (1, 1.5, 5, [1, 1.5, 2.25, 3.375, 5, 5]),
    ],
)
def test_streaming_retry_sleep_generator(
    sequence, initial, multiplier, maximum, expected
):
    """
    should be able to pass in sleep generator to control backoff
    """
    retry = retries.StreamingRetry(
        predicate=retries.if_exception_type(core_exceptions.ServiceUnavailable),
        initial=initial,
        maximum=maximum,
        multiplier=multiplier,
    )
    content = ["hello", "world"]
    error = Status(
        code=_code_from_exc(core_exceptions.ServiceUnavailable),
        message="transient error",
    )
    transient_error_list = [{"status": error}] * len(expected)
    responses = transient_error_list + [
        {"status": Status(code=0), "response_index": len(content)}
    ]
    seq = sequence.create_streaming_sequence(
        streaming_sequence={
            "name": __name__,
            "content": " ".join(content),
            "responses": responses,
        }
    )
    with mock.patch("random.uniform") as mock_uniform:
        # make sleep generator deterministic
        mock_uniform.side_effect = lambda a, b: b
        with mock.patch("time.sleep") as mock_sleep:
            it = sequence.attempt_streaming_sequence(name=seq.name, retry=retry)
            [pb.content for pb in it]
            assert mock_sleep.call_count == len(expected)
    # ensure that sleep times match expected
    assert mock_sleep.call_args_list == [
        mock.call(sleep_time) for sleep_time in expected
    ]

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
    content = ['hello', 'world']
    seq = sequence.create_streaming_sequence(
        streaming_sequence={
            'name': 'test_streaming_retry_success',
            'content': ' '.join(content),
            # single response with entire stream content
            'responses': [{'status': Status(code=0), 'response_index': len(content)}],
        }
    )
    it = sequence.attempt_streaming_sequence(name=seq.name)
    results = [pb.content for pb in it]
    assert results == content
    # verify streaming report
    report = sequence.get_streaming_sequence_report(name=f'{seq.name}/streamingSequenceReport')
    assert len(report.attempts) == 1
    assert report.attempts[0].status == Status(code=0)


def test_streaming_non_retryable_error(sequence):
    """
    Test a retryable stream failing with non-retryable error
    """
    retry = retries.Retry(predicate=retries.if_exception_type(), is_stream=True)
    content = ['hello', 'world']
    error = Status(code=_code_from_exc(core_exceptions.ServiceUnavailable), message='expected error')
    seq = sequence.create_streaming_sequence(
        streaming_sequence={
            'name': 'test_streaming_retry_success',
            'content': ' '.join(content),
            'responses': [{'status': error, 'response_index': 0}],
        }
    )
    with pytest.raises(core_exceptions.ServiceUnavailable):
        it = sequence.attempt_streaming_sequence(name=seq.name, retry=retry)
        next(it)
    # verify streaming report
    report = sequence.get_streaming_sequence_report(name=f'{seq.name}/streamingSequenceReport')
    assert len(report.attempts) == 1
    assert report.attempts[0].status == error

def test_streaming_retryable_eventual_success(sequence):
    """
    Server returns a retryable error a number of times before success.
    Retryable errors should not be presented to the end user.
    """
    retry = retries.Retry(
        predicate=retries.if_exception_type(core_exceptions.ServiceUnavailable),
        initial=0,
        maximum=0,
        timeout=1,
        is_stream=True
    )
    content = ['hello', 'world']
    error = Status(code=_code_from_exc(core_exceptions.ServiceUnavailable), message='transient error')
    responses =  [{'status': error, 'response_index': 0} for _ in range(3)] + [{'status': Status(code=0), 'response_index': len(content)}]
    seq = sequence.create_streaming_sequence(
        streaming_sequence={
            'name': 'test_streaming_retry_success',
            'content': ' '.join(content),
            'responses': responses,
        }
    )
    it = sequence.attempt_streaming_sequence(name=seq.name, retry=retry)
    results = [pb.content for pb in it]
    assert results == content
    # verify streaming report
    report = sequence.get_streaming_sequence_report(name=f'{seq.name}/streamingSequenceReport')
    assert len(report.attempts) == 4
    assert report.attempts[0].status == error
    assert report.attempts[1].status == error
    assert report.attempts[2].status == error
    assert report.attempts[3].status == Status(code=0)


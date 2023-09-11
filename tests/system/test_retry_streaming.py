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

from google.rpc.status_pb2 import Status
from datetime import timedelta


def test_streaiming_retry_success(sequence):
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


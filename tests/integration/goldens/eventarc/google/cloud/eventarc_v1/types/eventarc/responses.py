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

from google.cloud.eventarc_v1.types import trigger as gce_trigger
from google.protobuf import field_mask_pb2  # type: ignore
from google.protobuf import timestamp_pb2  # type: ignore

__protobuf__ = proto.module(
    package='google.cloud.eventarc.v1',
    manifest={
        'ListTriggersResponse',
    },
)

__manifest__ = (
        'ListTriggersResponse',
)


class ListTriggersResponse(proto.Message):
    r"""The response message for the ListTriggers method.

    Attributes:
        triggers (Sequence[google.cloud.eventarc_v1.types.Trigger]):
            The requested triggers, up to the number specified in
            ``page_size``.
        next_page_token (str):
            A page token that can be sent to ListTriggers
            to request the next page. If this is empty, then
            there are no more pages.
        unreachable (Sequence[str]):
            Unreachable resources, if any.
    """
    __module__ = __module__.rsplit('.', maxsplit=1)[0]  # type: ignore

    @property
    def raw_page(self):
        return self

    triggers = proto.RepeatedField(
        proto.MESSAGE,
        number=1,
        message=gce_trigger.Trigger,
    )
    next_page_token = proto.Field(
        proto.STRING,
        number=2,
    )
    unreachable = proto.RepeatedField(
        proto.STRING,
        number=3,
    )


__all__ = tuple(sorted(__manifest__))

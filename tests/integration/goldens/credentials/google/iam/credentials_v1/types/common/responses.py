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

from google.protobuf import duration_pb2  # type: ignore
from google.protobuf import timestamp_pb2  # type: ignore

__manifest__ = (
        'GenerateAccessTokenResponse',
        'SignBlobResponse',
        'SignJwtResponse',
        'GenerateIdTokenResponse',
)


class GenerateAccessTokenResponse(proto.Message):
    r"""

    Attributes:
        access_token (str):
            The OAuth 2.0 access token.
        expire_time (google.protobuf.timestamp_pb2.Timestamp):
            Token expiration time.
            The expiration time is always set.
    """
    __module__ = __module__.rsplit('.', maxsplit=1)[0]  # type: ignore

    access_token = proto.Field(
        proto.STRING,
        number=1,
    )
    expire_time = proto.Field(
        proto.MESSAGE,
        number=3,
        message=timestamp_pb2.Timestamp,
    )


class SignBlobResponse(proto.Message):
    r"""

    Attributes:
        key_id (str):
            The ID of the key used to sign the blob.
        signed_blob (bytes):
            The signed blob.
    """
    __module__ = __module__.rsplit('.', maxsplit=1)[0]  # type: ignore

    key_id = proto.Field(
        proto.STRING,
        number=1,
    )
    signed_blob = proto.Field(
        proto.BYTES,
        number=4,
    )


class SignJwtResponse(proto.Message):
    r"""

    Attributes:
        key_id (str):
            The ID of the key used to sign the JWT.
        signed_jwt (str):
            The signed JWT.
    """
    __module__ = __module__.rsplit('.', maxsplit=1)[0]  # type: ignore

    key_id = proto.Field(
        proto.STRING,
        number=1,
    )
    signed_jwt = proto.Field(
        proto.STRING,
        number=2,
    )


class GenerateIdTokenResponse(proto.Message):
    r"""

    Attributes:
        token (str):
            The OpenId Connect ID token.
    """
    __module__ = __module__.rsplit('.', maxsplit=1)[0]  # type: ignore

    token = proto.Field(
        proto.STRING,
        number=1,
    )


__all__ = tuple(sorted(__manifest__))

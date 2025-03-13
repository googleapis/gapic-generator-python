# Copyright 2018 Google LLC
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

import os
import pytest
from datetime import datetime, timedelta, timezone

from google import showcase
from google.api_core import exceptions
from google.rpc import code_pb2


def test_lro_success(echo):
    future = echo.wait(
        {
            "end_time": datetime.now(tz=timezone.utc) + timedelta(seconds=1),
            "success": {
                "content": "The hail in Wales falls mainly on the snails...eventually."
            },
        }
    )
    response = future.result()
    assert isinstance(response, showcase.WaitResponse)
    assert response.content.endswith("the snails...eventually.")


def test_lro_error(echo):
    with pytest.raises(
        exceptions.GoogleAPICallError,
        match="(?i)This took longer than you said it should",
    ):
        future = echo.wait(
            {
                "end_time": datetime.now(tz=timezone.utc) + timedelta(seconds=1),
                "error": {
                    "code": code_pb2.Code.Value("DEADLINE_EXCEEDED"),
                    "message": "This took longer than you said it should.",
                },
            }
        )
        future.result()


def test_lro_no_result(echo):
    # As per the link below, `Some services might not provide a result`.
    # Neither `error` or `response`.
    # See https://github.com/googleapis/googleapis/blob/a6c9ed2d33105cb3dc9a0867a0a5d761b049b932/google/longrunning/operations.proto#L141
    future = echo.wait(
        {
            "end_time": datetime.now(tz=timezone.utc) + timedelta(seconds=1),
        }
    )
    response = future.result()
    assert response is None


if os.environ.get("GAPIC_PYTHON_ASYNC", "true") == "true":

    @pytest.mark.asyncio
    async def test_lro_async_success(async_echo):

        future = await async_echo.wait(
            {
                "end_time": datetime.now(tz=timezone.utc) + timedelta(seconds=1),
                "success": {
                    "content": "The hail in Wales falls mainly on the snails...eventually."
                },
            }
        )
        response = await future.result()
        assert isinstance(response, showcase.WaitResponse)
        assert response.content.endswith("the snails...eventually.")

    @pytest.mark.asyncio
    async def test_lro_async_error(async_echo):

        with pytest.raises(
            exceptions.GoogleAPICallError,
            match="(?i)This took longer than you said it should",
        ):
            future = await async_echo.wait(
                {
                    "end_time": datetime.now(tz=timezone.utc) + timedelta(seconds=1),
                    "error": {
                        "code": code_pb2.Code.Value("DEADLINE_EXCEEDED"),
                        "message": "This took longer than you said it should.",
                    },
                }
            )
            await future.result(timeout=600)

    @pytest.mark.asyncio
    async def test_lro_async_no_result(async_echo):
        # As per the link below, `Some services might not provide a result`.
        # Neither `error` or `response`.
        # See https://github.com/googleapis/googleapis/blob/a6c9ed2d33105cb3dc9a0867a0a5d761b049b932/google/longrunning/operations.proto#L141
        future = await async_echo.wait(
            {
                "end_time": datetime.now(tz=timezone.utc) + timedelta(seconds=1),
            }
        )
        response = await future.result()
        assert response is None

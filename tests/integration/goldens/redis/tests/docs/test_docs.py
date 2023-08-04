# -*- coding: utf-8 -*-
# Copyright 2023 Google LLC
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
import os
import pathlib
import requests
import subprocess

INTERSPHINX_CACHE = "/tmp/intersphinx_inventories/"

# Download intersphinx inventories to workaround rate limits
# related to fetching intersphinx inventories from the internet during
# the docs build. The error when rate limits occur is shown below:
# `not fetchable due to HTTPError 429 Client Error: Too Many Requests for url`
intersphinx_mapping = [
    {"package": "python", "url": "https://python.readthedocs.io/en/latest/"},
    {"package": "google-auth", "url": "https://googleapis.dev/python/google-auth/latest/"},
    {"package": "google.api_core", "url": "https://googleapis.dev/python/google-api-core/latest/"},
    {"package": "grpc", "url": "https://grpc.github.io/grpc/python/"},
    {"package": "requests", "url": "https://requests.kennethreitz.org/en/stable/"},
    {"package": "proto", "url": "https://googleapis.dev/python/proto-plus/latest/"},
    {"package": "protobuf", "url": "https://googleapis.dev/python/protobuf/latest/"},
]

def cache_intersphinx_inventory(package: str, url: str):
    if not pathlib.Path(f"{INTERSPHINX_CACHE}/{package}").exists():
        os.mkdir(f"{INTERSPHINX_CACHE}/{package}")
    if not pathlib.Path(f"{INTERSPHINX_CACHE}/{package}/objects.inv").exists():
        response = requests.get(f"{url}objects.inv", allow_redirects=True, stream=True)
        if response.status_code == 200:
            with open(f"{INTERSPHINX_CACHE}/{package}/objects.inv", "wb") as f:
                f.write(response.content)


def test_docs():
    if not pathlib.Path(INTERSPHINX_CACHE).exists():
        os.mkdir(INTERSPHINX_CACHE)
    for item in intersphinx_mapping:
        cache_intersphinx_inventory(item['package'], item['url'])

    # Update permissions so that docs can be created
    os.chmod(
        str(
            os.path.join(
                os.path.dirname(os.path.abspath(__file__)),
                "../../"
                "docs",
            )
        ),
        0o744,
    )

    result = subprocess.run(
        [
            "python3",
            "-m",
            "sphinx.cmd.build",
            "-W",  # warnings as errors
            "-T",  # show full traceback on exception
            "-N",  # no colors
            "-b",
            "html",
            "-d",
            os.path.join(
                os.path.dirname(os.path.abspath(__file__)),
                "../../"
                "docs",
                "_build",
                "doctrees",
                "",
            ),
            os.path.join(
                os.path.dirname(os.path.abspath(__file__)),
                "../../"
                "docs",
                "",
            ),
            os.path.join(
                os.path.dirname(os.path.abspath(__file__)),
                "../../"
                "docs",
                "_build",
                "html",
                "",
            ),
        ]
    )

    assert result.returncode == 0, result

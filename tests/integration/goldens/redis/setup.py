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
import io
import os
import re

import setuptools # type: ignore

package_root = os.path.abspath(os.path.dirname(__file__))

name = 'google-cloud-redis'


description = "Google Cloud Redis API client library"

version = None

with open(os.path.join(package_root, 'google/cloud/redis/gapic_version.py')) as fp:
    version_candidates = re.findall(r"(?<=\")\d+.\d+.\d+(?=\")", fp.read())
    assert (len(version_candidates) == 1)
    version = version_candidates[0]

if version[0] == "0":
    release_status = "Development Status :: 4 - Beta"
else:
    release_status = "Development Status :: 5 - Production/Stable"

dependencies = [
    "google-api-core[grpc] >= 2.19.1, <3.0.0dev",
    # Exclude incompatible versions of `google-auth`
    # See https://github.com/googleapis/google-cloud-python/issues/12364
    "google-auth >= 2.14.1, <3.0.0dev,!=2.24.0,!=2.25.0",
    "proto-plus >= 1.24.0, <2.0.0dev",
    "proto-plus >= 1.25.0, <2.0.0dev; python_version >= '3.13'",
    # protobuf >= 5.27.0 is needed which supports `google.protobuf.runtime_version`
    "protobuf>=5.27.0,<6.0.0dev",
]
extras = {
    "async_rest": [
        "google-api-core[grpc] >= 2.21.0, < 3.0.0dev",
        "google-auth[aiohttp] >= 2.35.0, <3.0.0dev"
    ],
}
url = "https://github.com/googleapis/google-cloud-python/tree/main/packages/google-cloud-redis"

package_root = os.path.abspath(os.path.dirname(__file__))

readme_filename = os.path.join(package_root, "README.rst")
with io.open(readme_filename, encoding="utf-8") as readme_file:
    readme = readme_file.read()

packages = [
    package
    for package in setuptools.find_namespace_packages()
    if package.startswith("google")
]

setuptools.setup(
    name=name,
    version=version,
    description=description,
    long_description=readme,
    author="Google LLC",
    author_email="googleapis-packages@google.com",
    license="Apache 2.0",
    url=url,
    classifiers=[
        release_status,
        "Intended Audience :: Developers",
        "License :: OSI Approved :: Apache Software License",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Programming Language :: Python :: 3.12",
        "Programming Language :: Python :: 3.13",
        "Operating System :: OS Independent",
        "Topic :: Internet",
    ],
    platforms="Posix; MacOS X; Windows",
    packages=packages,
    python_requires=">=3.8",
    install_requires=dependencies,
    extras_require=extras,
    include_package_data=True,
    zip_safe=False,
)

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
import sys
import warnings

from google.iam.credentials import gapic_version as package_version

__version__ = package_version.__version__


from google.iam.credentials_v1.services.iam_credentials.client import IAMCredentialsClient
from google.iam.credentials_v1.services.iam_credentials.async_client import IAMCredentialsAsyncClient

from google.iam.credentials_v1.types.common import GenerateAccessTokenRequest
from google.iam.credentials_v1.types.common import GenerateAccessTokenResponse
from google.iam.credentials_v1.types.common import GenerateIdTokenRequest
from google.iam.credentials_v1.types.common import GenerateIdTokenResponse
from google.iam.credentials_v1.types.common import SignBlobRequest
from google.iam.credentials_v1.types.common import SignBlobResponse
from google.iam.credentials_v1.types.common import SignJwtRequest
from google.iam.credentials_v1.types.common import SignJwtResponse


class Python37DeprecationWarning(DeprecationWarning):
    """
    Deprecation warning raised when Python 3.7 runtime is detected.
    Python 3.7 support will be dropped after January 1, 2024. See
    https://cloud.google.com/python/docs/python37-sunset/ for more information.
    """
    pass

# Checks if the current runtime is Python 3.7.
if sys.version_info.major == 3 and sys.version_info.minor == 7:
    message = (
        "After January 1, 2024, new releases of this client library will drop support "
        "for Python 3.7. More details about Python 3.7 support for Client Libraries "
        "can be found at https://cloud.google.com/python/docs/python37-sunset/"
    )
    # Configure the Python37DeprecationWarning warning so that it is only emitted once.
    warnings.simplefilter('once', Python37DeprecationWarning)
    warnings.warn(message, Python37DeprecationWarning)


__all__ = ('IAMCredentialsClient',
    'IAMCredentialsAsyncClient',
    'GenerateAccessTokenRequest',
    'GenerateAccessTokenResponse',
    'GenerateIdTokenRequest',
    'GenerateIdTokenResponse',
    'SignBlobRequest',
    'SignBlobResponse',
    'SignJwtRequest',
    'SignJwtResponse',
)

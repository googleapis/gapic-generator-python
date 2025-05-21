# -*- coding: utf-8 -*-
# Copyright 2025 Google LLC
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

# try/except added for compatibility with python < 3.8
try:
    from unittest import mock
except ImportError:  # pragma: NO COVER
    import mock

from google.auth.exceptions import MutualTLSChannelError          # type: ignore

def _read_environment_variables():
    """Returns the environment variables used by the client.

    Returns:
        Tuple[bool, str, str]: returns the GOOGLE_API_USE_CLIENT_CERTIFICATE,
        GOOGLE_API_USE_MTLS_ENDPOINT, and GOOGLE_CLOUD_UNIVERSE_DOMAIN environment variables.

    Raises:
        ValueError: If GOOGLE_API_USE_CLIENT_CERTIFICATE is not
            any of ["true", "false"].
        google.auth.exceptions.MutualTLSChannelError: If GOOGLE_API_USE_MTLS_ENDPOINT
            is not any of ["auto", "never", "always"].
    """
    use_client_cert = os.getenv("GOOGLE_API_USE_CLIENT_CERTIFICATE", "false").lower()
    use_mtls_endpoint = os.getenv("GOOGLE_API_USE_MTLS_ENDPOINT", "auto").lower()
    universe_domain_env = os.getenv("GOOGLE_CLOUD_UNIVERSE_DOMAIN")
    if use_client_cert not in ("true", "false"):
        raise ValueError("Environment variable `GOOGLE_API_USE_CLIENT_CERTIFICATE` must be either `true` or `false`")
    if use_mtls_endpoint not in ("auto", "never", "always"):
        raise MutualTLSChannelError("Environment variable `GOOGLE_API_USE_MTLS_ENDPOINT` must be `never`, `auto` or `always`")
    return use_client_cert == "true", use_mtls_endpoint, universe_domain_env

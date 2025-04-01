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
    from unittest.mock import AsyncMock  # pragma: NO COVER
except ImportError:  # pragma: NO COVER
    import mock

import grpc
from grpc.experimental import aio
from collections.abc import Iterable, AsyncIterable
from google.protobuf import json_format
import json
import math
import pytest
from google.api_core import api_core_version
from proto.marshal.rules.dates import DurationRule, TimestampRule
from proto.marshal.rules import wrappers
from requests import Response
from requests import Request, PreparedRequest
from requests.sessions import Session
from google.protobuf import json_format

try:
    from google.auth.aio import credentials as ga_credentials_async
    HAS_GOOGLE_AUTH_AIO = True
except ImportError: # pragma: NO COVER
    HAS_GOOGLE_AUTH_AIO = False

from google.api_core import client_options
from google.api_core import exceptions as core_exceptions
from google.api_core import gapic_v1
from google.api_core import grpc_helpers
from google.api_core import grpc_helpers_async
from google.api_core import path_template
from google.api_core import retry as retries
from google.auth import credentials as ga_credentials
from google.auth.exceptions import MutualTLSChannelError
from google.fragment.services.page_size_dataset_service import PageSizeDatasetServiceAsyncClient
from google.fragment.services.page_size_dataset_service import PageSizeDatasetServiceClient
from google.fragment.services.page_size_dataset_service import pagers
from google.fragment.services.page_size_dataset_service import transports
from google.fragment.types import test_pagination_page_size
from google.oauth2 import service_account
import google.auth



CRED_INFO_JSON = {
    "credential_source": "/path/to/file",
    "credential_type": "service account credentials",
    "principal": "service-account@example.com",
}
CRED_INFO_STRING = json.dumps(CRED_INFO_JSON)


async def mock_async_gen(data, chunk_size=1):
    for i in range(0, len(data)):  # pragma: NO COVER
        chunk = data[i : i + chunk_size]
        yield chunk.encode("utf-8")

def client_cert_source_callback():
    return b"cert bytes", b"key bytes"

# TODO: use async auth anon credentials by default once the minimum version of google-auth is upgraded.
# See related issue: https://github.com/googleapis/gapic-generator-python/issues/2107.
def async_anonymous_credentials():
    if HAS_GOOGLE_AUTH_AIO:
        return ga_credentials_async.AnonymousCredentials()
    return ga_credentials.AnonymousCredentials()

# If default endpoint is localhost, then default mtls endpoint will be the same.
# This method modifies the default endpoint so the client can produce a different
# mtls endpoint for endpoint testing purposes.
def modify_default_endpoint(client):
    return "foo.googleapis.com" if ("localhost" in client.DEFAULT_ENDPOINT) else client.DEFAULT_ENDPOINT

# If default endpoint template is localhost, then default mtls endpoint will be the same.
# This method modifies the default endpoint template so the client can produce a different
# mtls endpoint for endpoint testing purposes.
def modify_default_endpoint_template(client):
    return "test.{UNIVERSE_DOMAIN}" if ("localhost" in client._DEFAULT_ENDPOINT_TEMPLATE) else client._DEFAULT_ENDPOINT_TEMPLATE


def test__get_default_mtls_endpoint():
    api_endpoint = "example.googleapis.com"
    api_mtls_endpoint = "example.mtls.googleapis.com"
    sandbox_endpoint = "example.sandbox.googleapis.com"
    sandbox_mtls_endpoint = "example.mtls.sandbox.googleapis.com"
    non_googleapi = "api.example.com"

    assert PageSizeDatasetServiceClient._get_default_mtls_endpoint(None) is None
    assert PageSizeDatasetServiceClient._get_default_mtls_endpoint(api_endpoint) == api_mtls_endpoint
    assert PageSizeDatasetServiceClient._get_default_mtls_endpoint(api_mtls_endpoint) == api_mtls_endpoint
    assert PageSizeDatasetServiceClient._get_default_mtls_endpoint(sandbox_endpoint) == sandbox_mtls_endpoint
    assert PageSizeDatasetServiceClient._get_default_mtls_endpoint(sandbox_mtls_endpoint) == sandbox_mtls_endpoint
    assert PageSizeDatasetServiceClient._get_default_mtls_endpoint(non_googleapi) == non_googleapi

def test__read_environment_variables():
    assert PageSizeDatasetServiceClient._read_environment_variables() == (False, "auto", None)

    with mock.patch.dict(os.environ, {"GOOGLE_API_USE_CLIENT_CERTIFICATE": "true"}):
        assert PageSizeDatasetServiceClient._read_environment_variables() == (True, "auto", None)

    with mock.patch.dict(os.environ, {"GOOGLE_API_USE_CLIENT_CERTIFICATE": "false"}):
        assert PageSizeDatasetServiceClient._read_environment_variables() == (False, "auto", None)

    with mock.patch.dict(os.environ, {"GOOGLE_API_USE_CLIENT_CERTIFICATE": "Unsupported"}):
        with pytest.raises(ValueError) as excinfo:
            PageSizeDatasetServiceClient._read_environment_variables()
    assert str(excinfo.value) == "Environment variable `GOOGLE_API_USE_CLIENT_CERTIFICATE` must be either `true` or `false`"

    with mock.patch.dict(os.environ, {"GOOGLE_API_USE_MTLS_ENDPOINT": "never"}):
        assert PageSizeDatasetServiceClient._read_environment_variables() == (False, "never", None)

    with mock.patch.dict(os.environ, {"GOOGLE_API_USE_MTLS_ENDPOINT": "always"}):
        assert PageSizeDatasetServiceClient._read_environment_variables() == (False, "always", None)

    with mock.patch.dict(os.environ, {"GOOGLE_API_USE_MTLS_ENDPOINT": "auto"}):
        assert PageSizeDatasetServiceClient._read_environment_variables() == (False, "auto", None)

    with mock.patch.dict(os.environ, {"GOOGLE_API_USE_MTLS_ENDPOINT": "Unsupported"}):
        with pytest.raises(MutualTLSChannelError) as excinfo:
            PageSizeDatasetServiceClient._read_environment_variables()
    assert str(excinfo.value) == "Environment variable `GOOGLE_API_USE_MTLS_ENDPOINT` must be `never`, `auto` or `always`"

    with mock.patch.dict(os.environ, {"GOOGLE_CLOUD_UNIVERSE_DOMAIN": "foo.com"}):
        assert PageSizeDatasetServiceClient._read_environment_variables() == (False, "auto", "foo.com")

def test__get_client_cert_source():
    mock_provided_cert_source = mock.Mock()
    mock_default_cert_source = mock.Mock()

    assert PageSizeDatasetServiceClient._get_client_cert_source(None, False) is None
    assert PageSizeDatasetServiceClient._get_client_cert_source(mock_provided_cert_source, False) is None
    assert PageSizeDatasetServiceClient._get_client_cert_source(mock_provided_cert_source, True) == mock_provided_cert_source

    with mock.patch('google.auth.transport.mtls.has_default_client_cert_source', return_value=True):
        with mock.patch('google.auth.transport.mtls.default_client_cert_source', return_value=mock_default_cert_source):
            assert PageSizeDatasetServiceClient._get_client_cert_source(None, True) is mock_default_cert_source
            assert PageSizeDatasetServiceClient._get_client_cert_source(mock_provided_cert_source, "true") is mock_provided_cert_source

@mock.patch.object(PageSizeDatasetServiceClient, "_DEFAULT_ENDPOINT_TEMPLATE", modify_default_endpoint_template(PageSizeDatasetServiceClient))
@mock.patch.object(PageSizeDatasetServiceAsyncClient, "_DEFAULT_ENDPOINT_TEMPLATE", modify_default_endpoint_template(PageSizeDatasetServiceAsyncClient))
def test__get_api_endpoint():
    api_override = "foo.com"
    mock_client_cert_source = mock.Mock()
    default_universe = PageSizeDatasetServiceClient._DEFAULT_UNIVERSE
    default_endpoint = PageSizeDatasetServiceClient._DEFAULT_ENDPOINT_TEMPLATE.format(UNIVERSE_DOMAIN=default_universe)
    mock_universe = "bar.com"
    mock_endpoint = PageSizeDatasetServiceClient._DEFAULT_ENDPOINT_TEMPLATE.format(UNIVERSE_DOMAIN=mock_universe)

    assert PageSizeDatasetServiceClient._get_api_endpoint(api_override, mock_client_cert_source, default_universe, "always") == api_override
    assert PageSizeDatasetServiceClient._get_api_endpoint(None, mock_client_cert_source, default_universe, "auto") == PageSizeDatasetServiceClient.DEFAULT_MTLS_ENDPOINT
    assert PageSizeDatasetServiceClient._get_api_endpoint(None, None, default_universe, "auto") == default_endpoint
    assert PageSizeDatasetServiceClient._get_api_endpoint(None, None, default_universe, "always") == PageSizeDatasetServiceClient.DEFAULT_MTLS_ENDPOINT
    assert PageSizeDatasetServiceClient._get_api_endpoint(None, mock_client_cert_source, default_universe, "always") == PageSizeDatasetServiceClient.DEFAULT_MTLS_ENDPOINT
    assert PageSizeDatasetServiceClient._get_api_endpoint(None, None, mock_universe, "never") == mock_endpoint
    assert PageSizeDatasetServiceClient._get_api_endpoint(None, None, default_universe, "never") == default_endpoint

    with pytest.raises(MutualTLSChannelError) as excinfo:
        PageSizeDatasetServiceClient._get_api_endpoint(None, mock_client_cert_source, mock_universe, "auto")
    assert str(excinfo.value) == "mTLS is not supported in any universe other than googleapis.com."


def test__get_universe_domain():
    client_universe_domain = "foo.com"
    universe_domain_env = "bar.com"

    assert PageSizeDatasetServiceClient._get_universe_domain(client_universe_domain, universe_domain_env) == client_universe_domain
    assert PageSizeDatasetServiceClient._get_universe_domain(None, universe_domain_env) == universe_domain_env
    assert PageSizeDatasetServiceClient._get_universe_domain(None, None) == PageSizeDatasetServiceClient._DEFAULT_UNIVERSE

    with pytest.raises(ValueError) as excinfo:
        PageSizeDatasetServiceClient._get_universe_domain("", None)
    assert str(excinfo.value) == "Universe Domain cannot be an empty string."

@pytest.mark.parametrize("error_code,cred_info_json,show_cred_info", [
    (401, CRED_INFO_JSON, True),
    (403, CRED_INFO_JSON, True),
    (404, CRED_INFO_JSON, True),
    (500, CRED_INFO_JSON, False),
    (401, None, False),
    (403, None, False),
    (404, None, False),
    (500, None, False)
])
def test__add_cred_info_for_auth_errors(error_code, cred_info_json, show_cred_info):
    cred = mock.Mock(["get_cred_info"])
    cred.get_cred_info = mock.Mock(return_value=cred_info_json)
    client = PageSizeDatasetServiceClient(credentials=cred)
    client._transport._credentials = cred

    error = core_exceptions.GoogleAPICallError("message", details=["foo"])
    error.code = error_code

    client._add_cred_info_for_auth_errors(error)
    if show_cred_info:
        assert error.details == ["foo", CRED_INFO_STRING]
    else:
        assert error.details == ["foo"]

@pytest.mark.parametrize("error_code", [401,403,404,500])
def test__add_cred_info_for_auth_errors_no_get_cred_info(error_code):
    cred = mock.Mock([])
    assert not hasattr(cred, "get_cred_info")
    client = PageSizeDatasetServiceClient(credentials=cred)
    client._transport._credentials = cred

    error = core_exceptions.GoogleAPICallError("message", details=[])
    error.code = error_code

    client._add_cred_info_for_auth_errors(error)
    assert error.details == []

@pytest.mark.parametrize("client_class,transport_name", [
    (PageSizeDatasetServiceClient, "grpc"),
    (PageSizeDatasetServiceAsyncClient, "grpc_asyncio"),
    (PageSizeDatasetServiceClient, "rest"),
])
def test_page_size_dataset_service_client_from_service_account_info(client_class, transport_name):
    creds = ga_credentials.AnonymousCredentials()
    with mock.patch.object(service_account.Credentials, 'from_service_account_info') as factory:
        factory.return_value = creds
        info = {"valid": True}
        client = client_class.from_service_account_info(info, transport=transport_name)
        assert client.transport._credentials == creds
        assert isinstance(client, client_class)

        assert client.transport._host == (
            'my.example.com:443'
            if transport_name in ['grpc', 'grpc_asyncio']
            else
            'https://my.example.com'
        )


@pytest.mark.parametrize("transport_class,transport_name", [
    (transports.PageSizeDatasetServiceGrpcTransport, "grpc"),
    (transports.PageSizeDatasetServiceGrpcAsyncIOTransport, "grpc_asyncio"),
    (transports.PageSizeDatasetServiceRestTransport, "rest"),
])
def test_page_size_dataset_service_client_service_account_always_use_jwt(transport_class, transport_name):
    with mock.patch.object(service_account.Credentials, 'with_always_use_jwt_access', create=True) as use_jwt:
        creds = service_account.Credentials(None, None, None)
        transport = transport_class(credentials=creds, always_use_jwt_access=True)
        use_jwt.assert_called_once_with(True)

    with mock.patch.object(service_account.Credentials, 'with_always_use_jwt_access', create=True) as use_jwt:
        creds = service_account.Credentials(None, None, None)
        transport = transport_class(credentials=creds, always_use_jwt_access=False)
        use_jwt.assert_not_called()


@pytest.mark.parametrize("client_class,transport_name", [
    (PageSizeDatasetServiceClient, "grpc"),
    (PageSizeDatasetServiceAsyncClient, "grpc_asyncio"),
    (PageSizeDatasetServiceClient, "rest"),
])
def test_page_size_dataset_service_client_from_service_account_file(client_class, transport_name):
    creds = ga_credentials.AnonymousCredentials()
    with mock.patch.object(service_account.Credentials, 'from_service_account_file') as factory:
        factory.return_value = creds
        client = client_class.from_service_account_file("dummy/file/path.json", transport=transport_name)
        assert client.transport._credentials == creds
        assert isinstance(client, client_class)

        client = client_class.from_service_account_json("dummy/file/path.json", transport=transport_name)
        assert client.transport._credentials == creds
        assert isinstance(client, client_class)

        assert client.transport._host == (
            'my.example.com:443'
            if transport_name in ['grpc', 'grpc_asyncio']
            else
            'https://my.example.com'
        )


def test_page_size_dataset_service_client_get_transport_class():
    transport = PageSizeDatasetServiceClient.get_transport_class()
    available_transports = [
        transports.PageSizeDatasetServiceGrpcTransport,
        transports.PageSizeDatasetServiceRestTransport,
    ]
    assert transport in available_transports

    transport = PageSizeDatasetServiceClient.get_transport_class("grpc")
    assert transport == transports.PageSizeDatasetServiceGrpcTransport


@pytest.mark.parametrize("client_class,transport_class,transport_name", [
    (PageSizeDatasetServiceClient, transports.PageSizeDatasetServiceGrpcTransport, "grpc"),
    (PageSizeDatasetServiceAsyncClient, transports.PageSizeDatasetServiceGrpcAsyncIOTransport, "grpc_asyncio"),
    (PageSizeDatasetServiceClient, transports.PageSizeDatasetServiceRestTransport, "rest"),
])
@mock.patch.object(PageSizeDatasetServiceClient, "_DEFAULT_ENDPOINT_TEMPLATE", modify_default_endpoint_template(PageSizeDatasetServiceClient))
@mock.patch.object(PageSizeDatasetServiceAsyncClient, "_DEFAULT_ENDPOINT_TEMPLATE", modify_default_endpoint_template(PageSizeDatasetServiceAsyncClient))
def test_page_size_dataset_service_client_client_options(client_class, transport_class, transport_name):
    # Check that if channel is provided we won't create a new one.
    with mock.patch.object(PageSizeDatasetServiceClient, 'get_transport_class') as gtc:
        transport = transport_class(
            credentials=ga_credentials.AnonymousCredentials()
        )
        client = client_class(transport=transport)
        gtc.assert_not_called()

    # Check that if channel is provided via str we will create a new one.
    with mock.patch.object(PageSizeDatasetServiceClient, 'get_transport_class') as gtc:
        client = client_class(transport=transport_name)
        gtc.assert_called()

    # Check the case api_endpoint is provided.
    options = client_options.ClientOptions(api_endpoint="squid.clam.whelk")
    with mock.patch.object(transport_class, '__init__') as patched:
        patched.return_value = None
        client = client_class(transport=transport_name, client_options=options)
        patched.assert_called_once_with(
            credentials=None,
            credentials_file=None,
            host="squid.clam.whelk",
            scopes=None,
            client_cert_source_for_mtls=None,
            quota_project_id=None,
            client_info=transports.base.DEFAULT_CLIENT_INFO,
            always_use_jwt_access=True,
            api_audience=None,
        )

    # Check the case api_endpoint is not provided and GOOGLE_API_USE_MTLS_ENDPOINT is
    # "never".
    with mock.patch.dict(os.environ, {"GOOGLE_API_USE_MTLS_ENDPOINT": "never"}):
        with mock.patch.object(transport_class, '__init__') as patched:
            patched.return_value = None
            client = client_class(transport=transport_name)
            patched.assert_called_once_with(
                credentials=None,
                credentials_file=None,
                host=client._DEFAULT_ENDPOINT_TEMPLATE.format(UNIVERSE_DOMAIN=client._DEFAULT_UNIVERSE),
                scopes=None,
                client_cert_source_for_mtls=None,
                quota_project_id=None,
                client_info=transports.base.DEFAULT_CLIENT_INFO,
                always_use_jwt_access=True,
                api_audience=None,
            )

    # Check the case api_endpoint is not provided and GOOGLE_API_USE_MTLS_ENDPOINT is
    # "always".
    with mock.patch.dict(os.environ, {"GOOGLE_API_USE_MTLS_ENDPOINT": "always"}):
        with mock.patch.object(transport_class, '__init__') as patched:
            patched.return_value = None
            client = client_class(transport=transport_name)
            patched.assert_called_once_with(
                credentials=None,
                credentials_file=None,
                host=client.DEFAULT_MTLS_ENDPOINT,
                scopes=None,
                client_cert_source_for_mtls=None,
                quota_project_id=None,
                client_info=transports.base.DEFAULT_CLIENT_INFO,
                always_use_jwt_access=True,
                api_audience=None,
            )

    # Check the case api_endpoint is not provided and GOOGLE_API_USE_MTLS_ENDPOINT has
    # unsupported value.
    with mock.patch.dict(os.environ, {"GOOGLE_API_USE_MTLS_ENDPOINT": "Unsupported"}):
        with pytest.raises(MutualTLSChannelError) as excinfo:
            client = client_class(transport=transport_name)
    assert str(excinfo.value) == "Environment variable `GOOGLE_API_USE_MTLS_ENDPOINT` must be `never`, `auto` or `always`"

    # Check the case GOOGLE_API_USE_CLIENT_CERTIFICATE has unsupported value.
    with mock.patch.dict(os.environ, {"GOOGLE_API_USE_CLIENT_CERTIFICATE": "Unsupported"}):
        with pytest.raises(ValueError) as excinfo:
            client = client_class(transport=transport_name)
    assert str(excinfo.value) == "Environment variable `GOOGLE_API_USE_CLIENT_CERTIFICATE` must be either `true` or `false`"

    # Check the case quota_project_id is provided
    options = client_options.ClientOptions(quota_project_id="octopus")
    with mock.patch.object(transport_class, '__init__') as patched:
        patched.return_value = None
        client = client_class(client_options=options, transport=transport_name)
        patched.assert_called_once_with(
            credentials=None,
            credentials_file=None,
            host=client._DEFAULT_ENDPOINT_TEMPLATE.format(UNIVERSE_DOMAIN=client._DEFAULT_UNIVERSE),
            scopes=None,
            client_cert_source_for_mtls=None,
            quota_project_id="octopus",
            client_info=transports.base.DEFAULT_CLIENT_INFO,
            always_use_jwt_access=True,
            api_audience=None,
        )
    # Check the case api_endpoint is provided
    options = client_options.ClientOptions(api_audience="https://language.googleapis.com")
    with mock.patch.object(transport_class, '__init__') as patched:
        patched.return_value = None
        client = client_class(client_options=options, transport=transport_name)
        patched.assert_called_once_with(
            credentials=None,
            credentials_file=None,
            host=client._DEFAULT_ENDPOINT_TEMPLATE.format(UNIVERSE_DOMAIN=client._DEFAULT_UNIVERSE),
            scopes=None,
            client_cert_source_for_mtls=None,
            quota_project_id=None,
            client_info=transports.base.DEFAULT_CLIENT_INFO,
            always_use_jwt_access=True,
            api_audience="https://language.googleapis.com"
        )

@pytest.mark.parametrize("client_class,transport_class,transport_name,use_client_cert_env", [
    (PageSizeDatasetServiceClient, transports.PageSizeDatasetServiceGrpcTransport, "grpc", "true"),
    (PageSizeDatasetServiceAsyncClient, transports.PageSizeDatasetServiceGrpcAsyncIOTransport, "grpc_asyncio", "true"),
    (PageSizeDatasetServiceClient, transports.PageSizeDatasetServiceGrpcTransport, "grpc", "false"),
    (PageSizeDatasetServiceAsyncClient, transports.PageSizeDatasetServiceGrpcAsyncIOTransport, "grpc_asyncio", "false"),
    (PageSizeDatasetServiceClient, transports.PageSizeDatasetServiceRestTransport, "rest", "true"),
    (PageSizeDatasetServiceClient, transports.PageSizeDatasetServiceRestTransport, "rest", "false"),
])
@mock.patch.object(PageSizeDatasetServiceClient, "_DEFAULT_ENDPOINT_TEMPLATE", modify_default_endpoint_template(PageSizeDatasetServiceClient))
@mock.patch.object(PageSizeDatasetServiceAsyncClient, "_DEFAULT_ENDPOINT_TEMPLATE", modify_default_endpoint_template(PageSizeDatasetServiceAsyncClient))
@mock.patch.dict(os.environ, {"GOOGLE_API_USE_MTLS_ENDPOINT": "auto"})
def test_page_size_dataset_service_client_mtls_env_auto(client_class, transport_class, transport_name, use_client_cert_env):
    # This tests the endpoint autoswitch behavior. Endpoint is autoswitched to the default
    # mtls endpoint, if GOOGLE_API_USE_CLIENT_CERTIFICATE is "true" and client cert exists.

    # Check the case client_cert_source is provided. Whether client cert is used depends on
    # GOOGLE_API_USE_CLIENT_CERTIFICATE value.
    with mock.patch.dict(os.environ, {"GOOGLE_API_USE_CLIENT_CERTIFICATE": use_client_cert_env}):
        options = client_options.ClientOptions(client_cert_source=client_cert_source_callback)
        with mock.patch.object(transport_class, '__init__') as patched:
            patched.return_value = None
            client = client_class(client_options=options, transport=transport_name)

            if use_client_cert_env == "false":
                expected_client_cert_source = None
                expected_host = client._DEFAULT_ENDPOINT_TEMPLATE.format(UNIVERSE_DOMAIN=client._DEFAULT_UNIVERSE)
            else:
                expected_client_cert_source = client_cert_source_callback
                expected_host = client.DEFAULT_MTLS_ENDPOINT

            patched.assert_called_once_with(
                credentials=None,
                credentials_file=None,
                host=expected_host,
                scopes=None,
                client_cert_source_for_mtls=expected_client_cert_source,
                quota_project_id=None,
                client_info=transports.base.DEFAULT_CLIENT_INFO,
                always_use_jwt_access=True,
                api_audience=None,
            )

    # Check the case ADC client cert is provided. Whether client cert is used depends on
    # GOOGLE_API_USE_CLIENT_CERTIFICATE value.
    with mock.patch.dict(os.environ, {"GOOGLE_API_USE_CLIENT_CERTIFICATE": use_client_cert_env}):
        with mock.patch.object(transport_class, '__init__') as patched:
            with mock.patch('google.auth.transport.mtls.has_default_client_cert_source', return_value=True):
                with mock.patch('google.auth.transport.mtls.default_client_cert_source', return_value=client_cert_source_callback):
                    if use_client_cert_env == "false":
                        expected_host = client._DEFAULT_ENDPOINT_TEMPLATE.format(UNIVERSE_DOMAIN=client._DEFAULT_UNIVERSE)
                        expected_client_cert_source = None
                    else:
                        expected_host = client.DEFAULT_MTLS_ENDPOINT
                        expected_client_cert_source = client_cert_source_callback

                    patched.return_value = None
                    client = client_class(transport=transport_name)
                    patched.assert_called_once_with(
                        credentials=None,
                        credentials_file=None,
                        host=expected_host,
                        scopes=None,
                        client_cert_source_for_mtls=expected_client_cert_source,
                        quota_project_id=None,
                        client_info=transports.base.DEFAULT_CLIENT_INFO,
                        always_use_jwt_access=True,
                        api_audience=None,
                    )

    # Check the case client_cert_source and ADC client cert are not provided.
    with mock.patch.dict(os.environ, {"GOOGLE_API_USE_CLIENT_CERTIFICATE": use_client_cert_env}):
        with mock.patch.object(transport_class, '__init__') as patched:
            with mock.patch("google.auth.transport.mtls.has_default_client_cert_source", return_value=False):
                patched.return_value = None
                client = client_class(transport=transport_name)
                patched.assert_called_once_with(
                    credentials=None,
                    credentials_file=None,
                    host=client._DEFAULT_ENDPOINT_TEMPLATE.format(UNIVERSE_DOMAIN=client._DEFAULT_UNIVERSE),
                    scopes=None,
                    client_cert_source_for_mtls=None,
                    quota_project_id=None,
                    client_info=transports.base.DEFAULT_CLIENT_INFO,
                    always_use_jwt_access=True,
                    api_audience=None,
                )


@pytest.mark.parametrize("client_class", [
    PageSizeDatasetServiceClient, PageSizeDatasetServiceAsyncClient
])
@mock.patch.object(PageSizeDatasetServiceClient, "DEFAULT_ENDPOINT", modify_default_endpoint(PageSizeDatasetServiceClient))
@mock.patch.object(PageSizeDatasetServiceAsyncClient, "DEFAULT_ENDPOINT", modify_default_endpoint(PageSizeDatasetServiceAsyncClient))
def test_page_size_dataset_service_client_get_mtls_endpoint_and_cert_source(client_class):
    mock_client_cert_source = mock.Mock()

    # Test the case GOOGLE_API_USE_CLIENT_CERTIFICATE is "true".
    with mock.patch.dict(os.environ, {"GOOGLE_API_USE_CLIENT_CERTIFICATE": "true"}):
        mock_api_endpoint = "foo"
        options = client_options.ClientOptions(client_cert_source=mock_client_cert_source, api_endpoint=mock_api_endpoint)
        api_endpoint, cert_source = client_class.get_mtls_endpoint_and_cert_source(options)
        assert api_endpoint == mock_api_endpoint
        assert cert_source == mock_client_cert_source

    # Test the case GOOGLE_API_USE_CLIENT_CERTIFICATE is "false".
    with mock.patch.dict(os.environ, {"GOOGLE_API_USE_CLIENT_CERTIFICATE": "false"}):
        mock_client_cert_source = mock.Mock()
        mock_api_endpoint = "foo"
        options = client_options.ClientOptions(client_cert_source=mock_client_cert_source, api_endpoint=mock_api_endpoint)
        api_endpoint, cert_source = client_class.get_mtls_endpoint_and_cert_source(options)
        assert api_endpoint == mock_api_endpoint
        assert cert_source is None

    # Test the case GOOGLE_API_USE_MTLS_ENDPOINT is "never".
    with mock.patch.dict(os.environ, {"GOOGLE_API_USE_MTLS_ENDPOINT": "never"}):
        api_endpoint, cert_source = client_class.get_mtls_endpoint_and_cert_source()
        assert api_endpoint == client_class.DEFAULT_ENDPOINT
        assert cert_source is None

    # Test the case GOOGLE_API_USE_MTLS_ENDPOINT is "always".
    with mock.patch.dict(os.environ, {"GOOGLE_API_USE_MTLS_ENDPOINT": "always"}):
        api_endpoint, cert_source = client_class.get_mtls_endpoint_and_cert_source()
        assert api_endpoint == client_class.DEFAULT_MTLS_ENDPOINT
        assert cert_source is None

    # Test the case GOOGLE_API_USE_MTLS_ENDPOINT is "auto" and default cert doesn't exist.
    with mock.patch.dict(os.environ, {"GOOGLE_API_USE_CLIENT_CERTIFICATE": "true"}):
        with mock.patch('google.auth.transport.mtls.has_default_client_cert_source', return_value=False):
            api_endpoint, cert_source = client_class.get_mtls_endpoint_and_cert_source()
            assert api_endpoint == client_class.DEFAULT_ENDPOINT
            assert cert_source is None

    # Test the case GOOGLE_API_USE_MTLS_ENDPOINT is "auto" and default cert exists.
    with mock.patch.dict(os.environ, {"GOOGLE_API_USE_CLIENT_CERTIFICATE": "true"}):
        with mock.patch('google.auth.transport.mtls.has_default_client_cert_source', return_value=True):
            with mock.patch('google.auth.transport.mtls.default_client_cert_source', return_value=mock_client_cert_source):
                api_endpoint, cert_source = client_class.get_mtls_endpoint_and_cert_source()
                assert api_endpoint == client_class.DEFAULT_MTLS_ENDPOINT
                assert cert_source == mock_client_cert_source

    # Check the case api_endpoint is not provided and GOOGLE_API_USE_MTLS_ENDPOINT has
    # unsupported value.
    with mock.patch.dict(os.environ, {"GOOGLE_API_USE_MTLS_ENDPOINT": "Unsupported"}):
        with pytest.raises(MutualTLSChannelError) as excinfo:
            client_class.get_mtls_endpoint_and_cert_source()

        assert str(excinfo.value) == "Environment variable `GOOGLE_API_USE_MTLS_ENDPOINT` must be `never`, `auto` or `always`"

    # Check the case GOOGLE_API_USE_CLIENT_CERTIFICATE has unsupported value.
    with mock.patch.dict(os.environ, {"GOOGLE_API_USE_CLIENT_CERTIFICATE": "Unsupported"}):
        with pytest.raises(ValueError) as excinfo:
            client_class.get_mtls_endpoint_and_cert_source()

        assert str(excinfo.value) == "Environment variable `GOOGLE_API_USE_CLIENT_CERTIFICATE` must be either `true` or `false`"

@pytest.mark.parametrize("client_class", [
    PageSizeDatasetServiceClient, PageSizeDatasetServiceAsyncClient
])
@mock.patch.object(PageSizeDatasetServiceClient, "_DEFAULT_ENDPOINT_TEMPLATE", modify_default_endpoint_template(PageSizeDatasetServiceClient))
@mock.patch.object(PageSizeDatasetServiceAsyncClient, "_DEFAULT_ENDPOINT_TEMPLATE", modify_default_endpoint_template(PageSizeDatasetServiceAsyncClient))
def test_page_size_dataset_service_client_client_api_endpoint(client_class):
    mock_client_cert_source = client_cert_source_callback
    api_override = "foo.com"
    default_universe = PageSizeDatasetServiceClient._DEFAULT_UNIVERSE
    default_endpoint = PageSizeDatasetServiceClient._DEFAULT_ENDPOINT_TEMPLATE.format(UNIVERSE_DOMAIN=default_universe)
    mock_universe = "bar.com"
    mock_endpoint = PageSizeDatasetServiceClient._DEFAULT_ENDPOINT_TEMPLATE.format(UNIVERSE_DOMAIN=mock_universe)

    # If ClientOptions.api_endpoint is set and GOOGLE_API_USE_CLIENT_CERTIFICATE="true",
    # use ClientOptions.api_endpoint as the api endpoint regardless.
    with mock.patch.dict(os.environ, {"GOOGLE_API_USE_CLIENT_CERTIFICATE": "true"}):
        with mock.patch("google.auth.transport.requests.AuthorizedSession.configure_mtls_channel"):
            options = client_options.ClientOptions(client_cert_source=mock_client_cert_source, api_endpoint=api_override)
            client = client_class(client_options=options, credentials=ga_credentials.AnonymousCredentials())
            assert client.api_endpoint == api_override

    # If ClientOptions.api_endpoint is not set and GOOGLE_API_USE_MTLS_ENDPOINT="never",
    # use the _DEFAULT_ENDPOINT_TEMPLATE populated with GDU as the api endpoint.
    with mock.patch.dict(os.environ, {"GOOGLE_API_USE_MTLS_ENDPOINT": "never"}):
        client = client_class(credentials=ga_credentials.AnonymousCredentials())
        assert client.api_endpoint == default_endpoint

    # If ClientOptions.api_endpoint is not set and GOOGLE_API_USE_MTLS_ENDPOINT="always",
    # use the DEFAULT_MTLS_ENDPOINT as the api endpoint.
    with mock.patch.dict(os.environ, {"GOOGLE_API_USE_MTLS_ENDPOINT": "always"}):
        client = client_class(credentials=ga_credentials.AnonymousCredentials())
        assert client.api_endpoint == client_class.DEFAULT_MTLS_ENDPOINT

    # If ClientOptions.api_endpoint is not set, GOOGLE_API_USE_MTLS_ENDPOINT="auto" (default),
    # GOOGLE_API_USE_CLIENT_CERTIFICATE="false" (default), default cert source doesn't exist,
    # and ClientOptions.universe_domain="bar.com",
    # use the _DEFAULT_ENDPOINT_TEMPLATE populated with universe domain as the api endpoint.
    options = client_options.ClientOptions()
    universe_exists = hasattr(options, "universe_domain")
    if universe_exists:
        options = client_options.ClientOptions(universe_domain=mock_universe)
        client = client_class(client_options=options, credentials=ga_credentials.AnonymousCredentials())
    else:
        client = client_class(client_options=options, credentials=ga_credentials.AnonymousCredentials())
    assert client.api_endpoint == (mock_endpoint if universe_exists else default_endpoint)
    assert client.universe_domain == (mock_universe if universe_exists else default_universe)

    # If ClientOptions does not have a universe domain attribute and GOOGLE_API_USE_MTLS_ENDPOINT="never",
    # use the _DEFAULT_ENDPOINT_TEMPLATE populated with GDU as the api endpoint.
    options = client_options.ClientOptions()
    if hasattr(options, "universe_domain"):
        delattr(options, "universe_domain")
    with mock.patch.dict(os.environ, {"GOOGLE_API_USE_MTLS_ENDPOINT": "never"}):
        client = client_class(client_options=options, credentials=ga_credentials.AnonymousCredentials())
        assert client.api_endpoint == default_endpoint


@pytest.mark.parametrize("client_class,transport_class,transport_name", [
    (PageSizeDatasetServiceClient, transports.PageSizeDatasetServiceGrpcTransport, "grpc"),
    (PageSizeDatasetServiceAsyncClient, transports.PageSizeDatasetServiceGrpcAsyncIOTransport, "grpc_asyncio"),
    (PageSizeDatasetServiceClient, transports.PageSizeDatasetServiceRestTransport, "rest"),
])
def test_page_size_dataset_service_client_client_options_scopes(client_class, transport_class, transport_name):
    # Check the case scopes are provided.
    options = client_options.ClientOptions(
        scopes=["1", "2"],
    )
    with mock.patch.object(transport_class, '__init__') as patched:
        patched.return_value = None
        client = client_class(client_options=options, transport=transport_name)
        patched.assert_called_once_with(
            credentials=None,
            credentials_file=None,
            host=client._DEFAULT_ENDPOINT_TEMPLATE.format(UNIVERSE_DOMAIN=client._DEFAULT_UNIVERSE),
            scopes=["1", "2"],
            client_cert_source_for_mtls=None,
            quota_project_id=None,
            client_info=transports.base.DEFAULT_CLIENT_INFO,
            always_use_jwt_access=True,
            api_audience=None,
        )

@pytest.mark.parametrize("client_class,transport_class,transport_name,grpc_helpers", [
    (PageSizeDatasetServiceClient, transports.PageSizeDatasetServiceGrpcTransport, "grpc", grpc_helpers),
    (PageSizeDatasetServiceAsyncClient, transports.PageSizeDatasetServiceGrpcAsyncIOTransport, "grpc_asyncio", grpc_helpers_async),
    (PageSizeDatasetServiceClient, transports.PageSizeDatasetServiceRestTransport, "rest", None),
])
def test_page_size_dataset_service_client_client_options_credentials_file(client_class, transport_class, transport_name, grpc_helpers):
    # Check the case credentials file is provided.
    options = client_options.ClientOptions(
        credentials_file="credentials.json"
    )

    with mock.patch.object(transport_class, '__init__') as patched:
        patched.return_value = None
        client = client_class(client_options=options, transport=transport_name)
        patched.assert_called_once_with(
            credentials=None,
            credentials_file="credentials.json",
            host=client._DEFAULT_ENDPOINT_TEMPLATE.format(UNIVERSE_DOMAIN=client._DEFAULT_UNIVERSE),
            scopes=None,
            client_cert_source_for_mtls=None,
            quota_project_id=None,
            client_info=transports.base.DEFAULT_CLIENT_INFO,
            always_use_jwt_access=True,
            api_audience=None,
        )

def test_page_size_dataset_service_client_client_options_from_dict():
    with mock.patch('google.fragment.services.page_size_dataset_service.transports.PageSizeDatasetServiceGrpcTransport.__init__') as grpc_transport:
        grpc_transport.return_value = None
        client = PageSizeDatasetServiceClient(
            client_options={'api_endpoint': 'squid.clam.whelk'}
        )
        grpc_transport.assert_called_once_with(
            credentials=None,
            credentials_file=None,
            host="squid.clam.whelk",
            scopes=None,
            client_cert_source_for_mtls=None,
            quota_project_id=None,
            client_info=transports.base.DEFAULT_CLIENT_INFO,
            always_use_jwt_access=True,
            api_audience=None,
        )


@pytest.mark.parametrize("client_class,transport_class,transport_name,grpc_helpers", [
    (PageSizeDatasetServiceClient, transports.PageSizeDatasetServiceGrpcTransport, "grpc", grpc_helpers),
    (PageSizeDatasetServiceAsyncClient, transports.PageSizeDatasetServiceGrpcAsyncIOTransport, "grpc_asyncio", grpc_helpers_async),
])
def test_page_size_dataset_service_client_create_channel_credentials_file(client_class, transport_class, transport_name, grpc_helpers):
    # Check the case credentials file is provided.
    options = client_options.ClientOptions(
        credentials_file="credentials.json"
    )

    with mock.patch.object(transport_class, '__init__') as patched:
        patched.return_value = None
        client = client_class(client_options=options, transport=transport_name)
        patched.assert_called_once_with(
            credentials=None,
            credentials_file="credentials.json",
            host=client._DEFAULT_ENDPOINT_TEMPLATE.format(UNIVERSE_DOMAIN=client._DEFAULT_UNIVERSE),
            scopes=None,
            client_cert_source_for_mtls=None,
            quota_project_id=None,
            client_info=transports.base.DEFAULT_CLIENT_INFO,
            always_use_jwt_access=True,
            api_audience=None,
        )

    # test that the credentials from file are saved and used as the credentials.
    with mock.patch.object(
        google.auth, "load_credentials_from_file", autospec=True
    ) as load_creds, mock.patch.object(
        google.auth, "default", autospec=True
    ) as adc, mock.patch.object(
        grpc_helpers, "create_channel"
    ) as create_channel:
        creds = ga_credentials.AnonymousCredentials()
        file_creds = ga_credentials.AnonymousCredentials()
        load_creds.return_value = (file_creds, None)
        adc.return_value = (creds, None)
        client = client_class(client_options=options, transport=transport_name)
        create_channel.assert_called_with(
            "my.example.com:443",
            credentials=file_creds,
            credentials_file=None,
            quota_project_id=None,
            default_scopes=(
),
            scopes=None,
            default_host="my.example.com",
            ssl_credentials=None,
            options=[
                ("grpc.max_send_message_length", -1),
                ("grpc.max_receive_message_length", -1),
            ],
        )


@pytest.mark.parametrize("request_type", [
  test_pagination_page_size.ListPageSizeDatasetRequest,
  dict,
])
def test_list_page_size_dataset(request_type, transport: str = 'grpc'):
    client = PageSizeDatasetServiceClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport=transport,
    )

    # Everything is optional in proto3 as far as the runtime is concerned,
    # and we are mocking out the actual API, so just send an empty request.
    request = request_type()

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(
            type(client.transport.list_page_size_dataset),
            '__call__') as call:
        # Designate an appropriate return value for the call.
        call.return_value = test_pagination_page_size.ListPageSizeDatasetResponse(
            next_page_token='next_page_token_value',
            datasets=['datasets_value'],
        )
        response = client.list_page_size_dataset(request)

        # Establish that the underlying gRPC stub method was called.
        assert len(call.mock_calls) == 1
        _, args, _ = call.mock_calls[0]
        request = test_pagination_page_size.ListPageSizeDatasetRequest()
        assert args[0] == request

    # Establish that the response is the type that we expect.
    assert isinstance(response, pagers.ListPageSizeDatasetPager)
    assert response.next_page_token == 'next_page_token_value'
    assert response.datasets == ['datasets_value']


# =========================================
def test_list_my_dataset_w_page_size_set():
    client = PageSizeDatasetServiceClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport='grpc',
    )

    # Populate all string fields in the request which are not UUID4
    # since we want to check that UUID4 are populated automatically
    # if they meet the requirements of AIP 4235.
    request = test_pagination_page_size.ListPageSizeDatasetRequest(
        page_size=4,
        page_token='page_token_value',
    )

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(
            type(client.transport.list_page_size_dataset),
            '__call__') as call:

        call.side_effect = (
            test_pagination_page_size.ListPageSizeDatasetResponse(
                datasets=[
                    "a",
                    "b",
                    "c",
                    "d",                                        
                    "e",                    
                ],
                next_page_token='abc',   
            ),
            test_pagination_page_size.ListPageSizeDatasetResponse(
                datasets=[
                    "f",
                ],
            ),
        )


        pager = client.list_page_size_dataset(request=request)
        results = list(pager)
        assert len(results) == 6
        assert all(isinstance(i, str)
            for i in results)        
        
        call.assert_called()
        _, args, _ = call.mock_calls[0]
        assert args[0] == test_pagination_page_size.ListPageSizeDatasetRequest(
            page_size=4,
            page_token='page_token_value',
        )
# =========================================



def test_list_page_size_dataset_non_empty_request_with_auto_populated_field():
    # This test is a coverage failsafe to make sure that UUID4 fields are
    # automatically populated, according to AIP-4235, with non-empty requests.
    client = PageSizeDatasetServiceClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport='grpc',
    )

    # Populate all string fields in the request which are not UUID4
    # since we want to check that UUID4 are populated automatically
    # if they meet the requirements of AIP 4235.
    request = test_pagination_page_size.ListPageSizeDatasetRequest(
        page_token='page_token_value',
    )

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(
            type(client.transport.list_page_size_dataset),
            '__call__') as call:
        call.return_value.name = "foo" # operation_request.operation in compute client(s) expect a string.
        client.list_page_size_dataset(request=request)
        call.assert_called()
        _, args, _ = call.mock_calls[0]
        assert args[0] == test_pagination_page_size.ListPageSizeDatasetRequest(
            page_token='page_token_value',
        )

def test_list_page_size_dataset_use_cached_wrapped_rpc():
    # Clients should use _prep_wrapped_messages to create cached wrapped rpcs,
    # instead of constructing them on each call
    with mock.patch("google.api_core.gapic_v1.method.wrap_method") as wrapper_fn:
        client = PageSizeDatasetServiceClient(
            credentials=ga_credentials.AnonymousCredentials(),
            transport="grpc",
        )

        # Should wrap all calls on client creation
        assert wrapper_fn.call_count > 0
        wrapper_fn.reset_mock()

        # Ensure method has been cached
        assert client._transport.list_page_size_dataset in client._transport._wrapped_methods

        # Replace cached wrapped function with mock
        mock_rpc = mock.Mock()
        mock_rpc.return_value.name = "foo" # operation_request.operation in compute client(s) expect a string.
        client._transport._wrapped_methods[client._transport.list_page_size_dataset] = mock_rpc
        request = {}
        client.list_page_size_dataset(request)

        # Establish that the underlying gRPC stub method was called.
        assert mock_rpc.call_count == 1

        client.list_page_size_dataset(request)

        # Establish that a new wrapper was not created for this call
        assert wrapper_fn.call_count == 0
        assert mock_rpc.call_count == 2

@pytest.mark.asyncio
async def test_list_page_size_dataset_async_use_cached_wrapped_rpc(transport: str = "grpc_asyncio"):
    # Clients should use _prep_wrapped_messages to create cached wrapped rpcs,
    # instead of constructing them on each call
    with mock.patch("google.api_core.gapic_v1.method_async.wrap_method") as wrapper_fn:
        client = PageSizeDatasetServiceAsyncClient(
            credentials=async_anonymous_credentials(),
            transport=transport,
        )

        # Should wrap all calls on client creation
        assert wrapper_fn.call_count > 0
        wrapper_fn.reset_mock()

        # Ensure method has been cached
        assert client._client._transport.list_page_size_dataset in client._client._transport._wrapped_methods

        # Replace cached wrapped function with mock
        mock_rpc = mock.AsyncMock()
        mock_rpc.return_value = mock.Mock()
        client._client._transport._wrapped_methods[client._client._transport.list_page_size_dataset] = mock_rpc

        request = {}
        await client.list_page_size_dataset(request)

        # Establish that the underlying gRPC stub method was called.
        assert mock_rpc.call_count == 1

        await client.list_page_size_dataset(request)

        # Establish that a new wrapper was not created for this call
        assert wrapper_fn.call_count == 0
        assert mock_rpc.call_count == 2

@pytest.mark.asyncio
async def test_list_page_size_dataset_async(transport: str = 'grpc_asyncio', request_type=test_pagination_page_size.ListPageSizeDatasetRequest):
    client = PageSizeDatasetServiceAsyncClient(
        credentials=async_anonymous_credentials(),
        transport=transport,
    )

    # Everything is optional in proto3 as far as the runtime is concerned,
    # and we are mocking out the actual API, so just send an empty request.
    request = request_type()

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(
            type(client.transport.list_page_size_dataset),
            '__call__') as call:
        # Designate an appropriate return value for the call.
        call.return_value =grpc_helpers_async.FakeUnaryUnaryCall(test_pagination_page_size.ListPageSizeDatasetResponse(
            next_page_token='next_page_token_value',
            datasets=['datasets_value'],
        ))
        response = await client.list_page_size_dataset(request)

        # Establish that the underlying gRPC stub method was called.
        assert len(call.mock_calls)
        _, args, _ = call.mock_calls[0]
        request = test_pagination_page_size.ListPageSizeDatasetRequest()
        assert args[0] == request

    # Establish that the response is the type that we expect.
    assert isinstance(response, pagers.ListPageSizeDatasetAsyncPager)
    assert response.next_page_token == 'next_page_token_value'
    assert response.datasets == ['datasets_value']


@pytest.mark.asyncio
async def test_list_page_size_dataset_async_from_dict():
    await test_list_page_size_dataset_async(request_type=dict)


def test_list_page_size_dataset_pager(transport_name: str = "grpc"):
    client = PageSizeDatasetServiceClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport=transport_name,
    )

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(
            type(client.transport.list_page_size_dataset),
            '__call__') as call:
        # Set the response to a series of pages.
        call.side_effect = (
            test_pagination_page_size.ListPageSizeDatasetResponse(
                datasets=[
                    str(),
                    str(),
                    str(),
                ],
                next_page_token='abc',
            ),
            test_pagination_page_size.ListPageSizeDatasetResponse(
                datasets=[],
                next_page_token='def',
            ),
            test_pagination_page_size.ListPageSizeDatasetResponse(
                datasets=[
                    str(),
                ],
                next_page_token='ghi',
            ),
            test_pagination_page_size.ListPageSizeDatasetResponse(
                datasets=[
                    str(),
                    str(),
                ],
            ),
            RuntimeError,
        )

        expected_metadata = ()
        retry = retries.Retry()
        timeout = 5
        pager = client.list_page_size_dataset(request={}, retry=retry, timeout=timeout)

        assert pager._metadata == expected_metadata
        assert pager._retry == retry
        assert pager._timeout == timeout

        results = list(pager)
        assert len(results) == 6
        assert all(isinstance(i, str)
                   for i in results)
def test_list_page_size_dataset_pages(transport_name: str = "grpc"):
    client = PageSizeDatasetServiceClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport=transport_name,
    )

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(
            type(client.transport.list_page_size_dataset),
            '__call__') as call:
        # Set the response to a series of pages.
        call.side_effect = (
            test_pagination_page_size.ListPageSizeDatasetResponse(
                datasets=[
                    str(),
                    str(),
                    str(),
                ],
                next_page_token='abc',
            ),
            test_pagination_page_size.ListPageSizeDatasetResponse(
                datasets=[],
                next_page_token='def',
            ),
            test_pagination_page_size.ListPageSizeDatasetResponse(
                datasets=[
                    str(),
                ],
                next_page_token='ghi',
            ),
            test_pagination_page_size.ListPageSizeDatasetResponse(
                datasets=[
                    str(),
                    str(),
                ],
            ),
            RuntimeError,
        )
        pages = list(client.list_page_size_dataset(request={}).pages)
        for page_, token in zip(pages, ['abc','def','ghi', '']):
            assert page_.raw_page.next_page_token == token

@pytest.mark.asyncio
async def test_list_page_size_dataset_async_pager():
    client = PageSizeDatasetServiceAsyncClient(
        credentials=async_anonymous_credentials(),
    )

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(
            type(client.transport.list_page_size_dataset),
            '__call__', new_callable=mock.AsyncMock) as call:
        # Set the response to a series of pages.
        call.side_effect = (
            test_pagination_page_size.ListPageSizeDatasetResponse(
                datasets=[
                    str(),
                    str(),
                    str(),
                ],
                next_page_token='abc',
            ),
            test_pagination_page_size.ListPageSizeDatasetResponse(
                datasets=[],
                next_page_token='def',
            ),
            test_pagination_page_size.ListPageSizeDatasetResponse(
                datasets=[
                    str(),
                ],
                next_page_token='ghi',
            ),
            test_pagination_page_size.ListPageSizeDatasetResponse(
                datasets=[
                    str(),
                    str(),
                ],
            ),
            RuntimeError,
        )
        async_pager = await client.list_page_size_dataset(request={},)
        assert async_pager.next_page_token == 'abc'
        responses = []
        async for response in async_pager: # pragma: no branch
            responses.append(response)

        assert len(responses) == 6
        assert all(isinstance(i, str)
                for i in responses)


@pytest.mark.asyncio
async def test_list_page_size_dataset_async_pages():
    client = PageSizeDatasetServiceAsyncClient(
        credentials=async_anonymous_credentials(),
    )

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(
            type(client.transport.list_page_size_dataset),
            '__call__', new_callable=mock.AsyncMock) as call:
        # Set the response to a series of pages.
        call.side_effect = (
            test_pagination_page_size.ListPageSizeDatasetResponse(
                datasets=[
                    str(),
                    str(),
                    str(),
                ],
                next_page_token='abc',
            ),
            test_pagination_page_size.ListPageSizeDatasetResponse(
                datasets=[],
                next_page_token='def',
            ),
            test_pagination_page_size.ListPageSizeDatasetResponse(
                datasets=[
                    str(),
                ],
                next_page_token='ghi',
            ),
            test_pagination_page_size.ListPageSizeDatasetResponse(
                datasets=[
                    str(),
                    str(),
                ],
            ),
            RuntimeError,
        )
        pages = []
        # Workaround issue in python 3.9 related to code coverage by adding `# pragma: no branch`
        # See https://github.com/googleapis/gapic-generator-python/pull/1174#issuecomment-1025132372
        async for page_ in ( # pragma: no branch
            await client.list_page_size_dataset(request={})
        ).pages:
            pages.append(page_)
        for page_, token in zip(pages, ['abc','def','ghi', '']):
            assert page_.raw_page.next_page_token == token


def test_list_page_size_dataset_rest_no_http_options():
    client = PageSizeDatasetServiceClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport="rest",
    )
    request = test_pagination_page_size.ListPageSizeDatasetRequest()
    with pytest.raises(RuntimeError):
        client.list_page_size_dataset(request)


def test_list_page_size_dataset_rest_error():
    client = PageSizeDatasetServiceClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport='rest'
    )
    # Since a `google.api.http` annotation is required for using a rest transport
    # method, this should error.
    with pytest.raises(NotImplementedError) as not_implemented_error:
        client.list_page_size_dataset({})
    assert (
        "Method ListPageSizeDataset is not available over REST transport"
        in str(not_implemented_error.value)
    )


def test_credentials_transport_error():
    # It is an error to provide credentials and a transport instance.
    transport = transports.PageSizeDatasetServiceGrpcTransport(
        credentials=ga_credentials.AnonymousCredentials(),
    )
    with pytest.raises(ValueError):
        client = PageSizeDatasetServiceClient(
            credentials=ga_credentials.AnonymousCredentials(),
            transport=transport,
        )

    # It is an error to provide a credentials file and a transport instance.
    transport = transports.PageSizeDatasetServiceGrpcTransport(
        credentials=ga_credentials.AnonymousCredentials(),
    )
    with pytest.raises(ValueError):
        client = PageSizeDatasetServiceClient(
            client_options={"credentials_file": "credentials.json"},
            transport=transport,
        )

    # It is an error to provide an api_key and a transport instance.
    transport = transports.PageSizeDatasetServiceGrpcTransport(
        credentials=ga_credentials.AnonymousCredentials(),
    )
    options = client_options.ClientOptions()
    options.api_key = "api_key"
    with pytest.raises(ValueError):
        client = PageSizeDatasetServiceClient(
            client_options=options,
            transport=transport,
        )

    # It is an error to provide an api_key and a credential.
    options = client_options.ClientOptions()
    options.api_key = "api_key"
    with pytest.raises(ValueError):
        client = PageSizeDatasetServiceClient(
            client_options=options,
            credentials=ga_credentials.AnonymousCredentials()
        )

    # It is an error to provide scopes and a transport instance.
    transport = transports.PageSizeDatasetServiceGrpcTransport(
        credentials=ga_credentials.AnonymousCredentials(),
    )
    with pytest.raises(ValueError):
        client = PageSizeDatasetServiceClient(
            client_options={"scopes": ["1", "2"]},
            transport=transport,
        )


def test_transport_instance():
    # A client may be instantiated with a custom transport instance.
    transport = transports.PageSizeDatasetServiceGrpcTransport(
        credentials=ga_credentials.AnonymousCredentials(),
    )
    client = PageSizeDatasetServiceClient(transport=transport)
    assert client.transport is transport

def test_transport_get_channel():
    # A client may be instantiated with a custom transport instance.
    transport = transports.PageSizeDatasetServiceGrpcTransport(
        credentials=ga_credentials.AnonymousCredentials(),
    )
    channel = transport.grpc_channel
    assert channel

    transport = transports.PageSizeDatasetServiceGrpcAsyncIOTransport(
        credentials=ga_credentials.AnonymousCredentials(),
    )
    channel = transport.grpc_channel
    assert channel

@pytest.mark.parametrize("transport_class", [
    transports.PageSizeDatasetServiceGrpcTransport,
    transports.PageSizeDatasetServiceGrpcAsyncIOTransport,
    transports.PageSizeDatasetServiceRestTransport,
])
def test_transport_adc(transport_class):
    # Test default credentials are used if not provided.
    with mock.patch.object(google.auth, 'default') as adc:
        adc.return_value = (ga_credentials.AnonymousCredentials(), None)
        transport_class()
        adc.assert_called_once()

def test_transport_kind_grpc():
    transport = PageSizeDatasetServiceClient.get_transport_class("grpc")(
        credentials=ga_credentials.AnonymousCredentials()
    )
    assert transport.kind == "grpc"


def test_initialize_client_w_grpc():
    client = PageSizeDatasetServiceClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport="grpc"
    )
    assert client is not None


# This test is a coverage failsafe to make sure that totally empty calls,
# i.e. request == None and no flattened fields passed, work.
def test_list_page_size_dataset_empty_call_grpc():
    client = PageSizeDatasetServiceClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport="grpc",
    )

    # Mock the actual call, and fake the request.
    with mock.patch.object(
            type(client.transport.list_page_size_dataset),
            '__call__') as call:
        call.return_value = test_pagination_page_size.ListPageSizeDatasetResponse()
        client.list_page_size_dataset(request=None)

        # Establish that the underlying stub method was called.
        call.assert_called()
        _, args, _ = call.mock_calls[0]
        request_msg = test_pagination_page_size.ListPageSizeDatasetRequest()

        assert args[0] == request_msg


def test_transport_kind_grpc_asyncio():
    transport = PageSizeDatasetServiceAsyncClient.get_transport_class("grpc_asyncio")(
        credentials=async_anonymous_credentials()
    )
    assert transport.kind == "grpc_asyncio"


def test_initialize_client_w_grpc_asyncio():
    client = PageSizeDatasetServiceAsyncClient(
        credentials=async_anonymous_credentials(),
        transport="grpc_asyncio"
    )
    assert client is not None


# This test is a coverage failsafe to make sure that totally empty calls,
# i.e. request == None and no flattened fields passed, work.
@pytest.mark.asyncio
async def test_list_page_size_dataset_empty_call_grpc_asyncio():
    client = PageSizeDatasetServiceAsyncClient(
        credentials=async_anonymous_credentials(),
        transport="grpc_asyncio",
    )

    # Mock the actual call, and fake the request.
    with mock.patch.object(
            type(client.transport.list_page_size_dataset),
            '__call__') as call:
        # Designate an appropriate return value for the call.
        call.return_value = grpc_helpers_async.FakeUnaryUnaryCall(test_pagination_page_size.ListPageSizeDatasetResponse(
            next_page_token='next_page_token_value',
            datasets=['datasets_value'],
        ))
        await client.list_page_size_dataset(request=None)

        # Establish that the underlying stub method was called.
        call.assert_called()
        _, args, _ = call.mock_calls[0]
        request_msg = test_pagination_page_size.ListPageSizeDatasetRequest()

        assert args[0] == request_msg


def test_transport_kind_rest():
    transport = PageSizeDatasetServiceClient.get_transport_class("rest")(
        credentials=ga_credentials.AnonymousCredentials()
    )
    assert transport.kind == "rest"


def test_list_page_size_dataset_rest_error():

    client = PageSizeDatasetServiceClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport="rest"
    )

    with pytest.raises(NotImplementedError) as not_implemented_error:
        client.list_page_size_dataset({})
    assert (
        "Method ListPageSizeDataset is not available over REST transport"
        in str(not_implemented_error.value)
    )


def test_initialize_client_w_rest():
    client = PageSizeDatasetServiceClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport="rest"
    )
    assert client is not None


# This test is a coverage failsafe to make sure that totally empty calls,
# i.e. request == None and no flattened fields passed, work.
def test_list_page_size_dataset_empty_call_rest():
    client = PageSizeDatasetServiceClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport="rest",
    )

    # Mock the actual call, and fake the request.
    with mock.patch.object(
            type(client.transport.list_page_size_dataset),
            '__call__') as call:
        client.list_page_size_dataset(request=None)

        # Establish that the underlying stub method was called.
        call.assert_called()
        _, args, _ = call.mock_calls[0]
        request_msg = test_pagination_page_size.ListPageSizeDatasetRequest()

        assert args[0] == request_msg


def test_transport_grpc_default():
    # A client should use the gRPC transport by default.
    client = PageSizeDatasetServiceClient(
        credentials=ga_credentials.AnonymousCredentials(),
    )
    assert isinstance(
        client.transport,
        transports.PageSizeDatasetServiceGrpcTransport,
    )

def test_page_size_dataset_service_base_transport_error():
    # Passing both a credentials object and credentials_file should raise an error
    with pytest.raises(core_exceptions.DuplicateCredentialArgs):
        transport = transports.PageSizeDatasetServiceTransport(
            credentials=ga_credentials.AnonymousCredentials(),
            credentials_file="credentials.json"
        )


def test_page_size_dataset_service_base_transport():
    # Instantiate the base transport.
    with mock.patch('google.fragment.services.page_size_dataset_service.transports.PageSizeDatasetServiceTransport.__init__') as Transport:
        Transport.return_value = None
        transport = transports.PageSizeDatasetServiceTransport(
            credentials=ga_credentials.AnonymousCredentials(),
        )

    # Every method on the transport should just blindly
    # raise NotImplementedError.
    methods = (
        'list_page_size_dataset',
    )
    for method in methods:
        with pytest.raises(NotImplementedError):
            getattr(transport, method)(request=object())

    with pytest.raises(NotImplementedError):
        transport.close()

    # Catch all for all remaining methods and properties
    remainder = [
        'kind',
    ]
    for r in remainder:
        with pytest.raises(NotImplementedError):
            getattr(transport, r)()


def test_page_size_dataset_service_base_transport_with_credentials_file():
    # Instantiate the base transport with a credentials file
    with mock.patch.object(google.auth, 'load_credentials_from_file', autospec=True) as load_creds, mock.patch('google.fragment.services.page_size_dataset_service.transports.PageSizeDatasetServiceTransport._prep_wrapped_messages') as Transport:
        Transport.return_value = None
        load_creds.return_value = (ga_credentials.AnonymousCredentials(), None)
        transport = transports.PageSizeDatasetServiceTransport(
            credentials_file="credentials.json",
            quota_project_id="octopus",
        )
        load_creds.assert_called_once_with("credentials.json",
            scopes=None,
            default_scopes=(
),
            quota_project_id="octopus",
        )


def test_page_size_dataset_service_base_transport_with_adc():
    # Test the default credentials are used if credentials and credentials_file are None.
    with mock.patch.object(google.auth, 'default', autospec=True) as adc, mock.patch('google.fragment.services.page_size_dataset_service.transports.PageSizeDatasetServiceTransport._prep_wrapped_messages') as Transport:
        Transport.return_value = None
        adc.return_value = (ga_credentials.AnonymousCredentials(), None)
        transport = transports.PageSizeDatasetServiceTransport()
        adc.assert_called_once()


def test_page_size_dataset_service_auth_adc():
    # If no credentials are provided, we should use ADC credentials.
    with mock.patch.object(google.auth, 'default', autospec=True) as adc:
        adc.return_value = (ga_credentials.AnonymousCredentials(), None)
        PageSizeDatasetServiceClient()
        adc.assert_called_once_with(
            scopes=None,
            default_scopes=(
),
            quota_project_id=None,
        )


@pytest.mark.parametrize(
    "transport_class",
    [
        transports.PageSizeDatasetServiceGrpcTransport,
        transports.PageSizeDatasetServiceGrpcAsyncIOTransport,
    ],
)
def test_page_size_dataset_service_transport_auth_adc(transport_class):
    # If credentials and host are not provided, the transport class should use
    # ADC credentials.
    with mock.patch.object(google.auth, 'default', autospec=True) as adc:
        adc.return_value = (ga_credentials.AnonymousCredentials(), None)
        transport_class(quota_project_id="octopus", scopes=["1", "2"])
        adc.assert_called_once_with(
            scopes=["1", "2"],
            default_scopes=(),
            quota_project_id="octopus",
        )


@pytest.mark.parametrize(
    "transport_class",
    [
        transports.PageSizeDatasetServiceGrpcTransport,
        transports.PageSizeDatasetServiceGrpcAsyncIOTransport,
        transports.PageSizeDatasetServiceRestTransport,
    ],
)
def test_page_size_dataset_service_transport_auth_gdch_credentials(transport_class):
    host = 'https://language.com'
    api_audience_tests = [None, 'https://language2.com']
    api_audience_expect = [host, 'https://language2.com']
    for t, e in zip(api_audience_tests, api_audience_expect):
        with mock.patch.object(google.auth, 'default', autospec=True) as adc:
            gdch_mock = mock.MagicMock()
            type(gdch_mock).with_gdch_audience = mock.PropertyMock(return_value=gdch_mock)
            adc.return_value = (gdch_mock, None)
            transport_class(host=host, api_audience=t)
            gdch_mock.with_gdch_audience.assert_called_once_with(
                e
            )


@pytest.mark.parametrize(
    "transport_class,grpc_helpers",
    [
        (transports.PageSizeDatasetServiceGrpcTransport, grpc_helpers),
        (transports.PageSizeDatasetServiceGrpcAsyncIOTransport, grpc_helpers_async)
    ],
)
def test_page_size_dataset_service_transport_create_channel(transport_class, grpc_helpers):
    # If credentials and host are not provided, the transport class should use
    # ADC credentials.
    with mock.patch.object(google.auth, "default", autospec=True) as adc, mock.patch.object(
        grpc_helpers, "create_channel", autospec=True
    ) as create_channel:
        creds = ga_credentials.AnonymousCredentials()
        adc.return_value = (creds, None)
        transport_class(
            quota_project_id="octopus",
            scopes=["1", "2"]
        )

        create_channel.assert_called_with(
            "my.example.com:443",
            credentials=creds,
            credentials_file=None,
            quota_project_id="octopus",
            default_scopes=(
),
            scopes=["1", "2"],
            default_host="my.example.com",
            ssl_credentials=None,
            options=[
                ("grpc.max_send_message_length", -1),
                ("grpc.max_receive_message_length", -1),
            ],
        )


@pytest.mark.parametrize("transport_class", [transports.PageSizeDatasetServiceGrpcTransport, transports.PageSizeDatasetServiceGrpcAsyncIOTransport])
def test_page_size_dataset_service_grpc_transport_client_cert_source_for_mtls(
    transport_class
):
    cred = ga_credentials.AnonymousCredentials()

    # Check ssl_channel_credentials is used if provided.
    with mock.patch.object(transport_class, "create_channel") as mock_create_channel:
        mock_ssl_channel_creds = mock.Mock()
        transport_class(
            host="squid.clam.whelk",
            credentials=cred,
            ssl_channel_credentials=mock_ssl_channel_creds
        )
        mock_create_channel.assert_called_once_with(
            "squid.clam.whelk:443",
            credentials=cred,
            credentials_file=None,
            scopes=None,
            ssl_credentials=mock_ssl_channel_creds,
            quota_project_id=None,
            options=[
                ("grpc.max_send_message_length", -1),
                ("grpc.max_receive_message_length", -1),
            ],
        )

    # Check if ssl_channel_credentials is not provided, then client_cert_source_for_mtls
    # is used.
    with mock.patch.object(transport_class, "create_channel", return_value=mock.Mock()):
        with mock.patch("grpc.ssl_channel_credentials") as mock_ssl_cred:
            transport_class(
                credentials=cred,
                client_cert_source_for_mtls=client_cert_source_callback
            )
            expected_cert, expected_key = client_cert_source_callback()
            mock_ssl_cred.assert_called_once_with(
                certificate_chain=expected_cert,
                private_key=expected_key
            )

def test_page_size_dataset_service_http_transport_client_cert_source_for_mtls():
    cred = ga_credentials.AnonymousCredentials()
    with mock.patch("google.auth.transport.requests.AuthorizedSession.configure_mtls_channel") as mock_configure_mtls_channel:
        transports.PageSizeDatasetServiceRestTransport (
            credentials=cred,
            client_cert_source_for_mtls=client_cert_source_callback
        )
        mock_configure_mtls_channel.assert_called_once_with(client_cert_source_callback)


@pytest.mark.parametrize("transport_name", [
    "grpc",
    "grpc_asyncio",
    "rest",
])
def test_page_size_dataset_service_host_no_port(transport_name):
    client = PageSizeDatasetServiceClient(
        credentials=ga_credentials.AnonymousCredentials(),
        client_options=client_options.ClientOptions(api_endpoint='my.example.com'),
         transport=transport_name,
    )
    assert client.transport._host == (
        'my.example.com:443'
        if transport_name in ['grpc', 'grpc_asyncio']
        else 'https://my.example.com'
    )

@pytest.mark.parametrize("transport_name", [
    "grpc",
    "grpc_asyncio",
    "rest",
])
def test_page_size_dataset_service_host_with_port(transport_name):
    client = PageSizeDatasetServiceClient(
        credentials=ga_credentials.AnonymousCredentials(),
        client_options=client_options.ClientOptions(api_endpoint='my.example.com:8000'),
        transport=transport_name,
    )
    assert client.transport._host == (
        'my.example.com:8000'
        if transport_name in ['grpc', 'grpc_asyncio']
        else 'https://my.example.com:8000'
    )

@pytest.mark.parametrize("transport_name", [
    "rest",
])
def test_page_size_dataset_service_client_transport_session_collision(transport_name):
    creds1 = ga_credentials.AnonymousCredentials()
    creds2 = ga_credentials.AnonymousCredentials()
    client1 = PageSizeDatasetServiceClient(
        credentials=creds1,
        transport=transport_name,
    )
    client2 = PageSizeDatasetServiceClient(
        credentials=creds2,
        transport=transport_name,
    )
    session1 = client1.transport.list_page_size_dataset._session
    session2 = client2.transport.list_page_size_dataset._session
    assert session1 != session2
def test_page_size_dataset_service_grpc_transport_channel():
    channel = grpc.secure_channel('http://localhost/', grpc.local_channel_credentials())

    # Check that channel is used if provided.
    transport = transports.PageSizeDatasetServiceGrpcTransport(
        host="squid.clam.whelk",
        channel=channel,
    )
    assert transport.grpc_channel == channel
    assert transport._host == "squid.clam.whelk:443"
    assert transport._ssl_channel_credentials == None


def test_page_size_dataset_service_grpc_asyncio_transport_channel():
    channel = aio.secure_channel('http://localhost/', grpc.local_channel_credentials())

    # Check that channel is used if provided.
    transport = transports.PageSizeDatasetServiceGrpcAsyncIOTransport(
        host="squid.clam.whelk",
        channel=channel,
    )
    assert transport.grpc_channel == channel
    assert transport._host == "squid.clam.whelk:443"
    assert transport._ssl_channel_credentials == None


# Remove this test when deprecated arguments (api_mtls_endpoint, client_cert_source) are
# removed from grpc/grpc_asyncio transport constructor.
@pytest.mark.parametrize("transport_class", [transports.PageSizeDatasetServiceGrpcTransport, transports.PageSizeDatasetServiceGrpcAsyncIOTransport])
def test_page_size_dataset_service_transport_channel_mtls_with_client_cert_source(
    transport_class
):
    with mock.patch("grpc.ssl_channel_credentials", autospec=True) as grpc_ssl_channel_cred:
        with mock.patch.object(transport_class, "create_channel") as grpc_create_channel:
            mock_ssl_cred = mock.Mock()
            grpc_ssl_channel_cred.return_value = mock_ssl_cred

            mock_grpc_channel = mock.Mock()
            grpc_create_channel.return_value = mock_grpc_channel

            cred = ga_credentials.AnonymousCredentials()
            with pytest.warns(DeprecationWarning):
                with mock.patch.object(google.auth, 'default') as adc:
                    adc.return_value = (cred, None)
                    transport = transport_class(
                        host="squid.clam.whelk",
                        api_mtls_endpoint="mtls.squid.clam.whelk",
                        client_cert_source=client_cert_source_callback,
                    )
                    adc.assert_called_once()

            grpc_ssl_channel_cred.assert_called_once_with(
                certificate_chain=b"cert bytes", private_key=b"key bytes"
            )
            grpc_create_channel.assert_called_once_with(
                "mtls.squid.clam.whelk:443",
                credentials=cred,
                credentials_file=None,
                scopes=None,
                ssl_credentials=mock_ssl_cred,
                quota_project_id=None,
                options=[
                    ("grpc.max_send_message_length", -1),
                    ("grpc.max_receive_message_length", -1),
                ],
            )
            assert transport.grpc_channel == mock_grpc_channel
            assert transport._ssl_channel_credentials == mock_ssl_cred


# Remove this test when deprecated arguments (api_mtls_endpoint, client_cert_source) are
# removed from grpc/grpc_asyncio transport constructor.
@pytest.mark.parametrize("transport_class", [transports.PageSizeDatasetServiceGrpcTransport, transports.PageSizeDatasetServiceGrpcAsyncIOTransport])
def test_page_size_dataset_service_transport_channel_mtls_with_adc(
    transport_class
):
    mock_ssl_cred = mock.Mock()
    with mock.patch.multiple(
        "google.auth.transport.grpc.SslCredentials",
        __init__=mock.Mock(return_value=None),
        ssl_credentials=mock.PropertyMock(return_value=mock_ssl_cred),
    ):
        with mock.patch.object(transport_class, "create_channel") as grpc_create_channel:
            mock_grpc_channel = mock.Mock()
            grpc_create_channel.return_value = mock_grpc_channel
            mock_cred = mock.Mock()

            with pytest.warns(DeprecationWarning):
                transport = transport_class(
                    host="squid.clam.whelk",
                    credentials=mock_cred,
                    api_mtls_endpoint="mtls.squid.clam.whelk",
                    client_cert_source=None,
                )

            grpc_create_channel.assert_called_once_with(
                "mtls.squid.clam.whelk:443",
                credentials=mock_cred,
                credentials_file=None,
                scopes=None,
                ssl_credentials=mock_ssl_cred,
                quota_project_id=None,
                options=[
                    ("grpc.max_send_message_length", -1),
                    ("grpc.max_receive_message_length", -1),
                ],
            )
            assert transport.grpc_channel == mock_grpc_channel


def test_common_billing_account_path():
    billing_account = "squid"
    expected = "billingAccounts/{billing_account}".format(billing_account=billing_account, )
    actual = PageSizeDatasetServiceClient.common_billing_account_path(billing_account)
    assert expected == actual


def test_parse_common_billing_account_path():
    expected = {
        "billing_account": "clam",
    }
    path = PageSizeDatasetServiceClient.common_billing_account_path(**expected)

    # Check that the path construction is reversible.
    actual = PageSizeDatasetServiceClient.parse_common_billing_account_path(path)
    assert expected == actual

def test_common_folder_path():
    folder = "whelk"
    expected = "folders/{folder}".format(folder=folder, )
    actual = PageSizeDatasetServiceClient.common_folder_path(folder)
    assert expected == actual


def test_parse_common_folder_path():
    expected = {
        "folder": "octopus",
    }
    path = PageSizeDatasetServiceClient.common_folder_path(**expected)

    # Check that the path construction is reversible.
    actual = PageSizeDatasetServiceClient.parse_common_folder_path(path)
    assert expected == actual

def test_common_organization_path():
    organization = "oyster"
    expected = "organizations/{organization}".format(organization=organization, )
    actual = PageSizeDatasetServiceClient.common_organization_path(organization)
    assert expected == actual


def test_parse_common_organization_path():
    expected = {
        "organization": "nudibranch",
    }
    path = PageSizeDatasetServiceClient.common_organization_path(**expected)

    # Check that the path construction is reversible.
    actual = PageSizeDatasetServiceClient.parse_common_organization_path(path)
    assert expected == actual

def test_common_project_path():
    project = "cuttlefish"
    expected = "projects/{project}".format(project=project, )
    actual = PageSizeDatasetServiceClient.common_project_path(project)
    assert expected == actual


def test_parse_common_project_path():
    expected = {
        "project": "mussel",
    }
    path = PageSizeDatasetServiceClient.common_project_path(**expected)

    # Check that the path construction is reversible.
    actual = PageSizeDatasetServiceClient.parse_common_project_path(path)
    assert expected == actual

def test_common_location_path():
    project = "winkle"
    location = "nautilus"
    expected = "projects/{project}/locations/{location}".format(project=project, location=location, )
    actual = PageSizeDatasetServiceClient.common_location_path(project, location)
    assert expected == actual


def test_parse_common_location_path():
    expected = {
        "project": "scallop",
        "location": "abalone",
    }
    path = PageSizeDatasetServiceClient.common_location_path(**expected)

    # Check that the path construction is reversible.
    actual = PageSizeDatasetServiceClient.parse_common_location_path(path)
    assert expected == actual


def test_client_with_default_client_info():
    client_info = gapic_v1.client_info.ClientInfo()

    with mock.patch.object(transports.PageSizeDatasetServiceTransport, '_prep_wrapped_messages') as prep:
        client = PageSizeDatasetServiceClient(
            credentials=ga_credentials.AnonymousCredentials(),
            client_info=client_info,
        )
        prep.assert_called_once_with(client_info)

    with mock.patch.object(transports.PageSizeDatasetServiceTransport, '_prep_wrapped_messages') as prep:
        transport_class = PageSizeDatasetServiceClient.get_transport_class()
        transport = transport_class(
            credentials=ga_credentials.AnonymousCredentials(),
            client_info=client_info,
        )
        prep.assert_called_once_with(client_info)


def test_transport_close_grpc():
    client = PageSizeDatasetServiceClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport="grpc"
    )
    with mock.patch.object(type(getattr(client.transport, "_grpc_channel")), "close") as close:
        with client:
            close.assert_not_called()
        close.assert_called_once()


@pytest.mark.asyncio
async def test_transport_close_grpc_asyncio():
    client = PageSizeDatasetServiceAsyncClient(
        credentials=async_anonymous_credentials(),
        transport="grpc_asyncio"
    )
    with mock.patch.object(type(getattr(client.transport, "_grpc_channel")), "close") as close:
        async with client:
            close.assert_not_called()
        close.assert_called_once()


def test_transport_close_rest():
    client = PageSizeDatasetServiceClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport="rest"
    )
    with mock.patch.object(type(getattr(client.transport, "_session")), "close") as close:
        with client:
            close.assert_not_called()
        close.assert_called_once()


def test_client_ctx():
    transports = [
        'rest',
        'grpc',
    ]
    for transport in transports:
        client = PageSizeDatasetServiceClient(
            credentials=ga_credentials.AnonymousCredentials(),
            transport=transport
        )
        # Test client calls underlying transport.
        with mock.patch.object(type(client.transport), "close") as close:
            close.assert_not_called()
            with client:
                pass
            close.assert_called()

@pytest.mark.parametrize("client_class,transport_class", [
    (PageSizeDatasetServiceClient, transports.PageSizeDatasetServiceGrpcTransport),
    (PageSizeDatasetServiceAsyncClient, transports.PageSizeDatasetServiceGrpcAsyncIOTransport),
])
def test_api_key_credentials(client_class, transport_class):
    with mock.patch.object(
        google.auth._default, "get_api_key_credentials", create=True
    ) as get_api_key_credentials:
        mock_cred = mock.Mock()
        get_api_key_credentials.return_value = mock_cred
        options = client_options.ClientOptions()
        options.api_key = "api_key"
        with mock.patch.object(transport_class, "__init__") as patched:
            patched.return_value = None
            client = client_class(client_options=options)
            patched.assert_called_once_with(
                credentials=mock_cred,
                credentials_file=None,
                host=client._DEFAULT_ENDPOINT_TEMPLATE.format(UNIVERSE_DOMAIN=client._DEFAULT_UNIVERSE),
                scopes=None,
                client_cert_source_for_mtls=None,
                quota_project_id=None,
                client_info=transports.base.DEFAULT_CLIENT_INFO,
                always_use_jwt_access=True,
                api_audience=None,
            )

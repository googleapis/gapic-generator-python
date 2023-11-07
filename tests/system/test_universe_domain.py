import os
import pytest

from google.api_core import exceptions
from google.rpc import code_pb2

from google.auth import credentials
from google.showcase import EchoClient
from google.api_core import client_options as client_options_lib
from unittest import mock


def modify_default_endpoint_template(client):
    return "dummy.{UNIVERSE_DOMAIN}" if ("localhost" in client.DEFAULT_ENDPOINT_TEMPLATE) else client.DEFAULT_ENDPOINT_TEMPLATE



@mock.patch.object(EchoClient, "DEFAULT_ENDPOINT_TEMPLATE", modify_default_endpoint_template(EchoClient))
def test_echo_client_get_mtls_endpoint_and_cert_source():
    mock_client_cert_source = mock.Mock()
    client_options = client_options_lib.ClientOptions(client_cert_source=mock_client_cert_source, universe_domain="foo.com")
    client = EchoClient()
    api_endpoint, _ = client.get_mtls_endpoint_and_cert_source(client_options)
    assert api_endpoint == "dummy.foo.com"




@mock.patch.object(EchoClient, "DEFAULT_ENDPOINT_TEMPLATE", modify_default_endpoint_template(EchoClient))
def test_universe_domain_populates_host():
    mock_client_cert_source = mock.Mock()
    client_options = client_options_lib.ClientOptions(client_cert_source=mock_client_cert_source, universe_domain="foo.com")
    client = EchoClient(client_options=client_options)
    assert client.transport._host == "dummy.foo.com:443"
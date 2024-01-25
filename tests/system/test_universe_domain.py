import pytest

import grpc

# We are not able to stack multiple dimensions of
# `@pytest.mark.parametrize` for multiple parameters in the tests that
# follow, so we flatten each combination of parameter values into a
# single EchoParams object with multiple attributes, and parametrize
# the test only on EchoParams.


class EchoParams(object):
    def setattrs(self, **kwargs):
        for k, v in kwargs.items():
            setattr(self, k, v)
        return self

# What we'd like for the following test is:
#    @pytest.mark.parametrize("channel_creator", [grpc.insecure_channel])
#    @pytest.mark.parametrize("transport_name",["grpc","rest"])


def vary_transport():
    for transport_name in ["grpc", "rest"]:
        params = EchoParams()
        params.setattrs(
            channel_creator=grpc.insecure_channel,
            transport_name=transport_name,
            transport_endpoint="localhost:7469",
            credential_universe="googleapis.com",
            client_universe="googleapis.com"
        )
        yield params


@pytest.mark.parametrize("test_params", vary_transport())
def test_universe_domain_validation_pass(parametrized_echo, test_params):
    # Test that only the configured client universe and credentials universe are used for validation
    assert parametrized_echo.universe_domain == test_params.client_universe
    assert parametrized_echo.transport._credentials._universe_domain == test_params.credential_universe
    if test_params.transport_name == "rest":
        assert parametrized_echo.api_endpoint == "http://" + test_params.transport_endpoint
    else:
        assert parametrized_echo.api_endpoint == test_params.transport_endpoint
    response = parametrized_echo.echo({
        'content': 'Universe validation succeeded!'
        })
    assert response.content == "Universe validation succeeded!"


# What we'd like to do for the following test is:
#    @pytest.mark.parametrize("channel_creator", [grpc.insecure_channel])
#    @pytest.mark.parametrize("transport_name",["grpc","rest"])
#    @pytest.mark.parametrize("transport_endpoint", ["showcase.googleapis.com", "localhost:7469" ])
#    @pytest.mark.parametrize("credential_universe",["showcase.googleapis.com", "localhost:7469"])
def vary_channel_transport_endpoints_universes():
    for channel_creator in [grpc.insecure_channel]:
        for transport_name in ["grpc", "rest"]:
            for transport_endpoint in ["showcase.googleapis.com", "localhost:7469"]:
                for credential_universe in ["showcase.googleapis.com", "localhost:7469"]:
                    params = EchoParams()
                    params.setattrs(
                        channel_creator=channel_creator,
                        transport_name=transport_name,
                        transport_endpoint=transport_endpoint,
                        credential_universe=credential_universe,
                        client_universe="googleapis.com"
                    )
                    yield params

# TODO: Test without passing a channel to gRPC transports in the test fixture
# TODO: Test without creating a transport in the test fixture
# TODO: Test asynchronous client as well.
# @pytest.mark.parametrize("channel_creator", [grpc.insecure_channel, None])


@pytest.mark.parametrize("test_params", vary_channel_transport_endpoints_universes())
def test_universe_domain_validation_fail(parametrized_echo, test_params):
    """Test that only the client and credentials universes are used for validation, and not the endpoint."""
    assert parametrized_echo.universe_domain == test_params.client_universe
    assert parametrized_echo.transport._credentials._universe_domain == test_params.credential_universe
    if test_params.transport_name == "rest":
        assert parametrized_echo.api_endpoint == "http://" + test_params.transport_endpoint
    elif test_params.channel_creator == grpc.insecure_channel:
        # TODO: Investigate where this endpoint override is coming from
        assert parametrized_echo.api_endpoint == "localhost:7469"
    else:
        assert parametrized_echo.api_endpoint == test_params.transport_endpoint
    with pytest.raises(ValueError) as err:
        parametrized_echo.echo({
            'content': 'Universe validation failed!'
            })
    assert str(
        err.value) == f"The configured universe domain ({test_params.client_universe}) does not match the universe domain found in the credentials ({test_params.credential_universe}). If you haven't configured the universe domain explicitly, `googleapis.com` is the default."

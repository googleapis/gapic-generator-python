from google.showcase import EchoClient, IdentityClient
from google.auth import credentials as ga_credentials
from google.cloud.logging.handlers import StructuredLogHandler


import os
import logging

import grpc


def construct_echo_client():
    transport_cls = EchoClient.get_transport_class("rest")
    transport = transport_cls(
                credentials=ga_credentials.AnonymousCredentials(),
                host="localhost:7469",
                url_scheme="http",
            )
    
    
    echo = EchoClient(transport=transport)
    return echo

def construct_identity_client():
    transport_cls = IdentityClient.get_transport_class("grpc")
    transport = transport_cls(
                credentials=ga_credentials.AnonymousCredentials(),
                channel=grpc.insecure_channel("localhost:7469")
            )
    
    
    identity = IdentityClient(transport=transport)
    return identity

def echo_request(echo):
    response = echo.echo(
        {
            "content": "The hail in Wales falls mainly on the snails.",
            "request_id": "some_value",
            "other_request_id": "",
        }
    )
    return response

def identity_request(identity):

    # request to create user
    user = identity.create_user(
        request={
            "user": {"display_name": "Guido van Rossum", "email": "guido@guido.fake1", }
        }
    )

    # request to delete user
    identity.delete_user({"name": user.name})
    return user


def test_env_var_settings(log_level=""):
    os.environ["GOOGLE_SDK_PYTHON_LOGGING_LEVEL"] = log_level
    
    # echo request
    echo = construct_echo_client()
    response = echo_request(echo)
    
    # identity request
    identity = construct_identity_client()
    response = identity_request(identity)
    print(f"Test completed with env var set to: {os.getenv('GOOGLE_SDK_PYTHON_LOGGING_LEVEL')}")


def test_base_logger_settings():

    base_logger = logging.getLogger("google")
    base_logger.setLevel("DEBUG")
    console_handler = logging.StreamHandler()
    formatter = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s")
    console_handler.setFormatter(formatter)
    base_logger.addHandler(console_handler)

    # echo request
    echo = construct_echo_client()
    response = echo_request(echo)
    
    # identity request
    identity = construct_identity_client()
    response = identity_request(identity)
    print("base logger test completed.")


def test_root_logger_settings():

    base_logger = logging.getLogger()
    base_logger.setLevel("DEBUG")
    console_handler = logging.StreamHandler()
    formatter = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s")
    console_handler.setFormatter(formatter)
    base_logger.addHandler(console_handler)

    # echo request
    echo = construct_echo_client()
    response = echo_request(echo)
    
    # identity request
    identity = construct_identity_client()
    response = identity_request(identity)
    print("root logger test completed.")


def test_module_logger_settings():

    module_logger = logging.getLogger("google.showcase_v1beta1.services.echo")
    module_logger.setLevel("DEBUG")
    console_handler = logging.StreamHandler()
    formatter = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s")
    console_handler.setFormatter(formatter)
    module_logger.addHandler(console_handler)

    # echo request
    echo = construct_echo_client()
    response = echo_request(echo)
    
    # identity request
    identity = construct_identity_client()
    response = identity_request(identity)
    print("module logger test completed.")


def test_structured_log_settings():

    module_logger = logging.getLogger("google.showcase_v1beta1.services.echo")
    module_logger.setLevel("DEBUG")
    handler = StructuredLogHandler() # for structured logging format.
    module_logger.addHandler(handler)

    # echo request
    echo = construct_echo_client()
    response = echo_request(echo)
    
    # identity request
    identity = construct_identity_client()
    response = identity_request(identity)
    print("structured log test completed.")



def test_root_logger_and_env_var():

    os.environ["GOOGLE_SDK_PYTHON_LOGGING_LEVEL"] = "DEBUG"

    base_logger = logging.getLogger()
    base_logger.setLevel("INFO")
    console_handler = logging.StreamHandler()
    formatter = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s")
    console_handler.setFormatter(formatter)
    base_logger.addHandler(console_handler)

    # echo request
    echo = construct_echo_client()
    response = echo_request(echo)
    
    # identity request
    identity = construct_identity_client()
    response = identity_request(identity)
    print("structured log test completed.")


def test_base_logger_and_env_var():
    # NOTE: This test case results in duplicated logs due to an unexpected
    # behaviour caused by attaching the streamhandler twice to the logger
    # with namespace = "google".

    os.environ["GOOGLE_SDK_PYTHON_LOGGING_LEVEL"] = "DEBUG"

    base_logger = logging.getLogger("google")
    base_logger.setLevel("INFO")
    console_handler = logging.StreamHandler()
    formatter = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s")
    console_handler.setFormatter(formatter)
    base_logger.addHandler(console_handler)

    # echo request
    echo = construct_echo_client()
    response = echo_request(echo)
    
    # identity request
    identity = construct_identity_client()
    response = identity_request(identity)
    print("structured log test completed.")

def test_module_logger_and_env_var():

    os.environ["GOOGLE_SDK_PYTHON_LOGGING_LEVEL"] = "DEBUG"

    module_logger = logging.getLogger("google.showcase_v1beta1.services.echo")
    module_logger.setLevel("DEBUG")
    # NOTE: Uncommment the line below to avoid duplicated logs.
    # module_logger.propagate = False
    console_handler = logging.StreamHandler()
    formatter = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s")
    console_handler.setFormatter(formatter)
    module_logger.addHandler(console_handler)

    # echo request
    echo = construct_echo_client()
    response = echo_request(echo)
    
    # identity request
    identity = construct_identity_client()
    response = identity_request(identity)
    print("structured log test completed.")


'''
Install the changes in from python-api-core:
    1. Checkout the prototype changes: git checkout debug-logging
    2. Install the core changes: pip install -e .


# Generate showcase using the prototype changes:
    1. Checkout the prototype changes: git checkout logging-prototype
    2. Add a breakpoint in the noxfile.py in the `showcase_library` function (Ex: line 326 or anywhere before it yields.)
    3. Run a nox session to generate the showcase library: nox -s showcase-3.9 
    4. Install the temp directory (i.e. showcase): pip install -e ./tmp/tmpjkj33

# Run the showcase server:
    curl -sSL https://github.com/googleapis/gapic-showcase/releases/download/v0.35.0/gapic-showcase-0.35.0-linux-amd64.tar.gz | tar xz && ./gapic-showcase run

# Uncomment any of the the tests below and run (to see the expected behaviour):
    python3 tests/system/logging_test.py

'''

### TEST SUITE

# Test default settings: (Expected: No logs.)
# test_env_var_settings(log_level="")

# Test GOOGLE_SDK_PYTHON_LOGGING_LEVEL=DEBUG (Expected: logs for google APIs only.)
# test_env_var_settings(log_level="DEBUG")

# Test GOOGLE_SDK_PYTHON_LOGGING_LEVEL=123 (Expected: No logs. Defaults to "WARNING".)
# test_env_var_settings(log_level="123")

# Test Base Logger configured using code. (Expected: logs for google APIs only.)
# test_base_logger_settings()

# Test root Logger configured using code. (Expected: All logs.)
# test_root_logger_settings()

# Test module logger ("google.showcase_v1beta1.services.echo") configured using code. (Expected: logs for echo service only.)
# test_module_logger_settings()

# Test module logger ("google.showcase_v1beta1.services.echo") with structured logging format configured using code. (Expected: logs for echo service only.)
# test_structured_log_settings()

# Test root logger and env variable (Expected: Root logger settings take precedence i.e. logs at `INFO` level shall appear only.)
# test_root_logger_and_env_var()

# Test base logger and env variable (NOTE: This results in unexpected behaviour due to a stream handler being attached twice to the logger.)
# test_base_logger_and_env_var()

# Test module logger and env variable.
# NOTE: This results in unexpected behaviour i.e. we see duplicated logs due to logs being propogated upstream.
#       A possible solution is to set logger.propogate = False to get around this. (uncomment in code)
# test_module_logger_and_env_var()

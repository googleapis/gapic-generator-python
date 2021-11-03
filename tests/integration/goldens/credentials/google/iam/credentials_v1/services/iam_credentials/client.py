# -*- coding: utf-8 -*-
# Copyright 2020 Google LLC
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
from collections import OrderedDict
from distutils import util
import os
import re
from typing import Dict, Optional, Sequence, Tuple, Type, Union
import pkg_resources

from google.api_core import client_options as client_options_lib  # type: ignore
from google.api_core import exceptions as core_exceptions         # type: ignore
from google.api_core import gapic_v1                              # type: ignore
from google.api_core import retry as retries                      # type: ignore
from google.auth import credentials as ga_credentials             # type: ignore
from google.auth.transport import mtls                            # type: ignore
from google.auth.transport.grpc import SslCredentials             # type: ignore
from google.auth.exceptions import MutualTLSChannelError          # type: ignore
from google.oauth2 import service_account                         # type: ignore

try:
    OptionalRetry = Union[retries.Retry, gapic_v1.method._MethodDefault]
except AttributeError:
    OptionalRetry = Union[retries.Retry, object]  # type: ignore

from google.iam.credentials_v1.types import common
from google.protobuf import duration_pb2  # type: ignore
from google.protobuf import timestamp_pb2  # type: ignore
from .transports.base import IAMCredentialsTransport, DEFAULT_CLIENT_INFO
from .transports.grpc import IAMCredentialsGrpcTransport
from .transports.grpc_asyncio import IAMCredentialsGrpcAsyncIOTransport


class IAMCredentialsClientMeta(type):
    """Metaclass for the IAMCredentials client.

    This provides class-level methods for building and retrieving
    support objects (e.g. transport) without polluting the client instance
    objects.
    """
    _transport_registry = OrderedDict()  # type: Dict[str, Type[IAMCredentialsTransport]]
    _transport_registry["grpc"] = IAMCredentialsGrpcTransport
    _transport_registry["grpc_asyncio"] = IAMCredentialsGrpcAsyncIOTransport

    def get_transport_class(cls,
            label: str = None,
        ) -> Type[IAMCredentialsTransport]:
        """Returns an appropriate transport class.

        Args:
            label: The name of the desired transport. If none is
                provided, then the first transport in the registry is used.

        Returns:
            The transport class to use.
        """
        # If a specific transport is requested, return that one.
        if label:
            return cls._transport_registry[label]

        # No transport is requested; return the default (that is, the first one
        # in the dictionary).
        return next(iter(cls._transport_registry.values()))


class IAMCredentialsClient(metaclass=IAMCredentialsClientMeta):
    """A service account is a special type of Google account that
    belongs to your application or a virtual machine (VM), instead
    of to an individual end user. Your application assumes the
    identity of the service account to call Google APIs, so that the
    users aren't directly involved.

    Service account credentials are used to temporarily assume the
    identity of the service account. Supported credential types
    include OAuth 2.0 access tokens, OpenID Connect ID tokens, self-
    signed JSON Web Tokens (JWTs), and more.
    """

    @staticmethod
    def _get_default_mtls_endpoint(api_endpoint):
        """Converts api endpoint to mTLS endpoint.

        Convert "*.sandbox.googleapis.com" and "*.googleapis.com" to
        "*.mtls.sandbox.googleapis.com" and "*.mtls.googleapis.com" respectively.
        Args:
            api_endpoint (Optional[str]): the api endpoint to convert.
        Returns:
            str: converted mTLS api endpoint.
        """
        if not api_endpoint:
            return api_endpoint

        mtls_endpoint_re = re.compile(
            r"(?P<name>[^.]+)(?P<mtls>\.mtls)?(?P<sandbox>\.sandbox)?(?P<googledomain>\.googleapis\.com)?"
        )

        m = mtls_endpoint_re.match(api_endpoint)
        name, mtls, sandbox, googledomain = m.groups()
        if mtls or not googledomain:
            return api_endpoint

        if sandbox:
            return api_endpoint.replace(
                "sandbox.googleapis.com", "mtls.sandbox.googleapis.com"
            )

        return api_endpoint.replace(".googleapis.com", ".mtls.googleapis.com")

    DEFAULT_ENDPOINT = "iamcredentials.googleapis.com"
    DEFAULT_MTLS_ENDPOINT = _get_default_mtls_endpoint.__func__(  # type: ignore
        DEFAULT_ENDPOINT
    )

    @classmethod
    def from_service_account_info(cls, info: dict, *args, **kwargs):
        """Creates an instance of this client using the provided credentials
            info.

        Args:
            info (dict): The service account private key info.
            args: Additional arguments to pass to the constructor.
            kwargs: Additional arguments to pass to the constructor.

        Returns:
            IAMCredentialsClient: The constructed client.
        """
        credentials = service_account.Credentials.from_service_account_info(info)
        kwargs["credentials"] = credentials
        return cls(*args, **kwargs)

    @classmethod
    def from_service_account_file(cls, filename: str, *args, **kwargs):
        """Creates an instance of this client using the provided credentials
            file.

        Args:
            filename (str): The path to the service account private key json
                file.
            args: Additional arguments to pass to the constructor.
            kwargs: Additional arguments to pass to the constructor.

        Returns:
            IAMCredentialsClient: The constructed client.
        """
        credentials = service_account.Credentials.from_service_account_file(
            filename)
        kwargs["credentials"] = credentials
        return cls(*args, **kwargs)

    from_service_account_json = from_service_account_file

    @property
    def transport(self) -> IAMCredentialsTransport:
        """Returns the transport used by the client instance.

        Returns:
            IAMCredentialsTransport: The transport used by the client
                instance.
        """
        return self._transport

    @staticmethod
    def service_account_path(project: str,service_account: str,) -> str:
        """Returns a fully-qualified service_account string."""
        return "projects/{project}/serviceAccounts/{service_account}".format(project=project, service_account=service_account, )

    @staticmethod
    def parse_service_account_path(path: str) -> Dict[str,str]:
        """Parses a service_account path into its component segments."""
        m = re.match(r"^projects/(?P<project>.+?)/serviceAccounts/(?P<service_account>.+?)$", path)
        return m.groupdict() if m else {}

    @staticmethod
    def common_billing_account_path(billing_account: str, ) -> str:
        """Returns a fully-qualified billing_account string."""
        return "billingAccounts/{billing_account}".format(billing_account=billing_account, )

    @staticmethod
    def parse_common_billing_account_path(path: str) -> Dict[str,str]:
        """Parse a billing_account path into its component segments."""
        m = re.match(r"^billingAccounts/(?P<billing_account>.+?)$", path)
        return m.groupdict() if m else {}

    @staticmethod
    def common_folder_path(folder: str, ) -> str:
        """Returns a fully-qualified folder string."""
        return "folders/{folder}".format(folder=folder, )

    @staticmethod
    def parse_common_folder_path(path: str) -> Dict[str,str]:
        """Parse a folder path into its component segments."""
        m = re.match(r"^folders/(?P<folder>.+?)$", path)
        return m.groupdict() if m else {}

    @staticmethod
    def common_organization_path(organization: str, ) -> str:
        """Returns a fully-qualified organization string."""
        return "organizations/{organization}".format(organization=organization, )

    @staticmethod
    def parse_common_organization_path(path: str) -> Dict[str,str]:
        """Parse a organization path into its component segments."""
        m = re.match(r"^organizations/(?P<organization>.+?)$", path)
        return m.groupdict() if m else {}

    @staticmethod
    def common_project_path(project: str, ) -> str:
        """Returns a fully-qualified project string."""
        return "projects/{project}".format(project=project, )

    @staticmethod
    def parse_common_project_path(path: str) -> Dict[str,str]:
        """Parse a project path into its component segments."""
        m = re.match(r"^projects/(?P<project>.+?)$", path)
        return m.groupdict() if m else {}

    @staticmethod
    def common_location_path(project: str, location: str, ) -> str:
        """Returns a fully-qualified location string."""
        return "projects/{project}/locations/{location}".format(project=project, location=location, )

    @staticmethod
    def parse_common_location_path(path: str) -> Dict[str,str]:
        """Parse a location path into its component segments."""
        m = re.match(r"^projects/(?P<project>.+?)/locations/(?P<location>.+?)$", path)
        return m.groupdict() if m else {}

    def __init__(self, *,
            credentials: Optional[ga_credentials.Credentials] = None,
            transport: Union[str, IAMCredentialsTransport, None] = None,
            client_options: Optional[client_options_lib.ClientOptions] = None,
            client_info: gapic_v1.client_info.ClientInfo = DEFAULT_CLIENT_INFO,
            ) -> None:
        """Instantiates the iam credentials client.

        Args:
            credentials (Optional[google.auth.credentials.Credentials]): The
                authorization credentials to attach to requests. These
                credentials identify the application to the service; if none
                are specified, the client will attempt to ascertain the
                credentials from the environment.
            transport (Union[str, IAMCredentialsTransport]): The
                transport to use. If set to None, a transport is chosen
                automatically.
            client_options (google.api_core.client_options.ClientOptions): Custom options for the
                client. It won't take effect if a ``transport`` instance is provided.
                (1) The ``api_endpoint`` property can be used to override the
                default endpoint provided by the client. GOOGLE_API_USE_MTLS_ENDPOINT
                environment variable can also be used to override the endpoint:
                "always" (always use the default mTLS endpoint), "never" (always
                use the default regular endpoint) and "auto" (auto switch to the
                default mTLS endpoint if client certificate is present, this is
                the default value). However, the ``api_endpoint`` property takes
                precedence if provided.
                (2) If GOOGLE_API_USE_CLIENT_CERTIFICATE environment variable
                is "true", then the ``client_cert_source`` property can be used
                to provide client certificate for mutual TLS transport. If
                not provided, the default SSL client certificate will be used if
                present. If GOOGLE_API_USE_CLIENT_CERTIFICATE is "false" or not
                set, no client certificate will be used.
            client_info (google.api_core.gapic_v1.client_info.ClientInfo):
                The client info used to send a user-agent string along with
                API requests. If ``None``, then default info will be used.
                Generally, you only need to set this if you're developing
                your own client library.

        Raises:
            google.auth.exceptions.MutualTLSChannelError: If mutual TLS transport
                creation failed for any reason.
        """
        if isinstance(client_options, dict):
            client_options = client_options_lib.from_dict(client_options)
        if client_options is None:
            client_options = client_options_lib.ClientOptions()

        # Create SSL credentials for mutual TLS if needed.
        use_client_cert = bool(util.strtobool(os.getenv("GOOGLE_API_USE_CLIENT_CERTIFICATE", "false")))

        client_cert_source_func = None
        is_mtls = False
        if use_client_cert:
            if client_options.client_cert_source:
                is_mtls = True
                client_cert_source_func = client_options.client_cert_source
            else:
                is_mtls = mtls.has_default_client_cert_source()
                if is_mtls:
                    client_cert_source_func = mtls.default_client_cert_source()
                else:
                    client_cert_source_func = None

        # Figure out which api endpoint to use.
        if client_options.api_endpoint is not None:
            api_endpoint = client_options.api_endpoint
        else:
            use_mtls_env = os.getenv("GOOGLE_API_USE_MTLS_ENDPOINT", "auto")
            if use_mtls_env == "never":
                api_endpoint = self.DEFAULT_ENDPOINT
            elif use_mtls_env == "always":
                api_endpoint = self.DEFAULT_MTLS_ENDPOINT
            elif use_mtls_env == "auto":
                if is_mtls:
                    api_endpoint = self.DEFAULT_MTLS_ENDPOINT
                else:
                    api_endpoint = self.DEFAULT_ENDPOINT
            else:
                raise MutualTLSChannelError(
                    "Unsupported GOOGLE_API_USE_MTLS_ENDPOINT value. Accepted "
                    "values: never, auto, always"
                )

        # Save or instantiate the transport.
        # Ordinarily, we provide the transport, but allowing a custom transport
        # instance provides an extensibility point for unusual situations.
        if isinstance(transport, IAMCredentialsTransport):
            # transport is a IAMCredentialsTransport instance.
            if credentials or client_options.credentials_file:
                raise ValueError("When providing a transport instance, "
                                 "provide its credentials directly.")
            if client_options.scopes:
                raise ValueError(
                    "When providing a transport instance, provide its scopes "
                    "directly."
                )
            self._transport = transport
        else:
            Transport = type(self).get_transport_class(transport)
            self._transport = Transport(
                credentials=credentials,
                credentials_file=client_options.credentials_file,
                host=api_endpoint,
                scopes=client_options.scopes,
                client_cert_source_for_mtls=client_cert_source_func,
                quota_project_id=client_options.quota_project_id,
                client_info=client_info,
                always_use_jwt_access=True,
            )

    def generate_access_token(self,
            request: Union[common.GenerateAccessTokenRequest, dict] = None,
            *,
            name: str = None,
            delegates: Sequence[str] = None,
            scope: Sequence[str] = None,
            lifetime: duration_pb2.Duration = None,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: float = None,
            metadata: Sequence[Tuple[str, str]] = (),
            ) -> common.GenerateAccessTokenResponse:
        r"""Generates an OAuth 2.0 access token for a service
        account.

        Args:
            request (Union[google.iam.credentials_v1.types.GenerateAccessTokenRequest, dict]):
                The request object.
            name (str):
                Required. The resource name of the service account for
                which the credentials are requested, in the following
                format:
                ``projects/-/serviceAccounts/{ACCOUNT_EMAIL_OR_UNIQUEID}``.
                The ``-`` wildcard character is required; replacing it
                with a project ID is invalid.

                This corresponds to the ``name`` field
                on the ``request`` instance; if ``request`` is provided, this
                should not be set.
            delegates (Sequence[str]):
                The sequence of service accounts in a delegation chain.
                Each service account must be granted the
                ``roles/iam.serviceAccountTokenCreator`` role on its
                next service account in the chain. The last service
                account in the chain must be granted the
                ``roles/iam.serviceAccountTokenCreator`` role on the
                service account that is specified in the ``name`` field
                of the request.

                The delegates must have the following format:
                ``projects/-/serviceAccounts/{ACCOUNT_EMAIL_OR_UNIQUEID}``.
                The ``-`` wildcard character is required; replacing it
                with a project ID is invalid.

                This corresponds to the ``delegates`` field
                on the ``request`` instance; if ``request`` is provided, this
                should not be set.
            scope (Sequence[str]):
                Required. Code to identify the scopes
                to be included in the OAuth 2.0 access
                token. See
                https://developers.google.com/identity/protocols/googlescopes
                for more information.
                At least one value required.

                This corresponds to the ``scope`` field
                on the ``request`` instance; if ``request`` is provided, this
                should not be set.
            lifetime (google.protobuf.duration_pb2.Duration):
                The desired lifetime duration of the
                access token in seconds. Must be set to
                a value less than or equal to 3600 (1
                hour). If a value is not specified, the
                token's lifetime will be set to a
                default value of one hour.

                This corresponds to the ``lifetime`` field
                on the ``request`` instance; if ``request`` is provided, this
                should not be set.
            retry (google.api_core.retry.Retry): Designation of what errors, if any,
                should be retried.
            timeout (float): The timeout for this request.
            metadata (Sequence[Tuple[str, str]]): Strings which should be
                sent along with the request as metadata.

        Returns:
            google.iam.credentials_v1.types.GenerateAccessTokenResponse:

        """
        # Create or coerce a protobuf request object.
        # Sanity check: If we got a request object, we should *not* have
        # gotten any keyword arguments that map to the request.
        has_flattened_params = any([name, delegates, scope, lifetime])
        if request is not None and has_flattened_params:
            raise ValueError('If the `request` argument is set, then none of '
                             'the individual field arguments should be set.')

        # Minor optimization to avoid making a copy if the user passes
        # in a common.GenerateAccessTokenRequest.
        # There's no risk of modifying the input as we've already verified
        # there are no flattened fields.
        if not isinstance(request, common.GenerateAccessTokenRequest):
            request = common.GenerateAccessTokenRequest(request)
            # If we have keyword arguments corresponding to fields on the
            # request, apply these.
            if name is not None:
                request.name = name
            if delegates is not None:
                request.delegates = delegates
            if scope is not None:
                request.scope = scope
            if lifetime is not None:
                request.lifetime = lifetime

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = self._transport._wrapped_methods[self._transport.generate_access_token]

        # Certain fields should be provided within the metadata header;
        # add these here.
        metadata = tuple(metadata) + (
            gapic_v1.routing_header.to_grpc_metadata((
                ("name", request.name),
            )),
        )

        # Send the request.
        response = rpc(
            request,
            retry=retry,
            timeout=timeout,
            metadata=metadata,
        )

        # Done; return the response.
        return response

    def generate_id_token(self,
            request: Union[common.GenerateIdTokenRequest, dict] = None,
            *,
            name: str = None,
            delegates: Sequence[str] = None,
            audience: str = None,
            include_email: bool = None,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: float = None,
            metadata: Sequence[Tuple[str, str]] = (),
            ) -> common.GenerateIdTokenResponse:
        r"""Generates an OpenID Connect ID token for a service
        account.

        Args:
            request (Union[google.iam.credentials_v1.types.GenerateIdTokenRequest, dict]):
                The request object.
            name (str):
                Required. The resource name of the service account for
                which the credentials are requested, in the following
                format:
                ``projects/-/serviceAccounts/{ACCOUNT_EMAIL_OR_UNIQUEID}``.
                The ``-`` wildcard character is required; replacing it
                with a project ID is invalid.

                This corresponds to the ``name`` field
                on the ``request`` instance; if ``request`` is provided, this
                should not be set.
            delegates (Sequence[str]):
                The sequence of service accounts in a delegation chain.
                Each service account must be granted the
                ``roles/iam.serviceAccountTokenCreator`` role on its
                next service account in the chain. The last service
                account in the chain must be granted the
                ``roles/iam.serviceAccountTokenCreator`` role on the
                service account that is specified in the ``name`` field
                of the request.

                The delegates must have the following format:
                ``projects/-/serviceAccounts/{ACCOUNT_EMAIL_OR_UNIQUEID}``.
                The ``-`` wildcard character is required; replacing it
                with a project ID is invalid.

                This corresponds to the ``delegates`` field
                on the ``request`` instance; if ``request`` is provided, this
                should not be set.
            audience (str):
                Required. The audience for the token,
                such as the API or account that this
                token grants access to.

                This corresponds to the ``audience`` field
                on the ``request`` instance; if ``request`` is provided, this
                should not be set.
            include_email (bool):
                Include the service account email in the token. If set
                to ``true``, the token will contain ``email`` and
                ``email_verified`` claims.

                This corresponds to the ``include_email`` field
                on the ``request`` instance; if ``request`` is provided, this
                should not be set.
            retry (google.api_core.retry.Retry): Designation of what errors, if any,
                should be retried.
            timeout (float): The timeout for this request.
            metadata (Sequence[Tuple[str, str]]): Strings which should be
                sent along with the request as metadata.

        Returns:
            google.iam.credentials_v1.types.GenerateIdTokenResponse:

        """
        # Create or coerce a protobuf request object.
        # Sanity check: If we got a request object, we should *not* have
        # gotten any keyword arguments that map to the request.
        has_flattened_params = any([name, delegates, audience, include_email])
        if request is not None and has_flattened_params:
            raise ValueError('If the `request` argument is set, then none of '
                             'the individual field arguments should be set.')

        # Minor optimization to avoid making a copy if the user passes
        # in a common.GenerateIdTokenRequest.
        # There's no risk of modifying the input as we've already verified
        # there are no flattened fields.
        if not isinstance(request, common.GenerateIdTokenRequest):
            request = common.GenerateIdTokenRequest(request)
            # If we have keyword arguments corresponding to fields on the
            # request, apply these.
            if name is not None:
                request.name = name
            if delegates is not None:
                request.delegates = delegates
            if audience is not None:
                request.audience = audience
            if include_email is not None:
                request.include_email = include_email

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = self._transport._wrapped_methods[self._transport.generate_id_token]

        # Certain fields should be provided within the metadata header;
        # add these here.
        metadata = tuple(metadata) + (
            gapic_v1.routing_header.to_grpc_metadata((
                ("name", request.name),
            )),
        )

        # Send the request.
        response = rpc(
            request,
            retry=retry,
            timeout=timeout,
            metadata=metadata,
        )

        # Done; return the response.
        return response

    def sign_blob(self,
            request: Union[common.SignBlobRequest, dict] = None,
            *,
            name: str = None,
            delegates: Sequence[str] = None,
            payload: bytes = None,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: float = None,
            metadata: Sequence[Tuple[str, str]] = (),
            ) -> common.SignBlobResponse:
        r"""Signs a blob using a service account's system-managed
        private key.

        Args:
            request (Union[google.iam.credentials_v1.types.SignBlobRequest, dict]):
                The request object.
            name (str):
                Required. The resource name of the service account for
                which the credentials are requested, in the following
                format:
                ``projects/-/serviceAccounts/{ACCOUNT_EMAIL_OR_UNIQUEID}``.
                The ``-`` wildcard character is required; replacing it
                with a project ID is invalid.

                This corresponds to the ``name`` field
                on the ``request`` instance; if ``request`` is provided, this
                should not be set.
            delegates (Sequence[str]):
                The sequence of service accounts in a delegation chain.
                Each service account must be granted the
                ``roles/iam.serviceAccountTokenCreator`` role on its
                next service account in the chain. The last service
                account in the chain must be granted the
                ``roles/iam.serviceAccountTokenCreator`` role on the
                service account that is specified in the ``name`` field
                of the request.

                The delegates must have the following format:
                ``projects/-/serviceAccounts/{ACCOUNT_EMAIL_OR_UNIQUEID}``.
                The ``-`` wildcard character is required; replacing it
                with a project ID is invalid.

                This corresponds to the ``delegates`` field
                on the ``request`` instance; if ``request`` is provided, this
                should not be set.
            payload (bytes):
                Required. The bytes to sign.
                This corresponds to the ``payload`` field
                on the ``request`` instance; if ``request`` is provided, this
                should not be set.
            retry (google.api_core.retry.Retry): Designation of what errors, if any,
                should be retried.
            timeout (float): The timeout for this request.
            metadata (Sequence[Tuple[str, str]]): Strings which should be
                sent along with the request as metadata.

        Returns:
            google.iam.credentials_v1.types.SignBlobResponse:

        """
        # Create or coerce a protobuf request object.
        # Sanity check: If we got a request object, we should *not* have
        # gotten any keyword arguments that map to the request.
        has_flattened_params = any([name, delegates, payload])
        if request is not None and has_flattened_params:
            raise ValueError('If the `request` argument is set, then none of '
                             'the individual field arguments should be set.')

        # Minor optimization to avoid making a copy if the user passes
        # in a common.SignBlobRequest.
        # There's no risk of modifying the input as we've already verified
        # there are no flattened fields.
        if not isinstance(request, common.SignBlobRequest):
            request = common.SignBlobRequest(request)
            # If we have keyword arguments corresponding to fields on the
            # request, apply these.
            if name is not None:
                request.name = name
            if delegates is not None:
                request.delegates = delegates
            if payload is not None:
                request.payload = payload

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = self._transport._wrapped_methods[self._transport.sign_blob]

        # Certain fields should be provided within the metadata header;
        # add these here.
        metadata = tuple(metadata) + (
            gapic_v1.routing_header.to_grpc_metadata((
                ("name", request.name),
            )),
        )

        # Send the request.
        response = rpc(
            request,
            retry=retry,
            timeout=timeout,
            metadata=metadata,
        )

        # Done; return the response.
        return response

    def sign_jwt(self,
            request: Union[common.SignJwtRequest, dict] = None,
            *,
            name: str = None,
            delegates: Sequence[str] = None,
            payload: str = None,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: float = None,
            metadata: Sequence[Tuple[str, str]] = (),
            ) -> common.SignJwtResponse:
        r"""Signs a JWT using a service account's system-managed
        private key.

        Args:
            request (Union[google.iam.credentials_v1.types.SignJwtRequest, dict]):
                The request object.
            name (str):
                Required. The resource name of the service account for
                which the credentials are requested, in the following
                format:
                ``projects/-/serviceAccounts/{ACCOUNT_EMAIL_OR_UNIQUEID}``.
                The ``-`` wildcard character is required; replacing it
                with a project ID is invalid.

                This corresponds to the ``name`` field
                on the ``request`` instance; if ``request`` is provided, this
                should not be set.
            delegates (Sequence[str]):
                The sequence of service accounts in a delegation chain.
                Each service account must be granted the
                ``roles/iam.serviceAccountTokenCreator`` role on its
                next service account in the chain. The last service
                account in the chain must be granted the
                ``roles/iam.serviceAccountTokenCreator`` role on the
                service account that is specified in the ``name`` field
                of the request.

                The delegates must have the following format:
                ``projects/-/serviceAccounts/{ACCOUNT_EMAIL_OR_UNIQUEID}``.
                The ``-`` wildcard character is required; replacing it
                with a project ID is invalid.

                This corresponds to the ``delegates`` field
                on the ``request`` instance; if ``request`` is provided, this
                should not be set.
            payload (str):
                Required. The JWT payload to sign: a
                JSON object that contains a JWT Claims
                Set.

                This corresponds to the ``payload`` field
                on the ``request`` instance; if ``request`` is provided, this
                should not be set.
            retry (google.api_core.retry.Retry): Designation of what errors, if any,
                should be retried.
            timeout (float): The timeout for this request.
            metadata (Sequence[Tuple[str, str]]): Strings which should be
                sent along with the request as metadata.

        Returns:
            google.iam.credentials_v1.types.SignJwtResponse:

        """
        # Create or coerce a protobuf request object.
        # Sanity check: If we got a request object, we should *not* have
        # gotten any keyword arguments that map to the request.
        has_flattened_params = any([name, delegates, payload])
        if request is not None and has_flattened_params:
            raise ValueError('If the `request` argument is set, then none of '
                             'the individual field arguments should be set.')

        # Minor optimization to avoid making a copy if the user passes
        # in a common.SignJwtRequest.
        # There's no risk of modifying the input as we've already verified
        # there are no flattened fields.
        if not isinstance(request, common.SignJwtRequest):
            request = common.SignJwtRequest(request)
            # If we have keyword arguments corresponding to fields on the
            # request, apply these.
            if name is not None:
                request.name = name
            if delegates is not None:
                request.delegates = delegates
            if payload is not None:
                request.payload = payload

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = self._transport._wrapped_methods[self._transport.sign_jwt]

        # Certain fields should be provided within the metadata header;
        # add these here.
        metadata = tuple(metadata) + (
            gapic_v1.routing_header.to_grpc_metadata((
                ("name", request.name),
            )),
        )

        # Send the request.
        response = rpc(
            request,
            retry=retry,
            timeout=timeout,
            metadata=metadata,
        )

        # Done; return the response.
        return response

    def __enter__(self):
        return self

    def __exit__(self, type, value, traceback):
        """Releases underlying transport's resources.

        .. warning::
            ONLY use as a context manager if the transport is NOT shared
            with other clients! Exiting the with block will CLOSE the transport
            and may cause errors in other clients!
        """
        self.transport.close()



try:
    DEFAULT_CLIENT_INFO = gapic_v1.client_info.ClientInfo(
        gapic_version=pkg_resources.get_distribution(
            "google-iam-credentials",
        ).version,
    )
except pkg_resources.DistributionNotFound:
    DEFAULT_CLIENT_INFO = gapic_v1.client_info.ClientInfo()


__all__ = (
    "IAMCredentialsClient",
)

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
import warnings
from typing import Callable, Dict, Optional, Sequence, Tuple, Union

from google.api_core import grpc_helpers
from google.api_core import gapic_v1
import google.auth                         # type: ignore
from google.auth import credentials as ga_credentials  # type: ignore
from google.auth.transport.grpc import SslCredentials  # type: ignore

import grpc  # type: ignore

from google.cloud.location import locations_pb2 # type: ignore
from google.iam.v1 import iam_policy_pb2  # type: ignore
from google.iam.v1 import policy_pb2  # type: ignore
from google.longrunning import operations_pb2 # type: ignore
from google.showcase_v1beta1.types import compliance
from .base import ComplianceTransport, DEFAULT_CLIENT_INFO


class ComplianceGrpcTransport(ComplianceTransport):
    """gRPC backend transport for Compliance.

    This service is used to test that GAPICs implement various
    REST-related features correctly. This mostly means transcoding
    proto3 requests to REST format correctly for various types of
    HTTP annotations, but it also includes verifying that unknown
    (numeric) enums received by clients can be round-tripped
    correctly.

    This class defines the same methods as the primary client, so the
    primary client can load the underlying transport implementation
    and call it.

    It sends protocol buffers over the wire using gRPC (which is built on
    top of HTTP/2); the ``grpcio`` package must be installed.
    """
    _stubs: Dict[str, Callable]

    def __init__(self, *,
            host: str = 'localhost:7469',
            credentials: Optional[ga_credentials.Credentials] = None,
            credentials_file: Optional[str] = None,
            scopes: Optional[Sequence[str]] = None,
            channel: Optional[grpc.Channel] = None,
            api_mtls_endpoint: Optional[str] = None,
            client_cert_source: Optional[Callable[[], Tuple[bytes, bytes]]] = None,
            ssl_channel_credentials: Optional[grpc.ChannelCredentials] = None,
            client_cert_source_for_mtls: Optional[Callable[[], Tuple[bytes, bytes]]] = None,
            quota_project_id: Optional[str] = None,
            client_info: gapic_v1.client_info.ClientInfo = DEFAULT_CLIENT_INFO,
            always_use_jwt_access: Optional[bool] = False,
            api_audience: Optional[str] = None,
            ) -> None:
        """Instantiate the transport.

        Args:
            host (Optional[str]):
                 The hostname to connect to (default: 'localhost:7469').
            credentials (Optional[google.auth.credentials.Credentials]): The
                authorization credentials to attach to requests. These
                credentials identify the application to the service; if none
                are specified, the client will attempt to ascertain the
                credentials from the environment.
                This argument is ignored if ``channel`` is provided.
            credentials_file (Optional[str]): A file with credentials that can
                be loaded with :func:`google.auth.load_credentials_from_file`.
                This argument is ignored if ``channel`` is provided.
            scopes (Optional(Sequence[str])): A list of scopes. This argument is
                ignored if ``channel`` is provided.
            channel (Optional[grpc.Channel]): A ``Channel`` instance through
                which to make calls.
            api_mtls_endpoint (Optional[str]): Deprecated. The mutual TLS endpoint.
                If provided, it overrides the ``host`` argument and tries to create
                a mutual TLS channel with client SSL credentials from
                ``client_cert_source`` or application default SSL credentials.
            client_cert_source (Optional[Callable[[], Tuple[bytes, bytes]]]):
                Deprecated. A callback to provide client SSL certificate bytes and
                private key bytes, both in PEM format. It is ignored if
                ``api_mtls_endpoint`` is None.
            ssl_channel_credentials (grpc.ChannelCredentials): SSL credentials
                for the grpc channel. It is ignored if ``channel`` is provided.
            client_cert_source_for_mtls (Optional[Callable[[], Tuple[bytes, bytes]]]):
                A callback to provide client certificate bytes and private key bytes,
                both in PEM format. It is used to configure a mutual TLS channel. It is
                ignored if ``channel`` or ``ssl_channel_credentials`` is provided.
            quota_project_id (Optional[str]): An optional project to use for billing
                and quota.
            client_info (google.api_core.gapic_v1.client_info.ClientInfo):
                The client info used to send a user-agent string along with
                API requests. If ``None``, then default info will be used.
                Generally, you only need to set this if you're developing
                your own client library.
            always_use_jwt_access (Optional[bool]): Whether self signed JWT should
                be used for service account credentials.

        Raises:
          google.auth.exceptions.MutualTLSChannelError: If mutual TLS transport
              creation failed for any reason.
          google.api_core.exceptions.DuplicateCredentialArgs: If both ``credentials``
              and ``credentials_file`` are passed.
        """
        self._grpc_channel = None
        self._ssl_channel_credentials = ssl_channel_credentials
        self._stubs: Dict[str, Callable] = {}

        if api_mtls_endpoint:
            warnings.warn("api_mtls_endpoint is deprecated", DeprecationWarning)
        if client_cert_source:
            warnings.warn("client_cert_source is deprecated", DeprecationWarning)

        if channel:
            # Ignore credentials if a channel was passed.
            credentials = False
            # If a channel was explicitly provided, set it.
            self._grpc_channel = channel
            self._ssl_channel_credentials = None

        else:
            if api_mtls_endpoint:
                host = api_mtls_endpoint

                # Create SSL credentials with client_cert_source or application
                # default SSL credentials.
                if client_cert_source:
                    cert, key = client_cert_source()
                    self._ssl_channel_credentials = grpc.ssl_channel_credentials(
                        certificate_chain=cert, private_key=key
                    )
                else:
                    self._ssl_channel_credentials = SslCredentials().ssl_credentials

            else:
                if client_cert_source_for_mtls and not ssl_channel_credentials:
                    cert, key = client_cert_source_for_mtls()
                    self._ssl_channel_credentials = grpc.ssl_channel_credentials(
                        certificate_chain=cert, private_key=key
                    )

        # The base transport sets the host, credentials and scopes
        super().__init__(
            host=host,
            credentials=credentials,
            credentials_file=credentials_file,
            scopes=scopes,
            quota_project_id=quota_project_id,
            client_info=client_info,
            always_use_jwt_access=always_use_jwt_access,
            api_audience=api_audience,
        )

        if not self._grpc_channel:
            self._grpc_channel = type(self).create_channel(
                self._host,
                # use the credentials which are saved
                credentials=self._credentials,
                # Set ``credentials_file`` to ``None`` here as
                # the credentials that we saved earlier should be used.
                credentials_file=None,
                scopes=self._scopes,
                ssl_credentials=self._ssl_channel_credentials,
                quota_project_id=quota_project_id,
                options=[
                    ("grpc.max_send_message_length", -1),
                    ("grpc.max_receive_message_length", -1),
                ],
            )

        # Wrap messages. This must be done after self._grpc_channel exists
        self._prep_wrapped_messages(client_info)

    @classmethod
    def create_channel(cls,
                       host: str = 'localhost:7469',
                       credentials: Optional[ga_credentials.Credentials] = None,
                       credentials_file: Optional[str] = None,
                       scopes: Optional[Sequence[str]] = None,
                       quota_project_id: Optional[str] = None,
                       **kwargs) -> grpc.Channel:
        """Create and return a gRPC channel object.
        Args:
            host (Optional[str]): The host for the channel to use.
            credentials (Optional[~.Credentials]): The
                authorization credentials to attach to requests. These
                credentials identify this application to the service. If
                none are specified, the client will attempt to ascertain
                the credentials from the environment.
            credentials_file (Optional[str]): A file with credentials that can
                be loaded with :func:`google.auth.load_credentials_from_file`.
                This argument is mutually exclusive with credentials.
            scopes (Optional[Sequence[str]]): A optional list of scopes needed for this
                service. These are only used when credentials are not specified and
                are passed to :func:`google.auth.default`.
            quota_project_id (Optional[str]): An optional project to use for billing
                and quota.
            kwargs (Optional[dict]): Keyword arguments, which are passed to the
                channel creation.
        Returns:
            grpc.Channel: A gRPC channel object.

        Raises:
            google.api_core.exceptions.DuplicateCredentialArgs: If both ``credentials``
              and ``credentials_file`` are passed.
        """

        return grpc_helpers.create_channel(
            host,
            credentials=credentials,
            credentials_file=credentials_file,
            quota_project_id=quota_project_id,
            default_scopes=cls.AUTH_SCOPES,
            scopes=scopes,
            default_host=cls.DEFAULT_HOST,
            **kwargs
        )

    @property
    def grpc_channel(self) -> grpc.Channel:
        """Return the channel designed to connect to this service.
        """
        return self._grpc_channel

    @property
    def repeat_data_body(self) -> Callable[
            [compliance.RepeatRequest],
            compliance.RepeatResponse]:
        r"""Return a callable for the repeat data body method over gRPC.

        This method echoes the ComplianceData request. This
        method exercises sending the entire request object in
        the REST body.

        Returns:
            Callable[[~.RepeatRequest],
                    ~.RepeatResponse]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if 'repeat_data_body' not in self._stubs:
            self._stubs['repeat_data_body'] = self.grpc_channel.unary_unary(
                '/google.showcase.v1beta1.Compliance/RepeatDataBody',
                request_serializer=compliance.RepeatRequest.serialize,
                response_deserializer=compliance.RepeatResponse.deserialize,
            )
        return self._stubs['repeat_data_body']

    @property
    def repeat_data_body_info(self) -> Callable[
            [compliance.RepeatRequest],
            compliance.RepeatResponse]:
        r"""Return a callable for the repeat data body info method over gRPC.

        This method echoes the ComplianceData request. This
        method exercises sending the a message-type field in the
        REST body. Per AIP-127, only top-level, non-repeated
        fields can be sent this way.

        Returns:
            Callable[[~.RepeatRequest],
                    ~.RepeatResponse]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if 'repeat_data_body_info' not in self._stubs:
            self._stubs['repeat_data_body_info'] = self.grpc_channel.unary_unary(
                '/google.showcase.v1beta1.Compliance/RepeatDataBodyInfo',
                request_serializer=compliance.RepeatRequest.serialize,
                response_deserializer=compliance.RepeatResponse.deserialize,
            )
        return self._stubs['repeat_data_body_info']

    @property
    def repeat_data_query(self) -> Callable[
            [compliance.RepeatRequest],
            compliance.RepeatResponse]:
        r"""Return a callable for the repeat data query method over gRPC.

        This method echoes the ComplianceData request. This
        method exercises sending all request fields as query
        parameters.

        Returns:
            Callable[[~.RepeatRequest],
                    ~.RepeatResponse]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if 'repeat_data_query' not in self._stubs:
            self._stubs['repeat_data_query'] = self.grpc_channel.unary_unary(
                '/google.showcase.v1beta1.Compliance/RepeatDataQuery',
                request_serializer=compliance.RepeatRequest.serialize,
                response_deserializer=compliance.RepeatResponse.deserialize,
            )
        return self._stubs['repeat_data_query']

    @property
    def repeat_data_simple_path(self) -> Callable[
            [compliance.RepeatRequest],
            compliance.RepeatResponse]:
        r"""Return a callable for the repeat data simple path method over gRPC.

        This method echoes the ComplianceData request. This method
        exercises sending some parameters as "simple" path variables
        (i.e., of the form "/bar/{foo}" rather than "/{foo=bar/*}"), and
        the rest as query parameters.

        Returns:
            Callable[[~.RepeatRequest],
                    ~.RepeatResponse]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if 'repeat_data_simple_path' not in self._stubs:
            self._stubs['repeat_data_simple_path'] = self.grpc_channel.unary_unary(
                '/google.showcase.v1beta1.Compliance/RepeatDataSimplePath',
                request_serializer=compliance.RepeatRequest.serialize,
                response_deserializer=compliance.RepeatResponse.deserialize,
            )
        return self._stubs['repeat_data_simple_path']

    @property
    def repeat_data_path_resource(self) -> Callable[
            [compliance.RepeatRequest],
            compliance.RepeatResponse]:
        r"""Return a callable for the repeat data path resource method over gRPC.

        Same as RepeatDataSimplePath, but with a path
        resource.

        Returns:
            Callable[[~.RepeatRequest],
                    ~.RepeatResponse]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if 'repeat_data_path_resource' not in self._stubs:
            self._stubs['repeat_data_path_resource'] = self.grpc_channel.unary_unary(
                '/google.showcase.v1beta1.Compliance/RepeatDataPathResource',
                request_serializer=compliance.RepeatRequest.serialize,
                response_deserializer=compliance.RepeatResponse.deserialize,
            )
        return self._stubs['repeat_data_path_resource']

    @property
    def repeat_data_path_trailing_resource(self) -> Callable[
            [compliance.RepeatRequest],
            compliance.RepeatResponse]:
        r"""Return a callable for the repeat data path trailing
        resource method over gRPC.

        Same as RepeatDataSimplePath, but with a trailing
        resource.

        Returns:
            Callable[[~.RepeatRequest],
                    ~.RepeatResponse]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if 'repeat_data_path_trailing_resource' not in self._stubs:
            self._stubs['repeat_data_path_trailing_resource'] = self.grpc_channel.unary_unary(
                '/google.showcase.v1beta1.Compliance/RepeatDataPathTrailingResource',
                request_serializer=compliance.RepeatRequest.serialize,
                response_deserializer=compliance.RepeatResponse.deserialize,
            )
        return self._stubs['repeat_data_path_trailing_resource']

    @property
    def repeat_data_body_put(self) -> Callable[
            [compliance.RepeatRequest],
            compliance.RepeatResponse]:
        r"""Return a callable for the repeat data body put method over gRPC.

        This method echoes the ComplianceData request, using
        the HTTP PUT method.

        Returns:
            Callable[[~.RepeatRequest],
                    ~.RepeatResponse]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if 'repeat_data_body_put' not in self._stubs:
            self._stubs['repeat_data_body_put'] = self.grpc_channel.unary_unary(
                '/google.showcase.v1beta1.Compliance/RepeatDataBodyPut',
                request_serializer=compliance.RepeatRequest.serialize,
                response_deserializer=compliance.RepeatResponse.deserialize,
            )
        return self._stubs['repeat_data_body_put']

    @property
    def repeat_data_body_patch(self) -> Callable[
            [compliance.RepeatRequest],
            compliance.RepeatResponse]:
        r"""Return a callable for the repeat data body patch method over gRPC.

        This method echoes the ComplianceData request, using
        the HTTP PATCH method.

        Returns:
            Callable[[~.RepeatRequest],
                    ~.RepeatResponse]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if 'repeat_data_body_patch' not in self._stubs:
            self._stubs['repeat_data_body_patch'] = self.grpc_channel.unary_unary(
                '/google.showcase.v1beta1.Compliance/RepeatDataBodyPatch',
                request_serializer=compliance.RepeatRequest.serialize,
                response_deserializer=compliance.RepeatResponse.deserialize,
            )
        return self._stubs['repeat_data_body_patch']

    @property
    def get_enum(self) -> Callable[
            [compliance.EnumRequest],
            compliance.EnumResponse]:
        r"""Return a callable for the get enum method over gRPC.

        This method requests an enum value from the server.
        Depending on the contents of EnumRequest, the enum value
        returned will be a known enum declared in the .proto
        file, or a made-up enum value the is unknown to the
        client. To verify that clients can round-trip unknown
        enum vaues they receive, use the response from this RPC
        as the request to VerifyEnum()

        The values of enums sent by the server when a known or
        unknown value is requested will be the same within a
        single Showcase server run (this is needed for
        VerifyEnum() to work) but are not guaranteed to be the
        same across separate Showcase server runs.

        Returns:
            Callable[[~.EnumRequest],
                    ~.EnumResponse]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if 'get_enum' not in self._stubs:
            self._stubs['get_enum'] = self.grpc_channel.unary_unary(
                '/google.showcase.v1beta1.Compliance/GetEnum',
                request_serializer=compliance.EnumRequest.serialize,
                response_deserializer=compliance.EnumResponse.deserialize,
            )
        return self._stubs['get_enum']

    @property
    def verify_enum(self) -> Callable[
            [compliance.EnumResponse],
            compliance.EnumResponse]:
        r"""Return a callable for the verify enum method over gRPC.

        This method is used to verify that clients can
        round-trip enum values, which is particularly important
        for unknown enum values over REST. VerifyEnum() verifies
        that its request, which is presumably the response that
        the client previously got to a GetEnum(), contains the
        correct data. If so, it responds with the same
        EnumResponse; otherwise, the RPC errors.

        This works because the values of enums sent by the
        server when a known or unknown value is requested will
        be the same within a single Showcase server run,
        although they are not guaranteed to be the same across
        separate Showcase server runs.

        Returns:
            Callable[[~.EnumResponse],
                    ~.EnumResponse]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if 'verify_enum' not in self._stubs:
            self._stubs['verify_enum'] = self.grpc_channel.unary_unary(
                '/google.showcase.v1beta1.Compliance/VerifyEnum',
                request_serializer=compliance.EnumResponse.serialize,
                response_deserializer=compliance.EnumResponse.deserialize,
            )
        return self._stubs['verify_enum']

    def close(self):
        self.grpc_channel.close()

    @property
    def delete_operation(
        self,
    ) -> Callable[[operations_pb2.DeleteOperationRequest], None]:
        r"""Return a callable for the delete_operation method over gRPC.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "delete_operation" not in self._stubs:
            self._stubs["delete_operation"] = self.grpc_channel.unary_unary(
                "/google.longrunning.Operations/DeleteOperation",
                request_serializer=operations_pb2.DeleteOperationRequest.SerializeToString,
                response_deserializer=None,
            )
        return self._stubs["delete_operation"]

    @property
    def cancel_operation(
        self,
    ) -> Callable[[operations_pb2.CancelOperationRequest], None]:
        r"""Return a callable for the cancel_operation method over gRPC.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "cancel_operation" not in self._stubs:
            self._stubs["cancel_operation"] = self.grpc_channel.unary_unary(
                "/google.longrunning.Operations/CancelOperation",
                request_serializer=operations_pb2.CancelOperationRequest.SerializeToString,
                response_deserializer=None,
            )
        return self._stubs["cancel_operation"]

    @property
    def get_operation(
        self,
    ) -> Callable[[operations_pb2.GetOperationRequest], operations_pb2.Operation]:
        r"""Return a callable for the get_operation method over gRPC.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "get_operation" not in self._stubs:
            self._stubs["get_operation"] = self.grpc_channel.unary_unary(
                "/google.longrunning.Operations/GetOperation",
                request_serializer=operations_pb2.GetOperationRequest.SerializeToString,
                response_deserializer=operations_pb2.Operation.FromString,
            )
        return self._stubs["get_operation"]

    @property
    def list_operations(
        self,
    ) -> Callable[[operations_pb2.ListOperationsRequest], operations_pb2.ListOperationsResponse]:
        r"""Return a callable for the list_operations method over gRPC.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "list_operations" not in self._stubs:
            self._stubs["list_operations"] = self.grpc_channel.unary_unary(
                "/google.longrunning.Operations/ListOperations",
                request_serializer=operations_pb2.ListOperationsRequest.SerializeToString,
                response_deserializer=operations_pb2.ListOperationsResponse.FromString,
            )
        return self._stubs["list_operations"]

    @property
    def list_locations(
        self,
    ) -> Callable[[locations_pb2.ListLocationsRequest], locations_pb2.ListLocationsResponse]:
        r"""Return a callable for the list locations method over gRPC.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "list_locations" not in self._stubs:
            self._stubs["list_locations"] = self.grpc_channel.unary_unary(
                "/google.cloud.location.Locations/ListLocations",
                request_serializer=locations_pb2.ListLocationsRequest.SerializeToString,
                response_deserializer=locations_pb2.ListLocationsResponse.FromString,
            )
        return self._stubs["list_locations"]

    @property
    def get_location(
        self,
    ) -> Callable[[locations_pb2.GetLocationRequest], locations_pb2.Location]:
        r"""Return a callable for the list locations method over gRPC.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "get_location" not in self._stubs:
            self._stubs["get_location"] = self.grpc_channel.unary_unary(
                "/google.cloud.location.Locations/GetLocation",
                request_serializer=locations_pb2.GetLocationRequest.SerializeToString,
                response_deserializer=locations_pb2.Location.FromString,
            )
        return self._stubs["get_location"]

    @property
    def set_iam_policy(
        self,
    ) -> Callable[[iam_policy_pb2.SetIamPolicyRequest], policy_pb2.Policy]:
        r"""Return a callable for the set iam policy method over gRPC.
        Sets the IAM access control policy on the specified
        function. Replaces any existing policy.
        Returns:
            Callable[[~.SetIamPolicyRequest],
                    ~.Policy]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "set_iam_policy" not in self._stubs:
            self._stubs["set_iam_policy"] = self.grpc_channel.unary_unary(
                "/google.iam.v1.IAMPolicy/SetIamPolicy",
                request_serializer=iam_policy_pb2.SetIamPolicyRequest.SerializeToString,
                response_deserializer=policy_pb2.Policy.FromString,
            )
        return self._stubs["set_iam_policy"]

    @property
    def get_iam_policy(
        self,
    ) -> Callable[[iam_policy_pb2.GetIamPolicyRequest], policy_pb2.Policy]:
        r"""Return a callable for the get iam policy method over gRPC.
        Gets the IAM access control policy for a function.
        Returns an empty policy if the function exists and does
        not have a policy set.
        Returns:
            Callable[[~.GetIamPolicyRequest],
                    ~.Policy]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "get_iam_policy" not in self._stubs:
            self._stubs["get_iam_policy"] = self.grpc_channel.unary_unary(
                "/google.iam.v1.IAMPolicy/GetIamPolicy",
                request_serializer=iam_policy_pb2.GetIamPolicyRequest.SerializeToString,
                response_deserializer=policy_pb2.Policy.FromString,
            )
        return self._stubs["get_iam_policy"]

    @property
    def test_iam_permissions(
        self,
    ) -> Callable[
        [iam_policy_pb2.TestIamPermissionsRequest], iam_policy_pb2.TestIamPermissionsResponse
    ]:
        r"""Return a callable for the test iam permissions method over gRPC.
        Tests the specified permissions against the IAM access control
        policy for a function. If the function does not exist, this will
        return an empty set of permissions, not a NOT_FOUND error.
        Returns:
            Callable[[~.TestIamPermissionsRequest],
                    ~.TestIamPermissionsResponse]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "test_iam_permissions" not in self._stubs:
            self._stubs["test_iam_permissions"] = self.grpc_channel.unary_unary(
                "/google.iam.v1.IAMPolicy/TestIamPermissions",
                request_serializer=iam_policy_pb2.TestIamPermissionsRequest.SerializeToString,
                response_deserializer=iam_policy_pb2.TestIamPermissionsResponse.FromString,
            )
        return self._stubs["test_iam_permissions"]

    @property
    def kind(self) -> str:
        return "grpc"


__all__ = (
    'ComplianceGrpcTransport',
)
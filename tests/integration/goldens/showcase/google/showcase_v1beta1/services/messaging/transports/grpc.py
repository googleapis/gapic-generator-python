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
from google.api_core import operations_v1
from google.api_core import gapic_v1
import google.auth                         # type: ignore
from google.auth import credentials as ga_credentials  # type: ignore
from google.auth.transport.grpc import SslCredentials  # type: ignore

import grpc  # type: ignore

from google.cloud.location import locations_pb2 # type: ignore
from google.iam.v1 import iam_policy_pb2  # type: ignore
from google.iam.v1 import policy_pb2  # type: ignore
from google.longrunning import operations_pb2 # type: ignore
from google.protobuf import empty_pb2  # type: ignore
from google.showcase_v1beta1.types import messaging
from .base import MessagingTransport, DEFAULT_CLIENT_INFO


class MessagingGrpcTransport(MessagingTransport):
    """gRPC backend transport for Messaging.

    A simple messaging service that implements chat rooms and
    profile posts.
    This messaging service showcases the features that API clients
    generated by gapic-generators implement.

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
        self._operations_client: Optional[operations_v1.OperationsClient] = None

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
    def operations_client(self) -> operations_v1.OperationsClient:
        """Create the client designed to process long-running operations.

        This property caches on the instance; repeated calls return the same
        client.
        """
        # Quick check: Only create a new client if we do not already have one.
        if self._operations_client is None:
            self._operations_client = operations_v1.OperationsClient(
                self.grpc_channel
            )

        # Return the client from cache.
        return self._operations_client

    @property
    def create_room(self) -> Callable[
            [messaging.CreateRoomRequest],
            messaging.Room]:
        r"""Return a callable for the create room method over gRPC.

        Creates a room.

        Returns:
            Callable[[~.CreateRoomRequest],
                    ~.Room]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if 'create_room' not in self._stubs:
            self._stubs['create_room'] = self.grpc_channel.unary_unary(
                '/google.showcase.v1beta1.Messaging/CreateRoom',
                request_serializer=messaging.CreateRoomRequest.serialize,
                response_deserializer=messaging.Room.deserialize,
            )
        return self._stubs['create_room']

    @property
    def get_room(self) -> Callable[
            [messaging.GetRoomRequest],
            messaging.Room]:
        r"""Return a callable for the get room method over gRPC.

        Retrieves the Room with the given resource name.

        Returns:
            Callable[[~.GetRoomRequest],
                    ~.Room]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if 'get_room' not in self._stubs:
            self._stubs['get_room'] = self.grpc_channel.unary_unary(
                '/google.showcase.v1beta1.Messaging/GetRoom',
                request_serializer=messaging.GetRoomRequest.serialize,
                response_deserializer=messaging.Room.deserialize,
            )
        return self._stubs['get_room']

    @property
    def update_room(self) -> Callable[
            [messaging.UpdateRoomRequest],
            messaging.Room]:
        r"""Return a callable for the update room method over gRPC.

        Updates a room.

        Returns:
            Callable[[~.UpdateRoomRequest],
                    ~.Room]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if 'update_room' not in self._stubs:
            self._stubs['update_room'] = self.grpc_channel.unary_unary(
                '/google.showcase.v1beta1.Messaging/UpdateRoom',
                request_serializer=messaging.UpdateRoomRequest.serialize,
                response_deserializer=messaging.Room.deserialize,
            )
        return self._stubs['update_room']

    @property
    def delete_room(self) -> Callable[
            [messaging.DeleteRoomRequest],
            empty_pb2.Empty]:
        r"""Return a callable for the delete room method over gRPC.

        Deletes a room and all of its blurbs.

        Returns:
            Callable[[~.DeleteRoomRequest],
                    ~.Empty]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if 'delete_room' not in self._stubs:
            self._stubs['delete_room'] = self.grpc_channel.unary_unary(
                '/google.showcase.v1beta1.Messaging/DeleteRoom',
                request_serializer=messaging.DeleteRoomRequest.serialize,
                response_deserializer=empty_pb2.Empty.FromString,
            )
        return self._stubs['delete_room']

    @property
    def list_rooms(self) -> Callable[
            [messaging.ListRoomsRequest],
            messaging.ListRoomsResponse]:
        r"""Return a callable for the list rooms method over gRPC.

        Lists all chat rooms.

        Returns:
            Callable[[~.ListRoomsRequest],
                    ~.ListRoomsResponse]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if 'list_rooms' not in self._stubs:
            self._stubs['list_rooms'] = self.grpc_channel.unary_unary(
                '/google.showcase.v1beta1.Messaging/ListRooms',
                request_serializer=messaging.ListRoomsRequest.serialize,
                response_deserializer=messaging.ListRoomsResponse.deserialize,
            )
        return self._stubs['list_rooms']

    @property
    def create_blurb(self) -> Callable[
            [messaging.CreateBlurbRequest],
            messaging.Blurb]:
        r"""Return a callable for the create blurb method over gRPC.

        Creates a blurb. If the parent is a room, the blurb
        is understood to be a message in that room. If the
        parent is a profile, the blurb is understood to be a
        post on the profile.

        Returns:
            Callable[[~.CreateBlurbRequest],
                    ~.Blurb]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if 'create_blurb' not in self._stubs:
            self._stubs['create_blurb'] = self.grpc_channel.unary_unary(
                '/google.showcase.v1beta1.Messaging/CreateBlurb',
                request_serializer=messaging.CreateBlurbRequest.serialize,
                response_deserializer=messaging.Blurb.deserialize,
            )
        return self._stubs['create_blurb']

    @property
    def get_blurb(self) -> Callable[
            [messaging.GetBlurbRequest],
            messaging.Blurb]:
        r"""Return a callable for the get blurb method over gRPC.

        Retrieves the Blurb with the given resource name.

        Returns:
            Callable[[~.GetBlurbRequest],
                    ~.Blurb]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if 'get_blurb' not in self._stubs:
            self._stubs['get_blurb'] = self.grpc_channel.unary_unary(
                '/google.showcase.v1beta1.Messaging/GetBlurb',
                request_serializer=messaging.GetBlurbRequest.serialize,
                response_deserializer=messaging.Blurb.deserialize,
            )
        return self._stubs['get_blurb']

    @property
    def update_blurb(self) -> Callable[
            [messaging.UpdateBlurbRequest],
            messaging.Blurb]:
        r"""Return a callable for the update blurb method over gRPC.

        Updates a blurb.

        Returns:
            Callable[[~.UpdateBlurbRequest],
                    ~.Blurb]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if 'update_blurb' not in self._stubs:
            self._stubs['update_blurb'] = self.grpc_channel.unary_unary(
                '/google.showcase.v1beta1.Messaging/UpdateBlurb',
                request_serializer=messaging.UpdateBlurbRequest.serialize,
                response_deserializer=messaging.Blurb.deserialize,
            )
        return self._stubs['update_blurb']

    @property
    def delete_blurb(self) -> Callable[
            [messaging.DeleteBlurbRequest],
            empty_pb2.Empty]:
        r"""Return a callable for the delete blurb method over gRPC.

        Deletes a blurb.

        Returns:
            Callable[[~.DeleteBlurbRequest],
                    ~.Empty]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if 'delete_blurb' not in self._stubs:
            self._stubs['delete_blurb'] = self.grpc_channel.unary_unary(
                '/google.showcase.v1beta1.Messaging/DeleteBlurb',
                request_serializer=messaging.DeleteBlurbRequest.serialize,
                response_deserializer=empty_pb2.Empty.FromString,
            )
        return self._stubs['delete_blurb']

    @property
    def list_blurbs(self) -> Callable[
            [messaging.ListBlurbsRequest],
            messaging.ListBlurbsResponse]:
        r"""Return a callable for the list blurbs method over gRPC.

        Lists blurbs for a specific chat room or user profile
        depending on the parent resource name.

        Returns:
            Callable[[~.ListBlurbsRequest],
                    ~.ListBlurbsResponse]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if 'list_blurbs' not in self._stubs:
            self._stubs['list_blurbs'] = self.grpc_channel.unary_unary(
                '/google.showcase.v1beta1.Messaging/ListBlurbs',
                request_serializer=messaging.ListBlurbsRequest.serialize,
                response_deserializer=messaging.ListBlurbsResponse.deserialize,
            )
        return self._stubs['list_blurbs']

    @property
    def search_blurbs(self) -> Callable[
            [messaging.SearchBlurbsRequest],
            operations_pb2.Operation]:
        r"""Return a callable for the search blurbs method over gRPC.

        This method searches through all blurbs across all
        rooms and profiles for blurbs containing to words found
        in the query. Only posts that contain an exact match of
        a queried word will be returned.

        Returns:
            Callable[[~.SearchBlurbsRequest],
                    ~.Operation]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if 'search_blurbs' not in self._stubs:
            self._stubs['search_blurbs'] = self.grpc_channel.unary_unary(
                '/google.showcase.v1beta1.Messaging/SearchBlurbs',
                request_serializer=messaging.SearchBlurbsRequest.serialize,
                response_deserializer=operations_pb2.Operation.FromString,
            )
        return self._stubs['search_blurbs']

    @property
    def stream_blurbs(self) -> Callable[
            [messaging.StreamBlurbsRequest],
            messaging.StreamBlurbsResponse]:
        r"""Return a callable for the stream blurbs method over gRPC.

        This returns a stream that emits the blurbs that are
        created for a particular chat room or user profile.

        Returns:
            Callable[[~.StreamBlurbsRequest],
                    ~.StreamBlurbsResponse]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if 'stream_blurbs' not in self._stubs:
            self._stubs['stream_blurbs'] = self.grpc_channel.unary_stream(
                '/google.showcase.v1beta1.Messaging/StreamBlurbs',
                request_serializer=messaging.StreamBlurbsRequest.serialize,
                response_deserializer=messaging.StreamBlurbsResponse.deserialize,
            )
        return self._stubs['stream_blurbs']

    @property
    def send_blurbs(self) -> Callable[
            [messaging.CreateBlurbRequest],
            messaging.SendBlurbsResponse]:
        r"""Return a callable for the send blurbs method over gRPC.

        This is a stream to create multiple blurbs. If an
        invalid blurb is requested to be created, the stream
        will close with an error.

        Returns:
            Callable[[~.CreateBlurbRequest],
                    ~.SendBlurbsResponse]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if 'send_blurbs' not in self._stubs:
            self._stubs['send_blurbs'] = self.grpc_channel.stream_unary(
                '/google.showcase.v1beta1.Messaging/SendBlurbs',
                request_serializer=messaging.CreateBlurbRequest.serialize,
                response_deserializer=messaging.SendBlurbsResponse.deserialize,
            )
        return self._stubs['send_blurbs']

    @property
    def connect(self) -> Callable[
            [messaging.ConnectRequest],
            messaging.StreamBlurbsResponse]:
        r"""Return a callable for the connect method over gRPC.

        This method starts a bidirectional stream that
        receives all blurbs that are being created after the
        stream has started and sends requests to create blurbs.
        If an invalid blurb is requested to be created, the
        stream will close with an error.

        Returns:
            Callable[[~.ConnectRequest],
                    ~.StreamBlurbsResponse]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if 'connect' not in self._stubs:
            self._stubs['connect'] = self.grpc_channel.stream_stream(
                '/google.showcase.v1beta1.Messaging/Connect',
                request_serializer=messaging.ConnectRequest.serialize,
                response_deserializer=messaging.StreamBlurbsResponse.deserialize,
            )
        return self._stubs['connect']

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
    'MessagingGrpcTransport',
)

# -*- coding: utf-8 -*-
# Copyright 2022 Google LLC
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
import proto  # type: ignore

from google.protobuf import field_mask_pb2  # type: ignore
from google.protobuf import timestamp_pb2  # type: ignore


__protobuf__ = proto.module(
    package='google.cloud.redis.v1',
    manifest={
        'Instance',
        'ListInstancesRequest',
        'ListInstancesResponse',
        'GetInstanceRequest',
        'CreateInstanceRequest',
        'UpdateInstanceRequest',
        'UpgradeInstanceRequest',
        'DeleteInstanceRequest',
        'GcsSource',
        'InputConfig',
        'ImportInstanceRequest',
        'GcsDestination',
        'OutputConfig',
        'ExportInstanceRequest',
        'FailoverInstanceRequest',
        'OperationMetadata',
        'LocationMetadata',
        'ZoneMetadata',
    },
)

from .requests import (
        ListInstancesRequest,
        GetInstanceRequest,
        CreateInstanceRequest,
        UpdateInstanceRequest,
        UpgradeInstanceRequest,
        DeleteInstanceRequest,
        ImportInstanceRequest,
        ExportInstanceRequest,
        FailoverInstanceRequest,
)

from .responses import (
        ListInstancesResponse,
)


class Instance(proto.Message):
    r"""A Google Cloud Redis instance.

    Attributes:
        name (str):
            Required. Unique name of the resource in this scope
            including project and location using the form:
            ``projects/{project_id}/locations/{location_id}/instances/{instance_id}``

            Note: Redis instances are managed and addressed at regional
            level so location_id here refers to a GCP region; however,
            users may choose which specific zone (or collection of zones
            for cross-zone instances) an instance should be provisioned
            in. Refer to
            [location_id][google.cloud.redis.v1.Instance.location_id]
            and
            [alternative_location_id][google.cloud.redis.v1.Instance.alternative_location_id]
            fields for more details.
        display_name (str):
            An arbitrary and optional user-provided name
            for the instance.
        labels (Mapping[str, str]):
            Resource labels to represent user provided
            metadata
        location_id (str):
            Optional. The zone where the instance will be provisioned.
            If not provided, the service will choose a zone for the
            instance. For STANDARD_HA tier, instances will be created
            across two zones for protection against zonal failures. If
            [alternative_location_id][google.cloud.redis.v1.Instance.alternative_location_id]
            is also provided, it must be different from
            [location_id][google.cloud.redis.v1.Instance.location_id].
        alternative_location_id (str):
            Optional. Only applicable to STANDARD_HA tier which protects
            the instance against zonal failures by provisioning it
            across two zones. If provided, it must be a different zone
            from the one provided in
            [location_id][google.cloud.redis.v1.Instance.location_id].
        redis_version (str):
            Optional. The version of Redis software. If not provided,
            latest supported version will be used. Currently, the
            supported values are:

            -  ``REDIS_3_2`` for Redis 3.2 compatibility
            -  ``REDIS_4_0`` for Redis 4.0 compatibility (default)
            -  ``REDIS_5_0`` for Redis 5.0 compatibility
        reserved_ip_range (str):
            Optional. The CIDR range of internal
            addresses that are reserved for this instance.
            If not provided, the service will choose an
            unused /29 block, for example, 10.0.0.0/29 or
            192.168.0.0/29. Ranges must be unique and
            non-overlapping with existing subnets in an
            authorized network.
        host (str):
            Output only. Hostname or IP address of the
            exposed Redis endpoint used by clients to
            connect to the service.
        port (int):
            Output only. The port number of the exposed
            Redis endpoint.
        current_location_id (str):
            Output only. The current zone where the Redis endpoint is
            placed. For Basic Tier instances, this will always be the
            same as the
            [location_id][google.cloud.redis.v1.Instance.location_id]
            provided by the user at creation time. For Standard Tier
            instances, this can be either
            [location_id][google.cloud.redis.v1.Instance.location_id] or
            [alternative_location_id][google.cloud.redis.v1.Instance.alternative_location_id]
            and can change after a failover event.
        create_time (google.protobuf.timestamp_pb2.Timestamp):
            Output only. The time the instance was
            created.
        state (google.cloud.redis_v1.types.Instance.State):
            Output only. The current state of this
            instance.
        status_message (str):
            Output only. Additional information about the
            current status of this instance, if available.
        redis_configs (Mapping[str, str]):
            Optional. Redis configuration parameters, according to
            http://redis.io/topics/config. Currently, the only supported
            parameters are:

            Redis version 3.2 and newer:

            -  maxmemory-policy
            -  notify-keyspace-events

            Redis version 4.0 and newer:

            -  activedefrag
            -  lfu-decay-time
            -  lfu-log-factor
            -  maxmemory-gb

            Redis version 5.0 and newer:

            -  stream-node-max-bytes
            -  stream-node-max-entries
        tier (google.cloud.redis_v1.types.Instance.Tier):
            Required. The service tier of the instance.
        memory_size_gb (int):
            Required. Redis memory size in GiB.
        authorized_network (str):
            Optional. The full name of the Google Compute Engine
            `network <https://cloud.google.com/vpc/docs/vpc>`__ to which
            the instance is connected. If left unspecified, the
            ``default`` network will be used.
        persistence_iam_identity (str):
            Output only. Cloud IAM identity used by import / export
            operations to transfer data to/from Cloud Storage. Format is
            "serviceAccount:<service_account_email>". The value may
            change over time for a given instance so should be checked
            before each import/export operation.
        connect_mode (google.cloud.redis_v1.types.Instance.ConnectMode):
            Optional. The network connect mode of the Redis instance. If
            not provided, the connect mode defaults to DIRECT_PEERING.
    """
    class State(proto.Enum):
        r"""Represents the different states of a Redis instance."""
        STATE_UNSPECIFIED = 0
        CREATING = 1
        READY = 2
        UPDATING = 3
        DELETING = 4
        REPAIRING = 5
        MAINTENANCE = 6
        IMPORTING = 8
        FAILING_OVER = 9

    class Tier(proto.Enum):
        r"""Available service tiers to choose from"""
        TIER_UNSPECIFIED = 0
        BASIC = 1
        STANDARD_HA = 3

    class ConnectMode(proto.Enum):
        r"""Available connection modes."""
        CONNECT_MODE_UNSPECIFIED = 0
        DIRECT_PEERING = 1
        PRIVATE_SERVICE_ACCESS = 2

    name = proto.Field(
        proto.STRING,
        number=1,
    )
    display_name = proto.Field(
        proto.STRING,
        number=2,
    )
    labels = proto.MapField(
        proto.STRING,
        proto.STRING,
        number=3,
    )
    location_id = proto.Field(
        proto.STRING,
        number=4,
    )
    alternative_location_id = proto.Field(
        proto.STRING,
        number=5,
    )
    redis_version = proto.Field(
        proto.STRING,
        number=7,
    )
    reserved_ip_range = proto.Field(
        proto.STRING,
        number=9,
    )
    host = proto.Field(
        proto.STRING,
        number=10,
    )
    port = proto.Field(
        proto.INT32,
        number=11,
    )
    current_location_id = proto.Field(
        proto.STRING,
        number=12,
    )
    create_time = proto.Field(
        proto.MESSAGE,
        number=13,
        message=timestamp_pb2.Timestamp,
    )
    state = proto.Field(
        proto.ENUM,
        number=14,
        enum=State,
    )
    status_message = proto.Field(
        proto.STRING,
        number=15,
    )
    redis_configs = proto.MapField(
        proto.STRING,
        proto.STRING,
        number=16,
    )
    tier = proto.Field(
        proto.ENUM,
        number=17,
        enum=Tier,
    )
    memory_size_gb = proto.Field(
        proto.INT32,
        number=18,
    )
    authorized_network = proto.Field(
        proto.STRING,
        number=20,
    )
    persistence_iam_identity = proto.Field(
        proto.STRING,
        number=21,
    )
    connect_mode = proto.Field(
        proto.ENUM,
        number=22,
        enum=ConnectMode,
    )


class GcsSource(proto.Message):
    r"""The Cloud Storage location for the input content

    Attributes:
        uri (str):
            Required. Source data URI. (e.g.
            'gs://my_bucket/my_object').
    """

    uri = proto.Field(
        proto.STRING,
        number=1,
    )


class InputConfig(proto.Message):
    r"""The input content

    .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

    Attributes:
        gcs_source (google.cloud.redis_v1.types.GcsSource):
            Google Cloud Storage location where input
            content is located.

            This field is a member of `oneof`_ ``source``.
    """

    gcs_source = proto.Field(
        proto.MESSAGE,
        number=1,
        oneof='source',
        message='GcsSource',
    )


class GcsDestination(proto.Message):
    r"""The Cloud Storage location for the output content

    Attributes:
        uri (str):
            Required. Data destination URI (e.g.
            'gs://my_bucket/my_object'). Existing files will be
            overwritten.
    """

    uri = proto.Field(
        proto.STRING,
        number=1,
    )


class OutputConfig(proto.Message):
    r"""The output content

    .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

    Attributes:
        gcs_destination (google.cloud.redis_v1.types.GcsDestination):
            Google Cloud Storage destination for output
            content.

            This field is a member of `oneof`_ ``destination``.
    """

    gcs_destination = proto.Field(
        proto.MESSAGE,
        number=1,
        oneof='destination',
        message='GcsDestination',
    )


class OperationMetadata(proto.Message):
    r"""Represents the v1 metadata of the long-running operation.

    Attributes:
        create_time (google.protobuf.timestamp_pb2.Timestamp):
            Creation timestamp.
        end_time (google.protobuf.timestamp_pb2.Timestamp):
            End timestamp.
        target (str):
            Operation target.
        verb (str):
            Operation verb.
        status_detail (str):
            Operation status details.
        cancel_requested (bool):
            Specifies if cancellation was requested for
            the operation.
        api_version (str):
            API version.
    """

    create_time = proto.Field(
        proto.MESSAGE,
        number=1,
        message=timestamp_pb2.Timestamp,
    )
    end_time = proto.Field(
        proto.MESSAGE,
        number=2,
        message=timestamp_pb2.Timestamp,
    )
    target = proto.Field(
        proto.STRING,
        number=3,
    )
    verb = proto.Field(
        proto.STRING,
        number=4,
    )
    status_detail = proto.Field(
        proto.STRING,
        number=5,
    )
    cancel_requested = proto.Field(
        proto.BOOL,
        number=6,
    )
    api_version = proto.Field(
        proto.STRING,
        number=7,
    )


class LocationMetadata(proto.Message):
    r"""This location metadata represents additional configuration options
    for a given location where a Redis instance may be created. All
    fields are output only. It is returned as content of the
    ``google.cloud.location.Location.metadata`` field.

    Attributes:
        available_zones (Mapping[str, google.cloud.redis_v1.types.ZoneMetadata]):
            Output only. The set of available zones in the location. The
            map is keyed by the lowercase ID of each zone, as defined by
            GCE. These keys can be specified in ``location_id`` or
            ``alternative_location_id`` fields when creating a Redis
            instance.
    """

    available_zones = proto.MapField(
        proto.STRING,
        proto.MESSAGE,
        number=1,
        message='ZoneMetadata',
    )


class ZoneMetadata(proto.Message):
    r"""Defines specific information for a particular zone. Currently
    empty and reserved for future use only.

    """


__all__ = tuple(sorted(__protobuf__.manifest))

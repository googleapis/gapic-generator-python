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
    package='google.logging.v2',
    manifest={
        'LifecycleState',
        'LogBucket',
        'LogView',
        'LogSink',
        'BigQueryOptions',
        'ListBucketsRequest',
        'ListBucketsResponse',
        'CreateBucketRequest',
        'UpdateBucketRequest',
        'GetBucketRequest',
        'DeleteBucketRequest',
        'UndeleteBucketRequest',
        'ListViewsRequest',
        'ListViewsResponse',
        'CreateViewRequest',
        'UpdateViewRequest',
        'GetViewRequest',
        'DeleteViewRequest',
        'ListSinksRequest',
        'ListSinksResponse',
        'GetSinkRequest',
        'CreateSinkRequest',
        'UpdateSinkRequest',
        'DeleteSinkRequest',
        'LogExclusion',
        'ListExclusionsRequest',
        'ListExclusionsResponse',
        'GetExclusionRequest',
        'CreateExclusionRequest',
        'UpdateExclusionRequest',
        'DeleteExclusionRequest',
        'GetCmekSettingsRequest',
        'UpdateCmekSettingsRequest',
        'CmekSettings',
    },
)

from .requests import (
        ListBucketsRequest,
        CreateBucketRequest,
        UpdateBucketRequest,
        GetBucketRequest,
        DeleteBucketRequest,
        UndeleteBucketRequest,
        ListViewsRequest,
        CreateViewRequest,
        UpdateViewRequest,
        GetViewRequest,
        DeleteViewRequest,
        ListSinksRequest,
        GetSinkRequest,
        CreateSinkRequest,
        UpdateSinkRequest,
        DeleteSinkRequest,
        ListExclusionsRequest,
        GetExclusionRequest,
        CreateExclusionRequest,
        UpdateExclusionRequest,
        DeleteExclusionRequest,
        GetCmekSettingsRequest,
        UpdateCmekSettingsRequest,
)

from .responses import (
        ListBucketsResponse,
        ListViewsResponse,
        ListSinksResponse,
        ListExclusionsResponse,
)

class LifecycleState(proto.Enum):
    r"""LogBucket lifecycle states."""
    LIFECYCLE_STATE_UNSPECIFIED = 0
    ACTIVE = 1
    DELETE_REQUESTED = 2


class LogBucket(proto.Message):
    r"""Describes a repository of logs.

    Attributes:
        name (str):
            The resource name of the bucket. For example:
            "projects/my-project-id/locations/my-location/buckets/my-bucket-id
            The supported locations are: "global"

            For the location of ``global`` it is unspecified where logs
            are actually stored. Once a bucket has been created, the
            location can not be changed.
        description (str):
            Describes this bucket.
        create_time (google.protobuf.timestamp_pb2.Timestamp):
            Output only. The creation timestamp of the
            bucket. This is not set for any of the default
            buckets.
        update_time (google.protobuf.timestamp_pb2.Timestamp):
            Output only. The last update timestamp of the
            bucket.
        retention_days (int):
            Logs will be retained by default for this
            amount of time, after which they will
            automatically be deleted. The minimum retention
            period is 1 day. If this value is set to zero at
            bucket creation time, the default time of 30
            days will be used.
        locked (bool):
            Whether the bucket has been locked.
            The retention period on a locked bucket may not
            be changed. Locked buckets may only be deleted
            if they are empty.
        lifecycle_state (google.cloud.logging_v2.types.LifecycleState):
            Output only. The bucket lifecycle state.
    """

    name = proto.Field(
        proto.STRING,
        number=1,
    )
    description = proto.Field(
        proto.STRING,
        number=3,
    )
    create_time = proto.Field(
        proto.MESSAGE,
        number=4,
        message=timestamp_pb2.Timestamp,
    )
    update_time = proto.Field(
        proto.MESSAGE,
        number=5,
        message=timestamp_pb2.Timestamp,
    )
    retention_days = proto.Field(
        proto.INT32,
        number=11,
    )
    locked = proto.Field(
        proto.BOOL,
        number=9,
    )
    lifecycle_state = proto.Field(
        proto.ENUM,
        number=12,
        enum='LifecycleState',
    )


class LogView(proto.Message):
    r"""Describes a view over logs in a bucket.

    Attributes:
        name (str):
            The resource name of the view.
            For example
            "projects/my-project-id/locations/my-location/buckets/my-bucket-id/views/my-view
        description (str):
            Describes this view.
        create_time (google.protobuf.timestamp_pb2.Timestamp):
            Output only. The creation timestamp of the
            view.
        update_time (google.protobuf.timestamp_pb2.Timestamp):
            Output only. The last update timestamp of the
            view.
        filter (str):
            Filter that restricts which log entries in a bucket are
            visible in this view. Filters are restricted to be a logical
            AND of ==/!= of any of the following: originating
            project/folder/organization/billing account. resource type
            log id Example: SOURCE("projects/myproject") AND
            resource.type = "gce_instance" AND LOG_ID("stdout")
    """

    name = proto.Field(
        proto.STRING,
        number=1,
    )
    description = proto.Field(
        proto.STRING,
        number=3,
    )
    create_time = proto.Field(
        proto.MESSAGE,
        number=4,
        message=timestamp_pb2.Timestamp,
    )
    update_time = proto.Field(
        proto.MESSAGE,
        number=5,
        message=timestamp_pb2.Timestamp,
    )
    filter = proto.Field(
        proto.STRING,
        number=7,
    )


class LogSink(proto.Message):
    r"""Describes a sink used to export log entries to one of the
    following destinations in any project: a Cloud Storage bucket, a
    BigQuery dataset, or a Cloud Pub/Sub topic. A logs filter
    controls which log entries are exported. The sink must be
    created within a project, organization, billing account, or
    folder.


    .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

    Attributes:
        name (str):
            Required. The client-assigned sink identifier, unique within
            the project. Example: ``"my-syslog-errors-to-pubsub"``. Sink
            identifiers are limited to 100 characters and can include
            only the following characters: upper and lower-case
            alphanumeric characters, underscores, hyphens, and periods.
            First character has to be alphanumeric.
        destination (str):
            Required. The export destination:

            ::

                "storage.googleapis.com/[GCS_BUCKET]"
                "bigquery.googleapis.com/projects/[PROJECT_ID]/datasets/[DATASET]"
                "pubsub.googleapis.com/projects/[PROJECT_ID]/topics/[TOPIC_ID]"

            The sink's ``writer_identity``, set when the sink is
            created, must have permission to write to the destination or
            else the log entries are not exported. For more information,
            see `Exporting Logs with
            Sinks <https://cloud.google.com/logging/docs/api/tasks/exporting-logs>`__.
        filter (str):
            Optional. An `advanced logs
            filter <https://cloud.google.com/logging/docs/view/advanced-queries>`__.
            The only exported log entries are those that are in the
            resource owning the sink and that match the filter. For
            example:

            ::

                logName="projects/[PROJECT_ID]/logs/[LOG_ID]" AND severity>=ERROR
        description (str):
            Optional. A description of this sink.
            The maximum length of the description is 8000
            characters.
        disabled (bool):
            Optional. If set to True, then this sink is
            disabled and it does not export any log entries.
        exclusions (Sequence[google.cloud.logging_v2.types.LogExclusion]):
            Optional. Log entries that match any of the exclusion
            filters will not be exported. If a log entry is matched by
            both ``filter`` and one of ``exclusion_filters`` it will not
            be exported.
        output_version_format (google.cloud.logging_v2.types.LogSink.VersionFormat):
            Deprecated. This field is unused.
        writer_identity (str):
            Output only. An IAM identity—a service account or
            group—under which Logging writes the exported log entries to
            the sink's destination. This field is set by
            [sinks.create][google.logging.v2.ConfigServiceV2.CreateSink]
            and
            [sinks.update][google.logging.v2.ConfigServiceV2.UpdateSink]
            based on the value of ``unique_writer_identity`` in those
            methods.

            Until you grant this identity write-access to the
            destination, log entry exports from this sink will fail. For
            more information, see `Granting Access for a
            Resource <https://cloud.google.com/iam/docs/granting-roles-to-service-accounts#granting_access_to_a_service_account_for_a_resource>`__.
            Consult the destination service's documentation to determine
            the appropriate IAM roles to assign to the identity.
        include_children (bool):
            Optional. This field applies only to sinks owned by
            organizations and folders. If the field is false, the
            default, only the logs owned by the sink's parent resource
            are available for export. If the field is true, then logs
            from all the projects, folders, and billing accounts
            contained in the sink's parent resource are also available
            for export. Whether a particular log entry from the children
            is exported depends on the sink's filter expression. For
            example, if this field is true, then the filter
            ``resource.type=gce_instance`` would export all Compute
            Engine VM instance log entries from all projects in the
            sink's parent. To only export entries from certain child
            projects, filter on the project part of the log name:

            ::

                logName:("projects/test-project1/" OR "projects/test-project2/") AND
                resource.type=gce_instance
        bigquery_options (google.cloud.logging_v2.types.BigQueryOptions):
            Optional. Options that affect sinks exporting
            data to BigQuery.

            This field is a member of `oneof`_ ``options``.
        create_time (google.protobuf.timestamp_pb2.Timestamp):
            Output only. The creation timestamp of the
            sink.
            This field may not be present for older sinks.
        update_time (google.protobuf.timestamp_pb2.Timestamp):
            Output only. The last update timestamp of the
            sink.
            This field may not be present for older sinks.
    """
    class VersionFormat(proto.Enum):
        r"""Deprecated. This is unused."""
        VERSION_FORMAT_UNSPECIFIED = 0
        V2 = 1
        V1 = 2

    name = proto.Field(
        proto.STRING,
        number=1,
    )
    destination = proto.Field(
        proto.STRING,
        number=3,
    )
    filter = proto.Field(
        proto.STRING,
        number=5,
    )
    description = proto.Field(
        proto.STRING,
        number=18,
    )
    disabled = proto.Field(
        proto.BOOL,
        number=19,
    )
    exclusions = proto.RepeatedField(
        proto.MESSAGE,
        number=16,
        message='LogExclusion',
    )
    output_version_format = proto.Field(
        proto.ENUM,
        number=6,
        enum=VersionFormat,
    )
    writer_identity = proto.Field(
        proto.STRING,
        number=8,
    )
    include_children = proto.Field(
        proto.BOOL,
        number=9,
    )
    bigquery_options = proto.Field(
        proto.MESSAGE,
        number=12,
        oneof='options',
        message='BigQueryOptions',
    )
    create_time = proto.Field(
        proto.MESSAGE,
        number=13,
        message=timestamp_pb2.Timestamp,
    )
    update_time = proto.Field(
        proto.MESSAGE,
        number=14,
        message=timestamp_pb2.Timestamp,
    )


class BigQueryOptions(proto.Message):
    r"""Options that change functionality of a sink exporting data to
    BigQuery.

    Attributes:
        use_partitioned_tables (bool):
            Optional. Whether to use `BigQuery's partition
            tables <https://cloud.google.com/bigquery/docs/partitioned-tables>`__.
            By default, Logging creates dated tables based on the log
            entries' timestamps, e.g. syslog_20170523. With partitioned
            tables the date suffix is no longer present and `special
            query
            syntax <https://cloud.google.com/bigquery/docs/querying-partitioned-tables>`__
            has to be used instead. In both cases, tables are sharded
            based on UTC timezone.
        uses_timestamp_column_partitioning (bool):
            Output only. True if new timestamp column based partitioning
            is in use, false if legacy ingestion-time partitioning is in
            use. All new sinks will have this field set true and will
            use timestamp column based partitioning. If
            use_partitioned_tables is false, this value has no meaning
            and will be false. Legacy sinks using partitioned tables
            will have this field set to false.
    """

    use_partitioned_tables = proto.Field(
        proto.BOOL,
        number=1,
    )
    uses_timestamp_column_partitioning = proto.Field(
        proto.BOOL,
        number=3,
    )


class LogExclusion(proto.Message):
    r"""Specifies a set of log entries that are not to be stored in
    Logging. If your GCP resource receives a large volume of logs,
    you can use exclusions to reduce your chargeable logs.
    Exclusions are processed after log sinks, so you can export log
    entries before they are excluded. Note that organization-level
    and folder-level exclusions don't apply to child resources, and
    that you can't exclude audit log entries.

    Attributes:
        name (str):
            Required. A client-assigned identifier, such as
            ``"load-balancer-exclusion"``. Identifiers are limited to
            100 characters and can include only letters, digits,
            underscores, hyphens, and periods. First character has to be
            alphanumeric.
        description (str):
            Optional. A description of this exclusion.
        filter (str):
            Required. An `advanced logs
            filter <https://cloud.google.com/logging/docs/view/advanced-queries>`__
            that matches the log entries to be excluded. By using the
            `sample
            function <https://cloud.google.com/logging/docs/view/advanced-queries#sample>`__,
            you can exclude less than 100% of the matching log entries.
            For example, the following query matches 99% of low-severity
            log entries from Google Cloud Storage buckets:

            ``"resource.type=gcs_bucket severity<ERROR sample(insertId, 0.99)"``
        disabled (bool):
            Optional. If set to True, then this exclusion is disabled
            and it does not exclude any log entries. You can [update an
            exclusion][google.logging.v2.ConfigServiceV2.UpdateExclusion]
            to change the value of this field.
        create_time (google.protobuf.timestamp_pb2.Timestamp):
            Output only. The creation timestamp of the
            exclusion.
            This field may not be present for older
            exclusions.
        update_time (google.protobuf.timestamp_pb2.Timestamp):
            Output only. The last update timestamp of the
            exclusion.
            This field may not be present for older
            exclusions.
    """

    name = proto.Field(
        proto.STRING,
        number=1,
    )
    description = proto.Field(
        proto.STRING,
        number=2,
    )
    filter = proto.Field(
        proto.STRING,
        number=3,
    )
    disabled = proto.Field(
        proto.BOOL,
        number=4,
    )
    create_time = proto.Field(
        proto.MESSAGE,
        number=5,
        message=timestamp_pb2.Timestamp,
    )
    update_time = proto.Field(
        proto.MESSAGE,
        number=6,
        message=timestamp_pb2.Timestamp,
    )


class CmekSettings(proto.Message):
    r"""Describes the customer-managed encryption key (CMEK) settings
    associated with a project, folder, organization, billing account, or
    flexible resource.

    Note: CMEK for the Logs Router can currently only be configured for
    GCP organizations. Once configured, it applies to all projects and
    folders in the GCP organization.

    See `Enabling CMEK for Logs
    Router <https://cloud.google.com/logging/docs/routing/managed-encryption>`__
    for more information.

    Attributes:
        name (str):
            Output only. The resource name of the CMEK
            settings.
        kms_key_name (str):
            The resource name for the configured Cloud KMS key.

            KMS key name format:
            "projects/[PROJECT_ID]/locations/[LOCATION]/keyRings/[KEYRING]/cryptoKeys/[KEY]"

            For example:
            ``"projects/my-project-id/locations/my-region/keyRings/key-ring-name/cryptoKeys/key-name"``

            To enable CMEK for the Logs Router, set this field to a
            valid ``kms_key_name`` for which the associated service
            account has the required
            ``roles/cloudkms.cryptoKeyEncrypterDecrypter`` role assigned
            for the key.

            The Cloud KMS key used by the Log Router can be updated by
            changing the ``kms_key_name`` to a new valid key name.
            Encryption operations that are in progress will be completed
            with the key that was in use when they started. Decryption
            operations will be completed using the key that was used at
            the time of encryption unless access to that key has been
            revoked.

            To disable CMEK for the Logs Router, set this field to an
            empty string.

            See `Enabling CMEK for Logs
            Router <https://cloud.google.com/logging/docs/routing/managed-encryption>`__
            for more information.
        service_account_id (str):
            Output only. The service account that will be used by the
            Logs Router to access your Cloud KMS key.

            Before enabling CMEK for Logs Router, you must first assign
            the role ``roles/cloudkms.cryptoKeyEncrypterDecrypter`` to
            the service account that the Logs Router will use to access
            your Cloud KMS key. Use
            [GetCmekSettings][google.logging.v2.ConfigServiceV2.GetCmekSettings]
            to obtain the service account ID.

            See `Enabling CMEK for Logs
            Router <https://cloud.google.com/logging/docs/routing/managed-encryption>`__
            for more information.
    """

    name = proto.Field(
        proto.STRING,
        number=1,
    )
    kms_key_name = proto.Field(
        proto.STRING,
        number=2,
    )
    service_account_id = proto.Field(
        proto.STRING,
        number=3,
    )


#class _MagicProtoCompletion_google_logging_v2_5(proto.Message):
#    """
#    This is magic. This class needs to be here, so the Metaclass-proto-miracle-workings
#    could properly construct all the protobuf classes and pretend like if they were from
#    this file and not from other/requests/responses.py.
#    """
#    pass

__all__ = tuple(sorted(__protobuf__.manifest))

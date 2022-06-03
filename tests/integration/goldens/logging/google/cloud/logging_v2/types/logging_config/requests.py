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
        'ListBucketsRequest',
        'CreateBucketRequest',
        'UpdateBucketRequest',
        'GetBucketRequest',
        'DeleteBucketRequest',
        'UndeleteBucketRequest',
        'ListViewsRequest',
        'CreateViewRequest',
        'UpdateViewRequest',
        'GetViewRequest',
        'DeleteViewRequest',
        'ListSinksRequest',
        'GetSinkRequest',
        'CreateSinkRequest',
        'UpdateSinkRequest',
        'DeleteSinkRequest',
        'ListExclusionsRequest',
        'GetExclusionRequest',
        'CreateExclusionRequest',
        'UpdateExclusionRequest',
        'DeleteExclusionRequest',
        'GetCmekSettingsRequest',
        'UpdateCmekSettingsRequest',
    },
)


__manifest__ = (
        'ListBucketsRequest',
        'CreateBucketRequest',
        'UpdateBucketRequest',
        'GetBucketRequest',
        'DeleteBucketRequest',
        'UndeleteBucketRequest',
        'ListViewsRequest',
        'CreateViewRequest',
        'UpdateViewRequest',
        'GetViewRequest',
        'DeleteViewRequest',
        'ListSinksRequest',
        'GetSinkRequest',
        'CreateSinkRequest',
        'UpdateSinkRequest',
        'DeleteSinkRequest',
        'ListExclusionsRequest',
        'GetExclusionRequest',
        'CreateExclusionRequest',
        'UpdateExclusionRequest',
        'DeleteExclusionRequest',
        'GetCmekSettingsRequest',
        'UpdateCmekSettingsRequest',
)


class ListBucketsRequest(proto.Message):
    r"""The parameters to ``ListBuckets``.

    Attributes:
        parent (str):
            Required. The parent resource whose buckets are to be
            listed:

            ::

                "projects/[PROJECT_ID]/locations/[LOCATION_ID]"
                "organizations/[ORGANIZATION_ID]/locations/[LOCATION_ID]"
                "billingAccounts/[BILLING_ACCOUNT_ID]/locations/[LOCATION_ID]"
                "folders/[FOLDER_ID]/locations/[LOCATION_ID]"

            Note: The locations portion of the resource must be
            specified, but supplying the character ``-`` in place of
            [LOCATION_ID] will return all buckets.
        page_token (str):
            Optional. If present, then retrieve the next batch of
            results from the preceding call to this method.
            ``pageToken`` must be the value of ``nextPageToken`` from
            the previous response. The values of other method parameters
            should be identical to those in the previous call.
        page_size (int):
            Optional. The maximum number of results to return from this
            request. Non-positive values are ignored. The presence of
            ``nextPageToken`` in the response indicates that more
            results might be available.
    """
    __module__ = __module__.rsplit('.', maxsplit=1)[0]  # type: ignore

    parent = proto.Field(
        proto.STRING,
        number=1,
    )
    page_token = proto.Field(
        proto.STRING,
        number=2,
    )
    page_size = proto.Field(
        proto.INT32,
        number=3,
    )


class CreateBucketRequest(proto.Message):
    r"""The parameters to ``CreateBucket``.

    Attributes:
        parent (str):
            Required. The resource in which to create the bucket:

            ::

                "projects/[PROJECT_ID]/locations/[LOCATION_ID]"

            Example: ``"projects/my-logging-project/locations/global"``
        bucket_id (str):
            Required. A client-assigned identifier such as
            ``"my-bucket"``. Identifiers are limited to 100 characters
            and can include only letters, digits, underscores, hyphens,
            and periods.
        bucket (google.cloud.logging_v2.types.LogBucket):
            Required. The new bucket. The region
            specified in the new bucket must be compliant
            with any Location Restriction Org Policy. The
            name field in the bucket is ignored.
    """
    __module__ = __module__.rsplit('.', maxsplit=1)[0]  # type: ignore

    parent = proto.Field(
        proto.STRING,
        number=1,
    )
    bucket_id = proto.Field(
        proto.STRING,
        number=2,
    )
    bucket = proto.Field(
        proto.MESSAGE,
        number=3,
        message='LogBucket',
    )


class UpdateBucketRequest(proto.Message):
    r"""The parameters to ``UpdateBucket``.

    Attributes:
        name (str):
            Required. The full resource name of the bucket to update.

            ::

                "projects/[PROJECT_ID]/locations/[LOCATION_ID]/buckets/[BUCKET_ID]"
                "organizations/[ORGANIZATION_ID]/locations/[LOCATION_ID]/buckets/[BUCKET_ID]"
                "billingAccounts/[BILLING_ACCOUNT_ID]/locations/[LOCATION_ID]/buckets/[BUCKET_ID]"
                "folders/[FOLDER_ID]/locations/[LOCATION_ID]/buckets/[BUCKET_ID]"

            Example:
            ``"projects/my-project-id/locations/my-location/buckets/my-bucket-id"``.
            Also requires permission
            "resourcemanager.projects.updateLiens" to set the locked
            property
        bucket (google.cloud.logging_v2.types.LogBucket):
            Required. The updated bucket.
        update_mask (google.protobuf.field_mask_pb2.FieldMask):
            Required. Field mask that specifies the fields in ``bucket``
            that need an update. A bucket field will be overwritten if,
            and only if, it is in the update mask. ``name`` and output
            only fields cannot be updated.

            For a detailed ``FieldMask`` definition, see
            https://developers.google.com/protocol-buffers/docs/reference/google.protobuf#google.protobuf.FieldMask

            Example: ``updateMask=retention_days``.
    """
    __module__ = __module__.rsplit('.', maxsplit=1)[0]  # type: ignore

    name = proto.Field(
        proto.STRING,
        number=1,
    )
    bucket = proto.Field(
        proto.MESSAGE,
        number=2,
        message='LogBucket',
    )
    update_mask = proto.Field(
        proto.MESSAGE,
        number=4,
        message=field_mask_pb2.FieldMask,
    )


class GetBucketRequest(proto.Message):
    r"""The parameters to ``GetBucket``.

    Attributes:
        name (str):
            Required. The resource name of the bucket:

            ::

                "projects/[PROJECT_ID]/locations/[LOCATION_ID]/buckets/[BUCKET_ID]"
                "organizations/[ORGANIZATION_ID]/locations/[LOCATION_ID]/buckets/[BUCKET_ID]"
                "billingAccounts/[BILLING_ACCOUNT_ID]/locations/[LOCATION_ID]/buckets/[BUCKET_ID]"
                "folders/[FOLDER_ID]/locations/[LOCATION_ID]/buckets/[BUCKET_ID]"

            Example:
            ``"projects/my-project-id/locations/my-location/buckets/my-bucket-id"``.
    """
    __module__ = __module__.rsplit('.', maxsplit=1)[0]  # type: ignore

    name = proto.Field(
        proto.STRING,
        number=1,
    )


class DeleteBucketRequest(proto.Message):
    r"""The parameters to ``DeleteBucket``.

    Attributes:
        name (str):
            Required. The full resource name of the bucket to delete.

            ::

                "projects/[PROJECT_ID]/locations/[LOCATION_ID]/buckets/[BUCKET_ID]"
                "organizations/[ORGANIZATION_ID]/locations/[LOCATION_ID]/buckets/[BUCKET_ID]"
                "billingAccounts/[BILLING_ACCOUNT_ID]/locations/[LOCATION_ID]/buckets/[BUCKET_ID]"
                "folders/[FOLDER_ID]/locations/[LOCATION_ID]/buckets/[BUCKET_ID]"

            Example:
            ``"projects/my-project-id/locations/my-location/buckets/my-bucket-id"``.
    """
    __module__ = __module__.rsplit('.', maxsplit=1)[0]  # type: ignore

    name = proto.Field(
        proto.STRING,
        number=1,
    )


class UndeleteBucketRequest(proto.Message):
    r"""The parameters to ``UndeleteBucket``.

    Attributes:
        name (str):
            Required. The full resource name of the bucket to undelete.

            ::

                "projects/[PROJECT_ID]/locations/[LOCATION_ID]/buckets/[BUCKET_ID]"
                "organizations/[ORGANIZATION_ID]/locations/[LOCATION_ID]/buckets/[BUCKET_ID]"
                "billingAccounts/[BILLING_ACCOUNT_ID]/locations/[LOCATION_ID]/buckets/[BUCKET_ID]"
                "folders/[FOLDER_ID]/locations/[LOCATION_ID]/buckets/[BUCKET_ID]"

            Example:
            ``"projects/my-project-id/locations/my-location/buckets/my-bucket-id"``.
    """
    __module__ = __module__.rsplit('.', maxsplit=1)[0]  # type: ignore

    name = proto.Field(
        proto.STRING,
        number=1,
    )


class ListViewsRequest(proto.Message):
    r"""The parameters to ``ListViews``.

    Attributes:
        parent (str):
            Required. The bucket whose views are to be listed:

            ::

                "projects/[PROJECT_ID]/locations/[LOCATION_ID]/buckets/[BUCKET_ID]".
        page_token (str):
            Optional. If present, then retrieve the next batch of
            results from the preceding call to this method.
            ``pageToken`` must be the value of ``nextPageToken`` from
            the previous response. The values of other method parameters
            should be identical to those in the previous call.
        page_size (int):
            Optional. The maximum number of results to return from this
            request. Non-positive values are ignored. The presence of
            ``nextPageToken`` in the response indicates that more
            results might be available.
    """
    __module__ = __module__.rsplit('.', maxsplit=1)[0]  # type: ignore

    parent = proto.Field(
        proto.STRING,
        number=1,
    )
    page_token = proto.Field(
        proto.STRING,
        number=2,
    )
    page_size = proto.Field(
        proto.INT32,
        number=3,
    )


class CreateViewRequest(proto.Message):
    r"""The parameters to ``CreateView``.

    Attributes:
        parent (str):
            Required. The bucket in which to create the view

            ::

                "projects/[PROJECT_ID]/locations/[LOCATION_ID]/buckets/[BUCKET_ID]"

            Example:
            ``"projects/my-logging-project/locations/my-location/buckets/my-bucket"``
        view_id (str):
            Required. The id to use for this view.
        view (google.cloud.logging_v2.types.LogView):
            Required. The new view.
    """
    __module__ = __module__.rsplit('.', maxsplit=1)[0]  # type: ignore

    parent = proto.Field(
        proto.STRING,
        number=1,
    )
    view_id = proto.Field(
        proto.STRING,
        number=2,
    )
    view = proto.Field(
        proto.MESSAGE,
        number=3,
        message='LogView',
    )


class UpdateViewRequest(proto.Message):
    r"""The parameters to ``UpdateView``.

    Attributes:
        name (str):
            Required. The full resource name of the view to update

            ::

                "projects/[PROJECT_ID]/locations/[LOCATION_ID]/buckets/[BUCKET_ID]/views/[VIEW_ID]"

            Example:
            ``"projects/my-project-id/locations/my-location/buckets/my-bucket-id/views/my-view-id"``.
        view (google.cloud.logging_v2.types.LogView):
            Required. The updated view.
        update_mask (google.protobuf.field_mask_pb2.FieldMask):
            Optional. Field mask that specifies the fields in ``view``
            that need an update. A field will be overwritten if, and
            only if, it is in the update mask. ``name`` and output only
            fields cannot be updated.

            For a detailed ``FieldMask`` definition, see
            https://developers.google.com/protocol-buffers/docs/reference/google.protobuf#google.protobuf.FieldMask

            Example: ``updateMask=filter``.
    """
    __module__ = __module__.rsplit('.', maxsplit=1)[0]  # type: ignore

    name = proto.Field(
        proto.STRING,
        number=1,
    )
    view = proto.Field(
        proto.MESSAGE,
        number=2,
        message='LogView',
    )
    update_mask = proto.Field(
        proto.MESSAGE,
        number=4,
        message=field_mask_pb2.FieldMask,
    )


class GetViewRequest(proto.Message):
    r"""The parameters to ``GetView``.

    Attributes:
        name (str):
            Required. The resource name of the policy:

            ::

                "projects/[PROJECT_ID]/locations/[LOCATION_ID]/buckets/[BUCKET_ID]/views/[VIEW_ID]"

            Example:
            ``"projects/my-project-id/locations/my-location/buckets/my-bucket-id/views/my-view-id"``.
    """
    __module__ = __module__.rsplit('.', maxsplit=1)[0]  # type: ignore

    name = proto.Field(
        proto.STRING,
        number=1,
    )


class DeleteViewRequest(proto.Message):
    r"""The parameters to ``DeleteView``.

    Attributes:
        name (str):
            Required. The full resource name of the view to delete:

            ::

                "projects/[PROJECT_ID]/locations/[LOCATION_ID]/buckets/[BUCKET_ID]/views/[VIEW_ID]"

            Example:
            ``"projects/my-project-id/locations/my-location/buckets/my-bucket-id/views/my-view-id"``.
    """
    __module__ = __module__.rsplit('.', maxsplit=1)[0]  # type: ignore

    name = proto.Field(
        proto.STRING,
        number=1,
    )


class ListSinksRequest(proto.Message):
    r"""The parameters to ``ListSinks``.

    Attributes:
        parent (str):
            Required. The parent resource whose sinks are to be listed:

            ::

                "projects/[PROJECT_ID]"
                "organizations/[ORGANIZATION_ID]"
                "billingAccounts/[BILLING_ACCOUNT_ID]"
                "folders/[FOLDER_ID]".
        page_token (str):
            Optional. If present, then retrieve the next batch of
            results from the preceding call to this method.
            ``pageToken`` must be the value of ``nextPageToken`` from
            the previous response. The values of other method parameters
            should be identical to those in the previous call.
        page_size (int):
            Optional. The maximum number of results to return from this
            request. Non-positive values are ignored. The presence of
            ``nextPageToken`` in the response indicates that more
            results might be available.
    """
    __module__ = __module__.rsplit('.', maxsplit=1)[0]  # type: ignore

    parent = proto.Field(
        proto.STRING,
        number=1,
    )
    page_token = proto.Field(
        proto.STRING,
        number=2,
    )
    page_size = proto.Field(
        proto.INT32,
        number=3,
    )


class GetSinkRequest(proto.Message):
    r"""The parameters to ``GetSink``.

    Attributes:
        sink_name (str):
            Required. The resource name of the sink:

            ::

                "projects/[PROJECT_ID]/sinks/[SINK_ID]"
                "organizations/[ORGANIZATION_ID]/sinks/[SINK_ID]"
                "billingAccounts/[BILLING_ACCOUNT_ID]/sinks/[SINK_ID]"
                "folders/[FOLDER_ID]/sinks/[SINK_ID]"

            Example: ``"projects/my-project-id/sinks/my-sink-id"``.
    """
    __module__ = __module__.rsplit('.', maxsplit=1)[0]  # type: ignore

    sink_name = proto.Field(
        proto.STRING,
        number=1,
    )


class CreateSinkRequest(proto.Message):
    r"""The parameters to ``CreateSink``.

    Attributes:
        parent (str):
            Required. The resource in which to create the sink:

            ::

                "projects/[PROJECT_ID]"
                "organizations/[ORGANIZATION_ID]"
                "billingAccounts/[BILLING_ACCOUNT_ID]"
                "folders/[FOLDER_ID]"

            Examples: ``"projects/my-logging-project"``,
            ``"organizations/123456789"``.
        sink (google.cloud.logging_v2.types.LogSink):
            Required. The new sink, whose ``name`` parameter is a sink
            identifier that is not already in use.
        unique_writer_identity (bool):
            Optional. Determines the kind of IAM identity returned as
            ``writer_identity`` in the new sink. If this value is
            omitted or set to false, and if the sink's parent is a
            project, then the value returned as ``writer_identity`` is
            the same group or service account used by Logging before the
            addition of writer identities to this API. The sink's
            destination must be in the same project as the sink itself.

            If this field is set to true, or if the sink is owned by a
            non-project resource such as an organization, then the value
            of ``writer_identity`` will be a unique service account used
            only for exports from the new sink. For more information,
            see ``writer_identity`` in
            [LogSink][google.logging.v2.LogSink].
    """
    __module__ = __module__.rsplit('.', maxsplit=1)[0]  # type: ignore

    parent = proto.Field(
        proto.STRING,
        number=1,
    )
    sink = proto.Field(
        proto.MESSAGE,
        number=2,
        message='LogSink',
    )
    unique_writer_identity = proto.Field(
        proto.BOOL,
        number=3,
    )


class UpdateSinkRequest(proto.Message):
    r"""The parameters to ``UpdateSink``.

    Attributes:
        sink_name (str):
            Required. The full resource name of the sink to update,
            including the parent resource and the sink identifier:

            ::

                "projects/[PROJECT_ID]/sinks/[SINK_ID]"
                "organizations/[ORGANIZATION_ID]/sinks/[SINK_ID]"
                "billingAccounts/[BILLING_ACCOUNT_ID]/sinks/[SINK_ID]"
                "folders/[FOLDER_ID]/sinks/[SINK_ID]"

            Example: ``"projects/my-project-id/sinks/my-sink-id"``.
        sink (google.cloud.logging_v2.types.LogSink):
            Required. The updated sink, whose name is the same
            identifier that appears as part of ``sink_name``.
        unique_writer_identity (bool):
            Optional. See
            [sinks.create][google.logging.v2.ConfigServiceV2.CreateSink]
            for a description of this field. When updating a sink, the
            effect of this field on the value of ``writer_identity`` in
            the updated sink depends on both the old and new values of
            this field:

            -  If the old and new values of this field are both false or
               both true, then there is no change to the sink's
               ``writer_identity``.
            -  If the old value is false and the new value is true, then
               ``writer_identity`` is changed to a unique service
               account.
            -  It is an error if the old value is true and the new value
               is set to false or defaulted to false.
        update_mask (google.protobuf.field_mask_pb2.FieldMask):
            Optional. Field mask that specifies the fields in ``sink``
            that need an update. A sink field will be overwritten if,
            and only if, it is in the update mask. ``name`` and output
            only fields cannot be updated.

            An empty updateMask is temporarily treated as using the
            following mask for backwards compatibility purposes:
            destination,filter,includeChildren At some point in the
            future, behavior will be removed and specifying an empty
            updateMask will be an error.

            For a detailed ``FieldMask`` definition, see
            https://developers.google.com/protocol-buffers/docs/reference/google.protobuf#google.protobuf.FieldMask

            Example: ``updateMask=filter``.
    """
    __module__ = __module__.rsplit('.', maxsplit=1)[0]  # type: ignore

    sink_name = proto.Field(
        proto.STRING,
        number=1,
    )
    sink = proto.Field(
        proto.MESSAGE,
        number=2,
        message='LogSink',
    )
    unique_writer_identity = proto.Field(
        proto.BOOL,
        number=3,
    )
    update_mask = proto.Field(
        proto.MESSAGE,
        number=4,
        message=field_mask_pb2.FieldMask,
    )


class DeleteSinkRequest(proto.Message):
    r"""The parameters to ``DeleteSink``.

    Attributes:
        sink_name (str):
            Required. The full resource name of the sink to delete,
            including the parent resource and the sink identifier:

            ::

                "projects/[PROJECT_ID]/sinks/[SINK_ID]"
                "organizations/[ORGANIZATION_ID]/sinks/[SINK_ID]"
                "billingAccounts/[BILLING_ACCOUNT_ID]/sinks/[SINK_ID]"
                "folders/[FOLDER_ID]/sinks/[SINK_ID]"

            Example: ``"projects/my-project-id/sinks/my-sink-id"``.
    """
    __module__ = __module__.rsplit('.', maxsplit=1)[0]  # type: ignore

    sink_name = proto.Field(
        proto.STRING,
        number=1,
    )


class ListExclusionsRequest(proto.Message):
    r"""The parameters to ``ListExclusions``.

    Attributes:
        parent (str):
            Required. The parent resource whose exclusions are to be
            listed.

            ::

                "projects/[PROJECT_ID]"
                "organizations/[ORGANIZATION_ID]"
                "billingAccounts/[BILLING_ACCOUNT_ID]"
                "folders/[FOLDER_ID]".
        page_token (str):
            Optional. If present, then retrieve the next batch of
            results from the preceding call to this method.
            ``pageToken`` must be the value of ``nextPageToken`` from
            the previous response. The values of other method parameters
            should be identical to those in the previous call.
        page_size (int):
            Optional. The maximum number of results to return from this
            request. Non-positive values are ignored. The presence of
            ``nextPageToken`` in the response indicates that more
            results might be available.
    """
    __module__ = __module__.rsplit('.', maxsplit=1)[0]  # type: ignore

    parent = proto.Field(
        proto.STRING,
        number=1,
    )
    page_token = proto.Field(
        proto.STRING,
        number=2,
    )
    page_size = proto.Field(
        proto.INT32,
        number=3,
    )


class GetExclusionRequest(proto.Message):
    r"""The parameters to ``GetExclusion``.

    Attributes:
        name (str):
            Required. The resource name of an existing exclusion:

            ::

                "projects/[PROJECT_ID]/exclusions/[EXCLUSION_ID]"
                "organizations/[ORGANIZATION_ID]/exclusions/[EXCLUSION_ID]"
                "billingAccounts/[BILLING_ACCOUNT_ID]/exclusions/[EXCLUSION_ID]"
                "folders/[FOLDER_ID]/exclusions/[EXCLUSION_ID]"

            Example:
            ``"projects/my-project-id/exclusions/my-exclusion-id"``.
    """
    __module__ = __module__.rsplit('.', maxsplit=1)[0]  # type: ignore

    name = proto.Field(
        proto.STRING,
        number=1,
    )


class CreateExclusionRequest(proto.Message):
    r"""The parameters to ``CreateExclusion``.

    Attributes:
        parent (str):
            Required. The parent resource in which to create the
            exclusion:

            ::

                "projects/[PROJECT_ID]"
                "organizations/[ORGANIZATION_ID]"
                "billingAccounts/[BILLING_ACCOUNT_ID]"
                "folders/[FOLDER_ID]"

            Examples: ``"projects/my-logging-project"``,
            ``"organizations/123456789"``.
        exclusion (google.cloud.logging_v2.types.LogExclusion):
            Required. The new exclusion, whose ``name`` parameter is an
            exclusion name that is not already used in the parent
            resource.
    """
    __module__ = __module__.rsplit('.', maxsplit=1)[0]  # type: ignore

    parent = proto.Field(
        proto.STRING,
        number=1,
    )
    exclusion = proto.Field(
        proto.MESSAGE,
        number=2,
        message='LogExclusion',
    )


class UpdateExclusionRequest(proto.Message):
    r"""The parameters to ``UpdateExclusion``.

    Attributes:
        name (str):
            Required. The resource name of the exclusion to update:

            ::

                "projects/[PROJECT_ID]/exclusions/[EXCLUSION_ID]"
                "organizations/[ORGANIZATION_ID]/exclusions/[EXCLUSION_ID]"
                "billingAccounts/[BILLING_ACCOUNT_ID]/exclusions/[EXCLUSION_ID]"
                "folders/[FOLDER_ID]/exclusions/[EXCLUSION_ID]"

            Example:
            ``"projects/my-project-id/exclusions/my-exclusion-id"``.
        exclusion (google.cloud.logging_v2.types.LogExclusion):
            Required. New values for the existing exclusion. Only the
            fields specified in ``update_mask`` are relevant.
        update_mask (google.protobuf.field_mask_pb2.FieldMask):
            Required. A non-empty list of fields to change in the
            existing exclusion. New values for the fields are taken from
            the corresponding fields in the
            [LogExclusion][google.logging.v2.LogExclusion] included in
            this request. Fields not mentioned in ``update_mask`` are
            not changed and are ignored in the request.

            For example, to change the filter and description of an
            exclusion, specify an ``update_mask`` of
            ``"filter,description"``.
    """
    __module__ = __module__.rsplit('.', maxsplit=1)[0]  # type: ignore

    name = proto.Field(
        proto.STRING,
        number=1,
    )
    exclusion = proto.Field(
        proto.MESSAGE,
        number=2,
        message='LogExclusion',
    )
    update_mask = proto.Field(
        proto.MESSAGE,
        number=3,
        message=field_mask_pb2.FieldMask,
    )


class DeleteExclusionRequest(proto.Message):
    r"""The parameters to ``DeleteExclusion``.

    Attributes:
        name (str):
            Required. The resource name of an existing exclusion to
            delete:

            ::

                "projects/[PROJECT_ID]/exclusions/[EXCLUSION_ID]"
                "organizations/[ORGANIZATION_ID]/exclusions/[EXCLUSION_ID]"
                "billingAccounts/[BILLING_ACCOUNT_ID]/exclusions/[EXCLUSION_ID]"
                "folders/[FOLDER_ID]/exclusions/[EXCLUSION_ID]"

            Example:
            ``"projects/my-project-id/exclusions/my-exclusion-id"``.
    """
    __module__ = __module__.rsplit('.', maxsplit=1)[0]  # type: ignore

    name = proto.Field(
        proto.STRING,
        number=1,
    )


class GetCmekSettingsRequest(proto.Message):
    r"""The parameters to
    [GetCmekSettings][google.logging.v2.ConfigServiceV2.GetCmekSettings].

    See `Enabling CMEK for Logs
    Router <https://cloud.google.com/logging/docs/routing/managed-encryption>`__
    for more information.

    Attributes:
        name (str):
            Required. The resource for which to retrieve CMEK settings.

            ::

                "projects/[PROJECT_ID]/cmekSettings"
                "organizations/[ORGANIZATION_ID]/cmekSettings"
                "billingAccounts/[BILLING_ACCOUNT_ID]/cmekSettings"
                "folders/[FOLDER_ID]/cmekSettings"

            Example: ``"organizations/12345/cmekSettings"``.

            Note: CMEK for the Logs Router can currently only be
            configured for GCP organizations. Once configured, it
            applies to all projects and folders in the GCP organization.
    """
    __module__ = __module__.rsplit('.', maxsplit=1)[0]  # type: ignore

    name = proto.Field(
        proto.STRING,
        number=1,
    )


class UpdateCmekSettingsRequest(proto.Message):
    r"""The parameters to
    [UpdateCmekSettings][google.logging.v2.ConfigServiceV2.UpdateCmekSettings].

    See `Enabling CMEK for Logs
    Router <https://cloud.google.com/logging/docs/routing/managed-encryption>`__
    for more information.

    Attributes:
        name (str):
            Required. The resource name for the CMEK settings to update.

            ::

                "projects/[PROJECT_ID]/cmekSettings"
                "organizations/[ORGANIZATION_ID]/cmekSettings"
                "billingAccounts/[BILLING_ACCOUNT_ID]/cmekSettings"
                "folders/[FOLDER_ID]/cmekSettings"

            Example: ``"organizations/12345/cmekSettings"``.

            Note: CMEK for the Logs Router can currently only be
            configured for GCP organizations. Once configured, it
            applies to all projects and folders in the GCP organization.
        cmek_settings (google.cloud.logging_v2.types.CmekSettings):
            Required. The CMEK settings to update.

            See `Enabling CMEK for Logs
            Router <https://cloud.google.com/logging/docs/routing/managed-encryption>`__
            for more information.
        update_mask (google.protobuf.field_mask_pb2.FieldMask):
            Optional. Field mask identifying which fields from
            ``cmek_settings`` should be updated. A field will be
            overwritten if and only if it is in the update mask. Output
            only fields cannot be updated.

            See [FieldMask][google.protobuf.FieldMask] for more
            information.

            Example: ``"updateMask=kmsKeyName"``
    """
    __module__ = __module__.rsplit('.', maxsplit=1)[0]  # type: ignore

    name = proto.Field(
        proto.STRING,
        number=1,
    )
    cmek_settings = proto.Field(
        proto.MESSAGE,
        number=2,
        message='CmekSettings',
    )
    update_mask = proto.Field(
        proto.MESSAGE,
        number=3,
        message=field_mask_pb2.FieldMask,
    )


__all__ = tuple(sorted(__manifest__))

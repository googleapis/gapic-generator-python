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

__manifest__ = (
        'ListInstancesRequest',
        'GetInstanceRequest',
        'CreateInstanceRequest',
        'UpdateInstanceRequest',
        'UpgradeInstanceRequest',
        'DeleteInstanceRequest',
        'ImportInstanceRequest',
        'ExportInstanceRequest',
        'FailoverInstanceRequest',
)


class ListInstancesRequest(proto.Message):
    r"""Request for
    [ListInstances][google.cloud.redis.v1.CloudRedis.ListInstances].

    Attributes:
        parent (str):
            Required. The resource name of the instance location using
            the form: ``projects/{project_id}/locations/{location_id}``
            where ``location_id`` refers to a GCP region.
        page_size (int):
            The maximum number of items to return.

            If not specified, a default value of 1000 will be used by
            the service. Regardless of the page_size value, the response
            may include a partial list and a caller should only rely on
            response's
            [``next_page_token``][google.cloud.redis.v1.ListInstancesResponse.next_page_token]
            to determine if there are more instances left to be queried.
        page_token (str):
            The ``next_page_token`` value returned from a previous
            [ListInstances][google.cloud.redis.v1.CloudRedis.ListInstances]
            request, if any.
    """
    __module__ = __module__.rsplit('.', maxsplit=1)[0]  # type: ignore

    parent = proto.Field(
        proto.STRING,
        number=1,
    )
    page_size = proto.Field(
        proto.INT32,
        number=2,
    )
    page_token = proto.Field(
        proto.STRING,
        number=3,
    )


class GetInstanceRequest(proto.Message):
    r"""Request for
    [GetInstance][google.cloud.redis.v1.CloudRedis.GetInstance].

    Attributes:
        name (str):
            Required. Redis instance resource name using the form:
            ``projects/{project_id}/locations/{location_id}/instances/{instance_id}``
            where ``location_id`` refers to a GCP region.
    """
    __module__ = __module__.rsplit('.', maxsplit=1)[0]  # type: ignore

    name = proto.Field(
        proto.STRING,
        number=1,
    )


class CreateInstanceRequest(proto.Message):
    r"""Request for
    [CreateInstance][google.cloud.redis.v1.CloudRedis.CreateInstance].

    Attributes:
        parent (str):
            Required. The resource name of the instance location using
            the form: ``projects/{project_id}/locations/{location_id}``
            where ``location_id`` refers to a GCP region.
        instance_id (str):
            Required. The logical name of the Redis instance in the
            customer project with the following restrictions:

            -  Must contain only lowercase letters, numbers, and
               hyphens.
            -  Must start with a letter.
            -  Must be between 1-40 characters.
            -  Must end with a number or a letter.
            -  Must be unique within the customer project / location
        instance (google.cloud.redis_v1.types.Instance):
            Required. A Redis [Instance] resource
    """
    __module__ = __module__.rsplit('.', maxsplit=1)[0]  # type: ignore

    parent = proto.Field(
        proto.STRING,
        number=1,
    )
    instance_id = proto.Field(
        proto.STRING,
        number=2,
    )
    instance = proto.Field(
        proto.MESSAGE,
        number=3,
        message='Instance',
    )


class UpdateInstanceRequest(proto.Message):
    r"""Request for
    [UpdateInstance][google.cloud.redis.v1.CloudRedis.UpdateInstance].

    Attributes:
        update_mask (google.protobuf.field_mask_pb2.FieldMask):
            Required. Mask of fields to update. At least one path must
            be supplied in this field. The elements of the repeated
            paths field may only include these fields from
            [Instance][google.cloud.redis.v1.Instance]:

            -  ``displayName``
            -  ``labels``
            -  ``memorySizeGb``
            -  ``redisConfig``
        instance (google.cloud.redis_v1.types.Instance):
            Required. Update description. Only fields specified in
            update_mask are updated.
    """
    __module__ = __module__.rsplit('.', maxsplit=1)[0]  # type: ignore

    update_mask = proto.Field(
        proto.MESSAGE,
        number=1,
        message=field_mask_pb2.FieldMask,
    )
    instance = proto.Field(
        proto.MESSAGE,
        number=2,
        message='Instance',
    )


class UpgradeInstanceRequest(proto.Message):
    r"""Request for
    [UpgradeInstance][google.cloud.redis.v1.CloudRedis.UpgradeInstance].

    Attributes:
        name (str):
            Required. Redis instance resource name using the form:
            ``projects/{project_id}/locations/{location_id}/instances/{instance_id}``
            where ``location_id`` refers to a GCP region.
        redis_version (str):
            Required. Specifies the target version of
            Redis software to upgrade to.
    """
    __module__ = __module__.rsplit('.', maxsplit=1)[0]  # type: ignore

    name = proto.Field(
        proto.STRING,
        number=1,
    )
    redis_version = proto.Field(
        proto.STRING,
        number=2,
    )


class DeleteInstanceRequest(proto.Message):
    r"""Request for
    [DeleteInstance][google.cloud.redis.v1.CloudRedis.DeleteInstance].

    Attributes:
        name (str):
            Required. Redis instance resource name using the form:
            ``projects/{project_id}/locations/{location_id}/instances/{instance_id}``
            where ``location_id`` refers to a GCP region.
    """
    __module__ = __module__.rsplit('.', maxsplit=1)[0]  # type: ignore

    name = proto.Field(
        proto.STRING,
        number=1,
    )


class ImportInstanceRequest(proto.Message):
    r"""Request for
    [Import][google.cloud.redis.v1.CloudRedis.ImportInstance].

    Attributes:
        name (str):
            Required. Redis instance resource name using the form:
            ``projects/{project_id}/locations/{location_id}/instances/{instance_id}``
            where ``location_id`` refers to a GCP region.
        input_config (google.cloud.redis_v1.types.InputConfig):
            Required. Specify data to be imported.
    """
    __module__ = __module__.rsplit('.', maxsplit=1)[0]  # type: ignore

    name = proto.Field(
        proto.STRING,
        number=1,
    )
    input_config = proto.Field(
        proto.MESSAGE,
        number=3,
        message='InputConfig',
    )


class ExportInstanceRequest(proto.Message):
    r"""Request for
    [Export][google.cloud.redis.v1.CloudRedis.ExportInstance].

    Attributes:
        name (str):
            Required. Redis instance resource name using the form:
            ``projects/{project_id}/locations/{location_id}/instances/{instance_id}``
            where ``location_id`` refers to a GCP region.
        output_config (google.cloud.redis_v1.types.OutputConfig):
            Required. Specify data to be exported.
    """
    __module__ = __module__.rsplit('.', maxsplit=1)[0]  # type: ignore

    name = proto.Field(
        proto.STRING,
        number=1,
    )
    output_config = proto.Field(
        proto.MESSAGE,
        number=3,
        message='OutputConfig',
    )


class FailoverInstanceRequest(proto.Message):
    r"""Request for
    [Failover][google.cloud.redis.v1.CloudRedis.FailoverInstance].

    Attributes:
        name (str):
            Required. Redis instance resource name using the form:
            ``projects/{project_id}/locations/{location_id}/instances/{instance_id}``
            where ``location_id`` refers to a GCP region.
        data_protection_mode (google.cloud.redis_v1.types.FailoverInstanceRequest.DataProtectionMode):
            Optional. Available data protection modes that the user can
            choose. If it's unspecified, data protection mode will be
            LIMITED_DATA_LOSS by default.
    """
    __module__ = __module__.rsplit('.', maxsplit=1)[0]  # type: ignore
    class DataProtectionMode(proto.Enum):
        r"""Specifies different modes of operation in relation to the
        data retention.
        """
        __module__ = __module__.rsplit('.', maxsplit=1)[0]  # type: ignore
        DATA_PROTECTION_MODE_UNSPECIFIED = 0
        LIMITED_DATA_LOSS = 1
        FORCE_DATA_LOSS = 2

    name = proto.Field(
        proto.STRING,
        number=1,
    )
    data_protection_mode = proto.Field(
        proto.ENUM,
        number=2,
        enum=DataProtectionMode,
    )


__all__ = tuple(sorted(__manifest__))

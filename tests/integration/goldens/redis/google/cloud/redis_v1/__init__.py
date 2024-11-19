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
from google.cloud.redis_v1 import gapic_version as package_version

__version__ = package_version.__version__


from .services.cloud_redis import CloudRedisClient
from .services.cloud_redis import CloudRedisAsyncClient

from .types import cloud_redis_pb2
from .types.cloud_redis_pb2 import CreateInstanceRequest
from .types.cloud_redis_pb2 import DeleteInstanceRequest
from .types.cloud_redis_pb2 import ExportInstanceRequest
from .types.cloud_redis_pb2 import FailoverInstanceRequest
from .types.cloud_redis_pb2 import GcsDestination
from .types.cloud_redis_pb2 import GcsSource
from .types.cloud_redis_pb2 import GetInstanceAuthStringRequest
from .types.cloud_redis_pb2 import GetInstanceRequest
from .types.cloud_redis_pb2 import ImportInstanceRequest
from .types.cloud_redis_pb2 import InputConfig
from .types.cloud_redis_pb2 import Instance
from .types.cloud_redis_pb2 import InstanceAuthString
from .types.cloud_redis_pb2 import ListInstancesRequest
from .types.cloud_redis_pb2 import ListInstancesResponse
from .types.cloud_redis_pb2 import LocationMetadata
from .types.cloud_redis_pb2 import MaintenancePolicy
from .types.cloud_redis_pb2 import MaintenanceSchedule
from .types.cloud_redis_pb2 import NodeInfo
from .types.cloud_redis_pb2 import OperationMetadata
from .types.cloud_redis_pb2 import OutputConfig
from .types.cloud_redis_pb2 import PersistenceConfig
from .types.cloud_redis_pb2 import RescheduleMaintenanceRequest
from .types.cloud_redis_pb2 import TlsCertificate
from .types.cloud_redis_pb2 import UpdateInstanceRequest
from .types.cloud_redis_pb2 import UpgradeInstanceRequest
from .types.cloud_redis_pb2 import WeeklyMaintenanceWindow
from .types.cloud_redis_pb2 import ZoneMetadata

__all__ = (
    'CloudRedisAsyncClient',
'CloudRedisClient',
'CreateInstanceRequest',
'DeleteInstanceRequest',
'ExportInstanceRequest',
'FailoverInstanceRequest',
'GcsDestination',
'GcsSource',
'GetInstanceAuthStringRequest',
'GetInstanceRequest',
'ImportInstanceRequest',
'InputConfig',
'Instance',
'InstanceAuthString',
'ListInstancesRequest',
'ListInstancesResponse',
'LocationMetadata',
'MaintenancePolicy',
'MaintenanceSchedule',
'NodeInfo',
'OperationMetadata',
'OutputConfig',
'PersistenceConfig',
'RescheduleMaintenanceRequest',
'TlsCertificate',
'UpdateInstanceRequest',
'UpgradeInstanceRequest',
'WeeklyMaintenanceWindow',
'ZoneMetadata',
)

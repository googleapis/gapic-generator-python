# -*- coding: utf-8 -*-
# Copyright 2025 Google LLC
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


import google.api_core as api_core

try:
  api_core.check_python_version("google.cloud.redis_v1")
  api_core.check_dependency_versions("google.cloud.redis_v1")
except AttributeError:
  # An older version of api_core is installed, which does not define the
  # functions above. We do equivalent checks manually.

  import logging
  import sys

  _py_version_str = sys.version.split()[0]
  _package_label = "google.cloud.redis_v1"
  if sys.version_info < (3, 9):
    logging.warning("You are using a non-supported Python version " +
            f"({_py_version_str}).  Google will not post any further " +
            f"updates to {_package_label} supporting this Python version. " +
            "Please upgrade to the latest Python version, or at " +
            f"least to Python 3.9, and then update {_package_label}.")
  if sys.version_info[:2] == (3, 9):
    logging.warning(f"You are using a Python version ({_py_version_str}) " +
            f"which Google will stop supporting in {_package_label} when " +
            "it reaches its end of life (October 2025). Please " +
            "upgrade to the latest Python version, or at " +
            "least Python 3.10, before then, and " +
            f"then update {_package_label}.")

  import pkg_resources
  from packaging.version import parse as parse_version

  def _get_version(dependency_name):
    version_string = pkg_resources.get_distribution(dependency_name).version
    return parse_version(version_string)

  try:
    _dependency_package = "google.protobuf"
    _version_used = _get_version(_dependency_package)
    _next_supported_version = "4.25.8"
    if _version_used < parse_version(_next_supported_version):
      logging.warning(f"DEPRECATION: Package {_package_label} depends on " +
              f"{_dependency_package}, currently installed at version " +
              f"{_version_used.__str__}. Future updates to " +
              f"{_package_label} will require {_dependency_package} at " +
              f"version {_next_supported_version} or higher. Please ensure " +
              "that either (a) your Python environment doesn't pin the " +
              f"version of {_dependency_package}, so that updates to " +
              f"{_package_label} can require the higher version, or " +
              "(b) you manually update your Python environment to use at " +
              f"least version {_next_supported_version} of " +
              f"{_dependency_package}.")
  except pkg_resources.DistributionNotFound:
    pass


from .services.cloud_redis import CloudRedisClient
from .services.cloud_redis import CloudRedisAsyncClient

from .types.cloud_redis import CreateInstanceRequest
from .types.cloud_redis import DeleteInstanceRequest
from .types.cloud_redis import ExportInstanceRequest
from .types.cloud_redis import FailoverInstanceRequest
from .types.cloud_redis import GcsDestination
from .types.cloud_redis import GcsSource
from .types.cloud_redis import GetInstanceAuthStringRequest
from .types.cloud_redis import GetInstanceRequest
from .types.cloud_redis import ImportInstanceRequest
from .types.cloud_redis import InputConfig
from .types.cloud_redis import Instance
from .types.cloud_redis import InstanceAuthString
from .types.cloud_redis import ListInstancesRequest
from .types.cloud_redis import ListInstancesResponse
from .types.cloud_redis import LocationMetadata
from .types.cloud_redis import MaintenancePolicy
from .types.cloud_redis import MaintenanceSchedule
from .types.cloud_redis import NodeInfo
from .types.cloud_redis import OperationMetadata
from .types.cloud_redis import OutputConfig
from .types.cloud_redis import PersistenceConfig
from .types.cloud_redis import RescheduleMaintenanceRequest
from .types.cloud_redis import TlsCertificate
from .types.cloud_redis import UpdateInstanceRequest
from .types.cloud_redis import UpgradeInstanceRequest
from .types.cloud_redis import WeeklyMaintenanceWindow
from .types.cloud_redis import ZoneMetadata

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

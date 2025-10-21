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
from google.cloud.eventarc_v1 import gapic_version as package_version

__version__ = package_version.__version__


import google.api_core as api_core

if hasattr(api_core, "check_python_version") and hasattr(api_core, "check_dependency_versions"):   # pragma: NO COVER
    api_core.check_python_version("google.cloud.eventarc_v1") # type: ignore
    api_core.check_dependency_versions("google.cloud.eventarc_v1") # type: ignore
else:   # pragma: NO COVER
    # An older version of api_core is installed which does not define the
    # functions above. We do equivalent checks manually.
    try:
        import warnings
        import sys

        _py_version_str = sys.version.split()[0]
        _package_label = "google.cloud.eventarc_v1"
        if sys.version_info < (3, 9):
            warnings.warn("You are using a non-supported Python version " +
                          f"({_py_version_str}).  Google will not post any further " +
                          f"updates to {_package_label} supporting this Python version. " +
                          "Please upgrade to the latest Python version, or at " +
                          f"least to Python 3.9, and then update {_package_label}.",
                          FutureWarning)
        if sys.version_info[:2] == (3, 9):
            warnings.warn(f"You are using a Python version ({_py_version_str}) " +
                          f"which Google will stop supporting in {_package_label} in " +
                          "January 2026. Please " +
                          "upgrade to the latest Python version, or at " +
                          "least to Python 3.10, before then, and " +
                          f"then update {_package_label}.",
                          FutureWarning)

        from packaging.version import parse as parse_version

        if sys.version_info < (3, 8):
            import pkg_resources

            def _get_version(dependency_name):
              try:
                version_string = pkg_resources.get_distribution(dependency_name).version
                return (parse_version(version_string), version_string)
              except pkg_resources.DistributionNotFound:
                return (None, "--")
        else:
            from importlib import metadata

            def _get_version(dependency_name):
                try:
                    version_string = metadata.version("requests")
                    parsed_version = parse_version(version_string)
                    return (parsed_version.release, version_string)
                except metadata.PackageNotFoundError:
                    return (None, "--")

        _dependency_package = "google.protobuf"
        _next_supported_version = "4.25.8"
        _next_supported_version_tuple = (4, 25, 8)
        _recommendation = " (we recommend 6.x)"
        (_version_used, _version_used_string) = _get_version(_dependency_package)
        if _version_used and _version_used < _next_supported_version_tuple:
            warnings.warn(f"Package {_package_label} depends on " +
                          f"{_dependency_package}, currently installed at version " +
                          f"{_version_used_string}. Future updates to " +
                          f"{_package_label} will require {_dependency_package} at " +
                          f"version {_next_supported_version} or higher{_recommendation}." +
                          " Please ensure " +
                          "that either (a) your Python environment doesn't pin the " +
                          f"version of {_dependency_package}, so that updates to " +
                          f"{_package_label} can require the higher version, or " +
                          "(b) you manually update your Python environment to use at " +
                          f"least version {_next_supported_version} of " +
                          f"{_dependency_package}.",
                          FutureWarning)
    except Exception:
            warnings.warn("Could not determine the version of Python " +
                          "currently being used. To continue receiving " +
                          "updates for {_package_label}, ensure you are " +
                          "using a supported version of Python; see " +
                          "https://devguide.python.org/versions/")


from .services.eventarc import EventarcClient
from .services.eventarc import EventarcAsyncClient

from .types.channel import Channel
from .types.channel_connection import ChannelConnection
from .types.discovery import EventType
from .types.discovery import FilteringAttribute
from .types.discovery import Provider
from .types.eventarc import CreateChannelConnectionRequest
from .types.eventarc import CreateChannelRequest
from .types.eventarc import CreateTriggerRequest
from .types.eventarc import DeleteChannelConnectionRequest
from .types.eventarc import DeleteChannelRequest
from .types.eventarc import DeleteTriggerRequest
from .types.eventarc import GetChannelConnectionRequest
from .types.eventarc import GetChannelRequest
from .types.eventarc import GetGoogleChannelConfigRequest
from .types.eventarc import GetProviderRequest
from .types.eventarc import GetTriggerRequest
from .types.eventarc import ListChannelConnectionsRequest
from .types.eventarc import ListChannelConnectionsResponse
from .types.eventarc import ListChannelsRequest
from .types.eventarc import ListChannelsResponse
from .types.eventarc import ListProvidersRequest
from .types.eventarc import ListProvidersResponse
from .types.eventarc import ListTriggersRequest
from .types.eventarc import ListTriggersResponse
from .types.eventarc import OperationMetadata
from .types.eventarc import UpdateChannelRequest
from .types.eventarc import UpdateGoogleChannelConfigRequest
from .types.eventarc import UpdateTriggerRequest
from .types.google_channel_config import GoogleChannelConfig
from .types.trigger import CloudRun
from .types.trigger import Destination
from .types.trigger import EventFilter
from .types.trigger import GKE
from .types.trigger import Pubsub
from .types.trigger import StateCondition
from .types.trigger import Transport
from .types.trigger import Trigger

__all__ = (
    'EventarcAsyncClient',
'Channel',
'ChannelConnection',
'CloudRun',
'CreateChannelConnectionRequest',
'CreateChannelRequest',
'CreateTriggerRequest',
'DeleteChannelConnectionRequest',
'DeleteChannelRequest',
'DeleteTriggerRequest',
'Destination',
'EventFilter',
'EventType',
'EventarcClient',
'FilteringAttribute',
'GKE',
'GetChannelConnectionRequest',
'GetChannelRequest',
'GetGoogleChannelConfigRequest',
'GetProviderRequest',
'GetTriggerRequest',
'GoogleChannelConfig',
'ListChannelConnectionsRequest',
'ListChannelConnectionsResponse',
'ListChannelsRequest',
'ListChannelsResponse',
'ListProvidersRequest',
'ListProvidersResponse',
'ListTriggersRequest',
'ListTriggersResponse',
'OperationMetadata',
'Provider',
'Pubsub',
'StateCondition',
'Transport',
'Trigger',
'UpdateChannelRequest',
'UpdateGoogleChannelConfigRequest',
'UpdateTriggerRequest',
)

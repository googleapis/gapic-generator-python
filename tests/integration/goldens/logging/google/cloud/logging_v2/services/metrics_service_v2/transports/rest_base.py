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
import json  # type: ignore
from google.api_core import path_template
from google.api_core import gapic_v1  # type: ignore

from google.protobuf import json_format
from .base import MetricsServiceV2Transport, DEFAULT_CLIENT_INFO
from google.auth import credentials as ga_credentials  # type: ignore

import re
from typing import Any, Callable, Dict, List, Optional, Sequence, Tuple, Union



from google.cloud.logging_v2.types import logging_metrics
from google.protobuf import empty_pb2  # type: ignore
from google.longrunning import operations_pb2  # type: ignore


class _BaseMetricsServiceV2RestTransport(MetricsServiceV2Transport):
    """Base REST backend transport for MetricsServiceV2.

    Note: This class is not meant to be used directly.
    """

    def __init__(self, *,
            host: str = 'logging.googleapis.com',
            credentials: Optional[ga_credentials.Credentials] = None,
            client_info: gapic_v1.client_info.ClientInfo = DEFAULT_CLIENT_INFO,
            always_use_jwt_access: Optional[bool] = False,
            url_scheme: str = 'https',
            api_audience: Optional[str] = None,
            ) -> None:
        """Instantiate the transport.
        Args:
            host (Optional[str]):
                 The hostname to connect to (default: 'logging.googleapis.com').
            credentials (Optional[google.auth.credentials.Credentials]): The
                authorization credentials to attach to requests. These
                credentials identify the application to the service; if none
                are specified, the client will attempt to ascertain the
                credentials from the environment.
            client_info (google.api_core.gapic_v1.client_info.ClientInfo):
                The client info used to send a user-agent string along with
                API requests. If ``None``, then default info will be used.
                Generally, you only need to set this if you are developing
                your own client library.
            always_use_jwt_access (Optional[bool]): Whether self signed JWT should
                be used for service account credentials.
            url_scheme: the protocol scheme for the API endpoint.  Normally
                "https", but for testing or local servers,
                "http" can be specified.
        """
        # Run the base constructor
        maybe_url_match = re.match("^(?P<scheme>http(?:s)?://)?(?P<host>.*)$", host)
        if maybe_url_match is None:
            raise ValueError(f"Unexpected hostname structure: {host}")  # pragma: NO COVER

        url_match_items = maybe_url_match.groupdict()

        host = f"{url_scheme}://{host}" if not url_match_items["scheme"] else host

        super().__init__(
            host=host,
            credentials=credentials,
            client_info=client_info,
            always_use_jwt_access=always_use_jwt_access,
            api_audience=api_audience
        )

    class _BaseCreateLogMetric:
        def __hash__(self):
            return hash("CreateLogMetric")

        __REQUIRED_FIELDS_DEFAULT_VALUES: Dict[str, Any] =  {
        }

        @classmethod
        def _get_unset_required_fields(cls, message_dict):
            return {k: v for k, v in cls.__REQUIRED_FIELDS_DEFAULT_VALUES.items() if k not in message_dict}

        @staticmethod
        def _get_http_options():
            http_options: List[Dict[str, str]] = [{
                'method': 'post',
                'uri': '/v2/{parent=projects/*}/metrics',
                'body': 'metric',
            },
            ]
            return http_options

        @staticmethod
        def _get_transcoded_request(http_options, request):
            pb_request = logging_metrics.CreateLogMetricRequest.pb(request)
            transcoded_request = path_template.transcode(http_options, pb_request)
            return transcoded_request

        @staticmethod
        def _get_request_body_json(transcoded_request):
            # Jsonify the request body

            body = json_format.MessageToJson(
                transcoded_request['body'],
                use_integers_for_enums=False
            )
            return body
        @staticmethod
        def _get_query_params_json(transcoded_request):
            query_params = json.loads(json_format.MessageToJson(
                transcoded_request['query_params'],
                use_integers_for_enums=False,
            ))
            query_params.update(_BaseMetricsServiceV2RestTransport._BaseCreateLogMetric._get_unset_required_fields(query_params))

            return query_params

    class _BaseDeleteLogMetric:
        def __hash__(self):
            return hash("DeleteLogMetric")

        __REQUIRED_FIELDS_DEFAULT_VALUES: Dict[str, Any] =  {
        }

        @classmethod
        def _get_unset_required_fields(cls, message_dict):
            return {k: v for k, v in cls.__REQUIRED_FIELDS_DEFAULT_VALUES.items() if k not in message_dict}

        @staticmethod
        def _get_http_options():
            http_options: List[Dict[str, str]] = [{
                'method': 'delete',
                'uri': '/v2/{metric_name=projects/*/metrics/*}',
            },
            ]
            return http_options

        @staticmethod
        def _get_transcoded_request(http_options, request):
            pb_request = logging_metrics.DeleteLogMetricRequest.pb(request)
            transcoded_request = path_template.transcode(http_options, pb_request)
            return transcoded_request

        @staticmethod
        def _get_query_params_json(transcoded_request):
            query_params = json.loads(json_format.MessageToJson(
                transcoded_request['query_params'],
                use_integers_for_enums=False,
            ))
            query_params.update(_BaseMetricsServiceV2RestTransport._BaseDeleteLogMetric._get_unset_required_fields(query_params))

            return query_params

    class _BaseGetLogMetric:
        def __hash__(self):
            return hash("GetLogMetric")

        __REQUIRED_FIELDS_DEFAULT_VALUES: Dict[str, Any] =  {
        }

        @classmethod
        def _get_unset_required_fields(cls, message_dict):
            return {k: v for k, v in cls.__REQUIRED_FIELDS_DEFAULT_VALUES.items() if k not in message_dict}

        @staticmethod
        def _get_http_options():
            http_options: List[Dict[str, str]] = [{
                'method': 'get',
                'uri': '/v2/{metric_name=projects/*/metrics/*}',
            },
            ]
            return http_options

        @staticmethod
        def _get_transcoded_request(http_options, request):
            pb_request = logging_metrics.GetLogMetricRequest.pb(request)
            transcoded_request = path_template.transcode(http_options, pb_request)
            return transcoded_request

        @staticmethod
        def _get_query_params_json(transcoded_request):
            query_params = json.loads(json_format.MessageToJson(
                transcoded_request['query_params'],
                use_integers_for_enums=False,
            ))
            query_params.update(_BaseMetricsServiceV2RestTransport._BaseGetLogMetric._get_unset_required_fields(query_params))

            return query_params

    class _BaseListLogMetrics:
        def __hash__(self):
            return hash("ListLogMetrics")

        __REQUIRED_FIELDS_DEFAULT_VALUES: Dict[str, Any] =  {
        }

        @classmethod
        def _get_unset_required_fields(cls, message_dict):
            return {k: v for k, v in cls.__REQUIRED_FIELDS_DEFAULT_VALUES.items() if k not in message_dict}

        @staticmethod
        def _get_http_options():
            http_options: List[Dict[str, str]] = [{
                'method': 'get',
                'uri': '/v2/{parent=projects/*}/metrics',
            },
            ]
            return http_options

        @staticmethod
        def _get_transcoded_request(http_options, request):
            pb_request = logging_metrics.ListLogMetricsRequest.pb(request)
            transcoded_request = path_template.transcode(http_options, pb_request)
            return transcoded_request

        @staticmethod
        def _get_query_params_json(transcoded_request):
            query_params = json.loads(json_format.MessageToJson(
                transcoded_request['query_params'],
                use_integers_for_enums=False,
            ))
            query_params.update(_BaseMetricsServiceV2RestTransport._BaseListLogMetrics._get_unset_required_fields(query_params))

            return query_params

    class _BaseUpdateLogMetric:
        def __hash__(self):
            return hash("UpdateLogMetric")

        __REQUIRED_FIELDS_DEFAULT_VALUES: Dict[str, Any] =  {
        }

        @classmethod
        def _get_unset_required_fields(cls, message_dict):
            return {k: v for k, v in cls.__REQUIRED_FIELDS_DEFAULT_VALUES.items() if k not in message_dict}

        @staticmethod
        def _get_http_options():
            http_options: List[Dict[str, str]] = [{
                'method': 'put',
                'uri': '/v2/{metric_name=projects/*/metrics/*}',
                'body': 'metric',
            },
            ]
            return http_options

        @staticmethod
        def _get_transcoded_request(http_options, request):
            pb_request = logging_metrics.UpdateLogMetricRequest.pb(request)
            transcoded_request = path_template.transcode(http_options, pb_request)
            return transcoded_request

        @staticmethod
        def _get_request_body_json(transcoded_request):
            # Jsonify the request body

            body = json_format.MessageToJson(
                transcoded_request['body'],
                use_integers_for_enums=False
            )
            return body
        @staticmethod
        def _get_query_params_json(transcoded_request):
            query_params = json.loads(json_format.MessageToJson(
                transcoded_request['query_params'],
                use_integers_for_enums=False,
            ))
            query_params.update(_BaseMetricsServiceV2RestTransport._BaseUpdateLogMetric._get_unset_required_fields(query_params))

            return query_params


__all__=(
    '_BaseMetricsServiceV2RestTransport',
)

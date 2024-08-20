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
from .base import ConfigServiceV2Transport, DEFAULT_CLIENT_INFO
from google.auth import credentials as ga_credentials  # type: ignore

import re
from typing import Any, Callable, Dict, List, Optional, Sequence, Tuple, Union



from google.cloud.logging_v2.types import logging_config
from google.protobuf import empty_pb2  # type: ignore
from google.longrunning import operations_pb2  # type: ignore


class _BaseConfigServiceV2RestTransport(ConfigServiceV2Transport):
    """Base REST backend transport for ConfigServiceV2.

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

    class _BaseCopyLogEntries:
        def __hash__(self):
            return hash("CopyLogEntries")

        __REQUIRED_FIELDS_DEFAULT_VALUES: Dict[str, Any] =  {
        }

        @classmethod
        def _get_unset_required_fields(cls, message_dict):
            return {k: v for k, v in cls.__REQUIRED_FIELDS_DEFAULT_VALUES.items() if k not in message_dict}

        @staticmethod
        def _get_http_options():
            http_options: List[Dict[str, str]] = [{
                'method': 'post',
                'uri': '/v2/entries:copy',
                'body': '*',
            },
            ]
            return http_options

        @staticmethod
        def _get_transcoded_request(http_options, request):
            pb_request = logging_config.CopyLogEntriesRequest.pb(request)
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
            query_params.update(_BaseConfigServiceV2RestTransport._BaseCopyLogEntries._get_unset_required_fields(query_params))

            return query_params

    class _BaseCreateBucket:
        def __hash__(self):
            return hash("CreateBucket")

        __REQUIRED_FIELDS_DEFAULT_VALUES: Dict[str, Any] =  {
            "bucketId" : "",        }

        @classmethod
        def _get_unset_required_fields(cls, message_dict):
            return {k: v for k, v in cls.__REQUIRED_FIELDS_DEFAULT_VALUES.items() if k not in message_dict}

        @staticmethod
        def _get_http_options():
            http_options: List[Dict[str, str]] = [{
                'method': 'post',
                'uri': '/v2/{parent=*/*/locations/*}/buckets',
                'body': 'bucket',
            },
        {
                'method': 'post',
                'uri': '/v2/{parent=projects/*/locations/*}/buckets',
                'body': 'bucket',
            },
        {
                'method': 'post',
                'uri': '/v2/{parent=organizations/*/locations/*}/buckets',
                'body': 'bucket',
            },
        {
                'method': 'post',
                'uri': '/v2/{parent=folders/*/locations/*}/buckets',
                'body': 'bucket',
            },
        {
                'method': 'post',
                'uri': '/v2/{parent=billingAccounts/*/locations/*}/buckets',
                'body': 'bucket',
            },
            ]
            return http_options

        @staticmethod
        def _get_transcoded_request(http_options, request):
            pb_request = logging_config.CreateBucketRequest.pb(request)
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
            query_params.update(_BaseConfigServiceV2RestTransport._BaseCreateBucket._get_unset_required_fields(query_params))

            return query_params

    class _BaseCreateBucketAsync:
        def __hash__(self):
            return hash("CreateBucketAsync")

        __REQUIRED_FIELDS_DEFAULT_VALUES: Dict[str, Any] =  {
            "bucketId" : "",        }

        @classmethod
        def _get_unset_required_fields(cls, message_dict):
            return {k: v for k, v in cls.__REQUIRED_FIELDS_DEFAULT_VALUES.items() if k not in message_dict}

        @staticmethod
        def _get_http_options():
            http_options: List[Dict[str, str]] = [{
                'method': 'post',
                'uri': '/v2/{parent=*/*/locations/*}/buckets:createAsync',
                'body': 'bucket',
            },
        {
                'method': 'post',
                'uri': '/v2/{parent=projects/*/locations/*}/buckets:createAsync',
                'body': 'bucket',
            },
        {
                'method': 'post',
                'uri': '/v2/{parent=organizations/*/locations/*}/buckets:createAsync',
                'body': 'bucket',
            },
        {
                'method': 'post',
                'uri': '/v2/{parent=folders/*/locations/*}/buckets:createAsync',
                'body': 'bucket',
            },
        {
                'method': 'post',
                'uri': '/v2/{parent=billingAccounts/*/locations/*}/buckets:createAsync',
                'body': 'bucket',
            },
            ]
            return http_options

        @staticmethod
        def _get_transcoded_request(http_options, request):
            pb_request = logging_config.CreateBucketRequest.pb(request)
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
            query_params.update(_BaseConfigServiceV2RestTransport._BaseCreateBucketAsync._get_unset_required_fields(query_params))

            return query_params

    class _BaseCreateExclusion:
        def __hash__(self):
            return hash("CreateExclusion")

        __REQUIRED_FIELDS_DEFAULT_VALUES: Dict[str, Any] =  {
        }

        @classmethod
        def _get_unset_required_fields(cls, message_dict):
            return {k: v for k, v in cls.__REQUIRED_FIELDS_DEFAULT_VALUES.items() if k not in message_dict}

        @staticmethod
        def _get_http_options():
            http_options: List[Dict[str, str]] = [{
                'method': 'post',
                'uri': '/v2/{parent=*/*}/exclusions',
                'body': 'exclusion',
            },
        {
                'method': 'post',
                'uri': '/v2/{parent=projects/*}/exclusions',
                'body': 'exclusion',
            },
        {
                'method': 'post',
                'uri': '/v2/{parent=organizations/*}/exclusions',
                'body': 'exclusion',
            },
        {
                'method': 'post',
                'uri': '/v2/{parent=folders/*}/exclusions',
                'body': 'exclusion',
            },
        {
                'method': 'post',
                'uri': '/v2/{parent=billingAccounts/*}/exclusions',
                'body': 'exclusion',
            },
            ]
            return http_options

        @staticmethod
        def _get_transcoded_request(http_options, request):
            pb_request = logging_config.CreateExclusionRequest.pb(request)
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
            query_params.update(_BaseConfigServiceV2RestTransport._BaseCreateExclusion._get_unset_required_fields(query_params))

            return query_params

    class _BaseCreateLink:
        def __hash__(self):
            return hash("CreateLink")

        __REQUIRED_FIELDS_DEFAULT_VALUES: Dict[str, Any] =  {
            "linkId" : "",        }

        @classmethod
        def _get_unset_required_fields(cls, message_dict):
            return {k: v for k, v in cls.__REQUIRED_FIELDS_DEFAULT_VALUES.items() if k not in message_dict}

        @staticmethod
        def _get_http_options():
            http_options: List[Dict[str, str]] = [{
                'method': 'post',
                'uri': '/v2/{parent=*/*/locations/*/buckets/*}/links',
                'body': 'link',
            },
        {
                'method': 'post',
                'uri': '/v2/{parent=projects/*/locations/*/buckets/*}/links',
                'body': 'link',
            },
        {
                'method': 'post',
                'uri': '/v2/{parent=organizations/*/locations/*/buckets/*}/links',
                'body': 'link',
            },
        {
                'method': 'post',
                'uri': '/v2/{parent=folders/*/locations/*/buckets/*}/links',
                'body': 'link',
            },
        {
                'method': 'post',
                'uri': '/v2/{parent=billingAccounts/*/locations/*/buckets/*}/links',
                'body': 'link',
            },
            ]
            return http_options

        @staticmethod
        def _get_transcoded_request(http_options, request):
            pb_request = logging_config.CreateLinkRequest.pb(request)
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
            query_params.update(_BaseConfigServiceV2RestTransport._BaseCreateLink._get_unset_required_fields(query_params))

            return query_params

    class _BaseCreateSink:
        def __hash__(self):
            return hash("CreateSink")

        __REQUIRED_FIELDS_DEFAULT_VALUES: Dict[str, Any] =  {
        }

        @classmethod
        def _get_unset_required_fields(cls, message_dict):
            return {k: v for k, v in cls.__REQUIRED_FIELDS_DEFAULT_VALUES.items() if k not in message_dict}

        @staticmethod
        def _get_http_options():
            http_options: List[Dict[str, str]] = [{
                'method': 'post',
                'uri': '/v2/{parent=*/*}/sinks',
                'body': 'sink',
            },
        {
                'method': 'post',
                'uri': '/v2/{parent=projects/*}/sinks',
                'body': 'sink',
            },
        {
                'method': 'post',
                'uri': '/v2/{parent=organizations/*}/sinks',
                'body': 'sink',
            },
        {
                'method': 'post',
                'uri': '/v2/{parent=folders/*}/sinks',
                'body': 'sink',
            },
        {
                'method': 'post',
                'uri': '/v2/{parent=billingAccounts/*}/sinks',
                'body': 'sink',
            },
            ]
            return http_options

        @staticmethod
        def _get_transcoded_request(http_options, request):
            pb_request = logging_config.CreateSinkRequest.pb(request)
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
            query_params.update(_BaseConfigServiceV2RestTransport._BaseCreateSink._get_unset_required_fields(query_params))

            return query_params

    class _BaseCreateView:
        def __hash__(self):
            return hash("CreateView")

        __REQUIRED_FIELDS_DEFAULT_VALUES: Dict[str, Any] =  {
            "viewId" : "",        }

        @classmethod
        def _get_unset_required_fields(cls, message_dict):
            return {k: v for k, v in cls.__REQUIRED_FIELDS_DEFAULT_VALUES.items() if k not in message_dict}

        @staticmethod
        def _get_http_options():
            http_options: List[Dict[str, str]] = [{
                'method': 'post',
                'uri': '/v2/{parent=*/*/locations/*/buckets/*}/views',
                'body': 'view',
            },
        {
                'method': 'post',
                'uri': '/v2/{parent=projects/*/locations/*/buckets/*}/views',
                'body': 'view',
            },
        {
                'method': 'post',
                'uri': '/v2/{parent=organizations/*/locations/*/buckets/*}/views',
                'body': 'view',
            },
        {
                'method': 'post',
                'uri': '/v2/{parent=folders/*/locations/*/buckets/*}/views',
                'body': 'view',
            },
        {
                'method': 'post',
                'uri': '/v2/{parent=billingAccounts/*/locations/*/buckets/*}/views',
                'body': 'view',
            },
            ]
            return http_options

        @staticmethod
        def _get_transcoded_request(http_options, request):
            pb_request = logging_config.CreateViewRequest.pb(request)
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
            query_params.update(_BaseConfigServiceV2RestTransport._BaseCreateView._get_unset_required_fields(query_params))

            return query_params

    class _BaseDeleteBucket:
        def __hash__(self):
            return hash("DeleteBucket")

        __REQUIRED_FIELDS_DEFAULT_VALUES: Dict[str, Any] =  {
        }

        @classmethod
        def _get_unset_required_fields(cls, message_dict):
            return {k: v for k, v in cls.__REQUIRED_FIELDS_DEFAULT_VALUES.items() if k not in message_dict}

        @staticmethod
        def _get_http_options():
            http_options: List[Dict[str, str]] = [{
                'method': 'delete',
                'uri': '/v2/{name=*/*/locations/*/buckets/*}',
            },
        {
                'method': 'delete',
                'uri': '/v2/{name=projects/*/locations/*/buckets/*}',
            },
        {
                'method': 'delete',
                'uri': '/v2/{name=organizations/*/locations/*/buckets/*}',
            },
        {
                'method': 'delete',
                'uri': '/v2/{name=folders/*/locations/*/buckets/*}',
            },
        {
                'method': 'delete',
                'uri': '/v2/{name=billingAccounts/*/locations/*/buckets/*}',
            },
            ]
            return http_options

        @staticmethod
        def _get_transcoded_request(http_options, request):
            pb_request = logging_config.DeleteBucketRequest.pb(request)
            transcoded_request = path_template.transcode(http_options, pb_request)
            return transcoded_request

        @staticmethod
        def _get_query_params_json(transcoded_request):
            query_params = json.loads(json_format.MessageToJson(
                transcoded_request['query_params'],
                use_integers_for_enums=False,
            ))
            query_params.update(_BaseConfigServiceV2RestTransport._BaseDeleteBucket._get_unset_required_fields(query_params))

            return query_params

    class _BaseDeleteExclusion:
        def __hash__(self):
            return hash("DeleteExclusion")

        __REQUIRED_FIELDS_DEFAULT_VALUES: Dict[str, Any] =  {
        }

        @classmethod
        def _get_unset_required_fields(cls, message_dict):
            return {k: v for k, v in cls.__REQUIRED_FIELDS_DEFAULT_VALUES.items() if k not in message_dict}

        @staticmethod
        def _get_http_options():
            http_options: List[Dict[str, str]] = [{
                'method': 'delete',
                'uri': '/v2/{name=*/*/exclusions/*}',
            },
        {
                'method': 'delete',
                'uri': '/v2/{name=projects/*/exclusions/*}',
            },
        {
                'method': 'delete',
                'uri': '/v2/{name=organizations/*/exclusions/*}',
            },
        {
                'method': 'delete',
                'uri': '/v2/{name=folders/*/exclusions/*}',
            },
        {
                'method': 'delete',
                'uri': '/v2/{name=billingAccounts/*/exclusions/*}',
            },
            ]
            return http_options

        @staticmethod
        def _get_transcoded_request(http_options, request):
            pb_request = logging_config.DeleteExclusionRequest.pb(request)
            transcoded_request = path_template.transcode(http_options, pb_request)
            return transcoded_request

        @staticmethod
        def _get_query_params_json(transcoded_request):
            query_params = json.loads(json_format.MessageToJson(
                transcoded_request['query_params'],
                use_integers_for_enums=False,
            ))
            query_params.update(_BaseConfigServiceV2RestTransport._BaseDeleteExclusion._get_unset_required_fields(query_params))

            return query_params

    class _BaseDeleteLink:
        def __hash__(self):
            return hash("DeleteLink")

        __REQUIRED_FIELDS_DEFAULT_VALUES: Dict[str, Any] =  {
        }

        @classmethod
        def _get_unset_required_fields(cls, message_dict):
            return {k: v for k, v in cls.__REQUIRED_FIELDS_DEFAULT_VALUES.items() if k not in message_dict}

        @staticmethod
        def _get_http_options():
            http_options: List[Dict[str, str]] = [{
                'method': 'delete',
                'uri': '/v2/{name=*/*/locations/*/buckets/*/links/*}',
            },
        {
                'method': 'delete',
                'uri': '/v2/{name=projects/*/locations/*/buckets/*/links/*}',
            },
        {
                'method': 'delete',
                'uri': '/v2/{name=organizations/*/locations/*/buckets/*/links/*}',
            },
        {
                'method': 'delete',
                'uri': '/v2/{name=folders/*/locations/*/buckets/*/links/*}',
            },
        {
                'method': 'delete',
                'uri': '/v2/{name=billingAccounts/*/locations/*/buckets/*/links/*}',
            },
            ]
            return http_options

        @staticmethod
        def _get_transcoded_request(http_options, request):
            pb_request = logging_config.DeleteLinkRequest.pb(request)
            transcoded_request = path_template.transcode(http_options, pb_request)
            return transcoded_request

        @staticmethod
        def _get_query_params_json(transcoded_request):
            query_params = json.loads(json_format.MessageToJson(
                transcoded_request['query_params'],
                use_integers_for_enums=False,
            ))
            query_params.update(_BaseConfigServiceV2RestTransport._BaseDeleteLink._get_unset_required_fields(query_params))

            return query_params

    class _BaseDeleteSink:
        def __hash__(self):
            return hash("DeleteSink")

        __REQUIRED_FIELDS_DEFAULT_VALUES: Dict[str, Any] =  {
        }

        @classmethod
        def _get_unset_required_fields(cls, message_dict):
            return {k: v for k, v in cls.__REQUIRED_FIELDS_DEFAULT_VALUES.items() if k not in message_dict}

        @staticmethod
        def _get_http_options():
            http_options: List[Dict[str, str]] = [{
                'method': 'delete',
                'uri': '/v2/{sink_name=*/*/sinks/*}',
            },
        {
                'method': 'delete',
                'uri': '/v2/{sink_name=projects/*/sinks/*}',
            },
        {
                'method': 'delete',
                'uri': '/v2/{sink_name=organizations/*/sinks/*}',
            },
        {
                'method': 'delete',
                'uri': '/v2/{sink_name=folders/*/sinks/*}',
            },
        {
                'method': 'delete',
                'uri': '/v2/{sink_name=billingAccounts/*/sinks/*}',
            },
            ]
            return http_options

        @staticmethod
        def _get_transcoded_request(http_options, request):
            pb_request = logging_config.DeleteSinkRequest.pb(request)
            transcoded_request = path_template.transcode(http_options, pb_request)
            return transcoded_request

        @staticmethod
        def _get_query_params_json(transcoded_request):
            query_params = json.loads(json_format.MessageToJson(
                transcoded_request['query_params'],
                use_integers_for_enums=False,
            ))
            query_params.update(_BaseConfigServiceV2RestTransport._BaseDeleteSink._get_unset_required_fields(query_params))

            return query_params

    class _BaseDeleteView:
        def __hash__(self):
            return hash("DeleteView")

        __REQUIRED_FIELDS_DEFAULT_VALUES: Dict[str, Any] =  {
        }

        @classmethod
        def _get_unset_required_fields(cls, message_dict):
            return {k: v for k, v in cls.__REQUIRED_FIELDS_DEFAULT_VALUES.items() if k not in message_dict}

        @staticmethod
        def _get_http_options():
            http_options: List[Dict[str, str]] = [{
                'method': 'delete',
                'uri': '/v2/{name=*/*/locations/*/buckets/*/views/*}',
            },
        {
                'method': 'delete',
                'uri': '/v2/{name=projects/*/locations/*/buckets/*/views/*}',
            },
        {
                'method': 'delete',
                'uri': '/v2/{name=organizations/*/locations/*/buckets/*/views/*}',
            },
        {
                'method': 'delete',
                'uri': '/v2/{name=folders/*/locations/*/buckets/*/views/*}',
            },
        {
                'method': 'delete',
                'uri': '/v2/{name=billingAccounts/*/locations/*/buckets/*/views/*}',
            },
            ]
            return http_options

        @staticmethod
        def _get_transcoded_request(http_options, request):
            pb_request = logging_config.DeleteViewRequest.pb(request)
            transcoded_request = path_template.transcode(http_options, pb_request)
            return transcoded_request

        @staticmethod
        def _get_query_params_json(transcoded_request):
            query_params = json.loads(json_format.MessageToJson(
                transcoded_request['query_params'],
                use_integers_for_enums=False,
            ))
            query_params.update(_BaseConfigServiceV2RestTransport._BaseDeleteView._get_unset_required_fields(query_params))

            return query_params

    class _BaseGetBucket:
        def __hash__(self):
            return hash("GetBucket")

        __REQUIRED_FIELDS_DEFAULT_VALUES: Dict[str, Any] =  {
        }

        @classmethod
        def _get_unset_required_fields(cls, message_dict):
            return {k: v for k, v in cls.__REQUIRED_FIELDS_DEFAULT_VALUES.items() if k not in message_dict}

        @staticmethod
        def _get_http_options():
            http_options: List[Dict[str, str]] = [{
                'method': 'get',
                'uri': '/v2/{name=*/*/locations/*/buckets/*}',
            },
        {
                'method': 'get',
                'uri': '/v2/{name=projects/*/locations/*/buckets/*}',
            },
        {
                'method': 'get',
                'uri': '/v2/{name=organizations/*/locations/*/buckets/*}',
            },
        {
                'method': 'get',
                'uri': '/v2/{name=folders/*/locations/*/buckets/*}',
            },
        {
                'method': 'get',
                'uri': '/v2/{name=billingAccounts/*/locations/*/buckets/*}',
            },
            ]
            return http_options

        @staticmethod
        def _get_transcoded_request(http_options, request):
            pb_request = logging_config.GetBucketRequest.pb(request)
            transcoded_request = path_template.transcode(http_options, pb_request)
            return transcoded_request

        @staticmethod
        def _get_query_params_json(transcoded_request):
            query_params = json.loads(json_format.MessageToJson(
                transcoded_request['query_params'],
                use_integers_for_enums=False,
            ))
            query_params.update(_BaseConfigServiceV2RestTransport._BaseGetBucket._get_unset_required_fields(query_params))

            return query_params

    class _BaseGetCmekSettings:
        def __hash__(self):
            return hash("GetCmekSettings")

        __REQUIRED_FIELDS_DEFAULT_VALUES: Dict[str, Any] =  {
        }

        @classmethod
        def _get_unset_required_fields(cls, message_dict):
            return {k: v for k, v in cls.__REQUIRED_FIELDS_DEFAULT_VALUES.items() if k not in message_dict}

        @staticmethod
        def _get_http_options():
            http_options: List[Dict[str, str]] = [{
                'method': 'get',
                'uri': '/v2/{name=*/*}/cmekSettings',
            },
        {
                'method': 'get',
                'uri': '/v2/{name=projects/*}/cmekSettings',
            },
        {
                'method': 'get',
                'uri': '/v2/{name=organizations/*}/cmekSettings',
            },
        {
                'method': 'get',
                'uri': '/v2/{name=folders/*}/cmekSettings',
            },
        {
                'method': 'get',
                'uri': '/v2/{name=billingAccounts/*}/cmekSettings',
            },
            ]
            return http_options

        @staticmethod
        def _get_transcoded_request(http_options, request):
            pb_request = logging_config.GetCmekSettingsRequest.pb(request)
            transcoded_request = path_template.transcode(http_options, pb_request)
            return transcoded_request

        @staticmethod
        def _get_query_params_json(transcoded_request):
            query_params = json.loads(json_format.MessageToJson(
                transcoded_request['query_params'],
                use_integers_for_enums=False,
            ))
            query_params.update(_BaseConfigServiceV2RestTransport._BaseGetCmekSettings._get_unset_required_fields(query_params))

            return query_params

    class _BaseGetExclusion:
        def __hash__(self):
            return hash("GetExclusion")

        __REQUIRED_FIELDS_DEFAULT_VALUES: Dict[str, Any] =  {
        }

        @classmethod
        def _get_unset_required_fields(cls, message_dict):
            return {k: v for k, v in cls.__REQUIRED_FIELDS_DEFAULT_VALUES.items() if k not in message_dict}

        @staticmethod
        def _get_http_options():
            http_options: List[Dict[str, str]] = [{
                'method': 'get',
                'uri': '/v2/{name=*/*/exclusions/*}',
            },
        {
                'method': 'get',
                'uri': '/v2/{name=projects/*/exclusions/*}',
            },
        {
                'method': 'get',
                'uri': '/v2/{name=organizations/*/exclusions/*}',
            },
        {
                'method': 'get',
                'uri': '/v2/{name=folders/*/exclusions/*}',
            },
        {
                'method': 'get',
                'uri': '/v2/{name=billingAccounts/*/exclusions/*}',
            },
            ]
            return http_options

        @staticmethod
        def _get_transcoded_request(http_options, request):
            pb_request = logging_config.GetExclusionRequest.pb(request)
            transcoded_request = path_template.transcode(http_options, pb_request)
            return transcoded_request

        @staticmethod
        def _get_query_params_json(transcoded_request):
            query_params = json.loads(json_format.MessageToJson(
                transcoded_request['query_params'],
                use_integers_for_enums=False,
            ))
            query_params.update(_BaseConfigServiceV2RestTransport._BaseGetExclusion._get_unset_required_fields(query_params))

            return query_params

    class _BaseGetLink:
        def __hash__(self):
            return hash("GetLink")

        __REQUIRED_FIELDS_DEFAULT_VALUES: Dict[str, Any] =  {
        }

        @classmethod
        def _get_unset_required_fields(cls, message_dict):
            return {k: v for k, v in cls.__REQUIRED_FIELDS_DEFAULT_VALUES.items() if k not in message_dict}

        @staticmethod
        def _get_http_options():
            http_options: List[Dict[str, str]] = [{
                'method': 'get',
                'uri': '/v2/{name=*/*/locations/*/buckets/*/links/*}',
            },
        {
                'method': 'get',
                'uri': '/v2/{name=projects/*/locations/*/buckets/*/links/*}',
            },
        {
                'method': 'get',
                'uri': '/v2/{name=organizations/*/locations/*/buckets/*/links/*}',
            },
        {
                'method': 'get',
                'uri': '/v2/{name=folders/*/locations/*/buckets/*/links/*}',
            },
        {
                'method': 'get',
                'uri': '/v2/{name=billingAccounts/*/locations/*/buckets/*/links/*}',
            },
            ]
            return http_options

        @staticmethod
        def _get_transcoded_request(http_options, request):
            pb_request = logging_config.GetLinkRequest.pb(request)
            transcoded_request = path_template.transcode(http_options, pb_request)
            return transcoded_request

        @staticmethod
        def _get_query_params_json(transcoded_request):
            query_params = json.loads(json_format.MessageToJson(
                transcoded_request['query_params'],
                use_integers_for_enums=False,
            ))
            query_params.update(_BaseConfigServiceV2RestTransport._BaseGetLink._get_unset_required_fields(query_params))

            return query_params

    class _BaseGetSettings:
        def __hash__(self):
            return hash("GetSettings")

        __REQUIRED_FIELDS_DEFAULT_VALUES: Dict[str, Any] =  {
        }

        @classmethod
        def _get_unset_required_fields(cls, message_dict):
            return {k: v for k, v in cls.__REQUIRED_FIELDS_DEFAULT_VALUES.items() if k not in message_dict}

        @staticmethod
        def _get_http_options():
            http_options: List[Dict[str, str]] = [{
                'method': 'get',
                'uri': '/v2/{name=*/*}/settings',
            },
        {
                'method': 'get',
                'uri': '/v2/{name=projects/*}/settings',
            },
        {
                'method': 'get',
                'uri': '/v2/{name=organizations/*}/settings',
            },
        {
                'method': 'get',
                'uri': '/v2/{name=folders/*}/settings',
            },
        {
                'method': 'get',
                'uri': '/v2/{name=billingAccounts/*}/settings',
            },
            ]
            return http_options

        @staticmethod
        def _get_transcoded_request(http_options, request):
            pb_request = logging_config.GetSettingsRequest.pb(request)
            transcoded_request = path_template.transcode(http_options, pb_request)
            return transcoded_request

        @staticmethod
        def _get_query_params_json(transcoded_request):
            query_params = json.loads(json_format.MessageToJson(
                transcoded_request['query_params'],
                use_integers_for_enums=False,
            ))
            query_params.update(_BaseConfigServiceV2RestTransport._BaseGetSettings._get_unset_required_fields(query_params))

            return query_params

    class _BaseGetSink:
        def __hash__(self):
            return hash("GetSink")

        __REQUIRED_FIELDS_DEFAULT_VALUES: Dict[str, Any] =  {
        }

        @classmethod
        def _get_unset_required_fields(cls, message_dict):
            return {k: v for k, v in cls.__REQUIRED_FIELDS_DEFAULT_VALUES.items() if k not in message_dict}

        @staticmethod
        def _get_http_options():
            http_options: List[Dict[str, str]] = [{
                'method': 'get',
                'uri': '/v2/{sink_name=*/*/sinks/*}',
            },
        {
                'method': 'get',
                'uri': '/v2/{sink_name=projects/*/sinks/*}',
            },
        {
                'method': 'get',
                'uri': '/v2/{sink_name=organizations/*/sinks/*}',
            },
        {
                'method': 'get',
                'uri': '/v2/{sink_name=folders/*/sinks/*}',
            },
        {
                'method': 'get',
                'uri': '/v2/{sink_name=billingAccounts/*/sinks/*}',
            },
            ]
            return http_options

        @staticmethod
        def _get_transcoded_request(http_options, request):
            pb_request = logging_config.GetSinkRequest.pb(request)
            transcoded_request = path_template.transcode(http_options, pb_request)
            return transcoded_request

        @staticmethod
        def _get_query_params_json(transcoded_request):
            query_params = json.loads(json_format.MessageToJson(
                transcoded_request['query_params'],
                use_integers_for_enums=False,
            ))
            query_params.update(_BaseConfigServiceV2RestTransport._BaseGetSink._get_unset_required_fields(query_params))

            return query_params

    class _BaseGetView:
        def __hash__(self):
            return hash("GetView")

        __REQUIRED_FIELDS_DEFAULT_VALUES: Dict[str, Any] =  {
        }

        @classmethod
        def _get_unset_required_fields(cls, message_dict):
            return {k: v for k, v in cls.__REQUIRED_FIELDS_DEFAULT_VALUES.items() if k not in message_dict}

        @staticmethod
        def _get_http_options():
            http_options: List[Dict[str, str]] = [{
                'method': 'get',
                'uri': '/v2/{name=*/*/locations/*/buckets/*/views/*}',
            },
        {
                'method': 'get',
                'uri': '/v2/{name=projects/*/locations/*/buckets/*/views/*}',
            },
        {
                'method': 'get',
                'uri': '/v2/{name=organizations/*/locations/*/buckets/*/views/*}',
            },
        {
                'method': 'get',
                'uri': '/v2/{name=folders/*/locations/*/buckets/*/views/*}',
            },
        {
                'method': 'get',
                'uri': '/v2/{name=billingAccounts/*/locations/*/buckets/*/views/*}',
            },
            ]
            return http_options

        @staticmethod
        def _get_transcoded_request(http_options, request):
            pb_request = logging_config.GetViewRequest.pb(request)
            transcoded_request = path_template.transcode(http_options, pb_request)
            return transcoded_request

        @staticmethod
        def _get_query_params_json(transcoded_request):
            query_params = json.loads(json_format.MessageToJson(
                transcoded_request['query_params'],
                use_integers_for_enums=False,
            ))
            query_params.update(_BaseConfigServiceV2RestTransport._BaseGetView._get_unset_required_fields(query_params))

            return query_params

    class _BaseListBuckets:
        def __hash__(self):
            return hash("ListBuckets")

        __REQUIRED_FIELDS_DEFAULT_VALUES: Dict[str, Any] =  {
        }

        @classmethod
        def _get_unset_required_fields(cls, message_dict):
            return {k: v for k, v in cls.__REQUIRED_FIELDS_DEFAULT_VALUES.items() if k not in message_dict}

        @staticmethod
        def _get_http_options():
            http_options: List[Dict[str, str]] = [{
                'method': 'get',
                'uri': '/v2/{parent=*/*/locations/*}/buckets',
            },
        {
                'method': 'get',
                'uri': '/v2/{parent=projects/*/locations/*}/buckets',
            },
        {
                'method': 'get',
                'uri': '/v2/{parent=organizations/*/locations/*}/buckets',
            },
        {
                'method': 'get',
                'uri': '/v2/{parent=folders/*/locations/*}/buckets',
            },
        {
                'method': 'get',
                'uri': '/v2/{parent=billingAccounts/*/locations/*}/buckets',
            },
            ]
            return http_options

        @staticmethod
        def _get_transcoded_request(http_options, request):
            pb_request = logging_config.ListBucketsRequest.pb(request)
            transcoded_request = path_template.transcode(http_options, pb_request)
            return transcoded_request

        @staticmethod
        def _get_query_params_json(transcoded_request):
            query_params = json.loads(json_format.MessageToJson(
                transcoded_request['query_params'],
                use_integers_for_enums=False,
            ))
            query_params.update(_BaseConfigServiceV2RestTransport._BaseListBuckets._get_unset_required_fields(query_params))

            return query_params

    class _BaseListExclusions:
        def __hash__(self):
            return hash("ListExclusions")

        __REQUIRED_FIELDS_DEFAULT_VALUES: Dict[str, Any] =  {
        }

        @classmethod
        def _get_unset_required_fields(cls, message_dict):
            return {k: v for k, v in cls.__REQUIRED_FIELDS_DEFAULT_VALUES.items() if k not in message_dict}

        @staticmethod
        def _get_http_options():
            http_options: List[Dict[str, str]] = [{
                'method': 'get',
                'uri': '/v2/{parent=*/*}/exclusions',
            },
        {
                'method': 'get',
                'uri': '/v2/{parent=projects/*}/exclusions',
            },
        {
                'method': 'get',
                'uri': '/v2/{parent=organizations/*}/exclusions',
            },
        {
                'method': 'get',
                'uri': '/v2/{parent=folders/*}/exclusions',
            },
        {
                'method': 'get',
                'uri': '/v2/{parent=billingAccounts/*}/exclusions',
            },
            ]
            return http_options

        @staticmethod
        def _get_transcoded_request(http_options, request):
            pb_request = logging_config.ListExclusionsRequest.pb(request)
            transcoded_request = path_template.transcode(http_options, pb_request)
            return transcoded_request

        @staticmethod
        def _get_query_params_json(transcoded_request):
            query_params = json.loads(json_format.MessageToJson(
                transcoded_request['query_params'],
                use_integers_for_enums=False,
            ))
            query_params.update(_BaseConfigServiceV2RestTransport._BaseListExclusions._get_unset_required_fields(query_params))

            return query_params

    class _BaseListLinks:
        def __hash__(self):
            return hash("ListLinks")

        __REQUIRED_FIELDS_DEFAULT_VALUES: Dict[str, Any] =  {
        }

        @classmethod
        def _get_unset_required_fields(cls, message_dict):
            return {k: v for k, v in cls.__REQUIRED_FIELDS_DEFAULT_VALUES.items() if k not in message_dict}

        @staticmethod
        def _get_http_options():
            http_options: List[Dict[str, str]] = [{
                'method': 'get',
                'uri': '/v2/{parent=*/*/locations/*/buckets/*}/links',
            },
        {
                'method': 'get',
                'uri': '/v2/{parent=projects/*/locations/*/buckets/*}/links',
            },
        {
                'method': 'get',
                'uri': '/v2/{parent=organizations/*/locations/*/buckets/*}/links',
            },
        {
                'method': 'get',
                'uri': '/v2/{parent=folders/*/locations/*/buckets/*}/links',
            },
        {
                'method': 'get',
                'uri': '/v2/{parent=billingAccounts/*/locations/*/buckets/*}/links',
            },
            ]
            return http_options

        @staticmethod
        def _get_transcoded_request(http_options, request):
            pb_request = logging_config.ListLinksRequest.pb(request)
            transcoded_request = path_template.transcode(http_options, pb_request)
            return transcoded_request

        @staticmethod
        def _get_query_params_json(transcoded_request):
            query_params = json.loads(json_format.MessageToJson(
                transcoded_request['query_params'],
                use_integers_for_enums=False,
            ))
            query_params.update(_BaseConfigServiceV2RestTransport._BaseListLinks._get_unset_required_fields(query_params))

            return query_params

    class _BaseListSinks:
        def __hash__(self):
            return hash("ListSinks")

        __REQUIRED_FIELDS_DEFAULT_VALUES: Dict[str, Any] =  {
        }

        @classmethod
        def _get_unset_required_fields(cls, message_dict):
            return {k: v for k, v in cls.__REQUIRED_FIELDS_DEFAULT_VALUES.items() if k not in message_dict}

        @staticmethod
        def _get_http_options():
            http_options: List[Dict[str, str]] = [{
                'method': 'get',
                'uri': '/v2/{parent=*/*}/sinks',
            },
        {
                'method': 'get',
                'uri': '/v2/{parent=projects/*}/sinks',
            },
        {
                'method': 'get',
                'uri': '/v2/{parent=organizations/*}/sinks',
            },
        {
                'method': 'get',
                'uri': '/v2/{parent=folders/*}/sinks',
            },
        {
                'method': 'get',
                'uri': '/v2/{parent=billingAccounts/*}/sinks',
            },
            ]
            return http_options

        @staticmethod
        def _get_transcoded_request(http_options, request):
            pb_request = logging_config.ListSinksRequest.pb(request)
            transcoded_request = path_template.transcode(http_options, pb_request)
            return transcoded_request

        @staticmethod
        def _get_query_params_json(transcoded_request):
            query_params = json.loads(json_format.MessageToJson(
                transcoded_request['query_params'],
                use_integers_for_enums=False,
            ))
            query_params.update(_BaseConfigServiceV2RestTransport._BaseListSinks._get_unset_required_fields(query_params))

            return query_params

    class _BaseListViews:
        def __hash__(self):
            return hash("ListViews")

        __REQUIRED_FIELDS_DEFAULT_VALUES: Dict[str, Any] =  {
        }

        @classmethod
        def _get_unset_required_fields(cls, message_dict):
            return {k: v for k, v in cls.__REQUIRED_FIELDS_DEFAULT_VALUES.items() if k not in message_dict}

        @staticmethod
        def _get_http_options():
            http_options: List[Dict[str, str]] = [{
                'method': 'get',
                'uri': '/v2/{parent=*/*/locations/*/buckets/*}/views',
            },
        {
                'method': 'get',
                'uri': '/v2/{parent=projects/*/locations/*/buckets/*}/views',
            },
        {
                'method': 'get',
                'uri': '/v2/{parent=organizations/*/locations/*/buckets/*}/views',
            },
        {
                'method': 'get',
                'uri': '/v2/{parent=folders/*/locations/*/buckets/*}/views',
            },
        {
                'method': 'get',
                'uri': '/v2/{parent=billingAccounts/*/locations/*/buckets/*}/views',
            },
            ]
            return http_options

        @staticmethod
        def _get_transcoded_request(http_options, request):
            pb_request = logging_config.ListViewsRequest.pb(request)
            transcoded_request = path_template.transcode(http_options, pb_request)
            return transcoded_request

        @staticmethod
        def _get_query_params_json(transcoded_request):
            query_params = json.loads(json_format.MessageToJson(
                transcoded_request['query_params'],
                use_integers_for_enums=False,
            ))
            query_params.update(_BaseConfigServiceV2RestTransport._BaseListViews._get_unset_required_fields(query_params))

            return query_params

    class _BaseUndeleteBucket:
        def __hash__(self):
            return hash("UndeleteBucket")

        __REQUIRED_FIELDS_DEFAULT_VALUES: Dict[str, Any] =  {
        }

        @classmethod
        def _get_unset_required_fields(cls, message_dict):
            return {k: v for k, v in cls.__REQUIRED_FIELDS_DEFAULT_VALUES.items() if k not in message_dict}

        @staticmethod
        def _get_http_options():
            http_options: List[Dict[str, str]] = [{
                'method': 'post',
                'uri': '/v2/{name=*/*/locations/*/buckets/*}:undelete',
                'body': '*',
            },
        {
                'method': 'post',
                'uri': '/v2/{name=projects/*/locations/*/buckets/*}:undelete',
                'body': '*',
            },
        {
                'method': 'post',
                'uri': '/v2/{name=organizations/*/locations/*/buckets/*}:undelete',
                'body': '*',
            },
        {
                'method': 'post',
                'uri': '/v2/{name=folders/*/locations/*/buckets/*}:undelete',
                'body': '*',
            },
        {
                'method': 'post',
                'uri': '/v2/{name=billingAccounts/*/locations/*/buckets/*}:undelete',
                'body': '*',
            },
            ]
            return http_options

        @staticmethod
        def _get_transcoded_request(http_options, request):
            pb_request = logging_config.UndeleteBucketRequest.pb(request)
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
            query_params.update(_BaseConfigServiceV2RestTransport._BaseUndeleteBucket._get_unset_required_fields(query_params))

            return query_params

    class _BaseUpdateBucket:
        def __hash__(self):
            return hash("UpdateBucket")

        __REQUIRED_FIELDS_DEFAULT_VALUES: Dict[str, Any] =  {
            "updateMask" : {},        }

        @classmethod
        def _get_unset_required_fields(cls, message_dict):
            return {k: v for k, v in cls.__REQUIRED_FIELDS_DEFAULT_VALUES.items() if k not in message_dict}

        @staticmethod
        def _get_http_options():
            http_options: List[Dict[str, str]] = [{
                'method': 'patch',
                'uri': '/v2/{name=*/*/locations/*/buckets/*}',
                'body': 'bucket',
            },
        {
                'method': 'patch',
                'uri': '/v2/{name=projects/*/locations/*/buckets/*}',
                'body': 'bucket',
            },
        {
                'method': 'patch',
                'uri': '/v2/{name=organizations/*/locations/*/buckets/*}',
                'body': 'bucket',
            },
        {
                'method': 'patch',
                'uri': '/v2/{name=folders/*/locations/*/buckets/*}',
                'body': 'bucket',
            },
        {
                'method': 'patch',
                'uri': '/v2/{name=billingAccounts/*/locations/*/buckets/*}',
                'body': 'bucket',
            },
            ]
            return http_options

        @staticmethod
        def _get_transcoded_request(http_options, request):
            pb_request = logging_config.UpdateBucketRequest.pb(request)
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
            query_params.update(_BaseConfigServiceV2RestTransport._BaseUpdateBucket._get_unset_required_fields(query_params))

            return query_params

    class _BaseUpdateBucketAsync:
        def __hash__(self):
            return hash("UpdateBucketAsync")

        __REQUIRED_FIELDS_DEFAULT_VALUES: Dict[str, Any] =  {
            "updateMask" : {},        }

        @classmethod
        def _get_unset_required_fields(cls, message_dict):
            return {k: v for k, v in cls.__REQUIRED_FIELDS_DEFAULT_VALUES.items() if k not in message_dict}

        @staticmethod
        def _get_http_options():
            http_options: List[Dict[str, str]] = [{
                'method': 'post',
                'uri': '/v2/{name=*/*/locations/*/buckets/*}:updateAsync',
                'body': 'bucket',
            },
        {
                'method': 'post',
                'uri': '/v2/{name=projects/*/locations/*/buckets/*}:updateAsync',
                'body': 'bucket',
            },
        {
                'method': 'post',
                'uri': '/v2/{name=organizations/*/locations/*/buckets/*}:updateAsync',
                'body': 'bucket',
            },
        {
                'method': 'post',
                'uri': '/v2/{name=folders/*/locations/*/buckets/*}:updateAsync',
                'body': 'bucket',
            },
        {
                'method': 'post',
                'uri': '/v2/{name=billingAccounts/*/locations/*/buckets/*}:updateAsync',
                'body': 'bucket',
            },
            ]
            return http_options

        @staticmethod
        def _get_transcoded_request(http_options, request):
            pb_request = logging_config.UpdateBucketRequest.pb(request)
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
            query_params.update(_BaseConfigServiceV2RestTransport._BaseUpdateBucketAsync._get_unset_required_fields(query_params))

            return query_params

    class _BaseUpdateCmekSettings:
        def __hash__(self):
            return hash("UpdateCmekSettings")

        __REQUIRED_FIELDS_DEFAULT_VALUES: Dict[str, Any] =  {
        }

        @classmethod
        def _get_unset_required_fields(cls, message_dict):
            return {k: v for k, v in cls.__REQUIRED_FIELDS_DEFAULT_VALUES.items() if k not in message_dict}

        @staticmethod
        def _get_http_options():
            http_options: List[Dict[str, str]] = [{
                'method': 'patch',
                'uri': '/v2/{name=*/*}/cmekSettings',
                'body': 'cmek_settings',
            },
        {
                'method': 'patch',
                'uri': '/v2/{name=organizations/*}/cmekSettings',
                'body': 'cmek_settings',
            },
            ]
            return http_options

        @staticmethod
        def _get_transcoded_request(http_options, request):
            pb_request = logging_config.UpdateCmekSettingsRequest.pb(request)
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
            query_params.update(_BaseConfigServiceV2RestTransport._BaseUpdateCmekSettings._get_unset_required_fields(query_params))

            return query_params

    class _BaseUpdateExclusion:
        def __hash__(self):
            return hash("UpdateExclusion")

        __REQUIRED_FIELDS_DEFAULT_VALUES: Dict[str, Any] =  {
            "updateMask" : {},        }

        @classmethod
        def _get_unset_required_fields(cls, message_dict):
            return {k: v for k, v in cls.__REQUIRED_FIELDS_DEFAULT_VALUES.items() if k not in message_dict}

        @staticmethod
        def _get_http_options():
            http_options: List[Dict[str, str]] = [{
                'method': 'patch',
                'uri': '/v2/{name=*/*/exclusions/*}',
                'body': 'exclusion',
            },
        {
                'method': 'patch',
                'uri': '/v2/{name=projects/*/exclusions/*}',
                'body': 'exclusion',
            },
        {
                'method': 'patch',
                'uri': '/v2/{name=organizations/*/exclusions/*}',
                'body': 'exclusion',
            },
        {
                'method': 'patch',
                'uri': '/v2/{name=folders/*/exclusions/*}',
                'body': 'exclusion',
            },
        {
                'method': 'patch',
                'uri': '/v2/{name=billingAccounts/*/exclusions/*}',
                'body': 'exclusion',
            },
            ]
            return http_options

        @staticmethod
        def _get_transcoded_request(http_options, request):
            pb_request = logging_config.UpdateExclusionRequest.pb(request)
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
            query_params.update(_BaseConfigServiceV2RestTransport._BaseUpdateExclusion._get_unset_required_fields(query_params))

            return query_params

    class _BaseUpdateSettings:
        def __hash__(self):
            return hash("UpdateSettings")

        __REQUIRED_FIELDS_DEFAULT_VALUES: Dict[str, Any] =  {
        }

        @classmethod
        def _get_unset_required_fields(cls, message_dict):
            return {k: v for k, v in cls.__REQUIRED_FIELDS_DEFAULT_VALUES.items() if k not in message_dict}

        @staticmethod
        def _get_http_options():
            http_options: List[Dict[str, str]] = [{
                'method': 'patch',
                'uri': '/v2/{name=*/*}/settings',
                'body': 'settings',
            },
        {
                'method': 'patch',
                'uri': '/v2/{name=organizations/*}/settings',
                'body': 'settings',
            },
        {
                'method': 'patch',
                'uri': '/v2/{name=folders/*}/settings',
                'body': 'settings',
            },
            ]
            return http_options

        @staticmethod
        def _get_transcoded_request(http_options, request):
            pb_request = logging_config.UpdateSettingsRequest.pb(request)
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
            query_params.update(_BaseConfigServiceV2RestTransport._BaseUpdateSettings._get_unset_required_fields(query_params))

            return query_params

    class _BaseUpdateSink:
        def __hash__(self):
            return hash("UpdateSink")

        __REQUIRED_FIELDS_DEFAULT_VALUES: Dict[str, Any] =  {
        }

        @classmethod
        def _get_unset_required_fields(cls, message_dict):
            return {k: v for k, v in cls.__REQUIRED_FIELDS_DEFAULT_VALUES.items() if k not in message_dict}

        @staticmethod
        def _get_http_options():
            http_options: List[Dict[str, str]] = [{
                'method': 'put',
                'uri': '/v2/{sink_name=*/*/sinks/*}',
                'body': 'sink',
            },
        {
                'method': 'put',
                'uri': '/v2/{sink_name=projects/*/sinks/*}',
                'body': 'sink',
            },
        {
                'method': 'put',
                'uri': '/v2/{sink_name=organizations/*/sinks/*}',
                'body': 'sink',
            },
        {
                'method': 'put',
                'uri': '/v2/{sink_name=folders/*/sinks/*}',
                'body': 'sink',
            },
        {
                'method': 'put',
                'uri': '/v2/{sink_name=billingAccounts/*/sinks/*}',
                'body': 'sink',
            },
        {
                'method': 'patch',
                'uri': '/v2/{sink_name=projects/*/sinks/*}',
                'body': 'sink',
            },
        {
                'method': 'patch',
                'uri': '/v2/{sink_name=organizations/*/sinks/*}',
                'body': 'sink',
            },
        {
                'method': 'patch',
                'uri': '/v2/{sink_name=folders/*/sinks/*}',
                'body': 'sink',
            },
        {
                'method': 'patch',
                'uri': '/v2/{sink_name=billingAccounts/*/sinks/*}',
                'body': 'sink',
            },
            ]
            return http_options

        @staticmethod
        def _get_transcoded_request(http_options, request):
            pb_request = logging_config.UpdateSinkRequest.pb(request)
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
            query_params.update(_BaseConfigServiceV2RestTransport._BaseUpdateSink._get_unset_required_fields(query_params))

            return query_params

    class _BaseUpdateView:
        def __hash__(self):
            return hash("UpdateView")

        __REQUIRED_FIELDS_DEFAULT_VALUES: Dict[str, Any] =  {
        }

        @classmethod
        def _get_unset_required_fields(cls, message_dict):
            return {k: v for k, v in cls.__REQUIRED_FIELDS_DEFAULT_VALUES.items() if k not in message_dict}

        @staticmethod
        def _get_http_options():
            http_options: List[Dict[str, str]] = [{
                'method': 'patch',
                'uri': '/v2/{name=*/*/locations/*/buckets/*/views/*}',
                'body': 'view',
            },
        {
                'method': 'patch',
                'uri': '/v2/{name=projects/*/locations/*/buckets/*/views/*}',
                'body': 'view',
            },
        {
                'method': 'patch',
                'uri': '/v2/{name=organizations/*/locations/*/buckets/*/views/*}',
                'body': 'view',
            },
        {
                'method': 'patch',
                'uri': '/v2/{name=folders/*/locations/*/buckets/*/views/*}',
                'body': 'view',
            },
        {
                'method': 'patch',
                'uri': '/v2/{name=billingAccounts/*/locations/*/buckets/*/views/*}',
                'body': 'view',
            },
            ]
            return http_options

        @staticmethod
        def _get_transcoded_request(http_options, request):
            pb_request = logging_config.UpdateViewRequest.pb(request)
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
            query_params.update(_BaseConfigServiceV2RestTransport._BaseUpdateView._get_unset_required_fields(query_params))

            return query_params


__all__=(
    '_BaseConfigServiceV2RestTransport',
)

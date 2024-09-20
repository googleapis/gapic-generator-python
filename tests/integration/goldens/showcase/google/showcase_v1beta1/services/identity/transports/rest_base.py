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
from google.api_core import gapic_v1

from google.protobuf import json_format
from google.iam.v1 import iam_policy_pb2  # type: ignore
from google.iam.v1 import policy_pb2  # type: ignore
from google.cloud.location import locations_pb2 # type: ignore
from .base import IdentityTransport, DEFAULT_CLIENT_INFO

import re
from typing import Any, Callable, Dict, List, Optional, Sequence, Tuple, Union


from google.protobuf import empty_pb2  # type: ignore
from google.showcase_v1beta1.types import identity
from google.longrunning import operations_pb2  # type: ignore


class _BaseIdentityRestTransport(IdentityTransport):
    """Base REST backend transport for Identity.

    Note: This class is not meant to be used directly. Use its sync and
    async sub-classes instead.

    This class defines the same methods as the primary client, so the
    primary client can load the underlying transport implementation
    and call it.

    It sends JSON representations of protocol buffers over HTTP/1.1
    """

    def __init__(self, *,
            host: str = 'localhost:7469',
            credentials: Optional[Any] = None,
            client_info: gapic_v1.client_info.ClientInfo = DEFAULT_CLIENT_INFO,
            always_use_jwt_access: Optional[bool] = False,
            url_scheme: str = 'https',
            api_audience: Optional[str] = None,
            ) -> None:
        """Instantiate the transport.
        Args:
            host (Optional[str]):
                 The hostname to connect to (default: 'localhost:7469').
            credentials (Optional[Any]): The
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

    class _BaseCreateUser:
        def __hash__(self):  # pragma: NO COVER
            return NotImplementedError("__hash__ must be implemented.")

        @staticmethod
        def _get_http_options():
            http_options: List[Dict[str, str]] = [{
                'method': 'post',
                'uri': '/v1beta1/users',
                'body': '*',
            },
            ]
            return http_options

        @staticmethod
        def _get_transcoded_request(http_options, request):
            pb_request = identity.CreateUserRequest.pb(request)
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

            return query_params

    class _BaseDeleteUser:
        def __hash__(self):  # pragma: NO COVER
            return NotImplementedError("__hash__ must be implemented.")

        __REQUIRED_FIELDS_DEFAULT_VALUES: Dict[str, Any] =  {
        }

        @classmethod
        def _get_unset_required_fields(cls, message_dict):
            return {k: v for k, v in cls.__REQUIRED_FIELDS_DEFAULT_VALUES.items() if k not in message_dict}

        @staticmethod
        def _get_http_options():
            http_options: List[Dict[str, str]] = [{
                'method': 'delete',
                'uri': '/v1beta1/{name=users/*}',
            },
            ]
            return http_options

        @staticmethod
        def _get_transcoded_request(http_options, request):
            pb_request = identity.DeleteUserRequest.pb(request)
            transcoded_request = path_template.transcode(http_options, pb_request)
            return transcoded_request

        @staticmethod
        def _get_query_params_json(transcoded_request):
            query_params = json.loads(json_format.MessageToJson(
                transcoded_request['query_params'],
                use_integers_for_enums=False,
            ))
            query_params.update(_BaseIdentityRestTransport._BaseDeleteUser._get_unset_required_fields(query_params))

            return query_params

    class _BaseGetUser:
        def __hash__(self):  # pragma: NO COVER
            return NotImplementedError("__hash__ must be implemented.")

        __REQUIRED_FIELDS_DEFAULT_VALUES: Dict[str, Any] =  {
        }

        @classmethod
        def _get_unset_required_fields(cls, message_dict):
            return {k: v for k, v in cls.__REQUIRED_FIELDS_DEFAULT_VALUES.items() if k not in message_dict}

        @staticmethod
        def _get_http_options():
            http_options: List[Dict[str, str]] = [{
                'method': 'get',
                'uri': '/v1beta1/{name=users/*}',
            },
            ]
            return http_options

        @staticmethod
        def _get_transcoded_request(http_options, request):
            pb_request = identity.GetUserRequest.pb(request)
            transcoded_request = path_template.transcode(http_options, pb_request)
            return transcoded_request

        @staticmethod
        def _get_query_params_json(transcoded_request):
            query_params = json.loads(json_format.MessageToJson(
                transcoded_request['query_params'],
                use_integers_for_enums=False,
            ))
            query_params.update(_BaseIdentityRestTransport._BaseGetUser._get_unset_required_fields(query_params))

            return query_params

    class _BaseListUsers:
        def __hash__(self):  # pragma: NO COVER
            return NotImplementedError("__hash__ must be implemented.")

        @staticmethod
        def _get_http_options():
            http_options: List[Dict[str, str]] = [{
                'method': 'get',
                'uri': '/v1beta1/users',
            },
            ]
            return http_options

        @staticmethod
        def _get_transcoded_request(http_options, request):
            pb_request = identity.ListUsersRequest.pb(request)
            transcoded_request = path_template.transcode(http_options, pb_request)
            return transcoded_request

        @staticmethod
        def _get_query_params_json(transcoded_request):
            query_params = json.loads(json_format.MessageToJson(
                transcoded_request['query_params'],
                use_integers_for_enums=False,
            ))

            return query_params

    class _BaseUpdateUser:
        def __hash__(self):  # pragma: NO COVER
            return NotImplementedError("__hash__ must be implemented.")

        @staticmethod
        def _get_http_options():
            http_options: List[Dict[str, str]] = [{
                'method': 'patch',
                'uri': '/v1beta1/{user.name=users/*}',
                'body': 'user',
            },
            ]
            return http_options

        @staticmethod
        def _get_transcoded_request(http_options, request):
            pb_request = identity.UpdateUserRequest.pb(request)
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

            return query_params

    class _BaseListLocations:

        @staticmethod
        def _get_http_options():
            http_options: List[Dict[str, str]] = [{
                'method': 'get',
                'uri': '/v1beta1/{name=projects/*}/locations',
            },
            ]
            return http_options

        @staticmethod
        def _get_transcoded_request(http_options, request):
            request_kwargs = json_format.MessageToDict(request)
            transcoded_request = path_template.transcode(
                http_options, **request_kwargs)
            return transcoded_request

        @staticmethod
        def _get_query_params_json(transcoded_request):
            query_params = json.loads(json.dumps(transcoded_request['query_params']))
            return query_params

    class _BaseGetLocation:

        @staticmethod
        def _get_http_options():
            http_options: List[Dict[str, str]] = [{
                'method': 'get',
                'uri': '/v1beta1/{name=projects/*/locations/*}',
            },
            ]
            return http_options

        @staticmethod
        def _get_transcoded_request(http_options, request):
            request_kwargs = json_format.MessageToDict(request)
            transcoded_request = path_template.transcode(
                http_options, **request_kwargs)
            return transcoded_request

        @staticmethod
        def _get_query_params_json(transcoded_request):
            query_params = json.loads(json.dumps(transcoded_request['query_params']))
            return query_params

    class _BaseSetIamPolicy:

        @staticmethod
        def _get_http_options():
            http_options: List[Dict[str, str]] = [{
                'method': 'post',
                'uri': '/v1beta1/{resource=users/*}:setIamPolicy',
                'body': '*',
            },
        {
                'method': 'post',
                'uri': '/v1beta1/{resource=rooms/*}:setIamPolicy',
                'body': '*',
            },
        {
                'method': 'post',
                'uri': '/v1beta1/{resource=rooms/*/blurbs/*}:setIamPolicy',
                'body': '*',
            },
        {
                'method': 'post',
                'uri': '/v1beta1/{resource=sequences/*}:setIamPolicy',
                'body': '*',
            },
            ]
            return http_options

        @staticmethod
        def _get_transcoded_request(http_options, request):
            request_kwargs = json_format.MessageToDict(request)
            transcoded_request = path_template.transcode(
                http_options, **request_kwargs)
            return transcoded_request

        @staticmethod
        def _get_request_body_json(transcoded_request):
            body = json.dumps(transcoded_request['body'])
            return body
        @staticmethod
        def _get_query_params_json(transcoded_request):
            query_params = json.loads(json.dumps(transcoded_request['query_params']))
            return query_params

    class _BaseGetIamPolicy:

        @staticmethod
        def _get_http_options():
            http_options: List[Dict[str, str]] = [{
                'method': 'get',
                'uri': '/v1beta1/{resource=users/*}:getIamPolicy',
            },
        {
                'method': 'get',
                'uri': '/v1beta1/{resource=rooms/*}:getIamPolicy',
            },
        {
                'method': 'get',
                'uri': '/v1beta1/{resource=rooms/*/blurbs/*}:getIamPolicy',
            },
        {
                'method': 'get',
                'uri': '/v1beta1/{resource=sequences/*}:getIamPolicy',
            },
            ]
            return http_options

        @staticmethod
        def _get_transcoded_request(http_options, request):
            request_kwargs = json_format.MessageToDict(request)
            transcoded_request = path_template.transcode(
                http_options, **request_kwargs)
            return transcoded_request

        @staticmethod
        def _get_query_params_json(transcoded_request):
            query_params = json.loads(json.dumps(transcoded_request['query_params']))
            return query_params

    class _BaseTestIamPermissions:

        @staticmethod
        def _get_http_options():
            http_options: List[Dict[str, str]] = [{
                'method': 'post',
                'uri': '/v1beta1/{resource=users/*}:testIamPermissions',
                'body': '*',
            },
        {
                'method': 'post',
                'uri': '/v1beta1/{resource=rooms/*}:testIamPermissions',
                'body': '*',
            },
        {
                'method': 'post',
                'uri': '/v1beta1/{resource=rooms/*/blurbs/*}:testIamPermissions',
                'body': '*',
            },
        {
                'method': 'post',
                'uri': '/v1beta1/{resource=sequences/*}:testIamPermissions',
                'body': '*',
            },
            ]
            return http_options

        @staticmethod
        def _get_transcoded_request(http_options, request):
            request_kwargs = json_format.MessageToDict(request)
            transcoded_request = path_template.transcode(
                http_options, **request_kwargs)
            return transcoded_request

        @staticmethod
        def _get_request_body_json(transcoded_request):
            body = json.dumps(transcoded_request['body'])
            return body
        @staticmethod
        def _get_query_params_json(transcoded_request):
            query_params = json.loads(json.dumps(transcoded_request['query_params']))
            return query_params

    class _BaseListOperations:

        @staticmethod
        def _get_http_options():
            http_options: List[Dict[str, str]] = [{
                'method': 'get',
                'uri': '/v1beta1/operations',
            },
            ]
            return http_options

        @staticmethod
        def _get_transcoded_request(http_options, request):
            request_kwargs = json_format.MessageToDict(request)
            transcoded_request = path_template.transcode(
                http_options, **request_kwargs)
            return transcoded_request

        @staticmethod
        def _get_query_params_json(transcoded_request):
            query_params = json.loads(json.dumps(transcoded_request['query_params']))
            return query_params

    class _BaseGetOperation:

        @staticmethod
        def _get_http_options():
            http_options: List[Dict[str, str]] = [{
                'method': 'get',
                'uri': '/v1beta1/{name=operations/**}',
            },
            ]
            return http_options

        @staticmethod
        def _get_transcoded_request(http_options, request):
            request_kwargs = json_format.MessageToDict(request)
            transcoded_request = path_template.transcode(
                http_options, **request_kwargs)
            return transcoded_request

        @staticmethod
        def _get_query_params_json(transcoded_request):
            query_params = json.loads(json.dumps(transcoded_request['query_params']))
            return query_params

    class _BaseDeleteOperation:

        @staticmethod
        def _get_http_options():
            http_options: List[Dict[str, str]] = [{
                'method': 'delete',
                'uri': '/v1beta1/{name=operations/**}',
            },
            ]
            return http_options

        @staticmethod
        def _get_transcoded_request(http_options, request):
            request_kwargs = json_format.MessageToDict(request)
            transcoded_request = path_template.transcode(
                http_options, **request_kwargs)
            return transcoded_request

        @staticmethod
        def _get_query_params_json(transcoded_request):
            query_params = json.loads(json.dumps(transcoded_request['query_params']))
            return query_params

    class _BaseCancelOperation:

        @staticmethod
        def _get_http_options():
            http_options: List[Dict[str, str]] = [{
                'method': 'post',
                'uri': '/v1beta1/{name=operations/**}:cancel',
            },
            ]
            return http_options

        @staticmethod
        def _get_transcoded_request(http_options, request):
            request_kwargs = json_format.MessageToDict(request)
            transcoded_request = path_template.transcode(
                http_options, **request_kwargs)
            return transcoded_request

        @staticmethod
        def _get_query_params_json(transcoded_request):
            query_params = json.loads(json.dumps(transcoded_request['query_params']))
            return query_params


__all__=(
    '_BaseIdentityRestTransport',
)

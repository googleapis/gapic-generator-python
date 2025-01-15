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
from collections import OrderedDict
from typing import Dict, Type, Tuple

from .base import IdentityTransport
from .grpc import IdentityGrpcTransport
from .grpc_asyncio import IdentityGrpcAsyncIOTransport
from .rest import IdentityRestTransport
from .rest import IdentityRestInterceptor
ASYNC_REST_CLASSES: Tuple[str, ...]
try:
    from .rest_asyncio import AsyncIdentityRestTransport
    from .rest_asyncio import AsyncIdentityRestInterceptor
    ASYNC_REST_CLASSES = ('AsyncIdentityRestTransport', 'AsyncIdentityRestInterceptor')
    HAS_REST_ASYNC = True
except ImportError:  # pragma: NO COVER
    ASYNC_REST_CLASSES = ()
    HAS_REST_ASYNC = False


# Compile a registry of transports.
_transport_registry = OrderedDict()  # type: Dict[str, Type[IdentityTransport]]
_transport_registry['grpc'] = IdentityGrpcTransport
_transport_registry['grpc_asyncio'] = IdentityGrpcAsyncIOTransport
_transport_registry['rest'] = IdentityRestTransport
if HAS_REST_ASYNC:  # pragma: NO COVER
    _transport_registry['rest_asyncio'] = AsyncIdentityRestTransport

__all__ = (
    'IdentityTransport',
    'IdentityGrpcTransport',
    'IdentityGrpcAsyncIOTransport',
    'IdentityRestTransport',
    'IdentityRestInterceptor',
) + ASYNC_REST_CLASSES
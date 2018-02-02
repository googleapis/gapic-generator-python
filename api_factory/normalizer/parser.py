# Copyright 2018 Google LLC
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     https://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

from datetime import datetime
import functools
import io
import json

from api_factory.normalizer import license
from api_factory.normalizer import schema


@functools.singledispatch
def parse(service: schema.service_pb2.Service) -> schema.APIDescriptor:
    """Return an API representation parsed from a APIDescriptor object."""
    # This is a placeholder; this is not in any way
    # the appropriate intermediate presentation.
    return schema.APIDescriptor(
        copyright=schema.Copyright(
            label='Google LLC',
            license=schema.License(
                boilerplate_notice=license.APACHE_BOILERPLATE,
                full_text=license.APACHE_FULL,
                label='Apache 2.0',
            ),
            year=str(datetime.now().year),
        ),
        service_config=service,
    )


@parse.register(dict)
def parse_dict(service: dict) -> schema.APIDescriptor:
    return parse(schema.service_pb2.Service(**service))


@parse.register(bytes)
def parse_descriptor(desc: bytes) -> schema.APIDescriptor:
    return parse(schema.service_pb2.Service.FromString(desc))


@parse.register(str)
def parse_filename(filename: str) -> schema.APIDescriptor:
    with io.open(filename, 'rb') as data:
        if filename.endswith('.json'):
            return parse_dict(json.loads(data.read()))
        return parse_descriptor(data.read())

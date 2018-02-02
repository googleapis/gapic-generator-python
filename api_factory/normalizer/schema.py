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

import dataclasses
import typing

from google.api import service_pb2

from api_factory import utils


@dataclasses.dataclass
class License:
    label: str
    full_text: str
    boilerplate_notice: str = ''


@dataclasses.dataclass
class Copyright:
    label: str
    year: str
    license: License
    email: str = ''


@dataclasses.dataclass
class MessageDesc:
    import_path: str
    label: str

    def __str__(self):
        return self.label


@dataclasses.dataclass
class RPC:
    label: str
    endpoint: str
    input_type: MessageDesc
    return_type: MessageDesc
    documentation: str = ''


@dataclasses.dataclass
class Service:
    label: str
    version: str = ''
    documentation: str = ''
    auth_scopes: typing.Set[str] = dataclasses.field(default_factory=set)
    rpcs: typing.List[RPC] = dataclasses.field(default_factory=list)


@dataclasses.dataclass
class APIDescriptor:
    service_config: service_pb2.Service
    copyright: Copyright

    @utils.cached_property
    def services(self) -> typing.Sequence[Service]:
        """Return a list of objects describing each API service."""
        # The term "service" here is a one-to-one correlation with the
        # service keyword in proto3, and *not* correlated to the
        # "service config". These terms are unfortunately overloaded and need
        # to be disambiguated.
        answer = []
        for raw in self.service_config.apis:
            auth_scopes = set()

            # Iterate over each of the methods and create an RPC object
            # for each.
            rpcs = []
            for method in raw.methods:
                # Append the auth scopes needed for this RPC to the overall
                # list. We do not keep this on a per-method basis; we just
                # use the union of scopes needed on the service.
                canonical_scopes = utils.find_in_sequence(
                    self.service_config.authentication.rules,
                    lambda r: r.selector.endswith(f'.{method.name}'),
                ).oauth.canonical_scopes
                for scope in canonical_scopes.split(','):
                    auth_scopes.add(scope.strip())

                # Append the description of the RPC overall to the list.
                rpcs.append(RPC(
                    documentation=utils.find_in_sequence(
                        self.service_config.documentation.rules,
                        lambda r: r.selector == f'{raw.name}.{method.name}',
                    ).description,
                    endpoint=f'/{raw.name}/{method.name}',
                    input_type=self.get_message(method.request_type_url),
                    label=method.name,
                    return_type=self.get_message(method.response_type_url),
                ))

            # Add my custom service object.
            answer.append(Service(
                auth_scopes=auth_scopes,
                documentation=utils.find_in_sequence(
                    self.service_config.documentation.rules,
                    lambda r: r.selector == raw.name,
                ).description,
                label=raw.name.split('.')[-1],
                rpcs=rpcs,
                version=raw.version,
            ))
        return answer

    @utils.cached_property
    def types(self) -> typing.Mapping[str, dict]:
        """Return a dictionary mapping of types."""
        answer = {}
        for t in self.service_config.types:
            answer[t.name] = t
        return answer

    def get_message(self, type_url: str):
            """Return an object describing the provided type URL.

            Args:
                type_url (str): A URL in the form of
                    type.googleapis.com/{import_path}/{class_name}

            Returns:
                MessageDesc: A description of the given message.
            """
            api_type = self.types[type_url.split('/')[1]]

            # Determine the correct import path, which is not contained in
            # a single place.
            # FIXME: This is dependent on where protoc puts things; make that
            # aspect better.
            src = api_type.source_context.file_name
            import_path = '{prefix}.{pb2}_pb2'.format(
                prefix='.'.join(api_type.name.split('.')[:-1]),
                pb2=src.split('/')[-1][:-len('.proto')]
            )

            # Return the description of the message.
            return MessageDesc(
                import_path=import_path,
                label=type_url.split('.')[-1],
            )

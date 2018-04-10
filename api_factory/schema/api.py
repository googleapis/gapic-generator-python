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

import collections
import dataclasses
import sys
from typing import Callable, List, Mapping

from google.protobuf import descriptor_pb2

from api_factory import utils
from api_factory.schema import metadata
from api_factory.schema import wrappers
from api_factory.schema.pb import client_pb2


@dataclasses.dataclass
class API:
    """A representation of a full API.

    An instance of this object is made available to every template
    (as ``api``); all data goes here.
    """
    client: client_pb2.Client = client_pb2.Client()
    services: Mapping[str, wrappers.Service] = dataclasses.field(
        default_factory=dict,
    )
    messages: Mapping[str, wrappers.MessageType] = dataclasses.field(
        default_factory=dict,
    )
    enums: Mapping[str, wrappers.EnumType] = dataclasses.field(
        default_factory=dict,
    )

    @property
    def long_name(self):
        """Return an appropriate title-cased long name."""
        return ' '.join(list(self.client.namespace) + [self.client.name])

    @property
    def warehouse_package_name(self):
        """Return the appropriate Python package name for Warehouse."""
        # Sanity check: If no name is provided, use a clearly placeholder
        # default that is not a valid name on Warehouse.
        if not self.client.name:
            return utils.E('<<< PACKAGE NAME >>>')

        # Piece the name and namespace together to come up with the
        # proper package name.
        answer = list(self.client.namespace) + [self.client.name]
        return '-'.join(answer).lower()

    def load(self, fdp: descriptor_pb2.FileDescriptorProto) -> None:
        """Load the provided FileDescriptorProto into this object.

        This method wraps Map as required, and recusrively
        parses through the descriptor.

        Args:
            fdp (~.descriptor_pb2.FileDescriptorProto): The
                :class:`FileDescriptorProto` object; this is usually provided
                as a list in :class:`CodeGeneratorRequest`.
        """
        # Compile together the comments from the source code.
        # This creates a nested diciontary structure sorted by the
        # location paths. So, a location with path [4, 1, 2, 7] will end
        # up being in `source_docs` under [4][1][2][7]['TERMINAL'].
        #
        # The purpose of always ending with 'TERMINAL' is because there
        # always could be something nested deeper.
        comments_by_path = {}
        for loc in fdp.source_code_info.location:
            cursor = comments_by_path
            for p in loc.path:
                cursor.setdefault(p, {})
                cursor = cursor[p]
            cursor['TERMINAL'] = loc

        # Now iterate over the FileDescriptorProto and grab the relevant
        # source documentation from the dictionary created above and
        # add this to the `self.comments` dictionary, which is sorted by
        # fully-qualfied proto identifiers.
        #
        # The hard-coded keys here are based on how descriptor.proto
        # works; it uses the proto message number of the pieces of each
        # message (e.g. the hard-code `4` for `message_type` immediately
        # below is because `repeated DescriptorProto message_type = 4;` in
        # descriptor.proto itself).
        address = metadata.Address(
            module=fdp.name.split('/')[-1][:-len('.proto')],
            package=fdp.package.split('.'),
        )
        self._load_children(fdp.message_type, loader=self._load_descriptor,
                            address=address, info=comments_by_path.get(4, {}))
        self._load_children(fdp.enum_type, loader=self._load_enum,
                            address=address, info=comments_by_path.get(5, {}))
        self._load_children(fdp.service, loader=self._load_service,
                            address=address, info=comments_by_path.get(6, {}))
        # self._load_children(fdp.extension, loader=self._load_field,
        #                   address=address, info=comments_by_path.get(7, {}))

        # If the FileDescriptorProto has a Client object, save it.
        if fdp.options.Extensions[client_pb2.client]:
            self.client = fdp.options.Extensions[client_pb2.client]

    def _load_children(self, children: list, loader: Callable,
                       address: metadata.Address, info: dict) -> None:
        """Load arbitrary children from a Descriptor.

        Args:
            children (list): A sequence of children of the given field to
                be loaded. For example, a FileDescriptorProto contains the
                lists ``message_type``, ``enum_type``, etc.; these are valid
                inputs for this argument.
            loader (Callable[Message, prefix, dict]): The function able
                to load the kind of message in ``children``. This should
                be one of the ``_load_{noun}`` methods on this class
                (e.g. ``_load_descriptor``).
            prefix (str): The protocol buffer qualified namespace up to this
                point. This will include the package and may include outer
                messages. Note that the proto file name is not part of the
                prefix.
            info (dict): A dictionary of comment information corresponding to
                the messages for which being laoded. In other words, this is
                the segment of the source info that has paths matching
                or within ``children``.
        """
        # Iterate over the list of children provided and call the
        # applicable loader function on each.
        for child, i in zip(children, range(0, sys.maxsize)):
            loader(child, address=address, info=info.get(i, {}))

    def _get_fields(self, fields: List[descriptor_pb2.FieldDescriptorProto],
                    address: metadata.Address, info: dict,
                    ) -> Mapping[str, wrappers.Field]:
        """Return a dictionary of wrapped fields for the given message.

        Args:
        """
        # Iterate over the fields and collect them into a dictionary.
        answer = collections.OrderedDict()
        for field_pb, i in zip(fields, range(0, sys.maxsize)):
            answer[field_pb.name] = wrappers.Field(
                field_pb=field_pb,
                meta=metadata.Metadata(
                    address=address,
                    documentation=info.get(i, {}).get(
                        'TERMINAL',
                        descriptor_pb2.SourceCodeInfo.Location(),
                    ),
                ),
            )

        # Done; return the answer.
        return answer

    def _get_methods(self, methods: List[descriptor_pb2.MethodDescriptorProto],
                     address: metadata.Address, info: dict,
                     ) -> Mapping[str, wrappers.Method]:
        """Return a dictionary of wrapped methods for the given service.

        Args:
        """
        # Iterate over the methods and collect them into a dictionary.
        answer = collections.OrderedDict()
        for method_pb, i in zip(methods, range(0, sys.maxsize)):
            answer[method_pb.name] = wrappers.Method(
                input=self.messages[method_pb.input_type.lstrip('.')],
                method_pb=method_pb,
                meta=metadata.Metadata(
                    address=address,
                    documentation=info.get(i, {}).get(
                        'TERMINAL',
                        descriptor_pb2.SourceCodeInfo.Location(),
                    ),
                ),
                output=self.messages[method_pb.output_type.lstrip('.')],
            )

        # Done; return the answer.
        return answer

    def _load_descriptor(self, message: descriptor_pb2.DescriptorProto,
                         address: metadata.Address, info: dict) -> None:
        """Load message descriptions from DescriptorProtos."""
        ident = f'{str(address)}.{message.name}'
        nested_addr = address.child(message.name)

        # Create a dictionary of all the fields for this message.
        fields = self._get_fields(
            message.field,
            address=nested_addr,
            info=info.get(2, {}),
        )
        fields.update(self._get_fields(
            message.extension,
            address=nested_addr,
            info=info.get(6, {}),
        ))

        # Create a message correspoding to this descriptor.
        self.messages[ident] = wrappers.MessageType(
            fields=fields,
            message_pb=message,
            meta=metadata.Metadata(address=address, documentation=info.get(
                'TERMINAL',
                descriptor_pb2.SourceCodeInfo.Location(),
            )),
        )

        # Load all nested items.
        self._load_children(message.nested_type, loader=self._load_descriptor,
                            address=nested_addr, info=info.get(3, {}))
        self._load_children(message.enum_type, loader=self._load_enum,
                            address=nested_addr, info=info.get(4, {}))
        # self._load_children(message.oneof_decl, loader=self._load_field,
        #                     address=nested_addr, info=info.get(8, {}))

    def _load_enum(self, enum: descriptor_pb2.EnumDescriptorProto,
                   address: metadata.Address, info: dict) -> None:
        """Load enum descriptions from EnumDescriptorProtos."""
        # Put together wrapped objects for the enum values.
        values = []
        for enum_value, i in zip(enum.value, range(0, sys.maxsize)):
            values.append(wrappers.EnumValueType(
                enum_value_pb=enum_value,
                meta=metadata.Metadata(
                    address=address,
                    documentation=info.get(2, {}).get(
                        'TERMINAL',
                        descriptor_pb2.SourceCodeInfo.Location(),
                    ),
                ),
            ))

        # Load the enum itself.
        ident = f'{str(address)}.{enum.name}'
        self.enums[ident] = wrappers.EnumType(
            enum_pb=enum,
            meta=metadata.Metadata(address=address, documentation=info.get(
                'TERMINAL',
                descriptor_pb2.SourceCodeInfo.Location(),
            )),
            values=values,
        )

    def _load_service(self, service: descriptor_pb2.ServiceDescriptorProto,
                      address: metadata.Address, info: dict) -> None:
        """Load comments for a service and its methods."""
        service_addr = address.child(service.name)

        # Put together a dictionary of the service's methods.
        methods = self._get_methods(
            service.method,
            address=service_addr,
            info=info.get(2, {}),
        )

        # Load the comments for the service itself.
        self.services[service.name] = wrappers.Service(
            meta=metadata.Metadata(address=address, documentation=info.get(
                'TERMINAL',
                descriptor_pb2.SourceCodeInfo.Location(),
            )),
            methods=methods,
            service_pb=service,
        )
